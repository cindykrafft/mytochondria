"""N4: `samtools depth -s` keys its overlap bookkeeping on the read name only
(bam2depth.c olap_hash).  Supplementary records are not in the default
exclusion list, so a supplementary alignment of read 1 that sorts between the
two mates consumes read 1's hash entry: the supplementary block is clipped
away entirely and the real mate overlap is then counted twice.
Usage: python note_depth_s_supplementary.py [samtools]
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
d = tmpdir()
refs = [("chr1", 10000)]

def run_case(label, recs, expect):
    bam = write_bam(os.path.join(d, "s.bam"), recs, refs)
    out, _, _ = run("depth", "-s", bam)
    got = {int(l.split("\t")[1]) - 1: int(l.split("\t")[2]) for l in out.splitlines()}
    print(f"\n[{label}]")
    for lo, hi, desc in expect:
        vals = sorted(set(got.get(p, 0) for p in range(lo, hi)))
        print(f"  positions {lo + 1}-{hi}: depth {vals}   ({desc})")

# pair: read1 fwd 100-200, read2 rev 150-250; overlap 150-200
r1 = simple_read("q", 100, "100M", flag=0x63, mtid=0, mpos=150, tlen=150)
r2 = simple_read("q", 150, "100M", flag=0x93, mtid=0, mpos=100, tlen=-150)
run_case("pair only", [r1, r2], [(100, 150, "read1 only: expect 1"), (150, 200, "overlap: expect 1 with -s"), (200, 250, "read2 only: expect 1")])
# same pair plus a supplementary record of read1 at 120-160 (sorts between the mates)
sup = simple_read("q", 120, "40M60H", flag=0x63 | 0x800, mtid=0, mpos=150, tlen=0)
run_case("pair + supplementary of read1 between the mates", [r1, sup, r2],
         [(100, 120, "read1 only: expect 1"), (120, 150, "read1 + supplementary: expect 2"), (150, 160, "read1 + supplementary + read2 overlap: expect 2"),
          (160, 200, "overlap: expect 1 with -s"), (200, 250, "read2 only: expect 1")])
run_case("same, with -G SUPPLEMENTARY excluded (what the user would want)", [r1, r2], [(150, 200, "overlap: expect 1")])
