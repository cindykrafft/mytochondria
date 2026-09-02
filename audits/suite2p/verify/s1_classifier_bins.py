#!/usr/bin/env python3
"""S1: Classifier._get_logp maps feature values at the training minimum to the
last probability bin.

suite2p/classification/classifier.py clamps each feature to the training range
and then bins it with

    ibin = np.digitize(x, grid, right=True) - 1

For x == grid[0] (every value at or below the training minimum, and NaNs,
which are set to grid[0]) np.digitize(..., right=True) returns 0, so ibin is
-1 and the probability of the *last* bin is used. With the builtin classifier
a ROI whose skew is below the training minimum is therefore scored as if it
had the highest skew.

Run inside a venv with suite2p (verified on 1.1.0):

    python s1_classifier_bins.py

Expected output (suite2p 1.1.0 builtin classifier):

    skew       ==min -> bin -1 -> p 0.948   (first bin p 0.071, last bin p 0.948)
    compact    ==min -> bin -1 -> p 0.001   (first bin p 0.448, last bin p 0.001)
    npix_norm  ==min -> bin -1 -> p 0.007   (first bin p 0.036, last bin p 0.007)
    P(cell): skew below training min 0.9856 | just above min 0.5345 | above max 0.9856
    builtin training set: 52/14058 ROIs (0.4%) have a feature at the minimum; 0 verdict flips
"""
import numpy as np
from suite2p.classification import Classifier, builtin_classfile

c = Classifier(str(builtin_classfile))
for n, k in enumerate(c.keys):
    g, p = c.grid[:, n], c.p[:, n]
    ibin = np.digitize(np.array([g[0]]), g, right=True)[0] - 1
    print(f"{k:10s} ==min -> bin {ibin} -> p {p[ibin]:.3f}   (first bin p {p[0]:.3f}, last bin p {p[-1]:.3f})")

mid = {k: c.grid[50, n] for n, k in enumerate(c.keys)}
def stat_with(skew):
    d = dict(mid); d["skew"] = skew; return [d]
i = c.keys.index("skew")
print("P(cell): skew below training min %.4f | just above min %.4f | above max %.4f" % (
    c.predict_proba(stat_with(c.grid[0, i] - 1))[0],
    c.predict_proba(stat_with(c.grid[0, i] + 1e-6))[0],
    c.predict_proba(stat_with(c.grid[-1, i] + 1))[0]))

m = np.load(str(builtin_classfile), allow_pickle=True).item()
S, y = m["stats"], m["iscell"]
aff = np.any(S <= c.grid[0][None, :], axis=1)
def proba_clipped(stats):
    logp = np.zeros(stats.shape)
    for n in range(stats.shape[1]):
        x = stats[:, n].copy(); g = c.grid[:, n]
        x[x < g[0]] = g[0]; x[x > g[-1]] = g[-1]; x[np.isnan(x)] = g[0]
        ibin = np.clip(np.digitize(x, g, right=True) - 1, 0, len(g) - 2)
        logp[:, n] = np.log(c.p[ibin, n] + 1e-6) - np.log(1 - c.p[ibin, n] + 1e-6)
    return c.model.predict_proba(logp)[:, 1]
p_cur = c.model.predict_proba(c._get_logp(S.copy()))[:, 1]
p_fix = proba_clipped(S.copy())
print("builtin training set: %d/%d ROIs (%.1f%%) have a feature at the minimum; %d verdict flips"
      % (aff.sum(), len(y), 100 * aff.mean(), int(((p_cur > .5) != (p_fix > .5)).sum())))
