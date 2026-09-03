#!/usr/bin/env python3
"""Held-up check: the three Wilcoxon implementations FindMarkers can dispatch to agree.

WilcoxDETest (R/differential_expression.R:2494-2569, main @ 084d9e4) uses, in order of
preference: presto::wilcoxauc (v5 default when presto is installed), limma::
rankSumTestWithCorrelation (v4 default, v5 "wilcox_limma"), or stats::wilcox.test.

presto's p-value (presto/R/utils.R:41-57, clone 2026-09-02) is ported verbatim below:
normal approximation of U with tie correction and a continuity correction of 0.5,
z clamped to 0 for fully tied features. It is compared with scipy's asymptotic
Mann-Whitney (continuity + tie correction: the same formula R's wilcox.test uses
whenever exact=FALSE, which is forced by ties, i.e. always on single-cell data), and
with the exact distribution for small tie-free samples to show where they diverge.

limma's rankSumTestWithCorrelation could not be fetched in this session
(git.bioconductor.org is denied by the egress policy); its documented formula is the
same normal approximation with continuity correction, correlation = 0 in Seurat's
call. Seurat takes min(2 * min(lower, upper), 1), a two-sided p.
"""
import numpy as np
from scipy import stats

def presto_pval(x, grp):
    """x: (genes, cells); grp: 0/1 per cell. Returns two-sided p per gene, presto's way."""
    n = x.shape[1]
    n1 = int((grp == 1).sum()); n2 = n - n1
    n1n2 = n1 * n2
    p = np.empty(x.shape[0])
    for g in range(x.shape[0]):
        r = stats.rankdata(x[g])                       # average ranks, as presto's rank_matrix
        R1 = r[grp == 1].sum()
        u = R1 - n1 * (n1 + 1) / 2                     # U for group 1
        _, counts = np.unique(x[g], return_counts=True)
        ties = counts[counts > 1]
        z = u - 0.5 * n1n2
        z = z - np.sign(z) * 0.5                       # continuity correction
        x1 = n ** 3 - n
        x2 = 1 / (12 * (n ** 2 - n))
        rhs = (x1 - np.sum(ties ** 3 - ties)) * x2
        usigma = np.sqrt(n1n2 * rhs)
        zz = z / usigma if usigma > 0 else 0.0
        p[g] = 2 * stats.norm.cdf(-abs(zz))
    return p

rng = np.random.default_rng(3)

# 1. single-cell-like data: sparse counts with many ties, unequal groups
n1, n2 = 80, 1200
grp = np.r_[np.ones(n1, int), np.zeros(n2, int)]
lam = np.exp(rng.normal(-2.5, 1.5, 300))
X = np.log1p(rng.poisson(np.outer(lam, np.ones(n1 + n2))))
X[:100, :n1] = np.log1p(rng.poisson(np.outer(lam[:100] * 3, np.ones(n1))))   # 100 DE genes
pp = presto_pval(X, grp)
ps = np.array([stats.mannwhitneyu(X[g, grp == 1], X[g, grp == 0], alternative="two-sided",
                                  method="asymptotic", use_continuity=True).pvalue
               for g in range(X.shape[0])])
ok = np.isfinite(pp) & np.isfinite(ps)
print("sparse counts, 80 vs 1200 cells, 300 genes (100 DE):")
print("  max |p_presto - p_scipy_asymptotic| = %.2e   (all-zero genes: presto p=1, scipy p=%s)"
      % (np.max(np.abs(pp[ok] - ps[ok])), "nan" if (~ok).any() else "n/a"))
print("  calls at p<0.05 identical: %s" % np.array_equal(pp[ok] < 0.05, ps[ok] < 0.05))

# 2. small tie-free samples: normal approximation vs exact
print("\nsmall tie-free groups, exact vs the continuity-corrected normal approximation both paths use:")
for n1, n2 in ((3, 3), (5, 5), (10, 10), (20, 20)):
    worst = 0
    for _ in range(300):
        a = rng.normal(0, 1, n1); b = rng.normal(0.8, 1, n2)
        pe = stats.mannwhitneyu(a, b, alternative="two-sided", method="exact").pvalue
        pa = presto_pval(np.r_[a, b][None, :], np.r_[np.ones(n1, int), np.zeros(n2, int)])[0]
        worst = max(worst, abs(pe - pa))
    print("  n1=n2=%2d  max |p_exact - p_approx| = %.3f" % (n1, worst))
print("  (relevant only to groups near min.cells.group = 3 with no tied zeros; not a defect)")
