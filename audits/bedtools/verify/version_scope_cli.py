#!/usr/bin/env python3
"""Version scope by execution: the six confirmed findings reproduced through the command
line on whichever `bedtools` binary the BT environment variable names.

  BT1  coverage -split on one two-block BED12 read: count column (expected 1) and
       coverage -split -f 0.5 on a 10 % read (expected count 0)
  BT2  intersect -split -F 0.5: three identical reads fully inside A (expected 3 lines)
  BT3  closest -D a -t first on a reverse-strand query with a left/right tie
       (expected the left record b1, the first in the B file)
  BT4  reldist at 1.2e9 (expected one line, 0.100); subtract at 3e9 (expected two
       positive pieces); closest -d at gap 3e9 (expected 3000000001)
  BT5  slop -pct -b 0.53 on a 100-bp feature (expected 53 added); slop -b 20000001
  BT6  shuffle -incl: 2000 50-bp features into a 100-bp include interval, seed 1
       (expected 0 features extending past the include interval)
"""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version(), "(", BT, ")")
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed"); G = os.path.join(tmp, "g.genome")

def verdict(label, got, exp):
    print("%s: got %s, expected %s -> %s" % (label, got, exp, "unaffected" if got == exp else "AFFECTED"))

# BT1
write(A, [["chr1", 100, 1000, "gene"]]); write(B, [bed12("chr1", 150, [(0, 100), (650, 100)])])
verdict("BT1 coverage -split count", lines(run(["coverage", "-a", A, "-b", B, "-split"]))[0][4], "1")
write(A, [["chr1", 100, 200, "gene"]]); write(B, [bed12("chr1", 120, [(0, 10)])])
verdict("BT1 coverage -split -f 0.5 count", lines(run(["coverage", "-a", A, "-b", B, "-split", "-f", "0.5"]))[0][4], "0")
# BT2
write(A, [["chr1", 100, 200, "gene"]]); write(B, [bed12("chr1", 120, [(0, 50)], "r%d" % i) for i in (1, 2, 3)])
verdict("BT2 intersect -split -F 0.5 lines", len(lines(run(["intersect", "-a", A, "-b", B, "-split", "-F", "0.5", "-wa", "-wb"]))), 3)
# BT3
write(A, [["chr1", 10, 20, "a1", 1, "-"]]); write(B, [["chr1", 5, 6, "b1", 1, "+"], ["chr1", 24, 25, "b2", 1, "+"]])
verdict("BT3 closest -D a -t first", lines(run(["closest", "-a", A, "-b", B, "-D", "a", "-t", "first"]))[0][9], "b1")
# BT4
base = 1_200_000_000
write(B, [["chr1", base - 100, base + 100], ["chr1", base + 900, base + 1100]]); write(A, [["chr1", base + 50, base + 150]])
verdict("BT4 reldist -detail at 1.2e9", [l[3] for l in lines(run(["reldist", "-a", A, "-b", B, "-detail"]))], ["0.100"])
base = 3_000_000_000
write(A, [["chr1", base, base + 100]]); write(B, [["chr1", base + 10, base + 20]])
verdict("BT4 subtract at 3e9", [(int(l[1]), int(l[2])) for l in lines(run(["subtract", "-a", A, "-b", B]))], [(base, base + 10), (base + 20, base + 100)])
write(A, [["chr1", 0, 10]]); write(B, [["chr1", base + 10, base + 20]])
verdict("BT4 closest -d at gap 3e9", lines(run(["closest", "-a", A, "-b", B, "-d"]))[0][-1], str(base + 1))
write(G, [["chr1", 5_000_000_000]]); write(A, [["chr1", base, base + 100]])
verdict("BT4 flank -l 10 -r 10 at 3e9", [(int(l[1]), int(l[2])) for l in lines(run(["flank", "-i", A, "-g", G, "-l", "10", "-r", "10"]))], [(base - 10, base), (base + 100, base + 110)])
# BT5
write(G, [["chr1", 100_000_000]]); write(A, [["chr1", 1_000_000, 1_000_100]])
verdict("BT5 slop -pct -b 0.53 on 100 bp, bases added", 1_000_000 - int(lines(run(["slop", "-i", A, "-g", G, "-b", "0.53", "-pct"]))[0][1]), 53)
write(A, [["chr1", 25_000_000, 25_000_010]])
verdict("BT5 slop -b 20000001 start", int(lines(run(["slop", "-i", A, "-g", G, "-b", "20000001"]))[0][1]), 4_999_999)
# BT6
write(G, [["chr1", 10_000_000]]); write(A, [["chr1", 0, 50, "f%d" % i] for i in range(2000)]); write(B, [["chr1", 1_000_000, 1_000_100]])
rows = lines(run(["shuffle", "-i", A, "-g", G, "-incl", B, "-seed", "1"]))
verdict("BT6 shuffle -incl features past include end", sum(1 for r in rows if int(r[2]) > 1_000_100), 0)
