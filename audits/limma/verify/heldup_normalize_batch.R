# normalizeQuantiles / normalizeBetweenArrays / normalizeCyclicLoess / removeBatchEffect on the
# shipped build against ports and closed forms.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(13)
maxabs <- function(a,b) max(abs(as.matrix(a)-as.matrix(b)), na.rm=TRUE)
G <- 2000; n <- 6
x <- matrix(rnorm(G*n, 8, 2), G, n) + rep(rnorm(n), each=G)
# quantile normalisation port (Bolstad 2003): sort each column, average the sorted columns, put back by rank
q_port <- function(x, ties=TRUE) { S <- apply(x, 2, sort); m <- rowMeans(S); out <- x
  for(j in 1:ncol(x)) { r <- rank(x[,j]); if(ties) out[,j] <- approx((0:(G-1))/(G-1), m, (r-1)/(G-1), ties=list("ordered",mean))$y else out[order(x[,j]),j] <- m }; out }
cat(sprintf("[normalizeQuantiles] no ties: %.1e; ties=FALSE %.1e; normalizeBetweenArrays default on matrix == quantile %.1e\n",
  maxabs(normalizeQuantiles(x), q_port(x)), maxabs(normalizeQuantiles(x, ties=FALSE), q_port(x, FALSE)), maxabs(normalizeBetweenArrays(x), normalizeQuantiles(x))))
xt <- round(x, 1)   # many ties
nq <- normalizeQuantiles(xt)
cat(sprintf("[ties] tied input values map to equal outputs within a column: %s; column quantiles identical across columns after normalisation (no-ties data): %.1e\n",
  all(sapply(1:n, function(j) { d <- tapply(nq[,j], xt[,j], function(v) diff(range(v))); max(d) })==0),
  max(apply(apply(normalizeQuantiles(x),2,sort),1,function(r) diff(range(r))))))
xna <- x; xna[sample(length(x), 100)] <- NA
nqn <- normalizeQuantiles(xna)
cat(sprintf("[NAs] NA positions preserved %s; each column's non-NA values are monotone in the input: %s\n", identical(is.na(nqn), is.na(xna)),
  all(sapply(1:n, function(j){ o <- !is.na(xna[,j]); !is.unsorted(nqn[o,j][order(xna[o,j])]) }))))
# cyclic loess: 'fast' method port using limma's loessFit is circular, so check the invariants:
# after normalisation the M vs A trend of each column against the row mean is flat (refit loess slope ~0)
# cyclic loess on low-noise data with a planted intensity-dependent distortion in each column
Gc <- 20000; ac <- runif(Gc, 4, 14); xc <- matrix(ac, Gc, n) + matrix(rnorm(Gc*n, 0, 0.15), Gc, n)
dist <- cbind(0.4*sin((ac-4)/3), -0.3*(ac-9)/5, 0.25*((ac-9)/5)^2, 0, 0.5, -0.2*cos(ac)); dist <- t(t(dist) - colMeans(dist)); xc <- xc + dist
span.a <- 0.3 + 0.7*(50/Gc)^(1/3)
trend <- function(m) { a <- rowMeans(m); max(sapply(1:n, function(j) max(abs(loessFit(m[,j]-a, a, span=span.a)$fitted)))) }
cat(sprintf("[normalizeCyclicLoess fast] planted column distortions up to %.2f; residual trend (loessFit at the adaptive span %.4f) after 1/3/10 iterations: %.2e %.2e %.2e\n",
  max(abs(dist)), span.a, trend(normalizeCyclicLoess(xc, iterations=1)), trend(normalizeCyclicLoess(xc, iterations=3)), trend(normalizeCyclicLoess(xc, iterations=10))))
cl <- normalizeCyclicLoess(x, iterations=3)
cat(sprintf("  affy / pairs methods, 3 iterations: residual trend %.2e %.2e\n", trend(normalizeCyclicLoess(xc, iterations=3, method="affy")), trend(normalizeCyclicLoess(xc, iterations=3, method="pairs"))))
# loessFit vs stats::lowess with the same span (the weighted lowess C code changed on devel)
a <- rowMeans(x); lf <- loessFit(x[,1]-a, a, span=0.4); lw <- lowess(a, x[,1]-a, f=0.4, iter=3)
cat(sprintf("[loessFit unweighted vs stats::lowess f=0.4] max |diff| %.2e (both tricube, 3 robustness iterations)\n", max(abs(lf$fitted[order(a)]-lw$y))))
w <- rexp(G); lfw <- loessFit(x[,1]-a, a, weights=w, span=0.4)
cat(sprintf("[loessFit weighted] fitted range %.4f %.4f  sum fitted %.6f\n", min(lfw$fitted), max(lfw$fitted), sum(lfw$fitted)))
# removeBatchEffect: closed form = y - beta_batch %*% t(Xbatch) with sum-to-zero batch coding, batch estimated adjusted for design
batch <- factor(rep(1:3, 2)); grp <- factor(rep(c("a","b"), each=3)); cov1 <- rnorm(n)
rb <- removeBatchEffect(x, batch=batch, covariates=cov1, design=model.matrix(~grp))
Xb <- cbind(model.matrix(~batch, contrasts.arg=list(batch="contr.sum"))[,-1], cov1-mean(cov1))
Xfull <- cbind(model.matrix(~grp), Xb)
B <- t(lm.fit(Xfull, t(x))$coefficients)[, 3:5]
refit <- t(lm.fit(Xfull, t(rb))$coefficients)
cat(sprintf("[removeBatchEffect] vs closed form %.1e; refit on corrected data: batch/covariate coefficients %.1e, design coefficients unchanged %.1e\n", maxabs(rb, x - B %*% t(Xb)),
  max(abs(refit[,3:5])), maxabs(refit[,1:2], t(lm.fit(Xfull, t(x))$coefficients)[,1:2])))
# without design: batch means removed including the group effect (documented one-group assumption)
rb0 <- suppressMessages(removeBatchEffect(x, batch=batch))
Xb0 <- model.matrix(~batch, contrasts.arg=list(batch="contr.sum"))[,-1]; B0 <- t(lm.fit(cbind(1,Xb0), t(x))$coefficients)[,2:3]
cat(sprintf("[removeBatchEffect no design] vs closed form %.1e\n", maxabs(rb0, x - B0 %*% t(Xb0))))
# normalizeBetweenArrays 'scale' on a matrix: median-centre columns to the geometric-mean... it uses normalizeMedianValues
sc <- normalizeBetweenArrays(x, method="scale")
cat(sprintf("[scale] column medians equal after scaling: %.1e\n", diff(range(apply(sc,2,median)))))
