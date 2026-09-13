# Held-up checks: camera (Wu & Smyth 2012) vs an independent port with exact t-to-z
# conversion; fry vs roast with many rotations; zscoreT approximation accuracy (note).
# Run: . ./rlib.sh <version>; Rscript heldup_camera_fry.R
suppressMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), R.version.string, "\n")
mx <- function(a, b) max(abs(a - b), na.rm=TRUE)
trigammaInv <- function(x) uniroot(function(y) trigamma(y) - x, c(1e-4, 1e6), tol=1e-12)$root
set.seed(41)
G <- 3000; n <- 10
grp <- rep(0:1, each=5); design <- cbind(Int=1, grp=grp)
y <- matrix(rnorm(G*n, sd=rep(sqrt(0.05*4/rchisq(G, 4)), n)), G, n) + rnorm(G, 8, 2)
# set 1: 60 genes shifted up; set 2: 80 correlated genes (shared factor); sets 3-20 random
y[1:60, grp==1] <- y[1:60, grp==1] + 0.4
fac <- rnorm(n); y[61:140,] <- y[61:140,] + outer(rnorm(80, 0, 0.5), fac)
index <- c(list(up=1:60, corr=61:140), lapply(3:20, function(i) sample(G, sample(20:200, 1))))
names(index)[3:20] <- paste0("rnd", 3:20)

port_camera <- function(y, design, index, fixed.cor=NULL) {
  p <- ncol(design); G <- nrow(y); n <- ncol(y); df.res <- n - p
  QR <- qr(design); eff <- qr.qty(QR, t(y))
  ut <- eff[p,]; if(QR$qr[p,p] < 0) ut <- -ut
  U <- eff[-(1:p),,drop=FALSE]; s2 <- colMeans(U^2); U <- t(U)/sqrt(pmax(s2, 1e-8))
  e <- log(s2) - digamma(df.res/2) + log(df.res/2); evar <- var(e) - trigamma(df.res/2)
  d0 <- 2*trigammaInv(evar); s0 <- exp(mean(e) - log(d0/2) + digamma(d0/2))
  s2post <- (df.res*s2 + d0*s0)/(df.res + d0)
  modt <- ut/sqrt(s2post); df.total <- min(df.res + d0, G*df.res)
  z <- qnorm(pt(modt, df.total))                        # exact t -> z (camera uses Hill's approximation)
  z[modt > 0] <- -qnorm(pt(modt[modt > 0], df.total, lower.tail=FALSE))
  meanz <- mean(z); varz <- var(z)
  out <- t(sapply(index, function(iset) {
    m <- length(iset); m2 <- G - m
    if(is.null(fixed.cor)) { vif <- m*mean(colMeans(U[iset,,drop=FALSE])^2); cor <- (vif-1)/(m-1); dfc <- min(df.res, G-2) }
    else { cor <- fixed.cor; vif <- 1 + (m-1)*cor; dfc <- G-2 }
    vif <- max(1, vif)
    delta <- G/m2*(mean(z[iset]) - meanz)
    vp <- ((G-1)*varz - delta^2*m*m2/G)/(G-2)
    t2 <- delta/sqrt(vp*(vif/m + 1/m2))
    c(m, cor, 2*pt(-abs(t2), dfc), if(t2 < 0) 1 else 2)
  }))
  data.frame(NGenes=out[,1], Correlation=out[,2], PValue=out[,3], Direction=c("Down","Up")[out[,4]], row.names=names(index))
}
cm <- camera(y, index, design, inter.gene.cor=NA, sort=FALSE)      # estimated correlations
pc <- port_camera(y, design, index)
cat(sprintf("A. camera (estimated inter-gene correlation): NGenes ok %s; correlation %.2e; PValue max |diff| %.2e, max relative %.2e; Direction ok %s\n",
            all(cm$NGenes == pc$NGenes), mx(cm$Correlation, pc$Correlation), mx(cm$PValue, pc$PValue), max(abs(cm$PValue/pc$PValue - 1)), all(cm$Direction == pc$Direction)))
cat(sprintf("   set 'up': camera p %.3g port %.3g; set 'corr': correlation %.4f, p %.3g (port %.3g); FDR == BH: %s\n", cm["up","PValue"], pc["up","PValue"], cm["corr","Correlation"], cm["corr","PValue"], pc["corr","PValue"], isTRUE(all.equal(cm$FDR, p.adjust(cm$PValue, "BH")))))
cm2 <- camera(y, index, design, sort=FALSE)                         # default inter.gene.cor=0.01
pc2 <- port_camera(y, design, index, fixed.cor=0.01)
cat(sprintf("   camera (inter.gene.cor=0.01 default): PValue max |diff| %.2e, max relative %.2e\n", mx(cm2$PValue, pc2$PValue), max(abs(cm2$PValue/pc2$PValue-1))))
# the moderated t inside camera equals lmFit+eBayes and the z-scores equal zscoreT
fe <- eBayes(lmFit(y, design)); cm3 <- camera(y, list(a=1:60), design, use.ranks=TRUE, inter.gene.cor=0, sort=FALSE)
w <- wilcox.test(fe$t[1:60, 2], fe$t[-(1:60), 2], exact=FALSE, correct=FALSE)$p.value
cat(sprintf("   use.ranks=TRUE, inter.gene.cor=0: p %.4g vs normal-approximation Wilcoxon on eBayes t: %.4g\n", cm3$PValue, w))

## ---- B. fry vs roast with many rotations ------------------------------------------------
set.seed(42)
fr <- fry(y, index[1:3], design, sort=FALSE)
ro <- mroast(y, index[1:3], design, nrot=49999, sort="none")
cat("B. fry vs mroast(nrot=49999), directional PValue:\n"); print(cbind(fry=fr$PValue, roast=ro$PValue, fry.mixed=fr$PValue.Mixed, roast.mixed=ro$PValue.Mixed))
cat(sprintf("   fry directional p == 2*pt(-|t|, df.residual) with t from the effects matrix: %s\n",
            isTRUE(all.equal(fr$PValue, 2*pt(-abs(qt(fr$PValue/2, n-2)), n-2)))))

## ---- C. zscoreT approximations vs exact (note) ---------------------------------------------
t <- seq(-8, 8, by=0.05); dfs <- c(3, 5, 10, 30, 100)
ex <- function(t, df) ifelse(t > 0, -qnorm(pt(t, df, lower.tail=FALSE)), qnorm(pt(t, df)))
for(df in dfs) cat(sprintf("C. zscoreT df=%3d: max |hill - exact| %.2e   max |bailey - exact| %.2e   (approx=FALSE) %.2e\n", df,
   mx(zscoreT(t, df, approx=TRUE, method="hill"), ex(t, df)), mx(zscoreT(t, df, approx=TRUE, method="bailey"), ex(t, df)), mx(zscoreT(t, df, approx=FALSE), ex(t, df))))
