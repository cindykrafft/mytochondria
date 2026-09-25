Title: PCA's `covariance_eigh` solver (the `auto` choice for tall dense data since 1.5) loses the variance of features with a common offset: 33 % off for float32 values around 100, 1.7 % off for float64 values around 1e6

_**Not for pasting as is.** Bug-report template fields. The project's Automated Contributions Policy asks that issue text not be AI-generated: the reproducer, numbers and analysis below are the facts to write from; the prose is to be written by the submitter in their own words (see `README.md` § How to file)._

**Introduce yourself**

(the submitter, in their own words: volunteer project checking the numerical core of research software used in published papers, every finding verified by execution; scikit-learn is named in 322 papers of the survey cohort, PCA in 55 of them)

**Describe the bug and give evidence about its user-facing impact**

Since 1.5 (#27491) `svd_solver="auto"` selects `covariance_eigh` for dense input with `n_features <= 1000` and `n_samples >= 10 * n_features`, and that solver forms the covariance as `X.T @ X - n_samples * mean ⊗ mean` (`sklearn/utils/_array_api.py::_cov`, called from `PCA._fit_full`). When the features share a common offset the two terms are nearly equal and the variance is lost to cancellation. The `full` solver, which `auto` chose up to 1.4, centres the data first and is not affected.

Measured on a 20,000 × 5 matrix with unit-scale variation (harness in the linked audit), relative error of `explained_variance_` against the exact centred eigendecomposition:

| dtype | values around | `covariance_eigh` (= `auto`) | `full` |
|---|---|---|---|
| float32 | 1e2 | 3.3e-01 | 3.8e-06 |
| float32 | 1e3 | 8.7e-01 (ratio 5.4e-01) | 2.4e-06 |
| float32 | 1e4 | 4.5e+01 (ratio 1.0) | 2.2e-04 |
| float64 | 1e4 | 1.0e-06 | 4.7e-15 |
| float64 | 1e6 | 1.7e-02 | 1.0e-12 |
| float64 | 1e7 | 2.0e-01 (PC1 scores 3.5e-02) | 3.8e-12 |
| float64 | 1e8 | 8.0e+00 (ratio 1.0, PC1 scores 3.7e-01) | 1.4e-10 |

Data like this is ordinary: float32 intensities or counts in the hundreds, timestamps, genomic coordinates, instrument readings with a baseline. Users do not choose the solver, `auto` does, and nothing warns. The docstring says the solver "effectively doubles the condition number", which describes the eigendecomposition of a well-centred covariance, not this loss, which is governed by mean²/variance and is already 33 % at a ratio of 1e4 in float32.

**Steps/Code to Reproduce**

```python
import numpy as np
from sklearn.decomposition import PCA

rng = np.random.RandomState(0)
X = rng.standard_normal((20000, 5)) @ rng.standard_normal((5, 5))
ref = PCA(svd_solver="full").fit(X)                      # offset-free reference
for dtype, offsets in ((np.float32, [1e2, 1e3]), (np.float64, [1e6, 1e8])):
    for offset in offsets:
        Xo = (X + offset).astype(dtype)
        for solver in ["auto", "full"]:
            pca = PCA(svd_solver=solver).fit(Xo)
            dev = np.abs(pca.explained_variance_ / ref.explained_variance_ - 1).max()
            print(f"{dtype.__name__} offset {offset:.0e} svd_solver={solver!r:8} -> {pca._fit_svd_solver:16}"
                  f" explained_variance_ratio_[0] = {pca.explained_variance_ratio_[0]:.4f}"
                  f" max relative deviation of explained_variance_ from the offset-free fit: {dev:.1e}")
```

**Expected Results**

Every line within ~1e-4 (float32) or ~1e-10 (float64) of the offset-free fit, as the `full` lines are, since `explained_variance_ratio_[0]` is 0.5298 for this data whatever the offset.

**Actual Results**

```
float32 offset 1e+02 svd_solver='auto'   -> covariance_eigh  explained_variance_ratio_[0] = 0.4718 max relative deviation of explained_variance_ from the offset-free fit: 2.6e-01
float32 offset 1e+02 svd_solver='full'   -> full             explained_variance_ratio_[0] = 0.5298 max relative deviation of explained_variance_ from the offset-free fit: 6.2e-07
float32 offset 1e+03 svd_solver='auto'   -> covariance_eigh  explained_variance_ratio_[0] = 0.9975 max relative deviation of explained_variance_ from the offset-free fit: 1.0e+00
float32 offset 1e+03 svd_solver='full'   -> full             explained_variance_ratio_[0] = 0.5298 max relative deviation of explained_variance_ from the offset-free fit: 4.6e-04
float64 offset 1e+06 svd_solver='auto'   -> covariance_eigh  explained_variance_ratio_[0] = 0.5295 max relative deviation of explained_variance_ from the offset-free fit: 2.2e-02
float64 offset 1e+06 svd_solver='full'   -> full             explained_variance_ratio_[0] = 0.5298 max relative deviation of explained_variance_ from the offset-free fit: 7.1e-13
float64 offset 1e+08 svd_solver='auto'   -> covariance_eigh  explained_variance_ratio_[0] = 0.9101 max relative deviation of explained_variance_ from the offset-free fit: 1.2e+01
float64 offset 1e+08 svd_solver='full'   -> full             explained_variance_ratio_[0] = 0.5298 max relative deviation of explained_variance_ from the offset-free fit: 1.8e-10
```

(1.9.1, numpy 2.4.6; the same on 1.5.2; on 1.3.2 `auto` selects `full` and every line agrees with the reference.)

**Versions**

```
System:
    python: 3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0]
   machine: Linux-6.18.44-x86_64-with-glibc2.39

Python dependencies:
      sklearn: 1.9.1
        numpy: 2.4.6
        scipy: 1.17.1
       joblib: 1.6.0
threadpoolctl: 3.7.0
     narwhals: 2.26.0

Built with OpenMP: True
BLAS: scipy_openblas 0.3.31, 4 threads
```

**Interest in fixing the bug**

Yes. Root cause: the post-hoc centering `X.T @ X - n * mean ⊗ mean` in `_fit_full`'s `covariance_eigh` branch. A fix that keeps the solver's memory footprint (no full centred copy of `X`) is to accumulate `(X[batch] - mean).T @ (X[batch] - mean)` over row batches (`gen_batches` / `get_chunk_n_rows`, as `pairwise_distances_chunked` does) for dense input and keep the post-hoc formula for sparse input, which cannot be centred without densifying. With that change every line above is within 5e-6 (float32) / 4e-10 (float64) of the reference, the whole `test_pca.py` passes, and a regression test at float64 offsets 1e6 / 1e8 and float32 offsets 1e2 / 1e3 fails on the current code and passes with the change. Happy to open the PR once this is triaged.

---
_Generated by [Claude Code](https://claude.ai/code)_
