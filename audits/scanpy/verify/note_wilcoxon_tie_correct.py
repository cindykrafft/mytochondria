#!/usr/bin/env python3
"""Note: rank_genes_groups(method="wilcoxon") defaults to tie_correct=False.

Without the tie term the rank-sum variance is n*m*(N+1)/12 instead of tc * that, with
tc = 1 - sum(t^3 - t)/(N^3 - N) over tie groups. On sparse counts (mostly zeros) tc is
far below 1, so |z| is shrunk by sqrt(tc) and p-values are conservative. Documented
behaviour (the `tie_correct` argument exists); this measures the size on 10x-like data
by running the shipped function both ways.
"""
import numpy as np, pandas as pd, anndata as ad, scanpy as sc
from importlib.metadata import version
sc.settings.verbosity = 0
rng = np.random.default_rng(2)
n, G = 3000, 4000
prop = np.exp(rng.normal(-5, 2, G)); prop /= prop.sum()
lib = rng.lognormal(np.log(5000), 0.3, n)
grp = np.r_[np.zeros(300, int), np.ones(n - 300, int)]
mu = np.outer(lib, prop); mu[grp == 0, :200] *= 2.5
X = rng.negative_binomial(2, 2 / (2 + mu)).astype(np.float32)
a = ad.AnnData(X); a.obs["g"] = pd.Categorical(grp.astype(str))
sc.pp.normalize_total(a, target_sum=1e4); sc.pp.log1p(a)
print("scanpy", version("scanpy"))
out = {}
for tc in (False, True):
    sc.tl.rank_genes_groups(a, "g", method="wilcoxon", tie_correct=tc, key_added="k")
    out[tc] = sc.get.rank_genes_groups_df(a, "0", key="k").set_index("names")
z0, z1 = out[False]["scores"], out[True]["scores"].loc[out[False].index]
frac_zero = 1 - (a.X > 0).mean(0)
ratio = (z0 / z1).to_numpy()
ok = np.isfinite(ratio) & (np.abs(z1.to_numpy()) > 1e-6)
print("|z| without tie correction / |z| with, by gene sparsity:")
fz = pd.Series(np.asarray(frac_zero).ravel(), index=a.var_names).loc[out[False].index].to_numpy()
for lo, hi in ((0, 0.5), (0.5, 0.8), (0.8, 0.95), (0.95, 1.0)):
    b = ok & (fz >= lo) & (fz < hi)
    if b.sum(): print(f"  zeros in [{lo:.2f},{hi:.2f}): n={b.sum():4d}  median ratio {np.median(ratio[b]):.3f}")
mu0 = np.outer(rng.lognormal(np.log(5000), 0.3, n), prop)
a0 = ad.AnnData(rng.negative_binomial(2, 2 / (2 + mu0)).astype(np.float32)); a0.obs["g"] = pd.Categorical(grp.astype(str))
sc.pp.normalize_total(a0, target_sum=1e4); sc.pp.log1p(a0)
for label, obj in (("null data", a0), ("DE data (200 genes 2.5x up)", a)):
    for tc in (False, True):
        sc.tl.rank_genes_groups(obj, "g", method="wilcoxon", tie_correct=tc, key_added="k")
        df = sc.get.rank_genes_groups_df(obj, "0", key="k").set_index("names")
        print(f"  {label:28} tie_correct={tc!s:5}: BH<0.05 genes = {(df['pvals_adj'] < 0.05).sum():4d}")
