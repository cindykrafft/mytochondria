"""Held-up checks for bcftools view/filter -i expression semantics on a 3-sample VCF:
missing values, & vs &&, | vs ||, MIN/MAX/AVG/MEDIAN/SUM over FORMAT vectors, per-sample
sMAX/sSUM, subscripts, GT tests, N_PASS/F_PASS, on-the-fly AC/AF/MAF/F_MISSING, TYPE.
Expected site sets are computed in Python from the manual's definitions (doc/bcftools.txt,
FILTERING EXPRESSIONS) and compared with the POS list that `bcftools view -i` returns.

Usage: python heldup_filter_expressions.py /path/to/bcftools
"""
import os, sys, tempfile, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import bcftools_bin, version, run, write_vcf, parse_vcf

BIN = bcftools_bin()
print("bcftools:", version(BIN))
D = tempfile.mkdtemp(prefix="fl_")
nfail = 0
#  pos, ref, alt, qual, filter, INFO(DP,AF), samples GT:DP:GQ:AD
sites = [
    (100, "A", "G",   "50", "PASS", (30, "0.25"),  ["0/1:10:99:5,5", "0/0:20:60:20,0", "0/0:5:10:5,0"]),
    (200, "A", "C",   "10", "q10",  (8, "0.5"),    ["0/1:.:.:.", "1/1:4:20:0,4", "./.:.:.:."]),
    (300, "C", "T",   ".",  "PASS", (None, "0.1"), ["0/0:12:50:12,0", "0/1:3:8:2,1", "0/1:30:99:15,15"]),
    (400, "AC", "A",  "99", "PASS", (100, "0.9"),  ["1/1:40:99:0,40", "1/1:35:99:1,34", "0/1:25:70:12,13"]),
    (500, "G", "T,C", "70", "PASS", (60, "0.2,0.3"), ["1/2:20:40:0,10,10", "0/1:20:50:10,10,0", "0/2:.:.:."]),
    (600, "T", ".",   "20", "PASS", (15, None),    ["0/0:15:99:15", "./.:.:.:.", "0/0:16:99:16"]),
    (700, "G", "A",   "35", "PASS", (10, "1"),     ["1/1:1:3:0,1", "1/1:2:6:0,2", "1/1:3:9:0,3"]),
]
recs = []
for pos, ref, alt, q, flt, (dp, af), smp in sites:
    info = ";".join(x for x in (("DP=%d" % dp) if dp is not None else "", ("AF=%s" % af) if af else "") if x) or "."
    recs.append(("ref", pos, ".", ref, alt, q, flt, info, "GT:DP:GQ:AD", smp))
hdr = ['##INFO=<ID=DP,Number=1,Type=Integer,Description="x">', '##INFO=<ID=AF,Number=A,Type=Float,Description="x">',
       '##FILTER=<ID=q10,Description="x">',
       '##FORMAT=<ID=GT,Number=1,Type=String,Description="x">', '##FORMAT=<ID=DP,Number=1,Type=Integer,Description="x">',
       '##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="x">', '##FORMAT=<ID=AD,Number=R,Type=Integer,Description="x">']
vcf = write_vcf(os.path.join(D, "in.vcf"), hdr, ["s1", "s2", "s3"], recs)

# Python model of each site
def fmt(site, tag, i):
    v = site[6][i].split(":")[["GT", "DP", "GQ", "AD"].index(tag)]
    if tag == "AD": return [None if x == "." else int(x) for x in v.split(",")]
    if tag == "GT": return v
    return None if v == "." else int(v)
def gt_alleles(g): return [None if a == "." else int(a) for a in g.replace("|", "/").split("/")]
def is_het(g): a = gt_alleles(g); return None not in a and len(set(a)) > 1
def is_mis(g): return None in gt_alleles(g)
def ac_an(site):
    an = 0; ac = {}
    for i in range(3):
        for a in gt_alleles(fmt(site, "GT", i)):
            if a is not None: an += 1; ac[a] = ac.get(a, 0) + 1
    return ac, an
def vals(site, tag): return [fmt(site, tag, i) for i in range(3)]
def nonmiss(xs): return [x for x in xs if x is not None]

E = {}   # expression -> predicate(site)
E['QUAL>30']                          = lambda s: s[3] != "." and float(s[3]) > 30
E['QUAL="."']                         = lambda s: s[3] == "."
E['INFO/DP>10']                       = lambda s: s[5][0] is not None and s[5][0] > 10
E['INFO/DP="."']                      = lambda s: s[5][0] is None
E['INFO/DP<=10 || INFO/DP="."']       = lambda s: s[5][0] is None or s[5][0] <= 10
E['AF[0]<0.3']                        = lambda s: s[5][1] is not None and float(s[5][1].split(",")[0]) < 0.3
E['AF[*]>0.25']                       = lambda s: s[5][1] is not None and any(float(x) > 0.25 for x in s[5][1].split(","))
E['FILTER="PASS"']                    = lambda s: s[4] == "PASS"
E['FILTER!="PASS"']                   = lambda s: s[4] != "PASS"
E['TYPE="snp"']                       = lambda s: s[2] != "." and all(len(a) == 1 for a in s[2].split(",")) and len(s[1]) == 1
E['TYPE="indel"']                     = lambda s: s[2] != "." and all(len(a) != len(s[1]) for a in s[2].split(","))
E['FMT/DP>10']                        = lambda s: any(x is not None and x > 10 for x in vals(s, "DP"))
E['FMT/DP[0]>10']                     = lambda s: fmt(s, "DP", 0) is not None and fmt(s, "DP", 0) > 10
E['FMT/DP[1-2]>10']                   = lambda s: any(x is not None and x > 10 for x in vals(s, "DP")[1:])
E['FMT/DP="."']                       = lambda s: any(x is None for x in vals(s, "DP"))
E['MIN(FMT/DP)>10']                   = lambda s: bool(nonmiss(vals(s, "DP"))) and min(nonmiss(vals(s, "DP"))) > 10
E['MAX(FMT/DP)>=30']                  = lambda s: bool(nonmiss(vals(s, "DP"))) and max(nonmiss(vals(s, "DP"))) >= 30
E['AVG(FMT/DP)>15']                   = lambda s: bool(nonmiss(vals(s, "DP"))) and statistics.mean(nonmiss(vals(s, "DP"))) > 15
E['MEDIAN(FMT/DP)>=12']               = lambda s: bool(nonmiss(vals(s, "DP"))) and statistics.median(nonmiss(vals(s, "DP"))) >= 12
E['SUM(FMT/DP)>40']                   = lambda s: sum(nonmiss(vals(s, "DP"))) > 40
E['SUM(FMT/AD[*:1])>=10']             = lambda s: sum(nonmiss([ad[1] if len(ad) > 1 else None for ad in vals(s, "AD")])) >= 10
E['GT="het"']                         = lambda s: any(is_het(g) for g in vals(s, "GT"))
E['GT="mis"']                         = lambda s: any(is_mis(g) for g in vals(s, "GT"))
E['GT="AA"']                          = lambda s: any((lambda a: None not in a and all(x > 0 for x in a) and len(set(a)) == 1)(gt_alleles(g)) for g in vals(s, "GT"))
E['GT="Aa"']                          = lambda s: any((lambda a: None not in a and all(x > 0 for x in a) and len(set(a)) > 1)(gt_alleles(g)) for g in vals(s, "GT"))
E['GT="het" & FMT/DP>10']             = lambda s: any(is_het(fmt(s, "GT", i)) and fmt(s, "DP", i) is not None and fmt(s, "DP", i) > 10 for i in range(3))
E['GT="het" && FMT/DP>10']            = lambda s: any(is_het(g) for g in vals(s, "GT")) and any(x is not None and x > 10 for x in vals(s, "DP"))
E['GT="hom" & FMT/GQ<20']             = lambda s: any((lambda a: None not in a and len(set(a)) == 1)(gt_alleles(fmt(s, "GT", i))) and fmt(s, "GQ", i) is not None and fmt(s, "GQ", i) < 20 for i in range(3))
E['FMT/DP>10 | FMT/GQ>90']            = lambda s: any((fmt(s, "DP", i) or 0) > 10 or (fmt(s, "GQ", i) or 0) > 90 for i in range(3))
E['sMAX(FMT/AD)>=20']                 = lambda s: any(max(nonmiss(ad), default=-1) >= 20 for ad in vals(s, "AD"))
E['sSUM(FMT/AD)>30']                  = lambda s: any(sum(nonmiss(ad)) > 30 for ad in vals(s, "AD") if nonmiss(ad))
E['N_PASS(GT="het")>=2']              = lambda s: sum(is_het(g) for g in vals(s, "GT")) >= 2
E['F_PASS(FMT/DP>=10)>0.5']           = lambda s: sum((x or 0) >= 10 for x in vals(s, "DP")) / 3 > 0.5
E['F_MISSING>0.3']                    = lambda s: sum(is_mis(g) for g in vals(s, "GT")) / 3 > 0.3
E['AC>2']                             = lambda s: any(v > 2 for a, v in ac_an(s)[0].items() if a > 0)
E['AC[0]=2']                          = lambda s: ac_an(s)[0].get(1, 0) == 2
E['AN=6']                             = lambda s: ac_an(s)[1] == 6
E['MAF<0.2']                          = lambda s: (lambda ac, an: an > 0 and (s[2] == "." or min(ac.get(1, 0), an - ac.get(1, 0)) / an < 0.2))(*ac_an(s))   # no ALT: MAF = 0
E['N_ALT=2']                          = lambda s: s[2] != "." and len(s[2].split(",")) == 2
E['ALT="."']                          = lambda s: s[2] == "."
E['(QUAL>30 & INFO/DP>20) || FILTER="q10"'] = lambda s: (s[3] != "." and float(s[3]) > 30 and s[5][0] is not None and s[5][0] > 20) or s[4] == "q10"
E['QUAL>30 && FMT/GQ>90']             = lambda s: s[3] != "." and float(s[3]) > 30 and any((x or 0) > 90 for x in vals(s, "GQ"))
E['QUAL>30 & FMT/GQ>90']              = E['QUAL>30 && FMT/GQ>90']

def check(expr, got, exp):
    global nfail
    ok = got == exp
    if not ok: nfail += 1
    print("   %-42s bcftools %-32s truth %-32s %s" % (expr, got, exp, "ok" if ok else "MISMATCH"))

print()
for expr, pred in E.items():
    out = run(BIN, ["view", "-H", "-i", expr, vcf])
    got = [int(l.split("\t")[1]) for l in out.splitlines()]
    exp = [s[0] for s in sites if pred(s)]
    check(expr, got, exp)
# view -e is the complement of -i
out_i = run(BIN, ["view", "-H", "-i", 'GT="het" & FMT/DP>10', vcf]); out_e = run(BIN, ["view", "-H", "-e", 'GT="het" & FMT/DP>10', vcf])
check("-e is the complement of -i", sorted(int(l.split("\t")[1]) for l in (out_i + out_e).splitlines()), [s[0] for s in sites])
# filter -s soft-filters the same set as view -i excludes
out_f = run(BIN, ["filter", "-s", "LOW", "-e", "QUAL<30 || INFO/DP<10", vcf])
got = [r["POS"] for r in parse_vcf(out_f) if r["FILTER"] == "LOW"]
exp = [s[0] for s in sites if (s[3] != "." and float(s[3]) < 30) or (s[5][0] is not None and s[5][0] < 10)]
check("filter -s LOW -e 'QUAL<30 || INFO/DP<10'", got, exp)
print("\nmismatches:", nfail)
