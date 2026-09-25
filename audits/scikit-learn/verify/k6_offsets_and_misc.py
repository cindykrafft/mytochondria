#!/usr/bin/env python
"""Large-offset float64 data through KMeans (inertia, centres), StandardScaler,
PCA and silhouette; roc_curve thresholds; cross_val_predict(predict_proba) with a
class missing from a training fold; SimpleImputer; LabelEncoder / OneHotEncoder
ordering; TSNE perplexity guard and kl_divergence_ attribute."""
import sys, math, warnings
sys.path.insert(0, ".")
from _synth import *
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, roc_curve
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.manifold import TSNE
banner(); warnings.filterwarnings("ignore"); rs = np.random.RandomState(4)
cents = np.array([[0, 0], [6, 0], [0, 6], [6, 6]], float); Xk = np.vstack([c + rs.randn(100, 2) for c in cents]); lab = np.repeat(range(4), 100)
Dtrue = np.sqrt(((Xk[:, None, :] - Xk[None, :, :]) ** 2).sum(-1)); sil_true = silhouette_score(Dtrue, lab, metric="precomputed")
for off in (0, 1e6, 1e8):
    Xo = Xk + off; km = KMeans(n_clusters=4, n_init=10, random_state=0).fit(Xo)
    D2 = ((Xo[:, None, :] - km.cluster_centers_[None, :, :]) ** 2).sum(-1); inertia_true = D2.min(1).sum()
    means = np.array([Xo[km.labels_ == j].mean(0) for j in range(4)])
    print(f"   KMeans float64 offset {off:.0e}: inertia_ {km.inertia_:.4f} vs exact for its own centres {inertia_true:.4f} (rel {abs(km.inertia_ - inertia_true) / inertia_true:.1e}); max |centre - cluster mean| {np.abs(km.cluster_centers_ - means).max():.1e}; labels = nearest centre on {np.mean(km.labels_ == D2.argmin(1)) * 100:.1f} %")
    report(f"KMeans float64 offset {off:.0e}: inertia_ within 1e-6 relative of the exact sum of squared distances to its centres", close(km.inertia_, inertia_true, 1e-6))
    report(f"KMeans float64 offset {off:.0e}: every label is the nearest centre", np.all(km.labels_ == D2.argmin(1)))
    sc = StandardScaler().fit(Xo); report(f"StandardScaler float64 offset {off:.0e}: var_ within 1e-9 relative of exact", np.allclose(sc.var_, Xk.var(0), rtol=1e-9), f"(rel err {np.max(np.abs(sc.var_ / Xk.var(0) - 1)):.1e})")
    p = PCA().fit(Xo); dev = np.max(np.abs(p.explained_variance_ / PCA().fit(Xk).explained_variance_ - 1))
    report(f"PCA float64 offset {off:.0e}: explained_variance_ within 1e-6 relative of the offset-free fit", dev < 1e-6, f"(max relative deviation {dev:.1e})")
    s = silhouette_score(Xo, lab); report(f"silhouette_score float64 offset {off:.0e} within 1e-6 of exact", close(s, sil_true, 1e-6), f"({s:.5f} vs {sil_true:.5f})")

# ---- roc_curve thresholds
y = np.array([0, 0, 1, 1]); s = np.array([0.1, 0.4, 0.35, 0.8]); fpr, tpr, thr = roc_curve(y, s)
print(f"   roc_curve thresholds: {thr.tolist()} (first element {'inf' if np.isinf(thr[0]) else 'max score + 1'})")
report("roc_curve first threshold is above every score so that the curve starts at (0,0)", fpr[0] == 0 and tpr[0] == 0 and thr[0] > s.max())

# ---- cross_val_predict with predict_proba when a class is missing from a training fold
y3 = np.array([0] * 10 + [1] * 10 + [2] * 2); X3 = rs.randn(22, 3) + y3[:, None]
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always")
    P = cross_val_predict(LogisticRegression(max_iter=2000), X3, y3, cv=KFold(2, shuffle=False), method="predict_proba")
print(f"   cross_val_predict(predict_proba) with class 2 absent from a training fold: shape {P.shape}, rows sum to 1: {np.allclose(P.sum(1), 1)}, warning: {[str(w.message)[:90] for w in wl][:1]}")
report("cross_val_predict(predict_proba): output has one column per class of y and the missing class gets probability 0 in that fold", P.shape == (22, 3) and np.allclose(P.sum(1), 1) and np.all(P[:11, 2] == 0) or np.all(P[11:, 2] == 0), f"(column 2 in fold 1 rows max {P[11:, 2].max():.3f})")

# ---- SimpleImputer, encoders
Xm = np.array([[1.0, np.nan], [3.0, 4.0], [np.nan, 8.0], [5.0, 2.0]])
report("SimpleImputer(median) uses np.nanmedian (linear, even-length average)", np.allclose(SimpleImputer(strategy="median").fit(Xm).statistics_, [3.0, 4.0]))
report("SimpleImputer(mean) uses np.nanmean", np.allclose(SimpleImputer(strategy="mean").fit(Xm).statistics_, [3.0, 14 / 3]))
le = LabelEncoder().fit(["b", "a", "c", "a"])
report("LabelEncoder classes_ sorted lexicographically", le.classes_.tolist() == ["a", "b", "c"] and le.transform(["c"]).tolist() == [2])
oh = OneHotEncoder(drop="first").fit(np.array([["b"], ["a"], ["c"]]))
report("OneHotEncoder(drop='first') drops the first sorted category", oh.get_feature_names_out().tolist() == ["x0_b", "x0_c"])

# ---- TSNE
try:
    TSNE(perplexity=30).fit(rs.randn(20, 3)); report("TSNE(perplexity=30) on 20 samples raises (perplexity must be < n_samples)", False)
except ValueError as e: report("TSNE(perplexity=30) on 20 samples raises ValueError", True)
ts = TSNE(perplexity=5, random_state=0, init="pca").fit(rs.randn(40, 3))
report("TSNE exposes kl_divergence_ (non-negative)", ts.kl_divergence_ >= 0, f"({ts.kl_divergence_:.4f})")
