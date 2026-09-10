# fitFDistUnequalDF1 (the squeezeVar default when residual df differ between genes, e.g. with
# missing values) on the shipped build: the returned (scale, df2) vs an independent maximiser of
# the scaled-F log-likelihood written from the density, and recovery of planted d0/s0.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(31)
G <- 6000; d0 <- 6; s02 <- 0.2
df1 <- sample(c(3,4,5,6), G, replace=TRUE)
s2 <- s02*d0/rchisq(G, d0) * rchisq(G, df1)/df1          # s^2 ~ s0^2 F(df1, d0)
ff <- fitFDistUnequalDF1(s2, df1)
cat(sprintf("[fitFDistUnequalDF1] df2 %.4f (truth %d), scale %.5f (truth %.2f)\n", ff$df2, d0, ff$scale, s02))
# independent maximum likelihood over (log d2, log s02): log density of s2 = s02 * F(df1, df2)
nll <- function(par) { d2 <- exp(par[1]); sc <- exp(par[2]); x <- s2/sc
  -sum(df(x, df1, d2, log=TRUE) - log(sc)) }
o <- optim(c(log(4), log(0.3)), nll, method="BFGS", control=list(reltol=1e-14))
cat(sprintf("  ML by optim: df2 %.4f scale %.5f; log-lik at limma's (df2,scale) minus at optim's: %.2e\n", exp(o$par[1]), exp(o$par[2]), -(nll(c(log(ff$df2), log(ff$scale))) - o$value)))
# compare with the moment estimator on equal-df data and with squeezeVar dispatch
df1e <- rep(5, G); s2e <- s02*d0/rchisq(G, d0) * rchisq(G, 5)/5
fm <- fitFDist(s2e, 5); fu <- fitFDistUnequalDF1(s2e, 5)
cat(sprintf("[equal df] moments: df2 %.4f scale %.5f; ML: df2 %.4f scale %.5f; squeezeVar(legacy=NULL) uses %s\n", fm$df2, fm$scale, fu$df2, fu$scale,
  if(isTRUE(all.equal(squeezeVar(s2e, 5)$df.prior, fm$df2))) "moments (legacy)" else "ML"))
sv <- squeezeVar(s2, df1); cat(sprintf("[squeezeVar unequal df] df.prior equals fitFDistUnequalDF1: %s; var.post formula %.1e\n", isTRUE(all.equal(sv$df.prior, ff$df2)), max(abs(sv$var.post - (df1*s2+ff$df2*ff$scale)/(df1+ff$df2)))))
# robust path with unequal df: outliers get smaller df.prior
s2o <- s2; out <- sample(G, 60); s2o[out] <- s2o[out]*30
fr <- fitFDistUnequalDF1(s2o, df1, robust=TRUE); fn <- fitFDistUnequalDF1(s2o, df1)
cat(sprintf("[robust, 60 planted outliers] non-robust df2 %.3f; robust df2 %.3f (truth %d); df2.shrunk median %.3f, median over outliers %.3f, outliers below the median: %d/60\n",
  fn$df2, fr$df2, d0, median(fr$df2.shrunk), median(fr$df2.shrunk[out]), sum(fr$df2.shrunk[out] < median(fr$df2.shrunk)-1e-8)))
# through eBayes with missing values (unequal residual df) -> this estimator
n <- 8; design <- cbind(1, rep(0:1, each=4)); y <- matrix(rnorm(G*n), G, n)*sqrt(s02*d0/rchisq(G,d0)); y[sample(length(y), 3000)] <- NA
fit <- lmFit(y, design); eb <- eBayes(fit)
ok <- fit$df.residual > 0
ref <- fitFDistUnequalDF1(fit$sigma[ok]^2, fit$df.residual[ok])
cat(sprintf("[eBayes with NAs] df.residual range %d-%d; df.prior %.4f (truth %d); equals fitFDistUnequalDF1 on df>0 genes: %s\n", min(fit$df.residual), max(fit$df.residual), eb$df.prior, d0, isTRUE(all.equal(eb$df.prior, ref$df2))))
