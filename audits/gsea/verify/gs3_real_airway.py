#!/usr/bin/env python3
"""GS3 on a real dataset: the airway RNA-seq experiment (Himes et al. 2014, GSE52778; the
Bioconductor `airway` package: 4 human airway smooth-muscle cell lines, dexamethasone vs
untreated, 63,677 Ensembl genes, 30,208 of them with zero counts in every sample).

Differential expression: DESeq2's algorithm (pydeseq2 0.5.4, design ~ cell + dex, contrast
trt vs untrt; DESeq2 itself gives NA for genes with all-zero counts, so the ranked lists below
mimic the ways an exact 0 reaches a .rnk in practice).  Gene sets: KEGG 2016 (293 human
pathways) and MSigDB Hallmark v7.0 (50), both as shipped in GSEApy's test data.

Ranked lists (Ensembl -> HGNC symbol through annotables grch38, duplicates collapsed to the
gene with the largest baseMean):
  stat_na0     every annotated gene, Wald statistic, NA replaced by 0
               (the "results table with NAs set to 0" list)
  lfc_na0      every annotated gene, log2 fold change, NA replaced by 0
  tested       only genes DESeq2 tested (padj not NA): the list a careful analyst makes
Each list is run through GseaPreranked on the audited build and on the GS3-patched jar with
the default settings (weighted, 1000 permutations, 15 <= size <= 500).  For every reported
set the script states whether all its members present in the list have score 0 (the GS3
condition) and what the program reported for it.

Usage: gs3_real_airway.py [build]     (build: master, v4.3.2, ..., patched_gs3)
Needs the DESeq2 results at /tmp/gs3real/data/airway_deseq2_results.csv (de.py) and the
data files under /tmp/gs3real/data (dash-free path: GSEA's option parser splits on "-").
"""
import os, re, sys, collections
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gsea_common as C

BUILD = sys.argv[1] if len(sys.argv) > 1 else "master"
D = "/tmp/gs3real/data"
W = "/tmp/gs3real/run_" + BUILD
os.makedirs(W, exist_ok=True)
C.banner("GS3 on real data: airway (GSE52778), DESeq2 ranking, KEGG 2016 + Hallmark", BUILD)

# ---- ranked lists -------------------------------------------------------------------
res = pd.read_csv(f"{D}/airway_deseq2_results.csv", index_col=0)
ann = pd.read_csv(f"{D}/grch38.csv").dropna(subset=["symbol"]).drop_duplicates("ensgene").set_index("ensgene")
res["symbol"] = ann["symbol"].reindex(res.index)
res = res.dropna(subset=["symbol"])
res = res.sort_values("baseMean", ascending=False).drop_duplicates("symbol").set_index("symbol")
print(f"genes with a symbol: {len(res)}  tested (padj not NA): {int(res['padj'].notna().sum())}  "
      f"stat NA: {int(res['stat'].isna().sum())}")

lists = {
    "stat_na0": res["stat"].fillna(0.0),
    "lfc_na0": res["log2FoldChange"].fillna(0.0),
    "tested": res.loc[res["padj"].notna(), "stat"],
}
for k, s in lists.items():
    s = s.sort_values(ascending=False)
    lists[k] = s
    C.write_rnk(os.path.join(W, k + ".rnk"), list(s.index), list(s.values))
    print(f"  list {k:9s}: {len(s):6d} genes, {int((s == 0).sum()):6d} scored exactly 0")


# ---- gene sets: sanitise names (spaces, slashes) -------------------------------------
def read_gmt(path, prefix):
    sets = {}
    for line in open(path):
        p = line.rstrip("\n").split("\t")
        if len(p) < 3:
            continue
        name = re.sub(r"[^A-Za-z0-9_]+", "_", p[0]).strip("_")
        sets[prefix + name] = [g for g in p[2:] if g]
    return sets


sets = read_gmt(f"{D}/kegg2016.gmt", "KEGG_")
sets.update(read_gmt(f"{D}/hallmark_v7.0.gmt", ""))
C.write_gmt(os.path.join(W, "sets.gmt"), sets)
print(f"gene sets: {len(sets)} (KEGG 2016 + Hallmark v7.0)")

# ---- run -----------------------------------------------------------------------------
for k, s in lists.items():
    present = {n: [g for g in m if g in s.index] for n, m in sets.items()}
    allzero = {n: (15 <= len(p) <= 500 and all(s[g] == 0 for g in p)) for n, p in present.items()}
    n_cond = sum(allzero.values())
    r = C.run_preranked(BUILD, os.path.join(W, k + ".rnk"), os.path.join(W, "sets.gmt"), W, label=k)
    if not r.ok():
        print(f"\n[{k}] GSEA failed: {r.error()}")
        continue
    rows = r.rows
    n_rep = len(rows)
    by_nes = sorted(rows.items(), key=lambda kv: kv[1]["nes"] if not np.isnan(kv[1]["nes"]) else 0)
    rank_neg = {n: i + 1 for i, (n, _) in enumerate(by_nes)}            # 1 = most negative NES
    print(f"\n[{k}] {n_rep} sets reported; {n_cond} of them meet the GS3 condition "
          f"(every member present has score 0)")
    warn = sum(1 for line in r.log.splitlines() if "zero" in line.lower() and "weight" in line.lower())
    if warn:
        print(f"  build printed {warn} zero-weight warning line(s)")
    sig25 = [n for n, v in rows.items() if v["fdr"] < 0.25]
    sig05 = [n for n, v in rows.items() if v["fdr"] < 0.05]
    art25 = [n for n in sig25 if allzero.get(n)]
    art05 = [n for n in sig05 if allzero.get(n)]
    print(f"  FDR < 0.25: {len(sig25)} sets, of which {len(art25)} are all-zero sets;  "
          f"FDR < 0.05: {len(sig05)} sets, of which {len(art05)} all-zero")
    if n_cond:
        print(f"  {'set':58s} {'size':>4s} {'ES':>8s} {'NES':>7s} {'p':>6s} {'FDR':>6s} {'neg-rank':>8s}")
        for n, v in sorted(rows.items(), key=lambda kv: kv[1]["nes"]):
            if allzero.get(n):
                print(f"  {n[:58]:58s} {v['size']:4d} {v['es']:8.4f} {v['nes']:7.3f} {v['np']:6.3f} {v['fdr']:6.3f} {rank_neg[n]:8d}")
        # the ten most negative sets of the run, artefacts marked
        print("  ten most negative NES in the run:")
        for n, v in by_nes[:10]:
            print(f"    {'*' if allzero.get(n) else ' '} {n[:58]:58s} NES {v['nes']:7.3f}  FDR {v['fdr']:6.3f}")
        # sets that are nearly all zero (>= 90 % members at 0 but not all): affected by ties, not GS3
        near = [n for n, p in present.items() if 15 <= len(p) <= 500 and not allzero[n]
                and sum(s[g] == 0 for g in p) >= 0.9 * len(p)]
        print(f"  sets with >= 90 % but not all members at 0 (tie-order dependent, not GS3): {len(near)}")
    with open(os.path.join(W, k + ".summary.tsv"), "w") as f:
        f.write("set\tsize\tall_zero\tES\tNES\tp\tFDR\n")
        for n, v in rows.items():
            f.write(f"{n}\t{v['size']}\t{int(bool(allzero.get(n)))}\t{v['es']}\t{v['nes']}\t{v['np']}\t{v['fdr']}\n")
