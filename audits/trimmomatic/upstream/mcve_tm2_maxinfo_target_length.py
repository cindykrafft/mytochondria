#!/usr/bin/env python3
"""MAXINFO with targetLength >= 248 at strictness 0.1 (or >= 711 at any strictness) trims
every read to one base.  Usage: python3 mcve_tm2_maxinfo_target_length.py <trimmomatic.jar>"""
import os, subprocess, sys, tempfile
jar = sys.argv[1]
d = tempfile.mkdtemp()
open(os.path.join(d, "in.fq"), "w").write("@r\n%s\n+\n%s\n" % ("ACGT" * 75, "I" * 300))   # one 300-nt read, all Q40
for step in ("MAXINFO:247:0.1", "MAXINFO:248:0.1", "MAXINFO:250:0.1", "MAXINFO:800:0.5"):
    out = os.path.join(d, "out.fq")
    subprocess.run(["java", "-jar", jar, "SE", "-threads", "1", "-phred33", os.path.join(d, "in.fq"), out, step], capture_output=True)
    print("%-16s expected 300 bases kept, got %d" % (step, len(open(out).read().split("\n")[1])))
