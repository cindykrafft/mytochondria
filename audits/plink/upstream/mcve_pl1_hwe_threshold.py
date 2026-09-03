#!/usr/bin/env python3
"""MCVE for the PLINK 1.9 --hwe boundary defect: one variant with genotype counts
(2 het, 2 hom, 2 hom), exact HWE p = 185/385 = 0.48052.  --hardy prints 0.4805;
--hwe 0.48 removes it although 0.4805 > 0.48.  Usage: mcve_pl1_hwe_threshold.py <plink 1.9 binary>"""
import os, subprocess, sys, tempfile
plink = sys.argv[1]
d = tempfile.mkdtemp()
open(f"{d}/x.map", "w").write("1\tsnp1\t0\t1000\n1\tsnp2\t0\t2000\n")
# snp1: 2 het, 2 hom, 2 hom; snp2: a filler variant in HWE so that the --hwe run keeps at least one variant
open(f"{d}/x.ped", "w").write("".join(f"F{i} I{i} 0 0 2 -9 {g} {f}\n" for i, (g, f) in enumerate(zip(["A A", "A A", "A T", "A T", "T T", "T T"], ["A A", "A T", "T T", "A A", "A T", "A A"]), 1)))
subprocess.run([plink, "--file", f"{d}/x", "--hardy", "--out", f"{d}/h"], capture_output=True)
print(open(f"{d}/h.hwe").read().splitlines()[1])                       # snp1 row: P = 0.4805
subprocess.run([plink, "--file", f"{d}/x", "--hwe", "0.48", "--write-snplist", "--out", f"{d}/w"], capture_output=True)
kept = open(f"{d}/w.snplist").read().split()
print("kept after --hwe 0.48:", kept)
print("expected: ['snp1', 'snp2']  (exact p = 185/385 = 0.480519 > 0.48)")
assert "snp1" in kept, "snp1 removed although its HWE p-value is above the threshold"
