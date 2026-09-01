#!/usr/bin/env python3
"""Profile which parts of AFNI each cohort paper used.

Run from survey/scripts/ (it imports the survey's own extractor and fetcher):

    cd survey/scripts && python3 ../../audits/afni/afni_profile.py

Writes afni_profiles.jsonl next to the cohort file and prints the feature /
command / version tallies that the audit README quotes.
"""
import json, re, sys, os, xml.etree.ElementTree as ET
import concurrent.futures as cf
sys.path.insert(0, ".")
import extract as E

# AFNI ships ~600 programs; these are the ones that carry published numbers
# and the ones the audit's findings live in.
COMMANDS = [
 "afni_proc.py", "uber_subject.py", "align_epi_anat.py", "@SSwarper",
 "@animal_warper", "auto_warp.py", "@auto_tlrc", "3dSkullStrip",
 "3dvolreg", "3dTshift", "3dDespike", "3dWarp", "3dNwarpApply", "3dQwarp",
 "3dAllineate", "3dresample", "3dmerge", "3dBlurToFWHM", "3dBlurInMask",
 "3dDeconvolve", "3dREMLfit", "3dSynthesize", "3dTproject", "3dBandpass",
 "3dttest++", "3dttest", "3dMEMA", "3dMVM", "3dLME", "3dLMEr", "3dANOVA",
 "3dANOVA2", "3dANOVA3", "3dRegAna", "3dICC", "3dISC",
 "3dClustSim", "3dFWHMx", "3dClusterize", "3dclust", "3dXClustSim", "3dETAC",
 "3dReHo", "3dRSFC", "3dNetCorr", "3dTcorr1D", "3dTcorrMap", "3dGroupInCorr",
 "3dAmpToRSFC", "3dLFCD", "3dDegreeCentrality", "3dECM",
 "3dTstat", "3dROIstats", "3dmaskave", "3dBrickStat", "3dcalc", "3dmaskdump",
 "3dDWItoDT", "3dDTeig", "3dTrackID", "3dProbTrackID", "3dDWUncert",
 "3dAutomask", "3dSeg", "3dQwarp", "3dUnifize", "3dToutcount", "3dTqual",
 "1dgenARMA11", "1d_tool.py", "1dplot", "timing_tool.py", "gen_group_command.py",
 "3dpc", "3dSVD", "3dTcat", "3dbucket", "3dinfo", "SUMA",
]
FEATURES = {
 "single-subject GLM (3dDeconvolve/3dREMLfit)":
   r"3dDeconvolve|3dREMLfit|deconvolution.{0,40}AFNI|AFNI.{0,40}deconvolution",
 "preprocessing pipeline (afni_proc.py)":
   r"afni_proc\.py|uber_subject\.py",
 "percent signal change scaling":
   r"percent(?:age)? signal change|scaled? to a mean of 100|mean of 100",
 "group t-tests (3dttest++)":
   r"3dttest\+\+|3dttest\b",
 "group mixed effects (3dMEMA/3dMVM/3dLME/3dLMEr)":
   r"3dMEMA|3dMVM|3dLMEr|3dLME\b|linear mixed[- ]effects.{0,40}AFNI",
 "ANOVA (3dANOVA family)":
   r"3dANOVA",
 "cluster-extent inference (3dClustSim/3dFWHMx/ACF)":
   r"3dClustSim|3dFWHMx|3dClusterize|3dclust\b|autocorrelation function.{0,40}cluster|\bACF\b.{0,40}cluster|cluster[- ]extent.{0,40}AFNI",
 "ETAC / permutation clustering":
   r"3dXClustSim|\bETAC\b|equitable thresholding",
 "regional homogeneity (3dReHo)":
   r"3dReHo|regional homogeneity",
 "resting-state amplitude (3dRSFC/ALFF)":
   r"3dRSFC|\bALFF\b|fALFF|amplitude of low[- ]frequency",
 "connectivity (3dNetCorr/3dTcorr*/InstaCorr)":
   r"3dNetCorr|3dTcorr|3dGroupInCorr|InstaCorr",
 "nuisance regression / bandpass (3dTproject/3dBandpass)":
   r"3dTproject|3dBandpass|band[- ]?pass.{0,40}AFNI|AFNI.{0,40}band[- ]?pass",
 "motion correction (3dvolreg)":
   r"3dvolreg|motion correct\w*.{0,40}AFNI|AFNI.{0,40}motion correct",
 "slice timing (3dTshift)":
   r"3dTshift|slice[- ]tim\w+.{0,40}AFNI|AFNI.{0,40}slice[- ]tim",
 "registration/alignment (align_epi_anat/3dAllineate/3dQwarp)":
   r"align_epi_anat|3dAllineate|3dQwarp|3dNwarpApply|@SSwarper|@auto_tlrc|auto_warp",
 "smoothing (3dmerge/3dBlurToFWHM/3dBlurInMask)":
   r"3dBlurToFWHM|3dBlurInMask|3dmerge.{0,30}blur|blur.{0,30}3dmerge",
 "ROI extraction (3dROIstats/3dmaskave/3dTstat)":
   r"3dROIstats|3dmaskave|3dTstat|3dBrickStat",
 "voxelwise arithmetic (3dcalc)":
   r"3dcalc",
 "diffusion (3dDWItoDT/3dTrackID/FATCAT)":
   r"3dDWItoDT|3dTrackID|3dDTeig|FATCAT|3dDWUncert",
 "surface analysis (SUMA)":
   r"\bSUMA\b",
}
FEATURES = {k: re.compile(v) for k, v in FEATURES.items()}
# AFNI versions come in two flavours: 24.1.22 style and 2016.09.04.1341 style
VER = re.compile(r"AFNI[^.;]{0,40}?(?:v(?:ersion)?\.?\s*)?"
                 r"(\d{2}\.\d+\.\d+(?:\.\d+)?|\d{4}\.\d{2}\.\d{2}\.\d{4}|\d{8})")
AFNIWIN = re.compile(r"\bAFNI\b|Analysis of Functional NeuroImages")


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
    cmds = sorted({cmd for cmd in COMMANDS
                   if re.search(r"(?<![\w.-])" + re.escape(cmd) + r"(?![\w-])", text)})
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers = sorted(set(VER.findall(text)))
    ctx = []
    for m in AFNIWIN.finditer(text):
        lo = max(0, m.start() - 240); hi = min(len(text), m.end() + 300)
        ctx.append(("..." + text[lo:hi] + "...").strip())
        if len(ctx) >= 3:
            break
    c.update({"commands": cmds, "features": feats, "versions_all": vers,
              "afni_context": ctx})
    return c


HERE = os.path.dirname(os.path.abspath(__file__))
SURVEY = os.path.normpath(os.path.join(HERE, "..", "..", "survey", "data"))


def build_cohort():
    """Derive the AFNI cohort straight from the survey tables, so this script is
    self-seeding and no intermediate file needs to be checked in."""
    import csv
    titles = {}
    with open(os.path.join(SURVEY, "papers.tsv"), newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            titles[r["pmcid"]] = r
    out = []
    with open(os.path.join(SURVEY, "paper_software.tsv"), newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["package"].lower() != "afni":
                continue
            out.append({"pmcid": r["pmcid"], "doi": r["doi"], "journal": r["journal"],
                        "year": r["year"], "title": titles.get(r["pmcid"], {}).get("title", ""),
                        "version_survey": r["version"], "evidence": r["evidence_sentence"]})
    return out


cache = os.path.join(HERE, "afni_cohort.jsonl")
if os.path.exists(cache):
    cohort = [json.loads(l) for l in open(cache)]
else:
    cohort = build_cohort()
    with open(cache, "w") as fh:
        for c in cohort:
            fh.write(json.dumps(c) + "\n")
print("cohort: %d papers" % len(cohort))
with cf.ThreadPoolExecutor(12) as ex:
    out = list(ex.map(profile, cohort))
with open(os.path.join(HERE, "afni_profiles.jsonl"), "w") as fh:
    for c in out:
        fh.write(json.dumps(c) + "\n")
ok = [c for c in out if "profile_error" not in c]
print("profiled %d/%d" % (len(ok), len(out)))
from collections import Counter
fc = Counter(); cc = Counter(); vc = Counter()
for c in ok:
    for f in c["features"]: fc[f] += 1
    for k in c["commands"]: cc[k] += 1
    for v in c["versions_all"]: vc[v] += 1
print("\nFEATURES (papers):")
for k, n in fc.most_common(): print("  %-52s %d" % (k, n))
print("\nEXPLICIT COMMANDS (papers, top 25):")
for k, n in cc.most_common(25): print("  %-22s %d" % (k, n))
print("\nVERSIONS:", dict(vc.most_common(12)))
