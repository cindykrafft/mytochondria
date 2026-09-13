"""Shared helpers for the BCFtools audit harnesses.

Builds synthetic references, BAMs (pysam) and VCFs where every read, quality,
position and genotype is known, runs a bcftools binary, and parses its output.
Each harness takes the bcftools binary as argv[1].
"""
import os, random, subprocess, sys, tempfile
import pysam

# scratch files go to $AUDIT_TMP when set (the audit keeps them out of /tmp)
if os.environ.get("AUDIT_TMP"):
    os.makedirs(os.environ["AUDIT_TMP"], exist_ok=True)
    tempfile.tempdir = os.environ["AUDIT_TMP"]

def bcftools_bin():
    if len(sys.argv) < 2:
        sys.exit("usage: python %s /path/to/bcftools" % sys.argv[0])
    b = os.path.abspath(sys.argv[1])
    # plugins (+fill-tags) live next to the built binary
    if not os.environ.get("BCFTOOLS_PLUGINS") and os.path.isdir(os.path.join(os.path.dirname(b), "plugins")):
        os.environ["BCFTOOLS_PLUGINS"] = os.path.join(os.path.dirname(b), "plugins")
    return b

def version(binary):
    out = subprocess.run([binary, "--version"], capture_output=True, text=True).stdout
    return " / ".join(l.strip() for l in out.splitlines()[:2])

def run(binary, args, stdin=None, check=True):
    p = subprocess.run([binary] + list(args), input=stdin, capture_output=True, text=True)
    if check and p.returncode != 0:
        sys.exit("bcftools %s failed:\n%s" % (" ".join(args), p.stderr))
    return p.stdout

def make_ref(path, length=3000, seed=1, name="ref"):
    rng = random.Random(seed)
    seq = "".join(rng.choice("ACGT") for _ in range(length))
    with open(path, "w") as fh:
        fh.write(">%s\n" % name)
        for i in range(0, length, 60):
            fh.write(seq[i:i+60] + "\n")
    pysam.faidx(path)
    return seq

def make_bam(path, ref_len, reads, ref_name="ref", rg=None):
    """reads: list of dicts with keys name, pos (0-based), seq, qual (list of ints),
    mapq, rev (bool), and optional cigar (list of (op,len)), tags (dict)."""
    hdr = {"HD": {"VN": "1.6", "SO": "coordinate"}, "SQ": [{"SN": ref_name, "LN": ref_len}]}
    if rg:
        hdr["RG"] = [{"ID": rg, "SM": rg}]
    tmp = path + ".unsorted.bam"
    with pysam.AlignmentFile(tmp, "wb", header=hdr) as fh:
        for r in reads:
            a = pysam.AlignedSegment(fh.header)
            a.query_name = r["name"]
            a.query_sequence = r["seq"]
            a.query_qualities = pysam.qualitystring_to_array("".join(chr(q+33) for q in r["qual"]))
            a.reference_id = 0
            a.reference_start = r["pos"]
            a.mapping_quality = r["mapq"]
            a.flag = 16 if r.get("rev") else 0
            a.cigar = r.get("cigar") or [(0, len(r["seq"]))]
            tags = dict(r.get("tags", {}))
            if rg:
                tags["RG"] = rg
            a.set_tags(list(tags.items()))
            fh.write(a)
    pysam.sort("-o", path, tmp)
    os.remove(tmp)
    pysam.index(path)
    return path

def site_reads(refseq, site, n, base, mapqs, bqs, read_len=100, prefix="r", strand=None, seed=0):
    """n reads of read_len covering 0-based position `site` with `base` there;
    mapqs/bqs are lists of length n (MAPQ per read, base quality at the site);
    other bases have Q30. Alternating strand unless strand is given."""
    rng = random.Random(seed)
    out = []
    for i in range(n):
        off = rng.randrange(5, read_len - 5)          # site offset within the read
        pos = site - off
        seq = list(refseq[pos:pos+read_len])
        seq[off] = base
        qual = [30] * read_len
        qual[off] = bqs[i]
        rev = (i % 2 == 1) if strand is None else strand
        out.append(dict(name="%s%04d" % (prefix, i), pos=pos, seq="".join(seq), qual=qual,
                        mapq=mapqs[i], rev=rev, tags={"NM": 0 if base == refseq[site] else 1}))
    return out

def parse_vcf(text):
    """-> list of dicts with CHROM POS REF ALT QUAL INFO (dict) FORMAT samples (list of dicts)."""
    recs = []
    samples = []
    for line in text.splitlines():
        if line.startswith("##"):
            continue
        if line.startswith("#CHROM"):
            samples = line.split("\t")[9:]
            continue
        f = line.split("\t")
        info = {}
        for kv in f[7].split(";"):
            if "=" in kv:
                k, v = kv.split("=", 1); info[k] = v
            elif kv:
                info[kv] = True
        rec = dict(CHROM=f[0], POS=int(f[1]), REF=f[3], ALT=f[4], QUAL=f[5], FILTER=f[6], INFO=info, samples=[])
        if len(f) > 8:
            keys = f[8].split(":")
            for s in f[9:]:
                rec["samples"].append(dict(zip(keys, s.split(":"))))
        rec["sample_names"] = samples
        recs.append(rec)
    return recs

def write_vcf(path, header_lines, samples, records, contigs=(("ref", 3000),)):
    """records: list of (chrom,pos,id,ref,alt,qual,filter,info,format,[sample strings])"""
    with open(path, "w") as fh:
        fh.write("##fileformat=VCFv4.2\n")
        for c, l in contigs:
            fh.write("##contig=<ID=%s,length=%d>\n" % (c, l))
        for h in header_lines:
            fh.write(h + "\n")
        fh.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO" + ("\tFORMAT\t" + "\t".join(samples) if samples else "") + "\n")
        for r in records:
            fh.write("\t".join(str(x) for x in r[:9]) + ("\t" + "\t".join(r[9]) if len(r) > 9 else "") + "\n")
    return path
