# Upstream filing kit

AFNI takes bug reports on the [AFNI Message Board](https://discuss.afni.nimh.nih.gov)
and pull requests on [github.com/afni/afni](https://github.com/afni/afni). Unlike
FSL, both channels are open, so findings go straight to GitHub.

## Filed

| Finding | Route | State |
|---|---|---|
| AF1 — `3dReHo` tie detection truncates floats to int | [afni/afni PR #944](https://github.com/afni/afni/pull/944) | **merged 2026-08-28** (`a0a9530`) |

**PR #944**, *"3dReHo: fix tie handling in CalcRanksForReHo"* — stores the sorted time
series as `float` instead of `int` so the comparison is lossless (`THD_get_voxel()`
already returns `float`). One-line change; the harness in `../reproductions/` is the
evidence. The PR description reports the two regimes the fix moves: values in [0,1)
gave 100% incorrect ranks with a maximum rank error of 22.5, and values in [0,1000)
gave 64% incorrect ranks with a maximum error of 1.5.

Not included in that PR, and worth a follow-up: **AF1b**, the trailing tie run that
`rsfc.c:99-118` never closes. It is a real defect in both the buggy and the fixed
code — genuinely tied values at the top of the sorted array get no correction — but
it is independent of the truncation fix, and it is currently the only thing making
sub-integer-scale input come out right.

## Ready to file, not yet filed

Ordered by (severity × exposure). Each is written up with file:line evidence in
`../component-reviews/`; the fixes are small enough to send as PRs.

| Finding | Component | Fix shape |
|---|---|---|
| AF3 | `3dMEMA -missing_data` DF (two bugs) | sign fix + per-group DF index |
| AF6 | NIfTI `SEQ_DEC` slice timing no-op | loop bound `slice_end` → `slice_start` |
| AF4 | `3dLMEr` GLT/GLF sub-brick stamping | missing factor of 2 on `num_glt` |
| AF7 | `3dROIstats -sigma` Bessel no-op | integer division → double |
| AF5 | `3dMVM -robust` z conversion | `qnorm(p)` → `qnorm(p/2)` |
| AF2 | `3dttest++ -paired -zskip` | add `!IS_PAIRED` guard |
| AF13 | `3dBrickStat -automask` truncated scan, `-absolute` integer `abs()` | loop bound + `fabs` |
| AF12 | `3dTstat -DW`/`-tdiff`/`-nzmean` | three independent small fixes |
| AF15 | `1dgenARMA11 -arma31/-arma51` integer `abs()` | `fabs` |
| AF14 | `3dDWItoDT` nonlinear NaN on zero-gradient rows | copy the linear path's b=0 guard |
| AF9 | ACF "effective FWHM" vs kernel FWHM | documentation, not code — the behaviour is by construction |

AF9 is deliberately last: nothing there is a coding error. What is wrong is the help
text's explanation ("long tails") for what is actually a hard-wired change of
definition, and that is what a report should say.

## Verification honesty

"CONFIRMED" in this audit means the defect was derived independently and, in most
cases, reproduced numerically in isolation — compiled C harnesses built from the
actual translation units, comparisons against SciPy, fuzz tests against sorted
references, and Monte-Carlo simulation. It does **not** mean anyone ran the shipped
AFNI binaries on imaging data and watched the wrong number appear. Please reproduce
before merging.
