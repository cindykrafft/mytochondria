#!/usr/bin/env python3
"""Profile how each cohort paper used Scrublet (and the other doublet tools the
survey groups with it).

The survey files doublet-detection tools under one package name, `scDblFinder`,
with aliases `scDblFinder`, `DoubletFinder` and `Scrublet`. This script takes
that whole group as the cohort and records which tool each paper names, so
that the Scrublet-specific counts can be read off. It mines the choices that
select Scrublet code paths: the expected doublet rate, a stated threshold,
whether Scanpy's port (`sc.pp.scrublet` / `scanpy.external`) was used,
per-sample runs, default parameters, and the stated Scrublet version.
One JSONL record per paper.

Usage: python3 scrublet_profile.py            (fetch full texts, cache fallback)
       python3 scrublet_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the evidence sentence in
                 paper_software.tsv plus every per-package evidence snippet in
                 pipelines.jsonl.gz. A few hundred characters per package, so
                 feature counts from this source are LOWER BOUNDS on usage,
                 not measurements of it.

As for the Seurat and Scanpy audits, the 2026-09-03 run had no route to Europe
PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so
every record in scrublet_profiles.jsonl is source=survey_cache. Rerun from a
host with Europe PMC access to replace them; the fetch path is unchanged from
the other audits. Version regexes require a word boundary after "Scrublet".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

PACKAGE = "scDblFinder"   # the survey's name for the doublet-tool group

FEATURES = {
 "Scrublet named":                      r"[Ss]crublet",
 "DoubletFinder named":                 r"DoubletFinder",
 "scDblFinder named":                   r"scDblFinder",
 "other doublet tool (DoubletDetection/DoubletDecon/scds/Solo/DoubletDecon)": r"DoubletDetection|DoubletDecon|\bscds\b|\bSolo\b|scvi-tools[^.]{0,40}doublet",
 "Scanpy port (sc.pp.scrublet / scanpy.external)": r"sc\.pp\.scrublet|sce?\.pp\.scrublet|scanpy\.external|scanpy'?s? (?:implementation|wrapper|version) of [Ss]crublet|[Ss]crublet[^.]{0,40}(?:in|via|through|within) [Ss]canpy",
 "Scanpy also used":                    r"[Ss]canpy(?![A-Za-z])",
 "Seurat also used":                    r"Seurat(?![A-Za-z])",
 "expected doublet rate stated":        r"expected[_ ]doublet[_ ]rate|expected (?:doublet|multiplet) rate|doublet rate[^.]{0,40}\d+(?:\.\d+)?\s*%|\d+(?:\.\d+)?\s*%[^.]{0,30}(?:expected )?doublet rate",
 "threshold stated":                    r"(?:doublet[- ]score|threshold)[^.]{0,50}(?:>|<|≥|≤|above|below|of|at|=)\s*0\.\d+|threshold[^.]{0,30}(?:manually|adjust|set)",
 "score used to filter (removed cells)": r"(?:doublet[s]?|cells?)[^.]{0,60}(?:remov|filter|exclud|discard)|(?:remov|filter|exclud|discard)[^.]{0,60}doublet",
 "run per sample / library":            r"(?:per|each|every|individual|separately for each)[- ](?:sample|library|lane|batch|channel|run)|separately",
 "default parameters":                  r"default (?:parameters|settings|values|arguments)",
 "sim_doublet_ratio / n_neighbors / n_prin_comps stated": r"sim_doublet_ratio|n_neighbors|n_prin_comps|min_gene_variability_pctl|min_counts|min_cells",
 "DoubletFinder pK / pN / homotypic stated": r"\bpK\b|\bpN\b|homotypic",
 "multiplexing ground truth (demuxlet/hashing)": r"demuxlet|souporcell|vireo|freemuxlet|hashtag|\bHTO\b|cell hashing|CellHashing|MULTI-seq",
 "snRNA-seq":                           r"single[- ]nucle(?:us|i)|snRNA",
 "10x Genomics":                        r"10[xX] Genomics|Chromium|Cell Ranger|cellranger",
 "Scrublet version stated":             r"[Ss]crublet(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"expected doublet rate stated", "threshold stated", "score used to filter (removed cells)",
      "run per sample / library", "default parameters", "snRNA-seq"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Ss]crublet(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
EDR   = re.compile(r"(?:expected[_ ](?:doublet|multiplet)[_ ]rate|doublet rate)[^.;]{0,30}?(\d+(?:\.\d+)?)\s*%|(\d+(?:\.\d+)?)\s*%[^.;]{0,30}?(?:expected )?doublet rate|expected_doublet_rate\s*=\s*(0\.\d+)", re.I)
THR   = re.compile(r"(?:doublet[- ]score|threshold)[^.;]{0,50}?(?:>|<|≥|≤|above|below|of|at|=)\s*(0\.\d+)", re.I)
KWIN  = re.compile(r"[Ss]crublet(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    if int(m.group(1)) != 0: return None   # scrublet has only had 0.x releases; a 1.x/3.x here is a neighbouring package's version (Scanpy, R) caught by the window
    return "%s.%s" % (m.group(1), m.group(2))

def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = set(VER.findall(text))
    if c.get("version_survey") and "Scrublet named" in feats and re.search(r"[Ss]crublet[^.;]{0,25}" + re.escape(c["version_survey"]), text):
        vers.add(c["version_survey"])     # the survey's own extraction, only if it sits next to "Scrublet"
    vers  = sorted(vers)
    fams  = sorted({f for f in (family(v) for v in vers) if f})
    tools = [t for t in ("Scrublet named", "DoubletFinder named", "scDblFinder named") if t in feats]
    c.update({
        "source": source,
        "features": feats,
        "tools_named": [t.split(" ")[0] for t in tools],
        "scrublet_versions": vers,
        "scrublet_version_family": fams,
        "expected_doublet_rates": sorted({a or b or c_ for a, b, c_ in EDR.findall(text)}),
        "thresholds": sorted(set(THR.findall(text))),
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
        if row["package"] == PACKAGE:
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != PACKAGE)
        # Evidence snippets only (the pipeline_stages strings put other
        # packages' versions within a few characters of the tool name).
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort (survey package %r):" % PACKAGE, len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("scrublet_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
scrub = [c for c in out if "Scrublet named" in c["features"]]
print("papers naming Scrublet in the cached evidence: %d of %d (lower bound)" % (len(scrub), len(out)))
print("journals (Scrublet-naming papers):", dict(Counter(c["journal"] for c in scrub)))
print("years    (Scrublet-naming papers):", dict(sorted(Counter(c["year"] for c in scrub).items())))
fc, fcs, vc, fam, co = Counter(), Counter(), Counter(), Counter(), Counter()
edr, thr = Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    if c in scrub:
        for f in c["features"]: fcs[f] += 1
    for v in c["scrublet_versions"]: vc[v] += 1
    for f in c["scrublet_version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for e in c["expected_doublet_rates"]: edr[e] += 1
    for t in c["thresholds"]: thr[t] += 1
print("\nFEATURES (papers; whole doublet-tool cohort / Scrublet-naming papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-72s %4d  %4d" % (k, n, fcs[k]))
print("\nSCRUBLET VERSION FAMILY:", dict(fam.most_common()))
print("SCRUBLET VERSIONS:", dict(vc.most_common(20)))
print("expected doublet rates:", dict(edr.most_common(10)))
print("thresholds:", dict(thr.most_common(10)))
print("\nCO-PACKAGES (top 30):")
for k, n in co.most_common(30): print("  %-24s %d" % (k, n))
