"""m2: does the truncated mapQ_coef_fac (3 instead of ln 50 = 3.912) make bwa mem
MAPQ better or worse calibrated?

Simulation: a 3-Mb random genome with planted repeat families (300-3000 bp,
2-20 copies, 0.5-15 % divergence per copy from the family consensus; about a
third of the genome); reads with 0.5 % substitution and 0.02 % indel errors,
uniform positions, both strands: single-end 150, 100 and 60 bp, and 2x150
pairs (fragments ~ N(400, 60)). A primary alignment is correct when it lies on
the true strand within 10 bp of the true leftmost position (5 bp + clip).

Two builds are compared on the same reads: $BWA (as released, FAC = 3) and
$BWA_ALT (the one-line fix, FAC = ln 50). For each MAPQ bin the observed number
of wrong alignments is compared with the number the MAPQs promise,
sum(10^(-MAPQ/10)); and the reads passing MAPQ >= 20 / >= 30 are counted.
"""
import random
from _synth import *

BWA_ALT = os.environ.get("BWA_ALT")
rng = random.Random(2026)
G = 3_000_000
genome = list(rand_seq(rng, G))
occupied = []
rep_bases = 0
fams = 0
lengths = [300, 1000, 3000]
copies = [2, 3, 5, 10, 20]
divs = [0.005, 0.01, 0.02, 0.04, 0.08, 0.15]


def free(s, e):
    for a, b in occupied:
        if s < b + 200 and e > a - 200:
            return False
    return True


while rep_bases < G * 0.33:
    Lf = rng.choice(lengths)
    c = rng.choice(copies)
    d = rng.choice(divs)
    cons = rand_seq(rng, Lf)
    for _ in range(c):
        for _try in range(200):
            s = rng.randrange(1000, G - Lf - 1000)
            if free(s, s + Lf):
                break
        else:
            continue
        cp = list(cons)
        for p in range(Lf):
            if rng.random() < d:
                cp[p] = rng.choice([x for x in "ACGT" if x != cp[p]])
        genome[s:s + Lf] = cp
        occupied.append((s, s + Lf))
        rep_bases += Lf
    fams += 1
genome = "".join(genome)
fa = os.path.join(WORK, "m2_ref.fa")
write_fasta(fa, [("chr1", genome)])
index(fa)


def seq_errors(s):
    out = []
    for ch in s:
        r = rng.random()
        if r < 0.005:
            out.append(rng.choice([x for x in "ACGT" if x != ch]))
        elif r < 0.0051:
            out.append(ch + rng.choice("ACGT"))   # 1-bp insertion
        elif r < 0.0052:
            pass                                  # 1-bp deletion
        else:
            out.append(ch)
    return "".join(out)


def sim_se(n, L, tag):
    reads, truth = [], {}
    for i in range(n):
        st = rng.randrange(0, G - L - 5)
        s = seq_errors(genome[st:st + L + 3])[:L]
        rev = rng.random() < 0.5
        name = "%s%d" % (tag, i)
        truth[name] = (st, rev)
        reads.append((name, revcomp(s) if rev else s))
    return reads, truth


def sim_pe(n, L):
    r1, r2, truth = [], [], {}
    for i in range(n):
        frag = max(L + 50, int(rng.gauss(400, 60)))
        st = rng.randrange(0, G - frag - 5)
        f = genome[st:st + frag]
        a = seq_errors(f[:L + 3])[:L]
        b = seq_errors(revcomp(f)[:L + 3])[:L]
        name = "p%d" % i
        if rng.random() < 0.5:   # fragment from the reverse strand
            truth[name] = ((st + frag - L, True), (st, False))
            r1.append((name, b)); r2.append((name, a))
        else:
            truth[name] = ((st, False), (st + frag - L, True))
            r1.append((name, a)); r2.append((name, b))
    return r1, r2, truth


BINS = [(0, 0), (1, 9), (10, 19), (20, 29), (30, 39), (40, 49), (50, 59), (60, 60)]


def evaluate(recs, truth, paired=False):
    rows = []
    for r in recs:
        if not r.primary or r.unmapped:
            continue
        if paired:
            st, rev = truth[r.qname][0 if r.flag & 64 else 1]
        else:
            st, rev = truth[r.qname]
        lclip = clip_lengths(r.cigar)[0]
        correct = (r.rev == rev) and abs((r.pos - 1 - lclip) - st) <= 10
        rows.append((r.mapq, correct))
    return rows


def report(label, rows):
    print("   %s: %d mapped primaries" % (label, len(rows)))
    print("     %-8s %7s %7s %10s %8s" % ("MAPQ", "n", "wrong", "promised", "obs/prom"))
    for lo, hi in BINS:
        sel = [(q, c) for q, c in rows if lo <= q <= hi]
        if not sel:
            continue
        wrong = sum(1 for q, c in sel if not c)
        prom = sum(10 ** (-q / 10) for q, c in sel)
        print("     %-8s %7d %7d %10.2f %8s" % ("%d-%d" % (lo, hi), len(sel), wrong, prom,
                                                 ("%.2f" % (wrong / prom)) if prom > 0 else "-"))
    out = {}
    for t in (20, 30):
        sel = [(q, c) for q, c in rows if q >= t]
        wrong = sum(1 for q, c in sel if not c)
        out[t] = (len(sel), wrong)
        print("     MAPQ >= %d: %d reads, %d wrong (%.4f %%)" % (t, len(sel), wrong, 100. * wrong / max(1, len(sel))))
    mid = [(q, c) for q, c in rows if 1 <= q <= 59]
    wrong = sum(1 for q, c in mid if not c)
    prom = sum(10 ** (-q / 10) for q, c in mid)
    print("     MAPQ 1-59 overall: %d reads, %d wrong, %.1f promised, obs/prom %.2f" % (len(mid), wrong, prom, wrong / prom if prom else 0))
    return out


print("bwa %s  m2 MAPQ calibration; genome 3 Mb, %d repeat families, %.1f %% repeat" % (bwa_version(), fams, 100. * rep_bases / G))
sets = []
for L, n, tag in ((150, 60000, "s"), (100, 60000, "m"), (60, 60000, "t")):
    reads, truth = sim_se(n, L, tag)
    fq = os.path.join(WORK, "m2_%s.fq" % tag)
    write_fastq(fq, reads)
    sets.append(("single-end %d bp" % L, fq, None, truth, False))
r1, r2, tpe = sim_pe(30000, 150)
fq1 = os.path.join(WORK, "m2_1.fq"); fq2 = os.path.join(WORK, "m2_2.fq")
write_fastq(fq1, r1); write_fastq(fq2, r2)
sets.append(("paired 2x150", fq1, fq2, tpe, True))

builds = [("as released (FAC=3)", BWA)]
if BWA_ALT:
    builds.append(("fixed (FAC=ln 50)", BWA_ALT))
summary = []
for name, fq, fq2_, truth, paired in sets:
    print()
    print("== %s ==" % name)
    for blabel, exe in builds:
        cmd = [exe, "mem", "-t", "4", "-K", "100000000", fa, fq] + ([fq2_] if fq2_ else [])
        out, err = run(cmd)
        rows = evaluate(parse_sam(out), truth, paired)
        res = report(blabel, rows)
        summary.append((name, blabel, res))
print()
print("summary (reads passing the filter, wrong among them):")
for name, blabel, res in summary:
    print("   %-18s %-22s MAPQ>=20: %6d (%4d wrong)   MAPQ>=30: %6d (%4d wrong)" % (name, blabel, res[20][0], res[20][1], res[30][0], res[30][1]))
