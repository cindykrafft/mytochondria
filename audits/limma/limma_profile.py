#!/usr/bin/env python3
"""Profile how each cohort paper used limma.

Mines the full text for the choices that select limma code paths:
lmFit/eBayes/topTable, voom (and voomWithQualityWeights/voomLmFit), treat,
duplicateCorrelation/blocking, contrasts.fit/makeContrasts, robust/trend eBayes,
decideTests, the gene-set tests (camera/roast/fry/romer/goana/kegga), removeBatchEffect,
quantile/cyclic-loess normalisation, arrayWeights, microarray vs RNA-seq use, FDR and
logFC cutoffs, and the stated limma version. One JSONL record per paper.

Usage: python3 limma_profile.py            (fetch full texts, cache fallback)
       python3 limma_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the limma evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy and edgeR audits, the 2026-09-09 run had no route to Europe PMC
(www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so every record in
limma_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "limma".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below; limma's function names are
# camelCase/dotted identifiers and matching them exactly is the point.
FEATURES = {
 "lmFit / eBayes / topTable named":      r"lmFit|eBayes|topTable|topTreat|moderated t|empirical Bayes",
 "voom (any variant)":                   r"\bvoom",
 "voomWithQualityWeights / voomLmFit":   r"voomWithQualityWeights|voomLmFit|quality weights",
 "treat / fold-change threshold test":   r"\btreat\(|\bTREAT\b|glmTreat",
 "duplicateCorrelation / block":         r"duplicateCorrelation|consensus correlation|intra-?block|block\s*=|random effect",
 "contrasts.fit / makeContrasts":        r"contrasts\.fit|makeContrasts|contrast matrix",
 "robust / trend eBayes":                r"robust\s*=\s*T|trend\s*=\s*T|robust empirical Bayes|limma-trend|mean-variance trend",
 "decideTests":                          r"decideTests",
 "camera / roast / fry / romer":         r"\bcamera\b|cameraPR|\bmroast\b|\broast\b|\bfry\b|\bromer\b",
 "goana / kegga":                        r"\bgoana\b|\bkegga\b",
 "removeBatchEffect":                    r"removeBatchEffect",
 "quantile / cyclic loess normalisation": r"normalizeBetweenArrays|normalizeQuantiles|quantile[- ]normali[sz]|cyclic[- ]?loess|normalizeCyclicLoess",
 "arrayWeights":                         r"arrayWeights|array weights|sample weights",
 "edgeR also used (TMM/calcNormFactors)": r"edgeR|calcNormFactors|normLibSizes|\bTMM\b|filterByExpr",
 "DESeq2 also used":                     r"DESeq2?",
 "microarray (Affy/Illumina/Agilent)":   r"microarray|Affymetrix|Illumina (?:Human|Mouse)HT|Agilent|BeadChip|\bRMA\b|\baffy\b|\blumi\b",
 "methylation / EPIC / 450K":            r"methylation|EPIC|450[Kk]|minfi|bisulfite|M-value",
 "proteomics / metabolomics":            r"proteom|metabolom|mass spectrometry|DIA-NN|MaxQuant|TMT",
 "pseudo-bulk / single-cell":            r"pseudo[- ]?bulk|single[- ]cell|scRNA",
 "ATAC / ChIP / CUT&RUN":                r"ATAC|ChIP[- ]seq|CUT&(?:RUN|Tag)",
 "adjusted p / FDR / BH":                r"adjusted [pP][- ]?value|Benjamini|\bFDR\b|false discovery rate|padj|\bBH\b",
 "log fold change cutoff":               r"log2?\s*(?:fold[- ]?change|FC)|\blogFC\b|fold[- ]?change[^.]{0,20}[>≥]",
 "batch / covariate in design":          r"batch|covariate|paired|blocking",
 "limma version stated":                 r"limma(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "Bioconductor version stated":          r"Bioconductor[^.;]{0,20}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "R version stated":                     r"\bR\s*(?:v(?:ersion)?\.?\s*)?[34]\.\d",
}
CI = {"treat / fold-change threshold test", "duplicateCorrelation / block", "contrasts.fit / makeContrasts",
      "robust / trend eBayes", "quantile / cyclic loess normalisation", "arrayWeights",
      "microarray (Affy/Illumina/Agilent)", "methylation / EPIC / 450K", "proteomics / metabolomics",
      "pseudo-bulk / single-cell", "adjusted p / FDR / BH", "log fold change cutoff", "batch / covariate in design"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"limma(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"resolution[^.;]{0,30}?(\d\.\d+)", re.I)
MITO  = re.compile(r"(\d{1,2}(?:\.\d)?)\s*%[^.;]{0,40}?mitochondrial|mitochondrial[^.;]{0,60}?(\d{1,2}(?:\.\d)?)\s*%", re.I)
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|p_val_adj|padj|FDR|[qQ][- ]?value|Bonferroni)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
LFC   = re.compile(r"(?:logfc\.threshold|\|?\s*(?:avg_)?log2?\s*(?:fold[- ]?change|FC)\s*\|?|\bLFC\b|fold[- ]?change)[^.;]{0,30}?[>≥=]\s*(\d+(?:\.\d+)?)", re.I)
DIMS  = re.compile(r"(?:dims\s*=\s*1:|(?:first|top)\s+)(\d{1,3})\s*(?:PCs?|principal components|dimensions)?", re.I)
KWIN  = re.compile(r"limma(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major != 3: return None  # limma 3.x since 2008 (3.68 = Bioconductor 3.23, 2026)
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
        if row["package"] == "limma":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "limma")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "limma".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("limma_profiles.jsonl", "w") as fh:
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
