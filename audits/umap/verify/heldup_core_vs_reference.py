#!/usr/bin/env python3
"""Held-up checks on the deterministic core, executed on the shipped code.

1. smooth_knn_dist sigma/rho vs the paper's definition solved with scipy brentq
   (local_connectivity 1.0 and 1.5), row sums of the kernel = log2(k).
2. fuzzy_simplicial_set: symmetric, entries in [0, 1], equals A + A.T - A*A.T computed
   in numpy from the unsymmetrised matrix; set_op_mix_ratio=0.5 equals the documented mix.
3. find_ab_params vs an independent least-squares fit of the same curve, and the
   documented default (min_dist=0.1, spread=1.0).
4. spectral_layout vs dense scipy.linalg.eigh of the normalized Laplacian (subspace).
5. metric='euclidean' vs metric='precomputed' on the same distances: identical graph_.
6. nearest_neighbors exact small-data path vs sklearn NearestNeighbors.
"""
import warnings
import numpy as np
import scipy.linalg
import scipy.sparse
from scipy.optimize import brentq, least_squares
from scipy.spatial.distance import cdist
from sklearn.neighbors import NearestNeighbors
import umap
from umap.umap_ import smooth_knn_dist, compute_membership_strengths, fuzzy_simplicial_set, find_ab_params
from umap.spectral import spectral_layout

warnings.simplefilter("ignore")
print("umap-learn", umap.__version__)
rng = np.random.default_rng(1)
k = 15
X = np.vstack([rng.normal(0, 1, (400, 10)), rng.normal(4, 1, (400, 10))]).astype(np.float32)
knn_dists, knn_indices = NearestNeighbors(n_neighbors=k).fit(X).kneighbors(X)
knn_dists = knn_dists.astype(np.float32); knn_indices = knn_indices.astype(np.int64)


def reference_sigma_rho(dists, k, local_connectivity=1.0):
    n = dists.shape[0]; target = np.log2(k)
    sig, rho = np.zeros(n), np.zeros(n)
    for i in range(n):
        d = dists[i].astype(np.float64); nz = d[d > 0]
        idx = int(np.floor(local_connectivity)); interp = local_connectivity - idx
        if idx > 0:
            rho[i] = nz[idx - 1] + (interp * (nz[idx] - nz[idx - 1]) if interp > 1e-5 else 0.0)
        else:
            rho[i] = interp * nz[0]
        dj = d[1:]
        f = lambda s: np.sum(np.exp(-np.maximum(dj - rho[i], 0.0) / s)) - target
        s = brentq(f, 1e-12, 1e12, xtol=1e-14, rtol=1e-12)
        sig[i] = max(s, 1e-3 * d.mean())
    return sig, rho

print("\n1. smooth_knn_dist vs brentq on the paper's equation (800 points, k=15)")
for lc in (1.0, 1.5):
    s0, r0 = smooth_knn_dist(knn_dists, float(k), local_connectivity=lc)
    s1, r1 = reference_sigma_rho(knn_dists, k, lc)
    rows, cols, vals, _ = compute_membership_strengths(knn_indices, knn_dists, s0, r0, False)
    rowsum = vals.reshape(-1, k)[:, 1:].sum(1)
    print(f"  local_connectivity={lc}: max |sigma rel diff| = {np.max(np.abs(s0 - s1) / s1):.2e}, max |rho diff| = {np.abs(r0 - r1).max():.2e}, "
          f"kernel row sums in [{rowsum.min():.5f}, {rowsum.max():.5f}] (target log2(15) = {np.log2(15):.5f})")
print(f"  sigma floor active (sigma == 1e-3 * row mean) in {np.sum(np.isclose(s0, 1e-3 * knn_dists.mean(1)))} rows")

print("\n2. fuzzy_simplicial_set symmetrisation")
A, s, r = fuzzy_simplicial_set(X, k, None, "euclidean", knn_indices=knn_indices, knn_dists=knn_dists, apply_set_operations=False)
A = A.tocsr().toarray().astype(np.float64)
for ratio in (1.0, 0.5, 0.0):
    G, _, _ = fuzzy_simplicial_set(X, k, None, "euclidean", knn_indices=knn_indices, knn_dists=knn_dists, set_op_mix_ratio=ratio)
    G = G.tocsr()
    asym = abs(G - G.T).max()
    Gd = G.toarray()
    ref = ratio * (A + A.T - A * A.T) + (1 - ratio) * (A * A.T)
    print(f"  set_op_mix_ratio={ratio}: max |G - G.T| = {asym:.1e}, min {Gd.min():.3f}, max {Gd.max():.6f}, max |G - numpy reference| = {np.abs(Gd - ref).max():.2e}, nnz {G.nnz}")
print(f"  unsymmetrised A: diagonal all zero: {np.all(np.diag(A) == 0)}, max entry {A.max():.4f}, entries == 1 per row: {np.bincount((A == 1.0).sum(1)).tolist()} (count of rows with 0,1,2,... ones)")

print("\n3. find_ab_params")
def curve(x, a, b): return 1.0 / (1.0 + a * x ** (2 * b))
for spread, min_dist in ((1.0, 0.1), (1.0, 0.0), (1.0, 0.5), (1.0, 0.99), (3.0, 0.1), (0.5, 0.25)):
    a, b = find_ab_params(spread, min_dist)
    xv = np.linspace(0, spread * 3, 300); yv = np.where(xv < min_dist, 1.0, np.exp(-(xv - min_dist) / spread))
    res = least_squares(lambda p: curve(xv, *p) - yv, x0=[1.0, 1.0], xtol=1e-14, ftol=1e-14)
    print(f"  spread={spread} min_dist={min_dist}: a={a:.4f} b={b:.4f}; independent least squares a={res.x[0]:.4f} b={res.x[1]:.4f}; residual rms {np.sqrt(np.mean((curve(xv, a, b) - yv) ** 2)):.4f}")

print("\n4. spectral_layout vs dense eigh of the normalized Laplacian")
X1 = rng.normal(0, 1, (600, 6)).astype(np.float32)          # one Gaussian: connected kNN graph
kd1, ki1 = NearestNeighbors(n_neighbors=k).fit(X1).kneighbors(X1)
G, _, _ = fuzzy_simplicial_set(X1, k, None, "euclidean", knn_indices=ki1.astype(np.int64), knn_dists=kd1.astype(np.float32))
G = G.tocsr()
ncomp = scipy.sparse.csgraph.connected_components(G)[0]
print(f"  graph connected components: {ncomp}")
if ncomp == 1:
    emb = spectral_layout(X1, G, 2, np.random.RandomState(0))
    W = G.toarray().astype(np.float64); dg = W.sum(0); Dm = np.diag(1 / np.sqrt(dg))
    L = np.eye(W.shape[0]) - Dm @ W @ Dm
    w, V = scipy.linalg.eigh(L)
    ref = V[:, 1:3]
    # compare subspaces: principal angles
    Q1, _ = np.linalg.qr(emb); Q2, _ = np.linalg.qr(ref)
    sv = np.linalg.svd(Q1.T @ Q2, compute_uv=False)
    print(f"  eigenvalues (dense) 0..3: {np.array2string(w[:4], precision=6)}; principal angles between umap and dense 2-d eigenspaces: {np.degrees(np.arccos(np.clip(sv, -1, 1)))} deg")
    print(f"  Rayleigh quotients of umap's vectors: {[float(v @ L @ v / (v @ v)) for v in emb.T]}")
# two-component graph (the original 2-cluster data): multi_component_layout places each
# component around a meta-position
G2, _, _ = fuzzy_simplicial_set(X, k, None, "euclidean", knn_indices=knn_indices, knn_dists=knn_dists)
G2 = G2.tocsr(); nc2, lab2 = scipy.sparse.csgraph.connected_components(G2)
emb2 = spectral_layout(X, G2, 2, np.random.RandomState(0))
print(f"  2-cluster graph: {nc2} components; layout finite: {np.isfinite(emb2).all()}; component centroids: {np.array2string(np.array([emb2[lab2 == c].mean(0) for c in range(nc2)]), precision=3)}")

print("\n5. metric='euclidean' vs metric='precomputed' (exact small-data path)")
m1 = umap.UMAP(n_neighbors=k, random_state=0).fit(X)
m2 = umap.UMAP(n_neighbors=k, metric="precomputed", random_state=0).fit(cdist(X, X).astype(np.float32))
print(f"  max |graph_ difference| = {abs(m1.graph_ - m2.graph_).max():.2e}; max |sigma diff| = {np.abs(m1._sigmas - m2._sigmas).max():.2e}; max |rho diff| = {np.abs(m1._rhos - m2._rhos).max():.2e}")
G3, _, _ = fuzzy_simplicial_set(X, k, None, "euclidean", knn_indices=knn_indices, knn_dists=knn_dists)
print(f"  vs fuzzy_simplicial_set on sklearn exact kNN: max |graph_ difference| = {abs(m1.graph_ - G3.tocsr()).max():.2e}")

print("\n6. nearest_neighbors: precomputed path (fast_knn_indices) vs sklearn")
from umap.umap_ import nearest_neighbors
ki, kd, _ = nearest_neighbors(cdist(X, X).astype(np.float32), k, "precomputed", {}, False, None)
print(f"  indices identical: {np.array_equal(ki, knn_indices)}; max |dist diff| = {np.abs(kd - knn_dists).max():.2e}; column 0 is self: {np.all(ki[:, 0] == np.arange(X.shape[0]))}")
