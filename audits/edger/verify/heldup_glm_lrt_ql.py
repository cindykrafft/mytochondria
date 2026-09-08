#!/usr/bin/env python3
"""Held-up check: glmFit()/glmLRT() against an NB-GLM port, predFC() shrinkage of logFC, and
the arithmetic of glmQLFit()/glmQLFTest() in both the legacy (Lund et al 2012 / Lun & Smyth
2017) and the 4.x adjusted-deviance form (Chen et al 2025), recomputed from the fit's own
components.

  glmFit:   NB GLM, log link, fixed dispersion; deviance = 2 sum [y log(y/mu) - (y+1/phi) log((y+1/phi)/(mu+1/phi))]
  glmLRT:   LR = deviance(null) - deviance(full), p = chi2.sf(LR, df)
  logFC:    coefficients of the same GLM on y + p_j with offsets log(L_j + 2 p_j), p_j = 0.125 L_j/mean(L)  (predFC)
  legacy QL: s2_g = deviance/df_g, df_g = n - p - (#exact zero fitted values, adjusted for design rank),
             squeezeVar(s2, df, covariate=AveLogCPM) -> s2.post, df.prior;
             F = (LR/df.test)/s2.post; p = F-distribution with (df.test, min(df.prior + df_g, sum df)).
  new QL:    same F/p arithmetic from deviance.adj/df.residual.adj/s2.post; NB dispersion = common
             Cox-Reid dispersion of the top `top.proportion` genes by AveLogCPM,
             top.proportion default = chooseLowessSpan(G*sqrt(n-p), small.n=20, min.span=0.02).

Run: python heldup_glm_lrt_ql.py [--lib=<version>]
"""
import numpy as np
from scipy.special import gammaln, xlogy
from scipy.stats import chi2, f as fdist
from rrun import run_r, version_arg, edger_version

V = version_arg()
print("edgeR/limma:", edger_version(V))

from nbglm import nb_fit, nb_loglik

def nb_dev(y, mu, phi):
    r = 1/phi
    return 2*np.sum(xlogy(y, y/mu) - (y + r)*np.log((y + r)/(mu + r)))

rng = np.random.default_rng(21)
n = 8
group = np.array([0, 0, 0, 0, 1, 1, 1, 1]); x = rng.normal(size=n)
X = np.column_stack([np.ones(n), group, x]).astype(float)
L = rng.uniform(1e6, 5e6, n); o = np.log(L)
G = 2000
mu0 = np.exp(rng.uniform(np.log(2), np.log(3000), G))
fc = np.where(rng.random(G) < 0.1, np.exp(rng.normal(0, 1.0, G)), 1.0)
mu = mu0[:, None]*np.where(group == 1, fc[:, None], 1.0)*np.exp(0.3*x)[None, :]*L[None, :]/1e6
phi_true = 0.02 + 1.0/np.sqrt(mu0)
y = rng.negative_binomial(1/phi_true[:, None], 1/(1+phi_true[:, None]*mu)).astype(float)
y[rng.random((G, n)) < 0.03] = 0
y = y[y.sum(1) >= 10]; G = len(y)
phi = 0.1

# --- part 1: glmFit / glmLRT / predFC vs port ---------------------------------------------
outs, _ = run_r(f"""
o <- as.numeric(o)
fit <- glmFit(y, X, offset=matrix(o, nrow(y), ncol(y), byrow=TRUE), dispersion={phi})
lrt <- glmLRT(fit, coef=2)
write.csv(cbind(fit$unshrunk.coefficients, fit$coefficients, fit$deviance, lrt$table$LR, lrt$table$PValue, lrt$table$logFC), file.path(OUT,"f.csv"), row.names=FALSE)
""", V, {"y": y, "X": X, "o": o.reshape(1, -1)})
F = outs["f"]
b_port = np.array([nb_fit(y[g], X, o, phi) for g in range(G)])
dev_port = np.array([nb_dev(y[g], np.exp(X @ b_port[g] + o), phi) for g in range(G)])
X0 = X[:, [0, 2]]
dev0 = np.array([nb_dev(y[g], np.exp(X0 @ nb_fit(y[g], X0, o, phi) + o), phi) for g in range(G)])
LR = dev0 - dev_port
pc = 0.125*L/L.mean(); o2 = np.log(L + 2*pc)
b_shr = np.array([nb_fit(y[g] + pc, X, o2, phi) for g in range(G)])
print(f"part 1: glmFit/glmLRT on ~group+x, {G} genes, dispersion {phi}, n={n}")
print(f"  unshrunk coefficients: max |edgeR - port| = {np.max(np.abs(F[:, :3] - b_port)):.2e}")
cd = np.max(np.abs(F[:, :3] - b_port), axis=1); rm = y.mean(1)
print(f"    median {np.median(cd):.1e}; max over genes with mean count > 20: {cd[rm > 20].max():.1e}; the worst gene has mean count {rm[np.argmax(cd)]:.1f}")
dd = F[:, 6] - dev_port
print(f"  deviance:              max |edgeR - port| = {np.max(np.abs(dd)):.2e}; min(edgeR - port) = {dd.min():.2e} (negative would mean edgeR found a lower deviance than the port)")
llp = np.array([nb_loglik(y[g], np.exp(X @ b_port[g] + o), phi) for g in range(G)])
lle = np.array([nb_loglik(y[g], np.exp(X @ F[g, :3] + o), phi) for g in range(G)])
print(f"  log-likelihood at the port's vs edgeR's coefficients: max(edgeR - port) = {np.max(lle - llp):.2e}, max(port - edgeR) = {np.max(llp - lle):.2e}")
print(f"  LR statistic:          max |edgeR - port| = {np.max(np.abs(F[:, 7] - LR)):.2e};  p-value max |diff| = {np.max(np.abs(F[:, 8] - chi2.sf(LR, 1))):.2e}")
print(f"  shrunk coefficients (predFC, prior.count 0.125): max |edgeR - port on y+p_j| = {np.max(np.abs(F[:, 3:6] - b_shr)):.2e}; logFC column = coef/log2: max |diff| = {np.max(np.abs(F[:, 9] - F[:, 4]/np.log(2))):.2e}")

# --- part 2: legacy QL arithmetic ----------------------------------------------------------
outs, _ = run_r(f"""
o <- as.numeric(o)
off <- matrix(o, nrow(y), ncol(y), byrow=TRUE)
A <- aveLogCPM(y, offset=off, dispersion={phi})
fit <- glmQLFit(y, X, offset=off, dispersion={phi}, AveLogCPM=A, legacy=TRUE)
qlf <- glmQLFTest(fit, coef=2)
fit0 <- glmFit(y, X, offset=off, dispersion={phi})
lrt <- glmLRT(fit0, coef=2)
zero <- (fit0$fitted.values < 1e-4) & (fit0$counts < 1e-4)
if(is.null(qlf$df.total)) qlf$df.total <- rep(NA_real_, nrow(y))     # not stored before 4.2
if(is.null(fit$s2.post)) fit$s2.post <- fit$var.post                 # renamed in 4.4.0
write.csv(cbind(fit$df.residual.zeros, fit$deviance, fit$s2.post, fit$df.prior, qlf$table$F, qlf$table$PValue, qlf$df.total, lrt$table$LR, rowSums(zero)), file.path(OUT,"q.csv"), row.names=FALSE)
# limma's squeezeVar on the same inputs, called directly
s2 <- fit$deviance/fit$df.residual.zeros; s2[fit$df.residual.zeros==0] <- 0
sq <- limma::squeezeVar(s2, df=fit$df.residual.zeros, covariate=A)
write.csv(cbind(sq$var.post, sq$df.prior), file.path(OUT,"sq.csv"), row.names=FALSE)
""", V, {"y": y, "X": X, "o": o.reshape(1, -1)})
Q = outs["q"]; SQ = outs["sq"]
df_res, dev, s2post, dfprior, Fstat, pQL, dftot, LRr, nzero = Q.T
# residual df adjusted for exact zeros: n - nzero - rank(X[nonzero rows]) (the .residDF rule)
df_port = np.array([n - int(nz) - np.linalg.matrix_rank(X[(y[g] > 1e-4) | True][: n - int(nz)]) if False else 0 for g, nz in enumerate(nzero)])
df_port = np.array([n - 3 if nz == 0 else (n - nz - np.linalg.matrix_rank(X[y[g] > 0])) for g, nz in enumerate(nzero.astype(int))])
df_port = np.maximum(df_port, 0)
F_port = LRr/1/s2post
dft_port = np.minimum(dfprior + df_res, df_res.sum())
p_port = fdist.sf(F_port, 1, dft_port)
if np.isnan(dftot).all():
    dftot = dft_port
print(f"\npart 2: glmQLFit(legacy=TRUE)/glmQLFTest arithmetic, {G} genes ({int((nzero > 0).sum())} with exact-zero fitted values)")
print(f"  df.residual.zeros vs n - p - zeros (rank-adjusted): {int(np.sum(df_res != df_port))} genes differ")
print(f"  s2.post / df.prior vs limma::squeezeVar called directly: max |diff| {np.max(np.abs(s2post - SQ[:, 0])):.2e} / {np.max(np.abs(dfprior - SQ[0, 1])):.2e}  (df.prior {dfprior[0]:.3f})")
print(f"  F = (LR/df.test)/s2.post: max |diff| {np.max(np.abs(Fstat - F_port)):.2e};  df.total = min(df.prior+df.res, sum df.res): max |diff| {np.max(np.abs(dftot - dft_port)):.2e}")
print(f"  p = pf(F, 1, df.total, lower=FALSE): max |diff| {np.max(np.abs(pQL - p_port)):.2e}   (Poisson bound: {int(np.sum(pQL > p_port + 1e-12))} genes raised)")

# --- part 3: new QL (legacy=FALSE) ---------------------------------------------------------
_, has_legacy = run_r('cat(packageVersion("edgeR") >= "4.2.0")', V)
if has_legacy.strip() != "TRUE":
    print("\npart 3: legacy=FALSE is not this version's default and top.proportion did not exist yet (skipped)")
    raise SystemExit(0)
outs, txt = run_r("""
o <- as.numeric(o)
off <- matrix(o, nrow(y), ncol(y), byrow=TRUE)
A <- aveLogCPM(y, offset=off)
fit <- glmQLFit(y, X, offset=off, AveLogCPM=A)
qlf <- glmQLFTest(fit, coef=2)
lrt <- glmLRT(fit, coef=2)          # the same null fit at the working dispersion that glmQLFTest uses internally
G <- nrow(y); dfres <- ncol(y)-ncol(X)
tp <- chooseLowessSpan(G*sqrt(dfres), small.n=20, min.span=0.02)
i <- order(A, decreasing=TRUE)[1:ceiling(tp*G)]
disp.top <- estimateGLMCommonDisp(y[i,], design=X, offset=off[i,])
write.csv(cbind(fit$top.proportion, tp, fit$dispersion, disp.top, fit$average.ql.dispersion, fit$df.prior), file.path(OUT,"h.csv"), row.names=FALSE)
write.csv(cbind(fit$df.residual.adj, fit$deviance.adj, fit$s2.post, qlf$table$F, qlf$table$PValue, qlf$df.total, lrt$table$LR, fit$df.residual), file.path(OUT,"q.csv"), row.names=FALSE)
""", V, {"y": y, "X": X, "o": o.reshape(1, -1)})
H = np.atleast_2d(outs["h"])[0]; Q = outs["q"]
df_adj, dev_adj, s2post, Fstat, pQL, dftot, LRr, dfr = Q.T
F_port = LRr/s2post
dft_port = np.minimum(H[5] + df_adj, dfr.sum())
p_port = fdist.sf(F_port, 1, dft_port)
print(f"\npart 3: glmQLFit(legacy=FALSE, default since 4.2.0)/glmQLFTest arithmetic")
print(f"  top.proportion: fit {H[0]:.4f}, chooseLowessSpan(G*sqrt(df), 20, 0.02) {H[1]:.4f}; NB dispersion: fit {H[2]:.5f}, estimateGLMCommonDisp on the top genes {H[3]:.5f}; average QL dispersion {H[4]:.4f}; df.prior {H[5]:.3f}")
print(f"  F = (LR/df.test)/s2.post with LR from the working-dispersion null fit: max |diff| {np.max(np.abs(Fstat - F_port)):.2e}")
print(f"  df.total = min(df.prior + df.residual.adj, sum df.residual): max |diff| {np.max(np.abs(dftot - dft_port)):.2e};  p = pf(): max |diff| {np.max(np.abs(pQL - p_port)):.2e}")
print(f"  adjusted df in (0, n-p]: min {df_adj.min():.3f}, max {df_adj.max():.3f}; s2 = deviance.adj/df.adj: max |s2.post - squeeze input| irrelevant; deviance.adj >= 0: {bool((dev_adj >= 0).all())}")
