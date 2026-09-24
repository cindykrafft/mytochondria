#!/usr/bin/env python3
"""Profile how each cohort paper used Bowtie 2.
Mines the text for the choices that select Bowtie 2 code paths: alignment mode
(--local / --end-to-end / the presets), paired-end use, -X/--maxins, -I,
--no-mixed / --no-discordant, -k / -a, trimming options, the MAPQ threshold
or XS-based "unique" filter applied afterwards, the assay (ATAC, ChIP, CUT&RUN,
Hi-C, RNA, metagenomics, bisulfite via Bismark), the numbers reported
(alignment rate, fragment/insert size) and the stated version. One JSONL record
per paper.
Usage: python3 bowtie2_profile.py            (fetch full texts, cache fallback)
       python3 bowtie2_profile.py --offline  (survey cache only, no network)
Two sources, recorded per paper in `source`: "fulltext" (Europe PMC JATS body)
or "survey_cache" (the survey's stored evidence sentences; a few hundred
characters per package, so feature counts are LOWER BOUNDS).
As for the earlier audits, the 2026-09-24 run had no route to Europe PMC from
this session, so every record in bowtie2_profiles.jsonl is source=survey_cache.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below.
FEATURES = {
 "Bowtie 2 named":                        r"[Bb]owtie ?2|bowtie2",
 "paired-end":                            r"paired[- ]end|\bPE\b|-1 .{0,60}-2 |mate",
 "--local / local presets":               r"--local|sensitive-local|--fast-local|local alignment|local mode",
 "--end-to-end / e2e presets":            r"--end-to-end|end-to-end|--very-sensitive(?!-local)|--sensitive(?!-local)|--very-fast(?!-local)",
 "--very-sensitive (either)":             r"very-sensitive",
 "-X / --maxins stated":                  r"(?:^|[\s(,;])-X ?\d+|--maxins|maxins|-X ?2000|X2000",
 "-I / --minins stated":                  r"(?:^|[\s(,;])-I ?\d+|--minins",
 "--no-mixed":                            r"--no-mixed|no-mixed",
 "--no-discordant":                       r"--no-discordant|no-discordant",
 "--dovetail":                            r"--dovetail|dovetail",
 "-k / -a multi-reporting":               r"(?:^|[\s(,;])-k ?\d+|--all\b|(?:^|[\s(,;])-a\b",
 "trimming inside bowtie2 (-3/-5/--trim-to)": r"--trim5|--trim3|--trim-to|(?:^|[\s(,;])-[35] ?\d+",
 "-N / -L / seed options":                r"(?:^|[\s(,;])-N ?[01]\b|(?:^|[\s(,;])-L ?\d+|--seed",
 "-p threads":                            r"(?:^|[\s(,;])-p ?\d+|--threads",
 "MAPQ threshold applied":                r"MAPQ|mapping quality|(?:^|[\s(,;])-q ?\d+",
 "XS-tag / 'uniquely mapped' filter":     r"XS:i|XS tag|uniquely (?:mapped|aligned|mapping|aligning)|unique(?:ly)?[- ]mapp|multi-?mapp",
 "alignment rate reported":               r"(?:alignment|mapping) rate|% (?:of (?:the )?reads )?(?:mapped|aligned)|overall alignment",
 "fragment / insert size reported":       r"fragment[- ](?:size|length)|insert[- ]size|TLEN|template length",
 "ATAC-seq":                              r"ATAC",
 "ChIP-seq":                              r"ChIP",
 "CUT&RUN / CUT&Tag":                     r"CUT&RUN|CUT&Tag|CUT and RUN|CUT and Tag",
 "Hi-C / HiChIP / Micro-C":               r"Hi-?C\b|HiChIP|Micro-C|HiCUP|HiC-Pro",
 "RNA-seq / small RNA":                   r"RNA-?seq|transcriptom|small RNA|miRNA|ribosome profiling|Ribo-seq",
 "bisulfite (Bismark)":                   r"Bismark|bisulfite|WGBS|RRBS",
 "metagenomics / host removal / decontamination": r"metagenom|host (?:read )?(?:removal|depletion|filtering)|decontaminat|microbiome|16S",
 "CRISPR screen / sgRNA counting":        r"CRISPR|sgRNA|guide RNA|MAGeCK",
 "variant calling":                       r"variant call|GATK|HaplotypeCaller|freebayes|bcftools call|Mutect|VarScan|indel",
 "Picard / MarkDuplicates also used":     r"[Pp]icard|MarkDuplicates",
 "samtools also used":                    r"[Ss][Aa][Mm][Tt]ools",
 "MACS2 also used":                       r"MACS ?2|MACS3",
 "deepTools also used":                   r"deep[Tt]ools|bamCoverage|bamCompare",
 "Bowtie 2 version stated":               r"[Bb]owtie ?2(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
}
CI = {"paired-end", "MAPQ threshold applied", "XS-tag / 'uniquely mapped' filter", "alignment rate reported", "fragment / insert size reported",
      "ChIP-seq", "RNA-seq / small RNA", "bisulfite (Bismark)", "metagenomics / host removal / decontamination", "variant calling", "--local / local presets", "--end-to-end / e2e presets"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"[Bb]owtie ?2(?![A-Za-z])[^.;(]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
RES   = re.compile(r"MAPQ\s*(?:>=?|≥|of|above|greater than|at least|>)\s*(\d+)|mapping quality\s*(?:>=?|≥|of|above|greater than|at least|threshold(?: of)?|>|score(?: of)?)\s*(\d+)|(?:^|[\s(,;])-q ?(\d+)", re.I)
MITO  = re.compile(r"(?:^|[\s(,;])-X ?(\d+)|--maxins[ =](\d+)|maxins[ =:]?(\d+)", re.I)
PADJ  = re.compile(r"(?:^|[\s(,;])-I ?(\d+)|--minins[ =](\d+)", re.I)
LFC   = re.compile(r"(?:alignment|mapping) rate[^.;]{0,25}?(\d{1,3}(?:\.\d+)?)\s?%|(\d{1,3}(?:\.\d+)?)\s?% (?:of (?:the )?reads )?(?:mapped|aligned)", re.I)
DIMS  = re.compile(r"(?:fragment|insert)[- ](?:size|length)[^.;]{0,40}?(\d{2,4})\s?(?:bp|nt|base)", re.I)
KWIN  = re.compile(r"[Bb]owtie ?2(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major != 2: return None
    return "2.%d.x" % minor

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
        "maxins_X": sorted({a or b or c for a, b, c in MITO.findall(text)}),
        "minins_I": sorted({a or b for a, b in PADJ.findall(text)}),
        "mapping_rate_pct": sorted({a or b for a, b in LFC.findall(text)}),
        "fragment_sizes": sorted({int(d) for d in DIMS.findall(text) if 20 <= int(d) <= 5000}),
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
        if row["package"] == "Bowtie2":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "Bowtie2")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Bowtie2".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("bowtie2_profiles.jsonl", "w") as fh:
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
    for m in c["maxins_X"]: mito[m] += 1
    for p in c["minins_I"]: padj[p] += 1
    for l in c["mapping_rate_pct"]: lfc[l] += 1
    for d in c["fragment_sizes"]: dims[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nMAPQ thresholds:", dict(res.most_common(10)))
print("-X values:", dict(mito.most_common(10)))
print("-I values:", dict(padj.most_common(8)))
print("mapping rate %:", dict(lfc.most_common(8)))
print("fragment / insert sizes (bp):", dict(dims.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
