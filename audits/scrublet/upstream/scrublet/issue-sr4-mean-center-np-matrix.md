# `scrub_doublets(mean_center=True, normalize_variance=False)` raises `TypeError: np.matrix is not supported`

_Plain issue: the repository has no issue template._

## Summary

`pipeline_mean_center` computes `self._E_obs_norm - gene_means` where `_E_obs_norm` is a
`scipy.sparse.csc_matrix` and `gene_means` an `np.matrix` (the result of `.mean(0)`). The
difference is an `np.matrix`, and `pipeline_pca` hands it to
`sklearn.decomposition.PCA`, which refuses `np.matrix` input. The other three
combinations of `mean_center` / `normalize_variance` run: `pipeline_zscore` wraps the
same expression in `np.array(...)` and the two `normalize_variance`-only paths stay
sparse.

## Minimal reproduction

```python
import numpy as np, scipy.sparse, scrublet as scr

E = scipy.sparse.csc_matrix(np.random.RandomState(0).poisson(0.5, size=(300, 400)))
scr.Scrublet(E, random_state=0).scrub_doublets(mean_center=True, normalize_variance=False)
```

Expected: doublet scores. Got:

```
Traceback (most recent call last):
  File "issue.py", line 4, in <module>
    scr.Scrublet(E, random_state=0).scrub_doublets(mean_center=True, normalize_variance=False)
  File ".../scrublet/scrublet.py", line 237, in scrub_doublets
    pipeline_pca(self, n_prin_comps=n_prin_comps, random_state=self.random_state, svd_solver=svd_solver)
  File ".../scrublet/helper_functions.py", line 89, in pipeline_pca
    pca = PCA(n_components=n_prin_comps, random_state=random_state, svd_solver=svd_solver).fit(X_obs)
  File ".../sklearn/utils/validation.py", line 860, in check_array
    raise TypeError(
TypeError: np.matrix is not supported. Please convert to a numpy array with np.asarray. For more information see: https://numpy.org/doc/stable/reference/generated/numpy.matrix.html
```

Shrinking: any input reproduces it; only this option combination; the whole cause is
`type(scipy.sparse.csc_matrix(...) - np.matrix(...)) is np.matrix`. Reproduced with
scikit-learn 1.4.2, 1.5.2, 1.6.1, 1.7.2 and 1.9.0.

## Fix

```python
self._E_obs_norm = np.asarray(self._E_obs_norm - gene_means)
if self._E_sim_norm is not None:
    self._E_sim_norm = np.asarray(self._E_sim_norm - gene_means)
```

Patch with a small pytest file: `0002-Fix-TypeError-in-scrub_doublets-mean_center-True-nor.patch`
(PR to follow).

## Environment

scrublet master `67f8ecb` and PyPI 0.2.3 (same source); Python 3.12.3, numpy 2.5.2,
scipy 1.18.1, scikit-learn 1.9.0 (and the versions above), scikit-image 0.26.0.
