#!/usr/bin/env Rscript
# Held-up check: filterByExpr() against an independent implementation of the rule in
# its help page (filterByExpr.Rd, Details):
#   keep genes with CPM >= CPM.cutoff in at least MinSampleSize samples, where
#   CPM.cutoff = min.count / median(lib.size) * 1e6,
#   MinSampleSize = smallest group size (group) or 1/max(hat(design)) (design),
#   if MinSampleSize > large.n: MinSampleSize <- large.n + (MinSampleSize - large.n)*min.prop,
#   and total count >= min.total.count.
# The DGEList method's documented default library size is the normalized library size
# (lib.size * norm.factors).
suppressMessages(library(edgeR))
cat("edgeR", as.character(packageVersion("edgeR")), "\n")

port <- function(y, lib.size, MinSampleSize, min.count=10, min.total.count=15, large.n=10, min.prop=0.7) {
  if (MinSampleSize > large.n) MinSampleSize <- large.n + (MinSampleSize - large.n)*min.prop
  cutoff <- min.count/median(lib.size)*1e6
  cpm <- t(t(y)/lib.size)*1e6
  (rowSums(cpm >= cutoff - 1e-9) >= MinSampleSize - 1e-9) & (rowSums(y) >= min.total.count - 1e-9)
}

set.seed(11)
mismatch <- 0; ntests <- 0; kept <- c(); boundary <- 0
for (rep in 1:30) {
  G <- 3000; n <- sample(4:30, 1)
  ngroups <- sample(2:4, 1)
  group <- factor(sample(ngroups, n, replace=TRUE))
  while (nlevels(droplevels(group)) < 2) group <- factor(sample(ngroups, n, replace=TRUE))
  group <- droplevels(group)
  L <- runif(n, 2e5, 5e6)
  mu <- exp(rnorm(G, 1, 2.5))
  y <- matrix(rnbinom(G*n, mu=outer(mu, L/1e6), size=3), G, n)
  nf <- exp(rnorm(n, 0, 0.2)); nf <- nf/exp(mean(log(nf)))
  d <- DGEList(y, group=group, lib.size=L, norm.factors=nf)
  mc <- sample(c(5, 10, 20), 1)

  # (a) group argument
  k1 <- filterByExpr(d, group=group, min.count=mc)
  r1 <- port(y, L*nf, min(table(group)), min.count=mc)
  # (b) design argument (oneway design + a covariate)
  x <- rnorm(n)
  design <- model.matrix(~group + x)
  k2 <- filterByExpr(d, design=design, min.count=mc)
  r2 <- port(y, L*nf, 1/max(hat(design)), min.count=mc)
  # (c) matrix input, no group: all samples one group -> MinSampleSize = n
  k3 <- suppressMessages(filterByExpr(y, min.count=mc))
  r3 <- port(y, colSums(y), n, min.count=mc)
  # (d) explicit lib.size overrides the DGEList's
  k4 <- filterByExpr(d, group=group, lib.size=L, min.count=mc)
  r4 <- port(y, L, min(table(group)), min.count=mc)
  # (e) large.n / min.prop rule with a big group
  k5 <- filterByExpr(d, group=group, large.n=3, min.prop=0.5, min.count=mc)
  r5 <- port(y, L*nf, min(table(group)), large.n=3, min.prop=0.5, min.count=mc)
  # a disagreement is "at the boundary" (EG3) when the gene has exactly min.count reads in a
  # library whose size equals the median library size used by that call
  atb <- function(keep, ref, ls) { jm <- which(ls == median(ls)); if (!length(jm)) return(0); sum((keep != ref) & (y[, jm[1]] == mc)) }
  for (p in list(list(k1, r1, L*nf), list(k2, r2, L*nf), list(k3, r3, colSums(y)), list(k4, r4, L), list(k5, r5, L*nf))) {
    ntests <- ntests + 1
    mismatch <- mismatch + sum(p[[1]] != p[[2]])
    boundary <- boundary + atb(p[[1]], p[[2]], p[[3]])
  }
  kept <- c(kept, mean(k1))
}
cat("30 random datasets x 5 call forms:", ntests, "comparisons,", mismatch, "gene-level disagreements between filterByExpr and the port,",
    boundary, "of them genes with exactly min.count reads in the median-size library (the EG3 boundary case)\n")
cat("fraction of genes kept (group form), range:", signif(range(kept), 3), "\n")

# The CPM cutoff and MinSampleSize for a concrete case, printed for the review
L <- c(1e6, 2e6, 3e6, 4e6, 5e6, 6e6); group <- factor(c(1,1,1,2,2,2))
cat("\nlib sizes 1..6 million, min.count=10: CPM cutoff = ", 10/median(L)*1e6, "; MinSampleSize = 3\n")
cat("with 12 samples per group and defaults: MinSampleSize -> ", 10 + (12-10)*0.7, "\n")
# boundary: exactly MinSampleSize samples at exactly the cutoff count
y <- matrix(0, 3, 6); y[1, 1:3] <- 10*L[1:3]/3.5e6; y[2, 1:2] <- 100; y[3, ] <- 2.5
d <- DGEList(y, group=group, lib.size=L)
cat("boundary genes (3 samples exactly at the cutoff / 2 samples high / total 15 spread thin):", filterByExpr(d, group=group), "\n")
