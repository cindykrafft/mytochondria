Title: BUG: `score_genes` expression bins are not `n_bins` equal-frequency bins; the top bin holds 1–12 genes (or none)

<!-- scverse/scanpy bug-report template fields -->

**Please make sure these conditions are met**
- [x] I have checked that this issue has not already been reported.
- [x] I have confirmed this bug exists on the latest version of scanpy. (executed on 1.12.4, the latest release; identical code in 1.11.5, 1.9.1, 1.7.2, 1.4.6)
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
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "scanpy@git+https://github.com/scverse/scanpy.git@main",
# ]
# ///
import numpy as np
import scanpy as sc
from anndata import AnnData

rng = np.random.default_rng(0)
adata = AnnData(rng.lognormal(0, 1, (100, 20_000)).astype(np.float32))  # synthetic, 20,000 genes
adata.var_names = [f"g{i}" for i in range(adata.n_vars)]
top9 = adata.var_names[np.argsort(adata.X.mean(axis=0))[-9:]]  # the 9 most-expressed genes

# Expected (n_bins=25): the top genes share an expression bin of 20000/25 = 800 genes,
# so 50 control genes are drawn for them. Got: the top bin holds only these 9 genes,
# 4 controls are used for five of them, and scoring all nine raises RuntimeError.
sc.settings.verbosity = 4
sc.tl.score_genes(adata, top9[-5:])  # logs "4 total control genes are used."
sc.tl.score_genes(adata, top9)       # RuntimeError: No control genes found in any cut.
```

**Error output**

```
    4 total control genes are used. (0:00:00)
Traceback (most recent call last):
  File "sc2.py", line 22, in <module>
    sc.tl.score_genes(adata, top9)       # RuntimeError: No control genes found in any cut.
  File ".../scanpy/tools/_score_genes.py", line 200, in score_genes
    raise RuntimeError(msg)
RuntimeError: No control genes found in any cut. Try setting `ctrl_as_ref=False`.
```

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
