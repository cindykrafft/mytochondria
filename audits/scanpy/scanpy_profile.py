#!/usr/bin/env python3
"""Profile how each cohort paper used Scanpy.

Mines the full text for the choices that select Scanpy code paths:
normalize_total/log1p, highly_variable_genes flavour, regress_out/scale,
neighbors/leiden/louvain parameters, the rank_genes_groups test, score_genes,
QC metrics, batch integration, and the stated scanpy version. One JSONL record per paper.

Usage: python3 scanpy_profile.py            (fetch full texts, cache fallback)
       python3 scanpy_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the Seurat evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat audit, the 2026-09-02 run had no route to Europe PMC (www.ebi.ac.uk denied by the
session's egress policy; NCBI likewise), so every record in
scanpy_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "scanpy".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below; Seurat's function names are
# CamelCase identifiers and matching them exactly is the point.
FEATURES = {
 "normalize_total / library-size normalisation": r"normalize_total|normalize_per_cell|(?:library[- ]size|total[- ]count|CPM|counts per (?:million|10,?000))[^.]{0,60}normali",
 "target_sum 1e4 stated":               r"target_sum\s*=\s*1e4|10,?000 (?:counts|reads|UMIs) per cell|1e4",
 "log1p":                               r"log1p|log\(x\s*\+\s*1\)|log-?transform",
 "highly_variable_genes":               r"highly_variable_genes|highly variable genes",
 "HVG flavor seurat_v3":                r"seurat_v3|flavor\s*=\s*['\"]seurat",
 "HVG flavor cell_ranger":              r"cell_ranger",
 "n_top_genes stated":                  r"n_top_genes|top \d,?\d{3} (?:highly )?variable",
 "regress_out":                         r"regress_out|regress(?:ed|ing)? out",
 "scale / max_value":                   r"sc\.pp\.scale|max_value|scaled to unit variance",
 "pca":                                 r"sc\.pp\.pca|sc\.tl\.pca|principal component",
 "neighbors":                           r"sc\.pp\.neighbors|n_neighbors|k-?nearest|kNN graph",
 "leiden":                              r"leiden",
 "louvain":                             r"louvain",
 "resolution stated":                   r"resolution[^.]{0,30}(?:of |= ?|set to )?\d\.\d+|resolution parameter",
 "umap":                                r"UMAP",
 "rank_genes_groups":                   r"rank_genes_groups",
 "wilcoxon named":                      r"wilcoxon",
 "t-test named":                        r"t-test|t_test|ttest",
 "t-test_overestim_var":                r"overestim_var",
 "logreg":                              r"logreg|logistic regression",
 "log fold change reported":            r"logfoldchange|log2? ?fold[- ]?change|\bLFC\b|\blogFC\b",
 "adjusted p / BH":                     r"pvals_adj|adjusted [pP][- ]?value|Benjamini|\bFDR\b|padj",
 "score_genes":                         r"score_genes|gene (?:set )?score|module score|signature score",
 "score_genes_cell_cycle":              r"score_genes_cell_cycle|cell[- ]cycle (?:score|scoring|regress)",
 "calculate_qc_metrics / percent mito": r"calculate_qc_metrics|pct_counts_mt|mitochondrial (?:gene|read|content|percent|fraction)",
 "mito threshold stated":               r"(?:<|>|≤|≥|less than|more than|above|below|under|over)\s*\d{1,2}\s*% (?:of )?(?:mitochondrial|mito)|mitochondrial[^.]{0,60}(?:<|>|≤|≥|less than|more than|above|below)\s*\d{1,2}\s*%",
 "doublet removal":                     r"scrublet|Scrublet|DoubletFinder|scDblFinder|doublet",
 "batch integration (harmony/bbknn/scVI/combat)": r"harmony|Harmony|bbknn|BBKNN|scVI|scvi|combat|ComBat|scanorama|Scanorama",
 "scanpy version stated":               r"[Ss]canpy(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "diffusion / PAGA / trajectory":       r"diffmap|diffusion (?:map|pseudotime)|PAGA|dpt|pseudotime|scVelo|velocity",
 "Seurat also used":                    r"Seurat(?![A-Za-z])",
 "squidpy / spatial":                   r"squidpy|Visium|Xenium|MERFISH|spatial transcriptom",
 "CellChat / ligand-receptor":          r"CellChat|CellPhoneDB|liana|LIANA|NicheNet|ligand[- ]receptor",
 "snRNA-seq":                           r"single[- ]nucle(?:us|i)|snRNA",
}
CI = {"normalize_total / library-size normalisation", "target_sum 1e4 stated", "log1p",
      "highly_variable_genes", "n_top_genes stated", "regress_out", "scale / max_value", "pca",
      "neighbors", "leiden", "louvain", "resolution stated", "wilcoxon named", "t-test named",
      "log fold change reported", "adjusted p / BH", "score_genes", "score_genes_cell_cycle",
      "calculate_qc_metrics / percent mito", "mito threshold stated", "diffusion / PAGA / trajectory",
      "snRNA-seq"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Ss]canpy(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"resolution[^.;]{0,30}?(\d\.\d+)", re.I)
MITO  = re.compile(r"(\d{1,2}(?:\.\d)?)\s*%[^.;]{0,40}?mitochondrial|mitochondrial[^.;]{0,60}?(\d{1,2}(?:\.\d)?)\s*%", re.I)
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|p_val_adj|padj|FDR|[qQ][- ]?value|Bonferroni)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
LFC   = re.compile(r"(?:logfc\.threshold|\|?\s*(?:avg_)?log2?\s*(?:fold[- ]?change|FC)\s*\|?|\bLFC\b|fold[- ]?change)[^.;]{0,30}?[>≥=]\s*(\d+(?:\.\d+)?)", re.I)
DIMS  = re.compile(r"(?:dims\s*=\s*1:|(?:first|top)\s+)(\d{1,3})\s*(?:PCs?|principal components|dimensions)?", re.I)
KWIN  = re.compile(r"[Ss]canpy(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major != 1: return None          # scanpy has only had 1.x releases in the cohort years
    return "1.%d" % minor

def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = set(VER.findall(text))
    if c.get("version_survey"):           # the survey's own full-text extraction
        vers.add(c["version_survey"])
    vers  = sorted(vers)
    fams  = sorted({f for f in (family(v) for v in vers) if f})
    c.update({
        "source": source,
        "features": feats,
        "versions_all": vers,
        "version_family": fams,
        "resolutions": sorted(set(RES.findall(text))),
        "mito_pct": sorted({a or b for a, b in MITO.findall(text)}),
        "padj_cutoffs": sorted(set(PADJ.findall(text))),
        "lfc_cutoffs": sorted(set(LFC.findall(text))),
        "dims": sorted({int(d) for d in DIMS.findall(text) if 0 < int(d) <= 200}),
    })
    if source == "fulltext":
        ctx = []
        for m in KWIN.finditer(text):
            lo = max(0, m.start()-260); hi = min(len(text), m.end()+320)
            ctx.append(("..."+text[lo:hi]+"...").strip())
            if len(ctx) >= 3: break
        c["context"] = ctx
    return c

OFFLINE = "--offline" in sys.argv[1:]

def profile(c):
    raw, why = (None, "offline") if OFFLINE else E.fetch(c["pmcid"])
    if raw:
        try:
            root = ET.fromstring(raw)
            E._strip_refs(root)
            body = root.find(".//body")
            text = re.sub(r"\s+", " ", " ".join(body.itertext())) if body is not None else ""
            if text:
                return mine(c, text, "fulltext")
            why = "empty_body"
        except Exception:
            why = "parse"
    c["profile_error"] = why
    return mine(c, c.pop("_cache_text"), "survey_cache")

cohort, by_pmcid = [], {}
with open("../../survey/data/paper_software.tsv") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["package"] == "Scanpy":
            rec = {"pmcid": row["pmcid"], "doi": row["doi"],
                   "journal": row["journal"], "year": row["year"],
                   "version_survey": row["version"],
                   "in_methods": row["in_methods"] == "True",
                   "pipeline_stages_survey": row["pipeline_stages"],
                   "evidence_survey": row["evidence_sentence"],
                   "_cache_text": row["evidence_sentence"]}
            cohort.append(rec); by_pmcid[row["pmcid"]] = rec
with gzip.open("../../survey/data/pipelines.jsonl.gz", "rt") as fh:
    for line in fh:
        d = json.loads(line)
        rec = by_pmcid.get(d["pmcid"])
        if rec is None: continue
        rec["title"] = d.get("title", "")
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "Scanpy")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("scanpy_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
res, mito, padj, lfc, dims = Counter(), Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for r in c["resolutions"]: res[r] += 1
    for m in c["mito_pct"]: mito[m] += 1
    for p in c["padj_cutoffs"]: padj[p] += 1
    for l in c["lfc_cutoffs"]: lfc[l] += 1
    for d in c["dims"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nresolutions:", dict(res.most_common(10)))
print("mito %:", dict(mito.most_common(10)))
print("padj cutoffs:", dict(padj.most_common(8)))
print("lfc cutoffs:", dict(lfc.most_common(8)))
print("dims:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
