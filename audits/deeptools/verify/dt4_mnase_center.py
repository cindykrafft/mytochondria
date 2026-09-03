#!/usr/bin/env python3
"""DT4: bamCoverage --MNase counts four bases, off centre, for fragments of odd
length (documented: three bases at the centre).

bamCoverage.CenterFragment.get_fragment_from_read computes
    fragment_start = read.pos + read.tlen / 2 - 1
with Python 3 true division; for odd TLEN the start is a half-integer, and
countReadsPerBin.get_coverage_of_region floors the start bin and ceils the end
bin, so [x.5, x.5 + 3) covers four 1-bp bins. Under Python 2 (integer
division) the same expression gave three bases centred on the middle base.

Proper pairs of fragment length 149, 150, 151 and 200 at known positions on
one chromosome; bamCoverage --MNase -bs 1 -of bedgraph; the covered bases per
fragment are compared with the documented rule (even: the two central bases;
odd: the central base and its two neighbours).
"""
import os
import numpy as np
import _synth as S

print(S.version())
d = S.tmpdir()
L = 5000
reads, truth = [], []
for i, (start, flen) in enumerate([(100, 149), (600, 150), (1100, 151), (1600, 200), (2100, 131), (2600, 199)]):
    reads.extend(S.pe_pair(0, start, flen, 50, "f%d" % i))
    truth.append((start, flen))
bam = S.write_bam(os.path.join(d, "mnase.bam"), [("chr1", L)], reads)
out = os.path.join(d, "mnase.bg")
S.run(["bamCoverage", "-b", bam, "-o", out, "-of", "bedgraph", "--MNase", "-bs", 1, "-p", 1])
cov = S.bedgraph_to_per_base(S.read_bedgraph(out), "chr1", L, fill=0.0)

print("%-8s %-6s %-22s %-22s %s" % ("start", "len", "documented bases", "bamCoverage bases", "ok"))
nbad = 0
for start, flen in truth:
    if flen % 2 == 0:
        exp = [start + flen // 2 - 1, start + flen // 2]
    else:
        c = start + flen // 2
        exp = [c - 1, c, c + 1]
    got = [int(x) for x in np.flatnonzero(cov[start:start + flen]) + start]
    ok = got == exp
    nbad += not ok
    print("%-8d %-6d %-22s %-22s %s" % (start, flen, exp, got, ok))
print("fragments with wrong centre bases: %d of %d (all odd-length ones: %s)"
      % (nbad, len(truth), nbad == sum(f % 2 for _, f in truth)))
