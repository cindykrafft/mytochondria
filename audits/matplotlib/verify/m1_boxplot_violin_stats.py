#!/usr/bin/env python
"""Statistics behind box plots and violin plots: cbook.boxplot_stats, Axes.boxplot / bxp
(drawn line data), cbook.violin_stats, mlab.GaussianKDE, Axes.violinplot / violin (drawn
LineCollections and body polygons).

Truths: fractions.Fraction for means, H&F type-7 percentiles (numpy's default 'linear',
which is what the docstrings' '25th percentile' resolves to), IQR, fences, whiskers and
fliers ported from the documented rule, the notch formula med +- 1.57*IQR/sqrt(N)
(documented), the bootstrap percentile CI of the median (ported, using the same numpy
global-RNG draw so the resamples coincide), sample variances (ddof=1) for the KDE
covariance, the Scott / Silverman factors n**(-1/(d+4)) and (n*(d+2)/4)**(-1/(d+4)), the
KDE as a direct math.fsum of Gaussian kernels, linspace grids as min + k*(max-min)/(P-1).
SciPy's gaussian_kde is used only as an informational cross-check where installed.

Version awareness (release notes):
  3.9  "Boxplots now ignore masked data points" (api_changes_3.9.0/behaviour.rst)
  3.9  violin side= ('low'/'high'); 3.10 orientation=; 3.9 tick_labels=
  3.11 "Axes.violinplot and cbook.violin_stats ignore non-finite values ... now ignore
       masked and non-finite (NaN and inf) values" (api_changes_3.11.0/behavior.rst)
  3.11 violin_stats method=("GaussianKDE", bw_method) tuple form and default."""
import math, random, inspect, warnings
from fractions import Fraction as F
from _synth import *
import matplotlib.pyplot as plt
from matplotlib import cbook, mlab

warnings.filterwarnings("ignore")
V = mpl_version()
def info(s): print("   " + s)
def raises(fn):
    try: fn()
    except Exception as e: return type(e).__name__ + ": " + str(e)[:100]
    return None

# ------------------------------------------------------------------ exact truths
def segs(coll): return [np.asarray(s, float) for s in coll.get_segments()]
def fr(v): return F(float(v))
def q7(vals, pct):
    """Hyndman & Fan type 7 on the exact values; pct a percent in [0, 100]."""
    s = sorted(fr(v) for v in vals); n = len(s)
    h = (n - 1) * F(pct) / 100; j = math.floor(h); g = h - j
    if j >= n - 1: return s[-1]
    return s[j] + g * (s[j + 1] - s[j])
def mean_x(vals): return sum((fr(v) for v in vals), F(0)) / len(vals)
def var_x(vals, ddof=1):
    m = mean_x(vals); return sum(((fr(v) - m) ** 2 for v in vals), F(0)) / (len(vals) - ddof)

def box_truth(vals, whis=1.5):
    """Port of the documentation: quartiles = 25/50/75th percentiles (H&F-7), IQR = Q3-Q1,
    whiskers = most extreme data 'lying within whis*IQR from the box' (inclusive fences),
    fliers = 'data beyond the whiskers', notch = med +- 1.57*IQR/sqrt(N)."""
    q1, med, q3 = q7(vals, 25), q7(vals, 50), q7(vals, 75); iqr = q3 - q1
    xs = [fr(v) for v in vals]
    if isinstance(whis, tuple):
        lo, hi = q7(vals, whis[0]), q7(vals, whis[1])
    elif math.isinf(whis):
        lo, hi = None, None
    else:
        w = fr(whis); lo, hi = q1 - w * iqr, q3 + w * iqr
    inside = [v for v in xs if (lo is None or v >= lo) and (hi is None or v <= hi)]
    whislo, whishi = min(inside), max(inside)
    fl = sorted(v for v in xs if v < whislo or v > whishi)
    n = len(vals); half = F(157, 100) * iqr
    return dict(mean=mean_x(vals), q1=q1, med=med, q3=q3, iqr=iqr, whislo=whislo, whishi=whishi,
                fliers=fl, cilo=float(med) - float(half) / math.sqrt(n), cihi=float(med) + float(half) / math.sqrt(n))

KEYS = ["mean", "q1", "med", "q3", "iqr", "whislo", "whishi", "cilo", "cihi"]
def cmp_stats(name, got, t, rel=1e-12, abs_=1e-12, keys=KEYS):
    bad = [k for k in keys if not close(got[k], float(t[k]), rel, abs_)]
    report(f"{name}: mean/q1/med/q3/iqr/whislo/whishi/cilo/cihi = documented definitions (H&F-7 quartiles, inclusive 1.5*IQR fences, med+-1.57*IQR/sqrt(N))",
           not bad, "mismatch " + ", ".join(f"{k}: {float(got[k])!r} vs {float(t[k])!r}" for k in bad))
    info(f"{name}: q1={float(got['q1'])!r} med={float(got['med'])!r} q3={float(got['q3'])!r} whis=[{float(got['whislo'])!r}, {float(got['whishi'])!r}] "
         f"notch=[{float(got['cilo'])!r}, {float(got['cihi'])!r}] fliers={sorted(np.asarray(got['fliers'], float).tolist())}")
    gf = sorted(np.asarray(got["fliers"], float).tolist()); tf = [float(v) for v in t["fliers"]]
    report(f"{name}: fliers are exactly the data beyond the whiskers ('Beyond the whiskers, data are considered outliers')",
           len(gf) == len(tf) and allclose(gf, tf, rel, abs_), f"{gf} vs {tf}")

banner()
rng = random.Random(20261001)

# ================================================================== boxplot_stats core
print("#### boxplot_stats: quartiles, IQR, whiskers, fliers, notch on odd / even / ties / n=1 / n=2 / negative / int / float32 / offset")
D = {
    "odd n=7 with ties and negatives": [3.5, -1.25, 7, 2, 2, 9.75, 0.5],
    "even n=8 with outlier": [10, 1, 4, 4, 6, 2, 8, 30],
    "n=1": [4.25],
    "n=2": [1.0, 3.0],
    "n=3": [2.0, -7.0, 11.0],
    "negative values, both-side outliers": [-100, -3, -2.5, -2, -1, -1, 0, 50],
    "random n=101 normal + 3 outliers": [rng.gauss(0, 1) for _ in range(101)] + [9.0, -8.5, 12.25],
    "large offset 1e9 + small spread": [1e9 + rng.uniform(-1, 1) for _ in range(40)] + [1e9 + 25.0],
}
for name, vals in D.items():
    got = cbook.boxplot_stats(np.array(vals, float))[0]
    cmp_stats(name, got, box_truth(vals))

xi = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], dtype=int)
got = cbook.boxplot_stats(xi)[0]
cmp_stats("integer input int64 n=11", got, box_truth(xi.tolist()))
report("integer input: quartiles returned as floating values (2.5 is not truncated)", close(got["q1"], 2.5) and np.asarray(got["q1"]).dtype.kind == "f",
       f"q1={got['q1']!r}")
x32 = np.array([rng.gauss(3, 2) for _ in range(57)] + [25.0], dtype=np.float32)
got = cbook.boxplot_stats(x32)[0]
cmp_stats("float32 input n=58 (truth on the exact float32 values)", got, box_truth(x32.tolist()), rel=2e-6, abs_=2e-6)
report("float32 input: whislo / whishi are actual data values (exact, no float32 round-trip error)",
       float(got["whislo"]) in x32.astype(float).tolist() and float(got["whishi"]) in x32.astype(float).tolist())
info("dtypes returned for float32 input: " + ", ".join(f"{k}:{np.asarray(got[k]).dtype}" for k in ("mean", "q1", "cilo", "whishi")))

# Tukey hinges vs H&F-7 (informational: the docstrings say only '25th percentile')
v8 = list(range(1, 9)); info(f"n=8 [1..8]: boxplot_stats q1={float(cbook.boxplot_stats(np.array(v8, float))[0]['q1'])} "
                             f"(H&F-7 {float(q7(v8, 25))}; Tukey's lower hinge would be 2.5)")

# ================================================================== whisker rule, edge wording
print("#### whisker rule at the fences, the Q3 clamp, whis options")
fence = [-2.0, 1.0, 2.0, 3.0, 6.0]   # Q1=1, Q3=3, IQR=2, fences exactly -2 and 6
got = cbook.boxplot_stats(np.array(fence))[0]
report("datum exactly on the upper fence: 'the upper whisker at the highest datum below Q3 + whis*(Q3-Q1)' (strict 'below' -> whishi=3, 6 a flier)",
       close(got["whishi"], 3.0) and 6.0 in np.asarray(got["fliers"]).tolist(), f"whishi={float(got['whishi'])!r} fliers={np.asarray(got['fliers']).tolist()}")
report("datum exactly on the lower fence: 'the lower whisker is at the lowest datum above Q1 - whis*(Q3-Q1)' (strict 'above' -> whislo=1, -2 a flier)",
       close(got["whislo"], 1.0) and -2.0 in np.asarray(got["fliers"]).tolist(), f"whislo={float(got['whislo'])!r}")
report("same data, Axes.boxplot wording 'farthest data point lying within 1.5x the IQR from the box' (inclusive -> whiskers -2 and 6, no fliers)",
       close(got["whislo"], -2.0) and close(got["whishi"], 6.0) and len(got["fliers"]) == 0)

clamp = [0, 0, 0, 0, 0, 0, 10, 10.0]  # Q1=0, Q3=2.5, IQR=2.5, upper fence 6.25; highest datum <= 6.25 is 0 < Q3
got = cbook.boxplot_stats(np.array(clamp))[0]
report("upper whisker is a datum: 'the upper whisker at the highest datum below Q3 + whis*(Q3-Q1)' ([0]*6+[10,10]: highest datum <= 6.25 is 0)",
       close(got["whishi"], 0.0), f"whishi={float(got['whishi'])!r} (Q3={float(got['q3'])!r}); fliers={np.asarray(got['fliers']).tolist()}")
report("same data: fliers are the two 10s", sorted(np.asarray(got["fliers"]).tolist()) == [10.0, 10.0])

for w in (0.25, 3.0, 5.0):
    vals = D["even n=8 with outlier"]
    cmp_stats(f"whis={w} (float: fences Q1/Q3 -+ whis*IQR)", cbook.boxplot_stats(np.array(vals, float), whis=w)[0], box_truth(vals, w))
vals = D["random n=101 normal + 3 outliers"]
cmp_stats("whis=inf (np.isreal path; fences at +-inf -> min/max, no fliers)", cbook.boxplot_stats(np.array(vals), whis=np.inf)[0], box_truth(vals, float("inf")))
r = raises(lambda: cbook.boxplot_stats(np.array(vals), whis="range"))
info(f"whis='range' (removed string option): {r or 'accepted'}")
report("whis='range' is rejected (string option not documented on this build)", r is not None, str(r))

v20 = [float(k) for k in range(1, 21)]
got = cbook.boxplot_stats(np.array(v20), whis=(0, 100))[0]
report("whis=(0, 100): 'whiskers covering the whole range of the data' (1 and 20, no fliers)",
       close(got["whislo"], 1) and close(got["whishi"], 20) and len(got["fliers"]) == 0, f"{float(got['whislo'])}, {float(got['whishi'])}")
got = cbook.boxplot_stats(np.array(v20), whis=(5, 95))[0]
p5, p95 = q7(v20, 5), q7(v20, 95)
report("whis=(5, 95) on 1..20: 'they indicate the percentiles at which to draw the whiskers' (whiskers at P5=1.95, P95=19.05)",
       close(got["whislo"], float(p5)) and close(got["whishi"], float(p95)), f"whiskers {float(got['whislo'])!r}, {float(got['whishi'])!r} vs {float(p5)}, {float(p95)}")
report("whis=(5, 95) on 1..20: whiskers at the most extreme data inside [P5, P95] (2 and 19); fliers 1 and 20",
       close(got["whislo"], 2) and close(got["whishi"], 19) and sorted(np.asarray(got["fliers"]).tolist()) == [1.0, 20.0])
vals = D["random n=101 normal + 3 outliers"]
for wp in ((10, 90), (2.5, 97.5)):
    got = cbook.boxplot_stats(np.array(vals), whis=wp)[0]; t = box_truth(vals, wp)
    report(f"whis={wp}: whiskers are the most extreme data inside [P{wp[0]}, P{wp[1]}], fliers outside them",
           close(got["whislo"], float(t["whislo"])) and close(got["whishi"], float(t["whishi"])) and
           allclose(sorted(np.asarray(got["fliers"]).tolist()), [float(v) for v in t["fliers"]]))

# ================================================================== autorange
print("#### autorange when Q1 == Q3")
ties = [5.0] * 6 + [1.0, 9.0]
got = cbook.boxplot_stats(np.array(ties))[0]
report("ties [5]*6+[1,9], autorange=False: Q1=Q3=5, IQR=0, whiskers 5/5, fliers 1 and 9",
       close(got["q1"], 5) and close(got["q3"], 5) and close(got["iqr"], 0) and close(got["whislo"], 5) and close(got["whishi"], 5)
       and sorted(np.asarray(got["fliers"]).tolist()) == [1.0, 9.0], f"{got}")
got = cbook.boxplot_stats(np.array(ties), autorange=True)[0]
report("autorange=True: 'whis is set to (0, 100) such that the whisker ends are at the minimum and maximum' (1 and 9, no fliers)",
       close(got["whislo"], 1) and close(got["whishi"], 9) and len(got["fliers"]) == 0, f"{float(got['whislo'])}, {float(got['whishi'])}")
got = cbook.boxplot_stats([np.array(ties), np.array(D["even n=8 with outlier"], float)], autorange=True)
report("autorange=True with two datasets: only the IQR==0 one is reset; the other keeps whis=1.5 (30 still a flier)",
       close(got[1]["whishi"], 10) and np.asarray(got[1]["fliers"]).tolist() == [30.0], f"{float(got[1]['whishi'])}")

# ================================================================== notch / bootstrap
print("#### notch: med +- 1.57*IQR/sqrt(N); bootstrap percentile CI of the median")
for n in (5, 16, 401):
    vals = [rng.gauss(10, 3) for _ in range(n)]
    got = cbook.boxplot_stats(np.array(vals))[0]; t = box_truth(vals)
    report(f"n={n}: cilo/cihi = med -+ 1.57*IQR/sqrt(N) (documented Notes formula)", close(got["cilo"], t["cilo"]) and close(got["cihi"], t["cihi"]),
           f"[{got['cilo']!r}, {got['cihi']!r}] vs [{t['cilo']!r}, {t['cihi']!r}]")

def boot_truth(vals, N, seed):
    """Percentile bootstrap of the median: N resamples of size M with replacement, 2.5th and
    97.5th percentiles (H&F-7) of the resampled medians.  The resample indices are drawn with
    the numpy global RNG exactly as the documented 'bootstrapped' procedure would do it."""
    np.random.seed(seed); M = len(vals)
    idx = np.random.randint(M, size=(N, M))
    xs = [fr(v) for v in vals]
    meds = [q7([xs[i] for i in row], 50) for row in idx.tolist()]
    return q7(meds, F(5, 2)), q7(meds, F(195, 2)), meds
vals = [round(rng.gauss(0, 1), 3) for _ in range(25)]
for N, seed in ((500, 1), (2000, 77)):
    lo, hi, meds = boot_truth(vals, N, seed)
    np.random.seed(seed); got = cbook.boxplot_stats(np.array(vals), bootstrap=N)[0]
    report(f"bootstrap={N} (seed {seed}): cilo/cihi = 2.5th/97.5th percentiles of {N} resampled medians ('95% confidence intervals', 'percentile method')",
           close(got["cilo"], float(lo)) and close(got["cihi"], float(hi)), f"[{got['cilo']!r}, {got['cihi']!r}] vs [{float(lo)!r}, {float(hi)!r}]")
np.random.seed(3); a = cbook.boxplot_stats(np.array(vals), bootstrap=300)[0]
np.random.seed(3); b = cbook.boxplot_stats(np.array(vals), bootstrap=300)[0]
report("bootstrap is reproducible under np.random.seed (it draws from the global RNG)", a["cilo"] == b["cilo"] and a["cihi"] == b["cihi"])
np.random.seed(11); st0 = np.random.get_state(); cbook.boxplot_stats(np.array(vals), bootstrap=10); st1 = np.random.get_state()
info(f"bootstrap advances numpy's global RNG state (side effect): {not (np.array_equal(st0[1], st1[1]) and st0[2] == st1[2])}")
got = cbook.boxplot_stats(np.array(vals))[0]
info(f"n=25: asymptotic notch [{got['cilo']:.4f}, {got['cihi']:.4f}]  bootstrap(2000) notch [{float(boot_truth(vals, 2000, 77)[0]):.4f}, {float(boot_truth(vals, 2000, 77)[1]):.4f}]")

# ================================================================== containers, labels, empty, masked, NaN/inf
print("#### multiple datasets, 2D arrays, labels, empty input, masked arrays, NaN / inf")
X = [D["odd n=7 with ties and negatives"], D["even n=8 with outlier"], D["n=1"], D["n=2"]]
got = cbook.boxplot_stats([np.array(v, float) for v in X], labels=["a", "b", "c", "d"])
report("list of 4 datasets of different lengths -> 4 dicts in order", len(got) == 4)
for k, (g, v) in enumerate(zip(got, X)):
    t = box_truth(v)
    report(f"  dataset {k} (n={len(v)}) of the list: stats equal its own documented stats",
           all(close(g[kk], float(t[kk]), 1e-12, 1e-12) for kk in KEYS))
report("labels=['a','b','c','d'] -> stats['label'] per dataset", [g.get("label") for g in got] == ["a", "b", "c", "d"])
r = raises(lambda: cbook.boxplot_stats([np.array(v, float) for v in X], labels=["a", "b"]))
report("labels of the wrong length -> ValueError ('Length must be compatible with dimensions of X')", (r or "").startswith("ValueError"), str(r))
A = np.array([[rng.randint(-50, 50) / 4 for _ in range(3)] for _ in range(9)])
got = cbook.boxplot_stats(A)
report("2D array (9, 3) -> 3 dicts, one per COLUMN, each equal to that column's documented stats",
       len(got) == 3 and all(all(close(g[k], float(box_truth(A[:, j].tolist())[k]), 1e-12, 1e-12) for k in KEYS) for j, g in enumerate(got)))

for name, X0 in (("[]", []), ("np.array([])", np.array([]))):
    got = cbook.boxplot_stats(X0)
    g = got[0]
    report(f"empty input {name}: one dict, every documented key present (incl. 'iqr'), stats NaN, fliers empty",
           len(got) == 1 and all(k in g for k in KEYS + ["fliers"]) and all(np.isnan(g[k]) for k in KEYS if k in g) and len(g["fliers"]) == 0,
           f"keys={sorted(g)}")
got = cbook.boxplot_stats([np.array(D["n=2"]), np.array([])])
report("one empty dataset among two: the other is unaffected, the empty one is all-NaN",
       close(got[0]["med"], 2.0) and np.isnan(got[1]["med"]) and len(got[1]["fliers"]) == 0)

base = D["even n=8 with outlier"]
xm = np.ma.array(base + [1000.0, -1000.0, 7.0], mask=[0] * 8 + [1, 1, 1])
got = cbook.boxplot_stats(xm)[0]
if V >= (3, 9):
    cmp_stats("1D masked array (3 masked, incl. +-1000): 'boxplot_stats now ignore any masked points' (3.9 note)", got, box_truth(base))
    A2 = np.ma.array(np.column_stack([base, base[::-1]]), mask=np.zeros((8, 2), bool)); A2[2, 0] = np.ma.masked; A2[5, 1] = np.ma.masked
    g2 = cbook.boxplot_stats(A2)
    t0 = box_truth([v for k, v in enumerate(base) if k != 2]); t1 = box_truth([v for k, v in enumerate(base[::-1]) if k != 5])
    report("2D masked array: masked cells dropped per column",
           all(close(g2[0][k], float(t0[k])) for k in KEYS) and all(close(g2[1][k], float(t1[k])) for k in KEYS))
    gl = cbook.boxplot_stats([xm, np.ma.array([1.0, 2.0, 99.0], mask=[0, 0, 1])])
    report("list of masked arrays: masked points dropped in each", close(gl[0]["med"], float(box_truth(base)["med"])) and close(gl[1]["med"], 1.5) and close(gl[1]["whishi"], 2.0),
           f"med={gl[1]['med']!r} whishi={gl[1]['whishi']!r}")
else:
    info(f"masked arrays before 3.9 (not ignored; 3.9 note): med={float(got['med'])} (unmasked-only would be {float(box_truth(base)['med'])}); "
         f"fliers={np.asarray(got['fliers']).tolist()}")

g = cbook.boxplot_stats(np.array([1.0, 2, 3, np.nan, 5, 6, 7]))[0]
info("NaN in the data (no documented rule in boxplot_stats/Axes.boxplot): " + ", ".join(f"{k}={float(g[k])!r}" for k in ("mean", "q1", "med", "q3", "whislo", "whishi")) +
     f", fliers={np.asarray(g['fliers']).tolist()}")
vals = [1, 2, 3, 4, 5, 6, 7, 8, math.inf]
g = cbook.boxplot_stats(np.array(vals, float))[0]
report("+inf as the 9th of 9 values (Q3 index 6, not next to inf): Q3=7, IQR=4, whishi=8, +inf a flier",
       close(g["q3"], 7) and close(g["iqr"], 4) and close(g["whishi"], 8) and np.isinf(np.asarray(g["fliers"])).sum() == 1, f"{g}")
vals = [1, 2, 3, 4, math.inf]
g = cbook.boxplot_stats(np.array(vals, float))[0]
report("+inf as the 5th of 5 values: Q3 = 4 (H&F-7 index exactly 3, weight 0 on the inf), whishi = 4, +inf a flier",
       close(g["q3"], 4) and close(g["whishi"], 4) and np.isinf(np.asarray(g["fliers"])).sum() == 1,
       f"q3={float(g['q3'])!r} iqr={float(g['iqr'])!r} whishi={float(g['whishi'])!r} fliers={np.asarray(g['fliers']).tolist()} "
       f"(np.percentile([1,2,3,4,inf],75)={np.percentile(np.array(vals), 75)!r})")

# ================================================================== Axes.boxplot drawn data
print("#### Axes.boxplot / bxp: drawn lines equal the documented statistics")
def hz_kw(): return dict(orientation="horizontal") if V >= (3, 10) else dict(vert=False)
def tl_kw(lbls): return dict(tick_labels=lbls) if V >= (3, 9) else dict(labels=lbls)
X = [D["even n=8 with outlier"], D["odd n=7 with ties and negatives"], xi.tolist()]
T = [box_truth(v) for v in X]
fig, ax = plt.subplots()
res = ax.boxplot([np.array(v) for v in X], showmeans=True, **tl_kw(["e", "o", "i"]))
ok_m = all(allclose(res["medians"][i].get_ydata(), [float(t["med"])] * 2) for i, t in enumerate(T))
ok_b = all(allclose(res["boxes"][i].get_ydata(), [float(t[k]) for k in ("q1", "q1", "q3", "q3", "q1")]) for i, t in enumerate(T))
ok_w = all(allclose(res["whiskers"][2 * i].get_ydata(), [float(t["q1"]), float(t["whislo"])]) and
           allclose(res["whiskers"][2 * i + 1].get_ydata(), [float(t["q3"]), float(t["whishi"])]) for i, t in enumerate(T))
ok_c = all(allclose(res["caps"][2 * i].get_ydata(), [float(t["whislo"])] * 2) and allclose(res["caps"][2 * i + 1].get_ydata(), [float(t["whishi"])] * 2)
           for i, t in enumerate(T))
ok_f = all(allclose(sorted(np.asarray(res["fliers"][i].get_ydata(), float)), [float(v) for v in t["fliers"]]) for i, t in enumerate(T))
ok_fx = all(allclose(res["fliers"][i].get_xdata(), [i + 1] * len(t["fliers"])) for i, t in enumerate(T))
ok_mn = all(allclose(res["means"][i].get_ydata(), [float(t["mean"])]) for i, t in enumerate(T))
ok_pos = all(close(np.mean(res["medians"][i].get_xdata()), i + 1) for i in range(3))
report("medians: y = [med, med] for each box", ok_m)
report("boxes: y = [q1, q1, q3, q3, q1] (box from Q1 to Q3)", ok_b)
report("whiskers: [q1 -> whislo] and [q3 -> whishi]", ok_w)
report("caps at whislo and whishi", ok_c)
report("fliers: drawn y = the data beyond the whiskers", ok_f)
report("fliers drawn at x = box position (default positions 1..N)", ok_fx)
report("showmeans=True: mean marker at y = arithmetic mean", ok_mn)
report("boxes centred on the default positions range(1, N+1)", ok_pos)
plt.close(fig)

fig, ax = plt.subplots()
res = ax.boxplot([np.array(v) for v in X], showmeans=True, meanline=True, notch=True, positions=[2, 5, 9])
ok_n = all(allclose(res["boxes"][i].get_ydata(), [float(t["q1"]), float(t["q1"]), t["cilo"], float(t["med"]), t["cihi"], float(t["q3"]), float(t["q3"]),
                                                  t["cihi"], float(t["med"]), t["cilo"], float(t["q1"])]) for i, t in enumerate(T))
report("notch=True: box outline passes through cilo, med, cihi = med -+ 1.57*IQR/sqrt(N)", ok_n)
report("meanline=True: mean line y = [mean, mean]", all(allclose(res["means"][i].get_ydata(), [float(t["mean"])] * 2) for i, t in enumerate(T)))
report("positions=[2,5,9]: medians centred on the given positions", all(close(np.mean(res["medians"][i].get_xdata()), p) for i, p in enumerate([2, 5, 9])))
report("positions=[2,5,9]: fliers drawn at x = the given position", all(allclose(res["fliers"][i].get_xdata(), [p] * len(T[i]["fliers"])) for i, p in enumerate([2, 5, 9])))
plt.close(fig)

fig, ax = plt.subplots()
res = ax.boxplot([np.array(v) for v in X], notch=True, usermedians=[None, 1.75, None], conf_intervals=[None, None, (2.0, 6.5)])
report("usermedians=[None, 1.75, None]: 'forces the value of the median' of box 2, others computed",
       allclose(res["medians"][1].get_ydata(), [1.75, 1.75]) and allclose(res["medians"][0].get_ydata(), [float(T[0]["med"])] * 2))
yb = res["boxes"][2].get_ydata()
report("conf_intervals=(2.0, 6.5) for box 3: notch drawn at cilo=2.0, cihi=6.5", close(yb[2], 2.0) and close(yb[4], 6.5) and close(yb[7], 6.5) and close(yb[9], 2.0), f"{list(yb)}")
yb1 = res["boxes"][1].get_ydata()
info(f"usermedians box: notch y = cilo {yb1[2]!r}, cihi {yb1[4]!r} (still centred on the computed median {float(T[1]['med'])}, not on 1.75)")
plt.close(fig)

fig, ax = plt.subplots()
res = ax.boxplot([np.array(v) for v in X], **hz_kw())
report("horizontal boxplot: medians / whiskers / fliers carry the statistics on x",
       all(allclose(res["medians"][i].get_xdata(), [float(t["med"])] * 2) and allclose(res["whiskers"][2 * i + 1].get_xdata(), [float(t["q3"]), float(t["whishi"])])
           and allclose(sorted(res["fliers"][i].get_xdata()), [float(v) for v in t["fliers"]]) for i, t in enumerate(T)))
plt.close(fig)

vals = [round(rng.gauss(0, 1), 3) for _ in range(31)]
lo, hi, _ = boot_truth(vals, 1000, 2024)
np.random.seed(2024)
fig, ax = plt.subplots(); res = ax.boxplot(np.array(vals), notch=True, bootstrap=1000)
yb = res["boxes"][0].get_ydata()
report("Axes.boxplot(bootstrap=1000, notch=True): notch at the percentile-bootstrap CI of the median", close(yb[2], float(lo)) and close(yb[4], float(hi)),
       f"[{yb[2]!r}, {yb[4]!r}] vs [{float(lo)!r}, {float(hi)!r}]")
plt.close(fig)
fig, ax = plt.subplots(); res = ax.boxplot(np.array(ties), autorange=True)
report("Axes.boxplot(autorange=True) on Q1==Q3 data: whiskers to min and max, no fliers",
       allclose(res["caps"][0].get_ydata(), [1, 1]) and allclose(res["caps"][1].get_ydata(), [9, 9]) and len(res["fliers"][0].get_ydata()) == 0)
plt.close(fig)
fig, ax = plt.subplots(); res = ax.boxplot(np.array(v20), whis=(0, 100))
report("Axes.boxplot(whis=(0, 100)): whiskers at min and max", allclose(res["caps"][0].get_ydata(), [1, 1]) and allclose(res["caps"][1].get_ydata(), [20, 20]))
plt.close(fig)
if V >= (3, 9):
    fig, ax = plt.subplots(); res = ax.boxplot(xm)
    t = box_truth(base)
    report("Axes.boxplot(masked array): masked points not drawn and not used (3.9 note)",
           allclose(res["medians"][0].get_ydata(), [float(t["med"])] * 2) and allclose(sorted(res["fliers"][0].get_ydata()), [float(v) for v in t["fliers"]]))
    plt.close(fig)

# ================================================================== GaussianKDE
print("#### mlab.GaussianKDE: bandwidth factors, covariance (ddof), evaluation vs a direct sum of Gaussians")
def kde_truth(vals, pts, factor):
    n = len(vals); sd = math.sqrt(float(var_x(vals, 1))); h = factor * sd
    c = 1.0 / (n * h * math.sqrt(2 * math.pi))
    return [c * math.fsum(math.exp(-0.5 * ((t - v) / h) ** 2) for v in vals) for t in pts]

for n in (7, 40, 300):
    vals = [rng.gauss(2, 1.5) for _ in range(n)]
    k = mlab.GaussianKDE(np.array(vals))
    report(f"n={n}, default bw: factor = Scott n**(-1/5)", close(k.factor, n ** (-1 / 5), 1e-14), f"{k.factor!r} vs {n ** (-1 / 5)!r}")
    report(f"n={n}: covariance = sample variance with ddof=1 times factor**2 (as scipy.stats.gaussian_kde)", close(k.covariance[0, 0], float(var_x(vals, 1)) * k.factor ** 2, 1e-12),
           f"{k.covariance[0, 0]!r} vs ddof1 {float(var_x(vals, 1)) * k.factor ** 2!r} / ddof0 {float(var_x(vals, 0)) * k.factor ** 2!r}")
    pts = np.linspace(min(vals) - 2, max(vals) + 2, 100)  # 100 points: n=7,40 loop over data; n=300 loop over points
    got = k.evaluate(pts); t = kde_truth(vals, pts.tolist(), n ** (-1 / 5))
    report(f"n={n}: evaluate(100 points) = (1/(n h sqrt(2 pi))) sum exp(-((t-x_i)/h)^2/2), h = factor*sd ({'data' if 100 >= n else 'points'}-loop branch)",
           allclose(got, t, 1e-10, 1e-300), f"maxrel={max(abs(a - b) / b for a, b in zip(got, t)):.2e}")
    ks = mlab.GaussianKDE(np.array(vals), "silverman")
    fs = (n * 3 / 4) ** (-1 / 5)
    report(f"n={n}, bw_method='silverman': factor = (n*(d+2)/4)**(-1/(d+4)) = (3n/4)**(-1/5)", close(ks.factor, fs, 1e-14), f"{ks.factor!r} vs {fs!r}")
    report(f"n={n}, silverman: evaluate = direct sum with h = factor*sd", allclose(ks.evaluate(pts), kde_truth(vals, pts.tolist(), fs), 1e-10, 1e-300))
    if HAVE_SCIPY:
        from scipy.stats import gaussian_kde
        report(f"n={n}: evaluate equals scipy.stats.gaussian_kde (scott) [scipy, informational]", allclose(got, gaussian_kde(np.array(vals)).evaluate(pts), 1e-9, 1e-300))
    lo_, hi_ = min(vals) - 10 * k.factor * 1.5 * 3, max(vals) + 10 * k.factor * 1.5 * 3
    g = np.linspace(lo_, hi_, 20001); yv = k.evaluate(g)
    area = float(np.sum((yv[1:] + yv[:-1]) * np.diff(g)) / 2)
    report(f"n={n}: the estimated pdf integrates to 1 (trapezoid on a wide fine grid)", close(area, 1.0, 1e-6), f"{area!r}")

vals = [rng.gauss(0, 1) for _ in range(30)]; pts = np.linspace(-4, 4, 50)
for bw in (0.3, 1, 2.5):
    k = mlab.GaussianKDE(np.array(vals), bw)
    report(f"bw_method={bw!r} (scalar): 'used directly as kde.factor'; h = {bw}*sd", close(k.factor, bw) and allclose(k.evaluate(pts), kde_truth(vals, pts.tolist(), bw), 1e-10, 1e-300))
k = mlab.GaussianKDE(np.array(vals), lambda kd: 0.5 * kd.num_dp ** (-1 / 5))
report("bw_method=callable(kde) -> factor = its return value (0.5 * n**(-1/5))", close(k.factor, 0.5 * 30 ** (-1 / 5), 1e-14) and
       allclose(k.evaluate(pts), kde_truth(vals, pts.tolist(), 0.5 * 30 ** (-1 / 5)), 1e-10, 1e-300))
r = raises(lambda: mlab.GaussianKDE(np.array(vals), "scot"))
report("bw_method='scot' (invalid string) -> ValueError", (r or "").startswith("ValueError"), str(r))
x32 = np.array(vals, dtype=np.float32)
k = mlab.GaussianKDE(x32)
report("float32 dataset: evaluate = direct sum on the float32 values (rel 1e-6)", allclose(k.evaluate(pts), kde_truth(x32.tolist(), pts.tolist(), 30 ** (-1 / 5)), 1e-6, 1e-300))
off = [1e6 + v for v in vals]
k = mlab.GaussianKDE(np.array(off)); pp = (1e6 + pts).tolist()
report("offset 1e6 + data: evaluate = direct sum (rel 1e-7; cancellation in x - mean)", allclose(k.evaluate(np.array(pp)), kde_truth(off, pp, 30 ** (-1 / 5)), 1e-7, 1e-300))

# 2-D and 3-D
n2 = 60
xy = [(rng.gauss(0, 1), 0) for _ in range(n2)]; xy = [(a, 0.6 * a + rng.gauss(0, 0.5)) for a, _ in xy]
k = mlab.GaussianKDE(np.array(xy).T)
fac = n2 ** (-1 / 6)
Xs = [fr(a) for a, _ in xy]; Ys = [fr(b) for _, b in xy]; mx = sum(Xs) / n2; my = sum(Ys) / n2
cxx = sum((a - mx) ** 2 for a in Xs) / (n2 - 1); cyy = sum((b - my) ** 2 for b in Ys) / (n2 - 1); cxy = sum((a - mx) * (b - my) for a, b in zip(Xs, Ys)) / (n2 - 1)
report("2-D: factor = Scott n**(-1/(d+4)) with d=2", close(k.factor, fac, 1e-14))
report("2-D: covariance = sample covariance matrix (ddof=1) * factor**2", allclose(k.covariance, [[float(cxx) * fac ** 2, float(cxy) * fac ** 2], [float(cxy) * fac ** 2, float(cyy) * fac ** 2]], 1e-12))
det = cxx * cyy - cxy ** 2; ixx, iyy, ixy = cyy / det, cxx / det, -cxy / det
ptsxy = [(-1.0, -0.5), (0.0, 0.0), (0.7, 1.2), (2.0, 0.3), (-2.5, -1.4)]
tv = []
for (px, py) in ptsxy:
    s = math.fsum(math.exp(-0.5 * (float(ixx) * (px - float(a)) ** 2 + 2 * float(ixy) * (px - float(a)) * (py - float(b)) + float(iyy) * (py - float(b)) ** 2) / fac ** 2) for a, b in zip(Xs, Ys))
    tv.append(s / (n2 * 2 * math.pi * fac ** 2 * math.sqrt(float(det))))
report("2-D: evaluate = direct sum of bivariate Gaussians with covariance factor**2 * Sigma", allclose(k.evaluate(np.array(ptsxy).T), tv, 1e-10, 1e-300))
k3 = mlab.GaussianKDE(np.array([[rng.gauss(0, 1) for _ in range(50)] for _ in range(3)]), "silverman")
report("3-D, silverman: factor = (n*(d+2)/4)**(-1/(d+4)) = (50*5/4)**(-1/7)", close(k3.factor, (50 * 5 / 4) ** (-1 / 7), 1e-14))

r1 = raises(lambda: mlab.GaussianKDE(np.array([3.0])))
r0 = raises(lambda: mlab.GaussianKDE(np.array([2.0, 2.0, 2.0])))
info(f"GaussianKDE(n=1): {r1}")
info(f"GaussianKDE(constant data): {r0}")
info("GaussianKDE signature: " + str(inspect.signature(mlab.GaussianKDE.__init__)) + "  (no weights parameter on this build)")

# ================================================================== violin_stats
print("#### cbook.violin_stats: grid, KDE values, mean / median / min / max / quantiles")
def vstats(X, bw=None, points=100, quantiles=None):
    if V >= (3, 11):
        return cbook.violin_stats(X, ("GaussianKDE", bw), points=points, quantiles=quantiles)
    def m(x, c):
        if np.all(x[0] == x): return (x[0] == c).astype(float)
        return mlab.GaussianKDE(x, bw).evaluate(c)
    return cbook.violin_stats(X, m, points=points, quantiles=quantiles)
def vtruth(vals, bw="scott", points=100, qs=()):
    n = len(vals); mn, mxv = min(fr(v) for v in vals), max(fr(v) for v in vals)
    coords = [float(mn + (mxv - mn) * k / (points - 1)) for k in range(points)]
    fac = n ** (-1 / 5) if bw in (None, "scott") else ((n * 3 / 4) ** (-1 / 5) if bw == "silverman" else bw)
    return dict(coords=coords, vals=kde_truth(vals, coords, fac), mean=mean_x(vals), median=q7(vals, 50), min=mn, max=mxv,
                quantiles=[q7(vals, F(q) * 100) for q in qs])
def cmp_v(name, g, t, rel=1e-10):
    report(f"{name}: coords = linspace(min, max, points)", len(g["coords"]) == len(t["coords"]) and allclose(g["coords"], t["coords"], 1e-12, 1e-12))
    report(f"{name}: vals = Gaussian KDE (direct sum) at coords", allclose(g["vals"], t["vals"], rel, 1e-300),
           f"maxrel={max(abs(a - b) / max(b, 1e-300) for a, b in zip(g['vals'], t['vals'])):.2e}" if len(g["vals"]) == len(t["vals"]) else f"len {len(g['vals'])}")
    report(f"{name}: mean / median / min / max exact", all(close(g[k], float(t[k]), 1e-13, 1e-13) for k in ("mean", "median", "min", "max")),
           ", ".join(f"{k}={float(g[k])!r}/{float(t[k])!r}" for k in ("mean", "median", "min", "max")))
    if t["quantiles"]:
        report(f"{name}: quantiles = H&F-7 percentiles (np.percentile 'linear')", allclose(g["quantiles"], [float(v) for v in t["quantiles"]], 1e-12, 1e-12),
               f"{list(g['quantiles'])} vs {[float(v) for v in t['quantiles']]}")

va = [rng.gauss(5, 2) for _ in range(23)]; vb = [rng.expovariate(1.0) for _ in range(150)]; vc = [1.0, 4.0]
g = vstats([np.array(va), np.array(vb), np.array(vc)], quantiles=[[0.1, 0.5, 0.9], [0.25, 0.75], [0.07]])
for name, gg, vals, qs in (("A n=23", g[0], va, (0.1, 0.5, 0.9)), ("B n=150 (points-loop)", g[1], vb, (0.25, 0.75)), ("C n=2", g[2], vc, (0.07,))):
    cmp_v(name, gg, vtruth(vals, qs=qs))
g = vstats(np.array(va), bw="silverman", points=7)
cmp_v("A, silverman, points=7", g[0], vtruth(va, "silverman", 7))
g = vstats(np.array(va), bw=0.25)
cmp_v("A, bw=0.25", g[0], vtruth(va, 0.25))
xi2 = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
g = vstats(xi2, quantiles=[0.5])
cmp_v("integer input n=11", g[0], vtruth(xi2.tolist(), qs=(0.5,)))
A3 = np.array([[rng.gauss(0, 1) for _ in range(2)] for _ in range(12)])
g = vstats(A3)
report("2D array (12, 2): one violin per column, each column's mean/min/max", len(g) == 2 and all(close(g[j]["mean"], float(mean_x(A3[:, j].tolist()))) and close(g[j]["max"], A3[:, j].max()) for j in range(2)))
if V >= (3, 11):
    g = cbook.violin_stats(np.array(va))
    report("violin_stats default method = ('GaussianKDE', 'scott') (3.11)", allclose(g[0]["vals"], vtruth(va)["vals"], 1e-10, 1e-300))
    g = cbook.violin_stats(np.array(va), ("GaussianKDE", lambda kd: 0.4))
    report("violin_stats method=('GaussianKDE', callable) -> factor from the callable", allclose(g[0]["vals"], vtruth(va, 0.4)["vals"], 1e-10, 1e-300))
    r = raises(lambda: cbook.violin_stats(np.array(va), ("Epanechnikov", "scott")))
    report("violin_stats unknown KDE name -> ValueError", (r or "").startswith("ValueError"), str(r))
g = cbook.violin_stats(np.array(va), lambda d, c: np.full(len(c), float(len(d))), points=5)
report("violin_stats(method=callable(data, coords)): vals are what the callable returns at the 5 coords",
       allclose(g[0]["vals"], [23.0] * 5) and allclose(g[0]["coords"], vtruth(va, points=5)["coords"], 1e-12, 1e-12))

for name, vals in (("constant data [2.5]*6", [2.5] * 6), ("n=1 [7.0]", [7.0])):
    g = vstats(np.array(vals))[0]
    ok = all(close(g[k], vals[0]) for k in ("mean", "median", "min", "max")) and np.all(np.isfinite(g["vals"]))
    report(f"{name}: no exception; mean = median = min = max = the value; vals finite", ok, f"{g['mean']}, {g['min']}, {g['max']}")
    info(f"{name}: coords {np.unique(g['coords'])} vals {np.unique(g['vals'])} (indicator fallback, not a density)")

clean = [rng.gauss(0, 1) for _ in range(40)]
dirty = clean[:20] + [math.nan, math.inf] + clean[20:] + [-math.inf, math.nan]
mk = np.ma.array(clean + [50.0, -50.0, 3.3], mask=[0] * 40 + [1, 1, 1])
if V >= (3, 11):
    g = vstats(np.array(dirty), quantiles=[0.25, 0.75])[0]
    cmp_v("NaN and +-inf in the data ('Non-finite and masked values are ignored', 3.11)", g, vtruth(clean, qs=(0.25, 0.75)))
    g = vstats(mk, quantiles=[0.25, 0.75])[0]
    cmp_v("1D masked array, 3 masked incl. +-50 ('Non-finite and masked values are ignored', 3.11)", g, vtruth(clean, qs=(0.25, 0.75)))
    g = vstats([mk, np.ma.array([1.0, 2.0, 3.0, 99.0], mask=[0, 0, 0, 1])])
    report("list of masked arrays: masked values ignored (max of the 2nd = 3, not 99)", close(g[1]["max"], 3.0) and close(g[0]["max"], max(clean)),
           f"max={g[0]['max']!r}, {g[1]['max']!r}")
    g = vstats([np.array([]), np.array(vc)])
    report("empty dataset among two: NaN stats and empty vals/coords for it, the other unaffected (3.11)",
           np.isnan(g[0]["mean"]) and len(g[0]["vals"]) == 0 and close(g[1]["mean"], 2.5))
    g = vstats(np.array([math.nan, math.nan]))[0]
    report("all-NaN dataset -> treated as empty (NaN stats, no exception)", np.isnan(g["mean"]) and len(g["coords"]) == 0)
else:
    r = raises(lambda: vstats(np.array(dirty)))
    info(f"NaN/inf before 3.11 (not ignored): {r or 'min=' + repr(vstats(np.array(dirty))[0]['min'])}")
    g = vstats(mk, quantiles=[0.25, 0.75])[0]
    info(f"masked array before 3.11: min={float(g['min'])!r} max={float(g['max'])!r} mean={float(g['mean'])!r} median={float(g['median'])!r} "
         f"quantiles={np.asarray(g['quantiles'], float).tolist()} (unmasked-only: {min(clean)!r}, {max(clean)!r}, {float(mean_x(clean))!r}, "
         f"{float(q7(clean, 50))!r}, {[float(q7(clean, 25)), float(q7(clean, 75))]}); vals masked: {int(np.ma.count_masked(g['vals']))}/{len(g['vals'])}")
    fig, ax = plt.subplots(); res = ax.violinplot([mk], showextrema=True, showmeans=True)
    info(f"Axes.violinplot(masked) before 3.11: max line at {segs(res['cmaxes'])[0][0, 1]!r}, mean line at {segs(res['cmeans'])[0][0, 1]!r}"); plt.close(fig)

# ================================================================== Axes.violinplot drawn data
print("#### Axes.violinplot / violin: stat lines and body widths")
data = [np.array(va), np.array(vb), np.array(vc)]; pos = [1.0, 3.0, 4.5]; wid = [0.5, 1.2, 0.8]
qs = [[0.1, 0.5, 0.9], [0.25, 0.75], [0.07]]
T = [vtruth(va, qs=qs[0]), vtruth(vb, qs=qs[1]), vtruth(vc, qs=qs[2])]
fig, ax = plt.subplots()
res = ax.violinplot(data, positions=pos, widths=wid, showmeans=True, showmedians=True, showextrema=True, quantiles=qs)
for key, sk in (("cmeans", "mean"), ("cmedians", "median"), ("cmins", "min"), ("cmaxes", "max")):
    ss = segs(res[key])
    ok = len(ss) == 3 and all(allclose(s[:, 1], [float(t[sk])] * 2, 1e-12, 1e-12) and allclose(s[:, 0], [p - w / 4, p + w / 4]) for s, t, p, w in zip(ss, T, pos, wid))
    report(f"{key}: horizontal segment at y = {sk}, x from pos - widths/4 to pos + widths/4", ok, f"{[s.tolist() for s in ss][:1]}")
ss = segs(res["cbars"])
report("cbars: vertical segment at x = pos from min to max", all(allclose(s[:, 0], [p, p]) and allclose(sorted(s[:, 1]), [float(t["min"]), float(t["max"])], 1e-12, 1e-12) for s, t, p in zip(ss, T, pos)))
ss = segs(res["cquantiles"]); flat = [(float(v), p, w) for t, p, w in zip(T, pos, wid) for v in t["quantiles"]]
report("cquantiles: one segment per requested quantile at its H&F-7 value, widths repeated per violin",
       len(ss) == len(flat) and all(allclose(s[:, 1], [v, v], 1e-12, 1e-12) and allclose(s[:, 0], [p - w / 4, p + w / 4]) for s, (v, p, w) in zip(ss, flat)))

def body_check(body, t, p, w, side="both", horizontal=False):
    vt = np.asarray(body.get_paths()[0].vertices, float)
    if horizontal: vt = vt[:, ::-1]
    f = t["vals"]; fm = max(f); half = [0.5 * w * v / fm for v in f]
    worst = 0.0
    for y, h in zip(t["coords"], half):
        for xexp in ([p - h, p + h] if side == "both" else ([p - h, p] if side == "low" else [p, p + h])):
            d = np.min(np.hypot(vt[:, 0] - xexp, vt[:, 1] - y)); worst = max(worst, d)
    return worst, vt[:, 0].min(), vt[:, 0].max()
for i, (b, t, p, w) in enumerate(zip(res["bodies"], T, pos, wid)):
    worst, xmin, xmax = body_check(b, t, p, w)
    report(f"body {i}: outline at pos -+ 0.5*widths*kde/max(kde) for every coord (KDE truth); max full width = widths={w}",
           worst < 1e-9 and close(xmax - xmin, w, 1e-12), f"worst vertex distance {worst:.2e}, full width {xmax - xmin!r}")
plt.close(fig)

fig, ax = plt.subplots()
res = ax.violinplot([np.array(va)], **hz_kw(), showmeans=True)
worst, _, _ = body_check(res["bodies"][0], T[0], 1.0, 0.5, horizontal=True)
ss = segs(res["cmeans"])
report("horizontal violin: body outline mirrored onto x (coords) / y (density); mean line at x = mean",
       worst < 1e-9 and allclose(ss[0][:, 0], [float(T[0]["mean"])] * 2, 1e-12, 1e-12), f"worst {worst:.2e}")
plt.close(fig)
fig, ax = plt.subplots()
res = ax.violinplot([np.array(va)], bw_method="silverman")
worst, _, _ = body_check(res["bodies"][0], vtruth(va, "silverman"), 1.0, 0.5)
report("violinplot(bw_method='silverman'): body shape from the Silverman-factor KDE", worst < 1e-9, f"worst {worst:.2e}")
plt.close(fig)
fig, ax = plt.subplots()
res = ax.violinplot([np.array(va)], bw_method=0.2, points=31)
worst, _, _ = body_check(res["bodies"][0], vtruth(va, 0.2, 31), 1.0, 0.5)
report("violinplot(bw_method=0.2, points=31): body shape from h = 0.2*sd on a 31-point grid", worst < 1e-9, f"worst {worst:.2e}")
plt.close(fig)
if V >= (3, 9):
    for side in ("low", "high"):
        fig, ax = plt.subplots()
        res = ax.violinplot([np.array(va)], side=side, showmeans=True)
        worst, xmin, xmax = body_check(res["bodies"][0], T[0], 1.0, 0.5, side=side)
        s = segs(res["cmeans"])[0]
        exp_x = [0.875, 1.0] if side == "low" else [1.0, 1.125]
        report(f"side='{side}': half-violin of width widths/2 on the {side} side; mean line from {exp_x[0]} to {exp_x[1]}",
               worst < 1e-9 and close(xmax - xmin, 0.25, 1e-12) and allclose(s[:, 0], exp_x), f"worst {worst:.2e}, x {s[:, 0].tolist()}")
        plt.close(fig)
fig, ax = plt.subplots()
r = raises(lambda: ax.violinplot([np.array([2.5] * 6), np.array([7.0])], showmeans=True, showextrema=True))
report("violinplot of constant data and of n=1: no exception", r is None, str(r))
plt.close(fig)
fig, ax = plt.subplots()
res = ax.violinplot([np.array([2.5] * 6), np.array([7.0])], showmeans=True, showextrema=True)
report("constant / n=1 violins: mean, min and max lines at the value", allclose([s[0, 1] for s in segs(res["cmeans"])], [2.5, 7.0]) and
       allclose([s[0, 1] for s in segs(res["cmins"])], [2.5, 7.0]) and allclose([s[0, 1] for s in segs(res["cmaxes"])], [2.5, 7.0]))
plt.close(fig)
if V >= (3, 11):
    fig, ax = plt.subplots()
    res = ax.violinplot([mk], showextrema=True, showmeans=True)
    report("Axes.violinplot(masked array): 'Non-finite and masked values are ignored' (max line at max of unmasked = %.4f)" % max(clean),
           close(segs(res["cmaxes"])[0][0, 1], max(clean)) and close(segs(res["cmeans"])[0][0, 1], float(mean_x(clean)), 1e-12),
           f"max line at {segs(res['cmaxes'])[0][0, 1]!r}, mean line at {segs(res['cmeans'])[0][0, 1]!r}")
    plt.close(fig)
    fig, ax = plt.subplots()
    res = ax.violinplot([np.array(dirty)], showextrema=True, showmedians=True)
    report("Axes.violinplot with NaN / +-inf: lines at the finite data's min / max / median (3.11)",
           close(segs(res["cmaxes"])[0][0, 1], max(clean)) and close(segs(res["cmins"])[0][0, 1], min(clean)) and close(segs(res["cmedians"])[0][0, 1], float(q7(clean, 50))))
    plt.close(fig)
print("done")
