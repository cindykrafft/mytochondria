#!/usr/bin/env python3
"""Profile how each cohort paper used VCFtools.
Mines the text for the choices that select VCFtools code paths: the site
filters (--maf/--mac, --max-missing / --max-missing-count, --minQ, --minDP /
--minGQ genotype filters, --hwe, --thin, --remove-indels, --min/max-alleles),
the statistics (--window-pi / --site-pi, --TajimaD, --weir-fst-pop, --het,
--relatedness / --relatedness2, --hap-r2 / --geno-r2, --missing-*, --depth,
--freq, --hardy), the conversions (--012, --plink, --recode), the data type
(RAD-seq / GBS, WGS, exome, pooled), the co-packages and the stated version.
One JSONL record per paper.
Usage: python3 vcftools_profile.py            (fetch full texts, cache fallback)
       python3 vcftools_profile.py --offline  (survey cache only, no network)
Two sources, recorded per paper in `source`: "fulltext" (Europe PMC JATS body)
or "survey_cache" (the survey's stored evidence sentences; a few hundred
characters per package, so feature counts are LOWER BOUNDS).
As for the earlier audits, the 2026-09-24 run had no route to Europe PMC from
this session, so every record in vcftools_profiles.jsonl is source=survey_cache.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "VCFtools named":                        r"VCFtools|vcftools|VCFTools",
 "--maf / --mac (minor allele filter)":   r"--maf|--mac\b|--max-maf|minor allele (?:frequency|count)|\bMAF\b|\bMAC\b",
 "--max-missing / --max-missing-count":   r"--max-missing|max-missing|missing(?:ness)? (?:rate|threshold|data)|\bmissing data\b",
 "--minQ (site quality)":                 r"--minQ|minQ",
 "--minDP / --maxDP / --minGQ (genotype filters)": r"--minDP|--maxDP|--minGQ|minDP|maxDP|minGQ|genotype quality|read depth",
 "--min-alleles / --max-alleles (biallelic)": r"--min-alleles|--max-alleles|bi-?allelic",
 "--remove-indels / --keep-only-indels":  r"--remove-indels|--keep-only-indels|indels? (?:were )?(?:removed|excluded)",
 "--hwe":                                 r"--hwe|Hardy[- ]Weinberg|\bHWE\b",
 "--thin":                                r"--thin\b|thinned",
 "--window-pi / --site-pi (nucleotide diversity)": r"--window-pi|--site-pi|window-pi|site-pi|nucleotide diversity|\bpi\b|\bπ\b",
 "--TajimaD":                             r"--TajimaD|TajimaD|Tajima",
 "--weir-fst-pop (Fst)":                  r"--weir-fst-pop|weir-fst|\bF\s?ST\b|\bFst\b|Weir and Cockerham|Weir & Cockerham",
 "--het (inbreeding / heterozygosity)":   r"--het\b|heterozygosity|inbreeding coefficient|\bF(?:IS)?\b statistic",
 "--relatedness / --relatedness2":        r"--relatedness2?|relatedness|kinship|\bKING\b",
 "--hap-r2 / --geno-r2 / LD":             r"--hap-r2|--geno-r2|--ld-window|linkage disequilibrium|\bLD\b|r\^?2 decay",
 "--missing-indv / --missing-site":       r"--missing-indv|--missing-site|missing-indv|missing-site",
 "--depth / --site-mean-depth":           r"--depth\b|--site-mean-depth|--site-depth|--geno-depth|mean depth",
 "--freq / --counts":                     r"--freq2?\b|--counts2?\b|allele frequenc",
 "--hardy":                               r"--hardy",
 "--012 / --plink / --recode (conversion)": r"--012|--plink|--recode|012 (?:matrix|format)|recode",
 "--keep / --remove (individual subsets)": r"--keep\b|--remove\b",
 "RAD-seq / GBS / ddRAD":                 r"RAD-?seq|ddRAD|\bGBS\b|genotyping[- ]by[- ]sequencing|Stacks|ipyrad",
 "whole-genome resequencing":             r"whole[- ]genome (?:re)?sequenc|\bWGS\b|resequenc",
 "exome / targeted":                      r"exome|\bWES\b|target(?:ed)? (?:capture|enrichment)",
 "pool-seq":                              r"pool-?seq|pooled sequenc",
 "population structure / admixture":      r"ADMIXTURE|STRUCTURE\b|fastSTRUCTURE|\bPCA\b|principal component",
 "GATK / bcftools / freebayes calling":   r"GATK|HaplotypeCaller|bcftools|freebayes|SAMtools mpileup|Stacks",
 "PLINK also used":                       r"PLINK|plink",
 "VCFtools version stated":               r"VCFtools(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"VCFtools named", "--maf / --mac (minor allele filter)", "--max-missing / --max-missing-count", "--minDP / --maxDP / --minGQ (genotype filters)",
      "--min-alleles / --max-alleles (biallelic)", "--remove-indels / --keep-only-indels", "--hwe", "--window-pi / --site-pi (nucleotide diversity)",
      "--het (inbreeding / heterozygosity)", "--relatedness / --relatedness2", "--hap-r2 / --geno-r2 / LD", "--freq / --counts",
      "RAD-seq / GBS / ddRAD", "whole-genome resequencing", "exome / targeted", "pool-seq", "population structure / admixture",
      "GATK / bcftools / freebayes calling", "PLINK also used"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"VCFtools(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)", re.I)
RES   = re.compile(r"--max-missing[ =]?(0?\.\d+|1(?:\.0)?)|max-missing[ =]?(0?\.\d+)|missing(?:ness)?[^.;]{0,30}?(\d{1,3})\s?%", re.I)
MITO  = re.compile(r"--maf[ =]?(0?\.\d+)|MAF[^.;]{0,15}?(?:>|>=|≥|of|above|below|<)\s?(0?\.\d+)", re.I)
PADJ  = re.compile(r"--minDP[ =]?(\d+)|minDP[ =:]?(\d+)|depth[^.;]{0,20}?(?:>=?|≥|of at least|at least|minimum(?: of)?)\s?(\d+)", re.I)
LFC   = re.compile(r"--window-pi[ =]?(\d+)|--TajimaD[ =]?(\d+)|--fst-window-size[ =]?(\d+)", re.I)
DIMS  = re.compile(r"--minGQ[ =]?(\d+)|--minQ[ =]?(\d+)", re.I)
KWIN  = re.compile(r"VCFtools", re.I)

def family(v):
    m = re.match(r"(\d+)\.(\d+)\.?(\d*)", v)
    if not m: return None
    if m.group(1) != "0" or m.group(2) != "1": return None
    return "0.1.%s" % (m.group(3) or "?")

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
        "max_missing": sorted({a or b or c for a, b, c in RES.findall(text)}),
        "maf": sorted({a or b for a, b in MITO.findall(text)}),
        "minDP": sorted({a or b or c for a, b, c in PADJ.findall(text)}),
        "window_sizes": sorted({a or b or c for a, b, c in LFC.findall(text)}),
        "minGQ_minQ": sorted({a or b for a, b in DIMS.findall(text)}),
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
        if row["package"] == "VCFtools":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "VCFtools")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "VCFtools".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("vcftools_profiles.jsonl", "w") as fh:
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
    for r in c["max_missing"]: res[r] += 1
    for m in c["maf"]: mito[m] += 1
    for p in c["minDP"]: padj[p] += 1
    for l in c["window_sizes"]: lfc[l] += 1
    for d in c["minGQ_minQ"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\n--max-missing values:", dict(res.most_common(10)))
print("--maf values:", dict(mito.most_common(10)))
print("--minDP values:", dict(padj.most_common(8)))
print("window sizes (pi / TajimaD / Fst):", dict(lfc.most_common(8)))
print("--minGQ / --minQ values:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
