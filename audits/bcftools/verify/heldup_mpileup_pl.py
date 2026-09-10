#!/usr/bin/env python3
"""Held-up: bcftools mpileup genotype likelihoods (PL) and its per-site annotations
against an independent Python port of the model.

Truth: a port of HTSlib errmod.c (MAQ-style error model with dependency correction,
theta=0.83, eta=0.03) fed with the same per-base quality rules as bam2bcf.c
bcf_call_glfgen() (neighbour-quality rule with --delta-BQ 30, --max-BQ 60, -Q, MAPQ cap 60,
q in [4,63]), then bcf_call_combine()'s allele ordering by summed normalised QS and
PL = round(p - min), capped at 255. Also DP, AD/ADF/ADR, DP4, QS, I16, MQ0F and SP
(Fisher exact two-sided on DP4, phred-scaled; cross-checked with scipy) and, after
`call -m`, DP4 and MQ. Reads have random per-base qualities so the neighbour rule fires.

usage: python heldup_mpileup_pl.py /path/to/bcftools
"""
import os, sys, math, random, tempfile
from scipy.stats import fisher_exact
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import write_ref, Bam, run, version, vcf_records

BIN = sys.argv[1]
print("binary:", version(BIN))
tmp = tempfile.mkdtemp(prefix="mp_")
REF_PATH = os.path.join(tmp, "ref.fa")
REF = write_ref(REF_PATH, 2000, seed=3)
SITE = 1000
RL = 80
rnd = random.Random(9)
NT = "ACGT"

# ---------------- errmod port ----------------
THETA, ETA = 0.83, 0.03
DEPCORR = 1 - THETA
FK = [1.0] + [(1 - DEPCORR)**n * (1 - ETA) + ETA for n in range(1, 256)]
_lfact = [0.0]*260
for i in range(1, 260): _lfact[i] = _lfact[i-1] + math.log(i)
def lC(n, k): return _lfact[n] - _lfact[k] - _lfact[n-k]
_beta_cache = {}
def beta(q, n, k):
    key = (q, n)
    if key not in _beta_cache:
        e = 10.0**(-q/10.0); le = math.log(e); le1 = math.log(1 - e)
        b = [0.0]*(n+1)
        sum1 = lC(n, n) + n*le
        b[n] = float("inf")
        for kk in range(n-1, -1, -1):
            s = sum1 + math.log1p(math.exp(lC(n, kk) + kk*le + (n-kk)*le1 - sum1))
            b[kk] = -10.0/math.log(10) * (sum1 - s)
            sum1 = s
        _beta_cache[key] = b
    return _beta_cache[key][k]
def lhet(n, k): return lC(n, k) - math.log(2)*n

def errmod_cal(bases, m=5):
    """bases: list of (q, strand, base) ; returns 5x5 phred-scaled likelihood matrix."""
    n = len(bases)
    assert n <= 255
    enc = sorted(b[0] << 5 | b[1] << 4 | b[2] for b in bases)
    w = [0]*32; fsum = [0.0]*16; bsum = [0.0]*16; c = [0]*16
    for j in range(n-1, -1, -1):
        b = enc[j]
        qual = 4 if (b >> 5) < 4 else (b >> 5)
        qual = min(qual, 63)
        bs = b & 0x1f; base = b & 0xf
        fsum[base] += FK[w[bs]]
        bsum[base] += FK[w[bs]] * beta(qual, n, c[base])
        c[base] += 1; w[bs] += 1
    q = [[0.0]*m for _ in range(m)]
    for j in range(m):
        t1 = sum(bsum[k] for k in range(m) if k != j); t2 = sum(c[k] for k in range(m) if k != j)
        if t2: q[j][j] = t1
        for k in range(j+1, m):
            cjk = c[j] + c[k]
            o1 = sum(bsum[i] for i in range(m) if i not in (j, k)); o2 = sum(c[i] for i in range(m) if i not in (j, k))
            v = -4.343*lhet(cjk, c[k]) + (o1 if o2 else 0.0)
            q[j][k] = q[k][j] = v
        for k in range(m): q[j][k] = max(q[j][k], 0.0)
    return q

# ---------------- synthetic data ----------------
ref_base = REF[SITE-1]
alts = [b for b in NT if b != ref_base]
ALT1, ALT2 = alts[0], alts[1]
samples = ["S1", "S2"]
reads = {}   # sample -> list of dicts
for si, s in enumerate(samples):
    lst = []
    n = 70 if si == 0 else 40
    for i in range(n):
        r = rnd.random()
        base = ref_base if r < 0.55 else (ALT1 if r < 0.9 else ALT2)
        if si == 1 and r >= 0.9: base = ref_base      # S2: no second alt
        start = SITE - 1 - rnd.randint(3, RL-4)
        quals = [rnd.choice([8, 15, 20, 25, 30, 35, 40, 45]) for _ in range(RL)]
        mq = rnd.choice([60, 60, 60, 40, 20, 0, 255])
        rev = rnd.random() < 0.5
        seq = list(REF[start:start+RL]); seq[SITE-1-start] = base
        lst.append(dict(name="%s_r%d" % (s, i), start=start, seq="".join(seq), quals=quals, mq=mq, rev=rev, qpos=SITE-1-start, base=base))
    reads[s] = lst
bams = []
for s in samples:
    b = Bam(os.path.join(tmp, s + ".bam"), len(REF), s)
    for r in reads[s]:
        b.add(r["name"], r["start"], r["seq"], r["quals"], mapq=r["mq"], rev=r["rev"])
    bams.append(b.write())

def truth(min_bq, min_mq, delta=30, max_bq=60):
    per = {}
    for s in samples:
        bases = []; QS = [0]*4; ADF = [0]*4; ADR = [0]*4; anno = [0.0]*16; ori = 0; mq0 = 0
        for r in reads[s]:
            if r["mq"] < min_mq: continue                     # mpileup -q, applied at read level
            ori += 1
            qp = r["qpos"]; q = r["quals"][qp]
            if qp > 0 and q > r["quals"][qp-1] + delta: q = r["quals"][qp-1] + delta
            if qp+1 < RL and q > r["quals"][qp+1] + delta: q = r["quals"][qp+1] + delta
            if q < min_bq: continue
            if q > max_bq: q = max_bq
            baseQ = q
            mapQ = r["mq"] if r["mq"] < 255 else 20
            if mapQ == 0: mq0 += 1
            mapQ = min(mapQ, 60)
            q = min(q, 99, mapQ, 63); q = max(q, 4)
            b = NT.index(r["base"])
            is_diff = 0 if r["base"] == ref_base else 1
            rev = 1 if r["rev"] else 0
            bases.append((q, rev, b))
            QS[b] += q
            (ADR if rev else ADF)[b] += 1
            anno[is_diff << 1 | rev] += 1
            md = min(qp, RL-1-qp, 25)
            anno[4 | is_diff << 1] += baseQ; anno[4 | is_diff << 1 | 1] += baseQ*baseQ
            anno[8 | is_diff << 1] += mapQ;  anno[8 | is_diff << 1 | 1] += mapQ*mapQ
            anno[12 | is_diff << 1] += md;   anno[12 | is_diff << 1 | 1] += md*md
        per[s] = dict(p=errmod_cal(bases), QS=QS, ADF=ADF, ADR=ADR, anno=anno, ori=ori, mq0=mq0)
    # combine: allele order = ref, then alleles by summed normalised QS (desc), then unseen <*>
    qsum = [0.0]*4
    for s in samples:
        tot = sum(per[s]["QS"])
        if tot:
            for j in range(4): qsum[j] += per[s]["QS"][j]/tot
    ref4 = NT.index(ref_base)
    order = [ref4] + [j for j in sorted(range(4), key=lambda j: -qsum[j]) if j != ref4 and qsum[j] > 0]
    seen = len(order)
    unseen = [j for j in range(4) if j not in order]
    if unseen: order.append(unseen[0])
    alleles = [NT[j] for j in order[:seen]] + (["<*>"] if unseen else [])
    na = len(order)
    gts = [(order[j], order[i]) for i in range(na) for j in range(i+1)]
    res = dict(alleles=alleles, qsum=[qsum[j] for j in order], per={}, anno=[sum(per[s]["anno"][k] for s in samples) for k in range(16)],
               DP=sum(per[s]["ori"] for s in samples), mq0=sum(per[s]["mq0"] for s in samples))
    for s in samples:
        p = per[s]["p"]
        vals = [p[a][b] for (a, b) in gts]
        mn = min(vals)
        PL = [min(int(v - mn + 0.499), 255) for v in vals]
        ADF = [per[s]["ADF"][j] if j < 4 else 0 for j in order]; ADR = [per[s]["ADR"][j] if j < 4 else 0 for j in order]
        a = per[s]["anno"]
        dp4 = [int(a[0]), int(a[1]), int(a[2]), int(a[3])]
        if dp4[0]+dp4[1] < 2 or dp4[2]+dp4[3] < 2 or dp4[0]+dp4[2] < 2 or dp4[1]+dp4[3] < 2: sp = 0
        else:
            two = fisher_exact([[dp4[0], dp4[1]], [dp4[2], dp4[3]]])[1]
            sp = min(int(-4.343*math.log(two) + 0.499), 255)
        res["per"][s] = dict(PL=PL, AD=[f+r for f, r in zip(ADF, ADR)], ADF=ADF, ADR=ADR, DP4=dp4, DP=sum(dp4), SP=sp, QS=[per[s]["QS"][j] if j < 4 else 0 for j in order])
    return res

def compare(label, extra, min_bq, min_mq):
    out, _ = run(BIN, ["mpileup", "-f", REF_PATH, "-B", "-a", "FORMAT/AD,FORMAT/ADF,FORMAT/ADR,FORMAT/DP,FORMAT/DP4,FORMAT/SP,FORMAT/QS,INFO/AD"] + extra + bams)
    rec = [r for r in vcf_records(out) if r["pos"] == SITE][0]
    t = truth(min_bq, min_mq)
    nbad = 0
    def chk(name, got, exp, tol=0):
        nonlocal nbad
        ok = (abs(float(got) - float(exp)) <= tol) if not isinstance(exp, list) else all(abs(float(g)-float(e)) <= tol for g, e in zip(str(got).split(","), exp)) and len(str(got).split(",")) == len(exp)
        if not ok: nbad += 1; print("  MISMATCH %s: got %s expected %s" % (name, got, exp))
    chk("ALT alleles", ",".join(rec["alt"]), None) if False else None
    if rec["alt"] != t["alleles"][1:]: nbad += 1; print("  MISMATCH alleles: got %s expected %s" % (rec["alt"], t["alleles"]))
    chk("INFO/DP", rec["info"]["DP"], t["DP"])
    chk("INFO/I16", rec["info"]["I16"], t["anno"], tol=0.5)
    chk("INFO/QS", rec["info"]["QS"], t["qsum"], tol=1e-4)
    chk("INFO/MQ0F", rec["info"]["MQ0F"], t["mq0"]/t["DP"], tol=1e-5)
    for s in samples:
        g = rec["samples"][s]; e = t["per"][s]
        for k in ("PL", "AD", "ADF", "ADR", "DP4", "QS"): chk("%s %s" % (s, k), g[k], e[k])
        chk("%s DP" % s, g["DP"], e["DP"]); chk("%s SP" % s, g["SP"], e["SP"], tol=1)
    # call -m: DP4 and MQ
    out2, _ = run(BIN, ["call", "-m", "-A"], stdin=out)
    rc = [r for r in vcf_records(out2) if r["pos"] == SITE][0]
    a = t["anno"]; dp4s = a[0]+a[1]+a[2]+a[3]
    chk("call DP4", rc["info"]["DP4"], [a[0], a[1], a[2], a[3]])
    chk("call MQ", rc["info"]["MQ"], (a[8]+a[10])/dp4s, tol=0.01)
    print("[%s] alleles %s; S1 PL=%s AD=%s SP=%s; S2 PL=%s; I16 ok; %d mismatches" % (label, ",".join([rec["ref"]]+rec["alt"]), rec["samples"]["S1"]["PL"], rec["samples"]["S1"]["AD"], rec["samples"]["S1"]["SP"], rec["samples"]["S2"]["PL"], nbad))
    return nbad

tot = 0
tot += compare("defaults (-Q1 -q0 --delta-BQ 30)", [], 1, 0)
tot += compare("-Q 13", ["-Q", "13"], 13, 0)
tot += compare("-Q 20 -q 30", ["-Q", "20", "-q", "30"], 20, 30)
tot += compare("-Q 30 -q 20", ["-Q", "30", "-q", "20"], 30, 20)
print("\nTOTAL mismatches: %d" % tot)
