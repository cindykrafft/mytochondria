#!/usr/bin/env python3
"""Profile how each cohort paper used STAR (the RNA-seq aligner).

Mines the full text for the choices that select STAR code paths: the outputs
read (ReadsPerGene / --quantMode GeneCounts, Aligned.toTranscriptome for
RSEM/salmon, SJ.out.tab for splicing tools, chimeric output for fusion callers),
the options stated (2-pass, multimapper limits, strandedness, ENCODE settings),
the downstream counters (featureCounts, htseq-count, RSEM), the numbers reported
(uniquely mapped %, mapping rate), the data type and the stated STAR version.
One JSONL record per paper.

Usage: python3 star_profile.py            (fetch full texts, cache fallback)
       python3 star_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the STAR evidence sentence in
                 paper_software.tsv plus every per-package evidence snippet in
                 pipelines.jsonl.gz. A few hundred characters per package, so
                 feature counts from this source are LOWER BOUNDS on usage, not
                 measurements of it.

As for the Seurat, Scanpy and SAMtools audits, the 2026-09-13 run had no route
to Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI
likewise), so every record in star_profiles.jsonl is source=survey_cache. Rerun
from a host with Europe PMC access to replace them; the fetch path is unchanged
from the other audits. Version regexes require "STAR" in capitals followed by a
non-letter, so that "start", "Stargazer" and "STAR-Fusion" versions are not
taken as STAR versions.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "STAR named":                          r"\bSTAR\b(?!-Fusion)",
 "STAR version stated":                 r"\bSTAR\b(?![A-Za-z-])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "GeneCounts / ReadsPerGene":           r"quantMode|GeneCounts|ReadsPerGene",
 "TranscriptomeSAM / RSEM / salmon":    r"TranscriptomeSAM|toTranscriptome|\bRSEM\b|\bsalmon\b|kallisto",
 "featureCounts / htseq-count":         r"featureCounts|htseq-?count|HTSeq|Rsubread",
 "2-pass mode":                         r"two-?pass|2-?pass|twopassMode",
 "SJ.out.tab / splicing analysis":      r"SJ\.out|splice junction|rMATS|LeafCutter|MAJIQ|SUPPA|alternative splicing",
 "multimapper option stated":           r"outFilterMultimapNmax|multi-?mapp|multiple loci",
 "stranded library":                    r"strand-?specific|stranded|dUTP",
 "paired-end reads":                    r"paired-?end",
 "single-cell / STARsolo":              r"STARsolo|soloType|single-?cell|scRNA|10[xX] Genomics|Cell ?Ranger",
 "chimeric / fusion":                   r"STAR-Fusion|chimSegmentMin|chimeric|[Aa]rriba|gene fusion",
 "ENCODE options":                      r"ENCODE (?:options|parameters|standard|pipeline)|outFilterType BySJout|alignSJoverhangMin",
 "uniquely mapped reads reported":      r"uniquely (?:mapped|aligned)|unique(?:ly)? mapping",
 "mapping rate / % mapped reported":    r"(?:mapping|alignment) rate|(?:mapped|aligned) reads[^.]{0,40}%|% (?:of reads )?(?:mapped|aligned)|percent(?:age)? (?:of reads )?(?:mapped|aligned)",
 "GENCODE / Ensembl annotation":        r"GENCODE|Ensembl|RefSeq|GTF",
 "human genome (GRCh38/hg38/hg19)":     r"GRCh3[78]|hg[13][89]",
 "mouse genome (GRCm38/39, mm10)":      r"GRCm3[89]|mm(?:10|39)",
 "sjdbOverhang stated":                 r"sjdbOverhang",
 "outSAMstrandField / Cufflinks / StringTie": r"outSAMstrandField|Cufflinks|StringTie",
 "DESeq2 / edgeR / limma downstream":   r"DESeq2|edgeR|limma",
 "MultiQC / QC":                        r"MultiQC|RSeQC|Qualimap|FastQC",
 "Picard / samtools also used":         r"Picard|[Ss]amtools",
 "ribosomal / mitochondrial filtering": r"rRNA|ribosomal|mitochondrial reads",
 "trimming before STAR":                r"Trimmomatic|[Cc]utadapt|fastp|Trim Galore|TrimGalore",
}
CI = {"GeneCounts / ReadsPerGene", "2-pass mode", "SJ.out.tab / splicing analysis", "multimapper option stated",
      "stranded library", "paired-end reads", "uniquely mapped reads reported", "mapping rate / % mapped reported",
      "single-cell / STARsolo", "MultiQC / QC", "ribosomal / mitochondrial filtering"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"\bSTAR\b(?![A-Za-z-])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*[a-z]?)")
RES   = re.compile(r"outFilterMultimapNmax\s*(\d+)|(?:up to|at most|maximum of|max(?:imum)?)\s*(\d+)\s*(?:loci|locations|alignments)", re.I)
MITO  = re.compile(r"sjdbOverhang\s*(\d+)", re.I)
PADJ  = re.compile(r"uniquely (?:mapped|aligned)[^.;]{0,40}?(\d{1,3}(?:\.\d+)?)\s?%|(\d{1,3}(?:\.\d+)?)\s?% (?:of (?:the )?reads )?(?:were |was )?uniquely (?:mapped|aligned)", re.I)
LFC   = re.compile(r"(?:mapping|alignment) rate[^.;]{0,25}?(\d{1,3}(?:\.\d+)?)\s?%|(\d{1,3}(?:\.\d+)?)\s?% (?:of (?:the )?reads )?(?:mapped|aligned)", re.I)
DIMS  = re.compile(r"(\d{2,3})\s?(?:bp|nt|base|-base)[- ](?:paired-end |single-end |)reads", re.I)
KWIN  = re.compile(r"\bSTAR\b(?!-Fusion)")

def family(v):
    m = re.match(r"(\d+)\.(\d+)(?:\.(\d+))?", v)
    if not m: return None
    major, minor, patch = int(m.group(1)), int(m.group(2)), m.group(3)
    if major != 2: return None
    if minor >= 7 and patch is not None: return "2.7.%s" % patch
    return "%d.%d" % (major, minor)

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
        "multimap_nmax": sorted({a or b for a, b in RES.findall(text)}),
        "sjdb_overhang": sorted(set(MITO.findall(text))),
        "unique_mapped_pct": sorted({a or b for a, b in PADJ.findall(text)}),
        "mapping_rate_pct": sorted({a or b for a, b in LFC.findall(text)}),
        "read_lengths": sorted({int(d) for d in DIMS.findall(text) if 25 <= int(d) <= 300}),
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
        if row["package"] == "STAR":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "STAR")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, STAR, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "STAR".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("star_profiles.jsonl", "w") as fh:
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
    for r in c["multimap_nmax"]: res[r] += 1
    for m in c["sjdb_overhang"]: mito[m] += 1
    for p in c["unique_mapped_pct"]: padj[p] += 1
    for l in c["mapping_rate_pct"]: lfc[l] += 1
    for d in c["read_lengths"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\noutFilterMultimapNmax / max loci:", dict(res.most_common(10)))
print("sjdbOverhang:", dict(mito.most_common(10)))
print("uniquely mapped %:", dict(padj.most_common(8)))
print("mapping rate %:", dict(lfc.most_common(8)))
print("read lengths (bp):", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
