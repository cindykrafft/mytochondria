#!/usr/bin/env python3
"""Independent Python references for Trimmomatic's trimming steps, written from the
manual (README.md "Description of Trimming Steps" / "The Adapter Fasta") and, where the
manual gives no formula, from the algorithm as stated in the code comments; plus helpers
that run a Trimmomatic build on synthetic FASTQ and read back its outputs.

Two flavours are provided where they differ:
  *_doc   the documented rule (the statement of intended behaviour)
  *_code  a faithful port of the shipped arithmetic (used to attribute discrepancies)

A "build" is a list of command-line words that starts the Trimmomatic main class, e.g.
  ["java", "-jar", "trimmomatic-0.39.jar"]  or
  ["java", "-cp", "classes:lib/*", "org.usadellab.trimmomatic.Trimmomatic"].
"""
import math, os, random, subprocess, sys, tempfile

LOG10_4 = 0.60206          # the constant the code uses (float32 in Java)
ENV = dict(os.environ, JAVA_TOOL_OPTIONS="")   # silence the session's proxy banner
COMP = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}

def revcomp(s): return "".join(COMP[c] for c in reversed(s))
def rand_seq(rng, n): return "".join(rng.choice("ACGT") for _ in range(n))
def q2c(q, off=33): return chr(q + off)
def qs2str(qs, off=33): return "".join(chr(q + off) for q in qs)
def str2qs(s, off=33): return [ord(c) - off for c in s]

def mutate(rng, base): return rng.choice([b for b in "ACGT" if b != base])

# ----------------------------------------------------------------- build discovery
def build_from_arg(arg):
    """'path.jar' -> java -jar; 'dir' containing classes/ and lib/ -> classpath run."""
    if arg.endswith(".jar"):
        return ["java", "-jar", arg]
    cp = os.path.join(arg, "classes") + ":" + os.path.join(arg, "lib", "*")
    return ["java", "-cp", cp, "org.usadellab.trimmomatic.Trimmomatic"]

# ----------------------------------------------------------------- FASTQ helpers
def write_fastq(path, reads, off=33):
    """reads: list of (name, seq, quals[list of int])"""
    with open(path, "w") as fh:
        for name, seq, quals in reads:
            fh.write("@%s\n%s\n+\n%s\n" % (name, seq, qs2str(quals, off)))

def read_fastq(path, off=33):
    out = {}
    if not os.path.exists(path):
        return out
    with open(path) as fh:
        lines = fh.read().split("\n")
    i = 0
    while i + 3 < len(lines) and lines[i]:
        name = lines[i][1:].split()[0]
        out[name] = (lines[i + 1], str2qs(lines[i + 3], off))
        i += 4
    return out

def run_se(build, reads, steps, extra=(), off=33, workdir=None, keep=False):
    """Run SE mode; returns (dict name->(seq, quals), stderr+stdout text, workdir)."""
    d = workdir or tempfile.mkdtemp(prefix="tm_se_")
    inp, outp = os.path.join(d, "in.fq"), os.path.join(d, "out.fq")
    write_fastq(inp, reads, off)
    phred = ["-phred33"] if off == 33 else ["-phred64"]
    if off == 0:
        phred = []
    cmd = list(build) + ["SE", "-threads", "1"] + phred + list(extra) + [inp, outp] + list(steps)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=d)
    log = p.stdout + p.stderr
    res = read_fastq(outp, off if off else 33)
    return res, log, d

def run_pe(build, reads1, reads2, steps, extra=(), off=33, workdir=None):
    """Run PE mode; returns (dict of 4 outputs {'1P','1U','2P','2U'} -> {name: (seq, quals)}, log, dir)."""
    d = workdir or tempfile.mkdtemp(prefix="tm_pe_")
    in1, in2 = os.path.join(d, "in1.fq"), os.path.join(d, "in2.fq")
    write_fastq(in1, reads1, off); write_fastq(in2, reads2, off)
    outs = {k: os.path.join(d, "out_%s.fq" % k) for k in ("1P", "1U", "2P", "2U")}
    phred = ["-phred33"] if off == 33 else (["-phred64"] if off == 64 else [])
    cmd = list(build) + ["PE", "-threads", "1"] + phred + list(extra) + [in1, in2,
           outs["1P"], outs["1U"], outs["2P"], outs["2U"]] + list(steps)
    p = subprocess.run(cmd, capture_output=True, text=True, env=ENV, cwd=d)
    log = p.stdout + p.stderr
    res = {k: read_fastq(v, off if off else 33) for k, v in outs.items()}
    return res, log, d

def summary_line(log, pe=False):
    key = "Input Read Pairs:" if pe else "Input Reads:"
    for line in log.splitlines():
        if line.startswith(key):
            return line.strip()
    return None

# ----------------------------------------------------------------- simple trimmers (documented)
def zero_n(seq, quals):
    """Trimmomatic scores an N base as quality 0 in every quality-based step (code: getQualityAsInteger(true))."""
    return [0 if b == "N" else q for b, q in zip(seq, quals)]

def leading(seq, quals, thr):
    q = zero_n(seq, quals)
    for i in range(len(seq)):
        if q[i] >= thr:
            return seq[i:], quals[i:]
    return None

def trailing_doc(seq, quals, thr):
    """Cut bases off the end of a read if below the threshold quality: keep up to and including
    the last base with quality >= thr; drop the read if no base qualifies."""
    q = zero_n(seq, quals)
    for i in range(len(seq) - 1, -1, -1):
        if q[i] >= thr:
            return seq[:i + 1], quals[:i + 1]
    return None

def trailing_code(seq, quals, thr):
    """As shipped: the loop stops at index 1, so a read whose only qualifying base is the first
    one is dropped instead of kept as a 1-base read."""
    q = zero_n(seq, quals)
    for i in range(len(seq) - 1, 0, -1):
        if q[i] >= thr:
            return seq[:i + 1], quals[:i + 1]
    return None

def crop(seq, quals, n): return seq[:n], quals[:n]
def headcrop(seq, quals, n):
    if len(seq) <= n: return None
    return seq[n:], quals[n:]
def tailcrop(seq, quals, n):
    if len(seq) <= n: return None
    return seq[:len(seq) - n], quals[:len(seq) - n]
def minlen(seq, quals, n): return (seq, quals) if len(seq) >= n else None
def maxlen(seq, quals, n): return (seq, quals) if len(seq) <= n else None
def avgqual(seq, quals, thr):
    q = zero_n(seq, quals)
    return (seq, quals) if (len(q) == 0 or sum(q) / len(q) >= thr) else None
def basecount(seq, quals, bases, mn=0, mx=None):
    c = sum(1 for b in seq if b in bases)
    if c < mn: return None
    if mx is not None and c > mx: return None
    return seq, quals

def sliding_window_doc(seq, quals, w, req):
    """Documented: scan from the 5' end and clip once the average quality within the window
    falls below the threshold. Read as: keep everything before the first failing window
    (i.e. up to the end of the last passing window), then also remove trailing bases whose
    own quality is below the threshold (the code's 'backtrack'; the versionHistory 0.30 entry
    calls the alternative 'half-window clipping'). Reads shorter than the window are handled
    by the caller's convention; here they are compared as coded (dropped)."""
    q = zero_n(seq, quals)
    n = len(q)
    if n < w:
        return None
    keep = n
    for i in range(0, n - w + 1):
        if sum(q[i:i + w]) / w < req:
            keep = i + w - 1 if i > 0 else 0   # end of the last passing window
            break
    if keep == 0:
        return None
    while keep > 1 and q[keep - 1] < req:
        keep -= 1
    if keep < 1:
        return None
    return seq[:keep], quals[:keep]

def sliding_window_code(seq, quals, w, req):
    """Faithful port of SlidingWindowTrimmer.processRecord (integer sums vs float total)."""
    q = zero_n(seq, quals)
    if len(q) < w:
        return None
    total_req = req * w
    total = sum(q[:w])
    if total < total_req:
        return None
    keep = len(q)
    for i in range(0, len(q) - w):
        total = total - q[i] + q[i + w]
        if total < total_req:
            keep = i + w
            break
    i = keep
    last = q[i - 1]
    while last < req and i > 1:
        i -= 1
        last = q[i - 1]
    if i < 1:
        return None
    return seq[:i], quals[:i]

def maxinfo_double(seq, quals, target, strictness, plus_half=True):
    """MAXINFO scoring in double precision, from the formulas stated in the code comments
    (Bolger et al. 2014, 'maximum information' trimming): score(L) = log[1/(1+e^{target-L})]
    + (1-s)·log L + s·Σ_{k<L} log(1 - 10^{-(q_k+0.5)/10}), maximised over L (ties -> longest)."""
    q = zero_n(seq, quals)
    best, best_len, acc = -math.inf, 0, 0.0
    for i, qi in enumerate(q):
        qi = min(max(qi, 0), 60)
        p = (qi + 0.5) / 10.0 if plus_half else qi / 10.0
        acc += math.log(1 - 10 ** (-p)) * strictness
        x = target - i - 1
        unique = -math.log1p(math.exp(x)) if x < 700 else -x   # log(1/(1+e^x)), overflow-safe
        ls = unique + math.log(i + 1) * (1 - strictness)
        s = ls + acc
        if s >= best:
            best, best_len = s, i + 1
    if best_len < 1:
        return None
    return seq[:best_len], quals[:best_len]

def tophred(seq, quals, cur, new):
    return seq, quals   # integer qualities are encoding-free; the runner applies the offset

# ----------------------------------------------------------------- ILLUMINACLIP references
def seed_ok(a, b, seed_mm, ns_half=True):
    """Does some aligned 16-mer of the two equal-length strings differ in <= seed_mm bases?
    (Trimmomatic packs bases one-hot, so an N against a base costs half a mismatch.)"""
    n = len(a)
    for i in range(0, n - 15):
        d = 0.0
        for k in range(i, i + 16):
            if a[k] == "N" or b[k] == "N":
                if a[k] != b[k]:
                    d += 0.5
            elif a[k] != b[k]:
                d += 1
        if d <= seed_mm:
            return True
    return False

def score_doc(pairs):
    """pairs: iterable of (base1, base2, q): +LOG10_4 per match, -q/10 per mismatch, 0 with an N."""
    s = 0.0
    for a, b, q in pairs:
        if a == "N" or b == "N":
            continue
        s += LOG10_4 if a == b else -q / 10.0
    return s

def max_range_code(vals):
    """Port of IlluminaClippingSeq.calculateMaximumRange: greedy merge of same-sign runs."""
    merges, total = [], 0.0
    for v in vals:
        if (total > 0 and v < 0) or (total < 0 and v > 0):
            merges.append(total); total = v
        else:
            total += v
    merges.append(total)
    again = True
    while merges and again:
        again = False
        i = 0
        while i < len(merges):
            v = merges[i]
            if v < 0 and i > 0 and i + 1 < len(merges):
                prev, nxt = merges[i - 1], merges[i + 1]
                if prev > -v and nxt > -v:
                    merges[i - 1:i + 2] = [prev + v + nxt]
                    again = True
                    i = i - 1
                    continue
            i += 1
    return max([0.0] + merges)

def simple_clip(seq, quals, adapter, seed_mm, thr, mode="doc", min_overlap=None):
    """Simple-mode ILLUMINACLIP for one adapter (documented rule): slide the adapter over the
    read (adapter may overhang the 3' end), score the overlap, clip at the first (leftmost)
    offset whose score >= thr and whose overlap has a qualifying 16-mer seed.
    mode='doc'  : score = sum over the whole overlap
    mode='code' : score = best sub-range (port of calculateMaximumRange)
    Returns the number of bases to keep, or None. 0 means the read is dropped.
    min_overlap: the code's minimum overlap (int(thr/0.60206), capped at 15) + 1; when given,
    shorter overlaps are not considered (documented indirectly: score of a k-base perfect
    match is 0.6k, so k < thr/0.6 can never pass)."""
    q = zero_n(seq, quals)
    n, m = len(seq), len(adapter)
    hits = []
    for off in range(-(m - 1), n):
        lo, hi = max(0, off), min(n, off + m)
        ov = hi - lo
        if ov <= 0:
            continue
        if min_overlap is not None and ov <= min_overlap:
            continue
        a = seq[lo:hi]; b = adapter[lo - off:hi - off]; qq = q[lo:hi]
        if ov >= 16 and not seed_ok(a, b, seed_mm):
            continue
        if ov < 16:
            # a seed shorter than 16 bases: compare the whole overlap
            d = sum(1 for x, y in zip(a, b) if x != y and "N" not in (x, y))
            if d > seed_mm:
                continue
        vals = [0.0 if "N" in (x, y) else (LOG10_4 if x == y else -qi / 10.0) for x, y, qi in zip(a, b, qq)]
        s = sum(vals) if mode == "doc" else max_range_code(vals)
        if s >= thr:
            hits.append(off)
    if not hits:
        return None
    return max(min(hits), 0)

def code_min_overlap(thr):
    mo = int(thr / LOG10_4)
    return min(mo, 15)

def palindrome_score(read1, q1, read2, q2, prefix1, prefix2, insert, penalty="doc"):
    """Score of the palindrome alignment of prefix1+read1 against revcomp(prefix2+read2)
    under the hypothesis that the insert has length `insert`. Adapter (prefix) bases carry
    quality 100 (as coded); a mismatch costs min(q1, q2)/10 ('doc', the manual's Q/10) or
    int(min(q1,q2)/10) ('code', the shipped integer division). Returns (score, n_aligned)."""
    P = len(prefix1)
    assert len(prefix2) == P
    s1 = prefix1 + read1; qq1 = [100] * P + zero_n(read1, q1)
    s2 = prefix2 + read2; qq2 = [100] * P + zero_n(read2, q2)
    F = insert + 2 * P
    score, n = 0.0, 0
    for j in range(F):
        m = F - 1 - j
        if j >= len(s1) or m >= len(s2):
            continue
        a, b = s1[j], COMP[s2[m]]
        qa, qb = qq1[j], qq2[m]
        n += 1
        if a == "N" or b == "N":
            continue
        if a == b:
            score += LOG10_4
        else:
            qm = min(qa, qb)
            score += -(qm // 10) if penalty == "code" else -qm / 10.0
    return score, n

def palindrome_clip(read1, q1, read2, q2, prefix1, prefix2, seed_mm, thr, min_adapter=8,
                    penalty="doc"):
    """Documented palindrome mode: the smallest insert length whose ligated-fragment alignment
    scores >= thr (and has a clean 16-mer seed somewhere in the aligned region); None if none."""
    R = min(len(read1), len(read2))
    P = len(prefix1)
    for L in range(0, R - min_adapter + 1):
        s, n = palindrome_score(read1, q1, read2, q2, prefix1, prefix2, L, penalty)
        if n < 16:
            continue
        # seed: aligned region as two strings
        s1 = prefix1 + read1; s2 = prefix2 + read2; F = L + 2 * P
        a = "".join(s1[j] for j in range(F) if j < len(s1) and F - 1 - j < len(s2))
        b = "".join(COMP[s2[F - 1 - j]] for j in range(F) if j < len(s1) and F - 1 - j < len(s2))
        if not seed_ok(a, b, seed_mm):
            continue
        if s >= thr:
            return L
    return None

def load_fasta(path):
    recs, name, buf = [], None, []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line: continue
            if line.startswith(">"):
                if name is not None: recs.append((name, "".join(buf)))
                name, buf = line[1:], []
            else:
                buf.append(line)
    if name is not None: recs.append((name, "".join(buf)))
    return recs
