#!/usr/bin/env python3
"""Held-up: bcftools +fill-tags AN/AC/AF/MAF/NS/AC_Het/AC_Hom/AC_Hemi/F_MISSING and the
exact HWE / ExcHet p-values against an independent truth.

Truth for HWE: Levene/Haldane exact distribution of the heterozygote count given the
allele counts, in exact rational arithmetic (fractions), then Wigginton 2005's
p = sum of P(n_het') over n_het' with P <= P(observed); ExcHet = P(n_het' >= observed).
Genotypes are random per site so nothing is hand-tuned.

usage: python heldup_fill_tags_hwe.py /path/to/bcftools
"""
import os, sys, random, tempfile
from fractions import Fraction
from math import comb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import run, version, write_vcf, vcf_records

BIN = sys.argv[1]
print("binary:", version(BIN))
tmp = tempfile.mkdtemp(prefix="ft_")
rnd = random.Random(2024)
NS = 60
samples = ["s%02d" % i for i in range(NS)]

def hwe_exact(n_ref, n_alt, n_het):
    n = (n_ref + n_alt) // 2
    rare = min(n_ref, n_alt)
    # number of hets has the parity of rare; P(h) ∝ 2^h / ((rare-h)/2)! h! ((2n-rare-h)/2)!
    probs = {}
    for h in range(rare % 2, rare + 1, 2):
        hr = (rare - h) // 2; hc = n - h - hr
        if hc < 0: continue
        probs[h] = Fraction(2**h * comb(n, h) * comb(n - h, hr), 1)
    tot = sum(probs.values())
    probs = {h: p / tot for h, p in probs.items()}
    p_obs = probs[n_het]
    p_hwe = sum(p for p in probs.values() if p <= p_obs)
    p_exc = sum(p for h, p in probs.items() if h >= n_het)
    return float(p_hwe), float(p_exc)

hdr = ['##contig=<ID=1,length=100000>', '##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">']
recs, truth = [], []
for i in range(40):
    p = rnd.choice([0.02, 0.1, 0.3, 0.5, 0.8])
    miss = rnd.choice([0, 0, 0.1, 0.3])
    excess = rnd.choice([0, 0, 1])           # push heterozygosity up on some sites
    gts = []
    for s in range(NS):
        if rnd.random() < miss:
            gts.append("./."); continue
        if excess and rnd.random() < 0.5:
            gts.append("0/1"); continue
        a = int(rnd.random() < p); b = int(rnd.random() < p)
        gts.append("%d/%d" % (min(a, b), max(a, b)))
    if i == 39:  # one haploid/mixed site
        gts = [g if s % 5 else g[0] for s, g in enumerate(gts)]
    recs.append(("1", 1000 + i, ".", "A", "G", ".", ".", ".", "GT", gts))
    truth.append(gts)
vcf = write_vcf(os.path.join(tmp, "in.vcf"), hdr, samples, recs)
out, _ = run(BIN, ["+fill-tags", vcf, "--", "-t", "AN,AC,AF,MAF,NS,AC_Het,AC_Hom,AC_Hemi,F_MISSING,HWE,ExcHet"])
res = vcf_records(out)

nbad = 0; ncmp = 0
for r, gts in zip(res, truth):
    info = r["info"]
    dip = [g for g in gts if len(g) == 3 and "." not in g]
    hap = [g for g in gts if len(g) == 1 and g != "."]
    nmiss = sum(1 for g in gts if g in (".", "./."))
    n_het = sum(1 for g in dip if g == "0/1")
    n_homalt = sum(1 for g in dip if g == "1/1")
    n_homref = sum(1 for g in dip if g == "0/0")
    hemi_alt = sum(1 for g in hap if g == "1")
    ac = n_het + 2*n_homalt + hemi_alt
    an = 2*len(dip) + len(hap)
    exp = {"AN": an, "AC": ac, "NS": NS - nmiss, "AC_Het": n_het, "AC_Hom": 2*n_homalt, "AC_Hemi": hemi_alt}
    for k, v in exp.items():
        ncmp += 1
        if int(info[k]) != v:
            nbad += 1; print("MISMATCH %s pos %d: got %s expected %s" % (k, r["pos"], info[k], v))
    af = ac / an
    ncmp += 3
    if abs(float(info["AF"]) - af) > 1e-5: nbad += 1; print("MISMATCH AF pos %d: %s vs %.6f" % (r["pos"], info["AF"], af))
    if abs(float(info["MAF"]) - min(af, 1-af)) > 1e-5: nbad += 1; print("MISMATCH MAF pos %d: %s vs %.6f" % (r["pos"], info["MAF"], min(af, 1-af)))
    if abs(float(info["F_MISSING"]) - nmiss/NS) > 1e-5: nbad += 1; print("MISMATCH F_MISSING pos %d: %s vs %.6f" % (r["pos"], info["F_MISSING"], nmiss/NS))
    # HWE over the diploid genotypes only (haploids excluded by design, see fill-tags.c calc_hwe caller)
    n_ref = 2*n_homref + n_het; n_alt = 2*n_homalt + n_het
    if n_ref > 0 and n_alt > 0:
        p_hwe, p_exc = hwe_exact(n_ref, n_alt, n_het)
    else:
        p_hwe, p_exc = 1.0, 1.0
    ncmp += 2
    g_hwe, g_exc = float(info["HWE"]), float(info["ExcHet"])
    ok = abs(g_hwe - p_hwe) <= 2e-6 + 1e-5*p_hwe and abs(g_exc - p_exc) <= 2e-6 + 1e-5*p_exc
    if not ok:
        nbad += 2; print("MISMATCH HWE/ExcHet pos %d: got %g/%g exact %g/%g" % (r["pos"], g_hwe, g_exc, p_hwe, p_exc))
    if r["pos"] in (1000, 1005, 1012, 1039):
        print("pos %d: hets=%d homalt=%d homref=%d hap=%d miss=%d  HWE got %s exact %.6g  ExcHet got %s exact %.6g"
              % (r["pos"], n_het, n_homalt, n_homref, len(hap), nmiss, info["HWE"], p_hwe, info["ExcHet"], p_exc))
print("\n%d values compared over %d sites, %d mismatches (float32 tolerance 1e-5 relative)" % (ncmp, len(res), nbad))

# Multiallelic site: the documented limitation (fill-tags.c: "NB this neglects multiallelic genotypes")
gts = ["0/1"]*10 + ["0/2"]*10 + ["1/2"]*10 + ["0/0"]*20 + ["1/1"]*5 + ["2/2"]*5
vcf2 = write_vcf(os.path.join(tmp, "ma.vcf"), hdr, samples, [("1", 5000, ".", "A", "G,T", ".", ".", ".", "GT", gts)])
out, _ = run(BIN, ["+fill-tags", vcf2, "--", "-t", "AN,AC,AF,MAF,HWE,ExcHet"])
r = vcf_records(out)[0]
print("\nmultiallelic (10 0/1, 10 0/2, 10 1/2, 20 0/0, 5 1/1, 5 2/2): AN=%s AC=%s AF=%s MAF=%s HWE=%s ExcHet=%s" % (r["info"]["AN"], r["info"]["AC"], r["info"]["AF"], r["info"]["MAF"], r["info"]["HWE"], r["info"]["ExcHet"]))
print("  AF exact: 1=%.4f 2=%.4f; MAF printed is the second-largest allele frequency (allele 1 or 2), not min(AF)" % (30/120, 30/120))
