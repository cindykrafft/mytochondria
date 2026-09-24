"""Shared helpers for the Picard harnesses: write a reference FASTA (+ .fai, .dict),
build coordinate-sorted BAMs from plain Python records with pysam, run picard.jar,
and parse Picard metrics files.

Every harness takes the picard jar as argv[1] (default: $PICARD_JAR or picard.jar).
"""
import collections, os, re, subprocess, sys, tempfile
import pysam

CIG_RE = re.compile(r"(\d+)([MIDNSHP=X])")

def picard_jar():
    return sys.argv[1] if len(sys.argv) > 1 else os.environ.get("PICARD_JAR", "picard.jar")

def run(tool, *args, quiet=True):
    """Run a Picard tool with new-style arguments (--ARG value)."""
    argl = [str(a) for a in args]
    if quiet:
        argl += ["--QUIET", "true", "--VERBOSITY", "ERROR"]
    if os.environ.get("PICARD_LEGACY"):   # Picard 2.x legacy syntax: ARG=value
        short = {"-I": "INPUT", "-O": "OUTPUT", "-R": "REFERENCE_SEQUENCE", "-S": "SUMMARY_OUTPUT", "-M": "METRICS_FILE", "-H": "HISTOGRAM_FILE"}
        out = []; i = 0
        while i < len(argl):
            a = argl[i]
            if a.startswith("--"): out.append(f"{a[2:]}={argl[i + 1]}"); i += 2
            elif a in short: out.append(f"{short[a]}={argl[i + 1]}"); i += 2
            else: out.append(a); i += 1
        argl = out
    cmd = ["java", "-Xmx2g", "-jar", picard_jar(), tool] + argl
    p = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if p.returncode != 0:
        exc = [l for l in p.stderr.splitlines() if "Exception" in l]
        raise RuntimeError(f"{tool} failed: exit {p.returncode}: {exc[0].strip()[:160] if exc else p.stderr[-300:]}")
    return p.stdout, p.stderr

def version():
    p = subprocess.run(["java", "-jar", picard_jar(), "MarkDuplicates", "--version"], capture_output=True, text=True)
    return (p.stdout + p.stderr).replace("\n", " ").strip().split("Version:")[-1].strip()[:40]

def parse_cigar(cig):
    return [(int(n), op) for n, op in CIG_RE.findall(cig)]

def ref_len(cig):
    return sum(n for n, op in parse_cigar(cig) if op in "MDN=X")

def qlen(cig):
    return sum(n for n, op in parse_cigar(cig) if op in "MIS=X")

def write_fasta(path, refs):
    """refs: list of (name, sequence). Writes .fa, .fa.fai and .dict."""
    with open(path, "w") as f:
        for n, s in refs:
            f.write(f">{n}\n")
            for i in range(0, len(s), 60):
                f.write(s[i:i + 60] + "\n")
    pysam.faidx(path)
    dict_path = re.sub(r"\.fa(sta)?$", "", path) + ".dict"
    with open(dict_path, "w") as f:
        f.write("@HD\tVN:1.6\n")
        for n, s in refs:
            f.write(f"@SQ\tSN:{n}\tLN:{len(s)}\n")
    return path

def write_bam(path, records, refs, sort=True, rg=None, extra_header=None):
    """records: dicts with keys name,flag,tid,pos(0-based),mapq,cigar,seq,qual(list),mtid,mpos,tlen,tags(dict).
    refs: list of (name, length) or (name, sequence)."""
    sq = [{"SN": n, "LN": (L if isinstance(L, int) else len(L))} for n, L in refs]
    header = {"HD": {"VN": "1.6", "SO": "coordinate" if sort else "unsorted"}, "SQ": sq}
    rgs = rg or [{"ID": "rg1", "SM": "s1", "LB": "lib1", "PL": "ILLUMINA"}]
    header["RG"] = rgs
    if extra_header:
        header.update(extra_header)
    if sort:
        records = sorted(records, key=lambda r: (r["tid"] if r["tid"] >= 0 else 1 << 30, r["pos"], r.get("order", 0)))
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
            tags = dict(r.get("tags", {}))
            tags.setdefault("RG", rgs[0]["ID"])
            a.set_tags(list(tags.items()))
            f.write(a)
    if sort:
        pysam.index(path)
    return path

def simple_read(name, pos, cigar, flag=0, tid=0, mapq=60, qual=30, seq=None, **kw):
    n = qlen(cigar)
    r = dict(name=name, flag=flag, tid=tid, pos=pos, mapq=mapq, cigar=cigar,
             seq=seq or "A" * n, qual=[qual] * n if isinstance(qual, int) else list(qual))
    r.update(kw)
    return r

def pair(name, pos1, pos2, rlen=100, tid=0, qual=30, seq1=None, seq2=None, dup=False, tags1=None, tags2=None, mapq=60, cigar1=None, cigar2=None, extra_flag=0):
    """An FR pair: read1 forward at pos1, read2 reverse at pos2 (0-based starts). TLEN from the outer ends."""
    c1 = cigar1 or f"{rlen}M"; c2 = cigar2 or f"{rlen}M"
    end2 = pos2 + ref_len(c2)
    tlen = end2 - pos1
    d = 0x400 if dup else 0
    r1 = simple_read(name, pos1, c1, flag=0x63 | d | extra_flag, tid=tid, mapq=mapq, qual=qual, seq=seq1, mtid=tid, mpos=pos2, tlen=tlen, tags=tags1 or {}, order=0)
    r2 = simple_read(name, pos2, c2, flag=0x93 | d | extra_flag, tid=tid, mapq=mapq, qual=qual, seq=seq2, mtid=tid, mpos=pos1, tlen=-tlen, tags=tags2 or {}, order=1)
    return [r1, r2]

def parse_metrics(path):
    """Returns (list of dicts for the METRICS CLASS table, dict of histograms {label: {bin: value}})."""
    lines = open(path).read().splitlines()
    metrics, hists = [], {}
    i = 0
    while i < len(lines):
        if lines[i].startswith("## METRICS CLASS"):
            header = lines[i + 1].split("\t")
            i += 2
            while i < len(lines) and lines[i].strip():
                vals = lines[i].split("\t")
                metrics.append({h: _num(v) for h, v in zip(header, vals)})
                i += 1
        elif lines[i].startswith("## HISTOGRAM"):
            header = lines[i + 1].split("\t")
            i += 2
            cols = {h: {} for h in header[1:]}
            while i < len(lines) and lines[i].strip():
                vals = lines[i].split("\t")
                b = _num(vals[0])
                for h, v in zip(header[1:], vals[1:]):
                    cols[h][b] = _num(v)
                i += 1
            hists.update(cols)
        else:
            i += 1
    return metrics, hists

def _num(v):
    if v == "" or v == "?":
        return None
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v

def tmpdir():
    return tempfile.mkdtemp(prefix="picard_audit_")

def rand_seq(rng, n, gc=0.5):
    import random
    return "".join(rng.choice("GC") if rng.random() < gc else rng.choice("AT") for _ in range(n))
