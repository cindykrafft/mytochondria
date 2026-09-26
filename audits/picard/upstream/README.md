# Picard upstream filing kit

_Default branch: **`master`** (PRs go against it). Prepared 2026-09-24 against
`broadinstitute/picard` `master` @ `c2a483d` (htsjdk 5.0.0). **Nothing filed.** The three fixes are single commits (fix +
TestNG regression test) on `c2a483d`, pushed to the fork `cindykrafft/picard` on 2026-09-26
(`fix/rnaseq-coverage-last-base` @ `50959b5b`, `fix/hsmetrics-zero-cvg-denominator` @ `0305ec69`,
`fix/alignment-summary-bisulfite-ref-index` @ `3b443b78`). The original local clone was lost in a
container restart, so the branches were rebuilt with `git am` from the patches in this directory:
same author, date, message and diff; only the committer date and therefore the SHAs differ from the
`From` lines of the patches. `broadinstitute/picard` `master` is still `c2a483d`._

Filing tier (README step 5): **now** for P1 and P2 — both change numbers that reach QC tables
under default settings (`CollectRnaSeqMetrics` coverage statistics; `CollectHsMetrics`
`ZERO_CVG_TARGETS_PCT`) on the current release and every release the cohort names (P2 since
2.19.0), and neither has a prior report. **P3 ready** as the third filing (a documented option, but
the only route to alignment metrics for bisulfite data; a wrong number and a crash) once P1 or P2
has a reply, under the two-unanswered-filings cap. P4 (comment for #1278) and P5–P7 are **held**.

## What was read before preparing this (step 4 of the method)

- No `CONTRIBUTING.md`, no `CODE_OF_CONDUCT`, no AI-contribution policy anywhere in the tree
  (`README.md`, `.github/`, `build.gradle`, `docs/` searched). `README.md` sends user questions
  to the GATK forum.
- `.github/PULL_REQUEST_TEMPLATE.md`: a concise descriptive title; the changes, the motivation and
  the issues addressed in a Description; then a **checklist that must never be deleted** (tests
  added or modified; README/documentation edited if applicable; all tests passing on GitHub
  Actions; final thumbs-up from a reviewer; rebase, squash and reword as applicable), linking the
  wiki "Guidelines for pull requests". `pr-bodies.md` keeps the checklist verbatim under each
  description with the applicable boxes ticked and a note on the inapplicable one.
- `.github/ISSUE_TEMPLATE.md`: a header stating the tracker is for bug reports only and asking
  for a support-forum post first; a Bug Report block (affected tool(s), affected version(s) with
  release/master checkboxes, description, steps to reproduce, expected and actual behaviour).
  The three issue texts follow the block in order. Reproducible bugs with a fix do go straight to
  the tracker in practice (#1971 by a Broad user, #1522 ported by a maintainer); the texts work
  verbatim as forum posts if the submitter prefers the letter of the header.
- `.github/workflows/tests.yml`: `./gradlew compileJava` then the TestNG suite on Temurin 17 with
  and without the Barclay parser tests (`test` depends on `barclayTest`); R installed for chart
  tests; `cloud_tests.yml` needs Broad credentials. No linter or formatter.
- Metric definitions in `RnaSeqMetrics.java`, `PanelMetricsBase.java` ("the fraction of targets
  that did not reach coverage=1 over any base"), `AlignmentSummaryMetrics.java` and the
  metric-definitions page they generate, as the statement of intended behaviour.
- `git log -S` and the release tags: the P2 denominator has been `allTargets.getIntervals().size()`
  since 2016; htsjdk 2.15.1 (Picard 2.18.7) `IntervalList.fromFiles` returned `union(...)`, htsjdk
  2.19.0 (Picard 2.19.0) `concatenate(...)` (samtools/htsjdk#1273, 2019-02-21, Y. Farjoun); the P3
  line predates 2.18.7.
- Issue tracker searched 2026-09-24 (eight `search_issues` phrasings across the three tools) and
  nine threads read in full through a helper session (artifact "Mytochondria threads picard 1278
  1532 1522 1647 1605 1971 787 1330 1609"): **no prior report of P1, P2 or P3**. #1278 (2019, open,
  no labels) is P4's window off-by-one — the maintainer replied "there seems to be a off-by-one
  bug here. Would appreciate your fix" and nothing followed; #1532/#1522 are `CollectGcBiasMetrics`
  AIOOBEs on large references (a different index); #1647 asks for an option not to merge abutting
  targets in the per-target output (related to P2's merging, no comments); #1605 is about bait vs
  target definitions; #1971 (2024, open, assigned) is P7 and already argues FOLD_80 should exclude
  zero-coverage targets; #787 (2017, open) is about supplementary reads in the alignment
  collector and carries the maintainer's wish that `BAD_CYCLES` be documented as "no-calls or
  mismatched the reference" (P5 context); #1330 and #1609 are questions about the RNA-seq
  histogram and per-transcript bias.
- `site/audits.json` records no fork of `broadinstitute/picard` under `cindykrafft`; the
  `upstream-declines-ai-contributions` topic cannot apply yet.

## Contents

| file | what |
|---|---|
| `issue-p1-rnaseq-coverage-last-base.md` | bug report in the template's block: shell reproduction (refFlat + spliced SAM), expected vs got, the realistic-library numbers, fix offer |
| `issue-p2-hsmetrics-zero-cvg-targets-pct.md` | bug report: eight-interval list + 20-read SAM, 0.5 vs 0.667, the htsjdk 2.19.0 regression trail |
| `issue-p3-alignment-summary-bisulfite-ref-index.md` | bug report: converted reads on contigs starting with A vs C, the `40S60M` crash |
| `0001-CollectRnaSeqMetrics-count-the-last-base-of-each-al.patch` | P1 fix (`Gene.java`) + `CollectRnaSeqMetricsTest.testCoverageIncludesLastBaseOfEachAlignmentBlock` |
| `0002-CollectHsMetrics-divide-ZERO_CVG_TARGETS_PCT-by-the.patch` | P2 fix (`TargetMetricsCollector.java`) + `CollectHsMetricsTest.testZeroCvgTargetsPctCountsUniqueTargets` |
| `0003-CollectAlignmentSummaryMetrics-compare-bisulfite-ba.patch` | P3 fix (`AlignmentSummaryMetricsCollector.java`) + `CollectAlignmentSummaryMetricsTest.testBisulfiteMismatchesUseTheAlignedReferenceBase` + two small test-data files |
| `pr-bodies.md` | PR titles and bodies in the template's layout with the checklist |
| `comment-p4-1278-gcbias-window.md` | held: comment for #1278 with the measured effects and a fix shape |

## Verification status of the patches

Harness runs (`../verify/*.patched.out`, jar built from all three fixes): P1's two-exon transcript
gives `MEDIAN_CV_COVERAGE` 0 and a flat histogram; the 276-gene library matches the independent
per-base truth to six digits (`MEDIAN_CV_COVERAGE` 0.430119, biases 0.233688 / 0.529971 /
0.466054); P2 gives 0.666667; P3 gives `PF_MISMATCH_RATE` 0 on both contigs and no exception; the
held-up harnesses (`MarkDuplicates`, insert size, WGS, alignment summary) are unchanged.

Picard's own tests (TestNG, Temurin 17, `./gradlew test -x barclayTest --tests <class>` and
`barclayTest --tests <class>`, i.e. both command-line parsers as CI runs them; details in
`test-runs.txt`):

| branch | commit | test class | result |
|---|---|---|---|
| `fix/rnaseq-coverage-last-base` | `50959b5b` (was `35f8617d`) | `CollectRnaSeqMetricsTest` | 12 / 12 pass with both parsers; the new test fails on `master`; `testBiasEndBiasAdjust`'s expected values, taken from the tool's output with the off-by-one, are replaced by the values derived from the read layout (1.6 / 2.466667 / 1.666667 / 0.675676) |
| `fix/hsmetrics-zero-cvg-denominator` | `0305ec69` (was `eba097ba`) | `CollectHsMetricsTest` | 15 / 15 pass with both parsers; the new test fails on `master` (0.5) |
| `fix/alignment-summary-bisulfite-ref-index` | `3b443b78` (was `a01cc321`) | `CollectAlignmentSummaryMetricsTest` | 17 / 17 pass with both parsers; the new test fails on `master` (exception); the existing bisulfite test is unchanged (its reads sit at contig position 1, where offset and position coincide) |

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| P1 | 2.18.7, 2.27.4, 3.0.0, 3.3.0, `master` (`../verify/r1_rnaseq_exon_last_base.v*.out`) | patched |
| P2 | 2.27.4, 3.0.0, 3.3.0, `master` | 2.18.7 (htsjdk 2.15.1 uniqued the list), patched |
| P3 | 2.18.7, 2.27.4, 3.0.0, 3.3.0, `master` | patched |
| P4, P5 | 2.18.7, 2.27.4, 3.0.0, 3.3.0, `master` | — |

## Order of operations

1. ~~Fork `broadinstitute/picard`; tell the session; the three branches are pushed.~~ Done 2026-09-26.
2. Open the P1 issue from `issue-p1-rnaseq-coverage-last-base.md`, then the PR from
   `fix/rnaseq-coverage-last-base` with the body from `pr-bodies.md` § PR 1 (issue number in the
   first line). Same for P2 (`fix/hsmetrics-zero-cvg-denominator`, § PR 2).
3. When one of them has a maintainer reply, P3 (`fix/alignment-summary-bisulfite-ref-index`, § PR 3)
   and the #1278 comment.
4. Record issue and PR numbers and every maintainer response in `../README.md` and the top-level
   status table.
