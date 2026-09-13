import warnings, numba
import numpy as np, scipy.sparse
import umap
from umap.spectral import spectral_layout, multi_component_layout, component_layout
from sklearn.utils import check_random_state
warnings.simplefilter("ignore")
rng = np.random.RandomState(0)
base = rng.normal(size=(1000, 50)).astype(np.float32)
X = np.vstack([base] + [base[:200]] * 4)
a = umap.UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric="cosine", random_state=42).fit(X)
g = a.graph_.tocoo().copy()
g.data[g.data < g.data.max() / 500.0] = 0.0
g.eliminate_zeros()
ncomp, labels = scipy.sparse.csgraph.connected_components(g)
print("pruned graph: nnz", g.nnz, "of", a.graph_.nnz, "| connected components:", ncomp, "| sizes:", np.bincount(labels)[:10], "...")
ncomp0, _ = scipy.sparse.csgraph.connected_components(a.graph_)
print("unpruned graph components:", ncomp0)
e1 = spectral_layout(X, g, 5, check_random_state(42), metric="cosine")
e2 = spectral_layout(X, g, 5, check_random_state(42), metric="cosine")
print("spectral_layout on pruned COO graph twice: identical", np.array_equal(e1, e2), float(np.abs(e1-e2).max()))
if ncomp > 1:
    for i in range(2):
        c = component_layout(X, ncomp, labels, 5, check_random_state(42), metric="cosine")
        print("component_layout call", i, "first row", c[0][:3])
    m1 = multi_component_layout(X, g, ncomp, labels, 5, check_random_state(42), metric="cosine")
    m2 = multi_component_layout(X, g, ncomp, labels, 5, check_random_state(42), metric="cosine")
    print("multi_component_layout twice: identical", np.array_equal(m1, m2), float(np.abs(m1-m2).max()))
    # which components are unstable?
    bad = [k for k in range(ncomp) if not np.array_equal(m1[labels == k], m2[labels == k])]
    print("components whose layout differs:", len(bad), "of", ncomp, "| sizes of those:", [int((labels == k).sum()) for k in bad][:10])
