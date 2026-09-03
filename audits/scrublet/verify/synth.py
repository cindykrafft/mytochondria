"""Synthetic scRNA-seq counts with labelled doublets, shared by the harnesses.

A mixture of `n_types` cell states. Each state has its own set of marker genes
(4x the baseline mean); every gene's baseline mean is log-normal. Library sizes
are log-normal. Counts are Poisson given the cell's expected profile. True
doublets are made exactly the way Scrublet simulates them -- by adding the
counts of two singlets -- but the two parents are always of *different* states
(heterotypic), so every true doublet is in principle detectable. Labels are
returned, so recall and precision are known.

No package under audit is imported here.
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp


def make_counts(
    n_singlets: int = 1500,
    n_doublets: int = 150,
    n_genes: int = 2000,
    n_types: int = 6,
    n_markers: int = 80,
    lib_size: float = 4000.0,
    marker_fold: float = 4.0,
    overdispersion: float = 0.1,
    seed: int = 1,
):
    """`overdispersion` is the extra CV^2 of a gamma-Poisson (NB) count model,
    so that the v-score noise fit has a positive baseline to find, as on real
    droplet data; 0 gives pure Poisson counts."""
    rng = np.random.default_rng(seed)
    base = np.exp(rng.normal(-1.0, 1.2, size=n_genes))  # heavy-tailed gene means
    base /= base.sum()
    types = rng.integers(0, n_types, size=n_singlets)
    profiles = np.tile(base, (n_types, 1))
    marker_pool = rng.permutation(n_genes)[: n_types * n_markers].reshape(n_types, n_markers)
    for t in range(n_types):
        profiles[t, marker_pool[t]] *= marker_fold
        profiles[t] /= profiles[t].sum()
    libs = np.exp(rng.normal(np.log(lib_size), 0.35, size=n_singlets))
    lam = libs[:, None] * profiles[types]
    if overdispersion > 0:
        lam = lam * rng.gamma(1 / overdispersion, overdispersion, size=lam.shape)
    singlets = rng.poisson(lam)
    # heterotypic true doublets: two singlets of different states, counts added
    a = rng.integers(0, n_singlets, size=n_doublets)
    b = rng.integers(0, n_singlets, size=n_doublets)
    same = types[a] == types[b]
    while same.any():
        b[same] = rng.integers(0, n_singlets, size=same.sum())
        same = types[a] == types[b]
    doublets = singlets[a] + singlets[b]
    X = np.vstack([singlets, doublets]).astype(np.int64)
    is_doublet = np.r_[np.zeros(n_singlets, bool), np.ones(n_doublets, bool)]
    cell_type = np.r_[types, -np.ones(n_doublets, int)]
    perm = rng.permutation(X.shape[0])  # shuffle rows so order carries no label
    return sp.csc_matrix(X[perm]), is_doublet[perm], cell_type[perm]


def recall_precision(pred, truth):
    pred = np.asarray(pred, bool)
    truth = np.asarray(truth, bool)
    tp = (pred & truth).sum()
    rec = tp / max(truth.sum(), 1)
    prec = tp / max(pred.sum(), 1)
    return float(rec), float(prec), int(pred.sum())


if __name__ == "__main__":
    X, d, t = make_counts()
    print(X.shape, d.sum(), np.bincount(t[t >= 0]), X.sum(1).A.ravel().mean())
