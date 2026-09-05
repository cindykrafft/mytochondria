#!/usr/bin/env python3
"""computeMatrixOperations sort cannot sort a single-BED matrix written by the
4.0.0 computeMatrix unless the BED file is named genes.bed.

A synthetic bigWig (pyBigWig) and a 4-region BED called regions.bed;
computeMatrix (Rust, 4.0.0) labels the one region group by the file stem
('regions'), computeMatrix_old (3.5.6 code path) labels it 'genes';
computeMatrixOperations sort --regionsFileName regions.bed expects 'genes'.
"""
import gzip
import json
import os
import subprocess
import sys
import tempfile
import pyBigWig

BIN = os.path.dirname(sys.executable)
d = tempfile.mkdtemp()
bw = os.path.join(d, "signal.bw")
b = pyBigWig.open(bw, "w")
b.addHeader([("chr1", 10000)])
b.addEntries(["chr1"] * 100, list(range(0, 10000, 100)), ends=list(range(100, 10001, 100)), values=[float(i) for i in range(100)])
b.close()
bed = os.path.join(d, "regions.bed")
with open(bed, "w") as fh:
    for name, s in [("geneA", 1000), ("geneB", 3000), ("geneC", 5000), ("geneD", 7000)]:
        fh.write("chr1\t%d\t%d\t%s\t0\t+\n" % (s, s + 500, name))
sort_bed = os.path.join(d, "order.bed")
with open(sort_bed, "w") as fh:            # the order we want: D, B, A, C
    for name, s in [("geneD", 7000), ("geneB", 3000), ("geneA", 1000), ("geneC", 5000)]:
        fh.write("chr1\t%d\t%d\t%s\t0\t+\n" % (s, s + 500, name))


def group_labels(mat):
    return json.loads(gzip.open(mat).readline().decode()[1:])["group_labels"]


def regions(mat):
    return [l.split("\t")[3] for l in gzip.open(mat).read().decode().splitlines()[1:]]


for tool in ["computeMatrix", "computeMatrix_old"]:
    mat = os.path.join(d, tool + ".mat.gz")
    subprocess.run([os.path.join(BIN, tool), "reference-point", "-S", bw, "-R", bed, "-o", mat, "-a", "300", "-b", "300", "-bs", "100", "-p", "1"],
                   check=True, capture_output=True)
    print("%-18s group_labels %-12s regions %s" % (tool, group_labels(mat), regions(mat)))
    out = os.path.join(d, tool + ".sorted.mat.gz")
    r = subprocess.run([os.path.join(BIN, "computeMatrixOperations"), "sort", "-m", mat, "-R", sort_bed, "-o", out], capture_output=True, text=True)
    if r.returncode == 0:
        print("   sort with order.bed: regions %s" % regions(out))
    else:
        print("   sort with order.bed: exit %d: %s" % (r.returncode, (r.stderr or r.stdout).strip().splitlines()[-1]))
    if tool == "computeMatrix":
        assert r.returncode == 0, "computeMatrixOperations sort cannot sort the matrix computeMatrix wrote from regions.bed"
