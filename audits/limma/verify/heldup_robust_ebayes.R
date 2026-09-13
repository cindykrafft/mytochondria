# Held-up / sanity checks for robust empirical Bayes (Phipson et al 2016): with no outliers the
# robust and non-robust hyperparameters agree; planted variance outliers get gene-specific
# df.prior shrunk towards zero, monotone in the tail probability, and lose their false
# discoveries; the same on the unequal-df estimator. Run: . ./rlib.sh <version>; Rscript heldup_robust_ebayes.R
suppressMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), R.version.string, "\n")
set.seed(91)
G <- 10000; n <- 8; d0 <- 5; s0 <- 0.04
design <- cbind(1, rep(0:1, each=4))
s2 <- s0*d0/rchisq(G, d0)
y <- matrix(rnorm(G*n, sd=rep(sqrt(s2), n)), G, n) + rnorm(G, 8, 2)
fit <- lmFit(y, design)
e0 <- eBayes(fit); r0 <- eBayes(fit, robust=TRUE)
cat(sprintf("A. no outliers: df.prior %.4f (robust: min %.4f, max %.4f) ; s2.prior %.5f vs %.5f (true %g, %g)\n", e0$df.prior, min(r0$df.prior), max(r0$df.prior), e0$s2.prior, r0$s2.prior, d0, s0))
# 200 hypervariable genes (variance 30x) and 100 genes with one wild observation
out <- 1:200; yo <- y
yo[out,] <- matrix(rnorm(200*n, sd=rep(sqrt(30*s2[out]), n)), 200, n) + rowMeans(y[out,])
wild <- 201:300; yo[wild, 3] <- yo[wild, 3] + 6*sqrt(s2[wild])
fo <- lmFit(yo, design); e1 <- eBayes(fo); r1 <- eBayes(fo, robust=TRUE)
cat(sprintf("B. with outliers: non-robust df.prior %.4f s2.prior %.5f ; robust df.prior (non-outlier genes) %.4f s2.prior %.5f ; robust df.prior on the 200 hypervariable genes: median %.3f, min %.3f\n",
            e1$df.prior, e1$s2.prior, median(r1$df.prior[-(1:300)]), r1$s2.prior, median(r1$df.prior[out]), min(r1$df.prior[out])))
tp <- pf(fo$sigma^2/r1$s2.prior, n-2, median(r1$df.prior[-(1:300)]), lower.tail=FALSE)
cat(sprintf("   df.prior monotone non-decreasing in the F tail probability: %s\n", !is.unsorted(r1$df.prior[order(tp)])))
fp <- function(e) sum(p.adjust(e$p.value[,2], "BH") < 0.05)          # all genes are null for the group coefficient
cat(sprintf("   false discoveries at adj.P<0.05 (all null): non-robust %d, robust %d ; among the wild-observation genes: %d vs %d\n", fp(e1), fp(r1), sum(p.adjust(e1$p.value[,2], "BH")[wild] < 0.05), sum(p.adjust(r1$p.value[,2], "BH")[wild] < 0.05)))
if("legacy" %in% names(formals(eBayes))) {
  r2 <- eBayes(fo, robust=TRUE, legacy=FALSE)
  dp2 <- rep_len(r2$df.prior, G)
  cat(sprintf("C. unequal-df estimator (legacy=FALSE) robust: df.prior length %d (non-outlier %.4f, hypervariable median %.3f), s2.prior %.5f ; false discoveries %d\n",
              length(r2$df.prior), median(dp2[-(1:300)]), median(dp2[out]), r2$s2.prior, fp(r2)))
  cat(sprintf("   hypervariable genes: median s2.post/sigma^2 legacy-robust %.3f, unequal-df-robust %.3f, non-robust %.3f (true variance ratio to the prior scale: 30)\n",
              median(r1$s2.post[out]/fo$sigma[out]^2), median(r2$s2.post[out]/fo$sigma[out]^2), median(e1$s2.post[out]/fo$sigma[out]^2)))
}
# winsor.tail.p and trend
r3 <- eBayes(fo, robust=TRUE, trend=TRUE)
cat(sprintf("D. robust+trend: s2.prior range %.5f..%.5f, df.prior non-outlier %.4f\n", min(r3$s2.prior), max(r3$s2.prior), median(r3$df.prior[-(1:300)])))
