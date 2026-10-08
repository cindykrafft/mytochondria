library(enrichit)
set.seed(1)
stats <- sort(setNames(rnorm(24), sprintf("g%02d", 1:24)), decreasing = TRUE)
es_of <- function(idx) { hit <- seq_along(stats) %in% idx; w <- abs(stats) * hit
  run <- cumsum(ifelse(hit, w / sum(w), -1 / (24 - length(idx)))); run[which.max(abs(run))] }
null <- apply(combn(24, 3), 2, es_of)                  # exact null: all 2,024 three-gene sets
p_exact <- mean(null[null < 0] <= -1)                  # same-sign p for ES = -1
run <- function(...) suppressWarnings(as.data.frame(gsea(stats, list(S = names(stats)[22:24]),
  minGSSize = 1, maxGSSize = 23, nPerm = 2e5, seed = 5, verbose = FALSE, ...)))$pvalue
signif(c(exact = p_exact, sample = run(method = "sample"),
         sample_adaptive = run(method = "sample", adaptive = TRUE),
         permute = run(method = "permute"), multilevel = run(method = "multilevel")), 3)
