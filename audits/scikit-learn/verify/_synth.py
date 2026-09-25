"""Shared helpers for the scikit-learn harnesses: exact recomputations (Fraction /
mpmath) of the classification, ranking, regression and clustering metrics, and a
report() line format. Every harness runs under whichever interpreter is given:
    <venv>/bin/python k1_....py
and prints the installed versions first."""
import sys, math, itertools, collections
from fractions import Fraction as F
import numpy as np
import sklearn

def banner():
    print(f"scikit-learn {sklearn.__version__}  numpy {np.__version__}  python {sys.version.split()[0]}")

def report(label, ok, detail=""):
    print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))

def close(a, b, rel=1e-9, abs_=1e-12):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))

# ---- ranking metrics, exact
def auc_exact(y, s):
    """Mann-Whitney AUC with ties counted 1/2 (the ROC-AUC definition)."""
    pos = [F(x) for x, t in zip(s, y) if t == 1]; neg = [F(x) for x, t in zip(s, y) if t == 0]
    if not pos or not neg: return None
    tot = F(0)
    for p in pos:
        for n in neg:
            tot += 1 if p > n else (F(1, 2) if p == n else 0)
    return tot / (len(pos) * len(neg))

def roc_points_exact(y, s):
    """(fpr, tpr) at every distinct threshold, descending, plus (0,0)."""
    P = sum(1 for t in y if t == 1); N = len(y) - P
    pts = [(F(0), F(0))]
    for thr in sorted(set(s), reverse=True):
        tp = sum(1 for x, t in zip(s, y) if x >= thr and t == 1); fp = sum(1 for x, t in zip(s, y) if x >= thr and t == 0)
        pts.append((F(fp, N), F(tp, P)))
    return pts

def ap_exact(y, s):
    """Average precision = sum_k (R_k - R_{k-1}) P_k over distinct thresholds, descending."""
    P = sum(1 for t in y if t == 1); prev_r = F(0); ap = F(0)
    for thr in sorted(set(s), reverse=True):
        sel = [t for x, t in zip(s, y) if x >= thr]
        tp = sum(sel); prec = F(tp, len(sel)); rec = F(tp, P)
        ap += (rec - prev_r) * prec; prev_r = rec
    return ap

# ---- classification metrics, exact
def confusion(y, p, labels):
    c = {(a, b): 0 for a in labels for b in labels}
    for a, b in zip(y, p): c[(a, b)] += 1
    return c

def prf_exact(y, p, labels, average):
    c = confusion(y, p, labels); out = {}
    for l in labels:
        tp = c[(l, l)]; fp = sum(c[(a, l)] for a in labels if a != l); fn = sum(c[(l, b)] for b in labels if b != l)
        pr = F(tp, tp + fp) if tp + fp else F(0); rc = F(tp, tp + fn) if tp + fn else F(0)
        f1 = 2 * pr * rc / (pr + rc) if pr + rc else F(0)
        out[l] = (pr, rc, f1, tp + fn)
    if average == "macro":
        return tuple(sum(out[l][i] for l in labels) / len(labels) for i in range(3))
    if average == "weighted":
        n = sum(out[l][3] for l in labels)
        return tuple(sum(out[l][i] * out[l][3] for l in labels) / n for i in range(3))
    if average == "micro":
        tp = sum(c[(l, l)] for l in labels); n = len(y); v = F(tp, n); return (v, v, v)
    return out

def mcc_exact(y, p, labels):
    c = confusion(y, p, labels); n = len(y)
    t = {k: sum(c[(k, b)] for b in labels) for k in labels}; q = {k: sum(c[(a, k)] for a in labels) for k in labels}
    cov_yp = n * sum(c[(k, k)] for k in labels) - sum(t[k] * q[k] for k in labels)
    cov_yy = n * n - sum(t[k] ** 2 for k in labels); cov_pp = n * n - sum(q[k] ** 2 for k in labels)
    if cov_yy == 0 or cov_pp == 0: return F(0)
    return cov_yp / math.sqrt(cov_yy * cov_pp)

def kappa_exact(y, p, labels, weights=None):
    c = confusion(y, p, labels); n = len(y)
    t = {k: sum(c[(k, b)] for b in labels) for k in labels}; q = {k: sum(c[(a, k)] for a in labels) for k in labels}
    idx = {l: i for i, l in enumerate(labels)}
    def w(a, b):
        if weights is None: return 0 if a == b else 1
        d = abs(idx[a] - idx[b]); return d if weights == "linear" else d * d
    obs = sum(w(a, b) * c[(a, b)] for a in labels for b in labels)
    exp = sum(w(a, b) * F(t[a] * q[b], n) for a in labels for b in labels)
    return 1 - F(obs) / exp if exp else F(0)

def balanced_accuracy_exact(y, p, labels, adjusted=False):
    c = confusion(y, p, labels)
    recalls = [F(c[(l, l)], sum(c[(l, b)] for b in labels)) for l in labels if sum(c[(l, b)] for b in labels)]
    ba = sum(recalls) / len(recalls)
    if adjusted:
        chance = F(1, len(recalls)); ba = (ba - chance) / (1 - chance)
    return ba

def log_loss_exact(y, probs, labels):
    idx = {l: i for i, l in enumerate(labels)}
    return -sum(math.log(probs[i][idx[t]]) for i, t in enumerate(y)) / len(y)

# ---- regression
def r2_exact(y, p):
    ybar = sum(F(v) for v in y) / len(y)
    ss_res = sum((F(a) - F(b)) ** 2 for a, b in zip(y, p)); ss_tot = sum((F(a) - ybar) ** 2 for a in y)
    if ss_tot == 0: return None
    return 1 - ss_res / ss_tot

# ---- clustering, exact
def contingency(a, b):
    c = collections.Counter(zip(a, b)); return c

def ari_exact(a, b):
    c = contingency(a, b); n = len(a)
    comb = lambda x: F(x * (x - 1), 2)
    sum_ij = sum(comb(v) for v in c.values())
    ra = collections.Counter(a); rb = collections.Counter(b)
    sa = sum(comb(v) for v in ra.values()); sb = sum(comb(v) for v in rb.values())
    expected = sa * sb / comb(n); mx = (sa + sb) / 2
    if mx == expected: return F(1)
    return (sum_ij - expected) / (mx - expected)

def entropy_exact(labels):
    n = len(labels); c = collections.Counter(labels)
    return -sum(F(v, n) * math.log(F(v, n)) for v in c.values())

def mi_exact(a, b):
    n = len(a); c = contingency(a, b); ra = collections.Counter(a); rb = collections.Counter(b)
    return sum(F(v, n) * math.log(F(v * n, ra[i] * rb[j])) for (i, j), v in c.items())

def nmi_exact(a, b, method="arithmetic"):
    mi = mi_exact(a, b); ha = entropy_exact(a); hb = entropy_exact(b)
    if method == "arithmetic": d = (ha + hb) / 2
    elif method == "geometric": d = math.sqrt(ha * hb)
    elif method == "min": d = min(ha, hb)
    else: d = max(ha, hb)
    return mi / d if d else (1.0 if mi == 0 else float("nan"))

def silhouette_exact(X, labels):
    X = np.asarray(X, dtype=float); labels = np.asarray(labels); n = len(labels); out = []
    D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    for i in range(n):
        own = labels == i * 0 + labels[i]; own[i] = False
        if own.sum() == 0: out.append(0.0); continue
        a = D[i, own].mean()
        b = min(D[i, labels == l].mean() for l in set(labels) if l != labels[i])
        out.append((b - a) / max(a, b))
    return np.array(out)
