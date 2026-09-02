#!/usr/bin/env python3
"""Held-up: rank_genes_groups(method="wilcoxon", tie_correct=True) equals scipy's
asymptotic Mann-Whitney without continuity correction (scanpy applies none), and the
numba rankdata/_tiecorrect ports equal scipy.stats.rankdata/tiecorrect. Also checks that
normalize_total(exclude_highly_expressed=True) gives the same result on CSR and dense
input (the CSR path builds `gene_subset` with a bitwise-not of an index array, which is
only used for logging)."""
import numpy as np, pandas as pd, anndata as ad, scanpy as sc, scipy.sparse as sp
from scipy import stats
from scanpy.tools._rank_genes_groups import rankdata, _tiecorrect
from importlib.metadata import version
sc.settings.verbosity = 0
print("scanpy", version("scanpy"))
rng = np.random.default_rng(5)
n, G = 800, 600
prop = np.exp(rng.normal(-5, 2, G)); prop /= prop.sum()
X = rng.negative_binomial(2, 2 / (2 + np.outer(rng.lognormal(np.log(5000), 0.3, n), prop))).astype(np.float32)
grp = rng.integers(0, 2, n)
a = ad.AnnData(X); a.obs["g"] = pd.Categorical(grp.astype(str))
sc.pp.normalize_total(a, target_sum=1e4); sc.pp.log1p(a)
sc.tl.rank_genes_groups(a, "g", method="wilcoxon", tie_correct=True, groups=["0"], reference="1")
df = sc.get.rank_genes_groups_df(a, "0").set_index("names").loc[a.var_names]
p_sp = np.array([stats.mannwhitneyu(a.X[grp == 0, j], a.X[grp == 1, j], alternative="two-sided",
                                    method="asymptotic", use_continuity=False).pvalue for j in range(G)])
ok = np.isfinite(p_sp)
print("wilcoxon tie_correct=True vs scipy asymptotic (no continuity): max |p diff| = %.2e" % np.nanmax(np.abs(df.pvals.to_numpy()[ok] - p_sp[ok])))
R = rankdata(a.X); Rs = stats.rankdata(a.X, axis=0)
print("numba rankdata vs scipy.stats.rankdata: max |diff| = %.2e" % np.max(np.abs(R - Rs)))
tc = _tiecorrect(R); tcs = np.array([stats.tiecorrect(Rs[:, j]) for j in range(G)])
print("numba _tiecorrect vs scipy.stats.tiecorrect: max |diff| = %.2e" % np.max(np.abs(tc - tcs)))
# normalize_total exclude_highly_expressed: CSR vs dense
b1 = ad.AnnData(sp.csr_matrix(X)); b2 = ad.AnnData(X.copy())
sc.pp.normalize_total(b1, exclude_highly_expressed=True, max_fraction=0.05)
sc.pp.normalize_total(b2, exclude_highly_expressed=True, max_fraction=0.05)
print("normalize_total(exclude_highly_expressed) CSR vs dense: max |diff| = %.2e" % np.max(np.abs(b1.X.toarray() - b2.X)))
