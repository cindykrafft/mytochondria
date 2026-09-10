#!/usr/bin/env python3
"""Held-up: bcftools norm — left-alignment/trimming of indels against an independent
Python left-aligner on a hand-made reference (repeats and homopolymers), and the
multiallelic split (-m -any) / join (-m +any) arithmetic of AC, AF, AN, GT, AD and PL.

usage: python heldup_norm_split_join.py /path/to/bcftools
"""
import os, sys, random, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import run, version, write_vcf, vcf_records, write_ref

BIN = sys.argv[1]
print("binary:", version(BIN))
tmp = tempfile.mkdtemp(prefix="nm_")
rnd = random.Random(12)
# reference with repeats: random background with planted homopolymers and tandem repeats
seq = list("".join(rnd.choice("ACGT") for _ in range(4000)))
for start, unit, n in [(200, "A", 8), (500, "CA", 6), (900, "GAT", 5), (1300, "T", 12), (1700, "ACGT", 4), (2100, "C", 6), (2500, "TTA", 7)]:
    s = unit*n
    seq[start:start+len(s)] = list(s)
seq = "".join(seq)
REF_PATH = os.path.join(tmp, "ref.fa")
with open(REF_PATH, "w") as f:
    f.write(">1\n"); [f.write(seq[i:i+60]+"\n") for i in range(0, len(seq), 60)]
import pysam; pysam.faidx(REF_PATH)

def left_align(pos1, ref, alt):
    """VCF-style normalisation: trim common suffix, then shift left while the last bases
    match, keep one shared leading base; then trim common prefix (keeping >=1 base)."""
    pos = pos1
    while len(ref) > 1 and len(alt) > 1 and ref[-1] == alt[-1]:
        ref, alt = ref[:-1], alt[:-1]
    while ref[-1] == alt[-1] and pos > 1:
        b = seq[pos-2]; pos -= 1
        ref, alt = b + ref[:-1], b + alt[:-1]
    while len(ref) > 1 and len(alt) > 1 and ref[0] == alt[0]:
        ref, alt = ref[1:], alt[1:]; pos += 1
    return pos, ref, alt

hdr = ['##contig=<ID=1,length=4000>']
recs, cases = [], []
for i in range(120):
    # random indel placed inside or after a repeat, written in a non-left-aligned way
    anchor = rnd.choice([205, 206, 208, 503, 506, 509, 903, 909, 1305, 1310, 1703, 1709, 2103, 2506, 2512, rnd.randint(100, 3800)])
    L = rnd.randint(1, 4)
    if rnd.random() < 0.5:   # deletion of seq[anchor+1 .. anchor+L]
        ref = seq[anchor-1:anchor+L]; alt = seq[anchor-1]
    else:                   # insertion after anchor of a copy of the following bases (repeat-like) or random
        ins = seq[anchor:anchor+L] if rnd.random() < 0.7 else "".join(rnd.choice("ACGT") for _ in range(L))
        ref = seq[anchor-1]; alt = seq[anchor-1] + ins
    pad = rnd.randint(0, 2)   # add redundant flanking bases on both sides
    ref2 = seq[anchor-1-pad:anchor-1] + ref + seq[anchor-1+len(ref):anchor-1+len(ref)+pad]
    alt2 = seq[anchor-1-pad:anchor-1] + alt + seq[anchor-1+len(ref):anchor-1+len(ref)+pad]
    pos2 = anchor - pad
    recs.append(("1", pos2, ".", ref2, alt2, 50, ".", "."))
    cases.append((pos2, ref2, alt2))
vcf = write_vcf(os.path.join(tmp, "indels.vcf"), hdr, [], recs)
out, err = run(BIN, ["norm", "-f", REF_PATH, vcf])
got = sorted((r["pos"], r["ref"], r["alt"][0]) for r in vcf_records(out))
exp = sorted(left_align(*c) for c in cases)
nbad = sum(1 for g, e in zip(got, exp) if g != e)
for g, e in list(zip(got, exp))[:0]: pass
print("left-alignment: %d indels (homopolymers, di/tri/tetra-nucleotide repeats, padded representations): %d differ from the Python left-aligner" % (len(cases), nbad))
for g, e in zip(got, exp):
    if g != e: print("  MISMATCH got %s expected %s" % (g, e))
print("  ", [l for l in err.splitlines() if "total" in l])
# duplicates after normalisation are expected (different padded forms of the same variant)

# ---- split / join ----
hdr2 = hdr + ['##INFO=<ID=AC,Number=A,Type=Integer,Description="x">', '##INFO=<ID=AN,Number=1,Type=Integer,Description="x">',
              '##INFO=<ID=AF,Number=A,Type=Float,Description="x">', '##INFO=<ID=DP,Number=1,Type=Integer,Description="x">',
              '##FORMAT=<ID=GT,Number=1,Type=String,Description="x">', '##FORMAT=<ID=AD,Number=R,Type=Integer,Description="x">',
              '##FORMAT=<ID=PL,Number=G,Type=Integer,Description="x">']
samples = ["s1", "s2", "s3", "s4"]
gts = ["0/1", "1/2", "2/2", "0/0"]
ad = [[10, 8, 0], [1, 6, 7], [0, 0, 12], [15, 0, 0]]
pl = [[40, 0, 60, 90, 99, 120], [80, 50, 70, 0, 20, 30], [200, 150, 160, 40, 30, 0], [0, 45, 90, 45, 90, 90]]
fmt = ["%s:%s:%s" % (g, ",".join(map(str, a)), ",".join(map(str, p))) for g, a, p in zip(gts, ad, pl)]
rec = ("1", 300, ".", "A", "G,T", 60, ".", "AC=2,3;AN=8;AF=0.25,0.375;DP=59", "GT:AD:PL", fmt)
vcf2 = write_vcf(os.path.join(tmp, "ma.vcf"), hdr2, samples, [rec])
out, _ = run(BIN, ["norm", "-m", "-any", vcf2])
rs = vcf_records(out)
print("\nsplit -m -any of A>G,T with GT 0/1,1/2,2/2,0/0 AD (10,8,0),(1,6,7),(0,0,12),(15,0,0):")
nb2 = 0
def idx(a, b): return (max(a, b)*(max(a, b)+1))//2 + min(a, b)
for k, r in enumerate(rs, start=1):
    e_ac, e_af = ["2", "3"][k-1], ["0.25", "0.375"][k-1]
    e_gt = []
    for g in gts:
        a, b = (int(x) for x in g.split("/"))
        m = lambda x: "0" if x == 0 else ("1" if x == k else ".")
        e_gt.append(m(a) + "/" + m(b))
    e_ad = [[a[0], a[k]] for a in ad]
    e_pl = [[p[idx(0, 0)], p[idx(0, k)], p[idx(k, k)]] for p in pl]
    line = "  ALT %s: AC=%s AF=%s AN=%s GT=%s AD=%s PL=%s" % (r["alt"][0], r["info"]["AC"], r["info"]["AF"], r["info"]["AN"],
        [r["samples"][s]["GT"] for s in samples], [r["samples"][s]["AD"] for s in samples], [r["samples"][s]["PL"] for s in samples])
    ok = r["info"]["AC"] == e_ac and r["info"]["AF"] == e_af and r["info"]["AN"] == "8" and [r["samples"][s]["GT"] for s in samples] == e_gt \
        and [r["samples"][s]["AD"] for s in samples] == [",".join(map(str, x)) for x in e_ad] and [r["samples"][s]["PL"] for s in samples] == [",".join(map(str, x)) for x in e_pl]
    if not ok: nb2 += 1; line += "   MISMATCH (expected GT %s AD %s PL %s)" % (e_gt, e_ad, e_pl)
    print(line)
print("  the other ALT allele in a genotype becomes '.' (--multi-overlaps . default); AN, DP, QUAL are copied; Number=A/R/G fields take the allele's slots")
out2, _ = run(BIN, ["norm", "-m", "-any", "--multi-overlaps", "0", vcf2])
print("  with --multi-overlaps 0: GT =", [[r["samples"][s]["GT"] for s in samples] for r in vcf_records(out2)])
# join back
split_path = os.path.join(tmp, "split.vcf"); open(split_path, "w").write(out)
out3, _ = run(BIN, ["norm", "-m", "+any", split_path])
j = vcf_records(out3)[0]
print("join -m +any of the two records: ALT=%s AC=%s AF=%s AN=%s GT=%s AD=%s PL=%s" % (j["alt"], j["info"]["AC"], j["info"]["AF"], j["info"]["AN"],
      [j["samples"][s]["GT"] for s in samples], [j["samples"][s]["AD"] for s in samples], [j["samples"][s]["PL"] for s in samples]))
e_join_gt = ["0/1", "1/2", "2/2", "0/0"]
e_join_ad = ["10,8,0", "1,6,7", "0,0,12", "15,0,0"]
e_join_pl = [",".join(str(p[idx(a, b)]) if (a == b or 0 in (a, b)) else "." for a in range(3) for b in range(a+1)) for p in pl]
e_join_pl = [",".join([str(p[0]), str(p[1]), str(p[2]), str(p[3]), ".", str(p[5])]) for p in pl]
ok = j["alt"] == ["G", "T"] and j["info"]["AC"] == "2,3" and j["info"]["AF"] == "0.25,0.375" and [j["samples"][s]["GT"] for s in samples] == e_join_gt \
     and [j["samples"][s]["AD"] for s in samples] == e_join_ad and [j["samples"][s]["PL"] for s in samples] == e_join_pl
print("  expected GT %s AD %s PL %s (the 1/2 PL cannot be recovered and is '.') -> %s" % (e_join_gt, e_join_ad, e_join_pl, "as expected" if ok else "MISMATCH"))
nb2 += 0 if ok else 1
print("\nmismatches: %d" % (nbad + nb2))
