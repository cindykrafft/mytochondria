#!/usr/bin/env python3
"""Profile which cohort papers used AlphaFold 3, and which parts of it.

The survey records the package as "AlphaFold" without distinguishing major
versions, so this re-reads each full text and keeps only papers that name
AlphaFold 3 / AF3 / the AlphaFold Server. It then records, per paper, which
AF3 features the text describes -- the code paths an audit finding would have
to travel to reach that paper's numbers -- and whether the run was local
(the open-source code audited here) or on the AlphaFold Server (same weights,
different genetic search; not this codebase).
"""
import csv, json, re, sys
import concurrent.futures as cf
import xml.etree.ElementTree as ET
sys.path.insert(0, "../../survey/scripts")
import extract as E

# A paper is in the AF3 cohort only if one of these appears.
AF3 = re.compile(
    r"AlphaFold[- ]?3\b|AlphaFold ?v?3\.\d|\bAF3\b|AlphaFold[- ]?Server|"
    r"alphafoldserver\.com|AlphaFold ?3 \(AF3\)")

# Local open-source install vs the hosted server.
LOCAL = re.compile(
    r"alphafold3 (?:repository|code|GitHub)|github\.com/google-deepmind/alphafold3|"
    r"run_alphafold\.py|locally installed AlphaFold ?3|local (?:install|copy|version) of AlphaFold ?3|"
    r"AlphaFold ?3 (?:was )?(?:installed|run) (?:locally|on our)")
SERVER = re.compile(r"AlphaFold[- ]?Server|alphafoldserver\.com")

FEATURES = {
 "protein-ligand complex":  r"AlphaFold ?3[^.]{0,120}ligand|ligand[^.]{0,120}AlphaFold ?3|"
                            r"\bAF3\b[^.]{0,120}(?:ligand|small molecule)|protein[- ]ligand[^.]{0,60}(?:AF3|AlphaFold ?3)",
 "SMILES ligand":           r"SMILES",
 "CCD code ligand":         r"\bCCD\b|Chemical Component Dictionary|userCCD",
 "nucleic acid (DNA/RNA)":  r"(?:AF3|AlphaFold ?3)[^.]{0,140}(?:\bDNA\b|\bRNA\b)|"
                            r"(?:\bDNA\b|\bRNA\b)[^.]{0,140}(?:AF3|AlphaFold ?3)",
 "post-translational mod.": r"phosphoryl|glycosyl|SUMOyl|acetylat|methylat|modified residue",
 "ion / cofactor":          r"(?:AF3|AlphaFold ?3)[^.]{0,140}(?:\bion\b|cofactor|\bZn\b|\bMg\b|heme|ATP|GTP|NAD)",
 "templates mentioned":     r"template",
 "custom / provided MSA":   r"custom MSA|user[- ]provided MSA|our own MSA|unpairedMsa|pairedMsa|precomputed MSA",
 "MSA depth discussed":     r"MSA depth|depth of the MSA|number of (?:effective )?sequences|Neff",
 "multiple seeds":          r"seed",
 "num. of predictions/samples": r"(?:AF3|AlphaFold ?3)[^.]{0,100}(?:\d+ (?:models|predictions|samples|structures))|"
                                r"(?:\d+ (?:models|predictions|samples|seeds))[^.]{0,100}(?:AF3|AlphaFold ?3)",
 "ipTM reported":           r"\bipTM\b|\biPTM\b|interface predicted TM",
 "pTM reported":            r"\bpTM\b|predicted TM[- ]score",
 "pLDDT reported":          r"pLDDT|predicted lDDT|predicted local distance",
 "PAE reported":            r"\bPAE\b|predicted aligned error",
 "ranking score":           r"ranking score|ranking_score|ranked_0|top[- ]ranked model",
 "confidence-based filtering": r"(?:pLDDT|ipTM|PAE|ranking score)[^.]{0,60}(?:cut[- ]?off|threshold|>|<|above|below)",
 "structure comparison (RMSD/TM)": r"\bRMSD\b|TM[- ]align|TM[- ]score|DockQ",
 "experimental validation":  r"cryo[- ]?EM|crystallograph|X[- ]ray structure|NMR structure|SAXS|crosslink",
 "molecular replacement":    r"molecular replacement|Phaser|PHENIX|MOLREP",
}
FEATURES = {k: re.compile(v, re.I) for k, v in FEATURES.items()}
VER = re.compile(r"AlphaFold[ -]?3[^.;(]{0,20}?(?:v(?:ersion)?\.?\s*)(\d+(?:\.\d+)*)")
WIN = re.compile(r"AlphaFold[- ]?3\b|\bAF3\b|AlphaFold[- ]?Server")


def profile(c):
    raw, why = E.fetch(c["pmcid"])
    if not raw:
        c["profile_error"] = why
        return c
    try:
        root = ET.fromstring(raw)
    except Exception:
        c["profile_error"] = "parse"
        return c
    E._strip_refs(root)
    body = root.find(".//body")
    text = re.sub(r"\s+", " ", " ".join(body.itertext())) if body is not None else ""
    if not text:
        c["profile_error"] = "empty_body"
        return c
    if not AF3.search(text):
        c["af3"] = False
        return c
    c["af3"] = True
    c["features"] = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    c["local"] = bool(LOCAL.search(text))
    c["server"] = bool(SERVER.search(text))
    c["versions"] = sorted(set(VER.findall(text)))
    ctx = []
    for m in WIN.finditer(text):
        lo, hi = max(0, m.start() - 250), min(len(text), m.end() + 320)
        ctx.append(("..." + text[lo:hi] + "...").strip())
        if len(ctx) >= 3:
            break
    c["context"] = ctx
    return c


cohort = []
with open("../../survey/data/paper_software.tsv") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["package"] == "AlphaFold":
            cohort.append({"pmcid": row["pmcid"], "doi": row["doi"],
                           "journal": row["journal"], "year": row["year"],
                           "version_survey": row["version"],
                           "evidence_survey": row["evidence_sentence"]})
seen, uniq = set(), []
for c in cohort:
    if c["pmcid"] in seen:
        continue
    seen.add(c["pmcid"])
    uniq.append(c)
cohort = [c for c in uniq if c["year"] >= "2024"]
print("AlphaFold papers (unique, 2024+):", len(cohort))

with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("af3_profiles.jsonl", "w") as fh:
    for c in out:
        fh.write(json.dumps(c) + "\n")

err = [c for c in out if "profile_error" in c]
ok = [c for c in out if "profile_error" not in c]
af3 = [c for c in ok if c.get("af3")]
print("re-read %d, unreadable %d, name AlphaFold 3/AF3/Server: %d" % (len(ok), len(err), len(af3)))
print("  local install described: %d | AlphaFold Server named: %d | server only: %d"
      % (sum(c["local"] for c in af3), sum(c["server"] for c in af3),
         sum(c["server"] and not c["local"] for c in af3)))
from collections import Counter
fc, jc, vc = Counter(), Counter(), Counter()
for c in af3:
    for f in c["features"]:
        fc[f] += 1
    jc[(c["journal"], c["year"])] += 1
    for v in c["versions"]:
        vc[v] += 1
print("\nFEATURES (papers):")
for k, n in fc.most_common():
    print("  %-34s %d" % (k, n))
print("\nJOURNAL/YEAR:", dict(sorted(jc.items())))
print("VERSIONS STATED:", dict(vc.most_common()))
