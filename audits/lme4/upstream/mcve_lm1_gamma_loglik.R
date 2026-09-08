## LM1: logLik() of a Gamma GLMM is evaluated at phi = deviance/n while the fit uses
## and reports phi = deviance/(n - rank[X, Z])  (lme4 master, disp_dof_correction = TRUE)
library(lme4)
set.seed(14)
J <- 40; nj <- 8
g <- gl(J, nj); x <- rnorm(J * nj); b <- rnorm(J, sd = 0.7)
y <- rgamma(J * nj, shape = 4, scale = exp(1 + 0.5 * x + b[g]) / 4)      # true dispersion 0.25

recompute <- function(fit, phi) {                                        # -2 logLik of the Laplace approximation at phi
    ldL2 <- 2 * as.numeric(Matrix::determinant(getME(fit, "L"), sqrt = TRUE)$modulus)
    -2 * sum(dgamma(y, shape = 1 / phi, scale = fitted(fit) * phi, log = TRUE)) + sum(getME(fit, "u")^2) + ldL2
}
for (dof in c(TRUE, FALSE)) {
    fit <- glmer(y ~ x + (1 | g), family = Gamma(link = "log"), control = glmerControl(disp_dof_correction = dof))
    dev.n <- sum(residuals(fit, "deviance")^2) / length(y)
    cat(sprintf("disp_dof_correction = %-5s sigma(fit)^2 = %.5f  deviance/n = %.5f\n", dof, sigma(fit)^2, dev.n))
    print(c(reported = -2 * as.numeric(logLik(fit)),
            at_sigma2 = recompute(fit, sigma(fit)^2),
            at_dev_over_n = recompute(fit, dev.n)), digits = 8)
}
cat("lme4", as.character(packageVersion("lme4")), "|", R.version.string, "\n")
