#!/usr/bin/env python3
"""DT3: plotCorrelation --removeOutliers scales deviations by the median of
|x|, not by the median absolute deviation.

correlation.Correlation.get_outlier_indices computes
    mad = 1.4826 * median(|data|)
where the documented method (Iglewicz & Hoaglin, cited in the docstring; the
--removeOutliers help text says "median absolute deviation (MAD) method
applying a threshold of 200") needs median(|data - median(data)|). For count
data median(|x|) is the median itself, so a bin is only flagged when it
exceeds the median by 200 * 1.4826 * median, i.e. ~300x the typical count.

Synthetic multiBamSummary matrix: 5000 bins of Poisson(100) counts in three
samples plus 25 "blacklist" bins with counts around 4000 (40x the median) in
every sample. Reports how many bins each rule flags, the Pearson matrix
produced by the shipped tool with and without --removeOutliers, and the
Pearson matrix after removing the bins the documented rule flags.
"""
import os
import numpy as np
import _synth as S
from deeptools.correlation import Correlation

print(S.version())
rng = np.random.default_rng(3)
d = S.tmpdir()
nb, ns = 5000, 3
mat = rng.poisson(100.0, (nb, ns)).astype(float)
hot = rng.choice(nb, 25, replace=False)
mat[hot] = rng.poisson(4000.0, (25, ns))
npz = os.path.join(d, "m.npz")
with open(npz, "wb") as fh:
    np.savez_compressed(fh, matrix=mat, labels=["a", "b", "c"])


def documented_outliers(col, max_dev=200):
    med = np.median(col)
    mad = 1.4826 * np.median(np.abs(col - med))
    return np.flatnonzero(np.abs(col - med) / mad > max_dev)


col = mat[:, 0]
print("column 0: median %.0f, median|x-median| %.0f, median|x| %.0f" % (
    np.median(col), np.median(np.abs(col - np.median(col))), np.median(np.abs(col))))
print("threshold on |x - median| for an outlier: documented rule %.0f, shipped rule %.0f"
      % (200 * 1.4826 * np.median(np.abs(col - np.median(col))), 200 * 1.4826 * np.median(np.abs(col))))
print("bins flagged in column 0: documented rule %d, shipped get_outlier_indices %d (planted hot bins: %d)"
      % (len(documented_outliers(col)), len(Correlation.get_outlier_indices(col)), len(hot)))


def pearson_shipped(extra):
    tab = os.path.join(d, "cor_%d.tab" % len(extra))
    S.run(["plotCorrelation", "-in", npz, "--corMethod", "pearson", "--whatToPlot", "heatmap",
           "-o", os.path.join(d, "h.png"), "--outFileCorMatrix", tab] + extra)
    rows = [l.rstrip("\n").split("\t") for l in open(tab) if not l.startswith("#") and not l.startswith("\t")]
    return np.array([[float(x) for x in r[1:]] for r in rows])


c_all = pearson_shipped([])
c_rm = pearson_shipped(["--removeOutliers"])
keep = np.ones(nb, bool)
keep[np.intersect1d(np.intersect1d(documented_outliers(mat[:, 0]), documented_outliers(mat[:, 1])),
                    documented_outliers(mat[:, 2]))] = False
c_doc = np.corrcoef(mat[keep].T)
c_ref_all = np.corrcoef(mat.T)
print("\nshipped Pearson, no option        : off-diagonal %s  (numpy on all bins: %s)"
      % (np.round(c_all[np.triu_indices(ns, 1)], 4), np.round(c_ref_all[np.triu_indices(ns, 1)], 4)))
print("shipped Pearson, --removeOutliers : off-diagonal %s  (bins removed: %d)"
      % (np.round(c_rm[np.triu_indices(ns, 1)], 4), nb - Correlation(npz, remove_outliers=True).matrix.shape[0]))
print("documented MAD rule (numpy)       : off-diagonal %s  (bins removed: %d)"
      % (np.round(c_doc[np.triu_indices(ns, 1)], 4), (~keep).sum()))
