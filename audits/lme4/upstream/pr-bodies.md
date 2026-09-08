# PR bodies (lme4/lme4 has no pull-request template; README: "pull requests are welcome, but please open a discussion as an issue first", NEWS in `inst/NEWS.Rd`, testthat tests in `tests/testthat`)

Each patch is one commit on top of `master` @ `69588fa` (`git am`-able); each carries a
test that fails on unmodified `master` and a `inst/NEWS.Rd` entry under 2.1-0 BUG FIXES.
`#NNN` is the issue (or, for PR 3, the comment on #867) that precedes the PR.

---

### PR 1 — `fix/checkconv-component` — "Report the gradient component that triggered the max|grad| convergence warning"

Closes #NNN.

`checkConv()` built the "(component %d)" part of the max|grad| warning from
`which.max(maxmingrad)`, where `maxmingrad` is already the scalar `max(mingrad)`, so the
reported component was always 1 (`R/checkConv.R:86`). This uses `which.max(mingrad)`.

Message text only; no fit changes. Adds `tests/testthat/test-checkConv.R` (fails on
`master`: "component 1" where 2 and 3 are expected; passes with the change) and a NEWS
entry. `test-lmer.R` and `test-utils.R` give the same results with and without the
change (the two errors in `test-lmer.R` on R 4.3.3 come from `%||%` being used in the
test file itself and are unrelated).

---

### PR 2 — `fix/gamma-loglik-phi` — "Evaluate the GLMM log-likelihood at the dispersion the fit actually uses"

Closes #NNN.

For families with an estimated dispersion, `glmResp::Laplace()` added the family's
`aic()`, which evaluates the log-density at a plug-in `deviance/n`; the fit itself
(PIRLS working weights, `profilePhi()`) and `sigma()` use the profiled phi, which with
the default `disp_dof_correction = TRUE` is `deviance/(n - rank[X, Z])`. `logLik()`,
`AIC()`, `BIC()` and `anova()` therefore reported a value that is not the Laplace
approximation at the fitted parameters (2.4 log-likelihood units off for n = 320,
rank 42; the offset depends on the random-effect structure, so it does not cancel in
model comparisons).

This evaluates the density term at `d_phi`: `Gamma` gets the deviance value whose
internal plug-in equals `d_phi`; `gaussian` and `inverse.gaussian`, whose `aic()`
methods are in profiled form, get `N*log(phi) + dev/phi` in place of the profiled term.
User-defined families keep their own `aic()`. The consistency test in
`test-gamma_glmm_bias.R` now recomputes at `sigma(fit)^2` and covers both settings of
`disp_dof_correction` for both families (it fails on `master` with the correction on,
passes with the change); `test-sigma-dof.R` and `test-glmer.R` are unchanged with and
without (the two errors in `test-sigma-dof.R` on my machine come from the test calling
the unexported `computeQEff` without `lme4:::`). NEWS entry added.

Behaviour change to flag: `logLik` values of Gamma/inverse-Gaussian/log-link Gaussian
GLMMs fitted with the default control change (they become the Laplace value at the
reported parameters); fits with `disp_dof_correction = FALSE` change by the fixed-point
tolerance only.

---

### PR 3 — `fix/vcov-hessian-fallback` — "vcov(): fall back to RX when the Hessian-based standard errors are implausible"

Follows the comment on #867 (#NNN).

On ordinary Bernoulli random-intercept fits 9 of 150 simulated datasets below 10^4
observations gave default (finite-difference Hessian) standard errors about 100 times
smaller than the RX-based ones, always alongside a max|grad| warning; the RX-based
errors were plausible in every case, and `vcov()` only compared the two when
`use.hessian = FALSE` was given explicitly.

This compares the SEs implied by the two matrices whenever the Hessian is used and
falls back to RX, with a warning naming the factor, when any differ by more than
`getOption("lme4.vcov.hess.se.ratio")` (default 2; `Inf` disables the check). On the
150 fits it triggers on exactly the nine bad ones. Adds
`tests/testthat/test-vcov-fallback.R` (fails on `master`, passes with the change),
documents the check in `?vcov.merMod`, NEWS entry. `test-methods.R` and `test-glmer.R`
are unchanged with and without (the one error in `test-methods.R` on my machine is
`%||%`/`merDeriv` in the test environment).

This is a policy proposal as much as a fix: the threshold, or a fallback keyed on a
negative `checkConv` code instead, is your call.
