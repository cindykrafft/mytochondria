# n5_ufuncs_arithmetic_casting — notes

Harness: `audits/numpy/verify/n5_ufuncs_arithmetic_casting.py` (409 checks). Truths: `fractions.Fraction`,
`mpmath` at 200 bits, Python's own `round` / `//` / `%` / `math` / `cmath` (C99 Annex G), hand-written
implementations of the documented rules (two's-complement wrap, the `reduceat` slice rules, the
promotion lattice), and IEEE-754 constants. Builds: numpy 2.4.6 (`.out`), 1.23.5, 1.24.4, 1.26.4
(`.v<ver>.out`); all on the same x86-64 host with AVX512_SKX (SVML paths engaged). Runtime ~4 s per build.

Counts: 2.4.6 — 409 ok / 0 FAIL; 1.26.4 — 402 ok / 3 FAIL; 1.24.4 — 400 ok / 5 FAIL; 1.23.5 — 400 ok / 5 FAIL.
(The 1.x builds run fewer checks because some 2.x-only checks are replaced by their 1.x counterparts.)

Accuracy is reported two ways: "ulp vs exact" (|y − t| / spacing at the correctly rounded truth) and
"steps" (number of representable values between y and the correctly rounded truth, which is what NumPy's
own `assert_array_max_ulp` counts). The pass criterion is the steps measure against the tolerance NumPy
itself asserts in `numpy/_core/tests/data/umath-validation-set-<func>.csv` (float64: 1 for every
function except cbrt/tanh = 2; float32: 2–4 depending on the function).

## FAIL lines

### `FAIL sin float64: max error 2.29 ulp vs exact, 2 representable steps ...` and `FAIL cos float64: max error 2.41 ulp ...` — builds 1.23.5, 1.24.4

Measured: over 646 float64 points in [−1e−3, 1e−3] ∪ [−10, 10] ∪ [−1e5, 1e5] ∪ [1e9, 1e10] plus 1e10,
1e15, 1e22, `np.sin` is 2 representable doubles away from the correctly rounded value (2.29 ulp vs
mpmath) at x = −1.82078879…, `np.cos` 2.41 ulp at x = 3.16799966…. The large arguments themselves are
fine (≤ 0.5 ulp at 1e22 on every build — range reduction is exact).
What the library does: on Linux + AVX512_SKX, numpy 1.22–1.24 dispatch float64 `sin`/`cos` to Intel
SVML's default-accuracy kernels (`__svml_sin8`, `__svml_cos8`; symbols present in the 1.23.5 and 1.24.4
`_multiarray_umath` shared objects, no `_ha` variants linked), introduced in 1.22 ("Vectorize umath
module using AVX-512 ... 18 umath functions ... for both single and double precision", 1.22.0 release
notes). Intel specifies those kernels at ≤ 4 ulp. Since 1.25 the float64 sin/cos loops were reverted
to libm: `numpy/_core/src/umath/loops_trigonometric.dispatch.cpp`: "/* Disable SIMD code sin/cos f64
and revert to libm: see https://mail.python.org/archives/list/numpy-discussion@python.org/thread/
C6EYZZSR4EWGVKHAZXLE7IBILRMNVK7L/ */". 1.26.4 and 2.4.6 measure 0.50 ulp (correctly rounded, glibc).
What the docs say: nothing about accuracy in the `sin`/`cos` docstrings; NumPy's own validation data
asserts 1 step for float64. Verdict: real accuracy regression of 1.22–1.24 on AVX-512 hardware,
acknowledged on the numpy-discussion thread cited in the source and fixed upstream in 1.25; users pinned to 1.22–1.24 on AVX-512
servers get up to ~2.5 ulp instead of ≤ 1. Not a harness limitation.

### `FAIL tan float64: max error 1.70 ulp vs exact, 2 representable steps ...` — builds 1.23.5, 1.24.4, 1.26.4

Measured: 2 steps (1.70 ulp) at x = −1.26147262…, in the [−1.5, 1.5] sample. 2.4.6: 0.51 ulp / 1 step.
Library: float64 `tan` goes through `loops_umath_fp.dispatch.c.src` (`#func = exp2, log2, log10, expm1,
log1p, cbrt, tan, asin, acos, atan, sinh, cosh, asinh, acosh, atanh#`), which under
`NPY_HAVE_AVX512_SKX && NPY_CAN_LINK_SVML` calls `__svml_@func@@func_suffix@`. In the 1.x builds the
suffix is the default-accuracy `8` kernel; in numpy main (and the 2.4.6 wheel, which measures ≤ 1 step
for every function) the file sets `#func_suffix = f16, 8_ha#`, i.e. the SVML "high accuracy" (≤ 1 ulp)
kernels for float64. (The 1.26.4 wheel links the `_ha` symbols but its measured errors are identical to
1.23.5's, so its dispatch still calls the default kernels.) Docs: none on accuracy; validation set says
1 step. Verdict: same SVML accuracy issue, fixed in 2.x by the switch to `_ha`; documentation gap that
the 1.x accuracy on AVX-512 differs from other hardware.

### `FAIL arcsin float64: max error 1.88 ulp vs exact, 2 representable steps ...` — builds 1.23.5, 1.24.4, 1.26.4

Measured: 2 steps (1.88 ulp) at x = 0.50710604… (the [−1, 1] sample). 2.4.6: 0.70 ulp / 1 step.
Same mechanism and verdict as `tan` (`__svml_asin8` vs `__svml_asin8_ha`).

### `FAIL log10 float64: max error 1.57 ulp vs exact, 2 representable steps ...` — builds 1.23.5, 1.24.4, 1.26.4

Measured: 2 steps (1.57 ulp) at x = 1.01808218… (the [0.9, 1.1] sample near the zero of log10). 2.4.6:
0.52 ulp / 1 step. Same mechanism and verdict as `tan` (`__svml_log108` vs `__svml_log108_ha`).

Related, not failing under NumPy's own steps measure but visible in the "ulp vs exact" column on the 1.x
builds: exp 1.27, log 1.45, log2 1.38, log1p 1.17, arccos 1.26, sinh 1.41, cosh 1.48, arctanh 1.03,
arctan2 1.34 (1.24.4/1.26.4) — all ≤ 1 step but well above the 0.5–0.75 ulp of 2.4.6. float32 SIMD paths
are within NumPy's stated tolerances on every build (2.4.6: exp 1.64 ulp/2 steps ≤ 3, log 2.11/2 ≤ 4,
sin 0.89, cos 0.93, tan 1.54/2 ≤ 4, arcsin 1.85/2 ≤ 4, …); float16 is ≤ 1 step everywhere.

## Things recorded as `ok` that deserve a note (documented, or undocumented but consistent)

* `np.spacing(finfo.max)` is `inf` with an "overflow encountered in spacing" RuntimeWarning (float64 and
  float32, all builds): it is implemented as `nextafter(x, +inf) − x`. The docstring's invariant ("no
  representable number between x + spacing(x) and x") still holds, but "distance to the nearest adjacent
  number" (2^971 for float64 max) does not. Documentation gap.
* `np.reciprocal(np.array([0]))` returns int64 min with a "divide by zero" warning; the docstring says
  "For integer zero the result is an overflow". Documentation nit.
* `promote_types` is not associative for 28 of 2744 triples (e.g. (int8, uint8) → int16, then with
  float16 → float32, but int8 with (uint8, float16 → float16) → float16), and `np.result_type(int8,
  uint8, float16)` is float16 on every build, i.e. multi-argument `result_type` is not the left-to-right
  pairwise reduction. Nothing in `arrays.promotion.rst` claims associativity; documentation gap only.
* 2.x `np.clip(int8_array, -200, 200)` returns the array unchanged (int8) although `np.minimum(int8_array,
  200)` raises OverflowError under NEP 50: `_core/_methods.py::_clip` deliberately drops Python-int bounds
  that are outside the dtype's range ("If min/max is a Python integer, deal with out-of-bound values
  here"). Sensible, undocumented in the `clip` docstring. On 1.x the same call promotes to int16.
* `np.round(int8 [127], -1)` gives −126: 130 is computed in float and cast back to int8, wrapping.
* `np.sinc` at nonzero integers is ~4e−17, not 0 (inherent to sin(πx)/(πx) with rounded πx); its accuracy
  is absolute (≤ 3 eps measured on [−100, 100] for float64/32/16), so relative error near the zeros is
  unbounded (up to 1.6e4 ulp measured) — the definition, not a bug.
* `np.rad2deg` float32 is 1.34 ulp (multiplication by a rounded 180/π); tolerance set to 2 for float32.
* float→int casts of NaN/±inf/out-of-range values (documented undefined): int64/int32 → INT_MIN,
  int8/uint8 → 0, uint64 → 2^63 for NaN and −inf, 0 for +inf; −3.99 → uint8 253 (wraps). Since 1.24 a
  "invalid value encountered in cast" RuntimeWarning is emitted (1.23.5: silent).
* Sum of int64/uint64 arrays at the boundary wraps silently (max + 1 → INT64_MIN / 0); the other widths
  are exact because the accumulator is int64/uint64. `np.add.accumulate`/`reduceat` on int8 keep int8
  (no upcast; the upcast is documented only for `reduce`).
* `np.add.accumulate` on float32 is a naive running sum (1.5e−5 relative error for 1e6 terms) while
  `np.add.reduce`/`sum` are pairwise (4e−8 on 2.4.6, 1.2e−7 on 1.x).
* `left_shift`/`right_shift` by ≥ width give 0 / sign-fill (the C UB is guarded in
  `npy_math_internal.h.src::npy_lshift/npy_rshift`), equal to Python's big-int shift reduced mod 2^bits;
  a negative count is treated as ≥ width (cast to size_t).
* `gcd(int64 min, 2^62)` = 2^62 despite |int64 min| overflowing; `lcm` on int8 wraps silently.
* Version differences encoded and verified: NEP 50 table (2.x) vs value-based promotion (1.x);
  `can_cast(300, uint8)` TypeError on 2.x / False on 1.x; `sign(3+4j)` = x/|x| on 2.x, 1+0j on 1.x;
  `floor`/`ceil`/`trunc` keep integer dtype from 2.1 (rint stays float64); `clip` with a scalar NaN bound
  and `clip(float, out=int)` follow the deprecated paths on ≤ 1.24 (`_clip_dep_is_scalar_nan`,
  `_clip_dep_invoke_with_casting`) and the strict paths from 1.25; `nextafter(float32(1), 2)` is float64
  on 1.x.

## What held up (all four builds unless stated)

Rounding: `round`/`around` half-to-even on binary halves incl. −0.0; `round(x, decimals)` equals the
documented `true_divide(rint(a*10**d), 10**d)` for positive and negative decimals (0.125→0.12, 0.375→0.38,
2.675→2.68, 56294995342131.5→…51, 250→200); integers with negative decimals equal Python's `round`; float32
rounding in float32; rint/floor/ceil/trunc/fix vs `math`, with C99 signed zeros; complex rounding per part.
Division: floor_divide/remainder/mod/fmod/divmod on ints and floats equal Python's `//`, `%`, `math.fmod`,
`divmod` including signed zeros; int division by zero → 0 with RuntimeWarning (raise under errstate);
float division by zero → IEEE inf/−inf/nan; `a = a % b + b*(a//b)`.
Integer overflow: add/sub/mul/neg/abs/square/power wrap modulo 2^bits for int8…int64/uint8…uint64 arrays
silently, scalars wrap identically with RuntimeWarning('overflow'), errstate(over='raise') raises for
scalars only; abs(int min) = int min; `-uint8(1)` = 255.
power: int ** negative int → ValueError; 0**0 = 1; 0.0**−1 = inf; (−8)**(1/3) = nan; int64 3**41 wraps;
float_power always ≥ float64; reciprocal on ints; square.
gcd/lcm with zeros/negatives/int8; bitwise and/or/xor/invert on signed ints vs Python; shifts.
Accuracy (2.4.6): every float64 function ≤ 1 step (exp/log/sqrt/sin/cos/tan/arctan/arcsinh/arctanh/hypot
0.50 ulp, arcsin 0.70, cosh 0.75, tanh 0.90, i0 2.94 ulp vs mpmath besseli within the documented 5.8e−16),
sin/cos/tan at 1e10/1e15/1e22/1e300 exact range reduction (≤ 0.5 ulp), float32 SIMD within NumPy's
tolerances, float16 ≤ 1 step; arctan2 C99 special-value table (signed zeros, ±inf) for float64/float32;
logaddexp identities; sinc(0)=1, sinc(0.5)=2/π; deg2rad(180)=π exactly; exp2(10)=1024, exp2(−1074).
Complex: sqrt/log/angle/arcsin/arccos/arctanh/arccosh branch cuts with signed zeros equal `cmath`
(C99 Annex G), abs via hypot (no overflow, inf with nan), power principal roots.
clip (a_min > a_max → a_max, NaN propagation, dtype rules, out=, in place), isclose asymmetry and
equal_nan and the 1e−9 vs 2e−9 default-atol trap, sign/signbit/copysign on ±0 and ±nan, nan_to_num
(defaults, custom, float32, ints untouched, complex per part, copy=False), errstate/seterr/geterr/call
handler/all modes, sqrt/log(−1) nan+invalid, log(0) −inf+divide, inf−inf, inf·0, overflow/underflow.
astype: 121 dtype pairs × boundary values — 461 exactly representable values preserved, 66 int→int wraps
modular, int→float and float→float round to nearest / inf, 84 in-range float→int truncations; bool casts.
Promotion: promote_types over all 196 pairs equals the documented lattice (uint64+int64→float64,
int16+float16→float32, int32+float32→float64, float64+complex64→complex128, …), result_type of arrays
agrees, can_cast('safe') equals promote_types(a,b)==b for all pairs, 'no'/'equiv'/'same_kind'/'unsafe'.
finfo for float16/32/64 (eps, max, min, tiny, smallest_normal, smallest_subnormal, epsneg, precision,
resolution, nmant, nexp, minexp, maxexp, bits) vs IEEE 754; longdouble = x86 80-bit (nmant 63, eps 2^−63,
2^−16382, 2^−16445, precision 18) with real 64-bit mantissa arithmetic; iinfo for all 8 int types.
nextafter at 0/±0/1/max/inf/subnormal boundary, float32/float16; spacing at 1, 0, subnormals, powers of
two, sign; frexp = math.frexp incl. subnormals with exact ldexp round trip, ldexp at 2^−1074/2^−1075
(ties to even)/overflow, float32; modf signs incl. −0.0, inf, nan, ints → float64; divmod(x, 1) vs modf.
Reductions: true_divide of ints → float64 (no integer loops), divide with int out → TypeError
(unsafe casting works), sum/mean/prod dtypes for every int width, bool sums, mean(float32) stays float32,
add.reduce upcasts int8 to int64 and dtype= wraps, float32 pairwise vs accumulate, sum(dtype=float64).
ufunc methods: reduce (axis, None, tuple, keepdims, identity, no-identity ValueError, initial, where),
accumulate, reduceat against a plain-Python implementation of the documented rules incl. decreasing
indices and the `[::2]` example, IndexError for ≥ len and negative, axis=1, dtype=; outer shapes; add.at
vs fancy +=; negative.at; overlapping out= views computed as if unaliased; where= with/without out;
out= shape/type errors; out tuple; dtype= keyword.
Scalars/bool: np.float64 results (float subclass), np.int64 not an int subclass, 0-d results are scalars,
np.float64(1)/0 = inf; np.bool_ + is logical or, − and unary − TypeError, /, **, ~; heaviside table incl.
nan/±inf/x2 at zero/float dtypes; positive/negative/abs dtype rules; rint/floor on float16.

## Not checked, and why

* SIMD paths for architectures other than x86-64 AVX-512 (NEON, AVX2-only, non-SVML builds): only this
  host is available; the 1.x findings above apply to AVX-512 machines specifically.
* float64 → float32 double rounding of the mpmath truth when computing "steps" (probability ~2^−29 per
  point; ignored).
* Object-dtype and datetime/timedelta arithmetic, `np.unwrap` (n11), masked arrays, `np.emath`,
  `np.float128` beyond finfo/eps arithmetic, and `np.errstate` inside threads.
* `np.fix` is deprecated on numpy main (2.5) but present and correct on all installed builds.
