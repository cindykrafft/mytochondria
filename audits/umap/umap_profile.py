#!/usr/bin/env python3
"""Profile how each cohort paper used UMAP (umap-learn / uwot / Seurat / Scanpy).

Mines the full text for the choices that select UMAP code paths: the
implementation the paper reached UMAP through (Scanpy calls umap-learn's
fuzzy_simplicial_set + simplicial_set_embedding; Seurat's RunUMAP defaults to
uwot in R; Monocle/ArchR use uwot), n_neighbors / min_dist / spread / metric
stated, the input space (PCA, Harmony, scVI latent), transform of new data,
supervised / densMAP / parametric variants, cytometry inputs (duplicate rows),
and the stated umap-learn version. One JSONL record per paper.

Usage: python3 umap_profile.py            (fetch full texts, cache fallback)
       python3 umap_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the UMAP evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat and Scanpy audits, the 2026-09-03 run had no route to Europe
PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so
every record in umap_profiles.jsonl is source=survey_cache. Rerun from a host
with Europe PMC access to replace them; the fetch path is unchanged from the
other audits. Version regexes require "umap-learn" or "UMAP" followed within a
few characters by a 0.x version, so that Seurat/Scanpy versions in the same
sentence are not attributed to UMAP.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 "umap-learn named (Python package)":   r"umap-learn|umap\.UMAP|import umap|umap_learn",
 "uwot named (R package)":              r"\buwot\b",
 "Seurat RunUMAP / Seurat also used":   r"RunUMAP|Seurat(?![A-Za-z])",
 "Scanpy also used (calls umap-learn)": r"[Ss]canpy(?![A-Za-z])|sc\.tl\.umap|sc\.pp\.neighbors",
 "Monocle / ArchR / Signac (uwot)":     r"Monocle|ArchR|Signac",
 "n_neighbors stated":                  r"n[_. ]?neighbou?rs|n\.neighbors|number of neighbou?rs[^.]{0,20}\d|neighbou?rs\s*=\s*\d",
 "min_dist stated":                     r"min[_. ]?dist|minimum distance[^.]{0,20}\d",
 "spread stated":                       r"\bspread\s*=\s*\d",
 "metric cosine":                       r"cosine",
 "metric correlation":                  r"metric\s*=\s*['\"]?correlation|correlation (?:distance|metric)",
 "metric euclidean stated":             r"euclidean",
 "n_components / 3D UMAP":              r"n_components|three[- ]dimensional UMAP|3D UMAP|3-D UMAP",
 "input: PCA / PCs":                    r"principal component|\bPCs?\b|PCA",
 "input: Harmony / scVI / latent space":r"Harmony|harmony|scVI|scANVI|latent (?:space|embedding|representation)",
 "transform / projection of new data":  r"transform\(|projected (?:onto|into) the (?:reference )?UMAP|\.transform\b|MapQuery|ProjectUMAP|reference UMAP",
 "supervised UMAP":                     r"supervised UMAP|target_weight",
 "densMAP":                             r"densMAP|densmap",
 "parametric UMAP":                     r"[Pp]arametric UMAP|ParametricUMAP",
 "cytometry input (CyTOF/flow/spectral)": r"CyTOF|mass cytometry|flow cytometry|spectral (?:flow )?cytometry|FlowJo|Cytobank|FCS files?",
 "spatial transcriptomics":             r"Visium|Xenium|MERFISH|spatial transcriptom|CosMx|Slide-seq",
 "random_state / seed stated":          r"random[_. ]?state|random seed|set\.seed|seed\s*=\s*\d",
 "clustering (Leiden / Louvain) on the same graph": r"[Ll]eiden|[Ll]ouvain",
 "UMAP used for clustering (on UMAP coords)": r"cluster(?:ed|ing)? (?:on|in|using|based on)(?: the)? UMAP (?:coordinates|embedding|space)|HDBSCAN|DBSCAN",
 "UMAP on non-single-cell data":        r"spectra|imaging|behaviou?r|neural (?:activity|recording)|electrophysiolog|protein (?:structure|language)|embedding vectors|word embeddings|molecul",
 "umap-learn version stated":           r"(?:umap-learn|UMAP)(?![A-Za-z])[^.;(\n]{0,20}?(?:v(?:ersion)?\.?\s*)?0\.\d+(?:\.\d+)?",
 "snRNA-seq":                           r"single[- ]nucle(?:us|i)|snRNA",
 "scRNA-seq":                           r"single[- ]cell RNA|scRNA",
}
CI = {"n_neighbors stated", "min_dist stated", "metric cosine", "metric euclidean stated",
      "n_components / 3D UMAP", "supervised UMAP", "snRNA-seq", "scRNA-seq", "spatial transcriptomics",
      "random_state / seed stated"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"(?:umap-learn|UMAP)(?![A-Za-z])[^.;(\n]{0,20}?(?:v(?:ersion)?\.?\s*)?(0\.\d+(?:\.\d+)*)")
NNB   = re.compile(r"n[_. ]?neighbou?rs\s*(?:=|of|:|was set to|set to)?\s*(\d{1,3})|(\d{1,3})\s*(?:nearest )?neighbou?rs", re.I)
MIND  = re.compile(r"min[_. ]?dist\s*(?:=|of|:|was set to|set to)?\s*(\d?\.\d+|\d)", re.I)
DIMS  = re.compile(r"(?:dims\s*=\s*1:|(?:first|top)\s+)(\d{1,3})\s*(?:PCs?|principal components|dimensions)", re.I)
KWIN  = re.compile(r"UMAP(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major != 0: return None          # umap-learn has only had 0.x releases
    return "0.%d" % minor

def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = set(VER.findall(text))
    if c.get("version_survey") and c["version_survey"].startswith("0."):
        vers.add(c["version_survey"])   # the survey's own extraction; 1.x/2.x/3.x are other packages
    vers  = sorted(vers)
    fams  = sorted({f for f in (family(v) for v in vers) if f})
    c.update({
        "source": source,
        "features": feats,
        "versions_all": vers,
        "version_family": fams,
        "n_neighbors": sorted({int(a or b) for a, b in NNB.findall(text) if 0 < int(a or b) <= 500}),
        "min_dist": sorted(set(MIND.findall(text))),
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
        if row["package"] == "UMAP":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "UMAP")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, UMAP, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "UMAP".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("umap_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co, jr, yr = Counter(), Counter(), Counter(), Counter(), Counter(), Counter()
nnb, mind, dims = Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for n in c["n_neighbors"]: nnb[n] += 1
    for m in c["min_dist"]: mind[m] += 1
    for d in c["dims"]: dims[d] += 1
    jr[c["journal"]] += 1; yr[c["year"]] += 1
print("\nJOURNAL:", dict(jr.most_common()), "\nYEAR:", dict(sorted(yr.items())))
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nn_neighbors:", dict(nnb.most_common(12)))
print("min_dist:", dict(mind.most_common(12)))
print("dims (PCs):", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
