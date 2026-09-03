"""Reproduction for lmcinnes/umap#1194: UMAP(metric="precomputed").transform()
raises NotImplementedError once the training set has >= 4096 rows.

Synthetic data made in the script: n points in 5-D, the full Euclidean
distance matrix as the training input, and the distances from 5 new points
to the training points as the transform input (the layout transform()
documents for the precomputed metric).
"""
import numpy as np
from sklearn.metrics import pairwise_distances
import umap

rng = np.random.RandomState(0)
new = rng.normal(size=(5, 5)).astype(np.float32)

for n in (4095, 4096):
    train = rng.normal(size=(n, 5)).astype(np.float32)
    D = pairwise_distances(train).astype(np.float32)
    model = umap.UMAP(metric="precomputed", n_neighbors=10, n_epochs=50,
                      random_state=42).fit(D)
    D_new = pairwise_distances(new, train).astype(np.float32)
    try:
        emb = model.transform(D_new)
        print(f"n={n}: transform OK, shape {emb.shape}, "
              f"finite={np.isfinite(emb).all()}")
    except Exception as e:
        print(f"n={n}: {type(e).__name__}: {e}")
