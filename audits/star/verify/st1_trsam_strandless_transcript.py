#!/usr/bin/env python3
"""ST1: --quantMode TranscriptomeSAM inverts the strand of every read on a transcript whose
GTF strand is '.', and STARsolo's stranded Gene/GeneFull counting does the same.

Usage: python st1_trsam_strandless_transcript.py /path/to/STAR [workdir]

A 6-kb random genome carries one two-exon transcript (GT/AG intron). The same reads are
mapped against two annotations that differ only in the strand column ('+' and '.'):
10 sense reads and 10 antisense reads (single-end 100 nt), the same as pairs (2 x 75),
and 40 sense-only cDNA reads with cell barcodes for STARsolo (2 cells x 20 UMIs). For
each transcriptome record: position, strand flag, and the number of mismatches between
SEQ and the transcript sequence at that position (the record is self-consistent only
if that is ~0); then the number of records on the forward strand (what a stranded
quantifier such as RSEM --forward-prob 1 would keep) per annotation, and STARsolo's
Gene / GeneFull counts under --soloStrand Forward and Unstranded per annotation.
"""
import sys, os, tempfile, random, collections, gzip
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import run, run_star_genome, run_star_map, star_version, rc
import pysam

star = sys.argv[1]
work = sys.argv[2] if len(sys.argv) > 2 else tempfile.mkdtemp(prefix="star_st1_")
os.makedirs(work, exist_ok=True)
ver = star_version(star)
print("STAR", ver, "| workdir", work)
rng = random.Random(7)
G = "".join(rng.choice("ACGT") for _ in range(6000))
EX = [(1001, 1400), (2001, 2400)]
G = G[:1400] + "GT" + G[1402:1998] + "AG" + G[2000:]          # canonical intron 1401..2000
if G[1399] == G[1999]: G = G[:1399] + ("C" if G[1999] != "C" else "A") + G[1400:]   # no repeat at the junction
if G[2000] == G[1400]: G = G[:2000] + ("C" if G[1400] != "C" else "A") + G[2001:]
TSEQ = G[1000:1400] + G[2000:2400]                             # 800 nt transcript, '+' orientation
fa = os.path.join(work, "genome.fa")
open(fa, "w").write(">chr1\n" + "\n".join(G[i:i + 80] for i in range(0, len(G), 80)) + "\n")
gtfs = {}
for strand in ("+", "."):
    p = os.path.join(work, "genes_%s.gtf" % ("plus" if strand == "+" else "dot"))
    with open(p, "w") as fh:
        for s, e in EX:
            fh.write('chr1\tsynth\texon\t%d\t%d\t.\t%s\t.\tgene_id "GX"; transcript_id "TX";\n' % (s, e, strand))
    gtfs[strand] = p

# reads: 10 sense + 10 antisense single-end; the same as pairs; solo cDNA reads (sense) with barcodes
def wfq(path, reads):
    with open(path, "w") as fh:
        for nm, sq in reads: fh.write("@%s\n%s\n+\n%s\n" % (nm, sq, "I" * len(sq)))
se = []; p1 = []; p2 = []; truth = {}
for i in range(20):
    pos = 20 + i * 34; frag = TSEQ[pos:pos + 100]; sense = i < 10
    nm = "%s%02d" % ("s" if sense else "a", i)
    se.append((nm, frag if sense else rc(frag))); truth[nm] = sense
    fl = TSEQ[pos:pos + 250]; fl = fl if sense else rc(fl)
    p1.append((nm, fl[:75])); p2.append((nm, rc(fl)[:75]))
fq_se, fq_1, fq_2 = [os.path.join(work, f) for f in ("se.fq", "r1.fq", "r2.fq")]
wfq(fq_se, se); wfq(fq_1, p1); wfq(fq_2, p2)
CBS = ["ACGTACGTACGTACGT", "TTGCATTGCATTGCAT"]
solo_cdna = []; solo_bc = []
for ci, cb in enumerate(CBS):
    for u in range(20):
        umi = "".join(rng.choice("ACGT") for _ in range(10)); pos = 30 + u * 30
        nm = "c%d_u%02d" % (ci, u)
        solo_cdna.append((nm, TSEQ[pos:pos + 100])); solo_bc.append((nm, cb + umi))
fq_cdna, fq_bc = os.path.join(work, "solo_cdna.fq"), os.path.join(work, "solo_bc.fq")
wfq(fq_cdna, solo_cdna); wfq(fq_bc, solo_bc)

def tr_records(bam):
    out = []
    with pysam.AlignmentFile(bam, "rb") as bf:
        for r in bf:
            if r.is_unmapped: continue
            seq = r.query_sequence; tpos = r.reference_start
            mm = sum(1 for a, b in zip(seq, TSEQ[tpos:tpos + len(seq)]) if a != b)
            out.append((r.query_name, 1 if r.is_read1 else (2 if r.is_read2 else 0), r.reference_start + 1, "-" if r.is_reverse else "+", r.cigarstring, mm, r.flag))
    return out

def read_mtx(path):
    n = collections.Counter()
    for line in open(path):
        if line.startswith("%"): continue
        f = line.split()
        if len(f) == 3 and n.get("_hdr") is None: n["_hdr"] = 1; continue
        n[int(f[1])] += int(f[2])
    return {k: v for k, v in n.items() if k != "_hdr"}

affected = False
res = {}
for strand, gtf in gtfs.items():
    gdir = run_star_genome(star, os.path.join(work, "genome_" + ("plus" if strand == "+" else "dot")), fa, gtf, overhang=99)
    for lib, reads in (("SE", [fq_se]), ("PE", [fq_1, fq_2])):
        pre = run_star_map(star, gdir, os.path.join(work, "map_%s_%s/" % (lib, "plus" if strand == "+" else "dot")), reads,
                           ["--quantMode", "TranscriptomeSAM", "--outSAMtype", "BAM", "Unsorted"])
        res[(strand, lib)] = tr_records(pre + "Aligned.toTranscriptome.out.bam")
    pre = run_star_map(star, gdir, os.path.join(work, "solo_%s/" % ("plus" if strand == "+" else "dot")), [fq_cdna, fq_bc],
                       ["--soloType", "CB_UMI_Simple", "--soloCBwhitelist", "None", "--soloFeatures", "Gene", "GeneFull",
                        "--soloStrand", "Forward", "--outSAMtype", "None"])
    pre_u = run_star_map(star, gdir, os.path.join(work, "solo_%s_unstranded/" % ("plus" if strand == "+" else "dot")), [fq_cdna, fq_bc],
                         ["--soloType", "CB_UMI_Simple", "--soloCBwhitelist", "None", "--soloFeatures", "Gene", "GeneFull",
                          "--soloStrand", "Unstranded", "--outSAMtype", "None"])
    res[(strand, "solo")] = {f: sum(read_mtx(pre + "Solo.out/%s/raw/matrix.mtx" % f).values()) for f in ("Gene", "GeneFull")}
    res[(strand, "solo_unstranded")] = {f: sum(read_mtx(pre_u + "Solo.out/%s/raw/matrix.mtx" % f).values()) for f in ("Gene", "GeneFull")}

for lib in ("SE", "PE"):
    print("\n== %s: Aligned.toTranscriptome.out.bam records with the transcript annotated '+' vs '.'" % lib)
    print("   %-6s %-5s | %-5s %-3s %-6s %-7s | %-5s %-3s %-6s %-7s" % ("read", "truth", "pos", "str", "cigar", "SEQ!=tr", "pos", "str", "cigar", "SEQ!=tr"))
    plus = {(r[0], r[1]): r for r in res[("+", lib)]}; dot = {(r[0], r[1]): r for r in res[(".", lib)]}
    n_same_pos = n_flip = n_mm_plus = n_mm_dot = 0
    for k in sorted(plus):
        a = plus[k]; b = dot.get(k)
        if b is None: print("   %s missing with '.'" % (k,)); continue
        n_same_pos += a[2] == b[2]; n_flip += a[3] != b[3]; n_mm_plus += a[5]; n_mm_dot += b[5]
        if k[0] in ("s00", "s01", "a10", "a11"):
            print("   %-6s %-5s | %-5d %-3s %-6s %-7d | %-5d %-3s %-6s %-7d" % (k[0], "sense" if truth[k[0]] else "anti", a[2], a[3], a[4], a[5], b[2], b[3], b[4], b[5]))
    print("   records %d: same position in both %d, strand flag differs %d; SEQ mismatches vs transcript: '+' total %d, '.' total %d" % (
        len(plus), n_same_pos, n_flip, n_mm_plus, n_mm_dot))
    fwd_plus = sum(1 for r in res[("+", lib)] if r[1] in (0, 1) and r[3] == "+")
    fwd_dot = sum(1 for r in res[(".", lib)] if r[1] in (0, 1) and r[3] == "+")
    print("   reads whose (first) mate is on the transcript's forward strand [RSEM --forward-prob 1 keeps these]: '+' annotation %d of 20 (truth: 10 sense), '.' annotation %d" % (fwd_plus, fwd_dot))
    affected |= (n_flip == len(plus) and len(plus) > 0)

print("\n== STARsolo (40 sense cDNA reads, 2 cells): UMI counts for the gene")
for strand in ("+", "."):
    print("   annotation '%s': --soloStrand Forward  Gene %d  GeneFull %d ;  --soloStrand Unstranded  Gene %d  GeneFull %d" % (
        strand, res[(strand, "solo")]["Gene"], res[(strand, "solo")]["GeneFull"], res[(strand, "solo_unstranded")]["Gene"], res[(strand, "solo_unstranded")]["GeneFull"]))
affected |= (res[("+", "solo")]["Gene"] > 0 and res[(".", "solo")]["Gene"] == 0)
print("\nRESULT: %s -- %s" % (ver, "AFFECTED (strand inverted for the '.'-strand transcript)" if affected else "unaffected"))
