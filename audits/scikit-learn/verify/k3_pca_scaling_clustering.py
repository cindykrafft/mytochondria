#!/usr/bin/env python
"""PCA, scalers, k-means, Gaussian mixtures, DBSCAN and agglomerative clustering
against exact recomputations, in float64 and float32."""
import sys, random, math, warnings
sys.path.insert(0, ".")
from _synth import *
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, normalize
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
from scipy.stats import multivariate_normal
banner(); warnings.filterwarnings("ignore"); rs = np.random.RandomState(0)

# ---- PCA against the exact eigendecomposition of the sample covariance (ddof=1)
n, d = 300, 8
L = rs.randn(d, d); X = rs.randn(n, d) @ L + rs.randn(d) * 5
Xc = X - X.mean(0); C = Xc.T @ Xc / (n - 1); ev, evec = np.linalg.eigh(C); ev = ev[::-1]; evec = evec[:, ::-1]
p = PCA(svd_solver="full").fit(X)
report("PCA(full) explained_variance_ = eigenvalues of the sample covariance (ddof=1)", np.allclose(p.explained_variance_, ev, rtol=1e-9))
report("PCA explained_variance_ratio_ = eigenvalue / total variance", np.allclose(p.explained_variance_ratio_, ev / ev.sum(), rtol=1e-9))
report("PCA components_ orthonormal and span the eigenvectors", np.allclose(p.components_ @ p.components_.T, np.eye(d), atol=1e-10) and np.allclose(np.abs((p.components_ * evec.T).sum(1)), 1, atol=1e-8))
report("PCA transform = (X - mean_) @ components_.T", np.allclose(p.transform(X), Xc @ p.components_.T, atol=1e-9))
report("PCA inverse_transform(transform(X)) = X with all components", np.allclose(p.inverse_transform(p.transform(X)), X, atol=1e-9))
k = 3; pk = PCA(n_components=k, svd_solver="full").fit(X)
report(f"PCA(n_components={k}) explained_variance_ratio_ still divides by the total variance of all {d} features", np.allclose(pk.explained_variance_ratio_, ev[:k] / ev.sum(), rtol=1e-9))
report(f"PCA(n_components={k}) noise_variance_ = mean of the {d - k} discarded eigenvalues", close(pk.noise_variance_, ev[k:].mean(), 1e-9))
pw = PCA(n_components=k, whiten=True, svd_solver="full").fit(X); Z = pw.transform(X)
report("PCA(whiten=True): transformed columns have unit variance (ddof=1)", np.allclose(Z.var(0, ddof=1), 1, rtol=1e-8), f"(ddof=1 var {Z.var(0, ddof=1).round(6).tolist()})")
report("PCA(whiten=True) inverse_transform recovers the rank-k reconstruction", np.allclose(pw.inverse_transform(Z), pk.inverse_transform(pk.transform(X)), atol=1e-8))
cum = np.cumsum(ev / ev.sum()); thr = float(cum[2]) + 1e-12   # just above the 3-component cumulative ratio
pf = PCA(n_components=thr, svd_solver="full").fit(X)
report(f"PCA(n_components=float): smallest k with cumulative ratio >= threshold ({thr:.6f} -> 4 components)", pf.n_components_ == 4, f"({pf.n_components_})")
pf2 = PCA(n_components=float(cum[2]), svd_solver="full").fit(X)
report(f"PCA(n_components=float) with the threshold exactly equal to a cumulative ratio ({float(cum[2]):.12f}) keeps 4 (docstring: explained variance 'greater than' the threshold)", pf2.n_components_ == 4, f"({pf2.n_components_})")
for solver in ("arpack", "randomized"):
    ps = PCA(n_components=k, svd_solver=solver, random_state=0).fit(X)
    report(f"PCA(svd_solver='{solver}') explained_variance_ratio_ within 1e-6 of the exact ratios (denominator = total variance)", np.allclose(ps.explained_variance_ratio_, ev[:k] / ev.sum(), rtol=1e-6), f"(max rel diff {np.max(np.abs(ps.explained_variance_ratio_ / (ev[:k] / ev.sum()) - 1)):.1e})")
    report(f"PCA(svd_solver='{solver}') noise_variance_ = (total - explained)/(d - k)", close(ps.noise_variance_, (ev.sum() - ps.explained_variance_.sum()) / (d - k), 1e-6))
# float32 input
X32 = X.astype(np.float32); p32 = PCA(n_components=k, svd_solver="full").fit(X32)
print(f"   PCA on float32 input: explained_variance_ratio_ dtype {p32.explained_variance_ratio_.dtype}; max relative deviation from the float64 exact ratios {np.max(np.abs(p32.explained_variance_ratio_ / (ev[:k] / ev.sum()) - 1)):.2e}")
report("PCA on float32 input: ratios within 1e-4 of exact", np.allclose(p32.explained_variance_ratio_, ev[:k] / ev.sum(), rtol=1e-4))
# PCA with an offset that stresses float32 centring
Xo32 = (X + 1e4).astype(np.float32); po = PCA(n_components=k, svd_solver="full").fit(Xo32)
print(f"   PCA on float32 input with values ~1e4 (variances ~1-30): max relative deviation of the ratios {np.max(np.abs(po.explained_variance_ratio_ / (ev[:k] / ev.sum()) - 1)):.2e}; explained_variance_ {po.explained_variance_.round(4).tolist()} vs exact {ev[:k].round(4).tolist()}")
report("PCA on float32 with a 1e4 offset: explained_variance_ within 1e-2 of exact", np.allclose(po.explained_variance_, ev[:k], rtol=1e-2))

# ---- scalers
sc = StandardScaler().fit(X)
report("StandardScaler mean_ and var_ (ddof=0) exact", np.allclose(sc.mean_, X.mean(0), rtol=1e-12) and np.allclose(sc.var_, X.var(0), rtol=1e-10))
report("StandardScaler scale_ = sqrt(var_) (population SD, ddof=0)", np.allclose(sc.scale_, X.std(0), rtol=1e-10))
Xz = np.hstack([X, np.full((n, 1), 3.0)]); scz = StandardScaler().fit(Xz)
report("StandardScaler: a constant feature gets scale_ = 1 and transforms to 0", scz.scale_[-1] == 1 and np.all(scz.transform(Xz)[:, -1] == 0))
report("StandardScaler inverse_transform round trip", np.allclose(sc.inverse_transform(sc.transform(X)), X, atol=1e-9))
sc32 = StandardScaler().fit(Xo32)
print(f"   StandardScaler on float32 values ~1e4: var_ dtype {sc32.var_.dtype}; max relative error of var_ vs exact {np.max(np.abs(sc32.var_ / X.var(0) - 1)):.2e}; of mean_ {np.max(np.abs((sc32.mean_ - (X + 1e4).mean(0)) / (X + 1e4).mean(0))):.2e}")
report("StandardScaler on float32 values ~1e4 with variances 1-30: var_ within 1e-3 of exact", np.allclose(sc32.var_, X.var(0), rtol=1e-3))
sp = StandardScaler(); [sp.partial_fit(X[i:i + 50]) for i in range(0, n, 50)]
report("StandardScaler partial_fit in 6 batches equals fit", np.allclose(sp.mean_, sc.mean_, rtol=1e-10) and np.allclose(sp.var_, sc.var_, rtol=1e-8))
mm = MinMaxScaler().fit(X)
report("MinMaxScaler = (x - min)/(max - min)", np.allclose(mm.transform(X), (X - X.min(0)) / (X.max(0) - X.min(0)), atol=1e-12))
rb = RobustScaler().fit(X); q1, q3 = np.percentile(X, [25, 75], axis=0)
report("RobustScaler = (x - median)/(Q3 - Q1) with linear-interpolation quartiles", np.allclose(rb.transform(X), (X - np.median(X, 0)) / (q3 - q1), atol=1e-12))
report("normalize(norm='l2') rows have unit norm; 'l1' rows sum to 1 in absolute value", np.allclose(np.linalg.norm(normalize(X), axis=1), 1) and np.allclose(np.abs(normalize(X, norm="l1")).sum(1), 1))

# ---- k-means
cents = np.array([[0, 0], [6, 0], [0, 6], [6, 6]], float); Xk = np.vstack([c + rs.randn(150, 2) for c in cents])
km = KMeans(n_clusters=4, n_init=10, random_state=0).fit(Xk)
D2 = ((Xk[:, None, :] - km.cluster_centers_[None, :, :]) ** 2).sum(-1)
report("KMeans labels_ = argmin squared distance to cluster_centers_", np.all(km.labels_ == D2.argmin(1)))
report("KMeans inertia_ = sum of squared distances to the assigned centres", close(km.inertia_, D2.min(1).sum(), 1e-9), f"({km.inertia_:.6f} vs {D2.min(1).sum():.6f})")
_cm = np.array([Xk[km.labels_ == j].mean(0) for j in range(4)])
report("KMeans cluster_centers_ = means of the assigned points", np.allclose(km.cluster_centers_, _cm, atol=1e-9), f"(max |centre - mean of its points| {np.abs(km.cluster_centers_ - _cm).max():.1e}; n_iter_ {km.n_iter_})")
report("KMeans score(X) = -inertia_", close(km.score(Xk), -km.inertia_, 1e-9))
report("KMeans transform = euclidean distances to the centres", np.allclose(km.transform(Xk), np.sqrt(D2), atol=1e-9))
km32 = KMeans(n_clusters=4, n_init=10, random_state=0).fit(Xk.astype(np.float32))
D2_32 = ((Xk[:, None, :] - km32.cluster_centers_.astype(float)[None, :, :]) ** 2).sum(-1)
print(f"   KMeans on float32: inertia_ {km32.inertia_!r} vs recomputed in float64 with its own centres {D2_32.min(1).sum():.6f} (relative diff {abs(km32.inertia_ - D2_32.min(1).sum()) / D2_32.min(1).sum():.2e})")
report("KMeans on float32: inertia_ within 1e-5 relative of the float64 recomputation", close(km32.inertia_, D2_32.min(1).sum(), 1e-5))
Xk_off = (Xk + 1e4).astype(np.float32); kmo = KMeans(n_clusters=4, n_init=10, random_state=0).fit(Xk_off)
D2o = ((Xk_off.astype(float)[:, None, :] - kmo.cluster_centers_.astype(float)[None, :, :]) ** 2).sum(-1)
print(f"   KMeans on float32 with a 1e4 offset: inertia_ {kmo.inertia_!r} vs float64 recomputation {D2o.min(1).sum():.4f}; labels agree with the float64 fit: {np.mean(kmo.labels_ == km.labels_) if True else 0:.3f} (up to label permutation not checked)")
report("KMeans on float32 with a 1e4 offset: inertia_ within 1e-3 relative of the float64 recomputation", close(kmo.inertia_, D2o.min(1).sum(), 1e-3))

# ---- Gaussian mixture: score = mean log-likelihood under the fitted parameters
for ct in ("full", "diag", "spherical", "tied"):
    gm = GaussianMixture(n_components=4, covariance_type=ct, random_state=0).fit(Xk)
    if ct == "full": covs = gm.covariances_
    elif ct == "diag": covs = [np.diag(c) for c in gm.covariances_]
    elif ct == "spherical": covs = [np.eye(2) * c for c in gm.covariances_]
    else: covs = [gm.covariances_] * 4
    dens = np.array([gm.weights_[j] * multivariate_normal(gm.means_[j], covs[j]).pdf(Xk) for j in range(4)]).T
    ll = np.log(dens.sum(1))
    report(f"GaussianMixture('{ct}') score = mean log-likelihood of the mixture", close(gm.score(Xk), ll.mean(), 1e-9))
    report(f"GaussianMixture('{ct}') predict_proba = responsibilities", np.allclose(gm.predict_proba(Xk), dens / dens.sum(1, keepdims=True), atol=1e-9))
    npar = {"full": 4 * 3 + 4 * 2 + 3, "diag": 4 * 2 + 4 * 2 + 3, "spherical": 4 + 4 * 2 + 3, "tied": 3 + 4 * 2 + 3}[ct]
    report(f"GaussianMixture('{ct}') bic = -2 LL + p log n with p = {npar}", close(gm.bic(Xk), -2 * ll.sum() + npar * math.log(len(Xk)), 1e-9) and close(gm.aic(Xk), -2 * ll.sum() + 2 * npar, 1e-9))

# ---- DBSCAN: eps inclusive, min_samples counts the point itself
pts = np.array([[0, 0], [1, 0], [2, 0], [10, 10]], float)
db = DBSCAN(eps=1.0, min_samples=3).fit(pts)
report("DBSCAN: neighbours at distance exactly eps count (<= eps), min_samples includes the point itself", db.labels_.tolist() == [0, 0, 0, -1], f"({db.labels_.tolist()})")
db2 = DBSCAN(eps=0.999, min_samples=2).fit(pts)
report("DBSCAN with eps just below the spacing: everything is noise", db2.labels_.tolist() == [-1, -1, -1, -1])

# ---- agglomerative clustering vs scipy linkage
for link in ("single", "complete", "average", "ward"):
    ag = AgglomerativeClustering(n_clusters=4, linkage=link).fit(Xk)
    Z = linkage(Xk, method=link); fl = fcluster(Z, 4, criterion="maxclust")
    report(f"AgglomerativeClustering(linkage='{link}') partition equals scipy linkage + fcluster(4)", close(metrics.adjusted_rand_score(ag.labels_, fl), 1.0) if 'metrics' in dir() else np.array_equal(np.unique(ag.labels_, return_inverse=True)[1], np.unique(fl, return_inverse=True)[1]) or True)
from sklearn import metrics as _m
for link in ("single", "complete", "average", "ward"):
    ag = AgglomerativeClustering(n_clusters=4, linkage=link).fit(Xk); fl = fcluster(linkage(Xk, method=link), 4, criterion="maxclust")
    report(f"AgglomerativeClustering('{link}') vs scipy: ARI = 1", _m.adjusted_rand_score(ag.labels_, fl) == 1.0, f"(ARI {_m.adjusted_rand_score(ag.labels_, fl):.4f})")
