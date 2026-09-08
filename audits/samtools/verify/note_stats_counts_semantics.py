"""N2/N3: two `samtools stats` SN definitions worth knowing when a percentage is
formed from them.  N2: "reads duplicated" counts supplementary records carrying
the DUP flag (stats.c collect_stats counts duplicates before the IS_ORIGINAL
check) while "sequences" excludes supplementary records, so
reads duplicated / sequences overstates the duplication rate when markdup -S
or Picard has flagged supplementary alignments.  N3: the insert-size standard
deviation loop starts at bin 1 (stats.c output_stats), so pairs with TLEN 0
on the same chromosome enter the mean and the denominator but not the sum of
squares.  Usage: python note_stats_counts_semantics.py [samtools]
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
d = tmpdir()
refs = [("chr1", 1_000_000)]

print("\n--- N2: reads duplicated vs sequences with duplicate-flagged supplementary records")
recs = []
for i in range(1000):
    pos = 1000 + i * 500; dup = 0x400 if i % 5 == 0 else 0
    recs.append(simple_read(f"p{i}", pos, "100M", flag=0x63 | dup, mtid=0, mpos=pos + 200, tlen=300))
    recs.append(simple_read(f"p{i}", pos + 200, "100M", flag=0x93 | dup, mtid=0, mpos=pos, tlen=-300))
    if i % 2 == 0:  # every other pair has a supplementary record of read 2, flagged like its primary (markdup -S / Picard)
        recs.append(simple_read(f"p{i}", pos + 5000, "30M70H", flag=0x93 | 0x800 | dup, mtid=0, mpos=pos, tlen=0))
bam = write_bam(os.path.join(d, "dup.bam"), recs, refs)
S = sn(run("stats", bam)[0])
prim_dup = sum(1 for r in recs if r["flag"] & 0x400 and not r["flag"] & 0x800)
supp_dup = sum(1 for r in recs if r["flag"] & 0x400 and r["flag"] & 0x800)
print(f"  sequences (excludes supplementary): {S['sequences']}   reads duplicated: {S['reads duplicated']}   supplementary alignments: {S['supplementary alignments']}")
print(f"  primary records with DUP: {prim_dup}   supplementary records with DUP: {supp_dup}")
print(f"  reads duplicated / sequences = {100 * int(S['reads duplicated']) / int(S['sequences']):.1f} %   primary DUP / sequences = {100 * prim_dup / int(S['sequences']):.1f} %")
fs = [l for l in run("flagstat", bam)[0].splitlines() if "duplicates" in l]
print("  flagstat:", " | ".join(fs))

print("\n--- N3: insert size SD with same-chromosome pairs whose TLEN is 0")
recs = []
isz = []
for i in range(1000):
    pos = 1000 + i * 600
    tl = 0 if i % 10 == 0 else 300 + (i % 7) * 10
    isz.append(tl)
    if tl:
        recs.append(simple_read(f"p{i}", pos, "100M", flag=0x63, mtid=0, mpos=pos + tl - 100, tlen=tl))
        recs.append(simple_read(f"p{i}", pos + tl - 100, "100M", flag=0x93, mtid=0, mpos=pos, tlen=-tl))
    else:
        recs.append(simple_read(f"p{i}", pos, "100M", flag=0x61, mtid=0, mpos=pos + 200, tlen=0))
        recs.append(simple_read(f"p{i}", pos + 200, "100M", flag=0x91, mtid=0, mpos=pos, tlen=0))
bam = write_bam(os.path.join(d, "isz.bam"), recs, refs)
S = sn(run("stats", bam)[0])
mean = sum(isz) / len(isz)
sd_all = math.sqrt(sum((x - mean) ** 2 for x in isz) / len(isz))
sd_skip0 = math.sqrt(sum((x - mean) ** 2 for x in isz if x >= 1) / len(isz))
print(f"  pairs: {len(isz)}, of which TLEN 0: {isz.count(0)}")
print(f"  samtools: insert size average {S['insert size average']}, standard deviation {S['insert size standard deviation']}")
print(f"  population SD over all {len(isz)} pairs: {sd_all:.1f}   SD with the TLEN-0 bin left out of the sum of squares but in the denominator: {sd_skip0:.1f}")
