#!/usr/bin/env python3
"""Profile how each cohort paper used scDblFinder.
Mines the text for the choices that select scDblFinder code paths: per-sample
runs (`samples`), cluster-based vs random artificial doublets (`clusters`), a
stated doublet rate (`dbr`), whether the doublets were removed or only flagged,
whether the doublet origins / cell-type combinations were analysed, the other
doublet tools run alongside (DoubletFinder, Scrublet, scds, DoubletDetection,
demuxlet/souporcell-style genetic demultiplexing), the framework (Seurat /
Bioconductor / Scanpy), the platform (10x, multiome, ATAC), and the stated
version. One JSONL record per paper.
Usage: python3 scdblfinder_profile.py            (fetch full texts, cache fallback)
       python3 scdblfinder_profile.py --offline  (survey cache only, no network)
Two sources, recorded per paper in `source`: "fulltext" (Europe PMC JATS body)
or "survey_cache" (the survey's stored evidence sentences; a few hundred
characters per package, so feature counts are LOWER BOUNDS).
As for the earlier audits, the 2026-09-24 run had no route to Europe PMC from
this session, so every record in scdblfinder_profiles.jsonl is source=survey_cache.
The survey's own version column for this package is polluted by neighbouring
tools' versions (DoubletFinder 2.0.x, Scrublet 0.2.x); `versions_all` here
keeps only a version that follows the word scDblFinder.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "scDblFinder named":                     r"scDblFinder|scDBLFinder|scdblfinder",
 "per-sample run (samples= / per library)": r"samples ?=|per[- ](?:sample|library|capture|lane)|each (?:sample|library|capture|lane) (?:separately|individually)|separately for each",
 "cluster-based doublets (clusters=)":    r"clusters ?=|cluster-based|cluster based",
 "doublet rate stated (dbr / % per 1000)": r"\bdbr\b|doublet rate|expected (?:doublet|multiplet)|per (?:1,?000|thousand) cells|0\.8 ?%|multiplet rate",
 "doublets removed":                      r"doublets? (?:were |was )?(?:removed|excluded|filtered|discarded|eliminated)|remov(?:ed|ing|al of) (?:putative |predicted |potential |likely )?doublets|exclud(?:ed|ing) (?:putative |predicted |potential )?doublets",
 "doublet score used / threshold stated": r"doublet score|scDblFinder\.score|score (?:threshold|cutoff|cut-off)|threshold",
 "doublet origins / cell-type combinations analysed": r"mostLikelyOrigin|origin of (?:the )?doublets|heterotypic|homotypic|doublet (?:composition|origin)",
 "DoubletFinder also used":               r"DoubletFinder",
 "Scrublet also used":                    r"Scrublet",
 "scds / cxds / bcds also used":          r"\bscds\b|\bcxds\b|\bbcds\b",
 "DoubletDetection / Solo / other":       r"DoubletDetection|\bSolo\b|DoubletDecon|Chord",
 "genetic demultiplexing (demuxlet, souporcell, vireo, cellSNP, hashing)": r"demuxlet|souporcell|vireo|cellSNP|freemuxlet|HTODemux|hashtag|hashing|CellHashR|demultiplex",
 "Seurat framework":                      r"Seurat",
 "Bioconductor / SingleCellExperiment":   r"SingleCellExperiment|Bioconductor|scater|scran",
 "Scanpy framework":                      r"Scanpy|scanpy|anndata",
 "10x Chromium":                          r"10[xX]|Chromium",
 "multiome / ATAC":                       r"multiome|Multiome|ATAC|scATAC|chromatin accessibility",
 "snRNA-seq (nuclei)":                    r"snRNA|single[- ]nucle|nuclei",
 "spatial / other platform":              r"Visium|Slide-?seq|MERFISH|Parse Biosciences|BD Rhapsody|Drop-?seq|Smart-?seq",
 "CellBender / SoupX (ambient) also used": r"CellBender|SoupX|DecontX|ambient",
 "scDblFinder version stated":            r"scDblFinder(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"per-sample run (samples= / per library)", "cluster-based doublets (clusters=)", "doublet rate stated (dbr / % per 1000)", "doublets removed",
      "doublet score used / threshold stated", "doublet origins / cell-type combinations analysed", "genetic demultiplexing (demuxlet, souporcell, vireo, cellSNP, hashing)",
      "multiome / ATAC", "snRNA-seq (nuclei)", "CellBender / SoupX (ambient) also used"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"scDblFinder(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)", re.I)
RES   = re.compile(r"\bdbr ?= ?(0?\.\d+)|doublet rate[^.;]{0,25}?(\d{1,2}(?:\.\d+)?) ?%|(\d{1,2}(?:\.\d+)?) ?% (?:expected )?doublet", re.I)
MITO  = re.compile(r"(\d{1,2}(?:\.\d+)?) ?% (?:of (?:the |all )?cells )?(?:were |was )?(?:identified|called|flagged|classified|predicted|removed|detected) as doublets|doublets?[^.;]{0,30}?(\d{1,2}(?:\.\d+)?) ?% of (?:the |all )?cells", re.I)
PADJ  = re.compile(r"clusters ?= ?([A-Za-z0-9_.$\"']+)", re.I)
LFC   = re.compile(r"score ?(?:>|>=|≥|above|greater than) ?(0?\.\d+)|threshold (?:of )?(0?\.\d+)", re.I)
DIMS  = re.compile(r"(\d{1,3},?\d{3}) (?:cells|nuclei) (?:per|in each|for each) (?:sample|library|capture)", re.I)
KWIN  = re.compile(r"scDblFinder", re.I)

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    if m.group(1) != "1": return None
    return "1.%s" % m.group(2)

def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = set(VER.findall(text))
    # the survey's version column is not merged for this package (see the module docstring)
    vers  = sorted(vers)
    fams  = sorted({f for f in (family(v) for v in vers) if f})
    c.update({
        "source": source,
        "features": feats,
        "versions_all": vers,
        "version_family": fams,
        "dbr_stated": sorted({a or b or c for a, b, c in RES.findall(text)}),
        "pct_doublets_reported": sorted({a or b for a, b in MITO.findall(text)}),
        "clusters_arg": sorted(set(PADJ.findall(text))),
        "score_thresholds": sorted({a or b for a, b in LFC.findall(text)}),
        "cells_per_sample": sorted(set(DIMS.findall(text))),
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
        if row["package"] == "scDblFinder":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "scDblFinder")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "scDblFinder".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("scdblfinder_profiles.jsonl", "w") as fh:
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
    for r in c["dbr_stated"]: res[r] += 1
    for m in c["pct_doublets_reported"]: mito[m] += 1
    for p in c["clusters_arg"]: padj[p] += 1
    for l in c["score_thresholds"]: lfc[l] += 1
    for d in c["cells_per_sample"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\ndoublet rates stated:", dict(res.most_common(10)))
print("% doublets reported:", dict(mito.most_common(10)))
print("clusters= arguments:", dict(padj.most_common(8)))
print("score thresholds:", dict(lfc.most_common(8)))
print("cells per sample:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
