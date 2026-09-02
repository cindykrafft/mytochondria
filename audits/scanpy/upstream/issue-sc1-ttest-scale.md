Title: BUG: `rank_genes_groups(method="t-test", mean_in_log_space=False)` runs the t-test on exponentiated values

<!-- scverse/scanpy bug-report template fields -->

**Please make sure these conditions are met**
- [x] I have checked that this issue has not already been reported.
- [ ] I have confirmed this bug exists on the latest version of scanpy. (NOT in 1.12.4, the latest stable release; present in 1.13.0a1/a2 pre-releases and main)
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
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "scanpy@git+https://github.com/scverse/scanpy.git@main",
#   "scipy",
# ]
# ///
import numpy as np
import scanpy as sc
from scipy import stats

adata = sc.datasets.pbmc68k_reduced()  # bundled; .raw holds log1p-normalized values
scores = {}
for mean_in_log_space in (True, False):
    sc.tl.rank_genes_groups(
        adata, "bulk_labels", groups=["CD19+ B"], reference="rest",
        method="t-test", n_genes=adata.raw.n_vars, mean_in_log_space=mean_in_log_space,
    )
    df = sc.get.rank_genes_groups_df(adata, "CD19+ B").set_index("names")
    scores[mean_in_log_space] = df.loc[adata.raw.var_names, "scores"].to_numpy()

# Expected: identical t statistics (the parameter is documented as a fold-change option).
# Got on main: they differ by up to ~27, and the mean_in_log_space=False values equal
# Welch's t computed on expm1(X), i.e. the test ran on linear-scale values.
X = adata.raw.X.toarray()
is_b = (adata.obs["bulk_labels"] == "CD19+ B").to_numpy()
welch_on_expm1 = stats.ttest_ind(np.expm1(X[is_b]), np.expm1(X[~is_b]), equal_var=False).statistic
print("max |t(True) - t(False)|        =", np.nanmax(np.abs(scores[True] - scores[False])))
print("max |t(False) - Welch on expm1| =", np.nanmax(np.abs(scores[False] - np.nan_to_num(welch_on_expm1))))
np.testing.assert_allclose(scores[True], scores[False], atol=1e-3)
```

**Error output**

```
max |t(True) - t(False)|        = 26.637714
max |t(False) - Welch on expm1| = 4.005432e-05
Traceback (most recent call last):
  File "sc1.py", line 30, in <module>
    np.testing.assert_allclose(scores[True], scores[False], atol=1e-3)
AssertionError:
Not equal to tolerance rtol=1e-07, atol=0.001
(on 1.12.4 the same script prints max |t(True) - t(False)| = 0.0 and exits cleanly)
```

**Versions**

scanpy 1.14.0.dev1+ga656a33b0 (main @ a656a33b), anndata 0.12.x, numpy 2.x, scipy 1.x, Python 3.12.
Executed on 1.12.4 (latest release): the t-test stays on the log values for both settings (1.12.x
accepts `mean_in_log_space` only via `**kwds`). Executed on 1.13.0a2: affected. 1.11.5 has no such parameter.

**Proposed fix**

Compute the test statistics on `X` and, when `mean_in_log_space=False`, the
exponentiated means for the fold change separately, as the `wilcoxon` branch already
does; add a test that `scores`/`pvals` are identical for both settings. Patch with test
and release-note fragment ready (PR to follow).
