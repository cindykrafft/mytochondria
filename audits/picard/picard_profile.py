#!/usr/bin/env python3
"""Profile how each cohort paper used Picard.
Mines the text for the choices that select Picard code paths: the tools named
(MarkDuplicates, CollectInsertSizeMetrics, CollectWgsMetrics, CollectHsMetrics,
CollectAlignmentSummaryMetrics, CollectRnaSeqMetrics, CollectGcBiasMetrics,
EstimateLibraryComplexity, SortSam, AddOrReplaceReadGroups, ...), the QC numbers
reported (duplication rate, insert size, coverage, on-target rate, 5'-3' bias),
the data type (RNA-seq, exome/targeted, WGS, bisulfite), and the stated Picard
version. One JSONL record per paper.
Usage: python3 picard_profile.py            (fetch full texts, cache fallback)
       python3 picard_profile.py --offline  (survey cache only, no network)
Two sources, recorded per paper in `source`: "fulltext" (Europe PMC JATS body)
or "survey_cache" (the survey's stored evidence sentences; a few hundred
characters per package, so feature counts are LOWER BOUNDS).
As for the earlier audits, the 2026-09-24 run had no route to Europe PMC from
this session, so every record in picard_profiles.jsonl is source=survey_cache.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "Picard named":                          r"[Pp]icard",
 "MarkDuplicates":                        r"MarkDuplicates|mark(?:ed|ing)? duplicates|duplicates? (?:were|was|are) (?:marked|removed|flagged)|remove(?:d)? duplicates|deduplicat",
 "CollectInsertSizeMetrics":              r"CollectInsertSizeMetrics|InsertSizeMetrics",
 "CollectWgsMetrics":                     r"CollectWgsMetrics|CollectRawWgsMetrics|WgsMetrics",
 "CollectHsMetrics / targeted":           r"CollectHsMetrics|CalculateHsMetrics|CollectTargetedPcrMetrics|HsMetrics",
 "CollectAlignmentSummaryMetrics":        r"CollectAlignmentSummaryMetrics|AlignmentSummaryMetrics",
 "CollectRnaSeqMetrics":                  r"CollectRnaSeqMetrics|RnaSeqMetrics",
 "CollectGcBiasMetrics":                  r"CollectGcBiasMetrics|GcBiasMetrics",
 "CollectMultipleMetrics":                r"CollectMultipleMetrics",
 "EstimateLibraryComplexity":             r"EstimateLibraryComplexity",
 "SortSam / MergeSamFiles / BuildBamIndex": r"SortSam|MergeSamFiles|BuildBamIndex|SamFormatConverter|ReorderSam",
 "AddOrReplaceReadGroups":                r"AddOrReplaceReadGroups",
 "CreateSequenceDictionary / faidx":      r"CreateSequenceDictionary",
 "SamToFastq / FastqToSam / MergeBamAlignment": r"SamToFastq|FastqToSam|MergeBamAlignment|RevertSam",
 "DownsampleSam":                         r"DownsampleSam",
 "LiftoverVcf / vcf tools":               r"LiftoverVcf|SortVcf|MergeVcfs|GenotypeConcordance|CollectVariantCallingMetrics",
 "duplication rate reported":             r"duplication rate|duplicate rate|PCR duplicat|optical duplicat|library complexity|library size",
 "insert size reported":                  r"insert[- ]size|fragment (?:size|length) distribution",
 "mean depth / coverage reported":        r"(?:mean|average|median) (?:sequencing |read )?(?:depth|coverage)|\d+\s?[x×] (?:coverage|depth)|fold[- ]80",
 "on-target / capture rate reported":     r"on[- ]target|off[- ]target|capture efficiency|fold enrichment|bait",
 "5'-3' bias / RNA coverage reported":    r"5[′']-3[′']|5[′'] to 3[′']|gene body coverage|transcript coverage",
 "mapping rate / % mapped reported":      r"(?:mapping|alignment) rate|% (?:of (?:the )?reads )?(?:mapped|aligned)|uniquely (?:mapped|aligned)",
 "GC bias reported":                      r"GC[- ]bias|GC content bias|GC dropout|AT dropout",
 "RNA-seq":                               r"RNA-?seq|transcriptom",
 "WES / exome / targeted":                r"whole[- ]exome|\bWES\b|exome|target(?:ed)? (?:capture|enrichment|sequencing)|hybrid(?:ization)? capture|panel sequencing",
 "WGS":                                   r"whole[- ]genome sequencing|\bWGS\b",
 "bisulfite / methylation":               r"bisulfite|WGBS|RRBS|Bismark|methylation",
 "ATAC / ChIP / CUT&RUN / Hi-C":          r"ATAC|ChIP-?seq|CUT&RUN|CUT&Tag|Hi-C",
 "single-cell":                           r"single[- ]cell|scRNA|10x Genomics|Cell Ranger",
 "long reads (nanopore / PacBio)":        r"[Nn]anopore|PacBio|long[- ]read|HiFi",
 "variant calling (GATK etc.)":           r"variant call|GATK|HaplotypeCaller|Mutect|freebayes|DeepVariant|Strelka",
 "samtools also used":                    r"[Ss][Aa][Mm][Tt]ools",
 "MultiQC used":                          r"MultiQC",
 "GATK used":                             r"\bGATK\b|Genome Analysis Toolkit",
 "Picard version stated":                 r"[Pp]icard(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"MarkDuplicates", "duplication rate reported", "insert size reported", "mean depth / coverage reported", "on-target / capture rate reported",
      "mapping rate / % mapped reported", "GC bias reported", "RNA-seq", "WES / exome / targeted", "WGS", "bisulfite / methylation", "variant calling (GATK etc.)"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Pp]icard(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"MAPQ\s*(?:>=?|≥|of|above|greater than|at least)\s*(\d+)|mapping quality\s*(?:>=?|≥|of|above|greater than|at least|threshold(?: of)?)\s*(\d+)|-q\s?(\d+)", re.I)
MITO  = re.compile(r"(\d{1,3}(?:\.\d)?)\s?[x×]\s?(?:coverage|depth)|(?:mean|average|median) (?:sequencing |read )?(?:depth|coverage)[^.;]{0,30}?(\d{1,4}(?:\.\d)?)\s?[x×]?", re.I)
PADJ  = re.compile(r"(?:duplication|duplicate) rate[^.;]{0,25}?(\d{1,2}(?:\.\d+)?)\s?%", re.I)
LFC   = re.compile(r"(?:mapping|alignment) rate[^.;]{0,25}?(\d{1,3}(?:\.\d+)?)\s?%|(\d{1,3}(?:\.\d+)?)\s?% (?:of (?:the )?reads )?(?:mapped|aligned)", re.I)
DIMS  = re.compile(r"insert[- ]size[^.;]{0,40}?(\d{2,4})\s?(?:bp|nt|base)", re.I)
KWIN  = re.compile(r"[Pp]icard(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major == 1: return "1.x (pre-2016)"
    if major == 2: return "2.%d" % (minor // 10 * 10) + "x"
    if major == 3: return "3.x"
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
        "mapq_thresholds": sorted({a or b or c for a, b, c in RES.findall(text)}),
        "depth_x": sorted({a or b for a, b in MITO.findall(text)}),
        "dup_rate_pct": sorted(set(PADJ.findall(text))),
        "mapping_rate_pct": sorted({a or b for a, b in LFC.findall(text)}),
        "insert_sizes": sorted({int(d) for d in DIMS.findall(text) if 50 <= int(d) <= 5000}),
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
        if row["package"] == "Picard":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "Picard")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("picard_profiles.jsonl", "w") as fh:
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
    for r in c["mapq_thresholds"]: res[r] += 1
    for m in c["depth_x"]: mito[m] += 1
    for p in c["dup_rate_pct"]: padj[p] += 1
    for l in c["mapping_rate_pct"]: lfc[l] += 1
    for d in c["insert_sizes"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nMAPQ thresholds:", dict(res.most_common(10)))
print("depth (x):", dict(mito.most_common(10)))
print("duplication rate %:", dict(padj.most_common(8)))
print("mapping rate %:", dict(lfc.most_common(8)))
print("insert sizes (bp):", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
