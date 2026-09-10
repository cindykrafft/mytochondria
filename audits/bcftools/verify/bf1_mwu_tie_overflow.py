#!/usr/bin/env python3
"""BF1: the tie-correction term of the Mann-Whitney U Z-scores (MQBZ, BQBZ, RPBZ,
MQSBZ, SCBZ, NMBZ) overflows 32-bit int once a single histogram bin holds >= 1291
reads, so the reported Z is wrong for deep or multi-sample pileups.

bam2bcf.c calc_mwu_biasZ():
    int64_t t; ... int p = a[i]+b[i]; t += (p*p-1)*p;
(p*p-1)*p is evaluated in int before the add: p^3 > 2^31-1 for p >= 1291.

Truth: the same statistic (U = #pairs ref<alt + ties/2, tie-corrected variance,
Z = (U-m)/sd, see https://en.wikipedia.org/wiki/Mann-Whitney_U_test) in Python
integers, cross-checked against scipy.stats.mannwhitneyu (asymptotic, no
continuity correction, tie-corrected), plus a replica of the overflowing
arithmetic to show it predicts the shipped number.

usage: python bf1_mwu_tie_overflow.py /path/to/bcftools
"""
import os, sys, math, random, tempfile
import numpy as np
from scipy.stats import mannwhitneyu, norm
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import write_ref, Bam, run, version, vcf_records

BIN = sys.argv[1]
print("binary:", version(BIN))
tmp = tempfile.mkdtemp(prefix="bf1_")
REF = write_ref(os.path.join(tmp, "ref.fa"), 3000, seed=7)
SITE = 1500          # 1-based
RL = 100
ALT = {"A": "C", "C": "G", "G": "T", "T": "A"}[REF[SITE-1]]

def make_bam(path, reads, sample="S1"):
    """reads: list of (is_alt, mapq, baseq)"""
    rnd = random.Random(11)
    b = Bam(path, len(REF), sample)
    for i, (is_alt, mq, bq) in enumerate(reads):
        start = SITE - 1 - rnd.randint(10, RL-11)       # covers SITE, away from the read ends
        seq = list(REF[start:start+RL])
        if is_alt:
            seq[SITE-1-start] = ALT
        b.add("r%d_%s" % (i, sample), start, "".join(seq), chr(33+bq)*RL, mapq=mq, rev=(i % 2 == 1))
    return b.write()

def z_true(a_vals, b_vals):
    """Tie-corrected Mann-Whitney Z exactly as bam2bcf.c defines it, in Python ints."""
    nb_ = 60
    a = [0]*nb_; b = [0]*nb_
    for v in a_vals: a[min(v, 59)] += 1
    for v in b_vals: b[min(v, 59)] += 1
    e = l = na = nb = t = 0
    for i in range(nb_-1, -1, -1):
        e += a[i]*b[i]
        l += a[i]*nb
        na += a[i]; nb += b[i]
        p = a[i]+b[i]
        t += (p*p-1)*p
    U = l + e*0.5
    m = na*nb/2.0
    var2 = (na*nb)/12.0 * ((na+nb+1) - t/float((na+nb)*(na+nb-1)))
    return (U-m)/math.sqrt(var2), t

def z_int32_replica(a_vals, b_vals):
    """The same, but with (p*p-1)*p wrapped to a signed 32-bit int as the C code does."""
    nb_ = 60
    a = [0]*nb_; b = [0]*nb_
    for v in a_vals: a[min(v, 59)] += 1
    for v in b_vals: b[min(v, 59)] += 1
    e = l = na = nb = t = 0
    def wrap(x):
        x &= 0xFFFFFFFF
        return x - (1 << 32) if x >= (1 << 31) else x
    for i in range(nb_-1, -1, -1):
        e += a[i]*b[i]; l += a[i]*nb; na += a[i]; nb += b[i]
        p = a[i]+b[i]
        t += wrap(wrap(wrap(p*p)-1)*p)
    U = l + e*0.5; m = na*nb/2.0
    var2 = (na*nb)/12.0 * ((na+nb+1) - t/float((na+nb)*(na+nb-1)))
    if var2 <= 0: return 0.0
    return (U-m)/math.sqrt(var2)

def scipy_p(a_vals, b_vals):
    return mannwhitneyu(a_vals, b_vals, alternative="two-sided", method="asymptotic", use_continuity=False).pvalue

def mpileup(bams, extra):
    out, err = run(BIN, ["mpileup", "-f", REF_PATH, "-B", "-a", "INFO/AD"] + extra + bams)
    recs = [r for r in vcf_records(out) if r["pos"] == SITE]
    assert len(recs) == 1, out[-2000:]
    return recs[0]

REF_PATH = os.path.join(tmp, "ref.fa")

def case(label, n_ref60, n_alt60, n_alt30, extra=("-d", "100000"), nfiles=1):
    """n_ref60 ref reads at MQ60, n_alt60 alt reads at MQ60, n_alt30 alt reads at MQ30,
    all base quality 40; spread over nfiles BAMs (one sample each)."""
    reads = [(0, 60, 40)]*n_ref60 + [(1, 60, 40)]*n_alt60 + [(1, 30, 40)]*n_alt30
    random.Random(3).shuffle(reads)
    bams = []
    for k in range(nfiles):
        chunk = reads[k::nfiles]
        bams.append(make_bam(os.path.join(tmp, "%s_%d.bam" % (label, k)), chunk, "S%d" % (k+1)))
    rec = mpileup(bams, list(extra))
    ref_mq = [60]*n_ref60
    alt_mq = [60]*n_alt60 + [30]*n_alt30
    z, t = z_true(ref_mq, alt_mq)
    zrep = z_int32_replica(ref_mq, alt_mq)
    p_sc = scipy_p(ref_mq, alt_mq)
    p_z = 2*norm.sf(abs(z))
    got = rec["info"].get("MQBZ", "absent")
    n = n_ref60+n_alt60+n_alt30
    print("\n[%s] %d reads in %d file(s) (%d ref MQ60, %d alt MQ60, %d alt MQ30); DP=%s AD=%s"
          % (label, n, nfiles, n_ref60, n_alt60, n_alt30, rec["info"].get("DP"), rec["info"].get("AD")))
    print("  largest tie bin p = %d, p^3 = %d (int32 max 2147483647) -> %s"
          % (n_ref60+n_alt60, (n_ref60+n_alt60)**3, "OVERFLOWS" if (n_ref60+n_alt60)**3 > 2**31-1 else "fits"))
    print("  truth: Z = %.4f  (scipy two-sided p = %.3e, p from Z = %.3e)" % (z, p_sc, p_z))
    print("  int32-wrap replica of the C code: Z = %.4f" % zrep)
    print("  bcftools INFO/MQBZ = %s" % got)
    if got == "absent":
        print("  -> NOT APPLICABLE: this version has no Z-score annotations (pre-1.13; INFO/MQB = %s is the old probability score)" % rec["info"].get("MQB"))
        return rec
    try:
        g = float(got)
        ok = abs(g - z) < 0.01
        print("  -> %s (|got-truth| = %.4f; |got-replica| = %.4f)" % ("MATCHES TRUTH" if ok else "WRONG", abs(g-z), abs(g-zrep)))
    except ValueError:
        print("  -> annotation not produced by this version")
    return rec

# A: below the threshold (largest bin 1200 < 1291): must agree with truth
case("A_1200reads", 1140, 60, 40)
# B: above the threshold in one deep sample (-d raised, as for amplicon/mtDNA data)
case("B_1500reads", 1400, 60, 40)
# C: a 30-sample cohort at ~100x, everything under the default -d 250 per file
case("C_cohort30x100", 2850, 100, 50, extra=(), nfiles=30)
# D: 3000 reads, alt reads all MQ60 too except 5% at MQ30 -- a mild bias, typical of a real site
case("D_3000_mild", 2850, 140, 10)
# E: BQBZ through the same function: ref at BQ40, alt half BQ40 half BQ20
def case_bq(label, n_ref, n_alt40, n_alt20, extra=("-d", "100000")):
    reads = [(0, 60, 40)]*n_ref + [(1, 60, 40)]*n_alt40 + [(1, 60, 20)]*n_alt20
    random.Random(5).shuffle(reads)
    bam = make_bam(os.path.join(tmp, label + ".bam"), reads)
    rec = mpileup([bam], list(extra))
    z, _ = z_true([40]*n_ref, [40]*n_alt40 + [20]*n_alt20)
    zrep = z_int32_replica([40]*n_ref, [40]*n_alt40 + [20]*n_alt20)
    got = rec["info"].get("BQBZ", "absent")
    print("\n[%s] %d reads (%d ref BQ40, %d alt BQ40, %d alt BQ20)" % (label, n_ref+n_alt40+n_alt20, n_ref, n_alt40, n_alt20))
    print("  truth Z = %.4f ; int32-wrap replica Z = %.4f ; bcftools INFO/BQBZ = %s" % (z, zrep, got))
    if got == "absent":
        print("  -> NOT APPLICABLE: no Z-score annotations in this version (INFO/BQB = %s)" % rec["info"].get("BQB")); return
    try:
        g = float(got); print("  -> %s" % ("MATCHES TRUTH" if abs(g-z) < 0.01 else "WRONG (|got-truth| = %.4f, |got-replica| = %.4f)" % (abs(g-z), abs(g-zrep))))
    except ValueError:
        print("  -> annotation not produced by this version")
case_bq("E_bq_1200", 1140, 30, 30)
case_bq("F_bq_1500", 1440, 30, 30)
