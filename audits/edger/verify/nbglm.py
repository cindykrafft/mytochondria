"""Independent negative-binomial GLM fitter (log link, fixed dispersion) used by the
Python harnesses as the reference for glmFit()/adjustedProfileLik(). Fisher scoring with
step halving, then a trust-region Newton polish on the exact log-likelihood with the
observed information, so that the reference is converged to ~1e-12 in the log-likelihood."""
import numpy as np
from scipy.special import gammaln
from scipy.optimize import minimize

def nb_loglik(y, mu, phi):
    if phi <= 0:
        return np.sum(y*np.log(mu) - mu - gammaln(y + 1))
    r = 1/phi
    return np.sum(gammaln(y + r) - gammaln(r) - gammaln(y + 1) + r*np.log(r/(r + mu)) + y*np.log(mu/(r + mu)))

def nb_fit(y, X, o, phi, tol=1e-13, maxit=200):
    beta = np.linalg.lstsq(X, np.log(y + 0.5) - o, rcond=None)[0]
    def ll(b):
        return nb_loglik(y, np.exp(X @ b + o), phi)
    cur = ll(beta)
    for it in range(maxit):
        mu = np.exp(X @ beta + o)
        w = mu/(1 + phi*mu)
        score = X.T @ ((y - mu)/(1 + phi*mu))
        info = X.T @ (w[:, None]*X)
        step = np.linalg.solve(info, score)
        t = 1.0
        while True:
            nb = beta + t*step
            new = ll(nb)
            if new >= cur - 1e-12 or t < 1e-8:
                break
            t /= 2
        if new < cur:
            break
        beta, cur = nb, new
        if np.max(np.abs(t*step)) < tol:
            break
    # polish: exact Newton (observed information) in a trust region
    def f(b): return -ll(b)
    def g(b):
        mu = np.exp(X @ b + o)
        return -(X.T @ ((y - mu)/(1 + phi*mu)))
    def h(b):
        mu = np.exp(X @ b + o)
        return X.T @ ((mu*(1 + phi*y)/(1 + phi*mu)**2)[:, None]*X)
    res = minimize(f, beta, jac=g, hess=h, method="trust-exact", options={"gtol": 1e-12, "maxiter": 200})
    if -res.fun >= cur - 1e-12:
        beta = res.x
    return beta
