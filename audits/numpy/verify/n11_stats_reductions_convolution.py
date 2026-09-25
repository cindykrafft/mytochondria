#!/usr/bin/env python
"""NumPy statistics, reductions, binning, convolution and calculus helpers beyond the
basics covered by n1 / n2 / n4.  Truths: fractions.Fraction (exact sums, variances,
H&F type-7 quantiles, the weighted inverted-CDF definition, exact bin membership,
Lagrange-interpolant derivatives for np.gradient, exact convolution sums) and mpmath
(square roots, logs, cube roots, skewness for the bin estimators, atan2 in degrees);
plain-Python reference implementations (Stone's cross-validation estimator, unwrap by
the documented rule, direct convolution / correlation sums with complex conjugation).
No scipy anywhere (the numpy 1.x builds have none).

Covered: nanvar / nanstd ddof and all-NaN slices (warnings + NaN), correction= /
mean= (2.0+); nanmedian / nanpercentile / nanquantile with axis tuples + keepdims;
nanmax / nanmin / nanargmax / nanmean / nansum / nanprod on all-NaN; nanmean /
nansum dtype and out; average with weights / returned / axis / keepdims / zero-sum
weights; median / percentile with +-inf and NaN; weighted quantile (2.0+,
inverted_cdf) against the coverage definition; histogram2d / histogramdd (edges,
range, density, weights, the inclusive last bin on every axis); histogram_bin_edges
for all eight string estimators against the documented formulas; bincount;
cumsum / cumprod / nancumsum / nancumprod dtypes and NaN; cumulative_sum /
cumulative_prod include_initial (2.1+); diff (n, prepend, append, bool, uint,
datetime) and ediff1d; sum / prod dtype rules, empty reductions, initial= and
where=; max / min with initial / where; ptp int8 wraparound; convolve / correlate
(full / same / valid, odd / even lengths, complex conjugation, swap); piecewise;
select; where with scalars; interp (period, left / right, complex fp, decreasing
xp, NaN in xp); trapezoid (x, dx, axis); gradient (edge_order 1 / 2, non-uniform,
several axes, varargs forms); unwrap (discont, period, axis); angle(deg); clip
bounds; cov / corrcoef (rowvar, bias, ddof, y, complex, clipping, constant / NaN
rows); float16 mean; complex var / std; median of even-length ints; percentile q
array + out; quantile q out of range; count_nonzero keepdims; apply_over_axes."""
import sys, math, cmath, warnings, random, inspect
from fractions import Fraction as F
import numpy as np
import mpmath as mp
mp.mp.dps = 40
NPV = tuple(int(v) for v in np.__version__.split(".")[:2]); NP2 = NPV >= (2, 0)
def banner(): print(f"numpy {np.__version__}  mpmath {mp.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def info(s): print("   " + s)
def close(a, b, rel=1e-12, abs_=1e-300):
    a = complex(a); b = complex(b)
    if cmath.isnan(a) and cmath.isnan(b): return True
    if cmath.isinf(a) or cmath.isinf(b): return a == b
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
def allclose(xs, ys, rel=1e-12, abs_=1e-300):
    xs = list(np.ravel(np.asarray(xs, dtype=complex))) if not isinstance(xs, list) else xs
    ys = list(ys)
    return len(xs) == len(ys) and all(close(a, b, rel, abs_) for a, b in zip(xs, ys))
def isnan(x): return isinstance(x, float) and math.isnan(x) or (hasattr(x, "dtype") and np.isnan(x))
warnings.filterwarnings("ignore")
class caught:
    def __enter__(self):
        self._cm = warnings.catch_warnings(record=True); self.w = self._cm.__enter__(); warnings.simplefilter("always"); return self
    def __exit__(self, *a): self._cm.__exit__(*a)
    @property
    def cats(self): return sorted({x.category.__name__ for x in self.w})
    @property
    def msgs(self): return [str(x.message) for x in self.w]
def raises(fn):
    try: fn()
    except Exception as e: return type(e).__name__ + ": " + str(e)[:90]
    return None
rng = random.Random(20260925)
def fr(x): return F(float(x))
def fsum(v): return sum((F(x) for x in v), F(0))
def mean_x(v): return fsum(v) / len(v)
def var_x(v, ddof=0):
    m = mean_x(v); return sum(((F(x) - m) ** 2 for x in v), F(0)) / (len(v) - ddof)
def sqrt_m(q): return float(mp.sqrt(mp.mpf(q.numerator) / q.denominator))
def q7(vals, q):
    """H&F type 7 (numpy 'linear') on the exact values, q a Fraction in [0, 1]."""
    s = sorted(F(v) for v in vals); n = len(s); h = (n - 1) * q; j = math.floor(h); g = h - j
    if j >= n - 1: return s[-1]
    return s[j] + g * (s[j + 1] - s[j])
def med_x(vals): return q7(vals, F(1, 2))

banner()

# ================================================================== nan-functions
print("#### nanvar / nanstd with ddof, all-NaN slices, correction= / mean=")
nan = float("nan"); inf = float("inf")
x = np.array([1., 2., nan, 4., 7., nan, 11.]); xv = [1, 2, 4, 7, 11]
for d in (0, 1, 2, 4):
    t = var_x(xv, d)
    report(f"nanvar(ddof={d}) = sum (x - mean)^2 / (n_nonnan - ddof) over the 5 non-NaN values (exact)", close(np.nanvar(x, ddof=d), float(t), 1e-14),
           f"{float(np.nanvar(x, ddof=d))!r} vs {float(t)!r}")
    report(f"nanstd(ddof={d}) = sqrt(nanvar(ddof={d}))", close(np.nanstd(x, ddof=d), sqrt_m(t), 1e-14))
for d in (5, 6):
    with caught() as c: r = np.nanvar(x, ddof=d)
    report(f"nanvar(ddof={d}) with ddof >= n_nonnan=5: NaN and RuntimeWarning 'Degrees of freedom <= 0 for slice' (documented)",
           bool(np.isnan(r)) and "RuntimeWarning" in c.cats and any("egrees of freedom" in m for m in c.msgs), f"{r!r} {c.msgs[:2]}")
A = np.array([[1., nan, 3., 5.], [nan, nan, nan, nan], [2., 2., 8., nan]])
with caught() as c: r = np.nanvar(A, axis=1, ddof=1)
t0 = var_x([1, 3, 5], 1); t2 = var_x([2, 2, 8], 1)
report("nanvar(axis=1, ddof=1) with an all-NaN row: that row NaN, the others exact, RuntimeWarning raised",
       close(r[0], float(t0), 1e-14) and np.isnan(r[1]) and close(r[2], float(t2), 1e-14) and "RuntimeWarning" in c.cats, f"{r} {c.msgs[:2]}")
with caught() as c: r = np.nanstd(A, axis=0, keepdims=True)
tt = [sqrt_m(var_x([1, 2], 0)), sqrt_m(var_x([2], 0)), sqrt_m(var_x([3, 8], 0)), sqrt_m(var_x([5], 0))]
report("nanstd(axis=0, keepdims=True): shape (1, 4), columns exact (a single non-NaN value gives 0)", r.shape == (1, 4) and allclose(r, tt, 1e-14), f"{r}")
with caught() as c: r = np.nanvar(np.array([nan, nan]))
report("nanvar of an all-NaN vector: NaN with a RuntimeWarning", bool(np.isnan(r)) and "RuntimeWarning" in c.cats, f"{r} {c.msgs}")
report("nanvar(float32 input) returns float32 ('for arrays of float types it is the same as the array type')", np.nanvar(x.astype(np.float32)).dtype == np.float32)
report("nanvar(int input) returns float64", np.nanvar(np.array([1, 2, 4])).dtype == np.float64)
if NP2:
    report("var(correction=1) == var(ddof=1) (2.0+ Array API alias)", close(np.var(xv, correction=1), float(var_x(xv, 1)), 1e-14))
    report("nanvar(correction=2) == nanvar(ddof=2)", close(np.nanvar(x, correction=2), float(var_x(xv, 2)), 1e-14))
    report("var(ddof=1, correction=1) both given -> ValueError", (raises(lambda: np.var(xv, ddof=1, correction=1)) or "").startswith("ValueError"),
           str(raises(lambda: np.var(xv, ddof=1, correction=1))))
    m = np.mean(np.array(xv, float)); report("var(mean=<the mean>) (2.0+) = var", close(np.var(np.array(xv, float), mean=m), float(var_x(xv)), 1e-14))
    B = np.array([[1., 2, 4], [3, 5, 11]]); mB = B.mean(axis=1, keepdims=True)
    report("std(axis=1, mean=<keepdims mean>) = per-row std", allclose(np.std(B, axis=1, mean=mB), [sqrt_m(var_x([1, 2, 4])), sqrt_m(var_x([3, 5, 11]))], 1e-14))
    mn = np.nanmean(x); report("nanvar(mean=<nanmean>) = nanvar", close(np.nanvar(x, mean=mn, ddof=1), float(var_x(xv, 1)), 1e-14))
else:
    info("correction= / mean= keywords are 2.0+; not present in this build")

print("#### nanmedian / nanpercentile / nanquantile with axis tuples and keepdims")
R = random.Random(11)
C3 = np.array([[[R.randint(-20, 20) / 4 for _ in range(5)] for _ in range(4)] for _ in range(3)])
for (i, j, k) in [(0, 0, 0), (1, 2, 3), (2, 1, 4), (0, 3, 1), (2, 3, 3), (1, 0, 2)]: C3[i, j, k] = nan
C3[:, 1, :] = nan  # one whole slice for axis=(0, 2) is all-NaN
def nn(v): return [float(t) for t in v if not math.isnan(t)]
with caught() as c: r = np.nanmedian(C3, axis=(0, 2), keepdims=True)
tt = []
for j in range(4):
    v = nn(C3[:, j, :].ravel()); tt.append(float(med_x(v)) if v else nan)
report("nanmedian(axis=(0, 2), keepdims=True): shape (1, 4, 1), entries = exact median of the non-NaN values of each (i, :, k) slab",
       r.shape == (1, 4, 1) and allclose(r, tt, 1e-15), f"{np.ravel(r)} vs {tt}")
report("nanmedian on the all-NaN slab: NaN and RuntimeWarning 'All-NaN slice encountered'",
       bool(np.isnan(r[0, 1, 0])) and any("All-NaN" in m for m in c.msgs), f"{c.msgs[:2]}")
qs = [0.1, 0.5, 0.9]
with caught() as c: r = np.nanquantile(C3, qs, axis=(0, 2), keepdims=True)
ok = r.shape == (3, 1, 4, 1)
for a_, q in enumerate(qs):
    for j in range(4):
        v = nn(C3[:, j, :].ravel()); t = float(q7(v, F(str(q)))) if v else nan
        ok &= close(r[a_, 0, j, 0], t, 1e-14)
report("nanquantile(q=[.1,.5,.9], axis=(0, 2), keepdims=True): shape (3, 1, 4, 1) (q axis first), exact H&F-7 per slab", ok, f"shape {r.shape}")
with caught() as c: r = np.nanpercentile(C3, 30, axis=(1, 2))
tt = [float(q7(nn(C3[i].ravel()), F(3, 10))) for i in range(3)]
report("nanpercentile(30, axis=(1, 2)): shape (3,), exact H&F-7 of each block's non-NaN values", r.shape == (3,) and allclose(r, tt, 1e-14), f"{r} vs {tt}")
with caught() as c: r = np.nanpercentile(C3, [25, 75], axis=(0, 1, 2), keepdims=True)
v = nn(C3.ravel())
report("nanpercentile over all three axes with keepdims: shape (2, 1, 1, 1), equals the flattened result",
       r.shape == (2, 1, 1, 1) and allclose(r, [float(q7(v, F(1, 4))), float(q7(v, F(3, 4)))], 1e-14))
with caught() as c: r = np.nanpercentile(np.array([[nan, nan], [1., 3.]]), 50, axis=1)
report("nanpercentile on an all-NaN row: NaN + RuntimeWarning, other row exact", bool(np.isnan(r[0])) and r[1] == 2.0 and "RuntimeWarning" in c.cats, f"{r} {c.msgs[:1]}")
with caught() as c: r = np.nanmedian(np.array([nan, nan, nan]))
report("nanmedian of an all-NaN vector: NaN + RuntimeWarning", bool(np.isnan(r)) and "RuntimeWarning" in c.cats, f"{r} {c.msgs}")
with caught() as c: r = np.nanmedian(np.array([[1., nan], [nan, nan], [2., 4.]]), axis=0, keepdims=True)
report("nanmedian(axis=0, keepdims=True) on a 3x2 with NaNs: [[1.5, 4.0]]", r.shape == (1, 2) and allclose(r, [1.5, 4.0]))

print("#### nanmax / nanmin / nanargmax / nanmean / nansum / nanprod on all-NaN slices")
Z = np.array([[nan, nan, nan], [1., nan, -2.]])
with caught() as c: r = np.nanmax(Z, axis=1)
report("nanmax on an all-NaN row: NaN + RuntimeWarning 'All-NaN slice encountered'; other row 1.0",
       bool(np.isnan(r[0])) and r[1] == 1.0 and any("All-NaN" in m for m in c.msgs), f"{r} {c.msgs}")
with caught() as c: r = np.nanmin(Z, axis=1)
report("nanmin on an all-NaN row: NaN + RuntimeWarning; other row -2.0", bool(np.isnan(r[0])) and r[1] == -2.0 and "RuntimeWarning" in c.cats)
with caught() as c: r = np.nanmax(np.array([nan, nan]))
report("nanmax of an all-NaN vector (axis=None): NaN + RuntimeWarning", bool(np.isnan(r)) and "RuntimeWarning" in c.cats)
e = raises(lambda: np.nanargmax(Z, axis=1))
report("nanargmax on an all-NaN slice raises ValueError (documented 'For all-NaN slices ValueError is raised')", (e or "").startswith("ValueError"), str(e))
report("nanargmin on the other row ignores the NaN: index 2", np.nanargmin(Z[1]) == 2)
with caught() as c: r = np.nanmean(Z, axis=1)
report("nanmean on an all-NaN row: NaN + RuntimeWarning 'Mean of empty slice'", bool(np.isnan(r[0])) and r[1] == -0.5 and any("empty slice" in m for m in c.msgs), f"{r} {c.msgs}")
report("nansum of an all-NaN row is 0 ('zero is returned for slices that are all-NaN or empty')", np.nansum(Z, axis=1)[0] == 0.0 and np.nansum(Z, axis=1)[1] == -1.0)
report("nanprod of an all-NaN row is 1; other row 1*-2 = -2", list(np.nanprod(Z, axis=1)) == [1.0, -2.0])
report("nansum of an empty array is 0.0", np.nansum(np.array([], float)) == 0.0)
report("nanmax of a +-inf / NaN mix ignores only the NaN", np.nanmax(np.array([nan, -inf, inf])) == inf and np.nanmin(np.array([nan, -inf, inf])) == -inf)

print("#### nanmean / nansum dtype and out")
v32 = np.array([1.5, nan, 2.25, 3.0], dtype=np.float32)
r = np.nanmean(v32); report("nanmean(float32) returns float32 (same as input for inexact)", r.dtype == np.float32 and r == np.float32(6.75 / 3))
r = np.nanmean(v32, dtype=np.float64); report("nanmean(float32, dtype=float64) returns float64", r.dtype == np.float64 and r == 2.25)
r = np.nanmean(np.array([1, 2, 4])); report("nanmean(int array) returns float64 (default for integer input)", r.dtype == np.float64 and close(r, 7 / 3, 1e-15))
o = np.zeros(2); A2 = np.array([[1., nan, 3.], [nan, 5., 7.]])
r = np.nanmean(A2, axis=1, out=o); report("nanmean(axis=1, out=o) writes into and returns o", r is o and list(o) == [2.0, 6.0], f"{o}")
o = np.zeros(3, dtype=np.float32); r = np.nansum(A2, axis=0, out=o)
report("nansum(axis=0, out=float32) writes the cast sums and returns out", r is o and list(o) == [1.0, 5.0, 10.0])
report("nansum(int array) = sum (integer dtype kept)", np.nansum(np.array([1, 2, 3], np.int32)).dtype == np.sum(np.array([1, 2, 3], np.int32)).dtype)
r = np.nanmean(np.array([1., nan, 3.], dtype=np.float16)); report("nanmean(float16) returns float16", r.dtype == np.float16 and r == 2.0)
r = np.nansum(A2, axis=1, keepdims=True); report("nansum(keepdims=True): shape (2, 1)", r.shape == (2, 1) and list(r.ravel()) == [4.0, 12.0])

# ================================================================== average
print("#### average: weights, returned, axis, keepdims, zero-sum weights, dtypes")
a = np.array([[1, 5, 2, 8], [3, 3, 9, 1], [7, 2, 4, 6]]); w1 = np.array([1, 2, 0, 5]); wa = np.array([[1, 2, 3, 4], [0, 1, 0, 1], [2, 2, 1, 3]])
t = [fsum([a[i, k] * w1[k] for k in range(4)]) / fsum(w1) for i in range(3)]
r = np.average(a, axis=1, weights=w1)
report("average(axis=1, weights=1-D of length 4): sum(a w) / sum(w) per row, exact", allclose(r, [float(v) for v in t], 1e-15), f"{r}")
t0 = [fsum([a[i, k] * wa[i, k] for i in range(3)]) / fsum(wa[:, k]) for k in range(4)]
r = np.average(a, axis=0, weights=wa); report("average(axis=0, weights same shape as a), exact", allclose(r, [float(v) for v in t0], 1e-15))
tall = fsum([a[i, k] * wa[i, k] for i in range(3) for k in range(4)]) / fsum(wa.ravel())
r = np.average(a, weights=wa); report("average(axis=None, weights same shape) over all elements, exact", close(r, float(tall), 1e-15))
r, sw = np.average(a, axis=1, weights=w1, returned=True)
report("average(returned=True): (avg, sum_of_weights) with sum_of_weights broadcast to avg's shape and dtype", sw.shape == r.shape and list(sw) == [8.0] * 3 and sw.dtype == r.dtype,
       f"sw={sw!r}")
r, sw = np.average(a, axis=0, returned=True)
report("average(returned=True, weights=None): sum_of_weights = number of elements averaged (3.0 each)", list(sw) == [3.0] * 4 and allclose(r, [float(mean_x(a[:, k])) for k in range(4)], 1e-15), f"{sw}")
r, sw = np.average(a, returned=True); report("average(returned=True) over all: sum_of_weights = a.size = 12.0", float(sw) == 12.0 and close(r, float(mean_x(a.ravel())), 1e-15))
r = np.average(a, axis=1, weights=w1, keepdims=True); report("average(keepdims=True) with weights: shape (3, 1)", r.shape == (3, 1) and allclose(r, [float(v) for v in t], 1e-15))
at = np.arange(24.).reshape(2, 3, 4); wt = np.arange(1., 25.).reshape(2, 3, 4)
tt = [fsum([at[i, j, k] * wt[i, j, k] for i in range(2) for k in range(4)]) / fsum([wt[i, j, k] for i in range(2) for k in range(4)]) for j in range(3)]
e = raises(lambda: np.average(at, axis=(0, 2), weights=wt))
if e is None:
    r = np.average(at, axis=(0, 2), weights=wt); report("average(axis=(0, 2), weights same shape): exact per middle index", allclose(r, [float(v) for v in tt], 1e-15), f"{r}")
else:
    info(f"average(axis=tuple, weights=) not supported in this build: {e}")
e = raises(lambda: np.average(a, axis=1, weights=[1, -1, 2, -2]))
report("average with weights summing to 0 (not all zero) raises ZeroDivisionError ('sum(weights) must not be 0')", (e or "").startswith("ZeroDivisionError"), str(e))
e = raises(lambda: np.average(a, axis=0, weights=np.zeros(3)))
report("average with all-zero weights raises ZeroDivisionError", (e or "").startswith("ZeroDivisionError"), str(e))
e = raises(lambda: np.average(a, weights=w1)); report("average(axis=None) with weights of a different shape raises TypeError (documented)", (e or "").startswith("TypeError"), str(e))
e = raises(lambda: np.average(a, axis=1, weights=[1, 2, 3])); report("average(axis=1) with 1-D weights of the wrong length raises ValueError (documented)", (e or "").startswith("ValueError"), str(e))
report("average(int a, int weights) returns float64", np.average(a, weights=wa).dtype == np.float64)
report("average(float32 a, float32 weights) returns float32 ('lowest precision capable of representing both')",
       np.average(a.astype(np.float32), axis=1, weights=w1.astype(np.float32)).dtype == np.float32)
report("average(float32 a, weights=None) returns float32 (dtype of a)", np.average(a.astype(np.float32)).dtype == np.float32)
r = np.average(np.array([1 + 2j, 3 - 1j]), weights=[1, 3]); report("average of complex values with real weights: (1+2j + 3(3-1j)) / 4", r == (10 - 1j) / 4)

# ================================================================== median / percentile with inf and NaN
print("#### median / percentile with +-inf and NaN")
report("median([1, NaN, 3]) is NaN (NaN propagates)", bool(np.isnan(np.median([1., nan, 3.]))))
r = np.median(np.array([[1., 2.], [nan, 4.], [3., 6.]]), axis=0)
report("median(axis=0) with a NaN in column 0: that column NaN, column 1 exact 4.0", bool(np.isnan(r[0])) and r[1] == 4.0, f"{r}")
report("percentile with a NaN: NaN for every q", bool(np.all(np.isnan(np.percentile([1., nan, 3.], [0, 50, 100])))))
report("median([-inf, 1, 2, inf]) = 1.5 (mean of the two middle values)", np.median([-inf, 1., 2., inf]) == 1.5)
report("median([1, inf]) = inf", np.median([1., inf]) == inf)
r = np.median([-inf, inf]); report("median([-inf, inf]) = mean(-inf, inf) = NaN (IEEE)", bool(np.isnan(r)), f"{r}")
report("median([1, 2, inf]) (odd n) = 2", np.median([1., 2., inf]) == 2.0, f"{np.median([1., 2., inf])}")
for data, q, t, what in [([1., 2., inf], 50, 2.0, "virtual index exactly 1 (g = 0), upper neighbour +inf"),
                         ([0., inf], 0, 0.0, "q = 0 with the next value +inf"),
                         ([1., 2., 3., 4., inf], 75, 4.0, "index 3 exactly, next +inf"),
                         ([-inf, 5., 6.], 50, 5.0, "index 1 exactly, previous -inf"),
                         ([1., 2., inf], 100, inf, "q = 100 on +inf"),
                         ([1., 2., inf], 75, inf, "g = 0.5 between 2 and +inf"),
                         ([1., 2., inf], 60, inf, "g = 0.2 between 2 and +inf"),
                         ([-inf, 1., 2.], 25, -inf, "g = 0.5 between -inf and 1"),
                         ([-inf, 1., 2.], 10, -inf, "g = 0.2 between -inf and 1")]:
    with caught() as c: r = np.percentile(data, q)
    report(f"percentile({data}, {q}) = {t}: documented (1-g)*y[j] + g*y[j+1] (g = 0 -> y[j]) with {what}", r == t, f"got {float(r)!r} warnings {c.cats}")
for data in ([1., 2., inf], [-inf, 0., 1.], [1., 2., 3., inf, inf]):
    with caught() as c: r1 = np.median(data); r2 = np.quantile(data, 0.5)
    report(f"median({data}) == quantile(.., 0.5) (documented 'median: equivalent to quantile(..., 0.5)')", r1 == r2 or (np.isnan(r1) and np.isnan(r2)), f"median {float(r1)!r} quantile {float(r2)!r}")
    with caught() as c: r1 = np.percentile(data, [0, 100])
    report(f"percentile({data}, [0, 100]) == [min, max]", list(r1) == [min(data), max(data)], f"{r1.tolist()}")
with caught() as c: r = np.quantile([1., 2., inf], 0.5, method="lower")
report("quantile(method='lower') on [1, 2, inf] at 0.5 = 2", r == 2.0, f"{r}")
with caught() as c: r = np.nanpercentile([1., nan, 2., inf], 50)
report("nanpercentile([1, NaN, 2, inf], 50) = 2 (NaN dropped, then g = 0 next to +inf)", r == 2.0, f"{r}")

# ================================================================== weighted quantiles
print("#### weighted quantile / percentile (2.0+, method='inverted_cdf')")
def wq_exact(vals, wts, q):
    """Smallest sorted value x_i with positive weight and cumulative weight C_i >= q * W (the coverage conditions
    P(Y < x) <= q <= P(Y <= x) of the weighted empirical CDF; q = 0 -> first positive-weight value)."""
    pr = sorted(zip([F(v) for v in vals], [F(w) for w in wts]), key=lambda p: p[0])
    W = sum(w for _, w in pr); C = F(0)
    for v, w in pr:
        C += w
        if w > 0 and C >= q * W: return v
    return pr[-1][0]
def covers(vals, wts, q, x):
    W = fsum(wts); lt = sum((F(w) for v, w in zip(vals, wts) if F(v) < x), F(0)); le = sum((F(w) for v, w in zip(vals, wts) if F(v) <= x), F(0))
    return lt <= q * W <= le
if "weights" in inspect.signature(np.quantile).parameters:
    vals = [3.5, -1.0, 7.25, 0.0, 2.0, 7.25, 10.0]; wts = [2, 1, 0, 3, 1, 2, 1]   # total 10
    qd = [str(k / 10) for k in range(11)] + ["0.05", "0.15", "0.333", "0.95", "0.999"]
    ok = True; det = []
    for s in qd:
        r = np.quantile(vals, float(s), weights=wts, method="inverted_cdf"); t = wq_exact(vals, wts, F(s))
        if F(float(r)) != t or not covers(vals, wts, F(s), F(float(r))): ok = False; det.append(f"q={s}: {r} vs {float(t)}")
    report("weighted quantile at 16 q (incl. every cdf step k/10): smallest x with C(x) >= qW, coverage conditions hold (exact)", ok, "; ".join(det))
    r = np.percentile(vals, [30, 55.5], weights=wts, method="inverted_cdf")
    report("weighted percentile(q=[30, 55.5]) = weighted quantile(q/100)", [F(float(v)) for v in r] == [wq_exact(vals, wts, F(3, 10)), wq_exact(vals, wts, F(555, 1000))], f"{r}")
    iw = [2, 1, 1, 3, 1, 2, 1]; rep = [v for v, k in zip(vals, iw) for _ in range(k)]
    ok = all(np.quantile(vals, q, weights=iw, method="inverted_cdf") == np.quantile(rep, q, method="inverted_cdf") for q in np.linspace(0, 1, 41))
    report("integer weights == repeating each value w times (unweighted inverted_cdf), 41 q in [0, 1]", ok)
    ok = all(np.quantile(vals, q, weights=np.ones(7), method="inverted_cdf") == np.quantile(vals, q, method="inverted_cdf") for q in np.linspace(0, 1, 41))
    report("weights=ones == unweighted inverted_cdf", ok)
    r = np.quantile([5., 1., 3.], 0.0, weights=[1, 0, 1], method="inverted_cdf")
    report("q = 0 with a zero-weight minimum: returns the smallest value with positive weight (3.0)", r == 3.0, f"{r}")
    M = np.array([[4., 1., 3., 2.], [8., 6., 7., 5.]]); wv = [1, 1, 2, 4]
    r = np.quantile(M, [0.25, 0.5], axis=1, weights=wv, method="inverted_cdf")
    tt = [[wq_exact(M[i], wv, q) for i in range(2)] for q in (F(1, 4), F(1, 2))]
    report("weighted quantile(axis=1) with 1-D weights of length a.shape[1], q array first in the output shape", r.shape == (2, 2) and [[F(float(v)) for v in row] for row in r] == tt, f"{r.tolist()}")
    WM = np.array([[1, 0, 1, 1], [3, 1, 0, 1]])
    r = np.quantile(M, 0.5, axis=1, weights=WM, method="inverted_cdf")
    report("weighted quantile(axis=1) with 2-D weights of a's shape", [F(float(v)) for v in r] == [wq_exact(M[i], WM[i], F(1, 2)) for i in range(2)], f"{r}")
    e = raises(lambda: np.quantile(vals, 0.5, weights=wts)); report("weights with the default method ('linear') raises ValueError ('Only method inverted_cdf supports weights')", (e or "").startswith("ValueError"), str(e))
    e = raises(lambda: np.quantile(vals, 0.5, weights=[1, 1, 1, -1, 1, 1, 1], method="inverted_cdf")); report("negative weight raises ValueError", (e or "").startswith("ValueError"), str(e))
    e = raises(lambda: np.quantile(vals, 0.5, weights=np.zeros(7), method="inverted_cdf")); report("all-zero weights raise ValueError", (e or "").startswith("ValueError"), str(e))
    e = raises(lambda: np.quantile(M, 0.5, weights=wv, method="inverted_cdf")); report("1-D weights with axis=None on 2-D a raises TypeError ('Axis must be specified')", (e or "").startswith("TypeError"), str(e))
    vn = [3.5, nan, 7.25, 0.0, nan, 2.0]; wn = [1, 5, 2, 1, 5, 1]
    ok = all(F(float(np.nanquantile(vn, q, weights=wn, method="inverted_cdf"))) == wq_exact([3.5, 7.25, 0.0, 2.0], [1, 2, 1, 1], F(str(q))) for q in (0.1, 0.2, 0.4, 0.6, 0.8, 1.0))
    report("nanquantile with weights: NaN values and their weights are dropped, then the weighted definition", ok)
    ok = F(float(np.nanpercentile(vn, 60, weights=wn, method="inverted_cdf"))) == wq_exact([3.5, 7.25, 0.0, 2.0], [1, 2, 1, 1], F(3, 5))
    report("nanpercentile with weights = nanquantile(q/100) with weights", ok)
    r = np.quantile(np.array(vals, np.float32), 0.3, weights=wts, method="inverted_cdf")
    report("weighted quantile of float32 data returns float32 and a data value", r.dtype == np.float32 and F(float(r)) == wq_exact(vals, wts, F(3, 10)), f"{r!r}")
else:
    info("weights= for quantile / percentile is 2.0+; not present in this build")

# ================================================================== histogram2d / histogramdd
print("#### histogram2d / histogramdd: edges, range, density, weights, inclusive last bin on every axis")
def bin_of(v, edges):
    """Exact bin index for the documented rule [e_i, e_(i+1)) with the last bin closed; None if outside."""
    v = F(v); E = [F(float(e)) for e in edges]
    if v < E[0] or v > E[-1]: return None
    if v == E[-1]: return len(E) - 2
    for i in range(len(E) - 1):
        if E[i] <= v < E[i + 1]: return i
def hist_exact(points, edges_list, weights=None):
    shape = [len(e) - 1 for e in edges_list]; H = np.zeros(shape, dtype=object); H[...] = F(0)
    for p_i, p in enumerate(points):
        idx = [bin_of(c, e) for c, e in zip(p, edges_list)]
        if any(i is None for i in idx): continue
        H[tuple(idx)] += F(1) if weights is None else fr(weights[p_i])
    return H
def edges_exact(lo, hi, n): return [F(lo) + (F(hi) - F(lo)) * i / n for i in range(n + 1)]
Rh = random.Random(5)
xs = [Rh.randint(-6, 10) / 4 for _ in range(60)] + [-1.0, 2.0, 2.0, -1.0, 0.5, 2.0, 2.5, -1.25]
ys = [Rh.randint(-4, 12) / 4 for _ in range(60)] + [0.0, 3.0, 0.0, 3.0, 3.0, 1.5, 1.0, 3.0]
ws = [Rh.randint(1, 8) / 8 for _ in range(len(xs))]
H, ex, ey = np.histogram2d(xs, ys, bins=[4, 3], range=[[-1, 2], [0, 3]])
report("histogram2d(bins=[4, 3], range=[[-1, 2], [0, 3]]): edges = lo + i (hi - lo) / n exactly", [F(float(e)) for e in ex] == edges_exact(-1, 2, 4) and [F(float(e)) for e in ey] == edges_exact(0, 3, 3))
T = hist_exact(list(zip(xs, ys)), [ex, ey])
report("histogram2d counts: [e_i, e_(i+1)) on each axis, last bin closed on each axis, points outside either range dropped",
       H.shape == (4, 3) and all(H[i, j] == T[i, j] for i in range(4) for j in range(3)), f"total {H.sum()} vs {sum(T.ravel())}")
report("histogram2d: the point (2.0, 3.0) = (x_max edge, y_max edge) lands in H[-1, -1] (inclusive last bin on both axes)",
       np.histogram2d([2.0], [3.0], bins=[4, 3], range=[[-1, 2], [0, 3]])[0][-1, -1] == 1)
report("histogram2d: (2.0, 1.5) -> H[-1, 1]; (2.0 + 1ulp, 1.5) dropped", np.histogram2d([2.0, np.nextafter(2.0, 3)], [1.5, 1.5], bins=[4, 3], range=[[-1, 2], [0, 3]])[0][-1, 1] == 1
       and np.histogram2d([2.0, np.nextafter(2.0, 3)], [1.5, 1.5], bins=[4, 3], range=[[-1, 2], [0, 3]])[0].sum() == 1)
Hw, _, _ = np.histogram2d(xs, ys, bins=[4, 3], range=[[-1, 2], [0, 3]], weights=ws)
Tw = hist_exact(list(zip(xs, ys)), [ex, ey], ws)
report("histogram2d(weights=): per-bin sums of the weights (exact, dyadic weights)", all(Hw[i, j] == Tw[i, j] for i in range(4) for j in range(3)))
Hd, _, _ = np.histogram2d(xs, ys, bins=[4, 3], range=[[-1, 2], [0, 3]], density=True)
area = F(3, 4) * F(1); N = sum(T.ravel())
report("histogram2d(density=True) = bin_count / sample_count_in_range / bin_area (documented), exact",
       all(close(Hd[i, j], float(T[i, j] / N / area), 1e-15) for i in range(4) for j in range(3)), f"N in range {N}")
Hdw, _, _ = np.histogram2d(xs, ys, bins=[4, 3], range=[[-1, 2], [0, 3]], density=True, weights=ws)
Nw = sum(Tw.ravel())
report("histogram2d(density=True, weights=): weights normalised to 1 -> Tw / sum(Tw) / area; integral = 1",
       all(close(Hdw[i, j], float(Tw[i, j] / Nw / area), 1e-14) for i in range(4) for j in range(3)) and close((Hdw * float(area)).sum(), 1.0, 1e-14))
H0, ex0, ey0 = np.histogram2d(xs, ys, bins=5)
report("histogram2d(bins=5) without range: edges span [min, max] of each coordinate", ex0[0] == min(xs) and ex0[-1] == max(xs) and ey0[0] == min(ys) and ey0[-1] == max(ys))
T0 = hist_exact(list(zip(xs, ys)), [ex0, ey0]); report("histogram2d(bins=5): counts exact, every point counted (max point in the last bins)", all(H0[i, j] == T0[i, j] for i in range(5) for j in range(5)) and H0.sum() == len(xs))
bx = [-1.5, -0.25, 0.0, 2.5]
H1, e1, e2 = np.histogram2d(xs, ys, bins=[bx, 2])
T1 = hist_exact(list(zip(xs, ys)), [bx, e2]); report("histogram2d(bins=[edge array, int]): mixed specification, exact", list(e1) == bx and H1.shape == (3, 2) and all(H1[i, j] == T1[i, j] for i in range(3) for j in range(2)))
H2, e1, e2 = np.histogram2d(xs, ys, bins=np.array([-1., 0., 1., 3.]))
T2 = hist_exact(list(zip(xs, ys)), [[-1, 0, 1, 3], [-1, 0, 1, 3]]); report("histogram2d(bins=one array): the same edges on both axes", all(H2[i, j] == T2[i, j] for i in range(3) for j in range(3)))
pts3 = [(Rh.randint(0, 8) / 4, Rh.randint(-4, 4) / 2, Rh.randint(0, 10)) for _ in range(80)] + [(2.0, 2.0, 10), (0.0, -2.0, 0), (2.0, -2.0, 10)]
S3 = np.array(pts3, dtype=float)
Hd3, E3 = np.histogramdd(S3, bins=[[0, 0.5, 1.75, 2.0], 4, 5], range=[None, (-2, 2), (0, 10)])
T3 = hist_exact(pts3, E3)
report("histogramdd((N, 3), bins=[edges, 4, 5], range=[None, (-2, 2), (0, 10)]): exact counts, last bin closed on each axis",
       Hd3.shape == (3, 4, 5) and all(Hd3[idx] == T3[idx] for idx in np.ndindex(3, 4, 5)) and Hd3[-1, -1, -1] >= 1, f"sum {Hd3.sum()} vs {sum(T3.ravel())}")
report("histogramdd edges: explicit array kept, ranges linspace'd exactly", [float(e) for e in E3[0]] == [0, 0.5, 1.75, 2.0] and [F(float(e)) for e in E3[1]] == edges_exact(-2, 2, 4) and [F(float(e)) for e in E3[2]] == edges_exact(0, 10, 5))
Ht, Et = np.histogramdd(tuple(S3.T), bins=[[0, 0.5, 1.75, 2.0], 4, 5], range=[None, (-2, 2), (0, 10)])
report("histogramdd(sequence of D coordinate arrays) == histogramdd((N, D) array) ('unusual interpretation', documented)", np.array_equal(Ht, Hd3))
Hdd, Edd = np.histogramdd(S3, bins=[2, 2, 2], density=True)
vol = [(Edd[0][i + 1] - Edd[0][i]) * (Edd[1][j + 1] - Edd[1][j]) * (Edd[2][k + 1] - Edd[2][k]) for i in range(2) for j in range(2) for k in range(2)]
report("histogramdd(density=True): sum(density * bin volume) = 1", close(sum(d * v for d, v in zip(Hdd.ravel(), vol)), 1.0, 1e-14))
e = raises(lambda: np.histogramdd(S3, bins=[[0, 1, 0.5], 2, 2])); report("histogramdd with non-monotonic edges raises ValueError", (e or "").startswith("ValueError"), str(e))

# ================================================================== histogram_bin_edges estimators
print("#### histogram_bin_edges: the eight string estimators vs the documented formulas")
def est_truth(vals, name):
    """Documented width h (mpmath), or the documented bin count n_h converted to a width via ptp."""
    n = len(vals); lo = min(vals); hi = max(vals); ptp = mp.mpf(F(hi) - F(lo)) if True else None
    ptp = mp.mpf((F(hi) - F(lo)).numerator) / (F(hi) - F(lo)).denominator
    m = mean_x(vals); var = var_x(vals); sig = mp.sqrt(mp.mpf(var.numerator) / var.denominator)
    if name == "sqrt": return ptp / mp.sqrt(n)
    if name == "sturges": return ptp / (mp.log(n, 2) + 1)
    if name == "rice": return ptp / (2 * mp.cbrt(n))
    if name == "scott": return sig * mp.cbrt(24 * mp.sqrt(mp.pi) / n)
    if name == "fd":
        iqr = q7(vals, F(3, 4)) - q7(vals, F(1, 4)); return 2 * (mp.mpf(iqr.numerator) / iqr.denominator) / mp.cbrt(n)
    if name == "doane":
        g1 = sum(((mp.mpf(F(v).numerator) / F(v).denominator - mp.mpf(m.numerator) / m.denominator) / sig) ** 3 for v in vals) / n
        sg1 = mp.sqrt(mp.mpf(6) * (n - 2) / ((n + 1) * (n + 3)))
        return ptp / (1 + mp.log(n, 2) + mp.log(1 + abs(g1) / sg1, 2))
    if name == "auto": return min(est_truth(vals, "fd"), est_truth(vals, "sturges"))
    if name == "stone":
        nb_max = max(100, int(math.isqrt(n))); best = None
        Fl, Fh = F(lo), F(hi)
        for nb in range(1, nb_max + 1):
            cnt = [0] * nb
            for v in vals:
                k = min(int((F(v) - Fl) * nb / (Fh - Fl)), nb - 1); cnt[k] += 1
            J = (2 - F(n + 1, n * n) * sum(c * c for c in cnt)) * nb / (Fh - Fl)
            if best is None or J < best[0]: best = (J, nb)
        return ptp / best[1]
def nbins_truth(vals, name):
    h = est_truth(vals, name); ptp = mp.mpf(float(max(vals)) - float(min(vals)))
    r = ptp / h; nb = int(mp.ceil(r)); near = abs(r - mp.nint(r)) < mp.mpf(1e-9)
    return nb, near, float(r)
Rb = random.Random(99)
dsets = {"n=200 lognormal-ish": [round(math.exp(Rb.gauss(0, 0.7)), 6) for _ in range(200)],
         "n=1000 normal": [round(Rb.gauss(10, 3), 5) for _ in range(1000)],
         "n=37 uniform": [round(Rb.uniform(-5, 5), 4) for _ in range(37)]}
for dn, vals in dsets.items():
    arr = np.array(vals)
    for name in ("sqrt", "sturges", "rice", "scott", "fd", "doane", "stone", "auto"):
        with caught() as c: e = np.histogram_bin_edges(arr, bins=name)
        nb, near, r = nbins_truth(vals, name)
        ok = len(e) - 1 == nb and e[0] == min(vals) and e[-1] == max(vals)
        report(f"histogram_bin_edges({dn}, '{name}'): ceil(ptp / h) = {nb} bins spanning [min, max] (ptp/h = {r:.6f})", ok or near,
               f"numpy {len(e) - 1} bins" + ("  (ptp/h within 1e-9 of an integer: tie, informational)" if near and not ok else ""))
arr = np.array(dsets["n=200 lognormal-ish"])
e = np.histogram_bin_edges(arr, bins="scott", range=(0, 20)); inr = [v for v in dsets["n=200 lognormal-ish"] if 0 <= v <= 20]
h = est_truth(inr, "scott"); nb = int(mp.ceil(20 / h))
report("histogram_bin_edges('scott', range=(0, 20)): width from the in-range data, count fills the whole range: ceil(20 / h)", len(e) - 1 == nb and e[0] == 0 and e[-1] == 20, f"{len(e) - 1} vs {nb}")
# the n^(1/3) / sqrt(n) / log2(n) cases where the documented n_h is an integer
for name, n, nh in (("sqrt", 256, 16), ("sturges", 256, 9), ("rice", 125, 10), ("rice", 1000, 20), ("sqrt", 196, 14), ("sturges", 1024, 11)):
    vals = [i / 7 for i in range(n)]; e = np.histogram_bin_edges(np.array(vals), bins=name)
    report(f"histogram_bin_edges('{name}') on n = {n}: documented n_h = {nh} exactly -> {nh} bins", len(e) - 1 == nh, f"numpy {len(e) - 1} bins")
# 'auto' where FD is much narrower than sqrt/2 (heavy tails, n = 5000)
Ra = random.Random(3); vals = [round(Ra.gauss(0, 1), 6) for _ in range(4990)] + [round(Ra.uniform(-400, 400), 3) for _ in range(10)]
nb_doc, near, r = nbins_truth(vals, "auto"); e = np.histogram_bin_edges(np.array(vals), bins="auto")
nb_fd = nbins_truth(vals, "fd")[0]; nb_sq = nbins_truth(vals, "sqrt")[0]
info(f"heavy-tailed n=5000: fd -> {nb_fd} bins, sturges -> {nbins_truth(vals, 'sturges')[0]}, sqrt -> {nb_sq}; numpy 'auto' -> {len(e) - 1}")
report("histogram_bin_edges('auto') = 'Minimum bin width between the sturges and fd estimators' on heavy-tailed n=5000 data",
       len(e) - 1 == nb_doc, f"documented {nb_doc} bins, numpy {len(e) - 1}")
iv = np.array([Rb.randint(0, 9) for _ in range(10000)])
for name in ("sqrt", "fd", "auto"):
    e = np.histogram_bin_edges(iv, bins=name)
    if NPV >= (2, 1):
        report(f"integer data, '{name}' on n=10000 values 0..9: 'binwidth will never be less than 1' -> 9 bins (2.1+)", len(e) - 1 == 9, f"{len(e) - 1} bins")
    else:
        info(f"integer data '{name}' n=10000 in 0..9: {len(e) - 1} bins (the width >= 1 rule is 2.1+)")
e = np.histogram_bin_edges(np.array([1., 1., 1., 1., 1., 2.]), bins="fd")
report("'fd' with IQR = 0 -> width 0 -> 1 bin (documented 'If the IQR is 0, this function returns 0 for the bin width')", len(e) - 1 == 1, f"{len(e) - 1}")
e = raises(lambda: np.histogram_bin_edges(np.arange(5.), bins="auto", weights=np.ones(5)))
report("string estimator with weights raises TypeError ('Weighted data is not supported for automated bin size selection')", (e or "").startswith("TypeError"), str(e))
e = raises(lambda: np.histogram_bin_edges(np.arange(5.), bins="bogus")); report("unknown estimator name raises ValueError", (e or "").startswith("ValueError"), str(e))
e = np.histogram_bin_edges(np.array([]), bins="auto"); report("empty data with 'auto': one bin on [0, 1]", list(e) == [0.0, 1.0], f"{e}")

# ================================================================== bincount
print("#### bincount: weights, minlength")
bx = [0, 3, 3, 1, 7, 3, 0]; bw = [0.5, 1.25, -2.0, 4.0, 0.125, 1.0, 3.0]
r = np.bincount(bx); report("bincount: length max+1 = 8, counts exact, integer dtype", list(r) == [2, 1, 0, 3, 0, 0, 0, 1] and r.dtype.kind == "i")
r = np.bincount(bx, weights=bw); t = [sum(fr(w) for v, w in zip(bx, bw) if v == k) for k in range(8)]
report("bincount(weights=): out[n] += weight[i] (exact), float64 result", [F(float(v)) for v in r] == t and r.dtype == np.float64, f"{r.tolist()}")
report("bincount(minlength=12): length 12, zero-padded", list(np.bincount(bx, minlength=12)) == [2, 1, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0])
report("bincount(minlength=3) smaller than max+1: length stays 8", len(np.bincount(bx, minlength=3)) == 8)
report("bincount([], minlength=4) = four zeros", list(np.bincount(np.array([], dtype=int), minlength=4)) == [0, 0, 0, 0])
e = raises(lambda: np.bincount([1, -1, 2])); report("bincount with a negative value raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.bincount(np.array([1.5, 2.]))); report("bincount of a float ndarray raises TypeError (cannot cast safely to intp)", (e or "").startswith("TypeError"), str(e))
with caught() as c: r = np.bincount([1.5, 2.7])
if NPV >= (2, 1):
    report("bincount of a Python list of non-integer floats: DeprecationWarning 'Non-integer input passed to bincount' (2.1+)", "DeprecationWarning" in c.cats, f"{r.tolist()} {c.msgs}")
else:
    info(f"bincount([1.5, 2.7]) (list of floats) silently truncates in this build: {r.tolist()} (deprecated in 2.1)")
r = np.bincount(np.array([1, 1, 2], dtype=np.uint8), weights=np.array([1, 2, 3], dtype=np.int64)); report("bincount(int weights) returns float64", r.dtype == np.float64 and list(r) == [0, 3, 3])

# ================================================================== cumulative sums / products
print("#### cumsum / cumprod / nancumsum / nancumprod: dtypes and NaN handling")
def wrap_int(v, dt):
    info_ = np.iinfo(dt); bits = info_.bits; v = int(v) % (1 << bits)
    if info_.min < 0 and v >= 1 << (bits - 1): v -= 1 << bits
    return v
def pycum(v, op="+"):
    out = []; acc = 0 if op == "+" else 1
    for t in v: acc = acc + t if op == "+" else acc * t; out.append(acc)
    return out
PI = np.dtype(np.int_); PU = np.dtype(np.uint64) if PI.itemsize == 8 else np.dtype(np.uint32)
i8 = np.array([100, 100, 100, -128, 127, 90], dtype=np.int8)
r = np.cumsum(i8); report("cumsum(int8) accumulates in the platform integer (no wrap): dtype int_, values exact", r.dtype == PI and list(r) == pycum(i8.tolist()), f"{r.dtype} {r.tolist()}")
r = np.cumsum(i8, dtype=np.int8); report("cumsum(int8, dtype=int8) wraps modulo 2^8 ('Arithmetic is modular when using integer types')", r.dtype == np.int8 and list(r) == [wrap_int(v, np.int8) for v in pycum(i8.tolist())])
u8 = np.array([200, 100, 250], dtype=np.uint8)
r = np.cumsum(u8); report("cumsum(uint8) -> unsigned platform integer (uint64), exact", r.dtype == PU and list(r) == [200, 300, 550], f"{r.dtype}")
r = np.cumsum(np.array([True, True, False, True])); report("cumsum(bool) -> platform int counts", r.dtype == PI and list(r) == [1, 2, 2, 3])
r = np.cumprod(np.array([10, 20, 30, 40], dtype=np.int8)); report("cumprod(int8) -> platform int, exact products", r.dtype == PI and list(r) == [10, 200, 6000, 240000])
r = np.cumprod(np.array([3, 5, 7], dtype=np.uint16)); report("cumprod(uint16) -> uint64", r.dtype == PU and list(r) == [3, 15, 105])
r = np.cumsum(np.array([1.5, 2.25], dtype=np.float32)); report("cumsum(float32) stays float32", r.dtype == np.float32 and list(r) == [1.5, 3.75])
r = np.cumsum([1., 2., nan, 4., 5.]); report("cumsum with a NaN: NaN from that position on", r[:2].tolist() == [1., 3.] and bool(np.all(np.isnan(r[2:]))))
r = np.cumsum([1., inf, -inf, 2.]); report("cumsum [1, inf, -inf, 2] -> [1, inf, nan, nan]", r[0] == 1 and r[1] == inf and np.isnan(r[2]) and np.isnan(r[3]))
r = np.nancumsum([nan, 1., nan, 2., 4.]); report("nancumsum: NaN treated as 0 ('Zeros are substituted for NaNs'): [0, 1, 1, 3, 7]", r.tolist() == [0., 1., 1., 3., 7.])
r = np.nancumprod([nan, 2., nan, 3., 0.5]); report("nancumprod: NaN treated as 1: [1, 2, 2, 6, 3]", r.tolist() == [1., 2., 2., 6., 3.])
r = np.nancumsum(np.array([[nan, nan], [nan, nan]]), axis=0); report("nancumsum of all-NaN -> zeros", r.tolist() == [[0., 0.], [0., 0.]])
r = np.nancumprod(np.array([[nan, 2.], [3., nan]]), axis=1); report("nancumprod(axis=1)", r.tolist() == [[1., 2.], [3., 3.]])
r = np.nancumsum(np.array([1, 2, 3], dtype=np.int8)); report("nancumsum(int8) = cumsum(int8) (dtype int_)", r.dtype == PI and r.tolist() == [1, 3, 6])
M2 = np.array([[1, 2, 3], [4, 5, 6]])
report("cumsum(axis=None) flattens in C order", np.cumsum(M2).tolist() == [1, 3, 6, 10, 15, 21])
report("cumsum(axis=0) / cumprod(axis=1)", np.cumsum(M2, axis=0).tolist() == [[1, 2, 3], [5, 7, 9]] and np.cumprod(M2, axis=1).tolist() == [[1, 2, 6], [4, 20, 120]])
if hasattr(np, "cumulative_sum"):
    x1 = np.array([3, -1, 4, 1, -5])
    r = np.cumulative_sum(x1, include_initial=True); report("cumulative_sum(include_initial=True): [0] + partial sums, length n + 1", r.tolist() == [0] + pycum(x1.tolist()), f"{r.tolist()}")
    r = np.cumulative_sum(x1); report("cumulative_sum default (include_initial=False) == cumsum", r.tolist() == pycum(x1.tolist()))
    r = np.cumulative_prod(x1, include_initial=True); report("cumulative_prod(include_initial=True): [1] + partial products", r.tolist() == [1] + pycum(x1.tolist(), "*"))
    r = np.cumulative_sum(M2, axis=1, include_initial=True); report("cumulative_sum(2-D, axis=1, include_initial=True): shape (2, 4), leading zero column", r.shape == (2, 4) and r.tolist() == [[0, 1, 3, 6], [0, 4, 9, 15]])
    r = np.cumulative_prod(M2, axis=0, include_initial=True); report("cumulative_prod(axis=0, include_initial=True): shape (3, 3), leading ones row", r.tolist() == [[1, 1, 1], [1, 2, 3], [4, 10, 18]])
    e = raises(lambda: np.cumulative_sum(M2)); report("cumulative_sum of 2-D without axis raises ValueError (axis required for ndim > 1)", (e or "").startswith("ValueError"), str(e))
    r = np.cumulative_sum(np.array([1, 2], np.int8)); report("cumulative_sum(int8) dtype follows cumsum (platform int)", r.dtype == PI, f"{r.dtype}")
    r = np.cumulative_sum(np.array([], dtype=float), include_initial=True); report("cumulative_sum(empty, include_initial=True) = [0.]", r.tolist() == [0.0])
    r = np.cumulative_sum(np.array([True, False, True]), include_initial=True); report("cumulative_sum(bool, include_initial=True) = [0, 1, 1, 2]", r.tolist() == [0, 1, 1, 2])
else:
    info("cumulative_sum / cumulative_prod are 2.1+; not present in this build")

# ================================================================== diff / ediff1d
print("#### diff (n, prepend, append, bool, uint, datetime) and ediff1d")
d = [1, 4, 9, 16, 25, 36]
report("diff(n=1) exact", np.diff(d).tolist() == [3, 5, 7, 9, 11])
report("diff(n=2) = second differences (constant 2 for squares)", np.diff(d, n=2).tolist() == [2, 2, 2, 2])
report("diff(n=3) of squares = 0", np.diff(d, n=3).tolist() == [0, 0, 0])
a_ = np.array(d); report("diff(n=0) returns the input as-is", np.diff(a_, n=0) is a_ or np.array_equal(np.diff(a_, n=0), a_))
r = np.diff(d, n=7); report("diff(n > len) -> empty result", r.shape == (0,), f"{r.shape}")
e = raises(lambda: np.diff(d, n=-1)); report("diff(n=-1) raises ValueError", (e or "").startswith("ValueError"), str(e))
report("diff(prepend=0, append=100)", np.diff(d, prepend=0, append=100).tolist() == [1, 3, 5, 7, 9, 11, 64])
M3 = np.array([[1, 3, 6], [10, 15, 21]])
report("diff(2-D, axis=0, prepend=scalar) broadcasts the scalar to a row", np.diff(M3, axis=0, prepend=0).tolist() == [[1, 3, 6], [9, 12, 15]])
report("diff(2-D, axis=1, append=[[7], [8]])", np.diff(M3, axis=1, append=[[7], [8]]).tolist() == [[2, 3, 1], [5, 6, -13]])
e = raises(lambda: np.diff(M3, axis=1, append=[7, 8, 9])); report("diff with append of the wrong shape raises ValueError", (e or "").startswith("ValueError"), str(e))
r = np.diff(np.array([True, True, False, True, True])); report("diff(bool): type preserved, True where consecutive elements differ", r.dtype == bool and r.tolist() == [False, True, True, False])
r = np.diff(np.array([1, 0, 5, 3], dtype=np.uint8)); report("diff(uint8) wraps: [1, 0] -> 255 (documented), [5, 3] -> 254", r.dtype == np.uint8 and r.tolist() == [255, 5, 254])
r = np.diff(np.array([-128, 127, -128], dtype=np.int8)); report("diff(int8) keeps int8 and wraps: 127 - (-128) -> -1, -128 - 127 -> 1", r.dtype == np.int8 and r.tolist() == [-1, 1])
dt = np.array(["2024-02-27", "2024-03-01", "2025-03-01"], dtype="datetime64[D]")
r = np.diff(dt); report("diff(datetime64[D]) -> timedelta64[D] (documented exception), leap-year exact", r.dtype == np.dtype("timedelta64[D]") and r.astype(int).tolist() == [3, 365])
r = np.diff(dt, n=2); report("diff(datetime64, n=2) -> timedelta64 second difference", r.dtype.kind == "m" and r.astype(int).tolist() == [362])
r = np.diff(np.array([0.1, 0.3, 0.7])); report("diff(float) = correctly rounded pairwise differences", r.tolist() == [0.3 - 0.1, 0.7 - 0.3])
r = np.ediff1d([1, 2, 4, 7, 0]); report("ediff1d = flat[1:] - flat[:-1]", r.tolist() == [1, 2, 3, -7])
r = np.ediff1d([1, 2, 4, 7, 0], to_begin=-99, to_end=np.array([88, 99])); report("ediff1d(to_begin=-99, to_end=[88, 99])", r.tolist() == [-99, 1, 2, 3, -7, 88, 99])
r = np.ediff1d([[1, 2, 4], [1, 6, 24]]); report("ediff1d flattens 2-D input (always 1-D)", r.tolist() == [1, 2, -3, 5, 18])
r = np.ediff1d([5.], to_begin=[1, 2]); report("ediff1d of a single element: empty differences, only to_begin", r.tolist() == [1., 2.])
e = raises(lambda: np.ediff1d(np.array([1, 2, 4]), to_begin=0.5))
info(f"ediff1d(int array, to_begin=0.5): {e or np.ediff1d(np.array([1, 2, 4]), to_begin=0.5).tolist()} (the docstring does not state the cast rule)")
r = np.ediff1d(np.array([1, 0], dtype=np.uint8)); report("ediff1d(uint8) keeps uint8 and wraps like diff", r.dtype == np.uint8 and r.tolist() == [255])

# ================================================================== sum / prod dtype, empty, initial, where; max / min; ptp
print("#### sum / prod dtype rules, empty reductions, initial= and where=")
for dt_, exp_ in ((np.int8, PI), (np.int16, PI), (np.int32, PI), (np.int64, PI), (np.uint8, PU), (np.uint16, PU), (np.uint32, PU), (np.bool_, PI),
                  (np.float16, np.float16), (np.float32, np.float32)):
    rs = np.sum(np.ones(3, dtype=dt_)); rp = np.prod(np.ones(3, dtype=dt_))
    report(f"sum / prod of {np.dtype(dt_).name}: result dtype {np.dtype(exp_).name} (integer narrower than platform int -> int_ / uint)", rs.dtype == exp_ and rp.dtype == exp_, f"{rs.dtype} {rp.dtype}")
big = np.full(300, 100, dtype=np.int8)
report("sum of 300 x int8(100) = 30000 exactly (accumulated in int_)", np.sum(big) == 30000)
report("sum(int8, dtype=int8) wraps modulo 2^8", np.sum(big, dtype=np.int8) == wrap_int(30000, np.int8))
report("sum(bool) counts True", np.sum(np.array([True, False, True, True])) == 3)
report("prod of 12 x int8(10) = 10^12 in int64 exactly", np.prod(np.full(12, 10, dtype=np.int8)) == 10 ** 12)
r = np.sum(np.array([], dtype=float)); report("sum of an empty float array = 0.0", r == 0.0 and r.dtype == np.float64)
r = np.prod(np.array([], dtype=float)); report("prod of an empty array = 1.0", r == 1.0)
r = np.sum(np.array([], dtype=np.int8)); report("sum of an empty int8 array = 0 of dtype int_", r == 0 and r.dtype == PI)
r = np.sum(np.zeros((0, 3)), axis=0); report("sum over a zero-length axis: zeros of the remaining shape", r.tolist() == [0., 0., 0.])
report("sum(initial=5) = 5 + sum", np.sum([1, 2, 3], initial=5) == 11)
report("prod(initial=2) = 2 * prod", np.prod([1, 2, 3], initial=2) == 12)
report("sum(empty, initial=5) = 5", np.sum([], initial=5) == 5)
wm = np.array([True, False, True, False]); vv = np.array([1., 20., 300., 4000.])
report("sum(where=mask) sums only the selected elements", np.sum(vv, where=wm) == 301.0)
report("sum(where=mask, initial=0.5)", np.sum(vv, where=wm, initial=0.5) == 301.5)
report("prod(where=mask)", np.prod(vv, where=wm) == 300.0)
report("mean(where=mask) = mean of the selected elements", np.mean(vv, where=wm) == 150.5)
r = np.sum(np.array([[1, 2], [3, 4]]), axis=1, where=np.array([[True, False], [False, True]])); report("sum(axis=1, where=2-D mask)", r.tolist() == [1, 4])
print("#### max / min with initial and where; ptp")
e = raises(lambda: np.max(np.array([]))); report("max of an empty array raises ValueError (no identity)", (e or "").startswith("ValueError"), str(e))
report("max(empty, initial=-inf) = -inf", np.max(np.array([]), initial=-inf) == -inf)
report("max(initial=100) larger than every element returns 100", np.max([1, 5, 3], initial=100) == 100)
report("max(initial=0) smaller than every element returns the max", np.max([1, 5, 3], initial=0) == 5)
report("min(initial=-7) returns -7", np.min([1, 5, 3], initial=-7) == -7)
report("max(where=mask, initial=-inf) over the selected elements", np.max(vv, where=np.array([True, False, True, False]), initial=-inf) == 300.0)
report("min(where=mask, initial=inf)", np.min(vv, where=np.array([False, True, False, True]), initial=inf) == 20.0)
e = raises(lambda: np.max(vv, where=wm)); report("max(where=mask) without initial raises ValueError (no identity for maximum)", (e or "").startswith("ValueError"), str(e))
r = np.max(np.array([[1, 9], [7, 2]]), axis=0, where=np.array([[True, False], [False, False]]), initial=-1); report("max(axis=0, where, initial=-1): a column with nothing selected gives initial", r.tolist() == [1, -1])
report("max with NaN propagates NaN", bool(np.isnan(np.max([1., nan, 3.]))))
r = np.ptp(np.array([-128, 127], dtype=np.int8)); report("ptp(int8 [-128, 127]) = 255 wraps to -1 (documented: 'values greater than 2**(n-1)-1 will be returned as negative values')", r == -1 and r.dtype == np.int8, f"{r!r}")
r = np.ptp(np.array([0, 255], dtype=np.uint8)); report("ptp(uint8 [0, 255]) = 255", r == 255)
r = np.ptp(np.array([[4, 9, 2], [3, 5, 7]]), axis=1); report("ptp(axis=1)", r.tolist() == [7, 4])
report("ptp with NaN is NaN", bool(np.isnan(np.ptp([1., nan, 2.]))))
e = raises(lambda: np.ptp(np.array([]))); report("ptp of an empty array raises ValueError", (e or "").startswith("ValueError"), str(e))
r = np.ptp(np.array([[1, 5], [2, 9]]), axis=0, keepdims=True); report("ptp(keepdims=True) shape (1, 2)", r.shape == (1, 2) and r.tolist() == [[1, 4]])

# ================================================================== convolve / correlate
print("#### convolve / correlate: full / same / valid, odd / even lengths, complex conjugation, swap")
def conv_full(a, v):
    M, N = len(a), len(v); return [sum(a[m] * v[n - m] for m in range(M) if 0 <= n - m < N) for n in range(M + N - 1)]
def corr_full(a, v):
    """c_k = sum_n a[n+k] conj(v[n]) for k = -(N-1) .. M-1 (the documented definition, lag order ascending)."""
    M, N = len(a), len(v); return [sum(a[n + k] * complex(v[n]).conjugate() for n in range(N) if 0 <= n + k < M) for k in range(-(N - 1), M)]
Rc = random.Random(17)
def rc(n): return [complex(Rc.randint(-9, 9), Rc.randint(-9, 9)) for _ in range(n)]
same_windows = []
for M, N in [(7, 3), (7, 4), (6, 3), (6, 4), (3, 7), (4, 7), (3, 6), (4, 6), (5, 5), (4, 4), (1, 5), (5, 1), (2, 9)]:
    a, v = rc(M), rc(N); A_, V_ = np.array(a), np.array(v)
    full = conv_full(a, v); lo, hi = min(M, N), max(M, N)
    ok = allclose(np.convolve(A_, V_), full, 0, 0) and allclose(np.convolve(A_, V_, "valid"), full[lo - 1: hi], 0, 0)
    s = (lo - 1) // 2; ok &= allclose(np.convolve(A_, V_, "same"), full[s: s + hi], 0, 0) and len(np.convolve(A_, V_, "same")) == hi
    report(f"convolve complex (M={M}, N={N}): full = sum a_m v_(n-m); valid = the max-min+1 fully overlapping values; same = length max(M,N) centred", ok)
    cf = corr_full(a, v); r = np.correlate(A_, V_, "full")
    ok = allclose(r, cf, 0, 0)
    k0, k1 = min(0, M - N), max(0, M - N); vv_ = np.correlate(A_, V_)       # default 'valid'
    ok_valid = allclose(vv_, cf[k0 + N - 1: k1 + N], 0, 0)
    rs = np.correlate(A_, V_, "same"); rsw = np.correlate(V_, A_, "same")
    report(f"correlate complex (M={M}, N={N}) full: c_k = sum_n a[n+k] conj(v[n]), k = -(N-1)..M-1", ok)
    report(f"correlate (M={M}, N={N}) default mode 'valid' = lags min(0, M-N)..max(0, M-N)", ok_valid and len(vv_) == hi - lo + 1)
    report(f"correlate (M={M}, N={N}) swapped inputs: full = time-reversed, conjugated (documented)", allclose(np.correlate(V_, A_, "full"), [z.conjugate() for z in cf[::-1]], 0, 0))
    st = [i for i in range(len(cf) - hi + 1) if allclose(rs, cf[i: i + hi], 0, 0)]
    report(f"correlate (M={M}, N={N}) 'same': length max(M, N), a contiguous window of the full correlation", len(rs) == hi and len(st) >= 1)
    if not allclose(rsw, [complex(z).conjugate() for z in rs[::-1]], 0, 0):
        info(f"correlate 'same' (M={M}, N={N}): swapping a and v does NOT give the reversed conjugate (even overlap length: no centring rule can be reversal-symmetric; only shown for 'full' in the docstring)")
    same_windows.append(f"(M={M},N={N}): full[{st[0] if st else '?'}:+{hi}] (convolve's centring (min-1)//2 = {s})")
info("correlate 'same' takes these windows of the full output (undocumented beyond 'length max(M, N)'): " + "; ".join(same_windows))
ia = [3, -1, 4, 1, -5, 9, 2]; iv = [2, 7, -1, 8]
r = np.convolve(ia, iv); report("convolve of int lists: int result, exact", r.dtype.kind == "i" and r.tolist() == conv_full(ia, iv))
r = np.correlate(ia, iv, "full"); report("correlate of int lists 'full': exact, integer dtype", r.dtype.kind == "i" and r.tolist() == [int(z.real) for z in corr_full(ia, iv)])
report("correlate([1, 2, 3], [0, 1, 0.5], 'same') = [2, 3.5, 3] (docstring example)", np.correlate([1, 2, 3], [0, 1, 0.5], "same").tolist() == [2.0, 3.5, 3.0])
report("correlate([1, 1], [1..6], 'valid') = [11, 9, 7, 5, 3] (lags -4..0, docstring)", np.correlate([1, 1], [1, 2, 3, 4, 5, 6], "valid").tolist() == [11, 9, 7, 5, 3])
e = raises(lambda: np.convolve([], [1, 2])); report("convolve with an empty input raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.correlate([1, 2], [1], "bogus")); report("correlate with an unknown mode raises ValueError", (e or "").startswith("ValueError"), str(e))
r = np.convolve(np.ones(3, np.float32), np.ones(2, np.float32)); report("convolve(float32, float32) returns float32", r.dtype == np.float32)

# ================================================================== piecewise / select / where
print("#### piecewise")
x = np.linspace(-2, 2, 9)
r = np.piecewise(x, [x < 0, x >= 0], [lambda t: -t, lambda t: t ** 2]); report("piecewise(x, [x<0, x>=0], [-x, x^2]) exact", r.tolist() == [(-t if t < 0 else t * t) for t in x.tolist()])
r = np.piecewise(x, [x < -1, x > 1], [-1, 5]); report("piecewise with scalars in funclist = constant functions; uncovered points default to 0",
                                                      r.tolist() == [(-1.0 if t < -1 else 5.0 if t > 1 else 0.0) for t in x.tolist()])
r = np.piecewise(x, [x < -1, x > 1], [-1, 5, lambda t: 100 + t]); report("piecewise with len(funclist) == len(condlist) + 1: the extra function is the default where all conditions are False",
                                                                         r.tolist() == [(-1.0 if t < -1 else 5.0 if t > 1 else 100 + t) for t in x.tolist()])
e = raises(lambda: np.piecewise(x, [x < 0, x > 0], [1, 2, 3, 4])); report("piecewise with len(funclist) = len(condlist) + 2 raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.piecewise(x, [x < 0, x > 0, x > 1], [1])); report("piecewise with too few functions raises ValueError", (e or "").startswith("ValueError"), str(e))
r = np.piecewise(x, x > 0, [1, -1]); report("piecewise with a single boolean array as condlist and [f, default]", r.tolist() == [(1.0 if t > 0 else -1.0) for t in x.tolist()])
r = np.piecewise(np.arange(4), [np.arange(4) > 1], [lambda t: t * 0.5]); report("piecewise output has the type of x ('same shape and type as x'): int x, float function -> truncated ints", r.dtype.kind == "i" and r.tolist() == [0, 0, 1, 1], f"{r.tolist()}")
r = np.piecewise(x, [x < 0, x >= 0], [lambda t, k: k * t, lambda t, k: -k * t], k=3); report("piecewise passes **kw to every function", r.tolist() == [(3 * t if t < 0 else -3 * t) for t in x.tolist()])
r = np.piecewise(x, [x < 0, x >= 0], [lambda t, k: k * t, lambda t, k: k], 2.0); report("piecewise passes *args to every function", r.tolist() == [(2 * t if t < 0 else 2.0) for t in x.tolist()])
r = np.piecewise(np.array(3.0), [True], [lambda t: t * 2]); report("piecewise on a 0-d x", float(r) == 6.0 and np.ndim(r) == 0)
r = np.piecewise(x, [x < 1, x > -1], [10, 20])
info(f"piecewise with overlapping conditions [x<1, x>-1] -> {r.tolist()} (later condition wins; the docstring does not state the priority, np.select uses the first)")
print("#### select")
x6 = np.arange(6)
report("select docstring example: [x<3, x>3], [-x, x^2], default 42", np.select([x6 < 3, x6 > 3], [-x6, x6 ** 2], 42).tolist() == [0, -1, -2, 42, 16, 25])
report("select: 'When multiple conditions are satisfied, the first one encountered in condlist is used'", np.select([x6 <= 4, x6 > 3], [x6, x6 ** 2], 55).tolist() == [0, 1, 2, 3, 4, 25])
cr = np.array([[True], [False], [True]]); ch = np.array([[1, 2, 3, 4]])
r = np.select([cr, ~cr], [ch, -ch], default=0); report("select broadcasts condlist (3, 1) against choices (1, 4) -> (3, 4)", r.shape == (3, 4) and r.tolist() == [[1, 2, 3, 4], [-1, -2, -3, -4], [1, 2, 3, 4]])
r = np.select([x6 > 2], [7], default=0); report("select with scalar choices and default", r.tolist() == [0, 0, 0, 7, 7, 7])
r = np.select([x6 > 2], [x6], default=np.nan); report("select(int choices, default=nan) -> float64 with NaN", r.dtype == np.float64 and np.isnan(r[0]) and r[3] == 3.0)
e = raises(lambda: np.select([], [])); report("select with empty condlist raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.select([x6 > 1, x6 > 2], [x6])); report("select with len(condlist) != len(choicelist) raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.select([x6], [x6])); report("select with a non-boolean condition raises TypeError", (e or "").startswith("TypeError"), str(e))
c2 = np.array([True, False]); a8 = np.array([1, 2], np.int8)
for what, fn in (("default=300 with int8 choices", lambda: np.select([c2], [a8], default=300)),
                 ("default=-129 with int8 choices", lambda: np.select([c2], [a8], default=-129)),
                 ("choice 300 (Python int) with default int8(1)", lambda: np.select([c2], [300], default=np.int8(1)))):
    try:
        r = fn(); val = 300 if "300" in what else -129
        ok = val in r.tolist(); det = f"{r.tolist()} dtype {r.dtype}"
    except Exception as ex:
        ok = True; det = f"raises {type(ex).__name__}"
    report(f"select {what}: the value appears in the output (or an error is raised), not a silently wrapped value", ok, det)
print("#### where with scalars")
cw = np.array([True, False, True])
r = np.where(cw, 1, 2); report("where(c, 1, 2) -> integer [1, 2, 1]", r.dtype.kind == "i" and r.tolist() == [1, 2, 1])
r = np.where(cw, 1, 2.5); report("where(c, 1, 2.5) -> float64", r.dtype == np.float64 and r.tolist() == [1.0, 2.5, 1.0])
r = np.where(cw, np.array([1, 2, 3], np.int8), 5); report("where(c, int8 array, 5) -> int8 (value-based in 1.x, weak scalar in 2.x)", r.dtype == np.int8 and r.tolist() == [1, 5, 3], f"{r.dtype}")
r = np.where(cw, np.array([1., 2, 3], np.float32), 0.5); report("where(c, float32 array, 0.5) -> float32", r.dtype == np.float32 and r.tolist() == [1.0, 0.5, 3.0])
try:
    r = np.where(cw, np.array([1, 2, 3], np.int8), 300); ok = 300 in r.tolist(); det = f"{r.tolist()} dtype {r.dtype}"
except Exception as ex:
    ok = True; det = f"raises {type(ex).__name__}: {ex}"
report("where(c, int8 array, 300): 300 appears in the output (or an error is raised), not a silently wrapped value", ok, det)
r = np.where(np.array([[True], [False]]), np.array([1, 2, 3]), -1); report("where broadcasts condition (2, 1) with x (3,) and scalar y", r.tolist() == [[1, 2, 3], [-1, -1, -1]])
r = np.where(np.array([[0, 3], [5, 0]])); report("where(condition) alone == nonzero", [t.tolist() for t in r] == [[0, 1], [1, 0]])
e = raises(lambda: np.where(cw, 1)); report("where with only x (no y) raises ValueError", (e or "").startswith("ValueError"), str(e))

# ================================================================== interp
print("#### interp: period, left / right, complex fp, decreasing xp, NaN in xp")
def interp_x(x, xp, fp, left=None, right=None):
    x = F(x); xp = [F(t) for t in xp]
    if x < xp[0]: return fp[0] if left is None else left
    if x > xp[-1]: return fp[-1] if right is None else right
    for i in range(len(xp) - 1):
        if xp[i] <= x <= xp[i + 1]:
            if x == xp[i + 1]: return fp[i + 1]
            fa, fb = fp[i], fp[i + 1]
            if isinstance(fa, complex) or isinstance(fb, complex):
                t = (x - xp[i]) / (xp[i + 1] - xp[i]); return complex(fa) + complex(fb - fa) * float(t)
            return F(fa) + (x - xp[i]) * (F(fb) - F(fa)) / (xp[i + 1] - xp[i])
    return fp[-1]
def interp_period_x(x, xp, fp, p):
    p = F(p); pts = sorted(((F(a) % p, b) for a, b in zip(xp, fp)), key=lambda t: t[0])
    ext = [(pts[-1][0] - p, pts[-1][1])] + pts + [(pts[0][0] + p, pts[0][1])]
    return interp_x(F(x) % p, [a for a, _ in ext], [b for _, b in ext])
Ri = random.Random(8)
xp = sorted(set(Ri.randint(-40, 40) / 8 for _ in range(12))); fp = [Ri.randint(-50, 50) / 4 for _ in xp]
xq = [Ri.uniform(-6, 6) for _ in range(40)] + xp + [xp[0] - 1, xp[-1] + 1]
r = np.interp(xq, xp, fp); report("interp at 54 points (incl. every xp and both sides): exact piecewise-linear value, fp[0] / fp[-1] outside",
                                  all(close(a, float(interp_x(t, xp, fp)), 1e-14, 1e-14) for a, t in zip(r, xq)))
report("interp at x == xp[i] returns fp[i] exactly", np.interp(xp, xp, fp).tolist() == fp)
r = np.interp([xp[0] - 1, xp[-1] + 1], xp, fp, left=-99.0, right=99.0); report("interp(left=-99, right=99) used outside [xp[0], xp[-1]]", r.tolist() == [-99.0, 99.0])
r = np.interp([xp[0], xp[-1]], xp, fp, left=-99.0, right=99.0); report("interp left / right do not apply at the end points themselves", r.tolist() == [fp[0], fp[-1]])
report("interp(x=NaN) is NaN", bool(np.isnan(np.interp(nan, xp, fp))))
x_doc = [-180, -170, -185, 185, -10, -5, 0, 365]; xp_doc = [190, -190, 350, -350]; fp_doc = [5, 10, 3, 4]
r = np.interp(x_doc, xp_doc, fp_doc, period=360)
report("interp(period=360) docstring example -> [7.5, 5, 8.75, 6.25, 3, 3.25, 3.5, 3.75]", r.tolist() == [7.5, 5., 8.75, 6.25, 3., 3.25, 3.5, 3.75])
report("interp(period=360) equals the periodic-extension definition (xp % period, sorted, wrapped) exactly", all(close(a, float(interp_period_x(t, xp_doc, fp_doc, 360)), 1e-15) for a, t in zip(r, x_doc)))
angs = [Ri.randint(-720, 720) / 4 for _ in range(30)]; xpa = [10, 100, 200, 300, 355]; fpa = [1.0, -2.0, 4.0, 0.5, 3.0]
r = np.interp(angs, xpa, fpa, period=360)
report("interp(period=360) on 30 angles in [-180, 180]*4 (wrap-around segment 355 -> 370)", all(close(a, float(interp_period_x(t, xpa, fpa, 360)), 1e-14, 1e-14) for a, t in zip(r, angs)))
r2 = np.interp(angs, xpa, fpa, period=360, left=-1e9, right=1e9); report("interp(period=..): left / right ignored ('Parameters left and right are ignored if period is specified')", np.array_equal(r, r2))
e = raises(lambda: np.interp([1], [0, 1], [0, 1], period=0)); report("interp(period=0) raises ValueError", (e or "").startswith("ValueError"), str(e))
tp = 2 * math.pi; r = np.interp([0.1, tp - 0.1], [-0.5, 0.5], [1.0, 3.0], period=tp)
t_ = [float(interp_period_x(v, [-0.5, 0.5], [1.0, 3.0], F(tp))) for v in (0.1, tp - 0.1)]
report("interp(period=2pi) on angles in radians, wrapping near 0 and 2pi", allclose(r, t_, 1e-13), f"{r.tolist()} vs {t_}")
fpc = [complex(Ri.randint(-9, 9), Ri.randint(-9, 9)) for _ in xp]
r = np.interp(xq[:40], xp, fpc); report("interp with complex fp interpolates real and imaginary parts", all(close(a, complex(interp_x(t, xp, fpc)), 1e-14, 1e-14) for a, t in zip(r, xq[:40])) and r.dtype.kind == "c")
r = np.interp([xp[0] - 1, xp[-1] + 1], xp, fpc, left=1j, right=-1j); report("interp complex fp with complex left / right", r.tolist() == [1j, -1j])
e = raises(lambda: np.interp([1], [0, 1, 2], [0, 1])); report("interp with len(xp) != len(fp) raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.interp([1], [], [])); report("interp with empty xp raises ValueError", (e or "").startswith("ValueError"), str(e))
r = np.interp([0.5, 1.5, 2.5], [3, 2, 1, 0], [30, 20, 10, 0])
info(f"interp with decreasing xp [3, 2, 1, 0] at [0.5, 1.5, 2.5] -> {r.tolist()} (documented: 'If xp is not increasing, the results are nonsense'; the increasing reorder would give [5, 15, 25])")
with caught() as c: r = np.interp([0.5, 1.5, 2.5, 3.5], [0, 1, nan, 3], [0, 10, 20, 30])
info(f"interp with NaN in xp [0, 1, nan, 3] at [0.5, 1.5, 2.5, 3.5] -> {r.tolist()} (undocumented; NaN breaks the increasing assumption)")
r = np.interp([1.0], [0, 1, 1, 2], [0, 10, 20, 30]); info(f"interp with a repeated xp value [0, 1, 1, 2] at x=1 -> {r.tolist()}")
r = np.interp(np.float32(0.25), np.array([0, 1], np.float32), np.array([0, 1], np.float32)); report("interp of float32 inputs returns float64", np.asarray(r).dtype == np.float64)

# ================================================================== trapezoid
print("#### trapezoid: x, dx, axis")
tz = getattr(np, "trapezoid", None) or np.trapz
def trap_x(y, x): return sum(((F(x[i + 1]) - F(x[i])) * (F(y[i]) + F(y[i + 1])) / 2 for i in range(len(y) - 1)), F(0))
yv = [Ri.randint(-20, 20) / 4 for _ in range(9)]; xv_ = sorted(Ri.sample(range(-40, 40), 9)); xv_ = [t / 8 for t in xv_]
report("trapezoid(y, x) non-uniform = sum (x_(i+1) - x_i)(y_i + y_(i+1)) / 2, exact", close(tz(yv, xv_), float(trap_x(yv, xv_)), 1e-15))
report("trapezoid(y, dx=0.25) = trapezoid with x = 0.25 i", close(tz(yv, dx=0.25), float(trap_x(yv, [F(i, 4) for i in range(9)])), 1e-15))
report("trapezoid(y) default dx = 1", close(tz(yv), float(trap_x(yv, list(range(9)))), 1e-15))
report("trapezoid with decreasing x gives the negated integral", close(tz(yv[::-1], xv_[::-1]), -float(trap_x(yv, xv_)), 1e-15))
Y2 = np.array([[Ri.randint(-9, 9) for _ in range(5)] for _ in range(4)], float); xa = [0, 0.5, 2, 2.25, 4]; xb = [0, 1, 1.5, 3.5]
r = tz(Y2, xa, axis=1); report("trapezoid(2-D y, 1-D x, axis=1): one integral per row", allclose(r, [float(trap_x(Y2[i], xa)) for i in range(4)], 1e-15))
r = tz(Y2, xb, axis=0); report("trapezoid(2-D y, 1-D x, axis=0): one integral per column", allclose(r, [float(trap_x(Y2[:, j], xb)) for j in range(5)], 1e-15))
X2 = np.array([[k * (i + 1) * 0.5 for k in range(5)] for i in range(4)])
r = tz(Y2, X2, axis=1); report("trapezoid(y, x of the same 2-D shape, axis=1): row-specific sample points", allclose(r, [float(trap_x(Y2[i], X2[i])) for i in range(4)], 1e-15))
r = tz(Y2, dx=0.5, axis=0); report("trapezoid(dx=0.5, axis=0)", allclose(r, [float(trap_x(Y2[:, j], [F(i, 2) for i in range(4)])) for j in range(5)], 1e-15))
report("trapezoid of a single sample = 0.0", tz([3.0]) == 0.0)
report("trapezoid of an empty array = 0.0", tz(np.array([])) == 0.0)
if NP2:
    info(f"np.trapz present in this 2.x build: {hasattr(np, 'trapz')} (deprecated in 2.0 in favour of np.trapezoid)")

# ================================================================== gradient
print("#### gradient: edge_order 1 / 2, non-uniform spacing, several axes, varargs forms")
def lag_deriv(xs, fs, t):
    """Derivative at t of the Lagrange interpolant through (xs, fs) (exact Fractions)."""
    xs = [F(v) for v in xs]; fs = [F(v) for v in fs]; t = F(t); tot = F(0)
    for j in range(len(xs)):
        dj = F(0)
        for m in range(len(xs)):
            if m == j: continue
            term = F(1) / (xs[j] - xs[m])
            for l in range(len(xs)):
                if l != j and l != m: term *= (t - xs[l]) / (xs[j] - xs[l])
            dj += term
        tot += fs[j] * dj
    return tot
def grad_x(f, x, edge_order):
    n = len(f); out = []
    for i in range(n):
        if 0 < i < n - 1: out.append(lag_deriv(x[i - 1:i + 2], f[i - 1:i + 2], x[i]))
        elif edge_order == 1: out.append((F(f[1]) - F(f[0])) / (F(x[1]) - F(x[0])) if i == 0 else (F(f[-1]) - F(f[-2])) / (F(x[-1]) - F(x[-2])))
        else: out.append(lag_deriv(x[:3], f[:3], x[0]) if i == 0 else lag_deriv(x[-3:], f[-3:], x[-1]))
    return out
fg = [Ri.randint(-30, 30) / 4 for _ in range(8)]; xu = [F(i, 2) for i in range(8)]; xn = sorted(set(Ri.randint(0, 60) / 8 for _ in range(20)))[:8]
for eo in (1, 2):
    report(f"gradient(f, 0.5, edge_order={eo}) = derivative of the local Lagrange interpolant (central interior, {'secant' if eo == 1 else '3-point one-sided'} edges)",
           allclose(np.gradient(fg, 0.5, edge_order=eo), [float(v) for v in grad_x(fg, xu, eo)], 1e-14, 1e-13))
    report(f"gradient(f, x non-uniform, edge_order={eo}) = Lagrange-interpolant derivative (Fornberg weights), exact to 1e-13",
           allclose(np.gradient(fg, xn, edge_order=eo), [float(v) for v in grad_x(fg, xn, eo)], 1e-13, 1e-12), f"x = {xn}")
report("gradient(f, x coordinate array that is uniform) == gradient(f, scalar spacing)", allclose(np.gradient(fg, [float(v) for v in xu]), np.gradient(fg, 0.5).tolist(), 1e-15))
fq = [3 * t * t - 2 * t + 1 for t in xn]
report("gradient of a quadratic on non-uniform x with edge_order=2 is exact everywhere (6x - 2)", allclose(np.gradient(fq, xn, edge_order=2), [6 * t - 2 for t in xn], 1e-12, 1e-11))
report("gradient docstring example: f = [1, 2, 4, 7, 11, 16], x = [0, 1, 1.5, 3.5, 4, 6] -> [1, 3, 3.5, 6.7, 6.9, 2.5]",
       allclose(np.gradient([1, 2, 4, 7, 11, 16], [0., 1., 1.5, 3.5, 4., 6.]), [1, 3, 3.5, 6.7, 6.9, 2.5], 1e-14))
G = np.array([[Ri.randint(-9, 9) for _ in range(5)] for _ in range(4)], float)
gy = [0, 1, 1.5, 3.5, 4.0]
g0, g1 = np.gradient(G, 2.0, gy)
ok0 = all(allclose(g0[:, j], [float(v) for v in grad_x(G[:, j].tolist(), [0, 2, 4, 6], 1)], 1e-14, 1e-13) for j in range(5))
ok1 = all(allclose(g1[i], [float(v) for v in grad_x(G[i].tolist(), gy, 1)], 1e-14, 1e-13) for i in range(4))
report("gradient(2-D, dx scalar, y coordinate array): tuple (d/daxis0, d/daxis1), each exact", ok0 and ok1)
r = np.gradient(G, 0.5); report("gradient(2-D, one scalar) applies the spacing to every axis", allclose(r[0], (np.gradient(G, 1.0)[0] * 2).ravel().tolist(), 1e-15) and allclose(r[1], (np.gradient(G, 1.0)[1] * 2).ravel().tolist(), 1e-15))
r = np.gradient(G, gy, axis=1); report("gradient(axis=1, coordinate array) returns a single array", isinstance(r, np.ndarray) and allclose(r, g1.ravel().tolist(), 1e-15))
r = np.gradient(G, axis=-1); report("gradient(axis=-1) counts from the end", allclose(r, np.gradient(G, axis=1).ravel().tolist(), 0, 0))
r = np.gradient(G, 2.0, gy, axis=(0, 1), edge_order=2); report("gradient(axis=(0, 1), two varargs, edge_order=2)", len(r) == 2 and all(allclose(r[1][i], [float(v) for v in grad_x(G[i].tolist(), gy, 2)], 1e-13, 1e-12) for i in range(4)))
e = raises(lambda: np.gradient(G, 1.0, 2.0, 3.0)); report("gradient with 3 varargs for a 2-D array raises TypeError ('invalid number of arguments')", (e or "").startswith("TypeError"), str(e))
e = raises(lambda: np.gradient(G, [0, 1, 2], axis=1)); report("gradient with a coordinate array of the wrong length raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.gradient([1., 2.], edge_order=2)); report("gradient(edge_order=2) with 2 points raises ValueError (needs edge_order + 1)", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.gradient([1., 2., 3.], edge_order=3)); report("gradient(edge_order=3) raises ValueError", (e or "").startswith("ValueError"), str(e))
r = np.gradient(np.array([5, 3, 1, 0], dtype=np.uint8)); report("gradient of uint8 decreasing data is computed in float64 (no wraparound): [-2, -2, -1.5, -1]", r.dtype == np.float64 and r.tolist() == [-2., -2., -1.5, -1.])
r = np.gradient(np.array([0., 1., 4., 9.]), np.array([3, 2, 1, 0], dtype=np.uint8)); report("gradient with uint8 decreasing coordinates: spacing -1 (no wraparound)", r.tolist() == [-1., -2., -4., -5.], f"{r.tolist()}")
r = np.gradient(np.array([1, 2, 4], dtype=np.float32)); report("gradient(float32) keeps float32", r.dtype == np.float32)

# ================================================================== unwrap / angle / clip
print("#### unwrap: discont, period, axis;  angle(deg);  clip bounds")
Ru = random.Random(21); th = [0.3]
for _ in range(60): th.append(th[-1] + Ru.uniform(-3.0, 3.0))
wr = [math.remainder(t, 2 * math.pi) for t in th]
r = np.unwrap(wr); ok = all(abs(a - (t - th[0] + wr[0])) < 1e-12 for a, t in zip(r, th))
report("unwrap(wrapped phase with steps |d| < pi) recovers the phase up to the initial offset (1e-12)", ok, f"max err {max(abs(a - (t - th[0] + wr[0])) for a, t in zip(r, th)):.1e}")
report("unwrap: adjacent differences of the result are all <= pi ('never greater than pi')", bool(np.all(np.abs(np.diff(r)) <= math.pi)))
ph = np.linspace(0, np.pi, num=5); ph[3:] += np.pi
report("unwrap docstring example: [0, pi/4, pi/2, -pi/4, 0]", allclose(np.unwrap(ph), [0, math.pi / 4, math.pi / 2, -math.pi / 4, 0], 1e-15, 1e-15))
r = np.unwrap([1, 2, 3, 4, 5, 6, 1, 2, 3], period=6); report("unwrap(period=6) on ints -> [1..9], integer dtype", r.tolist() == list(range(1, 10)) and r.dtype.kind == "i", f"{r.tolist()} {r.dtype}")
r = np.unwrap([2, 3, 4, 5, 2, 3, 4, 5], period=4); report("unwrap(period=4) docstring example -> [2..9]", r.tolist() == list(range(2, 10)))
r = np.unwrap([0, 1, 2, -1, 0], period=4); report("unwrap([0, 1, 2, -1, 0], period=4) -> [0, 1, 2, 3, 4]", r.tolist() == [0, 1, 2, 3, 4])
pd = [5, 15, 355, 5, 20, 350]; r = np.unwrap(pd, period=360); report("unwrap(degrees, period=360) exact", r.tolist() == [5, 15, -5, 5, 20, -10], f"{r.tolist()}")
def unwrap_doc(p, discont, period):
    """Documented rule on exact values: a step d with |d| > max(discont, period/2) is replaced by its period-complement
    d - k*period in [-period/2, period/2] (ties keep the sign of d); smaller steps are kept."""
    th_ = max(F(discont), F(period) / 2); out = [F(p[0])]
    for i in range(1, len(p)):
        d = F(p[i]) - F(p[i - 1])
        if abs(d) > th_:
            d2 = d - F(period) * round(d / F(period))
            if abs(d2) == F(period) / 2 and (d2 > 0) != (d > 0): d2 = -d2
            d = d2
        out.append(out[-1] + d)
    return out
pp = [0, 3.5, 7.0, 5.0, 9.0, 1.0, 0.0]
for disc in (None, 1.0, 4.0, 5.0):
    r = np.unwrap(pp, period=8) if disc is None else np.unwrap(pp, discont=disc, period=8)
    t = unwrap_doc(pp, 4 if disc is None else disc, 8)
    report(f"unwrap(period=8, discont={disc}): steps with |d| > max(discont, period/2) replaced by their period complement (exact)", [F(float(v)) for v in r] == t, f"{r.tolist()} vs {[float(v) for v in t]}")
r = np.unwrap([0, 5, 10], discont=5, period=8)
report("unwrap(period=8, discont=5): a step of exactly 5 = discont is not 'more than max(discont, period/2)' -> kept", r.tolist() == [0, 5, 10], f"{r.tolist()}")
r = np.unwrap([0., 3.5], discont=4.0); report("unwrap(discont=4 > pi): a step of 3.5 is left alone", r.tolist() == [0.0, 3.5])
r = np.unwrap([0., 3.5]); report("unwrap(default discont = pi): a step of 3.5 becomes 3.5 - 2 pi", close(r[1], 3.5 - 2 * math.pi, 1e-15))
r = np.unwrap([0., 2.0], discont=1.0); report("unwrap(discont=1 < pi): acts as discont = pi (step 2 kept)", r.tolist() == [0.0, 2.0])
W2 = np.array([wr[:20], wr[20:40]]).T
r = np.unwrap(W2, axis=0); report("unwrap(2-D, axis=0) == column-wise 1-D unwrap", np.array_equal(r[:, 0], np.unwrap(W2[:, 0])) and np.array_equal(r[:, 1], np.unwrap(W2[:, 1])))
r = np.unwrap(W2.T); report("unwrap default axis=-1 on the transpose", np.array_equal(r, np.unwrap(W2, axis=0).T))
zs = [1 + 1j, -1 + 0j, complex(-1, -0.0), 1j, -1j, complex(-3, 4), complex(0.0, -0.0), complex(-0.0, 0.0), 2.5, -2.5]
ok = True; det = []
for z in zs:
    im = z.imag if isinstance(z, complex) else 0.0; re = z.real
    if im == 0:   # atan2 on the axis: +-0 or +-pi with the sign of the (signed) zero imaginary part
        base = mp.pi if (re < 0 or (re == 0 and math.copysign(1, re) < 0)) else mp.mpf(0)
        tr = float(mp.degrees(base)) * math.copysign(1, im)
    else:
        tr = float(mp.degrees(mp.atan2(im, re)))
    a_ = np.angle(z, deg=True)
    if not close(a_, tr, 2.3e-16) and not (a_ == tr): ok = False; det.append(f"{z}: {a_} vs {tr}")
report("angle(z, deg=True) = degrees(atan2(imag, real)) to 1 ulp, signed zeros follow atan2 (-1-0j -> -180, -0.0 -> 180)", ok, "; ".join(det))
report("angle(1j, deg=True) == 90.0 and angle(-1, deg=True) == 180.0 exactly", np.angle(1j, deg=True) == 90.0 and np.angle(-1, deg=True) == 180.0)
report("angle of a real array: 0 for positive, pi for negative", np.angle(np.array([2., -3.])).tolist() == [0.0, math.pi])
report("clip(a, 5, 2) with a_min > a_max: every value equals a_max (documented)", np.clip(np.arange(8), 5, 2).tolist() == [2] * 8)
report("clip with array bounds broadcasts", np.clip(np.arange(6).reshape(2, 3), [1, 2, 3], [[2], [4]]).tolist() == [[1, 2, 2], [3, 4, 4]])
report("clip keeps NaN elements", bool(np.isnan(np.clip(np.array([nan, 5.]), 0, 1)[0])))
if NPV >= (2, 1):
    r = np.clip(np.arange(4)); report("clip(a) with both bounds None returns the values unchanged (2.1+)", r.tolist() == [0, 1, 2, 3])
    report("clip(a, min=1, max=2) keyword aliases (2.1+)", np.clip(np.arange(4), min=1, max=2).tolist() == [1, 1, 2, 2])
else:
    e = raises(lambda: np.clip(np.arange(4), None, None)); report("clip(a, None, None) raises ValueError before 2.1 ('One of max or min must be given')", (e or "").startswith("ValueError"), str(e))

# ================================================================== cov / corrcoef
print("#### cov / corrcoef: rowvar, bias, ddof, y, complex conjugation, clipping, constant / NaN rows")
def cov_x(rows, ddof=1):
    n = len(rows[0]); ms = [sum((F(v) if not isinstance(v, complex) else v for v in r), F(0)) / n for r in rows]
    out = []
    for i, ri in enumerate(rows):
        row = []
        for j, rj in enumerate(rows):
            s = sum(((F(a) - ms[i]) * (F(b) - ms[j]) for a, b in zip(ri, rj)), F(0)); row.append(s / (n - ddof))
        out.append(row)
    return out
def ccov_x(rows, ddof=1):
    """complex covariance sum (x_i - m_i) conj(x_j - m_j) / (N - ddof) on Gaussian-integer data (exact via Fraction pairs)."""
    n = len(rows[0]); ms = [(sum(F(int(z.real)) for z in r) / n, sum(F(int(z.imag)) for z in r) / n) for r in rows]
    out = []
    for i, ri in enumerate(rows):
        row = []
        for j, rj in enumerate(rows):
            re_ = F(0); im_ = F(0)
            for a, b in zip(ri, rj):
                ar, ai = F(int(a.real)) - ms[i][0], F(int(a.imag)) - ms[i][1]; br, bi = F(int(b.real)) - ms[j][0], F(int(b.imag)) - ms[j][1]
                re_ += ar * br + ai * bi; im_ += ai * br - ar * bi
            row.append(complex(float(re_ / (n - ddof)), float(im_ / (n - ddof))))
        out.append(row)
    return out
Rv = random.Random(4)
X = [[Rv.randint(-9, 9) for _ in range(6)] for _ in range(3)]; Yy = [[Rv.randint(-9, 9) for _ in range(6)] for _ in range(2)]
flat = lambda M_: [complex(v) for row in M_ for v in row]
report("cov(X.T, rowvar=False) == exact covariance of the columns (ddof=1)", allclose(np.cov(np.array(X).T, rowvar=False), flat([[float(v) for v in r] for r in cov_x(X, 1)]), 1e-14))
report("cov(bias=True) normalises by N", allclose(np.cov(X, bias=True), flat([[float(v) for v in r] for r in cov_x(X, 0)]), 1e-14))
report("cov(ddof=2) normalises by N - 2", allclose(np.cov(X, ddof=2), flat([[float(v) for v in r] for r in cov_x(X, 2)]), 1e-14))
report("cov(bias=True, ddof=1): 'ddof ... overrides the value implied by bias' -> N - 1", allclose(np.cov(X, bias=True, ddof=1), flat([[float(v) for v in r] for r in cov_x(X, 1)]), 1e-14))
report("cov(x, y) = cov of the stacked variables (5 x 5)", allclose(np.cov(X, Yy), flat([[float(v) for v in r] for r in cov_x(X + Yy, 1)]), 1e-14) and np.cov(X, Yy).shape == (5, 5))
report("cov(x.T, y.T, rowvar=False): y's columns appended as variables", allclose(np.cov(np.array(X).T, np.array(Yy).T, rowvar=False), flat([[float(v) for v in r] for r in cov_x(X + Yy, 1)]), 1e-14))
report("cov(1-D x, 1-D y) -> 2 x 2", allclose(np.cov(X[0], X[1]), flat([[float(v) for v in r] for r in cov_x([X[0], X[1]], 1)]), 1e-14))
r = np.cov(X[0]); report("cov(1-D x) -> 0-d variance with ddof 1", np.ndim(r) == 0 and close(r, float(var_x(X[0], 1)), 1e-14))
Zc = [[complex(Rv.randint(-9, 9), Rv.randint(-9, 9)) for _ in range(7)] for _ in range(3)]
C = np.cov(Zc); T = ccov_x(Zc, 1)
report("cov(complex) = sum (x_i - m_i) conj(x_j - m_j) / (N - 1), exact", allclose(C, flat(T), 1e-14))
hd = float(np.max(np.abs(C - C.conj().T))); di = max(abs(C[i, i].imag) for i in range(3)); sc_ = float(np.max(np.abs(C)))
report("cov(complex) is Hermitian with a real positive diagonal up to rounding (1e-14 x max|C|)", hd <= 1e-14 * sc_ and di <= 1e-14 * sc_ and all(C[i, i].real > 0 for i in range(3)))
info(f"cov(complex) measured: max |C - C^H| = {hd:.1e}, max |Im C_ii| = {di:.1e} (max |C| = {sc_:.1f}); not exactly Hermitian (matrix product rounding)")
R_ = np.corrcoef(Zc); tr = [[T[i][j] / math.sqrt(T[i][i].real * T[j][j].real) for j in range(3)] for i in range(3)]
report("corrcoef(complex) = C_ij / sqrt(C_ii C_jj)", allclose(R_, flat(tr), 1e-14))
report("corrcoef(complex): real and imaginary parts within [-1, 1] (clipped)", bool(np.all(np.abs(R_.real) <= 1) and np.all(np.abs(R_.imag) <= 1)))
worst = 0.0
for trial in range(300):
    base = [Rv.uniform(-1, 1) * 10 ** Rv.randint(-3, 5) for _ in range(Rv.randint(2, 12))]
    sc = Rv.choice([1, -1]) * Rv.uniform(0.1, 1e4); off = Rv.uniform(-1e6, 1e6)
    rr = np.corrcoef(base, [sc * t + off for t in base]); worst = max(worst, float(np.max(np.abs(rr))))
report("corrcoef of 300 exactly (anti-)correlated pairs with large offsets: every |r| <= 1 (clipped)", worst <= 1.0, f"max |r| {worst!r}")
with caught() as c: r = np.corrcoef([[1., 2., 3.], [5., 5., 5.], [3., 1., 2.]])
report("corrcoef with a constant row: that row and column NaN, RuntimeWarning, the rest finite",
       bool(np.all(np.isnan(r[1]))) and bool(np.all(np.isnan(r[:, 1]))) and np.isfinite(r[0, 2]) and "RuntimeWarning" in c.cats, f"{c.cats}")
with caught() as c: r = np.corrcoef([[1., 2., 3., 4.], [2., nan, 1., 0.], [4., 3., 1., 2.]])
report("corrcoef with a NaN in row 1: row / column 1 NaN, the others exact", bool(np.all(np.isnan(r[1]))) and bool(np.all(np.isnan(r[:, 1]))) and close(r[0, 2], float(cov_x([[1, 2, 3, 4], [4, 3, 1, 2]])[0][1] / F(5, 3)), 1e-14))
if NPV >= (2, 4):
    e = raises(lambda: np.corrcoef(X, bias=True)); report("corrcoef(bias=...) removed in 2.4 (release note: 'had no effect') -> TypeError", (e or "").startswith("TypeError"), str(e))
else:
    with caught() as c: r1 = np.corrcoef(X, bias=True)
    report("corrcoef(bias=...) is accepted but deprecated (DeprecationWarning) and has no effect", "DeprecationWarning" in c.cats and np.array_equal(r1, np.corrcoef(X)), f"{c.cats}")
r = np.cov(X, dtype=np.float32); report("cov(dtype=float32) returns float32", r.dtype == np.float32)
r = np.corrcoef(X, dtype=np.float32); report("corrcoef(dtype=float32) returns float32", r.dtype == np.float32)
e = raises(lambda: np.cov(X, fweights=[1, 2, 1.5, 1, 1, 1])); report("cov(fweights non-integer) raises TypeError", (e or "").startswith("TypeError"), str(e))
e = raises(lambda: np.cov(X, fweights=[1, 2, -1, 1, 1, 1])); report("cov(fweights negative) raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.cov(X, aweights=[1, 2, -1, 1, 1, 1])); report("cov(aweights negative) raises ValueError", (e or "").startswith("ValueError"), str(e))
with caught() as c: r = np.cov([[1.], [2.]])
report("cov with a single observation (N - ddof = 0): RuntimeWarning 'Degrees of freedom <= 0' and non-finite result", "RuntimeWarning" in c.cats and not np.all(np.isfinite(r)), f"{r.tolist()} {c.msgs[:1]}")

# ================================================================== misc documented behaviours
print("#### float16 mean, complex var / std, median of ints, percentile q array + out, quantile q range, count_nonzero, apply_over_axes")
h = np.full(10000, 0.1, dtype=np.float16); r = np.mean(h)
report("mean(float16): 'float16 results are computed using float32 intermediates' -> exact float16(0.1) for 10000 copies", r.dtype == np.float16 and r == np.float16(0.1), f"{r!r}")
Rh2 = random.Random(6); hv = np.array([Rh2.uniform(0, 100) for _ in range(20000)], dtype=np.float16)
ex_ = mean_x([float(t) for t in hv.tolist()]); r = np.mean(hv)
report("mean(float16) of 20000 values in [0, 100) equals float16(exact mean) (within 1 float16 ulp)", abs(float(r) - float(ex_)) <= float(np.spacing(np.float16(float(ex_)))), f"{float(r)} vs {float(ex_)}")
with caught() as c: s16 = np.sum(hv); m16 = np.mean(hv, dtype=np.float16)
info(f"sum(float16, 20000 values) = {float(s16)} (exact {float(fsum(hv.tolist()))} exceeds float16 max 65504); mean(dtype=float16) = {float(m16)} (explicit float16 accumulation overflows; no float32 promise when dtype is given)")
zc = [complex(Rv.randint(-9, 9), Rv.randint(-9, 9)) for _ in range(9)]
mz = (fsum([z.real for z in zc]) / 9, fsum([z.imag for z in zc]) / 9)
vz = sum(((F(z.real) - mz[0]) ** 2 + (F(z.imag) - mz[1]) ** 2 for z in zc), F(0)) / 9
r = np.var(zc); report("var(complex) = mean(|z - mean|^2), a real float64 (documented 'absolute value is taken before squaring')", r.dtype == np.float64 and close(r, float(vz), 1e-14), f"{r!r}")
report("std(complex, ddof=1) = sqrt(sum |z - mean|^2 / (n - 1))", close(np.std(zc, ddof=1), sqrt_m(vz * 9 / 8), 1e-14))
report("var(complex64) returns float32", np.var(np.array(zc, dtype=np.complex64)).dtype == np.float32)
report("median of an even-length int array is the float mean of the middle two: [1, 2, 3, 4] -> 2.5 float64", np.median([1, 2, 3, 4]) == 2.5 and np.median([1, 2, 3, 4]).dtype == np.float64)
report("median(int8 [100, 120]) = 110.0 (no int8 overflow in the averaging)", np.median(np.array([100, 120], dtype=np.int8)) == 110.0)
report("median(uint8 [250, 254, 1, 3]) = (3 + 250) / 2 = 126.5", np.median(np.array([250, 254, 1, 3], dtype=np.uint8)) == 126.5)
P = np.array([[4., 1., 9., 3.], [2., 8., 5., 7.], [6., 0., 3., 1.]]); qa = np.array([[10, 50], [75, 90]])
r = np.percentile(P, qa, axis=1); ok = r.shape == (2, 2, 3) and all(close(r[i, j, k], float(q7(P[k], F(int(qa[i, j]), 100))), 1e-15) for i in range(2) for j in range(2) for k in range(3))
report("percentile(q 2-D (2, 2), axis=1): shape q.shape + reduced shape = (2, 2, 3), exact", ok, f"{r.shape}")
o = np.empty((2, 2, 3)); r = np.percentile(P, qa, axis=1, out=o); report("percentile(out=o) returns o, filled with the same values", r is o and np.array_equal(o, np.percentile(P, qa, axis=1)))
e = raises(lambda: np.percentile(P, qa, axis=1, out=np.empty((3, 2)))); report("percentile with an out of the wrong shape raises", e is not None, str(e))
for q in (-0.01, 1.01, nan):
    e = raises(lambda: np.quantile(P, q)); report(f"quantile(q={q}) outside [0, 1] raises ValueError ('Quantiles must be in the range [0, 1]')", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.percentile(P, 100.5)); report("percentile(q=100.5) raises ValueError", (e or "").startswith("ValueError"), str(e))
e = raises(lambda: np.quantile(P, [0.5, 2.0])); report("quantile(q=[0.5, 2.0]) raises ValueError (one entry out of range)", (e or "").startswith("ValueError"), str(e))
K = np.array([[[0, 1.], [nan, 0]], [[-0.0, 2], [3, 0]], [[0, 0], [0, 5]]])
r = np.count_nonzero(K, axis=(0, 2), keepdims=True); report("count_nonzero(axis=(0, 2), keepdims=True): shape (1, 2, 1); NaN counts as nonzero, -0.0 as zero", r.shape == (1, 2, 1) and r.ravel().tolist() == [2, 3], f"{r.ravel().tolist()}")
r = np.count_nonzero(K, axis=1, keepdims=True); report("count_nonzero(axis=1, keepdims=True): shape (3, 1, 2)", r.shape == (3, 1, 2) and r.ravel().tolist() == [1, 1, 1, 1, 0, 1])
report("count_nonzero(axis=None) -> int total", np.count_nonzero(K) == 5)
A3 = np.arange(24).reshape(2, 3, 4)
r = np.apply_over_axes(np.sum, A3, [0, 2]); report("apply_over_axes(np.sum, a, [0, 2]) == a.sum(axis=(0, 2), keepdims=True) (dims re-inserted, ndim kept)", r.shape == (1, 3, 1) and np.array_equal(r, A3.sum(axis=(0, 2), keepdims=True)))
r = np.apply_over_axes(lambda t, ax: np.cumsum(t, axis=ax), A3, [1, 2]); report("apply_over_axes with a shape-preserving func (cumsum): repeated application", np.array_equal(r, np.cumsum(np.cumsum(A3, axis=1), axis=2)))
r = np.apply_over_axes(np.mean, A3, 1); report("apply_over_axes(np.mean, a, 1) with a scalar axis", r.shape == (2, 1, 4) and np.array_equal(r, A3.mean(axis=1, keepdims=True)))
e = raises(lambda: np.apply_over_axes(lambda t, ax: np.sum(t), A3, [0])); report("apply_over_axes with a func dropping all dims raises ValueError", (e or "").startswith("ValueError"), str(e))
print("---- done")
