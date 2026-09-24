#!/usr/bin/env Rscript
# metadata(sce)$scDblFinder.stats: is the "observed" column (doublets called per
# cluster combination) filled in when clusters are given as cell-type names, as
# numeric strings (Seurat-style "0","1",...), and as integers 1..k?
# Usage: Rscript d4_stats_cluster_labels.R [libPath]
args <- commandArgs(trailingOnly=TRUE)
if(length(args)>0) .libPaths(c(args[1], .libPaths()))
suppressPackageStartupMessages({library(scDblFinder); library(SingleCellExperiment)})
cat("scDblFinder", as.character(packageVersion("scDblFinder")), "\n")
ok <- function(label, cond, detail=""){ cat(if(isTRUE(cond)) "ok  " else "FAIL", label, detail, "\n") }
set.seed(21)
ncl <- c(A=700, B=600, C=400, D=300); ng <- 600
mus <- lapply(names(ncl), function(k) 2^rnorm(ng, -1.5, 1.6)); names(mus) <- names(ncl)
sce <- mockDoubletSCE(ncells=ncl, ngenes=ng, mus=mus, dbl.rate=0.06, only.heterotypic=TRUE)
labels <- list("cell-type names (A..D)"=as.character(sce$cluster),
               "numeric strings (0..3)"=as.character(as.integer(sce$cluster) - 1L),
               "integers 1..k"=as.integer(sce$cluster),
               "factor with names"=sce$cluster)
for(nm in names(labels)){
  set.seed(5); res <- scDblFinder(sce, clusters=labels[[nm]], verbose=FALSE)
  st <- metadata(res)$scDblFinder.stats; called <- sum(res$scDblFinder.class == "doublet")
  o <- res$scDblFinder.mostLikelyOrigin[res$scDblFinder.class == "doublet"]
  cat(sprintf("   clusters as %s: %d doublets called; stats combinations %s; sum(observed) = %d; origins of the called doublets e.g. %s\n", nm, called, paste(head(st$combination, 3), collapse=","), sum(st$observed), paste(head(unique(as.character(o)), 3), collapse=",")))
  ok(sprintf("clusters as %s: scDblFinder.stats$observed sums to the number of called doublets with an origin", nm), sum(st$observed) == sum(!is.na(o)), sprintf("(%d vs %d)", sum(st$observed), sum(!is.na(o))))
}
