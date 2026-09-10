#!/usr/bin/env python3
"""Independent Python references for Trimmomatic's trimming steps, plus helpers
to run a shipped Trimmomatic (jar or class directory) on synthetic FASTQ.

Two kinds of reference are provided for the steps whose documented rule and
coded rule can differ:

  *_doc(...)    the rule as the README ("Description of Trimming Steps" and
                "The Adapter Fasta") states it;
  *_coded(...)  a faithful port of the Java at usadellab/Trimmomatic main
                @ ef98d62 (2026-07-03), with switches for the individual
                heuristics so that each difference can be attributed.

Everything works on plain Python ints/floats; no Trimmomatic code is imported.
"""
import math, os, random, subprocess, sys, tempfile

LOG10_4 = 0.60206  # IlluminaClippingTrimmer.LOG10_4 (a float in Java)

# ----------------------------------------------------------------------------
# FASTQ helpers
# ----------------------------------------------------------------------------

def write_fastq(path, recs, offset=33):
    """recs: iterable of (name, seq, quals) with quals a list of ints."""
    with open(path, "w") as fh:
        for name, seq, quals in recs:
            fh.write("@%s\n%s\n+\n%s\n" % (name, seq, "".join(chr(q + offset) for q in quals)))


def read_fastq(path, offset=33):
    out = []
    with open(path) as fh:
        lines = fh.read().split("\n")
    i = 0
    while i + 3 < len(lines) or (i + 3 == len(lines) - 1 and lines[i]):
        if not lines[i]:
            break
        name = lines[i][1:]
        seq = lines[i + 1]
        qual = lines[i + 3]
        out.append((name, seq, [ord(c) - offset for c in qual]))
        i += 4
    return out


def rc(s):
    return s.translate(str.maketrans("ACGTN", "TGCAN"))[::-1]


# ----------------------------------------------------------------------------
# Runner
# ----------------------------------------------------------------------------

def launcher(target):
    """target: path to a jar, or a 'classes:lib' directory built from an old tag
    (a directory containing classes/ and lib/)."""
    if target.endswith(".jar"):
        return ["java", "-jar", target]
    cp = os.path.join(target, "classes") + ":" + os.path.join(target, "lib", "*")
    return ["java", "-cp", cp, "org.usadellab.trimmomatic.Trimmomatic"]


def run(target, mode, files, steps, opts=(), threads=1, workdir=None):
    """Run Trimmomatic SE/PE. files: input/output paths in command-line order.
    Returns (stderr+stdout text, returncode)."""
    env = dict(os.environ)
    env["JAVA_TOOL_OPTIONS"] = ""  # silence the sandbox's proxy banner
    cmd = launcher(target) + [mode, "-threads", str(threads)] + list(opts) + list(files) + list(steps)
    p = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=workdir)
    return p.stderr + p.stdout, p.returncode


def _phred_opts(opts, offset, autodetect):
    """Pass -phred33/-phred64 explicitly unless the caller wants auto-detection
    (constant-quality synthetic reads defeat the detector, see the review)."""
    opts = list(opts)
    if not autodetect and not any(o.startswith("-phred") for o in opts):
        opts = ["-phred%d" % offset] + opts
    return opts


def run_se(target, recs, steps, opts=(), threads=1, offset=33, tmpdir=None, autodetect=False):
    """Run SE mode on records; return (output records, log text)."""
    opts = _phred_opts(opts, offset, autodetect)
    d = tmpdir or tempfile.mkdtemp(prefix="trimmo_")
    inp = os.path.join(d, "in.fq"); outp = os.path.join(d, "out.fq")
    write_fastq(inp, recs, offset)
    log, rc_ = run(target, "SE", [inp, outp], steps, opts, threads, workdir=d)
    if rc_ != 0:
        raise RuntimeError("Trimmomatic failed:\n" + log)
    return read_fastq(outp, 33 if "TOPHRED33" in steps else (64 if "TOPHRED64" in steps else offset)), log


def run_pe(target, recs1, recs2, steps, opts=(), threads=1, offset=33, tmpdir=None, autodetect=False):
    """Run PE mode; return dict of the four outputs + log."""
    opts = _phred_opts(opts, offset, autodetect)
    d = tmpdir or tempfile.mkdtemp(prefix="trimmo_")
    in1 = os.path.join(d, "in1.fq"); in2 = os.path.join(d, "in2.fq")
    outs = [os.path.join(d, n) for n in ("1P.fq", "1U.fq", "2P.fq", "2U.fq")]
    write_fastq(in1, recs1, offset); write_fastq(in2, recs2, offset)
    log, rc_ = run(target, "PE", [in1, in2] + outs, steps, opts, threads, workdir=d)
    if rc_ != 0:
        raise RuntimeError("Trimmomatic failed:\n" + log)
    return {k: read_fastq(p, offset) for k, p in zip(("1P", "1U", "2P", "2U"), outs)}, log


# ----------------------------------------------------------------------------
# Quality handling as FastqRecord.getQualityAsInteger(true): N bases -> 0
# ----------------------------------------------------------------------------

def zero_ns(seq, quals):
    return [0 if b == "N" else q for b, q in zip(seq, quals)]


# ----------------------------------------------------------------------------
# Simple trimmers. Each returns (start, end) of the kept slice or None (dropped).
# ----------------------------------------------------------------------------

def sliding_window_coded(seq, quals, w, req):
    """SlidingWindowTrimmer.processRecord, as coded."""
    q = zero_ns(seq, quals)
    if len(q) < w:
        return None
    total_req = float(req) * w  # float in Java (float * int)
    total = sum(q[:w])
    if total < total_req:
        return None
    keep = len(q)
    for i in range(len(q) - w):
        total = total - q[i] + q[i + w]
        if total < total_req:
            keep = i + w
            break
    i = keep
    while q[i - 1] < req and i > 1:
        i -= 1
    if i < 1:
        return None
    return (0, i)


def sliding_window_doc(seq, quals, w, req):
    """README: 'cutting once the average quality within the window falls below a
    threshold' -- scan 5'->3', cut at the START of the first failing window."""
    q = zero_ns(seq, quals)
    for s in range(0, len(q) - w + 1):
        if sum(q[s:s + w]) / w < req:
            return None if s == 0 else (0, s)
    return (0, len(q))


def leading(seq, quals, thr):
    q = zero_ns(seq, quals)
    for i, v in enumerate(q):
        if v >= thr:
            return (i, len(q))
    return None


def trailing_coded(seq, quals, thr):
    """TrailingTrimmer: loop runs i = len-1 .. 1 (never checks base 0)."""
    q = zero_ns(seq, quals)
    for i in range(len(q) - 1, 0, -1):
        if q[i] >= thr:
            return (0, i + 1)
    return None


def trailing_doc(seq, quals, thr):
    q = zero_ns(seq, quals)
    for i in range(len(q) - 1, -1, -1):
        if q[i] >= thr:
            return (0, i + 1)
    return None


def maxinfo(seq, quals, target, strictness):
    """MaximumInformationTrimmer: score(L) = log sigmoid(L - target)
    + (1 - s) log L + s * sum_{i<L} log(1 - 10^-((q_i + 0.5)/10)); keep the
    longest L with the maximal score. Float arithmetic (the Java scales the
    tables to longs; ties can differ in the last ulp)."""
    q = zero_ns(seq, quals)
    best = -math.inf; best_pos = 0; acc = 0.0
    for i, v in enumerate(q):
        v = min(max(v, 0), 60)
        acc += math.log(1 - 10 ** (-(0.5 + v) / 10.0)) * strictness
        L = i + 1
        ls = math.log(1.0 / (1.0 + math.exp(target - L))) + math.log(L) * (1 - strictness)
        sc = ls + acc
        if sc >= best:
            best = sc; best_pos = L
    if best_pos < 1:
        return None
    return (0, best_pos)


def minlen(seq, quals, n):
    return (0, len(seq)) if len(seq) >= n else None


def maxlen(seq, quals, n):
    return (0, len(seq)) if len(seq) <= n else None


def crop(seq, quals, n):
    return (0, min(n, len(seq)))


def headcrop(seq, quals, n):
    return None if len(seq) <= n else (n, len(seq))


def tailcrop(seq, quals, n):
    return None if len(seq) <= n else (0, len(seq) - n)


def avgqual(seq, quals, thr):
    q = zero_ns(seq, quals)
    return (0, len(q)) if sum(q) >= thr * len(q) else None


def basecount(seq, quals, bases, lo=0, hi=None):
    c = sum(1 for b in seq if b in bases)
    if c < lo or (hi is not None and c > hi):
        return None
    return (0, len(seq))


# ----------------------------------------------------------------------------
# ILLUMINACLIP, simple mode
# ----------------------------------------------------------------------------

BASE = {"A": 0x1, "T": 0x2, "C": 0x4, "G": 0x8}
M64 = (1 << 64) - 1


def pack_ch(ch, rev=False):
    v = BASE.get(ch, 0)
    if rev and v:
        v = {0x1: 0x2, 0x2: 0x1, 0x4: 0x8, 0x8: 0x4}[v]
    return v


def pack_seq_external(seq):
    """packSeqExternal: out[i] = 16-mer starting at i, zero-padded past the end."""
    out = []
    pack = 0; off = 0
    for _ in range(15):
        tmp = pack_ch(seq[off]) if off < len(seq) else 0
        pack = ((pack << 4) | tmp) & M64; off += 1
    for i in range(len(seq)):
        tmp = pack_ch(seq[off]) if off < len(seq) else 0
        pack = ((pack << 4) | tmp) & M64
        out.append(pack); off += 1
    return out


def pack_seq_internal(seq, rev=False):
    out = []
    pack = 0
    for i, ch in enumerate(seq):
        tmp = pack_ch(ch, rev)
        if not rev:
            pack = ((pack << 4) | tmp) & M64
        else:
            pack = ((pack >> 4) | (tmp << 60)) & M64
        if i >= 15:
            out.append(pack)
    return out


def pack_prefix_and_seq(prefix, seq, rev):
    return pack_seq_internal(prefix + seq, rev)


def single_mask(length):
    mask = M64
    if length < 16:
        mask = (mask << ((16 - length) * 4)) & M64
    return mask


def popcount(x):
    return bin(x).count("1")


def diff_quality_simple(seq, quals, clip, overlap, rec_offset, use_maxrange=True):
    """calculateDifferenceQuality: per-base log-odds then calculateMaximumRange."""
    q = zero_ns(seq, quals)
    rec_pos = rec_offset if rec_offset > 0 else 0
    clip_pos = -rec_offset if rec_offset < 0 else 0
    vals = []
    for _ in range(overlap):
        c1 = seq[rec_pos]; c2 = clip[clip_pos]
        if c1 == "N" or c2 == "N":
            vals.append(0.0)
        elif c1 != c2:
            vals.append(-q[rec_pos] / 10.0)
        else:
            vals.append(LOG10_4)
        rec_pos += 1; clip_pos += 1
    return maximum_range(vals) if use_maxrange else sum(vals)


def maximum_range(vals):
    """Port of IlluminaClippingSeq.calculateMaximumRange (a run-merging heuristic)."""
    merges = []
    total = 0.0
    for v in vals:
        if (total > 0 and v < 0) or (total < 0 and v > 0):
            merges.append(total); total = v
        else:
            total += v
    merges.append(total)
    scan = True
    while merges and scan:
        scan = False
        i = 0
        while i < len(merges):
            val = merges[i]
            if val < 0 and i > 0 and i + 1 < len(merges):
                prev, nxt = merges[i - 1], merges[i + 1]
                if prev > -val and nxt > -val:
                    merges[i - 1:i + 2] = [prev + val + nxt]
                    scan = True
                    i = i - 1
                    continue
            i += 1
    return max([0.0] + merges)


class ClipSeq:
    """One non-prefix adapter; the class (short/medium/long) follows the length."""

    def __init__(self, name, seq):
        self.name = name; self.seq = seq
        n = len(seq)
        self.kind = "short" if n < 16 else ("medium" if n < 24 else "long")
        if self.kind == "short":
            self.mask = single_mask(n); self.pack = pack_seq_external(seq)
        elif self.kind == "medium":
            self.pack = pack_seq_internal(seq)
        else:
            full = pack_seq_internal(seq)
            self.pack = [full[i] for i in range(0, len(full), 4)]

    def compare_coded(self, seq, quals, seed_max_miss, min_lik, min_overlap,
                      use_seeds=True, use_maxrange=True):
        """readsSeqCompare: returns the clip offset (bases to keep) or None."""
        seed_max = seed_max_miss * 2
        pack_rec = pack_seq_external(seq)
        offsets = set()
        if use_seeds:
            rec_max = len(pack_rec) - min_overlap
            if self.kind == "short":
                clip_max = len(self.pack) - min_overlap
                for i in range(rec_max):
                    combo = single_mask(len(pack_rec) - i) & self.mask
                    for j in range(clip_max):
                        if popcount((pack_rec[i] ^ self.pack[j]) & combo) <= seed_max:
                            offsets.add(i - j)
            else:
                mult = 4 if self.kind == "long" else 1
                for i in range(rec_max):
                    combo = single_mask(len(pack_rec) - i)
                    for j in range(len(self.pack)):
                        if popcount((pack_rec[i] ^ self.pack[j]) & combo) <= seed_max:
                            offsets.add(i - j * mult)
        else:
            offsets = set(range(-(len(self.seq) - 1), len(seq)))
        for off in sorted(offsets):
            rec_len = len(seq) - off if off > 0 else len(seq)
            clip_len = len(self.seq) + off if off < 0 else len(self.seq)
            comp = min(rec_len, clip_len)
            if comp > min_overlap:
                lik = diff_quality_simple(seq, quals, self.seq, comp, off, use_maxrange)
                if lik >= min_lik:
                    return off
        return None


def min_sequence_overlap(min_lik):
    v = int(min_lik / LOG10_4)
    return min(v, 15)


def simple_clip_doc(seq, quals, adapters, min_lik):
    """README: each adapter is tested against the read; score = sum of +0.6 per
    match and -Q/10 per mismatch (0 for N) over the aligned bases; if a
    sufficiently accurate match (>= threshold) is found the read is clipped at
    the adapter start. Smallest passing offset wins; offsets <= 0 drop the read."""
    best = None
    for name, ad in adapters:
        for off in range(-(len(ad) - 1), len(seq)):
            rec_len = len(seq) - off if off > 0 else len(seq)
            clip_len = len(ad) + off if off < 0 else len(ad)
            comp = min(rec_len, clip_len)
            if comp <= 0:
                continue
            lik = diff_quality_simple(seq, quals, ad, comp, off, use_maxrange=False)
            if lik >= min_lik:
                best = off if best is None else min(best, off)
                break
    return best


# ----------------------------------------------------------------------------
# ILLUMINACLIP, palindrome mode
# ----------------------------------------------------------------------------

def comp_ch(ch):
    return {"A": "T", "C": "G", "G": "C", "T": "A"}.get(ch, "N")


def palindrome_score(seq1, q1, seq2, q2, p1, p2, T, int_division):
    """calculatePalindromeDifferenceQuality for total overlap T (insert + 2*prefix):
    A = p1+seq1 aligned against the reverse complement of C = p2+seq2, both taken
    from their first T bases; positions past either end are skipped."""
    q1 = zero_ns(seq1, q1); q2 = zero_ns(seq2, q2)
    p = len(p1)
    len1 = len(seq1) + p; len2 = len(seq2) + p
    skip1 = T - len2 if T > len2 else 0
    skip2 = T - len1 if T > len1 else 0
    overlap = T - skip1 - skip2
    total = 0.0
    for i in range(overlap):
        o1 = i + skip1
        o2 = skip2 + overlap - i - 1
        c1 = p1[o1] if o1 < p else seq1[o1 - p]
        c2 = p2[o2] if o2 < p else seq2[o2 - p]
        c2 = comp_ch(c2)
        qa = 100 if o1 < p else q1[o1 - p]
        qb = 100 if o2 < p else q2[o2 - p]
        if c1 == "N" or c2 == "N":
            v = 0.0
        elif c1 != c2:
            qm = qa if qa < qb else qb
            v = float(-(qm // 10)) if int_division else -qm / 10.0
        else:
            v = LOG10_4
        total += v
    return total, overlap


def palindrome_coded(seq1, q1, seq2, q2, p1, p2, seed_max_miss, min_lik, min_prefix,
                     int_division=True, use_seeds=True):
    """IlluminaPrefixPair.palindromeReadsCompare. Returns the insert length to keep
    (may be <= 0, meaning drop) or None."""
    # prefixes are right-aligned to equal length in the constructor
    m = min(len(p1), len(p2))
    p1 = p1[len(p1) - m:]; p2 = p2[len(p2) - m:]
    seed_max = seed_max_miss * 2
    pack1 = pack_prefix_and_seq(p1, seq1, False)
    pack2 = pack_prefix_and_seq(p2, seq2, True)
    p = len(p1)
    test = 0; ref = p
    if len(pack1) <= ref or len(pack2) <= ref:
        return None
    count = 0
    seed_skip = p - 16
    if seed_skip > 0:
        test = seed_skip; count = seed_skip
    len1 = len(seq1) + p; len2 = len(seq2) + p
    max_count = max(len1, len2) - 15 - min_prefix
    while count < max_count:
        r1 = pack1[ref]; r2 = pack2[ref]
        hit = ((test < len(pack2) and popcount(r1 ^ pack2[test]) <= seed_max)
               or (test < len(pack1) and popcount(r2 ^ pack1[test]) <= seed_max))
        if not use_seeds:
            hit = True
        if hit:
            T = count + p + 16
            lik, _ = palindrome_score(seq1, q1, seq2, q2, p1, p2, T, int_division)
            if lik >= min_lik:
                return T - 2 * p
        count += 1
        tr = ref + 1
        if (count & 1) == 0 and tr < len(pack1) and tr < len(pack2):
            ref += 1
        else:
            test += 1
    return None


def palindrome_doc(seq1, q1, seq2, q2, p1, p2, min_lik, min_prefix):
    """README: ligate the prefixes in silico, align forward against reverse for
    every read-through geometry (insert length L from 0 up to readlen - minAdapterLength);
    score = +0.6 per match, -Q/10 per mismatch, 0 for N; the first L reaching the
    threshold clips the forward read to L and drops the reverse read."""
    m = min(len(p1), len(p2))
    p1 = p1[len(p1) - m:]; p2 = p2[len(p2) - m:]
    p = len(p1)
    n = max(len(seq1), len(seq2))
    for L in range(0, n - min_prefix + 1):
        T = L + 2 * p
        lik, overlap = palindrome_score(seq1, q1, seq2, q2, p1, p2, T, int_division=False)
        if overlap <= 0:
            continue
        if lik >= min_lik:
            return L
    return None


# ----------------------------------------------------------------------------
# Whole ILLUMINACLIP step (as coded), on a pair or a single read
# ----------------------------------------------------------------------------

class IlluminaClip:
    def __init__(self, fasta_path, seed_mm, pal_thr, simple_thr, min_prefix=8, keep_both=False):
        self.seed_mm = seed_mm; self.pal_thr = pal_thr; self.simple_thr = simple_thr
        self.min_prefix = min_prefix; self.keep_both = keep_both
        self.min_overlap = min_sequence_overlap(simple_thr)
        recs = read_fasta(fasta_path)
        fwd, rev, common = {}, {}, {}
        fpre, rpre = set(), set()
        for name, seq in recs:
            if name.endswith("/1"):
                fwd[name] = seq
                if name.startswith("Prefix"):
                    fpre.add(name[:-2])
            elif name.endswith("/2"):
                rev[name] = seq
                if name.startswith("Prefix"):
                    rpre.add(name[:-2])
            else:
                common[name] = seq
        self.pairs = []
        for pre in sorted(fpre & rpre):
            self.pairs.append((pre, fwd.pop(pre + "/1"), rev.pop(pre + "/2")))
        self.fwd = self._clipset(fwd); self.rev = self._clipset(rev); self.common = self._clipset(common)

    @staticmethod
    def _clipset(d):
        seen, out = set(), []
        for name, seq in d.items():
            if seq in seen:
                continue
            seen.add(seq); out.append(ClipSeq(name, seq))
        return out

    def _simple_min(self, seq, quals, sets, **kw):
        best = None
        for s in sets:
            for cs in s:
                r = cs.compare_coded(seq, quals, self.seed_mm, self.simple_thr, self.min_overlap, **kw)
                if r is not None and (best is None or r < best):
                    best = r
        return best

    def process(self, r1, r2=None, int_division=True, use_seeds=True, use_maxrange=True):
        """r1, r2: (seq, quals) or None. Returns (keep1, keep2): bases kept from the
        start, or None for dropped. Mirrors IlluminaClippingTrimmer.processRecords."""
        keep1 = keep2 = None
        if r1 is not None and r2 is not None:
            for pre, p1, p2 in self.pairs:
                tk = palindrome_coded(r1[0], r1[1], r2[0], r2[1], p1, p2, self.seed_mm, self.pal_thr,
                                      self.min_prefix, int_division, use_seeds)
                if tk is not None:
                    keep1 = tk if keep1 is None else min(keep1, tk)
                    keep2 = (tk if keep2 is None else min(keep2, tk)) if self.keep_both else 0
        out1 = out2 = None
        if r1 is not None:
            if keep1 is None or keep1 > 0:
                s = self._simple_min(r1[0], r1[1], (self.fwd, self.common), use_seeds=use_seeds, use_maxrange=use_maxrange)
                if s is not None:
                    keep1 = s if keep1 is None else min(keep1, s)
            out1 = len(r1[0]) if keep1 is None else (keep1 if keep1 > 0 else None)
        if r2 is not None:
            if keep2 is None or keep2 > 0:
                s = self._simple_min(r2[0], r2[1], (self.rev, self.common), use_seeds=use_seeds, use_maxrange=use_maxrange)
                if s is not None:
                    keep2 = s if keep2 is None else min(keep2, s)
            out2 = len(r2[0]) if keep2 is None else (keep2 if keep2 > 0 else None)
        return out1, out2


def read_fasta(path):
    out = []; name = None; seq = []
    for line in open(path):
        line = line.rstrip("\n")
        if line.startswith(">"):
            if name is not None:
                out.append((name, "".join(seq)))
            name = line[1:].strip().split("|")[0].split(" ")[0]; seq = []
        elif line and not line.startswith(";"):
            seq.append(line.strip())
    if name is not None:
        out.append((name, "".join(seq)))
    return out


# ----------------------------------------------------------------------------
# Synthetic data
# ----------------------------------------------------------------------------

def rand_seq(rng, n):
    return "".join(rng.choice("ACGT") for _ in range(n))


def mutate(rng, s, rate, allow_n=0.0):
    out = []
    for c in s:
        u = rng.random()
        if u < allow_n:
            out.append("N")
        elif u < allow_n + rate:
            out.append(rng.choice([b for b in "ACGT" if b != c]))
        else:
            out.append(c)
    return "".join(out)


def rand_quals(rng, n, profile="mixed"):
    """Quality profiles. 'mixed': a 5' plateau (Q28-41) and a decaying tail where
    Q2-Q15 bases are common, as in late-cycle Illumina data."""
    if profile == "high":
        return [rng.randint(30, 41) for _ in range(n)]
    if profile == "uniform":
        return [rng.randint(2, 41) for _ in range(n)]
    out = []
    for i in range(n):
        f = i / max(1, n - 1)
        if rng.random() < 0.15 + 0.6 * f * f:
            out.append(rng.randint(2, 19))
        else:
            out.append(rng.randint(20, 41))
    return out
