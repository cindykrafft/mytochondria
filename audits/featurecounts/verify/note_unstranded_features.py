#!/usr/bin/env python3
"""N2: features whose strand column is '.' are never counted under -s 1 and
always counted (from both strands) under -s 2.

The strand test compares the fragment strand (0/1) with the feature strand
stored as 0 (+), 1 (-) or -1 ('.'): `-s 1` requires equality, `-s 2`
inequality, so a '.' feature fails every `-s 1` test and passes every `-s 2`
test.  The manual does not say what happens to strandless features.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib

print("featureCounts", fclib.fc_version())
wd = tempfile.mkdtemp(prefix="fcn2_")
CH = {"chr1": 10000}
gtf = os.path.join(wd, "a.gtf")
fclib.write_gtf(gtf, [("PLUS", "chr1", "+", [(1000, 2000)]), ("DOT", "chr1", ".", [(3000, 4000)]),
                      ("MINUS", "chr1", "-", [(5000, 6000)])])
recs = []
for g, p in (("PLUS", 1000), ("DOT", 3000), ("MINUS", 5000)):
    for i in range(10):
        recs.append(fclib.single(f"{g}_fwd{i}", "chr1", p + 10 * i, "50M", rev=False))
        recs.append(fclib.single(f"{g}_rev{i}", "chr1", p + 10 * i, "50M", rev=True))
bam = os.path.join(wd, "a.bam")
fclib.make_bam(bam, CH, recs)
print("10 forward + 10 reverse single-end reads inside each of a '+', a '.' and a '-' feature")
for s in ("0", "1", "2"):
    counts, summary, det, _ = fclib.run_fc(gtf, bam, ["-s", s], workdir=wd)
    print(f"  -s {s}: counts {counts}")
