Title: BUG: `score_genes` expression bins are not `n_bins` equal-frequency bins; the top bin holds 1–12 genes (or none)

<!-- scverse/scanpy bug-report template fields -->

**Please make sure these conditions are met**
- [x] I have checked that this issue has not already been reported.
- [x] I have confirmed this bug exists on the latest version of scanpy. (1.11.5; identical code in 1.4.6, 1.7.2, 1.9.1)
- [x] (optional) I have confirmed this bug exists on the main branch of scanpy. (`a656a33b`)

**What happened?**

`_score_genes_bins` assigns genes to expression bins with

```python
n_items = int(np.round(len(obs_avg) / (n_bins - 1)))
obs_cut = obs_avg.rank(method="min") // n_items
```

Ranks run 1..N, so bins `0 .. n_bins-2` hold `n_items` genes each and the last bin
holds whatever is left: `N - (n_bins-1)*n_items + 1` genes, i.e. between 1 and about
`n_bins/2` of the most highly expressed genes, or nothing at all when rounding goes the
other way (then there are only `n_bins-1` bins). The docstring says the function
reproduces Seurat's approach and that `n_bins` is the "number of expression level bins
for sampling"; Seurat's `AddModuleScore` uses `cut_number()`, i.e. `n_bins` bins of
`N/n_bins` genes each.

Consequence: a gene list containing any of the top handful of expressed genes (in PBMC
data: MALAT1, mitochondrial and ribosomal genes, B2M, TMSB4X, FTL/FTH1 — exactly what
"stress", "housekeeping" or ribosomal signatures contain) draws its matched controls
for that bin from at most a handful of genes, and a list made of those genes raises
`RuntimeError: No control genes found in any cut`. Lists that avoid the top handful of
genes are unaffected (I checked scores agree to three decimals with equal-frequency
bins).

Bin sizes from the formula:

| N genes | n_bins | genes per bin | genes in top bin |
|---|---|---|---|
| 2,000 | 25 | 83 | 9 |
| 18,000 | 25 | 750 | 1 |
| 20,000 | 25 | 833 | 9 |
| 25,000 | 25 | 1,042 | (no top bin: 24 bins) |
| 30,000 | 25 | 1,250 | 1 |
| 20,000 | 10 | 2,222 | 3 |

**Minimal code sample**

```python
import numpy as np
import pandas as pd
import scanpy as sc
from anndata import AnnData

rng = np.random.default_rng(0)
n_obs, n_vars = 500, 20_000
adata = AnnData(rng.lognormal(0, 1, (n_obs, n_vars)).astype(np.float32))
adata.var_names = [f"g{i}" for i in range(n_vars)]
avg = pd.Series(adata.X.mean(axis=0), index=adata.var_names).sort_values()

# bin sizes as computed inside _score_genes_bins (n_bins=25)
n_items = int(np.round(n_vars / 24))
obs_cut = avg.rank(method="min") // n_items
print(obs_cut.value_counts().sort_index().tail(3).to_dict())   # {22.0: 833, 23.0: 833, 24.0: 9}

top = list(avg.index[-9:])                # the 9 genes in the top bin
sc.settings.verbosity = 4
sc.tl.score_genes(adata, top[-5:], rng=0)  # "4 total control genes are used."
sc.tl.score_genes(adata, top, rng=0)       # RuntimeError: No control genes found in any cut.
```

**Error output**

```
RuntimeError: No control genes found in any cut. Try setting `ctrl_as_ref=False`.
```

(`ctrl_as_ref=False` raises the same error.)

**Versions**

scanpy 1.14.0.dev1+ga656a33b0 (main @ a656a33b) and 1.11.5; Python 3.12.

**Proposed fix**

```python
obs_cut = ((obs_avg.rank(method="first") - 1) * n_bins // len(obs_avg)).astype(int)
```

`n_bins` equal-frequency bins with ties broken by order, as `cut_number` does. Bin
membership changes for the top ~4 % of genes, so seeded control draws (and
`tests/_data/score_genes_reference_paul2015.pkl`, generated "using the same code")
change; a regression test on bin sizes is included. Patch ready (PR to follow).
