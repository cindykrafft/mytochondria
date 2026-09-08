## CP4 version scope: the same tiny design as gsea_exact_small.R (N = 24, set {8, 12, 16}; exact
## same-sign p = 0.8824, exact unconditional P(ES* >= ES) = 0.4521) through each enrichit release.
## Usage: for each library: R_LIBS_USER=<lib-enrichit-x.y.z>:<lib> Rscript cp4_versions.R
suppressPackageStartupMessages(library(enrichit))
set.seed(124); stats <- sort(rnorm(24), decreasing = TRUE); names(stats) <- sprintf("g%02d", 1:24)
one <- list(mid = names(stats)[c(8, 12, 16)])
s <- suppressWarnings(gsea(stats, one, minGSSize = 1, maxGSSize = 23, method = "sample", nPerm = 2e5, seed = 5, verbose = FALSE))
p <- suppressWarnings(gsea(stats, one, minGSSize = 1, maxGSSize = 23, method = "permute", nPerm = 5e4, seed = 6, verbose = FALSE))
m <- suppressWarnings(gsea(stats, one, minGSSize = 1, maxGSSize = 23, method = "multilevel", eps = 0, seed = 7, verbose = FALSE))
cat(sprintf("enrichit %s: ES=%.4f  sample p=%.4f  permute p=%.4f  multilevel p=%.4f   (exact same-sign 0.8824; unconditional 0.4521)\n",
            as.character(packageVersion("enrichit")), s$enrichmentScore, s$pvalue, p$pvalue, m$pvalue))
