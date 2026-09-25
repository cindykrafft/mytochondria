#!/usr/bin/env python3
"""Profile how each cohort paper used NumPy.
Mines the text for the operations named (random numbers and permutation /
bootstrap, linear algebra: eig / SVD / lstsq / solve, correlation, polynomial
fitting, interpolation, integration, FFT, histograms and binning, descriptive
statistics: mean / median / std / percentiles, normalisation / z-scores,
smoothing, masking, sorting / unique), the co-libraries and the stated version.
One JSONL record per paper.
Usage: python3 numpy_profile.py            (fetch full texts, cache fallback)
       python3 numpy_profile.py --offline  (survey cache only, no network)
Two sources, recorded per paper in `source`: "fulltext" (Europe PMC JATS body)
or "survey_cache" (the survey's stored evidence sentences; a few hundred
characters per package, so feature counts are LOWER BOUNDS).
As for the earlier audits, the 2026-09-25 run had no route to Europe PMC from
this session, so every record in numpy_profiles.jsonl is source=survey_cache.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "NumPy named":                           r"NumPy|numpy",
 "random numbers / permutation / bootstrap": r"random|permutation|shuffle|bootstrap|resampl|Monte Carlo|seed",
 "eig / SVD / linear algebra":            r"eigen|\beig\b|\bSVD\b|singular value|linalg|matrix (?:inversion|multiplication|decomposition)|least[- ]squares|lstsq|solve",
 "correlation (corrcoef, Pearson, cross-correlation)": r"correlat|corrcoef|Pearson|Spearman",
 "polynomial fitting (polyfit)":          r"polyfit|polynomial fit|polynomial regression|curve fit",
 "interpolation (interp)":                r"interp",
 "integration (trapz, cumsum)":           r"integrat|trapz|trapezoid|area under|cumulative sum|cumsum",
 "FFT / spectral":                        r"\bFFT\b|Fourier|spectr|power spectrum|periodogram",
 "histogram / binning":                   r"histogram|\bbins?\b|binned|digitize",
 "mean / median / std / variance":        r"\bmean\b|median|standard deviation|\bSD\b|\bstd\b|variance|\bSEM\b|standard error",
 "percentiles / quantiles":               r"percentile|quantile|interquartile|\bIQR\b",
 "normalisation / z-score":               r"normali[sz]|z-?score|standardi[sz]|rescal|min-?max",
 "smoothing / convolution / moving average": r"smooth|convol|moving average|rolling|running average|Gaussian filter|Savitzky",
 "masking / thresholding":                r"mask|threshold",
 "sorting / unique / ranking":            r"sort|unique|rank",
 "gradient / derivative / diff":          r"gradient|derivative|\bdiff\b|finite difference",
 "argmax / peak detection":               r"argmax|argmin|peak",
 "nan handling":                          r"\bnan|missing values|NaN",
 "image / array processing":              r"image|pixel|voxel|array processing",
 "SciPy also used":                       r"SciPy|scipy",
 "pandas also used":                      r"pandas",
 "scikit-learn also used":                r"scikit-?learn|sklearn",
 "Matplotlib also used":                  r"[Mm]atplotlib",
 "custom code stated":                    r"custom(?:-written)? (?:Python )?(?:code|script)|in-?house (?:code|script)",
 "NumPy version stated":                  r"NumPy(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+|numpy[^.;(]{0,20}?\d+\.\d+",
}
CI = {"random numbers / permutation / bootstrap", "eig / SVD / linear algebra", "correlation (corrcoef, Pearson, cross-correlation)", "polynomial fitting (polyfit)",
      "interpolation (interp)", "integration (trapz, cumsum)", "FFT / spectral", "histogram / binning", "mean / median / std / variance", "percentiles / quantiles",
      "normalisation / z-score", "smoothing / convolution / moving average", "masking / thresholding", "sorting / unique / ranking", "gradient / derivative / diff",
      "argmax / peak detection", "image / array processing", "custom code stated"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"NumPy(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)|numpy[^.;(]{0,20}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)", re.I)
RES   = re.compile(r"(\d{1,3}) ?(?:bins|bin)", re.I)
MITO  = re.compile(r"(\d{1,2}(?:\.\d+)?)(?:st|nd|rd|th) percentile|(\d{1,2})% percentile", re.I)
PADJ  = re.compile(r"(?:polynomial|degree)[^.;]{0,15}?(\d)|(\d)(?:st|nd|rd|th)[- ](?:order|degree) polynomial", re.I)
LFC   = re.compile(r"(\d{2,6}) (?:bootstrap|permutation|random|iterations|shuffles|resamples)", re.I)
DIMS  = re.compile(r"Python (?:v(?:ersion)?\.?\s*)?(\d\.\d+)", re.I)
KWIN  = re.compile(r"NumPy|numpy", re.I)

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    return "%s.%s" % (m.group(1), m.group(2))

def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = {a or b for a, b in VER.findall(text)}
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
        if row["package"] == "NumPy":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "NumPy")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "NumPy".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("numpy_profiles.jsonl", "w") as fh:
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
