#!/usr/bin/env python3
"""Held-up check: GseaPreranked on a synthetic ranked list (8,000 genes, 45 gene sets with
planted truth) against the independent numpy port in ref_gsea.py.

A. ES, rank-at-ES and leading edge for the three scoring schemes that use |score|
   symmetrically (classic p=0, weighted p=1 [default], weighted_p2), read from the report
   TSV (full float precision) and results.edb (exact ranks / hit indices).
B. Given GSEA's own null (RND_ES in results.edb, 1,000 gene-set permutations, 4 decimals):
   NES (mean-of-same-sign normalisation), nominal p (strict count over the same-sign null),
   FWER, and the FDR both as the code defines it (mean over permutations of the per-
   permutation fraction) and as the paper's supplement defines it (pooled fraction).
C. Sanity of the null itself: every permutation's ES is an ES of a set of the same size
   (|ES| within [0,1]) and the planted sets are called, the random ones are not.

Run: python3 heldup_preranked_vs_reference.py  (GSEA_CP selects the jar; see gsea_cli.py)
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsea_cli as G  # noqa: E402
import ref_gsea as R  # noqa: E402
import synth  # noqa: E402

W = "/tmp/gseawork/heldup_preranked"
os.makedirs(W, exist_ok=True)
names, sc, rng = synth.ranked_list(N=8000, seed=0)
gs = synth.gene_sets(names, rng)
G.write_rnk(f"{W}/list.rnk", names, sc)
G.write_gmt(f"{W}/sets.gmt", gs)
print("jar/classpath:", G.GSEA_CP)
print("N =", len(names), " gene sets =", len(gs), " nperm = 1000, seed 149, set_min 15 set_max 500")

masks = {k: np.isin(names, v) for k, v in gs.items()}

# ------------------------------------------------------------------ A: ES per scheme
for scheme, p in (("classic", 0.0), ("weighted", 1.0), ("weighted_p2", 2.0)):
    d = G.run_preranked(f"{W}/list.rnk", f"{W}/sets.gmt", f"{W}/out_{scheme}", nperm=1000,
                        extra=["-scoring_scheme", scheme])
    edb = G.parse_edb(d)
    tsv = G.parse_report_tsv(d)
    max_d_es = 0.0
    n_rank_mismatch = 0
    n_le_mismatch = 0
    for k in gs:
        es_ref, i_ref, _ = R.enrichment_score(sc, masks[k], p)
        le_ref, _, _ = R.leading_edge(sc, masks[k], p)
        es_gsea = float(tsv[k]["ES"])
        max_d_es = max(max_d_es, abs(es_gsea - es_ref))
        if edb[k]["rank_at_es"] != i_ref:
            n_rank_mismatch += 1
        hits = edb[k]["hit_indices"]
        le_gsea = hits[hits <= edb[k]["rank_at_es"]] if es_gsea >= 0 else hits[hits >= edb[k]["rank_at_es"]]
        if not np.array_equal(le_gsea, le_ref):
            n_le_mismatch += 1
        if not np.array_equal(hits, np.flatnonzero(masks[k])):
            print("  HIT INDEX MISMATCH", k)
    print(f"A. scheme={scheme:12s} p={p}: max |ES_gsea - ES_ref| = {max_d_es:.2e} over {len(gs)} sets; "
          f"rank-at-ES mismatches = {n_rank_mismatch}; leading-edge mismatches = {n_le_mismatch}")
    if scheme == "weighted":
        d_weighted, edb_w, tsv_w = d, edb, tsv

# ------------------------------------------------------------------ B: null-derived stats
keys = list(gs)
es_real = np.array([float(tsv_w[k]["ES"]) for k in keys])
rnd = np.array([edb_w[k]["rnd_es"] for k in keys])           # sets x perms, 4 dp
nes_gsea = np.array([float(tsv_w[k]["NES"]) for k in keys])
np_gsea = np.array([float(tsv_w[k]["NOM p-val"]) for k in keys])
fdr_gsea = np.array([float(tsv_w[k]["FDR q-val"]) for k in keys])
fwer_gsea = np.array([float(tsv_w[k]["FWER p-val"]) for k in keys])

nes_ref = np.array([R.nes_meandiv(es_real[j], rnd[j]) for j in range(len(keys))])
np_ref = np.array([R.nominal_p(es_real[j], rnd[j]) for j in range(len(keys))])
# NES of every permutation ES, normalised with its own set's same-sign mean (as the code does)
nes_rnd = np.empty_like(rnd)
for j in range(len(keys)):
    pos = rnd[j][rnd[j] >= 0]
    neg = rnd[j][rnd[j] < 0]
    mp = pos.mean() if pos.size else np.nan
    mn = abs(neg.mean()) if neg.size else np.nan
    nes_rnd[j] = np.where(rnd[j] >= 0, rnd[j] / mp, rnd[j] / mn)
fdr_code = R.fdr_gsea_code(nes_ref, nes_rnd)
fdr_paper = R.fdr_paper(nes_ref, nes_rnd)
fwer_ref = R.fwer(nes_ref, nes_rnd)

print(f"B. NES:  max |NES_gsea - NES_ref|  = {np.nanmax(np.abs(nes_gsea - nes_ref)):.2e}  (ref built from the 4-dp RND_ES)")
print(f"B. NOMp: max |p_gsea - p_ref|      = {np.nanmax(np.abs(np_gsea - np_ref)):.2e}  (1/nperm = 1e-3); "
      f"sets with p = 0 reported: {(np_gsea == 0).sum()} of {len(keys)}")
print(f"B. FWER: max |FWER_gsea - FWER_ref| = {np.nanmax(np.abs(fwer_gsea - fwer_ref)):.2e}")
print(f"B. FDR:  max |FDR_gsea - FDR_code-definition|  = {np.nanmax(np.abs(fdr_gsea - fdr_code)):.2e}")
print(f"B. FDR:  max |FDR_gsea - FDR_paper-definition| = {np.nanmax(np.abs(fdr_gsea - fdr_paper)):.2e}; "
      f"median |diff| = {np.nanmedian(np.abs(fdr_gsea - fdr_paper)):.2e}")
print("   per set (NES, FDR reported, FDR code-def, FDR paper-def):")
for j in np.argsort(-np.abs(nes_ref)):
    print(f"   {keys[j]:14s} NES={nes_ref[j]:7.3f} p={np_gsea[j]:.3f} FDR={fdr_gsea[j]:.4f} "
          f"code={fdr_code[j]:.4f} paper={fdr_paper[j]:.4f} FWER={fwer_gsea[j]:.3f}")

# ------------------------------------------------------------------ C: sanity of calls
print(f"C. null ES range: [{rnd.min():.4f}, {rnd.max():.4f}]; perms per set = {rnd.shape[1]}")
planted = ["TOP", "BOTTOM", "UPPER_HALF", "LOWER_MID"]
print("C. planted sets FDR:", {k: fdr_gsea[keys.index(k)] for k in planted})
rand_fdr = [fdr_gsea[keys.index(k)] for k in keys if k.startswith("RND")]
print(f"C. random sets with FDR < 0.25: {sum(f < 0.25 for f in rand_fdr)} of {len(rand_fdr)}; MIXED_HALF ES = {es_real[keys.index('MIXED_HALF')]:.4f}")
