## CP1: with enrichit <= 0.2.1 (CRAN) the GSEA result table of clusterProfiler 4.20.x contains every
## gene set with raw p <= pvalueCutoff, regardless of p.adjust. Minimal: a ranked list with NO signal.
library(clusterProfiler)          # 4.20.0 / 4.21.1.002; engine: enrichit
set.seed(1)
geneList <- sort(setNames(rnorm(5000), paste0("g", 1:5000)), decreasing = TRUE)   # pure noise
term2gene <- data.frame(term = rep(paste0("S", 1:400), each = 40), gene = sample(names(geneList), 16000, replace = TRUE))
term2gene <- unique(term2gene)
x <- suppressWarnings(GSEA(geneList, TERM2GENE = term2gene, pvalueCutoff = 0.05, verbose = FALSE, seed = 1))
res <- as.data.frame(x)
cat("enrichit", as.character(packageVersion("enrichit")), "\n")
cat("rows in the result table:", nrow(res), "  rows with p.adjust > 0.05:", sum(res$p.adjust > 0.05), "  max p.adjust:", round(max(res$p.adjust), 3), "\n")
## expected (clusterProfiler <= 4.18 and enrichit >= 0.2.2): 0 rows (no term has p.adjust <= 0.05 on noise)
stopifnot(all(res$p.adjust <= 0.05))
