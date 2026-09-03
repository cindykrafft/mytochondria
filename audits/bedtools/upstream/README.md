# BEDTools upstream filing kit

_Prepared 2026-09-03 against `arq5x/bedtools2` **master** @ `614e9a5`
(2026-06-10). Default branch: **master** (needed for the PR compare URL:
`https://github.com/arq5x/bedtools2/compare/master...<branch>`)._

**Nothing has been filed.** The three fix branches were built from
`master` @ `614e9a5` in a local worktree and the full `make test` suite passes on
each; the `git format-patch` patches are in this directory and each applies
cleanly to a fresh `master` checkout.

| finding | branch | patch | tests added |
|---|---|---|---|
| BT1 | `fix/coverage-split-hit-count` | `0001-coverage-split-count.patch` | test/coverage/test-coverage.sh t10,t10b changed; t10c–t10g added |
| BT2 | `fix/intersect-split-per-record-F` | `0002-intersect-split-per-record-F.patch` | test/intersect/test-intersect.sh t22.p changed; t22.s,t22.t added |
| BT4 | `fix/large-chrom-int-truncation` | `0003-large-chrom-coordinates.patch` | test/{reldist,subtract,flank}/ large-chromosome case each |

BT3 (closest tie order) and BT5 (`-pct` float) are confirmed but their fixes are
invasive (a `RecDistList` redesign; option-parsing signature changes) and are
filed as issues only, with the fix shape described.

## What was read before preparing this (step 4 of the method)

- **No `CONTRIBUTING.md`, no `.github/ISSUE_TEMPLATE`, no
  `.github/PULL_REQUEST_TEMPLATE`, no `config.yml`, no `CODE_OF_CONDUCT`, no
  `.clang-format`, no pinned policy issue** — checked the repo root and
  `.github/` (which contains only `workflows/main.yml`). So there is no issue
  form to fill and no changelog fragment convention; the issue texts here use the
  usual bug-report shape (version, command, input, produced vs expected output,
  cause, fix), which is what the existing well-formed issues (#673, #1142) use.
- **`.github/workflows/main.yml`**: CI is `make -j8 && make test` then
  `make -j8 static` on ubuntu-latest with libbz2/liblzma/zlib. The bar for a PR
  is that the per-tool test suites in `test/` still pass; each patch adds tests
  in the relevant tool's `test-<tool>.sh` and the full `make test` passes.
- **`docs/content/history.rst`**: the changelog is edited by hand at release time
  as numbered bullets crediting contributors by GitHub handle; there is no
  per-PR fragment, so the patches add none. A one-line history entry can be added
  when a release is cut.
- **`docs/content/tools/{coverage,intersect,closest,reldist,subtract,flank,slop,
  fisher,jaccard,shuffle,map,merge,genomecov}.rst`**: the statement of intended
  behaviour each finding is measured against (e.g. closest `-t first` = "first
  tie in the B file"; coverage count column = "number of features in B that
  overlapped"; `-f` = "minimum overlap required as a fraction of A").
- **Issue tracker** (`mcp__github__search_issues`, several phrasings per finding,
  2026-09-03). Nearest prior issues, recorded even where none matches:
  - BT1 → **#673** (open, 2018, `coverage -split -f 1.0 -counts` wrong count — the
    same defect; the patch here also fixes the default count column and `-f`),
    #591, #8.
  - BT2 → **#1142** (open, 2026-08-05, exact match with a `BlockMgr.cpp`
    root-cause read) and **#1141** (same defect via `-wao -f`); #928. The BT2
    text is drafted as a **comment on #1142**, not a new issue.
  - BT3 → none (nearest #157, #471, #148 about `-iu/-id`, `-k` and hangs).
  - BT4 → #1060 (open, 32-bit overflow on line counts, different); none on
    coordinate truncation in these tools.
  - BT5 → none (nearest #45, #195, closed, are other slop bugs).
  - BT6 (note) → **#1089** (open, 2024, "-incl: fall out of include.bed") and
    #381 (closed, related length weighting).
- **Matthew Rocklin, "Craft Minimal Bug Reports"**: each issue text carries a
  synthetic reproduction made in the snippet, no unnecessary line, produced-vs-
  expected stated, and a "what shrinking showed" sentence. The standalone MCVE
  scripts are `mcve_bt{1,2,3,4,5}.py` and their output is `mcve_outputs.txt`.

## Contents

| file | what |
|---|---|
| `issue-bt1-coverage-split-count.md` | BT1 bug report (also relevant to #673) |
| `issue-bt2-intersect-split-F.md` | BT2, drafted as a comment on #1142 |
| `issue-bt3-closest-tie-order.md` | BT3 bug report (issue only) |
| `issue-bt4-large-chrom-coordinates.md` | BT4 bug report |
| `issue-bt5-pct-float-truncation.md` | BT5 bug report (issue only) |
| `mcve_bt{1,2,3,4,5}.py`, `mcve_outputs.txt` | the reproductions and their output on the master build |
| `0001-coverage-split-count.patch` | BT1 fix + tests (git am-able on master) |
| `0002-intersect-split-per-record-F.patch` | BT2 fix + tests |
| `0003-large-chrom-coordinates.patch` | BT4 fix + tests |
| `pr-bodies.md` | PR titles and bodies (#NNN placeholders) |

## Verification status of the patches (executed)

Built each branch from `master` @ `614e9a5` and ran the full `make test`:

| patch | new/changed tests on unmodified master | full `make test` with patch |
|---|---|---|
| 0001 (BT1) | coverage t10/t10c–t10g **fail** on master | all tools pass (negativecontrol expected-fail) |
| 0002 (BT2) | intersect t22.q/t22.s/t22.t **fail** on master | all tools pass |
| 0003 (BT4) | reldist/subtract/flank bigchrom **fail** on master | all tools pass |

Unmodified master: all tool suites pass (negativecontrol is the intentional
failure). `git apply --check` succeeds for each patch against a clean `master`.

## Version scope (executed, `../verify/version_scope_cli.*.out`)

Every confirmed finding (BT1–BT5) reproduces identically on **master**,
**v2.31.1** (latest release) and **v2.30.0** (the cohort's most-cited version).
No release in scope is unaffected. (v2.30.0 needed a one-line `#include <cstdint>`
in `src/utils/general/ParseTools.h` to compile with this GCC; the code paths
under test are unchanged by that.)

## Order of operations

1. Comment on **#1142** with the BT2 confirmation + patch; comment on **#673**
   (or open a fresh issue) with the BT1 broader scope + patch; open new issues
   for BT3, BT4, BT5 from the texts here.
2. Because all of these change published numbers, get the maintainer's agreement
   on the number changes (especially the coverage.t10 and intersect.t22.p
   expected-value changes) before opening PRs 1–3.
3. Record issue/PR numbers and every maintainer response in `../README.md` and
   the top-level status table.
