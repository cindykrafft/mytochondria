#!/usr/bin/env python
"""svm (SVC / NuSVC / SVR / NuSVR / OneClassSVM / LinearSVC / LinearSVR / l1_min_c),
neighbors (KNeighbors* / RadiusNeighbors* / NearestNeighbors / KDTree / BallTree /
LocalOutlierFactor / NearestCentroid / NeighborhoodComponentsAnalysis / KernelDensity),
kernel_approximation (Nystroem / RBFSampler / SkewedChi2Sampler / AdditiveChi2Sampler /
PolynomialCountSketch) and random_projection -- every check against an independent truth:
kernel formulas coded here, the documented dual / KKT conditions, closed forms, a plain-Python
brute-force neighbour search, mpmath integrals for the kernel normalisations, scipy.optimize
references for the liblinear primal / dual objectives, fractions.Fraction where exact."""
import sys, math, warnings, itertools, traceback
sys.path.insert(0, ".")
from _synth import *
import mpmath
from mpmath import mp, mpf
mp.dps = 30
import scipy
from scipy import optimize
import scipy.sparse as sp
from sklearn.svm import SVC, NuSVC, SVR, NuSVR, OneClassSVM, LinearSVC, LinearSVR, l1_min_c
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import (KNeighborsClassifier, KNeighborsRegressor, RadiusNeighborsClassifier,
                               RadiusNeighborsRegressor, NearestNeighbors, KDTree, BallTree,
                               LocalOutlierFactor, NearestCentroid, NeighborhoodComponentsAnalysis,
                               KernelDensity, kneighbors_graph, radius_neighbors_graph)
from sklearn.kernel_approximation import (Nystroem, RBFSampler, SkewedChi2Sampler, AdditiveChi2Sampler,
                                          PolynomialCountSketch)
from sklearn.random_projection import johnson_lindenstrauss_min_dim, GaussianRandomProjection, SparseRandomProjection
banner(); warnings.filterwarnings("ignore")
V = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
rs = np.random.RandomState(12)

def allclose(a, b, rel=1e-9, abs_=1e-12):
    a = np.asarray(a, float); b = np.asarray(b, float)
    if a.shape != b.shape: return False
    return bool(np.all(np.abs(a - b) <= abs_ + rel * np.maximum(np.abs(a), np.abs(b))))

def maxdiff(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    return float(np.max(np.abs(a - b))) if a.shape == b.shape else float("inf")

def kern(kind, A, B, gamma=1.0, coef0=0.0, degree=3):
    """The kernels as documented in the SVM user guide, coded independently."""
    A = np.asarray(A, float); B = np.asarray(B, float)
    if kind == "rbf":
        return np.exp(-gamma * ((A[:, None, :] - B[None, :, :]) ** 2).sum(-1))
    if kind == "chi2":
        out = np.zeros((len(A), len(B)))
        for i in range(len(A)):
            for j in range(len(B)):
                s = 0.0
                for a, b in zip(A[i], B[j]):
                    if a + b != 0: s += (a - b) ** 2 / (a + b)
                out[i, j] = math.exp(-gamma * s)
        return out
    G = A @ B.T
    if kind == "linear": return G
    if kind == "poly": return (gamma * G + coef0) ** degree
    if kind == "sigmoid": return np.tanh(gamma * G + coef0)
    raise ValueError(kind)

def frac_var_all(X):
    vals = [F(float(v)) for v in np.asarray(X).ravel()]
    m = sum(vals) / len(vals)
    return sum((v - m) ** 2 for v in vals) / len(vals)

def expect_raises(fn, exc=ValueError):
    try:
        fn(); return False
    except exc:
        return True

# =============================================================================
def qp_ref(Xt, y, C, kind, eps=0.0):
    """Primal QP reference with slack variables, solved by scipy SLSQP:
    min 1/2||w||^2 + C sum xi  s.t.  xi_i >= 1 - y_i w.x_i (hinge)  or  xi_i >= |y_i - w.x_i| - eps (svr),  xi >= 0.
    Returns (w, primal value of w computed with the exact loss)."""
    n, p = Xt.shape
    if kind == "hinge":
        A = np.hstack([y[:, None] * Xt, np.eye(n)]); lb = np.ones(n)
    else:
        A = np.vstack([np.hstack([Xt, np.eye(n)]), np.hstack([-Xt, np.eye(n)])]); lb = np.concatenate([y - eps, -y - eps])
    def f(z): return 0.5 * z[:p] @ z[:p] + C * z[p:].sum(), np.concatenate([z[:p], np.full(n, C)])
    r = optimize.minimize(f, np.concatenate([np.zeros(p), np.full(n, 10.0)]), jac=True, method="SLSQP",
                          constraints=[dict(type="ineq", fun=lambda z: A @ z - lb, jac=lambda z: A)], bounds=[(None, None)] * p + [(0, None)] * n,
                          options=dict(ftol=1e-15, maxiter=5000))
    w = r.x[:p]
    loss = np.maximum(0, 1 - y * (Xt @ w)) if kind == "hinge" else np.maximum(0, np.abs(y - Xt @ w) - eps)
    return w, 0.5 * w @ w + C * loss.sum()

def tol_sweep(tag, make, X, y, primal, opt):
    """Fit at tol = 1e-4 ... 1e-14 (max_iter 200000) and record n_iter_, the primal objective and whether a
    ConvergenceWarning was raised. A dual coordinate-descent solver that is monotone in the dual objective should
    not return a worse primal at a tighter tolerance than at a looser one."""
    res = {}
    for t in (1e-4, 1e-8, 1e-10, 1e-11, 1e-12, 1e-14):
        with warnings.catch_warnings(record=True) as wl:
            warnings.simplefilter("always"); m = make(t).fit(X, y)
        res[t] = (int(np.max(m.n_iter_)), float(primal(m)), any(w.category.__name__ == "ConvergenceWarning" for w in wl))
    print(f"   {tag} tolerance sweep; optimum {opt:.10f}:")
    for t, (it, P, cw) in res.items(): print(f"      tol {t:g}: n_iter_ {it}, primal {P:.10f} (excess {P - opt:.2e}), ConvergenceWarning {cw}")
    report(f"{tag}: every tol in 1e-8 ... 1e-14 (max_iter=200000) returns a primal objective within 1e-7 (relative) of the optimum (a tighter tolerance must not give a worse solution than tol=1e-8)",
           all(res[t][1] - opt <= 1e-7 * max(1, abs(opt)) for t in (1e-8, 1e-10, 1e-11, 1e-12, 1e-14)))
    return res

def reseed(k):
    """Every section draws its data from its own stream, so version-dependent code paths in one section
    cannot change the data of another."""
    global rs
    rs = np.random.RandomState(1200 + k)

def section(name, fn):
    print(f"== {name}")
    try: fn()
    except Exception as e:
        report(f"[{name}] section ran to completion", False, f"crashed: {type(e).__name__}: {e}")
        traceback.print_exc(file=sys.stdout)

def _s00():
    global K, Kq, Ktr, Xb, Xf32, Xq, dec, df, g_exact, kind, kw, m, m32, ml, mp2, mpre, mrbf, ms, perm, yb, ysgn
    reseed(0)
    Xb = rs.randn(30, 2)
    yb = np.where(Xb[:, 0] + 0.5 * Xb[:, 1] + 0.4 * rs.randn(30) > 0, 7, 3)
    Xq = rs.randn(8, 2)
    ysgn = np.where(yb == 7, 1.0, -1.0)
    print(f"   classes {sorted(set(yb))}: counts {[(c, int((yb == c).sum())) for c in (3, 7)]}")
    for kind, kw in [("linear", {}), ("poly", dict(gamma=0.7, coef0=0.5, degree=2)), ("rbf", dict(gamma=0.7)),
                     ("sigmoid", dict(gamma=0.2, coef0=-0.3))]:
        m = SVC(kernel=kind, C=1.5, tol=1e-8, **kw).fit(Xb, yb)
        K = kern(kind, m.support_vectors_, Xq, gamma=kw.get("gamma", 1.0), coef0=kw.get("coef0", 0.0), degree=kw.get("degree", 3))
        dec = (m.dual_coef_ @ K + m.intercept_).ravel(); df = m.decision_function(Xq)
        print(f"   {kind}: n_SV {len(m.support_)} intercept_ {m.intercept_[0]:.6f} decision {np.round(df, 6).tolist()} max|diff| {maxdiff(df, dec):.2e}")
        report(f"SVC(kernel={kind}) decision_function = dual_coef_ @ K(SV, x) + intercept_ (K coded independently, gamma/coef0/degree as given)", allclose(df, dec, 1e-9, 1e-9))
        report(f"SVC(kernel={kind}) predict = classes_[1] (=7) iff decision_function > 0, classes_ sorted", np.array_equal(m.predict(Xq), np.where(df > 0, 7, 3)) and list(m.classes_) == [3, 7])
        report(f"SVC(kernel={kind}) support_vectors_ == X[support_], n_support_ sums to n_SV, SVs grouped by class in classes_ order",
               np.array_equal(m.support_vectors_, Xb[m.support_]) and int(m.n_support_.sum()) == len(m.support_)
               and np.array_equal(yb[m.support_], np.repeat([3, 7], m.n_support_)))
    ml = SVC(kernel="linear", C=1.5, tol=1e-8).fit(Xb, yb)
    report("SVC(linear) coef_ = dual_coef_ @ support_vectors_ and decision_function = X @ coef_.T + intercept_ (intercept_ sign)",
           allclose(ml.coef_, ml.dual_coef_ @ ml.support_vectors_) and allclose(ml.decision_function(Xq), (Xq @ ml.coef_.T + ml.intercept_).ravel(), 1e-9, 1e-9))
    # class ordering independent of data order
    perm = rs.permutation(30)
    mp2 = SVC(kernel="linear", C=1.5, tol=1e-8).fit(Xb[perm], yb[perm])
    report("SVC classes_ sorted and decision function unchanged when the rows are permuted (max |diff| 1e-6)",
           list(mp2.classes_) == [3, 7] and allclose(mp2.decision_function(Xq), ml.decision_function(Xq), 1e-6, 1e-6))
    # precomputed
    Ktr = kern("rbf", Xb, Xb, gamma=0.7); Kq = kern("rbf", Xq, Xb, gamma=0.7)
    mpre = SVC(kernel="precomputed", C=1.5, tol=1e-8).fit(Ktr, yb)
    mrbf = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-8).fit(Xb, yb)
    dec = (mpre.dual_coef_ @ Kq[:, mpre.support_].T + mpre.intercept_).ravel()
    report("SVC(kernel='precomputed') decision_function = dual_coef_ @ K_test[:, support_] + intercept_", allclose(mpre.decision_function(Kq), dec, 1e-9, 1e-9))
    report("SVC(kernel='precomputed' with the rbf Gram matrix) equals SVC(kernel='rbf') (support_, dual_coef_, intercept_ within 1e-6)",
           np.array_equal(mpre.support_, mrbf.support_) and allclose(mpre.dual_coef_, mrbf.dual_coef_, 1e-6, 1e-6) and allclose(mpre.intercept_, mrbf.intercept_, 1e-6, 1e-6))
    report("SVC(kernel='precomputed') support_vectors_ is empty (documented 'An empty array if kernel is precomputed')", mpre.support_vectors_.size == 0)
    # gamma='scale'
    g_exact = 1 / (F(Xb.shape[1]) * frac_var_all(Xb))
    ms = SVC(kernel="rbf", C=1.5, tol=1e-8).fit(Xb, yb)
    dec = (ms.dual_coef_ @ kern("rbf", ms.support_vectors_, Xq, gamma=float(g_exact)) + ms.intercept_).ravel()
    print(f"   gamma='scale': exact 1/(n_features*X.var()) = {float(g_exact):.12f}; model _gamma = {getattr(ms, '_gamma', float('nan'))!r}")
    report("SVC(gamma='scale' default) decision_function recomputed with gamma = 1/(n_features * X.var()) (population variance of all entries, exact Fraction)", allclose(ms.decision_function(Xq), dec, 1e-9, 1e-9))
    report("SVC(gamma='auto') decision_function recomputed with gamma = 1/n_features",
           allclose(SVC(kernel="rbf", gamma="auto", C=1.5, tol=1e-8).fit(Xb, yb).decision_function(Xq),
                    (lambda m: (m.dual_coef_ @ kern("rbf", m.support_vectors_, Xq, gamma=0.5) + m.intercept_).ravel())(SVC(kernel="rbf", gamma="auto", C=1.5, tol=1e-8).fit(Xb, yb)), 1e-9, 1e-9))
    Xf32 = Xb.astype(np.float32)
    m32 = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-8).fit(Xf32, yb)
    report("SVC float32 input: decision_function within 1e-4 of the float64 fit", allclose(m32.decision_function(Xq.astype(np.float32)), mrbf.decision_function(Xq), 1e-4, 1e-4), f"(max diff {maxdiff(m32.decision_function(Xq.astype(np.float32)), mrbf.decision_function(Xq)):.1e})")
    msp = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-8).fit(sp.csr_matrix(Xb), yb)
    report("SVC on scipy.sparse CSR input = the dense fit (support_, dual_coef_, intercept_, decision_function within 1e-8; sparse support_vectors_ documented)",
           np.array_equal(msp.support_, mrbf.support_) and allclose(msp.dual_coef_.toarray(), mrbf.dual_coef_, 1e-8, 1e-8) and allclose(msp.intercept_, mrbf.intercept_, 1e-8, 1e-8)
           and allclose(msp.decision_function(sp.csr_matrix(Xq)), mrbf.decision_function(Xq), 1e-8, 1e-8) and sp.issparse(msp.support_vectors_))
    # large offset: the rbf kernel only sees differences, so shifting X by a constant must not change the fit
    moff = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-8).fit(Xb + 1e4, yb)
    print(f"   X + 1e4: max |decision diff| {maxdiff(moff.decision_function(Xq + 1e4), mrbf.decision_function(Xq)):.2e}")
    report("SVC(rbf) on X + 1e4 (translation-invariant kernel) = fit on X: same support_, decision_function within 1e-5", np.array_equal(moff.support_, mrbf.support_) and allclose(moff.decision_function(Xq + 1e4), mrbf.decision_function(Xq), 1e-5, 1e-5))
    report("SVC with a single class in y raises ValueError", expect_raises(lambda: SVC().fit(Xb, np.full(30, 3))))
    Xnan = Xb.copy(); Xnan[4, 1] = np.nan
    report("SVC with NaN in X raises ValueError (input validation)", expect_raises(lambda: SVC().fit(Xnan, yb)))
    # sample_weight = 0 means C_i = 0, i.e. alpha_i = 0: the same problem as dropping the sample
    sw0 = np.ones(30); drop = [2, 5, 11, 17, 23]; sw0[drop] = 0.0; keep = np.setdiff1d(np.arange(30), drop)
    mw0 = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-10).fit(Xb, yb, sample_weight=sw0); mdr = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-10).fit(Xb[keep], yb[keep])
    print(f"   sample_weight 0 on 5 rows: n_SV {len(mw0.support_)} vs dropped-rows fit {len(mdr.support_)}; max |decision diff| {maxdiff(mw0.decision_function(Xq), mdr.decision_function(Xq)):.2e}")
    report("SVC(sample_weight=0 on some rows) = fit with those rows removed ('Rescale C per sample': C_i = 0 forces alpha_i = 0): decision_function within 1e-6",
           allclose(mw0.decision_function(Xq), mdr.decision_function(Xq), 1e-6, 1e-6))
    print(f"   support_ {mw0.support_.tolist()}; zero-weight rows {drop}; support_vectors_ == X[support_]: {np.array_equal(mw0.support_vectors_, Xb[mw0.support_])}; "
          f"== X[nonzero-weight rows][support_]: {np.array_equal(mw0.support_vectors_, Xb[keep][mw0.support_])}")
    report("SVC(sample_weight with zeros): support_ indexes the rows of the X passed to fit (documented 'support_ : Indices of support vectors'): support_vectors_ == X[support_] and no zero-weight row in support_",
           np.array_equal(mw0.support_vectors_, Xb[mw0.support_]) and not set(mw0.support_.tolist()) & set(drop))
    # consequence for kernel='precomputed', where decision_function selects the test-kernel columns K_test[:, support_]
    mpw0 = SVC(kernel="precomputed", C=1.5, tol=1e-10).fit(kern("rbf", Xb, Xb, gamma=0.7), yb, sample_weight=sw0)
    dpw0 = mpw0.decision_function(kern("rbf", Xq, Xb, gamma=0.7))
    print(f"   precomputed rbf Gram, same zero weights: decision {np.round(dpw0, 4).tolist()}\n      rbf kernel fit (= dropped-rows fit): {np.round(mw0.decision_function(Xq), 4).tolist()}")
    report("SVC(kernel='precomputed', sample_weight with zeros) decision_function = the same fit with kernel='rbf' (= rows dropped), within 1e-6",
           allclose(dpw0, mw0.decision_function(Xq), 1e-6, 1e-6), f"(max diff {maxdiff(dpw0, mw0.decision_function(Xq)):.3f}; predictions differ on {int(np.sum(np.sign(dpw0) != np.sign(mw0.decision_function(Xq))))}/8 query points)")
    if V >= (1, 9):
        with warnings.catch_warnings(record=True) as wl:
            warnings.simplefilter("always"); SVC(probability=True, random_state=0).fit(Xb, yb)
        report("SVC(probability=True) emits a FutureWarning in 1.9+ (documented '..deprecated:: 1.9 The `probability` parameter is deprecated')", any(issubclass(w.category, FutureWarning) for w in wl))
section('svm.SVC binary: decision function recomputed from the dual, kernels coded independently', _s00)

def _s01():
    global C, Xs, cw, kkt_checks, m_c1, m_nos, mbal, mh, mh4, mk, mk2, nb3, nb7, sw, ys
    reseed(1)
    cw = {3: 1.0, 7: 2.5}; sw = rs.uniform(0.5, 2.0, 30)
    def kkt_checks(tag, m, X, y, Cbase, cwd, swv, kind, gamma):
        ysg = np.where(y == m.classes_[1], 1.0, -1.0)
        Ci = Cbase * np.array([cwd.get(v, 1.0) for v in y]) * (np.ones(len(y)) if swv is None else swv)
        alpha = np.zeros(len(y)); alpha[m.support_] = m.dual_coef_.ravel() * ysg[m.support_]
        f = m.decision_function(X); marg = ysg * f
        free = (alpha > 1e-9) & (alpha < Ci - 1e-9); bound = alpha >= Ci - 1e-9; nsv = alpha <= 1e-9
        print(f"   {tag}: n_SV {len(m.support_)} free {int(free.sum())} bounded {int(bound.sum())} non-SV {int(nsv.sum())}; max alpha/C_i {np.max(alpha / Ci):.9f}; sum dual_coef_ {m.dual_coef_.sum():.2e}")
        print(f"      margins y f: free {np.round(marg[free], 7).tolist()}; bounded max {marg[bound].max() if bound.any() else float('nan'):.6f}; non-SV min {marg[nsv].min() if nsv.any() else float('nan'):.6f}")
        report(f"{tag}: alpha_i = y_i * dual_coef_i >= 0 and support_ == {{i : alpha_i > 0}}", np.all(alpha >= 0) and set(m.support_.tolist()) == set(np.flatnonzero(alpha > 0).tolist()))
        report(f"{tag}: alpha_i <= C_i = C * class_weight[y_i] * sample_weight[i] (documented 'sets the parameter C of class i to class_weight[i]*C' / 'C * sample_weight[i]')", np.all(alpha <= Ci * (1 + 1e-9)))
        report(f"{tag}: the bounded SVs sit exactly at alpha_i = C_i and there is at least one (non-separable problem)", bound.any() and np.all(np.abs(alpha[bound] - Ci[bound]) <= 1e-9 * Ci[bound]))
        report(f"{tag}: equality constraint sum_i y_i alpha_i = sum(dual_coef_) = 0 (1e-9)", abs(m.dual_coef_.sum()) <= 1e-9)
        report(f"{tag}: complementary slackness within 1e-6 (libsvm caches the kernel in single precision, 'typedef float Qfloat'): free SVs y_i f(x_i) = 1, bounded y_i f(x_i) <= 1, non-SVs y_i f(x_i) >= 1",
               np.all(np.abs(marg[free] - 1) <= 1e-6) and np.all(marg[bound] <= 1 + 1e-6) and np.all(marg[nsv] >= 1 - 1e-6))
        SV = m.support_vectors_; a = m.dual_coef_.ravel(); Ksv = kern(kind, SV, SV, gamma=gamma)
        wn2 = a @ Ksv @ a
        P = 0.5 * wn2 + np.sum(Ci * np.maximum(0, 1 - marg)); D = alpha.sum() - 0.5 * wn2
        print(f"      primal 1/2||w||^2 + sum C_i max(0, 1 - y_i f_i) = {P:.10f}; dual e'alpha - 1/2 alpha'Q alpha = {D:.10f}; gap {P - D:.2e}")
        report(f"{tag}: duality gap primal - dual >= 0 and <= 1e-7 (both objectives recomputed from dual_coef_ / decision values)", -1e-9 <= P - D <= 1e-7 * max(1, P))
    mk = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-10, class_weight=cw).fit(Xb, yb, sample_weight=sw)
    kkt_checks("SVC(rbf, C=1.5, class_weight={3:1,7:2.5}, sample_weight)", mk, Xb, yb, 1.5, cw, sw, "rbf", 0.7)
    mk2 = SVC(kernel="linear", C=0.8, tol=1e-10).fit(Xb, yb)
    kkt_checks("SVC(linear, C=0.8)", mk2, Xb, yb, 0.8, {}, None, "linear", 1.0)
    mbal = SVC(kernel="linear", C=1.0, tol=1e-10, class_weight="balanced").fit(Xb, yb)
    nb3, nb7 = int((yb == 3).sum()), int((yb == 7).sum())
    kkt_checks(f"SVC(linear, class_weight='balanced' = n/(2*count): {{3: {30/(2*nb3):.4f}, 7: {30/(2*nb7):.4f}}})", mbal, Xb, yb, 1.0, {3: 30 / (2 * nb3), 7: 30 / (2 * nb7)}, None, "linear", 1.0)
    # hard margin closed form
    Xs = np.array([[0, 0], [2, 0], [1, 2], [-1, -1], [1, 5], [3, -2]], float); ys = np.array([0, 0, 1, 0, 1, 0])
    for C in (1e6, 1.0):
        mh = SVC(kernel="linear", C=C, tol=1e-12).fit(Xs, ys)
        print(f"   separable toy, C={C:g}: coef_ {mh.coef_.ravel().tolist()} intercept_ {mh.intercept_.tolist()} support_ {mh.support_.tolist()} dual_coef_ {mh.dual_coef_.ravel().tolist()}")
        report(f"SVC(linear, C={C:g}) on a separable toy = hard-margin closed form w=(0,1), b=-1, SVs {{0,1,2}}, alphas (1/4, 1/4, 1/2) (C >= max alpha = 1/2 suffices)",
               allclose(mh.coef_.ravel(), [0, 1], 1e-6, 1e-6) and allclose(mh.intercept_, [-1], 1e-6, 1e-6) and sorted(mh.support_.tolist()) == [0, 1, 2]
               and allclose(mh.dual_coef_.ravel(), [-0.25, -0.25, 0.5], 1e-6, 1e-6))
    mh4 = SVC(kernel="linear", C=0.4, tol=1e-12).fit(Xs, ys)
    print(f"   C=0.4 < 1/2: coef_ {mh4.coef_.ravel().tolist()} (soft margin, must differ)")
    report("SVC(linear, C=0.4 < max hard-margin alpha) is a different (soft-margin) solution", not allclose(mh4.coef_.ravel(), [0, 1], 1e-6, 1e-6))
    m_nos = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-8, shrinking=False).fit(Xb, yb)
    m_c1 = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-8, cache_size=1).fit(Xb, yb)
    report("SVC shrinking=False gives the same solution as shrinking=True (dual_coef_, intercept_ within 1e-6; 'shrinking heuristic')", np.array_equal(m_nos.support_, mrbf.support_) and allclose(m_nos.dual_coef_, mrbf.dual_coef_, 1e-6, 1e-6) and allclose(m_nos.intercept_, mrbf.intercept_, 1e-6, 1e-6))
    report("SVC cache_size=1 MB has no effect on the solution", np.array_equal(m_c1.support_, mrbf.support_) and allclose(m_c1.dual_coef_, mrbf.dual_coef_, 1e-12, 1e-12) and allclose(m_c1.intercept_, mrbf.intercept_, 1e-12, 1e-12))
    report("SVC max_iter=1 sets fit_status_ = 1 (documented '0 if correctly fitted, 1 otherwise')", SVC(kernel="rbf", max_iter=1).fit(Xb, yb).fit_status_ == 1 and mrbf.fit_status_ == 0)
section('svm.SVC KKT conditions of the documented dual (0 <= alpha_i <= C_i, complementary slackness), class_weight / sample_weight', _s01)

def _s02():
    global A, B, Xg, Xm, centers, coupling_exact, d, dec_ovo, dec_q, df_ovo, df_ovr, f, fg, first_max, gx, gy, i, inc4, incons, j, k, libsvm_coupling, mbt, mm, mpb, mpm, nc, ns, ovo_decision, ovr_ref, p0, pg, pij, pit, platt_kw, pp, pp4, ppg, probs_ref, r, row, sconf, starts, tied, votes, ym
    reseed(2)
    centers = np.array([[0, 0], [3, 0], [0, 3], [3, 3]], float)
    Xm = np.vstack([centers[k] + 0.9 * rs.randn(12, 2) for k in range(4)]); ym = np.repeat([10, 20, 30, 40], 12)
    mm = SVC(kernel="rbf", gamma=0.5, C=1.0, tol=1e-8, decision_function_shape="ovo").fit(Xm, ym)
    nc = 4; ns = mm.n_support_; starts = np.concatenate([[0], np.cumsum(ns)])
    report("SVC multiclass: support vectors grouped by class in classes_ order with n_support_ counts; dual_coef_ shape (n_classes-1, n_SV); intercept_ shape n(n-1)/2",
           np.array_equal(ym[mm.support_], np.repeat(mm.classes_, ns)) and mm.dual_coef_.shape == (3, int(ns.sum())) and mm.intercept_.shape == (6,))
    def ovo_decision(m, Xq_, kind="rbf", gamma=0.5):
        K = kern(kind, m.support_vectors_, Xq_, gamma=gamma); D = m.dual_coef_; k = 0; cols = []
        for i in range(nc):
            for j in range(i + 1, nc):
                si = slice(starts[i], starts[i + 1]); sj = slice(starts[j], starts[j + 1])
                cols.append(D[j - 1, si] @ K[si] + D[i, sj] @ K[sj] + m.intercept_[k]); k += 1
        return np.array(cols).T
    gx, gy = np.meshgrid(np.linspace(-2, 5, 30), np.linspace(-2, 5, 30)); Xg = np.c_[gx.ravel(), gy.ravel()]
    dec_ovo = ovo_decision(mm, Xg); df_ovo = mm.decision_function(Xg)
    print(f"   ovo decision_function shape {df_ovo.shape}; max |diff| vs recomputation from the documented dual_coef_ layout {maxdiff(df_ovo, dec_ovo):.2e}")
    report("SVC(decision_function_shape='ovo') = the 6 pairwise decisions '0 vs 1', '0 vs 2', ..., '2 vs 3' recomputed from the documented dual_coef_ layout (SV of class i vs class j uses row j-1, SV of class j uses row i)", allclose(df_ovo, dec_ovo, 1e-8, 1e-8))
    votes = np.zeros((len(Xg), nc)); sconf = np.zeros((len(Xg), nc)); k = 0
    for i in range(nc):
        for j in range(i + 1, nc):
            d = dec_ovo[:, k]; votes[d > 0, i] += 1; votes[d <= 0, j] += 1; sconf[:, i] += d; sconf[:, j] -= d; k += 1
    first_max = np.argmax(votes, axis=1)
    tied = np.sum(votes == votes.max(1, keepdims=True), axis=1) > 1
    print(f"   grid of {len(Xg)} query points: {int(tied.sum())} with tied vote counts")
    report("SVC predict (ovo) = class with most pairwise votes (positive decision votes for class i in 'i vs j')", np.array_equal(mm.predict(Xg), mm.classes_[first_max]))
    report("SVC predict with tied votes = 'the first class among the tied classes' (documented), on the tied grid points", tied.any() and np.array_equal(mm.predict(Xg[tied]), mm.classes_[first_max[tied]]))
    mm.decision_function_shape = "ovr"
    ovr_ref = votes + sconf / (3 * (np.abs(sconf) + 1))
    df_ovr = mm.decision_function(Xg)
    print(f"   ovr: max |diff| vs votes + sum_conf/(3(|sum_conf|+1)) {maxdiff(df_ovr, ovr_ref):.2e}")
    report("SVC(decision_function_shape='ovr') = votes + sum_of_confidences/(3(|sum_of_confidences|+1)) recomputed from the ovo decisions (the formula of sklearn.utils.multiclass._ovr_decision_function's docstring; public docs only say 'an ovr matrix is only constructed from the ovo matrix')", allclose(df_ovr, ovr_ref, 1e-8, 1e-8))
    report("ovr transformation keeps the vote order: |transformed confidences| < 1/3, argmax of ovr = a max-vote class", np.all(np.abs(df_ovr - votes) < 1 / 3) and np.all(votes[np.arange(len(Xg)), np.argmax(df_ovr, 1)] == votes.max(1)))
    mm2 = SVC(kernel="rbf", gamma=0.5, C=1.0, tol=1e-8).fit(Xm, ym)
    report("SVC default decision_function_shape is 'ovr' (documented default) with shape (n_samples, n_classes)", mm2.decision_function_shape == "ovr" and mm2.decision_function(Xg).shape == (len(Xg), 4) and allclose(mm2.decision_function(Xg), df_ovr, 1e-12, 1e-12))
    report("SVC(ovr, break_ties=False) predict still returns the first tied class (documented: 'the predict method does not try to break ties by default')", np.array_equal(mm.predict(Xg), mm.classes_[first_max]))
    mbt = SVC(kernel="rbf", gamma=0.5, C=1.0, tol=1e-8, decision_function_shape="ovr", break_ties=True).fit(Xm, ym)
    report("SVC(break_ties=True) predict == argmax(decision_function ovr) on all grid points (documented)", np.array_equal(mbt.predict(Xg), mbt.classes_[np.argmax(mbt.decision_function(Xg), 1)]))
    report("SVC(break_ties=True) changes the prediction on some tied points vs break_ties=False", np.any(mbt.predict(Xg[tied]) != mm.predict(Xg[tied])) if tied.any() else True)
    report("SVC(break_ties=True, decision_function_shape='ovo') predict raises ValueError (documented)", expect_raises(lambda: SVC(decision_function_shape="ovo", break_ties=True).fit(Xm, ym).predict(Xm)))
    # Platt scaling binary
    def platt_kw(): return dict(probability=True, random_state=0)
    mpb = SVC(kernel="rbf", gamma=0.7, C=1.5, tol=1e-8, **platt_kw()).fit(Xb, yb)
    A, B = mpb.probA_[0], mpb.probB_[0]
    f = mpb.decision_function(Xq)
    p0 = 1 / (1 + np.exp(A * (-f) + B)); p0 = np.clip(p0, 1e-7, 1 - 1e-7)
    pp = mpb.predict_proba(Xq)
    print(f"   binary Platt: probA_ {A:.6f} probB_ {B:.6f}; predict_proba[:,0] {np.round(pp[:, 0], 6).tolist()}\n   sigmoid(A*(-f)+B) {np.round(p0, 6).tolist()}")
    fg = mpb.decision_function(Xg); pg = np.clip(1 / (1 + np.exp(A * (-fg) + B)), 1e-7, 1 - 1e-7); ppg = mpb.predict_proba(Xg)
    print(f"   over the 900 grid points: max |predict_proba[:,0] - sigmoid| {maxdiff(ppg[:, 0], pg):.2e}")
    report("SVC(probability=True) binary predict_proba[:, 0] = 1/(1+exp(probA_ * d + probB_)) with d = libsvm's decision value = -decision_function (sklearn flips the binary sign), clipped to [1e-7, 1-1e-7], to 1e-10 (documented formula for probA_/probB_)",
           allclose(ppg[:, 0], pg, 1e-10, 1e-10) and allclose(ppg[:, 1], 1 - pg, 1e-10, 1e-10))
    def libsvm_coupling(r):
        """libsvm's multiclass_probability (Wu-Lin-Weng iteration, stops at max_error < 0.005/k), in plain Python."""
        k = len(r); Q = [[0.0] * k for _ in range(k)]; p = [1.0 / k] * k; Qp = [0.0] * k
        for t in range(k):
            Q[t][t] = sum(r[j][t] ** 2 for j in range(k) if j != t)
            for j in range(k):
                if j != t: Q[t][j] = -r[j][t] * r[t][j]
        for it in range(max(100, k)):
            pQp = 0.0
            for t in range(k):
                Qp[t] = sum(Q[t][j] * p[j] for j in range(k)); pQp += p[t] * Qp[t]
            if max(abs(Qp[t] - pQp) for t in range(k)) < 0.005 / k: break
            for t in range(k):
                diff = (-Qp[t] + pQp) / Q[t][t]; p[t] += diff
                pQp = (pQp + diff * (diff * Q[t][t] + 2 * Qp[t])) / (1 + diff) / (1 + diff)
                for j in range(k):
                    Qp[j] = (Qp[j] + diff * Q[t][j]) / (1 + diff); p[j] /= (1 + diff)
        return p
    pit = np.array([libsvm_coupling([[0.0, q], [1 - q, 0.0]]) for q in pg])
    report("SVC(probability=True) binary predict_proba = libsvm's pairwise-coupling iteration (max_error < 0.005/2 stopping rule, reproduced in plain Python) applied to the 2x2 sigmoid table, to 1e-10 -- i.e. the deviation from the documented sigmoid is the early-stopped coupling iteration",
           allclose(ppg, pit, 1e-10, 1e-10))
    report("SVC(probability=True) binary predict_proba within 1e-2 of the Platt sigmoid (the documented formula holds only up to the coupling iteration's tolerance)", allclose(ppg[:, 0], pg, 0, 1e-2))
    report("SVC(probability=True) binary predict_proba rows sum to 1 and predict_log_proba = log(predict_proba)", allclose(pp.sum(1), np.ones(8)) and allclose(mpb.predict_log_proba(Xq), np.log(pp), 1e-12, 1e-12))
    incons = int(np.sum(mpb.predict(Xb) != mpb.classes_[np.argmax(mpb.predict_proba(Xb), 1)]))
    print(f"   training points where predict != argmax predict_proba: {incons} of 30 (documented: 'predict_proba may be inconsistent with predict')")
    report("SVC(probability=True) predict is unchanged by probability=True (still the sign of the decision function, documented inconsistency with predict_proba is allowed)", np.array_equal(mpb.predict(Xb), mrbf.predict(Xb)))
    # multiclass pairwise coupling: exact solution of the Wu-Lin-Weng QP
    mpm = SVC(kernel="rbf", gamma=0.5, C=1.0, tol=1e-8, decision_function_shape="ovo", **platt_kw()).fit(Xm, ym)
    def coupling_exact(r):
        """min_p sum_i sum_{j!=i} (r_ji p_i - r_ij p_j)^2 s.t. sum p = 1 (Wu, Lin & Weng 2004, method 2): solve the KKT system."""
        k = len(r); Q = np.zeros((k, k))
        for t in range(k):
            Q[t, t] = sum(r[j][t] ** 2 for j in range(k) if j != t)
            for j in range(k):
                if j != t: Q[t, j] = -r[j][t] * r[t][j]
        M = np.zeros((k + 1, k + 1)); M[:k, :k] = Q; M[:k, k] = 1; M[k, :k] = 1
        rhs = np.zeros(k + 1); rhs[k] = 1
        return np.linalg.solve(M, rhs)[:k]
    dec_q = mpm.decision_function(Xg[::37])
    probs_ref = []
    for row in dec_q:
        r = [[0.0] * nc for _ in range(nc)]; k = 0
        for i in range(nc):
            for j in range(i + 1, nc):
                pij = min(max(1 / (1 + math.exp(mpm.probA_[k] * row[k] + mpm.probB_[k])), 1e-7), 1 - 1e-7)
                r[i][j] = pij; r[j][i] = 1 - pij; k += 1
        probs_ref.append(coupling_exact(r))
    probs_ref = np.array(probs_ref); pp4 = mpm.predict_proba(Xg[::37])
    print(f"   multiclass coupling: max |predict_proba - exact QP solution| {maxdiff(pp4, probs_ref):.2e} (libsvm iterates to 0.005/n_classes)")
    report("SVC multiclass predict_proba = pairwise coupling (Wu-Lin-Weng method 2 QP solved exactly) of the Platt sigmoids of the ovo decisions, within 5e-3 (libsvm's iteration tolerance)", allclose(pp4, probs_ref, 0, 5e-3))
    report("SVC multiclass predict_proba rows sum to 1", allclose(pp4.sum(1), np.ones(len(pp4))))
    inc4 = int(np.sum(mpm.predict(Xg) != mpm.classes_[np.argmax(mpm.predict_proba(Xg), 1)]))
    print(f"   multiclass grid points where predict != argmax predict_proba: {inc4} of {len(Xg)} (documented as possible)")
section('svm.SVC multiclass: ovo layout, votes, ovr transformation, break_ties, Platt / pairwise coupling', _s02)

def _s03():
    global Ximb, f, fm, frac_me, frac_sv, fs, marg, mg, n_, nu_, nus, ok_, yimb
    reseed(3)
    nus = NuSVC(nu=0.5, kernel="rbf", gamma=0.7, tol=1e-10).fit(Xb, yb)
    f = nus.decision_function(Xb); marg = ysgn * f
    frac_sv = len(nus.support_) / 30; frac_me = float(np.mean(marg < 1 - 1e-5))
    print(f"   nu=0.5: fraction of SVs {frac_sv:.4f}, fraction of margin errors (y f < 1 - 1e-5) {frac_me:.4f}")
    report("NuSVC(nu=0.5): fraction of support vectors >= nu and fraction of margin errors <= nu (documented bounds)", frac_sv >= 0.5 - 1e-12 and frac_me <= 0.5 + 1e-12)
    report("NuSVC decision_function = dual_coef_ @ K(SV, x) + intercept_ (rbf coded independently)", allclose(nus.decision_function(Xq), (nus.dual_coef_ @ kern("rbf", nus.support_vectors_, Xq, gamma=0.7) + nus.intercept_).ravel(), 1e-9, 1e-9))
    report("NuSVC: predict = classes_[1] iff decision_function > 0; margin scaled so free SVs have y_i f(x_i) = 1 (libsvm rescales rho to 1)",
           np.array_equal(nus.predict(Xq), np.where(nus.decision_function(Xq) > 0, 7, 3)) and np.any(np.abs(marg[nus.support_] - 1) < 1e-6))
    for nu_, ok_ in ((0.2, True), (0.7, True)):
        n_ = NuSVC(nu=nu_, kernel="rbf", gamma=0.7, tol=1e-10).fit(Xb, yb); mg = ysgn * n_.decision_function(Xb)
        fs, fm = len(n_.support_) / 30, float(np.mean(mg < 1 - 1e-5))
        print(f"   nu={nu_}: SV fraction {fs:.4f}, margin-error fraction {fm:.4f}")
        report(f"NuSVC(nu={nu_}): margin errors <= nu <= support vectors", fm <= nu_ + 1e-12 <= fs + 2e-12)
    yimb = np.array([3] * 25 + [7] * 5); Ximb = Xb.copy(); Ximb[25:] += 2
    report("NuSVC(nu=0.5) on 25/5 classes (max feasible nu = 2*min(n_+, n_-)/n = 1/3) raises ValueError 'specified nu is infeasible'", expect_raises(lambda: NuSVC(nu=0.5).fit(Ximb, yimb)))
    report("NuSVC(nu=0.3 < 1/3) on the same data fits", not expect_raises(lambda: NuSVC(nu=0.3).fit(Ximb, yimb)))
    report("NuSVC(nu=1.5) raises ValueError (nu in (0, 1])", expect_raises(lambda: NuSVC(nu=1.5).fit(Xb, yb)))
    nucw = NuSVC(nu=0.5, kernel="rbf", gamma=0.7, tol=1e-10, class_weight={3: 1.0, 7: 5.0}).fit(Xb, yb)
    nusw = NuSVC(nu=0.5, kernel="rbf", gamma=0.7, tol=1e-10).fit(Xb, yb, sample_weight=np.where(yb == 7, 2.0, 1.0))
    print(f"   NuSVC class_weight={{3:1, 7:5}}: max |decision diff vs unweighted| {maxdiff(nucw.decision_function(Xq), nus.decision_function(Xq)):.2e}; "
          f"sample_weight 2 on class 7: {maxdiff(nusw.decision_function(Xq), nus.decision_function(Xq)):.2e}")
    report("NuSVC(class_weight={3: 1, 7: 5}) changes the fit (documented parameter 'Set the parameter C of class i to class_weight[i]*C')", maxdiff(nucw.decision_function(Xq), nus.decision_function(Xq)) > 1e-6)
    report("NuSVC(sample_weight = 2 on class 7) changes the fit (documented 'Per-sample weights. Rescale C per sample')", maxdiff(nusw.decision_function(Xq), nus.decision_function(Xq)) > 1e-6)
section('svm.NuSVC', _s03)

def _s04():
    global a, an, aw, bound, eps_hat, f, fn, free, n_err, nsv, nsvr, resid, rn, svr, svr_lin, svrw, swr, xq1, xr, yr
    reseed(4)
    xr = np.linspace(0, 6, 40)[:, None]; yr = np.sin(xr.ravel()) + 0.15 * rs.randn(40)
    svr = SVR(kernel="rbf", gamma=0.8, C=2.0, epsilon=0.1, tol=1e-10).fit(xr, yr)
    f = svr.predict(xr); resid = yr - f; a = np.zeros(40); a[svr.support_] = svr.dual_coef_.ravel()
    free = (np.abs(a) > 1e-9) & (np.abs(a) < 2.0 - 1e-9); bound = np.abs(a) >= 2.0 - 1e-9; nsv = np.abs(a) <= 1e-9
    print(f"   SVR: n_SV {len(svr.support_)} free {int(free.sum())} bounded {int(bound.sum())} non-SV {int(nsv.sum())}; max|dual_coef_| {np.abs(a).max():.6f}; sum {a.sum():.2e}")
    print(f"      |y-f| non-SV max {np.abs(resid[nsv]).max():.6f}; free {np.round(np.abs(resid[free]), 7).tolist()}; bounded min {np.abs(resid[bound]).min():.6f}")
    xq1 = np.array([[0.5], [2.2], [4.9], [7.0]])
    report("SVR predict = dual_coef_ @ K(SV, x) + intercept_ (rbf coded independently)", allclose(svr.predict(xq1), (svr.dual_coef_ @ kern("rbf", svr.support_vectors_, xq1, gamma=0.8) + svr.intercept_).ravel(), 1e-9, 1e-9))
    report("SVR dual coefficients alpha_i - alpha_i^* in [-C, C], sum = 0, support_ = nonzero ones", np.all(np.abs(a) <= 2.0 * (1 + 1e-9)) and abs(a.sum()) <= 1e-9 and set(svr.support_.tolist()) == set(np.flatnonzero(np.abs(a) > 0).tolist()))
    report("SVR epsilon tube (KKT, 1e-6: libsvm caches the kernel in single precision, 'typedef float Qfloat'): non-SVs |y - f| <= epsilon; free SVs |y - f| = epsilon; bounded SVs |y - f| >= epsilon",
           np.all(np.abs(resid[nsv]) <= 0.1 + 1e-6) and np.all(np.abs(np.abs(resid[free]) - 0.1) <= 1e-6) and np.all(np.abs(resid[bound]) >= 0.1 - 1e-6))
    report("SVR sign: dual_coef_i > 0 iff the target lies above the tube (y_i - f_i >= epsilon, 1e-6)", np.all(resid[a > 1e-9] >= 0.1 - 1e-6) and np.all(resid[a < -1e-9] <= -0.1 + 1e-6))
    swr = rs.uniform(0.5, 3.0, 40)
    svrw = SVR(kernel="rbf", gamma=0.8, C=2.0, epsilon=0.1, tol=1e-10).fit(xr, yr, sample_weight=swr)
    aw = np.zeros(40); aw[svrw.support_] = svrw.dual_coef_.ravel()
    report("SVR(sample_weight): |dual_coef_i| <= C * sample_weight[i] and some SV sits at that bound", np.all(np.abs(aw) <= 2.0 * swr * (1 + 1e-9)) and np.any(np.abs(np.abs(aw) - 2.0 * swr) <= 1e-9 * 2.0 * swr))
    nsvr = NuSVR(nu=0.3, C=2.0, kernel="rbf", gamma=0.8, tol=1e-10).fit(xr, yr)
    fn = nsvr.predict(xr); rn = np.abs(yr - fn); an = np.zeros(40); an[nsvr.support_] = nsvr.dual_coef_.ravel()
    eps_hat = rn[nsvr.support_].min(); n_err = int(np.sum(rn > eps_hat + 1e-6))
    print(f"   NuSVR(nu=0.3): n_SV {len(nsvr.support_)} (fraction {len(nsvr.support_)/40:.3f}); tube half-width recovered from the SVs {eps_hat:.6f}; points outside the tube {n_err} (fraction {n_err/40:.3f})")
    report("NuSVR(nu=0.3): fraction of SVs >= nu and fraction of points outside the (automatically chosen) epsilon tube <= nu; non-SVs inside the tube; |dual_coef_| <= C",
           len(nsvr.support_) / 40 >= 0.3 - 1e-12 and n_err / 40 <= 0.3 + 1e-12 and np.all(rn[an == 0] <= eps_hat + 1e-6) and np.all(np.abs(an) <= 2.0 * (1 + 1e-9)))
    report("NuSVR predict = dual_coef_ @ K(SV, x) + intercept_", allclose(nsvr.predict(xq1), (nsvr.dual_coef_ @ kern("rbf", nsvr.support_vectors_, xq1, gamma=0.8) + nsvr.intercept_).ravel(), 1e-9, 1e-9))
    report("SVR(epsilon=0): every training point is a support vector unless the residual is exactly 0 (tube of width 0)", (lambda m: len(m.support_) >= 39)(SVR(kernel="rbf", gamma=0.8, C=2.0, epsilon=0.0, tol=1e-10).fit(xr, yr)))
    svr_lin = SVR(kernel="linear", C=1.0, epsilon=0.2, tol=1e-10).fit(xr, yr)
    report("SVR(linear) coef_ = dual_coef_ @ support_vectors_", allclose(svr_lin.coef_, svr_lin.dual_coef_ @ svr_lin.support_vectors_))
section('svm.SVR / NuSVR: epsilon tube, dual bounds, predict recomputed', _s04)

def _s05():
    global Xo, ao, dfo, oc, oc2, off, ss
    reseed(5)
    Xo = rs.randn(50, 2); Xo[0] = [6.0, 6.0]; Xo[1] = [-6.0, 5.0]; Xo[2] = [5.0, -6.0]
    oc = OneClassSVM(nu=0.2, kernel="rbf", gamma=0.5, tol=1e-10).fit(Xo)
    ss = oc.score_samples(Xo); dfo = oc.decision_function(Xo); ao = oc.dual_coef_.ravel()
    off = float(np.ravel(oc.offset_)[0])
    print(f"   offset_ {oc.offset_!r} (documented 'float') intercept_ {oc.intercept_[0]:.6f}; n_SV {len(oc.support_)} (fraction {len(oc.support_)/50:.2f}); outliers on training data {int((oc.predict(Xo) == -1).sum())} (fraction {(oc.predict(Xo) == -1).mean():.2f}); dual_coef_ in [{ao.min():.4f}, {ao.max():.4f}], sum {ao.sum():.6f} (nu*n = {0.2*50})")
    report("OneClassSVM offset_ is a Python/numpy scalar as documented ('offset_ : float')", np.ndim(oc.offset_) == 0, f"(got {type(oc.offset_).__name__} of shape {np.shape(oc.offset_)})")
    report("OneClassSVM decision_function = score_samples - offset_ (documented)", allclose(dfo, ss - off, 1e-12, 1e-12))
    report("OneClassSVM offset_ = -intercept_ (documented 'The offset is the opposite of intercept_')", close(off, -oc.intercept_[0], 1e-12))
    report("OneClassSVM score_samples = dual_coef_ @ K(SV, x) (rbf coded independently, no intercept)", allclose(ss, (oc.dual_coef_ @ kern("rbf", oc.support_vectors_, Xo, gamma=0.5)).ravel(), 1e-9, 1e-9))
    report("OneClassSVM predict = +1 iff decision_function > 0 else -1", np.array_equal(oc.predict(Xo), np.where(dfo > 0, 1, -1)))
    n_err = int(np.sum(dfo < -1e-6)); n_bnd = int(np.sum(np.abs(dfo) <= 1e-6))
    print(f"   decision_function < -1e-6 (training errors, xi > 0): {n_err}; |decision| <= 1e-6 (on the boundary: free SVs, which predict() labels -1 when the value rounds to <= 0): {n_bnd}")
    report("OneClassSVM(nu=0.2): fraction of training errors (decision_function < 0 beyond 1e-6) <= nu <= fraction of support vectors (documented 'upper bound on the fraction of training errors and a lower bound of the fraction of support vectors')", n_err / 50 <= 0.2 + 1e-12 <= len(oc.support_) / 50 + 2e-12)
    report("OneClassSVM dual: 0 <= dual_coef_ <= 1 and sum(dual_coef_) = nu * n (libsvm's scaling of the one-class dual: alpha in [0,1], sum alpha = nu l)", np.all(ao >= -1e-12) and np.all(ao <= 1 + 1e-9) and close(ao.sum(), 0.2 * 50, 1e-8))
    report("OneClassSVM: the three isolated far-away points are flagged as outliers (decision_function < 0)", np.all(oc.predict(Xo[:3]) == -1), f"(decision {np.round(dfo[:3], 4).tolist()})")
    oc2 = OneClassSVM(nu=0.2, kernel="rbf", gamma=0.5, tol=1e-10, shrinking=False).fit(Xo)
    report("OneClassSVM shrinking=False same solution", allclose(oc2.dual_coef_, oc.dual_coef_, 1e-6, 1e-6) and close(float(np.ravel(oc2.offset_)[0]), off, 1e-6))
section('svm.OneClassSVM', _s05)

def _s06():
    global D_ref, J1_lib, J1_ref, J_cs, J_cs_0, J_cs_at_ovr, J_lib, J_ref, J_ref0, P_lib, P_ref, Q, Xl, Xl3, Xt, Xwide, _, b_l1, bk, cs_obj, dual_obj, hinge_obj, k, l100, l1_, l1_primal, l1sq_obj, la, law, lbfgs, lcs, lcw, ld, lfi, lh, ll1, lov, lsq, rd, rl1, rows_ok, s, sqh_obj, sqh_w, th_cw, th_lib, th_ref, th_ref0, th_un, w_l1, w_ref, worse, yl, yl3, ywide
    reseed(6)
    Xl = rs.randn(40, 3); yl = np.where(Xl @ np.array([1.0, -0.5, 0.2]) + 0.3 * rs.randn(40) > 0, 1, -1)
    Xwide = np.random.RandomState(612).randn(6, 12); ywide = np.array([1, -1, 1, -1, 1, -1])
    def sqh_obj(theta, X, y, C, s):
        w = theta[:-1]; v = theta[-1]; m = y * (X @ w + s * v); act = np.maximum(0, 1 - m)
        val = 0.5 * (w @ w + v * v) + C * np.sum(act ** 2)
        gw = w - 2 * C * (X.T @ (act * y)); gv = v - 2 * C * s * np.sum(act * y)
        return val, np.append(gw, gv)
    def hinge_obj(theta, X, y, C, s):
        w = theta[:-1]; v = theta[-1]; m = y * (X @ w + s * v)
        return 0.5 * (w @ w + v * v) + C * np.sum(np.maximum(0, 1 - m))
    def lbfgs(fun, x0, args):
        r = optimize.minimize(fun, x0, args=args, jac=True, method="L-BFGS-B", options=dict(gtol=1e-13, ftol=1e-16, maxiter=20000, maxfun=100000))
        return r.x, r.fun
    for s in (1.0, 10.0):
        lsq = LinearSVC(loss="squared_hinge", penalty="l2", dual=False, C=1.0, tol=1e-12, max_iter=100000, intercept_scaling=s).fit(Xl, yl)
        th_lib = np.append(lsq.coef_.ravel(), lsq.intercept_[0] / s)
        th_ref, J_ref = lbfgs(sqh_obj, np.zeros(4), (Xl, yl.astype(float), 1.0, s))
        J_lib = sqh_obj(th_lib, Xl, yl.astype(float), 1.0, s)[0]
        print(f"   squared_hinge/l2/dual=False, intercept_scaling={s}: objective lib {J_lib:.12f} ref(L-BFGS) {J_ref:.12f}; coef_ {lsq.coef_.ravel().tolist()} intercept_ {lsq.intercept_[0]:.6f}; ref coef {th_ref[:-1].tolist()} ref intercept {s*th_ref[-1]:.6f}")
        report(f"LinearSVC(squared_hinge, l2, dual=False, intercept_scaling={s}) minimises 1/2(||w||^2 + (b/s)^2) + C sum max(0, 1 - y(w.x + b))^2: objective within 1e-8 of the L-BFGS reference and coef_ within 1e-5",
               abs(J_lib - J_ref) <= 1e-8 * J_ref and allclose(th_lib[:-1], th_ref[:-1], 1e-5, 1e-5) and close(lsq.intercept_[0], s * th_ref[-1], 1e-5, 1e-5))
        ld = LinearSVC(loss="squared_hinge", penalty="l2", dual=True, C=1.0, tol=1e-12, max_iter=100000, intercept_scaling=s).fit(Xl, yl)
        report(f"LinearSVC(squared_hinge, dual=True, intercept_scaling={s}) solves the same problem: coef_/intercept_ within 1e-5 of dual=False", allclose(ld.coef_, lsq.coef_, 1e-5, 1e-5) and allclose(ld.intercept_, lsq.intercept_, 1e-5, 1e-5))
    l1_ = LinearSVC(intercept_scaling=1.0, dual=False, tol=1e-12, max_iter=100000).fit(Xl, yl); l100 = LinearSVC(intercept_scaling=100.0, dual=False, tol=1e-12, max_iter=100000).fit(Xl, yl)
    th_un, _ = lbfgs(lambda t, X, y, C, s: (lambda v: (v[0] - 0.5 * t[-1] ** 2, np.append(v[1][:-1], v[1][-1] - t[-1])))(sqh_obj(t, X, y, C, s)), np.zeros(4), (Xl, yl.astype(float), 1.0, 1.0))
    print(f"   intercept_: scaling 1 -> {l1_.intercept_[0]:.6f}, scaling 100 -> {l100.intercept_[0]:.6f}, unregularised intercept (reference) {th_un[-1]:.6f}")
    report("LinearSVC intercept_scaling=100 brings the intercept closer to the unregularised-intercept solution than intercept_scaling=1 (documented 'the higher the value, the lower the impact of regularization on it')",
           abs(l100.intercept_[0] - th_un[-1]) < abs(l1_.intercept_[0] - th_un[-1]))
    if V >= (1, 3):
        la = LinearSVC(dual="auto", tol=1e-12, max_iter=100000).fit(Xl, yl)
        report("LinearSVC(dual='auto') on n_samples > n_features gives the dual=False solution (coef_ within 1e-6)", allclose(la.coef_, LinearSVC(dual=False, tol=1e-12, max_iter=100000).fit(Xl, yl).coef_, 1e-6, 1e-6))
        law = LinearSVC(dual="auto", tol=1e-12, max_iter=100000).fit(Xwide, ywide)
        report("LinearSVC(dual='auto') on n_samples < n_features gives the dual=True solution (coef_ within 1e-6)", allclose(law.coef_, LinearSVC(dual=True, tol=1e-12, max_iter=100000).fit(Xwide, ywide).coef_, 1e-6, 1e-6))
    lwt = LinearSVC(dual=True, tol=1e-12, max_iter=100000).fit(Xwide, ywide); lwf = LinearSVC(dual=False, tol=1e-12, max_iter=100000).fit(Xwide, ywide)
    report("LinearSVC(squared_hinge) dual=True and dual=False agree on n_samples < n_features (6 x 12): coef_, intercept_ within 1e-5", allclose(lwt.coef_, lwf.coef_, 1e-5, 1e-5) and allclose(lwt.intercept_, lwf.intercept_, 1e-5, 1e-5))
    # hinge: reference = box-constrained dual solved with L-BFGS-B
    Xt = np.c_[Xl, np.ones(40)]; Q = (yl[:, None] * yl[None, :]) * (Xt @ Xt.T)
    def dual_obj(al): return 0.5 * al @ Q @ al - al.sum(), Q @ al - 1
    rd = optimize.minimize(dual_obj, np.zeros(40), jac=True, method="L-BFGS-B", bounds=[(0, 1.0)] * 40, options=dict(gtol=1e-14, ftol=1e-16, maxiter=50000))
    w_ref = Xt.T @ (rd.x * yl); D_ref = -rd.fun
    lh = LinearSVC(loss="hinge", penalty="l2", dual=True, C=1.0, tol=1e-10, max_iter=200000, random_state=0).fit(Xl, yl)
    th_lib = np.append(lh.coef_.ravel(), lh.intercept_[0])
    P_lib = hinge_obj(th_lib, Xl, yl.astype(float), 1.0, 1.0); P_ref = hinge_obj(w_ref, Xl, yl.astype(float), 1.0, 1.0)
    print(f"   hinge/l2 (dual, tol=1e-10): primal lib {P_lib:.10f}; reference dual (L-BFGS-B box QP) {D_ref:.10f}, primal at ref w {P_ref:.10f}; coef_ {lh.coef_.ravel().tolist()} ref {w_ref[:-1].tolist()}")
    report("LinearSVC(loss='hinge', tol=1e-10) minimises 1/2||w~||^2 + C sum max(0, 1 - y w~.x~): primal at coef_ within 1e-7 of the dual optimum of a box-constrained QP reference (weak duality: primal >= dual)",
           P_lib >= D_ref - 1e-9 and P_lib - D_ref <= 1e-7 * max(1, P_lib) and allclose(th_lib, w_ref, 1e-4, 1e-4))
    tol_sweep("LinearSVC(loss='hinge', dual=True)", lambda t: LinearSVC(loss="hinge", penalty="l2", dual=True, C=1.0, tol=t, max_iter=200000, random_state=0),
              Xl, yl, lambda m: hinge_obj(np.append(m.coef_.ravel(), m.intercept_[0]), Xl, yl.astype(float), 1.0, 1.0), D_ref)
    report("LinearSVC(penalty='l1', loss='hinge') raises ValueError (documented 'not supported')", expect_raises(lambda: LinearSVC(penalty="l1", loss="hinge", dual=True).fit(Xl, yl)))
    # l1 penalty: split variables, L-BFGS-B with bounds
    def l1sq_obj(z, X, y, C):
        p = X.shape[1]; u, v, bp, bm = z[:p], z[p:2 * p], z[2 * p], z[2 * p + 1]
        w = u - v; b = bp - bm; m = y * (X @ w + b); act = np.maximum(0, 1 - m)
        val = np.sum(u) + np.sum(v) + bp + bm + C * np.sum(act ** 2)
        gw = -2 * C * (X.T @ (act * y)); gb = -2 * C * np.sum(act * y)
        return val, np.concatenate([1 + gw, 1 - gw, [1 + gb, 1 - gb]])
    rl1 = optimize.minimize(l1sq_obj, np.zeros(8), args=(Xl, yl.astype(float), 0.5), jac=True, method="L-BFGS-B", bounds=[(0, None)] * 8, options=dict(gtol=1e-14, ftol=1e-16, maxiter=50000))
    w_l1 = rl1.x[:3] - rl1.x[3:6]; b_l1 = rl1.x[6] - rl1.x[7]
    ll1 = LinearSVC(penalty="l1", loss="squared_hinge", dual=False, C=0.5, tol=1e-12, max_iter=200000).fit(Xl, yl)
    def l1_primal(w, b, X, y, C): return np.sum(np.abs(w)) + abs(b) + C * np.sum(np.maximum(0, 1 - y * (X @ w + b)) ** 2)
    J1_lib = l1_primal(ll1.coef_.ravel(), ll1.intercept_[0], Xl, yl, 0.5); J1_ref = l1_primal(w_l1, b_l1, Xl, yl, 0.5)
    print(f"   l1/squared_hinge C=0.5: objective lib {J1_lib:.10f} ref {J1_ref:.10f}; coef_ {ll1.coef_.ravel().tolist()} intercept_ {ll1.intercept_[0]:.6f}; ref {w_l1.tolist()} {b_l1:.6f}")
    report("LinearSVC(penalty='l1', squared_hinge, dual=False) minimises ||w~||_1 + C sum max(0, 1 - y w~.x~)^2 (intercept penalised too): objective within 1e-7 of the split-variable L-BFGS-B reference, coef_ within 1e-4",
           abs(J1_lib - J1_ref) <= 1e-7 * J1_ref and allclose(ll1.coef_.ravel(), w_l1, 1e-4, 1e-4) and close(ll1.intercept_[0], b_l1, 1e-4, 1e-4))
    # multi-class
    Xl3 = np.vstack([Xl, Xl + [3, 0, 0]]); yl3 = np.r_[np.where(yl == 1, 0, 1), np.full(40, 2)]
    lov = LinearSVC(dual=False, tol=1e-12, max_iter=100000, C=0.7).fit(Xl3, yl3)
    rows_ok = True
    for k in range(3):
        bk = LinearSVC(dual=False, tol=1e-12, max_iter=100000, C=0.7).fit(Xl3, np.where(yl3 == k, 1, -1))
        rows_ok &= allclose(lov.coef_[k], bk.coef_.ravel(), 1e-6, 1e-6) and close(lov.intercept_[k], bk.intercept_[0], 1e-6, 1e-6)
    report("LinearSVC(multi_class='ovr') rows of coef_/intercept_ = the n_classes separate one-vs-rest binary fits (documented), decision_function = X @ coef_.T + intercept_",
           rows_ok and allclose(lov.decision_function(Xl3), Xl3 @ lov.coef_.T + lov.intercept_, 1e-9, 1e-9) and np.array_equal(lov.predict(Xl3), np.argmax(lov.decision_function(Xl3), 1)))
    lcs = LinearSVC(multi_class="crammer_singer", tol=1e-12, max_iter=100000, C=0.7).fit(Xl3, yl3)
    def cs_obj(W, b, X, y, C):
        S = X @ W.T + b; n = len(y)
        loss = 0.0
        for i in range(n):
            e = np.ones(3); e[y[i]] = 0
            loss += np.max(e - (S[i, y[i]] - S[i]))
        return 0.5 * (np.sum(W ** 2) + np.sum(b ** 2)) + C * loss
    J_cs = cs_obj(lcs.coef_, lcs.intercept_, Xl3, yl3, 0.7); J_cs_at_ovr = cs_obj(lov.coef_, lov.intercept_, Xl3, yl3, 0.7); J_cs_0 = cs_obj(np.zeros((3, 3)), np.zeros(3), Xl3, yl3, 0.7)
    print(f"   crammer_singer objective at its solution {J_cs:.6f}; at the ovr solution {J_cs_at_ovr:.6f}; at 0 {J_cs_0:.6f}")
    report("LinearSVC(multi_class='crammer_singer') optimises the joint objective 1/2 sum_k ||w~_k||^2 + C sum_i max_k(1 - delta_{k,y_i} - (w~_{y_i} - w~_k).x~_i): lower at its solution than at the ovr solution and at 0; decision_function recomputed",
           J_cs < J_cs_at_ovr and J_cs < J_cs_0 and allclose(lcs.decision_function(Xl3), Xl3 @ lcs.coef_.T + lcs.intercept_, 1e-9, 1e-9))
    # subgradient optimality check for crammer-singer: random perturbations do not decrease the objective
    worse = all(cs_obj(lcs.coef_ + 1e-4 * rs.randn(3, 3), lcs.intercept_ + 1e-4 * rs.randn(3), Xl3, yl3, 0.7) >= J_cs - 1e-12 for _ in range(200))
    report("LinearSVC(crammer_singer): 200 random perturbations of size 1e-4 of (coef_, intercept_) never decrease the joint objective (local optimality of a convex problem)", worse)
    # independent reference: the Crammer-Singer primal as a QP, 0.5||W~||^2 + C sum xi_i s.t.
    # (w~_{y_i} - w~_m).x~_i + xi_i >= 1 for m != y_i, xi_i >= 0, solved with scipy SLSQP
    X3t = np.c_[Xl3, np.ones(len(yl3))]; n3, p3 = X3t.shape; nv = 3 * p3 + n3; rows = []
    for i in range(n3):
        for m_ in range(3):
            if m_ == yl3[i]: continue
            r_ = np.zeros(nv); r_[yl3[i] * p3:(yl3[i] + 1) * p3] += X3t[i]; r_[m_ * p3:(m_ + 1) * p3] -= X3t[i]; r_[3 * p3 + i] = 1.0; rows.append(r_)
    Acs = np.array(rows)
    def cs_qp(z): return 0.5 * z[:3 * p3] @ z[:3 * p3] + 0.7 * z[3 * p3:].sum(), np.concatenate([z[:3 * p3], np.full(n3, 0.7)])
    rcs = optimize.minimize(cs_qp, np.concatenate([np.zeros(3 * p3), np.ones(n3)]), jac=True, method="SLSQP",
                            constraints=[dict(type="ineq", fun=lambda z: Acs @ z - 1.0, jac=lambda z: Acs)], bounds=[(None, None)] * (3 * p3) + [(0, None)] * n3,
                            options=dict(ftol=1e-14, maxiter=2000))
    Wcs = rcs.x[:3 * p3].reshape(3, p3); J_cs_ref = cs_obj(Wcs[:, :-1], Wcs[:, -1], Xl3, yl3, 0.7)
    print(f"   crammer_singer SLSQP reference: status '{rcs.message}', min constraint slack {np.min(Acs @ rcs.x - 1.0):.1e}, objective {J_cs_ref:.10f} vs library {J_cs:.10f}; max |coef diff| {maxdiff(np.c_[lcs.coef_, lcs.intercept_], Wcs):.2e}")
    report("LinearSVC(crammer_singer, tol=1e-12) objective within 1e-6 (relative) of an SLSQP solution of the Crammer-Singer primal QP (intercept as a regularised synthetic feature), coef_/intercept_ within 1e-3",
           np.min(Acs @ rcs.x - 1.0) >= -1e-7 and abs(J_cs - J_cs_ref) <= 1e-6 * J_cs_ref and allclose(np.c_[lcs.coef_, lcs.intercept_], Wcs, 1e-3, 1e-3))
    lfi = LinearSVC(fit_intercept=False, dual=False, tol=1e-12, max_iter=100000).fit(Xl, yl)
    def sqh_noint(t, X, y, C):
        v, g = sqh_obj(np.append(t, 0.0), X, y, C, 1.0); return v, g[:-1]
    th_ref0, J_ref0 = lbfgs(sqh_noint, np.zeros(3), (Xl, yl.astype(float), 1.0))
    report("LinearSVC(fit_intercept=False) intercept_ = 0 and coef_ minimises the objective without intercept (L-BFGS reference within 1e-5)", np.all(lfi.intercept_ == 0) and allclose(lfi.coef_.ravel(), th_ref0, 1e-5, 1e-5))
    lcw = LinearSVC(dual=False, tol=1e-12, max_iter=100000, class_weight={1: 3.0, -1: 1.0}).fit(Xl, yl)
    def sqh_w(theta, X, y, Cvec, s):
        w = theta[:-1]; v = theta[-1]; m = y * (X @ w + s * v); act = np.maximum(0, 1 - m)
        return 0.5 * (w @ w + v * v) + np.sum(Cvec * act ** 2), np.append(w - 2 * (X.T @ (Cvec * act * y)), v - 2 * s * np.sum(Cvec * act * y))
    th_cw, _ = lbfgs(sqh_w, np.zeros(4), (Xl, yl.astype(float), np.where(yl == 1, 3.0, 1.0), 1.0))
    report("LinearSVC(class_weight={1: 3}) = per-sample C_i = C * class_weight[y_i] in the objective (L-BFGS reference within 1e-5)", allclose(np.append(lcw.coef_.ravel(), lcw.intercept_[0]), th_cw, 1e-5, 1e-5))
section('svm.LinearSVC: documented primal objectives vs scipy.optimize references', _s06)

def _s07():
    global D_svr, J2, J_ref, P_l, P_r, Qr, Xr2, Xr2t, eps_primal, lsvr, lsvr2, lsvr3, lsvr_s, m_, rsv, sqeps_obj, svr_dual, sweep, tol_, w_svr, wt2, wt_lib, wt_ref, yr2
    reseed(7)
    Xr2 = rs.randn(30, 2); yr2 = Xr2 @ np.array([2.0, -1.0]) + 0.5 + 0.3 * rs.randn(30)
    Xr2t = np.c_[Xr2, np.ones(30)]
    def eps_primal(wt, X, y, C, eps): return 0.5 * wt @ wt + C * np.sum(np.maximum(0, np.abs(y - X @ wt) - eps))
    Qr = Xr2t @ Xr2t.T
    def svr_dual(z, C, eps):
        a, b = z[:30], z[30:]; beta = a - b; Qb = Qr @ beta
        return 0.5 * beta @ Qb + eps * np.sum(a + b) - yr2 @ beta, np.concatenate([Qb + eps - yr2, -Qb + eps + yr2])
    rsv = optimize.minimize(svr_dual, np.zeros(60), args=(1.0, 0.2), jac=True, method="L-BFGS-B", bounds=[(0, 1.0)] * 60, options=dict(gtol=1e-14, ftol=1e-16, maxiter=50000))
    w_svr = Xr2t.T @ (rsv.x[:30] - rsv.x[30:]); D_svr = -rsv.fun
    lsvr = LinearSVR(loss="epsilon_insensitive", C=1.0, epsilon=0.2, tol=1e-10, max_iter=200000, random_state=0).fit(Xr2, yr2)
    wt_lib = np.append(lsvr.coef_, lsvr.intercept_[0])
    P_l = eps_primal(wt_lib, Xr2t, yr2, 1.0, 0.2); P_r = eps_primal(w_svr, Xr2t, yr2, 1.0, 0.2)
    print(f"   epsilon_insensitive: primal lib {P_l:.10f}; reference dual {D_svr:.10f}, primal at ref {P_r:.10f}; coef_ {lsvr.coef_.tolist()} intercept_ {lsvr.intercept_[0]:.6f}; ref {w_svr.tolist()}")
    report("LinearSVR(epsilon_insensitive, tol=1e-10) minimises 1/2||w~||^2 + C sum max(0, |y - w~.x~| - eps): primal within 1e-7 of the dual optimum (box-constrained QP reference, weak duality holds), coef_ within 1e-4",
           P_l >= D_svr - 1e-9 and P_l - D_svr <= 1e-7 * max(1, P_l) and allclose(wt_lib, w_svr, 1e-4, 1e-4))
    tol_sweep("LinearSVR(loss='epsilon_insensitive')", lambda t: LinearSVR(loss="epsilon_insensitive", C=1.0, epsilon=0.2, tol=t, max_iter=200000, random_state=0),
              Xr2, yr2, lambda m: eps_primal(np.append(m.coef_, m.intercept_[0]), Xr2t, yr2, 1.0, 0.2), D_svr)
    def sqeps_obj(wt, X, y, C, eps):
        r = y - X @ wt; ex = np.sign(r) * np.maximum(0, np.abs(r) - eps)
        return 0.5 * wt @ wt + C * np.sum(ex ** 2), wt - 2 * C * (X.T @ ex)
    wt_ref, J_ref = lbfgs(sqeps_obj, np.zeros(3), (Xr2t, yr2, 1.0, 0.2))
    lsvr2 = LinearSVR(loss="squared_epsilon_insensitive", C=1.0, epsilon=0.2, tol=1e-12, max_iter=200000, dual=False).fit(Xr2, yr2) if V >= (1, 3) else LinearSVR(loss="squared_epsilon_insensitive", C=1.0, epsilon=0.2, tol=1e-12, max_iter=200000, dual=False).fit(Xr2, yr2)
    wt2 = np.append(lsvr2.coef_, lsvr2.intercept_[0]); J2 = sqeps_obj(wt2, Xr2t, yr2, 1.0, 0.2)[0]
    print(f"   squared_epsilon_insensitive (dual=False): objective lib {J2:.10f} ref {J_ref:.10f}; coef_ {lsvr2.coef_.tolist()} ref {wt_ref[:-1].tolist()}")
    report("LinearSVR(squared_epsilon_insensitive, dual=False) minimises 1/2||w~||^2 + C sum max(0, |y - w~.x~| - eps)^2: objective within 1e-8 of the L-BFGS reference, coef_ within 1e-5", abs(J2 - J_ref) <= 1e-8 * J_ref and allclose(wt2, wt_ref, 1e-5, 1e-5))
    lsvr3 = LinearSVR(loss="squared_epsilon_insensitive", C=1.0, epsilon=0.2, tol=1e-12, max_iter=200000, dual=True).fit(Xr2, yr2)
    report("LinearSVR(squared_epsilon_insensitive, dual=True) agrees with dual=False (1e-5)", allclose(np.append(lsvr3.coef_, lsvr3.intercept_[0]), wt2, 1e-5, 1e-5))
    report("LinearSVR predict = X @ coef_ + intercept_", allclose(lsvr.predict(Xr2), Xr2 @ lsvr.coef_ + lsvr.intercept_, 1e-12, 1e-12))
    Xr2s = np.c_[Xr2, np.full(30, 50.0)]; Qs = Xr2s @ Xr2s.T
    def svr_dual_s(z):
        be = z[:30] - z[30:]; Qb = Qs @ be
        return 0.5 * be @ Qb + 0.2 * np.sum(z) - yr2 @ be, np.concatenate([Qb + 0.2 - yr2, -Qb + 0.2 + yr2])
    rss = optimize.minimize(svr_dual_s, np.zeros(60), jac=True, method="L-BFGS-B", bounds=[(0, 1.0)] * 60, options=dict(gtol=1e-14, ftol=1e-16, maxiter=50000))
    ws = Xr2s.T @ (rss.x[:30] - rss.x[30:])
    lsvr_s = LinearSVR(C=1.0, epsilon=0.2, tol=1e-10, max_iter=200000, intercept_scaling=50.0, random_state=0).fit(Xr2, yr2)
    Ps = eps_primal(np.append(lsvr_s.coef_, lsvr_s.intercept_[0] / 50.0), Xr2s, yr2, 1.0, 0.2)
    print(f"   LinearSVR intercept_scaling=50: intercept_ {lsvr_s.intercept_[0]:.8f} (scaling 1: {lsvr.intercept_[0]:.8f}); reference intercept 50*w_b = {50 * ws[-1]:.8f}; primal lib {Ps:.10f} vs reference dual {-rss.fun:.10f}")
    report("LinearSVR(intercept_scaling=50) minimises 1/2(||w||^2 + (b/50)^2) + C sum max(0, |y - w.x - b| - eps) (documented synthetic feature of value intercept_scaling, intercept_ = intercept_scaling * its weight): primal within 1e-7 of the box-QP dual optimum, intercept_ within 1e-4",
           Ps - (-rss.fun) <= 1e-7 * max(1, Ps) and close(lsvr_s.intercept_[0], 50 * ws[-1], 1e-4, 1e-4))
    # how often does the dual coordinate descent stall at tol=1e-12? 60 random data sets, each against its own
    # SLSQP reference for the primal QP (min 1/2||w~||^2 + C sum xi, xi >= loss constraints), max_iter=200000
    stall_svr, stall_svc = [], []
    for seed in range(60):
        r0 = np.random.RandomState(seed); Xs_ = r0.randn(30, 2); ys_ = Xs_ @ np.array([2.0, -1.0]) + 0.5 + 0.3 * r0.randn(30); Xst = np.c_[Xs_, np.ones(30)]
        _, opt = qp_ref(Xst, ys_, 1.0, "svr", 0.2)
        with warnings.catch_warnings(record=True) as wl:
            warnings.simplefilter("always"); m12 = LinearSVR(C=1.0, epsilon=0.2, tol=1e-12, max_iter=200000, random_state=0).fit(Xs_, ys_)
        P12 = eps_primal(np.append(m12.coef_, m12.intercept_[0]), Xst, ys_, 1.0, 0.2)
        if P12 - opt > 1e-7 * opt: stall_svr.append((seed, float("%.3g" % (P12 - opt)), int(m12.n_iter_), any(w.category.__name__ == "ConvergenceWarning" for w in wl)))
        r0 = np.random.RandomState(seed); Xc_ = r0.randn(40, 3); yc_ = np.where(Xc_ @ np.array([1.0, -0.5, 0.2]) + 0.3 * r0.randn(40) > 0, 1, -1); Xct = np.c_[Xc_, np.ones(40)]
        _, optc = qp_ref(Xct, yc_.astype(float), 1.0, "hinge")
        with warnings.catch_warnings(record=True) as wl:
            warnings.simplefilter("always"); mc12 = LinearSVC(loss="hinge", C=1.0, tol=1e-12, max_iter=200000, random_state=0).fit(Xc_, yc_)
        wc = np.append(mc12.coef_, mc12.intercept_); Pc12 = 0.5 * wc @ wc + np.sum(np.maximum(0, 1 - yc_ * (Xct @ wc)))
        if Pc12 - optc > 1e-7 * optc: stall_svc.append((seed, float("%.3g" % (Pc12 - optc)), int(np.max(mc12.n_iter_)), any(w.category.__name__ == "ConvergenceWarning" for w in wl)))
    print(f"   tol=1e-12, max_iter=200000, 60 random data sets; (seed, excess primal over the SLSQP reference, n_iter_, ConvergenceWarning):")
    print(f"      LinearSVR(epsilon_insensitive) {stall_svr}\n      LinearSVC(hinge) {stall_svc}")
    report("LinearSVR(epsilon_insensitive) / LinearSVC(hinge) with tol=1e-12, max_iter=200000 reach the optimum (primal within 1e-7 relative of an SLSQP primal-QP reference) on all of 60 random data sets",
           not stall_svr and not stall_svc, f"(not reached: LinearSVR {len(stall_svr)}/60, LinearSVC {len(stall_svc)}/60)")
    for seed, *_ in stall_svr[:1]:
        r0 = np.random.RandomState(seed); Xs_ = r0.randn(30, 2); ys_ = Xs_ @ np.array([2.0, -1.0]) + 0.5 + 0.3 * r0.randn(30); Xst = np.c_[Xs_, np.ones(30)]
        tol_sweep(f"LinearSVR(epsilon_insensitive) on data set {seed}", lambda t: LinearSVR(loss="epsilon_insensitive", C=1.0, epsilon=0.2, tol=t, max_iter=200000, random_state=0),
                  Xs_, ys_, lambda m: eps_primal(np.append(m.coef_, m.intercept_[0]), Xst, ys_, 1.0, 0.2), qp_ref(Xst, ys_, 1.0, "svr", 0.2)[1])
    for seed, *_ in stall_svc[:1]:
        r0 = np.random.RandomState(seed); Xc_ = r0.randn(40, 3); yc_ = np.where(Xc_ @ np.array([1.0, -0.5, 0.2]) + 0.3 * r0.randn(40) > 0, 1, -1); Xct = np.c_[Xc_, np.ones(40)]
        tol_sweep(f"LinearSVC(hinge) on data set {seed}", lambda t: LinearSVC(loss="hinge", C=1.0, tol=t, max_iter=200000, random_state=0),
                  Xc_, yc_, lambda m: (lambda w: 0.5 * w @ w + np.sum(np.maximum(0, 1 - yc_ * (Xct @ w))))(np.append(m.coef_, m.intercept_)), qp_ref(Xct, yc_.astype(float), 1.0, "hinge")[1])
section('svm.LinearSVR vs scipy.optimize references', _s07)

def _s08():
    global Xc, cmin, cmin_log, d0, den_exact, dun, hi, lo, lr_l1, lrhi, lrlo, yc, yun
    reseed(8)
    Xc = rs.randn(20, 3); Xc -= Xc.mean(0); yc = np.array([1, -1] * 10)
    def den_exact(X, y, fit_intercept, s=1.0):
        Y = [F(int(v)) for v in y]; d = max(abs(sum(Y[i] * F(float(X[i, j])) for i in range(len(y)))) for j in range(X.shape[1]))
        if fit_intercept: d = max(d, abs(sum(Y) * F(s)))
        return d
    d0 = den_exact(Xc, yc, True)
    cmin = l1_min_c(Xc, yc, loss="squared_hinge"); cmin_log = l1_min_c(Xc, yc, loss="log")
    print(f"   balanced centred data: max_j |X_j^T y| = {float(d0):.10f}; l1_min_c squared_hinge {cmin:.12f} (0.5/den {float(F(1, 2) / d0):.12f}); log {cmin_log:.12f} (2/den {float(2 / d0):.12f})")
    report("l1_min_c(loss='squared_hinge') = 0.5 / max(|X^T y|_inf, |sum y| * intercept_scaling) (derivation: at w=0 the gradient of C*sum(1 - y w.x)^2 is 2C X^T y; exact Fraction)", close(cmin, float(F(1, 2) / d0), 1e-12))
    report("l1_min_c(loss='log') = 2 / den (gradient of the logistic loss at w=0 is X^T y / 2)", close(cmin_log, float(2 / d0), 1e-12))
    yun = np.array([1] * 14 + [-1] * 6); dun = den_exact(Xc, yun, True, 3.0)
    report("l1_min_c with unbalanced y and intercept_scaling=3: the intercept column enters as |sum y| * intercept_scaling", close(l1_min_c(Xc, yun, loss="squared_hinge", intercept_scaling=3.0), float(F(1, 2) / dun), 1e-12) and close(l1_min_c(Xc, yun, fit_intercept=False), float(F(1, 2) / den_exact(Xc, yun, False)), 1e-12))
    lo = LinearSVC(penalty="l1", loss="squared_hinge", dual=False, C=0.99 * cmin, tol=1e-12, max_iter=200000).fit(Xc, yc)
    hi = LinearSVC(penalty="l1", loss="squared_hinge", dual=False, C=1.01 * cmin, tol=1e-12, max_iter=200000).fit(Xc, yc)
    print(f"   LinearSVC l1 at 0.99*l1_min_c: coef_ {lo.coef_.ravel().tolist()} intercept_ {lo.intercept_.tolist()}; at 1.01*l1_min_c: coef_ {hi.coef_.ravel().tolist()} intercept_ {hi.intercept_.tolist()}")
    report("LinearSVC(penalty='l1') at C = 0.99 * l1_min_c is the null model (coef_ and intercept_ exactly 0)", np.all(lo.coef_ == 0) and np.all(lo.intercept_ == 0))
    report("LinearSVC(penalty='l1') at C = 1.01 * l1_min_c is non-null (documented 'guaranteed not to be empty' for C > l1_min_c)", (np.any(hi.coef_ != 0) or np.any(hi.intercept_ != 0)))
    def lr_l1(C):
        if V >= (1, 8): return LogisticRegression(l1_ratio=1.0, solver="liblinear", C=C, tol=1e-12, max_iter=200000)
        return LogisticRegression(penalty="l1", solver="liblinear", C=C, tol=1e-12, max_iter=200000)
    lrlo = lr_l1(0.99 * cmin_log).fit(Xc, yc); lrhi = lr_l1(1.01 * cmin_log).fit(Xc, yc)
    print(f"   LogisticRegression l1 (liblinear) at 0.99*l1_min_c(log): coef_ {lrlo.coef_.ravel().tolist()} intercept_ {lrlo.intercept_.tolist()}; at 1.01: coef_ {lrhi.coef_.ravel().tolist()} intercept_ {lrhi.intercept_.tolist()}")
    report("LogisticRegression(l1, liblinear) at C = 0.99 * l1_min_c(loss='log') is null and at 1.01 * l1_min_c is non-null", np.all(lrlo.coef_ == 0) and np.all(lrlo.intercept_ == 0) and (np.any(lrhi.coef_ != 0) or np.any(lrhi.intercept_ != 0)))
    report("l1_min_c on all-zero X raises ValueError ('Ill-posed')", expect_raises(lambda: l1_min_c(np.zeros((6, 2)), [1, -1, 1, -1, 1, -1], fit_intercept=False)))
section('svm.l1_min_c', _s08)

def _s09():
    global Dq, Dtr, Xdup, Xexact, Xfar, Xn, Xnq, Xtie, Y2, alg, d_, dd, i_, ii, kd, kdd, ki, km2, knd, knn, kp, kpre, kr, kr2, kr32, krd, kt, kt3, kw_, mode_y, onehot, p2, p99, p_, pd_ref, pe, pr_ref, proba_ref, prr, r_, rc, rc2, rc99, rcm, rd, ref2, ref_knn, ref_radius, ref_rw, ref_u, ref_w, ri, rn_, rr, rrd, wl, wref, y99, ydup, yn, yreg, ytie
    reseed(9)
    def ref_knn(Xt, Xq_, k, p=2.0, w=None):
        Xt = np.asarray(Xt, float); out_d, out_i = [], []
        for q in np.asarray(Xq_, float):
            ds = []
            for i, x in enumerate(Xt):
                diff = np.abs(q - x)
                if w is not None: d = float(np.sum(np.asarray(w) * diff ** p) ** (1.0 / p))
                elif p == np.inf: d = float(diff.max())
                elif p == 2.0: d = math.sqrt(float(np.sum(diff * diff)))
                else: d = float(np.sum(diff ** p) ** (1.0 / p))
                ds.append((d, i))
            ds.sort(); out_d.append([d for d, _ in ds[:k]]); out_i.append([i for _, i in ds[:k]])
        return np.array(out_d), np.array(out_i)
    Xn = rs.rand(25, 2); yn = rs.randint(0, 3, 25); Xnq = rs.rand(6, 2)
    kd, ki = ref_knn(Xn, Xnq, 5)
    knn = KNeighborsClassifier(n_neighbors=5).fit(Xn, yn)
    d_, i_ = knn.kneighbors(Xnq)
    report("KNeighborsClassifier.kneighbors: distances and indices equal the brute-force reference (no ties), distances sorted ascending", allclose(d_, kd, 1e-12, 1e-12) and np.array_equal(i_, ki) and np.all(np.diff(d_, axis=1) >= 0))
    proba_ref = np.array([[np.sum(yn[ki[q]] == c) / 5 for c in range(3)] for q in range(6)])
    report("KNeighborsClassifier(weights='uniform') predict_proba = class counts among the k neighbours / k (rows sum to 1)", allclose(knn.predict_proba(Xnq), proba_ref) and np.array_equal(knn.predict(Xnq), np.argmax(proba_ref, 1)))
    knd = KNeighborsClassifier(n_neighbors=5, weights="distance").fit(Xn, yn)
    wref = 1 / kd; pd_ref = np.array([[np.sum(wref[q][yn[ki[q]] == c]) for c in range(3)] for q in range(6)]); pd_ref /= pd_ref.sum(1, keepdims=True)
    report("KNeighborsClassifier(weights='distance') predict_proba = (sum of 1/d over neighbours of each class) normalised to 1 (documented 'inverse of their distance')", allclose(knd.predict_proba(Xnq), pd_ref, 1e-10, 1e-12) and np.array_equal(knd.predict(Xnq), np.argmax(pd_ref, 1)))
    # exact-match rule
    Xexact = np.vstack([Xn[[3, 8]], Xnq[:1]])
    pe = knd.predict_proba(Xexact)
    onehot = np.array([[1.0 if c == yn[3] else 0.0 for c in range(3)], [1.0 if c == yn[8] else 0.0 for c in range(3)]])
    print(f"   query at training points 3 (class {yn[3]}) and 8 (class {yn[8]}) with weights='distance': proba {pe[:2].tolist()}")
    report("KNeighborsClassifier(weights='distance') query equal to a training point: that point gets weight 1 and the others 0 (rule stated in the source comment of neighbors._base._get_weights; the public docs only say 'inverse of their distance', undefined at 0) -> one-hot proba", allclose(pe[:2], onehot))
    Xdup = np.vstack([Xn, Xn[[3]]]); ydup = np.append(yn, (yn[3] + 1) % 3)
    kdd = KNeighborsClassifier(n_neighbors=5, weights="distance").fit(Xdup, ydup)
    report("KNeighborsClassifier(weights='distance') with two zero-distance training points of different classes: both get weight 1 -> proba 1/2 each", allclose(kdd.predict_proba(Xn[[3]])[0], [0.5 if c in (yn[3], (yn[3] + 1) % 3) else 0.0 for c in range(3)]))
    # ties in the vote
    Xtie = np.array([[0.0], [1.0], [2.0], [3.0]]); ytie = np.array([9, 9, 5, 5])
    for alg in ("brute", "kd_tree", "ball_tree"):
        kt = KNeighborsClassifier(n_neighbors=4, algorithm=alg).fit(Xtie, ytie)
        report(f"KNeighborsClassifier({alg}) tied vote 2-2 between classes 9 and 5 -> the smallest class label (5) and proba 1/2 each (ties are undocumented; predict = classes_[argmax(predict_proba)] and np.argmax / scipy.stats.mode return the first maximum of the sorted classes_)", kt.predict([[1.4]])[0] == 5 and allclose(kt.predict_proba([[1.4]])[0], [0.5, 0.5]))
    kt3 = KNeighborsClassifier(n_neighbors=3).fit(np.array([[0.0], [1.0], [2.0], [10.0], [11.0], [12.0]]), np.array([1, 2, 3, 3, 3, 3]))
    report("KNeighborsClassifier three-way tie 1-1-1 -> smallest class label (1)", kt3.predict([[0.9]])[0] == 1)
    # metrics
    for p_ in (1.0, 3.0, np.inf):
        kp = KNeighborsClassifier(n_neighbors=5, p=p_).fit(Xn, yn); dd, ii = kp.kneighbors(Xnq); rd, ri = ref_knn(Xn, Xnq, 5, p=p_)
        report(f"KNeighborsClassifier(metric='minkowski', p={p_}) kneighbors = reference (sum |d|^p)^(1/p)", allclose(dd, rd, 1e-12, 1e-12) and np.array_equal(ii, ri))
    try:
        kw_ = KNeighborsClassifier(n_neighbors=5, metric="minkowski", p=2, metric_params={"w": [1.0, 3.0]}).fit(Xn, yn); dd, ii = kw_.kneighbors(Xnq); rd, ri = ref_knn(Xn, Xnq, 5, p=2.0, w=[1.0, 3.0])
        report("KNeighborsClassifier(metric_params={'w': [1, 3]}) weighted Minkowski (sum w_j |d_j|^p)^(1/p) = reference", allclose(dd, rd, 1e-12, 1e-12) and np.array_equal(ii, ri))
    except Exception as e:
        print(f"   metric_params w unsupported on this build: {type(e).__name__}: {e}")
    Dtr = np.sqrt(((Xn[:, None] - Xn[None]) ** 2).sum(-1)); Dq = np.sqrt(((Xnq[:, None] - Xn[None]) ** 2).sum(-1))
    kpre = KNeighborsClassifier(n_neighbors=5, metric="precomputed").fit(Dtr, yn)
    report("KNeighborsClassifier(metric='precomputed') with the Euclidean distance matrix = the Euclidean reference (kneighbors, predict_proba)", allclose(kpre.kneighbors(Dq)[0], kd, 1e-12, 1e-12) and np.array_equal(kpre.kneighbors(Dq)[1], ki) and allclose(kpre.predict_proba(Dq), proba_ref))
    report("KNeighborsClassifier(n_neighbors=26 > 25 samples): predict raises ValueError ('Expected n_neighbors <= n_samples_fit')", expect_raises(lambda: KNeighborsClassifier(n_neighbors=26).fit(Xn, yn).predict(Xnq)))
    report("kneighbors(n_neighbors > n_samples_fit) raises ValueError", expect_raises(lambda: knn.kneighbors(Xnq, n_neighbors=26)))
    report("KNeighborsClassifier.kneighbors(X=None) excludes each point from its own neighbours (documented)", np.all(knn.kneighbors(None, n_neighbors=3)[1] != np.arange(25)[:, None]) and np.all(knn.kneighbors(None, n_neighbors=3)[0] > 0))
    # multi-output
    Y2 = np.c_[yn, (yn * 2 + 1) % 4]
    km2 = KNeighborsClassifier(n_neighbors=5).fit(Xn, Y2); p2 = km2.predict_proba(Xnq)
    ref2 = np.array([[np.sum(Y2[ki[q], 1] == c) / 5 for c in sorted(set(Y2[:, 1]))] for q in range(6)])
    report("KNeighborsClassifier multi-output: predict_proba is a list per output, second output = counts/k", isinstance(p2, list) and allclose(p2[0], proba_ref) and allclose(p2[1], ref2))
    # regressor
    yreg = np.sin(3 * Xn[:, 0]) + Xn[:, 1] ** 2
    kr = KNeighborsRegressor(n_neighbors=5).fit(Xn, yreg); krd = KNeighborsRegressor(n_neighbors=5, weights="distance").fit(Xn, yreg)
    ref_u = np.array([np.mean(yreg[ki[q]]) for q in range(6)]); ref_w = np.array([np.sum(wref[q] * yreg[ki[q]]) / np.sum(wref[q]) for q in range(6)])
    report("KNeighborsRegressor(uniform) predict = mean of the k neighbour targets", allclose(kr.predict(Xnq), ref_u, 1e-12, 1e-12))
    report("KNeighborsRegressor(weights='distance') predict = sum(y_i/d_i)/sum(1/d_i)", allclose(krd.predict(Xnq), ref_w, 1e-12, 1e-12))
    report("KNeighborsRegressor(weights='distance') at a training point returns that point's target exactly (zero-distance rule)", close(krd.predict(Xn[[3]])[0], yreg[3], 1e-15, 0))
    kr2 = KNeighborsRegressor(n_neighbors=5).fit(Xn, np.c_[yreg, 2 * yreg])
    report("KNeighborsRegressor multi-output: column-wise means", allclose(kr2.predict(Xnq), np.c_[ref_u, 2 * ref_u], 1e-12, 1e-12))
    kr32 = KNeighborsRegressor(n_neighbors=5).fit(Xn.astype(np.float32), yreg)
    report("KNeighborsRegressor float32 input within 1e-5 of the reference", allclose(kr32.predict(Xnq.astype(np.float32)), ref_u, 1e-5, 1e-5))
    # radius classifier / regressor
    r_ = 0.25
    def ref_radius(Xt, Xq_, r):
        return [[i for i in range(len(Xt)) if math.sqrt(float(np.sum((np.asarray(Xq_[q], float) - Xt[i]) ** 2))) <= r] for q in range(len(Xq_))]
    rn_ = ref_radius(Xn, Xnq, r_)
    rc = RadiusNeighborsClassifier(radius=r_).fit(Xn, yn)
    pr_ref = np.array([[np.sum(yn[idx] == c) / len(idx) for c in range(3)] for idx in rn_])
    print(f"   radius {r_}: neighbourhood sizes {[len(x) for x in rn_]}")
    report("RadiusNeighborsClassifier predict_proba = class counts within the radius / count (all queries have neighbours)", allclose(rc.predict_proba(Xnq), pr_ref) and np.array_equal(rc.predict(Xnq), np.argmax(pr_ref, 1)))
    Xfar = np.array([[5.0, 5.0]])
    report("RadiusNeighborsClassifier(outlier_label=None) with an empty neighbourhood raises ValueError (documented)", expect_raises(lambda: rc.predict(Xfar)))
    mode_y = int(np.argmax(np.bincount(yn)))
    rcm = RadiusNeighborsClassifier(radius=r_, outlier_label="most_frequent").fit(Xn, yn)
    report(f"RadiusNeighborsClassifier(outlier_label='most_frequent') predicts the most frequent training label ({mode_y}) for an outlier, proba one-hot", rcm.predict(Xfar)[0] == mode_y and allclose(rcm.predict_proba(Xfar)[0], np.eye(3)[mode_y]))
    rc2 = RadiusNeighborsClassifier(radius=r_, outlier_label=2).fit(Xn, yn)
    report("RadiusNeighborsClassifier(outlier_label=2) predicts 2 for an outlier with proba one-hot on class 2, inliers unchanged", rc2.predict(Xfar)[0] == 2 and allclose(rc2.predict_proba(Xfar)[0], [0, 0, 1]) and allclose(rc2.predict_proba(Xnq), pr_ref))
    rc99 = RadiusNeighborsClassifier(radius=r_, outlier_label=99).fit(Xn, yn)
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always"); p99 = rc99.predict_proba(Xfar); y99 = rc99.predict(Xfar)
    report("RadiusNeighborsClassifier(outlier_label=99 not in classes) -> predict 99, all class probabilities 0 and a warning (documented)", y99[0] == 99 and allclose(p99[0], [0, 0, 0]) and len(wl) >= 1)
    rr = RadiusNeighborsRegressor(radius=r_).fit(Xn, yreg)
    report("RadiusNeighborsRegressor predict = mean of targets within the radius", allclose(rr.predict(Xnq), [np.mean(yreg[idx]) for idx in rn_], 1e-12, 1e-12))
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always"); prr = rr.predict(np.vstack([Xnq[:1], Xfar]))
    report("RadiusNeighborsRegressor empty neighbourhood -> NaN prediction with a UserWarning, other rows unaffected", np.isnan(prr[1]) and close(prr[0], np.mean(yreg[rn_[0]])) and any(issubclass(w.category, UserWarning) for w in wl))
    rrd = RadiusNeighborsRegressor(radius=r_, weights="distance").fit(Xn, yreg)
    ref_rw = [np.sum(yreg[idx] / Dq[q, idx]) / np.sum(1 / Dq[q, idx]) for q, idx in enumerate(rn_)]
    report("RadiusNeighborsRegressor(weights='distance') = inverse-distance weighted mean within the radius", allclose(rrd.predict(Xnq), ref_rw, 1e-10, 1e-12))
section('neighbors: plain-Python brute-force reference', _s09)

def _s10():
    global G, Gd, Gf, Gt, Rg, Xgrid, Xq3, d, i, j, kd3, ki3, level_sets, nn, orders_same, qg, rd4, rdist, ref_conn, ref_dist, ref_rg, ref_self, res, rest, ri4, rind, rn_self, tie_dist_ok, tie_sets_ok
    reseed(10)
    nn = NearestNeighbors(n_neighbors=3).fit(Xn)
    kd3, ki3 = ref_knn(Xn, Xn, 4)  # self first (distance 0), then 3 others
    G = nn.kneighbors_graph(mode="connectivity").toarray(); Gd = nn.kneighbors_graph(mode="distance").toarray()
    ref_conn = np.zeros((25, 25)); ref_dist = np.zeros((25, 25))
    for i in range(25):
        for d, j in zip(kd3[i][1:], ki3[i][1:]): ref_conn[i, j] = 1; ref_dist[i, j] = d
    report("NearestNeighbors.kneighbors_graph(mode='connectivity') = 0/1 rows of the 3 nearest others (self excluded), 'distance' holds the distances", np.array_equal(G, ref_conn) and allclose(Gd, ref_dist, 1e-12, 1e-12))
    Gf = kneighbors_graph(Xn, 3, mode="connectivity", include_self=False).toarray(); Gt = kneighbors_graph(Xn, 3, mode="connectivity", include_self=True).toarray()
    ref_self = np.zeros((25, 25))
    for i in range(25):
        for j in ki3[i][:3]: ref_self[i, j] = 1
    report("kneighbors_graph(include_self=False) excludes the point itself; include_self=True marks the point as its own first neighbour (documented)", np.array_equal(Gf, ref_conn) and np.array_equal(Gt, ref_self) and np.all(np.diag(Gt) == 1))
    report("kneighbors_graph(include_self='auto'): True for connectivity, False for distance (documented)", np.array_equal(kneighbors_graph(Xn, 3, mode="connectivity", include_self="auto").toarray(), Gt) and allclose(kneighbors_graph(Xn, 3, mode="distance", include_self="auto").toarray(), ref_dist, 1e-12, 1e-12))
    Rg = nn.radius_neighbors_graph(radius=r_, mode="distance").toarray(); rn_self = ref_radius(Xn, Xn, r_)
    ref_rg = np.zeros((25, 25))
    for i in range(25):
        for j in rn_self[i]:
            if j != i: ref_rg[i, j] = Dtr[i, j]
    report("NearestNeighbors.radius_neighbors_graph(mode='distance') = distances to the points within the radius, self excluded", allclose(Rg, ref_rg, 1e-12, 1e-12))
    report("radius_neighbors_graph(include_self=True) adds the zero-distance self entry only in connectivity mode (distance 0 is not stored as an explicit nonzero)",
           np.array_equal(radius_neighbors_graph(Xn, r_, mode="connectivity", include_self=True).toarray(), (ref_rg > 0) + np.eye(25)))
    Xq3 = rs.rand(10, 2)
    res = {alg: NearestNeighbors(n_neighbors=4, algorithm=alg).fit(Xn).kneighbors(Xq3) for alg in ("brute", "kd_tree", "ball_tree", "auto")}
    rd4, ri4 = ref_knn(Xn, Xq3, 4)
    report("NearestNeighbors brute / kd_tree / ball_tree / auto give identical kneighbors on float data (all equal to the reference)", all(allclose(res[a][0], rd4, 1e-12, 1e-12) and np.array_equal(res[a][1], ri4) for a in res))
    Xgrid = np.array([[i, j] for i in range(5) for j in range(5)], float); qg = np.array([[2.0, 2.0], [0.0, 0.0], [2.5, 2.5]])
    rest = {alg: NearestNeighbors(n_neighbors=6, algorithm=alg).fit(Xgrid).kneighbors(qg) for alg in ("brute", "kd_tree", "ball_tree")}
    tie_dist_ok = all(allclose(rest[a][0], rest["brute"][0], 1e-12, 1e-12) for a in rest)
    def level_sets(d, i):
        return [frozenset(i[r][np.isclose(d[r], v)]) for r in range(len(d)) for v in np.unique(d[r])]
    tie_sets_ok = all(level_sets(*rest[a]) == level_sets(*rest["brute"]) for a in rest)
    orders_same = all(np.array_equal(rest[a][1], rest["brute"][1]) for a in rest)
    print(f"   integer grid with many ties: neighbour index orders identical across algorithms: {orders_same}; brute indices {rest['brute'][1].tolist()}")
    report("NearestNeighbors on a grid with many tied distances: the sorted distances are identical across brute/kd_tree/ball_tree and the neighbour sets per distance level agree (documented: order within ties may depend on the data ordering)", tie_dist_ok and tie_sets_ok)
    rdist, rind = nn.radius_neighbors(Xnq, radius=r_, sort_results=True)
    report("radius_neighbors(sort_results=True) returns each row sorted by distance, sets equal to the reference", all(np.all(np.diff(d) >= 0) for d in rdist) and all(set(i.tolist()) == set(rn_[q]) for q, i in enumerate(rind)))
    report("radius_neighbors(return_distance=False, sort_results=True) raises ValueError (documented)", expect_raises(lambda: nn.radius_neighbors(Xnq, radius=r_, return_distance=False, sort_results=True)))
    report("radius_neighbors_graph(sort_results=True) rows in CSR order have non-decreasing distances", (lambda g: all(np.all(np.diff(g.data[g.indptr[i]:g.indptr[i + 1]]) >= 0) for i in range(g.shape[0])))(nn.radius_neighbors_graph(Xnq, radius=r_, mode="distance", sort_results=True)))
    # boundary: on the integer grid the 4 axis neighbours of (2,2) are at distance exactly 1.0, the diagonal ones at sqrt(2)
    for alg in ("brute", "kd_tree", "ball_tree"):
        got_b = NearestNeighbors(algorithm=alg).fit(Xgrid).radius_neighbors([[2.0, 2.0]], radius=1.0)[1][0]
        report(f"NearestNeighbors({alg}).radius_neighbors at radius exactly 1.0 on the integer grid returns (2,2) and its 4 axis neighbours (documented 'Points lying on the boundary are included')",
               set(got_b.tolist()) == {7, 11, 12, 13, 17}, f"(got {sorted(got_b.tolist())})")
    # the other minkowski metrics: algorithms agree with the plain-Python reference
    for p_ in (1.0, np.inf):
        rdp, rip = ref_knn(Xn, Xq3, 4, p=p_)
        report(f"NearestNeighbors(p={p_}) brute / kd_tree / ball_tree kneighbors = reference", all((lambda o: allclose(o[0], rdp, 1e-12, 1e-12) and np.array_equal(o[1], rip))(NearestNeighbors(n_neighbors=4, p=p_, algorithm=alg).fit(Xn).kneighbors(Xq3)) for alg in ("brute", "kd_tree", "ball_tree")))
    # translation invariance of the Euclidean distance: a large common offset must not change neighbours or distances
    for off in (1e4, 1e6):
        ok_off = True; worst = 0.0
        for alg in ("brute", "kd_tree", "ball_tree"):
            do_, io_ = NearestNeighbors(n_neighbors=4, algorithm=alg).fit(Xn + off).kneighbors(Xq3 + off)
            worst = max(worst, maxdiff(do_, rd4)); ok_off &= np.array_equal(io_, ri4) and allclose(do_, rd4, 1e-6, 1e-6)
            print(f"   offset {off:g}, {alg}: max |distance - exact| {maxdiff(do_, rd4):.2e}; index rows differing {int(np.sum(np.any(io_ != ri4, axis=1)))}/10")
        report(f"NearestNeighbors kneighbors on X + {off:g} (all three algorithms) = exact neighbours of X, distances within 1e-6 (Euclidean distance is translation invariant; exact values from differences computed on the offset data would err by ~ {off:g} * 1e-16)", ok_off, f"(max distance error {worst:.2e})")
section('neighbors.NearestNeighbors: graphs, include_self, algorithms, ties, sort_results', _s10)

def _s11():
    global Kp, Tree, X1, X2, X4, Xq_, Xt, cnt, dd, dim, dist_s, ex, got, got_, gotb, h, hi_, ind_r, ind_s, kd4, kernel_norm_exact, kernel_profile, kind, kind_, ok_, q1, q2, q4, ref, ref_2pt, ref_kde, rr_, surf, td, ti, tr, trg
    reseed(11)
    for Tree in (KDTree, BallTree):
        tr = Tree(Xn, leaf_size=3); td, ti = tr.query(Xnq, k=5)
        report(f"{Tree.__name__}.query(k=5) = reference", allclose(td, kd, 1e-12, 1e-12) and np.array_equal(ti, ki))
        ind_r = tr.query_radius(Xnq, r=r_); cnt = tr.query_radius(Xnq, r=r_, count_only=True)
        report(f"{Tree.__name__}.query_radius sets = reference (d <= r), count_only = sizes", all(set(a.tolist()) == set(b) for a, b in zip(ind_r, rn_)) and np.array_equal(cnt, [len(b) for b in rn_]))
        ind_s, dist_s = tr.query_radius(Xnq, r=r_, return_distance=True, sort_results=True)
        report(f"{Tree.__name__}.query_radius(sort_results=True) rows sorted ascending", all(np.all(np.diff(d) >= 0) for d in dist_s))
        trg = Tree(Xgrid); rr_ = np.array([0.5, 1.0, 1.5, 2.0])
        ref_2pt = [sum(1 for q in qg for x in Xgrid if math.sqrt(float(np.sum((q - x) ** 2))) <= r) for r in rr_]
        report(f"{Tree.__name__}.two_point_correlation = number of (query, data) pairs with distance <= r (r exactly on grid distances 1.0, 2.0)", np.array_equal(trg.two_point_correlation(qg, rr_), ref_2pt) and np.array_equal(trg.two_point_correlation(qg, rr_, dualtree=True), ref_2pt))
        report(f"{Tree.__name__}.query_radius at r exactly equal to a distance includes that point (<=)", set(trg.query_radius([[2.0, 2.0]], r=1.0)[0].tolist()) == {7, 11, 12, 13, 17})
    def kernel_profile(kind, h):
        if kind == "gaussian": return lambda r: mpmath.exp(-r ** 2 / (2 * h ** 2))
        if kind == "tophat": return lambda r: mpf(1) if r < h else mpf(0)
        if kind == "epanechnikov": return lambda r: 1 - r ** 2 / h ** 2 if r < h else mpf(0)
        if kind == "exponential": return lambda r: mpmath.exp(-r / h)
        if kind == "linear": return lambda r: 1 - r / h if r < h else mpf(0)
        if kind == "cosine": return lambda r: mpmath.cos(mpmath.pi * r / (2 * h)) if r < h else mpf(0)
    def kernel_norm_exact(kind, h, d):
        # surface of the unit sphere in R^d: 2 pi^(d/2) / Gamma(d/2) (= 2 for d = 1, 2 pi for d = 2)
        K = kernel_profile(kind, mpf(h)); Sd = 2 * mpmath.pi ** (mpf(d) / 2) / mpmath.gamma(mpf(d) / 2); surf = lambda r: Sd * r ** (d - 1)
        hi = mpmath.inf if kind in ("gaussian", "exponential") else mpf(h)
        return 1 / mpmath.quad(lambda r: K(r) * surf(r), [0, hi])
    def ref_kde(kind, h, Xt, Xq_):
        K = kernel_profile(kind, mpf(h)); d = Xt.shape[1]; c = kernel_norm_exact(kind, h, d); out = []
        for q in Xq_:
            out.append(float(c * sum(K(mpf(math.sqrt(float(np.sum((q - x) ** 2))))) for x in Xt)))
        return np.array(out)
    X1 = np.sort(rs.rand(12))[:, None] * 3; q1 = np.array([[0.3], [1.1], [2.9], [4.2]])
    X2 = rs.rand(12, 2) * 2; q2 = rs.rand(4, 2) * 2
    for kind in ("gaussian", "tophat", "epanechnikov", "exponential", "linear", "cosine"):
        for Xt, Xq_, h, dim in ((X1, q1, 0.7, 1), (X2, q2, 0.9, 2)):
            ref = ref_kde(kind, h, Xt, Xq_); got = KDTree(Xt).kernel_density(Xq_, h=h, kernel=kind, rtol=1e-13, atol=0); gotb = BallTree(Xt).kernel_density(Xq_, h=h, kernel=kind, rtol=1e-13, atol=0)
            print(f"   {kind} {dim}-D h={h}: KDTree {np.round(got, 8).tolist()} exact {np.round(ref, 8).tolist()} (norm {float(kernel_norm_exact(kind, h, dim)):.8f})")
            report(f"KDTree/BallTree.kernel_density({kind}, {dim}-D) = sum_i K(||x - x_i||) with K normalised to integrate to 1 over R^{dim} (mpmath quad of the documented profile)", allclose(got, ref, 1e-8, 1e-12) and allclose(gotb, ref, 1e-8, 1e-12))
    try:
        from sklearn.neighbors._kd_tree import kernel_norm as _kn
        for dd in (1, 2, 3, 4, 5):
            ex = float(kernel_norm_exact("cosine", 1.0, dd)) if dd <= 2 else float(1 / (mpmath.quad(lambda u: u ** (dd - 1) * mpmath.cos(u), [0, mpmath.pi / 2]) * (2 * mpmath.pi ** (mpf(dd) / 2) / mpmath.gamma(mpf(dd) / 2)) * (2 / mpmath.pi) ** dd))
            got_ = _kn(1.0, dd, "cosine")
            print(f"   cosine kernel normalisation constant, h=1, d={dd}: library {got_!r} exact {ex:.12f}")
            report(f"cosine kernel normalisation in d={dd} = 1 / (S_(d-1) (2h/pi)^d int_0^(pi/2) u^(d-1) cos u du) (mpmath)", close(got_, ex, 1e-10))
        for kind_ in ("gaussian", "tophat", "epanechnikov", "exponential", "linear"):
            ok_ = True
            for dd in (1, 2, 3, 4, 5):
                Kp = kernel_profile(kind_, mpf(1)); surf = 2 * mpmath.pi ** (mpf(dd) / 2) / mpmath.gamma(mpf(dd) / 2)
                hi_ = mpmath.inf if kind_ in ("gaussian", "exponential") else mpf(1)
                ok_ &= close(_kn(1.0, dd, kind_), float(1 / mpmath.quad(lambda r: Kp(r) * surf * r ** (dd - 1), [0, hi_])), 1e-10)
            report(f"{kind_} kernel normalisation constants for d = 1..5 = 1/int_R^d K (mpmath, surface area 2 pi^(d/2)/Gamma(d/2))", ok_)
    except ImportError as e:
        print(f"   kernel_norm not importable: {e}")
    X4 = rs.rand(10, 4); q4 = rs.rand(3, 4)
    for dd in (3, 4):
        kdd_ = KDTree(X4[:, :dd]).kernel_density(q4[:, :dd], h=0.9, kernel="cosine", rtol=1e-13); refd = ref_kde("cosine", 0.9, X4[:, :dd], q4[:, :dd])
        print(f"   cosine kernel_density in {dd}-D: KDTree {kdd_.tolist()} exact {refd.tolist()}")
        report(f"KDTree.kernel_density(cosine, {dd}-D) = exact normalised cosine KDE (mpmath radial integral)", allclose(kdd_, refd, 1e-8, 1e-12))
    report("KDTree.kernel_density(return_log=True) = log of the density", allclose(KDTree(X2).kernel_density(q2, h=0.9, kernel="gaussian", return_log=True, rtol=1e-13), np.log(ref_kde("gaussian", 0.9, X2, q2)), 1e-8, 1e-12))
    report("KDTree.kernel_density(breadth_first=False, depth-first) same result", allclose(KDTree(X2).kernel_density(q2, h=0.9, kernel="epanechnikov", breadth_first=False, rtol=1e-13), ref_kde("epanechnikov", 0.9, X2, q2), 1e-8, 1e-12))
section('neighbors.KDTree / BallTree: query, query_radius, two_point_correlation, kernel_density normalisation (mpmath integrals)', _s11)

def _s12():
    global Xdupes, Xl_, Xnew, _, kdist_ref, lof, lof29, lof_ref, lofbig, lofc, lofd, lofn, lofp, lrd_ref, percentile_linear, ref_lof, sc_ref, wl
    reseed(12)
    Xl_ = rs.randn(30, 2); Xl_[0] = [6.0, 6.0]; Xl_[1] = [-4.0, 5.0]
    def ref_lof(X, k, Xnew=None):
        n = len(X); D = np.sqrt(((X[:, None] - X[None]) ** 2).sum(-1))
        nb = []
        for i in range(n):
            ds = sorted((D[i, j], j) for j in range(n) if j != i); nb.append([j for _, j in ds[:k]])
        kdist = np.array([D[i, nb[i][-1]] for i in range(n)])
        lrd = np.array([1.0 / np.mean([max(D[i, o], kdist[o]) for o in nb[i]]) for i in range(n)])
        lof = np.array([np.mean([lrd[o] for o in nb[i]]) / lrd[i] for i in range(n)])
        if Xnew is None: return lof, lrd, kdist
        out = []
        for q in Xnew:
            dq = np.sqrt(((X - q) ** 2).sum(1)); ds = sorted((dq[j], j) for j in range(n)); nq = [j for _, j in ds[:k]]
            lrd_q = 1.0 / np.mean([max(dq[o], kdist[o]) for o in nq]); out.append(np.mean([lrd[o] for o in nq]) / lrd_q)
        return np.array(out)
    lof_ref, lrd_ref, kdist_ref = ref_lof(Xl_, 5)
    lof = LocalOutlierFactor(n_neighbors=5).fit(Xl_)
    print(f"   LOF of the two planted outliers {(-lof.negative_outlier_factor_[:2]).tolist()} (ref {lof_ref[:2].tolist()}); offset_ {lof.offset_}; max rel diff {np.max(np.abs(-lof.negative_outlier_factor_ - lof_ref) / lof_ref):.2e}")
    report("LocalOutlierFactor negative_outlier_factor_ = -LOF with LOF_k(p) = mean_o lrd(o) / lrd(p), lrd(p) = 1/mean_o reach_dist_k(p, o), reach_dist = max(d(p,o), k-distance(o)) (rel 1e-8; library adds 1e-10 to the mean reach distance)", allclose(-lof.negative_outlier_factor_, lof_ref, 1e-8, 1e-12))
    report("LocalOutlierFactor(contamination='auto') offset_ = -1.5 (documented 'as in the original paper'), predict on training data = 1 if nof >= offset_ else -1", lof.offset_ == -1.5 and np.array_equal(lof.fit_predict(Xl_), np.where(lof.negative_outlier_factor_ < -1.5, -1, 1)))
    report("LocalOutlierFactor: the planted outliers have the two largest LOF values, > 1.5", np.all(np.argsort(lof.negative_outlier_factor_)[:2] < 2) and np.all(-lof.negative_outlier_factor_[:2] > 1.5))
    def percentile_linear(v, q):
        s = sorted(v); pos = (len(s) - 1) * q / 100.0; lo = int(math.floor(pos)); hi = min(lo + 1, len(s) - 1)
        return s[lo] + (pos - lo) * (s[hi] - s[lo])
    lofc = LocalOutlierFactor(n_neighbors=5, contamination=0.2).fit(Xl_)
    report("LocalOutlierFactor(contamination=0.2) offset_ = 20th percentile (linear interpolation) of negative_outlier_factor_, so ~20% of the training points are flagged", close(lofc.offset_, percentile_linear(lofc.negative_outlier_factor_, 20), 1e-12) and int((lofc.fit_predict(Xl_) == -1).sum()) == 6)
    lofn = LocalOutlierFactor(n_neighbors=5, novelty=True).fit(Xl_)
    Xnew = np.array([[0.2, -0.1], [5.0, -5.0], [1.0, 1.5]]); sc_ref = -ref_lof(Xl_, 5, Xnew)
    print(f"   novelty score_samples {lofn.score_samples(Xnew).tolist()} ref {sc_ref.tolist()}")
    report("LocalOutlierFactor(novelty=True).score_samples(X_new) = -LOF of the new points w.r.t. the training neighbours (lrd of training points reused)", allclose(lofn.score_samples(Xnew), sc_ref, 1e-8, 1e-12))
    report("LocalOutlierFactor(novelty=True) decision_function = score_samples - offset_, predict = sign", allclose(lofn.decision_function(Xnew), lofn.score_samples(Xnew) - lofn.offset_, 1e-12, 1e-12) and np.array_equal(lofn.predict(Xnew), np.where(lofn.decision_function(Xnew) < 0, -1, 1)))
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always"); lofbig = LocalOutlierFactor(n_neighbors=50).fit(Xl_)
    lof29, _, _ = ref_lof(Xl_, 29)
    report("LocalOutlierFactor(n_neighbors=50 > 30 samples): n_neighbors_ = n_samples - 1 with a warning, LOF computed with 29 neighbours", lofbig.n_neighbors_ == 29 and len(wl) >= 1 and allclose(-lofbig.negative_outlier_factor_, lof29, 1e-8, 1e-12))
    Xdupes = np.vstack([np.zeros((7, 2)), rs.randn(10, 2) + 3])
    lofd = LocalOutlierFactor(n_neighbors=5).fit(Xdupes)
    print(f"   7 duplicates with k=5: nof of the duplicates {lofd.negative_outlier_factor_[:2].tolist()} (finite thanks to the 1e-10 guard)")
    report("LocalOutlierFactor with more duplicates than n_neighbors: negative_outlier_factor_ finite and = -1 for the duplicates (all lrd equal, 1/(0 + 1e-10))", np.all(np.isfinite(lofd.negative_outlier_factor_)) and allclose(lofd.negative_outlier_factor_[:7], -np.ones(7), 1e-9, 1e-9))
    lofp = LocalOutlierFactor(n_neighbors=5, metric="precomputed").fit(np.sqrt(((Xl_[:, None] - Xl_[None]) ** 2).sum(-1)))
    report("LocalOutlierFactor(metric='precomputed') same LOF", allclose(lofp.negative_outlier_factor_, lof.negative_outlier_factor_, 1e-10, 1e-12))
    report("LocalOutlierFactor(novelty=True) has no fit_predict (documented: 'fit_predict ... not available when novelty=True')", not hasattr(lofn, "fit_predict") or expect_raises(lambda: lofn.fit_predict(Xl_), AttributeError))
    report("LocalOutlierFactor(novelty=False) has no predict / decision_function / score_samples on new data (documented 'only available for novelty detection')",
           all((not hasattr(lof, a)) or expect_raises(lambda a=a: getattr(lof, a)(Xnew), AttributeError) for a in ("predict", "decision_function", "score_samples")))
section('neighbors.LocalOutlierFactor: lrd / LOF recomputed from the k-distance definitions', _s12)

def _s13():
    global Xnc, Xt_, c_ref, cent_ref, delta, dev_raw, dev_ref, ds_ref, med_ref, nce, ncl, ncm, ncp, ncs, s_ref, shrink_ref, ync
    reseed(13)
    Xnc = rs.randint(0, 10, (15, 3)).astype(float); ync = np.array([0] * 4 + [1] * 5 + [2] * 6)
    ncl = NearestCentroid().fit(Xnc, ync)
    cent_ref = np.array([[float(sum(F(v) for v in Xnc[ync == k, j]) / int((ync == k).sum())) for j in range(3)] for k in range(3)])
    report("NearestCentroid centroids_ = per-class means (exact Fraction)", allclose(ncl.centroids_, cent_ref, 1e-15, 0))
    report("NearestCentroid predict = class of the nearest (Euclidean) centroid", np.array_equal(ncl.predict(Xnc), np.argmin(((Xnc[:, None] - cent_ref[None]) ** 2).sum(-1), 1)))
    def shrink_ref(X, y, delta):
        n, p = X.shape; K = 3; nk = np.array([(y == k).sum() for k in range(K)]); cent = np.array([X[y == k].mean(0) for k in range(K)])
        s = np.sqrt(np.sum((X - cent[y]) ** 2, axis=0) / (n - K)); s0 = np.median(s); m = np.sqrt(1.0 / nk - 1.0 / n); xbar = X.mean(0)
        dev = (cent - xbar) / (m[:, None] * (s + s0)); dev_s = np.sign(dev) * np.maximum(np.abs(dev) - delta, 0)
        return xbar + m[:, None] * (s + s0) * dev_s, dev_s, s, dev
    delta = 0.5
    ncs = NearestCentroid(shrink_threshold=delta).fit(Xnc, ync)
    c_ref, dev_ref, s_ref, dev_raw = shrink_ref(Xnc, ync, delta)
    print(f"   shrunken centroids {np.round(ncs.centroids_, 6).tolist()}\n   reference          {np.round(c_ref, 6).tolist()}\n   raw deviations {np.round(dev_raw, 4).tolist()}")
    report("NearestCentroid(shrink_threshold=0.5) centroids_ = xbar_j + m_k (s_j + s0) d'_kj with d'_kj = sign(d)(|d| - delta)_+, d_kj = (xbar_kj - xbar_j)/(m_k (s_j + s0)), m_k = sqrt(1/n_k - 1/n), s_j pooled within-class sd (n-K), s0 = median(s) (ESL eq. 18.4-18.5 as documented)", allclose(ncs.centroids_, c_ref, 1e-12, 1e-12))
    report("NearestCentroid shrinkage: some deviations shrunk to exactly 0 (soft thresholding removes features)", np.any(dev_ref == 0) and np.any(dev_ref != 0))
    if V >= (1, 6):
        report("NearestCentroid deviations_ (1.6+) = the shrunken standardised deviations d'_kj; within_class_std_dev_ = pooled sd", allclose(ncs.deviations_, dev_ref, 1e-12, 1e-12) and allclose(ncs.within_class_std_dev_, s_ref, 1e-12, 1e-12))
        print(f"   default priors='uniform': class_prior_ {ncl.class_prior_.tolist()} (docstring also says 'By default, the class proportions are inferred from the training data')")
        report("NearestCentroid default priors='uniform' (signature 'default=\"uniform\"') -> class_prior_ = 1/n_classes", allclose(ncl.class_prior_, [1 / 3] * 3))
        report("NearestCentroid default class_prior_ = class proportions of the training data (docstring of `priors`: 'By default, the class proportions are inferred from the training data')", allclose(ncl.class_prior_, [4 / 15, 5 / 15, 6 / 15]),
               f"(got {np.round(ncl.class_prior_, 4).tolist()}, proportions {[round(4 / 15, 4), round(5 / 15, 4), round(6 / 15, 4)]})")
        _, dev0, _, dev_raw0 = shrink_ref(Xnc, ync, 0.0)
        report("NearestCentroid(shrink_threshold=None) deviations_ = eq. (18.4) d_kj = (xbar_kj - xbar_j)/(m_k (s_j + s0)) unshrunk (documented 'Equal to eq. (18.4) if shrink_threshold=None')", allclose(ncl.deviations_, dev_raw0, 1e-12, 1e-12))
        nce = NearestCentroid(priors="empirical").fit(Xnc, ync)
        report("NearestCentroid(priors='empirical') class_prior_ = class counts / n", allclose(nce.class_prior_, [4 / 15, 5 / 15, 6 / 15]))
        Xt_ = rs.rand(8, 3) * 10
        ds_ref = np.array([[-np.sum(((x - cent_ref[k]) / s_ref) ** 2) + 2 * math.log([4 / 15, 5 / 15, 6 / 15][k]) for k in range(3)] for x in Xt_])
        report("NearestCentroid(priors='empirical') decision_function = -sum_j ((x_j - xbar_kj)/s_j)^2 + 2 log pi_k (ESL eq. 18.2), predict = argmax", allclose(nce.decision_function(Xt_), ds_ref, 1e-10, 1e-12) and np.array_equal(nce.predict(Xt_), np.argmax(ds_ref, 1)))
        ncp = NearestCentroid(priors=[0.6, 0.3, 0.1]).fit(Xnc, ync)
        report("NearestCentroid(priors=[.6,.3,.1]) uses the given priors in the discriminant", allclose(ncp.class_prior_, [0.6, 0.3, 0.1]) and allclose(ncp.decision_function(Xt_), ds_ref - 2 * np.log([4 / 15, 5 / 15, 6 / 15]) + 2 * np.log([0.6, 0.3, 0.1]), 1e-10, 1e-12))
        report("NearestCentroid(priors=[.7,.7,.1]) not summing to 1 -> normalised with a warning", allclose(NearestCentroid(priors=[0.7, 0.7, 0.1]).fit(Xnc, ync).class_prior_, [0.7 / 1.5, 0.7 / 1.5, 0.1 / 1.5]))
    ncm = NearestCentroid(metric="manhattan").fit(Xnc, ync)
    med_ref = np.array([[float((lambda s: (s[len(s) // 2] if len(s) % 2 else (s[len(s) // 2 - 1] + s[len(s) // 2]) / 2))(sorted(F(v) for v in Xnc[ync == k, j]))) for j in range(3)] for k in range(3)])
    report("NearestCentroid(metric='manhattan') centroids_ = feature-wise medians (documented; even counts -> midpoint)", allclose(ncm.centroids_, med_ref, 1e-15, 0))
    report("NearestCentroid(metric='manhattan') predict = argmin of the L1 distance to the medians", np.array_equal(ncm.predict(Xnc), np.argmin(np.abs(Xnc[:, None] - med_ref[None]).sum(-1), 1)))
    report("NearestCentroid(shrink_threshold) with a single-sample class: m_k = sqrt(1/1 - 1/n) finite, fits", not expect_raises(lambda: NearestCentroid(shrink_threshold=0.1).fit(np.vstack([Xnc, [[1, 2, 3]]]), np.append(ync, 3)), Exception))
section('neighbors.NearestCentroid: centroids, Tibshirani/ESL shrinkage recomputed, manhattan medians, priors', _s13)

def _s14():
    global A0, J0, J1, Xa, fd_grad, g_fd, g_fd0, grad_lib, loss_lib, mask, nca, ncaI, nca_obj, traj, ya
    reseed(14)
    Xa = rs.randn(20, 3); ya = np.array([0, 1, 2, 0, 1] * 4); A0 = rs.randn(2, 3)
    def nca_obj(Aflat, X, y):
        A = np.asarray(Aflat, float).reshape(-1, X.shape[1]); Z = X @ A.T; tot = 0.0
        for i in range(len(X)):
            d = ((Z - Z[i]) ** 2).sum(1); d[i] = np.inf; e = np.exp(-(d - d.min())); p = e / e.sum()
            tot += float(np.sum(p[y == y[i]]))
        return tot
    def fd_grad(fun, x, h=1e-6):
        g = np.zeros_like(x)
        for i in range(len(x)):
            e = np.zeros_like(x); e[i] = h; g[i] = (fun(x + e) - fun(x - e)) / (2 * h)
        return g
    nca = NeighborhoodComponentsAnalysis(n_components=2, init=A0, tol=1e-12, max_iter=300, random_state=0)
    traj = []
    its = []
    nca.set_params(callback=lambda T, it: (traj.append(T.copy()), its.append(it))); nca.fit(Xa, ya); n_iter_fit = nca.n_iter_
    J0 = nca_obj(A0.ravel(), Xa, ya); J1 = nca_obj(nca.components_.ravel(), Xa, ya)
    g_fd = fd_grad(lambda t: nca_obj(t, Xa, ya), nca.components_.ravel())
    print(f"   objective sum_i p_i at init {J0:.8f} -> at components_ {J1:.8f} (max {len(Xa)}); n_iter_ {n_iter_fit}; ||grad|| at solution (finite differences) {np.linalg.norm(g_fd):.2e}")
    report("NCA maximises sum_i p_i (softmax over squared Euclidean distances in the embedding, same-class mass): objective at components_ > at init and gradient (central finite differences) small at the solution (< 1e-4)", J1 > J0 and np.linalg.norm(g_fd) < 1e-4)
    try:
        mask = ya[:, None] == ya[None, :]
        nca.n_iter_ = 1   # a private call; n_iter_ = 0 would make it print a verbose header (n_iter_ of the fit was saved above)
        loss_lib, grad_lib = nca._loss_grad_lbfgs(A0.ravel(), Xa, mask, sign=1.0)
        g_fd0 = fd_grad(lambda t: nca_obj(t, Xa, ya), A0.ravel())
        print(f"   at init: library objective {loss_lib:.10f} vs recomputed {J0:.10f}; max |grad - finite differences| {maxdiff(grad_lib, g_fd0):.2e}")
        report("NCA internal objective at init = recomputed softmax neighbour loss (1e-9) and its analytic gradient = central finite differences (1e-6)", close(loss_lib, J0, 1e-9) and allclose(grad_lib, g_fd0, 1e-6, 1e-6))
    except Exception as e:
        print(f"   (private _loss_grad_lbfgs unavailable: {type(e).__name__}: {e})")
    # independent count: scipy's own L-BFGS-B on the same objective/gradient calls its callback once per iteration
    nit_scipy = None
    try:
        nca2 = NeighborhoodComponentsAnalysis(n_components=2, init=A0, tol=1e-12, max_iter=300, random_state=0); nca2.n_iter_ = 1
        mask2 = ya[:, None] == ya[None, :]; cnt = []
        r_ = optimize.minimize(lambda t: nca2._loss_grad_lbfgs(t, Xa, mask2, -1.0), A0.ravel(), jac=True, method="L-BFGS-B", tol=1e-12, options=dict(maxiter=300), callback=lambda xk: cnt.append(1))
        nit_scipy = (r_.nit, len(cnt))
    except Exception as e:
        print(f"   (scipy re-run skipped: {type(e).__name__}: {e})")
    print(f"   callback invoked {len(traj)} times with iteration numbers {its[:3]} ... {its[-2:]}; n_iter_ after fit = {n_iter_fit}; scipy L-BFGS-B on the same objective: (nit, callbacks) = {nit_scipy}")
    report("NCA callback is called after every iteration with the current solution; the last one equals components_", len(traj) >= 1 and allclose(traj[-1].reshape(2, 3), nca.components_))
    report("NCA callback receives the iteration numbers 1, 2, ..., N (documented 'taking as arguments the current solution ... and the number of iterations')", its == list(range(1, len(its) + 1)))
    report("NCA n_iter_ 'counts the number of iterations performed by the optimizer' = number of callback invocations (documented 'called after every iteration of the optimizer')", len(traj) == n_iter_fit, f"(callbacks {len(traj)}, n_iter_ {n_iter_fit})")
    report("NCA transform(X) = X @ components_.T", allclose(nca.transform(Xa), Xa @ nca.components_.T, 1e-12, 1e-12))
    report("NCA(init='identity') with n_components=None starts from the identity (components_ shape (n_features, n_features))", NeighborhoodComponentsAnalysis(init="identity", max_iter=1).fit(Xa, ya).components_.shape == (3, 3))
section('neighbors.NeighborhoodComponentsAnalysis: softmax neighbour objective and gradient', _s14)

def _s15():
    global S_, St, Xk, d_, dmin, kde, kind, kk, ks, ksi, kt_, kw2, mu_ref, n_, qk, ref_ls, ref_w, scott, silv, var_ref
    reseed(15)
    Xk = rs.randn(40, 2) * [1.0, 2.0]
    kde = KernelDensity(bandwidth=0.8, kernel="gaussian").fit(Xk); qk = rs.randn(5, 2)
    ref_ls = np.log(ref_kde("gaussian", 0.8, Xk, qk) / 40)
    report("KernelDensity.score_samples = log(mean_i K_norm(x - x_i)) (Gaussian normalised in 2-D), score = sum of log densities", allclose(kde.score_samples(qk), ref_ls, 1e-8, 1e-12) and close(kde.score(qk), np.sum(kde.score_samples(qk)), 1e-12))
    for kind in ("tophat", "epanechnikov", "exponential", "linear", "cosine"):
        kk = KernelDensity(bandwidth=0.8, kernel=kind).fit(Xk)
        report(f"KernelDensity(kernel='{kind}').score_samples = log of the normalised {kind} KDE (exp(score_samples) integrates to 1)", allclose(np.exp(kk.score_samples(qk)), ref_kde(kind, 0.8, Xk, qk) / 40, 1e-8, 1e-300))
    if V >= (1, 2):
        # Scott (1992, eq. 6.42): h_j = sigma_j n^(-1/(d+4)); Silverman (1986, eq. 4.14, normal reference for data scaled
        # to unit variance): h = (4/(d+2))^(1/(d+4)) n^(-1/(d+4)). Both are proportional to the data scale sigma.
        # On data standardised to unit sample standard deviation (ddof=1) in every coordinate they reduce to the factors.
        for d_ in (1, 3):
            Z_ = rs.randn(45, d_); Z_ = (Z_ - Z_.mean(0)) / Z_.std(0, ddof=1); n_ = len(Z_)
            scott = float(mpf(n_) ** (mpf(-1) / (d_ + 4))); silv = float((4 / mpf(d_ + 2)) ** (mpf(1) / (d_ + 4)) * mpf(n_) ** (mpf(-1) / (d_ + 4)))
            ks = KernelDensity(bandwidth="scott").fit(Z_); ksi = KernelDensity(bandwidth="silverman").fit(Z_)
            print(f"   d={d_}, n={n_}, unit-variance data: bandwidth_ scott {ks.bandwidth_!r} (n^(-1/(d+4)) = {scott!r}); silverman {ksi.bandwidth_!r} ((4/(d+2))^(1/(d+4)) n^(-1/(d+4)) = {silv!r})")
            report(f"KernelDensity(bandwidth='scott'), d={d_}, unit-variance data: bandwidth_ = n^(-1/(d+4)) (Scott's rule, 1e-14)", close(ks.bandwidth_, scott, 1e-14))
            report(f"KernelDensity(bandwidth='silverman'), d={d_}, unit-variance data: bandwidth_ = (4/(d+2))^(1/(d+4)) n^(-1/(d+4)) (Silverman's normal-reference rule, 1e-14)", close(ksi.bandwidth_, silv, 1e-14))
            ks10 = KernelDensity(bandwidth="scott").fit(10 * Z_); ksi10 = KernelDensity(bandwidth="silverman").fit(10 * Z_)
            print(f"      data x 10: scott {ks10.bandwidth_!r}, silverman {ksi10.bandwidth_!r} (the rules give 10x: {10 * scott!r}, {10 * silv!r})")
            report(f"KernelDensity(bandwidth='scott'/'silverman'), d={d_}: data multiplied by 10 -> bandwidth_ multiplied by 10 (both rules are proportional to the data standard deviation; user guide 'Scott's and Silverman's estimation methods')",
                   close(ks10.bandwidth_, 10 * ks.bandwidth_, 1e-12) and close(ksi10.bandwidth_, 10 * ksi.bandwidth_, 1e-12))
        ks = KernelDensity(bandwidth="scott").fit(Xk); hs = float(mpf(40) ** (mpf(-1) / 6))
        report("KernelDensity(bandwidth='scott') score_samples uses bandwidth_ (2-D Gaussian KDE recomputed with h = bandwidth_)", close(ks.bandwidth_, hs, 1e-14) and allclose(ks.score_samples(qk), np.log(ref_kde("gaussian", hs, Xk, qk) / 40), 1e-8, 1e-12))
    S_ = kde.sample(20000, random_state=1)
    mu_ref = Xk.mean(0); var_ref = Xk.var(0) + 0.8 ** 2
    print(f"   gaussian sample(20000): mean {S_.mean(0).tolist()} (data mean {mu_ref.tolist()}); var {S_.var(0).tolist()} (var(data) + h^2 = {var_ref.tolist()})")
    report("KernelDensity(gaussian).sample: mean within 4 sigma of the data mean and variance within 4% of var(data) + h^2 (mixture of N(x_i, h^2))", np.all(np.abs(S_.mean(0) - mu_ref) < 4 * np.sqrt(var_ref / 20000)) and np.all(np.abs(S_.var(0) / var_ref - 1) < 0.04))
    kt_ = KernelDensity(bandwidth=0.5, kernel="tophat").fit(Xk); St = kt_.sample(3000, random_state=2)
    dmin = np.sqrt(((St[:, None] - Xk[None]) ** 2).sum(-1)).min(1)
    report("KernelDensity(tophat).sample: every sample within h of some data point", np.all(dmin <= 0.5 + 1e-12))
    report("KernelDensity(epanechnikov).sample raises NotImplementedError (documented 'only for gaussian and tophat')", expect_raises(lambda: KernelDensity(kernel="epanechnikov").fit(Xk).sample(2), NotImplementedError))
    kw2 = KernelDensity(bandwidth=0.8).fit(Xk, sample_weight=np.r_[np.full(20, 3.0), np.ones(20)])
    ref_w = np.log(np.array([float(kernel_norm_exact("gaussian", 0.8, 2) * sum(wt * mpmath.exp(-mpf(float(np.sum((q - x) ** 2))) / (2 * 0.64)) for wt, x in zip(np.r_[np.full(20, 3.0), np.ones(20)], Xk))) for q in qk]) / 80)
    report("KernelDensity(sample_weight) score_samples = log(sum_i w_i K(x - x_i) / sum w)", allclose(kw2.score_samples(qk), ref_w, 1e-8, 1e-12))
section('neighbors.KernelDensity', _s15)

def _s16():
    global Kapprox, Kfull, Kref, Ksig_psd, Xnew_, Xny, Z, Z5, Zc, Zd, Zp, Zsg, idx, kind, mineig, ny, ny5, nyb, nyc, nyd, nyp, nys, params, ref_fn, wl
    reseed(16)
    Xny = rs.rand(20, 3)
    for kind, params, ref_fn in (("rbf", dict(gamma=0.9), lambda A, B: kern("rbf", A, B, gamma=0.9)),
                                  ("poly", dict(gamma=0.5, coef0=1.0, degree=3), lambda A, B: kern("poly", A, B, 0.5, 1.0, 3)),
                                  ("sigmoid", dict(gamma=0.3, coef0=0.2), lambda A, B: kern("sigmoid", A, B, 0.3, 0.2)),
                                  ("chi2", dict(gamma=0.7), lambda A, B: kern("chi2", A, B, gamma=0.7))):
        ny = Nystroem(kernel=kind, n_components=20, random_state=0, **params).fit(Xny); Z = ny.transform(Xny); Kref = ref_fn(Xny, Xny)
        mineig = float(np.linalg.eigvalsh(Kref).min())
        print(f"   {kind} n_components=n_samples: max |Z Z^T - K| {maxdiff(Z @ Z.T, Kref):.2e} (min eigenvalue of K {mineig:.3e})")
        report(f"Nystroem(kernel='{kind}', n_components=n_samples): transform(X) @ transform(X).T = K exactly (user guide: Z Z^T = K21 K11^-1 K21^T, exact when every sample is in the basis; 1e-6, K coded independently)" + (" [this K is indefinite: no real feature map can reproduce it; the docstring says 'an arbitrary kernel']" if mineig < -1e-10 else ""), allclose(Z @ Z.T, Kref, 1e-6, 1e-6))
        if mineig < -1e-10:
            ev, Qv = np.linalg.eigh(Kref); Kabs = (Qv * np.abs(ev)) @ Qv.T
            print(f"      indefinite K: max |Z Z^T - |K|| (matrix absolute value Q|L|Q^T) {maxdiff(Z @ Z.T, Kabs):.2e}")
            report(f"Nystroem(kernel='{kind}') with an indefinite Gram matrix: Z Z^T = |K| = Q |Lambda| Q^T, i.e. the SVD-based normalization_ silently approximates the PSD kernel |K| (what the implementation computes; not documented)", allclose(Z @ Z.T, Kabs, 1e-6, 1e-6))
        ny5 = Nystroem(kernel=kind, n_components=6, random_state=1, **params).fit(Xny); Z5 = ny5.transform(Xny); idx = ny5.component_indices_
        Kapprox = Kref[:, idx] @ np.linalg.pinv(Kref[np.ix_(idx, idx)]) @ Kref[idx, :]
        report(f"Nystroem(kernel='{kind}', n_components=6): Z Z^T = K[:, m] pinv(K[m, m]) K[m, :] (numpy pinv on the independently computed kernel, 1e-6)", allclose(Z5 @ Z5.T, Kapprox, 1e-6, 1e-6) and np.array_equal(ny5.components_, Xny[idx]))
    Kfull = kern("rbf", Xny, Xny, gamma=0.9)
    nyp = Nystroem(kernel="precomputed", n_components=20, random_state=0).fit(Kfull); Zp = nyp.transform(Kfull)
    report("Nystroem(kernel='precomputed') on the Gram matrix reproduces it: Z Z^T = K", allclose(Zp @ Zp.T, Kfull, 1e-6, 1e-6))
    Xsg = np.random.RandomState(1).randn(6, 10); Ksig_psd = kern("sigmoid", Xsg, Xsg, 0.05, 0.0)
    nys = Nystroem(kernel="sigmoid", gamma=0.05, coef0=0.0, n_components=6, random_state=0).fit(Xsg); Zsg = nys.transform(Xsg)
    print(f"   sigmoid(gamma=0.05, coef0=0) on 6 points in 10-D: min eigenvalue {np.linalg.eigvalsh(Ksig_psd).min():.3e} (positive definite); max |Z Z^T - K| {maxdiff(Zsg @ Zsg.T, Ksig_psd):.2e}")
    report("Nystroem(kernel='sigmoid') on data whose sigmoid Gram matrix is positive definite (min eigenvalue > 1e-3) reproduces K exactly (1e-8)", np.linalg.eigvalsh(Ksig_psd).min() > 1e-3 and allclose(Zsg @ Zsg.T, Ksig_psd, 1e-8, 1e-8))
    nyc = Nystroem(kernel=lambda a, b, scale=1.0: float(np.exp(-scale * np.sum((a - b) ** 2))), kernel_params={"scale": 0.9}, n_components=20, random_state=0).fit(Xny); Zc = nyc.transform(Xny)
    report("Nystroem(kernel=callable, kernel_params) = the rbf result", allclose(Zc @ Zc.T, Kfull, 1e-6, 1e-6))
    nyd = Nystroem(kernel="rbf", n_components=20, random_state=0).fit(Xny); Zd = nyd.transform(Xny)
    report("Nystroem(kernel='rbf', gamma=None) uses the pairwise default gamma = 1/n_features", allclose(Zd @ Zd.T, kern("rbf", Xny, Xny, gamma=1 / 3), 1e-6, 1e-6))
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always"); nyb = Nystroem(kernel="rbf", gamma=0.9, n_components=50, random_state=0).fit(Xny)
    report("Nystroem(n_components=50 > 20 samples): warning and n_components set to n_samples (transform has 20 columns, exact kernel)", len(wl) >= 1 and nyb.transform(Xny).shape[1] == 20 and allclose(nyb.transform(Xny) @ nyb.transform(Xny).T, Kfull, 1e-6, 1e-6))
    Xnew_ = rs.rand(4, 3)
    report("Nystroem transform on new points: Z(new) Z(train)^T = K(new, train) when n_components = n_samples", allclose(nyd.transform(Xnew_) @ Zd.T, kern("rbf", Xnew_, Xny, gamma=1 / 3), 1e-6, 1e-6))
section('kernel_approximation.Nystroem', _s16)

def _s17():
    global Kchi, Kp, Kr, Ksk, L, Xc_, Xp_, Xr_, Xs_, Za, Za15, Za3, Zp_, Zr, Zs, ac, ac3, acc, add_chi2_ref, count_sketch_ref, g_sc, nrep, pcs, rbfs, rsc, seed, sk, steps
    reseed(17)
    Xr_ = rs.rand(5, 3)
    rbfs = RBFSampler(gamma=0.5, n_components=20000, random_state=0).fit(Xr_); Zr = rbfs.transform(Xr_)
    Kr = kern("rbf", Xr_, Xr_, gamma=0.5)
    print(f"   RBFSampler D=20000: max |Z Z^T - exp(-gamma||x-y||^2)| {maxdiff(Zr @ Zr.T, Kr):.4f}; var(random_weights_) {rbfs.random_weights_.var():.5f} (2 gamma = {1.0})")
    report("RBFSampler(D=20000): Z Z^T approximates exp(-gamma ||x-y||^2) within 0.03 (Monte-Carlo error ~ 1/sqrt(D))", allclose(Zr @ Zr.T, Kr, 0, 0.03))
    report("RBFSampler transform = sqrt(2/D) cos(X @ random_weights_ + random_offset_) (Rahimi-Recht random Fourier features)", allclose(Zr, math.sqrt(2.0 / 20000) * np.cos(Xr_ @ rbfs.random_weights_ + rbfs.random_offset_), 1e-12, 1e-12))
    report("RBFSampler random_weights_ ~ N(0, 2 gamma): empirical variance within 3% of 2*gamma; random_offset_ in [0, 2 pi)", abs(rbfs.random_weights_.var() / (2 * 0.5) - 1) < 0.03 and np.all(rbfs.random_offset_ >= 0) and np.all(rbfs.random_offset_ < 2 * np.pi))
    report("RBFSampler(D=20000) for two identical points: Z(x).Z(x) = mean 2cos^2 = 1 + mean cos(2(wx+b)) ~ 1 (within 0.03)", abs((Zr @ Zr.T)[0, 0] - 1) < 0.03)
    if V >= (1, 2):
        try:
            rsc = RBFSampler(gamma="scale", n_components=20000, random_state=0).fit(Xr_); g_sc = 1 / (3 * frac_var_all(Xr_))
            print(f"   RBFSampler(gamma='scale'): 1/(n_features X.var()) = {float(g_sc):.6f}; var(random_weights_)/2 = {rsc.random_weights_.var() / 2:.6f}")
            report("RBFSampler(gamma='scale') (1.2+) uses gamma = 1/(n_features * X.var()): var(random_weights_)/2 within 3%", abs(rsc.random_weights_.var() / 2 / float(g_sc) - 1) < 0.03)
        except Exception as e:
            print(f"   RBFSampler gamma='scale' unsupported: {type(e).__name__}: {e}")
    Xs_ = rs.rand(4, 2) + 0.1
    sk = SkewedChi2Sampler(skewedness=1.0, n_components=20000, random_state=0).fit(Xs_); Zs = sk.transform(Xs_)
    Ksk = np.array([[np.prod([2 * math.sqrt(a + 1) * math.sqrt(b + 1) / (a + b + 2) for a, b in zip(x, y)]) for y in Xs_] for x in Xs_])
    print(f"   SkewedChi2Sampler D=20000: max |Z Z^T - k| {maxdiff(Zs @ Zs.T, Ksk):.4f}")
    report("SkewedChi2Sampler(c=1, D=20000): Z Z^T approximates prod_i 2 sqrt(x_i+c) sqrt(y_i+c)/(x_i+y_i+2c) within 0.03 (documented kernel)", allclose(Zs @ Zs.T, Ksk, 0, 0.03))
    report("SkewedChi2Sampler transform = sqrt(2/D) cos(log(X + c) @ W + b) with W = log(tan(pi u/2))/pi (secant-distributed)", allclose(Zs, math.sqrt(2.0 / 20000) * np.cos(np.log(Xs_ + 1.0) @ sk.random_weights_ + sk.random_offset_), 1e-12, 1e-12))
    Wsk = sk.random_weights_.ravel()
    print(f"   SkewedChi2Sampler random_weights_: mean {Wsk.mean():.4f}, var {Wsk.var():.4f} (pdf sech(pi w) has mean 0, variance 1/4); random_offset_ in [{sk.random_offset_.min():.4f}, {sk.random_offset_.max():.4f}]")
    report("SkewedChi2Sampler random_weights_ ~ 'secant hyperbolic distribution' with pdf sech(pi w) (the density whose Fourier transform gives the skewed-chi2 kernel): mean within 0.01 of 0, variance within 5% of 1/4; random_offset_ in [0, 2 pi)",
           abs(Wsk.mean()) < 0.01 and abs(Wsk.var() / 0.25 - 1) < 0.05 and np.all(sk.random_offset_ >= 0) and np.all(sk.random_offset_ < 2 * np.pi))
    report("SkewedChi2Sampler.transform raises ValueError for entries <= -skewedness", expect_raises(lambda: sk.transform(np.array([[-1.0, 0.5]]))))
    def add_chi2_ref(X, steps, L):
        cols = [np.sqrt(X * L)]
        for j in range(1, steps):
            fac = np.sqrt(2 * X * L / np.cosh(np.pi * j * L)); cols.append(fac * np.cos(j * L * np.log(X))); cols.append(fac * np.sin(j * L * np.log(X)))
        return np.hstack(cols)
    Xc_ = rs.rand(4, 3) + 0.05
    for steps, L in ((1, 0.8), (2, 0.5), (3, 0.4)):
        ac = AdditiveChi2Sampler(sample_steps=steps).fit(Xc_); Za = ac.transform(Xc_)
        report(f"AdditiveChi2Sampler(sample_steps={steps}) transform = [sqrt(xL), sqrt(2xL sech(pi j L)) cos(jL log x), ... sin(...)] with the documented default sample_interval {L} (Vedaldi & Zisserman)", Za.shape == (4, 3 * (2 * steps - 1)) and allclose(Za, add_chi2_ref(Xc_, steps, L), 1e-12, 1e-12))
    ac3 = AdditiveChi2Sampler(sample_steps=3).fit(Xc_); Za3 = ac3.transform(Xc_)
    Kchi = np.array([[np.sum(2 * x * y / (x + y)) for y in Xc_] for x in Xc_])
    print(f"   AdditiveChi2Sampler(3 steps): max |Z Z^T - sum 2xy/(x+y)| {maxdiff(Za3 @ Za3.T, Kchi):.4f}")
    report("AdditiveChi2Sampler(sample_steps=3, default interval 0.4): Z Z^T approximates the additive chi2 kernel sum_i 2 x_i y_i/(x_i + y_i) within 10% relative (truncation at |j| <= 2: sech(3 pi 0.4) = 4.6%)", allclose(Za3 @ Za3.T, Kchi, 0.1, 0))
    Za15 = AdditiveChi2Sampler(sample_steps=15, sample_interval=0.2).fit(Xc_).transform(Xc_)
    print(f"   AdditiveChi2Sampler(15 steps, L=0.2): max rel |Z Z^T - k| {np.max(np.abs(Za15 @ Za15.T - Kchi) / Kchi):.2e}")
    report("AdditiveChi2Sampler(sample_steps=15, sample_interval=0.2): the quadrature converges, Z Z^T = additive chi2 kernel within 1e-3 relative", allclose(Za15 @ Za15.T, Kchi, 1e-3, 0))
    report("AdditiveChi2Sampler(sample_interval=0.3, sample_steps=4) uses the given interval", allclose(AdditiveChi2Sampler(sample_steps=4, sample_interval=0.3).fit(Xc_).transform(Xc_), add_chi2_ref(Xc_, 4, 0.3), 1e-12, 1e-12))
    report("AdditiveChi2Sampler(sample_steps=4) without sample_interval raises ValueError (documented)", expect_raises(lambda: AdditiveChi2Sampler(sample_steps=4).fit(Xc_).transform(Xc_)))
    report("AdditiveChi2Sampler sparse input gives the same features", allclose(AdditiveChi2Sampler().fit(sp.csr_matrix(Xc_)).transform(sp.csr_matrix(Xc_)).toarray(), add_chi2_ref(Xc_, 2, 0.5), 1e-12, 1e-12))
    Xp_ = rs.rand(4, 3)
    Kp = (0.5 * Xp_ @ Xp_.T + 1.0) ** 2
    acc = np.zeros((4, 4)); nrep = 12
    for seed in range(nrep):
        pcs = PolynomialCountSketch(gamma=0.5, coef0=1.0, degree=2, n_components=4000, random_state=seed).fit(Xp_); Zp_ = pcs.transform(Xp_); acc += Zp_ @ Zp_.T
    acc /= nrep
    print(f"   PolynomialCountSketch (12 x 4000 components): mean Z Z^T {np.round(acc, 4).tolist()}\n   (gamma x.y + coef0)^2 {np.round(Kp, 4).tolist()}; max rel diff {np.max(np.abs(acc - Kp) / Kp):.4f}")
    report("PolynomialCountSketch: Z Z^T approximates (gamma x.y + coef0)^degree in expectation (mean over 12 sketches of 4000 components within 5% relative)", np.all(np.abs(acc - Kp) / Kp < 0.05))
    report("PolynomialCountSketch indexHash_ in [0, n_components) of shape (degree, n_features+1 with coef0), bitHash_ in {-1, +1}", pcs.indexHash_.shape == (2, 4) and pcs.indexHash_.min() >= 0 and pcs.indexHash_.max() < 4000 and set(np.unique(pcs.bitHash_).tolist()) <= {-1.0, 1.0})
    def count_sketch_ref(X, pcs):
        Xg_ = np.hstack([np.sqrt(0.5) * X, np.sqrt(1.0) * np.ones((len(X), 1))]); D = pcs.n_components; out = np.zeros((len(X), D))
        for r in range(len(X)):
            prod = np.ones(D, complex)
            for d in range(pcs.degree):
                cs = np.zeros(D)
                for j in range(Xg_.shape[1]): cs[pcs.indexHash_[d, j]] += pcs.bitHash_[d, j] * Xg_[r, j]
                prod *= np.fft.fft(cs)
            out[r] = np.real(np.fft.ifft(prod))
        return out
    report("PolynomialCountSketch transform = ifft(prod_d fft(CountSketch_d([sqrt(gamma) x, sqrt(coef0)]))) (TensorSketch, recomputed with numpy fft)", allclose(pcs.transform(Xp_), count_sketch_ref(Xp_, pcs), 1e-9, 1e-9))
section('kernel_approximation.RBFSampler / SkewedChi2Sampler / AdditiveChi2Sampler / PolynomialCountSketch', _s17)

def _s18():
    global C, C1, C3, Cd, Ci, D0, D1, Xbig, Xrp, Xsp, Zg, Zi, Zs1, Zs2, comp, dens, e_, ga, got, gri, grp, iu, n_, nz, nz3, pinv, ratio, ref, sri, sri2, srp, srp1, srp3, val
    reseed(18)
    for n_, e_ in ((100, 0.1), (1000, 0.5), (100000, 0.1), (5, 0.9)):
        ref = int(mpmath.floor(4 * mpmath.log(n_) / (mpf(e_) ** 2 / 2 - mpf(e_) ** 3 / 3)))
        got = johnson_lindenstrauss_min_dim(n_, eps=e_)
        bound = 4 * mpmath.log(n_) / (mpf(e_) ** 2 / 2 - mpf(e_) ** 3 / 3)
        print(f"   n={n_}, eps={e_}: 4 log n / (eps^2/2 - eps^3/3) = {mpmath.nstr(bound, 12)}; returned {int(got)}")
        report(f"johnson_lindenstrauss_min_dim({n_}, eps={e_}) = floor(4 log n / (eps^2/2 - eps^3/3)) = {ref} (the rounding shown by the docstring examples, e.g. 1e6, eps=0.5 -> 663)", int(got) == ref)
        report(f"johnson_lindenstrauss_min_dim({n_}, eps={e_}) satisfies the documented condition 'n_components >= 4 log(n_samples) / (eps^2 / 2 - eps^3 / 3)' (the 'minimal number of components' is the ceiling, {int(mpmath.ceil(bound))})", int(got) >= bound)
    report("johnson_lindenstrauss_min_dim reproduces its docstring examples: (1e6, 0.5) -> 663; (1e6, [0.5, 0.1, 0.01]) -> [663, 11841, 1112658]; ([1e4, 1e5, 1e6], 0.1) -> [7894, 9868, 11841]",
           int(johnson_lindenstrauss_min_dim(1e6, eps=0.5)) == 663 and np.array_equal(johnson_lindenstrauss_min_dim(1e6, eps=[0.5, 0.1, 0.01]), [663, 11841, 1112658])
           and np.array_equal(johnson_lindenstrauss_min_dim([1e4, 1e5, 1e6], eps=0.1), [7894, 9868, 11841]))
    report("johnson_lindenstrauss_min_dim with arrays of n_samples and eps broadcasts elementwise", np.array_equal(johnson_lindenstrauss_min_dim([100, 1000], eps=[0.1, 0.5]), [johnson_lindenstrauss_min_dim(100, eps=0.1), johnson_lindenstrauss_min_dim(1000, eps=0.5)]))
    report("johnson_lindenstrauss_min_dim(eps=0) raises ValueError", expect_raises(lambda: johnson_lindenstrauss_min_dim(100, eps=0.0)))
    Xrp = rs.randn(30, 50)
    grp = GaussianRandomProjection(n_components=1000, random_state=0).fit(Xrp)
    comp = grp.components_
    print(f"   Gaussian components_ shape {comp.shape}: mean {comp.mean():.5f}, var {comp.var():.6f} (1/n_components = {1/1000})")
    report("GaussianRandomProjection components_ shape (n_components, n_features), entries ~ N(0, 1/n_components): empirical var within 3%, mean within 4 sigma", comp.shape == (1000, 50) and abs(comp.var() * 1000 - 1) < 0.03 and abs(comp.mean()) < 4 * math.sqrt(1 / 1000 / comp.size))
    Zg = grp.transform(Xrp)
    report("GaussianRandomProjection transform = X @ components_.T", allclose(Zg, Xrp @ comp.T, 1e-12, 1e-12))
    D0 = ((Xrp[:, None] - Xrp[None]) ** 2).sum(-1); D1 = ((Zg[:, None] - Zg[None]) ** 2).sum(-1); iu = np.triu_indices(30, 1)
    ratio = D1[iu] / D0[iu]
    print(f"   squared-distance ratios after projection: mean {ratio.mean():.4f}, min {ratio.min():.4f}, max {ratio.max():.4f}")
    report("GaussianRandomProjection(k=1000): pairwise squared distances preserved on average (E ratio = 1, sd sqrt(2/k) = 0.045 per pair): mean ratio within 0.05 of 1 and all 435 ratios within 1 +- 0.3", abs(ratio.mean() - 1) < 0.05 and np.all(np.abs(ratio - 1) < 0.3))
    ga = GaussianRandomProjection(n_components="auto", eps=0.5, random_state=0)
    Xbig = rs.randn(1000, 5000)[:, :]
    try:
        ga.fit(Xbig)
        report("GaussianRandomProjection(n_components='auto', eps=0.5) n_components_ = johnson_lindenstrauss_min_dim(n_samples, eps)", ga.n_components_ == int(johnson_lindenstrauss_min_dim(1000, eps=0.5)) == int(mpmath.floor(4 * mpmath.log(1000) / (mpf("0.5") ** 2 / 2 - mpf("0.5") ** 3 / 3))))
    except Exception as e:
        print(f"   auto n_components: {type(e).__name__}: {e}")
    report("GaussianRandomProjection n_components > n_features fits with a warning only", not expect_raises(lambda: GaussianRandomProjection(n_components=80, random_state=0).fit(Xrp), Exception))
    srp = SparseRandomProjection(n_components=500, random_state=0).fit(np.zeros((2, 100)))
    C = srp.components_; Cd = C.toarray() if sp.issparse(C) else C
    nz = Cd[Cd != 0]; dens = 1 / math.sqrt(100); val = math.sqrt(1 / (dens * 500))
    print(f"   Sparse density_ {srp.density_} (1/sqrt(n_features) = {dens}); nonzero fraction {np.mean(Cd != 0):.4f}; distinct nonzero values {np.unique(nz).tolist()} (+-sqrt(1/(density n_components)) = +-{val:.6f}); fraction positive {np.mean(nz > 0):.4f}")
    report("SparseRandomProjection density_ default = 1/sqrt(n_features) (Ping Li et al., documented)", close(srp.density_, dens, 1e-15))
    report("SparseRandomProjection nonzero entries are exactly +-sqrt(1/(density * n_components)) (Li et al. formula), sign balanced within 2%, nonzero fraction within 0.01 of density", np.all(np.isclose(np.abs(nz), val, rtol=1e-12)) and abs(np.mean(nz > 0) - 0.5) < 0.02 and abs(np.mean(Cd != 0) - dens) < 0.01)
    srp3 = SparseRandomProjection(n_components=300, density=1 / 3, random_state=1).fit(np.zeros((2, 60)))
    C3 = srp3.components_.toarray(); nz3 = C3[C3 != 0]
    report("SparseRandomProjection(density=1/3) (Achlioptas): entries +-sqrt(3/n_components), nonzero fraction ~ 1/3", np.all(np.isclose(np.abs(nz3), math.sqrt(3 / 300), rtol=1e-12)) and abs(np.mean(C3 != 0) - 1 / 3) < 0.02)
    srp1 = SparseRandomProjection(n_components=10, density=1.0, random_state=1).fit(np.zeros((2, 6)))
    C1 = srp1.components_; C1 = C1.toarray() if sp.issparse(C1) else np.asarray(C1)
    report("SparseRandomProjection(density=1): dense +-1/sqrt(n_components) matrix", np.all(np.isclose(np.abs(C1), 1 / math.sqrt(10))))
    Xsp = sp.csr_matrix(rs.rand(8, 100))
    Zs1 = SparseRandomProjection(n_components=500, random_state=0).fit(Xsp).transform(Xsp); Zs2 = SparseRandomProjection(n_components=500, dense_output=True, random_state=0).fit(Xsp).transform(Xsp)
    report("SparseRandomProjection: sparse input -> sparse output by default, dense_output=True -> ndarray with the same values = X @ components_.T", sp.issparse(Zs1) and isinstance(Zs2, np.ndarray) and allclose(Zs1.toarray(), Zs2, 1e-12, 1e-12) and allclose(Zs2, Xsp.toarray() @ Cd.T, 1e-12, 1e-12))
    if V >= (1, 1):   # compute_inverse_components / inverse_transform: versionadded 1.1
        sri = SparseRandomProjection(n_components=150, random_state=0, compute_inverse_components=True).fit(Xrp[:, :50])
        Ci = sri.components_.toarray(); pinv = np.linalg.pinv(Ci)
        report("SparseRandomProjection(compute_inverse_components=True) (1.1+) inverse_components_ = pinv(components_) (numpy pinv, 1e-8)", allclose(sri.inverse_components_, pinv, 1e-8, 1e-10))
        Zi = sri.transform(Xrp[:, :50])
        report("SparseRandomProjection.inverse_transform(Z) = Z @ pinv(components_).T and recovers X when n_components >= n_features (1e-8)", allclose(sri.inverse_transform(Zi), Zi @ pinv.T, 1e-10, 1e-12) and allclose(sri.inverse_transform(Zi), Xrp[:, :50], 1e-8, 1e-8))
        gri = GaussianRandomProjection(n_components=150, random_state=0, compute_inverse_components=True).fit(Xrp[:, :50])
        report("GaussianRandomProjection inverse_components_ = pinv(components_), inverse_transform recovers X", allclose(gri.inverse_components_, np.linalg.pinv(gri.components_), 1e-8, 1e-10) and allclose(gri.inverse_transform(gri.transform(Xrp[:, :50])), Xrp[:, :50], 1e-8, 1e-8))
        sri2 = SparseRandomProjection(n_components=150, random_state=0).fit(Xrp[:, :50])
        report("SparseRandomProjection.inverse_transform without compute_inverse_components computes the pseudo-inverse on the fly (same result)", allclose(sri2.inverse_transform(Zi), Zi @ pinv.T, 1e-10, 1e-12))
section('random_projection', _s18)

print("== done")
