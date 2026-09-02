#!/usr/bin/env python3
"""SC2: score_genes' expression bins are not n_bins equal-frequency bins; the top bin
holds between 1 and ~n_bins/2 genes.

src/scanpy/tools/_score_genes.py, `_score_genes_bins`:

    n_items = int(np.round(len(obs_avg) / (n_bins - 1)))
    obs_cut = obs_avg.rank(method="min") // n_items

Ranks run 1..N, so bins 0..n_bins-2 hold n_items genes each (bin 0 one fewer) and the
last bin holds the N - (n_bins-1)*n_items + 1 highest-expressed genes -- between 1 and
about n_bins/2 depending on rounding, or none at all when rounding goes the other way
(then there are only n_bins-1 bins). Seurat's AddModuleScore, which the docstring says
this reproduces, uses cut_number(): n_bins equal-frequency bins.

Consequence: a gene list containing any of the top handful of expressed genes draws its
matched controls for that bin from at most a handful of genes (fewer after removing the
list genes themselves); a list made of those genes cannot be scored at all.

Part A: closed form, bin sizes for realistic N and n_bins.
Part B: the shipped function on 10x-like simulated data (20,000 genes).
Part C: the same lists scored with equal-frequency bins (one-line replacement),
        to show the intended behaviour is reachable.
"""
import io
import sys
from importlib.metadata import version

import numpy as np
import pandas as pd
import anndata as ad
import scanpy as sc
from scanpy.tools import _score_genes as sg

print("scanpy", version("scanpy"))

# ------------------------------------------------------------------ Part A
print("\nPART A  bin sizes from the formula, ranks 1..N, obs_cut = rank // round(N/(n_bins-1))")
print("%8s %7s | %7s %7s %10s %8s" % ("N genes", "n_bins", "n_items", "n bins", "typical", "top bin"))
for N in (2000, 18000, 20000, 25000, 30000, 33000):
    for nb in (25, 10):
        n_items = int(np.round(N / (nb - 1)))
        cut = (np.arange(1, N + 1)) // n_items
        sizes = np.bincount(cut)
        print("%8d %7d | %7d %7d %10d %8d" % (N, nb, n_items, len(sizes), sizes[1], sizes[-1]))
print("        Seurat cut_number(): every bin holds N/n_bins genes (800 for N=20,000, n_bins=25).")

# ------------------------------------------------------------------ data
rng = np.random.default_rng(1)
n, G = 1500, 20000
prop = np.exp(rng.normal(-5, 2, G)); prop /= prop.sum()
lib = rng.lognormal(np.log(5000), 0.3, n)
X = rng.negative_binomial(2, 2 / (2 + np.outer(lib, prop))).astype(np.float32)
a = ad.AnnData(X)
a.var_names = [f"g{i}" for i in range(G)]
sc.pp.normalize_total(a, target_sum=1e4)
sc.pp.log1p(a)
avg = pd.Series(np.asarray(a.X.mean(0)).ravel(), index=a.var_names).sort_values()
top = list(avg.index[-9:])                    # scanpy's degenerate top bin for N=20,000

def run(genes, **kw):
    buf = io.StringIO()
    sc.settings.logfile = buf
    sc.settings.verbosity = 4
    try:
        sc.tl.score_genes(a, genes, score_name="s", rng=0, **kw)
    except RuntimeError as e:
        return f"RuntimeError: {e}"
    finally:
        sc.settings.verbosity = 0
        sc.settings.logfile = sys.stdout
    s = a.obs["s"].to_numpy()
    ctrl = [l for l in buf.getvalue().splitlines() if "control genes are used" in l]
    nctrl = ctrl[-1].strip().split()[0] if ctrl else "?"
    return f"controls used = {nctrl:>4}   score mean = {s.mean():+.3f}  sd = {s.std():.3f}"

cases = [
    ("1 top-9 gene + 4 mid-ranked genes", [top[-1]] + list(avg.index[10000:10004])),
    ("5 of the top-9 genes", top[-5:]),
    ("all top-9 genes", top),
    ("all top-9 genes, ctrl_as_ref=False", top),
    ("5 genes ranked ~10,000 (control)", list(avg.index[10000:10005])),
    ("50 random genes (control)", list(rng.choice(a.var_names, 50, replace=False))),
]

# ------------------------------------------------------------------ Part B
print("\nPART B  shipped score_genes on simulated 10x-like data, 20,000 genes, no module structure")
for name, genes in cases:
    kw = {"ctrl_as_ref": False} if "ctrl_as_ref" in name else {}
    print(f"  {name:38} {run(genes, **kw)}")

# ------------------------------------------------------------------ Part C
print("\nPART C  same calls after replacing the two binning lines with n_bins equal-frequency bins")
_orig = sg._score_genes_bins
def _bins_equal_freq(gene_list, gene_pool, *, ctrl_as_ref, ctrl_size, n_bins, get_subset, rng):
    obs_avg = pd.Series(sg._nan_means(get_subset(gene_pool), axis=0), index=gene_pool)
    obs_avg = obs_avg[np.isfinite(obs_avg)]
    # equal-frequency bins, as Seurat's cut_number(): ranks 0..N-1 scaled to 0..n_bins-1
    obs_cut = ((obs_avg.rank(method="first") - 1) * n_bins // len(obs_avg)).astype(int)
    keep_ctrl_in_obs_cut = np.False_ if ctrl_as_ref else obs_cut.index.isin(gene_list)
    cuts = np.unique(obs_cut.loc[gene_list])
    for cut, sub_rng in zip(cuts, rng.spawn(len(cuts)), strict=True):
        r_genes = obs_cut[(obs_cut == cut) & ~keep_ctrl_in_obs_cut].index
        if ctrl_size < len(r_genes):
            r_genes = r_genes.to_series().sample(ctrl_size, random_state=sub_rng).index
        if ctrl_as_ref:
            r_genes = r_genes.difference(gene_list)
        yield r_genes
sg._score_genes_bins = _bins_equal_freq
for name, genes in cases:
    kw = {"ctrl_as_ref": False} if "ctrl_as_ref" in name else {}
    print(f"  {name:38} {run(genes, **kw)}")
sg._score_genes_bins = _orig
