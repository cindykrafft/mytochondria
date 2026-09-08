#!/usr/bin/env Rscript
# Note: where glmQLFit(legacy=FALSE) takes its NB dispersion from, by version.
# NEWS 4.4.0: "the DGEList method for glmQLFit() with legacy=FALSE will take the dispersion
#   from the mean of the right tail values of the trended dispersions, instead of
#   re-estimating, if these are found in the DGEList object."
# NEWS 4.10.0: "glmQLFit() with legacy=FALSE no longer automatically estimates the NB dispersion
#   from trended values found in the DGEList object, if present. The results will now be the
#   same whether the DGEList contains dispersion estimates or not."
# The User's Guide pipeline runs estimateDisp() before glmQLFit(), so on 4.4-4.8 the QL
# p-values depended on that call; this harness sizes the difference.
suppressMessages(library(edgeR))
cat("edgeR", as.character(packageVersion("edgeR")), "\n")
set.seed(8)
G <- 6000; n <- 6
group <- factor(rep(c("A", "B"), each=3)); design <- model.matrix(~group)
L <- runif(n, 8e6, 2e7)
mu0 <- exp(rnorm(G, 4, 2)); phi <- 0.05 + 2/sqrt(mu0)
fc <- ifelse(seq_len(G) <= 600, 2^sample(c(-1, 1), G, TRUE), 1)
mu <- outer(mu0, L/1e6); mu[, 4:6] <- mu[, 4:6]*fc
y <- matrix(rnbinom(G*n, mu=mu, size=1/phi), G, n)
d <- DGEList(y, group=group); d <- d[filterByExpr(d, group=group), , keep.lib.sizes=FALSE]; d <- normLibSizes(d)
d2 <- estimateDisp(d, design)
if ("legacy" %in% names(formals(edgeR:::glmQLFit.DGEList))) {
  f1 <- glmQLFit(d, design, legacy=FALSE); f2 <- glmQLFit(d2, design, legacy=FALSE)
} else {
  f1 <- glmQLFit(d, design, dispersion=estimateGLMCommonDisp(d, design)); f2 <- glmQLFit(d2, design)
}
p1 <- glmQLFTest(f1, coef=2)$table$PValue; p2 <- glmQLFTest(f2, coef=2)$table$PValue
cat("NB dispersion used by glmQLFit: without estimateDisp", signif(unique(f1$dispersion)[1], 5), " (length", length(f1$dispersion), ");",
    "after estimateDisp", signif(unique(f2$dispersion)[1], 5), " (length", length(f2$dispersion), ")\n")
cat("QL p-values identical with/without a prior estimateDisp():", isTRUE(all.equal(p1, p2)),
    "; genes with BH<0.05:", sum(p.adjust(p1, "BH") < 0.05), "vs", sum(p.adjust(p2, "BH") < 0.05),
    "; max |log10 p ratio|", signif(max(abs(log10(p1/p2))), 3), "\n")
# Remaining dependence: estimateDisp() stores y$AveLogCPM computed at the common dispersion,
# while glmQLFit() on a fresh DGEList computes it at the default dispersion 0.05; the QL trend
# covariate therefore differs slightly. Equalising it should make the p-values identical.
cat("max |AveLogCPM difference| between the two fits:", signif(max(abs(f1$AveLogCPM - f2$AveLogCPM)), 3), "\n")
if ("legacy" %in% names(formals(edgeR:::glmQLFit.DGEList))) {
  d3 <- d2; d3$AveLogCPM <- f1$AveLogCPM        # the fresh DGEList's AveLogCPM (dispersion 0.05)
  p3 <- glmQLFTest(glmQLFit(d3, design, legacy=FALSE), coef=2)$table$PValue
  cat("after giving the estimateDisp'ed DGEList the fresh AveLogCPM: p-values identical to the fresh fit:", isTRUE(all.equal(p1, p3)), "\n")
}
# poisson.bound is documented as used only when legacy=TRUE
if ("legacy" %in% names(formals(edgeR:::glmQLFit.DGEList))) {
  pa <- glmQLFTest(f1, coef=2, poisson.bound=TRUE)$table$PValue; pb <- glmQLFTest(f1, coef=2, poisson.bound=FALSE)$table$PValue
  cat("legacy=FALSE: poisson.bound=TRUE vs FALSE identical:", identical(pa, pb), "\n")
}
