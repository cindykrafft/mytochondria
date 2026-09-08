"""Run an R snippet against one of the edgeR builds made for this audit and exchange
matrices through CSV files. Used by the Python harnesses; the version names are the
same as in rlib.sh."""
import os, subprocess, sys, tempfile
import numpy as np

SCRATCH = os.environ.get("EDGER_SCRATCH",
    "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/edger")
LIBS = {
    "4.0.16": None,
    "3.36.0": f"{SCRATCH}/lib3.36.0",
    "4.4.2":  f"{SCRATCH}/libdeps:{SCRATCH}/lib4.4.2",
    "4.10.1": f"{SCRATCH}/libdeps:{SCRATCH}/lib4.10.1",
    "4.10.5": f"{SCRATCH}/libdeps:{SCRATCH}/lib_rel323",
    "devel":  f"{SCRATCH}/libdeps:{SCRATCH}/lib_src",
}

def version_arg(default="4.10.5"):
    for a in sys.argv[1:]:
        if a.startswith("--lib="):
            return a.split("=", 1)[1]
    return default

def run_r(code, version, inputs=None):
    """inputs: dict name -> ndarray, written as CSV and available in R as `name`
    (read with as.matrix(read.csv(...))). The R code must write any outputs it wants
    returned with write.csv(x, file.path(OUT, "<name>.csv"), row.names=FALSE); they
    come back as a dict of ndarrays. R's stdout is returned too."""
    env = dict(os.environ)
    lib = LIBS[version]
    if lib is None:
        env.pop("R_LIBS_USER", None)
    else:
        env["R_LIBS_USER"] = lib
    with tempfile.TemporaryDirectory() as td:
        pre = [f'OUT <- "{td}"', "suppressMessages(library(edgeR))"]
        for k, v in (inputs or {}).items():
            p = os.path.join(td, k + ".csv")
            np.savetxt(p, np.asarray(v, dtype=float), delimiter=",")
            pre.append(f'{k} <- as.matrix(read.csv("{p}", header=FALSE))')
        script = "\n".join(pre) + "\n" + code
        r = subprocess.run(["Rscript", "-"], input=script, text=True, env=env,
                           capture_output=True)
        if r.returncode != 0:
            raise RuntimeError("R failed:\n" + r.stderr + "\n" + r.stdout)
        outs = {}
        for f in os.listdir(td):
            if f.endswith(".csv") and f[:-4] not in (inputs or {}):
                outs[f[:-4]] = np.loadtxt(os.path.join(td, f), delimiter=",", skiprows=1, ndmin=1)
        return outs, r.stdout

def edger_version(version):
    _, out = run_r('cat(as.character(packageVersion("edgeR")), as.character(packageVersion("limma")))', version)
    return out.strip()
