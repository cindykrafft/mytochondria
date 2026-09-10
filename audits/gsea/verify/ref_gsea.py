#!/usr/bin/env python3
"""Independent numpy port of the GSEA statistics, written from Subramanian et al. (2005,
PNAS 102:15545; Methods "Enrichment score", "Estimating significance", "Multiple hypothesis
testing" and the supplementary appendix), NOT from the Java code.

Used as the reference for every harness in this directory.  Nothing here reads GSEA's
output; the harnesses call these functions on the same synthetic inputs they hand to the
shipped jar and compare.

Conventions: a ranked list is (names: list[str], scores: np.ndarray) sorted descending
(ties in input order, as the .rnk parser keeps them).  A gene set is a set of names; only
members present in the ranked list count (the Java code qualifies sets the same way).
"""
import numpy as np


# ----------------------------------------------------------------------------- ES
def enrichment_score(scores, hit_mask, p=1.0):
    """Running-sum ES of the paper (eq. in Methods).  P_hit(S,i) = sum_{hits<=i} |r|^p / N_R,
    P_miss(S,i) = #misses<=i / (N - N_H).  ES = the running sum value with the largest |.|
    (first occurrence).  Returns (es, rank_at_es(0-based), running_sum)."""
    scores = np.asarray(scores, dtype=np.float64)
    hit_mask = np.asarray(hit_mask, dtype=bool)
    N = scores.size
    NH = int(hit_mask.sum())
    if NH == 0 or NH == N:
        raise ValueError("gene set must have between 1 and N-1 members in the list")
    w = np.abs(scores) ** p
    NR = w[hit_mask].sum()
    inc = np.where(hit_mask, w / NR, -1.0 / (N - NH))
    rs = np.cumsum(inc)
    i = int(np.argmax(np.abs(rs)))          # first index of the max |running sum|
    return float(rs[i]), i, rs


def leading_edge(scores, hit_mask, p=1.0):
    """Members at or before the ES peak (positive ES) / at or after it (negative)."""
    es, i, _ = enrichment_score(scores, hit_mask, p)
    idx = np.flatnonzero(hit_mask)
    return (idx[idx <= i] if es >= 0 else idx[idx >= i]), es, i


# ----------------------------------------------------------------------------- null
def nes_meandiv(es, rnd_es):
    """NES = ES / mean of the same-sign portion of the null (paper: 'normalizing ... by the
    mean of the positive or negative ES values of the permutations')."""
    rnd_es = np.asarray(rnd_es, dtype=np.float64)
    same = rnd_es[rnd_es >= 0] if es >= 0 else rnd_es[rnd_es < 0]
    return es / abs(same.mean()) if same.size else np.nan


def nominal_p(es, rnd_es):
    """Fraction of the same-sign null strictly more extreme than ES (the code's
    convention; the paper says 'the portion of the distribution corresponding to the
    sign of the observed ES')."""
    rnd_es = np.asarray(rnd_es, dtype=np.float64)
    if es >= 0:
        same = rnd_es[rnd_es >= 0]
        return float((same > es).sum() / same.size) if same.size else np.nan
    same = rnd_es[rnd_es < 0]
    return float((same < es).sum() / same.size) if same.size else np.nan


def fdr_paper(nes_real, nes_rnd):
    """FDR q-values as defined in the paper's supplement: for NES* >= 0,
    q = [% of all (S, pi) with NES(S,pi) >= 0 that have NES(S,pi) >= NES*]
      / [% of observed S with NES(S) >= 0 that have NES(S) >= NES*],
    pooled over every permutation; symmetric for NES* < 0.  nes_rnd is (sets x perms)."""
    nes_real = np.asarray(nes_real, dtype=np.float64)
    nes_rnd = np.asarray(nes_rnd, dtype=np.float64)
    out = np.full(nes_real.shape, np.nan)
    pos_rnd = nes_rnd[nes_rnd >= 0]
    neg_rnd = nes_rnd[nes_rnd < 0]
    pos_real = nes_real[nes_real >= 0]
    neg_real = nes_real[nes_real < 0]
    for k, v in enumerate(nes_real):
        if np.isnan(v):
            continue
        if v >= 0:
            num = (pos_rnd >= v).sum() / pos_rnd.size
            den = (pos_real >= v).sum() / pos_real.size
        else:
            num = (neg_rnd <= v).sum() / neg_rnd.size
            den = (neg_real <= v).sum() / neg_real.size
        out[k] = min(1.0, num / den)
    return out


def fdr_gsea_code(nes_real, nes_rnd):
    """What the Java code computes (SkewCorrectedFdrStruc): the numerator is the MEAN over
    permutation columns of the per-column fraction (#{NES(S,pi) >= NES*} / #{NES(S,pi) >= 0}
    within that column), columns with no same-sign value skipped; the denominator is the
    observed fraction as in the paper."""
    nes_real = np.asarray(nes_real, dtype=np.float64)
    nes_rnd = np.asarray(nes_rnd, dtype=np.float64)
    out = np.full(nes_real.shape, np.nan)
    pos_real = nes_real[nes_real >= 0]
    neg_real = nes_real[nes_real < 0]
    for k, v in enumerate(nes_real):
        if np.isnan(v):
            continue
        fr = []
        for c in range(nes_rnd.shape[1]):
            col = nes_rnd[:, c]
            same = col[col >= 0] if v >= 0 else col[col < 0]
            if same.size == 0:
                continue
            fr.append(((same >= v).sum() if v >= 0 else (same <= v).sum()) / same.size)
        num = float(np.mean(fr))
        den = ((pos_real >= v).sum() / pos_real.size) if v >= 0 else ((neg_real <= v).sum() / neg_real.size)
        out[k] = min(1.0, num / den)
    return out


def fwer(nes_real, nes_rnd):
    """Family-wise error: fraction of permutations whose most extreme same-sign NES over all
    sets is more extreme than NES*."""
    nes_real = np.asarray(nes_real, dtype=np.float64)
    nes_rnd = np.asarray(nes_rnd, dtype=np.float64)
    colmax = np.nanmax(nes_rnd, axis=0)
    colmin = np.nanmin(nes_rnd, axis=0)
    out = np.empty(nes_real.shape)
    for k, v in enumerate(nes_real):
        out[k] = (colmax > v).mean() if v >= 0 else (colmin < v).mean()
    return out


# ----------------------------------------------------------------------------- metrics
def _sd_floor(x, fixlow=True, biased=False):
    x = np.asarray(x, dtype=np.float64)
    mu = x.mean()
    sd = x.std(ddof=0 if biased else 1)
    if fixlow:
        floor = 0.2 if abs(mu) <= 1e-9 else 0.2 * abs(mu)
        sd = max(sd, floor)
    return mu, sd


def signal2noise(a, b, fixlow=True, biased=False):
    """(mu_A - mu_B) / (sd_A + sd_B); GSEA's minimum-sd rule sd >= 0.2*|mu| (0.2 at mu=0)."""
    ma, sa = _sd_floor(a, fixlow, biased)
    mb, sb = _sd_floor(b, fixlow, biased)
    return (ma - mb) / (sa + sb)


def ttest(a, b, fixlow=True, biased=False):
    """(mu_A - mu_B) / sqrt(sd_A^2/n_A + sd_B^2/n_B) with the same sd floor."""
    ma, sa = _sd_floor(a, fixlow, biased)
    mb, sb = _sd_floor(b, fixlow, biased)
    return (ma - mb) / np.sqrt(sa ** 2 / len(a) + sb ** 2 / len(b))


def ratio_of_classes(a, b):
    return np.mean(a) / np.mean(b)


def log2_ratio_of_classes(a, b):
    return np.log2(np.mean(a) / np.mean(b))


def diff_of_classes(a, b):
    return np.mean(a) - np.mean(b)


METRICS = {"Signal2Noise": signal2noise, "tTest": ttest, "Ratio_of_Classes": ratio_of_classes,
           "log2_Ratio_of_Classes": log2_ratio_of_classes, "Diff_of_Classes": diff_of_classes}


def rank_dataset(X, labels, metric="Signal2Noise"):
    """Score every row of X (genes x samples) with class A = labels==0 first, then sort
    descending with ties in row order (stable).  Returns (order, scores)."""
    f = METRICS[metric]
    a = X[:, labels == 0]
    b = X[:, labels == 1]
    s = np.array([f(a[i], b[i]) for i in range(X.shape[0])])
    order = np.argsort(-s, kind="stable")
    return order, s


# ----------------------------------------------------------------------------- collapse
def collapse(X, probe_symbols, mode="Max_probe"):
    """Probe->gene collapse of a genes x samples matrix.  Max_probe: per-sample maximum over
    the probes of a symbol (the documented behaviour); Median/Mean/Sum per sample;
    Abs_max: the signed value with the largest |.| per sample.  Returns (symbols, M) with
    symbols in first-appearance order."""
    groups = {}
    for i, s in enumerate(probe_symbols):
        groups.setdefault(s, []).append(i)
    syms = list(groups)
    M = np.empty((len(syms), X.shape[1]))
    for k, s in enumerate(syms):
        sub = X[groups[s]]
        if mode == "Max_probe":
            M[k] = np.nanmax(sub, axis=0)
        elif mode == "Median_of_probes":
            M[k] = np.nanmedian(sub, axis=0)
        elif mode == "Mean_of_probes":
            M[k] = np.nanmean(sub, axis=0)
        elif mode == "Sum_of_probes":
            M[k] = np.nansum(sub, axis=0)
        elif mode == "Abs_max_of_probes":
            j = np.nanargmax(np.abs(sub), axis=0)
            M[k] = sub[j, np.arange(sub.shape[1])]
        else:
            raise ValueError(mode)
    return syms, M
