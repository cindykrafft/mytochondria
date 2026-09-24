# Trimmomatic upstream filing kit

Default branch: **`main`** (`usadellab/Trimmomatic`; compare URL base
`https://github.com/usadellab/Trimmomatic/compare/main...`).

_Prepared 2026-09-13 against `usadellab/Trimmomatic` `main` @ `ef98d62` (2026-07-03,
the V0.41 release merge). **TM1 filed 2026-09-24 as issue #90 and PR #91** from `fix/palindrome-mismatch-penalty` on the fork
`cindykrafft/Trimmomatic` (both branches pushed the same evening, unchanged commits; the fork has no
Actions runs, so CI runs only on the upstream PR); the `git am`-able patches are in
this directory:_

| branch | commit | patch | finding |
|---|---|---|---|
| `fix/palindrome-mismatch-penalty` | `71fb53e` on `ef98d62` | `0001-Charge-Q-10-per-mismatch-in-ILLUMINACLIP-palindrome-.patch` | TM1 |
| `fix/maxinfo-normalisation` | `2c78514` on `ef98d62` | `0002-Keep-MAXINFO-score-tables-inside-long-range-for-larg.patch` | TM2 |

Ranking under the two-unanswered-filings cap: **TM1 goes first** (default settings,
silent, every version since 0.32), **TM2 second** (settings the cohort does not use;
loud when it hits — every read to one base). Both are new issues; no comment drafts.

## What was read before preparing this (step 4 of the method)

- `README.md` on `main`, in full: "Running Trimmomatic", "Description of Trimming Steps"
  and "The Adapter Fasta" are the statement of intended behaviour (the score sentence
  "each mismatch reduces the alignment score by Q/10" is what TM1 is measured against; the
  MAXINFO paragraph gives no formula and no bound on `targetLength`). "Build from Source"
  asks for JDK 25 and `mvn clean package`. There is **no CONTRIBUTING file, no issue or
  PR template** (`.github/` holds only `workflows/`), **no code-of-conduct, no linter or
  formatter configuration, no pinned policy issue and no AI-contribution policy**. The
  issue texts therefore follow the README's own order (command, what happened, what was
  expected) as free-form bug reports.
- `.github/workflows/build-and-test.yml`: `mvn -B clean verify` on Temurin JDK 25 for
  every push and PR to `main` — so each patch was verified with the full Maven suite on
  JDK 25 (`patch_verification.txt`). `release.yml`: `mvn -B clean package` on `v*.*` tags,
  attaching `target/Trimmomatic-*.zip`; `container-release.yml` builds the image.
- `versionHistory.txt`: the changelog, one block per version ("Version 0.30: … Fix:
  Correct 'half-window' clipping …"). Its last entry is 0.40; the 0.41 release added
  none, and the next version number is the maintainers' to choose, so the patches carry no
  entry and each PR body offers the line instead.
- `pom.xml`: `maven.compiler.release` 25, JUnit Jupiter 5.11 + Mockito 5.15 for tests,
  surefire 3.3.0, shade plugin for the jar. The tests live in
  `src/test/java/org/usadellab/trimmomatic/trim/`, one small class per concern with
  `makeSequence`/`makeQuality` helpers (e.g. `IlluminaPalindromeTest`,
  `MaximumInformationTrimmerTest`); the two new test classes copy that style.
- The existing tests that touch the same code: `IlluminaPalindromeTest` (a Q40 mismatch,
  penalty 4 under both rules — which is why TM1 was not caught),
  `IlluminaClippingTrimmerScoreTest` (simple mode, Q10 vs Q40), `TrailingTrimmerTest`
  (asserts the 1-base drop of N5), `MaximumInformationTrimmerTest` (targets 150 only).
- Issue tracker searched 2026-09-13 with `mcve_*`-independent phrasings (semantic
  search over `usadellab/Trimmomatic`; comment bodies cannot be read from this session):
  - TM1 — "palindrome mode mismatch penalty quality score integer division" (0 hits),
    "ILLUMINACLIP palindrome clip threshold mismatches quality scoring wrong reverse read
    dropped" (#84, #52, #57, #15, #8, #3), "adapter score log likelihood Q/10 penalty simple
    mode palindrome mode inconsistent" (0), "reverse read dropped unexpectedly palindrome
    keepBothReads forward only surviving" (#56, #15). Nearest: **#52** "question about
    ILLUMINACLIP 2:30:10" (closed, 2 comments), **#16** "keepBothReads: flag or boolean?"
    (closed), #56/#15 (forward-only survivors, questions). No prior report.
  - TM2 — "MAXINFO target length strictness trims reads too short overflow" (#84, #74),
    "MAXINFO long reads 250 300 bp all reads trimmed to 1 base MiSeq" (24 hits, none about
    MAXINFO arithmetic), "MAXINFO all reads dropped surviving one base long reads target
    length" (#84, #51, #56, #15). Nearest: **#74** "About MAXINFO:40:0.8" (closed, 2
    comments), **#22** "SLIDINGWINDOW vs MAXINFO" (closed, 3), **#84** "TrimmomaticPE
    discarding (almost) all reads at Q36" (closed 2025-12-03, a SLIDINGWINDOW question).
    No prior report.
  - Related to note N6 (not filed): **#42** "Quality score autodetection fails for Element
    Biosciences AVITI data" (closed 2026-01-08, 2 comments) is the "Unable to detect
    quality encoding" symptom reproduced in `../verify/heldup_quality_trimmers.out`.
- Maintainer activity, from the tracker: 39 issues in total; the 2021–2024 backlog was
  answered and closed in batches during 2025–2026 (#25, #29, #31 closed 2026-02; #30, #34,
  #37, #40, #62, #88 closed 2026-07), 0.40 was released 2025-08 and 0.41 2026-07 with a
  new Bioinformatics paper — an active, small team.
- Matthew Rocklin's "Craft Minimal Bug Reports" as summarised in the project brief: each
  issue carries a script that makes its own read(s), has no line that is not needed,
  prints expected vs got, and says what shrinking revealed. The scripts are
  `mcve_tm1_palindrome_penalty.py` and `mcve_tm2_maxinfo_target_length.py`;
  `mcve_outputs.txt` is their output on `main`, 0.41 and 0.39.

## Contents

| file | what |
|---|---|
| `issue-tm1-palindrome-mismatch-penalty.md` | bug report: palindrome mismatch penalty truncated to int(Q/10) (MCVE, cause, numbers, fix) |
| `issue-tm2-maxinfo-normalisation.md` | bug report: MAXINFO trims every read to one base for large target lengths |
| `mcve_tm1_palindrome_penalty.py`, `mcve_tm2_maxinfo_target_length.py`, `mcve_outputs.txt` | the reproductions embedded in the issues, and their output on `main`, 0.41 and 0.39 |
| `0001-Charge-Q-10-per-mismatch-in-ILLUMINACLIP-palindrome-.patch` | TM1 fix (two `/ 10` → `/ 10.0f`) + `IlluminaPalindromeMismatchPenaltyTest` (`git am`-able on `ef98d62`) |
| `0002-Keep-MAXINFO-score-tables-inside-long-range-for-larg.patch` | TM2 fix (`Math.min`, `Math.abs`, overflow-safe logistic) + `MaximumInformationTrimmerLargeTargetTest` |
| `pr-bodies.md` | PR titles and bodies |
| `patch_verification.txt` | every Maven run with and without each patch |

## Verification status of the patches

From `patch_verification.txt` (`mvn -o -B`, JDK 25.0.4; the "without" column is the new
test class copied into unmodified `main`):

| patch | new tests on unmodified `main` | new tests with patch | `trim` package with patch | full suite with patch | harness under patch |
|---|---|---|---|---|---|
| 0001 (TM1) | 2 run, **1 failed** (`testTwoMismatchesAtQ19StayBelowThreshold: expected: not <null>`) | 2 pass | 168 pass (166 on `main`) | **261 pass** (259 on `main`) | `../verify/tm1_palindrome_penalty.patched.out`, `version_scope_cli.patched-tm1.out` |
| 0002 (TM2) | 4 run, **3 failed** (`expected: <300> but was: <1>`) | 4 pass | 170 pass | **263 pass** | `../verify/tm2_maxinfo_normalisation.patched.out`, `version_scope_cli.patched-tm2.out` |

`git apply --check` succeeds for each patch and for both together against `ef98d62`
(they touch different files). There is no linter to run.

## Version scope (executed, `../verify/version_scope_cli.*.out`)

| finding | present | absent |
|---|---|---|
| TM1 | `main` (0.41), 0.41, 0.40, 0.39 release, 0.39/0.38/0.36/0.33/0.32 builds — 200/200 pairs clipped where the documented rule clips 0 | — (the integer division is in the 0.32 source; older tags not run) |
| TM2 | the same nine — `MAXINFO:248:0.1`, `250:0.1`, `500:0.2`, `800:0.5` keep 1 base of 300 | — (`MAXINFO:247:0.1` and `40:0.5` keep 300 on all nine) |

0.38, 0.36, 0.33 and 0.32 are builds of the tagged sources (the usadellab.org download
site is unreachable from the session); 0.39, 0.40 and 0.41 are the GitHub release jars.

## Order of operations

1. Open the TM1 issue from `issue-tm1-palindrome-mismatch-penalty.md`; push
   `fix/palindrome-mismatch-penalty` (`git am 0001-*.patch` onto a fresh `main`) to a fork
   and open PR 1 from `pr-bodies.md` with the issue number filled in.
2. After a maintainer signal, the TM2 issue and PR 2 the same way.
3. Record issue and PR numbers, and every maintainer response, in `../README.md` and in
   the top-level status table.
