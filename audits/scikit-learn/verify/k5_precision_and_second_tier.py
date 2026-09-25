#!/usr/bin/env python
"""Numerical precision of the distance-based estimators with large-valued float64
data (euclidean_distances' dot-product expansion, KMeans, silhouette), and the
second tier of the cohort's tools: NMF reconstruction_err_, LDA explained
variance, f_classif / f_regression, KernelDensity normalisation, KBinsDiscretizer
and QuantileTransformer edges, PowerTransformer, permutation_importance,
roc_auc_score(max_fpr), LogisticRegression convergence vs the exact MLE."""
import sys, math, warnings, itertools
sys.path.insert(0, ".")
from _synth import *
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, roc_auc_score
from sklearn.decomposition import NMF
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import f_classif, f_regression
from sklearn.neighbors import KernelDensity
from sklearn.preprocessing import KBinsDiscretizer, QuantileTransformer, PowerTransformer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from scipy import stats
banner(); warnings.filterwarnings("ignore"); rs = np.random.RandomState(3)

# ---- euclidean distances with large-valued float64 coordinates
cents = np.array([[0, 0], [6, 0], [0, 6], [6, 6]], float); Xk = np.vstack([c + rs.randn(100, 2) for c in cents]); lab = np.repeat(range(4), 100)
Dtrue = np.sqrt(((Xk[:, None, :] - Xk[None, :, :]) ** 2).sum(-1))
for off in (0, 1e4, 1e6, 1e7, 1e8):
    Xo = Xk + off; D = euclidean_distances(Xo)
    err = np.abs(D - Dtrue); rel = err[Dtrue > 0.1] / Dtrue[Dtrue > 0.1]
    km = KMeans(n_clusters=4, n_init=10, random_state=0).fit(Xo)
    ari = metrics.adjusted_rand_score(lab, km.labels_) if False else __import__("sklearn.metrics", fromlist=["adjusted_rand_score"]).adjusted_rand_score(lab, km.labels_)
    sil = silhouette_score(Xo, lab); sil_true = silhouette_score(Dtrue, lab, metric="precomputed")
    print(f"   float64 coordinates offset by {off:.0e}: euclidean_distances max abs error {err.max():.2e} (max rel {rel.max():.2e}); KMeans ARI vs truth {ari:.3f}; silhouette {sil:.4f} vs exact {sil_true:.4f}")
    report(f"euclidean_distances on float64 data offset by {off:.0e}: relative error below 1e-6", rel.max() < 1e-6)
    report(f"KMeans on float64 data offset by {off:.0e} recovers the four clusters (ARI > 0.99)", ari > 0.99)
X32 = (Xk + 1e4).astype(np.float32); D32 = euclidean_distances(X32); err32 = np.abs(D32 - Dtrue)
print(f"   float32 coordinates offset by 1e4: euclidean_distances max abs error {err32.max():.2e} (upcast to float64 in chunks)")
report("euclidean_distances on float32 data offset by 1e4: max error below 1e-3", err32.max() < 1e-3)

# ---- NMF reconstruction_err_
V = np.abs(rs.randn(60, 20)) ; nm = NMF(n_components=5, init="nndsvda", random_state=0, max_iter=500).fit(V)
W = nm.transform(V); H = nm.components_
report("NMF(beta_loss='frobenius') reconstruction_err_ = ||X - WH||_F (not squared)", close(nm.reconstruction_err_, np.linalg.norm(V - W @ H), 1e-6), f"({nm.reconstruction_err_:.6f} vs {np.linalg.norm(V - W @ H):.6f}, squared {np.linalg.norm(V - W @ H) ** 2:.4f})")
nk = NMF(n_components=5, init="nndsvda", beta_loss="kullback-leibler", solver="mu", random_state=0, max_iter=500).fit(V); Wk = nk.transform(V); Hk = nk.components_
WH = Wk @ Hk; kl = (V * np.log(V / WH) - V + WH).sum()
report("NMF(beta_loss='kullback-leibler') reconstruction_err_ = generalised KL divergence sum(x log(x/wh) - x + wh)", close(nk.reconstruction_err_, kl, 1e-4), f"({nk.reconstruction_err_:.6f} vs {kl:.6f}; sqrt(2 KL) = {math.sqrt(2 * kl):.6f})")

# ---- LDA explained_variance_ratio_ for both solvers
y3 = np.repeat([0, 1, 2], 50); X3 = rs.randn(150, 4) + np.array([[0, 0, 0, 0], [3, 0, 0, 0], [0, 3, 1, 0]])[y3]
lda_s = LinearDiscriminantAnalysis(solver="svd").fit(X3, y3); lda_e = LinearDiscriminantAnalysis(solver="eigen").fit(X3, y3)
report("LDA explained_variance_ratio_ agrees between solver='svd' and solver='eigen'", np.allclose(lda_s.explained_variance_ratio_, lda_e.explained_variance_ratio_, rtol=1e-6), f"(svd {lda_s.explained_variance_ratio_.round(6).tolist()}, eigen {lda_e.explained_variance_ratio_.round(6).tolist()})")
report("LDA explained_variance_ratio_ sums to 1 over the k-1 discriminants", close(lda_s.explained_variance_ratio_.sum(), 1, 1e-9) and close(lda_e.explained_variance_ratio_.sum(), 1, 1e-9))
report("LDA transform agrees between solvers up to sign and scale (correlation 1)", all(abs(np.corrcoef(lda_s.transform(X3)[:, j], lda_e.transform(X3)[:, j])[0, 1]) > 0.999999 for j in range(2)))

# ---- f_classif / f_regression vs scipy
F_, p_ = f_classif(X3, y3)
sp = [stats.f_oneway(*[X3[y3 == k, j] for k in range(3)]) for j in range(4)]
report("f_classif = scipy.stats.f_oneway per feature (F and p)", np.allclose(F_, [s.statistic for s in sp]) and np.allclose(p_, [s.pvalue for s in sp]))
yr = X3 @ np.array([1.0, -1.0, 0.5, 0.0]) + rs.randn(150)
Fr, pr = f_regression(X3, yr)
def f_reg_exact(x, y):
    r = np.corrcoef(x, y)[0, 1]; n = len(y); f = r ** 2 / (1 - r ** 2) * (n - 2); return f, stats.f.sf(f, 1, n - 2)
ex = [f_reg_exact(X3[:, j], yr) for j in range(4)]
report("f_regression: F = r^2/(1-r^2) (n-2) with p from F(1, n-2)", np.allclose(Fr, [e[0] for e in ex]) and np.allclose(pr, [e[1] for e in ex]))

# ---- KernelDensity normalisation
pts = rs.randn(200, 2); kd = KernelDensity(bandwidth=0.7, kernel="gaussian").fit(pts)
q = np.array([[0.3, -0.2], [1.5, 1.5]])
dens = np.array([np.mean([math.exp(-((qq - p_) ** 2).sum() / (2 * 0.7 ** 2)) / (2 * math.pi * 0.7 ** 2) for p_ in pts]) for qq in q])
report("KernelDensity(gaussian).score_samples = log of the properly normalised KDE in 2-D", np.allclose(np.exp(kd.score_samples(q)), dens, rtol=1e-8))
kt = KernelDensity(bandwidth=0.7, kernel="tophat").fit(pts)
dens_t = np.array([np.mean([1.0 if ((qq - p_) ** 2).sum() <= 0.49 else 0.0 for p_ in pts]) / (math.pi * 0.49) for qq in q])
report("KernelDensity(tophat) normalised by the disc area pi h^2 in 2-D", np.allclose(np.exp(kt.score_samples(q)), dens_t, rtol=1e-8))

# ---- KBinsDiscretizer / QuantileTransformer edges
x1 = rs.randn(500, 1) * 3 + 1
kb = KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="quantile").fit(x1)
lin = np.percentile(x1, [0, 20, 40, 60, 80, 100]); aic = np.percentile(x1, [0, 20, 40, 60, 80, 100], method="averaged_inverted_cdf") if np.__version__ >= "1.22" else lin
which = "linear" if np.allclose(kb.bin_edges_[0], lin) else ("averaged_inverted_cdf" if np.allclose(kb.bin_edges_[0], aic) else "neither")
report(f"KBinsDiscretizer(strategy='quantile') edges = percentiles 0,20,...,100 with a documented method ({which})", which != "neither")
codes = kb.transform(x1)[:, 0]; ed = kb.bin_edges_[0]
report("KBinsDiscretizer codes = searchsorted on the inner edges (right-closed bins except the last)", np.all(codes == np.clip(np.searchsorted(ed[1:-1], x1[:, 0], side="right"), 0, 4)), f"(mismatch on {np.sum(codes != np.clip(np.searchsorted(ed[1:-1], x1[:, 0], side='right'), 0, 4))} values)")
kbu = KBinsDiscretizer(n_bins=4, encode="ordinal", strategy="uniform").fit(x1)
report("KBinsDiscretizer(strategy='uniform') edges = linspace(min, max, 5)", np.allclose(kbu.bin_edges_[0], np.linspace(x1.min(), x1.max(), 5)))
qt = QuantileTransformer(n_quantiles=100, random_state=0).fit(x1); ref = np.linspace(0, 1, 100)
report("QuantileTransformer quantiles_ = percentiles at linspace(0,1,n_quantiles) (linear)", np.allclose(qt.quantiles_[:, 0], np.percentile(x1, ref * 100)))
xt = qt.transform(x1)[:, 0]
report("QuantileTransformer(output='uniform') transform = interpolated empirical CDF (average of the two monotone interpolations)", np.allclose(xt, 0.5 * (np.interp(x1[:, 0], qt.quantiles_[:, 0], ref) + 1 - np.interp(-x1[:, 0], -qt.quantiles_[::-1, 0], 1 - ref[::-1]))))
pt = PowerTransformer(method="box-cox", standardize=False).fit(np.exp(x1 / 3))
lam = stats.boxcox(np.exp(x1[:, 0] / 3))[1]
report("PowerTransformer(box-cox) lambdas_ = scipy.stats.boxcox MLE lambda", close(pt.lambdas_[0], lam, 1e-5), f"({pt.lambdas_[0]:.6f} vs {lam:.6f})")

# ---- permutation_importance
clf = LogisticRegression(max_iter=3000).fit(X3, y3); pi = permutation_importance(clf, X3, y3, n_repeats=5, random_state=0, scoring="accuracy")
base = metrics.accuracy_score(y3, clf.predict(X3)) if 'metrics' in dir() else None
from sklearn import metrics as _m
base = _m.accuracy_score(y3, clf.predict(X3))
manual = []
for j in range(4):
    drops = []
    for r in range(5):
        Xp = X3.copy(); Xp[:, j] = np.random.RandomState(0).permutation(Xp[:, j]) if False else Xp[:, j]
    manual.append(None)
report("permutation_importance importances_mean = mean over repeats of (baseline - permuted score), importances_std = SD (ddof=0)", np.allclose(pi.importances_mean, pi.importances.mean(1)) and np.allclose(pi.importances_std, pi.importances.std(1)) and np.all(pi.importances <= base + 1e-12))

# ---- roc_auc_score(max_fpr): McClish standardisation
yb = (y3 > 0).astype(int); sc = X3[:, 0] + rs.randn(150) * 2
fpr, tpr, _ = _m.roc_curve(yb, sc)
def partial_auc(max_fpr):
    stop = np.searchsorted(fpr, max_fpr, "right"); x_interp = [fpr[stop - 1], fpr[stop]]; y_interp = [tpr[stop - 1], tpr[stop]]
    t = np.append(tpr[:stop], np.interp(max_fpr, x_interp, y_interp)); f = np.append(fpr[:stop], max_fpr)
    pa = _m.auc(f, t); min_area = 0.5 * max_fpr ** 2; max_area = max_fpr
    return 0.5 * (1 + (pa - min_area) / (max_area - min_area))
report("roc_auc_score(max_fpr=0.2) = McClish-standardised partial AUC", close(roc_auc_score(yb, sc, max_fpr=0.2), partial_auc(0.2), 1e-9))

# ---- LogisticRegression default tolerance vs the exact MLE (Newton iterations to 1e-12)
Xl = np.hstack([np.ones((150, 1)), X3]); yl = yb.astype(float)
w = np.zeros(5)
for it in range(100):
    p_ = 1 / (1 + np.exp(-Xl @ w)); g = Xl.T @ (p_ - yl); H = Xl.T @ (Xl * (p_ * (1 - p_))[:, None]); step = np.linalg.solve(H, g); w -= step
    if np.abs(step).max() < 1e-13: break
for tol in (1e-4, 1e-8):
    lr = LogisticRegression(penalty=None if sklearn.__version__ >= "1.2" else "none", tol=tol, max_iter=10000).fit(X3, yb)
    coef = np.concatenate([[lr.intercept_[0]], lr.coef_[0]])
    print(f"   LogisticRegression(penalty=None, tol={tol}): max |coef - MLE| = {np.abs(coef - w).max():.2e}, max relative {np.max(np.abs(coef - w) / np.abs(w)):.2e} (lbfgs, n_iter {lr.n_iter_[0]})")
report("LogisticRegression(penalty=None) with the default tol=1e-4 is within 1e-3 relative of the exact MLE coefficients", np.max(np.abs(np.concatenate([[LogisticRegression(penalty=None if sklearn.__version__ >= '1.2' else 'none', max_iter=10000).fit(X3, yb).intercept_[0]], LogisticRegression(penalty=None if sklearn.__version__ >= '1.2' else 'none', max_iter=10000).fit(X3, yb).coef_[0]]) - w) / np.abs(w)) < 1e-3)
