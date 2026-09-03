#!/usr/bin/env python3
"""Profile how each cohort paper used CellPhoneDB.

Mines the full text for the choices that select CellPhoneDB code paths: which of the three
methods was run (statistical / simple / DEG), the permutation settings (`iterations`, `threads`,
`debug_seed`), the expression `threshold`, the p-value cut-off, microenvironments, subsampling,
the v5 scoring and CellSign modules, the output files the paper reports (means /
significant_means / pvalues / relevant_interactions / deconvoluted), and the stated version.
One JSONL record per paper.

Usage: python3 cellphonedb_profile.py            (fetch full texts, cache fallback)
       python3 cellphonedb_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the other audits'
                 *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's stored evidence
                 for the paper -- the CellPhoneDB evidence sentence in paper_software.tsv plus
                 every per-package evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source are LOWER BOUNDS on
                 usage, not measurements of it.

As for the Seurat and Scanpy audits, the 2026-09-03 run had no route to Europe PMC
(www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so every record in
cellphonedb_profiles.jsonl is source=survey_cache. Rerun from a host with Europe PMC access to
replace them; the fetch path is unchanged from the other audits.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

PACKAGE = "CellPhoneDB"

# Case-insensitive unless the token is a code identifier whose case carries meaning.
FEATURES = {
 "statistical method (method 2)":       r"statistical[_ ]analysis|statistical method|cpdb_statistical|permutation|shuffl",
 "simple/basic method (method 1)":      r"cpdb_analysis_method|analysis_method\.call|simple analysis|basic analysis|non-?statistical",
 "DEG method (method 3)":               r"degs_analysis|cpdb_degs|DEG-based|differentially expressed genes.{0,40}CellPhoneDB",
 "iterations stated":                   r"iterations|permutation[s]?\s*(?:=|of|:)?\s*\d{2,}|1,?000 permutation",
 "threshold stated":                    r"threshold\s*=|expressed (?:in|by) (?:more than |at least )?\d{1,2}\s*%|10\s*% of cells|0\.1 threshold",
 "p-value cutoff stated":               r"p[- ]?(?:value)?\s*[<≤]\s*0?\.\d+|significan\w+ (?:at|if) p|pvalue\s*=",
 "means / significant_means reported":  r"significant[_ ]means|means\.txt|mean expression of the (?:ligand|receptor)|interaction mean",
 "pvalues file reported":               r"pvalues?\.txt|p-?values? (?:file|output|matrix)",
 "relevant_interactions reported":      r"relevant[_ ]interactions",
 "deconvoluted reported":               r"deconvoluted",
 "microenvironments":                   r"microenviron|micro-?environment file|spatial(?:ly)? restrict",
 "subsampling":                         r"subsampl|geometric sketch|geosketch",
 "v5 scoring module":                   r"score_interactions|interaction[_ ]score|specificity score|scoring module",
 "CellSign / TF module":                r"CellSign|active[_ ]tfs|transcription factor activit",
 "complexes / heteromers named":        r"heteromer|multi-?subunit|complex(?:es)? of (?:ligand|receptor)|subunit",
 "counts_data / gene ids":              r"counts[_-]data|hgnc[_ ]symbol|ensembl id|gene_name",
 "log-normalised input stated":         r"log-?normali|normalized count|lognorm",
 "database version stated":             r"CellPhoneDB[- ]?(?:database|DB)? ?v(?:ersion)?\.? ?\d|cellphonedb-data",
 "CellPhoneDB version stated":          r"[Cc]ell[Pp]hone[Dd][Bb](?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+(?:\.\d+)*",
 "ktplots / ktplotspy":                 r"ktplot",
 "CellChat also used":                  r"CellChat",
 "NicheNet also used":                  r"NicheNet",
 "LIANA also used":                     r"\bLIANA\b|liana\+",
 "squidpy / omnipath wrapper":          r"[Ss]quidpy|[Oo]mnipath",
 "Seurat / Scanpy upstream":            r"Seurat|Scanpy|SCANPY",
 "spatial data":                        r"Visium|Xenium|MERFISH|spatial transcriptom|cell2location",
 "R / reticulate driver":               r"reticulate|RStudio|\bR package\b",
 "dot plot / heatmap of interactions":  r"dot ?plot|heatmap of (?:the )?interactions|chord (?:diagram|plot)",
}
CS = {"CellPhoneDB version stated"}          # case-sensitive
FEATURES = {k: re.compile(v, 0 if k in CS else re.I) for k, v in FEATURES.items()}

# A bare number after "CellPhoneDB" is usually a citation superscript ("CellPhoneDB 75"), so a
# version must carry an explicit v/version marker or be dotted. CellPhoneDB majors are 1-5.
VER   = re.compile(r"[Cc]ell[Pp]hone[Dd][Bb](?![A-Za-z])[^.;(]{0,25}?"
                   r"(?:v(?:ersion)?\.?\s*(\d+(?:\.\d+)*)|(\d\.\d+(?:\.\d+)*))")
ITER  = re.compile(r"(?:iterations?|permutations?)[^.;]{0,25}?(\d{2,6})|(\d{1,3},?\d{3})\s*(?:iterations|permutations)", re.I)
THR   = re.compile(r"(?:threshold[^.;]{0,20}?(0?\.\d+)|expressed (?:in|by)[^.;]{0,30}?(\d{1,2})\s*%|(\d{1,2})\s*% of (?:the )?cells)", re.I)
PCUT  = re.compile(r"[pP][- ]?(?:value)?s?\s*[<≤]\s*(0?\.\d+)")
KWIN  = re.compile(r"[Cc]ell[Pp]hone[Dd][Bb]")


def near_text(text, window=300):
    """Text within `window` characters of a CellPhoneDB mention.

    The survey-cache text concatenates the evidence snippets of every package the paper used,
    so a bare "1,000 permutations" or "p < 0.05" in it may belong to another tool. Numeric
    settings and versions are therefore read only from the neighbourhood of a CellPhoneDB
    mention. Feature flags stay on the whole text and are paper-level signals.
    """
    spans = [text[max(0, m.start() - window):m.end() + window] for m in KWIN.finditer(text)]
    return " ".join(spans) if spans else ""


def family(v):
    m = re.match(r"(\d+)", v)
    if not m:
        return None
    major = int(m.group(1))
    return "v%d" % major if 1 <= major <= 5 else None


def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    near = near_text(text)
    vers = {a or b for a, b in VER.findall(near)}
    if c.get("version_survey"):
        vers.add(c["version_survey"])
    vers = sorted(v for v in vers if v)
    fams = sorted({f for f in (family(v) for v in vers) if f})
    iters = sorted({(a or b).replace(",", "") for a, b in ITER.findall(near) if (a or b)})
    thrs = sorted({(a or b or cc) for a, b, cc in THR.findall(near) if (a or b or cc)})
    c.update({
        "source": source,
        "features": feats,
        "versions_all": vers,
        "version_family": fams,
        "iterations": iters,
        "thresholds": thrs,
        "pvalue_cutoffs": sorted(set(PCUT.findall(near))),
    })
    if source == "fulltext":
        ctx = []
        for m in KWIN.finditer(text):
            lo = max(0, m.start() - 260); hi = min(len(text), m.end() + 320)
            ctx.append(("..." + text[lo:hi] + "...").strip())
            if len(ctx) >= 3:
                break
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
            rec = {"pmcid": row["pmcid"], "doi": row["doi"], "journal": row["journal"],
                   "year": row["year"], "version_survey": row["version"],
                   "in_methods": row["in_methods"] == "True",
                   "pipeline_stages_survey": row["pipeline_stages"],
                   "evidence_survey": row["evidence_sentence"],
                   "_cache_text": row["evidence_sentence"]}
            cohort.append(rec); by_pmcid[row["pmcid"]] = rec
with gzip.open("../../survey/data/pipelines.jsonl.gz", "rt") as fh:
    for line in fh:
        d = json.loads(line)
        rec = by_pmcid.get(d["pmcid"])
        if rec is None:
            continue
        rec["title"] = d.get("title", "")
        rec["co_packages"] = sorted(p for p in d["packages"] if p != PACKAGE)
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))

print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("cellphonedb_profiles.jsonl", "w") as fh:
    for c in out:
        fh.write(json.dumps(c) + "\n")
full = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)"
      % (len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))

fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
it, th, pc, jr, yr = Counter(), Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for i in c["iterations"]: it[i] += 1
    for t in c["thresholds"]: th[t] += 1
    for p in c["pvalue_cutoffs"]: pc[p] += 1
    jr[c["journal"]] += 1
    yr[c["year"]] += 1
print("\nJOURNALS:", dict(jr.most_common()))
print("YEARS:", dict(sorted(yr.items())))
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common():
    print("  %-40s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS:", dict(vc.most_common(20)))
print("iterations stated:", dict(it.most_common(8)))
print("thresholds stated:", dict(th.most_common(8)))
print("p-value cutoffs:", dict(pc.most_common(8)))
print("\nCO-PACKAGES (top 30):")
for k, n in co.most_common(30):
    print("  %-24s %d" % (k, n))
