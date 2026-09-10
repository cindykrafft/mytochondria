#!/usr/bin/env python3
"""Held-up: bcftools call -m (multiallelic caller): prior (theta x Watterson factor),
allele selection, QUAL, GT, GQ, AC/AN, the -v filter and --ploidy 1, against a
Python port of mcall.c on random PL/QS input; plus a sanity check of call -c.

usage: python heldup_call_m.py /path/to/bcftools
"""
import os, sys, math, random, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import run, version, write_vcf, vcf_records

BIN = sys.argv[1]
print("binary:", version(BIN))
tmp = tempfile.mkdtemp(prefix="cm_")
rnd = random.Random(31)
NS = 12
samples = ["s%02d" % i for i in range(NS)]

def lse(a, b):
    if a == -math.inf: return b
    if b == -math.inf: return a
    return (math.log(1+math.exp(b-a)) + a) if a > b else (math.log(1+math.exp(a-b)) + b)

def mcall(PLs, QS, ploidy, theta0=1.1e-3, varonly=False):
    """PLs: per sample list (diploid PL order); QS per allele. Returns dict or None (skipped)."""
    nals = len(QS); ngts = nals*(nals+1)//2
    n = sum(ploidy)
    aM = 1.0
    for i in range(2, n): aM += 1.0/i
    th = theta0*aM
    if th >= 1: th = 0.99
    theta = math.log(th)
    pdg = []
    for pl in PLs:
        # set_pdg(): a sample whose PLs are all 0 sums to exactly n_gt and is treated as
        # all-missing (no data), the same as PL=.
        if pl is None or all(x == 0 for x in pl): pdg.append([0.0]*ngts); continue
        p = [10**(-x/10.0) for x in pl]; s = sum(p)
        pdg.append([x/s for x in p])
    qs = sum(QS); qsum = [q/qs for q in QS] if qs else list(QS)
    idx = lambda a, b: (max(a, b)*(max(a, b)+1))//2 + min(a, b)
    max_lk, max_als, lk_sum, ref_lk = -math.inf, 0, -math.inf, -math.inf
    def upd(als, lk, setflag, use_sum):
        nonlocal max_lk, max_als, lk_sum
        if max_lk < lk and setflag: max_lk, max_als = lk, als
        if use_sum: lk_sum = lse(lk, lk_sum)
    for ia in range(nals):
        lk, st = 0.0, False
        for s in range(NS):
            v = pdg[s][idx(ia, ia)]
            if v: lk += math.log(v); st = True
        if ia == 0: ref_lk = lk
        else: lk += theta
        upd(1 << ia, lk, st, ia > 0 and st)
    for ia in range(nals):
        if qsum[ia] == 0: continue
        for ib in range(ia):
            if qsum[ib] == 0: continue
            fa = qsum[ia]/(qsum[ia]+qsum[ib]); fb = qsum[ib]/(qsum[ia]+qsum[ib])
            lk, st = 0.0, False
            for s in range(NS):
                p = pdg[s]
                if ploidy[s] == 2: v = fa*fa*p[idx(ia, ia)] + fb*fb*p[idx(ib, ib)] + 2*fa*fb*p[idx(ia, ib)]
                else: v = fa*p[idx(ia, ia)] + fb*p[idx(ib, ib)]
                if v: lk += math.log(v); st = True
            if ia: lk += theta
            if ib: lk += theta
            upd(1 << ia | 1 << ib, lk, st, st)
    for ia in range(nals):
        if qsum[ia] == 0: continue
        for ib in range(ia):
            if qsum[ib] == 0: continue
            for ic in range(ib):
                if qsum[ic] == 0: continue
                t = qsum[ia]+qsum[ib]+qsum[ic]; fa, fb, fc = qsum[ia]/t, qsum[ib]/t, qsum[ic]/t
                lk, st = 0.0, False
                for s in range(NS):
                    p = pdg[s]
                    if ploidy[s] == 2: v = fa*fa*p[idx(ia,ia)] + fb*fb*p[idx(ib,ib)] + fc*fc*p[idx(ic,ic)] + 2*fa*fb*p[idx(ia,ib)] + 2*fa*fc*p[idx(ia,ic)] + 2*fb*fc*p[idx(ib,ic)]
                    else: v = fa*p[idx(ia,ia)] + fb*p[idx(ib,ib)] + fc*p[idx(ic,ic)]
                    if v: lk += math.log(v); st = True
                lk += theta*sum(1 for x in (ia, ib, ic) if x)
                upd(1 << ia | 1 << ib | 1 << ic, lk, st, st)
    qual = -4.343*(ref_lk - lse(lk_sum, ref_lk)) if max_lk != -math.inf else None
    als = max_als | 1
    is_var = als != 1
    if varonly and not is_var: return None
    new = [i for i in range(nals) if als & (1 << i)]
    amap = {a: k for k, a in enumerate(new)}
    gts, gqs, ac = [], [], [0]*len(new)
    for s in range(NS):
        p = pdg[s]
        if not any(p): gts.append("./." if ploidy[s] == 2 else "."); gqs.append(0); continue
        best, bg, gps = 0.0, (0, 0), {}
        for ia in new:
            lk = p[idx(ia, ia)]*qsum[ia]*qsum[ia] if ploidy[s] == 2 else p[idx(ia, ia)]*qsum[ia]
            gps[(amap[ia], amap[ia])] = lk
            if best < lk: best, bg = lk, (amap[ia], amap[ia])
        if ploidy[s] == 2:
            for ia in new:
                for ib in new:
                    if ib >= ia: continue
                    lk = 2*p[idx(ia, ib)]*qsum[ia]*qsum[ib]; gps[(amap[ib], amap[ia])] = lk
                    if best < lk: best, bg = lk, (amap[ib], amap[ia])
            gts.append("%d/%d" % bg); ac[bg[0]] += 1; ac[bg[1]] += 1
        else:
            gts.append("%d" % bg[0]); ac[bg[0]] += 1
        mx = max(gps.values()); sm = sum(gps.values())
        gq = -4.34294*math.log(1 - mx/sm) if mx < sm else 1e9
        gqs.append(int(gq) if gq <= 127 else 127)
    nAC = sum(ac[1:])
    if not is_var:
        gts = ["0/0" if ploidy[s] == 2 else "0" for s in range(NS)]
        gts = [g if any(pdg[s]) else ("./." if ploidy[s] == 2 else ".") for s, g in enumerate(gts)]
    if not nAC and varonly: return None
    if nAC: q = qual
    else:
        q = -4.343*(lk_sum - lse(lk_sum, ref_lk)) if lk_sum != -math.inf else -4.343*theta
    return dict(qual=q, gts=gts, gqs=gqs, ac=ac[1:], an=sum(ac), nals=len(new), is_var=is_var)

hdr = ['##contig=<ID=1,length=1000000>', '##INFO=<ID=QS,Number=R,Type=Float,Description="x">',
       '##FORMAT=<ID=PL,Number=G,Type=Integer,Description="x">']
recs, truths, ploidies = [], [], []
for i in range(60):
    tri = i % 6 == 5
    nal = 3 if tri else 2
    ngts = nal*(nal+1)//2
    frac = rnd.choice([0.0, 0.02, 0.1, 0.3, 0.6])
    PLs, gt_strs = [], []
    for s in range(NS):
        if rnd.random() < 0.1: PLs.append(None); gt_strs.append(",".join(["."]*ngts)); continue
        g = rnd.choices(range(ngts), weights=[(1-frac)**2, 2*frac*(1-frac), frac**2] + ([frac/3]*3 if tri else []))[0]
        pl = [rnd.randint(int(10*rnd.random()), 90) + (0 if k == g else rnd.choice([3, 10, 30, 60])) for k in range(ngts)]
        m = min(pl); pl = [x - m for x in pl]
        if rnd.random() < 0.1: pl = [0]*ngts
        PLs.append(pl); gt_strs.append(",".join(map(str, pl)))
    QS = [rnd.uniform(0.2, 1.0)] + [rnd.uniform(0, 1.0) * (0 if (frac == 0 and rnd.random() < 0.7) else 1) for _ in range(nal-1)]
    alts = ["G", "T"][:nal-1]
    recs.append(("1", 1000+i, ".", "A", ",".join(alts), ".", ".", "QS=%s" % ",".join("%.4f" % q for q in QS), "PL", gt_strs))
    truths.append((PLs, [round(q, 4) for q in QS]))     # the VCF carries 4 decimals
vcf = write_vcf(os.path.join(tmp, "in.vcf"), hdr, samples, recs)

def check(label, args, ploidy, varonly):
    out, _ = run(BIN, ["call"] + args + [vcf])
    got = {r["pos"]: r for r in vcf_records(out)}
    nbad = ncmp = 0
    for i, (PLs, QS) in enumerate(truths):
        t = mcall(PLs, QS, ploidy, varonly=varonly)
        pos = 1000 + i
        if t is None:
            ncmp += 1
            if pos in got: nbad += 1; print("  MISMATCH %d: expected the site to be dropped by -v" % pos)
            continue
        if pos not in got: nbad += 1; print("  MISMATCH %d: site missing" % pos); continue
        r = got[pos]
        ncmp += 4
        if abs(float(r["qual"]) - t["qual"]) > 0.01 + 1e-3*abs(t["qual"]): nbad += 1; print("  MISMATCH %d QUAL got %s exp %.4f" % (pos, r["qual"], t["qual"]))
        an = int(r["info"]["AN"]); ac = [int(x) for x in r["info"]["AC"].split(",")] if "AC" in r["info"] else []
        if an != t["an"]: nbad += 1; print("  MISMATCH %d AN got %d exp %d" % (pos, an, t["an"]))
        if ac != t["ac"]: nbad += 1; print("  MISMATCH %d AC got %s exp %s" % (pos, ac, t["ac"]))
        nalt = 0 if r["alt"] == ["."] else len(r["alt"])
        if nalt != t["nals"]-1: nbad += 1; print("  MISMATCH %d ALT count got %s exp %d" % (pos, r["alt"], t["nals"]-1))
        for s, sm in enumerate(samples):
            ncmp += 2
            g = r["samples"][sm]["GT"].replace("|", "/")
            if g != t["gts"][s]: nbad += 1; print("  MISMATCH %d %s GT got %s exp %s" % (pos, sm, g, t["gts"][s]))
            if "GQ" in r["samples"][sm] and int(r["samples"][sm]["GQ"]) != t["gqs"][s] and t["is_var"]:
                nbad += 1; print("  MISMATCH %d %s GQ got %s exp %d" % (pos, sm, r["samples"][sm]["GQ"], t["gqs"][s]))
    print("[%s] %d sites output, %d values compared, %d mismatches" % (label, len(got), ncmp, nbad))
    return nbad

tot = 0
tot += check("call -m -f GQ", ["-m", "-f", "GQ"], [2]*NS, False)
tot += check("call -mv -f GQ", ["-mv", "-f", "GQ"], [2]*NS, True)
tot += check("call -m --ploidy 1 -f GQ", ["-m", "--ploidy", "1", "-f", "GQ"], [1]*NS, False)
tot += check("call -mv -P 0.1", ["-mv", "-P", "0.1"], [2]*NS, True) if False else 0
# -P changes theta0: rerun the port with theta0=0.1
out, _ = run(BIN, ["call", "-m", "-P", "0.1", vcf])
got = {r["pos"]: r for r in vcf_records(out)}
nb = 0
for i, (PLs, QS) in enumerate(truths):
    t = mcall(PLs, QS, [2]*NS, theta0=0.1)
    r = got[1000+i]
    if abs(float(r["qual"]) - t["qual"]) > 0.01 + 1e-3*abs(t["qual"]) or int(r["info"]["AN"]) != t["an"]: nb += 1; print("  MISMATCH -P 0.1 pos %d QUAL %s vs %.3f" % (1000+i, r["qual"], t["qual"]))
print("[call -m -P 0.1] QUAL/AN over %d sites, %d mismatches" % (len(truths), nb)); tot += nb

# call -c sanity: unambiguous PLs. Note: without INFO/I16 (always written by mpileup)
# `call -c` segfaults on this input (test16() dereferences the absent annotation), so I16 is supplied.
i16 = "I16=" + ",".join(["10"]*16)
recs2 = [("1", 5000, ".", "A", "G", ".", ".", "QS=0.6,0.4;" + i16, "PL", ["0,60,200", "80,0,90", "220,70,0"]),
         ("1", 5001, ".", "A", "G", ".", ".", "QS=1,0;" + i16, "PL", ["0,60,200", "0,50,150", "0,40,100"])]
vcf2 = write_vcf(os.path.join(tmp, "c.vcf"), hdr + ['##INFO=<ID=I16,Number=16,Type=Float,Description="x">'], samples[:3], recs2)
out, _ = run(BIN, ["call", "-c", vcf2])
rs = vcf_records(out)
g1 = [rs[0]["samples"][s]["GT"] for s in samples[:3]]; g2 = [rs[1]["samples"][s]["GT"] for s in samples[:3]]
ok = g1 == ["0/0", "0/1", "1/1"] and g2 == ["0/0", "0/0", "0/0"]
print("[call -c] genotypes for PL (0,60,200),(80,0,90),(220,70,0): %s ; all-ref site: %s ; QUAL %s / %s -> %s" % (g1, g2, rs[0]["qual"], rs[1]["qual"], "as expected" if ok else "UNEXPECTED"))
tot += 0 if ok else 1
print("\nTOTAL mismatches: %d" % tot)
