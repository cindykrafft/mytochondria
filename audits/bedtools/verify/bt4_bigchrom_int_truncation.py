#!/usr/bin/env python3
"""BT4: coordinates are CHRPOS (int64) since 2.28 ("support for genomes with large
chromosomes"), but several tools still route them through `int`:
  reldist   LoadMidpoints: `(int)(bed.end + bed.start) / 2`  -> wrong for start+end >= 2^31
  subtract  subtractHits: keyStart/keyEnd/hitStart/hitEnd/... are `int` -> wrong for pos >= 2^31
  flank     AddFlank/AddStrandedFlank: `int chromSize`, static_cast<int>(feature.start/end)
  closest   RecDistList stores distances as `int` (`(int)dist`), INT_MAX sentinels -> wrong -d for gaps >= 2^31
Each tool is run at a small control position and above the threshold, against a port.
"""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed"); G = os.path.join(tmp, "g.genome")
write(G, [["chr1", 5_000_000_000]])

def show(label, got, exp):
    ok = got == exp
    print("   %-34s got %-48s expected %-40s %s" % (label, got, exp, "ok" if ok else "WRONG"))
    return ok

print("\n== reldist -detail: B midpoints at base and base+1000, A midpoint at base+100 -> 0.100")
for base in (1_000_000, 1_000_000_000, 1_073_741_000, 1_073_742_000, 3_000_000_000):
    write(B, [["chr1", base - 100, base + 100], ["chr1", base + 900, base + 1100]])
    write(A, [["chr1", base + 50, base + 150]])
    out = [l[3] for l in lines(run(["reldist", "-a", A, "-b", B, "-detail"]))]
    show("base %d (start+end %s 2^31)" % (base, "<" if 2 * base + 200 < 2**31 else ">="), out, ["0.100"])
print("   (threshold: start+end of a B record >= 2^31 = 2147483648, i.e. positions from 1,073,741,824)")

print("\n== subtract: A = [base, base+100) minus B = [base+10, base+20)")
for base in (1_000_000, 2_147_483_000, 2_147_484_000, 3_000_000_000):
    write(A, [["chr1", base, base + 100]]); write(B, [["chr1", base + 10, base + 20]])
    out = [(int(l[1]), int(l[2])) for l in lines(run(["subtract", "-a", A, "-b", B]))]
    show("base %d" % base, out, [(base, base + 10), (base + 20, base + 100)])

print("\n== flank -l 10 -r 10: A = [base, base+100) on a 5e9 chromosome")
for base in (1_000_000, 2_147_483_000, 2_147_484_000, 3_000_000_000):
    write(A, [["chr1", base, base + 100]])
    out = [(int(l[1]), int(l[2])) for l in lines(run(["flank", "-i", A, "-g", G, "-l", "10", "-r", "10"]))]
    show("base %d" % base, out, [(base - 10, base), (base + 100, base + 110)])
print("   flank with a chromosome size >= 2^31 but small coordinates: A = [1000, 1100)")
write(A, [["chr1", 1000, 1100]])
out = [(int(l[1]), int(l[2])) for l in lines(run(["flank", "-i", A, "-g", G, "-l", "10", "-r", "10"]))]
show("chromSize 5e9, base 1000", out, [(990, 1000), (1100, 1110)])

print("\n== closest -d: A = [0, 10), B = [gap+10, gap+20) -> distance gap+1")
for gap in (1_000_000, 2_147_483_000, 2_147_484_000, 3_000_000_000):
    write(A, [["chr1", 0, 10]]); write(B, [["chr1", gap + 10, gap + 20]])
    out = [int(l[-1]) for l in lines(run(["closest", "-a", A, "-b", B, "-d"]))]
    show("gap %d" % gap, out, [gap + 1])
print("   closest -k 2 with two B records at gaps 3e9 and 3e9+5 (order by distance)")
write(B, [["chr1", 3_000_000_010, 3_000_000_020, "near"], ["chr1", 3_000_000_015, 3_000_000_025, "far"]])
out = [(l[6], l[-1]) for l in lines(run(["closest", "-a", A, "-b", B, "-d", "-k", "2"]))]
show("gap 3e9, -k 2", out, [("near", "3000000001"), ("far", "3000000006")])

print("\n== controls at base 3e9: intersect -wo, coverage, merge -d, cluster -d, slop, window -w")
base = 3_000_000_000
write(A, [["chr1", base, base + 100]]); write(B, [["chr1", base + 10, base + 20]])
show("intersect -wo overlap", [l[-1] for l in lines(run(["intersect", "-a", A, "-b", B, "-wo"]))], ["10"])
show("coverage", [l[3:] for l in lines(run(["coverage", "-a", A, "-b", B]))], [["1", "10", "100", "0.1000000"]])
write(A, [["chr1", base, base + 100], ["chr1", base + 105, base + 200]])
show("merge -d 10", [(int(l[1]), int(l[2])) for l in lines(run(["merge", "-i", A, "-d", "10"]))], [(base, base + 200)])
show("cluster -d 10", [l[3] for l in lines(run(["cluster", "-i", A, "-d", "10"]))], ["1", "1"])
write(A, [["chr1", base, base + 100]])
show("slop -b 10", [(int(l[1]), int(l[2])) for l in lines(run(["slop", "-i", A, "-g", G, "-b", "10"]))], [(base - 10, base + 110)])
write(B, [["chr1", base + 105, base + 110]])
show("window -w 10", len(lines(run(["window", "-a", A, "-b", B, "-w", "10"]))), 1)
