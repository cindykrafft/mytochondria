#!/usr/bin/env python3
"""Held-up check: --quantMode GeneCounts (ReadsPerGene.out.tab) against an independent
HTSeq-union port applied to STAR's own alignments, and against the simulation truth.

Usage: python heldup_genecounts.py /path/to/STAR [workdir]

Port (independent of STAR's code): for every read, if it has no mapped record it is
unmapped; if NH>1 it is a multimapper; otherwise every aligned block (M ops; D and N
split blocks) is intersected with the GTF exons; column 2 ignores strand, column 3 keeps
exons of genes on the read's strand (mate 1's strand, or what it would be for a
mate-2-only alignment), column 4 the opposite; strand-less genes accept both. One gene ->
that gene, none -> N_noFeature, several -> N_ambiguous.
"""
import sys, os, tempfile, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

star = sys.argv[1]
work = sys.argv[2] if len(sys.argv) > 2 else tempfile.mkdtemp(prefix="star_audit_")
S = Synth(os.path.join(work, "data"))
print("STAR", star_version(star), "| workdir", work)
gdir = run_star_genome(star, os.path.join(work, "genome_gtf"), S.fa, S.gtf)

COMMON = ["--quantMode", "TranscriptomeSAM", "GeneCounts", "--outSAMtype", "BAM", "Unsorted", "SortedByCoordinate",
          "--outSAMattributes", "All", "--outSAMunmapped", "Within"]
runs = {
    "SE":       run_star_map(star, gdir, os.path.join(work, "map_se/"), [S.fq_se], COMMON),
    "PE":       run_star_map(star, gdir, os.path.join(work, "map_pe/"), [S.fq_1, S.fq_2], COMMON),
    "SE_mm2":   run_star_map(star, gdir, os.path.join(work, "map_se_mm2/"), [S.fq_se], COMMON + ["--outFilterMultimapNmax", "2"]),
}

# exon table per chromosome
exons = collections.defaultdict(list)
for gid, (chrom, strand, exs) in S.gene_exons.items():
    for s, e in exs:
        exons[chrom].append((s - 1, e, strand, gid))

def port(bam):
    gcount = [collections.Counter() for _ in range(3)]
    cnone = [0, 0, 0]; cambig = [0, 0, 0]; cmulti = 0; unmapped = 0; per_read = {}
    for qname, recs in bam_by_read(bam).items():
        mapped = [r for r in recs if not r.is_unmapped]
        if not mapped:
            unmapped += 1; per_read[qname] = ("unmapped",) * 3; continue
        if mapped[0].get_tag("NH") > 1:
            cmulti += 1; per_read[qname] = ("multi",) * 3; continue
        Str = read_strand_star(mapped)
        genes = [set(), set(), set()]
        for r in mapped:
            chrom = r.reference_name
            for bs, be, qs in blocks_of(r):
                for es, ee, strand, gid in exons[chrom]:
                    if es < be and bs < ee:
                        str1 = {"+": 0, "-": 1}.get(strand)
                        for itype in range(3):
                            if itype == 1 and str1 is not None and Str != str1: continue
                            if itype == 2 and str1 is not None and Str == str1: continue
                            genes[itype].add(gid)
        res = []
        for itype in range(3):
            if len(genes[itype]) == 0: cnone[itype] += 1; res.append("none")
            elif len(genes[itype]) > 1: cambig[itype] += 1; res.append("ambig")
            else:
                g = next(iter(genes[itype])); gcount[itype][g] += 1; res.append(g)
        per_read[qname] = tuple(res)
    table = collections.OrderedDict()
    table["N_unmapped"] = (unmapped,) * 3
    table["N_multimapping"] = (cmulti,) * 3
    table["N_noFeature"] = tuple(cnone)
    table["N_ambiguous"] = tuple(cambig)
    for gid, *_ in GENES:
        table[gid] = tuple(gcount[i][gid] for i in range(3))
    return table, per_read

allok = True
for name, prefix in runs.items():
    star_tab = read_genecounts(prefix + "ReadsPerGene.out.tab")
    port_tab, per_read = port(prefix + "Aligned.out.bam")
    lf = read_logfinal(prefix + "Log.final.out")
    print("\n== %s: ReadsPerGene.out.tab vs port (unstranded / read-strand / reverse)" % name)
    print("%-16s %-24s %-24s %s" % ("row", "STAR", "port", ""))
    nbad = 0
    for k in port_tab:
        s = star_tab.get(k); p = port_tab[k]
        flag = "" if s == p else "  <-- MISMATCH"
        nbad += (s != p); allok &= (s == p)
        print("%-16s %-24s %-24s%s" % (k, s, p, flag))
    print("rows differing: %d of %d" % (nbad, len(port_tab)))
    tot = sum(v[0] for v in star_tab.values())
    print("column sums: %s ; Log.final.out input reads %s" % ([sum(v[i] for v in star_tab.values()) for i in range(3)], lf["Number of input reads"]))
    print("Log.final.out: unique %s, multi %s, too many loci %s, unmapped mism/short/other %s/%s/%s" % (
        lf["Uniquely mapped reads number"], lf["Number of reads mapped to multiple loci"], lf["Number of reads mapped to too many loci"],
        lf["Number of reads unmapped: too many mismatches"], lf["Number of reads unmapped: too short"], lf["Number of reads unmapped: other"]))
    n_unm = int(lf["Number of reads unmapped: too many mismatches"]) + int(lf["Number of reads unmapped: too short"]) + int(lf["Number of reads unmapped: other"])
    print("N_unmapped %d == unmapped(mism+short+other) %d + too many loci %s : %s" % (
        star_tab["N_unmapped"][0], n_unm, lf["Number of reads mapped to too many loci"],
        star_tab["N_unmapped"][0] == n_unm + int(lf["Number of reads mapped to too many loci"])))

    # truth comparison (unstranded column): reads simulated from a transcript, by outcome
    lib = "se" if name.startswith("SE") else "pe"
    outcome = collections.Counter()
    for qname, res in per_read.items():
        t = S.truth[qname]
        if t["lib"] != lib: continue
        exp = t.get("gid")
        got = res[0]
        if t["kind"] in ("tr", "ins", "del", "mate2junk"):
            if got == exp: outcome[("from gene", "counted to its gene")] += 1
            else: outcome[("from gene %s" % exp, got)] += 1
        else:
            outcome[(t["kind"], got)] += 1
    print("truth vs unstranded column (reads by simulated origin -> port/STAR assignment):")
    for k, v in sorted(outcome.items(), key=lambda x: -x[1]):
        print("   %-40s %6d" % (" -> ".join(k), v))
    # strand columns vs truth: sense reads of + genes should be in column 3
    if name == "SE":
        stranded = collections.Counter()
        for qname, res in per_read.items():
            t = S.truth[qname]
            if t["lib"] != lib or t["kind"] != "tr" or res[0] not in S.gene_exons: continue
            gstrand = S.gene_exons[res[0]][1]
            read_on_gene_strand = t["sense"]      # read sequence equals the transcript strand
            stranded[(gstrand, "sense" if read_on_gene_strand else "antisense", "col3" if res[1] == res[0] else ("col4" if res[2] == res[0] else "neither"))] += 1
        print("stranded columns vs truth (gene strand, read orientation -> column holding the gene):")
        for k, v in sorted(stranded.items()):
            print("   %-40s %6d" % (" ".join(k), v))

print("\nRESULT:", "all ReadsPerGene rows equal the port on every run" if allok else "DIFFERENCES FOUND")
