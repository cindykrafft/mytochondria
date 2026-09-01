suppressMessages(library(DESeq2))
set.seed(7)
cat("== A. null calibration of the default pipeline (context; known-literature territory) ==\n")
calib <- function(n_per, n=8000, mu=80, disp=0.15) {
  m <- 2*n_per
  cond <- factor(rep(c("A","B"), each=n_per))
  cts <- matrix(rnbinom(n*m, mu=mu, size=1/disp), ncol=m); mode(cts) <- "integer"
  dds <- DESeqDataSetFromMatrix(cts, S4Vectors::DataFrame(cond=cond), ~cond)
  dds <- DESeq(dds, quiet=TRUE)
  res <- results(dds)
  p <- res$pvalue[!is.na(res$pvalue)]
  cat(sprintf("  %dv%d: FPR@0.05 = %.4f  FPR@0.01 = %.4f  (n=%d genes)\n",
              n_per, n_per, mean(p<0.05), mean(p<0.01), length(p)))
}
calib(3); calib(5); calib(10)

cat("\n== B. greaterAbs p-values: 2014 formula (releases <=1.42) vs 2024 formula (>=1.44), same data ==\n")
## papers using lfcThreshold reproduce differently across this boundary
n <- 6000; n_per <- 5; m <- 2*n_per
cond <- factor(rep(c("A","B"), each=n_per))
cts <- matrix(rnbinom(n*m, mu=100, size=1/0.1), ncol=m)
## half the genes have a true LFC near the threshold
beta <- c(rep(0, n/2), rnorm(n/2, 0, 0.8))
cts[, cond=="B"] <- matrix(rnbinom(n*n_per, mu=100*2^rep(beta,n_per), size=1/0.1), ncol=n_per)
mode(cts) <- "integer"
dds <- DESeqDataSetFromMatrix(cts, S4Vectors::DataFrame(cond=cond), ~cond)
dds <- DESeq(dds, quiet=TRUE)
res <- results(dds)  # plain, for LFC and SE
T <- 0.585  # |FC|>1.5, a common published choice
LFC <- res$log2FoldChange; SE <- res$lfcSE
p2014 <- pmin(1, 2*pnorm((abs(LFC)-T)/SE, lower.tail=FALSE))
p2024 <- pnorm(-abs(LFC)+T, sd=SE) + pnorm(-abs(LFC)-T, sd=SE)
ok <- !is.na(p2014)
padj2014 <- p.adjust(p2014[ok], "BH"); padj2024 <- p.adjust(p2024[ok], "BH")
cat(sprintf("  threshold T=%.3f (FC 1.5): significant padj<0.05: old %d vs new %d (+%.0f%%)\n",
            T, sum(padj2014<0.05), sum(padj2024<0.05),
            100*(sum(padj2024<0.05)/max(1,sum(padj2014<0.05))-1)))
flip <- sum((padj2014<0.05) != (padj2024<0.05))
cat(sprintf("  genes whose call flips across the version boundary: %d (%.1f%% of tested)\n",
            flip, 100*flip/sum(ok)))
q <- quantile((p2014/p2024)[ok & p2024>0], c(.5,.9,.99), na.rm=TRUE)
cat(sprintf("  p-ratio old/new: median %.2f  90th %.2f  99th %.2f\n", q[1], q[2], q[3]))
