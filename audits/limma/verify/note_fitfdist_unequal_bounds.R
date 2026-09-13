# Note N1: fitFDistUnequalDF1 (the squeezeVar/eBayes path taken whenever residual df are
# unequal, e.g. voomLmFit rows with structural zeros or any missing values) maximises the
# profile likelihood over df2/2 in (1, 4999) -> df.prior in (2, 9998). A true prior df below 2
# is floored at 2 and the prior scale then follows from the moment relation at df2=2.
# Run: . ./rlib.sh <version>; Rscript note_fitfdist_unequal_bounds.R
suppressMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), R.version.string, "\n")
if(!exists("fitFDistUnequalDF1", asNamespace("limma"))) { cat("no fitFDistUnequalDF1 in this version: legacy estimator only\n"); quit(status=0) }
set.seed(61)
G <- 20000; s0 <- 0.05
df <- rep(c(4, 6), G/2)                                   # unequal df -> new estimator by default
cat(sprintf("%-8s %-24s %-24s %s\n", "true d0", "new: df.prior  s2.prior", "legacy: df.prior s2.prior", "median s2.post ratio new/legacy"))
for(d0 in c(0.5, 1, 1.5, 2, 3, 6, 20, 100, Inf)) {
  s2true <- if(is.finite(d0)) s0*d0/rchisq(G, d0) else rep(s0, G)
  v <- s2true*rchisq(G, df)/df
  a <- squeezeVar(v, df); b <- squeezeVar(v, df, legacy=TRUE)
  cat(sprintf("%-8s %9.4f   %.5f        %9.4f   %.5f          %.4f\n", format(d0), a$df.prior, a$var.prior, b$df.prior, b$var.prior, median(a$var.post/b$var.post)))
}
# equal df: the default is the legacy estimator; unequal df: the new one
v <- s0*1/rchisq(G, 1)*rchisq(G, 4)/4
cat(sprintf("equal df=4, true d0=1: default df.prior %.4f (legacy) ; legacy=FALSE %.4f\n", squeezeVar(v, 4)$df.prior, squeezeVar(v, 4, legacy=FALSE)$df.prior))
# effect on a moderated t: gene with sample variance 5x the prior scale, df=4
s2 <- 5*s0
for(d0 in c(0.5, 1)) {
  s2true <- s0*d0/rchisq(G, d0); v <- s2true*rchisq(G, df)/df
  a <- squeezeVar(v, df); b <- squeezeVar(v, df, legacy=TRUE)
  pa <- (4*s2 + a$df.prior*a$var.prior)/(4 + a$df.prior); pb <- (4*s2 + b$df.prior*b$var.prior)/(4 + b$df.prior)
  cat(sprintf("true d0=%g: a gene with s2 = 5*s0 and df=4 gets s2.post %.4f (new) vs %.4f (legacy); t-statistic ratio new/legacy %.3f\n", d0, pa, pb, sqrt(pb/pa)))
}
