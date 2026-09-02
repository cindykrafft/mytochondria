#!/usr/bin/env python3
"""Profile how each cohort paper used Suite2p."""
import csv, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 "two-photon":              r"two[- ]photon|2[- ]photon|\b2P\b",
 "one-photon / miniscope":  r"one[- ]photon|miniscope|1[- ]photon|widefield",
 "GCaMP":                   r"GCaMP",
 "registration / motion correction": r"motion[- ]correct|registration|rigid|non-?rigid",
 "nonrigid registration":   r"non-?rigid",
 "ROI detection":           r"ROI(?:s)? (?:were |was )?(?:detect|extract|identif|segment)|cell detection|segmentation",
 "Cellpose in suite2p":     r"[Cc]ellpose",
 "anatomical (cellpose) mode": r"anatomical",
 "manual curation of ROIs": r"manually (?:curat|inspect|select|verif)|curated",
 "classifier / iscell":     r"classifier|iscell|probability of being a cell",
 "neuropil correction":     r"neuropil",
 "neuropil coefficient stated": r"neuropil[^.]{0,80}0\.7|0\.7[^.]{0,60}neuropil|coefficient of 0\.\d",
 "deconvolution (OASIS/spks)": r"deconvol|OASIS|\bspks\b|spike inference|inferred spike",
 "dF/F":                    r"\bdF/F|\u0394F/F|ΔF/F|delta ?F/F",
 "tau / decay constant":    r"\btau\b|decay (?:time )?constant|time constant",
 "z-stack / multiplane":    r"multi-?plane|z-?stack|volumetric|planes",
 "frame rate stated":       r"\d+(?:\.\d+)? ?Hz",
 "SNR / skew metrics":      r"skewness|signal-to-noise|\bSNR\b",
 "CaImAn also used":        r"CaImAn",
 "EXTRACT also used":       r"\bEXTRACT\b",
 "version stated":          r"[Ss]uite2[Pp][^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "MATLAB suite2p (old)":    r"[Ss]uite2[Pp][^.]{0,60}MATLAB|MATLAB[^.]{0,60}[Ss]uite2[Pp]",
 "spatial scale / diameter": r"diameter|spatial scale",
 "cross-day / longitudinal": r"longitudinal|across (?:days|sessions)|chronic",
}
FEATURES = {k: re.compile(v) for k, v in FEATURES.items()}
VER = re.compile(r"[Ss]uite2[Pp][^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
KWIN = re.compile(r"[Ss]uite2[Pp]")

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
    for m in KWIN.finditer(text):
        lo = max(0, m.start()-250); hi = min(len(text), m.end()+320)
        ctx.append(("..."+text[lo:hi]+"...").strip())
        if len(ctx) >= 3: break
    c.update({"features": feats, "versions_all": vers, "context": ctx})
    return c

cohort = []
with open("../../survey/data/paper_software.tsv") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["package"] == "Suite2p":
            cohort.append({"pmcid": row["pmcid"], "doi": row["doi"],
                           "journal": row["journal"], "year": row["year"],
                           "version_survey": row["version"],
                           "evidence_survey": row["evidence_sentence"]})
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("suite2p_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
ok = [c for c in out if "profile_error" not in c]
print("profiled %d/%d" % (len(ok), len(out)))
from collections import Counter
fc, vc = Counter(), Counter()
for c in ok:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
print("\nFEATURES (papers):")
for k, n in fc.most_common(): print("  %-32s %d" % (k, n))
print("\nVERSIONS:", dict(vc.most_common(15)))
