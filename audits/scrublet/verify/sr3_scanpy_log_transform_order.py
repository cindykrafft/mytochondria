"""SR3: `sc.pp.scrublet(log_transform=True)` log-transforms the observed cells
and the simulated doublets on different scales, and before (not after) the
per-cell 1e6 normalisation.

In `_run_scrublet` the observed matrix is `normalize_total` (median target)
at the time `log1p` is applied, while the simulated doublets are raw summed
counts; both are then `normalize_total(target_sum=1e6)` on the *log* values.
The original package normalises both to 1e6 first and takes log10(1 + x) of
both. The two populations therefore get different transforms in the port.

Measured: recall/precision against labelled doublets and the separation of
simulated from observed cells (mean score of each population) for
log_transform False/True in the port and in the original.

Run in a venv with scrublet and scanpy installed:  python sr3_scanpy_log_transform_order.py
"""

from __future__ import annotations

import importlib.metadata as md
import io
import sys
import warnings
from contextlib import redirect_stdout

import numpy as np
import scipy.sparse as sp

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


def summarise(name, obs, sim, pred, truth, thr):
    rec, prec, n = recall_precision(pred, truth)
    print(f"  {name:52s} mean obs score {np.mean(obs):.3f}  mean sim score {np.mean(sim):.3f}  threshold {thr:7.4f}  called {n:4d}  recall {rec:.3f}  precision {prec:.3f}")


for seed in (1, 2):
    X, is_doublet, _ = make_counts(seed=seed)
    print(f"\nsynthetic data seed {seed}: {X.shape[0]} cells, {is_doublet.sum()} true doublets")
    adata = ad.AnnData(sp.csr_matrix(X)); adata.var_names = [f"g{i}" for i in range(X.shape[1])]
    for lt in (False, True):
        a = adata.copy()
        sc.pp.scrublet(a, log_transform=lt, use_approx_neighbors=False, random_state=0, expected_doublet_rate=0.1)
        thr = a.uns["scrublet"].get("threshold", np.nan)
        pred = a.obs["predicted_doublet"].to_numpy().astype(bool)
        summarise(f"scanpy  log_transform={lt}", a.obs["doublet_score"].to_numpy(), a.uns["scrublet"]["doublet_scores_sim"], pred, is_doublet, thr)
    for lt in (False, True):
        s = scr.Scrublet(X, random_state=0, expected_doublet_rate=0.1)
        scores, pred = quiet(s.scrub_doublets, log_transform=lt, use_approx_neighbors=False, verbose=False)
        thr = getattr(s, "threshold_", np.nan)
        if pred is None:
            pred = np.zeros(X.shape[0], bool)
        summarise(f"original log_transform={lt}", scores, s.doublet_scores_sim_, pred, is_doublet, thr)

# mechanism: what the port feeds to the classifier when log_transform=True
print("\nmechanism (seed 1): the matrices the port builds before z-scoring, log_transform=True")
X, is_doublet, _ = make_counts(seed=1)
adata = ad.AnnData(sp.csr_matrix(X)); adata.var_names = [f"g{i}" for i in range(X.shape[1])]
ad_obs = adata.copy()
sc.pp.filter_genes(ad_obs, min_cells=3); sc.pp.filter_cells(ad_obs, min_genes=3)
ad_obs.layers["raw"] = ad_obs.X.copy()
sc.pp.normalize_total(ad_obs)
ad_obs.layers["log1p"] = ad_obs.X.copy(); sc.pp.log1p(ad_obs, layer="log1p"); sc.pp.highly_variable_genes(ad_obs, layer="log1p")
ad_obs = ad_obs[:, ad_obs.var["highly_variable"]].copy()
ad_sim = sc.pp.scrublet_simulate_doublets(ad_obs, layer="raw", sim_doublet_ratio=2.0, random_state=0)
obs_before = np.asarray(ad_obs.X.sum(1)).ravel(); sim_before = np.asarray(ad_sim.X.sum(1)).ravel()
print(f"  per-cell sums over the {ad_obs.n_vars} HVGs at the moment log1p is applied: observed (median-normalised) mean {obs_before.mean():.1f}, simulated (raw sums) mean {sim_before.mean():.1f}")
sc.pp.log1p(ad_obs); sc.pp.log1p(ad_sim)
sc.pp.normalize_total(ad_obs, target_sum=1e6); sc.pp.normalize_total(ad_sim, target_sum=1e6)
mo = np.asarray(ad_obs.X.mean(0)).ravel(); ms = np.asarray(ad_sim.X.mean(0)).ravel()
print(f"  after log1p then normalize_total(1e6): correlation of mean gene profiles obs vs sim = {np.corrcoef(mo, ms)[0,1]:.4f}")
print("  (the original applies log10(1+x) after both populations are normalised to 1e6 by their full-gene totals, so they share one transform)")

# structural test: a "doublet" made from a cell and itself is 2x that cell. Under one common
# per-cell normalisation it lands exactly on its parent; if observed and simulated cells are
# transformed differently it does not.
print("\nself-doublet test (seed 1): sim = raw counts of cell i added to itself, for 20 cells, then each package's transform sequence")
X, is_doublet, _ = make_counts(seed=1)
adata = ad.AnnData(sp.csr_matrix(X)); adata.var_names = [f"g{i}" for i in range(X.shape[1])]
ad_obs = adata.copy()
sc.pp.filter_genes(ad_obs, min_cells=3); sc.pp.filter_cells(ad_obs, min_genes=3)
ad_obs.layers["raw"] = ad_obs.X.copy()
sc.pp.normalize_total(ad_obs)  # median target, as in _run_scrublet
ad_obs.layers["log1p"] = ad_obs.X.copy(); sc.pp.log1p(ad_obs, layer="log1p"); sc.pp.highly_variable_genes(ad_obs, layer="log1p")
ad_obs = ad_obs[:, ad_obs.var["highly_variable"]].copy()
cells = np.arange(20)
raw = sp.csr_matrix(ad_obs.layers["raw"])
ad_sim = ad.AnnData(sp.csr_matrix(raw[cells] + raw[cells])); ad_sim.var_names = ad_obs.var_names
for lt in (False, True):
    o = ad_obs.copy(); s_ = ad_sim.copy()
    del o.layers["raw"]
    if lt:
        sc.pp.log1p(o); sc.pp.log1p(s_)
    sc.pp.normalize_total(o, target_sum=1e6); sc.pp.normalize_total(s_, target_sum=1e6)
    d = np.linalg.norm(o.X[cells].toarray() - s_.X.toarray(), axis=1) / np.linalg.norm(o.X[cells].toarray(), axis=1)
    print(f"  scanpy   log_transform={lt!s:5}: relative distance between cell i and its self-doublet: max {d.max():.3g}, mean {d.mean():.3g}")
tot = np.asarray(raw.sum(1)).ravel()  # HVG-subset totals stand in for full totals; the ratio parent:doublet is 1:2 either way
for lt in (False, True):
    o = sp.diags(1e6 / tot) @ raw
    s_ = sp.diags(1e6 / (2 * tot[cells])) @ (raw[cells] + raw[cells])
    o = o[cells].toarray(); s_ = s_.toarray()
    if lt:
        o = np.log10(1 + o); s_ = np.log10(1 + s_)
    d = np.linalg.norm(o - s_, axis=1) / np.linalg.norm(o, axis=1)
    print(f"  original log_transform={lt!s:5}: relative distance between cell i and its self-doublet: max {d.max():.3g}, mean {d.mean():.3g}")
