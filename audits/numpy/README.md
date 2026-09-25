# NumPy audit against 253 published papers (2021–2026)

_Generated 2026-09-25 against `numpy/numpy` `main` @ `55511445dc` by reading, executed on the
2.4.6 release and on 1.23.5, 1.24.4 and 1.26.4. Focus: the routines whose numbers reach the
papers — descriptive statistics and quantiles, histograms, polynomial fitting, interpolation and
integration, correlation, linear algebra, FFT and the random generators — checked against exact
recomputations._

## What this is

The six-journal survey found **253 papers** in PNAS, *Nature*, *Cell* and *Science*, 2021–2026,
that name NumPy in their methods, nearly always beside SciPy (147), Matplotlib (135), pandas (69)
or scikit-learn (64); 86 use it for image or array processing. Every function in the list above
was exercised on generated data and compared with a `Fraction`/`mpmath` recomputation or the
published definition (Hyndman & Fan for the quantile methods, an explicit DFT for the FFT, the
normal equations for `polyfit` and `lstsq`).

## Findings (details in [`component-reviews/statistics-fitting-linalg-random.md`](component-reviews/statistics-fitting-linalg-random.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| N1 | note, documented; open upstream as numpy/numpy#22956 (2023) and #8869 (2017) | held (nothing to add) | `mean`/`sum`/`var` of a float32 array along the sample axis (axis 0 of the usual C-ordered layout) use a plain running sum, not the pairwise summation used for contiguous data: 2.2e-6 relative on a 2,000-frame image stack, 1.4e-5 on a (200,000 × 10) matrix, 2.9e-2 on (5,000,000 × 2). `dtype=np.float64` removes it. |
| N2 | fixed upstream in 2.1.0 (commit 5a3ba2a8f0) | held | `percentile(method="closest_observation")` took the odd order statistic at ties on 1.22–2.0; the default `linear` and the other eleven methods are exact on every version. |
| N3 | note, documented as undefined | held | `multivariate_normal` with a non-PSD covariance warns and samples from V|Λ|Vᵀ (for `[[1,2],[2,1]]`: sample covariance `[[2,1],[1,2]]`). |
| N4 | note, release-noted | held | Since 2.0 `fft` of float32 input is computed in single precision (`complex64`, 5e-8 relative), where 1.x transformed in float64. |
| N5 | note, documented | held | `np.round(2.675, 2)` is 2.68 (multiply–rint–divide), Python's `round` gives 2.67. |

**Held up under execution (all four builds):** `mean`, `var`, `std`, `median`, `average`,
`nanmean`/`nanstd`/`nanmedian`/`nanpercentile`; all thirteen `percentile` methods (2.x) against
Hyndman & Fan; `cov` with `ddof`/`bias`/`fweights`/`aweights`; `corrcoef`; `histogram` (edge
rules, `density`, `range`, `'auto'`, float32 data); `digitize`; `searchsorted`; `polyfit`
(coefficients, residual, `cov` scaling, weights, conditioning on year-valued abscissae);
`interp`; `trapezoid`; `gradient`; `lstsq`; `eig`/`eigh`/`svd`/`solve`/`det`/`norm`/`matrix_rank`
/`pinv`; `fft`/`ifft`/`rfft`/`fftfreq`; `default_rng`/`RandomState` streams, `choice`,
`integers`, `permutation`, `shuffle`, `multivariate_normal`, `binomial`, `normal`, `exponential`,
`gamma`; `unique` with NaN, `round`, `linspace`, `arange`, `isclose`, unsigned `diff`, integer
accumulators, float16 means. Not checked: masked arrays, `einsum`, `convolve`/`correlate`,
`polynomial.Polynomial`, `savetxt`/`loadtxt`, datetime arithmetic.

## Verification method

`verify/n1_descriptive_statistics.py` (moments, medians, the thirteen quantile methods, nan
variants, `cov`/`corrcoef`, float32 slow-axis reductions), `n2_fitting_binning_calculus.py`
(`histogram`, `digitize`, `polyfit`, `interp`, `trapezoid`, `gradient`, `lstsq`, `unique`,
`round`), `n3_linalg_fft_random.py` (decompositions, cut-offs, DFT, the generators),
`n4_float32_and_edge_cases.py` (realistic float32 shapes, float32 histograms and percentiles,
integer and float16 inputs). Each runs under the interpreter given; `.out` is 2.4.6,
`.v<version>.out` the 1.x builds.

## How the papers use NumPy (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 26 (1.19 ×15 mentions, 1.24 ×11, 1.26 ×9, 1.21 ×9, 1.23 ×8, 1.20 ×8) |
| SciPy / Matplotlib / pandas / scikit-learn alongside | 147 / 135 / 69 / 64 |
| image or array processing | 86 |
| sorting, unique, ranking | 43 |
| normalisation / z-scores | 40 |
| random numbers, permutations, bootstraps | 29 |
| descriptive statistics | 28 |
| integration; linear algebra; correlation | 22; 20; 19 |
| histograms; FFT; smoothing; interpolation; polyfit | 12; 9; 9; 8; 5 |

The profile (`numpy_profile.py`, `numpy_profiles.jsonl`, `profile_run.log`) ran on the survey's
stored evidence sentences (no route to Europe PMC from this session), so the counts are lower
bounds.

## Filing channel

Nothing to file: the one behaviour with a measurable effect on cohort-like data (N1) is
documented and has open upstream issues since 2017 and 2023; N2 is fixed. NumPy's AI policy
(`doc/source/dev/ai_policy.rst`: disclosure of any AI-generated code or text in the PR, rejection of
undisclosed use) and templates are recorded in [`upstream/README.md`](upstream/README.md) for any
later filing.

## Files

| path | what |
|---|---|
| `component-reviews/statistics-fitting-linalg-random.md` | the review: N1–N5, held-up list, version scope |
| `verify/n1_…py` … `n4_…py`, `*.out`, `*.v<version>.out` | harnesses and captured output per build |
| `numpy_profile.py`, `numpy_profiles.jsonl`, `profile_run.log` | cohort profile |
| `upstream/README.md` | filing channel notes (nothing filed) |
