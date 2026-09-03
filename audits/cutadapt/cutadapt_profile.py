#!/usr/bin/env python3
"""Profile how each cohort paper used Cutadapt.

Mines the full text for the choices that select Cutadapt code paths: which
adapter options (-a/-g/-b, -A/-G, anchored, linked), quality trimming (-q,
--nextseq-trim), length filters (-m/-M), error rate (-e), overlap (-O),
--no-indels, --max-n, --max-ee, --trim-n, --poly-a, --pair-filter,
--interleaved, demultiplexing/barcodes, the Trim Galore wrapper, and the stated
Cutadapt version. One JSONL record per paper.

Usage: python3 cutadapt_profile.py            (fetch full texts, cache fallback)
       python3 cutadapt_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the Cutadapt evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat and Scanpy audits, the 2026-09-03 run had no route to Europe
PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so
every record in cutadapt_profiles.jsonl is source=survey_cache. Rerun from a
host with Europe PMC access to replace them; the fetch path is unchanged from
the other audits. Version regexes require a word boundary after "cutadapt".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 "3' adapter (-a) or 3' adapter named":     r"(?<![\w-])-a\s+[\"']?[ACGTUN^$]{4,}|3['′]\s*adapt|3['′]\s*end",
 "5' adapter (-g) or 5' adapter named":     r"(?<![\w-])-g\s+[\"']?[ACGTUN^]{4,}|5['′]\s*adapt|5['′]\s*(?:end|barcode)",
 "R2 adapter (-A/-G)":                      r"(?<![\w-])-[AG]\s+[\"']?[ACGTUN^$]{4,}",
 "anywhere adapter (-b)":                   r"(?<![\w-])-b\s+[\"']?[ACGTUN]{4,}",
 "linked adapter (ADAPTER1...ADAPTER2)":    r"[ACGTN]\.\.\.[ACGTN]|linked adapter",
 "anchored adapter (^ or $)":               r"(?<![\w-])-[gG]\s+[\"']?\^|[ACGT]{4,}\$",
 "quality trimming (-q / Phred cutoff)":    r"--quality-cutoff|(?<![\w-])-q\s*=?\s*\d|quality[- ]cut[- ]?off|quality[- ]trim|low[- ]quality (?:bases|ends|reads)|Phred[^.;]{0,25}(?:<|below|lower than|under)\s*\d|quality (?:score )?(?:<|below|lower than|of)\s*\d",
 "--nextseq-trim":                          r"--nextseq-trim|nextseq[- ]trim|two[- ]colou?r",
 "minimum length (-m)":                     r"--minimum-length|(?<![\w-])-m\s*=?\s*\d|min(?:imum)?[- ](?:read[- ])?length|(?:shorter|fewer|less) than \d+\s*(?:bp|nt|bases|nucleotides)",
 "maximum length (-M)":                     r"--maximum-length|(?<![\w-])-M\s*=?\s*\d|max(?:imum)?[- ](?:read[- ])?length",
 "error rate (-e)":                         r"--error-rate|(?<![\w-])-e\s*=?\s*\d|error[- ]rate|mismatch rate|mismatches? (?:allowed|permitted|tolerated)",
 "minimum overlap (-O)":                    r"--overlap|(?<![\w-])-O\s*=?\s*\d|overlap\s*(?:=|of|length)\s*\d",
 "--no-indels":                             r"--no-indels",
 "--times (-n)":                            r"--times|(?<![\w-])-n\s*=?\s*\d",
 "--max-n":                                 r"--max-n",
 "--max-ee / expected errors":              r"--max-ee|--max-expected-errors|expected errors",
 "--trim-n":                                r"--trim-n",
 "poly-A / poly-T trimming":                r"--poly-a|poly[- ]?\(?[AT]\)?[- ]?(?:tail|stretch|sequence|trim)|A\{\d+\}|T\{\d+\}",
 "fixed cut (-u/-U)":                       r"(?<![\w-])-[uU]\s*=?\s*-?\d|--cut\b",
 "shorten (-l/--length)":                   r"(?<![\w-])-l\s*=?\s*-?\d|--length\b",
 "--pair-filter":                           r"--pair-filter",
 "--interleaved":                           r"--interleaved",
 "--discard-untrimmed / --trimmed-only":    r"--discard-untrimmed|--trimmed-only|--untrimmed-output",
 "--discard-trimmed":                       r"--discard-trimmed",
 "--action (mask/retain/none)":             r"--action|--no-trim|--mask-adapter",
 "--revcomp":                               r"--revcomp|--rc\b",
 "demultiplexing / barcodes":               r"demultiplex|barcode|\{name\}",
 "UMI":                                     r"\bUMIs?\b|unique molecular identifier",
 "paired-end":                              r"paired[- ]end|read ?2|R2\b",
 "Trim Galore wrapper":                     r"Trim[ _]?Galore",
 "multi-core (-j)":                         r"(?<![\w-])-j\s*=?\s*\d|--cores",
 "Illumina TruSeq / universal adapter":     r"AGATCGGAAGAGC|TruSeq|universal adapter|Nextera|CTGTCTCTTATACACATCT",
 "small RNA / miRNA":                       r"small[- ]RNA|miRNA|microRNA|TGGAATTCTCGG|sRNA",
 "amplicon / 16S / primer removal":         r"16S|18S|ITS\b|amplicon|primer",
 "CRISPR screen / sgRNA":                   r"CRISPR|sgRNA|guide RNA|gRNA",
 "ribosome profiling":                      r"ribosome profiling|Ribo-?seq|footprint",
 "bisulfite / EM-seq":                      r"bisulfite|Bismark|EM-seq|WGBS|RRBS",
 "ATAC / ChIP / CUT&RUN / CUT&Tag":         r"ATAC|ChIP|CUT&(?:RUN|Tag)|CUT&amp;",
 "RNA-seq":                                 r"RNA-?seq",
 "single-cell":                             r"single[- ]cell|scRNA|10x|Cell ?Ranger",
 "nanopore / long reads":                   r"nanopore|Oxford|long[- ]read|PacBio",
 "cutadapt version stated":                 r"[Cc]ut[Aa]dapt(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"linked adapter (ADAPTER1...ADAPTER2)", "quality trimming (-q / Phred cutoff)", "--nextseq-trim",
      "minimum length (-m)", "maximum length (-M)", "error rate (-e)", "minimum overlap (-O)",
      "poly-A / poly-T trimming", "demultiplexing / barcodes", "paired-end", "Trim Galore wrapper",
      "small RNA / miRNA", "amplicon / 16S / primer removal", "ribosome profiling", "bisulfite / EM-seq",
      "RNA-seq", "single-cell", "nanopore / long reads"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Cc]ut[Aa]dapt(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
MINL  = re.compile(r"(?:--minimum-length|(?<![\w-])-m|min(?:imum)?[- ](?:read[- ])?length)\s*(?:=|of|:|\s)\s*(\d{1,3})", re.I)
QCUT  = re.compile(r"(?:--quality-cutoff|(?<![\w-])-q|quality[- ]cut[- ]?off|Phred(?: score)?(?: quality)?)\s*(?:=|of|<|:|\s)\s*(\d{1,2})", re.I)
ERATE = re.compile(r"(?:--error-rate|(?<![\w-])-e|error rate)\s*(?:=|of|:|\s)\s*(0?\.\d+|\d)", re.I)
OVERL = re.compile(r"(?:--overlap|(?<![\w-])-O|overlap)\s*(?:=|of|:|\s)\s*(\d{1,2})", re.I)
ADSEQ = re.compile(r"(?<![\w-])-[aAgGbB]\s+[\"']?\^?([ACGTUN]{6,}(?:\{\d+\})?)[\$\"']?")
KWIN  = re.compile(r"[Cc]ut[Aa]dapt(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    return m.group(1) + ".x"

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
        "min_lengths": sorted({int(x) for x in MINL.findall(text)}),
        "quality_cutoffs": sorted({int(x) for x in QCUT.findall(text)}),
        "error_rates": sorted(set(ERATE.findall(text))),
        "overlaps": sorted({int(x) for x in OVERL.findall(text)}),
        "adapter_sequences": sorted(set(ADSEQ.findall(text))),
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
        if row["package"] == "Cutadapt":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "Cutadapt")
        # Evidence snippets only (the pipeline_stages strings put other
        # packages' versions within a few characters of "Cutadapt").
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("cutadapt_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
minl, qcut, erate, overl, adseq = Counter(), Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for x in c["min_lengths"]: minl[x] += 1
    for x in c["quality_cutoffs"]: qcut[x] += 1
    for x in c["error_rates"]: erate[x] += 1
    for x in c["overlaps"]: overl[x] += 1
    for x in c["adapter_sequences"]: adseq[x] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-44s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 25):", dict(vc.most_common(25)))
print("\nminimum lengths:", dict(minl.most_common(10)))
print("quality cutoffs:", dict(qcut.most_common(10)))
print("error rates:", dict(erate.most_common(8)))
print("overlaps:", dict(overl.most_common(8)))
print("adapter sequences (top 10):", dict(adseq.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
