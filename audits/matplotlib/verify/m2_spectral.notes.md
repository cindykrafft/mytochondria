# m2_spectral — notes

Harness: `audits/matplotlib/verify/m2_spectral.py`. Outputs:

- `m2_spectral.out`: the "main overlay" build. This is matplotlib 3.11.2 with `mlab.py`, `axes/_axes.py` (and cbook / colors / colorizer / contour / stackplot) from main @ 44f2e0033a copied in. A full build of main was impossible here because its SheenBidi download is blocked. The banner therefore reads 3.11.2. The overlay shows up in the output as `Axes.psd has Funits: True`, a 3.12 parameter.
- `m2_spectral.v3.11.2.out`
- `m2_spectral.v3.7.1.out` (no SciPy)
- `m2_spectral.v3.5.2.out` (no SciPy)

Runtime is 2–16 s per build.

On 44f2e00, `mlab.py` and `axes/_axes.py` in the overlay are byte-identical to `$M/src`. All file:line citations below refer to that commit.

Truths:

- **Welch reference.** Welch's averaged periodogram, written in plain numpy from the psd/csd docstrings and Bendat & Piersol, with an explicit O(n²) DFT matrix (np.fft is not used). The steps are:
  1. Zero-pad x to NFFT if it is shorter.
  2. Take segments advancing by NFFT − noverlap.
  3. Detrend each segment, then multiply by the window.
  4. Take the DFT at pad_to points and average conj(X)·Y over the segments.
  5. Scale by 1/(Fs·Σw²) or 1/(Σw)².
  6. One-sided output keeps bins 0..pad_to//2 and doubles every bin except DC and, **when pad_to is even**, the Nyquist bin.
- **Parseval.** The variance is computed in `fractions.Fraction` on integer data.
- **Fraction least squares** for `detrend_linear`.
- **Closed forms:** A·cos at a bin centre, constant input, and white noise with level 2σ²/Fs.
- **SciPy.** `scipy.signal.welch / csd / coherence / spectrogram` (SciPy 1.18.1), on the two builds that have it. The labels carry `(scipy)`.

## Counts

| build | ok | FAIL |
|---|---|---|
| main overlay (3.11.2 + main mlab/_axes) | 258 | 24 |
| 3.11.2 | 258 | 24 |
| 3.7.1 (no scipy) | 234 | 20 |
| 3.5.2 (no scipy) | 233 | 21 |

The 24 FAIL lines on main come down to eight distinct findings:

- three wrong-number bugs (F1, F2, F3)
- one display bug (F8)
- four documentation gaps (F4–F7)

A ninth finding, F9, is a bug present only on 3.5.2 and fixed in 3.7.0.

The FAIL sets on main and 3.11.2 are identical. 3.7.1 lacks only the four `(scipy)` lines, and 3.5.2 adds F9.

## FAIL lines

### F1. One-sided doubling keyed to NFFT parity instead of pad_to parity (bug; all builds)

These FAIL lines all come from this one cause:

- `psd NFFT=99 pad_to=128`
- `psd NFFT=100 pad_to=101`
- `psd NFFT=63 pad_to=64 Fs=10 scale_by_freq=False`
- the four `Parseval one-sided` lines: NFFT=64 with pad_to=65 and 127; NFFT=63 with pad_to=64 and 128
- `csd NFFT=99 pad_to=128`
- `specgram NFFT=129 noverlap=0 pad_to=256 ...`
- `Axes.psd NFFT=99 pad_to=128 ...`
- on the SciPy builds, `(scipy) psd/csd NFFT=99 pad_to=128` and `(scipy) psd/csd NFFT=100 pad_to=101`

That is 14 lines on main and 3.11.2, and 10 on 3.7.1 and 3.5.2.

**Measured.** In every case only the last returned bin is wrong, by exactly a factor of 2:

- **NFFT odd, pad_to even** (e.g. 99/128, 63/64, 129/256): the last bin is the Nyquist bin (f = Fs/2), and it is doubled when it should not be.
  - Parseval: sum·df / variance = 1.011 at 63/64 and 1.00018 at 63/128.
- **NFFT even, pad_to odd** (100/101, 64/65, 64/127): the last bin is an ordinary positive frequency below Fs/2, and it is left undoubled.
  - Parseval: ratio 0.99893 at 64/65 and 0.99961 at 64/127.

When NFFT and pad_to have the same parity, everything matches the reference to about 1e-13. That covers 64/64, 64/128, 63/63, 63/101, 100/128 and 99/101.

**What matplotlib does.** `mlab.py:357–363` in `_spectral_helper`:

```python
if not NFFT % 2:
    slc = slice(1, -1, None)
else:
    slc = slice(1, None, None)
result[slc] *= scaling_factor
```

The comment says "if we have an even number of frequencies, don't scale NFFT/2". However, the bins come from `np.fft.fft(result, n=pad_to, ...)`, and the number of frequencies (`numFreqs`, lines 304–308) is correctly computed from `pad_to`. Only the doubling slice uses `NFFT`. The same function also uses `pad_to % 2` for the frequency-sign fix at line 383.

**Documentation.**

- The psd docstring promises a density that "allows for integration over the returned frequency values" (`scale_by_freq`, `mlab.py:472–476`).
- *pad_to* is documented as "The number of points to which the data segment is padded when performing the FFT ... This can be different from *NFFT*".

**SciPy.** `scipy.signal.welch`/`csd` with the same nfft disagree in exactly that bin; SciPy keys the doubling to nfft.

**Verdict.** Bug: a wrong number versus the documented definition.

- It affects psd, csd, specgram (mode='psd') and Axes.psd/csd/specgram.
- It does not affect cohere, where the factor cancels in |Pxy|²/(Pxx·Pyy) (checked ok at NFFT=99, pad_to=128).
- The typical trigger is an odd NFFT with a power-of-two pad_to.
- Present in 3.5.2, 3.7.1, 3.11.2 and main.

### F2. `detrend_linear` fits a conjugated slope to complex data (bug; all builds)

FAIL lines:

- `detrend_linear(complex exact line) = 0`
- `detrend_linear(complex) = x minus least-squares complex line`
- `psd complex input detrend='linear'`

**Measured.** For the exact line (1+2i) + (0.5−3i)·n, n = 0..11, the residual should be 0. Matplotlib returns a residual whose maximum magnitude is 33.0.

**What matplotlib does.** `mlab.py:207–208`:

```python
C = np.cov(x, y, bias=1)
b = C[0, 1]/C[0, 0]
```

`np.cov` conjugates its second variable, so `C[0,1] = Σ(x−x̄)·conj(y−ȳ)/N` and the fitted slope is conj(b). The residual for the exact line is (b − conj b)(n − n̄) = −6i(n − 5.5), whose maximum magnitude is 33, as measured.

**Documentation.**

- `detrend_linear`: "Return *x* minus best fit line", with y a "0-D or 1-D array or sequence". Complex input is not excluded.
- psd/csd/specgram document complex input ("'default' is one-sided for real data and two-sided for complex data") and offer `detrend='linear'`.

**Verdict.** Bug: wrong numbers for complex input. psd of complex input with detrend='linear' is off by up to 14% of the peak (maxabsdiff 0.32 against a scale of 2.3). Real input is unaffected. All builds.

### F3. `detrend_linear` of a single value returns NaN (bug, edge case; all builds)

FAIL line: `detrend_linear(single value) = 0`.

**Measured.** `detrend_linear([5.0])` returns `[nan]`, with a RuntimeWarning.

**What matplotlib does.** Same code as F2: `C[0,0] = 0`, so `b = 0/0`.

**Documentation.** "Return *x* minus best fit line". A least-squares line fits a single point exactly, so the residual is 0.

**Verdict.** Bug, minor. The 0-D case is short-circuited to 0 (`mlab.py:201–203`; checked ok), but the 1-element 1-D case is not. It reaches the spectra only through NFFT=1 with detrend='linear'. All builds.

### F4. `scale_by_freq=False` does more than "not divide by Fs" (documentation gap; all builds)

FAIL line: `scale_by_freq docs: ... Pxx(False) = Fs * Pxx(True)`.

**Measured.** With a Hann window, NFFT=128 and Fs=10, Pxx(False)/Pxx(True) = 0.11811 rather than 10. This equals Fs·Σw²/(Σw)².

**What matplotlib does.**

- `mlab.py:370–375`: `result /= Fs; result /= (window**2).sum()` when True.
- Otherwise: `result /= window.sum()**2` ("preserve power in the segment").

The False branch therefore gives the power spectrum, SciPy's `scaling='spectrum'`, and not an undivided density. This was checked ok against the definition, against SciPy, and against the sinusoid closed form (peak = A²/2).

**Documentation.** `mlab.py:472–476`: "Whether the resulting density values should be divided by the sampling frequency, which gives density in units of 1/Hz". Nothing mentions the change of window normalisation. With a boxcar window the two only differ by Fs/NFFT (checked ok).

**Verdict.** Documentation gap: the numbers follow the standard power-spectrum convention, but the documentation describes something else. All builds.

### F5. `mlab.csd` documents Pxy as "real valued" (documentation gap; all builds)

FAIL line: `mlab.csd docstring 'Pxy ... (real valued)': returned Pxy is real`.

**Measured.** The returned dtype is complex128, with max |imag| = 5.1.

**What matplotlib does.** `csd` returns the complex mean of conj(X)·Y (`mlab.py:583–596`). This is correct, and was checked against the reference and SciPy.

**Documentation.** `mlab.py:568–569`: "The values for the cross spectrum P_xy before scaling (real valued)". The Axes.csd docstring correctly says "(complex valued)" (checked ok).

**Verdict.** Documentation gap. All builds.

### F6. specgram detrends in every mode, but its Notes say detrend only applies to mode='psd' (documentation gap; all builds)

FAIL line: `specgram Notes: 'detrend ... only appl[ies] when mode is psd' -> mode='magnitude', detrend='mean' equals no detrend`.

**Measured.** Signal with a +40 offset, mode='magnitude', detrend='mean'. The first segment's DC bin is 0.0405, which is the detrended value. Without detrending it would be 39.92.

**What matplotlib does.** `mlab.py:323`: `result = detrend(result, detrend_func, axis=0)` runs before the mode branch, for every mode. `scale_by_freq` is forced off for non-psd modes (lines 291–292), as documented (checked ok).

**Documentation.**

- `mlab.py:714`: "*detrend* and *scale_by_freq* only apply when *mode* is set to 'psd'".
- `axes/_axes.py:8731` says the same.

**Verdict.** Documentation gap. Detrending a magnitude spectrogram is reasonable behaviour; the Notes are wrong about detrend. The single-spectrum functions pass `detrend_none` themselves, so they are unaffected. All builds.

### F7. `Axes.psd` / `Axes.csd` with `return_line=True` return a list, not a Line2D (documentation gap; all builds)

FAIL lines:

- `Axes.psd returned 'line : Line2D' is a Line2D`
- `Axes.csd returned 'line : Line2D' is a Line2D`

**Measured.** The third return value is a `list` holding one Line2D.

**What matplotlib does.**

- `axes/_axes.py:8218`: `line = self.plot(freqs, 10 * np.log10(pxx), **kwargs)`
- line 8321 for csd.

`plot` returns a list. By contrast, magnitude_spectrum, angle_spectrum and phase_spectrum unpack it (`line, = self.plot(...)` / `lines[0]`).

**Documentation.** `axes/_axes.py:8167` and `8283`: "line : `~matplotlib.lines.Line2D` The line created by this function."

**Verdict.** Documentation gap or API inconsistency; it is not a numeric error. The ydata of that line is correct (10·log10 of the linear Pxx, checked ok). All builds.

### F8. Axes.specgram image rows are offset from their frequencies by up to half a bin (display bug; all builds)

FAIL line: `Axes.specgram image row centres = freqs (rows of spectrum)`.

**Setup.** NFFT=128, Fs=50, Fc=7, giving 65 rows with df = 0.390625. The image extent along y is [7.0, 32.0] = [freqs[0], freqs[-1]].

**Measured.**

- The pixel row centres run from 7.1923 to 31.8077. Row k is centred at freqs[k] + df·(n−1−2k)/(2n).
- The maximum offset is 0.1923, which is about half a bin, at both ends.
- Along x, the column centres equal the returned segment midpoints t exactly (checked ok).

**What matplotlib does.**

- `axes/_axes.py:8775`: `pad_xextent = (NFFT-noverlap) / Fs / 2` pads the time extent by half a column.
- `axes/_axes.py:8779`: `extent = xmin, xmax, freqs[0], freqs[-1]` applies no half-bin padding to the frequency extent.

**Documentation.** The return value `freqs` is "The frequencies corresponding to the rows in *spectrum*". The x extent is documented as running from "the left border of the first bin" to "the right border of the last bin", but nothing is said about y.

**Verdict.** Bug in what the reader sees: a spectral line at freqs[k] is drawn in a pixel row centred up to df/2 away, and the image is stretched by n/(n−1). The returned arrays are correct. All builds.

### F9. 3.5.2 only: power normalisation used |window| (bug; fixed in 3.7.0)

FAIL line: `psd window=array with negative values, scale_by_freq=False: Pxx`.

**Measured.** The window has negative lobes. The result is off by maxabsdiff 0.45 against a scale of 1.4. The density variant passes on 3.5.2, because (|w|)² = w².

**What matplotlib does.** 3.5.2's `_spectral_helper` divides by `np.abs(window).sum()**2` and computes the magnitude/complex scaling with `np.abs(window).sum()`. On 3.7.1 and later the code uses `window.sum()` (main: `mlab.py:343`, `348`, `375`).

**Release notes.** Fixed by PR #25122 "FIX: scaling factor for window with negative value" (issue #24821, in `doc/release/prev_whats_new/github_stats_3.7.0.rst`).

**Verdict.** Bug in 3.5.2 (and 3.6.x), fixed in 3.7.0. Passes on 3.7.1, 3.11.2 and main.

## What held up (all four builds unless noted)

**Windows**

- `window_hanning` equals the symmetric Hann 0.5 − 0.5·cos(2πn/(M−1)) for M = 2, 7, 8, 256, and multiplies its argument.
- `window_none` returns its input.

**detrend helpers**

- `detrend_mean` matches Fraction values on integer input, for 2-D input with axis 0 / 1 / None, and raises ValueError for an out-of-range axis.
- `detrend_linear` matches the Fraction least-squares fit on integer input. It returns 0 for an exact line, a constant, two points and 0-D input, and raises ValueError for 2-D input.
- `detrend_none` returns its input unchanged.
- `detrend(key=...)` maps None / 'default' / 'constant' / 'mean' / 'linear' / 'none' / a callable correctly. On 2-D input it does per-column linear and per-row mean detrending, and raises ValueError for an unknown key.

**psd against the explicit-DFT Welch reference, to about 1e-13 relative**

- Defaults.
- Odd NFFT = 255.
- noverlap 64 and the maximal 99.
- pad_to with matching parity (100/128, 99/101).
- scale_by_freq True / False / None.
- detrend 'mean', 'linear', the `detrend_linear` function, and a custom callable.
- window_none, a triangle array, and a window with negative values (3.7.1 and later).
- sides 'twosided' (even and odd NFFT) and 'default'.
- Integer input.
- float32 input: computed in float64 with Hann. With window_none on numpy 2.x it is computed in complex64 and agrees to 1e-5, which is acceptable for single precision.
- len(x) = 100 < NFFT = 256, zero-padded as documented.
- Complex input: two-sided by default (even and odd NFFT), forced one-sided, and with ascending frequencies −Fs/2..Fs/2−df.
- Frequency vectors are exact in every case. The one-sided Nyquist frequency is positive.

**Edge cases**

- Empty input gives zeros of length NFFT//2+1.
- A single value with NFFT=1 gives 4.5 = 9/Fs.
- Constant input with detrend='mean' gives exactly 0.
- Constant input with no detrend and a boxcar window puts all its power in the DC bin, c²·NFFT/Fs.
- A 1e8 offset with detrend='mean' agrees to 1e-6.
- noverlap = NFFT, a window-length mismatch and an invalid `sides` each raise ValueError.

**Parseval**

- Exact (1e-12, Fraction variance) whenever NFFT and pad_to have the same parity: 64/64, 64/128, 63/63, 63/101.
- Two-sided real input with pad_to = 96.
- Complex two-sided: sum·df = mean|x|².

**Closed forms**

- A tone of amplitude A at a bin centre gives a one-sided psd peak (boxcar, scale_by_freq=False) of exactly A²/2, with nothing in other bins.
- `magnitude_spectrum` gives A/2, both one-sided and at ±f0 two-sided.
- `complex_spectrum` gives (A/2)e^{iφ}, and `angle_spectrum` gives φ.

**White noise** (σ = 1.5, Fs = 100, 2¹⁸ samples)

- One-sided level 0.04491 against 2σ²/Fs = 0.045.
- Two-sided level 0.02245 against σ²/Fs = 0.0225.
- The integral of the PSD equals the sample variance within 0.03%.
- The scale_by_freq=False level matches 2σ²Σw²/(Σw)².

**csd**

- Matches the reference conj(X)·Y for defaults, noverlap / pad_to / Fs combinations with matching parity, linear detrend with scale_by_freq=False, two-sided output, both inputs shorter than NFFT (zero-padded), and complex inputs.
- Axes.csd returns complex Pxy, as its docstring says.

**cohere**

- Equals |Pxy|²/(Pxx·Pyy) from the reference, including NFFT=99 with pad_to=128 and positional arguments.
- Lies within [0, 1].
- Is exactly 1 for y = −2.5x and for complex y = (1+2i)x.
- Independent noise with 64 segments gives a mean coherence of about 1/K: 0.0147–0.0191.

**specgram**

- Columns equal the per-segment reference for psd mode, with defaults (NFFT 256, noverlap 128) and other settings, including two-sided output.
- Magnitude, complex and angle modes (angle compared modulo 2π) match the reference.
- Phase mode equals angle + 2πk, with |Δ| ≤ π along frequency.
- scale_by_freq is ignored outside psd mode.
- t equals the segment midpoints (start + NFFT/2)/Fs.
- len(x) < NFFT gives one zero-padded segment, t = [NFFT/2/Fs], and the documented "Only one segment" warning.
- Complex input works.

**complex / magnitude / angle / phase spectrum**

- Match the reference with default Hann, pad_to (512, and even 400 for odd length), Fs, two-sided with window_none, and complex input. Frequencies are exact.

**SciPy** (main and 3.11.2)

- `welch`, `csd`, `coherence` and `spectrogram` in all five modes, and the spectrogram t vector, agree to 1e-9 whenever NFFT and pad_to parities match.

**Axes wrappers**

- psd: the returned Pxx is the linear density; freqs and line xdata include Fc; line ydata = 10·log10(Pxx); return_line None / False give 2-tuples; complex input works with Fc.
- csd: ydata = 10·log10|Pxy|.
- magnitude_spectrum: scale None / 'linear' / 'dB' gives linear or 20·log10 ydata, with the spectrum itself returned linear.
- angle_spectrum, phase_spectrum and cohere: data and Fc are correct.
- specgram: the returned spectrum is correct; the image array is flipud(10·log10) for psd, flipud(20·log10) for magnitude, and linear for 'linear' / angle / phase; freqs + Fc and t are correct; column centres equal t.
- specgram raises ValueError for mode='complex' and for angle with dB.

## Not checked / observations

- **Magnitude normalisation is undocumented.** `magnitude_spectrum`, and specgram mode='magnitude', return |DFT|/Σw with no one-sided doubling, so a tone of amplitude A reads A/2 one-sided. This is the same as SciPy's `scaling='spectrum'` magnitude, but no docstring states the normalisation. Treated as an observation rather than a FAIL.
- **Undocumented behaviour, printed as info and not judged:**
  - A NaN anywhere makes every bin NaN.
  - The mask of masked arrays is ignored.
  - pad_to < NFFT silently truncates the windowed segment (51 bins at pad_to=100, NFFT=128).
  - `cohere` raises ValueError when len(x) < 2·NFFT, which is not mentioned in its docstring.
  - `specgram(x, NFFT=64)` raises "noverlap must be less than NFFT" because of the documented default noverlap=128. 3.5.2's message says "less than n".
  - `csd` with len(x)=1000 and len(y)=150 at NFFT=200 silently pairs y's single zero-padded segment with all five x segments. Lengths that give 5 against 4 segments raise a broadcast ValueError. Unequal lengths are not documented.
- **Not checked:**
  - `GaussianKDE`, which belongs to another group.
  - The 32-bit `_stride_windows` path: there is no 32-bit build.
  - The `Funits` labels, which are cosmetic.
  - Rendered pixels.
  - Statistical bias of Welch estimates beyond the white-noise level, which is a property of the method, not of matplotlib.
