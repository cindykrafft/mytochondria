# n11_stats_reductions_convolution: notes

Harness: `audits/numpy/verify/n11_stats_reductions_convolution.py`. Outputs: `n11_stats_reductions_convolution.out`
(numpy 2.4.6), `.v1.23.5.out`, `.v1.24.4.out`, `.v1.26.4.out`. Runtime is about 2 s per build.
Truths: `fractions.Fraction` for the exact sums, variances, covariances (complex via exact real/imaginary pairs),
H&F type-7 quantiles, the weighted inverted-CDF coverage definition, exact bin membership for histogram2d/dd,
trapezoid sums, the derivative of the local Lagrange interpolant (as the truth for `gradient`), piecewise-linear and
periodic `interp`, and unwrap by the documented rule. mpmath at 40 digits for square roots, cube roots, log2, the
Doane skewness and atan2 in degrees. Plain-Python references for Stone's cross-validation estimator and for direct
convolution and correlation sums with complex conjugation. The harness does not use scipy.
The checks follow what the docstrings say. Where behaviour differs by version, the expectation depends on the version:
`correction=`/`mean=` (2.0+), `weights=` for quantiles (2.0+), `cumulative_sum/prod` (2.1+), the integer bin-width rule
(2.1+), `clip(a)` with no bounds (2.1+), and the removal of `corrcoef(bias=)` (2.4).

## Counts

| build | ok | FAIL |
|---|---|---|
| numpy 2.4.6 | 451 | 18 |
| numpy 1.26.4 | 422 | 13 |
| numpy 1.24.4 | 422 | 13 |
| numpy 1.23.5 | 422 | 13 |

The 1.x builds run fewer checks because the 2.x-only features appear there as information lines. Every build has the
same 13 FAIL lines: 12 of them come from one root cause (quantile interpolation next to ±inf), and 1 is an unwrap
boundary case. numpy 2.4.6 adds 5 more: the 'auto' bin estimator and four silent integer wraparounds in
`select`/`where`.

## FAIL lines

### 1–12. Quantile interpolation next to ±inf returns NaN (all builds; one root cause)

These lines fail:
- `percentile([1, 2, inf], 50) = 2`: virtual index exactly 1, so g = 0.
- `percentile([0, inf], 0) = 0`.
- `percentile([1, 2, 3, 4, inf], 75) = 4`.
- `percentile([1, 2, inf], 100) = inf`.
- `percentile([1, 2, inf], 75) = inf`: g = 0.5.
- `percentile([-inf, 1, 2], 10) = -inf`: g = 0.2.
- `median(x) == quantile(x, 0.5)` for `[1, 2, inf]` (median 2.0, quantile nan) and for `[1, 2, 3, inf, inf]` (3.0 vs nan).
- `percentile(x, [0, 100]) == [min, max]` for `[1, 2, inf]` → `[1, nan]`, for `[-inf, 0, 1]` → `[nan, 1]`, and for
  `[1, 2, 3, inf, inf]` → `[1, nan]`.
- `nanpercentile([1, NaN, 2, inf], 50) = 2` → nan.

Each of these NaN results also raises a RuntimeWarning ("invalid value encountered in multiply/add").

In the library, every continuous method goes through `_lerp` (numpy 2.4.6
`numpy/lib/_function_base_impl.py:_lerp`, and the same code in 1.23 `numpy/lib/function_base.py:_lerp`):

```
diff_b_a = b - a
lerp_interpolation = add(a, diff_b_a * t, ...)
subtract(b, diff_b_a * (1 - t), out=lerp_interpolation, where=t >= 0.5, ...)
```

With b = +inf, `diff_b_a` is inf. So t = 0 gives `a + inf*0 = nan`, t ≥ 0.5 gives `inf - inf = nan`, and for the -inf
lower neighbour with t < 0.5, `-inf + inf*t = nan`. The q = 100 / q = 0 cases fail because j+1 is clipped to n-1
(documented), so `a = b = ±inf` and `diff = nan`.

The documentation (quantile Notes) says the result is `(1-g)*y[j] + g*y[j+1]`. For g > 0 the literal formula gives
±inf in IEEE arithmetic: `0.5*2 + 0.5*inf = inf` and `0.8*(-inf) + 0.2*1 = -inf`. For the clipped end points it gives
`1*inf + 0*inf`. When g = 0 and the neighbour is infinite, evaluating the formula literally in IEEE arithmetic gives NaN
(0*inf). The H&F estimator is y[j] by definition in that case, though, and `np.median`, which the docstring says is
"equivalent to quantile(..., 0.5)", returns y[j]. The 0th/100th percentile being NaN when the min/max is ±inf is the
clearest symptom.

Verdict: **bug** (an edge case in the lerp implementation). It contradicts the documented formula for g > 0 and at the
clipped ends, and the documented median equivalence for g = 0. Results with finite data are unaffected. All four
builds show it. The dev build of main (2.6.0.dev0 @ 55511445dc) still returns nan for `percentile([1, 2, inf], 50)`.

### 13. `unwrap(period=8, discont=5)`: a step of exactly `discont` is changed (all builds)

What was measured: `np.unwrap([0, 5, 10], discont=5, period=8)` returns `[0, -3, -6]`. The docstring says unwrap changes
"elements which have an absolute difference from their predecessor of **more than** `max(discont, period/2)`". Here
that is max(5, 4) = 5, and the steps are exactly 5, so the expectation is `[0, 5, 10]`. In the library,
`_unwrap_fallback`/`unwrap` in `_function_base_impl.py` (1.x: `function_base.py:unwrap`) zeroes the correction only
`where=abs(dd) < discont`. A step equal to `discont` is therefore corrected, which means "at least", not "more than".
Main's C++ kernel `numpy/_core/src/umath/unwrap.cpp` uses the same test (`if (adiff < discont)`).

Verdict: **documentation / boundary inconsistency**. It matters only when a step equals `discont` exactly, which in
practice happens with integer data and an explicit discont. With the default discont = period/2 the tie handling is
explicit in the code (`ddmod == interval_low & dd > 0`) and gives the same values either way. All builds.

### 14. `histogram_bin_edges(bins='auto')` does not match its documentation (2.4.6 only)

What was measured: heavy-tailed data (n = 5000: 4990 N(0,1) values plus 10 uniform on ±400). Freedman–Diaconis gives
4295 bins, Sturges 14, and sqrt 71. The documented 'auto' is "Minimum bin width between the 'sturges' and 'fd'
estimators", which means 4295 bins. numpy 2.4.6 returns 142. In the library,
`numpy/lib/_histograms_impl.py:_hist_bin_auto` (2.4.6 lines 230–264) now computes
`fd_bw_corrected = max(fd_bw, sqrt_bw / 2); return min(fd_bw_corrected, sturges_bw)`, a "relaxed" FD that caps the
count at 2·sqrt(n). The 2.3.0 release note (gh-28426) says only that the automatic selection "has been modified to avoid
out-of-memory errors for samples with low variation". The public docstring still gives the old rule twice: in the
`bins` parameter text, and in Notes, "'auto' (minimum bin width of the 'sturges' and 'fd' estimators)". The 1.x builds
return 4295, as documented.

Verdict: **documentation gap**. The behaviour change is deliberate and reasonable, but the docstring was not updated. It
affects only 2.3+ builds. The other seven estimators matched their documented formulas exactly on three data sets, and
so did the integer-n_h cases (n = 256, 125, 1000, 196, 1024), in every build.

### 15–17. `np.select` silently wraps out-of-range Python integers (2.4.6 only)

What was measured:
- `np.select([c], [int8 array], default=300)` returns `[1, 44]` with dtype int8.
- `default=-129` gives 127.
- `np.select([c], [300], default=np.int8(1))` gives `[44, 1]` with dtype int8.

The 1.x builds give int16 `[1, 300]` / `[1, -129]` / int64 `[300, 1]`. In the library,
`_function_base_impl.py:select` keeps Python scalars as Python scalars so that NEP 50 weak promotion applies
(`dtype = np.result_type(*choicelist)` gives int8), then broadcasts them into arrays and calls
`result = np.full(result_shape, choicelist[-1], dtype)` followed by `np.copyto(result, choice, where=cond)`.
`np.full` fills through `copyto(..., casting='unsafe')`, so 300 becomes 44 without a warning.

The documentation says: select: "default: The element inserted in `output` when all conditions evaluate to False".
NEP 50 says an out-of-range Python int raises `OverflowError` rather than being truncated. For `np.where`, numpy 2.5.0
fixed exactly this ("`numpy.where` no longer truncates Python integers … Now, an OverflowError will be raised",
gh-30803). The dev build of main still wraps in `select` (`[1, 44]`), because by the time `np.full` sees the value it is
a broadcast int64 array rather than a Python int.

Verdict: **bug** (silent data corruption). It affects 2.x only, and is not yet fixed in main.

### 18. `np.where(c, int8 array, 300)` silently wraps to 44 (2.4.6 only)

What was measured: the result is `[1, 44, 3]` with dtype int8. The 1.x builds give int16 `[1, 300, 3]`. In the library,
`PyArray_Where` in 2.4.6 promotes weakly to int8 and casts the scalar unsafely. The 2.5.0 release note above describes
the fix: `OverflowError` for an out-of-range Python int. The dev build raises
`OverflowError('Python integer 300 out of bounds for int8')`.

Verdict: **bug**, acknowledged and fixed upstream in 2.5.0. It affects 2.0–2.4.

## Information lines (not FAIL)

- `correlate(a, v, 'same')`: the docstring defines 'same' only as "length max(M, N)", so the window it takes from the
  full correlation is not specified. Measured: `full[(min-1)//2 : ...]` when len(a) ≥ len(v). When len(v) > len(a)
  (internal swap followed by reversal), it is `full[min//2 : ...]` for an even shorter length. When M = N = 4 (even),
  swapping a and v does not give the reversed conjugate. No centring of an even window can be symmetric under reversal,
  and the docstring shows the swap relation only for 'full'. The full/valid swap relation holds exactly in every case.
- `piecewise` with overlapping conditions: the later condition wins, while `select` uses the first. The piecewise
  docstring says nothing about priority.
- `interp` with decreasing xp returns `[0, 0, 0]`, which the docstring covers ("results are nonsense"). With NaN in xp
  it returns `[5, nan, nan, 30]` (undocumented). With a repeated xp value it returns the right-hand fp.
- `ediff1d(int array, to_begin=0.5)` raises TypeError under the same_kind rule. The docstring does not mention this.
- `cov(complex)` is Hermitian only to 7e-15 (the diagonal has an imaginary part of 1.7e-16) because of matrix-product
  rounding. The check uses a relative tolerance of 1e-14. The corrcoef docstring does say "may not be Hermitian".
- `sum(float16)` of 20000 values in [0, 100) overflows to inf (float16 result dtype), and so does
  `mean(dtype=float16)`. The default `mean(float16)` uses float32 intermediates as documented and is exact to 1 float16
  ulp.
- 1.x: `bincount([1.5, 2.7])` on a list silently truncates to `[0, 1, 1]` (deprecated in 2.1; 2.4.6 raises a
  DeprecationWarning, which is checked). On 1.x the integer-data 'sqrt'/'fd'/'auto' estimators give 100/20/20 bins for
  values 0..9, because the width ≥ 1 rule is 2.1+.

## What held up (all builds unless noted)

- `nanvar`/`nanstd` for ddof 0–4 are exact. With ddof ≥ the non-NaN count they return NaN with the "Degrees of freedom
  <= 0" warning. All-NaN rows give NaN plus a RuntimeWarning, and keepdims shapes are correct. On 2.x,
  `correction=`/`mean=` work, and giving both ddof and correction raises ValueError.
- `nanmedian`/`nanquantile`/`nanpercentile` with axis tuples (0, 2), (1, 2) and (0, 1, 2), keepdims and q arrays (q
  axis first) are exact. An all-NaN slab gives NaN plus "All-NaN slice encountered". nanmax/nanmin on all-NaN slices
  give NaN plus a warning. nanargmax raises ValueError. nanmean gives "Mean of empty slice", nansum gives 0, nanprod
  gives 1. The dtype and out rules of nanmean/nansum match the docs.
- `average`:
  - Weights along an axis, weights of the same shape, and axis tuples with weights (all builds) are exact.
  - `returned=True` gives sum_of_weights with the same shape and dtype as the result, or the element count when there
    are no weights.
  - keepdims works.
  - ZeroDivisionError is raised both for all-zero weights and for weights that sum to 0.
  - The documented TypeError/ValueError shape errors are raised, and the result-dtype rules hold.
- median/percentile with NaN propagate NaN. `median([-inf, 1, 2, inf]) = 1.5`, `median([-inf, inf]) = nan`, and
  percentile with g = 0.5 next to -inf is correct.
- Weighted quantile (2.4.6): the result equals the smallest x with C(x) ≥ qW and satisfies the coverage conditions
  exactly at 16 values of q, including every CDF step k/10.
  - Integer weights give the same result as repeating each value; unit weights give the unweighted result.
  - A zero-weight minimum at q = 0 is handled.
  - 1-D and 2-D weights work with an axis.
  - The documented errors (other method, negative weights, all-zero weights, 1-D weights without an axis) are raised.
  - nanquantile/nanpercentile drop NaN values together with their weights, and float32 input stays float32.
- histogram2d/histogramdd:
  - The edges are exactly `lo + i(hi-lo)/n`. Counts follow the half-open rule with the last bin closed on every axis,
    including (x_max, y_max) → `H[-1, -1]` and dropping the point one ulp above the range.
  - Weights, density, and density with weights (normalised) are exact.
  - The mixed bins specifications work: int, [edges, int], one array, per-axis `range` with None.
  - The "sequence of D arrays" input form is accepted, and the non-monotonic-edges error is raised.
- histogram_bin_edges: sqrt, sturges, rice, scott, fd, doane and stone all match their documented formulas (stone
  against a plain-Python reference) on n = 37, 200 and 1000. 'auto' matches on those data sets, and in every build on
  1.x. `range=` fills the whole range. An IQR of 0 gives one bin. The weights and unknown-name errors are raised. Empty
  data gives [0, 1]. Integer data has a bin width ≥ 1 (2.1+).
- bincount with weights and minlength is exact. Negative values raise ValueError, and a float ndarray raises TypeError.
- cumsum/cumprod dtypes: int8/int16/int32/bool accumulate as int64 and unsigned types as uint64 on this platform, and
  float32 stays float32. dtype=int8 wraps modulo 2^8, as documented. NaN propagates through cumsum and inf-inf gives
  nan. nancumsum/nancumprod substitute 0 and 1 for NaN. cumulative_sum/prod (2.1+) handle include_initial, 2-D axes,
  the axis-required error, empty input and bool input.
- diff:
  - n = 0/2/3/too large, the negative-n error, and scalar/array prepend/append with broadcasting and the shape error
    all behave as documented.
  - bool inputs give XOR, uint8 wraps (documented), int8 wraps, and datetime64 gives timedelta64 (including a
    leap-year span).
  - ediff1d handles to_begin/to_end and flattening.
- Reduction dtypes follow the documented platform-int/uint rule. Empty sum is 0 and empty prod is 1. `initial=` and
  `where=` work for sum, prod and mean. max/min with initial/where work, and the no-identity errors are raised. ptp on
  int8 wraps to -1 (documented warning), and its NaN, empty, axis and keepdims behaviour is correct.
- convolve/correlate:
  - For 13 (M, N) pairs with odd, even, swapped, equal and length-1 inputs, all complex, full/valid/same match exact
    sums: convolution `a_m v_(n-m)`, correlation `a[n+k] conj(v[n])`.
  - The documented reversed-conjugate swap relation holds for 'full', and the default mode of correlate is 'valid'.
  - The docstring examples, integer exactness, float32 dtype and errors hold.
- piecewise: functions, scalars, the extra default function, length errors, a single-array condlist, the output taking
  the type of x (documented truncation), *args/**kw and 0-d x all behave as documented.
- select: first-true priority, condlist broadcasting, scalar choices, NaN default promotion and the errors behave as
  documented. where: scalar dtypes, broadcasting, the condition-only form and the error behave as documented.
- interp: 54 points are exact, including at every xp. left/right apply only outside the range. The periodic docstring
  example is exact, and so are the periodic extension on 30 angles and radians near 0 and 2π. Complex fp works,
  including complex left/right. The errors are raised, and float32 input returns float64.
- trapezoid: non-uniform x, dx, the default dx, decreasing x (negated), 2-D with a 1-D x on either axis, x with the
  same shape as y, a single sample and empty input are all exact.
- gradient:
  - With edge_order 1 and 2, uniform and non-uniform spacing match the Lagrange-interpolant derivative to 1e-13; the
    second-order non-uniform one-sided stencils are the documented Fornberg weights.
  - A quadratic is differentiated exactly by edge_order = 2.
  - The docstring example holds.
  - The 2-D varargs forms work: a scalar for all axes, scalar plus coordinates, axis, and an axis tuple.
  - The errors are raised.
  - uint8 data and uint8 decreasing coordinates are handled without wraparound, and float32 stays float32.
- unwrap:
  - It recovers a 60-step random phase to 1e-12, and |diff| ≤ π afterwards.
  - The docstring examples hold (radians, and period 6 and 4 with integer dtype), and so does the degree example.
  - The discont rule (None, 1, 4, 5 with period 8) is exact except at the tie in FAIL 13.
  - axis handling is correct.
- angle(deg=True) is correct to 1 ulp, and signed zeros follow atan2 (-1-0j → -180).
- clip: a_min > a_max gives a_max, array bounds broadcast, and NaN is preserved. On 2.1+, clip with no bounds and the
  min/max keywords work. On 1.x, clip with no bounds raises ValueError.
- cov:
  - rowvar=False, bias, ddof, and ddof overriding bias are exact.
  - y is stacked for both rowvar settings.
  - 1-D inputs give 2x2 or 0-d results.
  - Complex input computes (x-m)·conj(y-m)/(N-1) exactly.
  - The dtype parameter works, the fweights/aweights errors are raised, and N - ddof = 0 gives a warning with a
    non-finite result.
- corrcoef:
  - Complex input is exact and clipped.
  - 300 exactly correlated pairs with offsets up to 1e6 never gave |r| > 1.
  - A constant row or a NaN row gives NaN for that row and column.
  - `bias=` gives a DeprecationWarning with no effect on 1.x and a TypeError on 2.4 (removed, per the release note).
- mean(float16) uses float32 intermediates, as documented. complex var/std are real and exact, and complex64 gives
  float32. median of even-length int, int8 and uint8 arrays gives the float mean without overflow. percentile with a 2-D
  q gives the documented shape, out= returns out, and the wrong-shape error is raised. quantile rejects q outside
  [0, 1] and NaN. count_nonzero works with axis tuples and keepdims, NaN counts as nonzero and -0.0 does not.
  apply_over_axes works with reducing, shape-preserving and scalar-axis functions, and its error is raised.

## Not checked, and why

- `np.sinc`, `np.einsum`, and masked-array `average`/`ma.cov` are out of scope for this group.
- The window that correlate 'same' takes for even lengths is recorded but not judged, because it is undocumented.
- The 'stone' upper bound of `max(100, sqrt n)` candidate bin counts, and its "may be suboptimal" warning, are
  implementation details. The reference uses the same candidate range, and the upper-bound warning was not triggered.
- Timing and performance, and `overwrite_input=`: no documented numerical contract.
- The dev build of main (2.6.0.dev0) is not one of the audited builds. It was used only to confirm whether FAILs 1,
  15–18 are still present upstream (1 and 15–17 are; 18 is fixed in 2.5.0).
