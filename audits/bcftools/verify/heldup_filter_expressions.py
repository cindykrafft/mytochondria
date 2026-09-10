#!/usr/bin/env python3
"""Held-up: bcftools filter/view -i/-e expression semantics against a Python evaluator
on a random VCF: numeric comparisons on QUAL/INFO/FORMAT, missing-value rules
(comparisons with '.' are false; TAG="." and TAG!="." as documented), `&` vs `&&` and
`|` vs `||` on per-sample expressions, GT string tests ("het","hom","alt","mis","RR"...),
MIN/MAX/AVG/MEDIAN/STDEV/SUM/COUNT and SMPL_* forms, binom() and fisher() vs scipy,
N_PASS/F_PASS, and the -i vs -e complement.

usage: python heldup_filter_expressions.py /path/to/bcftools
"""
import os, sys, random, tempfile, statistics, math
from scipy.stats import binomtest, fisher_exact
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import run, version, write_vcf, vcf_records

BIN = sys.argv[1]
print("binary:", version(BIN))
tmp = tempfile.mkdtemp(prefix="fl_")
rnd = random.Random(5)
NS = 4
samples = ["a", "b", "c", "d"]
hdr = ['##contig=<ID=1,length=1000000>',
       '##INFO=<ID=DP,Number=1,Type=Integer,Description="x">', '##INFO=<ID=MQ,Number=1,Type=Float,Description="x">',
       '##INFO=<ID=AF,Number=A,Type=Float,Description="x">', '##INFO=<ID=DP4,Number=4,Type=Integer,Description="x">',
       '##INFO=<ID=INDEL,Number=0,Type=Flag,Description="x">',
       '##FORMAT=<ID=GT,Number=1,Type=String,Description="x">', '##FORMAT=<ID=DP,Number=1,Type=Integer,Description="x">',
       '##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="x">', '##FORMAT=<ID=AD,Number=R,Type=Integer,Description="x">']
recs, sites = [], []
for i in range(300):
    qual = rnd.choice([".", 5, 19.9, 20, 20.1, 50, 99])
    dp = rnd.choice([".", 0, 5, 10, 20, 30])
    mq = rnd.choice([".", 10.5, 30, 59.9, 60])
    nal = rnd.choice([1, 1, 2])
    af = [round(rnd.random(), 3) for _ in range(nal)]
    dp4 = [rnd.randint(0, 20) for _ in range(4)]
    indel = rnd.random() < 0.2
    gts, sm = [], []
    for s in range(NS):
        g = rnd.choice(["0/0", "0/1", "1/1", "./.", "0|1", "1/2" if nal == 2 else "0/0", ".", "0", "1"])
        sdp = rnd.choice([".", 0, 3, 8, 15, 40]); gq = rnd.choice([".", 0, 10, 20, 30, 99])
        ad = [rnd.randint(0, 15) for _ in range(nal+1)]
        if rnd.random() < 0.1: ad = ["."]*(nal+1)
        gts.append("%s:%s:%s:%s" % (g, sdp, gq, ",".join(map(str, ad))))
        sm.append(dict(gt=g, dp=sdp, gq=gq, ad=ad))
    info = "DP4=%s" % ",".join(map(str, dp4))
    if dp != ".": info += ";DP=%d" % dp
    if mq != ".": info += ";MQ=%s" % mq
    info += ";AF=%s" % ",".join(map(str, af))
    if indel: info += ";INDEL"
    recs.append(("1", 1000+i, ".", "A", ",".join(["G", "T"][:nal]), qual, ".", info, "GT:DP:GQ:AD", gts))
    sites.append(dict(pos=1000+i, qual=qual, dp=dp, mq=mq, af=af, dp4=dp4, indel=indel, sm=sm, nal=nal))
vcf = write_vcf(os.path.join(tmp, "in.vcf"), hdr, samples, recs)

def num(v): return None if v == "." else float(v)
def gt_class(g):
    if g in (".", "./.", ".|."): return "mis"
    als = [int(x) for x in g.replace("|", "/").split("/") if x != "."]
    if len(als) == 1: return "hap"
    if als[0] == als[1]: return "RR" if als[0] == 0 else "AA"
    return "RA" if 0 in als else "Aa"
def dpvals(st): return [x for x in (num(s["dp"]) for s in st["sm"]) if x is not None]
def cmp(a, op, b):
    if a is None or b is None: return False
    return {">": a > b, "<": a < b, ">=": a >= b, "<=": a <= b, "=": a == b, "!=": a != b}[op]

def binom_ok(s):
    g = s["gt"].replace("|", "/")
    if len(g) != 3 or "." in g or s["ad"][0] == ".": return False
    a, b = (int(x) for x in g.split("/"))
    if a == b or s["ad"][a] + s["ad"][b] == 0: return False       # na==nb -> p=1; 0,0 -> missing
    return binomtest(s["ad"][a], s["ad"][a]+s["ad"][b], 0.5).pvalue < 0.05

def truth_site(st, expr):
    q, dp, mq = num(st["qual"]), num(st["dp"]), num(st["mq"])
    sm = st["sm"]
    dps = [num(s["dp"]) for s in sm]; gqs = [num(s["gq"]) for s in sm]
    E = {
     "QUAL>20": cmp(q, ">", 20), "QUAL>=20": cmp(q, ">=", 20), "QUAL<20": cmp(q, "<", 20), 'QUAL="."': q is None, 'QUAL!="."': q is not None,
     "INFO/DP>10": cmp(dp, ">", 10), "INFO/DP<10": cmp(dp, "<", 10), 'INFO/DP="."': dp is None, 'INFO/DP!="."': dp is not None,
     "MQ<30": cmp(mq, "<", 30), "MQ>=30": cmp(mq, ">=", 30),
     "QUAL>20 && INFO/DP>10": cmp(q, ">", 20) and cmp(dp, ">", 10), "QUAL>20 || INFO/DP>10": cmp(q, ">", 20) or cmp(dp, ">", 10),
     "INDEL=1": st["indel"], "INDEL=0": not st["indel"], "TYPE=\"snp\"": True, "N_ALT=2": st["nal"] == 2,
     "AF[0]>0.5": st["af"][0] > 0.5, "MAX(AF)>0.5": max(st["af"]) > 0.5, "MIN(AF)<0.1": min(st["af"]) < 0.1,
     "FMT/DP>10": any(cmp(x, ">", 10) for x in dps), "FMT/GQ>=20": any(cmp(x, ">=", 20) for x in gqs),
     "FMT/DP>10 & FMT/GQ>=20": any(cmp(x, ">", 10) and cmp(y, ">=", 20) for x, y in zip(dps, gqs)),
     "FMT/DP>10 && FMT/GQ>=20": any(cmp(x, ">", 10) for x in dps) and any(cmp(y, ">=", 20) for y in gqs),
     "FMT/DP>10 | FMT/GQ>=20": any(cmp(x, ">", 10) or cmp(y, ">=", 20) for x, y in zip(dps, gqs)),
     "FMT/DP>10 || FMT/GQ>=20": any(cmp(x, ">", 10) for x in dps) or any(cmp(y, ">=", 20) for y in gqs),
     "QUAL>20 & FMT/DP>10": cmp(q, ">", 20) and any(cmp(x, ">", 10) for x in dps),
     'GT="het"': any(gt_class(s["gt"]) in ("RA", "Aa") for s in sm), 'GT="hom"': any(gt_class(s["gt"]) in ("RR", "AA") for s in sm),   # haploid genotypes are GT="hap", not "hom"
     'GT="mis"': any(gt_class(s["gt"]) == "mis" for s in sm), 'GT="RR"': any(gt_class(s["gt"]) == "RR" for s in sm),
     'GT="AA"': any(gt_class(s["gt"]) == "AA" for s in sm), 'GT="alt"': any(gt_class(s["gt"]) in ("RA", "Aa", "AA") or s["gt"] == "1" for s in sm),
     'GT="het" & FMT/GQ>=20': any(gt_class(s["gt"]) in ("RA", "Aa") and cmp(num(s["gq"]), ">=", 20) for s in sm),
     "MAX(FMT/DP)>10": max(dpvals(st)) > 10 if dpvals(st) else False, "MIN(FMT/DP)<3": min(dpvals(st)) < 3 if dpvals(st) else False,
     "AVG(FMT/DP)>10": (sum(dpvals(st))/len(dpvals(st)) > 10) if dpvals(st) else False,
     "MEDIAN(FMT/DP)>=8": (statistics.median(dpvals(st)) >= 8) if dpvals(st) else False,
     "SUM(FMT/DP)>30": sum(dpvals(st)) > 30 if dpvals(st) else False,
     "STDEV(FMT/DP)>10": (statistics.pstdev(dpvals(st)) > 10) if dpvals(st) else False,
     "COUNT(GT=\"het\")>1": sum(gt_class(s["gt"]) in ("RA", "Aa") for s in sm) > 1,
     "N_PASS(GQ>=20)>=2": sum(cmp(num(s["gq"]), ">=", 20) for s in sm) >= 2,
     "F_PASS(FMT/DP>10)>0.5": sum(cmp(x, ">", 10) for x in dps)/NS > 0.5,
     "F_MISSING>0.25": sum(gt_class(s["gt"]) == "mis" for s in sm)/NS > 0.25,
     "SMPL_MAX(FMT/AD)>10": any(max(x for x in s["ad"] if x != ".") > 10 for s in sm if s["ad"][0] != "."),
     "SMPL_SUM(FMT/AD)>20": any(sum(x for x in s["ad"] if x != ".") > 20 for s in sm if s["ad"][0] != "."),
     "fisher(INFO/DP4)<0.05": fisher_exact([[st["dp4"][0], st["dp4"][1]], [st["dp4"][2], st["dp4"][3]]])[1] < 0.05,
     "binom(FMT/AD)<0.05": any(binom_ok(s) for s in sm),
    }
    return E[expr]

EXPRS = ["QUAL>20", "QUAL>=20", "QUAL<20", 'QUAL="."', 'QUAL!="."', "INFO/DP>10", "INFO/DP<10", 'INFO/DP="."', 'INFO/DP!="."', "MQ<30", "MQ>=30",
         "QUAL>20 && INFO/DP>10", "QUAL>20 || INFO/DP>10", "INDEL=1", "INDEL=0", "N_ALT=2", "AF[0]>0.5", "MAX(AF)>0.5", "MIN(AF)<0.1",
         "FMT/DP>10", "FMT/GQ>=20", "FMT/DP>10 & FMT/GQ>=20", "FMT/DP>10 && FMT/GQ>=20", "FMT/DP>10 | FMT/GQ>=20", "FMT/DP>10 || FMT/GQ>=20",
         "QUAL>20 & FMT/DP>10", 'GT="het"', 'GT="hom"', 'GT="mis"', 'GT="RR"', 'GT="AA"', 'GT="alt"', 'GT="het" & FMT/GQ>=20',
         "MAX(FMT/DP)>10", "MIN(FMT/DP)<3", "AVG(FMT/DP)>10", "MEDIAN(FMT/DP)>=8", "SUM(FMT/DP)>30", "STDEV(FMT/DP)>10",
         "COUNT(GT=\"het\")>1", "N_PASS(GQ>=20)>=2", "F_PASS(FMT/DP>10)>0.5", "F_MISSING>0.25", "SMPL_MAX(FMT/AD)>10", "SMPL_SUM(FMT/AD)>20",
         "fisher(INFO/DP4)<0.05", "binom(FMT/AD)<0.05"]
nbad = 0
for expr in EXPRS:
    out, _ = run(BIN, ["view", "-H", "-i", expr, vcf])
    got_i = {int(l.split("\t")[1]) for l in out.splitlines()}
    out, _ = run(BIN, ["view", "-H", "-e", expr, vcf])
    got_e = {int(l.split("\t")[1]) for l in out.splitlines()}
    exp = {st["pos"] for st in sites if truth_site(st, expr)}
    allpos = {st["pos"] for st in sites}
    ok = got_i == exp and got_e == allpos - exp
    if not ok:
        nbad += 1
        d1 = sorted(got_i ^ exp)[:5]
        print("  MISMATCH %-32s -i selected %d expected %d (e.g. %s); -e complement %s" % (expr, len(got_i), len(exp), d1, got_e == allpos - got_i))
    else:
        print("  ok  %-32s -i selects %3d of 300 sites, -e the complement" % (expr, len(got_i)))
print("\n%d expressions, %d mismatches" % (len(EXPRS), nbad))
