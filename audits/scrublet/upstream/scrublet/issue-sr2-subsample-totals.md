# Total counts of UMI-subsampled synthetic doublets are inflated (`subsample_counts`)

_Plain issue: the repository has no issue template._

## Summary

With `synthetic_doublet_umi_subsampling < 1`, `helper_functions.subsample_counts`
thins the counts of the genes kept for scoring **first** and only then computes
`unsampled_orig_totals = original_totals - current_totals`. `current_totals` is already
thinned, so the counts just removed from the kept genes are drawn a second time. The
expected total per synthetic doublet is `rate * T + rate * (1 - rate) * F` (T = the
parents' full-gene total, F = their total over the kept genes) instead of `rate * T`.
`scrub_doublets` then normalises the synthetic doublets to 1e6 with these totals
(`scrublet.py:225`), so every synthetic doublet is scaled down relative to the observed
cells.

Default `synthetic_doublet_umi_subsampling=1.0` is not affected.

## Minimal reproduction

```python
import numpy as np, scipy.sparse
from scrublet.helper_functions import subsample_counts

rng = np.random.RandomState(0)
# 2000 doublets: 1000 counts in the genes kept for scoring, 4000 counts in all genes
E = scipy.sparse.csc_matrix(rng.multinomial(1000, np.full(50, 1 / 50), size=2000).astype(float))
_, totals = subsample_counts(E, 0.5, np.full(2000, 4000.0), random_seed=0)
print(totals.mean())   # expected 0.5 * 4000 = 2000
```

Expected: `2000` (± sampling noise). Got: `2250.3` — exactly
`0.5 * 4000 + 0.5 * 0.5 * 1000`.

Shrinking the example showed the discrepancy is independent of the data: any `E`, any
`original_totals >= E.sum(1)`, and the excess is always `rate * (1 - rate) * E.sum(1)`;
it vanishes when `original_totals - E.sum(1)` is taken before the thinning.

## Effect on results

On simulated counts with 150 labelled doublets among 1,650 cells, `scrub_doublets(
synthetic_doublet_umi_subsampling=0.8, use_approx_neighbors=False)` at `random_state=0`:
synthetic-doublet totals are 1.056× what they should be, the mean synthetic doublet
score rises by 0.047, the automatic threshold moves from 0.1701 (fixed) to 0.1876, and
one call flips (recall 0.980 vs 0.973). Small on this data, but systematic: every
synthetic doublet is shifted the same way.

## Fix

Measure the part of each total that `E` does not contain before thinning:

```python
totals_in_E = E.sum(1).A.squeeze()
E.data = np.random.binomial(np.round(E.data).astype(int), rate)
current_totals = E.sum(1).A.squeeze()
unsampled_orig_totals = original_totals - totals_in_E
```

Patch with a small pytest file: `0001-Fix-inflated-total-counts-of-UMI-subsampled-syntheti.patch`
(PR to follow).

## Environment

scrublet master `67f8ecb` and PyPI 0.2.3 (same source); Python 3.12.3, numpy 2.5.2,
scipy 1.18.1, scikit-learn 1.9.0, scikit-image 0.26.0, annoy 1.17.3.
