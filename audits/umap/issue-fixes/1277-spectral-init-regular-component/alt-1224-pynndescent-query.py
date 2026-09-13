"""#1224, pynndescent path: is the subset-vs-all difference in pynndescent's query() itself?"""
import warnings
import numpy as np
import umap
from sklearn.neighbors import NearestNeighbors
warnings.simplefilter("ignore")
rng = np.random.RandomState(0)
CENTRES = np.random.RandomState(123).normal(0, 6, size=(4, 20))  # shared by train and new data
def blobs(n, d=20, seed=0):
    r = np.random.RandomState(seed)
    lab = r.randint(0, 4, n)
    return (CENTRES[lab] + r.normal(size=(n, d))).astype(np.float32), lab
Xtr, ltr = blobs(5000, seed=1); Xnew, lnew = blobs(1200, seed=2)
sub = np.sort(rng.choice(1200, 600, replace=False))
m = umap.UMAP(n_neighbors=15, random_state=42).fit(Xtr)
idx = m._knn_search_index
print("index type", type(idx).__name__, "| angular", idx._angular_trees, "| n_jobs", idx.n_jobs)
exact_d, exact_i = NearestNeighbors(n_neighbors=15).fit(Xtr).kneighbors(Xnew)
def recall(I, rows):
    return np.mean([len(set(I[j]) & set(exact_i[r])) / 15 for j, r in enumerate(rows)])
I_all, D_all = idx.query(Xnew, 15, epsilon=0.12)
I_sub, D_sub = idx.query(Xnew[sub], 15, epsilon=0.12)
I_all2, D_all2 = idx.query(Xnew, 15, epsilon=0.12)
print("query(all) repeated identical:", np.array_equal(I_all, I_all2))
print("recall vs exact kNN: all", f"{recall(I_all, range(1200)):.3f}", "| subset", f"{recall(I_sub, sub):.3f}")
diff = np.where((I_all[sub] != I_sub).any(1))[0]
print("rows whose neighbour list differs between the two batches:", len(diff), "of", len(sub))
# wrong-blob neighbours: label of the query vs labels of returned neighbours
wrong_all = np.mean(ltr[I_all[sub]] != lnew[sub][:, None], axis=1)
wrong_sub = np.mean(ltr[I_sub] != lnew[sub][:, None], axis=1)
print("rows with >= half of neighbours in another blob: all[sub]", int((wrong_all >= 0.5).sum()), "| subset", int((wrong_sub >= 0.5).sum()))
print("rows with the -1 (not found) marker: all", int((I_all == -1).any(1).sum()), "| subset", int((I_sub == -1).any(1).sum()))
r = diff[:3]
for j in r:
    print(" row", sub[j], "all:", I_all[sub[j]][:6], np.round(D_all[sub[j]][:6], 2), "\n        sub:", I_sub[j][:6], np.round(D_sub[j][:6], 2), "\n      exact:", exact_i[sub[j]][:6], np.round(exact_d[sub[j]][:6], 2))
# single-row queries
one = np.array([idx.query(Xnew[i:i+1], 15, epsilon=0.12)[0][0] for i in sub[:50]])
print("single-row queries equal the all-batch rows:", int((one == I_all[sub[:50]]).all(1).sum()), "of 50; equal the subset-batch rows:", int((one == I_sub[:50]).all(1).sum()), "of 50")
