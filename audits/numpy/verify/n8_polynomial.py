#!/usr/bin/env python
"""NumPy polynomial packages against exact recomputations (n2 covered the basic
np.polyfit coefficients / residual / cov / weights). numpy.polynomial: the six
series kinds (power, Chebyshev, Legendre, Hermite, HermiteE, Laguerre) through
their module functions -- *val / *val2d / *val3d / *grid2d / *grid3d against the
basis recurrences evaluated in mpmath at points inside and outside [-1, 1],
*vander / *vander2d / *vander3d, *fit (integer deg, list of degrees, weights,
full=True, rcond default), *roots / *companion against mpmath.polyroots,
*fromroots / *der / *int / *add / *sub / *mul / *mulx / *div / *pow / *line and
the poly2cheb ... lag2poly conversions against fractions.Fraction, *gauss
quadrature (nodes = mpmath roots of the basis polynomial, exact integration of
monomials to degree 2n-1 against closed-form moments), *weight, chebinterpolate,
trimcoef / trimseq / as_series, mapdomain / mapparms / getdomain -- and the
ABCPolyBase classes (domain/window mapping in __call__, fit + convert round
trips, exact least squares through convert().coef, deriv / integ chain rule
with a non-trivial window, roots on a mapped domain, mismatched-domain
TypeError, mapparms, linspace, degree / cutdeg / truncate / trim, equality,
copy, basis / identity / fromroots / cast, __repr__ / __str__ / __format__ and
set_default_printstyle, maxpower).  Legacy API: poly1d (highest-first
coefficients, r / c / o / order / variable, indexing, arithmetic, deriv /
integ, roots), np.polyval Horner, np.roots (leading zeros stripped, trailing
zeros -> zero roots, degree 0 / 1), np.polyder / np.polyint (k list semantics),
np.polymul / polydiv / polyadd / polysub, np.poly (conjugate pairs -> real,
characteristic polynomial), np.polyfit (deg 0 covariance, full=True, complex y,
int y, weights, 2-D y, RankWarning on years 2000-2020, coefficient order vs
numpy.polynomial.polynomial.polyfit), np.vander(increasing=).  Truths: mpmath
at 50 digits (basis recurrences, polyroots, closed-form moments) and
fractions.Fraction (exact polynomial algebra and normal-equation least
squares).  No scipy anywhere."""
import sys, math, cmath, warnings, functools, random
from fractions import Fraction as F
import numpy as np
import mpmath as mp
mp.mp.dps = 50
MAJOR, MINOR = [int(x) for x in np.__version__.split('.')[:2]]
NP2 = MAJOR >= 2; V124 = (MAJOR, MINOR) >= (1, 24); V125 = (MAJOR, MINOR) >= (1, 25)
RankWarning = getattr(getattr(np, "exceptions", None), "RankWarning", None) or getattr(np, "RankWarning", None) or np.polynomial.polyutils.RankWarning
from numpy.polynomial import polynomial as PM, chebyshev as CM, legendre as LM, hermite as HM, hermite_e as HEM, laguerre as LAM
from numpy.polynomial import Polynomial, Chebyshev, Legendre, Hermite, HermiteE, Laguerre, polyutils as pu
def banner(): print(f"numpy {np.__version__}  mpmath {mp.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-10, abs_=1e-300):
    if isinstance(a, complex) or isinstance(b, complex) or np.iscomplexobj(a) or np.iscomplexobj(b):
        a = complex(a); b = complex(b); return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
def allclose(a, b, rel=1e-10, abs_=1e-300):
    a = np.asarray(a, dtype=object).ravel().tolist(); b = np.asarray(b, dtype=object).ravel().tolist()
    return len(a) == len(b) and all(close(x, y, rel, abs_) for x, y in zip(a, b))
def maxrel(a, b):
    a = np.asarray(a, dtype=float).ravel(); b = np.asarray(b, dtype=float).ravel()
    return float(np.max(np.abs(a - b) / np.maximum(np.abs(b), 1e-300))) if a.size else 0.0
def raises(fn, exc):
    try: fn(); return False
    except exc: return True
def match_err(w, wt):
    """greedy nearest-neighbour matching of two root multisets; max absolute distance"""
    wt = [complex(v) for v in wt]; err = 0.0
    for x in [complex(v) for v in w]:
        d = [abs(x - y) for y in wt]; j = int(np.argmin(d)); err = max(err, d[j]); wt.pop(j)
    return err
warnings.filterwarnings("ignore")
rng = random.Random(8)

# ---------------------------------------------------------------- exact polynomial algebra (power basis, low -> high, Fractions)
def FR(v): return F(v) if not isinstance(v, F) else v
def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a
def padd(a, b):
    n = max(len(a), len(b)); return [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(n)]
def pscale(a, s): return [x * s for x in a]
def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return out
def ppow(a, n):
    out = [F(1)]
    for _ in range(n): out = pmul(out, a)
    return out
def pder(a): return [i * a[i] for i in range(1, len(a))] or [F(0)]
def pint(a): return [F(0)] + [a[i] / (i + 1) for i in range(len(a))]
def peval(a, x):
    y = 0
    for c in reversed(a): y = y * x + c
    return y
def pdivmod(a, b):
    a = ptrim(a); b = ptrim(b)
    if len(a) < len(b): return [F(0)], a
    q = [F(0)] * (len(a) - len(b) + 1); r = list(a)
    for i in range(len(q) - 1, -1, -1):
        q[i] = r[i + len(b) - 1] / b[-1]
        for j in range(len(b)): r[i + j] -= q[i] * b[j]
    return q, ptrim(r[:len(b) - 1] or [F(0)])
def pcompose(a, inner):
    """a(inner(x)) exactly"""
    out = [F(0)]
    for c in reversed(a): out = padd(pmul(out, inner), [c])
    return out
def fromroots_exact(roots):
    out = [F(1)]
    for r in roots: out = pmul(out, [-FR(r), F(1)])
    return out

# basis polynomials of each kind in exact power form, from the recurrences
KINDS = {"poly": (PM, "poly", Polynomial), "cheb": (CM, "cheb", Chebyshev), "leg": (LM, "leg", Legendre),
         "herm": (HM, "herm", Hermite), "herme": (HEM, "herme", HermiteE), "lag": (LAM, "lag", Laguerre)}
def fn(kind, name): mod, pre, _ = KINDS[kind]; return getattr(mod, pre + name)
@functools.lru_cache(None)
def basis(kind, n):
    if n == 0: return (F(1),)
    if n == 1: return tuple(F(v) for v in {"poly": (0, 1), "cheb": (0, 1), "leg": (0, 1), "herm": (0, 2), "herme": (0, 1), "lag": (1, -1)}[kind])
    a = list(basis(kind, n - 1)); b = list(basis(kind, n - 2)); m = n - 1; xa = [F(0)] + a
    if kind == "poly": r = xa
    elif kind == "cheb": r = padd(pscale(xa, 2), pscale(b, -1))
    elif kind == "leg": r = pscale(padd(pscale(xa, 2 * m + 1), pscale(b, -m)), F(1, m + 1))
    elif kind == "herm": r = padd(pscale(xa, 2), pscale(b, -2 * m))
    elif kind == "herme": r = padd(xa, pscale(b, -m))
    else: r = pscale(padd(padd(pscale(a, 2 * m + 1), pscale(xa, -1)), pscale(b, -m)), F(1, m + 1))
    return tuple(r)
def mp_basis(kind, n, x):
    """the same recurrences evaluated directly in mpmath at x (independent of the exact power form)"""
    x = mp.mpf(x) if not isinstance(x, mp.mpc) else x
    b0, b1 = mp.mpf(1), {"poly": x, "cheb": x, "leg": x, "herm": 2 * x, "herme": x, "lag": 1 - x}[kind]
    if n == 0: return b0
    for m in range(1, n):
        if kind == "poly": b2 = x * b1
        elif kind == "cheb": b2 = 2 * x * b1 - b0
        elif kind == "leg": b2 = ((2 * m + 1) * x * b1 - m * b0) / (m + 1)
        elif kind == "herm": b2 = 2 * x * b1 - 2 * m * b0
        elif kind == "herme": b2 = x * b1 - m * b0
        else: b2 = ((2 * m + 1 - x) * b1 - m * b0) / (m + 1)
        b0, b1 = b1, b2
    return b1
def mp_series(kind, c, x): return sum(mp.mpf(FR(ci).numerator) / FR(ci).denominator * mp_basis(kind, i, x) for i, ci in enumerate(c))
def from_basis(kind, c):
    out = [F(0)]
    for i, ci in enumerate(c): out = padd(out, pscale(list(basis(kind, i)), FR(ci)))
    return out
def to_basis(kind, p):
    p = [FR(v) for v in p]; c = [F(0)] * len(p)
    for n in range(len(p) - 1, -1, -1):
        B = list(basis(kind, n)); c[n] = p[n] / B[n]; p = padd(p, pscale(B, -c[n]))
    return c
def fl(seq): return np.array([float(v) for v in seq])                                   # ndarray: 1.x series __call__ rejects lists
def mp_roots(p):
    """roots of an exact power-form polynomial (low -> high) at high precision"""
    p = ptrim(p); hi = [mp.mpf(v.numerator) / v.denominator for v in reversed(p)]
    return [complex(r) for r in mp.polroots(hi, maxsteps=500, extraprec=800)] if False else [complex(r) for r in mp.polyroots(hi, maxsteps=500, extraprec=800)]
def lstsq_exact(rows, y, w=None):
    """exact weighted normal equations: minimise sum (w_i (y_i - sum_j c_j rows[i][j]))^2"""
    m = len(rows[0]); w2 = [FR(v) ** 2 for v in w] if w is not None else [F(1)] * len(rows)
    A = [[sum(w2[r] * rows[r][i] * rows[r][j] for r in range(len(rows))) for j in range(m)] for i in range(m)]
    b = [sum(w2[r] * rows[r][i] * FR(y[r]) for r in range(len(rows))) for i in range(m)]
    M = [A[i] + [b[i]] for i in range(m)]
    for c in range(m):
        piv = next(r for r in range(c, m) if M[r][c] != 0); M[c], M[piv] = M[piv], M[c]
        M[c] = [v / M[c][c] for v in M[c]]
        for r in range(m):
            if r != c and M[r][c] != 0: M[r] = [a - M[r][c] * bb for a, bb in zip(M[r], M[c])]
    return [M[i][m] for i in range(m)]

banner()
print("#### module functions of the six series kinds")
XPTS = [F(-3), F(-1), F(-1, 2), F(0), F(3, 10), F(1), F(5, 2), F(10)]           # inside and outside [-1, 1]
XF = [float(v) for v in XPTS]
for kind in KINDS:
    mod, pre, cls = KINDS[kind]
    c = [rng.randint(-5, 5) for _ in range(5)] + [rng.choice([-3, -2, 2, 3])]     # degree 5
    # ---- *val against the mpmath recurrence
    v = fn(kind, "val")(XF, c)
    truth = [mp_series(kind, c, x) for x in XPTS]
    err = max(abs(float(a) - float(b)) / max(abs(float(b)), 1e-300) for a, b in zip(v, truth))
    report(f"{pre}val(x, c) = sum c_i B_i(x) from the recurrence in mpmath at x in {XF}", err < 1e-12, f"(max rel err {err:.1e}; c={c})")
    report(f"{pre}val scalar x returns a 0-d result equal to the mpmath value", np.ndim(fn(kind, "val")(2.5, c)) == 0 and close(fn(kind, "val")(2.5, c), truth[6], 1e-12))
    xc = complex(0.5, 1.5); vc = fn(kind, "val")(xc, c); tc = mp_series(kind, c, mp.mpc(0.5, 1.5))
    report(f"{pre}val at a complex point equals the recurrence with complex x", close(vc, complex(tc), 1e-12))
    # 2-D c: tensor semantics
    c2 = np.array([c, [1, 0, -1, 2, 0, 1]]).T                                       # shape (6, 2): two series
    vt = fn(kind, "val")(XF, c2); vf = fn(kind, "val")(XF[:2], c2, tensor=False)
    report(f"{pre}val(x, c 2-D, tensor=True): shape c.shape[1:] + x.shape, column k evaluated at every x", vt.shape == (2, len(XF)) and allclose(vt[1], [mp_series(kind, c2[:, 1].tolist(), x) for x in XPTS], 1e-12))
    report(f"{pre}val(tensor=False): shape c.shape[1:], column k evaluated at x[k]", vf.shape == (2,) and close(vf[1], mp_series(kind, c2[:, 1].tolist(), XPTS[1]), 1e-12))
    # ---- 2-D / 3-D evaluation and grids
    c2d = np.array([[rng.randint(-3, 3) for _ in range(3)] for _ in range(4)], dtype=float)   # (4, 3)
    xs = [F(-2), F(1, 2), F(3)]; ys = [F(2), F(-1, 4), F(7, 2)]
    def s2d(x, y): return sum(F(int(c2d[i, j])) * peval(basis(kind, i), x) * peval(basis(kind, j), y) for i in range(4) for j in range(3))
    v2 = fn(kind, "val2d")(fl(xs), fl(ys), c2d)
    report(f"{pre}val2d(x, y, c) = sum c_ij B_i(x) B_j(y) exactly (Fraction)", allclose(v2, [s2d(x, y) for x, y in zip(xs, ys)], 1e-12))
    g2 = fn(kind, "grid2d")(fl(xs), fl(ys[:2]), c2d)
    report(f"{pre}grid2d: shape x.shape + y.shape, entry [i, j] = p(x[i], y[j])", g2.shape == (3, 2) and allclose(g2, [[s2d(x, y) for y in ys[:2]] for x in xs], 1e-12))
    c3d = np.array([[[rng.randint(-2, 2) for _ in range(2)] for _ in range(3)] for _ in range(3)], dtype=float)  # (3, 3, 2)
    zs = [F(1), F(-3, 2), F(1, 5)]
    def s3d(x, y, z): return sum(F(int(c3d[i, j, k])) * peval(basis(kind, i), x) * peval(basis(kind, j), y) * peval(basis(kind, k), z) for i in range(3) for j in range(3) for k in range(2))
    v3 = fn(kind, "val3d")(fl(xs), fl(ys), fl(zs), c3d)
    report(f"{pre}val3d(x, y, z, c) = sum c_ijk B_i(x) B_j(y) B_k(z) exactly", allclose(v3, [s3d(x, y, z) for x, y, z in zip(xs, ys, zs)], 1e-12))
    g3 = fn(kind, "grid3d")(fl(xs[:2]), fl(ys), fl(zs[:1]), c3d)
    report(f"{pre}grid3d: shape x.shape + y.shape + z.shape on the Cartesian product", g3.shape == (2, 3, 1) and allclose(g3, [[[s3d(x, y, z) for z in zs[:1]] for y in ys] for x in xs[:2]], 1e-12))
    # ---- vander
    V = fn(kind, "vander")(XF, 5)
    report(f"{pre}vander(x, 5): V[..., i] = B_i(x) (recurrence in mpmath), shape x.shape + (6,)", V.shape == (len(XF), 6) and all(close(V[r, i], mp_basis(kind, i, XPTS[r]), 1e-12) for r in range(len(XF)) for i in range(6)))
    V2 = fn(kind, "vander2d")(fl(xs), fl(ys), [3, 2])
    report(f"{pre}vander2d(x, y, [3, 2]): column (deg[1]+1)*i + j = B_i(x) B_j(y); V @ c.flat = val2d", V2.shape == (3, 12) and all(close(V2[r, 3 * i + j], peval(basis(kind, i), xs[r]) * peval(basis(kind, j), ys[r]), 1e-12) for r in range(3) for i in range(4) for j in range(3)) and allclose(V2 @ c2d.ravel(), v2, 1e-12))
    V3 = fn(kind, "vander3d")(fl(xs), fl(ys), fl(zs), [2, 2, 1])
    report(f"{pre}vander3d(x, y, z, [2, 2, 1]): column (d1+1)(d2+1) i + (d2+1) j + k = B_i(x) B_j(y) B_k(z); V @ c.flat = val3d", V3.shape == (3, 18) and all(close(V3[r, 6 * i + 2 * j + k], peval(basis(kind, i), xs[r]) * peval(basis(kind, j), ys[r]) * peval(basis(kind, k), zs[r]), 1e-12) for r in range(3) for i in range(3) for j in range(3) for k in range(2)) and allclose(V3 @ c3d.ravel(), v3, 1e-12))
    # ---- fit against exact normal equations in this basis
    xf = [F(i, 4) for i in range(-6, 13)]; yf = [F(i * i * i, 8) - F(3 * i, 2) + F((i * 7) % 5, 3) for i in range(-6, 13)]
    rows = [[peval(basis(kind, j), x) for j in range(4)] for x in xf]
    ce = lstsq_exact(rows, yf)
    cf = fn(kind, "fit")(fl(xf), fl(yf), 3)
    report(f"{pre}fit(x, y, deg=3) = exact least-squares coefficients in the {pre} basis (Fraction normal equations)", allclose(cf, ce, 1e-9), f"(max rel err {maxrel(cf, ce):.1e})")
    cf2, (resid, rank, sv, rc) = fn(kind, "fit")(fl(xf), fl(yf), 3, full=True)
    rss = sum((y - sum(ce[j] * r[j] for j in range(4))) ** 2 for r, y in zip(rows, yf))
    report(f"{pre}fit(full=True): [resid, rank, sv, rcond] with resid = sum of squared residuals, rank 4, 4 singular values, rcond = len(x)*eps", close(resid[0], rss, 1e-8) and rank == 4 and len(sv) == 4 and rc == len(xf) * np.finfo(float).eps, f"(resid {float(resid[0]):.6g} exact {float(rss):.6g})")
    degs = [0, 2, 3]; rows_l = [[peval(basis(kind, j), x) for j in degs] for x in xf]; ce_l = lstsq_exact(rows_l, yf)
    cfl = fn(kind, "fit")(fl(xf), fl(yf), degs)
    report(f"{pre}fit(deg=[0, 2, 3]): 'only those terms' -- coefficient of degree 1 exactly 0, the rest the exact LS over B_0, B_2, B_3", len(cfl) == 4 and cfl[1] == 0 and allclose([cfl[0], cfl[2], cfl[3]], ce_l, 1e-9))
    wts = [F(1 + (i % 3)) for i in range(len(xf))]; ce_w = lstsq_exact(rows, yf, wts)
    cfw = fn(kind, "fit")(fl(xf), fl(yf), 3, w=fl(wts))
    report(f"{pre}fit(w=): 'weight w[i] applies to the unsquared residual' -> minimises sum (w_i r_i)^2 (normal equations with w^2)", allclose(cfw, ce_w, 1e-9))
    y2 = np.array([fl(yf), fl([v * 2 + 1 for v in yf])]).T; cf2d = fn(kind, "fit")(fl(xf), y2, 3)
    report(f"{pre}fit with 2-D y: one fit per column, coefficients in the columns", cf2d.shape == (4, 2) and allclose(cf2d[:, 0], ce, 1e-9) and allclose(cf2d[:, 1], [2 * v for v in ce[:1]] + [2 * v for v in ce[1:]] if False else lstsq_exact(rows, [v * 2 + 1 for v in yf]), 1e-9))
    # ---- roots / companion against mpmath.polyroots of the exact power form
    pw = from_basis(kind, c); rt = mp_roots(pw); r = fn(kind, "roots")(c)
    scale = max(abs(z) for z in rt)
    report(f"{pre}roots(c) = mpmath.polyroots of the equivalent power series (degree 5, {sum(abs(z.imag) > 1e-12 for z in rt)} complex)", len(r) == 5 and match_err(r, rt) <= 1e-9 * scale, f"(max abs err {match_err(r, rt):.1e}, |root| <= {scale:.3g})")
    creal = to_basis(kind, fromroots_exact([F(-3, 2), F(-1, 3), F(1, 2), F(2)]))
    rr = fn(kind, "roots")(fl(creal))
    report(f"{pre}roots: 'if all the roots are real then out is also real' (roots -3/2, -1/3, 1/2, 2)", not np.iscomplexobj(rr) and allclose(sorted(rr), [-1.5, -1 / 3, 0.5, 2], 1e-9))
    A = fn(kind, "companion")(c); ev = np.linalg.eigvals(A)
    report(f"{pre}companion(c): (deg, deg) matrix whose eigenvalues are the roots (vs mpmath)", A.shape == (5, 5) and match_err(ev, rt) <= 1e-9 * scale)
    if kind != "poly":
        report(f"{pre}companion of the basis polynomial B_6 is symmetric (documented: 'scaled to be symmetric')", np.allclose(fn(kind, "companion")([0] * 6 + [1]), fn(kind, "companion")([0] * 6 + [1]).T, atol=1e-14))
    # ---- fromroots exact
    roots_ = [F(-2), F(1, 2), F(3), F(-1, 4)]
    fr = fn(kind, "fromroots")(fl(roots_)); fr_e = to_basis(kind, fromroots_exact(roots_))
    report(f"{pre}fromroots: product (x - r_i) expanded exactly in the {pre} basis", allclose(fr, fr_e, 1e-12), f"(coef {np.round(fr, 6).tolist()})")
    frc = fn(kind, "fromroots")([1j, -1j, 2])
    report(f"{pre}fromroots with complex roots returns a complex array (documented) whose values are the exact real expansion", np.iscomplexobj(frc) and allclose(frc.real, to_basis(kind, pmul([F(1), F(0), F(1)], [F(-2), F(1)])), 1e-12) and np.max(np.abs(frc.imag)) < 1e-14)
    # ---- der / int exact
    d2 = fn(kind, "der")(c, 2, scl=3); d2_e = to_basis(kind, pscale(pder(pder(pw)), 9))
    report(f"{pre}der(c, m=2, scl=3): exact second derivative times scl**2 (documented 'multiplication by scl**m')", allclose(d2, ptrim(d2_e), 1e-12))
    report(f"{pre}der(c, 0) returns c unchanged; der beyond the degree gives [0]", allclose(fn(kind, "der")(c, 0), c) and fn(kind, "der")(c, 7).tolist() == [0.0])
    m, k, lbnd, scl = 2, [F(1), F(-2)], F(1, 2), F(3)
    pe = list(pw)
    for i in range(m):
        pe = pscale(pint(pe), scl); pe[0] += k[i] - peval(pe, lbnd)
    i2 = fn(kind, "int")(c, m=m, k=fl(k), lbnd=float(lbnd), scl=float(scl)); i2_e = to_basis(kind, pe)
    report(f"{pre}int(c, m=2, k=[1,-2], lbnd=1/2, scl=3): each step = scl * antiderivative, then constant so the value at lbnd is k[i]", allclose(i2, i2_e, 1e-11), f"(max rel err {maxrel(i2, i2_e):.1e})")
    i1 = fn(kind, "int")(c, k=[F(7, 3)], lbnd=-1.5)
    report(f"{pre}int(c, k=7/3, lbnd=-1.5): value of the integral at lbnd equals k", close(fn(kind, "val")(-1.5, i1), 7 / 3, 1e-10) and allclose(fn(kind, "der")(i1), c, 1e-12))
    report(f"{pre}int: default lbnd=0, k=[] -> value 0 at 0; m=0 leaves c unchanged", close(fn(kind, "val")(0.0, fn(kind, "int")(c)), 0.0, 1e-10, 1e-13) and allclose(fn(kind, "int")(c, 0), c))
    report(f"{pre}int raises ValueError for len(k) > m and for scl / lbnd non-scalar", raises(lambda: fn(kind, "int")(c, 1, k=[1, 2]), ValueError) and raises(lambda: fn(kind, "int")(c, lbnd=[0, 1]), ValueError))
    # ---- arithmetic exact
    ca = [rng.randint(-4, 4) for _ in range(4)] + [2]; cb = [rng.randint(-4, 4) for _ in range(2)] + [3]
    pa, pb = from_basis(kind, ca), from_basis(kind, cb)
    report(f"{pre}add / sub of different lengths: exact (aligned at the low end)", allclose(fn(kind, "add")(ca, cb), to_basis(kind, padd(pa, pb)), 1e-12) and allclose(fn(kind, "sub")(cb, ca), to_basis(kind, padd(pb, pscale(pa, -1))), 1e-12))
    report(f"{pre}mul: exact product expanded in the {pre} basis (linearisation)", allclose(fn(kind, "mul")(ca, cb), to_basis(kind, pmul(pa, pb)), 1e-12))
    report(f"{pre}mulx: multiplication by x exact (uses the recurrence)", allclose(fn(kind, "mulx")(ca), to_basis(kind, [F(0)] + pa), 1e-12))
    q, r_ = fn(kind, "div")(ca, cb); qe, re_ = pdivmod(pa, pb)
    report(f"{pre}div: quotient and remainder exact (deg rem < deg divisor)", allclose(q, ptrim(to_basis(kind, qe)), 1e-11) and allclose(r_, ptrim(to_basis(kind, re_)), 1e-11), f"(quotient {np.round(q, 6).tolist()}, remainder {np.round(r_, 6).tolist()})")
    report(f"{pre}div by a higher-degree series: quotient [0], remainder the dividend", fn(kind, "div")(cb, ca)[0].tolist() == [0.0] and allclose(fn(kind, "div")(cb, ca)[1], cb))
    report(f"{pre}pow(c, 3) exact; pow(c, 0) = [1]; pow > maxpower raises ValueError", allclose(fn(kind, "pow")(cb, 3), to_basis(kind, ppow(pb, 3)), 1e-12) and fn(kind, "pow")(cb, 0).tolist() == [1.0] and raises(lambda: fn(kind, "pow")(cb, 5, maxpower=4), ValueError))
    ln = fn(kind, "line")(2.5, -1.5)
    report(f"{pre}line(off=2.5, scl=-1.5) represents off + scl*x (exact in the {pre} basis)", allclose(ln, to_basis(kind, [F(5, 2), F(-3, 2)]), 1e-14) and close(fn(kind, "val")(3.0, ln), 2.5 - 4.5, 1e-14))
    report(f"{pre}line(off, 0) is the constant [off]", fn(kind, "line")(4, 0).tolist() == [4.0])
    # ---- conversions to and from the power basis
    if kind != "poly":
        cp = [3, -1, 2, 5, -4, 1]
        report(f"poly2{pre}([3,-1,2,5,-4,1]) exact (Fraction) and {pre}2poly inverts it", allclose(getattr(mod, "poly2" + pre)(cp), to_basis(kind, [F(v) for v in cp]), 1e-12) and allclose(getattr(mod, pre + "2poly")(c), from_basis(kind, c), 1e-12) and allclose(getattr(mod, pre + "2poly")(getattr(mod, "poly2" + pre)(cp)), cp, 1e-12))
    # ---- trimming
    report(f"{pre} functions trim trailing zeros of the inputs ('c is a trimmed copy'): add([1,2,0,0],[0,0,0]) -> [1,2]", fn(kind, "add")([1, 2, 0, 0], [0, 0, 0]).tolist() == [1.0, 2.0])

print("#### gauss quadrature, weight functions, Chebyshev points and interpolation")
moment = {"cheb": lambda k: mp.pi * mp.fac2(k - 1) / mp.fac2(k) if k % 2 == 0 else mp.mpf(0),    # int x^k / sqrt(1-x^2)
          "leg": lambda k: mp.mpf(2) / (k + 1) if k % 2 == 0 else mp.mpf(0),                                # int x^k
          "herm": lambda k: mp.gamma(mp.mpf(k + 1) / 2) if k % 2 == 0 else mp.mpf(0),                        # int x^k exp(-x^2)
          "herme": lambda k: mp.sqrt(2 * mp.pi) * mp.fac2(k - 1) if k % 2 == 0 else mp.mpf(0),         # int x^k exp(-x^2/2)
          "lag": lambda k: mp.factorial(k)}                                                                  # int_0^inf x^k exp(-x)
wfun = {"cheb": lambda x: 1 / mp.sqrt(1 - x * x), "leg": lambda x: mp.mpf(1), "herm": lambda x: mp.exp(-x * x), "herme": lambda x: mp.exp(-x * x / 2), "lag": lambda x: mp.exp(-x)}
for kind in ["cheb", "leg", "herm", "herme", "lag"]:
    mod, pre, cls = KINDS[kind]
    for n in (1, 5, 12):
        xg, wg = fn(kind, "gauss")(n)
        nodes = sorted(z.real for z in mp_roots(list(basis(kind, n))))
        node_err = max(abs(float(a) - b) for a, b in zip(sorted(xg.tolist()), nodes))
        report(f"{pre}gauss({n}): nodes are the roots of B_{n} (mpmath polyroots of the exact basis polynomial)", len(xg) == n and node_err < 1e-13 * max(1, max(abs(v) for v in nodes)), f"(max abs err {node_err:.1e})")
        report(f"{pre}gauss({n}): weights sum to the integral of the weight function {float(moment[kind](0)):.10g}", close(wg.sum(), moment[kind](0), 1e-13) and (wg > 0).all())
        xm = [mp.mpf(float(v)) for v in xg]; wm = [mp.mpf(float(v)) for v in wg]            # the returned doubles, summed exactly
        def quad(k): return sum(w * x ** k for x, w in zip(xm, wm))
        errs = [float(abs(quad(k) - moment[kind](k)) / max(moment[kind](0), abs(moment[kind](k)))) for k in range(2 * n)]
        e2n = float(abs(quad(2 * n) - moment[kind](2 * n)) / moment[kind](2 * n))
        report(f"{pre}gauss({n}): integrates x^k exactly for k <= 2n-1 = {2 * n - 1} (closed-form moments; the double nodes / weights summed in mpmath)", max(errs) < 1e-12, f"(max rel err {max(errs):.1e}; x^(2n) off by {e2n:.2e}, as expected)")
        if n > 1:
            Vm = mp.matrix([[mp.mpf(r) ** j for r in nodes] for j in range(n)]); we = mp.lu_solve(Vm, mp.matrix([moment[kind](j) for j in range(n)]))
            pairs = sorted(zip(xg.tolist(), wg.tolist())); werr = max(abs(w - float(we[i])) / float(we[i]) for i, (x, w) in enumerate(pairs))
            print(f"   {pre}gauss({n}): max relative weight error vs the mpmath Vandermonde-moment solve at the exact nodes {werr:.1e} (smallest weight {float(min(we)):.2e}) (informational)")
    xw = [F(-1, 2), F(0), F(3, 10), F(9, 10)] if kind != "lag" else [F(0), F(1, 2), F(3), F(10)]
    report(f"{pre}weight(x) = documented weight function (ndarray and scalar input)", allclose(fn(kind, "weight")(np.array(fl(xw))), [wfun[kind](mp.mpf(x.numerator) / x.denominator) for x in xw], 1e-14) and close(fn(kind, "weight")(float(xw[1])), wfun[kind](mp.mpf(xw[1].numerator) / xw[1].denominator), 1e-14))
    try: wl_ = fn(kind, "weight")([float(v) for v in xw]); ok_ = allclose(wl_, [wfun[kind](mp.mpf(x.numerator) / x.denominator) for x in xw], 1e-14); det = ""
    except Exception as e: ok_ = False; det = f"({type(e).__name__}: {e})"
    report(f"{pre}weight accepts a plain Python list ('x : array_like' in the docstring)", ok_, det)
xg, wg = CM.chebgauss(7)
report("chebgauss(7): closed form x_i = cos(pi (2i-1)/(2n)), w_i = pi/n", allclose(xg, [math.cos(math.pi * (2 * i - 1) / 14) for i in range(1, 8)], 1e-14, 1e-15) and allclose(wg, [math.pi / 7] * 7, 1e-14))
p1 = CM.chebpts1(5); p2 = CM.chebpts2(5)
report("chebpts1(5) = {cos(pi (k + 1/2)/5)} (returned ascending, the docstring lists them descending: same set), chebpts2(5) = cos(pi k/4) ascending", allclose(p1, sorted(math.cos(math.pi * (k + .5) / 5) for k in range(5)), 1e-14, 1e-15) and p1.tolist() == sorted(p1.tolist()) and allclose(p2, sorted(math.cos(math.pi * k / 4) for k in range(5)), 1e-14, 1e-15))
ci = CM.chebinterpolate(lambda x: x ** 3 - 2 * x + 0.5, 3)
report("chebinterpolate(x^3 - 2x + 1/2, deg=3): exact Chebyshev coefficients of the polynomial (Fraction) to 1e-14 abs", allclose(ci, to_basis("cheb", [F(1, 2), F(-2), F(0), F(1)]), 1e-14, 1e-14), f"(max abs err {float(np.max(np.abs(ci - np.array(fl(to_basis('cheb', [F(1, 2), F(-2), F(0), F(1)])))))):.1e})")
ci = CM.chebinterpolate(lambda x: x ** 3 - 2 * x + 0.5, 6)
report("chebinterpolate at a higher degree than the function: the extra coefficients are 0 (to 1e-14)", allclose(ci[:4], to_basis("cheb", [F(1, 2), F(-2), F(0), F(1)]), 1e-14, 1e-14) and np.max(np.abs(ci[4:])) < 1e-14, f"(max |extra coef| {float(np.max(np.abs(ci[4:]))):.1e})")
ce = CM.chebinterpolate(np.exp, 10); pts = CM.chebpts1(11)
report("chebinterpolate(exp, 10) interpolates: series equals exp at the 11 Chebyshev points of the first kind", allclose(CM.chebval(pts, ce), np.exp(pts), 1e-14))
xx = np.linspace(-1, 1, 2001); e_int = float(np.max(np.abs(CM.chebval(xx, ce) - np.exp(xx))))
print(f"   chebinterpolate(exp, 10): max |interpolant - exp| on [-1,1] = {e_int:.2e} (informational; 11 T_11 coefficient ~ {1 / (2 ** 10 * math.factorial(11)):.1e})")
ca = CM.chebinterpolate(lambda x, a, b: a * x + b, 2, args=(3.0, -1.0))
report("chebinterpolate(func, deg, args=): extra arguments are passed to func", allclose(ca[:2], [-1, 3], 1e-14) and abs(ca[2]) < 1e-15)
ci_cls = Chebyshev.interpolate(lambda x: x * x, 2, domain=[0, 2])
report("Chebyshev.interpolate(x^2, 2, domain=[0, 2]): series on the domain whose convert().coef is [0, 0, 1]", ci_cls.domain.tolist() == [0, 2] and allclose(ci_cls.convert(kind=Polynomial).coef, [0, 0, 1], 1e-13, 1e-14))

print("#### polyutils")
report("trimcoef([1,2,0,0]) = [1,2]; trimcoef([0,0]) = [0]; trimcoef(tol=1e-4) removes trailing |c| <= tol: [1,1e-3,1e-5,1e-5] -> [1,1e-3]", pu.trimcoef([1, 2, 0, 0]).tolist() == [1.0, 2.0] and pu.trimcoef([0, 0]).tolist() == [0.0] and pu.trimcoef([1, 1e-3, 1e-5, 1e-5], tol=1e-4).tolist() == [1.0, 1e-3] and raises(lambda: pu.trimcoef([1], tol=-1), ValueError))
report("trimseq removes only exact trailing zeros; an all-zero sequence keeps its first element", list(pu.trimseq([1, 0, 2, 0, 0])) == [1, 0, 2] and list(pu.trimseq([0, 0])) == [0])
s = pu.as_series([[1, 2, 3], [4, 5, 6]]); s1 = pu.as_series([1, 2, 3]); s2 = pu.as_series([[2, 0], [1.1, 0]]); s3 = pu.as_series([[2, 0], [1.1, 0]], trim=False)
report("as_series: 2-D parsed by row into float64 arrays; 1-D into size-1 arrays; trailing zeros trimmed unless trim=False", [a.tolist() for a in s] == [[1, 2, 3], [4, 5, 6]] and all(a.dtype == np.float64 for a in s) and [a.tolist() for a in s1] == [[1], [2], [3]] and [a.tolist() for a in s2] == [[2], [1.1]] and [a.tolist() for a in s3] == [[2, 0], [1.1, 0]])
report("as_series raises ValueError for an empty series and for a 3-D input", raises(lambda: pu.as_series([[]]), ValueError) and raises(lambda: pu.as_series(np.zeros((2, 2, 2))), ValueError))
report("as_series of complex input gives complex arrays, of integer input float64", pu.as_series([[1j, 2]])[0].dtype == np.complex128 and pu.as_series([np.array([1, 2])])[0].dtype == np.float64)
report("getdomain(real x) = [min, max]; complex x -> corners of the bounding rectangle", pu.getdomain([3, -1, 7, 2]).tolist() == [-1, 7] and pu.getdomain([1 + 2j, -3 + 5j, 2 - 1j]).tolist() == [-3 - 1j, 2 + 5j])
off, scl = pu.mapparms([2, 10], [-1, 1])
report("mapparms(old, new): off + scl*x maps old[i] -> new[i]: [2,10] -> [-1,1] is off=-1.5, scl=1/4", close(off, -1.5, 1e-15) and close(scl, 0.25, 1e-15))
report("mapparms([-1,1],[1,-1]) = (-0, -1); complex domains: ([0, 1j], [1, 1+1j]) -> (1, 1)", pu.mapparms([-1, 1], [1, -1]) == (0, -1) and pu.mapparms([0, 1j], [1, 1 + 1j]) == (1, 1))
report("mapdomain(x, old, new) = new[0] + m (x - old[0]), m = (new1-new0)/(old1-old0); endpoints map to endpoints", allclose(pu.mapdomain([2, 4, 10, 14], [2, 10], [-1, 1]), [-1, -0.5, 1, 2], 1e-15))
report("mapdomain preserves the shape and an ndarray subtype (np.matrix)", pu.mapdomain(np.zeros((2, 3)), [0, 1], [0, 2]).shape == (2, 3) and isinstance(pu.mapdomain(np.matrix([[0.5]]), [0, 1], [0, 2]), np.matrix))
V = np.vander([2, 3, 5], 4); Vi = np.vander([2, 3, 5], 4, increasing=True)
report("np.vander(x, 4): columns x^3, x^2, x, 1 (decreasing); increasing=True reverses; default N = len(x)", V.tolist() == [[8, 4, 2, 1], [27, 9, 3, 1], [125, 25, 5, 1]] and Vi.tolist() == [[1, 2, 4, 8], [1, 3, 9, 27], [1, 5, 25, 125]] and np.vander([2, 3]).tolist() == [[2, 1], [3, 1]])

print("#### ABCPolyBase classes")
p = Polynomial([1, 2, 3], domain=[0, 10], window=[-1, 1])
off, scl = p.mapparms()
report("Polynomial([1,2,3], domain=[0,10]).mapparms() = (-1, 1/5): off + scl*x maps domain to window", close(off, -1, 1e-15) and close(scl, 0.2, 1e-15))
inner = [F(-1), F(1, 5)]; p_exact = pcompose([F(1), F(2), F(3)], inner)             # p(x) = c(-1 + x/5) in powers of x
xt = [F(0), F(1), F(5, 2), F(7), F(10), F(-4), F(25)]
report("__call__ maps x through the domain->window map first: p(x) = c(off + scl*x) (exact composition)", allclose(p(np.array(fl(xt))), [peval(p_exact, x) for x in xt], 1e-13))
report("__call__ on a scalar / 2-D ndarray keeps the shape", np.ndim(p(3.0)) == 0 and p(np.array([[0, 5], [10, 20]])).shape == (2, 2))
try: lst_ok = p([0.0, 5.0]).shape == (2,); lst_det = ""
except Exception as e: lst_ok = False; lst_det = f"({type(e).__name__}: {e})"
report("__call__ accepts a plain list argument" + ("" if NP2 else " (1.x: 'off + scl*arg' on the raw argument; 2.x maps through pu.mapdomain -> informational on 1.x)"), lst_ok or not NP2, lst_det + ("" if lst_ok else " -- 1.x does not"))
pd = p.deriv(); pd_exact = pder(p_exact)
report("deriv() of a series with domain [0,10] is the derivative w.r.t. x (chain rule: coef scaled by scl = window/domain ratio = 1/5), domain kept", pd.domain.tolist() == [0, 10] and allclose(pd(fl(xt)), [peval(pd_exact, x) for x in xt], 1e-13) and allclose(pd.coef, [2 * 0.2, 6 * 0.2], 1e-14))
pd2 = p.deriv(2)
report("deriv(2) = second derivative w.r.t. x (scl**2)", allclose(pd2(fl(xt)), [peval(pder(pd_exact), x) for x in xt], 1e-13))
pi1 = p.integ(1, k=[4], lbnd=3)
I = pint(p_exact); I[0] += F(4) - peval(I, F(3))
report("integ(k=[4], lbnd=3) on domain [0,10]: antiderivative w.r.t. x with value 4 at x = 3 (lbnd in domain coordinates)", pi1.domain.tolist() == [0, 10] and allclose(pi1(fl(xt)), [peval(I, x) for x in xt], 1e-12) and close(pi1(3.0), 4.0, 1e-13))
pi2 = p.integ(2, k=[1, 2], lbnd=0)
I2 = pint(p_exact); I2[0] += F(1) - peval(I2, F(0)); I2 = pint(I2); I2[0] += F(2) - peval(I2, F(0))
report("integ(2, k=[1,2], lbnd=0) on domain [0,10]: first integral is 1 at x=0, second is 2 at x=0 (exact)", allclose(pi2(fl(xt)), [peval(I2, x) for x in xt], 1e-12) and allclose(pi2.deriv()(fl(xt)), [peval(pder(I2), x) for x in xt], 1e-12))
pid = p.integ(); pi0 = p.integ(lbnd=0)
print(f"   integ() with lbnd omitted on domain [0,10]: value at x=0 is {pid(0.0):.6g}, at x=5 (window origin) {pid(5.0):.6g}; integ(lbnd=0): value at x=0 is {pi0(0.0):.6g}")
report("integ() with lbnd omitted equals integ(lbnd=0): an explicit lbnd is taken in domain coordinates (mapped through off + scl*lbnd), so the default should be the domain point 0", allclose(pid.coef, pi0.coef, 1e-13) and close(pid(0.0), 0.0, 1e-12, 1e-12), f"(lbnd=None integrates from the WINDOW origin x={pu.mapdomain(0.0, p.window, p.domain):.6g})")
report("integ then deriv returns the original series values (round trip on the mapped domain)", allclose(p.integ().deriv()(fl(xt)), p(fl(xt)), 1e-12))
q = Polynomial([-1, 0, 1], domain=[0, 10])                                          # u^2 - 1 with u = -1 + x/5 -> roots at x = 0, 10
q_exact = pcompose([F(-1), F(0), F(1)], inner)
report("roots() of a series on domain [0,10]: roots of c mapped back through window -> domain (x = 0 and 10 for u^2 - 1)", allclose(sorted(q.roots()), [0, 10], 1e-13, 1e-13) and match_err(q.roots(), mp_roots(q_exact)) < 1e-12)
r2 = Polynomial([1, -3, 2, 1], domain=[-2, 6], window=[-1, 1]).roots(); r2_exact = mp_roots(pcompose([F(1), F(-3), F(2), F(1)], [F(-1, 2), F(1, 4)]))
report("roots() on domain [-2,6]: equals mpmath roots of the composed polynomial in x", match_err(r2, r2_exact) < 1e-11)
# fit / convert
xd = [F(2000 + i) for i in range(21)]; yd = [F(i * i * i, 7) - F(5 * i) + F((3 * i) % 4, 2) for i in range(21)]
pf = Polynomial.fit(fl(xd), fl(yd), 3)
report("Polynomial.fit: default domain = [min(x), max(x)], window = [-1, 1]", pf.domain.tolist() == [2000, 2020] and pf.window.tolist() == [-1, 1])
rows = [[x ** j for j in range(4)] for x in xd]; ce = lstsq_exact(rows, yd)
pc = pf.convert()
report("Polynomial.fit(x, y, 3).convert().coef = exact least-squares coefficients in the unshifted x (documented usage of convert())", allclose(pc.coef, ce, 1e-6) and pc.domain.tolist() == [-1, 1], f"(max rel err {maxrel(pc.coef, ce):.1e}; exact {fl(ce).tolist()})")
report("fit values equal the exact LS polynomial at the data (domain-mapped fit is well conditioned on years 2000-2020)", allclose(pf(fl(xd)), [peval(ce, x) for x in xd], 1e-10), f"(max rel err {maxrel(pf(fl(xd)), [peval(ce, x) for x in xd]):.1e})")
pback = pc.convert(domain=[2000, 2020]); p10 = Polynomial([1.5, -2, 3.25, 0.5], domain=[0, 10]); p10b = p10.convert().convert(domain=[0, 10])
report("convert() round trip: convert().convert(domain=orig) recovers the coefficients on the original domain (domain [0,10], 1e-12)", allclose(p10b.coef, p10.coef, 1e-12) and p10b.domain.tolist() == [0, 10] and pback.domain.tolist() == [2000, 2020])
print(f"   the same round trip through raw-x coefficients ~1e9 for the years 2000-2020 fit: max rel coefficient err {maxrel(pback.coef, pf.coef):.1e} (informational; ill-conditioned representation, documented note in convert())")
pcheb = pf.convert(kind=Chebyshev); pcheb_d = pf.convert(kind=Chebyshev, domain=[2000, 2020])
report("convert(kind=Chebyshev) gives the exact Chebyshev coefficients of the x-polynomial; convert(kind=Chebyshev, domain=orig) keeps the values", isinstance(pcheb, Chebyshev) and allclose(pcheb.coef, to_basis("cheb", ce), 1e-6) and allclose(pcheb_d(fl(xd)), pf(fl(xd)), 1e-10) and pcheb_d.domain.tolist() == [2000, 2020])
print(f"   evaluating the raw-x Chebyshev series (coefficients ~1e9, T_k(2000) ~ 1e10) at the data loses digits: max rel err {maxrel(pcheb(fl(xd)), pf(fl(xd))):.1e} ('conversion ... can result in numerically ill defined series', documented)")
pf_w = Polynomial.fit(fl(xd), fl(yd), 3, window=[0, 1]); pf_d = Polynomial.fit(fl(xd), fl(yd), 3, domain=[])
report("fit(window=[0,1]) / fit(domain=[]) ('[] -> class domain'): recorded and values still the LS polynomial", pf_w.window.tolist() == [0, 1] and pf_d.domain.tolist() == [-1, 1] and allclose(pf_w(fl(xd)), [peval(ce, x) for x in xd], 1e-10) and allclose(pf_w.convert().coef, ce, 1e-6))
pff, stat = Polynomial.fit(fl(xd), fl(yd), 3, full=True)
rss = sum((y - peval(ce, x)) ** 2 for x, y in zip(xd, yd))
report("Polynomial.fit(full=True) returns (series, [resid, rank, sv, rcond]) with rcond = len(x)*eps", isinstance(pff, Polynomial) and close(stat[0][0], rss, 1e-7) and stat[1] == 4 and len(stat[2]) == 4 and stat[3] == 21 * np.finfo(float).eps)
pfl = Polynomial.fit(fl(xd), fl(yd), [0, 1, 3]); rows_l = [[x ** j for j in (0, 1, 3)] for x in xd]; ce_l = lstsq_exact(rows_l, yd)
print(f"   fit(deg=[0,1,3]) coef on the window {pfl.coef.tolist()}")
report("Polynomial.fit(deg=[0,1,3]): the window-space coefficient of x^2 is exactly 0 (fit restricted to those terms)", len(pfl.coef) == 4 and pfl.coef[2] == 0)
try:
    pcx = Polynomial.fit([5.0] * 4, [1, 2, 3, 6], 0); cx_ok = pcx.domain.tolist() == [4, 6] and close(pcx(5.0), 3.0, 1e-14); cx_det = f"(domain {pcx.domain.tolist()}, value {pcx(5.0)})"
except Exception as e: cx_ok = False; cx_det = f"({type(e).__name__}: {e})"
report("Polynomial.fit with constant x: " + ("2.x widens the domain to [x-1, x+1] (source) and the fit is the mean" if NP2 else "1.x maps through a zero-length domain (NaN) and raises LinAlgError; 2.x widens the domain -> informational on 1.x"), cx_ok or not NP2, cx_det)
# mismatched domains
p1 = Polynomial([1, 2], domain=[0, 1]); p2 = Polynomial([1, 2], domain=[0, 2]); p3 = Polynomial([1, 2], window=[0, 2])
report("arithmetic between series with different domains raises TypeError ('Domains differ'); different windows too; different types too", raises(lambda: p1 + p2, TypeError) and raises(lambda: p1 * p2, TypeError) and raises(lambda: Polynomial([1, 2]) - p3, TypeError) and raises(lambda: Polynomial([1, 2]) + Chebyshev([1, 2]), TypeError))
# class arithmetic exact (default domain)
A_, B_ = Chebyshev([1, -2, 3, 1]), Chebyshev([2, 0, -1])
pa_, pb_ = from_basis("cheb", [1, -2, 3, 1]), from_basis("cheb", [2, 0, -1])
report("Chebyshev class: +, -, *, //, %, divmod, ** exact vs Fraction (converted back to power form)", allclose((A_ + B_).convert(kind=Polynomial).coef, padd(pa_, pb_), 1e-13) and allclose((A_ - B_).convert(kind=Polynomial).coef, padd(pa_, pscale(pb_, -1)), 1e-13) and allclose((A_ * B_).convert(kind=Polynomial).coef, pmul(pa_, pb_), 1e-13) and allclose((A_ // B_).convert(kind=Polynomial).coef, pdivmod(pa_, pb_)[0], 1e-12) and allclose((A_ % B_).convert(kind=Polynomial).coef, pdivmod(pa_, pb_)[1], 1e-12) and (A_ // B_, A_ % B_) == divmod(A_, B_) and allclose((B_ ** 3).convert(kind=Polynomial).coef, ppow(pb_, 3), 1e-13))
report("scalar arithmetic: 2 + p, p * 3, p - 1, 4 - p, p / 2 (true division by a scalar only; by a series raises TypeError)", allclose((2 + A_).coef, [3, -2, 3, 1]) and allclose((A_ * 3).coef, [3, -6, 9, 3]) and allclose((A_ - 1).coef, [0, -2, 3, 1]) and allclose((4 - A_).coef, [3, 2, -3, -1]) and allclose((A_ / 2).coef, [.5, -1, 1.5, .5]) and raises(lambda: A_ / B_, TypeError))
comp = Polynomial([1, 0, 1])(Polynomial([2, 3]))
report("p(q) with a series argument composes: (1 + x^2)(2 + 3x) = 5 + 12x + 9x^2", isinstance(comp, Polynomial) and allclose(comp.coef, [5, 12, 9]))
report("__pow__ above maxpower (100) raises ValueError; ** 0 gives [1]", raises(lambda: Polynomial([1, 1]) ** 101, ValueError) and (Polynomial([1, 1]) ** 0).coef.tolist() == [1.0])
# misc methods
lx, ly = p.linspace(5)
report("linspace(n=5): x = linspace(domain[0], domain[1], 5), y = p(x); domain= overrides", lx.tolist() == [0, 2.5, 5, 7.5, 10] and allclose(ly, p(lx)) and p.linspace(3, domain=[1, 2])[0].tolist() == [1, 1.5, 2])
t = Polynomial([1, 7, 0, 0])
report("degree() = len(coef) - 1 without trimming (documented); trim().degree() drops trailing zeros; trim(tol)", t.degree() == 3 and t.trim().degree() == 1 and Polynomial([1, 1e-3, 1e-5]).trim(1e-4).coef.tolist() == [1, 1e-3])
report("cutdeg(1) / truncate(2) keep the two lowest coefficients; cutdeg above the degree returns a copy; truncate(0) raises ValueError", t.cutdeg(1).coef.tolist() == [1, 7] and t.truncate(2).coef.tolist() == [1, 7] and t.cutdeg(9).coef.tolist() == [1, 7, 0, 0] and raises(lambda: t.truncate(0), ValueError))
report("has_samedomain / has_samewindow / has_sametype / has_samecoef", p1.has_samedomain(Polynomial([9], domain=[0, 1])) and not p1.has_samedomain(p2) and p1.has_samewindow(p2) and not Polynomial([1]).has_samewindow(p3) and p1.has_sametype(p2) and not p1.has_sametype(Chebyshev([1])) and p1.has_samecoef(p2) and not p1.has_samecoef(Polynomial([1, 2, 0])))
cp = p.copy()
report("copy() is equal but independent (new coefficient array)", cp == p and cp.coef is not p.coef and cp.domain.tolist() == [0, 10])
report("== compares coefficients, domain, window (and symbol); != is its negation; trailing zeros are not ignored", Polynomial([1, 2]) == Polynomial([1, 2]) and Polynomial([1, 2]) != Polynomial([1, 2, 0]) and p1 != p2 and Polynomial([1, 2]) != p3 and Polynomial([1, 2]) != Chebyshev([1, 2]) and not (Polynomial([1, 2]) != Polynomial([1.0, 2.0])))
report("Polynomial.basis(3) = x^3; basis(3, domain=[0,2]) evaluates to u^3 with u the mapped variable", Polynomial.basis(3).coef.tolist() == [0, 0, 0, 1] and close(Polynomial.basis(3, domain=[0, 2])(1.5), 0.5 ** 3, 1e-14) and Chebyshev.basis(2).coef.tolist() == [0, 0, 1])
idn = Polynomial.identity(domain=[0, 10]); idc = Chebyshev.identity(domain=[-3, 5])
report("identity(domain): p(x) == x for all x (documented) on both Polynomial and Chebyshev", allclose(idn(np.array([0, 2.5, 10, -7])), [0, 2.5, 10, -7], 1e-14) and allclose(idc(np.array([-3, 0, 5, 12])), [-3, 0, 5, 12], 1e-14))
fr = Polynomial.fromroots([1, 2, 3], domain=[0, 10])
report("fromroots([1,2,3], domain=[0,10]): roots() gives 1,2,3 and convert().coef is the exact monic expansion [-6, 11, -6, 1]", allclose(sorted(fr.roots()), [1, 2, 3], 1e-12) and allclose(fr.convert().coef, fromroots_exact([1, 2, 3]), 1e-12))
frn = Polynomial.fromroots([1, 5]); frN = Polynomial.fromroots([1, 5], domain=None)
report("fromroots default domain [] -> class domain [-1,1]; domain=None -> [min root, max root]", frn.domain.tolist() == [-1, 1] and frN.domain.tolist() == [1, 5] and allclose(frN.convert().coef, [5, -6, 1], 1e-12))
cast = Polynomial.cast(Chebyshev([1, 2, 3]))
report("Polynomial.cast(Chebyshev([1,2,3])) = 1 + 2 T1 + 3 T2 in the power basis = [-2, 2, 6]", isinstance(cast, Polynomial) and allclose(cast.coef, [-2, 2, 6], 1e-14))
report("iteration and len give the coefficients / their count", list(Polynomial([1, 2, 3])) == [1, 2, 3] and len(Polynomial([1, 2, 3])) == 3)
report("negation / unary plus", (-Polynomial([1, -2])).coef.tolist() == [-1, 2] and (+Polynomial([1, -2])).coef.tolist() == [1, -2])
# printing
np.polynomial.set_default_printstyle("unicode")
pp = Polynomial([1, 2, 3]); cc = Chebyshev([1, 2, 3])
X1U, X1A = ("x", "x") if V124 else ("x¹", "x**1")                                     # 1.23 documents '2.0·x¹' / '2.0 x**1' for the degree-1 term
report(f"set_default_printstyle('unicode'): str(Polynomial([1,2,3])) = '1.0 + 2.0·{X1U} + 3.0·x²', Chebyshev -> '1.0 + 2.0·T₁(x) + 3.0·T₂(x)' (documented examples of this version)", str(pp) == f"1.0 + 2.0·{X1U} + 3.0·x²" and str(cc) == "1.0 + 2.0·T₁(x) + 3.0·T₂(x)", f"({str(pp)!r}, {str(cc)!r})")
np.polynomial.set_default_printstyle("ascii")
report(f"set_default_printstyle('ascii'): '1.0 + 2.0 {X1A} + 3.0 x**2' and '1.0 + 2.0 T_1(x) + 3.0 T_2(x)'", str(pp) == f"1.0 + 2.0 {X1A} + 3.0 x**2" and str(cc) == "1.0 + 2.0 T_1(x) + 3.0 T_2(x)", f"({str(pp)!r}, {str(cc)!r})")
report("format(p, 'unicode') / format(p, 'ascii') independent of the default; negative coefficients print as ' - '; unknown style raises ValueError", f"{Polynomial([1, -2]):unicode}" == f"1.0 - 2.0·{X1U}" and f"{Polynomial([1, -2]):ascii}" == f"1.0 - 2.0 {X1A}" and raises(lambda: format(pp, "latex"), ValueError))
sd = str(Polynomial([1, 1], domain=[.1, .2]))
report("str of a series with a non-default domain " + ("shows the mapped variable '1.0 + 1.0 (off + scale x)' with off = -3, scale = 20 (2.0 release note; _format_term prints '-3.0 + 20.0x')" if NP2 else "is '1.0 + 1.0 x' (pre-2.0, per the 2.0 release note)"), sd == ("1.0 + 1.0 (-3.0 + 20.0x)" if NP2 else f"1.0 + 1.0 {X1A}"), f"({sd!r}; the 2.0 release-note example reads '1.0 + 1.0 (-3.0000000000000004 + 20.0 x)')")
for name, cls_, uni, asc in [("Legendre", Legendre, "P₁", "P_1"), ("Hermite", Hermite, "H₁", "H_1"), ("HermiteE", HermiteE, "He₁", "He_1"), ("Laguerre", Laguerre, "L₁", "L_1")]:
    report(f"{name}([0, 1]) prints its basis symbol {uni} / {asc}", f"{cls_([0, 1]):unicode}" == f"0.0 + 1.0·{uni}(x)" and f"{cls_([0, 1]):ascii}" == f"0.0 + 1.0 {asc}(x)", f"({format(cls_([0, 1]), 'unicode')!r})")
np.polynomial.set_default_printstyle("unicode")
rp = repr(Polynomial([1, 2, 3])); dw = "[-1.,  1.]" if NP2 else "[-1,  1]"          # 1.x class domain / window are int arrays
rp_e = f"Polynomial([1., 2., 3.], domain={dw}, window={dw}" + (", symbol='x')" if V124 else ")")
report("repr: " + repr(rp_e) + " (symbol shown from 1.24; float domain/window from 2.0)", rp == rp_e, f"({rp!r})")
if V124:
    ps = Polynomial([1, 2], symbol="t")
    report("symbol='t' (1.24+): used in str, part of equality, propagated by arithmetic; mixing symbols raises ValueError", str(ps) == "1.0 + 2.0·t" and ps != Polynomial([1, 2]) and (ps * 2).symbol == "t" and raises(lambda: ps + Polynomial([1, 2]), ValueError) and raises(lambda: Polynomial([1], symbol=""), ValueError) and raises(lambda: Polynomial([1], symbol=1), TypeError))

print("#### legacy API: np.poly1d and friends")
p = np.poly1d([1, 2, 3])
report("poly1d([1,2,3]) is x^2 + 2x + 3: coefficients highest power first via .c / .coef / .coeffs / .coefficients; order 2 (.o); p(0.5) = 4.25", p.c.tolist() == [1, 2, 3] and p.coef.tolist() == [1, 2, 3] and p.coeffs.tolist() == [1, 2, 3] and p.coefficients.tolist() == [1, 2, 3] and p.order == 2 and p.o == 2 and p(0.5) == 4.25 and len(p) == 2)
report("poly1d indexing p[k] = coefficient of x^k (documented; p.c[-(k+1)]); p[k > order] = 0", p[0] == 3 and p[1] == 2 and p[2] == 1 and p[7] == 0)
ps = np.poly1d([1, 2, 3]); ps[4] = 5
report("poly1d __setitem__ beyond the order extends the polynomial (p[4] = 5 -> 5x^4 + x^2 + 2x + 3)", ps.c.tolist() == [5, 0, 1, 2, 3])
report("poly1d strips leading zero coefficients: poly1d([0,0,1,2]).order == 1, .c == [1,2]; poly1d([0]) is the zero polynomial of order 0", np.poly1d([0, 0, 1, 2]).order == 1 and np.poly1d([0, 0, 1, 2]).c.tolist() == [1, 2] and np.poly1d([0]).c.tolist() == [0] and np.poly1d([0, 0]).order == 0)
pr = np.poly1d([1, 2, 3], True)
report("poly1d([1,2,3], r=True) builds from roots: x^3 - 6x^2 + 11x - 6 (exact); .r / .roots recovers them", allclose(pr.c, list(reversed(fromroots_exact([1, 2, 3]))), 1e-14) and allclose(sorted(pr.r), [1, 2, 3], 1e-12) and allclose(sorted(pr.roots), [1, 2, 3], 1e-12))
report("poly1d variable: default 'x'; variable='z' used in str; str layout matches the documented example", p.variable == "x" and np.poly1d([1, 2, 3], variable="z").variable == "z" and str(np.poly1d([1, 2, 3], variable="z")) == "   2\n1 z + 2 z + 3" and str(p) == "   2\n1 x + 2 x + 3" and repr(p) == "poly1d([1, 2, 3])", f"({str(np.poly1d([1, 2, 3], variable='z'))!r})")
q = np.poly1d([2, -1])
pa_, pb_ = [F(3), F(2), F(1)], [F(-1), F(2)]                                     # low -> high forms of p and q
report("poly1d arithmetic: p + q, p - q, p * q, p ** 2 exact (Fraction)", allclose((p + q).c, list(reversed(padd(pa_, pb_)))) and allclose((p - q).c, list(reversed(padd(pa_, pscale(pb_, -1))))) and allclose((p * q).c, list(reversed(pmul(pa_, pb_)))) and allclose((p ** 2).c, list(reversed(pmul(pa_, pa_)))) and isinstance(p * q, np.poly1d))
qq, rr = p / q; qe, re_ = pdivmod(pa_, pb_)
report("poly1d p / q returns (quotient, remainder) poly1d pair with p = q*quotient + remainder exactly", isinstance(qq, np.poly1d) and allclose(qq.c, list(reversed(qe)), 1e-14) and allclose(rr.c, list(reversed(re_)), 1e-14), f"(quotient {qq.c.tolist()}, remainder {rr.c.tolist()})")
report("poly1d scalar arithmetic: 2*p, p + 1, p / 2, 1 - p; equality compares coefficients", allclose((2 * p).c, [2, 4, 6]) and allclose((p + 1).c, [1, 2, 4]) and allclose((p / 2).c, [.5, 1, 1.5]) and allclose((1 - p).c, [-1, -2, -2]) and p == np.poly1d([1, 2, 3]) and p != q and not (p == q))
report("poly1d(poly1d) copies (variable kept); np.asarray(p) gives the coefficient array; iteration over coefficients", np.poly1d(np.poly1d([1, 2], variable="t")).variable == "t" and np.asarray(p).tolist() == [1, 2, 3] and list(p) == [1, 2, 3])
report("poly1d.deriv(m) exact: (x^2+2x+3)' = 2x + 2, '' = 2, ''' = 0 (order-0 zero polynomial)", p.deriv().c.tolist() == [2, 2] and p.deriv(2).c.tolist() == [2] and p.deriv(3).c.tolist() == [0] and p.deriv(4).c.tolist() == [0])
I3 = p.integ(3, k=[6, 5, 3])
report("poly1d.integ(3, k=[6,5,3]): P''(0) = 6, P'(0) = 5, P(0) = 3 ('constants of the highest-order terms come first'): exact", allclose(I3.c, [F(1, 60), F(2, 24), F(3, 6), F(6, 2), F(5), F(3)], 1e-15), f"({I3.c.tolist()})")
report("poly1d.integ(k=scalar) for m=1 and default k=0; deriv(integ(p)) == p", allclose(p.integ(k=7).c, [F(1, 3), 1, 3, 7], 1e-15) and allclose(p.integ().c, [F(1, 3), 1, 3, 0], 1e-15) and p.integ().deriv() == p)
# np.polyval / polyder / polyint / polymul / polydiv / polyadd / polysub / poly / roots
coefs = [1.1, -2.3, 0.7, 5.9, -0.4]; xv = 1.37
def horner(cs, x):
    y = 0.0
    for c_ in cs: y = y * x + c_
    return y
report("np.polyval: p[0] x^(N-1) + ... + p[N-1] evaluated by Horner's scheme -- bit-identical to the plain Python Horner loop from the highest coefficient", np.polyval(coefs, xv) == horner(coefs, xv) and all(np.polyval(coefs, x_) == horner(coefs, x_) for x_ in [-3.3, 0.0, 12.5, 1e-3]))
report("np.polyval keeps the shape of x, returns a poly1d for a poly1d x (composition p(q(t)))", np.polyval([1, 2], [[0, 1], [2, 3]]).tolist() == [[2, 3], [4, 5]] and isinstance(np.polyval([1, 0, 1], np.poly1d([2, 3])), np.poly1d) and np.polyval([1, 0, 1], np.poly1d([2, 3])).c.tolist() == [4, 12, 10])
report("np.polyval of a scalar x with a poly1d p equals p(x); polyval([], x) = 0", np.polyval(p, 0.5) == p(0.5) and np.polyval([], 2.0) == 0)
report("np.roots: leading zeros are stripped ([0,0,1,-3,2] -> roots 1, 2)", allclose(sorted(np.roots([0, 0, 1, -3, 2])), [1, 2], 1e-14))
rt = np.roots([1, -3, 2, 0, 0])
report("np.roots: trailing zeros give exact zero roots ([1,-3,2,0,0] -> 0, 0, 1, 2), appended after the eigenvalues", len(rt) == 4 and (rt[2:] == 0).all() and allclose(sorted(rt[:2]), [1, 2], 1e-14))
report("np.roots degree 0 / 1 / empty / all-zero: [5] -> [], [2,-4] -> [2], [] -> [], [0,0] -> []", np.roots([5]).tolist() == [] and np.roots([2, -4]).tolist() == [2] and np.roots([]).tolist() == [] and np.roots([0, 0]).tolist() == [] and np.roots([0, 0, 0, 3]).tolist() == [])
report("np.roots returns real dtype when all roots are real, complex otherwise; x^2 + 1 -> +-i", not np.iscomplexobj(np.roots([1, -3, 2])) and np.iscomplexobj(np.roots([1, 0, 1])) and match_err(np.roots([1, 0, 1]), [1j, -1j]) < 1e-15)
report("np.roots raises ValueError for a 2-D input", raises(lambda: np.roots([[1, 2], [3, 4]]), ValueError))
w20 = fromroots_exact([F(i) for i in range(1, 21)]); rw = np.roots(fl(reversed(w20)))
ew = match_err(rw, list(range(1, 21)))
print(f"   np.roots of the degree-20 Wilkinson polynomial (exact float coefficients up to 20! ~ 2.4e18): max abs root error {ew:.3e} (informational; the docs promise nothing beyond 'may have large errors')")
rc3 = np.roots(fl(reversed(fromroots_exact([F(1), F(1), F(1), F(3)]))))
print(f"   np.roots of (x-1)^3 (x-3): triple-root error {max(abs(z - 1) for z in rc3 if abs(z - 1) < .5):.2e} (eps^(1/3) ~ {2.2e-16 ** (1 / 3):.1e}), simple root error {min(abs(z - 3) for z in rc3):.2e} (informational)")
p3 = [1, 2, 3, 4]
report("np.polyder([1,2,3,4], m) exact: [3,4,3], [6,4], [6]; poly1d in -> poly1d out with the documented poly1d([0]) for m = 4", np.polyder(p3).tolist() == [3, 4, 3] and np.polyder(p3, 2).tolist() == [6, 4] and np.polyder(p3, 3).tolist() == [6] and isinstance(np.polyder(np.poly1d(p3)), np.poly1d) and np.polyder(np.poly1d(p3), 4).c.tolist() == [0])
d4 = np.polyder(p3, 4)
report("np.polyder(sequence, m > degree) is the zero polynomial [0] like the poly1d input (docstring: 'The fourth-order derivative of a 3rd-order polynomial is zero')", d4.tolist() == [0], f"(returned {d4!r}; np.polyval of it is {np.polyval(d4, 2.0)!r})")
report("np.polyder(sequence) return type is poly1d as documented ('Returns: der : poly1d')", isinstance(np.polyder(p3), np.poly1d), f"(returned {type(np.polyder(p3)).__name__}; the docstring examples only show poly1d input)")
report("np.polyder raises ValueError for m < 0", raises(lambda: np.polyder(p3, -1), ValueError))
Ip = np.polyint([1, 2, 3], 3, k=[6, 5, 3])
report("np.polyint(p, 3, k=[6,5,3]): P^(j)(0) = k[m-j-1] -> P = int^3 p + 6/2! x^2 + 5 x + 3 (documented example, exact); ndarray for a sequence input, poly1d for poly1d input", isinstance(Ip, np.ndarray) and allclose(Ip, [F(1, 60), F(2, 24), F(3, 6), F(3), F(5), F(3)], 1e-15) and isinstance(np.polyint(np.poly1d([1, 2, 3]), 3, k=[6, 5, 3]), np.poly1d))
report("np.polyint(p, k=scalar) for m=1; k=None -> zeros; len(k) != m raises ValueError", allclose(np.polyint([1, 2, 3], k=4), [F(1, 3), 1, 3, 4], 1e-15) and allclose(np.polyint([1, 2, 3], 2), [F(1, 12), F(1, 3), F(3, 2), 0, 0], 1e-15) and raises(lambda: np.polyint([1, 2, 3], 3, k=[1, 2]), ValueError))
report("np.polyint(p, 2, k=[1]): a length-1 list is broadcast to all m constants (source: 'len(k) == 1 and m > 1'; undocumented convenience)", allclose(np.polyint([1, 2, 3], 2, k=[1]), np.polyint([1, 2, 3], 2, k=[1, 1])))
report("np.polymul exact convolution: (x^2+2x+3)(2x-1) = 2x^3 + 3x^2 + 4x - 3; poly1d in -> poly1d out", np.polymul([1, 2, 3], [2, -1]).tolist() == [2, 3, 4, -3] and isinstance(np.polymul(np.poly1d([1, 2, 3]), [2, -1]), np.poly1d))
qd, rd = np.polydiv([3, 5, 2], [2, 1])
report("np.polydiv: (3x^2 + 5x + 2)/(2x + 1) = 1.5x + 1.75 remainder 0.25 (documented example, exact)", qd.tolist() == [1.5, 1.75] and rd.tolist() == [0.25])
qd2, rd2 = np.polydiv([1, 0, 0, -1], [1, -1])
report("np.polydiv exact division: (x^3 - 1)/(x - 1) = x^2 + x + 1 remainder [0]", qd2.tolist() == [1, 1, 1] and rd2.tolist() == [0])
qd3, rd3 = np.polydiv([1, 2], [1, 0, 0, 5])
report("np.polydiv with a lower-degree dividend: quotient [0], remainder the dividend; scalar (0-d) operands work", qd3.tolist() == [0] and rd3.tolist() == [1, 2] and np.polydiv(np.array(6.0), np.array(3.0))[0].tolist() == [2] and np.polydiv([2, 4], np.array(2.0))[0].tolist() == [1, 2])
report("np.polyadd / np.polysub of different lengths align at the constant term: [1,2,3] + [1] = [1,2,4], [1] - [1,2,3] = [-1,-2,-2]", np.polyadd([1, 2, 3], [1]).tolist() == [1, 2, 4] and np.polysub([1], [1, 2, 3]).tolist() == [-1, -2, -2] and np.polyadd([1, 2, 3], [-1, 0, 0]).tolist() == [0, 2, 3])
report("np.poly from roots (0,0,0) = [1,0,0,0]; from (-1/2, 0, 1/2) = [1, 0, -1/4, 0] (documented examples, exact)", np.poly((0, 0, 0)).tolist() == [1, 0, 0, 0] and np.poly((-.5, 0, .5)).tolist() == [1, 0, -.25, 0])
pc = np.poly([1 + 1j, 1 - 1j]); pcx = np.poly([1 + 1j, 2])
report("np.poly with complex-conjugate roots returns a REAL array (x^2 - 2x + 2); a non-conjugate complex root keeps complex dtype", not np.iscomplexobj(pc) and pc.tolist() == [1, -2, 2] and np.iscomplexobj(pcx) and allclose(pcx, [1, -3 - 1j, 2 + 2j], 1e-15))
Am = [[2, 1, 0], [1, 3, 1], [0, 1, 4]]
# Faddeev-LeVerrier: c_{n-k} coefficients of det(tI - A), exact
def charpoly(A_):
    n = len(A_); A_ = [[F(v) for v in row] for row in A_]; Mk = [[F(0)] * n for _ in range(n)]; cs = [F(1)]
    for k in range(1, n + 1):
        Mk = [[sum(A_[i][l] * Mk[l][j] for l in range(n)) + (cs[-1] if i == j else 0) for j in range(n)] for i in range(n)]
        AM = [[sum(A_[i][l] * Mk[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        cs.append(-sum(AM[i][i] for i in range(n)) / k)
    return cs
report("np.poly(square matrix) = coefficients of the characteristic polynomial det(tI - A) (Faddeev-LeVerrier, exact)", allclose(np.poly(Am), charpoly(Am), 1e-12), f"({np.poly(Am).tolist()})")
report("np.poly([]) = 1.0; np.poly raises ValueError for a non-square 2-D input", np.poly([]) == 1.0 and raises(lambda: np.poly([[1, 2, 3], [4, 5, 6]]), ValueError))

print("#### np.polyfit beyond n2")
xd_f = fl(xd); yd_f = fl(yd)
c0, cov0 = np.polyfit(xd_f, yd_f, 0, cov=True); c0u, cov0u = np.polyfit(xd_f, yd_f, 0, cov="unscaled")
ybar = sum(yd) / len(yd); s2 = sum((y - ybar) ** 2 for y in yd) / (len(yd) - 1)
report("np.polyfit(deg=0, cov=True): coefficient = mean(y); cov = RSS/(n-1) / n (documented chi2/dof scaling, dof = M - (deg+1))", close(c0[0], ybar, 1e-13) and close(cov0[0, 0], s2 / len(yd), 1e-10), f"(cov {float(cov0[0, 0]):.6g} exact {float(s2 / len(yd)):.6g})")
report("np.polyfit(deg=0, cov='unscaled'): cov = (A^T A)^-1 = 1/n", close(cov0u[0, 0], 1 / len(yd), 1e-12))
report("np.polyfit(cov=True) raises ValueError when the number of points does not exceed the order", raises(lambda: np.polyfit([1., 2., 3.], [1., 2., 4.], 2, cov=True), ValueError))
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); c5 = np.polyfit(xd_f, yd_f, 5)
rank_warned = any(issubclass(w_.category, RankWarning) for w_ in wl)
rows5 = [[x ** j for j in range(6)] for x in xd]; ce5 = lstsq_exact(rows5, yd)
c5e = list(reversed(ce5)); rel5 = [abs(float(a) - float(b)) / abs(float(b)) for a, b in zip(c5, c5e)]
fitted5 = np.polyval(c5, xd_f); yfit_err = max(abs(float(v) - peval(ce5, x)) for v, x in zip(fitted5, xd)) / max(abs(float(v)) for v in yd)
print(f"   np.polyfit(years 2000-2020, deg=5): RankWarning raised = {rank_warned}; exact LS coefficients (highest first) {[float(v) for v in c5e]}")
print(f"   returned coefficients {c5.tolist()}; relative errors per coefficient {[f'{e:.1e}' for e in rel5]}; fitted-value error {yfit_err:.2e} relative to max|y| (informational)")
c5f, res5, rank5, sv5, rc5 = np.polyfit(xd_f, yd_f, 5, full=True)
print(f"   full=True: rank {rank5} of 6, singular values {sv5.tolist()}, rcond {rc5:.3e} = len(x)*eps = {21 * np.finfo(float).eps:.3e}")
report("np.polyfit(full=True) returns (coef, residuals, rank, singular_values, rcond) with rcond = len(x)*eps and residuals = sum of squared residuals of ITS fit", rc5 == 21 * np.finfo(float).eps and len(sv5) == 6 and (len(res5) == 1 or rank5 < 6) and (rank5 < 6 or close(res5[0], float(sum((float(v) - y) ** 2 for v, y in zip(fitted5, yd_f))), 1e-6, 1e-12)))
report("np.polyfit issues RankWarning exactly when full=False and rank < order (rank from full=True: %d)" % rank5, rank_warned == (rank5 < 6))
c5c = np.polyfit([float(x) - 2010 for x in xd], yd_f, 5)
rows5c = [[(x - 2010) ** j for j in range(6)] for x in xd]; ce5c = list(reversed(lstsq_exact(rows5c, yd)))
report("np.polyfit degree 5 on the centred years (x - 2010): coefficients equal the exact LS to 1e-9 relative (the documented remedy)", allclose(c5c, ce5c, 1e-9), f"(max rel err {maxrel(c5c, ce5c):.1e})")
yc = np.array(yd_f) + 1j * np.array([float(F(i * i, 3) - 4) for i in range(21)])
ccx = np.polyfit(xd_f, yc, 2)
rows2 = [[x ** j for j in range(3)] for x in xd]
ce_r = list(reversed(lstsq_exact(rows2, yd))); ce_i = list(reversed(lstsq_exact(rows2, [F(i * i, 3) - 4 for i in range(21)])))
report("np.polyfit with complex y (real x): coefficients = LS(real y) + i LS(imag y), complex dtype", np.iscomplexobj(ccx) and allclose(ccx.real, ce_r, 1e-8) and allclose(ccx.imag, ce_i, 1e-8))
ci_ = np.polyfit([0, 1, 2, 3], np.array([1, 3, 7, 13]), 2)
report("np.polyfit with int y: float64 output equal to the exact fit (interpolating 1 + x + x^2)", ci_.dtype == np.float64 and allclose(ci_, [1, 1, 1], 1e-12))
cw = np.polyfit(xd_f, yd_f, 2, w=fl(wts[:21] if len(wts) >= 21 else [F(1 + (i % 3)) for i in range(21)]))
wts21 = [F(1 + (i % 3)) for i in range(21)]; ce_w = list(reversed(lstsq_exact(rows2, yd, wts21)))
report("np.polyfit(w=): 'w[i] applies to the unsquared residual' -> minimises sum (w_i (y_i - p(x_i)))^2, i.e. w = 1/sigma, not 1/sigma^2", allclose(cw, ce_w, 1e-8), f"(max rel err {maxrel(cw, ce_w):.1e})")
report("np.polyfit(w=) with a weight vector of the wrong length raises TypeError; deg < 0 ValueError; x 2-D TypeError", raises(lambda: np.polyfit(xd_f, yd_f, 1, w=[1, 2]), TypeError) and raises(lambda: np.polyfit(xd_f, yd_f, -1), ValueError) and raises(lambda: np.polyfit([[1, 2]], [1, 2], 1), TypeError))
Y2 = np.array([yd_f, [2 * v + 1 for v in yd_f]]).T; c2d = np.polyfit(xd_f, Y2, 2)
report("np.polyfit with 2-D y: 'coefficients for the k-th data set are in p[:, k]'", c2d.shape == (3, 2) and allclose(c2d[:, 0], ce_r, 1e-8) and allclose(c2d[:, 1], list(reversed(lstsq_exact(rows2, [2 * v + 1 for v in yd]))), 1e-8))
cnew = PM.polyfit(xd_f, yd_f, 2); cold = np.polyfit(xd_f, yd_f, 2)
report("numpy.polynomial.polynomial.polyfit returns low -> high, np.polyfit high -> low: reversed arrays", allclose(cnew, cold[::-1], 1e-8) and allclose(cnew, list(reversed(ce_r)), 1e-8))
# conditioning at degree 20: Chebyshev.fit vs Polynomial.fit vs raw np.polyfit
xl = np.linspace(2000, 2020, 200); ul = (xl - 2010) / 10; yl = np.cos(3 * ul)
cf_c, st_c = Chebyshev.fit(xl, yl, 20, full=True); cf_p, st_p = Polynomial.fit(xl, yl, 20, full=True)
with warnings.catch_warnings(record=True) as wl2:
    warnings.simplefilter("always"); craw = np.polyfit(xl, yl, 20)
craw_f, res_raw, rank_raw, sv_raw, _ = np.polyfit(xl, yl, 20, full=True)
e_c = float(np.max(np.abs(cf_c(xl) - yl))); e_p = float(np.max(np.abs(cf_p(xl) - yl))); e_r = float(np.max(np.abs(np.polyval(craw, xl) - yl)))
print(f"   degree-20 fit of cos(3u), u=(x-2010)/10, 200 points: Chebyshev.fit rank {st_c[1]} cond {st_c[2][0] / st_c[2][-1]:.2e} max resid {e_c:.1e}; Polynomial.fit rank {st_p[1]} cond {st_p[2][0] / st_p[2][-1]:.2e} max resid {e_p:.1e}; raw np.polyfit rank {rank_raw} cond {sv_raw[0] / sv_raw[-1]:.2e} max resid {e_r:.1e} (RankWarning {any(issubclass(w_.category, RankWarning) for w_ in wl2)})")
report("Chebyshev.fit at degree 20 on years 2000-2020 is full rank (21) and reproduces the smooth data to 1e-8 ('better conditioned', documented)", st_c[1] == 21 and e_c < 1e-8)
report("Chebyshev.fit degree 20: the Chebyshev coefficients decay (|c_20| < 1e-10 |c_0|) as a smooth function's should (informational threshold)", abs(cf_c.coef[20]) < 1e-10 * abs(cf_c.coef[0]))
print("---- done")
