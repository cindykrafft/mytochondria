"""Held-up checks for bcftools mpileup counting and per-read quality handling:
INFO/DP, FORMAT/DP, AD, ADF, ADR, DP4, SP (Fisher strand), I16 sums, MQ0F under
default settings and under -Q/-q filters; the -d per-file cap; single-read PL.
Truth computed in Python from the synthetic reads (bam2bcf.c rules cited inline).

Usage: python heldup_mpileup_counts.py /path/to/bcftools
"""
import os, sys, math, random, tempfile
from scipy.stats import fisher_exact
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import bcftools_bin, version, run, make_ref, make_bam, parse_vcf

BIN = bcftools_bin()
print("bcftools:", version(BIN))
D = tempfile.mkdtemp(prefix="hm_")
REF = os.path.join(D, "ref.fa")
refseq = make_ref(REF, 3000, seed=21)
SITE = 1500
REFB = refseq[SITE]
OTHER = [b for b in "ACGT" if b != REFB]
ALTB, THIRD = OTHER[0], OTHER[1]
rng = random.Random(5)
nfail = 0

def mk(name, base, off, mapq, bq, rev, cigar=None, read_len=100, site=SITE):
    pos = site - off
    seq = list(refseq[pos:pos+read_len]); seq[off] = base
    qual = [30] * read_len; qual[off] = bq
    r = dict(name=name, pos=pos, seq="".join(seq), qual=qual, mapq=mapq, rev=rev)
    if cigar: r["cigar"] = cigar
    return r

# A mixed site: ref/alt/third bases, BQ 0..40, MQ 0..60 and 255, both strands, plus one read
# whose deletion spans the site and one read whose N (ref-skip) spans the site.
reads = []
spec = []   # (kind, base, mapq, bq, rev, off)
for i in range(60):
    base = REFB if i % 3 else ALTB
    if i in (7, 31): base = THIRD
    mapq = [60, 60, 60, 40, 20, 10, 0, 255, 60, 30][i % 10]
    bq = [30, 40, 20, 13, 12, 5, 0, 30, 41, 2][i % 10] if i % 3 else [30, 25, 12, 13, 41][i % 5]
    rev = bool(rng.getrandbits(1)); off = rng.randrange(3, 97)
    reads.append(mk("r%03d" % i, base, off, mapq, bq, rev)); spec.append((base, mapq, bq, rev, off))
# deletion read: 40M5D55M with the site inside the deletion (pos = SITE-42: bases 0..39 then del 40..44)
dpos = SITE - 42
dseq = refseq[dpos:dpos+40] + refseq[dpos+45:dpos+100]
reads.append(dict(name="del", pos=dpos, seq=dseq, qual=[30]*95, mapq=60, rev=False, cigar=[(0,40),(2,5),(0,55)]))
reads.append(dict(name="skip", pos=dpos, seq=dseq, qual=[30]*95, mapq=60, rev=False, cigar=[(0,40),(3,5),(0,55)]))
bam = make_bam(os.path.join(D, "A.bam"), 3000, reads, rg="A")

def truth(min_bq, min_mq):
    """bam2bcf.c bcf_call_glfgen: reads with MAPQ<min_mq are dropped before pileup (mpileup.c:293);
    is_del/is_refskip reads skipped (:301,:307); INFO/DP=ori_depth counted before the BQ test (:311);
    bases with q<min_baseQ skipped (:437); mapQ 255->20 (:452), capped 60 (:460); baseQ capped 60."""
    t = dict(DP=0, dp4=[0,0,0,0], ad=[0,0,0], adf=[0,0,0], adr=[0,0,0], I16=[0.0]*16, mq0=0)
    for base, mapq, bq, rev, off in spec:
        if mapq < min_mq: continue
        t["DP"] += 1
        if bq < min_bq: continue
        mq = 20 if mapq == 255 else mapq
        if mq == 0: t["mq0"] += 1
        mq = min(mq, 60); bqc = min(bq, 60)
        is_diff = 0 if base == REFB else 1
        ai = 0 if base == REFB else (1 if base == ALTB else 2)
        t["ad"][ai] += 1; (t["adr"] if rev else t["adf"])[ai] += 1
        t["dp4"][is_diff*2 + rev] += 1
        min_dist = min(off, 99 - off, 25)
        I = t["I16"]
        I[4 + is_diff*2] += bqc; I[5 + is_diff*2] += bqc*bqc
        I[8 + is_diff*2] += mq; I[9 + is_diff*2] += mq*mq
        I[12 + is_diff*2] += min_dist; I[13 + is_diff*2] += min_dist*min_dist
    t["I16"][0:4] = t["dp4"]
    fr, rr, fa, ra = t["dp4"]
    if fr+rr < 2 or fa+ra < 2 or fr+fa < 2 or rr+ra < 2: t["SP"] = 0
    else:
        p = fisher_exact([[fr, rr], [fa, ra]])[1]
        t["SP"] = min(255, int(-4.343*math.log(p) + .499))
    t["MQ0F"] = t["mq0"] / t["DP"] if t["DP"] else 0
    return t

def check(label, got, exp):
    global nfail
    ok = got == exp
    if not ok: nfail += 1
    print("   %-28s bcftools %-22s truth %-22s %s" % (label, got, exp, "ok" if ok else "MISMATCH"))

def order_alleles(rec):
    """map truth allele order [REF, ALTB, THIRD] onto the record's ALT order"""
    alts = rec["ALT"].split(",")
    idx = [0]
    for a in alts:
        if a == "<*>": continue
        idx.append({ALTB: 1, THIRD: 2}[a])
    return idx

for label, extra, min_bq, min_mq in (("default (-Q 1, -q 0)", [], 1, 0), ("-Q 13", ["-Q", "13"], 13, 0),
                                     ("-q 20", ["-q", "20"], 0 if False else 1, 20), ("-Q 20 -q 30", ["-Q", "20", "-q", "30"], 20, 30)):
    out = run(BIN, ["mpileup", "-f", REF, "-B", "-r", "ref:%d-%d" % (SITE+1, SITE+1),
                    "-a", "FORMAT/AD,FORMAT/ADF,FORMAT/ADR,FORMAT/DP,FORMAT/SP,FORMAT/DP4,INFO/AD,INFO/ADF,INFO/ADR"] + extra + [bam])
    rec = [r for r in parse_vcf(out) if r["POS"] == SITE+1][0]
    t = truth(min_bq, min_mq)
    idx = order_alleles(rec)
    print("\n%s: ALT=%s" % (label, rec["ALT"]))
    s = rec["samples"][0]
    check("INFO/DP (raw, pre -Q)", int(rec["INFO"]["DP"]), t["DP"])
    check("FORMAT/DP (post -Q)", int(s["DP"]), sum(t["dp4"]))
    check("FORMAT/DP4 rf,rr,af,ar", [int(x) for x in s["DP4"].split(",")], t["dp4"])
    ad_t = [t["ad"][i] for i in idx] + ([0] if "<*>" in rec["ALT"] else [])
    check("FORMAT/AD", [int(x) for x in s["AD"].split(",")], ad_t)
    check("FORMAT/ADF", [int(x) for x in s["ADF"].split(",")], [t["adf"][i] for i in idx] + ([0] if "<*>" in rec["ALT"] else []))
    check("FORMAT/ADR", [int(x) for x in s["ADR"].split(",")], [t["adr"][i] for i in idx] + ([0] if "<*>" in rec["ALT"] else []))
    check("INFO/AD", [int(x) for x in rec["INFO"]["AD"].split(",")], ad_t)
    check("FORMAT/SP (Fisher, phred)", int(s["SP"]), t["SP"])
    got16 = [float(x) for x in rec["INFO"]["I16"].split(",")]
    check("INFO/I16 (16 sums)", got16, [float(x) for x in t["I16"]])
    check("INFO/MQ0F", round(float(rec["INFO"]["MQ0F"]), 5), round(t["MQ0F"], 5))
    # INFO/MQ after `call`: (I16[8]+I16[10])/DP4sum, i.e. the plain mean of capped MAPQ (mcall.c:1663)
    outc = run(BIN, ["call", "-m", "-A"], stdin=out)
    recc = [r for r in parse_vcf(outc) if r["POS"] == SITE+1][0]
    mq_t = (t["I16"][8] + t["I16"][10]) / sum(t["dp4"]) if sum(t["dp4"]) else 0
    check("call INFO/MQ (mean MAPQ)", round(float(recc["INFO"]["MQ"]), 2), round(mq_t, 2))

# -d per-file cap
print("\n-d per-file cap: 400 ref reads with random starts, -d 100 / -d 250 (default) / -d 0  (printed, not checked: see note)")
reads = [mk("c%03d" % i, REFB, rng.randrange(3, 97), 60, 30, bool(i % 2)) for i in range(400)]
bamc = make_bam(os.path.join(D, "C.bam"), 3000, reads, rg="C")
for d in (["-d", "100"], [], ["-d", "0"]):
    out = run(BIN, ["mpileup", "-f", REF, "-B", "-r", "ref:%d-%d" % (SITE+1, SITE+1), "-a", "FORMAT/DP"] + d + [bamc])
    rec = [r for r in parse_vcf(out) if r["POS"] == SITE+1][0]
    print("   INFO/DP with %-8s bcftools %s   (400 reads overlap the site)" % (" ".join(d) or "default", rec["INFO"]["DP"]))
print("   htslib sam.c bam_plp_push drops a read only when it STARTS at the current position while the buffer already holds")
print("   more than maxcnt reads (sam.c:6139), so the per-position depth can exceed -d; the cap is a memory guard, not a depth.")

# indel smoke test: a clean heterozygous 3-bp deletion at 40x
print("\nindel: 20 ref reads + 20 reads carrying a CAG deletion, mpileup | call -m (no -B)")
dsite = 2000
dreads = []
for i in range(20):
    dreads.append(mk("ir%02d" % i, refseq[dsite], 30 + i, 60, 30, bool(i % 2), site=dsite))
for i in range(20):
    off = 30 + i; pos = dsite - off
    seq = refseq[pos:pos + off + 1] + refseq[pos + off + 4:pos + 100 + 3]
    dreads.append(dict(name="id%02d" % i, pos=pos, seq=seq, qual=[30] * len(seq), mapq=60, rev=bool(i % 2), cigar=[(0, off + 1), (2, 3), (0, len(seq) - off - 1)]))
dbam = make_bam(os.path.join(D, "indel.bam"), 3000, dreads, rg="I")
out = run(BIN, ["mpileup", "-f", REF, "-a", "FORMAT/AD", "-r", "ref:%d-%d" % (dsite - 5, dsite + 5), dbam])
outc = run(BIN, ["call", "-mv"], stdin=out)
for r in parse_vcf(outc):
    print("   %s %d %s>%s QUAL=%s GT=%s AD=%s IDV=%s IMF=%s" % (r["CHROM"], r["POS"], r["REF"], r["ALT"], r["QUAL"], r["samples"][0]["GT"], r["samples"][0].get("AD"), r["INFO"].get("IDV"), r["INFO"].get("IMF")))
    check("indel called at the site with the 3-bp deletion", (r["POS"], len(r["REF"]) - len(r["ALT"].split(",")[0]), r["samples"][0]["GT"]), (dsite + 1, 3, "0/1"))

# single-read and two-read PL
print("\nPL for tiny pileups (errmod_cal, htslib errmod.c; theta=0.83 dependency model): values printed for the record")
for label, rs in (("1 ref read Q10", [mk("a", REFB, 50, 60, 10, False)]), ("1 ref read Q20", [mk("a", REFB, 50, 60, 20, False)]),
                  ("1 ref read Q30", [mk("a", REFB, 50, 60, 30, False)]), ("1 alt read Q30", [mk("a", ALTB, 50, 60, 30, False)]),
                  ("1 ref read Q30 MQ0", [mk("a", REFB, 50, 0, 30, False)]),
                  ("2 ref reads Q30", [mk("a", REFB, 50, 60, 30, False), mk("b", REFB, 40, 60, 30, True)]),
                  ("1 ref + 1 alt Q30", [mk("a", REFB, 50, 60, 30, False), mk("b", ALTB, 40, 60, 30, True)]),
                  ("5 ref reads Q30", [mk("r%d" % i, REFB, 30+i, 60, 30, bool(i%2)) for i in range(5)]),
                  ("5 alt reads Q30", [mk("r%d" % i, ALTB, 30+i, 60, 30, bool(i%2)) for i in range(5)])):
    b = make_bam(os.path.join(D, "pl.bam"), 3000, rs, rg="P")
    out = run(BIN, ["mpileup", "-f", REF, "-B", "-r", "ref:%d-%d" % (SITE+1, SITE+1), b])
    rec = [r for r in parse_vcf(out) if r["POS"] == SITE+1][0]
    print("   %-22s ALT=%-6s PL=%s" % (label, rec["ALT"], rec["samples"][0]["PL"]))

print("\nmismatches:", nfail)
