import numpy as np
import umap

rng = np.random.RandomState(0)
X = np.vstack([rng.normal(0, 0.3, (8, 5)), rng.normal(10, 1, (300, 5))]).astype(np.float32)
# 8 points in a tight cluster, 300 points ~17 away: each cluster point's 15-NN list
# holds 7 cluster neighbours and 7 far points, which disconnection_distance prunes
model = umap.UMAP(n_neighbors=15, disconnection_distance=5.0, random_state=0).fit(X)
print("sigma of the 8 cluster points:", model._sigmas[:8])
row = model.graph_.tocsr()[0].toarray().ravel()
print("membership strengths of point 0 to its 7 kept neighbours:", row[row > 0])
assert np.all(np.isfinite(model._sigmas))  # expected: finite sigma, graded strengths
