# m1_boxplot_violin_stats: notes

Harness: `audits/matplotlib/verify/m1_boxplot_violin_stats.py`. Outputs:
- `m1_boxplot_violin_stats.out`: main overlay. This is matplotlib 3.11.2 with main @ 44f2e00's `cbook.py`, `mlab.py`,
  `colors.py`, `colorizer.py`, `contour.py`, `stackplot.py` and `axes/_axes.py` copied in, on numpy 2.5.3 and scipy 1.18.1.
  A full build of main is not possible here because the download of its SheenBidi dependency is blocked.
- `.v3.11.2.out`: 3.11.2, numpy 2.5.3, scipy 1.18.1.
- `.v3.7.1.out`: numpy 1.26.4, no scipy.
- `.v3.5.2.out`: numpy 1.23.5, no scipy.

The harness takes about 9 s per build. For this group, the code in 3.11.2 is identical to main: `boxplot_stats`,
`violin_stats`, `_reshape_2D`, `delete_masked_points`, `GaussianKDE`, `boxplot`, `bxp`, `violinplot` and `violin` show no
diff. That is why the main and 3.11.2 outputs are line-for-line the same.

Truths:
- `fractions.Fraction` for means, Hyndman & Fan type-7 percentiles, IQR, fences, whiskers and fliers, sample
  variances and covariances (ddof=1), and the `linspace` grids (min + k·(max−min)/(P−1)).
- The notch formula med ± 1.57·IQR/√N from the Notes section.
- A plain-Python percentile bootstrap of the median. Its resample indices come from numpy's global RNG with the same
  seed, so the resamples are the same ones matplotlib draws. The medians and the 2.5/97.5 percentiles are then computed
  exactly.
- The KDE as a direct `math.fsum` of Gaussian kernels, in 1-D and in 2-D (with the 2×2 inverse done by formula).
- Scott n^(−1/(d+4)) and Silverman (n(d+2)/4)^(−1/(d+4)).
- `scipy.stats.gaussian_kde` only as an informational cross-check (main and 3.11.2 only).

The quartile method: the docstrings say only "first quartile (25th percentile)". The code calls `np.percentile` with
its default 'linear' method (H&F type 7, cbook.py:1307). The harness uses H&F-7 as the truth and records Tukey's hinges
as information only (for n=8, H&F-7 gives Q1=2.75 where Tukey's hinge is 2.5).

The expectations depend on the version:
- Masked points are ignored by `boxplot_stats` from 3.9 on (api_changes_3.9.0/behaviour.rst, "Boxplots now ignore
  masked data points").
- Masked and non-finite values are ignored by `violin_stats`/`violinplot` from 3.11 on (api_changes_3.11.0/behavior.rst).
- The `("GaussianKDE", bw_method)` method tuple and its default are 3.11+.
- `side=` is 3.9+, and `orientation=` is 3.10+ (`vert=False` is used before that).

## Counts

| build | ok | FAIL |
|---|---|---|
| main overlay (3.11.2 + main files) | 164 | 12 |
| 3.11.2 | 164 | 12 |
| 3.7.1 | 144 | 6 |
| 3.5.2 | 142 | 8 |

The old builds run fewer checks for three reasons: the 3.9 and 3.11 features become information lines there, scipy is
absent, and `side=` does not exist.

## FAIL lines

### 1–2. A datum exactly on a fence is a whisker end, not a flier (all builds; documentation wording)

These lines fail:
- `datum exactly on the upper fence: 'the upper whisker at the highest datum below Q3 + whis*(Q3-Q1)'`
- `... lower fence: 'the lower whisker is at the lowest datum above Q1 - whis*(Q3-Q1)'`

The data are [−2, 1, 2, 3, 6], so Q1=1, Q3=3, IQR=2, and both fences fall exactly on data (−2 and 6). Taken literally,
"highest datum below" / "lowest datum above" puts the whiskers at 3 and 1 and makes −2 and 6 fliers. matplotlib uses
inclusive fences: cbook.py:boxplot_stats has `wiskhi = x[x <= hival]` (1329) and `wisklo = x[x >= loval]` (1336), so it
gives whiskers at −2 and 6 and no fliers.

The Axes.boxplot summary says "the farthest data point lying within 1.5x the IQR from the box" (_axes.py:4381–4382).
That wording is inclusive, matches the code, and its check passes. Tukey's convention is also inclusive.

Verdict: **documentation gap (wording)**. The `whis` parameter text in cbook.py:1166–1168 and _axes.py:4430–4432 should
say "at or above" / "at or below". The same text and code appear in all four builds. This only matters when a datum
sits exactly on a fence.

### 3–4. Whiskers are clamped to the box edge, so a whisker end can be a non-datum (all builds; undocumented behaviour)

These lines fail:
- `upper whisker is a datum: 'the upper whisker at the highest datum below Q3 + whis*(Q3-Q1)'`
- `whis=0.25 (float: ...): mean/q1/.../whislo/whishi/... = documented definitions`

For the first line the data are [0,0,0,0,0,0,10,10], so Q1=0, Q3=2.5 and the upper fence is 6.25. The highest datum
≤ 6.25 is 0, which lies inside the box. matplotlib reports `whishi = 2.5`, which is Q3 and not a datum.

For the second line the data are [1,2,4,4,6,8,10,30] with whis=0.25, so the fences are 2.25 and 9.75. The data inside
are 4…8. matplotlib reports whiskers at Q1=3.5 and Q3=8.5 instead of 4 and 8.

The cause is in cbook.py:boxplot_stats (1330–1340):

```
if len(wiskhi) == 0 or np.max(wiskhi) < q3:
    stats['whishi'] = q3
...
if len(wisklo) == 0 or np.min(wisklo) > q1:
    stats['whislo'] = q1
```

The fliers are the same under both readings (1, 2, 10, 30), so only the whisker ends differ. Clamping gives a
zero-length whisker instead of one drawn back into the box, which is a sensible drawing choice. But the docstring
promises "the highest datum below Q3 + whis*IQR", and `whislo`/`whishi` are returned to users and to seaborn as numbers.

Verdict: **documentation gap**. The clamp is deliberate but not documented: the returned whisker end can be Q1/Q3
rather than a datum. It occurs when the data are sparse between a quartile and its fence (small n, ties, or small
`whis`). Same on all builds.

### 5. `whis=(5, 95)`: whiskers sit at the most extreme datum inside the percentiles, not at the percentiles (all builds; documentation imprecise)

This line fails: `whis=(5, 95) on 1..20: 'they indicate the percentiles at which to draw the whiskers'`. The literal
reading is P5=1.95 and P95=19.05. matplotlib gives 2 and 19.

For a pair, the code computes `loval, hival = np.percentile(x, whis)` (cbook.py:1321) and then applies the same datum
search as for a float, including the clamp described in FAILs 3–4. So the whisker ends at the most extreme datum within
[P5, P95]. The companion check, which uses exactly that reading, passes, and so do the (10, 90) and (2.5, 97.5) checks
on n=104.

The fliers are the same under both readings. Only the whisker end moves, by less than one datum gap.

Verdict: **documentation gap**. "the percentiles at which to draw the whiskers" should say "the whiskers extend to the
most extreme data within these percentiles". Same on all builds.

### 6. `+inf` next to a quartile turns Q3, the IQR and the upper whisker into NaN, and the box loses its outlier (all builds; wrong numbers, numpy root cause)

This line fails: `+inf as the 5th of 5 values: Q3 = 4 (H&F-7 index exactly 3, weight 0 on the inf)`. The data are
[1,2,3,4,inf]. H&F-7 gives Q3 = y[3] + 0·(y[4]−y[3]) = 4.

matplotlib returns:
- `q3=nan`, `iqr=nan`, `whishi=nan`;
- `fliers=[1.0]`, so the finite value 1 is wrongly called an outlier and the +inf value is missing.

The cause is `q1, med, q3 = np.percentile(x, [25, 50, 75])` (cbook.py:1307). numpy's `_lerp` computes
`a + (b−a)·t` = `4 + inf·0` = NaN (see the numpy audit, n11 FAIL 1–12). Then `loval = q1 − whis·nan` is NaN,
`x[x >= nan]` is empty, `whislo` falls back to Q1 = 2, and `x < 2` flags 1 as a flier.

When +inf is not next to a quartile index ([1..8, inf]), every statistic is correct and +inf is reported as a flier.
That check passes. boxplot_stats documents no handling of non-finite values.

Verdict: **bug: wrong numbers vs the documented definition**. The root cause is in numpy. The reader sees a box with no
upper whisker or upper edge and a spurious low outlier. All four builds are affected (numpy 1.23.5 through 2.5.3).

### 7–12. `violin_stats` / `violinplot` do not ignore masked values, despite the 3.11 release note and docstrings (main overlay and 3.11.2; bug)

These lines fail:
- `1D masked array, 3 masked incl. +-50 ('Non-finite and masked values are ignored', 3.11)`: coords, vals,
  mean/median/min/max, and quantiles (4 lines);
- `list of masked arrays: masked values ignored`;
- `Axes.violinplot(masked array): 'Non-finite and masked values are ignored'`.

The input is 40 clean values plus 50.0, −50.0 and 3.3, all three masked. matplotlib returns:
- `min=-50`, `max=50`, a mean of −0.1167 (clean: −0.2079), a median of 0.0403 (clean: 0.0352), and quantiles
  [−0.9021, 0.5390] (clean: [−0.9008, 0.4050]);
- a grid from −50 to 50 and a KDE built on all 43 values;
- for a list of masked arrays, a second violin with max 99 where the masked 99 should be excluded;
- in `Axes.violinplot`, the max line drawn at 50.

The cause is in cbook.py:violin_stats (1591–1592):

```
x = np.asarray(x)
x, = delete_masked_points(x)
```

`np.asarray` drops the mask of a `MaskedArray` before `delete_masked_points` can see it. `_reshape_2D` itself keeps the
masked array (1D: `return [X]`; list: `np.asanyarray(xi)`). `delete_masked_points` then removes only NaN and inf, which
is why the NaN/±inf checks pass.

The docs say the opposite of what happens:
- the `violin_stats` docstring: "Non-finite and masked values are ignored" (cbook.py:1502);
- the `violinplot` docstring (_axes.py:9004);
- api_changes_3.11.0/behavior.rst: "now ignore masked and non-finite (NaN and inf) values".

Using `np.asanyarray` (or nothing) would fix it.

Verdict: **bug: wrong numbers vs the documented behaviour**, in main and 3.11.2.

The older builds are worse for the body but better for some lines. In 3.7.1 and 3.5.2 the masked array reaches `np.min`,
`np.max` and `np.mean`, which respect the mask, so the min, max and mean lines were right. But `np.median` and
`np.percentile` ignore the mask: the median is 0.0403 and the quantiles are wrong, and numpy warns "'partition' will
ignore the 'mask'". The KDE `vals` came back fully masked (100/100), which leaves the body undefined. These are info
lines in those `.out` files, because those versions did not document masked handling.

So 3.11 changed which numbers go wrong. It did not deliver the "ignore masked" promise: the min and max lines of a
masked violin moved from correct (3.7.1) to wrong (3.11.2 and main).

### 3.5.2 only: empty input has no `'iqr'` key (2 lines; bug fixed later)

These lines fail: `empty input []` and `empty input np.array([])`, which check that every documented key is present.
The 3.5.2 empty branch (matplotlib/cbook/__init__.py:1178–1189) sets `med` twice and never sets `iqr`, although the
Returns table lists `iqr`. 3.7.1 sets `stats['iqr'] = np.nan`, and so does main (cbook.py:1292).

Verdict: **bug, fixed by 3.7.1**. Code that reads `stats['iqr']` raises a KeyError on an empty dataset in 3.5.2.

## What held up

boxplot_stats on all four builds:
- mean, Q1, median, Q3, IQR, whiskers, notch and fliers equal the documented definitions exactly (H&F-7 quartiles,
  inclusive fences) for odd n=7 with ties and negatives, even n=8 with an outlier, n=1, n=2, n=3, negative data with
  outliers on both sides, a random n=104 sample, data offset by 1e9 (rel 1e-12), int64 input, and float32 input (rel
  2e-6).
- Integer input returns float quartiles: Q1=2.5 is not truncated.
- For float32 input the whisker ends are exact data values.
- For whis=3.0, whis=5.0 and whis=inf the whiskers and fliers follow the fence rule. whis=inf gives min/max and no
  fliers.
- The fliers for whis=0.25 are the data beyond the whiskers.
- whis='range' is rejected with ValueError.
- whis=(0, 100) gives whiskers at the min and max with no fliers.
- whis=(5, 95), (10, 90) and (2.5, 97.5) put the whiskers at the most extreme data inside the percentile interval, and
  the fliers are the data outside it.
- With Q1==Q3 and autorange=False: IQR is 0, the whiskers are at the quartile, and the two extremes are fliers.
- autorange=True moves the whiskers to the min and max as documented, and only for the dataset whose IQR is 0.
- The asymptotic notch equals med ± 1.57·IQR/√N for n = 5, 16 and 401.
- bootstrap=500 and bootstrap=2000 give exactly the 2.5th and 97.5th H&F-7 percentiles of the resampled medians, which
  is a percentile-method 95% CI of the median. Results are reproducible under `np.random.seed`. The draw advances
  numpy's global RNG, a side effect recorded as info.
- A list of four datasets of different lengths gives four dicts in order, each equal to its own truth.
- `labels` are attached per dataset, and labels of the wrong length raise ValueError.
- A 2-D array is split by column.
- Empty input gives all-NaN stats and empty fliers (3.7.1+; see the 3.5.2 FAIL), and one empty dataset does not
  disturb the others.
- From 3.9 on, masked points are ignored in 1-D masked arrays, 2-D masked arrays (per column) and lists of masked
  arrays.
- +inf away from the quartile indices is reported as a flier and leaves the other statistics correct.

Axes.boxplot / bxp on all builds, with the drawn line data compared to the independent truth:
- The median line y is [med, med] and the box y is [q1, q1, q3, q3, q1].
- The whiskers run q1→whislo and q3→whishi, and the caps sit at whislo and whishi.
- The flier y values are exactly the data beyond the whiskers, drawn at x equal to the box position.
- The showmeans marker and the meanline line sit at the exact mean.
- Boxes are centred on the default positions 1..N and on custom positions [2, 5, 9], and the fliers follow custom
  positions.
- The notched outline passes through cilo, med and cihi = med ∓ 1.57·IQR/√N in the documented vertex order.
- usermedians forces only the chosen median.
- conf_intervals places the notch at the given (2.0, 6.5).
- Horizontal boxplots carry the same statistics on x.
- boxplot(bootstrap=1000, notch=True) draws the notch at the ported bootstrap CI.
- autorange=True and whis=(0, 100) draw the caps at the min and max.
- From 3.9 on, masked points are neither used nor drawn.

mlab.GaussianKDE on all builds:
- The default factor is Scott's n^(−1/5) for n = 7, 40 and 300, and 'silverman' gives (3n/4)^(−1/5).
- The covariance is the ddof=1 sample variance × factor², the same as scipy's.
- `evaluate` equals the direct sum of Gaussians to about 1e-15 in both code branches (loop over data, loop over
  points), for Scott and Silverman.
- On main and 3.11.2, `evaluate` equals `scipy.stats.gaussian_kde` (informational).
- The estimated pdf integrates to 1 within 1e-6.
- Scalar bw_method 0.3, 1 and 2.5 are used directly as the factor (h = factor·sd).
- A callable bw_method gives the factor it returns, and the misspelled string 'scot' raises ValueError.
- float32 data (rel 1e-6) and data offset by 1e6 (rel 1e-7) evaluate correctly.
- In 2-D, the factor is n^(−1/6), the covariance matrix is the ddof=1 matrix × factor², and the density equals a direct
  sum of bivariate Gaussians.
- In 3-D, Silverman's factor is (5n/4)^(−1/7).

violin_stats on all builds:
- `coords` = linspace(min, max, points) for points = 100 and points = 7.
- `vals` equals the direct-sum KDE for Scott (n = 2, 11, 23 and 150, covering both evaluate branches), for Silverman and
  for bw=0.25.
- mean, median, min and max are exact.
- Quantiles are H&F-7, including q=0.07 and per-dataset quantile lists of different lengths.
- Integer input works, and a 2-D array is split by column.
- A callable `method(data, coords)` receives the grid and its output is returned as-is.
- Constant data and n=1 do not raise, and give mean = median = min = max = the value.

3.11+ only:
- The default method and the ("GaussianKDE", callable) form work, and an unknown KDE name raises ValueError.
- NaN and ±inf are ignored in every returned statistic and in the KDE.
- Empty and all-NaN datasets give NaN statistics and empty grids without disturbing the other datasets.

Axes.violinplot / violin on all builds:
- The cmeans, cmedians, cmins and cmaxes segments sit at the exact statistics and span pos ± widths/4.
- The cbars run from min to max at x = pos.
- cquantiles has one segment per requested quantile at its H&F-7 value, with the widths repeated per violin.
- Each body outline passes through pos ± 0.5·widths·kde/max(kde) at every grid point, using the KDE truth (worst vertex
  distance about 1e-15). The maximum full width equals `widths` (0.5, 1.2 and 0.8).
- The horizontal violin, bw_method='silverman', and bw_method=0.2 with points=31 also hold.
- Constant data and n=1 draw without error, with their lines at the value.

3.9+ only: side='low' and side='high' draw a half-violin of half the width, with the mean line from pos − w/4 to pos or
from pos to pos + w/4.

3.11+ only: NaN and ±inf are ignored in the drawn min, max and median lines.

## Not checked, or observed without a documented rule

- **NaN in boxplot data.** No docstring says what happens. Observed on every build: one NaN makes mean, Q1, median, Q3,
  IQR, the notch and both whiskers NaN, and the fliers come back empty. The box silently disappears. In contrast,
  violin_stats documents (3.11+) and implements dropping NaN. Recorded as info. This is a documentation gap worth
  raising, but there is no documented truth to FAIL against.
- **Constant data and n=1 in violins.** `_kde_method` returns the indicator `(x[0] == coords).astype(float)` (cbook.py:1565)
  rather than a density, so the body is a zero-height line of full width. This is undocumented and recorded as info.
  `mlab.GaussianKDE` itself raises `LinAlgError: Singular matrix` for constant data and `ValueError` for n=1, also
  undocumented and recorded as info.
- **usermedians and the notch.** With usermedians, the notch stays centred on the computed median rather than the user
  median (info line). The docstring does not say which is intended.
- **Weights.** No version of `mlab.GaussianKDE`, `violin_stats` or `violinplot` accepts weights (signature recorded), so
  there is nothing to check.
- **Default box widths** (`np.clip(0.15*ptp, 0.15, 0.5)` against the documented "0.5, or 0.15*(distance between extreme
  positions), if that is smaller") and cap widths. These are cosmetic and out of scope.
- **int64 data beyond 2**53.** `np.percentile` and `np.mean` work in float64. This is numpy behaviour, not checked here.
- **seaborn ≥ 0.13** calls `cbook.boxplot_stats`, so FAILs 1–6 reach seaborn box plots too. seaborn itself was not run.
- **Statistical coverage of the bootstrap CI.** Only the algorithm was checked: percentile bootstrap, 95%, and the same
  resamples. Its coverage was not simulated.
