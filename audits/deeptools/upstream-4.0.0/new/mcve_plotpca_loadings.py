#!/usr/bin/env python3
"""plotPCA 4.0.0 (default, untransposed layout): the table and plot hold the
PC scores of the first rows (bins), not the loadings of the samples.

A synthetic multiBamSummary-style matrix (4,000 bins x 6 samples, numpy) with
two groups of three samples: 'a' samples share one set of 30 % up/down bins,
'b' samples another, so one of the leading components must separate the groups.  plotPCA is run with
--outFileNameData and the 'Component 1' row (one value per sample, per the
header and the help: "the loading per-sample and PC") is compared with the
loadings of a PCA done in numpy on the same 500 most variable rows.
Loadings are the rows of V^T, so each Component row must have unit norm and
the rows must be orthogonal; the 4.0.0 rows are (U*S)[i, :] instead.
"""
import os
import subprocess
import sys
import tempfile
import numpy as np

BIN = os.path.dirname(sys.executable)
d = tempfile.mkdtemp()
rng = np.random.default_rng(3)
nb, ns = 4000, 6
labels = ["a1", "a2", "a3", "b1", "b2", "b3"]
base = rng.gamma(2.0, 50.0, nb)
eff_a = np.where(rng.random(nb) < 0.3, rng.choice([0.2, 5.0], nb), 1.0)
eff_b = np.where(rng.random(nb) < 0.3, rng.choice([0.2, 5.0], nb), 1.0)
mat = np.zeros((nb, ns))
for j in range(ns):
    mat[:, j] = rng.poisson(base * (eff_a if j < 3 else eff_b))
npz = os.path.join(d, "counts.npz")
with open(npz, "wb") as fh:
    np.savez_compressed(fh, matrix=mat, labels=labels)

tab = os.path.join(d, "pca.tab")
subprocess.run([os.path.join(BIN, "plotPCA"), "-in", npz, "--outFileNameData", tab, "-o", os.path.join(d, "pca.png")], check=True)
rows = [l.rstrip("\n").split("\t") for l in open(tab) if not l.startswith("Component")]
W = np.array([[float(x) for x in r[1:1 + ns]] for r in rows])

# the same PCA in numpy: 500 most variable rows, columns standardised, SVD
ntop = 500
m = mat[np.argpartition(mat.var(axis=1), -ntop)[-ntop:]]
m = (m - m.mean(0)) / m.std(0)
U, S, Vt = np.linalg.svd(m - m.mean(0), full_matrices=False)
sg = np.sign(U[np.argmax(np.abs(U), axis=0), range(U.shape[1])])   # sklearn's svd_flip, as plotPCA does
U *= sg
Vt *= sg[:, None]
print(open(tab).readline().strip())
print("plotPCA 'Component 1' row:                        ", np.round(W[0], 3))
print("loadings of the six samples on PC1 (numpy V^T[0]):", np.round(Vt[0], 3), "(sign arbitrary)")
print("scores of the first selected bin (numpy (U*S)[0]):", np.round((U * S)[0], 3))
norms = np.linalg.norm(W, axis=1)
print("norm of each Component row:", np.round(norms, 3), "(loadings: all 1)")
same_as_loadings = all(np.allclose(W[i], Vt[i], atol=1e-6) or np.allclose(W[i], -Vt[i], atol=1e-6) for i in range(ns))
same_as_bin_scores = all(np.allclose(W[i], (U * S)[i], atol=1e-6) for i in range(ns))
print("table rows are the sample loadings V^T:", same_as_loadings)
print("table rows are the first six bins' scores (U*S):", same_as_bin_scores)


def separates(row):   # all a-samples on one side of 0, all b-samples on the other
    return (row[:3] > 0).all() and (row[3:] < 0).all() or (row[:3] < 0).all() and (row[3:] > 0).all()


k = [i for i in range(ns) if separates(Vt[i])]
print("components whose loadings separate the a and b groups (numpy):", [i + 1 for i in k])
print("Component rows of the plotPCA table that separate them:      ", [i + 1 for i in range(ns) if separates(W[i])])
assert same_as_loadings, "plotPCA's default table does not contain the per-sample loadings"
