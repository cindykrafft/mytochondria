# FastQC upstream filing kit

_Default branch: **`master`** (PRs go against it). Prepared 2026-09-24 against
`s-andrews/FastQC` `master` @ `87fb336` (2026-07-20; unreleased commits on top of 0.12.1).
**Nothing filed, nothing pushed.** The FQ2 fix is a single commit on a local branch of the
audit clone, `git am`-able from the patch here against `87fb336`; it needs a fork of
`s-andrews/FastQC` under `cindykrafft` to be pushed._

Filing tier (README step 5): **now** for FQ1 (a report that follows up the closed #147 with a
reproduction and a proposed default) and FQ2 (every version; one-line fix with PR). **FQ3
ready** as the third filing (page or code, the maintainer's call) once FQ1 or FQ2 has a reply,
under the two-unanswered-filings cap. N1–N4 held (N2 is being reworked in PR #205 already).

## What was read before preparing this (step 4 of the method)

- No `CONTRIBUTING` file, no issue or PR template, no AI-contribution policy (`README.md`'s
  "Contributions" section points to the tracker or the author's e-mail; `.github/` holds
  `dependabot.yml` and the `build.yml`/`pr.yml` workflows; confirmed by the helper session on
  the default branch). No test suite in the tree (`test/` holds data); the harness was run on
  the patched build instead (`test-runs.txt`).
- The module pages under `Help/3 Analysis Modules/` for Basic Statistics, per-base and
  per-sequence quality, GC content, duplication, overrepresented sequences and adapter
  content, as the statement of intended behaviour; `Configuration/limits.txt` for the
  thresholds.
- `git log` on the three files: `PhredEncoding.java` and `PerSequenceQualityScores.java`
  unchanged since 2020 apart from a 2026 hot-path edit; `PerSequenceGCContent.java` likewise
  (the truncation predates 0.11.5, executed).
- Issue tracker searched 2026-09-24 (six `search_issues` phrasings) and twelve threads read
  in full through a helper session (artifact "Mytochondria threads fastqc 147 202 153 148 20
  26 93 114 182 168 44 55", which also lists the twelve open PRs and the contribution files):
  **#147 (2025, closed 2026-05-26 without a change) is FQ1's case** — the reporter had a
  NextSeq 2000 file with every base `'C'`; the maintainer answered that the misdetection
  "would only happen if there were no bases anywhere in the file with a Phred score of less
  than 31 (ASCII char < 64) which would be a fairly remarkable dataset unless it's been heavily
  filtered", that there is no option to bypass the detection and he had "never seen a real
  dataset where this was needed". FQ1's text answers that with the filtered-file argument and
  a proposal rather than a request for an option alone. **PR #210** (ewels, open since
  2026-08-13, "Use Phred+33 for BAM/SAM quality encoding rather than guessing from the data")
  removes the guess for BAM/SAM only. **No prior report of FQ2 or FQ3.** #153, #148, #20, #55
  are the maintainer explaining the 50-bp / 100,000-sequence duplication design (N1); #93 is
  the duplication warn threshold vs the tutorial (closed); #114 removed the deduplicated line
  (0.12.0); #182 and #168 are counter overflows fixed in 0.12; #26 is the adapter-content
  row range (12-mer); #202 is the `--min_length` crash (open, owner-filed); #44 empty plots on
  PacBio (open, no comments). **PR #205** (ewels, open) refines the mean/median length output,
  which covers note N2. Twelve PRs are open, seven from 2025–2026, so review is slow.
- `site/audits.json` records no fork of `s-andrews/FastQC` under `cindykrafft`; the
  `upstream-declines-ai-contributions` topic cannot apply.

## Contents

| file | what |
|---|---|
| `issue-fq1-encoding-detection-high-quality.md` | report: the detection rule, the reproduction (all qualities 31–37 → Illumina 1.5, means 31 too low), why filtered files hit it, the proposed default / option, #147 and #210 referenced |
| `issue-fq2-per-sequence-quality-mean-truncated.md` | bug report: the integer division, 2,000-read reproduction (29.53 vs 30.02), the fix |
| `issue-fq3-gc-content-first-100-bases.md` | report: the truncation, the 150-bp poly-G reproduction (45 % vs 63 %), page or code |
| `0001-Round-the-per-read-mean-quality-instead-of-truncatin.patch` | FQ2 fix (`PerSequenceQualityScores.java`), commit bce1b2b on `fix/per-sequence-quality-mean-rounding` |
| `pr-bodies.md` | PR title and body |
| `test-runs.txt` | the harness on the patched build |

## Verification status of the patch

| branch | commit | harness on the patched build |
|---|---|---|
| `fix/per-sequence-quality-mean-rounding` | `bce1b2b` | `../verify/f1_basic_quality_modules.patched.out`: the per-sequence quality histogram equals the rounded per-read means (2,000/2,000 bins), histogram mean 30.017 for an exact 30.018; every other check unchanged (10/12 as on master: FQ1 and the floor check are the two expected differences) |

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| FQ1, FQ3, N1–N4 | 0.11.5, 0.11.9, 0.12.1, `master` | — |
| FQ2 | 0.11.5, 0.11.9, 0.12.1, `master` | patched |

## Order of operations

1. Fork `s-andrews/FastQC`; tell the session; the FQ2 branch is pushed.
2. Open FQ1 from `issue-fq1-encoding-detection-high-quality.md` (a report; no PR until the
   maintainer picks a shape). Open FQ2 from `issue-fq2-per-sequence-quality-mean-truncated.md`,
   then the PR from `fix/per-sequence-quality-mean-rounding` with the body from
   `pr-bodies.md` (issue number in the first line).
3. When one of them has a maintainer reply: FQ3.
4. Record issue and PR numbers and every maintainer response in `../README.md` and the
   top-level status table.
