# duplicateCorrelation on the shipped build against (i) lme4 REML variance components per gene
# (rho = sb2/(sb2+se2)), (ii) statmod::mixedModel2Fit called directly (the reference limma
# used before the devel C backend), (iii) the consensus rule tanh(mean(atanh(rho), trim=0.15)),
# and planted truth. Weighted and missing-value cases included.
suppressPackageStartupMessages({library(limma); library(statmod); library(lme4)})
cat("limma", as.character(packageVersion("limma")), " statmod", as.character(packageVersion("statmod")), " lme4", as.character(packageVersion("lme4")), "\n")
set.seed(7)
G <- 300; nsubj <- 6; nrep <- 2; n <- nsubj*nrep
block <- rep(1:nsubj, each=nrep)
trt <- rep(c(0,1), length.out=nsubj)[block]   # treatment constant within block
design <- cbind(Int=1, Trt=trt)
rho.true <- 0.4
u <- matrix(rnorm(G*nsubj, sd=sqrt(rho.true)), G, nsubj)
y <- matrix(rnorm(G, 5), G, n) + outer(rnorm(G), trt) + u[,block] + matrix(rnorm(G*n, sd=sqrt(1-rho.true)), G, n)
dimnames(y) <- list(paste0("g",1:G), paste0("s",1:n))

dc <- duplicateCorrelation(y, design, block=block)
cat("consensus correlation (truth 0.4):", dc$consensus.correlation, "\n")
rho <- tanh(dc$atanh.correlations)

# (i) lme4 REML per gene (first 40 genes)
rl <- sapply(1:40, function(g) {
  d <- data.frame(y=y[g,], trt=trt, b=factor(block))
  vc <- as.data.frame(VarCorr(lmer(y ~ trt + (1|b), data=d, REML=TRUE, control=lmerControl(check.conv.singular="ignore"))))
  sb <- vc$vcov[vc$grp=="b"]; se <- vc$vcov[vc$grp=="Residual"]; sb/(sb+se)
})
ok <- rl > 1e-6 & rho[1:40] > 0 & rho[1:40] < 0.989   # interior REML optima (lme4 constrains sb2 >= 0; statmod's gamma GLM does not)
cat(sprintf("lme4 REML rho vs limma genewise rho: max |diff| %.2e over %d interior genes; %d genes with negative/boundary block variance excluded\n",
  max(abs(rl[ok]-rho[1:40][ok])), sum(ok), sum(!ok)))

# (ii) statmod::mixedModel2Fit reference loop (limma <= 3.68 code path) on all genes
Z <- model.matrix(~0+factor(block))
ref <- sapply(1:G, function(g) { s <- mixedModel2Fit(y[g,], design, Z, only.varcomp=TRUE, maxit=20)$varcomp; s[2]/sum(s) })
ref <- pmin(pmax(ref, 1/(1-nrep)+0.01), 0.99)
cat(sprintf("statmod reference rho vs limma genewise rho: max |diff| %.2e, median %.2e\n", max(abs(ref-rho)), median(abs(ref-rho))))
cat(sprintf("consensus rule tanh(mean(atanh(rho),trim=0.15)): %.2e\n", abs(tanh(mean(atanh(ref),trim=0.15)) - dc$consensus.correlation)))

# weights and missing values
w <- matrix(rexp(G*n), G, n); yna <- y; yna[sample(length(y), 60)] <- NA
dcw <- duplicateCorrelation(yna, design, block=block, weights=w)
refw <- sapply(1:G, function(g) { o <- is.finite(yna[g,]); A <- factor(block[o])
  if(sum(o) <= 4 || nlevels(A) < 2 || nlevels(A) >= sum(o)-1) return(NA)
  s <- mixedModel2Fit(yna[g,o], design[o,,drop=FALSE], model.matrix(~0+A), w[g,o], only.varcomp=TRUE, maxit=20)$varcomp; s[2]/sum(s) })
refw <- pmin(pmax(refw, 1/(1-nrep)+0.01), 0.99)
rw <- tanh(dcw$atanh.correlations)
cat(sprintf("weights+NA: statmod reference vs limma: max |diff| %.2e over %d genes, NA-pattern mismatches %d (ref NA %d, limma NA %d); consensus %.5f vs rule %.5f\n",
  max(abs(refw-rw), na.rm=TRUE), sum(!is.na(refw)), sum(is.na(refw)!=is.na(rw)), sum(is.na(refw)), sum(is.na(rw)),
  dcw$consensus.correlation, tanh(mean(atanh(refw),trim=0.15,na.rm=TRUE))))

# ndups (within-array duplicates) form: spacing=1, ndups=2
y2 <- matrix(0, 2*G, nsubj); for(g in 1:G) y2[2*g-1,] <- y[g, seq(1,n,2)]; for(g in 1:G) y2[2*g,] <- y[g, seq(2,n,2)]
d2 <- duplicateCorrelation(y2, design[seq(1,n,2),,drop=FALSE], ndups=2, spacing=1)   # each block = one array with two spots
cat(sprintf("ndups=2 form vs block form: consensus %.6f vs %.6f, genewise max |diff| %.2e\n", d2$consensus.correlation, dc$consensus.correlation, max(abs(tanh(d2$atanh.correlations)-rho))))

# nthreads (devel)
tryCatch({ d4 <- duplicateCorrelation(yna, design, block=block, weights=w, nthreads=4L); cat("nthreads=4 identical:", identical(d4, dcw), "\n") }, error=function(e) cat("nthreads not available\n"))
