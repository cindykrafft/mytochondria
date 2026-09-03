#!/usr/bin/env python3
"""MCVE for BT5: slop -pct / flank -pct lose one base; -b rounds above 2^24."""
import os, subprocess, tempfile
BT = os.environ.get("BT", "bedtools")
tmp = tempfile.mkdtemp()
def w(p, s): open(os.path.join(tmp, p), "w").write(s); return os.path.join(tmp, p)
def run(*a): return subprocess.run([BT, *a], capture_output=True, text=True).stdout.strip()
g = w("g.genome", "chr1\t100000000\n"); a = w("a.bed", "chr1\t1000000\t1000100\n")
s = run("slop", "-i", a, "-g", g, "-b", "0.53", "-pct").split("\t")
print("slop -pct -b 0.53 on 100 bp:", s, "-> added", 1000000 - int(s[1]), "each side (expected 53)")
f = run("flank", "-i", a, "-g", g, "-l", "0.53", "-r", "0", "-pct").split("\t")
print("flank -pct -l 0.53 -r 0    :", f, "-> length", int(f[2]) - int(f[1]), "(expected 53)")
a = w("a.bed", "chr1\t25000000\t25000010\n")
print("slop -b 20000001           :", run("slop", "-i", a, "-g", g, "-b", "20000001"), "(expected 4999999-45000011)")
