#!/usr/bin/env python3
"""Profile how each cohort paper used FieldTrip."""
import csv, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 "cluster-based permutation":  r"cluster[- ]based permutation|cluster[- ]?(?:level|mass|size)[^.]{0,60}permutation|permutation[^.]{0,60}cluster|nonparametric cluster|Maris (?:and|&) Oostenveld",
 "montecarlo/permutation stat":r"[Mm]onte ?[Cc]arlo|permutation test|randomi[sz]ation test|ft_statistics_montecarlo",
 "ft_freqstatistics":          r"ft_freqstatistics",
 "ft_timelockstatistics":      r"ft_timelockstatistics",
 "ft_sourcestatistics":        r"ft_sourcestatistics",
 "depsamplesT / indepsamplesT":r"depsamples|indepsamples|ft_statfun",
 "time-frequency (wavelet/multitaper)": r"multitaper|[Mm]orlet|wavelet|Hanning taper|ft_freqanalysis|mtmconvol|mtmfft|superlet",
 "ERP/ERF timelock":           r"ft_timelockanalysis|event[- ]related (?:potential|field)|\bERPs?\b|\bERFs?\b",
 "source reconstruction":      r"beamform|\bLCMV\b|\bDICS\b|minimum[- ]norm|\bMNE\b|\beLORETA\b|sLORETA|ft_sourceanalysis|source[- ]reconstruct|dipole fit",
 "connectivity":               r"ft_connectivityanalysis|coherence|phase[- ]locking value|\bPLV\b|Granger|imaginary (?:part of )?coherenc|weighted phase lag|\bwPLI\b|\bPLI\b|phase slope|\bPSI\b|debiased",
 "ICA artifact removal":       r"\bICA\b|independent component",
 "MEG":                        r"\bMEG\b|magnetoencephalogra",
 "EEG":                        r"\bEEG\b|electroencephalogra",
 "iEEG/ECoG/sEEG":             r"\biEEG\b|\bECoG\b|\bsEEG\b|intracranial|stereo[- ]?EEG",
 "LFP/animal ephys":           r"\bLFPs?\b|local field potential",
 "head model / forward":       r"ft_prepare_headmodel|ft_prepare_leadfield|boundary element|\bBEM\b|\bFEM\b|single[- ]shell|openmeeg|dipoli|simbio",
 "planar gradient":            r"planar gradient|ft_megplanar|synthetic planar",
 "baseline correction":        r"baseline[- ]correct|ft_freqbaseline|relative change|decibel",
 "phase-amplitude coupling":   r"phase[- ]amplitude coupling|\bPAC\b|modulation index",
 "decoding/MVPA":              r"\bMVPA\b|decoding|classifier|ft_statistics_mvpa|MVPA[- ]Light",
 "SPM also used":              r"\bSPM ?(?:8|12)?\b",
 "EEGLAB also used":           r"EEGLAB",
 "MNE also used":              r"MNE[- ]Python",
 "Brainstorm also used":       r"Brainstorm",
 "min cluster / neighbours":   r"minnbchan|neighbou?r(?:hood)? (?:structure|template|definition)|ft_prepare_neighbours",
 "alpha / two-sided":          r"cluster[- ]?alpha|two[- ](?:sided|tailed)|one[- ](?:sided|tailed)",
 "n permutations":             r"(?:\d[\d,]{2,}|1000|5000|10,?000) (?:random )?permutations|permutations? \(n ?= ?\d",
}
FEATURES = {k: re.compile(v) for k, v in FEATURES.items()}
VER = re.compile(r"[Ff]ield[Tt]rip[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(20\d{6}|\d{4}-\d{2}-\d{2}|\d+\.\d+(?:\.\d+)?)")
KWIN = re.compile(r"[Ff]ield[Tt]rip")

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
    # also capture the cluster-permutation sentence(s) for later adjudication
    cl = []
    for m in FEATURES["cluster-based permutation"].finditer(text):
        lo = max(0, m.start()-300); hi = min(len(text), m.end()+400)
        cl.append(("..."+text[lo:hi]+"...").strip())
        if len(cl) >= 2: break
    c.update({"features": feats, "versions_all": vers, "context": ctx, "cluster_context": cl})
    return c

cohort = []
with open("../../survey/data/paper_software.tsv") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["package"] == "FieldTrip":
            cohort.append({"pmcid": row["pmcid"], "doi": row["doi"],
                           "journal": row["journal"], "year": row["year"],
                           "version_survey": row["version"],
                           "evidence_survey": row["evidence_sentence"]})
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("fieldtrip_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
ok = [c for c in out if "profile_error" not in c]
print("profiled %d/%d" % (len(ok), len(out)))
from collections import Counter
fc, vc = Counter(), Counter()
for c in ok:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
print("\nFEATURES (papers):")
for k, n in fc.most_common(): print("  %-36s %d" % (k, n))
print("\nVERSIONS:", dict(vc.most_common(20)))
