#!/usr/bin/env python3
"""Profile how each cohort paper used deepTools.

Mines the full text for the choices that select deepTools code paths: which
tool (bamCoverage, bamCompare, computeMatrix, plotHeatmap/plotProfile,
multiBamSummary/multiBigwigSummary, plotCorrelation, plotPCA, plotFingerprint,
...), the normalisation (RPKM/CPM/BPM/RPGC, --scaleFactor, SES), read
processing options (--extendReads, --ignoreDuplicates, --centerReads,
--MNase, --Offset, --smoothLength), the comparison operation, the matrix mode
and averaging, correlation method and outlier handling, and the stated
deepTools version. One JSONL record per paper.

Usage: python3 deeptools_profile.py            (fetch full texts, cache fallback)
       python3 deeptools_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the deepTools evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy and Cutadapt audits, the 2026-09-03 run had no route
to Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI
likewise), so every record in deeptools_profiles.jsonl is source=survey_cache.
Rerun from a host with Europe PMC access to replace them; the fetch path is
unchanged from the other audits. Version regexes require a word boundary after
"deepTools".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

PACKAGE = "deepTools"

# Tool names are CamelCase identifiers; matched case-insensitively because
# papers write them in running text as "bamcoverage" too.
FEATURES = {
 "bamCoverage":                          r"bamCoverage",
 "bamCompare":                           r"bamCompare",
 "bigwigCompare / bigwigAverage":        r"bigwigCompare|bigwigAverage",
 "computeMatrix":                        r"computeMatrix",
 "plotHeatmap":                          r"plotHeatmap",
 "plotProfile":                          r"plotProfile",
 "multiBamSummary":                      r"multiBamSummary",
 "multiBigwigSummary":                   r"multiBigwigSummary",
 "plotCorrelation":                      r"plotCorrelation",
 "plotPCA":                              r"plotPCA",
 "plotFingerprint":                      r"plotFingerprint",
 "bamPEFragmentSize":                    r"bamPEFragmentSize",
 "computeGCBias / correctGCBias":        r"computeGCBias|correctGCBias|GC[- ]bias correction",
 "alignmentSieve":                       r"alignmentSieve",
 "plotEnrichment / plotCoverage":        r"plotEnrichment|plotCoverage",
 "bigWig / coverage track produced":     r"bigwig|bigWig|coverage track|signal track|bedgraph",
 "RPKM normalisation":                   r"\bRPKM\b",
 "CPM normalisation":                    r"\bCPM\b|counts per million",
 "BPM normalisation":                    r"\bBPM\b|bins per million",
 "RPGC / 1x normalisation":              r"\bRPGC\b|1x (?:genome|coverage|normali[sz])|1[- ]?x normali[sz]|reads per genomic content|effectiveGenomeSize|effective genome size",
 "--normalizeUsing named":               r"normalizeUsing|normalize ?Using",
 "--scaleFactor / spike-in scaling":     r"scaleFactor|scale factor|spike[- ]?in",
 "SES scaling":                          r"\bSES\b|signal extraction scaling",
 "log2 ratio (bamCompare/bigwigCompare)": r"log2 ?ratio|log2\(?(?:ChIP|IP)[^)]{0,20}/|--operation|log2 fold[- ]?change of|log2 ?\((?:IP|ChIP|treatment)",
 "subtract operation":                   r"--operation subtract|subtract(?:ed|ing)? (?:the )?input",
 "input-normalised / ratio to input":    r"(?:normali[sz]ed|ratio|divided|relative) (?:to|by|over|against) (?:the )?(?:input|IgG|control)",
 "--extendReads":                        r"extendReads|extend(?:ed|ing)? (?:reads|fragments)|fragment[- ]length extension",
 "--ignoreDuplicates":                   r"ignoreDuplicates|(?:ignor|remov|exclud|discard|filter)\w* (?:PCR )?duplicates?",
 "--centerReads":                        r"centerReads|cent(?:er|re)d reads",
 "--MNase":                              r"--MNase|MNase(?:-| )?seq|nucleosome",
 "--Offset":                             r"--Offset|Offset [0-9]",
 "--smoothLength":                       r"smoothLength|smooth(?:ed|ing)? (?:window|length)",
 "--skipZeroOverZero / --skipNAs":       r"skipZeroOverZero|skipNAs|skipNonCoveredRegions",
 "--minMappingQuality / MAPQ filter":    r"minMappingQuality|MAPQ|mapping quality",
 "--binSize stated":                     r"binSize|bin size|bins? of \d+ ?bp|\d+ ?bp bins",
 "reference-point mode":                 r"reference-point|referencePoint|centered (?:on|at) (?:the )?(?:TSS|summit|peak cent)",
 "scale-regions mode":                   r"scale-regions|scaled? (?:to|regions)|gene body",
 "TSS / TES named":                      r"\bTSS\b|\bTES\b|transcription start site",
 "--averageType / --averageTypeBins":    r"averageType|averageTypeBins",
 "--missingDataAsZero / --skipZeros":    r"missingDataAsZero|skipZeros",
 "k-means / hierarchical clustering of heatmap": r"kmeans|k-means|hclust|hierarchical clustering",
 "--sortRegions / sorted heatmap":       r"sortRegions|sortUsing|sorted by (?:mean|median|max|signal)",
 "Pearson correlation":                  r"[Pp]earson",
 "Spearman correlation":                 r"[Ss]pearman",
 "--removeOutliers":                     r"removeOutliers",
 "PCA":                                  r"\bPCA\b|principal component",
 "plotPCA --log2 / --transpose / --ntop": r"--log2|--transpose|--ntop|rowCenter",
 "fingerprint / JSD / CHANCE":           r"fingerprint|Jensen[- ]Shannon|\bJSD\b|CHANCE",
 "fragment size / insert size":          r"fragment (?:size|length)|insert size",
 "GC bias":                              r"GC[- ]bias",
 "blacklist":                            r"blacklist|black list|ENCODE[- ]?black",
 "paired-end":                           r"paired[- ]end",
 "deepTools version stated":             r"[Dd]eep[Tt]ools(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "ChIP-seq":                             r"ChIP[- ]?seq|chromatin immunoprecipitation",
 "ATAC-seq":                             r"ATAC[- ]?seq",
 "CUT&RUN / CUT&Tag":                    r"CUT ?& ?(?:RUN|Tag)|CUT&amp;(?:RUN|Tag)|CUTRUN|CUTTag",
 "RNA-seq":                              r"RNA[- ]?seq",
 "Hi-C / 4C / HiChIP":                   r"Hi-?C|HiChIP|\b4C\b",
 "DNase / MNase / NOMe":                 r"DNase[- ]?seq|MNase[- ]?seq|\bNOMe\b",
 "MACS2 / MACS3 peak calling":           r"MACS ?[23]?",
 "Bowtie2 / BWA / STAR aligner":         r"[Bb]owtie ?2|\bBWA\b|\bSTAR\b",
 "IGV":                                  r"\bIGV\b|Integrative Genomics Viewer",
 "bedtools":                             r"[Bb]edtools|BEDTools",
 "Picard MarkDuplicates":                r"Picard|MarkDuplicates",
 "samtools":                             r"[Ss]amtools|SAMtools",
 "HOMER":                                r"\bHOMER\b",
 "Galaxy":                               r"\bGalaxy\b",
 "nf-core / Snakemake pipeline":         r"nf-core|Snakemake|snakePipes",
}
CI = {"bamCoverage", "bamCompare", "bigwigCompare / bigwigAverage", "computeMatrix", "plotHeatmap", "plotProfile",
      "multiBamSummary", "multiBigwigSummary", "plotCorrelation", "plotPCA", "plotFingerprint", "bamPEFragmentSize",
      "computeGCBias / correctGCBias", "alignmentSieve", "plotEnrichment / plotCoverage", "bigWig / coverage track produced",
      "CPM normalisation", "BPM normalisation", "RPGC / 1x normalisation", "--normalizeUsing named",
      "--scaleFactor / spike-in scaling", "log2 ratio (bamCompare/bigwigCompare)", "subtract operation",
      "input-normalised / ratio to input", "--extendReads", "--ignoreDuplicates", "--centerReads", "--smoothLength",
      "--minMappingQuality / MAPQ filter", "--binSize stated", "reference-point mode", "scale-regions mode",
      "--averageType / --averageTypeBins", "--missingDataAsZero / --skipZeros", "k-means / hierarchical clustering of heatmap",
      "--sortRegions / sorted heatmap", "PCA", "fingerprint / JSD / CHANCE", "fragment size / insert size", "GC bias",
      "blacklist", "paired-end", "ChIP-seq", "ATAC-seq", "RNA-seq", "MACS2 / MACS3 peak calling"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Dd]eep[Tt]ools(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
BIN   = re.compile(r"(?:binSize|bin size|bins? of|bin width)[^.;]{0,12}?(\d+)\s*(?:bp|base)", re.I)
BIN2  = re.compile(r"(\d+)[- ]?bp bins", re.I)
EXT   = re.compile(r"extend(?:ed|Reads)?[^.;]{0,25}?(\d{2,4})\s*(?:bp|base)", re.I)
SMOOTH = re.compile(r"smooth(?:Length|ed|ing)?[^.;]{0,25}?(\d{2,5})\s*(?:bp|base)", re.I)
EGS   = re.compile(r"effective ?genome ?size[^.;]{0,20}?(\d[\d,.e]{5,})", re.I)
UPDOWN = re.compile(r"(\d+(?:\.\d+)?)\s*(kb|bp)\s*(?:up|down)stream", re.I)
KWIN  = re.compile(r"[Dd]eep[Tt]ools(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major not in (2, 3): return None          # deepTools releases in the cohort years are 2.x / 3.x
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
        "bin_sizes": sorted({int(x) for x in BIN.findall(text) + BIN2.findall(text)}),
        "extend_bp": sorted({int(x) for x in EXT.findall(text)}),
        "smooth_bp": sorted({int(x) for x in SMOOTH.findall(text)}),
        "effective_genome_size": sorted(set(EGS.findall(text))),
        "flank": sorted({"%s %s" % (a, b.lower()) for a, b in UPDOWN.findall(text)}),
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
        if row["package"] == PACKAGE:
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != PACKAGE)
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, deepTools, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "deepTools".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("deeptools_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
bins, ext, smooth, egs, flank = Counter(), Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for b in c["bin_sizes"]: bins[b] += 1
    for e in c["extend_bp"]: ext[e] += 1
    for s in c["smooth_bp"]: smooth[s] += 1
    for g in c["effective_genome_size"]: egs[g] += 1
    for f in c["flank"]: flank[f] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nbin sizes:", dict(bins.most_common(10)))
print("extension lengths:", dict(ext.most_common(10)))
print("smooth lengths:", dict(smooth.most_common(8)))
print("effective genome sizes:", dict(egs.most_common(8)))
print("flanks:", dict(flank.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
