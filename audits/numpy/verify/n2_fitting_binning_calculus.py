#!/usr/bin/env python
"""NumPy fitting, binning and calculus routines against exact recomputations:
histogram (edges, closed last bin, density, 'auto'), digitize / searchsorted,
polyfit (coefficients, residuals, weights, cov scaling, conditioning with an
offset abscissa), interp (clamping, period), trapezoid, gradient (edge order,
uneven spacing), lstsq (rcond), unique with NaN, round half to even."""
import sys, math, random, warnings
from fractions import Fraction as F
import numpy as np
print(f"numpy {np.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-10, abs_=1e-300):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
rng = random.Random(3); warnings.filterwarnings("ignore")
trapezoid = getattr(np, "trapezoid", None) or np.trapz

# ---- histogram
x = np.array([rng.uniform(0, 10) for _ in range(1000)] + [0.0, 10.0, 2.5, 5.0, 7.5])   # values exactly on edges
h, e = np.histogram(x, bins=4, range=(0, 10))
def hist_exact(vals, edges):
    counts = [0] * (len(edges) - 1)
    for v in vals:
        if v < edges[0] or v > edges[-1]: continue
        for i in range(len(edges) - 1):
            if edges[i] <= v < edges[i + 1] or (i == len(edges) - 2 and v == edges[-1]): counts[i] += 1; break
    return counts
report("histogram(bins=4, range=(0,10)): bins [a,b) except the last [a,b]; edges exact", h.tolist() == hist_exact(x.tolist(), e.tolist()) and e.tolist() == [0, 2.5, 5, 7.5, 10])
h2, e2 = np.histogram(x, bins=[0, 1, 2.5, 5, 10])
report("histogram with unequal explicit edges: same rule", h2.tolist() == hist_exact(x.tolist(), e2.tolist()))
hd, ed = np.histogram(x, bins=[0, 1, 2.5, 5, 10], density=True)
report("histogram(density=True): sum(density * width) = 1", close(float((hd * np.diff(ed)).sum()), 1.0))
report("histogram(density=True) = count / (n_in_range * width)", all(close(hd[i], h2[i] / (h2.sum() * (e2[i + 1] - e2[i]))) for i in range(len(h2))))
xo = np.concatenate([x, [-1, 11]]); ho, eo = np.histogram(xo, bins=4, range=(0, 10))
report("histogram(range=): values outside the range are dropped, not clipped", ho.tolist() == h.tolist())
ha, ea = np.histogram(x, bins="auto")
fd = 2 * (np.percentile(x, 75) - np.percentile(x, 25)) / len(x) ** (1 / 3); sturges = (x.max() - x.min()) / (math.log2(len(x)) + 1)
width = min(fd, sturges); nb = math.ceil((x.max() - x.min()) / width)
report(f"histogram(bins='auto') = min(Freedman-Diaconis, Sturges) width -> {nb} bins", len(ha) == nb, f"({len(ha)})")
# float32 data on edges
x32 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], dtype=np.float32); e32 = [0.1, 0.3, 0.5, 0.7]
h32, _ = np.histogram(x32, bins=e32)
print(f"   float32 values on float64 edges {e32}: counts {h32.tolist()} (values as float64: {[float(v) for v in x32]})")
report("float32 values on the edges: counted by their exact (float64-widened) value against the edges", h32.tolist() == hist_exact([float(v) for v in x32], e32))
# digitize / searchsorted
bins = [1.0, 2.0, 3.0]; vals = [0.5, 1.0, 1.5, 2.0, 3.0, 3.5]
report("digitize(right=False): index i with bins[i-1] <= x < bins[i]", np.digitize(vals, bins).tolist() == [0, 1, 1, 2, 3, 3])
report("digitize(right=True): bins[i-1] < x <= bins[i]", np.digitize(vals, bins, right=True).tolist() == [0, 0, 1, 1, 2, 3])
report("searchsorted side='left'/'right'", np.searchsorted(bins, 2.0).tolist() == 1 and np.searchsorted(bins, 2.0, side="right").tolist() == 2)

# ---- polyfit against exact least squares
def lstsq_exact(rows, y):
    """Solve the normal equations exactly with Fractions."""
    m = len(rows[0]); A = [[sum(F(r[i]) * F(r[j]) for r in rows) for j in range(m)] for i in range(m)]
    b = [sum(F(r[i]) * F(v) for r, v in zip(rows, y)) for i in range(m)]
    M = [A[i] + [b[i]] for i in range(m)]
    for c in range(m):
        piv = next(r for r in range(c, m) if M[r][c] != 0); M[c], M[piv] = M[piv], M[c]
        M[c] = [v / M[c][c] for v in M[c]]
        for r in range(m):
            if r != c and M[r][c] != 0: M[r] = [a - M[r][c] * b_ for a, b_ in zip(M[r], M[c])]
    return [M[i][m] for i in range(m)], A
xs = [F(i, 2) for i in range(-10, 11)]; ys = [F(3) * v ** 2 - F(2) * v + F(1, 3) + F(rng.randint(-20, 20), 10) for v in xs]
xf = np.array([float(v) for v in xs]); yf = np.array([float(v) for v in ys]); ysE = [F(v) for v in yf.tolist()]
deg = 2; rows = [[v ** (deg - k) for k in range(deg + 1)] for v in xs]
coef_e, ATA = lstsq_exact(rows, ysE)
c, res, rank, sv, rc = np.polyfit(xf, yf, deg, full=True)
report("polyfit(deg=2) coefficients exact (highest power first)", all(close(a, b, 1e-9) for a, b in zip(c, coef_e)))
rss = sum((sum(F(r[k]) * coef_e[k] for k in range(deg + 1)) - v) ** 2 for r, v in zip(rows, ysE))
report("polyfit(full=True) residual = sum of squared residuals", close(res[0], rss, 1e-8))
c2, cov = np.polyfit(xf, yf, deg, cov=True)
# exact covariance: sigma^2 (A^T A)^-1 with sigma^2 = RSS / (n - deg - 1)
def inv_exact(A):
    m = len(A); M = [A[i] + [F(1) if i == j else F(0) for j in range(m)] for i in range(m)]
    for c_ in range(m):
        piv = next(r for r in range(c_, m) if M[r][c_] != 0); M[c_], M[piv] = M[piv], M[c_]
        M[c_] = [v / M[c_][c_] for v in M[c_]]
        for r in range(m):
            if r != c_ and M[r][c_] != 0: M[r] = [a - M[r][c_] * b_ for a, b_ in zip(M[r], M[c_])]
    return [row[m:] for row in M]
n = len(xs); Ainv = inv_exact(ATA); s2 = rss / (n - deg - 1)
cov_e = [[s2 * Ainv[i][j] for j in range(deg + 1)] for i in range(deg + 1)]
ratio = float(cov[0, 0]) / float(cov_e[0][0])
scale_ = max(abs(float(v)) for row in cov_e for v in row)
report("polyfit(cov=True) = RSS/(n - deg - 1) (A^T A)^-1", all(close(cov[i, j], cov_e[i][j], 1e-8, 1e-9 * scale_) for i in range(deg + 1) for j in range(deg + 1)), f"(ratio to the exact scaling {ratio:.6f}; RSS/(n-deg-3) would give {(n - deg - 1) / (n - deg - 3):.6f})")
c3, cov3 = np.polyfit(xf, yf, deg, cov="unscaled")
scale_u = max(abs(float(v)) for row in Ainv for v in row)
report("polyfit(cov='unscaled') = (A^T A)^-1", all(close(cov3[i, j], Ainv[i][j], 1e-8, 1e-9 * scale_u) for i in range(deg + 1) for j in range(deg + 1)))
# weights: w multiplies the residual (so w = 1/sigma)
wts = [F(rng.randint(1, 5)) for _ in xs]
rows_w = [[wv * v for v in r] for wv, r in zip(wts, rows)]; ys_w = [wv * v for wv, v in zip(wts, ysE)]
coef_w, _ = lstsq_exact(rows_w, ys_w)
cw = np.polyfit(xf, yf, deg, w=[float(v) for v in wts])
report("polyfit(w=): minimises sum (w_i (y_i - p(x_i)))^2, i.e. w = 1/sigma_i, not 1/sigma_i^2", all(close(a, b, 1e-9) for a, b in zip(cw, coef_w)))
# conditioning: years as abscissa
yrs = np.arange(2000, 2021, dtype=float); yv = 0.5 * (yrs - 2010) ** 3 - 2 * (yrs - 2010) + 5
with warnings.catch_warnings(record=True) as wlist:
    warnings.simplefilter("always"); cy = np.polyfit(yrs, yv, 3)
fitted = np.polyval(cy, yrs); cc = np.polyfit(yrs - 2010, yv, 3); fitted_c = np.polyval(cc, yrs - 2010)
print(f"   polyfit degree 3 on x = 2000..2020: max |fit - data| {np.abs(fitted - yv).max():.3e} (centred abscissa: {np.abs(fitted_c - yv).max():.3e}); RankWarning raised: {any(issubclass(w_.category, np.exceptions.RankWarning if hasattr(np, 'exceptions') else np.RankWarning) for w_ in wlist)}")
report("polyfit degree 3 on years 2000-2020 reproduces an exact cubic to 1e-6 relative", np.abs(fitted - yv).max() <= 1e-6 * np.abs(yv).max())

# ---- interp
xp = [0.0, 1.0, 2.0, 4.0]; fp = [0.0, 10.0, 0.0, 8.0]
report("interp linear between points", close(np.interp(3.0, xp, fp), 4.0) and close(np.interp(0.5, xp, fp), 5.0))
report("interp outside xp is clamped to fp[0] / fp[-1] (no extrapolation)", np.interp(-1, xp, fp) == 0.0 and np.interp(9, xp, fp) == 8.0)
report("interp(left=, right=) override the clamping", math.isnan(np.interp(-1, xp, fp, left=np.nan)) and np.interp(9, xp, fp, right=-1) == -1)
report("interp(period=) wraps the abscissa", close(np.interp(4.5, xp, fp, period=4), np.interp(0.5, xp, fp, period=4)))
xd = [0.0, 2.0, 1.0, 4.0]
print(f"   interp with non-increasing xp {xd}: {np.interp([0.5, 1.5, 3.0], xd, fp).tolist()} (documented as unchecked; results are meaningless)")

# ---- trapezoid, gradient
ys2 = [F(v) for v in yf.tolist()]; xs2 = [F(v) for v in xf.tolist()]
tz = sum((xs2[i + 1] - xs2[i]) * (ys2[i] + ys2[i + 1]) / 2 for i in range(len(xs2) - 1))
report("trapezoid(y, x) exact", close(trapezoid(yf, xf), tz))
report("trapezoid(y, dx=0.5) exact", close(trapezoid(yf, dx=0.5), tz))
g1 = np.gradient(yf, xf); g2 = np.gradient(yf, xf, edge_order=2)
interior = [(ys2[i + 1] - ys2[i - 1]) / (xs2[i + 1] - xs2[i - 1]) for i in range(1, len(xs2) - 1)]
report("gradient interior (uniform spacing) = central difference", all(close(g1[i], interior[i - 1]) for i in range(1, len(xs2) - 1)))
report("gradient edges default edge_order=1 = one-sided difference", close(g1[0], (ys2[1] - ys2[0]) / (xs2[1] - xs2[0])) and close(g1[-1], (ys2[-1] - ys2[-2]) / (xs2[-1] - xs2[-2])))
h_ = xs2[1] - xs2[0]
report("gradient edge_order=2 edges = second-order one-sided stencil", close(g2[0], (-3 * ys2[0] + 4 * ys2[1] - ys2[2]) / (2 * h_)) and close(g2[-1], (3 * ys2[-1] - 4 * ys2[-2] + ys2[-3]) / (2 * h_)))
xu = np.array([0.0, 0.5, 1.5, 3.0, 3.2]); yu = xu ** 2; gu = np.gradient(yu, xu)
def grad_uneven(i):
    hs = F(xu[i] - xu[i - 1]); hd = F(xu[i + 1] - xu[i]); f0, f1, f2 = (F(v) for v in (yu[i - 1], yu[i], yu[i + 1]))
    return (hs ** 2 * f2 + (hd ** 2 - hs ** 2) * f1 - hd ** 2 * f0) / (hs * hd * (hd + hs))
report("gradient with uneven spacing: second-order interior formula", all(close(gu[i], grad_uneven(i)) for i in range(1, 4)))
report("gradient of x^2 on uneven spacing is exact in the interior (2x)", all(close(gu[i], 2 * xu[i]) for i in range(1, 4)))

# ---- lstsq
A = np.array([[1.0, 1.0], [1.0, 2.0], [1.0, 3.0], [1.0, 4.0]]); b = np.array([6.0, 5.0, 7.0, 10.0])
sol, resid, rk, svs = np.linalg.lstsq(A, b, rcond=None)
sol_e, _ = lstsq_exact([[F(1), F(1)], [F(1), F(2)], [F(1), F(3)], [F(1), F(4)]], [F(6), F(5), F(7), F(10)])
report("lstsq solution exact; residuals = sum of squared residuals", all(close(a, b_) for a, b_ in zip(sol, sol_e)) and close(resid[0], sum((F(1) * sol_e[0] + F(i + 1) * sol_e[1] - v) ** 2 for i, v in enumerate([6, 5, 7, 10]))))

# ---- unique with NaN, round half to even
u = np.unique(np.array([1.0, np.nan, 2.0, np.nan, 1.0]))
print(f"   unique([1, nan, 2, nan, 1]) = {u.tolist()} ({'NaNs collapsed to one' if len(u) == 3 else 'each NaN kept'})")
report("round half to even: round(0.5)=0, round(1.5)=2, round(2.5)=2", np.round([0.5, 1.5, 2.5]).tolist() == [0, 2, 2])
print(f"   np.round(2.675, 2) = {np.round(2.675, 2)} (Python round: {round(2.675, 2)}; 2.675 is stored below the half, but 2.675 * 100 rounds up to exactly 267.5 in binary, then half-to-even gives 268 -- the documented multiply-rint-divide algorithm)")
report("round(x, 2) for x = 1.005 (stored below 1.005) gives 1.0", np.round(1.005, 2) == 1.0, f"({np.round(1.005, 2)})")
