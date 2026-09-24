"""Held-up check: CollectWgsMetrics against an independent per-position depth, plus HET_SNP_SENSITIVITY.

Truth: per-position depth counting each read name once per position, only bases with quality >= 20
(MINIMUM_BASE_QUALITY) from reads with MAPQ >= 20, non-duplicate, paired with both mates mapped
(COUNT_UNPAIRED false), primary; reference N positions excluded; capped at COVERAGE_CAP 250;
MEAN/SD (sample)/MEDIAN/MAD over the capped depths of all genome positions; PCT_xX; PCT_EXC_*
as fractions of all bases seen (excluded + kept); FOLD_80 = MEAN / 20th percentile.
HET_SNP_SENSITIVITY: with every base at Q30 and depth d at every position, the sum of m alt
qualities is 30 m exactly and a het is called when 30 m > 10 (d log10 2 + 3), so the sensitivity
is sum over m of Binom(d, 0.5)(m) [30 m > 10 (d log10 2 + 3)]; Picard estimates it by sampling
quality sums with a rejection sampler that gives up after 600 rejections and returns quality 0.
Usage: python heldup_wgs_metrics.py [picard.jar]
"""
import os, sys, random, statistics, math, collections
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(31)
L = 3000
seq = rand_seq(rng, L)
seq = seq[:1000] + "N" * 20 + seq[1020:]     # 20 N bases in the reference
fa = write_fasta(os.path.join(d, "ref.fa"), [("chr1", seq)])

recs = []
# 40 random pairs (100 bp reads, insert 250-350), qualities mixed (some Q10 bases), some MAPQ 5, some duplicates, one unpaired
for i in range(40):
    p1 = rng.randrange(0, L - 400)
    ins = rng.randrange(250, 351)
    q = [rng.choice((30, 30, 30, 10, 2)) for _ in range(100)]
    mapq = 60 if i % 7 else 5
    r = pair(f"p{i}", p1, p1 + ins - 100, rlen=100, qual=q, mapq=mapq, dup=(i % 11 == 0))
    r[1]["qual"] = [rng.choice((30, 30, 30, 10, 2)) for _ in range(100)]
    recs += r
recs.append(simple_read("single", 500, "100M", flag=0, qual=30))
# an overlapping pair (insert 150 -> 50 bp overlap)
recs += pair("ovl", 2000, 2050, rlen=100, qual=30)
bam = write_bam(os.path.join(d, "reads.bam"), recs, [("chr1", L)])

# truth
depth = [0] * L; seen = collections.defaultdict(set)
exc = collections.Counter()
for r in recs:
    if r["flag"] & (0x100 | 0x800): continue
    paired_ok = (r["flag"] & 1) and not (r["flag"] & 8)
    if r["mapq"] < 20: exc["MAPQ"] += len(r["qual"]); continue
    if r["flag"] & 0x400: exc["DUPE"] += len(r["qual"]); continue
    if not paired_ok: exc["UNPAIRED"] += len(r["qual"]); continue
    pos = r["pos"]
    for k, q in enumerate(r["qual"]):
        g = pos + k
        if seq[g] == "N": continue
        if q < 20: exc["BASEQ"] += 1; continue
        if r["name"] in seen[g]: exc["OVERLAP"] += 1; continue
        seen[g].add(r["name"]); depth[g] += 1
territory = [depth[g] for g in range(L) if seq[g] != "N"]
total = sum(territory); tot_ex = total + sum(exc.values())
t = dict(GENOME_TERRITORY=len(territory), MEAN_COVERAGE=statistics.fmean(territory), SD_COVERAGE=statistics.stdev(territory),
         MEDIAN_COVERAGE=statistics.median(territory), MAD_COVERAGE=statistics.median(abs(x - statistics.median(territory)) for x in territory),
         PCT_EXC_MAPQ=exc["MAPQ"] / tot_ex, PCT_EXC_DUPE=exc["DUPE"] / tot_ex, PCT_EXC_UNPAIRED=exc["UNPAIRED"] / tot_ex,
         PCT_EXC_BASEQ=exc["BASEQ"] / tot_ex, PCT_EXC_OVERLAP=exc["OVERLAP"] / tot_ex, PCT_EXC_TOTAL=(tot_ex - total) / tot_ex,
         PCT_1X=sum(x >= 1 for x in territory) / len(territory), PCT_5X=sum(x >= 5 for x in territory) / len(territory),
         PCT_10X=sum(x >= 10 for x in territory) / len(territory))
srt = sorted(territory); p20 = srt[math.ceil(0.2 * len(srt)) - 1]
t["FOLD_80_BASE_PENALTY"] = t["MEAN_COVERAGE"] / p20 if p20 else float("inf")
out = os.path.join(d, "wgs.txt")
run("CollectWgsMetrics", "-I", bam, "-O", out, "-R", fa)
m, h = parse_metrics(out); m = m[0]
bad = 0
for k, v in t.items():
    g = m[k]
    ok = g is not None and abs(float(g) - float(v)) < 1e-5
    bad += not ok
    print(f"  {k:22s} picard {g!s:12s} truth {round(v, 6)!s:12s} {'ok' if ok else 'MISMATCH'}")
print(f"  depth histogram: {'ok' if all(h['high_quality_coverage_count'].get(k, 0) == v for k, v in collections.Counter(territory).items()) else 'MISMATCH'}; mismatches {bad}")

# HET_SNP_SENSITIVITY: uniform depth d, all Q30
print("\n--- HET_SNP_SENSITIVITY with every base Q30 and uniform depth (exact binomial vs Picard's sampler)")
def exact(dd):
    thr = 10 * (dd * math.log10(2) + 3.0)
    return sum(math.comb(dd, mm) / 2 ** dd for mm in range(dd + 1) if 30 * mm > thr)
for dd in (4, 6, 8, 12, 20):
    L2 = 2000
    rr = []
    for j in range(dd):
        # tile the whole contig with pairs of 100-bp reads so that every position has depth dd: reads at every 100 bp, offset j*0
        for start in range(0, L2, 200):
            rr += pair(f"d{dd}_{j}_{start}", start, start + 100, rlen=100, qual=30)
    fa2 = write_fasta(os.path.join(d, "ref2.fa"), [("chr1", rand_seq(rng, L2))])
    b2 = write_bam(os.path.join(d, "unif.bam"), rr, [("chr1", L2)])
    run("CollectWgsMetrics", "-I", b2, "-O", out, "-R", fa2)
    m2 = parse_metrics(out)[0][0]
    print(f"  depth {dd:3d}: MEAN_COVERAGE {m2['MEAN_COVERAGE']}  HET_SNP_SENSITIVITY picard {m2['HET_SNP_SENSITIVITY']}  exact {exact(dd):.6f}  HET_SNP_Q picard {m2['HET_SNP_Q']}")
