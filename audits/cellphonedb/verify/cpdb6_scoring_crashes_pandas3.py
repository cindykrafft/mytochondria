#!/usr/bin/env python3
"""CPDB6: `score_interactions=True` fails on pandas >= 3 (and on pandas 2 with copy-on-write
enabled), because the index rewrite it depends on is a chained inplace assignment.

`heteromer_geometric_expression_per_cell_type` (scoring_utils.py:135-140) converts the mean
expression matrix's index from multidata ids to gene names:

    if matrix.index.intersection(genes[counts_data]).empty:
        index_name = matrix.index.name
        matrix = matrix.reset_index()
        matrix[index_name].replace(to_replace=id2name, inplace=True)   # <-- no-op under CoW
        matrix.set_index(index_name, inplace=True)

`matrix[index_name].replace(..., inplace=True)` mutates a temporary Series, not `matrix`. Under
pandas' copy-on-write semantics -- opt-in in 2.x, the only behaviour in 3.0 -- the write is
discarded (pandas raises ChainedAssignmentError as a warning). The index therefore stays as
integer multidata ids, the very next line

    idx = [gene in list(genes[counts_data]) for gene in matrix.index]

selects nothing, and the empty matrix reaches `scale_expression`, where MinMaxScaler raises
"ValueError: at least one array or dtype is required" -- an error that names neither the
scoring step nor the cause.

The package requires only `pandas = ">=1.5.0"` (pyproject.toml), so a fresh install today gets
pandas 3.x. Scoring is the headline feature of v5 ("A scoring methodology to rank interaction
based on the expression specificity of the interacting partners") and is enabled in all three
tutorial notebooks. The project's CI pins Python 3.8 (.github/workflows/python-app.yml), which
cannot install pandas 3, so `test_basic_method` -- which passes `score_interactions=True` --
still passes there.

Run this under both a pandas>=3 and a pandas<3 environment; it reports which it is in.
"""
import os
import sys
import tempfile
import traceback
import warnings
import numpy as np
import pandas as pd
from importlib.metadata import version

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tiny_dataset as T

from cellphonedb.src.core.methods import cpdb_statistical_analysis_method
from cellphonedb.utils import scoring_utils

print("cellphonedb %s   pandas %s   numpy %s"
      % (version("cellphonedb"), pd.__version__, np.__version__))
try:
    cow = pd.options.mode.copy_on_write
except Exception:
    cow = "n/a (pandas 3: always on)"
print("pandas copy_on_write:", cow)

# ---- the mechanism, in three lines of pandas -------------------------------------------------
df = pd.DataFrame({"i": [1, 2, 3], "v": [10.0, 20.0, 30.0]})
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    df["i"].replace(to_replace={1: "A", 2: "B", 3: "C"}, inplace=True)
print("\nmechanism: df['i'].replace({1:'A',...}, inplace=True) leaves column 'i' as", list(df["i"]))
print("           (the replacement took effect: %s)" % (list(df["i"]) == ["A", "B", "C"]))

# ---- end to end through the public API --------------------------------------------------------
tmp = tempfile.mkdtemp(prefix="cpdb6_")
db = T.build_db(os.path.join(tmp, "db"))
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"))
print("\ncalling cpdb_statistical_analysis_method.call(..., score_interactions=True)")
try:
    res = cpdb_statistical_analysis_method.call(
        cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp,
        counts_data="ensembl", output_path=os.path.join(tmp, "out"), iterations=100,
        threshold=0.1, threads=1, debug_seed=0, result_precision=3, pvalue=0.05, separator="|",
        output_suffix="run", score_interactions=True)
    sc = res["interaction_scores"]
    cols = [c for c in sc.columns if "|" in c]
    print("RESULT: completed. interaction_scores shape %s, non-zero entries %d"
          % (sc[cols].shape, int((sc[cols].astype(float).to_numpy() > 0).sum())))
    print(sc.set_index("interacting_pair")[cols].to_string())
except Exception:
    print("RESULT: raised ->")
    traceback.print_exc(file=sys.stdout)

# ---- isolate the failing step ------------------------------------------------------------------
print("\nthe failing step in isolation (heteromer_geometric_expression_per_cell_type):")
from cellphonedb.utils import db_utils
interactions, genes, cc, ce, _syn, _tf = db_utils.get_interactions_genes_complex(db)
from collections import ChainMap
id2name = dict(ChainMap(dict(zip(genes.protein_id, genes["gene_name"])),
                        dict(zip(ce.complex_multidata_id, ce.name))))
mean_by_ct = pd.DataFrame({"CTA": [3.0, 0.33, 1.0, 2.0, 0.0], "CTB": [0.33, 2.0, 3.0, 1.0, 2.0]},
                          index=pd.Index([0, 1, 2, 3, 4], name="id_multidata"))
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    out = scoring_utils.heteromer_geometric_expression_per_cell_type(
        matrix=mean_by_ct, counts_data="gene_name", genes=genes, complex_composition=cc,
        complex_expanded=ce, id2name=id2name)
print("   input rows : %d (index %s)" % (len(mean_by_ct), list(mean_by_ct.index)))
print("   output rows: %d (index %s)" % (len(out), list(out.index)))
print("   -> expected 5 genes + 2 complexes; an empty frame here is the defect, and it is what")
print("      reaches MinMaxScaler.")
