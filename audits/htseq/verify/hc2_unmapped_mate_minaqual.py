#!/usr/bin/env python3
"""HC2: a read pair whose second mate is unmapped but present in the file is
discarded as `__too_low_aQual` under the default `-a 10`.

`_assess_pe_read` (HTSeq/scripts/count_features/count_features_per_file.py)
tests `(r[0] and r[0].aQual < minaqual) or (r[1] and r[1].aQual < minaqual)`
without checking that the mate is aligned. Aligners write MAPQ 0 on unmapped
records (STAR, HISAT2, BWA, Bowtie2), so the unmapped mate fails the -a test
and the whole pair is skipped. The FAQ in doc/htseqcount.rst says: "What
happened if the mate of an aligned read is not aligned? For the default mode
union, only the aligned read determines how the read pair is counted." The
same pair counts when the unmapped mate is simply absent from the file
(`(r[0], None)`), and when `-a 0` is given.

Part A: minimal -- three pairs in gene A: (mate 1 MAPQ 60, mate 2 unmapped
MAPQ 0), (mate 1 MAPQ 60, mate 2 absent from the file), (both MAPQ 60).
Part B: a 2,000-pair library, HISAT2/BWA-style with 6 % one-mate-unmapped
pairs, counted with -a 10 (default), -a 0, and with the unmapped records
stripped from the file, name- and position-sorted.
"""
import os
import random
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import HTSeq  # noqa: E402
from htseq_port import Rec, SPECIAL, per_base_sets, port_count, run_htseq_count, write_bams, write_gtf  # noqa: E402

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0])
tmp = tempfile.mkdtemp()


def pair(name, chrom, s1, s2, mapq1=60, mapq2=60, mate2="mapped"):
    """mate2: 'mapped' | 'unmapped' (record present, placed at mate 1) | 'absent'."""
    r1 = Rec(name, chrom, s1, [("M", 50)], "+", mapq=mapq1, paired=True, which=1)
    if mate2 == "mapped":
        r2 = Rec(name, chrom, s2, [("M", 50)], "-", mapq=mapq2, paired=True, which=2)
        r1.mate_chrom, r1.mate_start, r1.mate_strand = chrom, s2, "-"
        r2.mate_chrom, r2.mate_start, r2.mate_strand = chrom, s1, "+"
        t = max(s1, s2) + 50 - min(s1, s2)
        r1.tlen, r2.tlen = (t, -t) if s1 <= s2 else (-t, t)
        return [r1, r2], (r1, r2)
    if mate2 == "unmapped":
        r2 = Rec(name, paired=True, which=2)
        r2.placed_at = (chrom, s1)
        r2.mate_chrom, r2.mate_start, r2.mate_strand = chrom, s1, "+"
        r1.mate_unmapped, r1.mate_chrom, r1.mate_start = True, chrom, s1
        return [r1, r2], (r1, r2)
    r1.mate_chrom, r1.mate_start, r1.mate_strand, r1.tlen = chrom, s1 + 300, "-", 350
    return [r1], (r1,)


# ------------------------------------------------------------- Part A
print("\n== A. minimal: gene A = chr1:[1000,2000)+, three pairs whose mate 1 (MAPQ 60) lies in A")
gtf = os.path.join(tmp, "a.gtf")
write_gtf(gtf, [("chr1", 1000, 2000, "+", "exon", {"gene_id": "A"})])
recs = []
for name, kind in (("mate2_unmapped_in_file", "unmapped"), ("mate2_absent", "absent"), ("both_mapped", "mapped")):
    rr, _ = pair(name, "chr1", 1100, 1400, mate2=kind)
    recs += rr
name_bam, pos_bam = write_bams(os.path.join(tmp, "a"), recs, {"chr1": 5000})
import pysam  # noqa: E402
print("  records:", [(r.query_name, "flag", r.flag, "MAPQ", r.mapping_quality) for r in pysam.AlignmentFile(name_bam)])
for a in ("10", "0"):
    for order, bam in (("name", name_bam), ("pos", pos_bam)):
        cli, _ = run_htseq_count(bam, gtf, ["-s", "yes", "-a", a, "-r", order, "-o", os.path.join(tmp, "a.sam")])
        xf = {}
        for line in open(os.path.join(tmp, "a.sam")):  # text parse: old versions write the SAM without a header
            if line.startswith("@"):
                continue
            fields = line.rstrip("\n").split("\t")
            xf.setdefault(fields[0], next((f[5:] for f in fields[11:] if f.startswith("XF:Z:")), None))
        print(f"  -a {a:2s} -r {order}: A = {cli['A']:g}, __too_low_aQual = {cli['__too_low_aQual']:g}; XF: {xf}")

# ------------------------------------------------------------- Part B
print("\n== B. 2,000 pairs, 6 % with an unmapped mate 2 (record present, MAPQ 0), all mate-1 MAPQ 60, 20 genes")
rng = random.Random(5)
features = [("chr1", 1000 + 3000 * g, 1000 + 3000 * g + 1500, "+", "exon", {"gene_id": f"G{g:02d}"}) for g in range(20)]
gtf = os.path.join(tmp, "b.gtf")
write_gtf(gtf, features)
recs, units, recs_stripped = [], [], []
n_unmapped_mate = 0
for i in range(2000):
    g = rng.randrange(20)
    s1 = 1000 + 3000 * g + rng.randint(0, 1400)
    kind = "unmapped" if rng.random() < 0.06 else "mapped"
    rr, u = pair(f"p{i}", "chr1", s1, s1 + rng.randint(50, 300), mate2=kind)
    recs += rr
    units.append(u)
    recs_stripped += [r for r in rr if r.aligned]
    n_unmapped_mate += kind == "unmapped"
sets, ids = per_base_sets(features, ["exon"], ["gene_id"], True)
port = port_count(units, sets, ids, "union", "yes")
name_bam, pos_bam = write_bams(os.path.join(tmp, "b"), recs, {"chr1": 70000})
name_s, pos_s = write_bams(os.path.join(tmp, "bs"), recs_stripped, {"chr1": 70000})
print(f"  pairs with an unmapped mate: {n_unmapped_mate}; documented expectation: every pair counts in its gene "
      f"(sum = {float(sum(v for k, v in port.items() if not k.startswith('__'))):g})")
for label, bam, a in (("-a 10 (default), unmapped mates in file, -r name", name_bam, "10"),
                      ("-a 10 (default), unmapped mates in file, -r pos ", pos_bam, "10"),
                      ("-a 0,            unmapped mates in file, -r name", name_bam, "0"),
                      ("-a 10,           unmapped mates stripped, -r name", name_s, "10"),
                      ("-a 10,           unmapped mates stripped, -r pos ", pos_s, "10")):
    cli, _ = run_htseq_count(bam, gtf, ["-s", "yes", "-a", a, "-r", label.split("-r ")[1].strip()])
    s = sum(v for k, v in cli.items() if not k.startswith("__"))
    lost = sum(1 for g in ids if abs(cli[g] - float(port[g])) > 1e-9)
    print(f"  {label}: sum(genes) = {s:g}, __too_low_aQual = {cli['__too_low_aQual']:g}, "
          f"genes differing from expectation: {lost}/20")
print("\nRESULT: with the default -a 10 every pair whose unmapped mate is in the file is counted as "
      "__too_low_aQual; the same pairs count when -a 0 is given or when the unmapped records are removed.")
