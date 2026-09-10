# Which shipped call paths reach .arrayWeightsPrWtsREML (arrayWeights method="reml" WITH prior
# weights) at default settings?  arrayWeights(method="auto") routes prior weights to
# "genebygene", so the released default paths do not; limma devel's voomLmFit() asks for
# method="reml" explicitly.  Each path is compared with the converged REML solution
# (tol=1e-14) and with genebygene on the same data.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(31)
G <- 4000; n <- 8
design <- cbind(Int=1, Trt=rep(c(0,1), each=4))
qual <- c(1,1,3,1,1,0.5,1,2)
mu <- 2^runif(G, 3, 11)
lam <- outer(mu, rep(1,n)) * exp(matrix(rnorm(G*n,0,0.25),G,n) * rep(qual, each=G))
counts <- matrix(rnbinom(G*n, mu=lam, size=12), G, n)
counts <- counts[rowSums(counts) >= 20, ]
v <- voom(counts, design)
p <- function(x) paste(sprintf("%.4f", x), collapse=" ")
aw.gbg <- arrayWeights(v, design, method="genebygene")
aw.rml <- arrayWeights(v, design, method="reml")
aw.con <- suppressWarnings(arrayWeights(v, design, method="reml", tol=1e-14, maxiter=500))
aw.def <- arrayWeights(v, design)                                  # method="auto"
cat("arrayWeights(v,design) [auto]      :", p(aw.def), "\n")
cat("  == genebygene:", isTRUE(all.equal(aw.def, aw.gbg)), "  == reml(default tol):", isTRUE(all.equal(aw.def, aw.rml)), "\n")
cat("arrayWeights(v,design,method='reml'):", p(aw.rml), "\n")
cat("  converged (tol=1e-14)            :", p(aw.con), "\n")
cat(sprintf("  max |reml(default) - converged| %.4f; max |genebygene - converged| %.4f\n",
            max(abs(aw.rml-aw.con)), max(abs(aw.gbg-aw.con))))
sw.of <- function(e) if(!is.null(e$targets$sample.weight)) e$targets$sample.weight else e$sample.weights
vq  <- voomWithQualityWeights(counts, design)                       # method="genebygene" default
vqr <- voomWithQualityWeights(counts, design, method="reml")
cat("voomWithQualityWeights() default   :", p(sw.of(vq)), "\n")
cat("voomWithQualityWeights(reml)       :", p(sw.of(vqr)), "\n")
cat(sprintf("  max |default - reml| %.4f\n", max(abs(sw.of(vq) - sw.of(vqr)))))
vlf <- if(exists("voomLmFit", where=asNamespace("limma"))) limma::voomLmFit else
       if(requireNamespace("edgeR", quietly=TRUE)) edgeR::voomLmFit else NULL
if(!is.null(vlf)) {
  f <- suppressMessages(vlf(counts, design, sample.weights=TRUE))
  sw <- f$targets$sample.weight
  cat(sprintf("voomLmFit(sample.weights=TRUE) [%s]: %s\n", environmentName(environment(vlf)), p(sw)))
  cat(sprintf("  max |voomLmFit - vwqw(genebygene)| %.4f; max |voomLmFit - vwqw(reml)| %.4f\n",
              max(abs(sw - sw.of(vq))), max(abs(sw - sw.of(vqr)))))
} else cat("voomLmFit not available on this build\n")
