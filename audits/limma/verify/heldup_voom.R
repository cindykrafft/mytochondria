# voom on the shipped build against an independent port of Law et al. (2014): log-cpm with
# the 0.5/1 offsets, genewise lm, sqrt-sd vs mean log-count lowess trend (same span rule),
# per-observation weights from fitted log-counts. Then the contrasts.fit approximation on
# voom-weighted fits: exact per-gene contrast sd vs the fit's shared-correlation approximation.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(5)
maxabs <- function(a,b) max(abs(as.matrix(a)-as.matrix(b)), na.rm=TRUE)
G <- 4000; n <- 8
group <- factor(rep(c("A","B"), each=4)); design <- model.matrix(~group)
mu <- 2^runif(G, 1, 12); mu <- mu/sum(mu)
L <- round(runif(n, 8e6, 3e7))
fc <- ifelse(runif(G) < 0.1, 2^rnorm(G, 0, 1), 1)
lam <- outer(mu, L); lam[, 5:8] <- lam[, 5:8]*fc
disp <- 0.05 + 2/sqrt(outer(mu*mean(L),rep(1,n)))
counts <- matrix(rnbinom(G*n, mu=lam, size=1/disp), G, n)
counts <- counts[rowSums(counts) > 10, ]; G <- nrow(counts)
rownames(counts) <- paste0("g",1:G)

HasAdaptive <- "adaptive.span" %in% names(formals(voom))   # added in limma 3.66; older builds use the fixed span=0.5
voom05 <- function(...) if(HasAdaptive) voom(..., span=0.5, adaptive.span=FALSE) else voom(..., span=0.5)
v <- voom05(counts, design)
# port
lib <- colSums(counts)
E <- log2(t((t(counts)+0.5)/(lib+1))*1e6)
fitp <- lm.fit(design, t(E))
sig <- sqrt(colMeans(fitp$effects[-(1:2),]^2))
Amean <- rowMeans(E)
sx <- Amean + mean(log2(lib+1)) - log2(1e6); sy <- sqrt(sig)
lo <- lowess(sx, sy, f=0.5)
f <- approxfun(lo, rule=2, ties=list("ordered", mean))
fitted.logcount <- log2(2^(t(fitp$coefficients) %*% t(design)) * t(matrix(lib+1, n, G)) * 1e-6)
wport <- 1/f(fitted.logcount)^4; dim(wport) <- dim(E)
cat(sprintf("[voom span=0.5] E %.1e  weights max rel %.1e  targets lib.size %.1e\n", maxabs(v$E, E), max(abs(v$weights/wport-1)), maxabs(v$targets$lib.size, lib)))
# adaptive span (default since 3.66): chooseLowessSpan(G, small.n=50, min.span=0.3, power=1/3)
va <- voom(counts, design)
span.a <- if(HasAdaptive) 0.3 + (1-0.3)*(50/G)^(1/3) else 0.5    # chooseLowessSpan: min.span + (1-min.span)*(small.n/n)^power
lo2 <- lowess(sx, sy, f=span.a); f2 <- approxfun(lo2, rule=2, ties=list("ordered",mean)); w2 <- 1/f2(fitted.logcount)^4; dim(w2) <- dim(E)
cat(sprintf("[voom adaptive span] span used %s vs rule %.5f; weights max rel %.1e\n", if(is.null(va$span)) "NA (fixed 0.5)" else format(va$span, digits=6), span.a, max(abs(va$weights/w2-1))))
# lib.size argument and DGEList-like norm factors
nf <- exp(rnorm(n, 0, 0.1)); vl <- voom05(counts, design, lib.size=lib*nf)
El <- log2(t((t(counts)+0.5)/(lib*nf+1))*1e6)
cat(sprintf("[voom lib.size] E %.1e\n", maxabs(vl$E, El)))

# --- contrasts.fit on a voom fit: documented approximation vs the exact per-gene contrast ---
# non-orthogonal design: four groups of two plus an unbalanced batch covariate, so the per-gene
# (weighted) coefficient covariance has a gene-specific correlation structure
grp <- factor(rep(c("A","B","C","D"), each=2)); batch <- c(0,1,1,0,0,0,1,1)
design3 <- cbind(model.matrix(~0+grp), batch=batch); colnames(design3) <- c("A","B","C","D","batch")
v3 <- voom05(counts, design3)
fit3 <- lmFit(v3, design3)
C <- makeContrasts(BvsA=B-A, CvsA=C-A, DvsA=D-A, "B+C-2A"=B+C-2*A, levels=design3)
cf <- contrasts.fit(fit3, C)
exact <- matrix(NA_real_, G, ncol(C))
for(g in 1:G) { w <- v3$weights[g,]; XtXi <- solve(crossprod(design3*sqrt(w))); exact[g,] <- sqrt(diag(t(C) %*% XtXi %*% C)) }
rel <- cf$stdev.unscaled/exact - 1
cat(sprintf("[contrasts.fit under voom weights, non-orthogonal design] stdev.unscaled relative error: max %.4f, 99th pct %.4f, median |.| %.4f; shared cov2cor off-diagonal max %.3f\n",
  max(abs(rel)), quantile(abs(rel), 0.99), median(abs(rel)), max(abs(cov2cor(fit3$cov.coefficients)[lower.tri(diag(5))]))))
ebc <- eBayes(cf)
fitx <- cf; fitx$stdev.unscaled <- exact
ebx <- eBayes(fitx)
cat(sprintf("  moderated t max |rel diff| %.4f; p-value max |log10 ratio| %.3f; genes BH<0.05 (BvsA): approx %d exact %d, set differences %d; (B+C-2A): approx %d exact %d, differences %d\n",
  max(abs(ebc$t/ebx$t-1)), max(abs(log10(ebc$p.value/ebx$p.value))),
  sum(p.adjust(ebc$p.value[,1],"BH")<0.05), sum(p.adjust(ebx$p.value[,1],"BH")<0.05),
  sum(xor(p.adjust(ebc$p.value[,1],"BH")<0.05, p.adjust(ebx$p.value[,1],"BH")<0.05)),
  sum(p.adjust(ebc$p.value[,4],"BH")<0.05), sum(p.adjust(ebx$p.value[,4],"BH")<0.05),
  sum(xor(p.adjust(ebc$p.value[,4],"BH")<0.05, p.adjust(ebx$p.value[,4],"BH")<0.05))))
# same with a standard intercept design (~group) and the treatment coefficients themselves: no contrasts.fit needed, exact
# unweighted fit: contrasts.fit exact
fit0 <- lmFit(v3$E, design3); c0 <- contrasts.fit(fit0, C)
ex0 <- sqrt(diag(t(C) %*% solve(crossprod(design3)) %*% C))
cat(sprintf("[contrasts.fit unweighted] stdev.unscaled vs exact %.1e\n", max(abs(t(t(c0$stdev.unscaled)/ex0)-1))))
if("contrasts" %in% names(formals(lmFit))) { fe <- lmFit(v3, design3, contrasts=C); cat(sprintf("[lmFit(contrasts=) devel] stdev.unscaled vs exact %.1e\n", maxabs(fe$stdev.unscaled, exact))) } else cat("[lmFit(contrasts=)] not on this version\n")
# voomWithQualityWeights: weights = voom weights x array weights
vq <- if(HasAdaptive) voomWithQualityWeights(counts, design, span=0.5, adaptive.span=FALSE) else voomWithQualityWeights(counts, design, span=0.5)
aw1 <- arrayWeights(voom05(counts, design), design, method="genebygene")
v2 <- voom05(counts, design, weights=aw1)
aw2 <- arrayWeights(v2, design, method="genebygene")
if(is.null(vq$targets$sample.weights)) vq$targets$sample.weights <- aw2   # not stored before limma 3.4x; only the weights are checked then
cat(sprintf("[voomWithQualityWeights] two-pass rule (voom -> aw -> voom(weights=aw) -> aw -> weights*aw): weights %.1e, sample.weights %.1e; aw range %.3f-%.3f\n",
  maxabs(vq$weights, t(aw2*t(v2$weights))), maxabs(vq$targets$sample.weights, aw2), min(aw2), max(aw2)))
