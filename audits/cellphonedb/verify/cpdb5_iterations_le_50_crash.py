#!/usr/bin/env python3
"""CPDB5: `threads=1` with `iterations <= 50` raises ZeroDivisionError before any analysis runs.

The single-threaded branch of `shuffled_analysis`
(cpdb_statistical_analysis_helper.py:479-492) computes a progress step and takes a modulus by
it:

    progress_step = round(iterations / 100, 0)
    for i in range(iterations):
        ...
        if i % progress_step == 0:

`round(iterations/100, 0)` is 0.0 for every iterations <= 50 (0.5 rounds to 0 under banker's
rounding), so the modulus raises. Only the threads=1 path is affected; the pooled path has no
progress_step. threads=1 is not an exotic setting -- the comment directly above this branch
recommends it as the only option when the package is driven from R/RStudio on Windows
(referencing issue #102), and the DEG and simple methods take a `threads` argument too.

Below: the boundary is mapped arithmetically, then the crash is reproduced end to end through
the public API with the complete traceback.
"""
import os
import sys
import tempfile
import traceback
from importlib.metadata import version

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tiny_dataset as T

from cellphonedb.src.core.methods import cpdb_statistical_analysis_method

print("cellphonedb", version("cellphonedb"))
print("\nprogress_step = round(iterations/100, 0) in the threads=1 branch:")
for it in (1, 5, 10, 25, 49, 50, 51, 100, 1000):
    ps = round(it / 100, 0)
    print("   iterations=%-5d progress_step=%-5s %s"
          % (it, ps, "-> ZeroDivisionError" if ps == 0 else "ok"))

tmp = tempfile.mkdtemp(prefix="cpdb5_")
db = T.build_db(os.path.join(tmp, "db"))
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"))

for iterations, threads in ((10, 1), (10, 4), (51, 1)):
    print("\n=== iterations=%d, threads=%d ===" % (iterations, threads))
    try:
        res = cpdb_statistical_analysis_method.call(
            cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp,
            counts_data="ensembl", output_path=os.path.join(tmp, "out"), iterations=iterations,
            threshold=0.1, threads=threads, debug_seed=0, result_precision=3, pvalue=0.05,
            separator="|", output_suffix="i%d_t%d" % (iterations, threads))
        print("completed; pvalues shape", res["pvalues"].shape)
    except Exception:
        traceback.print_exc(file=sys.stdout)
