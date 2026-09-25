#!/usr/bin/env python3
"""Profile how each cohort paper used scikit-learn.
Mines the text for the estimators, metrics and model-selection tools named
(PCA, k-means, DBSCAN, hierarchical clustering, Gaussian mixtures, NMF, t-SNE,
logistic regression, SVM, random forests, gradient boosting, linear models,
nearest neighbours, MLP), the scalers, the cross-validation scheme, the metrics
reported (AUC, accuracy, precision/recall/F1, R2, silhouette, ARI/NMI), the
co-libraries and the stated version. One JSONL record per paper.
Usage: python3 sklearn_profile.py            (fetch full texts, cache fallback)
       python3 sklearn_profile.py --offline  (survey cache only, no network)
Two sources, recorded per paper in `source`: "fulltext" (Europe PMC JATS body)
or "survey_cache" (the survey's stored evidence sentences; a few hundred
characters per package, so feature counts are LOWER BOUNDS).
As for the earlier audits, the 2026-09-25 run had no route to Europe PMC from
this session, so every record in sklearn_profiles.jsonl is source=survey_cache.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "scikit-learn named":                    r"scikit-?learn|sklearn",
 "PCA":                                   r"\bPCA\b|principal component",
 "k-means":                               r"k-?means|KMeans|MiniBatchKMeans",
 "DBSCAN / HDBSCAN / OPTICS":             r"DBSCAN|OPTICS",
 "hierarchical / agglomerative clustering": r"hierarchical clustering|Agglomerative|agglomerative|Ward",
 "Gaussian mixture":                      r"GaussianMixture|Gaussian mixture|GMM",
 "spectral clustering / embedding":       r"[Ss]pectral(?:Clustering|Embedding| clustering| embedding)",
 "NMF":                                   r"\bNMF\b|non-?negative matrix",
 "t-SNE / MDS / Isomap (manifold)":       r"t-?SNE|TSNE|\bMDS\b|Isomap|LocallyLinear",
 "logistic regression":                   r"LogisticRegression|logistic regression",
 "SVM / SVC / SVR":                       r"\bSVM\b|\bSVC\b|\bSVR\b|support vector",
 "random forest / extra trees":           r"RandomForest|random forest|ExtraTrees",
 "gradient boosting":                     r"GradientBoosting|gradient boost|HistGradient|XGBoost|LightGBM",
 "linear / ridge / lasso / elastic net":  r"LinearRegression|linear regression|\bRidge\b|\bLasso\b|ElasticNet|elastic net",
 "nearest neighbours":                    r"KNeighbors|k-?nearest|\bkNN\b|NearestNeighbors",
 "MLP / neural network":                  r"MLPClassifier|MLPRegressor|multi-?layer perceptron",
 "LDA (discriminant)":                    r"LinearDiscriminant|\bLDA\b",
 "Gaussian process / kernel methods":     r"GaussianProcess|Gaussian process|KernelRidge|kernel ridge|\bRBF\b",
 "StandardScaler / MinMaxScaler / normalization": r"StandardScaler|MinMaxScaler|RobustScaler|z-?score|standardi[sz]ed|scaled to",
 "cross-validation":                      r"cross[- ]?validat|cross_val|KFold|StratifiedKFold|LeaveOneOut|GridSearch|RandomizedSearch|nested",
 "train/test split":                      r"train_test_split|train(?:ing)?[/-]test|held-?out|hold-?out",
 "AUC / ROC":                             r"\bAUC\b|\bROC\b|roc_auc|AUROC|AUPRC|average precision",
 "accuracy / precision / recall / F1":    r"accuracy|precision|recall|F1|F-?score|confusion matrix|balanced accuracy|Matthews|MCC",
 "R2 / MSE / MAE":                        r"\bR2\b|R\^2|R²|coefficient of determination|mean squared error|\bMSE\b|RMSE|\bMAE\b",
 "silhouette / ARI / NMI (clustering metrics)": r"silhouette|adjusted Rand|\bARI\b|\bNMI\b|mutual information|Davies|Calinski",
 "feature importance / permutation / SHAP": r"feature importance|permutation importance|SHAP|Gini importance",
 "calibration":                           r"calibrat",
 "class imbalance handling":              r"class_weight|imbalance|SMOTE|oversampl|undersampl",
 "UMAP also used":                        r"UMAP",
 "scanpy / Seurat also used":             r"[Ss]canpy|Seurat",
 "scikit-learn version stated":           r"scikit-?learn(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+|sklearn[^.;(]{0,20}?\d+\.\d+",
}
CI = {"PCA", "k-means", "hierarchical / agglomerative clustering", "Gaussian mixture", "NMF", "logistic regression", "SVM / SVC / SVR",
      "random forest / extra trees", "gradient boosting", "linear / ridge / lasso / elastic net", "nearest neighbours", "MLP / neural network",
      "Gaussian process / kernel methods", "StandardScaler / MinMaxScaler / normalization", "cross-validation", "train/test split",
      "accuracy / precision / recall / F1", "R2 / MSE / MAE", "silhouette / ARI / NMI (clustering metrics)", "feature importance / permutation / SHAP",
      "calibration", "class imbalance handling"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"scikit-?learn(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)|sklearn[^.;(]{0,20}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)", re.I)
RES   = re.compile(r"(\d+)-fold", re.I)
MITO  = re.compile(r"AUC[^.;]{0,20}?(0?\.\d+)", re.I)
PADJ  = re.compile(r"(\d{1,3}) ?(?:principal )?components|n_components ?= ?(\d+)", re.I)
LFC   = re.compile(r"accuracy[^.;]{0,20}?(\d{1,3}(?:\.\d+)?) ?%", re.I)
DIMS  = re.compile(r"(\d{2,3})[/:](\d{2,3}) (?:train|split)", re.I)
KWIN  = re.compile(r"scikit-?learn|sklearn", re.I)

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
        "cv_folds": sorted(set(RES.findall(text))),
        "auc_values": sorted(set(MITO.findall(text))),
        "n_components": sorted({a or b for a, b in PADJ.findall(text)}),
        "accuracy_pct": sorted(set(LFC.findall(text))),
        "split_ratios": sorted({"%s/%s" % ab for ab in DIMS.findall(text)}),
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
        if row["package"] == "scikit-learn":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "scikit-learn")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "scikit-learn".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("sklearn_profiles.jsonl", "w") as fh:
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
    for r in c["cv_folds"]: res[r] += 1
    for m in c["auc_values"]: mito[m] += 1
    for p in c["n_components"]: padj[p] += 1
    for l in c["accuracy_pct"]: lfc[l] += 1
    for d in c["split_ratios"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nCV folds:", dict(res.most_common(10)))
print("AUC values:", dict(mito.most_common(10)))
print("n components:", dict(padj.most_common(8)))
print("accuracy %:", dict(lfc.most_common(8)))
print("train/test ratios:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
