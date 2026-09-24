# FastQC — the QC modules whose numbers reach papers

_Read on `s-andrews/FastQC` `master` @ `87fb336` (2026-07-20; VERSION 0.12.1 plus the 2026
commits, unreleased), compiled here with javac, and executed on that build and on the release
archives 0.11.5, 0.11.9 and 0.12.1 (the cohort's three most-cited versions; 0.11.9 alone is
named by 56 papers). Every number below comes from a harness in `../verify/` whose captured
output sits next to it (`.out` for the master build, `.v<version>.out` for the releases,
`.patched.out` for the fix branch)._

Files read: `Modules/BasicStats.java`, `PerBaseQualityScores.java` + `Utilities/QualityCount.java`,
`PerSequenceQualityScores.java`, `PerBaseSequenceContent.java`, `NContent.java`,
`SequenceLengthDistribution.java`, `PerSequenceGCContent.java` + `GCModel/GCModel.java` +
`Statistics/NormalDistribution.java`, `DuplicationLevel.java`, `OverRepresentedSeqs.java`,
`AdapterContent.java`, `Graphs/BaseGroup.java`, `Sequence/QualityEncoding/PhredEncoding.java`,
`Configuration/limits.txt` and `adapter_list.txt`, `FastQCConfig.java`, and the module pages
under `Help/3 Analysis Modules/` as the statement of intended behaviour.

## Findings

### FQ1 — a Phred+33 file whose lowest quality is 31 or more is read as Illumina 1.5, and every quality is reported 31 too low (every version)

`PhredEncoding.getFastQEncodingOffset(char lowestChar)` decides from the lowest quality
character in the file: below `'@'` (64) is Sanger/Illumina 1.9 (offset 33), `'@'` or above is
Illumina 1.3/1.5 (offset 64). A file in the modern encoding whose lowest Phred quality is 31
(`'@'`) or more therefore has offset 64 applied everywhere: Q37 (`'F'`) becomes 6, Q31 becomes 0.
The per-base and per-sequence quality modules, the encoding line in Basic Statistics and their
pass/warn/fail statuses all follow.

`f1_basic_quality_modules.py`, library C (500 reads, qualities drawn from {31, 33, 36, 37},
Phred+33): Basic Statistics `Encoding: Illumina 1.5`, per-base mean at position 1 = 3.22 for a
true 34.3, on 0.11.5, 0.11.9, 0.12.1 and master. Library B (every quality 36) is read the
same way. The module page says "in some very limited datasets it is possible that it will
guess this incorrectly (ironically only when your data is universally very good!)". With
two-colour Illumina instruments emitting four binned qualities (2, 12, 23, 37) and quality
filters that reject any base below Q30, files without a single base under Q31 are no longer
unusual; issue #147 (2025) reported exactly this on a NextSeq 2000 run (every base `'C'`,
Q34) and asked for a way to state the encoding. Whether a fix landed is in the thread (kit
README). Since no Illumina 1.3/1.5 instrument has produced data since 2011 and Phred+33 files
with a lowest character `'@'`–`'J'` are the common case today, the defensible change is to
default to offset 33 unless a character above `'J'` (74, Q41 in Phred+33) is present, or to
add an encoding option.

### FQ2 — the per-read mean quality is truncated toward zero before binning (every version)

`PerSequenceQualityScores.processSequence` sums the quality characters into an `int` and
divides by the read length with integer division (`averageQuality /= qualLen`), so a read
whose mean quality is 27.9 is counted at 27. The histogram "Per sequence quality scores",
the "most frequent mean quality" that its warn (≤ 27) and fail (≤ 20) thresholds test, and
MultiQC's copy of the histogram are all shifted down by up to one unit, on average 0.5.

`f1_basic_quality_modules.py`, library A (2,000 reads, exact mean of the per-read means 30.018):
FastQC's histogram has mean 29.527; every bin equals the count of reads whose floored mean
is that value (2,000 / 2,000) and none equals the rounded means. Same on every build. One-line
fix (`0001-Round-the-per-read-mean-quality-instead-of-truncating.patch`: sum into a `long`,
`Math.round` the mean); on the patched build the histogram equals the rounded means and
its mean is 30.03.

### FQ3 — the Per sequence GC content module uses only the first 100 bases of a 101–199-bp read; the page says "across the whole length of each sequence" (every version)

`PerSequenceGCContent.truncateSequence` cuts each read to the largest multiple of 100 below
its length (multiple of 1,000 beyond 1,000 bp) before counting G and C, to keep the number of
cached `GCModel` objects small. For today's 150-bp reads a third of every read is ignored;
for 250-bp reads a fifth. The module page and the "Basic Statistics" `%GC`, which counts every
base, describe the whole read.

`f2_gc_duplication.py`: 4,000 150-bp reads whose first 100 bases have GC ~N(45 %, 6 %) and
whose last 50 bases are G (the two-colour poly-G artefact): true whole-read GC 63.3 %, GC of
the first 100 bases 44.9 %, FastQC's distribution mean 45.4 %, `%GC` in Basic Statistics 63;
the module's distribution equals a port that truncates to 100 bases (max abs diff 0). Same on
0.11.5, 0.11.9, 0.12.1 and master. On 100-bp reads the port with no truncation matches
exactly. A report; the fix is either the page or the truncation, and the maintainer's call.

### Notes (documented behaviour, recorded for readers of the numbers)

- N1 — Only sequences that first appear among the first 100,000 distinct sequences are tracked
  by the duplication and overrepresented-sequence modules (page says so). `f3`: 3,000 copies
  (2.4 %) of a sequence first seen after 120,000 distinct sequences → no overrepresented row,
  status pass, "Total Deduplicated Percentage" 100.0 for a true 97.56. Files sorted by tile
  or by barcode can put a contaminant late.
- N2 — `%GC` in Basic Statistics is an integer (`(G+C)*100 / (A+C+G+T)` in long arithmetic:
  49.956 % prints as 49); "Mean Length" is `totalBases / count` in integer division (88 for
  88.886).
- N3 — In the grouped per-base quality rows the group mean is the unweighted mean of the
  per-position means and the group percentiles the unweighted mean of per-position
  percentiles over positions with more than 100 observations, not statistics of the pooled
  qualities; `f1` confirms both definitions exactly.
- N4 — `QualityCount.getPercentile` returns the ⌊pN⌋-th smallest value (the conventional
  nearest-rank statistic is the ⌈pN⌉-th); for the thousands of observations per position the
  two coincide (0 of 100 positions differ in `f1`).

## Held up under execution (identical on the four builds)

- **Basic Statistics**: total sequences, sequence length (single value and range), mean and
  median length (0.12.1+; median is the upper median for an even count), `%GC` as the
  integer above.
- **Per base sequence quality** (`--nogroup` and default grouping): mean exact and median /
  quartiles / 10th / 90th equal to the port of `QualityCount.getPercentile` on 100/100
  positions; group labels equal the port of `BaseGroup.makeLinearBaseGroups`; grouped
  values as in N3.
- **Per sequence quality scores**: every bin equals the count of reads with that floored
  mean (FQ2 is the floor, the binning itself is exact).
- **Per base sequence content / N content**: exact to 1e-9 with N excluded from the content
  denominator and included in the N denominator.
- **Sequence Length Distribution**: 46 bins on a 30–120-bp library sum to the read count and
  each bin equals the count in its range.
- **Per sequence GC content**: the 101-bin distribution equals the port of `GCModel`
  (fractional claims of neighbouring percentage bins) on 100-bp reads to 0; the status
  follows the port's modal-normal deviation.
- **Sequence Duplication Levels**: "Total Deduplicated Percentage" and the 16 level bins
  within 0.07 points of the exact values for libraries under the 100,000 limit (0.00), over
  it (250,000 distinct + 20,000 ×2 + 5,000 ×5 + 50 ×500: 80.94 vs 80.90) and heavily
  duplicated (30.00 vs 30.00); the extrapolation from the tracked subset is sound.
- **Adapter Content**: 49 rows × 6 adapters equal the port (cumulative share of reads that
  contain the 12-mer at or before the position, averaged over the group) to 1e-6; statuses
  follow the 5 %/10 % thresholds.
- **Overrepresented sequences**: the planted 0.59 % and 1.23 % sequences (first 50 bases),
  their counts and percentages, nothing else; fail status above 1 %.

Not checked: Per tile sequence quality (needs Illumina read names; no arithmetic beyond a
mean deviation), Kmer Content (off by default), BAM/SAM and nanopore input, CASAVA filtering,
the contaminant search ("Possible Source"), the HTML rendering.
