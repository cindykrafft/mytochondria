#!/usr/bin/env python3
"""Profile how each cohort paper used Matplotlib.
Mines the text for the plot types named (histograms, box plots, violin plots /
KDE, heatmaps and colour scales, log scales, spectrograms / PSD, contours,
hexbin / 2D density, error bars), the co-libraries and the stated version.
One JSONL record per paper.
Usage: python3 matplotlib_profile.py            (fetch full texts, cache fallback)
       python3 matplotlib_profile.py --offline  (survey cache only, no network)
Two sources, recorded per paper in `source`: "fulltext" (Europe PMC JATS body)
or "survey_cache" (the survey's stored evidence sentences; a few hundred
characters per package, so feature counts are LOWER BOUNDS).
As for the earlier audits, the 2026-10-01 run had no route to Europe PMC from
this session, so every record in matplotlib_profiles.jsonl is source=survey_cache.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "Matplotlib named":                      r"[Mm]atplotlib",
 "histogram":                             r"histogram|\bhist\b|\bbins?\b|binned",
 "box plot":                              r"box[- ]?(?:and[- ]whisker )?plot|boxplot|whisker|interquartile|\bIQR\b",
 "violin plot / KDE":                     r"violin|kernel density|\bKDE\b",
 "heatmap / colormap / colour scale":     r"heat ?map|colou?r ?map|cmap|colou?r ?scale|colou?r ?bar|imshow|pcolor",
 "log / symlog scale":                    r"log(?:arithmic)? scale|log[- ]scale|symlog|log10|log2",
 "spectrogram / PSD / spectral":          r"spectrogram|specgram|power spectr|spectral density|\bPSD\b|Welch|periodogram|coheren",
 "contour":                               r"contour",
 "hexbin / 2D density":                   r"hexbin|hexagonal bin|2D histogram|hist2d|density plot",
 "error bars / mean +- SEM":              r"error ?bar|\bSEM\b|standard error|confidence interval|mean ?[\u00b1+]",
 "scatter / line plots":                  r"scatter|line plot|line graph",
 "3D plotting":                           r"3D|three-dimensional|mplot3d",
 "pie / stacked plots":                   r"pie chart|stacked|stackplot",
 "seaborn also used":                     r"seaborn",
 "NumPy also used":                       r"NumPy|numpy",
 "SciPy also used":                       r"SciPy|scipy",
 "pandas also used":                      r"pandas",
 "custom code stated":                    r"custom(?:-written)? (?:Python )?(?:code|script)|in-?house (?:code|script)",
 "Matplotlib version stated":             r"[Mm]atplotlib[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"histogram", "box plot", "violin plot / KDE", "heatmap / colormap / colour scale", "log / symlog scale", "spectrogram / PSD / spectral",
      "contour", "hexbin / 2D density", "error bars / mean +- SEM", "scatter / line plots", "pie / stacked plots", "custom code stated"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Mm]atplotlib[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"(\d{1,3}) ?(?:bins|bin)", re.I)
MITO  = re.compile(r"(\d{1,2}(?:\.\d+)?)(?:st|nd|rd|th) percentile|(\d{1,2})% percentile", re.I)
PADJ  = re.compile(r"(?:polynomial|degree)[^.;]{0,15}?(\d)|(\d)(?:st|nd|rd|th)[- ](?:order|degree) polynomial", re.I)
LFC   = re.compile(r"(\d{2,6}) (?:bootstrap|permutation|random|iterations|shuffles|resamples)", re.I)
DIMS  = re.compile(r"Python (?:v(?:ersion)?\.?\s*)?(\d\.\d+)", re.I)
KWIN  = re.compile(r"[Mm]atplotlib")

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
        "bin_counts": sorted(set(RES.findall(text))),
        "percentiles": sorted({a or b for a, b in MITO.findall(text)}),
        "poly_degrees": sorted({a or b for a, b in PADJ.findall(text)}),
        "resample_counts": sorted(set(LFC.findall(text))),
        "python_versions": sorted(set(DIMS.findall(text))),
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
        if row["package"] == "Matplotlib":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "Matplotlib")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Matplotlib".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("matplotlib_profiles.jsonl", "w") as fh:
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
    for r in c["bin_counts"]: res[r] += 1
    for m in c["percentiles"]: mito[m] += 1
    for p in c["poly_degrees"]: padj[p] += 1
    for l in c["resample_counts"]: lfc[l] += 1
    for d in c["python_versions"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nbin counts:", dict(res.most_common(10)))
print("percentiles named:", dict(mito.most_common(10)))
print("polynomial degrees:", dict(padj.most_common(8)))
print("resample counts:", dict(lfc.most_common(8)))
print("Python versions:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
