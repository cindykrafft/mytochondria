#!/usr/bin/env python3
"""New on 4.0.0: bamCompare --operation first/second/add/mean write the log2 track.

src/calc.rs calc_ratio matches "log2", "ratio", "reciprocal_ratio" and "subtract"
and computes log2 in its catch-all arm; the CLI (bamCompare2.py) still offers
all eight operations. Its reciprocal_ratio arm returns b/a when a/b >= 1 and -a/b
otherwise, where 3.5.6 (getRatio.py) returned a/b when a/b >= 1 and -b/a otherwise. Runs the shipped testA.bam / testB.bam through every
operation with --scaleFactors 1:1 and prints the bedGraph lines; the expected
values follow from bamCoverage's tracks (A: 100-200 = 1; B: 50-150 = 1,
150-200 = 2) with the default pseudocount 1 where it applies.
"""
import os
import sys
import subprocess
import _synth as S

print(S.version())
import deeptools
T = os.path.join(os.path.dirname(deeptools.__file__), "test", "test_data")
d = S.tmpdir()
expected = {
    "log2": "3R 0 50 0 | 3R 50 100 -1 | 3R 100 150 0 | 3R 150 200 -0.58",
    "ratio": "3R 0 50 1 | 3R 50 100 0.5 | 3R 100 150 1 | 3R 150 200 0.67",
    "subtract": "3R 0 50 0 | 3R 50 100 -1 | 3R 100 150 0 | 3R 150 200 -1",
    "reciprocal_ratio": "3R 0 50 1 | 3R 50 100 -2 | 3R 100 150 1 | 3R 150 200 -1.5",
    "first": "3R 0 100 0 | 3R 100 200 1",
    "second": "3R 0 50 0 | 3R 50 150 1 | 3R 150 200 2",
    "add": "3R 0 50 0 | 3R 50 100 1 | 3R 100 150 2 | 3R 150 200 3",
    "mean": "3R 0 50 0 | 3R 50 100 0.5 | 3R 100 150 1 | 3R 150 200 1.5",
}
outs = {}
for op in ["log2", "ratio", "subtract", "reciprocal_ratio", "first", "second", "add", "mean"]:
    out = os.path.join(d, op + ".bg")
    S.run(["bamCompare", "-b1", os.path.join(T, "testA.bam"), "-b2", os.path.join(T, "testB.bam"), "-o", out, "-of", "bedgraph",
           "--scaleFactors", "1:1", "--operation", op, "-p", 1])
    outs[op] = " | ".join(l.strip().replace("\t", " ") for l in open(out))
    flag = "" if op not in expected else ("  <- expected: %s" % expected[op] if outs[op] != expected[op] else "  (as expected)")
    print("--operation %-16s %s%s" % (op, outs[op], flag))
print("\nidentical to the log2 output:", [op for op in outs if op != "log2" and outs[op] == outs["log2"]])
