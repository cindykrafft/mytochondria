#!/usr/bin/env python3
"""Reproducibility: with random_state set, does n_jobs change the result (fit and graph)?
Exact path (n < 4096) and pynndescent path (n >= 4096).  Also: two unseeded runs differ
(expected), and the seeded run is bit-identical on repeat.
"""
import warnings
import numpy as np
import umap

warnings.simplefilter("ignore")
print("umap-learn", umap.__version__)
rng = np.random.default_rng(6)
for N in (2000, 6000):
    X = np.vstack([rng.normal(0, 1, (N // 2, 20)), rng.normal(3, 1, (N // 2, 20))]).astype(np.float32)
    res = {}
    for nj in (1, 4):
        m = umap.UMAP(n_neighbors=15, random_state=42, n_jobs=nj).fit(X)
        res[nj] = (m.embedding_.copy(), m.graph_.tocsr().copy(), m.n_jobs)
    m2 = umap.UMAP(n_neighbors=15, random_state=42, n_jobs=1).fit(X)
    print(f"\nN={N} ({'exact' if N < 4096 else 'pynndescent'} path):")
    print(f"  n_jobs after fit: requested 1 -> {res[1][2]}, requested 4 -> {res[4][2]}")
    print(f"  graph_ n_jobs=1 vs n_jobs=4: max |diff| = {abs(res[1][1] - res[4][1]).max():.2e}")
    print(f"  embedding n_jobs=1 vs n_jobs=4: max |diff| = {np.abs(res[1][0] - res[4][0]).max():.2e}")
    print(f"  repeat seeded run: max |embedding diff| = {np.abs(res[1][0] - m2.embedding_).max():.2e}")
    u1 = umap.UMAP(n_neighbors=15).fit(X); u2 = umap.UMAP(n_neighbors=15).fit(X)
    print(f"  two unseeded runs: graph_ max |diff| = {abs(u1.graph_ - u2.graph_).max():.2e}, embedding max |diff| = {np.abs(u1.embedding_ - u2.embedding_).max():.2f} (expected to differ)")
