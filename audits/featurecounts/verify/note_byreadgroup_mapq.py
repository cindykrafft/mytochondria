#!/usr/bin/env python3
"""N3: with --byReadGroup the Unassigned_MappingQuality row of every read
group is 0, so the per-group summary columns no longer sum to the group's
reads; the reads dropped by -Q are not attributed to any group.

Every other filter routes its counter through the read group's own table;
the mapping-quality branch increments the thread-level counter only.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib
import pysam

print("featureCounts", fclib.fc_version())
wd = tempfile.mkdtemp(prefix="fcn3_")
CH = {"chr1": 10000}
gtf = os.path.join(wd, "a.gtf")
fclib.write_gtf(gtf, [("A", "chr1", "+", [(1000, 2000)])])
bam = os.path.join(wd, "a.bam")
header = {"HD": {"VN": "1.6"}, "SQ": [{"SN": "chr1", "LN": 10000}],
          "RG": [{"ID": "g1", "SM": "s1"}, {"ID": "g2", "SM": "s2"}]}
with pysam.AlignmentFile(bam, "wb", header=header) as f:
    for i in range(40):
        a = pysam.AlignedSegment(f.header)
        a.query_name = f"r{i}"
        a.reference_id = 0
        a.reference_start = 1000 + i
        a.cigarstring = "50M"
        a.query_sequence = "A" * 50
        a.query_qualities = pysam.qualitystring_to_array("I" * 50)
        a.mapping_quality = 60 if i % 4 else 0          # every 4th read has MAPQ 0
        a.set_tag("RG", "g1" if i < 20 else "g2")
        a.flag = 1024 if i % 10 == 1 else 0              # one duplicate per ten
        f.write(a)
out = os.path.join(wd, "c.txt")
import subprocess
subprocess.run([fclib.FC, "-a", gtf, "-o", out, "--byReadGroup", "-Q", "10", "--ignoreDup", bam],
               capture_output=True, text=True, check=True)
print("40 reads: 20 in RG g1, 20 in g2; 10 have MAPQ 0, 4 are duplicates; --byReadGroup -Q 10 --ignoreDup")
with open(out + ".summary") as f:
    print(f.read())
with open(out) as f:
    print([l for l in f if not l.startswith("#")][-1].strip())
