#!/usr/bin/env python
"""m2_spectral: matplotlib.mlab spectral functions (psd, csd, cohere, specgram,
complex_spectrum, magnitude_spectrum, angle_spectrum, phase_spectrum and the
private _spectral_helper under them), the window / detrend helpers
(window_hanning, window_none, detrend, detrend_mean, detrend_linear,
detrend_none), and the Axes wrappers (Axes.psd / csd / magnitude_spectrum /
angle_spectrum / phase_spectrum / cohere / specgram).

Truths (all independent of matplotlib):
  * Welch's averaged periodogram written in plain numpy from the definition in
    the psd/csd docstrings and Bendat & Piersol: split x into NFFT-long segments
    advancing by NFFT - noverlap (zero-pad x to NFFT first if shorter, as the
    docstring says), detrend, multiply by the window, take an EXPLICIT O(n^2)
    DFT (matrix of exp(-2 pi i k m / pad_to), not np.fft) zero-padded to pad_to,
    average conj(X) * Y over the segments, scale by 1 / (Fs * sum(w^2)) when
    scale_by_freq is True (density, V**2/Hz) or 1 / sum(w)^2 when False
    (power per bin), and for a one-sided spectrum keep bins 0..pad_to//2 and
    double every bin except DC and, when pad_to is even, the Nyquist bin.
  * Parseval: sum(Pxx) * Fs / pad_to = variance (detrend='mean', boxcar
    window, one segment) computed with fractions.Fraction on integer data.
  * Closed forms: A cos(2 pi k0 m / N + phi) -> |DFT| / N = A/2 at +-k0;
    white noise of variance s^2 -> flat one-sided density 2 s^2 / Fs.
  * Least squares line fitted in fractions.Fraction for detrend_linear.
  * scipy.signal.welch / csd / coherence / spectrogram with the same window
    array, detrend, nfft and scaling, where SciPy is installed (labels marked
    '(scipy)'; the 3.7.1 and 3.5.2 builds carry no SciPy so these are absent).
Numbers are taken from the returned arrays and from Line2D / AxesImage data.
"""
import sys, math, warnings, inspect
from fractions import Fraction as F
from _synth import *
import numpy as np
import matplotlib
from matplotlib import mlab
from matplotlib.figure import Figure

banner()
V = mpl_version()
if HAVE_SCIPY:
    import scipy.signal as ss

rng = np.random.default_rng(20261001)

def raises(fn, exc=Exception):
    try:
        fn(); return False
    except exc:
        return True

def errname(fn):
    try:
        fn(); return "no exception"
    except Exception as e:
        return f"{type(e).__name__}: {e}"

def quiet(fn, *a, **k):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return fn(*a, **k)

# ------------------------------------------------------------------ reference
def hann_sym(M):
    """symmetric Hann: 0.5 - 0.5 cos(2 pi n / (M-1)), n = 0..M-1 (M = 1 -> [1])"""
    if M == 1: return np.ones(1)
    n = np.arange(M, dtype=float)
    return 0.5 - 0.5 * np.cos(2 * np.pi * n / (M - 1))

def dft(seg, n):
    """explicit DFT A_k = sum_m a_m exp(-2 pi i k m / n) of seg zero-padded / cut to n"""
    seg = np.asarray(seg)
    a = np.zeros(n, dtype=complex)
    m = min(n, len(seg)); a[:m] = seg[:m]
    k = np.arange(n)
    E = np.exp(-2j * np.pi * np.outer(k, k) / n)
    return E @ a

def dft_cols(S, n):
    """explicit DFT of each column of S"""
    S = np.asarray(S)
    A = np.zeros((n, S.shape[1]), dtype=complex)
    m = min(n, S.shape[0]); A[:m] = S[:m]
    k = np.arange(n)
    E = np.exp(-2j * np.pi * np.outer(k, k) / n)
    return E @ A

def lin_detrend(s):
    s = np.asarray(s, dtype=complex if np.iscomplexobj(s) else float)
    n = len(s)
    if n < 2: return s - s  # a line through one point fits it exactly
    i = np.arange(n, dtype=float); ib = i.mean(); sb = s.mean()
    b = np.sum((i - ib) * (s - sb)) / np.sum((i - ib) ** 2)
    return s - (sb + b * (i - ib))

def do_detrend(s, d):
    if d in (None, 'none'): return s
    if d == 'mean': return s - s.mean()
    if d == 'linear': return lin_detrend(s)
    return d(s)

def ref_spec(x, y=None, NFFT=256, Fs=2, window=None, noverlap=0, pad_to=None,
             sides='default', scale_by_freq=True, detrend='none', mode='psd', average=True):
    """returns (P, freqs, t); P averaged (1-D) if average else (nfreq, nseg)"""
    x = np.asarray(x); cplx = np.iscomplexobj(x) or (y is not None and np.iscomplexobj(y))
    if len(x) < NFFT: x = np.concatenate([x, np.zeros(NFFT - len(x), x.dtype)])
    if y is not None:
        y = np.asarray(y)
        if len(y) < NFFT: y = np.concatenate([y, np.zeros(NFFT - len(y), y.dtype)])
    if pad_to is None: pad_to = NFFT
    w = hann_sym(NFFT) if window is None else np.asarray(window, dtype=float)
    step = NFFT - noverlap
    starts = list(range(0, len(x) - NFFT + 1, step))
    Sx = np.array([do_detrend(np.asarray(x[s:s + NFFT], dtype=complex if cplx else float), detrend) * w
                   for s in starts]).T
    X = dft_cols(Sx, pad_to)
    if y is not None:
        Sy = np.array([do_detrend(np.asarray(y[s:s + NFFT], dtype=complex if cplx else float), detrend) * w
                       for s in starts]).T
        Y = dft_cols(Sy, pad_to)
    if sides == 'default': sides = 'twosided' if cplx else 'onesided'
    if mode == 'psd':
        P = np.conj(X) * (Y if y is not None else X)
    elif mode == 'magnitude': P = np.abs(X) / w.sum()
    elif mode == 'complex': P = X / w.sum()
    elif mode in ('angle', 'phase'): P = np.angle(X)
    k = np.arange(pad_to)
    if sides == 'onesided':
        nf = pad_to // 2 + 1
        P = P[:nf]
        freqs = k[:nf] * Fs / pad_to
        if mode == 'psd':
            dbl = np.ones(nf); dbl[1:] = 2.0
            if pad_to % 2 == 0: dbl[-1] = 1.0           # Nyquist bin is not doubled
            P = P * dbl[:, None]
    else:
        ks = np.arange(-(pad_to // 2), pad_to - pad_to // 2)
        P = P[ks % pad_to]
        freqs = ks * Fs / pad_to
    if mode == 'psd':
        P = P / (Fs * np.sum(w ** 2)) if scale_by_freq else P / np.sum(w) ** 2
    if mode == 'phase':
        P = np.unwrap(P, axis=0)
    t = (np.array(starts) + NFFT / 2) / Fs
    if average: P = P.mean(axis=1)
    return P, freqs, t

def cmp(label, got, want, rel=1e-9, absfrac=1e-12, show=True):
    got = np.asarray(got); want = np.asarray(want)
    if got.shape != want.shape:
        report(label, False, f"shape {got.shape} vs truth {want.shape}"); return False
    scale = float(np.max(np.abs(want))) if want.size else 1.0
    if np.iscomplexobj(got) or np.iscomplexobj(want):
        ok = bool(np.all(np.abs(got - want) <= np.maximum(absfrac * scale, rel * np.abs(want))))
        md = float(np.max(np.abs(got - want))) if got.size else 0.0
    else:
        ok = allclose(got, want, rel, absfrac * scale)
        md = maxdiff(got, want)
    report(label, ok, "" if ok else f"maxabsdiff {md:.3e} (scale {scale:.3e})")
    if show: print(f"   maxabsdiff {md:.3e}  scale {scale:.3e}")
    return ok

X1000 = rng.normal(size=1000) * 2.0 + 0.7
Y1000 = np.convolve(X1000, [0.5, 0.3, -0.2], mode='same') + rng.normal(size=1000)

# ================================================================= windows
print("# windows")
for M in (2, 7, 8, 256):
    w = mlab.window_hanning(np.ones(M))
    report(f"window_hanning(ones({M})) = 'Hanning (or Hann) window' 0.5-0.5cos(2 pi n/(M-1))",
           allclose(w, hann_sym(M), 1e-12, 1e-15))
xr = rng.normal(size=9)
report("window_hanning(x) = 'x times the Hanning window of len(x)'", allclose(mlab.window_hanning(xr), hann_sym(9) * xr, 1e-12, 1e-15))
report("window_none(x) returns x unchanged ('simply return x')", np.array_equal(mlab.window_none(xr), xr))

# ================================================================= detrend
print("# detrend helpers")
ints = [3, -1, 4, 1, -5, 9, 2, 6]
fm = sum(F(v) for v in ints) / len(ints)
report("detrend_mean(int list) = x - mean(x) (Fraction)", allclose(mlab.detrend_mean(ints), [float(F(v) - fm) for v in ints], 1e-15, 1e-15))
A2 = np.array([[1, 2, 9], [4, 0, -3]], dtype=float)
report("detrend_mean(2-D, axis=0) = column means removed", allclose(mlab.detrend_mean(A2, axis=0), A2 - A2.mean(0), 1e-15, 1e-15))
report("detrend_mean(2-D, axis=1) = row means removed", allclose(mlab.detrend_mean(A2, axis=1), A2 - A2.mean(1)[:, None], 1e-15, 1e-15))
report("detrend_mean(2-D, axis=None) = global mean removed ('see numpy.mean')", allclose(mlab.detrend_mean(A2), A2 - A2.mean(), 1e-15, 1e-15))
report("detrend_mean(1-D, axis=1) -> ValueError (axis out of bounds)", raises(lambda: mlab.detrend_mean([1., 2.], axis=1), ValueError))

def fr_linfit(y):
    n = len(y); I = [F(i) for i in range(n)]; Yf = [F(v) for v in y]
    ib = sum(I) / n; yb = sum(Yf) / n
    b = sum((i - ib) * (v - yb) for i, v in zip(I, Yf)) / sum((i - ib) ** 2 for i in I)
    return [float(v - (yb + b * (i - ib))) for i, v in zip(I, Yf)]
ints7 = [5, -2, 7, 7, 0, 3, -8]
report("detrend_linear(ints) = x minus least-squares line (Fraction)", allclose(mlab.detrend_linear(ints7), fr_linfit(ints7), 1e-12, 1e-13))
report("detrend_linear(exact line 3+2.5i) = 0", maxdiff(mlab.detrend_linear(3 + 2.5 * np.arange(20)), np.zeros(20)) < 1e-12)
report("detrend_linear(constant) = 0", maxdiff(mlab.detrend_linear(np.full(6, 4.25)), np.zeros(6)) < 1e-14)
report("detrend_linear(two points) = 0 (line through both)", maxdiff(mlab.detrend_linear([1.0, 7.0]), [0, 0]) < 1e-14)
r1 = quiet(mlab.detrend_linear, [5.0])
print(f"   detrend_linear([5.0]) -> {np.asarray(r1).tolist()}")
report("detrend_linear(single value) = 0 ('x minus best fit line'; a line fits one point exactly)",
       np.asarray(r1).shape == (1,) and abs(float(np.asarray(r1)[0])) < 1e-14, f"got {np.asarray(r1).tolist()}")
report("detrend_linear(0-D) = 0", float(mlab.detrend_linear(np.float64(3.5))) == 0.0)
zl = (1 + 2j) + (0.5 - 3j) * np.arange(12)
rz = mlab.detrend_linear(zl)
print(f"   detrend_linear((1+2i) + (0.5-3i) n): max |residual| {np.max(np.abs(rz)):.3e}")
report("detrend_linear(complex exact line) = 0 (psd/csd accept complex input with detrend='linear')", float(np.max(np.abs(rz))) < 1e-12,
       f"max |residual| {np.max(np.abs(rz)):.3e}")
zr = rng.normal(size=9) + 1j * rng.normal(size=9)
cmp("detrend_linear(complex) = x minus least-squares complex line", mlab.detrend_linear(zr), lin_detrend(zr), 1e-12, 1e-13)
report("detrend_linear(2-D) -> ValueError ('0-D or 1-D')", raises(lambda: mlab.detrend_linear(A2), ValueError))
report("detrend_none returns its input ('no detrending')", mlab.detrend_none(xr) is xr)
xs = np.array(ints7, dtype=float)
mean_t = xs - xs.mean()
for key in (None, 'default', 'constant', 'mean'):
    report(f"detrend(x, key={key!r}) = detrend_mean", allclose(mlab.detrend(xs, key=key), mean_t, 1e-14, 1e-14))
report("detrend(x, 'linear') = detrend_linear", allclose(mlab.detrend(xs, key='linear'), fr_linfit(ints7), 1e-12, 1e-13))
report("detrend(x, 'none') = x", allclose(mlab.detrend(xs, key='none'), xs, 0, 0))
report("detrend(x, callable) uses the callable", allclose(mlab.detrend(xs, key=lambda v: v - v[0]), xs - xs[0], 0, 0))
B = np.array([[1., 4., 0.], [3., 1., 2.], [8., 5., 9.], [10., 2., 3.]])
want = np.column_stack([fr_linfit(list(B[:, j])) for j in range(3)])
report("detrend(2-D, 'linear', axis=0) = per-column least-squares (Fraction)", allclose(mlab.detrend(B, key='linear', axis=0), want, 1e-12, 1e-13))
report("detrend(2-D, 'mean', axis=1) = row means removed", allclose(mlab.detrend(B, key='mean', axis=1), B - B.mean(1)[:, None], 1e-14, 1e-14))
report("detrend(x, 'bogus') -> ValueError", raises(lambda: mlab.detrend(xs, key='bogus'), ValueError))

# ================================================================= psd vs Welch reference
print("# psd against plain-numpy Welch (explicit DFT)")
neg_window = 1 - 1.9 * np.cos(2 * np.pi * np.arange(64) / 63) + 0.9 * np.cos(4 * np.pi * np.arange(64) / 63)  # has negative values
tri = 1 - np.abs((np.arange(50) - 24.5) / 25)
custom = lambda v: v - v[0]
cases = [
    ("defaults (NFFT 256, Fs 2, Hann, onesided, density)", dict(), dict()),
    ("NFFT=255 (odd)", dict(NFFT=255), dict(NFFT=255)),
    ("NFFT=128 noverlap=64 Fs=1000", dict(NFFT=128, noverlap=64, Fs=1000), dict(NFFT=128, noverlap=64, Fs=1000)),
    ("NFFT=100 noverlap=99 (maximum overlap)", dict(NFFT=100, noverlap=99), dict(NFFT=100, noverlap=99)),
    ("NFFT=100 pad_to=128 (even/even)", dict(NFFT=100, pad_to=128), dict(NFFT=100, pad_to=128)),
    ("NFFT=99 pad_to=101 (odd/odd)", dict(NFFT=99, pad_to=101), dict(NFFT=99, pad_to=101)),
    ("NFFT=99 pad_to=128 (odd NFFT, even pad_to: Nyquist bin present)", dict(NFFT=99, pad_to=128), dict(NFFT=99, pad_to=128)),
    ("NFFT=100 pad_to=101 (even NFFT, odd pad_to: no Nyquist bin)", dict(NFFT=100, pad_to=101), dict(NFFT=100, pad_to=101)),
    ("NFFT=63 pad_to=64 Fs=10 scale_by_freq=False", dict(NFFT=63, pad_to=64, Fs=10, scale_by_freq=False), dict(NFFT=63, pad_to=64, Fs=10, scale_by_freq=False)),
    ("scale_by_freq=False ('/ sum(w)^2')", dict(NFFT=128, scale_by_freq=False), dict(NFFT=128, scale_by_freq=False)),
    ("scale_by_freq=None (= True, documented default)", dict(NFFT=128, scale_by_freq=None), dict(NFFT=128)),
    ("detrend='mean'", dict(NFFT=128, detrend='mean'), dict(NFFT=128, detrend='mean')),
    ("detrend='linear'", dict(NFFT=128, detrend='linear'), dict(NFFT=128, detrend='linear')),
    ("detrend=mlab.detrend_linear (function)", dict(NFFT=128, detrend=mlab.detrend_linear), dict(NFFT=128, detrend='linear')),
    ("detrend=custom callable", dict(NFFT=128, detrend=custom), dict(NFFT=128, detrend=custom)),
    ("window=window_none", dict(NFFT=128, window=mlab.window_none), dict(NFFT=128, window=np.ones(128))),
    ("window=array (triangle, NFFT=50)", dict(NFFT=50, window=tri), dict(NFFT=50, window=tri)),
    ("window=array with negative values, density", dict(NFFT=64, window=neg_window), dict(NFFT=64, window=neg_window)),
    ("window=array with negative values, scale_by_freq=False", dict(NFFT=64, window=neg_window, scale_by_freq=False), dict(NFFT=64, window=neg_window, scale_by_freq=False)),
    ("sides='twosided' on real input", dict(NFFT=128, sides='twosided'), dict(NFFT=128, sides='twosided')),
    ("sides='twosided' odd NFFT=127", dict(NFFT=127, sides='twosided'), dict(NFFT=127, sides='twosided')),
    ("sides='default' (= onesided for real)", dict(NFFT=128, sides='default'), dict(NFFT=128)),
]
for label, kw, rkw in cases:
    P, f = mlab.psd(X1000, **kw)
    R, rf, _ = ref_spec(X1000, **rkw)
    cmp(f"psd {label}: Pxx", P, R.real)
    cmp(f"psd {label}: freqs", f, rf, 1e-12, 1e-15, show=False)

print("# psd input kinds / edge cases")
xi = rng.integers(-9, 10, size=300)
P, f = mlab.psd(xi, NFFT=64, noverlap=16); R, rf, _ = ref_spec(xi.astype(float), NFFT=64, noverlap=16)
cmp("psd integer input", P, R.real)
x32 = X1000.astype(np.float32)
P, f = mlab.psd(x32, NFFT=128); R, rf, _ = ref_spec(x32.astype(float), NFFT=128)
cmp("psd float32 input (Hann; truth on the float32 values)", P, R.real, 1e-9)
print(f"   dtype {P.dtype}")
P, f = mlab.psd(x32, NFFT=128, window=mlab.window_none); R, rf, _ = ref_spec(x32.astype(float), NFFT=128, window=np.ones(128))
cmp("psd float32 input, window_none (rel 1e-5: single precision accepted)", P, R.real, 1e-5, 1e-6)
print(f"   dtype {P.dtype}")
xs100 = X1000[:100]
P, f = mlab.psd(xs100, NFFT=256); R, rf, _ = ref_spec(xs100, NFFT=256)
cmp("psd len(x)=100 < NFFT=256 ('zero padded to NFFT')", P, R.real)
report("psd len(x) < NFFT: 129 bins", P.shape == (129,))
xc = rng.normal(size=600) + 1j * rng.normal(size=600)
P, f = mlab.psd(xc, NFFT=128, noverlap=32, Fs=5); R, rf, _ = ref_spec(xc, NFFT=128, noverlap=32, Fs=5)
cmp("psd complex input: default two-sided ('default' is two-sided for complex)", P, R.real)
cmp("psd complex input: freqs ascending -Fs/2..Fs/2-df", f, rf, 1e-12, 1e-15, show=False)
P, f = mlab.psd(xc, NFFT=127, Fs=5); R, rf, _ = ref_spec(xc, NFFT=127, Fs=5)
cmp("psd complex input odd NFFT=127", P, R.real)
cmp("psd complex input odd NFFT=127: freqs", f, rf, 1e-12, 1e-15, show=False)
P, f = mlab.psd(xc, NFFT=128, sides='onesided'); R, rf, _ = ref_spec(xc, NFFT=128, sides='onesided')
cmp("psd complex input sides='onesided' (forced)", P, R.real)
P, f = mlab.psd(xc, NFFT=128, detrend='linear'); R, rf, _ = ref_spec(xc, NFFT=128, detrend='linear')
cmp("psd complex input detrend='linear'", P, R.real)
P, f = mlab.psd(np.array([]), NFFT=16)
report("psd(empty) = zero-padded to NFFT -> all zeros, 9 bins", P.shape == (9,) and np.all(P == 0), f"got {P}")
P, f = mlab.psd([3.0], NFFT=1)
print(f"   psd([3.0], NFFT=1) -> {P.tolist()} freqs {f.tolist()}")
report("psd single value NFFT=1: Pxx = 9 / Fs = 4.5 (Parseval: 4.5 * Fs/1 = 9)", P.shape == (1,) and close(P[0], 4.5))
P, f = mlab.psd(np.full(512, 7.25), NFFT=128, detrend='mean')
report("psd constant input with detrend='mean' = 0", float(np.max(np.abs(P))) < 1e-25, f"max {np.max(np.abs(P)):.3e}")
P, f = mlab.psd(np.full(512, 7.25), NFFT=128, window=mlab.window_none)
want = np.zeros(65); want[0] = 7.25 ** 2 * 128 / 2
cmp("psd constant input, no detrend, boxcar: all power in DC = c^2 NFFT / Fs", P, want, 1e-12, 1e-14)
base = rng.integers(-9, 10, size=1024).astype(float)
P, f = mlab.psd(1e8 + base, NFFT=256, detrend='mean'); R, rf, _ = ref_spec(base, NFFT=256, detrend='mean')
cmp("psd large offset 1e8 + noise, detrend='mean' (rel 1e-6)", P, R.real, 1e-6, 1e-8)
report("psd noverlap = NFFT -> ValueError", raises(lambda: mlab.psd(X1000, NFFT=64, noverlap=64), ValueError), errname(lambda: mlab.psd(X1000, NFFT=64, noverlap=64)))
report("psd window length != NFFT -> ValueError", raises(lambda: mlab.psd(X1000, NFFT=64, window=np.ones(63)), ValueError))
report("psd sides='threesided' -> ValueError", raises(lambda: mlab.psd(X1000, sides='threesided'), ValueError))
xn = X1000.copy(); xn[500] = np.nan
P, f = mlab.psd(xn, NFFT=128)
print(f"   info: one NaN in x -> NaN bins: {int(np.isnan(P).sum())}/{P.size} (NaN handling undocumented)")
xm = np.ma.masked_array(X1000, mask=np.zeros(1000, bool)); xm[10:20] = np.ma.masked
P1, _ = mlab.psd(xm, NFFT=128); P2, _ = mlab.psd(xm.data, NFFT=128)
print(f"   info: masked input: mask ignored (psd(masked) == psd(data)): {bool(np.array_equal(P1, P2))} (undocumented)")
P, f = quiet(mlab.psd, X1000, NFFT=128, pad_to=100)
print(f"   info: pad_to=100 < NFFT=128 -> {P.shape[0]} bins; no error (pad_to < NFFT undocumented; fft truncates the windowed segment)")

# ================================================================= Parseval (exact)
print("# Parseval: sum(Pxx) * Fs / pad_to = variance (detrend='mean', boxcar, one segment)")
for N, pad in ((64, 64), (64, 128), (64, 65), (64, 127), (63, 63), (63, 64), (63, 128), (63, 101)):
    xi = [int(v) for v in rng.integers(-9, 10, size=N)]
    m = F(sum(xi), N); var = sum((F(v) - m) ** 2 for v in xi) / N
    Fs = 4
    P, f = mlab.psd(np.array(xi, float), NFFT=N, Fs=Fs, window=mlab.window_none, detrend='mean', pad_to=pad)
    tot = float(np.sum(P)) * Fs / pad
    print(f"   NFFT={N} pad_to={pad}: sum*df = {tot:.15g}  variance = {float(var):.15g}")
    report(f"Parseval one-sided NFFT={N} pad_to={pad}", close(tot, float(var), 1e-12), f"sum*df {tot:.12g} vs var {float(var):.12g} (ratio {tot/float(var):.6f})")
xi = [int(v) for v in rng.integers(-9, 10, size=64)]
m = F(sum(xi), 64); var = sum((F(v) - m) ** 2 for v in xi) / 64
P, f = mlab.psd(np.array(xi, float), NFFT=64, Fs=4, window=mlab.window_none, detrend='mean', sides='twosided', pad_to=96)
report("Parseval two-sided real NFFT=64 pad_to=96", close(float(np.sum(P)) * 4 / 96, float(var), 1e-12))
xr_ = [int(v) for v in rng.integers(-9, 10, size=50)]; xi_ = [int(v) for v in rng.integers(-9, 10, size=50)]
zc = np.array(xr_, float) + 1j * np.array(xi_, float)
ms = F(sum(a * a + b * b for a, b in zip(xr_, xi_)), 50)
P, f = mlab.psd(zc, NFFT=50, Fs=3, window=mlab.window_none)
report("Parseval complex two-sided: sum*df = mean |x|^2", close(float(np.sum(P)) * 3 / 50, float(ms), 1e-12))

# ================================================================= closed forms
print("# closed forms")
N, k0, A, phi = 64, 5, 3.0, 0.7
xcos = A * np.cos(2 * np.pi * k0 * np.arange(N) / N + phi)
P, f = mlab.psd(xcos, NFFT=N, Fs=N, window=mlab.window_none, scale_by_freq=False)
print(f"   psd peak {P[k0]:.15g} at f={f[k0]}; rest max {np.max(np.delete(P, k0)):.3e}")
report("psd of A cos at bin k0, boxcar, scale_by_freq=False: one-sided peak = A^2/2 (power of the tone)", close(P[k0], A * A / 2, 1e-12))
report("psd of A cos: no power off bin k0", float(np.max(np.delete(P, k0))) < 1e-24)
Mg, f = mlab.magnitude_spectrum(xcos, Fs=N, window=mlab.window_none)
print(f"   magnitude_spectrum one-sided peak {Mg[k0]:.15g} (A = {A})")
report("magnitude_spectrum one-sided peak = A/2 (|DFT|/sum(w); no one-sided doubling)", close(Mg[k0], A / 2, 1e-12))
Mg2, f2 = mlab.magnitude_spectrum(xcos, Fs=N, window=mlab.window_none, sides='twosided')
i_p = int(np.argmin(np.abs(f2 - k0))); i_m = int(np.argmin(np.abs(f2 + k0)))
report("magnitude_spectrum two-sided peaks = A/2 at +-f0", close(Mg2[i_p], A / 2, 1e-12) and close(Mg2[i_m], A / 2, 1e-12))
Cs, f = mlab.complex_spectrum(xcos, Fs=N, window=mlab.window_none)
report("complex_spectrum at k0 = (A/2) exp(i phi)", abs(Cs[k0] - A / 2 * np.exp(1j * phi)) < 1e-12)
An, f = mlab.angle_spectrum(xcos, Fs=N, window=mlab.window_none)
report("angle_spectrum at k0 = phi", close(An[k0], phi, 1e-12))
# white noise
sig, Fs = 1.5, 100.0
wn = rng.normal(scale=sig, size=2 ** 18)
P, f = mlab.psd(wn, NFFT=256, Fs=Fs)
lev = float(np.mean(P[1:-1])); want = 2 * sig ** 2 / Fs
print(f"   white noise sigma={sig}, Fs={Fs}: mean one-sided level {lev:.6g}, 2 sigma^2/Fs = {want:.6g} (ratio {lev/want:.5f})")
report("white noise one-sided density level = 2 sigma^2 / Fs (within 2%)", abs(lev / want - 1) < 0.02)
P2, f2 = mlab.psd(wn, NFFT=256, Fs=Fs, sides='twosided')
lev2 = float(np.mean(P2)); print(f"   two-sided mean level {lev2:.6g} vs sigma^2/Fs {sig**2/Fs:.6g}")
report("white noise two-sided density level = sigma^2 / Fs (within 2%)", abs(lev2 / (sig ** 2 / Fs) - 1) < 0.02)
tot = float(np.sum(P)) * Fs / 256; v = float(np.var(wn))
print(f"   integral of PSD {tot:.6g} vs sample variance {v:.6g}")
report("white noise: integral of one-sided PSD = variance (within 2%)", abs(tot / v - 1) < 0.02)
Pf, _ = mlab.psd(wn, NFFT=256, Fs=Fs, scale_by_freq=False)
w = hann_sym(256); lvf = float(np.mean(Pf[1:-1])); wf = 2 * sig ** 2 * np.sum(w ** 2) / np.sum(w) ** 2
print(f"   scale_by_freq=False level {lvf:.6g} vs 2 sigma^2 sum(w^2)/sum(w)^2 = {wf:.6g}")
report("white noise scale_by_freq=False level = 2 sigma^2 sum(w^2)/sum(w)^2 (within 2%)", abs(lvf / wf - 1) < 0.02)
# documented meaning of scale_by_freq
Pt, _ = mlab.psd(X1000, NFFT=128, Fs=10, scale_by_freq=True)
Pf, _ = mlab.psd(X1000, NFFT=128, Fs=10, scale_by_freq=False)
ratio = float(np.median(Pf / Pt))
print(f"   Pxx(False)/Pxx(True) = {ratio:.6g} (Fs = 10; sum(w)^2/sum(w^2)/Fs-free ratio = {np.sum(hann_sym(128))**2/np.sum(hann_sym(128)**2):.6g})")
report("scale_by_freq docs: 'Whether the resulting density values should be divided by the sampling frequency' -> Pxx(False) = Fs * Pxx(True)",
       close(ratio, 10.0, 1e-9), f"ratio {ratio:.6g}, not Fs = 10 (the window normalisation also changes from sum(w^2) to sum(w)^2)")
P1, _ = mlab.psd(X1000, NFFT=128, Fs=10, window=mlab.window_none, scale_by_freq=True)
P2, _ = mlab.psd(X1000, NFFT=128, Fs=10, window=mlab.window_none, scale_by_freq=False)
report("boxcar window: Pxx(False)/Pxx(True) = Fs sum(w^2)/sum(w)^2 = Fs/NFFT",
       allclose(P2, P1 * 10 / 128, 1e-12, 1e-30))

# ================================================================= csd
print("# csd")
for label, kw in (("defaults", {}), ("NFFT=100 noverlap=50 pad_to=128 Fs=7", dict(NFFT=100, noverlap=50, pad_to=128, Fs=7)),
                  ("NFFT=99 pad_to=128", dict(NFFT=99, pad_to=128)),
                  ("detrend='linear' scale_by_freq=False", dict(NFFT=128, detrend='linear', scale_by_freq=False)),
                  ("sides='twosided'", dict(NFFT=128, sides='twosided'))):
    C, f = mlab.csd(X1000, Y1000, **kw)
    R, rf, _ = ref_spec(X1000, Y1000, **kw)
    cmp(f"csd {label}: Pxy = mean conj(X) Y scaled", C, R)
    cmp(f"csd {label}: freqs", f, rf, 1e-12, 1e-15, show=False)
C, f = mlab.csd(X1000[:170], Y1000[:150], NFFT=200)
R, rf, _ = ref_spec(X1000[:170], Y1000[:150], NFFT=200)
cmp("csd x (170) and y (150) shorter than NFFT=200 ('they will be zero padded to NFFT')", C, R)
C, f = mlab.csd(X1000, Y1000[:150], NFFT=200)
print(f"   info: csd(len(x)=1000, len(y)=150, NFFT=200) -> no error, shape {C.shape}: the single zero-padded y segment is paired with all 5 x segments (unequal lengths undocumented)")
print(f"   info: csd(len(x)=1000, len(y)=900, NFFT=200) -> {errname(lambda: mlab.csd(X1000, Y1000[:900], NFFT=200))}")
C, f = mlab.csd(xc, xc[::-1].copy(), NFFT=128)
R, rf, _ = ref_spec(xc, xc[::-1].copy(), NFFT=128)
cmp("csd complex inputs (two-sided)", C, R)
C, f = mlab.csd(X1000, Y1000, NFFT=128)
print(f"   csd dtype {C.dtype}, max |imag| {np.max(np.abs(C.imag)):.3e}")
report("mlab.csd docstring 'Pxy ... (real valued)': returned Pxy is real", not np.iscomplexobj(C), f"dtype {C.dtype}, max|imag| {np.max(np.abs(C.imag)):.3e}")

# ================================================================= cohere
print("# cohere")
Cx, f = mlab.cohere(X1000, Y1000, NFFT=128, Fs=4, noverlap=64)
Pxy = ref_spec(X1000, Y1000, NFFT=128, Fs=4, noverlap=64)[0]
Pxx = ref_spec(X1000, NFFT=128, Fs=4, noverlap=64)[0].real
Pyy = ref_spec(Y1000, NFFT=128, Fs=4, noverlap=64)[0].real
cmp("cohere = |Pxy|^2/(Pxx Pyy) (reference Welch)", Cx, np.abs(Pxy) ** 2 / (Pxx * Pyy))
print(f"   min {Cx.min():.4g} max {Cx.max():.4g}")
report("cohere in [0, 1]", bool(np.all((Cx >= 0) & (Cx <= 1 + 1e-12))))
Cx, f = mlab.cohere(X1000, Y1000, 99, 4, mlab.detrend_none, mlab.window_hanning, 0, 128)
Pxy = ref_spec(X1000, Y1000, NFFT=99, Fs=4, pad_to=128)[0]
Pxx = ref_spec(X1000, NFFT=99, Fs=4, pad_to=128)[0].real; Pyy = ref_spec(Y1000, NFFT=99, Fs=4, pad_to=128)[0].real
cmp("cohere NFFT=99 pad_to=128 (positional args)", Cx, np.abs(Pxy) ** 2 / (Pxx * Pyy))
Cx, f = mlab.cohere(X1000, -2.5 * X1000, NFFT=128)
report("cohere(x, -2.5 x) = 1 at every bin", maxdiff(Cx, np.ones_like(Cx)) < 1e-12, f"maxdiff {maxdiff(Cx, np.ones_like(Cx)):.3e}")
z1 = rng.normal(size=4096); z2 = rng.normal(size=4096)
Cx, f = mlab.cohere(z1, z2, NFFT=64)
print(f"   independent noise, 64 segments: mean coherence {Cx.mean():.4f} (expected about 1/K = {1/64:.4f})")
report("cohere of independent noise ~ 1/K (K=64 segments; mean within [0.5/K, 2/K])", 0.5 / 64 < Cx.mean() < 2 / 64)
print(f"   info: cohere(len(x) < 2*NFFT) -> {errname(lambda: mlab.cohere(X1000[:300], Y1000[:300], NFFT=256))} (not in the docstring)")
Cx, f = mlab.cohere(xc, xc * (1 + 2j), NFFT=64)
report("cohere complex input, y = (1+2i) x -> 1 at every two-sided bin", f.shape == (64,) and maxdiff(Cx, np.ones(64)) < 1e-12)

# ================================================================= specgram
print("# specgram")
xs2 = rng.normal(size=2000) + 0.5 * np.sin(2 * np.pi * 0.1 * np.arange(2000))
for label, kw, rkw in (
        ("NFFT=128 noverlap=64 Fs=50 psd", dict(NFFT=128, noverlap=64, Fs=50), dict(NFFT=128, noverlap=64, Fs=50)),
        ("defaults (NFFT 256, noverlap 128, Fs 2)", dict(), dict(NFFT=256, noverlap=128)),
        ("NFFT=129 noverlap=0 pad_to=256 detrend='linear' scale_by_freq=False", dict(NFFT=129, noverlap=0, pad_to=256, detrend='linear', scale_by_freq=False),
         dict(NFFT=129, noverlap=0, pad_to=256, detrend='linear', scale_by_freq=False)),
        ("NFFT=100 noverlap=30 sides='twosided'", dict(NFFT=100, noverlap=30, sides='twosided'), dict(NFFT=100, noverlap=30, sides='twosided')),
        ("mode='magnitude'", dict(NFFT=128, noverlap=0, mode='magnitude'), dict(NFFT=128, mode='magnitude')),
        ("mode='complex'", dict(NFFT=128, noverlap=0, mode='complex'), dict(NFFT=128, mode='complex')),
        ("mode='angle'", dict(NFFT=128, noverlap=0, mode='angle'), dict(NFFT=128, mode='angle')),
        ("mode='magnitude' scale_by_freq=True (ignored per Notes)", dict(NFFT=128, noverlap=0, mode='magnitude', scale_by_freq=True), dict(NFFT=128, mode='magnitude')),
        ):
    S, f, t = mlab.specgram(xs2, **kw)
    R, rf, rt = ref_spec(xs2, average=False, **rkw)
    if kw.get('mode') == 'angle':   # compare angles modulo 2 pi (a bin with ~0 imaginary part may sit at +pi or -pi)
        dd = np.angle(np.exp(1j * (S - R.real)))
        report(f"specgram {label}: spectrum columns (mod 2 pi)", float(np.max(np.abs(dd))) < 1e-9, f"max {np.max(np.abs(dd)):.3e}")
        print(f"   max wrapped diff {np.max(np.abs(dd)):.3e}; raw diffs of 2 pi at {int(np.sum(np.abs(S - R.real) > 6))} entries (+pi vs -pi)")
    else:
        cmp(f"specgram {label}: spectrum columns", S, R if np.iscomplexobj(S) else R.real, 1e-9, 1e-11)
    cmp(f"specgram {label}: freqs", f, rf, 1e-12, 1e-15, show=False)
    cmp(f"specgram {label}: t = segment midpoints (start + NFFT/2)/Fs", t, rt, 1e-12, 1e-15, show=False)
S, f, t = mlab.specgram(xs2, NFFT=128, noverlap=0, mode='phase')
An, _, _ = mlab.specgram(xs2, NFFT=128, noverlap=0, mode='angle')
k2 = np.round((S - An) / (2 * np.pi))
report("specgram mode='phase' = angle + 2 pi k ('phase spectrum with unwrapping')", maxdiff(S - An, 2 * np.pi * k2) < 1e-9)
report("specgram mode='phase': |successive differences along freq| <= pi", float(np.max(np.abs(np.diff(S, axis=0)))) <= np.pi + 1e-12)
# Notes: 'detrend and scale_by_freq only apply when mode is set to psd'
xo = xs2 + 40.0
S, f, t = mlab.specgram(xo, NFFT=128, noverlap=0, mode='magnitude', detrend='mean')
R, _, _ = ref_spec(xo, NFFT=128, mode='magnitude', average=False)
R2, _, _ = ref_spec(xo, NFFT=128, mode='magnitude', average=False, detrend='mean')
print(f"   magnitude DC bin, first segment: got {S[0,0]:.6g}; without detrend {R[0,0]:.6g}; with detrend {R2[0,0]:.6g}")
cmp("specgram Notes: 'detrend ... only appl[ies] when mode is psd' -> mode='magnitude', detrend='mean' equals no detrend", S, R.real)
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always")
    S, f, t = mlab.specgram(X1000[:200], NFFT=256, noverlap=0)
R, rf, rt = ref_spec(X1000[:200], NFFT=256, average=False)
cmp("specgram len(x)=200 < NFFT=256: one zero-padded segment", S, R.real)
report("specgram len(x) < NFFT: t = [NFFT/2/Fs]", allclose(t, [128 / 2], 1e-12))
report("specgram len(x) <= NFFT warns ('Only one segment')", any("one segment" in str(w_.message) for w_ in wl))
S, f, t = mlab.specgram(xc[:512], NFFT=64, noverlap=16)
R, rf, rt = ref_spec(xc[:512], NFFT=64, noverlap=16, average=False)
cmp("specgram complex input (two-sided)", S, R.real)
cmp("specgram complex input: freqs", f, rf, 1e-12, 1e-15, show=False)
print(f"   info: specgram(x, NFFT=64) with default noverlap -> {errname(lambda: mlab.specgram(xs2, NFFT=64))}")

# ================================================================= single-spectrum functions
print("# complex / magnitude / angle / phase spectrum")
xsig = X1000[:301]
for fn, mode in ((mlab.complex_spectrum, 'complex'), (mlab.magnitude_spectrum, 'magnitude'),
                 (mlab.angle_spectrum, 'angle'), (mlab.phase_spectrum, 'phase')):
    for label, kw in (("default (Hann, onesided)", {}), ("pad_to=512 Fs=8", dict(pad_to=512, Fs=8)),
                      ("sides='twosided' window_none", dict(sides='twosided', window=mlab.window_none)),
                      ("pad_to=400 (even pad_to, odd len)", dict(pad_to=400))):
        Sx, f = fn(xsig, **kw)
        rkw = dict(kw)
        if rkw.get('window') is mlab.window_none: rkw['window'] = np.ones(len(xsig))
        R, rf, _ = ref_spec(xsig, NFFT=len(xsig), mode=mode, **rkw)
        cmp(f"{fn.__name__ if hasattr(fn, '__name__') else mode + '_spectrum'} {mode} {label}", Sx, R if mode == 'complex' else R.real, 1e-9, 1e-11, show=False)
        cmp(f"{mode}_spectrum {label}: freqs", f, rf, 1e-12, 1e-15, show=False)
Sx, f = mlab.magnitude_spectrum(xc[:200])
R, rf, _ = ref_spec(xc[:200], NFFT=200, mode='magnitude')
cmp("magnitude_spectrum complex input (two-sided default)", Sx, R.real, 1e-9, 1e-11, show=False)

# ================================================================= scipy cross-checks
if HAVE_SCIPY:
    print("# scipy.signal (informational truth where installed)")
    def sp_detr(d): return {None: False, 'none': False, 'mean': 'constant', 'linear': 'linear'}[d]
    for label, kw in (("NFFT=256", dict(NFFT=256)), ("NFFT=128 noverlap=96 Fs=30", dict(NFFT=128, noverlap=96, Fs=30)),
                      ("NFFT=100 pad_to=128 detrend=mean", dict(NFFT=100, pad_to=128, detrend='mean')),
                      ("NFFT=99 pad_to=128", dict(NFFT=99, pad_to=128)), ("NFFT=100 pad_to=101", dict(NFFT=100, pad_to=101)),
                      ("NFFT=127 detrend=linear scale_by_freq=False", dict(NFFT=127, detrend='linear', scale_by_freq=False)),
                      ("NFFT=128 twosided", dict(NFFT=128, sides='twosided'))):
        NF = kw['NFFT']; Fs_ = kw.get('Fs', 2); nov = kw.get('noverlap', 0); pt = kw.get('pad_to', NF)
        two = kw.get('sides') == 'twosided'
        P, f = mlab.psd(X1000, **kw)
        fs_, Ps = ss.welch(X1000, fs=Fs_, window=np.hanning(NF), nperseg=NF, noverlap=nov, nfft=pt,
                           detrend=sp_detr(kw.get('detrend')), return_onesided=not two,
                           scaling='density' if kw.get('scale_by_freq', True) else 'spectrum')
        if two: fs_, Ps = np.fft.fftshift(fs_), np.fft.fftshift(Ps)
        if not two and pt % 2 == 0: fs_ = np.abs(fs_)
        cmp(f"(scipy) psd {label} = scipy.signal.welch", P, Ps, 1e-9, 1e-12, show=False)
        cmp(f"(scipy) psd {label}: freqs = welch freqs", f, fs_, 1e-12, 1e-15, show=False)
        C, f = mlab.csd(X1000, Y1000, **kw)
        fs_, Cs_ = ss.csd(X1000, Y1000, fs=Fs_, window=np.hanning(NF), nperseg=NF, noverlap=nov, nfft=pt,
                          detrend=sp_detr(kw.get('detrend')), return_onesided=not two,
                          scaling='density' if kw.get('scale_by_freq', True) else 'spectrum')
        if two: Cs_ = np.fft.fftshift(Cs_)
        cmp(f"(scipy) csd {label} = scipy.signal.csd", C, Cs_, 1e-9, 1e-12, show=False)
    Cx, f = mlab.cohere(X1000, Y1000, NFFT=128, noverlap=64, Fs=4)
    fs_, Cxs = ss.coherence(X1000, Y1000, fs=4, window=np.hanning(128), nperseg=128, noverlap=64, detrend=False)
    cmp("(scipy) cohere = scipy.signal.coherence", Cx, Cxs, 1e-9, 1e-12, show=False)
    for mode in ('psd', 'magnitude', 'complex', 'angle', 'phase'):
        S, f, t = mlab.specgram(xs2, NFFT=128, noverlap=32, Fs=10, mode=mode)
        fs_, ts_, Ss = ss.spectrogram(xs2, fs=10, window=np.hanning(128), nperseg=128, noverlap=32, detrend=False,
                                      scaling='density' if mode == 'psd' else 'spectrum', mode=mode)
        cmp(f"(scipy) specgram mode={mode} = scipy.signal.spectrogram", S, Ss, 1e-9, 1e-11, show=False)
        if mode == 'psd':
            cmp("(scipy) specgram t = scipy.signal.spectrogram t (segment centres)", t, ts_, 1e-12, 1e-15, show=False)
else:
    print("# scipy not installed: scipy cross-checks skipped")

# ================================================================= Axes wrappers
print("# Axes wrappers")
fig = Figure(); ax = fig.add_subplot()
has_funits = 'Funits' in inspect.signature(type(ax).psd).parameters
print(f"   Axes.psd has Funits: {has_funits}")
R, rf, _ = ref_spec(X1000, NFFT=128, Fs=20, noverlap=32)
out = ax.psd(X1000, NFFT=128, Fs=20, noverlap=32, Fc=1000, return_line=True)
report("Axes.psd(return_line=True) returns (Pxx, freqs, line)", len(out) == 3)
Pxx, fr, line = out
from matplotlib.lines import Line2D
print(f"   type of returned line: {type(line).__name__}")
report("Axes.psd returned 'line : Line2D' is a Line2D", isinstance(line, Line2D), f"got {type(line).__name__}")
if isinstance(line, list): line = line[0]
cmp("Axes.psd returned Pxx is the linear density ('Pxx itself is returned')", Pxx, R.real, show=False)
cmp("Axes.psd returned freqs = k Fs/NFFT + Fc", fr, rf + 1000, 1e-12, 1e-15, show=False)
cmp("Axes.psd line xdata = freqs + Fc", line.get_xdata(), rf + 1000, 1e-12, 1e-15, show=False)
cmp("Axes.psd line ydata = 10 log10(Pxx) ('plotted as 10 log10(Pxx)')", line.get_ydata(), 10 * np.log10(R.real), 1e-9, 1e-12, show=False)
ax.cla()
out = ax.psd(X1000, NFFT=128)
report("Axes.psd default return_line -> (Pxx, freqs)", len(out) == 2)
out = ax.psd(X1000, NFFT=128, return_line=False)
report("Axes.psd return_line=False -> (Pxx, freqs)", len(out) == 2)
ax.cla()
R, rf, _ = ref_spec(X1000, NFFT=99, pad_to=128, Fs=3, scale_by_freq=False)
Pxx, fr, line = ax.psd(X1000, NFFT=99, pad_to=128, Fs=3, scale_by_freq=False, return_line=True)
if isinstance(line, list): line = line[0]
cmp("Axes.psd NFFT=99 pad_to=128 scale_by_freq=False: Pxx", Pxx, R.real, show=False)
cmp("Axes.psd NFFT=99 pad_to=128: ydata = 10 log10(Pxx)", line.get_ydata(), 10 * np.log10(Pxx), 1e-12, 1e-12, show=False)
ax.cla()
R, rf, _ = ref_spec(xc, NFFT=64, Fs=8)
Pxx, fr = ax.psd(xc, NFFT=64, Fs=8, Fc=100)
cmp("Axes.psd complex input: two-sided Pxx", Pxx, R.real, show=False)
cmp("Axes.psd complex input: freqs = Fc - Fs/2 .. Fc + Fs/2 - df (ascending)", fr, rf + 100, 1e-12, 1e-15, show=False)
cmp("Axes.psd complex input: line ydata = 10 log10(Pxx)", ax.get_lines()[-1].get_ydata(), 10 * np.log10(R.real), 1e-9, 1e-12, show=False)
ax.cla()
R, rf, _ = ref_spec(X1000, Y1000, NFFT=128, Fs=20)
Pxy, fr, line = ax.csd(X1000, Y1000, NFFT=128, Fs=20, Fc=-5, return_line=True)
report("Axes.csd returned 'line : Line2D' is a Line2D", isinstance(line, Line2D), f"got {type(line).__name__}")
if isinstance(line, list): line = line[0]
cmp("Axes.csd returned Pxy (complex) = reference", Pxy, R, show=False)
report("Axes.csd Pxy documented '(complex valued)'", np.iscomplexobj(Pxy))
cmp("Axes.csd freqs = k Fs/NFFT + Fc", fr, rf - 5, 1e-12, 1e-15, show=False)
cmp("Axes.csd line ydata = 10 log10 |Pxy|", line.get_ydata(), 10 * np.log10(np.abs(R)), 1e-9, 1e-12, show=False)
ax.cla()
for scale, fz in ((None, lambda v: v), ('linear', lambda v: v), ('dB', lambda v: 20 * np.log10(v))):
    R, rf, _ = ref_spec(xsig, NFFT=len(xsig), mode='magnitude', Fs=6, pad_to=512)
    sp, fr, line = ax.magnitude_spectrum(xsig, Fs=6, Fc=2, pad_to=512, scale=scale)
    cmp(f"Axes.magnitude_spectrum scale={scale!r}: returned spectrum is linear magnitude", sp, R.real, 1e-9, 1e-11, show=False)
    cmp(f"Axes.magnitude_spectrum scale={scale!r}: ydata ({'20 log10' if scale == 'dB' else 'linear'})",
        line.get_ydata(), fz(R.real), 1e-9, 1e-11, show=False)
    cmp(f"Axes.magnitude_spectrum scale={scale!r}: xdata = freqs + Fc", line.get_xdata(), rf + 2, 1e-12, 1e-15, show=False)
    ax.cla()
for meth, mode in ((ax.angle_spectrum, 'angle'), (ax.phase_spectrum, 'phase')):
    R, rf, _ = ref_spec(xsig, NFFT=len(xsig), mode=mode, Fs=6)
    sp, fr, line = meth(xsig, Fs=6, Fc=-1)
    cmp(f"Axes.{mode}_spectrum returned spectrum", sp, R.real, 1e-9, 1e-11, show=False)
    cmp(f"Axes.{mode}_spectrum ydata", line.get_ydata(), R.real, 1e-9, 1e-11, show=False)
    cmp(f"Axes.{mode}_spectrum xdata = freqs + Fc", line.get_xdata(), rf - 1, 1e-12, 1e-15, show=False)
    ax.cla()
Cx, fr = ax.cohere(X1000, Y1000, NFFT=128, Fs=4, Fc=3)
Pxy = ref_spec(X1000, Y1000, NFFT=128, Fs=4)[0]
Pxx = ref_spec(X1000, NFFT=128, Fs=4)[0].real; Pyy = ref_spec(Y1000, NFFT=128, Fs=4)[0].real
cmp("Axes.cohere returned Cxy", Cx, np.abs(Pxy) ** 2 / (Pxx * Pyy), show=False)
cmp("Axes.cohere freqs = k Fs/NFFT + Fc", fr, np.arange(65) * 4 / 128 + 3, 1e-12, 1e-15, show=False)
ln = ax.get_lines()[-1]
cmp("Axes.cohere line ydata = Cxy, xdata = freqs", np.concatenate([ln.get_ydata(), ln.get_xdata()]), np.concatenate([Cx, fr]), 1e-12, 1e-15, show=False)
ax.cla()
for mode, scale, fz in (('psd', None, lambda v: 10 * np.log10(v)), ('psd', 'linear', lambda v: v),
                        ('magnitude', None, lambda v: 20 * np.log10(v)), ('magnitude', 'linear', lambda v: v),
                        ('angle', None, lambda v: v), ('phase', None, lambda v: v)):
    NF, nov, Fs_, Fc_ = 128, 64, 50.0, 7.0
    sp, fr, t, im = ax.specgram(xs2, NFFT=NF, noverlap=nov, Fs=Fs_, Fc=Fc_, mode=mode, scale=scale)
    R, rf, rt = ref_spec(xs2, NFFT=NF, noverlap=nov, Fs=Fs_, mode=mode, average=False)
    if mode == 'angle':   # angles compared modulo 2 pi (+pi / -pi at bins with ~0 imaginary part)
        d1 = float(np.max(np.abs(np.angle(np.exp(1j * (sp - R.real))))))
        d2 = float(np.max(np.abs(np.angle(np.exp(1j * (np.asarray(im.get_array()) - np.flipud(R.real)))))))
        report(f"Axes.specgram mode={mode} scale={scale}: returned spectrum (mod 2 pi)", d1 < 1e-9, f"max {d1:.3e}")
        report(f"Axes.specgram mode={mode} scale={scale}: image array = flipud(linear) (mod 2 pi)", d2 < 1e-9, f"max {d2:.3e}")
    else:
        cmp(f"Axes.specgram mode={mode} scale={scale}: returned spectrum", sp, R.real, 1e-9, 1e-11, show=False)
        cmp(f"Axes.specgram mode={mode} scale={scale}: image array = flipud({'dB' if scale is None and mode in ('psd','magnitude') else 'linear'})",
            np.asarray(im.get_array()), np.flipud(fz(R.real)), 1e-9, 1e-11, show=False)
    if mode == 'psd' and scale is None:
        cmp("Axes.specgram returned freqs = freqs + Fc", fr, rf + Fc_, 1e-12, 1e-15, show=False)
        cmp("Axes.specgram returned t = segment midpoints", t, rt, 1e-12, 1e-15, show=False)
        x0, x1, y0, y1 = im.get_extent()
        nr, nc = sp.shape
        colc = x0 + (np.arange(nc) + 0.5) * (x1 - x0) / nc
        rowc = y0 + (np.arange(nr) + 0.5) * (y1 - y0) / nr      # image is flipud: row 0 from the bottom is freqs[0]
        print(f"   extent {im.get_extent()}; first/last freqs {fr[0]}, {fr[-1]}; first/last row centres {rowc[0]:.6g}, {rowc[-1]:.6g}")
        cmp("Axes.specgram image column centres = t ('xmin left border of the first bin')", colc, rt, 1e-12, 1e-12, show=False)
        cmp("Axes.specgram image row centres = freqs (rows of spectrum)", rowc, rf + Fc_, 1e-9, 1e-9, show=True)
    ax.cla()
report("Axes.specgram mode='complex' -> ValueError ('Cannot plot a complex specgram')",
       raises(lambda: ax.specgram(xs2, NFFT=128, mode='complex'), ValueError))
report("Axes.specgram mode='angle' scale='dB' -> ValueError (documented 'must be linear')",
       raises(lambda: ax.specgram(xs2, NFFT=128, mode='angle', scale='dB'), ValueError))
print("done")
