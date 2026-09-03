"""Minimal reproduction for FP3: an adapter carrying one inserted or deleted base
is only recognised when it sits at the very start of the read.

Three reads of 74 nt: 40 nt of insert followed by the Illumina TruSeq Read 1
adapter, once exactly, once with one inserted base, once with one deleted base.
All three should come out 40 nt long; only the exact one does. The fourth read
puts the same adapter-with-insertion at position 0, where it is recognised --
which is the whole search space the two gapped loops actually cover.

Usage: python3 mcve_fp3_indel_adapter.py [path-to-fastp]
"""
import os
import subprocess
import sys
import tempfile

FASTP = sys.argv[1] if len(sys.argv) > 1 else "fastp"
AD = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"
INSERT = "TTTTAACCCCCCCCCCCCCCCCCCCCCCCCCCCCAATTTT"      # 40 nt
reads = [
    ("exact", INSERT + AD, 40),
    ("one_inserted_base", INSERT + AD[:8] + "G" + AD[8:], 40),
    ("one_deleted_base", INSERT + AD[:8] + AD[9:], 40),
    ("insertion_at_position_0", AD[:8] + "G" + AD[8:] + INSERT, 0),
]
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "reads.fastq")
    with open(path, "w") as f:
        for name, seq, _ in reads:
            f.write("@%s\n%s\n+\n%s\n" % (name, seq, "I" * len(seq)))
    out = os.path.join(tmp, "out.fastq")
    subprocess.run([FASTP, "-i", path, "-o", out, "-a", AD,
                    "--disable_quality_filtering", "--disable_length_filtering",
                    "--disable_trim_poly_g", "-j", os.path.join(tmp, "j"),
                    "-h", os.path.join(tmp, "h")], capture_output=True, text=True)
    lines = open(out).read().splitlines()
    got = {lines[i][1:]: lines[i + 1] for i in range(0, len(lines), 4)}
    for name, seq, expected in reads:
        n = len(got.get(name, ""))
        print("%-24s output %3d nt (expected %d)%s"
              % (name, n, expected, "" if n == expected else "   <-- adapter left in the read"))
