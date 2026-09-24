"""A1/A2: CollectAlignmentSummaryMetrics with IS_BISULFITE_SEQUENCED, and BAD_CYCLES with indels.

A1. AlignmentSummaryMetricsCollector.collectQualityData tests
    SequenceUtil.bisulfiteBasesEqual(negStrand, readBases[readBaseIndex], refBases[readBaseIndex])
    i.e. it looks up the REFERENCE base at the read's index instead of at the reference position
    (refIndex + i). With IS_BISULFITE_SEQUENCED=true a converted base is excused only if the
    reference base at contig position (read offset + 1) happens to be C (or G on the reverse
    strand), so PF_MISMATCH_RATE and PF_HQ_ERROR_RATE for bisulfite data depend on the first
    read-length bases of the contig rather than on the aligned bases, and a read aligned to a
    contig shorter than the read length raises ArrayIndexOutOfBoundsException.
A2. badCycleHistogram.increment(getCycle(neg, readLength, i)) uses i, the offset within the
    alignment block, so mismatches in the second and later blocks of a read with an indel are
    attributed to the wrong cycle (BAD_CYCLES).

Design A1: contig 'chr1' whose bases 1..100 are all A (so refBases[readBaseIndex] is never C),
reads of 100 bp aligned at position 1001.. where the reference is a random sequence; every
read has every reference C replaced by T (complete bisulfite conversion, forward strand) and no
other differences. Truth with bisulfite semantics: mismatch rate 0. Control: same reads on a
contig whose bases 1..100 are all C: Picard then excuses every conversion.
Design A2: reads with a 1-bp deletion after base 50 and one mismatch at the last base of the
read (cycle 100): BAD_CYCLES should count cycle 100 when >= 80 % of reads mismatch there.
Usage: python a1_alignment_summary_bisulfite.py [picard.jar]
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(7)
core = rand_seq(rng, 3000)
RL = 100
def make_ref(prefix):
    return prefix * RL + core[RL:]   # bases 1..100 are `prefix`, the rest random
refA = make_ref("A"); refC = make_ref("C")
faA = write_fasta(os.path.join(d, "refA.fa"), [("chr1", refA)])
faC = write_fasta(os.path.join(d, "refC.fa"), [("chr1", refC)])
assert refA[1000:] == refC[1000:]

# forward reads at 1-based positions 1001, 1101, ... with every C -> T (bisulfite converted, forward strand)
recs = []
n_conv = 0
for k in range(10):
    pos0 = 1000 + k * 100
    seg = refA[pos0:pos0 + RL]
    read = seg.replace("C", "T")
    n_conv += seg.count("C")
    recs.append(simple_read(f"bs{k}", pos0, f"{RL}M", flag=0, qual=30, seq=read))
print(f"A1: 10 forward reads x {RL} bp, {n_conv} C->T conversions and no other differences (bisulfite truth: mismatch rate 0.0; non-bisulfite truth: {n_conv/1000:.3f})")
for label, fa, refseq in (("contig bases 1-100 = A", faA, refA), ("contig bases 1-100 = C", faC, refC)):
    bam = write_bam(os.path.join(d, "bs.bam"), recs, [("chr1", len(refseq))])
    for bis in ("false", "true"):
        out = os.path.join(d, "asm.txt")
        run("CollectAlignmentSummaryMetrics", "-I", bam, "-O", out, "-R", fa, "--IS_BISULFITE_SEQUENCED", bis)
        m = parse_metrics(out)[0][0]
        print(f"  {label}, IS_BISULFITE_SEQUENCED={bis}: PF_MISMATCH_RATE {m['PF_MISMATCH_RATE']}  PF_HQ_ERROR_RATE {m['PF_HQ_ERROR_RATE']}  PF_ALIGNED_BASES {m['PF_ALIGNED_BASES']}")

# short contig: a read longer than the contig it maps to, bisulfite mode
short = refA[1000:1000 + 60]   # 60-bp contig
faS = write_fasta(os.path.join(d, "refS.fa"), [("chr1", refA), ("tiny", short)])
recs2 = list(recs) + [simple_read("tiny_read", 0, "60M", flag=0, tid=1, qual=30, seq=short.replace("C", "T"))]
bam2 = write_bam(os.path.join(d, "bs2.bam"), recs2, [("chr1", len(refA)), ("tiny", 60)])
# make the read 100 bp long on a 60-bp contig: 60M40S
recs3 = list(recs) + [simple_read("tiny_read", 0, "60M40S", flag=0, tid=1, qual=30, seq=short.replace("C", "T") + "A" * 40)]
bam3 = write_bam(os.path.join(d, "bs3.bam"), recs3, [("chr1", len(refA)), ("tiny", 60)])
recs6 = list(recs) + [simple_read("tiny_read", 0, "40S60M", flag=0, tid=1, qual=30, seq="A" * 40 + short.replace("C", "T"))]
bam6 = write_bam(os.path.join(d, "bs6.bam"), recs6, [("chr1", len(refA)), ("tiny", 60)])
for label, b in (("100-bp read with 60M40S on a 60-bp contig", bam3), ("100-bp read with 40S60M on a 60-bp contig", bam6)):
    for bis in ("false", "true"):
        try:
            run("CollectAlignmentSummaryMetrics", "-I", b, "-O", os.path.join(d, "asm2.txt"), "-R", faS, "--IS_BISULFITE_SEQUENCED", bis)
            print(f"  {label}, IS_BISULFITE_SEQUENCED={bis}: ran (PF_MISMATCH_RATE {parse_metrics(os.path.join(d,'asm2.txt'))[0][0]['PF_MISMATCH_RATE']})")
        except RuntimeError as e:
            print(f"  {label}, IS_BISULFITE_SEQUENCED={bis}: FAILED ({e})")
        except Exception as e:
            print(f"  {label}, IS_BISULFITE_SEQUENCED={bis}: FAILED ({e})")

# A2: BAD_CYCLES with a deletion. 10 forward reads, CIGAR 50M1D50M; reads 0-4 mismatch at cycle 50 (last base of
# block 1), reads 5-9 mismatch at cycle 100 (last base of block 2). Correct attribution: 50 % at cycle 50 and 50 %
# at cycle 100, no cycle at >= 80 % -> BAD_CYCLES 0. With the block-relative offset both land on cycle 50.
def mut(b): return "A" if b != "A" else "C"
recs4 = []
for k in range(10):
    pos0 = 1000 + k * 100
    seg = refA[pos0:pos0 + 50] + refA[pos0 + 51:pos0 + 101]
    seg = (seg[:49] + mut(seg[49]) + seg[50:]) if k < 5 else (seg[:-1] + mut(seg[-1]))
    recs4.append(simple_read(f"del{k}", pos0, "50M1D50M", flag=0, qual=30, seq=seg))
recs5 = []
for k in range(10):
    pos0 = 1000 + k * 100
    seg = refA[pos0:pos0 + 100]
    seg = (seg[:49] + mut(seg[49]) + seg[50:]) if k < 5 else (seg[:-1] + mut(seg[-1]))
    recs5.append(simple_read(f"nodel{k}", pos0, "100M", flag=0, qual=30, seq=seg))
for label, rr in (("10 reads 50M1D50M, 5 mismatch at cycle 50 and 5 at cycle 100", recs4), ("control: 10 reads 100M, 5 mismatch at cycle 50 and 5 at cycle 100", recs5)):
    b = write_bam(os.path.join(d, "bad.bam"), rr, [("chr1", len(refA))])
    run("CollectAlignmentSummaryMetrics", "-I", b, "-O", os.path.join(d, "asm3.txt"), "-R", faA)
    m = parse_metrics(os.path.join(d, "asm3.txt"))[0][0]
    print(f"A2: {label}: BAD_CYCLES {m['BAD_CYCLES']} (truth 0: no cycle mismatches in >= 80 % of reads), PF_MISMATCH_RATE {m['PF_MISMATCH_RATE']}, PF_INDEL_RATE {m['PF_INDEL_RATE']}")
