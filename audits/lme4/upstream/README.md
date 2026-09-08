# lme4 upstream filing kit

_Prepared 2026-09-08 against `lme4/lme4` `master` @ `69588fa` (2026-09-07, version
string 2.1-0). **Default branch: `master`.** Nothing filed, nothing pushed; no fork of
`lme4/lme4` exists under `github.com/cindykrafft` (checked 2026-09-08), so the
`upstream-declines-ai-contributions` topic does not apply._

## What was read before preparing this (step 4 of the method)

- `README.md` of the repository: bugs and wishes go to GitHub issues; usage questions
  to r-sig-mixed-models; "pull requests are welcome, but please open a discussion as an
  issue first"; NEWS lives in `inst/NEWS.Rd` (not `NEWS.md`); documentation is hand-
  written `.Rd`; tests are the classic `tests/*.R` plus `testthat` in `tests/testthat`,
  run together by `R CMD check`; CI is a manually triggered `R-CMD-check-allOS` workflow
  (`.github/workflows/`, `[run ci]` in the commit message). There is **no
  `CONTRIBUTING.md`, no issue template and no PR template** (`.github/` holds only the
  workflows), and no linter configuration.
- `tests/README.md`: `LME4_TEST_LEVEL` gates slow tests; numerical results must not be
  pinned to full precision.
- `inst/NEWS.Rd` for 1.1-35 through 2.1-0 (devel): the 2.1-0 section already announces
  the fixes for the Gamma-GLMM working-weights bias, the "+2" log-likelihood constant,
  and the `nAGQ > 1` normalising constants (LM5/LM6 in the review), which is why those
  are not in this kit; the same section documents `disp_dof_correction` (LM1's context).
- `man/vcov.merMod.Rd`, `man/lmerControl.Rd`, `man/convergence.Rd`,
  `man/profile-methods.Rd`, `man/confint.merMod.Rd` (LM2, LM4, LM7 context).
- Issue tracker (searched 2026-09-08, `mcp__github__search_issues`, one query per
  minute): for LM2 the nearest are **#867 "revisit use.hess default" (open, opened by
  the maintainer 2025-08-29, no comments — the target of the comment text)**, #994
  (open; the mismatch warning only fires with `use.hessian = FALSE`), #720 (closed, the
  motivating example the maintainer says may be lost), #434 (Richardson extrapolation),
  #371 (finite-difference epsilon), #872 (closed; calc.derivs and singularity). For LM1
  the Gamma threads are #557, #643, #936 (from NEWS), #179 and #573 (open, PIRLS
  failures in Gamma GLMMs); none reports the `dev/n` vs `dev/(n − q)` inconsistency,
  which only exists on the development branch. For LM3 (component number) no prior
  report: nearest #425, #489, #783 (convergence warnings in general). For LM5 the
  maintainers' own #868; for LM6 #557/#643/#936.
- Matthew Rocklin's "Craft Minimal Bug Reports": every example below makes its data in
  the script, has no line that is not needed, states expected vs got, records what
  shrinking revealed, and was run on `master` (outputs in `mcve_*.master.out`) and on
  the patched build (`mcve_*.patched-000N.out`).

No results-stability policy of the DESeq2 kind; behaviour-changing fixes are routine
in NEWS. The project asks for an issue before a PR, so each patch has an issue (or, for
PR 3, a comment on the maintainer's open issue) in front of it.

## Contents

| file | what |
|---|---|
| `issue-lm1-gamma-loglik-phi.md` | pre-release report: `logLik` of free-dispersion GLMMs evaluated at `dev/n` while the fit uses `dev/(n − q)`; MCVE + output |
| `comment-lm2-hessian-se-867.md` | comment for #867: failure-rate table, MCVE with output, the offered guard |
| `issue-lm3-checkconv-component.md` | the "component 1" message; MCVE + output |
| `mcve_lm1_gamma_loglik.R` (+ `.master.out`, `.patched-0002.out`) | LM1 reproduction |
| `mcve_lm2_hessian_se.R` (+ `.master.out`, `.patched-0003.out`) | LM2 reproduction (seed 6, 20 clusters × 10) |
| `mcve_lm3_checkconv_component.R` (+ `.master.out`, `.patched-0001.out`) | LM3 reproduction |
| `0001-Report-the-gradient-component-that-triggered-the-max.patch` | LM3 fix + `test-checkConv.R` + NEWS (branch `fix/checkconv-component`) |
| `0002-Evaluate-the-GLMM-log-likelihood-at-the-dispersion-t.patch` | LM1 fix (`src/respModule.cpp`) + updated consistency test + NEWS (branch `fix/gamma-loglik-phi`) |
| `0003-vcov-fall-back-to-RX-when-the-Hessian-based-standard.patch` | LM2 guard (`R/lmer.R`, `man/vcov.merMod.Rd`) + `test-vcov-fallback.R` + NEWS (branch `fix/vcov-hessian-fallback`) |
| `pr-bodies.md` | PR titles and bodies |

## Verification status of the patches

Each branch is one commit on `69588fa`, built with `R CMD INSTALL --no-docs` into its
own library (R 4.3.3, Rcpp 1.1.2, Matrix 1.6-5); tests run with
`testthat::test_file()` against the installed package.

| patch | new/changed test on unmodified `master` | with the patch | other tests of the touched module |
|---|---|---|---|
| 0001 | `test-checkConv.R`: 3 expectations, **2 failed** ("component 1" where 2 and 3 are expected) | 3 expectations, 0 failed | `test-lmer.R` 113 expectations, 0 failed, 2 errors both with and without (the test file uses `%||%`, absent from R 4.3.3's base); `test-utils.R` 13/0 both |
| 0002 | updated `test-gamma_glmm_bias.R`: 9 expectations, **2 failed** (Gamma and log-link Gaussian with `disp_dof_correction = TRUE`) | 9 expectations, 0 failed | `test-sigma-dof.R` 12 expectations, 0 failed, 2 errors both with and without (the test calls the unexported `computeQEff` without `lme4:::`); `test-glmer.R` 9/0 both. The unmodified master version of the test file fails with the patch by construction (it pins `dev/n`) |
| 0003 | `test-vcov-fallback.R`: 7 expectations, **2 failed** (no warning; tiny matrix returned) | 7 expectations, 0 failed | `test-methods.R` 61 expectations, 0 failed, 1 error both with and without (`%||%`; `merDeriv` not installed); `test-glmer.R` 9/0 both |

Harness reruns on the patched builds: `../verify/gamma_glmm_loglik.patched-0002.out`
(reported `logLik` −594.058 vs independent Laplace −594.040 at the same parameters,
from −591.622) and `../verify/glmer_hessian_se_failure.patched-0003.out` (0 of 150 fits
with an implausible default SE; the guard fired on exactly the nine that were bad).
No linter is configured for the project; the R changes follow the surrounding style.

## Tiers and order of operations (step 5; nothing has been filed)

1. **LM2 — comment on #867** (a comment on an issue the maintainers keep open is the
   low-cost category): post `comment-lm2-hessian-se-867.md`; if the maintainer wants the
   guard, push `fix/vcov-hessian-fallback` to a fork and open PR 3 against it.
2. **LM1 — held (pre-release report).** Development-branch only, on code the
   maintainers are actively changing. File `issue-lm1-gamma-loglik-phi.md` as a
   pre-release report if the lead judges it useful before 2.1-0 goes to CRAN, or after
   a maintainer signal on #867; PR 2 follows the issue.
3. **LM3 — held** (message text). Issue + PR 1 after a positive signal.
4. LM4, LM5, LM6, LM7 are notes: no filing (LM5/LM6 are fixed and announced upstream;
   LM4/LM7 are documentation).

Record issue and PR numbers, and every maintainer response, in `../README.md` and the
top-level status table.
