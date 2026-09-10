#!/usr/bin/env python3
"""Minimal complete verifiable example for the ILLUMINACLIP palindrome
mismatch penalty.

Usage: python3 mcve_tc1_palindrome_penalty.py /path/to/trimmomatic-0.41.jar

Everything the example needs is written by the script: a two-record adapter
FASTA holding the stock TruSeq3 PrefixPE pair, and a one-pair FASTQ set.

Geometry: a 40 nt insert read through into the adapters on both sides, 50 nt
reads, so the palindrome alignment is 60 bases long (34 nt prefix + 50 nt read,
overlapping). 54 of those 60 bases match; six mismatches are planted in read 2,
all outside the two 16-mer seeds, and their quality is the only thing the script
varies.

README.md (the "Adapter sequence" section) says: "Each matching base adds just
over 0.6, while each mismatch reduces the alignment score by Q/10."

  54 matches x 0.60206                 = 32.51
  six mismatches at Q9,  6 x 0.9       =  5.40  ->  27.11, below the threshold 30
  six mismatches at Q10, 6 x 1.0       =  6.00  ->  26.51, below the threshold 30

So neither pair should be clipped at ILLUMINACLIP:<fa>:2:30:10. The Q10 pair is
indeed left alone; the Q9 pair is clipped to 40 nt and its mate is dropped.
"""
import os
import subprocess
import sys
import tempfile

JAR = sys.argv[1]

PREFIX1 = "TACACTCTTTCCCTACACGACGCTCTTCCGATCT"   # TruSeq3 PrefixPE/1
PREFIX2 = "GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT"   # TruSeq3 PrefixPE/2

READ1 = "CCGTAATGCCTTTCCCTAACAGAGTTTTTCGAACTCGTGTAGATCGGAAG"
READ2 = "CCCCGAGTTCGAAAAACTCTGTTAGGGAAAGGCATTAGGTAGCTCTGAAG"
MISMATCHES = [0, 2, 37, 39, 42, 45]   # positions in read 2, outside both seeds


def run(tmp, mismatch_q):
    fa = os.path.join(tmp, "adapters.fa")
    with open(fa, "w") as fh:
        fh.write(">PrefixPE/1\n%s\n>PrefixPE/2\n%s\n" % (PREFIX1, PREFIX2))

    q1 = "".join(chr(33 + 35) for _ in READ1)
    q2 = [chr(33 + 35)] * len(READ2)
    for p in MISMATCHES:
        q2[p] = chr(33 + mismatch_q)
    q2 = "".join(q2)

    for name, seq, qual in (("in1.fq", READ1, q1), ("in2.fq", READ2, q2)):
        with open(os.path.join(tmp, name), "w") as fh:
            fh.write("@pair\n%s\n+\n%s\n" % (seq, qual))

    outs = [os.path.join(tmp, n) for n in ("1P.fq", "1U.fq", "2P.fq", "2U.fq")]
    cmd = ["java", "-jar", JAR, "PE", "-phred33",
           os.path.join(tmp, "in1.fq"), os.path.join(tmp, "in2.fq")] + outs + \
          ["ILLUMINACLIP:%s:2:30:10" % fa]
    subprocess.run(cmd, capture_output=True, text=True, check=True,
                   env=dict(os.environ, JAVA_TOOL_OPTIONS=""))

    def length(path):
        with open(path) as fh:
            lines = fh.read().split("\n")
        return len(lines[1]) if len(lines) > 1 and lines[1] else None

    return length(outs[0]) or length(outs[1]), length(outs[2]) or length(outs[3])


for mismatch_q, documented in ((10, 26.51), (9, 27.11)):
    with tempfile.TemporaryDirectory() as tmp:
        l1, l2 = run(tmp, mismatch_q)
    print("six mismatches at Q%-2d  documented score %.2f (threshold 30)" % (mismatch_q, documented))
    print("    expected: read 1 50 nt, read 2 50 nt   (score below the threshold, nothing to clip)")
    print("    got:      read 1 %s, read 2 %s" % (
        "%d nt" % l1 if l1 else "dropped", "%d nt" % l2 if l2 else "dropped"))
