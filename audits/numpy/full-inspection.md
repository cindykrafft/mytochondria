# NumPy full inspection: findings ledger

_Full inspection requested 2026-09-25, independent of the survey. Nine harness groups (`verify/n5` …
`n13`, plus round 6's `n1` … `n4`) executed on 2.4.6 and on 1.23.5, 1.24.4 and 1.26.4 against exact truths
(Fraction, mpmath at 30–200 digits, Python's own `datetime`/`str`/`math`/`cmath`, plain-Python
reimplementations), and checked against a source build of `main` @ 55511445dc (2.6.0.dev0) where the
question was whether a finding is already fixed. Each group's `verify/<group>.notes.md` has one paragraph
per failing check with the source lines. "By hand" means reproduced again outside the harness. Nothing is
filed._

## Bugs in the current release (2.4.6) still on `main`

| id | finding | builds | by hand | prior report | fix |
|---|---|---|---|---|---|
| NP1 | `MT19937.jumped()` does not jump the stream: jump-then-draw-700 and draw-700-then-jump agree on 0 of 2,300 outputs (PCG64: 2,300 of 2,300); the documented 2^128 spacing does not hold | 1.23–main | yes | #15394 (2020, closed) to be read | — |
| NP2 | `RandomState.set_state` / the `MT19937.state` setter accept an out-of-range `pos`; the next draw segfaults | 1.23–main | yes | — | memory safety: NumPy's security channel, not a public issue |
| NP3 | `np.unique` hash path (2.3+): `equal_nan=False` collapses NaT; the complex NaN representative differs from the sorting path | 2.4 | yes | #30113 related | branch, verified on a source build |
| NP4 | quantile interpolation next to ±inf returns NaN (`percentile([1, 2, inf], 50)` is nan, `median` 2.0; 0th/100th percentiles nan) | 1.23–main | yes | #12282 (2018), #21091 (2022) open | known |
| NP5 | `np.select` wraps an out-of-range Python int default into the result dtype (300 → 44 in int8) | 2.x–main (1.x promoted) | yes | none found | — |
| NP6 | datetime64 construction wraps silently: a 2020 timestamp with 10 fraction digits becomes 1969-11-25; 2263 in ns becomes 1678 | 1.23–main | yes | #9956 (2017), #31926, #5452 | known |
| NP7 | `timedelta64 // int` truncates toward zero (−7 µs // 2 = −3 µs) | 1.23–main | yes | none found yet | — |
| NP8 | `np.ma.corrcoef` on masked 2-D input returns 1.2247 (1.0 on 1.26.4) | 2.1–main | yes | none found yet | — |
| NP9 | `zipf` for a near 1 accepts every proposal above 2^53 (both APIs; CDF off by up to 88 standard errors) | 1.23–main | harness | none found yet | — |
| NP10 | StringDType `lstrip`/`strip` with multi-byte characters in `chars` skip later characters | 2.x–main | harness | none found yet | — |
| NP11 | `Polynomial.integ()` applies the default `lbnd` in window coordinates, an explicit one in domain coordinates | 1.23–main | harness | #9533, #26491 related | — |
| NP12 | Unicode case mappings (`np.char`/`np.strings` upper/swapcase/title) truncate to the itemsize ('ß' → 'S') | 1.23–main | harness | — | — |
| NP13 | int8 masked arrays: the default fill value 999999 wraps to 63 silently | 1.23–main | harness | — | — |
| NP14 | Legacy `RandomState` only: dirichlet with tiny alphas gives NaN rows; `negative_binomial` / `geometric` return INT64_MIN; `wald` cancellation; `zipf(2000)` hangs (fixed for Generator) | 1.23–main | harness | — | legacy stream is frozen: likely docs or errors, not stream changes |

## Documentation errors and gaps (still on `main`)

FFT module "Type Promotion" paragraph (float32 is single precision since 2.0); `rfft` "silently discarded"
(TypeError in 2.x, ComplexWarning in 1.x); `irfftn` round-trip idiom without `axes`; `histogram_bin_edges('auto')`
rule changed in 2.3; `unwrap` boundary at |step| == discont; `shares_memory(max_work=0)`; `bincount` of a
float list; the five `*weight` functions reject lists; `np.polyder` return type; Philox `advance` wording;
`ma.cov` of a single 2-D x; qr sign convention and `eig` NaN input (notes).

## Fixed on `main` or in a later release (nothing to file)

`hfft(out=)` (845f93ce51), `np.where` Python-int wrap (2.5), StringDType replace/partition with long
patterns, invalid UTF-8 cast and `na_object` comparisons (main), pad reflect/symmetric/wrap with large widths
(1.25/2.0), complex-step `mgrid` (1.24), `closest_observation` (2.1), float64 SVML accuracy on AVX-512
(1.25/2.x), `ljust`/`rjust` narrowing (2.0), zoneinfo tz (2.4), `busday_count` reversed ranges (1.25),
Generator wald/geometric/zipf (1.25–2.3).

## Held up

Every check in each group's "held up" list: all ufuncs within the validation-set ulp bounds on 2.x, the
promotion and casting tables, sorting and set operations on every dtype, the whole linear-algebra surface
against mpmath, the polynomial package against exact algebra, every distribution's moments, every FFT to
7.6e-16, the statistics and reductions, array manipulation, and the dtype/io/printing surface.
