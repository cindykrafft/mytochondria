#!/usr/bin/env python3
"""Profile which parts of FSL each cohort paper used."""
import json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
sys.path.insert(0, ".")
import extract as E

COMMANDS = [
 "FEAT", "MELODIC", "randomise", "randomise_parallel",
 "FLAME", "flameo", "FILM", "film_gls","BET", "flirt", "FLIRT",
 "fnirt", "FNIRT", "applywarp", "FAST", "FIRST",
 "run_first_all", "fslmaths", "fslstats", "fslmeants", "fslmerge",
 "mcflirt", "MCFLIRT", "slicetimer", "susan", "SUSAN", "tbss_1_preproc",
 "TBSS", "dtifit", "bedpostx", "probtrackx", "probtrackx2", "xtract",
 "eddy_correct", "eddy_cuda", "topup", "fugue", "epi_reg",
 "dual_regression", "fsl_glm", "fslreorient2std", "smoothest",
 "fsl_anat", "fsl_motion_outliers", "ICA-AROMA", "oxford_asl",
 "basil", "fabber", "possum", "fslvbm", "siena", "SIENA", "sienax",
]
FEATURES = {
 "task fMRI GLM (FEAT/FILM)":  r"\bFEAT\b|FMRI Expert Analysis Tool|film_gls|prewhiten",
 "group mixed effects (FLAME)":r"\bFLAME\b|flameo|mixed[- ]effects.{0,40}FSL|FSL.{0,40}mixed[- ]effects",
 "permutation inference (randomise)": r"randomise|permutation.{0,50}FSL|FSL.{0,50}permutation|threshold[- ]free cluster enhancement|\bTFCE\b",
 "GRF cluster correction":     r"Gaussian random field|GRF|cluster.{0,40}[zZ]\s*[>=]\s*\d|cluster[- ]forming threshold.{0,60}FSL",
 "ICA (MELODIC)":              r"MELODIC|independent component analysis.{0,60}FSL|FSL.{0,60}independent component",
 "ICA cleanup (FIX/AROMA)":    r"ICA[- ]?AROMA|FIX.{0,30}(?:classifier|clean|denois)|fsl_regfilt",
 "brain extraction (BET)":     r"\bBET\b|[Bb]rain [Ee]xtraction [Tt]ool",
 "linear registration (FLIRT)":r"FLIRT|linear (?:image )?registration tool",
 "nonlinear registration (FNIRT)": r"FNIRT|nonlinear (?:image )?registration.{0,40}FSL|FSL.{0,40}nonlinear registration",
 "tissue segmentation (FAST)": r"\bFAST\b.{0,60}segment|segment.{0,60}\bFAST\b|FMRIB.{0,10}Automated Segmentation",
 "subcortical segmentation (FIRST)": r"\bFIRST\b.{0,60}segment|segment.{0,60}\bFIRST\b|run_first_all|FMRIB.{0,10}Integrated Registration",
 "TBSS":                       r"\bTBSS\b|[Tt]ract[- ][Bb]ased [Ss]patial [Ss]tatistics",
 "diffusion fitting (dtifit/bedpostx)": r"dtifit|bedpostx|BEDPOSTX",
 "tractography (probtrackx/xtract)": r"probtrackx|\\bXTRACT\\b|(?<![a-zA-Z])xtract(?![a-zA-Z])",
 "distortion correction (topup/eddy)": r"\btopup\b|\beddy\b|eddy_correct|eddy current[s]? correct",
 "motion correction (MCFLIRT)": r"MCFLIRT",
 "fieldmap (FUGUE/epi_reg)":   r"\bFUGUE\b|epi_reg|fieldmap.{0,40}FSL",
 "VBM/siena":                  r"fslvbm|FSL[- ]VBM|\bSIENA\b|sienax",
 "resting-state seed/dual regression": r"dual[- _]regression|seed[- ]based.{0,60}FSL",
 "smoothing (SUSAN)":          r"\bSUSAN\b",
}
FEATURES = {k: re.compile(v) for k, v in FEATURES.items()}
VER = re.compile(r"FSL[^.;]{0,30}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
FSLWIN = re.compile(r"\bFSL\b|FMRIB Software Library")

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
    cmds = sorted({cmd for cmd in COMMANDS
                   if re.search(r"(?<![\w-])"+re.escape(cmd)+r"(?![\w-])", text)})
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers = sorted(set(VER.findall(text)))
    ctx = []
    for m in FSLWIN.finditer(text):
        lo = max(0, m.start()-240); hi = min(len(text), m.end()+300)
        ctx.append(("..."+text[lo:hi]+"...").strip())
        if len(ctx) >= 3: break
    c.update({"commands": cmds, "features": feats, "versions_all": vers, "fsl_context": ctx})
    return c

cohort = [json.loads(l) for l in open("fsl_cohort.jsonl")]
with cf.ThreadPoolExecutor(12) as ex:
    out = list(ex.map(profile, cohort))
with open("fsl_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
ok = [c for c in out if "profile_error" not in c]
print("profiled %d/%d" % (len(ok), len(out)))
from collections import Counter
fc = Counter(); cc = Counter(); vc = Counter()
for c in ok:
    for f in c["features"]: fc[f] += 1
    for k in c["commands"]: cc[k] += 1
    for v in c["versions_all"]: vc[v] += 1
print("\nFEATURES (papers):")
for k, n in fc.most_common(): print("  %-40s %d" % (k, n))
print("\nEXPLICIT COMMANDS (papers, top 20):")
for k, n in cc.most_common(20): print("  %-20s %d" % (k, n))
print("\nVERSIONS:", dict(vc.most_common(12)))
