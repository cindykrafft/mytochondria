"""N5: `samtools coverage --rf` ("required flags: skip reads with mask bits
unset") keeps a read when ANY of the mask bits is set (coverage.c read_bam:
`!(flag & required_flags)`), like mpileup's --rf, whereas `depth
--require-flags` and `view -f` need ALL bits.  Usage: python note_coverage_rf_semantics.py [samtools]
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
d = tmpdir()
refs = [("chr1", 10000)]
recs = []
for i, flag in enumerate([0x63, 0x93, 0x41, 0x81, 0x61, 0x91, 0x0, 0x10] * 10):
    recs.append(simple_read(f"r{i}", 100 + i * 20, "50M", flag=flag, mtid=0, mpos=100, tlen=0))
bam = write_bam(os.path.join(d, "rf.bam"), recs, refs)
for mask in ("0x42", "0x2", "0x40", "0x43"):
    m = int(mask, 16)
    cov = [l for l in run("coverage", "--rf", mask, bam)[0].splitlines() if l.startswith("chr1")][0].split("\t")
    dep = run("depth", "--require-flags", mask, bam)[0]
    reads_all = sum(1 for r in recs if (r["flag"] & m) == m)
    reads_any = sum(1 for r in recs if r["flag"] & m)
    depth_total = sum(int(l.split("\t")[2]) for l in dep.splitlines())
    print(f"  --rf {mask}: coverage numreads {cov[3]}   reads with ALL bits {reads_all}   reads with ANY bit {reads_any}   | depth --require-flags total depth {depth_total} = {depth_total // 50} reads")
