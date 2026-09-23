# Upstream filing kit

AFNI takes bug reports on the [AFNI Message Board](https://discuss.afni.nimh.nih.gov)
and pull requests on [github.com/afni/afni](https://github.com/afni/afni). Unlike
FSL, both channels are open, so findings go straight to GitHub.

## Filed (as of 2026-09-18)

Every correctness PR is paired with an issue carrying a runnable reproduction.

| PR | Issue | Finding | State |
|---|---|---|---|
| [#944](https://github.com/afni/afni/pull/944) | #945 | AF1 — `3dReHo` tie detection truncates floats to int | **merged 2026-08-28** |
| [#947](https://github.com/afni/afni/pull/947) | #946 | AF6 — NIfTI `SEQ_DEC` slice timing discarded | **merged 2026-08-28** |
| [#926](https://github.com/afni/afni/pull/926) | — | test suite: `test_3dttest++` never executed `3dttest++` | **merged 2026-08-28** |
| [#928](https://github.com/afni/afni/pull/928) | — | test suite: return the exit code from asynchronous command execution | **merged 2026-08-28** |
| [#951](https://github.com/afni/afni/pull/951) | #952 | AF2 — `3dttest++ -paired -zskip`; `3dGroupInCorr` BminusA slots; t-to-z saturation | open |
| [#953](https://github.com/afni/afni/pull/953) | #954 | AF12 — `3dTstat -DW`/`-tdiff`/`-nzmean` | open |
| [#956](https://github.com/afni/afni/pull/956) | #955 | AF13 — `3dBrickStat -automask` scan truncation, `-absolute` integer `abs()` | open |
| [#958](https://github.com/afni/afni/pull/958) | #957 | `3dTshift -no_detrend` demeans the wrong array for the second voxel of each pair | **merged 2026-09-18** (`322124671`, one comment on the PR, not yet read from the session) |
| [#960](https://github.com/afni/afni/pull/960) | #959 | AF3/AF4/AF5 — `3dMEMA` missing-data DF, `3dLMEr` GLT stamping, `3dMVM -robust` z conversion | **fix applied on master by Gang Chen 2026-09-22** (`94211003e` 3dLMEr 1.2.3, `cb91276aa` 3dMVM 4.2.4, `d4e4951bc` 3dMEMA 1.2.1, each "a fix per cindykrafft's suggestion"; the code lines are identical to the PR's, only his comments and version strings differ); he then merged master into the PR branch (`db5642514`), so the PR is open with an empty diff; his review says "Thanks for the suggestions! Fixes are in and pushed to master."; closing note drafted in `reply-960-close.md`; R parse check done 2026-09-02 (see below) |
| [#962](https://github.com/afni/afni/pull/962) | #961 | AF7 — `3dROIstats -sigma` Bessel factor in integer arithmetic | **merged 2026-09-18** (`6a889c57d`, one comment on the PR, not yet read from the session) |
| [#964](https://github.com/afni/afni/pull/964) | #963 | `3dmaskave`/`mri_percents` one-past-end reads at extreme percentiles | open |
| [#966](https://github.com/afni/afni/pull/966) | #965 | AF15/AF14 and three more one-liners — `armacor` `abs()`, `3dXClustSim`, `edt_coerce`, `3dpc`, `3dDWItoDT` | open |
| — | [#967](https://github.com/afni/afni/issues/967) | `3dcalc atanh(±1)` returns ±1: Fisher-z pipelines silently saturate | open (issue only); afni-dglen replied 2026-09-18 with four candidate values (0, ±13, ±4, ±1) and no decision; reply drafted in `reply-967-atanh.md` (argues ±13, the value `3dcalc`'s own `cdf` function returns; asks for |x| > 1 and acosh/asin/acos to saturate the same way; offers the PR) |
| — | [#968](https://github.com/afni/afni/issues/968) | AF9 — ACF "effective FWHM" is √2 larger than kernel FWHM by definition; help text says "long tails" | open (issue only) |

**PR #944** stores the sorted time series as `float` instead of `int` so the comparison
is lossless; the harness in `../reproductions/` is the evidence. The trailing-tie
closure that the first review called AF1b was merged separately the day before
(`29384a2`, authored 2023) and a divide-by-zero guard the day after (`74a90ac`); see
`../reanalysis/README.md` for what each build does.

## R scripts: parse-check before filing

PR #960 went out with a note that no R interpreter was available and asked the
maintainer to run a parse check. That shifts verification onto the maintainer and
must not happen again: `apt-get install r-base-core` works in the project container,
so any change touching `src/R_scripts/` is parse-checked here first
(`Rscript -e "invisible(parse('file.R'))"` on both the PR head and the base), and
the PR body says what was and was not run.

Done retroactively for #960 on 2026-09-02 under R 4.3.3: `3dLMEr.R`, `3dMEMA.R`
and `3dMVM.R` all parse at the PR head (and at the base). The `3dMVM` Z
conversion was also checked numerically: `qnorm(p/2, lower.tail=FALSE)` gives
1.960 at p = 0.05 where the old `qnorm(p)` form gave 1.645, and a chi-square of
1.96² round-trips to Z = 1.96. None of the three programs was run end to end on
data. A comment on the PR thread (2026-09-02) records the parse check, the Z check, and
that limit.

## Verification honesty

"CONFIRMED" in this project means the defect was derived independently and, in most
cases, reproduced numerically in isolation — compiled C harnesses built from the
actual translation units, comparisons against SciPy, fuzz tests against sorted
references, and Monte-Carlo simulation. It does **not** mean anyone ran the shipped
AFNI binaries on imaging data and watched the wrong number appear. Please reproduce
before merging.

- 2026-09-22 evening (watcher): #967 has a second comment (21:20 UTC), PR #960 was closed with a second comment (21:32) and #959 closed (21:33): the owner posted the drafted #967 reply and the #960 closing note and closed both; to be confirmed by the owner.
