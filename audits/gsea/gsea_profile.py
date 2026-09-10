#!/usr/bin/env python3
"""Profile how each cohort paper used GSEA (the GSEA-MSigDB desktop / command-line
application).

Mines the text for the choices that select GSEA code paths: GSEA vs GSEAPreranked, the
ranking metric, the permutation type, the number of permutations, the weighting scheme,
the FDR/NES cutoffs quoted, gene-set collection (Hallmark, C2/KEGG/Reactome, C5/GO),
probe collapse, the stated GSEA version, and which other GSEA implementations (fgsea,
clusterProfiler, GSEApy, WebGestalt) appear.  One JSONL record per paper.

Usage: python3 gsea_profile.py            (fetch full texts, cache fallback)
       python3 gsea_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the GSEA evidence sentence in
                 paper_software.tsv plus every per-package evidence snippet in
                 pipelines.jsonl.gz.  A few hundred characters per package, so
                 feature counts from this source are LOWER BOUNDS on usage, not
                 measurements of it.

As for the Seurat and Scanpy audits, the 2026-09-09 run had no route to Europe PMC
(www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so every record in
gsea_profiles.jsonl is source=survey_cache.  Rerun from a host with Europe PMC access to
replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "GSEA" and a 2.x/3.x/4.x version.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 "GSEAPreranked / preranked":          r"pre-?ranked|GSEAPreranked|GseaPreranked",
 "GSEA desktop / Broad / MSigDB named": r"GSEA (?:desktop|software|application|v?\d)|Broad Institute|MSigDB|Molecular Signatures Database",
 "Hallmark gene sets":                 r"hallmark",
 "KEGG / Reactome / C2 sets":          r"KEGG|Reactome|\bC2\b|curated gene sets",
 "GO / C5 sets":                       r"Gene Ontology|\bGO\b|\bC5\b",
 "Signal2Noise / signal-to-noise":     r"signal[- ]?to[- ]?noise|Signal2Noise",
 "t-test metric":                      r"t-?test|tTest",
 "log2 ratio / fold-change ranking":   r"log2?[- ]?(?:fold|ratio)|fold[- ]?change|ratio of classes",
 "ranked by DESeq2/limma/edgeR statistic": r"DESeq2|limma|edgeR|Wald|shrunken",
 "phenotype permutation":              r"phenotype permutation|permut\w+ (?:the )?(?:phenotype|sample|class) labels|sample permutation",
 "gene-set permutation":               r"gene[- ]?set permutation|permut\w+ (?:the )?gene sets",
 "number of permutations stated":      r"\b1,?000 permutations|\b\d{2,5} permutations|permutations\s*=\s*\d+|nperm",
 "weighted / classic scoring":         r"weighted|classic|enrichment statistic|scoring scheme|p\s*=\s*1\b",
 "FDR cutoff quoted":                  r"FDR|q-?value|false discovery",
 "FDR < 0.25 quoted":                  r"(?:FDR|q)[^.;]{0,20}?(?:<|≤|less than|below)\s*0?\.25",
 "NES quoted":                         r"\bNES\b|normali[sz]ed enrichment score",
 "nominal p-value quoted":             r"nominal p|NOM p",
 "leading edge":                       r"leading[- ]edge",
 "collapse / probe / chip":            r"collapse|probe[- ]?set|\.chip\b|chip platform",
 "min/max gene set size stated":       r"gene sets? (?:with |of )?(?:fewer|less|more) than \d+|set_min|set_max|(?:minimum|maximum) (?:gene )?set size|between \d+ and \d+ genes",
 "single-cell / pseudobulk input":     r"single[- ]cell|scRNA|pseudobulk|Seurat|Scanpy",
 "fgsea also":                         r"fgsea",
 "clusterProfiler also":               r"clusterProfiler|gseGO|gseKEGG",
 "GSEApy / gseapy also":               r"GSEApy|gseapy",
 "WebGestalt / other web GSEA":        r"WebGestalt|Enrichr|GenePattern",
 "ssGSEA / GSVA":                      r"ssGSEA|single[- ]sample GSEA|GSVA",
 "GSEA version stated":                r"GSEA(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?[234]\.\d",
 "MSigDB version stated":              r"MSigDB[^.;(]{0,15}?v?\s*\d+\.\d",
}
CI = {"GSEAPreranked / preranked", "Hallmark gene sets", "Signal2Noise / signal-to-noise", "t-test metric",
      "log2 ratio / fold-change ranking", "phenotype permutation", "gene-set permutation",
      "number of permutations stated", "weighted / classic scoring", "FDR cutoff quoted", "FDR < 0.25 quoted",
      "nominal p-value quoted", "leading edge", "collapse / probe / chip", "min/max gene set size stated",
      "single-cell / pseudobulk input", "fgsea also", "ssGSEA / GSVA"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"GSEA(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?([234]\.\d+(?:\.\d+)*)")
NPERM = re.compile(r"\b(\d{2,5}|1,000|10,000)\s+permutations", re.I)
PADJ  = re.compile(r"(?:FDR|q-?value|false discovery rate)[^.;]{0,25}?[<≤]\s*(0\.\d+)", re.I)
NESC  = re.compile(r"\|?NES\|?[^.;]{0,15}?[>≥]\s*(\d(?:\.\d+)?)")
KWIN  = re.compile(r"GSEA(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    return "%s.%s" % (m.group(1), m.group(2))
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
        "nperm": sorted(set(NPERM.findall(text))),
        "fdr_cutoffs": sorted(set(PADJ.findall(text))),
        "nes_cutoffs": sorted(set(NESC.findall(text))),
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
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
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
npc, fdrc, nesc = Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for r in c["nperm"]: npc[r] += 1
    for p in c["fdr_cutoffs"]: fdrc[p] += 1
    for l in c["nes_cutoffs"]: nesc[l] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\npermutations stated:", dict(npc.most_common(10)))
print("FDR cutoffs:", dict(fdrc.most_common(8)))
print("NES cutoffs:", dict(nesc.most_common(8)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
