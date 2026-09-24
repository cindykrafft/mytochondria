# Picard audit against 289 published papers (2021–2026)

_Generated 2026-09-24 against `broadinstitute/picard` `master` @ `c2a483d` (htsjdk 5.0.0), built
here, and the 2.18.7, 2.27.4, 3.0.0 and 3.3.0 release jars. Focus: the tools whose numbers appear in
methods sections and QC tables — `MarkDuplicates`, `CollectInsertSizeMetrics`,
`CollectAlignmentSummaryMetrics`, `CollectWgsMetrics`, `CollectHsMetrics`,
`CollectRnaSeqMetrics`, `CollectGcBiasMetrics` — verified by executing the jars on synthetic BAMs
with independently computed truths._

## What this is

The six-journal survey found **289 papers** in *Nature* (144), PNAS (119), *Cell* (19) and
*Science* (7), 2021–2026, that used Picard; 143 name `MarkDuplicates` and 74 report a duplication
rate (lower bounds, see the profiling caveat). Its metrics and duplicate-marking core was read in
full on `master` and every suspicion was run through five builds on BAMs constructed with pysam
where every flag, CIGAR, base, quality, position and insert size is known and the truth is computed
in Python (an independent duplicate caller with union-find optical clustering and the
Lander–Waterman solver, per-position depth, per-transcript coverage, exact binomial sensitivity).

## Findings (details and line citations in [`component-reviews/metrics-and-duplicates-core.md`](component-reviews/metrics-and-duplicates-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **P1** | **CONFIRMED on `master`, 3.3.0, 3.0.0, 2.27.4 and 2.18.7** | **now** | `CollectRnaSeqMetrics` never counts the last base of any alignment block in per-transcript coverage (`Gene.Transcript.addCoverageCounts` loops `i < genomeEnd` on an inclusive end). Spliced reads' blocks end at exon ends, so the last base of every internal exon has ~0 coverage. A transcript covered by exactly 50 reads at every base reports `MEDIAN_CV_COVERAGE` **0.032** (truth 0) and a normalized coverage of **0.91** at the junction; a realistic 276-gene library shifts `MEDIAN_CV_COVERAGE` 0.430 → 0.436, `MEDIAN_5PRIME_TO_3PRIME_BIAS` 0.466 → 0.468 and the 3′-end point of the coverage curve by −9 %. One-line fix with a regression test on `fix/rnaseq-coverage-last-base`. |
| **P2** | **CONFIRMED on `master`, 3.3.0, 3.0.0, 2.27.4; correct on 2.18.7** | **now** | `CollectHsMetrics` `ZERO_CVG_TARGETS_PCT` counts uncovered targets over the merged (unique) target list but divides by the number of intervals in the file. Since Picard 2.19.0 (htsjdk 2.19.0 stopped uniquing `IntervalList.fromFiles`, samtools/htsjdk#1273) any target file with overlapping intervals understates the fraction: 8 intervals merging to 6 unique targets, 4 uncovered, reports **0.5** for a true 0.667. One-line fix with a test on `fix/hsmetrics-zero-cvg-denominator`. |
| **P3** | **CONFIRMED on `master`, 3.3.0, 3.0.0, 2.27.4 and 2.18.7** | ready (third, after a reply) | `CollectAlignmentSummaryMetrics --IS_BISULFITE_SEQUENCED true` tests the bisulfite match against `refBases[readBaseIndex]`, the contig base at the read's offset, instead of the aligned base. Ten fully converted reads report `PF_MISMATCH_RATE` **0.24** (truth 0) when the contig starts with 100 A's and 0 when it starts with 100 C's; on a human reference whose chromosomes start with N the exclusion never fires. A read with a leading soft clip on a contig shorter than the read crashes with `ArrayIndexOutOfBoundsException`. One-token fix with a test on `fix/alignment-summary-bisulfite-ref-index`. Non-default option; the only way to get these metrics for bisulfite data. |
| P4 | CONFIRMED, every version; prior report #1278 (2019, open, maintainer agreed) | held (comment drafted) | `CollectGcBiasMetrics` looks up the GC window at the 1-based alignment start in a 0-based table (forward reads' windows start one base late) and counts reads whose window runs off the contig end in the GC = 0 bin (101 of 300 reads on a 300-bp contig). Negligible for chromosomes, real for fragmented or transcriptome references. |
| P5 | CONFIRMED, every version; related #787 | held | `BAD_CYCLES` attributes mismatches in a read's second and later alignment blocks to block-relative cycles (`50M1D50M` reads mismatching at cycles 50 and 100 report 1 bad cycle for a true 0). |
| P6 | verified, modelling note | held | `HET_SNP_SENSITIVITY`'s quality sampler returns Q0 after 600 rejections, ~0.9 % of draws when qualities are concentrated: 0.681 vs the exact 0.688 at 4×, 0.9985 vs 0.9987 at 20×. |
| P7 | documented / prior report #1971 | held | `FOLD_80_BASE_PENALTY` undefined when ≥ 20 % of the territory has zero coverage. |

**Held up under execution:** `MarkDuplicates` on 141 read names covering PCR sets, optical chains
and triangles, libraries, soft clips, fragments vs pairs, FR/RF, secondary/supplementary, mate-unmapped
and inter-chromosomal cases, plus a 100-pair hot spot (every flag and all seven metrics, optical
count 59, library size 24); all 20 `CollectInsertSizeMetrics` numbers on three designs;
16 `CollectAlignmentSummaryMetrics` PAIR metrics (non-bisulfite); 16 `CollectWgsMetrics` numbers
and the depth histogram; HsMetrics territory, `PCT_TARGET_BASES_1X` and the on/near/off-bait split.
Not checked: `EstimateLibraryComplexity`'s sequence-based grouping, `MarkDuplicatesWithMateCigar`,
UMI-aware marking, `CollectMultipleMetrics` orchestration, `DownsampleSam`, the VCF tools.

## How the papers use Picard (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| MarkDuplicates named (or duplicates marked/removed) | 143 |
| duplication rate / library complexity reported | 74 |
| RNA-seq | 73 |
| Picard version stated | 66 (2.2.4 ×4; 2.27.4, 2.18.26, 3.1.1, 2.9.4, 2.8.0, 2.23.4, 2.26.10, 2.9.0 ×3 each; families: 2.2x ×41, 2.0x ×28, 2.1x ×17, 1.x ×14, 3.x ×7) |
| variant calling (GATK named 112) | 123 |
| ATAC / ChIP / CUT&RUN / Hi-C | 47 |
| single-cell | 33 |
| mapping rate reported | 16 |
| WES / exome / targeted capture | 14 |
| bisulfite / methylation | 13 |
| MultiQC used | 11 |
| WGS | 10 |
| mean depth / coverage reported | 9 |
| insert size reported | 3 |
| on-target / capture rate reported | 2 |
| `CollectRnaSeqMetrics`, `CollectInsertSizeMetrics`, `CollectWgsMetrics`, `CollectAlignmentSummaryMetrics`, `CollectGcBiasMetrics` spelled out | 1 each |

Exposure by finding: P1 needs `CollectRnaSeqMetrics` (73 papers are RNA-seq; the tool is rarely
spelled out in methods, so 1 is a weak lower bound; MultiQC's RNA-seq report runs it by default);
P2 needs `CollectHsMetrics` on a target file with overlapping intervals (14 exome/targeted papers);
P3 needs the bisulfite flag (13 methylation papers name Picard). `MarkDuplicates`, the tool the
cohort actually names, held up in full.

**Profiling caveat.** As for the earlier audits, this session had no route to Europe PMC, so
`picard_profile.py` ran in `--offline` mode over the survey's stored evidence snippets; every
record in `picard_profiles.jsonl` is `source: survey_cache` and every count above is a lower bound.
Rerun without `--offline` from a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- No `CONTRIBUTING.md`. `.github/PULL_REQUEST_TEMPLATE.md`: a concise descriptive title, the
  changes, the motivation, the issues addressed, and a checklist that must not be deleted (tests
  added or modified, README/docs edited if applicable, all tests passing on GitHub Actions, final
  thumbs-up from a reviewer, rebase/squash/reword as applicable); it links the wiki "Guidelines
  for pull requests". `.github/ISSUE_TEMPLATE.md`: Bug Report with affected tool(s), affected
  version(s), description, steps to reproduce, expected and actual behaviour. No AI-contribution
  policy anywhere in the tree (`README.md`, `.github/`, `build.gradle` searched).
- CI (`.github/workflows/tests.yml`): `./gradlew compileJava` then the TestNG suite on Java 17
  (Temurin), with and without the Barclay tests; R is installed for chart tests. The three fix
  branches each carry a TestNG regression test that fails on `master`; the project's own test
  classes for the touched code were run here on JDK 17 (numbers in [`upstream/README.md`](upstream/README.md)).
- Prior reports searched 2026-09-24 (eight `search_issues` phrasings) and nine threads read in full
  (#1278, #1532, #1522, #1647, #1605, #1971, #787, #1330, #1609): no report of P1, P2 or P3; #1278
  is P4's window off-by-one (acknowledged 2019, unfixed); #1971 is P7; #787 touches P5's histogram.
- Under the two-unanswered-filings cap: P1 and P2 first (default settings, numbers in QC tables),
  P3 as soon as one of them has a reply. **The kit is in [`upstream/`](upstream/)**: three issue
  texts in the template's headings with reproductions that run on the release jars, three
  single-commit branches (fix + regression test) that need a fork of `broadinstitute/picard` to be
  pushed, and the PR bodies in the template's layout.

## Files

| file | what |
|---|---|
| `picard_profile.py`, `picard_profiles.jsonl`, `profile_run.log` | profiling pass over the 289 cohort papers (offline; see caveat) |
| `component-reviews/metrics-and-duplicates-core.md` | the review: P1–P7, held-up list, withdrawn suspicions, semantics notes |
| `verify/_synth.py` | shared helpers: reference FASTA, BAM builder (pysam), Picard runner (new and legacy syntax), metrics-file parser |
| `verify/r1_rnaseq_exon_last_base.py` (+ `.out`, `.v2.18.7.out`, `.v2.27.4.out`, `.v3.0.0.out`, `.v3.3.0.out`, `.patched.out`) | P1: the two-exon uniform-coverage reproduction and the bug model |
| `verify/r1_rnaseq_realistic_library.py` (+ `.out`, `.patched.out`) | P1: 276-gene synthetic library, unmodified vs fixed jar |
| `verify/h1_hsmetrics_zero_cvg_targets.py` (+ same version set) | P2: overlapping targets |
| `verify/a1_alignment_summary_bisulfite.py` (+ same version set) | P3 and P5: bisulfite reference index, the soft-clip crash, BAD_CYCLES |
| `verify/g1_gcbias_window.py` (+ same version set) | P4: window shift and contig-end binning |
| `verify/heldup_markduplicates.py`, `heldup_insert_size.py`, `heldup_wgs_metrics.py` (P6 inside), `heldup_alignment_summary.py` (+ `.out`) | held-up checks against independent truths |
| `upstream/` | filing kit: issue texts, PR bodies, patches, documents read, test numbers |

Harnesses take the Picard jar as their first argument (`python verify/<h>.py /path/to/picard.jar`;
`PICARD_LEGACY=1` in the environment switches to the `ARG=value` syntax of the 2.x jars) and need a
Python ≥ 3.12 venv with `pysam` and `numpy`. Build: `./gradlew shadowJar` with a JDK 17 toolchain
(the audit jar was built with the JDK 21 toolchain by editing `JavaLanguageVersion.of(17)` locally;
the project's tests were run with a Temurin 17 through `-Porg.gradle.java.installations.paths`).

## Next steps

1. Fork `broadinstitute/picard`; push the three branches; file P1 and P2 (issue then PR each), P3
   after a reply; comment on #1278 with the P4 diagnosis when the cap allows.
2. Extend to `EstimateLibraryComplexity` (sequence-based grouping), UMI-aware marking,
   `CollectMultipleMetrics`, and the GATK copies of these collectors.
3. Full-text profiling rerun when Europe PMC is reachable.
