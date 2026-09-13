# Note N2: contrasts.fit()'s documented approximation of stdev.unscaled when the fit had
# precision weights (voom) and the design is non-orthogonal; size of the effect and the exact
# alternative in devel (lmFit(contrasts=), voomLmFit(contrasts=)).
# Run: . ./rlib.sh <version>; Rscript note_contrasts_fit_weights.R
suppressMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), R.version.string, "\n")
mx <- function(a, b) max(abs(a - b), na.rm=TRUE)
set.seed(71)
G <- 6000; n <- 12
grp <- factor(rep(c("A","B","C"), each=4)); batch <- factor(rep(1:2, 6))
design <- model.matrix(~0 + grp + batch); colnames(design) <- c("A","B","C","batch2")   # non-orthogonal (batch)
mu <- rexp(G, 1/200)
L <- rep(c(0.3, 3), 6)                                     # strongly unequal library sizes -> unequal voom weights
counts <- matrix(rnbinom(G*n, mu=outer(mu, L), size=8), G, n)
counts[1:300, grp=="B"] <- counts[1:300, grp=="B"]*2
vm <- function(...) if("adaptive.span" %in% names(formals(voom))) voom(..., span=0.5, adaptive.span=FALSE) else voom(..., span=0.5)
v <- vm(counts, design)
fit <- lmFit(v, design)
C <- makeContrasts(BvsA=B-A, CvsA=C-A, BCvsA=(B+C)/2-A, levels=design)
cf <- contrasts.fit(fit, C)
ex <- t(sapply(1:G, function(g) { V <- solve(crossprod(design*sqrt(v$weights[g,]))); sqrt(diag(t(C) %*% V %*% C)) }))
r <- cf$stdev.unscaled/ex
cat("ratio contrasts.fit stdev.unscaled / exact, quantiles per contrast:\n"); print(round(apply(r, 2, quantile, c(0, .01, .1, .5, .9, .99, 1)), 4))
cat(sprintf("coefficients are exact: %.2e\n", mx(cf$coefficients, fit$coefficients %*% C)))
eb <- eBayes(cf); cx <- cf; cx$stdev.unscaled <- ex; ebx <- eBayes(cx)
cat("t-statistic ratio approx/exact, quantiles (BvsA):", format(quantile(eb$t[,1]/ebx$t[,1], c(0, .01, .5, .99, 1)), digits=4), "\n")
cat(sprintf("genes at adj.P<0.05 per contrast: approx %s ; exact %s ; disagreements %s\n", paste(colSums(decideTests(eb) != 0), collapse="/"), paste(colSums(decideTests(ebx) != 0), collapse="/"), paste(colSums(decideTests(eb) != decideTests(ebx)), collapse="/")))
if("contrasts" %in% names(formals(lmFit))) {
  f2 <- lmFit(v, design, contrasts=C)
  cat(sprintf("devel lmFit(contrasts=C): stdev.unscaled vs exact %.2e ; coefficients vs contrasts.fit %.2e\n", mx(f2$stdev.unscaled, ex), mx(f2$coefficients, cf$coefficients)))
  f3 <- voomLmFit(counts, design, contrasts=C, span=0.5, adaptive.span=FALSE)
  ex3 <- t(sapply(1:G, function(g) { V <- solve(crossprod(design*sqrt(f3$EList$weights[g,]))); sqrt(diag(t(C) %*% V %*% C)) }))
  cat(sprintf("devel voomLmFit(contrasts=C): stdev.unscaled vs exact (from its own weights) %.2e\n", mx(f3$stdev.unscaled, ex3)))
}
# an orthogonal design (one-way) is exact even with weights
d1 <- model.matrix(~0 + grp); colnames(d1) <- c("A","B","C")
v1 <- vm(counts, d1); f1 <- lmFit(v1, d1); C1 <- C[1:3,]
ex1 <- t(sapply(1:G, function(g) { V <- solve(crossprod(d1*sqrt(v1$weights[g,]))); sqrt(diag(t(C1) %*% V %*% C1)) }))
cat(sprintf("one-way design (orthogonal): contrasts.fit stdev.unscaled vs exact %.2e\n", mx(contrasts.fit(f1, C1)$stdev.unscaled, ex1)))
