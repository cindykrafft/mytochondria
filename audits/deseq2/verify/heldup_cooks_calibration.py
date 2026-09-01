#!/usr/bin/env python3
"""Cook's-distance calibration check.

DESeq2 flags a gene as a count outlier when any sample's Cook's distance
exceeds qf(.99, p, m-p) ("the .99 quantile of F(p, m-p)").  Cook's is
computed with a *robust method-of-moments* dispersion (trimmedCellVariance,
core.R): trimmed variance of counts scaled by constants calibrated on the
NORMAL distribution (comment: 'scale due to trimming of large squares, by
e.g. 1/mean(rnorm(1e6)^2,trim=1/8)').

Two questions:
 1. Are the constants (2.04, 1.86, 1.51) what the comment says they are?
 2. Applied to actual NB counts, what dispersion does the robust MoM
    return, and what fraction of clean NB genes get flagged at the
    nominal-looking .99 cutoff?
"""
import numpy as np
from scipy.stats import f as fdist

rng = np.random.default_rng(11)

def r_trimmed_mean(x, trim):
    """R's mean(x, trim=t): drop floor(n*t) from each end of sorted x."""
    n = len(x)
    k = int(np.floor(n*trim))
    xs = np.sort(x)
    return xs[k:n-k].mean() if n-2*k > 0 else np.median(x)

# --- 1. the constants ---
z = rng.standard_normal(4_000_000)
for tr, claimed in [(1/3, 2.04), (1/4, 1.86), (1/8, 1.51)]:
    got = 1.0/r_trimmed_mean(z**2, tr)
    print(f"trim {tr:.3f}: 1/mean(z^2,trim) = {got:.3f}   code constant {claimed}")

# --- 2. behavior on NB data: replicate the exact code path ---
TRIMRATIO = {1: 1/3, 2: 1/4, 3: 1/8}
SCALE     = {1: 2.04, 2: 1.86, 3: 1.51}
def trimbin(n):  # cut(n, breaks=c(0,3.5,23.5,Inf))
    return 1 if n <= 3.5 else (2 if n <= 23.5 else 3)

def robust_mom_alpha(cnts_norm, cells):
    """core.R trimmedCellVariance + robustMethodOfMomentsDisp, one gene at a time
    cnts_norm: genes x samples of normalized counts; cells: sample -> cell id"""
    ng, m = cnts_norm.shape
    lvls = np.unique(cells)
    varEst = np.zeros((ng, len(lvls)))
    qmat = np.zeros_like(cnts_norm)
    for li, lvl in enumerate(lvls):
        idx = cells == lvl
        n = idx.sum()
        b = trimbin(n)
        cm = np.apply_along_axis(r_trimmed_mean, 1, cnts_norm[:, idx], TRIMRATIO[b])
        qmat[:, idx] = cm[:, None]
    sqerror = (cnts_norm - qmat)**2
    for li, lvl in enumerate(lvls):
        idx = cells == lvl
        n = idx.sum()
        b = trimbin(n)
        varEst[:, li] = SCALE[b]*np.apply_along_axis(r_trimmed_mean, 1, sqerror[:, idx], TRIMRATIO[b])
    v = varEst.max(axis=1)
    mrow = cnts_norm.mean(axis=1)
    alpha = (v - mrow)/mrow**2
    return np.maximum(alpha, 0.04)

def cooks_flag_rate(m_per_grp, alpha_true, mu0=100, ngenes=20000):
    """2-group design, clean NB data, no outliers.  Fraction of genes with
    maxCooks > qf(.99, p, m-p) -- 'false outlier' rate of the default filter."""
    m = 2*m_per_grp; p = 2
    cells = np.repeat([0,1], m_per_grp)
    r = 1.0/alpha_true
    y = rng.negative_binomial(r, r/(r+mu0), size=(ngenes, m)).astype(float)
    alpha_rob = robust_mom_alpha(y, cells)   # sf=1 so normalized == raw
    # group means as mu-hat (the GLM fit for 2-group is group means)
    mu = np.zeros_like(y)
    for k in (0,1):
        mu[:, cells==k] = y[:, cells==k].mean(axis=1, keepdims=True)
    mu = np.maximum(mu, 0.5)
    V = mu + alpha_rob[:,None]*mu**2
    pr2 = (y-mu)**2/V
    H = 1.0/m_per_grp   # hat diag for group-mean fit (approx; exact for equal weights)
    cooks = pr2/p * H/(1-H)**2
    cutoff = fdist.ppf(0.99, p, m-p)
    flagged = (cooks > cutoff).any(axis=1).mean()
    med_ratio = np.median(alpha_rob)/alpha_true
    return flagged, med_ratio, cutoff

print("\nclean NB data, default cutoff qf(.99,p,m-p); flag rate = genes wrongly treated as outlier-containing")
print(f"{'n/grp':>6} {'alpha':>6} | {'median a_rob/a':>14} {'flag rate':>10} {'cutoff':>7}")
for n_per, a in [(3,0.05),(3,0.2),(3,0.5),(5,0.05),(5,0.2),(5,0.5),(10,0.2),(10,0.5)]:
    fl, ratio, cut = cooks_flag_rate(n_per, a)
    print(f"{n_per:>6} {a:>6} | {ratio:>14.3f} {fl:>10.4f} {cut:>7.2f}")
