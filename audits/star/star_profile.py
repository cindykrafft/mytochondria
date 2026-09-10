#!/usr/bin/env python3
"""Profile how each cohort paper used STAR.

Mines the full text for the choices that select STAR code paths: the outputs
named (GeneCounts / ReadsPerGene, TranscriptomeSAM + RSEM, SJ.out.tab, sorted
BAM, chimeric output), the options stated (--twopassMode, --outFilterMultimapNmax,
--outSAMstrandField, --quantMode, --sjdbOverhang), the QC numbers reported (unique
mapping rate), the annotation and downstream tools, single-cell use (STARsolo),
and the stated STAR version. One JSONL record per paper.

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

As for the Seurat, Scanpy, Cutadapt and SAMtools audits, the 2026-09-09 run had no
route to Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI
likewise), so every record in star_profiles.jsonl is source=survey_cache. Rerun
from a host with Europe PMC access to replace them; the fetch path is unchanged
from the other audits. Version regexes require a word boundary after "STAR".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "STAR named":                            r"\bSTAR\b",
 "STAR version stated":                   r"\bSTAR\b(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "GeneCounts / ReadsPerGene":             r"quantMode GeneCounts|ReadsPerGene|GeneCounts",
 "TranscriptomeSAM / transcriptome BAM":  r"TranscriptomeSAM|toTranscriptome|transcriptome[- ]aligned|transcriptome BAM",
 "RSEM also used":                        r"\bRSEM\b",
 "2-pass mode":                           r"two[- ]?pass|twopassMode|2[- ]pass",
 "SJ.out.tab / novel junctions":          r"SJ\.out\.tab|splice junction|novel junction",
 "outFilterMultimapNmax stated":          r"outFilterMultimapNmax",
 "multimapper handling stated":           r"multi-?mapp|multiple loci|uniquely (?:mapped|aligned) reads (?:were|was) (?:retained|kept|used)",
 "outSAMstrandField / XS":                r"outSAMstrandField|intronMotif|XS tag",
 "sorted BAM output":                     r"SortedByCoordinate|coordinate[- ]sorted",
 "chimeric / fusion":                     r"chimSegmentMin|chimeric|STAR-Fusion|Arriba|fusion",
 "STARsolo":                              r"STARsolo|soloType|soloFeatures",
 "sjdbOverhang stated":                   r"sjdbOverhang",
 "ENCODE options":                        r"ENCODE (?:standard )?(?:options|parameters)|outFilterType BySJout",
 "featureCounts also used":               r"featureCounts|Subread",
 "HTSeq also used":                       r"HTSeq|htseq-count",
 "Salmon / kallisto also used":           r"\bSalmon\b|kallisto",
 "GENCODE / Ensembl annotation":          r"GENCODE|Ensembl",
 "RefSeq annotation":                     r"RefSeq",
 "StringTie / Cufflinks assembly":        r"StringTie|Cufflinks|Cuffdiff",
 "DESeq2 / edgeR / limma downstream":     r"DESeq2|edgeR|limma",
 "unique mapping rate reported":          r"uniquely (?:mapped|aligned)[^.]{0,40}%|% (?:of reads )?(?:uniquely|unique)|mapping rate",
 "paired-end":                            r"paired-?end",
 "single-cell / snRNA":                   r"single[- ]cell|scRNA|snRNA|10x Genomics|Chromium|Smart-?seq",
 "long reads":                            r"[Nn]anopore|PacBio|long[- ]read|Iso-Seq",
 "rMATS / splicing analysis":             r"rMATS|MAJIQ|LeafCutter|SUPPA|alternative splicing",
 "samtools also used":                    r"[Ss][Aa][Mm][Tt]ools",
 "Picard / duplicates":                   r"Picard|MarkDuplicates|duplicate",
 "RNA-SeQC / MultiQC / QC":               r"RNA-?SeQC|MultiQC|FastQC|Qualimap",
 "genome build stated":                   r"GRCh3[78]|hg19|hg38|GRCm3[89]|mm10|mm39|GRCz|TAIR",
}
CI = {"GeneCounts / ReadsPerGene", "2-pass mode", "SJ.out.tab / novel junctions", "multimapper handling stated",
      "sorted BAM output", "chimeric / fusion", "unique mapping rate reported", "paired-end", "single-cell / snRNA",
      "rMATS / splicing analysis", "Picard / duplicates"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"\bSTAR\b(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*[a-z]?)")
RES   = re.compile(r"outFilterMultimapNmax\s*(\d+)")
MITO  = re.compile(r"sjdbOverhang\s*(\d+)")
LFC   = re.compile(r"(\d{1,3}(?:\.\d+)?)\s?%[^.;]{0,30}?uniquely (?:mapped|aligned)|uniquely (?:mapped|aligned)[^.;]{0,40}?(\d{1,3}(?:\.\d+)?)\s?%", re.I)
KWIN  = re.compile(r"\bSTAR\b")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major != 2: return None
    return "2.%d" % minor

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
        "multimap_nmax": sorted(set(RES.findall(text))),
        "sjdb_overhang": sorted(set(MITO.findall(text))),
        "unique_rate_pct": sorted({a or b for a, b in LFC.findall(text)}),
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
res, mito, lfc = Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for r in c["multimap_nmax"]: res[r] += 1
    for m in c["sjdb_overhang"]: mito[m] += 1
    for l in c["unique_rate_pct"]: lfc[l] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\noutFilterMultimapNmax:", dict(res.most_common(10)))
print("sjdbOverhang:", dict(mito.most_common(10)))
print("unique mapping rate %:", dict(lfc.most_common(8)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
