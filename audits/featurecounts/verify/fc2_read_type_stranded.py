#!/usr/bin/env python3
"""FC2: the documented "read type" filter does not exist; single-end records
in a paired-end file are counted under stranded pair counting as if they were
first reads.

Manual (section "Read filtering"): "if there are single end reads included in
a paired end read dataset ... and reads are required to be counted in a
strand-specific manner, then all the single end reads will be excluded from
counting because their strandness cannot be determined.  However if such
reads are to be counted in an unstranded manner then all the single end reads
will be considered for counting."  The summary row for that filter is
`Unassigned_Read_Type`.

Shipped code: the counter `unassigned_read_type` is never incremented; a
single-end record in `-p --countReadPairs -s 1|2` mode is paired with an
unmapped placeholder and its own strand is taken as the fragment strand, i.e.
it is treated as a first read.  Orphan reads that came from the second read
of a pair therefore point the wrong way.

Design: gene S on the + strand and, antisense to it on the - strand, gene AS.
A dUTP library (`-s 2`: read 1 on the opposite strand of the gene): proper
pairs from S have R1 reverse / R2 forward.  Then 500 orphan single-end
records derived from R1 (reverse) and 500 derived from R2 (forward), all from
gene S, written as SAM single-end records (flag 0/16) as aligners do for
unpaired reads.
"""
import os
import random
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib

print("featureCounts", fclib.fc_version())
wd = tempfile.mkdtemp(prefix="fc2_")
CH = {"chr1": 10000}
genes = [("S", "chr1", "+", [(1000, 2000)]), ("AS", "chr1", "-", [(1000, 2000)])]
gtf = os.path.join(wd, "ann.gtf")
fclib.write_gtf(gtf, genes)
PE_ARGS = ["-p", "--countReadPairs"] if os.environ.get("FC_OLD_PE") is None else ["-p"]

rng = random.Random(1)
recs = []
for i in range(300):
    p = rng.randint(1000, 1800)
    recs += fclib.pair(f"pair{i}", "chr1", p + 100, "50M", p, "50M", r1_rev=True, r2_rev=False)  # dUTP pair from S
for i in range(500):
    recs.append(fclib.single(f"orphanR1_{i}", "chr1", rng.randint(1000, 1900), "50M", rev=True))   # from R1: reverse
for i in range(500):
    recs.append(fclib.single(f"orphanR2_{i}", "chr1", rng.randint(1000, 1900), "50M", rev=False))  # from R2: forward
rng.shuffle(recs)
bam = os.path.join(wd, "mixed.bam")
fclib.make_bam(bam, CH, recs)

for label, args in [("-s 2 (dUTP)", [*PE_ARGS, "-s", "2"]), ("-s 1", [*PE_ARGS, "-s", "1"]),
                    ("-s 0", [*PE_ARGS, "-s", "0"]), ("-s 2 -B", [*PE_ARGS, "-s", "2", "-B"])]:
    counts, summary, det, _ = fclib.run_fc(gtf, bam, args, workdir=wd)
    by = {}
    for k, v in det.items():
        grp = k.split("_")[0] if k.startswith("orphan") else "pair"
        by.setdefault(grp, {}).setdefault(v[0] + ("->" + v[2] if v[0] == "Assigned" else ""), 0)
        by[grp][v[0] + ("->" + v[2] if v[0] == "Assigned" else "")] += 1
    print(f"\n{' '.join(PE_ARGS)} {label}: counts S={counts['S']:g} AS={counts['AS']:g}; "
          f"Unassigned_Read_Type={summary['Unassigned_Read_Type']}; Unassigned_Singleton={summary['Unassigned_Singleton']}")
    for grp in ("pair", "orphanR1", "orphanR2"):
        print(f"   {grp:9s}: {by.get(grp)}")
print("\nManual: with -s 1/-s 2 the 1,000 single-end records should be excluded as Unassigned_Read_Type;")
print("with -s 0 they should be counted.  Expected S under -s 2 = 300 (pairs only).")
