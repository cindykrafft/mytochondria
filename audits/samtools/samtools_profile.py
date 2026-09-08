#!/usr/bin/env python3
"""Profile how each cohort paper used SAMtools.

Mines the full text for the choices that select SAMtools code paths:
the subcommands named (sort/index/view/flagstat/stats/depth/coverage/idxstats/
mpileup/markdup/...), MAPQ and flag filters, the QC numbers reported (mapping
rate, depth, insert size, duplication and error rates), the data type, and
the stated samtools version. One JSONL record per paper.

Usage: python3 samtools_profile.py            (fetch full texts, cache fallback)
       python3 samtools_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the SAMtools evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat and Scanpy audits, the 2026-09-08 run had no route to Europe PMC (www.ebi.ac.uk denied by the
session's egress policy; NCBI likewise), so every record in
samtools_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "samtools" (any case).
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "samtools named":                       r"[Ss][Aa][Mm][Tt]ools",
 "sort":                                 r"samtools sort|sorted (?:with|using|by) samtools|coordinate[- ]sorted",
 "index":                                r"samtools index|indexed (?:with|using) samtools",
 "view / filtering":                     r"samtools view|filtered (?:with|using) samtools",
 "MAPQ filter stated":                   r"MAPQ\s*(?:>=?|≥|of|above|greater than|at least)\s*\d+|mapping quality\s*(?:>=?|≥|of|above|greater than|at least|threshold)\s*\d+|-q\s?\d+",
 "-f/-F flag filter":                    r"\s-[fF]\s?(?:0x)?\d+|properly paired reads (?:were|was) (?:retained|kept|selected)|-F\s?0x?4",
 "flagstat":                             r"flagstat",
 "stats":                                r"samtools stats|bamstats|plot-bamstats",
 "depth":                                r"samtools depth",
 "coverage":                             r"samtools coverage|samtools bedcov|bedcov",
 "idxstats":                             r"idxstats",
 "mpileup":                              r"mpileup",
 "markdup / rmdup / duplicates":         r"markdup|rmdup|duplicate",
 "fixmate":                              r"fixmate",
 "merge":                                r"samtools merge",
 "faidx":                                r"faidx",
 "fastq / bam2fq":                       r"samtools fastq|bam2fq",
 "consensus / calmd":                    r"samtools consensus|calmd",
 "insert size reported":                 r"insert[- ]size",
 "mapping rate / % mapped reported":     r"(?:mapping|alignment) rate|(?:mapped|aligned) reads[^.]{0,40}%|% (?:of reads )?(?:mapped|aligned)|percent(?:age)? (?:of reads )?(?:mapped|aligned)",
 "mean depth / coverage reported":       r"(?:mean|average|median) (?:sequencing |read )?(?:depth|coverage)|\d+\s?[x×] (?:coverage|depth)|coverage of \d+",
 "duplication rate reported":            r"duplication rate|duplicate rate|PCR duplicates",
 "error / mismatch rate reported":       r"error rate|mismatch rate",
 "Picard also used":                     r"Picard|MarkDuplicates",
 "bcftools also used":                   r"bcftools",
 "htslib named":                         r"htslib|HTSlib",
 "BWA / Bowtie / STAR / minimap2 aligner": r"\bBWA\b|bwa[- ]mem|[Bb]owtie|\bSTAR\b|minimap2|HISAT",
 "RNA-seq / spliced":                    r"RNA-?seq|spliced|transcriptom",
 "long reads (nanopore / PacBio)":        r"[Nn]anopore|PacBio|long[- ]read|HiFi",
 "ATAC / ChIP / CUT&RUN":                r"ATAC|ChIP-?seq|CUT&RUN|CUT&Tag",
 "WGS / WES / exome":                    r"whole[- ]genome sequencing|\bWGS\b|whole[- ]exome|\bWES\b|exome",
 "variant calling":                      r"variant call|GATK|freebayes|DeepVariant",
 "samtools version stated":              r"[Ss][Aa][Mm][Tt]ools(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"sort", "index", "view / filtering", "MAPQ filter stated", "flagstat", "stats", "depth", "coverage", "idxstats",
      "mpileup", "markdup / rmdup / duplicates", "fixmate", "merge", "faidx", "fastq / bam2fq", "consensus / calmd",
      "insert size reported", "mapping rate / % mapped reported", "mean depth / coverage reported",
      "duplication rate reported", "error / mismatch rate reported", "RNA-seq / spliced", "WGS / WES / exome", "variant calling"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Ss][Aa][Mm][Tt]ools(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"MAPQ\s*(?:>=?|≥|of|above|greater than|at least)\s*(\d+)|mapping quality\s*(?:>=?|≥|of|above|greater than|at least|threshold(?: of)?)\s*(\d+)|-q\s?(\d+)", re.I)
MITO  = re.compile(r"(\d{1,3}(?:\.\d)?)\s?[x×]\s?(?:coverage|depth)|(?:mean|average|median) (?:sequencing |read )?(?:depth|coverage)[^.;]{0,30}?(\d{1,4}(?:\.\d)?)\s?[x×]?", re.I)
PADJ  = re.compile(r"(?:duplication|duplicate) rate[^.;]{0,25}?(\d{1,2}(?:\.\d+)?)\s?%", re.I)
LFC   = re.compile(r"(?:mapping|alignment) rate[^.;]{0,25}?(\d{1,3}(?:\.\d+)?)\s?%|(\d{1,3}(?:\.\d+)?)\s?% (?:of (?:the )?reads )?(?:mapped|aligned)", re.I)
DIMS  = re.compile(r"insert[- ]size[^.;]{0,40}?(\d{2,4})\s?(?:bp|nt|base)", re.I)
KWIN  = re.compile(r"[Ss]canpy(?![A-Za-z])")

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
        if row["package"] == "SAMtools":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "SAMtools")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("samtools_profiles.jsonl", "w") as fh:
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
