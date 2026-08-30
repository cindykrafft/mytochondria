#!/usr/bin/env python3
"""Numerical reproduction of B1: cluster-correction connectivity mismatch.

FreeSurfer <=7.4 builds the Monte-Carlo null max-cluster distribution with
face-only (6) connectivity (clustGetClusters -> clustGrowOneVoxel with
AllowDiag=0: neighbors require |dc|+|dr|+|ds| == 1), while mri_glmfit-sim
clusters the observed map with --allowdiag (full 26-neighborhood).

scipy equivalents (exact same neighbor sets):
  6-conn : generate_binary_structure(3, 1)   (|dc|+|dr|+|ds| == 1)
  26-conn: np.ones((3,3,3))                  (any of the 26 neighbors)

Protocol (mirrors mc-full on a one-sided positive test):
  - Null fields: white Gaussian noise on a 64x64x40 grid, Gaussian-smoothed,
    standardized to unit variance per realization (as z maps).
  - CSD: max cluster size over NSIM independent null fields, per connectivity.
  - Test: NTEST further independent null fields ("the data" under H0).
  - p(cluster) uses the shipped v6/v7.1 convention: nover/nreps with strict >.
  - Achieved FWER at nominal 0.05 = fraction of test fields whose max cluster
    is called significant. Mismatched = 26-conn data vs 6-conn null (as
    shipped); matched pairs are the controls.
"""
import json, sys
import numpy as np
from scipy.ndimage import gaussian_filter, label, generate_binary_structure

SHAPE = (64, 64, 40)
NSIM = 5000
NTEST = 5000
CDTS = {"z2.3 (p=0.01)": 2.326, "z3.1 (p=0.001)": 3.090}
FWHMS = [1.5, 2.0, 2.5]          # voxels
S6 = generate_binary_structure(3, 1)
S26 = np.ones((3, 3, 3), dtype=bool)

def max_clusters(field, thresh):
    sup = field > thresh
    out = {}
    for name, st in (("c6", S6), ("c26", S26)):
        lab, n = label(sup, structure=st)
        out[name] = 0 if n == 0 else int(np.bincount(lab.ravel())[1:].max())
    return out

def run(fwhm, seed):
    rng = np.random.default_rng(seed)
    sigma = fwhm / 2.3548
    sim = {k: {"c6": [], "c26": []} for k in CDTS}
    tst = {k: {"c6": [], "c26": []} for k in CDTS}
    for i in range(NSIM + NTEST):
        f = gaussian_filter(rng.standard_normal(SHAPE), sigma, mode="constant")
        f /= f.std()
        for k, z in CDTS.items():
            m = max_clusters(f, z)
            dst = sim if i < NSIM else tst
            dst[k]["c6"].append(m["c6"])
            dst[k]["c26"].append(m["c26"])
    res = {}
    for k in CDTS:
        null6 = np.sort(sim[k]["c6"]); null26 = np.sort(sim[k]["c26"])
        def fs_p(null, obs):   # v6/v7.1 convention: strict >, nover/nreps
            return (null > obs).sum() / len(null)
        def fwer(null, obs_list):
            return float(np.mean([fs_p(null, o) < 0.05 for o in obs_list]))
        # p the shipped 6-null assigns to a cluster at the true (26-matched) 5% critical size
        crit26 = float(np.quantile(null26, 0.95))
        p_at_true_crit = float((null6 > crit26).sum() / len(null6))
        res[k] = {
            "p6_assigned_at_matched_crit_size": p_at_true_crit,
            "fwhm_vox": fwhm,
            "q95_null6": float(np.quantile(null6, 0.95)),
            "q95_null26": float(np.quantile(null26, 0.95)),
            "FWER_shipped_26data_6null": fwer(null6, tst[k]["c26"]),
            "FWER_matched_26_26": fwer(null26, tst[k]["c26"]),
            "FWER_matched_6_6": fwer(null6, tst[k]["c6"]),
        }
    return res

if __name__ == "__main__":
    out = {}
    for j, fwhm in enumerate(FWHMS):
        out[f"fwhm{fwhm}"] = run(fwhm, seed=1234 + j)
        print(f"done fwhm={fwhm}", file=sys.stderr, flush=True)
    print(json.dumps(out, indent=1))
