"""G1: CollectGcBiasMetrics bins read starts near contig ends at GC 0 and shifts forward-read windows by one base.

GcBiasUtils.calculateAllGcs fills gc[i] for 0-based window starts i = 1 .. lastWindowStart-1 only;
gc[0] and gc[lastWindowStart..] stay 0. GcBiasMetricsCollector.addRead looks up gc[pos] with pos =
the 1-based alignment start (forward reads) or alignmentEnd - windowSize (reverse reads) and accepts
any value >= 0, so (a) a forward read's window starts one base after its 5' end, and (b) reads whose
window would run past the contig end are counted in the GC = 0 bin instead of being skipped.

Design: (a) a contig whose first 100 bases are A and base 101 is G: a forward read starting at
base 1 has a 0 % GC window by the documented definition; Picard uses bases 2-101 (1 %).
(b) a 300-bp contig with a 100-bp forward read starting at every position 1..201 plus reads
starting at 202..300 whose window does not fit: the latter should not be counted at any GC.
Usage: python g1_gcbias_window.py [picard.jar]
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(3)
W = 100
# contig A: 100 A's, then G, then random 50% GC
seqA = "A" * 100 + "G" + rand_seq(rng, 899)
# contig B: 300 bp, 50 % GC everywhere (windows all have GC in a narrow range)
seqB = "".join("GCAT"[i % 4] for i in range(300))   # exactly 50 % GC in every window
refs = [("cA", seqA), ("cB", seqB)]
fa = write_fasta(os.path.join(d, "ref.fa"), refs)

recs = []
# (a) one forward read at base 1 of cA
recs.append(simple_read("a_fwd_1", 0, f"{W}M", flag=0, tid=0, qual=30, seq=seqA[0:W]))
# (b) forward reads on cB at 1-based starts 1..300 (reads past the end are shortened to fit the contig)
for p in range(1, 301):
    ln = min(W, 300 - p + 1)
    recs.append(simple_read(f"b_fwd_{p}", p - 1, f"{ln}M", flag=0, tid=1, qual=30, seq=seqB[p - 1:p - 1 + ln]))
bam = write_bam(os.path.join(d, "reads.bam"), recs, [(n, len(s)) for n, s in refs])

out = os.path.join(d, "gc.txt"); summ = os.path.join(d, "gc_summary.txt"); chart = os.path.join(d, "gc.pdf")
run("CollectGcBiasMetrics", "-I", bam, "-O", out, "-S", summ, "--CHART_OUTPUT", chart, "-R", fa, "--SCAN_WINDOW_SIZE", W)
m, _ = parse_metrics(out)
details = [x for x in m if "GC" in x]
by_gc = {x["GC"]: x for x in details}
print("\n(a) documented window for a_fwd_1 = cA bases 1-100 = 0 % GC; Picard uses bases 2-101 (1 %).")
print("    READ_STARTS at GC=0:", by_gc[0]["READ_STARTS"], "  at GC=1:", by_gc[1]["READ_STARTS"], " (cB reads all sit at GC 50: ", by_gc[50]["READ_STARTS"], ")")
print("(b) cB: 300 bp, 50 % GC everywhere. Forward reads at every start 1..300.")
print("    windows fitting in the contig: starts 1..201; Picard computes gc[] for 0-based starts 1..199 and counts", by_gc[50]["WINDOWS"], "windows at GC 50")
print("    reads counted at GC 50:", by_gc[50]["READ_STARTS"], " reads counted at GC 0:", by_gc[0]["READ_STARTS"], " (expected 0 at GC 0: a read whose window runs off the contig has no window)")
sm = parse_metrics(summ)[0][0]
print("    summary: TOTAL_CLUSTERS", sm["TOTAL_CLUSTERS"], "ALIGNED_READS", sm["ALIGNED_READS"], "GC_NC_40_59", sm["GC_NC_40_59"], "AT_DROPOUT", sm["AT_DROPOUT"], "GC_DROPOUT", sm["GC_DROPOUT"])
tot = sum(x["READ_STARTS"] for x in details)
print("    sum of READ_STARTS over all GC bins:", tot, "of", len(recs), "reads")
