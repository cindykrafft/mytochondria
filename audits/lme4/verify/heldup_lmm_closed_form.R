## Held-up checks for lme4's linear mixed-model core, against closed forms,
## a dense direct maximisation of the marginal (RE)ML criterion, and nlme::lme.
##
## Run:  Rscript heldup_lmm_closed_form.R            (library on R_LIBS_USER)
## Every number printed here is reproduced in ../component-reviews/numerical-core.md
## from this file's captured .out.
suppressPackageStartupMessages({library(lme4); library(Matrix); library(nlme)})
cat("lme4", as.character(packageVersion("lme4")), "from",
    dirname(system.file(package = "lme4")), "\n")
cat("nlme", as.character(packageVersion("nlme")), "|", R.version.string, "\n\n")
options(digits = 10, width = 120)
f10 <- function(x) format(x, digits = 10)
rel <- function(a, b) max(abs(a - b) / pmax(abs(b), 1e-12))

## ---- dense reference: -2 log L (ML) and -2 log L_R (REML) for y ~ N(X beta, Z G Z' + s2 W^-1)
dense_crit <- function(y, X, Z, G, s2, w = rep(1, length(y)), REML = TRUE) {
    n <- length(y); p <- ncol(X)
    V  <- Z %*% G %*% t(Z) + s2 * diag(1 / w, n)
    Vi <- solve(V)
    XtVi <- t(X) %*% Vi
    beta <- solve(XtVi %*% X, XtVi %*% y)
    r <- y - X %*% beta
    ldV <- as.numeric(determinant(V, logarithm = TRUE)$modulus)
    q <- drop(t(r) %*% Vi %*% r)
    crit <- if (REML) {
        ldV + as.numeric(determinant(XtVi %*% X, logarithm = TRUE)$modulus) + q + (n - p) * log(2 * pi)
    } else ldV + q + n * log(2 * pi)
    list(crit = crit, beta = drop(beta), vcov = solve(XtVi %*% X), Vi = Vi, r = drop(r))
}

## =====================================================================
## A. balanced one-way random-effects ANOVA: closed-form REML and ML
## =====================================================================
set.seed(101)
a <- 12; n <- 5
g <- gl(a, n, labels = sprintf("g%02d", 1:a))
y <- 10 + rnorm(a, sd = 2)[g] + rnorm(a * n, sd = 1.5)
d1 <- data.frame(y, g)
MSA <- n * sum((tapply(y, g, mean) - mean(y))^2) / (a - 1)
MSE <- sum((y - ave(y, g))^2) / (a * (n - 1))
cf <- list(REML = c(sa2 = (MSA - MSE) / n, se2 = MSE),
           ML   = c(sa2 = ((a - 1) / a * MSA - MSE) / n, se2 = MSE))
cat("A. balanced one-way, a =", a, "groups x n =", n, "; MSA =", f10(MSA), " MSE =", f10(MSE), "\n")
for (REML in c(TRUE, FALSE)) {
    fit <- lmer(y ~ 1 + (1 | g), d1, REML = REML)
    vc <- as.data.frame(VarCorr(fit))
    est <- c(sa2 = vc$vcov[1], se2 = vc$vcov[2])
    tru <- cf[[if (REML) "REML" else "ML"]]
    se.int <- sqrt((n * tru[["sa2"]] + tru[["se2"]]) / (a * n))
    X <- matrix(1, a * n); Z <- model.matrix(~ 0 + g)
    ref <- dense_crit(y, X, Z, diag(tru[["sa2"]], a), tru[["se2"]], REML = REML)
    cat(sprintf("  %-4s sigma_a^2 lmer %s closed %s | sigma_e^2 lmer %s closed %s | max rel err %.2e\n",
                if (REML) "REML" else "ML", f10(est[["sa2"]]), f10(tru[["sa2"]]),
                f10(est[["se2"]]), f10(tru[["se2"]]), rel(est, tru)))
    cat(sprintf("       intercept %s (closed %s), SE %s (closed %s) | -2logL lmer %s dense %s\n",
                f10(fixef(fit)[[1]]), f10(mean(y)), f10(sqrt(vcov(fit)[1, 1])), f10(se.int),
                f10(-2 * as.numeric(logLik(fit))), f10(ref$crit)))
    ## nlme
    nl <- lme(y ~ 1, random = ~ 1 | g, data = d1, method = if (REML) "REML" else "ML")
    cat(sprintf("       nlme::lme sigma_a^2 %s sigma_e^2 %s logLik lme %s lmer %s\n",
                f10(as.numeric(VarCorr(nl)[1, 1])), f10(nl$sigma^2),
                f10(as.numeric(logLik(nl))), f10(as.numeric(logLik(fit)))))
}
## conditional modes and variances, closed form for the one-way model (REML fit)
fit1 <- lmer(y ~ 1 + (1 | g), d1)
vc <- as.data.frame(VarCorr(fit1)); sa2 <- vc$vcov[1]; se2 <- vc$vcov[2]
shrink <- n * sa2 / (n * sa2 + se2)
b.cf <- shrink * (tapply(y, g, mean) - fixef(fit1)[[1]])
cv.cf <- 1 / (n / se2 + 1 / sa2)
rr <- ranef(fit1, condVar = TRUE)
cat(sprintf("  ranef vs shrinkage closed form: max abs diff %.2e ; condVar lmer %s closed %s\n",
            max(abs(rr$g[, 1] - b.cf)), f10(attr(rr$g, "postVar")[1, 1, 1]), f10(cv.cf)))

## =====================================================================
## B. balanced two-level nested design: closed-form REML
## =====================================================================
set.seed(202)
A <- 6; B <- 4; m <- 3
dd <- expand.grid(rep = 1:m, B = 1:B, A = 1:A)
dd$A <- factor(dd$A); dd$B <- factor(dd$B)
dd$y <- 5 + rnorm(A, sd = 1.8)[dd$A] + rnorm(A * B, sd = 1.2)[interaction(dd$A, dd$B)] + rnorm(nrow(dd), sd = 0.9)
ybar.a  <- ave(dd$y, dd$A); ybar.ab <- ave(dd$y, dd$A, dd$B)
MSA2 <- B * m * sum((tapply(dd$y, dd$A, mean) - mean(dd$y))^2) / (A - 1)
cm <- tapply(dd$y, list(dd$A, dd$B), mean)          # A x B cell means (balanced, so rowMeans = A means)
MSB2 <- m * sum(sweep(cm, 1, rowMeans(cm))^2) / (A * (B - 1))
MSE2 <- sum((dd$y - ybar.ab)^2) / (A * B * (m - 1))
cf2 <- c(sa2 = (MSA2 - MSB2) / (B * m), sb2 = (MSB2 - MSE2) / m, se2 = MSE2)
fit2 <- lmer(y ~ 1 + (1 | A / B), dd)
vc2 <- as.data.frame(VarCorr(fit2))
est2 <- c(sa2 = vc2$vcov[vc2$grp == "A"], sb2 = vc2$vcov[vc2$grp == "B:A"], se2 = vc2$vcov[vc2$grp == "Residual"])
cat("\nB. balanced nested A/B (", A, "x", B, "x", m, "): REML lmer vs closed form\n")
print(rbind(lmer = est2, closed = cf2))
cat(sprintf("  max rel err %.2e\n", rel(est2, cf2)))
nl2 <- lme(y ~ 1, random = ~ 1 | A / B, data = dd)
cat(sprintf("  nlme::lme: sigma_a^2 %s sigma_b^2 %s sigma_e^2 %s ; logLik lme %s lmer %s\n",
            f10(as.numeric(VarCorr(nl2)[2, 1])), f10(as.numeric(VarCorr(nl2)[4, 1])), f10(nl2$sigma^2),
            f10(as.numeric(logLik(nl2))), f10(as.numeric(logLik(fit2)))))

## =====================================================================
## C. sleepstudy: correlated random slopes vs direct dense maximisation and nlme
## =====================================================================
data(sleepstudy, package = "lme4")
X <- model.matrix(~ Days, sleepstudy)
Zs <- as.matrix(getME(lmer(Reaction ~ Days + (Days | Subject), sleepstudy), "Z"))
ns <- nlevels(sleepstudy$Subject)
mkG <- function(par) { Lc <- matrix(0, 2, 2); Lc[lower.tri(Lc, TRUE)] <- par[1:3]; kronecker(diag(ns), Lc %*% t(Lc)) }
obj <- function(par, REML) tryCatch(dense_crit(sleepstudy$Reaction, X, Zs, mkG(par), exp(par[4]), REML = REML)$crit,
                                    error = function(e) 1e10)
cat("\nC. sleepstudy Reaction ~ Days + (Days | Subject)\n")
for (REML in c(TRUE, FALSE)) {
    fit <- lmer(Reaction ~ Days + (Days | Subject), sleepstudy, REML = REML)
    best <- NULL
    for (st in list(c(24, 0.4, 6, log(650)), c(15, 2, 3, log(400)), c(35, -3, 9, log(1000)))) {
        o <- optim(st, obj, REML = REML, method = "L-BFGS-B", lower = c(0, -Inf, 0, log(10)),
                   upper = c(Inf, Inf, Inf, log(1e5)), control = list(factr = 10, maxit = 5000))
        o <- optim(o$par, obj, REML = REML, method = "Nelder-Mead", control = list(reltol = 1e-15, maxit = 10000))
        if (is.null(best) || o$value < best$value) best <- o
    }
    G <- mkG(best$par)[1:2, 1:2]
    ref <- dense_crit(sleepstudy$Reaction, X, Zs, mkG(best$par), exp(best$par[4]), REML = REML)
    vc <- as.data.frame(VarCorr(fit))
    cat(sprintf("  %-4s -2logL lmer %s | direct optim %s | diff %.3e\n", if (REML) "REML" else "ML",
                f10(-2 * as.numeric(logLik(fit))), f10(best$value), -2 * as.numeric(logLik(fit)) - best$value))
    cat(sprintf("       var(Int) %s / %s ; var(Days) %s / %s ; cov %s / %s ; sigma^2 %s / %s\n",
                f10(vc$vcov[1]), f10(G[1, 1]), f10(vc$vcov[2]), f10(G[2, 2]), f10(vc$vcov[3]), f10(G[2, 1]),
                f10(sigma(fit)^2), f10(exp(best$par[4]))))
    cat(sprintf("       fixef lmer %s / direct %s ; SE lmer %s / direct %s\n",
                paste(f10(fixef(fit)), collapse = " "), paste(f10(ref$beta), collapse = " "),
                paste(f10(sqrt(diag(vcov(fit)))), collapse = " "), paste(f10(sqrt(diag(ref$vcov))), collapse = " ")))
    nl <- lme(Reaction ~ Days, random = ~ Days | Subject, data = sleepstudy, method = if (REML) "REML" else "ML")
    cat(sprintf("       nlme::lme fixef %s ; SE %s ; sd(Int) %s sd(Days) %s cor %s sigma %s ; logLik %s (lmer %s)\n",
                paste(f10(fixef(nl)), collapse = " "), paste(f10(sqrt(diag(vcov(nl)))), collapse = " "),
                f10(as.numeric(VarCorr(nl)[1, 2])), f10(as.numeric(VarCorr(nl)[2, 2])), f10(as.numeric(VarCorr(nl)[2, 3])),
                f10(nl$sigma), f10(as.numeric(logLik(nl))), f10(as.numeric(logLik(fit)))))
    ## conditional modes and variances at the lmer estimates
    Gfit <- matrix(c(vc$vcov[1], vc$vcov[3], vc$vcov[3], vc$vcov[2]), 2)
    Gbig <- kronecker(diag(ns), Gfit)
    dc <- dense_crit(sleepstudy$Reaction, X, Zs, Gbig, sigma(fit)^2, REML = REML)
    b.ref <- drop(Gbig %*% t(Zs) %*% dc$Vi %*% dc$r)
    rr <- ranef(fit, condVar = TRUE)
    b.lme4 <- as.vector(t(as.matrix(rr$Subject)))
    Z1 <- Zs[sleepstudy$Subject == levels(sleepstudy$Subject)[1], 1:2]
    cv.ref <- solve(t(Z1) %*% Z1 / sigma(fit)^2 + solve(Gfit))
    cat(sprintf("       ranef vs G Z' V^-1 r: max abs diff %.2e ; condVar[,,1] lme4 %s ref %s\n",
                max(abs(b.lme4 - b.ref)), paste(f10(attr(rr$Subject, "postVar")[, , 1]), collapse = " "),
                paste(f10(cv.ref), collapse = " ")))
}

## =====================================================================
## D. prior weights and the REML <-> ML conversions in devCrit()
## =====================================================================
set.seed(303)
d1$w <- rexp(nrow(d1), 1) + 0.2
fw <- lmer(y ~ 1 + (1 | g), d1, weights = w)
fwML <- lmer(y ~ 1 + (1 | g), d1, weights = w, REML = FALSE)
vcw <- as.data.frame(VarCorr(fw)); vcwML <- as.data.frame(VarCorr(fwML))
Z1w <- model.matrix(~ 0 + g, d1)
refw   <- dense_crit(d1$y, matrix(1, nrow(d1)), Z1w, diag(vcw$vcov[1], a), vcw$vcov[2], w = d1$w, REML = TRUE)
refwML <- dense_crit(d1$y, matrix(1, nrow(d1)), Z1w, diag(vcwML$vcov[1], a), vcwML$vcov[2], w = d1$w, REML = FALSE)
cat("\nD. prior weights (REML fit): REMLcrit", f10(REMLcrit(fw)), "dense", f10(refw$crit), "\n")
cat("   ML fit: deviance", f10(deviance(fwML)), "dense", f10(refwML$crit), "\n")
## deviance(REML fit, REML=FALSE): the ML criterion at the REML theta, beta and sigma profiled
th <- getME(fw, "theta"); s2p <- fw@devcomp$cmp[["pwrss"]] / nrow(d1)
refx <- dense_crit(d1$y, matrix(1, nrow(d1)), Z1w, diag(th^2 * s2p, a), s2p, w = d1$w, REML = FALSE)
cat("   deviance(REMLfit, REML=FALSE)", f10(deviance(fw, REML = FALSE)), "| dense ML crit at REML theta, sigma^2 = pwrss/n:", f10(refx$crit), "\n")
th <- getME(fwML, "theta"); s2r <- fwML@devcomp$cmp[["pwrss"]] / (nrow(d1) - 1)
refy <- dense_crit(d1$y, matrix(1, nrow(d1)), Z1w, diag(th^2 * s2r, a), s2r, w = d1$w, REML = TRUE)
cat("   REMLcrit(MLfit)", f10(REMLcrit(fwML)), "| dense REML crit at ML theta, sigma^2 = pwrss/(n-p):", f10(refy$crit), "\n")
nlw <- lme(y ~ 1, random = ~ 1 | g, data = d1, weights = varFixed(~ I(1 / w)))
cat("   nlme::lme(varFixed(~1/w)) logLik", f10(as.numeric(logLik(nlw))), "lmer", f10(as.numeric(logLik(fw))), "\n")

## =====================================================================
## E. profile confidence intervals vs an independent profile of the dense ML likelihood
## =====================================================================
cat("\nE. profile CIs (balanced one-way, ML profile as lme4 documents)\n")
ci <- confint(fit1, method = "profile", quiet = TRUE)
Xa <- matrix(1, a * n); Za <- model.matrix(~ 0 + g)
mlfit <- lmer(y ~ 1 + (1 | g), d1, REML = FALSE)
base <- -2 * as.numeric(logLik(mlfit))
## profile the intercept: minimise the ML -2logL over (log sa2, log se2) at fixed beta0
prof.beta <- function(b0) {
    f <- function(p) { V <- exp(p[1]) * Za %*% t(Za) + exp(p[2]) * diag(a * n); r <- y - b0
        as.numeric(determinant(V, TRUE)$modulus) + drop(t(r) %*% solve(V, r)) + a * n * log(2 * pi) }
    optim(log(c(sa2, se2)), f, control = list(reltol = 1e-14))$value }
zeta.beta <- function(b0) sign(b0 - fixef(mlfit)[[1]]) * sqrt(pmax(0, prof.beta(b0) - base))
## profile sigma_a (sd scale): minimise over (beta, log se2) at fixed sa
prof.sa <- function(sa) {
    f <- function(p) { V <- sa^2 * Za %*% t(Za) + exp(p[1]) * diag(a * n); Vi <- solve(V)
        b <- sum(Vi %*% y) / sum(Vi); r <- y - b
        as.numeric(determinant(V, TRUE)$modulus) + drop(t(r) %*% Vi %*% r) + a * n * log(2 * pi) }
    optim(log(se2), f, method = "BFGS", control = list(reltol = 1e-14))$value }
sa.hat <- as.data.frame(VarCorr(mlfit))$sdcor[1]
zeta.sa <- function(sa) sign(sa - sa.hat) * sqrt(pmax(0, prof.sa(sa) - base))
## profile sigma (residual sd): minimise over (beta, log sa2) at fixed sigma
prof.se <- function(se) {
    f <- function(p) { V <- exp(p[1]) * Za %*% t(Za) + se^2 * diag(a * n); Vi <- solve(V)
        b <- sum(Vi %*% y) / sum(Vi); r <- y - b
        as.numeric(determinant(V, TRUE)$modulus) + drop(t(r) %*% Vi %*% r) + a * n * log(2 * pi) }
    optim(log(sa2), f, method = "BFGS", control = list(reltol = 1e-14))$value }
se.hat <- sigma(mlfit)
zeta.se <- function(se) sign(se - se.hat) * sqrt(pmax(0, prof.se(se) - base))
z <- qnorm(0.975)
ref.ci <- rbind(
    .sig01 = c(uniroot(function(s) zeta.sa(s) + z, c(0.05, sa.hat), tol = 1e-8)$root,
               uniroot(function(s) zeta.sa(s) - z, c(sa.hat, 10 * sa.hat), tol = 1e-8)$root),
    .sigma = c(uniroot(function(s) zeta.se(s) + z, c(0.3 * se.hat, se.hat), tol = 1e-8)$root,
               uniroot(function(s) zeta.se(s) - z, c(se.hat, 3 * se.hat), tol = 1e-8)$root),
    `(Intercept)` = c(uniroot(function(b) zeta.beta(b) + z, c(fixef(mlfit)[[1]] - 10, fixef(mlfit)[[1]]), tol = 1e-8)$root,
                      uniroot(function(b) zeta.beta(b) - z, c(fixef(mlfit)[[1]], fixef(mlfit)[[1]] + 10), tol = 1e-8)$root))
print(cbind(lme4 = ci, independent = ref.ci))
cat(sprintf("  max rel diff %.2e\n", rel(ci, ref.ci)))
wald <- confint(fit1, method = "Wald")
cat("  Wald (fixed effect only):", f10(wald["(Intercept)", ]), "| closed:", f10(fixef(fit1)[[1]] + c(-1, 1) * z * sqrt(vcov(fit1)[1, 1])), "\n")

## =====================================================================
## F. anova(): REML fits are refitted with ML and the LRT uses the ML log-likelihoods
## =====================================================================
set.seed(404)
d1$x <- rnorm(nrow(d1))
m0 <- lmer(y ~ 1 + (1 | g), d1); m1 <- lmer(y ~ x + (1 | g), d1)
m0ML <- refitML(m0); m1ML <- refitML(m1)
an <- suppressMessages(anova(m0, m1))
chi.ref <- 2 * (as.numeric(logLik(m1ML)) - as.numeric(logLik(m0ML)))
cat("\nF. anova(m0, m1): Chisq", f10(an$Chisq[2]), "| 2*diff(ML logLik)", f10(chi.ref),
    "| p", f10(an$`Pr(>Chisq)`[2]), "| pchisq", f10(pchisq(chi.ref, 1, lower.tail = FALSE)), "\n")
cat("   logLik in table:", f10(an$logLik), "| ML refits:", f10(c(logLik(m0ML), logLik(m1ML))),
    "| REML logLik would be:", f10(c(logLik(m0), logLik(m1))), "\n")
an2 <- anova(m0, m1, refit = FALSE)
cat("   refit=FALSE: Chisq", f10(an2$Chisq[2]), "| 2*diff(REML logLik)", f10(2 * (as.numeric(logLik(m1)) - as.numeric(logLik(m0)))), "\n")

## =====================================================================
## G. predict()/simulate() with re.form, and bootMer()
## =====================================================================
fitG <- m1
p0 <- predict(fitG, re.form = NA); p1 <- predict(fitG)
Xg <- model.matrix(~ x, d1); bg <- ranef(fitG)$g[as.character(d1$g), 1]
cat("\nG. predict re.form=NA vs X beta: max abs diff", format(max(abs(p0 - drop(Xg %*% fixef(fitG)))), digits = 3),
    "; predict() vs X beta + Z b: ", format(max(abs(p1 - drop(Xg %*% fixef(fitG)) - bg)), digits = 3), "\n")
nd <- data.frame(x = c(0, 1), g = factor(c("g01", "new")))
pn <- predict(fitG, newdata = nd, allow.new.levels = TRUE)
cat("   newdata (known level g01, new level): ", f10(pn), "| expected:",
    f10(c(fixef(fitG)[[1]] + ranef(fitG)$g["g01", 1], sum(fixef(fitG)))), "\n")
set.seed(505)
S0 <- as.matrix(simulate(fitG, nsim = 4000, re.form = NA))
S1 <- as.matrix(simulate(fitG, nsim = 4000, re.form = NULL))
vcg <- as.data.frame(VarCorr(fitG))
i1 <- which(d1$g == "g01")[1:2]
cat(sprintf("   simulate(re.form=NA): mean-Xb %.3f ; var %.3f (sa2+se2 = %.3f) ; within-group cov %.3f (sa2 = %.3f)\n",
            max(abs(rowMeans(S0) - p0)), mean(apply(S0, 1, var)), sum(vcg$vcov), cov(S0[i1[1], ], S0[i1[2], ]), vcg$vcov[1]))
cat(sprintf("   simulate(re.form=NULL): mean-(Xb+Zb) %.3f ; var %.3f (se2 = %.3f) ; within-group cov %.3f (0 expected)\n",
            max(abs(rowMeans(S1) - p1)), mean(apply(S1, 1, var)), vcg$vcov[2], cov(S1[i1[1], ], S1[i1[2], ])))
bb <- bootMer(fitG, function(x) c(fixef(x), sigma = sigma(x), sd_g = as.data.frame(VarCorr(x))$sdcor[1]), nsim = 400, seed = 606)
cat("   bootMer (parametric, 400 sims): t0 =", f10(bb$t0), "\n")
cat("     boot mean =", f10(colMeans(bb$t)), "\n")
cat("     boot sd of fixef =", f10(apply(bb$t[, 1:2], 2, sd)), "| model SE =", f10(sqrt(diag(vcov(fitG)))), "\n")
cat("     boot 95% percentile CI (confint method='boot' machinery):\n"); print(confint(bb, type = "perc"))
cat("\ndone\n")
