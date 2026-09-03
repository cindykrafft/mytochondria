"""Independent numpy/scipy port of the Scrublet (Wolock, Lopez & Klein 2019)
pipeline as implemented in swolock/scrublet master (67f8ecb), written from the
paper's description and checked line by line against the shipped code, but
sharing no code with it. Dense arithmetic throughout, exact nearest neighbours,
full SVD for PCA.

Two deliberate concessions so that results can be compared *exactly* to the
shipped package on the same seed:

* `simulate_pairs` draws the parent pairs with the same numpy legacy call
  (`np.random.seed(seed); np.random.randint(0, n, size=(n_sim, 2))`) that
  scrublet uses. Any other RNG stream would give different doublets, and
  a different Monte Carlo realisation, which is not what we want to test.
* the v-score fit minimises the same L1 objective with the same
  `scipy.optimize.fmin` call, because a different optimiser converges to a
  slightly different `b` and the 85th-percentile cut then moves by a few genes.

Everything else (normalisation, running quantile, gene gating, z-scoring, PCA,
kNN, score, standard error, threshold summary statistics) is written
independently.
"""

from __future__ import annotations

import numpy as np
import scipy.optimize
import scipy.sparse as sp
from scipy.spatial import cKDTree


# ---------------------------------------------------------------- normalisation
def total_count_normalise(X: np.ndarray, totals: np.ndarray, target: float) -> np.ndarray:
    return X * (target / totals)[:, None]


# ----------------------------------------------------------------- v-scores
def running_quantile(x, y, p, n_bins):
    """p-th *percentile* (numpy convention, 0-100) of y in n_bins equal-width
    bins of x; empty bins inherit the previous bin's value (NaN for the first)."""
    o = np.argsort(x)
    x, y = x[o], y[o]
    dx = (x[-1] - x[0]) / n_bins
    centres = np.linspace(x[0] + dx / 2, x[-1] - dx / 2, n_bins)
    out = np.full(n_bins, np.nan)
    for i, c in enumerate(centres):
        m = (x >= c - dx / 2) & (x < c + dx / 2)
        if m.any():
            out[i] = np.percentile(y[m], p)
        elif i > 0:
            out[i] = out[i - 1]
    return centres, out


def vscores(Enorm: np.ndarray, n_bins=50, fit_percentile=0.1):
    """Klein et al. 2015 v-score: Fano factor relative to a fitted
    FF(mu) = (1+a)(1+b) + b*mu noise model. Returns v, keep-index, mu, FF, a, b."""
    mu = Enorm.mean(0)
    keep = np.flatnonzero(mu > 0)
    mu = mu[keep]
    var = (Enorm[:, keep] ** 2).mean(0) - mu**2  # population variance
    ff = var / mu
    x, y = running_quantile(np.log(mu), np.log(ff / mu), fit_percentile, n_bins)
    ok = ~np.isnan(y)
    x, y = x[ok], y[ok]
    h, edges = np.histogram(np.log(ff), bins=200)
    mids = edges[:-1] + np.diff(edges) / 2
    c = max(np.exp(mids[np.argmax(h)]), 1.0)

    def obj(b2):
        return np.sum(np.abs(np.log(c * np.exp(-x) + b2) - y))

    b = scipy.optimize.fmin(obj, x0=[0.1], disp=False)
    a = c / (1 + b) - 1
    v = ff / ((1 + a) * (1 + b) + b * mu)
    return v, keep, mu, ff, a, b


def gene_filter(Enorm, min_counts=3, min_cells=3, pctl=85):
    v, keep, mu, ff, a, b = vscores(Enorm)
    pos = v > 0
    v, keep = v[pos], keep[pos]
    cut = np.percentile(v, pctl)
    expressed = (Enorm[:, keep] >= min_counts).sum(0) >= min_cells
    return keep[expressed & (v >= cut)]


# ---------------------------------------------------------------- simulation
def simulate_pairs(n_obs, n_sim, seed):
    np.random.seed(seed)  # noqa: NPY002 -- deliberately the legacy stream, see module docstring
    return np.random.randint(0, n_obs, size=(n_sim, 2))  # noqa: NPY002


# --------------------------------------------------------------- embedding
def zscore_fit(Xobs):
    mean = Xobs.mean(0)
    std = np.sqrt(((Xobs - mean) ** 2).mean(0))  # population sd, as scrublet
    return mean, std


def pca_fit_transform(Zobs, Zsim, n_pcs):
    mean = Zobs.mean(0)
    U, S, Vt = np.linalg.svd(Zobs - mean, full_matrices=False)
    comps = Vt[:n_pcs]
    return (Zobs - mean) @ comps.T, (Zsim - mean) @ comps.T


# ------------------------------------------------------------------ scoring
def knn_doublet_neighbours(manifold, labels, k):
    """Number of simulated-doublet neighbours among the k exact nearest
    neighbours of each point, excluding the point itself."""
    tree = cKDTree(manifold)
    _, idx = tree.query(manifold, k=k + 1)
    # drop the point itself by *index*, not by position: a simulated doublet
    # made from the pair (i, i) sits exactly on cell i, so the zero-distance
    # column is not always the point itself (sklearn's kneighbors() without a
    # query set excludes by index, which is what scrublet relies on)
    own = np.arange(idx.shape[0])[:, None]
    is_self = idx == own
    has_self = is_self.any(1)
    out = np.empty((idx.shape[0], k), dtype=idx.dtype)
    out[has_self] = idx[has_self][~is_self[has_self]].reshape(-1, k)
    out[~has_self] = idx[~has_self][:, :k]
    return labels[out].sum(1)


def score(nd, N, rho, r):
    q = (nd + 1) / (N + 2)
    return q * rho / r / (1 - rho - q * (1 - rho - rho / r))


def score_odds_form(nd, N, rho, r):
    """Same quantity written as a probability from an odds ratio: identical to
    `score` algebraically (checked in heldup harness)."""
    q = (nd + 1) / (N + 2)
    odds = q * rho / (r * (1 - rho) * (1 - q))
    return odds / (1 + odds)


def standard_error(nd, N, rho, r, se_rho):
    q = (nd + 1) / (N + 2)
    se_q = np.sqrt(q * (1 - q) / (N + 3))
    den = 1 - rho - q * (1 - rho - rho / r)
    return q * rho / r / den**2 * np.sqrt((se_q / q * (1 - rho)) ** 2 + (se_rho / rho * (1 - q)) ** 2)


def k_default(n_obs):
    return int(round(0.5 * np.sqrt(n_obs)))


def k_adjusted(k, n_obs, n_sim):
    return int(round(k * (1 + n_sim / n_obs)))


# ------------------------------------------------------------------ pipeline
def run(
    X,
    seed=0,
    sim_doublet_ratio=2.0,
    expected_doublet_rate=0.1,
    stdev_doublet_rate=0.02,
    n_prin_comps=30,
    n_neighbors=None,
    min_counts=3,
    min_cells=3,
    pctl=85,
):
    X = X.toarray() if sp.issparse(X) else np.asarray(X)
    X = X.astype(float)
    n_obs = X.shape[0]
    totals = X.sum(1)
    Enorm = total_count_normalise(X, totals, totals.mean())
    genes = gene_filter(Enorm, min_counts, min_cells, pctl)
    Xf = X[:, genes]
    n_sim = int(n_obs * sim_doublet_ratio)
    pairs = simulate_pairs(n_obs, n_sim, seed)
    Xsim = Xf[pairs[:, 0]] + Xf[pairs[:, 1]]
    tot_sim = totals[pairs[:, 0]] + totals[pairs[:, 1]]
    Nobs = total_count_normalise(Xf, totals, 1e6)
    Nsim = total_count_normalise(Xsim, tot_sim, 1e6)
    mean, std = zscore_fit(Nobs)
    Zobs = (Nobs - mean) / std
    Zsim = (Nsim - mean) / std
    Pobs, Psim = pca_fit_transform(Zobs, Zsim, n_prin_comps)
    k = k_default(n_obs) if n_neighbors is None else n_neighbors
    k_adj = k_adjusted(k, n_obs, n_sim)
    manifold = np.vstack([Pobs, Psim])
    labels = np.r_[np.zeros(n_obs, int), np.ones(n_sim, int)]
    nd = knn_doublet_neighbours(manifold, labels, k_adj)
    r = n_sim / n_obs
    ld = score(nd, k_adj, expected_doublet_rate, r)
    se = standard_error(nd, k_adj, expected_doublet_rate, r, stdev_doublet_rate)
    return dict(
        genes=genes,
        pairs=pairs,
        k=k,
        k_adj=k_adj,
        manifold_obs=Pobs,
        manifold_sim=Psim,
        nd=nd,
        scores_obs=ld[:n_obs],
        scores_sim=ld[n_obs:],
        se_obs=se[:n_obs],
        se_sim=se[n_obs:],
    )


def call(scores_obs, scores_sim, threshold):
    detected = (scores_obs > threshold).mean()
    detectable = (scores_sim > threshold).mean()
    return dict(
        predicted=scores_obs > threshold,
        detected_doublet_rate=detected,
        detectable_doublet_fraction=detectable,
        overall_doublet_rate=detected / detectable,
    )
