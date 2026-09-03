#!/usr/bin/env python3
"""Note: the shipped defaults of htseq-count's --secondary-alignments and
--supplementary-alignments versus doc/htseqcount.rst, which says
"(default: ``score``)" for both. Also records the other defaults the review
cites and the float32 dtype used for the mtx/h5ad/loom count matrices.

Executed: `htseq-count --help` parsed for the defaults, a two-record BAM
(primary + secondary) counted with and without the options, and a count of
2^24 + 1 written through the mtx path.
"""
import os
import re
import subprocess
import sys
import tempfile

import numpy as np
import pysam
import HTSeq

print("HTSeq", HTSeq.__version__, "python", sys.version.split()[0])
help_text = subprocess.run([sys.executable, "-W", "ignore", "-m", "HTSeq.scripts.count", "--help"],
                           capture_output=True, text=True).stdout
help_text = re.sub(r"\s+", " ", help_text)
for opt in ("--secondary-alignments", "--supplementary-alignments", "--nonunique", "--stranded", "--minaqual",
            "--mode", "--order"):
    m = re.search(re.escape(opt) + r".{0,400}?\(default: ([^)]*)\)", help_text)
    m2 = re.search(re.escape(opt) + r" \{([^}]*)\}", help_text)
    print(f"  {opt:28s} choices {('{' + m2.group(1) + '}') if m2 else '?':40s} help says default: "
          f"{m.group(1) if m else '(not stated in --help)'}")

tmp = tempfile.mkdtemp()
gtf = os.path.join(tmp, "g.gtf")
open(gtf, "w").write('chr1\tsrc\texon\t1001\t2000\t.\t+\t.\tgene_id "A";\n')
bam = os.path.join(tmp, "g.bam")
with pysam.AlignmentFile(bam, "wb", header={"HD": {"VN": "1.6"}, "SQ": [{"SN": "chr1", "LN": 10000}]}) as f:
    for flag in (0, 0x100, 0x800):
        a = pysam.AlignedSegment()
        a.query_name, a.flag, a.query_sequence = "r", flag, "A" * 30
        a.query_qualities = pysam.qualitystring_to_array("I" * 30)
        a.reference_id, a.reference_start, a.mapping_quality, a.cigartuples = 0, 1100, 60, [(0, 30)]
        f.write(a)


def run(extra):
    p = subprocess.run([sys.executable, "-W", "ignore", "-m", "HTSeq.scripts.count", "-q"] + extra + [bam, gtf],
                       capture_output=True, text=True)
    return dict(line.split("\t") for line in p.stdout.splitlines())


print("\nBAM with one read: primary + secondary + supplementary record, all in gene A:")
print("  defaults                                       -> A =", run([])["A"])
print("  --secondary-alignments score                   -> A =", run(["--secondary-alignments", "score"])["A"])
print("  --secondary-alignments score --supplementary-alignments score -> A =",
      run(["--secondary-alignments", "score", "--supplementary-alignments", "score"])["A"])
print("  doc/htseqcount.rst says both default to 'score'; the code defaults to 'ignore'"
      " (count.py, commit 7be4fe3 of 2018-05-16, history.rst entry for 0.10.0).")

# float32 output matrices
from HTSeq.scripts.utils import _merge_counts  # noqa: E402
res = [{"isam": 0, "counts": {"A": 2**24 + 1, "B": 3}, "empty": 0, "ambiguous": 0, "lowqual": 0,
        "notaligned": 0, "nonunique": 0}]
t = _merge_counts(res, {"A": [], "B": []}, [], sparse=False, dtype=np.float32)["table"]
print(f"\nmtx/h5ad/loom table dtype {t.dtype}: a count of {2**24 + 1} is stored as {int(t[0, 0])} "
      f"(documented: 'the data type is float32')")
