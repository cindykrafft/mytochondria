# Held-up checks for voom (Law et al 2014) against an independent port, voomWithQualityWeights'
# weight combination, and devel voomLmFit vs edgeR 4.0.16 voomLmFit.
# Run: . ./rlib.sh <version>; Rscript heldup_voom.R
suppressMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), R.version.string, "\n")
mx <- function(a, b) max(abs(a - b), na.rm=TRUE)
set.seed(21)
G <- 6000; n <- 8
grp <- rep(0:1, each=4); design <- cbind(Int=1, grp=grp)
mu <- rexp(G, 1/200)
L <- c(2e6, 4e6, 1e6, 8e6, 3e6, 6e6, 1.5e6, 5e6)/4e6      # library-size factors (0.25..2)
lambda <- outer(mu, L) * (1 + outer(rep(c(0,1), c(G-500, 500)), grp))   # 500 genes 2x up
counts <- matrix(rnbinom(G*n, mu=lambda, size=8), G, n)
lib <- colSums(counts)

## ---- A. voom port (Law 2014, with limma's chooseLowessSpan rule) ----------------------
port_voom <- function(counts, design, lib, span) {
  y <- log2(t((t(counts) + 0.5)/(lib + 1))*1e6)
  f <- lm.fit(design, t(y)); p <- ncol(design)
  sigma <- sqrt(colMeans(f$effects[-(1:p),,drop=FALSE]^2))
  Amean <- rowMeans(y)
  sx <- Amean + mean(log2(lib+1)) - log2(1e6); sy <- sqrt(sigma)
  keep <- rowSums(counts) > 0                      # Law et al 2014 / voom.R:98-102: all-zero genes do not enter the trend fit
  l <- lowess(sx[keep], sy[keep], f=span)
  fn <- approxfun(l, rule=2, ties=list("ordered", mean))
  fitted.logcount <- log2(2^(t(f$coefficients) %*% t(design)) * 1e-6 * rep(lib+1, each=nrow(counts)))
  w <- 1/fn(fitted.logcount)^4; dim(w) <- dim(y)
  list(E=y, weights=w)
}
has.adapt <- "adaptive.span" %in% names(formals(voom))
if(has.adapt) { v <- voom(counts, design, adaptive.span=TRUE); span <- pmin(0.3 + 0.7*(50/G)^(1/3), 1) } else { v <- voom(counts, design, span=0.5); span <- 0.5 }
pv <- port_voom(counts, design, lib, span)
cat(sprintf("A. voom (span %.4f%s; %d all-zero genes): E %.2e  weights (relative) %.2e  weight range %.3g..%.3g\n", span, if(has.adapt) ", adaptive" else " fixed", sum(rowSums(counts)==0),
            mx(v$E, pv$E), max(abs(v$weights/pv$weights - 1)), min(v$weights), max(v$weights)))
v2 <- if(has.adapt) voom(counts, design, lib.size=lib*c(1.1,0.9,1,1,1.2,0.8,1,1), span=0.5, adaptive.span=FALSE) else voom(counts, design, lib.size=lib*c(1.1,0.9,1,1,1.2,0.8,1,1), span=0.5)
pv2 <- port_voom(counts, design, lib*c(1.1,0.9,1,1,1.2,0.8,1,1), 0.5)
cat(sprintf("   voom with lib.size given (norm factors): E %.2e  weights %.2e\n", mx(v2$E, pv2$E), max(abs(v2$weights/pv2$weights-1))))

## ---- B. voomWithQualityWeights combines voom weights with arrayWeights -----------------
vq <- voomWithQualityWeights(counts, design, plot=FALSE)
v1 <- voom(counts, design); aw1 <- arrayWeights(v1, design, method="genebygene")
v3 <- voom(counts, design, weights=aw1); aw2 <- arrayWeights(v3, design, method="genebygene")
cat(sprintf("B. voomWithQualityWeights == t(aw * t(voom(weights=aw1)$weights)): %.2e ; sample.weights: %s\n",
            mx(vq$weights, t(aw2 * t(v3$weights))), paste(format(vq$targets$sample.weights, digits=4), collapse=" ")))

## ---- C. (the DGEList offset probe is in lm2_voom_offset_double_count.R) ----------------

## ---- D. devel voomLmFit vs edgeR 4.0.16 voomLmFit (no sample weights) ------------------
if(exists("voomLmFit", asNamespace("limma")) && requireNamespace("edgeR", quietly=TRUE)) {
  cz <- counts; cz[1:400, 1:4] <- 0                       # 400 genes with a structural-zero group
  cz[401:600, 1:3] <- 0
  a <- suppressMessages(limma::voomLmFit(cz, design))
  b <- suppressMessages(edgeR::voomLmFit(cz, design))
  cat(sprintf("D. voomLmFit limma-devel vs edgeR 4.0.16: coef %.2e  stdev.unscaled %.2e  sigma %.2e  df.residual %d  weights %.2e  (genes with reduced df: %d)\n",
              mx(a$coefficients, b$coefficients), mx(a$stdev.unscaled, b$stdev.unscaled), mx(a$sigma, b$sigma), mx(a$df.residual, b$df.residual), mx(a$EList$weights, b$EList$weights), sum(a$df.residual < n-2)))
  blk <- rep(1:4, 2)
  a2 <- suppressMessages(limma::voomLmFit(cz, design, block=blk)); b2 <- suppressMessages(edgeR::voomLmFit(cz, design, block=blk))
  cat(sprintf("   with block: coef %.2e  sigma %.2e  weights %.2e\n", mx(a2$coefficients, b2$coefficients), mx(a2$sigma, b2$sigma), mx(a2$EList$weights, b2$EList$weights)))
  a3 <- suppressMessages(limma::voomLmFit(cz, design, sample.weights=TRUE)); b3 <- suppressMessages(edgeR::voomLmFit(cz, design, sample.weights=TRUE))
  cat(sprintf("   with sample.weights (zero rows present -> genebygene in both): max |sample weight diff| %.2e\n", mx(a3$targets$sample.weight, b3$targets$sample.weight)))
  a4 <- suppressMessages(limma::voomLmFit(counts, design, sample.weights=TRUE)); b4 <- suppressMessages(edgeR::voomLmFit(counts, design, sample.weights=TRUE))
  cat(sprintf("   with sample.weights, no zero rows (devel: reml/PrWts path; edgeR: genebygene): max |sample weight diff| %.3f\n", mx(a4$targets$sample.weight, b4$targets$sample.weight)))
  cat("   devel:", format(a4$targets$sample.weight, digits=4), "\n   edgeR:", format(b4$targets$sample.weight, digits=4), "\n")
}
