## A gene set holding the top k genes of a list whose top scores repeat (ES = 1).  fgsea 1.20/1.30
## do not return (issue #151); 1.32-1.36 return with an overestimated p ("gracefully fail",
## 7282d85); 1.37.1+ (hash tie-breaking) return the exact value.  Run under `timeout`.
## Usage: R_LIBS=<fgsea lib>:<deps lib> timeout 300 Rscript v6_es1_hang.R [eps, default 0]
suppressPackageStartupMessages({library(fgsea); library(BiocParallel)})
cat("fgsea", as.character(packageVersion("fgsea")), "\n")
set.seed(20261018)
z <- sort(rnorm(1000), decreasing = TRUE)
st <- sign(z) * pmin(pmax(ceiling(abs(z) * 1.5), 1), 4)       # integer scores 1..4, many ties
names(st) <- sprintf("g%04d", seq_along(st))
k <- 15
cat("top", k, "scores:", st[1:k], "\n")
cat("exact p = 1 / choose(1000, 15) / P(ES >= 0) =", signif(1 / choose(1000, 15) / 0.5084, 4), "(P(ES >= 0) = 0.5084 from v3)\n")
t0 <- Sys.time()
set.seed(1)
EPS <- if (length(commandArgs(TRUE))) as.numeric(commandArgs(TRUE)[1]) else 0
cat("eps =", EPS, "\n")
r <- suppressWarnings(fgseaMultilevel(list(top = names(st)[1:k]), st, eps = EPS, BPPARAM = SerialParam()))
cat(sprintf("returned after %.1f s: ES = %g, pval = %.3g, log2err = %s\n", as.numeric(Sys.time() - t0, units = "secs"), r$ES, r$pval, format(r$log2err)))
