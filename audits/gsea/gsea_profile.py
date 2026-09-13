#!/usr/bin/env python3
"""Profile how each cohort paper used GSEA.

Mines the text for the choices that select GSEA code paths: GSEAPreranked vs the
expression-based tool, the ranking metric or the statistic the list was ranked by, the
permutation type, the scoring scheme, the gene-set size limits, MSigDB collections, the
FDR threshold, which implementation actually ran (GSEA desktop / javaGSEA, fgsea,
clusterProfiler, GSEApy, ssGSEA/GSVA, WebGestalt ...) and the stated version.  One JSONL
record per paper.

Usage: python3 gsea_profile.py            (fetch full texts, cache fallback)
       python3 gsea_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the GSEA evidence sentence in
                 paper_software.tsv plus every per-package evidence snippet in
                 pipelines.jsonl.gz. A few hundred characters per package, so
                 feature counts from this source are LOWER BOUNDS on usage, not
                 measurements of it.

As for the Seurat and Scanpy audits, the 2026-09-13 run had no route to Europe PMC
(www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so every record in
gsea_profiles.jsonl is source=survey_cache. Rerun from a host with Europe PMC access to
replace them; the fetch path is unchanged from the other audits.
Version regexes require "GSEA" followed (within a few tokens) by a 3.x/4.x version.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below; Seurat's function names are
# CamelCase identifiers and matching them exactly is the point.
FEATURES = {
 "GSEA desktop / javaGSEA / Broad named":  r"GSEA ?desktop|javaGSEA|GSEA (?:software|application|tool|program)|Broad Institute[^.]{0,80}GSEA|GSEA[^.]{0,60}Broad Institute|gsea-msigdb|GenePattern",
 "GSEAPreranked / pre-ranked":              r"pre-?ranked|GSEAPreranked|preranked",
 "fgsea used":                              r"fgsea|FGSEA",
 "clusterProfiler (gseGO/gseKEGG/GSEA())":  r"clusterProfiler|gseGO|gseKEGG|gsePathway",
 "GSEApy":                                  r"GSEApy|gseapy",
 "ssGSEA / GSVA":                           r"ssGSEA|single[- ]sample GSEA|GSVA",
 "WebGestalt / Enrichr / other web tool":   r"WebGestalt|Enrichr|g:Profiler|DAVID|Metascape",
 "MSigDB named":                            r"MSigDB|Molecular Signatures Database|msigdbr",
 "Hallmark collection":                     r"[Hh]allmark",
 "KEGG / Reactome / GO collections":        r"KEGG|Reactome|Gene Ontology|\bGO\b|C2\b|C5\b|C7\b",
 "ranked by log fold change":               r"rank(?:ed|ing)?[^.]{0,80}(?:log2? ?fold|fold[- ]change|logFC|log2FC)",
 "ranked by t / Wald / signed p statistic": r"rank(?:ed|ing)?[^.]{0,80}(?:t[- ]statistic|Wald|signed[^.]{0,20}p|test statistic|z[- ]score)",
 "Signal2Noise / signal-to-noise metric":   r"[Ss]ignal[- ]?(?:2|to)[- ]?[Nn]oise",
 "t-test metric named":                     r"t-?[Tt]est metric|metric[^.]{0,30}t-?test",
 "phenotype permutation":                   r"phenotype[- ]permutation|permut(?:ed|ing|ation)[^.]{0,40}(?:phenotype|sample label|class label)",
 "gene-set permutation":                    r"gene[- ]?set[- ]permutation|permut(?:ed|ing|ation)[^.]{0,40}gene[- ]?sets?",
 "number of permutations stated":           r"\d[\d,]{2,} permutations|nperm|permutations? ?=? ?\d[\d,]{2,}",
 "weighted / classic scoring stated":       r"weighted (?:scoring|enrichment statistic|Kolmogorov)|classic (?:scoring|enrichment statistic)|scoring[- ]scheme|p ?= ?1 weight",
 "gene set size limits stated":             r"(?:min(?:imum)?|max(?:imum)?)[^.]{0,30}(?:gene set|set) size|set_min|set_max|between \d+ and \d+ genes|sizes? (?:of|between) \d+[^.]{0,10}\d+ genes",
 "FDR threshold stated":                    r"FDR[^.]{0,30}(?:<|≤|less than|below)\s*0?\.\d+|q[- ]?value[^.]{0,30}(?:<|≤)\s*0?\.\d+|FDR[^.]{0,20}(?:25|5|10|1)\s*%",
 "NES reported":                            r"\bNES\b|normali[sz]ed enrichment score",
 "nominal p reported":                      r"nominal p|NOM p",
 "leading edge":                            r"leading[- ]edge",
 "collapse / chip platform":                r"collapse|\.chip\b|chip platform|probe set",
 "default parameters stated":               r"default (?:parameters|settings|options)",
 "GSEA version stated":                     r"GSEA[^.;(]{0,40}?(?:v(?:ersion)?\.?\s*)?[34]\.\d",
 "single-cell context":                     r"single[- ]cell|scRNA|snRNA|Seurat|Scanpy",
 "DESeq2 / edgeR / limma upstream":         r"DESeq2|edgeR|limma",
}
CI = {"GSEAPreranked / pre-ranked", "Hallmark collection", "ranked by log fold change",
      "ranked by t / Wald / signed p statistic", "phenotype permutation", "gene-set permutation",
      "number of permutations stated", "weighted / classic scoring stated", "gene set size limits stated",
      "FDR threshold stated", "leading edge", "collapse / chip platform", "default parameters stated",
      "nominal p reported"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"(?:GSEA|javaGSEA)[^.;(]{0,40}?(?:v(?:ersion)?\.?\s*)?([34]\.\d(?:\.\d+)*)")
RES   = re.compile(r"(\d[\d,]{2,}) permutations", re.I)
MITO  = re.compile(r"FDR[^.;]{0,30}?(?:<|≤|less than|below)\s*(0?\.\d+)|q[- ]?value[^.;]{0,30}?(?:<|≤)\s*(0?\.\d+)", re.I)
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|padj|FDR|[qQ][- ]?value)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
LFC   = re.compile(r"(?:min(?:imum)?|max(?:imum)?)[^.;]{0,30}?(?:gene set|set) size[^.;]{0,15}?(\d+)|set_(?:min|max)\s*=?\s*(\d+)", re.I)
DIMS  = re.compile(r"MSigDB[^.;]{0,20}?v\.?\s*(\d+)", re.I)
KWIN  = re.compile(r"GSEA")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major not in (3, 4): return None   # GSEA desktop 3.x (2017-2019) and 4.x (2019-) are the cohort-era releases
    return "%d.%d" % (major, minor)

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
        "nperm": sorted(set(RES.findall(text))),
        "fdr_cutoffs": sorted({a or b for a, b in MITO.findall(text)}),
        "padj_cutoffs": sorted(set(PADJ.findall(text))),
        "set_size_limits": sorted({a or b for a, b in LFC.findall(text)}),
        "msigdb_version": sorted({int(d) for d in DIMS.findall(text) if 0 < int(d) <= 2030}),
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
        if row["package"] == "GSEA":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "GSEA")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, GSEA, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "GSEA".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("gsea_profiles.jsonl", "w") as fh:
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
    for r in c["nperm"]: res[r] += 1
    for m in c["fdr_cutoffs"]: mito[m] += 1
    for p in c["padj_cutoffs"]: padj[p] += 1
    for l in c["set_size_limits"]: lfc[l] += 1
    for d in c["msigdb_version"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\npermutations stated:", dict(res.most_common(10)))
print("FDR cutoffs:", dict(mito.most_common(10)))
print("padj cutoffs:", dict(padj.most_common(8)))
print("set size limits:", dict(lfc.most_common(8)))
print("MSigDB versions:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
