# STAR upstream filing kit

_Default branch: **`master`** (the 2.7.11b tag is its HEAD, `b1edc12`; PRs go against it).
Prepared 2026-09-13 against `alexdobin/STAR` `master` @ `b1edc12`. **Nothing filed, nothing
pushed.** The fix is one commit, `a0b3f8c`, on the local branch `fix/undefined-strand-transcripts`
of the audit clone, and `git am`-able from
`0001-Treat-transcripts-with-undefined-GTF-strand-.-as-in-.patch` against `b1edc12`
(`git apply --check` clean)._

Filing tier (README step 5): **now** for STA1 + STA2, one issue and one PR — they share a root
cause (a transcript whose GTF strand is `.` is stored as strand 0 and every `trStr==1 ? Str :
1-Str` expression then treats it as `-`), they change numbers that reach papers
(`Aligned.toTranscriptome.out.bam` records for RSEM/salmon, STARsolo count matrices) under
default settings, on the current release and on every release the cohort names, and there is no
prior report. Under the two-unanswered-filings cap this repository gets exactly this issue and
this PR. The notes are **held**.

## What was read before preparing this (step 4 of the method)

- `CONTRIBUTING.md` (adapted from Atom's). Shaped the kit as follows:
  - *Ask a question*: questions go to the [rna-star Google group](https://groups.google.com/forum/#!forum/rna-star),
    not the tracker — the tracker is for bug reports and feature requests; STA1/STA2 are bug
    reports with a reproduction, so the tracker is the right place.
  - *Before submitting*: reproduce on the latest version with mostly default parameters
    (done: `master` = 2.7.11b, defaults except `--quantMode` / `--soloType`), check `Log.out`
    (no ERROR/WARNING for this case), search the tracker (below); if a *closed* issue looks the
    same, open a new one linking it (none found); if an *open* one does, comment there (none).
  - *A good bug report*: clear title; exact commands; copy-pasteable snippets in code blocks;
    observed vs expected behaviour and why; system information (CPU/RAM/storage); whether it
    reproduces reliably; attach `Log.out`. `issue-sta1-undefined-strand.md` follows that order;
    the MCVE (`mcve_st1_transcriptome_strandless.sh`) is self-contained and its output on four
    builds is in `mcve_outputs.txt`.
  - *Pull requests*: descriptive title; state the purpose (bug fix); explain the expected change
    in behaviour and **make sure the default STAR behaviour does not change** — `pr-bodies.md`
    states exactly which outputs change (only transcripts/genes with strand `.`) and that
    everything else is byte-identical in the audit harnesses; detailed commit message and code
    comments (the patch's commit message and in-line comments at each changed line).
- No `.github/` directory: no issue form, no PR template, no CI workflow. `.travis.yml` (legacy)
  only runs `make STAR` with g++; there is no unit-test runner. `extras/tests/scripts/` holds
  awk checkers for STARsolo output, so the regression test is added as a self-contained shell
  script there (`extras/tests/scripts/testUndefinedStrand.sh`, run manually with the STAR
  binary as argument; needs `samtools` for the BAM check).
- `CHANGES.md`: one line per fix under a version heading, in the style
  `* Issue #NNNN: Fixed ...`; the patch adds a `STAR 2.7.11c --- unreleased` heading with one
  bullet (the issue number to be filled in). `RELEASEnotes.md` is the user-facing summary
  and is left to the maintainer.
- `doc/STARmanual.pdf` §7 ("Output in transcript coordinates": the BAM is for RSEM/eXpress;
  default output satisfies RSEM requirements) and §8 (GeneCounts) and `docs/STARsolo.md`
  (`--soloStrand Forward`: "read strand same as the original RNA molecule") as the statement
  of intended behaviour; `Transcriptome_geneCountsAddAlign.cpp:34` ("genes w/o strand will
  accept reads from both strands") as STAR's own convention for `.` genes, which the patch
  extends to STARsolo.
- No `CODE_OF_CONDUCT` constraints beyond the usual; no AI-contribution policy anywhere in the
  tree (`CONTRIBUTING.md`, `README.md`, `CODE_OF_CONDUCT.md` searched). `site/audits.json` in
  this repository has no STAR entry and records no fork of `alexdobin/STAR` under `cindykrafft`;
  GitHub's repository API is not reachable from this session, so the
  `upstream-declines-ai-contributions` topic could not be checked directly.
- Issue tracker searched 2026-09-13 (`search_issues`, five phrasings: "toTranscriptome strand
  flag reversed undefined strand", "TranscriptomeSAM StringTie single-exon transcripts no
  strand reverse complemented RSEM", "quantMode TranscriptomeSAM unstranded transcript strand
  unknown wrong orientation", the two nearest titles re-queried for their bodies): **no prior
  report** of STA1 or STA2. Nearest: #1922 (open, 5 comments, 2023: user mis-entered `+` for
  every strand in a custom GTF and asks how strand is used — a question, not this defect),
  #1880 (open, 5 comments: soft-clipped record in the transcriptome BAM with STARsolo, RSEM
  rejects it — different), #2679 (open, 0 comments, 2026: custom GTF at the mapping step and
  TranscriptomeSAM — different), #735 / #2253 (reads missing from the transcriptome BAM),
  #2020 (feature request: genome-BAM-to-transcriptome-BAM run mode). Comment bodies cannot be
  read from this session; none of these threads needs to be read before filing a *new* issue.
- Matthew Rocklin's "Craft Minimal Bug Reports": the issue's example is generated by the
  script itself (3-kb LCG genome, two identical gene structures, eight 60-mers), ends in the
  expected-vs-got records, and says what shrinking revealed (one `+`/`.` pair is enough; the
  position and CIGAR are right and only flag and sequence differ; the STARsolo counterpart
  shows with the same eight reads).

## Contents

| file | what |
|---|---|
| `issue-sta1-undefined-strand.md` | bug report (STA1 + STA2) in the CONTRIBUTING order: commands, observed, expected, cause, versions, patch offer |
| `mcve_st1_transcriptome_strandless.sh`, `mcve_outputs.txt` | the reproduction embedded in the issue and its output on `master`, 2.7.10a, 2.7.9a and the patched build |
| `0001-Treat-transcripts-with-undefined-GTF-strand-.-as-in-.patch` | fix in five `Transcriptome_*.cpp` files (one line each) + `extras/tests/scripts/testUndefinedStrand.sh` + `CHANGES.md` entry |
| `pr-bodies.md` | PR title and body draft per CONTRIBUTING's PR guidelines |

## Verification status of the patch

STAR has no test suite to run "with and without"; the project builds with `make STAR` (as its
`.travis.yml` does) and the new script is the test.

| tree | `make STAR` | `extras/tests/scripts/testUndefinedStrand.sh` | audit harnesses |
|---|---|---|---|
| unmodified `master` @ `b1edc12` | builds (`STAR --version` 2.7.11b) | **FAIL** (8 transcriptome records differ between the `+` and `.` copy; STARsolo Forward counts 2 of 4 reads of the `.` gene in Gene/GeneFull/GeneFull_ExonOverIntron and 0 in GeneFull_Ex50pAS) | STA1: 600/600 SE and 396/396 PE reads on the `.` transcripts differ; STA2: 8 of 8 feature × gene combinations |
| `master` + patch (`a0b3f8c`) | builds (2.7.11b) | **PASS** | `../verify/*.patched.out`: STA1 0 of 8 records; transcriptome projection 0 of 4,727 SE / 3,069 PE reads differ; STA2 0 of 8; GeneCounts unchanged (0 of 19 rows × 4 configurations) |

No linter or formatter configuration exists in the tree (no `.clang-format`, no lint step);
the changed lines follow the surrounding style.

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| STA1 | `master` = 2.7.11b (`../verify/st1_transcriptome_strandless.out`, `heldup_transcriptome_sam.out`), 2.7.10a (`.v2.7.10a.out`), 2.7.9a (`.v2.7.9a.out`); `mcve_outputs.txt` | patched `a0b3f8c` (`.patched.out`) |
| STA2 | `master`, 2.7.10a (8 of 8), 2.7.9a (4 of 4: Gene, GeneFull — the two other features do not exist there) (`../verify/st2_solo_strandless*.out`) | patched `a0b3f8c` |

## Order of operations

1. Open the issue from `issue-sta1-undefined-strand.md` (paste a fresh run of
   `mcve_st1_transcriptome_strandless.sh`; attach the `Log.out` of the `tr/` run as
   CONTRIBUTING asks).
2. `git am` the patch onto a fresh `master` in a fork, review every line, add the issue number
   to the `CHANGES.md` bullet, push, open the PR against `master` with the body from
   `pr-bodies.md`.
3. Record issue and PR numbers, and every maintainer response, in `../README.md` and the
   top-level status table. The notes stay held until the maintainer responds.
