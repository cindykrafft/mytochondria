# Magnitude of the under-converged REML array weights on RNA-seq data: voom weights as prior
# weights, planted sample-quality differences. arrayWeights(method="reml") at the default tol vs
# the converged solution (tol=1e-14) and vs method="genebygene"; downstream DE-gene counts.
# Also voomLmFit(sample.weights=TRUE) where available (edgeR 4.x on release builds; limma on devel).
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(23)
G <- 8000; n <- 8
group <- rep(c(0,1), each=4); design <- cbind(Int=1, Trt=group)
mu <- 2^runif(G, 2, 11)
fc <- ifelse(runif(G) < 0.1, 2^rnorm(G, 0, 0.7), 1)
lam <- outer(mu, rep(1,n)); lam[,5:8] <- lam[,5:8]*fc
qual <- c(1, 1, 3, 1, 1, 0.5, 1, 2)      # sample-specific extra variability (log-scale sd multiplier)
lam <- lam * exp(matrix(rnorm(G*n, 0, 0.25), G, n) * rep(qual, each=G))
counts <- matrix(rnbinom(G*n, mu=lam, size=10), G, n)
counts <- counts[rowSums(counts) >= 20, ]; G <- nrow(counts)
v <- voom(counts, design)
aw.def <- arrayWeights(v, design, method="reml", trace=TRUE)
aw.con <- suppressWarnings(arrayWeights(v, design, method="reml", tol=1e-14, maxiter=500))
aw.gbg <- arrayWeights(v, design, method="genebygene")
cat(sprintf("planted quality (sd multiplier): %s\nreml default tol : %s\nreml converged   : %s\ngenebygene       : %s\nmax |default-converged| %.4f, max |log ratio| %.4f\n",
  paste(sprintf("%.2f",qual),collapse=" "), paste(sprintf("%.4f",aw.def),collapse=" "), paste(sprintf("%.4f",aw.con),collapse=" "), paste(sprintf("%.4f",aw.gbg),collapse=" "),
  max(abs(aw.def-aw.con)), max(abs(log(aw.def/aw.con)))))
de <- function(aw) { vv <- v; vv$weights <- t(aw*t(v$weights)); e <- eBayes(lmFit(vv, design)); c(sum(p.adjust(e$p.value[,2],"BH")<0.05), sum(p.adjust(e$p.value[,2],"BH")<0.01)) }
d1 <- de(aw.def); d2 <- de(aw.con); d3 <- de(aw.gbg)
cat(sprintf("DE genes (BH<0.05, BH<0.01): default-tol weights %d %d; converged %d %d; genebygene %d %d; no sample weights %d %d\n", d1[1],d1[2], d2[1],d2[2], d3[1],d3[2], de(rep(1,n))[1], de(rep(1,n))[2]))
# voomLmFit where available
vlf <- if(exists("voomLmFit", where=asNamespace("limma"))) limma::voomLmFit else if(requireNamespace("edgeR", quietly=TRUE) && exists("voomLmFit", where=asNamespace("edgeR"))) edgeR::voomLmFit else NULL
if(!is.null(vlf)) {
  f <- vlf(counts, design, sample.weights=TRUE)
  sw <- f$targets$sample.weight
  cat(sprintf("voomLmFit(sample.weights=TRUE) [%s]: %s\n", environmentName(environment(vlf)), paste(sprintf("%.4f", sw), collapse=" ")))
  # the same two-pass recipe with a converged arrayWeights
  v1 <- voom(counts, design); s1 <- suppressWarnings(arrayWeights(v1, design, method="reml", tol=1e-14, maxiter=500))
  v2 <- voom(counts, design, weights=s1); s2 <- suppressWarnings(arrayWeights(v2, design, method="reml", tol=1e-14, maxiter=500))
  v2g <- voom(counts, design, weights=arrayWeights(v1, design, method="genebygene")); s2g <- arrayWeights(v2g, design, method="genebygene")
  cat(sprintf("two-pass recipe with converged REML weights: %s\ntwo-pass recipe with genebygene weights   : %s\nmax |voomLmFit - converged REML| %.4f, max |voomLmFit - genebygene| %.4f\n", paste(sprintf("%.4f", s2), collapse=" "), paste(sprintf("%.4f", s2g), collapse=" "), max(abs(sw-s2)), max(abs(sw-s2g))))
} else cat("voomLmFit not available on this build\n")
