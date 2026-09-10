# camera / fry / roast on the shipped build against ports written from Wu & Smyth (2012) camera,
# and the fry/roast descriptions (Wu et al. 2010); zscoreT approximations vs the exact quantile map.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(9)
maxabs <- function(a,b) max(abs(as.matrix(a)-as.matrix(b)), na.rm=TRUE)
G <- 3000; n <- 10
design <- cbind(Int=1, Trt=rep(c(0,1),each=5))
s2g <- 0.5*4/rchisq(G, 4)                       # gene-specific variances so that df.prior is finite
y <- matrix(rnorm(G*n), G, n)*sqrt(s2g) + 5
# gene-set 1 up-regulated with inter-gene correlation 0.1; others random
set1 <- 1:60; z <- rnorm(n); y[set1,] <- y[set1,] + sqrt(0.1)*matrix(z,60,n,byrow=TRUE)*sqrt(s2g[set1])/sqrt(1-0.1) ; y[set1, 6:10] <- y[set1,6:10] + 0.5
sets <- list(up=set1, null1=61:120, null2=sample(121:G, 40), big=sample(121:G, 300))
rownames(y) <- paste0("g",1:G)

# --- camera port (Wu & Smyth 2012): moderated t -> z (exact), two-sample t with VIF from residual correlation ---
cam <- camera(y, sets, design, inter.gene.cor=NA, sort=FALSE)
camf <- camera(y, sets, design, sort=FALSE)   # default: inter.gene.cor=0.01
port_camera <- function(y, index, design, contrast=ncol(design), igc=NA, ranks=FALSE) {
  q <- qr(design); p <- ncol(design); Gn <- nrow(y); df <- n-p
  eff <- qr.qty(q, t(y)); ut <- eff[p,]; if(q$qr[p,p] < 0) ut <- -ut
  U <- eff[-(1:p),,drop=FALSE]; s2 <- colMeans(U^2); U <- t(U)/sqrt(s2)
  # squeezeVar moments (Smyth 2004) written out
  e <- log(s2) - digamma(df/2) + log(df/2); ev <- var(e) - trigamma(df/2)
  ti <- function(x){ yv <- 0.5+1/x; for(i in 1:60) yv <- yv + trigamma(yv)*(1-trigamma(yv)/x)/psigamma(yv,2); yv }
  if(ev > 0) { d0 <- 2*ti(ev); s02 <- exp(mean(e)+digamma(d0/2)-log(d0/2)) } else { d0 <- Inf; s02 <- mean(s2) }
  s2p <- if(is.finite(d0)) (d0*s02+df*s2)/(d0+df) else rep(s02, Gn); modt <- ut/sqrt(s2p); dft <- min(df+d0, Gn*df)
  Stat <- qnorm(pt(abs(modt), dft, lower.tail=FALSE, log.p=TRUE), lower.tail=FALSE, log.p=TRUE)*sign(modt)
  dfc <- if(is.na(igc)) min(df, Gn-2) else Gn-2
  out <- t(sapply(index, function(iset) {
    m <- length(iset); m2 <- Gn-m
    if(is.na(igc)) { Us <- U[iset,,drop=FALSE]; ub <- colMeans(Us); vif <- m*mean(ub^2); cor <- (vif-1)/(m-1) } else { cor <- igc; vif <- 1+(m-1)*cor }
    vif <- max(1, vif)
    mean1 <- mean(Stat[iset]); mean2 <- mean(Stat[-iset]); s1 <- var(Stat[iset]); s2v <- var(Stat[-iset])
    sp <- ((m-1)*s1 + (m2-1)*s2v)/(Gn-2)
    tt <- (mean1-mean2)/sqrt(sp*(vif/m+1/m2))
    c(cor, 2*pt(-abs(tt), dfc), if(tt>0) 1 else -1) }))
  colnames(out) <- c("cor","p","dir"); out }
pc <- port_camera(y, sets, design); pcf <- port_camera(y, sets, design, igc=0.01)
cat(sprintf("[camera, estimated correlation] Correlation %.1e  PValue %.1e  Direction agrees %s  FDR = BH %.1e\n", maxabs(cam$Correlation, pc[,"cor"]), maxabs(cam$PValue, pc[,"p"]), all((cam$Direction=="Up") == (pc[,"dir"]>0)), maxabs(cam$FDR, p.adjust(pc[,"p"],"BH"))))
cat(sprintf("[camera, inter.gene.cor=0.01] PValue %.1e\n", maxabs(camf$PValue, pcf[,"p"])))
cat(sprintf("  set 'up' (60 genes, planted cor 0.1, shift 0.5): estimated cor %.3f, p %.2e; null sets p %s\n", cam$Correlation[1], cam$PValue[1], paste(signif(cam$PValue[-1],2), collapse=" ")))
# zscoreT: Hill approximation (used by camera) vs exact
tt <- seq(-8, 8, by=0.05); zex <- function(x, df) qnorm(pt(abs(x), df, lower.tail=FALSE, log.p=TRUE), lower.tail=FALSE, log.p=TRUE)*sign(x)
if("method" %in% names(formals(zscoreT))) { for(dd in c(4, 8, 30)) cat(sprintf("[zscoreT Hill df=%d] max |z_hill - z_exact| %.1e over t in [-8,8]; Bailey %.1e\n", dd, max(abs(zscoreT(tt,dd,approx=TRUE,method="hill")-zex(tt,dd))), max(abs(zscoreT(tt,dd,approx=TRUE,method="bailey")-zex(tt,dd))))) } else
  for(dd in c(4, 8, 30)) cat(sprintf("[zscoreT approx df=%d] max |z_approx - z_exact| %.1e over t in [-8,8]\n", dd, max(abs(zscoreT(tt,dd,approx=TRUE)-zex(tt,dd)))))
# camera use.ranks: rankSumTestWithCorrelation vs port of the correlated Wilcoxon (Wu & Smyth 2012, eq. for var with VIF)
camr <- camera(y, sets, design, use.ranks=TRUE, inter.gene.cor=NA, sort=FALSE)
# --- fry: directional p from the standardized effects, port ---
fr <- fry(y, sets, design, sort=FALSE)
port_fry <- function(y, index, design) {
  q <- qr(design); p <- ncol(design); eff <- t(qr.qty(q, t(y)))[, p:n, drop=FALSE]; if(q$qr[p,p]<0) eff[,1] <- -eff[,1]
  df <- n-p; s2 <- rowMeans(eff[,-1]^2)
  # robust genewise sd: leave-one-out of the largest squared effect, expectation constant by quadrature
  gq <- statmod::gauss.quad.prob(128,"uniform"); Eu2max <- sum((df+1)*gq$nodes^df*qchisq(gq$nodes,1)*gq$weights)
  u2max <- apply(eff^2,1,max); s2r <- (rowSums(eff^2)-u2max)/(df+1-Eu2max)
  e <- log(s2) - digamma(df/2) + log(df/2); ev <- var(e) - trigamma(df/2)
  ti <- function(x){ yv <- 0.5+1/x; for(i in 1:60) yv <- yv + trigamma(yv)*(1-trigamma(yv)/x)/psigamma(yv,2); yv }
  d0 <- 2*ti(ev); s02 <- exp(mean(e)+digamma(d0/2)-log(d0/2))
  s2r <- (0.92*df*s2r + d0*s02)/(0.92*df+d0); E <- eff/sqrt(s2r)
  sapply(index, function(iset){ m <- colMeans(E[iset,,drop=FALSE]); t <- m[1]/sqrt(mean(m[-1]^2)); 2*pt(-abs(t), df) }) }
cat(sprintf("[fry] PValue vs port %.1e; FDR = BH %.1e\n", maxabs(fr$PValue, port_fry(y, sets, design)), maxabs(fr$FDR, p.adjust(fr$PValue,"BH"))))
# --- roast: port of the mean-statistic rotation test with the same random stream ---
set.seed(21); ro <- roast(y, sets$up, design, nrot=999, set.statistic="mean")
port_roast <- function(y, iset, design, nrot) {
  q <- qr(design); p <- ncol(design); eff <- t(qr.qty(q, t(y)))[, p:n, drop=FALSE]; if(q$qr[p,p]<0) eff[,1] <- -eff[,1]
  df <- n-p; s2 <- rowMeans(eff[,-1]^2)
  e <- log(s2) - digamma(df/2) + log(df/2); ev <- var(e) - trigamma(df/2)
  ti <- function(x){ yv <- 0.5+1/x; for(i in 1:60) yv <- yv + trigamma(yv)*(1-trigamma(yv)/x)/psigamma(yv,2); yv }
  d0 <- 2*ti(ev); s02 <- exp(mean(e)+digamma(d0/2)-log(d0/2)); dft <- min(df+d0, 10000)
  E <- eff[iset,,drop=FALSE]; s2p <- (d0*s02+df*s2[iset])/(d0+df)
  zb <- function(x, dfv) ((dfv+0.125)/(dfv+1.125))*sqrt((dfv+19/12)*log1p(x/(dfv+1/12)*x))*sign(x)   # Bailey z-score, as documented in ?zscoreT
  modt <- zb(E[,1]/sqrt(s2p), dft); m <- mean(modt)
  nchunk <- ceiling(nrot/1000); nroti <- ceiling(nrot/nchunk); count <- c(down=0,up=0,mixed=0)
  for(ch in 1:nchunk) { if(ch==nchunk) nroti <- nroti-(nchunk*nroti-nrot)
    R <- matrix(rnorm(nroti*ncol(E)), nroti, ncol(E)); R <- R/sqrt(rowSums(R^2)); Br <- tcrossprod(E, R)
    s2r <- (rowSums(E^2)-Br^2)/df; s2r <- (d0*s02+df*s2r)/(d0+df); mr <- zb(Br/sqrt(s2r), dft)
    mm <- colMeans(mr); count["down"] <- count["down"] + sum(c(-mm,mm) > -m); count["up"] <- count["up"] + sum(c(-mm,mm) > m); count["mixed"] <- count["mixed"] + sum(colMeans(abs(mr)) > mean(abs(modt))) }
  c(Down=(count["down"]+1)/(2*nrot+1), Up=(count["up"]+1)/(2*nrot+1), UpOrDown=(min(count["down"],count["up"])+1)/(nrot+1), Mixed=(count["mixed"]+1)/(nrot+1)) }
set.seed(21); pr <- port_roast(y, sets$up, design, 999)
cat(sprintf("[roast mean, same RNG stream] Down %.1e Up %.1e UpOrDown %.1e Mixed %.1e (limma: %s)\n", abs(ro$p.value["Down","P.Value"]-pr[1]), abs(ro$p.value["Up","P.Value"]-pr[2]), abs(ro$p.value["UpOrDown","P.Value"]-pr[3]), abs(ro$p.value["Mixed","P.Value"]-pr[4]), paste(signif(ro$p.value$P.Value,3), collapse=" ")))
# --- roast null calibration: p-values uniform on null sets over 200 sets x 199 rotations ---
set.seed(2); ynull <- matrix(rnorm(G*n), G, n); nulls <- replicate(200, sample(G, 30), simplify=FALSE)
mr <- mroast(ynull, nulls, design, nrot=199, sort="none")
cat(sprintf("[roast null] fraction PValue < 0.05: %.3f (200 sets), < 0.10: %.3f; Mixed < 0.05: %.3f\n", mean(mr$PValue<0.05), mean(mr$PValue<0.10), mean(mr$PValue.Mixed<0.05)))
cn <- camera(ynull, nulls, design, sort=FALSE); cn2 <- camera(ynull, nulls, design, inter.gene.cor=NA, sort=FALSE)
cat(sprintf("[camera null] fraction PValue < 0.05: fixed cor 0.01 %.3f; estimated cor %.3f (200 independent-gene sets)\n", mean(cn$PValue<0.05), mean(cn2$PValue<0.05)))
