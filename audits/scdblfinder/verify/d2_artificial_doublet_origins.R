#!/usr/bin/env Rscript
# getArtificialDoublets: are the origin labels attached to the right doublets?
# Three clusters with distinct expression profiles; every cross-cluster doublet's
# counts are compared with the three possible sums of cluster means, and the best
# match is compared with the label the function returned. Repeated with the
# default adjustSize=0.25 and with adjustSize=0, and with a corrected createDoublets.
# Usage: Rscript d2_artificial_doublet_origins.R [libPath]
args <- commandArgs(trailingOnly=TRUE)
if(length(args)>0) .libPaths(c(args[1], .libPaths()))
suppressPackageStartupMessages({library(scDblFinder); library(Matrix)})
cat("scDblFinder", as.character(packageVersion("scDblFinder")), "\n")
ok <- function(label, cond, detail=""){ cat(if(isTRUE(cond)) "ok  " else "FAIL", label, detail, "\n") }
set.seed(7)
ng <- 300; ncl <- c(A=400, B=300, C=200)
mus <- lapply(names(ncl), function(k) 2^rnorm(ng, -1, 1.5)); names(mus) <- names(ncl)
x <- do.call(cbind, lapply(names(ncl), function(k) matrix(rpois(ncl[k]*ng, mus[[k]]), ng)))
rownames(x) <- paste0("g", seq_len(ng)); colnames(x) <- paste0("c", seq_len(ncol(x)))
cl <- factor(rep(names(ncl), ncl)); xs <- as(x, "CsparseMatrix")
cm <- sapply(names(ncl), function(k) rowMeans(x[, cl==k]))
combos <- list("A+B"=cm[,"A"]+cm[,"B"], "A+C"=cm[,"A"]+cm[,"C"], "B+C"=cm[,"B"]+cm[,"C"])
best_combo <- function(v){ r <- sapply(combos, function(m) cor(log1p(v), log1p(m))); names(combos)[which.max(r)] }
check <- function(ad, label){
  o <- as.character(ad$origins); w <- which(!is.na(o) & grepl("^A|^B", colnames(ad$counts) == "", fixed=FALSE) | !is.na(o))
  w <- which(!is.na(o) & !grepl("^artMetaDbl|^artTriplet|^rDbl", colnames(ad$counts)))
  bc <- sapply(w, function(i) best_combo(ad$counts[, i]))
  mism <- sum(bc != o[w])
  cat(sprintf("   %s: %d cross-cluster doublets with an origin label, %d (%.1f %%) whose counts match a different pair of clusters\n", label, length(w), mism, 100*mism/length(w)))
  mism/length(w)
}
set.seed(11); ad <- getArtificialDoublets(xs, n=800, clusters=cl)                 # defaults: adjustSize=0.25, halfSize=0.25, resamp=0.25
cat("   default call: ", ncol(ad$counts), "doublets;", sum(grepl("^artMetaDbl", colnames(ad$counts))), "meta-cell,", sum(grepl("^artTriplet", colnames(ad$counts))), "triplet\n")
f_def <- check(ad, "adjustSize=0.25 (default)")
set.seed(11); ad0 <- getArtificialDoublets(xs, n=800, clusters=cl, adjustSize=0)
f_0 <- check(ad0, "adjustSize=0")
ok("getArtificialDoublets(adjustSize=0): every cross-cluster doublet's counts match its origin label", f_0 < 0.01)
ok("getArtificialDoublets(adjustSize=0.25, the default): every cross-cluster doublet's counts match its origin label", f_def < 0.01, sprintf("(%.1f %% mislabelled; createDoublets returns the size-adjusted doublets after the others, and the caller assigns the origins in the input order)", 100*f_def))

# ---- corrected createDoublets: keep the input order and count the halved doublets over all pairs
source("createDoubletsFixed.R")
ns <- asNamespace("scDblFinder")
orig_fun <- ns$createDoublets
unlockBinding("createDoublets", ns); assign("createDoublets", createDoubletsFixed, envir=ns); lockBinding("createDoublets", ns)
set.seed(11); adF <- getArtificialDoublets(xs, n=800, clusters=cl)
f_fix <- check(adF, "adjustSize=0.25 with the corrected createDoublets")
ok("corrected createDoublets: every cross-cluster doublet's counts match its origin label", f_fix < 0.01)
pairs <- cbind(sample(ncol(x), 40, TRUE), sample(ncol(x), 40, TRUE)); pairs <- pairs[pairs[,1]!=pairs[,2],]
ls.pair <- colSums(x)[pairs[,1]] + colSums(x)[pairs[,2]]
set.seed(4); m <- createDoubletsFixed(xs, pairs, clusters=cl, adjustSize=0.25, resamp=0, halfSize=0)
ok("corrected createDoublets: column i is pair i, size-adjusted columns keep the pair's total library size", all(abs(colSums(m) - ls.pair) < 1e-6))
set.seed(4); m <- createDoubletsFixed(xs, pairs, clusters=cl, adjustSize=0.25, resamp=0, halfSize=0.5)
halved <- abs(colSums(m) - ls.pair/2) < abs(colSums(m) - ls.pair)
ok("corrected createDoublets: ceiling(halfSize x pairs) columns are halved", sum(halved) == ceiling(0.5*nrow(pairs)), sprintf("(%d of %d)", sum(halved), nrow(pairs)))
set.seed(4); m <- createDoubletsFixed(xs, pairs[1:4,], clusters=cl, adjustSize=0.25)
ok("corrected createDoublets: 4 pairs with adjustSize=0.25 give 4 integer doublets", ncol(m)==4 && all(as.matrix(m)==round(as.matrix(m))))
unlockBinding("createDoublets", ns); assign("createDoublets", orig_fun, envir=ns); lockBinding("createDoublets", ns)
