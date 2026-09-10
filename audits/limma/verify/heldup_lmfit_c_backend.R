# lm.series / gls.series / lmFit(contrasts=) on the shipped build against an independent
# per-gene reference written from the model (base lm.wfit/chol per gene; no limma call
# inside the reference). On devel 3.99.0 this exercises the new C kernels (.Call lmfit/glsfit);
# on 3.68.x it exercises the R loops. Also: nthreads=4 vs 1, and the contrasts= argument
# vs contrasts.fit() on the unweighted path.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(11)
maxabs <- function(a,b) max(abs(as.matrix(a)-as.matrix(b)), na.rm=TRUE)
G <- 400; n <- 10
design <- cbind(Int=1, A=rep(c(0,1),each=5), B=rep(c(0,1),5), X=rnorm(n))
beta <- matrix(rnorm(G*4), G, 4)
y <- beta %*% t(design) + matrix(rnorm(G*n), G, n)
dimnames(y) <- list(paste0("g",1:G), paste0("s",1:n))
y[sample(length(y), 150)] <- NA           # missing values -> genewise QR
w <- matrix(rexp(G*n), G, n)              # probe weights

# reference: per-gene weighted least squares by hand
ref_lm <- function(y, X, w=NULL) {
  G <- nrow(y); p <- ncol(X)
  b <- s <- matrix(NA_real_, G, p); sig <- rep(NA_real_, G); df <- integer(G)
  for(g in 1:G) {
    o <- is.finite(y[g,]); if(!is.null(w)) o <- o & is.finite(w[g,])
    yy <- y[g,o]; XX <- X[o,,drop=FALSE]; ww <- if(is.null(w)) rep(1,sum(o)) else w[g,o]
    if(sum(o)==0) next
    Xw <- sqrt(ww)*XX; yw <- sqrt(ww)*yy
    q <- qr(Xw); r <- q$rank; est <- q$pivot[1:r]
    b[g,est] <- qr.coef(q, yw)[1:r]
    R <- qr.R(q)[1:r,1:r,drop=FALSE]; Rinv <- backsolve(R, diag(r))
    s[g,est] <- sqrt(rowSums(Rinv^2))
    df[g] <- sum(o)-r
    if(df[g]>0) sig[g] <- sqrt(sum(qr.resid(q,yw)^2)/df[g])
  }
  list(coefficients=b, stdev.unscaled=s, sigma=sig, df.residual=df)
}
cmp <- function(fit, ref, label) {
  cat(sprintf("%-46s coef %.2e  stdev %.2e  sigma %.2e  df %d  NAs-agree %s\n", label,
    maxabs(fit$coefficients, ref$coefficients), maxabs(fit$stdev.unscaled, ref$stdev.unscaled),
    maxabs(fit$sigma, ref$sigma), max(abs(fit$df.residual-ref$df.residual)),
    all(is.na(as.matrix(fit$coefficients)) == is.na(ref$coefficients))))
}
cat("\n[A] lm.series with missing values (no weights)\n")
cmp(lm.series(y, design), ref_lm(y, design), "lm.series NA")
cat("[B] lm.series with probe weights and missing values\n")
cmp(lm.series(y, design, weights=w), ref_lm(y, design, w), "lm.series NA+weights")
yc <- y; yc[is.na(yc)] <- 0
cmp(lm.series(yc, design, weights=w), ref_lm(yc, design, w), "lm.series complete+weights")
cat("[C] rank-deficient design per gene (column X zero except in samples that are NA for some genes)\n")
design2 <- design; design2[,4] <- 0; design2[1:2,4] <- 1
y2 <- y; y2[1:50,1:2] <- NA               # for genes 1..50 column X is all zero -> not estimable
cmp(lm.series(y2, design2), ref_lm(y2, design2), "lm.series genewise rank drop")

# GLS reference with block correlation
block <- rep(1:5, each=2); rho <- 0.35
ub <- unique(block); Z <- outer(block, ub, "==")*1; V0 <- Z %*% (rho*t(Z)); diag(V0) <- 1
ref_gls <- function(y, X, V0, w=NULL) {
  G <- nrow(y); p <- ncol(X)
  b <- s <- matrix(NA_real_, G, p); sig <- rep(NA_real_, G); df <- integer(G)
  for(g in 1:G) {
    o <- is.finite(y[g,]); if(!is.null(w)) o <- o & is.finite(w[g,])
    if(sum(o)==0) next
    V <- V0[o,o,drop=FALSE]
    if(!is.null(w)) { d <- 1/sqrt(w[g,o]); V <- d * t(d * t(V)) }
    L <- t(chol(V)); yy <- forwardsolve(L, y[g,o]); XX <- forwardsolve(L, X[o,,drop=FALSE])
    q <- qr(XX); r <- q$rank; est <- q$pivot[1:r]
    b[g,est] <- qr.coef(q, yy)[1:r]
    R <- qr.R(q)[1:r,1:r,drop=FALSE]; Rinv <- backsolve(R, diag(r))
    s[g,est] <- sqrt(rowSums(Rinv^2)); df[g] <- sum(o)-r
    if(df[g]>0) sig[g] <- sqrt(sum(qr.resid(q,yy)^2)/df[g])
  }
  list(coefficients=b, stdev.unscaled=s, sigma=sig, df.residual=df)
}
cat("\n[D] gls.series with block correlation\n")
cmp(gls.series(y, design, block=block, correlation=rho), ref_gls(y, design, V0), "gls.series NA")
cmp(gls.series(y, design, block=block, correlation=rho, weights=w), ref_gls(y, design, V0, w), "gls.series NA+weights")
cmp(gls.series(yc, design, block=block, correlation=rho, weights=w), ref_gls(yc, design, V0, w), "gls.series complete+weights")
cmp(gls.series(yc, design, block=block, correlation=rho), ref_gls(yc, design, V0), "gls.series complete (fast path)")

cat("\n[E] contrasts: exact per-gene contrast sd vs reference\n")
C <- cbind(AvsB=c(0,1,-1,0), A=c(0,1,0,0), ApX=c(0,1,0,1))
ref_contr <- function(y, X, C, V0=NULL, w=NULL) {
  G <- nrow(y); k <- ncol(C); b <- s <- matrix(NA_real_, G, k)
  for(g in 1:G) {
    o <- is.finite(y[g,]); if(!is.null(w)) o <- o & is.finite(w[g,])
    XX <- X[o,,drop=FALSE]; yy <- y[g,o]
    if(!is.null(V0)) { V <- V0[o,o,drop=FALSE]; if(!is.null(w)) { d <- 1/sqrt(w[g,o]); V <- d*t(d*t(V)) }
      L <- t(chol(V)); yy <- forwardsolve(L,yy); XX <- forwardsolve(L,XX) }
    else if(!is.null(w)) { yy <- sqrt(w[g,o])*yy; XX <- sqrt(w[g,o])*XX }
    q <- qr(XX); if(q$rank < ncol(X)) next
    XtXi <- chol2inv(qr.R(q))[order(q$pivot),order(q$pivot)]
    b[g,] <- drop(t(C) %*% qr.coef(q,yy)); s[g,] <- sqrt(diag(t(C) %*% XtXi %*% C))
  }
  list(coefficients=b, stdev.unscaled=s)
}
tryCatch({
  f1 <- lm.series(y, design, weights=w, contrasts=C); r1 <- ref_contr(y, design, C, w=w)
  cat(sprintf("lm.series(contrasts=) NA+weights: coef %.2e stdev %.2e\n", maxabs(f1$coefficients,r1$coefficients), maxabs(f1$stdev.unscaled,r1$stdev.unscaled)))
  f2 <- gls.series(y, design, block=block, correlation=rho, weights=w, contrasts=C); r2 <- ref_contr(y, design, C, V0=V0, w=w)
  cat(sprintf("gls.series(contrasts=) NA+weights: coef %.2e stdev %.2e\n", maxabs(f2$coefficients,r2$coefficients), maxabs(f2$stdev.unscaled,r2$stdev.unscaled)))
  f3 <- lm.series(yc, design, contrasts=C); f3b <- contrasts.fit(lm.series(yc, design), C)
  cat(sprintf("lm.series(contrasts=) unweighted vs contrasts.fit: coef %.2e stdev %.2e\n", maxabs(f3$coefficients,f3b$coefficients), maxabs(f3$stdev.unscaled,f3b$stdev.unscaled)))
  # contrasts.fit's approximation on the weighted path, for comparison
  f4 <- contrasts.fit(lm.series(y, design, weights=w), C)
  cat(sprintf("contrasts.fit on weighted fit vs exact: coef %.2e stdev max rel %.3f\n", maxabs(f4$coefficients,r1$coefficients), max(abs(f4$stdev.unscaled/r1$stdev.unscaled-1),na.rm=TRUE)))
}, error=function(e) cat("contrasts= argument not available on this version:", conditionMessage(e), "\n"))

cat("\n[F] nthreads=4 vs nthreads=1 (devel only)\n")
tryCatch({
  a <- lm.series(y, design, weights=w, nthreads=1L); b <- lm.series(y, design, weights=w, nthreads=4L)
  cat(sprintf("lm.series threads: %s\n", identical(a,b)))
  a <- gls.series(y, design, block=block, correlation=rho, weights=w, nthreads=1L); b <- gls.series(y, design, block=block, correlation=rho, weights=w, nthreads=4L)
  cat(sprintf("gls.series threads: %s\n", identical(a,b)))
}, error=function(e) cat("nthreads not available on this version\n"))

cat("\n[G] lmFit end to end (matrix input, weights, NA) vs reference\n")
fit <- lmFit(y, design, weights=w)
cmp(fit, ref_lm(y, design, w), "lmFit weights+NA")
cat("cov.coefficients equals chol2inv of the shared design:", maxabs(fit$cov.coefficients, chol2inv(qr.R(qr(design)))), "\n")
