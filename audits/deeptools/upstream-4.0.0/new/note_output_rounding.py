#!/usr/bin/env python3
"""4.0.0 bamCoverage/bamCompare round every output value to two decimals.

One synthetic single-end BAM (pysam): one 50-bp read per 50-bp bin on a
1,000-bp chromosome (20 reads).  --scaleFactor s stands in for the CPM factor
1e6 / mapped reads of a deep library (s = 0.004 is one read in 250 M mapped
reads; s = 0.034 one read in ~29 M).  Printed: the value written for a
one-read bin by bamCoverage (4.0.0, Rust) and bamCoverage_old (3.5.6 path),
and the same for a bamCompare log2 ratio of 1.03 (A = 1.03 B after scaling).
"""
import os
import subprocess
import sys
import tempfile
import numpy as np
import pysam

BIN = os.path.dirname(sys.executable)
d = tempfile.mkdtemp()
bam = os.path.join(d, "a.bam")
with pysam.AlignmentFile(bam, "wb", reference_names=["chr1"], reference_lengths=[1000]) as fh:
    for i in range(20):
        a = pysam.AlignedSegment()
        a.query_name = "r%d" % i; a.query_sequence = "A" * 50; a.flag = 0; a.reference_id = 0
        a.reference_start = 50 * i; a.mapping_quality = 30; a.cigar = ((0, 50),)
        a.query_qualities = pysam.qualitystring_to_array("I" * 50)
        fh.write(a)
pysam.index(bam)


def first_value(tool, args):
    out = os.path.join(d, "o.bg")
    subprocess.run([os.path.join(BIN, tool)] + args + ["-o", out, "-of", "bedgraph", "-bs", "50", "-p", "1"], check=True, capture_output=True)
    return open(out).readline().split()[3]


print("scale factor s   bamCoverage 4.0.0   bamCoverage_old   exact 1*s   relative error 4.0.0")
for s in ["0.5", "0.034", "0.012", "0.004", "0.001"]:
    v4 = first_value("bamCoverage", ["-b", bam, "--scaleFactor", s])
    v3 = first_value("bamCoverage_old", ["-b", bam, "--scaleFactor", s])
    print("%-16s %-19s %-17s %-11s %.0f %%" % (s, v4, v3, s, 100 * abs(float(v4) - float(s)) / float(s)))
print()
print("bamCompare log2 of a 1.03-fold change (--scaleFactors 1.03:1 on the same file, pseudocount 0):")
v4 = first_value("bamCompare", ["-b1", bam, "-b2", bam, "--scaleFactors", "1.03:1", "--pseudocount", "0"])
v3 = first_value("bamCompare_old", ["-b1", bam, "-b2", bam, "--scaleFactors", "1.03:1", "--pseudocount", "0"])
print("   4.0.0: %s   3.5.6 path: %s   exact: %.5f" % (v4, v3, np.log2(1.03)))
