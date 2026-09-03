#!/usr/bin/env python3
"""BT5: `slop -pct` and `flank -pct` compute the slop as float32(pct) * float32(size)
and truncate with a C cast (slopBed.cpp:58-60,87-88; flankBed.cpp:57-58). When pct*size
is an exact integer k but the float product lands just below k, one base is lost.
`slop -l/-r/-b` are also stored as float, so absolute values above 2^24 are rounded.

Part A: closed form over pct = 0.01..0.99 and sizes 1..20000 (numpy float32).
Part B: the shipped binary on a grid of (pct, size) from part A, slop and flank.
Part C: slop -b 20000001.
"""
import os, sys, tempfile
import numpy as np
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); G = os.path.join(tmp, "g.genome")
write(G, [["chr1", 100_000_000]])

print("\n== A. closed form: int(float32(p) * float32(n)) != p*n where p*n is an integer, n <= 20000")
hits = {}
for i in range(1, 100):
    p = i / 100; pf = np.float32(p); fr = Fraction(i, 100)
    bad = []
    for n in range(1, 20001):
        ex = fr * n
        if ex.denominator != 1: continue
        got = int(np.float32(pf * np.float32(n)))
        if got != int(ex): bad.append((n, int(ex), got))
    if bad: hits[p] = bad
for p, bad in sorted(hits.items()):
    print("   pct %.2f: %3d sizes affected, e.g. %s" % (p, len(bad), ", ".join("%d->%d" % (n, g) for n, e, g in bad[:4])))
print("   affected pct values: %s; unaffected: the other %d of 99" % ([p for p in sorted(hits)], 99 - len(hits)))

print("\n== B. shipped binary: slop -pct -b P and flank -pct -l P -r 0 on a feature of size n at chr1:1000000")
rows = []
n_bad_slop = n_bad_flank = n_cases = 0
for p, bad in sorted(hits.items()):
    for n, ex, got in bad[:3]:
        write(A, [["chr1", 1_000_000, 1_000_000 + n]])
        s = lines(run(["slop", "-i", A, "-g", G, "-b", str(p), "-pct"]))[0]
        f = lines(run(["flank", "-i", A, "-g", G, "-l", str(p), "-r", "0", "-pct"]))[0]
        slop_added = 1_000_000 - int(s[1]); flank_len = int(f[2]) - int(f[1])
        n_cases += 1; n_bad_slop += slop_added != ex; n_bad_flank += flank_len != ex
        rows.append((p, n, ex, slop_added, flank_len))
for p, n, ex, sa, fl in rows[:12]:
    print("   pct %.2f size %5d: exact %4d  slop added %4d  flank length %4d" % (p, n, ex, sa, fl))
print("   ... %d cases: slop wrong in %d, flank wrong in %d" % (n_cases, n_bad_slop, n_bad_flank))
print("   controls (pct 0.10, 0.25, 0.50 on 1000 bp):")
for p in ("0.10", "0.25", "0.50"):
    write(A, [["chr1", 1_000_000, 1_001_000]])
    s = lines(run(["slop", "-i", A, "-g", G, "-b", p, "-pct"]))[0]
    print("   pct %s -> slop added %d" % (p, 1_000_000 - int(s[1])))

print("\n== C. slop -b 20000001 on chr1:25000000-25000010 (expected 4999999-45000011)")
write(A, [["chr1", 25_000_000, 25_000_010]])
s = lines(run(["slop", "-i", A, "-g", G, "-b", "20000001"]))[0]
print("   got %s-%s  (float32(20000001) = %d)" % (s[1], s[2], int(np.float32(20000001))))
