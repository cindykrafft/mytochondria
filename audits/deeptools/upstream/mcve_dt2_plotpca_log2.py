"""plotPCA --log2 (and --rowCenter at the default --ntop) does not change the result.
A multiBamSummary-style matrix with a strong per-bin baseline; the loadings written by
--outFileNameData are identical with and without --log2."""
import subprocess, numpy as np

rng = np.random.RandomState(0)
mat = rng.poisson(rng.gamma(2.0, 50.0, 3000)[:, None] * np.array([1.0, 1.5, 0.5, 2.0])).astype(float)
with open("/tmp/m.npz", "wb") as fh:
    np.savez_compressed(fh, matrix=mat, labels=["a", "b", "c", "d"])

def loadings(extra):
    subprocess.run(["plotPCA", "-in", "/tmp/m.npz", "--outFileNameData", "/tmp/pca.tab"] + extra, check=True)
    return [line.split("\t")[1:5] for line in open("/tmp/pca.tab") if line[0].isdigit()]

plain, log2, rc = loadings([]), loadings(["--log2"]), loadings(["--rowCenter"])
print("PC1 loadings, no option :", plain[0])
print("PC1 loadings, --log2    :", log2[0])
print("PC1 loadings, --rowCenter:", rc[0])
assert log2 != plain, "--log2 had no effect on the PCA"
