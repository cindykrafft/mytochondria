"""Minimal reproduction for FP2: an auto-detected built-in adapter longer than
60 bases is printed and then discarded, so nothing is trimmed.

20,000 reads (the detector needs at least 10,000) that all read through into the
TruSeq Small RNA RPI1 adapter, which is one of the 234 built-in adapters and is
63 nt long. Expected: the adapter is detected and trimmed. The same file with
the same adapter given through --adapter_sequence is the control.

Usage: python3 mcve_fp2_known_adapter_over60.py [path-to-fastp]
"""
import os
import random
import re
import subprocess
import sys
import tempfile

FASTP = sys.argv[1] if len(sys.argv) > 1 else "fastp"
RPI1 = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"  # 63 nt
random.seed(0)
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "reads.fastq")
    with open(path, "w") as f:
        for i in range(20000):
            insert = "".join(random.choice("ACGT") for _ in range(random.randint(20, 37)))
            seq = (insert + RPI1)[:100]
            f.write("@r%d\n%s\n+\n%s\n" % (i, seq, "I" * len(seq)))
    for label, args in (("auto-detection", []), ("--adapter_sequence <RPI1>", ["-a", RPI1])):
        err = subprocess.run([FASTP, "-i", path, "-o", os.path.join(tmp, "out.fastq"),
                              "-j", os.path.join(tmp, "j"), "-h", os.path.join(tmp, "h")] + args,
                             capture_output=True, text=True).stderr
        printed = re.findall(r"^[ACGT]{20,}$", err, re.M)
        trimmed = re.search(r"reads with adapter trimmed: (\d+)", err)
        print("%-26s adapter printed by fastp: %-9s | %s | reads with adapter trimmed: %s"
              % (label,
                 ("%d nt" % len(printed[0])) if printed else "none",
                 "'No adapter detected'" if "No adapter detected" in err else "adapter used",
                 trimmed.group(1) if trimmed else "?"))
    print("expected in both rows: 20000 of 20000 reads trimmed")
