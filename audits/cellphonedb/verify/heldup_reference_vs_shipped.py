#!/usr/bin/env python3
"""Held-up check: an independent numpy port of the documented method vs the shipped package.

Runs `cpdb_statistical_analysis_method.call` (threads=1, debug_seed=0) on the 9-cell fixture in
tiny_dataset.py and compares EVERY number it produces with a from-scratch reference:

  A. cluster means            mean over all cells of the cluster, zeros included
  B. cluster percents         fraction of the cluster's cells with value > 0, per gene
  C. complex summarisation    minimum over subunits, taken AFTER per-subunit averaging
  D. interaction mean         (mean_a + mean_b)/2, set to 0 if either cluster mean is 0
  E. threshold rule           1 iff both partners' percents are > threshold (strict)
  F. permutation p-values     replicating the package's own shuffles from the same seed
  G. significant_means        mean where p <= pvalue, NaN otherwise; rank = non-NaN / n columns

The hand-computed values in the fixture docstring are asserted directly (part A/C), so this is
not a self-consistency check: the cluster means and complex minima are known by hand.

Part F replicates the package's permutations exactly (same seed, same Fisher-Yates draws) to
establish what the code computes. What the DOCUMENTED estimator would give on the same
permutations is the subject of cpdb2_pvalue_ties_and_zero.py.
"""
import os
import sys
import tempfile
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tiny_dataset as T

from cellphonedb.src.core.methods import cpdb_statistical_analysis_method
from importlib.metadata import version

ITERATIONS, SEED, THRESHOLD, PVALUE = 200, 0, 0.1, 0.05
tmp = tempfile.mkdtemp(prefix="cpdb_heldup_")
db = T.build_db(os.path.join(tmp, "db"))
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"))
out = os.path.join(tmp, "out")

print("cellphonedb", version("cellphonedb"))
print("fixture: 5 genes x 9 cells, 3 cell types x 3 cells, 2 complexes, 4 interactions")
print("iterations=%d debug_seed=%d threads=1 threshold=%.2f pvalue=%.2f\n"
      % (ITERATIONS, SEED, THRESHOLD, PVALUE))

res = cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp,
    counts_data="ensembl", output_path=out, iterations=ITERATIONS, threshold=THRESHOLD,
    threads=1, debug_seed=SEED, result_precision=3, pvalue=PVALUE, separator="|",
    output_suffix="run")

labels = np.array(T.CELL_TYPES)
pairs = T.cluster_pairs_of(labels)
cols = ["{}|{}".format(a, b) for a, b in pairs]

# ---- A/B/C: cluster means and percents, against hand-written values ----------------------
means, pcts = T.cluster_means_pcts(T.COUNTS, labels)
hand_means = {"LIG1": [3.0, 1 / 3, 0.0], "REC1": [1 / 3, 2.0, 1 / 3], "SUB1": [1.0, 3.0, 2 / 3],
              "SUB2": [2.0, 1.0, 2.0], "LIG2": [0.0, 2.0, 4.0],
              "RECCPLX": [1.0, 1.0, 2 / 3], "BIGCPLX": [0.0, 1.0, 1 / 3]}
hand_pcts = {"LIG1": [1.0, 1 / 3, 0.0], "REC1": [1 / 3, 1.0, 1 / 3], "SUB1": [1.0, 1.0, 1 / 3],
             "SUB2": [1.0, 1.0, 2 / 3], "LIG2": [0.0, 1.0, 1.0],
             "RECCPLX": [1.0, 1.0, 1 / 3], "BIGCPLX": [0.0, 1.0, 1 / 3]}
for name, vals in hand_means.items():
    np.testing.assert_allclose(means.loc[name].to_numpy(), vals, atol=1e-12)
for name, vals in hand_pcts.items():
    np.testing.assert_allclose(pcts.loc[name].to_numpy(), vals, atol=1e-12)
print("A/C  reference cluster means match the hand-computed table (incl. complex minima):")
print(means.round(4).to_string(), "\n")
print("B    reference cluster percents match the hand-computed table:")
print(pcts.round(4).to_string(), "\n")

# the package's own per-gene means/percents, for the simple (non-complex) genes: the
# deconvoluted output. (Its rows for COMPLEX SUBUNITS are the subject of CPDB4 and are
# excluded here.)
dec = res["deconvoluted"]
dec = dec[~dec["is_complex"]].drop_duplicates(subset=["gene_name"]).set_index("gene_name")
decp = res["deconvoluted_percents"]
decp = decp[decp["complex_name"].isna()].drop_duplicates(subset=["gene_name"]).set_index("gene_name")
ct = sorted(set(labels))
d_mean = np.abs(dec[ct].to_numpy(float) - means.loc[dec.index, ct].to_numpy()).max()
d_pct = np.abs(decp[ct].to_numpy(float) - pcts.loc[decp.index, ct].to_numpy()).max()
print("     shipped deconvoluted means (simple genes) vs reference: max |diff| = %.2e" % d_mean)
print("     shipped deconvoluted pcts  (simple genes) vs reference: max |diff| = %.2e\n" % d_pct)

# ---- D/E: interaction means and the threshold rule ----------------------------------------
ref_mean = T.interaction_means(means, pairs)
ref_pct = T.interaction_pcts(pcts, pairs, THRESHOLD)
ship_mean = res["means"].set_index("interacting_pair")[cols].astype(float)
ship_mean = ship_mean.loc[ref_mean.index]
d = np.abs(ship_mean.to_numpy() - ref_mean.to_numpy().round(3)).max()
print("D    interaction means (x>0)*(y>0)*(x+y)/2, shipped vs reference: max |diff| = %.2e" % d)
print(ref_mean.round(3).to_string(), "\n")
print("E    threshold flags (both percents > %.2f), reference:" % THRESHOLD)
print(ref_pct.to_string(), "\n")

# ---- F: p-values, on the permutations the package actually drew ----------------------------
# The p-value rule is checked on a CONTINUOUS-valued version of the fixture. On the integer
# fixture the permutation null puts several percent of its mass exactly on the observed value
# (see cpdb2_pvalue_ties_and_zero.py), and those ties are decided by float32 rounding, so a
# float64 reference cannot be expected to agree bit for bit. With continuous values ties have
# probability ~0 and the counting rule can be verified exactly. The package's own shuffles are
# recorded rather than re-derived from the seed, so no assumption about the RNG is needed.
from cellphonedb.src.core.methods import cpdb_statistical_analysis_helper as H

rng = np.random.default_rng(7)
cont = np.round(rng.random((5, 9)) * 4 + 0.5, 6)
cont[0, 6:] = 0.0            # keep a zero cluster mean so the (x>0)(y>0) rule is exercised
cont[4, :3] = 0.0
cfp, mfp, _ = T.write_inputs(os.path.join(tmp, "in_cont"), counts=cont)

drawn = []
_orig = H.shuffle_meta
H.shuffle_meta = lambda meta: (lambda out: (drawn.append(list(out["cell_type"])), out)[1])(_orig(meta))
res_c = cpdb_statistical_analysis_method.call(
    cpdb_file_path=db, meta_file_path=mfp, counts_file_path=cfp, counts_data="ensembl",
    output_path=os.path.join(tmp, "out_cont"), iterations=ITERATIONS, threshold=THRESHOLD,
    threads=1, debug_seed=SEED, result_precision=3, pvalue=PVALUE, separator="|",
    output_suffix="cont")
H.shuffle_meta = _orig

cmeans, cpcts = T.cluster_means_pcts(cont, labels)
cobs = T.interaction_means(cmeans, pairs)
cflag = T.interaction_pcts(cpcts, pairs, THRESHOLD)
count = np.zeros(cobs.shape)
for lab in drawn:
    m, _p = T.cluster_means_pcts(cont, np.array(lab))
    count += T.interaction_means(m, pairs).to_numpy() > cobs.to_numpy()
ref_p = count / len(drawn)
ref_p[(cobs.to_numpy() == 0) | (cflag.to_numpy() == 0)] = 1.0
ref_p = pd.DataFrame(ref_p, index=cobs.index, columns=cobs.columns)
ship_p = res_c["pvalues"].set_index("interacting_pair")[cols].astype(float).loc[ref_p.index]
print("F    p-values on a continuous (tie-free) fixture, over the %d shuffles the package drew:"
      % len(drawn))
print("     rule reproduced: p = #(shuffled mean > observed) / iterations, with p forced to 1")
print("     where the observed mean is 0 or the threshold flag is 0")
print("     max |shipped - reference| = %.2e   exact match: %s"
      % (np.abs(ship_p.to_numpy() - ref_p.to_numpy()).max(),
         np.array_equal(ship_p.to_numpy(), ref_p.to_numpy())))
print(ship_p.to_string(), "\n")

# ---- G: significant_means and rank (on the same continuous run) -----------------------------
ref_sig = cobs.where(ref_p <= PVALUE).round(3)
ref_rank = (ref_sig.notna().sum(axis=1) / len(cols)).round(3)
sm = res_c["significant_means"].set_index("interacting_pair")
ship_sig = sm[cols].astype(float).loc[ref_sig.index]
same = ((ship_sig.isna() == ref_sig.isna()) &
        (ship_sig.fillna(0).round(3) == ref_sig.fillna(0).round(3))).all().all()
print("G    significant_means (mean where p <= %.2f else NaN): identical to reference: %s"
      % (PVALUE, same))
print(ship_sig.to_string())
print("\n     rank (non-NaN / %d columns), shipped vs reference:" % len(cols))
print(pd.DataFrame({"shipped": sm.loc[ref_rank.index, "rank"],
                    "reference": ref_rank}).to_string())

print("\nFiles written by the run:")
for f in sorted(os.listdir(out)):
    print("   ", f)
