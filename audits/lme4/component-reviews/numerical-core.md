# Component: lme4 numerical core (`master` @ `69588fa`, 2026-09-07, version string 2.1-0)

Read in full: `R/lmer.R` (2,672 lines: `lmer`, `glmer`, `mkdevfun`, `anova`, `devCrit`,
`logLik`, `ranef`, `refit`, `refitML`, `vcov`, `summary`, `optwrap`), `R/modular.R`
(1,014: `mkFormula`, `mkLmerDevfun`, `optimizeLmer`, `mkGlmerDevfun`, `optimizeGlmer`,
`check.boundary`, `computeQEff`), `R/checkConv.R` (202), `R/lmerControl.R` (217),
`R/profile.R` (1,303), `R/bootMer.R` (229), `R/predict.R` (1,141), `R/utilities.R`
(`mkRespMod`, `mkMerMod`, `condVar`, `nloptwrap`), `R/VarCorr.R`, `R/GHrule.R`,
`R/deriv.R`, `R/optimizer.R`, and the C++ core `src/external.cpp` (PIRLS, `profilePhi`,
`glmerLaplace`, `glmerAGQ`, `lmer_Deviance`), `src/respModule.cpp` (the ML/REML and
GLMM Laplace criteria), `src/predModule.cpp` (the sparse Cholesky, `solve`, `condVar`,
`unsc`), `src/glmFamily.cpp` (family deviance and `aic` methods). Targeted reads of
`R/covariance.R` (profile-scale conversions) and `R/methods.R` (`sigma`).

Every suspicion was **executed on the shipped code** on three builds: `master` built
from the clone into a private library (`R CMD INSTALL --no-docs`, with Rcpp 1.1.2 and
reformulas 0.4.5 built from their GitHub tags because master needs `Rcpp >= 1.1.1-1.1`),
the current CRAN release **2.0-6** built from the `cran/lme4` mirror tag, and
**1.1-35.1** as installed by Ubuntu's `r-cran-lme4` (the cohort's version family: every
paper that states a version names 1.1-x). R 4.3.3, Matrix 1.6-5, nlme 3.1-164. The
references are closed forms (balanced one-way and nested designs), a dense direct
maximisation of the marginal (RE)ML criterion, `nlme::lme`, and for GLMMs an exact
one-dimensional marginal likelihood (adaptive Gauss–Hermite centred on each cluster's
conditional mode, certified against `integrate()`) maximised directly. Harnesses and
captured outputs are in `../verify/`, one `.out` per build.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### LM1 — CONFIRMED on `master` only (2.1-0 dev; not in 2.0-6 or 1.1-35.1, which carry the older Gamma defects): the log-likelihood of a GLMM with an estimated dispersion is evaluated at a different dispersion than the fit uses and `sigma()` reports

**Code.** `src/respModule.cpp:166-180`:

```cpp
double glmResp::Laplace(double ldL2, double ldRX2, double sqrL) const {
    double ans = ldL2 + sqrL + aic();
    if (hasFreeDispersion()) ans -= 2.;
    return ans;
}
```

`aic()` (`src/respModule.cpp:124-126`) hands `resDev()` to the family's `aic` method,
and `gammaDist::aic` (`src/glmFamily.cpp:239-247`) evaluates the Gamma log-density at
`disp = dev/nn` with `nn = Σ weights` (Gaussian: `dev/n`, `:273-277`; inverse Gaussian:
`dev/Σw`, `:293-297`). The dispersion the fit actually uses is `d_phi`: it enters the
PIRLS working weights (`src/respModule.cpp:163`, `sqrt(w / (d_phi * V(mu)))`), is
profiled by the nested fixed-point loop in `profilePhi` (`src/external.cpp:419-481`),
and is what `mkMerMod` stores as `sigmaML` (`R/utilities.R:536-544`, `resp$phi()`).
With the new default `glmerControl(disp_dof_correction = TRUE)` (`R/lmerControl.R:200`)
that loop uses `phi = deviance/(n − qEff)` with `qEff = rank([X, Z])`
(`src/external.cpp:425-426, 471`; `R/modular.R:840-867`). So `logLik()` (and
`AIC`, `BIC`, `anova`, `drop1`) reports `ldL2 + ‖u‖² − 2 Σ log f(y | μ, φ_dev/n)`
while the fitted parameters are `(β, θ, φ = dev/(n − q))`. The `nAGQ > 1` path ends in
the same call (`src/external.cpp:619-620`). The package's own consistency test
(`tests/testthat/test-gamma_glmm_bias.R:80-110`) recomputes `−2 logLik` at
`phihat <- dev / n`, so it passes while enshrining the mismatch.

**Verified** (`../verify/gamma_glmm_loglik.R`, Gamma(log) random-intercept model, 40
clusters × 8, true φ = 0.25; exact marginal likelihood by adaptive quadrature and an
independent Laplace approximation, both evaluated at glmer's own estimates):

| build | `logLik(fit)` | exact at the fit's parameters | independent Laplace at the fit's parameters | `sigma(fit)²` | `dev/n` | `dev/(n − 42)` |
|---|---|---|---|---|---|---|
| master, defaults | −591.6216 | −593.9473 (**+2.33**) | −594.0402 (**+2.42**) | 0.29432 | 0.25660 | 0.29537 |
| master, `disp_dof_correction = FALSE` | −594.2167 | −594.1187 (−0.10) | −594.2024 (−0.01) | 0.25616 | 0.25615 | — |
| master, `disp_method = "old/buggy"` | −573.3477 | −596.6420 (+23.3) | −596.7508 (+23.4) | 0.31649 | | |
| 2.0-6 (CRAN) | −574.3477 | −596.6420 (+22.3) | −596.7508 (+22.4) | 0.31649 | | |
| 1.1-35.1 | −574.3477 | −600.1015 (+25.8) | −600.1733 (+25.8) | 0.31649 | | |

The −0.01 agreement with the independent Laplace value when the correction is off
isolates the cause: the density term is evaluated at `dev/n` regardless of which φ the
fit used. The offset is `n/2 · (r − 1 − log r)` with `r = φ_dof/φ_n = n/(n − q)`, so it
does not cancel between models with different numbers of random-effect columns (a
model comparison by `anova` or AIC across random-effect structures is shifted). For
the exact maximum-likelihood fit of the same data the reference gives β = (1.0185,
0.4978), sd(RE) = 0.772, φ = 0.2766 (logLik −593.645); master's defaults give (1.0020,
0.4978), 0.774, φ = 0.2943 — the point estimates are within 0.13 SE, it is the reported
likelihood value that is off. On the two released versions the fit itself is biased
(sd(RE) 0.543 on 1.1-35.1; 0.966 on 2.0-6, which reports the same internal estimate on
a different scale) and the log-likelihood is 22–26 units too high; those are the
defects the master NEWS (2.1-0, "fixed a long-standing bug (GH #557, #643, partial
#936)") already describes and fixes, and are recorded under LM6.

**Fix shape.** Evaluate the density term at `d_phi`: for the Gamma family hand
`aic()` the deviance value whose internal plug-in equals `d_phi` (`d_phi · Σw`); for
the Gaussian and inverse-Gaussian families, whose `aic()` methods are written in
profiled form `N(log(dev/N) + 1) + …`, replace that term by `N log φ + dev/φ`; make the
consistency test recompute at `sigma(fit)^2`. Patch 0002 in `../upstream/` does this;
with it `logLik` is −594.0584 against the independent Laplace value −594.0403 at the
same parameters (−0.018, the fixed-point tolerance) for the default setting
(`../verify/gamma_glmm_loglik.patched-0002.out`), and the consistency test passes for
both settings of `disp_dof_correction` and both families. Whether the
dof-corrected moment estimator is the right φ is the maintainers' design choice
(documented in NEWS); the log-likelihood should simply be evaluated at it.

**Tier: held (pre-release report).** It is on the development branch only and the
maintainers are actively working on exactly this code (the `Gamma_GLMM` notes, the
`disp_dof_correction` option, `test-sigma-dof.R`); no released version and no cohort
paper carries it. The issue text is in `../upstream/issue-lm1-gamma-loglik-phi.md`.

### LM2 — CONFIRMED on `master`, 2.0-6 and 1.1-35.1: the default GLMM standard errors come from a finite-difference Hessian that is occasionally two orders of magnitude off, `vcov()` never checks it on the default path, and the only signal is a `max|grad|` warning the documentation calls frequently spurious

**Code.** `vcov.merMod` (`R/lmer.R:2242-2327`) uses the finite-difference Hessian
whenever one is stored and includes the fixed effects (`:2249-2254`: GLMMs with
`nAGQ > 0`). The Hessian is `deriv12(fn, opt$par, delta = 1e-4)` of the PIRLS-evaluated
Laplace deviance (`R/lmer.R:2654`, `R/deriv.R`). The only checks on it are NA and
non-positive-definiteness (`:2273-2281`); the comparison with the RX-based matrix and
its warning (`:2282-2291`) run **only when the user passes `use.hessian = FALSE`**
(issue #994 already notes this asymmetry).

**Verified** (`../verify/glmer_hessian_se_failure.R`; 25 simulated Bernoulli
random-intercept datasets per size, 10 observations per cluster, sd(RE) = 1.2,
β = (−0.5, 1), default `glmer(y ~ x + (1|g), family = binomial)`; identical on the three
builds because the fits are deterministic):

| nobs | fits with a Hessian | median SE_hess/SE_RX | SE_hess/SE_RX < 0.5 | with a convergence warning | bad without a warning |
|---|---|---|---|---|---|
| 200 | 25 | 1.010 | 2 | 2 | 0 |
| 500 | 25 | 1.010 | 4 | 5 | 0 |
| 1,000 | 25 | 1.010 | 2 | 2 | 0 |
| 2,500 | 25 | 1.010 | 0 | 0 | 0 |
| 5,000 | 25 | 1.011 | 1 | 1 | 0 |
| 9,990 | 25 | 1.011 | 0 | 0 | 0 |
| 10,010 | 0 (master, 2.0-6) / 25 (1.1-35.1) | — / 1.011 | 0 | 0 | 0 |

The nine failing fits (6 % of the 150 below 10⁴ observations) print an intercept SE of
0.0005–0.0026 where the RX-based one is 0.07–0.34, i.e. |z| of 198–978 instead of
1.7–7.4; each carries "Model failed to converge with max|grad| = 0.027–0.13 (tol =
0.002, component 1)" and nothing else. `?convergence` tells users that the gradient
check "may be too conservative" and gives a recipe for dismissing it. Section (1) of
`../verify/note_glmer_vcov_hessian_switch.R` shows the same failure on a 40-cluster
fit with sd(RE) = 1.5 (SE 0.0018 vs 0.2484, with a max|grad| = 0.039 warning) and,
where the Hessian is sound, Hessian-based and RX-based SEs differing by 1.5–7 % on
`cbpp` and `grouseticks` and by up to 52 % on sparse clusters with a large
random-effect variance; in a 300-replicate Monte Carlo (30 clusters × 4, sd(RE) = 2)
the sampling SD of β̂ is 0.486/0.368, the mean Hessian SE 0.456/0.337 and the mean RX
SE 0.432/0.302, so the Hessian is the better estimator when it is not broken. The
mechanism section of the failure harness shows the deviance returned by the PIRLS
loop is reproducible but only accurate to ~4e-5 at the 10⁴-observation scale (against
an expected second difference of 5e-6 at `delta = 1e-4`), which is the noise the
divided differences amplify.

**Who is exposed.** Every `glmer` user reading `summary()`, `confint(method =
"Wald")` or anything built on `vcov()` (emmeans, sjPlot, broom.mixed) on a fit that
raised a max|grad| warning; the 47 cohort papers that name `glmer` and the 24 that name
a binomial/logistic family (lower bounds) are the population. On 1.1-38 and later the
Hessian is skipped above 10⁴ observations, 20 parameters, or on singular fits, so those
fits get the RX matrix instead (LM4).

**Fix shape.** Compare the SEs implied by the two matrices on the default path and fall
back to RX, with a warning, when any differ by more than a factor of 2 (patch 0003,
option `lme4.vcov.hess.se.ratio`, `Inf` disables it); alternatively fall back whenever
`checkConv` set a negative code. On the nine failing fits above the RX matrix is what
should have been printed.

**Upstream.** Issue #867 "revisit use.hess default" (open, opened by the maintainer
2025-08-29, no comments) asks exactly "can we do better?" and mentions that the
reproducible example from #720 may be lost; #994 (open) is about the one-sided
mismatch warning. **Tier: comment on #867** (a low-cost category under step 5) with
the failure table and the offered patch; text in
`../upstream/comment-lm2-hessian-se-867.md`.

### LM3 — NOTE (message text), CONFIRMED on all three builds: the max|grad| warning always says "component 1"

`R/checkConv.R:83-89`:

```r
mingrad <- pmin(abs(scgrad),abs(derivs$gradient))
maxmingrad <- max(mingrad)
if (maxmingrad > ccl$tol) {
    w <- which.max(maxmingrad)
```

`which.max` of a scalar is 1, so the "(tol = 0.002, component %d)" part of the
warning never names the offending parameter. `../verify/note_checkconv_component.R`:
with gradient `(1e-6, 0.5, 1e-6)` the warning says component 1 on master, 2.0-6 and
1.1-35.1; on a perturbed `sleepstudy` fit whose gradient is `(−0.9, 53.1, −0.2)` it
also says component 1. No number in a paper changes. One-token fix (patch 0001, with a
test). `checkHess` (`:189`) also tests for a code `5L` that is never assigned. Tier:
held (documentation/message; a PR after a maintainer signal).

### LM4 — NOTE (undocumented behaviour change, 1.1-38 and later): which formula the GLMM standard errors come from depends on the sample size, the parameter count and singularity

Since 1.1-38 (`NEWS`: derivative checks skipped for large data / many parameters /
singular fits) `calc.derivs` defaults to `nobs < check.conv.nobsmax (1e4) && npar <
check.conv.nparmax` (`R/lmer.R:51-53, 182-184`; `R/lmerControl.R:92-93, 189`, 20 for
`glmer`, where `npar` counts the fixed effects too, `R/lmer.R:181` after
`updateGlmerDevfun`), and `optwrap` skips the derivatives on singular fits
(`R/lmer.R:2643-2644`). `vcov` then silently uses RX. Section (2) of
`../verify/note_glmer_vcov_hessian_switch.R`: the same generating process fitted with
19 parameters gives Hessian-based SEs (4.7 % from RX), with 20 parameters RX-based;
9,990 observations Hessian, 10,010 RX; a singular fit RX. On 1.1-35.1 all of these are
Hessian-based. `?vcov.merMod` still says "The default is to use the Hessian whenever
the fixed effect parameters are arguments to the deviance function (i.e. for GLMMs
with `nAGQ>0`)" and `?lmerControl` describes `check.conv.nparmax` as a count of
variance-covariance dimensions. A model with 17 factor levels plus a slope and two
variance parameters crosses the threshold. Tier: held (documentation).

### LM5 — NOTE (known; fixed on `master`, present on 2.0-6 and 1.1-35.1): with `nAGQ > 1` the log-likelihood omits the saturated-model term

`../verify/heldup_glmm_quadrature.R`: binomial (sizes 5–15) and Poisson
random-intercept fits with `nAGQ = 25` report log-likelihoods of −228.104 and −218.748
on 2.0-6 and 1.1-35.1 where the exact values at the same parameters are −538.555 and
−481.318; the differences, 310.451 and 262.570, equal minus the saturated
log-likelihoods `Σ log dbinom(y, size, y/size)` = −310.4511 and `Σ log dpois(y, y)`
= −262.5700 printed by the harness. The estimates are right, likelihood-ratio tests
between two `nAGQ > 1` fits of the same response are unaffected (the constant cancels),
but AIC/anova comparisons with `nAGQ = 1` fits, with `glm`, or across packages are
off, and Bernoulli data (saturated log-likelihood 0) are unaffected. Master's `glmerAGQ`
(`src/external.cpp:619-620`) uses the density-based `Laplace()` term and matches the
exact value to 5e-9; the 2.1-0 NEWS says so ("normalizing constants are now included
in the log-likelihoods and deviances of models fitted with `nAGQ>1`", GH #868). Not
filed: already fixed and announced.

### LM6 — NOTE (known; fixed on `master`, present on 2.0-6 and 1.1-35.1): Gamma GLMM random-effect variances biased and log-likelihood off by a constant

Recorded from the LM1 table: on the releases the PIRLS working weights ignore the
dispersion (`disp_method = "old/buggy"` on master reproduces it), the random-effect SD
comes out at 0.54 (1.1-35.1) instead of 0.77, and `logLik` is 22–26 units above the
exact value at the fit's own parameters. NEWS 2.1-0 lists both (GH #557, #643, #936).
Not filed.

### LM7 — NOTE (documentation): profile intervals of a REML fit are computed on the ML refit, and neither `?profile.merMod` nor `?confint.merMod` says so

`devfun2` (`R/profile.R:506`) starts with `fm <- refitML(fm)`, so for a `REML = TRUE`
fit `confint(method = "profile")` (the default method) profiles the ML likelihood,
while `confint(method = "Wald")` and `method = "boot"` use the REML fit. Neither help
page mentions the refit (grep of `man/profile-methods.Rd` and `man/confint.merMod.Rd`
for "ML"/"REML"/"refit" finds only the `fm01ML` example). The one-way model in section
E gives, for σ, a profile interval of (1.2053, 1.8014) on the ML fit against a Wald
computation that would use the REML σ̂ = 1.454; users who mix the two on a small
sample see a discrepancy that is a documentation gap, not a wrong number. Tier: held
(documentation).

## Withdrawn (own suspicions that verification killed)

- **"`nAGQ = 25` stops 3e-4 short of the exact maximum on Poisson and binomial data."**
  First seen against a plain (non-adaptive) 100-point Gauss–Hermite reference. With the
  reference made adaptive (mode-centred, curvature-scaled, certified by `integrate()`)
  the exact maximum moved and `nAGQ = 25` agrees with it to 1.5e-9 (Poisson) and 4.7e-9
  (binomial) in log-likelihood and to 1e-5 in the parameters. The plain rule, not lme4,
  was 3e-3 off; both values are printed in `heldup_glmm_quadrature.*.out`.
- **"`deriv12` steps below the lower bound when a variance parameter sits at 0."** It
  does (`optwrap` calls it without bounds), but derivatives are skipped on singular fits
  (`R/lmer.R:2643-2644`) and the LMM deviance is even in the sign of a scalar `theta`, so
  no number is affected.
- **"`profile()`/`confint(method = "profile")` on a REML fit returns wrong
  intervals."** It profiles the ML refit (`R/profile.R:506`, `fm <- refitML(fm)`), and
  the independent ML profile in section E of the LMM harness matches lme4's intervals
  to 1.7e-5, so the numbers are what a profile likelihood should be. Withdrawn as a
  numerical finding; what remains is LM7 below.

## What held up (executed, not just read)

All numbers below are identical on `master`, 2.0-6 and 1.1-35.1 unless stated
(`../verify/heldup_lmm_closed_form.*.out`, `heldup_glmm_quadrature.*.out`,
`heldup_glmm_methods.*.out`, `heldup_glmer_nb.*.out`).

- **Balanced one-way random-effects ANOVA** (12 × 5): REML `σ²_a = (MSA − MSE)/n`,
  `σ²_e = MSE` and ML `σ²_a = ((1 − 1/a)·MSA − MSE)/n` reproduced to relative 4.6e-8 and
  6.2e-9; intercept SE `√((nσ²_a + σ²_e)/(an))` to 1e-9; `−2 logLik` equals the dense
  marginal criterion (231.0557714 REML, 230.9003672 ML); `nlme::lme` agrees to 1e-6 in
  the variances and to all printed digits in `logLik`; conditional modes equal the
  shrinkage closed form `nσ²_a/(nσ²_a + σ²_e)·(ȳ_g − μ̂)` to 1.5e-15 and `condVar` equals
  `1/(n/σ²_e + 1/σ²_a)` = 0.3181746969 exactly.
- **Balanced two-level nested design** (6 × 4 × 3, `(1 | A/B)`): REML components equal
  the mean-square closed forms to 1.5e-5 (optimizer tolerance) and `nlme` to 1e-6.
- **`sleepstudy`, correlated random slopes**: `lmer` REML and ML `−2 logLik`
  (1743.628272, 1751.939344) equal a direct L-BFGS-B/Nelder–Mead maximisation of the
  dense criterion over the Cholesky factor of G and log σ² to 1.5e-9 and 2.6e-8;
  variance components agree to 1e-5, fixed effects to 1e-10, SEs to 1e-6; `nlme::lme`
  gives the same `logLik` to all digits; `ranef` equals `G Zᵀ V⁻¹ (y − Xβ̂)` to 6e-13 and
  `condVar` equals `(Zᵢᵀ Zᵢ/σ² + G⁻¹)⁻¹` exactly.
- **Prior weights and the REML ↔ ML conversions** in `devCrit` (`R/lmer.R:773-803`):
  `REMLcrit` and `deviance` equal the dense criteria with `V = ZGZᵀ + σ² W⁻¹`
  (235.1215576, 234.8865631); `deviance(REMLfit, REML = FALSE)` equals the dense ML
  criterion at the REML θ with σ² = pwrss/n (234.9228104), `REMLcrit(MLfit)` the dense
  REML criterion with σ² = pwrss/(n − p) (235.15661); `nlme::lme(weights =
  varFixed(~1/w))` gives the same `logLik`.
- **Profile confidence intervals** (`confint(method = "profile")`, one-way model): the
  three limits pairs equal an independent profile of the dense ML likelihood solved
  with `uniroot` to 1.7e-5 relative; Wald limits equal `β̂ ± 1.96·SE` exactly.
- **`anova()`**: REML fits are refitted with ML (message issued), `Chisq` equals
  `2·Δ logLik` of the ML refits (0.649217045) with the matching `pchisq` p; `refit =
  FALSE` uses the REML values and clamps a negative difference to 0. Single-model
  `anova` F values equal `nlme`'s sequential F to 0.01 % (46.0124 vs 46.0085, the
  estimates differ at 1e-5). `drop1(test = "Chisq")` equals the corresponding `anova`
  LRT to 3e-8. `AIC`/`BIC` are `−2 logLik + k·df` with `df` = fixed + θ + σ.
- **`predict`/`simulate` with `re.form`**: `re.form = NA` is `Xβ̂`, `NULL` is `Xβ̂ + Zb̂`
  (to 1e-15), a new level under `allow.new.levels` gets `Xβ̂`; 4,000 LMM simulations
  have variance 3.427 (σ²_a + σ²_e = 3.442) and within-group covariance 1.301 (σ²_a =
  1.324) under `re.form = NA`, and variance 2.118 (σ²_e = 2.118) with covariance 0.024
  under `re.form = NULL`; binomial GLMM simulations reproduce `fitted()` and
  `p(1 − p)/n`.
- **`bootMer`** (parametric, 400 simulations, one-way model): bootstrap SDs of the fixed
  effects 0.375/0.228 against model SEs 0.382/0.232; percentile intervals via
  `boot.ci`.
- **GLMM estimation** (`heldup_glmm_quadrature`): for Bernoulli, binomial and Poisson
  random-intercept models `nAGQ = 25` reproduces the exact marginal maximum to 7e-10,
  5e-9 and 2e-9 in log-likelihood and 1e-5 in the parameters; the Laplace fit sits
  0.34/0.14/0.10 below the exact maximum with parameters within 0.03 (the documented
  approximation); at `nAGQ = 25` the Hessian-based SEs equal the exact-likelihood
  observed-information SEs to 1e-6 (0.2058920 vs 0.2058910). The Gauss–Hermite nodes
  are the symmetrised `fastGHQuad` rules (`R/GHrule.R`); the AGQ formula
  (`src/external.cpp:595-620`) is the standard mode-centred, curvature-scaled rule.
- **`glmer.nb`**: log-likelihood at its estimates is 0.117 below the exact maximum
  (Laplace-sized), θ 1.917 vs 1.913 exact, `df = 4` counts the NB dispersion.
- **`refit()`** on the same response reproduces a GLMM fit to 6e-4 in the fixed effects
  and 2e-4 in `logLik`; Wald `confint` equals `β̂ ± z·SE`; a zero-between-group-variance
  design gives θ = 4e-17, the singular-fit message and `isSingular() = TRUE`.
- **Convergence machinery** read but not found wanting: `nloptwrap`'s BOBYQA defaults
  (`xtol_abs = ftol_abs = 1e-8`), the two-stage `glmer` optimisation (`bobyqa` at
  `nAGQ = 0`, then Nelder–Mead over (θ, β)), `check.boundary`, `restart_edge`, the
  singular tolerance 1e-4 on the relative-SD scale.

## Not audited

Structured covariances (`cs`, `ar1`, `diag`, new in 2.0), `nlmer`, `allFit`,
`influence`/`hatvalues`, `autoscale`, `lmList`, `mcmcsamp` (disabled), prediction
standard errors (`predict(se.fit = TRUE)`, a documented approximation), the
`optimx`/`nlminb` wrappers, and anything in `lmerTest`, `emmeans` or `pbkrtest` (the
cohort's p-value machinery lives there, not in lme4).
