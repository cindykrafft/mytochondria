#!/usr/bin/env python3
"""Profile how each cohort paper used edgeR.

Mines the full text for the choices that select edgeR code paths:
filterByExpr, TMM/normLibSizes, estimateDisp, the test used (glmQLFit/glmQLFTest,
glmFit/glmLRT, exactTest, voom/limma), topTags/FDR and logFC cutoffs, cpm/rpkm,
gene-set tests, pseudo-bulk single-cell use, and the stated edgeR version.
One JSONL record per paper.

Usage: python3 edger_profile.py            (fetch full texts, cache fallback)
       python3 edger_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the edgeR evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat audit, the 2026-09-02 run had no route to Europe PMC (www.ebi.ac.uk denied by the
session's egress policy; NCBI likewise), so every record in
edger_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "edgeR".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below; edgeR's function names are
# camelCase identifiers and matching them exactly is the point.
FEATURES = {
 "filterByExpr / low-count filter":     r"filterByExpr|filter(?:ed|ing)? (?:out )?(?:low(?:ly)?[- ]expressed|lowly|genes with (?:low|fewer|less than)|low[- ]count)|CPM\s*[>≥]|counts? per million[^.]{0,40}(?:>|≥|greater|at least|above)",
 "TMM / normLibSizes / calcNormFactors": r"\bTMM\b|trimmed mean of M|calcNormFactors|normLibSizes",
 "RLE / upperquartile named":            r"\bRLE\b|upper[- ]?quartile",
 "estimateDisp / dispersion":            r"estimateDisp|estimate(?:Common|Tagwise|Trended|GLM\w*)Disp|dispersion",
 "glmQLFit / QL F-test":                 r"glmQLF|quasi[- ]likelihood|\bQL\b F|QL[- ]F",
 "glmFit / glmLRT":                      r"glmFit|glmLRT|likelihood[- ]ratio test",
 "exactTest":                            r"exactTest|exact test",
 "glmTreat / TREAT":                     r"glmTreat|\bTREAT\b",
 "voom / limma":                         r"\bvoom|limma",
 "DESeq2 also used":                     r"DESeq2?",
 "topTags / decideTests":                r"topTags|decideTests",
 "adjusted p / FDR / BH":                r"adjusted [pP][- ]?value|Benjamini|\bFDR\b|false discovery rate|padj|\bBH\b",
 "log fold change cutoff":               r"log2?\s*(?:fold[- ]?change|FC)|\blogFC\b|fold[- ]?change[^.]{0,20}[>≥]",
 "cpm / logCPM / rpkm / TPM":            r"\bcpm\b|\bCPM\b|logCPM|log2?[- ]?CPM|\brpkm\b|\bRPKM\b|\bTPM\b",
 "gene set (camera/fry/roast/goana/kegga)": r"\bcamera\b|\bfry\b|\broast\b|\bgoana\b|\bkegga\b|cameraPR",
 "diffSplice / splicing":                r"diffSplice|differential (?:exon|splicing)",
 "pseudo-bulk / single-cell":            r"pseudo[- ]?bulk|Seurat2PB|single[- ]cell|scRNA",
 "ATAC / ChIP / CUT&RUN / methylation":  r"ATAC|ChIP[- ]seq|CUT&(?:RUN|Tag)|methylation|bisulfite|RRBS",
 "CRISPR screen / sgRNA":                r"CRISPR|sgRNA|guide RNA|processAmplicons",
 "featureCounts / Rsubread":             r"featureCounts|Rsubread",
 "Salmon / kallisto / tximport":         r"[Ss]almon|kallisto|tximport|catchSalmon|catchKallisto",
 "batch / covariate in design":          r"batch|covariate|paired|blocking|random effect",
 "no replicates / dispersion set":       r"no (?:biological )?replicates|without replicates|dispersion (?:was )?set to|BCV of",
 "edgeR version stated":                 r"edgeR(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "Bioconductor version stated":          r"Bioconductor[^.;]{0,20}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "R version stated":                     r"\bR\s*(?:v(?:ersion)?\.?\s*)?[34]\.\d",
}
CI = {"filterByExpr / low-count filter", "RLE / upperquartile named", "estimateDisp / dispersion", "glmQLFit / QL F-test",
      "glmFit / glmLRT", "exactTest", "adjusted p / FDR / BH", "log fold change cutoff", "diffSplice / splicing",
      "pseudo-bulk / single-cell", "batch / covariate in design", "no replicates / dispersion set"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"edgeR(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"resolution[^.;]{0,30}?(\d\.\d+)", re.I)
MITO  = re.compile(r"(\d{1,2}(?:\.\d)?)\s*%[^.;]{0,40}?mitochondrial|mitochondrial[^.;]{0,60}?(\d{1,2}(?:\.\d)?)\s*%", re.I)
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|p_val_adj|padj|FDR|[qQ][- ]?value|Bonferroni)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
LFC   = re.compile(r"(?:logfc\.threshold|\|?\s*(?:avg_)?log2?\s*(?:fold[- ]?change|FC)\s*\|?|\bLFC\b|fold[- ]?change)[^.;]{0,30}?[>≥=]\s*(\d+(?:\.\d+)?)", re.I)
DIMS  = re.compile(r"(?:dims\s*=\s*1:|(?:first|top)\s+)(\d{1,3})\s*(?:PCs?|principal components|dimensions)?", re.I)
KWIN  = re.compile(r"edgeR(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major not in (3, 4): return None  # edgeR 3.x (2012-2023) and 4.x (Oct 2023-)
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
        if row["package"] == "edgeR":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "edgeR")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("edger_profiles.jsonl", "w") as fh:
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
