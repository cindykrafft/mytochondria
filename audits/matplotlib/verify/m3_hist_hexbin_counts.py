#!/usr/bin/env python
"""m3_hist_hexbin_counts: the counts and derived numbers that Axes methods compute
(lib/matplotlib/axes/_axes.py, lib/matplotlib/stackplot.py).

Truths: fractions.Fraction (bin edges, exact bin membership by the documented half-open
rule with the last bin closed, densities, cumulative sums, percentages, correlation
sums, least-squares detrending); plain-Python ports written from the docstrings (the
hist bins rule; hist2d bins on both axes; the hexagonal grid of two interleaved
lattices with nearest-centre assignment, and point-in-drawn-hexagon membership with
exact rational arithmetic; the xcorr sum  sum_n x[n+k] * conj(y[n]); the stackplot
baselines from the docstring / Byron & Wattenberg 2008, including the minimiser of the
weighted squared midline slopes); closed forms (Sturges / sqrt / Rice bin counts,
log10). No scipy is needed.

Covered: Axes.hist (int / sequence / string bins, range, density per dataset, weights,
density+weights, cumulative True / -1, density+cumulative, stacked (cumulative across
datasets) with and without density, unequal bins, multiple datasets of different
lengths, 2-D array columns, empty datasets, NaN / inf, integer data on bin edges,
float32, large offsets, constant data, step / stepfilled / bar / barstacked geometry,
log=True, bottom); Axes.stairs path; Axes.hist2d (counts, density, weights, range,
[int, int] bins, cmin / cmax boundaries, cmin with density); Axes.hexbin (grid shape,
counts vs the drawn hexagons, conservation, extent, NaN/inf, C with mean / sum / max,
mincnt with and without C (version-aware: 3.8.0 / 3.8.1 API notes), bins='log'
(docstring-aware: log10(i+1) up to the doc fix, log10(i) / LogNorm later), integer and
sequence bins, xscale / yscale='log', get_offsets in data coordinates, marginals);
Axes.acorr / xcorr (normed, detrend mean / linear, maxlags, lag vector, maxlags=None,
complex, integer input); Axes.stackplot baselines zero / sym / wiggle / weighted_wiggle;
Axes.pie (wedge angles, autopct strings and callable, normalize True / False, sums < 1,
zeros, counterclock, startangle); Axes.errorbar (symmetric, asymmetric, scalar,
lolims / uplims / xlolims / xuplims, NaN errors, errorevery)."""
import sys, math, warnings, random, inspect
from fractions import Fraction as F
from _synth import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
warnings.filterwarnings("ignore")

V = mpl_version()
def info(s): print("   " + s)
def fr(v): return F(float(v))
def raises(fn):
    try: fn()
    except Exception as e: return type(e).__name__ + ": " + str(e)[:100]
    return None
def new_ax():
    plt.close("all"); fig, ax = plt.subplots(); return ax
rng = random.Random(20261001)

banner()

# ------------------------------------------------------------------ hist port
def port_hist(data, edges, weights=None):
    """Documented rule: bins [e_i, e_{i+1}) except the last, which is [e_{n-1}, e_n].
    NaN fails every comparison and so belongs to no bin. Exact (Fraction) sums."""
    e = [fr(t) for t in edges]; nb = len(e) - 1
    out = [F(0)] * nb
    for k, v in enumerate(data):
        v = float(v)
        if math.isnan(v) or math.isinf(v):  # NaN is in no bin; +-inf is outside any finite edges
            continue
        fv = fr(v)
        w = F(1) if weights is None else fr(weights[k])
        for i in range(nb):
            if e[i] <= fv < e[i + 1] or (i == nb - 1 and fv == e[-1]):
                out[i] += w; break
    return out
def lin_edges(lo, hi, n):
    lo = fr(lo); hi = fr(hi); return [lo + (hi - lo) * i / n for i in range(n + 1)]
def edges_ok(got, truth, ulps=4):
    """Each returned edge within a few ulps of the exact lo + i (hi - lo)/n, the ulp taken at
    the scale max(|lo|, |hi|) (linspace rounding of interior edges near zero)."""
    if len(got) != len(truth): return False
    scale = max(abs(truth[0]), abs(truth[-1]))
    tol = scale * ulps / F(2 ** 52)
    return all(abs(fr(g) - t) <= tol for g, t in zip(got, truth))
def ex(xs): return [float(t) for t in xs]

print("#### Axes.hist: counts against the documented half-open bins (last bin closed)")
data = [rng.gauss(0, 1) for _ in range(997)]
for nb in (1, 7, 10, 64):
    n, b, _ = new_ax().hist(data, bins=nb)
    te = lin_edges(min(data), max(data), nb)
    report(f"hist(bins={nb}): edges = linspace(min, max, {nb}+1) ('the number of equal-width bins in the range'; range defaults to (x.min(), x.max()))",
           edges_ok(b, te), f"maxdiff {maxdiff(b, ex(te)):.3g}")
    tc = port_hist(data, b)
    report(f"hist(bins={nb}): n equals the plain-Python count with [e_i, e_i+1) and the last bin closed", allclose(n, ex(tc), 0, 0),
           f"{list(n)[:6]} vs {ex(tc)[:6]}")
    report(f"hist(bins={nb}): sum(n) == len(x) (min and max both counted)", float(sum(n)) == len(data))
    report(f"hist(bins={nb}): n dtype is float ('will always be float even if no weighting')", n.dtype.kind == "f", str(n.dtype))
xi = [0, 1, 1, 2, 3, 3, 3, 4, 5, 5]
n, b, _ = new_ax().hist(xi, bins=5)
info(f"integer data {xi}, bins=5: edges {list(b)} n {list(n)}")
report("hist(integer data, bins=5): values on interior edges go to the right-hand bin, max goes to the closed last bin -> [1, 2, 1, 3, 3]",
       list(n) == [1, 2, 1, 3, 3], f"{list(n)}")
n, b, _ = new_ax().hist(xi, bins=[0, 1, 2, 3, 4, 5])
report("hist(bins=[0..5] sequence): the docstring example rule '[1, 2) ... last bin [3, 4] includes 4' -> [1, 2, 1, 3, 3]", list(n) == [1, 2, 1, 3, 3], f"{list(n)}")
ue = [-3, -1, -0.25, 0, 0.5, 2.5, 3.5]
n, b, _ = new_ax().hist(data, bins=ue)
report("hist(unequal bin sequence): n = exact counts, bins returned unchanged", allclose(n, ex(port_hist(data, ue)), 0, 0) and allclose(b, ue, 0, 0))
n, b, _ = new_ax().hist(data, bins=ue, range=(-0.1, 0.1))
report("hist(bins=sequence, range=...): 'Range has no effect if bins is a sequence'", allclose(n, ex(port_hist(data, ue)), 0, 0) and allclose(b, ue, 0, 0))
n, b, _ = new_ax().hist(data, bins=8, range=(-1, 2))
report("hist(bins=8, range=(-1, 2)): edges linspace(-1, 2, 9), 'Lower and upper outliers are ignored'",
       edges_ok(b, lin_edges(-1, 2, 8)) and allclose(n, ex(port_hist(data, b)), 0, 0), f"{list(n)}")
for name, nbf in [("sturges", lambda N: math.ceil(math.log2(N)) + 1), ("sqrt", lambda N: math.ceil(math.sqrt(N))),
                  ("rice", lambda N: math.ceil(2 * N ** (1 / 3)))]:
    n, b, _ = new_ax().hist(data, bins=name)
    k = nbf(len(data))
    report(f"hist(bins='{name}'): {k} bins (closed form for N={len(data)}) spanning [min, max], counts exact",
           len(n) == k and edges_ok(b, lin_edges(min(data), max(data), k)) and allclose(n, ex(port_hist(data, b)), 0, 0), f"{len(n)} bins")
n, b, _ = new_ax().hist(data, bins="auto")
report("hist(bins='auto'): returned edges are equal-width over [min, max], counts exact (number of bins delegated to numpy)",
       edges_ok(b, lin_edges(min(data), max(data), len(n))) and allclose(n, ex(port_hist(data, b)), 0, 0), f"{len(n)} bins")

print("#### hist: density, weights, cumulative")
w = [rng.choice([0.5, 1, 2, 3.25]) for _ in data]
n, b, _ = new_ax().hist(data, bins=12, density=True)
c = port_hist(data, b); tot = sum(c); dens = [ci / (tot * (fr(b[i + 1]) - fr(b[i]))) for i, ci in enumerate(c)]
report("hist(density=True): n = counts / (sum(counts) * diff(bins)) (docstring formula)", allclose(n, ex(dens), 1e-13), f"maxdiff {maxdiff(n, ex(dens)):.2g}")
report("hist(density=True): sum(n * diff(bins)) == 1", close(float(np.sum(n * np.diff(b))), 1.0, 1e-13))
n, b, _ = new_ax().hist(data, bins=ue, density=True)
c = port_hist(data, ue); tot = sum(c); dens = [ci / (tot * (fr(ue[i + 1]) - fr(ue[i]))) for i, ci in enumerate(c)]
report("hist(density=True, unequal bins): divides by each bin's own width", allclose(n, ex(dens), 1e-13))
n, b, _ = new_ax().hist(data, bins=12, weights=w)
report("hist(weights=w): n = sum of weights per bin (exact)", allclose(n, ex(port_hist(data, b, w)), 1e-14))
n, b, _ = new_ax().hist(data, bins=12, weights=w, density=True)
c = port_hist(data, b, w); tot = sum(c); dens = [ci / (tot * (fr(b[i + 1]) - fr(b[i]))) for i, ci in enumerate(c)]
report("hist(weights, density=True): 'the weights are normalized, so that the integral of the density over the range remains 1'",
       allclose(n, ex(dens), 1e-13) and close(float(np.sum(n * np.diff(b))), 1, 1e-13))
n, b, _ = new_ax().hist(data, bins=12, cumulative=True)
c = port_hist(data, b); cum = [sum(c[:i + 1]) for i in range(len(c))]
report("hist(cumulative=True): 'each bin gives the counts in that bin plus all bins for smaller values', last bin = N",
       allclose(n, ex(cum), 0, 0) and n[-1] == len(data), f"{list(n)[-3:]}")
n, b, _ = new_ax().hist(data, bins=12, cumulative=-1)
rc = [sum(c[i:]) for i in range(len(c))]
report("hist(cumulative=-1): 'the direction of accumulation is reversed' (first bin = N)", allclose(n, ex(rc), 0, 0) and n[0] == len(data))
n, b, _ = new_ax().hist(data, bins=ue, cumulative=True, density=True)
c = port_hist(data, ue); cum = [sum(c[:i + 1]) / sum(c) for i in range(len(c))]
info(f"{len(data) - int(sum(c))} of {len(data)} values lie outside the edges [-3, 3.5] and are ignored")
report("hist(cumulative=True, density=True, unequal bins): cumulative fraction of the in-range values, 'normalized such that the last bin equals 1'",
       allclose(n, ex(cum), 1e-13) and close(n[-1], 1, 1e-14), f"{list(n)}")
n, b, _ = new_ax().hist(data, bins=ue, cumulative=-1, density=True)
rc = [sum(c[i:]) / sum(c) for i in range(len(c))]
report("hist(cumulative=-1, density=True): 'normalized such that the first bin equals 1'", allclose(n, ex(rc), 1e-13) and close(n[0], 1, 1e-14))
n, b, _ = new_ax().hist(data, bins=12, cumulative=True, weights=w)
cw = port_hist(data, b, w)
report("hist(cumulative=True, weights): last bin = sum of weights", allclose(n, ex([sum(cw[:i + 1]) for i in range(12)]), 1e-14) and close(n[-1], float(sum(fr(t) for t in w)), 1e-14))
n, b, _ = new_ax().hist(data, bins=8, range=(-1, 2), cumulative=True)
info(f"cumulative=True with range=(-1, 2): last bin {n[-1]} of N={len(data)} (outliers ignored; the cumulative text says 'The last bin gives the total number of datapoints')")

print("#### hist: several datasets, stacked, 2-D input, empty")
d1 = [rng.uniform(-2, 3) for _ in range(301)]; d2 = [rng.gauss(1, 0.7) for _ in range(150)]; d3 = [rng.uniform(0, 1) for _ in range(7)]
allv = d1 + d2 + d3
ns, b, _ = new_ax().hist([d1, d2, d3], bins=9)
report("hist([d1, d2, d3]) different lengths: one bins array over the combined range ('Always a single array')",
       edges_ok(b, lin_edges(min(allv), max(allv), 9)) and len(ns) == 3)
report("hist([d1, d2, d3]): each n_k equals its own exact count on the shared bins",
       all(allclose(ns[k], ex(port_hist(d, b)), 0, 0) for k, d in enumerate([d1, d2, d3])))
ns, b, _ = new_ax().hist([d1, d2, d3], bins=9, density=True)
ok = True
for k, d in enumerate([d1, d2, d3]):
    c = port_hist(d, b); dens = [ci / (len(d) * (fr(b[i + 1]) - fr(b[i]))) for i, ci in enumerate(c)]
    ok &= allclose(ns[k], ex(dens), 1e-13) and close(float(np.sum(ns[k] * np.diff(b))), 1, 1e-13)
report("hist([d1, d2, d3], density=True, not stacked): each dataset normalised separately (integral 1 each)", ok)
ns, b, _ = new_ax().hist([d1, d2, d3], bins=9, stacked=True)
cs = [port_hist(d, b) for d in (d1, d2, d3)]
cumk = [[sum(cs[j][i] for j in range(k + 1)) for i in range(9)] for k in range(3)]
report("hist(stacked=True): n_k is the running sum of datasets 0..k (stacked tops)", all(allclose(ns[k], ex(cumk[k]), 0, 0) for k in range(3)),
       f"top {list(ns[2])}")
ns, b, _ = new_ax().hist([d1, d2, d3], bins=ue, stacked=True, density=True)
cs = [port_hist(d, ue) for d in (d1, d2, d3)]; Ntot = sum(sum(cc) for cc in cs)
cumk = [[sum(cs[j][i] for j in range(k + 1)) / (Ntot * (fr(ue[i + 1]) - fr(ue[i]))) for i in range(len(ue) - 1)] for k in range(3)]
report("hist(stacked=True, density=True, unequal bins): 'the sum of the histograms is normalized to 1' (top integrates to 1, lower layers to their share)",
       all(allclose(ns[k], ex(cumk[k]), 1e-13) for k in range(3)) and close(float(np.sum(ns[2] * np.diff(b))), 1, 1e-13),
       f"integrals {[round(float(np.sum(ns[k]*np.diff(b))), 6) for k in range(3)]}")
ns, b, _ = new_ax().hist([d1, d2, d3], bins=ue, stacked=True, density=True, cumulative=True)
report("hist(stacked, density, cumulative): top layer's last bin equals 1", close(ns[2][-1], 1, 1e-13), f"{ns[2][-1]!r}")
A = np.array([[rng.uniform(0, 4) for _ in range(3)] for _ in range(40)])
ns, b, _ = new_ax().hist(A, bins=5)
report("hist(2-D ndarray (40, 3)): 3 datasets, one per column ('each column is a dataset')",
       len(ns) == 3 and all(allclose(ns[k], ex(port_hist(A[:, k], b)), 0, 0) for k in range(3)))
ns, b, _ = new_ax().hist([d3, []], bins=4)
report("hist([d, []]): the empty dataset gives zeros, the other its exact counts", allclose(ns[1], [0] * 4, 0, 0) and allclose(ns[0], ex(port_hist(d3, b)), 0, 0))
n, b, _ = new_ax().hist([], bins=4)
info(f"hist([]) -> n {list(n)} bins {list(b)} (numpy's default range (0, 1); the docstring is silent)")
report("hist([]): all-zero n of length 4", list(n) == [0, 0, 0, 0])
ws = [rng.uniform(0.1, 2) for _ in d1]
ns, b, _ = new_ax().hist([d1, d3], bins=6, weights=[ws, [1.5] * len(d3)])
report("hist([d1, d3], weights=[w1, w3]): per-dataset weighted counts on the combined range",
       allclose(ns[0], ex(port_hist(d1, b, ws)), 1e-14) and allclose(ns[1], ex(port_hist(d3, b, [1.5] * len(d3))), 1e-14))

print("#### hist: NaN, inf, constant, float32, large offsets")
dn = [0.1, 0.4, float("nan"), 0.9, float("nan"), 0.5]
n, b, _ = new_ax().hist(dn, bins=4)
report("hist(data with NaN): NaN values are dropped and the range comes from the finite values",
       edges_ok(b, lin_edges(0.1, 0.9, 4)) and allclose(n, ex(port_hist(dn, b)), 0, 0) and sum(n) == 4, f"{list(n)}")
ns, b, _ = new_ax().hist([dn, [0.2, float("nan")]], bins=4)
report("hist([with NaN, with NaN]): NaN dropped in both datasets", sum(ns[0]) == 4 and sum(ns[1]) == 1)
di = [1.0, 2.0, 2.5, float("inf")]
r = raises(lambda: new_ax().hist(di, bins=3))
info(f"hist([1, 2, 2.5, inf], bins=3) -> {r}  (the docstring says nothing about inf)")
n, b, _ = new_ax().hist(di, bins=3, range=(1, 3))
report("hist(data with inf, explicit range=(1, 3), bins=3): inf is an upper outlier and is ignored -> [1, 1, 1]", list(n) == [1, 1, 1], f"{list(n)}")
r = raises(lambda: new_ax().hist([float("nan")] * 3, bins=3))
info(f"hist(all-NaN) -> {r}")
n, b, _ = new_ax().hist([3.0, 3.0, 3.0], bins=3)
info(f"hist([3, 3, 3], bins=3) -> n {list(n)} bins {list(b)} (degenerate range widened by numpy to +-0.5)")
report("hist(constant data): all three values counted once", sum(n) == 3)
d32 = np.array([rng.uniform(-1, 1) for _ in range(500)], np.float32)
n, b, _ = new_ax().hist(d32, bins=7)
report("hist(float32): counts exact against the returned edges, sum = N", allclose(n, ex(port_hist(d32, b)), 0, 0) and sum(n) == 500)
info(f"hist(float32): returned bins dtype {b.dtype} (the docstring only says 'array'; 3.6+ casts to float64)")
off = [1e9 + 0.001 * k for k in range(41)]
n, b, _ = new_ax().hist(off, bins=4)
report("hist(1e9 + 0.001k, k=0..40, bins=4): counts [10, 10, 10, 11] by the closed form (0.01-wide bins)",
       allclose(n, ex(port_hist(off, b)), 0, 0) and sum(n) == 41, f"{list(n)}")
n, b, _ = new_ax().hist(np.array([0, 1, 2, 3, 4, 5, 5], np.int8), bins=5)
report("hist(int8 data): edges 0..5, counts [1, 1, 1, 1, 3]", list(n) == [1, 1, 1, 1, 3] and allclose(b, [0, 1, 2, 3, 4, 5], 0, 0), f"{list(n)}")

print("#### hist: drawn geometry equals n (bar, barstacked, step, stepfilled, bottom, log)")
def hsegs(verts):
    s = set()
    for (x0, y0), (x1, y1) in zip(verts[:-1], verts[1:]):
        if y0 == y1 and x0 != x1: s.add((min(x0, x1), max(x0, x1), y0))
    return s
for ht in ("step", "stepfilled"):
    ax = new_ax(); n, b, p = ax.hist(data, bins=10, histtype=ht)
    v = p[0].get_xy(); s = hsegs(v)
    report(f"hist(histtype='{ht}'): the outline has a horizontal segment (e_i, e_i+1) at height n_i for every bin",
           all((b[i], b[i + 1], n[i]) in s for i in range(10)), f"{len(v)} vertices")
    ax = new_ax(); ns, b, p = ax.hist([d1, d2], bins=6, histtype=ht, stacked=True)
    s = hsegs(p[1][0].get_xy())
    report(f"hist(histtype='{ht}', stacked): the second polygon's top is at the stacked n_1", all((b[i], b[i + 1], ns[1][i]) in s for i in range(6)))
ax = new_ax(); n, b, p = ax.hist(data, bins=10, histtype="step", bottom=5)
s = hsegs(p[0].get_xy())
report("hist(histtype='step', bottom=5): outline at n_i + 5", all((b[i], b[i + 1], n[i] + 5) in s for i in range(10)))
ax = new_ax(); n, b, p = ax.hist(data, bins=10)
report("hist(histtype='bar'): bar i spans [e_i, e_i+1] with height n_i",
       all(close(r.get_x(), b[i], 1e-12) and close(r.get_x() + r.get_width(), b[i + 1], 1e-12) and r.get_height() == n[i] for i, r in enumerate(p)))
ax = new_ax(); ns, b, p = ax.hist([d1, d2, d3], bins=6, histtype="barstacked")
report("hist(histtype='barstacked'): layer k bars have bottom n_{k-1} and top n_k",
       all(close(r.get_y() + r.get_height(), ns[k][i], 1e-12) and close(r.get_y(), (ns[k - 1][i] if k else 0), 1e-12)
           for k in range(3) for i, r in enumerate(p[k])))
ax = new_ax(); n, b, p = ax.hist(data, bins=10, log=True)
report("hist(log=True): y axis is log-scaled, n unchanged, bar heights = n", ax.get_yscale() == "log" and allclose(n, ex(port_hist(data, b)), 0, 0)
       and all(r.get_height() == n[i] for i, r in enumerate(p)))
ax = new_ax(); n, b, p = ax.hist(data, bins=10, log=True, histtype="step")
report("hist(log=True, histtype='step'): y axis is log-scaled", ax.get_yscale() == "log")
ax = new_ax(); n, b, p = ax.hist(data, bins=10, orientation="horizontal", histtype="step")
s = set()
v = p[0].get_xy()
for (x0, y0), (x1, y1) in zip(v[:-1], v[1:]):
    if x0 == x1 and y0 != y1: s.add((min(y0, y1), max(y0, y1), x0))
report("hist(orientation='horizontal', 'step'): vertical outline segments at x = n_i", all((b[i], b[i + 1], n[i]) in s for i in range(10)))

print("#### Axes.stairs")
vals = [3, 0, 2.5, -1, 4]; ed = [0, 1, 1.5, 4, 5, 7]
ax = new_ax(); sp = ax.stairs(vals, ed)
verts = sp.get_path().vertices
s = hsegs(verts)
report("stairs(values, edges): a horizontal segment (e_i, e_i+1) at values_i for each i", all((ed[i], ed[i + 1], vals[i]) in s for i in range(5)),
       f"{verts.tolist()[:4]}")
report("stairs(): path starts and ends at the baseline 0", verts[0][1] == 0 and verts[-1][1] == 0 and verts[0][0] == 0 and verts[-1][0] == 7)
ax = new_ax(); sp = ax.stairs(vals)
report("stairs(values) with edges=None: edges are 0..len(values)", all((i, i + 1, vals[i]) in hsegs(sp.get_path().vertices) for i in range(5)))
ax = new_ax(); sp = ax.stairs(vals, ed, baseline=None)
v = sp.get_path().vertices
report("stairs(baseline=None): unclosed path, first point (e_0, v_0), last (e_n, v_last)", tuple(v[0]) == (0, 3) and tuple(v[-1]) == (7, 4), f"{v.tolist()}")
cnt, edg = np.histogram(data, bins=9)
ax = new_ax(); sp = ax.stairs(cnt, edg)
report("stairs(*np.histogram(x)): drawn steps equal the counts", all((edg[i], edg[i + 1], cnt[i]) in hsegs(sp.get_path().vertices) for i in range(9)))

# ------------------------------------------------------------------ hist2d
print("#### Axes.hist2d")
def port_h2(xs, ys, ex_, ey_, w=None):
    H = [[F(0)] * (len(ey_) - 1) for _ in range(len(ex_) - 1)]
    for k, (a, c) in enumerate(zip(xs, ys)):
        def idx(v, e):
            v = fr(v); e = [fr(t) for t in e]
            for i in range(len(e) - 1):
                if e[i] <= v < e[i + 1] or (i == len(e) - 2 and v == e[-1]): return i
            return None
        i = idx(a, ex_); j = idx(c, ey_)
        if i is not None and j is not None: H[i][j] += F(1) if w is None else fr(w[k])
    return H
X = [rng.uniform(0, 4) for _ in range(400)] + [0, 4, 4, 2]; Y = [rng.uniform(-1, 1) for _ in range(400)] + [-1, 1, -1, 0]
h, xe, ye, _ = new_ax().hist2d(X, Y, bins=(4, 5))
report("hist2d(bins=(4, 5)): x edges linspace(min, max, 5), y edges linspace(min, max, 6)", edges_ok(xe, lin_edges(0, 4, 4)) and edges_ok(ye, lin_edges(-1, 1, 5)))
T = port_h2(X, Y, xe, ye)
report("hist2d: h[i, j] counts x in x-bin i and y in y-bin j ('Values in x are histogrammed along the first dimension'), last bins closed",
       h.shape == (4, 5) and allclose(h, [[float(t) for t in r] for r in T], 0, 0) and h.sum() == len(X), f"corner {h[-1, -1]} {h[-1, 0]}")
h, xe, ye, _ = new_ax().hist2d(X, Y, bins=3, density=True)
T = port_h2(X, Y, xe, ye)
D = [[float(T[i][j] / (len(X) * (fr(xe[i + 1]) - fr(xe[i])) * (fr(ye[j + 1]) - fr(ye[j])))) for j in range(3)] for i in range(3)]
report("hist2d(density=True): count / (N * dx * dy), integrates to 1", allclose(h, D, 1e-13) and close(float((h * np.outer(np.diff(xe), np.diff(ye))).sum()), 1, 1e-13))
ww = [rng.uniform(0, 3) for _ in X]
h, xe, ye, _ = new_ax().hist2d(X, Y, bins=[[0, 1, 3, 4], [-1, 0, 1]], weights=ww)
T = port_h2(X, Y, xe, ye, ww)
report("hist2d(bins=[x edges, y edges], weights): weighted sums per cell", allclose(h, [[float(t) for t in r] for r in T], 1e-13))
h, xe, ye, _ = new_ax().hist2d(X, Y, bins=4, range=[[1, 3], [-0.5, 0.5]])
T = port_h2(X, Y, xe, ye)
report("hist2d(range=[[1, 3], [-0.5, 0.5]]): outliers not tallied", allclose(h, [[float(t) for t in r] for r in T], 0, 0) and edges_ok(xe, lin_edges(1, 3, 4)))
h0, xe, ye, _ = new_ax().hist2d(X, Y, bins=(4, 5))
counts = np.array(h0)
mid = float(np.median(counts)); lo_, hi_ = int(np.min(counts)) + 3, int(np.max(counts)) - 3
h, xe, ye, qm = new_ax().hist2d(X, Y, bins=(4, 5), cmin=lo_)
report(f"hist2d(cmin={lo_}): exactly the cells with count < cmin are NaN ('count less than cmin'); count == cmin kept",
       np.array_equal(np.isnan(h), counts < lo_) and np.all(h[~np.isnan(h)] == counts[counts >= lo_]) and np.any(counts == lo_) or not np.any(counts == lo_) and np.array_equal(np.isnan(h), counts < lo_),
       f"{int(np.sum(counts == lo_))} cells with count == cmin")
h, xe, ye, qm = new_ax().hist2d(X, Y, bins=(4, 5), cmax=hi_)
report(f"hist2d(cmax={hi_}): exactly the cells with count > cmax are NaN", np.array_equal(np.isnan(h), counts > hi_), f"{int(np.sum(counts == hi_))} cells with count == cmax")
arr = qm.get_array()
report("hist2d: the QuadMesh array is h.T (masked where NaN)", np.array_equal(np.ma.filled(np.ma.masked_invalid(arr).astype(float), -1).ravel(), np.nan_to_num(h.T, nan=-1).ravel()))
hd, xe, ye, _ = new_ax().hist2d(X, Y, bins=(4, 5), density=True, cmin=lo_)
info(f"hist2d(density=True, cmin={lo_}): {int(np.sum(np.isnan(hd)))} of 20 cells NaN; densities range {np.nanmin(hd) if not np.all(np.isnan(hd)) else 'all NaN'}")
report(f"hist2d(density=True, cmin={lo_}): 'All bins that has count less than cmin will not be displayed' -> NaN pattern follows the counts",
       np.array_equal(np.isnan(hd), counts < lo_), f"{int(np.sum(np.isnan(hd)))} NaN vs {int(np.sum(counts < lo_))} expected")
r = raises(lambda: new_ax().hist2d([0, 1, float("nan")], [0, 1, 1], bins=2))
info(f"hist2d with NaN in x and no range -> {r}")

# ------------------------------------------------------------------ hexbin
print("#### Axes.hexbin: grid, counts vs the drawn hexagons, conservation")
def hex_polys(pc):
    offs = np.asarray(pc.get_offsets(), float); base = pc.get_paths()[0].vertices[:6]
    return offs, base
def classify(px, py, offs, base):
    """Exact (Fraction) closed point-in-convex-hexagon test; returns (inside_strict, on_boundary) index lists."""
    P = (fr(px), fr(py)); ins = []; onb = []
    bx = [fr(v[0]) for v in base]; by = [fr(v[1]) for v in base]
    for m, (ox, oy) in enumerate(offs):
        if abs(px - ox) > 1.01 * float(max(bx) - min(bx)) or abs(py - oy) > 1.01 * float(max(by) - min(by)): continue
        fo = (fr(ox), fr(oy)); sgn = []
        for k in range(6):
            a = (fo[0] + bx[k], fo[1] + by[k]); b2 = (fo[0] + bx[(k + 1) % 6], fo[1] + by[(k + 1) % 6])
            sgn.append((b2[0] - a[0]) * (P[1] - a[1]) - (b2[1] - a[1]) * (P[0] - a[0]))
        if all(s > 0 for s in sgn) or all(s < 0 for s in sgn): ins.append(m)
        elif all(s >= 0 for s in sgn) or all(s <= 0 for s in sgn): onb.append(m)
    return ins, onb
def check_hex_counts(label, pc, xs, ys, vals=None, red=None, require_all=True):
    offs, base = hex_polys(pc); arr = np.asarray(pc.get_array(), float)
    strict = [[] for _ in offs]; bnd = []; outside = 0
    for k, (a, c) in enumerate(zip(xs, ys)):
        ins, onb = classify(a, c, offs, base)
        if len(ins) == 1 and not onb: strict[ins[0]].append(k)
        elif onb: bnd.append((k, onb))
        else: outside += 1
    if vals is None:
        lo = [len(s) for s in strict]; hi = lo[:]
        for k, onb in bnd:
            for m in onb: hi[m] += 1
        ok = all(lo[m] <= arr[m] <= hi[m] for m in range(len(offs))) and (not require_all or float(arr.sum()) == len(xs) - outside)
        report(label, ok, f"{len(bnd)} boundary points, {outside} outside all drawn hexagons, sum {arr.sum()} of {len(xs)}")
    else:
        tr = [red([vals[k] for k in s]) if s else None for s in strict]
        ok = not bnd and all((t is None) or close(arr[m], t, 1e-12) for m, t in enumerate(tr)) and len(arr) == sum(1 for t in tr if t is not None)
        report(label, ok, f"{len(bnd)} boundary points; {len(arr)} hexagons vs {sum(1 for t in tr if t is not None)} occupied")
    return strict
HX = [rng.gauss(0, 1) for _ in range(600)]; HY = [rng.gauss(0, 2) for _ in range(600)]
for gs in (5, 8, (6, 4)):
    pc = new_ax().hexbin(HX, HY, gridsize=gs)
    offs = np.asarray(pc.get_offsets()); nx = gs if np.isscalar(gs) else gs[0]; ny = int(nx / math.sqrt(3)) if np.isscalar(gs) else gs[1]
    ncols = len(np.unique(np.round(offs[:, 0], 9))); nrows = len(np.unique(np.round(offs[:, 1], 9)))
    report(f"hexbin(gridsize={gs}): two interleaved lattices, (nx+1)(ny+1) + nx*ny centres with ny = {'int(nx/sqrt(3))' if np.isscalar(gs) else 'given'} = {ny}",
           len(offs) == (nx + 1) * (ny + 1) + nx * ny and ncols == 2 * nx + 1 and nrows == 2 * ny + 1, f"{len(offs)} centres, {ncols} columns, {nrows} rows")
    xs = np.unique(np.round(offs[:, 0], 12))
    report(f"hexbin(gridsize={gs}): the hexagon columns span [min(x), max(x)] (to the 1e-9 padding)",
           close(xs[0], min(HX), 0, 2e-8 * (max(HX) - min(HX))) and close(xs[-1], max(HX), 0, 2e-8 * (max(HX) - min(HX))))
    if np.isscalar(gs):
        base = pc.get_paths()[0].vertices[:6]
        sx = (xs[-1] - xs[0]) / nx; ys_ = np.unique(np.round(offs[:, 1], 12)); sy = (ys_[-1] - ys_[0]) / ny
        report(f"hexbin(gridsize={gs}): hexagon vertices (+-sx/2, +-sy/6), (0, +-sy/3) (regular in axes units when nx/ny ~ sqrt(3))",
               allclose(np.sort(base[:, 0]), np.sort([.5 * sx, .5 * sx, 0, -.5 * sx, -.5 * sx, 0]), 1e-9, 1e-12) and
               allclose(np.sort(base[:, 1]), np.sort([-sy / 6, sy / 6, sy / 3, sy / 6, -sy / 6, -sy / 3]), 1e-9, 1e-12))
    check_hex_counts(f"hexbin(gridsize={gs}): each hexagon's value = the number of points inside that drawn hexagon; all N points counted", pc, HX, HY)
pc = new_ax().hexbin(HX, HY, gridsize=7)
report("hexbin: total count conservation sum(get_array()) == N (default extent)", float(np.sum(pc.get_array())) == len(HX))
report("hexbin(C=None, mincnt=None): every centre is returned, empty hexagons have value 0", np.min(pc.get_array()) == 0 and len(pc.get_array()) == 8 * 5 + 7 * 4)
GX = [k * 0.5 for k in range(-4, 5) for _ in range(3)]; GY = [((k % 5) - 2) * 0.5 for k in range(-4, 5) for _ in range(3)]
GX += [0.0, 0.25, -0.25, 1.0, 2.0]; GY += [0.0, 0.0, 0.5, 1.0, -1.0]
pc = new_ax().hexbin(GX, GY, gridsize=4)
check_hex_counts("hexbin(grid-aligned points, many on centres / near edges): counts consistent with the drawn hexagons, each point counted once", pc, GX, GY)
pc = new_ax().hexbin(HX, HY, gridsize=6, extent=(-1, 1, -2, 2))
check_hex_counts("hexbin(extent=(-1, 1, -2, 2)): points inside a drawn hexagon are counted there, the rest dropped", pc, HX, HY, require_all=False)
info(f"extent=(-1, 1, -2, 2): sum {np.sum(pc.get_array())} of {len(HX)} (points just outside the extent but inside an edge hexagon are counted)")
NX = HX[:50] + [float("nan"), float("inf"), 1.0]; NY = HY[:50] + [0.0, 0.0, float("nan")]
pc = new_ax().hexbin(NX, NY, gridsize=5)
report("hexbin(x/y with NaN and inf): non-finite points dropped (cbook.delete_masked_points), finite total conserved", float(np.sum(pc.get_array())) == 50,
       f"sum {np.sum(pc.get_array())}")
pc = new_ax().hexbin([2.0] * 5, [3.0] * 5, gridsize=4)
report("hexbin(constant data): all 5 points in one hexagon (singular extent expanded)", float(np.max(pc.get_array())) == 5 and float(np.sum(pc.get_array())) == 5)
pc = new_ax().hexbin(np.array(HX, np.float32), np.array(HY, np.float32), gridsize=6)
report("hexbin(float32): total conserved", float(np.sum(pc.get_array())) == len(HX))
pc = new_ax().hexbin([1e9 + t for t in HX], HY, gridsize=6)
check_hex_counts("hexbin(x offset by 1e9): counts consistent with the drawn hexagons", pc, [1e9 + t for t in HX], HY)

print("#### hexbin: C and reduce_C_function, mincnt")
HC = [rng.uniform(-3, 5) for _ in HX]
for red, nm in [(np.mean, "np.mean (default)"), (np.sum, "np.sum"), (np.max, "np.max")]:
    kw = {} if red is np.mean else {"reduce_C_function": red}
    pc = new_ax().hexbin(HX, HY, C=HC, gridsize=6, **kw)
    fred = {"np.mean (default)": lambda v: float(sum(fr(t) for t in v) / len(v)), "np.sum": lambda v: float(sum(fr(t) for t in v)), "np.max": max}[nm]
    check_hex_counts(f"hexbin(C, reduce_C_function={nm}): each shown hexagon's value is the reduction over the C values of the points inside it; empty hexagons omitted",
                     pc, HX, HY, vals=HC, red=fred)
pc0 = new_ax().hexbin(HX, HY, gridsize=6); cnt = np.asarray(pc0.get_array())
doc = Axes_doc = matplotlib.axes.Axes.hexbin.__doc__
inclusive_doc = "at least *mincnt*" in " ".join(doc.split()) or "at least" in doc.split("mincnt")[1][:200]
info(f"mincnt docstring in this build: {' '.join(doc.split('mincnt :')[1].split(chr(10))[:3]).strip()[:110]!r}")
for mc in (2, 3):
    pc = new_ax().hexbin(HX, HY, gridsize=6, mincnt=mc)
    keep = cnt >= mc if inclusive_doc else cnt > mc
    report(f"hexbin(C=None, mincnt={mc}): shown cells follow this build's docstring ({'at least' if inclusive_doc else 'more than'} mincnt points)",
           sorted(np.asarray(pc.get_array()).tolist()) == sorted(cnt[keep].tolist()), f"{len(pc.get_array())} shown vs {int(keep.sum())}; {int(np.sum(cnt == mc))} cells have exactly {mc}")
    pcC = new_ax().hexbin(HX, HY, C=[1.0] * len(HX), reduce_C_function=np.sum, gridsize=6, mincnt=mc)
    report(f"hexbin(C=ones, np.sum, mincnt={mc}): shown cells follow this build's docstring",
           sorted(np.asarray(pcC.get_array()).tolist()) == sorted(cnt[keep].tolist()), f"{len(pcC.get_array())} shown vs {int(keep.sum())}")
    if V >= (3, 8):
        report(f"hexbin(mincnt={mc}): C=None and C=ones/np.sum show the same cells (3.8.0 note: 'now inclusive of mincnt in both cases')",
               sorted(np.asarray(pc.get_array()).tolist()) == sorted(np.asarray(pcC.get_array()).tolist()))
    else:
        report(f"hexbin(mincnt={mc}) < 3.8: C=None inclusive, C given exclusive (the old behaviour the 3.8.0 API note describes)",
               sorted(np.asarray(pc.get_array()).tolist()) == sorted(cnt[cnt >= mc].tolist()) and sorted(np.asarray(pcC.get_array()).tolist()) == sorted(cnt[cnt > mc].tolist()))
pc = new_ax().hexbin(HX, HY, C=[1.0] * len(HX), reduce_C_function=np.sum, gridsize=6)
report("hexbin(C given, mincnt=None): cells with >= 1 point are shown (3.8.1 note: default requires at least 1 point)",
       sorted(np.asarray(pc.get_array()).tolist()) == sorted(cnt[cnt >= 1].tolist()))
pc = new_ax().hexbin(HX, HY, gridsize=6, mincnt=0)
report("hexbin(C=None, mincnt=0): all hexagons shown, including zeros", len(pc.get_array()) == len(cnt))
if inclusive_doc:
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always")
        pc = new_ax().hexbin(HX, HY, C=HC, gridsize=6, mincnt=0, reduce_C_function=lambda v: len(v))
    report("hexbin(C, mincnt=0): 'if set to 0 will pass empty input to the reduction function' (all hexagons reduced)", len(pc.get_array()) == len(cnt)
           and sorted(np.asarray(pc.get_array()).tolist()) == sorted(cnt.tolist()))

print("#### hexbin: bins='log', integer and sequence bins")
pc = new_ax().hexbin(HX, HY, gridsize=6, bins="log")
arr = np.ma.asarray(pc.get_array()); normed = pc.norm(arr)
plus1 = "log_{10}(i+1)" in doc
nz = cnt > 0
info(f"bins='log' docstring in this build: {'log10(i+1)' if plus1 else 'log10(i) / LogNorm'}; array min {arr.min()} max {arr.max()}; norm {type(pc.norm).__name__}")
if plus1:
    t = np.log10(cnt + 1.0); tt = (t - t.min()) / (t.max() - t.min())
    ok = not np.any(np.ma.getmaskarray(normed)) and allclose(np.ma.filled(normed, np.nan), tt, 1e-12)
    report("hexbin(bins='log'): colour position follows the documented log10(i+1) (zero-count cells get the lowest colour, not 'bad')", ok,
           f"{int(np.sum(np.ma.getmaskarray(normed) | ~np.isfinite(np.ma.filled(normed, np.nan))))} cells masked/bad; first values {np.ma.filled(normed, np.nan)[:4]} vs {tt[:4]}")
else:
    t = np.log10(cnt[nz]); tt = (t - t.min()) / (t.max() - t.min())
    nf = np.ma.filled(normed.astype(float), np.nan)
    bad = np.ma.getmaskarray(normed) | ~np.isfinite(nf)
    report("hexbin(bins='log'): colour position = (log10 i - log10 min)/(log10 max - log10 min) ('equivalent to norm=LogNorm()'), zero counts 'bad'",
           allclose(nf[nz], tt, 1e-12) and np.all(bad[~nz]), f"{int(np.sum(bad))} bad cells, {int(np.sum(~nz))} zero-count cells")
report("hexbin(bins='log'): get_array() still holds the raw counts", allclose(np.ma.filled(arr, np.nan), cnt, 0, 0))
pcs = new_ax().hexbin(HX, HY, gridsize=6, mincnt=1)
c1 = np.asarray(pcs.get_array()); k = 3
pc = new_ax().hexbin(HX, HY, gridsize=6, mincnt=1, bins=k)
got = np.asarray(pc.get_array())
lo, hi = float(c1.min()), float(c1.max())
eq = [min(int((F(int(v)) - F(int(lo))) * k / (F(int(hi)) - F(int(lo)))), k - 1) for v in c1]
info(f"bins={k}: counts {sorted(set(c1.tolist()))} -> classes {sorted(set(got.tolist()))}; per-class counts {[int(np.sum(got == j)) for j in range(k)]} vs equal-width {[eq.count(j) for j in range(k)]}")
report(f"hexbin(bins={k}): 'divide the counts in the specified number of bins' -> equal-width classes over [min, max] (last closed)",
       len(set(got.tolist())) <= k and all(int(got[m]) == eq[m] for m in range(len(c1))) or
       all((got[m] == got[q]) == (eq[m] == eq[q]) for m in range(len(c1)) for q in range(len(c1))),
       f"min count {lo:g} alone in class 0: {int(np.sum(got == got[np.argmin(c1)]))} cells, {int(np.sum(c1 == lo))} with the min count")
bnd = [1, 4, 8]
pc = new_ax().hexbin(HX, HY, gridsize=6, mincnt=1, bins=bnd)
got = np.asarray(pc.get_array())
def lower_bound_class(v):
    j = -1
    for i, l in enumerate(bnd):
        if v >= l: j = i
    return j
same = all((got[m] == got[q]) == (lower_bound_class(c1[m]) == lower_bound_class(c1[q])) for m in range(len(c1)) for q in range(len(c1)))
info(f"bins=[1, 4, 8]: count -> class {dict(sorted({int(c): int(g) for c, g in zip(c1, got)}.items()))}")
report("hexbin(bins=[1, 4, 8]): 'the values of the lower bound of the bins' -> counts 4..7 share a class, a count of 4 does not share with 3",
       same, "a count equal to a lower bound is put in the bin below")

print("#### hexbin: xscale / yscale = 'log', get_offsets, marginals")
LX = [10 ** rng.uniform(0, 3) for _ in range(400)]; LY = [rng.uniform(0, 5) for _ in range(400)]
def port_hexgrid(tx, ty, nx, ny, extent=None):
    """Two interleaved lattices from the docstring's description, nearest centre in the
    regular-hexagon metric dx^2 + 3 dy^2 (index units), out-of-range lattice cells dropped."""
    if extent is None:
        xmin, xmax, ymin, ymax = min(tx), max(tx), min(ty), max(ty)
    else:
        xmin, xmax, ymin, ymax = extent
    pad = 1e-9 * (xmax - xmin); xmin -= pad; xmax += pad
    sx = (xmax - xmin) / nx; sy = (ymax - ymin) / ny
    L1 = [[0] * (ny + 1) for _ in range(nx + 1)]; L2 = [[0] * ny for _ in range(nx)]
    for a, c in zip(tx, ty):
        best = None
        for i in range(nx + 1):
            for j in range(ny + 1):
                d = ((a - xmin) / sx - i) ** 2 + 3 * ((c - ymin) / sy - j) ** 2
                if best is None or d < best[0]: best = (d, 1, i, j)
        for i in range(nx):
            for j in range(ny):
                d = ((a - xmin) / sx - i - .5) ** 2 + 3 * ((c - ymin) / sy - j - .5) ** 2
                if d < best[0]: best = (d, 2, i, j)
        (L1 if best[1] == 1 else L2)[best[2]][best[3]] += 1
    cen = [(xmin + i * sx, ymin + j * sy) for i in range(nx + 1) for j in range(ny + 1)] + \
          [(xmin + (i + .5) * sx, ymin + (j + .5) * sy) for i in range(nx) for j in range(ny)]
    return [v for r in L1 for v in r] + [v for r in L2 for v in r], cen, (xmin, xmax, ymin, ymax)
tl, cen, lim = port_hexgrid([math.log10(v) for v in LX], LY, 6, 3)
pc = new_ax().hexbin(LX, LY, gridsize=6, xscale="log")
report("hexbin(xscale='log'): counts = nearest-centre assignment on the grid in log10(x) (multiset of all cell counts), total conserved",
       sorted(np.asarray(pc.get_array()).tolist()) == sorted(tl) and float(np.sum(pc.get_array())) == len(LX), f"max {max(tl)}")
pc = new_ax().hexbin(LX, LY, gridsize=6, xscale="log", mincnt=1)
cd = [(10 ** cx, cy) for (cx, cy), v in zip(cen, tl) if v >= 1]
offs = np.asarray(pc.get_offsets())
okoff = offs.shape == (len(cd), 2) and allclose(np.array(sorted(map(tuple, offs.tolist()))), np.array(sorted(cd)), 1e-9, 1e-9)
report("hexbin(xscale='log').get_offsets(): 'the x, y positions of the M hexagon centers in data coordinates'", okoff,
       f"shape {offs.shape} vs ({len(cd)}, 2); first rows {offs[:2].tolist()} vs {sorted(cd)[:2]}")
pc = new_ax().hexbin(LY, LX, gridsize=6, yscale="log", extent=(0, 5, 0, 3))
tl2, _, _ = port_hexgrid(LY, [math.log10(v) for v in LX], 6, 3, extent=(0, 5, 0, 3))
report("hexbin(yscale='log', extent=(0, 5, 0, 3)) ('limits are expected to be the exponent'): counts match the log10(y) grid",
       sorted(np.asarray(pc.get_array()).tolist()) == sorted(tl2), f"sum {np.sum(pc.get_array())} vs {sum(tl2)}")
r = raises(lambda: new_ax().hexbin([0.0, 1.0], [1.0, 2.0], xscale="log"))
report("hexbin(xscale='log') with x <= 0: ValueError", (r or "").startswith("ValueError"), str(r))
tlin, cenl, (xmn, xmx, ymn, ymx) = port_hexgrid(HX, HY, 6, 3)
pc = new_ax().hexbin(HX, HY, gridsize=6)
report("hexbin(linear): counts equal the plain-Python nearest-centre port in the same cell order", allclose(pc.get_array(), tlin, 0, 0))
pc = new_ax().hexbin(HX, HY, gridsize=6, marginals=True)
def marg(z, lo, hi, nb, vals=None, red=None):
    e = [lo + (hi - lo) * i / nb for i in range(nb + 1)]; out = []
    for i in range(nb):
        sel = [k for k, t in enumerate(z) if e[i] < t <= e[i + 1] or (i == 0 and t == e[0])]
        if sel: out.append(len(sel) if vals is None else red([vals[k] for k in sel]))
    return out
mx = marg(HX, xmn, xmx, 6); my = marg(HY, ymn, ymx, 2 * 3)
hb = np.asarray(pc.hbar.get_array()); vb = np.asarray(pc.vbar.get_array())
info(f"marginals (C=None): hbar values {hb.tolist()} ; x counts per column {mx}")
report("hexbin(marginals=True, C=None): 'plot the marginal density' -> hbar values proportional to the number of points per x-bin",
       len(hb) == len(mx) and allclose(hb / hb.sum(), np.array(mx) / sum(mx), 1e-12), f"{hb.tolist()} vs counts {mx}")
report("hexbin(marginals=True, C=None): vbar values proportional to the number of points per y-bin",
       len(vb) == len(my) and allclose(vb / vb.sum(), np.array(my) / sum(my), 1e-12), f"{vb.tolist()} vs counts {my}")
pc = new_ax().hexbin(HX, HY, C=HC, reduce_C_function=np.sum, gridsize=6, marginals=True)
mxs = marg(HX, xmn, xmx, 6, HC, lambda v: float(sum(fr(t) for t in v)))
report("hexbin(marginals=True, C, np.sum): hbar = sum of C per x-bin", allclose(pc.hbar.get_array(), mxs, 1e-12), f"{np.asarray(pc.hbar.get_array())[:3]} vs {mxs[:3]}")
pc = new_ax().hexbin(HX, HY, C=HC, gridsize=6, marginals=True)
mxm = marg(HX, xmn, xmx, 6, HC, lambda v: float(sum(fr(t) for t in v) / len(v)))
report("hexbin(marginals=True, C, default np.mean): hbar = mean of C per x-bin", allclose(pc.hbar.get_array(), mxm, 1e-12))

# ------------------------------------------------------------------ acorr / xcorr
print("#### Axes.acorr / xcorr")
def xc_true(x, y, lags):
    """Docstring: correlation at lag k is sum_n x[n+k] * conj(y[n])."""
    N = len(x); out = []
    for k in lags:
        s = 0
        for n_ in range(N):
            if 0 <= n_ + k < N: s += x[n_ + k] * (y[n_].conjugate() if isinstance(y[n_], complex) else y[n_])
        out.append(s)
    return out
xa = [F(rng.randint(-20, 20), 4) for _ in range(23)]; ya = [F(rng.randint(-20, 20), 8) for _ in range(23)]
xf = [float(t) for t in xa]; yf = [float(t) for t in ya]
lags, c, *_ = new_ax().xcorr(xf, yf, normed=False, maxlags=6)
report("xcorr(normed=False, maxlags=6): lag vector -6..6 and c_k = sum_n x[n+k] y[n] (exact)",
       list(lags) == list(range(-6, 7)) and allclose(c, [float(t) for t in xc_true(xa, ya, range(-6, 7))], 1e-14), f"{c[:3]}")
lags, c, *_ = new_ax().xcorr(xf, yf, maxlags=6)
nrm = math.sqrt(float(sum(t * t for t in xa) * sum(t * t for t in ya)))
report("xcorr(normed=True default): c / sqrt(dot(x,x) dot(y,y)) ('input vectors are normalised to unit length')",
       allclose(c, [float(t) / nrm for t in xc_true(xa, ya, range(-6, 7))], 1e-13))
lags, c, *_ = new_ax().acorr(xf)
report("acorr(x): default maxlags=10 -> 21 lags, c[0 lag] == 1, symmetric", len(lags) == 21 and close(c[10], 1, 1e-15) and allclose(c, c[::-1], 1e-14))
lags, c, *_ = new_ax().acorr(xf, maxlags=None)
report("acorr(maxlags=None): all 2N-1 lags, equal to the exact normalised sums",
       len(c) == 45 and list(lags) == list(range(-22, 23)) and allclose(c, [float(t / sum(u * u for u in xa)) for t in xc_true(xa, xa, range(-22, 23))], 1e-13))
r = raises(lambda: new_ax().acorr(xf, maxlags=23)); report("acorr(maxlags=N): ValueError ('strictly positive < N')", (r or "").startswith("ValueError"), str(r))
m = sum(xa) / len(xa); xd = [t - m for t in xa]
lags, c, *_ = new_ax().acorr(xf, maxlags=4, detrend=matplotlib.mlab.detrend_mean)
report("acorr(detrend=mlab.detrend_mean): autocorrelation of x - mean, normalised", allclose(c, [float(t / sum(u * u for u in xd)) for t in xc_true(xd, xd, range(-4, 5))], 1e-13))
tt_ = [F(i) for i in range(len(xa))]; tm = sum(tt_) / len(tt_)
slope = sum((t - tm) * (v - m) for t, v in zip(tt_, xa)) / sum((t - tm) ** 2 for t in tt_)
xl = [v - (m + slope * (t - tm)) for t, v in zip(tt_, xa)]
lags, c, *_ = new_ax().acorr(xf, maxlags=4, detrend=matplotlib.mlab.detrend_linear)
report("acorr(detrend=mlab.detrend_linear): autocorrelation of the least-squares residual (exact)",
       allclose(c, [float(t / sum(u * u for u in xl)) for t in xc_true(xl, xl, range(-4, 5))], 1e-12))
lags, c, *_ = new_ax().acorr(xf, maxlags=5, usevlines=False)
report("acorr(usevlines=False): same numbers", allclose(c, [float(t / sum(u * u for u in xa)) for t in xc_true(xa, xa, range(-5, 6))], 1e-13))
zc = [complex(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(12)]
lags, c, *_ = new_ax().xcorr(zc, zc, maxlags=3, usevlines=False, normed=False)
report("xcorr(complex, normed=False): sum_n x[n+k] conj(y[n]) (docstring formula)", allclose(np.real(c), [t.real for t in xc_true(zc, zc, range(-3, 4))], 1e-14)
       and allclose(np.imag(c), [t.imag for t in xc_true(zc, zc, range(-3, 4))], 1e-14))
lags, c, *_ = new_ax().xcorr(zc, zc, maxlags=3, usevlines=False)
e2 = sum(abs(t) ** 2 for t in zc); tr = [t / e2 for t in xc_true(zc, zc, range(-3, 4))]
report("acorr-by-xcorr(complex, normed=True): zero-lag value 1 ('normalised to unit length' = divide by ||x|| ||y||)",
       close(np.real(c[3]), 1, 1e-14) and close(np.imag(c[3]), 0, 0, 1e-14), f"c[0 lag] = {complex(c[3])!r}, |x|^2 = {e2}")
sig16 = np.array([int(20000 * math.sin(0.3 * i)) for i in range(40)], np.int16)
sf = [F(int(t)) for t in sig16]
try:
    lags, c, *_ = new_ax().acorr(sig16, maxlags=3)
    tr = [float(t / sum(u * u for u in sf)) for t in xc_true(sf, sf, range(-3, 4))]
    report("acorr(int16 samples, e.g. audio): equals the float result (zero lag 1)", allclose(c, tr, 1e-12), f"{np.asarray(c)[:4]} vs {tr[:4]}")
except Exception as e_:
    report("acorr(int16 samples, e.g. audio): equals the float result (zero lag 1)", False, f"raises {type(e_).__name__}: {str(e_)[:80]}")
try:
    lags, c, *_ = new_ax().acorr(sig16, maxlags=3, normed=False)
    tr = [float(t) for t in xc_true(sf, sf, range(-3, 4))]
    report("acorr(int16 samples, normed=False): exact sums of products", allclose(c, tr, 1e-12), f"{np.asarray(c)[:4]} vs {tr[:4]}")
except Exception as e_:
    report("acorr(int16 samples, normed=False): exact sums of products", False, f"raises {type(e_).__name__}")
ai = [F(t) for t in [3, 1, 4, 1, 5, 9, 2, 6]]
try:
    lags, c, *_ = new_ax().acorr(np.array([3, 1, 4, 1, 5, 9, 2, 6]), maxlags=3)
    report("acorr(int64 array of small values, normed=True default): exact normalised sums", allclose(c, [float(t / sum(u * u for u in ai)) for t in xc_true(ai, ai, range(-3, 4))], 1e-14))
except Exception as e_:
    report("acorr(int64 array of small values, normed=True default): exact normalised sums", False, f"raises {type(e_).__name__}: {str(e_)[:90]}")
lags, c, *_ = new_ax().acorr([3, 1, 4, 1, 5, 9, 2, 6], maxlags=3, normed=False)
report("acorr(list of ints, normed=False): exact sums", allclose(c, [float(t) for t in xc_true(ai, ai, range(-3, 4))], 0, 0))

# ------------------------------------------------------------------ stackplot
print("#### Axes.stackplot baselines")
xs_ = list(range(7))
layers = [[1, 1, 2, 3, 3, 2, 1], [1, 2, 3, 5, 4, 2, 2], [2, 1, 1, 1, 2, 4, 6]]
L = [[F(v) for v in r] for r in layers]
def baseline_of(colls):
    v = colls[0].get_paths()[0].vertices
    out = []
    for xv in xs_:
        ys = [p[1] for p in v if p[0] == xv]
        out.append(min(ys))
    return out
def tops_of(colls):
    out = []
    for cl in colls:
        v = cl.get_paths()[0].vertices
        out.append([max(p[1] for p in v if p[0] == xv) for xv in xs_])
    return out
flayers = [[float(v) for v in r] for r in layers]
for bl in ("zero", "sym", "wiggle", "weighted_wiggle"):
    colls = new_ax().stackplot(xs_, *flayers, baseline=bl)
    g0 = baseline_of(colls); tp = tops_of(colls)
    report(f"stackplot(baseline='{bl}'): layer k spans [g0 + sum_<k, g0 + sum_<=k] (thicknesses preserved)",
           all(close(tp[k][i] - (g0[i] + float(sum(L[j][i] for j in range(k + 1)))), 0, 0, 1e-12) for k in range(3) for i in range(7)))
    if bl == "zero":
        report("stackplot('zero'): 'Constant zero baseline'", allclose(g0, [0] * 7, 0, 0))
    elif bl == "sym":
        report("stackplot('sym'): 'Symmetric around zero' -> g0 = -sum(f)/2 (ThemeRiver)", allclose(g0, [float(-sum(L[j][i] for j in range(3)) / 2) for i in range(7)], 1e-14))
    elif bl == "wiggle":
        m_ = 3
        mid = [float(-sum((m_ - j - F(1, 2)) * L[j][i] for j in range(3)) / m_) for i in range(7)]
        bw = [float(-sum((m_ - j) * L[j][i] for j in range(3)) / (m_ + 1)) for i in range(7)]
        report("stackplot('wiggle'): 'Minimizes the sum of the squared slopes' of the layer midlines -> g0 = -(1/m) sum_i (m - i - 1/2) f_i",
               allclose(g0, mid, 1e-13), f"{g0[:3]}")
        info(f"Byron & Wattenberg's boundary-curve wiggle -1/(n+1) sum (n-i+1) f_i would give {bw[:4]} (vs {g0[:4]}); the docstring does not say which curves")
    else:
        # minimise sum_i w_i (slope of midline i)^2 per step, weights = layer thickness at the current x
        tru = [g0[0]]; ok0 = close(g0[0], float(-sum(L[j][0] for j in range(3)) / 2), 1e-14)
        mirror = [g0[0]]
        for i in range(1, 7):
            T = sum(L[j][i] for j in range(3)); d = [L[j][i] - L[j][i - 1] for j in range(3)]
            num = sum(L[k][i] * (sum(d[j] for j in range(k)) + d[k] / 2) for k in range(3))
            tru.append(tru[-1] - float(num / T))
            numr = sum(L[k][i] * (sum(d[j] for j in range(k + 1, 3)) + d[k] / 2) for k in range(3))
            mirror.append(mirror[-1] - float(numr / T))
        def obj(g):
            s = 0.0
            for i in range(1, 7):
                dg = g[i] - g[i - 1]
                for k in range(3):
                    sl = dg + float(sum(L[j][i] - L[j][i - 1] for j in range(k))) + float(L[k][i] - L[k][i - 1]) / 2
                    s += float(L[k][i]) * sl * sl
            return s
        info(f"weighted_wiggle g0 {['%.4f' % v for v in g0]}")
        info(f"minimiser of sum_i f_i (midline slope_i)^2 {['%.4f' % v for v in tru]} ; same objective with the layer order reversed {['%.4f' % v for v in mirror]}")
        info(f"weighted squared midline slopes: matplotlib {obj(g0):.4f}, minimiser {obj(tru):.4f}")
        report("stackplot('weighted_wiggle', float layers): 'Does the same but weights to account for size of each layer' (Byron & Wattenberg) -> minimises sum_i f_i * (midline slope_i)^2",
               ok0 and allclose(g0, tru, 1e-12), f"matplotlib {g0[1]:.4f} at x=1 vs {tru[1]:.4f}; equals the reversed-order minimiser: {allclose(g0, mirror, 1e-12)}")
        g0f = g0
colls = new_ax().stackplot(xs_, *layers, baseline="weighted_wiggle")
g0i = baseline_of(colls)
info(f"weighted_wiggle with the same layers as int64: {['%.4f' % v for v in g0i]}")
report("stackplot('weighted_wiggle', integer layers): same baseline as the same values given as floats",
       allclose(g0i, g0f, 1e-12), f"{g0i[:4]} vs {g0f[:4]}")
for bl in ("sym", "wiggle"):
    a1 = baseline_of(new_ax().stackplot(xs_, *layers, baseline=bl)); a2 = baseline_of(new_ax().stackplot(xs_, *flayers, baseline=bl))
    report(f"stackplot('{bl}', integer layers): same baseline as floats", allclose(a1, a2, 1e-14))
c32 = new_ax().stackplot(xs_, *np.array(flayers, np.float32), baseline="weighted_wiggle")
report("stackplot('weighted_wiggle', float32 layers): same baseline as float64 (to float32 precision)", allclose(baseline_of(c32), g0f, 1e-6, 1e-6))
colls = new_ax().stackplot(xs_, [[0] * 7, [0] * 7], baseline="weighted_wiggle")
report("stackplot('weighted_wiggle') with all-zero layers: finite baseline (no division by zero)", all(np.isfinite(baseline_of(colls))))

# ------------------------------------------------------------------ pie
print("#### Axes.pie")
def pie_parts(ax, *a, **k):
    ax.pie(*a, **k)
    wedges = [p for p in ax.patches if isinstance(p, Wedge)]
    texts = [t.get_text() for t in ax.texts if t.get_text() != ""]
    return wedges, texts
for vals_ in ([1, 2, 3], [0.1, 0.2, 0.3], [7, 0, 13, 0.5], [5], [1e-3, 2e-3, 1]):
    ax = new_ax(); wd, tx = pie_parts(ax, vals_, autopct="%.9f")
    S = sum(fr(v) for v in vals_)
    pct = [100 * fr(v) / S for v in vals_]
    report(f"pie({vals_}, autopct='%.9f'): labels = fmt % (100 * x / sum(x)) ('fractional area x/sum(x)')",
           [float(t) for t in tx] == [float(f"{float(p):.9f}") for p in pct], f"{tx}")
    report(f"pie({vals_}): percentages sum to 100 (to label rounding), wedge spans 360 * x/sum(x) degrees",
           close(sum(float(t) for t in tx), 100, 1e-8) and allclose([w.theta2 - w.theta1 for w in wd], [float(p) * 3.6 for p in pct], 1e-12, 1e-11))
ax = new_ax(); wd, tx = pie_parts(ax, [1, 2, 3, 7, 0.25], autopct="%.12f")
pct = [100 * F(v) / F(13.25) for v in [1, 2, 3, 7, 0.25]]
report("pie([1, 2, 3, 7, 0.25]): autopct percentages within float32 precision (rel 1e-6) of 100 x/sum(x)", allclose([float(t) for t in tx], [float(p) for p in pct], 1e-6),
       f"max rel err {max(abs(float(t) - float(p)) / float(p) for t, p in zip(tx, pct)):.2g}")
ax = new_ax(); wd, tx = pie_parts(ax, [0.1, 0.2, 0.3], autopct="%.6f", normalize=False)
report("pie([0.1, 0.2, 0.3], normalize=False): partial pie, wedges span 36, 72, 108 degrees, labels 10, 20, 30 (sum 60)",
       allclose([w.theta2 - w.theta1 for w in wd], [36, 72, 108], 1e-12) and [float(t) for t in tx] == [10, 20, 30], f"{tx}")
r = raises(lambda: new_ax().pie([0.5, 0.6], normalize=False))
report("pie(sum > 1, normalize=False): ValueError", (r or "").startswith("ValueError"), str(r))
ax = new_ax(); wd, tx = pie_parts(ax, [0.5, 0.5], autopct="%.3f", normalize=False)
report("pie(sum == 1, normalize=False): full pie", allclose([w.theta2 - w.theta1 for w in wd], [180, 180], 1e-12))
seen = []
ax = new_ax(); pie_parts(ax, [2, 3, 5], autopct=lambda p: (seen.append(p), "")[1])
report("pie(autopct=callable): called with 100 * x/sum(x)", allclose(seen, [20, 30, 50], 1e-14), f"{seen}")
ax = new_ax(); wd, _ = pie_parts(ax, [1, 1, 2], startangle=90)
report("pie(startangle=90): first wedge 90 -> 180, counterclockwise", close(wd[0].theta1, 90, 1e-12) and close(wd[0].theta2, 180, 1e-12) and close(wd[2].theta2, 450, 1e-12),
       f"{[(w.theta1, w.theta2) for w in wd]}")
ax = new_ax(); wd, _ = pie_parts(ax, [1, 1, 2], counterclock=False)
report("pie(counterclock=False): wedges run clockwise from 0 (spans 90, 90, 180)",
       allclose(sorted([w.theta2 - w.theta1 for w in wd]), [90, 90, 180], 1e-12) and close(max(wd[0].theta1, wd[0].theta2) % 360, 0, 0, 1e-9), f"{[(w.theta1, w.theta2) for w in wd]}")
for bad in ([1, -1], [0, 0], [1, float("nan")]):
    r = raises(lambda: new_ax().pie(bad))
    info(f"pie({bad}) -> {r}")
r = raises(lambda: new_ax().pie([1, -1]))
report("pie(negative value): ValueError", (r or "").startswith("ValueError"), str(r))
if "wedge_labels" in inspect.signature(matplotlib.axes.Axes.pie).parameters:
    ax = new_ax(); ax.pie([1, 2, 5], wedge_labels="{frac:.4%}|{absval:d}")
    tx = [t.get_text() for t in ax.texts if t.get_text()]
    report("pie(wedge_labels='{frac:.4%}|{absval:d}') (3.12+): frac = x/sum(x), absval = x", tx == ["12.5000%|1", "25.0000%|2", "62.5000%|5"], f"{tx}")

# ------------------------------------------------------------------ errorbar
print("#### Axes.errorbar")
def segs_of(cont):
    """Bar segments per LineCollection; a collection is vertical (yerr) if any of its
    segments has x0 == x1 and y0 != y1, horizontal otherwise. Degenerate segments
    (lolims and uplims both set) follow their collection."""
    out = {"v": [], "h": []}
    for lc in cont.lines[2]:
        sg = [np.asarray(t) for t in lc.get_segments() if len(t) >= 2]
        vert = any(t[0][0] == t[-1][0] and t[0][1] != t[-1][1] for t in sg)
        for t in sg:
            (x0, y0), (x1, y1) = t[0], t[-1]
            if vert: out["v"].append((x0, min(y0, y1), max(y0, y1)) if not (np.isnan(y0) or np.isnan(y1)) else (x0, y0, y1))
            else: out["h"].append((y0, min(x0, x1), max(x0, x1)) if not (np.isnan(x0) or np.isnan(x1)) else (y0, x0, x1))
    return out
ex_ = [0., 1, 2, 3, 4]; ey_ = [1., 3, 2, 5, 4]
ye1 = [0.5, 0.25, 1, 2, 0.1]
s = segs_of(new_ax().errorbar(ex_, ey_, yerr=ye1))
report("errorbar(yerr=shape(N)): vertical bar i from y-e to y+e", sorted(s["v"]) == sorted((ex_[i], ey_[i] - ye1[i], ey_[i] + ye1[i]) for i in range(5)), f"{s['v'][:2]}")
lo_e = [0.5, 0.25, 1, 2, 0]; hi_e = [1, 0.75, 0, 3, 0.125]
s = segs_of(new_ax().errorbar(ex_, ey_, yerr=[lo_e, hi_e]))
report("errorbar(yerr=shape(2, N)): 'First row contains the lower errors, the second row the upper'",
       sorted(s["v"]) == sorted((ex_[i], ey_[i] - lo_e[i], ey_[i] + hi_e[i]) for i in range(5)))
s = segs_of(new_ax().errorbar(ex_, ey_, xerr=0.25))
report("errorbar(xerr=scalar): horizontal bars x +- 0.25 at y", sorted(s["h"]) == sorted((ey_[i], ex_[i] - 0.25, ex_[i] + 0.25) for i in range(5)))
s = segs_of(new_ax().errorbar(ex_, ey_, xerr=[lo_e, hi_e], yerr=ye1))
report("errorbar(xerr=(2, N), yerr=(N)): both sets of bars", sorted(s["h"]) == sorted((ey_[i], ex_[i] - lo_e[i], ex_[i] + hi_e[i]) for i in range(5))
       and sorted(s["v"]) == sorted((ex_[i], ey_[i] - ye1[i], ey_[i] + ye1[i]) for i in range(5)))
lol = [True, False, True, False, False]; upl = [False, False, True, True, False]
s = segs_of(new_ax().errorbar(ex_, ey_, yerr=[lo_e, hi_e], lolims=lol, uplims=upl))
tr = []
for i in range(5):
    lo2 = ey_[i] if lol[i] else ey_[i] - lo_e[i]; hi2 = ey_[i] if upl[i] else ey_[i] + hi_e[i]
    tr.append((ex_[i], lo2, hi2))
report("errorbar(lolims, uplims): 'lolims True means the y-value is a lower limit ... only an upward-pointing arrow' (bar y..y+upper), uplims bar y-lower..y",
       sorted(s["v"]) == sorted(tr), f"{sorted(s['v'])} vs {sorted(tr)}")
s = segs_of(new_ax().errorbar(ex_, ey_, xerr=[lo_e, hi_e], xlolims=lol, xuplims=upl))
tr = []
for i in range(5):
    lo2 = ex_[i] if lol[i] else ex_[i] - lo_e[i]; hi2 = ex_[i] if upl[i] else ex_[i] + hi_e[i]
    tr.append((ey_[i], lo2, hi2))
report("errorbar(xlolims, xuplims): horizontal bars x..x+upper / x-lower..x", sorted(s["h"]) == sorted(tr), f"{sorted(s['h'])}")
s = segs_of(new_ax().errorbar(ex_, ey_, yerr=[0.5, float("nan"), 1, 2, 0.1]))
fin = [t for t in s["v"] if not (np.isnan(t[1]) or np.isnan(t[2]))]
report("errorbar(yerr with NaN): 'Use NaN if you want to skip a value' -> 4 finite bars, the NaN one not drawn",
       sorted(fin) == sorted((ex_[i], ey_[i] - e, ey_[i] + e) for i, e in enumerate([0.5, None, 1, 2, 0.1]) if e is not None), f"{len(fin)} finite")
s = segs_of(new_ax().errorbar(ex_, ey_, yerr=ye1, errorevery=2))
report("errorbar(errorevery=2): bars on points 0, 2, 4 only", sorted(s["v"]) == sorted((ex_[i], ey_[i] - ye1[i], ey_[i] + ye1[i]) for i in (0, 2, 4)))
r = raises(lambda: new_ax().errorbar(ex_, ey_, yerr=[-1, 1, 1, 1, 1]))
if "All values must be >= 0" in matplotlib.axes.Axes.errorbar.__doc__:
    report("errorbar(negative yerr): ValueError ('All values must be >= 0')", (r or "").startswith("ValueError"), str(r))
else:
    info(f"errorbar(negative yerr) -> {r} (this build's docstring states no sign constraint)")
cont = new_ax().errorbar(ex_, ey_, yerr=ye1, capsize=3)
caps = sorted(np.concatenate([l.get_ydata() for l in cont.lines[1]]).tolist())
report("errorbar(capsize=3): cap markers at y-e and y+e", allclose(caps, sorted([ey_[i] - ye1[i] for i in range(5)] + [ey_[i] + ye1[i] for i in range(5)]), 1e-15))

plt.close("all")
