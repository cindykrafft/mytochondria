#!/usr/bin/env python
"""numpy.fft against an exact DFT evaluated in mpmath (30 digits).  Every
function of numpy.fft: fft / ifft / rfft / irfft / hfft / ihfft / fft2 / ifft2 /
rfft2 / irfft2 / fftn / ifftn / rfftn / irfftn, fftfreq / rfftfreq and
fftshift / ifftshift.  Truths: the DFT as defined in the numpy.fft module
documentation (A_k = sum a_m exp(-2 pi i m k / n), inverse with 1/n), written
as an O(n^2) sum in mpmath (plus an independent radix-2 mpmath FFT for 2**15,
cross-checked against the O(n^2) sum at n = 1024); fractions.Fraction for
fftfreq / rfftfreq / Parseval; Python list rotation for fftshift; closed forms
(pure cosine -> two bins, repeated axis -> n * x[-k], shift theorem).  Inputs
are small random integers (exactly representable in every dtype tested).
Covers: the three norm modes with the documented scaling for each direction;
n smaller / larger than the input (crop / zero-pad) incl. the irfft / hfft
length ambiguity and the documented default n = 2*(m-1); axis / axes / s
(ordering, s shorter than axes, 2.0 deprecations of s without axes and of None
in s, s = -1); out= (2.0+); the Hermitian-symmetry handling of irfft / hfft
(imaginary part of the DC and Nyquist bins dropped); prime (7, 13, 97, 1009)
and composite (1024, 1000, 2**15) lengths with the measured max relative error
(FAIL threshold 1e-12 for float64; the docs give no bound); float32 (2.x:
computed in single precision per the 2.0 release note; 1.x: promoted),
longdouble (2.x native), int / bool promotion, complex input to rfft (docstring
'silently discarded'), empty / n=0 / negative n / 0-d inputs, non-contiguous
and Fortran-ordered inputs, N-D transforms = separable 1-D transforms,
ifft(fft(x)) = x, irfft(rfft(x)) = x (even n), Hermitian symmetry of the fft
of real input, Parseval under each norm, pure cosine -> two bins, linearity,
shift theorem, fftfreq order, fft along axis=-1 of 2-D input, and the aliases
removed / made private by version (numpy.fft.helper).  No scipy anywhere."""
import sys, math, cmath, warnings, random, time, importlib
from fractions import Fraction as F
import numpy as np
import mpmath as mp
mp.mp.dps = 30
MAJOR, MINOR = [int(x) for x in np.__version__.split('.')[:2]]
NP2 = MAJOR >= 2
EPS = np.finfo(np.float64).eps
def banner(): print(f"numpy {np.__version__}  mpmath {mp.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-10, abs_=1e-300):
    a = complex(a); b = complex(b); return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
def raises(fn, exc):
    try: fn(); return False
    except exc: return True
def errmsg(fn):
    try: fn(); return "no exception"
    except Exception as e: return f"{type(e).__name__}: {e}"
def warns_of(fn):
    """run fn, return (result, [warning categories])"""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        r = fn()
    return r, [x.category for x in w]
rng = random.Random(20260925)
def rints(n, lo=-9, hi=9): return [rng.randint(lo, hi) for _ in range(n)]
def rcomplex(n): return [complex(a, b) for a, b in zip(rints(n), rints(n))]
def rarr(shape, cplx=False):
    n = int(np.prod(shape))
    return np.array(rcomplex(n) if cplx else rints(n), dtype=complex if cplx else float).reshape(shape)

# ---------------------------------------------------------------- exact conversions
def mpf_exact(v):
    """exact mpf of a numpy / python real scalar of any float width, int or bool"""
    if isinstance(v, (bool, np.bool_)): return mp.mpf(int(v))
    if isinstance(v, (int, np.integer)): return mp.mpf(int(v))
    if isinstance(v, np.longdouble):
        if v == 0: return mp.mpf(0)
        m, e = np.frexp(v); mi = int(np.ldexp(m, 64))
        return mp.mpf(mi) * mp.mpf(2) ** (int(e) - 64)
    return mp.mpf(float(v))
def mpc_exact(v):
    if isinstance(v, (complex, np.complexfloating)):
        return mp.mpc(mpf_exact(v.real), mpf_exact(v.imag))
    return mp.mpc(mpf_exact(v), 0)
def to_mp(a):
    """numpy array (any dtype) -> object array of exact mpc"""
    a = np.asarray(a); out = np.empty(a.shape, dtype=object)
    for idx in np.ndindex(a.shape): out[idx] = mpc_exact(a[idx])
    return out
def from_list(x): return np.array([mpc_exact(v) for v in x], dtype=object)

# ---------------------------------------------------------------- exact DFT in mpmath
_W = {}
def wtab(n):
    if n not in _W: _W[n] = [mp.expjpi(mp.mpf(-2 * m) / n) for m in range(n)]
    return _W[n]
def dft_n2(x):
    """O(n^2) DFT, the module-doc definition A_k = sum_m a_m exp(-2 pi i m k / n)"""
    n = len(x); W = wtab(n)
    return [mp.fsum(x[j] * W[(j * k) % n] for j in range(n)) for k in range(n)]
def dft_pow2(x, W=None, ntop=None):
    """independent radix-2 decimation-in-time mpmath FFT (n a power of two)"""
    n = len(x)
    if W is None: W = wtab(n); ntop = n
    if n == 1: return [mp.mpc(x[0])]
    E = dft_pow2(x[0::2], W, ntop); O = dft_pow2(x[1::2], W, ntop); step = ntop // n
    out = [None] * n; h = n // 2
    for k in range(h):
        t = W[k * step] * O[k]; out[k] = E[k] + t; out[k + h] = E[k] - t
    return out
def dft(x):
    n = len(x)
    return dft_pow2(list(x)) if (n >= 4096 and n & (n - 1) == 0) else dft_n2(list(x))
def fct(norm, n, inverse):
    """documented scaling: backward: forward 1, inverse 1/n; ortho: 1/sqrt(n) both; forward: forward 1/n, inverse 1"""
    if norm in (None, "backward"): return mp.mpf(1) / n if inverse else mp.mpf(1)
    if norm == "ortho": return 1 / mp.sqrt(n)
    if norm == "forward": return mp.mpf(1) if inverse else mp.mpf(1) / n
    raise ValueError(norm)
def croppad(x, n):
    x = list(x); return x[:n] if len(x) >= n else x + [mp.mpc(0)] * (n - len(x))
def ref1(x, n=None, norm=None, inverse=False):
    """1-D reference transform of a list (crop/pad to n, DFT, inverse via index reversal, scale)"""
    x = [mpc_exact(v) if not isinstance(v, (mp.mpf, mp.mpc)) else v for v in x]
    if n is None: n = len(x)
    x = croppad(x, n); X = dft(x)
    if inverse: X = [X[(-k) % n] for k in range(n)]
    f = fct(norm, n, inverse)
    return [v * f for v in X]
def ref_axis(A, axis, n=None, norm=None, inverse=False, kind="c2c"):
    """apply a 1-D reference transform along `axis` of an object array A (lanes as lists).
    kind: c2c, r2c (keep n//2+1 bins), c2r (Hermitian-extend the lane to length n, DC/Nyquist imag dropped, real result),
    h2r (hfft: Hermitian-extend the TIME lane, forward DFT, real result), r2h (ihfft: inverse of a real lane, first n//2+1)"""
    A = np.asarray(A, dtype=object); axis = axis % A.ndim
    M = np.moveaxis(A, axis, -1); lanes = M.reshape(-1, M.shape[-1]); outs = []
    for lane in lanes:
        lane = list(lane)
        if n is None: n_ = len(lane) if kind in ("c2c", "r2c", "r2h") else 2 * (len(lane) - 1)
        else: n_ = n
        if kind == "c2c": y = ref1(lane, n_, norm, inverse)
        elif kind == "r2c": y = ref1([mp.mpc(v.real, 0) for v in lane], n_, norm, False)[:n_ // 2 + 1]
        elif kind == "r2h": y = ref1([mp.mpc(v.real, 0) for v in lane], n_, norm, True)[:n_ // 2 + 1]
        elif kind in ("c2r", "h2r"):
            m = n_ // 2 + 1; half = croppad(lane, m); full = [mp.mpc(0)] * n_
            for k in range(m): full[k] = half[k]
            for k in range(1, m):
                if (n_ - k) % n_ != k: full[(n_ - k) % n_] = mp.conj(half[k])
            full[0] = mp.mpc(half[0].real, 0)
            if n_ % 2 == 0: full[n_ // 2] = mp.mpc(half[n_ // 2].real, 0)
            y = ref1(full, n_, norm, inverse=(kind == "c2r"))
            y = [mp.mpc(v.real, 0) for v in y]
        outs.append(y)
    out = np.array(outs, dtype=object).reshape(M.shape[:-1] + (len(outs[0]),))
    return np.moveaxis(out, -1, axis)
def ref_nd(A, s=None, axes=None, norm=None, inverse=False):
    """separable N-D reference: 1-D transforms along each axis in turn (module doc: 'extends in the obvious way')"""
    A = np.asarray(A, dtype=object)
    if axes is None: axes = list(range(A.ndim)) if s is None else list(range(-len(s), 0))
    if s is None: s = [A.shape[a] for a in axes]
    for ax, n in zip(axes, s): A = ref_axis(A, ax, n, norm, inverse)
    return A
def ref_rfftn(A, s=None, axes=None, norm=None):
    A = np.asarray(A, dtype=object)
    if axes is None: axes = list(range(A.ndim)) if s is None else list(range(-len(s), 0))
    if s is None: s = [A.shape[a] for a in axes]
    A = ref_axis(A, axes[-1], s[-1], norm, kind="r2c")
    for ax, n in zip(axes[:-1], s[:-1]): A = ref_axis(A, ax, n, norm)
    return A
def ref_irfftn(A, s=None, axes=None, norm=None):
    A = np.asarray(A, dtype=object)
    if axes is None: axes = list(range(A.ndim)) if s is None else list(range(-len(s), 0))
    if s is None: s = [A.shape[a] for a in axes[:-1]] + [2 * (A.shape[axes[-1]] - 1)]
    for ax, n in zip(axes[:-1], s[:-1]): A = ref_axis(A, ax, n, norm, inverse=True)
    return ref_axis(A, axes[-1], s[-1], norm, kind="c2r")
def relerr(lib, ref):
    """max |lib - ref| / max |ref| (normwise relative error, exact conversion of lib)"""
    L = to_mp(lib).ravel(); R = np.asarray(ref, dtype=object).ravel()
    if L.shape != R.shape: return float("inf")
    scale = max([abs(v) for v in R] + [mp.mpf(0)])
    if scale == 0: return float(max(abs(a - b) for a, b in zip(L, R)))
    return float(max(abs(a - b) for a, b in zip(L, R)) / scale)
def imag_max(a): return float(np.max(np.abs(np.imag(a)))) if np.iscomplexobj(a) else 0.0
TOL = 1e-12
def chk(label, lib, ref, tol=TOL, extra=""):
    e = relerr(lib, ref); shp = np.shape(lib) == np.shape(ref)
    report(label, shp and e <= tol, f"(max rel err {e:.2e}{'; ' + extra if extra else ''})" if shp else f"shape {np.shape(lib)} vs {np.shape(ref)}")
    return e

banner()
print(f"   float64 eps {EPS:.3e}; FAIL threshold for float64 transforms: normwise rel err > {TOL:.0e}; NP2={NP2}")

print("#### 1-D fft / ifft against the exact DFT at prime and composite lengths")
t0 = time.perf_counter(); x1024 = rcomplex(1024)
A = dft_n2([mpc_exact(v) for v in x1024]); B = dft_pow2([mpc_exact(v) for v in x1024])
d = float(max(abs(a - b) for a, b in zip(A, B)) / max(abs(a) for a in A))
report("truth self-check: radix-2 mpmath FFT agrees with the O(n^2) mpmath DFT at n=1024 to < 1e-25", d < 1e-25, f"(rel diff {d:.1e}, {time.perf_counter()-t0:.1f}s)")
for n in (7, 13, 97, 1009, 1024, 1000, 2 ** 15):
    x = x1024 if n == 1024 else rcomplex(n)
    xa = np.array(x, dtype=complex)
    t0 = time.perf_counter(); R = ref1(x, n); tr = time.perf_counter() - t0
    e = chk(f"fft n={n} ({'prime' if n in (7,13,97,1009) else 'composite'}) complex int input vs mpmath DFT", np.fft.fft(xa), R,
            extra=f"eps*log2(n)={EPS*math.log2(n):.1e}; ref {tr:.1f}s")
    Ri = [R[(-k) % n] / n for k in range(n)]
    chk(f"ifft n={n}: (1/n) sum A_k exp(+2 pi i mk/n) (module doc inverse definition)", np.fft.ifft(xa), Ri)
    if n in (13, 1000, 2 ** 15):
        xr = rints(n); Rr = ref1(xr, n)
        chk(f"fft n={n} real int input vs mpmath DFT", np.fft.fft(np.array(xr, float)), Rr)
        chk(f"rfft n={n} = first n//2+1 bins of the DFT of real input (length {n//2+1})", np.fft.rfft(np.array(xr, float)), Rr[:n // 2 + 1])

print("#### the three norm modes: documented scaling per direction (module doc 'Normalization')")
for n in (12, 13):
    xc = rcomplex(n); xr = rints(n); xa = np.array(xc); xra = np.array(xr, float)
    m = n // 2 + 1; h = rcomplex(m); ha = np.array(h)
    for norm in (None, "backward", "ortho", "forward"):
        tag = f'norm={norm!r}' if norm else "norm default (None = 'backward')"
        kw = {} if norm is None else {"norm": norm}
        sc = {None: "fft unscaled, ifft 1/n", "backward": "fft unscaled, ifft 1/n", "ortho": "both 1/sqrt(n)", "forward": "fft 1/n, ifft unscaled"}[norm]
        chk(f"fft n={n} {tag}: {sc}", np.fft.fft(xa, **kw), ref1(xc, n, norm))
        chk(f"ifft n={n} {tag}", np.fft.ifft(xa, **kw), ref1(xc, n, norm, inverse=True))
        chk(f"rfft n={n} {tag}: forward scaling on the n//2+1 bins", np.fft.rfft(xra, **kw), ref1(xr, n, norm)[:m])
        chk(f"irfft(a, n={n}) {tag}: inverse scaling of the Hermitian-extended spectrum", np.fft.irfft(ha, n, **kw), ref_axis(from_list(h), 0, n, norm, kind="c2r"))
        chk(f"hfft(a, n={n}) {tag}: forward transform of the Hermitian-extended time signal, forward scaling", np.fft.hfft(ha, n, **kw), ref_axis(from_list(h), 0, n, norm, kind="h2r"))
        chk(f"ihfft n={n} {tag}: inverse transform of real input, n//2+1 bins, inverse scaling", np.fft.ihfft(xra, **kw), ref_axis(from_list(xr), 0, n, norm, kind="r2h"))
        chk(f"ifft(fft(x), {tag}) == x  (n={n}, documented round trip)", np.fft.ifft(np.fft.fft(xa, **kw), **kw), from_list(xc))
        chk(f"fft(ifft(x), {tag}) == x  (n={n})", np.fft.fft(np.fft.ifft(xa, **kw), **kw), from_list(xc))
report("invalid norm raises ValueError", raises(lambda: np.fft.fft(np.ones(4), norm="foo"), ValueError) and raises(lambda: np.fft.irfft(np.ones(4), norm="orthogonal"), ValueError) and raises(lambda: np.fft.fftn(np.ones((2, 2)), norm="x"), ValueError))

print("#### Parseval's theorem under each norm (exact integer sums via Fraction)")
n = 40; xc = rcomplex(n); xa = np.array(xc); E = sum(F(int(v.real)) ** 2 + F(int(v.imag)) ** 2 for v in xc)
for norm, factor in ((None, n), ("ortho", 1), ("forward", F(1, n))):
    P = float(np.sum(np.abs(np.fft.fft(xa, norm=norm)) ** 2)); exp = float(E * factor)
    report(f"Parseval norm={norm!r}: sum|X|^2 = {'n' if norm is None else '1' if norm=='ortho' else '1/n'} * sum|x|^2  (n={n})", close(P, exp, 1e-13), f"(lib {P:.6f} exact {exp:.6f})")
    Pi = float(np.sum(np.abs(np.fft.ifft(xa, norm=norm)) ** 2)); expi = float(E / factor)
    report(f"Parseval for ifft norm={norm!r}: sum|x_inv|^2 = sum|X|^2 {'/ n' if norm is None else '' if norm=='ortho' else '* n'}", close(Pi, expi, 1e-13), f"(lib {Pi:.6f} exact {expi:.6f})")

for n in (16, 15):
    xr = rints(n); Er = sum(F(v) ** 2 for v in xr); X = np.fft.rfft(np.array(xr, float), norm="ortho")
    w_ = np.full(len(X), 2.0); w_[0] = 1.0
    if n % 2 == 0: w_[-1] = 1.0
    P = float(np.sum(w_ * np.abs(X) ** 2))
    report(f"Parseval for rfft norm='ortho' (n={n}): |X0|^2 + 2 sum|Xk|^2 {'+ |X_n/2|^2 ' if n % 2 == 0 else ''}= sum x^2 (the omitted bins are the conjugates)", close(P, float(Er), 1e-13), f"(lib {P:.6f} exact {float(Er)})")

print("#### n smaller / larger than the input: crop / zero-pad (documented for every 1-D function)")
x = rcomplex(10); xa = np.array(x); xr = rints(10); xra = np.array(xr, float)
chk("fft(x, n=6) with len 10: 'the input is cropped'", np.fft.fft(xa, 6), ref1(x, 6))
chk("fft(x, n=16) with len 10: 'the input is padded with zeros' (appended at the end)", np.fft.fft(xa, 16), ref1(x, 16))
chk("ifft(x, n=7) cropped", np.fft.ifft(xa, 7), ref1(x, 7, inverse=True))
chk("ifft(x, n=15) zero-padded", np.fft.ifft(xa, 15), ref1(x, 15, inverse=True))
chk("rfft(x, n=6): cropped, output length 6//2+1 = 4", np.fft.rfft(xra, 6), ref1(xr, 6)[:4])
chk("rfft(x, n=7): cropped, output length (7+1)/2 = 4", np.fft.rfft(xra, 7), ref1(xr, 7)[:4])
chk("rfft(x, n=16): zero-padded, output length 9", np.fft.rfft(xra, 16), ref1(xr, 16)[:9])
report("rfft output length 'n//2 + 1' for n = 8, 9, 1, 2", [len(np.fft.rfft(np.ones(k))) for k in (8, 9, 1, 2)] == [5, 5, 1, 2])
report("ihfft output length 'n//2 + 1'", [len(np.fft.ihfft(np.ones(k))) for k in (8, 9, 1)] == [5, 5, 1])
h = rcomplex(6); ha = np.array(h)   # m = 6 half-spectrum coefficients
report("irfft default n = 2*(m-1) (m=6 -> 10)", np.fft.irfft(ha).shape == (10,))
report("hfft default n = 2*(m-1) (m=6 -> 10)", np.fft.hfft(ha).shape == (10,))
chk("irfft(a) default even length 10: last input entry treated as Nyquist", np.fft.irfft(ha), ref_axis(from_list(h), 0, 10, kind="c2r"))
chk("irfft(a, n=11) odd: 'To get an odd number of output points, n must be specified'", np.fft.irfft(ha, 11), ref_axis(from_list(h), 0, 11, kind="c2r"))
chk("irfft(a, n=6) < 2(m-1): 'For n output points, n//2+1 input points are necessary. If the input is longer than this, it is cropped'", np.fft.irfft(ha, 6), ref_axis(from_list(h), 0, 6, kind="c2r"))
chk("irfft(a, n=7) odd smaller", np.fft.irfft(ha, 7), ref_axis(from_list(h), 0, 7, kind="c2r"))
chk("irfft(a, n=16) > 2(m-1): 'If it is shorter than this, it is padded with zeros' (at high frequencies)", np.fft.irfft(ha, 16), ref_axis(from_list(h), 0, 16, kind="c2r"))
chk("irfft(a, n=17) odd larger", np.fft.irfft(ha, 17), ref_axis(from_list(h), 0, 17, kind="c2r"))
chk("hfft(a, n=11) odd ('2*m - 1 in the typical case')", np.fft.hfft(ha, 11), ref_axis(from_list(h), 0, 11, kind="h2r"))
chk("hfft(a, n=6) cropped", np.fft.hfft(ha, 6), ref_axis(from_list(h), 0, 6, kind="h2r"))
chk("hfft(a, n=15) zero-padded", np.fft.hfft(ha, 15), ref_axis(from_list(h), 0, 15, kind="h2r"))
chk("ihfft(x, n=6) cropped", np.fft.ihfft(xra, 6), ref_axis(from_list(xr), 0, 6, kind="r2h"))
chk("ihfft(x, n=15) zero-padded", np.fft.ihfft(xra, 15), ref_axis(from_list(xr), 0, 15, kind="r2h"))
report("irfft / hfft of a length-1 input: default n = 0 -> ValueError; n=1 works and returns [Re a0]",
       raises(lambda: np.fft.irfft(np.array([5. + 1j])), ValueError) and raises(lambda: np.fft.hfft(np.array([5. + 1j])), ValueError)
       and np.fft.irfft(np.array([5. + 1j]), n=1).tolist() == [5.0] and np.fft.hfft(np.array([5. + 1j]), n=1).tolist() == [5.0])
chk("fft(x, n=1) is the first sample; n=1 identity", np.fft.fft(xa, 1), ref1(x, 1))
chk("fft of a single element = itself", np.fft.fft(np.array([3. - 2j])), [mp.mpc(3, -2)])
chk("fft(empty, n=3) = zeros (padding an empty input)", np.fft.fft(np.array([]), n=3), [mp.mpc(0)] * 3)

print("#### documented round trips of the real / Hermitian pairs, odd vs even lengths")
for n in (8, 9):
    xr = rints(n); xra = np.array(xr, float)
    rt = np.fft.irfft(np.fft.rfft(xra), n)
    chk(f"irfft(rfft(x), len(x)) == x  (n={n}, documented 'to within numerical accuracy')", rt, from_list(xr))
    if n % 2 == 0: chk(f"irfft(rfft(x)) == x with n omitted for EVEN n={n}", np.fft.irfft(np.fft.rfft(xra)), from_list(xr))
    else:
        r = np.fft.irfft(np.fft.rfft(xra))
        report(f"irfft(rfft(x)) with n omitted for ODD n={n}: length 2*(m-1) = {n-1}, NOT x (documented ambiguity)", r.shape == (n - 1,))
        chk(f"   its value = inverse of the (m-1)-Nyquist reinterpretation of the {n//2+1} bins (last bin's imaginary part dropped)", r, ref_axis(ref_axis(from_list(xr), 0, n, kind="r2c"), 0, n - 1, kind="c2r"))
    hh = rcomplex(n // 2 + 1); hha = np.array(hh); hh[0] = complex(hh[0].real, 0)
    if n % 2 == 0: hh[-1] = complex(hh[-1].real, 0)
    hha = np.array(hh)
    chk(f"ihfft(hfft(a, {'2*len(a) - 2' if n % 2 == 0 else '2*len(a) - 1'})) == a  (n={n}, documented, a with real DC{'/Nyquist' if n%2==0 else ''})", np.fft.ihfft(np.fft.hfft(hha, n)), from_list(hh))
    chk(f"rfft(irfft(a, {n})) == a for a with real DC{'/Nyquist' if n%2==0 else ''}  (n={n})", np.fft.rfft(np.fft.irfft(hha, n)), from_list(hh))
X = np.fft.fft(np.array(rints(16), float)); n = 16
herm = max(abs(X[(n - k) % n] - np.conj(X[k])) for k in range(n)) / np.max(np.abs(X))
report("fft of real input is Hermitian-symmetric: A[n-k] == conj(A[k]) (n=16)", herm <= 1e-14, f"(max asymmetry {herm:.1e} rel)")
report("fft of real input: A[0] and A[n/2] 'purely real' (imag exactly 0 for n=16)", X[0].imag == 0 and X[8].imag == 0, f"(imag DC {X[0].imag:.1e}, Nyquist {X[8].imag:.1e})")
X9 = np.fft.fft(np.array(rints(9), float))
report("fft of real input, odd n=9: A[0] real, A[4] / A[5] largest positive / negative frequency are conjugates", X9[0].imag == 0 and abs(X9[4] - np.conj(X9[5])) <= 1e-13 * abs(X9[4]))

print("#### Hermitian-symmetry handling of irfft / hfft: imaginary part of the DC and Nyquist bins ignored")
a = np.array([1 + 5j, 2 - 1j, -3 + 4j, 3 + 7j])   # m=4 -> n=6 even: a[0] DC, a[3] Nyquist
chk("irfft([1+5j, 2-1j, -3+4j, 3+7j], n=6): equals the inverse of the extension with DC and Nyquist taken 'purely real' (documented)", np.fft.irfft(a, 6), ref_axis(to_mp(a), 0, 6, kind="c2r"))
report("   i.e. the same as irfft with the imaginary parts of a[0] and a[3] zeroed (max abs diff)", np.max(np.abs(np.fft.irfft(a, 6) - np.fft.irfft(np.array([1, 2 - 1j, -3 + 4j, 3]), 6))) == 0.0)
chk("irfft(same a, n=7) odd: a[3] is NOT the Nyquist bin, its imaginary part contributes ('complex in the general case')", np.fft.irfft(a, 7), ref_axis(to_mp(a), 0, 7, kind="c2r"))
report("   irfft(a, 7) differs from irfft with imag(a[3]) zeroed", np.max(np.abs(np.fft.irfft(a, 7) - np.fft.irfft(np.array([1, 2 - 1j, -3 + 4j, 3]), 7))) > 0.1)
chk("hfft([1+5j, 2-1j, -3+4j, 3+7j], n=6): Hermitian-extended time signal with real DC / Nyquist", np.fft.hfft(a, 6), ref_axis(to_mp(a), 0, 6, kind="h2r"))
chk("hfft(same a, n=7) odd", np.fft.hfft(a, 7), ref_axis(to_mp(a), 0, 7, kind="h2r"))
report("irfft / hfft return a REAL ndarray (no imaginary part) for complex input", not np.iscomplexobj(np.fft.irfft(a, 6)) and not np.iscomplexobj(np.fft.hfft(a, 7)))
report("hfft output dtype float64 for complex128 input; ihfft output complex128 for float64 input", np.fft.hfft(a).dtype == np.float64 and np.fft.ihfft(np.ones(4)).dtype == np.complex128)
sig = [1, 2, 3, 4, 3, 2]
chk("hfft docstring example: hfft(signal[:4]) = [15, -4, 0, -1, 0, -4] (= fft(signal), default n = 6)", np.fft.hfft(np.array(sig[:4])), [mp.mpc(v) for v in (15, -4, 0, -1, 0, -4)])
chk("   the same example against the reference (Hermitian extension of [1, 2, 3, 4], n = 6) and against the exact DFT of the full signal", np.fft.hfft(np.array(sig[:4])), [v.real for v in ref1(sig, 6)])
chk("hfft docstring example: hfft(signal, 6) 'Input entire signal and truncate' = [15, -4, 0, -1, 0, -4]", np.fft.hfft(np.array(sig), 6), [mp.mpc(v) for v in (15, -4, 0, -1, 0, -4)])
chk("hfft docstring 2-D example: hfft([[1, 1j], [-1j, 2]]) = [[1, 1], [2, -2]] (row-wise, n = 2, imaginary Nyquist dropped)", np.fft.hfft(np.array([[1, 1j], [-1j, 2]])), [[mp.mpc(1), mp.mpc(1)], [mp.mpc(2), mp.mpc(-2)]])
chk("irfft docstring example: irfft([1, -1j, -1]) = [0, 1, 0, 0]", np.fft.irfft(np.array([1, -1j, -1])), [mp.mpc(v) for v in (0, 1, 0, 0)])

print("#### closed forms: pure cosine -> two bins, DC, linearity, shift theorem, repeated axis")
n = 64; j = np.arange(n)
x = np.array([1.0, 0.0, -1.0, 0.0] * (n // 4))   # cos(2 pi (n/4) j / n) sampled exactly (np.cos gives ~1e-14 residues at the zeros)
print(f"   informational: np.cos(2 pi 16 j / 64) deviates from the exact [1, 0, -1, 0, ...] by up to {np.max(np.abs(np.cos(2 * np.pi * (n // 4) * j / n) - x)):.1e}")
X = np.fft.fft(x); chk("fft of the exact cosine at k=n/4 vs mpmath (bins n/4 and 3n/4 = n/2)", X, ref1(x.tolist(), n)); others = np.delete(np.abs(X), [n // 4, 3 * n // 4]).max()
report("fft of the exact cosine at k=n/4: bins n/4 and 3n/4 equal n/2 = 32 exactly, all other bins exactly 0", X[n // 4] == 32 and X[3 * n // 4] == 32 and others == 0.0, f"(max other |bin| {others:.1e})")
A = 2.5; f = 5; x = A * np.cos(2 * np.pi * f * j / n); X = np.fft.fft(x); others = np.delete(np.abs(X), [f, n - f]).max() / (A * n / 2)
report(f"fft of 2.5 cos(2 pi 5 j/64): bins 5 and 59 = A n/2 = {A*n/2} (rel 1e-13), all others < 1e-12 relative", close(X[f], A * n / 2, 1e-13) and close(X[n - f], A * n / 2, 1e-13) and others < 1e-12, f"(X[5]={X[f]:.15g}, max other {others:.1e} rel)")
X = np.fft.fft(A * np.sin(2 * np.pi * f * j / n)); others = np.delete(np.abs(X), [f, n - f]).max() / (A * n / 2)
report("fft of 2.5 sin(2 pi 5 j/64): bin 5 = -i A n/2, bin 59 = +i A n/2, others < 1e-12 rel", close(X[f], -1j * A * n / 2, 1e-13) and close(X[n - f], 1j * A * n / 2, 1e-13) and others < 1e-12, f"(X[5]={X[f]:.6g})")
X = np.fft.fft(np.full(n, 3.0))
report("fft of a constant 3: A[0] = 3 n exactly, others exactly 0 ('A[0] is the sum of the signal')", X[0] == 3 * n and np.all(X[1:] == 0))
X = np.fft.fft(np.exp(2j * np.pi * 7 * j / n))
report("fft of exp(2 pi i 7 j/n): single bin at k=7 equal to n (1e-13), others < 1e-12 rel (module doc 'single-frequency component')", close(X[7], n, 1e-13) and np.delete(np.abs(X), 7).max() / n < 1e-12)
x1 = rcomplex(20); x2 = rcomplex(20); a_, b_ = 3 - 2j, -1.5 + 0.25j
R = [a_ * u + b_ * v for u, v in zip(ref1(x1, 20), ref1(x2, 20))]
chk("linearity: fft(a x + b y) = a DFT(x) + b DFT(y) (mpmath)", np.fft.fft(a_ * np.array(x1) + b_ * np.array(x2)), R)
n = 24; x = rcomplex(n); m = 5; Rm = [v * mp.expjpi(mp.mpf(-2 * k * m) / n) for k, v in enumerate(ref1(x, n))]
chk("shift theorem: fft(roll(x, m)) = DFT(x)[k] exp(-2 pi i k m / n)  (n=24, m=5)", np.fft.fft(np.roll(np.array(x), m)), Rm)
A2 = rarr((5, 6), cplx=True); n = 6
R = np.array([[n * A2[i, (-k) % n] for k in range(n)] for i in range(5)])
chk("fftn(a, axes=(1, 1)): 'repeated indices ... performed multiple times' -> fft twice = n * a[-k mod n] (closed form)", np.fft.fftn(A2, axes=(1, 1)), to_mp(R))
chk("fftn(a, axes=(1, 1, 1, 1)) four times = n^2 * a (closed form)", np.fft.fftn(A2, axes=(1, 1, 1, 1)), to_mp(n * n * A2))

print("#### fftfreq / rfftfreq against Fraction (documented layout)")
def fftfreq_exact(n, d):
    d = F(d); return [F(i if i < (n - 1) // 2 + 1 else i - n) / (d * n) for i in range(n)]
def rfftfreq_exact(n, d): d = F(d); return [F(i) / (d * n) for i in range(n // 2 + 1)]
for n in (8, 9, 1, 2, 3, 16, 1000, 1009):
    for d in (1, F(1, 10), 2, F(1, 4)):
        f = np.fft.fftfreq(n, float(d)); ex = fftfreq_exact(n, d)
        ok = f.shape == (n,) and all(close(a, float(b), 4 * EPS) for a, b in zip(f, ex))
        if d in (1, 2) or (n, d) == (8, F(1, 10)):
            report(f"fftfreq(n={n}, d={float(d)}): [0, 1, ..., {'n/2-1, -n/2' if n % 2 == 0 else '(n-1)/2, -(n-1)/2'}, ..., -1] / (d n) within 4 eps", ok, f"(head {f[:3].tolist()} tail {f[-2:].tolist()})")
        elif not ok: report(f"fftfreq(n={n}, d={float(d)}) within 4 eps", ok)
        fr = np.fft.rfftfreq(n, float(d)); exr = rfftfreq_exact(n, d)
        okr = fr.shape == (n // 2 + 1,) and all(close(a, float(b), 4 * EPS) for a, b in zip(fr, exr))
        if d == 1: report(f"rfftfreq(n={n}): [0, 1, ..., {'n/2' if n % 2 == 0 else '(n-1)/2'}] / (d n), length n//2+1 = {n//2+1}", okr, f"({fr.tolist() if n < 10 else fr[-2:].tolist()})")
        elif not okr: report(f"rfftfreq(n={n}, d={float(d)}) within 4 eps", okr)
report("fftfreq(8) exact for d=1, n a power of two (no rounding)", np.fft.fftfreq(8).tolist() == [0.0, 0.125, 0.25, 0.375, -0.5, -0.375, -0.25, -0.125])
report("rfftfreq: 'the Nyquist frequency component is considered to be positive' (rfftfreq(8)[-1] = +0.5, fftfreq(8)[4] = -0.5)", np.fft.rfftfreq(8)[-1] == 0.5 and np.fft.fftfreq(8)[4] == -0.5)
report("rfftfreq(n odd) == non-negative part of fftfreq(n) (n=9)", np.fft.rfftfreq(9).tolist() == np.fft.fftfreq(9)[:5].tolist())
report("fftfreq / rfftfreq return float64 for Python-float d and for int d", np.fft.fftfreq(8).dtype == np.float64 and np.fft.rfftfreq(8, 2).dtype == np.float64 and np.fft.fftfreq(8, 0.1).dtype == np.float64)
report("fftfreq(n) with non-integer n raises ValueError ('n should be an integer'); np.int64 n accepted", raises(lambda: np.fft.fftfreq(4.0), ValueError) and raises(lambda: np.fft.rfftfreq(4.0), ValueError) and np.fft.fftfreq(np.int64(4)).shape == (4,))
report("fftfreq(1) = [0.], rfftfreq(1) = [0.], fftfreq(2) = [0, -0.5], rfftfreq(2) = [0, 0.5]", np.fft.fftfreq(1).tolist() == [0.0] and np.fft.rfftfreq(1).tolist() == [0.0] and np.fft.fftfreq(2).tolist() == [0.0, -0.5] and np.fft.rfftfreq(2).tolist() == [0.0, 0.5])
d32 = np.fft.fftfreq(8, d=np.float32(0.5)); dld = np.fft.fftfreq(8, d=np.longdouble(0.5))
print(f"   informational: fftfreq dtype with d=float32 -> {d32.dtype}, with d=longdouble -> {dld.dtype}; fftfreq(0) -> {errmsg(lambda: np.fft.fftfreq(0))}")
n, d, fq = 16, 0.25, 1.0   # signal exp(2 pi i f m dt) peaks at the bin whose fftfreq equals f
X = np.fft.fft(np.exp(2j * np.pi * fq * np.arange(n) * d)); k = int(np.argmax(np.abs(X)))
report("module doc: 'a_m = exp(2 pi i f m dt)' peaks at the bin where fftfreq(n, d=dt) == f  (n=16, dt=0.25, f=1 -> bin 4)", k == 4 and np.fft.fftfreq(n, d)[k] == fq, f"(peak bin {k}, fftfreq[{k}] = {np.fft.fftfreq(n, d)[k]})")

print("#### fftshift / ifftshift against list rotation (odd / even, axes int / tuple / None, round trip)")
def rot(xs, s): n = len(xs); return [xs[(i - s) % n] for i in range(n)]
for n in (8, 9, 1, 2, 3):
    x = list(range(n)); xa = np.array(x)
    report(f"fftshift n={n}: y[i] = x[(i - n//2) mod n] (roll by n//2 = {n//2})", np.fft.fftshift(xa).tolist() == rot(x, n // 2), f"({np.fft.fftshift(xa).tolist() if n < 10 else ''})")
    report(f"ifftshift n={n}: roll by -(n//2)", np.fft.ifftshift(xa).tolist() == rot(x, -(n // 2)))
    report(f"ifftshift(fftshift(x)) == x and fftshift(ifftshift(x)) == x  (n={n})", np.fft.ifftshift(np.fft.fftshift(xa)).tolist() == x and np.fft.fftshift(np.fft.ifftshift(xa)).tolist() == x)
    fs = np.fft.fftshift(np.fft.fftfreq(n))
    report(f"fftshift(fftfreq({n})) is strictly increasing with the zero frequency at index n//2 = {n//2} ('center of the spectrum')", np.all(np.diff(fs) > 0) and fs[n // 2] == 0, f"({fs.tolist() if n < 10 else ''})")
report("odd n: fftshift and ifftshift 'differ by one sample' (n=9: shifts 4 and -4 are not equal), even n: identical", np.fft.fftshift(np.arange(9)).tolist() != np.fft.ifftshift(np.arange(9)).tolist() and np.fft.fftshift(np.arange(8)).tolist() == np.fft.ifftshift(np.arange(8)).tolist())
M = np.arange(12).reshape(3, 4); Ml = M.tolist()
report("fftshift 2-D axes=None shifts all axes (rows by 1, cols by 2)", np.fft.fftshift(M).tolist() == [rot(r, 2) for r in rot(Ml, 1)])
report("fftshift 2-D axes=1 (int) shifts only the columns", np.fft.fftshift(M, axes=1).tolist() == [rot(r, 2) for r in Ml])
report("fftshift 2-D axes=(0,) shifts only the rows", np.fft.fftshift(M, axes=(0,)).tolist() == rot(Ml, 1))
report("fftshift 2-D axes=(1, 0) tuple == axes=None", np.fft.fftshift(M, axes=(1, 0)).tolist() == np.fft.fftshift(M).tolist())
report("ifftshift 2-D axes=(0, 1) undoes fftshift(axes=(0, 1)); axes=-1 same as axes=1", np.fft.ifftshift(np.fft.fftshift(M, axes=(0, 1)), axes=(0, 1)).tolist() == Ml and np.fft.fftshift(M, axes=-1).tolist() == np.fft.fftshift(M, axes=1).tolist())
Q = np.arange(16).reshape(4, 4); Qs = np.fft.fftshift(Q)
report("fft2 doc: fftshift of even 2-D 'swaps first and third quadrants, and second and fourth quadrants'", Qs[:2, :2].tolist() == Q[2:, 2:].tolist() and Qs[2:, 2:].tolist() == Q[:2, :2].tolist() and Qs[:2, 2:].tolist() == Q[2:, :2].tolist() and Qs[2:, :2].tolist() == Q[:2, 2:].tolist())
report("fftshift accepts a list and preserves dtype (int stays int)", np.fft.fftshift([1, 2, 3]).tolist() == [3, 1, 2] and np.fft.fftshift(np.arange(4)).dtype == np.int64)
report("fftshift docstring example: fftshift(fftfreq(10, 0.1)) = [-5, -4, ..., 4]", np.fft.fftshift(np.fft.fftfreq(10, 0.1)).tolist() == [float(v) for v in range(-5, 5)] or np.allclose(np.fft.fftshift(np.fft.fftfreq(10, 0.1)), list(range(-5, 5)), rtol=1e-15, atol=0))

print("#### axis argument and 2-D input: fft transforms along axis=-1 (rows) by default")
M = rarr((3, 5), cplx=True)
chk("fft(M) 2-D default axis=-1: each row transformed independently", np.fft.fft(M), ref_axis(to_mp(M), 1))
chk("fft(M, axis=0): each column transformed", np.fft.fft(M, axis=0), ref_axis(to_mp(M), 0))
chk("fft(M, axis=-2) == axis 0", np.fft.fft(M, axis=-2), ref_axis(to_mp(M), 0))
chk("fft(M, n=8, axis=0): zero-pad along axis 0 to shape (8, 5)", np.fft.fft(M, 8, axis=0), ref_axis(to_mp(M), 0, 8))
chk("ifft(M, n=2, axis=1): crop along axis 1", np.fft.ifft(M, 2, axis=1), ref_axis(to_mp(M), 1, 2, inverse=True))
T = rarr((2, 3, 4, 5), cplx=True)
chk("fft on 4-D input, axis=1", np.fft.fft(T, axis=1), ref_axis(to_mp(T), 1))
chk("fft on 4-D input, axis=-3 (== 1)", np.fft.fft(T, axis=-3), ref_axis(to_mp(T), 1))
chk("rfft on 3-D real input along axis=0: shape (n//2+1, ...)", np.fft.rfft(T.real, axis=0), ref_axis(to_mp(T.real), 0, kind="r2c"))
chk("irfft on 3-D input along axis=2, n=7", np.fft.irfft(T, 7, axis=2), ref_axis(to_mp(T), 2, 7, kind="c2r"))
chk("hfft along axis=0 of a 3-D input, n=5", np.fft.hfft(T[0], 5, axis=0), ref_axis(to_mp(T[0]), 0, 5, kind="h2r"))
chk("ihfft along axis=1 of a 3-D real input", np.fft.ihfft(T.real[0], axis=1), ref_axis(to_mp(T.real[0]), 1, kind="r2h"))
report("fft(M, axis=2) on 2-D raises IndexError (documented 'If axis is not a valid axis of a')", raises(lambda: np.fft.fft(M, axis=2), IndexError) and raises(lambda: np.fft.rfft(M.real, axis=-3), IndexError))

print("#### N-D transforms equal separable 1-D transforms along each axis (module doc 'extends in the obvious way')")
T3 = rarr((3, 4, 5), cplx=True); R3 = rarr((3, 4, 6))
chk("fftn(a) 3-D, all axes", np.fft.fftn(T3), ref_nd(to_mp(T3)))
chk("ifftn(a) 3-D = ifft along each axis (1/(3*4*5) total)", np.fft.ifftn(T3), ref_nd(to_mp(T3), inverse=True))
chk("ifftn(fftn(a)) == a (documented)", np.fft.ifftn(np.fft.fftn(T3)), to_mp(T3))
chk("fftn norm='ortho' 3-D: 1/sqrt(3*4*5)", np.fft.fftn(T3, norm="ortho"), ref_nd(to_mp(T3), norm="ortho"))
chk("fftn norm='forward' 3-D: 1/(3*4*5); ifftn 'forward' unscaled", np.fft.fftn(T3, norm="forward"), ref_nd(to_mp(T3), norm="forward"))
chk("ifftn norm='forward' unscaled", np.fft.ifftn(T3, norm="forward"), ref_nd(to_mp(T3), norm="forward", inverse=True))
chk("fft2(a) 3-D: default axes (-2, -1) = last two axes only", np.fft.fft2(T3), ref_nd(to_mp(T3), axes=[1, 2]))
chk("ifft2(a) 3-D default axes", np.fft.ifft2(T3), ref_nd(to_mp(T3), axes=[1, 2], inverse=True))
chk("ifft2(fft2(a)) == a", np.fft.ifft2(np.fft.fft2(T3)), to_mp(T3))
chk("fft2(a, axes=(0, 2))", np.fft.fft2(T3, axes=(0, 2)), ref_nd(to_mp(T3), axes=[0, 2]))
chk("fftn(a, axes=(0,)): a single axis", np.fft.fftn(T3, axes=(0,)), ref_nd(to_mp(T3), axes=[0]))
chk("fftn(a, axes=(2, 0)) == fftn(a, axes=(0, 2)) (order irrelevant without s)", np.fft.fftn(T3, axes=(2, 0)), ref_nd(to_mp(T3), axes=[0, 2]))
chk("fftn(a, s=(6, 2), axes=(2, 0)): 's[i] corresponds to axes[i]' -> pad axis 2 to 6, crop axis 0 to 2", np.fft.fftn(T3, s=(6, 2), axes=(2, 0)), ref_nd(to_mp(T3), s=[6, 2], axes=[2, 0]))
chk("fftn(a, s=(2, 3, 8), axes=(0, 1, 2))", np.fft.fftn(T3, s=(2, 3, 8), axes=(0, 1, 2)), ref_nd(to_mp(T3), s=[2, 3, 8], axes=[0, 1, 2]))
chk("ifftn(a, s=(5, 7), axes=(1, 2))", np.fft.ifftn(T3, s=(5, 7), axes=(1, 2)), ref_nd(to_mp(T3), s=[5, 7], axes=[1, 2], inverse=True))
chk("fft2(a, s=(2, 7)) on 3-D: s applies to the default axes (-2, -1)", np.fft.fft2(T3, s=(2, 7)), ref_nd(to_mp(T3), s=[2, 7], axes=[1, 2]))
chk("fftn(a, s=(5,)) 1-D transform of the last axis only (no axes: 'the last len(s) axes are used')", warns_of(lambda: np.fft.fftn(T3, s=(5,)))[0], ref_nd(to_mp(T3), s=[5], axes=[2]))
chk("fftn 2-D == fft along axis 1 then axis 0 (separability)", np.fft.fftn(T3[0]), ref_axis(ref_axis(to_mp(T3[0]), 1), 0))
report("fftn(a, s=(2,), axes=(0, 1)) with len(s) != len(axes) raises ValueError ('Shape and axes have different lengths')", raises(lambda: np.fft.fftn(T3, s=(2,), axes=(0, 1)), ValueError) and raises(lambda: np.fft.ifftn(T3, s=(2, 3, 4), axes=(0, 1)), ValueError))
report("fft2(a, s=(2, 3, 4)) with default axes (-2, -1) raises ValueError ('axes not given and len(s) != 2')", raises(lambda: np.fft.fft2(T3, s=(2, 3, 4)), ValueError) and raises(lambda: np.fft.fft2(T3, s=(3,)), ValueError))
report("fft2 on 1-D input raises IndexError (axis -2 out of range)", raises(lambda: np.fft.fft2(np.arange(4.0)), IndexError))
report("fftn axis out of range raises IndexError (documented)", raises(lambda: np.fft.fftn(T3, axes=(3,)), IndexError) and raises(lambda: np.fft.rfftn(R3, axes=(0, 5)), IndexError))
# real N-D
chk("rfftn(a) 3-D real: rfft along the last axis (length 6//2+1 = 4), fft along the others", np.fft.rfftn(R3), ref_rfftn(to_mp(R3)))
report("rfftn output shape (3, 4, 4) = s[-1]//2+1 on the last axis", np.fft.rfftn(R3).shape == (3, 4, 4))
chk("rfftn(a, axes=(0, 1)): the real transform is over axes[-1] = 1 (shape (3, 3, 6))", np.fft.rfftn(R3, axes=(0, 1)), ref_rfftn(to_mp(R3), axes=[0, 1]))
chk("rfftn(a, s=(4, 5, 7), axes=(0, 1, 2)) crop/pad; last length 7//2+1 = 4", np.fft.rfftn(R3, s=(4, 5, 7), axes=(0, 1, 2)), ref_rfftn(to_mp(R3), s=[4, 5, 7], axes=[0, 1, 2]))
chk("rfftn norm='ortho'", np.fft.rfftn(R3, norm="ortho"), ref_rfftn(to_mp(R3), norm="ortho"))
chk("rfft2(a) 3-D: default axes (-2, -1)", np.fft.rfft2(R3), ref_rfftn(to_mp(R3), axes=[1, 2]))
chk("rfft2(a, axes=(0, 1)) on 3-D: real axis is axes[-1] = 1", np.fft.rfft2(R3, axes=(0, 1)), ref_rfftn(to_mp(R3), axes=[0, 1]))
chk("rfft2(a, s=(5, 3)) 2-D", np.fft.rfft2(R3[0], s=(5, 3)), ref_rfftn(to_mp(R3[0]), s=[5, 3], axes=[0, 1]))
H = np.fft.rfftn(R3)
r, w = warns_of(lambda: np.fft.irfftn(H, R3.shape))
chk("irfftn(rfftn(a), a.shape) == a (documented)", r, to_mp(R3))
report("the documented idiom 'irfftn(rfftn(a), a.shape) == a' runs without a DeprecationWarning", DeprecationWarning not in w, f"(warnings {[c.__name__ for c in w]})")
r, w = warns_of(lambda: np.fft.irfft2(np.fft.rfft2(R3[0]), s=R3[0].shape))
chk("irfft2 docstring example idiom irfft2(A, s=a.shape) on 2-D == a", r, to_mp(R3[0])); report("   ... and without a DeprecationWarning (irfft2 default axes (-2, -1))", DeprecationWarning not in w)
chk("irfftn(rfftn(a)) with s omitted, even last axis 6 = 2*(4-1): == a", np.fft.irfftn(H), to_mp(R3))
R5 = rarr((3, 4, 5)); H5 = np.fft.rfftn(R5)
report("irfftn(rfftn(a)) with s omitted and ODD last axis 5: last axis becomes 2*(m-1) = 4, not 5", np.fft.irfftn(H5).shape == (3, 4, 4))
chk("irfftn(rfftn(a), a.shape, axes=(0, 1, 2)) == a for odd last axis (s 'must be given')", np.fft.irfftn(H5, R5.shape, axes=(0, 1, 2)), to_mp(R5))
chk("irfftn(H) vs reference: ifft along the leading axes then irfft along the last", np.fft.irfftn(H), ref_irfftn(to_mp(H)))
chk("irfftn(H, s=(3, 4, 7), axes=(0, 1, 2)): odd output length", np.fft.irfftn(H, s=(3, 4, 7), axes=(0, 1, 2)), ref_irfftn(to_mp(H), s=[3, 4, 7], axes=[0, 1, 2]))
chk("irfftn(H, s=(2, 5), axes=(1, 2)): crop axis 1, output last axis 5", np.fft.irfftn(H, s=(2, 5), axes=(1, 2)), ref_irfftn(to_mp(H), s=[2, 5], axes=[1, 2]))
chk("irfftn(H, axes=(1, 0)): real axis is axes[-1] = 0, default length 2*(3-1) = 4", np.fft.irfftn(H, axes=(1, 0)), ref_irfftn(to_mp(H), axes=[1, 0]))
chk("irfftn norm='forward' (inverse unscaled)", np.fft.irfftn(H, norm="forward"), ref_irfftn(to_mp(H), norm="forward"))
chk("irfft2(H) default axes (-2, -1)", np.fft.irfft2(H), ref_irfftn(to_mp(H), axes=[1, 2]))
chk("irfft2(rfft2(a), a.shape[-2:]) == a", np.fft.irfft2(np.fft.rfft2(R5), R5.shape[-2:]), to_mp(R5))
chk("irfft2(H, s=(4, 5), axes=(1, 2))", np.fft.irfft2(H, s=(4, 5), axes=(1, 2)), ref_irfftn(to_mp(H), s=[4, 5], axes=[1, 2]))
chk("irfftn of a general complex array: DC / Nyquist imaginary parts of the last axis dropped", np.fft.irfftn(T3, s=(3, 4, 8), axes=(0, 1, 2)), ref_irfftn(to_mp(T3), s=[3, 4, 8], axes=[0, 1, 2]))
report("irfftn / irfft2 return real float64; rfftn / rfft2 return complex128", np.fft.irfftn(H).dtype == np.float64 and np.fft.irfft2(H).dtype == np.float64 and H.dtype == np.complex128 and np.fft.rfft2(R3).dtype == np.complex128)

print("#### the three norm modes on fft2 / ifft2 / rfft2 / irfft2 (scaling by the product of the transformed lengths)")
Q2 = rarr((3, 5, 6), cplx=True); Qr = Q2.real.copy(); Hq = np.fft.rfft2(Qr)
for norm in ("backward", "ortho", "forward"):
    chk(f"fft2 norm={norm!r} on the last two axes (5*6 = 30 points)", np.fft.fft2(Q2, norm=norm), ref_nd(to_mp(Q2), axes=[1, 2], norm=norm))
    chk(f"ifft2 norm={norm!r}", np.fft.ifft2(Q2, norm=norm), ref_nd(to_mp(Q2), axes=[1, 2], norm=norm, inverse=True))
    chk(f"rfft2 norm={norm!r}", np.fft.rfft2(Qr, norm=norm), ref_rfftn(to_mp(Qr), axes=[1, 2], norm=norm))
    chk(f"irfft2 norm={norm!r} (output 5 x 2*(4-1) = 5 x 6)", np.fft.irfft2(Hq, norm=norm), ref_irfftn(to_mp(Hq), axes=[1, 2], norm=norm))
    chk(f"irfft2(rfft2(a, norm={norm!r}), a.shape[-2:], norm={norm!r}) == a", np.fft.irfft2(np.fft.rfft2(Qr, norm=norm), Qr.shape[-2:], norm=norm), to_mp(Qr))
    chk(f"irfftn(rfftn(a, norm={norm!r}), a.shape, axes=all, norm={norm!r}) == a (3-D, 90 points)", np.fft.irfftn(np.fft.rfftn(Qr, norm=norm), Qr.shape, axes=(0, 1, 2), norm=norm), to_mp(Qr))

print("#### 2.0 changes to s / axes: -1, deprecations (version-aware)")
r, w = warns_of(lambda: np.fft.fftn(T3, s=(4, 5)))
chk("fftn(a, s=(4, 5)) without axes: transforms the last two axes (both builds)", r, ref_nd(to_mp(T3), s=[4, 5], axes=[1, 2]))
if NP2: report("2.x: s without axes emits DeprecationWarning ('axes should not be None if s is not None')", DeprecationWarning in w, f"(warnings {[c.__name__ for c in w]})")
else: report("1.x: s without axes emits no warning (deprecation is 2.0)", DeprecationWarning not in w)
r, w = warns_of(lambda: np.fft.fftn(T3, s=(None, 5), axes=(0, 2)))
chk("fftn(a, s=(None, 5), axes=(0, 2)): None means 'the default value for n' = a.shape[0]", r, ref_nd(to_mp(T3), s=[3, 5], axes=[0, 2]))
if NP2: report("2.x: None in s emits DeprecationWarning", DeprecationWarning in w, f"(warnings {[c.__name__ for c in w]})")
else: report("1.x: None in s accepted silently", DeprecationWarning not in w)
r, w = warns_of(lambda: np.fft.irfftn(H, s=(None, 5), axes=(1, 2)))
chk("irfftn(H, s=(None, 5), axes=(1, 2)): None -> default n for that axis", r, ref_irfftn(to_mp(H), s=[4, 5], axes=[1, 2]))
if NP2:
    chk("2.x: s=-1 means 'the whole input is used (no padding/trimming)' (versionchanged 2.0)", np.fft.fftn(T3, s=(-1, 7), axes=(0, 2)), ref_nd(to_mp(T3), s=[3, 7], axes=[0, 2]))
    chk("2.x: rfftn s=-1 on the real axis", np.fft.rfftn(R3, s=(-1, -1), axes=(1, 2)), ref_rfftn(to_mp(R3), axes=[1, 2]))
    chk("2.x: irfftn s=-1 on the last axis: whole input m used -> n = m (=4 here), not 2(m-1)", np.fft.irfftn(H, s=(-1, -1), axes=(1, 2)), ref_irfftn(to_mp(H), s=[4, 4], axes=[1, 2]))
    r, w = warns_of(lambda: np.fft.fft2(T3, s=(4, 5), axes=None))
    report("2.x: fft2(s=..., axes=None) deprecation warning", DeprecationWarning in w)
else:
    report("1.x: s=-1 raises ValueError (no -1 support before 2.0)", raises(lambda: np.fft.fftn(T3, s=(-1, 7), axes=(0, 2)), ValueError))

print("#### out= parameter (2.0+: dtype / shape checks, in-place)")
x = rcomplex(8); xa = np.array(x); xr = np.array(rints(8), float)
if NP2:
    out = np.empty(8, dtype=complex); r = np.fft.fft(xa, out=out)
    report("fft(x, out=out) returns out itself and fills it", r is out, ""); chk("   contents vs mpmath", out, ref1(x, 8))
    y = xa.copy(); r = np.fft.fft(y, out=y)
    report("fft in place: out is the input array ('can be used for in-place calculations', release note)", r is y); chk("   in-place contents", y, ref1(x, 8))
    y = xa.copy(); np.fft.ifft(y, out=y, norm="ortho"); chk("ifft in place with norm='ortho'", y, ref1(x, 8, "ortho", inverse=True))
    report("fft out with wrong shape raises ValueError ('output array has wrong shape')", raises(lambda: np.fft.fft(xa, out=np.empty(7, dtype=complex)), ValueError) and raises(lambda: np.fft.fft(xa, n=6, out=np.empty(8, dtype=complex)), ValueError))
    report("fft out with wrong ndim raises ValueError", raises(lambda: np.fft.fft(rarr((2, 3), True), out=np.empty(3, dtype=complex)), ValueError))
    report("fft out with real dtype raises TypeError (complex -> float cast not 'same_kind')", raises(lambda: np.fft.fft(xa, out=np.empty(8)), TypeError))
    o = np.empty(8, dtype=np.complex64); r = np.fft.fft(xr, out=o)
    chk("fft float64 input into a complex64 out: accepted, result in complex64 (same_kind downcast)", r, ref1(rints_ := xr.tolist(), 8), tol=1e-6)
    report("   result is the complex64 out array", r is o and r.dtype == np.complex64)
    o = np.empty(5, dtype=complex); r = np.fft.rfft(xr, out=o)
    report("rfft out of shape n//2+1 accepted and returned", r is o); chk("   rfft out contents", o, ref1(xr.tolist(), 8)[:5])
    report("rfft out of shape n raises ValueError", raises(lambda: np.fft.rfft(xr, out=np.empty(8, dtype=complex)), ValueError))
    o = np.empty(8); r = np.fft.irfft(np.array(rcomplex(5)), out=o)
    report("irfft out real float64 of length n accepted and returned", r is o and o.dtype == np.float64)
    hq = rcomplex(4); o = np.full(6, -7.0); r = np.fft.hfft(np.array(hq), out=o)
    report("hfft(a, out=out) 'the result will be placed in this array': returns out", r is o, f"(returned a {'new array' if r is not o else 'out'}; out still all -7: {bool(np.all(o == -7.0))})")
    chk("   hfft out contents = Hermitian-extended forward transform", o, ref_axis(from_list(hq), 0, 6, kind="h2r"))
    chk("   (the returned value itself is correct)", r, ref_axis(from_list(hq), 0, 6, kind="h2r"))
    o = np.empty(5, dtype=complex); r = np.fft.ihfft(xr, out=o); report("ihfft out complex length n//2+1 accepted and returned (conjugated in place)", r is o)
    chk("   ihfft out contents", o, ref_axis(from_list(xr.tolist()), 0, kind="r2h"))
    o = np.empty((3, 4, 5), dtype=complex); r = np.fft.fftn(T3, out=o); report("fftn(a, out=out) returns out", r is o); chk("   fftn out contents", o, ref_nd(to_mp(T3)))
    o = np.empty((3, 4, 7), dtype=complex); r = np.fft.fftn(T3, s=(3, 4, 7), axes=(0, 1, 2), out=o)
    report("fftn out with s changing only the LAST axis works ('only the last axis can have s not equal to the shape', fft2 doc)", r is o); chk("   contents", o, ref_nd(to_mp(T3), s=[3, 4, 7], axes=[0, 1, 2]))
    report("fftn out with s changing a non-last axis raises ValueError (documented 'incompatible with passing in all but the trivial s')", raises(lambda: np.fft.fftn(T3, s=(5, 4, 5), axes=(0, 1, 2), out=np.empty((5, 4, 5), dtype=complex)), ValueError), f"({errmsg(lambda: np.fft.fftn(T3, s=(5, 4, 5), axes=(0, 1, 2), out=np.empty((5, 4, 5), dtype=complex)))[:60]})")
    o = np.empty((3, 4, 4), dtype=complex); r = np.fft.rfftn(R3, out=o); report("rfftn(a, out=out) returns out", r is o); chk("   rfftn out contents", o, ref_rfftn(to_mp(R3)))
    o = np.empty((3, 4, 6)); r = np.fft.irfftn(H, out=o); report("irfftn(H, out=out) real out returned", r is o); chk("   irfftn out contents", o, to_mp(R3))
    y = T3.copy(); r = np.fft.ifftn(y, out=y); chk("ifftn in place", y, ref_nd(to_mp(T3), inverse=True))
    ic = np.fft.irfft(np.array(rcomplex(5)), out=np.empty(8, dtype=complex))
    print(f"   informational: irfft into a complex out is accepted (dtype {ic.dtype}); fftn on a 0-d array returns it unchanged: {np.fft.fftn(np.float64(3))!r}")
else:
    report("1.x: fft() has no out= parameter (added in 2.0) -> TypeError", raises(lambda: np.fft.fft(xa, out=np.empty(8, dtype=complex)), TypeError) and raises(lambda: np.fft.fftn(T3, out=np.empty((3, 4, 5), dtype=complex)), TypeError))
    print(f"   informational: fftn on a 0-d array returns it unchanged: {np.fft.fftn(np.float64(3))!r}")

print("#### dtypes: float32 / longdouble (version-dependent), int / bool promotion, complex input to rfft")
n = 1024; xi = rints(n); xci = rcomplex(n); Rr = ref1(xi, n); Rc = ref1(xci, n)
x32 = np.array(xi, dtype=np.float32); c64 = np.array(xci, dtype=np.complex64)
r32 = np.fft.fft(x32); e32 = relerr(r32, Rr); rc64 = np.fft.fft(c64); ec64 = relerr(rc64, Rc)
if NP2:
    report("2.x float32 input -> complex64 output ('calculations natively in float ... output dtype adjusted', 2.0 release note)", r32.dtype == np.complex64, f"(dtype {r32.dtype})")
    report(f"2.x float32 fft n=1024: single-precision accuracy (measured {e32:.2e} rel; eps32*log2 n = {np.finfo(np.float32).eps*10:.1e}; threshold 1e-4)", e32 < 1e-4)
    report("2.x complex64 input -> complex64; rfft(float32) -> complex64; irfft(complex64) -> float32; hfft(float32) -> float32; ihfft(float32) -> complex64",
           rc64.dtype == np.complex64 and np.fft.rfft(x32).dtype == np.complex64 and np.fft.irfft(c64[:5]).dtype == np.float32 and np.fft.hfft(x32[:5]).dtype == np.float32 and np.fft.ihfft(x32).dtype == np.complex64, f"(complex64 fft err {ec64:.1e})")
    report("2.x float16 input -> complex64 (promoted to the smallest supported float)", np.fft.fft(np.arange(4, dtype=np.float16)).dtype == np.complex64)
    report("2.x fftn / rfftn / irfftn of float32 stay in single precision", np.fft.fftn(T3.astype(np.complex64)).dtype == np.complex64 and np.fft.rfftn(R3.astype(np.float32)).dtype == np.complex64 and np.fft.irfftn(H.astype(np.complex64)).dtype == np.float32)
    e = relerr(np.fft.irfft(np.fft.rfft(x32)), from_list(xi)); report(f"2.x irfft(rfft(float32 x)) == x to single precision (measured {e:.1e})", e < 1e-4)
    stale = "promotes ``float32``" in np.fft.__doc__
    report("2.x numpy.fft module docstring 'Type Promotion' paragraph no longer claims float32 is promoted to float64 (contradicts the 2.0 release note and the measured complex64 output)", not stale)
    xl = np.array(xi, dtype=np.longdouble); rl = np.fft.fft(xl); el = relerr(rl, Rr)
    report("2.x longdouble input -> clongdouble output (native long double support, 2.0 release note)", rl.dtype == np.clongdouble, f"(dtype {rl.dtype})")
    report(f"2.x longdouble fft n=1024 more accurate than float64 (measured {el:.2e} rel vs float64 {relerr(np.fft.fft(np.array(xi, float)), Rr):.2e}; threshold 1e-17)", el < 1e-17)
    cl = np.fft.rfft(xl); report("2.x rfft(longdouble) -> clongdouble; irfft(clongdouble) -> longdouble", cl.dtype == np.clongdouble and np.fft.irfft(cl, n).dtype == np.longdouble)
    e = relerr(np.fft.irfft(cl, n), from_list(xi)); report(f"2.x irfft(rfft(longdouble x)) == x beyond double precision (measured {e:.1e})", e < 1e-17)
else:
    report("1.x float32 input -> complex128 output (module doc 'Type Promotion': promotes float32 / complex64 to float64 / complex128)", r32.dtype == np.complex128 and rc64.dtype == np.complex128, f"(dtypes {r32.dtype}, {rc64.dtype})")
    report(f"1.x float32 fft n=1024 computed in double (measured {e32:.2e} rel <= 1e-12)", e32 <= TOL)
    report("1.x rfft(float32) -> complex128; irfft(complex64) -> float64; hfft(float32) -> float64; ihfft(float32) -> complex128", np.fft.rfft(x32).dtype == np.complex128 and np.fft.irfft(c64[:5]).dtype == np.float64 and np.fft.hfft(x32[:5]).dtype == np.float64 and np.fft.ihfft(x32).dtype == np.complex128)
    xl = np.array(xi, dtype=np.longdouble); rl = np.fft.fft(xl); el = relerr(rl, Rr)
    report("1.x longdouble input computed in double -> complex128 (no native support before 2.0)", rl.dtype == np.complex128, f"(dtype {rl.dtype}, err {el:.1e})")
    report(f"1.x longdouble input accuracy at double level (measured {el:.2e} <= 1e-12)", el <= TOL)
xp = rints(1009); Rp = ref1(xp, 1009); ep32 = relerr(np.fft.fft(np.array(xp, np.float32)), Rp)
if NP2: report(f"2.x float32 fft at prime n=1009 (Bluestein path): single-precision accuracy (measured {ep32:.2e}; threshold 1e-4)", ep32 < 1e-4)
else: report(f"1.x float32 fft at prime n=1009: computed in double (measured {ep32:.2e} <= 1e-12)", ep32 <= TOL)
ii = np.array(xi[:64]); Ri = ref1(xi[:64], 64)
report("int64 input -> complex128 output; bool -> complex128; int8 / uint8 -> complex128", np.fft.fft(ii).dtype == np.complex128 and np.fft.fft(np.array([True, False, True])).dtype == np.complex128 and np.fft.fft(ii.astype(np.int8)).dtype == np.complex128 and np.fft.fft(np.abs(ii).astype(np.uint8)).dtype == np.complex128)
chk("fft of int64 input = DFT of the integers", np.fft.fft(ii), Ri)
chk("rfft of int8 input", np.fft.rfft(ii.astype(np.int8)), Ri[:33])
b = np.array([True, False, True, True, False, False, True, True]); chk("fft of bool input = DFT of 0/1", np.fft.fft(b), ref1([int(v) for v in b], 8))
chk("ihfft of an int input", np.fft.ihfft(ii), ref_axis(from_list(xi[:64]), 0, kind="r2h"))
chk("fft of a Python list input", np.fft.fft([1, 2, 3, 4, 5]), ref1([1, 2, 3, 4, 5], 5))
chk("irfft of REAL input (no imaginary parts): treated as a real spectrum", np.fft.irfft(np.array([4., 1., 2.]), 4), ref_axis(from_list([4, 1, 2]), 0, 4, kind="c2r"))
report("irfft / hfft accept int input (-> float64)", np.fft.irfft(np.array([4, 1, 2])).dtype == np.float64 and np.fft.hfft(np.array([4, 1, 2])).dtype == np.float64)
# complex input to rfft: docstring 'If the input a contains an imaginary part, it is silently discarded.'
ac = np.array([1 + 2j, 3 - 1j, 2 + 0j, 5 + 4j]); Rre = ref1([1, 3, 2, 5], 4)[:3]
def rfft_cplx(): return np.fft.rfft(ac)
try:
    r, w = warns_of(rfft_cplx)
    report("rfft of complex input: 'If the input a contains an imaginary part, it is silently discarded' -> equals rfft of the real part", relerr(r, Rre) <= TOL, f"(warnings {[c.__name__ for c in w]})")
    report("rfft of complex input discards the imaginary part SILENTLY (no warning, as documented)", len(w) == 0, f"(emitted {[c.__name__ for c in w]})")
except Exception as e:
    report("rfft of complex input: 'If the input a contains an imaginary part, it is silently discarded' -> equals rfft of the real part", False, f"(raises {type(e).__name__}: {str(e)[:90]})")
    report("rfft of complex input discards the imaginary part SILENTLY (no warning, as documented)", False, f"(raises {type(e).__name__} instead)")
try:
    r, w = warns_of(lambda: np.fft.ihfft(ac)); report("ihfft of complex input: same rfft path (imaginary part discarded)", relerr(r, [mp.conj(v) / 4 for v in Rre]) <= TOL, f"(warnings {[c.__name__ for c in w]})")
except Exception as e: report("ihfft of complex input: same rfft path (imaginary part discarded)", False, f"(raises {type(e).__name__})")
try:
    r, w = warns_of(lambda: np.fft.rfftn(T3[0])); report("rfftn of complex input: imaginary part discarded (rfft docstring)", relerr(r, ref_rfftn(to_mp(T3[0].real))) <= TOL, f"(warnings {[c.__name__ for c in w]})")
except Exception as e: report("rfftn of complex input: imaginary part discarded (rfft docstring)", False, f"(raises {type(e).__name__})")

try: _r, _w = warns_of(rfft_cplx); _desc = f"returns {np.round(_r, 12).tolist()} with warnings {[c.__name__ for c in _w]}"
except Exception as e: _desc = f"raises {type(e).__name__}"
print(f"   informational: rfft([1+2j, 3-1j, 2, 5+4j]) on this build {_desc}")
print(f"   informational: fft of an object-dtype array: {errmsg(lambda: np.fft.fft(np.array([1, 2, 3, 4], dtype=object)))[:80]}")

print("#### edge cases: empty, n=0 / negative, 0-d, single element")
report("fft of an empty array raises ValueError ('Invalid number of FFT data points (0)')", raises(lambda: np.fft.fft(np.array([])), ValueError) and raises(lambda: np.fft.rfft(np.array([])), ValueError) and raises(lambda: np.fft.ifft([]), ValueError), f"({errmsg(lambda: np.fft.fft(np.array([])))})")
report("fftn / rfftn / irfftn of an empty 2-D array raise ValueError", raises(lambda: np.fft.fftn(np.zeros((0, 3))), ValueError) and raises(lambda: np.fft.rfftn(np.zeros((2, 0))), ValueError) and raises(lambda: np.fft.irfftn(np.zeros((2, 0), dtype=complex)), ValueError))
r = np.fft.fft(np.zeros((3, 0)), axis=0)
report("fft along a non-empty axis of an array with an empty other axis: shape (3, 0) complex result, no error", r.shape == (3, 0) and r.dtype == np.complex128)
report("n=0 raises ValueError for fft / ifft / rfft / irfft / hfft / ihfft", all(raises(lambda f=f: f(np.ones(4), n=0), ValueError) for f in (np.fft.fft, np.fft.ifft, np.fft.rfft, np.fft.irfft, np.fft.hfft, np.fft.ihfft)))
report("negative n raises ValueError", all(raises(lambda f=f: f(np.ones(4), n=-3), ValueError) for f in (np.fft.fft, np.fft.rfft, np.fft.irfft)))
report("fftn with s containing 0 raises ValueError", raises(lambda: np.fft.fftn(np.ones((2, 3)), s=(0, 3), axes=(0, 1)), ValueError))
report("0-d input raises IndexError for fft / rfft / ifft (axis -1 'not a valid axis of a')", raises(lambda: np.fft.fft(np.float64(3.0)), IndexError) and raises(lambda: np.fft.rfft(np.array(2.0)), IndexError) and raises(lambda: np.fft.ifft(4.0), IndexError), f"({errmsg(lambda: np.fft.fft(np.float64(3.0)))})")
report("fftshift of a 0-d input raises (nothing to shift)", raises(lambda: np.fft.fftshift(5.0), Exception))
chk("ifft of a single element = itself", np.fft.ifft(np.array([3. - 2j])), [mp.mpc(3, -2)])
chk("rfft of a single element = [x]; ihfft of one element = [x]", np.fft.rfft(np.array([7.])), [mp.mpc(7)]); chk("   ihfft", np.fft.ihfft(np.array([7.])), [mp.mpc(7)])
chk("fft of two elements = [a+b, a-b] exactly", np.fft.fft(np.array([3., 5.])), [mp.mpc(8), mp.mpc(-2)])
report("fft of two elements exact (no rounding)", np.fft.fft(np.array([3., 5.])).tolist() == [8 + 0j, -2 + 0j])
Xn = np.fft.fft(np.array([1.0, np.nan, 2.0, 3.0]))
report("fft with one NaN input: every bin has a NaN component (np.isnan true); not every real part (trivial twiddles +-1, +-i are applied without multiplication)", bool(np.all(np.isnan(Xn))), f"({Xn.tolist()})")
report("rfft / ifft with one NaN input: every output bin has a NaN component", bool(np.all(np.isnan(np.fft.rfft(np.array([1.0, np.nan, 2.0, 3.0, 5.0])))) and np.all(np.isnan(np.fft.ifft(np.array([1.0, 2.0, np.nan]))))))
report("fft of an all-zero input is exactly zero", np.all(np.fft.fft(np.zeros(9)) == 0) and np.all(np.fft.rfft(np.zeros(8)) == 0))

print("#### non-contiguous and Fortran-ordered inputs")
big = rarr((40,), cplx=True); v = big[::3]; chk("fft of a strided 1-D view x[::3]", np.fft.fft(v), ref1(v.tolist(), len(v)))
v = big[::-1]; chk("fft of a reversed view x[::-1] (negative stride)", np.fft.fft(v), ref1(v.tolist(), len(v)))
M = rarr((6, 8), cplx=True); Mf = np.asfortranarray(M)
report("Fortran-ordered copy is F-contiguous and not C-contiguous", Mf.flags.f_contiguous and not Mf.flags.c_contiguous)
chk("fft of a Fortran-ordered 2-D array along axis=-1", np.fft.fft(Mf), ref_axis(to_mp(M), 1))
chk("fft of a Fortran-ordered 2-D array along axis=0", np.fft.fft(Mf, axis=0), ref_axis(to_mp(M), 0))
chk("fftn of a Fortran-ordered 2-D array", np.fft.fftn(Mf), ref_nd(to_mp(M)))
chk("rfftn of a Fortran-ordered real array", np.fft.rfftn(np.asfortranarray(M.real)), ref_rfftn(to_mp(M.real)))
v = M[1::2, ::3]; chk("fft of a 2-D slice view M[1::2, ::3] along axis 0", np.fft.fft(v, axis=0), ref_axis(to_mp(np.ascontiguousarray(v)), 0))
chk("fft of a transposed view M.T along axis=-1 (rows of M.T = columns of M)", np.fft.fft(M.T), ref_axis(to_mp(np.ascontiguousarray(M.T)), 1))
chk("fft2 of a transposed view", np.fft.fft2(M.T), ref_nd(to_mp(np.ascontiguousarray(M.T))))
chk("irfft along axis 0 of a Fortran-ordered array", np.fft.irfft(Mf, 10, axis=0), ref_axis(to_mp(M), 0, 10, kind="c2r"))
bigr = rarr((64,)); chk("rfft of a strided real view x[::2]", np.fft.rfft(bigr[::2]), ref1(bigr[::2].tolist(), 32)[:17])
report("fft of a view leaves the input unchanged", (lambda c: (np.fft.fft(c[::2]), np.array_equal(c, big))[1])(big.copy()))

print("#### public API surface and aliases by version")
NAMES = ['fft', 'ifft', 'rfft', 'irfft', 'hfft', 'ihfft', 'rfftn', 'irfftn', 'rfft2', 'irfft2', 'fft2', 'ifft2', 'fftn', 'ifftn', 'fftshift', 'ifftshift', 'fftfreq', 'rfftfreq']
report("numpy.fft.__all__ is exactly the 18 documented routines", sorted(np.fft.__all__) == sorted(NAMES), f"(extra {sorted(set(np.fft.__all__) - set(NAMES))}, missing {sorted(set(NAMES) - set(np.fft.__all__))})")
report("all 18 routines are callables in numpy.fft", all(callable(getattr(np.fft, k, None)) for k in NAMES))
def helper_state():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        try: m = importlib.import_module("numpy.fft.helper"); return "present", [c.category.__name__ for c in w], m
        except ModuleNotFoundError: return "absent", [], None
st, w, hm = helper_state()
if NP2: report("2.x: numpy.fft.helper 'made private' (renamed to numpy.fft._helper, 2.0 release note): absent or DeprecationWarning stub", st == "absent" or "DeprecationWarning" in w, f"({st}, warnings {w})")
else: report("1.x: numpy.fft.helper is the public module carrying fftshift / fftfreq (same objects as numpy.fft)", st == "present" and hm.fftshift is np.fft.fftshift and hm.fftfreq is np.fft.fftfreq, f"({st})")
report("numpy.fft.fftpack and fftpack_lite (removed in 1.17) are absent", raises(lambda: importlib.import_module("numpy.fft.fftpack"), ModuleNotFoundError) and raises(lambda: importlib.import_module("numpy.fft.fftpack_lite"), ModuleNotFoundError))
if NP2:
    report("2.x: numpy.fft._helper and _pocketfft exist as the private implementation modules", importlib.import_module("numpy.fft._helper").fftfreq is np.fft.fftfreq and hasattr(importlib.import_module("numpy.fft._pocketfft"), "fft"))
    import inspect
    report("2.x: fftfreq / rfftfreq accept device='cpu' (array API) and reject other devices", np.fft.fftfreq(4, device="cpu").shape == (4,) and np.fft.rfftfreq(4, device="cpu").shape == (3,) and raises(lambda: np.fft.fftfreq(4, device="gpu"), ValueError))
    report("2.x: every transform exposes 'out' in its signature", all("out" in inspect.signature(getattr(np.fft, k)).parameters for k in NAMES[:14]))
report("norm=None accepted as the alias of 'backward' on every transform (module doc)", all(relerr(f(T3, norm=None), f(T3)) == 0 for f in (np.fft.fftn, np.fft.ifftn, np.fft.fft2, np.fft.ifft2)) and relerr(np.fft.rfft(xr, norm=None), np.fft.rfft(xr)) == 0)

print("#### informational: runtime prime vs composite lengths (best of 20)")
def best(f, reps=20):
    b = float("inf")
    for _ in range(reps):
        t = time.perf_counter(); f(); b = min(b, time.perf_counter() - t)
    return b
xs = {n: np.array(rcomplex(n)) for n in (1000, 1009, 1024, 4093, 4096)}
ts = {n: best(lambda n=n: np.fft.fft(xs[n])) for n in xs}
print("   " + ", ".join(f"n={n}: {ts[n]*1e6:.0f} us" for n in xs) + f"; prime/composite ratio 1009/1024 = {ts[1009]/ts[1024]:.1f}, 4093/4096 = {ts[4093]/ts[4096]:.1f} (Bluestein for primes; no expectation)")
