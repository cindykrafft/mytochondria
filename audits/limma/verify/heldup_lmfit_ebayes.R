# Held-up checks (and notes N-F, N-T) for lmFit / contrasts.fit / eBayes / treat / topTable /
# decideTests against per-gene lm.wfit closed forms and an independent port of Smyth (2004).
# Run: . ./rlib.sh <version>; Rscript heldup_lmfit_ebayes.R
suppressMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), R.version.string, "\n")
mx <- function(a, b) max(abs(a - b), na.rm=TRUE)

## ---- independent port of the Smyth (2004) hyperparameter estimator -------------------
trigammaInv <- function(x) uniroot(function(y) trigamma(y) - x, c(1e-4, 1e6), tol=1e-12)$root
port_fitFDist <- function(s2, d) {                  # equal d only
  e <- log(s2) - digamma(d/2) + log(d/2)
  emean <- mean(e); evar <- var(e) - trigamma(d/2)
  if(evar > 0) { d0 <- 2*trigammaInv(evar); s0 <- exp(emean - log(d0/2) + digamma(d0/2)) } else { d0 <- Inf; s0 <- mean(s2) }
  list(s0=s0, d0=d0)
}

## ---- A. lmFit vs per-gene weighted least squares with missing values ------------------
set.seed(11)
G <- 3000; n <- 10
design <- cbind(Int=1, x1=rnorm(n), x2=rep(0:1, each=5))       # non-orthogonal
y <- matrix(rnorm(G*n), G, n) + rnorm(G, 8, 2)
W <- matrix(rexp(G*n, 1), G, n)
y[sample(G*n, 200)] <- NA
fit <- lmFit(y, design, weights=W)
b <- s <- matrix(NA, G, 3); sig <- df <- rep(NA, G)
for(g in 1:G) {
  o <- is.finite(y[g,]); X <- design[o,,drop=FALSE]; w <- W[g,o]; yy <- y[g,o]
  V <- solve(crossprod(X*sqrt(w))); bb <- V %*% crossprod(X*w, yy)
  r <- yy - X %*% bb; b[g,] <- bb; s[g,] <- sqrt(diag(V)); df[g] <- sum(o)-3; sig[g] <- sqrt(sum(w*r^2)/df[g])
}
cat(sprintf("A. lmFit(weights, NAs) vs closed-form WLS: coef %.2e  stdev.unscaled %.2e  sigma %.2e  df.residual %d\n",
            mx(fit$coefficients, b), mx(fit$stdev.unscaled, s), mx(fit$sigma, sig), mx(fit$df.residual, df)))
fit0 <- lmFit(y[,], design)                                   # NAs, no weights
b0 <- t(apply(y, 1, function(v) { o <- is.finite(v); lm.fit(design[o,,drop=FALSE], v[o])$coefficients }))
cat(sprintf("   lmFit(NAs, no weights) vs lm.fit per gene: coef %.2e\n", mx(fit0$coefficients, b0)))

## ---- B. contrasts.fit is exact without weights, non-orthogonal design -----------------
yc <- matrix(rnorm(G*n), G, n) + rnorm(G, 8, 2)
fitc <- lmFit(yc, design)
C <- cbind(a=c(0,1,-1), b=c(0,1,1), c=c(0,0,1))
cf <- contrasts.fit(fitc, C)
V <- solve(crossprod(design)); exact <- sqrt(diag(t(C) %*% V %*% C))
cat(sprintf("B. contrasts.fit (no weights): coef %.2e  stdev.unscaled vs sqrt(diag(C'VC)) %.2e  cov.coefficients %.2e\n",
            mx(cf$coefficients, fitc$coefficients %*% C), mx(cf$stdev.unscaled, matrix(exact, G, 3, byrow=TRUE)), mx(cf$cov.coefficients, t(C) %*% V %*% C)))

## ---- C. eBayes vs the port (equal df, legacy path) ------------------------------------
set.seed(12)
d0true <- 4; s0true <- 0.05
s2g <- s0true * d0true / rchisq(G, d0true)
ye <- matrix(rnorm(G*n, sd=rep(sqrt(s2g), n)), G, n) + rnorm(G, 8, 2)
ye[1:300, 6:10] <- ye[1:300, 6:10] + rnorm(300, 0, 1)            # 300 DE genes on x2
fe <- lmFit(ye, design); eb <- eBayes(fe)
pp <- port_fitFDist(fe$sigma^2, fe$df.residual[1])
d <- fe$df.residual[1]
s2post <- (d*fe$sigma^2 + pp$d0*pp$s0)/(d + pp$d0)
tt <- fe$coefficients/fe$stdev.unscaled/sqrt(s2post)
dft <- min(d + pp$d0, G*d)
pv <- 2*pt(-abs(tt), dft)
cat(sprintf("C. eBayes: df.prior %.6f (port %.6f, true %g)  s2.prior %.6f (port %.6f, true %g)\n", eb$df.prior, pp$d0, d0true, eb$s2.prior, pp$s0, s0true))
cat(sprintf("   s2.post %.2e  t %.2e  p.value %.2e  df.total %.2e (df.total = %g)\n", mx(eb$s2.post, s2post), mx(eb$t, tt), mx(eb$p.value, pv), mx(eb$df.total, dft), eb$df.total[1]))
# legacy=TRUE gives the same as the default on equal df; the new estimator differs slightly
if("legacy" %in% names(formals(eBayes))) {
  eb2 <- eBayes(fe, legacy=TRUE); eb3 <- eBayes(fe, legacy=FALSE)
  cat(sprintf("   legacy=TRUE identical to default: %s;  legacy=FALSE (fitFDistUnequalDF1) df.prior %.4f s2.prior %.6f\n", identical(eb2$t, eb$t), eb3$df.prior, eb3$s2.prior))
} else cat("   (no legacy argument in this version)\n")
# B-statistic closed form given the estimated var.prior (Smyth 2004 eq. for the log-odds)
v0 <- eb$var.prior; r <- t(t(fe$stdev.unscaled^2) + v0)/fe$stdev.unscaled^2   # (v1+v0)/v1 per column
lods <- log(0.01/0.99) - log(r)/2 + (1+eb$df.total)/2*log((eb$t^2+eb$df.total)/(eb$t^2/r+eb$df.total))
cat(sprintf("   B-statistic closed form given var.prior: %.2e (var.prior = %s)\n", mx(eb$lods, lods), paste(format(v0, digits=4), collapse=" ")))
# moderated F for coefficients 2:3 vs b' V^-1 b / (r s2.post)
Vc <- solve(crossprod(design))[2:3, 2:3]; bb <- fe$coefficients[,2:3]
Fp <- rowSums((bb %*% solve(Vc)) * bb)/2/eb$s2.post
ebF <- eBayes(fe[,2:3])
cat(sprintf("   moderated F (coef 2:3) vs b'V^-1 b/(2 s2.post): %.2e ; F.p.value vs pf(.,2,df.prior+df.residual): %.2e\n",
            mx(ebF$F, Fp), mx(ebF$F.p.value, pf(Fp, 2, eb$df.prior + d, lower.tail=FALSE))))
# calibration of the moderated t on the null genes for coefficient x1 (all null)
cat(sprintf("   null coefficient x1: fraction p<0.05 = %.4f (%d genes), KS p = %.3f\n", mean(eb$p.value[,"x1"] < 0.05), G, ks.test(eb$p.value[,"x1"], "punif")$p.value))
# trend=TRUE: the prior varies with Amean and the estimator with a numeric trend reproduces it
ebt <- eBayes(fe, trend=TRUE)
cat(sprintf("   trend=TRUE: s2.prior range %.5f..%.5f, df.prior %.4f; trend=fe$Amean identical: %s\n", min(ebt$s2.prior), max(ebt$s2.prior), ebt$df.prior, identical(eBayes(fe, trend=fe$Amean)$t, ebt$t)))

## ---- D. treat p-values (McCarthy & Smyth 2009) ---------------------------------------
tr <- treat(fe, lfc=0.3)
se <- fe$stdev.unscaled*sqrt(tr$s2.post); ac <- abs(fe$coefficients)
ptr <- pt((ac-0.3)/se, tr$df.total, lower.tail=FALSE) + pt((ac+0.3)/se, tr$df.total, lower.tail=FALSE)
ttr <- ifelse(ac > 0.3, sign(fe$coefficients)*pmax((ac-0.3)/se, 0), 0)
cat(sprintf("D. treat(lfc=0.3): p.value %.2e  t %.2e  (df.prior %.6f = eBayes %s)\n", mx(tr$p.value, ptr), mx(tr$t, ttr), tr$df.prior, isTRUE(all.equal(tr$df.prior, eb$df.prior))))

## ---- E. topTable: BH over all genes, thinning after adjustment, confint ---------------
tab <- topTable(eb, coef="x2", n=Inf, sort.by="none")
cat(sprintf("E. topTable adj.P.Val vs p.adjust(BH) over all genes: %.2e ; sorted by B: %s\n", mx(tab$adj.P.Val, p.adjust(eb$p.value[,"x2"], "BH")), !is.unsorted(-topTable(eb, coef="x2", n=Inf)$B)))
tab5 <- topTable(eb, coef="x2", n=Inf, p.value=0.05, sort.by="none")
cat(sprintf("   p.value=0.05: %d rows, all adj.P.Val <= 0.05 and equal to the unfiltered BH values: %s\n", nrow(tab5), all(tab5$adj.P.Val <= 0.05) && isTRUE(all.equal(tab5$adj.P.Val, tab$adj.P.Val[tab$adj.P.Val <= 0.05]))))
tci <- topTable(eb, coef="x2", n=Inf, sort.by="none", confint=TRUE)
me <- qt(0.975, eb$df.total)*fe$stdev.unscaled[,"x2"]*sqrt(eb$s2.post)
cat(sprintf("   confint=TRUE: CI.L/CI.R vs logFC -/+ qt(0.975, df.total)*se: %.2e %.2e\n", mx(tci$CI.L, tab$logFC - me), mx(tci$CI.R, tab$logFC + me)))

## ---- F. decideTests ------------------------------------------------------------------
dt <- decideTests(eb)                                   # separate, BH, 0.05
padj <- apply(eb$p.value, 2, p.adjust, method="BH")
cat(sprintf("F. decideTests(separate) == sign(coef)*(BH per column < 0.05): %s\n", all(dt@.Data == sign(fe$coefficients)*(padj < 0.05))))
dg <- decideTests(eb, method="global")
pg <- eb$p.value; pg[] <- p.adjust(pg, "BH")
cat(sprintf("   decideTests(global) == sign(coef)*(BH over the whole matrix < 0.05): %s\n", all(dg@.Data == sign(fe$coefficients)*(pg < 0.05))))
# hierarchical port: F-test selects genes, then per-gene BH at a reduced cutoff
sel <- p.adjust(eb$F.p.value, "BH") < 0.05; a <- sum(sel)/G
h <- matrix(0, G, 3); for(g in which(sel)) h[g,] <- sign(fe$coefficients[g,])*(p.adjust(eb$p.value[g,], "BH") < 0.05*a)
dh <- decideTests(eb, method="hierarchical")
cat(sprintf("   decideTests(hierarchical) == port (F-selected %d genes, cutoff 0.05*%.4f): %s\n", sum(sel), a, all(dh@.Data == h)))
dn <- decideTests(eb, method="nestedF")
cat(sprintf("   decideTests(nestedF): %d genes with any call, all within the F-selected set: %s\n", sum(rowSums(dn@.Data != 0) > 0), all(rowSums(dn@.Data != 0)[!sel] == 0)))
# Note N-T: strict '<' in decideTests, '<=' in topTable(p.value=): a gene whose BH-adjusted p is exactly 0.05
for(GG in 1000:1100) { q1 <- p.adjust(c(0.05/GG, rep(1, GG-1)), "BH")[1]; if(q1 == 0.05) break }
p0 <- cbind(x2=c(0.05/GG, rep(1, GG-1)))
cat(sprintf("   N-T: %d genes, gene 1 with BH-adjusted p == 0.05 exactly (%s): decideTests(p.value=0.05) calls it %d; topTable(p.value=0.05) keeps it: %s\n", GG, q1 == 0.05,
            decideTests(p0, p.value=0.05)[1,1], nrow(topTable(eBayes(lmFit(matrix(rnorm(GG*n), GG, n), design)), coef=1, n=Inf, p.value=q1)) >= 0 && q1 <= 0.05))

## ---- G. Note N-F: F-test df2 is df.prior+df.residual, uncapped, unlike df.total -------
# df.total for the moderated t is min(df.prior+df.residual, sum(df.residual)); the F p-value in eBayes uses df.prior+df.residual.
# Reachable only when df.prior is finite and exceeds the pooled df (few genes): search seeds for such a case.
for(sd in 1:200) { set.seed(sd); f12 <- lmFit(matrix(rnorm(12*n, sd=0.2), 12, n), design); e12 <- eBayes(f12); if(is.finite(e12$df.prior) && e12$df.prior > 12*d) break }
cat(sprintf("G. 12-gene fit (seed %d): df.residual %d each, pooled %d, df.prior %.4g; df.total used for t = %g; df2 used for F = %g (= df.prior+df.residual)\n",
            sd, d, 12*d, e12$df.prior, e12$df.total[1], e12$df.prior + d))
Fp2 <- pf(e12$F, attr(classifyTestsF(e12, fstat.only=TRUE), "df1"), e12$df.total, lower.tail=FALSE)
cat(sprintf("   F.p.value (df2 = df.prior+df.residual) vs pf with df2 = df.total: max |diff| %.2e (p range %.3g..%.3g)\n", mx(e12$F.p.value, Fp2), min(e12$F.p.value), max(e12$F.p.value)))
