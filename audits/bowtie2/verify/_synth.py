"""Shared helpers for the Bowtie 2 harnesses: random references, index building,
reads with known edits (and therefore known expected CIGAR/MD/NM/XM/XO/XG/AS),
running bowtie2-align-s, parsing SAM records and the stderr alignment summary,
and Python ports of the pieces of Bowtie 2 whose arithmetic is checked here
(the mismatch-penalty table, the --score-min function, the MAPQ V2 calculator,
the paired-end classifier).

Every harness takes the directory holding bowtie2-align-s / bowtie2-build-s as
argv[1] (default $BT2_DIR, else the current directory).
"""
import collections, os, re, subprocess, sys, tempfile
import numpy as np

CIG_RE = re.compile(r"(\d+)([MIDNSHP=X])")
COMP = str.maketrans("ACGTN", "TGCAN")

def bt2_dir():
    return sys.argv[1] if len(sys.argv) > 1 else os.environ.get("BT2_DIR", ".")

def align_bin():
    return os.path.join(bt2_dir(), "bowtie2-align-s")

def build_bin():
    return os.path.join(bt2_dir(), "bowtie2-build-s")

def version():
    p = subprocess.run([align_bin(), "--version"], capture_output=True, text=True)
    return p.stdout.splitlines()[0].split("version")[-1].strip()

def tmpdir():
    return tempfile.mkdtemp(prefix="bt2h_")

def rand_seq(rng, n):
    return "".join(rng.choice("ACGT") for _ in range(n))

def revcomp(s):
    return s.translate(COMP)[::-1]

def write_fasta(path, refs):
    with open(path, "w") as f:
        for n, s in refs:
            f.write(f">{n}\n")
            for i in range(0, len(s), 60):
                f.write(s[i:i + 60] + "\n")

def build_index(fa, prefix):
    p = subprocess.run([build_bin(), "-q", fa, prefix], capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("bowtie2-build failed: " + p.stderr[-400:])
    return prefix

def write_fastq(path, reads):
    """reads: iterable of (name, seq, qual_string)."""
    with open(path, "w") as f:
        for n, s, q in reads:
            f.write(f"@{n}\n{s}\n+\n{q}\n")

Rec = collections.namedtuple("Rec", "qname flag rname pos mapq cigar rnext pnext tlen seq qual tags")

def parse_sam(path):
    out = []
    with open(path) as f:
        for line in f:
            if line.startswith("@"):
                continue
            t = line.rstrip("\n").split("\t")
            tags = {}
            for x in t[11:]:
                k, typ, v = x.split(":", 2)
                tags[k] = int(v) if typ == "i" else v
            out.append(Rec(t[0], int(t[1]), t[2], int(t[3]), int(t[4]), t[5], t[6], int(t[7]), int(t[8]), t[9], t[10], tags))
    return out

def align(index, unpaired=None, mates=None, args=(), workdir=None, wrapper=False):
    """Run bowtie2-align-s (or the perl wrapper `bowtie2` when wrapper=True,
    needed for --un-conc/--al-conc). unpaired: list of (name, seq, qual); mates:
    list of ((name, seq1, qual1), (name, seq2, qual2)). Returns (records, stderr)."""
    d = workdir or tmpdir()
    exe = os.path.join(bt2_dir(), "bowtie2") if wrapper else align_bin()
    cmd = [exe, "-x", index, "-S", os.path.join(d, "out.sam"), "--seed", "7"] + [str(a) for a in args]
    if unpaired:
        write_fastq(os.path.join(d, "u.fq"), unpaired)
        cmd += ["-U", os.path.join(d, "u.fq")]
    if mates:
        write_fastq(os.path.join(d, "m1.fq"), [m[0] for m in mates])
        write_fastq(os.path.join(d, "m2.fq"), [m[1] for m in mates])
        cmd += ["-1", os.path.join(d, "m1.fq"), "-2", os.path.join(d, "m2.fq")]
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=d)
    if p.returncode != 0:
        raise RuntimeError("bowtie2 failed: " + p.stderr[-600:])
    return parse_sam(os.path.join(d, "out.sam")), p.stderr

SUMMARY_KEYS = [
    ("reads", r"^(\d+) reads; of these:"),
    ("paired", r"^\s+(\d+) \([\d.]+%\) were paired"),
    ("conc0", r"^\s+(\d+) \([\d.]+%\) aligned concordantly 0 times"),
    ("conc1", r"^\s+(\d+) \([\d.]+%\) aligned concordantly exactly 1 time"),
    ("concM", r"^\s+(\d+) \([\d.]+%\) aligned concordantly >1 times"),
    ("disc1", r"^\s+(\d+) \([\d.]+%\) aligned discordantly 1 time"),
    ("mates", r"^\s+(\d+) mates make up the pairs"),
    ("mate0", r"^\s+(\d+) \([\d.]+%\) aligned 0 times$"),
    ("mate1", r"^\s+(\d+) \([\d.]+%\) aligned exactly 1 time$"),
    ("mateM", r"^\s+(\d+) \([\d.]+%\) aligned >1 times$"),
    ("unpaired", r"^\s+(\d+) \([\d.]+%\) were unpaired"),
    ("rate", r"^([\d.]+)% overall alignment rate"),
]

def parse_summary(stderr):
    """Returns the numbers of the stderr summary. For the mate lines (indented 8)
    and the unpaired lines (indented 4) the same regexes match, so the
    unpaired block's three lines are keyed unp0/unp1/unpM by position."""
    out = {}
    lines = stderr.splitlines()
    in_unpaired = False
    for line in lines:
        if "were unpaired" in line:
            in_unpaired = True
        for k, rx in SUMMARY_KEYS:
            m = re.match(rx, line)
            if m:
                key = k
                if in_unpaired and k in ("mate0", "mate1", "mateM"):
                    key = {"mate0": "unp0", "mate1": "unp1", "mateM": "unpM"}[k]
                val = float(m.group(1)) if k == "rate" else int(m.group(1))
                out.setdefault(key, val)
    return out

# ---------------------------------------------------------------- scoring ports
F32 = lambda x: float(np.float32(x))

def mm_pen(q, mx=6, mn=2):
    """scoring.h initPens, COST_MODEL_QUAL: consMin + (int)(frac * (consMax - consMin)),
    frac = (float)min(q, 40) / 40.0f."""
    frac = np.float32(min(q, 40)) / np.float32(40.0)
    return mn + int(np.float32(frac * np.float32(mx - mn)))

def score_min(L, mode="e2e", func=None):
    """SimpleFunc::f<int64> with truncation toward zero. Defaults: L,-0.6,-0.6
    (end-to-end) and G,20,8 (local)."""
    if func is None:
        func = ("L", -0.6, -0.6) if mode == "e2e" else ("G", 20.0, 8.0)
    typ, c, l = func
    x = {"C": 0.0, "L": float(L), "S": float(L) ** 0.5, "G": float(np.log(L))}[typ]
    return int(c + l * x)

def perfect(L, mode):
    return 0 if mode == "e2e" else 2 * L

def mapq_v2(best, secbest, L, oL=None, mode="e2e", func=None):
    """Port of BowtieMapq2::mapq (unique.h). best/secbest: AS (and, for a
    concordant pair, the sums over both mates); secbest None if no second-best.
    L: read length; oL: opposite mate's length for a pair (None = unpaired)."""
    monotone = mode == "e2e"
    scPer = perfect(L, mode) + (perfect(oL, mode) if oL is not None else 0)
    scMin = score_min(L, mode, func) + (score_min(oL, mode, func) if oL is not None else 0)
    diff = max(1, scPer - scMin)
    bestOver = best - scMin
    f = lambda c: diff * F32(c)
    if monotone:
        if secbest is None:
            for thr, r in ((0.8, 42), (0.7, 40), (0.6, 24), (0.5, 23), (0.4, 8), (0.3, 3)):
                if bestOver >= f(thr):
                    return r
            return 0
        bestdiff = abs(abs(best) - abs(secbest))
        if bestdiff >= f(0.9): return 39 if bestOver == diff else 33
        if bestdiff >= f(0.8): return 38 if bestOver == diff else 27
        if bestdiff >= f(0.7): return 37 if bestOver == diff else 26
        if bestdiff >= f(0.6): return 36 if bestOver == diff else 22
        if bestdiff >= f(0.5):
            return 35 if bestOver == diff else 25 if bestOver >= f(0.84) else 16 if bestOver >= f(0.68) else 5
        if bestdiff >= f(0.4):
            return 34 if bestOver == diff else 21 if bestOver >= f(0.84) else 14 if bestOver >= f(0.68) else 4
        if bestdiff >= f(0.3):
            return 32 if bestOver == diff else 18 if bestOver >= f(0.88) else 15 if bestOver >= f(0.67) else 3
        if bestdiff >= f(0.2):
            return 31 if bestOver == diff else 17 if bestOver >= f(0.88) else 11 if bestOver >= f(0.67) else 0
        if bestdiff >= f(0.1):
            return 30 if bestOver == diff else 12 if bestOver >= f(0.88) else 7 if bestOver >= f(0.67) else 0
        if bestdiff > 0:
            return 6 if bestOver >= f(0.67) else 2
        return 1 if bestOver >= f(0.67) else 0
    else:
        if secbest is None:
            for thr, r in ((0.8, 44), (0.7, 42), (0.6, 41), (0.5, 36), (0.4, 28), (0.3, 24)):
                if bestOver >= f(thr):
                    return r
            return 22
        bestdiff = abs(abs(best) - abs(secbest))
        if bestdiff >= f(0.9): return 40
        if bestdiff >= f(0.8): return 39
        if bestdiff >= f(0.7): return 38
        if bestdiff >= f(0.6): return 37
        if bestdiff >= f(0.5): return 35 if bestOver == diff else 25 if bestOver >= f(0.5) else 20
        if bestdiff >= f(0.4): return 34 if bestOver == diff else 21 if bestOver >= f(0.5) else 19
        if bestdiff >= f(0.3): return 33 if bestOver == diff else 18 if bestOver >= f(0.5) else 16
        if bestdiff >= f(0.2): return 32 if bestOver == diff else 17 if bestOver >= f(0.5) else 12
        if bestdiff >= f(0.1): return 31 if bestOver == diff else 14 if bestOver >= f(0.5) else 9
        if bestdiff > 0: return 11 if bestOver >= f(0.5) else 2
        return 1 if bestOver >= f(0.5) else 0

def classify_pair(off1, len1, fw1, off2, len2, fw2, pol="FR", maxfrag=500, minfrag=0,
                  olap_ok=True, contain_ok=True, dovetail_ok=False):
    """Port of PairedEndPolicy::peClassifyPair (pe.cpp): off = 0-based leftmost
    reference offset of the aligned extent, len = reference extent. Returns
    'DISCORD', 'NORMAL', 'OVERLAP', 'CONTAIN' or 'DOVETAIL'."""
    minfrag = max(minfrag, 1)
    if pol in ("FF", "RR"):
        if fw1 != fw2: return "DISCORD"
        oneLeft = fw1 if pol == "FF" else not fw1
    else:
        if fw1 == fw2: return "DISCORD"
        oneLeft = fw1 if pol == "FR" else not fw1
    frag = max(off1 + len1, off2 + len2) - min(off1, off2)
    if frag > maxfrag or frag < minfrag:
        return "DISCORD"
    lo1, hi1, lo2, hi2 = off1, off1 + len1 - 1, off2, off2 + len2 - 1
    containment = (lo1 >= lo2 and hi1 <= hi2) or (lo2 >= lo1 and hi2 <= hi1)
    typ = "NORMAL"; olap = False
    if (lo1 <= lo2 <= hi1) or (lo1 <= hi2 <= hi1) or containment:
        olap = True
        if not olap_ok: return "DISCORD"
        typ = "OVERLAP"
    if not olap:
        if (oneLeft and lo2 < lo1) or (not oneLeft and lo1 < lo2):
            return "DISCORD"
    if containment:
        if not contain_ok: return "DISCORD"
        typ = "CONTAIN"
    if (oneLeft and (hi1 > hi2 or lo2 < lo1)) or (not oneLeft and (hi2 > hi1 or lo1 < lo2)):
        if not dovetail_ok: return "DISCORD"
        typ = "DOVETAIL"
    return typ

# ------------------------------------------------------------- read builder
def make_read(name, ref, pos0, length, fw=True, edits=(), qual=40, mode="e2e",
              mm_max=6, mm_min=2, npen=1, rdg=(5, 3), rfg=(5, 3), ma=2):
    """Build a read from ref[pos0:] of `length` sequenced bases with edits given
    in reference orientation: ('mm', off, base) substitutes the read base at
    read offset `off` (off counts read bases in reference orientation),
    ('N', off) puts an N there, ('ins', off, bases) inserts bases before read
    offset `off` (a reference gap), ('del', off, n) deletes n reference bases
    before read offset `off` (a read gap). `qual` is an int or a list per read
    base (reference orientation). Returns a dict with the FASTQ fields and the
    expected SAM fields for the intended alignment."""
    edits = sorted(edits, key=lambda e: e[1])
    ed = {}
    for e in edits:
        ed.setdefault(e[1], []).append(e)
    seq = []; cigar = []; md = []; mdrun = 0
    nm = xm = xo = xg = 0
    pen = 0; matches = 0
    r = pos0; i = 0
    def cig(op, n=1):
        if cigar and cigar[-1][1] == op:
            cigar[-1][0] += n
        else:
            cigar.append([n, op])
    quals = list(qual) if isinstance(qual, (list, tuple)) else [qual] * length
    while i < length:
        for e in ed.get(i, []):
            if e[0] == "ins":
                for b in e[2]:
                    seq.append(b); i += 1
                    if i > length: raise ValueError("insertion runs past read end")
                n = len(e[2]); cig("I", n); nm += n; xo += 1; xg += n
                pen += rfg[0] + rfg[1] * n
            elif e[0] == "del":
                n = e[2]
                md.append(f"{mdrun}^{ref[r:r + n]}"); mdrun = 0
                r += n; cig("D", n); nm += n; xo += 1; xg += n
                pen += rdg[0] + rdg[1] * n
        if i >= length:
            break
        base = ref[r]; sub = None
        for e in ed.get(i, []):
            if e[0] == "mm": sub = e[2]
            elif e[0] == "N": sub = "N"
        if sub is None or sub == base:
            seq.append(base); matches += 1; mdrun += 1
        else:
            seq.append(sub); md.append(f"{mdrun}{base}"); mdrun = 0
            nm += 1; xm += 1
            pen += npen if sub == "N" else mm_pen(quals[i], mm_max, mm_min)
        cig("M"); r += 1; i += 1
    md.append(str(mdrun))
    seq = "".join(seq)
    assert len(seq) == length, (len(seq), length)
    qstr = "".join(chr(q + 33) for q in quals)
    as_ = -pen if mode == "e2e" else ma * matches - pen
    out = dict(name=name, seq=seq if fw else revcomp(seq), qual=qstr if fw else qstr[::-1],
               pos=pos0 + 1, cigar="".join(f"{n}{op}" for n, op in cigar), md="".join(md),
               nm=nm, xm=xm, xo=xo, xg=xg, AS=as_, fw=fw, ref_extent=r - pos0)
    return out

def fq(rd):
    return (rd["name"], rd["seq"], rd["qual"])

def mate_pair(name, ref, frag0, fraglen, len1, len2, edits1=(), edits2=(), qual=40, orient="FR", mode="e2e", **kw):
    """A fragment ref[frag0:frag0+fraglen]; mate 1 is its first len1 bases,
    mate 2 the reverse complement of its last len2 bases (FR). 'RF' swaps the
    strands; 'FF' puts both forward. Returns (mate1, mate2) read dicts."""
    fw1, fw2 = {"FR": (True, False), "RF": (False, True), "FF": (True, True)}[orient]
    m1 = make_read(name, ref, frag0, len1, fw=fw1, edits=edits1, qual=qual, mode=mode, **kw)
    m2 = make_read(name, ref, frag0 + fraglen - len2, len2, fw=fw2, edits=edits2, qual=qual, mode=mode, **kw)
    return m1, m2

def report(label, ok, detail=""):
    print(f"{'ok  ' if ok else 'FAIL'} {label}{('  ' + detail) if detail else ''}")
    return ok
