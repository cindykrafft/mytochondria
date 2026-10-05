_Update 2026-10-05: CP4 is NOT to be filed. Duplicate check (`dupcheck-2026-10-05.md`): YuLab-SMU/enrichit#3, opened 2026-10-01 23:40 by @musharna, reports the same bug on the same devel commit (23f64ce5), the same lines of `src/gsea.cpp` and the same fgsea-style fix; open, no comments. It does not cover our second point (p = 1/(nPerm+1) when ES = +/-1 on the `sample` path) or the exact-enumeration test. If anything, those go as a comment on #3. The branch's NEWS and test hunks now conflict with devel 3abcc6d. Owner, 2026-10-05: #3 is not theirs (an independent report by someone else), so CP4 counts as reported by another user, not as our filing._

# clusterProfiler / enrichit upstream filing kit

_Update 2026-10-02: CP4 goes to enrichit directly (owner's go-ahead) and is in Do next. `fix/gsea-sign-conditioned-pvalue` rebased onto enrichit devel 23f64ce (0.2.5; NEWS and test-file conflicts resolved by keeping both sides, the NEWS entry now under 0.2.5.001), re-authored as Cindy Krafft and force-pushed (`217a839`); patch 0001 regenerated. Re-verified on builds of 23f64ce with and without it (yulab.utils and gson from GitHub): the exact-enumeration test fails on devel and passes with the change; the whole testthat suite is 52 tests, 1 failure + 1 error on devel and 0 failures + the same 1 error with the change (`bayes_enrich candidate modes`, an environment error on both)._

Default branches: `YuLab-SMU/clusterProfiler` **`devel`**, `YuLab-SMU/enrichit` **`devel`**,
`YuLab-SMU/DOSE` `devel`, `ctlab/fgsea` `master` (development at `alserglab/fgsea`).

_Prepared 2026-09-08 against clusterProfiler `devel` @ `93835a3` and enrichit `devel` @ `a261244`.
Nothing filed, nothing pushed. No project fork of these repositories exists yet; `site/audits.json`
has no entry for them, so the `upstream-declines-ai-contributions` check is moot._

_Update 2026-10-01: the forks `cindykrafft/clusterProfiler` and `cindykrafft/enrichit` exist and
`site/audits.json` maps both repositories. The enrichit fork carries `fix/gsea-sign-conditioned-pvalue`
(patch 0001, for CP4). Nothing is prepared for a clusterProfiler PR: CP1 is held (fixed upstream).
Nothing filed._

## Tiers (README step 5)

| item | tier | why |
|---|---|---|
| CP4 — enrichit `gsea(method = "sample"/"permute")`, `adaptive = TRUE` p-values | **held** | wrong number at master, but a non-default path; `issue-cp4-enrichit-sample-pvalue.md` + patch 0001 ready for `YuLab-SMU/enrichit` |
| CP5 — ORA BH over zero-overlap sets (enrichit 0.1.x) | **comment** on open clusterProfiler #819 | the thread is the maintainers'; fixed in enrichit 0.2.0; `comment-cp5-issue819.md`, to be posted only after reading the 6 comments (unreadable from this session) |
| CP1 — GSEA table filtered on raw p (release 4.20.0 + CRAN enrichit ≤ 0.2.1) | **held** | fixed and announced upstream (enrichit 0.2.2 NEWS, clusterProfiler 4.21.1.003 NEWS); only the CRAN release is missing; `issue-cp1-gsea-table-rawp.md` is a heads-up for use if 0.2.2 is still not on CRAN at the next Bioconductor release |
| CP2, CP3 (legacy DOSE engine), CP6, CP7 (fixed enrichit releases) | held | not at master |
| CP8 (`simplify` orphans) | held | design question; no text prepared beyond the review |
| fgsea | nothing | every check held up |

## What was read before preparing this (step 4 of the method)

- clusterProfiler `CONTRIBUTING.md` (issues: packages loaded at the top, data via `dput()`,
  commented minimal code, verified in a fresh session; "Pull requests" heading with no text).
- clusterProfiler `.github/issue_template.md`: prerequisites (latest release, documentation, google),
  a reproducible example with comments on expected vs actual, and the venue rule — bugs and feature
  requests on GitHub, questions on Bioconductor support / Biostars with the `clusterProfiler` tag.
  It links the maintainer's guide "how to bug author" (`guangchuangyu.github.io/2016/07/...`) and
  the package book (`yulab-smu.top/biomedical-knowledge-mining-book/`, `contribution-knowledge-mining/`);
  **both hosts were unreachable from this session (HTTP 000) and must be read before anything is sent.**
- clusterProfiler `NEWS.md` (4.19.3 engine switch; 4.21.1 `eps` restored, #822; 4.21.1.003 GSEA
  filtering aligned, `seed` restored; 4.19.8/4.19.5 universe and keyType changes, #805/#823) and
  `DESCRIPTION` (`BugReports` → GitHub issues; `Imports: enrichit (>= 0.1.6)`; at the 4.20.0 release
  commit `d67d9f6`, `enrichit (>= 0.1.1)`). No PR template, no `.lintr`, no results-stability
  policy; `docs/adr/0001` is a product-direction record (mechanism interpretation).
- enrichit `NEWS.md` (0.2.0: zero-overlap sets excluded, #819/#821; 0.2.1: size filter on the
  overlap, #824; 0.2.2: p-value filtering aligned, seed), its tests (`tests/testthat/test-gsea.R`,
  `test-ora.R`, …), no CONTRIBUTING or templates; its only issue (#1, "rows with NA p-values should
  be filtered?") is closed. The `cran/enrichit` mirror: releases 0.0.8 (2025-12-22) … 0.2.1
  (2026-08-04); 0.2.2 not on CRAN on 2026-09-08.
- fgsea `NEWS` (1.37.1 hash-based ties and integer weights; 1.35.1 reproducibility) and README; no
  CONTRIBUTING or templates.
- Matthew Rocklin's "Craft Minimal Bug Reports" (as in the scanpy kit): the MCVEs make their data
  in the script, contain no unneeded line, end in an assertion, state expected vs got, and say
  what shrinking revealed.
- Issue trackers searched 2026-09-08 (`repo:` listings sorted by creation plus two keyword queries,
  one per minute): clusterProfiler open issues **#819** (CP5, exact match, 6 comments), #777
  ("enrichGO results not filtered by default pvalueCutoff", 2025-06, pre-enrichit, nearest to CP1),
  #103 ("leading_edge and core_enrichment columns", 2017, nearest to CP2), #763, #753; enrichit #1;
  fgsea open #18 (ties), #93, #143 — none matches CP1/CP2/CP4. The `ctlab/fgsea` path is not
  searchable (moved to `alserglab/fgsea`).

## Contents

| file | what |
|---|---|
| `issue-cp4-enrichit-sample-pvalue.md` | bug report for enrichit (template-free repo; written in the clusterProfiler template's order), MCVE with exact enumeration |
| `0001-Condition-sample-permute-adaptive-GSEA-p-values-on-t.patch` | CP4 fix in `src/gsea.cpp` + regression test in `tests/testthat/test-gsea.R` + NEWS entry; `git am`-able on enrichit `a261244` |
| `pr-bodies.md` | PR body for patch 0001 |
| `comment-cp5-issue819.md` | comment draft for clusterProfiler #819 |
| `issue-cp1-gsea-table-rawp.md` | heads-up text for CP1 (held) |
| `mcve_cp1_gsea_table_rawp.R`, `mcve_cp4_sample_pvalue.R`, `mcve_cp5_ora_zero_overlap_bh.R`, `mcve_outputs.txt` | the reproductions, run under the engine versions that carry each defect and the one that does not |

## Verification status of the patch

Built into a scratch library (`R CMD INSTALL --no-docs`) from a branch
`fix/gsea-sign-conditioned-pvalue` on enrichit `a261244`; tests run with `testthat::test_dir` on
the installed package (the project has no linter configuration):

| build | `tests/testthat/test-gsea.R` | full suite (9 files) |
|---|---|---|
| unmodified `devel` + new test | 11 tests, **5 failed** (all five expectations of the new test: `sample` p = 0.429 vs exact 0.882, …) | 37 tests, 5 failed |
| patched | 11 tests, 0 failed | 37 tests, 0 failed, 8 warnings (pre-existing `eps`/qvalue warnings) |

With the patch, `gsea(method = "sample", nPerm = 2e5)` returns p = 0.8791 and `permute` 0.8925 for the
set whose exact same-sign p is 0.8824 and whose `multilevel` p is 0.8789 (`mcve_outputs.txt` and the
build log in the review).

## Order of operations

1. Read the maintainer's guide and book pages, and the #819 thread.
2. Post the CP5 comment on #819 if it adds something the thread does not have.
3. After a maintainer signal on that repository, open the CP4 issue on `YuLab-SMU/enrichit`, then
   the PR from a fork branch carrying patch 0001.
4. Record numbers and responses in `../README.md` and the top-level status table.
