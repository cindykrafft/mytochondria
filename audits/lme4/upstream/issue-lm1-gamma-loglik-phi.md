Title: logLik() of free-dispersion GLMMs (Gamma etc.) is evaluated at phi = deviance/n while the fit uses and reports phi = deviance/(n - q) (master, disp_dof_correction = TRUE)

<!-- lme4 has no issue template; free-form report, master @ 69588fa (2.1-0). Pre-release: not in any CRAN version. -->

**Summary.** On `master` (2.1-0, `glmerControl(disp_dof_correction = TRUE)` default) `glmResp::Laplace()` (`src/respModule.cpp:166-180`) adds the family's `aic()`, which evaluates the Gamma/Gaussian/inverse-Gaussian log-density at the plug-in dispersion `deviance/n` (`src/glmFamily.cpp:239-247, 273-277, 293-297`). The dispersion the fit actually uses is `d_phi`: it is in the PIRLS working weights (`respModule.cpp:163`), profiled by `profilePhi()` as `deviance/(n - qEff)` (`external.cpp:425-426, 471`) and reported by `sigma()`. So `logLik()`, `AIC()`, `BIC()`, `anova()` and `drop1()` report a value that is not the Laplace approximation at the fitted parameters; the offset is about `n/2 * (r - 1 - log r)` with `r = n/(n - qEff)`, which does not cancel between models with different random-effect structures. `disp_dof_correction = FALSE` (where the plug-in and the profiled phi coincide) is consistent. The `nAGQ > 1` path ends in the same call (`external.cpp:619-620`).

**Expected:** `-2*logLik(fit)` equals `ldL2 + sum(u^2) - 2*sum(dgamma(y, shape = 1/phi, scale = mu*phi, log = TRUE))` at `phi = sigma(fit)^2`, the dispersion the object reports.

**Got** (script below, master @ 69588fa): with the default the reported deviance is 1183.2433, the value at `sigma(fit)^2` is 1188.1168 (a 4.87 difference, 2.43 log-likelihood units); with `disp_dof_correction = FALSE` the two agree (1188.4334 vs 1188.4340). Against references that do not use lme4's code (in the audit harness linked below): the exact marginal log-likelihood at the fitted parameters, by adaptive quadrature, is -593.947 and an independent Laplace approximation at the same parameters is -594.040, while `logLik(fit)` is -591.622; with the correction off, `logLik(fit)` is -594.217 against a Laplace value of -594.202. The point estimates are fine (beta within 0.13 SE of the exact ML fit, sd(RE) 0.774 vs 0.772); it is the likelihood value. Shrinking the example showed the effect only depends on `n` and `rank([X, Z])`: any Gamma or log-link Gaussian random-intercept fit reproduces it, and `disp_dof_correction = FALSE` removes it. The package's own consistency test (`tests/testthat/test-gamma_glmm_bias.R:80-110`) recomputes at `phihat <- dev/n`, which is why it passes.

**Minimal reproducible example**

```r
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
```

**Output**

```
disp_dof_correction = TRUE  sigma(fit)^2 = 0.29432  deviance/n = 0.25660
     reported     at_sigma2 at_dev_over_n 
    1183.2433     1188.1168     1183.2433 
disp_dof_correction = FALSE sigma(fit)^2 = 0.25616  deviance/n = 0.25615
     reported     at_sigma2 at_dev_over_n 
    1188.4334     1188.4340     1188.4334 
lme4 2.1.0 | R version 4.3.3 (2024-02-29)
```

**Proposed fix.** Evaluate the density term at `d_phi`: for `Gamma`, hand `aic()` the deviance value whose internal plug-in equals `d_phi` (`d_phi * sum(wt)`); for `gaussian` and `inverse.gaussian`, whose `aic()` methods are written in profiled form `N*(log(dev/N) + 1) + ...`, replace that term by `N*log(phi) + dev/phi`; and make the consistency test recompute at `sigma(fit)^2` for both settings of `disp_dof_correction`. With that change the example prints 1188.1168 for both `reported` and `at_sigma2` and the test file passes for both families. A branch with the fix, the updated test and a NEWS entry is ready; happy to open a PR if you want it (or to adapt it if the intended semantics are that `logLik` should stay at `deviance/n` and `sigma()` should change instead).

**Session info:** R 4.3.3 (Ubuntu), lme4 2.1-0 built from `master` @ 69588fa with Rcpp 1.1.2, RcppEigen 0.3.4.0.0, Matrix 1.6-5, reformulas 0.4.5, minqa 1.2.6, nloptr 2.0.3.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/lme4)

---
_Generated by [Claude Code](https://claude.ai/code)_
