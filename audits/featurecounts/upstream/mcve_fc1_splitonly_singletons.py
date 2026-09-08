#!/usr/bin/env python3
"""featureCounts --splitOnly counts a non-split fragment whose mate is unmapped
(and a single-end record in a paired-end file) in `-p --countReadPairs` mode.

Usage: python3 mcve_fc1_splitonly_singletons.py [path/to/featureCounts]
"""
import os, subprocess, sys, tempfile

fc = sys.argv[1] if len(sys.argv) > 1 else "featureCounts"
d = tempfile.mkdtemp()
open(f"{d}/a.gtf", "w").write('chr1\tx\texon\t1000\t1400\t.\t+\t.\tgene_id "A";\n')
S = "A" * 40
Q = "I" * 40
open(f"{d}/a.sam", "w").write(
    "@HD\tVN:1.6\tSO:unsorted\n@SQ\tSN:chr1\tLN:10000\n"
    # read pair: first read mapped, 40M, no N; mate unmapped
    f"frag1\t73\tchr1\t1100\t60\t40M\t=\t1100\t0\t{S}\t{Q}\n"
    f"frag1\t133\tchr1\t1100\t0\t*\t=\t1100\t0\t{S}\t{Q}\n"
    # single-end record, 40M, no N
    f"se1\t0\tchr1\t1100\t60\t40M\t*\t0\t0\t{S}\t{Q}\n"
    # proper pair, both ends 40M, no N (control: excluded as expected)
    f"pair1\t99\tchr1\t1100\t60\t40M\t=\t1300\t240\t{S}\t{Q}\n"
    f"pair1\t147\tchr1\t1300\t60\t40M\t=\t1100\t-240\t{S}\t{Q}\n")
subprocess.run([fc, "-p", "--countReadPairs", "--splitOnly", "-a", f"{d}/a.gtf", "-o", f"{d}/out", f"{d}/a.sam"],
               check=True, capture_output=True)
count = [l for l in open(f"{d}/out") if l.startswith("A\t")][0].split("\t")[-1].strip()
summ = {l.split("\t")[0]: l.split("\t")[1].strip() for l in open(f"{d}/out.summary")}
print(f"{fc}: count for gene A = {count} (expected 0: no fragment has an N in its CIGAR); "
      f"Assigned={summ['Assigned']} Unassigned_NonSplit={summ['Unassigned_NonSplit']}")
