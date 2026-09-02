# Upstream filing kit

Ready-to-file GitHub issues and pull requests for the Tier-1 defects from the
SPM audit (`../README.md`, reproductions in `../reproductions/`).

Five fixes plus one new test file are implemented and pushed to the
`cindykrafft/spm` fork as single-fix branches (all based on
`spm/spm@530ec52`). SPM's CONTRIBUTING.md takes bugs as GitHub issues
(expected vs. actual behaviour + reproduction code — every issue body in
`submission-kit.md` includes a runnable MATLAB snippet) and welcomes external
PRs; there is no template and no CLA. Suggested flow per fix: search existing
issues, file the issue, open the PR from the compare link, set `Fixes #NNN`.

| Branch | Finding | Fix | Compare URL |
|---|---|---|---|
| `fix/ecdensity-chi2` | SP1 | χ² EC density t-powers **+ `tests/test_spm_ECdensity.m`** | https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/ecdensity-chi2 |
| `fix/nlsi-gn-logdet` | SP2 | free-energy log-det ÷ nq | https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/nlsi-gn-logdet |
| `fix/meeg-badsamples-baseline` | SP3 | remove baseline double-count | https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/meeg-badsamples-baseline |
| `fix/meeg-downsample-fsample` | SP4 | stamp achieved sampling rate | https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/meeg-downsample-fsample |
| `fix/design-contrasts-nbases` | SP5 | modulator padding × nbases | https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/design-contrasts-nbases |

(The fork also carries `fix/high-priority-correctness`, all six commits on
one branch, if a combined submission is ever preferred.)

## Files

- **`submission-kit.md`** — per-fix issue title/body and PR title/body, the
  compare URLs above, and a pre-flight checklist (search issues first; run
  SP2-SP5 in real MATLAB; submission order; rebase note).
- **`bug-and-pr-descriptions.md`** — the longer-form originals the kit was
  distilled from, including the apply-from-patch recipe used to populate the
  fork.

## Status

| Finding | Issue / PR | State |
|---|---|---|
| SP1 — `spm_ECdensity` χ² EC densities | [#158](https://github.com/spm/spm/issues/158) / [PR #159](https://github.com/spm/spm/pull/159) | open (filed 2026-08-31) |
| SP2 — `spm_nlsi_GN` log-det × n_q | [#160](https://github.com/spm/spm/issues/160) / [PR #161](https://github.com/spm/spm/pull/161) | open (filed 2026-08-31) |
| SP3 — `@meeg/badsamples` baseline double-count | [PR #163](https://github.com/spm/spm/pull/163) | **merged 2026-09-02** (vlitvak) |
| SP4 — `spm_eeg_downsample` achieved fsample | [PR #165](https://github.com/spm/spm/pull/165) | **merged 2026-09-02** (vlitvak) |
| SP5 — `spm_design_contrasts` modulator padding | — | to file |

SP1's branch ships with the unit test that would have caught the bug (pre-fix
12/23 assertions fail, fixed 0/23 — `../reproductions/driver.m`); the
`matlab.unittest` wrapper follows the repo's own `test_spm_Ncdf.m` pattern but
has been executed only via the Octave driver. Each PR states what testing was
done.
