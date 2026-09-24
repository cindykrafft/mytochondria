"""Shared helpers for the FastQC harnesses: write FASTQ files with controlled
sequences, lengths and per-base qualities; run FastQC (the compiled head
build or a release directory) headless with --extract; parse
fastqc_data.txt into {module: (status, header, rows)} plus the summary.

Every harness takes the FastQC directory as argv[1] (default $FASTQC_DIR):
either a release unzip (containing uk/, the jars and Configuration/) or the
audit's compiled head (a directory holding build/ and the jars).
"""
import collections, glob, os, random, re, subprocess, sys, tempfile

def fastqc_dir():
    return sys.argv[1] if len(sys.argv) > 1 else os.environ.get("FASTQC_DIR", ".")

def classpath():
    d = fastqc_dir()
    parts = [os.path.join(d, "build")] if os.path.isdir(os.path.join(d, "build")) else [d]
    parts += sorted(glob.glob(os.path.join(d, "*.jar")))
    return ":".join(parts)

def version():
    d = fastqc_dir()
    for f in ("RELEASE_NOTES.txt",):
        p = os.path.join(d, f)
        if os.path.exists(p):
            m = re.search(r"FastQC v(\S+)", open(p).read())
            if m:
                return m.group(1) + (" (head build)" if os.path.isdir(os.path.join(d, "build")) else "")
    return "?"

def tmpdir():
    return tempfile.mkdtemp(prefix="fqc_")

def rand_seq(rng, n):
    return "".join(rng.choice("ACGT") for _ in range(n))

def qstr(quals):
    return "".join(chr(q + 33) for q in quals)

def write_fastq(path, reads):
    """reads: iterable of (name, seq, qual_string)."""
    with open(path, "w") as f:
        for n, s, q in reads:
            f.write(f"@{n}\n{s}\n+\n{q}\n")

def run(fastq, extra=()):
    """Run FastQC on one file; returns the parsed fastqc_data.txt."""
    out = tmpdir()
    props = {"fastqc.output_dir": out, "fastqc.unzip": "true", "fastqc.quiet": "true", "fastqc.threads": "1"}
    for e in extra:                       # extra: ("--nogroup",), ("--min_length", "50"), ... as the wrapper spells them
        pass
    i = 0; extra = list(extra)
    while i < len(extra):
        k = extra[i].lstrip("-")
        if k in ("nogroup", "expgroup", "casava", "nano", "nofilter"):
            props["fastqc." + k] = "true"; i += 1
        else:
            props["fastqc." + k] = extra[i + 1]; i += 2
    cmd = ["java", "-Djava.awt.headless=true", "-Xmx1g"] + [f"-D{k}={v}" for k, v in props.items()] + ["-cp", classpath(), "uk.ac.babraham.FastQC.FastQCApplication", fastq]
    p = subprocess.run(cmd, capture_output=True, text=True)
    files = glob.glob(os.path.join(out, "*_fastqc", "fastqc_data.txt"))
    if not files:
        raise RuntimeError("FastQC produced no data file: " + (p.stderr or p.stdout)[-800:])
    return parse_data(files[0])

def parse_data(path):
    mods = {}
    cur = None
    for line in open(path):
        line = line.rstrip("\n")
        if line.startswith(">>END_MODULE"):
            cur = None
        elif line.startswith(">>"):
            name, status = line[2:].rsplit("\t", 1)
            cur = name
            mods[cur] = dict(status=status, header=None, rows=[])
        elif cur is not None:
            if line.startswith("#"):
                if mods[cur]["header"] is None or line.startswith("#Total Deduplicated") or line.startswith("#Duplication Level"):
                    mods[cur].setdefault("comments", []).append(line)
                    if mods[cur]["header"] is None and "\t" in line and not line.startswith("#Total"):
                        mods[cur]["header"] = line[1:].split("\t")
            else:
                mods[cur]["rows"].append(line.split("\t"))
    return mods

def basic(mods):
    return {r[0]: r[1] for r in mods["Basic Statistics"]["rows"]}

def report(label, ok, detail=""):
    print(f"{'ok  ' if ok else 'FAIL'} {label}{('  ' + detail) if detail else ''}")
    return ok

# ---------------------------------------------------------------- ports
def base_groups(max_len, nogroup=False):
    """Port of BaseGroup.makeLinearBaseGroups (the default grouping)."""
    if nogroup or max_len <= 75:
        return [(i, i) for i in range(1, max_len + 1)]
    def interval(length):
        mult = 1
        while True:
            for b in (2, 5, 10):
                iv = b * mult
                groups = 9 + (length - 9) // iv + (1 if (length - 9) % iv else 0)
                if groups < 75:
                    return iv
            mult *= 10
    iv = interval(max_len)
    groups = []; start = 1
    while start <= max_len:
        end = start + iv - 1
        if start < 10: end = start
        if start == 10 and iv > 10: end = iv - 1
        if end > max_len: end = max_len
        groups.append((start, end))
        if start < 10: start += 1
        elif start == 10 and iv > 10: start = iv
        else: start += iv
    return groups

def fastqc_percentile(counts, percentile):
    """Port of QualityCount.getPercentile: counts is a dict quality -> count."""
    total = sum(counts.values())
    rank = total * percentile // 100
    c = 0
    for q in sorted(counts):
        c += counts[q]
        if c >= rank:
            return q
    return -1
