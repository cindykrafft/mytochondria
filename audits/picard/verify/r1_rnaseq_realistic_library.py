"""R1, size of the effect on a realistic library: CollectRnaSeqMetrics on 300 multi-exon transcripts.

Synthetic genome with 300 genes (2-14 exons of 80-400 bp, both strands, 1 transcript each, fully
coding). Paired-end 2x75 fragments (insert 250-350) drawn per transcript with a 3'-biased
coverage profile (relative density rising from 0.6 at the 5' end to 1.4 at the 3' end) and
Poisson noise, mean depth 5-200 per transcript, spliced through the junctions. The truth for
each transcript's coverage array is computed by counting every aligned base; the harness
prints MEDIAN_CV_COVERAGE, the 5'/3' biases and the normalized-coverage histogram from Picard
and from the truth, and the same after Picard's per-block last-base loss is modelled.
Run once on the unmodified jar and once on a jar with Gene.addCoverageCounts fixed (i <= end).
Usage: python r1_rnaseq_realistic_library.py [picard.jar]
"""
import os, sys, random, statistics, math, collections
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(101)
NG = 300
G = 0
genes = []
seqs = []
chrom_len = 0
CHROM_LEN = 5_000_000
ref = rand_seq(rng, CHROM_LEN)
pos = 5000
for g in range(NG):
    ne = rng.randint(2, 14)
    exons = []
    p = pos
    for e in range(ne):
        ln = rng.randint(80, 400)
        exons.append((p, p + ln - 1))
        p += ln + rng.randint(200, 3000)
    strand = rng.choice("+-")
    genes.append((f"G{g}", strand, exons))
    pos = p + rng.randint(2000, 5000)
    if pos > CHROM_LEN - 60000: break
NG = len(genes)
fa = write_fasta(os.path.join(d, "ref.fa"), [("chr1", ref)])
with open(os.path.join(d, "genes.refFlat"), "w") as f:
    for name, strand, exons in genes:
        f.write(f"{name}\t{name}.1\tchr1\t{strand}\t{exons[0][0]-1}\t{exons[-1][1]}\t{exons[0][0]-1}\t{exons[-1][1]}\t{len(exons)}\t{','.join(str(s-1) for s,_ in exons)},\t{','.join(str(e) for _,e in exons)},\n")

def tx_map(exons):
    """transcript coordinate (1-based, genomic order) -> genomic position, and inverse."""
    fwd = []
    for s, e in exons: fwd.extend(range(s, e + 1))
    return fwd
RL = 75
recs = []
truth_cov = {}
n = 0
for name, strand, exons in genes:
    fwd = tx_map(exons); L = len(fwd)
    if L < 2 * RL + 20: continue
    depth = rng.choice((5, 10, 20, 50, 100, 200))
    nfrag = max(1, int(depth * L / (2 * RL)))
    cov = [0] * L
    for k in range(nfrag):
        # 3' bias in transcript orientation: density 0.6 -> 1.4 from 5' to 3'
        while True:
            u = rng.random(); w = 0.6 + 0.8 * u
            if rng.random() < w / 1.4: break
        ins = rng.randint(250, 350)
        if strand == "+": start = int(u * max(1, L - ins)) + 1
        else: start = L - int(u * max(1, L - ins)) - ins + 1
        start = max(1, min(start, L - ins + 1))
        if ins > L: continue
        # two reads: transcript positions [start, start+RL-1] forward, [start+ins-RL, start+ins-1] reverse
        r1 = (start, start + RL - 1); r2 = (start + ins - RL, start + ins - 1)
        def cigar_for(a, b):
            gpos = [fwd[t - 1] for t in range(a, b + 1)]
            ops = []; run_len = 1
            for i in range(1, len(gpos)):
                gap = gpos[i] - gpos[i - 1]
                if gap == 1: run_len += 1
                else: ops.append(f"{run_len}M{gap - 1}N"); run_len = 1
            ops.append(f"{run_len}M")
            return gpos[0], "".join(ops)
        g1, c1 = cigar_for(*r1); g2, c2 = cigar_for(*r2)
        for t in range(r1[0], r1[1] + 1): cov[t - 1] += 1
        for t in range(r2[0], r2[1] + 1): cov[t - 1] += 1
        tl = (fwd[r2[1] - 1] - g1 + 1)
        recs.append(simple_read(f"f{n}", g1 - 1, c1, flag=0x63, qual=30, mtid=0, mpos=g2 - 1, tlen=tl))
        recs.append(simple_read(f"f{n}", g2 - 1, c2, flag=0x93, qual=30, mtid=0, mpos=g1 - 1, tlen=-tl))
        n += 1
    truth_cov[name] = (strand, cov)
bam = write_bam(os.path.join(d, "reads.bam"), recs, [("chr1", CHROM_LEN)])
print(f"{NG} genes, {len(truth_cov)} transcripts with reads, {n} fragments")

def summarize(covs, label):
    cvs, f5, f3, f53 = [], [], [], []
    hist = collections.defaultdict(float)
    picked = []
    for name, (strand, cov) in covs.items():
        c = cov if strand == "+" else cov[::-1]
        mean = statistics.fmean(c)
        if len(c) < 500 or mean < 1: continue
        picked.append((mean, name, c))
    picked.sort(reverse=True); picked = picked[:1000]
    for mean, name, c in picked:
        sd = statistics.pstdev(c)   # Picard's MathUtil.stddev is the population SD
        cvs.append(sd / mean)
        a = statistics.fmean(c[:100]); b = statistics.fmean(c[-100:])
        f5.append(a / mean); f3.append(b / mean); f53.append(a / b if b else 0)
        last = len(c) - 1
        for p in range(101):
            s = int(max(0, last * (p / 100 - 0.005))); e = int(min(last, last * (p / 100 + 0.005)))
            hist[p] += (statistics.fmean(c[s:e + 1]) / mean) / len(picked)
    print(f"  {label}: transcripts {len(picked)}, MEDIAN_CV_COVERAGE {statistics.median(cvs):.4f}, MEDIAN_5PRIME_BIAS {statistics.median(f5):.4f}, MEDIAN_3PRIME_BIAS {statistics.median(f3):.4f}, MEDIAN_5PRIME_TO_3PRIME_BIAS {statistics.median(f53):.4f}")
    print(f"    normalized coverage at 0/25/50/75/100 %: {[round(hist[p], 3) for p in (0, 25, 50, 75, 100)]}")
    return cvs

summarize(truth_cov, "truth (every aligned base counted)")
# bug model: drop the last base of every alignment block
bug_cov = {}
for name, (strand, cov) in truth_cov.items():
    bug_cov[name] = (strand, cov[:])
for r in recs:
    pos = r["pos"] + 1
    for ln, op in parse_cigar(r["cigar"]):
        if op == "M":
            g = pos + ln - 1
            pos += ln
            # find transcript & coordinate of g
            for name, (strand, exons) in ((nm, (st, ex)) for nm, st, ex in genes):
                if exons[0][0] <= g <= exons[-1][1]:
                    off = 0
                    for s, e in exons:
                        if s <= g <= e:
                            if name in bug_cov: bug_cov[name][1][off + g - s] -= 1
                            break
                        off += e - s + 1
                    break
        elif op == "N": pos += ln
summarize(bug_cov, "bug model (last base of each block dropped)")

out = os.path.join(d, "rna.txt")
run("CollectRnaSeqMetrics", "-I", bam, "-O", out, "--REF_FLAT", os.path.join(d, "genes.refFlat"), "--STRAND_SPECIFICITY", "NONE", "-R", fa)
m, h = parse_metrics(out); m = m[0]
print(f"  picard: MEDIAN_CV_COVERAGE {m['MEDIAN_CV_COVERAGE']}, MEDIAN_5PRIME_BIAS {m['MEDIAN_5PRIME_BIAS']}, MEDIAN_3PRIME_BIAS {m['MEDIAN_3PRIME_BIAS']}, MEDIAN_5PRIME_TO_3PRIME_BIAS {m['MEDIAN_5PRIME_TO_3PRIME_BIAS']}")
nc = h["All_Reads.normalized_coverage"]
print(f"    normalized coverage at 0/25/50/75/100 %: {[round(nc[p], 3) for p in (0, 25, 50, 75, 100)]}")
