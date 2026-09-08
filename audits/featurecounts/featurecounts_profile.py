#!/usr/bin/env python3
"""Profile how each cohort paper used featureCounts.

Mines the full text for the choices that select featureCounts code paths:
paired-end/fragment counting (-p, --countReadPairs), strandedness (-s),
multi-mapping (-M, --fraction, --primary), multi-overlap (-O), MAPQ (-Q),
feature/attribute types (-t, -g, -f), the overlap options, -B/-C/-P,
--ignoreDup, -J, the aligner and annotation named, the Rsubread interface,
and the stated featureCounts/Subread/Rsubread version. One JSONL record per
paper.

Usage: python3 featurecounts_profile.py            (fetch full texts, cache fallback)
       python3 featurecounts_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the featureCounts evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy and Cutadapt audits, the 2026-09-08 run had no
route to Europe PMC (www.ebi.ac.uk denied by the session's egress policy;
NCBI likewise), so every record in featurecounts_profiles.jsonl is
source=survey_cache. Rerun from a host with Europe PMC access to replace
them; the fetch path is unchanged from the other audits. Version regexes
require a word boundary after "featureCounts"/"Subread"/"Rsubread".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 "paired-end / fragment counting (-p, --countReadPairs)": r"(?<![\w-])-p\b|--countReadPairs|paired[- ]end|fragments? (?:were|was) counted|count(?:ing)? (?:read )?pairs|isPairedEnd",
 "strand-specific counting (-s 1/2, isStrandSpecific)":  r"(?<![\w-])-s\s*[12]\b|strand[- ]specific|(?<!un)stranded|reversely stranded|isStrandSpecific|strandSpecific",
 "unstranded stated (-s 0)":                             r"(?<![\w-])-s\s*0\b|unstranded|non-?strand",
 "multi-mapping reads counted (-M)":                     r"(?<![\w-])-M\b|multi[- ]?mapp(?:ed|ing) reads (?:were|are) (?:counted|included|kept)|countMultiMappingReads",
 "fractional counts (--fraction)":                       r"--fraction|fraction\s*=\s*T|fractional count",
 "multi-overlapping reads counted (-O)":                 r"(?<![\w-])-O\b|allowMultiOverlap|multi[- ]?overlap",
 "primary alignments only (--primary)":                  r"--primary|primaryOnly|primary alignments? only",
 "MAPQ filter (-Q)":                                     r"(?<![\w-])-Q\s*\d|minMQS|mapping quality (?:score )?(?:of |>=?|above |at least |threshold)\s*\d|MAPQ\s*(?:>=?|of|≥)\s*\d",
 "feature level (-f, exon counts)":                      r"(?<![\w-])-f\b|useMetaFeatures\s*=\s*F|exon[- ]level|per[- ]exon|exon counts",
 "feature type (-t)":                                    r"(?<![\w-])-t\s+[A-Za-z_]\w*|GTF\.featureType",
 "attribute type (-g)":                                  r"(?<![\w-])-g\s+[A-Za-z_]\w*|GTF\.attrType|gene_name|gene_id",
 "minimum overlap (--minOverlap)":                       r"--minOverlap|minOverlap",
 "fractional overlap (--fracOverlap)":                   r"--fracOverlap|fracOverlap",
 "largest overlap (--largestOverlap)":                   r"--largestOverlap|largestOverlap",
 "read extension / read2pos":                            r"--readExtension|readExtension|--read2pos|read2pos",
 "both ends mapped (-B)":                                r"(?<![\w-])-B\b|requireBothEndsMapped",
 "chimeric fragments excluded (-C)":                     r"(?<![\w-])-C\b|countChimericFragments",
 "fragment length check (-P -d -D)":                     r"(?<![\w-])-P\b|checkFragLength|minFragLength|maxFragLength",
 "duplicates ignored (--ignoreDup)":                     r"--ignoreDup|ignoreDup",
 "junction counting (-J)":                               r"(?<![\w-])-J\b|juncCounts|junction counts",
 "split-only / non-split-only":                          r"--splitOnly|--nonSplitOnly|splitOnly|nonSplitOnly",
 "threads (-T)":                                         r"(?<![\w-])-T\s*\d|nthreads",
 "Rsubread (R interface)":                               r"Rsubread",
 "SAF annotation":                                       r"\bSAF\b",
 "GTF/GFF annotation":                                   r"\bGTF\b|\bGFF3?\b",
 "GENCODE / Ensembl / RefSeq annotation":                r"GENCODE|Ensembl|RefSeq",
 "STAR aligner":                                         r"\bSTAR\b",
 "HISAT2 / TopHat":                                      r"HISAT2?|TopHat",
 "Subread / Subjunc aligner":                            r"\bSubread\b|Subjunc",
 "Bowtie2 / BWA":                                        r"Bowtie ?2|\bBWA\b",
 "DESeq2 / edgeR / limma downstream":                    r"DESeq2?|edgeR|limma",
 "RNA-seq":                                              r"RNA-?seq",
 "single-cell":                                          r"single[- ]cell|scRNA|10x|Cell ?Ranger",
 "ATAC / ChIP / CUT&RUN / CUT&Tag":                      r"ATAC|ChIP|CUT&(?:RUN|Tag)|CUT&amp;",
 "ribosome profiling":                                   r"ribosome profiling|Ribo-?seq",
 "small RNA / miRNA":                                    r"small[- ]RNA|miRNA|microRNA",
 "nanopore / long reads (-L)":                           r"nanopore|Oxford|long[- ]read|PacBio|(?<![\w-])-L\b",
 "TPM / FPKM / RPKM / CPM computed":                     r"\bTPM\b|\bFPKM\b|\bRPKM\b|\bCPM\b",
 "featureCounts version stated":                         r"(?:[Ff]eature[Cc]ounts|Subread|Rsubread)(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"paired-end / fragment counting (-p, --countReadPairs)", "strand-specific counting (-s 1/2, isStrandSpecific)",
      "unstranded stated (-s 0)", "fractional counts (--fraction)", "multi-overlapping reads counted (-O)",
      "primary alignments only (--primary)", "MAPQ filter (-Q)", "feature level (-f, exon counts)",
      "RNA-seq", "single-cell", "ribosome profiling", "small RNA / miRNA", "nanopore / long reads (-L)"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"(?:[Ff]eature[Cc]ounts|Subread|Rsubread)(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
STRND = re.compile(r"(?<![\w-])-s\s*([012])\b|isStrandSpecific\s*=\s*([012])|strandSpecific\s*=\s*([012])")
MAPQ  = re.compile(r"(?:(?<![\w-])-Q|minMQS)\s*=?\s*(\d{1,3})")
GATTR = re.compile(r"(?:(?<![\w-])-g\s+|GTF\.attrType\s*=\s*)[\"']?([A-Za-z_]\w*)")
FTYPE = re.compile(r"(?:(?<![\w-])-t\s+|GTF\.featureType\s*=\s*)[\"']?([A-Za-z_]\w*)")
KWIN  = re.compile(r"[Ff]eature[Cc]ounts(?![A-Za-z])|Rsubread")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    return m.group(1) + "." + m.group(2)

def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = set(VER.findall(text))
    if c.get("version_survey"):
        vers.add(c["version_survey"])
    vers  = sorted(vers)
    fams  = sorted({f for f in (family(v) for v in vers) if f})
    c.update({
        "source": source,
        "features": feats,
        "versions_all": vers,
        "version_family": fams,
        "strand_modes": sorted({next(g for g in m if g) for m in STRND.findall(text)}),
        "mapq_cutoffs": sorted({int(x) for x in MAPQ.findall(text)}),
        "attr_types": sorted(set(GATTR.findall(text))),
        "feature_types": sorted(set(FTYPE.findall(text))),
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
        if row["package"] == "featureCounts":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "featureCounts")
        # Evidence snippets only (the pipeline_stages strings put other
        # packages' versions within a few characters of "featureCounts").
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("featurecounts_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
strnd, mapq, gattr, ftype = Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for x in c["strand_modes"]: strnd[x] += 1
    for x in c["mapq_cutoffs"]: mapq[x] += 1
    for x in c["attr_types"]: gattr[x] += 1
    for x in c["feature_types"]: ftype[x] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-56s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 25):", dict(vc.most_common(25)))
print("\nstrand modes (-s):", dict(strnd.most_common(10)))
print("MAPQ cutoffs (-Q):", dict(mapq.most_common(10)))
print("attribute types (-g):", dict(gattr.most_common(8)))
print("feature types (-t):", dict(ftype.most_common(8)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
