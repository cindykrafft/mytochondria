"""Minimal reproduction for FP1: --cut_front together with --trim_front1 drops
cut_window_size-1 extra bases.

One 60 nt read whose every base is Q40 ('I'), so no sliding window can have a
mean quality below the threshold and the only thing that may shorten the read is
--trim_front1. Expected output: 55 nt. The 3' mirror (--cut_tail with
--trim_tail1) is included as the second case.

Usage: python3 mcve_fp1_cut_front_trim_front.py [path-to-fastp]
"""
import os
import subprocess
import sys
import tempfile

FASTP = sys.argv[1] if len(sys.argv) > 1 else "fastp"
read = "ACGT" * 15                       # 60 nt
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write("@r1\n%s\n+\n%s\n" % (read, "I" * 60))
    for label, args in (("--cut_front -f 5", ["--cut_front", "-f", "5"]),
                        ("--cut_tail  -t 5", ["--cut_tail", "-t", "5"]),
                        ("-f 5 (control)  ", ["-f", "5"])):
        out = os.path.join(tmp, "out.fastq")
        subprocess.run([FASTP, "-i", path, "-o", out, "-j", os.path.join(tmp, "j"),
                        "-h", os.path.join(tmp, "h")] + args,
                       capture_output=True, text=True)
        seq = open(out).read().splitlines()[1]
        print("%s: output read is %d nt (expected 55)" % (label, len(seq)))
