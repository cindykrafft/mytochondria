#!/usr/bin/env python
"""Classification and ranking metrics against exact recomputations: ROC AUC with
ties, roc_curve points, average precision, precision/recall/F1 with the four
averages and zero_division, MCC, Cohen's kappa (unweighted / linear / quadratic),
balanced accuracy (adjusted), log loss, accuracy, and the multiclass AUC
averages."""
import sys, random, math, warnings
sys.path.insert(0, ".")
from _synth import *
from sklearn import metrics
banner(); rng = random.Random(1)
warnings.filterwarnings("ignore")

# ---- binary ranking with many ties
n = 400
y = [rng.random() < 0.3 for _ in range(n)]; y = [1 if t else 0 for t in y]
s = [round(rng.random() * (0.6 if t == 0 else 1.0), 1) for t in y]        # scores on a 0.1 grid: many ties
auc = metrics.roc_auc_score(y, s); ex = auc_exact(y, s)
report(f"roc_auc_score with ties = Mann-Whitney with ties at 1/2 ({float(ex):.6f})", close(auc, ex))
fpr, tpr, thr = metrics.roc_curve(y, s, drop_intermediate=False); pts = roc_points_exact(y, s)
got = sorted(set((float(a), float(b)) for a, b in zip(fpr, tpr))); want = sorted(set((float(a), float(b)) for a, b in pts))
report(f"roc_curve(drop_intermediate=False): the {len(want)} (fpr, tpr) points at every distinct threshold", got == want)
report("auc(fpr, tpr) of the full curve equals roc_auc_score", close(metrics.auc(fpr, tpr), auc))
fpr2, tpr2, thr2 = metrics.roc_curve(y, s)
report(f"roc_curve default drop_intermediate keeps a subset of the points ({len(fpr2)} of {len(fpr)}) with the same trapezoid area", set(zip(fpr2, tpr2)) <= set(zip(fpr, tpr)) and close(metrics.auc(fpr2, tpr2), auc))
ap = metrics.average_precision_score(y, s); exap = ap_exact(y, s)
report(f"average_precision_score = sum (R_k - R_k-1) P_k over distinct thresholds ({float(exap):.6f})", close(ap, exap))
prec, rec, _ = metrics.precision_recall_curve(y, s)
report("precision_recall_curve ends at (recall 0, precision 1)", rec[-1] == 0 and prec[-1] == 1)
# degenerate score vectors
report("roc_auc_score with all scores equal = 0.5", close(metrics.roc_auc_score(y, [0.5] * n), 0.5))
report("average_precision_score with all scores equal = prevalence", close(metrics.average_precision_score(y, [0.5] * n), sum(y) / n))
try:
    metrics.roc_auc_score([0] * 10, [0.1] * 10); report("roc_auc_score with one class raises", False)
except ValueError: report("roc_auc_score with one class raises ValueError", True)

# ---- multiclass PRF, MCC, kappa, balanced accuracy
labels = [0, 1, 2, 3]
yt = [rng.choices(labels, weights=[5, 3, 1, 1])[0] for _ in range(300)]
yp = [t if rng.random() < 0.6 else rng.choice(labels) for t in yt]
yp = [3 if v == 3 and rng.random() < 0.0 else v for v in yp]
for avg in ("macro", "weighted", "micro"):
    got = metrics.precision_recall_fscore_support(yt, yp, average=avg, zero_division=0)[:3]; want = prf_exact(yt, yp, labels, avg)
    report(f"precision/recall/F1 average='{avg}' exact", all(close(g, w) for g, w in zip(got, want)))
# a class never predicted and a class never present
pairs = [(t, p_) for t, p_ in zip(yt, yp) if t != 3]; yt2 = [t for t, _ in pairs]; yp2 = [0 if p_ in (2, 3) else p_ for _, p_ in pairs]   # 3 absent from both, 2 never predicted
got = metrics.precision_recall_fscore_support(yt2, yp2, labels=labels, average="macro", zero_division=0)[:3]; want = prf_exact(yt2, yp2, labels, "macro")
report("macro PRF with labels=[0..3] where 2 is never predicted and 3 never occurs, zero_division=0: undefined terms count as 0 in the mean", all(close(g, w) for g, w in zip(got, want)))
got = metrics.precision_recall_fscore_support(yt2, yp2, labels=labels, average="macro", zero_division=1)[:3]
per = prf_exact(yt2, yp2, labels, None); pc = metrics.precision_recall_fscore_support(yt2, yp2, labels=labels, average=None, zero_division=1)
print(f"   zero_division=1 per class: precision {pc[0].tolist()}, recall {pc[1].tolist()}, F1 {pc[2].tolist()}, support {pc[3].tolist()}")
report("macro precision with zero_division=1: the two undefined precisions (classes 2 and 3) count as 1", close(got[0], (per[0][0] + per[1][0] + 1 + 1) / 4), f"(got {got[0]:.6f})")
report("macro recall with zero_division=1: class 3 (no true samples) counts as 1, class 2 (present, never predicted) as 0", close(got[1], (per[0][1] + per[1][1] + 0 + 1) / 4), f"(got {got[1]:.6f})")
report("macro F1 with zero_division=1: class 3 counts as 1, class 2 (precision 1 by fiat, recall 0) as 0", close(got[2], (per[0][2] + per[1][2] + 0 + 1) / 4), f"(got {got[2]:.6f})")
report("matthews_corrcoef multiclass exact", close(metrics.matthews_corrcoef(yt, yp), mcc_exact(yt, yp, labels)))
for w in (None, "linear", "quadratic"):
    report(f"cohen_kappa_score(weights={w}) exact", close(metrics.cohen_kappa_score(yt, yp, weights=w), kappa_exact(yt, yp, labels, w)))
report("balanced_accuracy_score = mean recall over classes present in y_true", close(metrics.balanced_accuracy_score(yt, yp), balanced_accuracy_exact(yt, yp, labels)))
report("balanced_accuracy_score(adjusted=True) = (BA - 1/K)/(1 - 1/K) with K classes present in y_true", close(metrics.balanced_accuracy_score(yt2, yp2, adjusted=True), balanced_accuracy_exact(yt2, yp2, [0, 1, 2], adjusted=True)))
report("accuracy_score exact", close(metrics.accuracy_score(yt, yp), sum(a == b for a, b in zip(yt, yp)) / len(yt)))
cm = metrics.confusion_matrix(yt, yp, labels=labels); c = confusion(yt, yp, labels)
report("confusion_matrix rows = true labels, columns = predicted, in `labels` order", all(cm[i, j] == c[(a, b)] for i, a in enumerate(labels) for j, b in enumerate(labels)))
report("confusion_matrix(normalize='true') rows sum to 1", np.allclose(metrics.confusion_matrix(yt, yp, normalize="true").sum(1), 1))

# ---- log loss: clipping and label order
probs = [[rng.random() for _ in labels] for _ in yt]; probs = [[v / sum(p) for v in p] for p in probs]
report("log_loss exact for probabilities in (0,1) that sum to 1", close(metrics.log_loss(yt, probs, labels=labels), log_loss_exact(yt, probs, labels)))
p0 = [[1.0 if j == t else 0.0 for j in labels] for t in yt]; p0[0] = [0.0, 1.0, 0.0, 0.0] if yt[0] != 1 else [1.0, 0.0, 0.0, 0.0]
ll = metrics.log_loss(yt, p0, labels=labels)
print(f"   log_loss with one sample at probability exactly 0 for the true class: {ll:.4f} (eps clipping: {'none, inf' if math.isinf(ll) else 'clipped to a finite value = -log(eps)/n'})")
report("log_loss of a certain wrong prediction is finite only through clipping; value equals -log(eps)/n for some eps", math.isinf(ll) or (ll > 0 and ll < 60 / len(yt)), f"({ll:.4f}; -log(1e-15)/n = {-math.log(1e-15)/len(yt):.4f}, -log(2.2e-16)/n = {-math.log(2.220446049250313e-16)/len(yt):.4f})")

# ---- multiclass AUC: ovr macro / weighted, ovo
Y = np.array(yt); Pm = np.array(probs)
def ovr(avg):
    vals = []; ws = []
    for k in labels:
        yb = [1 if t == k else 0 for t in yt]; vals.append(float(auc_exact(yb, [p[k] for p in probs]))); ws.append(sum(yb))
    return sum(vals) / len(vals) if avg == "macro" else sum(v * w for v, w in zip(vals, ws)) / sum(ws)
report("roc_auc_score(multi_class='ovr', average='macro') = mean of one-vs-rest AUCs", close(metrics.roc_auc_score(Y, Pm, multi_class="ovr", average="macro"), ovr("macro"), 1e-9))
report("roc_auc_score(multi_class='ovr', average='weighted') = prevalence-weighted mean", close(metrics.roc_auc_score(Y, Pm, multi_class="ovr", average="weighted"), ovr("weighted"), 1e-9))
def ovo_macro():
    tot = 0; cnt = 0
    for a, b in itertools.combinations(labels, 2):
        idx = [i for i, t in enumerate(yt) if t in (a, b)]
        ya = [1 if yt[i] == a else 0 for i in idx]
        auc_ab = float(auc_exact(ya, [probs[i][a] for i in idx])); auc_ba = float(auc_exact([1 - v for v in ya], [probs[i][b] for i in idx]))
        tot += (auc_ab + auc_ba) / 2; cnt += 1
    return tot / cnt
report("roc_auc_score(multi_class='ovo', average='macro') = mean over pairs of the two-direction average (Hand & Till)", close(metrics.roc_auc_score(Y, Pm, multi_class="ovo", average="macro"), ovo_macro(), 1e-9))

# ---- binary AUC from probabilities of the positive class only vs 2-column input
yb = [1 if t == 1 else 0 for t in yt]
report("roc_auc_score binary from the positive-class column equals the exact AUC", close(metrics.roc_auc_score(yb, Pm[:, 1]), auc_exact(yb, [p[1] for p in probs])))

# ---- f1 zero_division default warning behaviour, with no positive predictions
report("f1_score with no positive prediction and zero_division=0 is 0", metrics.f1_score([1, 1, 0], [0, 0, 0], zero_division=0) == 0)
report("f1_score with no positive prediction and zero_division=1 is 1 when y_true has positives? (precision undefined -> 1, recall 0 -> F1 0)", close(metrics.f1_score([1, 1, 0], [0, 0, 0], zero_division=1), 0.0), f"({metrics.f1_score([1, 1, 0], [0, 0, 0], zero_division=1)})")
report("f1_score with y_true and y_pred all negative, zero_division=1 -> 1.0", close(metrics.f1_score([0, 0, 0], [0, 0, 0], zero_division=1), 1.0), f"({metrics.f1_score([0, 0, 0], [0, 0, 0], zero_division=1)})")
