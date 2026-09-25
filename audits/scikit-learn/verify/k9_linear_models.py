#!/usr/bin/env python
"""Linear models beyond the k4 basics, every check against an independent truth
(plain-numpy reference implementations written here, closed forms, KKT conditions
of the DOCUMENTED objectives, documented invariants):
Lasso / ElasticNet (KKT, centring, positive, warm_start, precompute, sample_weight,
alpha=0, dual gap, sparse X), lasso_path / enet_path grid, Lars / LassoLars /
lars_path (vs a plain LARS written here), LarsCV / LassoLarsCV / LassoLarsIC,
OrthogonalMatchingPursuit, BayesianRidge, ARDRegression, HuberRegressor,
QuantileRegressor, Poisson / Gamma / Tweedie regressors, SGDRegressor / SGDClassifier,
PassiveAggressive, Perceptron, RANSAC, TheilSen, RidgeCV (LOO), LassoCV / ElasticNetCV,
MultiTaskLasso / MultiTaskElasticNet, Ridge solvers, LogisticRegression penalties and
solvers, LogisticRegressionCV, and sample_weight == duplicated rows per estimator."""
import sys, math, warnings, itertools, inspect
sys.path.insert(0, ".")
from _synth import *
from sklearn.linear_model import (Lasso, ElasticNet, lasso_path, enet_path, Lars, LassoLars, lars_path,
    LarsCV, LassoLarsCV, LassoLarsIC, OrthogonalMatchingPursuit, BayesianRidge, ARDRegression, HuberRegressor,
    QuantileRegressor, PoissonRegressor, GammaRegressor, TweedieRegressor, SGDRegressor, SGDClassifier,
    RANSACRegressor, TheilSenRegressor, RidgeCV, LassoCV, ElasticNetCV, MultiTaskLasso, MultiTaskElasticNet,
    PassiveAggressiveClassifier, PassiveAggressiveRegressor, Perceptron, Ridge, LogisticRegression,
    LogisticRegressionCV, LinearRegression)
from sklearn.model_selection import KFold, StratifiedKFold
from scipy import sparse, optimize
banner(); warnings.filterwarnings("ignore")
VER = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
rs = np.random.RandomState(0)
print(f"   sklearn version tuple {VER}; scipy {__import__('scipy').__version__}")

# ---------------------------------------------------------------- version shims
def LR(penalty="l2", l1_ratio=None, **kw):
    """LogisticRegression with the penalty expressed the way this version accepts it."""
    if VER >= (1, 8):
        if penalty == "l2": return LogisticRegression(l1_ratio=0.0, **kw)
        if penalty == "l1": return LogisticRegression(l1_ratio=1.0, **kw)
        if penalty == "elasticnet": return LogisticRegression(l1_ratio=l1_ratio, **kw)
        kw.pop("C", None); return LogisticRegression(C=np.inf, **kw)
    if penalty is None:
        return LogisticRegression(penalty=None if VER >= (1, 2) else "none", **kw)
    return LogisticRegression(penalty=penalty, l1_ratio=l1_ratio, **kw)

def ridgecv(store=False, **kw):
    if VER >= (1, 5): return RidgeCV(store_cv_results=store, **kw)
    return RidgeCV(store_cv_values=store, **kw)
def cvres(m): return getattr(m, "cv_results_" if VER >= (1, 5) else "cv_values_")
def QR(**kw): return QuantileRegressor(solver="highs", **kw)
LARS_KW = {"normalize": False} if VER < (1, 2) else {}   # normalize defaulted to True for the Lars family / OMP before 1.2
def BR(**kw):
    if VER < (1, 3) and "max_iter" in kw: kw["n_iter"] = kw.pop("max_iter")
    return BayesianRidge(**kw)
def ARD(**kw):
    if VER < (1, 3) and "max_iter" in kw: kw["n_iter"] = kw.pop("max_iter")
    return ARDRegression(**kw)
def nalph(k):
    """LassoCV/ElasticNetCV grid size: alphas=int from 1.7, n_alphas before."""
    return {"alphas": k} if VER >= (1, 7) else {"n_alphas": k}

# ---------------------------------------------------------------- references
def centre(X, y, sw=None):
    if sw is None: sw = np.ones(len(y))
    xm = sw @ X / sw.sum(); ym = sw @ y / sw.sum()
    return X - xm, y - ym, xm, ym

def ols(X, y):
    A = np.hstack([np.ones((len(y), 1)), X]); b = np.linalg.lstsq(A, y, rcond=None)[0]; return b[1:], b[0]

def enet_cd(X, y, alpha, l1_ratio=1.0, positive=False, fit_intercept=True, tol=1e-15, max_iter=200000, sw=None):
    """Plain coordinate descent for 1/(2n)||y-Xw-b||^2 + a*l1*||w||_1 + a(1-l1)/2||w||^2 (n = sum of weights)."""
    X = np.asarray(X, float); y = np.asarray(y, float); n, p = X.shape
    if sw is None: sw = np.ones(n)
    if fit_intercept: Xc, yc, xm, ym = centre(X, y, sw)
    else: Xc, yc, xm, ym = X, y, np.zeros(p), 0.0
    S = sw.sum(); w = np.zeros(p); r = yc.copy(); nrm = (sw[:, None] * Xc * Xc).sum(0) / S
    l1 = alpha * l1_ratio; l2 = alpha * (1 - l1_ratio)
    for it in range(max_iter):
        dmax = 0.0
        for j in range(p):
            if nrm[j] == 0: continue
            wj = w[j]; z = (sw * Xc[:, j]) @ r / S + nrm[j] * wj
            if positive: new = max(0.0, z - l1) / (nrm[j] + l2)
            else: new = np.sign(z) * max(0.0, abs(z) - l1) / (nrm[j] + l2)
            if new != wj:
                r -= Xc[:, j] * (new - wj); w[j] = new; dmax = max(dmax, abs(new - wj))
        if dmax <= tol: break
    return w, (ym - xm @ w if fit_intercept else 0.0)

def kkt_enet(Xc, yc, w, alpha, l1_ratio=1.0, positive=False, sw=None):
    """Max violation of the KKT conditions of the documented objective on centred data."""
    n = len(yc)
    if sw is None: g = -Xc.T @ (yc - Xc @ w) / n
    else: g = -(Xc * sw[:, None]).T @ (yc - Xc @ w) / sw.sum()
    g = g + alpha * (1 - l1_ratio) * w; l1 = alpha * l1_ratio; v = 0.0
    for j in range(len(w)):
        if positive:
            if w[j] > 0: v = max(v, abs(g[j] + l1))
            elif w[j] == 0: v = max(v, max(0.0, -(g[j] + l1)))
            else: v = max(v, abs(w[j]))
        else:
            if w[j] != 0: v = max(v, abs(g[j] + l1 * np.sign(w[j])))
            else: v = max(v, max(0.0, abs(g[j]) - l1))
    return v

def lars_plain(X, y, method="lar", max_steps=None):
    """Least angle regression (Efron et al. 2004) in plain numpy on centred X, y.
    Returns alphas = max|correlation|/n at each node and coefficients at the nodes."""
    X = np.asarray(X, float); y = np.asarray(y, float); n, p = X.shape
    beta = np.zeros(p); mu = np.zeros(n); active = []; signs = {}; order = []
    alphas = []; coefs = [beta.copy()]
    c = X.T @ (y - mu); C = np.max(np.abs(c)); alphas.append(C / n)
    steps = 0; max_steps = max_steps or 10 * p; drop = None
    while steps < max_steps and C > 1e-12:
        c = X.T @ (y - mu); C = np.max(np.abs(c))
        if drop is None:
            j = int(np.argmax(np.abs(c) * np.array([k not in active for k in range(p)])))
            active.append(j); signs[j] = np.sign(c[j]); order.append(j)
        drop = None
        s = np.array([signs[k] for k in active]); XA = X[:, active] * s
        G = XA.T @ XA; Ginv1 = np.linalg.solve(G, np.ones(len(active)))
        AA = 1.0 / math.sqrt(np.ones(len(active)) @ Ginv1); w = AA * Ginv1; u = XA @ w; a = X.T @ u
        if len(active) == p: gamma = C / AA
        else:
            cand = []
            for k in range(p):
                if k in active: continue
                for val in ((C - c[k]) / (AA - a[k]), (C + c[k]) / (AA + a[k])):
                    if val > 1e-12: cand.append(val)
            gamma = min(cand)
        if method == "lasso":
            d = s * w; gt = [(-beta[k] / d[i], k) for i, k in enumerate(active) if d[i] != 0 and -beta[k] / d[i] > 1e-12]
            if gt:
                g_t, k_t = min(gt)
                if g_t < gamma: gamma = g_t; drop = k_t
        for i, k in enumerate(active): beta[k] += gamma * s[i] * w[i]
        mu = mu + gamma * u
        if drop is not None:
            beta[drop] = 0.0; active.remove(drop); del signs[drop]
        c = X.T @ (y - mu); C = np.max(np.abs(c)) if len(active) < p or drop is not None else 0.0
        alphas.append(max(C, 0.0) / n); coefs.append(beta.copy()); steps += 1
        if len(active) == p and drop is None: break
    lars_plain.order = order
    return np.array(alphas), np.array(coefs).T

def dual_gap_lasso(Xc, yc, w, alpha, l1_ratio=1.0):
    """The duality gap of 1/(2n)||y-Xw||^2 + a l1 ||w||_1 + a(1-l1)/2 ||w||^2 with the dual point of
    formulation A (main) and of the pre-1.7 code path; both are valid gaps, returned as a pair."""
    n = len(yc); R = yc - Xc @ w; A = n * alpha * l1_ratio; B = n * alpha * (1 - l1_ratio)
    XtA = Xc.T @ R - B * w; dn = np.max(np.abs(XtA)); R2 = R @ R; w2 = w @ w; l1n = np.abs(w).sum(); Ry = R @ yc
    scale = A / dn if dn > A else 1.0
    primal = 0.5 * (R2 + B * w2) + A * l1n
    gapA = primal - (-0.5 * scale ** 2 * (R2 + B * w2) + scale * Ry)
    gap_old = (0.5 * (R2 + R2 * scale ** 2) if dn > A else R2) + A * l1n - scale * Ry + 0.5 * B * (1 + scale ** 2) * w2
    return gapA / n, gap_old / n

# ================================================================ Lasso / ElasticNet
n, p = 40, 6; X = rs.randn(n, p) * np.array([1, 2, 0.5, 1, 1, 3]) + rs.randn(p); w_true = np.array([2.0, -1.0, 0.0, 0.0, 0.5, 0.0])
y = X @ w_true + 3.0 + 0.5 * rs.randn(n)
Xc, yc, xm, ym = centre(X, y)
for alpha, l1r in [(0.1, 1.0), (0.05, 0.5), (0.2, 0.1), (0.3, 1.0)]:
    m = ElasticNet(alpha=alpha, l1_ratio=l1r, tol=1e-12, max_iter=100000).fit(X, y)
    v = kkt_enet(Xc, yc, m.coef_, alpha, l1r)
    wr, br = enet_cd(X, y, alpha, l1r)
    report(f"ElasticNet(alpha={alpha}, l1_ratio={l1r}, tol=1e-12): KKT of 1/(2n)||y-Xw||^2 + a*l1*||w||_1 + a(1-l1)/2||w||^2 hold (max violation < 1e-9) and coef = plain-numpy CD",
           v < 1e-9 and np.allclose(m.coef_, wr, atol=1e-8) and close(m.intercept_, br, 1e-9, 1e-9), f"(violation {v:.2e}, nnz {np.count_nonzero(m.coef_)})")
m = Lasso(alpha=0.1, tol=1e-12, max_iter=100000).fit(X, y)
report("Lasso(alpha): intercept = mean(y) - mean(X) @ coef (fit_intercept centring, intercept unpenalised)", close(m.intercept_, ym - xm @ m.coef_, 1e-12, 1e-12))
gA, gO = dual_gap_lasso(Xc, yc, m.coef_, 0.1)
report("Lasso dual_gap_ = duality gap of the documented objective divided by n_samples (my primal - dual at the same w)", close(m.dual_gap_, gA, 1e-6, 1e-12) or close(m.dual_gap_, gO, 1e-6, 1e-12), f"(dual_gap_ {m.dual_gap_:.3e}, mine {gA:.3e})")
report("Lasso dual_gap_ >= 0 and <= tol * ||y_centred||^2 / n at convergence (documented stopping rule)", 0 <= m.dual_gap_ <= 1e-12 * (yc @ yc) / n and m.n_iter_ < 100000, f"(gap {m.dual_gap_:.2e}, bound {1e-12 * (yc @ yc) / n:.2e}, n_iter {m.n_iter_})")
m = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(X, y)
gA, gO = dual_gap_lasso(Xc, yc, m.coef_, 0.05, 0.5)
which = "formulation A" if close(m.dual_gap_, gA, 1e-6, 1e-14) else ("pre-1.7 formula" if close(m.dual_gap_, gO, 1e-6, 1e-14) else "neither")
report("ElasticNet dual_gap_ = a valid duality gap (formulation A of main or the older formula) / n", which != "neither", f"({which}: dual_gap_ {m.dual_gap_:.3e}, A {gA:.3e}, old {gO:.3e})")
# l1_ratio = 0 is ridge with alpha scaled by n
m = ElasticNet(alpha=0.3, l1_ratio=0.0, tol=1e-14, max_iter=100000).fit(X, y)
wr = np.linalg.solve(Xc.T @ Xc + n * 0.3 * np.eye(p), Xc.T @ yc)
report("ElasticNet(l1_ratio=0, alpha) = ridge with penalty n*alpha: (Xc'Xc + n alpha I) w = Xc'yc (the 1/(2n) loss scaling)", np.allclose(m.coef_, wr, rtol=1e-8, atol=1e-10))
# positive
m = ElasticNet(alpha=0.05, l1_ratio=0.7, positive=True, tol=1e-12, max_iter=100000).fit(X, y)
wr, _ = enet_cd(X, y, 0.05, 0.7, positive=True)
report("ElasticNet(positive=True): all coef >= 0, KKT of the sign-constrained problem hold, = plain CD with the clamp", np.all(m.coef_ >= 0) and kkt_enet(Xc, yc, m.coef_, 0.05, 0.7, positive=True) < 1e-9 and np.allclose(m.coef_, wr, atol=1e-8), f"(coef {np.round(m.coef_, 4)})")
# alpha = 0 vs OLS
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); m0 = ElasticNet(alpha=0.0, tol=1e-14, max_iter=100000).fit(X, y)
wo, bo = ols(X, y)
report("ElasticNet(alpha=0) = OLS (documented: 'equivalent to an ordinary least square') and a warning advises LinearRegression", np.allclose(m0.coef_, wo, rtol=1e-6, atol=1e-8) and close(m0.intercept_, bo, 1e-6) and any("alpha=0" in str(x.message) or "LinearRegression" in str(x.message) for x in wl), f"({len(wl)} warnings)")
# warm_start
m1 = ElasticNet(alpha=0.1, tol=1e-12, max_iter=100000, warm_start=True).fit(X, y); it1 = m1.n_iter_; m1.fit(X, y)
report("warm_start=True: refitting from the converged solution takes fewer iterations and gives the same coef", m1.n_iter_ < it1 and np.allclose(m1.coef_, ElasticNet(alpha=0.1, tol=1e-12, max_iter=100000).fit(X, y).coef_, atol=1e-10), f"(n_iter {it1} then {m1.n_iter_})")
m1.set_params(alpha=0.02); m1.fit(X, y); wr, _ = enet_cd(X, y, 0.02, 0.5)
report("warm_start then a new alpha: converges to the solution of the new problem (plain CD)", np.allclose(m1.coef_, wr, atol=1e-8))
# precompute
mp = ElasticNet(alpha=0.05, l1_ratio=0.5, precompute=True, tol=1e-12, max_iter=100000).fit(X, y)
mg = ElasticNet(alpha=0.05, l1_ratio=0.5, precompute=Xc.T @ Xc, tol=1e-12, max_iter=100000).fit(X, y)
wr, _ = enet_cd(X, y, 0.05, 0.5)
report("precompute=True and precompute=Gram(Xc'Xc of the centred X) give the same solution as plain CD", np.allclose(mp.coef_, wr, atol=1e-8) and np.allclose(mg.coef_, wr, atol=1e-8))
# sample_weight semantics: objective 1/(2 sum(sw)) sum sw (y-Xw)^2 + penalty (sw rescaled to sum n)
sw = rs.uniform(0.2, 3.0, n)
m = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(X, y, sample_weight=sw)
Xcw, ycw, xmw, ymw = centre(X, y, sw); wr, br = enet_cd(X, y, 0.05, 0.5, sw=sw)
report("ElasticNet sample_weight: minimises 1/(2 sum sw) sum sw_i (y_i - x_i w - b)^2 + penalty, weighted centring ('rescaled to sum to n_samples')", kkt_enet(Xcw, ycw, m.coef_, 0.05, 0.5, sw=sw) < 1e-9 and np.allclose(m.coef_, wr, atol=1e-8) and close(m.intercept_, br, 1e-9, 1e-9))
m2 = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(X, y, sample_weight=np.full(n, 2.0))
m1 = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(X, y)
md = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(np.vstack([X, X]), np.concatenate([y, y]))
report("ElasticNet: sample_weight=2 == duplicated rows == unweighted fit (objective normalised by the weight sum)", np.allclose(m2.coef_, md.coef_, atol=1e-9) and np.allclose(m2.coef_, m1.coef_, atol=1e-9))
idx = rs.randint(0, n, 25); wcount = np.bincount(idx, minlength=n).astype(float)
mw = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(X, y, sample_weight=wcount)
mdup = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(X[idx], y[idx])
report("ElasticNet: integer sample_weight (some zero) == the row-duplicated data set", np.allclose(mw.coef_, mdup.coef_, atol=1e-8) and close(mw.intercept_, mdup.intercept_, 1e-8, 1e-8))
# sparse X
ms = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(sparse.csr_matrix(X), y)
report("ElasticNet on sparse csr X (fit_intercept=True) = dense solution (same objective, implicit centring)", np.allclose(ms.coef_, m1.coef_, atol=1e-8) and close(ms.intercept_, m1.intercept_, 1e-8, 1e-8))
ms = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(sparse.csr_matrix(X), y, sample_weight=sw)
report("ElasticNet on sparse X with sample_weight = dense weighted solution", np.allclose(ms.coef_, wr, atol=1e-8))
wr, _ = enet_cd(X, y, 0.05, 0.5)
m32 = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-8, max_iter=100000).fit(X.astype(np.float32), y.astype(np.float32))
report("ElasticNet float32 input: coef_ dtype float32 and within 1e-4 of the float64 solution", m32.coef_.dtype == np.float32 and np.allclose(m32.coef_, wr, atol=1e-4))
# multi-output ElasticNet: independent problems per target
Y2 = np.column_stack([y, X @ np.array([0, 0, 1.0, -1.0, 0, 0.3]) + rs.randn(n)])
mm = ElasticNet(alpha=0.05, l1_ratio=0.5, tol=1e-12, max_iter=100000).fit(X, Y2)
w1, _ = enet_cd(X, Y2[:, 1], 0.05, 0.5); wr, _ = enet_cd(X, y, 0.05, 0.5)
report("ElasticNet multi-output: coef_ shape (n_targets, n_features), each row the single-target solution", mm.coef_.shape == (2, p) and np.allclose(mm.coef_[0], wr, atol=1e-8) and np.allclose(mm.coef_[1], w1, atol=1e-8))

# ================================================================ lasso_path / enet_path grid
alpha_max = np.max(np.abs(X.T @ y)) / n; alpha_max_c = np.max(np.abs(Xc.T @ yc)) / n
al, co, _ = lasso_path(X, y, eps=1e-3, n_alphas=20)
grid = np.geomspace(alpha_max, alpha_max * 1e-3, 20)
report("lasso_path/enet_path/lars_path fit NO intercept (no fit_intercept parameter; docstrings silent): the grid starts at max|X'y|/n of the RAW data, not of the centred data", np.allclose(al, grid, rtol=1e-12) and not close(al[0], alpha_max_c, 1e-6), f"(alphas[0] {al[0]:.6f}, raw max|X'y|/n {alpha_max:.6f}, centred {alpha_max_c:.6f})")
report("lasso_path default grid: alphas[0] = max|X'y|/n, geometric down to eps*alpha_max (eps=1e-3), n_alphas points", np.allclose(al, grid, rtol=1e-12) and len(al) == 20, f"(alpha_max {alpha_max:.6f})")
report("lasso_path: coef at alpha_max is exactly 0 and non-zero at the next grid point ('alpha_max which results in coef=0')", np.all(co[:, 0] == 0) and np.any(co[:, 1] != 0))
al2, co2, _ = enet_path(X, y, l1_ratio=0.4, eps=1e-2, n_alphas=7)
report("enet_path(l1_ratio=0.4): alpha_max = max|X'y|/(n l1_ratio), eps and n_alphas honoured", np.allclose(al2, np.geomspace(alpha_max / 0.4, alpha_max / 0.4 * 1e-2, 7), rtol=1e-12) and np.all(co2[:, 0] == 0) and np.any(co2[:, 1] != 0))
al3, _, _ = lasso_path(X, y, alphas=[0.5, 0.01, 0.1])
report("lasso_path(alphas=...): the alphas are returned sorted in decreasing order", np.all(al3 == np.array([0.5, 0.1, 0.01])), f"({al3})")
alpos, copos, _ = lasso_path(X, y, positive=True, n_alphas=10)
apos = max(0.0, np.max(X.T @ y)) / n
pos_grid_ok = close(alpos[0], apos, 1e-12)
report(("lasso_path(positive=True): alpha_max = max(0, max X'y)/n (the smallest alpha with all coef 0 under the sign constraint)" if VER >= (1, 7) else "lasso_path(positive=True) [<1.7: grid ignores positive, alpha_max = max|X'y|/n and the first point(s) of the path are all-zero]"),
       pos_grid_ok if VER >= (1, 7) else close(alpos[0], alpha_max, 1e-12), f"(alphas[0] {alpos[0]:.6f}, positive alpha_max {apos:.6f}, unsigned {alpha_max:.6f})")
report("lasso_path(positive=True): coef at alphas[0] is 0, coefs >= 0 all along the path", np.all(copos[:, 0] == 0) and np.all(copos >= 0))
# alpha grid with sample_weight: n_samples replaced by sum(sw), weighted centring
alw, _, _ = lasso_path(X, y, n_alphas=5, sample_weight=sw) if "sample_weight" in inspect.signature(lasso_path).parameters else (None, None, None)
if alw is not None:
    amw = np.max(np.abs(X.T @ (sw * y))) / sw.sum()
    report("lasso_path(sample_weight): alpha_max = max|X'(sw*y)| / sum(sw) (n_samples replaced by the weight sum, raw data)", close(alw[0], amw, 1e-12), f"({alw[0]:.6f} vs {amw:.6f})")
# path coefficients satisfy KKT at every alpha (tol tight)
al, co, gaps = lasso_path(X, y, n_alphas=8, tol=1e-12, max_iter=100000)
viol = max(kkt_enet(X, y, co[:, i], al[i]) for i in range(len(al)))
report("lasso_path coefficients satisfy the no-intercept Lasso KKT on the raw data at every alpha of the grid (tol=1e-12)", viol < 1e-8, f"(max violation {viol:.2e})")

# ================================================================ Lars / LassoLars / lars_path
Xl = rs.randn(30, 5) @ np.array([[1, .6, 0, 0, 0], [0, 1, .5, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, .7], [0, 0, 0, 0, 1]]); yl = Xl @ np.array([3, -2, 0, 1.5, 0]) + 0.3 * rs.randn(30) + 1.0
Xlc, ylc, _, _ = centre(Xl, yl)
al_ref, co_ref = lars_plain(Xl, yl, "lar")
al_sk, act_sk, co_sk = lars_path(Xl, yl, method="lar")
report("lars_path(method='lar') alphas = max|X'(y - mu)|/n at every node of a plain-numpy LARS (raw data, no intercept)", np.allclose(al_sk, al_ref, rtol=1e-8, atol=1e-10), f"(alphas {np.round(al_sk, 5)})")
report("lars_path(method='lar') coefficient path at the nodes = plain-numpy LARS", co_sk.shape == co_ref.shape and np.allclose(co_sk, co_ref, atol=1e-8))
report("lars_path: active set order = order of entry in the plain LARS, final coef = OLS on centred data", [int(a) for a in act_sk] == lars_plain.order and np.allclose(co_sk[:, -1], np.linalg.lstsq(Xl, yl, rcond=None)[0], atol=1e-8), f"(active {[int(a) for a in act_sk]})")
# lasso path (with a variable drop) against the plain implementation
Xd = rs.randn(40, 4); Xd[:, 3] = Xd[:, 0] + Xd[:, 1] + 0.3 * rs.randn(40); yd = Xd @ np.array([2.0, 1.5, 0.0, -1.0]) + 0.2 * rs.randn(40)
Xdc, ydc, _, _ = centre(Xd, yd)
al_ref, co_ref = lars_plain(Xd, yd, "lasso"); al_sk, act_sk, co_sk = lars_path(Xd, yd, method="lasso")
report("lars_path(method='lasso') alphas and coefs at the nodes = plain-numpy LARS with the lasso modification", al_sk.shape == al_ref.shape and np.allclose(al_sk, al_ref, rtol=1e-8, atol=1e-10) and np.allclose(co_sk, co_ref, atol=1e-8), f"(nodes {len(al_sk)}, alphas {np.round(al_sk, 5)})")
Xk = rs.randn(50, 6); yk = Xk @ np.array([1, -1, 0.5, 0, 0, 0]) + 0.5 * rs.randn(50)
Xkc, ykc, _, _ = centre(Xk, yk); al_sk, _, co_sk = lars_path(Xkc, ykc, method="lasso")
viol = max(kkt_enet(Xkc, ykc, co_sk[:, i], al_sk[i]) for i in range(len(al_sk)))
mid = [(al_sk[i] + al_sk[i + 1]) / 2 for i in range(len(al_sk) - 1)]
report("lars_path(method='lasso') on centred data: every node satisfies the Lasso KKT at its alpha (the path is the exact Lasso solution)", viol < 1e-8, f"(max violation {viol:.2e})")
for a in mid[:3]:
    ll = LassoLars(**LARS_KW, alpha=a, fit_intercept=True).fit(Xk, yk); cd = Lasso(alpha=a, tol=1e-14, max_iter=200000).fit(Xk, yk)
    report(f"LassoLars(alpha={a:.4f}) between two nodes = Lasso(alpha) by coordinate descent (documented same objective)", np.allclose(ll.coef_, cd.coef_, atol=1e-8) and close(ll.intercept_, cd.intercept_, 1e-8, 1e-8), f"(nnz {np.count_nonzero(ll.coef_)})")
a = mid[2]; ll = LassoLars(**LARS_KW, alpha=a).fit(Xk, yk)
report("LassoLars(alpha): alphas_ stops at alpha (alpha_min), last node alpha == alpha, coef_ = the interpolated path there", close(ll.alphas_[-1], a, 1e-12) and np.all(ll.alphas_[:-1] > a) and kkt_enet(Xkc, ykc, ll.coef_, a) < 1e-8)
al_min, _, co_min = lars_path(Xkc, ykc, method="lasso", alpha_min=a)
report("lars_path(alpha_min): the path is truncated at alpha_min with the interpolated coefficients", close(al_min[-1], a, 1e-12) and np.allclose(co_min[:, -1], ll.coef_, atol=1e-10))
lp = LassoLars(**LARS_KW, alpha=mid[1], positive=True).fit(Xk, yk)
report("LassoLars(positive=True): coef >= 0 and satisfies the positive-Lasso KKT at alpha (alpha above the smallest alpha reached)", np.all(lp.coef_ >= 0) and kkt_enet(Xkc, ykc, lp.coef_, mid[1], positive=True) < 1e-8, f"(coef {np.round(lp.coef_, 4)}, alphas_ {np.round(lp.alphas_, 4)})")
l0 = Lars(**LARS_KW, n_nonzero_coefs=2).fit(Xk, yk)
report("Lars(n_nonzero_coefs=2): exactly 2 non-zero coefficients, alphas_ has 3 nodes", np.count_nonzero(l0.coef_) == 2 and len(l0.alphas_) == 3)
wo, bo = ols(Xk, yk)
try:
    lf = Lars(**LARS_KW, n_nonzero_coefs=np.inf).fit(Xk, yk); inf_ok = np.allclose(lf.coef_, wo, atol=1e-8); inf_detail = ""
except Exception as e:
    inf_ok = False; inf_detail = f"({type(e).__name__}: {str(e)[:90]})"
report("Lars(n_nonzero_coefs=np.inf): docstring says 'Use np.inf for no limit' -> accepted and the full path ends at OLS", inf_ok, inf_detail)
lf = Lars(**LARS_KW, n_nonzero_coefs=500).fit(Xk, yk)
report("Lars(n_nonzero_coefs=500 default) with 6 features: the full path ends at OLS (coef_ and intercept_)", np.allclose(lf.coef_, wo, atol=1e-8) and close(lf.intercept_, bo, 1e-8, 1e-8))
lm = Lars(**LARS_KW, fit_intercept=False).fit(Xk, yk); ar, cr = lars_plain(Xk, yk, "lar")
report("Lars(fit_intercept=False): path on the raw (uncentred) data = plain LARS on raw data", np.allclose(lm.alphas_, ar, rtol=1e-8) and np.allclose(lm.coef_path_, cr, atol=1e-8))
# LassoLars vs Lasso with alpha = 0 : OLS
ll0 = LassoLars(**LARS_KW, alpha=0.0).fit(Xk, yk)
report("LassoLars(alpha=0) = OLS (documented equivalence)", np.allclose(ll0.coef_, wo, atol=1e-8))

# ---- LassoLarsIC : AIC/BIC as documented
for crit, fac in [("aic", 2.0), ("bic", math.log(50))]:
    ic = LassoLarsIC(**LARS_KW, criterion=crit, noise_variance=0.25).fit(Xk, yk)
    al_sk, _, co_sk = lars_path(Xkc, ykc, method="lasso")
    rss = ((ykc[:, None] - Xkc @ co_sk) ** 2).sum(0); df = (np.abs(co_sk) > np.finfo(float).eps).sum(0)
    crit_ref = 50 * math.log(2 * math.pi * 0.25) + rss / 0.25 + fac * df
    report(f"LassoLarsIC({crit}, noise_variance=0.25): criterion_ = n log(2 pi sigma^2) + RSS/sigma^2 + {'2' if crit == 'aic' else 'log(n)'} * (number of non-zero coefs) along the lasso path, alpha_ = argmin", np.allclose(ic.criterion_, crit_ref, rtol=1e-10) and close(ic.alpha_, al_sk[np.argmin(crit_ref)], 1e-12) and np.allclose(ic.coef_, co_sk[:, np.argmin(crit_ref)], atol=1e-10), f"(chosen index {np.argmin(crit_ref)} of {len(crit_ref)}, df {df.tolist()})")
ic = LassoLarsIC(**LARS_KW, criterion="aic").fit(Xk, yk); rss_ols = ((ykc - Xkc @ np.linalg.lstsq(Xkc, ykc, rcond=None)[0]) ** 2).sum()
report("LassoLarsIC noise_variance_ default: user guide says RSS_OLS/(n - p) with p = n_features", close(ic.noise_variance_, rss_ols / (50 - 6), 1e-12), f"(noise_variance_ {ic.noise_variance_:.6f}, RSS/(n-p) {rss_ols / 44:.6f}, RSS/(n-p-1) {rss_ols / 43:.6f})")
report("LassoLarsIC noise_variance_ default = RSS_OLS/(n - p - 1) i.e. the intercept counted as a parameter (what the code does)", close(ic.noise_variance_, rss_ols / 43, 1e-12))
ic0 = LassoLarsIC(**LARS_KW, criterion="bic", fit_intercept=False).fit(Xk, yk); rss0 = ((yk - Xk @ np.linalg.lstsq(Xk, yk, rcond=None)[0]) ** 2).sum()
report("LassoLarsIC(fit_intercept=False) noise_variance_ = RSS_OLS/(n - p)", close(ic0.noise_variance_, rss0 / 44, 1e-12))
try:
    LassoLarsIC().fit(rs.randn(5, 6), rs.randn(5)); ok = False
except ValueError: ok = True
report("LassoLarsIC with n_samples <= n_features + 1 and no noise_variance raises ValueError (documented)", ok)

# ---- LassoLarsCV / LarsCV : mse_path_ from per-fold paths (reference = plain LARS + interpolation)
cvk = KFold(3)
lcv = LassoLarsCV(**LARS_KW, cv=cvk, max_iter=500).fit(Xk, yk)
ref_mse = np.zeros((len(lcv.cv_alphas_), 3))
for k, (tr, te) in enumerate(cvk.split(Xk)):
    Xt, yt, xmt, ymt = centre(Xk[tr], yk[tr]); ar, cr = lars_plain(Xt, yt, "lasso")
    for j, a in enumerate(lcv.cv_alphas_):
        aa = min(max(a, ar[-1]), ar[0])
        # linear interpolation of the coefficients between the nodes (alphas decreasing)
        i1 = np.searchsorted(-ar, -aa); i1 = min(max(i1, 1), len(ar) - 1); i0 = i1 - 1
        t = (ar[i0] - aa) / (ar[i0] - ar[i1]) if ar[i0] != ar[i1] else 0.0
        w = cr[:, i0] * (1 - t) + cr[:, i1] * t; b = ymt - xmt @ w
        ref_mse[j, k] = np.mean((yk[te] - Xk[te] @ w - b) ** 2)
report("LassoLarsCV(cv=KFold(3)): mse_path_[j,k] = test MSE on fold k of the fold-k lasso path interpolated at cv_alphas_[j] (plain LARS reference)", lcv.mse_path_.shape == ref_mse.shape and np.allclose(lcv.mse_path_, ref_mse, rtol=1e-6, atol=1e-9), f"(shape {lcv.mse_path_.shape}, max diff {np.max(np.abs(lcv.mse_path_ - ref_mse)):.2e})")
report("LassoLarsCV alpha_ = cv_alphas_[argmin of the fold-mean mse_path_], coef_ = LassoLars(alpha_) on all data", close(lcv.alpha_, lcv.cv_alphas_[np.argmin(lcv.mse_path_.mean(1))], 1e-12) and np.allclose(lcv.coef_, LassoLars(**LARS_KW, alpha=lcv.alpha_).fit(Xk, yk).coef_, atol=1e-10))
report("LassoLarsCV cv_alphas_ = np.unique of all fold-path alphas (increasing, no order documented)", np.all(np.diff(lcv.cv_alphas_) > 0))
report("LassoLarsCV mse_path_ shape as documented '(n_folds, n_cv_alphas)'", lcv.mse_path_.shape == (3, len(lcv.cv_alphas_)), f"(actual shape {lcv.mse_path_.shape}, n_folds 3, n_cv_alphas {len(lcv.cv_alphas_)})")
larscv = LarsCV(**LARS_KW, cv=cvk).fit(Xk, yk)
report("LarsCV: mse_path_ shape (n_cv_alphas, n_folds), alpha_ = argmin of the fold-mean", larscv.mse_path_.shape == (len(larscv.cv_alphas_), 3) and close(larscv.alpha_, larscv.cv_alphas_[np.argmin(larscv.mse_path_.mean(1))], 1e-12))

# ================================================================ OrthogonalMatchingPursuit
def omp_ref(Xc, yc, n_nonzero=None, tol=None):
    r = yc.copy(); act = []; w = np.zeros(Xc.shape[1]); nit = 0
    while True:
        j = int(np.argmax(np.abs(Xc.T @ r)))
        if j in act: break
        act.append(j); nit += 1
        w = np.zeros(Xc.shape[1]); w[act] = np.linalg.lstsq(Xc[:, act], yc, rcond=None)[0]; r = yc - Xc @ w
        if tol is not None and r @ r <= tol: break
        if tol is None and len(act) >= n_nonzero: break
    return w, act, nit
Xo = rs.randn(60, 10); yo = Xo @ np.array([0, 3, 0, 0, -2, 0, 0, 1, 0, 0]) + 0.3 * rs.randn(60) + 2
Xoc, yoc, xmo, ymo = centre(Xo, yo)
for k in (1, 2, 3):
    om = OrthogonalMatchingPursuit(**LARS_KW, n_nonzero_coefs=k).fit(Xo, yo); wr, act, nit = omp_ref(Xoc, yoc, n_nonzero=k)
    report(f"OMP(n_nonzero_coefs={k}): greedy selection of argmax|X'r| with least squares on the active set = plain reference, n_iter_ = {k}", np.allclose(om.coef_, wr, atol=1e-8) and om.n_iter_ == nit and close(om.intercept_, ymo - xmo @ wr, 1e-9, 1e-9), f"(active {act})")
om = OrthogonalMatchingPursuit().fit(Xo, yo)
report("OMP default n_nonzero_coefs = max(int(0.1 n_features), 1) = 1 for 10 features (n_nonzero_coefs_)", om.n_nonzero_coefs_ == 1 and np.count_nonzero(om.coef_) == 1)
om = OrthogonalMatchingPursuit(**LARS_KW, tol=0.5 * (yoc @ yoc)).fit(Xo, yo); wr, act, nit = omp_ref(Xoc, yoc, tol=0.5 * (yoc @ yoc))
report("OMP(tol): stops as soon as ||r||^2 <= tol (tol = maximum squared norm of the residual), n_nonzero_coefs_ is None", np.allclose(om.coef_, wr, atol=1e-8) and om.n_iter_ == nit and om.n_nonzero_coefs_ is None, f"(active {act})")
om = OrthogonalMatchingPursuit(**LARS_KW, n_nonzero_coefs=3, precompute=True).fit(Xo, yo); wr, _, _ = omp_ref(Xoc, yoc, n_nonzero=3)
report("OMP(precompute=True) (Gram/Xy path) = the same greedy solution", np.allclose(om.coef_, wr, atol=1e-8))
om = OrthogonalMatchingPursuit(**LARS_KW, n_nonzero_coefs=10).fit(Xo, yo); wo, bo = ols(Xo, yo)
report("OMP with n_nonzero_coefs = n_features = OLS", np.allclose(om.coef_, wo, atol=1e-8) and close(om.intercept_, bo, 1e-8, 1e-8))
om = OrthogonalMatchingPursuit(**LARS_KW, n_nonzero_coefs=2).fit(Xo, np.column_stack([yo, -yo]))
report("OMP multi-target: coef_ shape (n_targets, n_features), the negated target gives the negated coef", om.coef_.shape == (2, 10) and np.allclose(om.coef_[0], -om.coef_[1], atol=1e-10))

# ================================================================ BayesianRidge
def bayes_ridge_ref(X, y, n_iter, alpha_1=1e-6, alpha_2=1e-6, lambda_1=1e-6, lambda_2=1e-6, alpha_init=None, lambda_init=None, sw=None, legacy=False):
    """MacKay/Tipping evidence updates as documented: coef = posterior mean, gamma = sum a*l_i/(l + a*l_i),
    lambda = (gamma + 2 l1)/(||w||^2 + 2 l2), alpha = (n - gamma + 2 a1)/(SSE + 2 a2), n = sum of weights."""
    n, p = X.shape
    if sw is None: sw = np.ones(n)
    Xc, yc, xm, ym = centre(X, y, sw); Xs = Xc * np.sqrt(sw)[:, None]; ys = yc * np.sqrt(sw)
    yvar = np.average((y - ym) ** 2, weights=sw)
    if legacy: yvar = ys.var(); n_eff = n   # pre-1.9 code: alpha_init from the sqrt(sw)-rescaled y, n_samples = number of rows in the alpha update
    else: n_eff = sw.sum()
    a = 1.0 / (yvar + np.finfo(float).eps) if alpha_init is None else alpha_init; l = 1.0 if lambda_init is None else lambda_init
    ev = np.linalg.eigvalsh(Xs.T @ Xs); ev = np.clip(ev, 0, None)
    def coef(a, l):
        w = np.linalg.solve(l * np.eye(p) + a * Xs.T @ Xs, a * Xs.T @ ys); return w, ((ys - Xs @ w) ** 2).sum()
    for _ in range(n_iter):
        w, sse = coef(a, l); gamma = np.sum(a * ev / (l + a * ev))
        l = (gamma + 2 * lambda_1) / (w @ w + 2 * lambda_2); a = (n_eff - gamma + 2 * alpha_1) / (sse + 2 * alpha_2)
    w, sse = coef(a, l); sigma = np.linalg.inv(l * np.eye(p) + a * Xs.T @ Xs)
    return w, ym - xm @ w, a, l, sigma
Xb = rs.randn(50, 4); yb = Xb @ np.array([1.0, -2.0, 0.0, 0.5]) + 1.5 + 0.4 * rs.randn(50)
br = BR(max_iter=7, tol=1e-300).fit(Xb, yb); w, b, a, l, sig = bayes_ridge_ref(Xb, yb, 7)
report("BR(max_iter=7, tol tiny): coef_, intercept_, alpha_, lambda_ = 7 documented MacKay updates from alpha_init=1/Var(y), lambda_init=1 (plain-numpy replica)", np.allclose(br.coef_, w, rtol=1e-8, atol=1e-10) and close(br.intercept_, b, 1e-8) and close(br.alpha_, a, 1e-8) and close(br.lambda_, l, 1e-8) and br.n_iter_ == 7, f"(alpha_ {br.alpha_:.5f}, lambda_ {br.lambda_:.5f})")
br = BR(max_iter=3, tol=1e-300, alpha_init=2.0, lambda_init=0.5, alpha_1=1e-3, alpha_2=1e-2, lambda_1=1e-4, lambda_2=1e-5).fit(Xb, yb)
w, b, a, l, sig = bayes_ridge_ref(Xb, yb, 3, 1e-3, 1e-2, 1e-4, 1e-5, 2.0, 0.5)
report("BayesianRidge with alpha_init/lambda_init and non-default gamma hyper-parameters alpha_1, alpha_2, lambda_1, lambda_2 = replica", np.allclose(br.coef_, w, rtol=1e-8) and close(br.alpha_, a, 1e-8) and close(br.lambda_, l, 1e-8))
br = BR(max_iter=1000, tol=1e-14).fit(Xb, yb); Xbc, ybc, _, _ = centre(Xb, yb)
ev = np.linalg.eigvalsh(Xbc.T @ Xbc); gamma = np.sum(br.alpha_ * ev / (br.lambda_ + br.alpha_ * ev)); sse = ((ybc - Xbc @ br.coef_) ** 2).sum()
fp = [close(br.lambda_, (gamma + 2e-6) / (br.coef_ @ br.coef_ + 2e-6), 1e-6), close(br.alpha_, (50 - gamma + 2e-6) / (sse + 2e-6), 1e-6),
      np.allclose(br.coef_, np.linalg.solve(br.lambda_ * np.eye(4) + br.alpha_ * Xbc.T @ Xbc, br.alpha_ * Xbc.T @ ybc), rtol=1e-8)]
report("BayesianRidge converged (tol=1e-14): (alpha_, lambda_, coef_) is a fixed point of the evidence-maximisation equations", all(fp), f"(n_iter_ {br.n_iter_}, gamma {gamma:.4f})")
report("BayesianRidge sigma_ = (lambda I + alpha Xc'Xc)^-1 (posterior covariance of w)", np.allclose(br.sigma_, np.linalg.inv(br.lambda_ * np.eye(4) + br.alpha_ * Xbc.T @ Xbc), rtol=1e-8))
Xq = rs.randn(5, 4); ym_, ys_ = br.predict(Xq, return_std=True)
std_ref = np.sqrt(1 / br.alpha_ + np.einsum("ij,jk,ik->i", Xq - Xb.mean(0), br.sigma_, Xq - Xb.mean(0)))
std_raw = np.sqrt(1 / br.alpha_ + np.einsum("ij,jk,ik->i", Xq, br.sigma_, Xq))
report("BayesianRidge predict(return_std=True): std = sqrt(1/alpha_ + (x - X_offset_) sigma_ (x - X_offset_)') (sigma_ is the posterior covariance on the CENTRED design)", np.allclose(ys_, std_ref, rtol=1e-10) and np.allclose(ym_, Xq @ br.coef_ + br.intercept_, rtol=1e-10), f"(uncentred-x formula matches: {np.allclose(ys_, std_raw, rtol=1e-10)})")
swb = rs.uniform(0.5, 2, 50); brw = BR(max_iter=5, tol=1e-300).fit(Xb, yb, sample_weight=swb); w, b, a, l, sig = bayes_ridge_ref(Xb, yb, 5, sw=swb)
w_n, b_n, a_n, l_n, _ = bayes_ridge_ref(Xb, yb, 5, sw=swb, legacy=True)
report("BayesianRidge sample_weight: weighted centring, X,y scaled by sqrt(sw), alpha_init = 1/Var_w(y), n replaced by sum(sw) in the alpha update (replica)", np.allclose(brw.coef_, w, rtol=1e-8) and close(brw.alpha_, a, 1e-8) and close(brw.lambda_, l, 1e-8), f"(alpha_ {brw.alpha_:.5f} vs sum(sw) replica {a:.5f}; legacy replica [alpha_init = 1/var(sqrt(sw) y_c), n = n_rows] {a_n:.5f}, coef match legacy: {np.allclose(brw.coef_, w_n, rtol=1e-8)})")
b2 = BR(max_iter=20, tol=1e-300).fit(Xb, yb, sample_weight=np.full(50, 2.0)); bd = BR(max_iter=20, tol=1e-300).fit(np.vstack([Xb, Xb]), np.concatenate([yb, yb]))
report("BayesianRidge: sample_weight=2 == duplicated rows (coef_, alpha_, lambda_)", np.allclose(b2.coef_, bd.coef_, rtol=1e-8) and close(b2.alpha_, bd.alpha_, 1e-8) and close(b2.lambda_, bd.lambda_, 1e-8))
brs = BR(max_iter=7, tol=1e-300, compute_score=True).fit(Xb, yb)
report("BR(compute_score=True): scores_ has max_iter + 1 log-marginal-likelihood values and is increasing at the start", len(brs.scores_) == 8 and brs.scores_[1] >= brs.scores_[0], f"(scores {np.round(brs.scores_[:3], 3)} ...)")
Xbw = rs.randn(6, 10); ybw = rs.randn(6); brw = BR(max_iter=4, tol=1e-300).fit(Xbw, ybw); w, b, a, l, sig = bayes_ridge_ref(Xbw, ybw, 4)
report("BayesianRidge with n_samples < n_features (6 x 10): same documented updates (eigenvalues padded with zeros)", np.allclose(brw.coef_, w, rtol=1e-6, atol=1e-8) and close(brw.alpha_, a, 1e-6) and close(brw.lambda_, l, 1e-6))

# ================================================================ ARDRegression
def ard_ref(X, y, n_iter, threshold=1e4, alpha_1=1e-6, alpha_2=1e-6, lambda_1=1e-6, lambda_2=1e-6, tol=0.0):
    """ARD updates as documented (Tipping / MacKay); stops after n_iter or when sum|coef change| < tol like the code."""
    n, p = X.shape; Xc, yc, xm, ym = centre(X, y); a = 1.0 / (np.var(y) + np.finfo(float).eps); lam = np.ones(p); keep = np.ones(p, bool); w = np.zeros(p); w_old = None
    def sig(a, lam, keep): Xk = Xc[:, keep]; return np.linalg.inv(a * Xk.T @ Xk + np.diag(lam[keep]))
    for it in range(n_iter):
        S = sig(a, lam, keep); w[keep] = a * S @ Xc[:, keep].T @ yc; sse = ((yc - Xc @ w) ** 2).sum()
        gamma = 1 - lam[keep] * np.diag(S); lam[keep] = (gamma + 2 * lambda_1) / (w[keep] ** 2 + 2 * lambda_2)
        a = (n - gamma.sum() + 2 * alpha_1) / (sse + 2 * alpha_2); keep = lam < threshold; w[~keep] = 0
        if it > 0 and np.abs(w_old - w).sum() < tol: break
        w_old = w.copy()
    S = sig(a, lam, keep); w[keep] = a * S @ Xc[:, keep].T @ yc
    ard_ref.n_iter = it + 1
    return w, ym - xm @ w, a, lam, S
Xa = rs.randn(60, 5); ya = Xa @ np.array([2.0, 0, 0, -1.0, 0]) + 0.3 * rs.randn(60) + 0.5
ard = ARD(max_iter=6, tol=1e-300).fit(Xa, ya); w, b, a, lam, S = ard_ref(Xa, ya, 6)
report("ARD(max_iter=6): coef_, alpha_, lambda_ (one precision per feature), sigma_ = 6 documented ARD updates gamma_i = 1 - lambda_i Sigma_ii (replica)", np.allclose(ard.coef_, w, rtol=1e-8, atol=1e-10) and close(ard.alpha_, a, 1e-8) and np.allclose(ard.lambda_, lam, rtol=1e-8) and np.allclose(ard.sigma_, S, rtol=1e-8) and close(ard.intercept_, b, 1e-8), f"(lambda_ {np.round(ard.lambda_, 2)})")
ard = ARD(max_iter=300, tol=1e-12, threshold_lambda=50.0).fit(Xa, ya); w, b, a, lam, S = ard_ref(Xa, ya, 300, threshold=50.0, tol=1e-12)
pruned = ard.lambda_ >= 50.0
report("ARD(threshold_lambda=50): features whose lambda_ >= threshold are pruned: coef_ exactly 0, sigma_ only over the kept features", pruned.any() and np.all(ard.coef_[pruned] == 0) and ard.sigma_.shape == ((~pruned).sum(), (~pruned).sum()), f"(pruned {np.where(pruned)[0].tolist()}, kept {np.where(~pruned)[0].tolist()})")
report("ARDRegression converged with pruning (tol=1e-12) = replica with the same stopping rule (coef_, lambda_, alpha_)", np.allclose(ard.coef_, w, rtol=1e-6, atol=1e-9) and np.allclose(ard.lambda_, lam, rtol=1e-6) and close(ard.alpha_, a, 1e-6), f"(n_iter_ {getattr(ard, 'n_iter_', 'n/a (<1.3)')}, replica {ard_ref.n_iter})")
ym_, ys_ = ard.predict(Xq[:, :5] if Xq.shape[1] >= 5 else rs.randn(5, 5), return_std=True)
Xq5 = rs.randn(5, 5); ym_, ys_ = ard.predict(Xq5, return_std=True); Xk_ = (Xq5 - Xa.mean(0))[:, ~pruned]
Xk_raw = Xq5[:, ~pruned]
report("ARDRegression predict(return_std=True): std = sqrt(1/alpha_ + (x - X_offset_)_kept sigma_ (x - X_offset_)_kept') over the kept features", np.allclose(ys_, np.sqrt(1 / ard.alpha_ + np.einsum("ij,jk,ik->i", Xk_, ard.sigma_, Xk_)), rtol=1e-10), f"(uncentred-x formula matches: {np.allclose(ys_, np.sqrt(1 / ard.alpha_ + np.einsum('ij,jk,ik->i', Xk_raw, ard.sigma_, Xk_raw)), rtol=1e-10)})")
ardw = ARD(max_iter=4, tol=1e-300).fit(Xbw, ybw); w, b, a, lam, S = ard_ref(Xbw, ybw, 4)
report("ARDRegression with n_samples < n_features (Woodbury branch) = the same documented updates", np.allclose(ardw.coef_, w, rtol=1e-6, atol=1e-8) and np.allclose(ardw.lambda_, lam, rtol=1e-6) and close(ardw.alpha_, a, 1e-6))

# ================================================================ HuberRegressor
def huber_stationarity(X, y, w, b, s, eps, alpha, sw=None):
    """Gradient of sum_i sw_i (s + H_eps((y_i - x_i w - b)/s) s) + alpha ||w||^2 w.r.t. (w, b, s), all should vanish."""
    if sw is None: sw = np.ones(len(y))
    r = y - X @ w - b; out = np.abs(r) > eps * s
    gw = -2 * (sw * r * ~out) @ X / s - 2 * eps * (sw * np.sign(r) * out) @ X + 2 * alpha * w
    gb = -2 * (sw * r * ~out).sum() / s - 2 * eps * (sw * np.sign(r) * out).sum()
    gs = sw.sum() - (sw * r * r * ~out).sum() / s ** 2 - (sw * out).sum() * eps ** 2
    return max(np.abs(gw).max(), abs(gb), abs(gs))
Xh = rs.randn(80, 3); yh = Xh @ np.array([1.0, -1.0, 2.0]) + 0.5 + 0.3 * rs.randn(80); yh_out = yh.copy(); yh_out[:6] += np.array([8, -9, 10, 7, -8, 12])
def huber_obj(theta, X, y, eps, alpha, sw=None):
    if sw is None: sw = np.ones(len(y))
    w = theta[:X.shape[1]]; b = theta[X.shape[1]]; s = theta[-1]; z = (y - X @ w - b) / s
    H = np.where(np.abs(z) < eps, z * z, 2 * eps * np.abs(z) - eps ** 2); return np.sum(sw * (s + H * s)) + alpha * w @ w
def huber_opt(X, y, eps, alpha, sw=None):
    """My own minimiser of the documented objective: L-BFGS-B on the analytic gradient with ftol=0, gtol=1e-12."""
    def fg(t):
        w = t[:X.shape[1]]; b = t[X.shape[1]]; s = t[-1]; sw_ = np.ones(len(y)) if sw is None else sw
        r = y - X @ w - b; out = np.abs(r) > eps * s
        gw = -2 * (sw_ * r * ~out) @ X / s - 2 * eps * (sw_ * np.sign(r) * out) @ X + 2 * alpha * w
        gb = -2 * (sw_ * r * ~out).sum() / s - 2 * eps * (sw_ * np.sign(r) * out).sum()
        gs = sw_.sum() - (sw_ * r * r * ~out).sum() / s ** 2 - (sw_ * out).sum() * eps ** 2
        return huber_obj(t, X, y, eps, alpha, sw), np.concatenate([gw, [gb, gs]])
    t0 = np.zeros(X.shape[1] + 2); t0[-1] = 1.0
    r = optimize.minimize(fg, t0, jac=True, method="L-BFGS-B", bounds=[(None, None)] * (X.shape[1] + 1) + [(1e-10, None)], options=dict(ftol=0, gtol=1e-12, maxiter=100000))
    return r.x
hb = HuberRegressor(epsilon=1.35, alpha=0.01, tol=1e-12, max_iter=10000).fit(Xh, yh_out)
th = np.concatenate([hb.coef_, [hb.intercept_, hb.scale_]]); topt = huber_opt(Xh, yh_out, 1.35, 0.01)
v = huber_stationarity(Xh, yh_out, hb.coef_, hb.intercept_, hb.scale_, 1.35, 0.01)
report("HuberRegressor(epsilon=1.35, alpha=0.01): (coef_, intercept_, scale_) minimise the documented objective sum_i (sigma + H_eps((y_i - x_i w - c)/sigma) sigma) + alpha ||w||^2 (my own L-BFGS-B optimum: objective within 1e-8, parameters within 1e-3)", np.allclose(th, topt, rtol=1e-3, atol=1e-5) and huber_obj(th, Xh, yh_out, 1.35, 0.01) <= huber_obj(topt, Xh, yh_out, 1.35, 0.01) * (1 + 1e-8), f"(objective {huber_obj(th, Xh, yh_out, 1.35, 0.01):.9f} vs mine {huber_obj(topt, Xh, yh_out, 1.35, 0.01):.9f}, scale_ {hb.scale_:.4f})")
report("HuberRegressor(tol=1e-12) docstring: 'iteration will stop when max|proj g_i| <= tol' -> the gradient at the returned solution is <= 1e-8", v < 1e-8, f"(max |gradient| {v:.2e}, n_iter_ {hb.n_iter_}; scipy L-BFGS-B also stops on its default ftol=2.2e-9)")
r = np.abs(yh_out - Xh @ hb.coef_ - hb.intercept_)
report("HuberRegressor outliers_ = |y - Xw - c| > epsilon * scale_ and flags the 6 planted outliers", np.array_equal(hb.outliers_, r > hb.scale_ * 1.35) and np.all(hb.outliers_[:6]), f"({hb.outliers_.sum()} outliers)")
report("HuberRegressor scale_ = sqrt(sum_inliers r^2 / (n - n_out eps^2)) (the sigma stationarity condition, rel 1e-4)", close(hb.scale_, math.sqrt((r[~hb.outliers_] ** 2).sum() / (80 - hb.outliers_.sum() * 1.35 ** 2)), 1e-4))
hb0 = HuberRegressor(epsilon=1e6, alpha=0.0, tol=1e-14, max_iter=10000).fit(Xh, yh); wo, bo = ols(Xh, yh)
report("HuberRegressor(alpha=0, epsilon huge = no outliers) = OLS", np.allclose(hb0.coef_, wo, rtol=1e-6, atol=1e-8) and close(hb0.intercept_, bo, 1e-6), f"(max |diff| {np.abs(hb0.coef_ - wo).max():.2e})")
report("HuberRegressor with no outliers: scale_ = RMS residual sqrt(RSS/n) (sigma condition with all samples quadratic)", close(hb0.scale_, math.sqrt(((yh - Xh @ wo - bo) ** 2).sum() / 80), 1e-5))
hb1 = HuberRegressor(alpha=0.0, tol=1e-12, max_iter=10000).fit(Xh, yh_out); hb2 = HuberRegressor(alpha=0.0, tol=1e-12, max_iter=10000).fit(Xh, 10 * yh_out)
report("HuberRegressor(alpha=0) is scale invariant (documented): y*10 gives coef_, intercept_, scale_ times 10 and the same outliers_ (rel 1e-4, solver stops on ftol)", np.allclose(hb2.coef_, 10 * hb1.coef_, rtol=1e-4) and close(hb2.scale_, 10 * hb1.scale_, 1e-4) and np.array_equal(hb1.outliers_, hb2.outliers_), f"(max rel diff {np.abs(hb2.coef_ / hb1.coef_ / 10 - 1).max():.2e})")
swh = rs.uniform(0.5, 2, 80); hbw = HuberRegressor(alpha=0.01, tol=1e-12, max_iter=10000).fit(Xh, yh_out, sample_weight=swh)
thw = np.concatenate([hbw.coef_, [hbw.intercept_, hbw.scale_]]); toptw = huber_opt(Xh, yh_out, 1.35, 0.01, swh)
report("HuberRegressor sample_weight: minimises sum_i sw_i (sigma + H_eps(r_i/sigma) sigma) + alpha ||w||^2 (my optimum: parameters within 1e-3, objective within 1e-8)", np.allclose(thw, toptw, rtol=1e-3, atol=1e-5) and huber_obj(thw, Xh, yh_out, 1.35, 0.01, swh) <= huber_obj(toptw, Xh, yh_out, 1.35, 0.01, swh) * (1 + 1e-8), f"(objective {huber_obj(thw, Xh, yh_out, 1.35, 0.01, swh):.6f} vs mine {huber_obj(toptw, Xh, yh_out, 1.35, 0.01, swh):.6f})")
hbd = HuberRegressor(alpha=0.01, tol=1e-12, max_iter=10000).fit(np.vstack([Xh, Xh]), np.concatenate([yh_out, yh_out])); hb2w = HuberRegressor(alpha=0.01, tol=1e-12, max_iter=10000).fit(Xh, yh_out, sample_weight=np.full(80, 2.0))
report("HuberRegressor: sample_weight=2 == duplicated rows (rel 1e-4; and != the single copy because alpha is absolute)", np.allclose(hbd.coef_, hb2w.coef_, rtol=1e-4) and close(hbd.scale_, hb2w.scale_, 1e-4) and not np.allclose(hbd.coef_, hb.coef_, rtol=1e-6), f"(max rel diff {np.abs(hbd.coef_ / hb2w.coef_ - 1).max():.2e})")
try:
    HuberRegressor(epsilon=0.9).fit(Xh, yh); ok = False
except ValueError: ok = True
report("HuberRegressor epsilon < 1 raises ValueError (documented range [1, inf))", ok)

# ================================================================ QuantileRegressor
def pinball(r, q): return np.sum(q * np.maximum(r, 0) + (1 - q) * np.maximum(-r, 0))
xq = rs.uniform(-2, 2, 25); yq = 1.5 * xq + 0.7 + rs.standard_t(3, 25)
for q in (0.5, 0.2, 0.9):
    m = QR(quantile=q, alpha=0.0).fit(xq[:, None], yq)
    best = None
    for i, j in itertools.combinations(range(25), 2):
        if xq[i] == xq[j]: continue
        sl = (yq[j] - yq[i]) / (xq[j] - xq[i]); ic = yq[i] - sl * xq[i]; val = pinball(yq - sl * xq - ic, q)
        if best is None or val < best[0] - 1e-12: best = (val, sl, ic)
    val_sk = pinball(yq - m.predict(xq[:, None]), q)
    report(f"QuantileRegressor(quantile={q}, alpha=0, solver=highs): pinball loss = brute-force minimum over all lines through 2 data points (LP vertex)", close(val_sk, best[0], 1e-9, 1e-9) and close(m.coef_[0], best[1], 1e-6, 1e-8) and close(m.intercept_, best[2], 1e-6, 1e-8), f"(loss {val_sk:.6f}, coef {m.coef_[0]:.5f} vs {best[1]:.5f})")
    res = yq - m.predict(xq[:, None]); nneg = (res < -1e-9).sum(); nzero = (np.abs(res) <= 1e-9).sum()
    report(f"QuantileRegressor(quantile={q}): #(residual < 0) <= q n <= #(residual <= 0) (quantile property of the optimum)", nneg <= q * 25 <= nneg + nzero, f"(neg {nneg}, zero {nzero}, q n {q * 25})")
Xqm = rs.randn(40, 3); yqm = Xqm @ np.array([1, 0, -1.0]) + 0.5 + rs.standard_t(3, 40)
for q, al in ((0.5, 0.1), (0.3, 0.02)):
    m = QR(quantile=q, alpha=al).fit(Xqm, yqm)
    # independent LP formulation through scipy.optimize.linprog (dense): objective (1/n) sum pinball + alpha ||w||_1
    nq = 40; c = np.concatenate([np.full(8, al), np.full(nq, q / nq), np.full(nq, (1 - q) / nq)]); c[0] = c[4] = 0
    A = np.hstack([np.ones((nq, 1)), Xqm, -np.ones((nq, 1)), -Xqm, np.eye(nq), -np.eye(nq)])
    lp = optimize.linprog(c, A_eq=A, b_eq=yqm, bounds=(0, None), method="highs")
    obj_sk = pinball(yqm - m.predict(Xqm), q) / nq + al * np.abs(m.coef_).sum()
    report(f"QuantileRegressor(quantile={q}, alpha={al}): objective (1/n) sum PB_q + alpha ||w||_1 equals my own LP solution (linprog, intercept unpenalised)", close(obj_sk, lp.fun, 1e-9, 1e-9), f"(objective {obj_sk:.6f} vs LP {lp.fun:.6f})")
m2 = QR(quantile=0.4, alpha=0.05).fit(Xqm, yqm, sample_weight=np.full(40, 2.0)); md = QR(quantile=0.4, alpha=0.05).fit(np.vstack([Xqm, Xqm]), np.concatenate([yqm, yqm])); m1 = QR(quantile=0.4, alpha=0.05).fit(Xqm, yqm)
obj = lambda mm, X_, y_: pinball(y_ - mm.predict(X_), 0.4) / len(y_) + 0.05 * np.abs(mm.coef_).sum()
report("QuantileRegressor: sample_weight=2 == duplicated rows == single copy (objective normalised by sum(sw))", close(obj(m2, Xqm, yqm), obj(md, Xqm, yqm), 1e-9, 1e-9) and close(obj(m2, Xqm, yqm), obj(m1, Xqm, yqm), 1e-9, 1e-9))
mz = QR(quantile=0.5, alpha=0.0).fit(Xqm, yqm, sample_weight=(np.arange(40) < 30).astype(float)); mz2 = QR(quantile=0.5, alpha=0.0).fit(Xqm[:30], yqm[:30])
report("QuantileRegressor: zero sample weights drop the samples (same objective value as fitting the 30 weighted rows)", close(pinball(yqm[:30] - mz.predict(Xqm[:30]), 0.5), pinball(yqm[:30] - mz2.predict(Xqm[:30]), 0.5), 1e-9, 1e-9))
mbig = QR(quantile=0.5, alpha=100.0).fit(Xqm, yqm)
report("QuantileRegressor with a huge alpha: coef_ = 0 and intercept_ = the sample median", np.all(mbig.coef_ == 0) and close(mbig.intercept_, np.median(yqm), 1e-9, 1e-9) or (np.all(mbig.coef_ == 0) and pinball(yqm - mbig.intercept_, 0.5) <= pinball(yqm - np.median(yqm), 0.5) + 1e-9), f"(intercept {mbig.intercept_:.5f}, median {np.median(yqm):.5f})")
ms = QR(quantile=0.3, alpha=0.02).fit(sparse.csr_matrix(Xqm), yqm)
report("QuantileRegressor on sparse X (highs) = dense solution", np.allclose(ms.coef_, QR(quantile=0.3, alpha=0.02).fit(Xqm, yqm).coef_, atol=1e-8))

# ================================================================ Poisson / Gamma / Tweedie
def tweedie_dev(y, mu, pw):
    if pw == 0: return (y - mu) ** 2
    if pw == 1: return 2 * (np.where(y > 0, y * np.log(np.where(y > 0, y, 1) / mu), 0) - y + mu)
    if pw == 2: return 2 * (np.log(mu / y) + y / mu - 1)
    return 2 * (np.maximum(y, 0) ** (2 - pw) / ((1 - pw) * (2 - pw)) - y * mu ** (1 - pw) / (1 - pw) + mu ** (2 - pw) / (2 - pw))
def glm_grad(X, y, w, b, alpha, pw, sw=None):
    """Gradient of 1/(2 sum sw) sum sw d(y, exp(Xw+b)) + alpha/2 ||w||^2 (log link) in w and b."""
    if sw is None: sw = np.ones(len(y))
    mu = np.exp(X @ w + b); g = mu ** (1 - pw) * (mu - y) * sw / sw.sum()
    return np.abs(np.concatenate([X.T @ g + alpha * w, [g.sum()]])).max()
def glm_newton(X, y, pw, sw=None, iters=100):
    """Unpenalised MLE with log link by Newton-Raphson (plain numpy)."""
    if sw is None: sw = np.ones(len(y))
    A = np.hstack([X, np.ones((len(y), 1))]); th = np.zeros(A.shape[1]); th[-1] = math.log(np.average(y, weights=sw))
    for _ in range(iters):
        mu = np.exp(A @ th); g = A.T @ (sw * mu ** (1 - pw) * (mu - y))
        Wd = sw * mu ** (1 - pw) * ((2 - pw) * mu - (1 - pw) * y); Wd = np.maximum(Wd, 1e-12)
        H = A.T @ (Wd[:, None] * A); step = np.linalg.solve(H, g); th = th - step
        if np.abs(step).max() < 1e-14: break
    return th[:-1], th[-1]
Xg = rs.randn(120, 3) * 0.5; eta = Xg @ np.array([0.4, -0.3, 0.2]) + 1.0; yp = rs.poisson(np.exp(eta)).astype(float); yg = rs.gamma(3.0, np.exp(eta) / 3.0)
glm_kw = dict(max_iter=5000, tol=1e-12)
pr = PoissonRegressor(alpha=0.0, **glm_kw).fit(Xg, yp); wn, bn = glm_newton(Xg, yp, 1)
report("PoissonRegressor(alpha=0) = Poisson MLE with log link (plain-numpy Newton-Raphson)", np.allclose(pr.coef_, wn, rtol=1e-6, atol=1e-8) and close(pr.intercept_, bn, 1e-6), f"(max |diff| {np.abs(pr.coef_ - wn).max():.2e})")
pr = PoissonRegressor(alpha=0.3, **glm_kw).fit(Xg, yp)
report("PoissonRegressor(alpha=0.3): gradient of 1/(2n) sum 2(y log(y/mu) - y + mu) + alpha/2 ||w||^2 vanishes (intercept unpenalised)", glm_grad(Xg, yp, pr.coef_, pr.intercept_, 0.3, 1) < 1e-6, f"(|grad| {glm_grad(Xg, yp, pr.coef_, pr.intercept_, 0.3, 1):.2e})")
mu = pr.predict(Xg); ybar = yp.mean()
d2 = 1 - tweedie_dev(yp, mu, 1).sum() / tweedie_dev(yp, np.full(120, ybar), 1).sum()
report("PoissonRegressor.score = D^2 = 1 - D(y, mu)/D(y, ybar) with the Poisson unit deviance 2(y log(y/mu) - y + mu)", close(pr.score(Xg, yp), d2, 1e-10), f"(D2 {d2:.6f})")
gr = GammaRegressor(alpha=0.0, **glm_kw).fit(Xg, yg); wn, bn = glm_newton(Xg, yg, 2)
report("GammaRegressor(alpha=0) = Gamma MLE with log link (Newton-Raphson)", np.allclose(gr.coef_, wn, rtol=1e-6, atol=1e-8) and close(gr.intercept_, bn, 1e-6))
gr = GammaRegressor(alpha=0.2, **glm_kw).fit(Xg, yg); mu = gr.predict(Xg)
report("GammaRegressor(alpha=0.2): gradient of the penalised mean Gamma deviance 2(log(mu/y) + y/mu - 1) vanishes; score = D^2 with that deviance", glm_grad(Xg, yg, gr.coef_, gr.intercept_, 0.2, 2) < 1e-6 and close(gr.score(Xg, yg), 1 - tweedie_dev(yg, mu, 2).sum() / tweedie_dev(yg, np.full(120, yg.mean()), 2).sum(), 1e-10))
tw = TweedieRegressor(power=1.5, alpha=0.0, link="log", **glm_kw).fit(Xg, yp); wn, bn = glm_newton(Xg, yp, 1.5)
report("TweedieRegressor(power=1.5, alpha=0, link='log') = compound-Poisson-Gamma MLE (Newton on the unit deviance 2[y^(2-p)/((1-p)(2-p)) - y mu^(1-p)/(1-p) + mu^(2-p)/(2-p)])", np.allclose(tw.coef_, wn, rtol=1e-6, atol=1e-8) and close(tw.intercept_, bn, 1e-6))
tw = TweedieRegressor(power=1.5, alpha=0.1, **glm_kw).fit(Xg, yp); mu = tw.predict(Xg)
report("TweedieRegressor(power=1.5, alpha=0.1): penalised gradient vanishes and score = D^2 with the power-1.5 unit deviance", glm_grad(Xg, yp, tw.coef_, tw.intercept_, 0.1, 1.5) < 1e-6 and close(tw.score(Xg, yp), 1 - tweedie_dev(yp, mu, 1.5).sum() / tweedie_dev(yp, np.full(120, yp.mean()), 1.5).sum(), 1e-10))
tw3 = TweedieRegressor(power=3, alpha=0.05, **glm_kw).fit(Xg, yg); mu = tw3.predict(Xg)
report("TweedieRegressor(power=3) = inverse Gaussian: unit deviance (y - mu)^2/(y mu^2), score = D^2, penalised gradient vanishes", close(tw3.score(Xg, yg), 1 - ((yg - mu) ** 2 / (yg * mu ** 2)).sum() / ((yg - yg.mean()) ** 2 / (yg * yg.mean() ** 2)).sum(), 1e-10) and glm_grad(Xg, yg, tw3.coef_, tw3.intercept_, 0.05, 3) < 1e-6)
report("TweedieRegressor(power=1) == PoissonRegressor and (power=2) == GammaRegressor at the same alpha (documented)", np.allclose(TweedieRegressor(power=1, alpha=0.3, **glm_kw).fit(Xg, yp).coef_, PoissonRegressor(alpha=0.3, **glm_kw).fit(Xg, yp).coef_, rtol=1e-8) and np.allclose(TweedieRegressor(power=2, alpha=0.2, **glm_kw).fit(Xg, yg).coef_, GammaRegressor(alpha=0.2, **glm_kw).fit(Xg, yg).coef_, rtol=1e-8))
yn = Xg @ np.array([1.0, 2.0, -1.0]) + 0.5 + 0.3 * rs.randn(120); Xgc, ync, xmg, ymg = centre(Xg, yn)
tw0 = TweedieRegressor(power=0, alpha=0.4, **glm_kw).fit(Xg, yn); wr = np.linalg.solve(Xgc.T @ Xgc / 120 + 0.4 * np.eye(3), Xgc.T @ ync / 120)
report("TweedieRegressor(power=0, link='auto' -> identity) = ridge on the 1/(2n) loss: (Xc'Xc/n + alpha I) w = Xc'yc/n", np.allclose(tw0.coef_, wr, rtol=1e-6, atol=1e-9) and close(tw0.intercept_, ymg - xmg @ wr, 1e-6), f"(link auto -> identity, coef diff {np.abs(tw0.coef_ - wr).max():.2e})")
tw0l = TweedieRegressor(power=0, alpha=0.0, link="log", **glm_kw).fit(Xg, yp); wn, bn = glm_newton(Xg, yp, 0)
report("TweedieRegressor(power=0, link='log'): Normal deviance with log link, alpha=0 = nonlinear least squares of exp(Xw+b) (Newton)", np.allclose(tw0l.coef_, wn, rtol=1e-5, atol=1e-7) and close(tw0l.intercept_, bn, 1e-5))
report("Tweedie link='auto': identity for power <= 0, log for power > 0 (predict = exp of the linear predictor for Poisson)", np.allclose(pr.predict(Xg), np.exp(Xg @ pr.coef_ + pr.intercept_)) and np.allclose(tw0.predict(Xg), Xg @ tw0.coef_ + tw0.intercept_))
try:
    twh = TweedieRegressor(power=0.5, alpha=0.1, **glm_kw).fit(Xg, yp); half_ok = glm_grad(Xg, yp, twh.coef_, twh.intercept_, 0.1, 0.5) < 1e-6; half_detail = "(fits silently; the generic power-p deviance formula still minimised)"
except ValueError as e: half_ok = True; half_detail = f"(raises ValueError: {str(e)[:60]})"
report("TweedieRegressor(power=0.5): docs say 'For 0 < power < 1, no distribution exists' but promise no error: either raises or minimises the generic deviance", half_ok, half_detail)
try:
    PoissonRegressor().fit(Xg, yp - 1); ok = False
except ValueError: ok = True
report("PoissonRegressor with negative y raises ValueError (target domain y in [0, inf))", ok)
try:
    GammaRegressor().fit(Xg, np.where(yp > 0, yp, 0)); ok = False
except ValueError: ok = True
report("GammaRegressor with a zero target raises ValueError (target domain y in (0, inf))", ok)
swg = rs.uniform(0.5, 3, 120); prw = PoissonRegressor(alpha=0.3, **glm_kw).fit(Xg, yp, sample_weight=swg)
report("PoissonRegressor sample_weight: gradient of 1/(2 sum sw) sum sw_i d_i + alpha/2 ||w||^2 vanishes (weighted average as documented)", glm_grad(Xg, yp, prw.coef_, prw.intercept_, 0.3, 1, swg) < 1e-6)
pr2 = PoissonRegressor(alpha=0.3, **glm_kw).fit(Xg, yp, sample_weight=np.full(120, 2.0)); prd = PoissonRegressor(alpha=0.3, **glm_kw).fit(np.vstack([Xg, Xg]), np.concatenate([yp, yp])); pr1 = PoissonRegressor(alpha=0.3, **glm_kw).fit(Xg, yp)
report("PoissonRegressor: sample_weight=2 == duplicated rows == single copy (weighted-average objective)", np.allclose(pr2.coef_, prd.coef_, rtol=1e-7) and np.allclose(pr2.coef_, pr1.coef_, rtol=1e-7))
mu = pr1.predict(Xg); ybar_w = np.average(yp, weights=swg)
d2w = 1 - (swg * tweedie_dev(yp, mu, 1)).sum() / (swg * tweedie_dev(yp, np.full(120, ybar_w), 1)).sum()
report("GLM score(sample_weight): D^2 = 1 - sum sw d(y, mu) / sum sw d(y, ybar_w) with ybar_w the weighted mean ('averaged by sample_weight')", close(pr1.score(Xg, yp, sample_weight=swg), d2w, 1e-10), f"(score {pr1.score(Xg, yp, sample_weight=swg):.8f} vs {d2w:.8f})")
if VER >= (1, 2):
    prc = PoissonRegressor(alpha=0.3, solver="newton-cholesky", **glm_kw).fit(Xg, yp)
    report("PoissonRegressor(solver='newton-cholesky') = lbfgs solution (same objective, both converged)", np.allclose(prc.coef_, pr1.coef_, rtol=1e-6, atol=1e-8) and close(prc.intercept_, pr1.intercept_, 1e-6))
report("PoissonRegressor(fit_intercept=False): gradient of the penalised objective in w alone vanishes", np.abs(Xg.T @ ((np.exp(Xg @ PoissonRegressor(alpha=0.3, fit_intercept=False, **glm_kw).fit(Xg, yp).coef_) - yp) / 120) + 0.3 * PoissonRegressor(alpha=0.3, fit_intercept=False, **glm_kw).fit(Xg, yp).coef_).max() < 1e-6)

# ================================================================ SGDRegressor / SGDClassifier
def sgd_epochs(X, y, loss, penalty, alpha, l1_ratio, eta0, lr, power_t, epochs, fit_intercept=True, average=0, eps=0.1, sw=None, cw=None):
    """Plain-Python replica of the documented SGD (shuffle=False): for each sample p = w.x + b,
    eta by the schedule, update = -eta * dloss(y, p), w <- w * max(0, 1 - (1-l1_ratio) eta alpha) (L2 weight decay)
    then w += update x, b += update, then the cumulative L1 shrinkage of Tsuruoka et al.; average = running mean of w."""
    n, p = X.shape; w = np.zeros(p); b = 0.0; t = 1; q = np.zeros(p); u = 0.0
    l1r = {"l2": 0.0, "l1": 1.0, "elasticnet": l1_ratio, None: 0.0}[penalty]
    aw = np.zeros(p); ab = 0.0
    if lr == "optimal":
        typw = math.sqrt(1.0 / math.sqrt(alpha)); dl = {"hinge": lambda y_, p_: -y_ if p_ * y_ <= 1 else 0.0, "squared_error": lambda y_, p_: p_ - y_, "log_loss": lambda y_, p_: 1 / (1 + math.exp(-p_)) - (1 if y_ > 0 else 0)}[loss]
        init_eta0 = typw / max(1.0, dl(1.0, -typw)); t0 = 1.0 / (init_eta0 * alpha)
    def dloss(y_, p_):
        if loss == "squared_error": return p_ - y_
        if loss == "huber": r = p_ - y_; return r if abs(r) <= eps else (eps if r > 0 else -eps)
        if loss == "epsilon_insensitive": return -1.0 if y_ - p_ > eps else (1.0 if p_ - y_ > eps else 0.0)
        if loss == "squared_epsilon_insensitive": z = y_ - p_; return -2 * (z - eps) if z > eps else (2 * (-z - eps) if z < -eps else 0.0)
        if loss == "hinge": return -y_ if p_ * y_ <= 1 else 0.0
        if loss == "squared_hinge": z = 1 - p_ * y_; return -2 * y_ * z if z > 0 else 0.0
        if loss == "perceptron": return -y_ if p_ * y_ <= 0 else 0.0
        if loss == "log_loss": return 1 / (1 + math.exp(-p_)) - (1 if y_ > 0 else 0)
        if loss == "modified_huber": z = p_ * y_; return 0.0 if z >= 1 else (2 * (1 - z) * -y_ if z >= -1 else -4 * y_)
    for ep in range(epochs):
        for i in range(n):
            pr = w @ X[i] + b
            eta = eta0 if lr == "constant" else (eta0 / t ** power_t if lr == "invscaling" else 1.0 / (alpha * (t0 + t - 1)))
            upd = -eta * min(max(dloss(y[i], pr), -1e12), 1e12)  # MAX_DLOSS clipping of the code
            if sw is not None: upd *= sw[i]
            if cw is not None: upd *= cw[1] if y[i] > 0 else cw[0]
            if penalty in ("l2", "elasticnet"): w *= max(0.0, 1.0 - (1.0 - l1r) * eta * alpha)
            w = w + upd * X[i]
            if fit_intercept: b += upd
            if 0 < average <= t:
                aw += (w - aw) / (t - average + 1); ab += (b - ab) / (t - average + 1)
            if penalty in ("l1", "elasticnet"):
                u += l1r * eta * alpha
                for j in range(p):
                    z = w[j]
                    if w[j] > 0: w[j] = max(0.0, w[j] - (u + q[j]))
                    elif w[j] < 0: w[j] = min(0.0, w[j] + (u - q[j]))
                    q[j] += w[j] - z
            t += 1
    return (aw, ab) if average else (w, b)
Xs_ = rs.randn(30, 3); ys_ = Xs_ @ np.array([1.0, -2.0, 0.5]) + 0.3 + 0.1 * rs.randn(30)
for loss in ("squared_error", "huber", "epsilon_insensitive", "squared_epsilon_insensitive"):
    for pen in ("l2", "l1", "elasticnet", None):
        m = SGDRegressor(loss=loss, penalty=pen, alpha=0.01, l1_ratio=0.3, learning_rate="constant", eta0=0.05, max_iter=3, tol=None, shuffle=False, epsilon=0.1).fit(Xs_, ys_)
        w, b = sgd_epochs(Xs_, ys_, loss, pen, 0.01, 0.3, 0.05, "constant", 0.25, 3)
        report(f"SGDRegressor(loss={loss}, penalty={pen}, constant eta, 3 epochs, no shuffle) = plain-Python SGD with the documented loss gradient and penalty updates", np.allclose(m.coef_, w, rtol=1e-10, atol=1e-12) and close(m.intercept_[0], b, 1e-10, 1e-12) and m.t_ == 1 + 3 * 30, f"(coef {np.round(m.coef_, 4)})")
m = SGDRegressor(penalty="l2", alpha=0.01, learning_rate="invscaling", eta0=0.1, power_t=0.3, max_iter=2, tol=None, shuffle=False).fit(Xs_, ys_)
w, b = sgd_epochs(Xs_, ys_, "squared_error", "l2", 0.01, 0.15, 0.1, "invscaling", 0.3, 2)
report("SGDRegressor learning_rate='invscaling': eta = eta0 / t^power_t with t = 1, 2, ... per sample (replica)", np.allclose(m.coef_, w, rtol=1e-10) and close(m.intercept_[0], b, 1e-10))
m = SGDRegressor(penalty="l2", alpha=1.0, learning_rate="optimal", max_iter=2, tol=None, shuffle=False).fit(Xs_, ys_)
w, b = sgd_epochs(Xs_, ys_, "squared_error", "l2", 1.0, 0.15, 0.01, "optimal", 0.25, 2)
report("SGDRegressor learning_rate='optimal' (alpha=1): eta = 1/(alpha (t0 + t - 1)), t = 1, 2, ..., with Bottou's t0 = 1/(alpha eta_init), eta_init = typw/max(1, dloss(1, -typw)), typw = sqrt(1/sqrt(alpha)) (heuristic only 'documented' in the code; replica)", np.allclose(m.coef_, w, rtol=1e-10) and close(m.intercept_[0], b, 1e-10), f"(t0 = {1.0 / (math.sqrt(1 / math.sqrt(1.0)) * 1.0):.4f})")
Xcl0 = rs.randn(40, 3); ycl0 = np.where(Xcl0 @ np.array([1.0, -1.0, 0.5]) > 0, 1, -1)
m = SGDClassifier(loss="hinge", penalty="l2", alpha=0.01, learning_rate="optimal", max_iter=3, tol=None, shuffle=False).fit(Xcl0, ycl0)
w, b = sgd_epochs(Xcl0, ycl0.astype(float), "hinge", "l2", 0.01, 0.15, 0.01, "optimal", 0.25, 3)
report("SGDClassifier(hinge, learning_rate='optimal' default, alpha=0.01, 3 epochs): t0 = 1/(alpha typw) since dloss(1, -typw) = -1 for hinge (replica)", np.allclose(m.coef_[0], w, rtol=1e-10) and close(m.intercept_[0], b, 1e-10), f"(t0 = {1.0 / (math.sqrt(1 / math.sqrt(0.01)) * 0.01):.4f})")
m = SGDRegressor(penalty=None, learning_rate="constant", eta0=0.02, max_iter=4, tol=None, shuffle=False, average=True).fit(Xs_, ys_)
w, b = sgd_epochs(Xs_, ys_, "squared_error", None, 0.0, 0.0, 0.02, "constant", 0.25, 4, average=1)
report("SGDRegressor(average=True): coef_ = mean of the weight vectors over all T updates (documented 1/T sum w^(t))", np.allclose(m.coef_, w, rtol=1e-10) and close(m.intercept_[0], b, 1e-10))
m = SGDRegressor(penalty=None, learning_rate="constant", eta0=0.02, max_iter=4, tol=None, shuffle=False, average=50).fit(Xs_, ys_)
w, b = sgd_epochs(Xs_, ys_, "squared_error", None, 0.0, 0.0, 0.02, "constant", 0.25, 4, average=50)
report("SGDRegressor(average=50): averaging starts once 50 samples have been seen", np.allclose(m.coef_, w, rtol=1e-10) and close(m.intercept_[0], b, 1e-10))
m = SGDRegressor(penalty="l2", alpha=0.01, learning_rate="constant", eta0=0.05, max_iter=2, tol=None, shuffle=False).fit(Xs_, ys_, sample_weight=swb[:30])
w, b = sgd_epochs(Xs_, ys_, "squared_error", "l2", 0.01, 0.15, 0.05, "constant", 0.25, 2, sw=swb[:30])
report("SGDRegressor sample_weight: the per-sample update is multiplied by the weight (replica)", np.allclose(m.coef_, w, rtol=1e-10) and close(m.intercept_[0], b, 1e-10))
report("SGDRegressor / SGDClassifier documented default alpha = 0.0001, eta0 = 0.01, power_t = 0.25, epsilon = 0.1, learning_rate invscaling (regressor) / optimal (classifier)", SGDRegressor().alpha == 1e-4 and SGDClassifier().alpha == 1e-4 and SGDRegressor().eta0 == 0.01 and SGDRegressor().power_t == 0.25 and SGDRegressor().epsilon == 0.1 and SGDRegressor().learning_rate == "invscaling" and SGDClassifier().learning_rate == "optimal")
# many epochs, small eta -> closed form
Xbig = rs.randn(200, 3); ybig = Xbig @ np.array([1.0, -2.0, 0.5]) + 0.3 + 0.1 * rs.randn(200); wo, bo = ols(Xbig, ybig)
m = SGDRegressor(penalty=None, learning_rate="constant", eta0=0.005, max_iter=3000, tol=None, shuffle=True, random_state=0).fit(Xbig, ybig)
report("SGDRegressor(penalty=None, small constant eta, 3000 epochs) approaches OLS within 1e-2", np.allclose(m.coef_, wo, atol=1e-2) and close(m.intercept_[0], bo, 1e-2, 1e-2), f"(max |diff| {np.abs(m.coef_ - wo).max():.2e})")
m = SGDRegressor(penalty="l2", alpha=0.1, learning_rate="constant", eta0=0.002, max_iter=3000, tol=None, shuffle=True, random_state=0, average=True).fit(Xbig, ybig)
A = np.hstack([Xbig, np.ones((200, 1))]); H = A.T @ A / 200 + 0.1 * np.diag([1, 1, 1, 0]); wr = np.linalg.solve(H, A.T @ ybig / 200)
report("SGDRegressor(penalty='l2', alpha=0.1, averaged, small eta) approaches the minimiser of 1/n sum 1/2 (y - xw - b)^2 + alpha/2 ||w||^2 (intercept unpenalised) within 1e-2", np.allclose(m.coef_, wr[:3], atol=1e-2) and close(m.intercept_[0], wr[3], 1e-2, 1e-2), f"(max |diff| {np.abs(m.coef_ - wr[:3]).max():.2e})")
# classifier
Xcl = rs.randn(40, 3); ycl = np.where(Xcl @ np.array([1.0, -1.0, 0.5]) + 0.2 * rs.randn(40) > 0, 1, -1)
for loss in ("hinge", "squared_hinge", "log_loss", "modified_huber", "perceptron"):
    m = SGDClassifier(loss=loss, penalty="l2", alpha=0.01, learning_rate="constant", eta0=0.1, max_iter=2, tol=None, shuffle=False).fit(Xcl, ycl)
    w, b = sgd_epochs(Xcl, ycl.astype(float), loss, "l2", 0.01, 0.15, 0.1, "constant", 0.25, 2)
    report(f"SGDClassifier(loss={loss}, 2 epochs, no shuffle) = plain-Python SGD with the documented loss gradient (y in -1/+1)", np.allclose(m.coef_[0], w, rtol=1e-10, atol=1e-12) and close(m.intercept_[0], b, 1e-10, 1e-12))
m = SGDClassifier(loss="hinge", alpha=0.01, learning_rate="constant", eta0=0.1, max_iter=2, tol=None, shuffle=False, class_weight={-1: 1.0, 1: 3.0}).fit(Xcl, ycl)
w, b = sgd_epochs(Xcl, ycl.astype(float), "hinge", "l2", 0.01, 0.15, 0.1, "constant", 0.25, 2, cw={0: 1.0, 1: 3.0})
report("SGDClassifier class_weight: the update of a sample is multiplied by its class weight (replica)", np.allclose(m.coef_[0], w, rtol=1e-10) and close(m.intercept_[0], b, 1e-10))
m = SGDClassifier(loss="log_loss", alpha=0.01, learning_rate="constant", eta0=0.1, max_iter=5, tol=None, shuffle=False).fit(Xcl, ycl)
report("SGDClassifier(loss='log_loss') predict_proba = sigmoid(decision_function), classes_ sorted", np.allclose(m.predict_proba(Xcl)[:, 1], 1 / (1 + np.exp(-m.decision_function(Xcl)))) and list(m.classes_) == [-1, 1])
m = SGDClassifier(loss="modified_huber", alpha=0.01, learning_rate="constant", eta0=0.1, max_iter=5, tol=None, shuffle=False).fit(Xcl, ycl)
report("SGDClassifier(loss='modified_huber') predict_proba = (clip(decision, -1, 1) + 1)/2", np.allclose(m.predict_proba(Xcl)[:, 1], (np.clip(m.decision_function(Xcl), -1, 1) + 1) / 2))
m = SGDClassifier(loss="hinge", learning_rate="constant", eta0=0.1, max_iter=2, tol=None, shuffle=False).fit(Xcl, ycl)
report("SGDClassifier t_ = n_iter_ * n_samples + 1 (documented)", m.t_ == m.n_iter_ * 40 + 1, f"(t_ {m.t_}, n_iter_ {m.n_iter_})")
y3 = rs.randint(0, 3, 40); m3 = SGDClassifier(loss="hinge", alpha=0.01, learning_rate="constant", eta0=0.1, max_iter=2, tol=None, shuffle=False).fit(Xcl, y3)
ok3 = all(np.allclose(m3.coef_[k], sgd_epochs(Xcl, np.where(y3 == k, 1.0, -1.0), "hinge", "l2", 0.01, 0.15, 0.1, "constant", 0.25, 2)[0], rtol=1e-10) for k in range(3))
report("SGDClassifier multiclass = one-vs-all: coef_[k] is the binary SGD of class k vs the rest (replica), predict = argmax decision", ok3 and np.all(m3.predict(Xcl) == m3.classes_[m3.decision_function(Xcl).argmax(1)]))

# ================================================================ PassiveAggressive / Perceptron (one-step update rules)
x1 = np.array([[0.5, -1.0, 2.0]]); sq = float((x1 @ x1.T).item())
for C in (1.0, 0.1):
    pa = PassiveAggressiveClassifier(C=C, loss="hinge", max_iter=1, tol=None, shuffle=False); pa.partial_fit(x1, [1], classes=[-1, 1])
    tau = min(C, 1.0 / sq)
    report(f"PassiveAggressiveClassifier(C={C}, hinge = PA-I) one step from w=0 on (x, y=+1): loss = 1, w = min(C, loss/||x||^2) y x, intercept = same tau (intercept not in ||x||^2)", np.allclose(pa.coef_[0], tau * x1[0], rtol=1e-12) and close(pa.intercept_[0], tau, 1e-12), f"(tau {tau:.4f})")
    pa2 = PassiveAggressiveClassifier(C=C, loss="squared_hinge", max_iter=1, tol=None, shuffle=False); pa2.partial_fit(x1, [-1], classes=[-1, 1])
    tau2 = 1.0 / (sq + 1 / (2 * C))
    report(f"PassiveAggressiveClassifier(C={C}, squared_hinge = PA-II) one step on (x, y=-1): w = loss/(||x||^2 + 1/(2C)) y x", np.allclose(pa2.coef_[0], -tau2 * x1[0], rtol=1e-12) and close(pa2.intercept_[0], -tau2, 1e-12))
pa = PassiveAggressiveClassifier(C=1.0, max_iter=1, tol=None, shuffle=False); pa.partial_fit(x1, [1], classes=[-1, 1]); pa.partial_fit(x1, [1])
report("PassiveAggressiveClassifier: a second step on a correctly classified sample with margin >= 1 is passive (no change)", np.allclose(pa.coef_[0], min(1.0, 1 / sq) * x1[0]) if min(1.0, 1 / sq) * (sq + 1) >= 1 else True)
par = PassiveAggressiveRegressor(C=0.5, epsilon=0.1, loss="epsilon_insensitive", max_iter=1, tol=None, shuffle=False); par.partial_fit(x1, [3.0])
tau = min(0.5, (3.0 - 0.1) / sq)
report("PassiveAggressiveRegressor(C=0.5, epsilon=0.1, PA-I) one step from 0 on (x, y=3): loss = |y - 0| - eps, w = min(C, loss/||x||^2) sign(y - p) x", np.allclose(par.coef_, tau * x1[0], rtol=1e-12) and close(par.intercept_[0], tau, 1e-12))
par2 = PassiveAggressiveRegressor(C=0.5, epsilon=0.1, loss="squared_epsilon_insensitive", max_iter=1, tol=None, shuffle=False); par2.partial_fit(x1, [-3.0])
tau2 = (3.0 - 0.1) / (sq + 1 / (2 * 0.5))
report("PassiveAggressiveRegressor(PA-II) one step on (x, y=-3): w = loss/(||x||^2 + 1/(2C)) sign(y - p) x", np.allclose(par2.coef_, -tau2 * x1[0], rtol=1e-12) and close(par2.intercept_[0], -tau2, 1e-12))
pc = Perceptron(eta0=0.7, max_iter=2, tol=None, shuffle=False).fit(Xcl, ycl); w, b = sgd_epochs(Xcl, ycl.astype(float), "perceptron", None, 0.0, 0.0, 0.7, "constant", 0.5, 2)
report("Perceptron(eta0=0.7, 2 epochs, no shuffle): w += eta0 y x, b += eta0 y whenever y (w.x + b) <= 0, no penalty by default (replica)", np.allclose(pc.coef_[0], w, rtol=1e-12) and close(pc.intercept_[0], b, 1e-12) and pc.penalty is None)
pc1 = Perceptron(max_iter=1, tol=None, shuffle=False); pc1.partial_fit(x1, [1], classes=[-1, 1])
report("Perceptron one step from 0 on (x, y=+1) with the default eta0=1: w = x, intercept = 1", np.allclose(pc1.coef_[0], x1[0]) and pc1.intercept_[0] == 1.0)

# ================================================================ RANSACRegressor
from sklearn.utils import check_random_state
from sklearn.utils.random import sample_without_replacement
def ransac_ref(X, y, seed, min_samples, thr, max_trials=100, prob=0.99, stop_n=np.inf):
    """Plain re-implementation of the documented RANSAC loop with OLS as the base model (uses sklearn's
    sample_without_replacement only to draw the same subsets)."""
    n = len(y); rng = check_random_state(seed); n_best = 1; score_best = -np.inf; mask_best = None; trials = 0; mt = max_trials
    while trials < mt:
        trials += 1; idx = sample_without_replacement(n, min_samples, random_state=rng)
        w, b = ols(X[idx], y[idx]); res = np.abs(y - X @ w - b); mask = res <= thr; n_in = mask.sum()
        if n_in < n_best: continue
        yi = y[mask]; pi = X[mask] @ w + b; sc = 1 - ((yi - pi) ** 2).sum() / ((yi - yi.mean()) ** 2).sum()
        if n_in == n_best and sc < score_best: continue
        n_best, score_best, mask_best = n_in, sc, mask
        ir = n_best / n; nom = max(np.finfo(float).eps, 1 - prob); den = max(np.finfo(float).eps, 1 - ir ** min_samples)
        dyn = 0 if nom == 1 else (np.inf if den == 1 else abs(math.ceil(math.log(nom) / math.log(den)))); mt = min(mt, dyn)
        if n_best >= stop_n: break
    w, b = ols(X[mask_best], y[mask_best]); return mask_best, trials, w, b
Xr = rs.randn(60, 2); yr = Xr @ np.array([2.0, -1.0]) + 1.0 + 0.1 * rs.randn(60); yr[:12] += rs.choice([-1, 1], 12) * rs.uniform(5, 10, 12)
mad = np.median(np.abs(yr - np.median(yr)))
rr = RANSACRegressor(random_state=3).fit(Xr, yr); mask, trials, w, b = ransac_ref(Xr, yr, 3, 3, mad)
report("RANSACRegressor defaults: min_samples = n_features + 1, residual_threshold = MAD of y = median|y - median(y)|, absolute_error loss; inlier_mask_, n_trials_, estimator_ = plain replica of the documented loop", np.array_equal(rr.inlier_mask_, mask) and rr.n_trials_ == trials and np.allclose(rr.estimator_.coef_, w, rtol=1e-10), f"(MAD {mad:.4f}, inliers {mask.sum()}, trials {trials})")
report("RANSAC estimator_ is refit on the consensus set (OLS on inlier_mask_) and the 12 planted outliers are excluded", np.allclose(rr.estimator_.coef_, ols(Xr[rr.inlier_mask_], yr[rr.inlier_mask_])[0], rtol=1e-10) and not rr.inlier_mask_[:12].any())
n_in = rr.inlier_mask_.sum(); dyn = math.ceil(math.log(1 - 0.99) / math.log(1 - (n_in / 60) ** 3))
report("RANSAC n_trials_ >= N = ceil(log(1 - stop_probability)/log(1 - e^min_samples)) with e = final inlier fraction, and <= max_trials", dyn <= rr.n_trials_ <= 100, f"(N {dyn}, n_trials_ {rr.n_trials_})")
rr2 = RANSACRegressor(random_state=5, residual_threshold=0.5, min_samples=0.1, stop_probability=0.999, max_trials=40).fit(Xr, yr); mask, trials, w, b = ransac_ref(Xr, yr, 5, 6, 0.5, 40, 0.999)
report("RANSAC(min_samples=0.1 -> ceil(0.1 n) = 6, residual_threshold=0.5, stop_probability=0.999, max_trials=40) = replica", np.array_equal(rr2.inlier_mask_, mask) and rr2.n_trials_ == trials, f"(trials {trials}, inliers {mask.sum()})")
rr3 = RANSACRegressor(random_state=1, residual_threshold=0.5, stop_n_inliers=45).fit(Xr, yr); mask, trials, w, b = ransac_ref(Xr, yr, 1, 3, 0.5, stop_n=45)
report("RANSAC(stop_n_inliers=45) stops at the first trial reaching 45 inliers (replica)", rr3.n_trials_ == trials and np.array_equal(rr3.inlier_mask_, mask), f"(trials {trials})")
resid = np.abs(yr - rr2.predict(Xr)); rr_sq = RANSACRegressor(random_state=5, residual_threshold=0.25, loss="squared_error", min_samples=6, stop_probability=0.999, max_trials=40).fit(Xr, yr)
mask_sq, trials_sq, _, _ = ransac_ref(Xr, yr, 5, 6, 0.5, 40, 0.999)
report("RANSAC loss='squared_error' with threshold 0.25 = absolute_error with threshold 0.5 (same subsets, r^2 <= 0.25 <=> |r| <= 0.5)", np.array_equal(rr_sq.inlier_mask_, mask_sq) and rr_sq.n_trials_ == trials_sq)
report("RANSAC: 'points whose residuals are strictly equal to the threshold are considered as inliers' (<=): exact-threshold residual is an inlier", RANSACRegressor(random_state=0, residual_threshold=1.0, min_samples=2).fit(np.array([[0.], [1.], [2.], [3.]]), np.array([0., 1., 2., 4.])).inlier_mask_[3])

# ================================================================ TheilSenRegressor
xt = rs.uniform(1, 3, 15); yt = 2.0 * xt + rs.standard_t(2, 15) * 0.3
ts = TheilSenRegressor(fit_intercept=False, random_state=0).fit(xt[:, None], yt)
report("TheilSen(fit_intercept=False, 1 feature): n_subsamples = 1, coef = median of the n slopes y_i/x_i (spatial median in 1-D = median)", close(ts.coef_[0], np.median(yt / xt), 1e-12) and ts.n_subpopulation_ == 15, f"(coef {ts.coef_[0]:.6f})")
def weiszfeld(P, iters=100000, tol=1e-15):
    m = P.mean(0)
    for _ in range(iters):
        d = np.sqrt(((P - m) ** 2).sum(1)); nz = d > 1e-14
        if not nz.all(): break
        new = (P[nz] / d[nz, None]).sum(0) / (1 / d[nz]).sum()
        if np.abs(new - m).max() < tol: m = new; break
        m = new
    return m
Xt2 = rs.randn(12, 2); yt2 = Xt2 @ np.array([1.5, -0.5]) + 1.0 + 0.2 * rs.randn(12); yt2[0] += 6
P = np.array([np.concatenate([[b_], w_]) for s3 in itertools.combinations(range(12), 3) for w_, b_ in [ols(Xt2[list(s3)], yt2[list(s3)])]])
ts2 = TheilSenRegressor(tol=1e-13, max_iter=100000, random_state=0).fit(Xt2, yt2); sm = weiszfeld(P)
report("TheilSen(12 samples, 2 features): all C(12,3)=220 subset OLS fits (n_subsamples = n_features + 1), (intercept_, coef_) = spatial (L1) median of the fits by my own Weiszfeld iteration", ts2.n_subpopulation_ == 220 and close(ts2.intercept_, sm[0], 1e-6, 1e-8) and np.allclose(ts2.coef_, sm[1:], rtol=1e-6, atol=1e-8), f"(coef {np.round(ts2.coef_, 6)} vs {np.round(sm[1:], 6)})")
obj_sk = np.sqrt(((P - np.concatenate([[ts2.intercept_], ts2.coef_])) ** 2).sum(1)).sum(); obj_ref = np.sqrt(((P - sm) ** 2).sum(1)).sum()
report("TheilSen spatial median: sum of Euclidean distances to the subset fits is minimal (<= mine + 1e-9)", obj_sk <= obj_ref + 1e-9, f"({obj_sk:.9f} vs {obj_ref:.9f})")
report("TheilSen breakdown_ = 1 - (0.5^(1/k) (n - k + 1) + k - 1)/n with k = n_subsamples", close(ts2.breakdown_, 1 - (0.5 ** (1 / 3) * (12 - 3 + 1) + 3 - 1) / 12, 1e-12), f"({ts2.breakdown_:.5f})")
tsn = TheilSenRegressor(n_subsamples=12, random_state=0).fit(Xt2, yt2); wo, bo = ols(Xt2, yt2)
report("TheilSen(n_subsamples=n_samples) is identical to least squares (documented)", np.allclose(tsn.coef_, wo, rtol=1e-8) and close(tsn.intercept_, bo, 1e-8))
tsm = TheilSenRegressor(max_subpopulation=50, random_state=0).fit(Xt2, yt2)
report("TheilSen(max_subpopulation=50 < C(12,3)): n_subpopulation_ = 50 random subsets", tsm.n_subpopulation_ == 50)

# ================================================================ RidgeCV (leave-one-out closed form vs explicit loop)
def ridge_fit(X, y, alpha, sw=None):
    Xc_, yc_, xm_, ym_ = centre(X, y, sw); W = np.ones(len(y)) if sw is None else sw
    w = np.linalg.solve(Xc_.T @ (W[:, None] * Xc_) + alpha * np.eye(X.shape[1]), Xc_.T @ (W * yc_)); return w, ym_ - xm_ @ w
Xrc = rs.randn(30, 4); Yrc = np.column_stack([Xrc @ np.array([1, -1, 0.5, 0]) + 0.5 * rs.randn(30) + 1, Xrc @ np.array([0, 0, 1, 2.0]) + 2 * rs.randn(30)])
alphas = np.array([0.1, 1.0, 10.0, 100.0])
loo = np.zeros((30, 2, 4))
for j, a in enumerate(alphas):
    for i in range(30):
        tr = np.arange(30) != i
        for k in range(2):
            w, b = ridge_fit(Xrc[tr], Yrc[tr, k], a); loo[i, k, j] = (Yrc[i, k] - Xrc[i] @ w - b) ** 2
rcv = ridgecv(store=True, alphas=alphas).fit(Xrc, Yrc[:, 0])
report("RidgeCV(cv=None, store): cv_results_ (n_samples, n_alphas) = squared leave-one-out errors of an explicit LOO loop (ridge with unpenalised intercept)", cvres(rcv).shape == (30, 4) and np.allclose(cvres(rcv), loo[:, 0, :], rtol=1e-8, atol=1e-10), f"(max diff {np.abs(cvres(rcv) - loo[:, 0, :]).max():.2e})")
report("RidgeCV alpha_ = argmin of the mean LOO MSE, best_score_ = -mean MSE (scoring=None -> neg MSE), coef_ = ridge at alpha_", close(rcv.alpha_, alphas[np.argmin(loo[:, 0, :].mean(0))], 1e-12) and close(rcv.best_score_, -loo[:, 0, :].mean(0).min(), 1e-10) and np.allclose(rcv.coef_, ridge_fit(Xrc, Yrc[:, 0], rcv.alpha_)[0], rtol=1e-9), f"(alpha_ {rcv.alpha_})")
rcv2 = ridgecv(store=True, alphas=alphas, alpha_per_target=True).fit(Xrc, Yrc)
report("RidgeCV multi-target alpha_per_target=True: cv_results_ shape (n_samples, n_targets, n_alphas), alpha_ per target = argmin of each target's LOO MSE", cvres(rcv2).shape == (30, 2, 4) and np.allclose(cvres(rcv2), loo, rtol=1e-8, atol=1e-10) and np.allclose(rcv2.alpha_, alphas[np.argmin(loo.mean(0), axis=1)]) and rcv2.alpha_.shape == (2,), f"(alpha_ {rcv2.alpha_})")
rcv3 = ridgecv(store=True, alphas=alphas).fit(Xrc, Yrc)
report("RidgeCV multi-target alpha_per_target=False: one alpha_ = argmin of the LOO MSE averaged over samples AND targets", np.isscalar(rcv3.alpha_) and close(rcv3.alpha_, alphas[np.argmin(loo.mean((0, 1)))], 1e-12) and close(rcv3.best_score_, -loo.mean((0, 1)).min(), 1e-10))
rcv4 = ridgecv(store=True, alphas=alphas, scoring="r2").fit(Xrc, Yrc[:, 0]); pred_loo = Yrc[:, 0, None] - np.sqrt(loo[:, 0, :]) * np.sign(Yrc[:, 0, None] - (Yrc[:, 0, None] - np.sqrt(loo[:, 0, :])))
r2s = []
for j, a in enumerate(alphas):
    pr_ = np.array([Yrc[i, 0] - (Yrc[i, 0] - (Xrc[i] @ ridge_fit(Xrc[np.arange(30) != i], Yrc[np.arange(30) != i, 0], a)[0] + ridge_fit(Xrc[np.arange(30) != i], Yrc[np.arange(30) != i, 0], a)[1])) for i in range(30)])
    r2s.append(1 - ((Yrc[:, 0] - pr_) ** 2).sum() / ((Yrc[:, 0] - Yrc[:, 0].mean()) ** 2).sum()); pred_loo[:, j] = pr_
conv = "original-y scale" if np.allclose(cvres(rcv4), pred_loo, rtol=1e-8) else ("centred-y scale (prediction - mean(y))" if np.allclose(cvres(rcv4) + Yrc[:, 0].mean(), pred_loo, rtol=1e-8) else "neither")
report("RidgeCV(scoring='r2', cv=None): cv_results_ holds the LOO predictions ('standardized per point prediction values': original or centred y scale), alpha_ maximises R2 of the LOO predictions vs y, best_score_ = that R2", conv != "neither" and close(rcv4.alpha_, alphas[np.argmax(r2s)], 1e-12) and close(rcv4.best_score_, max(r2s), 1e-10), f"(cv_results_ in the {conv}; r2 {np.round(r2s, 4)})")
swr = rs.uniform(0.5, 2, 30); rcvw = ridgecv(store=True, alphas=alphas).fit(Xrc, Yrc[:, 0], sample_weight=swr)
loow = np.zeros((30, 4)); loow_raw = np.zeros((30, 4))
for j, a in enumerate(alphas):
    for i in range(30):
        tr = np.arange(30) != i; w, b = ridge_fit(Xrc[tr], Yrc[tr, 0], a, swr[tr]); e2 = (Yrc[i, 0] - Xrc[i] @ w - b) ** 2; loow[i, j] = swr[i] * e2; loow_raw[i, j] = e2
report("RidgeCV sample_weight LOO: cv_results_[i] = sw_i * (LOO error of the weighted ridge without sample i)^2 and best_score_ = -mean of those (the 'looe <- sqrt(s) looe' rescaling)", np.allclose(cvres(rcvw), loow, rtol=1e-8, atol=1e-10) and close(rcvw.best_score_, -loow.mean(0).min(), 1e-10), f"(max diff weighted {np.abs(cvres(rcvw) - loow).max():.2e}, unweighted {np.abs(cvres(rcvw) - loow_raw).max():.2e})")
rcvi = ridgecv(store=True, alphas=alphas, fit_intercept=False).fit(Xrc, Yrc[:, 0])
loo0 = np.array([[(Yrc[i, 0] - Xrc[i] @ np.linalg.solve(Xrc[np.arange(30) != i].T @ Xrc[np.arange(30) != i] + a * np.eye(4), Xrc[np.arange(30) != i].T @ Yrc[np.arange(30) != i, 0])) ** 2 for a in alphas] for i in range(30)])
report("RidgeCV(fit_intercept=False) LOO = explicit loop without centring", np.allclose(cvres(rcvi), loo0, rtol=1e-8, atol=1e-10))
for mode in ("svd", "eigen"):
    r_ = ridgecv(store=True, alphas=alphas, gcv_mode=mode).fit(Xrc, Yrc[:, 0])
    report(f"RidgeCV(gcv_mode='{mode}') = the same LOO errors", np.allclose(cvres(r_), loo[:, 0, :], rtol=1e-8, atol=1e-10))
r_wide = ridgecv(store=True, alphas=alphas).fit(Xbw, ybw)
loo_w = np.array([[(ybw[i] - Xbw[i] @ ridge_fit(Xbw[np.arange(6) != i], ybw[np.arange(6) != i], a)[0] - ridge_fit(Xbw[np.arange(6) != i], ybw[np.arange(6) != i], a)[1]) ** 2 for a in alphas] for i in range(6)])
report("RidgeCV with n_samples < n_features (6 x 10, Gram branch): LOO errors = explicit loop", np.allclose(cvres(r_wide), loo_w, rtol=1e-7, atol=1e-9), f"(max diff {np.abs(cvres(r_wide) - loo_w).max():.2e})")
rcvk = RidgeCV(alphas=alphas, cv=KFold(5)).fit(Xrc, Yrc[:, 0])
r2k = []
for a in alphas:
    sc = []
    for tr, te in KFold(5).split(Xrc):
        w, b = ridge_fit(Xrc[tr], Yrc[tr, 0], a); pr_ = Xrc[te] @ w + b; sc.append(1 - ((Yrc[te, 0] - pr_) ** 2).sum() / ((Yrc[te, 0] - Yrc[te, 0].mean()) ** 2).sum())
    r2k.append(np.mean(sc))
report("RidgeCV(cv=KFold(5)): scoring=None -> R2 per fold (documented), alpha_ = argmax of the fold-mean R2, best_score_ = that mean", close(rcvk.alpha_, alphas[np.argmax(r2k)], 1e-12) and close(rcvk.best_score_, max(r2k), 1e-10), f"(mean R2 {np.round(r2k, 4)})")
try:
    ridgecv(store=True, alphas=alphas, cv=3).fit(Xrc, Yrc[:, 0]); ok = False
except ValueError: ok = True
report("RidgeCV store_cv_results=True with cv != None raises ValueError (documented 'only compatible with cv=None')", ok)

# ================================================================ LassoCV / ElasticNetCV
Xcv = rs.randn(45, 4); ycv = Xcv @ np.array([1.5, 0, -1.0, 0]) + 0.5 * rs.randn(45) + 2
lcv = LassoCV(cv=3, tol=1e-12, max_iter=100000, **nalph(12)).fit(Xcv, ycv); Xcvc, ycvc, _, _ = centre(Xcv, ycv)
amax = np.max(np.abs(Xcvc.T @ ycvc)) / 45
report("LassoCV alphas_ = grid from alpha_max = max|Xc'yc|/n of the FULL data (centred) down to eps*alpha_max, n_alphas points", np.allclose(lcv.alphas_, np.geomspace(amax, amax * 1e-3, 12), rtol=1e-12))
mse_ref = np.zeros((12, 3))
for k, (tr, te) in enumerate(KFold(3).split(Xcv)):
    for j, a in enumerate(lcv.alphas_):
        w, b = enet_cd(Xcv[tr], ycv[tr], a, 1.0, tol=1e-13); mse_ref[j, k] = np.mean((ycv[te] - Xcv[te] @ w - b) ** 2)
report("LassoCV(cv=3): mse_path_[j, k] = test MSE on KFold(3) fold k of a Lasso(alphas_[j]) fitted on the training fold (plain CD reference), alpha_ = argmin of the fold mean", lcv.mse_path_.shape == (12, 3) and np.allclose(lcv.mse_path_, mse_ref, rtol=1e-6, atol=1e-9) and close(lcv.alpha_, lcv.alphas_[np.argmin(mse_ref.mean(1))], 1e-12), f"(max diff {np.abs(lcv.mse_path_ - mse_ref).max():.2e}, alpha_ {lcv.alpha_:.5f})")
w, b = enet_cd(Xcv, ycv, lcv.alpha_, 1.0)
report("LassoCV coef_ = Lasso(alpha_) refit on all the data (plain CD)", np.allclose(lcv.coef_, w, atol=1e-8) and close(lcv.intercept_, b, 1e-9))
ecv = ElasticNetCV(l1_ratio=[0.3, 0.8], cv=3, tol=1e-12, max_iter=100000, **nalph(6)).fit(Xcv, ycv)
mse_ref = np.zeros((2, 6, 3)); grids = [np.geomspace(amax / r_, amax / r_ * 1e-3, 6) for r_ in (0.3, 0.8)]
for li, r_ in enumerate((0.3, 0.8)):
    for k, (tr, te) in enumerate(KFold(3).split(Xcv)):
        for j, a in enumerate(grids[li]):
            w, b = enet_cd(Xcv[tr], ycv[tr], a, r_, tol=1e-13); mse_ref[li, j, k] = np.mean((ycv[te] - Xcv[te] @ w - b) ** 2)
best = np.unravel_index(np.argmin(mse_ref.mean(2)), (2, 6))
report("ElasticNetCV(l1_ratio=[0.3, 0.8]): alphas_ shape (2, 6) with alpha_max/l1_ratio per ratio, mse_path_ (2, 6, 3) = plain CD reference, (l1_ratio_, alpha_) = argmin of the fold mean", ecv.alphas_.shape == (2, 6) and np.allclose(ecv.alphas_, np.array(grids), rtol=1e-12) and ecv.mse_path_.shape == (2, 6, 3) and np.allclose(ecv.mse_path_, mse_ref, rtol=1e-6, atol=1e-9) and close(ecv.l1_ratio_, (0.3, 0.8)[best[0]], 1e-12) and close(ecv.alpha_, grids[best[0]][best[1]], 1e-12), f"(l1_ratio_ {ecv.l1_ratio_}, alpha_ {ecv.alpha_:.5f})")
lcva = LassoCV(alphas=[0.5, 0.05, 0.005], cv=3, tol=1e-12, max_iter=100000).fit(Xcv, ycv)
report("LassoCV(alphas=...): alphas_ sorted decreasing, mse_path_ rows in that order", np.all(lcva.alphas_ == np.array([0.5, 0.05, 0.005])) and lcva.mse_path_.shape == (3, 3))
lcvp = LassoCV(cv=3, positive=True, tol=1e-12, max_iter=100000, **nalph(8)).fit(Xcv, ycv)
report("LassoCV(positive=True): coef_ >= 0 and the refit satisfies the positive-Lasso KKT at alpha_", np.all(lcvp.coef_ >= 0) and kkt_enet(Xcvc, ycvc, lcvp.coef_, lcvp.alpha_, positive=True) < 1e-8)

# ================================================================ MultiTaskLasso / MultiTaskElasticNet (row-wise L21 KKT)
Ymt = np.column_stack([Xcv @ np.array([1.5, 0, -1.0, 0]) + 0.3 * rs.randn(45), Xcv @ np.array([-1.0, 0, 0.5, 0]) + 0.3 * rs.randn(45)])
Xmc, Ymc, _, _ = centre(Xcv, Ymt)
def kkt_l21(Xc_, Yc_, W, alpha, l1r=1.0):
    G = -Xc_.T @ (Yc_ - Xc_ @ W) / len(Yc_) + alpha * (1 - l1r) * W; v = 0.0
    for j in range(W.shape[0]):
        nrm_ = np.linalg.norm(W[j])
        if nrm_ > 0: v = max(v, np.abs(G[j] + alpha * l1r * W[j] / nrm_).max())
        else: v = max(v, max(0.0, np.linalg.norm(G[j]) - alpha * l1r))
    return v
mt = MultiTaskLasso(alpha=0.1, tol=1e-12, max_iter=100000).fit(Xcv, Ymt); W = mt.coef_.T
report("MultiTaskLasso(alpha=0.1): coef_ shape (n_tasks, n_features); KKT of 1/(2n)||Y - XW||_Fro^2 + alpha ||W||_21 hold row-wise: G_j + alpha W_j/||W_j|| = 0 for active rows, ||G_j|| <= alpha for zero rows", mt.coef_.shape == (2, 4) and kkt_l21(Xmc, Ymc, W, 0.1) < 1e-9, f"(violation {kkt_l21(Xmc, Ymc, W, 0.1):.2e}, zero rows {np.where(np.all(W == 0, axis=1))[0].tolist()})")
report("MultiTaskLasso: rows are zero jointly across tasks (structured sparsity) and intercept_ = mean(Y) - mean(X) @ W", np.all(np.all(W == 0, axis=1) | np.all(W != 0, axis=1)) and np.allclose(mt.intercept_, Ymt.mean(0) - Xcv.mean(0) @ W, atol=1e-12))
mte = MultiTaskElasticNet(alpha=0.1, l1_ratio=0.4, tol=1e-12, max_iter=100000).fit(Xcv, Ymt)
report("MultiTaskElasticNet(alpha=0.1, l1_ratio=0.4): KKT of 1/(2n)||Y-XW||^2 + a l1 ||W||_21 + a(1-l1)/2 ||W||_Fro^2", kkt_l21(Xmc, Ymc, mte.coef_.T, 0.1, 0.4) < 1e-9, f"(violation {kkt_l21(Xmc, Ymc, mte.coef_.T, 0.1, 0.4):.2e})")
mt1 = MultiTaskLasso(alpha=0.1, tol=1e-12, max_iter=100000).fit(Xcv, Ymt[:, :1]); w1, _ = enet_cd(Xcv, Ymt[:, 0], 0.1)
report("MultiTaskLasso with a single task = Lasso (||W||_21 = ||w||_1)", np.allclose(mt1.coef_[0], w1, atol=1e-8))
amax21 = np.max(np.linalg.norm(Xmc.T @ Ymc, axis=1)) / 45
mtz = MultiTaskLasso(alpha=amax21 * 1.0001, tol=1e-12, max_iter=100000).fit(Xcv, Ymt); mtnz = MultiTaskLasso(alpha=amax21 * 0.999, tol=1e-12, max_iter=100000).fit(Xcv, Ymt)
report("MultiTaskLasso: alpha_max = max_j ||(Xc'Yc)_j||_2 / n: all-zero just above, non-zero just below", np.all(mtz.coef_ == 0) and np.any(mtnz.coef_ != 0))

# ================================================================ Ridge solvers agreement (all documented to solve the same problem)
Xrs = rs.randn(80, 5); yrs = Xrs @ np.array([1, -2, 0.5, 0, 3.0]) + 1.0 + 0.5 * rs.randn(80); wr, br = ridge_fit(Xrs, yrs, 2.0)
for solver in ("svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga", "lbfgs"):
    kw = dict(alpha=2.0, solver=solver, tol=1e-12, max_iter=100000, random_state=0)
    if solver == "lbfgs": kw["positive"] = True
    try:
        m = Ridge(**kw).fit(Xrs, yrs)
        if solver == "lbfgs":
            Xc_, yc_, _, _ = centre(Xrs, yrs); g = Xc_.T @ (Xc_ @ m.coef_ - yc_) + 2.0 * m.coef_
            ok = np.all(m.coef_ >= 0) and np.all(g[m.coef_ > 0] < 1e-5) and np.all(np.abs(g[m.coef_ > 0]) < 1e-5) and np.all(g[m.coef_ == 0] > -1e-5)
            report("Ridge(solver='lbfgs', positive=True): coef >= 0 and NNLS-KKT of ||yc - Xc w||^2 + alpha ||w||^2 (g_j = 0 for w_j > 0, g_j >= 0 for w_j = 0)", ok, f"(coef {np.round(m.coef_, 4)})")
        else:
            report(f"Ridge(solver='{solver}') = closed form (Xc'Xc + alpha I) w = Xc'yc, intercept = ybar - xbar w", np.allclose(m.coef_, wr, rtol=1e-7, atol=1e-9) and close(m.intercept_, br, 1e-7), f"(max diff {np.abs(m.coef_ - wr).max():.2e})")
    except Exception as e:
        report(f"Ridge(solver='{solver}') fits", False, f"({type(e).__name__}: {str(e)[:80]})")
for solver in ("sparse_cg", "sag", "lsqr"):
    m = Ridge(alpha=2.0, solver=solver, tol=1e-12, max_iter=100000, random_state=0).fit(sparse.csr_matrix(Xrs), yrs)
    report(f"Ridge(solver='{solver}') on sparse X with fit_intercept=True = closed form", np.allclose(m.coef_, wr, rtol=1e-6, atol=1e-8) and close(m.intercept_, br, 1e-6))
mpos = Ridge(alpha=2.0, positive=True).fit(Xrs, yrs)
report("Ridge(positive=True) with solver='auto' selects lbfgs (the only solver supporting positive)", np.all(mpos.coef_ >= 0) and getattr(mpos, "solver_", "lbfgs") == "lbfgs")

# ================================================================ LogisticRegression penalties / solvers (KKT of the documented objective)
def logit_kkt(X, y01, w, b, C, l1_ratio, s=None, kappa=None, no_intercept=False):
    """Max violation of the KKT of (1/S) sum s_i logloss + r(w)/(S C), r = l1r ||w||_1 + (1-l1r)/2 ||w||^2.
    kappa != None: liblinear's synthetic feature: the intercept b = kappa v with v penalised like a coefficient."""
    if s is None: s = np.ones(len(y01))
    S = s.sum(); pr = 1 / (1 + np.exp(-(X @ w + b))); g = X.T @ (s * (pr - y01)) / S; gb = (s * (pr - y01)).sum() / S
    v = 0.0
    for j in range(len(w)):
        gj = g[j] + (1 - l1_ratio) * w[j] / (S * C)
        if w[j] != 0: v = max(v, abs(gj + l1_ratio * np.sign(w[j]) / (S * C)))
        else: v = max(v, max(0.0, abs(gj) - l1_ratio / (S * C)))
    if no_intercept: pass
    elif kappa is None: v = max(v, abs(gb))
    else:
        vv = b / kappa; gv = gb * kappa + (1 - l1_ratio) * vv / (S * C)
        v = max(v, abs(gv + l1_ratio * np.sign(vv) / (S * C)) if vv != 0 else max(0.0, abs(gv) - l1_ratio / (S * C)))
    return v
Xlg = rs.randn(120, 4); ylg = (Xlg @ np.array([1.5, -1.0, 0.0, 0.5]) + 0.3 + 0.8 * rs.randn(120) > 0).astype(int)
lkw = dict(tol=1e-12, max_iter=100000)
for solver, pen, l1r in [("lbfgs", "l2", 0.0), ("newton-cg", "l2", 0.0), ("newton-cholesky", "l2", 0.0), ("sag", "l2", 0.0), ("saga", "l2", 0.0), ("liblinear", "l2", 0.0),
                         ("saga", "l1", 1.0), ("liblinear", "l1", 1.0), ("saga", "elasticnet", 0.4)]:
    if solver == "newton-cholesky" and VER < (1, 2): continue
    try:
        m = LR(pen, l1_ratio=l1r if pen == "elasticnet" else None, C=0.5, solver=solver, random_state=0, **lkw).fit(Xlg, ylg)
        kappa = 1.0 if solver == "liblinear" else None
        v = logit_kkt(Xlg, ylg, m.coef_[0], m.intercept_[0], 0.5, l1r, kappa=kappa)
        report(f"LogisticRegression(penalty={pen}, C=0.5, solver={solver}): KKT of (1/S) sum logloss + r(w)/(S C){' with the intercept penalised via intercept_scaling=1' if kappa else ' (intercept unpenalised)'} (violation < 1e-5)", v < 1e-5, f"(violation {v:.2e}, nnz {np.count_nonzero(m.coef_)})")
    except Exception as e:
        report(f"LogisticRegression(penalty={pen}, solver={solver}) fits", False, f"({type(e).__name__}: {str(e)[:100]})")
m = LR(None, solver="lbfgs", **lkw).fit(Xlg, ylg)
report("LogisticRegression(penalty=None): unpenalised MLE, gradient of the mean log-loss vanishes", logit_kkt(Xlg, ylg, m.coef_[0], m.intercept_[0], np.inf, 0.0) < 1e-5)
m1 = LR("l1", C=0.3, solver="liblinear", intercept_scaling=1.0, random_state=0, **lkw).fit(Xlg, ylg); m3 = LR("l1", C=0.3, solver="liblinear", intercept_scaling=5.0, random_state=0, **lkw).fit(Xlg, ylg)
report("liblinear intercept_scaling: intercept = kappa * synthetic weight and the synthetic weight is penalised (L1 KKT with kappa=1 and kappa=5 both hold); larger kappa lessens the intercept penalty", logit_kkt(Xlg, ylg, m1.coef_[0], m1.intercept_[0], 0.3, 1.0, kappa=1.0) < 1e-5 and logit_kkt(Xlg, ylg, m3.coef_[0], m3.intercept_[0], 0.3, 1.0, kappa=5.0) < 1e-5 and abs(m3.intercept_[0]) >= abs(m1.intercept_[0]) - 1e-9, f"(intercepts {m1.intercept_[0]:.4f} vs {m3.intercept_[0]:.4f})")
# C scaling and sample weights
sw_l = rs.uniform(0.5, 2.0, 120); mw = LR("l2", C=0.5, solver="lbfgs", **lkw).fit(Xlg, ylg, sample_weight=sw_l)
report("LogisticRegression sample_weight: KKT of the weighted objective (1/S) sum s_i logloss_i + ||w||^2/(2 S C), S = sum s_i", logit_kkt(Xlg, ylg, mw.coef_[0], mw.intercept_[0], 0.5, 0.0, s=sw_l) < 1e-5)
mcw = LR("l2", C=0.5, solver="lbfgs", class_weight={0: 1.0, 1: 2.5}, **lkw).fit(Xlg, ylg, sample_weight=sw_l)
report("LogisticRegression class_weight * sample_weight: s_i = class_weight[y_i] * sample_weight_i (documented 'multiplied')", logit_kkt(Xlg, ylg, mcw.coef_[0], mcw.intercept_[0], 0.5, 0.0, s=sw_l * np.where(ylg == 1, 2.5, 1.0)) < 1e-5)
m2 = LR("l2", C=0.5, solver="lbfgs", **lkw).fit(Xlg, ylg, sample_weight=np.full(120, 2.0)); md = LR("l2", C=0.5, solver="lbfgs", **lkw).fit(np.vstack([Xlg, Xlg]), np.concatenate([ylg, ylg])); m1c = LR("l2", C=1.0, solver="lbfgs", **lkw).fit(Xlg, ylg); m05 = LR("l2", C=0.5, solver="lbfgs", **lkw).fit(Xlg, ylg)
report("LogisticRegression: sample_weight=2 == duplicated rows == single copy with C doubled (C is per-sample: r(w)/(S C)), and != the single copy at the same C", np.allclose(m2.coef_, md.coef_, rtol=1e-6) and np.allclose(m2.coef_, m1c.coef_, rtol=1e-6) and not np.allclose(m2.coef_, m05.coef_, rtol=1e-3))
# multinomial
y3l = np.argmax(Xlg @ rs.randn(4, 3) + 0.5 * rs.randn(120, 3), axis=1)
mm = LR("l2", C=0.7, solver="lbfgs", **lkw).fit(Xlg, y3l)
P = np.exp(mm.decision_function(Xlg)); P /= P.sum(1, keepdims=True); Y1 = np.eye(3)[y3l]
G = Xlg.T @ (P - Y1) / 120 + mm.coef_.T / (120 * 0.7); Gb = (P - Y1).sum(0) / 120
report("LogisticRegression multiclass (3 classes, lbfgs): KKT of the multinomial objective -(1/S) sum log p_{y_i} + ||W||_Fro^2/(2 S C), intercepts unpenalised; coef_ shape (3, 4)", mm.coef_.shape == (3, 4) and np.abs(G).max() < 1e-5 and np.abs(Gb).max() < 1e-5, f"(violation {max(np.abs(G).max(), np.abs(Gb).max()):.2e})")
for solver in ("newton-cg", "sag", "saga") + (("newton-cholesky",) if VER >= (1, 2) else ()):
    ms = LR("l2", C=0.7, solver=solver, random_state=0, **lkw).fit(Xlg, y3l)
    if solver == "newton-cholesky" and VER < (1, 6):
        ovr = max(logit_kkt(Xlg, (y3l == k).astype(int), ms.coef_[k], ms.intercept_[k], 0.7, 0.0) for k in range(3))
        report("LogisticRegression(solver='newton-cholesky') on 3 classes in < 1.6: one-vs-rest as documented ('can only handle binary classification'): each row satisfies the binary KKT of class k vs rest", ovr < 1e-5, f"(violation {ovr:.2e}, differs from multinomial by {np.abs(ms.coef_ - mm.coef_).max():.2e})")
        continue
    report(f"LogisticRegression multinomial with solver={solver} = the same minimiser (all solvers 'minimize the full multinomial loss')", np.allclose(ms.coef_, mm.coef_, rtol=1e-4, atol=1e-6) and np.allclose(ms.intercept_, mm.intercept_, rtol=1e-4, atol=1e-6), f"(max diff {np.abs(ms.coef_ - mm.coef_).max():.2e})")
try:
    LR("l2", solver="liblinear").fit(Xlg, y3l); lib_multi = "fits one-vs-rest"
except ValueError as e: lib_multi = "raises ValueError"
report("liblinear on 3 classes: main docs 'liblinear will raise an error' (versions < 1.8: one-vs-rest)", (lib_multi == "raises ValueError") if VER >= (1, 8) else (lib_multi == "fits one-vs-rest"), f"({lib_multi})")
if VER < (1, 8):
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always"); LogisticRegression(multi_class="ovr", max_iter=1000).fit(Xlg, y3l)
    dep = any("multi_class" in str(x.message) and "deprecat" in str(x.message).lower() for x in wl)
    report("LogisticRegression(multi_class='ovr'): deprecated from 1.5 (FutureWarning), accepted silently before", dep if VER >= (1, 5) else not dep, f"({len(wl)} warnings)")
else:
    try:
        LogisticRegression(multi_class="ovr"); ok = False
    except TypeError: ok = True
    report("LogisticRegression(multi_class=...) removed in 1.8: TypeError", ok)
if VER >= (1, 8):
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always"); LogisticRegression(penalty="l2", max_iter=1000).fit(Xlg, ylg)
    report("LogisticRegression(penalty='l2') deprecated in 1.8 (FutureWarning, use l1_ratio)", any("penalty" in str(x.message) for x in wl))
mws = LR("l2", C=0.5, solver="lbfgs", warm_start=True, **lkw).fit(Xlg, ylg); it0 = mws.n_iter_[0]; mws.fit(Xlg, ylg)
report("LogisticRegression warm_start=True: refitting the same problem starts from the solution (fewer iterations) and stays at the optimum", mws.n_iter_[0] < it0 and logit_kkt(Xlg, ylg, mws.coef_[0], mws.intercept_[0], 0.5, 0.0) < 1e-5, f"(n_iter {it0} then {mws.n_iter_[0]})")
mws.set_params(C=2.0); mws.fit(Xlg, ylg)
report("LogisticRegression warm_start then a new C: KKT of the new problem hold (warm start does not change the optimum)", logit_kkt(Xlg, ylg, mws.coef_[0], mws.intercept_[0], 2.0, 0.0) < 1e-5)
m = LR("l2", C=0.5, solver="lbfgs", **lkw).fit(Xlg, ylg)
report("LogisticRegression predict_proba = expit(decision_function), predict_log_proba = log of it, decision = X coef_ + intercept_", np.allclose(m.predict_proba(Xlg)[:, 1], 1 / (1 + np.exp(-(Xlg @ m.coef_[0] + m.intercept_[0])))) and np.allclose(m.predict_log_proba(Xlg), np.log(m.predict_proba(Xlg))))
ms_ = LR("l2", C=0.5, solver="saga", random_state=0, **lkw).fit(sparse.csr_matrix(Xlg), ylg)
report("LogisticRegression(saga) on sparse csr X = dense KKT", logit_kkt(Xlg, ylg, ms_.coef_[0], ms_.intercept_[0], 0.5, 0.0) < 1e-5)
m0 = LR("l1", C=0.5, solver="saga", fit_intercept=False, random_state=0, **lkw).fit(Xlg, ylg)
report("LogisticRegression(fit_intercept=False, l1, saga): intercept_ = 0 and the L1 KKT in w alone hold", np.all(m0.intercept_ == 0) and logit_kkt(Xlg, ylg, m0.coef_[0], 0.0, 0.5, 1.0, no_intercept=True) < 1e-5, f"(violation {logit_kkt(Xlg, ylg, m0.coef_[0], 0.0, 0.5, 1.0, no_intercept=True):.2e})")

# ================================================================ LogisticRegressionCV
def lrcv(**kw):
    if VER >= (1, 9): kw.setdefault("l1_ratios", None); kw.setdefault("scoring", None); kw.setdefault("use_legacy_attributes", True)
    return LogisticRegressionCV(**kw)
cv5 = StratifiedKFold(4)
lc = lrcv(Cs=5, cv=cv5, solver="lbfgs", tol=1e-10, max_iter=10000).fit(Xlg, ylg)
Cs = np.logspace(-4, 4, 5)
report("LogisticRegressionCV(Cs=5): Cs_ = logspace(-4, 4, 5) (documented grid)", np.allclose(lc.Cs_, Cs, rtol=1e-12))
sc_ref = np.zeros((4, 5))
for k, (tr, te) in enumerate(cv5.split(Xlg, ylg)):
    for j, C in enumerate(Cs):
        mm_ = LR("l2", C=C, solver="lbfgs", tol=1e-10, max_iter=10000).fit(Xlg[tr], ylg[tr]); sc_ref[k, j] = np.mean(mm_.predict(Xlg[te]) == ylg[te])
sc = lc.scores_[1] if isinstance(lc.scores_, dict) else lc.scores_
report("LogisticRegressionCV scores_[class] shape (n_folds, n_cs) = accuracy (default scoring) of LogisticRegression(C) fitted on each StratifiedKFold(4) training fold (my accuracy)", sc.shape == (4, 5) and np.allclose(sc, sc_ref, atol=1e-12), f"(fold means {np.round(sc.mean(0), 4)})")
best = np.argmax(sc_ref.mean(0)); mref = LR("l2", C=Cs[best], solver="lbfgs", tol=1e-10, max_iter=10000).fit(Xlg, ylg)
report("LogisticRegressionCV(refit=True): C_ = Cs_[argmax of the fold-mean score], coef_ = LogisticRegression(C_) refit on all data (rel 1e-4)", close(np.ravel(lc.C_)[0], Cs[best], 1e-12) and np.allclose(lc.coef_, mref.coef_, rtol=1e-4, atol=1e-6) and np.allclose(lc.intercept_, mref.intercept_, rtol=1e-4, atol=1e-6), f"(C_ {np.ravel(lc.C_)[0]}, max diff {np.abs(lc.coef_ - mref.coef_).max():.2e})")
lcn = lrcv(Cs=5, cv=cv5, solver="lbfgs", tol=1e-10, max_iter=10000, refit=False).fit(Xlg, ylg)
bidx = [int(np.argmax(sc_ref[k])) for k in range(4)]
coefs_f = [LR("l2", C=Cs[bidx[k]], solver="lbfgs", tol=1e-10, max_iter=10000).fit(Xlg[tr], ylg[tr]) for k, (tr, te) in enumerate(cv5.split(Xlg, ylg))]
report("LogisticRegressionCV(refit=False): C_ = mean over folds of each fold's best C, coef_/intercept_ = mean of the fold coefficients at those Cs (documented)", close(np.ravel(lcn.C_)[0], np.mean(Cs[bidx]), 1e-12) and np.allclose(lcn.coef_[0], np.mean([c_.coef_[0] for c_ in coefs_f], 0), rtol=1e-4, atol=1e-6) and close(lcn.intercept_[0], np.mean([c_.intercept_[0] for c_ in coefs_f]), 1e-4, 1e-6), f"(fold best Cs {Cs[bidx]})")
lcs = lrcv(Cs=[0.01, 1.0], cv=cv5, solver="lbfgs", scoring="neg_log_loss", tol=1e-10, max_iter=10000).fit(Xlg, ylg)
ll_ref = np.zeros((4, 2))
for k, (tr, te) in enumerate(cv5.split(Xlg, ylg)):
    for j, C in enumerate([0.01, 1.0]):
        mm_ = LR("l2", C=C, solver="lbfgs", tol=1e-10, max_iter=10000).fit(Xlg[tr], ylg[tr]); pr_ = mm_.predict_proba(Xlg[te])[:, 1]; ll_ref[k, j] = np.mean(ylg[te] * np.log(pr_) + (1 - ylg[te]) * np.log(1 - pr_))
scl = lcs.scores_[1] if isinstance(lcs.scores_, dict) else lcs.scores_
report("LogisticRegressionCV(scoring='neg_log_loss', Cs=[0.01, 1]): scores_ = negative mean log-loss per fold and C", np.allclose(scl, ll_ref, rtol=1e-5, atol=1e-6) and np.all(lcs.Cs_ == [0.01, 1.0]), f"(max diff {np.abs(scl - ll_ref).max():.2e})")
lc3 = lrcv(Cs=3, cv=cv5, solver="lbfgs", tol=1e-8, max_iter=10000).fit(Xlg, y3l)
sc3 = lc3.scores_ if isinstance(lc3.scores_, dict) else None
report("LogisticRegressionCV multiclass (3 classes): scores_ dict keyed by class, 'the same score is repeated across all classes', coef_ shape (3, 4)", sc3 is not None and sorted(sc3.keys()) == [0, 1, 2] and all(np.array_equal(sc3[0], sc3[k]) for k in (1, 2)) and lc3.coef_.shape == (3, 4))
cp = lc.coefs_paths_[1] if isinstance(lc.coefs_paths_, dict) else lc.coefs_paths_
report("LogisticRegressionCV coefs_paths_[class] shape (n_folds, n_cs, n_features + 1) with the intercept as the last column", cp.shape == (4, 5, 5), f"(shape {cp.shape})")
