"""Synthetic genotype data with known truth for the PLINK harnesses.

Writes PLINK 1 text (PED/MAP) from numpy arrays so that every harness makes its
own data in the script. Genotype coding: 0/1/2 = copies of allele "A2"... no:
we write alleles explicitly, so the harness knows which allele is which.
`geno` is an (n_samples, n_variants) int8 array with 0/1/2 = number of ALT
('T') alleles and -1 = missing. Allele 'A' is REF, 'T' is ALT.
"""
import os
import subprocess
import numpy as np

SCRATCH = os.environ.get("PLINK_SCRATCH", "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/plink")
PLINK19 = os.environ.get("PLINK19", os.path.join(SCRATCH, "src/1.9/plink"))
PLINK2 = os.environ.get("PLINK2", os.path.join(SCRATCH, "src/2.0/build_dynamic/plink2"))


def simulate(n, m, rng, maf=None, missing_rate=0.0, chrom=1, sex=None):
    """HWE genotypes at random or given allele frequencies (ALT frequency)."""
    if maf is None:
        maf = rng.uniform(0.05, 0.5, m)
    maf = np.broadcast_to(maf, (m,))
    g = (rng.random((n, m)) < maf).astype(np.int8) + (rng.random((n, m)) < maf).astype(np.int8)
    if missing_rate:
        g[rng.random((n, m)) < missing_rate] = -1
    return g


def write_pedmap(prefix, geno, pheno=None, sex=None, chrom=1, bp=None, fid=None, iid=None, ref="A", alt="T", cm=None):
    """PED/MAP: pheno None -> -9; sex None -> 1 (male) for everyone... use 2 for
    female by default so chrX is diploid unless the harness says otherwise."""
    n, m = geno.shape
    chrom = np.broadcast_to(np.asarray(chrom), (m,))
    bp = np.arange(1, m + 1) * 1000 if bp is None else bp
    cm = np.zeros(m) if cm is None else cm
    with open(prefix + ".map", "w") as f:
        for j in range(m):
            f.write(f"{chrom[j]}\tsnp{j+1}\t{cm[j]:g}\t{bp[j]}\n")
    sex = np.full(n, 2) if sex is None else sex
    pheno = np.full(n, -9) if pheno is None else pheno
    fid = [f"F{i+1}" for i in range(n)] if fid is None else fid
    iid = [f"I{i+1}" for i in range(n)] if iid is None else iid
    code = {0: f"{ref} {ref}", 1: f"{ref} {alt}", 2: f"{alt} {alt}", -1: "0 0"}
    with open(prefix + ".ped", "w") as f:
        for i in range(n):
            ph = pheno[i]
            phs = f"{ph:g}" if isinstance(ph, (float, np.floating)) else str(ph)
            f.write(f"{fid[i]} {iid[i]} 0 0 {sex[i]} {phs} " + " ".join(code[int(x)] for x in geno[i]) + "\n")
    return prefix


def run(exe, args, cwd=None, check=True):
    r = subprocess.run([exe, *args], capture_output=True, text=True, cwd=cwd)
    if check and r.returncode != 0:
        raise RuntimeError(f"{exe} {' '.join(args)}\n{r.stdout[-3000:]}\n{r.stderr[-3000:]}")
    return r


def read_table(path, sep=None):
    """Whitespace/tab table with a header line (leading '#' stripped) -> dict of columns (strings)."""
    with open(path) as f:
        lines = [l.rstrip("\n") for l in f if l.strip()]
    hdr = lines[0].lstrip("#").split(sep)
    rows = [l.split(sep) for l in lines[1:]]
    return {h: [r[k] for r in rows] for k, h in enumerate(hdr)}


def fnum(v):
    try:
        return float(v)
    except ValueError:
        return float("nan")


def version(exe):
    r = subprocess.run([exe, "--version"], capture_output=True, text=True)
    return (r.stdout + r.stderr).strip().splitlines()[0]
