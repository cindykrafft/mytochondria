"""Same input, same seed: the original package vs Scanpy's port, end to end,
and step by step, on synthetic data with labelled doublets.

Both are run at their own defaults (except the exact-neighbour backend, so that
approximate-search noise does not enter), then with the port's
`expected_doublet_rate` set to the original's 0.1. The step-by-step part
feeds the port the original's *simulated doublets* (through `adata_sim`) so
that only preprocessing/embedding/kNN differences remain, and finally the
original's PCA manifold, so that only the kNN rule remains.

Run in a venv with scrublet and scanpy installed:  python compare_original_vs_scanpy.py
"""

from __future__ import annotations

import importlib.metadata as md
import io
import sys
import warnings
from contextlib import redirect_stdout

import numpy as np
import pandas as pd
import scipy.sparse as sp
from scipy.stats import spearmanr

warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from synth import make_counts, recall_precision  # noqa: E402

import anndata as ad  # noqa: E402
import scanpy as sc  # noqa: E402
import scrublet as scr  # noqa: E402

sc.settings.verbosity = 0
print("scrublet", md.version("scrublet"), "| scanpy", md.version("scanpy"))


def quiet(fn, *a, **k):
    with redirect_stdout(io.StringIO()):
        return fn(*a, **k)


def row(name, scores, pred, sim, thr, truth, ref_scores=None, ref_pred=None):
    rec, prec, n = recall_precision(pred, truth)
    extra = ""
    if ref_scores is not None:
        rho = spearmanr(scores, ref_scores).correlation
        jac = (pred & ref_pred).sum() / max((pred | ref_pred).sum(), 1)
        extra = f"  Spearman vs original {rho:.3f}  call Jaccard {jac:.3f}  max|Δscore| {np.abs(scores - ref_scores).max():.3f}"
    print(f"  {name:58s} thr {thr:6.4f}  called {n:4d}  recall {rec:.3f}  prec {prec:.3f}{extra}")


X, is_doublet, _ = make_counts()
n_obs = X.shape[0]
print(f"\nsynthetic data: {n_obs} cells, {is_doublet.sum()} true doublets")

print("\n[1] defaults of each package (exact neighbours)")
o = scr.Scrublet(X, random_state=0)
o_scores, o_pred = quiet(o.scrub_doublets, use_approx_neighbors=False, verbose=False)
row("original: scr.Scrublet(X, random_state=0).scrub_doublets()", o_scores, o_pred, o.doublet_scores_sim_, o.threshold_, is_doublet)
print(f"    original preprocessing: {len(o._gene_filter)} genes kept (v-score >= 85th pctl, >=3 counts in >=3 cells); k = {o.n_neighbors}; expected_doublet_rate 0.1")
adata = ad.AnnData(sp.csr_matrix(X)); adata.var_names = [f"g{i}" for i in range(X.shape[1])]
a = adata.copy()
sc.pp.scrublet(a, use_approx_neighbors=False, random_state=0)
p_pred = a.obs["predicted_doublet"].to_numpy().astype(bool)
row("scanpy: sc.pp.scrublet(adata, random_state=0)", a.obs["doublet_score"].to_numpy(), p_pred, a.uns["scrublet"]["doublet_scores_sim"], a.uns["scrublet"].get("threshold", np.nan), is_doublet, o_scores, o_pred)
print(f"    scanpy preprocessing: filter_genes(min_cells=3), filter_cells(min_genes=3), normalize_total (median), highly_variable_genes (seurat flavour) -> {int(a.uns['scrublet']['doublet_parents'].shape[0])} simulated doublets; expected_doublet_rate default {a.uns['scrublet']['parameters']['expected_doublet_rate']}")
a2 = adata.copy()
sc.pp.scrublet(a2, use_approx_neighbors=False, random_state=0, expected_doublet_rate=0.1)
p2_pred = a2.obs["predicted_doublet"].to_numpy().astype(bool)
row("scanpy, expected_doublet_rate=0.1 (original's default)", a2.obs["doublet_score"].to_numpy(), p2_pred, a2.uns["scrublet"]["doublet_scores_sim"], a2.uns["scrublet"].get("threshold", np.nan), is_doublet, o_scores, o_pred)
pp_o = o.doublet_parents_; pp_p = a2.uns["scrublet"]["doublet_parents"]
shared = len({tuple(sorted(p)) for p in pp_o} & {tuple(sorted(p)) for p in pp_p})
print(f"    doublet parents with the same seed: original {pp_o.shape[0]} pairs (with replacement, {(pp_o[:,0]==pp_o[:,1]).sum()} self-pairs), scanpy {pp_p.shape[0]} pairs (grid without replacement, {(pp_p[:,0]==pp_p[:,1]).sum()} self-pairs); unordered pairs in common: {shared}")

print("\n[2] port fed the original's gene set and simulated doublets (adata_sim), expected_doublet_rate=0.1: differences left are z-score ddof, PCA seed, kNN rule")
genes = o._gene_filter
obs_hv = ad.AnnData(sp.csr_matrix(X[:, genes])); obs_hv.var_names = [f"g{i}" for i in genes]
obs_hv.obs_names = [str(i) for i in range(n_obs)]
sim_hv = ad.AnnData(sp.csr_matrix(o._E_sim)); sim_hv.var_names = obs_hv.var_names
sim_hv.obsm["doublet_parents"] = pp_o
# the original normalises both to 1e6 with *full-gene* totals; replicate that so only the core differs
obs_hv.X = sp.csr_matrix(sp.diags(1e6 / X.sum(1).A.ravel()) @ obs_hv.X)
sim_hv.X = sp.csr_matrix(sp.diags(1e6 / o._total_counts_sim) @ sim_hv.X)
a3 = sc.pp.scrublet(obs_hv, adata_sim=sim_hv, use_approx_neighbors=False, random_state=0, expected_doublet_rate=0.1, copy=True)
p3_pred = a3.obs["predicted_doublet"].to_numpy().astype(bool)
row("scanpy core on the original's obs/sim matrices", a3.obs["doublet_score"].to_numpy(), p3_pred, a3.uns["scrublet"]["doublet_scores_sim"], a3.uns["scrublet"].get("threshold", np.nan), is_doublet, o_scores, o_pred)
print(f"    port's simulated-score minimum {a3.uns['scrublet']['doublet_scores_sim'].min():.4f} vs original's {o.doublet_scores_sim_.min():.4f}; port's observed-score maximum {a3.obs['doublet_score'].max():.4f} vs original's {o_scores.max():.4f}")

print("\n[3] port's classifier on the original's PCA manifold (only the kNN rule differs) -- see sr1_scanpy_knn_self_neighbour.py for the rule")
import inspect  # noqa: E402
from scanpy.preprocessing._scrublet.core import Scrublet as P
seed_kw = "rng" if "rng" in inspect.signature(P).parameters else "random_state"
p = P(counts_obs=np.ones((n_obs, 2)), n_neighbors=o.n_neighbors, expected_doublet_rate=0.1, stdev_doublet_rate=0.02, **{seed_kw: 0})
p.set_manifold(o.manifold_obs_, o.manifold_sim_)
quiet(p.calculate_doublet_scores, use_approx_neighbors=False)
quiet(p.call_doublets, verbose=False)
row("scanpy classifier, original manifold", p.doublet_scores_obs_, p.predicted_doublets_, p.doublet_scores_sim_, p.threshold_, is_doublet, o_scores, o_pred)

print("\n[4] z-score ddof: the port uses ddof=1, the original ddof=0 -- a uniform rescaling of every gene, invariant for PCA-then-Euclidean-kNN")
from scanpy.preprocessing._scrublet import pipeline as PL
p4 = P(counts_obs=X[:, genes], n_neighbors=o.n_neighbors, expected_doublet_rate=0.1, stdev_doublet_rate=0.02, **{seed_kw: 0})
p4._counts_obs_norm = sp.csc_matrix(obs_hv.X); p4._counts_sim_norm = sp.csc_matrix(sim_hv.X)
PL.zscore(p4)
Zo = np.asarray(p4._counts_obs_norm.todense())
Zo_orig = np.asarray(o._E_obs_norm)
ratio = (Zo / Zo_orig)[np.abs(Zo_orig) > 1e-6]
print(f"    port z-scores / original z-scores: min {ratio.min():.6f} max {ratio.max():.6f}; sqrt((n-1)/n) = {np.sqrt((n_obs-1)/n_obs):.6f}")
