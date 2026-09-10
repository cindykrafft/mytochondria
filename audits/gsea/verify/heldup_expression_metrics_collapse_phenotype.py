#!/usr/bin/env python3
"""Held-up checks on the expression-dataset tool (xtools.gsea.Gsea) with synthetic data
(3,000 probes x 16 samples, 8 vs 8, 200 planted DE genes, low-variance and constant
blocks; see synth.expression_dataset):

A. Ranking metrics.  The ranked_gene_list_*.tsv the run writes (Float.toString, full
   float precision) against ref_gsea for Signal2Noise (default; minimum-sd rule
   sd >= 0.2*|mu|, 0.2 at mu = 0), tTest, Ratio_of_Classes, log2_Ratio_of_Classes and
   Diff_of_Classes, plus the rank order (descending, ties in input row order) and which
   class is "A".
B. Probe collapse.  A .chip that maps 3,000 probes to 1,000 symbols (1, 2 or 5 probes per
   symbol, one symbol with a missing probe value); the collapsed GCT that `-create_gcts
   true` writes against the port for Max_probe (default), Median_of_probes,
   Mean_of_probes, Sum_of_probes and Abs_max_of_probes.
C. Phenotype permutation.  `-permute phenotype -save_rnd_lists true`: every saved random
   ranked list must be the S2N ranking under some relabelling with the class sizes
   preserved (checked: each is a valid S2N vector of the data under the relabelling that
   the harness recovers by matching the per-gene scores), and the RND_ES of every set
   equals the port's ES on that list.  Also the NES/p/FDR arithmetic on this null.

Run: python3 heldup_expression_metrics_collapse_phenotype.py   (GSEA_CP selects the jar)
"""
import glob
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsea_cli as G  # noqa: E402
import ref_gsea as R  # noqa: E402
import synth  # noqa: E402

W = "/tmp/gseawork/heldup_expr"
os.makedirs(W, exist_ok=True)
names, X, labels, rng = synth.expression_dataset()
n, m = X.shape
G.write_gct(f"{W}/data.gct", names, X)
G.write_cls(f"{W}/pheno.cls", labels, ("A", "B"))
# gene sets on probe ids: planted UP_IN_A (from the +2 block), DOWN_IN_A, random ones
gs = {"UP_IN_A": names[:40], "DOWN_IN_A": names[100:140], "LOWVAR": names[200:230]}
for k in range(12):
    gs[f"RND{k}"] = list(rng.choice(names, 30 + 10 * k, replace=False))
G.write_gmt(f"{W}/sets.gmt", gs)
print("jar/classpath:", G.GSEA_CP)
print(f"dataset {n} x {m}, class A = first 8 samples")

# ------------------------------------------------------------------ A: metrics
for metric in ("Signal2Noise", "tTest", "Ratio_of_Classes", "log2_Ratio_of_Classes", "Diff_of_Classes"):
    d = G.run_gsea(f"{W}/data.gct", f"{W}/pheno.cls", f"{W}/sets.gmt", f"{W}/out_{metric}",
                   nperm=10, permute="gene_set", metric=metric)
    rn, rs = G.parse_ranked_gene_list(d)
    order, s_ref = R.rank_dataset(X, labels, metric)
    # scores per gene (the tool prints float32)
    idx = {nm: i for i, nm in enumerate(names)}
    s_gsea = np.array([rs[k] for k in range(n)])
    s_ref_in_gsea_order = np.array([s_ref[idx[nm]] for nm in rn])
    finite = np.isfinite(s_ref_in_gsea_order) & np.isfinite(s_gsea)
    absd = np.abs(s_gsea - s_ref_in_gsea_order)[finite]
    rel = absd / np.maximum(np.abs(s_ref_in_gsea_order)[finite], 1e-30)
    rel[np.abs(s_ref_in_gsea_order)[finite] == 0] = absd[np.abs(s_ref_in_gsea_order)[finite] == 0]  # exact zeros: absolute
    worst = np.argmax(rel)
    # NaN scores (log2 of a negative ratio) are printed as '---' and sorted to the end.
    # Order property checked on the tool's own printed scores: non-increasing, and within a
    # block of equal printed scores the input row order is kept (stable descending sort).
    fin = np.isfinite(s_gsea)
    non_increasing = bool(np.all(np.diff(s_gsea[fin]) <= 0))
    row_of = np.array([idx[nm] for nm in rn])
    ties_in_row_order = all(row_of[k] < row_of[k + 1] for k in range(n - 1) if fin[k] and fin[k + 1] and s_gsea[k] == s_gsea[k + 1])
    nan_last = bool(np.all(~fin[np.argmax(~fin):]) ) if (~fin).any() else True
    n_tied = int(sum(1 for k in range(n - 1) if fin[k] and fin[k + 1] and s_gsea[k] == s_gsea[k + 1]))
    print(f"A. {metric:22s}: max |score_gsea - score_ref| = {absd.max():.2e}, max rel = {rel.max():.2e} at score {s_ref_in_gsea_order[finite][worst]:.6g} "
          f"(float32 output); non-finite scores gsea/ref = {(~np.isfinite(s_gsea)).sum()}/{(~np.isfinite(s_ref)).sum()} (NaN last: {nan_last}); "
          f"order non-increasing: {non_increasing}; {n_tied} tied adjacent pairs kept in row order: {ties_in_row_order}")
    if metric == "Signal2Noise":
        # class A minus class B? the +2-in-A genes must be at the top
        print(f"   top-5 ranked probes: {rn[:5]} (planted UP_IN_A = p00000..p00099 -> class A is the first cls class)")
        lv = [s_gsea[k] for k in range(n) if rn[k] in names[200:250]]
        print(f"   low-variance block (sd 0.01, mean 5): S2N range [{min(lv):.4f}, {max(lv):.4f}] "
              f"(floor 0.2*5 = 1.0 per class -> |S2N| <= ~0.02); constant block score = "
              f"{[s_gsea[k] for k in range(n) if rn[k] == names[290]][0]}")
    if metric == "tTest":
        # the floor is applied to the variance too (var = floored sd^2)
        print(f"   tTest reference uses floored sd^2/n; agreement above confirms it")

# ------------------------------------------------------------------ B: collapse
probe_to_symbol = {}
sym = 0
i = 0
pattern = itertools.cycle([1, 2, 5])
while i < n:
    k = next(pattern)
    for j in range(k):
        if i < n:
            probe_to_symbol[names[i]] = f"SYM{sym:04d}"
            i += 1
    sym += 1
G.write_chip(f"{W}/probes.chip", probe_to_symbol)
# after collapsing, the dataset rows are symbols, so the sets must name symbols
sym_list = sorted(set(probe_to_symbol.values()))
gs_sym = {f"SYMSET{k}": list(rng.choice(sym_list, 30, replace=False)) for k in range(3)}
G.write_gmt(f"{W}/sets_sym.gmt", gs_sym)
Xm = X.copy()
Xm[1, 3] = np.nan          # a missing value inside a 2-probe symbol
Xm[5, 0] = np.nan          # inside a 5-probe symbol
G.write_gct(f"{W}/data_nan.gct", names, Xm)
syms_all = [probe_to_symbol[p] for p in names]
for mode in ("Max_probe", "Median_of_probes", "Mean_of_probes", "Sum_of_probes", "Abs_max_of_probes"):
    d = G.run_gsea(f"{W}/data_nan.gct", f"{W}/pheno.cls", f"{W}/sets_sym.gmt", f"{W}/out_collapse_{mode}",
                   nperm=0, permute="gene_set", metric="Signal2Noise",
                   extra=["-collapse", "Collapse", "-mode", mode, "-chip", f"{W}/probes.chip",
                          "-include_only_symbols", "true", "-create_gcts", "true", "-set_min", "1"])
    gct = glob.glob(os.path.join(d, "edb", "*.gct"))[0]
    cn, cs, C = G.parse_gct(gct)
    syms_ref, M = R.collapse(Xm, syms_all, mode)
    pos = {s: k for k, s in enumerate(syms_ref)}
    Mref = np.array([M[pos[s]] for s in cn])
    d_abs = np.nanmax(np.abs(C - Mref))
    print(f"B. collapse {mode:18s}: {len(cn)} symbols (expected {len(syms_ref)}); max |gsea - ref| = {d_abs:.2e}; "
          f"NaN cells gsea = {np.isnan(C).sum()} ref = {np.isnan(Mref).sum()}")

# ------------------------------------------------------------------ C: phenotype permutation
d = G.run_gsea(f"{W}/data.gct", f"{W}/pheno.cls", f"{W}/sets.gmt", f"{W}/out_pheno",
               nperm=200, permute="phenotype", metric="Signal2Noise", extra=["-save_rnd_lists", "true"])
edb = G.parse_edb(d)
tsv = G.parse_report_tsv(d)
rnd_files = sorted(glob.glob(os.path.join(d, "random_ranked_lists", "*.rnk")),
                   key=lambda f: int(os.path.basename(f).split("_")[0]))
print(f"C. saved random ranked lists: {len(rnd_files)}")
# all relabellings with 8 A of 16 samples: C(16,8) = 12870 -> precompute the S2N of the first gene
# under each and match; then verify the whole vector.
combos = list(itertools.combinations(range(m), 8))
g0 = X[0]
s0 = np.array([R.signal2noise(g0[list(c)], g0[[j for j in range(m) if j not in c]]) for c in combos])
n_valid = 0
max_es_diff = 0.0
sign_ties = []   # (set, perm) where |ES| agrees but the sign differs: the two extremes tie exactly
distinct = set()
keys = list(gs)
masks = {k: np.isin(names, gs[k]) for k in keys}
for c_idx, f in enumerate(rnd_files):
    rn, rs = G.parse_edb_rnk(d) if False else (None, None)
    rn, rs = [], []
    with open(f) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            a, b = line.rstrip("\n").split("\t")[:2]
            rn.append(a)
            rs.append(float(b))
    rs = np.array(rs)
    idx = {nm: i for i, nm in enumerate(rn)}
    v0 = rs[idx[names[0]]]
    cand = np.flatnonzero(np.abs(s0 - v0) < 1e-5)
    found = None
    for ci in cand:
        lab = np.ones(m, dtype=int)
        lab[list(combos[ci])] = 0
        _, s_ref = R.rank_dataset(X, lab, "Signal2Noise")
        if np.allclose(np.array([s_ref[k] for k in range(n)]), np.array([rs[idx[nm]] for nm in names]), atol=2e-6):
            found = ci
            break
    if found is not None:
        n_valid += 1
        distinct.add(found)
    # RND_ES column c must equal the port's ES on this saved list
    for k in keys:
        es_ref, _, rsum = R.enrichment_score(rs, np.isin(rn, gs[k]), 1.0)
        got = edb[k]["rnd_es"][c_idx]
        if abs(got - es_ref) > 1e-4 and abs(abs(got) - abs(es_ref)) < 1e-4:
            sign_ties.append((k, c_idx, es_ref, got, rsum.max() + rsum.min()))
        else:
            max_es_diff = max(max_es_diff, abs(got - es_ref))
print(f"C. random lists that are exact S2N rankings under a relabelling with 8+8 classes: {n_valid} of {len(rnd_files)}; "
      f"distinct relabellings: {len(distinct)}; real labelling drawn: {tuple(range(8)) in [combos[i] for i in distinct]}")
print(f"C. max |RND_ES - ES_ref(saved list)| = {max_es_diff:.2e} (RND_ES has 4 dp) over {len(keys) * len(rnd_files)} (set, permutation) pairs")
print(f"C. pairs where |ES| agrees but the sign differs (max and min of the running sum tie exactly): {len(sign_ties)}")
for k, c, ref, got, tie in sign_ties:
    print(f"   {k} perm {c}: paper/port takes the first extreme {ref:+.4f}, GSEA reports {got:+.4f}; max + min of the running sum = {tie:.1e}")
es_real = np.array([float(tsv[k]["ES"]) for k in keys])
rnd = np.array([edb[k]["rnd_es"] for k in keys])
nes_ref = np.array([R.nes_meandiv(es_real[j], rnd[j]) for j in range(len(keys))])
np_ref = np.array([R.nominal_p(es_real[j], rnd[j]) for j in range(len(keys))])
print(f"C. NES max diff = {np.nanmax(np.abs(np.array([float(tsv[k]['NES']) for k in keys]) - nes_ref)):.2e}; "
      f"nominal p max diff = {np.nanmax(np.abs(np.array([float(tsv[k]['NOM p-val']) for k in keys]) - np_ref)):.2e}")
print("C. planted:", {k: (round(float(tsv[k]["NES"]), 3), tsv[k]["FDR q-val"]) for k in ("UP_IN_A", "DOWN_IN_A", "LOWVAR")})
