# GSEA upstream filing kit

**Default branch: `master`.** Prepared 2026-09-10 against `GSEA-MSigDB/gsea-desktop`
`master` @ `dc35c7642d93fabc3223f1db5f844b0f1cadbdc2`. **Nothing has been filed.** Both
patches are one commit on top of that commit, made in the audit's scratch clone; neither
branch has been pushed anywhere.

## What was read before preparing this (step 4 of the method)

- **`CONTRIBUTING.md`** — the project's only contributing document. It asks contributors to
  (a) search the tracker before opening an issue, (b) give a bug report "a **title and
  clear description**, as much relevant information as possible, and a **code sample,
  executable test case, or clear set of instructions** demonstrating the expected behavior
  that is not occurring", (c) open a pull request for a patch whose description "clearly
  describes the problem and solution", includes the issue number, and stays "as focused as
  possible… not to fix multiple unrelated issues with a single pull request". This shaped
  the kit directly: each issue text carries a runnable shell MCVE that writes its own
  inputs, and the two fixes are on **two separate branches** with **two separate PR
  bodies** rather than one combined change.
- **`CODE_OF_CONDUCT.md`** — reporting address `gsea-team@broadinstitute.org`; no bearing
  on the content of a bug report.
- **`README.md`** — points general questions at the GSEA website contact page and the help
  forum. Both findings are defects with a reproduction, so they belong on the tracker, not
  the forum.
- **There is no `.github/` directory**: no issue form, no issue template, no pull-request
  template, no workflows. The issue texts are therefore plain markdown in the order
  `CONTRIBUTING.md` implies (title, description, expected vs got, versions, MCVE, proposed
  fix). The `Title:` first line is this kit's convention, not the project's.
- **There is no changelog file** in the repository (no `CHANGES`, `NEWS`, `CHANGELOG`;
  release notes live on the GSEA website), so neither patch carries a changelog fragment.
- **There is no AI policy** anywhere in the repository, and no fork
  `cindykrafft/gsea-desktop` exists, so there is no `upstream-declines-ai-contributions`
  topic to respect. Nothing here restricts AI-assisted contributions; the attribution
  footer is kept on both issues and both PR bodies.
- **`build.gradle` / `settings.gradle`** — there is **no `test` task** and no test
  dependency block; the JUnit 5.7.2 jars sit unwired in `lib_test/`, and the three existing
  test classes (`XMathTest`, `VectorTest`, and the two added here) are not run by any
  build. Both PR bodies say how the tests were executed and offer to wire a JUnit task in a
  separate PR — a change `CONTRIBUTING.md`'s "keep the pull request as focused as possible"
  rule says should not ride along with a bug fix.
- **No linter or formatter config** exists (no checkstyle, spotless, editorconfig or
  google-java-format setting), so there was nothing to run. Both patches follow the
  surrounding file's brace and indentation style.
- Matthew Rocklin's *Craft Minimal Bug Reports*: both MCVEs create their data in the
  script (no attachment, no download), contain no line that is not needed, state expected
  vs got explicitly, report the exact exception text where one is thrown, and each issue
  says what shrinking the example revealed (GS1: the data are irrelevant, the sibling
  schemes stay correct, which isolates the exponent; GS2: only the *equality* of the bounds
  matters, `-set_min 20 -set_max 21` is fine, which isolates the `!=` guard).

## Prior-art search on the tracker (2026-09-10, `mcp__github__search_issues`)

Queried with several phrasings: "weighted_p1.5 scoring scheme negative scores enrichment
score wrong"; "scoring scheme"; "weighted p1.5 NaN negative rank metric hit weight
down-regulated gene set enrichment wrong ES"; "gene set size filter set_min set_max
enrichment score gsea"; "Size thresholds min max equal". The tracker is small — 16 issues
surfaced in total, 2017–2022, most of them usage questions.

**No prior report of either finding.** Nearest neighbours, none of them the same bug:

| # | title | why it is not this |
|---|---|---|
| 5 | Size thresholds (closed, 1 comment) | the opposite symptom of the *working* filter: every set pruned away, `BadParamException: After pruning, none of the gene sets passed size thresholds`, with unequal bounds 15/500 |
| 14 | GSEA 4.0 fails to Infinite values (closed, 6 comments) | non-finite values in the input dataset, not in the hit weights |
| 26 | report sort error (open, 0 comments) | ordering of rows in the HTML report |
| 42 | Abs.max in Collapse Dataset (closed, 3 comments) | the collapse mode, which held up in this audit |
| 50 | Provide better guidance on significance thresholds when using gene_set permutation (open, 0 comments) | documentation about FDR interpretation |

Both drafts are therefore **new issues**, not comments on an existing thread; no
"provisional until the lead has read the thread" caveat applies. (Comment bodies cannot be
read from this environment at all — only issue bodies — which is why the table above is
built from titles, bodies and comment counts.)

## Filing order

The cap is two unanswered filings per repository, so they go one at a time.

1. **GS1 first.** It returns a wrong enrichment score — including a sign flip on a real
   ranked list, and an ES outside [−1, 1] on 4.0.3 and 4.1.0, two of the three most-cited
   versions in the survey cohort. One-line fix.
2. **GS2 second**, once GS1 has an answer.

## Contents

| file | what |
|---|---|
| `issue-gs1-weighted-p15-negative-scores.md` | bug report for GS1: code, expected vs got, six-build version table, shell MCVE |
| `issue-gs2-set-size-filter-equal-bounds.md` | bug report for GS2: code, expected vs got, six-build version table, shell MCVE |
| `0001-Fix-weighted_p1.5-hit-weights-for-negatively-scored-.patch` | GS1 fix + `GeneSetScoringTablesTest` (`git am`-able on `dc35c764`) |
| `0002-Apply-the-gene-set-size-filter-when-set_min-equals-s.patch` | GS2 fix + `GeneSetCohortSizeFilterTest` (`git am`-able on `dc35c764`) |
| `pr-bodies.md` | the two PR bodies, `#NNN` placeholder for the issue number |

## Verification status of the patches

Full output in `../verify/unit_tests_before_after.out`. The project has no `test` task, so
each branch was built with its own wrapper (`./gradlew jar`, Gradle 8.2.1, OpenJDK 25.0.4)
and the test classes were compiled against `build/libs/gsea-minimal-user.jar` plus
`modules/` and `lib_test/` and invoked with a small reflective runner.

| build | GeneSetScoringTablesTest | GeneSetCohortSizeFilterTest | XMathTest + VectorTest | total |
|---|---|---|---|---|
| unmodified master `dc35c764` | 2 passed, **2 failed** | 1 passed, **2 failed** | 54 passed | 57 passed, 4 failed |
| + patch 0001 (GS1) | **4 passed** | 1 passed, 2 failed | 54 passed | 59 passed, 2 failed |
| + patch 0002 (GS2) | 2 passed, 2 failed | **3 passed** | 54 passed | 59 passed, 2 failed |

Each patch fixes exactly its own regression tests and leaves the other finding's tests
failing, which is the check that the two are independent.

End-to-end, on the built jars: `../verify/mcve-gs1.out` and
`../verify/gs1_weighted_p15_negative_hits.patched.out` (0 mismatching (scheme, set) pairs
against the reference port after patch 0001, 3 before);
`../verify/mcve-gs2.out` and `../verify/gs2_setmin_eq_setmax_skips_filter.patched.out` (all
five bound pairs report exactly the sets in range after patch 0002, and the run that
aborted now completes).
