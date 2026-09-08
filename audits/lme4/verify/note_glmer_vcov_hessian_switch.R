## glmer() standard errors come from two different formulas depending on whether the
## finite-difference Hessian was computed at the end of the fit: vcov(use.hessian=NULL)
## uses the Hessian when it is available and getME(., "RX") otherwise. Since 1.1-38 the
## Hessian is skipped for nobs >= check.conv.nobsmax (1e4), for npar >= check.conv.nparmax
## (20 for glmer, counting fixed effects), and for singular fits. This harness measures
## (1) how far the two SEs are apart on ordinary models, (2) that the basis flips at the
## thresholds with no message, and (3) which SE is closer to the sampling SD.
##
## Run:  Rscript note_glmer_vcov_hessian_switch.R   (library on R_LIBS_USER)
suppressPackageStartupMessages(library(lme4))
cat("lme4", as.character(packageVersion("lme4")), "from", dirname(system.file(package = "lme4")), "\n\n")
options(digits = 6, width = 130)
ses <- function(f) {
    h <- sqrt(diag(as.matrix(vcov(f, use.hessian = !is.null(f@optinfo$derivs$Hessian)))))
    r <- sqrt(diag(as.matrix(vcov(f, use.hessian = FALSE))))
    d <- sqrt(diag(as.matrix(vcov(f))))
    hess.avail <- !is.null(f@optinfo$derivs$Hessian)
    basis <- if (!hess.avail) "RX" else if (isTRUE(all.equal(d, h))) "Hessian" else if (isTRUE(all.equal(d, r))) "RX" else "?"
    list(hess = h, rx = r, default = d, basis = basis, hess.avail = hess.avail)
}
show <- function(label, f) {
    s <- ses(f)
    cat(sprintf("%-46s hess.avail=%-5s default basis=%-7s max|SE_hess/SE_RX - 1| = %.4f\n",
                label, s$hess.avail, s$basis, if (s$hess.avail) max(abs(s$hess / s$rx - 1)) else NA))
    invisible(s)
}

## ---- (1) Hessian vs RX standard errors on ordinary models
cat("(1) Hessian-based vs RX-based SEs on the same fit (nobs < 1e4, npar < 20)\n")
data(cbpp, package = "lme4")
gm1 <- glmer(cbind(incidence, size - incidence) ~ period + (1 | herd), cbpp, binomial)
s <- show("cbpp binomial (1|herd), nAGQ=1", gm1)
print(rbind(Hessian = s$hess, RX = s$rx))
set.seed(21)
mk <- function(J, nj, sd.b, beta = c(-1, 1), p.extra = 0) {
    g <- gl(J, nj); x <- rnorm(J * nj); b <- rnorm(J, sd = sd.b)
    d <- data.frame(y = rbinom(J * nj, 1, plogis(beta[1] + beta[2] * x + b[g])), x, g)
    if (p.extra > 0) for (k in seq_len(p.extra)) d[[paste0("z", k)]] <- rnorm(J * nj)
    d
}
for (sd.b in c(0.5, 1.5, 3)) for (nj in c(3, 10)) {
    d <- mk(40, nj, sd.b)
    f <- glmer(y ~ x + (1 | g), d, binomial)
    s <- show(sprintf("Bernoulli J=40 nj=%d sd(RE)=%.1f", nj, sd.b), f)
    cat(sprintf("    SE(Intercept) Hessian %.4f RX %.4f ; SE(x) Hessian %.4f RX %.4f\n", s$hess[1], s$rx[1], s$hess[2], s$rx[2]))
}
data(grouseticks, package = "lme4")
gt <- glmer(TICKS ~ YEAR + cHEIGHT + (1 | BROOD) + (1 | INDEX) + (1 | LOCATION), grouseticks, poisson)
s <- show("grouseticks Poisson, 3 RE terms", gt); print(rbind(Hessian = s$hess, RX = s$rx))

## ---- (2) the basis flips at the thresholds without a message
cat("\n(2) same generating process, default SE basis by parameter count / nobs / singularity\n")
set.seed(22)
for (p.extra in c(16, 17)) {                              # 1 + 1 + p.extra fixed effects + 1 theta = 19 / 20 parameters
    d <- mk(60, 8, 1.2, p.extra = p.extra)
    form <- reformulate(c("x", paste0("z", 1:p.extra), "(1 | g)"), "y")
    f <- glmer(form, d, binomial)
    show(sprintf("npar = %d (1 theta + %d beta)", 2 + p.extra + 1 - 1 + 1, 2 + p.extra), f)
}
set.seed(23)
for (nobs in c(9990, 10010)) {
    d <- mk(nobs / 10, 10, 1.2)
    f <- glmer(y ~ x + (1 | g), d, binomial)
    s <- show(sprintf("nobs = %d", nobs), f)
    cat(sprintf("    SE(Intercept) default %.5f Hessian %s RX %.5f\n", s$default[1], if (s$hess.avail) sprintf("%.5f", s$hess[1]) else "n/a", s$rx[1]))
}
set.seed(24)
d <- mk(40, 8, 0.0)                                       # no cluster variance -> singular fit
f <- suppressMessages(glmer(y ~ x + (1 | g), d, binomial))
show(sprintf("singular fit (sd(RE) = %.2g)", as.data.frame(VarCorr(f))$sdcor[1]), f)
d <- mk(40, 8, 1.2)
f <- glmer(y ~ x + (1 | g), d, binomial, control = glmerControl(calc.derivs = FALSE))
show("calc.derivs = FALSE", f)

## ---- (3) which SE tracks the sampling SD? (small Monte-Carlo, sparse clusters, large RE variance)
cat("\n(3) Monte-Carlo: sampling SD of beta-hat vs mean SE from each basis (Bernoulli, J=30, nj=4, sd(RE)=2)\n")
set.seed(25)
R <- 300; res <- matrix(NA_real_, R, 6)
for (r in seq_len(R)) {
    d <- mk(30, 4, 2, beta = c(-0.5, 1))
    f <- try(suppressMessages(suppressWarnings(glmer(y ~ x + (1 | g), d, binomial))), silent = TRUE)
    if (inherits(f, "try-error") || is.null(f@optinfo$derivs$Hessian)) next
    s <- ses(f)
    res[r, ] <- c(fixef(f), s$hess, s$rx)
}
ok <- complete.cases(res); res <- res[ok, ]
cat(sprintf("  %d of %d replicates used (non-singular fits with a Hessian)\n", nrow(res), R))
tab <- rbind(`sampling SD of beta-hat` = apply(res[, 1:2], 2, sd),
             `mean Hessian SE` = colMeans(res[, 3:4]),
             `mean RX SE` = colMeans(res[, 5:6]),
             `median |SE_hess/SE_RX - 1|` = apply(abs(res[, 3:4] / res[, 5:6] - 1), 2, median))
colnames(tab) <- c("(Intercept)", "x"); print(tab)
cat("\ndone\n")
