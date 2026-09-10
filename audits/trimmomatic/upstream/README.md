# Trimmomatic upstream filing kit

_Default branch: **`main`** (PRs and the compare URL go against `main`).
Prepared 2026-09-10 against `usadellab/Trimmomatic` `main` @
**`ef98d6252abeae80cfee36acf9e0e1055097da0b`** ("Merge branch 'V0.41' — release
v0.41", 2026-07-03, version string 0.41). **Nothing has been filed, nothing has
been pushed.** The fix is one commit on the local branch
`fix/palindrome-mismatch-penalty` of the audit clone, `git am`-able from
`0001-Fix-charge-Q-10-per-mismatch-in-ILLUMINACLIP-palindr.patch` against
`ef98d62` (`git apply --check` clean)._

Filing tier: **now** for TC1, and it is the only thing to file. It changes which
reads reach a published count — the forward read is clipped and, under the
default `keepBothReads=false`, the reverse read is dropped — under the exact
option string 15 of the 291 cohort papers quote (`ILLUMINACLIP:...:2:30:10`),
on current `main` and on every release this session could execute. The nine
notes in the review are **held**: four of them are behaviour the project's own
JUnit tests already assert, and the rest are design choices or documentation
gaps, which this project's rules do not file.

Filing order under the two-unanswered-filings cap: **issue first, then the PR
that references it** (the project's issues are answered; there is no
"discussion first" policy to satisfy). Nothing else queued.

## AI-contribution policy check

The audit's own fork convention could not be applied here: there is **no
`cindykrafft/Trimmomatic` fork** (`user:cindykrafft` lists nine repositories,
none of them a Trimmomatic fork), so the
`upstream-declines-ai-contributions` topic could not be read and
`site/audits.json` carries no `declines_ai` entry for this package. Upstream
itself publishes no AI policy: there is no `CONTRIBUTING.md`, no
`CODE_OF_CONDUCT.md`, no pinned policy issue and nothing in `README.md` about
contributions or AI assistance. **Treated as "no stated policy"**, so the kit is
prepared in full — but the attribution footer is left on both texts, and the
patch's commit message carries the `Co-Authored-By:`/`Claude-Session:` trailers,
so the assistance is visible before anything is posted. If the lead can reach
the repository page and finds a policy that says otherwise, do not file.

## What was read before preparing this

The repository has **no contributing document, no issue template, no pull-request
template, no `CODE_OF_CONDUCT.md`, no `.editorconfig` and no linter
configuration**. `.github/` contains only three workflows. What exists, and how
each shaped the kit:

- **`.github/workflows/build-and-test.yml`** — on `push` and `pull_request` to
  `main`: `actions/setup-java@v4` with `java-version: '25'`, distribution
  `temurin`, then `mvn -B clean verify`. So a PR is expected to pass the whole
  JUnit suite on JDK 25 and needs no separate test invocation documented in the
  body. `container-release.yml` and `release.yml` are release plumbing and were
  not touched.
- **`pom.xml`** — `<maven.compiler.release>25</maven.compiler.release>`, JUnit 5
  (`junit-jupiter` 5.11.0) and Mockito 5.15.2 with
  `-Dnet.bytebuddy.experimental=true -XX:+EnableDynamicAgentLoading` in the
  surefire `argLine`. The new test therefore uses `org.junit.jupiter.api.Test`
  and `org.mockito.Mockito.mock(Logger.class)`, exactly as the existing
  `IlluminaPalindrome*Test` classes do. No checkstyle/spotbugs/pmd/spotless
  plugin — there is no linter to run, so `patch_verification.txt` records that
  and the patch follows the file's own style (tabs).
- **`src/test/java/org/usadellab/trimmomatic/trim/`** — 59 test classes (85 in the whole suite), one
  concern per class, named `<Class><Concern>Test`. The new class
  `IlluminaPalindromeMismatchPenaltyTest` follows that convention and sits next
  to `IlluminaPalindromeTest`, `IlluminaPalindromeMinLengthTest` and
  `IlluminaPalindromeOverlapTest`.
- **`versionHistory.txt`** — the project's changelog: one `Version <n>:` heading
  per release, then `Fix:` / `Feature:` / `Performance:` / `Internal:` lines. The
  most recent entry is literally `Version 0.41: Fix: Bug in
  IlluminaClippingTrimmer calculateMaximumRange`, i.e. the maintainers are
  actively fixing this same class, which is worth saying in the thread. The
  patch adds a `Fix:` line under a placeholder `Version 0.42 (unreleased):`
  heading, since 0.41 is released; the PR body says to renumber it.
- **`README.md`** — the manual. `README.md:303` is the sentence the finding is
  measured against ("each matching base adds just over 0.6, while each mismatch
  reduces the alignment score by Q/10"), and `README.md:234–241` is the
  ILLUMINACLIP parameter list. Both are quoted in the issue text.
- **`LICENSE`** (GPLv3) and the licence note at `README.md:309` (the adapter
  sequences are Illumina's, not GPL). The MCVE writes its own two-record FASTA
  containing the stock `PrefixPE` sequences, which are already in the repository
  under `adapters/`; no new adapter data is introduced.

## Prior-report search

Searched `usadellab/Trimmomatic` with `mcp__github__search_issues`, seven
phrasings. **No prior report of this bug exists.** Nearest issues found, none of
which is the same bug:

| query | nearest issues |
|---|---|
| "palindrome mode mismatch penalty integer division quality score ILLUMINACLIP" | **#52** "question about ILLUMINACLIP 2:30:10" (closed, 2 comments) |
| "adapter clipping score Q/10 penalty wrong low quality mismatch not penalised" | *no results* |
| "integer division float rounding bug in trimmer quality calculation" | *no results* |
| "scoring formula documentation discrepancy log likelihood alignment score simple clip threshold" | *no results* |
| "Trimmomatic not removing adapters read-through palindrome fails to clip" | #47, #81, #38, #13 (open); #39 "Overrepresented sequences remain after adapter trimming", #30, #45, #84 (closed) |
| "reverse read dropped unexpectedly keepBothReads short insert palindrome" | **#41** "paired read assignation" (closed, 2 comments), **#56** "Foward only surviving reads but no reverse only surviving and no dropped reads" (closed, 2 comments), #21 "keepBothReads - should it be \"true\" or \"True\"" (closed) |
| "MAXINFO exception crash long reads" | *no results* |

The closest in kind is **#52** — a user asking what `2:30:10` means — and
**#56**, a user surprised by the survival counts of a PE run; neither reports a
scoring error, and neither can be confirmed from here because **comment bodies
cannot be read in this environment** (only issue bodies come back from
`search_issues`). The issue text is therefore drafted as a **new issue**, not as
a comment on an existing thread, so the Round-4 "provisional until the lead has
read the thread" rule does not apply. If the lead reads #52 or #56 and finds
this bug already described there, post the text as a comment there instead.

## Maintainer activity

- Last commit on `main`: **`ef98d62`, 2026-07-03**, by Sebastian Beier
  (the 0.41 release merge) — two months before this audit.
- Highest issue number observed in the searches: **#88**, opened 2026-07-01,
  closed, 2 comments. Issues from 2021 through 2026 appear in the results with
  1–5 comments each, i.e. the tracker is answered.
- **The exact open-issue count could not be obtained.** The GitHub list and
  commit APIs are refused for this repository in this session ("repository
  ... is not configured for this session"); only `search_issues` works, and it
  is a semantic search whose `total_count` is per-query, not a tracker total.
  Of the 19 distinct issues that surfaced across the seven queries, 4 were open
  (#13, #38, #47, #81) and 15 closed — a sample, not a census.
- The project is packaged as a de.NBI / ELIXIR service and ships on both Galaxy
  servers (`README.md` badges), and a 2026 *Bioinformatics* paper accompanies
  0.41, so the project is under active maintenance.

## The kit

| file | what |
|---|---|
| `issue-tc1-palindrome-integer-penalty.md` | the issue text. No issue template exists, so the body is a plain MCVE report: version, reproduction, expected, got, cause with the two lines, how much it matters, and what shrinking the example revealed. First line is `Title: …`. |
| `mcve_tc1_palindrome_penalty.py` | the reproduction as a standalone script — writes its own adapter FASTA and FASTQ, takes a jar path, needs nothing from the audit harness |
| `mcve_outputs.txt` | that script's captured output on the 0.41 release jar, on `main` @ `ef98d62` built from source, on `main` + the patch, and on the 0.39 release jar |
| `0001-Fix-charge-Q-10-per-mismatch-in-ILLUMINACLIP-palindr.patch` | fix + JUnit regression test + `versionHistory.txt` entry, one commit |
| `pr-bodies.md` | the PR body, `#NNN` placeholder for the issue number |
| `patch_verification.txt` | the project's own suite with and without the patch, the new test alone on unmodified `main`, the end-to-end command-line check, and the "no linter" note |

## Before filing

1. Confirm the repository page carries no AI-contribution policy (this session
   cannot load `github.com` HTML).
2. Read #52 and #56 in full; if either already describes this, post as a comment
   there instead of opening a new issue.
3. Open the issue, then the PR referencing it. Replace `#NNN` in `pr-bodies.md`.
4. If the maintainer prefers it, the two-character change can go in without the
   test; but the test is what makes it a regression, so offer it first.
