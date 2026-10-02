#!/usr/bin/env python
"""Matplotlib colour mapping: how a data value becomes the colour a reader sees.

Covered: Normalize (formula, documented example, clip, vmin == vmax, autoscale from
data incl. masked / NaN, inverse, integer / float32 / large-offset input), LogNorm
(formula, non-positive values, autoscale ignoring non-positive, clip, inverse),
SymLogNorm (linthresh / linscale / base against the documented "linscale = number of
decades for each half of the linear range"), AsinhNorm (documented a0*asinh(a/a0)),
FuncNorm, PowerNorm (documented formula, values below vmin [changed in 3.9], clip,
inverse), TwoSlopeNorm (documented example, each side linear, autoscale expansion),
CenteredNorm (documented example, halfrange, autoscale), BoundaryNorm (documented
left-closed bins, clip, extend, ncolors > regions stretch, NaN / masked, values exactly
on boundaries), NoNorm. Colormap.__call__ (float -> index floor(x*N), x == 1 -> N-1,
under / over / bad, ints, alpha, bytes=True), LinearSegmentedColormap against a
plain-Python port of the documented segmentdata semantics (incl. gamma), from_list,
reversed() and resampled() of both colormap classes. End to end: ScalarMappable.to_rgba
and imshow (the RGBA array returned by AxesImage.make_image) with NaN / masked / inf
cells, values exactly at colour edges, float32 and large offsets; colorbar bands
(QuadMesh edges and colours) and ticks for Normalize, BoundaryNorm and contourf.
contour / contourf: automatic level choice (MaxNLocator, the documented level count),
extend, the documented fill rule "z1 < Z <= z2" (lowest interval closed), band colours
with a ListedColormap, with colors= and with set_under / set_over.

Truths: fractions.Fraction, closed forms (math.log, math.asinh), plain-Python ports
written from the docstrings. Never matplotlib itself."""
import sys, os, math, warnings, random
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import matplotlib.cm as mcm
from matplotlib.path import Path

warnings.filterwarnings("ignore")
banner()
_cfile = mc.__file__
print(f"   matplotlib.colors from {_cfile}")
MV = mpl_version()
NPV = tuple(int(v) for v in np.__version__.split(".")[:2])
def info(s): print("   " + s)
rng = random.Random(20261001)

def raises(fn, exc=Exception):
    try: fn()
    except exc as e: return type(e).__name__
    return None

def fl(x): return float(x)
def ex(x): return F(float(x))

# distinct byte-exact colours (0 or 255 components) -> robust index identification
PAL = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#00ffff', '#ff00ff', '#000000',
       '#ffffff', '#800000', '#008000', '#000080', '#808000', '#008080', '#800080',
       '#c0c0c0', '#404040']
def rgba_of(hexs):
    h = hexs.lstrip('#'); return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4)) + (1.0,)
def same_rgba(a, b, tol=1e-12):
    return all(abs(float(x) - float(y)) <= tol for x, y in zip(a, b))
def which(rgba, cols):
    for i, c in enumerate(cols):
        if same_rgba(rgba, rgba_of(c), 1e-9): return i
    return None

# ===================================================================== Normalize
print("#### Normalize")
n = mc.Normalize(vmin=-1, vmax=1, clip=False)
r = n([-2, -1, 0, 1, 2])
report('Normalize docstring example: Normalize(-1,1)([-2..2]) = [-0.5,0,0.5,1,1.5]',
       allclose(r, [-0.5, 0, 0.5, 1, 1.5], 0, 0), str(list(r)))
n = mc.Normalize(vmin=-1, vmax=1, clip=True)
r = n([-2, -1, 0, 1, 2])
report('Normalize docstring example clip=True -> [0,0,0.5,1,1]', allclose(r, [0, 0, 0.5, 1, 1], 0, 0), str(list(r)))
# random values against Fraction
bad = 0; worst = 0.0
for _ in range(400):
    a = rng.uniform(-1e3, 1e3); b = a + rng.uniform(1e-3, 1e4); v = rng.uniform(a - 10, b + 10)
    got = mc.Normalize(a, b)(v); tr = float((ex(v) - ex(a)) / (ex(b) - ex(a)))
    if not close(got, tr, 4e-16 * 8, 1e-15): bad += 1
    worst = max(worst, abs(float(got) - tr))
report('Normalize maps "[vmin, vmax] linearly to [0, 1]": 400 random (v-vmin)/(vmax-vmin) vs Fraction', bad == 0,
       f"{bad} off")
info(f"max abs error {worst:.2e}")
r = mc.Normalize(3, 3)([1, 3, 5])
report('Normalize: "If vmin == vmax, input data will be mapped to 0"', allclose(r, [0, 0, 0], 0, 0), str(list(r)))
report('Normalize vmin > vmax raises ValueError', raises(lambda: mc.Normalize(2, 1)([1.5])) == 'ValueError')
# autoscale
n = mc.Normalize(); r = n([3., 7., 5.])
report('Normalize(): vmin/vmax "default to the minimum and maximum values of the input"',
       n.vmin == 3 and n.vmax == 7 and allclose(r, [0, 1, 0.5], 0, 0), f"{n.vmin},{n.vmax}")
ma = np.ma.array([100., 3., 7., -50.], mask=[1, 0, 0, 1])
n = mc.Normalize(); r = n(ma)
report('Normalize autoscale on masked array ignores masked values (vmin=3, vmax=7)', n.vmin == 3 and n.vmax == 7,
       f"{n.vmin},{n.vmax}")
report('Normalize keeps the input mask (masked -> masked)', list(np.ma.getmaskarray(r)) == [True, False, False, True])
n = mc.Normalize(); r = n(np.array([3., np.nan, 7.]))
info(f"Normalize()([3, nan, 7]) direct call: vmin={n.vmin} vmax={n.vmax} result={list(np.ma.filled(r, -9))}")
report('Normalize() autoscale on plain ndarray with NaN: vmin/vmax = min/max of the numeric values',
       n.vmin == 3 and n.vmax == 7, f"vmin={n.vmin} vmax={n.vmax}")
n = mc.Normalize(0, 4); r = n(np.array([0., 1., np.nan]))
report('Normalize: NaN stays NaN (-> colormap "bad")', math.isnan(float(np.ma.filled(r, 0)[2])) or bool(np.ma.getmaskarray(r)[2]))
# inverse
n = mc.Normalize(-3.5, 12.25)
xs = [-3.5, 0.0, 1.0, 12.25, 20.0]
report('Normalize.inverse(norm(x)) == x', allclose(n.inverse(n(xs)), xs, 1e-14, 1e-14))
report('Normalize.inverse(0.25) = vmin + 0.25*(vmax-vmin)', close(n.inverse(0.25), -3.5 + 0.25 * 15.75, 1e-15))
report('Normalize.inverse unscaled raises ValueError', raises(lambda: mc.Normalize().inverse(0.5)) == 'ValueError')
# dtypes (process_value Notes)
for dt, want in [(np.int8, np.float32), (np.int16, np.float32), (np.uint8, np.float32), (np.int32, np.float64),
                 (np.int64, np.float64), (np.float32, np.float32), (np.float64, np.float64)]:
    r = mc.Normalize(0, 100)(np.array([0, 25, 100], dtype=dt))
    report(f'Normalize {np.dtype(dt).name} input -> {np.dtype(want).name} ("process_value" Notes) and exact values',
           r.dtype == want and allclose(r, [0, 0.25, 1], 0, 0), f"{r.dtype} {list(r)}")
# large offset, float64 and float32 (dyadic so exact)
off = 1e6
r = mc.Normalize(off, off + 256)(np.array([off + k for k in (0, 1, 128, 255, 256)]))
report('Normalize large offset float64 (1e6 + k)/256 exact', allclose(r, [0, 1 / 256, 0.5, 255 / 256, 1], 0, 0))
r = mc.Normalize(off, off + 256)(np.array([off + k for k in (0, 1, 128, 255, 256)], dtype=np.float32))
report('Normalize large offset float32 data (1e6 + k)/256 exact', allclose(r, [0, 1 / 256, 0.5, 255 / 256, 1], 0, 0),
       str(list(r)))
r = mc.Normalize()(np.array([2**40 + 1, 2**40 + 3, 2**40 + 5], dtype=np.int64))
report('Normalize autoscale int64 with offset 2**40: [0, 0.5, 1]', allclose(r, [0, 0.5, 1], 0, 0), str(list(r)))
r = mc.Normalize(0, 1)(np.inf); r2 = mc.Normalize(0, 1)(-np.inf)
report('Normalize(0,1)(+inf) = +inf and (-inf) = -inf (-> over / under)', float(r) == np.inf and float(r2) == -np.inf,
       f"{r} {r2}")
r = mc.Normalize(0, 1)(0.25)
report('Normalize scalar in -> scalar out', np.ndim(r) == 0 and close(r, 0.25, 0, 0))

# ===================================================================== LogNorm
print("#### LogNorm")
n = mc.LogNorm(1, 1000); xs = [1, 10, 100, 1000, 31.6, 0.1, 1e4]
r = n(xs); tr = [math.log10(x) / 3 for x in xs]
report('LogNorm(1,1000) = log10(x/vmin)/log10(vmax/vmin) incl. out of range', allclose(r, tr, 1e-14, 1e-15),
       f"maxdiff {maxdiff(r, tr):.1e}")
n = mc.LogNorm(0.02, 7.5); xs = [0.02, 0.05, 1.0, 3.3, 7.5]
r = n(xs); tr = [math.log(x / 0.02) / math.log(7.5 / 0.02) for x in xs]
report('LogNorm(0.02, 7.5) closed form', allclose(r, tr, 1e-13, 1e-15), f"maxdiff {maxdiff(r, tr):.1e}")
r = mc.LogNorm(1, 100)([-1., 0., 10.])
report('LogNorm: non-positive values are masked (-> "bad" colour)', list(np.ma.getmaskarray(r)) == [True, True, False])
n = mc.LogNorm(); r = n(np.array([-5., 0., 2., 20., 200.]))
report('LogNorm autoscale ignores non-positive values: vmin=2, vmax=200', n.vmin == 2 and n.vmax == 200,
       f"{n.vmin},{n.vmax}")
report('LogNorm autoscaled values [x, x, 0, 0.5, 1]', allclose(np.ma.filled(r, -9)[2:], [0, 0.5, 1], 1e-15, 1e-15))
try:
    n = mc.LogNorm(); r = n(np.array([np.nan, 1., 10., 100.]))
    report('LogNorm autoscale with NaN: vmin=1, vmax=100, NaN masked', n.vmin == 1 and n.vmax == 100 and
           bool(np.ma.getmaskarray(r)[0]), f"{n.vmin},{n.vmax}")
except Exception as e:
    report('LogNorm autoscale with NaN: vmin=1, vmax=100, NaN masked', False, f"raises {type(e).__name__}: {e}")
n = mc.LogNorm(); r = n(np.ma.array([0.001, 1., 10., 1e6], mask=[1, 0, 0, 1]))
report('LogNorm autoscale on masked array ignores masked values', n.vmin == 1 and n.vmax == 10, f"{n.vmin},{n.vmax}")
r = mc.LogNorm(1, 100, clip=True)([0.5, 1000., 10.])
report('LogNorm clip=True: below vmin -> 0, above vmax -> 1', allclose(r, [0, 1, 0.5], 1e-15, 1e-15), str(list(r)))
r = mc.LogNorm(1, 100, clip=True)([-3.])
info(f"LogNorm(1,100,clip=True)(-3) = {r[0]} masked={bool(np.ma.getmaskarray(r)[0])} (clip doc: below vmin -> 0)")
n = mc.LogNorm(2, 2000); xs = [2, 20, 200, 2000, 5]
report('LogNorm.inverse(norm(x)) == x', allclose(n.inverse(n(xs)), xs, 1e-13, 1e-13))
r = mc.LogNorm(5, 5)([5, 5])
report('LogNorm vmin == vmax -> 0', allclose(r, [0, 0], 0, 0), str(list(r)))

# ===================================================================== SymLogNorm
print("#### SymLogNorm (documented: linscale = decades used by each half of the linear range)")
def symlog_doc(x, lt, ls, base):
    """Documented semantics, in decades: |x| <= lt is linear and its half spans ls decades;
    outside, each factor `base` adds one decade."""
    if abs(x) <= lt: return ls * x / lt
    return math.copysign(ls + math.log(abs(x) / lt) / math.log(base), x)
def symlog_norm_doc(x, lt, ls, base, vmin, vmax):
    a, b = symlog_doc(vmin, lt, ls, base), symlog_doc(vmax, lt, ls, base)
    return (symlog_doc(x, lt, ls, base) - a) / (b - a)
for (lt, ls, base, vmin, vmax) in [(1, 1, 10, -100, 100), (1, 1, 2, -64, 64), (0.5, 2, 10, -1000, 10),
                                   (2, 0.5, math.e, -50, 500)]:
    n = mc.SymLogNorm(linthresh=lt, linscale=ls, base=base, vmin=vmin, vmax=vmax)
    xs = [vmin, -lt, 0, lt, lt * base, vmax]
    r = n(xs); tr = [symlog_norm_doc(x, lt, ls, base, vmin, vmax) for x in xs]
    report(f'SymLogNorm(linthresh={lt}, linscale={ls}, base={base:.4g}) vs documented "{ls} decade(s) for each half of '
           'the linear range"', allclose(r, tr, 1e-12, 1e-12), f"maxdiff {maxdiff(r, tr):.4f}")
    info(f"vals {[round(float(v), 4) for v in r]} doc {[round(v, 4) for v in tr]}")
    # share of the colour range used by the positive linear half vs one decade
    lin = float(n(lt)) - float(n(0)); dec = float(n(lt * base)) - float(n(lt))
    info(f"  colour-range share: linear half (0..linthresh) {lin:.4f}, one decade {dec:.4f}, ratio {lin / dec:.4f} "
         f"(documented ratio {ls})")
n = mc.SymLogNorm(linthresh=1, linscale=1, base=10, vmin=-100, vmax=100)
xs = [-1, -0.5, 0, 0.25, 0.5, 1]; r = [float(v) for v in n(xs)]
lin_ok = all(close((r[i] - r[2]) / (r[5] - r[2]), xs[i], 1e-12, 1e-12) for i in range(len(xs)))
report('SymLogNorm is linear inside (-linthresh, linthresh) ("the plot is linear")', lin_ok)
r = [float(v) for v in n([2, 20, 200 / 10 * 10, 5, 50])]
report('SymLogNorm log region: each factor of base adds the same colour step', close(r[1] - r[0], r[4] - r[3], 1e-12, 1e-14))
xs = [0.3, 1, 7, 55, 100]
r1 = n(xs); r2 = n([-x for x in xs])
report('SymLogNorm with vmin = -vmax is antisymmetric: norm(-x) = 1 - norm(x)', allclose(r2, [1 - float(v) for v in r1], 1e-13, 1e-13))
xs = [-100, -3, -0.2, 0, 0.7, 40, 100]
report('SymLogNorm.inverse(norm(x)) == x', allclose(n.inverse(n(xs)), xs, 1e-12, 1e-12))
r = mc.SymLogNorm(1, vmin=-10, vmax=10, clip=True)([-1e3, 1e3])
report('SymLogNorm clip=True -> [0, 1]', allclose(r, [0, 1], 1e-15, 1e-15), str(list(r)))

# ===================================================================== AsinhNorm / FuncNorm
print("#### AsinhNorm / FuncNorm")
if hasattr(mc, "AsinhNorm"):
    for a0 in (1.0, 0.1, 25.0):
        n = mc.AsinhNorm(linear_width=a0, vmin=-200, vmax=50)
        xs = [-200, -3, 0, 0.05, 2, 50, 80]
        T = lambda x: a0 * math.asinh(x / a0)
        tr = [(T(x) - T(-200)) / (T(50) - T(-200)) for x in xs]
        r = n(xs)
        report(f'AsinhNorm(linear_width={a0}) = documented a0*asinh(a/a0) rescaled', allclose(r, tr, 1e-12, 1e-13),
               f"maxdiff {maxdiff(r, tr):.1e}")
    n = mc.AsinhNorm(linear_width=2, vmin=-10, vmax=10); xs = [-10, -1, 0, 3, 10]
    report('AsinhNorm.inverse(norm(x)) == x', allclose(n.inverse(n(xs)), xs, 1e-12, 1e-12))
else:
    info("AsinhNorm not in this build (added in 3.6)")
n = mc.FuncNorm((np.sqrt, np.square), vmin=0, vmax=16)
r = n([0, 1, 4, 9, 16, 25])
report('FuncNorm((sqrt, square), 0, 16) = (sqrt(x)-0)/(4-0)', allclose(r, [0, .25, .5, .75, 1, 1.25], 1e-15, 1e-15), str(list(r)))
report('FuncNorm.inverse(norm(x)) == x', allclose(n.inverse(n([0, 1, 4, 9])), [0, 1, 4, 9], 1e-14, 1e-14))
n = mc.FuncNorm((np.sqrt, np.square)); r = n(np.array([4., 9., 16.]))
report('FuncNorm autoscale: vmin/vmax from data', n.vmin == 4 and n.vmax == 16 and allclose(r, [0, 0.5, 1], 1e-15, 1e-15))
r = mc.FuncNorm((np.sqrt, np.square), vmin=0, vmax=16)([-4.])
info(f"FuncNorm(sqrt)(-4) -> masked={bool(np.ma.getmaskarray(r)[0])} (outside the function domain)")

# ===================================================================== PowerNorm
print("#### PowerNorm")
n = mc.PowerNorm(gamma=2, vmin=1, vmax=5)
xs = [1, 2, 3, 4, 5]; tr = [float((F(x - 1, 4)) ** 2) for x in xs]
report('PowerNorm(gamma=2) = ((x-vmin)/(vmax-vmin))**gamma (Notes formula)', allclose(n(xs), tr, 1e-15, 1e-16))
n = mc.PowerNorm(gamma=0.5, vmin=0, vmax=10)
xs = [0, 0.1, 2.5, 10]; tr = [math.sqrt(x / 10) for x in xs]
report('PowerNorm(gamma=0.5) closed form', allclose(n(xs), tr, 1e-15, 1e-16))
r = mc.PowerNorm(gamma=2, vmin=1, vmax=5)([7.])
report('PowerNorm above vmax, clip=False: ((7-1)/4)**2 = 2.25 (> 1 -> over)', close(r[0], 2.25, 1e-15), str(r[0]))
r = mc.PowerNorm(gamma=2, vmin=1, vmax=5)([-1., 0.])
if MV >= (3, 9):
    tr = [-0.5, -0.25]; lab = 'PowerNorm below vmin, clip=False: "For input values below vmin, gamma is set to one" -> [-0.5, -0.25]'
else:
    tr = [0.0, 0.0]; lab = 'PowerNorm below vmin, clip=False: pre-3.9 behaviour maps to 0 (api_changes_3.9.0 "PowerNorm no longer clips values below vmin")'
report(lab, allclose(r, tr, 1e-15, 1e-16), str(list(r)))
r = mc.PowerNorm(gamma=2, vmin=1, vmax=5, clip=True)([-1., 3., 9.])
report('PowerNorm clip=True: [0, 0.25, 1]', allclose(r, [0, 0.25, 1], 1e-15, 1e-16), str(list(r)))
n = mc.PowerNorm(gamma=3, vmin=-2, vmax=6); xs = [-2, 0, 1, 6]
report('PowerNorm.inverse(norm(x)) == x', allclose(n.inverse(n(xs)), xs, 1e-13, 1e-13))
n = mc.PowerNorm(gamma=2); r = n(np.ma.array([2., 4., 6., 100.], mask=[0, 0, 0, 1]))
report('PowerNorm autoscale ignores masked, keeps mask', n.vmin == 2 and n.vmax == 6 and
       allclose(np.ma.filled(r, -9)[:3], [0, 0.25, 1], 1e-15) and bool(np.ma.getmaskarray(r)[3]))
r = mc.PowerNorm(2, 3, 3)([3., 3.])
report('PowerNorm vmin == vmax -> 0', allclose(r, [0, 0], 0, 0))

# ===================================================================== TwoSlopeNorm
print("#### TwoSlopeNorm")
n = mc.TwoSlopeNorm(vmin=-4000., vcenter=0., vmax=10000)
r = n([-4000., -2000., 0., 2500., 5000., 7500., 10000.])
report('TwoSlopeNorm docstring example -> [0, .25, .5, .625, .75, .875, 1]',
       allclose(r, [0., 0.25, 0.5, 0.625, 0.75, 0.875, 1.0], 1e-15, 1e-16), str(list(r)))
bad = 0
for _ in range(200):
    a = rng.uniform(-100, 0); c = a + rng.uniform(0.01, 50); b = c + rng.uniform(0.01, 500)
    v = rng.uniform(a, b); n = mc.TwoSlopeNorm(c, a, b)
    trv = (ex(v) - ex(a)) / (ex(c) - ex(a)) / 2 if v <= c else F(1, 2) + (ex(v) - ex(c)) / (ex(b) - ex(c)) / 2
    if not close(n(v), float(trv), 1e-13, 1e-15): bad += 1
report('TwoSlopeNorm: vcenter -> 0.5 and each side linear (200 random vs Fraction)', bad == 0, f"{bad} off")
r = mc.TwoSlopeNorm(0, -2, 4)([-3., 5.])
report('TwoSlopeNorm out of range -> -inf / +inf (under / over)', float(r[0]) == -np.inf and float(r[1]) == np.inf, str(list(r)))
n = mc.TwoSlopeNorm(vcenter=0); n(np.array([1., 2., 3.]))
if MV >= (3, 8):
    report('TwoSlopeNorm autoscale with all data above vcenter: "vmin ... expanded so vcenter lies in the middle" (vmin=-3)',
           n.vmin == -3 and n.vmax == 3, f"{n.vmin},{n.vmax}")
else:
    report('TwoSlopeNorm autoscale, data above vcenter: pre-3.8 "clip at vcenter" -> vmin=0 (api_changes_3.8.0 '
           '"TwoSlopeNorm now auto-expands")', n.vmin == 0 and n.vmax == 3, f"{n.vmin},{n.vmax}")
n = mc.TwoSlopeNorm(vcenter=10); n(np.array([-5., 2.]))
if MV >= (3, 8):
    report('TwoSlopeNorm autoscale with all data below vcenter: vmax expanded (vmax=25)', n.vmin == -5 and n.vmax == 25,
           f"{n.vmin},{n.vmax}")
else:
    report('TwoSlopeNorm autoscale, data below vcenter: pre-3.8 vmax clipped to vcenter (10)', n.vmin == -5 and n.vmax == 10,
           f"{n.vmin},{n.vmax}")
report('TwoSlopeNorm(vcenter >= vmax) raises ValueError', raises(lambda: mc.TwoSlopeNorm(5, 0, 5)) == 'ValueError')
r = mc.TwoSlopeNorm(0, -1, 1)(np.ma.array([0.5, 9.], mask=[0, 1]))
report('TwoSlopeNorm keeps the mask', list(np.ma.getmaskarray(r)) == [False, True])
n = mc.TwoSlopeNorm(1, -1, 5); xs = [-1, 0, 1, 2.5, 5]
report('TwoSlopeNorm.inverse(norm(x)) == x', allclose(n.inverse(n(xs)), xs, 1e-14, 1e-14))

# ===================================================================== CenteredNorm
print("#### CenteredNorm")
r = mc.CenteredNorm(halfrange=4.0)([-2., 0., 4.])
report('CenteredNorm docstring example: halfrange=4 -> [0.25, 0.5, 1]', allclose(r, [0.25, 0.5, 1.0], 0, 0), str(list(r)))
n = mc.CenteredNorm(vcenter=1); r = n(np.array([-1., 0.5, 4.]))
report('CenteredNorm autoscale: halfrange = max |A - vcenter| = 3, vmin=-2, vmax=4',
       n.halfrange == 3 and n.vmin == -2 and n.vmax == 4, f"{n.halfrange} {n.vmin} {n.vmax}")
report('CenteredNorm autoscaled values (x+2)/6', allclose(r, [1 / 6, 2.5 / 6, 1], 1e-15, 1e-16), str(list(r)))
n = mc.CenteredNorm(); n(np.ma.array([-1., 2., -50.], mask=[0, 0, 1]))
report('CenteredNorm autoscale ignores masked values (halfrange 2)', n.halfrange == 2, f"{n.halfrange}")
r = mc.CenteredNorm(halfrange=1, clip=True)([-5., 5.])
report('CenteredNorm clip=True -> [0, 1]', allclose(r, [0, 1], 0, 0))
n = mc.CenteredNorm(vcenter=0, halfrange=2); n.vcenter = 1; r = n([-1., 1., 3.])
report('CenteredNorm: changing vcenter keeps halfrange: norm([-1, 1, 3]) = [0, 0.5, 1]', allclose(r, [0, 0.5, 1], 0, 0),
       f"{list(r)} vmin={n.vmin} vmax={n.vmax}")

# ===================================================================== BoundaryNorm
print("#### BoundaryNorm")
def bn_doc(v, b, ncolors, clip=False, extend='neither'):
    """Port of the BoundaryNorm docstring: n-th bin is b[n] <= v < b[n+1]; out of range -> -1 / ncolors
    (clip: 0 / ncolors-1); extensions add bins; with more colours than bins the bin index is mapped
    linearly from [0, nbins-1] to [0, ncolors-1] (floor of the exact value, 1 bin -> middle colour)."""
    b = [ex(x) for x in b]; v = ex(v); nb = len(b) - 1; off = 0
    if extend in ('min', 'both'): nb += 1; off = 1
    if extend in ('max', 'both'): nb += 1
    if v < b[0]: return 0 if clip else -1
    if v >= b[-1]: return ncolors - 1 if clip else ncolors
    i = max(k for k in range(len(b) - 1) if b[k] <= v) + off
    if ncolors > nb:
        if nb == 1: return (ncolors - 1) // 2
        q = F(ncolors - 1, nb - 1) * i; return q.numerator // q.denominator
    return i
b = [0, 1, 2.5, 4, 10]
vals = [-1, 0, 0.5, 1, 2.4999, 2.5, 3.99, 4, 9.999, 10, 11]
for nc in (4, 5, 7, 16, 256):
    r = mc.BoundaryNorm(b, nc)(vals); tr = [bn_doc(v, b, nc) for v in vals]
    report(f'BoundaryNorm(b={b}, ncolors={nc}) on values incl. exactly on boundaries (left-closed bins)',
           list(map(int, r)) == tr, f"got {list(map(int, r))} doc {tr}")
for ext in ('min', 'max', 'both'):
    for nc in (6, 9, 256):
        r = mc.BoundaryNorm(b, nc, extend=ext)(vals); tr = [bn_doc(v, b, nc, extend=ext) for v in vals]
        report(f'BoundaryNorm extend={ext!r}, ncolors={nc}', list(map(int, r)) == tr, f"got {list(map(int, r))} doc {tr}")
r = mc.BoundaryNorm(b, 4, clip=True)(vals); tr = [bn_doc(v, b, 4, clip=True) for v in vals]
report('BoundaryNorm clip=True: below -> 0, >= last boundary -> ncolors-1', list(map(int, r)) == tr, f"got {list(map(int, r))}")
r = mc.BoundaryNorm(b, 10, clip=True)(vals); tr = [bn_doc(v, b, 10, clip=True) for v in vals]
report('BoundaryNorm clip=True with ncolors > bins', list(map(int, r)) == tr, f"got {list(map(int, r))} doc {tr}")
r = mc.BoundaryNorm([0, 1], 9)([-1, 0, 0.5, 1])
report('BoundaryNorm single bin, ncolors=9 -> middle colour 4', list(map(int, r)) == [-1, 4, 4, 9], str(list(r)))
report('BoundaryNorm ncolors < number of bins raises ValueError', raises(lambda: mc.BoundaryNorm(b, 3)) == 'ValueError')
report('BoundaryNorm extend=both needs ncolors >= bins+2 (ValueError)', raises(lambda: mc.BoundaryNorm(b, 5, extend='both')) == 'ValueError')
report('BoundaryNorm clip=True with extend raises ValueError', raises(lambda: mc.BoundaryNorm(b, 6, clip=True, extend='min')) == 'ValueError')
# exhaustive stretch: last bin must reach the last colour, every bin the documented floor
mism = []; last = []
for nc in range(2, 200):
    for nb in range(2, min(nc, 60)):
        bb = list(range(nb + 1)); r = mc.BoundaryNorm(bb, nc)([k + 0.5 for k in range(nb)])
        tr = [bn_doc(k + 0.5, bb, nc) for k in range(nb)]
        if list(map(int, r)) != tr:
            mism.append((nc, nb))
            if int(r[-1]) != nc - 1: last.append((nc, nb, int(r[-1])))
report('BoundaryNorm ncolors>bins: every bin index = documented linear map [0,nbins-1]->[0,ncolors-1] '
       '(2<=ncolors<200, 2<=bins<60)', not mism, f"{len(mism)} of the (ncolors, bins) pairs differ")
report('BoundaryNorm ncolors>bins: the last bin gets the last colour ncolors-1 (same grid)', not last,
       f"{len(last)} pairs give ncolors-2, e.g. {last[:4]}")
if mism: info(f"first mismatching (ncolors, bins): {mism[:8]}")
r = mc.BoundaryNorm(np.arange(27), 256)([25.5])
info(f"BoundaryNorm(arange(27) [26 bins], 256)(25.5) = {int(r[0])} (documented last colour 255)")
r = mc.BoundaryNorm(np.arange(13), 16)([11.5])
info(f"BoundaryNorm(arange(13) [12 bins], 16)(11.5) = {int(r[0])} (documented last colour 15)")
r = mc.BoundaryNorm(b, 5)(np.ma.array([0.5, 3., 7.], mask=[0, 1, 0]))
report('BoundaryNorm keeps the mask', list(np.ma.getmaskarray(r)) == [False, True, False])
cm5 = mc.ListedColormap(PAL[:4])
r = cm5(mc.BoundaryNorm(b, 4)(np.array([0.5, np.nan, 3.])))
report('cmap(BoundaryNorm(NaN)) is the "bad" colour ("invalid values (NaN or masked)")', same_rgba(r[1], (0, 0, 0, 0)),
       f"got {tuple(np.round(r[1], 3))}, idx {int(mc.BoundaryNorm(b, 4)(np.array([np.nan]))[0])}")
r = mc.BoundaryNorm(b, 4)(2.5)
report('BoundaryNorm scalar in -> Python int out', isinstance(r, int) and r == 2, repr(r))
try:
    r = mc.BoundaryNorm(np.arange(41), 40000)([0.5, 39.5, 41.])
    got = [int(x) for x in r]
except Exception as e:
    got = type(e).__name__
tr = [bn_doc(v, list(range(41)), 40000) for v in (0.5, 39.5, 41.)]
report('BoundaryNorm with ncolors=40000 (> int16) gives the documented indices', got == tr, f"got {got} doc {tr}")

# ===================================================================== NoNorm
print("#### NoNorm")
r = mc.NoNorm()([0, 3, 7]); report('NoNorm passes values through unchanged', list(r) == [0, 3, 7])
report('NoNorm scalar passthrough', mc.NoNorm()(5) == 5)
cmi = mc.ListedColormap(PAL[:8])
r = cmi(mc.NoNorm()(np.array([0, 3, 7, 8, -1])))
report('ListedColormap(ints from NoNorm) indexes directly; 8 -> over, -1 -> under',
       [which(x, PAL[:8]) for x in r] == [0, 3, 7, 7, 0])

# ===================================================================== Colormap.__call__
print("#### Colormap.__call__")
for N in (1, 2, 5, 8, 256):
    cols = [(i / max(N - 1, 1), (i * 7 % 256) / 255, 0.5, 1.0) for i in range(N)]
    cmN = mc.ListedColormap(cols)
    dyadic = (N & (N - 1)) == 0
    # dyadic N: k/N is exact, so the edges themselves are tested; N=5: interior points only
    # (the float 3/5 is below the decimal 0.6, so its exact floor is ambiguous by one ulp)
    xs = ([k / N for k in range(N)] if dyadic else [k / N + 1e-9 for k in range(N)] + [(k + 1) / N - 1e-9 for k in range(N)]) \
        + [(k + 0.5) / N for k in range(N)] + [1.0, 0.0]
    got = [tuple(c) for c in cmN(np.array(xs))]
    exp = []
    for x in xs:
        if x == 1.0: i = N - 1
        else:
            q = ex(x) * N; i = q.numerator // q.denominator
        exp.append(tuple(cols[i]))
    ok = all(same_rgba(a, b) for a, b in zip(got, exp))
    report(f'ListedColormap N={N}: float x -> colour floor(x*N), x == 1.0 -> N-1', ok)
cm8 = mc.ListedColormap(PAL[:8])
xs = np.array([-1e-300, -0.0, 0.0, 1.0, np.nextafter(1.0, 2.0), np.inf, -np.inf, np.nan])
r = cm8(xs)
report('Colormap: x<0 -> under, -0.0 -> first, 1.0 -> last, 1+ulp -> over, inf -> over, -inf -> under, NaN -> bad',
       [which(c, PAL[:8]) for c in r[:7]] == [0, 0, 0, 7, 7, 7, 0] and same_rgba(r[7], (0, 0, 0, 0)))
cmx = mc.ListedColormap(PAL[:5]).with_extremes(under=PAL[8], over=PAL[9], bad=PAL[10])
r = cmx(np.array([-0.1, 0.0, 0.9999, 1.0, 1.01, np.nan]))
report('Colormap.with_extremes: under / first / last / last / over / bad',
       [which(c, PAL[:11]) for c in r] == [8, 0, 4, 4, 9, 10], str([which(c, PAL[:11]) for c in r]))
r = cmx(np.ma.array([0.1, 0.5], mask=[0, 1]))
report('Colormap: masked value -> bad colour', which(r[1], PAL[:11]) == 10)
r = cmx(np.ma.array([0.1, np.nan, 0.5], mask=[0, 0, 1]))
got = [which(c, PAL[:11]) for c in r]
report('Colormap: NaN inside a masked array that has a masked element -> bad colour ("NaN or masked")', got == [0, 10, 10], str(got))
r = cmx(np.ma.array([0.1, np.nan, 0.5], mask=[0, 0, 0]))
report('Colormap: NaN inside a masked array with no masked element -> bad colour', [which(c, PAL[:11]) for c in r] == [0, 10, 2])
r = cmx(np.array([0, 4, 5, -1, 255], dtype=np.int64))
report('Colormap int input: index 0..N-1 direct; N -> over; -1 -> under; 255 -> over',
       [which(c, PAL[:11]) for c in r] == [0, 4, 9, 8, 9], str([which(c, PAL[:11]) for c in r]))
r = cmx(np.array([0, 4, 5, 200], dtype=np.uint8))
report('Colormap uint8 input: 5 -> over, 200 -> over', [which(c, PAL[:11]) for c in r] == [0, 4, 9, 9])
r = cmx(np.array([0.2, 0.6, 0.99999994], dtype=np.float32))
report('Colormap float32 input: floor(x*N)', [which(c, PAL[:11]) for c in r] == [1, 3, 4])
r = cm8(np.array([0.1, np.nan]), alpha=0.3)
report('Colormap alpha=0.3 sets alpha; NaN stays fully transparent', close(r[0][3], 0.3, 1e-15) and r[1][3] == 0)
r = cm8(0.5)
report('Colormap scalar -> tuple', isinstance(r, tuple) and len(r) == 4)
# bytes
grey = mc.ListedColormap(['#%02x%02x%02x' % (k, k, k) for k in range(256)])
rb = grey(np.arange(256), bytes=True)
report('Colormap bytes=True returns uint8 and hex #kkkkkk -> byte k for all 256 k', rb.dtype == np.uint8 and
       all(int(rb[k, 0]) == k for k in range(256)))
c = mc.ListedColormap([(0.5, 0.2, 0.998, 1.0)])
rb = c(0.0, bytes=True)
info(f"bytes=True for float colour (0.5, 0.2, 0.998): {rb} (x*255 = 127.5, 51.0, 254.49; truncation gives 127/51/254)")
chans = (0.999, 0.7, 0.0019)
v = mc.ListedColormap([chans + (1,)])(0.0, bytes=True)
want = tuple(int(math.floor(255 * c + 0.5)) for c in chans)
report('Colormap bytes=True: float channel c -> nearest uint8 round(255*c) (as to_hex does)',
       tuple(int(x) for x in v[:3]) == want, f"got {tuple(int(x) for x in v[:3])} nearest {want} (255*c = "
       f"{[round(255 * c, 3) for c in chans]})")
info(f"to_hex{chans} = {mc.to_hex(chans)}")
rb = plt.get_cmap('viridis')(np.arange(256), bytes=True)[:, :3].astype(int)
near = np.floor(np.asarray(plt.get_cmap('viridis').colors) * 255 + 0.5).astype(int)
info(f"viridis bytes=True vs nearest: {int((rb != near).sum())} of 768 channels are 1 lower")
vir = plt.get_cmap('viridis')
r = vir(np.array([0.0, 0.5, 1.0]))
report('viridis (N=256): 0 -> colors[0], 0.5 -> colors[128], 1.0 -> colors[255]',
       same_rgba(r[0][:3], vir.colors[0]) and same_rgba(r[1][:3], vir.colors[128]) and same_rgba(r[2][:3], vir.colors[255]))

# ===================================================================== LinearSegmentedColormap
print("#### LinearSegmentedColormap vs documented segmentdata semantics")
def seg_doc(z, rows):
    """'For any input value z falling between x[i] and x[i+1], the output value of a given color will be
    linearly interpolated between y1[i] and y0[i+1]'. Exact segment points: see notes (uses y0 for
    interior x == x[i], i.e. the value approached from the left)."""
    rows = [tuple(F(v) if not isinstance(v, F) else v for v in r) for r in rows]
    z = F(z)
    if z <= rows[0][0]: return rows[0][2]
    if z >= rows[-1][0]: return rows[-1][1]
    for i in range(len(rows) - 1):
        x0, _, y1i = rows[i]; x1, y0n, _ = rows[i + 1]
        if x0 < z <= x1:
            if x1 == x0: return y0n
            return y1i + (y0n - y1i) * (z - x0) / (x1 - x0)
cdict = {'red': [(0.0, 0.0, 0.0), (0.5, 1.0, 1.0), (1.0, 1.0, 1.0)],
         'green': [(0.0, 0.0, 0.0), (0.25, 0.0, 0.0), (0.75, 1.0, 1.0), (1.0, 1.0, 1.0)],
         'blue': [(0.0, 0.0, 0.0), (0.5, 0.0, 0.0), (1.0, 1.0, 1.0)]}
dis = {'red': [(0.0, 0.0, 0.2), (0.4, 0.6, 0.9), (1.0, 0.1, 1.0)],
       'green': [(0.0, 1.0, 1.0), (0.5, 0.0, 1.0), (1.0, 0.5, 0.0)],
       'blue': [(0.0, 0.3, 0.3), (1.0, 0.7, 0.7)]}
for name, cd in (('docstring example', cdict), ('discontinuous', dis)):
    for N in (2, 5, 11, 256):
        for g in (1.0, 2.0, 0.5):
            cmap = mc.LinearSegmentedColormap('t', cd, N=N, gamma=g)
            lut = cmap(np.arange(N))
            exp = []
            for i in range(N):
                z = F(i, N - 1) ** 2 if g == 2.0 else (F(i, N - 1) if g == 1.0 else None)
                if z is None: z = F(math.sqrt(i / (N - 1)))
                exp.append([float(seg_doc(z, cd[ch])) for ch in ('red', 'green', 'blue')])
            d = maxdiff(lut[:, :3], exp)
            # the discontinuous map has samples exactly on a jump only for N=11/256 at x=0.4/0.5
            report(f'LinearSegmentedColormap {name} N={N} gamma={g}: entry i = f((i/(N-1))**gamma)', d < 1e-12,
                   f"maxdiff {d:.3g}")
cmap = mc.LinearSegmentedColormap('t', dis, N=3)
info(f"discontinuous red at x=0.5 sample (N=3): {cmap(1)[0]:.3f}; green row x=0.5 has y0=0.0, y1=1.0 -> uses y0")
c = mc.LinearSegmentedColormap.from_list('t', ['#ff0000', '#0000ff'], N=5)
r = c(np.arange(5))
exp = [(1 - i / 4, 0, i / 4, 1) for i in range(5)]
report('LinearSegmentedColormap.from_list(2 colours, N=5): equal steps', allclose(r, exp, 1e-12, 1e-12))
c = mc.LinearSegmentedColormap.from_list('t', [(0, '#000000'), (0.8, '#ffffff'), (1, '#ff0000')], N=6)
r = c(np.arange(6))
exp = []
for i in range(6):
    z = i / 5
    if z <= 0.8: exp.append((z / 0.8,) * 3)
    else: t = (z - 0.8) / 0.2; exp.append((1, 1 - t, 1 - t))
report('LinearSegmentedColormap.from_list with (value, colour) anchors', allclose(r[:, :3], exp, 1e-12, 1e-12), f"maxdiff {maxdiff(r[:, :3], exp):.2g}")

# ===================================================================== reversed / resampled
print("#### reversed() / resampled()")
def resamp(c, k):
    # resampled() is public from 3.6; 3.5.2 has the same code as the private _resample()
    return c.resampled(k) if hasattr(c, 'resampled') else c._resample(k)
if not hasattr(mc.Colormap, 'resampled'): info("this build has no Colormap.resampled(); using _resample() (same code)")
for g in (1.0, 2.0):
    c = mc.LinearSegmentedColormap('t', cdict, N=64, gamma=g)
    cr = c.reversed()
    xs = np.linspace(0, 1, 41)
    exp = [[float(seg_doc(1 - F(i, 63) ** (2 if g == 2 else 1), cdict[ch])) for ch in ('red', 'green', 'blue')]
           for i in range(64)]
    lr = cr(np.arange(64))[:, :3]
    if g == 1.0:
        report('LinearSegmentedColormap.reversed(): entry i == original entry N-1-i', allclose(lr, c(np.arange(64))[::-1, :3], 1e-12, 1e-12))
    else:
        mirror = c(np.arange(64))[::-1, :3]
        report('LinearSegmentedColormap(gamma=2).reversed(): reversed colour sequence == original read backwards',
               allclose(lr, mirror, 1e-9, 1e-9), f"maxdiff {maxdiff(lr, mirror):.3f}")
        info(f"reversed(gamma=2) equals f(1 - (i/(N-1))**2) (same gamma applied to the reversed data): maxdiff {maxdiff(lr, exp):.2g}")
c = mc.LinearSegmentedColormap('t', cdict, N=256, gamma=2.0)
c8 = resamp(c, 8)
exp = [[float(seg_doc(F(i, 7) ** 2, cdict[ch])) for ch in ('red', 'green', 'blue')] for i in range(8)]
d = maxdiff(c8(np.arange(8))[:, :3], exp)
report('LinearSegmentedColormap(gamma=2).resampled(8) keeps gamma: entry i = f((i/7)**2)', d < 1e-12, f"maxdiff {d:.3f}")
info(f"resampled gamma attr: {getattr(c8, '_gamma', None)}")
c = mc.LinearSegmentedColormap('t', cdict, N=256)
c8 = resamp(c, 8)
exp = [[float(seg_doc(F(i, 7), cdict[ch])) for ch in ('red', 'green', 'blue')] for i in range(8)]
report('LinearSegmentedColormap.resampled(8): entry i = f(i/7)', maxdiff(c8(np.arange(8))[:, :3], exp) < 1e-12)
lc = mc.ListedColormap(PAL[:5]).with_extremes(under=PAL[8], over=PAL[9], bad=PAL[10])
for k in (3, 5, 9, 12):
    rs = resamp(lc, k)
    exp = []
    for j in range(k):
        x = j / (k - 1) if k > 1 else 0.0
        if x == 1.0: exp.append(4)
        else:
            q = ex(x) * 5; exp.append(q.numerator // q.denominator)
    got = [which(rs(j), PAL[:11]) for j in range(k)]
    report(f'ListedColormap(5).resampled({k}): entry j = original colour at x=j/(k-1)', got == exp, f"got {got} exp {exp}")
rs = resamp(lc, 7)
report('ListedColormap.resampled keeps under/over/bad', [which(c, PAL[:11]) for c in rs(np.array([-1., 2., np.nan]))] == [8, 9, 10])
rv = lc.reversed()
got = [which(rv(i), PAL[:11]) for i in range(5)] + [which(c, PAL[:11]) for c in rv(np.array([-1., 2., np.nan]))]
report('ListedColormap.reversed(): colours reversed, under<->over swapped, bad kept', got == [4, 3, 2, 1, 0, 9, 8, 10], str(got))
lsc = mc.LinearSegmentedColormap('t', cdict, N=16).with_extremes(under=PAL[8], over=PAL[9])
rv = lsc.reversed()
report('LinearSegmentedColormap.reversed(): under<->over swapped', [which(c, PAL[:11]) for c in rv(np.array([-1., 2.]))] == [9, 8])

# ===================================================================== ScalarMappable / imshow end to end
print("#### ScalarMappable / imshow: is value v drawn in the colour the colorbar shows for v?")
cm8 = mc.ListedColormap(PAL[:8]).with_extremes(under=PAL[8], over=PAL[9], bad=PAL[10])
sm = mcm.ScalarMappable(norm=mc.Normalize(0, 8), cmap=cm8)
data = np.ma.array([0., 0.5, 1., 7.999, 8., 8.5, -0.5, np.nan, 3.], mask=[0, 0, 0, 0, 0, 0, 0, 0, 1])
got = [which(c, PAL[:11]) for c in sm.to_rgba(data)]
report('ScalarMappable.to_rgba(Normalize(0,8), 8 colours): edges left-closed, 8 -> last, >8 over, <0 under, NaN/masked bad',
       got == [0, 0, 1, 7, 7, 9, 8, 10, 10], str(got))
smb = mcm.ScalarMappable(norm=mc.BoundaryNorm([0, 1, 2, 3, 4], 4), cmap=mc.ListedColormap(PAL[:4]).with_extremes(bad=PAL[10], over=PAL[9]))
got = [which(c, PAL[:11]) for c in smb.to_rgba(np.array([0.5, np.nan, 3.5]))]
report('ScalarMappable.to_rgba(BoundaryNorm) on plain ndarray with NaN -> bad colour', got == [0, 10, 3], str(got))

def image_cells(data, px=20, **kw):
    """RGBA uint8 that AxesImage.make_image returns, sampled at each cell centre (1 row of cells)."""
    ncol = data.shape[1]
    fig = plt.figure(figsize=(ncol * px / 100, px / 100), dpi=100); ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off()
    im = ax.imshow(data, aspect='auto', interpolation='nearest', **kw)
    fig.canvas.draw()
    rgba = im.make_image(fig.canvas.get_renderer(), magnification=1.0, unsampled=False)[0]
    out = [tuple(int(c) for c in rgba[px // 2, j * px + px // 2]) for j in range(ncol)]
    plt.close(fig); return out, im
def byte_idx(px, cols):
    for i, c in enumerate(cols):
        if px == tuple(int(round(255 * v)) for v in rgba_of(c)): return i
    if px[3] == 0: return 'transparent'
    return px
cmI = mc.ListedColormap(PAL[:8]).with_extremes(under=PAL[8], over=PAL[9])
for px in (20, 5, 2):
    for (lab, off, dt) in (('float64', 0.0, np.float64), ('float64 offset 1e6', 1e6, np.float64),
                           ('float32', 0.0, np.float32), ('float32 offset 1024', 1024.0, np.float32),
                           ('float64 offset 1e12', 1e12, np.float64)):
        vals = [0, 0.5, 1, 2, 3, 3.75, 4, 5, 6, 7, 7.5, 8, 8.25, -0.25]
        d = (np.array(vals, dtype=np.float64) + off).astype(dt)[None, :]
        out, im = image_cells(d, px=px, cmap=cmI, vmin=off, vmax=off + 8)
        got = [byte_idx(p, PAL[:10]) for p in out]
        exp = [0, 0, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 9, 8]
        report(f'imshow {lab}, {px}px/cell, Normalize(vmin,vmin+8), 8 colours: values on edges -> upper band, vmax -> last',
               got == exp, f"got {got}")
# BoundaryNorm with non-dyadic boundaries, values exactly on them
bnd = np.array([0.0, 0.1, 0.2, 0.3, 0.7, 1.1, 1.3, 2.9, 3.0])
for px in (20, 2):
    for off in (0.0, 1000.0):
        bb = bnd + off
        vals = list(bb[:-1]) + [np.nextafter(bb[1], -np.inf), np.nextafter(bb[4], -np.inf), bb[-1]]
        exp = list(range(8)) + [0, 3, 'over']
        out, im = image_cells(np.array(vals)[None, :], px=px, cmap=cmI, norm=mc.BoundaryNorm(bb, 8))
        got = [byte_idx(p, PAL[:10]) for p in out]
        got = [('over' if g == 9 else g) for g in got]
        report(f'imshow BoundaryNorm (offset {off:g}, {px}px/cell): value == boundary[i] -> colour i; 1 ulp below -> i-1',
               got == exp, f"got {got}")
d = np.ma.array([[1., np.nan, 3., np.inf, -np.inf, 5.]], mask=[[0, 0, 0, 0, 0, 1]])
out, im = image_cells(d, cmap=cmI, vmin=0, vmax=8)
got = [byte_idx(p, PAL[:10]) for p in out]
report('imshow: NaN and masked cells are drawn transparent ("bad" default)', got[1] == 'transparent' and got[5] == 'transparent', str(got))
report('imshow: +inf cell -> "over" colour, -inf -> "under" ("bad" is for NaN or masked)', got[3] == 9 and got[4] == 8, str(got))
arr = im.get_array()
info(f"imshow stores +/-inf as masked: mask = {list(np.ma.getmaskarray(arr)[0])}")

# ===================================================================== colorbar
print("#### colorbar bands vs the norm")
def cbar_bands(mappable, fig, **kw):
    cb = fig.colorbar(mappable, **kw); fig.canvas.draw()
    co = cb.solids.get_coordinates(); edges = co[:, 0, 1] if cb.orientation == 'vertical' else co[0, :, 0]
    fc = cb.solids.get_facecolor()
    return cb, np.asarray(edges, float), fc
fig, ax = plt.subplots()
bb = [0, 1, 3, 4, 10, 11]
im = ax.imshow(np.arange(12.).reshape(3, 4), cmap=mc.ListedColormap(PAL[:5]), norm=mc.BoundaryNorm(bb, 5))
cb, edges, fc = cbar_bands(im, fig)
report('colorbar(BoundaryNorm): band edges == boundaries', allclose(edges, bb, 1e-12, 1e-12), str(list(edges)))
report('colorbar(BoundaryNorm): band i colour == documented colour of bin i', [which(c, PAL[:5]) for c in fc] == [0, 1, 2, 3, 4])
report('colorbar(BoundaryNorm): ticks at the boundaries', allclose(cb.get_ticks(), bb, 1e-12, 1e-12), str(list(cb.get_ticks())))
plt.close(fig)
fig, ax = plt.subplots()
bb = [0, 1, 2, 4, 8]
im = ax.imshow(np.arange(8.).reshape(2, 4), cmap=plt.get_cmap('viridis'), norm=mc.BoundaryNorm(bb, 256, extend='both'))
cb, edges, fc = cbar_bands(im, fig)
exp = [vir.colors[bn_doc((bb[i] + bb[i + 1]) / 2, bb, 256, extend='both')] for i in range(4)]
report('colorbar(BoundaryNorm, 256 colours, extend=both): band colours == documented stretched indices',
       allclose(np.asarray(fc)[:, :3], exp, 1e-12, 1e-12) and allclose(edges, bb, 1e-12, 1e-12))
plt.close(fig)
fig, ax = plt.subplots()
im = ax.imshow(np.arange(10.).reshape(2, 5), cmap=mc.ListedColormap(PAL[:5]), vmin=-1, vmax=4)
cb, edges, fc = cbar_bands(im, fig)
report('colorbar(Normalize(-1,4), 5 colours): band edges vmin + k*(vmax-vmin)/N', allclose(edges, [-1, 0, 1, 2, 3, 4], 1e-12, 1e-12), str(list(edges)))
report('colorbar(Normalize): band k colour == data colour for values in [edge_k, edge_k+1)',
       [which(c, PAL[:5]) for c in fc] == [0, 1, 2, 3, 4] and
       [which(c, PAL[:5]) for c in im.to_rgba(np.array([-1, -0.01, 0, 1.5, 3, 3.999]))] == [0, 0, 1, 2, 4, 4])
plt.close(fig)
fig, ax = plt.subplots()
im = ax.imshow(np.array([[1., 10., 100., 1000.]]), cmap=mc.ListedColormap(PAL[:3]), norm=mc.LogNorm(1, 1000))
cb, edges, fc = cbar_bands(im, fig)
report('colorbar(LogNorm(1,1000), 3 colours): band edges 1, 10, 100, 1000', allclose(edges, [1, 10, 100, 1000], 1e-12, 1e-12), str(list(edges)))
plt.close(fig)

# ===================================================================== contour / contourf
print("#### contour / contourf")
def bands(cs):
    if MV < (3, 8):
        return [c.get_facecolor()[0] for c in cs.collections], [list(c.get_paths()) for c in cs.collections]
    return list(cs.get_facecolor()), [[p] for p in cs.get_paths()]
def doc_count_bound():
    d = plt.Axes.contour.__doc__ or ''
    return 2 if 'n+2' in d else 1
NB = doc_count_bound()
info(f"this build's contour docstring promises at most n+{NB} levels")
def mant(step):
    e = math.floor(math.log10(step) + 1e-9); return round(step / 10 ** e, 6)
cnt_bad = []; cover_bad = []; nice_bad = []; mult_bad = []; tot = {}; mants = set()
for trial in range(300):
    lo = rng.choice([0, -1, 1e-3, 37.2, -1e4, 1e6]) + rng.uniform(-5, 5) * 10 ** rng.randint(-3, 3)
    span = rng.uniform(0.01, 100) * 10 ** rng.randint(-3, 3)
    nlev = rng.choice([None, 1, 2, 3, 4, 5, 6, 7, 9, 10, 15, 20])
    Z = np.array([[lo, lo + span * 0.3], [lo + span * 0.8, lo + span]])
    fig, ax = plt.subplots()
    cs = ax.contourf(Z) if nlev is None else ax.contourf(Z, nlev)
    L = np.asarray(cs.levels); plt.close(fig)
    n_ = 7 if nlev is None else nlev
    inside = int(((L >= Z.min()) & (L <= Z.max())).sum())
    if inside > n_ + NB: cnt_bad.append((n_, inside, len(L)))
    tot[len(L) - n_] = tot.get(len(L) - n_, 0) + 1
    if not (L[0] <= Z.min() and L[-1] >= Z.max()): cover_bad.append((Z.min(), Z.max(), L[0], L[-1]))
    st = np.diff(L); stp = float(np.median(st))
    if not np.allclose(st, stp, rtol=1e-6, atol=0): nice_bad.append(list(L))
    else:
        m = mant(stp); e = math.floor(math.log10(stp) + 1e-9); step = m * 10 ** e; mants.add(m)
        k = np.round(L / step)
        if not np.all(np.abs(L - k * step) <= 1e-9 * np.maximum(np.abs(L), step)): mult_bad.append(list(L))
for n_ in range(1, 13):
    for (z0, z1) in ((0, 10), (0, 1), (-3, 3), (100, 160)):
        fig, ax = plt.subplots(); L = np.asarray(ax.contourf(np.array([[z0, z1], [z1, z0]], float), n_).levels); plt.close(fig)
        inside = int(((L >= z0) & (L <= z1)).sum())
        if inside > n_ + NB: cnt_bad.append((n_, inside, len(L)))
report(f'contourf(Z, n) automatic levels: "no more than n+{NB}" levels between min(Z) and max(Z) (300 random ranges + 48 round ranges)',
       not cnt_bad, f"{len(cnt_bad)} exceed, e.g. (n, inside, total) {cnt_bad[:4]}")
info(f"total number of levels returned minus n (incl. the levels just outside the data): {dict(sorted(tot.items()))}")
report('contourf automatic levels span the data: levels[0] <= min(Z), levels[-1] >= max(Z)', not cover_bad, str(cover_bad[:3]))
report('contourf automatic levels are evenly spaced (MaxNLocator "Place evenly spaced ticks")', not nice_bad, str(nice_bad[:2]))
report('contourf automatic levels are integer multiples of the step ("acceptable tick multiples")', not mult_bad, f"{len(mult_bad)} of 300, e.g. " + str([[float(v) for v in L[:4]] for L in mult_bad[:2]]))
info(f"step mantissas seen: {sorted(mants)} (MaxNLocator default steps are not stated in its docstring)")
if MV < (3, 8) or NB == 1:
    hits = 0
    for n_ in range(1, 12):
        for span in (1, 3, 7, 9.5, 13, 17):
            fig, ax = plt.subplots(); cs = ax.contourf(np.array([[0, span], [span / 2, span]]), n_)
            if len(cs.levels) == n_ + 2: hits += 1
            plt.close(fig)
    info(f"n+2 levels returned in {hits} of 66 (n, span) grid cases")
fig, ax = plt.subplots(); cs = ax.contourf(np.array([[0., 0.1], [0.2, 0.95]]))
info(f"contourf default levels for Z in [0, 0.95]: {list(cs.levels)}"); plt.close(fig)
# fill geometry on a ramp: band [l_i, l_{i+1}] spans exactly x in [l_i, l_{i+1}]
x = np.linspace(0, 10, 41); X, Y = np.meshgrid(x, [0, 1, 2]); Z = X.copy()
lev = [0, 1, 2.5, 6, 10]
fig, ax = plt.subplots(); cs = ax.contourf(X, Y, Z, levels=lev, cmap=mc.ListedColormap(PAL[:4]))
fcs, pths = bands(cs)
ext = [(min(p.vertices[:, 0].min() for p in ps), max(p.vertices[:, 0].max() for p in ps)) for ps in pths]
report('contourf on Z = x: band i covers exactly x in [levels[i], levels[i+1]]',
       all(close(a, lev[i], 1e-12, 1e-12) and close(b, lev[i + 1], 1e-12, 1e-12) for i, (a, b) in enumerate(ext)), str(ext))
mids = [(lev[i] + lev[i + 1]) / 2 for i in range(4)]
exp = []
for m in mids:
    q = (F(m) - F(lev[0])) / (F(lev[-1]) - F(lev[0])) * 4; exp.append(q.numerator // q.denominator)
report('contourf band colour with ListedColormap = colour at the layer midpoint (Normalize(levels[0], levels[-1]))',
       [which(c, PAL[:4]) for c in fcs] == exp, f"got {[which(c, PAL[:4]) for c in fcs]} doc {exp}")
info(f"levels {lev} with 4 listed colours -> band colours {[which(c, PAL[:4]) for c in fcs]} (colour 2 unused, bands 0/1 share colour 0)")
cb, edges, fc = cbar_bands(cs, fig)
report('colorbar(contourf): band edges == contour levels', allclose(edges, lev, 1e-12, 1e-12), str(list(edges)))
report('colorbar(contourf): band colours == contourf band colours', [which(c, PAL[:4]) for c in fc] == [which(c, PAL[:4]) for c in fcs])
plt.close(fig)
# equal levels with ListedColormap of the same length: band i -> colour i
fig, ax = plt.subplots(); cs = ax.contourf(X, Y, Z, levels=[0, 2, 4, 6, 8, 10], cmap=mc.ListedColormap(PAL[:5]))
report('contourf 5 equal bands, 5-colour ListedColormap: band i -> colour i', [which(c, PAL[:5]) for c in bands(cs)[0]] == [0, 1, 2, 3, 4])
plt.close(fig)
# colors=
fig, ax = plt.subplots(); cs = ax.contourf(X, Y, Z, levels=[0, 2, 4, 6, 8, 10], colors=PAL[:3])
report('contourf colors=3 colours, 5 bands: "the sequence is cycled ... repeated" -> 0,1,2,0,1',
       [which(c, PAL[:3]) for c in bands(cs)[0]] == [0, 1, 2, 0, 1], str([which(c, PAL[:3]) for c in bands(cs)[0]]))
plt.close(fig)
# extend with set_under / set_over
cmE = mc.ListedColormap(PAL[:3]).with_extremes(under=PAL[8], over=PAL[9])
fig, ax = plt.subplots(); cs = ax.contourf(X, Y, Z, levels=[2, 4, 6, 8], cmap=cmE, extend='both')
fcs, pths = bands(cs)
report('contourf extend=both: below/above bands use the colormap under/over colours',
       [which(c, PAL[:10]) for c in fcs] == [8, 0, 1, 2, 9], str([which(c, PAL[:10]) for c in fcs]))
ext = [(min(p.vertices[:, 0].min() for p in ps), max(p.vertices[:, 0].max() for p in ps)) if ps and len(ps[0].vertices) else None for ps in pths]
report('contourf extend=both: under band covers x in [0,2], over band x in [8,10]',
       ext[0] is not None and close(ext[0][0], 0) and close(ext[0][1], 2) and close(ext[-1][0], 8) and close(ext[-1][1], 10), str(ext))
plt.close(fig)
fig, ax = plt.subplots(); cs = ax.contourf(X, Y, Z, levels=[2, 4, 6, 8], colors=PAL[:5], extend='both')
report('contourf colors= with len == bands+2 and extend=both: first/last colours for under/over',
       [which(c, PAL[:5]) for c in bands(cs)[0]] == [0, 1, 2, 3, 4], str([which(c, PAL[:5]) for c in bands(cs)[0]]))
plt.close(fig)
fig, ax = plt.subplots(); cs = ax.contourf(X, Y, Z, levels=[2, 4, 6, 8], cmap=cmE, extend='neither')
_, pths = bands(cs)
ext = [(min(p.vertices[:, 0].min() for p in ps), max(p.vertices[:, 0].max() for p in ps)) for ps in pths]
report('contourf extend=neither: "values outside the levels range are not colored" (fill only x in [2,8])',
       close(ext[0][0], 2) and close(ext[-1][1], 8), str(ext))
plt.close(fig)
# fill rule z1 < Z <= z2 at plateaus exactly on a level
def contains(paths, pt): return any(p.contains_point(pt) for p in paths)
Zp = np.full((7, 7), 1.0); Zp[0, :] = 0.0; Zp[-1, :] = 2.0
fig, ax = plt.subplots(); cs = ax.contourf(Zp, levels=[0, 1, 2]); _, pths = bands(cs)
inb = [contains(ps, (3, 3)) for ps in pths]
report('contourf fill rule "z1 < Z <= z2": plateau Z == 1 with levels [0,1,2] lies in band [0,1]', inb == [True, False], str(inb))
plt.close(fig)
Zp = np.full((7, 7), 0.0); Zp[-1, :] = 2.0
fig, ax = plt.subplots(); cs = ax.contourf(Zp, levels=[0, 1, 2]); _, pths = bands(cs)
inb = [contains(ps, (3, 3)) for ps in pths]
report('contourf: plateau at Z == min(Z) == levels[0] is filled ("lowest interval ... closed on both sides")', inb == [True, False], str(inb))
plt.close(fig)
Zp = np.full((7, 7), 0.0); Zp[-1, :] = 2.0; Zp[0, :] = -1.0
fig, ax = plt.subplots(); cs = ax.contourf(Zp, levels=[0, 1, 2]); _, pths = bands(cs)
inb = [contains(ps, (3, 3)) for ps in pths]
report('contourf: plateau Z == levels[0] when min(Z) < levels[0] is filled in the lowest band '
       '("closed on both sides (i.e. it includes the lowest value)")', inb == [True, False], str(inb))
plt.close(fig)
Zp = np.full((7, 7), 0.0); Zp[-1, :] = 2.0; Zp[0, :] = -1.0
fig, ax = plt.subplots(); cs = ax.contourf(Zp, levels=[0, 1, 2], extend='min', cmap=cmE); fcs, pths = bands(cs)
inb = [contains(ps, (3, 3)) for ps in pths]
info(f"same plateau with extend='min': membership (under, [0,1], [1,2]) = {inb}; under colour = {which(fcs[0], PAL[:10])}")
plt.close(fig)
Zp = np.full((7, 7), 2.0); Zp[0, :] = 0.0
fig, ax = plt.subplots(); cs = ax.contourf(Zp, levels=[0, 1, 2]); _, pths = bands(cs)
inb = [contains(ps, (3, 3)) for ps in pths]
report('contourf: plateau Z == levels[-1] lies in the top band (closed at the top)', inb == [False, True], str(inb))
plt.close(fig)
# extend changes autolevel trimming
Zr = np.array([[0.3, 4.7], [2.0, 9.6]])
fig, ax = plt.subplots(); L0 = np.asarray(ax.contourf(Zr, 5).levels); Lb = np.asarray(ax.contourf(Zr, 5, extend='both').levels); plt.close(fig)
info(f"auto levels n=5 for Z in [0.3, 9.6]: neither {list(L0)}, extend=both {list(Lb)}")
report('contourf extend=both auto levels lie inside [min Z, max Z] (data beyond go to the extensions)',
       Lb[0] >= Zr.min() and Lb[-1] <= Zr.max(), str(list(Lb)))
# constant Z
fig, ax = plt.subplots()
try:
    cs = ax.contourf(np.full((3, 3), 5.0)); info(f"contourf(constant 5): levels {list(cs.levels)}")
except Exception as e:
    info(f"contourf(constant 5) raises {type(e).__name__}")
plt.close(fig)
# masked / NaN Z: levels from the finite values
Zm = np.array([[0., 1., np.nan], [2., 3., 4.], [5., 6., 7.]])
fig, ax = plt.subplots(); cs = ax.contourf(Zm, 7); L = np.asarray(cs.levels); plt.close(fig)
report('contourf with NaN in Z: automatic levels span the finite values [0, 7]', L[0] <= 0 and L[-1] >= 7 and np.isfinite(L).all(), str(list(L)))
# line contour colours at levels
fig, ax = plt.subplots(); cs = ax.contour(X, Y, Z, levels=[1, 3, 5, 7, 9], cmap=mc.ListedColormap(PAL[:4]))
lc = bands(cs)[0] if MV >= (3, 8) else [c.get_edgecolor()[0] for c in cs.collections]
if MV >= (3, 8): lc = list(cs.get_edgecolor())
exp = []
for v in [1, 3, 5, 7, 9]:
    q = (F(v) - 1) / 8 * 4; i = min(q.numerator // q.denominator, 3); exp.append(i)
report('contour line colours = colormap at Normalize(levels[0], levels[-1])(level)', [which(c, PAL[:4]) for c in lc] == exp,
       f"got {[which(c, PAL[:4]) for c in lc]} doc {exp}")
plt.close(fig)
print("done")
