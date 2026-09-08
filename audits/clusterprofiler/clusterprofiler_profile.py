#!/usr/bin/env python3
"""Profile how each cohort paper used clusterProfiler (and fgsea / GSEA through it).

Mines the text for the choices that select clusterProfiler code paths: ORA (enrichGO/
enrichKEGG/enricher) vs GSEA (gseGO/gseKEGG/GSEA/fgsea), the ontology, the background/
universe, the adjusted-p and q-value cutoffs, gene-set size limits, simplify, compareCluster,
setReadable, the ranking metric, the annotation database, and the stated clusterProfiler /
fgsea versions. One JSONL record per paper.

Usage: python3 clusterprofiler_profile.py            (fetch full texts, cache fallback)
       python3 clusterprofiler_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the clusterProfiler evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy and Cutadapt audits, the 2026-09-08 run had no route to Europe PMC
(www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so every record in
clusterprofiler_profiles.jsonl is source=survey_cache. Rerun from a host with Europe PMC
access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "clusterProfiler" / "fgsea".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below; Seurat's function names are
# CamelCase identifiers and matching them exactly is the point.
FEATURES = {
 "enrichGO / GO ORA":                    r"enrichGO|GO (?:term )?(?:enrichment|over-?representation)|gene ontology (?:enrichment|analysis|term)",
 "enrichKEGG / KEGG":                     r"enrichKEGG|gseKEGG|KEGG",
 "enricher / custom gene sets":           r"enricher\(|enricher function|TERM2GENE|MSigDB|msigdbr|Hallmark|hallmark gene set",
 "gseGO / GSEA via clusterProfiler":      r"gseGO|gseKEGG|gsePathway|\bGSEA\(|gene set enrichment analysis",
 "fgsea named":                           r"fgsea",
 "GSEA named":                            r"\bGSEA\b",
 "GSEA desktop / Broad":                  r"GSEA (?:desktop|software|v?[0-9]\.[0-9])|Broad Institute|GSEAPreranked|gsea-msigdb",
 "ORA / hypergeometric / Fisher named":   r"over-?representation|hypergeometric|Fisher'?s exact",
 "ontology BP / MF / CC named":           r"biological process|molecular function|cellular component|\bont\s*=",
 "background / universe stated":          r"universe|background (?:gene|set|list)|all (?:expressed|detected|tested) genes",
 "adjusted p / BH / FDR cutoff":          r"p\.adjust|adjusted [pP][- ]?value|Benjamini|\bFDR\b|padj|pvalueCutoff",
 "q-value stated":                        r"q-?value|qvalueCutoff",
 "gene set size limits (minGSSize/maxGSSize)": r"minGSSize|maxGSSize|gene sets? (?:with|of) (?:at least|fewer|more|between|size)",
 "simplify":                              r"simplify\(|simplify function|semantic similarity|redundan",
 "compareCluster":                        r"compareCluster",
 "setReadable / symbols":                 r"setReadable|bitr|gene symbols? (?:were )?converted|Entrez",
 "NES reported":                          r"\bNES\b|normali[sz]ed enrichment score",
 "leading edge / core enrichment":        r"leading[- ]edge|core_enrichment|core enrichment",
 "ranking metric stated":                 r"ranked (?:by|according to|based on)|log2? ?fold[- ]?change|signed[^.]{0,20}p-?value|Wald statistic|t-statistic",
 "permutations stated":                   r"nPerm|permutation",
 "Reactome / WikiPathways / DO":          r"Reactome|ReactomePA|WikiPathways|enrichWP|enrichDO|Disease Ontology",
 "org.*.eg.db named":                     r"org\.[A-Z][a-z]\.eg\.db",
 "clusterProfiler version stated":        r"[cC]lusterProfiler(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "fgsea version stated":                  r"fgsea(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "DESeq2 / edgeR / limma in the same paper": r"DESeq2|edgeR|limma",
 "Seurat / Scanpy in the same paper":     r"Seurat(?![A-Za-z])|[Ss]canpy",
 "single-cell":                           r"single[- ]cell|scRNA|snRNA",
 "enrichplot / dotplot / cnetplot":       r"enrichplot|dotplot|cnetplot|emapplot|gseaplot|ridgeplot",
}
CI = {"enrichGO / GO ORA", "ORA / hypergeometric / Fisher named", "ontology BP / MF / CC named", "background / universe stated",
      "adjusted p / BH / FDR cutoff", "q-value stated", "gene set size limits (minGSSize/maxGSSize)", "simplify",
      "NES reported", "leading edge / core enrichment", "ranking metric stated", "permutations stated", "single-cell",
      "gseGO / GSEA via clusterProfiler"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[cC]lusterProfiler(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
FGVER = re.compile(r"fgsea(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
ONT   = re.compile(r"\b(biological process|molecular function|cellular component)\b|ont\s*=\s*['\"](BP|MF|CC|ALL)['\"]", re.I)
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|p\.adjust|padj|FDR|Benjamini[^.;]{0,20}|pvalueCutoff\s*=)[^.;]{0,25}?[<≤=]\s*(0\.\d+)")
QVAL  = re.compile(r"(?:[qQ][- ]?value|qvalueCutoff\s*=)[^.;]{0,25}?[<≤=]\s*(0\.\d+)")
GSS   = re.compile(r"(?:minGSSize|maxGSSize)\s*=\s*(\d+)|gene sets? (?:with|of|containing) (?:at least|fewer than|more than|between|a minimum of|a maximum of)\s*(\d+)", re.I)
NPERM = re.compile(r"(?:nPerm(?:Simple)?\s*=\s*|(\d[\d,]*)\s+permutations)(\d[\d,]*)?", re.I)
KWIN  = re.compile(r"[cC]lusterProfiler(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major not in (3, 4): return None   # clusterProfiler 3.x (Bioc 3.6-3.12) and 4.x (Bioc 3.13-) in the cohort years
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
        "fgsea_versions": sorted(set(FGVER.findall(text))),
        "version_family": fams,
        "ontologies": sorted({(a or b).upper()[:2] if (a or b).upper()[:2] in ("BP", "MF", "CC", "AL") else (a or b) for a, b in ONT.findall(text)}),
        "padj_cutoffs": sorted(set(PADJ.findall(text))),
        "qvalue_cutoffs": sorted(set(QVAL.findall(text))),
        "gs_size_limits": sorted({int(a or b) for a, b in GSS.findall(text) if (a or b)}),
        "nperm": sorted({int((a or b).replace(",", "")) for a, b in NPERM.findall(text) if (a or b)}),
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
        if row["package"] == "clusterProfiler":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "clusterProfiler")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("clusterprofiler_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co, fgv = Counter(), Counter(), Counter(), Counter(), Counter()
ont, padj, qv, gss, npm = Counter(), Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for v in c.get("fgsea_versions", []): fgv[v] += 1
    for o in c["ontologies"]: ont[o] += 1
    for p in c["padj_cutoffs"]: padj[p] += 1
    for q in c["qvalue_cutoffs"]: qv[q] += 1
    for g in c["gs_size_limits"]: gss[g] += 1
    for n in c["nperm"]: npm[n] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("FGSEA VERSIONS:", dict(fgv.most_common(20)))
print("\nontologies:", dict(ont.most_common(10)))
print("padj cutoffs:", dict(padj.most_common(8)))
print("qvalue cutoffs:", dict(qv.most_common(8)))
print("gene-set size limits:", dict(gss.most_common(10)))
print("permutations:", dict(npm.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
