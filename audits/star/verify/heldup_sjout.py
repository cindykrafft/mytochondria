"""SJ.out.tab against an independent junction collapser and the documented --outSJfilter* rules.

Truth: from STAR's own Aligned.out.sam (all alignments), each read contributes each
distinct intron it crosses once (unique count if NH == 1, multi count otherwise; a
junction crossed by both mates or by several alignments of one read counts once); the
overhang of a read at a junction is min(left block, right block) of the adjacent M runs
and the column is the maximum over reads; motif from the genome at the intron ends
(GT/AG 1, CT/AC 2, GC/AG 3, CT/GC 4, AT/AC 5, GT/AT 6, else 0); strand from the motif
(0 for non-canonical); annotated if the intron is in the GTF. Unannotated junctions are
then filtered with the defaults of --outSJfilterCountUniqueMin 3 1 1 1,
--outSJfilterCountTotalMin 3 1 1 1, --outSJfilterOverhangMin 30 12 12 12,
--outSJfilterIntronMaxVsReadN 50000 100000 200000 and --outSJfilterDistToOtherSJmin
10 0 5 10 (distance of donor and acceptor to the nearest other junction's donor /
acceptor among the junctions that passed the count filters), as the manual describes.

Usage: python heldup_sjout.py <STAR binary> <work dir>
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _synth as S

star, W = sys.argv[1], sys.argv[2]
g, trs, rs = S.standard_dataset(W)
gidx = S.genome_generate(star, W, os.path.join(W, "gidx"))
annot = S.gtf_junctions(trs)


def collapse(sam_path, unique_only=False, cum=(3, 1, 1, 1), ctm=(3, 1, 1, 1), ohm=(30, 12, 12, 12), dist=(10, 0, 5, 10), imax=(50000, 100000, 200000)):
    reads = S.read_sam(sam_path)
    J = {}                                                   # (chrom, s, e) -> [uniq, multi, overhang]
    for name, recs in reads.items():
        al = S.alignments(recs)
        if not al or (unique_only and len(al) > 1):
            continue
        per_read = {}
        for hi, mates in al.items():
            for r in mates:
                for s, e, l, rt in S.junctions_of(r):
                    key = (r.reference_name, s, e)
                    per_read[key] = max(per_read.get(key, 0), min(l, rt))
        for key, oh in per_read.items():
            j = J.setdefault(key, [0, 0, 0])
            j[0 if len(al) == 1 else 1] += 1
            j[2] = max(j[2], oh)
    rows = {}
    for (chrom, s, e), (u, m, oh) in J.items():
        motif = S.motif_code(g, chrom, s, e)
        strand = 0 if motif == 0 else (1 if motif % 2 == 1 else 2)
        a = 1 if (chrom, s, e) in annot else 0
        cls = (motif + 1) // 2
        tot = u + m
        passed = a == 1 or ((u >= cum[cls] or tot >= ctm[cls]) and oh >= ohm[cls] and (tot > len(imax) or e - s + 1 <= imax[tot - 1]))
        if passed:
            rows[(chrom, s, e)] = [strand, motif, a, u, m, oh]
    # distance filter among the survivors (annotated exempt)
    keep = {}
    donors = collections.defaultdict(list); acceptors = collections.defaultdict(list)
    for (chrom, s, e) in rows:
        donors[chrom].append(s); acceptors[chrom].append(e)
    for key, v in rows.items():
        chrom, s, e = key
        if v[2] == 1:
            keep[key] = v; continue
        cls = (v[1] + 1) // 2
        dd = min([abs(s - x) for x in donors[chrom] if x != s] + [10**9]) if donors[chrom].count(s) == 1 else 0
        da = min([abs(e - x) for x in acceptors[chrom] if x != e] + [10**9]) if acceptors[chrom].count(e) == 1 else 0
        if dd >= dist[cls] and da >= dist[cls]:
            keep[key] = v
    return keep, J


def read_sjout(path):
    out = {}
    for line in open(path):
        f = line.split()
        out[(f[0], int(f[1]), int(f[2]))] = [int(x) for x in f[3:9]]
    return out


def compare(outdir, label, **kw):
    truth, raw = collapse(os.path.join(outdir, "Aligned.out.sam"), **kw)
    got = read_sjout(os.path.join(outdir, "SJ.out.tab"))
    keys = sorted(set(truth) | set(got))
    nd = 0
    print("\n== %s ==" % label)
    print("%-26s %-28s %-28s" % ("junction", "STAR [str mot ann uniq multi oh]", "truth"))
    for k in keys:
        t, s = truth.get(k), got.get(k)
        flag = "" if t == s else "   <-- DIFFERS"
        nd += t != s
        print("%-26s %-28s %-28s%s" % ("%s:%d-%d" % k, s, t, flag))
    print("junctions in the raw collapse (before filters): %d; passing the documented filters: %d; in SJ.out.tab: %d; rows differing: %d" % (len(raw), len(truth), len(got), nd))
    dropped = sorted(set(raw) - set(truth))
    for k in dropped:
        print("  filtered out (truth): %s:%d-%d uniq=%d multi=%d overhang=%d motif=%d" % (k + tuple(raw[k]) + (S.motif_code(g, *k),)))
    return nd


tot = 0
o = S.run_star(star, gidx, os.path.join(W, "sj_se"), [os.path.join(W, "se.fq")], quant=())
tot += compare(o, "single-end, default filters")
o = S.run_star(star, gidx, os.path.join(W, "sj_pe"), [os.path.join(W, "pe_1.fq"), os.path.join(W, "pe_2.fq")], quant=())
tot += compare(o, "paired-end, default filters (a junction crossed by both mates counts once)")
o = S.run_star(star, gidx, os.path.join(W, "sj_se_u"), [os.path.join(W, "se.fq")], quant=(), extra=["--outSJfilterReads", "Unique"])
tot += compare(o, "single-end, --outSJfilterReads Unique", unique_only=True)
o = S.run_star(star, gidx, os.path.join(W, "sj_se_raw"), [os.path.join(W, "se.fq")], quant=(),
               extra=["--outSJfilterCountUniqueMin", "1", "1", "1", "1", "--outSJfilterCountTotalMin", "1", "1", "1", "1",
                      "--outSJfilterOverhangMin", "5", "5", "5", "5", "--outSJfilterDistToOtherSJmin", "0", "0", "0", "0"])
tot += compare(o, "single-end, count/overhang/distance filters relaxed to 1/1/5/0", cum=(1,) * 4, ctm=(1,) * 4, ohm=(5,) * 4, dist=(0,) * 4)
o = S.run_star(star, gidx, os.path.join(W, "sj_se_strict"), [os.path.join(W, "se.fq")], quant=(),
               extra=["--outSJfilterCountUniqueMin", "50", "40", "30", "30", "--outSJfilterOverhangMin", "48", "48", "48", "48", "--outSJfilterDistToOtherSJmin", "10", "10", "10", "10"])
tot += compare(o, "single-end, strict count 50/40/30/30, overhang 48, distance 10 (annotated exempt)", cum=(50, 40, 30, 30), ohm=(48,) * 4, dist=(10,) * 4)
print("\nTOTAL rows differing: %d" % tot)
