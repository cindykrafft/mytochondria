## Is fgsea's output a function of set.seed() alone, whatever the parallel back-end?
## And what does the package's own reproducibility test actually compare?
## Usage: R_LIBS=<fgsea lib>:<deps lib> Rscript v5_reproducibility.R
suppressPackageStartupMessages({library(fgsea); library(BiocParallel); library(data.table)})
## nproc > 0 turns on BiocParallel progress bars; send them to a null connection
zz <- file(nullfile(), open = "wt"); sink(zz, type = "message")
cat("fgsea", as.character(packageVersion("fgsea")), " BiocParallel", as.character(packageVersion("BiocParallel")), "\n")
data(examplePathways); data(exampleRanks)
run <- function(...) { set.seed(42); suppressWarnings(fgsea(examplePathways, exampleRanks, minSize = 15, maxSize = 500, ...)) }
r0 <- run(BPPARAM = SerialParam())
cmp <- function(lab, r) cat(sprintf("%-34s identical pval: %s  identical NES: %s  max |log2 p ratio| vs serial: %.3g\n", lab,
    identical(r$pval, r0$pval), identical(r$NES, r0$NES), max(abs(log2(r$pval / r0$pval)), na.rm = TRUE)))
cmp("nproc = 1", run(nproc = 1))
cmp("nproc = 2", run(nproc = 2))
cmp("nproc = 4", run(nproc = 4))
cmp("default bpparam()", run())
cmp("SnowParam(2)", run(BPPARAM = SnowParam(2)))
set.seed(43); r43 <- suppressWarnings(fgsea(examplePathways, exampleRanks, minSize = 15, maxSize = 500, BPPARAM = SerialParam()))
cat(sprintf("%-34s identical pval: %s  max |log2 p ratio| vs seed 42: %.3g (median %.3g)\n", "different seed (43)",
    identical(r43$pval, r0$pval), max(abs(log2(r43$pval / r0$pval))), median(abs(log2(r43$pval / r0$pval)))))
## fgseaSimple
s <- function(...) { set.seed(42); fgseaSimple(examplePathways, exampleRanks, nperm = 10000, minSize = 15, maxSize = 500, ...)$pval }
s0 <- s(BPPARAM = SerialParam())
cat("fgseaSimple nproc = 2 identical:", identical(s(nproc = 2), s0), "; default bpparam identical:", identical(s(), s0), "\n")
## the package test "fgseaMultilevel is reproducable independent of bpparam settings" compares $nMoreExtreme
set.seed(42); fr <- fgseaMultilevel(examplePathways[1:2], exampleRanks, sampleSize = 50, maxSize = 500, nproc = 1)
cat("columns of fgseaMultilevel():", paste(names(fr), collapse = ", "), "\n")
cat("fr$nMoreExtreme is NULL:", is.null(fr$nMoreExtreme), " -> expect_equal(NULL, NULL) passes for any p-values\n")
cat("setUpBPPARAM(nproc = 1) class:", class(fgsea:::setUpBPPARAM(nproc = 1))[1], "(the SerialParam branch is overwritten)\n")
