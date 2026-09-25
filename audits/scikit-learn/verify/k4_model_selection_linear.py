#!/usr/bin/env python
"""Model selection and linear models against exact recomputations: KFold and
StratifiedKFold fold sizes and class proportions, train_test_split stratify,
cross_val_score vs manual folds, GridSearchCV mean_test_score (unweighted mean
over folds), permutation_test_score p-value, calibration_curve bins,
LinearRegression / Ridge (intercept unpenalised, alpha not scaled by n,
sample_weight) exact, LogisticRegression class_weight='balanced' and predict_proba
consistency, RandomForest feature_importances_ normalisation and OOB score,
SVC probability vs predict, mutual_info_classif."""
import sys, random, math, warnings, collections
sys.path.insert(0, ".")
from _synth import *
from sklearn.model_selection import KFold, StratifiedKFold, train_test_split, cross_val_score, GridSearchCV, permutation_test_score, cross_validate
from sklearn.linear_model import LinearRegression, Ridge, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.calibration import calibration_curve
from sklearn import metrics
banner(); warnings.filterwarnings("ignore"); rs = np.random.RandomState(1)

# ---- fold sizes and stratification
n = 103; y = np.array([0] * 70 + [1] * 25 + [2] * 8); rs.shuffle(y); X = rs.randn(n, 5) + y[:, None]
sizes = [len(te) for _, te in KFold(5).split(X)]
report("KFold(5) on 103 samples: the first 103 % 5 = 3 folds have one extra sample (21,21,21,20,20)", sizes == [21, 21, 21, 20, 20], f"({sizes})")
skf = list(StratifiedKFold(5, shuffle=True, random_state=0).split(X, y))
cls = [collections.Counter(y[te].tolist()) for _, te in skf]
report("StratifiedKFold(5): every fold's class counts differ from the proportional share by at most 1", all(abs(c[k] - len(te) * (y == k).mean()) <= 1 for c, (_, te) in zip(cls, skf) for k in (0, 1, 2)), f"({[dict(c) for c in cls]})")
report("StratifiedKFold: the 8-sample class is spread over folds (no fold without it, at most 2 per fold)", all(1 <= c[2] <= 2 for c in cls))
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)
report("train_test_split(test_size=0.25, stratify=y): test size = ceil(0.25 n) = 26 and class counts within 1 of proportional", len(yte) == 26 and all(abs((yte == k).sum() - 26 * (y == k).mean()) <= 1 for k in (0, 1, 2)), f"(test {len(yte)}, counts {collections.Counter(yte.tolist())})")
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)
report("train_test_split(test_size=0.2) on 103 samples: test size = ceil(20.6) = 21", len(yte) == 21, f"({len(yte)})")

# ---- cross_val_score = manual folds; GridSearchCV mean = unweighted mean over folds
clf = LogisticRegression(max_iter=2000)
cv = StratifiedKFold(5, shuffle=True, random_state=0)
cvs = cross_val_score(clf, X, y, cv=cv, scoring="accuracy")
manual = [metrics.accuracy_score(y[te], LogisticRegression(max_iter=2000).fit(X[tr], y[tr]).predict(X[te])) for tr, te in cv.split(X, y)]
report("cross_val_score = per-fold accuracy of a fresh fit on each training fold", np.allclose(cvs, manual))
gs = GridSearchCV(LogisticRegression(max_iter=2000), {"C": [0.1, 1.0]}, cv=KFold(5), scoring="accuracy").fit(X, y)
folds = [metrics.accuracy_score(y[te], LogisticRegression(C=0.1, max_iter=2000).fit(X[tr], y[tr]).predict(X[te])) for tr, te in KFold(5).split(X)]
pooled = sum(f * len(te) for f, (_, te) in zip(folds, KFold(5).split(X))) / n
report("GridSearchCV mean_test_score = unweighted mean of the fold scores (folds of 21 and 20 samples)", close(gs.cv_results_["mean_test_score"][0], np.mean(folds), 1e-12), f"(unweighted {np.mean(folds):.6f}, sample-weighted {pooled:.6f})")
report("GridSearchCV std_test_score = population SD (ddof=0) of the fold scores", close(gs.cv_results_["std_test_score"][0], np.std(folds), 1e-12))
score, perm_scores, pval = permutation_test_score(LogisticRegression(max_iter=2000), X, y, cv=KFold(5), n_permutations=30, random_state=0)
report("permutation_test_score p-value = (C + 1)/(n_permutations + 1) with C = permutations scoring >= the true score", close(pval, (np.sum(perm_scores >= score) + 1) / 31, 1e-12))

# ---- calibration_curve
yb = (y > 0).astype(int); prob = np.clip(rs.beta(2, 2, n) * 0.5 + yb * 0.4, 0, 1)
ft, mp = calibration_curve(yb, prob, n_bins=5, strategy="uniform")
edges = np.linspace(0, 1, 6); ids = np.searchsorted(edges[1:-1], prob)
ft_e = [yb[ids == b].mean() for b in range(5) if (ids == b).any()]; mp_e = [prob[ids == b].mean() for b in range(5) if (ids == b).any()]
report("calibration_curve(strategy='uniform', 5 bins): bins [0,.2),[.2,.4),...,[.8,1]; fraction of positives and mean predicted per non-empty bin", np.allclose(ft, ft_e) and np.allclose(mp, mp_e))
ftq, mpq = calibration_curve(yb, prob, n_bins=4, strategy="quantile")
qedges = np.percentile(prob, np.linspace(0, 100, 5)); idq = np.searchsorted(qedges[1:-1], prob)
report("calibration_curve(strategy='quantile'): edges at percentiles (linear), bins by searchsorted on the inner edges", np.allclose(ftq, [yb[idq == b].mean() for b in range(4)]) and np.allclose(mpq, [prob[idq == b].mean() for b in range(4)]))

# ---- linear models, exact
Xr = rs.randn(60, 3); beta = np.array([1.5, -2.0, 0.5]); yr = Xr @ beta + 0.7 + rs.randn(60) * 0.3
A = np.hstack([np.ones((60, 1)), Xr]); ols = np.linalg.solve(A.T @ A, A.T @ yr)
lr = LinearRegression().fit(Xr, yr)
report("LinearRegression = OLS with intercept (normal equations)", np.allclose(lr.coef_, ols[1:], rtol=1e-9) and close(lr.intercept_, ols[0], 1e-9))
alpha = 2.5; Xc = Xr - Xr.mean(0); yc = yr - yr.mean()
rc = np.linalg.solve(Xc.T @ Xc + alpha * np.eye(3), Xc.T @ yc); ri = yr.mean() - Xr.mean(0) @ rc
rg = Ridge(alpha=alpha).fit(Xr, yr)
report("Ridge(alpha): solves (Xc'Xc + alpha I) w = Xc'yc on centred data, intercept unpenalised, alpha NOT scaled by n", np.allclose(rg.coef_, rc, rtol=1e-8) and close(rg.intercept_, ri, 1e-8))
w = rs.uniform(0.5, 2, 60); W = np.diag(w); xm = (w @ Xr) / w.sum(); ym = (w @ yr) / w.sum(); Xcw = Xr - xm; ycw = yr - ym
rcw = np.linalg.solve(Xcw.T @ W @ Xcw + alpha * np.eye(3), Xcw.T @ W @ ycw); riw = ym - xm @ rcw
rgw = Ridge(alpha=alpha).fit(Xr, yr, sample_weight=w)
report("Ridge with sample_weight: weighted centring and weighted normal equations, alpha unchanged", np.allclose(rgw.coef_, rcw, rtol=1e-8) and close(rgw.intercept_, riw, 1e-8))
rg2 = Ridge(alpha=alpha).fit(np.vstack([Xr, Xr]), np.concatenate([yr, yr]))
rgd = Ridge(alpha=alpha).fit(Xr, yr, sample_weight=np.full(60, 2.0))
report("Ridge: duplicating every sample equals sample_weight=2 (and differs from the unweighted fit because alpha is absolute)", np.allclose(rg2.coef_, rgd.coef_, rtol=1e-8) and not np.allclose(rg2.coef_, rg.coef_, rtol=1e-6))
# logistic regression
lg = LogisticRegression(max_iter=5000, C=1e6).fit(Xr, (yr > yr.mean()).astype(int))
report("LogisticRegression predict = argmax predict_proba and predict_proba rows sum to 1", np.all(lg.predict(Xr) == lg.predict_proba(Xr).argmax(1)) and np.allclose(lg.predict_proba(Xr).sum(1), 1))
report("LogisticRegression predict_proba = sigmoid(decision_function) (binary)", np.allclose(lg.predict_proba(Xr)[:, 1], 1 / (1 + np.exp(-lg.decision_function(Xr))), atol=1e-12))
cw = LogisticRegression(class_weight="balanced", max_iter=5000).fit(X, y)
from sklearn.utils.class_weight import compute_class_weight
cwv = compute_class_weight("balanced", classes=np.array([0, 1, 2]), y=y)
report("class_weight='balanced' = n / (k n_c)", np.allclose(cwv, n / (3 * np.bincount(y))))
lgm = LogisticRegression(max_iter=5000).fit(X, y)
report("LogisticRegression multiclass: predict_proba = softmax(decision_function)", np.allclose(lgm.predict_proba(X), np.exp(lgm.decision_function(X)) / np.exp(lgm.decision_function(X)).sum(1, keepdims=True), atol=1e-10))

# ---- random forest
rf = RandomForestClassifier(n_estimators=50, oob_score=True, random_state=0).fit(X, y)
report("RandomForest feature_importances_ sum to 1 and equal the mean of the trees' importances", close(rf.feature_importances_.sum(), 1, 1e-12) and np.allclose(rf.feature_importances_, np.mean([t.feature_importances_ for t in rf.estimators_], 0), atol=1e-12))
oob_pred = rf.oob_decision_function_.argmax(1)
report("oob_score_ = accuracy of the out-of-bag votes", close(rf.oob_score_, metrics.accuracy_score(y, rf.classes_[oob_pred]), 1e-12))
report("RandomForest predict_proba = mean of the trees' predict_proba", np.allclose(rf.predict_proba(X), np.mean([t.predict_proba(X) for t in rf.estimators_], 0), atol=1e-12))

# ---- SVC probability vs predict (documented inconsistency)
sv = SVC(probability=True, random_state=0).fit(X, y)
dis = np.mean(sv.predict(X) != sv.classes_[sv.predict_proba(X).argmax(1)])
print(f"   SVC(probability=True): predict disagrees with argmax predict_proba on {dis * 100:.1f} % of the training samples (Platt scaling with internal CV; documented)")

# ---- mutual_info_classif on a discrete feature equals mutual_info_score
from sklearn.feature_selection import mutual_info_classif
xd = rs.randint(0, 3, n); mi = mutual_info_classif(xd.reshape(-1, 1), y, discrete_features=True)[0]
report("mutual_info_classif(discrete_features=True) = mutual_info_score (natural log)", close(mi, metrics.mutual_info_score(xd, y), 1e-12))
