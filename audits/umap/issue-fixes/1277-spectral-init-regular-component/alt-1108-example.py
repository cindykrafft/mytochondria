import warnings, numpy as np, umap
warnings.simplefilter("ignore")
din = [[39.715797424316406, 5.328598499298096],[40.119140625, 6.10653018951416],[39.6290283203125, 6.134637832641602],[39.19687271118164, 5.85951566696167],[9.60939884185791, 9.586419105529785],[-6.015710353851318, -11.25406265258789],[9.012431144714355, 8.989534378051758],[9.283456802368164, 9.261088371276855],[-5.681527614593506, -10.919998168945312],[-5.479494571685791, -10.71765422821045]]
a = umap.UMAP(random_state=42, n_neighbors=2, n_components=2).fit(np.array(din))
b = umap.UMAP(random_state=42, n_neighbors=2, n_components=2).fit(np.array(din))
import scipy.sparse
nc, lab = scipy.sparse.csgraph.connected_components(a.graph_)
print("#1108 example: embeddings identical:", np.array_equal(a.embedding_, b.embedding_), "max|d|", float(np.abs(a.embedding_-b.embedding_).max()))
print("  graph components:", nc, "sizes", np.bincount(lab), "| graph weights:", np.unique(np.round(a.graph_.data, 6)))
deg = np.asarray(a.graph_.sum(axis=0)).ravel()
for c in range(nc):
    print(f"  component {c}: size {(lab==c).sum()}, degrees {np.round(deg[lab==c], 4)}")
