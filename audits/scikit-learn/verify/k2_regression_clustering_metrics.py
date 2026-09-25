#!/usr/bin/env python
"""Regression and clustering metrics against exact recomputations: r2_score
(constant targets, force_finite, multioutput), MAE / MSE / RMSE / MAPE / explained
variance, and adjusted_rand, mutual_info, NMI (four averages), AMI (exact expected
MI), homogeneity / completeness / V-measure, silhouette (incl. singleton clusters),
Calinski-Harabasz, Davies-Bouldin, Fowlkes-Mallows."""
import sys, random, math, warnings, itertools, collections
sys.path.insert(0, ".")
from _synth import *
from sklearn import metrics
import mpmath
banner(); rng = random.Random(2); warnings.filterwarnings("ignore")

# ---- regression
y = [F(rng.randint(-100, 100), 4) for _ in range(120)]; p = [v + F(rng.randint(-30, 30), 7) for v in y]
yf = [float(v) for v in y]; pf = [float(v) for v in p]; yE = [F(v) for v in yf]; pE = [F(v) for v in pf]
report("r2_score exact", close(metrics.r2_score(yf, pf), r2_exact(yE, pE)))
report("mean_absolute_error exact", close(metrics.mean_absolute_error(yf, pf), sum(abs(a - b) for a, b in zip(yE, pE)) / len(yE)))
mse = sum((a - b) ** 2 for a, b in zip(yE, pE)) / len(yE)
report("mean_squared_error exact", close(metrics.mean_squared_error(yf, pf), mse))
rmse = getattr(metrics, "root_mean_squared_error", None)
if rmse: report("root_mean_squared_error = sqrt(MSE)", close(rmse(yf, pf), math.sqrt(mse)))
else: report("mean_squared_error(squared=False) = sqrt(MSE)", close(metrics.mean_squared_error(yf, pf, squared=False), math.sqrt(mse)))
ynz = [v if v != 0 else F(1, 4) for v in yE]; ynzf = [float(v) for v in ynz]
report("mean_absolute_percentage_error = mean |y - p| / |y| (a fraction, not a percentage)", close(metrics.mean_absolute_percentage_error(ynzf, pf), sum(abs(a - b) / abs(a) for a, b in zip(ynz, pE)) / len(ynz)))
mape0 = metrics.mean_absolute_percentage_error([0.0, 1.0], [1.0, 1.0])
print(f"   MAPE with a zero target: {mape0:.4g} (|0-1|/max(eps,0) averaged with 0: eps = {2 / mape0:.3g})")
ev = 1 - float(np.var(np.array(yf) - np.array(pf))) / float(np.var(np.array(yf)))
report("explained_variance_score = 1 - var(y - p)/var(y)", close(metrics.explained_variance_score(yf, pf), ev, 1e-9))
# constant y_true
yc = [2.0] * 10; pc_ = [2.0] * 10; pc2 = [2.0 + 0.1 * i for i in range(10)]
r_perf = metrics.r2_score(yc, pc_); r_imp = metrics.r2_score(yc, pc2)
print(f"   r2_score with constant y_true: perfect prediction -> {r_perf}, imperfect -> {r_imp}; force_finite=False -> {metrics.r2_score(yc, pc_, force_finite=False) if 'force_finite' in metrics.r2_score.__code__.co_varnames else 'n/a'}, {metrics.r2_score(yc, pc2, force_finite=False) if 'force_finite' in metrics.r2_score.__code__.co_varnames else 'n/a'}")
report("r2_score with constant y_true: 1.0 for a perfect prediction and 0.0 otherwise (force_finite default)", r_perf == 1.0 and r_imp == 0.0)
Y = np.array([yf, [2 * v for v in yf]]).T; P = np.array([pf, [2 * v + 1 for v in pf]]).T
r2u = metrics.r2_score(Y, P, multioutput="uniform_average"); r2v = metrics.r2_score(Y, P, multioutput="variance_weighted")
r2_each = [float(r2_exact([F(v) for v in Y[:, j].tolist()], [F(v) for v in P[:, j].tolist()])) for j in range(2)]
w = [float(np.var(Y[:, j])) for j in range(2)]
report("r2_score multioutput='uniform_average' (default) = mean of per-output R2", close(r2u, sum(r2_each) / 2, 1e-9))
report("r2_score multioutput='variance_weighted' weights by var(y_j)", close(r2v, sum(a * b for a, b in zip(r2_each, w)) / sum(w), 1e-9))

# ---- clustering, labels
a = [rng.choice("ABCD") for _ in range(200)]; b = [v if rng.random() < 0.7 else rng.choice("ABCDE") for v in a]
ai = [ord(v) for v in a]; bi = [ord(v) for v in b]
report("adjusted_rand_score exact", close(metrics.adjusted_rand_score(ai, bi), ari_exact(ai, bi)))
report("adjusted_rand_score symmetric and 1 for identical partitions", close(metrics.adjusted_rand_score(ai, bi), metrics.adjusted_rand_score(bi, ai)) and metrics.adjusted_rand_score(ai, ai) == 1.0)
report("rand_score exact", close(metrics.rand_score(ai, bi), (lambda: (sum(1 for i, j in itertools.combinations(range(len(ai)), 2) if (ai[i] == ai[j]) == (bi[i] == bi[j])) / F(len(ai) * (len(ai) - 1) // 2)))()))
report("mutual_info_score exact (natural log)", close(metrics.mutual_info_score(ai, bi), mi_exact(ai, bi)))
for meth in ("arithmetic", "geometric", "min", "max"):
    report(f"normalized_mutual_info_score(average_method='{meth}') exact", close(metrics.normalized_mutual_info_score(ai, bi, average_method=meth), nmi_exact(ai, bi, meth)))
report("normalized_mutual_info_score default average is arithmetic", close(metrics.normalized_mutual_info_score(ai, bi), nmi_exact(ai, bi, "arithmetic")))
h_ = float(mi_exact(ai, bi) / entropy_exact(ai)); c_ = float(mi_exact(ai, bi) / entropy_exact(bi))
report("homogeneity = MI/H(true), completeness = MI/H(pred), v_measure = harmonic mean", close(metrics.homogeneity_score(ai, bi), h_) and close(metrics.completeness_score(ai, bi), c_) and close(metrics.v_measure_score(ai, bi), 2 * h_ * c_ / (h_ + c_)))
# AMI: exact expected MI (Vinh et al. 2010) with mpmath
def emi_exact(a, b):
    n = len(a); ra = collections.Counter(a); rb = collections.Counter(b); tot = mpmath.mpf(0)
    for ai_ in ra.values():
        for bj in rb.values():
            for nij in range(max(1, ai_ + bj - n), min(ai_, bj) + 1):
                p_ = mpmath.binomial(bj, nij) * mpmath.binomial(n - bj, ai_ - nij) / mpmath.binomial(n, ai_)
                tot += mpmath.mpf(nij) / n * mpmath.log(mpmath.mpf(nij * n) / (ai_ * bj)) * p_
    return tot
emi = emi_exact(ai, bi); mi = mpmath.mpf(float(mi_exact(ai, bi))); ha = mpmath.mpf(float(entropy_exact(ai))); hb = mpmath.mpf(float(entropy_exact(bi)))
ami_e = (mi - emi) / ((ha + hb) / 2 - emi)
report("adjusted_mutual_info_score = (MI - E[MI]) / (mean(H) - E[MI]) with the exact hypergeometric E[MI]", close(metrics.adjusted_mutual_info_score(ai, bi), float(ami_e), 1e-9), f"({metrics.adjusted_mutual_info_score(ai, bi):.9f} vs {float(ami_e):.9f})")
fm = math.sqrt(float(F(sum(v * (v - 1) // 2 for v in collections.Counter(zip(ai, bi)).values())) ** 2 / (sum(v * (v - 1) // 2 for v in collections.Counter(ai).values()) * sum(v * (v - 1) // 2 for v in collections.Counter(bi).values()))))
report("fowlkes_mallows_score = TP / sqrt((TP+FP)(TP+FN)) over pairs", close(metrics.fowlkes_mallows_score(ai, bi), fm, 1e-9))

# ---- clustering, geometry
X = np.array([[rng.gauss(cx, 0.8), rng.gauss(cy, 0.8)] for cx, cy in [(0, 0), (5, 0), (0, 5)] for _ in range(30)]); lab = np.repeat([0, 1, 2], 30)
report("silhouette_score = mean of exact silhouette samples (euclidean)", close(metrics.silhouette_score(X, lab), silhouette_exact(X, lab).mean(), 1e-9))
report("silhouette_samples exact", np.allclose(metrics.silhouette_samples(X, lab), silhouette_exact(X, lab), rtol=1e-9, atol=1e-12))
lab1 = lab.copy(); lab1[0] = 3   # a singleton cluster
ss = metrics.silhouette_samples(X, lab1)
report("silhouette of a singleton cluster is 0 (defined that way), others computed against it as a candidate neighbour", ss[0] == 0 and np.allclose(ss, silhouette_exact(X, lab1), rtol=1e-9, atol=1e-12))
D = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
report("silhouette_score(metric='precomputed') equals the euclidean result", close(metrics.silhouette_score(D, lab, metric="precomputed"), metrics.silhouette_score(X, lab), 1e-12))
# Calinski-Harabasz, Davies-Bouldin
n, k = len(lab), 3; mu = X.mean(0); cents = [X[lab == j].mean(0) for j in range(k)]
B = sum((lab == j).sum() * ((cents[j] - mu) ** 2).sum() for j in range(k)); W = sum(((X[lab == j] - cents[j]) ** 2).sum() for j in range(k))
report("calinski_harabasz_score = (B/(k-1)) / (W/(n-k))", close(metrics.calinski_harabasz_score(X, lab), (B / (k - 1)) / (W / (n - k)), 1e-9))
s_ = [np.sqrt(((X[lab == j] - cents[j]) ** 2).sum(1)).mean() for j in range(k)]
db = np.mean([max((s_[i] + s_[j]) / np.linalg.norm(cents[i] - cents[j]) for j in range(k) if j != i) for i in range(k)])
report("davies_bouldin_score = mean_i max_j (s_i + s_j)/d(c_i, c_j) with s = mean euclidean distance to the centroid", close(metrics.davies_bouldin_score(X, lab), db, 1e-9))
