"""Held-up check for bcftools call -m: QUAL, GT, GQ, AC, AN, -v and --ploidy 1 against an
independent Python port of the multiallelic caller (mcall.c: set_pdg, mcall_find_best_alleles,
mcall_call_genotypes, QUAL at mcall.c:1546/1631) fed with the PL and INFO/QS that
bcftools mpileup writes for synthetic multi-sample BAMs.

Usage: python heldup_call_m_port.py /path/to/bcftools
"""
import os, sys, math, random, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import bcftools_bin, version, run, make_ref, make_bam, site_reads, parse_vcf

BIN = bcftools_bin()
print("bcftools:", version(BIN))
D = tempfile.mkdtemp(prefix="cm_")
REF = os.path.join(D, "ref.fa")
refseq = make_ref(REF, 3000, seed=31)
rng = random.Random(9)
nfail = 0

def logsumexp2(a, b):
    if a == -math.inf: return b
    if b == -math.inf: return a
    return (math.log(1 + math.exp(b - a)) + a) if a > b else (math.log(1 + math.exp(a - b)) + b)

def gt_index(a, b):
    a, b = min(a, b), max(a, b)
    return b * (b + 1) // 2 + a

def port_call(rec, theta, ploidy):
    """returns dict(QUAL, GT list, GQ list, AC, AN, variant) or None (site skipped / ref-only)."""
    alleles = [rec["REF"]] + rec["ALT"].split(",")
    nals = len(alleles)
    unseen = alleles.index("<*>") if "<*>" in alleles else -1
    ngts = nals * (nals + 1) // 2
    qs = [float(x) for x in rec["INFO"]["QS"].split(",")]
    qs += [0.0] * (nals - len(qs))
    s = sum(qs); qs = [q / s for q in qs] if s else qs
    nsmpl = len(rec["samples"])
    pdg = []
    for smp in rec["samples"]:
        pl = smp["PL"].split(",")
        if pl[0] == ".":
            pdg.append([0.0] * ngts); continue
        p = [10 ** (-int(x) / 10) for x in pl]
        s = sum(p)
        if s == len(p):          # all PL == 0 (flat, e.g. zero coverage): treated as missing data (set_pdg, mcall.c:532-540)
            pdg.append([0.0] * ngts); continue
        pdg.append([x / s for x in p])
    # the prior is scaled by the Watterson factor aM = 1 + sum_{i=2}^{n-1} 1/i, n = total ploidy (mcall.c:400-418)
    n = sum(ploidy); aM = 1.0 + sum(1.0 / i for i in range(2, n))
    th = theta * aM
    if th >= 1: th = 0.99
    logtheta = math.log(th)
    # best allele combination
    max_lk, max_als, lk_sum, ref_lk = -math.inf, 0, -math.inf, -math.inf
    def upd(als, lk, do_sum):
        nonlocal max_lk, max_als, lk_sum
        if lk is not None:
            if max_lk < lk: max_lk, max_als = lk, als
            if do_sum: lk_sum = logsumexp2(lk, lk_sum)
    for ia in range(nals):
        lk, seen = 0.0, False
        for i in range(nsmpl):
            v = pdg[i][gt_index(ia, ia)]
            if v: lk += math.log(v); seen = True
        if ia == 0: ref_lk = lk if seen else 0.0
        else: lk += logtheta
        upd(1 << ia, lk if seen else None, ia > 0)
    for ia in range(nals):
        if qs[ia] == 0: continue
        for ib in range(ia):
            if qs[ib] == 0: continue
            fa = qs[ia] / (qs[ia] + qs[ib]); fb = qs[ib] / (qs[ia] + qs[ib])
            lk, seen = 0.0, False
            for i in range(nsmpl):
                if ploidy[i] == 2: v = fa*fa*pdg[i][gt_index(ia, ia)] + fb*fb*pdg[i][gt_index(ib, ib)] + 2*fa*fb*pdg[i][gt_index(ia, ib)]
                else: v = fa*pdg[i][gt_index(ia, ia)] + fb*pdg[i][gt_index(ib, ib)]
                if v: lk += math.log(v); seen = True
            if ia: lk += logtheta
            if ib: lk += logtheta
            upd((1 << ia) | (1 << ib), lk if seen else None, True)
    # three-allele combinations (same pattern)
    for ia in range(nals):
        if qs[ia] == 0: continue
        for ib in range(ia):
            if qs[ib] == 0: continue
            for ic in range(ib):
                if qs[ic] == 0: continue
                tot = qs[ia] + qs[ib] + qs[ic]; fa, fb, fc = qs[ia]/tot, qs[ib]/tot, qs[ic]/tot
                lk, seen = 0.0, False
                for i in range(nsmpl):
                    P = pdg[i]
                    if ploidy[i] == 2:
                        v = fa*fa*P[gt_index(ia,ia)] + fb*fb*P[gt_index(ib,ib)] + fc*fc*P[gt_index(ic,ic)] + \
                            2*fa*fb*P[gt_index(ia,ib)] + 2*fa*fc*P[gt_index(ia,ic)] + 2*fb*fc*P[gt_index(ib,ic)]
                    else: v = fa*P[gt_index(ia,ia)] + fb*P[gt_index(ib,ib)] + fc*P[gt_index(ic,ic)]
                    if v: lk += math.log(v); seen = True
                lk += logtheta * ((ia > 0) + (ib > 0) + (ic > 0))
                upd((1 << ia) | (1 << ib) | (1 << ic), lk if seen else None, True)
    qual = -4.343 * (ref_lk - logsumexp2(lk_sum, ref_lk)) if max_lk != -math.inf else None
    als = max_als | 1
    if unseen > 0: als &= ~(1 << unseen)
    variant = als != 1
    if not variant:
        return dict(variant=False, QUAL=qual, lk_sum=lk_sum, ref_lk=ref_lk)
    kept = [i for i in range(nals) if als & (1 << i)]
    amap = {a: k for k, a in enumerate(kept)}
    gts, gqs, ac = [], [], [0] * len(kept)
    for i in range(nsmpl):
        P = pdg[i]
        if not any(P):
            gts.append("./." if ploidy[i] == 2 else "."); gqs.append(0); continue
        best, bgt, gps = 0.0, (0, 0), {}
        for ia in kept:
            lk = P[gt_index(ia, ia)] * qs[ia] * (qs[ia] if ploidy[i] == 2 else 1)
            gps[(amap[ia], amap[ia])] = lk
            if best < lk: best, bgt = lk, (amap[ia], amap[ia])
        if ploidy[i] == 2:
            for ia in kept:
                for ib in kept:
                    if ib >= ia: continue
                    lk = 2 * P[gt_index(ia, ib)] * qs[ia] * qs[ib]
                    gps[(amap[ib], amap[ia])] = lk
                    if best < lk: best, bgt = lk, (amap[ib], amap[ia])
            gts.append("%d/%d" % bgt); ac[bgt[0]] += 1; ac[bgt[1]] += 1
        else:
            gts.append("%d" % bgt[0]); ac[bgt[0]] += 1
        ssum = sum(gps.values()); mx = max(gps.values())
        gq = -4.34294 * math.log(1 - mx / ssum) if mx < ssum else float("inf")
        gqs.append(int(min(gq, 127)))
    return dict(variant=True, QUAL=qual, GT=gts, GQ=gqs, AC=ac[1:], AN=sum(ac), alleles=[alleles[k] for k in kept])

def check(label, got, exp, tol=None):
    global nfail
    if tol is None: ok = got == exp
    else: ok = abs(got - exp) <= tol * max(1.0, abs(exp))
    if not ok: nfail += 1
    return "ok" if ok else "MISMATCH"

# ---- build 6 samples with a variety of genotypes and depths at 12 sites
sites = list(range(400, 2800, 200))
bams = []
truth_gt = {}
for s in range(6):
    reads = []
    for k, site in enumerate(sites):
        refb = refseq[site]; altb = "A" if refb != "A" else "C"; third = "G" if refb not in "G" and altb != "G" else "T"
        depth = [0, 1, 2, 4, 8, 15, 30][(s + k) % 7]
        kind = ["ref", "het", "hom", "ref", "het", "third-het"][(s * 3 + k) % 6]
        if depth == 0: continue
        if kind == "ref": nalt = 0
        elif kind == "hom": nalt = depth
        else: nalt = max(1, depth // 2)
        b_alt = third if kind == "third-het" else altb
        reads += site_reads(refseq, site, depth - nalt, refb, [60] * (depth - nalt), [30 + (i % 8) for i in range(depth - nalt)], prefix="s%dk%dr" % (s, k), seed=s * 100 + k)
        reads += site_reads(refseq, site, nalt, b_alt, [60] * nalt, [25 + (i % 12) for i in range(nalt)], prefix="s%dk%da" % (s, k), seed=s * 100 + k + 50)
    bams.append(make_bam(os.path.join(D, "s%d.bam" % s), 3000, reads, rg="S%d" % s))
mp = run(BIN, ["mpileup", "-f", REF, "-B", "-a", "FORMAT/AD", "-r", ",".join("ref:%d-%d" % (p + 1, p + 1) for p in sites)] + bams)

for label, cargs, theta, ploidy in (("call -m", ["-m"], 1.1e-3, [2] * 6), ("call -mv", ["-mv"], 1.1e-3, [2] * 6),
                                     ("call -m -P 0.1", ["-m", "-P", "0.1"], 0.1, [2] * 6), ("call -m -P 1e-6", ["-m", "-P", "1e-6"], 1e-6, [2] * 6),
                                     ("call -mv --ploidy 1", ["-mv", "--ploidy", "1"], 1.1e-3, [1] * 6)):
    out = run(BIN, ["call"] + cargs + ["-f", "GQ"], stdin=mp)
    got = {r["POS"]: r for r in parse_vcf(out)}
    inp = {r["POS"]: r for r in parse_vcf(mp)}
    print("\n%s: %d input sites, %d output records" % (label, len(inp), len(got)))
    nvar = 0
    for pos in sorted(inp):
        t = port_call(inp[pos], theta, ploidy)
        g = got.get(pos)
        if "-v" in cargs[0] or "-mv" in cargs:
            if not t["variant"]:
                print("   %5d port: ref-only  bcftools: %s" % (pos, "absent  ok" if g is None else "PRESENT (%s) MISMATCH" % g["ALT"])); nfail += g is not None; continue
            if g is None:
                # bcftools also drops variant sites where every called GT is hom-ref (mcall.c:1615)
                if all(x in ("0/0", "0", "./.", ".") for x in t["GT"]): print("   %5d port: variant alleles but all GT hom-ref -> dropped  bcftools: absent  ok"); continue
                print("   %5d port variant QUAL %.2f GT %s  bcftools: ABSENT MISMATCH" % (pos, t["QUAL"], t["GT"])); nfail += 1; continue
        if not t["variant"]:
            q = float(g["QUAL"]) if g["QUAL"] != "." else None
            tq = -4.343 * (t["lk_sum"] - logsumexp2(t["lk_sum"], t["ref_lk"])) if t["lk_sum"] != -math.inf else None
            st = check("q", q, tq, 1e-3) if (q is not None and tq is not None) else ("ok" if q == tq else "MISMATCH")
            print("   %5d ref-only: QUAL bcftools %s port %s %s  GT %s" % (pos, g["QUAL"], "%.3f" % tq if tq else tq, st, ",".join(x["GT"] for x in g["samples"])))
            continue
        nvar += 1
        gq = [int(x["GQ"]) for x in g["samples"]]; gt = [x["GT"] for x in g["samples"]]
        ac = [int(x) for x in g["INFO"]["AC"].split(",")]
        sq = check("QUAL", float(g["QUAL"]), t["QUAL"], 1e-3); sg = check("GT", gt, t["GT"]); sgq = check("GQ", gq, t["GQ"])
        if sg != "ok":
            for i in range(6):
                if gt[i] != t["GT"][i]: print("      sample %d: mpileup PL=%s AD=%s -> bcftools %s GQ %d, port %s GQ %d" % (i, inp[pos]["samples"][i]["PL"], inp[pos]["samples"][i].get("AD"), gt[i], gq[i], t["GT"][i], t["GQ"][i]))
        sac = check("AC", ac, t["AC"]); san = check("AN", int(g["INFO"]["AN"]), t["AN"]); sal = check("ALT", g["ALT"], ",".join(t["alleles"][1:]))
        print("   %5d ALT=%-4s QUAL %8.3f/%8.3f %s | GT %s/%s %s | GQ %s/%s %s | AC %s/%s %s AN %s/%s %s" % (
            pos, g["ALT"], float(g["QUAL"]), t["QUAL"], sq, ",".join(gt), ",".join(t["GT"]), sg, gq, t["GQ"], sgq, ac, t["AC"], sac, g["INFO"]["AN"], t["AN"], san) + ("" if sal == "ok" else "  ALT MISMATCH port %s" % t["alleles"]))
print("\nmismatches:", nfail)
