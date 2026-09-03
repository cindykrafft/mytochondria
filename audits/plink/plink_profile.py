#!/usr/bin/env python3
"""Profile how each cohort paper used PLINK (1.9 / 2.0).

Mines the full text for the choices that select PLINK code paths: the HWE, MAF,
MAC and missingness filters and their thresholds, LD pruning parameters, PCA,
relatedness (--genome / KING), association and regression commands, --adjust,
--score, --clump, --fst, and the stated PLINK version. One JSONL record per paper.

Usage: python3 plink_profile.py            (fetch full texts, cache fallback)
       python3 plink_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the PLINK evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy and Cutadapt audits, the 2026-09-03 run had no route to Europe PMC
(www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so every record in
plink_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "PLINK"/"PLINK2".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below; PLINK flags are lower-case
# identifiers and matching them exactly is the point.
FEATURES = {
 "PLINK 1.9 named":                     r"PLINK\s*(?:v\.?\s*)?1\.9|1\.90|PLINK1\.9|plink19",
 "PLINK 2 named":                       r"PLINK\s*(?:v\.?\s*)?2(?:\.0)?(?![0-9])|plink2|PLINK2|2\.00a",
 "PLINK 1.07 named":                    r"1\.07",
 "HWE filter (--hwe / Hardy-Weinberg)": r"--hwe|hardy[- ]weinberg|\bHWE\b",
 "HWE threshold stated":                r"(?:HWE|hardy[- ]weinberg)[^.;]{0,60}?\d\s*[x×]\s*10|--hwe\s*\d|(?:HWE|hardy[- ]weinberg)[^.;]{0,40}?(?:<|>|less than|below)\s*(?:1e-|0\.0)",
 "MAF filter (--maf)":                  r"--maf|minor allele frequency|\bMAF\b",
 "MAC / allele count filter":           r"--mac|minor allele count|\bMAC\b",
 "missingness / call-rate filter (--geno / --mind)": r"--geno|--mind|call[- ]rate|missingness|genotyping rate",
 "LD pruning (--indep-pairwise / --indep)": r"--indep|indep-pairwise|LD[- ]prun|pruned for (?:linkage|LD)|linkage disequilibrium[^.]{0,40}prun",
 "--indep-pairwise parameters stated":  r"indep-pairwise\s*\d+\s*\d+\s*0?\.\d+|\d+\s*(?:kb|SNPs?)[^.]{0,20}step[^.]{0,30}r ?2",
 "LD / r2 calculation (--r2 / --ld / --ld-window)": r"--r2|--ld\b|--ld-window|pairwise (?:LD|linkage disequilibrium)|\br\s*2\s*(?:>|<|≥|threshold)",
 "PCA (--pca)":                         r"--pca|principal component|\bPCA\b|\bPCs?\b",
 "relatedness / IBD (--genome, --make-king, --king-cutoff, PI_HAT)": r"--genome|--make-king|king-cutoff|PI_HAT|pi-hat|identity[- ]by[- ]descent|\bIBD\b|KING",
 "heterozygosity (--het / F)":          r"--het\b|heterozygosity",
 "association: --assoc / --model / Fisher": r"--assoc|--model|--fisher|allelic (?:association|test)|Cochran[- ]Armitage",
 "regression: --glm / --linear / --logistic": r"--glm|--linear|--logistic|logistic regression|linear regression|linear mixed",
 "Firth":                               r"[Ff]irth",
 "covariates named":                    r"--covar|covariate",
 "--adjust / GC lambda / multiple testing": r"--adjust|genomic (?:control|inflation)|lambda\s*(?:GC|=)|Bonferroni|Benjamini|\bFDR\b",
 "genome-wide significance 5e-8":       r"5\s*[x×]\s*10\s*[-−]\s*8|5e-0?8|genome-wide significan",
 "polygenic score (--score)":           r"--score|polygenic (?:risk )?score|\bPRS\b|\bPGS\b|PGI",
 "clumping (--clump)":                  r"--clump|clump",
 "Fst (--fst)":                         r"--fst|\bF\s*ST\b|F_ST|Fst",
 "ROH (--homozyg)":                     r"--homozyg|runs of homozygosity|\bROH\b",
 "sex check (--check-sex)":             r"--check-sex|sex check|sex[- ]discrepan",
 "format conversion / --make-bed / --recode / VCF": r"--make-bed|--recode|--vcf|--bfile|--pfile|\.bed\b|VCF",
 "imputed / dosage data":               r"imput|dosage",
 "GWAS":                                r"\bGWAS\b|genome-wide association",
 "ancient DNA / population genetics (ADMIXTURE, EIGENSOFT, smartpca)": r"ADMIXTURE|EIGENSOFT|smartpca|ancient|eigenstrat|f-statistics|qpAdm",
 "UK Biobank":                          r"UK Biobank|UKB\b",
 "REGENIE / SAIGE / BOLT / GCTA / fastGWA co-used": r"REGENIE|regenie|SAIGE|BOLT-LMM|GCTA|fastGWA|GEMMA|LDSC|METAL",
 "PLINK version stated":                r"PLINK2?(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"HWE filter (--hwe / Hardy-Weinberg)", "HWE threshold stated", "MAF filter (--maf)", "missingness / call-rate filter (--geno / --mind)",
      "LD pruning (--indep-pairwise / --indep)", "--indep-pairwise parameters stated", "PCA (--pca)", "heterozygosity (--het / F)",
      "association: --assoc / --model / Fisher", "regression: --glm / --linear / --logistic", "covariates named",
      "--adjust / GC lambda / multiple testing", "genome-wide significance 5e-8", "polygenic score (--score)", "clumping (--clump)",
      "ROH (--homozyg)", "sex check (--check-sex)", "imputed / dosage data", "GWAS", "relatedness / IBD (--genome, --make-king, --king-cutoff, PI_HAT)"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"PLINK2?(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*(?:[a-z]\d*(?:\.\d+)*)?)")
RES   = re.compile(r"indep-pairwise\s*(\d+\s*\d+\s*0?\.\d+)", re.I)   # LD-pruning parameters
MITO  = re.compile(r"(?:HWE|hardy[- ]weinberg)[^.;]{0,60}?(\d(?:\.\d+)?\s*[x×]\s*10\s*[-−]\s*\d+|1e-\d+)|--hwe\s*(1e-\d+|0?\.\d+)", re.I)   # HWE thresholds
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|p_val_adj|padj|FDR|[qQ][- ]?value|Bonferroni)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
LFC   = re.compile(r"(?:MAF|minor allele frequency|--maf)[^.;]{0,30}?[<>≥≤]\s*(\d?\.\d+|\d+\s*%)", re.I)   # MAF cutoffs
DIMS  = re.compile(r"(?:first|top)\s+(\d{1,3})\s*(?:PCs?|principal components|genetic PCs)", re.I)
KWIN  = re.compile(r"PLINK2?(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major == 1 and minor in (9, 90): return "1.9"
    if major == 1 and minor == 7: return "1.07"
    if major == 2: return "2.0"
    return None

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
        if row["package"] == "PLINK":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "PLINK")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, PLINK, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "PLINK".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("plink_profiles.jsonl", "w") as fh:
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
print("\n--indep-pairwise parameters:", dict(res.most_common(10)))
print("HWE thresholds:", dict(mito.most_common(10)))
print("adjusted-p cutoffs:", dict(padj.most_common(8)))
print("MAF cutoffs:", dict(lfc.most_common(8)))
print("PCs used:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
