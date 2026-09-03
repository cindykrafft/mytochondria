"""SR4: `scrub_doublets(mean_center=True, normalize_variance=False)` crashes
in the original package with current scikit-learn: `pipeline_mean_center`
subtracts an `np.matrix` of gene means from the sparse matrix, which yields an
`np.matrix`, and `sklearn.decomposition.PCA` rejects `np.matrix` input.
The other three combinations run. Scanpy's port converts to CSC after the
subtraction and does not crash.

Run in a venv with scrublet and scanpy installed:  python sr4_mean_center_np_matrix.py
"""

from __future__ import annotations

import importlib.metadata as md
import io
import sys
import traceback
import warnings
from contextlib import redirect_stdout

import numpy as np
import scipy.sparse as sp

warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from synth import make_counts  # noqa: E402

import scrublet as scr  # noqa: E402

print("scrublet", md.version("scrublet"), "| scikit-learn", md.version("scikit-learn"), "| numpy", md.version("numpy"))

X, _, _ = make_counts(n_singlets=400, n_doublets=40, n_genes=800)
for mc, nv in [(True, True), (True, False), (False, True), (False, False)]:
    s = scr.Scrublet(X, random_state=0)
    try:
        with redirect_stdout(io.StringIO()):
            scores, pred = s.scrub_doublets(mean_center=mc, normalize_variance=nv, use_approx_neighbors=False, verbose=False)
        print(f"mean_center={mc!s:5} normalize_variance={nv!s:5}: OK   (_E_obs_norm is {type(s._E_obs_norm).__name__}, {len(scores)} scores)")
    except Exception:  # noqa: BLE001
        print(f"mean_center={mc!s:5} normalize_variance={nv!s:5}: FAIL (_E_obs_norm is {type(s._E_obs_norm).__name__})")
        tb = traceback.format_exc().strip().splitlines()
        print("   " + "\n   ".join(tb[-6:]))

print("\nminimal reproduction of the type: csc_matrix - np.matrix ->", type(sp.csc_matrix(np.eye(3)) - np.matrix(np.ones((1, 3)))).__name__)

try:
    import anndata as ad
    import scanpy as sc

    sc.settings.verbosity = 0
    a = ad.AnnData(sp.csr_matrix(X)); a.var_names = [f"g{i}" for i in range(X.shape[1])]
    sc.pp.scrublet(a, mean_center=True, normalize_variance=False, use_approx_neighbors=False, random_state=0)
    print(f"scanpy {md.version('scanpy')} sc.pp.scrublet(mean_center=True, normalize_variance=False): OK, threshold {a.uns['scrublet'].get('threshold', float('nan')):.4f}")
except Exception as e:  # noqa: BLE001
    print("scanpy port:", type(e).__name__, e)
