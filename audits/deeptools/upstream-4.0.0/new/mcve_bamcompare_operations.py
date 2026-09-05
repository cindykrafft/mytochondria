#!/usr/bin/env python3
"""bamCompare 4.0.0: --operation first/second/add/mean write the log2 track and
reciprocal_ratio is inverted.

Two synthetic single-end BAMs on a 300-bp chromosome (pysam), 50-bp reads:
  A: 3 reads at 0-50, 1 read at 100-150, 2 reads at 200-250
  B: 2 reads at 0-50, 3 reads at 100-150, 2 reads at 200-250
bamCompare is run with --scaleFactors 1:1, --binSize 50, --pseudocount 0 (so
that ratios are exact) and --no_collapse, for every offered --operation; the
expected values follow from the definitions in the help / 3.5.6 getRatio.py.
"""
import os
import subprocess
import sys
import tempfile
import numpy as np
import pysam

BIN = os.path.dirname(sys.executable)
d = tempfile.mkdtemp()
A_counts = np.array([3, 0, 1, 0, 2, 0], dtype=float)   # per 50-bp bin
B_counts = np.array([2, 0, 3, 0, 2, 0], dtype=float)


def write_bam(path, counts):
    with pysam.AlignmentFile(path, "wb", reference_names=["chr1"], reference_lengths=[300]) as fh:
        n = 0
        for b, c in enumerate(counts):
            for _ in range(int(c)):
                a = pysam.AlignedSegment()
                a.query_name = "r%d" % n; n += 1
                a.query_sequence = "A" * 50
                a.flag = 0; a.reference_id = 0; a.reference_start = 50 * b
                a.mapping_quality = 30; a.cigar = ((0, 50),)
                a.query_qualities = pysam.qualitystring_to_array("I" * 50)
                fh.write(a)
    pysam.index(path)


write_bam(os.path.join(d, "A.bam"), A_counts)
write_bam(os.path.join(d, "B.bam"), B_counts)
with np.errstate(divide="ignore", invalid="ignore"):
    ratio = A_counts / B_counts
    expected = {
        "log2": np.log2(ratio),
        "ratio": ratio,
        "reciprocal_ratio": np.where(ratio >= 1, ratio, -1.0 / ratio),   # a/b if a/b >= 1 else -b/a
        "subtract": A_counts - B_counts,
        "first": A_counts,
        "second": B_counts,
        "add": A_counts + B_counts,
        "mean": (A_counts + B_counts) / 2.0,
    }

print(subprocess.run([os.path.join(BIN, "bamCompare"), "--version"], capture_output=True, text=True).stdout.strip())
wrong = []
for op in ["log2", "ratio", "subtract", "reciprocal_ratio", "first", "second", "add", "mean"]:
    out = os.path.join(d, op + ".bg")
    subprocess.run([os.path.join(BIN, "bamCompare"), "-b1", os.path.join(d, "A.bam"), "-b2", os.path.join(d, "B.bam"),
                    "-o", out, "-of", "bedgraph", "--scaleFactors", "1:1", "--pseudocount", "0", "--binSize", "50",
                    "--no_collapse", "--operation", op, "-p", "1"], check=True, capture_output=True)
    got = np.array([float(l.split()[3]) for l in open(out)])
    exp = expected[op]
    ok = np.allclose(np.nan_to_num(got, nan=0, posinf=1e9, neginf=-1e9), np.nan_to_num(exp, nan=0, posinf=1e9, neginf=-1e9), atol=0.011)
    print("--operation %-16s got %-40s expected %s%s" % (op, np.round(got, 2), np.round(exp, 2), "" if ok else "   <- WRONG"))
    if not ok:
        wrong.append(op)
print("operations with wrong output:", wrong)
assert not wrong, "bamCompare --operation %s do not compute what they name" % ", ".join(wrong)
