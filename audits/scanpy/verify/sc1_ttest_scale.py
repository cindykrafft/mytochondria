#!/usr/bin/env python3
"""SC1: rank_genes_groups(method="t-test", mean_in_log_space=False) runs the t-test on
exponentiated values.

Executed against scanpy master (see run log for the exact version). `compute_statistics`
(src/scanpy/tools/_rank_genes_groups.py, `_basic_stats(exponentiate_values=not
mean_in_log_space, need_var=True)`) computes the per-group means AND variances on
expm1(X) whenever `mean_in_log_space=False`, and `t_test` builds Welch's statistic from
those. The parameter is documented (and release-noted, 1.13.0a1) as controlling only
how the log fold change is computed.

This script runs the shipped function both ways on log1p-normalized NB counts and
compares each result with scipy's Welch t-test on (a) the log1p values and (b) the
expm1 values, then shows the downstream difference in significant genes.
"""
import numpy as np
import pandas as pd
import anndata as ad
import scanpy as sc
from scipy import stats
from importlib.metadata import version

sc.settings.verbosity = 0
rng = np.random.default_rng(0)
n, G = 2000, 3000
prop = np.exp(rng.normal(-5, 2, G)); prop /= prop.sum()
lib = rng.lognormal(np.log(5000), 0.3, n)
grp = np.r_[np.zeros(300, int), np.ones(n - 300, int)]
mu = np.outer(lib, prop)
mu[grp == 0, :150] *= 3                       # 150 genes truly up 3x in group 0
X = rng.negative_binomial(2, 2 / (2 + mu)).astype(np.float32)
a = ad.AnnData(X)
a.obs["g"] = pd.Categorical(grp.astype(str))
sc.pp.normalize_total(a, target_sum=1e4)
sc.pp.log1p(a)

x0, x1 = a.X[grp == 0], a.X[grp == 1]
ref = {
    "Welch on log1p values": stats.ttest_ind(x0, x1, equal_var=False),
    "Welch on expm1 values": stats.ttest_ind(np.expm1(x0), np.expm1(x1), equal_var=False),
}
print("scanpy", version("scanpy"))
print("group 0 (n=300) vs group 1 (n=1700), method='t-test', groups=['0'], reference='1'\n")
res = {}
for mls in (True, False):
    sc.tl.rank_genes_groups(a, "g", method="t-test", mean_in_log_space=mls,
                            groups=["0"], reference="1", key_added="k")
    df = sc.get.rank_genes_groups_df(a, "0", key="k").set_index("names").loc[a.var_names]
    res[mls] = df
    for name, r in ref.items():
        d = np.nanmax(np.abs(df["scores"].to_numpy() - np.nan_to_num(r.statistic)))
        print(f"  mean_in_log_space={mls!s:5}  vs {name}:  max |score difference| = {d:.2e}")
print()
# Downstream: (i) a null dataset (no DE at all) for calibration, (ii) the DE dataset above.
mu0 = np.outer(rng.lognormal(np.log(5000), 0.3, n), prop)
X0 = rng.negative_binomial(2, 2 / (2 + mu0)).astype(np.float32)
a0 = ad.AnnData(X0); a0.obs["g"] = pd.Categorical(grp.astype(str))
sc.pp.normalize_total(a0, target_sum=1e4); sc.pp.log1p(a0)
for label, obj in (("null data (no DE)", a0), ("DE data (150 genes 3x up in group 0)", a)):
    sets = {}
    for mls in (True, False):
        sc.tl.rank_genes_groups(obj, "g", method="t-test", mean_in_log_space=mls, key_added="k2")
        df = sc.get.rank_genes_groups_df(obj, "0", key="k2").set_index("names")
        sets[mls] = set(df.index[df["pvals_adj"] < 0.05])
    print(f"  {label}, group 0 vs rest, BH<0.05: log-scale test {len(sets[True]):4d} genes, "
          f"linear-scale test {len(sets[False]):4d} genes, overlap {len(sets[True] & sets[False])}")
print("\nThe two settings are different statistical tests, not two fold-change conventions.")
