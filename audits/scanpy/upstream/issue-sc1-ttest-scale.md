Title: BUG: `rank_genes_groups(method="t-test", mean_in_log_space=False)` runs the t-test on exponentiated values

<!-- scverse/scanpy bug-report template fields -->

**Please make sure these conditions are met**
- [x] I have checked that this issue has not already been reported.
- [x] I have confirmed this bug exists on the latest version of scanpy. (1.12.3 and later; not in 1.11.x)
- [x] (optional) I have confirmed this bug exists on the main branch of scanpy. (`a656a33b`, 1.14.0.dev1)

**What happened?**

`mean_in_log_space` is documented as selecting how `logfoldchanges` is computed
("Whether to do log(mean(e^x)) (False) or log(e^mean(x)) (True)"), and the 1.13.0a1
release note describes it the same way. Since #4204 (1.12.3), however,
`compute_statistics` calls `_basic_stats(exponentiate_values=not mean_in_log_space,
need_var=True)` for the t-test methods, so the per-group means *and variances* that
`t_test` feeds to `scipy.stats.ttest_ind_from_stats` are computed on `expm1(X)`. With
`mean_in_log_space=False` the t-test therefore runs on linear-scale values, although
the function "expects logarithmized data". The `scores` and `pvals` change; the
`wilcoxon` methods are unaffected (ranks are always taken on `X`).

`ScanpyV1` defaults `mean_in_log_space=True`, so default calls are fine, but the
docstring recommends `False` as the "accurate" option, and `ScanpyV2Preview` defaults
to `False`, so `method="t-test"` under the v2 preset silently changes test.

`tests/test_rank_genes_groups.py::test_mean_in_log_space` only asserts
`logfoldchanges`, which is why this was not caught.

**Minimal code sample**

```python
import numpy as np
import scanpy as sc
from scipy import stats

adata = sc.datasets.pbmc68k_reduced()
raw = adata.raw.to_adata()  # log1p-normalized values
is_b = (raw.obs["bulk_labels"] == "CD19+ B").to_numpy()
X = raw.X.toarray() if hasattr(raw.X, "toarray") else raw.X
x_b, x_rest = X[is_b], X[~is_b]

welch_log = stats.ttest_ind(x_b, x_rest, equal_var=False).statistic
welch_lin = stats.ttest_ind(np.expm1(x_b), np.expm1(x_rest), equal_var=False).statistic

for mean_in_log_space in (True, False):
    sc.tl.rank_genes_groups(
        adata, "bulk_labels", groups=["CD19+ B"], method="t-test",
        n_genes=raw.n_vars, mean_in_log_space=mean_in_log_space,
    )
    df = sc.get.rank_genes_groups_df(adata, "CD19+ B").set_index("names").loc[raw.var_names]
    s = df["scores"].to_numpy()
    print(
        f"mean_in_log_space={mean_in_log_space}: "
        f"max |score - Welch on log1p| = {np.nanmax(np.abs(s - np.nan_to_num(welch_log))):.2g}, "
        f"max |score - Welch on expm1| = {np.nanmax(np.abs(s - np.nan_to_num(welch_lin))):.2g}"
    )
```

Output on `main`:

```
mean_in_log_space=True: max |score - Welch on log1p| = 5.1e-05, max |score - Welch on expm1| = 27
mean_in_log_space=False: max |score - Welch on log1p| = 27, max |score - Welch on expm1| = 4e-05
```

**Error output**

None (silent).

**Versions**

scanpy 1.14.0.dev1+ga656a33b0 (main @ a656a33b), anndata 0.12.x, numpy 2.x, scipy 1.x, Python 3.12.
Also reproduced on the 1.12.3 code path by reading the diff of #4204; 1.11.5 computes
`_basic_stats` on `X` only.

**Proposed fix**

Compute the test statistics on `X` and, when `mean_in_log_space=False`, the
exponentiated means for the fold change separately, as the `wilcoxon` branch already
does; add a test that `scores`/`pvals` are identical for both settings. Patch with test
and release-note fragment ready (PR to follow).
