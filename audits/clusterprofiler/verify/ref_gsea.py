"""Independent reference implementations used by the clusterProfiler/fgsea harnesses.

Written from Subramanian et al. (PNAS 2005, "Gene set enrichment analysis") and the
GSEA user guide's leading-edge definitions, not from fgsea/enrichit/DOSE code.

  running_sum(stats, hits, p)   P_hit(i) - P_miss(i), stats sorted decreasing
  gsea_es(...)                  ES = running sum at the position of maximum deviation
                                 from zero; leading edge, `rank`, tags/list/signal
  exact_null(stats, k, p)       ES for every one of the C(N, k) gene sets of size k
                                 (gene-set permutation null, enumerated exactly)
  hypergeom_sf(k, N, M, n)      P(X >= k), scipy
"""
import itertools
import numpy as np
from scipy.stats import hypergeom


def running_sum(stats, hits, p=1.0):
    """stats: array sorted decreasing (signed); hits: boolean array; returns the running sum."""
    stats = np.asarray(stats, dtype=float)
    hits = np.asarray(hits, dtype=bool)
    N = stats.size
    Nh = int(hits.sum())
    w = np.abs(stats) ** p
    NR = w[hits].sum()
    P_hit = np.cumsum(np.where(hits, w, 0.0)) / NR if NR > 0 else np.cumsum(hits) / max(Nh, 1)
    P_miss = np.cumsum(~hits) / (N - Nh)
    return P_hit - P_miss


def gsea_es(stats, hits, p=1.0):
    """Returns dict(ES, peak (0-based), running, leading_edge_idx, rank, tags, list, signal).

    ES: the maximum deviation from zero of the running sum (paper, Fig. 1 legend).
    Leading edge (GSEA user guide): for ES > 0 the members that appear in the ranked
    list at or before the peak; for ES < 0 the members at or after the peak.
    rank: position of the peak counted from the top (ES > 0) or from the bottom (ES < 0).
    tags = |leading edge| / Nh; list = rank / N; signal = tags * (1 - list) * N / (N - Nh).
    """
    hits = np.asarray(hits, dtype=bool)
    rs = running_sum(stats, hits, p)
    N = rs.size
    Nh = int(hits.sum())
    imax = int(np.argmax(rs))
    imin = int(np.argmin(rs))
    if abs(rs[imax]) >= abs(rs[imin]):
        ES, peak = float(rs[imax]), imax
    else:
        ES, peak = float(rs[imin]), imin
    idx = np.arange(N)
    if ES >= 0:
        le = idx[(idx <= peak) & hits]
        rank = peak + 1
    else:
        le = idx[(idx >= peak) & hits]
        rank = N - peak
    tags = le.size / Nh
    lst = rank / N
    signal = tags * (1 - lst) * N / (N - Nh)
    return dict(ES=ES, peak=peak, running=rs, leading_edge_idx=le, rank=rank,
                tags=tags, list=lst, signal=signal)


def exact_null(stats, k, p=1.0):
    """ES of every k-subset of positions 0..N-1 (exact gene-set permutation null)."""
    stats = np.asarray(stats, dtype=float)
    N = stats.size
    w = np.abs(stats) ** p
    out = np.empty(int(np.round(_comb(N, k))))
    hits = np.zeros(N, dtype=bool)
    for j, comb in enumerate(itertools.combinations(range(N), k)):
        hits[:] = False
        hits[list(comb)] = True
        NR = w[hits].sum()
        P_hit = np.cumsum(np.where(hits, w, 0.0)) / NR
        P_miss = np.cumsum(~hits) / (N - k)
        rs = P_hit - P_miss
        a, b = rs.max(), rs.min()
        out[j] = a if abs(a) >= abs(b) else b
    return out


def _comb(n, k):
    from math import comb
    return comb(n, k)


def gsea_pvalue_from_null(es, null):
    """GSEA-convention nominal p: P(null ES >= es | null ES >= 0) for es > 0, mirrored for es < 0.
    Also returns the unconditional two-sided-by-sign probability and the NES denominator."""
    null = np.asarray(null)
    if es >= 0:
        same = null[null >= 0]
        p_cond = (same >= es).sum() / same.size
        p_uncond = (null >= es).sum() / null.size
        nes = es / same.mean()
    else:
        same = null[null < 0]
        p_cond = (same <= es).sum() / same.size
        p_uncond = (null <= es).sum() / null.size
        nes = es / abs(same.mean())
    return dict(p_cond=p_cond, p_uncond=p_uncond, NES=nes, frac_same_sign=same.size / null.size)


def hypergeom_sf(k, N, M, n):
    """P(X >= k) for X ~ Hypergeom(N genes, M in the set, n drawn)."""
    return hypergeom.sf(k - 1, N, M, n)


def bh(p):
    p = np.asarray(p, dtype=float)
    n = p.size
    order = np.argsort(p)
    ranked = p[order] * n / (np.arange(n) + 1)
    q = np.minimum.accumulate(ranked[::-1])[::-1]
    out = np.empty(n)
    out[order] = np.minimum(q, 1.0)
    return out
