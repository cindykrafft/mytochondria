#!/usr/bin/env Rscript
# scDblFinder end to end on simulated data with known doublets and known origins:
# doublet calls (recall, false discovery, AUC) and the reported mostLikelyOrigin
# of the true doublets, with the installed createDoublets and with the corrected
# one (see d2). Cluster-based mode (clusters given), the mode in which origins exist.
# Usage: Rscript d3_end_to_end_origins.R [libPath]
args <- commandArgs(trailingOnly=TRUE)
if(length(args)>0) .libPaths(c(args[1], .libPaths()))
suppressPackageStartupMessages({library(scDblFinder); library(SingleCellExperiment); library(Matrix)})
cat("scDblFinder", as.character(packageVersion("scDblFinder")), "\n")
ok <- function(label, cond, detail=""){ cat(if(isTRUE(cond)) "ok  " else "FAIL", label, detail, "\n") }
source("createDoubletsFixed.R")
ns <- asNamespace("scDblFinder"); orig_fun <- ns$createDoublets
swap <- function(f){ unlockBinding("createDoublets", ns); assign("createDoublets", f, envir=ns); lockBinding("createDoublets", ns) }
auc <- function(score, truth){ r <- rank(score); n1 <- sum(truth); n0 <- sum(!truth); (sum(r[truth]) - n1*(n1+1)/2)/(n1*n0) }

# simulated capture: 5 cell types, 3000 singlets, 6 % doublets (heterotypic and homotypic, Poisson from the summed means)
set.seed(21)
ncl <- c(A=900, B=800, C=600, D=450, E=250); ng <- 800
mus <- lapply(names(ncl), function(k) 2^rnorm(ng, -1.5, 1.6)); names(mus) <- names(ncl)
sce <- mockDoubletSCE(ncells=ncl, ngenes=ng, mus=mus, dbl.rate=0.06, only.heterotypic=FALSE)
truth_dbl <- sce$type == "doublet"
truth_origin <- as.character(sce$origin); truth_origin[!truth_dbl] <- NA
canon <- function(o){ o <- as.character(o); w <- which(!is.na(o)); o[w] <- sapply(strsplit(o[w], "+", fixed=TRUE), function(p) paste(sort(p), collapse="+")); o }
truth_origin <- canon(truth_origin)
cat(sprintf("   %d cells, %d doublets (%.1f %%), %d heterotypic, clusters given as the true cell types (homotypic doublets carry their type's label)\n", ncol(sce), sum(truth_dbl), 100*mean(truth_dbl), sum(truth_dbl & grepl("\\+", truth_origin) & !sapply(strsplit(truth_origin, "+", fixed=TRUE), function(p) length(p)==2 && p[1]==p[2]))))
hetero <- truth_dbl & !is.na(truth_origin) & sapply(strsplit(truth_origin, "+", fixed=TRUE), function(p) length(p)==2 && p[1]!=p[2])

run <- function(label, fixed){
  swap(if(fixed) createDoubletsFixed else orig_fun)
  set.seed(5)
  res <- scDblFinder(sce, clusters=sce$cluster, verbose=FALSE)
  swap(orig_fun)
  called <- res$scDblFinder.class == "doublet"
  o <- canon(res$scDblFinder.mostLikelyOrigin)
  acc <- mean(o[hetero] == truth_origin[hetero], na.rm=TRUE)
  acc_called <- mean(o[hetero & called] == truth_origin[hetero & called], na.rm=TRUE)
  st <- metadata(res)$scDblFinder.stats
  cat(sprintf("   %s: called %d (%.1f %%); recall %.3f; FDR %.3f; AUC %.4f; threshold %.3f\n", label, sum(called), 100*mean(called), sum(called & truth_dbl)/sum(truth_dbl), sum(called & !truth_dbl)/sum(called), auc(res$scDblFinder.score, truth_dbl), metadata(res)$scDblFinder.threshold))
  cat(sprintf("   %s: mostLikelyOrigin correct for %.1f %% of the %d heterotypic doublets (%.1f %% of the called ones); originAmbiguous on %.1f %%\n", label, 100*acc, sum(hetero), 100*acc_called, 100*mean(res$scDblFinder.originAmbiguous[hetero], na.rm=TRUE)))
  if(!is.null(st)){
    st$truth <- as.numeric(table(factor(truth_origin[hetero], levels=st$combination)))
    cat(sprintf("   %s: stats table (expected / observed / truth) for the %d combinations: sum|observed - truth| = %d\n", label, nrow(st), sum(abs(st$observed - st$truth))))
    print(head(st[order(-st$truth), c("combination","expected","observed","truth","difficulty")], 6))
  }
  list(acc=acc, called=called, score=res$scDblFinder.score, origin=o, st=st)
}
a <- run("installed createDoublets", FALSE)
b <- run("corrected createDoublets", TRUE)
ok("installed: mostLikelyOrigin of the heterotypic doublets is right at least 90 % of the time", a$acc >= 0.9, sprintf("(%.1f %%)", 100*a$acc))
ok("corrected: mostLikelyOrigin of the heterotypic doublets is right at least 90 % of the time", b$acc >= 0.9, sprintf("(%.1f %%)", 100*b$acc))
cat(sprintf("   calls that differ between the two runs: %d of %d cells; score correlation %.4f\n", sum(a$called != b$called), length(a$called), cor(a$score, b$score)))
