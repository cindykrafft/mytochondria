# n10_fft — notes

Harness: `audits/numpy/verify/n10_fft.py`. Outputs: `n10_fft.out` (numpy 2.4.6), `n10_fft.v1.23.5.out`,
`n10_fft.v1.24.4.out`, `n10_fft.v1.26.4.out`. Runtime about 40 s per build (dominated by the O(n^2) mpmath DFTs
at n = 1000 / 1009 / 1024).
Truths: the DFT exactly as the `numpy.fft` module docstring defines it (`A_k = sum a_m exp(-2 pi i m k / n)`,
inverse with `1/n` and the opposite sign). It is evaluated in mpmath at 30 digits as an O(n^2) sum, and at
n = 2**15 as an independent radix-2 mpmath FFT. That radix-2 FFT is cross-checked against the O(n^2) sum at
n = 1024 (agreement 1.8e-31). The Hermitian-extension references for irfft / hfft / ihfft and the separable
N-D references are built on it. `fractions.Fraction` is the truth for fftfreq / rfftfreq and the Parseval sums,
Python list rotation for fftshift / ifftshift, and closed forms for the pure cosine / sine / constant /
complex exponential, the shift theorem and repeated axes. Inputs are small random integers, exactly
representable in every dtype used. No scipy anywhere.

## Counts

| build | ok | FAIL |
|---|---|---|
| numpy 2.4.6 | 384 | 9 |
| numpy 1.26.4 | 351 | 1 |
| numpy 1.24.4 | 351 | 1 |
| numpy 1.23.5 | 351 | 1 |

The 1.x builds run fewer checks because the 2.0-only features (`out=`, `s=-1`, native float32 / longdouble)
are replaced there by one version-aware check each. No FAIL is a numerical error. The worst float64 error
measured anywhere is 7.6e-16 (normwise relative, n = 1009 on 1.26.4), more than three orders of magnitude
below the 1e-12 FAIL threshold.

## FAIL lines

### 1. `hfft(a, out=out)` ignores `out` (2.4.6 only; fixed on main)

Measured: `o = np.full(6, -7.0); r = np.fft.hfft(a, out=o)` with `len(a) = 4` returns a new array `r`
(`r is o` is False) and leaves `o` untouched (still all -7). The returned `r` is correct: 1e-16 against the
mpmath Hermitian-extended forward transform. Library: `numpy/fft/_pocketfft.py` `hfft` in 2.4.6 ends with
`output = irfft(conjugate(a), n, axis, norm=new_norm, out=None)`, so it accepts `out` and then drops it.
Documentation: the 2.4.6 `hfft` docstring says "out : ndarray, optional  If provided, the result will be placed
in this array", and the 2.0.0 release note says "all FFT routines have gained an `out` argument". The sibling
`ihfft` does pass `out` through (`out = rfft(a, n, axis, norm=new_norm, out=out)`; checked ok). Verdict:
**bug** in the released 2.x line. numpy main @ 55511445dc already has
`irfft(conjugate(a), n, axis, norm=new_norm, out=out)` and a regression test
(`numpy/fft/tests/test_pocketfft.py::test_hfft_out`). The 1.x builds have no `out=` (checked: TypeError).

### 2. The `hfft` out-contents line (sub-check of 1; 2.4.6 only)

`out` is compared with the mpmath reference and differs by 1.2 relative, because it was never written. This is
the same bug as FAIL 1, not a separate finding.

### 3. Module docstring "Type Promotion" is stale (2.4.6; also on main)

Measured on 2.4.6: `fft(float32)` returns complex64, `rfft(float32)` complex64, `irfft(complex64)` float32,
`fft(longdouble)` clongdouble (all checked). The error of float32 input at n = 1024 is 3.7e-8, which is
single-precision accuracy. Documentation: `numpy/fft/__init__.py` (installed 2.4.6 and main @ 55511445dc,
line 127) still says "`numpy.fft` promotes ``float32`` and ``complex64`` arrays to ``float64`` and
``complex128`` arrays respectively. For an FFT implementation that does not promote input arrays, see
`scipy.fftpack`." The 2.0.0 release note (gh-25536) says the routines "now do their calculations natively in
float, double, or long double precision ... The data type of the output array will now be adjusted
accordingly." Verdict: **documentation gap**, a stale paragraph from 1.x, where it is true (1.x checks: float32
becomes complex128 and is computed in double, 1.9e-16). Users who rely on it get single-precision results
silently in 2.x.

### 4–7. `rfft` of complex input: docstring says "silently discarded"

Documentation: the `rfft` docstring (2.4.6 and main, `_pocketfft.py` line 399) says "If the input `a` contains
an imaginary part, it is silently discarded." Measured with `rfft([1+2j, 3-1j, 2, 5+4j])`:

- **2.4.6**: raises `TypeError: ufunc 'rfft_n_even' not supported for the input types, and the inputs could not
  be safely coerced`. The same happens for `ihfft` (which calls rfft) and `rfftn` of a complex array. Library:
  `rfft` does `a = asarray(a)` and then `_raw_fft(a, n, axis, True, True, norm, out=out)`, which calls the
  `pfu.rfft_n_even` / `rfft_n_odd` gufunc with its default `same_kind` casting, so complex to real is refused.
  All four FAIL lines fire: the value check, the "silently" check, ihfft, and rfftn.
- **1.23.5 / 1.24.4 / 1.26.4**: the imaginary part is discarded (the result equals rfft of the real part, ok),
  but a `ComplexWarning: Casting complex values to real discards the imaginary part` is emitted from
  `_raw_fft`'s `r = pfi.execute(a, is_real, is_forward, fct)`, whose C side force-casts to double. Only the
  "SILENTLY" line fails.

Verdict: **documentation gap** in every build. In 1.x the discard is not silent. In 2.x it does not happen at
all: the function now refuses complex input. That is arguably better behaviour, but it is an undocumented
behaviour change, not mentioned in the 2.0.0 release notes, and the docstring sentence is still present on main.

### 8. The documented idiom `irfftn(rfftn(a), a.shape)` emits a DeprecationWarning (2.4.6; also on main)

Measured: the round trip is exact to 1e-16 (ok), but the call emits `DeprecationWarning: \`axes\` should not be
\`None\` if \`s\` is not \`None\``. Library: `_cook_nd_args` in `_pocketfft.py` warns whenever `s` is given
without `axes` (the gh-25495 deprecation). Documentation: the `irfftn` Returns / Notes text (2.4.6 and main,
line ~1481) says "In other words, ``irfftn(rfftn(a), a.shape) == a`` to within numerical accuracy. (The
``a.shape`` is necessary like ``len(a)`` is for `irfft`...)", so it recommends exactly the deprecated call.
The `irfft2` example `irfft2(A, s=a.shape)` does not warn, because irfft2 has default axes (-2, -1); checked
ok. Verdict: **documentation gap**. The recommended idiom should read `irfftn(rfftn(a), a.shape,
axes=range(a.ndim))`. The 1.x builds do not warn (the deprecation is 2.0), so there is no FAIL there.

### Summary

The nine 2.4.6 FAILs (hfft out x2, Type Promotion x1, rfft-complex x4, irfftn idiom x1) come down to four distinct findings: one bug, fixed on main, and three documentation
gaps, all still present on main.

## Harness corrections made while completing the partial harness

- The partial compared `hfft([1, 2, 3, 4], 8)` against an invented "docstring example". The actual examples are
  now tested: `hfft(signal[:4]) = hfft(signal, 6) = [15, -4, 0, -1, 0, -4]` and the 2-D
  `hfft([[1, 1j], [-1j, 2]]) = [[1, 1], [2, -2]]`. All pass on every build.
- The pure-cosine check built its input with `np.cos` and zeroed values below 1e-15. The residues at the
  zeros reach 8.8e-15 for large j, so the input was not the intended exact [1, 0, -1, 0, ...]. The input is
  now written out exactly. The fft then gives exactly 32 at bins 16 / 48 and exactly 0 elsewhere on every build.
- The NaN check expected every real part to be NaN. For `[1, nan, 2, 3]` pocketfft returns
  `[nan+0j, -1+nanj, nan+0j, -1+nanj]`, because the trivial twiddles ±1 and ±i are applied as adds and swaps
  without multiplication, so `nan*0` never occurs. NaN handling is undocumented. The check is now "every bin
  has a NaN component" (np.isnan on complex), and it holds on every build.
- `irfftn(H5, R5.shape)` now passes `axes` explicitly, so the separate check for the documented idiom is the
  only place that deprecated call is made.

## What held up (every build unless noted)

- fft / ifft against the exact DFT at primes 7, 13, 97, 1009 and composites 1000, 1024, 2**15. Max normwise
  relative error 6.5e-17 to 7.6e-16, all below eps·log2(n). Real input at 13, 1000 and 2**15, and rfft = the
  first n//2+1 bins.
- Norm modes: None / "backward" / "ortho" / "forward" give the documented scaling in both directions for fft,
  ifft, rfft, irfft, hfft (forward scaling of the Hermitian-extended time signal) and ihfft, at n = 12 and 13.
  The same holds for fftn / ifftn / rfftn / irfftn and for fft2 / ifft2 / rfft2 / irfft2 (the latter added
  here). Round trips hold under every norm. Invalid norm gives ValueError. norm=None is identical to the default.
- Parseval under each norm for fft and ifft (Fraction truth), and for rfft with ortho (doubling of the
  non-DC / non-Nyquist bins), for even and odd n.
- n crop / zero-pad for all six 1-D functions. Output length n//2+1 for rfft / ihfft. irfft / hfft default
  n = 2*(m-1). Odd n must be given. Crop and pad of the half-spectrum. irfft / hfft of a length-1 input give
  ValueError (default n = 0), while n = 1 works.
- Hermitian handling: the imaginary parts of the DC and (even n) Nyquist bins are ignored by irfft / hfft.
  For odd n the last bin's imaginary part contributes. Output is real float64. irfft(rfft(x), len(x)) = x;
  for odd length without n the output has length n-1, as documented. ihfft(hfft(a, 2m-2 / 2m-1)) = a.
  The fft of real input is Hermitian (asymmetry below 1e-14), with DC / Nyquist exactly real.
- Closed forms: exact cosine at k = n/4 (exactly two bins), 2.5 cos / sin at bin 5, constant, complex
  exponential, linearity, shift theorem, and repeated axes in fftn (n·a[-k] and n²·a).
- fftfreq / rfftfreq layout against Fraction for n in {1, 2, 3, 8, 9, 16, 1000, 1009} and four d values.
  Nyquist is negative in fftfreq and positive in rfftfreq. Non-integer n gives ValueError. 2.x `device="cpu"`
  works. fftshift / ifftshift equal list rotation for odd and even n, int / tuple / None axes; the round trips
  and the quadrant swap hold.
- Axis semantics: default axis=-1 on 2-D input, axis 0 / -2 / -3 on 4-D, and IndexError for an out-of-range
  axis. N-D = separable 1-D along each axis. The s / axes pairing (s[i] ↔ axes[i]); s without axes uses the last
  len(s) axes. rfftn / irfftn put the real axis at axes[-1]. Shape / axes length mismatches give ValueError.
- 2.0 changes: s without axes and None in s give DeprecationWarning on 2.4.6 and are silent on 1.x. s = -1
  means the whole axis on 2.x (for irfftn's last axis this gives n = m, not 2(m-1)) and ValueError on 1.x.
- `out=` (2.x): returned identity, in-place fft / ifft, wrong shape / ndim gives ValueError, a real out for
  complex output gives TypeError, complex64 out accepted (same_kind), rfft / irfft / ihfft / fftn / rfftn /
  irfftn out. fftn out with a non-trivial s on a non-last axis gives ValueError (documented). hfft is the
  exception (FAIL 1).
- dtypes: on 2.x, float32 / complex64 stay single precision (3.7e-8 at n = 1024, 4.0e-8 at the prime
  n = 1009); float16 is promoted to complex64; longdouble becomes clongdouble with error 1.1e-19 (below
  float64's 2.0e-16). On 1.x, float32 and longdouble are computed in double and come out complex128. int /
  bool / int8 / uint8 / list inputs are promoted to complex128 and give the exact DFT.
- Edge cases: empty input gives ValueError; n = 0 or negative gives ValueError; 0-d input gives IndexError;
  a single element and two elements are exact; all-zero input gives exactly 0; an empty non-transformed
  axis is fine.
- Non-contiguous inputs (strided, reversed, sliced, transposed) and Fortran-ordered inputs give the same
  results as contiguous ones; the input is not modified.
- API surface: `numpy.fft.__all__` is exactly the 18 routines. On 1.x `numpy.fft.helper` is public; on 2.4.6 `numpy.fft.helper` no
  longer imports at all (ModuleNotFoundError) and the code lives in private `_helper` / `_pocketfft`. `fftpack` / `fftpack_lite` are absent.

## What could not be checked

- Accuracy at lengths much larger than 2**15, and adversarial inputs (for example large dynamic range): the
  O(n^2) mpmath reference and the time budget limit these. Integer inputs measure rounding in the
  transform, not input representation.
- longdouble on platforms where it equals double, or is double-double: only x86-64 80-bit extended precision
  was available.
- The docs give no error bound for the FFT. The 1e-12 threshold is the audit's, and every measured error sits
  near eps·log2(n) or below.
- Informational only, with no documented expectation: prime-length runtime (Bluestein) is about 5–7x the
  nearby composite length; `fftfreq(0)` raises ZeroDivisionError rather than ValueError; irfft into a complex
  `out` is accepted on 2.x; object-dtype input to fft works on 1.x and raises TypeError on 2.x.
