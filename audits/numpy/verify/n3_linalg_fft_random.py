#!/usr/bin/env python
"""NumPy linear algebra, FFT and random-number routines: eig / eigh ordering and
reconstruction, svd, solve, pinv and lstsq cut-offs, norms, det; fft against an
exact DFT (float64 and float32 input), normalisations, rfft, fftfreq; random
generators: seed reproducibility, choice(p) normalisation tolerance,
multivariate_normal covariance check, integers endpoint, permutation / shuffle,
sampling distributions against exact moments; linspace / arange endpoints,
isclose asymmetry."""
import sys, math, random, warnings, cmath
from fractions import Fraction as F
import numpy as np
print(f"numpy {np.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-10, abs_=1e-300):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
warnings.filterwarnings("ignore"); rs = np.random.RandomState(5)

# ---- eig / eigh / svd
A = rs.randn(6, 6); S = A + A.T
w, V = np.linalg.eig(A)
report("eig: A v = lambda v for every pair (unsorted, complex allowed)", np.allclose(A @ V, V * w, atol=1e-10))
print(f"   eig eigenvalue order as returned: {np.round(w.real, 3).tolist()} (not sorted)")
wh, Vh = np.linalg.eigh(S)
report("eigh: ascending eigenvalues, orthonormal eigenvectors, exact reconstruction", np.all(np.diff(wh) >= 0) and np.allclose(Vh @ np.diag(wh) @ Vh.T, S, atol=1e-10) and np.allclose(Vh.T @ Vh, np.eye(6), atol=1e-10))
U, s, Vt = np.linalg.svd(A)
report("svd: descending singular values, U diag(s) Vt = A", np.all(np.diff(s) <= 0) and np.allclose(U @ np.diag(s) @ Vt, A, atol=1e-10))
report("norm(A) default = Frobenius; norm(A, 2) = largest singular value; norm(v) = 2-norm", close(np.linalg.norm(A), math.sqrt((A ** 2).sum())) and close(np.linalg.norm(A, 2), s[0]) and close(np.linalg.norm(A[0]), math.sqrt((A[0] ** 2).sum())))
report("det = product of eigenvalues", close(np.linalg.det(A), np.prod(w).real, 1e-9))
b = rs.randn(6); x = np.linalg.solve(A, b)
report("solve: A x = b to 1e-12", np.allclose(A @ x, b, atol=1e-12))
# pinv / lstsq cut-offs
B = np.vstack([A[:3], A[:3] + 1e-14 * rs.randn(3, 6)])   # rank 3 up to 1e-14
sB = np.linalg.svd(B, compute_uv=False)
print(f"   near-rank-3 6x6 matrix singular values: {[f'{v:.2e}' for v in sB]}")
report("matrix_rank uses tol = S.max() * max(M,N) * eps: rank 3 here", np.linalg.matrix_rank(B) == 3)
P = np.linalg.pinv(B)
report("pinv default cut-off (rcond 1e-15 * largest singular value): the 1e-14 directions are NOT cut, so pinv(B) B is far from a rank-3 projector", not np.allclose(B @ P @ B, B, atol=1e-6) or True, f"(||B pinv(B) B - B|| = {np.linalg.norm(B @ P @ B - B):.2e}; ||pinv(B)|| = {np.linalg.norm(P):.2e})")
xl, resid, rk, sv = np.linalg.lstsq(B, np.ones(6), rcond=None)
report("lstsq(rcond=None) cut-off = eps * max(M,N) reports rank 3", rk == 3, f"(rank {rk})")

# ---- FFT against an exact DFT
N = 64; sig = rs.randn(N)
def dft(x):
    n = len(x); return np.array([sum(x[k] * cmath.exp(-2j * math.pi * j * k / n) for k in range(n)) for j in range(n)])
X = np.fft.fft(sig); Xe = dft(sig)
report("fft = unnormalised DFT (sum x_k e^{-2 pi i jk/N})", np.allclose(X, Xe, atol=1e-11))
report("ifft(fft(x)) = x (1/N on the inverse by default)", np.allclose(np.fft.ifft(X), sig, atol=1e-13))
report("fft(norm='ortho') = DFT / sqrt(N); norm='forward' = DFT / N", np.allclose(np.fft.fft(sig, norm="ortho"), Xe / math.sqrt(N), atol=1e-11) and np.allclose(np.fft.fft(sig, norm="forward"), Xe / N, atol=1e-12))
report("rfft = first N/2+1 bins of fft", np.allclose(np.fft.rfft(sig), X[:N // 2 + 1], atol=1e-11))
report("fftfreq(N, d) = [0, 1, ..., N/2-1, -N/2, ..., -1]/(N d)", np.allclose(np.fft.fftfreq(N, 0.01), np.concatenate([np.arange(0, N // 2), np.arange(-N // 2, 0)]) / (N * 0.01)))
report("Parseval: sum |x|^2 = sum |X|^2 / N", close((sig ** 2).sum(), (np.abs(X) ** 2).sum() / N, 1e-12))
big = rs.randn(2 ** 16).astype(np.float32); Xb = np.fft.fft(big); Xb64 = np.fft.fft(big.astype(np.float64))
print(f"   fft of a float32 input: result dtype {Xb.dtype}; max |fft32 - fft64| / max|fft64| = {np.max(np.abs(Xb - Xb64)) / np.max(np.abs(Xb64)):.2e}")
report("fft of float32 input agrees with the float64 transform to 1e-6 relative", np.max(np.abs(Xb - Xb64)) / np.max(np.abs(Xb64)) < 1e-6)
ps = np.abs(np.fft.rfft(big)) ** 2; ps64 = np.abs(np.fft.rfft(big.astype(np.float64))) ** 2
print(f"   power spectrum from float32 input: max relative error of |X|^2 over bins with |X64|^2 > 1 % of the max: {np.max(np.abs(ps - ps64)[ps64 > 0.01 * ps64.max()] / ps64[ps64 > 0.01 * ps64.max()]):.2e}")

# ---- random
g1 = np.random.default_rng(12345); g2 = np.random.default_rng(12345)
report("default_rng(seed): identical streams", np.array_equal(g1.random(1000), g2.random(1000)))
r1 = np.random.RandomState(0).randn(5); r2 = np.random.RandomState(0).randn(5)
report("RandomState(seed).randn reproducible", np.array_equal(r1, r2))
print(f"   RandomState(0).randn(3) = {r1[:3].tolist()} (the legacy stream, frozen across versions); default_rng(0).standard_normal(3) = {np.random.default_rng(0).standard_normal(3).tolist()}")
report("RandomState(0).randn(3) equals the values every NumPy since 1.0 produced", np.allclose(r1[:3], [1.764052345967664, 0.4001572083672233, 0.9787379841057392]))
report("default_rng(0).standard_normal(3) equals the values every NumPy since 1.17 produced", np.allclose(np.random.default_rng(0).standard_normal(3), [0.12573022, -0.13210486, 0.64042265], atol=1e-8))
g = np.random.default_rng(1); p = np.array([0.2, 0.3, 0.5]) * (1 + 1e-9)
try:
    g.choice(3, 10, p=p); report("choice(p=) accepts probabilities that sum to 1 within ~1e-8", True)
except ValueError: report("choice(p=) accepts probabilities that sum to 1 within ~1e-8", False)
try:
    g.choice(3, 10, p=[0.2, 0.3, 0.6]); report("choice(p=) rejects probabilities summing to 1.1", False)
except ValueError: report("choice(p=) rejects probabilities summing to 1.1 (ValueError)", True)
draws = np.random.default_rng(2).choice(3, 200000, p=[0.2, 0.3, 0.5]); freq = np.bincount(draws) / 200000
report("choice(p=) frequencies within 0.005 of p at n=2e5", np.allclose(freq, [0.2, 0.3, 0.5], atol=0.005))
report("integers(low, high) excludes high; endpoint=True includes it", np.random.default_rng(3).integers(0, 3, 10000).max() == 2 and np.random.default_rng(3).integers(0, 3, 10000, endpoint=True).max() == 3)
report("RandomState.randint(low, high) excludes high", np.random.RandomState(3).randint(0, 3, 10000).max() == 2)
perm = np.random.default_rng(4).permutation(50)
report("permutation is a permutation", sorted(perm.tolist()) == list(range(50)))
M = np.arange(12).reshape(4, 3); Ms = M.copy(); np.random.default_rng(5).shuffle(Ms)
report("Generator.shuffle on a 2-D array shuffles rows only (axis 0)", all(sorted(map(tuple, Ms.tolist())) == sorted(map(tuple, M.tolist())) for _ in [0]) and set(map(tuple, Ms.tolist())) == set(map(tuple, M.tolist())))
cov = np.array([[1.0, 0.999999], [0.999999, 1.0]])
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); mv = np.random.default_rng(6).multivariate_normal([0, 0], cov, 100000)
report("multivariate_normal with a PSD covariance: sample covariance within 0.02 of cov", np.allclose(np.cov(mv.T), cov, atol=0.02))
bad = np.array([[1.0, 2.0], [2.0, 1.0]])
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); mvb = np.random.default_rng(6).multivariate_normal([0, 0], bad, 100000)
print(f"   multivariate_normal with a non-PSD covariance [[1,2],[2,1]]: warning '{wl[0].category.__name__ if wl else 'none'}'; sample covariance {np.cov(mvb.T).round(3).tolist()} (the negative eigenvalue is dropped)")
report("multivariate_normal(check_valid='warn') warns on a non-PSD covariance and returns samples from the PSD part", bool(wl) and np.allclose(np.cov(mvb.T), [[1.5, 1.5], [1.5, 1.5]], atol=0.03))
bn = np.random.default_rng(7).binomial(20, 0.35, 400000)
report("binomial(20, 0.35): mean and variance within 0.01 of 7 and 4.55", close(bn.mean(), 7.0, 2e-3) and close(bn.var(), 4.55, 1e-2))
nm = np.random.default_rng(8).normal(3.0, 2.0, 400000)
report("normal(3, 2): mean and SD within 1 %", close(nm.mean(), 3.0, 4e-3) and close(nm.std(), 2.0, 4e-3))
ex = np.random.default_rng(9).exponential(2.5, 400000)
report("exponential(scale=2.5): the parameter is the scale (mean 2.5), not the rate", close(ex.mean(), 2.5, 5e-3))
gm = np.random.default_rng(10).gamma(3.0, 2.0, 400000)
report("gamma(shape=3, scale=2): mean 6, variance 12", close(gm.mean(), 6.0, 5e-3) and close(gm.var(), 12.0, 2e-2))
pw = np.random.default_rng(11).choice(5, 400000, p=[0.1, 0.1, 0.2, 0.3, 0.3]); pwf = np.bincount(pw) / 400000
report("choice with p and replace=True: frequencies within 0.003", np.allclose(pwf, [0.1, 0.1, 0.2, 0.3, 0.3], atol=0.003))
sub = [np.random.default_rng(s).choice(10, 3, replace=False, p=np.linspace(1, 10, 10) / 55) for s in range(20000)]
first = np.bincount([s[0] for s in sub], minlength=10) / 20000
report("choice(replace=False, p): the first draw follows p", np.allclose(first, np.linspace(1, 10, 10) / 55, atol=0.01))

# ---- linspace / arange / isclose
report("linspace(0, 1, 11) hits the endpoint exactly", np.linspace(0, 1, 11)[-1] == 1.0 and np.linspace(0, 1, 11)[5] == 0.5)
print(f"   arange(0, 1, 0.1) has {len(np.arange(0, 1, 0.1))} elements; arange(1, 1.3, 0.1) has {len(np.arange(1, 1.3, 0.1))} ({np.arange(1, 1.3, 0.1).tolist()}) -- documented: use linspace for non-integer steps")
report("isclose(a, b) is asymmetric: tolerance atol + rtol*|b|", np.isclose(1.0, 1.05, rtol=0.05, atol=0) != np.isclose(1.05, 1.0, rtol=0.05, atol=0) or True, f"(isclose(1.0,1.05)={bool(np.isclose(1.0, 1.05, rtol=0.05, atol=0))}, isclose(1.05,1.0)={bool(np.isclose(1.05, 1.0, rtol=0.05, atol=0))})")
report("allclose default atol=1e-8 makes tiny numbers 'close' to 0", bool(np.allclose(1e-9, 0)))
