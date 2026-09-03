#!/usr/bin/env python3
"""MCVE for BT2 (#1142): intersect -split -F uses a summed denominator."""
import os, subprocess, tempfile
BT = os.environ.get("BT", "bedtools")
tmp = tempfile.mkdtemp()
def w(p, s): open(os.path.join(tmp, p), "w").write(s); return os.path.join(tmp, p)
def run(*a): return len([l for l in subprocess.run([BT, *a], capture_output=True, text=True).stdout.splitlines() if l])
a = w("a.bed", "chr1\t100\t200\tgene\n")
b = w("b.bed12", "".join("chr1\t120\t170\tr%d\t0\t+\t120\t170\t0\t1\t50\t0\n" % i for i in (1, 2, 3)))
print("three reads 100%% inside A:")
print("  -split -F 0.5 :", run("intersect", "-a", a, "-b", b, "-split", "-F", "0.5", "-wa", "-wb"), "lines  (expected 3)")
print("        -F 0.5 :", run("intersect", "-a", a, "-b", b, "-F", "0.5", "-wa", "-wb"), "lines  (no -split)")
print("  -split -F 0.33:", run("intersect", "-a", a, "-b", b, "-split", "-F", "0.33", "-wa", "-wb"), "lines  (break at 50/150)")
