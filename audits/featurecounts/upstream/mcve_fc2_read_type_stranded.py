#!/usr/bin/env python3
"""featureCounts counts single-end records in a paired-end file under
`-p --countReadPairs -s 2` as first reads instead of excluding them as
Unassigned_Read_Type (users guide, "Read filtering").

Usage: python3 mcve_fc2_read_type_stranded.py [path/to/featureCounts]
"""
import os, subprocess, sys, tempfile

fc = sys.argv[1] if len(sys.argv) > 1 else "featureCounts"
d = tempfile.mkdtemp()
# gene S on +, gene AS antisense to it on -
open(f"{d}/a.gtf", "w").write('chr1\tx\texon\t1000\t2000\t.\t+\t.\tgene_id "S";\n'
                              'chr1\tx\texon\t1000\t2000\t.\t-\t.\tgene_id "AS";\n')
S = "A" * 50
Q = "I" * 50
open(f"{d}/a.sam", "w").write(
    "@HD\tVN:1.6\tSO:unsorted\n@SQ\tSN:chr1\tLN:10000\n"
    # dUTP pair from gene S: first read reverse, second read forward
    f"pair1\t83\tchr1\t1200\t60\t50M\t=\t1100\t-150\t{S}\t{Q}\n"
    f"pair1\t163\tchr1\t1100\t60\t50M\t=\t1200\t150\t{S}\t{Q}\n"
    # orphaned second read of another fragment from S, written single-end (forward)
    f"orphanR2\t0\tchr1\t1300\t60\t50M\t*\t0\t0\t{S}\t{Q}\n"
    # orphaned first read of a fragment from S, written single-end (reverse)
    f"orphanR1\t16\tchr1\t1400\t60\t50M\t*\t0\t0\t{S}\t{Q}\n")
subprocess.run([fc, "-p", "--countReadPairs", "-s", "2", "-a", f"{d}/a.gtf", "-o", f"{d}/out", f"{d}/a.sam"],
               check=True, capture_output=True)
counts = {l.split("\t")[0]: l.split("\t")[-1].strip() for l in open(f"{d}/out") if not l.startswith(("#", "Geneid"))}
summ = {l.split("\t")[0]: l.split("\t")[1].strip() for l in open(f"{d}/out.summary")}
print(f"{fc}: S={counts['S']} AS={counts['AS']} Unassigned_Read_Type={summ['Unassigned_Read_Type']} "
      f"(manual: S=1, AS=0, Unassigned_Read_Type=2)")
