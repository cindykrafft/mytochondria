"""Held-up checks for bcftools merge: default INFO rules (DP:sum, AN:sum, AC:sum by allele),
AF handling (not recomputed by default), PL/GT/AD/DP of samples absent from a file, and
the PL expansion when the files carry different ALT alleles at one site.

Usage: python heldup_merge.py /path/to/bcftools
"""
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import bcftools_bin, version, run, write_vcf, parse_vcf

BIN = bcftools_bin()
print("bcftools:", version(BIN))
D = tempfile.mkdtemp(prefix="mg_")
nfail = 0
hdr = ['##INFO=<ID=DP,Number=1,Type=Integer,Description="x">', '##INFO=<ID=AN,Number=1,Type=Integer,Description="x">',
       '##INFO=<ID=AC,Number=A,Type=Integer,Description="x">', '##INFO=<ID=AF,Number=A,Type=Float,Description="x">',
       '##FORMAT=<ID=GT,Number=1,Type=String,Description="x">', '##FORMAT=<ID=PL,Number=G,Type=Integer,Description="x">',
       '##FORMAT=<ID=DP,Number=1,Type=Integer,Description="x">', '##FORMAT=<ID=AD,Number=R,Type=Integer,Description="x">']
f1 = write_vcf(os.path.join(D, "f1.vcf"), hdr, ["A", "B"], [
    ("ref", 100, ".", "A", "G", "50", "PASS", "DP=30;AN=4;AC=1;AF=0.25", "GT:PL:DP:AD", ["0/1:20,0,30:10:5,5", "0/0:0,30,60:20:20,0"]),
    ("ref", 200, ".", "C", "T", "40", "PASS", "DP=12;AN=4;AC=2;AF=0.5", "GT:PL:DP:AD", ["0/1:10,0,20:6:3,3", "0/1:15,0,25:6:3,3"]),
    ("ref", 300, ".", "A", "G", "60", "PASS", "DP=40;AN=4;AC=3;AF=0.75", "GT:PL:DP:AD", ["1/1:90,10,0:20:0,20", "0/1:30,0,40:20:10,10"]),
])
f2 = write_vcf(os.path.join(D, "f2.vcf"), hdr, ["C"], [
    ("ref", 100, ".", "A", "G", "70", "PASS", "DP=25;AN=2;AC=2;AF=1", "GT:PL:DP:AD", ["1/1:80,9,0:25:0,25"]),
    ("ref", 300, ".", "A", "T", "45", "PASS", "DP=15;AN=2;AC=1;AF=0.5", "GT:PL:DP:AD", ["0/1:22,0,33:15:8,7"]),
    ("ref", 400, ".", "G", "C", "33", "PASS", "DP=9;AN=2;AC=1;AF=0.5", "GT:PL:DP:AD", ["0/1:11,0,44:9:4,5"]),
])
for f in (f1, f2):
    run(BIN, ["view", "-Oz", "-o", f + ".gz", f]); run(BIN, ["index", f + ".gz"])
out = run(BIN, ["merge", f1 + ".gz", f2 + ".gz"])
recs = {r["POS"]: r for r in parse_vcf(out)}

def check(label, got, exp):
    global nfail
    ok = got == exp
    if not ok: nfail += 1
    print("   %-52s bcftools %-26s truth %-26s %s" % (label, got, exp, "ok" if ok else "MISMATCH"))

print("\nsite 100 (same ALT in both files): INFO rules DP:sum AN:sum AC:sum; AF is not in the default rules")
r = recs[100]
check("DP", r["INFO"]["DP"], "55"); check("AN", r["INFO"]["AN"], "6"); check("AC", r["INFO"]["AC"], "3")
print("   AF written: %s  (true AC/AN = 0.5; the first file's 0.25 or a merged value?)" % r["INFO"].get("AF"))
check("QUAL (max of the inputs)", r["QUAL"], "70")
check("samples A,B,C GT", [s["GT"] for s in r["samples"]], ["0/1", "0/0", "1/1"])
check("samples A,B,C PL", [s["PL"] for s in r["samples"]], ["20,0,30", "0,30,60", "80,9,0"])
print("\nsite 200 (file 1 only): sample C absent")
r = recs[200]
check("DP,AN,AC (only file 1 contributes)", (r["INFO"]["DP"], r["INFO"]["AN"], r["INFO"]["AC"]), ("12", "4", "2"))
check("sample C GT,PL,DP,AD missing", tuple(r["samples"][2][k] for k in ("GT", "PL", "DP", "AD")), ("./.", ".", ".", "."))
print("\nsite 300 (A>G in file 1, A>T in file 2): merged as A>G,T with Number=G/R expansion")
r = recs[300]
check("ALT", r["ALT"], "G,T")
check("AC per merged allele (3 for G, 1 for T)", r["INFO"]["AC"], "3,1"); check("AN", r["INFO"]["AN"], "6"); check("DP", r["INFO"]["DP"], "55")
check("sample A GT (1/1 of G)", r["samples"][0]["GT"], "1/1")
check("sample C GT (0/1 of T -> 0/2)", r["samples"][2]["GT"], "0/2")
# PL order for 3 alleles: 00,01,11,02,12,22; genotypes involving the allele absent from a file are missing
check("sample A PL (90,10,0 -> 90,10,0,.,.,.)", r["samples"][0]["PL"], "90,10,0,.,.,.")
check("sample C PL (22,0,33 -> 22,.,.,0,.,33)", r["samples"][2]["PL"], "22,.,.,0,.,33")
check("sample A AD (0,20 -> 0,20,.)", r["samples"][0]["AD"], "0,20,.")
check("sample C AD (8,7 -> 8,.,7)", r["samples"][2]["AD"], "8,.,7")
print("   AF written: %s" % r["INFO"].get("AF"))
print("\nsite 400 (file 2 only)")
r = recs[400]
check("samples A,B missing; C kept", [s["GT"] for s in r["samples"]], ["./.", "./.", "0/1"])
print("\nINFO fields with no rule: the manual says they take the value from the FIRST input file (doc/bcftools.txt:2146)")
hdr2 = hdr + ['##INFO=<ID=XX,Number=1,Type=Float,Description="x">', '##INFO=<ID=XS,Number=1,Type=String,Description="x">']
g1 = write_vcf(os.path.join(D, "g1.vcf"), hdr2, ["A"], [("ref", 100, ".", "A", "G", "50", "PASS", "DP=30;AF=0.25;XX=1.5;XS=first", "GT", ["0/1"])])
g2 = write_vcf(os.path.join(D, "g2.vcf"), hdr2, ["C"], [("ref", 100, ".", "A", "G", "70", "PASS", "DP=25;AF=1;XX=2.5;XS=second", "GT", ["1/1"])])
for f in (g1, g2):
    run(BIN, ["view", "-Oz", "-o", f + ".gz", f]); run(BIN, ["index", f + ".gz"])
for order, files in (("g1 g2", [g1, g2]), ("g2 g1", [g2, g1])):
    r = parse_vcf(run(BIN, ["merge"] + [f + ".gz" for f in files]))[0]
    print("   merge %s: AF=%s XX=%s XS=%s DP=%s" % (order, r["INFO"]["AF"], r["INFO"]["XX"], r["INFO"]["XS"], r["INFO"]["DP"]))
r = parse_vcf(run(BIN, ["merge", g1 + ".gz", g2 + ".gz"]))[0]
check("XX (Number=1) from the first file as documented", r["INFO"]["XX"], "1.5")
check("XS (String) from the first file as documented", r["INFO"]["XS"], "first")
check("AF (Number=A) from the first file as documented", r["INFO"]["AF"], "0.25")
print("\nwith -i 'AF:avg' the rule replaces the default handling:")
out2 = run(BIN, ["merge", "-i", "AF:avg,DP:sum,AN:sum,AC:sum", f1 + ".gz", f2 + ".gz"])
print("   site 100 AF=%s (avg of 0.25 and 1 = 0.625)" % {r["POS"]: r for r in parse_vcf(out2)}[100]["INFO"].get("AF"))
print("\nmismatches:", nfail)
