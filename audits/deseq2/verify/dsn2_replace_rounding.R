## DS-N2: replaceOutliers truncates replacement counts (as.integer = floor for
## positive values). Demonstrate the systematic -0.5 bias on shipped 1.42.1,
## and that round() removes it.
suppressMessages(library(DESeq2))
set.seed(3)
n <- 3000; n_per <- 7; m <- 2*n_per
cond <- factor(rep(c("A","B"), each=n_per))
cts <- matrix(rnbinom(n*m, mu=30, size=1/0.15), ncol=m)
## inject one extreme outlier into 20% of genes
out_genes <- sample(n, n*0.2)
cts[cbind(out_genes, sample(m, length(out_genes), replace=TRUE))] <- 2000L
mode(cts) <- "integer"
dds <- DESeqDataSetFromMatrix(cts, S4Vectors::DataFrame(cond=cond), ~cond)
dds <- DESeq(dds, minReplicatesForReplace=7, quiet=TRUE)

repl <- assays(dds)[["replaceCounts"]]
orig <- counts(dds)
idx <- which(repl != orig)          # the replaced entries
cat(sprintf("replaced entries: %d\n", length(idx)))
## what the code intended: trimmed mean * size factor
trimBaseMean <- apply(counts(dds, normalized=TRUE), 1, mean, trim=0.2)
sf <- sizeFactors(dds)
intended <- outer(trimBaseMean, sf, "*")
shipped_bias <- mean(repl[idx] - intended[idx])
rounded_bias <- mean(as.integer(round(intended[idx])) - intended[idx])
cat(sprintf("shipped (as.integer): mean bias vs intended = %+.3f counts\n", shipped_bias))
cat(sprintf("with round():          mean bias vs intended = %+.3f counts\n", rounded_bias))
cat(sprintf("fraction of replaced entries where the integer differs: %.1f%%\n",
            100*mean(as.integer(intended[idx]) != as.integer(round(intended[idx])))))
