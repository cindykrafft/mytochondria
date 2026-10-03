"""m3b: stackplot(baseline='weighted_wiggle') against Byron & Wattenberg (2008).

Follow-up to m3_hist_hexbin_counts FAIL 14. Run with the interpreter of the build to test:
    <venv>/bin/python m3b_stackplot_wiggle.py

Truths (all exact, fractions.Fraction):
  * B&W 2008 sec. 5.1: g_i = g_0 + sum_{j<=i} f_j (f_1 is the bottom layer, fig 4), and
        weighted_wiggle(g0) = sum_i f_i (g0' + 1/2 f_i' + sum_{j<i} f_j')^2
    minimised pointwise by
        g0' = -(1/sum f) sum_i f_i (1/2 f_i' + sum_{j<i} f_j').
    Discretised the way matplotlib and Byron's StreamLayout do it: weights f(x_k),
    derivatives -> first differences f(x_k) - f(x_{k-1}), g0(x_0) = -T(x_0)/2.
    The discrete objective J = sum_k sum_i f_i(x_k) (dg0_k + 1/2 df_i + sum_{j<i} df_j)^2
    separates into one convex quadratic per step, so the per-step minimiser is the global
    minimiser over all baselines with g0(x_0) fixed (J does not depend on g0(x_0)).
  * A literal Fraction port of Byron's StreamLayout.java / LayerLayout.stackOnBaseline
    (github.com/leebyron/streamgraph_generator @ e7370a6), which works in Processing screen
    coordinates (y grows downwards; layer 0 is drawn at the bottom of the screen). It is
    converted to y-up by Y = -y.
  * A literal Fraction port of matplotlib's stackplot.py weighted_wiggle block
    (44f2e00 l. 115-129), used only to confirm that the port reproduces matplotlib.
"""
import math
import random
from fractions import Fraction as F

import numpy as np
from _synth import banner, report, allclose, close
import matplotlib.pyplot as plt

banner()


def info(s):
    print("   " + s)


H = F(1, 2)


# ---------------------------------------------------------------- exact baselines
def bw_minimiser(L, reverse=False):
    """Per-step minimiser of sum_i f_i (midline slope_i)^2 for the stacking order of L
    (L[0] at the bottom). reverse=True: the same objective with the order reversed
    (L[-1] at the bottom); the returned curve is still the bottom of that stack."""
    m, n = len(L), len(L[0])
    order = list(range(m))[::-1] if reverse else list(range(m))
    g = [-sum(L[i][0] for i in range(m)) * H]
    for k in range(1, n):
        T = sum(L[i][k] for i in range(m))
        d = [L[i][k] - L[i][k - 1] for i in range(m)]
        if T == 0:
            g.append(g[-1])  # objective is identically 0 at this step
            continue
        num, below = F(0), F(0)
        for i in order:
            num += L[i][k] * (below + H * d[i])
            below += d[i]
        g.append(g[-1] - num / T)
    return g


def byron_streamlayout_yup(L):
    """StreamLayout.layout + stackOnBaseline, literally, then Y = -y."""
    m, n = len(L), len(L[0])
    center = [F(0)] * n
    baseline = [F(0)] * n
    for i in range(n):
        center[i] = F(0) if i == 0 else center[i - 1]
        total = sum(L[j][i] for j in range(m))
        for j in range(m):
            if i == 0:
                increase = L[j][i]
                move_up = H
            else:
                below = H * L[j][i]
                for k in range(j + 1, m):
                    below += L[k][i]
                increase = L[j][i] - L[j][i - 1]
                move_up = F(0) if total == 0 else below / total
            center[i] += (move_up - H) * increase
        baseline[i] = center[i] + H * total  # screen y of the bottom edge
    # stackOnBaseline: layer j spans screen y in [baseline - sum_{<=j}, baseline - sum_{<j}]
    bottoms = [-b for b in baseline]  # y-up bottom of layer 0
    tops = []
    acc = list(baseline)
    for j in range(m):
        acc = [acc[i] - L[j][i] for i in range(n)]
        tops.append([-a for a in acc])  # y-up top of layer j
    return bottoms, tops


def mpl_port(L):
    """stackplot.py 44f2e00 l. 116-128, element by element, in Fraction."""
    m, n = len(L), len(L[0])
    total = [sum(L[j][i] for j in range(m)) for i in range(n)]
    inv_total = [F(0) if t <= 0 else 1 / t for t in total]
    stack = [[sum(L[j][i] for j in range(r + 1)) for i in range(n)] for r in range(m)]
    increase = [[L[j][0]] + [L[j][i] - L[j][i - 1] for i in range(1, n)] for j in range(m)]
    move_up = [[(total[i] - stack[j][i] + H * L[j][i]) * inv_total[i] for i in range(n)] for j in range(m)]
    for j in range(m):
        move_up[j][0] = H
    c = [sum((move_up[j][i] - H) * increase[j][i] for j in range(m)) for i in range(n)]
    center = [sum(c[:i + 1]) for i in range(n)]
    return [center[i] - H * total[i] for i in range(n)]


def objective(L, g, weights="current", reverse=False):
    """J = sum_k sum_i w_i (dg0 + 1/2 df_i + sum_{j<i} df_j)^2 over the order of L."""
    m, n = len(L), len(L[0])
    order = list(range(m))[::-1] if reverse else list(range(m))
    s = F(0)
    for k in range(1, n):
        dg = g[k] - g[k - 1]
        below = F(0)
        for i in order:
            d = L[i][k] - L[i][k - 1]
            w = {"current": L[i][k], "previous": L[i][k - 1], "average": (L[i][k] + L[i][k - 1]) / 2}[weights]
            sl = dg + below + H * d
            s += w * sl * sl
            below += d
    return s


def minimiser_w(L, weights):
    """Per-step minimiser of objective(L, ., weights) for the drawn order."""
    m, n = len(L), len(L[0])
    g = [-sum(L[i][0] for i in range(m)) * H]
    for k in range(1, n):
        num, den, below = F(0), F(0), F(0)
        for i in range(m):
            d = L[i][k] - L[i][k - 1]
            w = {"current": L[i][k], "previous": L[i][k - 1], "average": (L[i][k] + L[i][k - 1]) / 2}[weights]
            num += w * (below + H * d)
            den += w
            below += d
        g.append(g[-1] - (num / den if den else 0))
    return g


def wiggle_unweighted(L, reverse=False):
    m = len(L)
    idx = range(m)
    return [-sum((((j + H) if reverse else (m - j - H)) * L[j][i]) for j in idx) / m for i in range(len(L[0]))]


def mpl_baseline(L, baseline="weighted_wiggle", dtype=float):
    fig, ax = plt.subplots()
    xs = list(range(len(L[0])))
    colls = ax.stackplot(xs, *np.array([[float(v) for v in r] for r in L], dtype=dtype), baseline=baseline)
    def per_x(c, pick):
        d = {}
        for px, py in c.get_paths()[0].vertices:
            d[px] = pick(d.get(px, py), py)
        return [d[xv] for xv in xs]
    out = per_x(colls[0], min)
    tops = [per_x(c, max) for c in colls]
    plt.close(fig)
    return out, tops


def fmt(g):
    return "[" + ", ".join(str(x) for x in g) + "]"


def ffmt(g):
    return "[" + ", ".join("%.4f" % float(x) for x in g) + "]"


# ---------------------------------------------------------------- 0. the reference code
print("#### 0. Byron's StreamLayout (y-down) ported to y-up equals the B&W 2008 per-step minimiser")
cases = {
    "2 layers, bottom grows": [[1, 3], [1, 1]],
    "2 layers, top grows": [[1, 1], [1, 3]],
    "m3 example (3 layers x 7)": [[1, 1, 2, 3, 3, 2, 1], [1, 2, 3, 5, 4, 2, 2], [2, 1, 1, 1, 2, 4, 6]],
    "4 layers x 5": [[5, 1, 0, 2, 7], [1, 1, 4, 4, 0], [0, 3, 3, 1, 2], [2, 6, 1, 0, 1]],
}
LF = {k: [[F(v) for v in r] for r in L] for k, L in cases.items()}
for name, L in LF.items():
    bo, tops = byron_streamlayout_yup(L)
    mn = bw_minimiser(L)
    report(f"{name}: Byron StreamLayout bottom (y-up) == B&W minimiser, exactly", bo == mn, fmt(bo))
    st = [[mn[i] + sum(L[j][i] for j in range(r + 1)) for i in range(len(mn))] for r in range(len(L))]
    report(f"{name}: Byron layer tops (y-up) == minimiser + cumulative sums (layer 0 at the bottom)", tops == st)

# ---------------------------------------------------------------- 1. matplotlib vs the port
print("#### 1. matplotlib's weighted_wiggle: the Fraction port reproduces the installed build")
for name, L in LF.items():
    g_mpl, _ = mpl_baseline(cases[name])
    port = mpl_port(L)
    report(f"{name}: installed stackplot baseline == Fraction port of stackplot.py l.116-128", allclose(g_mpl, [float(x) for x in port], 1e-12, 1e-12), ffmt(g_mpl))

# ---------------------------------------------------------------- 2. the finding
print("#### 2. matplotlib vs the documented / published minimiser")
for name, L in LF.items():
    port = mpl_port(L)
    mn = bw_minimiser(L)
    rv = bw_minimiser(L, reverse=True)
    bo, tops = byron_streamlayout_yup(L)
    Jm, Jt = objective(L, port), objective(L, mn)
    info(f"{name}: layers {cases[name]}")
    info(f"  B&W minimiser (drawn order)   g0 = {fmt(mn)}  = {ffmt(mn)}")
    info(f"  matplotlib                    g0 = {fmt(port)}  = {ffmt(port)}")
    info(f"  max |difference|                 = {max(abs(a - b) for a, b in zip(port, mn))}  (max total thickness {max(sum(c) for c in zip(*L))})")
    info(f"  weighted wiggle J: matplotlib {Jm} = {float(Jm):.4f}; minimiser {Jt} = {float(Jt):.4f}; ratio {float(Jm / Jt) if Jt else float('inf'):.4f}")
    report(f"{name}: matplotlib baseline == B&W minimiser ('Does the same but weights ...', B&W 2008 eq. for g0')", port == mn,
           f"J {float(Jm):.4f} vs {float(Jt):.4f}")
    report(f"{name}: [explanation] matplotlib == minimiser for the REVERSED layer order, exactly", port == rv)
    report(f"{name}: [explanation] matplotlib == -(top of Byron's layout), i.e. +center - T/2 instead of -center - T/2",
           port == [-t for t in tops[-1]])
    report(f"{name}: [explanation] J(matplotlib, drawn order) == J(minimiser, reversed order)",
           Jm == objective(L, mn, reverse=True) and objective(L, port, reverse=True) == Jt)

# ---------------------------------------------------------------- 3. closed-form 2-layer case
print("#### 3. two layers, closed form")
# f1 (bottom), f2 (top), one step: dg0 = -(f1 d1/2 + f2 (d1 + d2/2)) / T   (drawn order)
#                                  mpl: -(f2 d2/2 + f1 (d2 + d1/2)) / T   (reversed)
# difference mpl - minimiser = (f2 d1 - f1 d2) / T  per step.
for (a0, a1), (b0, b1) in [((1, 3), (1, 1)), ((1, 1), (1, 3)), ((2, 2), (1, 5)), ((4, 1), (1, 4)), ((2, 4), (1, 2))]:
    L = [[F(a0), F(a1)], [F(b0), F(b1)]]
    d1, d2, T = L[0][1] - L[0][0], L[1][1] - L[1][0], L[0][1] + L[1][1]
    diff = mpl_port(L)[1] - bw_minimiser(L)[1]
    report(f"f1={a0}->{a1}, f2={b0}->{b1}: mpl - minimiser at x1 == (f2*d1 - f1*d2)/T = {(L[1][1] * d1 - L[0][1] * d2) / T}",
           diff == (L[1][1] * d1 - L[0][1] * d2) / T, f"J mpl {objective(L, mpl_port(L))} vs min {objective(L, bw_minimiser(L))}")
info("so the two agree at a step exactly when f2*d1 == f1*d2, i.e. both layers change in proportion to their thickness")

# ---------------------------------------------------------------- 4. when they agree
print("#### 4. cases where matplotlib is right")
L1 = [[F(v) for v in [1, 4, 2, 7]]]
report("one layer: matplotlib == minimiser (dg0 = -df/2)", mpl_port(L1) == bw_minimiser(L1))
Lp = [[F(v) for v in r] for r in [[1, 2, 5, 3], [4, 4, 1, 6], [1, 2, 5, 3]]]
report("palindromic layer order (L0 == L2): matplotlib == minimiser", mpl_port(Lp) == bw_minimiser(Lp))
Lprop = [[F(v) for v in r] for r in [[1, 2, 4, 3], [2, 4, 8, 6], [3, 6, 12, 9]]]
report("all layers proportional to one profile: matplotlib == minimiser", mpl_port(Lprop) == bw_minimiser(Lprop))

# ---------------------------------------------------------------- 5. random exact cases
print("#### 5. random small integer layers (exact)")
rng = random.Random(20081101)
N = 400
same = below_min = 0
ratios, worst = [], None
for t in range(N):
    m = rng.randint(2, 5)
    n = rng.randint(3, 8)
    L = [[F(rng.randint(0, 9)) for _ in range(n)] for _ in range(m)]
    for i in range(n):
        if sum(L[j][i] for j in range(m)) == 0:
            L[0][i] = F(1)
    p, mn = mpl_port(L), bw_minimiser(L)
    Jm, Jt = objective(L, p), objective(L, mn)
    if Jm < Jt:
        below_min += 1
    if p == mn:
        same += 1
    elif Jt > 0:
        ratios.append(Jm / Jt)
    gap = max(abs(a - b) for a, b in zip(p, mn)) / max(sum(c) for c in zip(*L))
    if worst is None or gap > worst[0]:
        worst = (gap, L)
ratios.sort()
info(f"{N} random cases (2-5 layers, 3-8 points, integers 0..9): matplotlib == minimiser in {same}")
info(f"J(matplotlib)/J(minimiser) over the others: min {float(ratios[0]):.3f}, median {float(ratios[len(ratios) // 2]):.3f}, "
     f"90th pct {float(ratios[int(0.9 * len(ratios))]):.3f}, max {float(ratios[-1]):.3f}")
info(f"largest max|g0_mpl - g0_min| / max total thickness: {float(worst[0]):.3f}")
report("random cases: matplotlib's J is never below the minimiser's (sanity of the minimiser)", below_min == 0, f"{below_min} below")
report("random cases: matplotlib == minimiser in every case", same == N, f"{same}/{N}")

# ---------------------------------------------------------------- 6. not a discretisation artefact
print("#### 6. the gap is not a discretisation choice")
L = LF["m3 example (3 layers x 7)"]
for w in ("current", "previous", "average"):
    mw = minimiser_w(L, w)
    report(f"weights f(x_{{k}}) choice '{w}': matplotlib == minimiser of that discretisation", mpl_port(L) == mw,
           f"J_{w}: mpl {float(objective(L, mpl_port(L), w)):.4f} vs min {float(objective(L, mw, w)):.4f}")
# smooth layers on [0, 1]: f1 = 1 + 2x (bottom), f2 = 1 (top). Continuous B&W:
#   g0' = -(3 + 2x)/(2 + 2x)  ->  g0(1) - g0(0) = -1 - ln(2)/2
#   reversed order: -(1 + 2x)/(2 + 2x) -> -1 + ln(2)/2    (gap ln 2, independent of the grid)
for npts in (11, 101, 1001, 10001):
    xs = np.linspace(0, 1, npts)
    Ls = [list(1 + 2 * xs), list(np.ones(npts))]
    g_mpl, _ = mpl_baseline(Ls)
    # float evaluation of the same per-step minimiser (Fraction is too slow at n = 10001)
    f1, f2 = np.asarray(Ls[0]), np.asarray(Ls[1])
    d1, d2 = np.diff(f1), np.diff(f2)
    mn = np.concatenate([[0.0], np.cumsum(-(f1[1:] * 0.5 * d1 + f2[1:] * (d1 + 0.5 * d2)) / (f1[1:] + f2[1:]))])
    gm = g_mpl[-1] - g_mpl[0]
    info(f"n={npts}: matplotlib g0(1)-g0(0) = {gm:.6f} (continuous reversed-order {-1 + math.log(2) / 2:.6f}); "
         f"minimiser {mn[-1]:.6f} (continuous {-1 - math.log(2) / 2:.6f})")
report("smooth 2-layer case: matplotlib's g0(1)-g0(0) tends to the reversed-order value -1 + ln2/2, not -1 - ln2/2",
       close(gm, -1 + math.log(2) / 2, 1e-3))

# ---------------------------------------------------------------- 7. the unweighted wiggle has the drawn orientation
print("#### 7. 'wiggle' (unweighted) is oriented for the drawn order; only 'weighted_wiggle' is reversed")
for name in ("m3 example (3 layers x 7)", "4 layers x 5"):
    L = LF[name]
    g_w, _ = mpl_baseline(cases[name], "wiggle")
    report(f"{name}: 'wiggle' == drawn-order midline minimiser -(1/m) sum (m - i - 1/2) f_i",
           allclose(g_w, [float(v) for v in wiggle_unweighted(L)], 1e-13, 1e-13))
    report(f"{name}: 'wiggle' differs from the reversed-order midline minimiser -(1/m) sum (i + 1/2) f_i",
           not allclose(g_w, [float(v) for v in wiggle_unweighted(L, True)], 1e-13, 1e-13))
    # the unweighted minimiser is the weighted one with all weights 1; check that identity in Fraction
    m = len(L)
    g = [-sum(L[i][0] for i in range(m)) * H]
    for k in range(1, len(L[0])):
        below, num = F(0), F(0)
        for i in range(m):
            d = L[i][k] - L[i][k - 1]
            num += below + H * d
            below += d
        g.append(g[-1] - num / m)
    off = wiggle_unweighted(L)[0] - g[0]
    report(f"{name}: integrating the unit-weight per-step minimiser reproduces the 'wiggle' closed form (up to its constant)",
           all(a - b == off for a, b in zip(wiggle_unweighted(L), g)))
