# STAR audit against 489 published papers (2021–2026)

_Generated 2026-09-10 against `alexdobin/STAR` `master` @ `b1edc12` — which is also the
tag `2.7.11b`, the latest release — built from `source/` with `make STAR` (g++ 13.3.0,
zlib, bundled htslib). Focus: the outputs whose numbers reach methods sections and
supplementary tables — `ReadsPerGene.out.tab`, `Aligned.toTranscriptome.out.bam`,
`SJ.out.tab`, the SAM tags and MAPQ, `Log.final.out`, and the STARsolo count matrices —
verified by executing the built binaries on a synthetic genome, annotation and read set
whose truth is known, against independent Python reimplementations._

## What this is

The six-journal survey found **489 papers** in *Nature*, PNAS, *Cell* and *Science*,
2021–2026, that used STAR — the standard RNA-seq aligner, and the source of the count
matrix that the 267 DESeq2 papers and the 70 edgeR papers in the same cohort then
analyse. Its quantification core was read in full on `master` and every suspicion was run
through three builds: `master`/2.7.11b (built here), and **2.7.10a** and **2.7.9a** built
from their release tags — the cohort's first and third most-cited versions — on a
fixed-seed synthetic genome with 14 genes on both strands (overlapping genes, an
antisense gene, two isoforms, genes inside 2-, 3- and 12-copy repeats, one gene with no
annotated strand, six planted intron motifs plus non-canonical) and reads simulated from
the transcripts, where the truth is computed in Python (an HTSeq-union gene counter, a
junction extractor with STAR's documented `--outSJfilter*` rules, a transcriptome
projector, and a recomputation of `NH`/`HI`/`AS`/`nM`/`NM`/`MD`/`jM`/`jI`/MAPQ/`XS` and
of all 27 `Log.final.out` statistics).

## Findings (details and line citations in [`component-reviews/quantification-core.md`](component-reviews/quantification-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **ST1** | **CONFIRMED on `master`/2.7.11b, 2.7.10a and 2.7.9a** | **now** | A GTF feature whose strand column is `.` gets strand code 0 (`GTF.cpp:138-143`); `--quantMode GeneCounts` handles code 0 deliberately (`Transcriptome_geneCountsAddAlign.cpp:34`: "genes w/o strand will accept reads from both strands"), but four other paths test only for code 1 and treat code 0 as the minus strand. In `Aligned.toTranscriptome.out.bam` the coordinates are transformed as if the transcript were `+` while the `0x10` flag is set as if it were `-` (`Transcriptome_quantAlign.cpp:107`), so **every** record is internally inconsistent: mapping the same reads against two GTFs that differ only in the strand column gives the same 20 positions with **all 20 strand flags flipped** and **1,524** SEQ-vs-transcript mismatches where the `+` annotation has **0** (paired-end: 36 records, 36 flipped, 2,018 vs 0). `RSEM --forward-prob 1` keeps 10 of the 20 reads either way — on the `.` annotation, the antisense ten. STARsolo `--soloStrand Forward` gives the gene **0** `Gene` and **0** `GeneFull` UMIs against **40 / 40** on the `+` annotation (`Unstranded`: 40 / 40 both). In the full synthetic annotation, **400 of 11,189** single-end transcriptome records differ from the independent port and every one is a strand flag on the strandless transcript (800 of 20,748 paired-end). Silent: no warning, no `Log.out` line. |
| N1 | note, verified, design | held | The default `--quantTranscriptomeSAMoutput BanSingleEnd BanIndels ExtendSoftclip` drops reads whose soft clips cannot be extended, uncounted: of the simulated reads with a true junction overhang of 1–2 nt, **9 of 40** reach the transcriptome BAM by default against 40 with soft clips allowed; over the whole run **9,547** vs **9,797** single-end reads (250, or 2.4 % of the 10,299 genome-mapped reads), 9,441 vs 9,595 paired-end. Documented as an RSEM-compatibility design; the manual does not say that extension can fail. |
| N2 | note, verified, documentation | held | `ReadsPerGene.out.tab`'s `N_unmapped` includes reads mapped to too many loci: **501 = 201 + 300** where `Log.final.out` reports 201 unmapped and 300 "too many loci"; with `--outFilterMultimapNmax 2`, **1,017 = 201 + 816**. The manual documents the four columns, not the `N_*` rows. |
| N3 | note, verified on 2.7.9a, fixed at master | held | 2.7.9a writes transcriptome records for reads it had itself discarded as mapping to too many loci: **11,489** records for **9,847** reads where the port has 11,189 / 9,547, the 300 extra reads all on the transcript inside the 12-copy repeat (598 extra paired-end records). Fixed at 2.7.10a and recorded in `CHANGES.md`; noted because **24 cohort papers name 2.7.9a**. |

Five own suspicions were withdrawn by execution (`--outSAMstrandField intronMotif` XS
inference; the MAPQ 255/3/1/0 boundary against `NH`; the 2-pass `annotated` column, which
does change meaning but is documented; non-deterministic primary-alignment choice among
equal-score multimappers; `Log.final.out` denominators) and are recorded in the review.

**Held up under execution** (identical output on all three builds unless N3 says
otherwise): all 18 rows of `ReadsPerGene.out.tab` in all three strandedness columns
against an HTSeq-union port on three runs — **0 rows differing** each time — covering
multimappers, the overlapping and antisense gene pairs producing 1,143 ambiguous
single-end reads unstranded but 278/276 stranded, two isoforms of one gene, and columns
summing to the 10,800 input reads; the stranded columns against the simulation truth
(2,687 sense reads to column 3 and 2,587 antisense to column 4 for `+` genes, 985/974 for
`-`); **all 9 columns of every `SJ.out.tab` row** on eight runs (single- and paired-end,
with and without a GTF, 2-pass with and without a GTF, `--outFilterType BySJout`,
unique-reads-only), including the `--outSJfilter*` defaults, which account for every one
of the 17 removed junctions, all 17 true junctions recovered, and 0 of 1,371 BAM junction
crossings missing from `SJ.out.tab` under `BySJout`; every field of every one of 11,639
single-end and 10,768 paired-end alignment records — `NH`, `HI`, MAPQ, `nM`, `NM`, `MD`,
`AS` (with the annotated-junction bonus, the motif penalties, the indel penalty and the
genomic-span log term), `jM`/`jI`, pair flags, TLEN, `XS` on 1,350 spliced records, and
exactly one maximal-`AS` primary per read — **discrepancies: none**; the coordinate-sorted
BAM as a permutation of the unsorted one; `--outFilterMultimapNmax` moving exactly the
right reads (823 → 307 multi, 300 → 816 too-many-loci, unique unchanged); and **all 27
`Log.final.out` statistics, 0 differing** on three runs with the denominators checked.
Not checked: chimeric/fusion detection, the splice-graph path, diploid/WASP, UMI
collapsing and cell filtering, read clipping, `STARlong`, and the seeding-and-stitching
search itself (read, but not reimplemented — the audit tests what STAR reports about the
alignments it found, not that it found the best ones).

## How the papers use STAR (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| STAR named | 488 |
| DESeq2 / edgeR / limma downstream | 327 |
| genome build stated | 322 |
| STAR version stated | 151 (2.7.10a ×26, 2.5.2b ×25, 2.7.9a ×24, 2.7.3a ×20, 2.6.1d ×13) |
| samtools also used | 121 |
| single-cell / snRNA | 113 |
| featureCounts also used | 111 |
| RNA-SeQC / MultiQC / QC | 98 |
| Picard / duplicates | 95 |
| GENCODE / Ensembl annotation | 86 |
| HTSeq also used | 67 |
| RSEM also used | 60 |
| paired-end | 47 |
| 2-pass mode | 28 |
| Salmon / kallisto also used | 23 |
| StringTie / Cufflinks assembly | 23 |
| `--outFilterMultimapNmax` stated | 23 (values: 1 ×8, 20 ×4, 10 ×2, 1000 ×2, 100 ×2) |
| long reads | 18 |
| ENCODE options | 12 |
| chimeric / fusion | 11 |
| `SJ.out.tab` / novel junctions | 9 |
| RefSeq annotation | 8 |
| rMATS / splicing analysis | 8 |
| STARsolo | 7 |
| multimapper handling stated | 7 |
| unique mapping rate reported | 7 |
| `GeneCounts` / `ReadsPerGene` | 5 |
| `TranscriptomeSAM` / transcriptome BAM | 4 |
| `--sjdbOverhang` stated | 4 |
| `--outSAMstrandField` / XS | 3 |

Exposure by finding: **ST1** needs an annotation with `.` in the strand column *and* one
of the two affected outputs — `--quantMode TranscriptomeSAM` (4 papers name it, 60 name
RSEM, 23 name Salmon or kallisto) or stranded STARsolo (7 papers; 113 are single-cell).
GENCODE, Ensembl and RefSeq give every feature a strand, so the 94 papers that name one
of those are not exposed through it; the papers at risk are those that add custom
features (repeats and TEs, ncRNA and enhancer catalogues, BED-derived or GFF3-converted
annotations, viral and organelle sequences), which the survey cache cannot detect at all.
**The exposure count for ST1 is therefore unknown, not small** — the profile can see
which outputs a paper names, not what is in its GTF's seventh column. N3 is bounded: 24
papers name 2.7.9a. N1 and N2 are documentation about documented designs.

**Profiling caveat.** As for the Seurat, Scanpy, Cutadapt and SAMtools audits, this
session had no route to Europe PMC (`www.ebi.ac.uk` denied by the session's egress
policy; NCBI likewise), so `star_profile.py` ran in `--offline` mode over the survey's
stored evidence snippets; every record in `star_profiles.jsonl` is `source: survey_cache`
and every count above is a lower bound. Rerun without `--offline` from a host with Europe
PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- `CONTRIBUTING.md` is the only contribution document: questions go to the
  [rna-star Google group](https://groups.google.com/forum/#!forum/rna-star), **not** the
  tracker; bug reports need the exact command, copy-pasteable snippets, `Log.out`, the
  observed and the expected behaviour, system information, and a statement of whether it
  reproduces reliably; PRs need a clear title, a stated purpose, a guarantee that
  **default STAR behaviour does not change**, and detailed commit messages. No AI policy,
  no DCO, no sign-off requirement.
- **No issue template, no PR template, no `.github/` directory, no CI, and no test
  suite** — `extras/tests/scripts/` holds three `awk` checkers for STARsolo
  `CellReads.stats` and nothing that runs them. So "the project's own tests for the
  touched module" do not exist; the patch adds the first executable regression test in
  the tree. It reports **2 FAIL / exit 1** on unpatched `master` and **2 PASS / exit 0**
  with the patch.
- `CHANGES.md` carries `* Issue #NNNN: Fixed …` bullets under a version heading; the
  patch adds a `STAR 2.7.11c --- unreleased` heading with one.
- ST1 is the only "file now" item; the tracker was searched with five phrasings on
  2026-09-10 and holds no prior report (nearest: **#1922**, a user whose custom GTF lost
  its strand information, 5 comments — the same situation, a different bug, so a new
  issue rather than a comment). **The kit is in [`upstream/`](upstream/)**: the issue text
  in `CONTRIBUTING.md`'s bug-report order with a 40-line self-contained MCVE (run on
  2.7.11b, 2.7.10a, 2.7.9a and the patched build), one `git am`-able patch (six one-line
  conditions in five files + the regression test + the `CHANGES.md` entry), and the PR
  body draft. The filing cap is two unanswered filings per repository; the issue goes
  first, and the PR is offered in its last line rather than opened unsolicited.
- The audit's fork `github.com/cindykrafft/STAR` could not be resolved from this session,
  so the `upstream-declines-ai-contributions` topic could not be checked — the lead
  should re-check it before sending anything. Nothing in `alexdobin/STAR` declines AI
  contributions.

## Files

| file | what |
|---|---|
| `star_profile.py`, `star_profiles.jsonl`, `profile_run.log` | profiling pass over the 489 cohort papers (offline; see caveat) |
| `component-reviews/quantification-core.md` | the review: ST1, N1–N3, five withdrawn suspicions, held-up list, not-audited list |
| `verify/_synth.py` | shared synthetic genome / GTF / read simulator, STAR runner and truth tables |
| `verify/st1_trsam_strandless_transcript.py` (+ `.out`, `.v2.7.10a.out`, `.v2.7.9a.out`, `.patched.out`) | ST1: the same reads against `+` and `.` annotations — transcriptome records and STARsolo counts |
| `verify/heldup_genecounts.py` (+ `.out`, `.v2.7.10a.out`, `.v2.7.9a.out`) | held-up: `ReadsPerGene.out.tab` vs an HTSeq-union port and vs the simulation truth, 3 runs |
| `verify/heldup_sjout.py` (+ same set) | held-up: `SJ.out.tab` on 8 runs, the `--outSJfilter*` accounting, 2-pass insertion, `BySJout` |
| `verify/heldup_sam_tags.py` (+ same set) | held-up: `NH`/`HI`/MAPQ/`AS`/`nM`/`NM`/`MD`/`jM`/`jI`/`XS`, primary choice, sorted-BAM order |
| `verify/heldup_logfinal.py` (+ same set) | held-up: all 27 `Log.final.out` statistics and their denominators, 3 runs |
| `verify/heldup_transcriptome.py` (+ same set) | held-up: transcriptome records vs an independent projector; N1's soft-clip accounting; N3 on 2.7.9a |
| `upstream/` | filing kit: issue text, MCVE + outputs on four builds, patch 0001, PR body, documents read, test numbers |

Harnesses take the STAR binary as their first argument and an optional working directory
(`python verify/<h>.py /path/to/STAR /path/to/workdir`) and need a Python ≥ 3.12 venv with
`pysam` and `numpy` (`uv venv --python /usr/bin/python3.12 venv && uv pip install pysam
numpy`). Builds: `git clone https://github.com/alexdobin/STAR`, then `make STAR` in
`source/` (gcc/g++, zlib; the bundled htslib builds with it); the release tags build the
same way.

## Next steps

1. File ST1: the issue first (`upstream/issue-st1-strandless-transcript-strand.md`), and
   open the PR from `fix/strandless-transcript-strand` only once a maintainer responds, as
   the issue's last line offers. Re-check the fork's topics first.
2. Extend the review to the paths not audited — chimeric detection (11 cohort papers name
   fusions), STARsolo UMI collapsing and `EmptyDrops_CR` filtering (113 papers are
   single-cell), and `--soloFeatures Velocyto`.
3. Full-text profiling rerun when Europe PMC is reachable, to find which papers built a
   custom GTF and so bound ST1's exposure with a number instead of an argument.
