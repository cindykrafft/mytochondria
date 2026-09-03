#!/usr/bin/env python3
"""The v5 interaction-scoring path (`score_interactions=True`), ported and compared, plus one
boundary inconsistency.

docs/RESULTS-DOCUMENTATION.md, "Interaction ranking: Scoring module", states the protocol:

    1) Exclude genes not participating in any interaction and those expressed in less than k%
       of cells within a given cell type.
    2) Calculate the mean expression of each gene within each cell type.
    3) For heteromeric proteins, aggregate the mean gene expression of each subunit employing
       the geometric mean.
    4) Scale mean gene/heteromer expression across cell types between 0 and 10.
    5) Calculate the product of the scale mean expression of the interaction proteins as a
       proxy of the interaction relevance.

Part A ports those five steps to plain numpy and compares with the shipped
`interaction_scores` table. Note that step 3 uses the GEOMETRIC MEAN over subunits while the
inference methods use the MINIMUM over subunits (helper.py:156); the two halves of the package
summarise a heteromer differently. That is deliberate and both the code comment
(scoring_utils.py:158-160) and the docs say so; it is recorded here as a fact of the pipeline,
not as a defect.

Part B is the inconsistency: the scoring filter drops a gene when
`gene_expr_pct < min_pct_cell` (scoring_utils.py:52), keeping a gene whose percentage is exactly
the threshold, while `percent_analysis` requires `pct > threshold` (helper.py:453) and so
rejects it. With `threshold` set to a value a gene hits exactly, the same gene in the same cell
type is "not expressed" for the p-value/significant-mean path and "expressed" for the score.
"""
import os
import sys
import tempfile
import numpy as np
import pandas as pd
from importlib.metadata import version

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tiny_dataset as T

from cellphonedb.src.core.methods import cpdb_statistical_analysis_method

# 12 cells, three cell types of FOUR, so a gene can sit exactly on a 0.5 threshold
CELLS = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"]
CT = ["CTA"] * 4 + ["CTB"] * 4 + ["CTC"] * 4
#            CTA              CTB              CTC
COUNTS = np.array([
    [2., 3., 0., 0.,   1., 1., 1., 1.,   4., 4., 0., 0.],   # LIG1: pct .50 / 1.00 / .50
    [1., 1., 1., 1.,   2., 2., 2., 0.,   1., 0., 0., 0.],   # REC1
    [1., 1., 1., 1.,   3., 3., 3., 3.,   2., 2., 0., 0.],   # SUB1
    [2., 2., 2., 2.,   1., 1., 1., 1.,   3., 3., 3., 0.],   # SUB2
    [0., 0., 0., 0.,   1., 2., 3., 2.,   4., 4., 4., 4.],   # LIG2
])
THRESHOLD = 0.5

tmp = tempfile.mkdtemp(prefix="cpdbscore_")
db = T.build_db(os.path.join(tmp, "db"))
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"), counts=COUNTS, cells=CELLS,
                                       cell_types=CT)
print("cellphonedb", version("cellphonedb"))
res = cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp, counts_data="ensembl",
    output_path=os.path.join(tmp, "out"), iterations=200, threshold=THRESHOLD, threads=1,
    debug_seed=0, result_precision=3, pvalue=0.05, separator="|", output_suffix="run",
    score_interactions=True)

names = ["LIG1", "REC1", "SUB1", "SUB2", "LIG2"]
cts = ["CTA", "CTB", "CTC"]
pct = pd.DataFrame({c: (COUNTS[:, np.array(CT) == c] > 0).mean(axis=1) for c in cts}, index=names)
print("\nfraction of cells expressing each gene, threshold = %.2f" % THRESHOLD)
print(pct.round(4).to_string())

# ---- A: port of the five documented steps ---------------------------------------------------
filt = COUNTS.copy().astype(float)
for c in cts:                                              # step 1
    sel = np.array(CT) == c
    low = pct[c].to_numpy() < THRESHOLD                    # note: strict <, as shipped
    filt[np.ix_(low, sel)] = 0.0
mean = pd.DataFrame({c: filt[:, np.array(CT) == c].mean(axis=1) for c in cts}, index=names)  # 2
geo = {}                                                    # step 3
for cx, subs in T.COMPLEXES.items():
    geo[cx] = np.prod(mean.loc[subs].to_numpy(), axis=0) ** (1.0 / len(subs))
mat = pd.concat([mean, pd.DataFrame(geo, index=cts).T])
lo, hi = mat.min(axis=1), mat.max(axis=1)                   # step 4: MinMax per gene, 0..10
rng_ = (hi - lo).replace(0, 1.0)
scaled = ((mat.sub(lo, axis=0)).div(rng_, axis=0) * 10.0)
ref = {}                                                    # step 5
for a, b in T.INTERACTIONS:
    ref["%s_%s" % (a, b)] = {"%s|%s" % (ca, cb): round(scaled.at[a, ca] * scaled.at[b, cb], 3)
                             for ca in cts for cb in cts}
ref = pd.DataFrame(ref).T

sc = res["interaction_scores"].set_index("interacting_pair")
cols = [c for c in sc.columns if "|" in c]
ship = sc[cols].astype(float).loc[ref.index]
print("\nA. scaled expression matrix (step 4, 0-10 per gene across cell types):")
print(scaled.round(3).to_string())
print("\n   shipped interaction_scores:")
print(ship.to_string())
print("\n   reference port of the five documented steps:")
print(ref[cols].to_string())
print("\n   max |shipped - reference| = %.3f" % np.abs(ship.to_numpy() - ref[cols].to_numpy()).max())
print("   -> the documented protocol reproduces the shipped scores exactly, including the")
print("      geometric mean for complexes and the 0-10 rescaling (so the lowest-expressing")
print("      cell type of every gene scores 0 by construction, as the docs warn).")

# ---- B: the boundary --------------------------------------------------------------------------
print("\nB. genes sitting exactly on the threshold (pct == %.2f)" % THRESHOLD)
sig = res["significant_means"].set_index("interacting_pair")
pv = res["pvalues"].set_index("interacting_pair")
print("   LIG1 in CTA has pct = %.2f exactly." % pct.at["LIG1", "CTA"])
print("   scoring filter  `pct < threshold` -> %s  (gene kept, scored)"
      % (pct.at["LIG1", "CTA"] < THRESHOLD))
print("   percent_analysis `pct > threshold` -> %s  (partner counted as not expressed)"
      % (pct.at["LIG1", "CTA"] > THRESHOLD))
for pair in ["LIG1_REC1", "LIG1_RECCPLX"]:
    col = "CTA|CTB"
    print("   %-14s %-9s  p-value = %-6s significant_mean = %-6s interaction_score = %s"
          % (pair, col, pv.at[pair, col], sig.at[pair, col], sc.at[pair, col]))
print("   -> the same gene/cell type is below the bar for the significance path and above it")
print("      for the score, from one `threshold` argument.")
