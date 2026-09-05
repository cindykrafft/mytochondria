"""Reproduction for deeptools/deepTools#1423 on 4.0.0 (4db9d816): computeMatrix is
now Rust-backed (deeptools.computeMatrix2) and reads gzipped BED files itself;
computeMatrixOperations sort still goes through computeMatrixOperations.loadBED.
The matrix is computed from the plain BED, then sorted with the plain and the gzipped copy.
Builds its own bigWig and BED, needs only deepTools (pyBigWig comes with it)."""
import gzip
import os
import sys
import tempfile
import traceback

import pyBigWig
import deeptools.computeMatrix2
import deeptools.computeMatrixOperations as cmo
from importlib.metadata import version

tmp = tempfile.mkdtemp(prefix="dt1423_")
bw = os.path.join(tmp, "signal.bw")
# named genes.bed: the Rust computeMatrix labels a single region group by the file
# stem, and computeMatrixOperations sort expects "genes" for a single -R file
bed = os.path.join(tmp, "genes.bed")
bedgz = bed + ".gz"

fh = pyBigWig.open(bw, "w")
fh.addHeader([("chr1", 2000), ("chr2", 2000)])
for chrom in ("chr1", "chr2"):
    starts = list(range(0, 2000, 100))
    fh.addEntries([chrom] * len(starts), starts, ends=[s + 100 for s in starts],
                  values=[float(s // 100) for s in starts])
fh.close()

lines = ["chr2\t1000\t1100\tgeneC\t0\t+",
         "chr1\t500\t600\tgeneA\t0\t+",
         "chr1\t1500\t1600\tgeneB\t0\t-"]
with open(bed, "w") as f:
    f.write("\n".join(lines) + "\n")
with gzip.open(bedgz, "wt") as f:
    f.write("\n".join(lines) + "\n")


def rows_of(path):
    with gzip.open(path, "rt") as f:
        return [l.split("\t")[3] for l in f if not l.startswith("@")]


sys.argv = ["computeMatrix", "reference-point"]
print("deeptools", version("deeptools"))
mat = os.path.join(tmp, "mat.gz")
for regions in (bed,):
    args = ("reference-point -R {} -S {} -b 200 -a 200 -bs 100 -p 1 "
            "-o {}".format(regions, bw, mat)).split()
    print("\n== computeMatrix (Rust backend)", os.path.basename(regions), "(default --sortRegions keep)")
    try:
        deeptools.computeMatrix2.main(args)
    except BaseException:
        traceback.print_exc(file=sys.stdout)
        print("RESULT: crashed")
        continue
    print("RESULT: ok, region order in the matrix:", rows_of(mat))

for regions in (bed, bedgz):
    out = os.path.join(tmp, "sorted.gz")
    print("\n== computeMatrixOperations sort -R", os.path.basename(regions))
    try:
        cmo.main("sort -m {} -o {} -R {}".format(mat, out, regions).split())
    except BaseException:
        traceback.print_exc(file=sys.stdout)
        print("RESULT: crashed")
        continue
    print("RESULT: ok, region order after sort:", rows_of(out))
