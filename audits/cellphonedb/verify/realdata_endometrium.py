#!/usr/bin/env python3
"""Impact of CPDB1/CPDB2 on the project's own example dataset.

Runs `cpdb_statistical_analysis_method` on the endometrium atlas example shipped in the
repository (example_data/endometrium_atlas_example: 1,949 cells, 20 cell types, 20,975 genes)
against the v5.0.0 database shipped in the repository
(NatureProtocols2024_case_studies/v5.0.0/cellphonedb.zip -- the official download endpoint
returns HTTP 403 from this environment), with the documented defaults iterations=1000,
threshold=0.1, pvalue=0.05.

Reports, on real output:
  1. how many reported p-values are exactly 0 (CPDB2: the estimator has no +1, and ties with
     the observed statistic are not counted, so 0 is attainable and common);
  2. the granularity of the p-value grid as a function of `threads` (CPDB1: with T workers the
     counts are multiples of T because the workers draw the same permutations);
  3. how much two runs that differ only in `threads` disagree.

Set CPDB_CLONE to the repository clone. Takes a few minutes per run.
"""
import os
import sys
import numpy as np
import pandas as pd
from importlib.metadata import version

CLONE = os.environ.get(
    "CPDB_CLONE",
    "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8"
    "/scratchpad/cellphonedb/CellphoneDB")
DB = os.path.join(CLONE, "NatureProtocols2024_case_studies/v5.0.0/cellphonedb.zip")
DATA = os.path.join(CLONE, "example_data/endometrium_atlas_example")
OUT = os.environ.get("CPDB_OUT", "/tmp/cpdb_realdata")

from cellphonedb.src.core.methods import cpdb_statistical_analysis_method

META = {"id_cp_interaction", "interacting_pair", "partner_a", "partner_b", "gene_a", "gene_b",
        "secreted", "receptor_a", "receptor_b", "annotation_strategy", "is_integrin",
        "directionality", "classification", "rank"}


def run(threads, iterations=1000):
    os.makedirs(OUT, exist_ok=True)
    return cpdb_statistical_analysis_method.call(
        cpdb_file_path=DB,
        meta_file_path=os.path.join(DATA, "endometrium_example_meta.tsv"),
        counts_file_path=os.path.join(DATA, "endometrium_example_counts.h5ad"),
        counts_data="hgnc_symbol", output_path=OUT,
        iterations=iterations, threshold=0.1, threads=threads, debug_seed=-1,
        result_precision=3, pvalue=0.05, separator="|",
        output_suffix="threads%d" % threads)


def pmatrix(res):
    df = res["pvalues"]
    return df[[c for c in df.columns if c not in META]].astype(float)


print("cellphonedb", version("cellphonedb"))
print("database:", os.path.basename(DB), " data:", os.path.basename(DATA))
res = {}
for t in (4, 1):
    print("\n===== running with threads=%d, iterations=1000 =====" % t, flush=True)
    res[t] = run(t)

for t in (1, 4):
    p = pmatrix(res[t]).to_numpy()
    tested = p < 1.0            # entries the method actually tested (p is forced to 1 otherwise)
    counts = np.round(p * 1000).astype(int)
    gcd = np.gcd.reduce(counts[counts > 0].ravel()) if (counts > 0).any() else 0
    print("\nthreads=%d  matrix %s" % (t, p.shape))
    print("  entries tested (p < 1)          : %d of %d (%.1f%%)"
          % (tested.sum(), p.size, 100 * tested.sum() / p.size))
    print("  reported p == 0                 : %d (%.1f%% of tested entries)"
          % ((p == 0).sum(), 100 * (p == 0).sum() / max(tested.sum(), 1)))
    print("  p <= 0.05 (called significant)  : %d" % ((p <= 0.05).sum()))
    print("  distinct p values below 1       : %d" % len(np.unique(p[tested])))
    print("  GCD of the exceedance counts    : %d   <-- CPDB1: equals `threads` when workers"
          " draw duplicate permutations" % gcd)

p1, p4 = pmatrix(res[1]), pmatrix(res[4])
common = [c for c in p1.columns if c in p4.columns]
a, b = p1[common].to_numpy(), p4[common].to_numpy()
sig1, sig4 = a <= 0.05, b <= 0.05
print("\nthreads=1 vs threads=4 (same data, same settings, different worker count):")
print("  significant calls: %d vs %d, disagreeing on %d entries"
      % (sig1.sum(), sig4.sum(), (sig1 != sig4).sum()))
print("  p == 0 entries   : %d vs %d" % ((a == 0).sum(), (b == 0).sum()))
