"""H1: CollectHsMetrics ZERO_CVG_TARGETS_PCT divides unique zero-coverage targets by the raw target count.

TargetMetricsCollector counts zero-coverage targets over the UNIQUED target list (overlapping or
duplicate intervals merged) but divides by allTargets.getIntervals().size(), the number of
intervals in the file as given. Target files with overlapping intervals (adjacent exons of
overlapping transcripts, padded designs) therefore understate the fraction of targets without
coverage.

Design: 8 target intervals of which two pairs overlap (uniqued: 6). Reads cover only the two
merged targets; the other four unique targets have no coverage. Truth: 4/6 = 0.667.
Usage: python h1_hsmetrics_zero_cvg_targets.py [picard.jar]
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(5)
L = 5000
ref = rand_seq(rng, L)
fa = write_fasta(os.path.join(d, "ref.fa"), [("chr1", ref)])
targets = [("A1", 100, 200), ("A2", 150, 250), ("B1", 400, 500), ("B2", 450, 550), ("C", 700, 800), ("D", 900, 1000), ("E", 1200, 1300), ("F", 1500, 1600)]
il = os.path.join(d, "targets.interval_list")
with open(il, "w") as f:
    f.write("@HD\tVN:1.6\tSO:coordinate\n@SQ\tSN:chr1\tLN:%d\n" % L)
    for n, s, e in targets:
        f.write(f"chr1\t{s}\t{e}\t+\t{n}\n")

recs = []
# pairs covering A (100-250) and B (400-550) completely, 10 pairs each
for i in range(10):
    recs += pair(f"pA{i}", 99, 150, rlen=100, qual=30)      # read1 100-199, read2 151-250
    recs += pair(f"pB{i}", 399, 450, rlen=100, qual=30)
# one pair near but not on any bait: read1 at 2000-2099 (nearest bait F ends at 1600 -> 400 bp away: off bait);
# and one pair with read1 at 1701-1800 (101 bp from F's end: within NEAR_DISTANCE 250, overlaps no bait)
recs += pair("near", 1700, 1800, rlen=100, qual=30)
recs += pair("off", 2500, 2600, rlen=100, qual=30)
bam = write_bam(os.path.join(d, "reads.bam"), recs, [("chr1", L)])

out = os.path.join(d, "hs.txt")
run("CollectHsMetrics", "-I", bam, "-O", out, "-R", fa, "--BAIT_INTERVALS", il, "--TARGET_INTERVALS", il)
m, h = parse_metrics(out)
m = m[0]
print("\ntargets as given: 8 intervals; after merging overlaps: 6 unique targets (A, B, C, D, E, F)")
print("reads cover A and B only -> zero-coverage unique targets C, D, E, F = 4 of 6 = 0.6667")
print("  ZERO_CVG_TARGETS_PCT:", m["ZERO_CVG_TARGETS_PCT"], " (Picard divides 4 by the 8 intervals in the file)")
print("  TARGET_TERRITORY:", m["TARGET_TERRITORY"], "(unique bases; the 8 raw intervals sum to", sum(e - s + 1 for _, s, e in targets), ")")
print("  PCT_TARGET_BASES_1X:", m["PCT_TARGET_BASES_1X"], " expected", round((151 + 151) / m["TARGET_TERRITORY"], 6))
print("  ON_BAIT_BASES / NEAR_BAIT_BASES / OFF_BAIT_BASES:", m["ON_BAIT_BASES"], m["NEAR_BAIT_BASES"], m["OFF_BAIT_BASES"])
print("  HS_LIBRARY_SIZE:", m["HS_LIBRARY_SIZE"], " MEAN_TARGET_COVERAGE:", m["MEAN_TARGET_COVERAGE"], " FOLD_80_BASE_PENALTY:", m["FOLD_80_BASE_PENALTY"])
