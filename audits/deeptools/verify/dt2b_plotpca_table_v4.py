#!/usr/bin/env python3
"""DT2 follow-up on 4.0.0: what does the re-implemented plotPCA write?

correlation.Correlation.plot_pca (4.0.0) standardises the (ntop rows x samples)
matrix, runs an SVD and sets Wt = U * S -- the PC scores of the *rows* (the
selected bins), shape (rows, components). plotPCA then writes row i of Wt as
"Component i" under the sample-name columns and plots Wt[PC1-1, :] against
Wt[PC2-1, :], i.e. the first two selected bins' scores across components. In
3.5.6 the table held Vt, the samples' loadings on each component. This script
replicates the 4.0.0 arithmetic in numpy and checks which of the two the table
contains, for the default --ntop (500) and --ntop 0.
"""
import os
import numpy as np
from scipy.linalg import svd
import _synth as S

print(S.version())
rng = np.random.default_rng(11)
d = S.tmpdir()
nb, ns = 4000, 4
base = rng.gamma(2.0, 50.0, nb)
depth = np.array([1.0, 1.4, 0.7, 2.2])
effect = np.where(rng.random(nb) < 0.1, rng.choice([0.3, 3.0], nb), 1.0)
mat = np.zeros((nb, ns))
for j in range(ns):
    mat[:, j] = rng.poisson(base * depth[j] * (effect if j >= 2 else 1.0))
npz = os.path.join(d, "counts.npz")
with open(npz, "wb") as fh:
    np.savez_compressed(fh, matrix=mat, labels=["s1", "s2", "s3", "s4"])


def table(extra):
    out = os.path.join(d, "pca.tab")
    S.run(["plotPCA", "-in", npz, "--outFileNameData", out] + extra)
    rows = [l.rstrip("\n").split("\t") for l in open(out) if not l.startswith("Component") and not l.startswith("#")]
    return np.array([[float(x) for x in r[1:1 + ns]] for r in rows]), np.array([float(r[-1]) for r in rows])


def replicate(ntop):
    m = mat.astype(float)
    rvs = m.var(axis=1)
    if ntop > 0 and m.shape[0] > ntop:
        m = m[np.argpartition(rvs, -ntop)[-ntop:]]
    m2 = (m - m.mean(0)) / m.std(0)
    X = m2 - m2.mean(0)
    U, Sv, Vt = svd(X, full_matrices=False)
    mac = np.argmax(np.abs(U), axis=0)
    sg = np.sign(U[mac, range(U.shape[1])])
    U *= sg
    Vt *= sg[:, None]
    return U * Sv, Vt, Sv ** 2 / (m.shape[0] - 1)


for ntop in [500, 0]:
    W, ev = table(["--ntop", str(ntop)])
    scores, Vt, e = replicate(ntop)
    rows_are_bin_scores = all(np.allclose(W[i], scores[i], atol=1e-6) for i in range(ns))
    rows_are_loadings = all(np.allclose(W[i], Vt[i], atol=1e-6) or np.allclose(W[i], -Vt[i], atol=1e-6) for i in range(ns))
    print("\n--ntop %d: eigenvalues in the table %s; replicated S^2/(n-1) %s" % (ntop, np.round(ev, 4), np.round(e, 4)))
    print("  table row i == (U*S)[i, :], the scores of the i-th selected bin across components: %s" % rows_are_bin_scores)
    print("  table row i == Vt[i, :], the samples' loadings on component i (3.5.6 semantics):     %s" % rows_are_loadings)
    print("  table 'Component 1' row: %s   loadings of the samples on PC1 would be: %s" % (np.round(W[0], 4), np.round(Vt[0], 4)))
W, ev = table(["--transpose"])
print("\n--transpose: table rows are each sample's projection on the components (Wt.T): first row %s" % np.round(W[0], 4))
