## Held-up checks for the post-fit methods that reach papers: single-model anova() F
## values (vs nlme's sequential F), drop1() LRTs (vs anova()), refit() reproducibility for
## a GLMM (the engine behind bootMer), predict()/simulate() for a binomial GLMM, Wald CIs
## for a GLMM, AIC/BIC bookkeeping, and the singular-fit message.
##
## Run:  Rscript heldup_glmm_methods.R   (library on R_LIBS_USER)
suppressPackageStartupMessages({library(lme4); library(nlme)})
cat("lme4", as.character(packageVersion("lme4")), "from", dirname(system.file(package = "lme4")), "\n\n")
options(digits = 8, width = 130)
f8 <- function(x) format(x, digits = 8)

## ---- single-model anova(): sequential F values against nlme::anova.lme(type = "sequential")
data(sleepstudy, package = "lme4")
set.seed(41)
sleepstudy$z <- rnorm(nrow(sleepstudy))
fm <- lmer(Reaction ~ Days + z + (Days | Subject), sleepstudy)
nl <- lme(Reaction ~ Days + z, random = ~ Days | Subject, data = sleepstudy)
a1 <- anova(fm); a2 <- anova(nl, type = "sequential")
cat("A. anova(lmer) F:", f8(a1$`F value`), "| anova(lme, sequential) F:", f8(a2$`F-value`[-1]), "\n")
cat("   Sum Sq / sigma^2:", f8(a1$`Sum Sq` / sigma(fm)^2), "\n")

## ---- drop1(test = "Chisq") vs anova() likelihood-ratio tests (both ML refits)
d1 <- drop1(fm, test = "Chisq")
fm.ml <- refitML(fm); fm0 <- update(fm.ml, . ~ . - z)
cat("B. drop1 LRT for z:", f8(d1["z", "LRT"]), "p", f8(d1["z", "Pr(Chi)"]), "| anova(ML fits):",
    f8(anova(fm0, fm.ml)$Chisq[2]), "p", f8(anova(fm0, fm.ml)$`Pr(>Chisq)`[2]), "\n")
cat("   AIC(fm) = -2 logLik + 2 npar:", f8(AIC(fm)), f8(-2 * as.numeric(logLik(fm)) + 2 * attr(logLik(fm), "df")),
    "| BIC with log(nobs):", f8(BIC(fm)), f8(-2 * as.numeric(logLik(fm)) + log(nobs(fm)) * attr(logLik(fm), "df")),
    "| df =", attr(logLik(fm), "df"), "(2 fixed + 3 theta + sigma)\n")

## ---- GLMM: refit() on the same response reproduces the fit (bootMer's engine)
data(cbpp, package = "lme4")
gm1 <- glmer(cbind(incidence, size - incidence) ~ period + (1 | herd), cbpp, binomial)
gm1r <- refit(gm1, cbind(cbpp$incidence, cbpp$size - cbpp$incidence))
cat("C. refit(gm1): max |fixef diff|", format(max(abs(fixef(gm1r) - fixef(gm1))), digits = 3),
    "| theta", f8(getME(gm1, "theta")), "->", f8(getME(gm1r, "theta")),
    "| logLik", f8(as.numeric(logLik(gm1))), "->", f8(as.numeric(logLik(gm1r))), "\n")

## ---- predict()/simulate() for the binomial GLMM
p.link <- predict(gm1, re.form = NA); p.resp <- predict(gm1, re.form = NA, type = "response")
Xc <- model.matrix(~ period, cbpp)
cat("D. predict(re.form=NA): link vs X beta max diff", format(max(abs(p.link - drop(Xc %*% fixef(gm1)))), digits = 3),
    "| response vs plogis(X beta)", format(max(abs(p.resp - plogis(drop(Xc %*% fixef(gm1))))), digits = 3), "\n")
p.full <- predict(gm1, type = "response")
cat("   predict(type='response') vs fitted():", format(max(abs(p.full - fitted(gm1))), digits = 3), "\n")
set.seed(42)
ss <- simulate(gm1, nsim = 2000, re.form = NULL)      # condition on the fitted herd effects
prop <- sapply(ss, function(m) m[, 1] / cbpp$size)
cat("   simulate(re.form=NULL) mean proportion vs fitted: max abs diff", format(max(abs(rowMeans(prop) - fitted(gm1))), digits = 3),
    "; mean var vs p(1-p)/n:", format(mean(apply(prop, 1, var)), digits = 4), "vs", format(mean(fitted(gm1) * (1 - fitted(gm1)) / cbpp$size), digits = 4), "\n")
ss0 <- simulate(gm1, nsim = 2000, re.form = NA)       # new herd effects
prop0 <- sapply(ss0, function(m) m[, 1] / cbpp$size)
vc <- as.data.frame(VarCorr(gm1))
h1 <- which(cbpp$herd == cbpp$herd[1])[1:2]
cat("   simulate(re.form=NA): logit-scale within-herd correlation of simulated proportions (herd 1, periods 1,2):",
    format(cor(qlogis(pmin(pmax(prop0[h1[1], ], 0.02), 0.98)), qlogis(pmin(pmax(prop0[h1[2], ], 0.02), 0.98))), digits = 3),
    "(> 0 expected; sd(herd) =", format(vc$sdcor[1], digits = 3), ")\n")

## ---- Wald CIs for the GLMM equal fixef +/- z * SE with the default vcov
ci <- confint(gm1, method = "Wald", parm = "beta_")
se <- sqrt(diag(as.matrix(vcov(gm1))))
cat("E. Wald CI max diff from fixef +/- 1.96 SE:", format(max(abs(ci - (fixef(gm1) + outer(se, qnorm(c(0.025, 0.975)))))), digits = 3), "\n")

## ---- singular-fit message and isSingular()
set.seed(43)
d <- data.frame(g = gl(20, 5)); d$y <- rnorm(100); d$y <- d$y - ave(d$y, d$g)   # group means exactly 0
msgs <- character(0)
fs <- withCallingHandlers(lmer(y ~ 1 + (1 | g), d), message = function(m) { msgs <<- c(msgs, conditionMessage(m)); invokeRestart("muffleMessage") })
cat("F. zero between-group variance: message =", sQuote(trimws(paste(msgs, collapse = " | "))), "; isSingular =", isSingular(fs),
    "; theta =", getME(fs, "theta"), "; derivs kept =", !is.null(fs@optinfo$derivs), "\n")
cat("\ndone\n")
