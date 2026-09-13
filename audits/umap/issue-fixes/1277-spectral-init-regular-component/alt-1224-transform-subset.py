"""Probe for lmcinnes/umap#1224: transform(X_sub) vs transform(X_all)[sub].
Is the difference the transform SGD's randomness (expected) or a per-row dependence on the
batch (graph rows, init) ?  Exact path (n < 4096) and pynndescent path (n >= 4096)."""
import warnings
import numpy as np
import umap
warnings.simplefilter("ignore")
print("umap", umap.__version__)
rng = np.random.RandomState(0)

CENTRES = np.random.RandomState(123).normal(0, 6, size=(4, 20))  # shared by train and new data


def blobs(n, d=20, seed=0):
    r = np.random.RandomState(seed)
    lab = r.randint(0, 4, n)
    return (CENTRES[lab] + r.normal(size=(n, d))).astype(np.float32)

for label, n_train, n_new in [("exact path", 1500, 1200), ("pynndescent path", 5000, 1200)]:
    Xtr = blobs(n_train, seed=1); Xnew = blobs(n_new, seed=2)
    sub = np.sort(rng.choice(n_new, n_new // 2, replace=False))
    print(f"\n== {label}: train {n_train}, new {n_new}, subset {len(sub)} ==")
    m = umap.UMAP(n_neighbors=15, random_state=42).fit(Xtr)
    # 1. the bipartite graph rows
    m.transform_mode = "graph"
    G_all = m.transform(Xnew).tocsr()[sub]
    G_sub = m.transform(Xnew[sub]).tocsr()
    print("  graph rows subset vs all[subset] identical:", (G_all != G_sub).nnz == 0, "| max|d|", float(abs(G_all - G_sub).max()))
    # 2. the initial placement (before SGD)
    from umap.umap_ import init_graph_transform
    I_all = init_graph_transform(G_all, m.embedding_); I_sub = init_graph_transform(G_sub, m.embedding_)
    print("  init_graph_transform subset vs all[subset]: max|d|", float(np.abs(I_all - I_sub).max()))
    # 3. the embedding after SGD
    m.transform_mode = "embedding"
    E_all = m.transform(Xnew)[sub]
    E_sub = m.transform(Xnew[sub])
    d = np.linalg.norm(E_all - E_sub, axis=1)
    ext = np.ptp(m.embedding_, axis=0).max()
    print(f"  embedding subset vs all[subset]: max|d| {float(np.abs(E_all - E_sub).max()):.3f}  RMSE {float(np.sqrt((d**2).mean())):.3f}  (embedding extent {ext:.1f})")
    # 4. same subset, different transform_seed: the SGD noise floor
    m.transform_seed = 7
    E_sub2 = m.transform(Xnew[sub])
    d2 = np.linalg.norm(E_sub - E_sub2, axis=1)
    print(f"  same subset, transform_seed 42 vs 7: max|d| {float(np.abs(E_sub - E_sub2).max()):.3f}  RMSE {float(np.sqrt((d2**2).mean())):.3f}")
    # 5. same batch, same seed, repeated
    m.transform_seed = 42
    E_sub3 = m.transform(Xnew[sub])
    print("  same subset, same seed, repeated: identical:", np.array_equal(E_sub, E_sub3))
    # 6. batch-level normalisations: the edge threshold and epochs_per_sample use graph.data.max()
    m.transform_mode = "graph"
    print(f"  graph.data.max() (edge threshold / epochs_per_sample scale): all {float(m.transform(Xnew).data.max()):.4f}, subset {float(m.transform(Xnew[sub]).data.max()):.4f}")
