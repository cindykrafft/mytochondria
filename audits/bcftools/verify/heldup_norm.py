"""Held-up checks for bcftools norm: left-alignment and parsimony against a Python
left-aligner, and the AC/AF/AN/DP/GT/PL/AD arithmetic of `-m -` (split) and `-m +`
(join) against the VCF Number=A/R/G definitions.

Usage: python heldup_norm.py /path/to/bcftools
"""
import os, sys, tempfile, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import bcftools_bin, version, run, make_ref, write_vcf, parse_vcf

BIN = bcftools_bin()
print("bcftools:", version(BIN))
D = tempfile.mkdtemp(prefix="nm_")
REF = os.path.join(D, "ref.fa")
rng = random.Random(3)
seq = list("".join(rng.choice("ACGT") for _ in range(3000)))
seq[1000:1012] = list("CAGCAGCAGCAG"); seq[999] = "T"; seq[1012] = "T"          # CAG x4 at 1000-1011 (0-based), flanked by T
seq[1500:1506] = list("AAAAAA"); seq[1499] = "C"; seq[1506] = "C"               # A x6 at 1500-1505
seq[2000:2010] = list("ATATATATAT"); seq[1999] = "C"; seq[2010] = "C"           # AT x5 at 2000-2009
refseq = "".join(seq)
with open(REF, "w") as fh:
    fh.write(">ref\n" + "\n".join(refseq[i:i+60] for i in range(0, 3000, 60)) + "\n")
import pysam; pysam.faidx(REF)
nfail = 0

def left_align(pos, ref, alts):
    """pos 1-based. Standard left-alignment then trimming of the common prefix (vt-style)."""
    als = [ref] + list(alts)
    while True:
        if all(len(a) > 0 for a in als) and len({a[-1] for a in als}) == 1 and (all(len(a) > 1 for a in als) or pos > 1):
            als = [a[:-1] for a in als]
            if any(len(a) == 0 for a in als):
                pos -= 1; base = refseq[pos - 1]; als = [base + a for a in als]
        else:
            break
    while all(len(a) > 1 for a in als) and len({a[0] for a in als}) == 1:
        als = [a[1:] for a in als]; pos += 1
    return pos, als[0], als[1:]

def check(label, got, exp):
    global nfail
    ok = got == exp
    if not ok: nfail += 1
    print("   %-58s bcftools %-28s truth %-28s %s" % (label, got, exp, "ok" if ok else "MISMATCH"))

print("\nA. left-alignment and parsimony (positions 1-based)")
cases0 = [  # (0-based pos, REF length, ALT builder) so that REF always matches the reference
    (1006, 4, lambda R: R[0]),                       # CAGC>C: CAG deletion inside the CAGx4 run
    (1011, 1, lambda R: R + "CAG"),                  # G>GCAG: CAG insertion at the run's right end
    (1503, 1, lambda R: R + "A"),                    # A>AA inside the A6 homopolymer
    (1502, 3, lambda R: R[0]),                       # AAA>A inside the homopolymer
    (2003, 3, lambda R: R[0]),                       # TAT>T inside the AT repeat
    (2008, 1, lambda R: R + "AT"),                   # A>AAT inside the AT repeat
    (299, 4, lambda R: R[:3] + ("A" if R[3] != "A" else "C")),   # 4-bp REF/ALT differing in the last base -> SNP
    (499, 1, lambda R: "T" if R != "T" else "G"),    # plain SNP
    (1003, 4, lambda R: R[0] + "," + R + "CAG"),     # CAGC>C,CAGCCAG: del and ins in one record
]
cases = [(p + 1, refseq[p:p + n], f(refseq[p:p + n])) for p, n, f in cases0]
recs = [("ref", p, ".", r, a, ".", ".", ".", ) for p, r, a in cases]
vcf = write_vcf(os.path.join(D, "a.vcf"), [], [], recs)
out = run(BIN, ["norm", "-f", REF, vcf])
got = parse_vcf(out)
# bcftools norm writes realigned records in sorted order, so compare as a set (one hit per case)
got_set = {(g["POS"], g["REF"], g["ALT"]) for g in got}
check("number of output records", len(got), len(cases))
for (p, r, a) in cases:
    tp, tr, ta = left_align(p, r, a.split(","))
    exp = (tp, tr, ",".join(ta))
    check("%d %s>%s" % (p, r, a), exp if exp in got_set else "not in output", exp)

print("   (default --multi-overlaps is 0, i.e. the other ALT becomes REF when splitting: vcfnorm.c:2600)")
print("\nB. split -m - of a multiallelic SNP with Number=A/R/G tags (samples: 1/2, 0/1, 0/2, 0/0, ./.)")
hdr = ['##INFO=<ID=AC,Number=A,Type=Integer,Description="x">', '##INFO=<ID=AF,Number=A,Type=Float,Description="x">',
       '##INFO=<ID=AN,Number=1,Type=Integer,Description="x">', '##INFO=<ID=DP,Number=1,Type=Integer,Description="x">',
       '##FORMAT=<ID=GT,Number=1,Type=String,Description="x">', '##FORMAT=<ID=PL,Number=G,Type=Integer,Description="x">',
       '##FORMAT=<ID=AD,Number=R,Type=Integer,Description="x">', '##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="x">']
smp = ["1/2:40,30,50,0,10,20:2,9,8:30", "0/1:10,0,40,50,60,70:7,6,0:20", "0/2:15,45,90,0,25,10:5,0,4:25", "0/0:0,30,60,30,60,60:12,0,0:35", "./.:.:.:."]
vcf = write_vcf(os.path.join(D, "b.vcf"), hdr, ["s1", "s2", "s3", "s4", "s5"],
                [("ref", 500, ".", refseq[499], "%s,%s" % tuple(b for b in "ACGT" if b != refseq[499])[:2], "100", "PASS", "AC=2,3;AF=0.2,0.3;AN=10;DP=50", "GT:PL:AD:GQ", smp)])
out = run(BIN, ["norm", "-m", "-", vcf])
recs = parse_vcf(out)
alts = [b for b in "ACGT" if b != refseq[499]][:2]
check("number of records", len(recs), 2)
# genotype index (a,b) -> PL index a + b(b+1)/2
for k, r in enumerate(recs):
    ialt = k + 1
    check("rec %d ALT" % k, r["ALT"], alts[k])
    check("rec %d AC,AF (Number=A element %d)" % (k, k), (r["INFO"]["AC"], r["INFO"]["AF"]), (["2", "3"][k], ["0.2", "0.3"][k]))
    check("rec %d AN,DP carried" % k, (r["INFO"]["AN"], r["INFO"]["DP"]), ("10", "50"))
    for i, (s, src) in enumerate(zip(r["samples"], smp)):
        gt, pl, ad, gq = src.split(":")
        if gt == "./.":
            check("rec %d s%d missing sample" % (k, i + 1), (s["GT"], s["PL"], s["AD"], s["GQ"]), ("./.", ".", ".,.", "."))
            continue
        pls = pl.split(","); ads = ad.split(",")
        epl = ",".join([pls[0], pls[ialt * (ialt + 1) // 2], pls[ialt * (ialt + 1) // 2 + ialt]])
        ead = ",".join([ads[0], ads[ialt]])
        # GT: this ALT -> 1, REF stays 0, the other ALT -> REF with the default --multi-overlaps 0 (vcfnorm.c:1024-1031)
        egt = "/".join("1" if a == str(ialt) else "0" for a in gt.split("/"))
        check("rec %d s%d GT,PL,AD,GQ" % (k, i + 1), (s["GT"], s["PL"], s["AD"], s["GQ"]), (egt, epl, ead, gq))

print("\nC. join -m + of the two split records back (what the merge produces for PL/GT/AC/AF/AN)")
out2 = run(BIN, ["norm", "-m", "+any", "-"], stdin=out)
j = parse_vcf(out2)
check("number of records", len(j), 1)
r = j[0]
check("ALT", r["ALT"], ",".join(alts))
check("AC, AF joined (Number=A concatenated)", (r["INFO"]["AC"], r["INFO"]["AF"]), ("2,3", "0.2,0.3"))
check("AN, DP (Number=1: taken from the first record)", (r["INFO"]["AN"], r["INFO"]["DP"]), ("10", "50"))
for i, (s, src) in enumerate(zip(r["samples"], smp)):
    gt, pl, ad, gq = src.split(":")
    print("   s%d  original %-28s joined GT=%s PL=%s AD=%s GQ=%s" % (i + 1, src, s["GT"], s["PL"], s["AD"], s["GQ"]))
print("   (PL(1/2) and the 1/2 genotype cannot be recovered from the two biallelic records; see the review for what bcftools writes)")
print("\nmismatches:", nfail)
