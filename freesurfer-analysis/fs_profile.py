#!/usr/bin/env python3
"""Profile which parts of FreeSurfer each cohort paper used."""
import json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
sys.path.insert(0, ".")
import extract as E

# FreeSurfer commands / binaries (exact, case-sensitive where meaningful)
COMMANDS = [
 "recon-all", "mri_glmfit", "mri_glmfit-sim", "mris_preproc", "mri_surf2surf",
 "mri_vol2surf", "mri_surf2vol", "mris_anatomical_stats", "mri_segstats",
 "mri_convert", "bbregister", "mri_coreg", "mris_ca_label", "mri_aparc2aseg",
 "mri_label2vol", "mri_label2label", "mris_expand", "mris_thickness",
 "mri_normalize", "mri_watershed", "mris_smooth", "mris_inflate",
 "mris_sphere", "mris_register", "mri_em_register", "mri_ca_register",
 "mri_ca_label", "mris_fix_topology", "mri_fill", "mri_segment",
 "mris_make_surfaces", "mris_place_surface", "mri_robust_register",
 "mri_robust_template", "trac-all", "dt_recon", "tkregister2", "freeview",
 "tksurfer", "mris_pmake", "mri_cvs_register", "mris_fwhm", "selxavg3-sess",
 "mkanalysis-sess", "asegstats2table", "aparcstats2table", "mri_annotation2label",
 "synthseg", "SynthSeg", "SynthStrip", "mri_synthstrip", "samseg", "run_samseg",
 "gtmseg", "mri_gtmpvc", "xhemireg", "surfreg", "mris_ca_train",
]
# Pipeline/feature signals (regex, case-insensitive)
FEATURES = {
 "cortical thickness":      r"cortical thickness|thickness map|mean thickness",
 "surface area":            r"surface area|pial area|white surface area",
 "cortical volume":         r"cortical (?:gr[ae]y matter )?volume",
 "subcortical segmentation (aseg)": r"\baseg\b|subcortical segment|subcortical volume|automated segmentation of subcortical",
 "parcellation (aparc/atlas)": r"\baparc\b|Desikan|Destrieux|DKT atlas|parcellat",
 "hippocampal subfields":   r"hippocampal subfield|subfield segmentation",
 "amygdala nuclei":         r"amygdala(?:r)? nuclei",
 "brainstem substructures": r"brainstem substructure",
 "thalamic nuclei":         r"thalamic nuclei segmentation",
 "surface reconstruction":  r"surface reconstruct|white(?:/|\s?and\s?)pial surface|cortical surface model|pial surface",
 "surface-based registration": r"fsaverage|spherical registration|surface(?:-| )based registration",
 "boundary-based registration": r"boundary[- ]based registration|\bBBR\b|bbregister",
 "longitudinal stream":     r"longitudinal (?:stream|pipeline|processing)|robust template",
 "group GLM (mri_glmfit)":  r"mri_glmfit|glm_fit|general linear model.{0,60}(?:vertex|surface)|vertex[- ]wise",
 "cluster correction (Monte Carlo)": r"Monte Carlo simulation.{0,60}cluster|cluster[- ]wise correction|mri_glmfit-sim|precomputed Z Monte Carlo",
 "LGI (gyrification)":      r"local gyrification index|\bLGI\b",
 "myelin/T1w-T2w ratio":    r"T1w/T2w|myelin map",
 "entorhinal/BA labels":    r"Brodmann area label|\bBA4[ab]?\b|\bentorhinal exvivo\b",
 "PET partial volume (PETsurfer)": r"PETsurfer|gtmpvc|partial volume correction.{0,50}(?:surface|FreeSurfer)",
 "TRACULA (diffusion)":     r"TRACULA|trac-all",
 "functional preprocessing (FS-FAST)": r"FS-?FAST|selxavg",
 "brain extraction/skullstrip": r"skull[- ]?strip|brain extraction|watershed",
 "manual edits/QC":         r"manual(?:ly)? (?:edit|inspect|correct)|quality (?:control|check).{0,60}(?:surface|segmentation)|visual inspection.{0,60}(?:surface|segmentation)",
}
FEATURES = {k: re.compile(v, re.I) for k, v in FEATURES.items()}
VER = re.compile(r"[Ff]ree[Ss]urfer[^.;]{0,40}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:\.\d+)*)")
FSWIN = re.compile(r"[Ff]ree[Ss]urfer")

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
    # commands: exact token search
    cmds = sorted({cmd for cmd in COMMANDS if re.search(r"(?<![\w-])"+re.escape(cmd)+r"(?![\w-])", text)})
    feats = sorted(k for k,rx in FEATURES.items() if rx.search(text))
    # all versions stated anywhere near "FreeSurfer"
    vers = sorted(set(VER.findall(text)))
    # grab up to 3 FreeSurfer-mention sentences as context
    ctx=[]
    for m in FSWIN.finditer(text):
        lo=max(0,m.start()-260); hi=min(len(text),m.end()+320)
        s=text[lo:hi]
        ctx.append(("..."+s+"...").strip())
        if len(ctx)>=3: break
    c.update({"commands":cmds,"features":feats,"versions_all":vers,"fs_context":ctx})
    return c

cohort=[json.loads(l) for l in open("fs_cohort.jsonl")]
with cf.ThreadPoolExecutor(12) as ex:
    out=list(ex.map(profile, cohort))
with open("fs_profiles.jsonl","w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
ok=[c for c in out if "profile_error" not in c]
print("profiled %d/%d" % (len(ok),len(out)))
from collections import Counter
fc=Counter(); cc=Counter(); vc=Counter()
for c in ok:
    for f in c["features"]: fc[f]+=1
    for k in c["commands"]: cc[k]+=1
    for v in c["versions_all"]: vc[v]+=1
print("\nFEATURES (papers):")
for k,n in fc.most_common(): print("  %-38s %d" % (k,n))
print("\nEXPLICIT COMMANDS (papers):")
for k,n in cc.most_common(): print("  %-24s %d" % (k,n))
print("\nALL VERSIONS SEEN:")
print(" ", dict(vc.most_common()))
