#!/usr/bin/env python3
"""Held-up check: the Cox-Reid adjusted profile likelihood behind estimateDisp(), and the
weighted-likelihood empirical Bayes (WLEB) that turns it into common, trended and tagwise
dispersions (McCarthy, Chen & Smyth 2012 NAR 40:4288; Chen, Lun & Smyth 2014).

Port written from the papers (numpy/scipy only):
  for a gene with counts y_j, design X, offsets o_j and dispersion phi:
    beta_hat(phi) = NB maximum-likelihood coefficients (log link, Fisher scoring),
    mu_j = exp(x_j beta_hat + o_j),  W = diag(mu_j/(1 + phi mu_j)),
    APL(phi) = sum_j log NB(y_j; mu_j, phi)  -  0.5 log det(X' W X).
  edgeR evaluates APL on the grid phi_k = 0.1 * 2^t_k, t_k = -10..10 (21 points), and:
    common   = 0.1*2^argmax_t  sum_g APL_g(t)            (spline interpolation of the grid),
    tagwise  = 0.1*2^argmax_t (APL_g(t) + prior.n * m0_g(t)),
    m0_g = mean over genes (trend.method="none") or a locfit smooth of APL over AveLogCPM.
    prior.n  = prior.df / (n - p), prior.df from limma::squeezeVar on the residual
               deviances at the trended dispersion.

Run: python heldup_apl_disp.py [--lib=<version>]
"""
import numpy as np
from scipy.special import gammaln
from scipy.optimize import minimize_scalar
from rrun import run_r, version_arg, edger_version

V = version_arg()
print("edgeR/limma:", edger_version(V))

from nbglm import nb_fit, nb_loglik

def apl(y, X, o, phi):
    b = nb_fit(y, X, o, phi)
    mu = np.exp(X @ b + o)
    w = mu/(1 + phi*mu)
    info = X.T @ (w[:, None]*X)
    sign, logdet = np.linalg.slogdet(info)
    return nb_loglik(y, mu, phi) - 0.5*logdet

rng = np.random.default_rng(12)
n = 7
group = np.array([0, 0, 0, 1, 1, 1, 1])
X1 = np.column_stack([np.ones(n), group]).astype(float)                    # oneway (glmFit shortcut path)
X2 = np.column_stack([np.ones(n), group, rng.normal(size=n)]).astype(float)  # + covariate (Levenberg path)
L = rng.uniform(1e6, 4e6, n)
o = np.log(L)
G = 300
mu0 = np.exp(rng.uniform(np.log(5), np.log(2000), G))
phi_true = 0.05 + 0.3/np.sqrt(mu0)
fc = np.where(rng.random(G) < 0.2, np.exp(rng.normal(0, 0.8, G)), 1.0)
mu = mu0[:, None]*np.where(group == 1, fc[:, None], 1.0)*L[None, :]/1e6
y = rng.negative_binomial(1/phi_true[:, None], 1/(1+phi_true[:, None]*mu)).astype(float)
y = y[(y.sum(1) >= 5)]
G = len(y)
grid_t = np.linspace(-10, 10, 21)
grid_phi = 0.1*2.0**grid_t

# --- part 1: APL kernel on both designs at five dispersions ----------------------------
print(f"part 1: adjustedProfileLik() vs port, {G} genes, n={n}")
for name, X in (("~group", X1), ("~group+x", X2)):
    outs, _ = run_r("""
    o <- as.numeric(o)
    res <- sapply(c(0.001, 0.01, 0.1, 0.5, 2), function(phi) adjustedProfileLik(phi, y, X, offset=matrix(o, nrow(y), ncol(y), byrow=TRUE)))
    write.csv(res, file.path(OUT,"apl.csv"), row.names=FALSE)
    """, V, {"y": y, "X": X, "o": o.reshape(1, -1)})
    for k, phi in enumerate([0.001, 0.01, 0.1, 0.5, 2]):
        ref = np.array([apl(y[g], X, o, phi) for g in range(G)])
        print(f"  design {name:9s} phi={phi:<6}: max |edgeR - port| = {np.max(np.abs(outs['apl'][:, k] - ref)):.2e}  (APL range {ref.min():.1f}..{ref.max():.1f})")

# --- part 2: estimateDisp with trend.method="none" -----------------------------------------
X = X1
l0 = np.array([[apl(y[g], X, o, phi) for phi in grid_phi] for g in range(G)])
outs, txt = run_r("""
o <- as.numeric(o)
d <- estimateDisp(y, design=X, offset=matrix(o, nrow(y), ncol(y), byrow=TRUE), trend.method="none")
write.csv(cbind(d$common.dispersion, d$prior.df, d$prior.n), file.path(OUT,"c.csv"), row.names=FALSE)
write.csv(cbind(d$tagwise.dispersion), file.path(OUT,"tw.csv"), row.names=FALSE)
spline.pts <- seq(-10, 10, length.out=21)
# edgeR's own interpolating maximiser applied to the port's likelihood grid
common.port <- 0.1*2^maximizeInterpolant(spline.pts, matrix(colSums(l0), nrow=1))
m0 <- matrix(colMeans(l0), nrow(l0), 21, byrow=TRUE)
tw.port <- 0.1*2^maximizeInterpolant(spline.pts, l0 + d$prior.n*m0)
write.csv(cbind(common.port), file.path(OUT,"cp.csv"), row.names=FALSE)
write.csv(cbind(tw.port), file.path(OUT,"twp.csv"), row.names=FALSE)
# prior.df recomputed: deviances at the common dispersion, squeezeVar as estimateDisp calls it
fit <- glmFit(y, X, offset=matrix(o, nrow(y), ncol(y), byrow=TRUE), dispersion=d$common.dispersion, prior.count=0)
s2 <- fit$deviance/fit$df.residual
write.csv(cbind(limma::squeezeVar(s2, df=fit$df.residual)$df.prior), file.path(OUT,"pdf.csv"), row.names=FALSE)
""", V, {"y": y, "X": X, "o": o.reshape(1, -1), "l0": l0})
common, prior_df, prior_n = outs["c"]
tot = l0.sum(0)
opt = minimize_scalar(lambda t: -np.interp(t, grid_t, tot), bounds=(-10, 10), method="bounded")
# continuous maximiser of the port's summed APL (no grid): golden search on the true function
fsum = lambda t: -sum(apl(y[g], X, o, 0.1*2**t) for g in range(G))
opt2 = minimize_scalar(fsum, bounds=(grid_t[np.argmax(tot)]-1.5, grid_t[np.argmax(tot)]+1.5), method="bounded", options={"xatol": 1e-6})
print(f"\npart 2: estimateDisp(trend.method='none'), {G} genes")
print(f"  common dispersion: edgeR {common:.6f}; maximizeInterpolant on the port grid {outs['cp'][0]:.6f}; continuous argmax of the port's summed APL {0.1*2**opt2.x:.6f}")
print(f"  prior.df: edgeR {prior_df:.4f}; squeezeVar on port-independent deviances at the common dispersion {outs['pdf'][0]:.4f}; prior.n {prior_n:.4f} (= prior.df/(n-p) = {prior_df/(n-2):.4f})")
tw = outs["tw"]; twp = outs["twp"]
print(f"  tagwise dispersions: max |log2 ratio| edgeR vs WLEB on the port grid = {np.max(np.abs(np.log2(tw/twp))):.2e}")
# The same objective on a fine grid (spacing 0.05 in log2 dispersion instead of 1), to size the
# interpolation error of edgeR's 21-point grid + spline (a design choice, not a defect).
from scipy.interpolate import CubicSpline
fine_t = np.arange(-6, 4.0001, 0.05)
lf = np.array([[apl(y[g], X, o, 0.1*2**t) for t in fine_t] for g in range(G)])
m0f = lf.mean(0)
obj = lf + prior_n*m0f[None, :]
ex = np.empty(G)
for g in range(G):
    cs = CubicSpline(fine_t, obj[g]); k = np.argmax(obj[g])
    lo, hi = fine_t[max(k-1, 0)], fine_t[min(k+1, len(fine_t)-1)]
    ex[g] = 0.1*2**minimize_scalar(lambda t: -cs(t), bounds=(lo, hi), method="bounded", options={"xatol": 1e-8}).x
r = np.abs(np.log2(tw/ex))
csum = CubicSpline(fine_t, lf.sum(0)); k = np.argmax(lf.sum(0))
cex = 0.1*2**minimize_scalar(lambda t: -csum(t), bounds=(fine_t[k-1], fine_t[k+1]), method="bounded", options={"xatol": 1e-8}).x
print(f"  common dispersion, fine-grid maximiser of the summed APL: {cex:.6f} (edgeR's 21-point grid + spline: {common:.6f}, relative difference {abs(common/cex-1):.1e})")
print(f"  tagwise, 21-point grid + spline vs fine-grid maximiser of the same objective: median |log2 ratio| {np.median(r):.2e}, max {r.max():.2e}")

# --- part 3: default trend.method="locfit" -------------------------------------------------
outs, _ = run_r("""
o <- as.numeric(o)
d <- estimateDisp(y, design=X, lib.size=exp(o))     # lib.size form: AveLogCPM covariate then uses the same library sizes
spline.pts <- seq(-10, 10, length.out=21)
A <- aveLogCPM(y, lib.size=exp(o), dispersion=d$common.dispersion)
m0 <- edgeR:::locfitByCol(l0, A, span=d$span, degree=0)
trend.port <- 0.1*2^maximizeInterpolant(spline.pts, m0)
tw.port <- 0.1*2^maximizeInterpolant(spline.pts, l0 + d$prior.n*m0)
write.csv(cbind(d$trended.dispersion, trend.port, d$tagwise.dispersion, tw.port), file.path(OUT,"t.csv"), row.names=FALSE)
write.csv(cbind(d$common.dispersion, d$prior.df, d$span), file.path(OUT,"c.csv"), row.names=FALSE)
""", V, {"y": y, "X": X, "o": o.reshape(1, -1), "l0": l0})
t = outs["t"]
print(f"\npart 3: estimateDisp() defaults (locfit trend): common {outs['c'][0]:.6f}, prior.df {outs['c'][1]:.4f}, span {outs['c'][2]:.4f}")
print(f"  trended: max |log2 ratio| edgeR vs locfit(degree 0) of the port grid + maximizeInterpolant = {np.max(np.abs(np.log2(t[:,0]/t[:,1]))):.2e}")
print(f"  tagwise: max |log2 ratio| edgeR vs WLEB(port grid, same m0, edgeR prior.n)              = {np.max(np.abs(np.log2(t[:,2]/t[:,3]))):.2e}")
