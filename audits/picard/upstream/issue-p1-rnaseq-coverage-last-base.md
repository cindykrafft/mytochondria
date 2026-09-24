Title: CollectRnaSeqMetrics never counts the last base of an alignment block in transcript coverage (MEDIAN_CV_COVERAGE, 5'/3' bias, normalized_coverage histogram)

<!-- broadinstitute/picard .github/ISSUE_TEMPLATE.md, Bug Report block. The template header asks for a support-forum post first; this is a reproducible bug with a fix, so it goes straight to the tracker as #1971 and #1522 did. -->

## Bug Report

### Affected tool(s)
CollectRnaSeqMetrics (and CollectMultipleMetrics with PROGRAM=RnaSeqMetrics): `MEDIAN_CV_COVERAGE`, `MEDIAN_5PRIME_BIAS`, `MEDIAN_3PRIME_BIAS`, `MEDIAN_5PRIME_TO_3PRIME_BIAS` and the `normalized_coverage` histogram.

### Affected version(s)
- [x] Latest public release version [3.3.0; also 3.0.0, 2.27.4 and 2.18.7]
- [x] Latest development/master branch as of [2026-09-24, c2a483d]

### Description

`RnaSeqMetricsCollector` accumulates per-transcript coverage with

```java
transcript.addCoverageCounts(alignmentBlock.getReferenceStart(),
        CoordMath.getEnd(alignmentBlock.getReferenceStart(), alignmentBlock.getLength()), coverage);
```

`CoordMath.getEnd` returns the inclusive last reference base of the block, but `Gene.Transcript.addCoverageCounts` loops

```java
for (int i=genomeStart; i<genomeEnd; ++i) {
```

so the last aligned base of every block is never added. For a spliced read the block ends exactly at the exon end, so the last base of every internal exon only gets coverage from reads that run unspliced into the intron, and the last base of the transcript is missed by every read that ends there. Everything derived from `coverageByTranscript` inherits this: the CV, the 5' and 3' biases and the normalized coverage curve. The base classification counts (`CODING_BASES`, `PCT_MRNA_BASES`, ...) use a different loop and are unaffected.

#### Steps to reproduce

A + strand transcript with two exons (chr1:1001-1500 and chr1:3001-3500, fully coding) and 50-bp reads starting at every transcript position from -49 to 1000, spliced with `1500N` where they cross the junction, so that every one of the 1000 transcript bases is covered by exactly 50 reads:

```sh
# refFlat: geneName name chrom strand txStart txEnd cdsStart cdsEnd exonCount exonStarts exonEnds (0-based starts)
printf 'G1\tT1\tchr1\t+\t1000\t3500\t1000\t3500\t2\t1000,3000,\t1500,3500,\n' > genes.refFlat
python3 - <<'EOF'
A = "A"*50; Q = "I"*50
print("@HD\tVN:1.4\tSO:coordinate\n@SQ\tSN:chr1\tLN:10000", end="")
n = 0
for t in range(-49, 1001):                       # transcript position of the read's first base
    last = t + 49
    start = 1001 + t - 1 if t <= 500 else 3001 + t - 501
    cigar = f"{500 - t + 1}M1500N{50 - (500 - t + 1)}M" if t <= 500 < last else "50M"
    print(f"\nr{n}\t{0 if n % 2 == 0 else 16}\tchr1\t{start}\t60\t{cigar}\t*\t0\t0\t{A}\t{Q}", end=""); n += 1
EOF
) > reads.sam
java -jar picard.jar SortSam -I reads.sam -O reads.bam -SO coordinate
java -jar picard.jar CollectRnaSeqMetrics -I reads.bam -O rna.txt --REF_FLAT genes.refFlat --STRAND_SPECIFICITY NONE
grep -A2 "^## METRICS" rna.txt | cut -f 17-20       # MEDIAN_CV_COVERAGE MEDIAN_5PRIME_BIAS MEDIAN_3PRIME_BIAS MEDIAN_5PRIME_TO_3PRIME_BIAS
awk '$1==50' rna.txt                                 # normalized coverage at the percentile holding the junction
```

(The stand-alone script `r1_rnaseq_exon_last_base.py` in the linked repository builds the same input with pysam and prints the truth next to Picard's numbers on 2.18.7, 2.27.4, 3.0.0, 3.3.0 and master.)

#### Expected behavior

Every transcript base has coverage 50, so `MEDIAN_CV_COVERAGE` 0, all three bias metrics 1.0, and `normalized_coverage` 1.0 at every percentile.

#### Actual behavior

```
MEDIAN_CV_COVERAGE 0.031639   MEDIAN_5PRIME_BIAS 1.001001   MEDIAN_3PRIME_BIAS 1.001001   MEDIAN_5PRIME_TO_3PRIME_BIAS 1
normalized_position 50   All_Reads.normalized_coverage 0.91
```

Transcript base 500 (the last base of exon 1) has coverage 0: all 50 reads covering it are spliced and their first block ends at chr1:1500. The same run on 2.18.7, 2.27.4, 3.0.0 and 3.3.0 gives the same numbers. Modelling "drop the last base of every block" in Python reproduces every figure (CV 0.0316, 0.910 at percentile 50).

On a more realistic synthetic library (276 genes of 2-14 exons, 229k 2x75 fragments with a 3'-biased profile and Poisson noise) the effect is small but systematic: `MEDIAN_CV_COVERAGE` 0.4301 -> 0.4362, `MEDIAN_5PRIME_TO_3PRIME_BIAS` 0.4661 -> 0.4681, and the last point of the normalized coverage curve 0.058 -> 0.053; with the fix below Picard reproduces the independently computed values to six digits.

**Fix:** change the loop to `i <= genomeEnd` (the only caller passes an inclusive end). A PR with that change and a regression test (the two-exon transcript above, which fails on `master`) follows.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/picard)

---
_Generated by [Claude Code](https://claude.ai/code)_
