## CP4: enrichit::gsea(method = "sample" | "permute") p-values are not conditioned on the sign of the
## permutation ES. Exact null enumerated over all C(24, 3) = 2024 gene sets of size 3.
library(enrichit)
set.seed(124)
stats <- sort(rnorm(24), decreasing = TRUE); names(stats) <- sprintf("g%02d", 1:24)
es_of <- function(idx) { hits <- seq_along(stats) %in% idx
  rs <- cumsum(ifelse(hits, abs(stats), 0)) / sum(abs(stats[hits])) - cumsum(!hits) / (24 - length(idx))
  if (abs(max(rs)) >= abs(min(rs))) max(rs) else min(rs) }
null <- apply(combn(24, 3), 2, es_of)
set <- list(mid = names(stats)[c(8, 12, 16)]); es <- es_of(c(8, 12, 16))
p_same_sign <- mean(null[null >= 0] >= es)      # GSEA convention (Subramanian 2005; fgsea; multilevel)
p_all <- mean(null >= es)                        # unconditional
r <- suppressWarnings(gsea(stats, set, minGSSize = 1, maxGSSize = 23, method = "sample", nPerm = 2e5, seed = 5, verbose = FALSE))
m <- suppressWarnings(gsea(stats, set, minGSSize = 1, maxGSSize = 23, method = "multilevel", eps = 0, seed = 7, verbose = FALSE))
cat(sprintf("enrichit %s: ES = %.4f; exact p (same-sign null) = %.4f; exact P(ES* >= ES) over all sets = %.4f\n", as.character(packageVersion("enrichit")), es, p_same_sign, p_all))
cat(sprintf("gsea(method = 'sample', nPerm = 2e5) p = %.4f   gsea(method = 'multilevel') p = %.4f\n", r$pvalue, m$pvalue))
stopifnot(abs(r$pvalue - p_same_sign) < 0.05)   # expected: the sample method agrees with the multilevel method and the exact same-sign p
