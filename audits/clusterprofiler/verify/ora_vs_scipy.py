"""Check the ORA tables written by ora_vs_scipy.R against scipy and the definitions.

For every engine/universe combination:
  * N = |annotated genes (∩ user universe)|, M = |term ∩ N|, n = |query ∩ N|, k = |query ∩ term|
    are recomputed from the design and compared with the table's BgRatio/GeneRatio/Count;
  * pvalue vs scipy hypergeom.sf(k-1, N, M, n);
  * p.adjust vs an independent BH over the rows the engine tested;
  * which terms are tested (size window; terms with zero overlap);
  * zScore, RichFactor, FoldEnrichment vs their definitions.
Usage: python ora_vs_scipy.py <outdir>
"""
import json, sys, os
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ref_gsea import hypergeom_sf, bh

out = sys.argv[1]
d = json.load(open(os.path.join(out, "design.json")))
t2g = pd.DataFrame(d["term2gene"])
terms = {t: set(g) for t, g in t2g.groupby("term")["gene"]}
query = set(d["query"]); annotated = set(d["annotated"]); user_u = set(d["universe_user"])


def check(fname, universe, minGS=10, maxGS=500, legacy=False):
    df = pd.read_csv(os.path.join(out, fname), sep="\t")
    N = len(universe)
    n_new = len(query & universe)
    n_legacy = len(query & annotated)          # legacy DOSE: query genes with any annotation
    n = n_legacy if legacy else n_new
    print(f"\n== {fname}: N={N}  n(new)={n_new}  n(legacy)={n_legacy}  rows={len(df)}")
    # which terms should be tested: size in window after intersecting with universe, overlap >= 1
    tested = {t for t, g in terms.items() if minGS <= len(g & universe) <= maxGS and len(g & universe & query) > 0}
    in_table = set(df["ID"])
    print(f"   terms in size window with overlap>=1: {len(tested)}; in table: {len(in_table)}; "
          f"missing: {sorted(tested - in_table)[:5]}; extra: {sorted(in_table - tested)[:5]}")
    zero_overlap_in_window = sum(1 for t, g in terms.items() if minGS <= len(g & universe) <= maxGS and len(g & universe & query) == 0)
    print(f"   terms in size window with zero overlap (should NOT be in table/BH): {zero_overlap_in_window}")
    # parameters and p-values
    M = np.array([len(terms[t] & universe) for t in df["ID"]])
    k = np.array([len(terms[t] & universe & query) for t in df["ID"]])
    bg = df["BgRatio"].str.split("/", expand=True).astype(int)
    gr = df["GeneRatio"].str.split("/", expand=True).astype(int)
    print(f"   BgRatio numerator == M: {bool((bg[0].values == M).all())}; BgRatio denominator == N: {bool((bg[1].values == N).all())}")
    print(f"   GeneRatio numerator == k == Count: {bool((gr[0].values == k).all() and (df['Count'].values == k).all())}; "
          f"GeneRatio denominator == n: {bool((gr[1].values == n).all())} (table says {gr[1].iloc[0]})")
    p_ref = hypergeom_sf(k, N, M, n)
    print(f"   max |pvalue - scipy hypergeom.sf(k-1,N,M,n)| = {np.abs(df['pvalue'].values - p_ref).max():.2e}  "
          f"(max rel {np.max(np.abs(df['pvalue'].values - p_ref) / np.maximum(p_ref, 1e-300)):.2e})")
    print(f"   max |p.adjust - BH over table rows| = {np.abs(df['p.adjust'].values - bh(df['pvalue'].values)).max():.2e}")
    if "zScore" in df:
        mu = M * n / N; sig = mu * (N - n) * (N - M) / N / (N - 1)
        print(f"   max |zScore - (k-mu)/sqrt(var_hypergeom)| = {np.abs(df['zScore'].values - (k - mu) / np.sqrt(sig)).max():.2e}")
        print(f"   RichFactor == k/M: {np.allclose(df['RichFactor'], k / M)}; FoldEnrichment == (k/n)/(M/N): {np.allclose(df['FoldEnrichment'], (k / n) / (M / N))}")
    print(f"   |universe| slot = {df['N_universe_slot'].iloc[0]} (N={N})")
    return df

e_def = check("enrichit_default.tsv", annotated)
e_usr = check("enrichit_user.tsv", annotated & user_u)
e_all = check("enrichit_size1_inf.tsv", annotated, 1, 10**9)
if os.path.exists(os.path.join(out, "dose_default.tsv")):
    d_def = check("dose_default.tsv", annotated, legacy=True)
    d_usr = check("dose_user.tsv", annotated & user_u, legacy=True)
    m = e_def.merge(d_def, on="ID", suffixes=("_new", "_old"))
    print(f"\n== enrichit vs DOSE, default universe: {len(m)} common rows; max |p diff| = {np.abs(m['pvalue_new'] - m['pvalue_old']).max():.2e}; "
          f"max |p.adjust diff| = {np.abs(m['p.adjust_new'] - m['p.adjust_old']).max():.2e}; max |qvalue diff| = {np.nanmax(np.abs(m['qvalue_new'] - m['qvalue_old'])):.2e}")
    m = e_usr.merge(d_usr, on="ID", suffixes=("_new", "_old"))
    print(f"== enrichit vs DOSE, user universe:    {len(m)} common rows; max |p diff| = {np.abs(m['pvalue_new'] - m['pvalue_old']).max():.2e}  "
          f"(n: new {e_usr['GeneRatio'].iloc[0].split('/')[1]} vs old {d_usr['GeneRatio'].iloc[0].split('/')[1]})")
