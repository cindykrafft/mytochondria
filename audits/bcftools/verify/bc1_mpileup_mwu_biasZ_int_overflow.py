"""BC1: bcftools mpileup INFO/MQBZ, BQBZ, MQSBZ (RPBZ, SCBZ, NMBZ share the code)
computed by calc_mwu_biasZ() in bam2bcf.c with `int` accumulators.

The tie term t += (p*p-1)*p is evaluated in 32-bit int for p = number of reads
(ref+alt, all samples) sharing one quality bin; it wraps once p >= 1291.
Truth: the tie-corrected normal approximation of the Mann-Whitney U test on
the same binned values (scipy.stats.mannwhitneyu, method="asymptotic",
use_continuity=False), which is the formula the function implements.

Usage: python bc1_mpileup_mwu_biasZ_int_overflow.py /path/to/bcftools
"""
import os, sys, math, tempfile
import numpy as np
from scipy.stats import mannwhitneyu, norm
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import bcftools_bin, version, run, make_ref, make_bam, site_reads, parse_vcf

BIN = bcftools_bin()
print("bcftools:", version(BIN))
D = tempfile.mkdtemp(prefix="bc1_")
REF = os.path.join(D, "ref.fa")
refseq = make_ref(REF, 3000, seed=11)
SITE = 1500                      # 0-based
REFB = refseq[SITE]
ALTB = "A" if REFB != "A" else "C"

def z_truth(a_vals, b_vals):
    """Z of U(b > a) with tie correction, as bcftools defines it (a = ref, b = alt).
    Primary: scipy asymptotic p-value; the direct formula is also returned."""
    a = np.asarray(a_vals); b = np.asarray(b_vals)
    na, nb = len(a), len(b); N = na + nb
    U = float(np.sum(b[:, None] > a[None, :]) + 0.5 * np.sum(b[:, None] == a[None, :]))
    m = na * nb / 2.0
    _, cnt = np.unique(np.concatenate([a, b]), return_counts=True)
    T = float(np.sum(cnt.astype(np.int64) ** 3 - cnt.astype(np.int64)))
    var2 = na * nb / 12.0 * ((N + 1) - T / (N * (N - 1.0)))
    formula = 0.0 if var2 <= 0 else (U - m) / math.sqrt(var2)
    res = mannwhitneyu(b, a, alternative="two-sided", method="asymptotic", use_continuity=False)
    if res.pvalue > 0 and res.pvalue < 1:
        sp = math.copysign(norm.isf(res.pvalue / 2), res.statistic - m)
    else:
        sp = float("nan")
    return formula, sp

def wrap32(x):
    x &= 0xFFFFFFFF
    return x - (1 << 32) if x >= (1 << 31) else x

def z_replica_int32(a_vals, b_vals):
    """calc_mwu_biasZ with the tie product wrapped to 32 bits (bam2bcf.c:846-847)."""
    vals = sorted(set(list(a_vals) + list(b_vals)))
    a = np.asarray(a_vals); b = np.asarray(b_vals)
    na, nb = len(a), len(b); N = na + nb
    U = float(np.sum(b[:, None] > a[None, :]) + 0.5 * np.sum(b[:, None] == a[None, :]))
    m = na * nb / 2.0
    t = 0
    for v in vals:
        p = int(np.sum(a == v) + np.sum(b == v))
        t += wrap32(wrap32(p * p - 1) * p)
    var2 = na * nb / 12.0 * ((N + 1) - t / float(N * (N - 1)))
    return 0.0 if var2 <= 0 else (U - m) / math.sqrt(var2)

def mq_bin(mq):
    if mq == 255: mq = 20            # DEF_MAPQ for the 255 special case
    return min(mq, 59)

def mpileup(bams, maxdepth=None, extra=()):
    args = ["mpileup", "-f", REF, "-B", "-r", "ref:%d-%d" % (SITE + 1, SITE + 1)] + list(extra)
    if maxdepth is not None:
        args += ["-d", str(maxdepth)]
    out = run(BIN, args + list(bams))
    recs = [r for r in parse_vcf(out) if r["POS"] == SITE + 1]
    assert len(recs) == 1, out
    return recs[0]

def getf(rec, tag):
    v = rec["INFO"].get(tag)
    return float(v) if v is not None else None

def report(name, tag, truth, got, replica=None, note=""):
    if got is None:
        print("%-34s %-6s truth %9.4f  bcftools   absent   %s" % (name, tag, truth, note)); return
    ok = abs(got - truth) <= 0.02 * max(1.0, abs(truth))
    line = "%-34s %-6s truth %9.4f  bcftools %9.4f  %s" % (name, tag, truth, got, "ok" if ok else "WRONG")
    if replica is not None:
        line += "  int32-replica %9.4f%s" % (replica, " (=bcftools)" if abs(replica - got) <= 0.02 * max(1.0, abs(got)) else "")
    print(line + ("  " + note if note else ""))
    return ok

# ---------------------------------------------------------------- A: small case, model check
print("\nA. small site (no overflow possible): 30 ref + 12 alt reads, mixed MAPQ, BQ, positions, strands")
ref_mq = [60] * 20 + [40] * 10
alt_mq = [30, 35, 40, 45, 50, 55, 60, 60, 60, 20, 25, 10]
ref_bq = [30 + (i % 12) for i in range(30)]
alt_bq = [15 + 2 * i for i in range(12)]
reads = site_reads(refseq, SITE, 30, REFB, ref_mq, ref_bq, prefix="ref", seed=1) + \
        site_reads(refseq, SITE, 12, ALTB, alt_mq, alt_bq, prefix="alt", seed=2)
bam = make_bam(os.path.join(D, "A.bam"), 3000, reads, rg="A")
rec = mpileup([bam], maxdepth=10000)
print("   ALT=%s DP=%s AD=%s" % (rec["ALT"], rec["INFO"]["DP"], rec["samples"][0].get("AD", "n/a")))
# bins exactly as bam2bcf.c: MQ capped 59 (255->20), BQ capped 59, position bin int((qpos+1)/(len+1)*99)
refr = [r for r in reads if r["name"].startswith("ref")]; altr = [r for r in reads if r["name"].startswith("alt")]
report("A MQBZ (ref_mq vs alt_mq)", "MQBZ", z_truth([mq_bin(r["mapq"]) for r in refr], [mq_bin(r["mapq"]) for r in altr])[0], getf(rec, "MQBZ"))
report("A BQBZ (ref_bq vs alt_bq)", "BQBZ", z_truth([min(r["qual"][SITE - r["pos"]], 59) for r in refr], [min(r["qual"][SITE - r["pos"]], 59) for r in altr])[0], getf(rec, "BQBZ"))
pb = lambda r: int((SITE - r["pos"] + 1) / (len(r["seq"]) + 1) * 99)
report("A RPBZ (ref_pos vs alt_pos)", "RPBZ", z_truth([pb(r) for r in refr], [pb(r) for r in altr])[0], getf(rec, "RPBZ"))
fwd = [mq_bin(r["mapq"]) for r in reads if not r["rev"]]; rev = [mq_bin(r["mapq"]) for r in reads if r["rev"]]
report("A MQSBZ (fwd_mq vs rev_mq)", "MQSBZ", z_truth(fwd, rev)[0], getf(rec, "MQSBZ"))
print("   scipy cross-check of the MQBZ truth (from its p-value): %.4f" % z_truth([mq_bin(r["mapq"]) for r in refr], [mq_bin(r["mapq"]) for r in altr])[1])

# ---------------------------------------------------------------- B: sweep the per-bin count across 1291
print("\nB. one sample, -d 100000: n_ref reads all MAPQ 60 (one bin) + 40 alt reads MAPQ 30; MQBZ vs truth")
print("   1290^3 = %d fits int32; 1291^3 = %d does not (INT32_MAX = %d)" % (1290**3, 1291**3, 2**31 - 1))
for nref in (1000, 1200, 1290, 1291, 1300, 1500, 2000, 2500, 3000, 4000, 5000, 8000, 12000):
    reads = site_reads(refseq, SITE, nref, REFB, [60] * nref, [30] * nref, prefix="ref", seed=3) + \
            site_reads(refseq, SITE, 40, ALTB, [30] * 40, [30] * 40, prefix="alt", seed=4)
    bam = make_bam(os.path.join(D, "B%d.bam" % nref), 3000, reads, rg="B")
    rec = mpileup([bam], maxdepth=100000)
    a = [59] * nref; b = [30] * 40
    tr, sp = z_truth(a, b)
    report("B n_ref=%d (bin 59 holds %d)" % (nref, nref), "MQBZ", tr, getf(rec, "MQBZ"), z_replica_int32(a, b),
           note="scipy %.4f DP=%s" % (sp, rec["INFO"]["DP"]))

# ---------------------------------------------------------------- C: NovaSeq-style binned base qualities -> BQBZ
print("\nC. one sample, -d 100000: binned base qualities (all ref bases Q37; alt bases Q37 x30 + Q12 x10); BQBZ")
for nref in (1000, 1500, 3000):
    alt_bq = [37] * 30 + [12] * 10
    reads = site_reads(refseq, SITE, nref, REFB, [60] * nref, [37] * nref, prefix="ref", seed=5) + \
            site_reads(refseq, SITE, 40, ALTB, [60] * 40, alt_bq, prefix="alt", seed=6)
    bam = make_bam(os.path.join(D, "C%d.bam" % nref), 3000, reads, rg="C")
    rec = mpileup([bam], maxdepth=100000)
    a = [37] * nref; b = alt_bq
    tr, sp = z_truth(a, b)
    report("C n_ref=%d (bin 37 holds %d)" % (nref, nref + 30), "BQBZ", tr, getf(rec, "BQBZ"), z_replica_int32(a, b), note="scipy %.4f" % sp)
    # MQBZ here: everything MAPQ 60 -> single bin, no information; var2 = 0 in exact arithmetic
    print("   (MQBZ with every read in one MAPQ bin: bcftools %s; exact var2 = 0 so Z is undefined/0)" % rec["INFO"].get("MQBZ"))

# ---------------------------------------------------------------- D: default settings, many single-sample BAMs
print("\nD. DEFAULT -d 250, one BAM per sample: every sample 30 ref reads MAPQ 60; 3 samples also carry 10 alt reads MAPQ 30")
for nsmpl in (40, 44, 48, 60, 100):
    bams = []
    ref_bins, alt_bins, fwd, rev = [], [], [], []
    for s in range(nsmpl):
        reads = site_reads(refseq, SITE, 30, REFB, [60] * 30, [30] * 30, prefix="ref", seed=100 + s)
        if s < 3:
            reads += site_reads(refseq, SITE, 10, ALTB, [30] * 10, [30] * 10, prefix="alt", seed=200 + s)
        bams.append(make_bam(os.path.join(D, "D%d_s%03d.bam" % (nsmpl, s)), 3000, reads, rg="s%03d" % s))
        ref_bins += [59] * 30
        alt_bins += [30] * 10 if s < 3 else []
        fwd += [mq_bin(r["mapq"]) for r in reads if not r["rev"]]; rev += [mq_bin(r["mapq"]) for r in reads if r["rev"]]
    rec = mpileup(bams)                       # default -d 250
    tr, sp = z_truth(ref_bins, alt_bins)
    report("D %d samples (bin 59 holds %d)" % (nsmpl, len(ref_bins)), "MQBZ", tr, getf(rec, "MQBZ"), z_replica_int32(ref_bins, alt_bins),
           note="scipy %.4f DP=%s" % (sp, rec["INFO"]["DP"]))
    trs, _ = z_truth(fwd, rev)
    report("D %d samples MQSBZ (fwd %d / rev %d)" % (nsmpl, len(fwd), len(rev)), "MQSBZ", trs, getf(rec, "MQSBZ"), z_replica_int32(fwd, rev))

# ---------------------------------------------------------------- E: same as D but without -B (BAQ on, the default)
print("\nE. as D with 48 samples but BAQ left on (no -B), i.e. the plain default command line")
bams = [os.path.join(D, "D48_s%03d.bam" % s) for s in range(48)]
out = run(BIN, ["mpileup", "-f", REF, "-r", "ref:%d-%d" % (SITE + 1, SITE + 1)] + bams)
rec = [r for r in parse_vcf(out) if r["POS"] == SITE + 1][0]
tr, _ = z_truth([59] * (48 * 30), [30] * 30)
report("E 48 samples, default BAQ", "MQBZ", tr, getf(rec, "MQBZ"), z_replica_int32([59] * (48 * 30), [30] * 30))
print("\ndone; scratch dir", D)
