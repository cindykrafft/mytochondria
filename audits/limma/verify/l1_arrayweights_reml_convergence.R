# arrayWeights(method="reml") with prior observation weights (.arrayWeightsPrWtsREML) vs without
# (.arrayWeightsREML): same model, same data, unit prior weights -> must agree. Traces the
# Fisher-scoring iterations of both, recomputes the REML+prior score at the returned weights
# with an independent lm.wfit loop, and shows the effect of tol on the weighted path.
suppressPackageStartupMessages(library(limma))
cat("limma", as.character(packageVersion("limma")), "\n")
set.seed(17)
G <- 3000; n <- 9
design2 <- cbind(1, rep(c(0,1), length.out=n)); sdv <- exp(c(-0.5,0,0.5,0,0,0,0.6,-0.6,0))
ya <- matrix(rnorm(G*n), G, n)*rep(sdv, each=G) + 6
w1 <- matrix(1, G, n); Z2 <- contr.sum(n)
score <- function(w, wp) { s <- rep(0,n); for(g in 1:G) { f <- lm.wfit(design2, ya[g,], w*wp[g,]); s2 <- mean(f$effects[-(1:f$rank)]^2); h <- hat(f$qr); if(s2>1e-15) s <- s + w*wp[g,]*f$residuals^2/s2 - (1-h) }; s <- s + 10*(w-1); max(abs(crossprod(Z2, s)))/(G+10) }
cat("--- .arrayWeightsREML trace (no prior weights), tol=1e-5\n"); aw.r <- arrayWeights(ya, design2, method="reml", trace=TRUE)
cat("--- .arrayWeightsPrWtsREML trace (unit prior weights), tol=1e-5\n"); aw.w <- arrayWeights(ya, design2, weights=w1, method="reml", trace=TRUE)
cat(sprintf("weights no-prior-weights : %s\nweights unit-prior-weights: %s\nmax |diff| %.3e\n", paste(sprintf("%.4f",aw.r),collapse=" "), paste(sprintf("%.4f",aw.w),collapse=" "), max(abs(aw.r-aw.w))))
cat(sprintf("independent REML+prior score |Z2'z|/(G+prior.n): no-weights path %.2e, unit-weights path %.2e\n", score(aw.r, w1), score(aw.w, w1)))
for(tl in c(1e-5, 1e-8, 1e-11, 1e-14)) { a <- suppressWarnings(arrayWeights(ya, design2, weights=w1, method="reml", tol=tl, maxiter=200)); cat(sprintf("unit-weights path tol=%g: max |diff| vs no-weights path %.2e, score %.2e\n", tl, max(abs(a-aw.r)), score(a, w1))) }
# with genuine (voom-like) prior weights: converged (tiny tol) vs default
wp <- matrix(rexp(G*n), G, n)
a5 <- arrayWeights(ya, design2, weights=wp, method="reml"); a14 <- suppressWarnings(arrayWeights(ya, design2, weights=wp, method="reml", tol=1e-14, maxiter=500))
cat(sprintf("random prior weights: default tol -> %s\n                      tol=1e-14  -> %s\n  max |diff| %.3e; scores %.2e vs %.2e\n", paste(sprintf("%.4f",a5),collapse=" "), paste(sprintf("%.4f",a14),collapse=" "), max(abs(a5-a14)), score(a5,wp), score(a14,wp)))
# the same through voom + arrayWeights(method="reml"), the voomLmFit path
counts <- matrix(rnbinom(G*n, mu=rep(2^runif(G,3,10), n), size=10), G, n)
v <- voom(counts, design2)
cat("--- voom weights, method='reml' trace\n"); av <- arrayWeights(v, design2, method="reml", trace=TRUE)
av14 <- suppressWarnings(arrayWeights(v, design2, method="reml", tol=1e-14, maxiter=500))
cat(sprintf("voom + reml: default %s\n             tol=1e-14 %s\n  max |diff| %.3e\n", paste(sprintf("%.4f",av),collapse=" "), paste(sprintf("%.4f",av14),collapse=" "), max(abs(av-av14))))
