#!/usr/bin/env python3
"""Notes N2-N8, each executed on the shipped binary:
  N2 subtract -N uses a strict '>' where -A/-f uses '>=' (exactly 50 % covered)
  N3 window -sw treats an unstranded A record as reverse strand (window flipped)
  N4 genomecov -5/-3 on an unstranded BED record uses the reverse-strand end
  N5 genomecov gives a zero-length record two bases of coverage
  N6 genomecov -scale prints with 6 significant digits (scientific notation above 1e6)
  N7 nuc -pattern counts overlapping occurrences
  N8 map -o count reports 0, not -null, for A records without hits; -prec help says 5, code default 10
"""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed"); G = os.path.join(tmp, "g.genome"); FA = os.path.join(tmp, "n.fa")

print("\n== N2 subtract: A = [100,200), B = [100,150) covers exactly 50 %")
write(A, [["chr1", 100, 200]]); write(B, [["chr1", 100, 150]])
print("   -A -f 0.5 -> %d line(s) (A removed)" % len(lines(run(["subtract", "-a", A, "-b", B, "-A", "-f", "0.5"]))))
print("   -N -f 0.5 -> %d line(s) (A kept: pctCovered > fraction is strict)" % len(lines(run(["subtract", "-a", A, "-b", B, "-N", "-f", "0.5"]))))
print("   -N -f 0.49 -> %d line(s)" % len(lines(run(["subtract", "-a", A, "-b", B, "-N", "-f", "0.49"]))))

print("\n== N3 window -sw -l 10 -r 0: A = [100,200) with no strand column; B left [90,95) and right [205,210)")
write(A, [["chr1", 100, 200]]); write(B, [["chr1", 90, 95, "left"], ["chr1", 205, 210, "right"]])
print("   unstranded A -> hits %s (window extended to the right, i.e. treated as '-')" % [l[-1] for l in lines(run(["window", "-a", A, "-b", B, "-l", "10", "-r", "0", "-sw"]))])
write(A, [["chr1", 100, 200, "x", 0, "+"]])
print("   A on '+'     -> hits %s" % [l[-1] for l in lines(run(["window", "-a", A, "-b", B, "-l", "10", "-r", "0", "-sw"]))])
write(A, [["chr1", 100, 200, "x", 0, "."]])
print("   A strand '.' -> hits %s" % [l[-1] for l in lines(run(["window", "-a", A, "-b", B, "-l", "10", "-r", "0", "-sw"]))])

print("\n== N4 genomecov -5 / -3 -bg on an unstranded BED record [100,110)")
write(G, [["chr1", 1000]]); write(A, [["chr1", 100, 110]])
print("   -5 -> %s (start 100 would be the '+' 5' end)" % lines(run(["genomecov", "-i", A, "-g", G, "-5", "-bg"])))
print("   -3 -> %s" % lines(run(["genomecov", "-i", A, "-g", G, "-3", "-bg"])))
write(A, [["chr1", 100, 110, "x", 0, "+"]])
print("   -5 on '+' -> %s" % lines(run(["genomecov", "-i", A, "-g", G, "-5", "-bg"])))

print("\n== N5 genomecov -bg on a zero-length record chr1 100 100")
write(A, [["chr1", 100, 100]])
print("   -> %s (two bases; the parser widens zero-length records to [start-1, end+1))" % lines(run(["genomecov", "-i", A, "-g", G, "-bg"])))

print("\n== N6 genomecov -scale: depth 3 on [0,10)")
write(A, [["chr1", 0, 10]] * 3)
for sc in ("0.5", "1234567.5", "333333.33"):
    print("   -scale %-10s -> %s" % (sc, lines(run(["genomecov", "-i", A, "-g", G, "-bg", "-scale", sc]))[0][3]))

print("\n== N7 nuc -pattern AA on AAAAGC")
write(FA, [[">chr1"], ["AAAAGC"]]); write(A, [["chr1", 0, 6]])
print("   user_patt_count = %s (3 = overlapping occurrences; 2 non-overlapping)" % lines(run(["nuc", "-fi", FA, "-bed", A, "-pattern", "AA"]))[-1][-1])

print("\n== N8 map -o count / -null on an A record without hits; -prec default")
write(A, [["chr1", 0, 100], ["chr1", 500, 600]]); write(B, [["chr1", 10, 20, "x", 5]])
for op in ("sum", "count", "mean", "collapse"):
    print("   -o %-8s -null NA -> %s" % (op, [l[3] for l in lines(run(["map", "-a", A, "-b", B, "-o", op, "-null", "NA"]))]))
write(B, [["chr1", 10, 20, "x", "0.1234567891234"]])
print("   -o sum of 0.1234567891234 -> %s (KeyListOps.h DEFAULT_PRECISION = 10; help text says 5)" % lines(run(["map", "-a", A, "-b", B, "-o", "sum"]))[0][3])
