# Held-up checks: duplicateCorrelation genewise REML correlations vs lme4::lmer, the
# consensus rule, and gls.series (lmFit with block/correlation, weights and NAs) vs a
# per-gene GLS closed form. Run on 3.68.5 (statmod-based R code) and devel (C backend).
# Run: . ./rlib.sh <version>; Rscript heldup_dupcor_gls.R
suppressMessages(library(limma)); suppressMessages(library(lme4))
cat("limma", as.character(packageVersion("limma")), "lme4", as.character(packageVersion("lme4")), R.version.string, "\n")
mx <- function(a, b) max(abs(a - b), na.rm=TRUE)
set.seed(31)
G <- 400; n <- 12
block <- rep(1:6, each=2); trt <- rep(0:1, 6)
design <- cbind(Int=1, trt=trt, cov=rnorm(n))
rho <- 0.4; sb2 <- rho; se2 <- 1 - rho
u <- matrix(rnorm(G*6, 0, sqrt(sb2)), G, 6)
y <- u[, block] + matrix(rnorm(G*n, 0, sqrt(se2)), G, n) + rnorm(G, 8, 2)
y[1:100, 2] <- y[1:100, 2] + 1

## ---- A. genewise correlations vs lme4 REML ------------------------------------------
dc <- duplicateCorrelation(y, design, block=block)
rl <- sapply(1:G, function(g) {
  f <- lmer(yy ~ design[,-1] + (1|block), data=data.frame(yy=y[g,], block=factor(block)), REML=TRUE,
            control=lmerControl(check.conv.singular="ignore"))
  vc <- as.data.frame(VarCorr(f)); vc$vcov[1]/sum(vc$vcov)
})
rlim <- tanh(dc$atanh.correlations)
ok <- rl > 0.02 & rlim > 0.02 & rlim < 0.98
cat(sprintf("A. genes: %d; genewise rho, limma vs lme4 on the %d genes where both are interior (0.02..0.98): max |diff| %.2e, median |diff| %.2e\n",
            G, sum(ok), mx(rlim[ok], rl[ok]), median(abs(rlim[ok]-rl[ok]))))
cat(sprintf("   genes where lme4 is at its boundary 0 (limma allows negative): %d; limma rho < 0 there: %d\n", sum(rl <= 1e-6), sum(rlim[rl <= 1e-6] < 0)))
cat(sprintf("   consensus %.5f (true %.2f); == tanh(mean(atanh(rho), trim=0.15)): %s\n", dc$consensus.correlation, rho,
            isTRUE(all.equal(dc$consensus.correlation, tanh(mean(dc$atanh.correlations, trim=0.15, na.rm=TRUE))))))
cat("   digest of atanh.correlations (first 8):", format(dc$atanh.correlations[1:8], digits=10), "\n")

## ---- B. with weights and NAs: cross-version digest only (different model from lme4) ------
W <- matrix(rexp(G*n, 1), G, n); yw <- y; yw[sample(G*n, 60)] <- NA
dcw <- duplicateCorrelation(yw, design, block=block, weights=W)
cat(sprintf("B. with weights+NAs: consensus %.10f; NA genewise: %d; first 6 atanh: %s\n", dcw$consensus.correlation, sum(is.na(dcw$atanh.correlations)),
            paste(format(dcw$atanh.correlations[1:6], digits=10), collapse=" ")))
# within-array duplicates (ndups=2)
yd <- y[rep(1:200, each=2),] + rnorm(400*n, 0, 0.3)
dcd <- duplicateCorrelation(yd, design, ndups=2, spacing=1)
cat(sprintf("   ndups=2: consensus %.10f\n", dcd$consensus.correlation))

## ---- C. gls.series vs per-gene GLS closed form (block correlation, weights, NAs) ----------
fit <- lmFit(yw, design, block=block, correlation=dc$consensus.correlation, weights=W)
Z <- outer(block, unique(block), "==") + 0; Cm <- Z %*% t(Z) * dc$consensus.correlation; diag(Cm) <- 1
b <- s <- matrix(NA, G, 3); sig <- df <- rep(NA, G)
for(g in 1:G) {
  o <- is.finite(yw[g,]); X <- design[o,,drop=FALSE]; w <- W[g,o]; yy <- yw[g,o]
  V <- Cm[o,o] / outer(sqrt(w), sqrt(w)); Vi <- solve(V)
  A <- solve(t(X) %*% Vi %*% X); bb <- A %*% t(X) %*% Vi %*% yy; r <- yy - X %*% bb
  b[g,] <- bb; s[g,] <- sqrt(diag(A)); df[g] <- sum(o)-3; sig[g] <- sqrt(drop(t(r) %*% Vi %*% r)/df[g])
}
cat(sprintf("C. lmFit(block, correlation, weights, NAs) vs GLS closed form: coef %.2e  stdev.unscaled %.2e  sigma %.2e  df %d\n",
            mx(fit$coefficients, b), mx(fit$stdev.unscaled, s), mx(fit$sigma, sig), mx(fit$df.residual, df)))
fit2 <- lmFit(y, design, block=block, correlation=dc$consensus.correlation)   # fast path
Vi <- solve(Cm); A <- solve(t(design) %*% Vi %*% design)
b2 <- t(A %*% t(design) %*% Vi %*% t(y)); r2 <- y - b2 %*% t(design)
sig2 <- sqrt(rowSums((r2 %*% Vi) * r2)/(n-3))
cat(sprintf("   fast path (no weights/NAs): coef %.2e  stdev.unscaled %.2e  sigma %.2e\n", mx(fit2$coefficients, b2), mx(fit2$stdev.unscaled, matrix(sqrt(diag(A)), G, 3, byrow=TRUE)), mx(fit2$sigma, sig2)))
fit3 <- lmFit(y, design, block=block, correlation=dc$consensus.correlation, weights=c(2,1,1,0.5,1,1,1,2,1,1,0.5,1))  # array weights, fast path
aw <- c(2,1,1,0.5,1,1,1,2,1,1,0.5,1); Vw <- Cm/outer(sqrt(aw), sqrt(aw)); Vi <- solve(Vw); A <- solve(t(design) %*% Vi %*% design)
b3 <- t(A %*% t(design) %*% Vi %*% t(y))
cat(sprintf("   fast path with array weights: coef %.2e  stdev.unscaled %.2e\n", mx(fit3$coefficients, b3), mx(fit3$stdev.unscaled, matrix(sqrt(diag(A)), G, 3, byrow=TRUE))))
