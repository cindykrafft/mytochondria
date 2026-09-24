#!/usr/bin/env Rscript
# scDblFinder: the deterministic pieces against independent recomputations.
# getExpectedDoublets (closed form), propHomotypic, .defaultKnnKs, cxds2 (explicit
# double-loop port of the co-expression score), doubletThresholding methods "dbr"
# and "griffiths" (ports), .optimThreshold's cost function (port + optimize), and
# createDoublets' bookkeeping (pair count, integer counts, the adjustSize branch).
# Usage: Rscript d1_deterministic_pieces.R [libPath]
args <- commandArgs(trailingOnly=TRUE)
if(length(args)>0) .libPaths(c(args[1], .libPaths()))
suppressPackageStartupMessages({library(scDblFinder); library(Matrix)})
cat("scDblFinder", as.character(packageVersion("scDblFinder")), "\n")
ns <- asNamespace("scDblFinder")
ok <- function(label, cond, detail=""){ cat(if(isTRUE(cond)) "ok  " else "FAIL", label, detail, "\n") }
close <- function(a, b, tol=1e-9) all(abs(a-b) <= tol*pmax(1, abs(b)))
set.seed(1)

# ---- getExpectedDoublets: heterotypic pairs 2 p_i p_j dbr N, homotypic p_i^2 dbr N
cl <- factor(rep(c("A","B","C","D"), c(300, 500, 150, 50))); N <- length(cl); dbr <- 0.04
p <- as.numeric(table(cl))/N; names(p) <- levels(cl)
ex <- getExpectedDoublets(cl, dbr=dbr)
truth <- c(); for(i in 1:3) for(j in (i+1):4) truth[paste(levels(cl)[i], levels(cl)[j], sep="+")] <- 2*p[i]*p[j]*dbr*N
ok("getExpectedDoublets(only.heterotypic=TRUE): 2 p_i p_j dbr N for every pair", close(ex[names(truth)], truth) && length(ex)==6, sprintf("(sum %.3f = dbr N (1 - sum p^2) %.3f)", sum(ex), dbr*N*(1-sum(p^2))))
exa <- getExpectedDoublets(cl, dbr=dbr, only.heterotypic=FALSE)
truth2 <- truth; for(i in 1:4) truth2[paste(levels(cl)[i], levels(cl)[i], sep="+")] <- p[i]^2*dbr*N
ok("getExpectedDoublets(only.heterotypic=FALSE): adds p_i^2 dbr N; total dbr N", close(exa[names(truth2)], truth2) && close(sum(exa), dbr*N))
ok("getExpectedDoublets default dbr = 0.01 x N/1000", close(sum(getExpectedDoublets(cl, only.heterotypic=FALSE)), 0.01*N/1000*N))
if(exists("propHomotypic", ns)) ok("propHomotypic = sum p_i^2", close(propHomotypic(cl), sum(p^2)), sprintf("(%.4f)", sum(p^2))) else cat("   propHomotypic: not in this version\n")

# ---- .defaultKnnKs
if(!is.function(ns$.defaultKnnKs)) cat("   .defaultKnnKs: not in this version\n") else for(n in c(500, 2000, 5000, 20000)){
  kmax <- max(ceiling(sqrt(n/2)), 25); exp <- unique(c(3,10,15,20,25,50,kmax)[c(3,10,15,20,25,50,kmax)<=kmax])
  ok(sprintf(".defaultKnnKs(n=%d) = {3,10,15,20,25,50,kmax} capped at kmax=max(ceil(sqrt(n/2)),25)=%d", n, kmax), identical(ns$.defaultKnnKs(NULL, n), exp), paste(ns$.defaultKnnKs(NULL, n), collapse=","))
}

# ---- cxds2 against an explicit port (binarize at >=1, top genes by p(1-p), pairwise upper-tail binomial log-p, score = -x' S x, min-max)
ng <- 40; nc <- 150
mu <- 2^rnorm(ng, -2.5, 1.2); x <- matrix(rpois(ng*nc, mu), ng, nc); rownames(x) <- paste0("g", seq_len(ng))   # ~15 % non-zero, the usual scRNA-seq sparsity
cat("   cxds2 test matrix: fraction non-zero", round(mean(x > 0), 3), "\n")
wd <- c(140:150)   # "known doublets" excluded from the pairwise statistics
port_cxds <- function(x, whichDbls, ntop){
  B <- x >= 1; ps <- rowMeans(B)
  if(nrow(B) > ntop){ hv <- order(ps*(1-ps), decreasing=TRUE)[seq_len(ntop)]; B <- B[hv,]; ps <- ps[hv] }
  Bp <- if(length(whichDbls)) B[,-whichDbls] else B
  n <- ncol(Bp); G <- nrow(B); S <- matrix(0, G, G)
  for(i in seq_len(G)) for(j in seq_len(G)){
    obs <- sum((Bp[i,] & !Bp[j,]) | (Bp[j,] & !Bp[i,]))
    prb <- ps[i]*(1-ps[j]) + ps[j]*(1-ps[i])
    S[i,j] <- pbinom(obs-1, size=n, prob=prb, lower.tail=FALSE, log.p=TRUE)
  }
  if(any(is.infinite(S))){ smin <- min(S[!is.infinite(S)]); S[S < smin] <- smin }
  s <- sapply(seq_len(ncol(B)), function(c) -as.numeric(t(B[,c]) %*% S %*% B[,c]))
  s <- s - min(s); s/max(s)
}
if(!exists("cxds2", ns)){ cat("   cxds2: not in this version\n") } else {
got <- cxds2(as(x, "CsparseMatrix"), whichDbls=wd, ntop=25); want <- port_cxds(x, wd, 25)
ok("cxds2 (sparse input, 25 of 40 genes, 11 excluded cells) equals the double-loop port on all 150 cells", close(got, want, 1e-8), sprintf("(max |diff| %.2e)", max(abs(got-want))))
got2 <- cxds2(x, whichDbls=c(), ntop=500)
ok("cxds2 (dense input, all genes, no exclusions) equals the port", close(got2, port_cxds(x, c(), 500), 1e-8))
# low-sparsity input (> 50 % non-zero): the sparse and dense code paths pick the binarisation threshold differently
xd <- matrix(rpois(ng*nc, 2^rnorm(ng, 0.5, 1)), ng, nc); rownames(xd) <- rownames(x)
cat("   low-sparsity matrix: fraction non-zero", round(mean(xd > 0), 3), "; cxds2(sparse) vs cxds2(dense) max |diff|", signif(max(abs(cxds2(as(xd, "CsparseMatrix"), ntop=25) - cxds2(xd, ntop=25))), 3), "\n")
}

# ---- doubletThresholding: "dbr" = 1-dbr quantile of the real scores; "griffiths" one-sided MAD
d <- data.frame(score=c(runif(900, 0, 0.6), runif(100, 0.4, 1)), type=rep("real", 1000)); d$src <- "real"
th <- doubletThresholding(d, dbr=0.08, method="dbr", returnType="threshold")
cat("   doubletThresholding(method='dbr') on a table with only real cells and no cluster column: threshold", as.numeric(th), "\n")
ok("doubletThresholding(method='dbr'): threshold = quantile(score, 1 - dbr) (the documented 'simple' method)", isTRUE(close(as.numeric(th), as.numeric(quantile(d$score, 0.92)))), "(dbr is first corrected for homotypic doublets from the artificial doublets' scores; with none the correction is NaN)")
d$cluster <- factor(rep(c("A","B","C"), length.out=nrow(d)))
th <- doubletThresholding(d, dbr=0.08, method="dbr", returnType="threshold"); pc <- as.numeric(table(d$cluster)/nrow(d))
ok("doubletThresholding(method='dbr') with clusters: threshold = quantile(score, 1 - dbr x (1 - sum p_i^2)) (heterotypic rate)", close(as.numeric(th), as.numeric(quantile(d$score, 1 - 0.08*(1-sum(pc^2))))), sprintf("(%.4f)", as.numeric(th)))
calls <- doubletThresholding(d, dbr=0.08, method="dbr", returnType="call")
ok("doubletThresholding(method='dbr') with clusters: calls = score > threshold", identical(as.character(calls), ifelse(d$score > as.numeric(th), "doublet", "singlet")))
med <- median(d$score); dev <- d$score - med; mad1 <- median(dev[dev > 0]) * 1.4826
thg <- doubletThresholding(d, method="griffiths", p=0.1, returnType="threshold")
ok("doubletThresholding(method='griffiths'): threshold = qnorm(1-p, median, 1.4826 x median of the positive deviations)", close(as.numeric(thg), qnorm(0.1, med, mad1, lower.tail=FALSE)))

# ---- .optimThreshold: port of the cost (dev^2 + 2(1-s) FNR + 2 s FPR) and optimize()
d2 <- data.frame(score=c(rbeta(2000, 1, 6), rbeta(1500, 5, 2)), type=rep(c("real","doublet"), c(2000, 1500)), cluster=1L, include.in.training=TRUE); d2$src <- ifelse(d2$type=="real", "real", "artificial")
rownames(d2) <- c(paste0("cell", 1:2000), paste0("aDbl.", 1:1500))
port_cost <- function(x, d, dbr, dbr.sd, stringency){
  real <- d$type=="real"; expected <- c(max(0, dbr-dbr.sd), min(1, dbr+dbr.sd)) * sum(real)
  obs <- 1 + sum(d$score >= x & real); e1 <- expected + 1
  dev <- if(obs > min(e1) && obs < max(e1)) 0 else min(abs(obs - e1)/e1)
  fnr <- max(0, sum(!real & d$score < x))/sum(!real)
  fpr <- sum(real & d$score >= x)/sum(real)
  dev^2 + 2*(1-stringency)*fnr + 2*stringency*fpr
}
for(s in c(0.5, 0.7)){
  got <- ns$.optimThreshold(d2, dbr=0.05, dbr.sd=0.02, stringency=s)
  want <- optimize(port_cost, c(0, 1), d=d2, dbr=0.05, dbr.sd=0.02, stringency=s)$minimum
  ok(sprintf(".optimThreshold(dbr=0.05, dbr.sd=0.02, stringency=%.1f) equals optimize() over the ported cost", s), close(got, want, 1e-6), sprintf("(%.5f vs %.5f)", got, want))
}
tab <- ns$.optimThreshold(d2, dbr=0.05, dbr.sd=0.02, ths=seq(0.1, 0.9, 0.1))
ok(".optimThreshold(ths=...): the tabulated cost equals the port at every threshold", close(tab$cost, sapply(tab$threshold, port_cost, d=d2, dbr=0.05, dbr.sd=0.02, stringency=0.5), 1e-9))

# ---- createDoublets: pair count, integer counts, halving/resampling bookkeeping
xs <- as(x, "CsparseMatrix"); pairs <- cbind(sample(nc, 60, TRUE), sample(nc, 60, TRUE)); pairs <- pairs[pairs[,1]!=pairs[,2],]
set.seed(3); m <- createDoublets(xs, pairs, resamp=0, halfSize=0)
ok("createDoublets(resamp=0, halfSize=0): one column per pair, each the sum of the two cells", ncol(m)==nrow(pairs) && all(as.matrix(m) == x[,pairs[,1]] + x[,pairs[,2]]))
set.seed(3); m <- createDoublets(xs, pairs, resamp=0.25, halfSize=0.25)
ok("createDoublets(resamp=halfSize=0.25): integer counts throughout (the halved doublets are the resampled ones)", all(as.matrix(m) == round(as.matrix(m))))
set.seed(3); m <- createDoublets(xs, pairs, resamp=0.1, halfSize=0.5)
cat("   createDoublets(resamp=0.1, halfSize=0.5): columns with non-integer counts", sum(colSums(as.matrix(m) != round(as.matrix(m))) > 0), "of", ncol(m), "\n")
cl2 <- factor(sample(c("A","B"), nc, TRUE))
res <- tryCatch({ set.seed(4); m <- createDoublets(xs, pairs[1:4,], clusters=cl2, adjustSize=0.25, resamp=0, halfSize=0); ncol(m) }, error=function(e) conditionMessage(e))
ok("createDoublets(4 pairs, adjustSize=0.25 -> one pair selected for size adjustment): 4 doublets returned", identical(res, 4L), paste("(got:", paste(res, collapse=" "), ")"))
res <- tryCatch({ set.seed(4); m <- createDoublets(xs, pairs[1:4,], clusters=cl2, adjustSize=0.25); ncol(m) }, error=function(e) conditionMessage(e))
cat("   createDoublets(4 pairs, adjustSize=0.25, default resamp/halfSize):", paste(res, collapse=" "), "\n")
set.seed(4); m <- createDoublets(xs, pairs[1:40,], clusters=cl2, adjustSize=0.25, resamp=0, halfSize=0)
ls.pair <- colSums(x)[pairs[1:40,1]] + colSums(x)[pairs[1:40,2]]
ok("createDoublets(40 pairs, adjustSize=0.25): 40 doublets, every column's library size equals some pair's total", ncol(m)==40 && all(abs(sort(colSums(m)) - sort(ls.pair)) < 1e-6))
ok("createDoublets(40 pairs, adjustSize=0.25): column i is pair i (same library size)", all(abs(colSums(m) - ls.pair) < 1e-6), sprintf("(%d of 40 columns sit at another pair's position)", sum(abs(colSums(m) - ls.pair) > 1e-6)))
set.seed(4); m <- createDoublets(xs, pairs[1:40,], clusters=cl2, adjustSize=0.25, resamp=0, halfSize=0.5)
full <- sort(ls.pair); cs <- colSums(m)
halved <- sapply(cs, function(v) min(abs(v - full/2)) < min(abs(v - full)))   # closer to half of some pair's size than to any pair's size
ok("createDoublets(40 pairs, adjustSize=0.25, halfSize=0.5): ceiling(0.5 x 40) = 20 columns halved", sum(halved) == 20, sprintf("(%d halved: the code halves ceiling(halfSize x number of size-adjusted pairs) columns)", sum(halved)))
