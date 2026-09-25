# NumPy: descriptive statistics, quantiles, histograms, fitting, calculus, linear algebra, FFT and random numbers

_Reviewed 2026-09-25 against `numpy/numpy` `main` @ `55511445dc` by reading, and executed on the
2.4.6 release (the current one) and on 1.23.5, 1.24.4 and 1.26.4 (the cohort's 1.19–1.26 range
as far as Python 3.11 wheels reach). Harnesses and outputs in `../verify/`; every number is
checked against an exact recomputation (`fractions.Fraction`, `mpmath`) or a closed-form
definition._

## What the cohort uses (253 papers, `../numpy_profiles.jsonl`, survey-cache lower bounds)

| use | papers |
|---|---|
| SciPy / Matplotlib / pandas / scikit-learn alongside | 147 / 135 / 69 / 64 |
| image or array processing | 86 |
| sorting / unique / ranking | 43 |
| normalisation / z-scores | 40 |
| random numbers, permutations, bootstraps | 29 |
| mean / median / SD | 28 |
| integration (trapezoid, cumsum) | 22 |
| eig / SVD / linear algebra | 20 |
| correlation (corrcoef, Pearson) | 19 |
| histograms / binning | 12 |
| FFT, smoothing, interpolation, polyfit | 9 / 9 / 8 / 5 |
| version stated | 26 (1.19 ×15 mentions, 1.24 ×11, 1.26 ×9, 1.21 ×9, 1.23 ×8, 1.20 ×8) |

NumPy sits under everything else in the cohort: the numbers papers report come out of `mean`,
`std`, `median`, `percentile`, `corrcoef`, `polyfit`, `histogram`, `linalg.eig`/`lstsq`,
`fft` and the random generators, usually on float64 data, sometimes on float32 image stacks
or recordings.

## Code read

`numpy/_core/fromnumeric.py` and `_methods.py` (`mean`, `var`, `std`, `sum` and their Notes),
`numpy/lib/_function_base_impl.py` (`percentile` / `quantile` and the thirteen methods, `median`,
`average`, `cov`, `corrcoef`, `histogram` and the bin estimators, `digitize`, `interp`, `gradient`,
`trapezoid`), `numpy/lib/_polynomial_impl.py` (`polyfit` incl. the covariance scaling and
weights), `numpy/linalg/_linalg.py` (`lstsq`, `matrix_rank`, `pinv` cut-offs), `numpy/fft`, and
`numpy/random` (`Generator`, `RandomState`, `choice`, `multivariate_normal`). Statement of
intended behaviour: the docstrings, Hyndman & Fan (1996) for the quantile methods, and the
NumPy 2.0 / 2.1 release notes.

## Findings

Nothing in the routines above returned a wrong number for the definition it documents. The
audit's yield is a set of documented behaviours whose size, measured on cohort-like inputs, is
worth knowing, and two already-fixed or already-open items.

### N1 — `mean` / `sum` / `var` of a float32 array along the sample axis use naive summation; the error grows with the number of rows

`np.sum`'s Notes say that the pairwise summation that keeps float32 sums accurate "is only used
when the summation occurs along the fast axis in memory". For the ordinary layout of tabular and
image data — a C-ordered `(n_samples, n_features)` or `(n_frames, height, width)` array reduced
over axis 0 — that is never the case, and the accumulation is a plain running float32 sum
(`../verify/n4_float32_and_edge_cases.out`, identical on 1.23.5–2.4.6):

| float32 input | relative error of `mean(axis=0)` | same column made contiguous |
|---|---|---|
| (2000, 64, 64) image stack, values 1000 ± 50 | 2.2 × 10⁻⁶ | 1.1 × 10⁻⁷ |
| (200 000, 10) matrix, values 100 ± 1 | 1.4 × 10⁻⁵ (variance 5.5 × 10⁻⁵) | — |
| (1 000 000, 4) matrix, values ~1500 | 4.1 × 10⁻⁴ (variance 4.3 × 10⁻⁴) | 8 × 10⁻⁹ |
| (5 000 000, 2) matrix, values 100 ± 1 | **2.9 × 10⁻²** | 2.9 × 10⁻⁸ |

Passing `dtype=np.float64` removes the error entirely. z-scores computed from the float32
column statistics of the (200 000, 10) matrix are off by up to 1.5 × 10⁻³ and no longer average
to zero. The behaviour is documented in `np.mean`'s Notes (float32 example) and `np.sum`'s
Notes, and is the subject of the open issues numpy/numpy#22956 (2023, "np.mean(axis=0) return
incorrect value for a large size float32 array") and #8869 (2017, "numpy.mean along multiple
axis gives wrong result for large arrays"), with the summation-algorithm discussion in #8786.
Nothing to file; recorded here because the cohort's float32 use (recordings, image stacks,
single-cell matrices) is exactly the layout the pairwise path does not cover.

### N2 — `percentile(method="closest_observation")` picked the odd order statistic at ties before 2.1.0

Hyndman & Fan's method 3 takes the *even* order statistic when `np − ½` is an integer; NumPy
1.22–2.0 took the odd one (commit 5a3ba2a8f0, 2024-06-20, "BUG: Quantile closest_observation to
round to nearest even order", released in 2.1.0). On 1.23.5–1.26.4 the harness sees it at three
of fifteen probabilities for n = 5 and n = 257 (`n1_descriptive_statistics.v1.26.4.out`); the
other twelve methods, including the default `linear`, match the H&F definitions exactly on every
version. Fixed upstream; no cohort paper names this method.

### N3 (note) — `multivariate_normal` with a covariance that is not positive semi-definite draws from V |Λ| Vᵀ

With `check_valid='warn'` (the default) a non-PSD covariance gives a `RuntimeWarning` and samples
whose covariance is the SVD reconstruction with the absolute singular values: for `[[1, 2], [2,
1]]` the sample covariance is `[[2, 1], [1, 2]]`, not the PSD part `[[1.5, 1.5], [1.5, 1.5]]`
(`n3_linalg_fft_random.out`). The docstring says the behaviour is undefined in that case; the
warning is the only signal, and its tolerance (`allclose` with `rtol=1e-5`, `atol=1e-8`) lets
slightly negative eigenvalues through silently, which is harmless.

### N4 (note) — `fft` of float32 input is computed in single precision since 2.0

NumPy 1.x always transformed in float64 (`complex128` result, identical to the float64
transform); 2.0 keeps the input precision (`complex64`, relative error 5 × 10⁻⁸ on a 65 536-point
transform, 4 × 10⁻⁷ on the power spectrum). Documented in the 2.0 release notes; an upgrade
changes float32 spectra at the 1e-7 level.

### N5 (note) — `round` is the documented multiply–rint–divide, so `np.round(2.675, 2)` is 2.68 where Python's `round` gives 2.67

Documented in `np.round`'s Notes. `np.round(1.005, 2)` is 1.0 like Python's.

## Held up

| what | harness | result |
|---|---|---|
| `mean`, `var`/`std` (ddof 0 and 1), `median` (odd and even n), `average(weights=)`, the nan-variants | `n1` | exact |
| `percentile`/`quantile`: all 13 methods vs Hyndman & Fan at 15 probabilities for n = 5, 8, 257 (2.x); 12 of 13 on 1.x (N2) | `n1` | exact |
| `cov` (ddof, bias, fweights, aweights: factor v1 − ddof·v2/v1), `corrcoef` (= cov/√(var var), clipped to [−1, 1]) | `n1` | exact |
| `histogram`: half-open bins with a closed last bin, explicit edges, `density`, `range` dropping outliers, `bins='auto'` = min(Freedman–Diaconis, Sturges); float32 data on float64 edges and float32 data ~1e6 | `n2`, `n4` | exact |
| `digitize` (both `right` conventions), `searchsorted` | `n2` | exact |
| `polyfit`: coefficients, `full=True` residual, `cov=True` = RSS/(n − deg − 1)·(AᵀA)⁻¹, `cov='unscaled'`, `w` multiplies residuals (w = 1/σ); degree 3 on x = 2000…2020 within 1e-8 of the exact cubic | `n2` | exact |
| `interp` (linear, clamped ends, `left`/`right`, `period`), `trapezoid`, `gradient` (central; edge orders 1 and 2; uneven spacing second-order) | `n2` | exact |
| `lstsq`, `eig`, `eigh`, `svd`, `norm`, `det`, `solve`, `matrix_rank`/`pinv`/`lstsq` cut-offs | `n2`, `n3` | exact |
| `fft`/`ifft`/`rfft` against an explicit DFT, `norm` options, `fftfreq`, Parseval | `n3` | 1e-11 |
| `default_rng` and `RandomState` reproducibility (the documented frozen streams), `choice(p=)` tolerance and frequencies, `integers`/`randint` bounds, `permutation`, `shuffle` axis, `multivariate_normal` on a PSD covariance, `binomial`/`normal`/`exponential`/`gamma` moments | `n3` | as documented |
| `unique` collapsing NaNs (1.24+), `round` half to even, `linspace` endpoints, `arange` float steps, `isclose` asymmetry, `diff` on unsigned integers, integer accumulators for `mean`/`sum`/`var`, float16 mean via float32 | `n2`, `n4` | as documented |

## Version scope (executed)

| item | affected | unaffected |
|---|---|---|
| N1 | 1.23.5, 1.24.4, 1.26.4, 2.4.6 (all) | contiguous reductions; `dtype=np.float64` |
| N2 | 1.23.5, 1.24.4, 1.26.4 (1.22–2.0) | 2.1.0+ (2.4.6 executed) |
| N3, N5 | all | — |
| N4 | 2.0+ (2.4.6) | 1.x |
