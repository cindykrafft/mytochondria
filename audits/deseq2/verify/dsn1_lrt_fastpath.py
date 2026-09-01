#!/usr/bin/env python3
"""DS-1: nbinomLRT with reduced=~1 uses the intercept fast path
(fitNbinomGLMs.R lines ~104-137): fitted value = arithmetic mean of
normalized counts. That is the NB MLE only when all size factors are
equal. With unequal size factors the reduced-model log-likelihood is
evaluated below its maximum, so LRT = 2*(ll_full - ll_reduced) is
inflated for every gene. This script quantifies the inflation.
"""
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import nbinom, chi2
from scipy.special import gammaln

rng = np.random.default_rng(7)

def nb_loglik(y, mu, alpha):
    # NB with mean mu, dispersion alpha (var = mu + alpha mu^2)
    r = 1.0/alpha
    p = r/(r+mu)
    return np.sum(gammaln(y+r) - gammaln(r) - gammaln(y+1) + r*np.log(p) + y*np.log1p(-p))

def fastpath_q(y, sf):
    return np.mean(y/sf)

def mle_q(y, sf, alpha):
    f = lambda lq: -nb_loglik(y, sf*np.exp(lq), alpha)
    q0 = max(fastpath_q(y, sf), 1e-8)
    res = minimize_scalar(f, bracket=(np.log(q0)-2, np.log(q0), np.log(q0)+2))
    return np.exp(res.x)

def simulate(m, alpha, sf_spread, q_true, n_genes=4000):
    """Null genes (no group effect). Returns per-gene LRT inflation
    2*(ll(q_mle) - ll(q_fast)) and achieved size of the LRT at 0.05
    with and without the deficit, for a 2-group Wald-equivalent LRT df=1."""
    # size factors: log-uniform spread, normalized to geomean 1
    sf = np.exp(rng.uniform(-np.log(sf_spread), np.log(sf_spread), m))
    sf /= np.exp(np.mean(np.log(sf)))
    r = 1.0/alpha
    infl = np.empty(n_genes)
    for g in range(n_genes):
        mu = sf*q_true
        y = rng.negative_binomial(r, r/(r+mu))
        qf = fastpath_q(y, sf)
        if qf <= 0:   # all-zero gene
            infl[g] = 0.0; continue
        qm = mle_q(y, sf, alpha)
        infl[g] = 2.0*(nb_loglik(y, sf*qm, alpha) - nb_loglik(y, sf*qf, alpha))
    return sf, infl

print(f"{'m':>3} {'alpha':>6} {'sf range':>9} {'q':>6} | {'mean infl':>9} {'p95 infl':>8} {'max':>7} | shift of p=0.050 ->")
for m, alpha, spread, q in [
    (6, 0.05, 1.5, 100), (6, 0.2, 1.5, 100), (6, 0.5, 1.5, 100),
    (6, 0.2, 2.0, 100),  (6, 0.5, 2.0, 100), (6, 0.5, 3.0, 100),
    (12, 0.2, 2.0, 100), (12, 0.5, 2.0, 100),
    (6, 0.5, 2.0, 10),   (6, 0.5, 2.0, 1000),
]:
    sf, infl = simulate(m, alpha, spread, q)
    # a gene at exactly p=0.05 (LRT df=1: stat 3.841) reported with stat+infl
    mean_i, p95, mx = infl.mean(), np.percentile(infl, 95), infl.max()
    p_shift = chi2.sf(3.841 + mean_i, 1)
    p_shift95 = chi2.sf(3.841 + p95, 1)
    print(f"{m:>3} {alpha:>6} {spread:>9} {q:>6} | {mean_i:>9.4f} {p95:>8.4f} {mx:>7.3f} | mean {p_shift:.4f}  p95 {p_shift95:.4f}")

# also: achieved size of a full null LRT (2-group, no true effect),
# comparing fast-path reduced vs true-MLE reduced
print("\nachieved size at nominal 0.05 (2-group null LRT, df=1):")
def lrt_size(m, alpha, spread, q_true, n_genes=6000):
    sf = np.exp(rng.uniform(-np.log(spread), np.log(spread), m))
    sf /= np.exp(np.mean(np.log(sf)))
    r = 1.0/alpha
    grp = np.arange(m) % 2
    rej_fast = rej_mle = 0
    for g in range(n_genes):
        mu = sf*q_true
        y = rng.negative_binomial(r, r/(r+mu))
        if np.mean(y/sf) <= 0: continue
        # full model: separate q per group (MLE per group over its samples)
        ll_full = 0.0
        ok = True
        for k in (0,1):
            yk, sk = y[grp==k], sf[grp==k]
            if np.mean(yk/sk) <= 0: ok = False; break
            qk = mle_q(yk, sk, alpha)
            ll_full += nb_loglik(yk, sk*qk, alpha)
        if not ok: continue
        qf = fastpath_q(y, sf); qm = mle_q(y, sf, alpha)
        lrt_fast = 2*(ll_full - nb_loglik(y, sf*qf, alpha))
        lrt_mle  = 2*(ll_full - nb_loglik(y, sf*qm, alpha))
        rej_fast += lrt_fast > 3.841
        rej_mle  += lrt_mle  > 3.841
    return rej_fast/n_genes, rej_mle/n_genes

for m, alpha, spread in [(6,0.2,2.0),(6,0.5,2.0),(6,0.5,3.0),(12,0.5,2.0)]:
    f, t = lrt_size(m, alpha, spread, 100)
    print(f"  m={m} alpha={alpha} sf x{spread}: fast-path {f:.4f} vs true-MLE {t:.4f}")
