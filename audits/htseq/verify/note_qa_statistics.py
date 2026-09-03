#!/usr/bin/env python3
"""htseq-qa statistics (HTSeq/scripts/qa.py `compute_quality`) against a numpy
reference on a synthetic FASTQ and a synthetic BAM.

Checks:
  1. base-composition-by-position (`norm_by_pos`) and quality-by-position
     (`norm_by_start`) equal a direct computation on the same reads;
  2. minus-strand BAM records are counted in sequencing orientation (the
     stored sequence is reverse-complemented back and the qualities reversed);
  3. `--primary-only` drops secondary (0x100) records but keeps supplementary
     (0x800) records, so a chimeric read counts twice (note);
  4. reads with a quality above --maxqual (default 41) abort the script (note).
"""
import os
import random
import sys
import tempfile

import numpy as np
import pysam
import HTSeq
from HTSeq.scripts.qa import compute_quality

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0])
rng = random.Random(3)
tmp = tempfile.mkdtemp()
L = 50
N = 2000
COMP = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}


def revcomp(s):
    return "".join(COMP[c] for c in reversed(s))


# ---------------------------------------------------------------- 1. FASTQ
seqs, quals = [], []
for i in range(N):
    n = L if rng.random() < 0.8 else rng.randint(20, L)  # some shorter reads
    seqs.append("".join(rng.choice("ACGTN") for _ in range(n)))
    quals.append([rng.randint(2, 41) for _ in range(n)])
fq = os.path.join(tmp, "r.fastq")
with open(fq, "w") as f:
    for i, (s, q) in enumerate(zip(seqs, quals)):
        f.write(f"@r{i}\n{s}\n+\n{''.join(chr(33 + x) for x in q)}\n")


def reference(seqs, quals, readlen, maxq=41):
    base = np.zeros((readlen, 5))
    qual = np.zeros((readlen, maxq + 1))
    for s, q in zip(seqs, quals):
        for i, (c, x) in enumerate(zip(s, q)):
            base[i, "ACGTN".index(c)] += 1
            qual[i, x] += 1
    with np.errstate(invalid="ignore", divide="ignore"):
        base_n = base / base.sum(1, keepdims=True)
    base_n[np.isnan(base_n)] = 0
    qual_n = qual / qual.sum(1)[0]  # fraction of all reads (reads with a base at position 0)
    return base_n, qual_n


res = compute_quality(fq, "fastq", nosplit=True, readlen=None, max_qual=41, gamma=0.3)
base_n, qual_n = reference(seqs, quals, res["readlen"])
print("\n== 1. FASTQ: readlen guessed", res["readlen"], "nreads", res["nreads_U"])
print("  max |base fraction - reference| =", float(np.abs(res["base_arr_U_n"] - base_n).max()))
print("  max |quality fraction - reference| =", float(np.abs(res["qual_arr_U_n"] - qual_n).max()))

# ---------------------------------------------------------------- 2. BAM with strands
hdr = {"HD": {"VN": "1.6"}, "SQ": [{"SN": "chr1", "LN": 100000}]}
bam = os.path.join(tmp, "r.bam")
aligned_flags = []
with pysam.AlignmentFile(bam, "wb", header=hdr) as f:
    for i, (s, q) in enumerate(zip(seqs, quals)):
        a = pysam.AlignedSegment()
        a.query_name = f"r{i}"
        kind = rng.random()
        if kind < 0.2:  # unaligned
            a.flag = 4
            a.query_sequence = s
            a.query_qualities = q
            a.reference_id, a.reference_start = -1, -1
        else:
            minus = kind < 0.6
            a.flag = 16 if minus else 0
            a.query_sequence = revcomp(s) if minus else s
            a.query_qualities = q[::-1] if minus else q
            a.reference_id, a.reference_start, a.mapping_quality = 0, 1000 + i * 3, 60
            a.cigartuples = [(0, len(s))]
        aligned_flags.append(a.flag)
        f.write(a)
res = compute_quality(bam, "bam", nosplit=False, readlen=L, max_qual=41, gamma=0.3)
al = [i for i, fl in enumerate(aligned_flags) if not fl & 4]
un = [i for i, fl in enumerate(aligned_flags) if fl & 4]
bA, qA = reference([seqs[i] for i in al], [quals[i] for i in al], L)
bU, qU = reference([seqs[i] for i in un], [quals[i] for i in un], L)
print("\n== 2. BAM split into aligned / unaligned; minus-strand records must be counted as sequenced")
print("  aligned:   max |base - ref| =", float(np.abs(res["base_arr_A_n"] - bA).max()),
      " max |qual - ref| =", float(np.abs(res["qual_arr_A_n"] - qA).max()), " nreads", res["nreads_A"], len(al))
print("  unaligned: max |base - ref| =", float(np.abs(res["base_arr_U_n"] - bU).max()),
      " max |qual - ref| =", float(np.abs(res["qual_arr_U_n"] - qU).max()), " nreads", res["nreads_U"], len(un))

# ---------------------------------------------------------------- 3. --primary-only and supplementary
bam2 = os.path.join(tmp, "chim.bam")
with pysam.AlignmentFile(bam2, "wb", header=hdr) as f:
    for i in range(100):
        s = "".join(rng.choice("ACGT") for _ in range(L))
        for flag in (0, 0x100, 0x800):  # primary, secondary, supplementary
            a = pysam.AlignedSegment()
            a.query_name = f"c{i}"
            a.flag = flag
            a.query_sequence = s
            a.query_qualities = [30] * L
            a.reference_id, a.reference_start, a.mapping_quality = 0, 100 + i, 60
            a.cigartuples = [(0, L)]
            f.write(a)
for po in (False, True):
    r = compute_quality(bam2, "bam", nosplit=False, readlen=L, max_qual=41, gamma=0.3, primary_only=po)
    print(f"\n== 3. 100 reads x (primary + secondary + supplementary); primary_only={po}: "
          f"records counted as aligned = {r['nreads_A']} (100 reads)")

# ---------------------------------------------------------------- 4. quality above maxqual
fq2 = os.path.join(tmp, "hi.fastq")
with open(fq2, "w") as f:
    f.write("@x\nACGT\n+\n" + "".join(chr(33 + 42) for _ in range(4)) + "\n")
try:
    compute_quality(fq2, "fastq", nosplit=True, readlen=None, max_qual=41, gamma=0.3)
    print("\n== 4. Q42 read with default --maxqual 41: no error")
except Exception as e:
    print("\n== 4. Q42 read with default --maxqual 41 ->", type(e).__name__, e)
