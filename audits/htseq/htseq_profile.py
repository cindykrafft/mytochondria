#!/usr/bin/env python3
"""Profile how each cohort paper used HTSeq.

Mines the full text for the choices that select htseq-count code paths:
overlap mode (-m), --nonunique, strandedness (-s), -r pos/name, -a MAPQ
cutoff, -t/-i feature and attribute selection, paired-end data, the aligner
that produced the BAM (STAR/HISAT2/TopHat/BWA/Bowtie2 -- which decides whether
unmapped mates and NH tags are present), htseq-count-barcodes / htseq-qa use,
the downstream DE tool, and the stated HTSeq version. One JSONL record per
paper.

Usage: python3 htseq_profile.py            (fetch full texts, cache fallback)
       python3 htseq_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the HTSeq evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy and Cutadapt audits, the 2026-09-03 run had no route
to Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI
likewise), so every record in htseq_profiles.jsonl is source=survey_cache.
Rerun from a host with Europe PMC access to replace them; the fetch path is
unchanged from the other audits.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below (STAR, BWA, DESeq2 and the like are
# proper names; option spellings are matched case-insensitively).
FEATURES = {
 "htseq-count named":                  r"htseq[- _]?count(?![- ]barcodes)",
 "htseq-count-barcodes":               r"htseq[- _]?count[- _]barcodes",
 "htseq-qa":                           r"htseq[- _]?qa\b",
 "mode union":                         r"\bunion\b",
 "mode intersection-strict":           r"intersection[- _]strict",
 "mode intersection-nonempty":         r"intersection[- _]non-?empty",
 "--nonunique all":                    r"nonunique[= ]*all|non-?unique all",
 "--nonunique fraction":               r"nonunique[= ]*fraction",
 "--nonunique random":                 r"nonunique[= ]*random",
 "--nonunique none":                   r"nonunique[= ]*none",
 "stranded yes / -s yes":              r"stranded[= ]*yes|-s yes|strand-?specific|strand-aware",
 "stranded no / -s no":                r"stranded[= ]*no\b|-s no\b|unstranded|non-?strand",
 "stranded reverse / -s reverse":      r"stranded[= ]*reverse|-s reverse|reverse[- ]strand",
 "-r pos":                             r"-r pos|order[= ]*pos|position-?sorted|coordinate-?sorted",
 "-r name":                            r"-r name|order[= ]*name|name-?sorted|sorted by (?:read )?name",
 "-a / --minaqual stated":             r"minaqual|\bMAPQ\b|-a \d+",
 "-t / --type stated":                 r"--type|\b-t (?:exon|gene|CDS|transcript)|type[= ]*(?:exon|gene|CDS)",
 "-i / --idattr stated":               r"idattr|\b-i (?:gene_id|gene_name|ID|Parent|transcript_id)|gene_id|gene_name",
 "--secondary/--supplementary-alignments": r"secondary[- ]alignments|supplementary[- ]alignments",
 "-f bam":                             r"-f bam|format[= ]*bam",
 "paired-end":                         r"paired[- ]end|\bPE\b|read pairs|mates",
 "uniquely mapped / unique reads":     r"uniquely (?:mapped|aligned)|unique(?:ly)? (?:mapping|aligned)|unique reads",
 "STAR aligner":                       r"\bSTAR\b",
 "HISAT2 / TopHat":                    r"HISAT2?|TopHat",
 "BWA / Bowtie":                       r"\bBWA\b|Bowtie2?",
 "featureCounts also named":           r"featureCounts",
 "DESeq2 downstream":                  r"DESeq2?",
 "edgeR / limma downstream":           r"edgeR|limma",
 "TCGA / GDC HTSeq counts downloaded": r"TCGA|GDC|Xena|HTSeq-FPKM|HTSeq-Counts",
 "FPKM / TPM":                         r"FPKM|\bTPM\b",
 "GENCODE / Ensembl / RefSeq GTF":     r"GENCODE|Ensembl|RefSeq|\bGTF\b|\bGFF3?\b",
 "single-cell / 10x":                  r"single[- ]cell|10x|10X|Chromium|cellranger",
 "ribosome profiling / Ribo-seq":      r"Ribo-?seq|ribosome profiling",
 "ChIP/ATAC/CUT&RUN":                  r"ChIP|ATAC|CUT&(?:RUN|Tag)",
 "bacterial / CDS features":           r"\bCDS\b|prokaryot|bacteri",
 "HTSeq version stated":               r"HTSeq(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"htseq-count named", "htseq-count-barcodes", "htseq-qa", "mode union", "mode intersection-strict",
      "mode intersection-nonempty", "--nonunique all", "--nonunique fraction", "--nonunique random",
      "--nonunique none", "stranded yes / -s yes", "stranded no / -s no", "stranded reverse / -s reverse",
      "-r pos", "-r name", "-t / --type stated", "-f bam", "paired-end", "uniquely mapped / unique reads",
      "HISAT2 / TopHat", "GENCODE / Ensembl / RefSeq GTF", "single-cell / 10x", "ribosome profiling / Ribo-seq",
      "bacterial / CDS features"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"HTSeq(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*(?:p\d*)?)")
RES   = re.compile(r"resolution[^.;]{0,30}?(\d\.\d+)", re.I)
MAPQ  = re.compile(r"(?:minaqual|MAPQ|-a)\s*(?:=|of|>=|≥|>)?\s*(\d{1,3})")
MITO  = re.compile(r"(\d{1,2}(?:\.\d)?)\s*%[^.;]{0,40}?mitochondrial|mitochondrial[^.;]{0,60}?(\d{1,2}(?:\.\d)?)\s*%", re.I)
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|p_val_adj|padj|FDR|[qQ][- ]?value|Bonferroni)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
LFC   = re.compile(r"(?:logfc\.threshold|\|?\s*(?:avg_)?log2?\s*(?:fold[- ]?change|FC)\s*\|?|\bLFC\b|fold[- ]?change)[^.;]{0,30}?[>≥=]\s*(\d+(?:\.\d+)?)", re.I)
DIMS  = re.compile(r"(?:dims\s*=\s*1:|(?:first|top)\s+)(\d{1,3})\s*(?:PCs?|principal components|dimensions)?", re.I)
KWIN  = re.compile(r"HTSeq(?![A-Za-z])|htseq[- _]?count")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    return "%d.%d" % (major, minor)     # 0.5 ... 0.13, 1.99, 2.0, 2.1

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
        "resolutions": sorted(set(RES.findall(text))),
        "mapq_cutoffs": sorted(set(MAPQ.findall(text))),
        "padj_cutoffs": sorted(set(PADJ.findall(text))),
        "lfc_cutoffs": sorted(set(LFC.findall(text))),
        "dims": sorted({int(d) for d in DIMS.findall(text) if 0 < int(d) <= 200}),
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
        if row["package"] == "HTSeq":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "HTSeq")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("htseq_profiles.jsonl", "w") as fh:
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
    for r in c["resolutions"]: res[r] += 1
    for m in c["mapq_cutoffs"]: mito[m] += 1
    for p in c["padj_cutoffs"]: padj[p] += 1
    for l in c["lfc_cutoffs"]: lfc[l] += 1
    for d in c["dims"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nresolutions:", dict(res.most_common(10)))
print("MAPQ cutoffs:", dict(mito.most_common(10)))
print("padj cutoffs:", dict(padj.most_common(8)))
print("lfc cutoffs:", dict(lfc.most_common(8)))
print("dims:", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
