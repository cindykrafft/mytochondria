"""Compare the GSEA tables written by gsea_vs_reference.R with the numpy reference (ref_gsea.py).
Usage: python gsea_vs_reference.py <outdir>"""
import json, sys, os
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ref_gsea import gsea_es

out = sys.argv[1]
d = json.load(open(os.path.join(out, "design.json")))
stats = pd.Series({k: v[0] if isinstance(v, list) else v for k, v in d["stats"].items()})
stats = stats.sort_values(ascending=False)          # the R script sorted before dumping; keep names
genes = np.array(stats.index); sv = stats.values
sets = {k: list(v) for k, v in d["sets"].items()}


def ref(setname, p=1.0):
    members = set(sets[setname]) & set(genes)
    hits = np.isin(genes, list(members))
    r = gsea_es(sv, hits, p)
    r["size"] = int(hits.sum())
    r["le_genes"] = set(genes[r["leading_edge_idx"]])
    return r


def load(name):
    f = os.path.join(out, name + ".tsv")
    return pd.read_csv(f, sep="\t") if os.path.exists(f) else None


def report(name, idcol, escol, sizecol=None, lecol=None, rankcol=None, lestr=None, p=1.0, note=""):
    df = load(name)
    if df is None:
        print(f"\n== {name}: not produced"); return None
    df = df.set_index(idcol)
    print(f"\n== {name}{note}: {len(df)} sets tested; SMALL tested: {'SMALL' in df.index}; BIG tested: {'BIG' in df.index}")
    dES = []; dsize = []; le_ok = []; rank_ok = []; tls_ok = []
    for sid in df.index:
        r = ref(sid, p)
        dES.append(abs(df.loc[sid, escol] - r["ES"]))
        if sizecol: dsize.append(int(df.loc[sid, sizecol]) - r["size"])
        if lecol and isinstance(df.loc[sid, lecol], str):
            le_ok.append(set(df.loc[sid, lecol].split("/")) == r["le_genes"])
        if rankcol: rank_ok.append(int(df.loc[sid, rankcol]) == r["rank"])
        if lestr:
            s = df.loc[sid, lestr]
            want = f"tags={round(r['tags']*100)}%, list={round(r['list']*100)}%, signal={round(r['signal']*100)}%"
            tls_ok.append(s == want)
    print(f"   max |ES - reference| = {max(dES):.2e}")
    if sizecol: print(f"   size - reference size: {sorted(set(dsize))}  (ABSENT size = {int(df.loc['ABSENT', sizecol]) if 'ABSENT' in df.index else 'n/a'}, DUP size = {int(df.loc['DUP', sizecol]) if 'DUP' in df.index else 'n/a'})")
    if lecol: print(f"   leading edge == reference: {sum(le_ok)}/{len(le_ok)}")
    if rankcol: print(f"   rank == reference: {sum(rank_ok)}/{len(rank_ok)}")
    if lestr: print(f"   'tags/list/signal' string == reference: {sum(tls_ok)}/{len(tls_ok)}")
    return df


fm = report("fgsea_multilevel", "pathway", "ES", "size", "leadingEdge")
fs = report("fgsea_simple", "pathway", "ES", "size", "leadingEdge")
report("fgsea_simple_p0", "pathway", "ES", "size", "leadingEdge", p=0, note=" (gseaParam=0)")
report("fgsea_simple_p2", "pathway", "ES", "size", "leadingEdge", p=2, note=" (gseaParam=2)")
em = report("enrichit_multilevel", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge")
es = report("enrichit_sample", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge")
ep = report("enrichit_permute", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge")
report("enrichit_sample_p0", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge", p=0, note=" (exponent=0)")
report("enrichit_sample_p2", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge", p=2, note=" (exponent=2)")
report("enrichit_multilevel_p0", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge", p=0, note=" (exponent=0)")
report("enrichit_multilevel_p2", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge", p=2, note=" (exponent=2)")
df_ = report("dose_fgsea", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge", note=" (legacy DOSE by='fgsea')")
dp_ = report("dose_perm", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge", note=" (legacy DOSE by='DOSE')")
cp = report("clusterProfiler_GSEA", "ID", "enrichmentScore", "setSize", "core_enrichment", "rank", "leading_edge", note=" (clusterProfiler::GSEA devel)")

# scoreType = "pos": ES must be max of the running sum, leading edge from the top
for name, idc, esc, lec in [("fgsea_multilevel_pos", "pathway", "ES", "leadingEdge"), ("enrichit_multilevel_pos", "ID", "enrichmentScore", "core_enrichment")]:
    df = load(name)
    if df is None: continue
    df = df.set_index(idc); ok = []; dmax = []
    for sid in df.index:
        members = set(sets[sid]) & set(genes); hits = np.isin(genes, list(members))
        from ref_gsea import running_sum
        rs = running_sum(sv, hits); imax = int(np.argmax(rs))
        dmax.append(abs(df.loc[sid, esc] - rs[imax]))
        le = set(genes[(np.arange(len(genes)) <= imax) & hits])
        ok.append(set(str(df.loc[sid, lec]).split("/")) == le)
    print(f"\n== {name}: max |ES - max(running sum)| = {max(dmax):.2e}; leading edge from top == reference: {sum(ok)}/{len(ok)}")

# cross-engine: NES and p-values (Monte-Carlo, so agreement within noise), sign conventions
print("\n== cross-engine NES / p-value on the two planted sets and 3 random sets")
rows = []
for sid in ["UP1", "DOWN1", "R01", "R02", "R03"]:
    row = {"set": sid}
    for name, df, pc, nc in [("fgsea_ml", fm, "pval", "NES"), ("fgsea_simple", fs, "pval", "NES"), ("enrichit_ml", em, "pvalue", "NES"),
                              ("enrichit_sample", es, "pvalue", "NES"), ("enrichit_permute", ep, "pvalue", "NES"), ("DOSE_fgsea", df_, "pvalue", "NES"), ("DOSE_perm", dp_, "pvalue", "NES")]:
        if df is not None and sid in df.index:
            row[name + " p"] = f"{df.loc[sid, pc]:.3g}"; row[name + " NES"] = f"{df.loc[sid, nc]:.3f}"
    rows.append(row)
print(pd.DataFrame(rows).set_index("set").T.to_string())

# ties
t = json.load(open(os.path.join(out, "ties.json")))
st = pd.Series({k: v[0] if isinstance(v, list) else v for k, v in t["stats"].items()})
st = st.sort_values(ascending=False, kind="stable")     # input-order for ties
hits = np.isin(np.array(st.index), t["set"])
r = gsea_es(st.values, hits)
f_es = t['fgsea_ES'][0] if isinstance(t['fgsea_ES'], list) else t['fgsea_ES']
e_es = t['enrichit_ES'][0] if isinstance(t['enrichit_ES'], list) else t['enrichit_ES']
print(f"\n== ties: reference ES with tied block in input order = {r['ES']:.6f}; fgsea {f_es:.6f}; enrichit {e_es:.6f}")
