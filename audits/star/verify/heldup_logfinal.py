#!/usr/bin/env python3
"""Held-up check: Log.final.out statistics and their denominators, recomputed from the
unsorted BAM (all records, --outSAMunmapped Within) and the read files.

Usage: python heldup_logfinal.py /path/to/STAR [workdir]

Port: input reads = distinct read names; average input read length = floor(sum of read
lengths / reads) (both mates summed for pairs); unique = reads with NH 1, multi = NH>1,
too many loci / too many mismatches / too short / other = unmapped records with
uT 3/2/1/0; average mapped length = aligned (M) bases of unique reads / unique reads;
mismatch rate = nM of unique reads / their M bases; deletion and insertion rate = D or I
bases of unique reads / their M bases, average lengths per event; splices = N operations
in unique reads (both mates), by jM motif, annotated if jM>=20; all percentages over
input reads and printed with two decimals as STAR does.
"""
import sys, os, tempfile, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

star = sys.argv[1]
work = sys.argv[2] if len(sys.argv) > 2 else tempfile.mkdtemp(prefix="star_audit_")
S = Synth(os.path.join(work, "data"))
print("STAR", star_version(star), "| workdir", work)
gdir = run_star_genome(star, os.path.join(work, "genome_gtf"), S.fa, S.gtf)
COMMON = ["--quantMode", "TranscriptomeSAM", "GeneCounts", "--outSAMtype", "BAM", "Unsorted", "SortedByCoordinate",
          "--outSAMattributes", "All", "--outSAMunmapped", "Within"]
runs = collections.OrderedDict([
    ("SE", (run_star_map(star, gdir, os.path.join(work, "map_se/"), [S.fq_se], COMMON), [S.fq_se])),
    ("PE", (run_star_map(star, gdir, os.path.join(work, "map_pe/"), [S.fq_1, S.fq_2], COMMON), [S.fq_1, S.fq_2])),
    ("SE_mm2", (run_star_map(star, gdir, os.path.join(work, "map_se_mm2/"), [S.fq_se], COMMON + ["--outFilterMultimapNmax", "2"]), [S.fq_se])),
])
def pct(a, b): return "%.2f%%" % (100.0 * a / b) if b else "0.00%"
def f2(x): return "%.2f" % x

allok = True
for name, (prefix, fqs) in runs.items():
    lf = read_logfinal(prefix + "Log.final.out")
    # read lengths from the fastq
    lens = collections.Counter()
    for fq in fqs:
        with open(fq) as fh:
            for i, line in enumerate(fh):
                if i % 4 == 0: nm = line[1:].split()[0]
                elif i % 4 == 1: lens[nm] += len(line.strip())
    n_in = len(lens); sum_len = sum(lens.values())
    uniq = multi = 0; ut = collections.Counter(); mapped_bases = 0; nmm = 0; ins_n = ins_l = del_n = del_l = 0
    spl = collections.Counter(); spl_ann = 0
    for qname, recs in bam_by_read(prefix + "Aligned.out.bam").items():
        mapped = [r for r in recs if not r.is_unmapped]
        if not mapped:
            ut[int(recs[0].get_tag("uT"))] += 1; continue
        nh = mapped[0].get_tag("NH")
        if nh > 1: multi += 1; continue
        uniq += 1
        nmm += mapped[0].get_tag("nM")
        for r in mapped:
            for op, ln in r.cigartuples:
                if op in (0, 7, 8): mapped_bases += ln
                elif op == 1: ins_n += 1; ins_l += ln
                elif op == 2: del_n += 1; del_l += ln
            jm = r.get_tag("jM"); jm = [] if list(jm) == [-1] else list(jm)
            for m in jm:
                spl[m % 20] += 1
                if m >= 20: spl_ann += 1
    exp = collections.OrderedDict([
        ("Number of input reads", str(n_in)),
        ("Average input read length", str(sum_len // n_in)),
        ("Uniquely mapped reads number", str(uniq)),
        ("Uniquely mapped reads %", pct(uniq, n_in)),
        ("Average mapped length", f2(mapped_bases / uniq)),
        ("Number of splices: Total", str(sum(spl.values()))),
        ("Number of splices: Annotated (sjdb)", str(spl_ann)),
        ("Number of splices: GT/AG", str(spl[1] + spl[2])),
        ("Number of splices: GC/AG", str(spl[3] + spl[4])),
        ("Number of splices: AT/AC", str(spl[5] + spl[6])),
        ("Number of splices: Non-canonical", str(spl[0])),
        ("Mismatch rate per base, %", pct(nmm, mapped_bases)),
        ("Deletion rate per base", pct(del_l, mapped_bases)),
        ("Deletion average length", f2(del_l / del_n if del_n else 0)),
        ("Insertion rate per base", pct(ins_l, mapped_bases)),
        ("Insertion average length", f2(ins_l / ins_n if ins_n else 0)),
        ("Number of reads mapped to multiple loci", str(multi)),
        ("% of reads mapped to multiple loci", pct(multi, n_in)),
        ("Number of reads mapped to too many loci", str(ut[3])),
        ("% of reads mapped to too many loci", pct(ut[3], n_in)),
        ("Number of reads unmapped: too many mismatches", str(ut[2])),
        ("% of reads unmapped: too many mismatches", pct(ut[2], n_in)),
        ("Number of reads unmapped: too short", str(ut[1])),
        ("% of reads unmapped: too short", pct(ut[1], n_in)),
        ("Number of reads unmapped: other", str(ut[0])),
        ("% of reads unmapped: other", pct(ut[0], n_in)),
        ("Number of chimeric reads", "0"),
    ])
    print("\n== %s" % name)
    print("%-48s %-14s %-14s" % ("statistic", "STAR", "port"))
    nbad = 0
    for k, v in exp.items():
        ok = lf.get(k) == v; nbad += not ok; allok &= ok
        print("%-48s %-14s %-14s%s" % (k, lf.get(k), v, "" if ok else "  <-- MISMATCH"))
    print("differing: %d of %d  (unique+multi+too many+unmapped = %d = input %d: %s)" % (
        nbad, len(exp), uniq + multi + sum(ut.values()), n_in, uniq + multi + sum(ut.values()) == n_in))
    print("denominators: mapped bases of unique reads %d (sum over both mates), unique reads %d, input reads %d, total read bases %d" % (mapped_bases, uniq, n_in, sum_len))

print("\nRESULT:", "every Log.final.out statistic equals the port" if allok else "DIFFERENCES FOUND")
