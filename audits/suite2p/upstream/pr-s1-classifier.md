# PR: Classifier: keep feature values at the training minimum in the first bin

**Target:** `MouseLand/suite2p`, base `main`; branch `fix/classifier-bin-clip`
**Patch:** `0001-Classifier-keep-feature-values-at-the-training-minim.patch`

## Title

```
Classifier: keep feature values at the training minimum in the first bin
```

## Body

```markdown
`Classifier._get_logp` clamps each feature to the training range and bins it with `np.digitize(x, grid, right=True) - 1`. For `x == grid[0]` — every value at or below the training minimum, and NaNs, which are set to `grid[0]` — `digitize` returns 0, so the bin index is -1 and the probability of the *last* bin is used. With the builtin classifier, a ROI whose skew is below the training minimum is scored with the highest-skew bin (P(cell) 0.986 instead of 0.535); `compact` and `npix_norm` wrap the same way.

This clips the bin index to the valid range. On the builtin classifier's own training set 0.4 % of ROIs are at a feature minimum and no 0.5-threshold verdict changes; user-trained classifiers, fit on far fewer ROIs, hit their minima more often. Reproduction: https://github.com/cindykrafft/mytochondria/blob/main/audits/suite2p/verify/s1_classifier_bins.py

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
```
