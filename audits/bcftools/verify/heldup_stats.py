"""Held-up checks for bcftools stats on a hand-built 4-sample VCF: SN counts, TSTV,
SiS (singletons), AF bins (default and --af-bins), QUAL bins, DP distribution and
the per-sample PSC counts (nRefHom, nNonRefHom, nHets, nTs, nTv, nIndels, average
depth, nSingletons, nHapRef, nHapAlt, nMissing). Truths derived in Python from the
genotype table with the definitions in vcfstats.c cited inline.

Usage: python heldup_stats.py /path/to/bcftools
"""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import bcftools_bin, version, run, write_vcf

BIN = bcftools_bin()
print("bcftools:", version(BIN))
D = tempfile.mkdtemp(prefix="st_")
nfail = 0
S = ["A", "B", "C", "D"]
TS = {("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")}
#      pos   ref    alt      qual   GTs                          DPs (None = missing)
sites = [
    (100, "A", "G",     "50",   ["0/1", "0/0", "0/0", "0/0"], [10, 20, 30, 40]),
    (200, "A", "C",     "30.5", ["1/1", "0/0", "0/0", "0/0"], [5, 5, 5, 5]),
    (300, "C", "T",     "99",   ["0/1", "0/1", "0/1", "0/1"], [8, 8, 8, 8]),
    (400, "A", "G,T",   "20",   ["1/2", "0/1", "0/2", "./."], [12, 12, 12, 12]),
    (500, "ACG", "A",   "40",   ["0/1", "1/1", "0/0", "0/0"], [7, 7, 7, 7]),
    (600, "A", "AT",    "10",   ["0/0", "0/0", "0/0", "0/1"], [9, 9, 9, 9]),
    (700, "AT", "GC",   "60",   ["0/1", "0/0", "0/0", "0/0"], [11, 11, 11, 11]),
    (800, "A", ".",     ".",    ["0/0", "0/0", "0/0", "0/0"], [3, 3, 3, 3]),
    (900, "G", "A",     "12.3", ["./.", "./.", "0/1", "0/0"], [None, 0, 6, 6]),
    (1000, "G", "T",    "70",   ["0", "1", "1", "0"],         [4, 4, 4, 4]),
    (1100, "T", "C",    "80",   ["0/1", "0/1", "1/1", "0/1"], [None, 0, 15, 15]),
    (1200, "T", "G",    "90",   ["1/1", "1/1", "1/1", "1/1"], [2, 2, 2, 2]),
    (1300, "C", "A",    "45",   ["0/1", "0/1", "0/1", "0/0"], [1, 1, 1, 1]),
    (1400, "C", "G",    "55",   ["0/1", "1/1", "1/1", "1/1"], [1, 1, 1, 1]),
    (1500, "A", "T",    "65",   ["0/1", "0/1", "1/1", "1/1"], [1, 1, 1, 1]),
]
records = []
for pos, ref, alt, qual, gts, dps in sites:
    info = "DP=%d" % sum(d for d in dps if d)
    smp = ["%s:%s" % (g, "." if d is None else d) for g, d in zip(gts, dps)]
    records.append(("ref", pos, ".", ref, alt, qual, "PASS", info, "GT:DP", smp))
hdr = ['##INFO=<ID=DP,Number=1,Type=Integer,Description="depth">', '##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">',
       '##FORMAT=<ID=DP,Number=1,Type=Integer,Description="depth">']
vcf = write_vcf(os.path.join(D, "in.vcf"), hdr, S, records)

def vtype(ref, alt):
    if alt == ".": return "ref"
    if len(ref) == len(alt) == 1: return "snp"
    if len(ref) == len(alt): return "mnp"
    if ref[0] == alt[0] and (len(ref) == 1 or len(alt) == 1): return "indel"
    return "other"

# ---- truths
sn = dict(records=len(sites), noalts=0, snps=0, mnps=0, indels=0, others=0, mals=0, snp_mals=0)
ts = tv = ts1 = tv1 = 0
sis = dict(snps=0, ts=0, tv=0, indels=0)
afrows = {}          # true AF -> [snps, ts, tv, indels]
psc = {s: dict(RefHom=0, NonRefHom=0, Hets=0, Ts=0, Tv=0, Indels=0, dpsum=0, ndp=0, Singletons=0, HapRef=0, HapAlt=0, Missing=0) for s in S}
dp_gt, dp_sites = {}, {}
for pos, ref, alt, qual, gts, dps in sites:
    alts = alt.split(",")
    types = [vtype(ref, a) for a in alts]
    if types == ["ref"]: sn["noalts"] += 1
    if "snp" in types: sn["snps"] += 1
    if "indel" in types: sn["indels"] += 1
    if "mnp" in types: sn["mnps"] += 1
    if len(alts) > 1: sn["mals"] += 1; sn["snp_mals"] += all(t == "snp" for t in types)
    # allele counts
    an = 0; ac = [0] * (len(alts) + 1)
    for g in gts:
        for a in g.replace("|", "/").split("/"):
            if a != ".": an += 1; ac[int(a)] += 1
    for i, (a, t) in enumerate(zip(alts, types), start=1):
        key = "singleton" if ac[i] == 1 else ac[i] / an
        row = afrows.setdefault(key, [0, 0, 0, 0])
        if t == "snp":
            is_ts = (ref, a) in TS
            ts += is_ts; tv += not is_ts
            if i == 1: ts1 += is_ts; tv1 += not is_ts
            row[0] += 1; row[1] += is_ts; row[2] += not is_ts
            if ac[i] == 1: sis["snps"] += 1; sis["ts"] += is_ts; sis["tv"] += not is_ts
        elif t == "indel":
            row[3] += 1
            if ac[i] == 1: sis["indels"] += 1
    dp_sites[sum(d for d in dps if d)] = dp_sites.get(sum(d for d in dps if d), 0) + 1
    nonref = []
    for s, g, d in zip(S, gts, dps):
        P = psc[s]
        if d: P["dpsum"] += d; P["ndp"] += 1; dp_gt[d] = dp_gt.get(d, 0) + 1
        als = g.replace("|", "/").split("/")
        if all(a == "." for a in als): P["Missing"] += 1; continue      # vcfstats.c:1003
        ial = [int(a) for a in als if a != "."]
        if len(als) == 1:                                               # haploid: :1012-1021, returns before ts/tv
            if ial[0] == 0: P["HapRef"] += 1
            else: P["HapAlt"] += 1
            if ial[0] != 0: nonref.append(s)
            continue
        if any(ial): nonref.append(s)                                   # :1023
        atypes = {vtype(ref, alts[a - 1]) if a else "ref" for a in ial}
        if "snp" in atypes or atypes == {"ref"}:                        # :1034
            if ial[0] != ial[1]: P["Hets"] += 1
            elif ial[0] == 0: P["RefHom"] += 1
            else: P["NonRefHom"] += 1
            for a in set(ial):
                if a and vtype(ref, alts[a - 1]) == "snp":
                    if (ref, alts[a - 1]) in TS: P["Ts"] += 1
                    else: P["Tv"] += 1
        if "indel" in atypes and any(ial): P["Indels"] += 1
    if len(nonref) == 1: psc[nonref[0]]["Singletons"] += 1            # :1159

def check(label, got, exp):
    global nfail
    ok = got == exp
    if not ok: nfail += 1
    print("   %-44s bcftools %-26s truth %-26s %s" % (label, got, exp, "ok" if ok else "MISMATCH"))

out = run(BIN, ["stats", "-s", "-", vcf])
lines = [l.split("\t") for l in out.splitlines() if l and not l.startswith("#")]
SN = {l[2].rstrip(":"): int(l[3]) for l in lines if l[0] == "SN"}
print("\nSN")
for k, key in (("number of records", "records"), ("number of no-ALTs", "noalts"), ("number of SNPs", "snps"), ("number of MNPs", "mnps"),
               ("number of indels", "indels"), ("number of others", "others"), ("number of multiallelic sites", "mals"), ("number of multiallelic SNP sites", "snp_mals")):
    check(k, SN[k], sn[key])
print("\nTSTV (all ALT alleles; then 1st ALT only)")
t = [l for l in lines if l[0] == "TSTV"][0]
check("ts, tv, ts/tv", (int(t[2]), int(t[3]), t[4]), (ts, tv, "%.2f" % (ts / tv)))
check("ts, tv, ts/tv (1st ALT)", (int(t[5]), int(t[6]), t[7]), (ts1, tv1, "%.2f" % (ts1 / tv1)))
print("\nSiS (AC=1)")
t = [l for l in lines if l[0] == "SiS"][0]
check("SNPs, ts, tv, indels", (int(t[3]), int(t[4]), int(t[5]), int(t[6])), (sis["snps"], sis["ts"], sis["tv"], sis["indels"]))
print("\nAF rows: bcftools label vs the true AF of the alleles in it (default binning: label = int(AF*99)/100, vcfstats.c:665/696/1486)")
af = [(float(l[2]), int(l[3]), int(l[4]), int(l[5]), int(l[6])) for l in lines if l[0] == "AF"]
exp = {}
for key, row in afrows.items():
    lab = 0.0 if key == "singleton" else int(key * 99) / 100.0
    e = exp.setdefault(lab, [0, 0, 0, 0])
    for i in range(4): e[i] += row[i]
for lab, a, b, c, d in af:
    truth_keys = sorted((k for k in afrows if (k == "singleton" and lab == 0.0) or (k != "singleton" and int(k * 99) / 100.0 == lab)), key=str)
    check("AF label %.2f  (true AF %s)" % (lab, ",".join("%.4g" % k if k != "singleton" else k for k in truth_keys)), [a, b, c, d], exp.get(lab))
print("   AF labels: 0.5 -> 0.49, 0.25 -> 0.24, 1.0 -> 0.99: the label is the bin's lower edge on a 99-step grid printed on a 100-step grid")
out2 = run(BIN, ["stats", "-s", "-", "--af-bins", "0,0.25,0.5,0.75,1", vcf])
print("   with --af-bins 0,0.25,0.5,0.75,1 (labels are bin midpoints):")
for l in out2.splitlines():
    if l.startswith("AF\t"): print("      " + l)
print("\nQUAL rows (bin = 0.1 * int(QUAL*10)): SNPs, ts, tv, indels")
for l in lines:
    if l[0] == "QUAL": print("   " + "\t".join(l))
print("\nDP distribution: genotypes (FORMAT/DP > 0) and sites (INFO/DP)")
for l in lines:
    if l[0] == "DP":
        b = int(l[2]); check("DP bin %d" % b, (int(l[3]), int(l[5])), (dp_gt.get(b, 0), dp_sites.get(b, 0)))
print("\nPSC per sample")
for l in lines:
    if l[0] == "PSC":
        s = l[2]; P = psc[s]
        got = [int(x) for x in l[3:9]] + [l[9]] + [int(x) for x in l[10:14]]
        exp = [P["RefHom"], P["NonRefHom"], P["Hets"], P["Ts"], P["Tv"], P["Indels"], "%.1f" % (P["dpsum"] / P["ndp"]), P["Singletons"], P["HapRef"], P["HapAlt"], P["Missing"]]
        check("%s RefHom,NonRefHom,Hets,Ts,Tv,Indels,avgDP,Sngl,HapR,HapA,Miss" % s, got, exp)
print("   (haploid genotypes are not counted in nTs/nTv, and a sample's hom-alt or MNP genotype counts as a singleton when it is the only non-ref genotype: vcfstats.c:1012-1023,1159)")
print("\nmismatches:", nfail)
