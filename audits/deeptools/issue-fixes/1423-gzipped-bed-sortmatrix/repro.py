"""Reproduction for deeptools/deepTools#1423: computeMatrix crashes on a gzipped BED
with the default --sortRegions keep.  Builds its own bigWig and BED, needs only
deepTools (pyBigWig comes with it)."""
import gzip
import os
import sys
import tempfile
import traceback

import pyBigWig
import deeptools.computeMatrix
from importlib.metadata import version

tmp = tempfile.mkdtemp(prefix="dt1423_")
bw = os.path.join(tmp, "signal.bw")
bed = os.path.join(tmp, "regions.bed")
bedgz = bed + ".gz"

# a 2-chromosome bigWig with a simple ramp so the matrix is easy to check
fh = pyBigWig.open(bw, "w")
fh.addHeader([("chr1", 2000), ("chr2", 2000)])
for chrom in ("chr1", "chr2"):
    starts = list(range(0, 2000, 100))
    fh.addEntries([chrom] * len(starts), starts, ends=[s + 100 for s in starts],
                  values=[float(s // 100) for s in starts])
fh.close()

# three regions, deliberately not in genomic order (so "keep" must reorder)
lines = ["chr2\t1000\t1100\tgeneC\t0\t+",
         "chr1\t500\t600\tgeneA\t0\t+",
         "chr1\t1500\t1600\tgeneB\t0\t-"]
with open(bed, "w") as f:
    f.write("\n".join(lines) + "\n")
with gzip.open(bedgz, "wt") as f:
    f.write("\n".join(lines) + "\n")

sys.argv = ["computeMatrix", "reference-point"]  # main() prints help and exits when len(sys.argv) == 1
print("deeptools", version("deeptools"))
for regions in (bed, bedgz):
    out = os.path.join(tmp, "mat.gz")
    args = ("reference-point -R {} -S {} -b 200 -a 200 -bs 100 -p 1 "
            "-o {}".format(regions, bw, out)).split()
    print("\n== computeMatrix", os.path.basename(regions), "(default --sortRegions keep)")
    try:
        deeptools.computeMatrix.main(args)
    except Exception:
        traceback.print_exc(file=sys.stdout)
        print("RESULT: crashed")
        continue
    with gzip.open(out, "rt") as f:
        rows = [l.split("\t")[3] for l in f if not l.startswith("@")]
    print("RESULT: ok, region order in the matrix:", rows)
