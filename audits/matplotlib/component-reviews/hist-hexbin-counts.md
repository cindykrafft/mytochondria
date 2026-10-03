# Component: counts and derived numbers (`Axes.hist`, `stairs`, `hist2d`, `hexbin`, `acorr` / `xcorr`, `stackplot`, `pie`, `errorbar`)

Harness `verify/m3_hist_hexbin_counts.py`, notes `verify/m3_hist_hexbin_counts.notes.md`. Executed on four builds:
the **main overlay** (matplotlib 3.11.2 with `cbook.py`, `mlab.py`, `colors.py`, `colorizer.py`, `contour.py`,
`stackplot.py` and `axes/_axes.py` from `main` @ 44f2e00 copied in; a full build of `main` is blocked because its
SheenBidi download is refused here; every code path in this group lives in the overlaid files), **3.11.2** (numpy
2.5.3), **3.7.1** (numpy 1.26.4) and **3.5.2** (numpy 1.23.5). About 9 s per build. File:line citations are to
44f2e00 unless a build is named.

Cohort (lower bounds from the survey cache): histograms in 14 papers, error bars / mean ± SEM in 5, pie / stacked
plots in 2, hexbin / 2-D density in 1. Prior reports for every finding: see `../prior-reports.md` (tracker searched 2026-10-03; one line per finding in the README table).

## Truths

- `fractions.Fraction` for bin edges, bin membership, densities, cumulative and weighted sums, correlation sums,
  least-squares detrending and pie percentages.
- Plain-Python ports written from the docstrings: the half-open bin rule with the last bin closed (1-D and 2-D);
  the hexagonal grid as two interleaved lattices with nearest-centre assignment, plus an exact rational
  point-in-drawn-hexagon test; `sum_n x[n+k]·conj(y[n])`; the stackplot baselines, including the per-step
  minimiser of the weighted squared midline slopes (Byron & Wattenberg 2008).
- Closed forms for the Sturges, sqrt and Rice bin counts and for log10. SciPy is not used.

Version-aware expectations: hexbin `mincnt` follows each build's own docstring ("more than" up to 3.7, "at least"
from 3.8) and the 3.8.0/3.8.1 API notes; hexbin `bins='log'` follows each build's docstring (`log10(i+1)` on
3.5.2/3.7.1, `log10(i)` / "equivalent to `norm=LogNorm()`" later); the errorbar sign check runs only where the
docstring says "All values must be >= 0" (not 3.5.2); pie `wedge_labels` (3.12) only on the main overlay.

## Counts

| build | ok | FAIL |
|---|---|---|
| main overlay (3.11.2 + main @ 44f2e00 files) | 165 | 11 |
| 3.11.2 | 164 | 11 |
| 3.7.1 | 149 | 25 |
| 3.5.2 | 148 | 25 |

The main overlay has one extra check (`wedge_labels`, 3.12+); the FAIL lines on main and 3.11.2 are identical.
3.5.2 lacks the errorbar sign check; the FAIL lines on 3.5.2 and 3.7.1 are identical. Every 3.11.2/main FAIL also
fails on 3.5.2/3.7.1; the old builds add 14: 2 `mincnt`-docstring lines (MPL40), 1 `bins='log'`-docstring line
(MPL41), 1 `acorr` on an int64 array (MPL37), 10 pie lines (MPL43). The 11 on main: MPL24 1, MPL25 1, MPL5 1,
MPL26 1, MPL4 2, MPL12 1, MPL11 2, MPL15 1, MPL14 1. (Notes item numbers are given in each heading.)

## Findings

### MPL4 (items 8–9) — `hexbin(marginals=True)` with `C=None`: every marginal bar has the value 1 (bug; all builds)

**Measured.** `hbar` = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0] against x-column counts [21, 89, 196, 184, 90, 20]; `vbar`
all 1.0 against y counts [3, 27, 146, 250, 143, 30].

**Cause.** The `C is None` branch sets `C = np.ones(len(x))` (l. 5776); the marginal loop computes
`values[i] = reduce_C_function(ci)` (l. 5909) with the default `np.mean`. The mean of ones is 1 in every non-empty
bin.

**Documentation.** "If marginals is *True*, plot the marginal density as colormapped rectangles along the bottom of
the x-axis and left of the y-axis."

**Verdict.** In the default call the "marginal density" is a constant. With `C` given the marginals equal the
per-bin `np.sum`/`np.mean` of C (passes). Workaround: `reduce_C_function=np.sum`.

### MPL5 (item 6) — `hexbin(bins=[1, 4, 8])`: a count equal to a listed "lower bound" goes to the bin below (bug; all builds)

**Measured.** Count → class {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 8: 2, 9: 3, …}: count 4 is grouped with 2–3, and
8 with 5–6.

**Documentation.** "If a sequence of values, the values of the lower bound of the bins to be used": 4 belongs with
5–7, and 8 starts a new bin.

**Cause.** `accum = bins.searchsorted(accum)` with side='left' (l. 5854) makes each listed value the inclusive
*upper* end of the bin below.

**Verdict.** With integer counts, ties with the listed bounds are the normal case; every cell whose count equals a
listed bound is coloured one class too low.

### MPL11 (items 11–12) — `acorr` on int16 samples: wrapped sums, and NaN with `normed=True` (bug; all builds)

**Measured.** A 40-sample int16 sine of amplitude 20000 (audio-like):

- `normed=False`: [22302, −97, −14889, 22590] against the true [5035415326.0, 6674972575.0, 7785006551.0,
  8234555454.0].
- `normed=True`: main and 3.11.2 return [nan nan nan nan] with no error, against [0.611498137832566,
  0.8106050912265798, 0.9454070222113049, 1.0]; 3.5.2 and 3.7.1 raise `UFuncTypeError: Cannot cast ufunc 'divide'
  output from dtype('float32') to dtype('int16')`.

**Cause.** `x = detrend(np.asarray(x))` (l. 2106) keeps int16; `np.correlate(x, y, mode="full")` (l. 2109) and
`np.dot(x, x)` accumulate in int16 and wrap modulo 2¹⁶; the dot product wraps negative and sqrt gives NaN.

**Verdict.** Silent wrong numbers for narrow-integer input. The docstring asks only for "a unit-less array". A
list of Python ints and int64 arrays with `normed=False` are exact on every build. Casting to float before
`np.correlate` fixes both lines.

### MPL12 (item 10) — `xcorr`/`acorr` with complex input and `normed=True`: zero-lag value is not 1 (bug; all builds)

**Measured.** 12 complex samples with ‖x‖² = 111.0: c[0] = (1.3419689119170986−2.300518134715026j).

**Cause.** `_axes.py:xcorr` l. 2112: `correls = correls / np.sqrt(np.dot(x, x) * np.dot(y, y))`; for complex
input `np.dot(x, x)` is Σx², not Σ|x|². The un-normalised sums follow the documented `sum_n x[n+k]·conj(y[n])`
(passes).

**Documentation.** The correlation is defined with an explicit conjugate (complex input anticipated); `normed`:
"input vectors are normalised to unit length". The normaliser should be `sqrt(vdot(x, x)·vdot(y, y))`. Real input
is unaffected.

### MPL14 (item 15) — `stackplot(baseline='weighted_wiggle')` with integer layers truncates 1/total to 0 (bug; all builds)

**Measured.** The same layers as int64 give [−2, −2, −4, −7, −7, −6, −7]; as floats [−2, −1.625, −2.375,
−3.7639, …].

**Cause.** `stackplot.py` l. 116–120: `total = np.sum(y, 0)` is int64, so `inv_total = np.zeros_like(total)` is
int64 and `inv_total[mask] = 1.0 / total[mask]` truncates every reciprocal to 0; `move_up` is 0 everywhere except
the first column. The code already promotes `stack` to float (`dtype=np.promote_types(y.dtype, np.float32)`,
l. 98) but not `inv_total`.

**Verdict.** Silent wrong numbers; integer counts are the most common streamgraph input. float32 layers match
float64 to float32 precision, and integer 'sym'/'wiggle' match their float results. This check compares integer
against float input and is independent of MPL15.

### MPL15 (item 14) — `stackplot(baseline='weighted_wiggle')` minimises the weighted wiggle of the layers in reverse order (bug; all builds since 1.3.0)

With three float layers over 7 x-values matplotlib's baseline is [−2, −1.625, −2.375, −3.764, −4.097,
−4.722, −6]; the per-step minimiser of Σᵢ fᵢ·(slope of midline i)² for the stacking as drawn is [−2, −2.375,
−3.625, −5.236, −4.903, −3.278, −3]; the objective is 84.3542 for matplotlib against 13.8819 for the minimiser,
and matplotlib's baseline equals the minimiser for the reversed layer order. The notes attribute this to
`stackplot.py` l. 121–128 keeping `+center` when porting Byron's screen-coordinate (y-down) `StreamLayout` to
y-up. Documentation: "'weighted_wiggle': Does the same but weights to account for size of each layer. It is also
called 'Streamgraph'-layout … http://leebyron.com/streamgraph/". Status: confirmed on re-verification (`verify/m3_stackplot_wiggle.notes.md`, harness `verify/m3b_stackplot_wiggle.py`, 40 ok / 8 FAIL on main and 3.11.2): the paper's minimiser (§5.1) and Byron's `StreamLayout.java` agree exactly in Fraction arithmetic; matplotlib's `first_line = center - 0.5 * total` (stackplot.py:128 on 44f2e00) is the minimiser for the reversed order. Two layers [1,3]/[1,1]: correct g0 (−1, −9/4), matplotlib (−1, −7/4). 0 of 400 random integer cases match (ratio 1.02–212, median 5.2). Introduced in 24f537f (2013-01-10), present in every release since 1.3.0; the only test is the image test `test_stackplot_baseline`, which pins the current output.

### MPL24 (item 1) — `hist2d(density=True, cmin=…)`: the threshold is applied to densities, not counts (documentation gap; all builds)

**Measured.** 404 points in 4×5 bins; without density exactly one cell has a count below 14; with
`density=True, cmin=14` all 20 of 20 cells are NaN.

**Code.** `_axes.py:hist2d` (l. 7998–8004): `h, … = np.histogram2d(..., density=density, weights=weights)` then
`h[h < cmin] = None`.

**Documentation.** "All bins that has count less than *cmin* or more than *cmax* will not be displayed … and these
count values in the return value count histogram will also be set to nan" (l. 7942). With `density=True` (and with
`weights`) the threshold applies to the returned values: a user who sets `cmin=5` to hide sparse cells of a
density plot blanks the whole plot. Without density the boundary semantics hold (a count equal to `cmin`/`cmax` is
kept).

### MPL25 (item 5) — `hexbin(bins=<int>)`: the minimum count is put alone in its own class (documentation gap / questionable behaviour; all builds)

**Measured.** k = 3 on counts 1..77: class sizes 7/22/5 (the 7 cells with the minimum count 1 alone in class 0),
against 26/4/4 for equal-width classes over [1, 77].

**Code.** `_axes.py:hexbin` l. 5849–5854: `bins -= 1`, `bins = minimum + (maximum - minimum) * np.arange(bins) /
bins`, `accum = bins.searchsorted(accum)`: bounds [1, 39], so class 0 = {count ≤ 1}, class 1 = (1, 39],
class 2 = (39, 77].

**Documentation.** "If an integer, divide the counts in the specified number of bins, and color the hexagons
accordingly." Of the k classes only k−1 split the range; a count equal to an interior bound goes to the lower
class (as MPL5).

### MPL26 (item 7) — `hexbin(xscale='log').get_offsets()` are not hexagon centres in data coordinates (documentation gap / API inconsistency; all builds, two different ways)

**Documentation.** l. 5636: "`PolyCollection.get_offsets` contains a Mx2 array containing the x, y positions of the
M hexagon centers in data coordinates" (3.5.2/3.7.1: the same sentence without "in data coordinates").

**Measured.** main and 3.11.2: shape (46, 2) as expected, but the x column holds log10(x): first rows
[[0.005821909300683488, 0.0056647904993228915], …] against centres at x = 1.0134956973556237. The offsets are
computed in log space (l. 5803) and never exponentiated; only the relative polygon is (`10.0 ** polygons`,
l. 5816–5819); drawing is still right through `offset_transform=AffineDeltaTransform(self.transData)` (l. 5835).
3.5.2 and 3.7.1: absolute polygons per hexagon, and `get_offsets()` returns a single [[0.0, 0.0]] (shape (1, 2)).

**Verdict.** Counts are right (the log-grid check passes everywhere); code reading hexagon positions back from the
collection gets exponents (3.11+) or nothing (≤ 3.7).

### MPL37 (item 13) — 3.5.2 and 3.7.1: `acorr`/`xcorr` with `normed=True` raises on any integer array (old-release only)

`acorr(np.array([3, 1, 4, 1, 5, 9, 2, 6]))` with the default `normed=True` raises `UFuncTypeError: Cannot cast
ufunc 'divide' output from dtype('float64') to dtype('int64')`: those builds divide in place (`correls /= ...`).
The 3.11.2/main code (`correls = correls / ...`) fixed the crash, and the line passes there.

### MPL40 (items 2–3) — 3.5.2 and 3.7.1: `hexbin(C=None, mincnt=…)` shows cells with exactly `mincnt` points; the docstring says "more than" (old-release only, documentation; fixed in 3.8.0)

`mincnt=2`: 27 cells shown against 26 expected (1 cell has exactly 2). `mincnt=3`: 26 shown against 21 (5 cells
have exactly 3). In those builds the `C=None` branch does `lattice1[lattice1 < mincnt] = np.nan` (inclusive) while
the `C` branch uses `len(vals) > mincnt` (exclusive). The 3.8.0 API note "hexbin *mincnt* parameter made
consistently inclusive" documents the old split (checked as described there, passes); 3.8+ says "at least" and is
inclusive in both branches, and all four `mincnt` lines plus the 3.8.1 default pass on 3.11.2/main.

### MPL41 (item 4) — 3.5.2 and 3.7.1: `hexbin(bins='log')` docstring says `log10(i+1)` (old-release only, documentation)

12 zero-count cells are masked by `LogNorm` ("bad"), and the colour positions of the non-zero cells follow
`log10(i)`, not the documented `log10(i+1)`. The 3.5.0 API note says hexbin "no longer (incorrectly) adds 1 to every
bin value if a log norm is being used", but the docstring was not updated until later; the 3.11.2/main docstring
("log10(i) … equivalent to `norm=LogNorm()` … 0 counts are thus marked with the 'bad' color") matches and passes.
Covers 3.5.0 to at least 3.7.1.

### MPL43 (items 16–25) — 3.5.2 and 3.7.1: pie percentages and angles carry float32 rounding (old-release only; precision limit, harness expectation at 9 digits)

**Measured.** `autopct='%.9f'` labels '16.666667163', '33.333334327' for [1, 2, 3] (exact '16.666666667',
'33.333333333'); the `autopct` callable receives 20.000000298023224 for 20; the `normalize=False` partial pie
labels '30.000001' for 30; wedge spans differ from 360·x/Σx at about 1e-7 relative (10 FAIL lines: four label
checks, four sum/span checks, the partial pie, the callable).

**Code.** 3.7.1 `_axes.py:pie`: `x = np.asarray(x, np.float32)`, commented "The use of float32 is 'historical', but
can't be changed without regenerating the test baselines."

**Verdict.** Documented in the code, not the docs; the tolerance check (rel 1e-6) passes on every build, default
formats such as `'%1.1f%%'` are correct, and 3.11.2/main compute in float64 and pass every exact check. Visible
only with formats of 7 or more significant digits or by reading the callable's argument. No API note naming the
change between 3.7.1 and 3.11.2 was found.

## What held up (all builds unless noted)

- **`Axes.hist` bins.** Integer `bins` give `linspace(min, max, n+1)` edges to a few ulps; counts match the
  half-open rule with the last bin closed for 1, 7, 10 and 64 bins on 997 normal values; integer data on edges
  gives [1, 2, 1, 3, 3]; the docstring's `[1, 2, 3, 4]` example rule; unequal bin sequences; "Range has no effect
  if bins is a sequence"; `range=(-1, 2)` drops outliers; 'sturges' (11), 'sqrt' (32), 'rice' (20) closed-form
  counts for N = 997; 'auto' equal-width with exact counts; `n` always float.
- **density / cumulative / stacked.** counts/(Σcounts·Δbin) integrating to 1 with unequal bins and weights;
  per-dataset normalisation when not stacked; `cumulative=True` and `-1` exact, last (first) bin = N or Σweights,
  and exactly 1 with density; stacked running sums, the top layer integrating to 1 (integrals 0.657205,
  0.984716, 1.0) and stacked+density+cumulative ending at 1.
- **Multiple datasets and edge data.** One shared bins array over the combined range; 2-D split by column; an empty
  dataset gives zeros; per-dataset weights; NaN dropped; float32 counts exact; a 1e9 offset gives [10, 10, 10, 11];
  int8 counted correctly.
- **Drawn geometry.** 'step'/'stepfilled' (plain and stacked) outlines at each nᵢ, `bottom=5`; bars and
  'barstacked' bottoms/tops; `log=True` without changing n; horizontal orientation.
- **`stairs`.** Steps at `values` between `edges`, default edges 0..N, closed on the baseline, open with
  `baseline=None`, `stairs(*np.histogram(x))` reproduces the counts.
- **`hist2d`.** linspace edges per axis; `h[i, j]` indexed x-first with last bins closed; density =
  count/(N·dx·dy) integrating to 1; weights with explicit edges; `range` drops outliers; `cmin`/`cmax` hide
  exactly the cells < cmin or > cmax (equality kept); the QuadMesh array is `h.T`.
- **`hexbin` grid and counts.** (nx+1)(ny+1) + nx·ny centres with ny = int(nx/√3) (28, 77, 59 centres for
  gridsize 5, 8, (6, 4)); columns span [min, max]; vertices (±sx/2, ±sy/6), (0, ±sy/3). Every hexagon's count equals
  the number of points inside the drawn hexagon (exact rational test), including grid-aligned points, an explicit
  extent and a 1e9 x offset; counts equal the nearest-centre port in cell order; total conserved (600 of 600);
  empty cells 0 with `mincnt=None`; NaN/inf dropped; constant and float32 data.
- **`hexbin` C, mincnt, log.** C mean/sum/max over the points in each hexagon exact (34 hexagons vs 34 occupied);
  `mincnt` "at least" on 3.8+ and the old split on ≤ 3.7; with C given the default is at least one point;
  `mincnt=0`; `bins='log'` on 3.11+ follows LogNorm with zero counts 'bad' and raw counts in `get_array`;
  `xscale='log'` counts equal the log10-grid port, `yscale='log'` with an exponent extent (sum 400 vs 400), x ≤ 0
  raises; marginals with C equal the per-bin sum or mean.
- **`acorr`/`xcorr`.** Lags −maxlags..maxlags; exact un-normalised sums; `normed` divides by sqrt(x·x · y·y) for
  real input; default 21 lags with c(0) = 1 and symmetry; `maxlags=None` gives 2N−1; `maxlags=N` raises;
  `detrend_mean`/`detrend_linear` residuals exact; `usevlines=False`; complex un-normalised sums; int64 with
  `normed=True` exact on 3.11+; lists of ints with `normed=False` exact everywhere.
- **`stackplot`.** 'zero' gives 0; 'sym' gives −Σf/2; 'wiggle' gives the midline least-squares baseline; layer
  thicknesses preserved for all four baselines; int input for 'sym' and 'wiggle'; float32 for 'weighted_wiggle';
  all-zero layers finite.
- **`pie`.** 3.11+: autopct strings equal `fmt % (100·x/Σx)` exactly for [1, 2, 3], [0.1, 0.2, 0.3], a zero
  wedge, one wedge and [0.001, 0.002, 1], summing to 100 with spans 3.6·pct degrees; all builds within float32
  precision; `normalize=False` partial/full/raising; callable autopct; startangle; counterclock; negative values
  raise; `wedge_labels` `{frac}`/`{absval}` (main, 3.12+).
- **`errorbar`.** (N,) and (2, N) errors (lower row first); scalar xerr; x and y together; `lolims`/`uplims` and
  `xlolims`/`xuplims`; NaN skips a bar; `errorevery=2`; negative errors raise where documented (3.7.1+); caps at
  y ± e.

## Information lines (not FAIL)

- `hist([1, 2, 2.5, inf])` without a range raises `ValueError: supplied range of [1.0, inf] is not finite` (the
  docstring says nothing about inf; with an explicit range inf is ignored, which passes). All-NaN input and
  `hist2d` with NaN and no range raise numpy's "autodetected range of [nan, nan] is not finite". `hist([])` gives
  zeros on (0, 1); constant data is widened by ±0.5.
- `hist(cumulative=True)` with `range=(-1, 2)` ends at 807.0 of N = 997, while the `cumulative` text says "The last
  bin gives the total number of datapoints"; the `range` text ("outliers are ignored") covers it.
- 3.5.2 returns float32 `bins` for float32 data; 3.6+ casts to float64.
- hexbin with `extent=(-1, 1, -2, 2)` counts points just outside the extent that fall inside an edge hexagon (sum
  308.0 of 600), consistent with the drawn hexagons; the docstring is silent.
- 'wiggle' minimises over the m layer *midlines* (−1.6667 at x = 0); Byron & Wattenberg's boundary-curve version
  gives −1.75; the docstring does not say which curves, so the midline version is accepted.
- `pie([0, 0])` and `pie([1, nan])` raise "cannot convert float NaN to integer" on 3.5.2/3.7.1 (gh-30007);
  current builds give clear messages. `errorbar` with a negative yerr is accepted silently on 3.5.2, whose
  docstring states no constraint.

## Not checked

Points exactly on a hexagon edge (the 1e-9 relative padding of xmin/xmax, l. 5748–5750, makes exact ties
unreachable from user coordinates); datetime/timedelta input to hist; masked arrays in hist ("not supported");
box plots (other group); rendered pixels beyond the norm position; `xcorr` with unequal lengths (raises by code
inspection); a reduce function that errors on empty input under `mincnt=0` (covered only by the `len` reduction).
