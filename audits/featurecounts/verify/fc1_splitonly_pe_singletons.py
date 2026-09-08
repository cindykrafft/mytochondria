#!/usr/bin/env python3
"""FC1: `--splitOnly` does not filter singleton fragments in read-pair mode.

Manual: "--splitOnly: If specified, only split alignments (CIGAR strings
contain letter 'N') will be counted. All the other alignments will be
ignored."

In `-p --countReadPairs` mode featureCounts drops a fragment for `--splitOnly`
only after it has seen TWO mapped, non-split records; an unmapped mate never
reaches that counter, and a single-end record inside a paired-end file gets
an unmapped placeholder mate.  So every non-split fragment with exactly one
mapped record is counted as if it were split.  `--nonSplitOnly` (the mirror
option) and read-level counting (`-p` alone) behave as documented.

Part A: five hand-made fragments.  Part B: 1,000 random non-split singletons
inside one gene (plus 200 proper non-split pairs), which should all be
Unassigned_NonSplit.
"""
import os
import random
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib

print("featureCounts", fclib.fc_version())
wd = tempfile.mkdtemp(prefix="fc1_")
CH = {"chr1": 10000}
genes = [("A", "chr1", "+", [(1000, 1400)]), ("B", "chr1", "+", [(2000, 2100), (2700, 2800)])]
gtf = os.path.join(wd, "ann.gtf")
fclib.write_gtf(gtf, genes)
PE_ARGS = ["-p", "--countReadPairs"] if os.environ.get("FC_OLD_PE") is None else ["-p"]

# ---------------------------------------------------------------- Part A
recs = []
recs += fclib.pair("pair_nonsplit", "chr1", 1050, "40M", 1200, "40M")            # both ends non-split -> NonSplit
recs += fclib.pair("pair_split", "chr1", 2080, "20M600N20M", 2020, "40M")        # one end split -> Assigned B
recs += [dict(name="singleton_nonsplit", flag=1 | 8 | 64, chrom="chr1", pos=1100, cigar="40M", mapq=60,
              mchrom="chr1", mpos=1100, tlen=0),
         dict(name="singleton_nonsplit", flag=1 | 4 | 128, chrom="chr1", pos=1100, mapq=0, mchrom="chr1",
              mpos=1100, tlen=0, readlen=40)]                                     # mate unmapped, read non-split
recs += [dict(name="singleton_split", flag=1 | 8 | 64, chrom="chr1", pos=2080, cigar="20M600N20M", mapq=60,
              mchrom="chr1", mpos=2080, tlen=0),
         dict(name="singleton_split", flag=1 | 4 | 128, chrom="chr1", pos=2080, mapq=0, mchrom="chr1",
              mpos=2080, tlen=0, readlen=40)]
recs += [fclib.single("se_read_nonsplit", "chr1", 1100, "40M")]                   # single-end record in the PE file
bam = os.path.join(wd, "a.bam")
fclib.make_bam(bam, CH, recs)

print("\nPart A: --splitOnly, five fragments (manual: only alignments whose CIGAR contains N are counted)")
for label, args in [("-p --countReadPairs --splitOnly", [*PE_ARGS, "--splitOnly"]),
                    ("-p --countReadPairs --nonSplitOnly", [*PE_ARGS, "--nonSplitOnly"]),
                    ("-p --splitOnly (read-level counting)", ["-p", "--splitOnly"])]:
    if os.environ.get("FC_OLD_PE") and "read-level" in label:
        continue
    counts, summary, det, _ = fclib.run_fc(gtf, bam, args, workdir=wd)
    print(f"  {label}")
    for name in ["pair_nonsplit", "pair_split", "singleton_nonsplit", "singleton_split", "se_read_nonsplit"]:
        print(f"    {name:22s} -> {det[name][0]:28s} targets={det[name][2]}")
    print(f"    counts A={counts['A']:g} B={counts['B']:g}; summary Assigned={summary['Assigned']} "
          f"NonSplit={summary.get('Unassigned_NonSplit', summary.get('Unassigned_Split'))}")

# ---------------------------------------------------------------- Part B
rng = random.Random(0)
recs = []
for i in range(1000):
    p = rng.randint(1000, 1360)
    r1 = rng.random() < 0.5
    recs += [dict(name=f"s{i}", flag=1 | 8 | (64 if r1 else 128) | (16 if rng.random() < 0.5 else 0), chrom="chr1",
                  pos=p, cigar="40M", mapq=60, mchrom="chr1", mpos=p, tlen=0),
             dict(name=f"s{i}", flag=1 | 4 | (128 if r1 else 64), chrom="chr1", pos=p, mapq=0, mchrom="chr1",
                  mpos=p, tlen=0, readlen=40)]
for i in range(200):
    p = rng.randint(1000, 1300)
    recs += fclib.pair(f"p{i}", "chr1", p, "40M", p + 60, "40M")
rng.shuffle(recs)
bam = os.path.join(wd, "b.bam")
fclib.make_bam(bam, CH, recs)
counts, summary, det, _ = fclib.run_fc(gtf, bam, [*PE_ARGS, "--splitOnly"], workdir=wd)
n_single_assigned = sum(1 for k, v in det.items() if k.startswith("s") and v[0] == "Assigned")
n_pair_assigned = sum(1 for k, v in det.items() if k.startswith("p") and v[0] == "Assigned")
print(f"\nPart B: 1000 non-split singletons + 200 non-split proper pairs in gene A, {' '.join(PE_ARGS)} --splitOnly")
print(f"  expected count for A: 0 (no fragment carries an N);  got A={counts['A']:g}")
print(f"  singletons Assigned: {n_single_assigned}/1000;  proper pairs Assigned: {n_pair_assigned}/200")
print(f"  summary: {dict((k, v) for k, v in summary.items() if v)}")
