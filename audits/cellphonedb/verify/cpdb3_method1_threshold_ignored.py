#!/usr/bin/env python3
"""CPDB3: in METHOD 1 (`cpdb_analysis_method`), the `threshold` argument changes nothing in any
returned or written output.

`cpdb_analysis_method.call` computes the percent analysis and passes it to `build_results`,
which uses it to build `significant_means` (cpdb_analysis_method.py:134-138, 240-242). But the
returned dict is assembled from `means_result`, `deconvoluted` and `deconvoluted_percents` only
(lines 175-177): `significant_means` -- the only product in which the threshold has any effect
-- is used for a rank sort (lines 171-173) and then dropped. `file_utils.save_dfs_as_tsv` then
writes exactly the keys of that dict, so no thresholded file is written either.

What the documentation promises for this method (docs/RESULTS-DOCUMENTATION.md:78, the METHOD 1
section):

    "Note that CellphoneDB will report the means only if all the gene members of the
     interactions are expressed by at least a fraction of cells in a cell type (`threshold`).
     If the condition `threshold` is not met, the interaction will be ignored in the
     corresponding cell type pairs."

and RESULTS-DOCUMENTATION.md:86: "Only interactions involving receptors and ligands expressed by
more than a fraction of the cells (`threshold` default is 0.1, which is 10%) in the specific
cluster are included."

The harness runs METHOD 1 at threshold=0.1 (default) and threshold=0.99 (which no gene in the
fixture meets in every cluster) and diffs every output, then runs METHOD 2 on the same data at
the same two thresholds to show that there the parameter does bite.
"""
import filecmp
import os
import sys
import tempfile
import numpy as np
import pandas as pd
from importlib.metadata import version

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tiny_dataset as T

from cellphonedb.src.core.methods import cpdb_analysis_method, cpdb_statistical_analysis_method

tmp = tempfile.mkdtemp(prefix="cpdb3_")
db = T.build_db(os.path.join(tmp, "db"))
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"))
print("cellphonedb", version("cellphonedb"))
print("fixture percents per cluster (fraction of cells with value > 0):")
_m, pcts = T.cluster_means_pcts(T.COUNTS, np.array(T.CELL_TYPES))
print(pcts.round(4).to_string())

res = {}
outs = {}
for thr in (0.1, 0.99):
    outs[thr] = os.path.join(tmp, "m1_%s" % thr)
    res[thr] = cpdb_analysis_method.call(
        cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp,
        counts_data="ensembl", output_path=outs[thr], separator="|", threshold=thr,
        result_precision=3, output_suffix="run", threads=1)

print("\nMETHOD 1 (cpdb_analysis_method)")
print("  keys returned at threshold=0.1 :", sorted(res[0.1].keys()))
print("  keys returned at threshold=0.99:", sorted(res[0.99].keys()))
print("  'significant_means' in the returned dict:",
      "significant_means" in res[0.1] or "significant_means_result" in res[0.1])
f1, f2 = sorted(os.listdir(outs[0.1])), sorted(os.listdir(outs[0.99]))
print("  files written at threshold=0.1 :", f1)
print("  files written at threshold=0.99:", f2)
same = [f for f in f1 if f in f2 and filecmp.cmp(os.path.join(outs[0.1], f),
                                                 os.path.join(outs[0.99], f), shallow=False)]
print("  files byte-identical between the two thresholds: %d of %d" % (len(same), len(f1)))
for f in f1:
    ident = f in same
    print("      %-52s %s" % (f, "identical" if ident else "DIFFERS"))

cols = [c for c in res[0.1]["means_result"].columns if "|" in c]
a = res[0.1]["means_result"].set_index("interacting_pair")[cols].astype(float)
b = res[0.99]["means_result"].set_index("interacting_pair")[cols].astype(float)
print("\n  means_result, max |threshold=0.1 - threshold=0.99| = %.1e" % np.abs(a - b).to_numpy().max())
print(a.to_string())
print("\n  Interactions the docs say METHOD 1 should have dropped at threshold=0.99")
print("  (an interaction is only 'expressed' if BOTH partners exceed the threshold):")
ref_flag = T.interaction_pcts(pcts, T.cluster_pairs_of(np.array(T.CELL_TYPES)), 0.99)
kept_but_should_drop = int(((ref_flag.to_numpy() == 0) & (a.loc[ref_flag.index].to_numpy() > 0)).sum())
print("      %d of %d cells of the means table carry a non-zero mean that the threshold rule"
      " excludes" % (kept_but_should_drop, ref_flag.size))

print("\nMETHOD 2 (cpdb_statistical_analysis_method) on the same data, for contrast")
sig = {}
for thr in (0.1, 0.99):
    r = cpdb_statistical_analysis_method.call(
        cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp,
        counts_data="ensembl", output_path=os.path.join(tmp, "m2_%s" % thr), iterations=100,
        threshold=thr, threads=1, debug_seed=0, result_precision=3, pvalue=0.05, separator="|",
        output_suffix="run")
    s = r["significant_means"].set_index("interacting_pair")
    sig[thr] = s[[c for c in s.columns if "|" in c]].notna().to_numpy().sum()
print("  significant_means entries kept: threshold=0.1 -> %d, threshold=0.99 -> %d"
      % (sig[0.1], sig[0.99]))
print("  -> the threshold works in METHOD 2 (through significant_means, which METHOD 2 returns"
      " and writes),\n     and is inert in METHOD 1 because METHOD 1 discards that table.")
