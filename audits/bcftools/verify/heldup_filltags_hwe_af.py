"""Held-up checks for bcftools +fill-tags: AN, AC, AF, MAF, NS, AC_Het, AC_Hom, AC_Hemi,
F_MISSING, HWE and ExcHet, against exact truths computed in Python.

HWE truth: the exact conditional distribution of the heterozygote count given the
allele counts (Wigginton, Cutler & Abecasis 2005, PMID 15789306), evaluated with
exact rational arithmetic from the closed form
    P(h | N, nA) = 2^h N! / (nAA! h! nBB!) * nA! nB! / (2N)!,  nAA = (nA-h)/2,
not the recurrence bcftools uses. p_HWE = sum of P(h') over h' with P(h') <= P(h_obs);
ExcHet = P(h' >= h_obs). Also the multiallelic case that the source marks as neglected.

Usage: python heldup_filltags_hwe_af.py /path/to/bcftools
"""
import os, sys, random, tempfile
from fractions import Fraction
from math import comb, factorial
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import bcftools_bin, version, run, parse_vcf, write_vcf

BIN = bcftools_bin()
print("bcftools:", version(BIN))
D = tempfile.mkdtemp(prefix="ft_")
nfail = 0

def hwe_exact(n_aa, n_ab, n_bb):
    N = n_aa + n_ab + n_bb; nA = 2*n_aa + n_ab; nB = 2*N - nA
    nrare = min(nA, nB)
    probs = {}
    for h in range(nrare % 2, nrare + 1, 2):
        naa = (nA - h) // 2; nbb = (nB - h) // 2
        if naa < 0 or nbb < 0: continue
        probs[h] = Fraction(2**h * factorial(N), factorial(naa) * factorial(h) * factorial(nbb)) * \
                   Fraction(factorial(nA) * factorial(nB), factorial(2*N))
    assert sum(probs.values()) == 1
    p_obs = probs[n_ab]
    p_hwe = sum(p for p in probs.values() if p <= p_obs)
    exc = sum(p for h, p in probs.items() if h >= n_ab)
    return float(min(p_hwe, 1)), float(exc)

def check(label, got, exp, tol=0.0):
    global nfail
    ok = (abs(got - exp) <= tol * max(1.0, abs(exp))) if isinstance(exp, float) else got == exp
    if not ok: nfail += 1
    print("   %-40s bcftools %-14s truth %-14s %s" % (label, got, exp, "ok" if ok else "MISMATCH"))

# ---- biallelic sites with chosen genotype counts (N samples = 2000, mixed missing and haploid rows)
rng = random.Random(7)
cases = [(10, 5, 1), (0, 4, 0), (100, 0, 100), (50, 100, 50), (999, 2, 0), (1, 1, 1), (30, 29, 0), (0, 1, 0),
         (600, 800, 600), (1990, 10, 0), (0, 0, 2000), (2000, 0, 0), (3, 3, 3), (1200, 2, 798)]
for _ in range(10):
    n = 2000; a = rng.randrange(n); b = rng.randrange(n - a); cases.append((a, b, n - a - b))
N = 2000
samples = ["s%04d" % i for i in range(N)]
records = []
truths = []
for k, (naa, nab, nbb) in enumerate(cases):
    nmiss = N - naa - nab - nbb
    gts = ["0/0"] * naa + ["0/1"] * nab + ["1/1"] * nbb + ["./."] * nmiss
    rng.shuffle(gts)
    records.append(("ref", 100 + k, ".", "A", "G", ".", ".", ".", "GT", gts))
    an = 2 * (naa + nab + nbb); ac = nab + 2 * nbb
    af = ac / an if an else None
    t = dict(AN=an, AC=ac, NS=naa + nab + nbb, AC_Het=nab, AC_Hom=2 * nbb, F_MISSING=nmiss / N,
             AF=af, MAF=min(af, 1 - af) if af is not None else None)
    if naa + nab + nbb and ac and an - ac:
        t["HWE"], t["ExcHet"] = hwe_exact(naa, nab, nbb)
    else:
        t["HWE"], t["ExcHet"] = 1.0, 1.0
    truths.append(t)
# a site with haploid, missing-half and phased genotypes
gts = ["0"] * 500 + ["1"] * 300 + ["0|1"] * 400 + ["./1"] * 100 + ["1/1"] * 200 + ["./."] * 500
records.append(("ref", 999, ".", "A", "G", ".", ".", ".", "GT", gts))
# AN counts every called allele: haploid 800 + phased het 800 + half-missing 100 + hom 400 = 2100.
# Documented conventions: a half-missing "./1" counts as hemizygous unless --drop-missing is given
# (fill-tags usage, -d), and F_MISSING is F_PASS(GT="mis") where GT="mis" matches "./1" as well
# (manual, FILTERING EXPRESSIONS), so AC_Hemi = 300 + 100 and F_MISSING = (500 + 100) / 2000.
truths.append(dict(AN=2100, AC=300 + 400 + 100 + 400, NS=1500, AC_Het=400, AC_Hom=400, F_MISSING=600 / 2000,
                   AF=1200 / 2100, MAF=min(1200 / 2100, 900 / 2100), AC_Hemi=400))
# multiallelic site: 0/0 x100, 0/1 x40, 0/2 x30, 1/2 x20, 1/1 x10, 2/2 x5 (N=205 called, 1795 missing)
gts = ["0/0"] * 100 + ["0/1"] * 40 + ["0/2"] * 30 + ["1/2"] * 20 + ["1/1"] * 10 + ["2/2"] * 5 + ["./."] * 1795
records.append(("ref", 1500, ".", "A", "G,T", ".", ".", ".", "GT", gts))
vcf = write_vcf(os.path.join(D, "in.vcf"), ['##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">'], samples, records)
out = run(BIN, ["+fill-tags", vcf, "--", "-t", "AN,AC,AF,MAF,NS,AC_Het,AC_Hom,AC_Hemi,F_MISSING,HWE,ExcHet"])
recs = parse_vcf(out)
print("\nbiallelic sites (2000 samples), exact HWE / ExcHet and the count tags")
for rec, t, c in zip(recs, truths, cases + [None]):
    I = rec["INFO"]
    lab = "AA/AB/BB=%s" % (c,) if c else "haploid+phased+half-missing site"
    print(" %s" % lab)
    for tag in ("AN", "AC", "NS", "AC_Het", "AC_Hom"):
        check(tag, int(I[tag]), t[tag])
    if "AC_Hemi" in t: check("AC_Hemi", int(I["AC_Hemi"]), t["AC_Hemi"])
    check("F_MISSING", float(I["F_MISSING"]), float(t["F_MISSING"]), 1e-6)
    if t["AF"] is None:
        check("AF (missing)", I["AF"], ".")
    else:
        check("AF", float(I["AF"]), float(t["AF"]), 1e-6); check("MAF", float(I["MAF"]), float(t["MAF"]), 1e-6)
    if "HWE" in t:
        check("HWE (p, Wigginton 2005)", float(I["HWE"]), t["HWE"], 2e-6)
        check("ExcHet (P(het >= obs))", float(I["ExcHet"]), t["ExcHet"], 2e-6)

print("\nmultiallelic site: 0/0 x100, 0/1 x40, 0/2 x30, 1/2 x20, 1/1 x10, 2/2 x5")
I = recs[-1]["INFO"]
print("   bcftools AN=%s AC=%s AF=%s AC_Het=%s AC_Hom=%s HWE=%s ExcHet=%s" % (I["AN"], I["AC"], I["AF"], I["AC_Het"], I["AC_Hom"], I["HWE"], I["ExcHet"]))
check("AN", int(I["AN"]), 410); check("AC", I["AC"], "%d,%d" % (40 + 20 + 20, 30 + 20 + 10))
# HWE for allele 1 vs everything else (allele 2 pooled with REF): AA=100+30+5=135, AB=40+20=60, BB=10
h1 = hwe_exact(135, 60, 10); h2 = hwe_exact(100 + 40 + 10, 30 + 20, 5)
print("   truth pooling the other allele with REF: HWE=%.6g,%.6g ExcHet=%.6g,%.6g" % (h1[0], h2[0], h1[1], h2[1]))
# what fill-tags.c:952-958 computes: nref = nhom[0] + sum_j nhet[j] - nhet[ialt]
nhet = [40 + 30, 40 + 20, 30 + 20]; nhom0 = 200
for j, (nalt, nh) in enumerate(((60 + 20, 60), (50 + 10, 50)), start=1):
    nref = nhom0 + sum(nhet) - nhet[j]
    true_nref = (2 * 135 + 60) if j == 1 else (2 * 150 + 50)   # 2*AA + AB with the other ALT pooled into REF
    print("   fill-tags.c counts for ALT%d: nref=%d (pooled truth 2*AA+AB=%d) nalt=%d nhet=%d" % (j, nref, true_nref, nalt, nh))
print("   (the source comment at fill-tags.c:953 says multiallelic genotypes are neglected; see the review)")
print("\nmismatches (biallelic and count tags):", nfail)
