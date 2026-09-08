#!/usr/bin/env python3
"""Held-up checks that the random battery does not cover: junction counting
(-J), thread count, the per-file form of -s, GTF attribute parsing, multiple
-t types, SAF vs GTF, the gene Length column, fractional-count rounding, and
the automatic 'chr' prefix matching between BAM and annotation.
"""
import os
import random
import sys
import tempfile
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib

print("featureCounts", fclib.fc_version())
wd = tempfile.mkdtemp(prefix="fcmisc_")
CH = {"chr1": 20000, "chr2": 20000}
rng = random.Random(3)

# ---------------------------------------------------------------- 1. junctions
genes = [("A", "chr1", "+", [(1000, 1200), (1500, 1700), (2000, 2200)]), ("B", "chr1", "-", [(5000, 5300)])]
gtf = os.path.join(wd, "j.gtf")
fclib.write_gtf(gtf, genes)
recs = []
expected = Counter()
for i in range(300):
    kind = rng.choice(["j1", "j2", "j12", "none"])
    dup = rng.random() < 0.2
    nh = rng.choice([1, 1, 2])
    mapq = rng.choice([60, 60, 0])
    if kind == "j1":
        cig, p = "30M299N30M", 1171           # last exon-1 base 1200, first exon-2 base 1500
        expected[("chr1", 1200, 1500)] += 1
    elif kind == "j2":
        cig, p = "30M299N30M", 1671           # 1700 -> 2000
        expected[("chr1", 1700, 2000)] += 1
    elif kind == "j12":
        cig, p = "20M299N201N30M".replace("299N201N", "299N201M299N"), 1181  # 1181-1200, 1500-1700, 2000-2029
        cig = "20M299N201M299N30M"
        expected[("chr1", 1200, 1500)] += 1
        expected[("chr1", 1700, 2000)] += 1
    else:
        cig, p = "50M", rng.randint(1000, 1150)
    recs.append(fclib.single(f"r{i}", "chr1", p, cig, rev=rng.random() < 0.5, mapq=mapq,
                             tags={"NH": nh} if nh > 1 else {}, extra_flag=1024 if dup else 0))
bam = os.path.join(wd, "j.bam")
fclib.make_bam(bam, CH, recs)
counts, summary, det, _ = fclib.run_fc(gtf, bam, ["-J", "-Q", "10", "--ignoreDup"], workdir=wd)
got = Counter()
with open(os.path.join(wd, "counts.txt.jcounts")) as f:
    hdr = next(f).rstrip("\n").split("\t")
    for line in f:
        t = line.rstrip("\n").split("\t")
        d = dict(zip(hdr, t))
        got[(d["Site1_chr"], int(d["Site1_location"]), int(d["Site2_location"]))] = int(t[-1])
print("1. -J junction counts (manual: identified from ALL exon-spanning reads, filters not applied):")
print(f"   expected {dict(expected)}\n   got      {dict(got)}  -> {'equal' if got == expected else 'DIFFERENT'}")
print(f"   (assigned reads under -Q 10 --ignoreDup: {summary['Assigned']} of 300; junction totals count every N read)")

# ---------------------------------------------------------------- 2. threads
genes2 = []
for c in CH:
    p = 100
    g = 0
    while p < 19000:
        n = rng.randint(1, 3)
        ex = []
        for _ in range(n):
            L = rng.randint(50, 300)
            ex.append((p, p + L - 1))
            p += L + rng.randint(30, 200)
        genes2.append((f"{c}_g{g}", c, rng.choice("+-"), ex))
        g += 1
        p += rng.randint(0, 400)
gtf2 = os.path.join(wd, "t.gtf")
fclib.write_gtf(gtf2, genes2)
recs = []
for i in range(6000):
    c = rng.choice(list(CH))
    p = rng.randint(1, 19000)
    cig = rng.choice(["50M", "50M", "25M200N25M", "10S40M"])
    if rng.random() < 0.7:
        recs += fclib.pair(f"p{i}", c, p, cig, min(p + rng.randint(-100, 300), 19500), "50M",
                           r1_rev=rng.random() < 0.5, mapq=rng.choice([60, 0]))
    else:
        recs.append(fclib.single(f"s{i}", c, p, cig, rev=rng.random() < 0.5, mapq=rng.choice([60, 0])))
rng.shuffle(recs)
bam2 = os.path.join(wd, "t.bam")
fclib.make_bam(bam2, CH, recs)
res = {}
for T in (1, 4, 8):
    counts, summary, _, _ = fclib.run_fc(gtf2, bam2, ["-p", "--countReadPairs", "-s", "2", "-Q", "10", "-T", str(T)],
                                         core=False, workdir=wd)
    res[T] = (counts, summary)
print(f"2. -T 1 vs -T 4 vs -T 8 on {len(recs)} records: counts identical: "
      f"{res[1][0] == res[4][0] == res[8][0]}; summaries identical: {res[1][1] == res[4][1] == res[8][1]}; "
      f"Assigned={res[1][1]['Assigned']}")

# ---------------------------------------------------------------- 3. per-file -s
bam3 = os.path.join(wd, "t2.bam")
fclib.make_bam(bam3, CH, recs[::-1])
out = os.path.join(wd, "multi.txt")
import subprocess
subprocess.run([fclib.FC, "-a", gtf2, "-o", out, "-p", "--countReadPairs", "-s", "1,2", bam2, bam3],
               capture_output=True, text=True, check=True)
cols = {}
with open(out) as f:
    for line in f:
        if line.startswith("#") or line.startswith("Geneid"):
            continue
        t = line.rstrip("\n").split("\t")
        cols[t[0]] = (float(t[-2]), float(t[-1]))
c1, _, _, _ = fclib.run_fc(gtf2, bam2, ["-p", "--countReadPairs", "-s", "1"], core=False, workdir=wd)
c2, _, _, _ = fclib.run_fc(gtf2, bam3, ["-p", "--countReadPairs", "-s", "2"], core=False, workdir=wd)
ok = all(cols[g][0] == c1[g] and cols[g][1] == c2[g] for g in cols)
print(f"3. -s 1,2 over two files equals separate -s 1 / -s 2 runs: {ok}")

# ---------------------------------------------------------------- 4. GTF attributes
attr_gtf = os.path.join(wd, "attr.gtf")
with open(attr_gtf, "w") as f:
    f.write('chr1\tx\texon\t1000\t1400\t.\t+\t.\tref_gene_id "WRONG"; gene_id "G1"; gene_name "N1"; ref_gene_id "WRONG2";\n')
    f.write('chr1\tx\texon\t3000\t3400\t.\t+\t.\tgene_id=G2;transcript_id=T2\n')                # GFF-style
    f.write('chr1\tx\texon\t5000\t5400\t.\t+\t.\ttranscript_id "T3"; gene_id "G3 with space";\n')
    f.write('chr1\tx\tCDS\t7000\t7400\t.\t+\t.\tgene_id "G4";\n')                              # not an exon
    f.write('chr1\tx\texon\t9000\t9400\t.\t+\t.\tgene_id "G5"; gene_id "G5b";\n')               # repeated key
recs = [fclib.single(f"a{i}", "chr1", p + 10, "30M") for i, p in enumerate([1000, 3000, 5000, 7000, 9000])]
bam4 = os.path.join(wd, "attr.bam")
fclib.make_bam(bam4, CH, recs)
counts, _, det, _ = fclib.run_fc(attr_gtf, bam4, [], workdir=wd)
print(f"4. GTF attribute parsing, default -t exon -g gene_id: rows={list(counts)}; "
      f"targets={[det[f'a{i}'][2] for i in range(5)]}")
counts, _, det, _ = fclib.run_fc(attr_gtf, bam4, ["-t", "exon,CDS"], workdir=wd)
print(f"   -t exon,CDS: rows={list(counts)}; a3 -> {det['a3']}")

# ---------------------------------------------------------------- 5. SAF vs GTF, Length, fractions, chr prefix
genes5 = [("L1", "chr1", "+", [(1000, 1500), (1400, 1600), (1800, 1900)]), ("L2", "chr1", "-", [(1000, 1500)]),
          ("L3", "chr1", "+", [(3000, 3100)])]
gtf5 = os.path.join(wd, "l.gtf")
saf5 = os.path.join(wd, "l.saf")
fclib.write_gtf(gtf5, genes5)
fclib.write_saf(saf5, genes5)
recs = [fclib.single("m", "chr1", 1450, "20M")] + [fclib.single(f"x{i}", "chr1", 1450, "20M", tags={"NH": 3},
                                                                  extra_flag=256 if i else 0) for i in range(3)]
bam5 = os.path.join(wd, "l.bam")
fclib.make_bam(bam5, CH, recs)
cg, _, dg, _ = fclib.run_fc(gtf5, bam5, ["-O", "--fraction", "-M"], workdir=wd)
cs, _, ds, _ = fclib.run_fc(saf5, bam5, ["-O", "--fraction", "-M"], fmt="SAF", workdir=wd)
lengths = {}
with open(os.path.join(wd, "counts.txt")) as f:
    for line in f:
        if line.startswith("#") or line.startswith("Geneid"):
            continue
        t = line.split("\t")
        lengths[t[0]] = int(t[5])
print(f"5. GTF == SAF counts: {cg == cs} ({cg}); Length column: {lengths} (L1 = union 1000-1600 (601) + 1800-1900 (101) = 702)")
print(f"   -O -M --fraction: read m over L1+L2 -> 0.50 each; x (NH=3, all three alignments over L1+L2) -> 1/(3*2) each: "
      f"{cg}")
# chr prefix
gtf6 = os.path.join(wd, "nochr.gtf")
with open(gtf6, "w") as f:
    f.write('1\tx\texon\t1000\t1500\t.\t+\t.\tgene_id "P1";\n')
counts, summary, det, log = fclib.run_fc(gtf6, bam5, [], workdir=wd)
gtf7 = os.path.join(wd, "chr.gtf")
with open(gtf7, "w") as f:
    f.write('chr1\tx\texon\t1000\t1500\t.\t+\t.\tgene_id "P1";\n')
bam7 = os.path.join(wd, "nochr.bam")
fclib.make_bam(bam7, {"1": 20000}, [fclib.single("m", "1", 1450, "20M")])
counts7, _, det7, _ = fclib.run_fc(gtf7, bam7, [], workdir=wd)
print(f"6. annotation chromosome '1', BAM 'chr1': read m -> {det['m'][0]} (P1={counts['P1']:g}); "
      f"annotation 'chr1', BAM '1': {det7['m'][0]} (P1={counts7['P1']:g}); the 'chr' prefix is matched "
      f"automatically in both directions (undocumented)")
