# PLINK upstream filing kit

Default branch: **`master`**.

_Prepared 2026-09-03 against `chrchang/plink-ng` `master` @ `8bfebe8` (2026-09-02).
**Nothing has been filed or pushed.** The fix branch `fix/hwe-threshold-tail-sum`
(one commit, `08256aa`, on top of `8bfebe8`) exists only in the local scratch clone;
its `git format-patch` output is `0001-PLINK-1.9-hwe-keeps-variants-whose-exact-p-is-at-or-.patch`._


## Fork branches (pushed 2026-09-03)

Each branch is one commit on top of `8bfebe8` (`master`) in the fork
[cindykrafft/plink-ng](https://github.com/cindykrafft/plink-ng); PR compare URLs use
`https://github.com/<upstream>/compare/master...cindykrafft:plink-ng:<branch>`.

| branch | commit | patch |
|---|---|---|
| [`fix/hwe-threshold-tail-sum`](https://github.com/cindykrafft/plink-ng/tree/fix/hwe-threshold-tail-sum) | `6a7a10a` | 0001 (PL1) |

## What was read before preparing this (step 4 of the method)

- Top-level `README.md`: points to the PLINK 1.9 / 2.0 documentation at
  cog-genomics.org, names the plink2-users Google group as the technical-support
  forum, and says 1.9's feature development ended in 2016 while it remains the
  drop-in PLINK 1.07 replacement. Shaped the kit: the finding is a plain bug in
  1.9 with a reproduction, so it goes to GitHub issues (where 1.9 bug reports
  live, e.g. #128, #353) rather than the forum; the report says which 1.9 tags
  carry it.
- No `CONTRIBUTING*`, no `.github/ISSUE_TEMPLATE`, no PR template, no `config.yml`,
  no pinned policy issue, no changelog file: the issue text below is free-form in
  the order version / command / data / got / expected / cause / fix.
- `.github/workflows/`: `plink2_functional_tests.yml` runs `2.0/Tests/run_tests.sh`
  (plink2 CLI regression tests against stored outputs), `ci.yaml` builds the pgenlib
  wheel, `auto_checkcommits_tests_linuxmac.yml` and `release.yaml` build binaries.
  None exercises 1.9.
- `1.9/README.md` and `1.9/tests/`: a description of the source layout with a
  pointer to the (unreachable here) dev page; `test_setup.sh` generates dummy
  datasets with `--dummy`, `tests.py` compares a `plink19` build against a
  `plink107` build on them. There is no unit-test target and no test that reaches
  `SNPHWE_t`, so the patch carries no test file; the MCVE and the exhaustive
  driver harness are the before/after evidence (numbers below).
- `1.9/plink_help.c:1647-1651`: "`--hwe <p> ['midp'] ['include-nonctrl']` : Exclude
  variants with Hardy-Weinberg equilibrium exact test p-values below a threshold" —
  the statement of intended behaviour the finding is measured against.
- `1.9/Makefile`: `NO_LAPACK`, `ZLIB`, `BLASFLAGS` overrides (used for the builds);
  no formatter or linter configuration in the repository (`clang-format` absent), so
  the patch follows the surrounding style (2-space indent, braces on every `if`).
- Issue tracker searched 2026-09-03 (`mcp__github__search_issues`, four phrasings:
  "--hwe filter removes variant with p-value above threshold", "Hardy-Weinberg exact
  test SNPHWE_t threshold wrong result inconsistent with --hardy output", "hwe midp
  heterozygote count small p-value discrepancy plink 1.9", "variant excluded by --hwe
  but --hardy p-value larger than threshold two heterozygotes"): no prior report.
  Nearest: #128 "`--hwe 0` still filters out variants based on hwe" (2019, closed),
  #341 "`--freq counts` … disagrees with `--geno-counts`/`--hardy`" (2026, open,
  plink2), #353 "PLINK 1.9: `--homozyg` … wrong subset_size" (2026, open). Several
  2026-08-31 … 09-02 issues (#341, #353, #363, #365) come from concurrent audits; the
  report should not collide with them.
- Matthew Rocklin's "Craft Minimal Bug Reports": the MCVE below makes its own
  6-sample PED/MAP, has no line that is not needed, prints got vs expected, and says
  what shrinking revealed.

## Contents

| file | what |
|---|---|
| `issue-pl1-hwe-threshold-boundary.md` | bug report: `--hwe` removes 2- and 3-heterozygote variants with p above the threshold (MCVE, cause, fix) |
| `mcve_pl1_hwe_threshold.py`, `mcve_outputs.txt` | the reproduction embedded in the issue, and its output on `master`, `v1.9.0-b.7.12`, `v1.90b6.21` and the patched build |
| `0001-PLINK-1.9-hwe-keeps-variants-whose-exact-p-is-at-or-.patch` | fix in `1.9/plink_stats.c` (`git am`-able on `8bfebe8`) |
| `pr-bodies.md` | PR title and body |

## Verification status of the patch

| check | unmodified `8bfebe8` | with patch 0001 |
|---|---|---|
| MCVE (`mcve_outputs.txt`): variant with `--hardy` P = 0.4805 under `--hwe 0.48` | removed (assertion fails) | kept |
| exhaustive bisection, `SNPHWE_t`, n ≤ 200, ≤ 6 hets (`../verify/pl1_hwe_threshold_boundary.out` / `.patched.out`) | 19,399 of 67,883 tables flip below their p | 0 of 67,883 |
| same, `SNPHWE_midp_t` | 19,399 of 67,883 | 0 of 67,883 |
| CLI tables n = 6, 1007, 307 (same files) | 12 wrong removals of 20 thresholds | 0 of 20 |
| `--hwe` on 400 random variants at 0.05 / 1e-3 / 1e-6, ± `midp` (`../verify/heldup_hardy_cli.py` rerun with `PLINK19` = patched build) | 0 differences from exact | 0 differences |
| version scope (`../verify/version_scope_hwe_cli.*.out`) | `master`, `v1.9.0-b.7.12`, `v1.90b6.21`, `v1.90b4`: affected | patched: unaffected |
| build | `make NO_LAPACK=1 …` clean, same warnings as unmodified | same |
| project tests | none reach this code (`1.9/tests/tests.py` needs a PLINK 1.07 build, not available here); `2.0/Tests` are plink2-only | — |

`git apply --check` succeeds against `8bfebe8`. The patch adds 28 lines (four
identical 7-line blocks) and changes no output outside the affected band.

## Order of operations

1. Open the issue from `issue-pl1-hwe-threshold-boundary.md`.
2. Push `fix/hwe-threshold-tail-sum` to a fork (or `git am` the patch onto a fresh
   `master`), open the PR with the body in `pr-bodies.md`, replacing `#NNN` with the
   issue number.
3. Record issue and PR numbers, and every maintainer response, in `../README.md`
   and in the top-level status table.
