#!/usr/bin/env python3
"""Sparse vs dense: (1) the numba sparse metrics in umap/sparse.py vs the dense metrics in
umap/distances.py vs scipy cdist on the same vectors; (2) UMAP.fit on a CSR matrix vs the
same matrix dense, exact path (n < 4096) and pynndescent path (n >= 4096), graph_ compared.
"""
import warnings
import numpy as np
import scipy.sparse
from scipy.spatial.distance import cdist
import umap
from umap import distances as dist, sparse as sp

warnings.simplefilter("ignore")
print("umap-learn", umap.__version__)
rng = np.random.default_rng(5)
n, p = 120, 60
Xd = rng.normal(0, 1, (n, p)).astype(np.float32)
Xd[rng.random((n, p)) < 0.6] = 0.0
Xd[:5] = 0.0                                       # all-zero rows
Xd[5:8] = Xd[8:11]                                 # duplicate rows
Xs = scipy.sparse.csr_matrix(Xd); Xs.sort_indices()
print("\n1. metrics on 120 x 60 vectors, 60 % zeros, all-zero rows and duplicates included (reported: max |diff| over all pairs)")
def dense_pd(f, **kw): return np.array([[f(Xd[i], Xd[j], **kw) for j in range(n)] for i in range(n)])
def sparse_pd(f, **kw):
    out = np.zeros((n, n))
    for i in range(n):
        i0, i1 = Xs.indptr[i], Xs.indptr[i + 1]
        for j in range(n):
            j0, j1 = Xs.indptr[j], Xs.indptr[j + 1]
            out[i, j] = f(Xs.indices[i0:i1], Xs.data[i0:i1], Xs.indices[j0:j1], Xs.data[j0:j1], **kw)
    return out
for name, dfun, sfun, skw, scipy_name in (
    ("euclidean", dist.euclidean, sp.sparse_euclidean, {}, "euclidean"),
    ("manhattan", dist.manhattan, sp.sparse_manhattan, {}, "cityblock"),
    ("cosine", dist.cosine, sp.sparse_cosine, {}, "cosine"),
    ("correlation", dist.correlation, sp.sparse_correlation, {"n_features": p}, "correlation"),
):
    D = dense_pd(dfun); S = sparse_pd(sfun, **skw)
    with np.errstate(all="ignore"):
        R = cdist(Xd.astype(np.float64), Xd.astype(np.float64), metric=scipy_name)
    finite = np.isfinite(R)
    print(f"  {name:12s} dense vs sparse: {np.abs(D - S).max():.2e};  dense vs scipy (finite pairs, {finite.sum()} of {n * n}): {np.abs(D - R)[finite].max():.2e};  sparse vs scipy: {np.abs(S - R)[finite].max():.2e}")
    if not finite.all():
        bad = ~finite
        print(f"    scipy is nan on {bad.sum()} pairs (zero / constant rows); there dense returns {np.unique(D[bad])}, sparse returns {np.unique(S[bad])}")

print("\n2. UMAP.fit dense vs CSR, graph_ compared")
for N, label in ((1500, "exact path (n < 4096)"), (5000, "pynndescent path (n >= 4096), random_state=0")):
    Y = rng.normal(0, 1, (N, 40)).astype(np.float32); Y[rng.random(Y.shape) < 0.7] = 0.0
    Ys = scipy.sparse.csr_matrix(Y)
    for metric in ("euclidean", "cosine"):
        g1 = umap.UMAP(n_neighbors=15, metric=metric, random_state=0, transform_mode="graph").fit(Y).graph_.tocsr()
        g2 = umap.UMAP(n_neighbors=15, metric=metric, random_state=0, transform_mode="graph").fit(Ys).graph_.tocsr()
        diff = abs(g1 - g2)
        same_support = ((g1 > 0) != (g2 > 0)).nnz
        print(f"  {label:48s} {metric:10s}: nnz {g1.nnz} vs {g2.nnz}, edges present in one only: {same_support}, max |weight diff| = {diff.max():.2e}, mean |diff| over union = {diff.sum() / max(diff.nnz, 1):.2e}")
