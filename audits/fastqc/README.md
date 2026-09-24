# FastQC audit against 322 published papers (2021–2026)

_Generated 2026-09-24 against `s-andrews/FastQC` `master` @ `87fb336` (2026-07-20, unreleased
commits on top of 0.12.1) compiled here, and the 0.11.5, 0.11.9 and 0.12.1 release archives.
Focus: the modules whose numbers and pass/warn/fail flags reach papers and MultiQC tables —
Basic Statistics, per-base and per-sequence quality, sequence content, GC content,
duplication, overrepresented sequences, adapter content — verified by running the jar on
FASTQ files built with known qualities, lengths, compositions and duplicate structure._

## What this is

The six-journal survey found **322 papers** in PNAS (173), *Nature* (113), *Cell* (25) and
*Science* (11), 2021–2026, that used FastQC — the survey's most-used quality-control tool,
present before nearly every trimming step (Trimmomatic 77, Cutadapt 72, Trim Galore 59,
fastp 16 co-uses) and aggregated by MultiQC in 44. The module code was read on `master` and
every number was recomputed from the input in Python: exact per-position statistics, ports of
the percentile, base-grouping, GC-model and adapter-counting routines, and exact duplicate
structure.

## Findings (details and line citations in [`component-reviews/qc-modules.md`](component-reviews/qc-modules.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **FQ1** | **CONFIRMED on 0.11.5, 0.11.9, 0.12.1 and `master`**; prior report #147 (2025, closed) | now (report; fix shape depends on the thread) | A Phred+33 file whose lowest quality is 31 (`'@'`) or more is read as Illumina 1.5: every quality is reported 31 too low (Q37 → 6), the encoding line says Illumina 1.5, and the quality modules' statuses follow. Two-colour instruments with binned qualities plus a Q30 filter produce such files; the module page admits the guess can be wrong "only when your data is universally very good". |
| **FQ2** | **CONFIRMED on all four builds** | now (one-line fix) | The per-read mean quality is truncated toward zero before binning (`averageQuality /= qualLen` in integer arithmetic): the "Per sequence quality scores" histogram, its most-frequent value that the ≤ 27 / ≤ 20 thresholds test, and MultiQC's copy sit 0.5 too low on average (2,000 reads: histogram mean 29.53 for a true 30.02). |
| **FQ3** | **CONFIRMED on all four builds** | now (report: page or code) | "Per sequence GC content" counts only the first 100 bases of a 101–199-bp read (the first 200 of 200–999): a third of every 150-bp read is ignored while the page says "across the whole length of each sequence" and Basic Statistics' `%GC` counts every base. 150-bp reads with a poly-G tail: whole-read GC 63.3 %, FastQC's distribution mean 45.4 %, `%GC` 63. |
| N1 | note, documented | held | Only sequences first seen among the first 100,000 distinct sequences are tracked: a 2.4 % contaminant first appearing later is invisible to the overrepresented and duplication modules (deduplicated percentage 100.0 for a true 97.6). |
| N2 | note, documented | held | `%GC` and "Mean Length" in Basic Statistics are integers by truncation (49.956 → 49; 88.886 → 88). |
| N3 | note, verified | held | Grouped per-base quality rows are unweighted means of per-position means and percentiles (positions with ≤ 100 observations excluded from the percentiles). |
| N4 | note, verified | held | Percentiles are the ⌊pN⌋-th smallest value; indistinguishable from the nearest-rank value at the read counts involved. |

**Held up under execution:** Basic Statistics; per-base quality mean and percentiles
(`--nogroup` and default grouping, labels from a port of the grouping); the per-sequence
quality bins as floors; per-base content and N content (exact); sequence length distribution;
the GC distribution against a port of `GCModel` and its modal-normal status; the duplication
estimator ("Total Deduplicated Percentage" and level bins within 0.07 points of the truth
under, over and far over the 100,000-sequence limit); adapter content against a port of the
cumulative count; overrepresented counts, percentages and thresholds. Not checked: per-tile
quality, Kmer content, BAM/nanopore input, CASAVA filtering, contaminant matching.

## How the papers use FastQC (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 85 (0.11.9 ×56, 0.11.8 ×30, 0.11.5 ×22, 0.12.1 ×13, 0.11.7 ×11) |
| adapters / adapter content named | 90 |
| duplication named | 68 |
| MultiQC also used | 44 |
| trimmer named: Trimmomatic 77, Cutadapt 72, Trim Galore 59, fastp 16 | |
| reads filtered or removed after QC | 45 |
| Q20/Q30/Phred threshold quoted | 11 |
| assay: RNA-seq 109, single-cell 34, ATAC/ChIP/CUT&RUN 26, metagenomics/16S 14, WGS/WES/amplicon 13, long reads 7 | |
| aligner downstream: STAR 92, Bowtie 2 79, BWA 46, HISAT2 35 | |

FastQC's role in the papers is a gate ("reads passed FastQC", "quality was checked with
FastQC") more often than a number: the per-sequence quality histogram, the encoding line and
the GC module's status are what FQ1–FQ3 change; a file mis-read as Illumina 1.5 (FQ1) turns
every quality module red and is the one finding that would visibly stop a pipeline.

The profile (`fastqc_profile.py`, `fastqc_profiles.jsonl`, `profile_run.log`) was run offline
against the survey's stored evidence sentences, so every count is a lower bound.

## Filing channel

`s-andrews/FastQC` has no `CONTRIBUTING` file and no issue or PR template (`README.md`
"Contributions" points to the issue tracker; `.github/` holds `dependabot.yml` and the
workflows). Bug reports go to the GitHub tracker. The helper session's artifact records the
open pull requests and the contribution files. Kit under [`upstream/`](upstream/): three issue
texts (FQ1–FQ3), one PR body with a `git am`-able patch (FQ2), test notes. No fork of
`s-andrews/FastQC` exists under `cindykrafft` yet.

## Files

| path | what |
|---|---|
| `component-reviews/qc-modules.md` | the review: FQ1–FQ3, N1–N4 with code citations, held-up list |
| `verify/_synth.py` | FASTQ writers, the headless FastQC runner (system properties as the wrapper sets them), `fastqc_data.txt` parser, ports of the base grouping and the percentile routine |
| `verify/f1_basic_quality_modules.py` | Basic Statistics, per-base and per-sequence quality, content, N, length, encoding (FQ1, FQ2, N2–N4) |
| `verify/f2_gc_duplication.py` | GC distribution port and the 150-bp truncation (FQ3); duplication estimator under/over the limit |
| `verify/f3_overrepresented_adapters.py` | overrepresented counts and thresholds, the late-contaminant limit (N1), adapter content port |
| `verify/*.out`, `*.v<version>.out`, `*.patched.out` | captured output per build |
| `fastqc_profile.py`, `fastqc_profiles.jsonl`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit |

## Next steps

1. Fork `s-andrews/FastQC`; the FQ2 branch is pushed.
2. FQ1 as a report referencing #147 (with the encoding-default proposal), FQ2 as issue + PR.
3. FQ3 once one of them has a reply.
