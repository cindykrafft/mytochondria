# Held-up checks: normalizeQuantiles vs a port (with and without ties/NAs), removeBatchEffect
# vs a per-gene closed form, normalizeCyclicLoess flattening the M-A trend.
# Run: . ./rlib.sh <version>; Rscript heldup_norm_batch.R
suppressMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), R.version.string, "\n")
mx <- function(a, b) max(abs(a - b), na.rm=TRUE)
set.seed(51)
G <- 5000; n <- 6
x <- matrix(rnorm(G*n, 8, 2), G, n) + rep(c(0, 0.5, -0.3, 1, 0.2, -1), each=G)
x[,2] <- x[,2]*1.3

## ---- A. normalizeQuantiles -------------------------------------------------------------
port_nq <- function(A) { S <- apply(A, 2, sort); m <- rowMeans(S); R <- apply(A, 2, rank); apply(R, 2, function(r) approx((0:(nrow(A)-1))/(nrow(A)-1), m, (r-1)/(nrow(A)-1))$y) }
q <- normalizeQuantiles(x)
cat(sprintf("A. normalizeQuantiles (no ties) vs port: %.2e ; every column has identical sorted values: %s\n", mx(q, port_nq(x)), mx(apply(q, 2, sort), rowMeans(apply(x, 2, sort)))))
xt <- round(x, 1)                                              # ties
qt <- normalizeQuantiles(xt); qt0 <- normalizeQuantiles(xt, ties=FALSE)
cat(sprintf("   with ties: ties=TRUE vs port (average ranks, interpolated) %.2e ; ties=FALSE assigns sorted means by position: %.2e ; tied inputs get equal outputs (ties=TRUE): %s\n",
            mx(qt, port_nq(xt)), mx(apply(qt0, 2, sort), rowMeans(apply(xt, 2, sort))), all(sapply(1:n, function(j) all(tapply(qt[,j], xt[,j], function(v) diff(range(v))) == 0)))))
xn <- x; xn[sample(G*n, 100)] <- NA
qn <- normalizeQuantiles(xn)
port_na <- function(A) {                                       # port of the documented NA rule: interpolate each column's quantiles onto the full grid
  N <- nrow(A); i <- (0:(N-1))/(N-1)
  S <- sapply(1:ncol(A), function(j) { v <- sort(A[,j]); if(length(v) < N) approx((0:(length(v)-1))/(length(v)-1), v, i)$y else v })
  m <- rowMeans(S)
  sapply(1:ncol(A), function(j) { r <- rank(A[,j]); o <- !is.na(A[,j]); out <- A[,j]; out[o] <- approx(i, m, (r[o]-1)/(sum(o)-1))$y; out })
}
cat(sprintf("   with NAs: vs port %.2e ; NAs preserved: %s\n", mx(qn, port_na(xn)), identical(is.na(qn), is.na(xn))))

## ---- B. removeBatchEffect --------------------------------------------------------------
batch <- factor(rep(1:3, 2)); grp <- factor(rep(c("a","b"), each=3)); cov <- rnorm(n)
xb <- x + rep(c(1, -1, 0.5)[batch], each=G) + outer(rnorm(G), cov)
design <- model.matrix(~grp)
rb <- removeBatchEffect(xb, batch=batch, covariates=cov, design=design)
Xb <- cbind(model.matrix(~batch, contrasts.arg=list(batch="contr.sum"))[,-1], cov - mean(cov))
Xall <- cbind(design, Xb)
beta <- t(lm.fit(Xall, t(xb))$coefficients)
port <- xb - beta[, -(1:2)] %*% t(Xb)
cat(sprintf("B. removeBatchEffect(batch, covariates, design) vs closed form: %.2e\n", mx(rb, port)))
rb1 <- removeBatchEffect(xb, batch=batch, design=design)
refit <- lmFit(rb1, cbind(design, Xb[,1:2]))
cat(sprintf("   batch only: refitted batch coefficients after removal %.2e ; group coefficient unchanged vs before %.2e\n",
            max(abs(refit$coefficients[,3:4])), mx(refit$coefficients[,2], lmFit(xb, cbind(design, Xb[,1:2]))$coefficients[,2])))
Xu <- cbind(model.matrix(~batch, contrasts.arg=list(batch="contr.sum"))[,-1], cov)     # covariate not centred (pre-3.66 behaviour)
betau <- t(lm.fit(cbind(design, Xu), t(xb))$coefficients)
cat(sprintf("   covariate centring: vs closed form with centred covariate %.2e ; with uncentred covariate %.2e (3.66.0 NEWS: covariates now mean-corrected)\n", mx(rb, port), mx(rb, xb - betau[, -(1:2)] %*% t(Xu))))
## ---- C. normalizeCyclicLoess -----------------------------------------------------------
xc <- x + outer(rnorm(G), c(0, 0.2, 0, -0.2, 0.1, 0))*0  ; xc[,2] <- xc[,2] + 0.3*(xc[,2]-8)^2/4   # nonlinear distortion in column 2
cl <- normalizeCyclicLoess(xc, method="fast", iterations=3)
trend <- function(M) max(sapply(1:ncol(M), function(j) max(abs(loessFit(M[,j] - rowMeans(M), rowMeans(M), span=0.7)$fitted))))
cat(sprintf("C. normalizeCyclicLoess(fast): max |loess trend of x_j - rowMean| before %.3f after %.4f\n", trend(xc), trend(cl)))
cp <- normalizeCyclicLoess(xc, method="pairs", iterations=3)
cat(sprintf("   pairs method: trend after %.4f; affy method: %.4f\n", trend(cp), trend(normalizeCyclicLoess(xc, method="affy", iterations=3))))
