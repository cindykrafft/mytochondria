"""Shared helpers for the BWA audit harnesses.

Everything that serves as "truth" here is computed independently of BWA:
reads are cut from a random reference with planted edits, so positions,
fragment lengths and edit operations are known; NM/MD are recomputed from
the read, the reference and the reported CIGAR; scores are recomputed from
the documented scoring scheme (bwa.1: -A1 -B4 -O6 -E1 -L5, a gap of length k
costs O + k*E, an N scores -1); the MAPQ and insert-size formulas are
Python ports of the documented / published formulas, written from the
manual and the paper, then checked against the code comments.

Usage from a harness:  from _synth import *
The BWA binary is taken from $BWA (default: `bwa` on PATH); the label used
in output file names from $BWA_LABEL.
"""
import math
import os
import random
import re
import subprocess
import sys
import tempfile

BWA = os.environ.get("BWA", "bwa")
LABEL = os.environ.get("BWA_LABEL", "master")
WORK = os.environ.get("BWA_WORK", tempfile.mkdtemp(prefix="bwa_audit_"))

COMP = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}


def revcomp(s):
    return "".join(COMP[c] for c in reversed(s))


def rand_seq(rng, n):
    return "".join(rng.choice("ACGT") for _ in range(n))


def mutate_sub(rng, s, pos):
    """Substitute s[pos] by a different base."""
    b = rng.choice([x for x in "ACGT" if x != s[pos]])
    return s[:pos] + b + s[pos + 1:]


def write_fasta(path, contigs):
    with open(path, "w") as f:
        for name, seq in contigs:
            f.write(">%s\n" % name)
            for i in range(0, len(seq), 60):
                f.write(seq[i:i + 60] + "\n")


def write_fastq(path, reads):
    """reads: list of (name, seq[, qual])"""
    with open(path, "w") as f:
        for r in reads:
            name, seq = r[0], r[1]
            qual = r[2] if len(r) > 2 else "I" * len(seq)
            f.write("@%s\n%s\n+\n%s\n" % (name, seq, qual))


def bwa_version():
    p = subprocess.run([BWA], capture_output=True, text=True)
    for line in p.stderr.splitlines():
        if line.startswith("Version:"):
            return line.split()[1]
    return "?"


def index(fa):
    if not os.path.exists(fa + ".bwt"):
        subprocess.run([BWA, "index", fa], check=True, capture_output=True)


def mem(fa, fq1, fq2=None, opts=()):
    """Run bwa mem; return (sam_records, stderr). -t 1 and -v 3 always."""
    cmd = [BWA, "mem", "-t", "1"] + list(opts) + [fa, fq1] + ([fq2] if fq2 else [])
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("bwa mem failed: %s\n%s" % (" ".join(cmd), p.stderr[-2000:]))
    return parse_sam(p.stdout), p.stderr


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("failed: %s\n%s" % (" ".join(cmd), p.stderr[-2000:]))
    return p.stdout, p.stderr


class Rec:
    __slots__ = ("qname", "flag", "rname", "pos", "mapq", "cigar", "rnext",
                 "pnext", "tlen", "seq", "qual", "tags", "line")

    def __init__(self, line):
        f = line.rstrip("\n").split("\t")
        self.line = line
        self.qname = f[0]
        self.flag = int(f[1])
        self.rname = f[2]
        self.pos = int(f[3])
        self.mapq = int(f[4])
        self.cigar = f[5]
        self.rnext = f[6]
        self.pnext = int(f[7])
        self.tlen = int(f[8])
        self.seq = f[9]
        self.qual = f[10]
        self.tags = {}
        for t in f[11:]:
            k, ty, v = t.split(":", 2)
            self.tags[k] = int(v) if ty == "i" else v

    @property
    def unmapped(self):
        return bool(self.flag & 4)

    @property
    def rev(self):
        return bool(self.flag & 16)

    @property
    def secondary(self):
        return bool(self.flag & 256)

    @property
    def supplementary(self):
        return bool(self.flag & 2048)

    @property
    def primary(self):
        return not (self.flag & (256 | 2048))


def parse_sam(text):
    return [Rec(l) for l in text.splitlines() if l and not l.startswith("@")]


CIG_RE = re.compile(r"(\d+)([MIDNSHP=X])")


def cigar_ops(c):
    return [(int(n), op) for n, op in CIG_RE.findall(c)]


def ref_span(c):
    return sum(n for n, op in cigar_ops(c) if op in "MD=XN")


def clip_lengths(c):
    ops = cigar_ops(c)
    left = ops[0][0] if ops and ops[0][1] in "SH" else 0
    right = ops[-1][0] if ops and ops[-1][1] in "SH" else 0
    return left, right


def nm_md(read, ref, pos0, cigar):
    """Independent NM/MD from the read as printed (SEQ, forward strand),
    the reference string and a 0-based POS. Follows the SAM spec: NM =
    mismatches + inserted + deleted bases (a read N against a base counts as
    a mismatch, as samtools calmd does); MD lists reference bases."""
    nm = 0
    md = []
    run_len = 0
    q = 0
    r = pos0
    for n, op in cigar_ops(cigar):
        if op in "M=X":
            for i in range(n):
                if read[q + i] != ref[r + i]:
                    md.append(str(run_len))
                    md.append(ref[r + i])
                    run_len = 0
                    nm += 1
                else:
                    run_len += 1
            q += n
            r += n
        elif op == "I":
            nm += n
            q += n
        elif op == "D":
            nm += n
            md.append(str(run_len))
            md.append("^" + ref[r:r + n])
            run_len = 0
            r += n
        elif op == "S":
            q += n
        elif op == "H":
            pass
    md.append(str(run_len))
    return nm, "".join(md)


def cigar_score(read, ref, pos0, cigar, a=1, b=4, o=6, e=1, nscore=-1):
    """Score of the alignment printed in the CIGAR, documented scheme."""
    s = 0
    q = 0
    r = pos0
    for n, op in cigar_ops(cigar):
        if op in "M=X":
            for i in range(n):
                x, y = read[q + i], ref[r + i]
                if x == "N" or y == "N":
                    s += nscore
                elif x == y:
                    s += a
                else:
                    s -= b
            q += n
            r += n
        elif op == "I":
            s -= o + n * e
            q += n
        elif op == "D":
            s -= o + n * e
            r += n
        elif op == "S":
            q += n
    return s


def local_sw(q, t, a=1, b=4, o=6, e=1, nscore=-1):
    """Plain affine-gap local Smith-Waterman (Gotoh). Returns the best
    score. Gap of length k costs o + k*e (bwa.1)."""
    NEG = -10 ** 9
    m = len(t)
    H_prev = [0] * (m + 1)
    E_prev = [NEG] * (m + 1)
    best = 0
    for i in range(1, len(q) + 1):
        H = [0] * (m + 1)
        E = [NEG] * (m + 1)
        F = NEG
        qi = q[i - 1]
        for j in range(1, m + 1):
            tj = t[j - 1]
            if qi == "N" or tj == "N":
                s = nscore
            elif qi == tj:
                s = a
            else:
                s = -b
            E[j] = max(E_prev[j] - e, H_prev[j] - o - e)   # gap in t (insertion in q)
            F = max(F - e, H[j - 1] - o - e)              # deletion
            h = max(0, H_prev[j - 1] + s, E[j], F)
            H[j] = h
            if h > best:
                best = h
        H_prev, E_prev = H, E
    return best


def ok(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    return cond


def header(title):
    print("bwa %s (%s)  %s" % (bwa_version(), LABEL, title))
