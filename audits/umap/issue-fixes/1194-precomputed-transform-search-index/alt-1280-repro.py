"""Reproduction for lmcinnes/umap#1280: transform() with unique=True indexes
self.embedding_ (n_original rows) with neighbour indices that refer to the
de-duplicated training data (n_unique rows).

Synthetic data made in the script: 4500 distinct 2-D points (so the
NN-descent search index path is used, the same one the issue reports) with
the first point repeated 300 extra times at the top of the array, so that
original row = unique row + 300 for every other point.  The query points are
the distinct training points plus a jitter of 1e-3, so each query's nearest
training row is known exactly.
"""
import numpy as np
import umap

rng = np.random.RandomState(0)
n_unique, n_dup = 4500, 300
uniq = rng.uniform(0, 100, size=(n_unique, 2)).astype(np.float32)
X = np.vstack([np.repeat(uniq[:1], n_dup, axis=0), uniq])  # 4800 rows
row_of_unique = np.arange(n_unique) + n_dup  # original row of unique row u (u>0)
row_of_unique[0] = 0

model = umap.UMAP(n_neighbors=10, unique=True, random_state=42, n_epochs=50).fit(X)
print("umap", umap.__version__, "| raw rows", model._raw_data.shape[0],
      "| embedding rows", model.embedding_.shape[0],
      "| search index rows", model._knn_search_index._raw_data.shape[0])

sel = rng.choice(np.arange(1, n_unique), 200, replace=False)
Q = uniq[sel] + rng.normal(scale=1e-3, size=(200, 2)).astype(np.float32)

# 1. transform_mode='graph': the strongest column of each query row should be
#    a row of the *training data* that is (almost) equal to the query.
model.transform_mode = "graph"
G = model.transform(Q).tocsr()
best_col = np.asarray(G.argmax(axis=1)).ravel()
d_best = np.linalg.norm(model._raw_data[best_col] - Q, axis=1)
print("graph: strongest column is a training row within 0.01 of the query:",
      f"{np.mean(d_best < 0.01):.0%}",
      "| median distance", f"{np.median(d_best):.3g}")

# 2. transform_mode='embedding': the embedded query should land next to the
#    embedding of its (jittered) training point.
model.transform_mode = "embedding"
E = model.transform(Q)
target = model.embedding_[row_of_unique[sel]]
d_emb = np.linalg.norm(E - target, axis=1)
spread = np.ptp(model.embedding_, axis=0).max()
print("embedding: median |transform(q) - embedding_[row of q]| =",
      f"{np.median(d_emb):.3g}", "| embedding extent", f"{spread:.3g}",
      "| within 1% of extent:", f"{np.mean(d_emb < 0.01 * spread):.0%}")
