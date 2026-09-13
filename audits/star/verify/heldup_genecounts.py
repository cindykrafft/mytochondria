"""--quantMode GeneCounts (ReadsPerGene.out.tab) against an independent Python counter.

Truth: STAR's own Aligned.out.sam re-counted with the documented rule (htseq-count
union mode, unique alignments only): the genes whose exons overlap any aligned block
of the read (PE: of either mate) are collected; exactly one gene -> counted, none ->
N_noFeature, several -> N_ambiguous; reads with NH > 1 -> N_multimapping; unmapped ->
N_unmapped. Column 3 keeps a gene only if read 1's strand equals the gene strand,
column 4 only if it is opposite; genes with strand '.' are kept in both. Read 1's
strand for a pair with only mate 2 aligned is the opposite of mate 2's.

Usage: python heldup_genecounts.py <STAR binary> <work dir>
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _synth as S

star, W = sys.argv[1], sys.argv[2]
g, trs, rs = S.standard_dataset(W)
gidx = S.genome_generate(star, W, os.path.join(W, "gidx"))

# exon table per chromosome: (start, end, strand, gene)
exons = collections.defaultdict(list)
for tid, tr in trs.items():
    if tr["in_gtf"]:
        for a, b in tr["exons"]:
            exons[tr["chrom"]].append((a, b, tr["strand"], tr["gene"]))
gene_ids = [gid for gid, *_ in S.GENES if _[-1]]     # GTF order


def genes_over(chrom, blocks):
    out = set()
    for a, b in blocks:
        for s, e, st, gid in exons[chrom]:
            if s <= b and e >= a:
                out.add((gid, st))
    return out


def count(sam_path, paired):
    reads = S.read_sam(sam_path)
    tab = {c: collections.Counter() for c in range(3)}
    n_unm = n_multi = 0
    for name, recs in reads.items():
        al = S.alignments(recs)
        if not al:
            n_unm += 1; continue
        if len(al) > 1:
            n_multi += 1; continue
        recs1 = list(al.values())[0]
        blocks = []
        for r in recs1:
            blocks += S.blocks_of(r)
        chrom = recs1[0].reference_name
        if paired:
            m1 = [r for r in recs1 if r.is_read1]
            r1_rev = m1[0].is_reverse if m1 else (not [r for r in recs1 if r.is_read2][0].is_reverse)
        else:
            r1_rev = recs1[0].is_reverse
        read_strand = "-" if r1_rev else "+"
        gs = genes_over(chrom, blocks)
        for col in range(3):
            if col == 0:
                keep = {gid for gid, st in gs}
            elif col == 1:
                keep = {gid for gid, st in gs if st == "." or st == read_strand}
            else:
                keep = {gid for gid, st in gs if st == "." or st != read_strand}
            if len(keep) == 0:
                tab[col]["N_noFeature"] += 1
            elif len(keep) == 1:
                tab[col][next(iter(keep))] += 1
            else:
                tab[col]["N_ambiguous"] += 1
    for col in range(3):
        tab[col]["N_unmapped"] = n_unm; tab[col]["N_multimapping"] = n_multi
    return tab


def compare(outdir, paired, label):
    star_tab = {}
    for line in open(os.path.join(outdir, "ReadsPerGene.out.tab")):
        f = line.rstrip("\n").split("\t")
        star_tab[f[0]] = [int(x) for x in f[1:]]
    truth = count(os.path.join(outdir, "Aligned.out.sam"), paired)
    rows = ["N_unmapped", "N_multimapping", "N_noFeature", "N_ambiguous"] + gene_ids
    ndiff = 0
    print("\n== %s ==" % label)
    print("%-16s %-24s %-24s" % ("row", "STAR (unstr, yes, rev)", "truth (unstr, yes, rev)"))
    for r in rows:
        t = [truth[c][r] for c in range(3)]
        s = star_tab.get(r)
        flag = "" if s == t else "   <-- DIFFERS"
        if s != t:
            ndiff += 1
        print("%-16s %-24s %-24s%s" % (r, s, t, flag))
    lf = S.log_final(outdir)
    unm = sum(int(lf[k]) for k in ("Number of reads unmapped: too many mismatches", "Number of reads unmapped: too short",
                                    "Number of reads unmapped: other", "Number of reads mapped to too many loci"))
    print("Log.final.out: unmapped(4 classes incl. too many loci)=%d, multi=%s, unique=%s; ReadsPerGene N_unmapped=%d N_multimapping=%d; column sums=%s (input reads %s)" % (
        unm, lf["Number of reads mapped to multiple loci"], lf["Uniquely mapped reads number"], star_tab["N_unmapped"][0], star_tab["N_multimapping"][0],
        [sum(v[c] for v in star_tab.values()) for c in range(3)], lf["Number of input reads"]))
    print("rows differing from the independent counter: %d of %d" % (ndiff, len(rows)))
    return ndiff


tot = 0
o = S.run_star(star, gidx, os.path.join(W, "gc_se"), [os.path.join(W, "se.fq")])
tot += compare(o, False, "single-end, defaults")
o = S.run_star(star, gidx, os.path.join(W, "gc_pe"), [os.path.join(W, "pe_1.fq"), os.path.join(W, "pe_2.fq")])
tot += compare(o, True, "paired-end, defaults")
o = S.run_star(star, gidx, os.path.join(W, "gc_se_mm1"), [os.path.join(W, "se.fq")], extra=["--outFilterMultimapNmax", "1"])
tot += compare(o, False, "single-end, --outFilterMultimapNmax 1 (multimappers become 'too many loci' -> N_unmapped)")
o = S.run_star(star, gidx, os.path.join(W, "gc_pe_ee"), [os.path.join(W, "pe_1.fq"), os.path.join(W, "pe_2.fq")], extra=["--alignEndsType", "EndToEnd"])
tot += compare(o, True, "paired-end, --alignEndsType EndToEnd")

# the simulation truth as a sanity check on the unique counts (column 1): reads simulated
# from each gene that are unique and lie in that gene's exons only
o = os.path.join(W, "gc_se")
reads = S.read_sam(os.path.join(o, "Aligned.out.sam"))
sim = collections.Counter()
for name, recs in reads.items():
    t = rs.truth[name]
    if t["kind"] == "tx" and len(S.alignments(recs)) == 1:
        sim[t["gene"]] += 1
star_tab = {l.split("\t")[0]: int(l.split("\t")[1]) for l in open(os.path.join(o, "ReadsPerGene.out.tab"))}
print("\nsimulated unique reads per gene (SE) vs STAR unstranded column (genes with overlaps differ by design):")
for gid in gene_ids:
    print("  %-8s simulated %4d   STAR %4d" % (gid, sim[gid], star_tab[gid]))
print("\nTOTAL rows differing: %d" % tot)
