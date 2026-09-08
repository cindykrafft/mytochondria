"""ST1: `samtools stats` coverage distribution (COV rows, and the -t/-g target
percentage) is computed in a fixed-size ring buffer (5 x the longest read seen,
1,500 cells for reads <= 300 bp) indexed modulo its size.  An aligned block that
starts more than the buffer size beyond the read's start -- the far exon of a
spliced RNA-seq alignment -- wraps around and is added to positions near the
read start (stats.c round_buffer_insert_read / round_buffer_lidx2ridx).
Cases: A minimal two-read wrap, A2 the same with a short intron (correct),
B a simulated six-exon gene with 3,000 spliced reads, C the -t/-g target
percentage on that gene.  Truth is computed in Python per position and
compared with the COV rows.  The reallocation defect is st2_stats_cov_realloc.py.
Usage: python st1_stats_cov_ringbuffer.py [samtools-binary]
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
d = tmpdir()
refs = [("chr1", 2_000_000)]

def check(label, recs, extra=()):
    bam = write_bam(os.path.join(d, label + ".bam"), recs, refs)
    out, err, rc = run("stats", *extra, bam)
    got = parse_cov(out)
    exp = dict(cov_hist(depth_truth(recs, 0)))
    ok = got == exp
    tot_got = sum(k * v for k, v in got.items()); tot_exp = sum(k * v for k, v in exp.items())
    print(f"\n[{label}]  {'OK' if ok else 'MISMATCH'}")
    print("  truth COV   :", dict(sorted(exp.items()))[:20] if False else dict(sorted(exp.items())) if len(exp) <= 12 else f"{len(exp)} depth values, {sum(exp.values())} positions, sum depth {tot_exp}")
    print("  samtools COV:", dict(sorted(got.items())) if len(got) <= 12 else f"{len(got)} depth values, {sum(got.values())} positions, sum depth {tot_got}")
    if err.strip(): print("  stderr:", err.strip()[:300])
    return got, exp, out

# --- A. minimal: one plain read + one spliced read whose far block lands exactly one ring size (1,500) downstream
recs = [simple_read("a", 0, "50M"), simple_read("b", 0, "50M1450N50M")]
check("A_splice_wraps_onto_read_start", recs)

# --- A2. same geometry but intron shorter than the ring: no wrap, correct
recs = [simple_read("a", 0, "50M"), simple_read("b", 0, "50M1000N50M")]
check("A2_short_intron_no_wrap", recs)

# --- B. realistic spliced RNA-seq: 3,000 100-bp reads over a 40-kb "gene" of 6 exons, introns 300-12,000 bp
random.seed(1)
exons = [(1000, 1400), (1700, 2000), (5000, 5300), (17000, 17400), (25000, 25200), (37000, 37600)]
tx = []  # transcript coordinate -> genome coordinate
for s, e in exons: tx.extend(range(s, e))
recs = []
for i in range(3000):
    t0 = random.randrange(0, len(tx) - 100)
    coords = tx[t0:t0 + 100]
    # build CIGAR from genome coordinates
    cig, run_len, prev = [], 1, coords[0]
    for c in coords[1:]:
        if c == prev + 1: run_len += 1
        else:
            cig.append(f"{run_len}M{c - prev - 1}N"); run_len = 1
        prev = c
    cig.append(f"{run_len}M")
    recs.append(simple_read(f"r{i}", coords[0], "".join(cig)))
got, exp, _ = check("B_spliced_rnaseq_3000_reads", recs)
def summarize(h):
    n = sum(h.values()); s = sum(k * v for k, v in h.items())
    ks = sorted(h)
    cum, med = 0, None
    for k in ks:
        cum += h[k]
        if med is None and cum >= n / 2: med = k
    return n, s / n if n else 0, med, max(ks) if ks else 0
for name, h in (("truth", exp), ("samtools", got)):
    n, mean, med, mx = summarize(h)
    print(f"  {name:9s}: covered positions {n}, mean depth over covered {mean:.2f}, median {med}, max {mx}")

# --- C. the -t/-g "percentage of target genome with coverage > N" uses the same buffer
tgt = os.path.join(d, "targets.tsv")
with open(tgt, "w") as f:
    for s, e in exons: f.write(f"chr1\t{s + 1}\t{e}\n")
bam = os.path.join(d, "B_spliced_rnaseq_3000_reads.bam")
for g in (0, 5, 10, 20):
    out, err, rc = run("stats", "-t", tgt, "-g", g, bam)
    v = sn(out).get(f"percentage of target genome with coverage > {g} (%)")
    tot = sum(e - s for s, e in exons)
    truth = 100.0 * sum(1 for p, dd in depth_truth(recs, 0).items() if dd > g) / tot
    print(f"  -g {g}: samtools {v} %   truth {truth:.2f} %")
