#!/usr/bin/env python3
"""Three small notes on the p-value cut-off and rounding, all executed on the shipped code.

N1  `result_precision` does not apply to pvalues.txt. `build_results` rounds the means and the
    significant means (cpdb_statistical_analysis_complex_method.py:191, 219-220) but
    `result_percent` is written unrounded (line 229), so with an `iterations` that is not a
    power of ten the p-value column carries full float repr. The parameter is documented as
    "Number of decimal digits in results."  (Related, unresolved: issues #60 "Precision of
    pvalues" and #24; the maintainers' replies are not readable from this environment.)

N2  the cut-off is inclusive, not strict. `get_significant_means` masks with
    `result_percent > min_significant_mean` (helper.py:72), so an interaction whose p-value is
    exactly `pvalue` is KEPT. Both the docstring ("A p-value below which a ligand/receptor
    expression mean is considered to be statistically significant") and
    docs/RESULTS-DOCUMENTATION.md ("If p.value < 0.05, the value will be the mean") describe a
    strict comparison. p == 0.05 exactly is reachable: 50 exceedances out of 1000 iterations.

N3  `pvalue=0` silently inverts the filter. The same line is guarded by `if min_significant_mean:`
    (helper.py:71), and 0.0 is falsy, so the function takes its non-statistical branch,
    `mask = result_percent == 0`. Asking for "keep nothing" instead keeps every interaction whose
    p-value is NOT 0 -- including every p = 1 entry -- and discards exactly the most significant
    ones.
"""
import os
import re
import sys
import tempfile
import numpy as np
import pandas as pd
from importlib.metadata import version

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tiny_dataset as T

from cellphonedb.src.core.methods import cpdb_statistical_analysis_helper as H
from cellphonedb.src.core.methods import cpdb_statistical_analysis_method

tmp = tempfile.mkdtemp(prefix="cpdbnote_")
db = T.build_db(os.path.join(tmp, "db"))
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"))
print("cellphonedb", version("cellphonedb"))

# ---- N1 -------------------------------------------------------------------------------------
out = os.path.join(tmp, "n1")
cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp, counts_data="ensembl",
    output_path=out, iterations=300, threshold=0.1, threads=1, debug_seed=0, result_precision=3,
    pvalue=0.05, separator="|", output_suffix="n1")
pfile = os.path.join(out, "statistical_analysis_pvalues_n1.txt")
mfile = os.path.join(out, "statistical_analysis_means_n1.txt")
print("\nN1  iterations=300, result_precision=3")


def max_decimals(path):
    worst, ex = 0, ""
    for line in open(path).read().splitlines()[1:]:
        for tok in line.split("\t"):
            m = re.fullmatch(r"-?\d+\.(\d+)", tok)
            if m and len(m.group(1)) > worst:
                worst, ex = len(m.group(1)), tok
    return worst, ex


w, ex = max_decimals(pfile)
print("    pvalues file : longest decimal expansion = %d digits, e.g. %s" % (w, ex))
w2, ex2 = max_decimals(mfile)
print("    means file   : longest decimal expansion = %d digits, e.g. %s" % (w2, ex2))

# ---- N2 -------------------------------------------------------------------------------------
real = pd.DataFrame([[1.0, 2.0, 3.0]], index=["i1"], columns=["a|a", "a|b", "b|b"])
pct = pd.DataFrame([[0.049, 0.050, 0.051]], index=["i1"], columns=["a|a", "a|b", "b|b"])
sig = H.get_significant_means(real, pct, 0.05)
print("\nN2  get_significant_means(real, p, min_significant_mean=0.05) at the boundary")
print("      p-value :", pct.to_numpy().tolist()[0])
print("      kept    :", ["kept" if not np.isnan(v) else "dropped" for v in sig.to_numpy()[0]])
print("      -> p exactly equal to the cut-off is KEPT; the docs say 'p.value < 0.05'.")

# ---- N3 -------------------------------------------------------------------------------------
res0 = cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp, counts_data="ensembl",
    output_path=os.path.join(tmp, "n3"), iterations=200, threshold=0.1, threads=1, debug_seed=0,
    result_precision=3, pvalue=0.0, separator="|", output_suffix="n3")
sm = res0["significant_means"].set_index("interacting_pair")
pv = res0["pvalues"].set_index("interacting_pair")
cols = [c for c in pv.columns if "|" in c]
kept = sm[cols].notna().to_numpy()
p = pv[cols].astype(float).to_numpy()
print("\nN3  the same analysis run with pvalue=0.0")
print("      entries kept in significant_means      : %d of %d" % (kept.sum(), kept.size))
print("      of those, entries whose p-value is 1.0 : %d" % int((kept & (p == 1.0)).sum()))
print("      entries with p == 0 that were DROPPED  : %d" % int((~kept & (p == 0.0)).sum()))
print("      -> 'keep nothing' became 'keep everything except the most significant'.")
print("\n      for contrast, the same run with pvalue=0.05:")
res5 = cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp, counts_data="ensembl",
    output_path=os.path.join(tmp, "n3b"), iterations=200, threshold=0.1, threads=1, debug_seed=0,
    result_precision=3, pvalue=0.05, separator="|", output_suffix="n3b")
sm5 = res5["significant_means"].set_index("interacting_pair")
print("      entries kept in significant_means      : %d of %d"
      % (sm5[cols].notna().to_numpy().sum(), kept.size))
