"""N1: `samtools stats -p` (remove overlaps) decides that a read cannot overlap
its mate when |TLEN| >= 2 x its own length (stats.c remove_overlaps).  With
mates of unequal length (adapter-trimmed pairs) the shorter mate bypasses the
overlap bookkeeping, so the overlap is counted twice in "bases mapped (cigar)"
and in the coverage distribution.  Usage: python note_stats_overlap_unequal_mates.py [samtools]
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
d = tmpdir()
refs = [("chr1", 100000)]

def pair(name, pos, l1, l2, ins):
    r1 = simple_read(name, pos, f"{l1}M", flag=0x63, mtid=0, mpos=pos + ins - l2, tlen=ins)
    r2 = simple_read(name, pos + ins - l2, f"{l2}M", flag=0x93, mtid=0, mpos=pos, tlen=-ins)
    return [r1, r2]

cases = [("equal mates 100/100, insert 150 (overlap 50)", 100, 100, 150),
         ("equal mates 100/100, insert 190 (overlap 10)", 100, 100, 190),
         ("unequal mates 150/90, insert 200 (overlap 40)", 150, 90, 200),
         ("unequal mates 150/70, insert 170 (overlap 50)", 150, 70, 170),
         ("unequal mates 120/60, insert 130 (overlap 50)", 120, 60, 130)]
for label, l1, l2, ins in cases:
    recs = []
    for i in range(200): recs += pair(f"p{i}", 1000 + i * 400, l1, l2, ins)
    bam = write_bam(os.path.join(d, "ov.bam"), recs, refs)
    out, _, _ = run("stats", "-p", bam)
    S = sn(out)
    union = 200 * (ins if ins < l1 + l2 else l1 + l2)  # bases covered by the pair once
    raw = 200 * (l1 + l2)
    cov = parse_cov(out)
    print(f"\n[{label}]")
    print(f"  bases mapped (cigar) with -p: {S['bases mapped (cigar)']}   truth (overlap counted once): {union}   without overlap removal: {raw}")
    print(f"  COV rows with -p: {dict(sorted(cov.items()))}   truth: {{1: {union}}}")
