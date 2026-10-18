## fgsea 1.38.0 (Bioconductor 3.23 release) and master 1.39.4 differ only in docs/CI/RcppExports
## names (git diff RELEASE_3_23..devel); confirm they return identical numbers.
## Usage: Rscript v0_release_equals_master.R <lib-1.38.0> <lib-master> <deps lib>
a <- commandArgs(TRUE)
run <- function(lib) {
    cmd <- sprintf("suppressPackageStartupMessages(library(fgsea, lib.loc='%s')); data(examplePathways); data(exampleRanks); set.seed(42); r <- fgsea(examplePathways, exampleRanks, minSize=15, maxSize=500, BPPARAM=BiocParallel::SerialParam()); saveRDS(list(v=as.character(packageVersion('fgsea', lib.loc='%s')), r=r), '%s/out.rds')", lib, lib, lib)
    system2("Rscript", c("-e", shQuote(cmd)), env = paste0("R_LIBS=", a[3]))
    readRDS(file.path(lib, "out.rds"))
}
x <- run(a[1]); y <- run(a[2])
cat("versions:", x$v, y$v, "\n")
cat("pathways:", nrow(x$r), nrow(y$r), "; identical pval/padj/log2err/ES/NES/size/leadingEdge:",
    identical(x$r$pval, y$r$pval), identical(x$r$padj, y$r$padj), identical(x$r$log2err, y$r$log2err),
    identical(x$r$ES, y$r$ES), identical(x$r$NES, y$r$NES), identical(x$r$size, y$r$size), identical(x$r$leadingEdge, y$r$leadingEdge), "\n")
