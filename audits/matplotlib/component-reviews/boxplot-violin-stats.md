# Component: box plot and violin statistics (`cbook.boxplot_stats`, `cbook.violin_stats`, `mlab.GaussianKDE`, `Axes.boxplot` / `bxp` / `violinplot` / `violin`)

Harness `verify/m1_boxplot_violin_stats.py`, notes `verify/m1_boxplot_violin_stats.notes.md`. Executed on four
builds: the **main overlay** (matplotlib 3.11.2 with `cbook.py`, `mlab.py`, `colors.py`, `colorizer.py`,
`contour.py`, `stackplot.py` and `axes/_axes.py` from `main` @ 44f2e00 copied in, numpy 2.5.3, scipy 1.18.1; a
full build of `main` is blocked because the download of its SheenBidi dependency is refused here), **3.11.2**
(numpy 2.5.3, scipy 1.18.1), **3.7.1** (numpy 1.26.4, no scipy) and **3.5.2** (numpy 1.23.5, no scipy). For this
group the 3.11.2 code is identical to `main`: `boxplot_stats`, `violin_stats`, `_reshape_2D`,
`delete_masked_points`, `GaussianKDE`, `boxplot`, `bxp`, `violinplot` and `violin` show no diff, and the two
outputs are line-for-line the same. File:line citations are to 44f2e00 unless a build is named.

Cohort: box plots are named in 8 papers, violin plots / KDE in 10 (lower bounds from the survey cache). seaborn
≥ 0.13 calls `cbook.boxplot_stats`, so MPL6 and MPL27–MPL29 reach seaborn box plots too (seaborn itself was not
run). Prior reports for every finding: search pending (`../prior-reports.md`).

## Truths

- `fractions.Fraction` for means, Hyndman & Fan type-7 percentiles, IQR, fences, whiskers and fliers, ddof=1
  variances and covariances, and the `linspace` grids (min + k·(max−min)/(P−1)).
- The notch formula med ± 1.57·IQR/√N from the Notes section.
- A plain-Python percentile bootstrap of the median, drawing the same resample indices from numpy's global RNG
  with the same seed; medians and the 2.5/97.5 percentiles computed exactly.
- The KDE as a direct `math.fsum` of Gaussian kernels in 1-D and 2-D (2×2 inverse by formula); Scott
  n^(−1/(d+4)) and Silverman (n(d+2)/4)^(−1/(d+4)).
- `scipy.stats.gaussian_kde` as an informational cross-check on main and 3.11.2 only.

Quartiles: the docstrings say only "first quartile (25th percentile)"; the code calls `np.percentile` with the
default 'linear' method (H&F type 7, cbook.py:1307), so H&F-7 is the truth. Tukey's hinges are printed as
information only (n=8: H&F-7 Q1 = 2.75, Tukey's hinge 2.5).

Version-dependent expectations: masked points are ignored by `boxplot_stats` from 3.9 (api_changes_3.9.0); masked
and non-finite values by `violin_stats`/`violinplot` from 3.11 (api_changes_3.11.0); the `("GaussianKDE",
bw_method)` method tuple is 3.11+; `side=` is 3.9+, `orientation=` 3.10+.

## Counts

| build | ok | FAIL |
|---|---|---|
| main overlay (3.11.2 + main @ 44f2e00 files) | 164 | 12 |
| 3.11.2 | 164 | 12 |
| 3.7.1 | 144 | 6 |
| 3.5.2 | 142 | 8 |

The old builds run fewer checks: the 3.9 and 3.11 features become information lines there, scipy is absent, and
`side=` does not exist. FAIL lines by finding: MPL2 6 (main, 3.11.2), MPL6 1, MPL27 2, MPL28 2, MPL29 1 (all
builds), MPL38 2 (3.5.2).

## Findings

### MPL2 — `violin_stats` / `violinplot` do not ignore masked values, despite the 3.11 release note and both docstrings (bug; main, 3.11.2)

**Measured.** Input: 40 clean values plus 50.0, −50.0 and 3.3, all three masked. Six FAIL lines (coords, vals,
mean/median/min/max, quantiles; list of masked arrays; `Axes.violinplot(masked array)`):

| statistic | matplotlib | clean (expected) |
|---|---|---|
| min / max | −50.0 / 50.0 | −2.8620539918219623 / 1.5265869454134247 |
| mean | −0.11667654626665863 | −0.207927287236658 |
| median | 0.04030224405126073 | 0.03517946967528861 |
| quantiles | [−0.9020736906638209, 0.5389883578231349] | [−0.9008415394557848, 0.40499042454150475] |
| KDE vals | maxrel 1.00e+00 against the clean KDE | — |

The grid runs from −50 to 50 and the KDE is built on all 43 values. For a list of masked arrays the second violin
has max 99 where the masked 99 should be excluded. `Axes.violinplot` draws the max line at 50.0 and the mean line
at −0.11667654626665863.

**Cause.** cbook.py:violin_stats (1591–1592):

```python
x = np.asarray(x)
x, = delete_masked_points(x)
```

`np.asarray` drops the `MaskedArray` mask before `delete_masked_points` can see it; `_reshape_2D` itself keeps the
masked array. `delete_masked_points` then removes only NaN and inf, which is why the NaN/±inf checks pass.
`np.asanyarray` (or no conversion) would fix it.

**Documentation.** `violin_stats` docstring "Non-finite and masked values are ignored" (cbook.py:1502); the
`violinplot` docstring (_axes.py:9004); api_changes_3.11.0/behavior.rst "now ignore masked and non-finite (NaN and
inf) values".

**Older builds** (information lines, since those versions documented no masked handling): on 3.7.1 and 3.5.2 the
masked array reaches `np.min`/`np.max`/`np.mean`, which respect the mask, so min, max and mean were right; the
median (0.04030224405126073) and quantiles were wrong, numpy warned "'partition' will ignore the 'mask'", and the
KDE `vals` came back fully masked (100/100). 3.11 changed which numbers go wrong rather than delivering the
promise: the min and max lines of a masked violin moved from correct (3.7.1) to wrong (3.11.2, main).

### MPL6 — `+inf` next to a quartile index makes Q3, the IQR and the upper whisker NaN and invents a low outlier (bug, numpy root cause; all builds)

**Measured.** Data [1, 2, 3, 4, inf]. H&F-7 gives Q3 = y[3] + 0·(y[4]−y[3]) = 4, whishi = 4, +inf a flier.
matplotlib: `q3=nan iqr=nan whishi=nan fliers=[1.0]` (`np.percentile([1,2,3,4,inf],75)` = nan).

**Cause.** `q1, med, q3 = np.percentile(x, [25, 50, 75])` (cbook.py:1307). numpy's `_lerp` computes
`4 + inf·0` = NaN (the numpy audit, n11 FAIL 1–12; NP4 in `../../numpy/full-inspection.md`). Then
`loval = q1 − whis·nan` is NaN, `x[x >= nan]` is empty, `whislo` falls back to Q1 = 2, and `x < 2` flags 1 as a
flier.

**Scope.** When +inf is not next to a quartile index ([1..8, inf]) every statistic is correct and +inf is a flier
(that check passes). `boxplot_stats` documents no handling of non-finite values. The reader sees a box with no
upper edge or upper whisker and a spurious low outlier. All four builds (numpy 1.23.5 through 2.5.3).

### MPL27 — a datum exactly on a fence is a whisker end, not a flier; the `whis` text says "below"/"above" (documentation gap, wording; all builds)

**Measured.** Data [−2, 1, 2, 3, 6]: Q1=1, Q3=3, IQR=2, fences exactly at −2 and 6. Read literally, "highest
datum below Q3 + whis*(Q3-Q1)" / "lowest datum above Q1 - whis*(Q3-Q1)" gives whiskers 3 and 1 with −2 and 6 as
fliers. matplotlib: `whishi=6.0`, `whislo=-2.0`, `fliers=[]` (2 FAIL lines).

**Code.** Inclusive fences: `wiskhi = x[x <= hival]` (cbook.py:1329), `wisklo = x[x >= loval]` (1336). The
`Axes.boxplot` summary, "the farthest data point lying within 1.5x the IQR from the box" (_axes.py:4381–4382), is
inclusive, matches the code, and its check passes; Tukey's convention is inclusive too.

**Fix.** The `whis` parameter text (cbook.py:1166–1168, _axes.py:4430–4432) should say "at or above" / "at or
below". Same text and code on all four builds; matters only when a datum sits exactly on a fence.

### MPL28 — whisker ends are clamped to the box edge, so a returned whisker can be Q1/Q3 rather than a datum (documentation gap; all builds)

**Measured.**
- [0,0,0,0,0,0,10,10]: Q1=0, Q3=2.5, upper fence 6.25; the highest datum ≤ 6.25 is 0 (inside the box).
  matplotlib `whishi=2.5` (= Q3, not a datum); fliers [10.0, 10.0].
- [1,2,4,4,6,8,10,30] with whis=0.25: fences 2.25 and 9.75, data inside 4…8. matplotlib whiskers 3.5 and 8.5
  (= Q1, Q3) against 4.0 and 8.0. Fliers [1.0, 2.0, 10.0, 30.0] are the same under both readings.

**Code.** cbook.py:boxplot_stats (1330–1340): `if len(wiskhi) == 0 or np.max(wiskhi) < q3: stats['whishi'] = q3`
and the mirror for `whislo`.

**Verdict.** The clamp is a sensible drawing choice (a zero-length whisker rather than one drawn back into the
box), but the docstring promises "the highest datum below Q3 + whis*IQR", and `whislo`/`whishi` are returned as
numbers to users and to seaborn. Occurs when data are sparse between a quartile and its fence (small n, ties, small
`whis`).

### MPL29 — `whis=(lo, hi)` puts the whiskers at the most extreme datum inside the percentiles, not at the percentiles (documentation gap; all builds)

**Measured.** `whis=(5, 95)` on 1..20: literal reading P5 = 1.95, P95 = 19.05; matplotlib whiskers 2.0 and 19.0.
The companion check using the "most extreme data inside [P5, P95]" reading passes, as do (10, 90) and
(2.5, 97.5) on n=104. Fliers are the same under both readings; the whisker end moves by less than one datum gap.

**Code.** `loval, hival = np.percentile(x, whis)` (cbook.py:1321), then the same datum search and clamp as for a
float `whis`.

**Fix.** "the percentiles at which to draw the whiskers" should read "the whiskers extend to the most extreme data
within these percentiles".

### MPL38 — 3.5.2 only: empty input has no `'iqr'` key (old-release only; fixed by 3.7.1)

**Measured.** `boxplot_stats([])` and `boxplot_stats(np.array([]))` return keys `['cihi', 'cilo', 'fliers',
'mean', 'med', 'q1', 'q3', 'whishi', 'whislo']` (2 FAIL lines). The 3.5.2 empty branch
(matplotlib/cbook/__init__.py:1178–1189) sets `med` twice and never sets `iqr`, although the Returns table lists
it; code reading `stats['iqr']` raises KeyError. 3.7.1 sets `stats['iqr'] = np.nan`, as does main (cbook.py:1292).

## What held up

**`boxplot_stats`, all four builds.** Mean, Q1, median, Q3, IQR, whiskers, notch and fliers equal the documented
definitions exactly (H&F-7 quartiles, inclusive fences) for odd n=7 with ties and negatives, even n=8 with an
outlier, n=1, n=2, n=3, negative data with outliers on both sides, a random n=104 sample, data offset by 1e9
(rel 1e-12), int64 input and float32 input (rel 2e-6). Integer input returns float quartiles (Q1 = 2.5 not
truncated); float32 whisker ends are exact data values. whis = 3.0, 5.0 and inf follow the fence rule (inf: min/max,
no fliers); whis='range' raises ValueError; whis=(0, 100) gives min and max with no fliers. With Q1 == Q3 and
`autorange=False` the IQR is 0 and both extremes are fliers; `autorange=True` moves the whiskers to min and max
only for the dataset whose IQR is 0. The asymptotic notch equals med ± 1.57·IQR/√N for n = 5, 16 and 401.
`bootstrap=500` and `2000` give exactly the 2.5th/97.5th H&F-7 percentiles of the resampled medians (a
percentile-method 95 % CI), reproducible under `np.random.seed` (the draw advances numpy's global RNG, recorded as
info). Lists of datasets, labels (wrong length raises ValueError), 2-D input split by column, empty input
(3.7.1+), masked input from 3.9, and +inf away from the quartile indices all behave as documented.

**`Axes.boxplot` / `bxp`, all builds** (drawn line data against the independent truth): median, box, whisker, cap
and flier coordinates; showmeans and meanline at the exact mean; default and custom positions; the notched outline
through cilo, med, cihi in documented vertex order; `usermedians`; `conf_intervals` (2.0, 6.5); horizontal boxes;
`boxplot(bootstrap=1000, notch=True)` at the ported bootstrap CI; `autorange=True` and `whis=(0, 100)`; masked
points neither used nor drawn from 3.9.

**`mlab.GaussianKDE`, all builds.** Default factor is Scott's n^(−1/5) for n = 7, 40, 300; 'silverman' gives
(3n/4)^(−1/5); covariance is the ddof=1 variance × factor²; `evaluate` equals the direct sum of Gaussians to about
1e-15 in both code branches (maxrel 4.74e-16, 1.08e-15, 1.80e-15); equals `scipy.stats.gaussian_kde` on main and
3.11.2; the pdf integrates to 1 within 1e-6; scalar and callable `bw_method`; 'scot' raises ValueError; float32
(rel 1e-6) and 1e6-offset data (rel 1e-7); 2-D factor n^(−1/6) with the ddof=1 covariance matrix and a density
equal to the direct bivariate sum; 3-D Silverman (5n/4)^(−1/7).

**`violin_stats`, all builds.** `coords` = linspace(min, max, points) for 100 and 7 points; `vals` equals the
direct-sum KDE for Scott (n = 2, 11, 23, 150, both branches), Silverman and bw=0.25; mean, median, min, max exact;
quantiles H&F-7 including q=0.07 and ragged per-dataset lists; integer input; 2-D split by column; a callable
`method(data, coords)` returned as-is; constant data and n=1 do not raise. 3.11+: the default method, the
("GaussianKDE", callable) form, unknown KDE name raises ValueError, NaN and ±inf ignored in every statistic and in
the KDE, empty and all-NaN datasets give NaN statistics without disturbing the others.

**`Axes.violinplot` / `violin`, all builds.** cmeans/cmedians/cmins/cmaxes at the exact statistics spanning
pos ± widths/4; cbars from min to max; cquantiles one segment per quantile; each body outline through
pos ± 0.5·widths·kde/max(kde) at every grid point (worst vertex distance about 1e-15), maximum full width = widths
(0.5, 1.2, 0.8); horizontal violins, `bw_method='silverman'`, `bw_method=0.2, points=31`; constant data and n=1.
3.9+: `side='low'`/`'high'` half-violins. 3.11+: NaN and ±inf ignored in the drawn lines.

## Not checked, or observed without a documented rule

- **NaN in box plot data.** No docstring says what happens. On every build one NaN makes mean, Q1, median, Q3,
  IQR, the notch and both whiskers NaN, with empty fliers: the box silently disappears. `violin_stats` documents
  (3.11+) and implements dropping NaN. Recorded as info; a documentation gap worth raising, but there is no
  documented truth to FAIL against.
- **Constant data and n=1 in violins.** `_kde_method` returns the indicator `(x[0] == coords).astype(float)`
  (cbook.py:1565), so the body is a zero-height line of full width; `mlab.GaussianKDE` itself raises
  `LinAlgError: Singular matrix` for constant data and `ValueError` for n=1. Undocumented; info.
- **`usermedians` and the notch.** The notch stays centred on the computed median (2.0), not the user median
  (1.75); the docstring does not say which is intended.
- **Weights.** No version of `GaussianKDE`, `violin_stats` or `violinplot` accepts weights.
- **Default box and cap widths**: cosmetic. **int64 beyond 2**53**: numpy behaviour. **Coverage of the bootstrap
  CI**: only the algorithm was checked, not its coverage.
