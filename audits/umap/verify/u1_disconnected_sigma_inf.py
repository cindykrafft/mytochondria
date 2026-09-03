#!/usr/bin/env python3
"""U1: smooth_knn_dist returns sigma = inf for every point that has at least one
disconnected neighbour, so all of that point's remaining edges get membership 1.0.

umap/umap_.py, smooth_knn_dist: after the binary search the MIN_K_DIST_SCALE floor is

    if rho[i] > 0.0:
        mean_ith_distances = np.mean(ith_distances)
        if result[i] < MIN_K_DIST_SCALE * mean_ith_distances:
            result[i] = MIN_K_DIST_SCALE * mean_ith_distances
    else:
        if result[i] < MIN_K_DIST_SCALE * mean_distances:   # mean_distances = np.mean(distances)
            result[i] = MIN_K_DIST_SCALE * mean_distances

UMAP.fit marks every neighbour at distance >= disconnection_distance with
knn_dists = np.inf (and knn_indices = -1) before calling fuzzy_simplicial_set, and
nearest_neighbors(metric="precomputed") keeps inf entries.  np.mean of a row that
contains inf is inf, so the floor "1e-3 * mean" is inf, the comparison
result < inf is always true, and sigma becomes inf.  compute_membership_strengths then
evaluates exp(-(d - rho) / inf) = 1.0 for every remaining finite neighbour.  Because
mean_distances (the global mean) is inf as soon as any row has an inf, every row with
rho == 0 (all neighbours identical) also gets sigma = inf.

Reference: sigma from the paper's definition, sum_{j>=1, finite} exp(-max(0, d_j - rho)/sigma)
= log2(k), solved with scipy.optimize.brentq, and the same floor computed on the finite
distances only.

Part A  smooth_knn_dist on a constructed distance array (8-point cluster whose 15-NN lists
        contain 7 finite and 7 disconnected neighbours), vs the reference.
Part B  UMAP.fit with disconnection_distance on the same data: exact path (n < 4096),
        pynndescent path (force_approximation_algorithm=True), precomputed path.
Part C  default settings, metric="jaccard" on sparse binary data (disconnection_distance
        defaults to 1 for jaccard, and disjoint rows are at distance exactly 1).
Part D  the same array through a copy of smooth_knn_dist whose floor uses the finite
        distances (the proposed fix), vs the reference.
"""
import warnings
import numpy as np
import numba
import scipy.sparse
from scipy.optimize import brentq
from sklearn.neighbors import NearestNeighbors
import umap
from umap.umap_ import smooth_knn_dist, compute_membership_strengths, fuzzy_simplicial_set

warnings.simplefilter("ignore")
print("umap-learn", umap.__version__, umap.__file__)
SMOOTH_K_TOLERANCE, MIN_K_DIST_SCALE = 1e-5, 1e-3


def reference_sigma_rho(dists, k, local_connectivity=1.0):
    """Paper definition of rho and sigma, floor on the finite distances."""
    n = dists.shape[0]
    target = np.log2(k)
    mean_all = dists[np.isfinite(dists)].mean()
    sig, rho = np.zeros(n), np.zeros(n)
    for i in range(n):
        d = dists[i].astype(np.float64)
        fin = d[np.isfinite(d)]
        nz = fin[fin > 0]
        if nz.size >= local_connectivity:
            idx = int(np.floor(local_connectivity)); interp = local_connectivity - idx
            if idx > 0:
                rho[i] = nz[idx - 1] + (interp * (nz[idx] - nz[idx - 1]) if interp > SMOOTH_K_TOLERANCE else 0.0)
            else:
                rho[i] = interp * nz[0]
        elif nz.size > 0:
            rho[i] = nz.max()
        dj = d[1:]; dj = dj[np.isfinite(dj)]
        f = lambda s: np.sum(np.exp(-np.maximum(dj - rho[i], 0.0) / s)) - target
        if f(1e-12) > 0:      # more than log2(k) neighbours within rho: sigma -> 0
            s = 0.0
        elif f(1e12) < 0:     # fewer finite neighbours than log2(k): sigma -> inf
            s = np.inf
        else:
            s = brentq(f, 1e-12, 1e12, xtol=1e-14, rtol=1e-12)
        floor = MIN_K_DIST_SCALE * (fin.mean() if rho[i] > 0 else mean_all)
        sig[i] = max(s, floor)
    return sig, rho


@numba.njit(parallel=True)
def smooth_knn_dist_fixed(distances, k, n_iter=64, local_connectivity=1.0, bandwidth=1.0):
    """smooth_knn_dist with disconnected (inf) neighbours excluded from rho and from the
    MIN_K_DIST_SCALE floor.  Everything else identical to the shipped function."""
    target = np.log2(k) * bandwidth
    rho = np.zeros(distances.shape[0], dtype=np.float32)
    result = np.zeros(distances.shape[0], dtype=np.float32)
    flat_distances = distances.ravel()
    mean_distances = np.mean(flat_distances[np.isfinite(flat_distances)])
    for i in numba.prange(distances.shape[0]):
        lo = 0.0
        hi = np.finfo(np.float32).max
        mid = 1.0
        ith_distances = distances[i]
        finite_dists = ith_distances[np.isfinite(ith_distances)]
        non_zero_dists = finite_dists[finite_dists > 0.0]
        if non_zero_dists.shape[0] >= local_connectivity:
            index = int(np.floor(local_connectivity))
            interpolation = local_connectivity - index
            if index > 0:
                rho[i] = non_zero_dists[index - 1]
                if interpolation > SMOOTH_K_TOLERANCE:
                    rho[i] += interpolation * (non_zero_dists[index] - non_zero_dists[index - 1])
            else:
                rho[i] = interpolation * non_zero_dists[0]
        elif non_zero_dists.shape[0] > 0:
            rho[i] = np.max(non_zero_dists)
        for n in range(n_iter):
            psum = 0.0
            for j in range(1, distances.shape[1]):
                d = distances[i, j] - rho[i]
                if d > 0:
                    psum += np.exp(-(d / mid))
                else:
                    psum += 1.0
            if np.fabs(psum - target) < SMOOTH_K_TOLERANCE:
                break
            if psum > target:
                hi = mid
                mid = (lo + hi) / 2.0
            else:
                lo = mid
                if hi >= np.finfo(np.float32).max:
                    mid *= 2
                else:
                    mid = (lo + hi) / 2.0
        result[i] = mid
        if rho[i] > 0.0:
            mean_ith_distances = np.mean(finite_dists)
            if result[i] < MIN_K_DIST_SCALE * mean_ith_distances:
                result[i] = MIN_K_DIST_SCALE * mean_ith_distances
        else:
            if result[i] < MIN_K_DIST_SCALE * mean_distances:
                result[i] = MIN_K_DIST_SCALE * mean_distances
    return result, rho


# ------------------------------------------------------------------ data
rng = np.random.default_rng(0)
k = 15
small = rng.normal(0, 0.3, (8, 5)).astype(np.float32)            # 8-point cluster at the origin
big = (rng.normal(0, 1.0, (300, 5)) + 10.0).astype(np.float32)    # 300 points ~17 away
X = np.vstack([small, big])
nn = NearestNeighbors(n_neighbors=k).fit(X)
knn_dists, knn_indices = nn.kneighbors(X)                         # column 0 is self (distance 0)
knn_dists = knn_dists.astype(np.float32); knn_indices = knn_indices.astype(np.int64)
D_CUT = 5.0
cut = knn_dists >= D_CUT
print(f"\ndata: 8-point cluster + 300-point cluster, k={k}; disconnection_distance={D_CUT}")
print(f"  rows with at least one disconnected neighbour: {cut.any(1).sum()} (the 8 cluster points)")
print(f"  finite neighbours per such row (excluding self): {(~cut[:8]).sum(1) - 1}")

# ------------------------------------------------------------------ Part A
print("\nPART A  smooth_knn_dist on the distance array with inf for disconnected neighbours")
d_inf = knn_dists.copy(); d_inf[cut] = np.inf
idx_inf = knn_indices.copy(); idx_inf[cut] = -1
sig_ship, rho_ship = smooth_knn_dist(d_inf, float(k))
sig_ref, rho_ref = reference_sigma_rho(d_inf, k)
print("  point  rho(ship)  rho(ref)   sigma(shipped)  sigma(reference)")
for i in range(8):
    print(f"  {i:5d}  {rho_ship[i]:9.4f}  {rho_ref[i]:8.4f}   {sig_ship[i]:>14}  {sig_ref[i]:16.5f}")
print(f"  rows with sigma == inf: shipped {np.isinf(sig_ship).sum()}, reference {np.isinf(sig_ref).sum()}")
ok = ~np.isinf(sig_ship)
print(f"  rows without a disconnected neighbour: max |sigma shipped - reference| = {np.abs(sig_ship[ok] - sig_ref[ok]).max():.2e}, max |rho diff| = {np.abs(rho_ship - rho_ref).max():.2e}")
rows, cols, vals, _ = compute_membership_strengths(idx_inf, d_inf, sig_ship, rho_ship, False)
vals = vals.reshape(-1, k)
_, _, vals_ref, _ = compute_membership_strengths(idx_inf, d_inf, sig_ref.astype(np.float32), rho_ref.astype(np.float32), False)
vals_ref = vals_ref.reshape(-1, k)
print("  membership strengths of point 0 to its finite neighbours (columns 1..7):")
print("    shipped  ", np.array2string(vals[0, 1:8], precision=4))
print("    reference", np.array2string(vals_ref[0, 1:8], precision=4))
print(f"  cluster rows: edges with weight exactly 1.0 -> shipped {(vals[:8, 1:] == 1.0).sum()} of {(~cut[:8, 1:]).sum()} finite edges, reference {(vals_ref[:8, 1:] == 1.0).sum()}")
print(f"  reference row sums of exp(-(d-rho)/sigma) over finite non-self neighbours (target log2(15) = {np.log2(15):.4f}): {np.array2string(vals_ref[:8, 1:].sum(1), precision=3)}")

# ------------------------------------------------------------------ Part B
print("\nPART B  UMAP.fit(disconnection_distance=5) on the same data")
def report(label, model):
    s = model._sigmas
    g = model.graph_.tocsr()
    sub = g[:8].toarray()
    print(f"  {label:58s} sigma==inf rows: {np.isinf(s).sum():3d};  cluster rows: {(sub == 1.0).sum():3d} edges of weight 1.0 among {(sub > 0).sum():3d} nonzero")
report("exact path (n < 4096)", umap.UMAP(n_neighbors=k, disconnection_distance=D_CUT, random_state=0).fit(X))
report("pynndescent path (force_approximation_algorithm=True)", umap.UMAP(n_neighbors=k, disconnection_distance=D_CUT, random_state=0, force_approximation_algorithm=True).fit(X))
from scipy.spatial.distance import cdist
dmat = cdist(X, X).astype(np.float32)
report("metric='precomputed', dense matrix, disconnection_distance", umap.UMAP(n_neighbors=k, metric="precomputed", disconnection_distance=D_CUT, random_state=0).fit(dmat))
dmat_inf = dmat.copy(); dmat_inf[dmat_inf >= D_CUT] = np.inf
# inf entries in a precomputed matrix (the documented way to disconnect pairs; the
# n >= 4096 precomputed path keeps them, see nearest_neighbors).  Needs the finite check
# switched off, whose keyword differs by version; 0.5.3 has none and is skipped.
m_inf = None
for kw in ({"ensure_all_finite": False}, {"force_all_finite": False}):
    try:
        m_inf = umap.UMAP(n_neighbors=k, metric="precomputed", random_state=0, force_approximation_algorithm=True).fit(dmat_inf, **kw)
        break
    except TypeError:
        continue
if m_inf is not None:
    report("metric='precomputed', inf entries, nearest_neighbors path", m_inf)
else:
    print("  metric='precomputed' with inf entries: fit() has no finite-check argument in this version; skipped")
report("control: no disconnection", umap.UMAP(n_neighbors=k, random_state=0).fit(X))
# transform(): indices of pruned neighbours are set to -1 but their distances stay finite, so
# the floor is finite there; the pruned neighbours still enter the sigma sum (by reading).
mt = umap.UMAP(n_neighbors=k, disconnection_distance=D_CUT, random_state=0, transform_mode="graph").fit(X)
Tg = mt.transform(X[:8]).tocsr()
print(f"  transform(X[:8]) graph rows (bipartite): {(Tg.data == 1.0).sum()} of {Tg.nnz} nonzero entries equal 1.0 (self edges: 8)")

# ------------------------------------------------------------------ Part C
print("\nPART C  default settings, metric='jaccard' on sparse binary data (disconnection_distance defaults to 1;")
print("        rows sharing no feature are at distance exactly 1 and are pruned)")
for n_rows, n_feat, density in ((400, 40, 0.06), (1000, 600, 0.005)):
    B = (rng.random((n_rows, n_feat)) < density).astype(np.float32)
    B[B.sum(1) == 0, 0] = 1.0
    m = umap.UMAP(n_neighbors=k, metric="jaccard", random_state=0, force_approximation_algorithm=True).fit(B)
    s = m._sigmas
    kd = m._knn_dists
    n_finite = np.isfinite(kd).sum(1) - 1                      # finite non-self neighbours
    genuinely_unbounded = n_finite < np.log2(k)                 # no sigma satisfies the definition
    wrongly_inf = np.isinf(s) & ~genuinely_unbounded
    g = m.graph_.tocsr()
    sub = g[wrongly_inf].toarray() if wrongly_inf.any() else np.zeros((0, n_rows))
    print(f"  {n_rows} x {n_feat} binary, density {density}: rows with a pruned neighbour {(np.isinf(kd).any(1)).sum():4d}; sigma == inf {np.isinf(s).sum():4d}; "
          f"of which fewer than log2(k) finite neighbours (unbounded by definition) {(np.isinf(s) & genuinely_unbounded).sum():4d}, wrongly inf {wrongly_inf.sum():4d}; "
          f"in the wrongly-inf rows {(sub == 1.0).sum()} of {(sub > 0).sum()} graph entries equal 1.0")

# ------------------------------------------------------------------ Part D
print("\nPART D  smooth_knn_dist with the floor computed on finite distances (proposed fix), Part A array")
sig_fix, rho_fix = smooth_knn_dist_fixed(d_inf, float(k))
print(f"  rows with sigma == inf: {np.isinf(sig_fix).sum()}")
print(f"  max |sigma fixed - reference| = {np.abs(sig_fix - sig_ref).max():.2e} (all rows), max |rho diff| = {np.abs(rho_fix - rho_ref).max():.2e}")
d_fin = knn_dists.copy()
sig_a, rho_a = smooth_knn_dist(d_fin, float(k)); sig_b, rho_b = smooth_knn_dist_fixed(d_fin, float(k))
print(f"  without any inf, fixed vs shipped: max |sigma diff| = {np.abs(sig_a - sig_b).max():.2e}, max |rho diff| = {np.abs(rho_a - rho_b).max():.2e}")
