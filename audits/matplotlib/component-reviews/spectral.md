# Component: spectral analysis (`mlab.psd` / `csd` / `cohere` / `specgram` / `*_spectrum`, the detrend and window helpers, and the `Axes` wrappers)

Harness `verify/m2_spectral.py`, notes `verify/m2_spectral.notes.md`. Executed on four builds: the **main overlay**
(matplotlib 3.11.2 with `mlab.py`, `axes/_axes.py`, `cbook.py`, `colors.py`, `colorizer.py`, `contour.py` and
`stackplot.py` from `main` @ 44f2e0033a copied in; the banner reads 3.11.2, and the overlay shows in the output as
`Axes.psd has Funits: True`, a 3.12 parameter), **3.11.2**, **3.7.1** (no SciPy) and **3.5.2** (no SciPy). A full
build of `main` is blocked because its SheenBidi download is refused here. On 44f2e00 the overlaid `mlab.py` and
`axes/_axes.py` are byte-identical to the source tree; all file:line citations are to that commit. Runtime 2–16 s
per build.

Cohort: spectrograms / PSD / spectral methods are named in 3 papers (lower bound from the survey cache). Prior
reports for every finding: search pending (`../prior-reports.md`); MPL36 has a known fix PR (below).

## Truths

- **Welch reference** written in plain numpy from the psd/csd docstrings and Bendat & Piersol, with an explicit
  O(n²) DFT matrix (np.fft not used): zero-pad to NFFT if shorter; segments advancing by NFFT − noverlap; detrend,
  then window; DFT at pad_to points; average conj(X)·Y; scale by 1/(Fs·Σw²) or 1/(Σw)²; one-sided output keeps
  bins 0..pad_to//2 and doubles every bin except DC and, **when pad_to is even**, the Nyquist bin.
- **Parseval**: the variance in `fractions.Fraction` on integer data.
- **Fraction least squares** for `detrend_linear`.
- **Closed forms**: A·cos at a bin centre, constant input, white noise at 2σ²/Fs.
- **SciPy** `scipy.signal.welch / csd / coherence / spectrogram` (1.18.1) on the two builds that have it; those
  lines carry `(scipy)`.

## Counts

| build | ok | FAIL |
|---|---|---|
| main overlay (3.11.2 + main mlab/_axes) | 258 | 24 |
| 3.11.2 | 258 | 24 |
| 3.7.1 (no scipy) | 234 | 20 |
| 3.5.2 (no scipy) | 233 | 21 |

The FAIL sets on main and 3.11.2 are identical. 3.7.1 lacks only the four `(scipy)` lines; 3.5.2 adds MPL36. The
24 lines on main: MPL3 14, MPL13 3, MPL17 1, MPL20 1, MPL22 1, MPL21 1, MPL23 2, MPL16 1. (Notes labels F1–F9 are
given in each heading.)

## Findings

### MPL3 (F1) — one-sided doubling keyed to NFFT parity instead of pad_to parity (bug; all builds)

**Measured.** Only the last returned bin is wrong, by exactly a factor of 2.

- **NFFT odd, pad_to even** (99/128, 63/64, 129/256): the last bin is the Nyquist bin and is doubled when it should
  not be.
- **NFFT even, pad_to odd** (100/101, 64/65, 64/127): the last bin is an ordinary positive frequency below Fs/2
  and is left undoubled.

| check | measured |
|---|---|
| psd NFFT=99 pad_to=128 | maxabsdiff 3.530e+00 (scale 2.404e+01) |
| psd NFFT=100 pad_to=101 | maxabsdiff 3.478e+00 (scale 2.058e+01) |
| psd NFFT=63 pad_to=64 Fs=10 scale_by_freq=False | maxabsdiff 1.214e-01 (scale 6.313e-01) |
| csd NFFT=99 pad_to=128 | maxabsdiff 7.830e-02 (scale 1.319e+01) |
| specgram NFFT=129 noverlap=0 pad_to=256 detrend='linear' scale_by_freq=False | maxabsdiff 2.412e-02 (scale 3.891e-01) |
| Axes.psd NFFT=99 pad_to=128 scale_by_freq=False | maxabsdiff 1.081e-01 (scale 7.358e-01) |
| Parseval one-sided NFFT=63 pad_to=64 | sum·df 32.3148870512 vs var 31.9627110103 (ratio 1.011018) |
| Parseval one-sided NFFT=63 pad_to=128 | sum·df 29.0800309542 vs var 29.074829932 (ratio 1.000179) |
| Parseval one-sided NFFT=64 pad_to=65 | sum·df 24.6139069313 vs var 24.6403808594 (ratio 0.998926) |
| Parseval one-sided NFFT=64 pad_to=127 | sum·df 24.5565579474 vs var 24.5661621094 (ratio 0.999609) |
| (scipy) psd / csd NFFT=99 pad_to=128 | maxabsdiff 3.530e+00 / 7.830e-02 |
| (scipy) psd / csd NFFT=100 pad_to=101 | maxabsdiff 3.478e+00 / 1.080e-01 |

When NFFT and pad_to have the same parity everything matches the reference to about 1e-13 (64/64, 64/128, 63/63,
63/101, 100/128, 99/101), and Parseval is exact.

**Cause.** `mlab.py:357–363` in `_spectral_helper`:

```python
if not NFFT % 2:
    slc = slice(1, -1, None)
else:
    slc = slice(1, None, None)
result[slc] *= scaling_factor
```

The comment says "if we have an even number of frequencies, don't scale NFFT/2", but the bins come from
`np.fft.fft(result, n=pad_to, ...)` and `numFreqs` (lines 304–308) is correctly computed from `pad_to`. Only the
doubling slice uses `NFFT`; the same function uses `pad_to % 2` for the frequency-sign fix at line 383.

**Documentation.** The psd density "allows for integration over the returned frequency values" (`scale_by_freq`,
`mlab.py:472–476`); *pad_to* "can be different from *NFFT*".

**SciPy** with the same nfft disagrees in exactly that bin (SciPy keys the doubling to nfft).

**Scope.** psd, csd, specgram (mode='psd') and `Axes.psd`/`csd`/`specgram`. Not `cohere`, where the factor cancels
in |Pxy|²/(Pxx·Pyy) (checked ok at NFFT=99, pad_to=128). Typical trigger: an odd NFFT with a power-of-two pad_to.
3.5.2, 3.7.1, 3.11.2 and main.

### MPL13 (F2) — `detrend_linear` fits a conjugated slope to complex data (bug; all builds)

**Measured.** For the exact line (1+2i) + (0.5−3i)·n, n = 0..11, the residual should be 0; matplotlib's maximum
|residual| is 3.300e+01. Against the least-squares complex line on general complex data: maxabsdiff 7.009e-01
(scale 1.187e+00). `psd` of complex input with `detrend='linear'`: maxabsdiff 3.159e-01 (scale 2.319e+00), up to
14 % of the peak. Real input is unaffected.

**Cause.** `mlab.py:207–208`: `C = np.cov(x, y, bias=1)`, `b = C[0, 1]/C[0, 0]`. `np.cov` conjugates its second
variable, so the fitted slope is conj(b); for the exact line the residual is (b − conj b)(n − n̄) = −6i(n − 5.5),
maximum magnitude 33.

**Documentation.** `detrend_linear`: "Return *x* minus best fit line", y a "0-D or 1-D array or sequence" (complex
not excluded); psd/csd/specgram document complex input and offer `detrend='linear'`.

### MPL16 (F8) — `Axes.specgram` image rows are offset from their frequencies by up to half a bin (bug, display; all builds)

**Setup.** NFFT=128, Fs=50, Fc=7: 65 rows, df = 0.390625; image y-extent [7.0, 32.0] = [freqs[0], freqs[-1]].

**Measured.** Pixel row centres run from 7.19231 to 31.8077; row k is centred at freqs[k] + df·(n−1−2k)/(2n).
Maximum offset 1.923e-01 (about half a bin) at both ends; the image is stretched by n/(n−1). Along x the column
centres equal the returned segment midpoints t exactly (checked ok).

**Cause.** `axes/_axes.py:8775` pads the time extent by half a column (`pad_xextent = (NFFT-noverlap) / Fs / 2`);
`axes/_axes.py:8779` (`extent = xmin, xmax, freqs[0], freqs[-1]`) applies no half-bin padding in frequency.

**Documentation.** `freqs` are "The frequencies corresponding to the rows in *spectrum*"; the x extent is
documented from "the left border of the first bin" to "the right border of the last bin"; nothing is said about y.

**Verdict.** A spectral line at freqs[k] is drawn in a pixel row centred up to df/2 away. The returned arrays are
correct.

### MPL17 (F3) — `detrend_linear` of a single value returns NaN (bug, edge case; all builds)

`detrend_linear([5.0])` returns `[nan]` with a RuntimeWarning (same code as MPL13: `C[0,0] = 0`, `b = 0/0`). A
least-squares line fits one point exactly, so the residual should be 0. The 0-D case is short-circuited to 0
(`mlab.py:201–203`, checked ok); the 1-element 1-D case is not. Reaches the spectra only through NFFT=1 with
`detrend='linear'`.

### MPL20 (F4) — `scale_by_freq=False` changes the window normalisation as well as "not dividing by Fs" (documentation gap; all builds)

**Measured.** Hann window, NFFT=128, Fs=10: Pxx(False)/Pxx(True) = 0.11811, not Fs = 10; this equals
Fs·Σw²/(Σw)².

**Code.** `mlab.py:370–375`: `result /= Fs; result /= (window**2).sum()` when True, otherwise
`result /= window.sum()**2`. The False branch is the power spectrum (SciPy `scaling='spectrum'`), checked ok against
the definition, SciPy and the tone closed form (peak = A²/2).

**Documentation.** `mlab.py:472–476`: "Whether the resulting density values should be divided by the sampling
frequency, which gives density in units of 1/Hz". The change of window normalisation is not mentioned; with a
boxcar window the two differ only by Fs/NFFT (checked ok).

### MPL21 (F6) — specgram detrends in every mode; its Notes say detrend only applies to mode='psd' (documentation gap; all builds)

**Measured.** Signal with a +40 offset, mode='magnitude', detrend='mean': first segment's DC bin 0.0392532 (the
detrended value; without detrending 39.9387); FAIL maxabsdiff 4.011e+01 (scale 4.024e+01) against "no detrend".

**Code.** `mlab.py:323`: `result = detrend(result, detrend_func, axis=0)` runs before the mode branch.
`scale_by_freq` is forced off for non-psd modes (lines 291–292), as documented (checked ok).

**Documentation.** `mlab.py:714` and `axes/_axes.py:8731`: "*detrend* and *scale_by_freq* only apply when *mode* is
set to 'psd'". The single-spectrum functions pass `detrend_none` themselves and are unaffected.

### MPL22 (F5) — `mlab.csd` documents Pxy as "real valued" (documentation gap; all builds)

Returned dtype complex128, max |imag| 5.134e+00. `csd` returns the complex mean of conj(X)·Y (`mlab.py:583–596`),
correct against the reference and SciPy. The docstring (`mlab.py:568–569`) says "(real valued)"; `Axes.csd`
correctly says "(complex valued)" (checked ok).

### MPL23 (F7) — `Axes.psd` / `Axes.csd` with `return_line=True` return a list, not a `Line2D` (documentation gap / API inconsistency; all builds)

The third return value is a `list` holding one Line2D (2 FAIL lines). `axes/_axes.py:8218`
(`line = self.plot(freqs, 10 * np.log10(pxx), **kwargs)`) and 8321 for csd; `magnitude_spectrum`,
`angle_spectrum` and `phase_spectrum` unpack (`line, = self.plot(...)` / `lines[0]`). Documented at
`axes/_axes.py:8167` and `8283` as "line : `~matplotlib.lines.Line2D`". Not numeric: the line's ydata is the
correct 10·log10(Pxx).

### MPL36 (F9) — 3.5.2 only: power normalisation used |window| (old-release only; fixed in 3.7.0)

**Measured.** A window with negative lobes, `scale_by_freq=False`: maxabsdiff 4.505e-01 (scale 1.415e+00). The
density variant passes on 3.5.2 because (|w|)² = w².

**Cause.** 3.5.2's `_spectral_helper` divides by `np.abs(window).sum()**2` and uses `np.abs(window).sum()` for the
magnitude/complex scaling; 3.7.1 and later use `window.sum()` (main: `mlab.py:343`, `348`, `375`). Fixed by PR
#25122 "FIX: scaling factor for window with negative value" (issue #24821; listed in
`doc/release/prev_whats_new/github_stats_3.7.0.rst`). Affects 3.5.2 (and 3.6.x per the notes); passes on 3.7.1,
3.11.2 and main.

## What held up (all four builds unless noted)

- **Windows.** `window_hanning` equals the symmetric Hann 0.5 − 0.5·cos(2πn/(M−1)) for M = 2, 7, 8, 256;
  `window_none` returns its input.
- **Detrend helpers.** `detrend_mean` (Fraction, 2-D with axis 0/1/None, out-of-range axis raises);
  `detrend_linear` on integer input, exact lines, constants, two points, 0-D, and 2-D raising ValueError;
  `detrend_none`; the `detrend(key=...)` mapping including callables and per-axis 2-D use.
- **psd against the explicit-DFT Welch reference, to about 1e-13 relative**: defaults (maxabsdiff 1.830e-13, scale
  3.778e+01), odd NFFT=255, noverlap 64 and the maximal 99, pad_to with matching parity (100/128, 99/101),
  `scale_by_freq` True/False/None, detrend 'mean'/'linear'/function/callable, window_none, a triangle array, a
  window with negative values (3.7.1+), 'twosided' (even and odd NFFT) and 'default', integer input, float32 input
  (float64 with Hann; complex64 with window_none on numpy 2.x, agreeing to 1e-5), len(x) < NFFT zero-padded,
  complex input (two-sided by default, forced one-sided, ascending −Fs/2..Fs/2−df). Frequency vectors exact.
- **Edge cases.** Empty input gives zeros of length NFFT//2+1; a single value with NFFT=1 gives 4.5 = 9/Fs;
  constant input with detrend='mean' gives exactly 0; constant input, no detrend, boxcar puts c²·NFFT/Fs in DC; a
  1e8 offset with detrend='mean' agrees to 1e-6; noverlap = NFFT, a window-length mismatch and an invalid `sides`
  raise ValueError.
- **Parseval.** Exact (ratio 1.000000) whenever NFFT and pad_to share parity (64/64, 64/128, 63/63, 63/101);
  two-sided real with pad_to=96; complex two-sided sum·df = mean|x|².
- **Closed forms.** A tone at a bin centre gives a one-sided psd peak (boxcar, scale_by_freq=False) of exactly
  A²/2 (4.5) with nothing elsewhere (rest max 1.032e-30); `magnitude_spectrum` A/2 (1.5 for A = 3.0) one- and
  two-sided; `complex_spectrum` (A/2)e^{iφ}; `angle_spectrum` φ.
- **White noise** (σ = 1.5, Fs = 100, 2¹⁸ samples): one-sided level 0.0449107 against 2σ²/Fs = 0.045 (ratio
  0.99802); two-sided 0.0224532 against 0.0225; integral of the PSD 2.24532 against sample variance 2.24594; the
  scale_by_freq=False level 0.026418 against 2σ²Σw²/(Σw)² = 0.0264706.
- **csd** against conj(X)·Y for defaults, matching-parity noverlap/pad_to/Fs, linear detrend with
  scale_by_freq=False, two-sided, both inputs shorter than NFFT, complex inputs; `Axes.csd` returns complex Pxy.
- **cohere** equals |Pxy|²/(Pxx·Pyy) including NFFT=99/pad_to=128; within [0, 1]; exactly 1 for y = −2.5x and
  complex y = (1+2i)x; independent noise with 64 segments gives mean coherence 0.0147 (about 1/K = 0.0156).
- **specgram** columns equal the per-segment reference in psd mode (defaults and other settings, two-sided);
  magnitude, complex and angle (mod 2π) modes; phase = angle + 2πk with |Δ| ≤ π; scale_by_freq ignored outside psd;
  t = (start + NFFT/2)/Fs; len(x) < NFFT gives one zero-padded segment with the documented warning; complex input.
- **complex / magnitude / angle / phase spectrum** match the reference with default Hann, pad_to 512 and 400, Fs,
  two-sided window_none and complex input.
- **SciPy** (main, 3.11.2): `welch`, `csd`, `coherence` and `spectrogram` in all five modes, and the spectrogram t
  vector, agree whenever NFFT and pad_to parities match.
- **Axes wrappers.** psd returns the linear density, freqs and line xdata include Fc, ydata = 10·log10(Pxx),
  `return_line` None/False give 2-tuples, complex input with Fc; csd ydata = 10·log10|Pxy|; magnitude_spectrum
  scale None/'linear'/'dB'; angle_spectrum, phase_spectrum, cohere; specgram returned arrays, image arrays
  (flipud dB / linear per mode), freqs + Fc, column centres = t; ValueError for mode='complex' and for angle with dB.

## Not checked / observations

- **Magnitude normalisation is undocumented.** `magnitude_spectrum` and specgram mode='magnitude' return |DFT|/Σw
  without one-sided doubling (a tone of amplitude A reads A/2), as SciPy's `scaling='spectrum'` magnitude; no
  docstring states it. Observation, not a FAIL.
- **Undocumented behaviour printed as info:** one NaN makes every bin NaN (65/65); the mask of masked arrays is
  ignored; pad_to < NFFT silently truncates the windowed segment (51 bins at pad_to=100, NFFT=128); `cohere`
  raises ValueError when len(x) < 2·NFFT; `specgram(x, NFFT=64)` raises "noverlap must be less than NFFT" because
  of the default noverlap=128; `csd` with len(x)=1000, len(y)=150, NFFT=200 silently pairs y's single zero-padded
  segment with all five x segments, while 900 against 1000 raises a broadcast ValueError.
- **Not checked:** `GaussianKDE` (box/violin group), the 32-bit `_stride_windows` path, `Funits` labels, rendered
  pixels, statistical bias of Welch estimates beyond the white-noise level.

## Notes against outputs

Two numbers in `m2_spectral.notes.md` do not appear in any of the four `.out` files, and this review uses the
`.out` values: F6 gives the magnitude DC bin as 0.0405 (39.92 undetrended), the outputs print 0.0392532 (39.9387)
on every build; the held-up list gives the independent-noise coherence as 0.0147–0.0191, the outputs print 0.0147
on every build.
