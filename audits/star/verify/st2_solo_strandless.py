"""STA2: STARsolo stranded counting (--soloFeatures Gene, GeneFull, GeneFull_ExonOverIntron,
GeneFull_Ex50pAS) of genes whose GTF strand is '.' (undefined).

Truth: 300 sense-strand cDNA reads (read 2 in 10x-style CB+UMI / cDNA pairs, one cell
barcode, a distinct UMI per read) are simulated from each of T1 ('+'), T2 ('-'), T3 ('.',
two exons) and T4 ('.', one exon) of the shared synthetic genome, so every read has the
strand of the RNA. With --soloStrand Forward every gene should receive its 300 reads;
with Reverse none; with Unstranded all. --quantMode GeneCounts on the same reads (column
3, "1st read strand aligned with RNA") counts a '.' gene from both strands, which is the
documented STAR convention for undefined strands. The four solo features are read from
Solo.out/<feature>/raw/matrix.mtx (features.tsv gives the gene order).

Usage: python st2_solo_strandless.py <STAR binary> <work dir>
"""
import os, sys, random, subprocess, shutil, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _synth as S

star, W = sys.argv[1], sys.argv[2]
g, trs, rs = S.standard_dataset(W)
gidx = S.genome_generate(star, W, os.path.join(W, "gidx"))
rng = random.Random(9)
CB = "ACGTACGTACGTACGT"
tids = ["T1", "T2", "T3", "T4"]
umis = set()
with open(os.path.join(W, "solo_cdna.fq"), "w") as f2, open(os.path.join(W, "solo_bc.fq"), "w") as f1:
    for tid in tids:
        seq = S.tr_seq(g, trs[tid])
        for i in range(300):
            off = rng.randrange(0, len(seq) - 90 + 1)
            read = seq[off:off + 90]                          # sense strand of the RNA
            while True:
                umi = "".join(rng.choice("ACGT") for _ in range(12))
                if umi not in umis:
                    umis.add(umi); break
            name = "%s_%03d" % (tid, i)
            f2.write("@%s\n%s\n+\n%s\n" % (name, read, "I" * 90))
            f1.write("@%s\n%s%s\n+\n%s\n" % (name, CB, umi, "I" * 28))
open(os.path.join(W, "wl.txt"), "w").write(CB + "\n")


def solo_counts(outdir, feature):
    d = os.path.join(outdir, "Solo.out", feature, "raw")
    genes = [l.split("\t")[0] for l in open(os.path.join(d, "features.tsv"))]
    counts = collections.Counter()
    for line in open(os.path.join(d, "matrix.mtx")):
        if line.startswith("%"):
            continue
        f = line.split()
        if len(f) == 3 and f[0] != "":
            if counts.get("_hdr") is None:
                counts["_hdr"] = 1; continue
            counts[genes[int(f[0]) - 1]] += int(f[2])
    return counts


features = ["Gene", "GeneFull", "GeneFull_ExonOverIntron", "GeneFull_Ex50pAS"]
ver = subprocess.run([star, "--version"], capture_output=True, text=True).stdout.strip()
import re
vt = tuple(int(x) for x in re.findall(r"\d+", ver)[:3])
if vt < (2, 7, 10):                                          # GeneFull_ExonOverIntron / GeneFull_Ex50pAS were added in 2.7.10a
    features = ["Gene", "GeneFull"]
print("STAR %s; solo features tested: %s" % (ver, " ".join(features)))
results = {}
for strand in ("Forward", "Reverse", "Unstranded"):
    o = S.run_star(star, gidx, os.path.join(W, "solo_" + strand), [os.path.join(W, "solo_cdna.fq"), os.path.join(W, "solo_bc.fq")],
                   quant=("GeneCounts",), attrs=("NH", "HI", "AS", "nM"),
                   extra=["--soloType", "CB_UMI_Simple", "--soloCBwhitelist", os.path.join(W, "wl.txt"), "--soloUMIlen", "12",
                          "--soloFeatures"] + features + ["--soloStrand", strand])
    gc = {l.split("\t")[0]: [int(x) for x in l.split("\t")[1:]] for l in open(os.path.join(o, "ReadsPerGene.out.tab"))}
    results[strand] = {f: solo_counts(o, f) for f in features}
    results[strand]["GeneCounts col2/3/4"] = gc
    lf = S.log_final(o)
    print("\n== --soloStrand %s (uniquely mapped %s of %s reads) ==" % (strand, lf["Uniquely mapped reads number"], lf["Number of input reads"]))
    print("%-10s %-7s " % ("gene", "strand") + "".join("%-26s" % f for f in features) + "GeneCounts [unstr, yes, rev]")
    for gid, st in (("G1", "+"), ("G2", "-"), ("G3", "."), ("G4", ".")):
        print("%-10s %-7s " % (gid, st) + "".join("%-26d" % results[strand][f][gid] for f in features) + str(gc[gid]))
bad = 0
for f in features:
    for gid in ("G3", "G4"):
        fwd, rev = results["Forward"][f][gid], results["Reverse"][f][gid]
        ok = fwd == 300
        bad += not ok
        print("%-26s %s ('.'): Forward %3d  Reverse %3d  Unstranded %3d  -> %s" % (f, gid, fwd, rev, results["Unstranded"][f][gid],
              "as documented (sense reads counted with Forward)" if ok else "DIFFERS: sense reads dropped with Forward, counted with Reverse"))
print("'.'-strand gene/feature combinations with 0 of 300 sense reads under --soloStrand Forward: %d of %d" % (bad, 2 * len(features)))
