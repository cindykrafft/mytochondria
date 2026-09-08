#!/usr/bin/env Rscript
# Held-up check by simulation: type I error and FDR of the four tests the cohort runs,
# on NB data with a dispersion trend and known truth.
#   pipeline: DGEList -> filterByExpr -> normLibSizes -> estimateDisp -> {glmQLFit/glmQLFTest,
#             glmFit/glmLRT, exactTest}; topTags FDR (BH).
# Null data: no DE genes; report the fraction of raw p < 0.05 and < 0.01.
# DE data: 10 % of genes at 2-fold; report discoveries and empirical FDR at BH 5 %.
suppressMessages(library(edgeR))
cat("edgeR", as.character(packageVersion("edgeR")), " limma", as.character(packageVersion("limma")), "\n")
legacy_arg <- "legacy" %in% names(formals(edgeR:::glmQLFit.DGEList))
sim <- function(seed, n1, n2, G=8000, de=0, regime="typical") {
  set.seed(seed)
  n <- n1 + n2
  group <- factor(rep(c("A", "B"), c(n1, n2)))
  L <- runif(n, 8e6, 2.5e7)
  mu0 <- exp(rnorm(G, 4.5, 2))
  if (regime == "typical") {
    # BCV ~ 0.2 for well-measured genes, rising for low counts (a typical inbred-mouse experiment)
    phi <- 0.04 * exp(rnorm(G, 0, 0.3)) + 1/mu0
  } else if (regime == "moderate") {
    # BCV ~ 0.4 (human tissue samples)
    phi <- 0.16 * exp(rnorm(G, 0, 0.3)) + 1/mu0
  } else {
    # harsh: BCV 0.3-1 at moderate counts, small counts
    mu0 <- exp(rnorm(G, 3, 2)); phi <- 0.1 + 2/sqrt(mu0) * exp(rnorm(G, 0, 0.4))
  }
  isde <- seq_len(G) <= round(de*G)
  fc <- ifelse(isde, 2^(sample(c(-1, 1), G, TRUE) * sample(c(1, 2), G, TRUE)), 1)   # 2- or 4-fold, either direction
  mu <- outer(mu0, L/1e6); mu[, group == "B"] <- mu[, group == "B"]*fc[row(mu[, group == "B"])]
  y <- matrix(rnbinom(G*n, mu=mu, size=1/phi), G, n)
  d <- DGEList(y, group=group)
  keep <- filterByExpr(d, group=group)
  d <- d[keep, , keep.lib.sizes=FALSE]
  d <- normLibSizes(d)
  design <- model.matrix(~group)
  d <- estimateDisp(d, design)
  res <- list()
  fq <- glmQLFit(d, design); res$QL <- glmQLFTest(fq, coef=2)$table$PValue
  if (legacy_arg) { fl <- glmQLFit(d, design, legacy=TRUE); res$QL.legacy <- glmQLFTest(fl, coef=2)$table$PValue }
  res$LRT <- glmLRT(glmFit(d, design), coef=2)$table$PValue
  res$exact <- exactTest(d)$table$PValue
  list(p=res, isde=isde[keep])
}
report <- function(n1, n2, de, nrep=8, regime="typical") {
  out <- NULL
  for (s in 1:nrep) {
    r <- sim(100*s + n1, n1, n2, de=de, regime=regime)
    for (t in names(r$p)) {
      p <- r$p[[t]]; fdr <- p.adjust(p, "BH") < 0.05
      out <- rbind(out, data.frame(test=t, p05=mean(p < 0.05), p01=mean(p < 0.01), ndisc=sum(fdr),
                                   efdr=if (sum(fdr)) mean(!r$isde[fdr]) else 0, power=if (de > 0) mean(fdr[r$isde]) else NA))
    }
  }
  agg <- aggregate(out[, -1], list(test=out$test), mean)
  cat(sprintf("\n[%s dispersions] %d vs %d samples, %d%% DE genes (%d replicates, ~8000 genes before filtering):\n", regime, n1, n2, round(100*de), nrep))
  cat(sprintf("  %-10s %8s %8s %8s %8s %8s\n", "test", "P(p<.05)", "P(p<.01)", "BH<.05", "FDR", "power"))
  for (i in seq_len(nrow(agg))) cat(sprintf("  %-10s %8.4f %8.4f %8.1f %8.3f %8.3f\n", agg$test[i], agg$p05[i], agg$p01[i], agg$ndisc[i], agg$efdr[i], agg$power[i]))
}
cat("P(p<.05)/P(p<.01): fraction of genes with raw p below the level (on null data: type I error rate);\n",
    "BH<.05: mean number of genes with BH-adjusted p < 0.05; FDR: mean fraction of those that are not DE; power: fraction of DE genes found\n")
report(3, 3, 0)
report(2, 2, 0)
report(3, 3, 0.1)
report(2, 2, 0.1)
report(5, 5, 0.1)
report(3, 3, 0, regime="moderate")
report(3, 3, 0.1, regime="moderate")
report(3, 3, 0, regime="harsh", nrep=16)
report(3, 3, 0.1, regime="harsh", nrep=16)
report(5, 5, 0.1, regime="harsh", nrep=16)
