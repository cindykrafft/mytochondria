"""Shared helpers for the samtools harnesses: build coordinate-sorted BAMs from
plain Python records with pysam, run a samtools binary, and compute truths.

Every harness takes the samtools binary as argv[1] (default: `samtools` on PATH).
"""
import collections, os, re, subprocess, sys, tempfile
import pysam

CIG_RE = re.compile(r"(\d+)([MIDNSHP=X])")

def samtools_bin():
    return sys.argv[1] if len(sys.argv) > 1 else "samtools"

def run(*args, stdin=None):
    p = subprocess.run([samtools_bin()] + [str(a) for a in args],
                       capture_output=True, text=True, errors="replace", input=stdin)
    return p.stdout, p.stderr, p.returncode

def version():
    out, _, _ = run("--version")
    return " / ".join(out.splitlines()[:2])

def parse_cigar(cig):
    return [(int(n), op) for n, op in CIG_RE.findall(cig)]

def ref_len(cig):
    return sum(n for n, op in parse_cigar(cig) if op in "MDN=X")

def qlen(cig):
    return sum(n for n, op in parse_cigar(cig) if op in "MIS=X")

def write_bam(path, records, refs, sort=True):
    """records: dicts with keys name,flag,tid,pos,mapq,cigar,seq,qual(list),mtid,mpos,tlen,tags(dict)."""
    header = {"HD": {"VN": "1.6", "SO": "coordinate"},
              "SQ": [{"SN": n, "LN": L} for n, L in refs]}
    if sort:
        records = sorted(records, key=lambda r: (r["tid"] if r["tid"] >= 0 else 1 << 30, r["pos"]))
    with pysam.AlignmentFile(path, "wb", header=header) as f:
        for r in records:
            a = pysam.AlignedSegment()
            a.query_name = r["name"]; a.flag = r["flag"]
            a.reference_id = r["tid"]; a.reference_start = r["pos"]
            a.mapping_quality = r.get("mapq", 60)
            if r.get("cigar"): a.cigarstring = r["cigar"]
            a.query_sequence = r["seq"]
            a.query_qualities = pysam.qualitystring_to_array("".join(chr(q + 33) for q in r["qual"]))
            a.next_reference_id = r.get("mtid", -1); a.next_reference_start = r.get("mpos", -1)
            a.template_length = r.get("tlen", 0)
            if r.get("tags"): a.set_tags(list(r["tags"].items()))
            f.write(a)
    pysam.index(path)
    return path

def simple_read(name, pos, cigar, flag=0, tid=0, mapq=60, qual=30, seq=None, **kw):
    n = qlen(cigar)
    r = dict(name=name, flag=flag, tid=tid, pos=pos, mapq=mapq, cigar=cigar,
             seq=seq or "A" * n, qual=[qual] * n if isinstance(qual, int) else list(qual))
    r.update(kw)
    return r

def depth_truth(records, tid, include_del=False, min_bq=0, min_mq=0,
                excl=0x4 | 0x100 | 0x200 | 0x400):
    """Per-position depth over M/=/X bases (and D with include_del) for one tid."""
    d = collections.Counter()
    for r in records:
        if r["tid"] != tid or (r["flag"] & excl) or r["mapq"] < min_mq:
            continue
        p, s = r["pos"], 0
        for n, op in parse_cigar(r["cigar"]):
            if op in "M=X":
                for i in range(n):
                    if r["qual"][s + i] >= min_bq:
                        d[p + i] += 1
                p += n; s += n
            elif op == "D":
                if include_del:
                    for i in range(n):
                        d[p + i] += 1
                p += n
            elif op == "N":
                p += n
            elif op in "IS":
                s += n
    return d

def cov_hist(depths):
    return collections.Counter(v for v in depths.values() if v > 0)

def parse_cov(stats_out):
    h = {}
    for l in stats_out.splitlines():
        if l.startswith("COV"):
            _, rng, mx, n = l.split("\t")
            h[int(mx)] = int(n)
    return h

def sn(stats_out):
    d = {}
    for l in stats_out.splitlines():
        if l.startswith("SN"):
            parts = l.split("\t")
            d[parts[1].rstrip(":")] = parts[2]
    return d

def tmpdir():
    d = tempfile.mkdtemp(prefix="samtools-audit-")
    return d
