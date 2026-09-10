#!/usr/bin/env python3
"""Helpers shared by the harnesses: write GSEA input files, run the shipped jar's
command-line tools (xtools.gsea.GseaPreranked / xtools.gsea.Gsea), and parse the
results.edb XML plus the report TSVs that a run writes.

The jar under test is selected with the environment variable GSEA_CP (a Java classpath;
defaults to the master build in the scratchpad).  Every number read back comes from the
files the tool wrote, so a comparison against ref_gsea.py is a comparison against what a
user of the release would see.  results.edb stores ES/NES/NP/FDR/FWER and the random ES
vector to four decimals (EdbFolderParser, Printf %.4f); RANK_AT_ES and HIT_INDICES exactly.
"""
import glob
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

import numpy as np

# GSEA's file parameters cannot contain "-" in the path (the value is cut at the first
# dash: "File not found: /tmp/claude"), so the scratchpad clone is reached through a
# dash-free symlink.  The tool also creates a dated working directory in its cwd, so every
# run is started from SCRATCH.
SCRATCH = "/tmp/gseawork"   # -> <scratchpad>/gsea
DEFAULT_CP = f"{SCRATCH}/src/build/libs/gsea-minimal-user.jar:{SCRATCH}/src/modules/*"
GSEA_CP = os.environ.get("GSEA_CP", DEFAULT_CP)
JAVA = os.environ.get("JAVA", "java")


# ----------------------------------------------------------------------------- inputs
def write_rnk(path, names, scores):
    with open(path, "w") as fh:
        for n, s in zip(names, scores):
            fh.write(f"{n}\t{float(s)!r}\n")


def write_gmt(path, gene_sets):
    with open(path, "w") as fh:
        for name, members in gene_sets.items():
            fh.write(name + "\tna\t" + "\t".join(members) + "\n")


def write_gct(path, names, X, sample_names=None):
    n, m = X.shape
    sample_names = sample_names or [f"s{j}" for j in range(m)]
    with open(path, "w") as fh:
        fh.write("#1.2\n%d\t%d\n" % (n, m))
        fh.write("NAME\tDESCRIPTION\t" + "\t".join(sample_names) + "\n")
        for i in range(n):
            fh.write(names[i] + "\tna\t" + "\t".join("" if np.isnan(v) else repr(float(v)) for v in X[i]) + "\n")


def write_cls(path, labels, class_names=("A", "B")):
    labels = list(labels)
    with open(path, "w") as fh:
        fh.write("%d 2 1\n# %s %s\n" % (len(labels), class_names[0], class_names[1]))
        fh.write(" ".join(str(int(l)) for l in labels) + "\n")


def write_chip(path, probe_to_symbol):
    with open(path, "w") as fh:
        fh.write("Probe Set ID\tGene Symbol\tGene Title\n")
        for p, s in probe_to_symbol.items():
            fh.write(f"{p}\t{s}\t{s} title\n")


# ----------------------------------------------------------------------------- run
COMMON = ["-gui", "false", "-zip_report", "false", "-plot_top_x", "0", "-make_sets", "false",
          "-rpt_label", "run"]


def run_preranked(rnk, gmt, out, nperm=1000, seed=149, extra=()):
    """GseaPreranked with the audit's fixed options; returns the run directory."""
    os.makedirs(out, exist_ok=True)
    cmd = [JAVA, "-Xmx2g", "-cp", GSEA_CP, "xtools.gsea.GseaPreranked",
           "-rnk", rnk, "-gmx", gmt, "-out", out, "-nperm", str(nperm), "-rnd_seed", str(seed),
           "-collapse", "No_Collapse"] + COMMON + list(extra)
    return _run(cmd, out)


def run_gsea(gct, cls, gmt, out, nperm=1000, seed=149, permute="gene_set", metric="Signal2Noise",
             extra=()):
    """xtools.gsea.Gsea (expression dataset + phenotype labels)."""
    os.makedirs(out, exist_ok=True)
    extra = list(extra)
    collapse = [] if "-collapse" in extra else ["-collapse", "No_Collapse"]
    cmd = [JAVA, "-Xmx2g", "-cp", GSEA_CP, "xtools.gsea.Gsea",
           "-res", gct, "-cls", cls, "-gmx", gmt, "-out", out, "-nperm", str(nperm),
           "-rnd_seed", str(seed), "-permute", permute, "-metric", metric] + collapse + COMMON + extra
    return _run(cmd, out)


def _run(cmd, out):
    before = set(glob.glob(os.path.join(out, "run.*")))
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=SCRATCH)
    new = sorted(set(glob.glob(os.path.join(out, "run.*"))) - before)
    if r.returncode != 0 or not new:
        sys.stderr.write(r.stdout[-3000:] + "\n" + r.stderr[-3000:] + "\n")
        raise RuntimeError("GSEA run failed: " + " ".join(cmd))
    return new[-1]


# ----------------------------------------------------------------------------- outputs
def _floats(s):
    return np.array([float(x) for x in s.split()]) if s else np.array([])


def parse_edb(run_dir):
    """results.edb -> dict gene_set -> dict(es, nes, np, fdr, fwer, rank_at_es, hit_indices,
    rnd_es, es_profile)."""
    edb = os.path.join(run_dir, "edb", "results.edb")
    root = ET.parse(edb).getroot()
    out = {}
    for el in root.iter("DTG"):
        name = el.get("GENESET").split("#", 1)[1]
        out[name] = dict(
            es=float(el.get("ES")), nes=float(el.get("NES")), np=float(el.get("NP")),
            fdr=float(el.get("FDR")), fwer=float(el.get("FWER")),
            rank_at_es=int(float(el.get("RANK_AT_ES"))),
            hit_indices=np.array([int(x) for x in el.get("HIT_INDICES").split()]),
            rnd_es=_floats(el.get("RND_ES")), es_profile=_floats(el.get("ES_PROFILE")),
            rank_score_at_es=float(el.get("RANK_SCORE_AT_ES")),
        )
    return out


def parse_report_tsv(run_dir):
    """gsea_report_for_*.tsv (both signs; .xls in releases before 4.2) -> dict gene_set -> dict
    of the printed columns."""
    out = {}
    for f in glob.glob(os.path.join(run_dir, "gsea_report_for_*.tsv")) + glob.glob(os.path.join(run_dir, "gsea_report_for_*.xls")):
        with open(f) as fh:
            header = fh.readline().rstrip("\n").split("\t")
            for line in fh:
                row = line.rstrip("\n").split("\t")
                d = dict(zip(header, row))
                out[d["NAME"]] = d
    return out


def parse_ranked_gene_list(run_dir):
    """ranked_gene_list_*.tsv -> (names, scores) in the tool's rank order (full float repr)."""
    f = (glob.glob(os.path.join(run_dir, "ranked_gene_list_*.tsv")) + glob.glob(os.path.join(run_dir, "ranked_gene_list_*.xls")))[0]
    names, scores = [], []
    with open(f) as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            row = line.rstrip("\n").split("\t")
            d = dict(zip(header, row))
            names.append(d["NAME"])
            scores.append(float("nan") if d["SCORE"] == "---" else float(d["SCORE"]))
    return names, np.array(scores)


def parse_edb_rnk(run_dir):
    """The ranked list the run analysed, as exported into edb/*.rnk."""
    f = glob.glob(os.path.join(run_dir, "edb", "*.rnk"))[0]
    names, scores = [], []
    with open(f) as fh:
        for line in fh:
            if not line.strip() or line.startswith("#"):
                continue
            n, s = line.rstrip("\n").split("\t")[:2]
            names.append(n)
            scores.append(float(s))
    return names, np.array(scores)


def parse_gct(path):
    with open(path) as fh:
        fh.readline()
        fh.readline()
        header = fh.readline().rstrip("\n").split("\t")
        names, rows = [], []
        for line in fh:
            row = line.rstrip("\n").split("\t")
            names.append(row[0])
            rows.append([float(v) for v in row[2:]])
    return names, header[2:], np.array(rows)


def java_version_string():
    r = subprocess.run([JAVA, "-cp", GSEA_CP, "xtools.gsea.GseaPreranked", "-help"], capture_output=True, text=True, cwd=SCRATCH)
    m = re.search(r"GSEA\s+v?[\d.]+", r.stdout + r.stderr)
    return m.group(0) if m else "unknown"
