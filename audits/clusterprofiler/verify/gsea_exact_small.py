"""Exact enumeration of the gene-set permutation null for the tiny designs of gsea_exact_small.R.
Usage: python gsea_exact_small.py <outdir>"""
import json, sys, os
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ref_gsea import exact_null, gsea_es, gsea_pvalue_from_null

out = sys.argv[1]
eng = pd.read_csv(os.path.join(out, "engines.tsv"), sep="\t")
nulls = {}
rows = []
for _, r in eng.iterrows():
    st = json.load(open(os.path.join(out, f"{r.design}_stats.json")))["stats"]
    s = pd.Series({k: v[0] if isinstance(v, list) else v for k, v in st.items()})
    sv = s.values; genes = np.array(s.index)
    key = (r.design, int(r.k))
    if key not in nulls:
        nulls[key] = exact_null(sv, int(r.k))
    null = nulls[key]
    hits = np.isin(genes, r.members.split("/"))
    ref = gsea_es(sv, hits)
    ex = gsea_pvalue_from_null(ref["ES"], null)
    rows.append(dict(design=r.design, set=r.set, ES_ref=ref["ES"], ES_fgsea=r.fgsea_ES, ES_enrichit=r.enrichit_ES,
                     p_exact_cond=ex["p_cond"], p_exact_uncond=ex["p_uncond"], NES_exact=ex["NES"],
                     fgsea_simple=r.fgsea_simple_p, fgsea_ml=r.fgsea_ml_p_mean, fgsea_ml_sd=r.fgsea_ml_p_sd,
                     enrichit_ml=r.enrichit_ml_p_mean, enrichit_ml_sd=r.enrichit_ml_p_sd,
                     enrichit_sample=r.enrichit_sample_p, enrichit_permute=r.enrichit_permute_p, enrichit_adaptive=r.enrichit_adaptive_p,
                     dose_perm=r.get("dose_perm_p", np.nan), NES_fgsea=r.fgsea_NES, NES_enrichit_sample=r.enrichit_sample_NES,
                     NES_dose=r.get("dose_perm_NES", np.nan), n_subsets=null.size))
df = pd.DataFrame(rows)
pd.set_option("display.width", 250)
print("ES: max |fgsea - ref| = %.2e, max |enrichit - ref| = %.2e" % ((df.ES_fgsea - df.ES_ref).abs().max(), (df.ES_enrichit - df.ES_ref).abs().max()))
print("\nExact conditional p = P(ES* >= ES | same sign)  vs engines  (multilevel: mean over 40 runs)")
cols = ["design", "set", "ES_ref", "n_subsets", "p_exact_cond", "p_exact_uncond", "fgsea_simple", "fgsea_ml", "enrichit_ml", "enrichit_sample", "enrichit_permute", "enrichit_adaptive", "dose_perm"]
print(df[cols].to_string(index=False, float_format=lambda x: f"{x:.4g}"))
print("\nratio engine / exact conditional p:")
for c in ["fgsea_simple", "fgsea_ml", "enrichit_ml", "enrichit_sample", "enrichit_permute", "enrichit_adaptive", "dose_perm"]:
    ratio = df[c] / df.p_exact_cond
    print(f"   {c:18s} median {ratio.median():.3f}  min {ratio.min():.3f}  max {ratio.max():.3f}")
print("\nratio enrichit sample / exact UNconditional p: median %.3f (min %.3f, max %.3f)" % ((df.enrichit_sample / df.p_exact_uncond).median(), (df.enrichit_sample / df.p_exact_uncond).min(), (df.enrichit_sample / df.p_exact_uncond).max()))
print("\nNES vs exact ES/mean(same-sign null ES):")
print(df[["design", "set", "NES_exact", "NES_fgsea", "NES_enrichit_sample", "NES_dose"]].to_string(index=False, float_format=lambda x: f"{x:.4f}"))
