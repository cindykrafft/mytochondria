"""Shared helpers for the BCFtools audit harnesses.

Builds small BAMs (pysam) and VCFs with fully known content, runs a bcftools
binary, and parses its output. Every "truth" is computed in the harness that
uses it, not here.
"""
import os, random, subprocess, sys
import pysam

def write_ref(path, length=5000, seed=1):
    rnd = random.Random(seed)
    seq = "".join(rnd.choice("ACGT") for _ in range(length))
    with open(path, "w") as f:
        f.write(">ref\n")
        for i in range(0, length, 60):
            f.write(seq[i:i+60] + "\n")
    pysam.faidx(path)
    return seq

class Bam:
    """Collect reads, then write a coordinate-sorted, indexed BAM."""
    def __init__(self, path, ref_len, sample="S1"):
        self.path = path
        self.sample = sample
        self.header = {"HD": {"VN": "1.6", "SO": "coordinate"},
                       "SQ": [{"SN": "ref", "LN": ref_len}],
                       "RG": [{"ID": sample, "SM": sample}]}
        self.reads = []
    def add(self, name, pos0, seq, quals, mapq=60, rev=False, cigar=None, flag=None, tags=None):
        a = pysam.AlignedSegment()
        a.query_name = name
        a.query_sequence = seq
        a.flag = flag if flag is not None else (16 if rev else 0)
        a.reference_id = 0
        a.reference_start = pos0
        a.mapping_quality = mapq
        a.cigartuples = cigar if cigar is not None else [(0, len(seq))]
        a.query_qualities = pysam.qualitystring_to_array(quals) if isinstance(quals, str) else quals
        a.next_reference_id = -1
        a.next_reference_start = -1
        a.template_length = 0
        a.set_tag("RG", self.sample)
        for k, v in (tags or {}).items():
            a.set_tag(k, v)
        self.reads.append(a)
    def write(self):
        self.reads.sort(key=lambda a: (a.reference_start, a.query_name))
        with pysam.AlignmentFile(self.path, "wb", header=self.header) as out:
            for a in self.reads:
                out.write(a)
        pysam.index(self.path)
        return self.path

def run(binary, args, stdin=None, check=True):
    env = dict(os.environ)
    if "BCFTOOLS_PLUGINS" not in env:   # plugins live next to an in-tree build
        env["BCFTOOLS_PLUGINS"] = os.path.join(os.path.dirname(os.path.abspath(binary)), "plugins")
    p = subprocess.run([binary] + list(args), input=stdin, capture_output=True, text=True, env=env)
    if check and p.returncode != 0:
        sys.stderr.write(p.stderr)
        raise SystemExit("bcftools failed: %s" % " ".join(args))
    return p.stdout, p.stderr

def version(binary):
    out, _ = run(binary, ["--version"])
    return " / ".join(out.strip().splitlines()[:2])

def write_vcf(path, header_lines, samples, records):
    """records: list of (chrom,pos,id,ref,alt,qual,filter,info,format,[sample strings])."""
    with open(path, "w") as f:
        f.write("##fileformat=VCFv4.2\n")
        for h in header_lines:
            f.write(h + "\n")
        cols = ["#CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO"]
        if samples:
            cols += ["FORMAT"] + list(samples)
        f.write("\t".join(cols) + "\n")
        for r in records:
            fields = list(r[:8])
            if samples:
                fields += [r[8]] + list(r[9])
            f.write("\t".join(str(x) for x in fields) + "\n")
    return path

def vcf_records(text):
    """Parse VCF text into a list of dicts with INFO and per-sample FORMAT maps."""
    out = []
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
            if kv == ".":
                continue
            if "=" in kv:
                k, v = kv.split("=", 1)
                info[k] = v
            else:
                info[kv] = True
        rec = {"chrom": f[0], "pos": int(f[1]), "id": f[2], "ref": f[3], "alt": f[4].split(","),
               "qual": f[5], "filter": f[6], "info": info, "samples": {}}
        if len(f) > 8:
            keys = f[8].split(":")
            for s, val in zip(samples, f[9:]):
                rec["samples"][s] = dict(zip(keys, val.split(":")))
        out.append(rec)
    return out
