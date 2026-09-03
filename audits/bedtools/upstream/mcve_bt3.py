#!/usr/bin/env python3
"""MCVE for BT3: closest -t first picks the wrong tie under -D a / -D b."""
import os, subprocess, tempfile
BT = os.environ.get("BT", "bedtools")
tmp = tempfile.mkdtemp()
def w(p, s): open(os.path.join(tmp, p), "w").write(s); return os.path.join(tmp, p)
def run(*a): 
    o = subprocess.run([BT, *a], capture_output=True, text=True).stdout.strip()
    return o.split("\t")[9] if o else "(none)"
a = w("a.bed", "chr1\t10\t20\ta1\t1\t-\n")
b = w("b.bed", "chr1\t5\t6\tb1\t1\t+\nchr1\t24\t25\tb2\t1\t+\n")
for args in (["-d", "-t", "first"], ["-D", "ref", "-t", "first"], ["-D", "a", "-t", "first"], ["-D", "a", "-t", "last"], ["-D", "b", "-t", "first"]):
    print("%-22s -> %s" % (" ".join(args), run("closest", "-a", a, "-b", b, *args)))
print("(-t first documented as the first tie in the B file = b1 in every mode)")
