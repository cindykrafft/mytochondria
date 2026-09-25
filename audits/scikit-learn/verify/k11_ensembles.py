#!/usr/bin/env python
"""Ensembles against independent recomputations (Fraction / closed forms / plain-Python
reference implementations / documented invariants):
GradientBoosting (init_ prior, negative-gradient targets, line-search leaf values per
loss, learning_rate, staged_predict = cumulative sum, subsample / oob_improvement_,
n_iter_no_change early stopping, feature_importances_, multiclass softmax, train_score_),
HistGradientBoosting (bin thresholds, NaN bin, categorical + unknown categories,
monotonic_cst, interaction_cst, early_stopping='auto', hand-computed first Newton step
with l2_regularization / min_samples_leaf / sample_weight for every loss, class_weight),
AdaBoost SAMME and AdaBoost.R2, Bagging (sample / feature draws, OOB), Voting, Stacking,
IsolationForest (path lengths, c(n), offset_), RandomTreesEmbedding, RandomForest /
ExtraTrees (bootstrap counts, OOB, balanced_subsample, min_impurity_decrease,
monotonic_cst, importances, predict = argmax mean proba, warm_start), random_state."""
import os
# The container advertises many CPUs but has a small CPU quota: OpenMP oversubscription makes one HGBT
# boosting round take seconds instead of milliseconds. One thread does not change any result.
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import sys, math, warnings, collections, traceback
sys.path.insert(0, ".")
from _synth import *
from fractions import Fraction as F
import numpy as np, sklearn
import scipy.sparse as sp
from sklearn.ensemble import (GradientBoostingClassifier, GradientBoostingRegressor, HistGradientBoostingClassifier,
                              HistGradientBoostingRegressor, AdaBoostClassifier, AdaBoostRegressor, BaggingClassifier,
                              BaggingRegressor, VotingClassifier, VotingRegressor, StackingClassifier, StackingRegressor,
                              IsolationForest, RandomTreesEmbedding, ExtraTreesClassifier, ExtraTreesRegressor,
                              RandomForestClassifier, RandomForestRegressor)
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression, RidgeCV
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.model_selection import cross_val_predict, StratifiedKFold, KFold, train_test_split
from sklearn.base import clone
banner(); warnings.filterwarnings("ignore")
V = tuple(int(x) for x in sklearn.__version__.split(".")[:2])

# ---------------------------------------------------------------- helpers
def est_kw(e): return {"estimator": e} if V >= (1, 2) else {"base_estimator": e}
def ada_kw(): return {} if V >= (1, 6) else {"algorithm": "SAMME"}
def section(name, fn):
    print(f"---- {name}")
    try: fn()
    except Exception as e:
        report(f"[{name}] section ran to completion", False, f"crashed: {type(e).__name__}: {e}")
        traceback.print_exc(file=sys.stdout)
def fr(a): return [F(float(v)) for v in np.asarray(a, dtype=float).ravel()]
def frac(p): return F(str(p)) if isinstance(p, float) else F(p)   # F(0.9) is not 9/10; F("0.9") is
def q_linear(vals, p):
    """numpy's default 'linear' quantile (Hyndman-Fan type 7), exact in Fraction."""
    s = sorted(fr(vals)); n = len(s); h = frac(p) * (n - 1); lo = math.floor(h); f_ = h - lo
    return s[lo] if f_ == 0 else s[lo] + f_ * (s[lo + 1] - s[lo])
def q_lower(vals, p):
    """'inverted_cdf' / lower weighted percentile with unit weights: smallest x with F(x) >= p."""
    s = sorted(fr(vals)); n = len(s); k = math.ceil(frac(p) * n); return s[max(k, 1) - 1]
def median_interval(vals):
    s = sorted(fr(vals)); n = len(s); return s[(n - 1) // 2], s[n // 2]
def pinball(vals, v, a):
    a = frac(a); v = F(v); return sum((x - v) * a if x >= v else (v - x) * (1 - a) for x in fr(vals))
def huber_sum(vals, delta):
    d = F(delta); tot = F(0)
    for x in fr(vals):
        ax = abs(x); tot += x * x / 2 if ax <= d else d * (ax - d / 2)
    return tot
def logit(p): return math.log(p / (1 - p))
def expit(z): return 1 / (1 + np.exp(-np.asarray(z, float)))
def softmax(z):
    z = np.asarray(z, float); e = np.exp(z - z.max(-1, keepdims=True)); return e / e.sum(-1, keepdims=True)
def const(g): return float(np.asarray(g.init_.constant_).ravel()[0])   # DummyRegressor.constant_ has shape (1, 1) in recent versions
def leaf_groups(tree, X):
    idx = tree.apply(X); return {int(l): np.nonzero(idx == l)[0] for l in np.unique(idx)}
def importances_by_hand(tree, n_features, normalize):
    """Sum over internal nodes of w_n*imp_n - w_l*imp_l - w_r*imp_r per feature, / w_root (the documented
    'total reduction of the criterion brought by that feature')."""
    t = tree.tree_; imp = np.zeros(n_features)
    for node in range(t.node_count):
        l, r = t.children_left[node], t.children_right[node]
        if l == -1: continue
        imp[t.feature[node]] += (t.weighted_n_node_samples[node] * t.impurity[node] - t.weighted_n_node_samples[l] * t.impurity[l]
                                 - t.weighted_n_node_samples[r] * t.impurity[r])
    imp /= t.weighted_n_node_samples[0]
    if normalize and imp.sum() > 0: imp = imp / imp.sum()
    return imp
def monotone(f, X, feat, direction, rs, n_anchor=15, n_grid=25):
    """Predictions non-decreasing (direction=1) / non-increasing (-1) along feat, other features fixed."""
    lo, hi = X[:, feat].min(), X[:, feat].max(); ok = True
    for a in rs.choice(len(X), n_anchor, replace=False):
        G = np.repeat(X[a:a + 1], n_grid, 0); G[:, feat] = np.linspace(lo, hi, n_grid); p = f(G)
        ok &= bool(np.all(direction * np.diff(p) >= -1e-12))
    return ok
rs = np.random.RandomState(1)

# ================================================================ GradientBoosting
def sec_gb():
    n = 21; Xr = rs.randn(n, 3); yr = Xr @ np.array([1.0, -2.0, 0.5]) + rs.randn(n) * 0.5 + 3.0
    # ---- init_ priors (documented: DummyEstimator predicting the mean for squared_error, a quantile otherwise)
    g = GradientBoostingRegressor(n_estimators=1, random_state=0).fit(Xr, yr)
    report("GBR init_ for loss='squared_error' is DummyRegressor(strategy='mean'): constant_ = mean(y)", close(const(g), float(sum(fr(yr)) / n), 1e-12), f"({const(g):.6f})")
    for loss in ("absolute_error", "huber"):
        g = GradientBoostingRegressor(loss=loss, n_estimators=1, random_state=0).fit(Xr, yr)
        report(f"GBR init_ for loss='{loss}' is DummyRegressor(quantile=0.5): constant_ = median(y) (n = 21, unambiguous)", close(const(g), float(q_linear(yr, 0.5)), 1e-12))
    g = GradientBoostingRegressor(loss="quantile", alpha=0.9, n_estimators=1, random_state=0).fit(Xr, yr)
    report("GBR init_ for loss='quantile', alpha=0.9: constant_ = 0.9-quantile of y (n = 21: order statistic 19 under both the linear and the inverted-cdf definition)", close(const(g), float(q_linear(yr, 0.9)), 1e-12) and q_linear(yr, 0.9) == q_lower(yr, 0.9))
    g = GradientBoostingRegressor(init="zero", n_estimators=1, learning_rate=0.3, random_state=0).fit(Xr, yr)
    report("GBR init='zero': predict = 0 + learning_rate * first tree", np.allclose(g.predict(Xr), 0.3 * g.estimators_[0, 0].predict(Xr), atol=1e-10))
    g = GradientBoostingRegressor(init=LinearRegression(), n_estimators=1, learning_rate=0.3, random_state=0).fit(Xr, yr)
    report("GBR init=LinearRegression(): predict = init_.predict + learning_rate * first tree, init_ fitted on the training data", np.allclose(g.predict(Xr), LinearRegression().fit(Xr, yr).predict(Xr) + 0.3 * g.estimators_[0, 0].predict(Xr), atol=1e-9))
    Xc = rs.randn(40, 3); yc = (Xc[:, 0] + 0.5 * Xc[:, 1] + rs.randn(40) * 0.5 > 0).astype(int); p1 = yc.mean()
    for loss, exp0, lab in (("log_loss", logit(p1), "log-odds"), ("exponential", 0.5 * logit(p1), "half the log-odds")):
        c = GradientBoostingClassifier(loss=loss, n_estimators=1, learning_rate=0.3, random_state=0).fit(Xc, yc)
        raw0 = c.decision_function(Xc) - 0.3 * c.estimators_[0, 0].predict(Xc)
        report(f"GBC loss='{loss}': initial raw prediction = {lab} of the class prior (DummyClassifier(strategy='prior'))", np.allclose(raw0, exp0, atol=1e-10), f"(raw0 {raw0[0]:.6f}, expected {exp0:.6f})")
    ym = rs.randint(0, 3, 60); Xm = rs.randn(60, 3) + ym[:, None] * 0.8; prior = np.bincount(ym) / 60
    c = GradientBoostingClassifier(n_estimators=1, learning_rate=0.3, random_state=0).fit(Xm, ym)
    raw0 = c.decision_function(Xm) - 0.3 * np.column_stack([c.estimators_[0, k].predict(Xm) for k in range(3)])
    report("GBC multiclass (K=3): estimators_ has K trees per stage and softmax(initial raw) = class priors", c.estimators_.shape == (1, 3) and np.allclose(softmax(raw0), prior, atol=1e-10))

    # ---- stage-1 tree targets and the documented line search per loss (max_depth=2, one stage, lr=0.3)
    lr = 0.3
    g = GradientBoostingRegressor(n_estimators=1, max_depth=2, learning_rate=lr, random_state=0).fit(Xr, yr)
    t = g.estimators_[0, 0]; r = yr - const(g)
    report("GBR squared_error: stage-1 tree fitted to the negative gradient y - init (leaf value = mean residual of the leaf; squared error needs no line search)", all(close(t.tree_.value[l, 0, 0], r[i].mean(), 1e-10) for l, i in leaf_groups(t, Xr).items()))
    report("GBR predict = init + learning_rate * leaf value", np.allclose(g.predict(Xr), const(g) + lr * t.predict(Xr), atol=1e-10))
    g = GradientBoostingRegressor(loss="absolute_error", n_estimators=1, max_depth=2, learning_rate=lr, random_state=0).fit(Xr, yr)
    t = g.estimators_[0, 0]; r = yr - const(g); ok = True; det = []
    for l, i in leaf_groups(t, Xr).items():
        lo, hi = median_interval(r[i]); v = F(float(t.tree_.value[l, 0, 0])); ok &= lo <= v <= hi; det.append((len(i), round(float(v), 5), round(float(lo), 5), round(float(hi), 5)))
    report("GBR absolute_error: leaf value = argmin_v sum|r_i - v| over the leaf (a median of the leaf residuals; the line search)", ok, f"(leaf size, value, median interval) {det}")
    a = 0.8; g = GradientBoostingRegressor(loss="quantile", alpha=a, n_estimators=1, max_depth=2, learning_rate=lr, random_state=0).fit(Xr, yr)
    t = g.estimators_[0, 0]; r = yr - const(g); ok = True
    for l, i in leaf_groups(t, Xr).items():
        v = float(t.tree_.value[l, 0, 0]); best = min(pinball(r[i], c_, a) for c_ in r[i]); ok &= pinball(r[i], v, a) <= best + F(1, 10 ** 12)
    report("GBR quantile(alpha=0.8): leaf value minimises the pinball loss over the leaf residuals (an 0.8-quantile; the line search)", ok)
    g = GradientBoostingRegressor(loss="huber", alpha=0.9, n_estimators=1, max_depth=2, learning_rate=lr, random_state=0).fit(Xr, yr)
    t = g.estimators_[0, 0]; r = yr - const(g); delta = float(q_linear(np.abs(r), 0.9)); ok = True; which = []
    assert q_linear(np.abs(r), 0.9) == q_lower(np.abs(r), 0.9)
    for l, i in leaf_groups(t, Xr).items():
        v = float(t.tree_.value[l, 0, 0]); cands = {}
        for name, med in (("lower-median", float(q_lower(r[i], 0.5))), ("linear-median", float(q_linear(r[i], 0.5)))):
            cands[name] = med + np.mean(np.clip(r[i] - med, -delta, delta))
        m = [k for k, val in cands.items() if close(v, val, 1e-10)]; ok &= bool(m); which.append((len(i), m))
    report("GBR huber(alpha=0.9): leaf value = median(r) + mean(clip(r - median, -delta, delta)) with delta = 0.9-quantile of |y - init| (Friedman 2001; median = lower or linear definition)", ok, f"{which}")
    c = GradientBoostingClassifier(n_estimators=1, max_depth=2, learning_rate=lr, random_state=0).fit(Xc, yc)
    t = c.estimators_[0, 0]; ok = True
    for l, i in leaf_groups(t, Xc).items():
        ok &= close(t.tree_.value[l, 0, 0], (yc[i] - p1).sum() / (len(i) * p1 * (1 - p1)), 1e-10)
    report("GBC log_loss: leaf value = sum(y - p) / sum(p(1-p)) over the leaf (one Newton step, p = prior at stage 1)", ok)
    report("GBC log_loss: predict_proba[:,1] = expit(decision_function), decision = init + lr * leaf", np.allclose(c.predict_proba(Xc)[:, 1], expit(logit(p1) + lr * t.predict(Xc)), atol=1e-10))
    c = GradientBoostingClassifier(loss="exponential", n_estimators=1, max_depth=2, learning_rate=lr, random_state=0).fit(Xc, yc)
    t = c.estimators_[0, 0]; ys = 2 * yc - 1; raw0 = 0.5 * logit(p1); ok = True
    for l, i in leaf_groups(t, Xc).items():
        ok &= close(t.tree_.value[l, 0, 0], (ys[i] * np.exp(-ys[i] * raw0)).sum() / np.exp(-ys[i] * raw0).sum(), 1e-10)
    report("GBC exponential: leaf value = sum(y* exp(-y* raw)) / sum(exp(-y* raw)), y* = 2y-1 (Newton step on the exponential loss)", ok)
    report("GBC exponential: predict_proba[:,1] = expit(2 * decision_function)", np.allclose(c.predict_proba(Xc)[:, 1], expit(2 * c.decision_function(Xc)), atol=1e-10))
    c = GradientBoostingClassifier(n_estimators=1, max_depth=2, learning_rate=lr, random_state=0).fit(Xm, ym); ok = True
    for k in range(3):
        t = c.estimators_[0, k]; yk = (ym == k).astype(float); pk = prior[k]
        for l, i in leaf_groups(t, Xm).items():
            ok &= close(t.tree_.value[l, 0, 0], (2 / 3) * (yk[i] - pk).sum() / (len(i) * pk * (1 - pk)), 1e-10)
    report("GBC multiclass log_loss: tree k leaf value = (K-1)/K * sum(y_k - p_k) / sum(p_k(1-p_k)) (Friedman's factor kept)", ok)
    report("GBC multiclass: predict_proba = softmax(decision_function) and predict = classes_[argmax]", np.allclose(c.predict_proba(Xm), softmax(c.decision_function(Xm)), atol=1e-12) and np.all(c.predict(Xm) == c.classes_[c.predict_proba(Xm).argmax(1)]))

    # ---- learning_rate scaling and staged predictions = cumulative sums
    g1 = GradientBoostingRegressor(n_estimators=1, max_depth=2, learning_rate=0.1, random_state=0).fit(Xr, yr)
    g2 = GradientBoostingRegressor(n_estimators=1, max_depth=2, learning_rate=0.2, random_state=0).fit(Xr, yr)
    same_tree = np.array_equal(g1.estimators_[0, 0].tree_.threshold, g2.estimators_[0, 0].tree_.threshold) and np.allclose(g1.estimators_[0, 0].tree_.value, g2.estimators_[0, 0].tree_.value)
    report("learning_rate: the stage-1 tree is identical for lr=0.1 and lr=0.2 and (predict - init) doubles", same_tree and np.allclose(g2.predict(Xr) - yr.mean(), 2 * (g1.predict(Xr) - yr.mean()), atol=1e-10))
    g = GradientBoostingRegressor(n_estimators=6, max_depth=2, learning_rate=lr, random_state=0).fit(Xr, yr)
    cum = const(g) + lr * np.cumsum([t.predict(Xr) for t in g.estimators_[:, 0]], 0); st = list(g.staged_predict(Xr))
    report("GBR staged_predict[i] = init + lr * cumulative sum of the first i+1 trees; last stage = predict", len(st) == 6 and all(np.allclose(a_, b_, atol=1e-10) for a_, b_ in zip(st, cum)) and np.allclose(st[-1], g.predict(Xr)))
    report("GBR train_score_[i] = mean squared error after stage i on the training data (loss='squared_error', subsample=1)", all(close(g.train_score_[i], float(sum((F(a_) - F(b_)) ** 2 for a_, b_ in zip(fr(yr), fr(st[i]))) / n), 1e-10) for i in range(6)), f"(train_score_[0] {g.train_score_[0]:.6f})")
    g = GradientBoostingRegressor(loss="absolute_error", n_estimators=4, max_depth=2, learning_rate=lr, random_state=0).fit(Xr, yr); st = list(g.staged_predict(Xr))
    report("GBR absolute_error train_score_[i] = mean |y - f_i|", all(close(g.train_score_[i], float(sum(abs(a_ - b_) for a_, b_ in zip(fr(yr), fr(st[i]))) / n), 1e-10) for i in range(4)))
    g = GradientBoostingRegressor(loss="quantile", alpha=a, n_estimators=4, max_depth=2, learning_rate=lr, random_state=0).fit(Xr, yr); st = list(g.staged_predict(Xr))
    report("GBR quantile(0.8) train_score_[i] = mean pinball loss", all(close(g.train_score_[i], float(pinball(yr - st[i], 0, a) / n), 1e-10) for i in range(4)))
    g = GradientBoostingRegressor(loss="huber", alpha=0.9, n_estimators=4, max_depth=2, learning_rate=lr, random_state=0).fit(Xr, yr); st = list(g.staged_predict(Xr))
    prev = [np.full(n, const(g))] + st[:-1]; ok = True
    for i in range(4):
        d = float(q_linear(np.abs(yr - prev[i]), 0.9)); assert q_linear(np.abs(yr - prev[i]), 0.9) == q_lower(np.abs(yr - prev[i]), 0.9)
        ok &= close(g.train_score_[i], float(huber_sum(yr - st[i], d) / n), 1e-10)
    report("GBR huber train_score_[i] = mean Huber loss (1/2 r^2 if |r|<=delta else delta(|r| - delta/2)) with delta = 0.9-quantile of |y - f_{i-1}| (set before fitting stage i)", ok)
    c = GradientBoostingClassifier(n_estimators=4, max_depth=2, learning_rate=lr, random_state=0).fit(Xc, yc); st = list(c.staged_predict_proba(Xc))
    ll = [-(np.log(st[i][np.arange(40), yc])).mean() for i in range(4)]
    report("GBC binary log_loss train_score_[i] = binomial deviance = 2 * mean log loss", all(close(c.train_score_[i], 2 * ll[i], 1e-10) for i in range(4)), f"(train_score_[0] {c.train_score_[0]:.6f}, logloss {ll[0]:.6f})")
    c = GradientBoostingClassifier(n_estimators=4, max_depth=2, learning_rate=lr, random_state=0).fit(Xm, ym); st = list(c.staged_predict_proba(Xm))
    ll = [-(np.log(st[i][np.arange(60), ym])).mean() for i in range(4)]
    f2 = all(close(c.train_score_[i], 2 * ll[i], 1e-10) for i in range(4)); f1 = all(close(c.train_score_[i], ll[i], 1e-10) for i in range(4))
    report("GBC multiclass train_score_[i] = 1 * mean multinomial log loss (NOT the deviance 2*logloss used in the binary case; documented as 'the loss')", f1, f"(matches factor 1: {f1}, factor 2: {f2}; train_score_[0] {c.train_score_[0]:.6f}, logloss {ll[0]:.6f})")
    c = GradientBoostingClassifier(loss="exponential", n_estimators=4, max_depth=2, learning_rate=lr, random_state=0).fit(Xc, yc); st = list(c.staged_decision_function(Xc))
    report("GBC exponential train_score_[i] = mean exp(-(2y-1) * raw_i) (staged_decision_function yields shape (n, 1) as documented)", all(close(c.train_score_[i], np.mean(np.exp(-(2 * yc - 1) * st[i].ravel())), 1e-10) for i in range(4)) and st[0].shape == (40, 1))

    # ---- subsample, oob_improvement_
    n2 = 60; Xr2 = rs.randn(n2, 3); yr2 = Xr2 @ np.array([1.0, -2.0, 0.5]) + rs.randn(n2) * 0.5
    g = GradientBoostingRegressor(n_estimators=8, subsample=0.6, max_depth=2, learning_rate=lr, random_state=7).fit(Xr2, yr2)
    n_inbag = max(1, int(0.6 * n2))
    report("GBR subsample=0.6: every stage's tree is fitted with in-bag weight sum = int(0.6 n) = 36 (root weighted_n_node_samples)", all(close(t.tree_.weighted_n_node_samples[0], n_inbag, 1e-12) for t in g.estimators_[:, 0]))
    u = np.random.RandomState(7).uniform(size=n2); mask0 = np.zeros(n2, bool); bagged = 0
    for i in range(n2):
        if u[i] * (n2 - i) < (n_inbag - bagged): mask0[i] = True; bagged += 1
    t0 = g.estimators_[0, 0]; lg = leaf_groups(t0, Xr2)
    mask_ok = all(close(t0.tree_.weighted_n_node_samples[l], mask0[i].sum(), 1e-12) for l, i in lg.items())
    print(f"   stage-0 in-bag mask replicated from RandomState(7).uniform (first draw of the fit): consistent with the tree's leaf weights: {mask_ok}")
    init_oob = np.mean((yr2[~mask0] - yr2.mean()) ** 2); st = list(g.staged_predict(Xr2)); oob0 = np.mean((yr2[~mask0] - st[0][~mask0]) ** 2)
    report("GBR oob_improvement_[0] = OOB loss (MSE) of the init estimator minus OOB loss after stage 1 ('improvement in loss of the first stage over the init estimator')", mask_ok and close(g.oob_improvement_[0], init_oob - oob0, 1e-8), f"({g.oob_improvement_[0]:.6f} vs {init_oob - oob0:.6f})")
    report("GBR train_score_[0] with subsample = MSE on the in-bag samples only", mask_ok and close(g.train_score_[0], np.mean((yr2[mask0] - st[0][mask0]) ** 2), 1e-8))
    if V >= (1, 3):
        report("GBR oob_scores_ (1.3+): oob_improvement_[i] = oob_scores_[i-1] - oob_scores_[i] for i >= 1, oob_scores_[0] = init OOB loss - oob_improvement_[0], oob_score_ = oob_scores_[-1]", np.allclose(g.oob_improvement_[1:], -np.diff(g.oob_scores_), atol=1e-10) and close(g.oob_scores_[0], oob0, 1e-8) and close(g.oob_score_, g.oob_scores_[-1], 1e-14))
    else:
        report("GBR oob_improvement_ has n_estimators entries (oob_scores_ / oob_score_ only exist from 1.3)", g.oob_improvement_.shape == (8,) and not hasattr(g, "oob_scores_"))
    # ---- early stopping with n_iter_no_change
    n3 = 120; Xr3 = rs.randn(n3, 3); yr3 = Xr3 @ np.array([1.0, -2.0, 0.5]) + rs.randn(n3) * 1.0
    seed = 3; tol = 1e-3; nic = 3
    g = GradientBoostingRegressor(n_estimators=300, n_iter_no_change=nic, validation_fraction=0.2, tol=tol, max_depth=2, learning_rate=0.3, random_state=seed).fit(Xr3, yr3)
    Xtr, Xva, ytr, yva = train_test_split(Xr3, yr3, random_state=np.random.RandomState(seed), test_size=0.2)
    split_ok = close(const(g), ytr.mean(), 1e-12) and all(close(t.tree_.weighted_n_node_samples[0], len(ytr), 1e-12) for t in g.estimators_[:, 0])
    report("GBR n_iter_no_change: validation set = train_test_split(test_size=validation_fraction, random_state=RandomState(seed)) [replicated]; init_ and trees fitted on the remaining ceil-complement 96 samples", split_ok, f"(n_train {len(ytr)}, n_estimators_ {g.n_estimators_})")
    L = [np.mean((yva - p) ** 2) for p in g.staged_predict(Xva)]; stop = None
    for i in range(len(L)):
        hist = L[max(0, i - nic):i]; ref = max(hist) if len(hist) == nic else math.inf
        if not (L[i] + tol < ref): stop = i; break
    report("GBR early stopping rule: stop at the first stage whose validation MSE is not below (max of the previous n_iter_no_change losses) - tol; n_estimators_ = that stage + 1 < n_estimators", g.n_estimators_ < 300 and stop == g.n_estimators_ - 1 and len(g.train_score_) == g.n_estimators_, f"(stop index {stop}, n_estimators_ {g.n_estimators_})")

    # ---- feature_importances_
    g = GradientBoostingRegressor(n_estimators=10, max_depth=3, random_state=0).fit(Xr2, yr2)
    trees = [t for t in g.estimators_[:, 0] if t.tree_.node_count > 1]
    hand = np.mean([importances_by_hand(t, 3, normalize=False) for t in trees], 0); hand /= hand.sum()
    report("GBR feature_importances_ = normalised mean over the trees of the per-tree unnormalised total impurity (MSE) decrease per feature, sums to 1", close(g.feature_importances_.sum(), 1, 1e-12) and np.allclose(g.feature_importances_, hand, atol=1e-12), f"({np.round(g.feature_importances_, 4)})")
    # ---- loss_ attribute history
    print(f"   attribute loss_ present: {hasattr(g, 'loss_')} (deprecated in 1.1, removed in 1.3); n_estimators_ = {g.n_estimators_}")
    # ---- reproducibility
    a1 = GradientBoostingRegressor(n_estimators=10, subsample=0.7, max_features="sqrt", random_state=11).fit(Xr2, yr2).predict(Xr2)
    a2 = GradientBoostingRegressor(n_estimators=10, subsample=0.7, max_features="sqrt", random_state=11).fit(Xr2, yr2).predict(Xr2)
    a3 = GradientBoostingRegressor(n_estimators=10, subsample=0.7, max_features="sqrt", random_state=12).fit(Xr2, yr2).predict(Xr2)
    report("GBR random_state: same int seed -> identical predictions (subsample and max_features randomness); different seed -> different", np.array_equal(a1, a2) and not np.array_equal(a1, a3))

# ================================================================ HistGradientBoosting
def hgb_stump(X, g, h, l2, min_leaf):
    """Best single split by the XGBoost gain G_L^2/(H_L+l2) + G_R^2/(H_R+l2) over all features and all thresholds
    between consecutive distinct values (candidate children need >= min_leaf rows); returns per-sample leaf
    values -G/(H+l2) (or the root value if no split)."""
    n, d = X.shape; best = (-math.inf, None); G, H = g.sum(), h.sum()
    for f in range(d):
        u = np.unique(X[:, f])
        for k in range(len(u) - 1):
            thr = (u[k] + u[k + 1]) / 2; L = X[:, f] <= thr
            if L.sum() < min_leaf or (~L).sum() < min_leaf: continue
            gl, hl = g[L].sum(), h[L].sum(); gr, hr = G - gl, H - hl
            if hl < 1e-3 or hr < 1e-3: continue
            gain = gl ** 2 / (hl + l2) + gr ** 2 / (hr + l2) - G ** 2 / (H + l2)
            if gain > best[0]: best = (gain, (f, thr, -gl / (hl + l2), -gr / (hr + l2)))
    if best[1] is None or best[0] <= 0 or n < 2 * min_leaf: return np.full(n, -G / (H + l2))
    f, thr, vl, vr = best[1]; return np.where(X[:, f] <= thr, vl, vr)

def sec_hgb():
    from sklearn.ensemble._hist_gradient_boosting.binning import _BinMapper
    method = "averaged_inverted_cdf" if V >= (1, 9) else "midpoint"
    # ---- binning thresholds
    x = rs.rand(1000); X1 = x.reshape(-1, 1)
    h = HistGradientBoostingRegressor(max_bins=16, max_iter=1, random_state=0).fit(X1, x)
    thr = h._bin_mapper.bin_thresholds_[0]; pct = np.linspace(0, 100, 17)[1:-1]
    exp = np.unique(np.percentile(x, pct, method=method))
    report(f"HGBT max_bins=16 on 1000 distinct values: bin_thresholds_ = np.percentile(x, linspace(0,100,17)[1:-1], method='{method}') ('quantiles so that each bin contains approximately the same number of samples')", thr.shape == (15,) and np.allclose(thr, exp, rtol=0, atol=1e-12), f"(first thresholds {np.round(thr[:3], 5)})")
    other = "midpoint" if method != "midpoint" else "averaged_inverted_cdf"
    print(f"   matches the other method '{other}': {np.allclose(thr, np.unique(np.percentile(x, pct, method=other)), atol=1e-12)}")
    xs = rs.randint(0, 10, 500).astype(float); h = HistGradientBoostingRegressor(max_bins=16, max_iter=1, random_state=0).fit(xs.reshape(-1, 1), xs)
    report("HGBT feature with 10 distinct values <= max_bins: thresholds = midpoints between consecutive distinct values (9 thresholds)", np.allclose(h._bin_mapper.bin_thresholds_[0], (np.arange(9) + 0.5)))
    bm = _BinMapper(n_bins=17, random_state=0).fit(X1)
    Xt = np.array([[np.nan], [x.min()], [x.max()], [thr[3]], [np.nextafter(thr[3], 1)], [0.5]])
    b = bm.transform(Xt).ravel(); expb = np.searchsorted(thr, Xt[1:].ravel(), side="left")
    report("HGBT binning: NaN goes to its own reserved bin (index max_bins = 16 = n_bins - 1) and x maps to bin i iff thresholds[i-1] < x <= thresholds[i]", b[0] == 16 and bm.missing_values_bin_idx_ == 16 and np.array_equal(b[1:], expb), f"(bins {b.tolist()})")
    thr_nan = _BinMapper(n_bins=17, random_state=0).fit(np.vstack([X1, np.full((50, 1), np.nan)])).bin_thresholds_[0]
    report("HGBT binning: missing values are ignored when computing the thresholds", np.allclose(thr_nan, thr))
    # ---- 200k subsample
    nbig = 250_000; xb = np.random.RandomState(5).rand(nbig); full = np.unique(np.percentile(xb, np.linspace(0, 100, 256)[1:-1], method=method))
    hb = HistGradientBoostingRegressor(max_iter=1, max_depth=1, early_stopping=False, random_state=0).fit(xb.reshape(-1, 1), xb); thb = hb._bin_mapper.bin_thresholds_[0]  # early_stopping off: otherwise the mapper is fitted on the 90 % training split
    rng = np.random.RandomState(0); seed2 = rng.randint(np.iinfo(np.uint32).max, dtype="u8")
    if V >= (1, 9):
        sub = np.random.RandomState(seed2).choice(nbig, 200_000, replace=True)
    else:
        sub = np.random.RandomState(seed2).choice(nbig, 200_000, replace=False)
    rep = np.unique(np.percentile(xb[sub], np.linspace(0, 100, 256)[1:-1], method=method))
    report("HGBT n_samples = 250000 > 200000: thresholds are quantiles of a random 200k subsample (within 0.01 of the full-data quantiles of U(0,1) but not equal to them)", thb.shape == (254,) and np.abs(thb - full).max() < 0.01 and not np.allclose(thb, full), f"(max |diff| {np.abs(thb - full).max():.5f})")
    print(f"   exact replication with RandomState(seed from RandomState(random_state).randint(uint32 max)).choice(n, 200000, {'replace=True' if V >= (1, 9) else 'replace=False'}): {np.allclose(thb, rep)}")
    # ---- categorical
    Xcat = np.column_stack([rs.randint(0, 10, 400).astype(float), rs.randn(400)]); ycat = (Xcat[:, 0] % 3) * 2 + Xcat[:, 1] + rs.randn(400) * 0.1
    hc = HistGradientBoostingRegressor(categorical_features=[0], max_iter=20, max_bins=10, random_state=0).fit(Xcat, ycat)
    Xu = Xcat[:30].copy(); Xu[:, 0] = 42; Xn = Xcat[:30].copy(); Xn[:, 0] = np.nan
    report("HGBR categorical_features (10 categories with max_bins=10 allowed): unknown category at predict time is treated as missing: predict(cat=42) == predict(cat=NaN)", np.allclose(hc.predict(Xu), hc.predict(Xn)))
    Xneg = Xcat[:30].copy(); Xneg[:, 0] = -1
    try:
        pneg = hc.predict(Xneg); print(f"   negative category at predict: {'treated as missing' if np.allclose(pneg, hc.predict(Xn)) else 'NOT equal to the NaN prediction'}")
    except Exception as e: print(f"   negative category at predict raises {type(e).__name__}: {str(e)[:80]}")
    try:
        HistGradientBoostingRegressor(categorical_features=[0], max_iter=2, max_bins=9, random_state=0).fit(Xcat, ycat); raised = False
    except ValueError as e: raised = True; msg = str(e)[:90]
    report("HGBR categorical feature with 10 categories and max_bins=9 raises ValueError (at most max_bins unique categories)", raised, msg if raised else "")
    Xcm = Xcat.copy(); Xcm[::7, 0] = np.nan
    hcm = HistGradientBoostingRegressor(categorical_features=[0], max_iter=20, max_bins=10, random_state=0).fit(Xcm, ycat)
    report("HGBR categorical with missing during training: unknown category == NaN prediction (missing is a proper category)", np.allclose(hcm.predict(Xu), hcm.predict(Xn)))
    # ---- monotonic_cst
    Xm = rs.rand(400, 3); ymn = 2 * Xm[:, 0] - 3 * Xm[:, 1] + np.sin(6 * Xm[:, 2]) + rs.randn(400) * 0.3
    hm = HistGradientBoostingRegressor(monotonic_cst=[1, -1, 0], max_iter=50, random_state=0).fit(Xm, ymn)
    report("HGBR monotonic_cst=[1,-1,0]: predictions are non-decreasing in feature 0 and non-increasing in feature 1 along grids (15 anchors x 25 points)", monotone(hm.predict, Xm, 0, 1, rs) and monotone(hm.predict, Xm, 1, -1, rs))
    hu = HistGradientBoostingRegressor(max_iter=50, random_state=0).fit(Xm, ymn * np.where(Xm[:, 2] > 0.5, -1, 1))
    print(f"   (unconstrained fit on a non-monotone target is monotone in feature 0: {monotone(hu.predict, Xm, 0, 1, rs)})")
    ybin = (ymn > np.median(ymn)).astype(int)
    hmc = HistGradientBoostingClassifier(monotonic_cst=[1, -1, 0], max_iter=50, random_state=0).fit(Xm, ybin)
    report("HGBC binary monotonic_cst: predict_proba[:,1] monotone along the constrained features", monotone(lambda G: hmc.predict_proba(G)[:, 1], Xm, 0, 1, rs) and monotone(lambda G: hmc.predict_proba(G)[:, 1], Xm, 1, -1, rs))
    # ---- interaction_cst
    if V >= (1, 2):
        Xi = rs.rand(500, 2); yi = Xi[:, 0] * Xi[:, 1] + rs.randn(500) * 0.05
        hi = HistGradientBoostingRegressor(interaction_cst=[[0], [1]], max_iter=40, random_state=0).fit(Xi, yi)
        hf = HistGradientBoostingRegressor(max_iter=40, random_state=0).fit(Xi, yi)
        def second_diff(f):
            P = np.array([[0.1, 0.1], [0.1, 0.9], [0.9, 0.1], [0.9, 0.9]]); p = f(P); return p[0] - p[1] - p[2] + p[3]
        report("HGBR interaction_cst=[[0],[1]]: the model is additive f(x0)+g(x1) (second difference f(a,b)-f(a,b')-f(a',b)+f(a',b') = 0), whereas the unconstrained model on y = x0*x1 is not", abs(second_diff(hi.predict)) < 1e-10 and abs(second_diff(hf.predict)) > 0.05, f"(constrained {second_diff(hi.predict):.2e}, free {second_diff(hf.predict):.3f})")
    # ---- early_stopping='auto'
    Xe = rs.randn(10_001, 2); ye = Xe[:, 0] + rs.randn(10_001) * 0.5
    he = HistGradientBoostingRegressor(max_iter=5, random_state=0).fit(Xe, ye); he2 = HistGradientBoostingRegressor(max_iter=5, random_state=0).fit(Xe[:10_000], ye[:10_000])
    report("HGBR early_stopping='auto': enabled iff n_samples > 10000 (do_early_stopping_ True for 10001, False for 10000; train_score_/validation_score_ empty without early stopping)", he.do_early_stopping_ and not he2.do_early_stopping_ and len(he.train_score_) == he.n_iter_ + 1 and len(he.validation_score_) == he.n_iter_ + 1 and len(he2.train_score_) == 0)
    n = 300; Xs = rs.randn(n, 3); ys = Xs @ np.array([1.0, -1.0, 0.5]) + rs.randn(n) * 0.5
    tol = 1e-3; nic = 5
    hs = HistGradientBoostingRegressor(early_stopping=True, validation_fraction=None, scoring="loss", n_iter_no_change=nic, tol=tol, max_iter=300, learning_rate=0.1, random_state=0).fit(Xs, ys)
    st = list(hs.staged_predict(Xs)); scores = [-0.5 * np.mean((ys - ys.mean()) ** 2)] + [-0.5 * np.mean((ys - p) ** 2) for p in st]
    report("HGBR early_stopping with scoring='loss', validation_fraction=None: train_score_[i] = -(half squared error) of the ensemble after i iterations on the training data (index 0 = baseline)", len(hs.train_score_) == hs.n_iter_ + 1 and np.allclose(hs.train_score_, scores, rtol=1e-9, atol=1e-12), f"(train_score_[0] {hs.train_score_[0]:.6f})")
    def should_stop(s):
        if len(s) < nic + 1: return False
        ref = s[-(nic + 1)] + tol; return not any(v > ref for v in s[-nic:])
    stops = [should_stop(scores[:i + 1]) for i in range(len(scores))]
    report("HGBR early-stopping rule: stop after the first iteration where none of the last n_iter_no_change scores beats the (n_iter_no_change+1)-th last + tol; n_iter_ < max_iter", hs.n_iter_ < 300 and stops[-1] and not any(stops[:-1]), f"(n_iter_ {hs.n_iter_})")
    # ---- hand-computed first Newton step for every loss (max_iter=1, learning_rate=1, max_depth=1, min_samples_leaf=1)
    # HGBT stores gradients and hessians as float32 (G_H_DTYPE), so leaf values agree to ~1e-7 relative: tolerance 1e-6.
    nt = 30; Xt = rs.randn(nt, 2); yt = Xt[:, 0] + 0.5 * Xt[:, 1] ** 2 + rs.randn(nt) * 0.3 + 3
    kw = dict(max_iter=1, learning_rate=1.0, max_depth=1, min_samples_leaf=1, random_state=0)
    for l2 in (0.0, 3.5):
        hr = HistGradientBoostingRegressor(l2_regularization=l2, **kw).fit(Xt, yt)
        base = yt.mean(); pred = base + hgb_stump(Xt, base - yt, np.ones(nt), l2, 1)
        report(f"HGBR squared_error, l2_regularization={l2}: predict = mean(y) + leaf value -sum(g)/(sum(h) + l2) of the best-gain stump (g = f - y, h = 1)", np.allclose(hr.predict(Xt), pred, rtol=1e-6, atol=1e-9), f"(leaf values {np.unique(np.round(pred - base, 5)).tolist()})")
    hr = HistGradientBoostingRegressor(l2_regularization=0.0, **dict(kw, min_samples_leaf=6)).fit(Xt, yt)
    base = yt.mean(); pred6 = base + hgb_stump(Xt, base - yt, np.ones(nt), 0.0, 6); pred1 = base + hgb_stump(Xt, base - yt, np.ones(nt), 0.0, 1)
    report("HGBR min_samples_leaf=6: best stump among the splits leaving >= 6 rows on each side", np.allclose(hr.predict(Xt), pred6, rtol=1e-6, atol=1e-9), f"(differs from the unrestricted stump: {not np.allclose(pred6, pred1)})")
    w = rs.uniform(0.5, 3, nt)
    hr = HistGradientBoostingRegressor(l2_regularization=1.0, **kw).fit(Xt, yt, sample_weight=w)
    base = np.average(yt, weights=w); pred = base + hgb_stump(Xt, w * (base - yt), w, 1.0, 1)
    report("HGBR sample_weight: baseline = weighted mean, gradients and hessians multiplied by the weights (l2=1)", np.allclose(hr.predict(Xt), pred, rtol=1e-6, atol=1e-9))
    hr = HistGradientBoostingRegressor(loss="absolute_error", **kw).fit(Xt, yt)
    base = float(q_linear(yt, 0.5)); g = np.where(base > yt, 1.0, -1.0); leaf = hgb_stump(Xt, g, np.ones(nt), 0.0, 1)
    pred = base + np.array([float(q_linear(yt[leaf == v] - base, 0.5)) for v in leaf])
    report("HGBR absolute_error: baseline = median(y); stump on g = sign(f - y), h = 1; leaf value replaced by median(y - f) of the leaf (line search for the non-differentiable loss)", np.allclose(hr.predict(Xt), pred, rtol=1e-6, atol=1e-9))
    qa = 0.7; hr = HistGradientBoostingRegressor(loss="quantile", quantile=qa, **kw).fit(Xt, yt)
    base = float(q_linear(yt, qa)); g = np.where(yt >= base, -qa, 1 - qa); leaf = hgb_stump(Xt, g, np.ones(nt), 0.0, 1)
    pred = base + np.array([float(q_linear(yt[leaf == v] - base, qa)) for v in leaf])
    report("HGBR quantile=0.7: baseline = 0.7-quantile(y) (linear); g = -q if y >= f else 1-q, h = 1; leaf value = 0.7-quantile of the leaf residuals", np.allclose(hr.predict(Xt), pred, rtol=1e-6, atol=1e-9))
    yp = rs.poisson(np.exp(0.5 * Xt[:, 0] + 1)).astype(float)
    hr = HistGradientBoostingRegressor(loss="poisson", l2_regularization=0.5, **kw).fit(Xt, yp)
    mu = yp.mean(); pred = np.exp(np.log(mu) + hgb_stump(Xt, mu - yp, np.full(nt, mu), 0.5, 1))
    report("HGBR poisson (l2=0.5): baseline = log(mean y); g = exp(f) - y, h = exp(f); predict = exp(baseline + leaf)", np.allclose(hr.predict(Xt), pred, rtol=1e-6), f"(max rel diff {np.max(np.abs(hr.predict(Xt) / pred - 1)):.2e}; library leaf values {np.unique(np.round(np.log(hr.predict(Xt)) - np.log(mu), 6)).tolist()}, hand {np.unique(np.round(np.log(pred) - np.log(mu), 6)).tolist()}; sizes {[int((np.isclose(pred, v)).sum()) for v in np.unique(pred)]})")
    if V >= (1, 3):
        yg = np.exp(0.3 * Xt[:, 0] + rs.randn(nt) * 0.3) + 0.5
        hr = HistGradientBoostingRegressor(loss="gamma", l2_regularization=0.5, **kw).fit(Xt, yg)
        mu = yg.mean(); pred = np.exp(np.log(mu) + hgb_stump(Xt, 1 - yg / mu, yg / mu, 0.5, 1))
        report("HGBR gamma (1.3+, l2=0.5): baseline = log(mean y); g = 1 - y exp(-f), h = y exp(-f); predict = exp(baseline + leaf)", np.allclose(hr.predict(Xt), pred, rtol=1e-6))
    yb = (Xt[:, 0] + rs.randn(nt) * 0.5 > 0).astype(int); p = yb.mean()
    hc = HistGradientBoostingClassifier(l2_regularization=0.5, **kw).fit(Xt, yb)
    pred = expit(logit(p) + hgb_stump(Xt, p - yb, np.full(nt, p * (1 - p)), 0.5, 1))
    report("HGBC binary log_loss (l2=0.5): baseline = logit(prior); g = p - y, h = p(1-p); predict_proba = expit(baseline + leaf)", np.allclose(hc.predict_proba(Xt)[:, 1], pred, rtol=1e-6, atol=1e-9))
    y3 = rs.randint(0, 3, nt); X3 = Xt + y3[:, None] * 0.7; pr = np.bincount(y3) / nt
    hc = HistGradientBoostingClassifier(l2_regularization=0.5, **kw).fit(X3, y3)
    raw = np.column_stack([np.log(pr[k]) + hgb_stump(X3, pr[k] - (y3 == k), np.full(nt, pr[k] * (1 - pr[k])), 0.5, 1) for k in range(3)])
    report("HGBC multiclass (K=3, l2=0.5): one stump per class on g_k = p_k - y_k, h_k = p_k(1-p_k); predict_proba = softmax(log prior_k + leaf_k)", np.allclose(hc.predict_proba(X3), softmax(raw), rtol=1e-6, atol=1e-9) and hc.n_trees_per_iteration_ == 3)
    # ---- class_weight, sample_weight equivalences
    if V >= (1, 2):
        a1 = HistGradientBoostingClassifier(class_weight={0: 1.0, 1: 3.0}, max_iter=10, min_samples_leaf=1, random_state=0).fit(Xt, yb).predict_proba(Xt)
        a2 = HistGradientBoostingClassifier(max_iter=10, min_samples_leaf=1, random_state=0).fit(Xt, yb, sample_weight=np.where(yb == 1, 3.0, 1.0)).predict_proba(Xt)
        report("HGBC class_weight={0:1,1:3} (1.2+) == sample_weight 3 for class 1", np.allclose(a1, a2, atol=1e-12))
        cw = nt / (2 * np.bincount(yb))
        a1 = HistGradientBoostingClassifier(class_weight="balanced", max_iter=10, min_samples_leaf=1, random_state=0).fit(Xt, yb).predict_proba(Xt)
        a2 = HistGradientBoostingClassifier(max_iter=10, min_samples_leaf=1, random_state=0).fit(Xt, yb, sample_weight=cw[yb]).predict_proba(Xt)
        report("HGBC class_weight='balanced' == sample_weight n/(K * bincount(y))[y]", np.allclose(a1, a2, atol=1e-12))
    Xd = rs.randint(0, 30, (80, 2)).astype(float); yd = Xd[:, 0] - Xd[:, 1] + rs.randn(80)
    a1 = HistGradientBoostingRegressor(max_iter=10, min_samples_leaf=1, random_state=0).fit(np.vstack([Xd, Xd]), np.concatenate([yd, yd])).predict(Xd)
    a2 = HistGradientBoostingRegressor(max_iter=10, min_samples_leaf=1, random_state=0).fit(Xd, yd, sample_weight=np.full(80, 2.0)).predict(Xd)
    report("HGBR duplicated rows == sample_weight=2 when min_samples_leaf=1 and n_distinct <= max_bins (documented equivalence; binning ignores weights)", np.allclose(a1, a2, atol=1e-10))
    mf = {"max_features": 0.5} if V >= (1, 4) else {}
    a1 = HistGradientBoostingRegressor(max_iter=20, random_state=3, **mf).fit(Xs, ys).predict(Xs)
    a2 = HistGradientBoostingRegressor(max_iter=20, random_state=3, **mf).fit(Xs, ys).predict(Xs)
    report("HGBR random_state: identical predictions for the same seed", np.array_equal(a1, a2))

# ================================================================ AdaBoost
def sec_ada():
    n = 60; ym = rs.randint(0, 3, n); Xm = rs.randn(n, 3) + ym[:, None] * 0.8; K = 3; lr = 0.7
    ab = AdaBoostClassifier(**est_kw(DecisionTreeClassifier(max_depth=1)), n_estimators=6, learning_rate=lr, random_state=0, **ada_kw()).fit(Xm, ym)
    w = np.ones(n) / n; ok_w = ok_e = ok_t = True; alphas = []
    for i, est in enumerate(ab.estimators_):
        t2 = DecisionTreeClassifier(max_depth=1, random_state=est.random_state).fit(Xm, ym, sample_weight=w)
        ok_t &= t2.tree_.feature[0] == est.tree_.feature[0] and close(t2.tree_.threshold[0], est.tree_.threshold[0], 1e-12)
        inc = est.predict(Xm) != ym; err = float(sum(F(float(x)) for x, m in zip(w, inc) if m) / sum(fr(w)))
        alpha = lr * (math.log((1 - err) / err) + math.log(K - 1)); alphas.append(alpha)
        ok_e &= close(ab.estimator_errors_[i], err, 1e-10); ok_w &= close(ab.estimator_weights_[i], alpha, 1e-10)
        w = w * np.exp(alpha * inc); w = w / w.sum()
    report("AdaBoostClassifier SAMME: stump i is the tree fitted with the current sample weights w_i (same feature and threshold on refit)", ok_t)
    report("AdaBoost SAMME: estimator_errors_[i] = weighted error rate under w_i", ok_e, f"({np.round(ab.estimator_errors_, 4).tolist()})")
    report("AdaBoost SAMME: estimator_weights_[i] = learning_rate * (log((1-err)/err) + log(K-1)); w_{i+1} = w_i * exp(alpha_i * 1[misclassified]) renormalised", ok_w, f"({np.round(ab.estimator_weights_, 4).tolist()})")
    P = np.array([est.predict(Xm) for est in ab.estimators_]); aw = ab.estimator_weights_
    sym = V >= (1, 3)   # 1.3 changelog (PR 26521): SAMME scores made symmetric (sum over classes = 0); before: plain weighted votes
    def dec(m):
        d = np.zeros((n, K))
        for i in range(m):
            d += aw[i] * np.where(P[i][:, None] == ab.classes_[None, :], 1.0, -1.0 / (K - 1) if sym else 0.0)
        return d / aw[:m].sum()
    report("AdaBoost decision_function = sum_i alpha_i (1[h_i=c] - 1/(K-1) 1[h_i!=c]) / sum alpha (1.3+, symmetric scores; before 1.3: sum_i alpha_i 1[h_i=c] / sum alpha)", np.allclose(ab.decision_function(Xm), dec(6), atol=1e-12))
    report("AdaBoost staged_decision_function[m] = the same with the first m+1 estimators", all(np.allclose(s, dec(m + 1), atol=1e-12) for m, s in enumerate(ab.staged_decision_function(Xm))))
    report("AdaBoost predict_proba = softmax(decision / (K-1)) (Zhu et al. eq. 15); predict = classes_[argmax decision]", np.allclose(ab.predict_proba(Xm), softmax(dec(6) / (K - 1)), atol=1e-12) and np.all(ab.predict(Xm) == ab.classes_[dec(6).argmax(1)]))
    yb = (ym > 0).astype(int)
    ab2 = AdaBoostClassifier(**est_kw(DecisionTreeClassifier(max_depth=1)), n_estimators=5, learning_rate=lr, random_state=0, **ada_kw()).fit(Xm, yb)
    P2 = np.array([est.predict(Xm) for est in ab2.estimators_]); d2 = sum(a_ * np.where(p == ab2.classes_[1], 1.0, -1.0) for a_, p in zip(ab2.estimator_weights_, P2)) / ab2.estimator_weights_.sum()
    dfun = ab2.decision_function(Xm); fac = 2 if sym else 1
    report(f"AdaBoost binary: decision_function = {fac} * sum alpha_i * (+1 if h_i = classes_[1] else -1) / sum alpha (difference of the two class scores: factor 2 from 1.3, 1 before; shape (n,)); predict_proba = softmax([-d, d]/2); alpha = lr*log((1-err)/err) (log(K-1)=0)", np.allclose(dfun, fac * d2, atol=1e-12) and np.allclose(ab2.predict_proba(Xm), softmax(np.column_stack([-dfun, dfun]) / 2), atol=1e-12) and close(ab2.estimator_weights_[0], lr * math.log((1 - ab2.estimator_errors_[0]) / ab2.estimator_errors_[0]), 1e-12))
    unanimous = np.all(P2 == P2[0], axis=0)
    report("AdaBoost binary decision_function docstring: 'values closer to -1 or 1 mean more like the first or second class' -> a unanimous ensemble gives |decision| = 1", unanimous.any() and np.allclose(np.abs(dfun[unanimous]), 1.0), f"(unanimous samples {int(unanimous.sum())}, their |decision| = {np.unique(np.round(np.abs(dfun[unanimous]), 6)).tolist()})")
    if V < (1, 6):
        d = AdaBoostClassifier(**est_kw(DecisionTreeClassifier(max_depth=1)), n_estimators=3, random_state=0)
        d.fit(Xm, ym)
        report("AdaBoostClassifier algorithm history: default algorithm is 'SAMME.R' before 1.6 (deprecated in 1.4), whose estimator_weights_ are all 1", d.algorithm == "SAMME.R" and np.all(d.estimator_weights_ == 1.0), f"(default algorithm {d.algorithm!r})")
    else:
        print(f"   AdaBoostClassifier algorithm history: {sklearn.__version__}: SAMME.R removed (1.6); 'algorithm' parameter accepted: {'algorithm' in AdaBoostClassifier().get_params()}")
    # ---- AdaBoost.R2
    n2 = 80; Xr = rs.randn(n2, 3); yr = Xr @ np.array([1.0, -2.0, 0.5]) + rs.randn(n2) * 0.5; lr = 0.8
    for loss in ("linear", "square", "exponential"):
        ar = AdaBoostRegressor(**est_kw(DecisionTreeRegressor(max_depth=3)), n_estimators=6, learning_rate=lr, loss=loss, random_state=0).fit(Xr, yr)
        w = np.ones(n2) / n2; ok = True
        for i, est in enumerate(ar.estimators_):
            e = np.abs(est.predict(Xr) - yr); e = e / e.max()
            if loss == "square": e = e ** 2
            elif loss == "exponential": e = 1 - np.exp(-e)
            err = float((w * e).sum()); beta = err / (1 - err); alpha = lr * math.log(1 / beta)
            ok &= close(ar.estimator_errors_[i], err, 1e-10) and close(ar.estimator_weights_[i], alpha, 1e-10)
            w = w * beta ** ((1 - e) * lr); w = w / w.sum()
        report(f"AdaBoostRegressor loss='{loss}': error_i = sum w |e|/max|e| ({loss}), beta = err/(1-err), estimator_weights_ = lr*log(1/beta), w *= beta^((1-loss)*lr) (Drucker 1997)", ok and len(ar.estimators_) == 6, f"(weights {np.round(ar.estimator_weights_, 3).tolist()})")
        P = np.array([est.predict(Xr) for est in ar.estimators_]).T; aw = ar.estimator_weights_; med = np.zeros(n2)
        for i in range(n2):
            o = np.argsort(P[i]); c = np.cumsum(aw[o]); j = np.nonzero(c >= 0.5 * c[-1])[0][0]; med[i] = P[i, o[j]]
        report(f"AdaBoostRegressor ({loss}) predict = weighted median of the estimators' predictions (smallest prediction whose cumulative weight >= half the total)", np.allclose(ar.predict(Xr), med, atol=1e-12))
    a1 = AdaBoostRegressor(**est_kw(DecisionTreeRegressor(max_depth=3)), n_estimators=4, random_state=5).fit(Xr, yr).predict(Xr)
    a2 = AdaBoostRegressor(**est_kw(DecisionTreeRegressor(max_depth=3)), n_estimators=4, random_state=5).fit(Xr, yr).predict(Xr)
    report("AdaBoostRegressor random_state: same seed -> identical (bootstrap draws)", np.array_equal(a1, a2))

# ================================================================ Bagging
def sec_bagging():
    n = 60; ym = rs.randint(0, 3, n); Xm = rs.randn(n, 4) + ym[:, None] * 0.8
    bc = BaggingClassifier(**est_kw(DecisionTreeClassifier(random_state=0)), n_estimators=15, max_samples=0.7, max_features=0.8, oob_score=True, random_state=0).fit(Xm, ym)
    S = bc.estimators_samples_; Fe = bc.estimators_features_
    report("BaggingClassifier max_samples=0.7 (float): each sample draw has int(0.7 * 60) = 42 indices with replacement (duplicates present)", all(len(s) == 42 for s in S) and all(len(set(s.tolist())) < 42 for s in S), f"(distinct per draw {[len(set(s.tolist())) for s in S[:5]]})")
    report("BaggingClassifier max_features=0.8 (float): int(0.8 * 4) = 3 distinct features per estimator (bootstrap_features=False)", all(len(f) == 3 and len(set(f.tolist())) == 3 for f in Fe))
    ok = True
    for est, s, f in zip(bc.estimators_, S, Fe):
        cnt = collections.Counter(est.apply(Xm[s][:, f]).tolist())
        ok &= all(close(est.tree_.weighted_n_node_samples[l], c, 1e-12) for l, c in cnt.items()) and close(est.tree_.weighted_n_node_samples[0], 42, 1e-12)
    report("Bagging: every base tree was fitted on exactly its drawn rows and features (leaf weighted counts = multiplicities of the drawn indices)", ok)
    oob = np.zeros((n, 3))
    for est, s, f in zip(bc.estimators_, S, Fe):
        m = np.ones(n, bool); m[s] = False; oob[m] += est.predict_proba(Xm[m][:, f])
    cnt = oob.sum(1); cnt[cnt == 0] = 1; oobn = oob / cnt[:, None]
    report("Bagging oob_decision_function_ = normalised sum of predict_proba over the estimators for which the sample was not drawn; oob_score_ = accuracy of its argmax", np.allclose(bc.oob_decision_function_, oobn, atol=1e-12) and close(bc.oob_score_, np.mean(bc.classes_[oobn.argmax(1)] == ym), 1e-12), f"(oob_score_ {bc.oob_score_:.4f})")
    pp = np.mean([est.predict_proba(Xm[:, f]) for est, f in zip(bc.estimators_, Fe)], 0)
    report("Bagging predict_proba = mean of the estimators' predict_proba; predict = classes_[argmax]", np.allclose(bc.predict_proba(Xm), pp, atol=1e-12) and np.all(bc.predict(Xm) == bc.classes_[pp.argmax(1)]))
    bn = BaggingClassifier(**est_kw(DecisionTreeClassifier()), n_estimators=8, max_samples=25, bootstrap=False, random_state=0).fit(Xm, ym)
    report("Bagging bootstrap=False, max_samples=25 (int): 25 distinct indices per estimator (subsampling without replacement)", all(len(s) == 25 and len(set(s.tolist())) == 25 for s in bn.estimators_samples_))
    Xr = rs.randn(n, 4); yr = Xr @ np.array([1.0, -2.0, 0.5, 0]) + rs.randn(n) * 0.5
    br = BaggingRegressor(**est_kw(DecisionTreeRegressor()), n_estimators=15, oob_score=True, random_state=0).fit(Xr, yr)
    S = br.estimators_samples_; pred = np.zeros(n); cnt = np.zeros(n)
    for est, s, f in zip(br.estimators_, S, br.estimators_features_):
        m = np.ones(n, bool); m[s] = False; pred[m] += est.predict(Xr[m][:, f]); cnt[m] += 1
    cnt[cnt == 0] = 1; pred /= cnt
    report("BaggingRegressor max_samples=None: n draws with replacement; oob_prediction_ = mean OOB prediction; oob_score_ = R^2(y, oob_prediction_)", all(len(s) == n for s in S) and np.allclose(br.oob_prediction_, pred, atol=1e-12) and close(br.oob_score_, float(r2_exact(yr, br.oob_prediction_)), 1e-12))
    report("BaggingRegressor predict = mean of the estimators' predictions", np.allclose(br.predict(Xr), np.mean([e.predict(Xr[:, f]) for e, f in zip(br.estimators_, br.estimators_features_)], 0), atol=1e-12))
    a1 = BaggingRegressor(n_estimators=5, random_state=9).fit(Xr, yr).predict(Xr); a2 = BaggingRegressor(n_estimators=5, random_state=9).fit(Xr, yr).predict(Xr); a3 = BaggingRegressor(n_estimators=5, random_state=10).fit(Xr, yr).predict(Xr)
    report("Bagging random_state: same seed identical, different seed differs", np.array_equal(a1, a2) and not np.array_equal(a1, a3))

# ================================================================ Voting
def sec_voting():
    n = 30; y = np.array([0, 1, 2] * 10); X = rs.randn(n, 2)
    def const(c): return DummyClassifier(strategy="constant", constant=c)
    v = VotingClassifier([("a", const(2)), ("b", const(1))], voting="hard").fit(X, y)
    report("VotingClassifier hard, tie 2 vs 1 -> the class first in ascending sort order (1) [user guide]", np.all(v.predict(X) == 1))
    v = VotingClassifier([("a", const(2)), ("b", const(1))], voting="hard", weights=[2, 1]).fit(X, y)
    report("VotingClassifier hard with weights [2, 1]: weighted vote 2 vs 1 -> class 2", np.all(v.predict(X) == 2))
    v = VotingClassifier([("a", const(2)), ("b", const(1)), ("c", const(2))], voting="hard").fit(X, y)
    report("VotingClassifier hard majority 2,1,2 -> 2", np.all(v.predict(X) == 2))
    v = VotingClassifier([("a", const(2)), ("b", const(0)), ("c", const(1))], voting="hard", weights=[1, 1, 1.5]).fit(X, y)
    report("VotingClassifier hard weights [1,1,1.5]: 2 (1) vs 0 (1) vs 1 (1.5) -> 1", np.all(v.predict(X) == 1))
    Xs = rs.randn(90, 3) + np.repeat([0, 1, 2], 30)[:, None]; ys = np.repeat([0, 1, 2], 30)
    ests = [("lr", LogisticRegression(max_iter=500)), ("nb", GaussianNB()), ("dt", DecisionTreeClassifier(max_depth=3, random_state=0))]
    v = VotingClassifier(ests, voting="soft", weights=[1, 2, 3]).fit(Xs, ys)
    P = np.array([clone(e).fit(Xs, ys).predict_proba(Xs) for _, e in ests]); avg = np.tensordot([1, 2, 3], P, 1) / 6
    report("VotingClassifier soft: predict_proba = weighted average of the estimators' predict_proba; predict = argmax", np.allclose(v.predict_proba(Xs), avg, atol=1e-12) and np.all(v.predict(Xs) == v.classes_[avg.argmax(1)]))
    yr = Xs @ np.array([1.0, 2.0, -1.0]) + rs.randn(90)
    regs = [("lr", LinearRegression()), ("dt", DecisionTreeRegressor(max_depth=3, random_state=0)), ("d", DummyRegressor())]
    vr = VotingRegressor(regs, weights=[1, 3, 2]).fit(Xs, yr)
    P = np.array([clone(e).fit(Xs, yr).predict(Xs) for _, e in regs]); avg = np.tensordot([1, 3, 2], P, 1) / 6
    report("VotingRegressor predict = weighted mean of the estimators' predictions; transform = the stacked predictions", np.allclose(vr.predict(Xs), avg, atol=1e-10) and np.allclose(vr.transform(Xs), P.T, atol=1e-12))

# ================================================================ Stacking
def sec_stacking():
    n = 100; Xc = rs.randn(n, 3); yc = (Xc[:, 0] + 0.5 * Xc[:, 1] + rs.randn(n) * 0.6 > 0).astype(int)
    ests = [("lr", LogisticRegression(max_iter=1000)), ("dt", DecisionTreeClassifier(max_depth=3, random_state=0))]
    sc = StackingClassifier(estimators=ests).fit(Xc, yc)
    report("StackingClassifier defaults: final_estimator_ = LogisticRegression(), stack_method_ = ['predict_proba', 'predict_proba'], cv = 5 folds", isinstance(sc.final_estimator_, LogisticRegression) and list(sc.stack_method_) == ["predict_proba", "predict_proba"])
    meta = np.column_stack([cross_val_predict(clone(e), Xc, yc, cv=StratifiedKFold(5), method="predict_proba")[:, 1] for _, e in ests])
    fe = LogisticRegression().fit(meta, yc)
    report("StackingClassifier binary: final estimator fitted on cross_val_predict(StratifiedKFold(5, shuffle=False), predict_proba) with the first probability column dropped (refit reproduces coef_/intercept_)", np.allclose(sc.final_estimator_.coef_, fe.coef_, rtol=1e-6, atol=1e-8) and np.allclose(sc.final_estimator_.intercept_, fe.intercept_, rtol=1e-6, atol=1e-8), f"(coef {np.round(sc.final_estimator_.coef_.ravel(), 4)} vs {np.round(fe.coef_.ravel(), 4)})")
    T = sc.transform(Xc)
    report("StackingClassifier transform(X) = column_stack of the refitted estimators' predict_proba[:, 1] (shape (n, 2)); predict_proba = final_estimator_.predict_proba(transform(X))", T.shape == (n, 2) and np.allclose(T, np.column_stack([clone(e).fit(Xc, yc).predict_proba(Xc)[:, 1] for _, e in ests]), atol=1e-8) and np.allclose(sc.predict_proba(Xc), sc.final_estimator_.predict_proba(T), atol=1e-12))
    sp_ = StackingClassifier(estimators=ests, passthrough=True).fit(Xc, yc); Tp = sp_.transform(Xc)
    report("StackingClassifier passthrough=True: transform = [predictions, X] (shape (n, 2 + 3))", Tp.shape == (n, 5) and np.allclose(Tp[:, 2:], Xc) and np.allclose(Tp[:, :2], T, atol=1e-8))
    ym = rs.randint(0, 3, n); Xm = Xc + ym[:, None] * 0.7
    sm = StackingClassifier(estimators=ests).fit(Xm, ym)
    report("StackingClassifier multiclass (K=3): all K probability columns kept -> transform shape (n, 2*3)", sm.transform(Xm).shape == (n, 6))
    sd = StackingClassifier(estimators=ests, stack_method="predict").fit(Xc, yc)
    report("StackingClassifier stack_method='predict': one label column per estimator", sd.transform(Xc).shape == (n, 2) and set(np.unique(sd.transform(Xc))) <= {0.0, 1.0})
    yr = Xc @ np.array([1.0, -2.0, 0.5]) + rs.randn(n) * 0.5
    regs = [("lr", LinearRegression()), ("dt", DecisionTreeRegressor(max_depth=3, random_state=0))]
    sr = StackingRegressor(estimators=regs).fit(Xc, yr)
    meta = np.column_stack([cross_val_predict(clone(e), Xc, yr, cv=KFold(5), method="predict") for _, e in regs]); fr_ = RidgeCV().fit(meta, yr)
    report("StackingRegressor defaults: final_estimator_ = RidgeCV() fitted on cross_val_predict(KFold(5, shuffle=False), predict) features (coef_, intercept_, alpha_ reproduced)", isinstance(sr.final_estimator_, RidgeCV) and np.allclose(sr.final_estimator_.coef_, fr_.coef_, rtol=1e-8) and close(sr.final_estimator_.intercept_, fr_.intercept_, 1e-8) and close(sr.final_estimator_.alpha_, fr_.alpha_, 1e-12), f"(coef {np.round(sr.final_estimator_.coef_, 4)}, alpha_ {sr.final_estimator_.alpha_})")
    report("StackingRegressor estimators_ are refitted on the full data; predict = final_estimator_.predict(transform(X))", np.allclose(sr.transform(Xc), np.column_stack([clone(e).fit(Xc, yr).predict(Xc) for _, e in regs]), atol=1e-10) and np.allclose(sr.predict(Xc), sr.final_estimator_.predict(sr.transform(Xc)), atol=1e-12))

# ================================================================ IsolationForest
def c_apl(m):
    if m <= 1: return 0.0
    if m == 2: return 1.0
    return 2 * (math.log(m - 1) + np.euler_gamma) - 2 * (m - 1) / m
def path_lengths(tree, X):
    t = tree.tree_; out = np.zeros(len(X)); leaf_n = np.zeros(len(X), int)
    for i, x in enumerate(X):
        node = 0; d = 0
        while t.children_left[node] != -1:
            node = t.children_left[node] if x[t.feature[node]] <= t.threshold[node] else t.children_right[node]; d += 1
        out[i] = d + c_apl(int(t.n_node_samples[node])); leaf_n[i] = t.n_node_samples[node]
    return out, leaf_n
def sec_iforest():
    Xo = np.vstack([rs.randn(300, 2), rs.uniform(-6, 6, (20, 2))]); n = len(Xo)
    iso = IsolationForest(n_estimators=30, random_state=0).fit(Xo)
    report("IsolationForest max_samples='auto' -> max_samples_ = min(256, n) = 256 for n = 320; = n for n = 100", iso.max_samples_ == 256 and IsolationForest(n_estimators=2, random_state=0).fit(Xo[:100]).max_samples_ == 100)
    report("each isolation tree is built on max_samples_ = 256 rows drawn without replacement (root n_node_samples = 256, bootstrap=False) with max_depth = ceil(log2(256)) = 8", all(t.tree_.n_node_samples[0] == 256 for t in iso.estimators_) and all(t.get_depth() <= 8 for t in iso.estimators_))
    H = []; big_leaves = 0
    for t, f in zip(iso.estimators_, iso.estimators_features_):
        h, ln = path_lengths(t, Xo[:, f]); H.append(h); big_leaves += int((ln > 2).sum())
    Hbar = np.mean(H, 0); s = -2.0 ** (-Hbar / c_apl(256))
    report("IsolationForest score_samples = -2^(-E[h(x)] / c(256)), h = leaf depth + c(n_leaf) with c(m) = 2(ln(m-1) + euler_gamma) - 2(m-1)/m (c(2)=1, c(1)=0), averaged over the trees", np.allclose(iso.score_samples(Xo), s, rtol=1e-10, atol=1e-12), f"(unsplit leaves with > 2 samples hit: {big_leaves} of {30 * n} sample-tree pairs)")
    report("IsolationForest contamination='auto': offset_ = -0.5 and decision_function = score_samples - offset_", iso.offset_ == -0.5 and np.allclose(iso.decision_function(Xo), iso.score_samples(Xo) + 0.5, atol=1e-12))
    report("IsolationForest predict = -1 iff decision_function < 0 else +1", np.all(iso.predict(Xo) == np.where(iso.decision_function(Xo) < 0, -1, 1)))
    ic = IsolationForest(n_estimators=30, contamination=0.1, random_state=0).fit(Xo); sc = ic.score_samples(Xo)
    report("IsolationForest contamination=0.1: offset_ = 10th percentile (linear) of the training score_samples; fraction of training outliers ~ 0.1", close(ic.offset_, float(q_linear(sc, 0.1)), 1e-12) and abs(np.mean(ic.predict(Xo) == -1) - 0.1) <= 1 / n, f"(offset_ {ic.offset_:.5f}, outlier fraction {np.mean(ic.predict(Xo) == -1):.4f})")
    im = IsolationForest(n_estimators=10, max_samples=64, random_state=0).fit(Xo)
    hh = np.mean([path_lengths(t, Xo[:, f])[0] for t, f in zip(im.estimators_, im.estimators_features_)], 0)
    report("IsolationForest max_samples=64 (int): trees on 64 rows, normalisation c(64)", im.max_samples_ == 64 and all(t.tree_.n_node_samples[0] == 64 for t in im.estimators_) and np.allclose(im.score_samples(Xo), -2.0 ** (-hh / c_apl(64)), rtol=1e-10))
    a1 = IsolationForest(n_estimators=10, random_state=4).fit(Xo).score_samples(Xo); a2 = IsolationForest(n_estimators=10, random_state=4).fit(Xo).score_samples(Xo)
    report("IsolationForest random_state: same seed identical scores", np.array_equal(a1, a2))

# ================================================================ RandomTreesEmbedding
def sec_rte():
    n = 80; X = rs.randn(n, 3)
    rte = RandomTreesEmbedding(n_estimators=5, max_depth=3, random_state=0).fit(X); T = rte.transform(X)
    n_leaves = [int((t.tree_.children_left == -1).sum()) for t in rte.estimators_]
    A = rte.apply(X); H = np.zeros((n, sum(n_leaves))); off = 0
    for k in range(5):
        ids = np.sort(np.unique(A[:, k])); H[np.arange(n), off + np.searchsorted(ids, A[:, k])] = 1; off += len(ids)
    report("RandomTreesEmbedding transform: sparse CSR (n, n_estimators * leaves) one-hot of the leaf index per tree (exactly one 1 per tree per row; every leaf has a training sample)", sp.issparse(T) and T.format == "csr" and T.shape == (n, sum(n_leaves)) and np.array_equal(T.toarray(), H), f"(leaves per tree {n_leaves}, shape {T.shape})")
    Td = RandomTreesEmbedding(n_estimators=5, max_depth=3, sparse_output=False, random_state=0).fit_transform(X)
    report("RandomTreesEmbedding sparse_output=False: dense ndarray equal to the sparse one", isinstance(Td, np.ndarray) and np.array_equal(Td, H))
    report("RandomTreesEmbedding trees are totally random regression trees on max_depth=3 (each tree <= 8 leaves) fitted without bootstrap (root n_node_samples = n)", all(l <= 8 for l in n_leaves) and all(t.tree_.n_node_samples[0] == n for t in rte.estimators_))

# ================================================================ RandomForest / ExtraTrees
def forest_samples(forest, n, n_boot):
    if V >= (1, 4): return list(forest.estimators_samples_), "estimators_samples_"
    return [np.random.RandomState(t.random_state).randint(0, n, n_boot) for t in forest.estimators_], "RandomState(tree.random_state).randint(0, n, n_boot)"
def sec_forest():
    n = 120; X = rs.randn(n, 4); y = (X[:, 0] * X[:, 1] + X[:, 2] + rs.randn(n) * 0.3 > 0).astype(int)
    rf = RandomForestClassifier(n_estimators=25, oob_score=True, min_samples_leaf=3, random_state=0).fit(X, y)
    S, src = forest_samples(rf, n, n)
    ok = all(len(s) == n for s in S)
    for t, s in zip(rf.estimators_, S):
        cnt = collections.Counter(t.apply(X[s]).tolist()); ok &= all(close(t.tree_.weighted_n_node_samples[l], c, 1e-12) for l, c in cnt.items()) and close(t.tree_.weighted_n_node_samples[0], n, 1e-12)
    report(f"RF bootstrap: n draws with replacement per tree, passed as per-row counts (leaf weighted_n_node_samples = multiplicities of the drawn indices; indices from {src})", ok, f"(root n_node_samples {rf.estimators_[0].tree_.n_node_samples[0]} = {'distinct drawn rows' if rf.estimators_[0].tree_.n_node_samples[0] == len(set(S[0].tolist())) else 'n'})")
    oob = np.zeros((n, 2)); cnt = np.zeros(n)
    for t, s in zip(rf.estimators_, S):
        m = np.ones(n, bool); m[s] = False; oob[m] += t.predict_proba(X[m]); cnt[m] += 1
    cnt[cnt == 0] = 1; oob /= cnt[:, None]
    report("RF oob_decision_function_ = mean predict_proba over the trees whose bootstrap sample excluded the row; oob_score_ = accuracy of its argmax", np.allclose(rf.oob_decision_function_, oob, atol=1e-12) and close(rf.oob_score_, np.mean(rf.classes_[oob.argmax(1)] == y), 1e-12), f"(oob_score_ {rf.oob_score_:.4f})")
    pp = np.mean([t.predict_proba(X) for t in rf.estimators_], 0); votes = np.array([np.bincount([t.predict(X)[i] for t in rf.estimators_], minlength=2).argmax() for i in range(n)])
    report("RF predict = classes_[argmax(mean of the trees' predict_proba)] (soft vote as documented, not the majority vote)", np.all(rf.predict(X) == rf.classes_[pp.argmax(1)]) and np.allclose(rf.predict_proba(X), pp, atol=1e-12), f"(majority vote disagrees with the mean-probability rule on {int((votes != pp.argmax(1)).sum())} of {n} samples)")
    imp_trees = [t.feature_importances_ for t in rf.estimators_ if t.tree_.node_count > 1]
    hand0 = importances_by_hand(rf.estimators_[0], 4, normalize=True)
    report("RF feature_importances_ = mean of the trees' normalised impurity importances (each = total weighted Gini decrease per feature / root weight, normalised), sums to 1", np.allclose(rf.feature_importances_, np.mean(imp_trees, 0), atol=1e-12) and close(rf.feature_importances_.sum(), 1, 1e-12) and np.allclose(hand0, rf.estimators_[0].feature_importances_, atol=1e-12))
    for ms, expv in ((0.3, {int(0.3 * n), round(0.3 * n)}), (50, {50})):
        r = RandomForestClassifier(n_estimators=5, max_samples=ms, random_state=0).fit(X, y)
        report(f"RF max_samples={ms}: each tree's bootstrap has {sorted(expv)} rows (root weighted_n_node_samples)", all(t.tree_.weighted_n_node_samples[0] in expv for t in r.estimators_), f"({r.estimators_[0].tree_.weighted_n_node_samples[0]})")
    r = RandomForestClassifier(n_estimators=5, max_samples=0.35, random_state=0).fit(X[:105], y[:105])
    print(f"   max_samples=0.35 on 105 rows (36.75): root weight {r.estimators_[0].tree_.weighted_n_node_samples[0]:.0f} (int -> 36, round -> 37; {'int' if V >= (1, 9) else 'round'} expected for this version)")
    report("RF max_samples float on 105 rows: int(...) from 1.9, round(...) before", close(r.estimators_[0].tree_.weighted_n_node_samples[0], 36 if V >= (1, 9) else 37, 1e-12))
    rb = RandomForestClassifier(n_estimators=10, class_weight="balanced_subsample", random_state=0).fit(X, y)
    S, _ = forest_samples(rb, n, n); ok = True
    for t, s in zip(rb.estimators_, S):
        cb = np.bincount(y[s], minlength=2); w = n / (2 * cb); leafw = collections.defaultdict(float)
        for l, yi in zip(t.apply(X[s]), y[s]): leafw[int(l)] += w[yi]
        ok &= all(close(t.tree_.weighted_n_node_samples[l], v, 1e-10) for l, v in leafw.items())
    report("RF class_weight='balanced_subsample': per-tree weights n_boot/(K * class counts of the bootstrap sample) (leaf weights = sum of w_c over the drawn rows)", ok)
    rb2 = RandomForestClassifier(n_estimators=10, class_weight="balanced", random_state=0).fit(X, y)
    S, _ = forest_samples(rb2, n, n); ok = True; w = n / (2 * np.bincount(y))
    if V >= (1, 9):
        # 1.9 changelog: forests "now use sample_weight to draw the samples instead of forwarding them ... to the
        # underlying estimators"; class_weight is folded into that sampling weight (_forest.py: _sample_weight).
        p = w[y] / w[y].sum(); ok_draw = all(np.array_equal(s, np.random.RandomState(t.random_state).choice(n, n, replace=True, p=p)) for t, s in zip(rb2.estimators_, S))
        for t, s in zip(rb2.estimators_, S):
            cnt = collections.Counter(t.apply(X[s]).tolist()); ok &= all(close(t.tree_.weighted_n_node_samples[l], c, 1e-12) for l, c in cnt.items())
        report("RF class_weight='balanced' (1.9+): realised by drawing the bootstrap with probability proportional to n/(K * class counts of the full y) (RandomState(tree.random_state).choice(n, n, p=w/sum) replicated); the trees then see plain multiplicities", ok and ok_draw, f"(class-1 fraction in the draws {np.mean([y[s].mean() for s in S]):.3f} vs {y.mean():.3f} in y)")
    else:
        for t, s in zip(rb2.estimators_, S):
            leafw = collections.defaultdict(float)
            for l, yi in zip(t.apply(X[s]), y[s]): leafw[int(l)] += w[yi]
            ok &= all(close(t.tree_.weighted_n_node_samples[l], v, 1e-10) for l, v in leafw.items())
        report("RF class_weight='balanced' (< 1.9): tree weights = n/(K * class counts of the full y) times the bootstrap multiplicities", ok)
    mid = 0.02; r0 = RandomForestClassifier(n_estimators=10, random_state=0).fit(X, y); r1 = RandomForestClassifier(n_estimators=10, min_impurity_decrease=mid, random_state=0).fit(X, y)
    ok = True; ndec = []
    for t in r1.estimators_:
        tr = t.tree_; N = tr.weighted_n_node_samples[0]
        for node in range(tr.node_count):
            l, rr = tr.children_left[node], tr.children_right[node]
            if l == -1: continue
            Nt, Nl, Nr = tr.weighted_n_node_samples[node], tr.weighted_n_node_samples[l], tr.weighted_n_node_samples[rr]
            dec = Nt / N * (tr.impurity[node] - Nr / Nt * tr.impurity[rr] - Nl / Nt * tr.impurity[l]); ndec.append(dec); ok &= dec >= mid - 1e-12
    report("RF min_impurity_decrease=0.02: every split satisfies N_t/N * (imp - N_tR/N_t imp_R - N_tL/N_t imp_L) >= 0.02 and the trees are smaller", ok and sum(t.tree_.node_count for t in r1.estimators_) < sum(t.tree_.node_count for t in r0.estimators_), f"(min decrease {min(ndec):.4f}; nodes {sum(t.tree_.node_count for t in r1.estimators_)} vs {sum(t.tree_.node_count for t in r0.estimators_)})")
    yr = 2 * X[:, 0] - 3 * X[:, 1] + np.sin(3 * X[:, 2]) + rs.randn(n) * 0.3
    if V >= (1, 4):
        rm = RandomForestRegressor(n_estimators=20, monotonic_cst=[1, -1, 0, 0], random_state=0).fit(X, yr)
        report("RF monotonic_cst=[1,-1,0,0] (1.4+): predictions monotone along the constrained features", monotone(rm.predict, X, 0, 1, rs) and monotone(rm.predict, X, 1, -1, rs))
    rr_ = RandomForestRegressor(n_estimators=20, oob_score=True, random_state=0).fit(X, yr)
    S, _ = forest_samples(rr_, n, n); pred = np.zeros(n); cnt = np.zeros(n)
    for t, s in zip(rr_.estimators_, S):
        m = np.ones(n, bool); m[s] = False; pred[m] += t.predict(X[m]); cnt[m] += 1
    cnt[cnt == 0] = 1; pred /= cnt
    report("RF regressor: predict = mean of the trees; oob_prediction_ = mean OOB prediction; oob_score_ = R^2", np.allclose(rr_.predict(X), np.mean([t.predict(X) for t in rr_.estimators_], 0), atol=1e-12) and np.allclose(rr_.oob_prediction_, pred, atol=1e-12) and close(rr_.oob_score_, float(r2_exact(yr, rr_.oob_prediction_)), 1e-12))
    rw = RandomForestRegressor(n_estimators=5, warm_start=True, random_state=0).fit(X, yr); first = [t.tree_.threshold.copy() for t in rw.estimators_]; p5 = rw.predict(X)
    rw.set_params(n_estimators=8).fit(X, yr)
    report("RF warm_start: refit with n_estimators 5 -> 8 keeps the first 5 trees unchanged and adds 3", len(rw.estimators_) == 8 and all(np.array_equal(a, t.tree_.threshold) for a, t in zip(first, rw.estimators_[:5])) and not np.allclose(rw.predict(X), p5))
    a1 = RandomForestRegressor(n_estimators=5, random_state=2).fit(X, yr).predict(X); a2 = RandomForestRegressor(n_estimators=5, random_state=2).fit(X, yr).predict(X); a3 = RandomForestRegressor(n_estimators=5, random_state=3).fit(X, yr).predict(X)
    report("RF random_state: same seed identical, different seed differs", np.array_equal(a1, a2) and not np.array_equal(a1, a3))
    # ---- ExtraTrees
    et = ExtraTreesClassifier(n_estimators=10, random_state=0).fit(X, y)
    ok = all(t.tree_.n_node_samples[0] == n and close(t.tree_.weighted_n_node_samples[0], n, 1e-12) for t in et.estimators_)
    report("ExtraTrees default bootstrap=False: every tree uses the whole sample (root count n, weight n)", ok)
    ok = True
    for t in et.estimators_[:5]:
        tr = t.tree_; path = t.decision_path(X).toarray().astype(bool)
        for node in range(tr.node_count):
            if tr.children_left[node] == -1: continue
            v = X[path[:, node], tr.feature[node]]; ok &= v.min() <= tr.threshold[node] <= v.max()
    report("ExtraTrees: each split threshold lies within [min, max] of the feature over the node's samples (random threshold)", ok)
    etr = ExtraTreesRegressor(n_estimators=10, bootstrap=True, oob_score=True, random_state=0).fit(X, yr)
    S, _ = forest_samples(etr, n, n); pred = np.zeros(n); cnt = np.zeros(n)
    for t, s in zip(etr.estimators_, S):
        m = np.ones(n, bool); m[s] = False; pred[m] += t.predict(X[m]); cnt[m] += 1
    cnt[cnt == 0] = 1; pred /= cnt
    report("ExtraTreesRegressor bootstrap=True, oob_score: oob_prediction_ recomputed from the unsampled rows; oob_score_ = R^2", np.allclose(etr.oob_prediction_, pred, atol=1e-12) and close(etr.oob_score_, float(r2_exact(yr, etr.oob_prediction_)), 1e-12))
    report("ExtraTrees feature_importances_ = mean of the trees' importances, sums to 1", np.allclose(et.feature_importances_, np.mean([t.feature_importances_ for t in et.estimators_], 0), atol=1e-12) and close(et.feature_importances_.sum(), 1, 1e-12))
    a1 = ExtraTreesRegressor(n_estimators=5, random_state=2).fit(X, yr).predict(X); a2 = ExtraTreesRegressor(n_estimators=5, random_state=2).fit(X, yr).predict(X)
    report("ExtraTrees random_state: same seed identical", np.array_equal(a1, a2))

for name, fn in (("GradientBoosting", sec_gb), ("HistGradientBoosting", sec_hgb), ("AdaBoost", sec_ada), ("Bagging", sec_bagging),
                 ("Voting", sec_voting), ("Stacking", sec_stacking), ("IsolationForest", sec_iforest), ("RandomTreesEmbedding", sec_rte),
                 ("Forests", sec_forest)):
    section(name, fn)
