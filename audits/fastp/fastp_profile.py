#!/usr/bin/env python3
"""Profile how each cohort paper used fastp.

Mines the full text for the choices that select fastp code paths: adapter
trimming and auto-detection, the sliding-window cutters and their window/quality
settings, global trimming, the quality/length/complexity filters, poly-G/poly-X
trimming, base correction, deduplication, UMI handling, overrepresentation
analysis, output splitting, threading, and the stated fastp version.
One JSONL record per paper.

Usage: python3 fastp_profile.py            (fetch full texts, cache fallback)
       python3 fastp_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the fastp evidence sentence
                 in paper_software.tsv plus every per-package evidence snippet
                 in pipelines.jsonl.gz. A few hundred characters per package,
                 so feature counts from this source are LOWER BOUNDS on usage,
                 not measurements of it.

As for the Seurat, Scanpy and Cutadapt audits, the 2026-09-03 run had no route to
Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI likewise),
so every record in fastp_profiles.jsonl is source=survey_cache. Rerun from a host
with Europe PMC access to replace them; the fetch path is unchanged from the
other audits.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 # adapters
 "adapter trimming mentioned":        r"adapt[eo]r[s]?[^.;]{0,40}(?:trim|remov|clip|cut)|(?:trim|remov|clip)[^.;]{0,30}adapt[eo]r",
 "adapter auto-detection":            r"auto[- ]?detect|automatic(?:ally)? detect|detect_adapter",
 "--adapter_sequence given":          r"adapter_sequence|-a\s+[ACGT]{6,}|AGATCGGAAGAGC|CTGTCTCTTATACACATCT|TGGAATTCTCGGGTGCCAAGG",
 "--detect_adapter_for_pe":           r"detect_adapter_for_pe|\B-2\b",
 "--adapter_fasta":                   r"adapter_fasta",
 "Illumina TruSeq / Nextera named":   r"TruSeq|Nextera|NEBNext|small ?RNA adapter|RPI\d",
 # sliding-window cutting
 "--cut_front (-5)":                  r"cut_front|cut_by_quality5|\B-5\b",
 "--cut_tail (-3)":                   r"cut_tail|cut_by_quality3|\B-3\b",
 "--cut_right (-r)":                  r"cut_right|cut_by_quality_aggressive|sliding window|SLIDINGWINDOW",
 "cut window size / mean quality":    r"cut_window_size|cut_mean_quality|cut_(?:front|tail|right)_(?:window_size|mean_quality)|window (?:size|of) \d",
 # global trimming
 "--trim_front1/2 (-f/-F)":           r"trim_front|\B-f\s*\d|\B-F\s*\d|trim(?:med|ming)?[^.;]{0,30}(?:5['′]|first|leading)[^.;]{0,20}(?:bp|bases|nucleotides)",
 "--trim_tail1/2 (-t/-T)":            r"trim_tail|\B-t\s*\d|\B-T\s*\d|trim(?:med|ming)?[^.;]{0,30}(?:3['′]|last|trailing)[^.;]{0,20}(?:bp|bases|nucleotides)",
 "--max_len1/2 (-b/-B)":              r"max_len|\B-b\s*\d{2,}|truncat[^.;]{0,30}\d{2,}\s*(?:bp|bases)",
 # filters
 "--qualified_quality_phred (-q)":    r"qualified_quality_phred|\B-q\s*\d|quality (?:score |value )?(?:of |>=?|≥)\s*\d{1,2}|Q\d{2} ?(?:cut|threshold)",
 "--unqualified_percent_limit (-u)":  r"unqualified_percent_limit|\B-u\s*\d",
 "--n_base_limit (-n)":               r"n_base_limit|\B-n\s*\d|(?:number of |maximum )?N (?:bases?|nucleotides?)[^.;]{0,20}(?:limit|>|more than)",
 "--average_qual (-e)":               r"average_qual|\B-e\s*\d{1,2}\b|mean quality[^.;]{0,25}(?:below|<|≤)\s*\d",
 "--length_required (-l)":            r"length_required|\B-l\s*\d|(?:shorter than|minimum length|less than)[^.;]{0,20}\d{2,}\s*(?:bp|bases|nt)",
 "--length_limit":                    r"length_limit",
 "--low_complexity_filter (-y)":      r"low_complexity|complexity_threshold|low[- ]complexity",
 "--disable_quality_filtering (-Q)":  r"disable_quality_filtering|\B-Q\b",
 "--disable_length_filtering (-L)":   r"disable_length_filtering",
 "--disable_adapter_trimming (-A)":   r"disable_adapter_trimming",
 # poly tails
 "--trim_poly_g (-g)":                r"trim_poly_g|poly[- ]?G|polyG",
 "--trim_poly_x (-x)":                r"trim_poly_x|poly[- ]?X|poly[- ]?A tail",
 # PE-specific
 "paired-end":                        r"paired[- ]end|\bPE\b|R1 and R2|read1 and read2",
 "--correction (-c)":                 r"\bcorrection\b|correct(?:ing|ed)? (?:mismatched )?bases|base correction",
 "--merge (-m)":                      r"merge[sd]? (?:the )?(?:overlapping )?(?:paired|reads|pairs)|merged_out|--merge\b",
 "overlap parameters":                r"overlap_len_require|overlap_diff_limit|overlap_diff_percent_limit",
 # duplication / UMI
 "--dedup (-D) / duplication":        r"\bdedup\b|deduplicat|duplication rate|duplicate reads|dup_calc_accuracy",
 "--umi (-U)":                        r"\bUMI\b|unique molecular identifier|umi_loc",
 # reporting / running
 "overrepresentation analysis (-p)":  r"overrepresentation|over[- ]represented sequence",
 "--split / --split_by_lines":        r"--split|split_by_lines",
 "--reads_to_process":                r"reads_to_process|subsampl|first \d+(?:,\d{3})* reads",
 "--thread (-w)":                     r"--thread|\B-w\s*\d|\d+ (?:CPU )?threads",
 "--phred64 (-6)":                    r"phred64|phred\+?64|Illumina 1\.[35]",
 "JSON/HTML report or Q20/Q30 cited": r"fastp (?:report|JSON|HTML)|Q20|Q30|q20_rate|q30_rate|GC content",
 "default parameters stated":         r"default (?:parameters|settings|options)|with default",
 # what the reads are
 "RNA-seq":                           r"RNA-?seq|transcriptom",
 "WGS / WES / resequencing":          r"whole[- ]genome sequencing|\bWGS\b|\bWES\b|exome|resequenc",
 "metagenomics / 16S / amplicon":     r"metagenom|16S|amplicon|shotgun sequencing of",
 "ATAC / ChIP / CUT&RUN":             r"ATAC-?seq|ChIP-?seq|CUT ?& ?(?:RUN|Tag)|CUT&RUN",
 "single-cell":                       r"single[- ]cell|scRNA|snRNA|10x Genomics",
 "small RNA / miRNA":                 r"small RNA|miRNA|microRNA|sRNA-?seq",
 "bisulfite / methylation":           r"bisulfite|methylation|WGBS|RRBS",
 "fastp version stated":              r"fastp(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 # neighbours
 "Trimmomatic also used":             r"Trimmomatic",
 "Cutadapt / Trim Galore also used":  r"[Cc]utadapt|[Tt]rim[- ]?[Gg]alore",
 "FastQC / MultiQC also used":        r"FastQC|MultiQC",
}
CI = {"adapter trimming mentioned", "adapter auto-detection", "paired-end", "RNA-seq",
      "WGS / WES / resequencing", "metagenomics / 16S / amplicon", "single-cell",
      "small RNA / miRNA", "bisulfite / methylation", "default parameters stated",
      "--correction (-c)", "--merge (-m)", "--dedup (-D) / duplication",
      "--low_complexity_filter (-y)", "--trim_poly_g (-g)", "--trim_poly_x (-x)",
      "--cut_right (-r)", "--thread (-w)", "--reads_to_process", "--phred64 (-6)"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"fastp(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)", re.I)
QCUT  = re.compile(r"(?:qualified_quality_phred|--?q(?:uality)?)[ =]{1,3}(\d{1,2})\b")
LREQ  = re.compile(r"(?:length_required|--?l(?:ength)?)[ =]{1,3}(\d{1,3})\b")
WIN   = re.compile(r"cut_(?:front|tail|right|window)_?(?:window_)?size[ =]{1,3}(\d{1,3})")
MEANQ = re.compile(r"cut_(?:front|tail|right|mean)_?(?:mean_)?quality[ =]{1,3}(\d{1,2})")
UNQ   = re.compile(r"unqualified_percent_limit[ =]{1,3}(\d{1,3})")
NBASE = re.compile(r"n_base_limit[ =]{1,3}(\d{1,2})")
AVGQ  = re.compile(r"average_qual[ =]{1,3}(\d{1,2})")
TRIMF = re.compile(r"trim_front[12][ =]{1,3}(\d{1,3})")
TRIMT = re.compile(r"trim_tail[12][ =]{1,3}(\d{1,3})")
KWIN  = re.compile(r"fastp(?![A-Za-z])", re.I)


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
        "q_cutoffs": sorted(set(QCUT.findall(text))),
        "length_required": sorted(set(LREQ.findall(text))),
        "cut_window_sizes": sorted(set(WIN.findall(text))),
        "cut_mean_quality": sorted(set(MEANQ.findall(text))),
        "unqualified_percent": sorted(set(UNQ.findall(text))),
        "n_base_limit": sorted(set(NBASE.findall(text))),
        "average_qual": sorted(set(AVGQ.findall(text))),
        "trim_front": sorted(set(TRIMF.findall(text))),
        "trim_tail": sorted(set(TRIMT.findall(text))),
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
        if row["package"] == "fastp":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "fastp")
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("fastp_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c) + "\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
extra = {k: Counter() for k in ("q_cutoffs", "length_required", "cut_window_sizes",
                                "cut_mean_quality", "unqualified_percent", "n_base_limit",
                                "average_qual", "trim_front", "trim_tail")}
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for k in extra:
        for v in c[k]: extra[k][v] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-38s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nSTATED PARAMETER VALUES:")
for k, ctr in extra.items():
    if ctr: print("  %-22s %s" % (k, dict(ctr.most_common(8))))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
