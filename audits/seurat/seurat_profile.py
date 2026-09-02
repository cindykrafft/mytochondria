#!/usr/bin/env python3
"""Profile how each cohort paper used Seurat.

Mines the full text for the choices that select Seurat code paths:
normalisation (LogNormalize vs SCTransform), variable-feature selection,
scaling/regression, dimensionality and clustering parameters, integration
route (CCA/RPCA anchors, Harmony, v5 IntegrateLayers), the differential-
expression test and thresholds, module/cell-cycle scoring, QC filters,
label transfer, and the stated Seurat version. One JSONL record per paper.

Usage: python3 seurat_profile.py            (fetch full texts, cache fallback)
       python3 seurat_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the Seurat evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

The 2026-09-02 run had no route to Europe PMC (www.ebi.ac.uk denied by the
session's egress policy; NCBI likewise), so every record in
seurat_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "Seurat" so that SeuratWrappers,
SeuratData, SeuratObject and SeuratPipe version strings are not counted.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below; Seurat's function names are
# CamelCase identifiers and matching them exactly is the point.
FEATURES = {
 # --- normalisation ---
 "NormalizeData / LogNormalize":       r"NormalizeData|LogNormali[sz]e|log[- ]normali[sz](?:ed|ation)[^.]{0,80}(?:Seurat|10,?000|scale factor)",
 "scale factor 10,000 stated":         r"scale[.\s]factor[^.]{0,20}10,?000|10,?000[^.]{0,40}(?:scale factor|scaling factor)|1e4",
 "SCTransform":                        r"SCTransform|sctransform",
 "SCTransform v2 / glmGamPoi":         r"vst\.flavor|glmGamPoi|SCTransform[^.]{0,40}v2|sctransform v2",
 "CLR (ADT / CITE-seq)":               r"\bCLR\b|centered log[- ]ratio|CITE[- ]seq|antibody[- ]derived tag",
 # --- feature selection / scaling ---
 "FindVariableFeatures":               r"FindVariableFeatures|FindVariableGenes|(?:highly )?variable (?:genes|features)[^.]{0,60}(?:Seurat|vst|2,?000)",
 "2,000 variable features":            r"2,?000 (?:most )?(?:highly )?variable (?:genes|features)|nfeatures\s*=\s*2000",
 "ScaleData":                          r"ScaleData",
 "regress out (vars.to.regress)":      r"vars\.to\.regress|regress(?:ed|ing)? out|regressed (?:for|against)",
 # --- reduction / clustering ---
 "RunPCA / PCs stated":                r"RunPCA|principal components?[^.]{0,80}(?:Seurat|dims|top \d+)|\bPCs?\b[^.]{0,40}(?:were|was) (?:used|selected|retained)",
 "ElbowPlot / JackStraw":              r"ElbowPlot|JackStraw|elbow plot",
 "FindNeighbors":                      r"FindNeighbors|shared nearest[- ]neigh|\bSNN\b",
 "FindClusters":                       r"FindClusters",
 "Louvain named":                      r"Louvain",
 "Leiden named":                       r"Leiden",
 "resolution stated":                  r"resolution[^.]{0,30}(?:of |= ?|set to )?\d\.\d+|resolution parameter",
 "RunUMAP":                            r"RunUMAP|UMAP",
 "RunTSNE":                            r"RunTSNE|t-?SNE",
 # --- integration / batch ---
 "CCA/anchor integration (v3/v4)":     r"FindIntegrationAnchors|IntegrateData|canonical correlation|\bCCA\b|anchor[- ]based integration|integration anchors",
 "RPCA":                               r"\bRPCA\b|reciprocal PCA",
 "IntegrateLayers (v5)":               r"IntegrateLayers|JoinLayers|split\(.{0,40}layer|Seurat v5 (?:integration|layers)",
 "Harmony":                            r"Harmony|RunHarmony",
 "SCT-based integration":              r"SelectIntegrationFeatures|PrepSCTIntegration|normalization\.method\s*=\s*['\"]SCT",
 "sketch-based (v5)":                  r"SketchData|sketch(?:ed|ing)?[^.]{0,40}(?:cells|Seurat)|BPCells",
 "fastMNN / Seurat wrapper":           r"fastMNN|RunFastMNN|SeuratWrappers",
 # --- differential expression ---
 "FindMarkers":                        r"FindMarkers",
 "FindAllMarkers":                     r"FindAllMarkers",
 "Wilcoxon named":                     r"Wilcoxon|wilcox",
 "MAST named":                         r"\bMAST\b",
 "DESeq2 via FindMarkers":             r"test\.use\s*=\s*['\"]DESeq2|FindMarkers[^.]{0,80}DESeq2|DESeq2[^.]{0,80}FindMarkers",
 "other test.use (t/bimod/roc/LR/negbinom/poisson)": r"test\.use\s*=\s*['\"](?:t|bimod|roc|LR|negbinom|poisson)['\"]|logistic regression[^.]{0,60}(?:marker|differential)",
 "logfc.threshold stated":             r"logfc\.threshold|(?:log2? ?)?fold[- ]?change (?:threshold|cutoff)[^.]{0,20}0\.25|0\.25[^.]{0,30}(?:log2? ?)?fold",
 "min.pct stated":                     r"min\.pct|expressed in (?:at least|>|≥) ?\d+ ?% of (?:the )?cells",
 "only.pos":                           r"only\.pos",
 "Bonferroni named":                   r"Bonferroni",
 "p_val_adj / adjusted p":             r"p_val_adj|adjusted [pP][- ]?value|padj|\bFDR\b",
 "avg_log2FC / log fold change":       r"avg_log2?FC|avg_logFC|log2? ?fold[- ]?change|\bLFC\b|\blogFC\b",
 "pseudobulk (AggregateExpression etc.)": r"pseudo-?bulk|AggregateExpression|AverageExpression",
 # --- scoring ---
 "AddModuleScore":                     r"AddModuleScore|module score",
 "CellCycleScoring":                   r"CellCycleScoring|cell[- ]cycle (?:score|scoring|regress)",
 "UCell / AUCell instead":             r"UCell|AUCell",
 # --- QC ---
 "PercentageFeatureSet / percent.mt":  r"PercentageFeatureSet|percent\.mt|mitochondrial (?:gene|read|transcript|RNA|content|percent|fraction)",
 "mito threshold stated":              r"(?:<|>|≤|≥|less than|more than|above|below|under|over)\s*\d{1,2}\s*% (?:of )?(?:mitochondrial|mito)|mitochondrial[^.]{0,60}(?:<|>|≤|≥|less than|more than|above|below)\s*\d{1,2}\s*%",
 "nFeature / nCount filter":           r"nFeature_RNA|nCount_RNA|(?:fewer|less|more) than \d[\d,]* (?:genes|features|UMIs)",
 "doublet removal":                    r"DoubletFinder|Scrublet|scDblFinder|doublet",
 "SoupX / ambient RNA":                r"SoupX|CellBender|ambient RNA",
 # --- label transfer / reference mapping ---
 "FindTransferAnchors / TransferData": r"FindTransferAnchors|TransferData|MapQuery|label transfer|reference[- ]based (?:annotation|mapping)",
 "Azimuth":                            r"Azimuth",
 "SingleR / other annotation":         r"SingleR|scType|CellTypist|Garnett",
 # --- modalities ---
 "Signac / ATAC":                      r"Signac|scATAC|snATAC|chromatin accessibility",
 "WNN multimodal":                     r"FindMultiModalNeighbors|weighted[- ]nearest[- ]neigh|\bWNN\b",
 "spatial (Visium etc.)":              r"Load10X_Spatial|Visium|Xenium|MERFISH|SpatialFeaturePlot|FindSpatiallyVariableFeatures",
 "snRNA-seq":                          r"single[- ]nucle(?:us|i)|snRNA",
 # --- downstream tools whose numbers rest on Seurat objects ---
 "Monocle / trajectory":               r"Monocle|Slingshot|PAGA|pseudotime|RNA velocity|scVelo",
 "CellChat / ligand-receptor":         r"CellChat|CellPhoneDB|NicheNet|ligand[- ]receptor",
 "SCENIC":                             r"SCENIC",
 "Scanpy also used":                   r"Scanpy|scanpy",
 "version stated":                     r"Seurat(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"NormalizeData / LogNormalize", "scale factor 10,000 stated", "regress out (vars.to.regress)",
      "resolution stated", "logfc.threshold stated", "min.pct stated", "mito threshold stated",
      "nFeature / nCount filter", "doublet removal", "SoupX / ambient RNA", "snRNA-seq",
      "CLR (ADT / CITE-seq)", "ElbowPlot / JackStraw", "RunTSNE", "RunUMAP",
      "AddModuleScore", "CellCycleScoring", "FindVariableFeatures", "2,000 variable features",
      "RunPCA / PCs stated", "pseudobulk (AggregateExpression etc.)", "Wilcoxon named",
      "avg_log2FC / log fold change", "p_val_adj / adjusted p", "FindTransferAnchors / TransferData",
      "spatial (Visium etc.)", "Monocle / trajectory", "CellChat / ligand-receptor",
      "CCA/anchor integration (v3/v4)", "SCT-based integration", "sketch-based (v5)",
      "PercentageFeatureSet / percent.mt", "other test.use (t/bimod/roc/LR/negbinom/poisson)"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"Seurat(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"resolution[^.;]{0,30}?(\d\.\d+)", re.I)
MITO  = re.compile(r"(\d{1,2}(?:\.\d)?)\s*%[^.;]{0,40}?mitochondrial|mitochondrial[^.;]{0,60}?(\d{1,2}(?:\.\d)?)\s*%", re.I)
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|p_val_adj|padj|FDR|[qQ][- ]?value|Bonferroni)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
LFC   = re.compile(r"(?:logfc\.threshold|\|?\s*(?:avg_)?log2?\s*(?:fold[- ]?change|FC)\s*\|?|\bLFC\b|fold[- ]?change)[^.;]{0,30}?[>≥=]\s*(\d+(?:\.\d+)?)", re.I)
DIMS  = re.compile(r"(?:dims\s*=\s*1:|(?:first|top)\s+)(\d{1,3})\s*(?:PCs?|principal components|dimensions)?", re.I)
KWIN  = re.compile(r"Seurat(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major >= 5: return "v5"
    if major == 4: return "v4"
    if major == 3: return "v3"
    if major == 2: return "v2"
    return "v%d" % major

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
        if row["package"] == "Seurat":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "Seurat")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("seurat_profiles.jsonl", "w") as fh:
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
