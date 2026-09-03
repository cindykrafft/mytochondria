"""SR1: Scanpy's Scrublet port scores each cell over k_adj - 1 real neighbours
plus the cell itself (sklearn / default backend) or k_adj - 1 neighbours
(pynndescent backend), while the original uses k_adj real neighbours; both
then divide by N = k_adj.

Both classifiers are run on the *same* manifold (PCA coordinates taken from an
original-scrublet run on synthetic data with labelled doublets), so the only
thing that can differ is the neighbour rule. The reference kNN (exact,
self-excluded by index) is used to say which rule each package implements.

Run in a venv with scrublet and scanpy installed:  python sr1_scanpy_knn_self_neighbour.py
"""

from __future__ import annotations

import importlib.metadata as md
import inspect
import io
import sys
import warnings
from contextlib import redirect_stdout

import numpy as np
from sklearn.neighbors import NearestNeighbors

warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import reference as R  # noqa: E402
from synth import make_counts, recall_precision  # noqa: E402

import scanpy as sc  # noqa: E402
import scrublet as scr  # noqa: E402

try:
    from scanpy.preprocessing._scrublet.core import Scrublet as ScanpyScrublet
except ImportError:  # 1.9-era layout
    from scanpy.external.pp._scrublet import Scrublet as ScanpyScrublet  # type: ignore

sc.settings.verbosity = 0
print("scrublet", md.version("scrublet"), "| scanpy", md.version("scanpy"), "| scikit-learn", md.version("scikit-learn"), "| pynndescent", md.version("pynndescent"))


def quiet(fn, *a, **k):
    with redirect_stdout(io.StringIO()):
        return fn(*a, **k)


X, is_doublet, _ = make_counts()
n_obs = X.shape[0]
orig = scr.Scrublet(X, random_state=0, expected_doublet_rate=0.1)
quiet(orig.scrub_doublets, use_approx_neighbors=False, verbose=False)
mo, ms = orig.manifold_obs_, orig.manifold_sim_
n_sim = ms.shape[0]
k = orig.n_neighbors
k_adj = R.k_adjusted(k, n_obs, n_sim)
r = n_sim / n_obs
rho = 0.1
print(f"\nmanifold: {n_obs} observed + {n_sim} simulated, {mo.shape[1]} PCs; k = {k}, k_adj = {k_adj}, r = {r}, rho = {rho}")

manifold = np.vstack([mo, ms])
labels = np.r_[np.zeros(n_obs, int), np.ones(n_sim, int)]


def nd_exact(kk):
    nb = NearestNeighbors(n_neighbors=kk).fit(manifold).kneighbors(return_distance=False)  # self excluded by index
    return labels[nb].sum(1)


rules = {
    "k_adj real neighbours, self excluded (original)": nd_exact(k_adj),
    "k_adj-1 real neighbours + self counted with own label": nd_exact(k_adj - 1) + labels,
    "k_adj-1 real neighbours, self excluded": nd_exact(k_adj - 1),
}
N = float(k_adj)


def which_rule(scores_all, tol):
    out = []
    for name, nd in rules.items():
        d = np.abs(scores_all - R.score(nd, N, rho, r)).max()
        out.append((d, name))
    out.sort()
    return out


print("\n--- original scrublet classifier on this manifold (use_approx_neighbors=False)")
o_all = np.r_[orig.doublet_scores_obs_, orig.doublet_scores_sim_]
for d, name in which_rule(o_all, 1e-12):
    print(f"  max|score - score({name})| = {d:.3g}")

results = {"original": (orig.doublet_scores_obs_, orig.doublet_scores_sim_)}
for uan in [None, False, True]:
    seed_kw = "rng" if "rng" in inspect.signature(ScanpyScrublet).parameters else "random_state"
    p = ScanpyScrublet(counts_obs=np.ones((n_obs, 2)), n_neighbors=k, expected_doublet_rate=rho, stdev_doublet_rate=0.02, **{seed_kw: 0})
    p.set_manifold(mo, ms)
    quiet(p.calculate_doublet_scores, use_approx_neighbors=uan)
    p_all = np.r_[p.doublet_scores_obs_, p.doublet_scores_sim_]
    print(f"\n--- scanpy port on the same manifold, use_approx_neighbors={uan}")
    for d, name in which_rule(p_all, 1e-12):
        print(f"  max|score - score({name})| = {d:.3g}")
    results[f"scanpy(use_approx_neighbors={uan})"] = (p.doublet_scores_obs_, p.doublet_scores_sim_)

print("\n--- consequences (same manifold, threshold by skimage.threshold_minimum on each package's own simulated scores)")
from skimage.filters import threshold_minimum

o_obs, o_sim = results["original"]
print(f"  {'classifier':44s} {'max obs score':>13s} {'min sim score':>13s} {'threshold':>9s} {'called':>6s} {'recall':>6s} {'prec':>6s} {'mean obs Δ vs orig':>18s} {'mean sim Δ':>10s}")
for name, (obs, sim) in results.items():
    try:
        t = threshold_minimum(sim)
    except Exception as e:  # noqa: BLE001
        t = np.nan
    pred = obs > t
    rec, prec, n = recall_precision(pred, is_doublet)
    print(f"  {name:44s} {obs.max():13.4f} {sim.min():13.4f} {t:9.4f} {n:6d} {rec:6.3f} {prec:6.3f} {np.mean(obs - o_obs):18.4f} {np.mean(sim - o_sim):10.4f}")

p_obs, p_sim = results["scanpy(use_approx_neighbors=False)"]
t_o, t_p = threshold_minimum(o_sim), threshold_minimum(p_sim)
flip = (o_obs > t_o) != (p_obs > t_p)
print(f"\n  cells whose call differs between original and scanpy(sklearn) on the same manifold: {flip.sum()} of {n_obs}")
print(f"  observed cells with score strictly lower in the port than in the original: {(p_obs < o_obs - 1e-12).sum()}; higher: {(p_obs > o_obs + 1e-12).sum()}")
print(f"  simulated doublets with score strictly higher in the port: {(p_sim > o_sim + 1e-12).sum()}; lower: {(p_sim < o_sim - 1e-12).sum()}")
print(f"  largest attainable observed score: original (nd=k_adj) {R.score(float(k_adj), N, rho, r):.4f}; port (nd<=k_adj-1) {R.score(float(k_adj-1), N, rho, r):.4f}")

# ---------------------------------------------------------------- mechanism
print("\n--- mechanism: what `Neighbors` stores and what the port's classifier receives")
import anndata as ad  # noqa: E402
from scanpy.neighbors import Neighbors  # noqa: E402
from scanpy.neighbors._common import _get_indices_distances_from_sparse_matrix as gi  # noqa: E402
from scanpy.neighbors._common import _has_self_column  # noqa: E402
from sklearn.neighbors import KNeighborsTransformer  # noqa: E402

rng = np.random.default_rng(0)
M = rng.normal(size=(12, 3)); M[7] = M[3]  # 12 points, rows 3 and 7 coincide
T = KNeighborsTransformer(algorithm="brute", n_neighbors=4, metric="euclidean", mode="distance").fit_transform(M)
print(f"  sklearn KNeighborsTransformer(n_neighbors=4): {T.getnnz(1)[0]} entries per row, the cell itself included: row 0 -> {T[0].indices.tolist()}, row 3 -> {T[3].indices.tolist()} (distances {np.round(T[3].data, 3).tolist()})")
nb = Neighbors(ad.AnnData(M))
quiet(nb.compute_neighbors, 4, metric="euclidean", knn=True, transformer="sklearn", method=None, **({"rng": 0} if "rng" in inspect.signature(nb.compute_neighbors).parameters else {"random_state": 0}))
D = nb.distances
print(f"  Neighbors.compute_neighbors(4) stores {D.getnnz(1)[0]} neighbours per row (self removed by *position*): row 0 -> {D[0].indices.tolist()}, row 3 -> {D[3].indices.tolist()}, row 7 -> {D[7].indices.tolist()}  <- row 7 keeps itself, its twin was in column 0")
idx, dist = gi(D, 4)
print(f"  classifier's _get_indices_distances_from_sparse_matrix(distances, 4): shape {idx.shape}; _has_self_column (an .any() over rows) = {_has_self_column(idx, dist)} -> no self column prepended, every cell gets {idx.shape[1]} = k_adj-1 neighbours")
M2 = rng.normal(size=(12, 3))
nb2 = Neighbors(ad.AnnData(M2))
quiet(nb2.compute_neighbors, 4, metric="euclidean", knn=True, transformer="sklearn", method=None, **({"rng": 0} if "rng" in inspect.signature(nb2.compute_neighbors).parameters else {"random_state": 0}))
idx2, dist2 = gi(nb2.distances, 4)
print(f"  same without coincident points: shape {idx2.shape}, rows with column 0 == the cell itself: {(idx2[:, 0] == np.arange(12)).sum()} of 12 -> self column prepended, every cell gets k_adj-1 neighbours plus itself")

print("\n--- the port's own pipeline (sc.pp.scrublet, exact neighbours): which rule applied, by seed")
import scanpy.preprocessing._scrublet.core as core  # noqa: E402
import scipy.sparse as sp  # noqa: E402

_orig = core._get_indices_distances_from_sparse_matrix
seen = {}


def spy(d, kk):
    out = _orig(d, kk)
    seen["shape"] = out[0].shape; seen["self0"] = int((out[0][:, 0] == np.arange(out[0].shape[0])).sum()); seen["k"] = kk
    return out


core._get_indices_distances_from_sparse_matrix = spy
for seed, n in [(1, 1500), (2, 1500), (3, 1500), (4, 600), (5, 300), (6, 180), (7, 180)]:
    Xs, _, _ = make_counts(n_singlets=n, n_doublets=n // 10, seed=seed)
    a = ad.AnnData(sp.csr_matrix(Xs)); a.var_names = [f"g{i}" for i in range(Xs.shape[1])]
    sc.pp.scrublet(a, use_approx_neighbors=False, random_state=0)
    pp = a.uns["scrublet"]["doublet_parents"]
    twice = len(pp) - len({tuple(sorted(p)) for p in pp})
    selfp = int((pp[:, 0] == pp[:, 1]).sum())
    rule = "k_adj-1 neighbours, no self" if seen["self0"] < seen["shape"][0] else "k_adj-1 neighbours + self"
    print(f"  seed {seed}, n_obs {Xs.shape[0]:4d}: simulated parents drawn as (i,i) {selfp}, unordered pair drawn twice {twice} -> neighbour matrix {seen['shape']} for k_adj = {seen['k']}: {rule}")
core._get_indices_distances_from_sparse_matrix = _orig
