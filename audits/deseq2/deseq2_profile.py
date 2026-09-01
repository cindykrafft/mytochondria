#!/usr/bin/env python3
"""Profile how each cohort paper used DESeq2.

Mines the full text for the choices that select DESeq2 code paths:
test type (Wald vs LRT), lfcShrink estimator, filtering and outlier
handling, design complexity, upstream quantifier, data domain, and the
stated significance thresholds. One JSONL record per paper.
"""
import csv, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf

sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 # --- which test / estimator ---
 "LRT (nbinomLRT / reduced model)": r"likelihood[- ]ratio test|nbinomLRT|\bLRT\b|reduced (?:model|formula)",
 "Wald test named":                r"Wald",
 "lfcShrink / shrunken LFC":       r"lfcShrink|shrunk(?:en)? (?:log2? ?)?fold[- ]?change|fold[- ]?change shrinkage|shrinkage of (?:log2? ?)?fold",
 "apeglm":                         r"apeglm",
 "ashr":                           r"\bashr\b",
 "normal shrinkage / betaPrior":   r"betaPrior|normal shrinkage",
 "lfcThreshold used":              r"lfcThreshold|null hypothesis of a (?:log2? ?)?fold",
 # --- filtering / outliers ---
 "independent filtering mentioned":r"independent[- ]filter|independentFiltering",
 "pre-filter low counts":          r"(?:pre[- ]?filter|filter(?:ed|ing)?(?: out)?)[^.]{0,80}(?:low|fewer than|less than|minimum|< ?\d+|at least \d+)[^.]{0,40}(?:read|count)|rowSums\s*\(",
 "Cook's / outlier handling":      r"Cook'?s|cooksCutoff|outlier (?:detection|replacement|filtering)[^.]{0,60}DESeq",
 "IHW instead of BH":              r"\bIHW\b|independent hypothesis weighting",
 # --- design ---
 "batch/covariate in design":      r"design[^.]{0,80}(?:batch|sex|age|donor|covariate)|(?:adjust|control|account)(?:ed|ing)? for[^.]{0,50}(?:batch|sex|age|donor)|~\s*\w+\s*\+",
 "interaction term":               r"interaction term|design[^.]{0,60}[:*][^.]{0,30}|interaction (?:effect|model)[^.]{0,60}DESeq",
 "paired design":                  r"paired[^.]{0,60}(?:design|analysis|sample)|patient[- ]matched|~\s*(?:patient|subject|donor|pair)\s*\+",
 "time course":                    r"time[- ]?course|longitudinal[^.]{0,60}expression",
 # --- replication level ---
 "no/low replicates hint":         r"no (?:biological )?replicat|single replicate|n\s*=\s*[12]\b[^.]{0,60}(?:per|each)|duplicate[s]? (?:per|for each)",
 "triplicate+":                    r"triplicate|n\s*=\s*[3-9][^.]{0,50}(?:per|each)|three (?:biological )?replicates",
 # --- upstream / import path ---
 "tximport (salmon/kallisto/RSEM)":r"tximport|salmon|kallisto|\bRSEM\b",
 "featureCounts/HTSeq counts":     r"featureCounts|HTSeq|htseq[- ]count",
 "10x/single-cell on DESeq2":      r"(?:single[- ]cell|snRNA|scRNA|10[xX] Genomics|Cell Ranger)[^.]{0,200}DESeq|DESeq[^.]{0,200}(?:single[- ]cell|pseudobulk)|pseudobulk",
 # --- non-RNA-seq domains (known-delicate uses) ---
 "ATAC/ChIP (DiffBind etc.)":      r"DiffBind|ATAC[^.]{0,120}DESeq|DESeq[^.]{0,120}ATAC|ChIP[- ]seq[^.]{0,120}DESeq|differential(?:ly)? accessib",
 "microbiome (phyloseq/16S)":      r"phyloseq|16S[^.]{0,120}DESeq|DESeq[^.]{0,120}(?:16S|microbio|amplicon|ASV|OTU)",
 "proteomics/other counts":        r"(?:proteomic|metabolomic|CRISPR screen|sgRNA|barcode)[^.]{0,120}DESeq|DESeq[^.]{0,120}(?:proteomic|metabolomic|sgRNA|guide)",
 # --- downstream use of DESeq2 stats ---
 "GSEA on DESeq2 stat/ranking":    r"(?:rank|ranked|ranking)[^.]{0,80}(?:DESeq|Wald|stat)|fgsea|GSEA[^.]{0,100}DESeq|DESeq[^.]{0,100}GSEA",
 "vst/rlog transform":             r"\bvst\b|variance[- ]stabiliz|rlog|regularized log",
 "DESeq2 normalization only":      r"DESeq2?[^.]{0,60}normaliz|normaliz[^.]{0,60}DESeq2?|median[- ]of[- ]ratios|size factor",
}
FEATURES = {k: re.compile(v, re.I if k not in ("Wald test named","apeglm","ashr","IHW instead of BH") else 0)
            for k, v in FEATURES.items()}

VER    = re.compile(r"DESeq2?[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
PADJ   = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|padj|FDR|[qQ][- ]?value)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
LFCCUT = re.compile(r"(?:\|?\s*log2?\s*(?:fold[- ]?change|FC)\s*\|?|\bLFC\b|fold[- ]?change)[^.;]{0,30}?[>≥]\s*(\d+(?:\.\d+)?)", re.I)
DWIN   = re.compile(r"DESeq2?")

def profile(c):
    raw, why = E.fetch(c["pmcid"])
    if not raw:
        c["profile_error"] = why; return c
    try:
        root = ET.fromstring(raw)
    except Exception:
        c["profile_error"] = "parse"; return c
    E._strip_refs(root)
    body = root.find(".//body")
    text = re.sub(r"\s+", " ", " ".join(body.itertext())) if body is not None else ""
    if not text:
        c["profile_error"] = "empty_body"; return c
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = sorted(set(VER.findall(text)))
    padj  = sorted(set(PADJ.findall(text)))
    lfc   = sorted(set(LFCCUT.findall(text)))
    ctx = []
    for m in DWIN.finditer(text):
        lo = max(0, m.start()-260); hi = min(len(text), m.end()+320)
        ctx.append(("..."+text[lo:hi]+"...").strip())
        if len(ctx) >= 3: break
    c.update({"features": feats, "versions_all": vers,
              "padj_cutoffs": padj, "lfc_cutoffs": lfc, "context": ctx})
    return c

cohort = []
with open("../../survey/data/paper_software.tsv") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["package"] == "DESeq2":
            cohort.append({"pmcid": row["pmcid"], "doi": row["doi"],
                           "journal": row["journal"], "year": row["year"],
                           "version_survey": row["version"],
                           "evidence_survey": row["evidence_sentence"]})
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("deseq2_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
ok = [c for c in out if "profile_error" not in c]
print("profiled %d/%d" % (len(ok), len(out)))
from collections import Counter
fc, vc, pc = Counter(), Counter(), Counter()
for c in ok:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for p in c["padj_cutoffs"]: pc[p] += 1
print("\nFEATURES (papers):")
for k, n in fc.most_common(): print("  %-42s %d" % (k, n))
print("\nVERSIONS (top 15):", dict(vc.most_common(15)))
print("\npadj cutoffs:", dict(pc.most_common(8)))
