#!/usr/bin/env python3
"""KL2: Kilosort 4 exports ContamPct = 0.0 (best possible score) for clusters
with 10 or fewer spikes.

`kilosort/CCG.py::refract` initializes `R12 = np.zeros(Nfilt)` and only
computes the contamination ratio for clusters with more than 10 spikes and a
nonzero time span.  `io.save_to_phy` then writes `est_contam_rate * 100` to
cluster_ContamPct.tsv.  A junk cluster with a handful of spikes is therefore
exported with ContamPct 0.0 - indistinguishable from a genuinely clean unit -
whereas Kilosort 2.5/3 defaulted `est_contam_rate` to 1 (ContamPct 100) for
units it could not evaluate (set_cutoff.m line 15/30).

Any analysis that selects units by "ContamPct < x" without an additional
minimum-spike-count criterion silently admits these clusters.

Run inside a venv with kilosort 4 (any version; verified on 4.1.7):

    python kl2_contampct.py

Expected output:

    is_ref:            [0. 0.]
    est_contam_rate:   [0.9388 0.    ]
    ContamPct.tsv row: cluster 0 -> 93.9   (5000-spike Poisson unit, correctly flagged)
    ContamPct.tsv row: cluster 1 -> 0.0    (8-spike junk cluster, best possible score)
"""
import numpy as np
from kilosort import CCG

rng = np.random.default_rng(1)
st_good = np.sort(rng.uniform(0, 600, 5000))   # Poisson unit, no refractoriness
st_junk = np.sort(rng.uniform(0, 600, 8))      # 8-spike junk cluster
st = np.concatenate([st_good, st_junk])
clu = np.concatenate([np.zeros(5000, int), np.ones(8, int)]).astype(np.int32)
order = np.argsort(st)

is_ref, est = CCG.refract(clu[order], st[order])
print("is_ref:          ", is_ref)
print("est_contam_rate: ", est)
print("ContamPct.tsv row: cluster 0 -> %.1f   (5000-spike Poisson unit)" % (est[0] * 100))
print("ContamPct.tsv row: cluster 1 -> %.1f   (8-spike junk cluster)" % (est[1] * 100))
