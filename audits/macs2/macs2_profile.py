#!/usr/bin/env python3
"""Profile how each cohort paper used MACS2/MACS3."""
import csv, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 # data type
 "ATAC-seq":            r"ATAC[- ]seq|assay for transposase",
 "ChIP-seq":            r"ChIP[- ]seq|chromatin immunoprecipitation",
 "CUT&RUN / CUT&Tag":   r"CUT\s*&\s*(?:RUN|Tag)|CUT&RUN|CUT&Tag|CUTandRUN",
 "scATAC":              r"scATAC|single[- ]cell ATAC|snATAC",
 # invocation modes
 "callpeak named":      r"callpeak",
 "broad peaks":         r"--?broad\b|broad[- ]peak",
 "narrow peaks":        r"narrow[- ]?[Pp]eak",
 "nomodel":             r"--?nomodel|no[- ]model",
 "shift/extsize set":   r"--?extsize|--?shift\b",
 "paired-end (BAMPE)":  r"BAMPE|--?format BAMPE|paired[- ]end mode",
 "no control/input":    r"without (?:a )?(?:control|input)|no (?:control|input) (?:sample|library|was)",
 "control/input used":  r"(?:input|control)[^.]{0,60}(?:MACS|peak call)|MACS[^.]{0,80}(?:input|control)",
 "genome size set":     r"-g\s*(?:hs|mm|ce|dm)|--?gsize|effective genome",
 "keep-dup":            r"--?keep-?dup",
 "summits":             r"--?call-?summits|summit",
 # thresholds
 "q-value cutoff":      r"(?:q[- ]?value|FDR)[^.;]{0,30}[<≤]?\s*0?\.\d+[^.;]{0,40}(?:MACS|peak)|MACS[^.;]{0,80}(?:q[- ]?value|FDR)",
 "p-value cutoff":      r"MACS[^.;]{0,80}p[- ]?value|p[- ]?value[^.;]{0,60}MACS",
 # downstream
 "DiffBind":            r"DiffBind",
 "DESeq2/edgeR on peaks": r"(?:DESeq2?|edgeR)[^.]{0,140}(?:peak|accessib|consensus)|(?:peak|accessib|consensus)[^.]{0,140}(?:DESeq2?|edgeR)",
 "IDR":                 r"\bIDR\b|irreproducib",
 "HOMER/motif":         r"HOMER|motif enrich",
 "ENCODE pipeline":     r"ENCODE[^.]{0,60}pipeline|encode[- ]dcc",
 "bedtools merge/consensus": r"consensus peak|merged? peak|union of peak",
 "MACS3 named":         r"MACS\s*3|macs3",
 "MACS1 (1.4)":         r"MACS\s*(?:v(?:ersion)?\.?\s*)?1\.4|MACS\s*1\b",
}
FEATURES = {k: re.compile(v) for k, v in FEATURES.items()}
VER = re.compile(r"MACS2?3?[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*(?:\.\d+)?)")
MWIN = re.compile(r"MACS")

def profile(c):
    raw, why = E.fetch(c["pmcid"])
    if not raw:
        c["profile_error"] = why; return c
    try:
        root = ET.fromstring(raw)
    except Exception:
        c["profile_error"] = "parse"; return c
    E._strip_refs(root)
    body = root.find(".//body")
    text = re.sub(r"\s+", " ", " ".join(body.itertext())) if body is not None else ""
    if not text:
        c["profile_error"] = "empty_body"; return c
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = sorted(set(VER.findall(text)))
    ctx = []
    for m in MWIN.finditer(text):
        lo = max(0, m.start()-260); hi = min(len(text), m.end()+320)
        ctx.append(("..."+text[lo:hi]+"...").strip())
        if len(ctx) >= 3: break
    c.update({"features": feats, "versions_all": vers, "context": ctx})
    return c

cohort = []
with open("../../survey/data/paper_software.tsv") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["package"] == "MACS2":
            cohort.append({"pmcid": row["pmcid"], "doi": row["doi"],
                           "journal": row["journal"], "year": row["year"],
                           "version_survey": row["version"],
                           "evidence_survey": row["evidence_sentence"]})
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("macs2_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
ok = [c for c in out if "profile_error" not in c]
print("profiled %d/%d" % (len(ok), len(out)))
from collections import Counter
fc, vc = Counter(), Counter()
for c in ok:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
print("\nFEATURES (papers):")
for k, n in fc.most_common(): print("  %-28s %d" % (k, n))
print("\nVERSIONS (top 15):", dict(vc.most_common(15)))
