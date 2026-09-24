#!/usr/bin/env python3
"""Profile how each cohort paper used FastQC.
Mines the text for what the paper takes from FastQC: which module or number is
named (per-base quality, per-sequence quality, duplication, adapter content,
GC content, overrepresented sequences, N content, sequence length), whether
MultiQC aggregated the reports, the trimmer that follows (Trimmomatic,
Cutadapt, Trim Galore, fastp), the quality threshold quoted (Q20/Q30, Phred),
the read type (paired-end, long reads) and the stated version. One JSONL record
per paper.
Usage: python3 fastqc_profile.py            (fetch full texts, cache fallback)
       python3 fastqc_profile.py --offline  (survey cache only, no network)
Two sources, recorded per paper in `source`: "fulltext" (Europe PMC JATS body)
or "survey_cache" (the survey's stored evidence sentences; a few hundred
characters per package, so feature counts are LOWER BOUNDS).
As for the earlier audits, the 2026-09-24 run had no route to Europe PMC from
this session, so every record in fastqc_profiles.jsonl is source=survey_cache.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "FastQC named":                          r"FastQC|fastqc",
 "MultiQC also used":                     r"MultiQC|multiqc",
 "per-base / per-sequence quality named": r"per[- ]base (?:sequence )?quality|base quality|quality score distribution|per[- ]sequence quality",
 "duplication level named":               r"duplication|duplicate",
 "adapter content / adapters named":      r"adapter",
 "GC content named":                      r"GC[- ]content|%GC|GC bias",
 "overrepresented sequences named":       r"overrepresented|over-represented",
 "N content named":                       r"N content|ambiguous bases",
 "sequence length distribution named":    r"length distribution|read length",
 "Q20 / Q30 / Phred threshold quoted":    r"\bQ[23]0\b|[Pp]hred(?: score| quality)? (?:>=?|≥|of|above|below|<)? ?\d+|quality (?:score )?(?:>=?|≥|threshold|cutoff|cut-off|of at least|above|below) ?\d+",
 "trimmed with Trimmomatic":              r"Trimmomatic",
 "trimmed with Cutadapt":                 r"[Cc]utadapt",
 "trimmed with Trim Galore":              r"Trim[ _]?Galore",
 "trimmed with fastp":                    r"fastp",
 "trimmed with BBDuk / other":            r"BBDuk|bbduk|Skewer|AdapterRemoval|Atropos|NGmerge",
 "paired-end":                            r"paired[- ]end|\bPE\b",
 "long reads (nanopore / PacBio)":        r"[Nn]anopore|PacBio|long[- ]read|NanoPlot|pycoQC",
 "RNA-seq":                               r"RNA-?seq|transcriptom",
 "ATAC / ChIP / CUT&RUN":                 r"ATAC|ChIP-?seq|CUT&RUN|CUT&Tag",
 "WGS / WES / amplicon":                  r"whole[- ]genome|whole[- ]exome|\bWGS\b|\bWES\b|amplicon",
 "metagenomics / 16S":                    r"metagenom|16S|microbiome",
 "single-cell":                           r"single[- ]cell|scRNA|10x Genomics",
 "reads filtered or removed after QC":    r"(?:reads|sequences) (?:were |was )?(?:filtered|removed|discarded|excluded)|low[- ]quality reads",
 "quality reported as a number (mean Q / % >= Q30)":  r"(?:mean|average) (?:base )?quality[^.;]{0,20}\d|\d{1,3}(?:\.\d+)? ?% (?:of )?(?:bases|reads) (?:>=?|≥|above|with) ?Q ?\d+",
 "FastQC version stated":                 r"FastQC(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"per-base / per-sequence quality named", "duplication level named", "adapter content / adapters named", "GC content named", "overrepresented sequences named",
      "N content named", "sequence length distribution named", "paired-end", "RNA-seq", "WGS / WES / amplicon", "metagenomics / 16S", "reads filtered or removed after QC",
      "quality reported as a number (mean Q / % >= Q30)", "trimmed with fastp", "trimmed with Cutadapt"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"FastQC(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"\bQ([23]0)\b|[Pp]hred(?: score| quality)? (?:>=?|≥|of|above)? ?(\d+)|quality (?:score )?(?:>=?|≥|threshold(?: of)?|cutoff(?: of)?|cut-off(?: of)?|of at least|above) ?(\d+)")
MITO  = re.compile(r"(?:minimum|min(?:imal)?) (?:read )?length(?: of)? ?(\d+)|reads? (?:shorter|less) than (\d+)|--?(?:min[-_]?len(?:gth)?|length) ?(\d+)", re.I)
PADJ  = re.compile(r"(?:duplication|duplicate) (?:rate|level)[^.;]{0,25}?(\d{1,2}(?:\.\d+)?)\s?%", re.I)
LFC   = re.compile(r"(\d{1,3}(?:\.\d+)?)\s?% (?:of )?(?:bases|reads) (?:>=?|≥|above|with) ?Q ?\d+", re.I)
DIMS  = re.compile(r"(?:read length|reads? of)[^.;]{0,20}?(\d{2,4})\s?(?:bp|nt|base)", re.I)
KWIN  = re.compile(r"FastQC(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major != 0: return None
    return "0.%d.x" % minor

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
        "quality_thresholds": sorted({a or b or c for a, b, c in RES.findall(text)}),
        "min_lengths": sorted({a or b or c for a, b, c in MITO.findall(text)}),
        "dup_rate_pct": sorted(set(PADJ.findall(text))),
        "pct_q_bases": sorted(set(LFC.findall(text))),
        "read_lengths": sorted({int(d) for d in DIMS.findall(text) if 20 <= int(d) <= 5000}),
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
        if row["package"] == "FastQC":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "FastQC")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "FastQC".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("fastqc_profiles.jsonl", "w") as fh:
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
    for r in c["quality_thresholds"]: res[r] += 1
    for m in c["min_lengths"]: mito[m] += 1
    for p in c["dup_rate_pct"]: padj[p] += 1
    for l in c["pct_q_bases"]: lfc[l] += 1
    for d in c["read_lengths"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nquality thresholds (Q):", dict(res.most_common(10)))
print("minimum lengths:", dict(mito.most_common(10)))
print("duplication rates %:", dict(padj.most_common(8)))
print("% bases/reads >= Q:", dict(lfc.most_common(8)))
print("read lengths (bp):", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
