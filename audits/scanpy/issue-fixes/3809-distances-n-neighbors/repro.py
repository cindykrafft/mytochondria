"""scverse/scanpy#3809: `.obsp["distances"]` has `n_neighbors` instead of `n_neighbors - 1` entries per cell.

Runs `sc.pp.neighbors` with the same `n_neighbors` through the brute-force path
(`transformer="sklearn"`) and the pynndescent path (explicitly, and implicitly via the
default `transformer=None` on >= 8192 cells) and counts, per cell, the non-zero entries in
`.obsp["distances"]` and how many of those neighbours are missing from `.obsp["connectivities"]`.
"""

from importlib.metadata import version

import numpy as np

import scanpy as sc

rng = np.random.default_rng(0)
k = 15
print(f"scanpy {version('scanpy')}, n_neighbors={k}, documented non-zero entries per row: {k - 1}\n")

cases = [
    ("sklearn", 1500),
    ("pynndescent", 1500),
    (None, 8500),  # default transformer: pynndescent for >= 8192 cells (euclidean)
]
for transformer, n_obs in cases:
    adata = sc.AnnData(rng.random((n_obs, 30)).astype(np.float32))
    sc.pp.neighbors(adata, n_neighbors=k, use_rep="X", transformer=transformer, random_state=0)
    dists, conns = adata.obsp["distances"], adata.obsp["connectivities"]
    nonzero = dists.getnnz(axis=1)
    stored = np.diff(dists.indptr)
    n_check = min(n_obs, 500)
    n_inconsistent = sum(
        len(set(dists[i].indices[dists[i].data != 0]) - set(conns[i].indices)) > 0
        for i in range(n_check)
    )
    print(
        f"transformer={transformer!s:12s} n_obs={n_obs:5d}: "
        f"non-zero entries per row {nonzero.min()}..{nonzero.max()}, stored {stored.min()}..{stored.max()}; "
        f"{n_inconsistent} of the first {n_check} cells have a neighbour in `distances` absent from `connectivities`"
    )
