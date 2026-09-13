#!/usr/bin/env python3
"""Profile how each cohort paper used Trimmomatic.

Mines the full text for the choices that select Trimmomatic code paths: the trimming
steps named on the command line (ILLUMINACLIP with its adapter file and thresholds,
SLIDINGWINDOW, LEADING/TRAILING, MINLEN, HEADCROP/CROP, MAXINFO, AVGQUAL, TOPHRED),
paired- vs single-end mode, the Phred flag, and the stated Trimmomatic version. One JSONL
record per paper.

Usage: python3 trimmomatic_profile.py            (fetch full texts, cache fallback)
       python3 trimmomatic_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the Trimmomatic evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy, Cutadapt and fastp audits, the 2026-09-13 run had no route to
Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so every
record in trimmomatic_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require a word boundary after "Trimmomatic".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-insensitive throughout: the step names are upper-case on the command line but papers
# also write them in prose ("sliding window", "leading", "minimum length").
FEATURES = {
 "ILLUMINACLIP / adapter clipping":       r"ILLUMINACLIP|adapter",
 "ILLUMINACLIP 2:30:10 (thresholds)":     r"ILLUMINACLIP:[^ ]*?:2:30:10|2:30:10",
 "palindrome / keepBothReads":            r"keepBothReads|palindrome|:2:30:10:\d+:(?:true|false)",
 "TruSeq3-PE adapters":                   r"TruSeq3-PE",
 "TruSeq3-SE adapters":                   r"TruSeq3-SE",
 "TruSeq2 adapters":                      r"TruSeq2",
 "Nextera adapters":                      r"Nextera",
 "custom adapter file":                   r"ILLUMINACLIP:(?!TruSeq|Nextera)[A-Za-z0-9_./-]+\.fa",
 "SLIDINGWINDOW":                         r"SLIDINGWINDOW|sliding[- ]window",
 "SLIDINGWINDOW:4:15":                    r"SLIDINGWINDOW:4:15",
 "SLIDINGWINDOW:4:20":                    r"SLIDINGWINDOW:4:20",
 "LEADING":                               r"LEADING:\d+|\bleading\b",
 "TRAILING":                              r"TRAILING:\d+|\btrailing\b",
 "LEADING:3 TRAILING:3":                  r"LEADING:3\b|TRAILING:3\b",
 "MINLEN":                                r"MINLEN|minimum (?:read )?length|min(?:imal|imum)? length",
 "MINLEN:36":                             r"MINLEN:36",
 "HEADCROP":                              r"HEADCROP",
 "CROP":                                  r"(?<!HEAD)(?<!TAIL)CROP:\d+",
 "MAXINFO":                               r"MAXINFO",
 "AVGQUAL":                               r"AVGQUAL",
 "TOPHRED33/64":                          r"TOPHRED",
 "-phred33 / -phred64 flag":              r"-phred(?:33|64)|phred\s*\+?\s*(?:33|64)",
 "paired-end":                            r"paired[- ]end|\bPE\b|TrimmomaticPE",
 "single-end":                            r"single[- ]end|\bSE\b|TrimmomaticSE",
 "default parameters stated":            r"default (?:parameter|setting|option)|default",
 "Trimmomatic version stated":            r"Trimmomatic(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "quality threshold stated (Q/phred)":    r"(?:quality|phred)[^.;]{0,30}?(?:<|>|≤|≥|below|above|of|score)\s*\d{1,2}\b|Q\s?\d{2}\b",
 "FastQC / MultiQC also used":            r"FastQC|MultiQC",
 "Cutadapt / Trim Galore / fastp also used": r"[Cc]utadapt|Trim ?Galore|fastp",
 "RNA-seq":                               r"RNA[- ]?seq|transcriptom",
 "metagenomics / 16S / amplicon":         r"metagenom|16S|amplicon|ITS\b",
 "ChIP / ATAC / CUT&RUN":                 r"ChIP|ATAC|CUT&(?:RUN|Tag)",
 "WGS / variant calling / resequencing":  r"whole[- ]genome|WGS|variant call|resequenc|SNP",
 "assembly":                              r"assembl",
 "single-cell":                           r"single[- ]cell|scRNA|10x",
 "small RNA / miRNA":                     r"small RNA|miRNA|microRNA",
}
CI = set(FEATURES)
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"Trimmomatic(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)", re.I)
SW    = re.compile(r"SLIDINGWINDOW:(\d+:\d+)", re.I)
MINL  = re.compile(r"MINLEN:(\d+)", re.I)
LEAD  = re.compile(r"LEADING:(\d+)", re.I)
TRAIL = re.compile(r"TRAILING:(\d+)", re.I)
CLIP  = re.compile(r"ILLUMINACLIP:[^ :]*:(\d+:\d+:\d+(?::\d+(?::(?:true|false))?)?)", re.I)
HEADC = re.compile(r"HEADCROP:(\d+)", re.I)
KWIN  = re.compile(r"Trimmomatic(?![A-Za-z])", re.I)

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major != 0: return None          # Trimmomatic has only had 0.x releases
    return "0.%d" % minor

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
        "slidingwindow": sorted(set(m.upper() for m in SW.findall(text))),
        "minlen": sorted({int(x) for x in MINL.findall(text)}),
        "leading": sorted({int(x) for x in LEAD.findall(text)}),
        "trailing": sorted({int(x) for x in TRAIL.findall(text)}),
        "illuminaclip": sorted(set(m.lower() for m in CLIP.findall(text))),
        "headcrop": sorted({int(x) for x in HEADC.findall(text)}),
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
        if row["package"] == "Trimmomatic":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "Trimmomatic")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Trimmomatic, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Trimmomatic".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("trimmomatic_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
sw, ml, ld, tr, cl, hc = Counter(), Counter(), Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for x in c["slidingwindow"]: sw[x] += 1
    for x in c["minlen"]: ml[x] += 1
    for x in c["leading"]: ld[x] += 1
    for x in c["trailing"]: tr[x] += 1
    for x in c["illuminaclip"]: cl[x] += 1
    for x in c["headcrop"]: hc[x] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nSLIDINGWINDOW window:quality:", dict(sw.most_common(12)))
print("MINLEN:", dict(ml.most_common(12)))
print("LEADING:", dict(ld.most_common(8)))
print("TRAILING:", dict(tr.most_common(8)))
print("ILLUMINACLIP seed:palindrome:simple[:minAdapter:keepBoth]:", dict(cl.most_common(8)))
print("HEADCROP:", dict(hc.most_common(8)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
