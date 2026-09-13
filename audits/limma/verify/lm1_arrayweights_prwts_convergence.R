# LM1: arrayWeights(method="reml") with prior weights (.arrayWeightsPrWtsREML) stops early.
# Its convergence criterion divides the score-step product by (ngenes+prior.n) a second
# time (the score and information are already per-gene averages), so it is
# (ngenes+prior.n) times smaller than the criterion of .arrayWeightsREML for the same
# state, and the default tol=1e-5 is met after one or two Fisher-scoring steps.
# Truth: with a weight matrix of ones the two routines fit the same model and must
# return the same weights. Run: . ./rlib.sh <version>; Rscript lm1_arrayweights_prwts_convergence.R
suppressMessages(library(limma))
ver <- as.character(packageVersion("limma"))
cat("limma", ver, R.version.string, "\n")
ns <- asNamespace("limma")
if(!exists(".arrayWeightsPrWtsREML", envir=ns)) {
  cat("This version has no .arrayWeightsPrWtsREML (arrayWeights predates the 2019 rewrite): not affected/not present\n")
  quit(status=0)
}

set.seed(1)
G <- 10000; n <- 8
design <- cbind(Int=1, Grp=rep(0:1, each=4))
truew <- c(4,2,1,0.5,4,2,1,0.5)                       # true precision of each array
y <- matrix(rnorm(G*n, sd=rep(sqrt(1/truew), each=G)), G, n) + rnorm(G, 8, 2)
W1 <- matrix(1, G, n)                                  # a no-op prior weight matrix

cat("\n## A. Same model, two code paths (default tol=1e-5, prior.n=10)\n")
a  <- arrayWeights(y, design, method="reml")                       # .arrayWeightsREML
b  <- arrayWeights(y, design, weights=W1, method="reml")           # .arrayWeightsPrWtsREML
b2 <- arrayWeights(y, design, weights=W1, method="reml", tol=1e-5/(G+10))  # tol rescaled by the missing factor
cat("true weights (scaled to geometric mean 1):", format(truew/exp(mean(log(truew))), digits=4), "\n")
cat("REML, no weights            :", format(a, digits=5), "\n")
cat("REML, weights = 1 (PrWts)   :", format(b, digits=5), "\n")
cat("PrWts, tol/(ngenes+prior.n) :", format(b2, digits=5), "\n")
cat(sprintf("max |PrWts - REML| = %.4g   max relative = %.4g\n", max(abs(b-a)), max(abs(b/a-1))))
cat(sprintf("max |PrWts(rescaled tol) - REML| = %.3g\n", max(abs(b2-a))))

cat("\n## B. Iteration traces (convcrit printed by each routine)\n")
cat("REML no weights:\n"); ta <- capture.output(invisible(arrayWeights(y, design, method="reml", trace=TRUE)))
cat(ta, sep="\n")
cat("PrWts weights=1:\n"); tb <- capture.output(invisible(arrayWeights(y, design, weights=W1, method="reml", trace=TRUE)))
cat(tb, sep="\n")
# parse first-iteration convcrit from both traces
num <- function(s) as.numeric(strsplit(trimws(s), " +")[[1]][2])
ca <- num(ta[grep("^1 ", ta)][1]); cb <- num(tb[grep("^1 ", tb)][1])
cat(sprintf("iteration-1 convcrit: REML %.6g  PrWts %.6g  ratio %.2f  (ngenes+prior.n = %d)\n", ca, cb, ca/cb, G+10))
cat(sprintf("iterations used: REML %d  PrWts %d\n", length(grep("^[0-9]+ ", ta)), length(grep("^[0-9]+ ", tb))))

cat("\n## C. Effect on the pipeline: voomWithQualityWeights(method='reml') on counts with two noisy samples\n")
set.seed(2)
G2 <- 8000; n2 <- 8
grp <- rep(0:1, each=4); d2 <- cbind(1, grp)
mu <- rexp(G2, 1/300)
de <- rep(c(1, 2), c(G2*0.9, G2*0.1))                 # 10% genes up 2x in group 2
lambda <- outer(mu, rep(1, n2)) * outer(de, grp, function(a, g) ifelse(g==1, a, 1))
counts <- matrix(rnbinom(G2*n2, mu=lambda, size=20), G2, n2)
noisy <- c(1, 5)                                       # two bad-quality samples
counts[, noisy] <- matrix(rnbinom(G2*2, mu=lambda[, noisy], size=1), G2, 2)
vq <- function(...) voomWithQualityWeights(counts, d2, plot=FALSE, ...)
v_default <- vq(method="reml")                        # default tol -> PrWts path stops early
v_conv    <- vq(method="reml", tol=1e-5/(G2+10))
cat("sample weights, default tol :", format(v_default$targets$sample.weights, digits=4), "\n")
cat("sample weights, converged   :", format(v_conv$targets$sample.weights, digits=4), "\n")
cat(sprintf("max relative difference in sample weights: %.3f\n", max(abs(v_default$targets$sample.weights/v_conv$targets$sample.weights-1))))
nde <- function(v) { tt <- topTable(eBayes(lmFit(v, d2)), coef=2, n=Inf, sort.by="none"); c(sum(tt$adj.P.Val<0.05), sum(tt$adj.P.Val<0.05 & de>1)) }
a1 <- nde(v_default); a2 <- nde(v_conv)
cat(sprintf("genes at adj.P<0.05 (coef 2): default %d (%d true)   converged %d (%d true)   (true DE: %d)\n", a1[1], a1[2], a2[1], a2[2], sum(de>1)))

if(exists("voomLmFit", envir=ns)) {
  cat("\n## D. devel voomLmFit(sample.weights=TRUE) routes to the same path (method='reml' with voom weights)\n")
  msg <- capture.output(f <- voomLmFit(counts, d2, sample.weights=TRUE), type="message")
  cat(msg, sep="\n")
  cat("voomLmFit sample.weight:", format(f$targets$sample.weight, digits=4), "\n")
  cat("voomWithQualityWeights(method='reml') default :", format(v_default$targets$sample.weights, digits=4), "\n")
  cat(sprintf("max |voomLmFit - vWQW(reml, default tol)| = %.3g   max |voomLmFit - converged| = %.3g\n",
              max(abs(f$targets$sample.weight - v_default$targets$sample.weights)),
              max(abs(f$targets$sample.weight - v_conv$targets$sample.weights))))
}
cat("\nVERDICT:", if(max(abs(b-a)) > 0.05) "AFFECTED" else "unaffected", "\n")
