#!/usr/bin/env python3
"""DT2: plotPCA --log2 has no effect; --rowCenter has no effect unless the
matrix is not copied by the --ntop filter.

correlation.Correlation.plot_pca binds `m = self.matrix`, replaces `m` by a
row-selected copy when --ntop keeps fewer rows than the matrix has, then
applies --log2 and --rowCenter to `self.matrix` (rebinding it for log2,
in place for rowCenter) and runs the SVD on `m`.

A multiBamSummary-style .npz (4000 bins x 4 samples, Poisson counts with a
strong per-bin baseline so that log2 and row-centering change the answer) is
run through plotPCA --outFileNameData under several option sets. Reference
loadings are computed with numpy following the documented pipeline (top-N rows
by variance, optional log2(x + 0.01), optional row centering, column centering
and unit variance with ddof=1, SVD). Loadings are compared up to the sign of
each component.
"""
import os
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(11)
d = S.tmpdir()
nb, ns = 4000, 4
base = rng.gamma(2.0, 50.0, nb)                       # per-bin baseline (shared)
depth = np.array([1.0, 1.4, 0.7, 2.2])
effect = np.where(rng.random(nb) < 0.1, rng.choice([0.3, 3.0], nb), 1.0)
mat = np.zeros((nb, ns))
for j in range(ns):
    lam = base * depth[j] * (effect if j >= 2 else 1.0)
    mat[:, j] = rng.poisson(lam)
npz = os.path.join(d, "counts.npz")
with open(npz, "wb") as fh:
    np.savez_compressed(fh, matrix=mat, labels=["s1", "s2", "s3", "s4"])


def reference(m, ntop, log2, rowcenter, transpose):
    m = m.copy()
    rvs = m.var(axis=1)
    if transpose:
        keep = np.nonzero(rvs)[0]
        m, rvs = m[keep], rvs[keep]
    if ntop > 0 and m.shape[0] > ntop:
        idx = np.argpartition(rvs, -ntop)[-ntop:]
        m = m[idx]
    if log2:
        m = np.log2(m + 0.01)
    if rowcenter and not transpose:
        m = m - m.mean(axis=1)[:, None]
    if transpose:
        m = m.T
    m2 = m - m.mean(axis=0)
    m2 = m2 / np.std(m2, axis=0, ddof=1)
    U, s, Vh = np.linalg.svd(m2, full_matrices=False)
    Wt = Vh
    if transpose:
        Wt = np.dot(m2, Vh.T).T
    return Wt, s ** 2


def shipped(extra):
    out = os.path.join(d, "pca_%s.tab" % "_".join(x.strip("-") for x in extra))
    S.run(["plotPCA", "-in", npz, "--outFileNameData", out] + extra)
    rows = [l.split("\t") for l in open(out) if not l.startswith("#") and not l.startswith("Component")]
    W = np.array([[float(x) for x in r[1:1 + ns]] for r in rows])
    ev = np.array([float(r[-1]) for r in rows])
    return W, ev


def same_up_to_sign(A, B, k=3):
    return all(np.allclose(A[i], B[i], atol=1e-6) or np.allclose(A[i], -B[i], atol=1e-6) for i in range(k))


W0, e0 = shipped([])
cases = [
    ("--log2", ["--log2"], dict(ntop=1000, log2=True, rowcenter=False, transpose=False)),
    ("--rowCenter", ["--rowCenter"], dict(ntop=1000, log2=False, rowcenter=True, transpose=False)),
    ("--ntop 0 --log2", ["--ntop", "0", "--log2"], dict(ntop=0, log2=True, rowcenter=False, transpose=False)),
    ("--ntop 0 --rowCenter", ["--ntop", "0", "--rowCenter"], dict(ntop=0, log2=False, rowcenter=True, transpose=False)),
    ("--ntop 0 --log2 --rowCenter", ["--ntop", "0", "--log2", "--rowCenter"], dict(ntop=0, log2=True, rowcenter=True, transpose=False)),
    ("--transpose --log2", ["--transpose", "--log2"], dict(ntop=1000, log2=True, rowcenter=False, transpose=True)),
]
Wd, ed = shipped([])
Wref0, eref0 = reference(mat, 1000, False, False, False)
print("default (--ntop 1000): shipped loadings equal numpy reference: %s; eigenvalues max rel diff %.2e"
      % (same_up_to_sign(Wd, Wref0), np.max(np.abs(ed - eref0) / eref0)))
Wt0, et0 = shipped(["--transpose"])
Wreft, ereft = reference(mat, 1000, False, False, True)
print("--transpose: shipped projections equal numpy reference: %s" % same_up_to_sign(Wt0[:, :ns], Wreft[:, :ns]))
Wn0, en0 = shipped(["--ntop", "0"])

print("\n%-30s %-28s %-28s %s" % ("option set", "equals no-option output?", "equals its reference?", "PC1 loadings (shipped)"))
for name, extra, kw in cases:
    W, ev = shipped(extra)
    Wr, er = reference(mat, **kw)
    baseline = Wt0 if kw["transpose"] else (Wn0 if kw["ntop"] == 0 else W0)
    print("%-30s %-28s %-28s %s" % (name, same_up_to_sign(W, baseline), same_up_to_sign(W[:, :ns], Wr[:, :ns]),
                                    np.round(W[0, :ns], 4)))
print("\nreference PC1 loadings with --log2 (ntop 1000):", np.round(reference(mat, 1000, True, False, False)[0][0], 4))
print("reference PC1 loadings with --rowCenter (ntop 1000):", np.round(reference(mat, 1000, False, True, False)[0][0], 4))
