#!/usr/bin/env Rscript
# EG3: filterByExpr() at the exact boundary of its own rule.
#
# The rule (filterByExpr.Rd): keep genes with CPM >= CPM.cutoff in at least MinSampleSize
# samples, CPM.cutoff = min.count / median(lib.size) * 1e6. With an odd number of samples the
# median library size IS one of the libraries, so a gene with exactly min.count reads in that
# library has CPM mathematically equal to the cutoff and must count as "CPM >= cutoff".
# In R/filterByExpr.R the cutoff is computed as  min.count/MedianLibSize*1e6  while cpm() computes
# each CPM in C as  y*1e6/lib.size  (src/compute_cpm.c, calc_cpm_raw). The two roundings differ
# in the last bit for many library sizes, so the equality becomes a coin toss decided by the
# library size's binary representation. This harness measures it.
suppressMessages(library(edgeR))
cat("edgeR", as.character(packageVersion("edgeR")), "\n")

# --- part A: how often does the boundary comparison come out wrong for a bare count of min.count? --
set.seed(2)
L <- runif(200000, 1e5, 8e7)                        # 200,000 random library sizes
mc <- 10
cpm_edger <- as.numeric(cpm(matrix(mc, 1, length(L)), lib.size=L))
cutoff <- mc/L*1e6                                   # exactly filterByExpr's expression for the median library
below <- cpm_edger < cutoff
above <- cpm_edger > cutoff
cat(sprintf("part A: count %d in a library of size L: cpm() < min.count/L*1e6 for %d of %d library sizes (%.2f%%), > for %d (%.2f%%), equal for the rest\n",
            mc, sum(below), length(L), 100*mean(below), sum(above), 100*mean(above)))
i <- which(below)[1]
cat(sprintf("  example: L = %.17g   cpm() = %.17g   cutoff = %.17g\n", L[i], cpm_edger[i], cutoff[i]))
for (mc2 in c(5, 10, 15, 20)) {
  ce <- as.numeric(cpm(matrix(mc2, 1, length(L)), lib.size=L))
  cat(sprintf("  min.count=%2d: fraction of library sizes where the exact-boundary gene fails the CPM test: %.4f\n", mc2, mean(ce < mc2/L*1e6)))
}

# --- part B: consequence on random data sets with an odd number of samples --------------------
# A gene is "at the margin" when it has exactly min.count reads in the median library and exactly
# MinSampleSize samples (that one included) with CPM >= cutoff by exact arithmetic. Such a gene
# must be kept by the documented rule; count how many such genes filterByExpr drops.
port <- function(y, lib.size, MinSampleSize, min.count=10, min.total.count=15, large.n=10, min.prop=0.7) {
  if (MinSampleSize > large.n) MinSampleSize <- large.n + (MinSampleSize - large.n)*min.prop
  cutoff <- min.count/median(lib.size)*1e6
  cpm <- t(t(y)/lib.size)*1e6                        # same rounding order as the cutoff expression
  (rowSums(cpm >= cutoff) >= MinSampleSize - 1e-9) & (rowSums(y) >= min.total.count - 1e-9)
}
set.seed(5)
tot_margin <- 0; tot_dropped <- 0; tot_extra <- 0; tot_genes <- 0; tot_disagree <- 0; datasets <- 0
for (rep in 1:40) {
  n <- sample(c(5, 7, 9, 11), 1)
  group <- factor(rep(1:2, length.out=n))
  L <- runif(n, 5e5, 5e7)
  G <- 20000
  mu <- exp(rnorm(G, 0.5, 2.5))
  y <- matrix(rnbinom(G*n, mu=outer(mu, L/1e6), size=3), G, n)
  d <- DGEList(y, group=group, lib.size=L)
  keep <- filterByExpr(d, group=group)
  ref <- port(y, L, min(table(group)))
  jmed <- which(L == median(L))
  cutoff <- 10/median(L)*1e6
  nabove <- rowSums(t(t(y)/L)*1e6 >= cutoff)
  margin <- (y[, jmed] == 10) & (nabove == min(table(group))) & (rowSums(y) >= 15)
  tot_margin <- tot_margin + sum(margin)
  tot_dropped <- tot_dropped + sum(margin & !keep)
  tot_disagree <- tot_disagree + sum(keep != ref)
  tot_extra <- tot_extra + sum((keep != ref) & !margin)
  tot_genes <- tot_genes + G
  datasets <- datasets + 1
}
cat(sprintf("\npart B: %d data sets, %d or more samples (odd), 20,000 genes each, defaults\n", datasets, 5))
cat(sprintf("  genes exactly at the margin (min.count reads in the median library, exactly MinSampleSize samples at/above cutoff): %d\n", tot_margin))
cat(sprintf("  of these, dropped by filterByExpr although the documented rule keeps them: %d\n", tot_dropped))
cat(sprintf("  total filterByExpr-vs-rule disagreements: %d (of %d gene decisions); disagreements not explained by the margin: %d\n", tot_disagree, tot_genes, tot_extra))

# --- part C: minimal example --------------------------------------------------------------------
# Three libraries, median library size 1,000,010. Gene 1 has exactly 10 reads there and 5 reads
# in the other two (CPM 5 and 1.67, below the cutoff of 9.9999); total 20 >= min.total.count.
# With group sizes 2/1, MinSampleSize = 1, so the rule keeps gene 1 (its CPM in the median
# library equals the cutoff). Gene 2 is the same with 11 reads (a control).
L <- c(1e6, 1000010, 3e6)
y <- rbind(c(5, 10, 5), c(5, 11, 5))
d <- DGEList(y, group=factor(c(1, 2, 1)), lib.size=L)
cat("\npart C: L = (1e6, 1000010, 3e6), min.count=10, group sizes 2/1 -> MinSampleSize 1\n")
cat(sprintf("  cpm() of 10 reads in the median library = %.17g, cutoff min.count/median(L)*1e6 = %.17g, exact value 9.99990000099999...\n", cpm(d)[1, 2], 10/median(L)*1e6))
cat("  filterByExpr keeps gene 1 (5,10,5):", filterByExpr(d, group=d$samples$group)[1], "  gene 2 (5,11,5):", filterByExpr(d, group=d$samples$group)[2], "\n")
