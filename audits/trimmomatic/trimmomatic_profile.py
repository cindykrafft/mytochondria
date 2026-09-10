#!/usr/bin/env python3
"""Profile how each cohort paper used Trimmomatic.

Mines the full text for the choices that select Trimmomatic code paths: the
trimming steps named (ILLUMINACLIP, SLIDINGWINDOW, LEADING, TRAILING, MINLEN,
CROP, HEADCROP, MAXINFO, AVGQUAL, TOPHRED33/64), their parameter values, the
adapter file, paired- or single-end mode, the Phred flag, thread count, and the
stated Trimmomatic version. One JSONL record per paper.

Usage: python3 trimmomatic_profile.py            (fetch full texts, cache fallback)
       python3 trimmomatic_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the Trimmomatic evidence
                 sentence in paper_software.tsv plus every per-package evidence
                 snippet in pipelines.jsonl.gz. A few hundred characters per
                 package, so feature counts from this source are LOWER BOUNDS on
                 usage, not measurements of it.

As for the Seurat, Scanpy, Cutadapt and fastp audits, the 2026-09-09 run had no
route to Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI
likewise), so every record in trimmomatic_profiles.jsonl is source=survey_cache.
Rerun from a host with Europe PMC access to replace them; the fetch path is
unchanged from the other audits.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 # steps
 "ILLUMINACLIP (adapter clipping)":   r"ILLUMINACLIP|adapt[eo]r[s]?[^.;]{0,40}(?:trim|remov|clip|cut)|(?:trim|remov|clip)[^.;]{0,30}adapt[eo]r",
 "ILLUMINACLIP parameters stated":    r"ILLUMINACLIP:[^\s:]+:\d+:\d+:\d+",
 "palindrome / keepBothReads / minAdapterLength": r"keepBothReads|palindrom|minAdapterLength|ILLUMINACLIP:[^\s:]+:\d+:\d+:\d+:\d+",
 "TruSeq3-PE / PE-2 adapters":        r"TruSeq3-PE|TruSeq3_PE",
 "TruSeq2 adapters":                  r"TruSeq2",
 "NexteraPE adapters":                r"Nextera",
 "TruSeq3-SE adapters":               r"TruSeq3-SE",
 "custom adapter file":               r"custom adapter|adapter (?:fasta|file|sequences?) (?:was|were|containing)|adapters?\.fa\b",
 "SLIDINGWINDOW":                     r"SLIDINGWINDOW|sliding[- ]window",
 "LEADING":                           r"LEADING:?\s*\d|leading (?:bases|low[- ]quality)",
 "TRAILING":                          r"TRAILING:?\s*\d|trailing (?:bases|low[- ]quality)",
 "MINLEN":                            r"MINLEN|minimum (?:read )?length|shorter than \d+|reads? (?:below|less than|<)\s*\d+\s*(?:bp|nt|bases)",
 "CROP":                              r"\bCROP:?\s*\d",
 "HEADCROP":                          r"HEADCROP",
 "TAILCROP":                          r"TAILCROP",
 "MAXINFO":                           r"MAXINFO",
 "AVGQUAL":                           r"AVGQUAL|average quality",
 "TOPHRED33/64":                      r"TOPHRED33|TOPHRED64",
 "MAXLEN / BASECOUNT":                r"\bMAXLEN\b|BASECOUNT",
 # mode and options
 "paired-end mode (PE)":              r"\bPE\b|paired[- ]end|read pairs|paired reads",
 "single-end mode (SE)":              r"\bSE\b|single[- ]end",
 "-phred33 / -phred64":               r"-?phred ?(?:33|64)",
 "-threads":                          r"-threads|\d+ threads",
 "-trimlog / -summary":               r"-trimlog|-summary",
 "unpaired reads discarded / used":   r"unpaired|orphan",
 "default parameters stated":         r"default (?:parameters|settings|options)|with default",
 "Trimmomatic version stated":        r"Trimmomatic(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 # what the reads are
 "RNA-seq":                           r"RNA-?seq|transcriptom",
 "WGS / WES / resequencing":          r"whole[- ]genome sequencing|\bWGS\b|\bWES\b|exome|resequenc",
 "metagenomics / 16S / amplicon":     r"metagenom|16S|amplicon|shotgun sequencing of",
 "ATAC / ChIP / CUT&RUN":             r"ATAC-?seq|ChIP-?seq|CUT ?& ?(?:RUN|Tag)|CUT&RUN",
 "single-cell":                       r"single[- ]cell|scRNA|snRNA|10x Genomics",
 "small RNA / miRNA":                 r"small RNA|miRNA|microRNA|sRNA-?seq",
 "bisulfite / methylation":           r"bisulfite|methylation|WGBS|RRBS",
 # neighbours
 "fastp also used":                   r"\bfastp\b",
 "Cutadapt / Trim Galore also used":  r"[Cc]utadapt|[Tt]rim[- ]?[Gg]alore",
 "FastQC / MultiQC also used":        r"FastQC|MultiQC",
}
CI = {"ILLUMINACLIP (adapter clipping)", "paired-end mode (PE)", "single-end mode (SE)", "RNA-seq",
      "WGS / WES / resequencing", "metagenomics / 16S / amplicon", "single-cell", "small RNA / miRNA",
      "bisulfite / methylation", "default parameters stated", "SLIDINGWINDOW", "MINLEN", "AVGQUAL",
      "-phred33 / -phred64", "-threads", "unpaired reads discarded / used", "custom adapter file",
      "palindrome / keepBothReads / minAdapterLength"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER    = re.compile(r"Trimmomatic(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)", re.I)
ICLIP  = re.compile(r"ILLUMINACLIP:[^\s:]+:(\d+):(\d+):(\d+)(?::(\d+))?(?::(true|false|TRUE|FALSE|True|False))?")
SWIN   = re.compile(r"SLIDINGWINDOW:(\d+):(\d+)")
LEAD   = re.compile(r"LEADING:(\d+)")
TRAIL  = re.compile(r"TRAILING:(\d+)")
MINL   = re.compile(r"MINLEN:(\d+)")
CROPV  = re.compile(r"\bCROP:(\d+)")
HCROP  = re.compile(r"HEADCROP:(\d+)")
MAXI   = re.compile(r"MAXINFO:(\d+):([\d.]+)")
AVGQ   = re.compile(r"AVGQUAL:(\d+)")
ADFILE = re.compile(r"ILLUMINACLIP:([^\s:]+):")
KWIN   = re.compile(r"Trimmomatic(?![A-Za-z])", re.I)


def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    return "%s.%s" % (m.group(1), m.group(2)) if m else None


def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers = set(VER.findall(text))
    if c.get("version_survey"):
        vers.add(c["version_survey"])
    vers = sorted(vers)
    fams = sorted({f for f in (family(v) for v in vers) if f})
    c.update({
        "source": source,
        "features": feats,
        "versions_all": vers,
        "version_family": fams,
        "illuminaclip": sorted({":".join(x for x in m if x) for m in ICLIP.findall(text)}),
        "adapter_file": sorted({m.split("/")[-1] for m in ADFILE.findall(text)}),
        "slidingwindow": sorted({"%s:%s" % m for m in SWIN.findall(text)}),
        "leading": sorted(set(LEAD.findall(text))),
        "trailing": sorted(set(TRAIL.findall(text))),
        "minlen": sorted(set(MINL.findall(text))),
        "crop": sorted(set(CROPV.findall(text))),
        "headcrop": sorted(set(HCROP.findall(text))),
        "maxinfo": sorted({"%s:%s" % m for m in MAXI.findall(text)}),
        "avgqual": sorted(set(AVGQ.findall(text))),
    })
    if source == "fulltext":
        ctx = []
        for m in KWIN.finditer(text):
            lo = max(0, m.start() - 260); hi = min(len(text), m.end() + 320)
            ctx.append(("..." + text[lo:hi] + "...").strip())
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
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("trimmomatic_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c) + "\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
extra = {k: Counter() for k in ("illuminaclip", "adapter_file", "slidingwindow", "leading", "trailing",
                                "minlen", "crop", "headcrop", "maxinfo", "avgqual")}
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for k in extra:
        for v in c[k]: extra[k][v] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-46s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nSTATED PARAMETER VALUES:")
for k, ctr in extra.items():
    if ctr: print("  %-16s %s" % (k, dict(ctr.most_common(10))))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
