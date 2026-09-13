#!/usr/bin/env python3
"""Profile how each cohort paper used BCFtools.

Mines the full text for the choices that select BCFtools code paths:
the subcommands named (mpileup/call/filter/view/norm/merge/stats/csq/roh/
gtcheck/+fill-tags/...), the calling model (-m/-c, --ploidy), the filter
thresholds quoted (QUAL, DP, MQ), the VCF numbers reported (Ts/Tv, allele
frequency, HWE, singletons), the data type, and the stated bcftools version.
One JSONL record per paper.

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

As for the Seurat, Scanpy, Cutadapt and SAMtools audits, the 2026-09-13 run had
no route to Europe PMC (www.ebi.ac.uk denied by the session's egress policy;
NCBI likewise), so every record in bcftools_profiles.jsonl is
source=survey_cache. Rerun from a host with Europe PMC access to replace them;
the fetch path is unchanged from the other audits.
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
 "call":                                 r"bcftools call|samtools call|\bcall -[mcv]|multiallelic caller|consensus caller",
 "call -m (multiallelic) stated":        r"call -m|call --multiallelic|multiallelic[- ]caller|-mv\b",
 "call -c (consensus) stated":           r"call -c\b|call --consensus|consensus[- ]caller|bcfview -c|-cv\b",
 "ploidy option":                        r"--ploidy|ploidy",
 "filter / view expression":             r"bcftools filter|bcftools view|-i ?['\"]|-e ?['\"]|--include|--exclude",
 "QUAL threshold stated":                r"QUAL\s*(?:>=?|≥|<|of|above|below|greater than|at least|threshold)\s*\d+|quality (?:score )?(?:>=?|≥|of|above|greater than|at least|threshold(?: of)?)\s*\d+",
 "DP threshold stated":                  r"\bDP\s*(?:>=?|≥|<=?|≤|of|above|below|greater than|at least)\s*\d+|(?:read )?depth\s*(?:>=?|≥|<=?|≤|of|above|below|greater than|at least|threshold(?: of)?)\s*\d+",
 "MQ threshold stated":                  r"\bMQ\s*(?:>=?|≥|<|of|above|below|greater than|at least)\s*\d+|mapping quality\s*(?:>=?|≥|of|above|greater than|at least|threshold(?: of)?)\s*\d+",
 "norm (left-align / split)":            r"bcftools norm|left[- ]align|left[- ]normali[sz]|split multi-?allelic|multiallelic (?:sites|variants) were split",
 "merge":                                r"bcftools merge",
 "concat":                               r"bcftools concat",
 "stats":                                r"bcftools stats|vcfstats|plot-vcfstats",
 "annotate":                             r"bcftools annotate",
 "query":                                r"bcftools query",
 "consensus":                            r"bcftools consensus",
 "csq":                                  r"bcftools csq|\bcsq\b",
 "roh":                                  r"bcftools roh|runs of homozygosity|\bROH\b",
 "gtcheck":                              r"gtcheck",
 "isec":                                 r"bcftools isec",
 "+fill-tags / AF AC AN HWE":            r"fill-tags|fill-AN-AC|\bHWE\b|Hardy[- ]Weinberg|ExcHet",
 "index / sort / convert":               r"bcftools index|bcftools sort|bcftools convert",
 "plugins named":                        r"bcftools \+[a-zA-Z-]+|\+fill-tags|\+setGT|\+split-vep|\+prune|\+dosage",
 "Ts/Tv reported":                       r"Ts/Tv|TsTv|transition[/ ]transversion|ti/tv|Ti/Tv",
 "allele frequency reported":            r"allele frequenc|minor allele frequenc|\bMAF\b|\bAF\b",
 "singletons reported":                  r"singleton",
 "genotype quality (GQ) stated":         r"\bGQ\b|genotype quality",
 "mean depth / coverage reported":       r"(?:mean|average|median) (?:sequencing |read )?(?:depth|coverage)|\d+\s?[x×] (?:coverage|depth)|coverage of \d+",
 "samtools also used":                   r"[Ss][Aa][Mm][Tt]ools",
 "GATK also used":                       r"GATK|HaplotypeCaller|GenotypeGVCFs",
 "freebayes / DeepVariant / other caller": r"[Ff]ree[Bb]ayes|DeepVariant|VarScan|Strelka|Mutect|Platypus|octopus|Clair",
 "BWA / Bowtie / STAR / minimap2 aligner": r"\bBWA\b|bwa[- ]mem|[Bb]owtie|\bSTAR\b|minimap2|HISAT",
 "RNA-seq":                              r"RNA-?seq|transcriptom",
 "long reads (nanopore / PacBio)":        r"[Nn]anopore|PacBio|long[- ]read|HiFi",
 "WGS / WES / exome":                    r"whole[- ]genome sequencing|\bWGS\b|whole[- ]exome|\bWES\b|exome",
 "amplicon / mitochondrial / viral / pooled": r"amplicon|mitochondri|\bmtDNA\b|viral|SARS-CoV-2|pool(?:ed)?[- ]seq|metagenom",
 "population / GWAS / phasing":          r"GWAS|population genetic|phasing|phased|imputation|PLINK|Beagle|SHAPEIT|Eagle",
 "many samples (cohort size stated)":    r"\b\d{2,5} (?:individuals|samples|genomes|accessions|isolates|strains)\b",
 "bcftools version stated":              r"[Bb][Cc][Ff][Tt]ools(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"mpileup", "call", "ploidy option", "norm (left-align / split)", "stats", "roh", "gtcheck",
      "Ts/Tv reported", "allele frequency reported", "singletons reported", "genotype quality (GQ) stated",
      "mean depth / coverage reported", "RNA-seq", "WGS / WES / exome", "amplicon / mitochondrial / viral / pooled",
      "QUAL threshold stated", "DP threshold stated", "MQ threshold stated", "population / GWAS / phasing",
      "many samples (cohort size stated)"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Bb][Cc][Ff][Tt]ools(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"QUAL\s*(?:>=?|≥|<|of|above|below|greater than|at least|threshold(?: of)?)\s*(\d+)|quality (?:score )?(?:>=?|≥|of|above|greater than|at least|threshold(?: of)?)\s*(\d+)", re.I)
MITO  = re.compile(r"(\d{1,3}(?:\.\d)?)\s?[x×]\s?(?:coverage|depth)|(?:mean|average|median) (?:sequencing |read )?(?:depth|coverage)[^.;]{0,30}?(\d{1,4}(?:\.\d)?)\s?[x×]?", re.I)
PADJ  = re.compile(r"\bDP\s*(?:>=?|≥|<=?|≤|of|above|below|greater than|at least)\s*(\d+)|(?:read )?depth\s*(?:>=?|≥|<=?|≤|of|above|below|greater than|at least|threshold(?: of)?)\s*(\d+)", re.I)
LFC   = re.compile(r"\bMQ\s*(?:>=?|≥|<|of|above|below|greater than|at least)\s*(\d+)|mapping quality\s*(?:>=?|≥|of|above|greater than|at least|threshold(?: of)?)\s*(\d+)", re.I)
DIMS  = re.compile(r"(?:Ts/Tv|TsTv|Ti/Tv|transition[/ -]to[- ]transversion(?: ratio)?)[^.;]{0,30}?(\d\.\d{1,3})", re.I)
NSMPL = re.compile(r"\b(\d{2,5}) (?:individuals|samples|genomes|accessions|isolates|strains)\b", re.I)
KWIN  = re.compile(r"[Bb][Cc][Ff][Tt]ools(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major == 0: return "0.1.x"       # bcftools 0.1.x (the samtools-era `bcftools view`) still gets cited
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
        "qual_thresholds": sorted({a or b for a, b in RES.findall(text)}),
        "depth_x": sorted({a or b for a, b in MITO.findall(text)}),
        "dp_thresholds": sorted({a or b for a, b in PADJ.findall(text)}),
        "mq_thresholds": sorted({a or b for a, b in LFC.findall(text)}),
        "tstv_values": sorted(set(DIMS.findall(text))),
        "sample_counts": sorted({int(n) for n in NSMPL.findall(text)}),
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
        # lists ("stage [PkgA v1.2, BCFtools, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "BCFtools".
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
res, mito, padj, lfc, dims, nsm = Counter(), Counter(), Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for r in c["qual_thresholds"]: res[r] += 1
    for m in c["depth_x"]: mito[m] += 1
    for p in c["dp_thresholds"]: padj[p] += 1
    for l in c["mq_thresholds"]: lfc[l] += 1
    for d in c["tstv_values"]: dims[d] += 1
    for n in c["sample_counts"]: nsm[n] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nQUAL thresholds:", dict(res.most_common(10)))
print("depth (x):", dict(mito.most_common(10)))
print("DP thresholds:", dict(padj.most_common(10)))
print("MQ thresholds:", dict(lfc.most_common(8)))
print("Ts/Tv values:", dict(dims.most_common(10)))
print("sample counts stated (top 15):", dict(nsm.most_common(15)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
