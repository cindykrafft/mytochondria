#!/usr/bin/env python3
"""MCVE for BT4: reldist/subtract/flank/closest -d truncate coords on a 5-Gb chrom."""
import os, subprocess, tempfile
BT = os.environ.get("BT", "bedtools")
tmp = tempfile.mkdtemp()
def w(p, s): open(os.path.join(tmp, p), "w").write(s); return os.path.join(tmp, p)
def run(*a): return subprocess.run([BT, *a], capture_output=True, text=True).stdout.strip() or "(no output)"
g = w("big.genome", "chr1\t5000000000\n")
b = w("b.bed", "chr1\t2999999900\t3000000100\nchr1\t3000000900\t3000001100\n"); a = w("a.bed", "chr1\t3000000050\t3000000150\n")
print("reldist -detail:", run("reldist", "-a", a, "-b", b, "-detail"), " (expected ...0.100)")
a = w("a.bed", "chr1\t3000000000\t3000000100\n"); b = w("b.bed", "chr1\t3000000010\t3000000020\n")
print("subtract       :", run("subtract", "-a", a, "-b", b).replace("\n", " | "), " (expected two positive pieces)")
print("flank -l10 -r10:", run("flank", "-i", a, "-g", g, "-l", "10", "-r", "10").replace("\n", " | "), " (expected 2999999990-3000000000, 3000000100-3000000110)")
a = w("a.bed", "chr1\t0\t10\n")
print("closest -d     :", run("closest", "-a", a, "-b", b, "-d").split("\t")[-1], " (expected 3000000001)")
