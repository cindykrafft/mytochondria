#!/usr/bin/env python3
"""Held-up (and note N1): bcftools stats SN counts, TSTV, per-sample PSC counts
(nRefHom/nNonRefHom/nHets/nTransitions/nTransversions/nIndels/average depth/
nSingletons/nHapRef/nHapAlt/nMissing), the DP distribution, the SiS/AF binning
(default and --af-bins) and the HWE section, against Python truth on a random
VCF with known genotypes, depths and AF.

usage: python heldup_stats.py /path/to/bcftools
"""
import os, sys, random, tempfile, math
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import run, version, write_vcf

BIN = sys.argv[1]
print("binary:", version(BIN))
tmp = tempfile.mkdtemp(prefix="st_")
rnd = random.Random(77)
NS = 8
samples = ["s%d" % i for i in range(NS)]
TS = {("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")}
hdr = ['##contig=<ID=1,length=1000000>', '##INFO=<ID=DP,Number=1,Type=Integer,Description="x">',
       '##INFO=<ID=AF,Number=A,Type=Float,Description="x">',
       '##FORMAT=<ID=GT,Number=1,Type=String,Description="x">', '##FORMAT=<ID=DP,Number=1,Type=Integer,Description="x">']
recs = []; sites = []
pos = 100
for i in range(400):
    pos += rnd.randint(1, 50)
    kind = rnd.choice(["snp", "snp", "snp", "indel", "msnp", "ref"])
    ref = rnd.choice("ACGT")
    if kind == "snp": alts = [rnd.choice([b for b in "ACGT" if b != ref])]
    elif kind == "msnp": alts = rnd.sample([b for b in "ACGT" if b != ref], 2)
    elif kind == "indel": alts = [ref + "".join(rnd.choice("ACGT") for _ in range(rnd.randint(1, 3)))] if rnd.random() < 0.5 else None
    else: alts = ["."]
    if kind == "indel" and alts is None:
        ref = ref + "".join(rnd.choice("ACGT") for _ in range(rnd.randint(1, 3))); alts = [ref[0]]
    nal = len(alts) if alts != ["."] else 0
    p = rnd.choice([0.05, 0.2, 0.5])
    gts, dps = [], []
    for s in range(NS):
        r = rnd.random()
        if r < 0.08: g = "./."
        elif r < 0.12: g = str(int(rnd.random() < p) if nal else 0)      # haploid
        else:
            a = int(rnd.random() < p) if nal else 0; b = int(rnd.random() < p) if nal else 0
            if nal == 2 and rnd.random() < 0.3: a, b = (rnd.choice([0, 1, 2]), 2)
            g = "%d/%d" % (min(a, b), max(a, b))
        dp = rnd.choice([0, 0, 3, 7, 12, 25, 40, 600])
        gts.append("%s:%d" % (g, dp)); dps.append(dp)
    idp = sum(dps)
    recs.append(("1", pos, ".", ref, ",".join(alts), rnd.choice([10.5, 30, 99]), ".", "DP=%d;AF=%s" % (idp, ",".join("%.3f" % p for _ in range(max(nal, 1))) if nal else "DP=%d" % idp), "GT:DP", gts))
    sites.append(dict(pos=pos, ref=ref, alts=alts, gts=[g.split(":")[0] for g in gts], dps=dps, idp=idp, af=p))
vcf = write_vcf(os.path.join(tmp, "in.vcf"), hdr, samples, recs)

def truth():
    T = dict(records=len(sites), snps=0, indels=0, mnps=0, others=0, noalts=0, mals=0, snp_mals=0, ts=0, tv=0, ts1=0, tv1=0)
    psc = {s: Counter() for s in samples}; dpsum = {s: 0 for s in samples}; dpn = {s: 0 for s in samples}
    dpdist_gt = Counter(); dpdist_site = Counter(); sis = Counter()
    for st in sites:
        alts = st["alts"]
        def vtype(a):
            if a == ".": return "ref"
            if len(a) == len(st["ref"]) == 1: return "snp"
            return "indel"
        types = {vtype(a) for a in alts}
        if types == {"ref"}: T["noalts"] += 1
        if "snp" in types: T["snps"] += 1
        if "indel" in types: T["indels"] += 1
        if len(alts) > 1: T["mals"] += 1; T["snp_mals"] += types == {"snp"}
        acs = Counter()
        for s, g in zip(samples, st["gts"]):
            for a in g.replace("|", "/").split("/"):
                if a != ".": acs[int(a)] += 1
        an = sum(acs.values())
        for i, a in enumerate(alts):
            if vtype(a) != "snp": continue
            is_ts = (st["ref"], a) in TS
            T["ts" if is_ts else "tv"] += 1
            if i == 0: T["ts1" if is_ts else "tv1"] += 1
            if acs[i+1] == 1: sis["snps"] += 1; sis["ts" if is_ts else "tv"] += 1
        for i, a in enumerate(alts):
            if vtype(a) == "indel" and acs[i+1] == 1: sis["indels"] += 1
        dpdist_site[st["idp"]] += 1
        nonref = []
        for s, g, dp in zip(samples, st["gts"], st["dps"]):
            if dp > 0: dpdist_gt[dp] += 1; dpsum[s] += dp; dpn[s] += 1
            if g == "./.": psc[s]["missing"] += 1; continue
            als = [int(x) for x in g.split("/")]
            if len(als) == 1:
                psc[s]["hapAlt" if als[0] else "hapRef"] += 1; continue
            if any(als): nonref.append(s)
            ial = sorted(set(a for a in als if a))         # non-ref alleles present
            snp_or_ref = any(vtype(alts[a-1]) == "snp" for a in ial) or (not ial)
            if snp_or_ref:
                if als[0] == als[1] == 0: psc[s]["homRR"] += 1
                elif als[0] == als[1]: psc[s]["homAA"] += 1
                else: psc[s]["hets"] += 1
                for a in ial:
                    if vtype(alts[a-1]) == "snp":
                        psc[s]["ts" if (st["ref"], alts[a-1]) in TS else "tv"] += 1
            if any(vtype(alts[a-1]) == "indel" for a in ial): psc[s]["indels"] += 1
        if len(nonref) == 1: psc[nonref[0]]["sngl"] += 1
    return T, psc, dpsum, dpn, dpdist_gt, dpdist_site, sis

T, psc, dpsum, dpn, dpdist_gt, dpdist_site, sis = truth()
out, _ = run(BIN, ["stats", "-s", "-", vcf])
lines = [l.split("\t") for l in out.splitlines() if l and not l.startswith("#")]
SN = {l[2]: l[3] for l in lines if l[0] == "SN"}
nbad = 0
def chk(name, got, exp, tol=0):
    global nbad
    if abs(float(got) - float(exp)) > tol: nbad += 1; print("  MISMATCH %s: got %s expected %s" % (name, got, exp))
for key, k in [("number of records:", "records"), ("number of SNPs:", "snps"), ("number of indels:", "indels"), ("number of no-ALTs:", "noalts"),
               ("number of multiallelic sites:", "mals"), ("number of multiallelic SNP sites:", "snp_mals"), ("number of MNPs:", "mnps"), ("number of others:", "others")]:
    chk(key, SN[key], T[k])
tstv = [l for l in lines if l[0] == "TSTV"][0]
chk("TSTV ts", tstv[2], T["ts"]); chk("TSTV tv", tstv[3], T["tv"]); chk("TSTV ts/tv", tstv[4], T["ts"]/T["tv"], 0.006)
chk("TSTV ts(1st ALT)", tstv[5], T["ts1"]); chk("TSTV tv(1st ALT)", tstv[6], T["tv1"])
print("SN/TSTV: records=%s SNPs=%s indels=%s mals=%s ts/tv=%s (truth %.2f)" % (SN["number of records:"], SN["number of SNPs:"], SN["number of indels:"], SN["number of multiallelic sites:"], tstv[4], T["ts"]/T["tv"]))
s_ = [l for l in lines if l[0] == "SiS"][0]
chk("SiS SNPs", s_[3], sis["snps"]); chk("SiS ts", s_[4], sis["ts"]); chk("SiS tv", s_[5], sis["tv"]); chk("SiS indels", s_[6], sis["indels"])
for l in lines:
    if l[0] != "PSC": continue
    s = l[2]; p = psc[s]
    for col, k in [(3, "homRR"), (4, "homAA"), (5, "hets"), (6, "ts"), (7, "tv"), (8, "indels"), (10, "sngl"), (11, "hapRef"), (12, "hapAlt"), (13, "missing")]:
        chk("PSC %s %s" % (s, k), l[col], p[k])
    avg = dpsum[s]/dpn[s]
    chk("PSC %s average depth (over DP>0 genotypes)" % s, l[9], avg, 0.051)
    if s == "s0":
        allavg = dpsum[s]/len(sites)
        print("PSC s0: nRefHom=%s nNonRefHom=%s nHets=%s nTs=%s nTv=%s nIndels=%s avgDP=%s nSingletons=%s nHapRef=%s nHapAlt=%s nMissing=%s" % tuple(l[3:14]))
        print("  N1: average depth %s equals the mean over genotypes with DP>0 (%.2f); the mean over all %d genotypes including DP=0 is %.2f" % (l[9], avg, len(sites), allavg))
dpl = {l[2]: l for l in lines if l[0] == "DP"}
def binned(c):
    out = Counter()
    for dp, n in c.items(): out[str(dp) if dp <= 500 else ">500"] += n
    return out
for key, n in binned(dpdist_gt).items(): chk("DP bin %s genotypes" % key, dpl[key][3], n)
for key, n in binned(dpdist_site).items(): chk("DP bin %s sites" % key, dpl[key][5], n)
print("DP distribution: %d genotype bins and %d site bins checked; genotypes with DP=0 (%d of them) appear in no bin" % (len(dpdist_gt), len(dpdist_site), sum(1 for st in sites for d in st["dps"] if d == 0)))
# AF binning with --af-bins and --af-tag: each SNP allele lands in [bin_lo, bin_hi)
out2, _ = run(BIN, ["stats", "--af-bins", "0.1,0.3,0.6", "--af-tag", "AF", vcf])
afl = [l for l in out2.splitlines() if l.startswith("AF\t")]
got = Counter(); exp = Counter()
bins = [0.0, 0.1, 0.3, 0.6, 1.0]
for st in sites:
    for a in st["alts"]:
        if a != "." and len(a) == len(st["ref"]) == 1:
            b = max(i for i in range(4) if st["af"] >= bins[i])
            exp[round((bins[b]+bins[b+1])/2, 3)] += 1     # bcftools prints the bin centre
for l in afl:
    f = l.split("\t"); got[float(f[2])] += int(f[3])
for b in exp:
    chk("--af-bins bin centre %.3f SNP count" % b, got.get(b, 0), exp.get(b, 0))
print("--af-bins 0.1,0.3,0.6 with --af-tag AF: SNP allele counts per bin got %s expected %s" % (dict(sorted(got.items())), dict(sorted(exp.items()))))
print("\nmismatches: %d" % nbad)
