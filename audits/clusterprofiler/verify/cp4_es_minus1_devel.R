suppressPackageStartupMessages(library(enrichit))
cat("enrichit", as.character(packageVersion("enrichit")), "\n")
res <- list()
for (s in 1:5) {
  set.seed(s)
  stats <- sort(setNames(rnorm(24), sprintf("g%02d", 1:24)), decreasing = TRUE)
  for (side in c("top","bottom")) {
    ix <- if (side == "top") 1:3 else 22:24
    gs <- list(S = names(stats)[ix])
    # exact null: every 3-gene set, same ES definition (weighted KS, p = 1)
    es_of <- function(idx) { hit <- seq_along(stats) %in% idx; w <- abs(stats) * hit
      run <- cumsum(ifelse(hit, w / sum(w), -1 / (length(stats) - length(idx)))); run[which.max(abs(run))] }
    null <- apply(combn(24, 3), 2, es_of); es <- es_of(ix)
    p_exact <- if (es > 0) mean(null[null > 0] >= es) else mean(null[null < 0] <= es)
    r <- suppressWarnings(as.data.frame(gsea(stats, gs, minGSSize = 1, maxGSSize = 23,
           method = "sample", nPerm = 2e5, seed = 5, verbose = FALSE)))
    cat(sprintf("seed %d %-6s ES=%+.4f  exact same-sign p=%.6f  sample p=%.2e\n", s, side, r$enrichmentScore, p_exact, r$pvalue))
  }
}
