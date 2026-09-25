#!/usr/bin/env python
"""Naive Bayes (Gaussian / Multinomial / Complement / Bernoulli / Categorical),
decision trees (split selection, impurities, pruning path, importances, criteria,
missing values, monotonic constraints, best-first), dummy estimators, one-vs-rest /
one-vs-one / output-code, multi-output and chains, label propagation / spreading and
self-training -- every check against an independent recomputation (Fraction, mpmath,
a plain-Python reference implementation or a documented invariant)."""
import sys, math, warnings, itertools, inspect
sys.path.insert(0, ".")
from _synth import *
import mpmath
from mpmath import mp, mpf
mp.dps = 40
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB, CategoricalNB
from sklearn.tree import (DecisionTreeClassifier, DecisionTreeRegressor, ExtraTreeClassifier,
                          ExtraTreeRegressor, export_text)
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier, OutputCodeClassifier
from sklearn.multioutput import MultiOutputClassifier, MultiOutputRegressor, ClassifierChain, RegressorChain
from sklearn.semi_supervised import LabelPropagation, LabelSpreading, SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.exceptions import ConvergenceWarning
banner(); warnings.filterwarnings("ignore")
V = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
rs = np.random.RandomState(7)

def lse(vals):
    m = max(vals); return m + mpmath.log(sum(mpmath.exp(v - m) for v in vals))

def softmax_rows(J):
    out = []
    for row in J:
        z = lse(row); out.append([float(mpmath.exp(v - z)) for v in row])
    return np.array(out)

def logrows(J):
    out = []
    for row in J:
        z = lse(row); out.append([float(v - z) for v in row])
    return np.array(out)

def allclose(a, b, rel=1e-9, abs_=1e-12):
    a = np.asarray(a, float); b = np.asarray(b, float)
    if a.shape != b.shape: return False
    return np.all(np.abs(a - b) <= abs_ + rel * np.maximum(np.abs(a), np.abs(b)))

def nb_kw(**kw):
    """force_alpha only exists from 1.2 on (default False until 1.4)."""
    if V < (1, 2): kw.pop("force_alpha", None)
    return kw

# =============================================================================
print("== naive_bayes: GaussianNB")
Xg = np.array([[1, 2], [2, 3], [3, 3], [5, 1], [6, 3], [7, 2], [9, 8], [4, 4]], float)
yg = np.array([0, 0, 0, 1, 1, 1, 1, 0])
def fr_stats(X, y, w=None):
    """theta (weighted mean), var (weighted population variance) per class, exact."""
    w = [F(1)] * len(y) if w is None else [F(v) for v in w]
    out = {}
    for c in sorted(set(y)):
        idx = [i for i in range(len(y)) if y[i] == c]; W = sum(w[i] for i in idx)
        th = [sum(w[i] * F(X[i, j]) for i in idx) / W for j in range(X.shape[1])]
        va = [sum(w[i] * (F(X[i, j]) - th[j]) ** 2 for i in idx) / W for j in range(X.shape[1])]
        out[c] = (th, va, W)
    return out
def fr_eps(X, vs):
    n = X.shape[0]; cols = []
    for j in range(X.shape[1]):
        m = sum(F(v) for v in X[:, j]) / n; cols.append(sum((F(v) - m) ** 2 for v in X[:, j]) / n)
    return F(vs) * max(cols)
st = fr_stats(Xg, yg); eps = fr_eps(Xg, "1e-9")
g = GaussianNB().fit(Xg, yg)
print(f"   theta_ {g.theta_.tolist()}  var_ {g.var_.tolist()}  epsilon_ {g.epsilon_:.3e} (exact {float(eps):.3e})  class_prior_ {g.class_prior_.tolist()}")
report("GaussianNB theta_ = per-class mean (exact)", allclose(g.theta_, [[float(v) for v in st[c][0]] for c in (0, 1)]))
report("GaussianNB epsilon_ = var_smoothing * max_j var(X[:, j]) (population variance)", close(g.epsilon_, float(eps), 1e-12))
report("GaussianNB var_ = per-class population variance + epsilon_ (exact)", allclose(g.var_, [[float(v + eps) for v in st[c][1]] for c in (0, 1)]))
report("GaussianNB class_prior_ = class counts / n (exact 4/8, 4/8)", allclose(g.class_prior_, [0.5, 0.5]))
def gnb_jll(X, st, eps, prior):
    J = []
    for x in X:
        row = []
        for c in sorted(st):
            th, va, _ = st[c]; s = mpmath.log(mpf(prior[c]))
            for j in range(len(th)):
                v = mpf(va[j].numerator) / va[j].denominator + mpf(eps.numerator) / eps.denominator
                s += -mpf(1) / 2 * mpmath.log(2 * mpmath.pi * v) - mpf(1) / 2 * (mpf(float(x[j])) - mpf(th[j].numerator) / th[j].denominator) ** 2 / v
            row.append(s)
        J.append(row)
    return J
Xq = np.array([[2.5, 2.0], [5.5, 2.5], [9.0, 8.0], [0.0, 0.0], [100.0, -50.0]])
J = gnb_jll(Xq, st, eps, {0: F(1, 2), 1: F(1, 2)})
P = g.predict_proba(Xq); LP = g.predict_log_proba(Xq)
print(f"   predict_proba {P[:, 1].tolist()}\n   exact         {softmax_rows(J)[:, 1].tolist()}")
report("GaussianNB predict_proba = softmax of exact Gaussian log-likelihood + log prior (rel 1e-9)", allclose(P, softmax_rows(J), 1e-9, 1e-300))
report("GaussianNB predict_log_proba = exact log posterior (abs 1e-9, incl. a far-away point with log p ~ -1e4)", np.all(np.abs(LP - logrows(J)) <= 1e-9 * (1 + np.abs(logrows(J)))), f"(max abs diff {np.max(np.abs(LP - logrows(J))):.2e})")
report("GaussianNB predict = argmax of exact posterior", np.array_equal(g.predict(Xq), np.argmax(logrows(J), 1)))
gp = GaussianNB(priors=[0.3, 0.7]).fit(Xg, yg)
Jp = gnb_jll(Xq, st, eps, {0: F(3, 10), 1: F(7, 10)})
report("GaussianNB(priors=[0.3,0.7]): class_prior_ is the given prior and theta_/var_ unchanged", allclose(gp.class_prior_, [0.3, 0.7]) and allclose(gp.theta_, g.theta_) and allclose(gp.var_, g.var_))
report("GaussianNB(priors): predict_proba uses the given prior (exact)", allclose(gp.predict_proba(Xq), softmax_rows(Jp), 1e-9, 1e-300))
try:
    GaussianNB(priors=[0.3, 0.6]).fit(Xg, yg); report("GaussianNB(priors not summing to 1) raises ValueError", False)
except ValueError: report("GaussianNB(priors not summing to 1) raises ValueError", True)
# sample_weight: exact weighted statistics; and equal to repeating rows
wg = np.array([1, 2, 1, 3, 1, 1, 2, 1])
gw = GaussianNB().fit(Xg, yg, sample_weight=wg); stw = fr_stats(Xg, yg, wg)
report("GaussianNB(sample_weight): theta_ = weighted mean, var_ = weighted population variance + epsilon_, class_count_ = sum of weights (exact)",
       allclose(gw.theta_, [[float(v) for v in stw[c][0]] for c in (0, 1)]) and allclose(gw.var_, [[float(v + eps) for v in stw[c][1]] for c in (0, 1)]) and allclose(gw.class_count_, [float(stw[c][2]) for c in (0, 1)]) and allclose(gw.class_prior_, [float(stw[c][2] / 12) for c in (0, 1)]))
grep_ = GaussianNB().fit(np.repeat(Xg, wg, axis=0), np.repeat(yg, wg))
report("GaussianNB(sample_weight=integer w) equals fitting on rows repeated w times (theta_, var_, class_prior_)", allclose(gw.theta_, grep_.theta_) and allclose(gw.var_, grep_.var_) and allclose(gw.class_prior_, grep_.class_prior_))
# partial_fit == fit
gpf = GaussianNB().partial_fit(Xg[:4], yg[:4], classes=[0, 1]).partial_fit(Xg[4:], yg[4:])
d = max(np.max(np.abs(gpf.theta_ - g.theta_)), np.max(np.abs(gpf.var_ - g.var_)))
print(f"   partial_fit(2 chunks) vs fit: max |theta_/var_ diff| {d:.2e}; epsilon_ {gpf.epsilon_:.3e} vs fit {g.epsilon_:.3e}")
report("GaussianNB partial_fit over two chunks equals fit (theta_, var_ within 1e-7 rel, class_count_, class_prior_) at the default var_smoothing", allclose(gpf.theta_, g.theta_, 1e-7) and allclose(gpf.var_, g.var_, 1e-7) and allclose(gpf.class_count_, g.class_count_) and allclose(gpf.class_prior_, g.class_prior_))
g5 = GaussianNB(var_smoothing=0.5).fit(Xg, yg)
g5p = GaussianNB(var_smoothing=0.5).partial_fit(Xg[:4], yg[:4], classes=[0, 1]).partial_fit(Xg[4:], yg[4:])
st5 = fr_stats(Xg, yg); eps5 = fr_eps(Xg, "0.5")
print(f"   var_smoothing=0.5: fit var_ {g5.var_.tolist()}; partial_fit var_ {g5p.var_.tolist()}; exact class-var + 0.5*max var {[[float(v + eps5) for v in st5[c][1]] for c in (0, 1)]}; fit epsilon_ {g5.epsilon_}, partial_fit epsilon_ {g5p.epsilon_}")
report("GaussianNB(var_smoothing=0.5) fit: var_ = class variance + var_smoothing*max var(X) (exact)", allclose(g5.var_, [[float(v + eps5) for v in st5[c][1]] for c in (0, 1)]))
report("GaussianNB(var_smoothing=0.5) partial_fit over two chunks: var_ equals the fit result on the same data (docs: epsilon_ is 'absolute additive value to variances')", allclose(g5p.var_, g5.var_, 1e-9), f"(max rel diff {np.max(np.abs(g5p.var_ / g5.var_ - 1)):.2e})")
g1 = GaussianNB().fit(np.array([[1.0, 5.0], [2.0, 9.0]]), [0, 1])
report("GaussianNB with one sample per class: var_ == epsilon_ exactly (zero variance plus smoothing)", np.all(g1.var_ == g1.epsilon_))
g32 = GaussianNB().fit(Xg.astype(np.float32), yg)
report("GaussianNB float32 input: predict_proba within 1e-5 of the exact float64 posterior", allclose(g32.predict_proba(Xq.astype(np.float32)), softmax_rows(J), 1e-5, 1e-6), f"(dtype of theta_ {g32.theta_.dtype})")
Xoff = Xg + 1e6; goff = GaussianNB().fit(Xoff, yg)
report("GaussianNB with offset 1e6 added to X: var_ within 1e-6 relative of the offset-free var_ (two-pass variance)", allclose(goff.var_, g.var_, 1e-6), f"(max rel diff {np.max(np.abs(goff.var_ / g.var_ - 1)):.2e})")

# =============================================================================
print("== naive_bayes: MultinomialNB / ComplementNB / BernoulliNB / CategoricalNB")
Xc = np.array([[2, 1, 0, 0], [1, 1, 0, 1], [0, 0, 3, 1], [0, 1, 2, 2], [1, 0, 0, 4], [0, 0, 1, 5], [3, 0, 0, 0]])
yc = np.array([0, 0, 1, 1, 2, 2, 0])
classes = [0, 1, 2]; nf = Xc.shape[1]
def counts(X, y, w=None):
    w = [1] * len(y) if w is None else list(w)
    fc = {c: [sum(F(w[i]) * int(X[i, j]) for i in range(len(y)) if y[i] == c) for j in range(X.shape[1])] for c in classes}
    cc = {c: sum(F(w[i]) for i in range(len(y)) if y[i] == c) for c in classes}
    return fc, cc
fc, cc = counts(Xc, yc)
def mnb_flp(fc, alpha):
    a = [F(alpha)] * nf if np.isscalar(alpha) else [F(x) for x in alpha]
    return [[float(mpmath.log(mpf((fc[c][j] + a[j]).numerator) / (fc[c][j] + a[j]).denominator) - mpmath.log(mpf(sum(fc[c][k] + a[k] for k in range(nf)).numerator) / sum(fc[c][k] + a[k] for k in range(nf)).denominator)) for j in range(nf)] for c in classes]
m = MultinomialNB(alpha=1.0).fit(Xc, yc)
print(f"   feature_count_ {m.feature_count_.tolist()} class_count_ {m.class_count_.tolist()}")
report("MultinomialNB feature_count_ / class_count_ are the summed counts", allclose(m.feature_count_, [[float(v) for v in fc[c]] for c in classes]) and allclose(m.class_count_, [3, 2, 2]))
report("MultinomialNB feature_log_prob_ = log((N_cj + alpha) / (N_c + alpha*n_features)), alpha=1 (rel 1e-12)", allclose(m.feature_log_prob_, mnb_flp(fc, 1), 1e-12))
report("MultinomialNB class_log_prior_ = log(class_count_/n) (fit_prior=True)", allclose(m.class_log_prior_, [math.log(3 / 7), math.log(2 / 7), math.log(2 / 7)], 1e-12))
report("MultinomialNB(fit_prior=False): class_log_prior_ = log(1/n_classes) uniform", allclose(MultinomialNB(fit_prior=False).fit(Xc, yc).class_log_prior_, [math.log(1 / 3)] * 3, 1e-12))
report("MultinomialNB(class_prior=[.2,.3,.5]): class_log_prior_ = log(class_prior)", allclose(MultinomialNB(class_prior=[0.2, 0.3, 0.5]).fit(Xc, yc).class_log_prior_, np.log([0.2, 0.3, 0.5]), 1e-12))
ma = MultinomialNB(alpha=[0.5, 1, 2, 0.1]).fit(Xc, yc)
report("MultinomialNB(alpha per feature array): feature_log_prob_ uses alpha_j in numerator and sum_j alpha_j in denominator", allclose(ma.feature_log_prob_, mnb_flp(fc, [0.5, 1, 2, 0.1]), 1e-12))
Xt = np.array([[1, 0, 0, 0], [0, 0, 2, 1], [0, 0, 0, 3], [5, 5, 5, 5], [0, 0, 0, 0]])
def disc_jll(X, flp, clp):
    return [[mpf(clp[ci]) + sum(mpf(int(x[j])) * mpf(flp[ci][j]) for j in range(nf)) for ci in range(len(classes))] for x in X]
Jm = disc_jll(Xt, mnb_flp(fc, 1), [math.log(3 / 7), math.log(2 / 7), math.log(2 / 7)])
report("MultinomialNB predict_log_proba = X.feature_log_prob_.T + class_log_prior_ minus logsumexp (rel 1e-9)", allclose(m.predict_log_proba(Xt), logrows(Jm), 1e-9, 1e-12))
report("MultinomialNB predict_proba = softmax of the joint log likelihood (rel 1e-9)", allclose(m.predict_proba(Xt), softmax_rows(Jm), 1e-9, 1e-300))
report("MultinomialNB all-zero row: predict_proba = class prior", allclose(m.predict_proba(Xt)[-1], [3 / 7, 2 / 7, 2 / 7], 1e-12))
if V >= (1, 2):
    m0 = MultinomialNB(alpha=0, force_alpha=True).fit(Xc, yc)
    exp0 = np.array([[math.log(float(fc[c][j] / sum(fc[c]))) if fc[c][j] > 0 else -np.inf for j in range(nf)] for c in classes])
    report("MultinomialNB(alpha=0, force_alpha=True): 'no smoothing' -> feature_log_prob_ = log(N_cj/N_c) with -inf for unseen features", np.array_equal(np.isinf(m0.feature_log_prob_), np.isinf(exp0)) and allclose(m0.feature_log_prob_[np.isfinite(exp0)], exp0[np.isfinite(exp0)], 1e-12))
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always"); mf = MultinomialNB(alpha=1e-12, force_alpha=False).fit(Xc, yc)
    report("MultinomialNB(alpha=1e-12, force_alpha=False): alpha is set to 1e-10 (documented) with a warning", allclose(mf.feature_log_prob_, mnb_flp(fc, "1e-10"), 1e-9) and any("alpha" in str(w.message) for w in wl))
else:
    with warnings.catch_warnings(record=True) as wl:
        warnings.simplefilter("always"); mf = MultinomialNB(alpha=1e-12).fit(Xc, yc)
    report("MultinomialNB(alpha=1e-12) on <1.2: alpha is clipped to 1e-10 with a warning", allclose(mf.feature_log_prob_, mnb_flp(fc, "1e-10"), 1e-9) and any("alpha" in str(w.message) for w in wl))
wc = np.array([1, 2, 1, 1, 3, 1, 2]); fcw, ccw = counts(Xc, yc, wc)
mw = MultinomialNB().fit(Xc, yc, sample_weight=wc)
report("MultinomialNB(sample_weight): feature_count_ = sum w*x, class_count_ = sum w, class_log_prior_ from weighted counts (exact)", allclose(mw.feature_count_, [[float(v) for v in fcw[c]] for c in classes]) and allclose(mw.class_count_, [float(ccw[c]) for c in classes]) and allclose(mw.class_log_prior_, [math.log(float(ccw[c] / sum(ccw.values()))) for c in classes], 1e-12))
mpf_ = MultinomialNB().partial_fit(Xc[:3], yc[:3], classes=classes).partial_fit(Xc[3:], yc[3:])
report("MultinomialNB partial_fit over two chunks equals fit (feature_log_prob_, class_log_prior_)", allclose(mpf_.feature_log_prob_, m.feature_log_prob_, 1e-12) and allclose(mpf_.class_log_prior_, m.class_log_prior_, 1e-12))
try:
    MultinomialNB().fit(np.array([[1, -1], [2, 3]]), [0, 1]); report("MultinomialNB rejects negative counts (ValueError)", False)
except ValueError: report("MultinomialNB rejects negative counts (ValueError)", True)

# ComplementNB
fa = [sum(fc[c][j] for c in classes) for j in range(nf)]
def cnb_flp(alpha, norm):
    out = []
    for c in classes:
        comp = [fa[j] + F(alpha) - fc[c][j] for j in range(nf)]; tot = sum(comp)
        logged = [float(mpmath.log(mpf((comp[j] / tot).numerator) / (comp[j] / tot).denominator)) for j in range(nf)]
        out.append([l / sum(logged) for l in logged] if norm else [-l for l in logged])
    return out
for norm in (False, True):
    cn = ComplementNB(alpha=1.0, norm=norm).fit(Xc, yc)
    print(f"   ComplementNB(norm={norm}) feature_all_ {cn.feature_all_.tolist()} feature_log_prob_[0] {np.round(cn.feature_log_prob_[0], 6).tolist()}")
    report(f"ComplementNB(norm={norm}) feature_all_ = per-feature totals and feature_log_prob_ = {'log(comp/sum) / sum(log(comp/sum))' if norm else '-log((N_j + alpha - N_cj)/sum)'} (rel 1e-12)", allclose(cn.feature_all_, [float(v) for v in fa]) and allclose(cn.feature_log_prob_, cnb_flp(1, norm), 1e-12))
    Jc = [[sum(mpf(int(x[j])) * mpf(cnb_flp(1, norm)[ci][j]) for j in range(nf)) for ci in range(3)] for x in Xt]
    report(f"ComplementNB(norm={norm}) predict = argmax(X . feature_log_prob_.T) with no class prior (3 classes) and predict_proba = softmax of it", np.array_equal(cn.predict(Xt), np.argmax(np.array(Jc, float), 1)) and allclose(cn.predict_proba(Xt), softmax_rows(Jc), 1e-9, 1e-300))

# BernoulliNB
Xb = np.array([[0.9, 0.0, 0.2, 1.0], [1.0, 0.0, 0.0, 0.6], [0.0, 1.0, 0.7, 0.0], [0.0, 1.0, 1.0, 0.0], [0.4, 0.0, 1.0, 1.0], [1.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
yb = np.array([0, 0, 1, 1, 0, 1, 0]); bcl = [0, 1]
def bnb_ref(Xbin, y, alpha):
    fcb = {c: [sum(int(Xbin[i, j]) for i in range(len(y)) if y[i] == c) for j in range(nf)] for c in bcl}
    ccb = {c: sum(1 for i in range(len(y)) if y[i] == c) for c in bcl}
    p = {c: [F(fcb[c][j] + alpha, ccb[c] + 2 * alpha) for j in range(nf)] for c in bcl}
    flp = [[float(mpmath.log(mpf(p[c][j].numerator) / p[c][j].denominator)) for j in range(nf)] for c in bcl]
    return fcb, ccb, p, flp
for thr in (0.0, 0.5):
    Xbin = (Xb > thr).astype(int); fcb, ccb, pb, flpb = bnb_ref(Xbin, yb, 1)
    b = BernoulliNB(alpha=1.0, binarize=thr).fit(Xb, yb)
    report(f"BernoulliNB(binarize={thr}): feature_count_ counts x > {thr} and feature_log_prob_ = log((N_cj+alpha)/(N_c+2alpha)) (rel 1e-12)", allclose(b.feature_count_, [fcb[c] for c in bcl]) and allclose(b.feature_log_prob_, flpb, 1e-12))
    Xtb = np.array([[1.0, 0.0, 0.0, 0.7], [0.0, 1.0, 1.0, 0.0], [0.3, 0.3, 0.3, 0.3], [1, 1, 1, 1]]); Xtbin = (Xtb > thr).astype(int)
    Jb = [[mpmath.log(mpf(ccb[c]) / len(yb)) + sum(mpmath.log(mpf(pb[c][j].numerator) / pb[c][j].denominator) if Xtbin[i, j] else mpmath.log(1 - mpf(pb[c][j].numerator) / pb[c][j].denominator) for j in range(nf)) for c in bcl] for i in range(len(Xtb))]
    report(f"BernoulliNB(binarize={thr}) predict_log_proba = sum_j [x_j log p_cj + (1-x_j) log(1-p_cj)] + log prior, normalised (absent features penalised; rel 1e-9)", allclose(b.predict_log_proba(Xtb), logrows(Jb), 1e-9, 1e-12))
bn = BernoulliNB(binarize=None).fit(Xb, yb)
fcn = [[sum(Xb[i, j] for i in range(len(yb)) if yb[i] == c) for j in range(nf)] for c in bcl]
report("BernoulliNB(binarize=None): X is used as-is (feature_count_ = sum of the fractional values)", allclose(bn.feature_count_, fcn, 1e-12))
Jbn = [[mpmath.log(mpf(ccb[c]) / len(yb)) + sum(mpf(float(Xtb[i, j])) * mpf(bn.feature_log_prob_[ci][j]) + (1 - mpf(float(Xtb[i, j]))) * mpmath.log(1 - mpmath.exp(mpf(bn.feature_log_prob_[ci][j]))) for j in range(nf)) for ci, c in enumerate(bcl)] for i in range(len(Xtb))]
report("BernoulliNB(binarize=None) with fractional x: jll = x log p + (1-x) log(1-p) using its own feature_log_prob_ (documented formula, rel 1e-9)", allclose(bn.predict_log_proba(Xtb), logrows(Jbn), 1e-9, 1e-12))

# CategoricalNB
Xk = np.array([[0, 1], [1, 0], [2, 1], [0, 2], [1, 1], [2, 2], [0, 0], [2, 0]])
yk = np.array([0, 0, 0, 1, 1, 1, 1, 0]); kcl = [0, 1]
def cat_ref(X, y, alpha, ncat):
    flp = []; cnt = []
    for j in range(X.shape[1]):
        cc_ = [[sum(1 for i in range(len(y)) if y[i] == c and X[i, j] == k) for k in range(ncat[j])] for c in kcl]
        cnt.append(cc_)
        flp.append([[float(mpmath.log(mpf(cc_[ci][k] + alpha) / (sum(cc_[ci]) + alpha * ncat[j]))) for k in range(ncat[j])] for ci, c in enumerate(kcl)])
    return cnt, flp
k = CategoricalNB(alpha=1.0).fit(Xk, yk); cnt, flp = cat_ref(Xk, yk, 1, [3, 3])
report("CategoricalNB n_categories_ = max+1 per feature and category_count_ = per (class, category) counts", np.array_equal(k.n_categories_, [3, 3]) and all(np.array_equal(k.category_count_[j], cnt[j]) for j in range(2)))
report("CategoricalNB feature_log_prob_[i] = log((N_tic + alpha)/(N_c + alpha*n_categories_i)) (rel 1e-12)", all(allclose(k.feature_log_prob_[j], flp[j], 1e-12) for j in range(2)))
Xkt = np.array([[0, 0], [2, 2], [1, 2], [0, 1]])
Jk = [[mpmath.log(mpf(sum(1 for t in yk if t == c)) / len(yk)) + sum(mpf(flp[j][ci][Xkt[i, j]]) for j in range(2)) for ci, c in enumerate(kcl)] for i in range(len(Xkt))]
report("CategoricalNB predict_log_proba = sum_i log P(x_i | y) + log prior, normalised (rel 1e-9)", allclose(k.predict_log_proba(Xkt), logrows(Jk), 1e-9, 1e-12))
k5 = CategoricalNB(alpha=0.5, min_categories=[5, 3]).fit(Xk, yk); cnt5, flp5 = cat_ref(Xk, yk, 0.5, [5, 3])
report("CategoricalNB(min_categories=[5,3], alpha=0.5): feature 0 gets 5 categories (2 unseen) and the smoothing denominator N_c + 0.5*5", np.array_equal(k5.n_categories_, [5, 3]) and k5.feature_log_prob_[0].shape == (2, 5) and all(allclose(k5.feature_log_prob_[j], flp5[j], 1e-12) for j in range(2)))
ki = CategoricalNB(min_categories=4).fit(Xk, yk)
report("CategoricalNB(min_categories=4 scalar): applied to every feature", np.array_equal(ki.n_categories_, [4, 4]))
kpf = CategoricalNB().partial_fit(Xk[:4], yk[:4], classes=kcl).partial_fit(Xk[4:], yk[4:])
report("CategoricalNB partial_fit over two chunks equals fit (feature_log_prob_)", all(allclose(kpf.feature_log_prob_[j], k.feature_log_prob_[j], 1e-12) for j in range(2)))
try:
    k.predict(np.array([[3, 0]])); report("CategoricalNB predict with an unseen category index (3 >= n_categories_) raises IndexError", False)
except IndexError: report("CategoricalNB predict with an unseen category index (3 >= n_categories_) raises IndexError", True)

# =============================================================================
print("== tree: reference implementation")
EPS_T = 1e-7  # sklearn FEATURE_THRESHOLD
def w_imp_cls(idx, y, w, crit, ncls):
    W = sum(w[i] for i in idx); cts = [sum(w[i] for i in idx if y[i] == c) for c in range(ncls)]
    if crit == "gini": return 1.0 - sum((c / W) ** 2 for c in cts)
    return -sum((c / W) * math.log2(c / W) for c in cts if c > 0)
def wmedian(vals, ws):
    order = sorted(range(len(vals)), key=lambda i: vals[i]); tot = sum(ws); half = tot / 2; cum = 0.0
    for r, i in enumerate(order):
        cum += ws[i]
        if cum > half: return vals[i]
        if cum == half: return (vals[i] + vals[order[r + 1]]) / 2
def w_imp_reg(idx, y, w, crit):
    W = sum(w[i] for i in idx); ys = [y[i] for i in idx]; ws = [w[i] for i in idx]
    if crit == "squared_error":
        mu = sum(a * b for a, b in zip(ys, ws)) / W; return sum(b * (a - mu) ** 2 for a, b in zip(ys, ws)) / W
    if crit == "absolute_error":
        med = wmedian(ys, ws); return sum(b * abs(a - med) for a, b in zip(ys, ws)) / W
    if crit == "poisson":
        mu = sum(a * b for a, b in zip(ys, ws)) / W
        if mu <= 0: return float("inf")
        return sum(b * (a * math.log(a / mu) if a > 0 else 0.0) for a, b in zip(ys, ws)) / W
def node_value(idx, y, w, task, ncls, crit):
    W = sum(w[i] for i in idx)
    if task == "cls": return [sum(w[i] for i in idx if y[i] == c) / W for c in range(ncls)]
    if crit == "absolute_error": return [wmedian([y[i] for i in idx], [w[i] for i in idx])]
    return [sum(w[i] * y[i] for i in idx) / W]
def best_splits(idx, X, y, w, task, crit, ncls, Wtot, msl=1, mwl=0.0, features=None):
    """All (feature, threshold, missing_go_to_left) achieving the maximal weighted impurity decrease
    N_t/N * (imp - N_L/N_t imp_L - N_R/N_t imp_R); thresholds are midpoints of adjacent values;
    NaN feature values are tried on both sides plus 'missing alone right' (threshold = inf)."""
    imp = (w_imp_cls(idx, y, w, crit, ncls) if task == "cls" else w_imp_reg(idx, y, w, crit))
    Wt = sum(w[i] for i in idx); best = -1.0; cands = []
    for f in (range(X.shape[1]) if features is None else features):
        miss = [i for i in idx if np.isnan(X[i, f])]; nonm = sorted([i for i in idx if not np.isnan(X[i, f])], key=lambda i: X[i, f])
        if not nonm: continue
        if X[nonm[-1], f] <= X[nonm[0], f] + EPS_T and not miss: continue
        opts = []
        for p in range(1, len(nonm)):
            if X[nonm[p], f] <= X[nonm[p - 1], f] + EPS_T: continue
            thr = X[nonm[p - 1], f] / 2 + X[nonm[p], f] / 2
            for mgl in ((False, True) if miss else (False,)):
                L = nonm[:p] + (miss if mgl else []); R = nonm[p:] + ([] if mgl else miss); opts.append((thr, mgl, L, R))
        if miss: opts.append((float("inf"), False, nonm, miss))
        for thr, mgl, L, R in opts:
            if len(L) < msl or len(R) < msl: continue
            WL = sum(w[i] for i in L); WR = sum(w[i] for i in R)
            if WL < mwl or WR < mwl: continue
            iL = (w_imp_cls(L, y, w, crit, ncls) if task == "cls" else w_imp_reg(L, y, w, crit)); iR = (w_imp_cls(R, y, w, crit, ncls) if task == "cls" else w_imp_reg(R, y, w, crit))
            gain = Wt / Wtot * (imp - WL / Wt * iL - WR / Wt * iR)
            if gain > best + 1e-12: best = gain; cands = [(f, thr, mgl)]
            elif abs(gain - best) <= 1e-12: cands.append((f, thr, mgl))
    return imp, best, cands
def check_tree(est, X, y, w, task, crit, ncls=2, msl=1, mss=2, mwfl=0.0, max_depth=None, label="", features_per_node=None):
    """Walk the fitted tree with the training rows; at every node verify impurity, n_node_samples,
    weighted_n_node_samples, value, leaf-ness under the stopping rules and that the split is one of the
    maximal-decrease splits. Returns (ok, message)."""
    X = X.astype(np.float32).astype(np.float64)  # the tree works on float32 copies of X
    t = est.tree_; Wtot = sum(w); msgs = []
    mwl = mwfl * Wtot
    def rec(node, idx, depth):
        Wt = sum(w[i] for i in idx)
        imp = (w_imp_cls(idx, y, w, crit, ncls) if task == "cls" else w_imp_reg(idx, y, w, crit))
        if not close(t.impurity[node], imp, 1e-9, 1e-12): msgs.append(f"node {node} impurity {t.impurity[node]} vs {imp}")
        if t.n_node_samples[node] != len(idx) or not close(t.weighted_n_node_samples[node], Wt, 1e-12): msgs.append(f"node {node} sample counts")
        val = node_value(idx, y, w, task, ncls, crit)
        tv = t.value[node][0]
        if task == "cls" and V < (1, 4): tv = tv / tv.sum()
        if not allclose(tv, val, 1e-9, 1e-12): msgs.append(f"node {node} value {tv.tolist()} vs {val}")
        must_leaf = (depth >= (max_depth if max_depth is not None else 10 ** 9) or len(idx) < mss or len(idx) < 2 * msl or Wt < 2 * mwl or imp <= 1e-7)
        imp2, best, cands = best_splits(idx, X, y, w, task, crit, ncls, Wtot, msl, mwl, None if features_per_node is None else features_per_node(node))
        is_leaf = t.children_left[node] == -1
        if must_leaf or not cands:
            if not is_leaf: msgs.append(f"node {node} should be a leaf (reference impurity {imp:.1e}, library impurity {t.impurity[node]:.1e} > EPSILON 2.2e-16?, value {tv.tolist()})"); return
            return
        if is_leaf: msgs.append(f"node {node} is a leaf but a split with decrease {best} exists"); return
        f = t.feature[node]; thr = t.threshold[node]; mgl = bool(t.missing_go_to_left[node]) if hasattr(t, "missing_go_to_left") else False
        hit = any(f == cf and (thr == ct or close(thr, ct, 1e-12)) and (mgl == cm or not any(np.isnan(X[i, f]) for i in idx)) for cf, ct, cm in cands)
        if not hit: msgs.append(f"node {node} split (f{f} <= {thr}, missing_left={mgl}) not among best {cands} (decrease {best})")
        L = [i for i in idx if (X[i, f] <= thr if not np.isnan(X[i, f]) else mgl)]; R = [i for i in idx if i not in L]
        rec(t.children_left[node], L, depth + 1); rec(t.children_right[node], R, depth + 1)
    rec(0, list(range(len(y))), 0)
    return (not msgs), "; ".join(msgs[:3])

# --- classification, gini / entropy, by hand on a small dataset
Xt6 = np.array([[1, 5], [2, 4], [3, 6], [4, 1], [5, 2], [6, 3], [7, 7], [8, 8], [2, 2], [7, 1]], float)
yt6 = np.array([0, 0, 0, 1, 1, 1, 0, 0, 1, 1]); w1 = [1.0] * 10
imp0, best0, cands0 = best_splits(list(range(10)), Xt6, yt6, w1, "cls", "gini", 2, 10.0)
print(f"   root gini {imp0} (exact 1 - 2*(1/2)^2 = 0.5); best weighted decrease {best0:.6f} by {cands0}")
for crit in ("gini", "entropy", "log_loss"):
    if crit == "log_loss" and V < (1, 1): continue
    dt = DecisionTreeClassifier(criterion=crit, random_state=0).fit(Xt6, yt6)
    ok, msg = check_tree(dt, Xt6, yt6, w1, "cls", "entropy" if crit == "log_loss" else crit)
    print(f"   {crit}: root feature {dt.tree_.feature[0]} threshold {dt.tree_.threshold[0]} impurity {dt.tree_.impurity[0]:.6f} n_leaves {dt.get_n_leaves()}")
    report(f"DecisionTreeClassifier({crit}) every node: impurity by hand ({'1 - sum p^2' if crit == 'gini' else '-sum p log2 p'}), split = max weighted impurity decrease with midpoint threshold, leaves only when pure/too small, value = class fractions", ok, msg)
report("DecisionTreeClassifier(entropy) impurity uses log base 2 (root = 1.0 bit for a 5/5 split)", close(DecisionTreeClassifier(criterion="entropy").fit(Xt6, yt6).tree_.impurity[0], 1.0, 1e-12))
# within-feature ties: the first (lowest) threshold with strictly greater proxy wins
Xtie = np.array([[0.0], [1.0], [2.0], [3.0]]); ytie = np.array([0, 1, 0, 1])
dtt = DecisionTreeClassifier(max_depth=1).fit(Xtie, ytie)
imp_, best_, cands_ = best_splits([0, 1, 2, 3], Xtie, ytie, [1.0] * 4, "cls", "gini", 2, 4.0)
print(f"   tie dataset: candidates with equal decrease {cands_}; chosen threshold {dtt.tree_.threshold[0]}")
report("DecisionTreeClassifier tie between thresholds of one feature: the lowest threshold is kept (strict '>' on the proxy, ascending scan)", dtt.tree_.threshold[0] == cands_[0][1] and len(cands_) >= 2)
# min_samples_split / min_samples_leaf / min_weight_fraction_leaf
rs = np.random.RandomState(7); rsX = rs.rand(60, 3); rsy = (rsX[:, 0] + 0.5 * rsX[:, 1] + 0.2 * rs.randn(60) > 0.8).astype(int)
for kw, tag in (({"min_samples_split": 8}, "min_samples_split=8"), ({"min_samples_leaf": 5}, "min_samples_leaf=5"), ({"min_samples_split": 0.2}, "min_samples_split=0.2 (ceil(0.2 n))"), ({"max_depth": 3}, "max_depth=3")):
    dt = DecisionTreeClassifier(random_state=0, **kw).fit(rsX, rsy)
    mss = kw.get("min_samples_split", 2); mss = int(math.ceil(mss * 60)) if isinstance(mss, float) else mss
    ok, msg = check_tree(dt, rsX, rsy, [1.0] * 60, "cls", "gini", 2, msl=kw.get("min_samples_leaf", 1), mss=mss, max_depth=kw.get("max_depth"))
    report(f"DecisionTreeClassifier({tag}) on 60 random rows: whole tree equals the reference builder under that rule (n_leaves {dt.get_n_leaves()}, depth {dt.get_depth()})", ok, msg)
wr = rs.randint(1, 5, 60).astype(float)
dtw = DecisionTreeClassifier(random_state=0, min_weight_fraction_leaf=0.1).fit(rsX, rsy, sample_weight=wr)
ok, msg = check_tree(dtw, rsX, rsy, list(wr), "cls", "gini", 2, mwfl=0.1)
leafw = dtw.tree_.weighted_n_node_samples[dtw.tree_.children_left == -1]
report("DecisionTreeClassifier(min_weight_fraction_leaf=0.1, sample_weight): every leaf holds >= 10% of the total weight and the tree equals the weighted reference", ok and np.all(leafw >= 0.1 * wr.sum() - 1e-9), msg + f" (min leaf weight {leafw.min()}, 10% = {0.1 * wr.sum()})")
# class_weight
cw = DecisionTreeClassifier(random_state=0, class_weight={0: 1.0, 1: 3.0}).fit(rsX, rsy)
ok, msg = check_tree(cw, rsX, rsy, [1.0 if t == 0 else 3.0 for t in rsy], "cls", "gini", 2)
report("DecisionTreeClassifier(class_weight={0:1,1:3}) equals the tree grown with sample_weight = class weight (impurities, values, splits)", ok, msg)
cb = DecisionTreeClassifier(random_state=0, class_weight="balanced").fit(rsX, rsy); bal = {c: 60 / (2 * np.sum(rsy == c)) for c in (0, 1)}
ok, msg = check_tree(cb, rsX, rsy, [bal[t] for t in rsy], "cls", "gini", 2)
report("DecisionTreeClassifier(class_weight='balanced') uses n_samples / (n_classes * bincount(y)) as sample weights", ok, msg)
tb = cb.tree_; pure_split = [i for i in range(tb.node_count) if tb.children_left[i] != -1 and np.max(tb.value[i, 0, :]) / np.sum(tb.value[i, 0, :]) >= 1 - 1e-12]
print(f"   balanced tree: internal nodes whose samples are all one class: {pure_split} (impurities {[tb.impurity[i] for i in pure_split]})")
report("DecisionTreeClassifier(class_weight='balanced'): no single-class node is split further (docs: 'nodes are expanded until all leaves are pure'; pure test is impurity <= 2.2e-16)", not pure_split, f"(split pure nodes {pure_split})")
# max_features=1: at each node the split is the best split of its (single, randomly drawn) feature
dmf = DecisionTreeClassifier(random_state=3, max_features=1).fit(rsX, rsy)
ok, msg = check_tree(dmf, rsX, rsy, [1.0] * 60, "cls", "gini", 2, features_per_node=lambda n: [dmf.tree_.feature[n]] if dmf.tree_.feature[n] >= 0 else None)
report("DecisionTreeClassifier(max_features=1): every split is the best split over the feature it uses (non-constant draw), tree otherwise standard", ok, msg)
# predict_proba = weighted leaf class fractions; apply / decision_path consistency via own traversal
def traverse(t, x):
    x = np.asarray(x, np.float32).astype(np.float64); node = 0; path = [0]
    while t.children_left[node] != -1:
        f = t.feature[node]; v = x[f]
        if np.isnan(v): left = bool(t.missing_go_to_left[node]) if hasattr(t, "missing_go_to_left") else False
        else: left = v <= t.threshold[node]
        node = t.children_left[node] if left else t.children_right[node]; path.append(node)
    return node, path
Xte = rs.rand(30, 3)
leaves_mine = [traverse(dtw.tree_, x)[0] for x in Xte]
train_leaf = np.array([traverse(dtw.tree_, x)[0] for x in rsX])
frac = np.array([[wr[(train_leaf == l) & (rsy == c)].sum() for c in (0, 1)] for l in leaves_mine]); frac = frac / frac.sum(1, keepdims=True)
report("DecisionTreeClassifier apply() equals an independent traversal of tree_ arrays (x <= threshold goes left)", np.array_equal(dtw.apply(Xte), leaves_mine))
report("DecisionTreeClassifier predict_proba = weighted class fractions of the training rows in the leaf (sample_weight)", allclose(dtw.predict_proba(Xte), frac, 1e-12))
dp = dtw.decision_path(Xte).toarray()
report("DecisionTreeClassifier decision_path rows are exactly the root-to-leaf node sets of the traversal", all(set(np.flatnonzero(dp[i])) == set(traverse(dtw.tree_, Xte[i])[1]) for i in range(30)))
# feature_importances_
def fi_ref(t):
    imp = np.zeros(t.n_features); cl, cr = t.children_left, t.children_right
    for n in range(t.node_count):
        if cl[n] != -1:
            imp[t.feature[n]] += t.weighted_n_node_samples[n] * t.impurity[n] - t.weighted_n_node_samples[cl[n]] * t.impurity[cl[n]] - t.weighted_n_node_samples[cr[n]] * t.impurity[cr[n]]
    imp /= t.weighted_n_node_samples[0]
    return imp / imp.sum() if imp.sum() > 0 else imp
report("DecisionTreeClassifier feature_importances_ = normalised sum over splits of weighted impurity decrease (recomputed from tree_ arrays)", allclose(dtw.feature_importances_, fi_ref(dtw.tree_), 1e-12) and allclose(DecisionTreeClassifier(random_state=0).fit(rsX, rsy).feature_importances_, fi_ref(DecisionTreeClassifier(random_state=0).fit(rsX, rsy).tree_), 1e-12))
report("feature_importances_ sum to 1", close(dtw.feature_importances_.sum(), 1.0, 1e-12))
# cost complexity pruning path
def ccp_ref(t):
    cl, cr, imp, wn = t.children_left, t.children_right, t.impurity, t.weighted_n_node_samples
    n = t.node_count; r = wn * imp / wn[0]; pruned = set()
    def leaves(i):
        if cl[i] == -1 or i in pruned: return [i]
        return leaves(cl[i]) + leaves(cr[i])
    alphas = [0.0]; imps = [sum(r[l] for l in leaves(0))]
    def internal(i):
        if cl[i] == -1 or i in pruned: return []
        return [i] + internal(cl[i]) + internal(cr[i])
    while cl[0] != -1 and 0 not in pruned:
        best = None
        for i in sorted(internal(0)):
            L = leaves(i); a = (r[i] - sum(r[l] for l in L)) / (len(L) - 1)
            if best is None or a < best[1]: best = (i, a)
        pruned.add(best[0]); alphas.append(best[1]); imps.append(sum(r[l] for l in leaves(0)))
    return np.array(alphas), np.array(imps)
rs = np.random.RandomState(8); Xr = rs.rand(80, 2); yr = np.sin(3 * Xr[:, 0]) + Xr[:, 1] ** 2 + 0.1 * rs.randn(80)
for est, X_, y_, tag in ((DecisionTreeRegressor(random_state=0, max_depth=4), Xr, yr, "Regressor"), (DecisionTreeClassifier(random_state=0), rsX, rsy, "Classifier")):
    est.fit(X_, y_); path = est.cost_complexity_pruning_path(X_, y_); al, im = ccp_ref(est.tree_)
    print(f"   {tag} pruning path: {len(path.ccp_alphas)} alphas, first {np.round(path.ccp_alphas[:4], 6).tolist()} (ref {np.round(al[:4], 6).tolist()}); impurities first {np.round(path.impurities[:3], 6).tolist()} (ref {np.round(im[:3], 6).tolist()})")
    report(f"DecisionTree{tag} cost_complexity_pruning_path: ccp_alphas = successive weakest-link alpha_eff = (R(t) - R(T_t))/(|leaves|-1) and impurities = sum of leaf R (recomputed from tree_)", len(path.ccp_alphas) == len(al) and allclose(path.ccp_alphas, al, 1e-9, 1e-12) and allclose(path.impurities, im, 1e-9, 1e-12))
    report(f"DecisionTree{tag} pruning path alphas are non-decreasing and end at the root-only tree impurity", np.all(np.diff(path.ccp_alphas) >= -1e-15) and close(path.impurities[-1], est.tree_.impurity[0], 1e-12))
    nl = {"exact": [], "mid": []}
    for kk, a in enumerate(al):
        if kk == 0: continue
        for kind, ccp in (("exact", a), ("mid", (a + al[kk + 1]) / 2 if kk + 1 < len(al) else a * 2)):
            pe = type(est)(**{**est.get_params(), "ccp_alpha": float(ccp)}).fit(X_, y_)
            kexp = max(j for j in range(len(al)) if al[j] <= ccp + 1e-15)
            t = pe.tree_; rleaf = sum(t.weighted_n_node_samples[i] * t.impurity[i] for i in range(t.node_count) if t.children_left[i] == -1) / t.weighted_n_node_samples[0]
            okk = close(rleaf, im[kexp], 1e-9, 1e-12); nl[kind].append(okk)
            if not okk: print(f"   ccp_alpha={ccp!r} ({kind}, path alpha #{kk} = {a!r}): leaf impurity {rleaf!r}, expected {im[kexp]!r} (n_leaves {pe.get_n_leaves()})")
    report(f"DecisionTree{tag}(ccp_alpha) strictly between successive path alphas: total leaf impurity equals the path impurity of the last alpha <= ccp_alpha", all(nl["mid"]), f"({sum(nl['mid'])}/{len(nl['mid'])} alphas)")
    report(f"DecisionTree{tag}(ccp_alpha) exactly equal to a path alpha: that weakest link is pruned too (docs: pruning stops only when the minimal alpha_eff is *greater* than ccp_alpha)", all(nl["exact"]), f"({sum(nl['exact'])}/{len(nl['exact'])} alphas)")
# max_leaf_nodes best-first
def best_first_ref(X, y, w, task, crit, ncls, max_leaf):
    """Expand the frontier node with the largest weighted impurity decrease of its best split until max_leaf leaves."""
    X = X.astype(np.float32).astype(np.float64); Wtot = sum(w); frontier = []; splits = []
    def cand(idx):
        imp, best, c = best_splits(idx, X, y, w, task, crit, ncls, Wtot)
        return (best if (c and imp > 1e-7 and len(idx) >= 2) else -1.0, idx, c)
    frontier.append(cand(list(range(len(y))))); n_leaves = 1
    while n_leaves < max_leaf:
        frontier.sort(key=lambda r: r[0]); best = frontier.pop()
        if best[0] <= 0: break
        f, thr, _ = best[2][0]; splits.append((f, thr, best[0]))
        L = [i for i in best[1] if X[i, f] <= thr]; R = [i for i in best[1] if X[i, f] > thr]
        frontier.append(cand(L)); frontier.append(cand(R)); n_leaves += 1
    return splits
for ml in (3, 5, 8):
    dl = DecisionTreeRegressor(random_state=0, max_leaf_nodes=ml).fit(Xr, yr); ref = best_first_ref(Xr, yr, [1.0] * 80, "reg", "squared_error", 1, ml)
    got = sorted((int(dl.tree_.feature[i]), float(dl.tree_.threshold[i])) for i in range(dl.tree_.node_count) if dl.tree_.children_left[i] != -1)
    report(f"DecisionTreeRegressor(max_leaf_nodes={ml}) = best-first growth by largest weighted impurity decrease: exactly {ml} leaves and the same split set as the reference", dl.get_n_leaves() == ml and got == sorted((f, t) for f, t, _ in ref), f"(got {got[:3]}..., ref {sorted((f, t) for f, t, _ in ref)[:3]}...)")

# --- regressors: criteria and leaf values
rs = np.random.RandomState(9); yp = rs.poisson(3, 80).astype(float)
for crit, y_ in (("squared_error", yr), ("absolute_error", yr), ("poisson", yp)):
    dr = DecisionTreeRegressor(criterion=crit, random_state=0, max_depth=3).fit(Xr, y_)
    ok, msg = check_tree(dr, Xr, y_, [1.0] * 80, "reg", crit, 1, max_depth=3)
    report(f"DecisionTreeRegressor({crit}) whole tree: impurity {'= variance' if crit == 'squared_error' else '= mean |y - median|, leaf value = median' if crit == 'absolute_error' else '= mean y log(y/ybar) (half Poisson deviance), leaf value = mean'} and splits maximise the weighted decrease", ok, msg)
wreg = rs.randint(1, 4, 80).astype(float)
for crit, y_ in (("squared_error", yr), ("absolute_error", yr), ("poisson", yp)):
    dr = DecisionTreeRegressor(criterion=crit, random_state=0, max_depth=3).fit(Xr, y_, sample_weight=wreg)
    ok, msg = check_tree(dr, Xr, y_, list(wreg), "reg", crit, 1, max_depth=3)
    report(f"DecisionTreeRegressor({crit}, sample_weight) whole tree: weighted impurities and weighted {'median (midpoint at an exact half-weight tie)' if crit == 'absolute_error' else 'mean'} leaf values", ok, msg)
dm = DecisionTreeRegressor(criterion="absolute_error", max_depth=1).fit(np.array([[0.], [1.], [2.], [3.]]), [1.0, 2.0, 10.0, 11.0])
report("DecisionTreeRegressor(absolute_error) root value = median of an even-count node = midpoint of the two middle values (6.0)", close(dm.tree_.value[0][0][0], 6.0))
try:
    DecisionTreeRegressor(criterion="poisson").fit(Xr[:5], [1.0, -1.0, 2.0, 3.0, 1.0]); report("DecisionTreeRegressor(poisson) rejects negative targets", False)
except ValueError: report("DecisionTreeRegressor(poisson) rejects negative targets (ValueError)", True)
# value_ semantics (1.4 change) and multi-output
d2 = DecisionTreeClassifier(max_depth=1).fit(rsX, rsy)
if V >= (1, 4): report("tree_.value (classifier, >=1.4) holds weighted class fractions (rows sum to 1)", allclose(d2.tree_.value[:, 0, :].sum(1), np.ones(3), 1e-12))
else: report("tree_.value (classifier, <1.4) holds weighted class counts (root row sums to n)", close(d2.tree_.value[0, 0, :].sum(), 60))
Y2 = np.c_[yr, 2 * yr + 1]; dmo = DecisionTreeRegressor(max_depth=2, random_state=0).fit(Xr, Y2)
leaf_mo = dmo.apply(Xr)
report("DecisionTreeRegressor multi-output: value[leaf] = per-output means of the training rows in the leaf and predict returns shape (n, 2)", all(allclose(dmo.tree_.value[l, :, 0], Y2[leaf_mo == l].mean(0), 1e-12) for l in set(leaf_mo)) and dmo.predict(Xr).shape == (80, 2))
# friedman_mse
Xf = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [0, 0], [1, 1]], float) + 0.0
Yf = np.array([[10, -10], [10, -10], [-10, 10], [-10, 10], [10, -10], [-10, 10]], float) + np.array([[1, 1], [-1, -1], [1, 1], [-1, -1], [1, 1], [-1, -1]], float) * 0.5
# feature 0 separates output means by (+-20, -+20) (cancelling in the Friedman sum), feature 1 by (+-1, +-1) (adding up)
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); dfr = DecisionTreeRegressor(criterion="friedman_mse", max_depth=1, random_state=0).fit(Xf, Yf)
dse = DecisionTreeRegressor(criterion="squared_error", max_depth=1, random_state=0).fit(Xf, Yf)
print(f"   friedman_mse root feature {dfr.tree_.feature[0]} vs squared_error root feature {dse.tree_.feature[0]}; FutureWarning: {any(w.category is FutureWarning for w in wl)}")
if V >= (1, 9):
    report("DecisionTreeRegressor(friedman_mse) on 1.9+: FutureWarning and identical tree to squared_error (deprecation maps it to squared_error)", any(w.category is FutureWarning for w in wl) and np.array_equal(dfr.tree_.feature, dse.tree_.feature))
else:
    fa = DecisionTreeRegressor(criterion="friedman_mse", random_state=0).fit(Xr, yr).tree_; fb = DecisionTreeRegressor(criterion="squared_error", random_state=0).fit(Xr, yr).tree_
    ndiff = int(np.sum(fa.threshold != fb.threshold)) if fa.node_count == fb.node_count else -1
    print(f"   friedman_mse vs squared_error single output, full trees: {ndiff} differing nodes of {fa.node_count} (differences arise only at tied 2-sample nodes)")
    report("DecisionTreeRegressor(friedman_mse) single-output equals squared_error split choice at max_depth=3 (documented in the 1.9 deprecation as 'always equivalent'; proxies rank splits identically for one output)", np.array_equal(DecisionTreeRegressor(criterion="friedman_mse", random_state=0, max_depth=3).fit(Xr, yr).tree_.threshold, DecisionTreeRegressor(criterion="squared_error", random_state=0, max_depth=3).fit(Xr, yr).tree_.threshold))
    report("DecisionTreeRegressor(friedman_mse) multi-output chooses the same root split as squared_error (1.9 deprecation note: 'both were always equivalent')", dfr.tree_.feature[0] == dse.tree_.feature[0], f"(friedman feature {dfr.tree_.feature[0]}, squared_error feature {dse.tree_.feature[0]}; Friedman proxy maximises (sum_k dmean_k)^2 which is 0 for feature 0 here)")
# monotonic_cst
if V >= (1, 4):
    rs = np.random.RandomState(10); Xm = rs.rand(200, 2); ym = ((Xm[:, 0] + 0.3 * np.sin(9 * Xm[:, 0]) + 0.5 * Xm[:, 1] + 0.3 * rs.randn(200)) > 0.9).astype(int)
    dmc = DecisionTreeClassifier(monotonic_cst=[1, 0], random_state=0).fit(Xm, ym)
    grid = np.linspace(0, 1, 60); okm = True
    for x1 in np.linspace(0, 1, 15):
        p = dmc.predict_proba(np.c_[grid, np.full(60, x1)])[:, 1]; okm &= bool(np.all(np.diff(p) >= -1e-12))
    dun = DecisionTreeClassifier(random_state=0).fit(Xm, ym); viol = 0
    for x1 in np.linspace(0, 1, 15): viol += int(np.any(np.diff(dun.predict_proba(np.c_[grid, np.full(60, x1)])[:, 1]) < 0))
    report("DecisionTreeClassifier(monotonic_cst=[1,0]): predicted positive-class probability is non-decreasing in feature 0 on a grid (unconstrained tree violates it)", okm and viol > 0, f"(unconstrained violations on {viol}/15 grid lines)")
    dmr = DecisionTreeRegressor(monotonic_cst=[-1, 0], random_state=0, max_depth=6).fit(Xm, Xm[:, 0] * -2 + np.sin(12 * Xm[:, 0]) + rs.randn(200) * 0.3)
    okr = all(np.all(np.diff(dmr.predict(np.c_[grid, np.full(60, x1)])) <= 1e-12) for x1 in np.linspace(0, 1, 15))
    report("DecisionTreeRegressor(monotonic_cst=[-1,0]): predictions non-increasing in feature 0", okr)
    try: DecisionTreeClassifier(monotonic_cst=[1, 0]).fit(Xm, rs.randint(0, 3, 200)); report("monotonic_cst with 3 classes raises (not supported for multiclass)", False)
    except ValueError: report("monotonic_cst with 3 classes raises ValueError (documented: not supported for multiclass)", True)
# ExtraTreeClassifier: random thresholds within [min, max) of the node's feature values
def check_extra(est, X, y):
    X = X.astype(np.float32).astype(np.float64); t = est.tree_; msgs = []
    def rec(node, idx):
        if t.children_left[node] == -1: return
        f = t.feature[node]; vals = X[idx, f]; vals = vals[~np.isnan(vals)]; thr = t.threshold[node]
        if not (vals.min() <= thr < vals.max() or (vals.min() == vals.max() == thr)) and not np.isinf(thr): msgs.append(f"node {node}: threshold {thr} outside [{vals.min()}, {vals.max()})")
        L = [i for i in idx if (X[i, f] <= thr if not np.isnan(X[i, f]) else bool(t.missing_go_to_left[node]))]; R = [i for i in idx if i not in L]
        rec(t.children_left[node], L); rec(t.children_right[node], R)
    rec(0, list(range(len(y)))); return not msgs, "; ".join(msgs[:3])
et = ExtraTreeClassifier(random_state=5, max_features=None).fit(rsX, rsy); ok, msg = check_extra(et, rsX, rsy)
report("ExtraTreeClassifier: every split threshold lies in [min, max) of the feature over the node's training rows (random draw, max mapped to min)", ok, msg)
thr_all = [float(et.tree_.threshold[i]) for i in range(et.tree_.node_count) if et.tree_.children_left[i] != -1]
mids = set();
for f in range(3):
    v = np.unique(rsX[:, f]); mids |= set(((v[:-1] + v[1:]) / 2).tolist())
report("ExtraTreeClassifier thresholds are not midpoints between adjacent values (they are uniform draws)", sum(1 for t_ in thr_all if t_ in mids) == 0)
et_leaf = et.apply(Xte); tl = et.apply(rsX)
report("ExtraTreeClassifier predict_proba = class fractions of the training rows in the leaf", allclose(et.predict_proba(Xte), [[np.mean(rsy[tl == l] == c) for c in (0, 1)] for l in et_leaf], 1e-12))
etr = ExtraTreeRegressor(random_state=1, max_features=None).fit(Xr, yr); ok, msg = check_extra(etr, Xr, yr)
report("ExtraTreeRegressor thresholds within [min, max) and leaf values = means", ok and allclose(etr.tree_.value[etr.apply(Xr), 0, 0], [yr[etr.apply(Xr) == l].mean() for l in etr.apply(Xr)], 1e-12), msg)
# export_text
dsm = DecisionTreeClassifier(max_depth=2, random_state=0).fit(rsX, rsy, sample_weight=wr)
txt = export_text(dsm, feature_names=["a", "b", "c"], show_weights=True, decimals=3)
leaf_lines = [l for l in txt.splitlines() if "weights" in l]
lv = [[float(v) for v in l.split("weights: [")[1].split("]")[0].split(",")] for l in leaf_lines]
lf = dsm.tree_.children_left == -1
exp_w = sorted((dsm.tree_.value[i, 0, :] * (dsm.tree_.weighted_n_node_samples[i] if V >= (1, 4) else 1.0)).round(3).tolist() for i in np.flatnonzero(lf))
print(f"   export_text leaf weights {lv}")
report("export_text(show_weights=True) prints the weighted class counts of each leaf (value * weighted_n_node_samples) and 'class:' = argmax", sorted(lv) == exp_w and all(("class: %d" % np.argmax(v)) in l for v, l in zip(lv, leaf_lines)))
txr = export_text(DecisionTreeRegressor(max_depth=1, random_state=0).fit(Xr, yr), decimals=4)
vals_r = [float(l.split("value: [")[1].split("]")[0]) for l in txr.splitlines() if "value" in l]
dr1 = DecisionTreeRegressor(max_depth=1, random_state=0).fit(Xr, yr)
report("export_text regressor leaf 'value:' = leaf mean (tree_.value)", sorted(vals_r) == sorted(np.round(dr1.tree_.value[dr1.tree_.children_left == -1, 0, 0], 4).tolist()))
# missing values (1.3+)
if V >= (1, 3):
    X1 = np.array([0, 1, 6, np.nan]).reshape(-1, 1); t1 = DecisionTreeClassifier(random_state=0).fit(X1, [0, 0, 1, 1])
    report("missing values (user guide example 1): X=[0,1,6,nan], y=[0,0,1,1] -> predict(X) = [0,0,1,1] (nan goes with the class used at training)", t1.predict(X1).tolist() == [0, 0, 1, 1])
    X2 = np.array([np.nan, -1, np.nan, 1]).reshape(-1, 1); t2 = DecisionTreeClassifier(random_state=0, max_depth=1).fit(X2, [0, 0, 1, 1])
    report("missing values (example 2): tie between sending nan left/right is broken towards the right child -> predict([nan]) = 1", t2.predict([[np.nan]]).tolist() == [1])
    X3 = np.array([0, 1, 2, 3]).reshape(-1, 1); t3 = DecisionTreeClassifier(random_state=0).fit(X3, [0, 1, 1, 1])
    report("missing values (example 3): no nan at training -> nan mapped to the child with the most samples -> predict([nan]) = 1", t3.predict([[np.nan]]).tolist() == [1] and bool(t3.tree_.missing_go_to_left[0]) is False)
    rs = np.random.RandomState(12); Xn = rs.rand(60, 3); Xn[rs.rand(60, 3) < 0.15] = np.nan; yn = ((np.nan_to_num(Xn[:, 0], nan=0.5) + np.nan_to_num(Xn[:, 1], nan=0.2)) > 0.9).astype(int)
    dn = DecisionTreeClassifier(random_state=0, max_depth=4).fit(Xn, yn)
    ok, msg = check_tree(dn, Xn, yn, [1.0] * 60, "cls", "gini", 2, max_depth=4)
    report("DecisionTreeClassifier with 15% NaN: every split is the best over thresholds x nan-left/nan-right plus 'nan alone right' (threshold inf) and impurities/values by hand", ok, msg)
    tcn = DecisionTreeClassifier(random_state=0).fit(np.array([[1.0], [1.0], [1.0], [np.nan], [np.nan]]), [0, 0, 0, 1, 1])
    report("missing values: a feature constant on the non-missing rows but with NaNs is still split ('nan alone' split, threshold inf) -> [1,1,1,nan,nan] with y=[0,0,0,1,1] is separated", tcn.get_n_leaves() == 2 and np.isinf(tcn.tree_.threshold[0]) and tcn.predict(np.array([[1.0], [np.nan]])).tolist() == [0, 1], f"(n_leaves {tcn.get_n_leaves()}, root threshold {tcn.tree_.threshold[0]})")
    ypn = np.random.RandomState(16).poisson(2 + 3 * np.nan_to_num(Xn[:, 0], nan=0.5), 60).astype(float)
    dpn = DecisionTreeRegressor(criterion="poisson", random_state=0, max_depth=3).fit(Xn, ypn); ok, msg = check_tree(dpn, Xn, ypn, [1.0] * 60, "reg", "poisson", 1, max_depth=3)
    report("DecisionTreeRegressor(poisson) with NaN in X: node impurities are the (non-negative) half Poisson deviance by hand and splits are optimal over the NaN routing options", ok and np.all(dpn.tree_.impurity >= 0), msg + f" (min impurity {dpn.tree_.impurity.min():.3e})")
    Xtn = rs.rand(40, 3); Xtn[rs.rand(40, 3) < 0.3] = np.nan
    report("DecisionTreeClassifier apply() on NaN test rows equals traversal using tree_.missing_go_to_left", np.array_equal(dn.apply(Xtn), [traverse(dn.tree_, x)[0] for x in Xtn]))
    if V >= (1, 6):
        en = ExtraTreeClassifier(random_state=0).fit(Xn, yn); ok, msg = check_extra(en, Xn, yn)
        report("ExtraTreeClassifier (1.6+) with NaN: thresholds within the non-missing [min, max) and apply() consistent with missing_go_to_left", ok and np.array_equal(en.apply(Xtn), [traverse(en.tree_, x)[0] for x in Xtn]), msg)

# =============================================================================
print("== dummy")
yd = np.array([0] * 5 + [1] * 3 + [2] * 2); Xd = np.zeros((10, 1)); Xdt = np.zeros((7, 1))
report("DummyClassifier(most_frequent): predict = most frequent class, predict_proba one-hot", np.all(DummyClassifier(strategy="most_frequent").fit(Xd, yd).predict(Xdt) == 0) and allclose(DummyClassifier(strategy="most_frequent").fit(Xd, yd).predict_proba(Xdt), np.tile([1, 0, 0], (7, 1))))
dpr = DummyClassifier(strategy="prior").fit(Xd, yd)
report("DummyClassifier(prior): class_prior_ = [.5,.3,.2], predict = most frequent, predict_proba = prior for every row", allclose(dpr.class_prior_, [0.5, 0.3, 0.2]) and np.all(dpr.predict(Xdt) == 0) and allclose(dpr.predict_proba(Xdt), np.tile([0.5, 0.3, 0.2], (7, 1))))
report("DummyClassifier(prior) predict_log_proba = log prior", allclose(dpr.predict_log_proba(Xdt), np.tile(np.log([0.5, 0.3, 0.2]), (7, 1)), 1e-12))
ds = DummyClassifier(strategy="stratified", random_state=0).fit(Xd, yd); Xbig = np.zeros((30000, 1))
Ps = ds.predict_proba(Xbig); ps = ds.predict(Xbig)
freq = np.bincount(ps, minlength=3) / 30000
print(f"   stratified: class frequencies over 30000 draws {freq.round(4).tolist()} (prior [.5,.3,.2])")
report("DummyClassifier(stratified) predict_proba rows are one-hot multinomial(1, prior) samples and predict = the class with probability one (same random_state)", np.all(Ps.sum(1) == 1) and np.all(np.isin(Ps, [0, 1])) and np.array_equal(ps, np.argmax(Ps, 1)))
report("DummyClassifier(stratified) empirical class frequencies within 0.01 of the prior", np.all(np.abs(freq - [0.5, 0.3, 0.2]) < 0.01))
du = DummyClassifier(strategy="uniform", random_state=0).fit(Xd, yd); fu = np.bincount(du.predict(Xbig), minlength=3) / 30000
report("DummyClassifier(uniform): predict_proba = 1/3 and predicted class frequencies within 0.01 of 1/3", allclose(du.predict_proba(Xdt), np.full((7, 3), 1 / 3), 1e-12) and np.all(np.abs(fu - 1 / 3) < 0.01), f"(freq {fu.round(4).tolist()})")
dc = DummyClassifier(strategy="constant", constant=2).fit(Xd, yd)
report("DummyClassifier(constant=2): predict = 2, predict_proba one-hot on class 2", np.all(dc.predict(Xdt) == 2) and allclose(dc.predict_proba(Xdt), np.tile([0, 0, 1], (7, 1))))
try: DummyClassifier(strategy="constant", constant=7).fit(Xd, yd); report("DummyClassifier(constant not in classes) raises ValueError", False)
except ValueError: report("DummyClassifier(constant not in classes) raises ValueError", True)
ytest = np.array([0, 1, 2, 0, 0, 1, 2]); report("DummyClassifier.score = accuracy (most_frequent on this y = 3/7)", close(DummyClassifier(strategy="most_frequent").fit(Xd, yd).score(Xdt, ytest), 3 / 7, 1e-12))
report("DummyClassifier.score with sample_weight = weighted accuracy", close(DummyClassifier(strategy="most_frequent").fit(Xd, yd).score(Xdt, ytest, sample_weight=[1, 2, 3, 4, 5, 6, 7]), (1 + 4 + 5) / 28, 1e-12))
dwc = DummyClassifier(strategy="prior").fit(Xd, yd, sample_weight=[1, 1, 1, 1, 1, 2, 2, 2, 5, 5])
report("DummyClassifier(prior, sample_weight): class_prior_ = weighted class frequencies [5, 6, 10]/21", allclose(dwc.class_prior_, [5 / 21, 6 / 21, 10 / 21], 1e-12) and dwc.predict(Xdt)[0] == 2)
Y2d = np.c_[yd, (yd == 0).astype(int)]; d2o = DummyClassifier(strategy="prior").fit(Xd, Y2d)
report("DummyClassifier multi-output: class_prior_ is a list per output and predict returns (n, 2)", isinstance(d2o.class_prior_, list) and allclose(d2o.class_prior_[1], [0.5, 0.5]) and d2o.predict(Xdt).shape == (7, 2))
# DummyRegressor
yreg = np.array([1.0, 2.0, 3.0, 4.0, 10.0]); Xr5 = np.zeros((5, 1))
report("DummyRegressor(mean): constant_ = mean = 4.0", close(DummyRegressor().fit(Xr5, yreg).constant_[0, 0], 4.0))
report("DummyRegressor(median): constant_ = 3.0 (np.median)", close(DummyRegressor(strategy="median").fit(Xr5, yreg).constant_[0, 0], 3.0))
report("DummyRegressor(quantile=0.25): np.percentile linear interpolation -> 2.0", close(DummyRegressor(strategy="quantile", quantile=0.25).fit(Xr5, yreg).constant_[0, 0], 2.0))
report("DummyRegressor(quantile=0.9): np.percentile linear -> 4 + 0.6*6 = 7.6", close(DummyRegressor(strategy="quantile", quantile=0.9).fit(Xr5, yreg).constant_[0, 0], 7.6))
report("DummyRegressor(constant=3.5): predict = 3.5", np.all(DummyRegressor(strategy="constant", constant=3.5).fit(Xr5, yreg).predict(Xr5) == 3.5))
wreg5 = np.array([1, 1, 2, 1, 1.0])
report("DummyRegressor(mean, sample_weight): weighted mean (1+2+6+4+10)/6", close(DummyRegressor().fit(Xr5, yreg, sample_weight=wreg5).constant_[0, 0], 23 / 6, 1e-12))
yeven = np.array([1.0, 2.0, 3.0, 4.0]); X4 = np.zeros((4, 1))
mu = DummyRegressor(strategy="median").fit(X4, yeven).constant_[0, 0]; mw_ = DummyRegressor(strategy="median").fit(X4, yeven, sample_weight=np.ones(4)).constant_[0, 0]
print(f"   DummyRegressor(median) on [1,2,3,4]: no weights {mu}, sample_weight=ones {mw_}; repeated data [1,2,2,3,4] median {np.median([1, 2, 2, 3, 4])} vs sample_weight=[1,2,1,1] {DummyRegressor(strategy='median').fit(X4, yeven, sample_weight=[1, 2, 1, 1]).constant_[0, 0]}")
report("DummyRegressor(median): sample_weight=ones gives the same median (2.5) as no sample_weight (unit-weight invariance)", close(mw_, mu))
report("DummyRegressor(median, sample_weight=[1,2,1,1]) equals the median of the rows repeated by weight (2.0)", close(DummyRegressor(strategy="median").fit(X4, yeven, sample_weight=[1, 2, 1, 1]).constant_[0, 0], 2.0))
qu = DummyRegressor(strategy="quantile", quantile=0.25).fit(X4, yeven).constant_[0, 0]; qw = DummyRegressor(strategy="quantile", quantile=0.25).fit(X4, yeven, sample_weight=np.ones(4)).constant_[0, 0]
print(f"   DummyRegressor(quantile=0.25) on [1,2,3,4]: no weights {qu}, sample_weight=ones {qw}")
report("DummyRegressor(quantile=0.25): sample_weight=ones equals no sample_weight (1.75)", close(qw, qu))
report("DummyRegressor.score = R^2 (mean predictor on y itself -> 0.0; constant 2.5 on [1,2,3,4] -> 1 - 5/5 = 0.0; constant 3.5 -> 1 - 9/5 = -0.8)", close(DummyRegressor().fit(Xr5, yreg).score(Xr5, yreg), 0.0, 1e-12, 1e-12) and close(DummyRegressor(strategy="constant", constant=2.5).fit(X4, yeven).score(X4, yeven), 0.0, 1e-12, 1e-12) and close(DummyRegressor(strategy="constant", constant=3.5).fit(X4, yeven).score(X4, yeven), -0.8))
d2r = DummyRegressor(strategy="median").fit(Xr5, np.c_[yreg, -yreg])
report("DummyRegressor multi-output median: constant_ shape (1, 2) = [3, -3]", d2r.constant_.shape == (1, 2) and allclose(d2r.constant_, [[3.0, -3.0]]))

# =============================================================================
print("== multiclass")
rs = np.random.RandomState(13); Xm3 = rs.randn(90, 4); ym3 = np.repeat([0, 1, 2], 30); Xm3[:, 0] += ym3 * 1.5; Xm3[:, 1] -= ym3
Xm3t = rs.randn(20, 4)
LR = lambda: LogisticRegression(C=0.7, max_iter=2000)
ovr = OneVsRestClassifier(LR()).fit(Xm3, ym3)
ests = [LR().fit(Xm3, (ym3 == c).astype(int)) for c in (0, 1, 2)]
Pc = np.array([e.predict_proba(Xm3t)[:, 1] for e in ests]).T; Dc = np.array([e.decision_function(Xm3t) for e in ests]).T
report("OneVsRestClassifier: per-class estimators equal separate binary fits of class-vs-rest (coef_)", all(allclose(a.coef_, b.coef_, 1e-9) for a, b in zip(ovr.estimators_, ests)))
report("OneVsRestClassifier.predict_proba = per-class P(class) normalised to sum 1 (documented: 'rows sum to 1' in the single-label case)", allclose(ovr.predict_proba(Xm3t), Pc / Pc.sum(1, keepdims=True), 1e-9))
report("OneVsRestClassifier.decision_function = stacked binary decision functions; predict = argmax", allclose(ovr.decision_function(Xm3t), Dc, 1e-9) and np.array_equal(ovr.predict(Xm3t), np.argmax(Dc, 1)))
Yml = np.c_[ym3 == 0, ym3 != 1].astype(int); ovm = OneVsRestClassifier(LR()).fit(Xm3, Yml)
em = [LR().fit(Xm3, Yml[:, j]) for j in range(2)]; Pm = np.array([e.predict_proba(Xm3t)[:, 1] for e in em]).T
report("OneVsRestClassifier multilabel: predict_proba = marginal per-label probabilities (not normalised) and predict = indicator of decision_function > 0", ovm.multilabel_ and allclose(ovm.predict_proba(Xm3t), Pm, 1e-9) and np.array_equal(ovm.predict(Xm3t), (np.array([e.decision_function(Xm3t) for e in em]).T > 0).astype(int)))
ovo = OneVsOneClassifier(LR()).fit(Xm3, ym3)
pairs = [(0, 1), (0, 2), (1, 2)]; pe = []
for i, j in pairs:
    msk = (ym3 == i) | (ym3 == j); pe.append(LR().fit(Xm3[msk], (ym3[msk] == j).astype(int)))
report("OneVsOneClassifier: pairwise estimators equal separate fits on the class pairs (label 0 for the smaller class)", all(allclose(a.coef_, b.coef_, 1e-9) for a, b in zip(ovo.estimators_, pe)))
votes = np.zeros((20, 3)); conf = np.zeros((20, 3))
for kq, (i, j) in enumerate(pairs):
    d = pe[kq].decision_function(Xm3t); pred = pe[kq].predict(Xm3t)
    votes[pred == 0, i] += 1; votes[pred == 1, j] += 1; conf[:, i] -= d; conf[:, j] += d
dec_ref = votes + conf / (3 * (np.abs(conf) + 1))
report("OneVsOneClassifier.decision_function = votes + sum_of_confidences / (3 (|sum| + 1)) recomputed from the pairwise estimators", allclose(ovo.decision_function(Xm3t), dec_ref, 1e-9))
report("OneVsOneClassifier.predict = argmax of that (confidence breaks vote ties without overturning a vote difference of 1)", np.array_equal(ovo.predict(Xm3t), np.argmax(dec_ref, 1)) and np.all(np.abs(conf / (3 * (np.abs(conf) + 1))) < 1 / 3))
# construct a genuine 3-way vote tie and check the confidence tie-break decides
tie_rows = [r for r in range(20) if len(set(votes[r])) == 1]
print(f"   OvO: {len(tie_rows)} test rows with a full vote tie (1,1,1) -> decided by confidences")
# a triangle of blobs has a central region with cyclic pairwise votes (1,1,1): there the confidence sum must decide
Xtri = np.r_[rs.randn(60, 2) * 0.8 + [0, 2.5], rs.randn(60, 2) * 0.8 + [-2.2, -1.2], rs.randn(60, 2) * 0.8 + [2.2, -1.2]]; ytri = np.repeat([0, 1, 2], 60)
ovt = OneVsOneClassifier(LR()).fit(Xtri, ytri); gx, gy = np.meshgrid(np.linspace(-1.5, 1.5, 61), np.linspace(-1.5, 1.5, 61)); G = np.c_[gx.ravel(), gy.ravel()]
pt = []; vg = np.zeros((len(G), 3)); cg = np.zeros((len(G), 3))
for kq, (i, j) in enumerate(pairs):
    msk = (ytri == i) | (ytri == j); e = LR().fit(Xtri[msk], (ytri[msk] == j).astype(int)); d = e.decision_function(G); pr = e.predict(G)
    vg[pr == 0, i] += 1; vg[pr == 1, j] += 1; cg[:, i] -= d; cg[:, j] += d
ties = np.flatnonzero((vg == 1).all(1)); dec_t = vg + cg / (3 * (np.abs(cg) + 1))
print(f"   OvO triangle: {len(ties)} grid points with cyclic votes (1,1,1); library predictions there {np.bincount(ovt.predict(G[ties]), minlength=3).tolist()} per class")
report("OneVsOneClassifier on cyclic-vote points (votes 1,1,1): predict = argmax of the summed confidences (documented confidence tie-break), recomputed from the pairwise fits", len(ties) > 0 and np.array_equal(ovt.predict(G[ties]), np.argmax(dec_t[ties], 1)) and allclose(ovt.decision_function(G[ties]), dec_t[ties], 1e-9), f"({len(ties)} tie points)")
occ = OutputCodeClassifier(LR(), code_size=2, random_state=0).fit(Xm3, ym3)
report("OutputCodeClassifier(code_size=2): int(n_classes*code_size) = 6 estimators, code_book_ shape (3, 6) in {-1, 1} (estimator has decision_function)", len(occ.estimators_) == 6 and occ.code_book_.shape == (3, 6) and set(np.unique(occ.code_book_)) <= {-1.0, 1.0})
Yo = np.array([e.decision_function(Xm3t) for e in occ.estimators_]).T
dist = ((Yo[:, None, :] - occ.code_book_[None, :, :]) ** 2).sum(-1)
report("OutputCodeClassifier.predict = class whose code word is nearest (euclidean) to the vector of binary decision_function values", np.array_equal(occ.predict(Xm3t), occ.classes_[np.argmin(dist, 1)]))
cols = [kq for kq in range(6) if len(set(occ.code_book_[:, kq])) == 2]
cb_ests = {kq: LR().fit(Xm3, (occ.code_book_[ym3, kq] == 1).astype(int)) for kq in cols}
report("OutputCodeClassifier estimators are binary fits on the code-book columns (constant columns get a constant predictor)", all(allclose(occ.estimators_[kq].coef_, cb_ests[kq].coef_, 1e-9) for kq in cols), f"({len(cols)} non-constant columns of 6)")
occp = OutputCodeClassifier(GaussianNB(), code_size=1, random_state=0).fit(Xm3, ym3)
report("OutputCodeClassifier with an estimator lacking decision_function: code_book_ in {0, 1}", set(np.unique(occp.code_book_)) <= {0.0, 1.0} and len(occp.estimators_) == 3)

# =============================================================================
print("== multioutput")
Ymo = np.c_[ym3, (Xm3[:, 2] > 0).astype(int)]
moc = MultiOutputClassifier(LR()).fit(Xm3, Ymo); sep = [LR().fit(Xm3, Ymo[:, j]) for j in range(2)]
report("MultiOutputClassifier: each output's estimator equals a separate fit; predict_proba is a list per output", all(allclose(a.coef_, b.coef_, 1e-9) for a, b in zip(moc.estimators_, sep)) and all(allclose(p, e.predict_proba(Xm3t), 1e-9) for p, e in zip(moc.predict_proba(Xm3t), sep)) and np.array_equal(moc.predict(Xm3t), np.c_[sep[0].predict(Xm3t), sep[1].predict(Xm3t)]))
Yreg = np.c_[Xm3 @ [1, 2, 0, 0] + rs.randn(90) * 0.1, Xm3 @ [0, 0, 1, -1]]
mor = MultiOutputRegressor(Ridge(alpha=1.0)).fit(Xm3, Yreg); sepr = [Ridge(alpha=1.0).fit(Xm3, Yreg[:, j]) for j in range(2)]
report("MultiOutputRegressor(Ridge): per-output coef_ equal separate fits and predict stacks them", all(allclose(a.coef_, b.coef_, 1e-9) for a, b in zip(mor.estimators_, sepr)) and allclose(mor.predict(Xm3t), np.c_[sepr[0].predict(Xm3t), sepr[1].predict(Xm3t)], 1e-9))
Ych = np.c_[(ym3 == 0), (ym3 != 1), Xm3[:, 3] > 0].astype(int)
cc = ClassifierChain(LR(), order=[2, 0, 1], random_state=0).fit(Xm3, Ych)
c0 = LR().fit(Xm3, Ych[:, 2]); c1 = LR().fit(np.c_[Xm3, Ych[:, 2]], Ych[:, 0]); c2 = LR().fit(np.c_[Xm3, Ych[:, 2], Ych[:, 0]], Ych[:, 1])
report("ClassifierChain(order=[2,0,1]) fit: estimator k is fit on [X, true labels of the previous outputs in chain order]", np.array_equal(cc.order_, [2, 0, 1]) and allclose(cc.estimators_[0].coef_, c0.coef_, 1e-9) and allclose(cc.estimators_[1].coef_, c1.coef_, 1e-9) and allclose(cc.estimators_[2].coef_, c2.coef_, 1e-9))
p0 = c0.predict(Xm3t); p1 = c1.predict(np.c_[Xm3t, p0]); p2 = c2.predict(np.c_[Xm3t, p0, p1])
report("ClassifierChain predict: chained features are the previous *predictions* and columns are put back in the original output order", np.array_equal(cc.predict(Xm3t), np.c_[p1, p2, p0]))
pp2 = c2.predict_proba(np.c_[Xm3t, p0, p1])[:, 1]
report("ClassifierChain predict_proba: P(label) from each estimator given the predicted chain features", allclose(cc.predict_proba(Xm3t), np.c_[c1.predict_proba(np.c_[Xm3t, p0])[:, 1], pp2, c0.predict_proba(Xm3t)[:, 1]], 1e-9))
if V >= (1, 5):
    ccp = ClassifierChain(LR(), order=[2, 0, 1], chain_method="predict_proba").fit(Xm3, Ych)
    q0 = c0.predict_proba(Xm3t)[:, 1]; q1 = c1.predict_proba(np.c_[Xm3t, q0]); q2 = c2.predict(np.c_[Xm3t, q0, q1[:, 1]])
    report("ClassifierChain(chain_method='predict_proba'): chained features at predict time are predict_proba[:, 1] (training still uses true labels)", allclose(ccp.estimators_[2].coef_, c2.coef_, 1e-9) and np.array_equal(ccp.predict(Xm3t), np.c_[c1.predict(np.c_[Xm3t, q0]), q2, c0.predict(Xm3t)]))
ccv = ClassifierChain(LR(), order=[2, 0, 1], cv=KFold(3, shuffle=True, random_state=0)).fit(Xm3, Ych)
cvp0 = cross_val_predict(LR(), Xm3, Ych[:, 2], cv=KFold(3, shuffle=True, random_state=0)); v1 = LR().fit(np.c_[Xm3, cvp0], Ych[:, 0])
cvp1 = cross_val_predict(LR(), np.c_[Xm3, cvp0], Ych[:, 0], cv=KFold(3, shuffle=True, random_state=0)); v2 = LR().fit(np.c_[Xm3, cvp0, cvp1], Ych[:, 1])
report("ClassifierChain(cv=KFold(3, shuffle)): chained training features are cross_val_predict predictions of the earlier links (recomputed)", allclose(ccv.estimators_[1].coef_, v1.coef_, 1e-9) and allclose(ccv.estimators_[2].coef_, v2.coef_, 1e-9))
rc = RegressorChain(Ridge(alpha=1.0), order=[1, 0]).fit(Xm3, Yreg)
r0 = Ridge(alpha=1.0).fit(Xm3, Yreg[:, 1]); r1 = Ridge(alpha=1.0).fit(np.c_[Xm3, Yreg[:, 1]], Yreg[:, 0])
report("RegressorChain(order=[1,0]): second link fit on [X, y1] and predict chains the first prediction, output re-ordered", allclose(rc.estimators_[1].coef_, r1.coef_, 1e-9) and allclose(rc.predict(Xm3t), np.c_[r1.predict(np.c_[Xm3t, r0.predict(Xm3t)]), r0.predict(Xm3t)], 1e-9))
ccr = ClassifierChain(LR(), order="random", random_state=3).fit(Xm3, Ych)
report("ClassifierChain(order='random', random_state): order_ is a permutation of the outputs", sorted(ccr.order_.tolist()) == [0, 1, 2])

# =============================================================================
print("== semi_supervised")
rs = np.random.RandomState(14); Xs = rs.randn(40, 2); Xs[20:] += 3.0; ys_true = np.r_[np.zeros(20, int), np.ones(20, int)]
ys = ys_true.copy(); unl = rs.rand(40) < 0.7; ys[unl] = -1; ys[0] = 0; ys[20] = 1; unl = ys == -1
print(f"   {unl.sum()} unlabeled of 40")
gamma = 0.5
W = np.exp(-gamma * ((Xs[:, None, :] - Xs[None, :, :]) ** 2).sum(-1))
T = W / W.sum(1, keepdims=True)
Y0 = np.zeros((40, 2)); Y0[~unl, ys[~unl]] = 1
def harmonic(T, Y0, unl):
    Fu = np.linalg.solve(np.eye(unl.sum()) - T[np.ix_(unl, unl)], T[np.ix_(unl, ~unl)] @ Y0[~unl]); return Fu
lp = LabelPropagation(kernel="rbf", gamma=gamma, max_iter=100000, tol=1e-13).fit(Xs, ys)
Fu = harmonic(T, Y0, unl); Fu = Fu / Fu.sum(1, keepdims=True)
print(f"   LabelPropagation(rbf) n_iter_ {lp.n_iter_}; max |label_distributions_ - closed form| {np.max(np.abs(lp.label_distributions_[unl] - Fu)):.2e}")
report("LabelPropagation(rbf): label_distributions_ on unlabeled rows = harmonic fixed point (I - T_uu)^-1 T_ul Y_l with T = row-normalised rbf kernel (abs 1e-8)", allclose(lp.label_distributions_[unl], Fu, 1e-6, 1e-8))
report("LabelPropagation: labeled rows are clamped to their one-hot label; rows sum to 1; transduction_ = argmax", allclose(lp.label_distributions_[~unl], Y0[~unl], 1e-12) and allclose(lp.label_distributions_.sum(1), np.ones(40), 1e-12) and np.array_equal(lp.transduction_, lp.classes_[np.argmax(lp.label_distributions_, 1)]))
report("LabelPropagation.predict_proba(X_train) = row-normalised K(X, X_train) . label_distributions_ (rbf, documented 'transduction' note: not equal to transduction_)", allclose(lp.predict_proba(Xs), (W @ lp.label_distributions_) / (W @ lp.label_distributions_).sum(1, keepdims=True), 1e-9))
# knn kernel
D2 = ((Xs[:, None, :] - Xs[None, :, :]) ** 2).sum(-1); kNN = 5
Wk = np.zeros((40, 40))
for i in range(40): Wk[i, np.argsort(D2[i], kind="stable")[:kNN]] = 1
Tk = Wk / Wk.sum(1, keepdims=True)
lpk = LabelPropagation(kernel="knn", n_neighbors=kNN, max_iter=100000, tol=1e-13).fit(Xs, ys)
Fuk = harmonic(Tk, Y0, unl); Fuk = Fuk / Fuk.sum(1, keepdims=True)
report("LabelPropagation(knn, n_neighbors=5): T = row-normalised connectivity graph of the 5 nearest neighbours *including the point itself*; fixed point matches (abs 1e-8)", allclose(lpk.label_distributions_[unl], Fuk, 1e-6, 1e-8), f"(max diff {np.max(np.abs(lpk.label_distributions_[unl] - Fuk)):.2e})")
# convergence bookkeeping: replicate the iteration exactly
def lp_iterate(T, Y0, unl, tol, max_iter):
    Fd = Y0.copy(); Fd[unl] = 0; prev = np.zeros_like(Fd); n_iter = 0
    for it in range(max_iter):
        n_iter = it
        if np.abs(Fd - prev).sum() < tol: return Fd, n_iter, True
        prev = Fd; Fd = T @ Fd; Fd = Fd / np.where(Fd.sum(1, keepdims=True) == 0, 1, Fd.sum(1, keepdims=True)); Fd = np.where(unl[:, None], Fd, Y0)
    return Fd, n_iter + 1, False
Fd, nit, conv = lp_iterate(T, Y0, unl, 1e-3, 1000); lp3 = LabelPropagation(kernel="rbf", gamma=gamma, tol=1e-3, max_iter=1000).fit(Xs, ys)
report("LabelPropagation(tol=1e-3): n_iter_ and label_distributions_ equal a plain re-implementation of the iteration (stop when L1 change < tol)", lp3.n_iter_ == nit and allclose(lp3.label_distributions_, Fd / Fd.sum(1, keepdims=True), 1e-9), f"(n_iter_ {lp3.n_iter_} vs {nit})")
with warnings.catch_warnings(record=True) as wl:
    warnings.simplefilter("always"); lp1 = LabelPropagation(kernel="rbf", gamma=gamma, max_iter=2, tol=0).fit(Xs, ys)
report("LabelPropagation(max_iter=2, tol=0): ConvergenceWarning and n_iter_ == max_iter", any(w.category is ConvergenceWarning for w in wl) and lp1.n_iter_ == 2)
# LabelSpreading
W0 = W.copy(); np.fill_diagonal(W0, 0); dS = W0.sum(1); S = W0 / np.sqrt(np.outer(dS, dS))
for alpha in (0.2, 0.8):
    ls = LabelSpreading(kernel="rbf", gamma=gamma, alpha=alpha, max_iter=100000, tol=1e-13).fit(Xs, ys)
    Fs = (1 - alpha) * np.linalg.solve(np.eye(40) - alpha * S, Y0); Fs = Fs / Fs.sum(1, keepdims=True)
    print(f"   LabelSpreading(alpha={alpha}) n_iter_ {ls.n_iter_}; max |diff to (1-a)(I - aS)^-1 Y| {np.max(np.abs(ls.label_distributions_ - Fs)):.2e}")
    report(f"LabelSpreading(alpha={alpha}): label_distributions_ = row-normalised (I - alpha S)^-1 Y with S = D^-1/2 W D^-1/2, zero diagonal, D from the off-diagonal rbf weights (abs 1e-8)", allclose(ls.label_distributions_, Fs, 1e-6, 1e-8))
report("LabelSpreading transduction_ on unlabeled rows recovers the two-blob labels", np.mean(ls.transduction_[unl] == ys_true[unl]) > 0.95, f"({np.mean(ls.transduction_[unl] == ys_true[unl]) * 100:.0f} % correct)")
lsk = LabelSpreading(kernel="knn", n_neighbors=kNN, alpha=0.2, max_iter=100000, tol=1e-13).fit(Xs, ys)
Wk0 = Wk.copy(); np.fill_diagonal(Wk0, 0); dk = Wk0.sum(0); wk_ = np.where(dk == 0, 1.0, np.sqrt(dk)); Sk = Wk0 / np.outer(wk_, wk_); Fsk = np.linalg.solve(np.eye(40) - 0.2 * Sk, Y0); Fsk /= Fsk.sum(1, keepdims=True)
print(f"   LabelSpreading(knn): kNN graph asymmetric (|W - W^T| sum {np.abs(Wk0 - Wk0.T).sum():.0f}); nodes with zero in-degree {int((dk == 0).sum())}")
report("LabelSpreading(knn): closed form with S = D^-1/2 W D^-1/2 where D holds the *column* sums (in-degree) of the asymmetric kNN graph and isolated columns get degree 1 (scipy normalized Laplacian, axis=0)", allclose(lsk.label_distributions_, Fsk, 1e-6, 1e-8), f"(max diff {np.max(np.abs(lsk.label_distributions_ - Fsk)):.2e})")
# SelfTrainingClassifier
def st_kw(est, **kw):
    name = "estimator" if "estimator" in inspect.signature(SelfTrainingClassifier).parameters else "base_estimator"
    return SelfTrainingClassifier(**{name: est}, **kw)
def self_train_ref(X, y, make, threshold=None, k_best=None, max_iter=10):
    y = y.copy(); has = y != -1; labeled_iter = np.where(has, 0, -1); n_iter = 0; term = None
    while not np.all(has) and (max_iter is None or n_iter < max_iter):
        n_iter += 1; est = make().fit(X[has], y[has]); prob = est.predict_proba(X[~has]); mx = prob.max(1); pred = est.classes_[prob.argmax(1)]
        if threshold is not None: sel = np.flatnonzero(mx > threshold)
        else:
            k = min(k_best, len(mx)); sel = np.argsort(-mx, kind="stable")[:k]
        full = np.flatnonzero(~has)[sel]; y[full] = pred[sel]; has[full] = True; labeled_iter[full] = n_iter
        if len(full) == 0: term = "no_change"; break
    if n_iter == max_iter: term = "max_iter"
    if np.all(has): term = "all_labeled"
    return y, labeled_iter, n_iter, term
rs = np.random.RandomState(15); Xst = rs.randn(120, 2); yst_true = (Xst[:, 0] + 0.5 * Xst[:, 1] > 0).astype(int); yst = yst_true.copy(); yst[rs.rand(120) < 0.8] = -1
for kw, tag in (({"threshold": 0.9}, "threshold=0.9"), ({"criterion": "k_best", "k_best": 7, "max_iter": 4}, "k_best=7, max_iter=4"), ({"threshold": 0.75, "max_iter": None}, "threshold=0.75, max_iter=None")):
    stc = st_kw(LR(), **kw).fit(Xst, yst)
    ref = self_train_ref(Xst, yst, LR, threshold=kw.get("threshold") if kw.get("criterion", "threshold") == "threshold" else None, k_best=kw.get("k_best"), max_iter=kw.get("max_iter", 10))
    print(f"   SelfTraining({tag}): n_iter_ {stc.n_iter_}, termination {stc.termination_condition_}, labeled per round {np.bincount(stc.labeled_iter_[stc.labeled_iter_ >= 0]).tolist()}")
    report(f"SelfTrainingClassifier({tag}): transduction_, labeled_iter_, n_iter_ and termination_condition_ equal a plain re-implementation (select max proba {'> threshold' if 'k_best' not in kw else 'top k_best'} each round)", np.array_equal(stc.transduction_, ref[0]) and np.array_equal(stc.labeled_iter_, ref[1]) and stc.n_iter_ == ref[2] and stc.termination_condition_ == ref[3], f"(got {stc.n_iter_}/{stc.termination_condition_}, ref {ref[2]}/{ref[3]})")
stc = st_kw(LR(), threshold=0.9).fit(Xst, yst)
report("SelfTrainingClassifier: labeled_iter_ is 0 for initially labeled rows, -1 for never-labeled rows, and predict/predict_proba delegate to the final estimator_", np.all(stc.labeled_iter_[yst != -1] == 0) and np.all((stc.labeled_iter_ == -1) == (stc.transduction_ == -1)) and allclose(stc.predict_proba(Xst[:5]), getattr(stc, "estimator_", getattr(stc, "base_estimator_", None)).predict_proba(Xst[:5])))
try: st_kw(LR(), criterion="k_best", k_best=1000).fit(Xst, yst); kb_ok = True
except ValueError: kb_ok = False
report("SelfTrainingClassifier(k_best larger than the unlabeled count) fits with a warning rather than raising", kb_ok)
print("done")
