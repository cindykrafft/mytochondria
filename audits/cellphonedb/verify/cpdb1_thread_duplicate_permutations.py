#!/usr/bin/env python3
"""CPDB1: the permutation workers draw the SAME permutations, so the null distribution holds
only about `iterations / threads` distinct label shuffles, each counted `threads` times.

`shuffled_analysis` (cpdb_statistical_analysis_helper.py:494-506) hands the per-iteration work
to `multiprocessing.pool.Pool(processes=threads)`. On a fork platform every worker inherits the
parent's numpy global RNG state and then advances its own private copy of it. `shuffle_meta`
(helper.py:96) uses the global `np.random.shuffle`, so worker k's j-th shuffle is identical to
worker l's j-th shuffle. `Pool.imap` hands out the tasks dynamically, so the multiplicities are
not exactly `threads` (a worker that gets more tasks contributes a few unique draws at the end),
but the bulk of the null is duplicated `threads` times.

The fixture here is 30 cells in three cell types of ten, i.e. 30!/(10!)^3 = 5.55e12 distinct
label assignments, so repeated draws cannot happen by chance -- unlike the 9-cell fixture used
elsewhere, where 1000 draws from 1680 assignments collide often on their own.

  A. distinct permutations actually drawn, by `threads`, recorded from the package's own
     shuffle_meta on the user-facing API;
  B. the multiplicity histogram;
  C. the effect on the p-value estimator: its variance over repeated runs corresponds to
     iterations/threads independent permutations, not to `iterations`.

`debug_seed` is left at its default -1 (no seeding) throughout: this is the default user path.
"""
import collections
import os
import sys
import tempfile
import numpy as np
import pandas as pd
from importlib.metadata import version

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tiny_dataset as T

from cellphonedb.src.core.methods import cpdb_statistical_analysis_helper as H
from cellphonedb.src.core.methods import cpdb_statistical_analysis_method

ITER = 1000
NREP = 20
tmp = tempfile.mkdtemp(prefix="cpdb1_")
db = T.build_db(os.path.join(tmp, "db"))

# 30 cells, 3 cell types x 10, continuous counts (no ties in the null)
rng = np.random.default_rng(11)
cells = ["c%02d" % i for i in range(30)]
ctypes = ["CTA"] * 10 + ["CTB"] * 10 + ["CTC"] * 10
counts = np.round(rng.random((5, 30)) * 4 + 0.5, 6)
counts_fp, meta_fp, _ = T.write_inputs(os.path.join(tmp, "in"), counts=counts, cells=cells,
                                       cell_types=ctypes)
rec_dir = os.path.join(tmp, "perm")
os.makedirs(rec_dir)
_orig_shuffle = H.shuffle_meta


def recording_shuffle(meta):
    """The package's own shuffle_meta, with the resulting label vector written to disk."""
    out = _orig_shuffle(meta)
    with open(os.path.join(rec_dir, "p%d.txt" % os.getpid()), "a") as fh:
        fh.write("".join(s[-1] for s in out["cell_type"]) + "\n")
    return out


def run(threads, suffix, record):
    if record:
        H.shuffle_meta = recording_shuffle
        for f in os.listdir(rec_dir):
            os.remove(os.path.join(rec_dir, f))
    else:
        H.shuffle_meta = _orig_shuffle
    res = cpdb_statistical_analysis_method.call(
        cpdb_file_path=db, meta_file_path=meta_fp, counts_file_path=counts_fp,
        counts_data="ensembl", output_path=os.path.join(tmp, "out"), iterations=ITER,
        threshold=0.1, threads=threads, debug_seed=-1, result_precision=3, pvalue=0.05,
        separator="|", output_suffix=suffix)
    perms = []
    if record:
        for f in sorted(os.listdir(rec_dir)):
            perms += open(os.path.join(rec_dir, f)).read().split()
    return res, perms


META_COLS = {"id_cp_interaction", "interacting_pair", "partner_a", "partner_b", "gene_a",
             "gene_b", "secreted", "receptor_a", "receptor_b", "annotation_strategy",
             "is_integrin", "rank"}


def pmatrix(res):
    df = res["pvalues"].set_index("interacting_pair")
    return df[[c for c in df.columns if c not in META_COLS]].astype(float).to_numpy()


# Child mode for part D: one analysis in a fresh process, p-matrix dumped to disk.
if os.environ.get("CPDB1_CHILD"):
    _res, _ = run(int(os.environ["CPDB1_THREADS"]), "child", False)
    np.save(os.environ["CPDB1_OUT"], pmatrix(_res))
    sys.exit(0)

import multiprocessing
print("cellphonedb", version("cellphonedb"), " python", sys.version.split()[0],
      " multiprocessing start method:", multiprocessing.get_start_method())
print("fixture: 30 cells, 3 cell types of 10 -> 30!/(10!)^3 = 5.55e12 distinct assignments")
print("iterations = %d, debug_seed = -1 (default, unseeded)\n" % ITER)

print("A/B. permutations the shipped code actually draws")
print("   %-8s %-9s %-10s %-10s %s" % ("threads", "workers", "drawn", "DISTINCT",
                                       "multiplicity histogram"))
for threads in (1, 2, 4, 8):
    _res, perms = run(threads, "A%d" % threads, True)
    cnt = collections.Counter(perms)
    hist = sorted(collections.Counter(cnt.values()).items())
    print("   %-8d %-9d %-10d %-10d %s"
          % (threads, len(os.listdir(rec_dir)), len(perms), len(cnt),
             ", ".join("%dx:%d" % (k, v) for k, v in hist)))
print("\n   Read the histogram as 'appeared k times: n permutations'. At threads=1 every draw"
      "\n   is unique; at threads=T most are drawn T times.")

# ---- C: two analyses in the SAME session reuse the same permutations -------------------------
# Nothing in the parent process consumes the global RNG when threads > 1 (all the shuffling
# happens in the children), so the parent's state at the second Pool() is the state it had at
# the first, and the children re-draw the same sequence. At threads=1 the shuffles run in the
# parent, which advances its state, so a second analysis draws fresh permutations.
print("\nC. two analyses run back to back in one session")
print("   %-8s %-22s %-22s %s" % ("threads", "distinct in run 1", "distinct in run 2",
                                  "shared between the runs"))
for threads in (1, 4):
    _r1, p1 = run(threads, "C1_%d" % threads, True)
    _r2, p2 = run(threads, "C2_%d" % threads, True)
    s1, s2 = set(p1), set(p2)
    print("   %-8d %-22d %-22d %d (%.0f%% of run 1)"
          % (threads, len(s1), len(s2), len(s1 & s2), 100 * len(s1 & s2) / len(s1)))
print("\n   At threads>1 a repeat analysis is not an independent replicate: it re-uses the same")
print("   permutations, so re-running does not average the Monte-Carlo error away.")

# ---- D: variance of the p-value estimator, across SEPARATE processes -------------------------
# Repeats must be separate processes: within one session (part C) the threads>1 runs are not
# independent. Each child re-invokes this script with CPDB1_CHILD set and dumps its p-matrix.
import subprocess
print("\nD. spread of the reported p-values over %d repeats run as SEPARATE processes" % NREP)
print("   %-26s %-12s %-16s %s" % ("configuration", "median sd", "effective n",
                                   "nominal iterations"))
for threads in (1, 4):
    mats = []
    for r in range(NREP):
        npy = os.path.join(tmp, "child_%d_%d.npy" % (threads, r))
        env = dict(os.environ, CPDB1_CHILD="1", CPDB1_THREADS=str(threads), CPDB1_OUT=npy,
                   CPDB1_TMP=tmp)
        subprocess.run([sys.executable, os.path.abspath(__file__)], env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        mats.append(np.load(npy))
    stack = np.stack(mats)
    pbar, sd = stack.mean(axis=0), stack.std(axis=0, ddof=1)
    live = (pbar > 0.05) & (pbar < 0.95)
    eff = pbar[live] * (1 - pbar[live]) / np.maximum(sd[live] ** 2, 1e-12)
    print("   %-26s %-12.5f %-16.0f %d"
          % ("threads=%d" % threads, np.median(sd[live]), np.median(eff), ITER))
print("\n   'effective n' is p(1-p)/var(p_hat): the number of independent permutations that")
print("   would produce the observed spread. At threads=4 it is about a quarter of the %d"
      % ITER)
print("   iterations the user asked for, which is what %d distinct permutations buys." % (ITER // 4))
H.shuffle_meta = _orig_shuffle
