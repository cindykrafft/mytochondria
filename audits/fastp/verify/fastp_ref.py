"""Independent Python ports of the fastp per-read trimming rules, plus helpers.

Shared by the harnesses in this directory. Every port is written from
`src/filter.cpp`, `src/polyx.cpp` and `README.md` of `OpenGene/fastp` @ dce5c40
and is deliberately independent of the C++ code (no shared arithmetic).

Two variants of the sliding-window cutter are provided:

  variant="shipped"  what the C++ does today, including `if(s > 0)` /
                     `if(t < l-1)` (filter.cpp:121, :189);
  variant="fixed"    the same with the two boundary tests written against the
                     globally trimmed ends (`s > front`, `t < l-tail-1`).

They differ only when --trim_front1/--trim_tail1 is non-zero (FP1).
"""
import os
import subprocess
import tempfile


# ---------------------------------------------------------------- fastq utils
def write_fastq(path, records):
    with open(path, "w") as fh:
        for name, seq, qual in records:
            fh.write(f"@{name}\n{seq}\n+\n{qual}\n")


def read_fastq(path):
    out = {}
    with open(path) as fh:
        lines = fh.read().splitlines()
    for i in range(0, len(lines), 4):
        out[lines[i][1:].split()[0]] = (lines[i + 1], lines[i + 3])
    return out


def run_fastp(exe, args, records=None, in_path=None, out=True, extra_files=()):
    """Run the fastp binary on `records`; return (dict of output reads, stderr, json path)."""
    tmp = tempfile.mkdtemp()
    if in_path is None:
        in_path = os.path.join(tmp, "in.fq")
        write_fastq(in_path, records)
    out_path = os.path.join(tmp, "out.fq")
    json_path = os.path.join(tmp, "out.json")
    cmd = [exe, "-i", in_path, "-j", json_path, "-h", os.path.join(tmp, "out.html")]
    if out:
        cmd += ["-o", out_path]
    cmd += list(args)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    reads = read_fastq(out_path) if (out and os.path.exists(out_path)) else {}
    return reads, proc.stderr, json_path


# ------------------------------------------------------- filter.cpp trimAndCut
class CutOpts:
    def __init__(self, front=False, tail=False, right=False, w=4, q=20,
                 wf=None, qf=None, wt=None, qt=None, wr=None, qr=None):
        self.front, self.tail, self.right = front, tail, right
        self.wf, self.qf = (w if wf is None else wf), (q if qf is None else qf)
        self.wt, self.qt = (w if wt is None else wt), (q if qt is None else qt)
        self.wr, self.qr = (w if wr is None else wr), (q if qr is None else qr)

    @property
    def any(self):
        return self.front or self.tail or self.right


def trim_and_cut(seq, qual, front, tail, o: CutOpts, variant="shipped"):
    """Port of Filter::trimAndCut (filter.cpp:99-238). Returns (seq, qual) or None."""
    q = [ord(c) for c in qual]
    l = len(seq)
    if front == 0 and tail == 0 and not o.any:
        return seq, qual
    rlen = l - front - tail
    if rlen < 0:
        return None
    if front == 0 and not o.any:
        return seq[:rlen], qual[:rlen]
    if not o.any:
        return seq[front:front + rlen], qual[front:front + rlen]

    if o.front:
        w = o.wf
        if l - front - tail - w <= 0:
            return None
        total = sum(q[front + i] for i in range(w - 1))
        s = front
        while s + w < l - tail:
            total += q[s + w - 1]
            if s > front:
                total -= q[s - 1]
            if total >= w * (33 + o.qf):
                break
            s += 1
        boundary = (s > 0) if variant == "shipped" else (s > front)
        if boundary:
            s = s + w - 1
        while s < l and seq[s] == "N":
            s += 1
        front = s
        rlen = l - front - tail

    if o.right:
        w = o.wr
        if l - front - tail - w <= 0:
            return None
        total = sum(q[front + i] for i in range(w - 1))
        s = front
        found = False
        while s + w < l - tail:
            total += q[s + w - 1]
            if s > front:
                total -= q[s - 1]
            if total < w * (33 + o.qr):
                found = True
                break
            s += 1
        if found:
            while s < l - 1 and q[s] >= 33 + o.qr:
                s += 1
            rlen = s - front

    if (not o.right) and o.tail:
        w = o.wt
        if l - front - tail - w <= 0:
            return None
        total = sum(q[l - tail - 1 - i] for i in range(w - 1))
        t = l - tail - 1
        while t - w >= front:
            total += q[t - w + 1]
            if t < l - tail - 1:
                total -= q[t + 1]
            if total >= w * (33 + o.qt):
                break
            t -= 1
        boundary = (t < l - 1) if variant == "shipped" else (t < l - tail - 1)
        if boundary:
            t = t - w + 1
        while t >= 0 and seq[t] == "N":
            t -= 1
        rlen = t - front + 1

    if rlen <= 0 or front >= l - 1:
        return None
    return seq[front:front + rlen], qual[front:front + rlen]


# ------------------------------------------------------------ polyx.cpp ports
def trim_poly_g(seq, compare_req=10):
    """Port of PolyX::trimPolyG (polyx.cpp:11-38). Returns the trimmed sequence."""
    rlen = len(seq)
    mismatch = 0
    first_g = rlen - 1
    i = 0
    while i < rlen:
        if seq[rlen - i - 1] != "G":
            mismatch += 1
        else:
            first_g = rlen - i - 1
        allowed = (i + 1) // 8
        if mismatch > 5 or (mismatch > allowed and i >= compare_req - 1):
            break
        i += 1
    if i >= compare_req:
        return seq[:first_g]
    return seq


def trim_poly_x(seq, compare_req=10):
    """Port of PolyX::trimPolyX (polyx.cpp:39-117). Returns the trimmed sequence."""
    rlen = len(seq)
    idx = {"A": 0, "T": 1, "C": 2, "G": 3}
    counts = [0, 0, 0, 0]
    pos = 0
    while pos < rlen:
        b = seq[rlen - pos - 1]
        if b in idx:
            counts[idx[b]] += 1
        elif b == "N":
            for k in range(4):
                counts[k] += 1
        cmp_ = pos + 1
        allowed = min(5, cmp_ // 8)
        need_break = all(cmp_ - counts[b] > allowed for b in range(4))
        if need_break and (pos >= 8 or pos + 1 >= compare_req - 1):
            break
        pos += 1
    if pos + 1 >= compare_req:
        poly = max(range(4), key=lambda b: (counts[b], -b))
        base = "ATCG"[poly]
        while pos >= 0 and (rlen - pos - 1 >= rlen or seq[rlen - pos - 1] != base):
            pos -= 1
            if pos < 0:
                break
        return seq[:rlen - pos - 1]
    return seq


# --------------------------------------------------------------- filter rules
def pass_filter(seq, qual, qualified_q=15, unqualified_pct=40, n_limit=5,
                avg_qual=0, min_len=15, max_len=0, complexity=None,
                qual_filter=True, len_filter=True):
    """Port of Filter::passFilter (filter.cpp:46-88). Returns a reason string."""
    if seq is None or len(seq) == 0:
        return "too_short"
    rlen = len(seq)
    low = sum(1 for c in qual if ord(c) < 33 + qualified_q)
    nb = seq.count("N")
    total_q = sum(ord(c) - 33 for c in qual)
    if qual_filter:
        if low > unqualified_pct * rlen / 100.0:
            return "low_quality"
        if avg_qual > 0 and (total_q // rlen) < avg_qual:
            return "low_quality"
        if nb > n_limit:
            return "too_many_N"
    if len_filter:
        if rlen < min_len:
            return "too_short"
        if max_len > 0 and rlen > max_len:
            return "too_long"
    if complexity is not None:
        if rlen <= 1:
            return "low_complexity"
        diff = sum(1 for i in range(rlen - 1) if seq[i] != seq[i + 1])
        if diff / (rlen - 1) < complexity:
            return "low_complexity"
    return "pass"
