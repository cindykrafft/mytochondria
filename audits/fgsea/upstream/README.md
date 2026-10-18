# fgsea upstream filing kit

_Default branch: **`master`** (PRs go against it). Prepared 2026-10-18 against `alserglab/fgsea`
`master` @ `570f590` (1.39.4; the current Bioconductor release 1.38.0 is numerically identical).
**Nothing filed, and nothing at the "now" tier.** Fork needed: **alserglab/fgsea** (none exists
under `cindykrafft`; `site/audits.json` lists `ctlab/fgsea` only under the clusterProfiler entry,
with no fork)._

Filing tier (TRIAGE rule): **no "now" item.** The two findings that changed numbers in published
work are reported and fixed upstream: FG1 (leading edge, #176, fixed in 1.31.3) and FG2 (the
multilevel sampler near ES = 1 with ties, #151, fixed in 1.37.1/1.38.0). They are duplicates and
are not filed. The current release reproduced every checked number. Held, ready if a filing is
wanted for another reason:

| order | finding | material | why held |
|---|---|---|---|
| 1 | FG5: vacuous reproducibility test; `setUpBPPARAM(nproc = 1)` | `issue-fg5-reproducibility-test-compares-null.md`, `pr-bodies.md` § PR 1, `0001-*.patch`, `0002-*.patch` | test/code quality, no number changes; the low-risk first contact if one is wanted |
| 2 | FG3: all-zero gene set gets an order-dependent ES with no ties warning | `issue-fg3-all-zero-set-order-dependent-es.md`, `mcve_fg3_all_zero_set.R` / `.out` | design question (the equal-weight branch is intentional); precondition not met by any MSigDB set on real lists; send as a question after a positive reply on item 1, and only after #18 has been read in full verbatim |
| — | FG4: floating tie counting in fgseaSimple | review only | ≤ 0.001 % of the tail at realistic list lengths; no draft |

Two-filing cap: at most two filings until a maintainer responds. Items 1 and 2 would be the two,
in that order.

## What was read before preparing this

- **Contribution rules.** No `CONTRIBUTING`, no `CODE_OF_CONDUCT`, no issue or PR template and no
  AI-contribution policy anywhere in the tree (`README.md`, `NEWS`, `DESCRIPTION`, `vignettes/`,
  `.github/`, which holds only `workflows/R-CMD-check.yaml`, searched on `570f590`).
  `DESCRIPTION`: `BugReports: https://github.com/alserglab/fgsea/issues`, MIT licence. `NEWS` is a
  plain `CHANGES IN VERSION x.y.z` list.
- **CI.** `R-CMD-check.yaml` runs `r-lib/actions/check-r-package` on macOS, Windows and Ubuntu
  (R devel, release, oldrel-1) for pushes and PRs against `master`. The PR body names the testthat
  command run here (`test-runs.txt`).
- **Maintainer practice** (from the threads in `dupcheck-2026-10-18.md`). Alexey Sergushichev
  (`assaron`) answers within a day, asks for a reproducible example, and closes questions that
  turn out to be usage. PR #181 (2026-03-21, an outside contributor) was closed the same day: it
  named no issue, and it changed intended single-pathway behaviour. His stated priority is
  reproducibility of the same analysis on the same version. Hence issue first, then the PR, and
  nothing that changes random streams.
- **Bioconductor.** Fixes reach users through the next Bioconductor release; the maintainer does
  not backport complex changes to the release branch (#151, 2026-04-13). Bioconductor 3.24 is
  devel (fgsea 1.39.2 there).
- `site/audits.json` records no fork of `alserglab/fgsea`, so the
  `upstream-declines-ai-contributions` topic cannot apply. No fgsea filing from this project
  exists (all 141 issues and 41 PRs were checked by title).

## Contents

| file | what |
|---|---|
| `issue-fg5-reproducibility-test-compares-null.md` | held: the `nMoreExtreme` comparison and the `setUpBPPARAM` overwrite, with real output |
| `issue-fg3-all-zero-set-order-dependent-es.md` | held: question with the reproducer, three possible changes offered |
| `mcve_fg3_all_zero_set.R`, `mcve_fg3_all_zero_set.out` | FG3 reproducer, output on 1.38.0 and 1.39.4 |
| `0001-Compare-p-values-in-the-fgseaMultilevel-reproducibil.patch` | FG5 test fix (`tests/testthat/test_gsea_multilevel.R`), commit eed4184 on `fix/bpparam-repro-test` |
| `0002-Use-SerialParam-for-nproc-1-as-intended.patch` | FG5 `setUpBPPARAM` fix (`R/fgsea.R`, `if` → `else if`), commit b718c5c |
| `pr-bodies.md` | PR 1 title and body (held) |
| `test-runs.txt` | fgsea's testthat suite on master and on the branch; mutation check of the test |
| `dupcheck-2026-10-18.md` | prior-report search and verdicts |

## Verification status of the patches

| branch | commits | check | project tests |
|---|---|---|---|
| `fix/bpparam-repro-test` (local, scratch clone; not pushed) | `eed4184`, `b718c5c` on `570f590` | the patched test fails when one of its calls is seeded differently (2 of 6 expectations); the old test passes the same mutation; `setUpBPPARAM(nproc = 1)` now returns `SerialParam` | 61 tests, 152 expectations, 0 failures, 2 skipped (reactome.db, GEOquery) on master and on the branch (`test-runs.txt`) |

## Order of operations (only if a filing is decided)

1. Fork `alserglab/fgsea`; `git am` the two patches onto `master` as `fix/bpparam-repro-test`; push.
2. Open the FG5 issue, then the PR with `pr-bodies.md` § PR 1 (issue number in its first line).
3. After a maintainer reply, and after a helper session has exported #18 verbatim and it has been
   read, the FG3 question.
4. Record numbers and responses in `../README.md` and the top-level status table.
