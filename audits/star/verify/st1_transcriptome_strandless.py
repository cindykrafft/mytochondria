"""STA1: Aligned.toTranscriptome.out.bam inverts the strand of every alignment to a transcript
whose GTF strand is '.' (undefined) and reverse-complements its sequence, while keeping
the '+' coordinates.

Self-contained reproduction (no _synth): a 3-kb random genome with two identical two-exon
gene structures, one on '+' (TP) and one with strand '.' (TD); four 60-bp reads, forward
and reverse, from each. Every read is an exact substring of its transcript, so the
transcriptome record of a forward read must be forward with the read sequence, and the
reverse read reverse with its sequence.

Usage: python st1_transcriptome_strandless.py <STAR binary> <work dir>
"""
import os, sys, random, subprocess, shutil
import pysam

star, W = sys.argv[1], sys.argv[2]
os.makedirs(W, exist_ok=True)
rng = random.Random(3)
COMP = str.maketrans("ACGT", "TGCA")
rc = lambda s: s.translate(COMP)[::-1]
G = list(rng.choice("ACGT") for _ in range(3000))
genes = {"TP": ("+", [(201, 500), (801, 1100)]), "TD": (".", [(1701, 2000), (2301, 2600)])}
for tid, (strand, ex) in genes.items():                      # plant GT..AG
    s, e = ex[0][1] + 1, ex[1][0] - 1
    G[s - 1], G[s], G[e - 2], G[e - 1] = "G", "T", "A", "G"
    G[s - 2] = "C"; G[e] = "C"
G = "".join(G)
open(os.path.join(W, "g.fa"), "w").write(">chr1\n" + G + "\n")
with open(os.path.join(W, "g.gtf"), "w") as fh:
    for tid, (strand, ex) in genes.items():
        for i, (a, b) in enumerate(ex):
            fh.write('chr1\tx\texon\t%d\t%d\t.\t%s\t.\tgene_id "g%s"; transcript_id "%s";\n' % (a, b, strand, tid, tid))
reads = []
with open(os.path.join(W, "r.fq"), "w") as fh:
    for tid, (strand, ex) in genes.items():
        tseq = G[ex[0][0] - 1:ex[0][1]] + G[ex[1][0] - 1:ex[1][1]]
        for off in (100, 270):                                # exonic, and spanning the junction
            frag = tseq[off:off + 60]
            for lab, seq in (("fwd", frag), ("rev", rc(frag))):
                name = "%s_%s_%d" % (tid, lab, off)
                reads.append((name, tid, off + 1, lab == "rev", seq))
                fh.write("@%s\n%s\n+\n%s\n" % (name, seq, "I" * 60))
gd = os.path.join(W, "gidx"); shutil.rmtree(gd, ignore_errors=True); os.makedirs(gd)
run = lambda cmd: subprocess.run(cmd, check=True, capture_output=True, text=True)
run([star, "--runMode", "genomeGenerate", "--genomeDir", gd, "--genomeFastaFiles", os.path.join(W, "g.fa"), "--sjdbGTFfile", os.path.join(W, "g.gtf"),
     "--sjdbOverhang", "59", "--genomeSAindexNbases", "4", "--outFileNamePrefix", gd + "/"])
od = os.path.join(W, "map"); shutil.rmtree(od, ignore_errors=True); os.makedirs(od)
run([star, "--genomeDir", gd, "--readFilesIn", os.path.join(W, "r.fq"), "--outFileNamePrefix", od + "/", "--outSAMtype", "SAM", "--quantMode", "TranscriptomeSAM"])
print(open(os.path.join(od, "Log.final.out")).read().split("UNIQUE READS:")[1].split("Number of splices: Total")[0].strip())
got = {}
with pysam.AlignmentFile(os.path.join(od, "Aligned.toTranscriptome.out.bam"), "rb") as fh:
    for r in fh:
        got[r.query_name] = (r.reference_name, r.reference_start + 1, r.is_reverse, r.cigarstring, r.query_sequence)
gen = {}
with pysam.AlignmentFile(os.path.join(od, "Aligned.out.sam"), "r") as fh:
    for r in fh:
        gen[r.query_name] = (r.reference_name, r.reference_start + 1, r.is_reverse, r.cigarstring)
bad = 0
print("%-12s %-28s %-36s %-36s" % ("read", "genomic (chr, pos, rev, CIGAR)", "transcriptome expected (tr,pos,rev,CIGAR,seq)", "transcriptome got"))
for name, tid, pos, rev, seq in reads:
    exp = (tid, pos, rev, "60M", seq if not rev else rc(seq))
    gt = got.get(name)
    flag = "" if gt == exp else "   <-- DIFFERS (%s)" % ("strand flag and sequence" if gt and gt[:2] == exp[:2] else "other")
    bad += gt != exp
    print("%-12s %-28s %-36s %-36s%s" % (name, gen.get(name), exp[:4] + (exp[4][:10] + "..",), (gt[:4] + (gt[4][:10] + "..",)) if gt else None, flag))
print("records differing from expectation: %d of %d (TP '+': %d, TD '.': %d)" % (bad, len(reads),
      sum(got.get(n) != (t, p, r, "60M", s if not r else rc(s)) for n, t, p, r, s in reads if t == "TP"),
      sum(got.get(n) != (t, p, r, "60M", s if not r else rc(s)) for n, t, p, r, s in reads if t == "TD")))
