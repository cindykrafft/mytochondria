Title: plotPCA (4.0.0 re-implementation): the default table and plot hold the PC scores of the first bins, not the loadings of the samples

<!-- deeptools/deepTools .github/ISSUE_TEMPLATE.md checklist -->

- [x] Search whether this issue (or a similar issue) has been solved before: no prior report found (nearest: #1215 "Normalization missing in multiBamSummary+plotPCA", which is about the input, not the output).
- [x] deepTools version: 4.0.0, `master` @ `4db9d816` ("4.0.0 cleanup (#1450)"), Python 3.12.3, numpy 2.5.2, scipy 1.18.1; not present in 3.5.6 (whose table held the loadings)
- [x] Full command producing the issue: `plotPCA -in counts.npz -o pca.png --outFileNameData pca.tab` (default options; script below builds `counts.npz`)
- [x] Output printed: see below

**What happens.** The re-implemented `Correlation.plot_pca` (`pydeeptools/deeptools/correlation.py`, lines 444–520) standardises the (`--ntop` rows × samples) matrix, runs `svd(X)` and sets `Wt = U * S` (line 507) for both layouts, transposing it only under `--transpose`. `U * S` are the PC scores of the *rows* of `X` — in the default layout, of the selected bins — with shape (rows, components). `plotPCA.py` (line 222) then writes row `i` of `Wt` as "Component i" under the sample-name columns, and `plot_pca` scatters `Wt[PC1-1, :]` against `Wt[PC2-1, :]` (line 543), one point per sample label. So the "Component 1" row is the first selected bin's scores across the components, the plotted point for sample `i` is (score of bin 1 on PC `i`, score of bin 2 on PC `i`), and the table rows have norms of 1.5–1.9 instead of 1. The help of plotPCA and `--outFileNameData` still say "the loadings for each sample in each principal component is plotted" / "the loading per-sample and PC" — those are the rows of `Vt`, which 3.5.6 wrote (`Wt = Vh`). `--transpose` is right (`(U * S).T` is each sample's projection). The existing image tests pass because the corrected plot is only 6.8 RMS from the golden PNG at a tolerance of 50, and the numeric tests deliberately avoid the coordinates ("not reproducible across platforms" — they are not, because they are bin scores whose bin selection is BLAS-dependent; the loadings on PC1 are).

**Minimal script** (4,000 bins × 6 samples, Poisson counts around a shared gamma baseline; the three `a` samples share one set of 30 % up/down bins, the three `b` samples another; the same PCA is done in numpy on the same 500 most variable rows):

```python
import os, subprocess, sys, tempfile
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

ntop = 500                                   # the same PCA in numpy
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
print("norm of each Component row:", np.round(np.linalg.norm(W, axis=1), 3), "(loadings: all 1)")
same_as_loadings = all(np.allclose(W[i], Vt[i], atol=1e-6) or np.allclose(W[i], -Vt[i], atol=1e-6) for i in range(ns))
print("table rows are the sample loadings V^T:", same_as_loadings)
print("table rows are the first six bins' scores (U*S):", all(np.allclose(W[i], (U * S)[i], atol=1e-6) for i in range(ns)))

def separates(row):   # all a-samples on one side of 0, all b-samples on the other
    return (row[:3] > 0).all() and (row[3:] < 0).all() or (row[:3] < 0).all() and (row[3:] > 0).all()

print("components whose loadings separate the a and b groups (numpy):", [i + 1 for i in range(ns) if separates(Vt[i])])
print("Component rows of the plotPCA table that separate them:      ", [i + 1 for i in range(ns) if separates(W[i])])
assert same_as_loadings, "plotPCA's default table does not contain the per-sample loadings"
```

**Output** (4.0.0 @ `4db9d816`):

```
Component	a1	a2	a3	b1	b2	b3	Eigenvalue
plotPCA 'Component 1' row:                         [-1.059 -1.086 -0.027 -0.131  0.031 -0.003]
loadings of the six samples on PC1 (numpy V^T[0]): [-0.408 -0.408 -0.409  0.408  0.409  0.408] (sign arbitrary)
scores of the first selected bin (numpy (U*S)[0]): [-1.059 -1.086 -0.027 -0.131  0.031 -0.003]
norm of each Component row: [1.523 1.509 1.509 1.489 1.491 1.85 ] (loadings: all 1)
table rows are the sample loadings V^T: False
table rows are the first six bins' scores (U*S): True
components whose loadings separate the a and b groups (numpy): [1]
Component rows of the plotPCA table that separate them:       []
AssertionError: plotPCA's default table does not contain the per-sample loadings
```

The two groups, which PC1 separates cleanly in the loadings (−0.41 ×3 / +0.41 ×3), are not separated by any row of the table, and the plot shows six points that are the first two bins' scores on PC1…PC6 — nothing about the samples. On the shipped `test_samples.npz` the golden `test_plotPCA_default.tsv` shows the same thing: "Component 1" is `-1.959, -0.060, 0.016, 0.361, -0.064, 0.013` where the loadings of the six samples on PC1 are `0.41 ± 0.01` each.

**Fix.** In the untransposed layout set `Wt = Vt` (the rows of `V^T`, shape components × samples), keep `Wt = (U * S).T` under `--transpose`, and drop the "not enough principal components to plot N samples" exit (each component row has one loading per sample, so `--ntop` below the sample count plots fine as long as the requested PCs exist — the other check). The eigenvalues, the variance fractions, the scree plot and `--transpose` are unchanged. The golden PNGs/TSVs under `test/test_plotPCA/` show the bin scores and need regenerating. A PR with the fix, a test that the default table rows are orthonormal and equal a numpy SVD's `V^T` on the same rows (fails on `4db9d816`), and the adjusted `--ntop` tests follows.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/deeptools)

---
_Generated by [Claude Code](https://claude.ai/code)_
