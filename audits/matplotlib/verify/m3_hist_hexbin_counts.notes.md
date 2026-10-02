# m3_hist_hexbin_counts: notes

Harness: `audits/matplotlib/verify/m3_hist_hexbin_counts.py`. It covers the counts and derived numbers produced by
`Axes.hist`, `stairs`, `hist2d`, `hexbin`, `acorr`/`xcorr`, `stackplot`, `pie` and `errorbar`.

Outputs:

| file | build |
|---|---|
| `m3_hist_hexbin_counts.out` | main overlay |
| `.v3.11.2.out` | 3.11.2 |
| `.v3.7.1.out` | 3.7.1 |
| `.v3.5.2.out` | 3.5.2 |

The "main overlay" is matplotlib 3.11.2 with main @ 44f2e00's `cbook.py`, `mlab.py`, `colors.py`, `colorizer.py`,
`contour.py`, `stackplot.py` and `axes/_axes.py` copied in. A full build of main is not possible here, because its
SheenBidi download is blocked. All of the code paths tested here live in those overlaid files. Each build runs in about
9 s.

Truths:
- `fractions.Fraction` for bin edges, bin membership, densities, cumulative sums, weighted sums, correlation sums,
  least-squares detrending and pie percentages.
- Plain-Python ports written from the docstrings:
  - the half-open bin rule with the last bin closed, in 1-D and 2-D;
  - the hexagonal grid as two interleaved lattices with nearest-centre assignment, plus an exact rational
    point-in-drawn-hexagon test;
  - `sum_n x[n+k]·conj(y[n])`;
  - the stackplot baselines, including the per-step minimiser of the weighted squared midline slopes (Byron & Wattenberg
    2008).
- Closed forms for the Sturges, sqrt and Rice bin counts and for log10.

SciPy is not used.

Some expectations are version-aware:
- **hexbin `mincnt`.** The expectation follows each build's own docstring ("more than" up to 3.7, "at least" from 3.8)
  and the 3.8.0/3.8.1 API notes.
- **hexbin `bins='log'`.** The expectation follows each build's own docstring: `log10(i+1)` in 3.5.2/3.7.1, and
  `log10(i)` / "equivalent to `norm=LogNorm()`" later.
- **errorbar sign check.** It runs only where the docstring says "All values must be >= 0". 3.5.2's docstring does not
  say this, so that build gets an info line instead.
- **pie `wedge_labels`.** This is a 3.12 feature, so only the main overlay checks it.

## Counts

| build | ok | FAIL |
|---|---|---|
| main overlay (3.11.2 + main @ 44f2e00 files) | 165 | 11 |
| 3.11.2 | 164 | 11 |
| 3.7.1 | 149 | 25 |
| 3.5.2 | 148 | 25 |

- **main overlay vs 3.11.2.** The main overlay has one extra check (`wedge_labels`, 3.12+). The FAIL lines are
  identical.
- **3.5.2 vs 3.7.1.** 3.5.2 lacks the errorbar sign check (see above). The FAIL lines are identical.

Every 3.11.2/main FAIL also fails on 3.5.2/3.7.1. The old builds add 14 more FAILs:
- 2 `mincnt`-docstring lines;
- 1 `bins='log'`-docstring line;
- 1 `acorr` on an int64 array;
- 10 pie lines from float32 arithmetic.

## FAIL lines

### 1. `hist2d(density=True, cmin=14)`: the NaN pattern does not follow the counts (all builds)

**What was measured.** The data has 404 points in 4×5 bins. Without density, exactly one cell has a count below 14.
With `density=True, cmin=14`, all 20 cells are NaN.

**What the code does.** `_axes.py:hist2d` (44f2e00 l. 7998–8004):

```python
h, xedges, yedges = np.histogram2d(..., density=density, weights=weights)
if cmin is not None:
    h[h < cmin] = None
```

With density on, the threshold is compared with the densities, which are all below 1 here.

**What the documentation says.** "All bins that has count less than *cmin* or more than *cmax* will not be displayed
(set to NaN …) and these count values in the return value count histogram will also be set to nan" (l. 7942). The
`cmin`/`cmax` boundary semantics hold without density: a count equal to `cmin` or `cmax` is kept, as the "ok" lines show.

**Verdict: documentation gap.** The docstring says "count", but with `density=True` (and with `weights`) the threshold
applies to the returned values. A user who sets `cmin=5` to hide sparse cells of a density plot blanks the whole plot.

### 2–3. `hexbin(C=None, mincnt=2|3)` displays cells with exactly `mincnt` points, but the docstring says "more than" (3.5.2, 3.7.1)

**What was measured.** With `mincnt=2`, 27 cells are shown against 26 expected, because one cell has exactly 2 points.
With `mincnt=3`, 26 cells are shown against 21 expected (5 cells have exactly 3).

**What the code does.** In those builds the `C=None` branch does `lattice1[lattice1 < mincnt] = np.nan`, which is
inclusive. The `C` branch uses `len(vals) > mincnt`, which is exclusive.

**What the documentation says.** The docstring in those builds: "only display cells with more than *mincnt* number of
points".

**Version notes.**
- The 3.8.0 API note "hexbin *mincnt* parameter made consistently inclusive" documents the old inconsistency. The harness
  checks the old behaviour as described there, and those lines pass.
- 3.8+ changed the docstring to "at least" and made both branches inclusive. On 3.11.2/main all four `mincnt` lines and
  the 3.8.1 default (C given, at least one point) pass.

**Verdict: documentation bug, fixed in 3.8.0.** It affects only 3.5.2 and 3.7.1.

### 4. `hexbin(bins='log')`: zero-count cells are 'bad' rather than coloured as `log10(0+1)` (3.5.2, 3.7.1)

**What was measured.** 12 zero-count cells are masked by `LogNorm`. The colour positions of the non-zero cells follow
`log10(i)`, not `log10(i+1)`.

**What the documentation says.** The docstring in those builds: "Internally, log10(i+1) is used to determine the hexagon
color."

**Version notes.** The 3.5.0 API note says hexbin "no longer (incorrectly) adds 1 to every bin value if a log norm is
being used", so the behaviour changed in 3.5.0 but the docstring was not updated. The 3.11.2/main docstring reads
"log10(i) … equivalent to `norm=LogNorm()`. Note that 0 counts are thus marked with the 'bad' color". That build passes
the corresponding check.

**Verdict: documentation bug.** It covers 3.5.0 to at least 3.7.1, and is fixed in the current docstring.

### 5. `hexbin(bins=3)`: the minimum count is put alone in its own class (all builds)

**What the code does.** `_axes.py:hexbin` l. 5849–5854:

```python
bins -= 1  # one less edge than bins
bins = minimum + (maximum - minimum) * np.arange(bins) / bins
bins = np.sort(bins)
accum = bins.searchsorted(accum)
```

For `k = 3` with counts 1..77, the bounds are `[1, 39]`. `searchsorted` (side='left') gives class 0 = {count ≤ 1},
class 1 = (1, 39] and class 2 = (39, 77].

**What was measured.** Class sizes are 7/22/5 (7 cells hold the minimum count 1). Equal-width classes over [1, 77]
would give 26/4/4.

**What the documentation says.** "If an integer, divide the counts in the specified number of bins, and color the
hexagons accordingly."

**Verdict: documentation gap / questionable behaviour.**
- Of the k classes, only k−1 split the range; the first holds exactly the minimum value.
- A count equal to an interior bound goes to the lower class (see 6).

### 6. `hexbin(bins=[1, 4, 8])`: a count equal to a "lower bound" goes to the bin below (all builds)

**What was measured.** The count-to-class map is {1:0, 2:1, 3:1, 4:1, 5:2, 6:2, 8:2, 9:3, …}. Count 4 is grouped with
2–3, and 8 with 5–6.

**What the documentation says.** "If a sequence of values, the values of the lower bound of the bins to be used." Under
that reading, 4 belongs with 5–7 and 8 starts a new bin.

**What the code does.** This is the same `searchsorted(side='left')` as in 5 (l. 5854), which makes each listed value the
inclusive *upper* end of the bin below.

**Verdict: bug against the documented definition.** With integer counts, ties with the listed bounds are the normal
case. Every cell whose count equals a listed bound is coloured one class too low.

### 7. `hexbin(xscale='log').get_offsets()` are not hexagon centres in data coordinates (all builds, two different ways)

**What the documentation says.** 44f2e00 l. 5636: "`PolyCollection.get_offsets` contains a Mx2 array containing the x,
y positions of the M hexagon centers in data coordinates". The 3.5.2/3.7.1 docstring has the same sentence without "in
data coordinates".

**3.11.2 and main.** The shape is right, (46, 2). But the x column holds log10(x) (for example 0.0058 where the centre
is at x = 1.0135). The offsets are computed in log space (l. 5803) and never exponentiated. Only the relative polygon is
exponentiated (`polygons = np.expand_dims(polygon, 0)` and `10.0 ** polygons`, l. 5816–5819). The drawing still comes
out right through `offset_transform=AffineDeltaTransform(self.transData)` (l. 5835).

**3.5.2 and 3.7.1.** Absolute polygons are built per hexagon, and `get_offsets()` returns a single `[[0, 0]]`.

**Verdict: documentation bug / API inconsistency.** The counts themselves are right: the log-grid check passes on every
build. Any code that reads hexagon positions back from the collection with a log scale gets exponents (3.11+) or nothing
(≤3.7).

### 8–9. `hexbin(marginals=True)` with `C=None`: every marginal bar has the value 1 (all builds)

**What was measured.** `hbar` = `[1, 1, 1, 1, 1, 1]`, but the x-column counts are `[21, 89, 196, 184, 90, 20]`.
`vbar` is all 1 likewise, against `[3, 27, 146, 250, 143, 30]`.

**What the code does.**
- The `C is None` branch sets `C = np.ones(len(x))` (l. 5776).
- The marginal loop computes `values[i] = reduce_C_function(ci)` (l. 5909), and `reduce_C_function` defaults to
  `np.mean`.
- The mean of ones is 1 in every non-empty bin, so the marginal colours carry no information.

**What the documentation says.** "If marginals is *True*, plot the marginal density as colormapped rectangles along the
bottom of the x-axis and left of the y-axis."

**The C-given case.** With `C` given, the marginals equal the per-bin `np.sum` and `np.mean` of C, and those lines pass.

**Verdict: bug against the documented definition.** In the default call, the "marginal density" is a constant.
Passing `reduce_C_function=np.sum` works around it.

### 10. `xcorr`/`acorr` with complex input and `normed=True`: the zero-lag value is not 1 (all builds)

**What was measured.** For 12 complex samples with ‖x‖² = 111, c[0] = 1.342 − 2.301j.

**What the code does.** `_axes.py:xcorr` l. 2112: `correls = correls / np.sqrt(np.dot(x, x) * np.dot(y, y))`. For
complex input, `np.dot(x, x)` is Σx², not Σ|x|². The un-normalised sums do follow the documented
`sum_n x[n+k]·conj(y[n])`, and that line passes.

**What the documentation says.** The docstring defines the correlation with an explicit complex conjugate, so complex
input is anticipated. It also says `normed`: "input vectors are normalised to unit length".

**Verdict: bug.** The normaliser should be `sqrt(vdot(x, x)·vdot(y, y))`. Real input is unaffected.

### 11–12. `acorr` on int16 samples: wrapped sums and NaN (all builds); old builds raise on any integer array with `normed=True` (13)

**What was measured.** A 40-sample int16 sine with amplitude 20000 (audio-like data).
- With `normed=False`, the result is `[22302, -97, -14889, 22590]` against the true `[5.04e9, 6.67e9, 7.79e9, 8.23e9]`.
- With `normed=True`, 3.11.2/main return `[nan, nan, …]` with no error.
- With `normed=True`, 3.5.2/3.7.1 raise `UFuncTypeError: Cannot cast ufunc 'divide' output … to int16`.

**What the code does.** `x = detrend(np.asarray(x))` (l. 2106) keeps int16. `np.correlate(x, y, mode="full")`
(l. 2109) and `np.dot(x, x)` then accumulate in int16 and wrap modulo 2¹⁶. The dot product wraps negative, and sqrt
gives NaN.

**Line 13 (3.5.2 and 3.7.1 only).** `acorr(np.array([3, 1, 4, 1, 5, 9, 2, 6]))` with the default `normed=True` raises
the same error even for int64 data. Those builds use in-place `correls /= ...`. The 3.11.2/main code
(`correls = correls / ...`) fixed that crash, and the line passes there. A list of Python ints and int64 arrays with
`normed=False` are exact on every build.

**Verdict: bug (silent wrong numbers).** It affects narrow-integer input on all builds. The docstring asks only for "a
unit-less array". Casting to float before `np.correlate` would fix both lines 11 and 12.

### 14. `stackplot(baseline='weighted_wiggle')` minimises the weighted wiggle of the layers in reverse order (all builds)

**What was measured.** Three float layers over 7 x-values. Matplotlib's baseline is
`[-2, -1.625, -2.375, -3.764, -4.097, -4.722, -6]`.

The per-step minimiser of Σᵢ fᵢ·(slope of midline i)² for the stacking as drawn (layer 0 at the bottom) is
`[-2, -2.375, -3.625, -5.236, -4.903, -3.278, -3]`. That is the Byron & Wattenberg 2008 formula
g0′ = −(1/Σf) Σᵢ fᵢ (½fᵢ′ + Σ_{j<i} fⱼ′), discretised as matplotlib does, with current-point weights and first
differences.

The objective is 84.35 for matplotlib against 13.88 for the minimiser. Matplotlib's baseline equals exactly the minimiser
for the reversed layer order.

**What the code does.** `stackplot.py` l. 121–128:

```python
increase = np.hstack((y[:, 0:1], np.diff(y)))
below_size = total - stack
below_size += 0.5 * y
move_up = below_size * inv_total
...
center = (move_up - 0.5) * increase
center = np.cumsum(center.sum(0))
first_line = center - 0.5 * total
```

This is Byron's reference `StreamLayout`, which works in screen coordinates (y down) and sets
`baseline = center + 0.5 * totalSize`. Ported to y-up, the bottom line should be `-center - 0.5 * total`. Keeping
`+center` mirrors the correction.

**What the documentation says.** "'weighted_wiggle': Does the same [minimizes the sum of the squared slopes] but weights
to account for size of each layer. It is also called 'Streamgraph'-layout … http://leebyron.com/streamgraph/".

**Verdict: bug against the documented definition.** The unweighted 'wiggle', 'sym' and 'zero' pass on all builds.
Layer thicknesses are preserved for all four baselines.

### 15. `stackplot(baseline='weighted_wiggle')` with integer layers truncates 1/total to 0 (all builds)

**What was measured.** The same layers given as int64 produce `[-2, -2, -4, -7, -7, -6, -7]`. As floats they produce
`[-2, -1.625, -2.375, …]`.

**What the code does.** `stackplot.py` l. 116–120: `total = np.sum(y, 0)` is int64, so
`inv_total = np.zeros_like(total)` is int64. `inv_total[mask] = 1.0 / total[mask]` then truncates every reciprocal to 0,
so `move_up` is 0 everywhere except the first column.

The code already promotes `stack` to float (`dtype=np.promote_types(y.dtype, np.float32)`, l. 98), but not
`inv_total`. float32 layers match float64 to float32 precision, and int 'sym'/'wiggle' match their float results.

**Verdict: bug (silent wrong numbers).** Integer counts are the most common streamgraph input. It is independent of item
14.

### 16–25. `pie` percentages and angles carry float32 rounding (3.5.2, 3.7.1)

These lines fail:
- the four `pie(..., autopct='%.9f')` label checks;
- the four "percentages sum to 100, wedge spans 360·x/sum(x)" checks;
- the `normalize=False` partial pie;
- the `autopct=callable` check.

**What was measured.**
- The labels are `16.666667163` instead of `16.666666667`.
- The callable receives `20.000000298023224` instead of 20.
- The partial-pie label is `30.000001` instead of 30.
- Wedge spans differ from 360·x/Σx at about 1e-7 relative.

**What the code does.** The 3.7.1 `_axes.py:pie` has `x = np.asarray(x, np.float32)` with the comment "The use of float32
is 'historical', but can't be changed without regenerating the test baselines."

**What held.**
- The added tolerance check (rel 1e-6) passes on every build.
- With the default-style formats such as `'%1.1f%%'`, the labels are correct.
- 3.11.2/main compute in float64 and pass all exact checks.

**Verdict: documented in the code, not the docs.** It is an expected precision limit of the old builds. Users see it
only with formats of 7 or more significant digits, or by reading the values passed to an `autopct` callable. The change
happened between 3.7.1 and 3.11.2, but no API note naming it was found in the doc tree.

## Information lines (not FAIL)

hist:
- `hist([1, 2, 2.5, inf])` without a range raises `ValueError: supplied range of [1.0, inf] is not finite` on all
  builds. The default range is (nanmin, nanmax), and numpy rejects it. The docstring says nothing about inf. With an
  explicit range, inf is ignored as an outlier, and that line is checked and passes.
- An all-NaN input, and `hist2d` with NaN and no range, raise numpy's "autodetected range of [nan, nan] is not finite".
- `hist([])` gives zeros on numpy's default (0, 1) range.
- Constant data is widened by numpy to ±0.5.
- `hist(cumulative=True)` with an explicit `range` ends at the in-range count (807 of 997), while the `cumulative` text
  says "The last bin gives the total number of datapoints". The `range` text ("outliers are ignored") covers it.
- 3.5.2 returns float32 `bins` for float32 data. 3.6+ casts to float64. The docstring only says "array".

hexbin:
- With `extent=(-1, 1, -2, 2)`, points just outside the extent that fall inside an edge hexagon are counted (308 of
  600). This is consistent with the drawn hexagons, and the docstring is silent.
- No random point fell exactly on a hexagon edge. The 1e-9 relative padding applied to `xmin`/`xmax` (l. 5748–5750), even
  with an explicit extent, makes exact edges unreachable from user coordinates. See "Not checked".

stackplot:
- 'wiggle' minimises the squared slopes of the m layer *midlines*: g0 = −(1/m) Σ (m − i − ½) fᵢ.
- Byron & Wattenberg's paper minimises over the m+1 *boundary* curves, giving −1/(m+1) Σ (m − i + 1) fᵢ. That gives a
  different baseline (−1.75 vs −1.667 at x = 0).
- The docstring does not say which curves are meant, so the midline version is accepted.

Errors:
- `pie([0, 0])` and `pie([1, nan])` raise `ValueError: cannot convert float NaN to integer` on 3.5.2/3.7.1 (gh-30007).
  The current builds give clear messages.
- `errorbar` with a negative yerr is accepted silently on 3.5.2, whose docstring states no constraint.

## What held up (all builds unless noted)

Axes.hist:
- **Bins.**
  - Integer `bins` produce `linspace(min, max, n+1)` edges, to a few ulps.
  - Counts match the plain-Python half-open rule with the last bin closed, for 1, 7, 10 and 64 bins on 997 normal
    values.
  - Integer data on edges gives [1, 2, 1, 3, 3], the docstring's own `[1, 2, 3, 4]` example rule holds, and unequal bin
    sequences give exact counts.
  - "Range has no effect if bins is a sequence" holds, and `range=(-1, 2)` drops outliers.
  - 'sturges', 'sqrt' and 'rice' give the closed-form bin counts, and 'auto' gives equal-width edges with exact counts.
  - `n` is always float.
- **density.**
  - The result equals counts/(Σcounts·Δbin) and integrates to 1, including with unequal bins.
  - Weighted density is normalised.
  - Each dataset is normalised separately when not stacked.
- **cumulative.**
  - `cumulative=True` and `-1` give exact running sums, with the last (or first) bin equal to N or to the sum of the
    weights.
  - With `density=True`, the last (or first) bin is exactly 1.
- **stacked.** `n_k` is the running sum over datasets. With density, the top layer integrates to 1 and the lower layers
  to their share. stacked+density+cumulative ends at 1.
- **Multiple datasets.**
  - Datasets of different lengths share one bins array over the combined range.
  - 2-D arrays are split by column.
  - An empty dataset in a list gives zeros.
  - Per-dataset weights work.
- **Edge-case data.**
  - NaN is dropped and the range comes from the finite values; this holds for multiple datasets too.
  - float32 counts are exact.
  - A 1e9 offset gives [10, 10, 10, 11].
  - int8 data is counted correctly.
- **Drawn geometry.**
  - The outlines of 'step' and 'stepfilled' (plain and stacked) contain a horizontal segment at each nᵢ, and
    `bottom=5` shifts them.
  - Bars span [eᵢ, eᵢ₊₁] with height nᵢ, and 'barstacked' bottoms and tops are the stacked n.
  - `log=True` sets a log y-scale without changing n.
  - In the horizontal orientation, the segments are at x = nᵢ.

Axes.stairs:
- The steps are at `values` between `edges`, and the default edges are 0..N.
- The path is closed on the baseline, while `baseline=None` gives an open path.
- `stairs(*np.histogram(x))` reproduces the counts.

Axes.hist2d:
- The edges are linspace on each axis.
- `h[i, j]` is indexed x-first, with the last bins closed on both axes.
- density equals count/(N·dx·dy) and integrates to 1.
- Weights with explicit edges, and `range` with outliers dropped, are handled.
- `cmin`/`cmax` hide exactly the cells with count < cmin or > cmax; a count equal to the threshold is kept.
- The QuadMesh array is `h.T`.

Axes.hexbin:
- **Grid.**
  - There are (nx+1)(ny+1) + nx·ny centres in 2nx+1 columns and 2ny+1 rows, with ny = int(nx/√3), and the tuple
    gridsize is honoured.
  - The columns span [min, max].
  - The hexagon vertices are (±sx/2, ±sy/6) and (0, ±sy/3).
- **Counts.**
  - Every hexagon's count equals the number of points inside the drawn hexagon (exact rational test), for gridsize 5,
    8 and (6, 4).
  - This also holds for grid-aligned points, an explicit extent, and an x offset of 1e9.
  - The counts equal the nearest-centre port in cell order.
  - The total is conserved, empty cells are 0 when `mincnt=None`, and NaN/inf points are dropped.
  - Constant data falls into one cell, and float32 data is handled.
- **C reductions.** With C, the mean, sum and max over the points inside each hexagon are exact, and empty hexagons are
  omitted.
- **mincnt.**
  - The "at least" semantics hold for both branches on 3.8+, and the old inclusive/exclusive split holds on ≤3.7.
  - With C given, the default is at least one point.
  - `mincnt=0` shows all cells; on 3.8+ it also passes empty input to the reduction.
- **bins='log'.** On 3.11+ the colour position follows LogNorm and zero counts are 'bad'. `get_array` keeps the raw
  counts.
- **Log scales.**
  - With `xscale='log'`, the counts equal the log10-grid port and the total is conserved.
  - With `yscale='log'` and an exponent extent, the counts are correct.
  - x ≤ 0 with a log scale raises ValueError.
- **Marginals with C.** The marginals equal the per-bin sum or mean of C.

Axes.acorr/xcorr:
- The lag vector is −maxlags..maxlags, and the un-normalised sums are exact.
- `normed` divides by sqrt(x·x · y·y).
- The default maxlags=10 gives 21 lags, with c(0) = 1 and symmetry.
- `maxlags=None` gives 2N−1 lags.
- `maxlags=N` raises ValueError.
- `detrend_mean` and `detrend_linear` match the exact residuals.
- `usevlines=False` gives the same numbers.
- The complex un-normalised sums follow x[n+k]·conj(y[n]).
- int64 data with `normed=True` is exact on 3.11+, and lists of ints with `normed=False` are exact everywhere.

Axes.stackplot:
- 'zero' gives 0, and 'sym' gives −Σf/2.
- 'wiggle' gives the midline least-squares baseline.
- Layer thicknesses are preserved for all baselines.
- int input works for 'sym' and 'wiggle', and float32 for 'weighted_wiggle'.
- All-zero layers give a finite baseline.

Axes.pie:
- **Percentages (3.11+).**
  - The autopct strings equal `fmt % (100·x/Σx)` exactly, for [1, 2, 3], [0.1, 0.2, 0.3], with a zero wedge, for a
    single wedge, and for [0.001, 0.002, 1].
  - They sum to 100.
  - The wedge spans are 3.6·pct degrees.
- **Percentages (all builds).** The autopct values are within float32 precision of 100·x/Σx, and a single wedge is exact.
- **normalize=False.** Σ < 1 gives a partial pie labelled 10/20/30 on 3.11+, Σ > 1 raises, and Σ = 1 gives a full pie.
- **Other options.**
  - The callable `autopct` receives the percentages.
  - startangle and counterclock behave as documented.
  - A negative value raises.
  - `wedge_labels` `{frac}`/`{absval}` are correct (main, 3.12+).

Axes.errorbar:
- Bars run from y−e to y+e for an `(N,)` error, and an `(2, N)` error uses the lower row then the upper row.
- A scalar xerr works, and xerr and yerr can be given together.
- `lolims` draws y..y+upper and `uplims` draws y−lower..y; both together give a degenerate bar.
- `xlolims`/`xuplims` behave the same way on the horizontal bars.
- A NaN error skips that bar.
- `errorevery=2` draws bars on points 0, 2 and 4 only.
- Negative errors raise ValueError where the docstring states the constraint (3.7.1+).
- The cap markers sit at y±e.

## Not checked

- **Points exactly on a hexagon edge.** The 1e-9 relative padding of xmin/xmax cannot be undone from user
  coordinates, so exact ties are unreachable. Conservation and the closed-polygon bounds would still catch double or
  missed counting.
- **Datetime and timedelta input to hist.** These are out of scope per the task. timedelta raises TypeError, as the code
  documents.
- **Masked arrays in hist.** The docstring says "Masked arrays are not supported".
- **Boxplot.** Covered by another group.
- **Rendered pixels and colours beyond the norm position.** Out of scope; the colour position is checked through
  `pc.norm`.
- **`xcorr` with x and y of different lengths.** It raises ValueError by code inspection and is not run.
- **`hexbin` with a reduce function that errors on empty input under `mincnt=0`.** This is covered only by the
  `len`-reduction check.
