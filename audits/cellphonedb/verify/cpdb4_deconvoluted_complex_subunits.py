#!/usr/bin/env python3
"""CPDB4: in deconvoluted.txt and deconvoluted_percents.txt, every subunit row of a heteromeric
complex carries the COMPLEX's minimum, not that subunit's own mean / percent.

`deconvolute_complex_interaction_component` (cpdb_statistical_analysis_complex_method.py:366-371)
fills each subunit row's `multidata_id` from `complex_multidata_id` while filling `gene_name`
from the subunit:

    deconvoluted_result[['multidata_id', 'protein_name', 'gene_name', ...]] = \\
        deconvolution_complex[['complex_multidata_id', 'protein_name_simple',
                               'gene_name_simple', ...]]

`deconvoluted_complex_result_build` (lines 292-304) then indexes by `multidata_id` and joins the
per-cluster tables:

    deconvoluted_result.set_index('multidata_id', inplace=True, drop=True)
    deconvoluted_result = pd.concat([deconvoluted_result,
                                     clusters_means.reindex(deconvoluted_result.index)], ...)

`clusters_means` is indexed by multidata id and contains a row per complex holding the minimum
over its subunits (build_clusters, helper.py:154-159). So the join attaches the complex's
minimum to a row labelled with the subunit's gene name, and every subunit of a complex shows
the same numbers.

What the documentation says these columns are
(docs/RESULTS-DOCUMENTATION.md, "Deconvoluted (deconvoluted.txt)"):

    gene_name: Gene identifier for one of the subunits that are participating in the
               interaction ...
    mean:      Mean expression of the corresponding gene in each cluster.

and for the percentages file: "this file denotes the percentage of cells expressing a given
gene". This is also the file the docs point users at to check heteromers: "This is important as
some of the interacting partners are heteromers. In other words, multiple molecules have to be
expressed in the same cluster in order for the interacting partner to be functional." -- which
the file cannot show if every subunit reports the same minimum.
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

tmp = tempfile.mkdtemp(prefix="cpdb4_")
db = T.build_db(os.path.join(tmp, "db"))
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"))
pd.set_option("display.width", 250)

res = cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp, counts_data="ensembl",
    output_path=os.path.join(tmp, "out"), iterations=100, threshold=0.1, threads=1, debug_seed=0,
    result_precision=3, pvalue=0.05, separator="|", output_suffix="run")

ct = ["CTA", "CTB", "CTC"]
means, pcts = T.cluster_means_pcts(T.COUNTS, np.array(T.CELL_TYPES))
print("cellphonedb", version("cellphonedb"))
print("\nTrue per-gene cluster means of the fixture (each gene's own mean over its cluster):")
print(means.loc[["LIG1", "REC1", "SUB1", "SUB2", "LIG2"], ct].round(4).to_string())
print("\nComplex minima (what build_clusters stores for the complex rows):")
print(means.loc[["RECCPLX", "BIGCPLX"], ct].round(4).to_string())

dec = res["deconvoluted"]
decp = res["deconvoluted_percents"]
print("\ndeconvoluted.txt as written by the shipped run:")
print(dec[["gene_name", "uniprot", "is_complex", "complex_name", "id_cp_interaction"] + ct]
      .to_string(index=False))
print("\ndeconvoluted_percents.txt as written by the shipped run:")
print(decp[["gene_name", "complex_name"] + ct].to_string(index=False))

print("\nsubunit rows, reported vs the subunit's own value:")
print("  %-8s %-9s %-24s %-24s %s" % ("gene", "complex", "reported mean", "own mean", "wrong?"))
bad = 0
for _i, row in dec[dec["is_complex"]].drop_duplicates(
        subset=["gene_name", "complex_name"]).iterrows():
    g, cx = row["gene_name"], row["complex_name"]
    rep = [round(float(row[c]), 3) for c in ct]
    own = [round(float(means.at[g, c]), 3) for c in ct]
    mism = rep != own
    bad += mism
    print("  %-8s %-9s %-24s %-24s %s" % (g, cx, rep, own, "YES" if mism else "no"))
print("\n  %d subunit rows report a mean that is not the gene's mean." % bad)

print("\nsubunit rows, reported vs the subunit's own percent:")
print("  %-8s %-9s %-24s %-24s %s" % ("gene", "complex", "reported pct", "own pct", "wrong?"))
badp = 0
for _i, row in decp[decp["complex_name"].notna()].drop_duplicates(
        subset=["gene_name", "complex_name"]).iterrows():
    g, cx = row["gene_name"], row["complex_name"]
    rep = [round(float(row[c]), 3) for c in ct]
    own = [round(float(pcts.at[g, c]), 3) for c in ct]
    mism = rep != own
    badp += mism
    print("  %-8s %-9s %-24s %-24s %s" % (g, cx, rep, own, "YES" if mism else "no"))
print("\n  %d subunit rows report a percent that is not the gene's percent." % badp)

print("\nWorked example: SUB1 is expressed at mean 3.0 in CTB (every cell of CTB expresses it),")
print("but deconvoluted.txt reports 1.0 for SUB1 in CTB, because RECCPLX's minimum over")
print("(SUB1=3.0, SUB2=1.0) is 1.0. A reader checking 'is SUB1 expressed in CTB?' is shown")
print("its partner's value. Simple (non-complex) rows are unaffected:")
simple = dec[~dec["is_complex"]].drop_duplicates(subset=["gene_name"])
ok = all(round(float(r[c]), 3) == round(float(means.at[r["gene_name"], c]), 3)
         for _i, r in simple.iterrows() for c in ct)
print("  all %d simple rows report the gene's own mean: %s" % (len(simple), ok))
