# decideTests (separate/global/hierarchical/nestedF) vs ports of the documented rules;
# topTable vs decideTests threshold; arrayWeights REML vs genebygene vs the devel C backend.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(17)
maxabs <- function(a,b) max(abs(as.matrix(a)-as.matrix(b)), na.rm=TRUE)
G <- 3000; n <- 9
design <- cbind(Int=1, A=rep(c(0,1,0),each=3), B=rep(c(0,0,1),each=3))
beta <- cbind(rnorm(G,6), ifelse(runif(G)<0.15, rnorm(G,0,1.5), 0), ifelse(runif(G)<0.15, rnorm(G,0,1.5), 0))
y <- beta %*% t(design) + matrix(rnorm(G*n), G, n)*rep(sqrt(0.1*4/rchisq(G,4)), n)
fit <- eBayes(lmFit(y, design)); p <- fit$p.value[,2:3]; cf <- fit$coefficients[,2:3]; fit23 <- fit[,2:3]
# separate
ds <- decideTests(fit23, method="separate", p.value=0.05)
ref <- sign(cf)*(apply(p,2,p.adjust,method="BH") < 0.05)
cat(sprintf("[separate] mismatches %d; counts Up/Down: %s\n", sum(ds@.Data != ref), paste(colSums(ds@.Data==1), colSums(ds@.Data==-1), collapse=" ")))
dg <- decideTests(fit23, method="global", p.value=0.05); pg <- p; pg[] <- p.adjust(p, "BH")
cat(sprintf("[global] mismatches %d\n", sum(dg@.Data != sign(cf)*(pg < 0.05))))
# hierarchical: select genes by BH on the F p-value, then within selected genes adjust row-wise (Holm-like via adjust.method) at a*p
dh <- decideTests(fit23, method="hierarchical", p.value=0.05)
sel <- p.adjust(fit23$F.p.value, "BH") < 0.05; a <- sum(sel)/G
refh <- matrix(0, G, 2); for(g in which(sel)) refh[g,] <- sign(cf[g,])*(p.adjust(p[g,], "BH") < 0.05*a)
cat(sprintf("[hierarchical] mismatches %d (selected genes %d, row-level threshold %.4f)\n", sum(dh@.Data != refh), sum(sel), 0.05*a))
# nestedF: within selected genes, classifyTestsF at threshold a*p: t' R^-1 t / r > qf, then peel by |t|
dn <- decideTests(fit23, method="nestedF", p.value=0.05)
Rc <- cov2cor(fit23$cov.coefficients); Rinv <- solve(Rc); qF <- qf(0.05*a, 2, fit23$df.prior+fit23$df.residual[1], lower.tail=FALSE)
refn <- matrix(0, G, 2)
for(g in which(sel)) { x <- fit23$t[g,]; Fx <- function(v) drop(t(v) %*% Rinv %*% v)/2
  if(Fx(x) > qF) { o <- order(abs(x), decreasing=TRUE); refn[g,o[1]] <- sign(x[o[1]]); x2 <- x; x2[o[1]] <- sign(x[o[1]])*abs(x[o[2]]); if(Fx(x2) > qF) refn[g,o[2]] <- sign(x[o[2]]) } }
cat(sprintf("[nestedF] mismatches %d; F from classifyTestsF equals t'R^-1t/2: %.1e\n", sum(dn@.Data != refn), maxabs(fit23$F, apply(fit23$t,1,function(v) drop(t(v)%*%Rinv%*%v)/2))))
# lfc and the threshold convention
dl <- decideTests(fit23, p.value=0.05, lfc=1)
cat(sprintf("[lfc=1] equals separate result masked by |logFC|>1: %d mismatches\n", sum(dl@.Data != ds@.Data*(abs(cf)>1))))
padj <- p.adjust(p[,1],"BH"); thr <- padj[order(abs(padj-0.05))[1]]  # an attained adjusted p-value used as the threshold
cat(sprintf("[threshold convention] with p.value set to an attained adj.P (%.6f): topTable keeps %d genes (<=), decideTests flags %d (<)\n", thr,
  nrow(topTable(fit23, coef=1, number=Inf, p.value=thr)), sum(decideTests(fit23, p.value=thr)@.Data[,1]!=0)))
# --- arrayWeights ---
design2 <- cbind(1, rep(c(0,1), length.out=n)); sdv <- exp(c(-0.5,0,0.5,0,0,0,0.6,-0.6,0))
ya <- matrix(rnorm(G*n), G, n)*rep(sdv, each=G) + 6
aw.r <- arrayWeights(ya, design2, method="reml"); aw.g <- arrayWeights(ya, design2, method="genebygene")
cat(sprintf("[arrayWeights] true 1/sd^2 = %s\n  reml       = %s\n  genebygene = %s\n", paste(sprintf("%.3f",1/sdv^2),collapse=" "), paste(sprintf("%.3f",aw.r),collapse=" "), paste(sprintf("%.3f",aw.g),collapse=" ")))
cat(sprintf("  reml vs truth max |log ratio| %.3f; genebygene vs truth %.3f; product of weights (geometric mean 1): %.1e %.1e\n",
  max(abs(log(aw.r*sdv^2))), max(abs(log(aw.g*sdv^2))), abs(mean(log(aw.r))), abs(mean(log(aw.g)))))
# REML with prior weights (C on devel, R on release): unit prior weights must reproduce the no-weights REML
w1 <- matrix(1, G, n); aw.rw <- arrayWeights(ya, design2, weights=w1, method="reml")
cat(sprintf("[arrayWeights reml, unit prior weights] vs reml without weights: %.1e\n", maxabs(aw.rw, aw.r)))
wp <- matrix(rexp(G*n), G, n); aw.pw <- arrayWeights(ya, design2, weights=wp, method="reml"); aw.pg <- arrayWeights(ya, design2, weights=wp, method="genebygene")
cat(sprintf("[arrayWeights reml, random prior weights] = %s\n  genebygene with the same weights = %s\n", paste(sprintf("%.5f",aw.pw),collapse=" "), paste(sprintf("%.5f",aw.pg),collapse=" ")))
# the REML fixed point: at convergence the averaged score Z2'z must be ~0 (recomputed independently with lm.wfit)
Z2 <- contr.sum(n); score <- rep(0, n); info <- 0
for(g in 1:G) { f <- lm.wfit(design2, ya[g,], aw.pw*wp[g,]); s2 <- mean(f$effects[-(1:f$rank)]^2); h <- hat(f$qr); if(s2 > 1e-15) score <- score + aw.pw*wp[g,]*f$residuals^2/s2 - (1-h) }
score <- score + 10*(aw.pw-1)
cat(sprintf("  REML+prior score at the returned weights: max |Z2'z|/(G+prior.n) = %.2e (tol 1e-5 on the scoring criterion)\n", max(abs(crossprod(Z2, score)))/(G+10)))
# var.group
vg <- arrayWeights(ya, design2, var.group=rep(1:3, each=3), method="reml")
cat(sprintf("[var.group] weights constant within group: %s; values %s\n", all(tapply(vg, rep(1:3,each=3), function(v) diff(range(v)))<1e-12), paste(sprintf("%.3f", vg[c(1,4,7)]), collapse=" ")))
