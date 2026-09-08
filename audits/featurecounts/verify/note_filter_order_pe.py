#!/usr/bin/env python3
"""N1: in read-pair mode the summary category of a fragment that fails two
filters does not follow the manual's filter order.

Manual: unmapped > read type > singleton > mapping quality > chimeric >
fragment length > duplicate > multi-mapping > secondary > split ...
"An unassigned alignment ... will only be allocated to one category which is
the category corresponding to the first filter that filtered this alignment
out."

Shipped code walks the two records one after the other and tests the mapping
quality only while looking at the second one, so a pair that is both
low-MAPQ and multi-mapping / duplicate / chimeric is labelled by the later
filter.  Counts are unaffected (the fragment is dropped either way); only the
`.summary` rows move.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib

print("featureCounts", fclib.fc_version())
wd = tempfile.mkdtemp(prefix="fcn1_")
CH = {"chr1": 10000, "chr2": 10000}
gtf = os.path.join(wd, "a.gtf")
fclib.write_gtf(gtf, [("A", "chr1", "+", [(1000, 3000)])])
recs = []
recs += fclib.pair("lowQ_multi", "chr1", 1100, "50M", 1300, "50M", mapq=0, tags={"NH": 2})
recs += fclib.pair("lowQ_dup", "chr1", 1100, "50M", 1300, "50M", mapq=0, extra_flag=1024)
recs += fclib.pair("lowQ_chimeric", "chr1", 1100, "50M", 1300, "50M", mapq=0, chrom2="chr2")
recs += fclib.pair("lowQ_fraglen", "chr1", 1100, "50M", 5000, "50M", mapq=0)
recs += fclib.pair("lowQ_secondary", "chr1", 1100, "50M", 1300, "50M", mapq=0, extra_flag=256)
recs += fclib.pair("lowQ_only", "chr1", 1100, "50M", 1300, "50M", mapq=0)
recs += fclib.pair("dup_multi", "chr1", 1100, "50M", 1300, "50M", tags={"NH": 2}, extra_flag=1024)
bam = os.path.join(wd, "a.bam")
fclib.make_bam(bam, CH, recs)
args = ["-p", "--countReadPairs", "-Q", "10", "-C", "-B", "-P", "-d", "50", "-D", "600", "--ignoreDup", "--primary"]
manual = {"lowQ_multi": "Unassigned_MappingQuality", "lowQ_dup": "Unassigned_MappingQuality",
          "lowQ_chimeric": "Unassigned_MappingQuality", "lowQ_fraglen": "Unassigned_MappingQuality",
          "lowQ_secondary": "Unassigned_MappingQuality", "lowQ_only": "Unassigned_MappingQuality",
          "dup_multi": "Unassigned_Duplicate"}
counts, summary, det, _ = fclib.run_fc(gtf, bam, args, workdir=wd)
print(" ".join(args))
for n in manual:
    print(f"  {n:15s} manual order -> {manual[n]:28s} got {det[n][0]}")
print("summary:", {k: v for k, v in summary.items() if v}, "| count A =", counts["A"])
