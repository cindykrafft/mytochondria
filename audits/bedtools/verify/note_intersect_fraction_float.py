#!/usr/bin/env python3
"""N1 (note): Record::sameChromIntersects computes the overlap fractions in float
(`(float)overlapBases / (float)aLen`, Record.cpp:205-206), so intervals longer than
2^24 = 16,777,216 bp cannot distinguish "all but a few bases" from "all": -f 1.0 /
-F 1.0 accept an interval that is not fully contained. Quantified: the minimal case,
and the disagreement rate between the float rule and exact rational arithmetic on
random large intervals at -f 0.5 and -f 1.0.
"""
import os, random, sys, tempfile
from fractions import Fraction
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
rng = random.Random(5)
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed")

print("\n== minimal: A = [0, 16777217), B = [0, 16777216): A is one base longer than B")
write(A, [["chr1", 0, 16777217]]); write(B, [["chr1", 0, 16777216]])
print("   intersect -f 1.0 -u    -> %d line(s) (expected 0)" % len(lines(run(["intersect", "-a", A, "-b", B, "-f", "1.0", "-u"]))))
print("   intersect -F 1.0 -u, roles swapped -> %d line(s) (expected 0)" % len(lines(run(["intersect", "-a", B, "-b", A, "-F", "1.0", "-u"]))))
write(A, [["chr1", 0, 17]]); write(B, [["chr1", 0, 16]])
print("   control A = [0,17), B = [0,16): -f 1.0 -u -> %d line(s)" % len(lines(run(["intersect", "-a", A, "-b", B, "-f", "1.0", "-u"]))))
print("   float32(16777216/16777217) = %r" % float(np.float32(16777216) / np.float32(16777217)))

print("\n== random: 20000 pairs of intervals of length 1e7-1e8 with overlap, -f 0.5 and -f 1.0, float rule vs exact rational")
for f in ("0.5", "1.0"):
    ff = np.float32(float(f)); disagree = 0; n_pairs = 0
    for _ in range(20000):
        alen = rng.randint(10_000_000, 100_000_000)
        # overlap drawn near the threshold to stress the boundary
        if f == "1.0":
            ov = alen - rng.randint(0, 20)
        else:
            ov = alen // 2 + rng.randint(-5, 5)
        exact = Fraction(ov, alen) >= Fraction(f)
        flt = (np.float32(ov) / np.float32(alen)) >= ff
        n_pairs += 1; disagree += exact != flt
    print("   -f %s: %d of %d boundary-stressed pairs decided differently by float32 and exact arithmetic" % (f, disagree, n_pairs))
print("   (pairs drawn uniformly at random almost never sit within 6e-8 of the threshold, so the practical rate is ~0 except for -f/-F 1.0 on > 16.7 Mb intervals)")
