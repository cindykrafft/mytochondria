#!/usr/bin/env python3
"""CPDB2: the permutation p-value counts only shuffles STRICTLY greater than the observed mean,
and never counts the observed configuration, so it is smaller than the documented p-value and
can be exactly 0.

The code (cpdb_statistical_analysis_helper.py:537-539, 611-613):

    np.packbits(shuffled_mean_analysis.values > real_mean_analysis.values, axis=None)
    ...
    percent_result += np.unpackbits(...); percent_result /= len(statistical_mean_analysis)

i.e. p = #{shuffles with mean > observed} / iterations.

The documentation says otherwise, in both places it states the rule:
  docs/RESULTS-DOCUMENTATION.md:62   "the proportion of the means that are as high as or higher
                                      than the actual mean"
  docs/RESULTS-DOCUMENTATION.md:104  "By calculating the proportion of the means which are equal
                                      or higher than the actual mean"
which is also the estimator of the CellPhoneDB v2 protocol paper.

The fixture has 9 cells in three groups of three, so the permutation null has 9!/(3!)^3 = 1680
distinct label assignments and can be enumerated EXHAUSTIVELY. The enumeration below is run
through the package's OWN `build_clusters` / `mean_analysis` (the same calls `_statistical_
analysis` makes for each shuffle, minus the shuffling), so the arithmetic -- float32 cluster
means from numpy_groupies, the complex minimum, the (x>0)(y>0)(x+y)/2 rule -- is identical to a
real run and nothing here depends on a reimplementation.

Reported:
  A. the exact null: p under the shipped rule (>) and under the documented rule (>=), and the
     tie mass between them, all in the package's own arithmetic;
  B. how many entries change significance at pvalue=0.05;
  C. what a real 20,000-iteration run reports, confirming it estimates the shipped rule;
  D. p == 0, which the documented rule cannot produce (the observed labelling is itself one of
     the 1680 assignments and always ties with itself, giving a floor of 1/1680).
"""
import itertools
import os
import sys
import tempfile
import numpy as np
import pandas as pd
from importlib.metadata import version

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tiny_dataset as T

from cellphonedb.src.core.methods import cpdb_statistical_analysis_helper as H
from cellphonedb.src.core.methods import cpdb_statistical_analysis_method
from cellphonedb.src.core.models.complex import complex_helper
from cellphonedb.utils import db_utils, file_utils

THRESHOLD, PVALUE, SEP = 0.1, 0.05, "|"
tmp = tempfile.mkdtemp(prefix="cpdb2_")
db = T.build_db(os.path.join(tmp, "db"))
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"))

print("cellphonedb", version("cellphonedb"))

# ---- set the analysis up exactly as cpdb_statistical_analysis_complex_method.call does -----
interactions, genes, complex_composition, complex_expanded, syn, _tf = \
    db_utils.get_interactions_genes_complex(db)
counts, meta, microenvs, _degs, _tfs = file_utils.get_user_files(
    counts=counts_fp, meta_fp=meta_fp, gene_synonym2gene_name=syn, counts_data="ensembl")
counts, counts_relations = H.add_multidata_and_means_to_counts(counts, genes, "ensembl")
interactions_reduced = interactions[["multidata_1_id", "multidata_2_id"]].drop_duplicates()
interactions_filtered, counts_filtered, ccf = H.prefilters(
    interactions_reduced, counts, complex_expanded, complex_composition)
meta = meta.loc[counts.columns]
meta["cell_type"] = meta["cell_type"].apply(str)
c2p = complex_helper.map_complex_to_protein_row_ids(ccf, counts_filtered)

clusters = H.build_clusters(meta, counts_filtered, c2p, skip_percent=False)
combos = H.get_cluster_combinations(clusters["names"], pd.DataFrame())
obs = H.mean_analysis(interactions_filtered, clusters, combos, SEP)
flag = H.percent_analysis(clusters, THRESHOLD, interactions_filtered, combos, SEP)
label_of = dict(zip(interactions_filtered.index,
                    H.interacting_pair_build(
                        interactions.loc[interactions_filtered.index].merge(
                            counts_relations, how="left", left_on="multidata_1_id",
                            right_on="id_multidata").drop("id_multidata", axis=1).merge(
                            counts_relations, how="left", left_on="multidata_2_id",
                            right_on="id_multidata", suffixes=("_1", "_2")).set_index(
                            interactions_filtered.index))))
rows = [label_of[i] for i in obs.index]
cols = list(obs.columns)

# ---- A: exhaustive enumeration of the null, through the package's own functions -------------
cells = list(range(9))
assignments = []
for a in itertools.combinations(cells, 3):
    rest = [c for c in cells if c not in a]
    for b in itertools.combinations(rest, 3):
        c = tuple(x for x in rest if x not in b)
        lab = np.empty(9, dtype=object)
        lab[list(a)], lab[list(b)], lab[list(c)] = "CTA", "CTB", "CTC"
        assignments.append(lab)
print("exhaustive permutation null: %d distinct label assignments of 9 cells into 3x3\n"
      % len(assignments))

obs_v = obs.to_numpy()
n_gt = np.zeros(obs_v.shape)
n_eq = np.zeros(obs_v.shape)
for lab in assignments:
    m2 = meta.copy()
    m2["cell_type"] = pd.Categorical(list(lab))
    cl = H.build_clusters(m2, counts_filtered, c2p, skip_percent=True)
    s = H.mean_analysis(interactions_filtered, cl, combos, SEP).to_numpy()
    n_gt += s > obs_v
    n_eq += s == obs_v                      # exact equality, in the package's own float32
N = len(assignments)

mask = (obs_v == 0) | (flag.to_numpy() == 0)      # forced to p = 1 by build_percent_result
p_code = np.where(mask, 1.0, n_gt / N)
p_doc = np.where(mask, 1.0, (n_gt + n_eq) / N)
ties = np.where(mask, 0.0, n_eq / N)
F = lambda a: pd.DataFrame(a, index=rows, columns=cols)

print("A. exact p over all 1680 permutations, estimator the code implements  #(mean > obs)/1680")
print(F(p_code).round(4).to_string())
print("\n   exact p under the documented rule                    #(mean >= obs)/1680")
print(F(p_doc).round(4).to_string())
print("\n   difference = tie mass                                #(mean == obs)/1680")
print(F(ties).round(4).to_string())
tested = ~mask
print("\n   over the %d tested entries: tie mass min %.4f, median %.4f, max %.4f"
      % (tested.sum(), ties[tested].min(), np.median(ties[tested]), ties[tested].max()))

# ---- B: significance flips -----------------------------------------------------------------
flip = (p_doc <= PVALUE) != (p_code <= PVALUE)
print("\nB. entries whose call at pvalue <= %.2f differs between the two estimators: %d of %d"
      % (PVALUE, int(flip.sum()), int(tested.sum())))
for i, j in zip(*np.nonzero(flip)):
    print("      %-14s %-9s  documented p=%.4f -> not significant;  shipped p=%.4f -> SIGNIFICANT"
          % (rows[i], cols[j], p_doc[i, j], p_code[i, j]))

# ---- C: a real run estimates the shipped rule ----------------------------------------------
res = cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp, counts_data="ensembl",
    output_path=os.path.join(tmp, "out"), iterations=20000, threshold=THRESHOLD, threads=1,
    debug_seed=-1, result_precision=3, pvalue=PVALUE, separator=SEP, output_suffix="run")
ship = res["pvalues"].set_index("interacting_pair")[cols].astype(float).loc[rows].to_numpy()
se = 1 / np.sqrt(20000)
print("\nC. a real run (iterations=20000, threads=1) reports:")
print(F(ship).to_string())
print("\n   max |run - exact shipped-rule p|  = %.4f   (2 x binomial se = %.4f)"
      % (np.abs(ship - p_code).max(), 2 * se))
print("   max |run - exact documented p|    = %.4f" % np.abs(ship - p_doc).max())
print("   -> the run estimates the strict-inequality quantity. The gap to the documented\n"
      "      value is the estimand, not Monte-Carlo noise.")

# ---- D: p == 0 -----------------------------------------------------------------------------
z = (ship == 0) & tested
print("\nD. entries the run reports as p == 0: %d" % int(z.sum()))
for i, j in zip(*np.nonzero(z)):
    print("      %-14s %-9s  reported p = 0.0 ;  exact documented p = %.4f ;  floor 1/1680 = %.6f"
          % (rows[i], cols[j], p_doc[i, j], 1 / N))
print("\n   The documented 'equal or higher' rule cannot return 0 -- the observed labelling is\n"
      "   itself one of the 1680 assignments and ties with itself -- and the standard\n"
      "   permutation correction (b+1)/(m+1) has a floor of 1/(iterations+1). Downstream\n"
      "   plotting turns p = 0 into -log10(p) = inf.")

# ---- footnote: float32 splits some mathematically-tied permutations -------------------------
lab0 = np.array(T.CELL_TYPES)
pairs = T.cluster_pairs_of(lab0)
ref_obs = T.interaction_means(T.cluster_means_pcts(T.COUNTS, lab0)[0], pairs).to_numpy()
n_eq64 = np.zeros(ref_obs.shape)
for lab in assignments:
    s = T.interaction_means(T.cluster_means_pcts(T.COUNTS, lab)[0], pairs).to_numpy()
    n_eq64 += np.isclose(s, ref_obs, rtol=0, atol=1e-12)
print("\nE. footnote on arithmetic: cluster means are float32 (counts are cast to float32 by\n"
      "   counts_preprocessor, and numpy_groupies returns float32), so permutations that are\n"
      "   mathematically tied with the observed value can land on either side of the strict\n"
      "   comparison by ~1e-7 of rounding noise.")
print("   tie mass counted in exact arithmetic (float64): median %.4f, max %.4f"
      % (np.median((n_eq64 / N)[tested]), (n_eq64 / N)[tested].max()))
print("   tie mass seen by the shipped float32 comparison: median %.4f, max %.4f"
      % (np.median(ties[tested]), ties[tested].max()))
print("   -> part of the tied mass is already split arbitrarily by rounding before the\n"
      "      strict-vs-inclusive question is even reached.")
