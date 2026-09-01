## DS-A: results(contrast=) with observation weights uses misaligned weight rows
## Affected: DESeq2 1.16.0 (2017) .. 1.49.x (fixed devel 2025-08-18, abe5994)
## Mechanism: getContrast() subsets counts/dispersions/betas to non-all-zero
## rows (objectNZ) but took weights from the UNSUBSET object; the C++ fitBeta
## then pairs gene i's counts with gene (i + offset)'s weights, where offset
## grows with the number of preceding all-zero rows.
suppressMessages(library(DESeq2))
cat("DESeq2 version:", as.character(packageVersion("DESeq2")), "\n")
set.seed(42)

n <- 2000; m <- 8
cond <- factor(rep(c("A","B"), each=4))
mu <- 100; disp <- 0.1
counts <- matrix(rnbinom(n*m, mu=mu, size=1/disp), ncol=m)
## make ~10% of genes all-zero, scattered through the matrix (common in RNA-seq
## count tables; guaranteed in scRNA/zinbwave workflows, the main users of weights)
zero_rows <- sort(sample(n, n*0.10))
counts[zero_rows,] <- 0L
mode(counts) <- "integer"
dds <- DESeqDataSetFromMatrix(counts, S4Vectors::DataFrame(cond=cond), ~cond)

## zinbwave-style observation weights: most ~1, but per-gene some samples
## strongly downweighted (as zero-inflation posteriors are)
w <- matrix(1, n, m)
downweighted <- matrix(runif(n*m) < 0.15, n, m)
w[downweighted] <- runif(sum(downweighted), 0.005, 0.2)
assays(dds, withDimnames=FALSE)[["weights"]] <- w

dds <- DESeq(dds, quiet=TRUE)

## same coefficient two ways: stored column vs numeric contrast
res_name <- results(dds, name="cond_B_vs_A")
res_ctr  <- results(dds, contrast=c(0,1))   # selects the same coefficient

ok <- !is.na(res_name$pvalue) & !is.na(res_ctr$pvalue)
se_ratio <- res_ctr$lfcSE[ok]/res_name$lfcSE[ok]
p_name <- res_name$pvalue[ok]; p_ctr <- res_ctr$pvalue[ok]
cat(sprintf("genes compared: %d (of %d non-zero)\n", sum(ok), n-length(zero_rows)))
cat(sprintf("lfcSE ratio (contrast/name): median %.4f  [min %.3f, max %.3f]\n",
            median(se_ratio), min(se_ratio), max(se_ratio)))
cat(sprintf("genes with lfcSE differing by >1%%: %d (%.1f%%)  >10%%: %d (%.1f%%)\n",
            sum(abs(se_ratio-1)>0.01), 100*mean(abs(se_ratio-1)>0.01),
            sum(abs(se_ratio-1)>0.10), 100*mean(abs(se_ratio-1)>0.10)))
disc <- (p_name < 0.05) != (p_ctr < 0.05)
cat(sprintf("significance calls at p<0.05 that flip between the two paths: %d (%.2f%%)\n",
            sum(disc), 100*mean(disc)))
cat(sprintf("largest p-value ratio: %.1fx\n", max(pmax(p_ctr/p_name, p_name/p_ctr))))

## control: same comparison with NO all-zero rows present -> paths agree
dds2 <- dds[-zero_rows,]
dds2 <- DESeq(dds2, quiet=TRUE)
r1 <- results(dds2, name="cond_B_vs_A"); r2 <- results(dds2, contrast=c(0,1))
cat(sprintf("control (all-zero rows removed): max |SE ratio - 1| = %.2e\n",
            max(abs(r2$lfcSE/r1$lfcSE - 1), na.rm=TRUE)))

## control 2: no weights, with all-zero rows -> paths agree
dds3 <- DESeqDataSetFromMatrix(counts, S4Vectors::DataFrame(cond=cond), ~cond)
dds3 <- DESeq(dds3, quiet=TRUE)
r3 <- results(dds3, name="cond_B_vs_A"); r4 <- results(dds3, contrast=c(0,1))
cat(sprintf("control (no weights, zeros kept): max |SE ratio - 1| = %.2e\n",
            max(abs(r4$lfcSE/r3$lfcSE - 1), na.rm=TRUE)))
