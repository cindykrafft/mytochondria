"""R1: CollectRnaSeqMetrics transcript coverage drops the last base of every alignment block.

Gene.Transcript.addCoverageCounts(genomeStart, genomeEnd, coverage) loops `i < genomeEnd`, but
RnaSeqMetricsCollector passes CoordMath.getEnd(blockStart, blockLength) = the INCLUSIVE last
reference base of the alignment block. So the last aligned base of every block is never added
to the per-transcript coverage that feeds MEDIAN_CV_COVERAGE, MEDIAN_5PRIME_BIAS,
MEDIAN_3PRIME_BIAS, MEDIAN_5PRIME_TO_3PRIME_BIAS and the normalized_coverage histogram.
For a spliced read the block ends at the exon end, so the last base of every internal exon
gets coverage only from reads that run unspliced into the intron.

Design: one + strand gene, one transcript with two exons (1001-1500, 3001-3500; transcript
length 1000, fully coding). 50-bp single-end reads start at every transcript position from
-49 to 1000 (reads that start before the transcript run unspliced into it, reads crossing the
junction are spliced with an N of 1500), so every transcript base is covered by exactly 50
reads. Truth: coverage 50 everywhere, CV 0, 5'/3' biases 1, normalized coverage 1 at every
percentile. Usage: python r1_rnaseq_exon_last_base.py [picard.jar]
"""
import os, sys, random, statistics
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(1)
L = 10000
ref = rand_seq(rng, L)
fa = write_fasta(os.path.join(d, "ref.fa"), [("chr1", ref)])

# transcript (1-based inclusive genomic): exon1 1001-1500, exon2 3001-3500
exons = [(1001, 1500), (3001, 3500)]
tx_len = sum(e - s + 1 for s, e in exons)
def tx2genome(t):  # transcript coordinate 1..tx_len -> genomic 1-based; t outside -> extrapolate from the nearest exon end
    if t < 1: return exons[0][0] + (t - 1)
    off = 0
    for s, e in exons:
        n = e - s + 1
        if t <= off + n: return s + (t - off - 1)
        off += n
    return exons[-1][1] + (t - tx_len)

with open(os.path.join(d, "genes.refFlat"), "w") as f:
    # geneName name chrom strand txStart(0-based) txEnd cdsStart cdsEnd exonCount exonStarts exonEnds
    f.write("G1\tT1\tchr1\t+\t1000\t3500\t1000\t3500\t2\t1000,3000,\t1500,3500,\n")

RL = 50
recs = []
n = 0
for t in range(-49, tx_len + 1):
    # read covers transcript positions t..t+49 (positions outside the transcript are genomic neighbours of the exon ends)
    gstart = tx2genome(t)
    # build CIGAR: walk transcript positions, split at the junction between transcript base 500 and 501
    a, b = t, t + RL - 1
    if a <= 500 < b:   # spliced
        m1 = 500 - a + 1
        m2 = RL - m1
        cigar = f"{m1}M1500N{m2}M"
    else:
        cigar = f"{RL}M"
    flag = 0 if n % 2 == 0 else 16
    recs.append(simple_read(f"r{n}", gstart - 1, cigar, flag=flag, qual=30))
    n += 1
bam = write_bam(os.path.join(d, "reads.bam"), recs, [("chr1", L)])

# independent truth: per-transcript-base coverage counting every aligned base
cov = [0] * tx_len
for r in recs:
    pos = r["pos"] + 1
    for ln, op in parse_cigar(r["cigar"]):
        if op == "M":
            for g in range(pos, pos + ln):
                # genomic -> transcript coordinate
                off = 0
                for s, e in exons:
                    if s <= g <= e:
                        cov[off + g - s] += 1
                        break
                    off += e - s + 1
            pos += ln
        elif op == "N":
            pos += ln
print(f"truth: transcript bases {tx_len}, coverage min {min(cov)} max {max(cov)} (every base 50 -> CV 0, biases 1.0)")

for strand in ("NONE", "SECOND_READ_TRANSCRIPTION_STRAND"):
    out = os.path.join(d, f"rna_{strand}.txt")
    run("CollectRnaSeqMetrics", "-I", bam, "-O", out, "--REF_FLAT", os.path.join(d, "genes.refFlat"), "--STRAND_SPECIFICITY", strand, "-R", fa)
    m, h = parse_metrics(out)
    m = m[0]
    print(f"\n--- CollectRnaSeqMetrics STRAND={strand}")
    for k in ("PF_ALIGNED_BASES", "CODING_BASES", "INTRONIC_BASES", "INTERGENIC_BASES", "PCT_CODING_BASES", "MEDIAN_CV_COVERAGE", "MEDIAN_5PRIME_BIAS", "MEDIAN_3PRIME_BIAS", "MEDIAN_5PRIME_TO_3PRIME_BIAS"):
        print(f"  {k}: {m[k]}")
    nc = h["All_Reads.normalized_coverage"]
    print("  normalized_coverage at percent 0,1,49,50,51,99,100:", [round(nc[p], 3) for p in (0, 1, 49, 50, 51, 99, 100)])
    low = {p: round(v, 3) for p, v in nc.items() if v < 0.99}
    print("  percentiles with normalized coverage < 0.99:", low)

# expected values if the last base of each block is dropped (bug model), from the truth coverage
bug = cov[:]
for r in recs:
    pos = r["pos"] + 1
    for ln, op in parse_cigar(r["cigar"]):
        if op == "M":
            g = pos + ln - 1  # last base of the block, dropped
            off = 0
            for s, e in exons:
                if s <= g <= e: bug[off + g - s] -= 1; break
                off += e - s + 1
            pos += ln
        elif op == "N": pos += ln
mean = statistics.fmean(bug); sd = statistics.pstdev(bug)
print(f"\nbug model (last block base dropped): coverage at transcript bases 500 and 1000 = {bug[499]}, {bug[999]}; CV = {sd/mean:.4f}; 5'/3' = {statistics.fmean(bug[:100])/statistics.fmean(bug[-100:]):.4f}")
last = len(bug) - 1
for p in (50, 100):
    s = int(max(0, last * (p / 100 - 0.005))); e = int(min(last, last * (p / 100 + 0.005)))
    print(f"  bug model normalized coverage at percent {p}: {statistics.fmean(bug[s:e+1]) / mean:.3f}")
