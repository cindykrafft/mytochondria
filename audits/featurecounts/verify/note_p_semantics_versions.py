#!/usr/bin/env python3
"""N4: the same command line, `featureCounts -p`, counts fragments in 2.0.1
and reads in 2.0.3+ (the 2.0.2 change that introduced --countReadPairs).

Runs one paired-end file with `-p` and, where the option exists, with
`-p --countReadPairs`, on the binary named by $FEATURECOUNTS.
"""
import os
import random
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib

print("featureCounts", fclib.fc_version())
wd = tempfile.mkdtemp(prefix="fcn4_")
CH = {"chr1": 10000}
gtf = os.path.join(wd, "a.gtf")
fclib.write_gtf(gtf, [("A", "chr1", "+", [(1000, 3000)]), ("B", "chr1", "+", [(2900, 4000)])])
rng = random.Random(5)
recs = []
for i in range(500):
    p = rng.randint(1000, 3800)
    recs += fclib.pair(f"p{i}", "chr1", p, "50M", min(p + 150, 3950), "50M")
bam = os.path.join(wd, "a.bam")
fclib.make_bam(bam, CH, recs)
for args in (["-p"], ["-p", "--countReadPairs"]):
    try:
        counts, summary, _, _ = fclib.run_fc(gtf, bam, args, core=False, workdir=wd)
        print(f"  {' '.join(args):22s}: counts {counts}; Assigned={summary['Assigned']} "
              f"Ambiguity={summary['Unassigned_Ambiguity']} (500 pairs in the file)")
    except RuntimeError as e:
        print(f"  {' '.join(args):22s}: {'option not recognised' if 'unrecognized' in str(e) else str(e).splitlines()[0]}")
