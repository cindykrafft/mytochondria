"""Independent reference for preranked GSEA as documented by Subramanian et al. (2005) and the
fgsea help pages. Written from the definitions, not from fgsea's code.

Conventions (fgsea's documented ones):
  * genes sorted by stat, decreasing; weight w_i = |r_i|^p (p = gseaParam);
  * running sum: hit adds w_i / N_R (N_R = sum of member weights), miss subtracts 1 / (N - k);
  * ES+ = max of the running sum (>= 0), ES- = min (<= 0); std ES = ES+ if ES+ > |ES-|,
    ES- if |ES-| > ES+, 0 on a tie; "pos" -> ES+, "neg" -> ES-;
  * nominal p (std): P(ES* >= ES | ES* >= 0) for ES >= 0, P(ES* <= ES | ES* <= 0) for ES < 0,
    over uniformly random gene sets of the same size; "pos"/"neg": unconditional tail;
  * NES = ES / mean(ES* | same sign as ES);
  * leading edge: members at or before the peak of the running sum (ES > 0), members at or after
    the trough (ES < 0), the latter listed from the bottom of the ranking upwards.
"""
import itertools
import math
import numpy as np


def running(w, pos, n):
    """w: weights of all n genes (sorted order); pos: sorted 0-based member positions.
    Returns (tops, bottoms): running sum right after / right before each hit."""
    pos = np.asarray(sorted(pos))
    k = len(pos)
    rw = np.asarray(w, dtype=float)[pos]
    NR = rw.sum()
    if NR == 0:
        rw = np.ones(k)
        NR = float(k)
    cum = np.cumsum(rw) / NR
    misses = pos - np.arange(k)          # misses before (and at) hit j
    tops = cum - misses / (n - k)
    bottoms = tops - rw / NR
    return tops, bottoms


def es_all(w, pos, n):
    tops, bottoms = running(w, pos, n)
    esp = max(0.0, tops.max())
    esn = min(0.0, bottoms.min())
    if esp > -esn:
        std = esp
    elif esp < -esn:
        std = esn
    else:
        std = 0.0
    return std, esp, esn


def leading_edge(w, pos, n, score_type="std"):
    pos = sorted(pos)
    tops, bottoms = running(w, pos, n)
    std, esp, esn = es_all(w, pos, n)
    if score_type == "pos" or (score_type == "std" and std > 0):
        j = int(np.argmax(tops))
        return list(pos[: j + 1])
    if score_type == "neg" or (score_type == "std" and std < 0):
        j = int(np.argmin(bottoms))
        return list(reversed(pos[j:]))
    return []


def batch_es(w, P, n):
    """Vectorised ES for a matrix P (B x k) of sorted 0-based positions. Returns std, ES+, ES-."""
    w = np.asarray(w, dtype=float)
    B, k = P.shape
    rw = w[P]
    NR = rw.sum(axis=1, keepdims=True)
    zero = NR[:, 0] == 0
    if zero.any():
        rw[zero] = 1.0
        NR[zero] = k
    cum = np.cumsum(rw, axis=1) / NR
    misses = P - np.arange(k)[None, :]
    tops = cum - misses / (n - k)
    bottoms = tops - rw / NR
    esp = np.maximum(tops.max(axis=1), 0.0)
    esn = np.minimum(bottoms.min(axis=1), 0.0)
    std = np.where(esp > -esn, esp, np.where(esp < -esn, esn, 0.0))
    return std, esp, esn


def exact_null(w, n, k, chunk=200000):
    """ES (std, +, -) for every k-subset of n positions (lexicographic)."""
    out = [[], [], []]
    it = itertools.combinations(range(n), k)
    while True:
        block = list(itertools.islice(it, chunk))
        if not block:
            break
        s, p, m = batch_es(w, np.array(block, dtype=np.int64), n)
        out[0].append(s); out[1].append(p); out[2].append(m)
    return tuple(np.concatenate(x) for x in out)


def pvals_from_null(es, null_std, null_pos, null_neg, score_type="std", tol=1e-12):
    """Documented nominal p and NES from a null sample/enumeration; ties within tol count."""
    if score_type == "pos":
        return float(np.mean(null_pos >= es - tol)), es / null_pos.mean()
    if score_type == "neg":
        return float(np.mean(null_neg <= es + tol)), es / abs(null_neg.mean())
    if es >= 0:
        same = null_std[null_std >= 0]
        return float(np.mean(same >= es - tol)), es / same.mean()
    same = null_std[null_std <= 0]
    return float(np.mean(same <= es + tol)), es / abs(same.mean())


def dp_tail_pos(wint, n, k, obs_pos):
    """Exact P(ES+* >= ES+(obs)) over all k-subsets for small non-negative INTEGER weights.
    For each possible member-weight total S, a DP over positions counts subsets that reach a
    running-sum value >= the observed ES+ at some hit.  Comparisons are exact integer
    arithmetic: top = (W*(n-k) - m*S) / (S*(n-k)), compared with the observed (W0, m0, S0).
    Returns the probability as a float (the counts are float64, only ever added)."""
    wint = np.asarray(wint, dtype=np.int64)
    assert (wint > 0).all(), "use strictly positive integer weights"
    obs_pos = sorted(obs_pos)
    # observed ES+ as a rational with exact integers
    S0 = int(wint[obs_pos].sum())
    best = None
    W = 0
    for j, p in enumerate(obs_pos):
        W += int(wint[p]); m = p - j
        num = W * (n - k) - m * S0          # top * S0*(n-k)
        if best is None or num * 1 > best:
            best = num
    T = best  # ES+ = T / (S0*(n-k)); assume > 0
    assert T > 0
    wmax = int(wint.max())
    Smax = int(np.sort(wint)[-k:].sum())
    Smin = int(np.sort(wint)[:k].sum())
    total_reached = 0.0
    for S in range(Smin, Smax + 1):
        # state arrays indexed [j hits so far][W so far]; two layers: not-yet-reached / reached
        A = np.zeros((k + 1, S + 1)); R = np.zeros((k + 1, S + 1))
        A[0, 0] = 1.0
        jj = np.arange(k + 1)[:, None]
        WW = np.arange(S + 1)[None, :]
        for i in range(n):
            wi = int(wint[i])
            if wi > S:
                continue_hit = False
            else:
                continue_hit = True
            nA = A.copy(); nR = R.copy()          # miss: state unchanged
            if continue_hit:
                # hit: (j, W) -> (j+1, W+wi); misses before this hit m = i - j
                srcA = A[:-1, : S + 1 - wi]; srcR = R[:-1, : S + 1 - wi]
                j_new = jj[1:]; W_new = WW[:, wi:]
                m = i - (j_new - 1)
                reach = (W_new * (n - k) - m * S) * S0 >= T * S
                nA[1:, wi:] += np.where(reach, 0.0, srcA)
                nR[1:, wi:] += srcR + np.where(reach, srcA, 0.0)
            A, R = nA, nR
        total_reached += R[k, S]
    return total_reached / math.comb(n, k)
