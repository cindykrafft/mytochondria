"""Shared helpers for the GSEA harnesses: builds, file writers, CLI runners, output parsers.

Every harness runs the *shipped* GSEA code (a jar built from the audited commit, or the
class trees compiled from the release tags) through its own command-line entry points,
`xtools.gsea.GseaPreranked` and `xtools.gsea.Gsea`, exactly as `gsea-cli.sh` does.

Set GSEA_SCRATCH to the directory holding the clone (`src/`, with `build/libs/*.jar`
and `modules/`) and the tag checkouts (`v4.3.2/`, `v4.1.0/`, `v4.0.3/`, each with
`out/` compiled by javac, `modules/` and `lib/`).
"""
import glob
import numpy as np
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

# /tmp/gseawork is a symlink to the scratchpad clone directory: GSEA's option parser splits
# a path containing "-" (the scratchpad path does), so every path handed to it must be dash-free.
SCRATCH = os.environ.get(
    "GSEA_SCRATCH",
    "/tmp/gseawork" if os.path.isdir("/tmp/gseawork") else
    "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/gsea",
)

JAVA_OPTS = ["-Djava.awt.headless=true", "-Xmx3g", "-Djava.util.logging.config.file=/dev/null"]


def classpath(build="master"):
    if build.startswith("patched_"):      # a jar built from a fix branch: <SCRATCH>/patched/<name>.jar + master modules
        return ":".join([os.path.join(SCRATCH, "patched", build.split("_", 1)[1] + ".jar"),
                         os.path.join(SCRATCH, "src", "modules", "*")])
    if build in ("master", "v4.4.0"):
        d = os.path.join(SCRATCH, "src" if build == "master" else "v4.4.0")
        jars = glob.glob(os.path.join(d, "build", "libs", "*.jar"))
        assert jars, "no jar under %s/build/libs" % d
        return ":".join([jars[0], os.path.join(d, "modules", "*")])
    d = os.path.join(SCRATCH, build)
    parts = [os.path.join(d, "out"), os.path.join(d, "modules", "*")]
    if os.path.isdir(os.path.join(d, "lib")):
        parts.append(os.path.join(d, "lib", "*"))
    return ":".join(parts)


def java_version():
    out = subprocess.run(["java", "-version"], capture_output=True, text=True).stderr
    return out.splitlines()[-3].strip() if out else "?"


def build_describe(build="master"):
    if build.startswith("patched_"):
        return "master + patch " + build.split("_", 1)[1]
    d = os.path.join(SCRATCH, "src" if build == "master" else build)
    try:
        return subprocess.run(["git", "-C", d, "log", "-1", "--format=%h %ad", "--date=short"],
                              capture_output=True, text=True).stdout.strip()
    except Exception:
        return "?"


# ----------------------------------------------------------------- file writers
def strictly_decreasing(scores, gap=4e-6):
    """Descending scores with no ties, also after GSEA reads them as float32."""
    s = np.sort(np.asarray(scores, dtype=np.float64))[::-1].copy()
    for i in range(1, s.size):
        if s[i] > s[i - 1] - gap:
            s[i] = s[i - 1] - gap
    assert len(set(s.astype(np.float32))) == s.size
    return s


def write_rnk(path, names, scores):
    with open(path, "w") as f:
        for n, s in zip(names, scores):
            f.write("%s\t%r\n" % (n, float(s)))


def write_gmt(path, sets):
    """sets: dict name -> iterable of gene names"""
    with open(path, "w") as f:
        for name, genes in sets.items():
            f.write("%s\tna\t%s\n" % (name, "\t".join(genes)))


def write_gct(path, names, samples, X):
    with open(path, "w") as f:
        f.write("#1.2\n%d\t%d\n" % (len(names), len(samples)))
        f.write("NAME\tDescription\t" + "\t".join(samples) + "\n")
        for n, row in zip(names, X):
            f.write(n + "\tna\t" + "\t".join("%r" % float(v) for v in row) + "\n")


def write_cls(path, labels, classes=("A", "B")):
    with open(path, "w") as f:
        f.write("%d %d 1\n" % (len(labels), len(classes)))
        f.write("# " + " ".join(classes) + "\n")
        f.write(" ".join(labels) + "\n")


def write_chip(path, probe_to_symbol):
    with open(path, "w") as f:
        f.write("Probe Set ID\tGene Symbol\tGene Title\n")
        for p, s in probe_to_symbol.items():
            f.write("%s\t%s\t%s title\n" % (p, s, s))


# ----------------------------------------------------------------- runners
COMMON = {"gui": "false", "zip_report": "false", "plot_top_x": "0", "make_sets": "false",
          "norm": "meandiv", "rnd_seed": "149", "set_min": "15", "set_max": "500",
          "scoring_scheme": "weighted", "nperm": "1000", "collapse": "No_Collapse",
          "include_only_symbols": "true"}


def _args(base, params):
    d = dict(base)
    d.update({k: str(v) for k, v in params.items()})
    out = []
    for k, v in d.items():
        out += ["-" + k, v]
    return out


def _run(build, main, args, outdir, label):
    os.makedirs(outdir, exist_ok=True)
    cmd = ["java"] + JAVA_OPTS + ["-cp", classpath(build), main] + args + ["-out", outdir, "-rpt_label", label]
    env = dict(os.environ)
    env.pop("JAVA_TOOL_OPTIONS", None)  # keep the log clean; the runs need no network
    env["HOME"] = os.path.join(SCRATCH, "home_" + build)  # isolate ~/.gsea preferences per build
    os.makedirs(env["HOME"], exist_ok=True)
    p = subprocess.run(cmd, capture_output=True, text=True, env=env)
    log = p.stdout + p.stderr
    with open(os.path.join(outdir, label + ".log"), "w") as f:
        f.write(" ".join(cmd) + "\n\n" + log)
    runs = sorted(glob.glob(os.path.join(outdir, label + ".Gsea*")), key=os.path.getmtime)
    return p.returncode, log, (runs[-1] if runs else None)


def run_preranked(build, rnk, gmt, outdir, label="run", **params):
    args = _args(dict(COMMON, rnk=rnk, gmx=gmt), params)
    rc, log, rundir = _run(build, "xtools.gsea.GseaPreranked", args, outdir, label)
    return Result(rc, log, rundir, "na_pos", "na_neg")


def run_gsea(build, gct, cls, gmt, outdir, label="run", classes=("A", "B"), **params):
    base = dict(COMMON, res=gct, cls="%s#%s_versus_%s" % (cls, classes[0], classes[1]), gmx=gmt,
                permute="gene_set", metric="Signal2Noise", sort="real", order="descending", num="10",
                median="false", rnd_type="no_balance", create_gcts="false", mode="Max_probe")
    args = _args(base, params)
    rc, log, rundir = _run(build, "xtools.gsea.Gsea", args, outdir, label)
    return Result(rc, log, rundir, classes[0], classes[1])


class Result:
    """Parsed GSEA run: report rows (pos + neg tables), edb records, ranked gene list."""

    def __init__(self, rc, log, rundir, pos_tag, neg_tag):
        self.rc, self.log, self.rundir = rc, log, rundir
        self.rows, self.edb, self.ranked, self.sizes = {}, {}, None, {}
        if rundir is None:
            return
        for tag in (pos_tag, neg_tag):
            for f in glob.glob(os.path.join(rundir, "gsea_report_for_%s_*.tsv" % tag)) + \
                    glob.glob(os.path.join(rundir, "gsea_report_for_%s_*.xls" % tag)):
                self.rows.update(_read_report(f))
        f = glob.glob(os.path.join(rundir, "ranked_gene_list_*.tsv")) + glob.glob(os.path.join(rundir, "ranked_gene_list_*.xls"))
        if f:
            self.ranked = _read_ranked(f[0])
        f = os.path.join(rundir, "edb", "results.edb")
        if os.path.exists(f):
            self.edb = _read_edb(f)
        f = os.path.join(rundir, "gene_set_sizes.tsv")
        if not os.path.exists(f):
            f = os.path.join(rundir, "gene_set_sizes.xls")
        if os.path.exists(f):
            with open(f) as fh:
                next(fh)
                for line in fh:
                    p = line.rstrip("\n").split("\t")
                    if len(p) >= 3 and p[0] and p[1].isdigit():
                        self.sizes[p[0]] = (int(p[1]), int(p[2]) if p[2].isdigit() else -1, p[3] if len(p) > 3 else "")

    def ok(self):
        return self.rc == 0 and self.rundir is not None

    def error(self):
        m = re.findall(r"(Exception[^\n]*|Error[^\n]*)", self.log)
        return m[0] if m else self.log[-400:]


def _read_report(path):
    rows = {}
    with open(path) as f:
        header = next(f).rstrip("\n").split("\t")
        idx = {h: i for i, h in enumerate(header)}
        for line in f:
            p = line.rstrip("\n").split("\t")
            if not p[0]:
                continue
            g = lambda k: float(p[idx[k]]) if p[idx[k]] not in ("", "NaN", "---") else float("nan")
            rows[p[0]] = dict(size=int(p[idx["SIZE"]]), es=g("ES"), nes=g("NES"), np=g("NOM p-val"),
                              fdr=g("FDR q-val"), fwer=g("FWER p-val"), rank_at_max=int(p[idx["RANK AT MAX"]]),
                              leading_edge=p[idx["LEADING EDGE"]])
    return rows


def _read_ranked(path):
    out = []
    with open(path) as f:
        header = next(f).rstrip("\n").split("\t")
        for line in f:
            p = line.rstrip("\n").split("\t")
            if p[0]:
                v = p[header.index("SCORE")]
                out.append((p[0], float(v) if v not in ("", "NaN", "---") else float("nan")))
    return out


def _read_edb(path):
    root = ET.parse(path).getroot()
    recs = {}
    for dtg in root.iter("DTG"):
        name = dtg.get("GENESET").split("#", 1)[1]
        recs[name] = dict(
            es=float(dtg.get("ES")), nes=float(dtg.get("NES")), np=float(dtg.get("NP")),
            fdr=float(dtg.get("FDR")), fwer=float(dtg.get("FWER")),
            rnd_es=[float(x) for x in dtg.get("RND_ES").split()] if dtg.get("RND_ES") else [],
            hit_indices=[int(x) for x in dtg.get("HIT_INDICES").split()] if dtg.get("HIT_INDICES") else [],
            rank_at_es=int(float(dtg.get("RANK_AT_ES"))),
        )
    return recs


def banner(title, build="master"):
    print("=" * 78)
    print(title)
    print("GSEA build: %s (%s)   %s   python %s" % (build, build_describe(build), java_version(),
                                                     sys.version.split()[0]))
    print("=" * 78)
