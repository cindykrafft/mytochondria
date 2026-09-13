# GSEA upstream filing kit

_Default branch: **`master`** (PRs go against it). Prepared 2026-09-13 against
`GSEA-MSigDB/gsea-desktop` `master` @ `dc35c76` (2025-03-10, one README-only commit after
the `v4.4.0` tag `2cfcbd9`; `git diff v4.4.0 master` touches only `scripts/readme.txt`).
**Nothing filed, nothing pushed.** The three fixes are single commits on local branches of
the audit clone (`fix/weighted-p1.5-abs-score` = `d44f77e`, `fix/set-size-filter-min-equals-max`
= `8b6aea6`, `fix/zero-weight-gene-set` = `d1c1f03`), `git am`-able from the three patches in this directory
(`git apply --check` clean against `dc35c76`). No fork of `gsea-desktop` exists under
`github.com/cindykrafft` (not among the repositories this session can reach) and
`site/audits.json` has no `gsea` entry, so the `upstream-declines-ai-contributions` topic
cannot apply yet; nothing in the repository declines AI-generated contributions (see below)._

## Filing tier and order (README step 5, `audits/TRIAGE.md`)

| rank | finding | tier | why |
|---|---|---|---|
| 1 | **GS3** — a gene set whose present members all have ranking score 0 is reported with a spurious ES/NES and p-value (default `weighted` scheme; `issue-gs3-*.md`, patch 0003) | **now** | default settings, a realistic preranked input (untested genes given stat 0, a set of unexpressed genes), on the current release and every release the cohort names; the patch implements one of two reasonable fixes (equal weights + warning; the other is exclusion + warning), so the issue offers both |
| 2 | **GS1** — `weighted_p1.5` hit weights for negative scores (`issue-gs1-*.md`, patch 0001) | held / next after a maintainer signal | a documented option, but not a default or common one (6 of 720 cohort papers state a scoring scheme at all); crisp one-line fix with a test |
| 3 | **GS2** — `set_min == set_max` skips the size filter (`issue-gs2-*.md`, patch 0002) | held | rare option value; wrong set collection or a crash; one-hunk fix with a test |

Cap: at most two unanswered filings per repository. Suggested order: GS3 issue + PR 3 and
GS1 issue + PR 1 first; GS2 after one of them has an answer. The notes (FDR numerator formula,
ties, rank-at-max convention, strict nominal p) are not filed.

## What was read before preparing this (step 4 of the method)

- `CONTRIBUTING.md` (the only contribution document): search the tracker first; a new issue
  needs "a title and clear description, as much relevant information as possible, and a code
  sample, executable test case, or clear set of instructions"; a bug-fix PR should "clearly
  describe the problem and solution", include the issue number, and stay focused on one
  issue; feature changes go through an issue first. No AI policy, no DCO or sign-off
  requirement, no coding standard. Shaped the kit: one issue text per finding with an
  executable shell test case (`mcve_*.sh`, outputs in `mcve_outputs.txt`), one patch per
  finding, PR bodies that name the problem, the solution and the behaviour change.
- No `.github/` directory: no issue template, no PR template, no `config.yml`, no
  discussions link, no pinned policy issue. `CODE_OF_CONDUCT.md` (Contributor Covenant)
  is the only other policy file. Bug reports are also taken by e-mail / the GSEA help forum
  (the website's Contact page is linked from `README.md`; the site is not reachable from
  this session).
- Repository history (`git log`, 400 commits fetched): 256 of 263 commits by the
  maintainer (David Eby), a handful by two collaborators, no merged external pull request
  in that window; all work lands on `master` with occasional topic branches. Commit
  messages are one short sentence ("Fixed the Windows launchers", "Removed outdated
  Dependencies section"); the three patches follow that form.
- Tests: `src/test/java/edu/mit/broad/genome/math/{XMathTest,VectorTest}.java` (JUnit 5,
  jars in `lib_test/`, "initial implementation of unit tests"). `build.gradle` declares no
  test task or test dependencies, so the tests are run from an IDE; here they were compiled
  against `lib_test/*.jar` and run through a 25-line reflective runner
  (`kit/runner/RunJUnit5.java` in the scratch directory, described in the PR bodies). No
  linter or formatter configuration in the tree; the Java follows the surrounding style
  (4-space indent, `{ ... }` one-liners as in the touched files).
- No changelog file in the repository (release notes live on the GSEA website), so the
  patches carry no changelog entry.
- Issue tracker searched 2026-09-13 with `mcp__github__search_issues` (eight phrasings:
  `weighted_p1.5` / scoring scheme / negative scores / NaN; `set_min set_max equal` / size
  threshold not applied; FDR calculation vs paper; ties / tied scores / order; `No such
  name` crash; nominal p / NES normalisation; AI policy): **no prior report of GS1, GS2 or
  GS3**. Nearest: #5 "Size thresholds" (closed 2018, 1 comment: a user whose sets were all
  pruned — the error message of the *normal* filter path, not the equal-thresholds path);
  #14 "GSEA 4.0 fails to Infinite values" (closed, 6 comments: infinite ranking scores, the
  origin of the 0.01 substitution in `Weighted`); #10 (FDR axis scale on the global plot,
  closed); #50 (open, FDR-threshold guidance for gene-set permutation); #23, #27, #39
  (unrelated). The tracker has 50-odd issues in total.
- Matthew Rocklin's "Craft Minimal Bug Reports" as summarised in the project brief: the
  three MCVEs make their data in the script (12, 30 or 40 genes), contain no unneeded line, print
  expected vs got, and the issue texts say what shrinking revealed.

## Contents

| file | what |
|---|---|
| `issue-gs1-weighted-p15-negative-scores.md` | GS1 bug report (title + body in CONTRIBUTING's order: description, executable test case, expected/got, fix) |
| `issue-gs2-set-min-equals-max.md` | GS2 bug report |
| `issue-gs3-zero-weight-gene-set.md` | GS3 bug report (two fix options offered; the patch implements the first) |
| `mcve_gs1_weighted_p15.sh`, `mcve_gs2_set_min_equals_max.sh`, `mcve_gs3_zero_weight_set.sh`, `mcve_outputs.txt` | the reproductions embedded in the issues and their output on `master` and on the patched builds |
| `0001-Fixed-the-weighted_p1.5-hit-weight-for-negative-rank.patch` | GS1 fix (one line) + `GeneSetScoringTablesTest` |
| `0002-Apply-the-gene-set-size-filter-also-when-set_min-equ.patch` | GS2 fix (one hunk) + `GeneSetCohortGeneratorTest` |
| `0003-Give-equal-hit-weights-to-a-gene-set-whose-members-a.patch` | GS3 fix (equal weights when the total weight is 0, a warning) + `ZeroWeightGeneSetTest` |
| `pr-bodies.md` | PR titles and bodies |

## Verification status of the patches

All five test classes (the project's `XMathTest` + `VectorTest`, 55 tests, and the three new
classes, 7 tests) compiled against the jar built from each tree and run with the reflective
runner (`kit/*_tests.txt` in the scratch directory):

| tree | result | new tests |
|---|---|---|
| unmodified `master` @ `dc35c76` + the three new test classes | 55 passed, **6 failed** | the three `weighted_p1.5` assertions, `equalMinAndMaxKeepsOnlySetsOfExactlyThatSize` and the two `ZeroWeightGeneSetTest` tests fail |
| `master` + patch 0001 | 58 passed, 3 failed | `GeneSetScoringTablesTest` passes; the GS2 and GS3 tests still fail (expected, other patches) |
| `master` + patch 0002 | 56 passed, 5 failed | `GeneSetCohortGeneratorTest` passes; the GS1 and GS3 tests still fail (expected) |
| `master` + patch 0003 | 57 passed, 4 failed | `ZeroWeightGeneSetTest` passes; the GS1 and GS2 tests still fail (expected) |

The jars built from each branch were also run through the audit harnesses:
`verify/gs1_weighted_p15_negative_scores.patched.out` (every set matches the |r|^1.5
definition to 2e-7), `verify/gs2_set_min_equals_max.patched.out` (`-set_min 20
-set_max 20` keeps the two size-20 sets; the absent-identifier collection runs) and
`verify/gs3_zero_weight_set.patched.out` (the all-zero sets get the classic ES; the
planted sets unchanged).

## Order of operations

1. Open the GS3 issue and PR 3 (patch 0003) from a fork branch, then the GS1 issue and
   PR 1 (patch 0001); put each issue number in its PR body.
2. After a maintainer responds on either, open the GS2 issue and PR 2 (patch 0002).
3. Record issue and PR numbers, and every maintainer response, in `../README.md` and the
   top-level status table.
