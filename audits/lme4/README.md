# lme4 audit against 312 published papers (2021–2026)

_Generated 2026-09-08 against `lme4/lme4` `master` @ `69588fa` (2026-09-07, version
string 2.1-0), the CRAN release 2.0-6 (built from the `cran/lme4` mirror tag) and
1.1-35.1 (Ubuntu's `r-cran-lme4`, the cohort's version family). Focus: correctness of
the numbers that reach papers, verified by executing the shipped code._

## What this is

The six-journal survey found **312 papers** in PNAS (239), *Nature* (64), *Science* (5),
*The Lancet* (2) and *Cell* (2), 2021–2026, that used lme4, the standard R package for
linear and generalized linear mixed models; 302 name it in their methods, 55 also use
emmeans and 70 name lmerTest or Satterthwaite degrees of freedom. Its numerical core —
the profiled ML/REML deviance and its optimisation, the convergence and singularity
checks, `glmer`'s PIRLS with Laplace and adaptive Gauss–Hermite quadrature, the
variance components, fixed-effect standard errors, profile/Wald/bootstrap intervals,
conditional modes and variances, `anova`/likelihood-ratio tests, `predict`/`simulate`
and `bootMer` — was read in full on `master` and every suspicion was run on the three
builds against closed forms (balanced one-way and nested designs), a dense direct
maximisation of the marginal likelihood, `nlme::lme`, and for GLMMs an exact
one-dimensional marginal likelihood (adaptive Gauss–Hermite certified with
`integrate()`) maximised directly.

## Findings (details and line citations in [`component-reviews/numerical-core.md`](component-reviews/numerical-core.md); harnesses with captured output per build in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **LM1** | **CONFIRMED on `master` (2.1-0 dev) only**; 2.0-6 and 1.1-35.1 not applicable (they carry the older Gamma defects, LM6) | held (pre-release report) | The log-likelihood of a GLMM with an estimated dispersion (Gamma, inverse Gaussian, log-link Gaussian) is evaluated at φ = deviance/n while the fit uses, and `sigma()` reports, φ = deviance/(n − rank[X, Z]) under the new default `disp_dof_correction = TRUE`. On a Gamma(log) random-intercept model (n = 320, rank 42) `logLik` is −591.62 where the exact value at the fit's own parameters is −593.95 and an independent Laplace approximation −594.04; with the correction off the reported and independent values agree to 0.01. The offset depends on the random-effect structure, so AIC/`anova` comparisons across structures shift; point estimates are fine. Patch with test ready. |
| **LM2** | **CONFIRMED on `master`, 2.0-6 and 1.1-35.1** | comment on the maintainers' open #867 (+ offered patch) | The default `glmer` standard errors (finite-difference Hessian of the Laplace deviance) are about 100× too small in 9 of 150 ordinary Bernoulli random-intercept fits below 10⁴ observations (|z| 198–978 instead of 1.7–7.4); every such fit carries only a `max|grad|` warning that the documentation calls often spurious, and `vcov()`'s Hessian-vs-RX check runs only when the user opts *out* of the Hessian. Where the Hessian is sound it beats RX (Monte Carlo: sampling SD 0.486 vs mean SEs 0.456 Hessian / 0.432 RX). A guard that falls back to RX when the two SEs differ by more than 2× fires on exactly the nine bad fits. |
| LM3 | NOTE (message text), confirmed on all three | held | The `max|grad|` warning always says "component 1" (`which.max` of a scalar). One-token fix with test. |
| LM4 | NOTE (undocumented behaviour change, 1.1-38 and later) | held (documentation) | Which formula the GLMM standard errors come from switches silently to RX at ≥ 10⁴ observations, ≥ 20 parameters (fixed effects counted), on singular fits or with `calc.derivs = FALSE`; `?vcov.merMod` still says the Hessian is used for every GLMM with `nAGQ > 0`, and the two differ by 1.5–52 % on ordinary fits. |
| LM5 | NOTE (known; fixed on `master`, present on 2.0-6 and 1.1-35.1) | none (NEWS 2.1-0, #868) | `nAGQ > 1` log-likelihoods omit the saturated-model term: +310.45 (binomial, sizes 5–15) and +262.57 (Poisson), exactly minus the saturated log-likelihood. Estimates and LRTs between `nAGQ > 1` fits are unaffected; AIC comparisons with `nAGQ = 1`/`glm` are off; Bernoulli data unaffected. |
| LM6 | NOTE (known; fixed on `master`, present on 2.0-6 and 1.1-35.1) | none (NEWS 2.1-0, #557/#643/#936) | Gamma GLMM random-effect SD 0.54 (1.1-35.1) instead of 0.77; log-likelihood 22–26 units too high. |
| LM7 | NOTE (documentation) | held | `confint(method = "profile")` on a REML fit profiles the ML refit (`R/profile.R:506`); neither `?profile.merMod` nor `?confint.merMod` says so. The intervals equal an independent ML profile to 2e-5. |

Three own suspicions were withdrawn after execution (a 3e-3 discrepancy that belonged to
my own non-adaptive quadrature rule, not to `nAGQ = 25`; `deriv12` stepping below a bound
on singular fits, which never reaches a number; the REML→ML profile, which is right and
became LM7).

**Held up under execution** (all three builds): balanced one-way REML/ML variance
components to 5e-8 against the mean-square closed forms, the intercept SE, `−2 logLik`
against the dense marginal criterion, conditional modes and variances against the
shrinkage closed form, `nlme::lme` to 1e-6; the balanced nested design to 2e-5;
`sleepstudy` with correlated random slopes against a direct dense maximisation (REML and
ML `−2 logLik` to 3e-8, variances to 1e-5, `ranef` to 6e-13, `condVar` exactly) and
`nlme`; prior weights and the `devCrit` REML↔ML conversions; profile intervals against an
independent profile of the dense likelihood (2e-5) and Wald intervals exactly; `anova`
LRTs on ML refits, single-model F against `nlme`'s sequential F, `drop1`, AIC/BIC
bookkeeping; `predict`/`simulate` with `re.form` (means, variances and within-group
covariances); `bootMer`; `nAGQ = 25` equal to the exact marginal maximum to 5e-9 for
Bernoulli, binomial and Poisson models with Hessian SEs equal to the exact
observed-information SEs to 1e-6; the Laplace fits within their documented
approximation; `glmer.nb`; `refit`; the singular-fit message. Not checked: structured
covariances (`cs`/`ar1`/`diag`, new in 2.0), `nlmer`, `allFit`, `influence`,
prediction SEs, and the p-value machinery in lmerTest/emmeans/pbkrtest.

## How the papers use lme4 (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| `lmer` / linear mixed model named | 142 |
| lmerTest / Satterthwaite | 70 |
| emmeans / post hoc | 59 |
| `glmer` / GLMM named | 47 |
| binomial / logistic family | 24 |
| random intercept only stated | 23 |
| ML stated / REML stated | 14 / 7 |
| nested design | 13 |
| repeated measures / longitudinal | 10 |
| nlme also used / glmmTMB also used / brms | 9 / 5 / 5 |
| bootstrap / bootMer | 8 |
| R² (MuMIn, performance) | 7 |
| negative binomial (`glmer.nb`) / Poisson / Gamma | 6 / 5 / 2 |
| likelihood-ratio test / anova | 5 |
| convergence / singular fit handling | 4 |
| Kenward–Roger / optimizer stated / nAGQ stated | 2 / 2 / 1 |
| version stated | 26 (all in the 1.1 family: 1.1-17 … 1.1-35.5; the "1.2" and "3.1"/"4.x" strings are nlme/R version bleed-through) |

Every stated version is 1.1-x, so LM2 (present since at least 1.1-35) and the two
already-fixed defects LM5/LM6 are the ones with published exposure; LM1 has none (no
release carries it); LM4 starts at 1.1-38 (2025-12).

**Profiling caveat.** As for the Seurat and Scanpy audits, this session had no route to
Europe PMC, so `lme4_profile.py` ran in `--offline` mode over the survey's stored
evidence snippets; every record in `lme4_profiles.jsonl` is `source: survey_cache` and
every count above is a lower bound. Rerun without `--offline` from a host with Europe
PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- No `CONTRIBUTING.md`, no issue or PR templates, no linter; the repository README says
  bugs go to GitHub issues, usage questions to r-sig-mixed-models, and "pull requests are
  welcome, but please open a discussion as an issue first". NEWS is `inst/NEWS.Rd`;
  tests are classic `tests/*.R` plus `testthat`; CI is a manually triggered workflow.
- The maintainer's own open issue **#867 "revisit use.hess default"** (2025-08-29, no
  comments) is the place for LM2; #994 already notes that the mismatch warning is
  one-sided. LM1 is on the development branch only, in code under active work
  (`disp_dof_correction`, `test-sigma-dof.R`), so it is held as a pre-release report.
  LM5/LM6 are fixed and announced in the 2.1-0 NEWS and are not filed.
- **The kit is in [`upstream/`](upstream/)**: three texts (issue for LM1, comment on
  #867 for LM2, issue for LM3) with reproductions run on `master`, three `git am`-able
  patches with tests that fail on unmodified `master` and NEWS entries, PR bodies, and
  the test counts with and without each patch. Nothing has been filed.

## Files

| file | what |
|---|---|
| `lme4_profile.py`, `lme4_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/numerical-core.md` | the review: LM1–LM7, withdrawn suspicions, held-up list, not-checked list |
| `verify/heldup_lmm_closed_form.R` (+ `.master.out`, `.v2.0-6.out`, `.v1.1-35.1.out`) | LMM core: closed forms, dense direct maximisation, `nlme`, weights, profile/Wald CIs, `anova`, `predict`/`simulate`, `bootMer` |
| `verify/heldup_glmm_quadrature.R` (+ 3 `.out`) | `glmer` Laplace and `nAGQ = 25` vs the exact marginal likelihood (Bernoulli, binomial, Poisson); LM5 |
| `verify/gamma_glmm_loglik.R` (+ 3 `.out`, `.patched-0002.out`) | LM1/LM6: Gamma GLMM vs exact likelihood and an independent Laplace approximation |
| `verify/glmer_hessian_se_failure.R` (+ 3 `.out`, `.patched-0003.out`) | LM2: failure rate of the default SEs by sample size; mechanism |
| `verify/note_glmer_vcov_hessian_switch.R` (+ 3 `.out`) | LM2/LM4: Hessian vs RX SEs, the silent basis switch, Monte Carlo |
| `verify/note_checkconv_component.R` (+ 3 `.out`) | LM3 |
| `verify/heldup_glmm_methods.R` (+ 3 `.out`) | held-up: single-model `anova` vs `nlme`, `drop1`, AIC/BIC, `refit`, binomial `predict`/`simulate`, Wald CIs, singular message |
| `verify/heldup_glmer_nb.R` (+ 3 `.out`) | held-up: `glmer.nb` vs the exact likelihood |
| `upstream/` | filing kit (see its README) |

Harnesses need R with lme4 on `R_LIBS_USER` (master: `R CMD INSTALL --no-docs <clone>`
after building Rcpp ≥ 1.1.1-1.1 and reformulas from their GitHub tags; 2.0-6 from the
`cran/lme4` mirror tag), plus nlme and statmod; each `.out` names the library it ran
from. This environment had no CRAN or Bioconductor access; every extra package came
from Ubuntu's apt or a GitHub tag.

## Next steps

1. Post the LM2 comment on #867 from the kit; if the maintainer engages, offer PR 3 and
   then the LM1 report and PR 2 (before 2.1-0 reaches CRAN if possible).
2. Extend the review to the structured covariance code (`cs`, `ar1`, `diag`) and to
   lmerTest's Satterthwaite path, which 70 cohort papers name.
3. Full-text profiling rerun when Europe PMC is reachable.
