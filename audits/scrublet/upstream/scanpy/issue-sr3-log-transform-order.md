# Bug report: `pp.scrublet(log_transform=True)` log-transforms observed and simulated cells on different scales, before the common normalisation

_Fields of `.github/ISSUE_TEMPLATE/bug-report.yml`._

**Please make sure these conditions are met**

- [x] I have checked that this issue has not already been reported.
- [x] I have confirmed this bug exists on the latest version of scanpy. (1.12.4)
- [x] (optional) I have confirmed this bug exists on the main branch of scanpy. (`a656a33b`)

**What happened?**

In `_run_scrublet`, when `log_transform=True`, `pp.log1p` is applied to `ad_obs` and
`ad_sim` *before* `pp.normalize_total(target_sum=1e6)`. At that point `ad_obs` has
already been `normalize_total`-ed to the median library size (for the HVG step) while
`ad_sim` holds raw summed counts, so the two populations are log-transformed on
different scales, and the 1e6 normalisation is then applied to log values. The original
Scrublet normalises both to 1e6 first and takes the log of both.

Consequence: a doublet simulated from a cell added to itself no longer coincides with
that cell (it must, under any common per-cell transform). With `log_transform=False`
the relative distance is 1e-7; with `log_transform=True` it is 0.08 on average and up to
0.19 on my data. On simulated counts with labelled doublets the damage to calls was
small (recall 0.94 vs 0.98), but every simulated doublet is displaced relative to the
observed cells, which is what the classifier measures.

**Minimal code sample**

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "scanpy@git+https://github.com/scverse/scanpy.git@main",
# ]
# ///
import numpy as np, scanpy as sc
from anndata import AnnData
from scipy import sparse

rng = np.random.default_rng(0)
counts = rng.poisson(np.outer(rng.lognormal(0, 0.4, 300), rng.gamma(0.5, 1.0, 600)))
adata = AnnData(sparse.csr_matrix(counts.astype(np.float32)))
adata.var_names = [f"g{i}" for i in range(adata.n_vars)]

# 1. the function's own preprocessing
auto = sc.pp.scrublet(adata, log_transform=True, use_approx_neighbors=False, copy=True, rng=0)

# 2. the same steps by hand, but normalise both populations first and log both
obs = adata.copy()
sc.pp.filter_genes(obs, min_cells=3); sc.pp.filter_cells(obs, min_genes=3)
obs.layers["raw"] = obs.X.copy()
sc.pp.normalize_total(obs)
logged = sc.pp.log1p(obs, copy=True); sc.pp.highly_variable_genes(logged)
obs = obs[:, logged.var["highly_variable"]].copy()
parents = auto.uns["scrublet"]["doublet_parents"]
sim = AnnData((obs.layers["raw"][parents[:, 0]] + obs.layers["raw"][parents[:, 1]]).astype(obs.X.dtype))
sim.var_names = obs.var_names; sim.obsm["doublet_parents"] = parents
del obs.layers["raw"]
sc.pp.normalize_total(obs, target_sum=1e6); sc.pp.normalize_total(sim, target_sum=1e6)
sc.pp.log1p(obs); sc.pp.log1p(sim)
manual = sc.pp.scrublet(obs, adata_sim=sim, use_approx_neighbors=False, copy=True, rng=0)

np.testing.assert_allclose(manual.obs["doublet_score"], auto.obs["doublet_score"], atol=1e-15, rtol=1e-15)
```

Expected: identical scores, as `test_scrublet_data` already asserts for
`log_transform=False`. Got:

```
AssertionError:
Not equal to tolerance rtol=1e-15, atol=1e-15
Mismatched elements: 278 / 300 (92.7%)
Max absolute difference among violations: 0.25531774
```

Shrinking: with `log_transform=False` the two agree to 1e-15; moving the two `log1p`
calls in `_run_scrublet` below the two `normalize_total(target_sum=1e6)` calls makes
them agree with `log_transform=True` as well, so the order is the whole cause.

**Error output**

(above)

**Versions**

<details>

```
# audit venv, scanpy main @ a656a33b (print_versions/print_header emit nothing at default verbosity; from importlib.metadata)
Python 3.12.3 (Linux-6.18.44-fc-v24-x86_64-with-glibc2.39)
scanpy         1.14.0.dev1+ga656a33b0
anndata        0.13.3.post0
numpy          2.5.2
scipy          1.18.1
scikit-learn   1.9.0
pynndescent    0.6.0
scikit-image   0.26.0
annoy          1.17.3
pandas         3.0.5
numba          0.67.0
```

</details>

**Proposed fix** (PR to follow): normalise both to 1e6, then `log1p` both, as in the
original; regression test on counts generated in the test.
