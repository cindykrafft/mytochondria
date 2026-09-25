#!/usr/bin/env python
"""NumPy descriptive statistics against exact (Fraction / mpmath) recomputations:
mean, var, std (ddof), median, average with weights, percentile/quantile for every
method against the Hyndman-Fan definitions, nan-variants, cov (ddof, fweights,
aweights), corrcoef, and the precision of float32 reductions along the slow axis."""
import sys, math, random
from fractions import Fraction as F
import numpy as np
try:
    import mpmath; mpmath.mp.dps = 50
except ImportError: mpmath = None
print(f"numpy {np.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-12, abs_=1e-300):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
rng = random.Random(7)
x = [F(rng.randint(-1000, 1000), rng.randint(1, 64)) for _ in range(257)]
xf = np.array([float(v) for v in x]); xF = [F(v) for v in xf.tolist()]     # exact values of the float64 array
n = len(xF); mean = sum(xF) / n
report("mean exact", close(xf.mean(), mean))
for ddof in (0, 1):
    var = sum((v - mean) ** 2 for v in xF) / (n - ddof)
    report(f"var(ddof={ddof}) exact", close(xf.var(ddof=ddof), var)); report(f"std(ddof={ddof}) = sqrt(var)", close(xf.std(ddof=ddof), math.sqrt(var)))
srt = sorted(xF)
report("median (odd n) = middle value", close(np.median(xf), srt[n // 2]))
report("median (even n) = mean of the two middle values", close(np.median(xf[:-1]), (sorted(xF[:-1])[n // 2 - 1] + sorted(xF[:-1])[n // 2]) / 2))
w = [F(rng.randint(1, 9)) for _ in range(n)]
report("average(weights) = sum w x / sum w", close(np.average(xf, weights=[float(v) for v in w]), sum(a * b for a, b in zip(w, xF)) / sum(w)))

# ---- percentile methods against Hyndman & Fan (1996) / Wikipedia definitions
def hf_quantile(sorted_vals, p, method):
    """Exact quantile for the nine H&F methods plus the four discontinuous ones NumPy offers."""
    xs = sorted_vals; n = len(xs); p = F(p)
    def interp(h):   # 1-based position h; linear interpolation with clamping
        if h <= 1: return xs[0]
        if h >= n: return xs[-1]
        lo = math.floor(h); frac = h - lo
        return xs[lo - 1] + frac * (xs[lo] - xs[lo - 1])
    if method == "inverted_cdf":            # H&F 1
        k = math.ceil(n * p); return xs[max(k, 1) - 1]
    if method == "averaged_inverted_cdf":   # H&F 2
        h = n * p; k = math.floor(h)
        if h == k: return (xs[max(k, 1) - 1] + xs[min(k, n - 1)]) / 2 if 0 < k < n else (xs[0] if k == 0 else xs[-1])
        return xs[min(k, n - 1)]
    if method == "closest_observation":     # H&F 3: j = floor(np - 1/2), g = np - 1/2 - j; x_{j+1} if g > 0, else x_j for even j and x_{j+1} for odd j
        h = n * p - F(1, 2); j = math.floor(h); g = h - j
        k = j + 1 if g > 0 else (j if j % 2 == 0 else j + 1)
        return xs[min(max(k, 1), n) - 1]
    if method == "interpolated_inverted_cdf": return interp(n * p)                 # H&F 4
    if method == "hazen":                    return interp(n * p + F(1, 2))        # H&F 5
    if method == "weibull":                  return interp((n + 1) * p)            # H&F 6
    if method == "linear":                   return interp((n - 1) * p + 1)        # H&F 7
    if method == "median_unbiased":          return interp((n + F(1, 3)) * p + F(1, 3))   # H&F 8
    if method == "normal_unbiased":          return interp((n + F(1, 4)) * p + F(3, 8))   # H&F 9
    h = (n - 1) * p + 1                      # the four discontinuous variants of method 7
    if method == "lower":  return xs[math.floor(h) - 1]
    if method == "higher": return xs[math.ceil(h) - 1]
    if method == "nearest":                  # NumPy rounds the 0-based virtual index (n-1)p half to even
        h0 = h - 1; k0 = round(h0) if (h0 - math.floor(h0)) != F(1, 2) else (math.floor(h0) if math.floor(h0) % 2 == 0 else math.ceil(h0)); return xs[k0]
    if method == "midpoint": return (xs[math.floor(h) - 1] + xs[math.ceil(h) - 1]) / 2
methods = ["inverted_cdf", "averaged_inverted_cdf", "closest_observation", "interpolated_inverted_cdf", "hazen", "weibull", "linear", "median_unbiased", "normal_unbiased", "lower", "higher", "nearest", "midpoint"]
ps = [0, 1, 2.5, 5, 10, 25, 33.3, 50, 66.7, 75, 90, 95, 97.5, 99, 100]
for nn in (5, 8, 257):
    xs = sorted(xF[:nn]); arr = np.array([float(v) for v in xs])
    for m in methods:
        try:
            got = [np.percentile(arr, p, method=m) for p in ps]
        except TypeError:
            got = [np.percentile(arr, p, interpolation=m) for p in ps] if m in ("linear", "lower", "higher", "nearest", "midpoint") else None
        if got is None: print(f"   percentile method '{m}': not in this version"); continue
        want = [hf_quantile(xs, F(p) / 100, m) for p in ps]
        bad = [(p, g, float(w_)) for p, g, w_ in zip(ps, got, want) if not close(g, w_, 1e-12, 1e-12)]
        report(f"percentile method '{m}' on n={nn} at {len(ps)} probabilities equals the H&F definition", not bad, str(bad[:2]) if bad else "")
report("quantile(q) == percentile(100 q) (default method)", all(close(np.quantile(xf, p / 100), np.percentile(xf, p)) for p in ps))
report("percentile default method is 'linear' (H&F 7)", all(close(np.percentile(xf, p), hf_quantile(srt, F(p) / 100, "linear")) for p in ps))
# nan variants
xn = xf.copy(); xn[::5] = np.nan; kept = sorted(F(v) for i, v in enumerate(xf.tolist()) if i % 5 != 0)
report("nanpercentile = percentile over the non-NaN values", all(close(np.nanpercentile(xn, p), hf_quantile(kept, F(p) / 100, "linear")) for p in ps))
report("nanmean / nanstd over the non-NaN values", close(np.nanmean(xn), sum(kept) / len(kept)) and close(np.nanstd(xn, ddof=1), math.sqrt(sum((v - sum(kept) / len(kept)) ** 2 for v in kept) / (len(kept) - 1))))
report("nanmedian over the non-NaN values", close(np.nanmedian(xn), (kept[len(kept) // 2 - 1] + kept[len(kept) // 2]) / 2 if len(kept) % 2 == 0 else kept[len(kept) // 2]))

# ---- cov / corrcoef
m = 4; k = 40
M = [[F(rng.randint(-50, 50), rng.randint(1, 8)) for _ in range(k)] for _ in range(m)]
Mf = np.array([[float(v) for v in row] for row in M]); ME = [[F(v) for v in row] for row in Mf.tolist()]
def cov_exact(ME, ddof=1, fw=None, aw=None):
    m = len(ME); k = len(ME[0])
    fw = [F(1)] * k if fw is None else [F(v) for v in fw]; aw = [F(1)] * k if aw is None else [F(v) for v in aw]
    w = [a * b for a, b in zip(fw, aw)]; v1 = sum(w); v2 = sum(a * b for a, b in zip(w, aw))
    means = [sum(a * b for a, b in zip(w, row)) / v1 for row in ME]
    fact = v1 - ddof * v2 / v1
    return [[sum(w[t] * (ME[i][t] - means[i]) * (ME[j][t] - means[j]) for t in range(k)) / fact for j in range(m)] for i in range(m)]
C = np.cov(Mf); CE = cov_exact(ME)
report("cov (ddof=1 default) exact", all(close(C[i, j], CE[i][j]) for i in range(m) for j in range(m)))
report("cov(bias=True) = ddof 0", all(close(np.cov(Mf, bias=True)[i, j], cov_exact(ME, 0)[i][j]) for i in range(m) for j in range(m)))
fw = [rng.randint(1, 4) for _ in range(k)]; aw = [rng.randint(1, 5) / 2 for _ in range(k)]
report("cov(fweights, aweights, ddof=1): factor v1 - ddof * v2 / v1 with v1 = sum w, v2 = sum w a", all(close(np.cov(Mf, fweights=fw, aweights=aw)[i, j], cov_exact(ME, 1, fw, aw)[i][j]) for i in range(m) for j in range(m)))
R = np.corrcoef(Mf)
report("corrcoef = cov / sqrt(var_i var_j)", all(close(R[i, j], CE[i][j] / math.sqrt(CE[i][i] * CE[j][j])) for i in range(m) for j in range(m)))
report("corrcoef |r| <= 1 (clipped)", np.all(np.abs(R) <= 1)); print(f"   corrcoef diagonal: {np.diag(R).tolist()} (1 - diag: {[1 - v for v in np.diag(R).tolist()]})")

# ---- float32 reductions along the slow axis: pairwise summation only along the fast axis
N = 1_000_000
big = (np.float32(1000.0) + np.arange(N, dtype=np.float32) * np.float32(1e-3)).reshape(N, 1)
A = np.hstack([big, big + np.float32(1), big + np.float32(2), big + np.float32(3)]).astype(np.float32)   # (N, 4), C order
exact_col0 = sum(F(v) for v in A[:, 0].astype(np.float64).tolist()) / N
m_axis0 = A.mean(axis=0)[0]; m_flat = A[:, 0].copy().mean(); m_f64 = A[:, 0].astype(np.float64).mean()
print(f"   float32 (1e6, 4) array, column mean along axis 0: {m_axis0!r}; the same column contiguous: {m_flat!r}; float64: {m_f64!r}; exact {float(exact_col0):.6f}")
report("float32 mean along axis 0 of a C-ordered (n, k) array is within 1e-6 relative of the exact mean", close(m_axis0, exact_col0, 1e-6, 0), f"(relative error {abs(float(m_axis0) - float(exact_col0)) / float(exact_col0):.2e}; contiguous copy {abs(float(m_flat) - float(exact_col0)) / float(exact_col0):.2e})")
report("float32 mean of the contiguous column is within 1e-6 relative (pairwise summation)", close(m_flat, exact_col0, 1e-6, 0))
report("float32 var along axis 0 within 1e-4 relative of exact", close(A.var(axis=0)[0], float(np.var(A[:, 0].astype(np.float64))), 1e-4, 0), f"(got {A.var(axis=0)[0]!r}, float64 {np.var(A[:, 0].astype(np.float64))!r})")
s_axis0 = A.sum(axis=0)[0]; s_flat = A[:, 0].copy().sum()
print(f"   float32 sum along axis 0: {s_axis0!r}; contiguous: {s_flat!r}; exact {float(exact_col0 * N):.1f}")
# float32 cumsum
cs = np.cumsum(A[:, 0])[-1]
print(f"   float32 cumsum last element: {cs!r} (relative error {abs(float(cs) - float(exact_col0 * N)) / float(exact_col0 * N):.2e})")
# float32 percentile / median precision
p32 = np.percentile(A[:, 0], 50); p64 = np.percentile(A[:, 0].astype(np.float64), 50)
report("float32 median equals the float64 median to float32 precision", close(p32, p64, 1e-6, 0), f"({p32!r} vs {p64!r})")
report("mean of an int64 array is computed in float64 (exact for these values)", close(np.arange(1, 10_000_001, dtype=np.int64).mean(), 5_000_000.5))
