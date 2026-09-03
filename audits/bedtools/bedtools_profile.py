#!/usr/bin/env python3
"""Profile how each cohort paper used BEDTools.

Mines the full text for the choices that select BEDTools code paths: which
sub-commands (intersect, merge, coverage, genomecov, closest, shuffle, fisher, jaccard,
multicov, map, slop/flank, subtract, window, ...), the options that change numbers
(-split, -f/-F/-r/-e, -s/-S, -c/-u/-v, -d, -pct, -incl/-excl), companion tools
(pybedtools, deepTools, bedops, MACS, samtools), and the stated BEDTools version.
One JSONL record per paper.

Usage: python3 bedtools_profile.py            (fetch full texts, cache fallback)
       python3 bedtools_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the BEDTools evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat, Scanpy and Cutadapt audits, the 2026-09-03 run had no route to
Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI likewise), so
every record in bedtools_profiles.jsonl is source=survey_cache. Rerun from a host with
Europe PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes accept "BEDTools", "bedtools", "BEDtools" and the classic
"intersectBed"-style names followed by a 2.x version.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-insensitive throughout: BEDTools sub-commands are lowercase words that also
# appear capitalised in prose; the classic CamelCase names (intersectBed) are listed too.
FEATURES = {
 "intersect":                          r"\bintersect(?:Bed)?\b|bedtools intersect|intersection[^.]{0,40}bedtools|bedtools[^.]{0,40}intersect",
 "merge":                              r"bedtools merge|\bmergeBed\b|merge(?:d)?[^.]{0,30}(?:with |using )bedtools|bedtools[^.]{0,30}merge",
 "coverage":                           r"bedtools coverage|\bcoverageBed\b|bedtools[^.]{0,30}coverage",
 "genomecov":                          r"genomecov|genomeCoverageBed",
 "closest":                            r"bedtools closest|\bclosestBed\b|closest[^.]{0,40}bedtools|bedtools[^.]{0,40}closest",
 "shuffle":                            r"bedtools shuffle|\bshuffleBed\b|shuffl[^.]{0,40}bedtools|bedtools[^.]{0,40}shuffl",
 "fisher":                             r"bedtools fisher|fisher[^.]{0,40}bedtools|bedtools[^.]{0,40}fisher",
 "jaccard":                            r"jaccard",
 "reldist":                            r"reldist|relative distance",
 "multicov":                           r"multicov|multiBamCov",
 "map":                                r"bedtools map\b|\bmapBed\b",
 "slop / flank":                       r"bedtools slop|\bslopBed\b|bedtools flank|\bflankBed\b",
 "subtract":                           r"bedtools subtract|\bsubtractBed\b|bedtools[^.]{0,30}subtract",
 "window":                             r"bedtools window|\bwindowBed\b",
 "makewindows":                        r"makewindows|windowMaker",
 "bamtobed / bedtobam":                r"bamtobed|bamToBed|bedtobam|bedToBam",
 "getfasta / nuc":                     r"getfasta|fastaFromBed|bedtools nuc|\bnucBed\b",
 "sort":                               r"bedtools sort|\bsortBed\b",
 "complement":                         r"bedtools complement|complementBed",
 "groupby":                            r"groupby|groupBy",
 "cluster":                            r"bedtools cluster|clusterBed",
 "random":                             r"bedtools random|randomBed",
 "-split named":                       r"-split\b",
 "-f / -F / -r / -e fraction named":   r"\s-[fF]\s+0?\.\d+|\s-r\b[^.]{0,20}(?:reciprocal|fraction)|reciprocal overlap|minimum overlap (?:fraction|of)",
 "-s / -S strand named":               r"\s-[sS]\b[^.]{0,30}strand|strand[- ]specific[^.]{0,30}bedtools|same strand",
 "-c / -u / -v named":                 r"\s-c\b|\s-u\b|\s-v\b|-wa\b|-wb\b|-wo\b|-wao\b|-loj\b",
 "-d distance named":                  r"\s-d\s+\d+|\bmerge[^.]{0,30}(?:within|distance)[^.]{0,20}\d",
 "-pct named":                         r"-pct\b",
 "-incl / -excl / -noOverlapping":     r"-incl\b|-excl\b|-noOverlapping|-chrom\b",
 "-bg / -bga / -scale named":          r"-bga?\b|-scale\b|bedGraph",
 "-pc / -fs named":                    r"\s-pc\b|\s-fs\b",
 "overlap / intersection in prose":    r"overlap|intersect",
 "permutation / shuffled null":        r"permut|shuffl|random(?:ly|ised|ized) (?:intervals|regions|peaks|background)",
 "pybedtools":                         r"pybedtools",
 "deepTools":                          r"deeptools|bamCoverage|computeMatrix|multiBigwigSummary",
 "bedops":                             r"bedops|bedmap",
 "MACS":                               r"MACS2?3?",
 "samtools":                           r"samtools",
 "HOMER":                              r"\bHOMER\b",
 "GREAT / ChIPseeker / annotation":    r"\bGREAT\b|ChIPseeker|annotatePeaks",
 "ATAC / ChIP / CUT&RUN":              r"ATAC|ChIP|CUT&(?:RUN|Tag)",
 "RNA-seq":                            r"RNA-seq|RNAseq",
 "WGS / variants / SV":                r"whole[- ]genome sequencing|\bWGS\b|structural variant|\bCNV\b|\bVCF\b",
 "Hi-C / TAD":                         r"Hi-C|\bTADs?\b",
 "methylation / bisulfite":            r"methylat|bisulfite|\bWGBS\b",
 "bedtools version stated":            r"(?:BEDTools|bedtools|BEDtools)(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?2\.\d+",
}
CI = set(FEATURES)
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"(?:BEDTools|bedtools|BEDtools|intersectBed|mergeBed|coverageBed|genomeCoverageBed|closestBed)(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(2\.\d+(?:\.\d+)*)")
FRAC  = re.compile(r"\s-[fF]\s+(0?\.\d+|1\.0|1)\b")
DIST  = re.compile(r"\s-d\s+(\d+)\b")
WIN   = re.compile(r"\s-w\s+(\d+)\b")
SLOP  = re.compile(r"\s-b\s+(\d+)\b")
SUBS  = re.compile(r"bedtools\s+([a-z]+)\b")
KWIN  = re.compile(r"(?:BEDTools|bedtools|BEDtools)(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major != 2: return None          # bedtools has only had 2.x releases
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
        "fractions": sorted(set(FRAC.findall(text))),
        "distances": sorted({int(d) for d in DIST.findall(text)}),
        "windows": sorted({int(d) for d in WIN.findall(text)}),
        "slops": sorted({int(d) for d in SLOP.findall(text)}),
        "subcommands": sorted(set(SUBS.findall(text))),
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
        if row["package"] == "BEDTools":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "BEDTools")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, BEDTools, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "BEDTools".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("bedtools_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
frac, dist, win, slop, subs = Counter(), Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for r in c["fractions"]: frac[r] += 1
    for m in c["distances"]: dist[m] += 1
    for p in c["windows"]: win[p] += 1
    for l in c["slops"]: slop[l] += 1
    for d in c["subcommands"]: subs[d] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\n-f/-F fractions:", dict(frac.most_common(10)))
print("-d distances:", dict(dist.most_common(10)))
print("-w windows:", dict(win.most_common(8)))
print("-b slops:", dict(slop.most_common(8)))
print("'bedtools <sub>' named:", dict(subs.most_common(20)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
