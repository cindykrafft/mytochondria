#!/usr/bin/env python3
"""BT1: `bedtools coverage -split` reports, in the "number of B features overlapping A"
column (and under -counts), the number of overlapping *blocks*, not the number of B
records; and it ignores -f/-F because CoverageFile::checkSplits keeps the per-block
overlap list regardless of whether BlockMgr::findBlockedOverlaps cleared the hit list.

Part A: minimal examples.
Part B: random BED12 reads (1-4 blocks) against random A intervals; the shipped count
        vs an independent port (records with >= 1 overlapping block) and vs the
        project's own `intersect -c -split`.
Part C: -f under -split: shipped coverage vs intersect -c -split -f (the project's
        cumulative-fraction semantic) and vs the per-record semantic.
"""
import os, random, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
rng = random.Random(20260903)
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed")

print("\n== A. minimal: A = chr1:100-1000; one BED12 read with two 100-bp blocks inside A")
write(A, [["chr1", 100, 1000, "gene"]])
write(B, [bed12("chr1", 150, [(0, 100), (650, 100)])])
for args in (["-split"], [], ["-split", "-counts"]):
    print("   coverage %-16s -> %s" % (" ".join(args), run(["coverage", "-a", A, "-b", B, *args]).strip()))
print("   intersect -c -split      -> %s" % run(["intersect", "-a", A, "-b", B, "-split", "-c"]).strip())
print("   (expected count 1: one B record; the project's test coverage.t10 expects 3 for a 3-block read)")

print("\n   A = chr1:100-200; one 10-bp single-block BED12 read inside; -f 0.5")
write(A, [["chr1", 100, 200, "gene"]])
write(B, [bed12("chr1", 120, [(0, 10)])])
print("   coverage -split -f 0.5    -> %s" % run(["coverage", "-a", A, "-b", B, "-split", "-f", "0.5"]).strip())
print("   coverage -f 0.5           -> %s" % run(["coverage", "-a", A, "-b", B, "-f", "0.5"]).strip())
print("   intersect -c -split -f 0.5-> %s" % run(["intersect", "-a", A, "-b", B, "-split", "-c", "-f", "0.5"]).strip())
print("   (expected under -f 0.5: 0 hits, 0 bases; 10/100 = 0.10 < 0.5)")

print("\n== B. random: 300 A intervals, 3000 BED12 reads with 1-4 blocks on chr1")
arows = sorted_bed([["chr1", s, s + rng.randint(200, 3000), "a%d" % i] for i, s in enumerate(rng.randint(0, 2_000_000) for _ in range(300))])
brows = []
for i in range(3000):
    blocks = rand_blocks(rng, rng.choice([1, 1, 2, 3, 4]), 10, 120, 10, 800)
    brows.append(bed12("chr1", rng.randint(0, 2_000_000), blocks, "r%d" % i, rng.choice("+-")))
brows = sorted_bed(brows)
write(A, arows); write(B, brows)
# port: per A, number of records with >=1 block overlapping A by >=1 bp; number of blocks overlapping; bases covered (union)
def blocks_of(r):
    st = int(r[1]); sizes = [int(x) for x in r[10].split(",") if x]; offs = [int(x) for x in r[11].split(",") if x]
    return [(st + o, st + o + s) for o, s in zip(offs, sizes)]
port = {}
for a in arows:
    a0, a1 = int(a[1]), int(a[2])
    nrec = nblk = 0; cov = []
    for r in brows:
        bl = [(max(s, a0), min(e, a1)) for s, e in blocks_of(r) if overlap(a0, a1, s, e) > 0]
        if bl:
            nrec += 1; nblk += len(bl); cov += bl
    port[a[3]] = (nrec, nblk, merged_length(cov))
ship = {l[3]: (int(l[4]), int(l[5])) for l in lines(run(["coverage", "-a", A, "-b", B, "-split"]))}
isec = {l[3]: int(l[4]) for l in lines(run(["intersect", "-a", A, "-b", B, "-split", "-c"]))}
n_rec_ok = sum(ship[k][0] == port[k][0] for k in port)
n_blk_ok = sum(ship[k][0] == port[k][1] for k in port)
n_cov_ok = sum(ship[k][1] == port[k][2] for k in port)
n_isec_ok = sum(isec[k] == port[k][0] for k in port)
differ = sum(port[k][0] != port[k][1] for k in port)
print("   A intervals where records != blocks in the port: %d of %d" % (differ, len(port)))
print("   coverage -split count == port records: %d / %d;  == port blocks: %d / %d" % (n_rec_ok, len(port), n_blk_ok, len(port)))
print("   coverage -split bases covered == port union: %d / %d" % (n_cov_ok, len(port)))
print("   intersect -c -split == port records: %d / %d" % (n_isec_ok, len(port)))
tot_ship = sum(v[0] for v in ship.values()); tot_rec = sum(v[0] for v in port.values()); tot_blk = sum(v[1] for v in port.values())
print("   totals: coverage -split %d, records %d, blocks %d" % (tot_ship, tot_rec, tot_blk))

print("\n== C. -f 0.5 under -split on the same data")
ship_f = {l[3]: (int(l[4]), int(l[5])) for l in lines(run(["coverage", "-a", A, "-b", B, "-split", "-f", "0.5"]))}
isec_f = {l[3]: int(l[4]) for l in lines(run(["intersect", "-a", A, "-b", B, "-split", "-c", "-f", "0.5"]))}
# per-record semantic: record qualifies if its overlap with A (unique over its own blocks) / len(A) >= 0.5
per_rec = {}
for a in arows:
    a0, a1 = int(a[1]), int(a[2]); n = 0
    for r in brows:
        ov = merged_length([(max(s, a0), min(e, a1)) for s, e in blocks_of(r) if overlap(a0, a1, s, e) > 0])
        if ov and ov / (a1 - a0) >= 0.5: n += 1
    per_rec[a[3]] = n
same_as_nosplit = {k: ship_f[k][0] == ship[k][0] and ship_f[k][1] == ship[k][1] for k in ship}
print("   coverage -split -f 0.5 identical to coverage -split (no -f): %d / %d A intervals" % (sum(same_as_nosplit.values()), len(ship)))
print("   A intervals with intersect -c -split -f 0.5 == 0 but coverage -split -f 0.5 count > 0: %d" %
      sum(1 for k in ship if isec_f[k] == 0 and ship_f[k][0] > 0))
print("   A intervals where per-record semantic == 0 but coverage -split -f 0.5 count > 0: %d" %
      sum(1 for k in ship if per_rec[k] == 0 and ship_f[k][0] > 0))
