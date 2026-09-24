# Picard: the metrics and duplicate-marking core, read and executed

_Review of `broadinstitute/picard` `master` @ `c2a483d` (2026-09-24; htsjdk 5.0.0), built here with
Gradle (`shadowJar`, JDK 21 toolchain for the audit jar, JDK 17 for the project's own tests).
Verified by executing the built jar and the 2.18.7, 2.27.4, 3.0.0 and 3.3.0 release jars on synthetic
BAMs written with pysam, where every flag, CIGAR, base, quality, position and insert size is known
and the truth is computed independently in Python. Harnesses and captured output are in
[`../verify/`](../verify/)._

## Scope

The tools whose numbers reach papers, in the order of the cohort's use (profile in
`../picard_profiles.jsonl`, lower bounds from the survey cache): `MarkDuplicates` (143 of 289
papers name it; 74 report a duplication rate), then the QC collectors that MultiQC and pipeline
reports print: `CollectInsertSizeMetrics`, `CollectAlignmentSummaryMetrics`,
`CollectWgsMetrics`, `CollectHsMetrics`, `CollectRnaSeqMetrics`, `CollectGcBiasMetrics`, and the
shared `DuplicationMetrics` library-size estimator. Read in full: `MarkDuplicates.java`,
`AbstractMarkDuplicatesCommandLineProgram.java`, `OpticalDuplicateFinder.java`,
`ReadEndsForMarkDuplicates.java`, `DuplicationMetrics.java`, `InsertSizeMetricsCollector.java`,
`AlignmentSummaryMetricsCollector.java`, `CollectWgsMetrics.java` (+ `AbstractWgsMetricsCollector`,
`FastWgsMetricsCollector`, `WgsMetrics`, `TheoreticalSensitivity`), `TargetMetricsCollector.java`
(+ `HsMetricCollector`, the metric definitions), `GcBiasMetricsCollector.java` + `GcBiasUtils.java`,
`RnaSeqMetricsCollector.java` + `annotation/Gene.java`, and htsjdk's `Histogram`,
`SamPairUtil.getPairOrientation` and `DuplicateScoringStrategy`. Skimmed: `EstimateLibraryComplexity`,
`DownsampleSam`, `MarkDuplicatesWithMateCigar`.

## Findings

### P1 — CollectRnaSeqMetrics drops the last base of every alignment block from transcript coverage (CONFIRMED, every version)

`RnaSeqMetricsCollector.acceptRecord` accumulates per-transcript coverage with

```java
transcript.addCoverageCounts(alignmentBlock.getReferenceStart(),
        CoordMath.getEnd(alignmentBlock.getReferenceStart(), alignmentBlock.getLength()), coverage);
```

`CoordMath.getEnd` returns the **inclusive** last reference base of the block, but
`Gene.Transcript.addCoverageCounts` loops `for (int i = genomeStart; i < genomeEnd; ++i)`, so the
block's last base is never counted. For a spliced read the block ends exactly at the exon end, so
the last base of every internal exon receives coverage only from reads that run unspliced into
the intron; the last base of the transcript is missed by every read that ends there. The affected
outputs are everything derived from `coverageByTranscript`: `MEDIAN_CV_COVERAGE`,
`MEDIAN_5PRIME_BIAS`, `MEDIAN_3PRIME_BIAS`, `MEDIAN_5PRIME_TO_3PRIME_BIAS` and the
`normalized_coverage` histogram that MultiQC plots as the gene-body coverage curve. The base
classification counts (`CODING_BASES`, `PCT_MRNA_BASES`, …) use a different, correct loop.

Executed (`r1_rnaseq_exon_last_base.py`): one two-exon transcript (1001–1500, 3001–3500) covered
by exactly 50 reads at every base. Truth: CV 0, biases 1.0, normalized coverage 1.0 everywhere.
Picard: `MEDIAN_CV_COVERAGE` **0.031639**, normalized coverage **0.91** at the percentile holding
the junction (transcript base 500 has coverage 0), 1.001 elsewhere; the "last base of each block
dropped" model reproduces every number. Same on 2.18.7, 2.27.4, 3.0.0 and 3.3.0. On a realistic
synthetic library (`r1_rnaseq_realistic_library.py`: 276 genes of 2–14 exons, 229k 2×75 fragments
with a 3′-biased profile and Poisson noise) the shift is small but systematic:
`MEDIAN_CV_COVERAGE` 0.4301 → **0.4362**, `MEDIAN_5PRIME_TO_3PRIME_BIAS` 0.4661 → 0.4681,
normalized coverage at position 100 0.058 → 0.053 (−9 %), with the fixed jar reproducing the truth
to six digits. The one-line fix (`i <= genomeEnd`) is on the branch
`fix/rnaseq-coverage-last-base` with a regression test.

### P2 — CollectHsMetrics ZERO_CVG_TARGETS_PCT divides unique targets by the raw interval count (CONFIRMED, regression since 2.19.0)

`TargetMetricsCollector.calculateTargetCoverageMetrics` counts `zeroCoverageTargets` over
`highQualityCoverageByTarget`, whose keys are the **uniqued** targets (overlapping and duplicate
intervals merged), then divides by `allTargets.getIntervals().size()`, the number of intervals
**in the file**. Until Picard 2.18.x the two agreed because htsjdk's `IntervalList.fromFiles()`
returned the union of the input lists; htsjdk 2.19.0 changed it to a plain concatenation
(samtools/htsjdk#1273, "Changed IntervalList fromFiles() so that it doesn't call .unique()",
2019-02-21), and Picard 2.19.0 picked that up. Target files with overlapping intervals — common in
vendor designs where exons of overlapping transcripts are listed separately — therefore
understate the fraction of targets with no coverage by the overlap factor.

Executed (`h1_hsmetrics_zero_cvg_targets.py`): 8 intervals, two overlapping pairs → 6 unique
targets; reads on the two merged targets only. Truth 4/6 = 0.6667. Picard 2.27.4, 3.0.0, 3.3.0 and
master: **0.5**; Picard 2.18.7: 0.6667. `TARGET_TERRITORY` (706, unique bases) and the
`PCT_TARGET_BASES_xX` family use the unique territory and are right. Fix on
`fix/hsmetrics-zero-cvg-denominator` (divide by `highQualityCoverageByTarget.size()`) with a test.

### P3 — CollectAlignmentSummaryMetrics with IS_BISULFITE_SEQUENCED compares against the wrong reference base (CONFIRMED, every version; crash)

`AlignmentSummaryMetricsCollector.collectQualityData`:

```java
boolean mismatch = refBases != null && !SequenceUtil.basesEqual(readBases[readBaseIndex], refBases[refIndex + i]);
final boolean bisulfiteMatch = refBases != null && isBisulfiteSequenced &&
        SequenceUtil.bisulfiteBasesEqual(record.getReadNegativeStrandFlag(), readBases[readBaseIndex], refBases[readBaseIndex]);
```

The bisulfite test indexes the reference with `readBaseIndex` (the base's offset within the read)
instead of `refIndex + i` (the aligned position). A converted base is excused only when the
contig's base at offset *readBaseIndex from the contig start* happens to be C (or G on the
reverse strand), so with `IS_BISULFITE_SEQUENCED=true` the mismatch rates depend on the first
read-length bases of each contig rather than on the alignment. On a human reference the first
10 kb of every chromosome are N, so the exclusion never fires and `PF_MISMATCH_RATE` ≈ the raw
conversion rate. A read with a leading soft clip aligned to a contig shorter than the read
(`40S60M` on a 60-bp contig) reads past the end of the contig's bases and the tool dies with
`ArrayIndexOutOfBoundsException`.

Executed (`a1_alignment_summary_bisulfite.py`): ten fully converted forward reads (240 C→T, no
other difference) at position 1001 of a contig; with bases 1–100 of the contig all A the tool
reports `PF_MISMATCH_RATE` **0.24** in bisulfite mode (truth 0), with bases 1–100 all C it reports
0; the `40S60M` case crashes. Same on 2.18.7 through master. Non-default option
(`IS_BISULFITE_SEQUENCED`), but the only way to get these metrics for bisulfite data. Fix on
`fix/alignment-summary-bisulfite-ref-index` (one token, `refBases[refIndex + i]`) with a test.

### P4 — CollectGcBiasMetrics: forward-read windows shifted by one base, reads near contig ends binned at GC = 0 (CONFIRMED, every version; prior report #1278)

`GcBiasUtils.calculateAllGcs` fills `gc[i]` for 0-based window starts `1 ≤ i < lastWindowStart`
and leaves `gc[0]` and `gc[lastWindowStart..refLength]` at 0. `GcBiasMetricsCollector.addRead`
looks up `gc[pos]` with `pos = rec.getAlignmentStart()` (1-based) for forward reads and
`alignmentEnd − windowSize` for reverse reads, and accepts any value ≥ 0. So (a) a forward read's
window starts one base after its 5′ end while a reverse read's window is exact, and (b) a read
whose window would run off the contig end is counted in the **GC = 0** bin instead of being
skipped. `calculateRefWindowsByGc` skips the first and last windows of every contig the same way.
Issue #1278 (2019, open) reported the skipped windows; the maintainer agreed "there seems to be
an off-by-one bug here" and nothing was changed.

Executed (`g1_gcbias_window.py`): a read starting at base 1 of a contig whose bases 1–100 are A
and base 101 is G lands at GC 1 (documented window: 0 %); on a 300-bp contig with a forward read
at every start, the 101 reads starting at 1-based 200–300 are all counted at GC 0 (`READ_STARTS`
101 at GC 0, 199 at GC 50). Negligible for whole chromosomes (reads within 100 bp of a contig end
are a 10⁻⁶ fraction) but real for fragmented assemblies, transcriptome references and amplicon
panels, where every contig contributes its end reads to the GC-0 bin and to
`AT_DROPOUT`. Held: a comment for #1278 is drafted.

### P5 — CollectAlignmentSummaryMetrics BAD_CYCLES uses the block-relative offset (CONFIRMED, every version)

`collectQualityData` increments the bad-cycle histogram with
`CoordMath.getCycle(negativeStrand, readBases.length, i)` where `i` is the offset **within the
alignment block**, not `readBaseIndex`. For reads with indels or splices, mismatches in the
second and later blocks are attributed to the wrong cycle. Executed: ten `50M1D50M` reads, five
mismatching at cycle 50 and five at cycle 100 → `BAD_CYCLES` **1** (both land on cycle 50; truth
0, no cycle reaches 80 %); the `100M` control gives 0. #787 (2017, open) discusses the same
histogram and the maintainer's wish that the definition read "no-calls **or mismatched the
reference**". Minor (a count of cycles, rarely reported). Held.

### P6 — HET_SNP_SENSITIVITY is slightly low when base qualities are concentrated (verified, modelling note)

`TheoreticalSensitivity.RouletteWheel.draw()` samples base qualities by rejection against
`w / wMax` over all 127 quality bins and returns quality **0** after 600 rejections. With every base
at one quality (binned NovaSeq scores are close to this) the acceptance rate is 1/127 per trial, so
(1 − 1/127)⁶⁰⁰ ≈ 0.9 % of the sampled qualities are 0. Executed (`heldup_wgs_metrics.py`, all
bases Q30, uniform depth): sensitivity 0.6813 vs the exact binomial 0.6875 at 4×, 0.8867 vs 0.8906
at 6×, 0.9630 vs 0.9648 at 8×, 0.9985 vs 0.9987 at 20×; the shortfall is what a 0.88 % rate of
zero draws predicts (0.6809 at 4×). Note only.

### P7 — FOLD_80_BASE_PENALTY is undefined (printed `?`) when 20 % of the territory has zero coverage (documented behaviour; prior report #1971)

`WgsMetrics` and `TargetMetricsCollector` divide the mean by `Histogram.getPercentile(0.2)`; the
20th percentile is 0 whenever ≥ 20 % of bases have no coverage. #1971 (2024, open, assigned)
already argues that the metric should exclude zero-coverage targets as its definition says.
Nothing to add.

## Held up under execution (0 mismatches against the independent truth)

| harness | what was checked |
|---|---|
| `heldup_markduplicates.py` | 277 records / 141 names: PCR duplicate sets of size 1–5 chosen by summed base quality ≥ 15, ties by (tile, x, y); optical chains (0/90/180/270 px, transitive), a 3-read triangle, libraries kept apart, soft-clipped duplicates by unclipped 5′ ends, fragments at a pair's start always duplicates, FR vs RF not duplicates of each other, secondary/supplementary/unmapped never marked, mate-unmapped reads counted as unpaired, inter-chromosomal pairs, a 100-pair hot spot with random tiles: every flag, `UNPAIRED_READS_EXAMINED`, `READ_PAIRS_EXAMINED`, `UNPAIRED_READ_DUPLICATES`, `READ_PAIR_DUPLICATES`, `READ_PAIR_OPTICAL_DUPLICATES` (59), `PERCENT_DUPLICATION`, `ESTIMATED_LIBRARY_SIZE` (Lander–Waterman bisection, 24) |
| `heldup_insert_size.py` | three designs (long right tail of chimeric inserts; even count with a half-integer median; flagged duplicates excluded): `MEDIAN`, `MODE`, `MIN`, `MAX`, `MEDIAN_ABSOLUTE_DEVIATION`, `MEAN` and `STANDARD_DEVIATION` after trimming to MEDIAN + 10·MAD, all eleven `WIDTH_OF_xx_PERCENT`, the histogram |
| `heldup_wgs_metrics.py` | 40 random pairs with Q2/Q10/Q30 bases, MAPQ 5 reads, duplicates, an unpaired read, an overlapping pair, 20 reference N: `GENOME_TERRITORY`, `MEAN`/`SD`/`MEDIAN`/`MAD_COVERAGE`, `PCT_EXC_MAPQ/DUPE/UNPAIRED/BASEQ/OVERLAP/TOTAL`, `PCT_1X/5X/10X`, the depth histogram |
| `heldup_alignment_summary.py` | 35 pairs with mismatches, a deletion, an insertion, hard clips, MAPQ 10 reads, an inter-chromosomal pair, an RF pair, an insert > 100 kb, a QC-fail pair: 16 PAIR-category metrics including `PF_MISMATCH_RATE`, `PF_HQ_ERROR_RATE`, `PF_INDEL_RATE`, `PCT_CHIMERAS`, `STRAND_BALANCE`, `PCT_PF_READS_IMPROPER_PAIRS`, `PCT_HARDCLIP`, `PF_HQ_ALIGNED_Q20_BASES` |
| `h1_hsmetrics_zero_cvg_targets.py` (rest of the output) | `TARGET_TERRITORY`, `PCT_TARGET_BASES_1X`, `ON/NEAR/OFF_BAIT_BASES` with the 250-bp near-bait rule |

## Withdrawn by reading or execution

- `MarkDuplicates` orientation of a pair whose two 5′ ends coincide on opposite strands looked
  order-dependent; the code normalises RF → FR for that case (comment in `buildSortedReadEndLists`)
  and execution agreed.
- The optical-duplicate "fast" path (sets < 3 or < 4 with a keeper) looked non-transitive; for
  the sizes it handles it gives the same clusters as the union-find path (worked through and
  executed on chains and triangles).
- `InsertSizeMetricsCollector`'s `WIDTH_OF_xx_PERCENT` loop with a half-integer median looked as if
  it could double-count the middle bin; it does not (design 2 held up bin by bin).
- `TheoreticalSensitivity.normalizeHistogram` sizes its array by `histogram.size()` and indexes by
  bin id, which would drop mass for a histogram with gaps; every caller passes a histogram
  prefilled contiguously from 0, so it cannot fire.

## Notes on semantics (not bugs)

- `MEAN_INSERT_SIZE` / `STANDARD_DEVIATION` are computed on the histogram trimmed at
  MEDIAN + 10 MAD (one-sided), as documented; MultiQC's "mean" is this core mean.
- `MarkDuplicates` on coordinate-sorted input never marks secondary or supplementary records
  (documented); `samtools markdup -S` and Picard therefore disagree on those records.
- `CollectGcBiasMetrics` and `CollectHsMetrics` both document `AT_DROPOUT` as GC ∈ [0..50] and
  `GC_DROPOUT` as [50..100], but only HsMetrics counts bin 50 in both; GcBias puts it in AT.
- `PF_SELECTED_PAIRS` (behind `HS_LIBRARY_SIZE`) counts a pair as selected when read 1 lies within
  `NEAR_DISTANCE` (250 bp) of a bait, not only on one.
- `PCT_CHIMERAS`' MAPQ gate reads `mateMq == null || (mateMq >= 20 && mq >= 20)`: without an `MQ`
  tag the read's own MAPQ is not checked.
- `CollectRnaSeqMetrics` "top 1000 transcripts" keeps 1001 (`coverages.length − 1001`).
