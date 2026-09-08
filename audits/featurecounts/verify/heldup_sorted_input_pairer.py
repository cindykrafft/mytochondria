#!/usr/bin/env python3
"""Held-up: the read pairer on coordinate-sorted input (the default output of
STAR/HISAT2 + samtools sort) gives the same counts as name-adjacent input,
with 1 and 8 threads, on a file large enough to spill orphans to disk.

60,000 fragments over two 2-Mb chromosomes: proper pairs with mates up to
300 kb apart, multi-mappers with NH/HI tags, chimeric pairs, pairs with one
unmapped mate, and single-end records.  The name-adjacent file is the ground
truth ordering; the coordinate-sorted file is what featureCounts re-pairs.
"""
import os
import random
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fclib

print("featureCounts", fclib.fc_version())
wd = tempfile.mkdtemp(prefix="fcpair_")
CH = {"chr1": 2_000_000, "chr2": 2_000_000}
rng = random.Random(11)
genes = []
for c in CH:
    p, g = 1000, 0
    while p < 1_990_000:
        ex = []
        for _ in range(rng.randint(1, 5)):
            L = rng.randint(80, 600)
            ex.append((p, p + L - 1))
            p += L + rng.randint(200, 3000)
        genes.append((f"{c}_g{g}", c, rng.choice("+-"), ex))
        g += 1
        p += rng.randint(0, 5000)
gtf = os.path.join(wd, "a.gtf")
fclib.write_gtf(gtf, genes)
recs = []
for i in range(60000):
    c = rng.choice(list(CH))
    p = rng.randint(1, 1_900_000)
    u = rng.random()
    nh = rng.choice([1, 1, 1, 2, 3])
    if u < 0.05:
        recs.append(fclib.single(f"s{i}", c, p, "75M", rev=rng.random() < 0.5))
    elif u < 0.10:
        recs += [dict(name=f"h{i}", flag=1 | 8 | 64, chrom=c, pos=p, cigar="75M", mapq=60, mchrom=c, mpos=p, tlen=0),
                 dict(name=f"h{i}", flag=1 | 4 | 128, chrom=c, pos=p, mapq=0, mchrom=c, mpos=p, tlen=0, readlen=75)]
    elif u < 0.13:
        recs += fclib.pair(f"c{i}", c, p, "75M", rng.randint(1, 1_900_000), "75M", chrom2="chr2" if c == "chr1" else "chr1")
    else:
        for k in range(nh):
            c1 = c if k == 0 else rng.choice(list(CH))
            p1 = p if k == 0 else rng.randint(1, 1_900_000)
            p2 = min(p1 + rng.choice([rng.randint(-200, 400), rng.randint(-300_000, 300_000)]), 1_990_000)
            p2 = max(1, p2)
            cig = rng.choice(["75M", "75M", "30M2000N45M", "5S70M"])
            recs += fclib.pair(f"p{i}", c1, p1, cig, p2, "75M", r1_rev=rng.random() < 0.5,
                               tags={"NH": nh, "HI": k + 1} if nh > 1 else {}, extra_flag=256 if k else 0)
print(f"{len(recs)} records")
bam_name = os.path.join(wd, "byname.bam")
fclib.make_bam(bam_name, CH, recs)
bam_pos = os.path.join(wd, "bypos.bam")
fclib.make_bam(bam_pos, CH, recs, sort=True)
res = {}
for label, bam, T in [("name-adjacent -T 1", bam_name, 1), ("coordinate-sorted -T 1", bam_pos, 1),
                      ("coordinate-sorted -T 8", bam_pos, 8), ("name-adjacent -T 8", bam_name, 8)]:
    for opts in (["-s", "2"], ["-s", "2", "-M", "--fraction", "-O"], ["-B", "-C", "-Q", "10"]):
        counts, summary, _, log = fclib.run_fc(gtf, bam, ["-p", "--countReadPairs", "-T", str(T), *opts], core=False, workdir=wd)
        res[(label, " ".join(opts))] = (counts, summary)
for opts in ("-s 2", "-s 2 -M --fraction -O", "-B -C -Q 10"):
    ref = res[("name-adjacent -T 1", opts)]
    same = {lab: res[(lab, opts)] == ref for lab in ("coordinate-sorted -T 1", "coordinate-sorted -T 8", "name-adjacent -T 8")}
    print(f"{opts:24s}: Assigned={ref[1]['Assigned']} of {fclib.summary_total(ref[1])} fragments; identical to name-adjacent -T 1: {same}")
