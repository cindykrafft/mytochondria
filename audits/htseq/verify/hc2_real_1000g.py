"""HC2 on real data: 1000 Genomes phase-3 BWA alignments of HG00096 (chr20).

Two real Illumina paired-end samples aligned upstream with bwa 0.5.9 (aln/sampe,
2012), downloaded from the public 1000 Genomes S3 bucket, counted with htseq-count
against Ensembl GRCh37 genes (chr20 only, from the iGenomes mirror on S3):

  exome   phase3/data/HG00096/exome_alignment/HG00096.chrom20.ILLUMINA.bwa.GBR.exome.20120522.bam
  lowcov  phase3/data/HG00096/alignment/HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam

The BAMs mix in a few thousand single-end records (other read groups), which
htseq-count refuses in a paired-end file, so they are filtered out first.  Three
runs per sample: unmodified main with the default `-a 10`, main with `-a 0`, and the
HC2 patch with the default.  The recovered pairs are then attributed exactly to the
pairs with one unmapped mate whose mapped mate has MAPQ >= 10.

Usage: HTSEQ_MAIN=<venv with main> HTSEQ_PATCHED=<venv with patch> python hc2_real_1000g.py [workdir]
"""
import os, sys, subprocess, collections, statistics, urllib.request
import pysam

S3 = "https://s3.amazonaws.com/1000genomes/phase3/data/HG00096/"
SAMPLES = {
    "exome": S3 + "exome_alignment/HG00096.chrom20.ILLUMINA.bwa.GBR.exome.20120522.bam",
    "lowcov": S3 + "alignment/HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam",
}
GTF_URL = "https://ngi-igenomes.s3.eu-west-1.amazonaws.com/igenomes/Homo_sapiens/Ensembl/GRCh37/Annotation/Genes/genes.gtf"
W = sys.argv[1] if len(sys.argv) > 1 else "realdata"
MAIN = os.environ["HTSEQ_MAIN"]; PATCHED = os.environ["HTSEQ_PATCHED"]
os.makedirs(W, exist_ok=True)

def fetch(url, dest):
    if not os.path.exists(dest):
        urllib.request.urlretrieve(url, dest)
    return dest

gtf = os.path.join(W, "GRCh37.chr20.gtf")
if not os.path.exists(gtf):
    with urllib.request.urlopen(GTF_URL) as r, open(gtf, "w") as o:
        for line in r:
            line = line.decode()
            if line.split("\t", 1)[0] == "20": o.write(line)

def counts(f):
    return {l.split("\t")[0]: int(l.split("\t")[1]) for l in open(f)}

def run(venv, bam, extra, out):
    if os.path.exists(out) and os.path.getsize(out) > 0:
        return counts(out)
    subprocess.run([os.path.join(venv, "bin", "htseq-count"), "-r", "pos", "-f", "bam", "-s", "no", *extra, bam, gtf],
                   stdout=open(out, "w"), stderr=open(out + ".log", "w"), check=True)
    return counts(out)

for name, url in SAMPLES.items():
    raw = fetch(url, os.path.join(W, f"HG00096.{name}.chrom20.bam"))
    paired = os.path.join(W, f"{name}.paired.bam")
    if not os.path.exists(paired):
        i = pysam.AlignmentFile(raw); o = pysam.AlignmentFile(paired, "wb", template=i)
        for r in i.fetch(until_eof=True):
            if r.is_paired: o.write(r)
        o.close(); pysam.index(paired)
    b = pysam.AlignmentFile(paired)
    pg = [(p.get("PN"), p.get("VN")) for p in b.header.get("PG", []) if p.get("PN") == "bwa"][:1]
    n = 0; one_unmapped = 0; mapq_of_unmapped = collections.Counter(); mate_ok = 0
    for r in b.fetch(until_eof=True):
        n += 1
        if r.is_unmapped and not r.mate_is_unmapped: mapq_of_unmapped[r.mapping_quality] += 1
        if not r.is_unmapped and r.mate_is_unmapped:
            one_unmapped += 1
            if r.mapping_quality >= 10: mate_ok += 1
    print(f"== {name}: aligner {pg}; {n} paired records; {one_unmapped} pairs with exactly one mate unmapped; "
          f"MAPQ on the unmapped record: {dict(mapq_of_unmapped)}; mapped mate MAPQ>=10 in {mate_ok} of them")
    a = run(MAIN, paired, [], os.path.join(W, f"{name}.main_a10.counts"))
    z = run(MAIN, paired, ["-a", "0"], os.path.join(W, f"{name}.main_a0.counts"))
    p = run(PATCHED, paired, [], os.path.join(W, f"{name}.patched_a10.counts"))
    for lab, c in (("main -a 10", a), ("main -a 0", z), ("patched -a 10", p)):
        genes = sum(v for k, v in c.items() if not k.startswith("__"))
        print(f"   {lab:14} __too_low_aQual={c['__too_low_aQual']:6d} __no_feature={c['__no_feature']:7d} __ambiguous={c['__ambiguous']:6d} gene-assigned={genes}")
    rec = a["__too_low_aQual"] - p["__too_low_aQual"]
    print(f"   pairs recovered from __too_low_aQual by the patch: {rec}  (== one-mate-unmapped pairs with mapped mate MAPQ>=10: {rec == mate_ok})")
    genes = [g for g in a if not g.startswith("__")]
    changed = [(g, a[g], p[g]) for g in genes if a[g] != p[g]]
    rel = sorted(((p[g] - a[g]) / p[g], g, a[g], p[g]) for g, _, _ in changed if p[g] > 0)
    print(f"   genes with count>0: {sum(1 for g in genes if p[g] > 0)}; genes whose count changes: {len(changed)}; "
          f"median relative change among them: {statistics.median(x[0] for x in rel):.4f}; "
          f">=1%: {sum(1 for x in rel if x[0] >= 0.01)}; >=5%: {sum(1 for x in rel if x[0] >= 0.05)}; largest: {rel[-1][0]:.3f} ({rel[-1][1]} {rel[-1][2]}->{rel[-1][3]})")
