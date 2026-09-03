"""Shared helpers for the deepTools verification harnesses.

Builds small synthetic BAM / bigWig / BED files with known truth (pysam writes
the BAM, pyBigWig the bigWig) and computes the reference quantities with numpy
only, so that every comparison is against an independent closed form.

Every harness imports this module from its own directory. The deepTools
executables are taken from the directory of the running interpreter, so the
same harness runs against whichever venv is active (master editable install,
or a PyPI wheel of a released version).
"""
import os
import subprocess
import sys
import tempfile

import numpy as np
import pysam
import pyBigWig

BIN = os.path.dirname(sys.executable)


def tool(name):
    return os.path.join(BIN, name)


def version():
    r = subprocess.run([tool("bamCoverage"), "--version"], capture_output=True, text=True)
    return (r.stdout or r.stderr).strip().splitlines()[-1]


def run(cmd, check=True):
    """Run a deepTools command line (list); return (stdout, stderr)."""
    cmd = [tool(cmd[0])] + [str(x) for x in cmd[1:]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("command failed: %s\n%s" % (" ".join(cmd), r.stderr))
    return r.stdout, r.stderr


# ----------------------------------------------------------------------------
# BAM construction
# ----------------------------------------------------------------------------

def _seg(chrom_id, pos, rlen, flag, qname, mapq=30, cigar=None):
    a = pysam.AlignedSegment()
    a.query_name = qname
    a.query_sequence = "A" * rlen
    a.flag = flag
    a.reference_id = chrom_id
    a.reference_start = int(pos)
    a.mapping_quality = mapq
    a.cigar = cigar if cigar is not None else ((0, rlen),)
    a.query_qualities = pysam.qualitystring_to_array("I" * rlen)
    a.next_reference_id = -1
    a.next_reference_start = -1
    a.template_length = 0
    return a


def se_read(chrom_id, pos, rlen, reverse, qname, mapq=30):
    """Single-end read: (chrom_id, 0-based start, length, strand)."""
    return _seg(chrom_id, pos, rlen, 16 if reverse else 0, qname, mapq)


def pe_pair(chrom_id, fstart, flen, rlen, qname, mapq=30, first_forward=True):
    """Properly paired fragment [fstart, fstart+flen): forward mate at the
    fragment start, reverse mate ending at the fragment end. Both mates carry
    TLEN = +/- flen as the SAM spec defines it. Returns the two reads."""
    fwd = _seg(chrom_id, fstart, rlen, 99 if first_forward else 163, qname, mapq)
    rev = _seg(chrom_id, fstart + flen - rlen, rlen, 147 if first_forward else 83, qname, mapq)
    fwd.next_reference_id = chrom_id
    fwd.next_reference_start = rev.reference_start
    fwd.template_length = flen
    rev.next_reference_id = chrom_id
    rev.next_reference_start = fwd.reference_start
    rev.template_length = -flen
    return fwd, rev


def write_bam(path, chroms, reads):
    """chroms: list of (name, length); reads: iterable of AlignedSegment.
    Writes a coordinate-sorted, indexed BAM."""
    header = {"HD": {"VN": "1.0", "SO": "unsorted"},
              "SQ": [{"SN": n, "LN": int(L)} for n, L in chroms]}
    tmp = path + ".unsorted.bam"
    with pysam.AlignmentFile(tmp, "wb", header=header) as fh:
        for r in reads:
            fh.write(r)
    pysam.sort("-o", path, tmp)
    os.remove(tmp)
    pysam.index(path)
    return path


def random_se_reads(rng, chrom_id, chrom_len, n, rlen, prefix="r", weights=None):
    """n single-end reads of length rlen with random strand; optional
    per-position weights (unnormalised) make the coverage non-uniform.
    Returns (reads, fragments) where fragments are (start, end, reverse)."""
    if weights is None:
        starts = rng.integers(0, chrom_len - rlen, n)
    else:
        p = np.asarray(weights, dtype=float)
        p = p / p.sum()
        starts = rng.choice(len(p), size=n, p=p)
        starts = np.minimum(starts, chrom_len - rlen)
    rev = rng.random(n) < 0.5
    reads, frags = [], []
    for i in range(n):
        reads.append(se_read(chrom_id, starts[i], rlen, bool(rev[i]), "%s%d" % (prefix, i)))
        frags.append((int(starts[i]), int(starts[i]) + rlen, bool(rev[i])))
    return reads, frags


def random_pe_pairs(rng, chrom_id, chrom_len, n, rlen, flen_choices, prefix="p"):
    """n proper pairs; fragment length drawn from flen_choices (list/array).
    Returns (reads, fragments) with fragments (start, end)."""
    flens = rng.choice(np.asarray(flen_choices), size=n)
    starts = rng.integers(0, chrom_len - int(np.max(flens)), n)
    reads, frags = [], []
    for i in range(n):
        reads.extend(pe_pair(chrom_id, int(starts[i]), int(flens[i]), rlen, "%s%d" % (prefix, i)))
        frags.append((int(starts[i]), int(starts[i]) + int(flens[i])))
    return reads, frags


# ----------------------------------------------------------------------------
# Reference quantities (numpy only)
# ----------------------------------------------------------------------------

def per_base(frags, L):
    """Per-base coverage (number of fragments covering each base)."""
    cov = np.zeros(L + 1, dtype=np.int64)
    for f in frags:
        s, e = f[0], f[1]
        cov[max(0, s)] += 1
        cov[min(L, e)] -= 1
    return np.cumsum(cov)[:L]


def bin_overlap_counts(frags, L, binsize):
    """Number of fragments overlapping each bin (deepTools' 'reads per bin')."""
    nb = int(np.ceil(L / binsize))
    counts = np.zeros(nb, dtype=np.int64)
    for f in frags:
        s, e = max(0, f[0]), min(L, f[1])
        if e <= s:
            continue
        b0 = s // binsize
        b1 = (e - 1) // binsize
        counts[b0:b1 + 1] += 1
    return counts


def bin_sums(frags, L, binsize):
    """Sum of per-base coverage in each bin."""
    pb = per_base(frags, L)
    nb = int(np.ceil(L / binsize))
    out = np.zeros(nb, dtype=np.int64)
    for b in range(nb):
        out[b] = pb[b * binsize:(b + 1) * binsize].sum()
    return out


# ----------------------------------------------------------------------------
# bigWig / bedGraph readers and writers
# ----------------------------------------------------------------------------

def write_bigwig(path, chroms, values_by_chrom):
    """values_by_chrom: {chrom: per-base float array}; NaN entries are left out
    (missing data)."""
    bw = pyBigWig.open(path, "w")
    bw.addHeader([(n, int(L)) for n, L in chroms])
    for n, L in chroms:
        v = np.asarray(values_by_chrom[n], dtype=float)
        # run-length encode into intervals, skipping NaN
        starts, ends, vals = [], [], []
        i = 0
        while i < len(v):
            if np.isnan(v[i]):
                i += 1
                continue
            j = i + 1
            while j < len(v) and v[j] == v[i]:
                j += 1
            starts.append(i)
            ends.append(j)
            vals.append(float(v[i]))
            i = j
        if starts:
            bw.addEntries([n] * len(starts), starts, ends=ends, values=vals)
    bw.close()
    return path


def read_bigwig_per_base(path, chrom, L):
    bw = pyBigWig.open(path)
    v = np.array(bw.values(chrom, 0, L), dtype=float)
    bw.close()
    return v


def read_bedgraph(path):
    out = []
    with open(path) as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("track"):
                continue
            c, s, e, v = line.split()[:4]
            out.append((c, int(s), int(e), float(v)))
    return out


def bedgraph_to_per_base(intervals, chrom, L, fill=np.nan):
    v = np.full(L, fill, dtype=float)
    for c, s, e, val in intervals:
        if c == chrom:
            v[s:min(e, L)] = val
    return v


def tmpdir():
    return tempfile.mkdtemp(prefix="dt_audit_")
