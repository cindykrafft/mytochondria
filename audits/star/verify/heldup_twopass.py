"""--twopassMode Basic: novel junctions from pass 1 are inserted before pass 2.

Documented behaviour checked: the junctions that pass the --outSJfilter* filters in pass 1
are inserted as database junctions (listed in _STARgenome/sjdbList.out.tab), reads
crossing them in pass 2 receive --sjdbScore (+2) like annotated junctions and the
SJ.out.tab column 6 reports them as annotated; reads whose overhang over a novel junction
is below --alignSJoverhangMin 5 but at least --alignSJDBoverhangMin 3 are spliced only
in pass 2.

Extra reads: 40 reads crossing the novel G12 junction (chrA 80301-81000, not in the GTF)
with a 3-base and 40 with a 4-base overhang on one side.

Usage: python heldup_twopass.py <STAR binary> <work dir>
"""
import os, sys, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _synth as S

star, W = sys.argv[1], sys.argv[2]
g, trs, rs = S.standard_dataset(W)
gidx = S.genome_generate(star, W, os.path.join(W, "gidx"))
tr = trs["T12"]; tseq = S.tr_seq(g, tr)      # exon1 80001-80300 (300 bp), exon2 81001-81300
short = []
for oh in (3, 4):
    for i in range(40):
        if i % 2 == 0:
            read = tseq[300 - oh:300 - oh + 100]           # oh bases of exon 1, rest exon 2
        else:
            read = tseq[300 + oh - 100:300 + oh]           # rest exon 1, oh bases of exon 2
        short.append(("short%d_%02d" % (oh, i), read, "I" * 100))
fq = os.path.join(W, "twopass.fq")
with open(fq, "w") as fh:
    fh.write(open(os.path.join(W, "se.fq")).read())
    for n, s, q in short:
        fh.write("@%s\n%s\n+\n%s\n" % (n, s, q))

o1 = S.run_star(star, gidx, os.path.join(W, "tp_1pass"), [fq], quant=())
o2 = S.run_star(star, gidx, os.path.join(W, "tp_2pass"), [fq], quant=(), extra=["--twopassMode", "Basic"])


def sj(path):
    return {(f[0], int(f[1]), int(f[2])): [int(x) for x in f[3:9]] for f in (l.split() for l in open(path))}


s1, s2 = sj(os.path.join(o1, "SJ.out.tab")), sj(os.path.join(o2, "SJ.out.tab"))
annot = S.gtf_junctions(trs)
inserted = set()
for line in open(os.path.join(o2, "_STARgenome", "sjdbList.out.tab")):
    f = line.split(); inserted.add((f[0], int(f[1]), int(f[2])))
print("junctions in the 1-pass SJ.out.tab: %d; database junctions after pass-1 insertion: %d (GTF %d)" % (len(s1), len(inserted), len(annot)))
novel1 = {k for k in s1 if k not in annot}
print("novel junctions in the 1-pass SJ.out.tab: %s" % sorted(novel1))
print("  all inserted for pass 2: %s; annotated-column in the 2-pass SJ.out.tab: %s" % (novel1 <= inserted, {k: s2[k][2] for k in sorted(novel1) if k in s2}))
print("%-26s %-32s %-32s" % ("junction", "1-pass [str mot ann uniq multi oh]", "2-pass"))
for k in sorted(set(s1) | set(s2)):
    print("%-26s %-32s %-32s%s" % ("%s:%d-%d" % k, s1.get(k), s2.get(k), "" if k in annot else "   novel"))

r1, r2 = S.read_sam(os.path.join(o1, "Aligned.out.sam")), S.read_sam(os.path.join(o2, "Aligned.out.sam"))
c = collections.Counter()
for name in r2:
    if name.startswith("short"):
        oh = name[5]
        for lab, rr in (("1-pass", r1), ("2-pass", r2)):
            m = [r for r in rr[name] if not r.is_unmapped]
            c[(oh, lab, "spliced" if m and "N" in m[0].cigarstring else ("unspliced " + m[0].cigarstring) if m else "unmapped")] += 1
print("\nshort-overhang reads over the novel G12 junction:")
for k in sorted(c):
    print("  overhang %s  %s  %-22s %d" % (k[0], k[1], k[2], c[k]))

das = collections.Counter()
for name, recs in r1.items():
    m1 = [r for r in recs if not r.is_unmapped]; m2 = [r for r in r2[name] if not r.is_unmapped]
    if m1 and m2 and len(m1) == 1 and len(m2) == 1:
        js = {(m1[0].reference_name, s, e) for s, e, l, rt in S.junctions_of(m1[0])}
        kind = "no junction" if not js else "GTF junction(s) only" if js <= set(annot) else "novel junction(s)"
        das[(kind, "AS 2-pass minus 1-pass = %d" % (m2[0].get_tag("AS") - m1[0].get_tag("AS")))] += 1
print("\nAS change from 1-pass to 2-pass for reads with one alignment in both runs:")
for k in sorted(das):
    print("  %-24s %-32s %d" % (k[0], k[1], das[k]))
l1, l2 = S.log_final(o1), S.log_final(o2)
for k in ("Number of input reads", "Uniquely mapped reads number", "Number of splices: Total", "Number of splices: Annotated (sjdb)", "Number of reads unmapped: too short"):
    print("  %-40s 1-pass %-8s 2-pass %s" % (k, l1[k], l2[k]))
