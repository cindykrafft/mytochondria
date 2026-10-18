"""m1: bwa mem MAPQ against a Python port of the formula.

Single-end port (mem_approx_mapq_se, default -A1 -B4, mapQ_coef_len 50):
  sub      = XS if XS > 0 else min_seed_len*a (19)
  l        = max(aligned query length, reference span)
  identity = 1 - (l*a - AS) / (a+b) / l
  f        = (1 if l < 50 else FAC/ln(l)) * identity^2
             FAC is mapQ_coef_fac: the code assigns log(mapQ_coef_len) = ln 50 = 3.912
             to a field declared `int` (bwamem.h:79), so the compiled value is 3.
             The port is run with FAC = 3 ("as compiled") and FAC = ln 50 ("intended").
  MAPQ     = int(6.02 * (AS - sub)/a * f^2 + .499)  - int(4.343 ln(sub_n+1) + .499)
             clamped to [0, 60]; 0 if sub >= AS
  sub_n    = number of other hits at overlapping read coordinates whose score is
             within max(a+b, o+e) = 7 of AS (read from the -a output).
Paired port (mem_sam_pe, one mate in an exact two-copy repeat, the other unique):
  o     = int(AS1 + AS2 + .721 ln(2 erfc(|d-mu|/sigma/sqrt2)) + .499),  d = TLEN-1
  subo  = AS1 + AS2 - 17          (no second pair: the copies are > 10 kb apart)
  q_pe  = min(60, int(6.02 (o - subo) + .499))
  MAPQ(repeat mate) = min(q_pe, 0 + 40);  MAPQ(unique mate) = 60
mu and sigma are the values bwa prints on stderr for the batch.
"""
import random
from _synth import *

rng = random.Random(5)
contigs = []
base = rand_seq(rng, 400000)
# repeat families: 500-bp segment, copy at +150 kb, with d substitutions
fam = []
seq = list(base)
for k, d in enumerate([0, 0, 1, 2, 3, 5, 8, 12]):
    s0 = 20000 + k * 15000
    s1 = 170000 + k * 15000
    segment = base[s0:s0 + 500]
    copy = segment
    for p in rng.sample(range(500), d):
        copy = mutate_sub(rng, copy, p)
    seq[s1:s1 + 500] = list(copy)
    fam.append((s0, s1, d))
# a three-copy family (exact)
s0 = 300000
for s in (330000, 360000):
    seq[s:s + 500] = seq[s0:s0 + 500]
fam3 = (s0, 330000, 360000)
ref = "".join(seq)
fa = os.path.join(WORK, "m1_ref.fa")
write_fasta(fa, [("chr1", ref)])
index(fa)
header("reference 400 kb with 8 two-copy and 1 three-copy 500-bp families")


def port_se(AS, XS, qlen_aln, rspan, sub_n, a=1, b=4, fac=3):
    sub = XS if XS and XS > 0 else 19
    if sub >= AS:
        return 0
    l = max(qlen_aln, rspan)
    identity = 1. - (l * a - AS) / (a + b) / l
    f = 1. if l < 50 else fac / math.log(l)
    f *= identity * identity
    q = int(6.02 * (AS - sub) / a * f * f + .499)
    if sub_n > 0:
        q -= int(4.343 * math.log(sub_n + 1) + .499)
    return max(0, min(60, q))


def aligned_qlen(cigar):
    return sum(n for n, op in cigar_ops(cigar) if op in "MI=X")


reads = []
meta = {}
i = 0
# unique reads, various lengths and mismatch counts
for L in (50, 75, 100, 150):
    for k in (0, 1, 2, 4, 6, 8):
        for j in range(4):
            st = rng.randrange(5000, 15000) if j % 2 else rng.randrange(390000 - 9000, 395000)
            r = ref[st:st + L]
            for p in rng.sample(range(2, L - 2), min(k, L - 4)):
                r = mutate_sub(rng, r, p)
            n = "u%d" % i; i += 1
            meta[n] = ("unique L=%d %d mm" % (L, k))
            reads.append((n, revcomp(r) if j & 2 else r))
# repeat reads from copy 0 of each family
for s0, s1, d in fam:
    for L in (70, 100, 150):
        for k in (0, 1, 3):
            st = s0 + rng.randrange(50, 500 - L - 10) if L < 440 else s0
            r = ref[st:st + L]
            for p in rng.sample(range(5, L - 5), k):
                r = mutate_sub(rng, r, p)
            n = "f%d" % i; i += 1
            meta[n] = ("2-copy d=%d L=%d %d mm" % (d, L, k))
            reads.append((n, r))
for L in (100, 150):
    for k in (0, 2):
        st = fam3[0] + 100
        r = ref[st:st + L]
        for p in rng.sample(range(5, L - 5), k):
            r = mutate_sub(rng, r, p)
        n = "t%d" % i; i += 1
        meta[n] = ("3-copy exact L=%d %d mm" % (L, k))
        reads.append((n, r))

fq = os.path.join(WORK, "m1_se.fq")
write_fastq(fq, reads)
recs, _ = mem(fa, fq, opts=["-a"])
by = {}
for r in recs:
    by.setdefault(r.qname, []).append(r)

match = match_i = tot = 0
rows = []
for n, rs in by.items():
    pri = [r for r in rs if r.primary]
    if not pri or pri[0].unmapped:
        continue
    p = pri[0]
    sec = [r for r in rs if r.secondary]
    sub_n = sum(1 for r in sec if p.tags["AS"] - r.tags["AS"] <= 7)
    exp = port_se(p.tags["AS"], p.tags.get("XS", 0), aligned_qlen(p.cigar), ref_span(p.cigar), sub_n)
    exp_i = port_se(p.tags["AS"], p.tags.get("XS", 0), aligned_qlen(p.cigar), ref_span(p.cigar), sub_n, fac=math.log(50))
    tot += 1
    match += exp == p.mapq
    match_i += exp_i == p.mapq
    rows.append((meta[n], p.tags["AS"], p.tags.get("XS"), sub_n, p.mapq, exp, exp_i))
classes = {}
for m, AS, XS, sn, q, e, ei in rows:
    key = m
    c = classes.setdefault(key, [0, 0, 0, set()])
    c[0] += 1
    c[1] += q == e
    c[2] += q == ei
    c[3].add((AS, XS, sn, q, e, ei))
for k in sorted(classes):
    c = classes[k]
    ex = sorted(c[3])[0]
    print("   %-26s n=%2d =port(FAC=3) %2d =port(FAC=ln50) %2d  e.g. AS=%s XS=%s sub_n=%d MAPQ=%d port3=%d portln50=%d" % (k, c[0], c[1], c[2], *ex))
ok(match == tot, "single-end MAPQ equals the port with FAC = 3 (as compiled): %d/%d" % (match, tot))
ok(match_i == tot, "single-end MAPQ equals the port with FAC = ln 50 (as written): %d/%d" % (match_i, tot))

# ---------------- paired: one mate in an exact repeat -----------------
pairs1, pairs2 = [], []
pmeta = {}
for j in range(400):
    frag = int(rng.gauss(350, 30))
    if j < 40:
        # mate 1 inside family 0 (exact copy at +150 kb), mate 2 unique downstream
        st = fam[0][0] + rng.randrange(380, 400)   # mate 1 ends inside the 500-bp copy
        frag = max(frag, 300)                         # mate 2 starts beyond it
    else:
        while True:   # unique pairs: keep clear of every planted copy
            st = rng.randrange(1000, 398000 - frag)
            if all(not (st < x + 600 and st + frag > x - 100) for x0, x1, d in fam for x in (x0, x1)) and \
               all(not (st < x + 600 and st + frag > x - 100) for x in fam3):
                break
    f = ref[st:st + frag]
    m1 = f[:100]
    m2 = revcomp(f[-100:])
    n = "p%d" % j
    pmeta[n] = ("repeat" if j < 40 else "unique", frag)
    pairs1.append((n, m1)); pairs2.append((n, m2))
fq1 = os.path.join(WORK, "m1_1.fq"); fq2 = os.path.join(WORK, "m1_2.fq")
write_fastq(fq1, pairs1); write_fastq(fq2, pairs2)
recs, err = mem(fa, fq1, fq2)
mu = sd = None
for line in err.splitlines():
    if "mean and std.dev" in line:
        mu, sd = [float(x) for x in re.findall(r"\(([\d.]+), ([\d.]+)\)", line)[0]]
print("   bwa insert-size estimate: mean %.2f sd %.2f" % (mu, sd))
by = {}
for r in recs:
    if r.primary:
        by.setdefault(r.qname, {})[1 if r.flag & 64 else 2] = r
pm = pt = 0
shown = 0
for n, d in by.items():
    if pmeta[n][0] != "repeat":
        continue
    a, b = d[1], d[2]
    if a.unmapped or b.unmapped:
        continue
    dist = abs(a.tlen) - 1
    ns = (dist - mu) / sd
    o = int(a.tags["AS"] + b.tags["AS"] + .721 * math.log(2. * math.erfc(abs(ns) * math.sqrt(0.5))) * 1 + .499)
    subo = a.tags["AS"] + b.tags["AS"] - 17
    qpe = min(60, max(0, int(6.02 * (o - subo) + .499)))
    exp1 = max(0, min(qpe, 40))
    exp2 = 60
    pt += 1
    good = a.mapq == exp1 and b.mapq == exp2
    pm += good
    if shown < 6 or not good:
        shown += 1
        print("   repeat pair %s TLEN %4d AS %d/%d XS %s/%s  MAPQ %2d/%2d  port %2d/%2d %s"
              % (n, a.tlen, a.tags["AS"], b.tags["AS"], a.tags.get("XS"), b.tags.get("XS"), a.mapq, b.mapq, exp1, exp2,
                 "" if good else "<-- differs"))
ok(pm == pt, "paired MAPQ (repeat mate rescued by a unique mate) equals the port: %d/%d" % (pm, pt))
uq = [d for n, d in by.items() if pmeta[n][0] == "unique" and not d[1].unmapped and not d[2].unmapped]
ok(all(d[1].mapq == 60 and d[2].mapq == 60 for d in uq), "unique perfect pairs get MAPQ 60/60: %d pairs" % len(uq))

# ---------------- length scan across the l = 50 boundary -----------------
# Two copies of a 400-bp segment that differ at exactly one base (segment
# position 200). Reads of 40-60 bp centred on that base from copy 0: AS = L,
# XS = L - 5, sub_n = 1 for every length. The intended factor is 1 at l <= 50
# and ln50/ln(l) above; the compiled one drops from 1 at l = 49 to 0.767 at 50.
rng2 = random.Random(99)
ref2 = list(rand_seq(rng2, 100000))
seg = ref2[20000:20400]
cp = list(seg)
cp[200] = [x for x in "ACGT" if x != cp[200]][0]
ref2[70000:70400] = cp
ref2 = "".join(ref2)
fa2 = os.path.join(WORK, "m1_scan.fa")
write_fasta(fa2, [("chr1", ref2)])
index(fa2)
scan = []
for L in range(40, 61):
    st = 20000 + 200 - L // 2
    scan.append(("L%d" % L, ref2[st:st + L]))
fq = os.path.join(WORK, "m1_scan.fq")
write_fastq(fq, scan)
recs, _ = mem(fa2, fq)
print()
print("   length scan, read from a two-copy segment with one difference (AS = L, XS = L-5):")
print("   %4s %4s %4s %6s %10s %12s" % ("L", "AS", "XS", "MAPQ", "port FAC=3", "port FAC=ln50"))
sm = 0
for r in recs:
    if not r.primary:
        continue
    L = len(r.seq)
    e3 = port_se(r.tags["AS"], r.tags.get("XS", 0), aligned_qlen(r.cigar), ref_span(r.cigar), 1)
    el = port_se(r.tags["AS"], r.tags.get("XS", 0), aligned_qlen(r.cigar), ref_span(r.cigar), 1, fac=math.log(50))
    sm += r.mapq == e3
    print("   %4d %4d %4s %6d %10d %12d" % (L, r.tags["AS"], r.tags.get("XS"), r.mapq, e3, el))
ok(sm == len(scan), "length scan MAPQ equals the port with FAC = 3: %d/%d" % (sm, len(scan)))
