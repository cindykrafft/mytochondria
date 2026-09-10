#!/usr/bin/env python3
"""Synthetic inputs with planted truth, shared by the harnesses."""
import numpy as np


def ranked_list(N=8000, seed=0):
    """A descending ranked list of N genes with normal scores (ties none)."""
    rng = np.random.default_rng(seed)
    names = [f"g{i:05d}" for i in range(N)]
    sc = rng.normal(size=N)
    order = np.argsort(-sc, kind="stable")
    return [names[i] for i in order], sc[order], rng


def gene_sets(names, rng, n_random=40, sizes=(15, 25, 40, 80, 150, 300)):
    """Planted sets: TOP (all in the first 200), BOTTOM (all in the last 200), UPPER_HALF
    (spread over the top 40 %), LOWER_MID (ranks 60-90 %), MIXED_HALF (half top, half bottom),
    plus random sets of several sizes.  Returns dict name -> list of members."""
    N = len(names)
    gs = {}
    gs["TOP"] = list(rng.choice(names[:200], 30, replace=False))
    gs["BOTTOM"] = list(rng.choice(names[-200:], 30, replace=False))
    gs["UPPER_HALF"] = list(rng.choice(names[: int(0.4 * N)], 60, replace=False))
    gs["LOWER_MID"] = list(rng.choice(names[int(0.6 * N): int(0.9 * N)], 50, replace=False))
    gs["MIXED_HALF"] = list(rng.choice(names[:300], 20, replace=False)) + list(rng.choice(names[-300:], 20, replace=False))
    k = 0
    for s in sizes:
        for _ in range(max(1, n_random // len(sizes))):
            gs[f"RND{s}_{k}"] = list(rng.choice(names, s, replace=False))
            k += 1
    return gs


def expression_dataset(n_genes=3000, nA=8, nB=8, n_de=200, seed=1):
    """Log-scale-like expression: genes x samples, class A = first nA columns.  The first
    n_de/2 genes are up in A (+2), the next n_de/2 down in A (-2); a block of genes has
    near-zero variance to exercise the minimum-sd rule; a block has identical values in both
    classes (metric exactly 0, a tie block)."""
    rng = np.random.default_rng(seed)
    X = rng.normal(loc=6.0, scale=1.0, size=(n_genes, nA + nB))
    X[: n_de // 2, :nA] += 2.0
    X[n_de // 2: n_de, :nA] -= 2.0
    # low-variance block: sd ~ 0.01 around mean 5 -> the 0.2*|mu| floor (=1.0) applies
    X[n_de: n_de + 50] = 5.0 + rng.normal(scale=0.01, size=(50, nA + nB))
    # zero-mean low-variance block: floor 0.2 applies
    X[n_de + 50: n_de + 80] = rng.normal(scale=0.001, size=(30, nA + nB))
    # tie block: same constant in every sample -> every metric returns 0 / ratio 1
    X[n_de + 80: n_de + 100] = 3.0
    labels = np.array([0] * nA + [1] * nB)
    names = [f"p{i:05d}" for i in range(n_genes)]
    return names, X, labels, rng
