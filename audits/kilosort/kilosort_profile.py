#!/usr/bin/env python3
"""Profile how each cohort paper used Kilosort."""
import csv, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 "KS1 (2016)":            r"[Kk]ilo[Ss]ort ?1\b|[Kk]ilo[Ss]ort[^.]{0,15}(?:Pachitariu|2016)",
 "KS2":                   r"[Kk]ilo[Ss]ort ?2(?!\.5)\b|[Kk]ilo[Ss]ort2(?!\.5)",
 "KS2.5":                 r"[Kk]ilo[Ss]ort ?2\.5|[Kk]ilo[Ss]ort2\.5",
 "KS3":                   r"[Kk]ilo[Ss]ort ?3\b|[Kk]ilo[Ss]ort3",
 "KS4":                   r"[Kk]ilo[Ss]ort ?4\b|[Kk]ilo[Ss]ort4",
 "Neuropixels":           r"[Nn]europixels?",
 "Neuropixels 2.0":       r"[Nn]europixels? 2\.0|NP ?2\.0",
 "tetrode/other probe":   r"tetrode|stereotrode|[Uu]tah array|silicon probe",
 "Phy manual curation":   r"\bphy\b|[Pp]hy2|manual(?:ly)? curat",
 "SpikeInterface":        r"[Ss]pike[Ii]nterface",
 "quality metrics":       r"ISI violation|refractory (?:period )?violation|amplitude cutoff|presence ratio|quality metric|[Bb]ombcell",
 "drift correction noted":r"drift correction|motion correction[^.]{0,40}(?:probe|electrode)|[Kk]ilosort[^.]{0,60}drift",
 "single/multi-unit criteria": r"(?:single|well[- ]isolated) unit|multi[- ]?unit|\bSUA\b|\bMUA\b",
 "acute / chronic":       r"chronic(?:ally)? implant|acute(?:ly)? (?:record|insert)",
 "CatGT/TPrime (SpikeGLX)": r"CatGT|TPrime|SpikeGLX",
 "Open Ephys":            r"Open ?Ephys",
 "waveform amplitude analysis": r"spike amplitude|waveform amplitude|amplitude of (?:the )?spike",
 "cell-type classification":    r"(?:putative|classified)[^.]{0,60}(?:interneuron|pyramidal|fast[- ]spiking)|cell[- ]type classif",
}
FEATURES = {k: re.compile(v) for k, v in FEATURES.items()}
VER = re.compile(r"[Kk]ilo[Ss]ort[^.;(]{0,20}?(?:v(?:ersion)?\.?\s*)?(\d+(?:\.\d+)*)")
KWIN = re.compile(r"[Kk]ilo[Ss]ort")

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
        if row["package"] == "Kilosort":
            cohort.append({"pmcid": row["pmcid"], "doi": row["doi"],
                           "journal": row["journal"], "year": row["year"],
                           "version_survey": row["version"],
                           "evidence_survey": row["evidence_sentence"]})
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("kilosort_profiles.jsonl", "w") as fh:
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
