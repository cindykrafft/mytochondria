#!/usr/bin/env python3
"""BT2: under -split, BlockMgr::findBlockedOverlaps tests -F (and -r) against the SUM of
the block lengths of every B record that touched the A record, with the unique overlap
as numerator, and clears every hit when the ratio is too small. A B record that is
100 % inside A is dropped when other B records also overlap A. Without -split, -F is
per B record. (Prior report: upstream issue #1142, 2026-08-05.)

Part A: minimal example (three identical 50-bp reads fully inside a 100-bp A).
Part B: random BED12 reads vs A intervals; shipped `-split -F 0.5` and `-split -f 0.5 -r`
        vs the per-record reference; false negatives and false positives counted.
Part C: -f under -split is cumulative over B (documented in the project's tests for
        issue #750): recorded, not counted as a defect.
"""
import os, random, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
rng = random.Random(7)
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed"); B1 = os.path.join(tmp, "b1.bed")

print("\n== A. minimal: A = chr1:100-200; B = three identical single-block BED12 reads chr1:120-170")
write(A, [["chr1", 100, 200, "gene"]])
reads = [bed12("chr1", 120, [(0, 50)], "r%d" % i) for i in (1, 2, 3)]
write(B, reads); write(B1, reads[:1])
for label, f, args in (("three reads", B, ["-split", "-F", "0.5"]), ("three reads, no -split", B, ["-F", "0.5"]),
                       ("one read", B1, ["-split", "-F", "0.5"]), ("three reads", B, ["-split", "-F", "0.34"]),
                       ("three reads", B, ["-split", "-F", "0.33"])):
    out = lines(run(["intersect", "-a", A, "-b", f, "-wa", "-wb", *args]))
    print("   %-24s %-22s -> %d lines %s" % (label, " ".join(args), len(out), [l[7] for l in out]))
print("   (each read is 100 % inside A; expected 3 lines for every -F <= 1.0; the break at 50/150 = 0.333 is the summed denominator)")

def blocks_of(r):
    st = int(r[1]); sizes = [int(x) for x in r[10].split(",") if x]; offs = [int(x) for x in r[11].split(",") if x]
    return [(st + o, st + o + s) for o, s in zip(offs, sizes)]

print("\n== B. random: 200 A intervals (BED4), 4000 BED12 reads with 1-3 blocks")
arows = sorted_bed([["chr1", s, s + rng.randint(100, 2000), "a%d" % i] for i, s in enumerate(rng.randint(0, 1_000_000) for _ in range(200))])
brows = sorted_bed([bed12("chr1", rng.randint(0, 1_000_000), rand_blocks(rng, rng.choice([1, 2, 3]), 10, 100, 10, 500), "r%d" % i) for i in range(4000)])
write(A, arows); write(B, brows)
for F in ("0.5", "0.9"):
    ref = set()
    for a in arows:
        a0, a1 = int(a[1]), int(a[2])
        for r in brows:
            bl = blocks_of(r); blen = sum(e - s for s, e in bl)
            ov = sum(overlap(a0, a1, s, e) for s, e in bl)
            if ov > 0 and ov / blen >= float(F):
                ref.add((a[3], r[3]))
    ship = {(l[3], l[7]) for l in lines(run(["intersect", "-a", A, "-b", B, "-split", "-F", F, "-wa", "-wb"]))}
    print("   -split -F %s: reference pairs %d, shipped %d, missed (false negatives) %d, extra (false positives) %d" %
          (F, len(ref), len(ship), len(ref - ship), len(ship - ref)))
    ship_nosplit = {(l[3], l[7]) for l in lines(run(["intersect", "-a", A, "-b", B, "-F", F, "-wa", "-wb"]))}
    # without -split the reference is span-based: overlap(A, span(B)) / len(span(B))
    ref_span = set()
    for a in arows:
        a0, a1 = int(a[1]), int(a[2])
        for r in brows:
            b0, b1 = int(r[1]), int(r[2]); ov = overlap(a0, a1, b0, b1)
            if ov > 0 and ov / (b1 - b0) >= float(F): ref_span.add((a[3], r[3]))
    print("      control without -split: reference %d, shipped %d, missed %d, extra %d" % (len(ref_span), len(ship_nosplit), len(ref_span - ship_nosplit), len(ship_nosplit - ref_span)))

# -r with -f: reciprocal per record (unique overlap / len A >= f AND / blocks(B) >= f); shipped uses cumulative A fraction and summed B
f = "0.5"
ref = set()
for a in arows:
    a0, a1 = int(a[1]), int(a[2])
    for r in brows:
        bl = blocks_of(r); blen = sum(e - s for s, e in bl); ov = sum(overlap(a0, a1, s, e) for s, e in bl)
        if ov > 0 and ov / blen >= 0.5 and ov / (a1 - a0) >= 0.5: ref.add((a[3], r[3]))
ship = {(l[3], l[7]) for l in lines(run(["intersect", "-a", A, "-b", B, "-split", "-f", f, "-r", "-wa", "-wb"]))}
print("   -split -f 0.5 -r: per-record reciprocal reference %d, shipped %d, missed %d, extra %d" % (len(ref), len(ship), len(ref - ship), len(ship - ref)))

print("\n== C. -f under -split is cumulative over all B records (project test intersect.t22.*; issue #750)")
write(A, [["chr1", 100, 200, "gene"]])
write(B, [bed12("chr1", 100, [(0, 40)], "r1"), bed12("chr1", 160, [(0, 40)], "r2")])
print("   two 40-bp reads at 100-140 and 160-200 on a 100-bp A, -f 0.5:")
print("   -split: %d lines; no -split: %d lines" % (len(lines(run(["intersect", "-a", A, "-b", B, "-split", "-f", "0.5", "-wa", "-wb"]))),
                                                  len(lines(run(["intersect", "-a", A, "-b", B, "-f", "0.5", "-wa", "-wb"])))))
