#!/usr/bin/env python3
"""ILLUMINACLIP palindrome mode: a mismatch at Q19 is charged 1, not 1.9.
Usage: python3 mcve_tm1_palindrome_penalty.py <trimmomatic.jar> <adapters/TruSeq3-PE.fa>"""
import os, subprocess, sys, tempfile
jar, fa = sys.argv[1], sys.argv[2]
# 2x50 pair, 42-base insert reading through into the TruSeq3 adapters (PrefixPE/2 rc on read 1,
# PrefixPE/1 rc on read 2); read 1 carries two errors at positions 3 and 8, quality Q19 ('4').
r1 = "CAGCTTTTTATATTATGCAGAAAATCTACTTCGCCTGATACGAGATCGGA"; q1 = "III4IIII4IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"
r2 = "CGTATCAGGCGAAGTAGATTTTCTGCATAATATGAAAATCTGAGATCGGA"; q2 = "I" * 50
d = tempfile.mkdtemp()
open(os.path.join(d, "r1.fq"), "w").write("@p\n%s\n+\n%s\n" % (r1, q1))
open(os.path.join(d, "r2.fq"), "w").write("@p\n%s\n+\n%s\n" % (r2, q2))
outs = [os.path.join(d, x) for x in ("1P.fq", "1U.fq", "2P.fq", "2U.fq")]
cmd = ["java", "-jar", jar, "PE", "-threads", "1", "-phred33", os.path.join(d, "r1.fq"), os.path.join(d, "r2.fq")] + outs + ["ILLUMINACLIP:%s:2:30:10" % fa]
p = subprocess.run(cmd, capture_output=True, text=True)
print([l for l in (p.stdout + p.stderr).splitlines() if l.startswith("Input Read Pairs")][0])
print("expected: Both Surviving: 1 (58 aligned bases, 56 matches: 56*0.60206 - 2*1.9 = 29.9 < 30)")
print("got     : forward-only survivor of length %d" % len(open(outs[1]).read().split("\n")[1]) if os.path.getsize(outs[1]) else "got     : both reads kept")
