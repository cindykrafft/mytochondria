#!/usr/bin/env python3
"""Note: points with more than about log2(k) duplicates (or ties at the nearest distance)
make the paper's sigma equation unsolvable; smooth_knn_dist then drives sigma to the
MIN_K_DIST_SCALE floor and every non-identical neighbour beyond the nearest one gets a
membership strength near zero.

smooth_knn_dist excludes zero distances from rho (rho = nearest non-identical neighbour)
but counts every neighbour with d <= rho as 1.0 in the sum, so with m duplicates the sum is
at least m + 1 for any sigma; the target is log2(k) = 3.91 for k = 15.  When m + 1 exceeds
that the bisection halves sigma 64 times (2^-64) and the floor 1e-3 * mean(row) is what is
returned.  The `unique=True` option is the documented remedy ("If you have more duplicates
than you have n_neighbors ...").  This measures the effect for small numbers of duplicates.
"""
import warnings
import numpy as np
from sklearn.neighbors import NearestNeighbors
import umap
from umap.umap_ import smooth_knn_dist, compute_membership_strengths

warnings.simplefilter("ignore")
print("umap-learn", umap.__version__)
rng = np.random.default_rng(3)
k = 15
base = rng.normal(0, 1, (500, 8)).astype(np.float32)
print(f"500 Gaussian points in 8-d, k={k}, target log2(k) = {np.log2(k):.3f}; point 0 replicated m extra times (identical rows)")
print("  m   sigma(point 0)   floor(1e-3*mean)   kernel sum   weights to non-identical neighbours (sorted by distance)")
for m in (0, 1, 2, 3, 4, 6, 10):
    X = np.vstack([base] + [base[:1]] * m)
    kd, ki = NearestNeighbors(n_neighbors=k).fit(X).kneighbors(X)
    kd = kd.astype(np.float32); ki = ki.astype(np.int64)
    s, r = smooth_knn_dist(kd, float(k))
    _, _, vals, _ = compute_membership_strengths(ki, kd, s, r, False)
    v = vals.reshape(-1, k)[0]
    d0 = kd[0]
    nonid = (d0 > 0)
    w = v[nonid]
    order = np.argsort(d0[nonid])
    print(f"  {m:2d}   {s[0]:12.5f}   {1e-3 * kd[0].mean():14.5f}   {v[1:].sum():8.3f}      {np.array2string(w[order][:6], precision=3)}")
print("\nSame via UMAP.fit (exact path), graph_ row of point 0: number of neighbours with weight > 0.01")
for m in (0, 2, 4, 10):
    X = np.vstack([base] + [base[:1]] * m)
    for uniq in (False, True):
        mod = umap.UMAP(n_neighbors=k, random_state=0, unique=uniq).fit(X)
        row = mod.graph_.tocsr()[0].toarray().ravel()
        ident = np.zeros(X.shape[0], bool); ident[0] = True; ident[500:] = True
        ident = ident[:row.size]                     # unique=True: graph_ is over the 500 distinct rows
        print(f"  m={m:2d} unique={uniq!s:5}: weights > 0.01 to identical rows: {(row[ident] > 0.01).sum():2d}, to distinct rows: {(row[~ident] > 0.01).sum():2d}; sigma(point 0) = {mod._sigmas[0]:.5f}")
