"""Independent numpy port of the GSEA statistics, written from Subramanian et al. 2005
(PNAS 102:15545, Methods and Supporting Information) and the GSEA user guide, *not* from
the Java source.  Used as the truth every harness compares the shipped program against.

Conventions follow the paper:
  ranked list L of N genes with correlations r_j (descending);
  P_hit(S, i) = sum_{g_j in S, j <= i} |r_j|^p / N_R,  N_R = sum_{g_j in S} |r_j|^p;
  P_miss(S, i) = sum_{g_j not in S, j <= i} 1 / (N - N_H);
  ES(S) = the maximum deviation from zero of P_hit - P_miss.
p = 0 is the "classic" Kolmogorov-Smirnov statistic; p = 1 is the default "weighted"
scheme; p = 1.5 and 2 are the "weighted_p1.5" and "weighted_p2" options.
"""
import numpy as np


# ------------------------------------------------------------------ enrichment score
def running_sum(scores, hit_mask, p=1.0):
    """P_hit - P_miss at every position of the ranked list (float64)."""
    scores = np.asarray(scores, dtype=np.float64)
    hit_mask = np.asarray(hit_mask, dtype=bool)
    N, NH = scores.size, int(hit_mask.sum())
    w = np.abs(scores) ** p if p != 0 else np.ones(N)
    NR = w[hit_mask].sum()
    hit_inc = np.where(hit_mask, w / NR, 0.0)
    miss_inc = np.where(hit_mask, 0.0, 1.0 / (N - NH))
    return np.cumsum(hit_inc - miss_inc)


def enrichment_score(scores, hit_mask, p=1.0):
    """ES and the 0-based position of the maximum deviation from zero."""
    rs = running_sum(scores, hit_mask, p)
    i = int(np.argmax(np.abs(rs)))
    return float(rs[i]), i


def hit_mask(names, gene_set):
    s = set(gene_set)
    return np.array([n in s for n in names], dtype=bool)


# ------------------------------------------------------------------ null distributions
def gene_set_null(scores, n_hits, nperm, rng, p=1.0):
    """Gene-set permutation null: ES of nperm random sets of n_hits genes from the list."""
    N = len(scores)
    out = np.empty(nperm)
    for k in range(nperm):
        m = np.zeros(N, dtype=bool)
        m[rng.choice(N, n_hits, replace=False)] = True
        out[k] = enrichment_score(scores, m, p)[0]
    return out


# ------------------------------------------------------------------ NES, p, FDR, FWER
def nes(es, null):
    """Normalize ES by the mean of the same-sign part of its own null (paper, Methods)."""
    null = np.asarray(null)
    if es >= 0:
        pos = null[null >= 0]
        return es / pos.mean() if pos.size else np.nan
    neg = null[null < 0]
    return es / abs(neg.mean()) if neg.size else np.nan


def nes_null(null):
    """Normalize a null vector the same way (positive by the positive mean, etc.)."""
    null = np.asarray(null, dtype=np.float64)
    out = np.empty_like(null)
    pos, neg = null[null >= 0], null[null < 0]
    mp = pos.mean() if pos.size else np.nan
    mn = abs(neg.mean()) if neg.size else np.nan
    out[null >= 0] = null[null >= 0] / mp
    out[null < 0] = null[null < 0] / mn
    return out


def nominal_p(es, null, strict=True):
    """Fraction of the same-sign null at least as extreme as ES.
    strict=True counts null values strictly beyond ES (what GSEA does);
    strict=False counts ties as well (>= / <=)."""
    null = np.asarray(null)
    if es >= 0:
        same = null[null >= 0]
        cnt = (same > es).sum() if strict else (same >= es).sum()
    else:
        same = null[null < 0]
        cnt = (same < es).sum() if strict else (same <= es).sum()
    return cnt / same.size if same.size else np.nan


def fdr_pooled(real_nes, null_nes):
    """FDR q as stated in the paper: for NES* >= 0, the ratio of the percentage of all
    (S, pi) pairs with NES(S, pi) >= 0 whose NES(S, pi) >= NES*, to the percentage of
    observed S with NES(S) >= 0 whose NES(S) >= NES*; mirrored for NES* < 0.
    real_nes: (n_sets,), null_nes: (n_sets, nperm)."""
    real_nes = np.asarray(real_nes, dtype=np.float64)
    pool = np.asarray(null_nes, dtype=np.float64).ravel()
    pool_pos, pool_neg = pool[pool >= 0], pool[pool < 0]
    real_pos, real_neg = real_nes[real_nes >= 0], real_nes[real_nes < 0]
    q = np.empty_like(real_nes)
    for i, v in enumerate(real_nes):
        if v >= 0:
            num = (pool_pos >= v).mean() if pool_pos.size else np.nan
            den = (real_pos >= v).mean()
        else:
            num = (pool_neg <= v).mean() if pool_neg.size else np.nan
            den = (real_neg <= v).mean()
        q[i] = min(1.0, num / den)
    return q


def fdr_per_permutation(real_nes, null_nes):
    """The variant GSEA computes: the numerator is the *mean over permutations* of the
    per-permutation fraction (#{NES(S, pi) >= NES*, over S} / #{NES(S, pi) >= 0, over S}),
    permutations with no same-sign value skipped; the denominator is rank-based."""
    real_nes = np.asarray(real_nes, dtype=np.float64)
    null_nes = np.asarray(null_nes, dtype=np.float64)
    n_sets, nperm = null_nes.shape
    q = np.empty(n_sets)
    for i, v in enumerate(real_nes):
        cols = []
        for c in range(nperm):
            col = null_nes[:, c]
            if v >= 0:
                same = col[col >= 0]
                if same.size:
                    cols.append((same >= v).sum() / same.size)
            else:
                same = col[col < 0]
                if same.size:
                    cols.append((same <= v).sum() / same.size)
        num = np.mean(cols) if cols else np.nan
        if v >= 0:
            real_same = real_nes[real_nes >= 0]
            den = (real_same >= v).sum() / real_same.size
        else:
            real_same = real_nes[real_nes < 0]
            den = (real_same <= v).sum() / real_same.size
        q[i] = min(1.0, num / den)
    return q


def fwer(real_nes_value, null_nes):
    """Family-wise error: fraction of permutations whose most extreme same-sign NES over
    all gene sets is beyond the observed NES."""
    null_nes = np.asarray(null_nes, dtype=np.float64)
    if real_nes_value >= 0:
        best = null_nes.max(axis=0)
        return (best > real_nes_value).mean()
    best = null_nes.min(axis=0)
    return (best < real_nes_value).mean()


# ------------------------------------------------------------------ ranking metrics
def _sd(x, fixlow=True, ddof=1):
    """Standard deviation with GSEA's documented minimum: sigma is at least 0.2 * |mean|,
    or 0.2 when the mean is zero."""
    x = np.asarray(x, dtype=np.float64)
    s = x.std(ddof=ddof)
    if fixlow:
        m = x.mean()
        floor = 0.2 if abs(m) <= 1e-9 else 0.2 * abs(m)
        s = max(s, floor)
    return s


def signal2noise(a, b, fixlow=True):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return (a.mean() - b.mean()) / (_sd(a, fixlow) + _sd(b, fixlow))


def ttest(a, b, fixlow=True):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return (a.mean() - b.mean()) / np.sqrt(_sd(a, fixlow) ** 2 / a.size + _sd(b, fixlow) ** 2 / b.size)


def ratio_of_classes(a, b):
    return np.mean(a) / np.mean(b)


def log2_ratio_of_classes(a, b):
    return np.log2(np.mean(a) / np.mean(b))


def diff_of_classes(a, b):
    return np.mean(a) - np.mean(b)


# ------------------------------------------------------------------ probe collapsing
def collapse(X, probe_symbols, mode="Max_probe"):
    """Collapse a probe x sample matrix to symbol x sample.  Max_probe takes, for each
    sample, the maximum over the probes of a symbol (the user guide: 'for each sample,
    use the maximum expression value for the probe set')."""
    X = np.asarray(X, dtype=np.float64)
    groups = {}
    for i, s in enumerate(probe_symbols):
        if s is not None:
            groups.setdefault(s, []).append(i)
    out = {}
    for s, idx in groups.items():
        sub = X[idx]
        if mode == "Max_probe":
            out[s] = sub.max(axis=0)
        elif mode == "Median_of_probes":
            out[s] = np.median(sub, axis=0)
        elif mode == "Mean_of_probes":
            out[s] = sub.mean(axis=0)
        elif mode == "Sum_of_probes":
            out[s] = sub.sum(axis=0)
        elif mode == "Abs_max_of_probes":
            j = np.argmax(np.abs(sub), axis=0)
            out[s] = sub[j, np.arange(sub.shape[1])]
        else:
            raise ValueError(mode)
    return out
