#!/usr/bin/env python3
"""Profile how each cohort paper used IQ-TREE.

Mines the full text for the choices that select IQ-TREE code paths:
ModelFinder (-m MFP/TEST), ultrafast bootstrap (-bb/-B) and replicate counts,
-bnni, SH-aLRT/aBayes/parametric aLRT, partition models, named substitution and
rate models (+G/+I/+R/+F/+ASC), concordance factors, constraint trees, topology
tests, seeds/threads, co-used tools, and the stated IQ-TREE version. One JSONL
record per paper.

Usage: python3 iqtree_profile.py            (fetch full texts, cache fallback)
       python3 iqtree_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the IQ-TREE evidence
                 sentence in paper_software.tsv plus every per-package
                 evidence snippet in pipelines.jsonl.gz. A few hundred
                 characters per package, so feature counts from this source
                 are LOWER BOUNDS on usage, not measurements of it.

As for the Seurat audit, the 2026-09-02 run had no route to Europe PMC (www.ebi.ac.uk denied by the
session's egress policy; NCBI likewise), so every record in
iqtree_profiles.jsonl is source=survey_cache. Rerun from a host with Europe
PMC access to replace them; the fetch path is unchanged from the other audits.
Version regexes require "IQ-TREE"/"IQTREE" not followed by a letter.
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

# Case-sensitive unless listed in CI below; model names (GTR, LG, +G, +R) and
# option flags (-bb, -B, -alrt) are case-significant and matching them exactly is the point.
FEATURES = {
 "ModelFinder / -m MFP / -m TEST":      r"ModelFinder|-m\s*(?:MFP|MF|TEST|TESTONLY|TESTNEW|MF\+MERGE|MFP\+MERGE)\b|best[- ]fit(?:ting)? (?:substitution )?model",
 "MFP+MERGE / partition merging":       r"MERGE|PartitionFinder|merg(?:e|ing) partitions?",
 "ultrafast bootstrap (UFBoot)":        r"UFBoot|ultra-?fast bootstrap|-bb\s*\d|-B\s*\d|--ufboot|UFB\b",
 "UFBoot replicates 1000":              r"(?:-bb|-B|--ufboot)\s*1,?000\b|1,?000 (?:ultra-?fast |UF)?bootstrap|1,?000 (?:UFBoot )?replicates|1,?000 iterations",
 "UFBoot replicates 10000":             r"(?:-bb|-B)\s*10,?000\b|10,?000 (?:ultra-?fast |UF)?bootstrap|10,?000 replicates",
 "-bnni refinement":                    r"-bnni|bnni",
 "standard nonparametric bootstrap (-b)": r"(?<![-\w])-b\s+\d|non-?parametric bootstrap|standard bootstrap|Felsenstein bootstrap",
 "SH-aLRT (-alrt)":                     r"SH-?aLRT|-alrt\s*\d|SH-like|approximate likelihood[- ]ratio",
 "SH-aLRT replicates 1000":             r"-alrt\s*1,?000|1,?000 SH-?aLRT|SH-?aLRT[^.]{0,40}1,?000",
 "aBayes":                              r"aBayes|-abayes",
 "parametric aLRT (-alrt 0)":           r"-alrt\s*0\b",
 "partition model (-p/-q/-spp/-Q)":     r"(?<![-\w])-(?:p|q|Q|spp|sp)\s+\S|partition(?:ed|ing)? (?:model|scheme|by|analysis)|edge-?(?:linked|unlinked)|partitioned",
 "model named GTR":                     r"\bGTR\b",
 "model named HKY/K2P/TN":              r"\bHKY\b|\bK2P\b|\bK80\b|\bTN93\b|\bTIM\b|\bTVM\b",
 "protein matrix named (LG/JTT/WAG etc.)": r"\bLG\b|\bJTT\b|\bWAG\b|\bDayhoff\b|\bmtREV\b|\bcpREV\b|\bQ\.(?:pfam|insect|plant|yeast|bird|mammal)\b|\bPMB\b|\bVT\b|\bBlosum62\b",
 "+G (discrete gamma)":                 r"\+\s?G\d?\b|gamma(?:-distributed)? rate|\+\s?Γ",
 "+I (invariable sites)":               r"\+\s?I\b|invariant sites|invariable sites",
 "+R (FreeRate)":                       r"\+\s?R\d+\b|FreeRate|free-?rate",
 "+F (empirical frequencies)":          r"\+\s?F[O]?\b|empirical (?:base|amino acid|state) frequenc",
 "+ASC (ascertainment bias)":           r"\+\s?ASC\b|ascertainment[- ]bias",
 "protein mixture (C10-C60/LG4X/EX/PMSF)": r"\bC[1-6]0\b|LG4[XM]|\bEX\d|\bEHO\b|PMSF|profile mixture",
 "gCF/sCF concordance factors":         r"\bgCF\b|\bsCF\b|concordance factor|--gcf|--scf",
 "constraint tree (-g)":                r"(?<![-\w])-g\s+\S|constraint tree|topological constraint",
 "tree topology tests (AU/SH/KH)":      r"\bAU test\b|approximately unbiased|Shimodaira|-zb\s*\d|-au\b|\bKH test\b",
 "seed stated":                         r"-seed\s*\d|--seed\s*\d|random seed",
 "threads stated":                      r"-nt\s*(?:\d+|AUTO)|-T\s*(?:\d+|AUTO)|--threads",
 "coalescent / ASTRAL also used":       r"ASTRAL|species tree|coalescent",
 "RAxML also used":                     r"RAxML",
 "MrBayes / BEAST also used":           r"MrBayes|BEAST",
 "MAFFT / MUSCLE alignment":            r"MAFFT|MUSCLE|Clustal|PRANK",
 "trimming (trimAl/ClipKIT/Gblocks/BMGE)": r"trimAl|ClipKIT|Gblocks|BMGE",
 "concatenation / supermatrix":         r"concatenat|supermatrix|super-matrix",
 "dating / LSD2 / MCMCtree":            r"LSD2|--date|MCMCtree|molecular clock|divergence time",
 "AliSim simulation":                   r"AliSim|--alisim",
 "SARS-CoV-2 / viral genomes":          r"SARS-CoV-2|coronavirus|viral genome|virus genome|HIV",
 "IQ-TREE version stated":              r"IQ-?TREE(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "IQ-TREE 1.x named":                   r"IQ-?TREE(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?1\.\d",
 "IQ-TREE 2 named":                     r"IQ-?TREE\s?2\b|IQ-?TREE(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?2\.\d",
 "IQ-TREE 3 named":                     r"IQ-?TREE\s?3\b|IQ-?TREE(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?3\.\d",
 "web server (CIPRES/IQ-TREE web)":     r"CIPRES|web ?server|iqtree\.cibiv|phylo\.org",
}
CI = {"ModelFinder / -m MFP / -m TEST", "ultrafast bootstrap (UFBoot)", "UFBoot replicates 1000",
      "UFBoot replicates 10000", "standard nonparametric bootstrap (-b)", "SH-aLRT (-alrt)",
      "SH-aLRT replicates 1000", "aBayes", "partition model (-p/-q/-spp/-Q)", "+G (discrete gamma)",
      "+I (invariable sites)", "+R (FreeRate)", "+ASC (ascertainment bias)", "gCF/sCF concordance factors",
      "constraint tree (-g)", "tree topology tests (AU/SH/KH)", "seed stated", "coalescent / ASTRAL also used",
      "MAFFT / MUSCLE alignment", "concatenation / supermatrix", "dating / LSD2 / MCMCtree",
      "SARS-CoV-2 / viral genomes", "web server (CIPRES/IQ-TREE web)", "MFP+MERGE / partition merging"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"IQ-?TREE(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*[a-z]?)", re.I)
UFB   = re.compile(r"(?:-bb|-B|--ufboot|(?<![\w-])-b)\s+(\d[\d,]{2,})|(\d[\d,]{2,})\s*(?:ultra-?fast |UF)?bootstrap", re.I)
ALRT  = re.compile(r"-alrt\s*(\d[\d,]*)|(\d[\d,]{2,})\s*SH-?aLRT", re.I)
MODEL = re.compile(r"\b((?:GTR|HKY|K2P|K80|TN93|TIM\d?e?|TVM|SYM|F81|JC|LG|JTT|WAG|Dayhoff|mtREV|cpREV|Q\.[a-z]+|C[1-6]0|LG4X|LG4M|MFP|MF|TEST|PMSF|GTR20)(?:\s?\+\s?(?:F[O]?|G\d?|I|R\d+|ASC|MERGE))*)\b")
THREADS = re.compile(r"(?:-nt|-T)\s*(\d+|AUTO)", re.I)
KWIN  = re.compile(r"IQ-?TREE(?![A-Za-z])", re.I)

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major not in (1, 2, 3): return None   # IQ-TREE 1.x, 2.x, 3.x
    return "%d.%d" % (major, minor)

def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = set(VER.findall(text))
    if c.get("version_survey"):           # the survey's own full-text extraction
        vers.add(c["version_survey"])
    vers  = sorted(vers)
    fams  = sorted({f for f in (family(v) for v in vers) if f})
    def _nums(rx):
        out = set()
        for m in rx.finditer(text):
            g = m.group(1) or m.group(2)
            if g: out.add(int(g.replace(",", "")))
        return sorted(out)
    c.update({
        "source": source,
        "features": feats,
        "versions_all": vers,
        "version_family": fams,
        "ufboot_replicates": _nums(UFB),
        "alrt_replicates": _nums(ALRT),
        "models_named": sorted(set(m.group(1).replace(" ", "") for m in MODEL.finditer(text))),
        "threads": sorted(set(THREADS.findall(text))),
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
        if row["package"] == "IQ-TREE":
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
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "IQ-TREE")
        # Evidence snippets only. The pipeline_stages strings are structured
        # lists ("stage [PkgA v1.2, Seurat, PkgB v0.4.5]") in which another
        # package's version sits within a few characters of "Seurat".
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("iqtree_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co = Counter(), Counter(), Counter(), Counter()
ufb, alrt, models, thr = Counter(), Counter(), Counter(), Counter()
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for r in c["ufboot_replicates"]: ufb[r] += 1
    for r in c["alrt_replicates"]: alrt[r] += 1
    for m in c["models_named"]: models[m] += 1
    for t in c["threads"]: thr[t] += 1
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 25):", dict(vc.most_common(25)))
print("\nUFBoot replicate counts:", dict(ufb.most_common(10)))
print("SH-aLRT replicate counts:", dict(alrt.most_common(10)))
print("models named (top 30):", dict(models.most_common(30)))
print("threads:", dict(thr.most_common(10)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
