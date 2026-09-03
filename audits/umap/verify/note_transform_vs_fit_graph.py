#!/usr/bin/env python3
"""Note: UMAP.transform builds its fuzzy graph with local_connectivity - 1 (so rho = 0)
and with the query's nearest training point excluded from the sigma sum, so the membership
strengths it assigns to a training point are not the strengths that point has in graph_.

transform() short-circuits to embedding_/graph_ only when the *whole* training matrix is
passed (joblib hash equality); any subset takes the full path.  Measured with
transform_mode="graph" on a subset of the training data, against the unsymmetrised fit
membership matrix (fuzzy_simplicial_set(apply_set_operations=False)) and against graph_.
Also: transform determinism under transform_seed, and the hash short-circuit.
"""
import warnings
import numpy as np
from sklearn.neighbors import NearestNeighbors
import umap
from umap.umap_ import fuzzy_simplicial_set

warnings.simplefilter("ignore")
print("umap-learn", umap.__version__)
rng = np.random.default_rng(4)
k = 15
X = np.vstack([rng.normal(0, 1, (600, 10)), rng.normal(4, 1, (600, 10))]).astype(np.float32)
kd, ki = NearestNeighbors(n_neighbors=k).fit(X).kneighbors(X)
A, sig_fit, rho_fit = fuzzy_simplicial_set(X, k, None, "euclidean", knn_indices=ki.astype(np.int64), knn_dists=kd.astype(np.float32), apply_set_operations=False)
A = A.tocsr()
for mode_n, label in ((1200, "exact path (n < 4096)"),):
    model = umap.UMAP(n_neighbors=k, random_state=0, transform_mode="graph").fit(X)
    sub = X[:200]
    T = model.transform(sub).tocsr()          # (200, 1200) bipartite membership graph
    Af = A[:200]; Gf = model.graph_.tocsr()[:200]
    # self edges
    selfw = T[np.arange(200), np.arange(200)]
    print(f"\n{label}: transform(X[:200]) with transform_mode='graph'")
    print(f"  self-edge weight in the transform graph: min {selfw.min():.3f} max {selfw.max():.3f} (fit sets self to 0)")
    T2 = T.copy(); T2[np.arange(200), np.arange(200)] = 0; T2.eliminate_zeros()
    print(f"  nonzeros per row: transform {T2.nnz / 200:.1f}, fit unsymmetrised {Af.nnz / 200:.1f}, graph_ {Gf.nnz / 200:.1f}")
    common = (T2.multiply(Af) > 0)
    tv = np.asarray(T2[common].ravel()).ravel(); av = np.asarray(Af[common].ravel()).ravel()
    print(f"  on shared edges: max |transform - fit| = {np.abs(tv - av).max():.3f}, mean |diff| = {np.abs(tv - av).mean():.3f}, corr {np.corrcoef(tv, av)[0, 1]:.3f}")
    print(f"  fit: nearest non-identical neighbour has weight 1.0 in {(Af.max(1).toarray().ravel() == 1.0).sum()} of 200 rows; transform: {(T2.max(1).toarray().ravel() == 1.0).sum()} of 200 rows")
    print(f"  fit sigma (first 5): {np.array2string(sig_fit[:5], precision=4)}, rho: {np.array2string(rho_fit[:5], precision=4)}")
    # recompute what transform did: rho = 0, sigma from sum over columns 1.. of exp(-d/sigma)
    from umap.umap_ import smooth_knn_dist
    d_q = kd[:200].astype(np.float32)
    s_t, r_t = smooth_knn_dist(d_q, float(k), local_connectivity=0.0)
    print(f"  transform's smooth_knn_dist(local_connectivity=0): sigma (first 5): {np.array2string(s_t[:5], precision=4)}, rho: {np.array2string(r_t[:5], precision=4)}")
    # the whole-matrix short circuit
    full = model.transform(X)
    print(f"  transform(X) on the full training matrix returns graph_ itself: {full is model.graph_}")
    # determinism of the embedding transform
    m2 = umap.UMAP(n_neighbors=k, random_state=0).fit(X)
    e1 = m2.transform(X[:200]); e2 = m2.transform(X[:200])
    print(f"  embedding transform of the same subset twice (transform_seed=42): max |diff| = {np.abs(e1 - e2).max():.2e}")
    print(f"  transform(X[:200]) vs embedding_[:200]: max |diff| = {np.abs(e1 - m2.embedding_[:200]).max():.3f}, median {np.median(np.linalg.norm(e1 - m2.embedding_[:200], axis=1)):.3f} (embedding range {np.ptp(m2.embedding_, 0)})")
