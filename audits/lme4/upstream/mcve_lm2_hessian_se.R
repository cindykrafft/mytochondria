## LM2: the default glmer() standard errors (finite-difference Hessian) can be ~100x too
## small; the RX-based ones are fine; the only signal is a max|grad| warning.
library(lme4)
set.seed(6)
J <- 20; nj <- 10
g <- gl(J, nj); x <- rnorm(J * nj); b <- rnorm(J, sd = 1.2)
y <- rbinom(J * nj, 1, plogis(-0.5 + x + b[g]))
fit <- glmer(y ~ x + (1 | g), family = binomial)          # warns: max|grad| = 0.0219 (tol = 0.002)
print(coef(summary(fit)), digits = 4)                       # what a user sees
se <- rbind(default = sqrt(diag(as.matrix(vcov(fit)))),
            RX = sqrt(diag(as.matrix(suppressWarnings(vcov(fit, use.hessian = FALSE))))))
print(se, digits = 4)
cat("lme4", as.character(packageVersion("lme4")), "|", R.version.string, "\n")
