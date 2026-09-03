"""SR2: `subsample_counts` (synthetic_doublet_umi_subsampling < 1) inflates the
simulated doublets' total counts.

The function thins the counts of the selected genes first and only then
computes "unsampled" = original_total - thinned_total, so the counts it
already dropped from the selected genes are drawn a second time. Expected
total = rate * T + rate * (1 - rate) * F, where T is the full-gene total and F
the selected-gene total, instead of rate * T. In the original package these
totals normalise the simulated doublets to 1e6, so every simulated doublet is
scaled down; in Scanpy's port the same function runs but its totals are only
stored in `adata_sim.obs["total_counts"]` (normalize_total recomputes row sums),
so the scores are unaffected there.

Run in a venv with scrublet and scanpy installed:  python sr2_subsample_totals.py
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

import scrublet as scr  # noqa: E402
import scrublet.helper_functions as H  # noqa: E402
import scrublet.scrublet as S  # noqa: E402

print("scrublet", md.version("scrublet"), "| scanpy", md.version("scanpy"))


def quiet(fn, *a, **k):
    with redirect_stdout(io.StringIO()):
        return fn(*a, **k)


def subsample_counts_fixed(E, rate, original_totals, random_seed=0):
    """Same draws, but the unsampled part is measured before thinning."""
    if rate < 1:
        np.random.seed(random_seed)
        pre = E.sum(1).A.squeeze()
        E.data = np.random.binomial(np.round(E.data).astype(int), rate)
        current = E.sum(1).A.squeeze()
        unsampled_orig = original_totals - pre
        final = current + np.random.binomial(np.round(unsampled_orig).astype(int), rate)
    else:
        final = original_totals
    return E, final


# ---------------------------------------------------------------- closed form
print("\n[A] closed form on a constructed matrix: 2000 cells, selected-gene total F = 1000, full total T = 4000, rate 0.5")
rng = np.random.default_rng(0)
n = 2000
F = 1000; T = 4000
E = sp.csc_matrix(rng.multinomial(F, np.full(50, 1 / 50), size=n).astype(float))
T_all = np.full(n, float(T))
_, tot_ship = H.subsample_counts(E.copy(), 0.5, T_all.copy(), random_seed=0)
_, tot_fix = subsample_counts_fixed(E.copy(), 0.5, T_all.copy(), random_seed=0)
print(f"  correct expectation rate*T = {0.5*T:.0f}; code's expectation rate*T + rate*(1-rate)*F = {0.5*T + 0.5*0.5*F:.0f}")
print(f"  shipped: mean final total {tot_ship.mean():.1f}   fixed: {tot_fix.mean():.1f}")

# ---------------------------------------------------------------- pipeline effect (original)
print("\n[B] original package, synthetic data, synthetic_doublet_umi_subsampling = 0.8, use_approx_neighbors=False")
X, is_doublet, _ = make_counts()
res = {}
for label, fn in [("shipped", H.subsample_counts), ("fixed", subsample_counts_fixed)]:
    S.subsample_counts = fn
    s = scr.Scrublet(X, random_state=0)
    scores, pred = quiet(s.scrub_doublets, synthetic_doublet_umi_subsampling=0.8, use_approx_neighbors=False, verbose=False)
    F_sim = s._E_sim.sum(1).A.ravel()  # thinned selected-gene counts
    res[label] = (s, scores, pred)
    rec, prec, npred = recall_precision(pred, is_doublet)
    tsim = s._total_counts_sim
    print(f"  {label:8s}: mean simulated total {tsim.mean():9.1f}; threshold {s.threshold_:.4f}; called {npred}; recall {rec:.3f}; precision {prec:.3f}; overall_doublet_rate_ {s.overall_doublet_rate_:.4f}")
S.subsample_counts = H.subsample_counts
s_ship, sc_ship, pr_ship = res["shipped"]
s_fix, sc_fix, pr_fix = res["fixed"]
parents_same = np.array_equal(s_ship.doublet_parents_, s_fix.doublet_parents_)
counts_same = (s_ship._E_sim != s_fix._E_sim).nnz == 0
print(f"  same parents {parents_same}, same thinned counts {counts_same}, totals differ for {(s_ship._total_counts_sim != s_fix._total_counts_sim).sum()} of {len(sc_fix)*2} simulated doublets")
tot_obs = X.sum(1).A.ravel()
pp = s_ship.doublet_parents_
T_pair = tot_obs[pp[:, 0]] + tot_obs[pp[:, 1]]
print(f"  simulated totals / (0.8 * parents' full totals): shipped mean {np.mean(s_ship._total_counts_sim / (0.8 * T_pair)):.4f}, fixed mean {np.mean(s_fix._total_counts_sim / (0.8 * T_pair)):.4f}")
print(f"  observed scores: max|diff| {np.abs(sc_ship - sc_fix).max():.4f}, mean(shipped - fixed) {np.mean(sc_ship - sc_fix):+.4f}; calls differ for {(pr_ship != pr_fix).sum()} cells")
print(f"  simulated scores: mean(shipped - fixed) {np.mean(s_ship.doublet_scores_sim_ - s_fix.doublet_scores_sim_):+.4f}")

s0 = scr.Scrublet(X, random_state=0)
sc0, pr0 = quiet(s0.scrub_doublets, use_approx_neighbors=False, verbose=False)
rec0, prec0, n0 = recall_precision(pr0, is_doublet)
print(f"  for scale, default (no subsampling): threshold {s0.threshold_:.4f}; called {n0}; recall {rec0:.3f}; precision {prec0:.3f}")

# ---------------------------------------------------------------- scanpy port
print("\n[C] scanpy port: same function, totals only stored as metadata")
import anndata as ad  # noqa: E402
import scanpy as sc  # noqa: E402

sc.settings.verbosity = 0
adata = ad.AnnData(sp.csr_matrix(X))
adata.var_names = [f"g{i}" for i in range(X.shape[1])]
import inspect  # noqa: E402

seed_kw = "random_state" if "random_state" in inspect.signature(sc.pp.scrublet_simulate_doublets).parameters or "rng" in inspect.signature(sc.pp.scrublet_simulate_doublets).parameters else "random_seed"
sim = sc.pp.scrublet_simulate_doublets(adata, sim_doublet_ratio=2.0, synthetic_doublet_umi_subsampling=0.8, **{seed_kw: 0})
rows = np.asarray(sim.X.sum(1)).ravel()
pp = sim.obsm["doublet_parents"]
T_pair = tot_obs[pp[:, 0]] + tot_obs[pp[:, 1]]
stored = sim.obs["n_counts"].to_numpy()  # the port stores the subsampled totals here
print(f"  adata_sim.obs['n_counts'] / X.sum(1): mean {np.mean(stored / rows):.4f} (all genes kept here, so F = T and the code's expected inflation factor is 1 + (1-rate) = {2-0.8:.1f})")
print(f"  adata_sim.obs['n_counts'] / (0.8 * parents' totals): mean {np.mean(stored / (0.8 * T_pair)):.4f}")
a1 = adata.copy(); a2 = adata.copy()
sc.pp.scrublet(a1, synthetic_doublet_umi_subsampling=0.8, use_approx_neighbors=False, random_state=0)
sc.pp.scrublet(a2, synthetic_doublet_umi_subsampling=1.0, use_approx_neighbors=False, random_state=0)
print(f"  sc.pp.scrublet runs with subsampling 0.8 (threshold {a1.uns['scrublet'].get('threshold', float('nan')):.4f}) and 1.0 (threshold {a2.uns['scrublet'].get('threshold', float('nan')):.4f}); its normalisation uses X row sums, not these totals")
