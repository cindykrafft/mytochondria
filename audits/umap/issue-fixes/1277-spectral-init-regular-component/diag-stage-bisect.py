"""#1277 on the exact path: which stage diverges between two seeded fits on duplicated data?"""
import warnings
import numpy as np
import umap
from umap.umap_ import fuzzy_simplicial_set, find_ab_params, simplicial_set_embedding
from umap.spectral import spectral_layout
from sklearn.utils import check_random_state
warnings.simplefilter("always")
rng = np.random.RandomState(0)
base = rng.normal(size=(1000, 50)).astype(np.float32)
X = np.vstack([base] + [base[:200]] * 4)
def fit():
    return umap.UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric="cosine", random_state=42).fit(X)
with warnings.catch_warnings(record=True) as w:
    a = fit(); b = fit()
print("warnings during the two fits:", sorted(set(str(x.message)[:90] for x in w)))
ga, gb = a.graph_.tocsr(), b.graph_.tocsr()
print("graph_ identical:", (ga != gb).nnz == 0, "| sigmas identical:", np.array_equal(a._sigmas, b._sigmas), "| rhos identical:", np.array_equal(a._rhos, b._rhos))
print("embedding identical:", np.array_equal(a.embedding_, b.embedding_), "max|d|", float(np.abs(a.embedding_ - b.embedding_).max()))
# spectral init on the same graph, same seed, twice
inits = []
for i in range(3):
    with warnings.catch_warnings(record=True) as w2:
        inits.append(spectral_layout(X, ga, 5, check_random_state(42), metric="cosine"))
    print(f"spectral_layout call {i}: warnings {[str(x.message)[:60] for x in w2]}")
print("spectral init call0 vs call1 identical:", np.array_equal(inits[0], inits[1]), "max|d|", float(np.abs(inits[0] - inits[1]).max()),
      "| call1 vs call2:", np.array_equal(inits[1], inits[2]))
# full embedding step on the same graph with the same init, twice
a_, b_ = find_ab_params(1.0, 0.0)
embs = []
for i in range(2):
    e, _ = simplicial_set_embedding(X, ga, 5, 1.0, a_, b_, 1.0, 5, None, inits[0].copy(), check_random_state(42), "cosine", {}, False, {}, False, verbose=False)
    embs.append(e)
print("simplicial_set_embedding with a fixed array init, twice: identical:", np.array_equal(embs[0], embs[1]), "max|d|", float(np.abs(embs[0]-embs[1]).max()))
