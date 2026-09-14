#!/usr/bin/env python3
"""BC1 on real data, part 1: align two real SARS-CoV-2 amplicon samples (nf-core/test-datasets,
viralrecon branch, illumina/amplicon/sample1 and sample2, ARTIC-style tiled amplicons) to the
MT192765.1 reference with minimap2 (mappy, preset sr), then run the unpatched develop build
(src-base, 7abcc0d6) and the patched build (src, 0432e61e) through `mpileup | call -mv --ploidy 1`
with the depth cap raised as viral pipelines do (-d 1000000; nf-core/viralrecon uses --max-depth 0)
and at the default -d 250, and compare the bias Z scores on the called variants.
Runs from a directory holding genome.fasta and sample{1,2}_R{1,2}.fastq.gz (see the audit README)."""
import mappy as mp, pysam, gzip, os, subprocess, sys, re, collections
REF = "genome.fasta"; OUT = "."
S = "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/bcftools"
BASE, PATCHED = f"{S}/src-base/bcftools", f"{S}/src/bcftools"
a = mp.Aligner(REF, preset="sr")
ctg = list(a.seq_names)[0]; L = len(a.seq(ctg))
def fq(p):
    with gzip.open(p, "rt") as f:
        while True:
            h = f.readline()
            if not h: return
            s = f.readline().strip(); f.readline(); q = f.readline().strip()
            yield h[1:].split()[0], s, q
def align(sample):
    hdr = {"HD": {"VN": "1.6", "SO": "unsorted"}, "SQ": [{"SN": ctg, "LN": L}], "RG": [{"ID": sample, "SM": sample, "PL": "ILLUMINA"}]}
    tmp = f"{sample}.unsorted.bam"; n = m = 0
    with pysam.AlignmentFile(tmp, "wb", header=hdr) as out:
        for (n1, s1, q1), (n2, s2, q2) in zip(fq(f"{sample}_R1.fastq.gz"), fq(f"{sample}_R2.fastq.gz")):
            n += 1
            hits = list(a.map(s1, s2))
            for h in hits:
                if not h.is_primary: continue
                seg = pysam.AlignedSegment(); seg.query_name = n1
                seq, qual = (s1, q1) if h.read_num == 1 else (s2, q2)
                if h.strand < 0: seq = mp.revcomp(seq); qual = qual[::-1]
                seg.query_sequence = seq; seg.query_qualities = pysam.qualitystring_to_array(qual)
                seg.reference_id = 0; seg.reference_start = h.r_st; seg.mapping_quality = h.mapq
                cig = [(1 if op == 1 else 2 if op == 2 else 4 if op == 4 else 0, ln) for ln, op in h.cigar]
                # soft clips from query coordinates
                lead, trail = h.q_st, len(seq) - h.q_en
                if h.strand < 0: lead, trail = trail, lead
                cig = ([(4, lead)] if lead else []) + [(0 if op == 0 else op, ln) for op, ln in [(op, ln) for op, ln in cig if op != 4]] + ([(4, trail)] if trail else [])
                seg.cigar = cig
                seg.flag = 1 | 2 | (16 if h.strand < 0 else 0) | (64 if h.read_num == 1 else 128)
                seg.set_tag("RG", sample); seg.set_tag("NM", h.NM)
                out.write(seg); m += 1
    pysam.sort("-o", f"{sample}.bam", tmp); pysam.index(f"{sample}.bam"); os.remove(tmp)
    print(f"{sample}: {n} pairs, {m} primary alignments written")
for s in ("sample1", "sample2"):
    if not os.path.exists(f"{s}.bam"): align(s)
    print(s, "depth summary:", subprocess.run(["samtools", "depth", "-a", f"{s}.bam"], capture_output=True, text=True).stdout.count("\n"), "positions;",
          subprocess.run(f"samtools depth -a {s}.bam | awk '{{if($3>=1291)n++; if($3>m)m=$3}} END{{print n\" positions with depth>=1291, max \"m}}'", shell=True, capture_output=True, text=True).stdout.strip())
TAGS = ["MQBZ", "BQBZ", "RPBZ", "SCBZ", "MQSBZ"]
def mpileup(binary, bams, maxdepth, label):
    cmd = [binary, "mpileup", "-f", REF, "-d", str(maxdepth), "-a", "INFO/AD", "-Ou"] + bams
    p1 = subprocess.run(cmd, capture_output=True)
    p2 = subprocess.run([binary, "call", "-mv", "--ploidy", "1", "-Ov"], input=p1.stdout, capture_output=True)
    vcf = p2.stdout.decode(); open(f"{label}.vcf", "w").write(vcf)
    recs = {}
    for line in vcf.splitlines():
        if line.startswith("#"): continue
        f = line.split("\t"); info = dict(kv.split("=", 1) for kv in f[7].split(";") if "=" in kv)
        recs[(f[1], f[3], f[4])] = {t: float(info[t]) for t in TAGS if t in info} | {"DP": int(info.get("DP", 0)), "QUAL": float(f[5])}
    return recs
for label, bams, d in [("s1_d1e6", ["sample1.bam"], 1000000), ("s2_d1e6", ["sample2.bam"], 1000000), ("s1s2_d250", ["sample1.bam", "sample2.bam"], 250), ("s1s2_d1e6", ["sample1.bam", "sample2.bam"], 1000000)]:
    b = mpileup(BASE, bams, d, label + ".base"); pch = mpileup(PATCHED, bams, d, label + ".patched")
    print(f"\n[{label}] called variants: {len(b)} (base) {len(pch)} (patched); same sites: {set(b) == set(pch)}")
    diff = collections.Counter(); worst = {}
    for k in b:
        for t in TAGS:
            if t in b[k] and t in pch[k] and abs(b[k][t] - pch[k][t]) > 1e-6:
                diff[t] += 1; worst[t] = max(worst.get(t, (0,)), (abs(b[k][t] - pch[k][t]), k[0], b[k][t], pch[k][t], b[k]["DP"]))
    print("  sites where a bias Z differs base vs patched:", dict(diff) or "none")
    for t, w in worst.items(): print(f"    {t}: largest change at pos {w[1]} (DP {w[4]}): base {w[2]:.3f} -> patched {w[3]:.3f}")
    deep = [k for k in b if b[k]["DP"] >= 1291]
    print(f"  called sites with DP >= 1291: {len(deep)} of {len(b)}")
    for thr in (-3.0, -5.0):
        for t in ("MQBZ", "RPBZ", "BQBZ", "SCBZ"):
            fb = {k for k in b if t in b[k] and b[k][t] < thr}; fp = {k for k in pch if t in pch[k] and pch[k][t] < thr}
            if fb != fp: print(f"    filter {t} < {thr}: base removes {len(fb)}, patched removes {len(fp)}, differing sites: {sorted(fb ^ fp)[:6]}")
