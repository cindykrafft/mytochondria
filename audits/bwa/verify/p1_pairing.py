"""p1: paired-end insert-size estimation, proper-pair flag, TLEN, mate rescue,
and the orientation classification of same-strand (FF) libraries.

A. FR library, fragments ~ N(300, 40) plus 3 % long outliers, perfect 100-bp
   mates. Port of mem_pestat (bwamem_pair.c) run on the TRUE fragment
   lengths: dist = fragment - 1 (mem_infer_dir measures from the leftmost base
   of one mate to the rightmost base of the other, i.e. TLEN - 1);
   percentiles q[(int)(p*n + .499)], mean/sd over [p25 - 2 IQR, p75 + 2 IQR],
   proper bounds [p25 - 3 IQR, p75 + 3 IQR] widened to mean +/- 4 sd.
   Checked: the printed percentiles/mean/sd/bounds, flag 0x2 on every pair
   against the port's bounds, TLEN = +/- fragment.
B. Mate rescue: mate 2 carries a mismatch every 12 bp (no exact 19-mer, so it
   cannot be seeded); expected to be placed by mate-SW at its true position
   with NM 8 and flag 0x2.
C. FF library (both mates read from the same strand, mate 1 first), with the
   left mate inside an exact two-copy 500-bp repeat and the right mate unique. Both fragment
   strands are equally likely; pairing should behave the same on both.
"""
import random
from _synth import *

rng = random.Random(7)
REF = 600000
ref = list(rand_seq(rng, REF))
rep0, rep1 = 400000, 550000
ref[rep1:rep1 + 500] = ref[rep0:rep0 + 500]
ref = "".join(ref)
fa = os.path.join(WORK, "p1_ref.fa")
write_fasta(fa, [("chr1", ref)])
index(fa)
header("reference 600 kb random, one exact 500-bp repeat (copies 150 kb apart)")


def pestat_port(dists, max_ins=10000):
    q = sorted(d for d in dists if 0 < d <= max_ins)
    n = len(q)
    p25 = q[int(.25 * n + .499)]
    p50 = q[int(.50 * n + .499)]
    p75 = q[int(.75 * n + .499)]
    low = int(p25 - 2.0 * (p75 - p25) + .499)
    low = max(low, 1)
    high = int(p75 + 2.0 * (p75 - p25) + .499)
    sel = [x for x in q if low <= x <= high]
    avg = sum(sel) / len(sel)
    sd = math.sqrt(sum((x - avg) ** 2 for x in sel) / len(sel))
    low = int(p25 - 3.0 * (p75 - p25) + .499)
    high = int(p75 + 3.0 * (p75 - p25) + .499)
    if low > avg - 4 * sd:
        low = int(avg - 4 * sd + .499)
    if high < avg + 4 * sd:
        high = int(avg + 4 * sd + .499)
    low = max(low, 1)
    return dict(n=n, p25=p25, p50=p50, p75=p75, avg=avg, sd=sd, low=low, high=high)


def parse_pestat(err, orient="FR"):
    lines = err.splitlines()
    out = {}
    on = False
    for l in lines:
        if "analyzing insert size distribution for orientation %s" % orient in l:
            on = True
            continue
        if on:
            if "percentile" in l:
                out["p25"], out["p50"], out["p75"] = [int(x) for x in re.findall(r"\((\d+), (\d+), (\d+)\)", l)[-1]]
            elif "mean and std.dev" in l:
                out["avg"], out["sd"] = [float(x) for x in re.findall(r"\(([\d.]+), ([\d.]+)\)", l)[0]]
            elif "boundaries for proper pairs" in l:
                out["low"], out["high"] = [int(x) for x in re.findall(r"\((\d+), (\d+)\)", l)[0]]
                break
    m = re.search(r"candidate unique pairs for \(FF, FR, RF, RR\): \((\d+), (\d+), (\d+), (\d+)\)", err)
    out["cand"] = tuple(int(x) for x in m.groups()) if m else None
    return out


def pairs_by_name(recs):
    by = {}
    for r in recs:
        if r.primary:
            by.setdefault(r.qname, {})[1 if r.flag & 64 else 2] = r
    return by


# ---------------- A: FR library ----------------
L = 100
p1, p2, truth = [], [], {}
for j in range(3000):
    if j % 33 == 0:
        frag = rng.randrange(600, 3000)
    else:
        frag = max(L + 20, int(round(rng.gauss(300, 40))))
    while True:
        st = rng.randrange(1000, REF - 4000)
        if not (st < rep0 + 600 and st + frag > rep0 - 100) and not (st < rep1 + 600 and st + frag > rep1 - 100):
            break
    f = ref[st:st + frag]
    m1, m2 = f[:L], revcomp(f[-L:])
    if rng.random() < 0.5:         # fragment from the reverse strand: mate 1 is the reverse read
        m1, m2 = m2, m1
    n = "a%d" % j
    truth[n] = (st, frag)
    p1.append((n, m1)); p2.append((n, m2))
fq1 = os.path.join(WORK, "p1a_1.fq"); fq2 = os.path.join(WORK, "p1a_2.fq")
write_fastq(fq1, p1); write_fastq(fq2, p2)
recs, err = mem(fa, fq1, fq2)
got = parse_pestat(err)
port = pestat_port([truth[n][1] - 1 for n in truth])
print("A. FR library, %d pairs (3 %% long outliers)" % len(truth))
print("   bwa : candidates %s  (25,50,75) = (%d, %d, %d)  mean %.2f sd %.2f  proper [%d, %d]"
      % (got["cand"], got["p25"], got["p50"], got["p75"], got["avg"], got["sd"], got["low"], got["high"]))
print("   port: candidates %d          (25,50,75) = (%d, %d, %d)  mean %.2f sd %.2f  proper [%d, %d]"
      % (port["n"], port["p25"], port["p50"], port["p75"], port["avg"], port["sd"], port["low"], port["high"]))
tl = [truth[n][1] for n in truth]
tl_sel = [x for x in tl if port["low"] <= x - 1 <= port["high"]]
print("   true fragment mean over the same pairs: %.2f (bwa's 'mean' is the mean of TLEN - 1)" % (sum(tl_sel) / len(tl_sel)))
same = all(abs(got[k] - port[k]) < 0.006 for k in ("p25", "p50", "p75", "avg", "sd", "low", "high"))
ok(same, "insert-size statistics equal the port of mem_pestat on the true fragment lengths")
by = pairs_by_name(recs)
fl_ok = tl_ok = 0
for n, d in by.items():
    st, frag = truth[n]
    exp_proper = port["low"] <= frag - 1 <= port["high"]
    a, b = d[1], d[2]
    fl_ok += (bool(a.flag & 2) == exp_proper) and (bool(b.flag & 2) == exp_proper)
    tl_ok += abs(a.tlen) == frag and a.tlen == -b.tlen
ok(fl_ok == len(by), "flag 0x2 set exactly when fragment-1 lies in the port's bounds: %d/%d" % (fl_ok, len(by)))
ok(tl_ok == len(by), "TLEN = +/- fragment length: %d/%d" % (tl_ok, len(by)))

# ---------------- B: mate rescue ----------------
p1b, p2b, tb = [], [], {}
for j in range(200):
    frag = max(L + 20, int(round(rng.gauss(300, 40))))
    st = rng.randrange(1000, 390000)
    f = ref[st:st + frag]
    m1 = f[:L]
    m2f = f[-L:]
    for p in range(6, L, 12):
        m2f = mutate_sub(rng, m2f, p)
    n = "b%d" % j
    tb[n] = (st, frag)
    p1b.append((n, m1)); p2b.append((n, revcomp(m2f)))
# add 2000 normal pairs so the batch has an insert-size estimate
for j in range(2000):
    frag = max(L + 20, int(round(rng.gauss(300, 40))))
    st = rng.randrange(1000, 390000)
    f = ref[st:st + frag]
    n = "bn%d" % j
    p1b.append((n, f[:L])); p2b.append((n, revcomp(f[-L:])))
fq1 = os.path.join(WORK, "p1b_1.fq"); fq2 = os.path.join(WORK, "p1b_2.fq")
write_fastq(fq1, p1b); write_fastq(fq2, p2b)
recs, err = mem(fa, fq1, fq2)
by = pairs_by_name(recs)
resc = 0
for n, (st, frag) in tb.items():
    b = by[n][2]
    if not b.unmapped and b.pos == st + frag - L + 1 and b.tags.get("NM") == 8 and b.flag & 2:
        resc += 1
print("B. mate rescue: mates with a mismatch every 12 bp")
ok(resc == len(tb), "rescued at the true position with NM 8 and flag 0x2: %d/%d" % (resc, len(tb)))
qs = sorted(set(by[n][2].mapq for n in tb if not by[n][2].unmapped))
print("   MAPQ of the rescued mates: %s" % qs)

# ---------------- C: FF library ----------------
p1c, p2c, tc = [], [], {}
for j in range(2400):
    frag = max(L + 20, int(round(rng.gauss(300, 40))))
    if j < 400:
        st = rep0 + rng.randrange(380, 400)  # mate 1 ends inside the repeat copy at rep0
        frag = max(frag, 300)
    else:
        while True:
            st = rng.randrange(1000, REF - 2000)
            if not (st < rep0 + 600 and st + frag > rep0 - 100) and not (st < rep1 + 600 and st + frag > rep1 - 100):
                break
    f = ref[st:st + frag]
    strand = j % 2
    if strand:                     # fragment from the reverse strand
        g = revcomp(f)
        m1, m2 = g[:L], g[-L:]
    else:
        m1, m2 = f[:L], f[-L:]
    n = "c%d" % j
    tc[n] = (st, frag, strand, j < 400)
    p1c.append((n, m1)); p2c.append((n, m2))
fq1 = os.path.join(WORK, "p1c_1.fq"); fq2 = os.path.join(WORK, "p1c_2.fq")
write_fastq(fq1, p1c); write_fastq(fq2, p2c)
recs, err = mem(fa, fq1, fq2)
gotc = parse_pestat(err, "FF")
print("C. FF library: candidate pairs (FF, FR, RF, RR) = %s; FF proper bounds [%s, %s]"
      % (gotc["cand"], gotc.get("low"), gotc.get("high")))
by = pairs_by_name(recs)
stats = {}
for n, (st, frag, strand, isrep) in tc.items():
    a, b = by[n][1], by[n][2]
    k = ("repeat mate" if isrep else "unique", "fwd fragment" if strand == 0 else "rev fragment")
    # the mate covering [st, st+L) is mate 1 on a forward fragment, mate 2 on a reverse one
    m = a if strand == 0 else b
    s = stats.setdefault(k, [0, 0, 0, []])
    s[0] += 1
    s[1] += bool(m.flag & 2)
    s[2] += m.pos == st + 1
    s[3].append(m.mapq)
for k in sorted(stats):
    s = stats[k]
    print("   %-12s %-13s n=%4d  flag 0x2 %4d  left mate at its true copy %4d  its MAPQ: %s"
          % (k[0], k[1], s[0], s[1], s[2], ", ".join("%d x%d" % (q, s[3].count(q)) for q in sorted(set(s[3])))))
fw = stats[("repeat mate", "fwd fragment")]
rv = stats[("repeat mate", "rev fragment")]
ok(fw[2] == rv[2] and fw[1] == rv[1] and sorted(fw[3]) == sorted(rv[3]),
   "FF library: repeat mates placed, flagged and scored the same on both fragment strands "
   "(true copy fwd %d/%d, rev %d/%d; flag 0x2 fwd %d, rev %d)" % (fw[2], fw[0], rv[2], rv[0], fw[1], rv[1]))
