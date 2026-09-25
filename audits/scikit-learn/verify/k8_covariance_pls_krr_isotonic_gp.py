#!/usr/bin/env python
"""sklearn.covariance (EmpiricalCovariance, ShrunkCovariance, LedoitWolf, OAS,
MinCovDet, EllipticEnvelope, GraphicalLasso / GraphicalLassoCV, the module
functions), sklearn.cross_decomposition (PLSRegression, PLSCanonical, CCA,
PLSSVD), kernel_ridge.KernelRidge, sklearn.isotonic and sklearn.gaussian_process
(GaussianProcessRegressor, GaussianProcessClassifier, every kernel) against
independent truths: exact rational arithmetic (fractions.Fraction) for the
covariance / shrinkage / kernel-ridge / PAVA closed forms, mpmath for chi-square
quantiles and Gaussian integrals, a plain-numpy NIPALS / SVD / CCA reference, an
ADMM graphical-lasso solver plus the KKT conditions, the closed-form GP
posterior, log-marginal likelihood and its finite-difference gradient, and a
plain-numpy Laplace approximation for the classifier."""
import sys, math, warnings, itertools
sys.path.insert(0, ".")
from _synth import *
import mpmath as mp
from fractions import Fraction as F
banner(); warnings.filterwarnings("ignore"); rs = np.random.RandomState(8)
VER = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
mp.mp.dps = 30

# ---------------------------------------------------------------- helpers (exact rational linear algebra, chi2 via mpmath)
def fmat(A): return [[F(int(v)) if float(v).is_integer() else F(v) for v in row] for row in np.asarray(A).tolist()]
def fmul(A, B): return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
def ftr(A): return [list(r) for r in zip(*A)]
def finv(A):
    n = len(A); M = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0); M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]; M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]
def fdet(A):
    n = len(A); M = [row[:] for row in A]; d = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None: return F(0)
        if piv != c: M[c], M[piv] = M[piv], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]; M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return d
def tofl(A): return np.array([[float(v) for v in row] for row in A]) if isinstance(A[0], list) else np.array([float(v) for v in A])
def dev(a, b):
    """max |a-b| relative to the largest magnitude of b (or 1 if b is tiny)."""
    a = np.asarray(a, float); b = np.asarray(b, float); return float(np.max(np.abs(a - b)) / max(1e-300, np.max(np.abs(b)), 1e-12 if np.max(np.abs(b)) < 1e-12 else 0))
def chi2_cdf(x, k): return float(mp.gammainc(mp.mpf(k) / 2, 0, mp.mpf(x) / 2, regularized=True))
def chi2_ppf(p, k):
    lo, hi = mp.mpf(0), mp.mpf(1000)
    for _ in range(200):
        mid = (lo + hi) / 2
        if mp.gammainc(mp.mpf(k) / 2, 0, mid / 2, regularized=True) < p: lo = mid
        else: hi = mid
    return float((lo + hi) / 2)
def empcov_np(X): X = np.asarray(X, float); Xc = X - X.mean(0); return Xc.T @ Xc / len(X)

# =============================================================================================== covariance
print("== sklearn.covariance")
from sklearn.covariance import (EmpiricalCovariance, empirical_covariance, log_likelihood, ShrunkCovariance, shrunk_covariance,
                                LedoitWolf, ledoit_wolf, ledoit_wolf_shrinkage, OAS, oas, MinCovDet, EllipticEnvelope, GraphicalLasso, GraphicalLassoCV, graphical_lasso)
Xi = rs.randint(-6, 7, (12, 3)); n, p = Xi.shape; X = Xi.astype(float)
Xf = fmat(Xi); mean = [sum(col) / n for col in zip(*Xf)]
C = [[sum((Xf[k][i] - mean[i]) * (Xf[k][j] - mean[j]) for k in range(n)) / n for j in range(p)] for i in range(p)]
Cu = [[sum(Xf[k][i] * Xf[k][j] for k in range(n)) / n for j in range(p)] for i in range(p)]
Cinv = finv(C); Cdet = fdet(C)
ec = empirical_covariance(X)
print(f"   empirical_covariance on 12x3 integers: max dev from exact rational (divisor n) {dev(ec, tofl(C)):.1e}; dtype {ec.dtype}")
report("empirical_covariance = (1/n) sum (x-mean)(x-mean)^T exactly (MLE, divisor n_samples, not n-1)", dev(ec, tofl(C)) < 1e-14)
report("empirical_covariance(assume_centered=True) = X^T X / n exactly ('data will not be centered')", dev(empirical_covariance(X, assume_centered=True), tofl(Cu)) < 1e-14)
report("empirical_covariance docstring example [[1,1,1]x3,[0,0,0]x3] -> 0.25 everywhere", np.allclose(empirical_covariance([[1, 1, 1]] * 3 + [[0, 0, 0]] * 3), 0.25))
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); one = empirical_covariance(np.array([1.0, 2.0, 3.0]))
print(f"   empirical_covariance(1-D vector of length 3): shape {one.shape}, values {one.ravel().tolist()}, warning: {[str(w.message)[:60] for w in wl]}")
report("empirical_covariance(1-D input) treats it as ONE sample of 3 features (zeros + 'Only one sample' warning)", one.shape == (3, 3) and np.all(one == 0) and len(wl) == 1)
E = EmpiricalCovariance().fit(X)
report("EmpiricalCovariance.location_ = column means exactly", dev(E.location_, tofl(mean)) < 1e-15)
report("EmpiricalCovariance.covariance_ = exact MLE covariance", dev(E.covariance_, tofl(C)) < 1e-14)
report("EmpiricalCovariance.precision_ = exact inverse of covariance_ (within 1e-10 rel)", dev(E.precision_, tofl(Cinv)) < 1e-10, f"(max rel dev {dev(E.precision_, tofl(Cinv)):.1e})")
report("EmpiricalCovariance(store_precision=False).precision_ is None and get_precision() still returns the inverse", EmpiricalCovariance(store_precision=False).fit(X).precision_ is None and dev(EmpiricalCovariance(store_precision=False).fit(X).get_precision(), tofl(Cinv)) < 1e-10)
Ec = EmpiricalCovariance(assume_centered=True).fit(X)
report("EmpiricalCovariance(assume_centered=True): location_ = 0 and covariance_ = X^T X / n", np.all(Ec.location_ == 0) and dev(Ec.covariance_, tofl(Cu)) < 1e-14)
Xt = rs.randint(-6, 7, (7, 3)); Xtf = fmat(Xt)
dexact = [fmul(fmul([[x - m for x, m in zip(row, mean)]], Cinv), ftr([[x - m for x, m in zip(row, mean)]]))[0][0] for row in Xtf]
print(f"   mahalanobis exact (squared) {tofl(dexact)[:3].round(6).tolist()} vs library {E.mahalanobis(Xt.astype(float))[:3].round(6).tolist()}")
report("EmpiricalCovariance.mahalanobis = SQUARED Mahalanobis distance (x-mu)^T P (x-mu) (docstring: 'Squared Mahalanobis distances')", dev(E.mahalanobis(Xt.astype(float)), tofl(dexact)) < 1e-10)
ll_exact = sum(mp.mpf(-1) / 2 * (mp.mpf(d.numerator) / d.denominator + mp.log(mp.mpf(Cdet.numerator) / Cdet.denominator) + p * mp.log(2 * mp.pi)) for d in dexact) / len(dexact)
print(f"   score(X_test) = {E.score(Xt.astype(float))!r} vs mean of log N(x | location_, covariance_) = {float(ll_exact)!r}")
report("EmpiricalCovariance.score(X_test) = sample mean of the Gaussian log-density log N(x | location_, covariance_)", close(E.score(Xt.astype(float)), float(ll_exact), 1e-12))
ll_fun = log_likelihood(tofl(C), tofl(Cinv)); ll_fun_exact = float(-(p - mp.log(1 / (mp.mpf(Cdet.numerator) / Cdet.denominator)) + p * mp.log(2 * mp.pi)) / 2)
report("log_likelihood(emp_cov, precision) = -(tr(S P) - log det P + p log 2pi)/2 ('accounts for normalization terms')", close(ll_fun, ll_fun_exact, 1e-12), f"({ll_fun!r} vs {ll_fun_exact!r})")
comp = tofl(C) + np.array([[0.5, 0.1, 0.0], [0.1, -0.2, 0.3], [0.0, 0.3, 0.1]]); err = comp - E.covariance_
report("error_norm(frobenius, scaling, squared) = sum(err^2)/n_features", close(E.error_norm(comp), (err ** 2).sum() / p, 1e-12))
report("error_norm(spectral, squared=False) = sqrt(max singular value(err^T err)/n_features)", close(E.error_norm(comp, norm="spectral", squared=False), math.sqrt(np.linalg.svd(err.T @ err, compute_uv=False).max() / p), 1e-12))
report("error_norm(frobenius, scaling=False, squared=False) = Frobenius norm of the error", close(E.error_norm(comp, scaling=False, squared=False), math.sqrt((err ** 2).sum()), 1e-12))
X32 = (X + 0.5).astype(np.float32); E32 = EmpiricalCovariance().fit(X32)
print(f"   float32 input: covariance_ dtype {E32.covariance_.dtype}, location_ dtype {E32.location_.dtype}, max dev from float64 fit {dev(E32.covariance_, EmpiricalCovariance().fit(X32.astype(float)).covariance_):.1e}")
report("EmpiricalCovariance float32 input: covariance_ within 1e-5 of the float64 result", dev(E32.covariance_, EmpiricalCovariance().fit(X32.astype(float)).covariance_) < 1e-5)
Xoff = X + 1e6
report("EmpiricalCovariance with 1e6 offset: covariance_ within 1e-9 relative of the offset-free exact covariance", dev(EmpiricalCovariance().fit(Xoff).covariance_, tofl(C)) < 1e-9, f"(dev {dev(EmpiricalCovariance().fit(Xoff).covariance_, tofl(C)):.1e})")

# ---- shrinkage
sh = F(3, 10); mu = sum(C[i][i] for i in range(p)) / p
Sh = [[(1 - sh) * C[i][j] + (sh * mu if i == j else 0) for j in range(p)] for i in range(p)]
report("shrunk_covariance(cov, 0.3) = (1 - shrinkage) * cov + shrinkage * mu * I, mu = trace(cov)/n_features (exact)", dev(shrunk_covariance(tofl(C), 0.3), tofl(Sh)) < 1e-14)
report("ShrunkCovariance(shrinkage=0.3).fit(X).covariance_ = shrunk exact MLE covariance", dev(ShrunkCovariance(shrinkage=0.3).fit(X).covariance_, tofl(Sh)) < 1e-14)
report("ShrunkCovariance(shrinkage=0) = EmpiricalCovariance; shrinkage=1 = mu * I", dev(ShrunkCovariance(shrinkage=0.0).fit(X).covariance_, tofl(C)) < 1e-14 and dev(ShrunkCovariance(shrinkage=1.0).fit(X).covariance_, float(mu) * np.eye(p)) < 1e-14)
if VER >= (1, 5): report("shrunk_covariance on a stack of matrices (..., p, p) shrinks each matrix (1.5+)", dev(shrunk_covariance(np.stack([tofl(C), tofl(Cu)]), 0.3)[0], tofl(Sh)) < 1e-14)

# ---- Ledoit-Wolf 2004 closed form, exact rational arithmetic
def lw_exact(Xf, centered):
    n = len(Xf); p = len(Xf[0])
    if centered: mean = [F(0)] * p
    else: mean = [sum(col) / n for col in zip(*Xf)]
    Xc = [[x - m for x, m in zip(row, mean)] for row in Xf]
    S = [[sum(Xc[k][i] * Xc[k][j] for k in range(n)) / n for j in range(p)] for i in range(p)]
    m = sum(S[i][i] for i in range(p)) / p
    d2 = sum((S[i][j] - (m if i == j else 0)) ** 2 for i in range(p) for j in range(p)) / p
    bbar2 = sum(sum((Xc[k][i] * Xc[k][j] - S[i][j]) ** 2 for i in range(p) for j in range(p)) for k in range(n)) / (n * n * p)
    b2 = min(bbar2, d2); shrink = b2 / d2 if d2 else F(0)
    cov = [[(1 - shrink) * S[i][j] + (shrink * m if i == j else 0) for j in range(p)] for i in range(p)]
    return shrink, cov, S, m, d2, bbar2
_b = rs.randint(-4, 5, (20, 2)); Xl = np.column_stack([_b[:, 0], _b[:, 0] + rs.randint(-1, 2, 20), _b[:, 1], _b[:, 1] - _b[:, 0] + rs.randint(-1, 2, 20)]).astype(float); Xlf = fmat(Xl)  # correlated integer columns -> shrinkage strictly inside (0, 1)
shr, lwcov, S_, m_, d2_, bb2_ = lw_exact(Xlf, False)
print(f"   Ledoit-Wolf exact: m={float(m_):.6f} d^2={float(d2_):.6f} bbar^2={float(bb2_):.6f} shrinkage=b^2/d^2={float(shr):.10f}; library ledoit_wolf_shrinkage={ledoit_wolf_shrinkage(Xl)!r}")
report("ledoit_wolf_shrinkage = min(bbar^2, d^2)/d^2 of Ledoit & Wolf (2004) exactly (data centered first)", close(ledoit_wolf_shrinkage(Xl), float(shr), 1e-12))
LW = LedoitWolf().fit(Xl)
report("LedoitWolf.shrinkage_ and covariance_ = (1-s) S + s m I with the 2004 closed form", close(LW.shrinkage_, float(shr), 1e-12) and dev(LW.covariance_, tofl(lwcov)) < 1e-12)
cv_f, sh_f = ledoit_wolf(Xl)
report("ledoit_wolf(X) function returns the same (covariance, shrinkage)", dev(cv_f, tofl(lwcov)) < 1e-12 and close(sh_f, float(shr), 1e-12))
bs = [ledoit_wolf_shrinkage(Xl, block_size=b) for b in (1, 2, 3, 1000)]
report("block_size in (1,2,3,1000) 'is purely a memory optimization and does not affect results' (within 1e-13)", max(abs(b - bs[-1]) for b in bs) < 1e-13, f"(spread {max(abs(b - bs[-1]) for b in bs):.1e})")
Xl_off = Xl + 3.0; shr_c, lwcov_c, *_ = lw_exact(fmat(Xl_off), True)
report("LedoitWolf(assume_centered=True) on uncentered data uses S = X^T X/n and raw x_k in the formula", close(LedoitWolf(assume_centered=True).fit(Xl_off).shrinkage_, float(shr_c), 1e-12) and dev(LedoitWolf(assume_centered=True).fit(Xl_off).covariance_, tofl(lwcov_c)) < 1e-12)
report("LedoitWolf with 1e6 offset: shrinkage_ within 1e-8 of the offset-free value", close(LedoitWolf().fit(Xl + 1e6).shrinkage_, float(shr), 1e-8), f"(dev {abs(LedoitWolf().fit(Xl + 1e6).shrinkage_ - float(shr)):.1e})")
one_f = LedoitWolf().fit(Xl[:, :1])
report("LedoitWolf on a single feature: shrinkage_ = 0 and covariance_ = variance ('the result is the same whatever the shrinkage')", one_f.shrinkage_ == 0 and close(one_f.covariance_[0, 0], Xl[:, 0].var(), 1e-14))
Xbig = rs.randn(20000, 5); s_big = LedoitWolf().fit(Xbig).shrinkage_
print(f"   LedoitWolf on 20000 x 5 iid N(0, I): shrinkage_ = {s_big:.4f} (user guide: 'approaches 1 as the number of samples increases' when the population covariance is a multiple of the identity)")
report("LedoitWolf on iid N(0,I) with n=20000: shrinkage_ > 0.8 (user guide caveat)", s_big > 0.8)
LW32 = LedoitWolf().fit(Xl.astype(np.float32))
print(f"   LedoitWolf float32 input: covariance_ dtype {LW32.covariance_.dtype}, shrinkage_ dev {abs(LW32.shrinkage_ - float(shr)):.1e}")
report("LedoitWolf float32 input: shrinkage_ within 1e-5 of exact", abs(LW32.shrinkage_ - float(shr)) < 1e-5)

# ---- OAS (Chen et al. 2010) closed form as documented (2/p terms omitted), exact rational
def oas_exact(Xf, centered):
    n = len(Xf); p = len(Xf[0]); mean = [F(0)] * p if centered else [sum(col) / n for col in zip(*Xf)]
    Xc = [[x - m for x, m in zip(row, mean)] for row in Xf]
    S = [[sum(Xc[k][i] * Xc[k][j] for k in range(n)) / n for j in range(p)] for i in range(p)]
    trS = sum(S[i][i] for i in range(p)); trS2 = sum(S[i][j] ** 2 for i in range(p) for j in range(p))
    num = trS2 + trS ** 2; den = (n + 1) * (trS2 - trS ** 2 / p)
    rho = F(1) if den == 0 else min(num / den, F(1))
    num23 = (1 - F(2, p)) * trS2 + trS ** 2; den23 = (n + 1 - F(2, p)) * (trS2 - trS ** 2 / p)
    rho23 = F(1) if den23 == 0 else min(num23 / den23, F(1))
    m = trS / p; cov = [[(1 - rho) * S[i][j] + (rho * m if i == j else 0) for j in range(p)] for i in range(p)]
    return rho, cov, rho23
rho_, oascov, rho23_ = oas_exact(Xlf, False); O = OAS().fit(Xl)
print(f"   OAS exact (sklearn's documented variant without the 2/p terms) = {float(rho_):.10f}; paper Eq. 23 with 2/p = {float(rho23_):.10f}; library shrinkage_ = {O.shrinkage_!r}")
report("OAS.shrinkage_ = (tr(S^2)+tr(S)^2)/((n+1)(tr(S^2)-tr(S)^2/p)) capped at 1 (docstring: Eq. 23 of Chen 2010 with the 2/p factors omitted)", close(O.shrinkage_, float(rho_), 1e-12))
report("OAS.covariance_ = (1-rho) S + rho mu I with that rho", dev(O.covariance_, tofl(oascov)) < 1e-12)
report("oas(X) function returns the same (covariance, shrinkage)", dev(oas(Xl)[0], tofl(oascov)) < 1e-12 and close(oas(Xl)[1], float(rho_), 1e-12))
report("OAS: omitting the 2/p terms of Chen et al. Eq. 23 'doesn't affect the value of the estimator' (docstring) -- |shrinkage difference| < 1e-2 on 20x4 data", abs(float(rho_) - float(rho23_)) < 1e-2, f"(|diff| {abs(float(rho_) - float(rho23_)):.2e}, relative {abs(float(rho_) - float(rho23_)) / float(rho23_):.1%})")
for pp in (4, 10, 50, 200):
    Xw = rs.randn(60, pp) @ (np.eye(pp) + 0.3 * rs.randn(pp, pp) / math.sqrt(pp)); Sw = empcov_np(Xw); trS, trS2 = np.trace(Sw), (Sw ** 2).sum()
    r_sk = min((trS2 + trS ** 2) / (61 * (trS2 - trS ** 2 / pp)), 1); r_23 = min(((1 - 2 / pp) * trS2 + trS ** 2) / ((61 - 2 / pp) * (trS2 - trS ** 2 / pp)), 1)
    print(f"   OAS with n=60, p={pp}: sklearn variant {r_sk:.5f} vs Eq. 23 {r_23:.5f} (relative difference {abs(r_sk - r_23) / r_23:.1%}); library {OAS().fit(Xw).shrinkage_:.5f}")
Xid = np.array([[1.0, 0], [-1, 0], [0, 1], [0, -1]]); Oid = OAS().fit(Xid)
report("OAS when S is a multiple of the identity (denominator 0): shrinkage_ = 1 and covariance_ = S", Oid.shrinkage_ == 1.0 and dev(Oid.covariance_, 0.5 * np.eye(2)) < 1e-15)
report("OAS single feature: shrinkage_ = 0", OAS().fit(Xl[:, :1]).shrinkage_ == 0)
rho_c, oascov_c, _ = oas_exact(fmat(Xl_off), True)
report("OAS(assume_centered=True) on uncentered data uses S = X^T X / n", close(OAS(assume_centered=True).fit(Xl_off).shrinkage_, float(rho_c), 1e-12) and dev(OAS(assume_centered=True).fit(Xl_off).covariance_, tofl(oascov_c)) < 1e-12)

# ---- MinCovDet
def mcd_reference(X, mcd):
    """Recompute correction + reweighting from the raw estimates, following the documented pipeline of the installed version."""
    n, p = X.shape; raw_loc, raw_cov, raw_sup = mcd.raw_location_, mcd.raw_covariance_, mcd.raw_support_
    h = int(raw_sup.sum()); P = np.linalg.inv(raw_cov); Xc = X - raw_loc; d = np.einsum("ij,jk,ik->i", Xc, P, Xc)
    if VER >= (1, 8):
        a = h / n; c = a / chi2_cdf(chi2_ppf(a, p), p + 2)
    else:
        c = np.median(d) / chi2_ppf(0.5, p)
    d_corr = d / c; mask = d_corr < chi2_ppf(0.975, p)
    loc = X[mask].mean(0); cov = empcov_np(X[mask])
    if VER >= (1, 8): cov = cov * (0.975 / chi2_cdf(chi2_ppf(0.975, p), p + 2))
    Xc2 = X - loc; d2 = np.einsum("ij,jk,ik->i", Xc2, np.linalg.inv(cov), Xc2)
    return dict(c=c, corrected=raw_cov * c, mask=mask, loc=loc, cov=cov, dist=d2)
# 1-D: shortest-half / brute force minimum variance subset
x1 = np.concatenate([rs.randn(30), [8.0, 9.5, -7.0]]); n1 = len(x1); h1 = min(int(math.ceil(0.5 * (n1 + 2))), n1)
m1 = MinCovDet(random_state=0).fit(x1[:, None]); xs1 = np.sort(x1)
best_var = min(np.var(xs1[i:i + h1]) for i in range(n1 - h1 + 1))
print(f"   MinCovDet 1-D (n={n1}, h={h1}): raw_covariance_ {m1.raw_covariance_[0, 0]:.6f}, min variance over all h-windows of sorted x {best_var:.6f}; raw_location_ {m1.raw_location_[0]:.6f} vs mean of raw support {x1[m1.raw_support_].mean():.6f}")
report(f"MinCovDet 1-D: raw_support_ has h = ceil((n+p+1)/2) = {h1} points", m1.raw_support_.sum() == h1)
report("MinCovDet 1-D: raw_covariance_ = variance (ddof=0) of the raw support", close(m1.raw_covariance_[0, 0], np.var(x1[m1.raw_support_]), 1e-12))
report("MinCovDet 1-D: raw_covariance_ is the minimum variance over all h-subsets (the MCD subset) within 1e-9", m1.raw_covariance_[0, 0] <= best_var * (1 + 1e-9))
report("MinCovDet 1-D: raw_location_ = mean of raw support ('raw robust estimated location')", close(m1.raw_location_[0], x1[m1.raw_support_].mean(), 1e-12), f"(location {m1.raw_location_[0]:.6f}, support mean {x1[m1.raw_support_].mean():.6f})")
# p = 2, tiny n: brute force over every h-subset
X2 = np.vstack([rs.randn(11, 2), [[6, 6], [7, -5], [-6, 5]]]); n2, p2 = X2.shape; h2 = int(math.ceil(0.5 * (n2 + p2 + 1)))
dets = {S: np.linalg.det(empcov_np(X2[list(S)])) for S in itertools.combinations(range(n2), h2)}; best = min(dets, key=dets.get)
m2 = MinCovDet(random_state=0).fit(X2)
print(f"   MinCovDet p=2 n={n2} h={h2}: brute force over {len(dets)} subsets min det {dets[best]:.6e}; library det(raw_covariance_) {np.linalg.det(m2.raw_covariance_):.6e}; support match {set(np.flatnonzero(m2.raw_support_)) == set(best)}")
report(f"MinCovDet p=2: raw_support_ has h = ceil((n+p+1)/2) = {h2} points", m2.raw_support_.sum() == h2)
report("MinCovDet p=2: raw_covariance_ = MLE covariance of X[raw_support_] and raw_location_ = its mean", dev(m2.raw_covariance_, empcov_np(X2[m2.raw_support_])) < 1e-12 and dev(m2.raw_location_, X2[m2.raw_support_].mean(0)) < 1e-12)
report(f"MinCovDet p=2: FastMCD finds the global minimum-determinant h-subset (brute force over {len(dets)} subsets)", np.linalg.det(m2.raw_covariance_) <= dets[best] * (1 + 1e-9))
# full pipeline on n = 100 with outliers
X3 = np.vstack([rs.multivariate_normal([1, -2], [[2, 0.6], [0.6, 1]], 90), rs.uniform(-8, 8, (10, 2))]); n3, p3 = X3.shape
for sf in (None, 0.75):
    m3 = MinCovDet(random_state=1, support_fraction=sf).fit(X3); ref = mcd_reference(X3, m3)
    hexp = int(math.ceil(0.5 * (n3 + p3 + 1))) if sf is None else int(sf * n3)
    tag = f"support_fraction={sf}"
    print(f"   MinCovDet {tag}: h={m3.raw_support_.sum()} (expected {hexp}); consistency factor {ref['c']:.6f}; reweighted support {m3.support_.sum()} (ref {ref['mask'].sum()}); cov dev {dev(m3.covariance_, ref['cov']):.1e}; dist_ dev {dev(m3.dist_, ref['dist']):.1e}")
    report(f"MinCovDet {tag}: raw support size = {'ceil((n+p+1)/2)' if sf is None else 'int(support_fraction*n)'}", m3.raw_support_.sum() == hexp)
    report(f"MinCovDet {tag}: covariance_ = consistency-corrected + reweighted covariance ({'Croux/Pison factors, >=1.8' if VER >= (1, 8) else 'median/chi2 correction, <1.8'}) recomputed from raw estimates with mpmath chi2", dev(m3.covariance_, ref["cov"]) < 1e-8)
    report(f"MinCovDet {tag}: support_ = mask of raw-corrected squared distances below chi2(p).isf(0.025) ('reweighting step')", np.array_equal(m3.support_, ref["mask"]))
    report(f"MinCovDet {tag}: location_ = mean of reweighted support", dev(m3.location_, ref["loc"]) < 1e-10)
    report(f"MinCovDet {tag}: dist_ = squared Mahalanobis distances of training data under the final (location_, covariance_)", dev(m3.dist_, ref["dist"]) < 1e-8)
    report(f"MinCovDet {tag}: mahalanobis(X_train) == dist_", dev(m3.mahalanobis(X3), m3.dist_) < 1e-10)
    d_before = m3.dist_.copy(); cc = m3.correct_covariance(X3)
    if VER >= (1, 8): a_cur = m3.support_.sum() / n3; fac_cur = a_cur / chi2_cdf(chi2_ppf(a_cur, p3), p3 + 2)
    else: fac_cur = np.median(d_before) / chi2_ppf(0.5, p3)
    report(f"MinCovDet {tag}: correct_covariance(X) called after fit returns raw_covariance_ * consistency factor of the CURRENT (reweighted) support_/dist_", dev(cc, m3.raw_covariance_ * fac_cur) < 1e-8)
    report(f"MinCovDet {tag}: correct_covariance(X) called after fit leaves dist_ unchanged (docstring documents only the returned matrix)", dev(m3.dist_, d_before) < 1e-12, f"(dist_ was divided by {fac_cur:.4f} in place)")
m3c = MinCovDet(random_state=1, assume_centered=True).fit(X3)
report("MinCovDet(assume_centered=True): raw_location_ = 0 and raw_covariance_ = X[support]^T X[support] / h", np.all(m3c.raw_location_ == 0) and dev(m3c.raw_covariance_, X3[m3c.raw_support_].T @ X3[m3c.raw_support_] / m3c.raw_support_.sum()) < 1e-12)
m3o = MinCovDet(random_state=1).fit(X3 + 1e6); m3r = MinCovDet(random_state=1).fit(X3)
report("MinCovDet with 1e6 offset: covariance_ within 1e-6 relative of the offset-free fit", dev(m3o.covariance_, m3r.covariance_) < 1e-6, f"(dev {dev(m3o.covariance_, m3r.covariance_):.1e})")
try:
    m_sc = MinCovDet(random_state=1).fit(X3.astype(np.float32)); print(f"   MinCovDet float32: covariance_ dtype {m_sc.covariance_.dtype}, dev from float64 {dev(m_sc.covariance_, m3r.covariance_):.1e}")
    report("MinCovDet float32 input: covariance_ within 1e-4 of the float64 fit", dev(m_sc.covariance_, m3r.covariance_) < 1e-4)
except Exception as e: report("MinCovDet float32 input fits", False, f"{type(e).__name__}: {e}")

# ---- EllipticEnvelope
for cont in (0.1, 0.25):
    ee = EllipticEnvelope(contamination=cont, random_state=1).fit(X3); mref = MinCovDet(random_state=1).fit(X3)
    d = ee.decision_function(X3); n_out = int((ee.predict(X3) == -1).sum())
    print(f"   EllipticEnvelope(contamination={cont}): offset_ {ee.offset_:.6f}, training outliers {n_out} of {n3}, decision<0 count {(d < 0).sum()}")
    report(f"EllipticEnvelope(contamination={cont}): covariance_/location_ equal MinCovDet with the same random_state (documented inheritance)", dev(ee.covariance_, mref.covariance_) < 1e-12 and dev(ee.location_, mref.location_) < 1e-12)
    report(f"EllipticEnvelope(contamination={cont}): score_samples = -mahalanobis and decision_function = score_samples - offset_", dev(ee.score_samples(X3), -ee.mahalanobis(X3)) < 1e-12 and dev(d, ee.score_samples(X3) - ee.offset_) < 1e-12)
    report(f"EllipticEnvelope(contamination={cont}): offset_ = percentile(-dist_, 100*contamination) so that round(contamination*n) training samples are outliers", close(ee.offset_, np.percentile(-ee.dist_, 100 * cont), 1e-12) and n_out == round(cont * n3))
    report(f"EllipticEnvelope(contamination={cont}): predict is -1 iff decision_function < 0 and +1 otherwise", np.array_equal(ee.predict(X3), np.where(d >= 0, 1, -1)))
    report(f"EllipticEnvelope(contamination={cont}): score(X, y) = accuracy of predict", close(ee.score(X3, np.where(d >= 0, 1, -1)), 1.0))
try:
    EllipticEnvelope(contamination=0.6).fit(X3); report("EllipticEnvelope(contamination=0.6) raises ('Range is (0, 0.5]')", False)
except ValueError: report("EllipticEnvelope(contamination=0.6) raises ('Range is (0, 0.5]')", True)

# ---- GraphicalLasso: ADMM reference + KKT conditions of the documented objective
def glasso_admm(S, alpha, rho=1.0, iters=50000, tol=1e-13):
    p = S.shape[0]; Z = np.eye(p); U = np.zeros((p, p))
    for it in range(iters):
        w, V = np.linalg.eigh(rho * (Z - U) - S); Theta = (V * ((w + np.sqrt(w ** 2 + 4 * rho)) / (2 * rho))) @ V.T
        M = Theta + U; Zn = np.sign(M) * np.maximum(np.abs(M) - alpha / rho, 0); np.fill_diagonal(Zn, np.diag(M))
        U = U + Theta - Zn
        if np.abs(Zn - Z).max() < tol and np.abs(Theta - Zn).max() < tol: Z = Zn; break
        Z = Zn
    return (Z + Z.T) / 2, it + 1
def kkt(S, Theta, alpha):
    W = np.linalg.inv(Theta); R = W - S; off = ~np.eye(len(S), dtype=bool)
    diag_res = np.abs(np.diag(R)).max()
    bound_viol = max(0.0, (np.abs(R[off]) - alpha).max())
    nz = off & (np.abs(Theta) > 1e-8); sign_res = np.abs(R[nz] - alpha * np.sign(Theta[nz])).max() if nz.any() else 0.0
    return diag_res, bound_viol, sign_res, int(nz.sum() // 2)
Lg = np.array([[1, 0, 0, 0, 0], [0.7, 1, 0, 0, 0], [0, 0.6, 1, 0, 0], [0, 0, 0, 1, 0], [0.3, 0, 0, 0.5, 1]])
Xg = rs.randn(120, 5) @ Lg.T; Sg = empcov_np(Xg)
for alpha in (0.05, 0.2):
    for mode in ("cd", "lars"):
        gl = GraphicalLasso(alpha=alpha, mode=mode, tol=1e-10, enet_tol=1e-12, max_iter=2000).fit(Xg)
        Zref, nit = glasso_admm(Sg, alpha); dres, bviol, sres, nedges = kkt(Sg, gl.precision_, alpha)
        print(f"   GraphicalLasso alpha={alpha} mode={mode}: n_iter_={gl.n_iter_}, max |precision_ - ADMM| {np.abs(gl.precision_ - Zref).max():.1e} (ADMM {nit} it), KKT: |W_ii-S_ii| {dres:.1e}, off-diag bound violation {bviol:.1e}, sign residual {sres:.1e}, {nedges} non-zero edges")
        report(f"GraphicalLasso(alpha={alpha}, mode='{mode}') precision_ matches an independent ADMM solution of argmin tr(SK) - log det K + alpha ||K||_offdiag_1 within 1e-5", np.abs(gl.precision_ - Zref).max() < 1e-5)
        report(f"GraphicalLasso(alpha={alpha}, mode='{mode}') KKT: diag(K^-1) = diag(S) (diagonal not penalised), |K^-1 - S|_offdiag <= alpha, and = alpha*sign(K_ij) where K_ij != 0", dres < 1e-6 and bviol < 1e-6 and sres < 1e-6)
        report(f"GraphicalLasso(alpha={alpha}, mode='{mode}') covariance_ = inverse of precision_ (within 1e-6)", dev(gl.covariance_, np.linalg.inv(gl.precision_)) < 1e-6)
        report(f"GraphicalLasso(alpha={alpha}, mode='{mode}') location_ = column means", dev(gl.location_, Xg.mean(0)) < 1e-12)
try:
    gl0 = GraphicalLasso(alpha=0.0).fit(Xg)
    report("GraphicalLasso(alpha=0): precision_ = inverse of the empirical covariance and covariance_ = empirical covariance (accepted although the docstring says 'Range is (0, inf]')", dev(gl0.precision_ @ Sg, np.eye(5)) < 1e-10 and dev(gl0.covariance_, Sg) < 1e-14)
except Exception as e:
    print(f"   GraphicalLasso(alpha=0.0): {type(e).__name__}: {str(e)[:100]}")
    report("GraphicalLasso(alpha=0) is rejected in this version (parameter validation, docstring 'Range is (0, inf]'); 1.3+ accept it with an early return", VER[:2] == (1, 2))
amax = np.abs(Sg - np.diag(np.diag(Sg))).max(); gla = GraphicalLasso(alpha=amax * 1.01, tol=1e-10).fit(Xg)
report("GraphicalLasso(alpha > max |S_ij|, i!=j): precision_ is diagonal with 1/S_ii", np.abs(gla.precision_ - np.diag(1 / np.diag(Sg))).max() < 1e-8)
cov_f, prec_f, costs, n_it = graphical_lasso(Sg, 0.1, tol=1e-8, enet_tol=1e-12, max_iter=2000, return_costs=True, return_n_iter=True)
objs = [c[0] for c in costs]; gaps = [c[1] for c in costs]
my_obj = lambda K: np.trace(Sg @ K) - np.linalg.slogdet(K)[1] + 0.1 * np.abs(K - np.diag(np.diag(K))).sum()
my_gap = np.trace(Sg @ prec_f) - 5 + 0.1 * np.abs(prec_f - np.diag(np.diag(prec_f))).sum()
print(f"   graphical_lasso(S, 0.1, tol=1e-8, enet_tol=1e-12) costs: objective {[float(o) for o in objs[:3]]} ... {objs[-1]:.8f} (documented objective of the result {my_obj(prec_f):.8f}; difference {objs[-1] - my_obj(prec_f):.8f} = 2 p log(2 pi) = {2 * 5 * math.log(2 * math.pi):.8f}); final dual gap {gaps[-1]:.2e} (my recomputation {my_gap:.2e}), n_iter {n_it}")
report("graphical_lasso return_costs: reported 'objective' = tr(SK) - log det K + alpha ||K||_offdiag_1 + 2 p log(2 pi) (constant shift, documented only as 'the objective function')", close(objs[-1] - 2 * 5 * math.log(2 * math.pi), my_obj(prec_f), 1e-9))
report("graphical_lasso (enet_tol=1e-12): objective is non-increasing over iterations and the final dual gap tr(SK) - p + alpha||K||_1 is below tol=1e-8", all(objs[i + 1] <= objs[i] + 1e-12 for i in range(len(objs) - 1)) and abs(my_gap) < 1e-8 and close(gaps[-1], my_gap, 1e-6, 1e-12))
_, _, costs_d, n_it_d = graphical_lasso(Sg, 0.1, return_costs=True, return_n_iter=True); objs_d = [c[0] for c in costs_d]
print(f"   graphical_lasso(S, 0.1) with default tol=1e-4, enet_tol=1e-4: n_iter {n_it_d}, final gap {costs_d[-1][1]:.2e}, objective monotone: {all(objs_d[i + 1] <= objs_d[i] + 1e-12 for i in range(len(objs_d) - 1))} (inner CD solved only to enet_tol)")
report("graphical_lasso with default tolerances converges (dual gap < 1e-4) before max_iter", n_it_d < 100 and abs(costs_d[-1][1]) < 1e-4)
if VER >= (1, 3):
    glp = GraphicalLasso(alpha=0.1, covariance="precomputed", tol=1e-8, enet_tol=1e-12, max_iter=2000).fit(Sg)
    report("GraphicalLasso(covariance='precomputed').fit(S) equals graphical_lasso(S) and location_ = 0", dev(glp.precision_, prec_f) < 1e-10 and np.all(glp.location_ == 0))
gl_off = GraphicalLasso(alpha=0.1, tol=1e-10).fit(Xg + 1e6); gl_ref = GraphicalLasso(alpha=0.1, tol=1e-10).fit(Xg)
report("GraphicalLasso with 1e6 offset: precision_ within 1e-6 of the offset-free fit", dev(gl_off.precision_, gl_ref.precision_) < 1e-6, f"(dev {dev(gl_off.precision_, gl_ref.precision_):.1e})")
# GraphicalLassoCV
from sklearn.model_selection import KFold
cvo = KFold(3, shuffle=False); gcv = GraphicalLassoCV(alphas=4, n_refinements=1, cv=cvo).fit(Xg)
a1 = amax; a0 = 0.01 * a1; grid = np.logspace(np.log10(a0), np.log10(a1), 4)[::-1]
res = gcv.cv_results_; alphas_cv = np.asarray(res["alphas"]); mts = np.asarray(res["mean_test_score"])
print(f"   GraphicalLassoCV(alphas=4, n_refinements=1): cv_results_ alphas {alphas_cv.round(5).tolist()}; expected grid logspace(0.01*alpha_max, alpha_max, 4) desc + [0] = {np.append(grid, 0).round(5).tolist()}; mean_test_score {mts.round(4).tolist()}; alpha_ {gcv.alpha_:.5f}")
report("GraphicalLassoCV(alphas=int): first grid = logspace(log10(0.01*alpha_max), log10(alpha_max), n_alphas) descending, then alpha=0 appended", len(alphas_cv) == 5 and np.allclose(alphas_cv[:4], grid, rtol=1e-12) and alphas_cv[-1] == 0)
best = max(range(4), key=lambda i: (mts[i], i))
report("GraphicalLassoCV.alpha_ = grid alpha with the highest mean_test_score (ties -> smallest alpha), alpha=0 row excluded", close(gcv.alpha_, alphas_cv[best], 1e-12))
scores0 = []
for tr, te in cvo.split(Xg):
    loc = Xg[tr].mean(0); Ptr = np.linalg.inv(empcov_np(Xg[tr])); Ste = (Xg[te] - loc).T @ (Xg[te] - loc) / len(te)
    scores0.append(-(np.sum(Ste * Ptr) - np.linalg.slogdet(Ptr)[1] + 5 * math.log(2 * math.pi)) / 2)
report("GraphicalLassoCV cv_results_ alpha=0 row = per-fold EmpiricalCovariance test log-likelihood (recomputed)", all(close(res[f"split{i}_test_score"][-1], scores0[i], 1e-10) for i in range(3)) and close(mts[-1], np.mean(scores0), 1e-10))
report("GraphicalLassoCV: mean_test_score / std_test_score are the mean / std over the split columns", np.allclose(mts, np.mean([res[f"split{i}_test_score"] for i in range(3)], axis=0)) and np.allclose(res["std_test_score"], np.std([res[f"split{i}_test_score"] for i in range(3)], axis=0)))
gl_best = GraphicalLasso(alpha=gcv.alpha_).fit(Xg)
report("GraphicalLassoCV final precision_ = GraphicalLasso(alpha=alpha_) refit on the whole data ('the model is fit again using the entire training set')", dev(gcv.precision_, gl_best.precision_) < 1e-10)
gcv2 = GraphicalLassoCV(alphas=[0.05, 0.2, 0.1], cv=cvo).fit(Xg)
report("GraphicalLassoCV(alphas=list): cv_results_ alphas = the list sorted descending + [0], no refinement", np.allclose(gcv2.cv_results_["alphas"], [0.2, 0.1, 0.05, 0]) and gcv2.alpha_ in (0.05, 0.1, 0.2))

# =============================================================================================== cross_decomposition
print("== sklearn.cross_decomposition")
from sklearn.cross_decomposition import PLSRegression, PLSCanonical, CCA, PLSSVD
def pls_ref(X, Y, K, mode="A", deflation="regression", scale=True, algorithm="nipals", tol=1e-14, max_iter=20000):
    X = np.array(X, float); Y = np.array(Y, float)
    if Y.ndim == 1: Y = Y[:, None]
    n, p = X.shape; q = Y.shape[1]; xm, ym = X.mean(0), Y.mean(0); X = X - xm; Y = Y - ym
    if scale:
        xs = X.std(0, ddof=1); xs[xs == 0] = 1; ys = Y.std(0, ddof=1); ys[ys == 0] = 1
    else: xs, ys = np.ones(p), np.ones(q)
    X = X / xs; Y = Y / ys; norm_y = deflation == "canonical"
    W = np.zeros((p, K)); Cw = np.zeros((q, K)); T = np.zeros((n, K)); U = np.zeros((n, K)); P = np.zeros((p, K)); Q = np.zeros((q, K)); n_iter = []
    for k in range(K):
        if algorithm == "svd":
            u_, s_, vt_ = np.linalg.svd(X.T @ Y, full_matrices=False); w = u_[:, 0]; c = vt_[0]
        else:
            yscore = Y[:, next(j for j in range(q) if np.abs(Y[:, j]).max() > 1e-13)]
            if mode == "B": Xp, Yp = np.linalg.pinv(X), np.linalg.pinv(Y)
            w_old = None
            for it in range(max_iter):
                w = Xp @ yscore if mode == "B" else X.T @ yscore / (yscore @ yscore); w = w / np.linalg.norm(w); t = X @ w
                c = Yp @ t if mode == "B" else Y.T @ t / (t @ t)
                if norm_y: c = c / np.linalg.norm(c)
                yscore = Y @ c / (c @ c)
                if q == 1 or (w_old is not None and np.sum((w - w_old) ** 2) < tol): break
                w_old = w
            n_iter.append(it + 1)
        s = np.sign(w[np.argmax(np.abs(w))]); w = w * s; c = c * s
        t = X @ w; u = Y @ c / (1.0 if norm_y else c @ c)
        pk = X.T @ t / (t @ t); X = X - np.outer(t, pk)
        if deflation == "canonical": qk = Y.T @ u / (u @ u); Y = Y - np.outer(u, qk)
        else: qk = Y.T @ t / (t @ t); Y = Y - np.outer(t, qk)
        W[:, k], Cw[:, k], T[:, k], U[:, k], P[:, k], Q[:, k] = w, c, t, u, pk, qk
    xrot = W @ np.linalg.pinv(P.T @ W); yrot = Cw @ np.linalg.pinv(Q.T @ Cw); coef_s = xrot @ Q.T
    return dict(W=W, C=Cw, T=T, U=U, P=P, Q=Q, xrot=xrot, yrot=yrot, coef=(coef_s * ys).T / xs, coef_s=coef_s, xm=xm, ym=ym, xs=xs, ys=ys, n_iter=n_iter)
def same_up_to_sign(A, B, tol):
    A = np.asarray(A, float); B = np.asarray(B, float); A = A.reshape(A.shape[0], -1); B = B.reshape(B.shape[0], -1)
    return all(min(dev(A[:, k], B[:, k]), dev(-A[:, k], B[:, k])) < tol for k in range(B.shape[1]))
Xp_ = rs.randn(25, 4) @ np.array([[1, 0.5, 0, 0.2], [0, 1, 0.3, 0], [0, 0, 1, 0.4], [0, 0, 0, 1]]) + np.array([10, -3, 0, 5])
Yp_ = Xp_ @ rs.randn(4, 3) + 0.3 * rs.randn(25, 3) + np.array([2, -1, 4])
for K in (1, 2, 3):
    pls = PLSRegression(n_components=K, tol=1e-14, max_iter=20000).fit(Xp_, Yp_); ref = pls_ref(Xp_, Yp_, K)
    coef_lib = np.asarray(pls.coef_); coef_exp = ref["coef"] if VER >= (1, 5) else ((ref["coef_s"] * ref["ys"]).T if VER >= (1, 3) else ref["coef_s"] * ref["ys"])
    print(f"   PLSRegression K={K}: n_iter_ {pls.n_iter_} (ref {ref['n_iter']}); |x_weights| cols {np.linalg.norm(pls.x_weights_, axis=0).round(12).tolist()}; coef_ shape {coef_lib.shape}, dev from the version's convention {dev(coef_lib, coef_exp):.1e}")
    report(f"PLSRegression K={K}: x_weights_ = unit-norm left singular vectors of X_k^T Y_k from the power method (NIPALS reference, mode A)", dev(pls.x_weights_, ref["W"]) < 1e-8 and np.allclose(np.linalg.norm(pls.x_weights_, axis=0), 1, atol=1e-12))
    report(f"PLSRegression K={K}: y_weights_ = Y_k^T t_k / (t_k^T t_k), 'never normalized' (user guide)", dev(pls.y_weights_, ref["C"]) < 1e-8)
    report(f"PLSRegression K={K}: x_loadings_ / y_loadings_ = regressions of X_k, Y_k on the x-score xi_k", dev(pls.x_loadings_, ref["P"]) < 1e-8 and dev(pls.y_loadings_, ref["Q"]) < 1e-8)
    report(f"PLSRegression K={K}: x_scores_ = X_k u_k and y_scores_ = Y_k v_k / (v_k^T v_k)", dev(pls.x_scores_, ref["T"]) < 1e-8 and dev(pls.y_scores_, ref["U"]) < 1e-8)
    report(f"PLSRegression K={K}: x_rotations_ = W (P^T W)^-1 and transform(X_train) = x_scores_ ('XP = Xi')", dev(pls.x_rotations_, ref["xrot"]) < 1e-8 and dev(pls.transform(Xp_), ref["T"]) < 1e-8)
    report(f"PLSRegression K={K}: x_scores_ columns are mutually orthogonal (Xi^T Xi diagonal)", np.abs(pls.x_scores_.T @ pls.x_scores_ - np.diag(np.diag(pls.x_scores_.T @ pls.x_scores_))).max() < 1e-8 * np.abs(pls.x_scores_).max() ** 2)
    if VER >= (1, 5):
        report(f"PLSRegression K={K}: coef_ shape (n_targets, n_features) and = (x_rotations_ y_loadings_^T * y_std)^T / x_std (original-unit coefficients, 1.5+)", pls.coef_.shape == (3, 4) and dev(pls.coef_, ref["coef"]) < 1e-8)
        report(f"PLSRegression K={K}: predict(X) = (X - x_mean) @ coef_.T + intercept_, intercept_ = y mean", dev(pls.predict(Xp_), (Xp_ - Xp_.mean(0)) @ pls.coef_.T + pls.intercept_) < 1e-10 and dev(pls.intercept_, Yp_.mean(0)) < 1e-12)
        report(f"PLSRegression K={K}: documented formula 'y = X @ coef_.T + intercept_' reproduces predict(X) on data with non-zero feature means", dev(pls.predict(Xp_), Xp_ @ pls.coef_.T + pls.intercept_) < 1e-8, f"(max rel dev {dev(pls.predict(Xp_), Xp_ @ pls.coef_.T + pls.intercept_):.1e})")
    elif VER >= (1, 3):
        report(f"PLSRegression K={K}: coef_ shape (n_targets, n_features) and = (x_rotations_ y_loadings_^T * y_std)^T [1.3-1.4: scaled-X coefficients, fixed in 1.5]", pls.coef_.shape == (3, 4) and dev(pls.coef_, (ref["coef_s"] * ref["ys"]).T) < 1e-8)
        report(f"PLSRegression K={K}: predict(X) = ((X - x_mean)/x_std) @ coef_.T + intercept_ [1.3-1.4], intercept_ = y mean", dev(pls.predict(Xp_), ((Xp_ - Xp_.mean(0)) / ref["xs"]) @ pls.coef_.T + pls.intercept_) < 1e-10 and dev(pls.intercept_, Yp_.mean(0)) < 1e-12)
        report(f"PLSRegression K={K}: documented formula 'Y = X @ coef_.T + intercept_' reproduces predict(X) on data with non-zero feature means", dev(pls.predict(Xp_), Xp_ @ pls.coef_.T + pls.intercept_) < 1e-8, f"(max rel dev {dev(pls.predict(Xp_), Xp_ @ pls.coef_.T + pls.intercept_):.1e})")
    else:
        report(f"PLSRegression K={K}: coef_ shape (n_features, n_targets) [<1.3] and = x_rotations_ y_loadings_^T * y_std (scaled-X coefficients)", np.asarray(pls.coef_).shape == (4, 3) and dev(np.asarray(pls.coef_), ref["coef_s"] * ref["ys"]) < 1e-8)
        report(f"PLSRegression K={K}: predict(X) = ((X - x_mean)/x_std) @ coef_ + intercept_ [<1.3], intercept_ = y mean", dev(pls.predict(Xp_), ((Xp_ - Xp_.mean(0)) / ref["xs"]) @ np.asarray(pls.coef_) + pls.intercept_) < 1e-10 and dev(pls.intercept_, Yp_.mean(0)) < 1e-12)
        report(f"PLSRegression K={K}: documented formula 'Y = X @ coef_ + intercept_' reproduces predict(X) on data with non-zero feature means", dev(pls.predict(Xp_), Xp_ @ np.asarray(pls.coef_) + pls.intercept_) < 1e-8, f"(max rel dev {dev(pls.predict(Xp_), Xp_ @ np.asarray(pls.coef_) + pls.intercept_):.1e})")
    report(f"PLSRegression K={K}: predict(X) = NIPALS reference prediction", dev(pls.predict(Xp_), (Xp_ - ref["xm"]) @ ref["coef"].T + ref["ym"]) < 1e-8)
    xs_, ys_ = pls.transform(Xp_, Yp_)
    report(f"PLSRegression K={K}: transform(X, y) returns (x_scores, y_scores) with y_scores = Y_scaled @ y_rotations_", dev(xs_, ref["T"]) < 1e-8 and dev(ys_, ((Yp_ - ref["ym"]) / ref["ys"]) @ ref["yrot"]) < 1e-8)
pls_def = PLSRegression(n_components=2).fit(Xp_, Yp_); ref2 = pls_ref(Xp_, Yp_, 2)
print(f"   PLSRegression default tol=1e-6: coef dev from the tightly converged reference {dev(pls_def.coef_ if VER >= (1, 3) else np.asarray(pls_def.coef_).T, ref2['coef']):.1e}, n_iter_ {pls_def.n_iter_}")
report("PLSRegression default tol=1e-6 agrees with the converged reference within 1e-4", dev(pls_def.predict(Xp_), (Xp_ - ref2["xm"]) @ ref2["coef"].T + ref2["ym"]) < 1e-4)
pls4 = PLSRegression(n_components=4, tol=1e-14, max_iter=20000).fit(Xp_, Yp_)
report("PLSRegression n_components = n_features: inverse_transform(transform(X)) = X ('only exact if n_components=n_features')", dev(pls4.inverse_transform(pls4.transform(Xp_)), Xp_) < 1e-8)
refn = pls_ref(Xp_, Yp_, 2, scale=False); plsn = PLSRegression(n_components=2, scale=False, tol=1e-14, max_iter=20000).fit(Xp_, Yp_)
report("PLSRegression(scale=False): weights/loadings/coef from the centred-only reference", dev(plsn.x_weights_, refn["W"]) < 1e-8 and dev(plsn.y_loadings_, refn["Q"]) < 1e-8 and dev(plsn.predict(Xp_), (Xp_ - refn["xm"]) @ refn["coef"].T + refn["ym"]) < 1e-8)
y1 = Yp_[:, 0]; pls1 = PLSRegression(n_components=2, tol=1e-14, max_iter=20000).fit(Xp_, y1); ref1 = pls_ref(Xp_, y1, 2)
print(f"   PLSRegression fitted with 1-D y: predict shape {pls1.predict(Xp_).shape} (1.3+ ravel to (n_samples,); earlier versions return (n_samples, 1))")
report(f"PLSRegression 1-D y (PLS1): predict returns shape {'(n_samples,)' if VER >= (1, 3) else '(n_samples, 1) [<1.3]'} and matches the reference", pls1.predict(Xp_).shape == ((25,) if VER >= (1, 3) else (25, 1)) and dev(pls1.predict(Xp_).ravel(), ((Xp_ - ref1["xm"]) @ ref1["coef"].T + ref1["ym"]).ravel()) < 1e-8)
try:
    PLSRegression(n_components=5).fit(Xp_, Yp_); report("PLSRegression n_components > min(n_samples, n_features) raises ValueError", False)
except ValueError as e: report("PLSRegression n_components > min(n_samples, n_features) raises ValueError", True, f"({str(e)[:50]})")
report("PLSRegression n_components = n_features (4) > n_targets (3) is allowed (bound is rank of X^T X)", PLSRegression(n_components=4).fit(Xp_, Yp_) is not None)
for cls, nm in ((PLSCanonical, "PLSCanonical"), (CCA, "CCA")):
    try:
        cls(n_components=4).fit(Xp_, Yp_); report(f"{nm} n_components > min(n_samples, n_features, n_targets) raises ValueError", False)
    except ValueError: report(f"{nm} n_components > min(n_samples, n_features, n_targets) raises ValueError", True)
p32 = PLSRegression(n_components=2, tol=1e-14, max_iter=20000).fit(Xp_.astype(np.float32), Yp_.astype(np.float32))
print(f"   PLSRegression float32 input: coef_ dtype {np.asarray(p32.coef_).dtype}, predict dev from float64 fit {dev(p32.predict(Xp_), pls_def.predict(Xp_)):.1e}")
report("PLSRegression float32 input: predictions within 1e-4 of the float64 fit", dev(p32.predict(Xp_), pls_def.predict(Xp_)) < 1e-4)
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); plsc = PLSRegression(n_components=1).fit(Xp_, np.full(25, 3.0))
print(f"   PLSRegression with constant y: warnings {[str(w.message)[:50] for w in wl]}, coef_ {np.asarray(plsc.coef_).ravel().tolist()}, predict {plsc.predict(Xp_[:2]).ravel().tolist()}")
report("PLSRegression with constant y warns 'y residual is constant', coef_ = 0 and predict = the constant", any("constant" in str(w.message) for w in wl) and np.all(np.asarray(plsc.coef_) == 0) and np.allclose(plsc.predict(Xp_), 3.0))
# PLSCanonical
for K in (1, 2, 3):
    for alg in ("nipals", "svd"):
        pc = PLSCanonical(n_components=K, algorithm=alg, tol=1e-14, max_iter=20000).fit(Xp_, Yp_); refc = pls_ref(Xp_, Yp_, K, deflation="canonical", algorithm=alg)
        report(f"PLSCanonical K={K} algorithm='{alg}': x_weights_, y_weights_ (both unit norm, 'canonical'), loadings and rotations = reference", dev(pc.x_weights_, refc["W"]) < 1e-8 and dev(pc.y_weights_, refc["C"]) < 1e-8 and np.allclose(np.linalg.norm(pc.y_weights_, axis=0), 1, atol=1e-10) and dev(pc.x_loadings_, refc["P"]) < 1e-8 and dev(pc.y_loadings_, refc["Q"]) < 1e-8 and dev(pc.x_rotations_, refc["xrot"]) < 1e-8 and dev(pc.y_rotations_, refc["yrot"]) < 1e-8)
        xs_, ys_ = pc.transform(Xp_, Yp_)
        report(f"PLSCanonical K={K} algorithm='{alg}': transform(X, y) = (Xi, Omega) of the reference; predict = reference", dev(xs_, refc["T"]) < 1e-8 and dev(ys_, refc["U"]) < 1e-8 and dev(pc.predict(Xp_), (Xp_ - refc["xm"]) @ refc["coef"].T + refc["ym"]) < 1e-8)
pcn = PLSCanonical(n_components=2, tol=1e-14, max_iter=20000).fit(Xp_, Yp_); pcs = PLSCanonical(n_components=2, algorithm="svd").fit(Xp_, Yp_)
print(f"   PLSCanonical nipals (tol=1e-14 on ||u_i - u_(i-1)||^2) vs svd: x_weights_ dev {dev(pcn.x_weights_, pcs.x_weights_):.1e}, predict dev {dev(pcn.predict(Xp_), pcs.predict(Xp_)):.1e}")
report("PLSCanonical algorithm='nipals' and 'svd' agree within 1e-6 (documented: two ways of performing step a; power method stops at ||u_i - u_(i-1)||^2 < tol)", dev(pcn.x_weights_, pcs.x_weights_) < 1e-6 and dev(pcn.predict(Xp_), pcs.predict(Xp_)) < 1e-6)
pc3 = PLSCanonical(n_components=3, tol=1e-14, max_iter=20000).fit(Xp_[:, :3], Yp_); xr, yr = pc3.inverse_transform(*pc3.transform(Xp_[:, :3], Yp_))
report("PLSCanonical with n_components = n_features = n_targets = 3: inverse_transform(transform(X, y)) = (X, y)", dev(xr, Xp_[:, :3]) < 1e-8 and dev(yr, Yp_) < 1e-8)
# PLSSVD vs SVD of X'Y
def plssvd_ref(X, Y, K, scale=True):
    X = np.array(X, float) - X.mean(0); Y = np.array(Y, float) - Y.mean(0)
    if scale: X = X / X.std(0, ddof=1); Y = Y / Y.std(0, ddof=1)
    U, s, Vt = np.linalg.svd(X.T @ Y, full_matrices=False); U = U[:, :K]; V = Vt[:K].T
    sg = np.sign(U[np.argmax(np.abs(U), axis=0), range(K)]); return U * sg, V * sg, X, Y, s
for K in (1, 2, 3):
    for sc in (True, False):
        ps = PLSSVD(n_components=K, scale=sc).fit(Xp_, Yp_); U, V, Xs, Ys, s = plssvd_ref(Xp_, Yp_, K, sc); xt, yt = ps.transform(Xp_, Yp_)
        report(f"PLSSVD K={K} scale={sc}: x_weights_/y_weights_ = leading singular vectors of X^T Y (sign: largest |u| entry positive) and transform = XU, YV", dev(ps.x_weights_, U) < 1e-10 and dev(ps.y_weights_, V) < 1e-10 and dev(xt, Xs @ U) < 1e-10 and dev(yt, Ys @ V) < 1e-10)
ps1 = PLSSVD(n_components=1).fit(Xp_, Yp_); pc1 = PLSCanonical(n_components=1, tol=1e-14, max_iter=20000).fit(Xp_, Yp_)
xs1, ys1 = ps1.transform(Xp_, Yp_); xc1, yc1 = pc1.transform(Xp_, Yp_)
print(f"   PLSSVD(1) vs PLSCanonical(1, nipals tol=1e-14): x_scores dev {dev(xs1, xc1):.1e}, y_scores dev {dev(ys1, yc1):.1e}; vs PLSCanonical(1, algorithm='svd'): {dev(xs1, PLSCanonical(n_components=1, algorithm='svd').fit(Xp_, Yp_).transform(Xp_, Yp_)[0]):.1e}")
report("PLSSVD(n_components=1) and PLSCanonical(n_components=1) transforms are 'strictly equivalent' (user guide; within 1e-6 for nipals, 1e-10 for algorithm='svd')", dev(xs1, xc1) < 1e-6 and dev(ys1, yc1) < 1e-6 and dev(xs1, PLSCanonical(n_components=1, algorithm="svd").fit(Xp_, Yp_).transform(Xp_, Yp_)[0]) < 1e-10)
try:
    PLSSVD(n_components=4).fit(Xp_, Yp_); report("PLSSVD n_components > min(n_samples, n_features, n_targets) raises ValueError", False)
except ValueError: report("PLSSVD n_components > min(n_samples, n_features, n_targets) raises ValueError", True)
# CCA vs canonical correlations from the whitened cross-covariance
def cca_ref(X, Y, scale=True):
    X = np.array(X, float) - X.mean(0); Y = np.array(Y, float) - Y.mean(0)
    if scale: X = X / X.std(0, ddof=1); Y = Y / Y.std(0, ddof=1)
    def inv_sqrt(A): w, V = np.linalg.eigh(A); return (V / np.sqrt(w)) @ V.T
    Ai, Bi = inv_sqrt(X.T @ X), inv_sqrt(Y.T @ Y); Uw, s, Vt = np.linalg.svd(Ai @ (X.T @ Y) @ Bi)
    return s, Ai @ Uw, Bi @ Vt.T, X, Y
for K in (1, 2, 3):
    cca = CCA(n_components=K, tol=1e-14, max_iter=20000).fit(Xp_, Yp_); rho, A, B, Xs, Ys = cca_ref(Xp_, Yp_); xt, yt = cca.transform(Xp_, Yp_)
    corr = [np.corrcoef(xt[:, k], yt[:, k])[0, 1] for k in range(K)]
    cosx = [abs(cca.x_rotations_[:, k] @ A[:, k]) / np.linalg.norm(cca.x_rotations_[:, k]) / np.linalg.norm(A[:, k]) for k in range(K)]
    cosy = [abs(cca.y_rotations_[:, k] @ B[:, k]) / np.linalg.norm(cca.y_rotations_[:, k]) / np.linalg.norm(B[:, k]) for k in range(K)]
    print(f"   CCA K={K}: corr(x_scores, y_scores) {np.round(corr, 10).tolist()} vs singular values of Sxx^-1/2 Sxy Syy^-1/2 {rho[:K].round(10).tolist()}; |cos| rotations vs canonical weights x {np.round(cosx, 10).tolist()} y {np.round(cosy, 10).tolist()}")
    report(f"CCA K={K}: correlations of the transformed pairs = the first {K} canonical correlations (SVD of the whitened cross-covariance)", all(close(c, r, 1e-8) for c, r in zip(corr, rho)))
    report(f"CCA K={K}: x_rotations_/y_rotations_ columns are parallel to the canonical weight vectors", all(abs(c - 1) < 1e-8 for c in cosx + cosy))
    refB = pls_ref(Xp_, Yp_, K, mode="B", deflation="canonical")
    report(f"CCA K={K}: weights/loadings/predict = mode-B NIPALS reference", dev(cca.x_weights_, refB["W"]) < 1e-8 and dev(cca.y_weights_, refB["C"]) < 1e-8 and dev(cca.predict(Xp_), (Xp_ - refB["xm"]) @ refB["coef"].T + refB["ym"]) < 1e-8)
report("CCA transformed x and y scores are unit-correlation-free across components (Xi^T Xi and Omega^T Omega diagonal)", np.abs(np.corrcoef(xt.T) - np.eye(3)).max() < 1e-8 and np.abs(np.corrcoef(yt.T) - np.eye(3)).max() < 1e-8)
p_off = PLSRegression(n_components=2, tol=1e-14, max_iter=20000).fit(Xp_ + 1e6, Yp_)
report("PLSRegression with 1e6 offset on X: predictions within 1e-6 of the offset-free fit", dev(p_off.predict(Xp_ + 1e6), PLSRegression(n_components=2, tol=1e-14, max_iter=20000).fit(Xp_, Yp_).predict(Xp_)) < 1e-6, f"(dev {dev(p_off.predict(Xp_ + 1e6), PLSRegression(n_components=2, tol=1e-14, max_iter=20000).fit(Xp_, Yp_).predict(Xp_)):.1e})")

# =============================================================================================== kernel_ridge
print("== sklearn.kernel_ridge.KernelRidge")
from sklearn.kernel_ridge import KernelRidge
Xk = rs.randint(-3, 4, (7, 2)); yk = rs.randint(-5, 6, 7); Xkt = rs.randint(-3, 4, (4, 2))
Kf = fmul(fmat(Xk), ftr(fmat(Xk))); Kt = fmul(fmat(Xkt), ftr(fmat(Xk)))
def exact_dual(K, y, alpha, w=None):
    n = len(K); A = [[K[i][j] + (F(alpha) * (1 if w is None else 1 / F(w[i])) if i == j else 0) for j in range(n)] for i in range(n)]
    return [row[0] for row in fmul(finv(A), [[F(int(v))] for v in y])]
kr = KernelRidge(alpha=1.0, kernel="linear").fit(Xk, yk); dual = exact_dual(Kf, yk, 1)
report("KernelRidge(linear, alpha=1): dual_coef_ = (K + alpha I)^-1 y exactly (rational arithmetic)", dev(kr.dual_coef_, tofl(dual)) < 1e-12)
report("KernelRidge(linear): predict(X_test) = K(X_test, X_fit) @ dual_coef_", dev(kr.predict(Xkt), tofl([r[0] for r in fmul(Kt, [[d] for d in dual])])) < 1e-12)
XtX = fmul(ftr(fmat(Xk)), fmat(Xk)); primal = fmul(finv([[XtX[i][j] + (1 if i == j else 0) for j in range(2)] for i in range(2)]), fmul(ftr(fmat(Xk)), [[F(int(v))] for v in yk]))
report("KernelRidge(linear, alpha) predictions = primal ridge (X^T X + alpha I)^-1 X^T y without intercept (kernel trick identity)", dev(kr.predict(Xkt), tofl([r[0] for r in fmul(fmat(Xkt), primal)])) < 1e-12)
Kp = [[(v + 1) ** 2 for v in row] for row in Kf]; Kpt = [[(v + 1) ** 2 for v in row] for row in Kt]
krp = KernelRidge(alpha=2.0, kernel="poly", gamma=1.0, coef0=1, degree=2).fit(Xk, yk); dualp = exact_dual(Kp, yk, 2)
report("KernelRidge(poly, gamma=1, coef0=1, degree=2, alpha=2): dual_coef_ and predict exact with K = (x.y + 1)^2", dev(krp.dual_coef_, tofl(dualp)) < 1e-12 and dev(krp.predict(Xkt), tofl([r[0] for r in fmul(Kpt, [[d] for d in dualp])])) < 1e-12)
Xr = rs.randn(9, 3); yr = rs.randn(9); Xrt = rs.randn(5, 3)
my_rbf_k = lambda A, B, g: np.exp(-g * ((A[:, None, :] - B[None, :, :]) ** 2).sum(-1))
for g in (0.3, None):
    gg = 0.3 if g is not None else 1 / 3
    krr = KernelRidge(alpha=0.5, kernel="rbf", gamma=g).fit(Xr, yr); d_ref = np.linalg.solve(my_rbf_k(Xr, Xr, gg) + 0.5 * np.eye(9), yr)
    report(f"KernelRidge(rbf, gamma={g}{' -> 1/n_features' if g is None else ''}, alpha=0.5): dual_coef_ = (K + alpha I)^-1 y with K = exp(-gamma ||x-y||^2)", dev(krr.dual_coef_, d_ref) < 1e-10 and dev(krr.predict(Xrt), my_rbf_k(Xrt, Xr, gg) @ d_ref) < 1e-10)
kpre = KernelRidge(alpha=0.5, kernel="precomputed").fit(my_rbf_k(Xr, Xr, 0.3), yr)
report("KernelRidge(kernel='precomputed'): fit on K and predict on K_test reproduce the rbf model", dev(kpre.dual_coef_, np.linalg.solve(my_rbf_k(Xr, Xr, 0.3) + 0.5 * np.eye(9), yr)) < 1e-10 and dev(kpre.predict(my_rbf_k(Xrt, Xr, 0.3)), KernelRidge(alpha=0.5, kernel="rbf", gamma=0.3).fit(Xr, yr).predict(Xrt)) < 1e-10)
w = rs.randint(1, 5, 7); krw = KernelRidge(alpha=1.0, kernel="linear").fit(Xk, yk, sample_weight=w); dualw = exact_dual(Kf, yk, 1, w)
report("KernelRidge sample_weight: dual_coef_ = (K + alpha diag(1/w))^-1 y (minimiser of sum_i w_i (y_i - f_i)^2 + alpha ||f||^2)", dev(krw.dual_coef_, tofl(dualw)) < 1e-12)
w2 = np.ones(7); w2[0] = 2; Xdup = np.vstack([Xk, Xk[:1]]); ydup = np.append(yk, yk[0])
report("KernelRidge integer sample_weight 2 on a sample == duplicating that sample (predictions equal)", dev(KernelRidge(alpha=1.0).fit(Xk, yk, sample_weight=w2).predict(Xkt), KernelRidge(alpha=1.0).fit(Xdup, ydup).predict(Xkt)) < 1e-12)
report("KernelRidge scalar float sample_weight=2.0 == alpha/2 (uniform reweighting)", dev(KernelRidge(alpha=1.0).fit(Xk, yk, sample_weight=2.0).dual_coef_, KernelRidge(alpha=0.5).fit(Xk, yk).dual_coef_) < 1e-12)
Yk = np.column_stack([yk, rs.randint(-5, 6, 7)]); krm = KernelRidge(alpha=[0.5, 2.0], kernel="linear").fit(Xk, Yk)
report("KernelRidge multi-output with alpha array: column j solved with alpha_j ('penalties are assumed to be specific to the targets')", krm.dual_coef_.shape == (7, 2) and dev(krm.dual_coef_[:, 0], tofl(exact_dual(Kf, Yk[:, 0], F(1, 2)))) < 1e-12 and dev(krm.dual_coef_[:, 1], tofl(exact_dual(Kf, Yk[:, 1], 2))) < 1e-12)
krm1 = KernelRidge(alpha=1.0, kernel="linear").fit(Xk, Yk)
report("KernelRidge multi-output scalar alpha: each column = separate single-output fit", dev(krm1.dual_coef_[:, 1], KernelRidge(alpha=1.0).fit(Xk, Yk[:, 1]).dual_coef_) < 1e-12 and krm1.predict(Xkt).shape == (4, 2))
kr0 = KernelRidge(alpha=0.0, kernel="rbf", gamma=0.3).fit(Xr, yr)
report("KernelRidge(alpha=0) with a full-rank rbf kernel interpolates the training targets", dev(kr0.predict(Xr), yr) < 1e-8)
kr32 = KernelRidge(alpha=0.5, kernel="rbf", gamma=0.3).fit(Xr.astype(np.float32), yr.astype(np.float32))
print(f"   KernelRidge float32 input: dual_coef_ dtype {kr32.dual_coef_.dtype}, dev from float64 {dev(kr32.dual_coef_, KernelRidge(alpha=0.5, kernel='rbf', gamma=0.3).fit(Xr, yr).dual_coef_):.1e}")
report("KernelRidge float32 input: dual_coef_ within 1e-4 of the float64 fit", dev(kr32.dual_coef_, KernelRidge(alpha=0.5, kernel="rbf", gamma=0.3).fit(Xr, yr).dual_coef_) < 1e-4)
for off in (1e3, 1e5):
    kro = KernelRidge(alpha=0.5, kernel="rbf", gamma=0.3).fit(Xr + off, yr); d_ref = np.linalg.solve(my_rbf_k(Xr, Xr, 0.3) + 0.5 * np.eye(9), yr)
    print(f"   KernelRidge rbf with feature offset {off:.0e}: dual_coef_ dev from exact (offset-free) {dev(kro.dual_coef_, d_ref):.1e}")
    report(f"KernelRidge rbf with feature offset {off:.0e}: dual_coef_ within 1e-4 of the exact translation-invariant solution (rbf_kernel uses the ||x||^2 + ||y||^2 - 2 x.y expansion)", dev(kro.dual_coef_, d_ref) < 1e-4)

# =============================================================================================== isotonic
print("== sklearn.isotonic")
from sklearn.isotonic import IsotonicRegression, isotonic_regression, check_increasing
def pava_exact(y, w=None):
    w = [1] * len(y) if w is None else w; blocks = []
    for yi, wi in zip(y, w):
        blocks.append([F(yi) * F(wi), F(wi), 1])
        while len(blocks) > 1 and blocks[-2][0] / blocks[-2][1] > blocks[-1][0] / blocks[-1][1]:
            b = blocks.pop(); blocks[-1][0] += b[0]; blocks[-1][1] += b[1]; blocks[-1][2] += b[2]
    out = []
    for b in blocks: out += [b[0] / b[1]] * b[2]
    return out
def pava_dec(y, w=None): return pava_exact(y[::-1], None if w is None else w[::-1])[::-1]
ex = isotonic_regression([5, 3, 1, 2, 8, 10, 7, 9, 6, 4])
report("isotonic_regression docstring example -> [2.75]*4 + [7.333..]*6", np.allclose(ex, [2.75] * 4 + [22 / 3] * 6, rtol=1e-12))
yi = rs.randint(-5, 10, 15); wi = rs.randint(1, 4, 15)
report("isotonic_regression(y) = exact pool-adjacent-violators solution (Fractions), ties and negatives included", dev(isotonic_regression(yi.astype(float)), tofl(pava_exact(yi))) < 1e-14)
report("isotonic_regression(y, sample_weight) = exact weighted PAVA", dev(isotonic_regression(yi.astype(float), sample_weight=wi.astype(float)), tofl(pava_exact(yi, wi))) < 1e-14)
report("isotonic_regression(increasing=False) = exact non-increasing PAVA (reverse, fit, reverse)", dev(isotonic_regression(yi.astype(float), sample_weight=wi.astype(float), increasing=False), tofl(pava_dec(list(yi), list(wi)))) < 1e-14)
clipped = [min(max(v, F(0)), F(5)) for v in pava_exact(yi, wi)]
report("isotonic_regression(y_min=0, y_max=5) = clip(PAVA, y_min, y_max) ('lower bound on the lowest predicted value')", dev(isotonic_regression(yi.astype(float), sample_weight=wi.astype(float), y_min=0, y_max=5), tofl(clipped)) < 1e-14)
fit = isotonic_regression(yi.astype(float), sample_weight=wi.astype(float))
report("isotonic fit is non-decreasing and preserves the weighted mean (sum w y = sum w yhat)", np.all(np.diff(fit) >= 0) and close((wi * fit).sum(), (wi * yi).sum(), 1e-12))
report("isotonic_regression of a constant / already-increasing sequence returns it unchanged; single element unchanged", np.array_equal(isotonic_regression([2.0, 2.0, 2.0]), [2, 2, 2]) and np.array_equal(isotonic_regression([1.0, 2.0, 3.0]), [1, 2, 3]) and np.array_equal(isotonic_regression([7.0]), [7.0]))
report("isotonic_regression with 1e8 offset and float64: exact", dev(isotonic_regression(yi + 1e8), tofl(pava_exact(yi)) + 1e8) < 1e-15)
f32 = isotonic_regression(yi.astype(np.float32))
print(f"   isotonic_regression float32 input: output dtype {f32.dtype}")
report("isotonic_regression float32 input returns float32 within 1e-6 of exact", f32.dtype == np.float32 and dev(f32, tofl(pava_exact(yi))) < 1e-6)
# IsotonicRegression with ties in X
Xt_ = rs.randint(0, 8, 20).astype(float); yt_ = rs.randint(-4, 8, 20).astype(float); wt_ = rs.randint(0, 4, 20).astype(float)
def iso_ref(X, y, w, increasing=True):
    w = np.ones_like(X) if w is None else w; m = w > 0; X, y, w = X[m], y[m], w[m]; ux = np.unique(X)
    yy = [sum(F(v) * F(ww) for v, ww in zip(y[X == u], w[X == u])) / sum(F(ww) for ww in w[X == u]) for u in ux]; ww = [sum(F(v) for v in w[X == u]) for u in ux]
    fitv = pava_exact(yy, ww) if increasing else pava_dec(yy, ww); return ux, tofl(fitv)
for wsel, tag in ((None, "unweighted"), (wt_, "weighted (zero weights dropped)")):
    ir = IsotonicRegression().fit(Xt_, yt_, sample_weight=wsel); ux, fv = iso_ref(Xt_, yt_, wsel)
    pred_ref = np.interp(Xt_, ux, fv)
    report(f"IsotonicRegression with tied X, {tag}: fitted values = PAVA on tie-pooled weighted means ('secondary method from de Leeuw 1977') exactly", dev(ir.predict(Xt_), pred_ref) < 1e-14)
    report(f"IsotonicRegression {tag}: X_thresholds_ ascending unique, y_thresholds_ non-decreasing, X_min_/X_max_ = range of (positive-weight) X", np.all(np.diff(ir.X_thresholds_) > 0) and np.all(np.diff(ir.y_thresholds_) >= 0) and ir.X_min_ == ux[0] and ir.X_max_ == ux[-1])
    Tq = rs.uniform(ux[0], ux[-1], 30)
    report(f"IsotonicRegression {tag}: predictions between thresholds are linear interpolations (compared with np.interp over the untrimmed fit)", dev(ir.predict(Tq), np.interp(Tq, ux, fv)) < 1e-12)
    report(f"IsotonicRegression {tag}: transform == predict", np.array_equal(ir.transform(Tq), ir.predict(Tq)))
ir = IsotonicRegression().fit(Xt_, yt_); ux, fv = iso_ref(Xt_, yt_, None); Tout = np.array([ux[0] - 1, ux[0], ux[-1], ux[-1] + 2])
report("IsotonicRegression(out_of_bounds='nan'): NaN outside [X_min_, X_max_], defined at the bounds", np.isnan(ir.predict(Tout)[[0, 3]]).all() and dev(ir.predict(Tout)[[1, 2]], [fv[0], fv[-1]]) < 1e-14)
irc = IsotonicRegression(out_of_bounds="clip").fit(Xt_, yt_)
report("IsotonicRegression(out_of_bounds='clip'): outside values get the nearest endpoint value", dev(irc.predict(Tout), [fv[0], fv[0], fv[-1], fv[-1]]) < 1e-14)
try:
    IsotonicRegression(out_of_bounds="raise").fit(Xt_, yt_).predict(Tout); report("IsotonicRegression(out_of_bounds='raise') raises ValueError outside the domain", False)
except ValueError: report("IsotonicRegression(out_of_bounds='raise') raises ValueError outside the domain", True)
report("IsotonicRegression(y_min=0, y_max=3): fitted values clipped", dev(IsotonicRegression(y_min=0, y_max=3).fit(Xt_, yt_).predict(Xt_), np.clip(np.interp(Xt_, ux, fv), 0, 3)) < 1e-14)
irdec = IsotonicRegression(increasing=False).fit(Xt_, yt_); uxd, fvd = iso_ref(Xt_, yt_, None, increasing=False)
report("IsotonicRegression(increasing=False): fitted values = non-increasing PAVA on pooled ties", dev(irdec.predict(Xt_), np.interp(Xt_, uxd, fvd)) < 1e-14 and np.all(np.diff(irdec.y_thresholds_) <= 0))
def spearman(x, y):
    def rank(a):
        a = np.asarray(a, float); order = np.argsort(a, kind="mergesort"); r = np.empty(len(a)); s = a[order]; i = 0
        while i < len(a):
            j = i
            while j + 1 < len(a) and s[j + 1] == s[i]: j += 1
            r[order[i:j + 1]] = (i + j) / 2 + 1; i = j + 1
        return r
    rx, ry = rank(x), rank(y); return np.corrcoef(rx, ry)[0, 1]
xa = rs.randn(30); ya_dec = -xa + 0.5 * rs.randn(30); ya_inc = xa + 0.5 * rs.randn(30)
for yy, nm in ((ya_dec, "decreasing"), (ya_inc, "increasing")):
    rho = spearman(xa, yy); ira = IsotonicRegression(increasing="auto").fit(xa, yy)
    print(f"   increasing='auto' on {nm} data: my Spearman rho {rho:.4f}, increasing_ {ira.increasing_}, check_increasing {check_increasing(xa, yy)}")
    report(f"IsotonicRegression(increasing='auto') on {nm} data: increasing_ = (Spearman rho >= 0) and the fit is monotone in that direction", ira.increasing_ == (rho >= 0) and bool(check_increasing(xa, yy)) == (rho >= 0) and (np.all(np.diff(ira.y_thresholds_) >= 0) if rho >= 0 else np.all(np.diff(ira.y_thresholds_) <= 0)))
report("check_increasing([1..5], [2,4,6,8,10]) True and ([1..5], [10,8,6,4,2]) False (docstring)", bool(check_increasing([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])) is True and bool(check_increasing([1, 2, 3, 4, 5], [10, 8, 6, 4, 2])) is False)
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); ci = check_increasing([1, 2, 3, 4, 5], [1, 3, 2, 5, 4])
rho_ = 0.7; Fz = 0.5 * math.log((1 + rho_) / (1 - rho_)); lo, hi = math.tanh(Fz - 1.96 / math.sqrt(2)), math.tanh(Fz + 1.96 / math.sqrt(2))
print(f"   check_increasing rho=0.7, n=5: Fisher 95% CI ({lo:.3f}, {hi:.3f}) spans zero -> warning issued: {any('spans zero' in str(w.message) for w in wl)}")
report("check_increasing warns when the Fisher-transform 95% CI of rho spans zero (rho=0.7, n=5)", bool(ci) is True and any("spans zero" in str(w.message) for w in wl))
ir32 = IsotonicRegression().fit(Xt_.astype(np.float32), yt_.astype(np.float32))
print(f"   IsotonicRegression float32: X_thresholds_ dtype {ir32.X_thresholds_.dtype}, predict dtype {ir32.predict(Xt_.astype(np.float32)).dtype}")
report("IsotonicRegression float32 input: predictions within 1e-6 of the exact fit", dev(ir32.predict(Xt_.astype(np.float32)), np.interp(Xt_, ux, fv)) < 1e-6)
irs = IsotonicRegression().fit([2.0, 2.0, 2.0], [1.0, 2.0, 6.0]); ps_ = irs.predict([0.0, 2.0, 5.0])
print(f"   IsotonicRegression with a single distinct X (out_of_bounds='nan' default): thresholds {irs.X_thresholds_.tolist()}/{irs.y_thresholds_.tolist()}, predict([0, 2, 5]) = {ps_.tolist()}")
report("IsotonicRegression single distinct X: prediction at X = weighted mean 3.0", close(ps_[1], 3.0))
report("IsotonicRegression single distinct X with out_of_bounds='nan': predictions outside the (degenerate) training domain are NaN ('predictions will be NaN')", np.isnan(ps_[0]) and np.isnan(ps_[2]), f"(got {ps_.tolist()})")
irconst = IsotonicRegression().fit(Xt_, np.full(20, 4.0))
report("IsotonicRegression constant y: all predictions = the constant", np.allclose(irconst.predict(Xt_), 4.0))
report("IsotonicRegression 2-D input with one column accepted; get_feature_names_out = ['isotonicregression0']", dev(IsotonicRegression().fit(Xt_[:, None], yt_).predict(Xt_[:, None]), ir.predict(Xt_)) < 1e-14 and list(ir.get_feature_names_out()) == ["isotonicregression0"])
try:
    IsotonicRegression().fit(Xt_, np.where(np.arange(20) == 3, np.nan, yt_)); report("IsotonicRegression rejects NaN in y (ValueError)", False)
except ValueError: report("IsotonicRegression rejects NaN in y (ValueError)", True)

# =============================================================================================== gaussian_process
print("== sklearn.gaussian_process")
from sklearn.gaussian_process import GaussianProcessRegressor, GaussianProcessClassifier
from sklearn.gaussian_process.kernels import (RBF, Matern, RationalQuadratic, ExpSineSquared, DotProduct, WhiteKernel, ConstantKernel, Sum, Product, Exponentiation, PairwiseKernel, CompoundKernel)
def my_k(name, A, B, **h):
    A = np.atleast_2d(A); B = np.atleast_2d(B); D = A[:, None, :] - B[None, :, :]
    if name == "rbf": l = np.broadcast_to(np.asarray(h["l"], float), (A.shape[1],)); return np.exp(-0.5 * ((D / l) ** 2).sum(-1))
    if name == "matern":
        l = np.broadcast_to(np.asarray(h["l"], float), (A.shape[1],)); r = np.sqrt(((D / l) ** 2).sum(-1)); nu = h["nu"]
        if nu == 0.5: return np.exp(-r)
        if nu == 1.5: return (1 + math.sqrt(3) * r) * np.exp(-math.sqrt(3) * r)
        if nu == 2.5: return (1 + math.sqrt(5) * r + 5 * r ** 2 / 3) * np.exp(-math.sqrt(5) * r)
        if nu == np.inf: return np.exp(-r ** 2 / 2)
        out = np.ones_like(r)
        for idx in zip(*np.nonzero(r > 0)):
            z = mp.sqrt(2 * nu) * mp.mpf(r[idx]); out[idx] = float(2 ** (1 - nu) / mp.gamma(nu) * z ** nu * mp.besselk(nu, z))
        return out
    if name == "rq": d2 = (D ** 2).sum(-1); return (1 + d2 / (2 * h["a"] * h["l"] ** 2)) ** (-h["a"])
    if name == "ess": d = np.sqrt((D ** 2).sum(-1)); return np.exp(-2 * np.sin(math.pi * d / h["p"]) ** 2 / h["l"] ** 2)
    if name == "dot": return A @ B.T + h["s0"] ** 2
    if name == "const": return np.full((len(A), len(B)), h["c"])
    if name == "white": return h["s"] * np.eye(len(A)) if h.get("same") else np.zeros((len(A), len(B)))
Xg1 = rs.randn(7, 2); Yg1 = rs.randn(4, 2)
kernels = [("RBF iso", RBF(0.7), lambda A, B, same: my_k("rbf", A, B, l=0.7)),
           ("RBF anisotropic", RBF([0.7, 1.9]), lambda A, B, same: my_k("rbf", A, B, l=[0.7, 1.9])),
           ("Matern nu=0.5", Matern(0.8, nu=0.5), lambda A, B, same: my_k("matern", A, B, l=0.8, nu=0.5)),
           ("Matern nu=1.5", Matern(0.8, nu=1.5), lambda A, B, same: my_k("matern", A, B, l=0.8, nu=1.5)),
           ("Matern nu=2.5 anisotropic", Matern([0.8, 1.3], nu=2.5), lambda A, B, same: my_k("matern", A, B, l=[0.8, 1.3], nu=2.5)),
           ("Matern nu=inf", Matern(0.8, nu=np.inf), lambda A, B, same: my_k("matern", A, B, l=0.8, nu=np.inf)),
           ("Matern nu=0.7 (general, Bessel K_nu via mpmath)", Matern(0.8, nu=0.7), lambda A, B, same: my_k("matern", A, B, l=0.8, nu=0.7)),
           ("RationalQuadratic", RationalQuadratic(length_scale=0.9, alpha=0.6), lambda A, B, same: my_k("rq", A, B, l=0.9, a=0.6)),
           ("ExpSineSquared", ExpSineSquared(length_scale=0.9, periodicity=1.7), lambda A, B, same: my_k("ess", A, B, l=0.9, p=1.7)),
           ("DotProduct", DotProduct(sigma_0=0.6), lambda A, B, same: my_k("dot", A, B, s0=0.6)),
           ("ConstantKernel", ConstantKernel(2.5), lambda A, B, same: my_k("const", A, B, c=2.5)),
           ("WhiteKernel", WhiteKernel(0.3), lambda A, B, same: my_k("white", A, B, s=0.3, same=same)),
           ("Sum C*RBF + White", ConstantKernel(1.4) * RBF(0.7) + WhiteKernel(0.2), lambda A, B, same: 1.4 * my_k("rbf", A, B, l=0.7) + my_k("white", A, B, s=0.2, same=same)),
           ("Product RBF*ESS", RBF(0.7) * ExpSineSquared(0.9, 1.7), lambda A, B, same: my_k("rbf", A, B, l=0.7) * my_k("ess", A, B, l=0.9, p=1.7)),
           ("Exponentiation DotProduct**2", DotProduct(0.6) ** 2, lambda A, B, same: my_k("dot", A, B, s0=0.6) ** 2),
           ("PairwiseKernel rbf gamma=0.4", PairwiseKernel(gamma=0.4, metric="rbf"), lambda A, B, same: np.exp(-0.4 * ((A[:, None, :] - B[None, :, :]) ** 2).sum(-1)))]
for nm, kern, ref in kernels:
    KXX = kern(Xg1); KXY = kern(Xg1, Yg1); dg = kern.diag(Xg1)
    okf = dev(KXX, ref(Xg1, Xg1, True)) < 1e-12 and dev(KXY, ref(Xg1, Yg1, False)) < 1e-12
    report(f"kernel {nm}: k(X) and k(X, Y) match the documented formula coded independently", okf, "" if okf else f"(dev {dev(KXX, ref(Xg1, Xg1, True)):.1e}, {dev(KXY, ref(Xg1, Yg1, False)):.1e})")
    report(f"kernel {nm}: np.diag(k(X, X)) == k.diag(X)", dev(dg, np.diag(KXX)) < 1e-14)
    if "White" not in nm:
        report(f"kernel {nm}: k(X) == k(X, Y=X) (user guide identity for all kernels except WhiteKernel)", dev(kern(Xg1, Xg1), KXX) < 1e-14)
    elif nm != "WhiteKernel":
        report(f"kernel {nm}: k(X) - k(X, Y=X) = noise_level * I (a sum containing a WhiteKernel inherits its exception)", dev(KXX - kern(Xg1, Xg1), 0.2 * np.eye(7)) < 1e-14)
    else:
        report("kernel WhiteKernel: k(X, Y=X) is all zeros while k(X) = noise_level * I (documented exception)", np.all(kern(Xg1, Xg1) == 0) and dev(KXX, 0.3 * np.eye(7)) < 1e-15)
    if kern.n_dims > 0:
        th = kern.theta.copy(); K, G = kern(Xg1, eval_gradient=True); h = 1e-6; Gfd = np.zeros_like(G)
        for i in range(len(th)):
            tp = th.copy(); tp[i] += h; tm = th.copy(); tm[i] -= h; Gfd[:, :, i] = (kern.clone_with_theta(tp)(Xg1) - kern.clone_with_theta(tm)(Xg1)) / (2 * h)
        gdev = np.abs(G - Gfd).max() / max(1.0, np.abs(Gfd).max()); tol_g = 1e-4 if "general" in nm or "Pairwise" in nm else 1e-6
        report(f"kernel {nm}: eval_gradient = d k / d log(theta) (central finite differences in theta space, shape (n, n, n_dims))", G.shape == (7, 7, len(th)) and gdev < tol_g, f"(max dev {gdev:.1e}{'; numerical gradient in the library' if 'general' in nm or 'Pairwise' in nm else ''})")
        report(f"kernel {nm}: the gradient array is symmetric in (i, j) and K returned with eval_gradient equals k(X)", np.abs(G - np.transpose(G, (1, 0, 2))).max() < (1e-5 if "general" in nm or "Pairwise" in nm else 1e-12) and dev(K, KXX) < 1e-15)
# theta / bounds / hyperparameters
kc = ConstantKernel(2.0, (1e-3, 1e3)) * RBF([1.0, 3.0], (1e-2, 1e2)) + WhiteKernel(0.5, "fixed")
report("compound kernel theta = log of the non-fixed hyperparameters in k1__..., k2__ order; fixed ones excluded", np.allclose(kc.theta, np.log([2.0, 1.0, 3.0])) and kc.n_dims == 3 and [hp.name for hp in kc.hyperparameters] == ["k1__k1__constant_value", "k1__k2__length_scale", "k2__noise_level"])
report("compound kernel bounds = log-transformed (n_dims, 2) bounds, anisotropic bounds repeated per dimension", np.allclose(kc.bounds, np.log([[1e-3, 1e3], [1e-2, 1e2], [1e-2, 1e2]])) and kc.bounds.shape == (3, 2))
kc.theta = np.log([4.0, 2.0, 5.0])
report("setting theta updates the underlying parameters as exp(theta) and leaves the fixed WhiteKernel untouched", kc.k1.k1.constant_value == 4.0 and np.allclose(kc.k1.k2.length_scale, [2.0, 5.0]) and kc.k2.noise_level == 0.5)
kc2 = kc.clone_with_theta(np.log([1.0, 1.0, 1.0]))
report("clone_with_theta returns a modified clone and leaves the original unchanged", np.allclose(kc2.theta, 0) and np.allclose(kc.theta, np.log([4.0, 2.0, 5.0])))
try:
    kc.theta = np.array([0.0, 0.0]); report("setting theta with the wrong number of entries raises ValueError", False)
except ValueError: report("setting theta with the wrong number of entries raises ValueError", True)
report("kernel arithmetic: RBF() + 2 == RBF() + ConstantKernel(2) and 3 * RBF() == ConstantKernel(3) * RBF() (docstring equivalences)", (RBF() + 2) == (RBF() + ConstantKernel(2.0)) and (3 * RBF()) == (ConstantKernel(3.0) * RBF()) and (RBF() ** 2) == Exponentiation(RBF(), 2))
report("kernel repr: ConstantKernel prints as sqrt(value)**2, e.g. ConstantKernel(4.0) -> '2**2'", repr(ConstantKernel(4.0)) == "2**2")
# GPR closed form
def gpr_ref(Kxx, Kxs, Kss, y, alpha):
    Kn = Kxx + (np.diag(alpha) if np.ndim(alpha) else alpha * np.eye(len(Kxx))); L = np.linalg.cholesky(Kn); Ki = np.linalg.inv(Kn)
    mean = Kxs.T @ Ki @ y; cov = Kss - Kxs.T @ Ki @ Kxs
    lml = -0.5 * np.sum(y * (Ki @ y), axis=0) - np.log(np.diag(L)).sum() - len(y) / 2 * math.log(2 * math.pi)
    return mean, cov, np.sqrt(np.clip(np.diag(cov), 0, None)), float(np.sum(lml))
Xtr = np.sort(rs.uniform(-3, 3, 8))[:, None]; ytr = np.sin(Xtr[:, 0]) + 0.1 * rs.randn(8); Xq = np.array([[-2.5], [-0.3], [0.2], [1.7], [4.0]])
gp_kernels = [("RBF", RBF(0.8, "fixed"), lambda A, B, same: my_k("rbf", A, B, l=0.8)),
              ("Matern 1.5", Matern(0.8, "fixed", nu=1.5), lambda A, B, same: my_k("matern", A, B, l=0.8, nu=1.5)),
              ("RationalQuadratic", RationalQuadratic(0.9, 0.6, "fixed", "fixed"), lambda A, B, same: my_k("rq", A, B, l=0.9, a=0.6)),
              ("ExpSineSquared", ExpSineSquared(0.9, 1.7, "fixed", "fixed"), lambda A, B, same: my_k("ess", A, B, l=0.9, p=1.7)),
              ("DotProduct", DotProduct(0.6, "fixed"), lambda A, B, same: my_k("dot", A, B, s0=0.6)),
              ("C*RBF + WhiteKernel", ConstantKernel(1.5, "fixed") * RBF(0.8, "fixed") + WhiteKernel(0.05, "fixed"), lambda A, B, same: 1.5 * my_k("rbf", A, B, l=0.8) + my_k("white", A, B, s=0.05, same=same))]
for nm, kern, ref in gp_kernels:
    gpr = GaussianProcessRegressor(kernel=kern, alpha=1e-2, optimizer=None).fit(Xtr, ytr)
    m_ref, c_ref, s_ref, lml_ref = gpr_ref(ref(Xtr, Xtr, True), ref(Xtr, Xq, False), ref(Xq, Xq, True), ytr, 1e-2)
    m1 = gpr.predict(Xq); m2, s2 = gpr.predict(Xq, return_std=True); m3, c3 = gpr.predict(Xq, return_cov=True)
    report(f"GPR {nm} (fixed): posterior mean = K*^T (K + alpha I)^-1 y, cov = K** - K*^T (K + alpha I)^-1 K* (closed form with my kernel formulas)", dev(m1, m_ref) < 1e-9 and dev(m2, m_ref) < 1e-9 and dev(m3, m_ref) < 1e-9 and dev(c3, c_ref) < 1e-9 and dev(s2, s_ref) < 1e-9)
    report(f"GPR {nm}: return_std == sqrt(diag(return_cov)) (consistency of the two outputs)", dev(s2, np.sqrt(np.clip(np.diag(c3), 0, None))) < 1e-10)
    report(f"GPR {nm}: log_marginal_likelihood_value_ = -1/2 y^T K^-1 y - 1/2 log|K| - n/2 log 2pi and equals log_marginal_likelihood(kernel_.theta)", close(gpr.log_marginal_likelihood_value_, lml_ref, 1e-10) and close(gpr.log_marginal_likelihood(gpr.kernel_.theta), lml_ref, 1e-10))
    report(f"GPR {nm}: alpha_ = (K + alpha I)^-1 y and L_ is the lower Cholesky factor of K + alpha I", dev(gpr.alpha_, np.linalg.solve(ref(Xtr, Xtr, True) + 1e-2 * np.eye(8), ytr)) < 1e-9 and dev(gpr.L_ @ gpr.L_.T, ref(Xtr, Xtr, True) + 1e-2 * np.eye(8)) < 1e-12 and np.allclose(np.triu(gpr.L_, 1), 0))
gw = [k for k in gp_kernels if "White" in k[0]][0]
gprw = GaussianProcessRegressor(kernel=gw[1], alpha=1e-2, optimizer=None).fit(Xtr, ytr); _, sw = gprw.predict(Xq, return_std=True); _, cw = gprw.predict(Xq, return_cov=True)
print(f"   GPR with a WhiteKernel in the kernel: predictive variance at a query point includes noise_level (0.05): var {cw[0, 0]:.6f} vs without-noise {1.5 * my_k('rbf', Xq[:1], Xq[:1], l=0.8)[0, 0] - 1.5 ** 2 * (my_k('rbf', Xtr, Xq[:1], l=0.8).T @ np.linalg.solve(gw[2](Xtr, Xtr, True) + 1e-2 * np.eye(8), my_k('rbf', Xtr, Xq[:1], l=0.8)))[0, 0]:.6f}")
al = rs.uniform(0.01, 0.1, 8); gpa = GaussianProcessRegressor(kernel=RBF(0.8, "fixed"), alpha=al, optimizer=None).fit(Xtr, ytr); m_ref, c_ref, s_ref, lml_ref = gpr_ref(my_k("rbf", Xtr, Xtr, l=0.8), my_k("rbf", Xtr, Xq, l=0.8), my_k("rbf", Xq, Xq, l=0.8), ytr, al)
report("GPR alpha array (per-sample noise): K + diag(alpha) in mean, cov and LML", dev(gpa.predict(Xq), m_ref) < 1e-9 and dev(gpa.predict(Xq, return_cov=True)[1], c_ref) < 1e-9 and close(gpa.log_marginal_likelihood_value_, lml_ref, 1e-10))
# LML gradient vs finite differences of the closed form (theta = log params)
kern_g = ConstantKernel(1.5, (1e-3, 1e3)) * RBF(0.8, (1e-2, 1e2)) + WhiteKernel(0.05, (1e-5, 1.0))
def lml_theta(theta, y, alpha=1e-2):
    c, l, s = np.exp(theta); Kxx = c * my_k("rbf", Xtr, Xtr, l=l) + s * np.eye(8); return gpr_ref(Kxx, Kxx[:, :1], Kxx[:1, :1], y, alpha)[3]
def fd_grad(fun, theta, h=1e-5): return np.array([(fun(theta + h * e) - fun(theta - h * e)) / (2 * h) for e in np.eye(len(theta))])
Y2 = np.column_stack([ytr, np.cos(Xtr[:, 0]) - 0.2 * rs.randn(8)])
for yy, nm in ((ytr, "single output"), (Y2, "two outputs (LML summed over outputs)")):
    gpg = GaussianProcessRegressor(kernel=kern_g, alpha=1e-2, optimizer=None).fit(Xtr, yy); th = gpg.kernel_.theta
    lml, grad = gpg.log_marginal_likelihood(th, eval_gradient=True); gfd = fd_grad(lambda t: lml_theta(t, yy), th)
    print(f"   GPR LML gradient ({nm}) at theta={th.round(4).tolist()}: analytic {grad.round(6).tolist()} vs finite differences of my closed form {gfd.round(6).tolist()}")
    report(f"GPR log_marginal_likelihood(theta, eval_gradient=True) ({nm}): value = closed form and gradient = central finite differences w.r.t. log-hyperparameters (sign: gradient of the LML itself)", close(lml, lml_theta(th, yy), 1e-10) and np.abs(grad - gfd).max() < 1e-6 * max(1, np.abs(gfd).max()))
    th2 = th + np.array([0.3, -0.2, 0.5]); lml2, grad2 = gpg.log_marginal_likelihood(th2, eval_gradient=True)
    report(f"GPR log_marginal_likelihood at another theta ({nm}): clone_kernel=True leaves kernel_.theta unchanged; value and gradient match", np.allclose(gpg.kernel_.theta, th) and close(lml2, lml_theta(th2, yy), 1e-10) and np.abs(grad2 - fd_grad(lambda t: lml_theta(t, yy), th2)).max() < 1e-6 * max(1, np.abs(grad2).max()))
report("GPR log_marginal_likelihood(theta=None) returns log_marginal_likelihood_value_", close(gpg.log_marginal_likelihood(), gpg.log_marginal_likelihood_value_))
try:
    gpg.log_marginal_likelihood(None, eval_gradient=True); report("GPR log_marginal_likelihood(None, eval_gradient=True) raises ValueError", False)
except ValueError: report("GPR log_marginal_likelihood(None, eval_gradient=True) raises ValueError", True)
# normalize_y
y_big = 5 + 3 * ytr; ym_, ys_ = y_big.mean(), y_big.std(); ysn = (y_big - ym_) / ys_
gpn = GaussianProcessRegressor(kernel=ConstantKernel(1.5, "fixed") * RBF(0.8, "fixed"), alpha=1e-2, optimizer=None, normalize_y=True).fit(Xtr, y_big)
m_ref, c_ref, s_ref, lml_ref = gpr_ref(1.5 * my_k("rbf", Xtr, Xtr, l=0.8), 1.5 * my_k("rbf", Xtr, Xq, l=0.8), 1.5 * my_k("rbf", Xq, Xq, l=0.8), ysn, 1e-2)
mn, sn = gpn.predict(Xq, return_std=True); _, cn = gpn.predict(Xq, return_cov=True)
report("GPR normalize_y=True: targets standardised with mean and std (ddof=0), predictions un-normalised: mean = std*m + mean, std = std*s, cov = std^2 * c", dev(mn, ys_ * m_ref + ym_) < 1e-9 and dev(sn, ys_ * s_ref) < 1e-9 and dev(cn, ys_ ** 2 * c_ref) < 1e-9)
lml_std = lml_ref; lml_jac = lml_ref - 8 * math.log(ys_)
print(f"   GPR normalize_y=True: log_marginal_likelihood_value_ {gpn.log_marginal_likelihood_value_:.6f}; closed form on standardised targets {lml_std:.6f}; with the Jacobian term -n log(std) of the change of variables {lml_jac:.6f}")
report("GPR normalize_y=True: log_marginal_likelihood_value_ = LML of the standardised targets (no -n log std Jacobian term; informational)", close(gpn.log_marginal_likelihood_value_, lml_std, 1e-10))
mf, sf_ = gpn.predict(np.array([[60.0]]), return_std=True)
report("GPR normalize_y=True far from the data: mean -> training mean and std -> std_y * sqrt(constant_value) (user guide: prior mean is the training data's mean)", close(mf[0], ym_, 1e-8) and close(sf_[0], ys_ * math.sqrt(1.5), 1e-8))
mf0, sf0 = GaussianProcessRegressor(kernel=ConstantKernel(1.5, "fixed") * RBF(0.8, "fixed"), alpha=1e-2, optimizer=None).fit(Xtr, y_big).predict(np.array([[60.0]]), return_std=True)
report("GPR normalize_y=False far from the data: mean -> 0 ('prior mean is assumed to be constant and zero')", abs(mf0[0]) < 1e-8 and close(sf0[0], math.sqrt(1.5), 1e-8))
Y2b = np.column_stack([y_big, -2 * ytr + 1]); gpn2 = GaussianProcessRegressor(kernel=ConstantKernel(1.5, "fixed") * RBF(0.8, "fixed"), alpha=1e-2, optimizer=None, normalize_y=True).fit(Xtr, Y2b)
mm, ss = gpn2.predict(Xq, return_std=True); _, cc = gpn2.predict(Xq, return_cov=True)
okm = True
for j in range(2):
    mj, sj = Y2b[:, j].mean(), Y2b[:, j].std(); mr, cr, sr, _ = gpr_ref(1.5 * my_k("rbf", Xtr, Xtr, l=0.8), 1.5 * my_k("rbf", Xtr, Xq, l=0.8), 1.5 * my_k("rbf", Xq, Xq, l=0.8), (Y2b[:, j] - mj) / sj, 1e-2)
    okm &= dev(mm[:, j], sj * mr + mj) < 1e-9 and dev(ss[:, j], sj * sr) < 1e-9 and dev(cc[:, :, j], sj ** 2 * cr) < 1e-9
report("GPR multi-output normalize_y=True: per-target standardisation; return_std shape (n, n_targets), return_cov shape (n, n, n_targets)", okm and mm.shape == (5, 2) and ss.shape == (5, 2) and cc.shape == (5, 5, 2))
# sample_y
gps = GaussianProcessRegressor(kernel=ConstantKernel(1.5, "fixed") * RBF(0.8, "fixed"), alpha=1e-2, optimizer=None).fit(Xtr, ytr)
Xq3 = Xq[:3]; S = gps.sample_y(Xq3, n_samples=40000, random_state=0); mq, cq = gps.predict(Xq3, return_cov=True)
print(f"   sample_y(40000 draws) at 3 points: sample mean {S.mean(1).round(4).tolist()} vs mean {mq.round(4).tolist()}; sample cov rel Frobenius dev {np.linalg.norm(np.cov(S) - cq) / np.linalg.norm(cq):.3f}")
report("GPR sample_y: shape (n_samples_X, n_samples); sample mean within 4 sigma/sqrt(n) and sample covariance within 5% (Frobenius) of predict(return_cov)", S.shape == (3, 40000) and np.all(np.abs(S.mean(1) - mq) < 4 * np.sqrt(np.diag(cq)) / 200) and np.linalg.norm(np.cov(S) - cq) / np.linalg.norm(cq) < 0.05)
S2 = gpn2.sample_y(Xq3, n_samples=5, random_state=0)
report("GPR sample_y multi-target: shape (n_samples_X, n_targets, n_samples)", S2.shape == (3, 2, 5))
# prior (unfitted)
gpp = GaussianProcessRegressor(kernel=ConstantKernel(2.0) * RBF(0.5)); mp_, cp_ = gpp.predict(Xq, return_cov=True); _, sp_ = gpp.predict(Xq, return_std=True)
report("GPR unfitted predict = GP prior: mean 0, cov = kernel(X), std = sqrt(diag)", np.all(mp_ == 0) and dev(cp_, 2.0 * my_k("rbf", Xq, Xq, l=0.5)) < 1e-12 and dev(sp_, np.sqrt(2.0) * np.ones(5)) < 1e-12)
try:
    gps.predict(Xq, return_std=True, return_cov=True); report("GPR predict(return_std=True, return_cov=True) raises RuntimeError ('At most one of the two can be requested')", False)
except RuntimeError: report("GPR predict(return_std=True, return_cov=True) raises RuntimeError ('At most one of the two can be requested')", True)
gpd = GaussianProcessRegressor(); _, sd = gpd.predict(Xq, return_std=True)
report("GPR default kernel (None) prior = ConstantKernel(1) * RBF(1): prior std 1", dev(sd, np.ones(5)) < 1e-12)
# optimisation: LML gradient vanishes at the fitted theta (or theta sits on a bound)
Xo = np.sort(rs.uniform(-4, 4, 30))[:, None]; yo = np.sin(1.3 * Xo[:, 0]) + 0.2 * rs.randn(30)
gpo = GaussianProcessRegressor(kernel=ConstantKernel(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2)) + WhiteKernel(0.1, (1e-5, 10.0)), random_state=0).fit(Xo, yo)
tho = gpo.kernel_.theta; bo = gpo.kernel_.bounds
def lml_theta_o(theta):
    c, l, s = np.exp(theta); Kxx = c * my_k("rbf", Xo, Xo, l=l) + s * np.eye(30) + 1e-10 * np.eye(30); return gpr_ref(Kxx, Kxx[:, :1], Kxx[:1, :1], yo, 0.0)[3]
go = fd_grad(lml_theta_o, tho); at_bound = np.isclose(tho, bo[:, 0]) | np.isclose(tho, bo[:, 1])
print(f"   GPR fitted kernel_ = {gpo.kernel_}; LML {gpo.log_marginal_likelihood_value_:.6f}; FD gradient of my closed form at theta_opt {go.round(6).tolist()}; at bound {at_bound.tolist()}")
report("GPR fit maximises the LML: finite-difference gradient of the closed-form LML vanishes at kernel_.theta (|g| < 1e-3) for every interior dimension", np.all((np.abs(go) < 1e-3) | at_bound))
report("GPR log_marginal_likelihood_value_ after fit = closed-form LML at kernel_.theta", close(gpo.log_marginal_likelihood_value_, lml_theta_o(tho), 1e-8))
# restarts: initial thetas must be log-uniform within the bounds
rec = []
def rec_opt(obj_func, initial_theta, bounds):
    rec.append(np.array(initial_theta, float))
    try: val = obj_func(initial_theta, eval_gradient=False)
    except Exception as e: val = np.inf; rec_err.append(type(e).__name__)
    return initial_theta, val
rec_err = []
kr_ = ConstantKernel(1.0, (1e-2, 1e2)) * RBF(1.0, (1e-2, 1e2)); GaussianProcessRegressor(kernel=kr_, optimizer=rec_opt, n_restarts_optimizer=300, random_state=0).fit(Xo, yo)
inits = np.array(rec[1:]); bnd = kr_.bounds; mid = bnd.mean(1)
print(f"   GPR n_restarts_optimizer=300 initial thetas: range [{inits.min(0).round(2).tolist()}, {inits.max(0).round(2).tolist()}] vs log-bounds {bnd.round(2).tolist()}; fraction below midpoint {(inits < mid).mean(0).round(3).tolist()}")
report("GPR restarts: initial thetas are within the (log) bounds and roughly uniform there ('sampled log-uniform randomly from the space of allowed theta-values')", np.all(inits >= bnd[:, 0]) and np.all(inits <= bnd[:, 1]) and np.all(np.abs((inits < mid).mean(0) - 0.5) < 0.12))
rec = []; ycl = (Xo[:, 0] > 0).astype(int)
GaussianProcessClassifier(kernel=ConstantKernel(1.0, (1e-2, 1e2)) * RBF(1.0, (1e-2, 1e2)), optimizer=rec_opt, n_restarts_optimizer=300, random_state=0).fit(Xo, ycl)
inits = np.array(rec[1:])
print(f"   GPC restarts: {len(rec_err)} of 300 initial thetas made the objective raise ({set(rec_err)}) when evaluated by a callable optimizer")
print(f"   GPC n_restarts_optimizer=300 initial thetas: range [{inits.min(0).round(2).tolist()}, {inits.max(0).round(2).tolist()}] vs log-bounds {bnd.round(2).tolist()}; fraction below midpoint {(inits < mid).mean(0).round(3).tolist()}; fraction outside bounds {((inits < bnd[:, 0]) | (inits > bnd[:, 1])).mean(0).round(3).tolist()}")
report("GPC restarts: initial thetas are within the (log) bounds and roughly uniform there ('sampled log-uniform randomly from the space of allowed theta-values')", np.all(inits >= bnd[:, 0]) and np.all(inits <= bnd[:, 1]) and np.all(np.abs((inits < mid).mean(0) - 0.5) < 0.12))
# GPC Laplace approximation reference
def laplace_ref(K, y01, iters=500):
    n = len(y01); f = np.zeros(n)
    for _ in range(iters):
        pi = 1 / (1 + np.exp(-f)); W = pi * (1 - pi); b = W * f + (y01 - pi); f_new = K @ np.linalg.solve(np.eye(n) + W[:, None] * K, b)
        if np.abs(f_new - f).max() < 1e-14: f = f_new; break
        f = f_new
    pi = 1 / (1 + np.exp(-f)); W = pi * (1 - pi); sW = np.sqrt(W); B = np.eye(n) + (sW[:, None] * K) * sW[None, :]
    a = np.linalg.solve(K, f); lml = -0.5 * a @ f - np.sum(np.log1p(np.exp(-(2 * y01 - 1) * f))) - 0.5 * np.linalg.slogdet(B)[1]
    return f, pi, W, lml
def latent_ref(K, Kstar, kss, y01, f, pi, W):
    n = len(y01); mean = Kstar.T @ (y01 - pi); Binv = np.linalg.inv(np.eye(n) + (np.sqrt(W)[:, None] * K) * np.sqrt(W)[None, :])
    var = kss - np.einsum("ij,ji->i", Kstar.T * np.sqrt(W), Binv @ (np.sqrt(W)[:, None] * Kstar)); return mean, var
def proba_ref(mean, var): return np.array([float(mp.quad(lambda z: 1 / (1 + mp.exp(-z)) * mp.exp(-(z - m) ** 2 / (2 * v)) / mp.sqrt(2 * mp.pi * v), [m - 12 * mp.sqrt(v), m + 12 * mp.sqrt(v)])) for m, v in zip(mean, var)])
Xc_ = np.linspace(-3, 3, 14)[:, None]; yc_ = (Xc_[:, 0] + 0.6 * rs.randn(14) > 0).astype(int)
kc_ = ConstantKernel(2.0, "fixed") * RBF(1.0, "fixed"); Kc = 2.0 * my_k("rbf", Xc_, Xc_, l=1.0)
gpc = GaussianProcessClassifier(kernel=kc_, optimizer=None).fit(Xc_, yc_); be = gpc.base_estimator_
f_, pi_, W_, lml_ = laplace_ref(Kc, yc_)
print(f"   GPC Laplace: my posterior mode f_hat {f_[:4].round(5).tolist()}..., library pi_ {be.pi_[:4].round(5).tolist()}... vs sigmoid(f_hat) {pi_[:4].round(5).tolist()}..., LML {gpc.log_marginal_likelihood_value_:.8f} vs reference {lml_:.8f}")
report("GPC binary: pi_ = sigmoid(posterior mode) and W_sr_ = sqrt(pi (1 - pi)) of the Newton mode of the Laplace approximation (plain-numpy reference)", dev(be.pi_, pi_) < 1e-8 and dev(be.W_sr_, np.sqrt(W_)) < 1e-8)
report("GPC binary: log_marginal_likelihood_value_ = -1/2 f^T K^-1 f + sum log sigmoid(y f) - 1/2 log|I + W^1/2 K W^1/2| (RW2006 eq. 3.32)", close(gpc.log_marginal_likelihood_value_, lml_, 1e-8))
Xq_ = np.array([[-2.5], [-0.3], [0.2], [1.7], [4.0]]); Ks = 2.0 * my_k("rbf", Xc_, Xq_, l=1.0); kss = np.full(5, 2.0)
lm_ref, lv_ref = latent_ref(Kc, Ks, kss, yc_, f_, pi_, W_)
if hasattr(gpc, "latent_mean_and_variance"):
    lm, lv = gpc.latent_mean_and_variance(Xq_)
    report("GPC latent_mean_and_variance = k*^T (y - pi) and k** - k*^T (K + W^-1)^-1 k* (RW2006 eqs 3.21 / 3.24)", dev(lm, lm_ref) < 1e-8 and dev(lv, lv_ref) < 1e-8)
else: print("   latent_mean_and_variance not available in this version (added later); skipped")
pr = gpc.predict_proba(Xq_); pr_ref = proba_ref(lm_ref, lv_ref)
print(f"   GPC predict_proba(class 1) {pr[:, 1].round(5).tolist()} vs exact Gaussian integral of the sigmoid (mpmath quad) {pr_ref.round(5).tolist()}; max |dev| {np.abs(pr[:, 1] - pr_ref).max():.2e}")
report("GPC predict_proba = int sigmoid(z) N(z | latent mean, var) dz within 5e-3 (Williams & Barber erf approximation) and rows sum to 1", np.abs(pr[:, 1] - pr_ref).max() < 5e-3 and np.allclose(pr.sum(1), 1))
report("GPC predict = classes_[1] iff the latent mean is positive (MAP decision, RW 3.4.2) and agrees with predict_proba > 0.5 where |mean| > 0.05", np.array_equal(gpc.predict(Xq_), np.where(lm_ref > 0, 1, 0)) and np.all((pr[:, 1] > 0.5) == (lm_ref > 0) | (np.abs(lm_ref) < 0.05)))
report("GPC classes_ sorted and n_classes_ = 2; default kernel is 1.0 * RBF(1.0) with fixed bounds when kernel=None", np.array_equal(gpc.classes_, [0, 1]) and gpc.n_classes_ == 2 and GaussianProcessClassifier().fit(Xc_, yc_).kernel_ == ConstantKernel(1.0, "fixed") * RBF(1.0, "fixed"))
kg = ConstantKernel(2.0, (1e-2, 1e2)) * RBF(1.0, (1e-2, 1e2)); gpc2 = GaussianProcessClassifier(kernel=kg, optimizer=None).fit(Xc_, yc_)
def lml_c(theta): c, l = np.exp(theta); return laplace_ref(c * my_k("rbf", Xc_, Xc_, l=l), yc_)[3]
for th in (kg.theta, kg.theta + np.array([-0.4, 0.3])):
    lmlv, gr = gpc2.log_marginal_likelihood(th, eval_gradient=True); gfd = fd_grad(lml_c, th)
    print(f"   GPC LML gradient at theta {th.round(3).tolist()}: analytic {gr.round(6).tolist()} vs FD of my Laplace LML {gfd.round(6).tolist()}")
    report(f"GPC log_marginal_likelihood(theta={th.round(3).tolist()}, eval_gradient=True): value = Laplace LML and gradient = finite differences (RW Algorithm 5.1, implicit dependence through the mode included)", close(lmlv, lml_c(th), 1e-8) and np.abs(gr - gfd).max() < 1e-5 * max(1, np.abs(gfd).max()))
# multi-class one_vs_rest
y3c = np.digitize(Xc_[:, 0] + 0.5 * rs.randn(14), [-1.0, 1.0]); gpc3 = GaussianProcessClassifier(kernel=kc_, optimizer=None).fit(Xc_, y3c)
P3 = gpc3.predict_proba(Xq_); refs = []
for k in range(3):
    fk, pik, Wk, lmlk = laplace_ref(Kc, (y3c == k).astype(int)); lmk, lvk = latent_ref(Kc, Ks, kss, (y3c == k).astype(int), fk, pik, Wk); refs.append((proba_ref(lmk, lvk), lmlk))
Pref = np.column_stack([r[0] for r in refs]); Pref = Pref / Pref.sum(1, keepdims=True)
Pbin = np.column_stack([GaussianProcessClassifier(kernel=kc_, optimizer=None).fit(Xc_, (y3c == k).astype(int)).predict_proba(Xq_)[:, 1] for k in range(3)]); Pbin = Pbin / Pbin.sum(1, keepdims=True)
print(f"   GPC one_vs_rest 3 classes: predict_proba row 0 {P3[0].round(5).tolist()} vs normalised binary GPCs {Pbin[0].round(5).tolist()} vs normalised exact integrals {Pref[0].round(5).tolist()}")
report("GPC multi_class='one_vs_rest': predict_proba = row-normalised probabilities of the per-class binary Laplace GPCs (documented OvR combination)", dev(P3, Pbin) < 1e-10)
report("GPC one_vs_rest: probabilities within 5e-3 of normalised exact sigmoid-Gaussian integrals of my Laplace reference", np.abs(P3 - Pref).max() < 5e-3)
report("GPC one_vs_rest: log_marginal_likelihood_value_ = mean of the binary LMLs; kernel_ is a CompoundKernel of 3 kernels; predict = argmax proba", close(gpc3.log_marginal_likelihood_value_, np.mean([r[1] for r in refs]), 1e-8) and isinstance(gpc3.kernel_, CompoundKernel) and len(gpc3.kernel_.kernels) == 3 and np.array_equal(gpc3.predict(Xq_), gpc3.classes_[P3.argmax(1)]))
gpc_ovo = GaussianProcessClassifier(kernel=kc_, optimizer=None, multi_class="one_vs_one").fit(Xc_, y3c)
try:
    gpc_ovo.predict_proba(Xq_); report("GPC multi_class='one_vs_one': predict_proba raises ValueError ('does not support predicting probability estimates')", False)
except ValueError: report("GPC multi_class='one_vs_one': predict_proba raises ValueError ('does not support predicting probability estimates')", True)
report("GPC multi_class='one_vs_one': predict returns class labels from classes_", set(gpc_ovo.predict(Xq_)).issubset(set(gpc3.classes_)))
try:
    GaussianProcessClassifier(kernel=kc_, optimizer=None).fit(Xc_, np.zeros(14, int)); report("GPC with a single class raises ValueError", False)
except ValueError: report("GPC with a single class raises ValueError", True)
g32 = GaussianProcessRegressor(kernel=RBF(0.8, "fixed"), alpha=1e-2, optimizer=None).fit(Xtr.astype(np.float32), ytr.astype(np.float32))
print(f"   GPR float32 input: prediction dtype {g32.predict(Xq.astype(np.float32)).dtype}, dev from float64 {dev(g32.predict(Xq.astype(np.float32)), GaussianProcessRegressor(kernel=RBF(0.8, 'fixed'), alpha=1e-2, optimizer=None).fit(Xtr, ytr).predict(Xq)):.1e}")
report("GPR float32 input: predictions within 1e-4 of the float64 fit", dev(g32.predict(Xq.astype(np.float32)), GaussianProcessRegressor(kernel=RBF(0.8, "fixed"), alpha=1e-2, optimizer=None).fit(Xtr, ytr).predict(Xq)) < 1e-4)
goff = GaussianProcessRegressor(kernel=RBF(0.8, "fixed"), alpha=1e-2, optimizer=None).fit(Xtr + 1e4, ytr)
print(f"   GPR RBF with 1e4 offset on X: prediction dev from the offset-free fit {dev(goff.predict(Xq + 1e4), GaussianProcessRegressor(kernel=RBF(0.8, 'fixed'), alpha=1e-2, optimizer=None).fit(Xtr, ytr).predict(Xq)):.1e} (pdist/cdist compute differences directly)")
report("GPR RBF with 1e4 offset on X: predictions within 1e-6 of the offset-free fit (stationary kernel evaluated on differences)", dev(goff.predict(Xq + 1e4), GaussianProcessRegressor(kernel=RBF(0.8, "fixed"), alpha=1e-2, optimizer=None).fit(Xtr, ytr).predict(Xq)) < 1e-6)
print("== done")
