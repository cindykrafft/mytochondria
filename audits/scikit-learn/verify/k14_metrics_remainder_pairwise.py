#!/usr/bin/env python
"""k14: the rest of sklearn.metrics against exact recomputations (Fraction / mpmath /
plain-Python reference implementations of the DOCUMENTED formulas): F-beta and the
'samples' average, PRF with labels subsets / pos_label / zero_division, jaccard,
hamming, zero-one, brier (incl. 1.7+ multiclass), hinge (binary + Crammer-Singer),
top-k with ties, classification_report numbers, multilabel_confusion_matrix,
class_likelihood_ratios, d2_log_loss, weighted MCC / kappa / balanced accuracy,
log_loss labels + eps history; DCG/NDCG tie averaging, LRAP, ranking loss, coverage,
det_curve, multilabel AUC / AP averages; the regression remainder (MSLE, RMSLE,
median AE incl. weighted, max_error, pinball, Tweedie family, D2 scores, MAPE
epsilon, r2 / explained variance force_finite, RMSE multioutput); clustering
remainder (contingency, pair confusion, consensus_score, V-measure beta, degenerate
label counts, silhouette sample_size); every pairwise distance / kernel, the
DistanceMetric class, chunked / argmin helpers; scorers."""
import sys, random, math, warnings, itertools, collections, re
sys.path.insert(0, ".")
from _synth import *
import numpy as np, mpmath
from fractions import Fraction as F
from sklearn import metrics
from sklearn.metrics import pairwise as pw
banner(); rng = random.Random(14); warnings.filterwarnings("ignore")
mpmath.mp.dps = 40
V = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
mp = lambda x: mpmath.mpf(x.numerator) / x.denominator if isinstance(x, F) else mpmath.mpf(x)

def raises(exc, f, *a, **k):
    try: f(*a, **k)
    except exc: return True
    except Exception: return False
    return False
def fmean(xs): xs = list(xs); return sum(xs) / len(xs)
def wmean(xs, ws): return sum(x * w for x, w in zip(xs, ws)) / sum(ws)
def isnan(x):
    try: return math.isnan(float(x))
    except Exception: return False
def mat_close(A, B, rel=1e-12, abs_=1e-12):
    A = np.asarray(A, float); B = np.asarray(B, float)
    return A.shape == B.shape and all(close(a, b, rel, abs_) for a, b in zip(A.ravel(), B.ravel()))

# =====================================================================================
# A. multilabel set-wise metrics
# =====================================================================================
print("---- classification: multilabel set-wise metrics")
n, L = 40, 4
Yt = [[1 if rng.random() < 0.4 else 0 for _ in range(L)] for _ in range(n)]
Yp = [[(t if rng.random() < 0.7 else 1 - t) for t in row] for row in Yt]
Yt[0] = [0] * L; Yp[0] = [0] * L          # both empty
Yt[1] = [0] * L; Yp[1] = [1, 0, 0, 0]     # true empty, pred non-empty
Yt[2] = [1, 1, 0, 0]; Yp[2] = [0] * L     # pred empty
Yt[3] = [0] * L; Yp[3] = [0] * L          # both empty again
YT, YP = np.array(Yt), np.array(Yp)
def counts(t, p, w=None):
    w = [1] * len(t) if w is None else w
    tp = sum(wi for a, b, wi in zip(t, p, w) if a and b); fp = sum(wi for a, b, wi in zip(t, p, w) if b and not a)
    fn = sum(wi for a, b, wi in zip(t, p, w) if a and not b); tn = sum(w) - tp - fp - fn
    return tp, fp, fn, tn
lab_counts = [counts([r[l] for r in Yt], [r[l] for r in Yp]) for l in range(L)]
samp_counts = [counts(t, p) for t, p in zip(Yt, Yp)]
def div(num, den, zd): return F(num) / F(den) if den else zd
def prf_from(c, beta, zd):
    tp, fp, fn, tn = c; b2 = beta * beta
    P = div(tp, tp + fp, zd); R = div(tp, tp + fn, zd)
    Fb = zd if (tp + fp == 0 and tp + fn == 0) else div((1 + b2) * tp, (1 + b2) * tp + b2 * fn + fp, zd)
    return P, R, Fb
def avg(vals, weights=None):
    """average that excludes NaN entries (documented for zero_division=np.nan)."""
    weights = [1] * len(vals) if weights is None else weights
    pairs = [(v, w) for v, w in zip(vals, weights) if not isnan(v)]
    if not pairs or sum(w for _, w in pairs) == 0: return float("nan")
    return sum(v * w for v, w in pairs) / sum(w for _, w in pairs)
def prf_avg(cs, beta, zd, average, which):
    idx = "PRF".index(which)
    if average == "micro":
        tot = tuple(sum(c[i] for c in cs) for i in range(4)); return prf_from(tot, beta, zd)[idx]
    per = [prf_from(c, beta, zd)[idx] for c in cs]
    if average is None: return per
    if average == "weighted": return avg(per, [c[0] + c[2] for c in cs])
    return avg(per)

for beta in [F(1, 2), F(1), F(2)]:
    for average in ["macro", "micro", "weighted"]:
        got = metrics.fbeta_score(YT, YP, beta=float(beta), average=average, zero_division=0)
        want = prf_avg(lab_counts, beta, F(0), average, "F")
        report(f"fbeta_score(beta={float(beta)}, average='{average}') multilabel = (1+b^2)tp/((1+b^2)tp+b^2 fn+fp) per label, averaged ({float(want):.6f})", close(got, want))
    got = metrics.fbeta_score(YT, YP, beta=float(beta), average="samples", zero_division=0)
    want = prf_avg(samp_counts, beta, F(0), "samples", "F")
    report(f"fbeta_score(beta={float(beta)}, average='samples') = mean over samples of the per-sample F-beta ({float(want):.6f})", close(got, want))
got = metrics.fbeta_score(YT, YP, beta=2, average=None, zero_division=0); want = prf_avg(lab_counts, F(2), F(0), None, "F")
report("fbeta_score(average=None) returns the per-label array", all(close(g, w) for g, w in zip(got, want)))
P_ = prf_avg(lab_counts, F(1), F(0), "macro", "P")
report("fbeta_score(beta=0, average='macro') 'considers only precision' (docstring)", close(metrics.fbeta_score(YT, YP, beta=0, average="macro", zero_division=0), P_))
if V >= (1, 3):
    R_ = prf_avg(lab_counts, F(1), F(0), "macro", "R")
    report("fbeta_score(beta=inf) 'considers only recall'", close(metrics.fbeta_score(YT, YP, beta=float("inf"), average="macro", zero_division=0), R_))
for zd in [0, 1]:
    for which, fn_ in [("P", metrics.precision_score), ("R", metrics.recall_score), ("F", metrics.f1_score)]:
        got = fn_(YT, YP, average="samples", zero_division=zd); want = prf_avg(samp_counts, F(1), F(zd), "samples", which)
        report(f"{fn_.__name__}(average='samples', zero_division={zd}): samples with empty true AND predicted sets take the zero_division value ({float(want):.6f})", close(got, want), f"(got {got:.6f})")
if V >= (1, 3):
    for which, fn_ in [("P", metrics.precision_score), ("R", metrics.recall_score), ("F", metrics.f1_score)]:
        got = fn_(YT, YP, average="samples", zero_division=np.nan); want = prf_avg(samp_counts, F(1), float("nan"), "samples", which)
        report(f"{fn_.__name__}(average='samples', zero_division=np.nan): 'such values will be excluded from the average' ({float(want):.6f})", close(got, want), f"(got {got:.6f})")
    got = metrics.f1_score(YT, YP, average="macro", zero_division=np.nan)
    report("f1_score(average='macro', zero_division=nan) equals the plain macro (no label has empty true+pred)", close(got, prf_avg(lab_counts, F(1), float("nan"), "macro", "F")))
w = [rng.randint(1, 4) for _ in range(n)]; W = [rng.randint(1, 4) for _ in range(60)]
got = metrics.f1_score(YT, YP, average="samples", sample_weight=w, zero_division=0)
report("f1_score(average='samples', sample_weight) = weighted mean of per-sample F1", close(got, avg([prf_from(c, F(1), F(0))[2] for c in samp_counts], w)))
lab_counts_w = [counts([r[l] for r in Yt], [r[l] for r in Yp], w) for l in range(L)]
for average in ["macro", "micro", "weighted"]:
    got = metrics.f1_score(YT, YP, average=average, sample_weight=w, zero_division=0)
    report(f"f1_score(average='{average}', sample_weight): tp/fp/fn are weight sums", close(got, prf_avg(lab_counts_w, F(1), F(0), average, "F")))

# ---- multiclass PRF with labels subsets and pos_label
print("---- classification: PRF labels / pos_label, jaccard")
ym = [rng.choice([0, 1, 2, 3]) for _ in range(60)]; pm = [(y if rng.random() < 0.6 else rng.choice([0, 1, 2, 3])) for y in ym]
cm = confusion(ym, pm, [0, 1, 2, 3])
def mc_counts(l, c=cm, labels=(0, 1, 2, 3), N=60):
    tp = c[(l, l)]; fp = sum(c[(a, l)] for a in labels if a != l); fn = sum(c[(l, b)] for b in labels if b != l)
    return (tp, fp, fn, N - tp - fp - fn)
prfs = metrics.precision_recall_fscore_support
p, r, f, s = prfs(ym, pm, labels=[3, 1], average=None)
want = [prf_from(mc_counts(l), F(1), F(0)) for l in [3, 1]]
report("precision_recall_fscore_support(labels=[3,1], average=None): rows 'in the order given' with support = true counts",
       all(close(p[i], want[i][0]) and close(r[i], want[i][1]) and close(f[i], want[i][2]) for i in range(2)) and list(s) == [sum(cm[(3, b)] for b in range(4)), sum(cm[(1, b)] for b in range(4))])
for average in ["macro", "micro", "weighted"]:
    p, r, f, _ = prfs(ym, pm, labels=[3, 1], average=average)
    cs = [mc_counts(3), mc_counts(1)]
    want = [prf_avg(cs, F(1), F(0), average, wch) for wch in "PRF"]
    report(f"precision_recall_fscore_support(labels=[3,1], average='{average}'): computed over the selected labels only (micro sums their tp/fp/fn)", close(p, want[0]) and close(r, want[1]) and close(f, want[2]), f"({p:.6f}, {r:.6f}, {f:.6f})")
p, r, f, s = prfs(ym, pm, labels=[1, 9], average=None, zero_division=0)
report("labels containing an absent class (9): 'assigned 0 samples' -> support 0 and P=R=F=zero_division", s[1] == 0 and p[1] == 0 and r[1] == 0 and f[1] == 0)
yb = ['a' if rng.random() < 0.5 else 'b' for _ in range(50)]; pb = [(y if rng.random() < 0.7 else ('a' if y == 'b' else 'b')) for y in yb]
cb = confusion(yb, pb, ['a', 'b'])
for pos, neg in [('a', 'b'), ('b', 'a')]:
    tp = cb[(pos, pos)]; fp = cb[(neg, pos)]; fn = cb[(pos, neg)]
    P, R, Fb = prf_from((tp, fp, fn, 50 - tp - fp - fn), F(1), F(0))
    p, r, f, s = prfs(yb, pb, pos_label=pos, average="binary")
    report(f"precision_recall_fscore_support(average='binary', pos_label='{pos}') reports the class '{pos}' only", close(p, P) and close(r, R) and close(f, Fb) and s is None)
report("pos_label='z' not present with two classes raises ValueError", raises(ValueError, prfs, yb, pb, pos_label='z', average='binary'))
p_mac = prfs(yb, pb, pos_label='a', average="macro")[0]
report("pos_label is ignored when average != 'binary' (macro over both classes)", close(p_mac, prf_avg([(cb[('a','a')], cb[('b','a')], cb[('a','b')], 0), (cb[('b','b')], cb[('a','b')], cb[('b','a')], 0)], F(1), F(0), "macro", "P")))

# ---- jaccard_score
def jac(c, zd): tp, fp, fn, tn = c; return div(tp, tp + fp + fn, zd)
def jac_avg(cs, zd, average):
    if average == "micro": return jac(tuple(sum(c[i] for c in cs) for i in range(4)), zd)
    per = [jac(c, zd) for c in cs]
    if average is None: return per
    if average == "weighted": return avg(per, [c[0] + c[2] for c in cs])
    return avg(per)
yb01 = [1 if y == 'a' else 0 for y in yb]; pb01 = [1 if y == 'a' else 0 for y in pb]
for pos in [0, 1]:
    c = counts([int(y == pos) for y in yb01], [int(y == pos) for y in pb01])
    report(f"jaccard_score binary pos_label={pos} = tp/(tp+fp+fn) for that class", close(metrics.jaccard_score(yb01, pb01, pos_label=pos), jac(c, F(0))))
mcs = [mc_counts(l) for l in range(4)]
got = metrics.jaccard_score(ym, pm, average=None)
report("jaccard_score multiclass average=None = per-class tp/(tp+fp+fn) (one-vs-rest)", all(close(g, w) for g, w in zip(got, jac_avg(mcs, F(0), None))))
for average in ["macro", "micro", "weighted"]:
    report(f"jaccard_score multiclass average='{average}'", close(metrics.jaccard_score(ym, pm, average=average), jac_avg(mcs, F(0), average)))
report("jaccard_score multiclass average='micro' with labels=[0,2] restricts the sums to those classes", close(metrics.jaccard_score(ym, pm, average="micro", labels=[0, 2]), jac_avg([mc_counts(0), mc_counts(2)], F(0), "micro")))
for average in ["macro", "micro", "weighted"]:
    report(f"jaccard_score multilabel average='{average}'", close(metrics.jaccard_score(YT, YP, average=average, zero_division=0), jac_avg(lab_counts, F(0), average)))
for zd in [0, 1]:
    got = metrics.jaccard_score(YT, YP, average="samples", zero_division=zd)
    report(f"jaccard_score(average='samples', zero_division={zd}) = mean over samples of |y & yhat| / |y | yhat|, empty union -> zero_division", close(got, jac_avg(samp_counts, F(zd), "samples")))
got = metrics.jaccard_score(YT, YP, average="samples", zero_division=0, sample_weight=w)
report("jaccard_score(average='samples', sample_weight) weighted mean", close(got, avg([jac(c, F(0)) for c in samp_counts], w)))
if V >= (1, 3):
    doc_nan = "np.nan" in (metrics.jaccard_score.__doc__ or "").split("zero_division :")[1][:60]
    try:
        got = metrics.jaccard_score(YT, YP, average="samples", zero_division=np.nan)
        report("jaccard_score(average='samples', zero_division=np.nan): docstring only says 'value to return' (no exclusion rule) -> plain average is NaN", isnan(got), f"(got {got}; the NaN-excluded mean would be {float(jac_avg(samp_counts, float('nan'), 'samples')):.6f})")
    except Exception as e:
        report(f"jaccard_score accepts zero_division=np.nan as its docstring lists ('{{\"warn\", 0.0, 1.0, np.nan}}' listed: {doc_nan})", not doc_nan, f"({type(e).__name__}: {str(e)[:110]})")

# ---- hamming / zero-one / accuracy
print("---- classification: hamming, zero-one, subset accuracy")
diff = sum(1 for t, p in zip(Yt, Yp) for a, b in zip(t, p) if a != b)
report("hamming_loss multilabel = (# label entries that differ) / (n_samples * n_labels)", close(metrics.hamming_loss(YT, YP), F(diff, n * L)))
diffw = sum(w[i] * sum(1 for a, b in zip(Yt[i], Yp[i]) if a != b) for i in range(n))
report("hamming_loss multilabel with sample_weight = sum_i w_i diff_i / (n_labels * sum w)", close(metrics.hamming_loss(YT, YP, sample_weight=w), F(diffw, L * sum(w))))
report("hamming_loss multiclass = fraction of misclassified samples", close(metrics.hamming_loss(ym, pm), F(sum(a != b for a, b in zip(ym, pm)), 60)))
wm = [rng.randint(1, 3) for _ in ym]
report("hamming_loss multiclass with sample_weight = weighted fraction", close(metrics.hamming_loss(ym, pm, sample_weight=wm), F(sum(wi for a, b, wi in zip(ym, pm, wm) if a != b), sum(wm))))
zol = F(sum(1 for t, p in zip(Yt, Yp) if t != p), n)
report("zero_one_loss multilabel = fraction of samples whose label set does not exactly match", close(metrics.zero_one_loss(YT, YP), zol))
report("zero_one_loss(normalize=False) = number of misclassified samples", metrics.zero_one_loss(YT, YP, normalize=False) == zol * n)
report("zero_one_loss with sample_weight = weighted fraction", close(metrics.zero_one_loss(YT, YP, sample_weight=w), F(sum(wi for t, p, wi in zip(Yt, Yp, w) if t != p), sum(w))))
report("accuracy_score multilabel = subset accuracy = 1 - zero_one_loss", close(metrics.accuracy_score(YT, YP), 1 - zol))
report("accuracy_score(normalize=False) multilabel = number of exactly matched samples", metrics.accuracy_score(YT, YP, normalize=False) == n - zol * n)
report("hamming_loss <= zero_one_loss (user guide: 'upper bounded by the zero-one loss')", metrics.hamming_loss(YT, YP) <= metrics.zero_one_loss(YT, YP))

# ---- Brier
print("---- classification: brier, hinge, top-k")
yb01 = [1 if rng.random() < 0.4 else 0 for _ in range(50)]; pr = [rng.randint(0, 16) / 16 for _ in yb01]
bs = fmean((F(y) - F(p)) ** 2 for y, p in zip(yb01, pr))
brier = metrics.brier_score_loss
report(f"brier_score_loss binary = mean (y - p)^2 ({float(bs):.6f})", close(brier(yb01, pr), bs))
report("brier_score_loss(pos_label=0) on 1 - p gives the same value", close(brier(yb01, [1 - p for p in pr], pos_label=0), bs))
report("brier_score_loss with sample_weight", close(brier(yb01, pr, sample_weight=W[:50]), wmean([(F(y) - F(p)) ** 2 for y, p in zip(yb01, pr)], W[:50])))
ystr = ['ham' if y else 'spam' for y in yb01]
report("brier string labels with pos_label='ham'", close(brier(ystr, pr, pos_label='ham'), bs))
report("brier string labels without pos_label raises ValueError ('an error will be raised')", raises(ValueError, brier, ystr, pr))
report("brier y_true in {2,5}: pos_label 'defaults to the greater label' 5", close(brier([5 if y else 2 for y in yb01], pr), bs))
report("brier y_true in {-1,1}: pos_label defaults to 1", close(brier([1 if y else -1 for y in yb01], pr), bs))
report("brier y_proba outside [0,1] raises ValueError", raises(ValueError, brier, yb01, [1.5] + pr[1:]))
if V >= (1, 7):
    y3 = [rng.randint(0, 2) for _ in range(45)]
    P3 = []
    for _ in y3:
        a = rng.randint(1, 8); b = rng.randint(1, 16 - a - 1); P3.append([F(a, 16), F(b, 16), F(16 - a - b, 16)])
    P3f = [[float(v) for v in row] for row in P3]
    bs3 = fmean(sum((F(int(y == c)) - P3[i][c]) ** 2 for c in range(3)) for i, y in enumerate(y3))
    report(f"brier_score_loss multiclass (1.7+) = mean sum_c (y_c - p_c)^2, not halved under scale_by_half='auto' ({float(bs3):.6f})", close(brier(y3, P3f), bs3))
    report("brier multiclass scale_by_half=True halves it", close(brier(y3, P3f, scale_by_half=True), bs3 / 2))
    report("brier binary scale_by_half=False = 2 x the halved binary score = sum over both classes", close(brier(yb01, pr, scale_by_half=False), 2 * bs))
    report("brier 2-column y_proba for a binary target is halved ('auto' = binary)", close(brier(yb01, np.c_[1 - np.array(pr), pr]), bs))
    y3m = [y if y != 2 else 0 for y in y3]
    bs3m = fmean(sum((F(int(y == c)) - P3[i][c]) ** 2 for c in range(3)) for i, y in enumerate(y3m))
    report("brier multiclass with labels=[0,1,2] when y_true lacks a class", close(brier(y3m, P3f, labels=[0, 1, 2]), bs3m))
    report("brier multiclass without labels when y_true lacks a class raises ValueError", raises(ValueError, brier, y3m, P3f))
    try:
        d2b = metrics.d2_brier_score(yb01, pr)
        pbar = fmean(F(y) for y in yb01)
        want = 1 - bs / fmean((F(y) - pbar) ** 2 for y in yb01)
        report(f"d2_brier_score binary = 1 - BS / BS(null = class proportion) ({float(want):.6f})", close(d2b, want))
    except AttributeError:
        print("   d2_brier_score not in this build")

# ---- hinge  (fresh generator: the version-gated brier block above consumes draws only on 1.7+)
rng = random.Random(1402)
yh = [1 if rng.random() < 0.5 else 0 for _ in range(40)]; dh = [rng.randint(-8, 8) / 4 for _ in yh]
hl = fmean(max(F(0), 1 - F(2 * y - 1) * F(d)) for y, d in zip(yh, dh))
report(f"hinge_loss binary = mean max(0, 1 - y*d), y in {{-1,+1}} ({float(hl):.6f})", close(metrics.hinge_loss(yh, dh), hl))
report("hinge_loss binary with sample_weight", close(metrics.hinge_loss(yh, dh, sample_weight=W[:40]), wmean([max(F(0), 1 - F(2 * y - 1) * F(d)) for y, d in zip(yh, dh)], W[:40])))
report("hinge_loss binary string labels: 'positive label being greater than the negative label' ('b' > 'a')", close(metrics.hinge_loss(['b' if y else 'a' for y in yh], dh), hl))
ymc = [rng.randint(0, 2) for _ in range(40)]; Dmc = [[rng.randint(-8, 8) / 4 for _ in range(3)] for _ in ymc]
hmc = fmean(max(F(0), 1 - (F(D[y]) - max(F(D[j]) for j in range(3) if j != y))) for y, D in zip(ymc, Dmc))
report(f"hinge_loss multiclass = mean max(0, 1 + max_(j!=y) w_j - w_y) (Crammer-Singer, user guide) ({float(hmc):.6f})", close(metrics.hinge_loss(ymc, Dmc), hmc))
ymc2 = [y if y != 2 else 0 for y in ymc]
hmc2 = fmean(max(F(0), 1 - (F(D[y]) - max(F(D[j]) for j in range(3) if j != y))) for y, D in zip(ymc2, Dmc))
report("hinge_loss multiclass with a class absent from y_true: raises without labels=, exact with labels=[0,1,2]", raises(ValueError, metrics.hinge_loss, ymc2, Dmc) and close(metrics.hinge_loss(ymc2, Dmc, labels=[0, 1, 2]), hmc2))

# ---- top-k
ytk = [rng.randint(0, 3) for _ in range(50)]; Stk = [[rng.randint(0, 5) / 5 for _ in range(4)] for _ in ytk]
def topk_ref(y, S, k, w=None):
    w = [1] * len(y) if w is None else w; hits = 0
    for yi, s, wi in zip(y, S, w):
        order = sorted(range(len(s)), key=lambda j: (s[j], j), reverse=True)   # ties: 'labels with the highest indices will be chosen first'
        hits += wi * (yi in order[:k])
    return F(hits, sum(w))
for k in [1, 2, 3]:
    report(f"top_k_accuracy_score(k={k}) with tied scores: hit iff the true label is among the top k, ties broken toward the highest index ({float(topk_ref(ytk, Stk, k)):.4f})", close(metrics.top_k_accuracy_score(ytk, Stk, k=k), topk_ref(ytk, Stk, k)))
report("top_k_accuracy_score(normalize=False) = number of hits", metrics.top_k_accuracy_score(ytk, Stk, k=2, normalize=False) == topk_ref(ytk, Stk, 2) * 50)
report("top_k_accuracy_score with sample_weight", close(metrics.top_k_accuracy_score(ytk, Stk, k=2, sample_weight=W[:50]), topk_ref(ytk, Stk, 2, W[:50])))
report("top_k_accuracy_score(k >= n_classes) = 1.0 ('will result in a perfect score')", metrics.top_k_accuracy_score(ytk, Stk, k=4) == 1.0)
ytk3 = [y if y != 3 else 0 for y in ytk]
report("top_k multiclass with a class absent from y_true: raises without labels=, exact with labels=[0,1,2,3]", raises(ValueError, metrics.top_k_accuracy_score, ytk3, Stk, k=2) and close(metrics.top_k_accuracy_score(ytk3, Stk, k=2, labels=[0, 1, 2, 3]), topk_ref(ytk3, Stk, 2)))
report("top_k labels in a non-sorted order raise ValueError (implementation check 'Parameter labels must be ordered')", raises(ValueError, metrics.top_k_accuracy_score, ytk, Stk, k=2, labels=[1, 0, 2, 3]))
sb = [rng.randint(0, 10) / 10 for _ in yb01]
report("top_k binary k=1 with scores in [0,1]: predicted positive iff score > 0.5", close(metrics.top_k_accuracy_score(yb01, sb, k=1), F(sum(int(s > 0.5) == y for y, s in zip(yb01, sb)), 50)))
sb2 = [s * 4 - 2 for s in sb]
report("top_k binary k=1 with decision scores: threshold 0", close(metrics.top_k_accuracy_score(yb01, sb2, k=1), F(sum(int(s > 0) == y for y, s in zip(yb01, sb2)), 50)))
report("top_k binary k=2 = 1.0", metrics.top_k_accuracy_score(yb01, sb, k=2) == 1.0)

# ---- classification_report, multilabel_confusion_matrix
print("---- classification: report, multilabel confusion, likelihood ratios, d2_log_loss")
rep = metrics.classification_report(ym, pm, output_dict=True, zero_division=0)
okc = True
for l in range(4):
    P, R, Fb = prf_from(mc_counts(l), F(1), F(0)); d = rep[str(l)]
    okc &= close(d["precision"], P) and close(d["recall"], R) and close(d["f1-score"], Fb) and d["support"] == sum(cm[(l, b)] for b in range(4))
report("classification_report(output_dict=True): per-class precision/recall/f1/support exact", okc)
acc = F(sum(a == b for a, b in zip(ym, pm)), 60)
report("classification_report 'accuracy' entry = accuracy_score", close(rep["accuracy"], acc))
report("classification_report 'macro avg' = unweighted means", all(close(rep["macro avg"][k], prf_avg(mcs, F(1), F(0), "macro", wch)) for k, wch in [("precision", "P"), ("recall", "R"), ("f1-score", "F")]) and rep["macro avg"]["support"] == 60)
report("classification_report 'weighted avg' = support-weighted means", all(close(rep["weighted avg"][k], prf_avg(mcs, F(1), F(0), "weighted", wch)) for k, wch in [("precision", "P"), ("recall", "R"), ("f1-score", "F")]))
txt = metrics.classification_report(ym, pm, digits=3, zero_division=0)
P0 = prf_from(mc_counts(0), F(1), F(0))[0]
report("classification_report text prints the class-0 precision with digits=3", f"{float(P0):.3f}" in txt.splitlines()[2] and "accuracy" in txt)
rep2 = metrics.classification_report(ym, pm, labels=[0, 1], output_dict=True, zero_division=0)
report("classification_report(labels=[0,1]) reports 'micro avg' (not 'accuracy') over the selected labels", "micro avg" in rep2 and "accuracy" not in rep2 and close(rep2["micro avg"]["precision"], prf_avg([mc_counts(0), mc_counts(1)], F(1), F(0), "micro", "P")))
repml = metrics.classification_report(YT, YP, output_dict=True, zero_division=0)
report("classification_report multilabel has a 'samples avg' row = 'samples' average", "samples avg" in repml and close(repml["samples avg"]["f1-score"], prf_avg(samp_counts, F(1), F(0), "samples", "F")))
M = metrics.multilabel_confusion_matrix(YT, YP)
report("multilabel_confusion_matrix per label = [[tn, fp], [fn, tp]]", M.tolist() == [[[tn, fp], [fn, tp]] for (tp, fp, fn, tn) in lab_counts])
Ms = metrics.multilabel_confusion_matrix(YT, YP, samplewise=True)
report("multilabel_confusion_matrix(samplewise=True) = one 2x2 per sample", Ms.tolist() == [[[tn, fp], [fn, tp]] for (tp, fp, fn, tn) in samp_counts])
Ml = metrics.multilabel_confusion_matrix(YT, YP, labels=[2, 0])
report("multilabel_confusion_matrix(labels=[2,0]) 'in the order specified in labels'", Ml.tolist() == [[[lab_counts[l][3], lab_counts[l][1]], [lab_counts[l][2], lab_counts[l][0]]] for l in [2, 0]])
Mm = metrics.multilabel_confusion_matrix(ym, pm)
report("multilabel_confusion_matrix multiclass = one-vs-rest binarisation, sorted labels", Mm.tolist() == [[[c[3], c[1]], [c[2], c[0]]] for c in mcs])
Mw = metrics.multilabel_confusion_matrix(YT, YP, sample_weight=w)
report("multilabel_confusion_matrix with sample_weight sums the weights", mat_close(Mw, [[[tn, fp], [fn, tp]] for (tp, fp, fn, tn) in lab_counts_w]))

# ---- class_likelihood_ratios
def clr_ref(y, p, w=None):
    tp, fp, fn, tn = counts(y, p, w); sens = F(tp, tp + fn); spec = F(tn, tn + fp)
    return sens / (1 - spec), (1 - sens) / spec
if V >= (1, 2):
    clr = metrics.class_likelihood_ratios
    pcl = [(y if rng.random() < 0.7 else 1 - y) for y in yb01]
    want = clr_ref(yb01, pcl); got = clr(yb01, pcl)
    report(f"class_likelihood_ratios: LR+ = sens/(1-spec), LR- = (1-sens)/spec ({float(want[0]):.6f}, {float(want[1]):.6f})", close(got[0], want[0]) and close(got[1], want[1]))
    report("class_likelihood_ratios docstring example ([0,1,0,1,0],[1,1,0,0,0]) = (1.5, 0.75)", clr([0, 1, 0, 1, 0], [1, 1, 0, 0, 0]) == (1.5, 0.75))
    ys = ['pos' if y else 'neg' for y in yb01]; ps = ['pos' if y else 'neg' for y in pcl]
    got = clr(ys, ps, labels=['neg', 'pos'])
    report("class_likelihood_ratios(labels=[negative, positive]) selects the classes", close(got[0], want[0]) and close(got[1], want[1]))
    got = clr(ys, ps)
    wswap = clr_ref([1 - y for y in yb01], [1 - y for y in pcl])
    report("class_likelihood_ratios with string labels and no labels=: sorted order -> 'pos' is the positive class (comes after 'neg')", close(got[0], want[0]) and close(got[1], want[1]), f"(got {got}; swapped-class values would be {float(wswap[0]):.4f}, {float(wswap[1]):.4f})")
    wl = W[:50]; wantw = clr_ref(yb01, pcl, wl); got = clr(yb01, pcl, sample_weight=wl)
    report("class_likelihood_ratios with sample_weight = ratios of weighted counts", close(got[0], wantw[0]) and close(got[1], wantw[1]))
    # zero denominators
    yz = [0, 0, 1, 1, 1, 0]; pz = [0, 0, 1, 1, 0, 0]        # fp == 0, tn > 0
    got = clr(yz, pz)
    report("fp == 0: LR+ undefined -> NaN (default), LR- computed as usual ((1-sens)/spec = (1/3)/1)", isnan(got[0]) and close(got[1], F(1, 3)))
    yz2 = [0, 0, 1, 1, 1, 0]; pz2 = [1, 1, 1, 1, 0, 1]      # tn == 0
    got = clr(yz2, pz2)
    report("tn == 0: LR- undefined -> NaN, LR+ = sens/(1-spec) = (2/3)/1", isnan(got[1]) and close(got[0], F(2, 3)))
    got = clr([0, 0, 0, 0], [0, 1, 0, 1])
    report("no positive samples in y_true: both ratios NaN", isnan(got[0]) and isnan(got[1]))
    if V >= (1, 7):
        got = clr(yz, pz, replace_undefined_by=1.0)
        report("replace_undefined_by=1.0 with fp == 0: 'only the affected metric is replaced' -> LR+ = 1.0, LR- computed", got[0] == 1.0 and close(got[1], F(1, 3)))
        got = clr(yz, pz, replace_undefined_by={"LR+": np.inf, "LR-": 0.0})
        report("replace_undefined_by={'LR+': inf, 'LR-': 0.0} with fp == 0: LR+ = inf, LR- still computed", got[0] == float("inf") and close(got[1], F(1, 3)))
        got = clr(yz2, pz2, replace_undefined_by={"LR+": np.inf, "LR-": 0.0})
        report("... with tn == 0: LR- = 0.0, LR+ computed", got[1] == 0.0 and close(got[0], F(2, 3)))
        report("replace_undefined_by dict with LR- > 1 raises ValueError", raises(ValueError, clr, yz, pz, replace_undefined_by={"LR+": 1.0, "LR-": 2.0}))

# ---- d2_log_loss_score
rng = random.Random(1403)
y3 = [rng.randint(0, 2) for _ in range(45)]
P3 = []
for _ in y3:
    a = rng.randint(1, 8); b = rng.randint(1, 16 - a - 1); P3.append([F(a, 16), F(b, 16), F(16 - a - b, 16)])
P3f = [[float(v) for v in row] for row in P3]
def ll_sum(y, P, w=None):
    w = [1] * len(y) if w is None else w
    return -sum(wi * mpmath.log(mp(P[i][yi])) for i, (yi, wi) in enumerate(zip(y, w)))
def d2ll_ref(y, P, w=None):
    w = [1] * len(y) if w is None else w
    freq = [F(sum(wi for yi, wi in zip(y, w) if yi == c), sum(w)) for c in range(3)]
    return 1 - ll_sum(y, P, w) / ll_sum(y, [freq] * len(y), w)
if V >= (1, 5):
    report(f"d2_log_loss_score = 1 - logloss(y, p) / logloss(y, class proportions) ({float(d2ll_ref(y3, P3)):.6f})", close(metrics.d2_log_loss_score(y3, P3f), float(d2ll_ref(y3, P3))))
    report("d2_log_loss_score with sample_weight (weighted proportions and sums)", close(metrics.d2_log_loss_score(y3, P3f, sample_weight=W[:45]), float(d2ll_ref(y3, P3, W[:45]))))
    report("d2_log_loss_score of the null model itself is 0", close(metrics.d2_log_loss_score(y3, [[float(F(sum(1 for t in y3 if t == c), 45)) for c in range(3)]] * 45), 0.0, abs_=1e-12))
    y3m = [y if y != 2 else 0 for y in y3]
    freq = [F(sum(1 for t in y3m if t == c), 45) for c in range(3)]
    want = 1 - ll_sum(y3m, P3) / ll_sum(y3m, [freq] * 45)
    try:
        got = metrics.d2_log_loss_score(y3m, P3f, labels=[0, 1, 2]); det = f"(got {got:.6f})"
    except Exception as e:
        got = None; det = f"({type(e).__name__}: {str(e)[:110]})"
    report(f"d2_log_loss_score(labels=[0,1,2]) when y_true lacks a class: 'labels' docstring -> 1 - LL/LL(null with that class at proportion 0) ({float(want):.6f})", got is not None and close(got, float(want)), det)
    report("d2_log_loss_score with a single sample returns NaN (documented)", isnan(metrics.d2_log_loss_score([1], [[0.2, 0.8]])))

# ---- weighted MCC / kappa / balanced accuracy, log_loss labels & eps
print("---- classification: weighted MCC/kappa/balanced accuracy, log_loss")
def confusion_w(y, p, labels, w):
    c = {(a, b): 0 for a in labels for b in labels}
    for a, b, wi in zip(y, p, w): c[(a, b)] += wi
    return c
def mcc_w(y, p, labels, w):
    c = confusion_w(y, p, labels, w); n_ = sum(w)
    t = {k: sum(c[(k, b)] for b in labels) for k in labels}; q = {k: sum(c[(a, k)] for a in labels) for k in labels}
    cov_yp = n_ * sum(c[(k, k)] for k in labels) - sum(t[k] * q[k] for k in labels)
    cov_yy = n_ * n_ - sum(t[k] ** 2 for k in labels); cov_pp = n_ * n_ - sum(q[k] ** 2 for k in labels)
    return mp(F(cov_yp)) / mpmath.sqrt(mp(F(cov_yy * cov_pp)))
def kappa_w(y, p, labels, w, weights=None):
    c = confusion_w(y, p, labels, w); n_ = sum(w)
    t = {k: sum(c[(k, b)] for b in labels) for k in labels}; q = {k: sum(c[(a, k)] for a in labels) for k in labels}
    idx = {l: i for i, l in enumerate(labels)}
    def wt(a, b):
        if weights is None: return 0 if a == b else 1
        d = abs(idx[a] - idx[b]); return d if weights == "linear" else d * d
    obs = sum(wt(a, b) * c[(a, b)] for a in labels for b in labels)
    exp = sum(wt(a, b) * F(t[a] * q[b], n_) for a in labels for b in labels)
    return 1 - F(obs) / exp
def bal_acc_w(y, p, labels, w):
    c = confusion_w(y, p, labels, w)
    return fmean(F(c[(l, l)], sum(c[(l, b)] for b in labels)) for l in labels)
labs = [0, 1, 2, 3]
report("matthews_corrcoef with sample_weight = MCC of the weighted confusion matrix", close(metrics.matthews_corrcoef(ym, pm, sample_weight=wm), float(mcc_w(ym, pm, labs, wm))))
report("matthews_corrcoef with integer sample_weight = MCC of the repeated sample", close(metrics.matthews_corrcoef(ym, pm, sample_weight=wm), metrics.matthews_corrcoef([a for a, k in zip(ym, wm) for _ in range(k)], [b for b, k in zip(pm, wm) for _ in range(k)])))
for wts in [None, "linear", "quadratic"]:
    report(f"cohen_kappa_score(weights={wts}) with sample_weight = kappa of the weighted confusion matrix", close(metrics.cohen_kappa_score(ym, pm, weights=wts, sample_weight=wm), kappa_w(ym, pm, labs, wm, wts)))
report("balanced_accuracy_score with sample_weight = mean of weighted per-class recalls", close(metrics.balanced_accuracy_score(ym, pm, sample_weight=wm), bal_acc_w(ym, pm, labs, wm)))
ba = bal_acc_w(ym, pm, labs, wm)
report("balanced_accuracy_score(adjusted=True) with sample_weight = (BA - 1/4)/(1 - 1/4)", close(metrics.balanced_accuracy_score(ym, pm, sample_weight=wm, adjusted=True), (ba - F(1, 4)) / (1 - F(1, 4))))
# log_loss
y3m = [y if y != 2 else 0 for y in y3]
want = ll_sum(y3m, P3) / 45
report("log_loss(labels=[0,1,2]) when y_true lacks a class = -mean log p[y] over the given label order", close(metrics.log_loss(y3m, P3f, labels=[0, 1, 2]), float(want)))
report("log_loss without labels when y_true lacks a class raises ValueError", raises(ValueError, metrics.log_loss, y3m, P3f))
report("log_loss(normalize=False) = sum", close(metrics.log_loss(y3, P3f, normalize=False), float(ll_sum(y3, P3))))
p1d = [float(F(rng.randint(1, 15), 16)) for _ in yb01]
want = -fmean(mpmath.log(mp(F(p))) if y else mpmath.log(1 - mp(F(p))) for y, p in zip(yb01, p1d))
report("log_loss with 1-D probabilities of the positive class", close(metrics.log_loss(yb01, p1d), float(want)))
eps_v = 1e-15 if V < (1, 2) else 2.0 ** -52
got = metrics.log_loss([0, 1], [[1.0, 0.0], [1.0, 0.0]])
want = (-math.log(eps_v) - math.log(1 - eps_v)) / 2
report(f"log_loss clips probabilities at eps = {'1e-15 (pre-1.2 default)' if V < (1, 2) else 'finfo(float64).eps (1.2+ auto)'}: p=0 at the true class gives -log(eps)/2 = {want:.6f}", close(got, want, 1e-9), f"(got {got:.6f})")
got32 = metrics.log_loss([0, 1], np.array([[1.0, 0.0], [1.0, 0.0]], dtype=np.float32))
eps32 = 1e-15 if V < (1, 2) else float(np.finfo(np.float32).eps)
report(f"log_loss on float32 probabilities clips at {'1e-15' if V < (1, 2) else 'finfo(float32).eps'} -> {(-math.log(eps32) - math.log(1 - eps32)) / 2:.4f}", close(got32, (-math.log(eps32) - math.log(1 - eps32)) / 2, 1e-5), f"(got {got32:.4f})")
got = metrics.log_loss([0, 1], [[0.2, 0.2], [0.2, 0.2]])
if V < (1, 5):
    report("log_loss on rows not summing to 1 (pre-1.5): renormalised -> [0.5, 0.5] -> log 2", close(got, math.log(2)), f"(got {got:.6f})")
else:
    report("log_loss on rows not summing to 1 (1.5+): used as given (warning only) -> -log 0.2", close(got, -math.log(0.2)), f"(got {got:.6f})")

# =====================================================================================
# B. ranking
# =====================================================================================
print("---- ranking: DCG / NDCG, LRAP, ranking loss, coverage, det_curve, multilabel AUC/AP")
rng = random.Random(1410)
nq, nd = 8, 5
G = [[rng.randint(0, 3) for _ in range(nd)] for _ in range(nq)]; Sc = [[rng.randint(0, 4) / 2 for _ in range(nd)] for _ in range(nq)]
G[0] = [0] * nd                     # all irrelevant
Sc[1] = [1.0] * nd                  # all tied
def dcg_perm(gains, scores, k=None, base=2):
    disc = [1 / mpmath.log(i + 2, base) if (k is None or i < k) else mpmath.mpf(0) for i in range(len(gains))]
    groups = [[j for j in range(len(gains)) if scores[j] == s] for s in sorted(set(scores), reverse=True)]
    total = mpmath.mpf(0); cnt = 0
    for perm in itertools.product(*[itertools.permutations(g) for g in groups]):
        order = [j for g in perm for j in g]
        total += sum(gains[order[r]] * disc[r] for r in range(len(gains))); cnt += 1
    return total / cnt
def ndcg_ref(gains, scores, k=None):
    ideal = dcg_perm(gains, gains, k)   # order by gains (ties among equal gains do not matter)
    return dcg_perm(gains, scores, k) / ideal if ideal != 0 else mpmath.mpf(0)
for k in [None, 2, 3]:
    want = fmean(dcg_perm(g, s, k) for g, s in zip(G, Sc))
    report(f"dcg_score(k={k}) with ties = average of DCG over all permutations of tied groups, discount 1/log2(r+2) ({float(want):.6f})", close(metrics.dcg_score(G, Sc, k=k), float(want)))
for base in [10, math.e]:
    want = fmean(dcg_perm(g, s, None, base) for g, s in zip(G, Sc))
    report(f"dcg_score(log_base={base:.3g}) uses discount 1/log_base(r+2)", close(metrics.dcg_score(G, Sc, log_base=base), float(want)))
want = wmean([dcg_perm(g, s) for g, s in zip(G, Sc)], w[:nq])
report("dcg_score with sample_weight", close(metrics.dcg_score(G, Sc, sample_weight=w[:nq]), float(want)))
Sc_nt = [[rng.random() for _ in range(nd)] for _ in range(nq)]
report("dcg_score(ignore_ties=True) on tie-free scores equals the tie-averaged value", close(metrics.dcg_score(G, Sc_nt, ignore_ties=True), metrics.dcg_score(G, Sc_nt)) and close(metrics.dcg_score(G, Sc_nt), float(fmean(dcg_perm(g, s) for g, s in zip(G, Sc_nt)))))
for k in [None, 2]:
    want = fmean(ndcg_ref(g, s, k) for g, s in zip(G, Sc))
    report(f"ndcg_score(k={k}) = DCG / ideal DCG, 0 for an all-irrelevant row ({float(want):.6f})", close(metrics.ndcg_score(G, Sc, k=k), float(want)))
report("ndcg_score of a perfect ranking is 1 (rows with some relevance)", close(metrics.ndcg_score(G[1:], G[1:]), 1.0))
report("ndcg_score with all scores tied in a row: that row scores E[DCG]/IDCG", close(metrics.ndcg_score([G[1]], [Sc[1]]), float(ndcg_ref(G[1], Sc[1]))))
Gneg = [[1, -1, 2, 0, 1]]
if V >= (1, 4):
    report("ndcg_score with negative y_true raises ValueError (1.4+)", raises(ValueError, metrics.ndcg_score, Gneg, [Sc[2]]))
else:
    try:
        v = metrics.ndcg_score(Gneg, [Sc[2]]); print(f"   ndcg_score with negative y_true on {sklearn.__version__}: {v} (deprecation path)")
    except Exception as e: print(f"   ndcg_score with negative y_true on {sklearn.__version__}: {type(e).__name__}")
report("ndcg_score with a single document raises ValueError", raises(ValueError, metrics.ndcg_score, [[1]], [[1]]))

# ---- LRAP, ranking loss, coverage
nl = 5; Ylr = [[1 if rng.random() < 0.4 else 0 for _ in range(nl)] for _ in range(20)]; Slr = [[rng.randint(0, 6) / 3 for _ in range(nl)] for _ in range(20)]
Ylr[0] = [0] * nl; Ylr[1] = [1] * nl
def lrap_ref(Y, S, w=None):
    w = [1] * len(Y) if w is None else w; out = []
    for y, s in zip(Y, S):
        rel = [j for j in range(nl) if y[j]]
        if len(rel) in (0, nl): out.append(F(1)); continue
        tot = F(0)
        for j in rel:
            rank = sum(1 for k in range(nl) if s[k] >= s[j]); Lij = sum(1 for k in rel if s[k] >= s[j])
            tot += F(Lij, rank)
        out.append(tot / len(rel))
    return wmean(out, w)
report(f"label_ranking_average_precision_score = mean over samples of (1/|y|) sum_j |L_ij|/rank_ij with >= ties (user guide) ({float(lrap_ref(Ylr, Slr)):.6f})", close(metrics.label_ranking_average_precision_score(Ylr, Slr), lrap_ref(Ylr, Slr)))
report("LRAP: samples with no or all relevant labels count 1", metrics.label_ranking_average_precision_score(Ylr[:2], Slr[:2]) == 1.0)
report("LRAP with sample_weight", close(metrics.label_ranking_average_precision_score(Ylr, Slr, sample_weight=w[:20]), lrap_ref(Ylr, Slr, w[:20])))
def rl_ref(Y, S):
    out = []
    for y, s in zip(Y, S):
        npos = sum(y)
        if npos in (0, nl): out.append(F(0)); continue
        bad = sum(1 for k in range(nl) for l in range(nl) if y[k] == 1 and y[l] == 0 and s[k] <= s[l])
        out.append(F(bad, npos * (nl - npos)))
    return fmean(out)
report(f"label_ranking_loss = mean |{{(k,l): f_k <= f_l, y_k=1, y_l=0}}| / (|y| (L-|y|)) (ties count as errors) ({float(rl_ref(Ylr, Slr)):.6f})", close(metrics.label_ranking_loss(Ylr, Slr), rl_ref(Ylr, Slr)))
report("label_ranking_loss of no/all-relevant rows is 0", metrics.label_ranking_loss(Ylr[:2], Slr[:2]) == 0.0)
def cov_ref(Y, S):
    out = []
    for y, s in zip(Y, S):
        rel = [j for j in range(nl) if y[j]]
        out.append(max((sum(1 for k in range(nl) if s[k] >= s[j]) for j in rel), default=0))
    return fmean(out)
report(f"coverage_error = mean max_(j: y_j=1) |{{k: f_k >= f_j}}| (ties -> maximal rank), 0 for a row without true labels ({float(cov_ref(Ylr, Slr)):.4f})", close(metrics.coverage_error(Ylr, Slr), cov_ref(Ylr, Slr)))
report("coverage_error with sample_weight", close(metrics.coverage_error(Ylr, Slr, sample_weight=w[:20]), wmean([max((sum(1 for k in range(nl) if s[k] >= s[j]) for j in range(nl) if y[j]), default=0) for y, s in zip(Ylr, Slr)], w[:20])))
report("coverage_error >= average number of true labels (its documented best value)", metrics.coverage_error(Ylr, Slr) >= fmean(sum(y) for y in Ylr))

# ---- det_curve
ydet = [1 if rng.random() < 0.4 else 0 for _ in range(60)]; sdet = [rng.randint(0, 10) / 10 for _ in ydet]
def det_pts(y, s):
    P = sum(y); N = len(y) - P; pts = {}
    for t in sorted(set(s)):
        fp = sum(1 for yi, si in zip(y, s) if si >= t and yi == 0); tp = sum(1 for yi, si in zip(y, s) if si >= t and yi == 1)
        pts[t] = (F(fp, N), F(P - tp, P))
    return pts
pts = det_pts(ydet, sdet)
fpr, fnr, thr = metrics.det_curve(ydet, sdet)
finite = [(f, g, t) for f, g, t in zip(fpr, fnr, thr) if np.isfinite(t)]
report("det_curve: for every finite threshold fpr = FP(score >= thr)/N and fnr = FN(score < thr)/P (docstring definitions)", all(t in pts and close(f, pts[t][0]) and close(g, pts[t][1]) for f, g, t in finite))
report("det_curve: thresholds increasing, fpr non-increasing, fnr non-decreasing", all(np.diff(thr) > 0) and all(np.diff(fpr) <= 0) and all(np.diff(fnr) >= 0))
report("det_curve: first point has fnr = 0 (every positive caught), last point has the minimal fpr (0 on 1.7+, where an fpr=0 point is always present)", bool(fnr[0] == 0) and (close(fpr[-1], min(p[0] for p in pts.values())) if V < (1, 7) else fpr[-1] == 0))
has_finite_fp0 = any(p[0] == 0 for p in pts.values())
if V >= (1, 7):
    report(f"det_curve (1.7+): an inf threshold (fpr=0, fnr=1) is added exactly when no finite threshold reaches fpr=0 (here finite fpr=0 exists: {has_finite_fp0})", (np.isinf(thr[-1]) and fpr[-1] == 0 and fnr[-1] == 1) == (not has_finite_fp0))
    y2 = ydet[:]; s2 = sdet[:]; s2[ydet.index(0)] = 1.0   # make the max score a negative -> no finite fpr=0
    fpr2, fnr2, thr2 = metrics.det_curve(y2, s2)
    report("det_curve (1.7+): with a negative at the top score, the last point is the inf threshold with fpr=0, fnr=1", np.isinf(thr2[-1]) and fpr2[-1] == 0 and fnr2[-1] == 1)
    fpr3, fnr3, thr3 = metrics.det_curve(ydet, sdet, drop_intermediate=True)
    full = set(zip(fpr, fnr, thr)); kept = set(zip(fpr3, fnr3, thr3))
    report("det_curve(drop_intermediate=True): a subset of the points that keeps every fnr level (only points whose tp equals both neighbours are dropped)", kept <= full and set(fnr3) == set(fnr) and len(kept) <= len(full))
else:
    print(f"   det_curve on {sklearn.__version__}: {len(thr)} points, no inf threshold ({np.isinf(thr).any()})")
report("det_curve with a single class raises ValueError", raises(ValueError, metrics.det_curve, [1, 1, 1], [0.1, 0.2, 0.3]))
report("det_curve pos_label='b' with string labels", all(close(f, pts[t][0]) and close(g, pts[t][1]) for f, g, t in zip(*metrics.det_curve(['b' if y else 'a' for y in ydet], sdet, pos_label='b')) if np.isfinite(t)))

# ---- multilabel AUC / AP averages
nm = 30; Ym = [[1 if rng.random() < 0.5 else 0 for _ in range(4)] for _ in range(nm)]; Sm = [[rng.randint(0, 9) / 9 for _ in range(4)] for _ in range(nm)]
for row in Ym:
    if sum(row) == 0: row[0] = 1
    if sum(row) == 4: row[3] = 0
cols = lambda M, j: [r[j] for r in M]
auc_lab = [auc_exact(cols(Ym, j), cols(Sm, j)) for j in range(4)]
report("roc_auc_score multilabel-indicator average='macro' = mean of per-label AUCs", close(metrics.roc_auc_score(Ym, Sm, average="macro"), fmean(auc_lab)))
report("roc_auc_score multilabel average=None = per-label array", all(close(g, e) for g, e in zip(metrics.roc_auc_score(Ym, Sm, average=None), auc_lab)))
report("roc_auc_score multilabel average='micro' = AUC of the flattened (y, score)", close(metrics.roc_auc_score(Ym, Sm, average="micro"), auc_exact([v for r in Ym for v in r], [v for r in Sm for v in r])))
report("roc_auc_score multilabel average='samples' = mean of per-sample AUCs (each row ranked across labels)", close(metrics.roc_auc_score(Ym, Sm, average="samples"), fmean(auc_exact(y, s) for y, s in zip(Ym, Sm))))
npos = [sum(cols(Ym, j)) for j in range(4)]
report("roc_auc_score multilabel average='weighted' = per-label AUCs weighted by the number of positives", close(metrics.roc_auc_score(Ym, Sm, average="weighted"), wmean(auc_lab, npos)))
ap_lab = [ap_exact(cols(Ym, j), cols(Sm, j)) for j in range(4)]
report("average_precision_score multilabel average='macro' = mean of per-label AP", close(metrics.average_precision_score(Ym, Sm, average="macro"), fmean(ap_lab)))
report("average_precision_score multilabel average='micro' = AP of the flattened arrays", close(metrics.average_precision_score(Ym, Sm, average="micro"), ap_exact([v for r in Ym for v in r], [v for r in Sm for v in r])))
report("average_precision_score multilabel average='samples' = mean of per-sample AP", close(metrics.average_precision_score(Ym, Sm, average="samples"), fmean(ap_exact(y, s) for y, s in zip(Ym, Sm))))
report("average_precision_score multilabel average='weighted'", close(metrics.average_precision_score(Ym, Sm, average="weighted"), wmean(ap_lab, npos)))

# =====================================================================================
# C. regression remainder
# =====================================================================================
print("---- regression: MSLE, median AE, max_error, pinball, Tweedie, D2, MAPE, r2/EV force_finite, RMSE")
rng = random.Random(1420)
yr = [F(rng.randint(1, 40), 4) for _ in range(24)]; pr_ = [v + F(rng.randint(-8, 8), 4) for v in yr]; pr_ = [max(p, F(1, 4)) for p in pr_]
yrf = [float(v) for v in yr]; prf = [float(v) for v in pr_]
wr = W[:24]
msle = fmean((mpmath.log1p(mp(a)) - mpmath.log1p(mp(b))) ** 2 for a, b in zip(yr, pr_))
report(f"mean_squared_log_error = mean (log(1+y) - log(1+p))^2 ({float(msle):.6f})", close(metrics.mean_squared_log_error(yrf, prf), float(msle)))
report("mean_squared_log_error with sample_weight", close(metrics.mean_squared_log_error(yrf, prf, sample_weight=wr), float(wmean([(mpmath.log1p(mp(a)) - mpmath.log1p(mp(b))) ** 2 for a, b in zip(yr, pr_)], wr))))
report("mean_squared_log_error with y_true = -1 raises ValueError", raises(ValueError, metrics.mean_squared_log_error, [-1.0] + yrf[1:], prf))
report("mean_squared_log_error with y_pred = -2 raises ValueError", raises(ValueError, metrics.mean_squared_log_error, yrf, [-2.0] + prf[1:]))
try:
    v_ = metrics.mean_squared_log_error([-0.5] + yrf[1:], prf); got_ok = True
except ValueError: got_ok = False
want_ok = V >= (1, 6)   # 1.6 changelog: 'now check whether the inputs are within the correct domain for y=log(1+x), rather than y=log(x)'
report(f"mean_squared_log_error with a target in (-1, 0): {'accepted (1.6+: domain of log(1+x) is x > -1)' if want_ok else 'rejected (pre-1.6: negative values rejected)'}", got_ok == want_ok)
if got_ok:
    want = fmean((mpmath.log1p(mp(a)) - mpmath.log1p(mp(b))) ** 2 for a, b in zip([F(-1, 2)] + yr[1:], pr_))
    report("mean_squared_log_error with a target of -0.5 = mean (log1p(y) - log1p(p))^2", close(v_, float(want)))
if V >= (1, 4):
    report("root_mean_squared_log_error = sqrt(MSLE)", close(metrics.root_mean_squared_log_error(yrf, prf), float(mpmath.sqrt(msle))))
    report("root_mean_squared_log_error negative target raises ValueError", raises(ValueError, metrics.root_mean_squared_log_error, [-1.0] + yrf[1:], prf))
# median absolute error
ae = [abs(a - b) for a, b in zip(yr, pr_)]
def median_expanded(vals, wts):
    xs = sorted(v for v, k in zip(vals, wts) for _ in range(k)); m = len(xs); return (xs[m // 2] + xs[(m - 1) // 2]) / 2
def inverted_cdf(vals, wts, q=F(1, 2)):
    tot = sum(wts); cum = 0
    for v, k in sorted(zip(vals, wts)): 
        cum += k
        if cum >= q * tot: return v
report(f"median_absolute_error = median |y - p| ({float(median_expanded(ae, [1] * 24)):.4f})", close(metrics.median_absolute_error(yrf, prf), median_expanded(ae, [1] * 24)))
want_new = median_expanded(ae, wr); want_old = inverted_cdf(ae, wr)
got = metrics.median_absolute_error(yrf, prf, sample_weight=wr)
if V >= (1, 8):
    report(f"median_absolute_error with integer sample_weight (1.8+ averaged_inverted_cdf) = median of the sample repeated by its weight ({float(want_new):.4f})", close(got, want_new), f"(got {got:.4f}; inverted_cdf would give {float(want_old):.4f})")
else:
    report(f"median_absolute_error with integer sample_weight (pre-1.8 inverted_cdf) = first value whose cumulative weight reaches half ({float(want_old):.4f})", close(got, want_old), f"(got {got:.4f}; repeated-sample median would be {float(want_new):.4f})")
Y2 = np.c_[yrf, [2 * v for v in prf]]; P2 = np.c_[prf, yrf]
ae2 = [abs(2 * b - a) for a, b in zip(yr, pr_)]
got = metrics.median_absolute_error(Y2, P2, multioutput="raw_values")
report("median_absolute_error(multioutput='raw_values') gives one median per output (the user guide says 'does not support multioutput': it does)", mat_close(got, [median_expanded(ae, [1] * 24), median_expanded(ae2, [1] * 24)]))
report("median_absolute_error(multioutput=[0.25, 0.75]) = weighted average of the per-output medians", close(metrics.median_absolute_error(Y2, P2, multioutput=[0.25, 0.75]), F(1, 4) * median_expanded(ae, [1] * 24) + F(3, 4) * median_expanded(ae2, [1] * 24)))
report("max_error = max |y - p|", close(metrics.max_error(yrf, prf), max(ae)))
report("max_error with multioutput raises ValueError ('Multioutput not supported')", raises(ValueError, metrics.max_error, Y2, P2))
# pinball
def pinball(y, p, a, wts=None):
    wts = [1] * len(y) if wts is None else wts
    return wmean([a * max(yi - pi, 0) + (1 - a) * max(pi - yi, 0) for yi, pi in zip(y, p)], wts)
for a in [F(1, 10), F(1, 2), F(9, 10)]:
    report(f"mean_pinball_loss(alpha={float(a)}) = mean alpha*max(y-p,0) + (1-alpha)*max(p-y,0) ({float(pinball(yr, pr_, a)):.6f})", close(metrics.mean_pinball_loss(yrf, prf, alpha=float(a)), pinball(yr, pr_, a)))
report("mean_pinball_loss(alpha=0.5) = half the mean absolute error (user guide)", close(metrics.mean_pinball_loss(yrf, prf), metrics.mean_absolute_error(yrf, prf) / 2))
report("mean_pinball_loss with sample_weight", close(metrics.mean_pinball_loss(yrf, prf, alpha=0.3, sample_weight=wr), pinball(yr, pr_, F(3, 10), wr)))
report("mean_pinball_loss multioutput raw_values", mat_close(metrics.mean_pinball_loss(Y2, P2, alpha=0.7, multioutput="raw_values"), [pinball(yr, pr_, F(7, 10)), pinball([2 * b for b in pr_], yr, F(7, 10))]))
# Tweedie
def tw_unit(y, m, p):
    y = mp(y); m = mp(m); p = mpmath.mpf(p)
    if p == 0: return (y - m) ** 2
    if p == 1: return 2 * ((y * mpmath.log(y / m) if y != 0 else 0) - y + m)
    if p == 2: return 2 * (mpmath.log(m / y) + y / m - 1)
    return 2 * (max(y, 0) ** (2 - p) / ((1 - p) * (2 - p)) - y * m ** (1 - p) / (1 - p) + m ** (2 - p) / (2 - p))
def tw_mean(y, m, p, wts=None):
    wts = [1] * len(y) if wts is None else wts
    return wmean([tw_unit(a, b, p) for a, b in zip(y, m)], wts)
for p in [0, 1, 1.5, 2, 3, -1]:
    want = tw_mean(yr, pr_, p)
    report(f"mean_tweedie_deviance(power={p}) = user-guide formula ({float(want):.6f})", close(metrics.mean_tweedie_deviance(yrf, prf, power=p), float(want), 1e-10))
report("mean_tweedie_deviance(power=1) with sample_weight", close(metrics.mean_tweedie_deviance(yrf, prf, power=1, sample_weight=wr), float(tw_mean(yr, pr_, 1, wr)), 1e-10))
report("mean_poisson_deviance == power=1 and mean_gamma_deviance == power=2 (documented)", close(metrics.mean_poisson_deviance(yrf, prf), metrics.mean_tweedie_deviance(yrf, prf, power=1)) and close(metrics.mean_gamma_deviance(yrf, prf), metrics.mean_tweedie_deviance(yrf, prf, power=2)))
report("mean_tweedie_deviance(power=0) == mean_squared_error", close(metrics.mean_tweedie_deviance(yrf, prf, power=0), metrics.mean_squared_error(yrf, prf)))
y0 = [0.0] + yrf[1:]
report("power=1 with y_true = 0 allowed (0 log 0 = 0)", close(metrics.mean_tweedie_deviance(y0, prf, power=1), float(tw_mean([F(0)] + yr[1:], pr_, 1)), 1e-10))
report("power=1.5 with y_true = 0 allowed", close(metrics.mean_tweedie_deviance(y0, prf, power=1.5), float(tw_mean([F(0)] + yr[1:], pr_, 1.5)), 1e-10))
report("power=2 with y_true = 0 raises ValueError ('strictly positive y')", raises(ValueError, metrics.mean_tweedie_deviance, y0, prf, power=2))
report("power=3 with negative y_true raises", raises(ValueError, metrics.mean_tweedie_deviance, [-1.0] + yrf[1:], prf, power=3))
report("power=1 with y_pred = 0 raises ValueError ('strictly positive y_pred')", raises(ValueError, metrics.mean_tweedie_deviance, yrf, [0.0] + prf[1:], power=1))
report("power=-1 with y_pred = 0 raises, negative y_true allowed", raises(ValueError, metrics.mean_tweedie_deviance, yrf, [0.0] + prf[1:], power=-1) and not raises(Exception, metrics.mean_tweedie_deviance, [-1.0] + yrf[1:], prf, power=-1))
yneg = [F(-3, 2)] + yr[1:]
report("power=-1 with negative y_true uses max(y, 0)^(2-p) in the first term (user-guide formula)", close(metrics.mean_tweedie_deviance([float(v) for v in yneg], prf, power=-1), float(tw_mean(yneg, pr_, -1)), 1e-10))
report("power=0.5 is rejected (power must be <= 0 or >= 1)", raises(Exception, metrics.mean_tweedie_deviance, yrf, prf, power=0.5))
report("Tweedie deviance is homogeneous of degree 2-power: scaling y and p by 3 multiplies power=1.5 deviance by 3^0.5", close(metrics.mean_tweedie_deviance([3 * v for v in yrf], [3 * v for v in prf], power=1.5), 3 ** 0.5 * metrics.mean_tweedie_deviance(yrf, prf, power=1.5), 1e-10))
# D2 scores
for p in [0, 1, 2]:
    ybar = fmean(yr); want = 1 - tw_mean(yr, pr_, p) / tw_mean(yr, [ybar] * 24, p)
    report(f"d2_tweedie_score(power={p}) = 1 - dev(y, p) / dev(y, mean y) ({float(want):.6f})", close(metrics.d2_tweedie_score(yrf, prf, power=p), float(want), 1e-10))
ybw = wmean(yr, wr); want = 1 - tw_mean(yr, pr_, 1, wr) / tw_mean(yr, [ybw] * 24, 1, wr)
report("d2_tweedie_score with sample_weight uses the weighted mean as null model", close(metrics.d2_tweedie_score(yrf, prf, power=1, sample_weight=wr), float(want), 1e-10))
report("d2_tweedie_score(power=0) == r2_score (documented)", close(metrics.d2_tweedie_score(yrf, prf, power=0), metrics.r2_score(yrf, prf)))
report("d2_tweedie_score of the mean prediction is 0", close(metrics.d2_tweedie_score(yrf, [float(fmean(yr))] * 24, power=1), 0.0, abs_=1e-12))
report("d2_tweedie_score with one sample returns NaN", isnan(metrics.d2_tweedie_score([1.0], [2.0])))
def quantile_expanded(vals, wts, q, average):
    """alpha-quantile of the sample repeated by its integer weights: inverted_cdf (average=False) or
    averaged_inverted_cdf (average=True)."""
    xs = sorted(v for v, k in zip(vals, wts) for _ in range(k)); m = len(xs); g = q * m
    if average and g == int(g) and 0 < int(g) < m: return (xs[int(g) - 1] + xs[int(g)]) / 2
    return xs[max(math.ceil(g) - 1, 0)]
def quantile_linear(vals, q):
    """numpy's default 'linear' percentile: h = (n-1) q, interpolate between order statistics."""
    xs = sorted(vals); h = (len(xs) - 1) * q; lo = math.floor(h)
    return xs[lo] if lo + 1 >= len(xs) else xs[lo] + (h - lo) * (xs[lo + 1] - xs[lo])
# 1.9 changelog: d2_pinball_score / d2_absolute_error_score 'now always use the "averaged_inverted_cdf" quantile
# method, both with and without sample weights. Previously, the "linear" quantile method was used only for the
# unweighted case'. The weighted path used _weighted_percentile (inverted_cdf) on the 1.1-1.5 builds.
for a in [F(1, 2), F(9, 10), F(1, 4)]:
    q_avg = quantile_expanded(yr, [1] * 24, a, True); q_lin = quantile_linear(yr, a)
    want_avg = 1 - pinball(yr, pr_, a) / pinball(yr, [q_avg] * 24, a); want_lin = 1 - pinball(yr, pr_, a) / pinball(yr, [q_lin] * 24, a)
    got = metrics.d2_pinball_score(yrf, prf, alpha=float(a))
    if V >= (1, 9):
        report(f"d2_pinball_score(alpha={float(a)}) = 1 - pinball(y,p)/pinball(y, alpha-quantile of y), 1.9+: averaged_inverted_cdf quantile ({float(want_avg):.6f})", close(got, want_avg), f"(got {got:.6f}; linear quantile would give {float(want_lin):.6f})")
    else:
        report(f"d2_pinball_score(alpha={float(a)}) = 1 - pinball(y,p)/pinball(y, alpha-quantile of y), pre-1.9 unweighted: numpy 'linear' percentile ({float(want_lin):.6f})", close(got, want_lin), f"(got {got:.6f}; averaged_inverted_cdf would give {float(want_avg):.6f})")
qa = quantile_expanded(yr, wr, F(1, 2), V >= (1, 8))
report("d2_pinball_score with integer sample_weight = the repeated-sample computation", close(metrics.d2_pinball_score(yrf, prf, sample_weight=wr), 1 - pinball(yr, pr_, F(1, 2), wr) / pinball(yr, [qa] * 24, F(1, 2), wr)), f"(check uses the {'averaged' if V >= (1, 8) else 'inverted_cdf'} weighted median)")
report("d2_absolute_error_score == d2_pinball_score(alpha=0.5)", close(metrics.d2_absolute_error_score(yrf, prf), metrics.d2_pinball_score(yrf, prf, alpha=0.5)))
report("d2_pinball_score multioutput raw_values", mat_close(metrics.d2_pinball_score(Y2, P2, multioutput="raw_values"), [metrics.d2_pinball_score(yrf, prf), metrics.d2_pinball_score([2 * v for v in prf], yrf)]))
# MAPE
eps64 = F(2) ** -52
yz = [F(0)] + yr[1:]
mape = fmean(abs(a - b) / max(abs(a), eps64) for a, b in zip(yz, pr_))
report(f"mean_absolute_percentage_error with a zero target: that term is |p| / eps with eps = finfo(float64).eps = 2^-52 ({float(mape):.4e})", close(metrics.mean_absolute_percentage_error([float(v) for v in yz], prf), mape))
report("mean_absolute_percentage_error (no zeros) = mean |y-p|/|y|", close(metrics.mean_absolute_percentage_error(yrf, prf), fmean(abs(a - b) / abs(a) for a, b in zip(yr, pr_))))
report("mean_absolute_percentage_error multioutput raw_values", mat_close(metrics.mean_absolute_percentage_error(Y2, P2, multioutput="raw_values"), [fmean(abs(a - b) / abs(a) for a, b in zip(yr, pr_)), fmean(abs(2 * b - a) / abs(2 * b) for a, b in zip(yr, pr_))]))
report("mean_absolute_percentage_error with sample_weight", close(metrics.mean_absolute_percentage_error(yrf, prf, sample_weight=wr), wmean([abs(a - b) / abs(a) for a, b in zip(yr, pr_)], wr)))
# r2 / explained variance
ybw = wmean(yr, wr)
r2w = 1 - sum(k * (a - b) ** 2 for a, b, k in zip(yr, pr_, wr)) / sum(k * (a - ybw) ** 2 for a, k in zip(yr, wr))
report("r2_score with sample_weight = 1 - sum w (y-p)^2 / sum w (y - weighted mean)^2", close(metrics.r2_score(yrf, prf, sample_weight=wr), r2w))
const = [2.0] * 24
report("r2_score constant y_true, imperfect prediction, force_finite=False -> -inf", metrics.r2_score(const, prf, force_finite=False) == -float("inf"))
report("r2_score constant y_true, perfect prediction, force_finite=False -> NaN", isnan(metrics.r2_score(const, const, force_finite=False)))
report("r2_score constant y_true with force_finite=True (default): 0.0 imperfect, 1.0 perfect", metrics.r2_score(const, prf) == 0.0 and metrics.r2_score(const, const) == 1.0)
def r2_1(y, p):
    yb = fmean(y); return 1 - sum((a - b) ** 2 for a, b in zip(y, p)) / sum((a - yb) ** 2 for a in y)
r2a = r2_1(yr, pr_); r2b = r2_1([2 * b for b in pr_], yr)
va = sum((a - fmean(yr)) ** 2 for a in yr); vb = sum((2 * b - fmean(2 * b for b in pr_)) ** 2 for b in pr_)
report("r2_score multioutput='variance_weighted' = per-output R2 weighted by the total sums of squares", close(metrics.r2_score(Y2, P2, multioutput="variance_weighted"), (r2a * va + r2b * vb) / (va + vb)))
report("r2_score multioutput='raw_values' / 'uniform_average'", mat_close(metrics.r2_score(Y2, P2, multioutput="raw_values"), [r2a, r2b]) and close(metrics.r2_score(Y2, P2), (r2a + r2b) / 2))
def ev_1(y, p, wts=None):
    wts = [1] * len(y) if wts is None else wts
    d = [a - b for a, b in zip(y, p)]; dm = wmean(d, wts); ym_ = wmean(y, wts)
    return 1 - wmean([(x - dm) ** 2 for x in d], wts) / wmean([(a - ym_) ** 2 for a in y], wts)
report("explained_variance_score = 1 - Var(y - p)/Var(y)", close(metrics.explained_variance_score(yrf, prf), ev_1(yr, pr_)))
report("explained_variance_score with sample_weight (weighted variances)", close(metrics.explained_variance_score(yrf, prf, sample_weight=wr), ev_1(yr, pr_, wr)))
eva = ev_1(yr, pr_); evb = ev_1([2 * b for b in pr_], yr)
report("explained_variance_score multioutput raw_values / uniform_average / variance_weighted", mat_close(metrics.explained_variance_score(Y2, P2, multioutput="raw_values"), [eva, evb]) and close(metrics.explained_variance_score(Y2, P2), (eva + evb) / 2) and close(metrics.explained_variance_score(Y2, P2, multioutput="variance_weighted"), (eva * va + evb * vb) / (va + vb)))
report("explained_variance_score constant y_true: force_finite=True gives 0.0/1.0, force_finite=False gives -inf/NaN", metrics.explained_variance_score(const, prf) == 0.0 and metrics.explained_variance_score(const, const) == 1.0 and metrics.explained_variance_score(const, prf, force_finite=False) == -float("inf") and isnan(metrics.explained_variance_score(const, const, force_finite=False)))
report("explained_variance_score constant y_true with a constant offset prediction (Var(y-p)=0) is 1.0 under force_finite (documented 'perfect' rule counts residual variance)", metrics.explained_variance_score(const, [3.0] * 24) == 1.0)
if V >= (1, 4):
    rm_a = mpmath.sqrt(mp(fmean((a - b) ** 2 for a, b in zip(yr, pr_)))); rm_b = mpmath.sqrt(mp(fmean((2 * b - a) ** 2 for a, b in zip(yr, pr_))))
    report("root_mean_squared_error multioutput='raw_values' = sqrt of each output's MSE", mat_close(metrics.root_mean_squared_error(Y2, P2, multioutput="raw_values"), [float(rm_a), float(rm_b)]))
    report("root_mean_squared_error default = uniform average of the per-output RMSEs (not sqrt of the mean MSE)", close(metrics.root_mean_squared_error(Y2, P2), float((rm_a + rm_b) / 2)), f"(sqrt of mean MSE would be {float(mpmath.sqrt((rm_a**2 + rm_b**2) / 2)):.6f})")
    report("root_mean_squared_error with sample_weight", close(metrics.root_mean_squared_error(yrf, prf, sample_weight=wr), float(mpmath.sqrt(mp(wmean([(a - b) ** 2 for a, b in zip(yr, pr_)], wr))))))

# =====================================================================================
# D. clustering remainder
# =====================================================================================
print("---- clustering: contingency, pair confusion, consensus_score, V-measure beta, degenerate counts, silhouette sample_size")
rng = random.Random(1430)
lt = [rng.randint(0, 2) for _ in range(30)]; lp = [rng.randint(0, 3) for _ in range(30)]
C = metrics.cluster.contingency_matrix(lt, lp)
want = [[sum(1 for a, b in zip(lt, lp) if a == i and b == j) for j in range(4)] for i in range(3)]
report("contingency_matrix C[i, j] = # samples in true class i and cluster j (sorted labels)", C.tolist() == want and C.dtype == np.int64)
report("contingency_matrix(eps=0.5) adds eps to every entry and returns float", mat_close(metrics.cluster.contingency_matrix(lt, lp, eps=0.5), [[v + 0.5 for v in row] for row in want]))
Cs = metrics.cluster.contingency_matrix(lt, lp, sparse=True)
report("contingency_matrix(sparse=True) is a CSR matrix with the same counts", Cs.format == "csr" and Cs.toarray().tolist() == want)
report("contingency_matrix(sparse=True, eps=...) raises ValueError", raises(ValueError, metrics.cluster.contingency_matrix, lt, lp, sparse=True, eps=0.1))
report("contingency_matrix(dtype=float) honours dtype", metrics.cluster.contingency_matrix(lt, lp, dtype=np.float64).dtype == np.float64)
report("contingency_matrix with string labels", metrics.cluster.contingency_matrix(['b', 'a', 'b'], [1, 1, 0]).tolist() == [[0, 1], [1, 1]])
pc = metrics.cluster.pair_confusion_matrix(lt, lp)
cnt = collections.Counter((lt[i] == lt[j], lp[i] == lp[j]) for i in range(30) for j in range(30) if i != j)
report("pair_confusion_matrix over ordered pairs i != j: C00 = different in both, C11 = same in both, C01 = different true / same pred, C10 = same true / different pred", pc.tolist() == [[cnt[(False, False)], cnt[(False, True)]], [cnt[(True, False)], cnt[(True, True)]]] and pc.sum() == 30 * 29)
report("pair_confusion_matrix of identical clusterings is diagonal", np.count_nonzero(metrics.cluster.pair_confusion_matrix(lt, lt) - np.diag(np.diag(metrics.cluster.pair_confusion_matrix(lt, lt)))) == 0)
report("rand_score = (C00 + C11) / n(n-1) from the pair confusion matrix (documented relation)", close(metrics.rand_score(lt, lp), F(int(pc[0, 0] + pc[1, 1]), 30 * 29)))
def jac_bic(ar, ac, br, bc):
    inter = sum(x and y for x, y in zip(ar, br)) * sum(x and y for x, y in zip(ac, bc)); sa = sum(ar) * sum(ac); sb = sum(br) * sum(bc)
    return F(inter, sa + sb - inter)
def consensus_ref(a, b, sim=jac_bic):
    na, nb = len(a[0]), len(b[0]); best = F(0)
    if na <= nb:
        for perm in itertools.permutations(range(nb), na): best = max(best, sum(sim(a[0][i], a[1][i], b[0][perm[i]], b[1][perm[i]]) for i in range(na)))
    else:
        for perm in itertools.permutations(range(na), nb): best = max(best, sum(sim(a[0][perm[j]], a[1][perm[j]], b[0][j], b[1][j]) for j in range(nb)))
    return best / max(na, nb)
def nonempty(n_):
    v = [rng.random() < 0.5 for _ in range(n_)]; v[rng.randrange(n_)] = True; return v
def bic(k, nr, nc): return ([nonempty(nr) for _ in range(k)], [nonempty(nc) for _ in range(k)])
A = bic(3, 8, 6); B = bic(4, 8, 6)
for a_, b_ in [(A, B), (B, A), (A, A)]:
    want = consensus_ref(a_, b_)
    report(f"consensus_score(jaccard) = best one-to-one matching of bicluster Jaccard similarities / max(n_a, n_b) ({float(want):.6f})", close(metrics.consensus_score((np.array(a_[0]), np.array(a_[1])), (np.array(b_[0]), np.array(b_[1]))), want))
sim2 = lambda ar, ac, br, bc: float(np.dot(ar, br) * np.dot(ac, bc)) / 100.0
report("consensus_score with a callable similarity", close(metrics.consensus_score((np.array(A[0]), np.array(A[1])), (np.array(B[0]), np.array(B[1])), similarity=sim2), consensus_ref(A, B, lambda ar, ac, br, bc: F(sim2(np.array(ar), np.array(ac), np.array(br), np.array(bc))))))
report("consensus_score docstring example = 1.0", metrics.consensus_score(([[True, False], [False, True]], [[False, True], [True, False]]), ([[False, True], [True, False]], [[True, False], [False, True]])) == 1.0)
h = float(mi_exact(lt, lp) / entropy_exact(lt)); c = float(mi_exact(lt, lp) / entropy_exact(lp))
for beta in [0.5, 1.0, 2.0]:
    vm = (1 + beta) * h * c / (beta * h + c)
    got = metrics.homogeneity_completeness_v_measure(lt, lp, beta=beta)
    report(f"homogeneity_completeness_v_measure(beta={beta}): V = (1+beta) h c / (beta h + c)", close(got[0], h) and close(got[1], c) and close(got[2], vm) and close(metrics.v_measure_score(lt, lp, beta=beta), vm))
report("v_measure_score(beta=1) == normalized_mutual_info_score (arithmetic) (documented identity)", close(metrics.v_measure_score(lt, lp), metrics.normalized_mutual_info_score(lt, lp)))
report("homogeneity_completeness_v_measure of empty inputs = (1, 1, 1)", metrics.homogeneity_completeness_v_measure([], []) == (1.0, 1.0, 1.0))
Xc = np.array([[rng.gauss(cx, 0.8), rng.gauss(cy, 0.8)] for cx, cy in [(0, 0), (5, 0), (0, 5)] for _ in range(12)]); labc = np.repeat([0, 1, 2], 12)
for name, fn_ in [("calinski_harabasz_score", metrics.calinski_harabasz_score), ("davies_bouldin_score", metrics.davies_bouldin_score), ("silhouette_score", metrics.silhouette_score)]:
    report(f"{name} with a single cluster raises ValueError ('2 to n_samples - 1')", raises(ValueError, fn_, Xc, np.zeros(36, int)))
    report(f"{name} with n_labels == n_samples raises ValueError", raises(ValueError, fn_, Xc, np.arange(36)))
print(f"   calinski_harabasz_score with zero within-cluster dispersion (undocumented, informational): {metrics.calinski_harabasz_score(np.repeat([[0.0, 0.0], [1.0, 1.0]], 3, axis=0), [0, 0, 0, 1, 1, 1])}")
ss_full = float(silhouette_exact(Xc, labc).mean())
report("silhouette_score(sample_size=None) = full mean", close(metrics.silhouette_score(Xc, labc), ss_full))
idx = np.random.RandomState(7).permutation(36)[:20]
want = float(silhouette_exact(Xc[idx], labc[idx]).mean())
report("silhouette_score(sample_size=20, random_state=7) = mean silhouette of the subset RandomState(7).permutation(n)[:20], computed within the subset", close(metrics.silhouette_score(Xc, labc, sample_size=20, random_state=7), want), f"({metrics.silhouette_score(Xc, labc, sample_size=20, random_state=7):.6f} vs full {ss_full:.6f})")
D = np.sqrt(((Xc[:, None, :] - Xc[None, :, :]) ** 2).sum(-1))
report("silhouette_score(metric='precomputed', sample_size=20, random_state=7) subsets rows and columns consistently", close(metrics.silhouette_score(D, labc, metric="precomputed", sample_size=20, random_state=7), want))
report("silhouette_score(sample_size > n_samples) uses all samples (permutation truncation)", close(metrics.silhouette_score(Xc, labc, sample_size=100, random_state=0), ss_full))

# =====================================================================================
# E. pairwise distances, kernels, DistanceMetric
# =====================================================================================
print("---- pairwise: every distance metric against plain-Python formulas")
import scipy.sparse as sp_
from sklearn.metrics import pairwise_distances, DistanceMetric
rng = random.Random(1440)
def qrow(nf, lo=-8, hi=8): return [F(rng.randint(lo, hi), 4) for _ in range(nf)]
nf = 4
Xq = [qrow(nf) for _ in range(6)]; Yq = [qrow(nf) for _ in range(5)]
Yq[2] = list(Xq[3])                        # one identical pair -> distance 0
Xq[5] = [F(0)] + Xq[5][1:]; Yq[4] = [F(0)] + Yq[4][1:]   # shared zero coordinate (canberra 0/0 term)
Xa = np.array([[float(v) for v in r] for r in Xq]); Ya = np.array([[float(v) for v in r] for r in Yq])
msqrt = lambda f: mpmath.sqrt(mp(F(f)))
def d_euc(x, y): return msqrt(sum((a - b) ** 2 for a, b in zip(x, y)))
def d_sqe(x, y): return sum((a - b) ** 2 for a, b in zip(x, y))
def d_man(x, y): return sum(abs(a - b) for a, b in zip(x, y))
def d_cheb(x, y): return max(abs(a - b) for a, b in zip(x, y))
def d_mink(x, y, p=3, w=None):
    w = [1] * len(x) if w is None else w
    return mpmath.power(sum(mp(F(wi)) * mpmath.power(abs(mp(a - b)), p) for a, b, wi in zip(x, y, w)), mpmath.mpf(1) / p)
def d_cos(x, y): return 1 - mp(sum(a * b for a, b in zip(x, y))) / (msqrt(sum(a * a for a in x)) * msqrt(sum(b * b for b in y)))
def d_corr(x, y):
    mx = fmean(x); my = fmean(y); return d_cos([a - mx for a in x], [b - my for b in y])
def d_bray_scipy(x, y): return F(sum(abs(a - b) for a, b in zip(x, y)), 1) / sum(abs(a + b) for a, b in zip(x, y))
def d_bray_skl(x, y): return F(sum(abs(a - b) for a, b in zip(x, y)), 1) / (sum(abs(a) for a in x) + sum(abs(b) for b in y))
def d_canb(x, y): return sum((abs(a - b) / (abs(a) + abs(b)) for a, b in zip(x, y) if abs(a) + abs(b) != 0), F(0))
def d_ham(x, y): return F(sum(a != b for a, b in zip(x, y)), len(x))
def d_seuc(x, y, V): return msqrt(sum((a - b) ** 2 / v for a, b, v in zip(x, y, V)))
def d_maha(x, y, VI):
    d = [a - b for a, b in zip(x, y)]; return msqrt(sum(d[i] * VI[i][j] * d[j] for i in range(len(d)) for j in range(len(d))))
def fr_inv(A):
    n_ = len(A); M = [[F(v) for v in A[i]] + [F(int(i == j)) for j in range(n_)] for i in range(n_)]
    for c in range(n_):
        p_ = next(r for r in range(c, n_) if M[r][c] != 0); M[c], M[p_] = M[p_], M[c]
        pv = M[c][c]; M[c] = [v / pv for v in M[c]]
        for r in range(n_):
            if r != c and M[r][c] != 0:
                f_ = M[r][c]; M[r] = [a - f_ * b for a, b in zip(M[r], M[c])]
    return [row[n_:] for row in M]
def fr_var(rows, j):
    col = [r[j] for r in rows]; m_ = fmean(col); return sum((v - m_) ** 2 for v in col) / (len(col) - 1)
def fr_cov(rows):
    k_ = len(rows[0]); mu = [fmean(r[j] for r in rows) for j in range(k_)]
    return [[sum((r[i] - mu[i]) * (r[j] - mu[j]) for r in rows) / (len(rows) - 1) for j in range(k_)] for i in range(k_)]
def ref_matrix(fn, A, B, **kw): return [[fn(a, b, **kw) for b in B] for a in A]
Vq = [F(rng.randint(1, 8), 4) for _ in range(nf)]; Va = np.array([float(v) for v in Vq])
Bq = [[F(rng.randint(-2, 2)) for _ in range(nf)] for _ in range(nf)]
Sq = [[sum(Bq[i][k] * Bq[j][k] for k in range(nf)) + (2 if i == j else 0) for j in range(nf)] for i in range(nf)]   # SPD
VIq = fr_inv(Sq); Sa = np.array([[float(v) for v in r] for r in Sq]); VIa = np.array([[float(v) for v in r] for r in VIq])
wq = [F(rng.randint(1, 6), 2) for _ in range(nf)]; wa = np.array([float(v) for v in wq])
cases = [("euclidean", d_euc, {}, {}), ("l2", d_euc, {}, {}), ("sqeuclidean", d_sqe, {}, {}),
         ("manhattan", d_man, {}, {}), ("l1", d_man, {}, {}), ("cityblock", d_man, {}, {}),
         ("chebyshev", d_cheb, {}, {}), ("minkowski", d_mink, {"p": 3}, {"p": 3}),
         ("minkowski", d_mink, {"p": 3, "w": wa}, {"p": 3, "w": wq}), ("minkowski", d_euc, {}, {}),
         ("cosine", d_cos, {}, {}), ("correlation", d_corr, {}, {}), ("braycurtis", d_bray_scipy, {}, {}),
         ("canberra", d_canb, {}, {}), ("hamming", d_ham, {}, {}), ("seuclidean", d_seuc, {"V": Va}, {"V": Vq}),
         ("mahalanobis", d_maha, {"VI": VIa}, {"VI": VIq})]
for name, fn, kw, kwq in cases:
    if name == "minkowski" and "w" in kw and V < (1, 0): continue
    try:
        got = pairwise_distances(Xa, Ya, metric=name, **kw); det = ""
    except Exception as e:
        got = None; det = f"({type(e).__name__}: {str(e)[:100]})"
    want = ref_matrix(fn, Xq, Yq, **kwq)
    kws = ", ".join(f"{k}=..." for k in kw)
    report(f"pairwise_distances(X, Y, metric='{name}'{', ' + kws if kws else ''}) = plain-Python formula on every pair", got is not None and mat_close(got, [[float(v) for v in r] for r in want], 1e-12, 1e-12), det)
print(f"   euclidean distance of the identical pair (X[3], Y[2]): {pairwise_distances(Xa, Ya)[3, 2]!r}")
report("pairwise_distances('braycurtis') on signed data uses scipy's sum|x-y| / sum|x+y| (sklearn defers to scipy for this name)", mat_close(pairwise_distances(Xa, Ya, metric="braycurtis"), [[float(d_bray_scipy(a, b)) for b in Yq] for a in Xq]))
# defaults V / VI from the data when Y is None (scipy's documented defaults for pdist)
Vdef = [fr_var(Xq, j) for j in range(nf)]
got = pairwise_distances(Xa, metric="seuclidean")
report("pairwise_distances(X, metric='seuclidean') without V uses V = var(X, ddof=1) per feature (scipy pdist default)", mat_close(got, [[float(d_seuc(a, b, Vdef)) for b in Xq] for a in Xq], 1e-12, 1e-12))
report("... and n_jobs=2 gives the same matrix (V is computed once, not per slice)", mat_close(pairwise_distances(Xa, metric="seuclidean", n_jobs=2), got, 1e-14, 1e-14))
Xq7 = [qrow(nf) for _ in range(9)]; Xa7 = np.array([[float(v) for v in r] for r in Xq7])
VIdef = fr_inv(fr_cov(Xq7))
got = pairwise_distances(Xa7, metric="mahalanobis")
report("pairwise_distances(X, metric='mahalanobis') without VI uses VI = inv(cov(X.T)) (scipy pdist default)", mat_close(got, [[float(d_maha(a, b, VIdef)) for b in Xq7] for a in Xq7], 1e-10, 1e-10))
report("... and n_jobs=2 gives the same matrix", mat_close(pairwise_distances(Xa7, metric="mahalanobis", n_jobs=2), got, 1e-12, 1e-12))
for name in ["seuclidean", "mahalanobis"]:
    try:
        pairwise_distances(Xa, Ya, metric=name); msg = "no error (scipy default from vstack(X, Y))"
    except Exception as e: msg = f"{type(e).__name__}: {str(e)[:90]}"
    print(f"   pairwise_distances(X, Y, metric='{name}') without V/VI: {msg}")
# haversine
rng = random.Random(1441)
Hx = [[rng.uniform(-1.4, 1.4), rng.uniform(-3.1, 3.1)] for _ in range(5)]; Hy = [[rng.uniform(-1.4, 1.4), rng.uniform(-3.1, 3.1)] for _ in range(4)]
Hy[0] = [-Hx[0][0], Hx[0][1] + math.pi]  # antipode
def d_hav(x, y):
    x = [mpmath.mpf(v) for v in x]; y = [mpmath.mpf(v) for v in y]
    return 2 * mpmath.asin(mpmath.sqrt(mpmath.sin((x[0] - y[0]) / 2) ** 2 + mpmath.cos(x[0]) * mpmath.cos(y[0]) * mpmath.sin((x[1] - y[1]) / 2) ** 2))
got = pw.haversine_distances(np.array(Hx), np.array(Hy))
report("haversine_distances = 2 arcsin(sqrt(sin^2(dlat/2) + cos lat1 cos lat2 sin^2(dlon/2))) (docstring formula)", mat_close(got, [[float(d_hav(a, b)) for b in Hy] for a in Hx], 1e-7, 1e-7), f"(max err {np.abs(got - np.array([[float(d_hav(a, b)) for b in Hy] for a in Hx])).max():.2e}; antipode {got[0, 0]:.15f} vs pi)")
report("pairwise_distances(metric='haversine') == haversine_distances", mat_close(pairwise_distances(np.array(Hx), np.array(Hy), metric="haversine"), got, 1e-15, 1e-15))
report("haversine_distances with 3 columns raises ValueError ('The dimension of the data must be 2')", raises(ValueError, pw.haversine_distances, Xa[:, :3]))
# nan_euclidean
nan = float("nan")
report("nan_euclidean_distances docstring example [3,na,na,6] vs [1,na,4,5] = sqrt(4/2 ((3-1)^2 + (6-5)^2))", close(pw.nan_euclidean_distances([[3, nan, nan, 6]], [[1, nan, 4, 5]])[0, 0], math.sqrt(4 / 2 * (4 + 1))))
Xn = [list(r) for r in Xq]; Yn = [list(r) for r in Yq]
for (i, j) in [(0, 1), (1, 0), (1, 3), (2, 2), (4, 0), (4, 1), (4, 2)]: Xn[i][j] = None
for (i, j) in [(0, 0), (1, 2), (3, 1), (3, 3)]: Yn[i][j] = None
Xn[5] = [None] * nf                                     # all missing row
def d_nan(x, y, squared=False):
    pres = [(a, b) for a, b in zip(x, y) if a is not None and b is not None]
    if not pres: return None
    v = F(len(x), len(pres)) * sum((a - b) ** 2 for a, b in pres); return v if squared else msqrt(v)
to_arr = lambda R: np.array([[nan if v is None else float(v) for v in r] for r in R])
for sq in [False, True]:
    got = pw.nan_euclidean_distances(to_arr(Xn), to_arr(Yn), squared=sq)
    want = [[d_nan(a, b, sq) for b in Yn] for a in Xn]
    ok_ = all((want[i][j] is None and math.isnan(got[i, j])) or (want[i][j] is not None and close(got[i, j], want[i][j], 1e-12, 1e-12)) for i in range(6) for j in range(5))
    report(f"nan_euclidean_distances(squared={sq}): weight = n_features / n_present on each pair, NaN when no common present coordinate", ok_)
report("pairwise_distances(metric='nan_euclidean') == nan_euclidean_distances", mat_close(pairwise_distances(to_arr(Xn), to_arr(Yn), metric="nan_euclidean"), pw.nan_euclidean_distances(to_arr(Xn), to_arr(Yn))))
Xm = to_arr(Xq); Xm[Xm == Xm[0, 0]] = -99.0
report("nan_euclidean_distances(missing_values=-99) treats -99 as missing", mat_close(pw.nan_euclidean_distances(Xm, missing_values=-99), pw.nan_euclidean_distances(np.where(Xm == -99, nan, Xm))))
Dn = pw.nan_euclidean_distances(to_arr(Xn[:5]))
report("nan_euclidean_distances(X) (Y=None) has a zero diagonal and is symmetric (NaN where no common coordinate)", np.allclose(np.diag(Dn), 0) and np.allclose(Dn, Dn.T, equal_nan=True))
# boolean metrics
print("---- pairwise: boolean metrics (scipy names) and DistanceMetric boolean classes")
rng = random.Random(1442)
nb_ = 7
Xbq = [[rng.random() < 0.5 for _ in range(nb_)] for _ in range(6)]; Ybq = [[rng.random() < 0.5 for _ in range(nb_)] for _ in range(5)]
for r in Xbq + Ybq:
    if not any(r): r[0] = True
    if all(r): r[-1] = False
Ybq[1] = list(Xbq[1])
def cnt(x, y):
    tt = sum(a and b for a, b in zip(x, y)); tf = sum(a and not b for a, b in zip(x, y)); ft = sum(b and not a for a, b in zip(x, y)); ff = len(x) - tt - tf - ft
    return tt, tf, ft, ff
def b_dice(x, y): tt, tf, ft, ff = cnt(x, y); return F(tf + ft, 2 * tt + tf + ft)
def b_jac(x, y): tt, tf, ft, ff = cnt(x, y); return F(tf + ft, tt + tf + ft) if tt + tf + ft else F(0)
def b_rt(x, y): tt, tf, ft, ff = cnt(x, y); R = 2 * (tf + ft); return F(R, tt + ff + R)
def b_rr(x, y): tt, tf, ft, ff = cnt(x, y); return F(len(x) - tt, len(x))
def b_ss(x, y): tt, tf, ft, ff = cnt(x, y); R = 2 * (tf + ft); return F(R, tt + R) if tt + R else F(0)
def b_yule(x, y): tt, tf, ft, ff = cnt(x, y); R = 2 * tf * ft; return F(R, tt * ff + R // 2) if R else F(0)
def b_sm(x, y): tt, tf, ft, ff = cnt(x, y); R = 2 * (tf + ft); return F(R, ff + tt + R)
def b_kul(x, y): tt, tf, ft, ff = cnt(x, y); n_ = len(x); return F(tf + ft - tt + n_, ft + tf + n_)
def b_match(x, y): tt, tf, ft, ff = cnt(x, y); return F(tf + ft, len(x))
bool_refs = {"dice": b_dice, "jaccard": b_jac, "rogerstanimoto": b_rt, "russellrao": b_rr, "sokalsneath": b_ss, "yule": b_yule,
             "sokalmichener": b_sm, "kulsinski": b_kul, "matching": b_match, "hamming": b_match}
Xb = np.array(Xbq, dtype=float); Yb = np.array(Ybq, dtype=float)
Xb_nz = Xb * np.array([rng.choice([2.0, -1.0, 0.5]) for _ in range(nb_)])   # nonzero -> True
def scipy_knows(name):
    try:
        from scipy.spatial import distance as sd_
        sd_.cdist(np.eye(2, dtype=bool), np.eye(2, dtype=bool), metric=name); return True
    except Exception: return False
for name in sorted(set(pw.PAIRWISE_BOOLEAN_FUNCTIONS) | {"hamming", "matching"}):
    if not scipy_knows(name):
        print(f"   '{name}' is in PAIRWISE_BOOLEAN_FUNCTIONS but this scipy no longer provides it (environment: scipy newer than the release supports) -> not checked")
        continue
    if name not in bool_refs: report(f"boolean metric '{name}' has a reference", False); continue
    want = [[float(bool_refs[name](a, b)) for b in Ybq] for a in Xbq]
    try:
        got = pairwise_distances(Xb, Yb, metric=name); got_nz = pairwise_distances(Xb_nz, Yb, metric=name) if name not in ("hamming", "matching") else got; det = ""
    except Exception as e:
        got = got_nz = None; det = f"({type(e).__name__}: {str(e)[:100]})"
    report(f"pairwise_distances(metric='{name}') on 0/1 data = scipy's documented boolean formula" + ("; non-zero entries count as True" if name not in ("hamming", "matching") else ""), got is not None and mat_close(got, want) and mat_close(got_nz, want), det)
# names listed in the docstring must be accepted (or carry a removal note)
doc = pairwise_distances.__doc__
m_ = re.search(r"From (?::mod:`)?scipy.spatial.distance`?: \[(.*?)\]", doc, re.S)
listed = re.findall(r"'(\w+)'", m_.group(1)) if m_ else []
notes = re.findall(r"`'(\w+)'` (?:is deprecated|has been removed)", doc)
print(f"   docstring lists scipy metrics {listed}; removal/deprecation notes for {notes}")
for name in listed:
    try:
        pairwise_distances(Xb, Yb, metric=name, **({"V": np.ones(nb_)} if name == "seuclidean" else {"VI": np.eye(nb_)} if name == "mahalanobis" else {})); acc = True; det = ""
    except Exception as e:
        acc = False; det = f"({type(e).__name__}: {str(e)[:80]})"
    # scipy removed kulsinski in 1.11 (June 2023) and sokalmichener in 1.17; a sklearn release older than that removal
    # cannot be blamed for listing it (environment artifact of pairing an old sklearn with a newer scipy)
    predates = (name == "kulsinski" and V < (1, 3)) or (name == "sokalmichener" and V < (1, 8))
    if not acc and predates and not scipy_knows(name):
        print(f"   docstring-listed '{name}' rejected, but this sklearn release predates scipy's removal of it (environment artifact) {det}"); continue
    report(f"pairwise_distances accepts metric='{name}' listed in its docstring (or the docstring notes its removal)", acc or name in notes, det)
try:
    pairwise_distances(Xa, Ya, metric="wminkowski", p=2, w=np.ones(nf)); msg = "accepted"
except Exception as e: msg = f"{type(e).__name__}: {str(e)[:80]}"
print(f"   'wminkowski' (in _VALID_METRICS: {'wminkowski' in getattr(pw, '_VALID_METRICS', [])}; not in the docstring): {msg}")
# Y=None symmetry, n_jobs, sparse
print("---- pairwise: Y=None symmetry, n_jobs, sparse input, callables, precomputed")
for name in ["euclidean", "manhattan", "cosine", "chebyshev", "canberra", "correlation", "minkowski", "braycurtis", "sqeuclidean"]:
    D1 = pairwise_distances(Xa, metric=name); D2 = pairwise_distances(Xa, Xa, metric=name)
    exact_diag = name in ("euclidean",) or name not in pw.PAIRWISE_DISTANCE_FUNCTIONS
    report(f"pairwise_distances(X, metric='{name}') with Y=None: symmetric, zero diagonal{' (exactly)' if exact_diag else ''}, equal to pairwise_distances(X, X)",
           mat_close(D1, D1.T, 1e-12, 1e-12) and (np.all(np.diag(D1) == 0) if exact_diag else np.allclose(np.diag(D1), 0, atol=1e-12)) and mat_close(D1, D2, 1e-12, 1e-12))
    report(f"pairwise_distances(metric='{name}', n_jobs=2) == n_jobs=1 ('breaking down the pairwise matrix into n_jobs even slices')", np.array_equal(pairwise_distances(Xa, Ya, metric=name, n_jobs=2), pairwise_distances(Xa, Ya, metric=name)))
Xs = sp_.csr_matrix(np.where(np.abs(Xa) < 1, 0, Xa)); Ys = sp_.csr_matrix(np.where(np.abs(Ya) < 1, 0, Ya))
for name in ["euclidean", "manhattan", "cosine", "l1", "l2", "cityblock"]:
    report(f"pairwise_distances(metric='{name}') on CSR input == dense ('All metrics support sparse matrix inputs except nan_euclidean')", mat_close(pairwise_distances(Xs, Ys, metric=name), pairwise_distances(Xs.toarray(), Ys.toarray(), metric=name), 1e-12, 1e-12))
report("pairwise_distances(metric='chebyshev') on sparse input raises TypeError (scipy metrics 'do not support sparse matrix inputs')", raises(TypeError, pairwise_distances, Xs, Ys, metric="chebyshev"))
cb = lambda x, y: float(np.abs(x - y).max() + 1)
report("pairwise_distances(metric=callable) calls it on every pair of rows", mat_close(pairwise_distances(Xa, Ya, metric=cb), [[float(d_cheb(a, b) + 1) for b in Yq] for a in Xq]))
Dcb = pairwise_distances(Xa, metric=cb)
report("pairwise_distances(metric=callable, Y=None): symmetric result", mat_close(Dcb, Dcb.T))
print(f"   callable metric with Y=None: diagonal = {np.diag(Dcb).tolist()} (callable(x, x) = 1 here; sklearn {'sets it to 0' if np.all(np.diag(Dcb) == 0) else 'evaluates it'})")
Dp = np.abs(np.subtract.outer(np.arange(4.0), np.arange(4.0)))
report("pairwise_distances(metric='precomputed') returns X as is", np.array_equal(pairwise_distances(Dp, metric="precomputed"), Dp))
report("pairwise_distances(metric='precomputed') with negative entries raises ValueError", raises(ValueError, pairwise_distances, -Dp - 1, metric="precomputed"))
# argmin / argmin_min
print("---- pairwise: argmin, argmin_min, chunked, paired")
def argmin_ref(fn, A, B, **kw):
    out = []
    for a in A:
        ds = [fn(a, b, **kw) for b in B]; m__ = min(ds); out.append((ds.index(m__), m__, sum(1 for d in ds if d == m__)))
    return out
for name, fn, kw, kwq in [("euclidean", d_sqe, {}, {}), ("manhattan", d_man, {}, {}), ("cosine", d_cos, {}, {}), ("minkowski", d_mink, {"p": 3}, {"p": 3}), ("chebyshev", d_cheb, {}, {})]:
    ref = argmin_ref(fn, Xq, Yq, **kwq)
    idx, dist = metrics.pairwise_distances_argmin_min(Xa, Ya, metric=name, metric_kwargs=kw or None)
    idx2 = metrics.pairwise_distances_argmin(Xa, Ya, metric=name, metric_kwargs=kw or None)
    ties = [i for i, r in enumerate(ref) if r[2] > 1]
    ok_ = all((idx[i] == ref[i][0] or i in ties) and close(dist[i], float(msqrt(ref[i][1]) if name == "euclidean" else ref[i][1]), 1e-12, 1e-12) for i in range(6))
    report(f"pairwise_distances_argmin_min(metric='{name}'{', metric_kwargs' if kw else ''}): index of the closest Y row and its distance", ok_ and np.array_equal(idx, idx2), f"(rows with tied minima: {ties})" if ties else "")
    if ties: print(f"   tied rows {ties}: sklearn chose {[int(idx[i]) for i in ties]}, first index would be {[ref[i][0] for i in ties]}")
idx0, d0 = metrics.pairwise_distances_argmin_min(Xa, Ya, axis=0)
ref0 = argmin_ref(d_sqe, Yq, Xq)
report("pairwise_distances_argmin_min(axis=0): for each Y row the closest X row", all(idx0[j] == ref0[j][0] and close(d0[j], float(msqrt(ref0[j][1]))) for j in range(5)))
Xt = np.array([[0.0, 0.0], [5.0, 5.0]]); Yt = np.array([[1.0, 0.0], [0.0, 1.0], [-1.0, 0.0], [6.0, 5.0], [5.0, 6.0]])
print(f"   argmin with exact ties (distance 1 to three / two Y rows): {metrics.pairwise_distances_argmin(Xt, Yt).tolist()} (np.argmin convention would be [0, 3])")
# chunked
full = pairwise_distances(Xa7)
wm = 2 * 8 * 9 / 2 ** 20            # room for exactly two float64 rows of 9 columns
chunks = list(metrics.pairwise_distances_chunked(Xa7, working_memory=wm))
report("pairwise_distances_chunked: vertical chunks that concatenate to pairwise_distances(X)", mat_close(np.vstack(chunks), full, 1e-12, 1e-12))
report(f"pairwise_distances_chunked(working_memory={wm:.3g} MiB = two 9-column float64 rows): every chunk fits ('sought maximum memory'), so chunk sizes <= 2", all(c.shape[0] <= 2 for c in chunks) and len(chunks) >= 5, f"(sizes {[c.shape[0] for c in chunks]})")
starts = []
def red(D, start):
    starts.append(start); return [np.flatnonzero(row < 2.5).tolist() for row in D]
nbrs = [x for c in metrics.pairwise_distances_chunked(Xa7, reduce_func=red, working_memory=wm) for x in c]
want = [[j for j in range(9) if d_sqe(Xq7[i], Xq7[j]) < F(25, 4)] for i in range(9)]
report("pairwise_distances_chunked(reduce_func): radius neighbours from the reduced chunks = exact neighbours", nbrs == want)
report("reduce_func(D_chunk, start): 'start' is the first row index of each chunk", starts == list(np.cumsum([0] + [c.shape[0] for c in chunks])[:-1]), f"(starts {starts})")
tup = list(metrics.pairwise_distances_chunked(Xa7, reduce_func=lambda D, s: (D.min(axis=1), D.argmax(axis=1)), working_memory=wm))
report("reduce_func returning a tuple yields tuples of per-chunk results", all(isinstance(t, tuple) and len(t) == 2 for t in tup) and np.allclose(np.concatenate([t[0] for t in tup]), full.min(axis=1)))
def bad(D, s): return D[:1]
report("reduce_func returning the wrong length raises ValueError ('should return ... of length D_chunk.shape[0]')", raises(ValueError, lambda: list(metrics.pairwise_distances_chunked(Xa7, reduce_func=bad, working_memory=wm))))
chs = list(metrics.pairwise_distances_chunked(Xa7, metric="seuclidean", working_memory=wm))
report("pairwise_distances_chunked(metric='seuclidean') without V: V from the whole X, not per chunk", mat_close(np.vstack(chs), pairwise_distances(Xa7, metric="seuclidean"), 1e-12, 1e-12))
chy = list(metrics.pairwise_distances_chunked(Xa, Ya, metric="manhattan", working_memory=8 * 5 / 2 ** 20))
report("pairwise_distances_chunked(X, Y, working_memory = one row) yields single rows equal to pairwise_distances(X, Y)", all(c.shape[0] == 1 for c in chy) and mat_close(np.vstack(chy), [[float(d_man(a, b)) for b in Yq] for a in Xq]))
# paired
Pa, Pb = Xa[:5], Ya
for name, fn in [("euclidean", d_euc), ("l2", d_euc), ("manhattan", d_man), ("l1", d_man), ("cityblock", d_man), ("cosine", d_cos)]:
    got = metrics.pairwise.paired_distances(Pa, Pb, metric=name)
    report(f"paired_distances(metric='{name}') = d(X[i], Y[i]) row by row", mat_close(got, [float(fn(a, b)) for a, b in zip(Xq[:5], Yq)], 1e-12, 1e-12))
report("paired_cosine_distances = 1 - cos = half the squared euclidean distance of the unit-normalised rows (docstring note)", mat_close(pw.paired_cosine_distances(Pa, Pb), [float(d_cos(a, b)) for a, b in zip(Xq[:5], Yq)], 1e-12, 1e-12))
report("paired_distances(metric=callable) applies it row by row", mat_close(metrics.pairwise.paired_distances(Pa, Pb, metric=lambda x, y: float(np.abs(x - y).max())), [float(d_cheb(a, b)) for a, b in zip(Xq[:5], Yq)]))
report("paired_distances with different numbers of rows raises ValueError", raises(ValueError, metrics.pairwise.paired_distances, Xa, Ya))
report("paired_distances(metric='chebyshev') (not in PAIRED_DISTANCES) raises ValueError", raises(ValueError, metrics.pairwise.paired_distances, Pa, Pb, metric="chebyshev"))

# ---- euclidean_distances norms, cosine clipping
print("---- pairwise: euclidean_distances with given norms, cosine clipping")
xx = (Xa ** 2).sum(1); yy = (Ya ** 2).sum(1)
want = [[float(d_euc(a, b)) for b in Yq] for a in Xq]
report("euclidean_distances with the correct X_norm_squared / Y_norm_squared = exact distances", mat_close(pw.euclidean_distances(Xa, Ya, X_norm_squared=xx, Y_norm_squared=yy), want, 1e-12, 1e-12))
report("... norms given as (n, 1) and (1, n) shapes are accepted", mat_close(pw.euclidean_distances(Xa, Ya, X_norm_squared=xx[:, None], Y_norm_squared=yy[None, :]), want, 1e-12, 1e-12))
report("euclidean_distances(squared=True) = sum of squares", mat_close(pw.euclidean_distances(Xa, Ya, squared=True), [[float(d_sqe(a, b)) for b in Yq] for a in Xq], 1e-12, 1e-12))
got = pw.euclidean_distances(Xa, Ya, X_norm_squared=xx + 1, Y_norm_squared=yy)
report("float64: given norms are used in dist = sqrt(dot(x,x) - 2 dot(x,y) + dot(y,y)): X norms + 1 -> sqrt(d^2 + 1)", mat_close(got, [[float(mpmath.sqrt(d_sqe(a, b) + 1)) for b in Yq] for a in Xq], 1e-12, 1e-12))
got32 = pw.euclidean_distances(Xa.astype(np.float32), Ya.astype(np.float32), X_norm_squared=(xx + 1).astype(np.float32))
print(f"   float32 input with wrong X_norm_squared: max |d - true| = {np.abs(got32 - np.array(want)).max():.2e} ('may be unused if passed as np.float32')")
Xr = np.array([[0.1, 0.2, 0.3], [1e8, 1.0, 1.0]]); Yr = np.array([[0.3, 0.6, 0.9], [-0.1, -0.2, -0.3], [3e8, 3.0, 3.0]])
Cd = pw.cosine_distances(Xr, Yr); Cs = pw.cosine_similarity(Xr, Yr)
report("cosine_distances clipped to [0, 2]: parallel rows give >= 0, antiparallel <= 2", Cd.min() >= 0 and Cd.max() <= 2 and close(Cd[0, 1], 2.0, 1e-15) and abs(Cd[0, 0]) < 1e-15, f"(parallel {Cd[0, 0]!r}, antiparallel {Cd[0, 1]!r}, similarity {Cs[0, 0]!r})")
Cself = pw.cosine_distances(Xa)
report("cosine_distances(X) with Y=None: exactly zero diagonal", np.all(np.diag(Cself) == 0))
report("cosine_similarity = <x,y>/(|x||y|) on every pair", mat_close(pw.cosine_similarity(Xa, Ya), [[float(1 - d_cos(a, b)) for b in Yq] for a in Xq], 1e-12, 1e-12))
report("cosine_similarity(dense_output=False) on two CSR inputs returns sparse with the same values", sp_.issparse(pw.cosine_similarity(Xs, Ys, dense_output=False)) and mat_close(pw.cosine_similarity(Xs, Ys, dense_output=False).toarray(), pw.cosine_similarity(Xs.toarray(), Ys.toarray()), 1e-12, 1e-12))
Z = np.vstack([np.zeros(nf), Xa[0]])
print(f"   cosine_similarity with a zero row (undocumented): {pw.cosine_similarity(Z)[0].tolist()}, cosine_distances: {pw.cosine_distances(Z)[0].tolist()}")

# ---- kernels
print("---- pairwise: every kernel in PAIRWISE_KERNEL_FUNCTIONS, default gamma, filter_params, callables")
rng = random.Random(1443)
Kx = [qrow(nf, 0, 8) for _ in range(5)]; Ky = [qrow(nf, 0, 8) for _ in range(4)]
Kx[0][1] = F(0); Ky[0][1] = F(0)                 # a 0/0 chi2 term
Kxa = np.array([[float(v) for v in r] for r in Kx]); Kya = np.array([[float(v) for v in r] for r in Ky])
dot = lambda x, y: sum(a * b for a, b in zip(x, y))
def chi2_sum(x, y): return sum(((a - b) ** 2 / (a + b) for a, b in zip(x, y) if a + b != 0), F(0))
g0 = F(1, nf)
k_refs = {
    "linear": (lambda x, y: dot(x, y), {}),
    "poly": (lambda x, y: (g0 * dot(x, y) + 1) ** 3, {}), "polynomial": (lambda x, y: (g0 * dot(x, y) + 1) ** 3, {}),
    "rbf": (lambda x, y: mpmath.exp(-mp(g0 * d_sqe(x, y))), {}),
    "laplacian": (lambda x, y: mpmath.exp(-mp(g0 * d_man(x, y))), {}),
    "sigmoid": (lambda x, y: mpmath.tanh(mp(g0 * dot(x, y) + 1)), {}),
    "cosine": (lambda x, y: 1 - d_cos(x, y), {}),
    "chi2": (lambda x, y: mpmath.exp(-mp(chi2_sum(x, y))), {}),          # documented default gamma=1 (not 1/n_features)
    "additive_chi2": (lambda x, y: -chi2_sum(x, y), {}),
}
for name in sorted(pw.PAIRWISE_KERNEL_FUNCTIONS):
    if name not in k_refs: report(f"kernel '{name}' has a reference", False); continue
    fn, _ = k_refs[name]
    got = metrics.pairwise_kernels(Kxa, Kya, metric=name)
    report(f"pairwise_kernels(metric='{name}') with default parameters = docstring formula{' (gamma = 1/n_features)' if name in ('poly', 'polynomial', 'rbf', 'laplacian', 'sigmoid') else ' (gamma default 1)' if name == 'chi2' else ''}", mat_close(got, [[float(fn(a, b)) for b in Ky] for a in Kx], 1e-12, 1e-12))
    report(f"pairwise_kernels(metric='{name}') == the PAIRWISE_KERNEL_FUNCTIONS function", mat_close(got, pw.PAIRWISE_KERNEL_FUNCTIONS[name](Kxa, Kya), 1e-15, 1e-15))
    K1 = metrics.pairwise_kernels(Kxa, metric=name)
    report(f"pairwise_kernels(metric='{name}', Y=None) is symmetric and equals K(X, X)", mat_close(K1, K1.T, 1e-12, 1e-12) and mat_close(K1, metrics.pairwise_kernels(Kxa, Kxa, metric=name), 1e-12, 1e-12))
g = F(3, 10); d_ = 2; c0 = F(-1, 2)
explicit = [("polynomial", dict(gamma=0.3, degree=2, coef0=-0.5), lambda x, y: (g * dot(x, y) + c0) ** d_),
            ("rbf", dict(gamma=0.3), lambda x, y: mpmath.exp(-mp(g * d_sqe(x, y)))),
            ("laplacian", dict(gamma=0.3), lambda x, y: mpmath.exp(-mp(g * d_man(x, y)))),
            ("sigmoid", dict(gamma=0.3, coef0=-0.5), lambda x, y: mpmath.tanh(mp(g * dot(x, y) + c0))),
            ("chi2", dict(gamma=0.3), lambda x, y: mpmath.exp(-mp(g * chi2_sum(x, y))))]
for name, kw, fn in explicit:
    report(f"pairwise_kernels(metric='{name}', {kw})", mat_close(metrics.pairwise_kernels(Kxa, Kya, metric=name, **kw), [[float(fn(a, b)) for b in Ky] for a in Kx], 1e-12, 1e-12))
report("chi2_kernel with negative input raises ValueError ('X and Y have to be non-negative')", raises(ValueError, pw.chi2_kernel, Xa, Ya))
report("additive_chi2_kernel with negative input raises ValueError", raises(ValueError, pw.additive_chi2_kernel, Xa, Ya))
report("pairwise_kernels(metric='linear', filter_params=True, gamma=3): the invalid gamma is filtered out", mat_close(metrics.pairwise_kernels(Kxa, Kya, metric="linear", filter_params=True, gamma=3.0), [[float(dot(a, b)) for b in Ky] for a in Kx]))
report("pairwise_kernels(metric='rbf', filter_params=True, gamma=0.3, degree=5): degree filtered, gamma kept", mat_close(metrics.pairwise_kernels(Kxa, Kya, metric="rbf", filter_params=True, gamma=0.3, degree=5), [[float(mpmath.exp(-mp(g * d_sqe(a, b)))) for b in Ky] for a in Kx], 1e-12, 1e-12))
report("pairwise_kernels(metric='linear', gamma=3) without filter_params raises TypeError", raises(TypeError, metrics.pairwise_kernels, Kxa, Kya, metric="linear", gamma=3.0))
kc = lambda x, y, s=1.0: float(s * np.dot(x, y) + 1)
report("pairwise_kernels(metric=callable) evaluates it on every pair of rows", mat_close(metrics.pairwise_kernels(Kxa, Kya, metric=kc), [[float(dot(a, b) + 1) for b in Ky] for a in Kx]))
report("pairwise_kernels(metric=callable, s=2) passes the keyword to the callable", mat_close(metrics.pairwise_kernels(Kxa, Kya, metric=kc, s=2.0), [[float(2 * dot(a, b) + 1) for b in Ky] for a in Kx]))
Kp = metrics.pairwise_kernels(Kxa, metric="rbf")
report("pairwise_kernels(metric='precomputed') returns X as is", np.array_equal(metrics.pairwise_kernels(Kp, metric="precomputed"), Kp))
report("pairwise_kernels(n_jobs=2) == n_jobs=1", np.array_equal(metrics.pairwise_kernels(Kxa, Kya, metric="rbf", n_jobs=2), metrics.pairwise_kernels(Kxa, Kya, metric="rbf")))
Ksx = sp_.csr_matrix(Kxa); Ksy = sp_.csr_matrix(Kya)
for name in ["linear", "poly", "rbf", "sigmoid", "cosine", "laplacian"]:
    report(f"pairwise_kernels(metric='{name}') on CSR input == dense", mat_close(metrics.pairwise_kernels(Ksx, Ksy, metric=name), metrics.pairwise_kernels(Kxa, Kya, metric=name), 1e-12, 1e-12))
report("rbf_kernel(gamma=None) on X with 4 features: gamma = 0.25 (docstring '1.0 / n_features')", mat_close(pw.rbf_kernel(Kxa, Kya), pw.rbf_kernel(Kxa, Kya, gamma=0.25), 1e-15, 1e-15))

# ---- DistanceMetric
print("---- DistanceMetric.get_metric: every documented identifier, pairwise, rdist round trip, float32")
dm_cases = [("euclidean", {}, d_euc, {}), ("l2", {}, d_euc, {}), ("manhattan", {}, d_man, {}), ("cityblock", {}, d_man, {}), ("l1", {}, d_man, {}),
            ("chebyshev", {}, d_cheb, {}), ("infinity", {}, d_cheb, {}), ("minkowski", {"p": 3}, d_mink, {"p": 3}), ("p", {"p": 3}, d_mink, {"p": 3}),
            ("minkowski", {"p": 3, "w": wa}, d_mink, {"p": 3, "w": wq}), ("minkowski", {"p": 1}, d_man, {}), ("minkowski", {"p": 2}, d_euc, {}),
            ("seuclidean", {"V": Va}, d_seuc, {"V": Vq}), ("mahalanobis", {"VI": VIa}, d_maha, {"VI": VIq}), ("mahalanobis", {"V": Sa}, d_maha, {"VI": VIq}),
            ("hamming", {}, d_ham, {}), ("canberra", {}, d_canb, {}), ("braycurtis", {}, d_bray_skl, {})]
for name, kw, fn, kwq in dm_cases:
    try:
        dm = DistanceMetric.get_metric(name, **kw); got = dm.pairwise(Xa, Ya); gotself = dm.pairwise(Xa); det = ""
    except Exception as e:
        got = None; det = f"({type(e).__name__}: {str(e)[:100]})"
    want = [[float(fn(a, b, **kwq)) for b in Yq] for a in Xq]
    kws = ", ".join(f"{k}=..." for k in kw)
    report(f"DistanceMetric.get_metric('{name}'{', ' + kws if kws else ''}).pairwise(X, Y) = docstring formula", got is not None and mat_close(got, want, 1e-12, 1e-12), det)
    if got is not None:
        report(f"   ... pairwise(X) symmetric with zero diagonal", mat_close(gotself, gotself.T, 1e-12, 1e-12) and np.allclose(np.diag(gotself), 0, atol=1e-7))
report("DistanceMetric 'braycurtis' uses sum|x-y| / (sum|x| + sum|y|) (its docstring), which differs from pairwise_distances('braycurtis') = scipy's sum|x+y| denominator on signed data",
       mat_close(DistanceMetric.get_metric("braycurtis").pairwise(Xa, Ya), [[float(d_bray_skl(a, b)) for b in Yq] for a in Xq]))
print(f"   braycurtis on signed data: DistanceMetric {DistanceMetric.get_metric('braycurtis').pairwise(Xa[:1], Ya[:1])[0, 0]:.6f} vs pairwise_distances {pairwise_distances(Xa[:1], Ya[:1], metric='braycurtis')[0, 0]:.6f}")
Hd = DistanceMetric.get_metric("haversine").pairwise(np.array(Hx), np.array(Hy))
report("DistanceMetric 'haversine' = docstring formula", mat_close(Hd, [[float(d_hav(a, b)) for b in Hy] for a in Hx], 1e-7, 1e-7))
dm_bool = {"jaccard": b_jac, "matching": b_match, "dice": b_dice, "kulsinski": b_kul, "rogerstanimoto": b_rt, "russellrao": b_rr, "sokalmichener": b_sm, "sokalsneath": b_ss}
def dm_doc_kul(x, y):
    tt, tf, ft, ff = cnt(x, y); nneq = tf + ft; n_ = len(x); return F(nneq + n_ - tt, nneq + n_)
dm_bool["kulsinski"] = dm_doc_kul
for name, fn in dm_bool.items():
    try:
        got = DistanceMetric.get_metric(name).pairwise(Xb_nz, Yb); det = ""
    except Exception as e:
        got = None; det = f"({type(e).__name__}: {str(e)[:100]})"
    report(f"DistanceMetric.get_metric('{name}') on boolean data (non-zero = True) = docstring formula", got is not None and mat_close(got, [[float(fn(a, b)) for b in Ybq] for a in Xbq]), det)
pyf = DistanceMetric.get_metric("pyfunc", func=lambda x, y: float(np.abs(x - y).sum() ** 0.5))
report("DistanceMetric 'pyfunc' with func", mat_close(pyf.pairwise(Xa, Ya), [[float(mpmath.sqrt(mp(d_man(a, b)))) for b in Yq] for a in Xq], 1e-12, 1e-12))
if V >= (1, 3):   # 1.3 changelog (1.3.1 fix): minkowski with 0 < p < 1 works; the class docstring says 'versionchanged 1.4.0'
    try:
        got = DistanceMetric.get_metric("minkowski", p=0.5).pairwise(Xa, Ya); det = ""
    except Exception as e: got = None; det = f"({type(e).__name__}: {e})"
    report("DistanceMetric minkowski p=0.5 (1.3.1+: 'allows p to be 0<p<1') = (sum |x-y|^0.5)^2", got is not None and mat_close(got, [[float(d_mink(a, b, p=0.5)) for b in Yq] for a in Xq], 1e-12, 1e-12), det)
    report("DistanceMetric.get_metric('minkowski', p=0) raises ValueError ('p must be greater than 0')", raises(ValueError, DistanceMetric.get_metric, "minkowski", p=0))
else:
    report("DistanceMetric.get_metric('minkowski', p=0.5) raises ValueError before 1.3 (p >= 1 required)", raises(ValueError, DistanceMetric.get_metric, "minkowski", p=0.5))
report("DistanceMetric.get_metric('nope') raises ValueError", raises(ValueError, DistanceMetric.get_metric, "nope"))
# reduced distance round trips
def rd_expect(dm, D, p=None):
    cn = type(dm).__name__.rstrip("0123456789")
    if cn in ("EuclideanDistance", "SEuclideanDistance", "MahalanobisDistance"): return D ** 2, "d^2"
    if cn == "MinkowskiDistance": return D ** p, "d^p"
    if cn == "HaversineDistance": return np.sin(D / 2) ** 2, "sin^2(d/2)"
    return D, "d itself"
for name, kw, _, _ in dm_cases[:15] + [("haversine", {}, None, None)]:
    dm = DistanceMetric.get_metric(name, **kw)
    D = dm.pairwise(np.array(Hx) if name == "haversine" else Xa, np.array(Hy) if name == "haversine" else Ya)
    rd = dm.dist_to_rdist(D); back = dm.rdist_to_dist(rd); exp_rd, lab = rd_expect(dm, D, kw.get('p'))
    report(f"DistanceMetric('{name}'{', p=' + str(kw['p']) if 'p' in kw else ''}) [{type(dm).__name__}]: rdist_to_dist(dist_to_rdist(D)) == D, reduced distance = {lab} (rank-preserving)",
           mat_close(back, D, 1e-12, 1e-7 if name == "haversine" else 1e-12) and mat_close(rd, exp_rd, 1e-12, 1e-12))
    if name == "haversine": print(f"   haversine round trip max |back - D| = {np.abs(back - D).max():.1e} (arcsin near 1 at the antipode loses ~sqrt(eps); tolerance 1e-7)")
# float32 variant
try:
    for name, kw, fn, kwq in dm_cases:
        kw32 = {k: v for k, v in kw.items()}
        dm32 = DistanceMetric.get_metric(name, dtype=np.float32, **kw32)
        got = dm32.pairwise(Xa.astype(np.float32), Ya.astype(np.float32))
        want = np.array([[float(fn(a, b, **kwq)) for b in Yq] for a in Xq])
        report(f"DistanceMetric.get_metric('{name}', dtype=np.float32) -> {type(dm32).__name__}: pairwise within float32 precision of the exact value", "32" in type(dm32).__name__ and np.allclose(got, want, rtol=2e-6, atol=2e-6), f"(max err {np.abs(got - want).max():.2e}, result dtype {got.dtype})")
except TypeError as e:
    print(f"   DistanceMetric.get_metric(dtype=np.float32) not supported on {sklearn.__version__}: {str(e)[:80]}")

# =====================================================================================
# F. scorers
# =====================================================================================
print("---- scorers: every get_scorer_names() entry on fixed-output estimators, make_scorer, check_scoring, multimetric")
from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
from sklearn.metrics import get_scorer, make_scorer, check_scoring
from sklearn.model_selection import cross_validate, KFold
class FixedClf(ClassifierMixin, BaseEstimator):
    """Classifier whose outputs are fixed tables indexed by X[:, 0] (so every score has an exact truth)."""
    def __init__(self, proba=None, dec=None, classes=None):
        self.proba = proba; self.dec = dec; self.classes = classes
    def fit(self, X, y=None):
        self.classes_ = np.asarray(self.classes); return self
    def _i(self, X): return np.asarray(X)[:, 0].astype(int)
    def predict_proba(self, X): return np.asarray(self.proba, dtype=float)[self._i(X)]
    def decision_function(self, X): return np.asarray(self.dec, dtype=float)[self._i(X)]
    def predict(self, X): return self.classes_[np.argmax(self.predict_proba(X), axis=1)]
class FixedReg(RegressorMixin, BaseEstimator):
    def __init__(self, pred=None): self.pred = pred
    def fit(self, X, y=None): return self
    def predict(self, X): return np.asarray(self.pred, dtype=float)[np.asarray(X)[:, 0].astype(int)]
rng = random.Random(1450)
# binary: decision_function deliberately ranks differently from predict_proba
nB = 30
yB = [1 if rng.random() < 0.45 else 0 for _ in range(nB)]
pB = [F(rng.choice([k for k in range(1, 16) if k != 8]), 16) for _ in range(nB)]
dB = [F(rng.randint(-8, 8), 4) for _ in range(nB)]
estB = FixedClf(proba=[[float(1 - p), float(p)] for p in pB], dec=[float(d) for d in dB], classes=[0, 1]).fit(None)
XB = np.c_[np.arange(nB), np.zeros(nB)]
predB = [int(p > F(1, 2)) for p in pB]
# multiclass
nM = 36
yM = [rng.randint(0, 2) for _ in range(nM)]; PM = []
for _ in range(nM):
    a = rng.randint(1, 10); b = rng.randint(1, 15 - a); PM.append([F(a, 16), F(b, 16), F(16 - a - b, 16)])
estM = FixedClf(proba=[[float(v) for v in r] for r in PM], dec=[[math.log(float(v)) for v in r] for r in PM], classes=[0, 1, 2]).fit(None)
XM = np.c_[np.arange(nM), np.zeros(nM)]
predM = [max(range(3), key=lambda c: (r[c], -c)) for r in PM]          # np.argmax: first maximum
# regression (positive targets for the log / deviance scorers)
nR = 24
yR = [F(rng.randint(1, 40), 4) for _ in range(nR)]; pRq = [max(v + F(rng.randint(-8, 8), 4), F(1, 4)) for v in yR]
estR = FixedReg(pred=[float(v) for v in pRq]).fit(None); XR = np.c_[np.arange(nR), np.zeros(nR)]
yRf = [float(v) for v in yR]

def pair_counts(a, b):
    n_ = len(a); tp = sum(1 for i in range(n_) for j in range(i + 1, n_) if a[i] == a[j] and b[i] == b[j])
    t_ = sum(1 for i in range(n_) for j in range(i + 1, n_) if a[i] == a[j]); p_ = sum(1 for i in range(n_) for j in range(i + 1, n_) if b[i] == b[j])
    return tp, t_, p_, n_ * (n_ - 1) // 2
def fm_exact(a, b): tp, t_, p_, _ = pair_counts(a, b); return tp / mpmath.sqrt(mp(F(t_ * p_)))
def rand_exact(a, b):
    tp, t_, p_, tot = pair_counts(a, b); return F(tot - t_ - p_ + 2 * tp, tot)
def ovr_auc(y, P, weighted=False):
    aucs = [auc_exact([int(t == c) for t in y], [r[c] for r in P]) for c in range(3)]
    return wmean(aucs, [sum(1 for t in y if t == c) for c in range(3)]) if weighted else fmean(aucs)
def ovo_pairs(y, P):
    out = []
    for j, k in itertools.combinations(range(3), 2):
        idx = [i for i, t in enumerate(y) if t in (j, k)]
        a_jk = auc_exact([int(y[i] == j) for i in idx], [P[i][j] for i in idx]); a_kj = auc_exact([int(y[i] == k) for i in idx], [P[i][k] for i in idx])
        out.append(((a_jk + a_kj) / 2, F(len(idx), len(y))))
    return out
mc_cnt = lambda y, p, l: counts([int(t == l) for t in y], [int(q == l) for q in p])
csB = [mc_cnt(yB, predB, l) for l in (0, 1)]; csM = [mc_cnt(yM, predM, l) for l in range(3)]
bin_counts = counts(yB, predB)
truth = {}
def T(name, val, sign=1): truth[name] = (sign, val)
# classification (binary estimator)
T("accuracy", F(sum(a == b for a, b in zip(yB, predB)), nB))
T("balanced_accuracy", bal_acc_w(yB, predB, [0, 1], [1] * nB))
for nm, wch in [("precision", "P"), ("recall", "R"), ("f1", "F")]:
    T(nm, prf_from(bin_counts, F(1), F(0))["PRF".index(wch)])
    for av in ["macro", "micro", "weighted"]: T(f"{nm}_{av}", prf_avg(csB, F(1), F(0), av, wch))
T("jaccard", jac(bin_counts, F(0)))
for av in ["macro", "micro", "weighted"]: T(f"jaccard_{av}", jac_avg(csB, F(0), av))
T("matthews_corrcoef", mcc_w(yB, predB, [0, 1], [1] * nB))
T("roc_auc", auc_exact(yB, dB))                    # ('decision_function', 'predict_proba'): decision_function first
T("average_precision", ap_exact(yB, dB))
T("neg_log_loss", -fmean(-mpmath.log(mp(p if y else 1 - p)) for y, p in zip(yB, pB)))
T("neg_brier_score", -fmean((F(y) - p) ** 2 for y, p in zip(yB, pB)))
T("positive_likelihood_ratio", clr_ref(yB, predB)[0]); T("neg_negative_likelihood_ratio", -clr_ref(yB, predB)[1])
nullB = F(sum(yB), nB)
T("d2_log_loss_score", 1 - sum(-mpmath.log(mp(p if y else 1 - p)) for y, p in zip(yB, pB)) / sum(-mpmath.log(mp(nullB if y else 1 - nullB)) for y in yB))
T("d2_brier_score", 1 - fmean((F(y) - p) ** 2 for y, p in zip(yB, pB)) / fmean((F(y) - nullB) ** 2 for y in yB))
# multiclass-only names evaluated on the multiclass estimator
multi_names = {"roc_auc_ovr": ovr_auc(yM, PM), "roc_auc_ovr_weighted": ovr_auc(yM, PM, True),
               "roc_auc_ovo": fmean(s for s, _ in ovo_pairs(yM, PM)), "roc_auc_ovo_weighted": wmean([s for s, _ in ovo_pairs(yM, PM)], [w_ for _, w_ in ovo_pairs(yM, PM)]),
               "top_k_accuracy": topk_ref(yM, PM, 2)}
# clustering scorers on the multiclass predictions
clus = {"adjusted_rand_score": ari_exact(yM, predM), "rand_score": rand_exact(yM, predM), "mutual_info_score": mi_exact(yM, predM),
        "normalized_mutual_info_score": nmi_exact(yM, predM), "homogeneity_score": mi_exact(yM, predM) / entropy_exact(yM),
        "completeness_score": mi_exact(yM, predM) / entropy_exact(predM), "fowlkes_mallows_score": fm_exact(yM, predM)}
hM, cM = clus["homogeneity_score"], clus["completeness_score"]; clus["v_measure_score"] = 2 * hM * cM / (hM + cM)
def emi_exact(a, b):
    """Expected mutual information under the permutation model (Vinh, Epps & Bailey 2010), mpmath."""
    N = len(a); ra = collections.Counter(a); rb = collections.Counter(b); lf = lambda k: mpmath.loggamma(k + 1); tot = mpmath.mpf(0)
    for ai in ra.values():
        for bj in rb.values():
            for nij in range(max(1, ai + bj - N), min(ai, bj) + 1):
                term = mpmath.mpf(nij) / N * mpmath.log(mpmath.mpf(N * nij) / (ai * bj))
                lw = lf(ai) + lf(bj) + lf(N - ai) + lf(N - bj) - lf(N) - lf(nij) - lf(ai - nij) - lf(bj - nij) - lf(N - ai - bj + nij)
                tot += term * mpmath.exp(lw)
    return tot
emiM = emi_exact(yM, predM)
clus["adjusted_mutual_info_score"] = (mp(mi_exact(yM, predM)) - emiM) / ((mp(entropy_exact(yM)) + mp(entropy_exact(predM))) / 2 - emiM)
# multilabel estimator for the *_samples scorers
class FixedML(ClassifierMixin, BaseEstimator):
    def __init__(self, Y=None): self.Y = Y
    def fit(self, X, y=None):
        self.classes_ = [np.array([0, 1]) for _ in range(np.asarray(self.Y).shape[1])]; return self
    def predict(self, X): return np.asarray(self.Y)[np.asarray(X)[:, 0].astype(int)]
estML = FixedML(Y=YP).fit(None); XML = np.c_[np.arange(n), np.zeros(n)]
mls = {f"{nm}_samples": prf_avg(samp_counts, F(1), F(0), "samples", wch) for nm, wch in [("precision", "P"), ("recall", "R"), ("f1", "F")]}
mls["jaccard_samples"] = jac_avg(samp_counts, F(0), "samples")
# regression
ybarR = fmean(yR)
regs = {"r2": r2_exact(yR, pRq), "explained_variance": ev_1(yR, pRq), "neg_mean_squared_error": -fmean((a - b) ** 2 for a, b in zip(yR, pRq)),
        "neg_root_mean_squared_error": -mpmath.sqrt(mp(fmean((a - b) ** 2 for a, b in zip(yR, pRq)))), "neg_mean_absolute_error": -fmean(abs(a - b) for a, b in zip(yR, pRq)),
        "neg_mean_absolute_percentage_error": -fmean(abs(a - b) / abs(a) for a, b in zip(yR, pRq)), "neg_median_absolute_error": -median_expanded([abs(a - b) for a, b in zip(yR, pRq)], [1] * nR),
        "neg_max_error": -max(abs(a - b) for a, b in zip(yR, pRq)), "max_error": -max(abs(a - b) for a, b in zip(yR, pRq)),
        "neg_mean_squared_log_error": -fmean((mpmath.log1p(mp(a)) - mpmath.log1p(mp(b))) ** 2 for a, b in zip(yR, pRq)),
        "neg_root_mean_squared_log_error": -mpmath.sqrt(fmean((mpmath.log1p(mp(a)) - mpmath.log1p(mp(b))) ** 2 for a, b in zip(yR, pRq))),
        "neg_mean_poisson_deviance": -tw_mean(yR, pRq, 1), "neg_mean_gamma_deviance": -tw_mean(yR, pRq, 2)}
qR = quantile_expanded(yR, [1] * nR, F(1, 2), True) if V >= (1, 9) else quantile_linear(yR, F(1, 2))
regs["d2_absolute_error_score"] = 1 - pinball(yR, pRq, F(1, 2)) / pinball(yR, [qR] * nR, F(1, 2))
names = metrics.get_scorer_names()
unchecked = []
for name in names:
    sc = get_scorer(name)
    if name in truth: est, X_, y_, want = estB, XB, yB, truth[name][1]
    elif name in multi_names: est, X_, y_, want = estM, XM, yM, multi_names[name]
    elif name in clus: est, X_, y_, want = estM, XM, yM, clus[name]
    elif name in regs: est, X_, y_, want = estR, XR, yRf, regs[name]
    elif name in mls: est, X_, y_, want = estML, XML, YT, mls[name]
    else: unchecked.append(name); continue
    try:
        got = sc(est, X_, np.asarray(y_)); det = f"({got:.6f})"
    except Exception as e:
        got = None; det = f"({type(e).__name__}: {str(e)[:100]})"
    neg = name.startswith("neg_") or name == "max_error"
    report(f"get_scorer('{name}')(est, X, y) = {'-' if neg else ''}exact metric of the fixed outputs{' (greater is better: loss sign-flipped)' if neg else ''}", got is not None and close(got, float(want), 1e-10, 1e-12), det)
print(f"   scorer names without an exact truth here: {unchecked}")
report("every scorer name in get_scorer_names() received an exact check", not unchecked)
doc_names = ["accuracy", "balanced_accuracy", "top_k_accuracy", "average_precision", "neg_brier_score", "f1", "f1_micro", "f1_macro", "f1_weighted", "f1_samples",
             "neg_log_loss", "precision", "recall", "jaccard", "roc_auc", "roc_auc_ovr", "roc_auc_ovo", "roc_auc_ovr_weighted", "roc_auc_ovo_weighted",
             "adjusted_mutual_info_score", "adjusted_rand_score", "completeness_score", "fowlkes_mallows_score", "homogeneity_score", "mutual_info_score",
             "normalized_mutual_info_score", "rand_score", "v_measure_score", "explained_variance", "neg_mean_absolute_error", "neg_mean_squared_error",
             "neg_root_mean_squared_error", "neg_mean_squared_log_error", "neg_median_absolute_error", "r2", "neg_mean_poisson_deviance", "neg_mean_gamma_deviance",
             "neg_mean_absolute_percentage_error"]
report("every scorer name of the user-guide table that exists since 1.0 is in get_scorer_names()", set(doc_names) <= set(names), f"(missing {sorted(set(doc_names) - set(names))})")
# user guide 'String name scorers' (main branch): "the table below shows all possible values"
table = set(doc_names) | {"neg_max_error", "neg_root_mean_squared_log_error", "d2_absolute_error_score", "d2_log_loss_score", "d2_brier_score"} | \
        {f"{m}_{s_}" for m in ("precision", "recall", "jaccard") for s_ in ("micro", "macro", "weighted", "samples")}
if V >= (1, 9):
    report("user guide: the scorer table 'shows all possible values' -> every get_scorer_names() entry appears in it", set(names) <= table, f"(not in the table: {sorted(set(names) - table)})")
else:
    print(f"   (main-branch scorer table not compared on {sklearn.__version__}); names outside it: {sorted(set(names) - table)}")
# OvO weighted: user-guide formula vs prevalence-weighted average
pairs = ovo_pairs(yM, PM)
lit = F(1, 3 * 2) * sum(w_ * 2 * s for s, w_ in pairs)          # 1/(c(c-1)) sum p(j u k) (AUC(j|k) + AUC(k|j))
got = metrics.roc_auc_score(yM, np.array([[float(v) for v in r] for r in PM]), multi_class="ovo", average="weighted")
report(f"roc_auc_score(multi_class='ovo', average='weighted') = the user guide's formula 1/(c(c-1)) sum_(j<k) p(j u k)(AUC(j|k)+AUC(k|j)) ({float(lit):.6f})", close(got, lit), f"(got {got:.6f}; the prevalence-weighted AVERAGE sum p s / sum p = {float(wmean([s for s, _ in pairs], [w_ for _, w_ in pairs])):.6f}; the literal formula gives 2/c = {2/3:.4f} for a perfect classifier)")
# sample_weight passthrough
wS = [rng.randint(1, 4) for _ in range(max(nB, nM, nR))]
report("scorer(est, X, y, sample_weight=w): accuracy uses the weights", close(get_scorer("accuracy")(estB, XB, yB, sample_weight=wS[:nB]), wmean([F(int(a == b)) for a, b in zip(yB, predB)], wS[:nB])))
report("... neg_log_loss uses the weights", close(get_scorer("neg_log_loss")(estB, XB, yB, sample_weight=wS[:nB]), float(-wmean([-mpmath.log(mp(p if y else 1 - p)) for y, p in zip(yB, pB)], wS[:nB]))))
report("... roc_auc uses the weights (weighted Mann-Whitney on the decision function)", close(get_scorer("roc_auc")(estB, XB, yB, sample_weight=wS[:nB]), auc_exact([y for y, k in zip(yB, wS) for _ in range(k)], [d for d, k in zip(dB, wS) for _ in range(k)])))
report("... neg_mean_squared_error uses the weights", close(get_scorer("neg_mean_squared_error")(estR, XR, yRf, sample_weight=wS[:nR]), -wmean([(a - b) ** 2 for a, b in zip(yR, pRq)], wS[:nR])))
report("... f1_macro uses the weights", close(get_scorer("f1_macro")(estM, XM, yM, sample_weight=wS[:nM]), prf_avg([counts([int(t == l) for t in yM], [int(q == l) for q in predM], wS[:nM]) for l in range(3)], F(1), F(0), "macro", "F")))
# make_scorer
fb = make_scorer(metrics.fbeta_score, beta=2, average="macro")
report("make_scorer(fbeta_score, beta=2, average='macro'): **kwargs are passed to score_func", close(fb(estM, XM, yM), prf_avg(csM, F(2), F(0), "macro", "F")))
report("make_scorer(f1_score, pos_label=0): f1 of class 0", close(make_scorer(metrics.f1_score, pos_label=0)(estB, XB, yB), prf_from(csB[0], F(1), F(0))[2]))
report("make_scorer(mean_squared_error, greater_is_better=False) 'will sign-flip the outcome'", close(make_scorer(metrics.mean_squared_error, greater_is_better=False)(estR, XR, yRf), regs["neg_mean_squared_error"]))
if V >= (1, 4):
    sc_p = make_scorer(metrics.brier_score_loss, response_method="predict_proba", greater_is_better=False)
    sc_t = make_scorer(metrics.roc_auc_score, response_method=("decision_function", "predict_proba"))
    sc_t2 = make_scorer(metrics.roc_auc_score, response_method=("predict_proba", "decision_function"))
    sc_ll = make_scorer(metrics.log_loss, response_method="predict_proba", greater_is_better=False)
    lab = "response_method"
else:
    sc_p = make_scorer(metrics.brier_score_loss, needs_proba=True, greater_is_better=False)
    sc_t = make_scorer(metrics.roc_auc_score, needs_threshold=True); sc_t2 = None
    sc_ll = make_scorer(metrics.log_loss, needs_proba=True, greater_is_better=False)
    lab = "needs_*"
report(f"make_scorer(brier_score_loss, {lab}=predict_proba, greater_is_better=False) on a binary estimator feeds the positive-class column", close(sc_p(estB, XB, yB), truth["neg_brier_score"][1]))
report(f"make_scorer(roc_auc_score, {lab}=('decision_function', 'predict_proba')): the first available method (decision_function) is used", close(sc_t(estB, XB, yB), auc_exact(yB, dB)), f"(proba ranking would give {float(auc_exact(yB, pB)):.6f})")
if sc_t2 is not None:
    report("make_scorer(roc_auc_score, response_method=('predict_proba', 'decision_function')): order of preference -> predict_proba", close(sc_t2(estB, XB, yB), auc_exact(yB, pB)))
report("make_scorer(log_loss, predict_proba) on a multiclass estimator passes the full probability matrix", close(sc_ll(estM, XM, yM), float(-ll_sum(yM, PM) / nM)))
# check_scoring
report("check_scoring(classifier) with scoring=None uses estimator.score (accuracy for ClassifierMixin)", close(check_scoring(estB)(estB, XB, yB), truth["accuracy"][1]))
report("check_scoring(regressor) with scoring=None uses estimator.score (R^2 for RegressorMixin)", close(check_scoring(estR)(estR, XR, yRf), regs["r2"]))
report("check_scoring(est, scoring='f1_macro') equals get_scorer('f1_macro')", close(check_scoring(estM, scoring="f1_macro")(estM, XM, yM), prf_avg(csM, F(1), F(0), "macro", "F")))
class NoScore(BaseEstimator):
    def fit(self, X, y=None): return self
    def predict(self, X): return np.zeros(len(X))
report("check_scoring on an estimator without score and scoring=None raises TypeError", raises(TypeError, check_scoring, NoScore()))
report("check_scoring(..., allow_none=True) returns None for such an estimator", check_scoring(NoScore(), allow_none=True) is None)
my = lambda est, X, y: 42.0
report("get_scorer(callable) returns it as is; get_scorer(None) returns None (docstring)", get_scorer(my) is my and get_scorer(None) is None)
report("get_scorer('not_a_scorer') raises ValueError (InvalidParameterError / ValueError)", raises(ValueError, get_scorer, "not_a_scorer"))
report("get_scorer(name) returns a new object on each call (docstring note)", get_scorer("accuracy") is not get_scorer("accuracy"))
doc_multi = bool(re.search(r"scoring : [^\n]*\blist\b", check_scoring.__doc__ or ""))
if doc_multi:
    ms = check_scoring(estM, scoring=["accuracy", "f1_macro"])
    got = ms(estM, XM, yM)
    report("check_scoring(est, scoring=['accuracy', 'f1_macro']) (multi-metric) returns a dict of the two exact scores", isinstance(got, dict) and close(got["accuracy"], F(sum(a == b for a, b in zip(yM, predM)), nM)) and close(got["f1_macro"], prf_avg(csM, F(1), F(0), "macro", "F")))
    got = check_scoring(estM, scoring={"acc": "accuracy", "nll": "neg_log_loss"})(estM, XM, yM)
    report("check_scoring with a dict of names", isinstance(got, dict) and close(got["nll"], float(ll_sum(yM, PM) / -nM)))
else:
    print(f"   check_scoring on {sklearn.__version__} does not document list/dict scoring")
cv = cross_validate(estM, XM, np.array(yM), cv=KFold(3), scoring=["accuracy", "neg_log_loss"])
folds = [list(range(12 * k, 12 * k + 12)) for k in range(3)]
report("cross_validate(scoring=['accuracy', 'neg_log_loss']): per-fold test scores = exact metrics on each KFold(3) test block",
       all(close(cv["test_accuracy"][k], F(sum(yM[i] == predM[i] for i in folds[k]), 12)) and close(cv["test_neg_log_loss"][k], float(-sum(-mpmath.log(mp(PM[i][yM[i]])) for i in folds[k]) / 12)) for k in range(3)))
cv = cross_validate(estR, XR, np.array(yRf), cv=KFold(4), scoring={"mae": "neg_mean_absolute_error", "m": make_scorer(metrics.max_error, greater_is_better=False)})
fr_ = [list(range(6 * k, 6 * k + 6)) for k in range(4)]
report("cross_validate(scoring=dict with a make_scorer entry): keys test_<name>, signs flipped for losses",
       all(close(cv["test_mae"][k], -fmean(abs(yR[i] - pRq[i]) for i in fr_[k])) and close(cv["test_m"][k], -max(abs(yR[i] - pRq[i]) for i in fr_[k])) for k in range(4)))
