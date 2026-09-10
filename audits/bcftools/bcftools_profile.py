#!/usr/bin/env python3
"""Profile how each cohort paper used BCFtools.

Mines the full text for the choices that select BCFtools code paths:
the subcommands named (mpileup/call/filter/view/norm/stats/merge/concat/csq/
consensus/annotate/+fill-tags/roh/gtcheck), the caller model (-m/-c), QUAL and
depth thresholds, the filter expressions quoted, the data type, and the stated
bcftools version. One JSONL record per paper.

Usage: python3 bcftools_profile.py            (fetch full texts, cache fallback)
       python3 bcftools_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the BCFtools evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy and SAMtools audits, the 2026-09-09 run had no route to Europe PMC (www.ebi.ac.uk denied by the
session's egress policy; NCBI likewise), so every record in
bcftools_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "bcftools" (any case).
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "bcftools named":                       r"[Bb][Cc][Ff][Tt]ools",
 "mpileup":                              r"mpileup",
 "call":                                 r"bcftools call|mpileup[^.]{0,60}call|called (?:with|using) bcftools|bcftools[^.]{0,40}(?:variant|genotype) call",
 "call -m (multiallelic)":               r"call -m|multiallelic[- ]caller|-mv\b|call -v?m|call -mv|--multiallelic",
 "call -c (consensus)":                  r"call -c\b|-cv\b|consensus[- ]caller|bcftools call[^.]{0,20}-c",
 "filter / view -i/-e":                  r"bcftools filter|bcftools view|-i ?'|-e ?'|--include|--exclude",
 "QUAL threshold stated":                r"QUAL\s*(?:>=?|≥|<=?|of|above|below|greater than|less than|at least)\s*\d+|quality (?:score )?(?:>=?|≥|of|above|greater than|at least|below|less than) ?\d+",
 "depth threshold stated":               r"\bDP\s*(?:>=?|≥|<=?|of|above|below|greater than|less than|at least)\s*\d+|(?:read )?depth (?:of )?(?:>=?|≥|<=?|above|below|greater than|less than|at least) ?\d+",
 "GATK-style filter expression (QD/FS/MQ/SOR)": r"\bQD\s*<|\bFS\s*>|\bMQ\s*<|\bSOR\s*>|MQRankSum|ReadPosRankSum",
 "MQ / mapping quality filter":          r"mapping quality|MAPQ|\bMQ\s*(?:>=?|≥|<|of)",
 "norm (left-align / split multiallelic)": r"bcftools norm|left[- ]align|left[- ]normali[sz]|split (?:multi-?allelic|multiallelic)|multiallelic (?:sites|variants) (?:were )?(?:split|decomposed)",
 "stats / ts/tv":                        r"bcftools stats|vcfstats|plot-vcfstats|Ts/Tv|ts/tv|transition[/ ]transversion",
 "merge":                                r"bcftools merge",
 "concat":                               r"bcftools concat",
 "consensus":                            r"bcftools consensus",
 "annotate":                             r"bcftools annotate",
 "csq (consequences)":                   r"bcftools csq|haplotype-aware consequence",
 "+fill-tags / HWE / AF tags":           r"fill-tags|\bHWE\b|Hardy[- ]Weinberg|ExcHet|F_MISSING",
 "roh":                                  r"bcftools roh|runs? of homozygosity|\bROH\b",
 "gtcheck":                              r"gtcheck",
 "query":                                r"bcftools query",
 "isec":                                 r"bcftools isec",
 "convert / index / sort":               r"bcftools (?:convert|index|sort)",
 "ploidy / haploid":                     r"--ploidy|ploidy|haploid",
 "BAQ / -B / -Q / -q options":           r"\bBAQ\b|--no-BAQ|-Q ?\d+|-q ?\d+|min-BQ|min-MQ",
 "indel calling":                        r"indel",
 "low coverage / imputation (GLIMPSE, BEAGLE)": r"GLIMPSE|BEAGLE|imputation|low[- ]coverage",
 "ancient DNA":                          r"ancient DNA|aDNA|damage",
 "samtools also used":                   r"[Ss][Aa][Mm][Tt]ools",
 "GATK also used":                       r"GATK|HaplotypeCaller",
 "freebayes / DeepVariant / other caller": r"[Ff]ree[Bb]ayes|DeepVariant|VarScan|Strelka|Platypus",
 "VEP / SnpEff / ANNOVAR annotation":    r"\bVEP\b|SnpEff|ANNOVAR",
 "PLINK / vcftools downstream":          r"\bPLINK\b|vcftools|VCFtools",
 "WGS / WES / exome":                    r"whole[- ]genome sequencing|\bWGS\b|whole[- ]exome|\bWES\b|exome",
 "RNA-seq":                              r"RNA-?seq",
 "long reads (nanopore / PacBio)":        r"[Nn]anopore|PacBio|long[- ]read|HiFi",
 "mitochondrial":                        r"mitochondri|\bmtDNA\b|chrM\b",
 "microbial / viral / bacterial":        r"bacteri|viral|virus|SARS-CoV-2|microb|isolate",
 "population genetics / GWAS":           r"population genetic|GWAS|allele frequenc|F_ST|\bFst\b",
 "bcftools version stated":              r"[Bb][Cc][Ff][Tt]ools(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"mpileup", "call", "filter / view -i/-e", "QUAL threshold stated", "depth threshold stated",
      "norm (left-align / split multiallelic)", "stats / ts/tv", "merge", "concat", "consensus", "annotate",
      "csq (consequences)", "roh", "gtcheck", "query", "isec", "convert / index / sort", "ploidy / haploid",
      "indel calling", "low coverage / imputation (GLIMPSE, BEAGLE)", "WGS / WES / exome", "RNA-seq",
      "microbial / viral / bacterial", "population genetics / GWAS"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Bb][Cc][Ff][Tt]ools(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"QUAL\s*(?:>=?|≥|<=?|of|above|below|greater than|less than|at least)\s*(\d+)|quality (?:score )?(?:>=?|≥|of|above|greater than|at least|below|less than) ?(\d+)|QUAL ?< ?(\d+)", re.I)
MITO  = re.compile(r"\bDP\s*(?:>=?|≥|<=?|of|above|below|greater than|less than|at least)\s*(\d+)|(?:read )?depth (?:of )?(?:>=?|≥|<=?|above|below|greater than|less than|at least) ?(\d+)", re.I)
PADJ  = re.compile(r"(?:MAF|minor allele frequency)\s*(?:>=?|≥|<=?|of|above|below)\s*(\d?\.\d+|\d+ ?%)", re.I)
LFC   = re.compile(r"(?:mapping quality|MAPQ|\bMQ)\s*(?:>=?|≥|of|above|greater than|at least|<)\s*(\d+)|-q ?(\d+)", re.I)
DIMS  = re.compile(r"(?:missing(?:ness)?|F_MISSING|call rate)[^.;]{0,30}?(\d{1,3})\s?%", re.I)
KWIN  = re.compile(r"[Bb][Cc][Ff][Tt]ools(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major == 0: return "0.1.x"       # 0.1.19 and older still get cited
    if major != 1: return None
    return "1.%d" % minor

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
        "qual_thresholds": sorted({a or b or c for a, b, c in RES.findall(text)}),
        "depth_thresholds": sorted({a or b for a, b in MITO.findall(text)}),
        "maf_thresholds": sorted(set(PADJ.findall(text))),
        "mapq_thresholds": sorted({a or b for a, b in LFC.findall(text)}),
        "missingness_pct": sorted({int(d) for d in DIMS.findall(text) if 0 <= int(d) <= 100}),
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
        if row["package"] == "BCFtools":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "BCFtools")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("bcftools_profiles.jsonl", "w") as fh:
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
    for r in c["qual_thresholds"]: res[r] += 1
    for m in c["depth_thresholds"]: mito[m] += 1
    for p in c["maf_thresholds"]: padj[p] += 1
    for l in c["mapq_thresholds"]: lfc[l] += 1
    for d in c["missingness_pct"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nQUAL thresholds:", dict(res.most_common(10)))
print("depth thresholds:", dict(mito.most_common(10)))
print("MAF thresholds:", dict(padj.most_common(8)))
print("MAPQ thresholds:", dict(lfc.most_common(8)))
print("missingness %:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
