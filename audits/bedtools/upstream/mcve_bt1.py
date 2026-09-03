#!/usr/bin/env python3
"""MCVE for BT1: coverage -split counts blocks, not records, and ignores -f.
Synthetic data made here; run with the bedtools under test on PATH (BT env var
overrides)."""
import os, subprocess, tempfile
BT = os.environ.get("BT", "bedtools")
tmp = tempfile.mkdtemp()
def w(p, s): open(os.path.join(tmp, p), "w").write(s); return os.path.join(tmp, p)
def run(*a): return subprocess.run([BT, *a], capture_output=True, text=True).stdout.strip()
a = w("a.bed", "chr1\t100\t1000\tgene\n")
b = w("b.bed12", "chr1\t150\t900\tread\t0\t+\t150\t900\t0\t2\t100,100\t0,650\n")
print("coverage -split      :", run("coverage", "-a", a, "-b", b, "-split"), "  (count 2; expected 1)")
print("intersect -c -split  :", run("intersect", "-a", a, "-b", b, "-split", "-c"), "  (1 record)")
a2 = w("a2.bed", "chr1\t100\t200\tgene\n")
b2 = w("b2.bed12", "chr1\t120\t130\tr\t0\t+\t120\t130\t0\t1\t10\t0\n")
print("coverage -split -f0.5:", run("coverage", "-a", a2, "-b", b2, "-split", "-f", "0.5"), "  (10% read still counted; expected 0/0)")
