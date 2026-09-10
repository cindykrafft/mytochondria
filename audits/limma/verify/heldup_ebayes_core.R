# eBayes / squeezeVar / fitFDist / treat / topTable / F-statistic on the shipped build against
# closed forms written from Smyth (2004) and McCarthy & Smyth (2009); no limma call inside a
# reference. Synthetic data with planted d0, s0.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(3)
maxabs <- function(a,b) max(abs(as.matrix(a)-as.matrix(b)), na.rm=TRUE)
G <- 5000; n <- 8; d0 <- 4; s0 <- 0.3
design <- cbind(Int=1, A=rep(c(0,1),each=4), B=rep(c(0,1),4))
s2g <- s0^2 * d0 / rchisq(G, d0)                     # scaled inverse chi-square prior
beta <- cbind(rnorm(G,7), ifelse(runif(G)<0.1, rnorm(G,0,1), 0), ifelse(runif(G)<0.1, rnorm(G,0,1), 0))
y <- beta %*% t(design) + matrix(rnorm(G*n), G, n) * sqrt(s2g)
fit <- lmFit(y, design)
eb <- eBayes(fit)

# --- fitFDist: moment estimator from Smyth 2004 eqs (5)-(6), independent code ---
trigamma_inv <- function(x) { yv <- 0.5 + 1/x; for(i in 1:60) yv <- yv + trigamma(yv)*(1-trigamma(yv)/x)/psigamma(yv,2); yv }
z <- log(fit$sigma^2); d1 <- fit$df.residual[1]
e <- z - digamma(d1/2) + log(d1/2)
evar <- var(e) - trigamma(d1/2)
d0.hat <- 2*trigamma_inv(evar); s02.hat <- exp(mean(e) + digamma(d0.hat/2) - log(d0.hat/2))
cat(sprintf("[fitFDist] df.prior %.6f vs port %.6f (diff %.1e; truth %d); s2.prior %.6f vs port %.6f (diff %.1e; truth %.4f)\n",
  eb$df.prior, d0.hat, abs(eb$df.prior-d0.hat), d0, eb$s2.prior, s02.hat, abs(eb$s2.prior-s02.hat), s0^2))
# --- posterior variance, moderated t, p, df ---
s2post <- (d0.hat*s02.hat + d1*fit$sigma^2)/(d0.hat+d1)
tmod <- fit$coefficients/fit$stdev.unscaled/sqrt(s2post)
df.total <- pmin(fit$df.residual + d0.hat, sum(fit$df.residual))
p <- 2*pt(-abs(tmod), df.total)
cat(sprintf("[eBayes] s2.post %.1e  t %.1e  df.total %.1e  p %.1e\n", maxabs(eb$s2.post,s2post), maxabs(eb$t,tmod), maxabs(eb$df.total,df.total), maxabs(eb$p.value,p)))
# --- B statistic: recompute from eb$var.prior with Smyth 2004 eq (14) ---
for(j in 1:3) {
  v0 <- eb$var.prior[j]; v1 <- fit$stdev.unscaled[,j]^2; r <- (v1+v0)/v1; t2 <- tmod[,j]^2
  B <- log(0.01/0.99) - log(r)/2 + (1+df.total)/2*log((t2+df.total)/(t2/r+df.total))
  cat(sprintf("[B-stat coef %d] max |diff| %.1e  (var.prior %.4f)\n", j, maxabs(eb$lods[,j], B), v0))
}
# --- var.prior via tmixture: independent port of the order-statistic estimator (Smyth 2004 s.6) ---
tmix <- function(tstat, su, df, proportion=0.01, lim) {
  ngenes <- length(tstat); ntarget <- ceiling(proportion/2*ngenes); pp <- max(ntarget/ngenes, proportion)
  ta <- abs(tstat); o <- order(ta, decreasing=TRUE)[1:ntarget]; ta <- ta[o]; v1 <- su[o]^2
  r <- 1:ntarget; p0 <- 2*pt(ta, df=max(df), lower.tail=FALSE)
  ptarget <- ((r-0.5)/ngenes - (1-pp)*p0)/pp
  v0 <- rep(0, ntarget); pos <- ptarget > p0
  qtarget <- qt(ptarget[pos]/2, df=max(df), lower.tail=FALSE); v0[pos] <- v1[pos]*((ta[pos]/qtarget)^2-1)
  mean(pmin(pmax(v0, lim[1]), lim[2]))
}
lim <- c(0.1,4)^2/median(eb$s2.prior)
cat(sprintf("[var.prior] port vs eBayes: %.1e %.1e %.1e\n", abs(tmix(tmod[,1],fit$stdev.unscaled[,1],df.total,lim=lim)-eb$var.prior[1]),
  abs(tmix(tmod[,2],fit$stdev.unscaled[,2],df.total,lim=lim)-eb$var.prior[2]), abs(tmix(tmod[,3],fit$stdev.unscaled[,3],df.total,lim=lim)-eb$var.prior[3])))
# --- F statistic for coefs 2:3: t' R^-1 t / r with R = cor of coefficients ---
Rc <- cov2cor(fit$cov.coefficients[2:3,2:3]); Q <- eigen(Rc, symmetric=TRUE)
Fst <- rowSums((tmod[,2:3] %*% Q$vectors %*% diag(1/sqrt(Q$values)))^2)/2
ebF <- eBayes(fit[,2:3])
cat(sprintf("[F] max |diff| %.1e; F.p.value vs pf(F,2,df) %.1e; single-coef F == t^2 %.1e, F p == t p %.1e\n",
  maxabs(ebF$F, Fst), maxabs(ebF$F.p.value, pf(Fst,2,d1+d0.hat,lower.tail=FALSE)),
  maxabs(eBayes(fit[,2])$F, tmod[,2]^2), maxabs(eBayes(fit[,2])$F.p.value, p[,2])))
# --- topTable: BH, sort, confint ---
tt <- topTable(eb, coef=2, number=Inf, sort.by="none", confint=TRUE)
cat(sprintf("[topTable] adj.P vs p.adjust(BH) %.1e; logFC %.1e; CI half-width vs qt(.975,df.total)*se %.1e; sorted by B: %s; p.value filter <= : %s\n",
  maxabs(tt$adj.P.Val, p.adjust(p[,2],"BH")), maxabs(tt$logFC, fit$coefficients[,2]),
  maxabs((tt$CI.R-tt$CI.L)/2, qt(0.975, df.total)*fit$stdev.unscaled[,2]*sqrt(s2post)),
  !is.unsorted(-topTable(eb,coef=2,number=Inf)$B),
  all(topTable(eb,coef=2,number=Inf,p.value=0.05)$adj.P.Val <= 0.05)))
# --- treat: p = P(T >= (|b|-lfc)/se) + P(T >= (|b|+lfc)/se), McCarthy & Smyth 2009 ---
tr <- treat(fit, lfc=log2(1.5))
se <- fit$stdev.unscaled*sqrt(s2post); ab <- abs(fit$coefficients); lfc <- log2(1.5)
ptreat <- pt((ab-lfc)/se, df.total, lower.tail=FALSE) + pt((ab+lfc)/se, df.total, lower.tail=FALSE)
ttreat <- sign(fit$coefficients)*pmax((ab-lfc)/se, 0); ttreat[ab <= lfc] <- 0
cat(sprintf("[treat] p %.1e  t %.1e  df.prior same as eBayes %s\n", maxabs(tr$p.value, ptreat), maxabs(tr$t, ttreat), isTRUE(all.equal(tr$df.prior, eb$df.prior))))
# --- squeezeVar directly, and the df=0 / NA guard ---
sv <- squeezeVar(fit$sigma^2, fit$df.residual)
cat(sprintf("[squeezeVar] var.post %.1e df.prior %.1e\n", maxabs(sv$var.post, s2post), abs(sv$df.prior-d0.hat)))
# --- trend=TRUE: spline regression of e on Amean, port with splines::ns(df=4, intercept) ---
ebt <- eBayes(fit, trend=TRUE)
X <- splines::ns(fit$Amean, df=4, intercept=TRUE); lf <- lm.fit(X, e)
evar.t <- mean(lf$effects[-(1:lf$rank)]^2) - trigamma(d1/2); d0t <- 2*trigamma_inv(evar.t)
s02t <- exp(lf$fitted.values + digamma(d0t/2) - log(d0t/2))
cat(sprintf("[trend] df.prior %.1e  s2.prior(vector) %.1e\n", abs(ebt$df.prior-d0t), maxabs(ebt$s2.prior, s02t)))
# --- robust=TRUE (Phipson 2016): calibration with planted d0 and with outliers ---
ebr <- eBayes(fit, robust=TRUE)
cat(sprintf("[robust, clean data] df.prior: non-robust %.3f, robust min %.3f median %.3f max %.3f (truth %d); genes with df.prior < non-robust: %d\n",
  eb$df.prior, min(ebr$df.prior), median(ebr$df.prior), max(ebr$df.prior), d0, sum(ebr$df.prior < eb$df.prior-1e-8)))
yo <- y; out <- sample(G, 100); yo[out, 1] <- yo[out,1] + 12   # 100 genes with one outlier observation
fo <- lmFit(yo, design); ebo <- eBayes(fo); ebro <- eBayes(fo, robust=TRUE)
cat(sprintf("[robust, 100 outlier genes] non-robust df.prior %.3f; robust df.prior median %.3f, median over outlier genes %.3f, min %.3f; outlier genes have smaller df.prior than the median: %d of 100\n",
  ebo$df.prior, median(ebro$df.prior), median(ebro$df.prior[out]), min(ebro$df.prior), sum(ebro$df.prior[out] < median(ebro$df.prior)-1e-8)))
# winsorizedMoments (the theoretical mean/var of a winsorised log-F) vs numeric integration
wm <- function(df1, df2, p=c(0.05,0.1)) {
  fq <- qf(c(p[1],1-p[2]), df1, df2); zq <- log(fq)
  dens <- function(zz) df(exp(zz), df1, df2)*exp(zz)
  m <- integrate(function(zz) zz*dens(zz), zq[1], zq[2], rel.tol=1e-12)$value + sum(zq*p)
  v <- integrate(function(zz) (zz-m)^2*dens(zz), zq[1], zq[2], rel.tol=1e-12)$value + sum((zq-m)^2*p)
  c(m,v) }
env <- environment(limma:::fitFDistRobustly)
g128 <- statmod::gauss.quad.prob(128, dist="uniform")
wm.limma <- function(df1, df2, winsor.tail.p=c(0.05,0.1)) {  # copy of the code in fitFDistRobustly for direct comparison
  linkfun <- function(x) x/(1+x); linkinv <- function(x) x/(1-x)
  fq <- qf(p=c(winsor.tail.p[1],1-winsor.tail.p[2]),df1=df1,df2=df2); zq <- log(fq); q <- linkfun(fq)
  nodes <- q[1] + (q[2]-q[1]) * g128$nodes; fnodes <- linkinv(nodes); znodes <- log(fnodes)
  f <- df(fnodes,df1=df1,df2=df2)/(1-nodes)^2; q21 <- q[2]-q[1]
  m <- q21*sum(g128$weights*f*znodes) + sum(zq * winsor.tail.p); v <- q21*sum(g128$weights*f*(znodes-m)^2) + sum((zq-m)^2 * winsor.tail.p); c(m,v) }
for(dd in c(4, 20, Inf)) cat(sprintf("[winsorized moments df1=%d df2=%s] quadrature vs integrate: mean %.1e var %.1e\n", d1, dd, abs(wm.limma(d1,dd)[1]-wm(d1,dd)[1]), abs(wm.limma(d1,dd)[2]-wm(d1,dd)[2])))
# --- NA-tolerance: p.adjust in topTable ignores NA p-values; decideTests too ---
yna <- y; yna[1:20, 3:8] <- NA
fna <- eBayes(lmFit(yna, design)); ttn <- topTable(fna, coef=2, number=Inf, sort.by="none")
cat(sprintf("[NA genes] %d genes with df 0; their t/p NA: %s; adj.P on the rest equals BH over non-NA: %.1e\n",
  sum(fna$df.residual==0), all(is.na(fna$p.value[1:20,2])), maxabs(ttn$adj.P.Val[-(1:20)], p.adjust(fna$p.value[-(1:20),2],"BH"))))
