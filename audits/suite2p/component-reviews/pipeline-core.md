# Suite2p pipeline core — adversarial review notes

Scope: the code paths behind the numbers the 32 cohort papers report —
registration (`registration/`), ROI detection (`detection/`), trace
extraction and neuropil correction (`extraction/masks.py`, `extract.py`),
baseline + OASIS deconvolution (`extraction/dcnv.py`), and the ROI classifier
(`classification/`). Suite2p `main` at 90be895 (v1.1.0, Jun 2026); line
numbers refer to that commit. Verification on the shipped `suite2p==1.1.0`
wheel (torch 2.13, CPU) in `../verify/`.

Legend: **[verified]** reproduced on the shipped package; **[code-read]**
mechanism unambiguous from the source; **[design note]**; **[exonerated]**.

---

## S2 — `bidiphase.shift` corrupts odd scan lines on torch tensors [verified]

`registration/bidiphase.py::shift` corrects bidirectional-scan line phase by
moving the odd lines with an overlapping in-place assignment:

```python
if bidiphase > 0:
    frames[:, 1::2, bidiphase:] = frames[:, 1::2, :-bidiphase]
```

numpy resolves overlapping assignments with a temporary copy;
`torch.Tensor.copy_` does not, so the assignment reads pixels it has already
overwritten. Up to v0.14.x the registration code passed numpy arrays and this
was correct. Since **v1.0.0.1 (Feb 11 2026)** `register_frames` (line 613)
and `shift_frames_and_write` (line 756) pass torch tensors, so with
bidirectional-phase correction enabled every frame's odd lines are corrupted
instead of shifted — while the reference image is still shifted through the
numpy path (`registration_wrapper` line 931) and is therefore correct, so
frames and reference disagree.

Verified on the shipped 1.1.0 (`../verify/s2_bidiphase_torch.py`):

```
unit: numpy odd row after shift 3: [8, 9, 10, 8, 9, 10, 11, 12]
unit: torch odd row after shift 3: [8, 9, 10, 8, 9, 10, 8, 9]  | matches numpy: False
end-to-end register_frames(bidiphase=3, CPU): odd lines correct? False
  fraction of odd-line pixels wrong: 34.4%
```

The corrupted lines are then phase-correlated, warped, extracted and
deconvolved like any other data. Trigger: `do_bidiphase=True` (auto-estimate)
or a nonzero `bidiphase` setting — off by default, but recommended by the
docs for resonant/bidirectional scanning, which 14/32 cohort papers describe.
No cohort paper states a suite2p version ≥ 1.0, so this is forward-protection
for current users rather than a published-result issue. Fix
(`upstream/0001-bidiphase.shift-...patch`): copy the source slice first
(`.clone()` for torch, `.copy()` for numpy); validated — odd lines exact for
positive and negative offsets on the patched tree.

## S1 — Classifier bins values at the training minimum into the last bin [verified]

`classification/classifier.py::_get_logp` (lines 136-141):

```python
x[x < self.grid[0, n]] = self.grid[0, n]
x[x > self.grid[-1, n]] = self.grid[-1, n]
x[np.isnan(x)] = self.grid[0, n]
ibin = np.digitize(x, self.grid[:, n], right=True) - 1
logp[:, n] = np.log(self.p[ibin, n] + 1e-6) - np.log(1 - self.p[ibin, n] + 1e-6)
```

`np.digitize(x, grid, right=True)` returns 0 for `x == grid[0]`, so every
value clamped to the training minimum (and every NaN) gets `ibin = -1` — the
probability of the **last** bin. On the builtin classifier
(`../verify/s1_classifier_bins.py`):

```
skew       ==min -> bin -1 -> p 0.948   (first bin p 0.071, last bin p 0.948)
compact    ==min -> bin -1 -> p 0.001   (first bin p 0.448, last bin p 0.001)
npix_norm  ==min -> bin -1 -> p 0.007   (first bin p 0.036, last bin p 0.007)
P(cell): skew below training min 0.9856 | just above min 0.5345 | above max 0.9856
```

A ROI whose skew is below the classifier's training range is scored as if it
had the highest skew (P(cell) 0.99 instead of 0.53). Impact is bounded by how
often features fall at/below the training minimum: on the builtin
classifier's own 14,058-ROI training set that is 52 ROIs (0.4 %) and changes
no 0.5-threshold verdict — small for the builtin model, but user-trained
classifiers (`classifier_user.npy`, the default path) are fit on far fewer
ROIs, so their minima are hit more often. One-line fix (clip the bin index),
validated: P(cell) is continuous across the minimum (0.5357 either side).
Eight cohort papers describe using the classifier probability.

## S3 — `baseline='constant'` subtracts one global scalar [code-read]

`extraction/dcnv.py::preprocess` lines 176-179:

```python
elif baseline == "constant":
    Flow = gaussian_filter(F, [0., sig_baseline])
    Flow = np.amin(Flow)
    F -= Flow
```

`np.amin` over the whole `(n_neurons, n_frames)` array: the *same* scalar —
the minimum over all neurons — is subtracted from every trace, so any neuron
whose own smoothed minimum is above that value keeps a positive floor and
OASIS (non-negative, no sparsity penalty) turns that floor into a constant
stream of "spikes". The parameter table describes `sig_baseline` as "applied
to find constant", which reads as per-trace; the per-trace form would be
`np.amin(Flow, axis=1, keepdims=True)`. Present unchanged since at least
v0.14.4. Default is `maximin` (unaffected), and only 2 cohort papers state a
baseline method. Filed as an issue rather than a PR since either reading may
be intended.

## S7 — Spatial high-pass applied twice in the Cellpose path [code-read]

`detection/anatomical.py::select_rois` lines 253-254 contain the identical
statement twice:

```python
img -= gaussian_filter(img, diameter[1] * settings["highpass_spatial"])
img -= gaussian_filter(img, diameter[1] * settings["highpass_spatial"])
```

v0.14.4 has it once. The second pass high-passes the already high-passed
image, i.e. a stronger filter than `highpass_spatial` implies, changing the
image Cellpose segments (and thus which ROIs exist) for anatomical-mode users
who set `highpass_spatial` — 3 cohort papers use Cellpose mode. Possibly an
intentional "two passes", so filed as a question with the diff.

## S4 — Nonrigid warp truncates to int16 [code-read; magnitude verified]

`registration/nonrigid.py::transform_data` returns
`fr_shift.squeeze().short()`: truncation toward zero of the bilinearly
interpolated frame. Every nonrigidly registered frame therefore carries a mean
offset of −0.5 intensity units (`../verify/s4_s5_numeric.py`: 0.4995) relative
to rounding, i.e. a constant −0.5 in every `F` and `Fneu` trace. Negligible
against typical signal levels and cancels in ΔF/F; recorded for completeness.

## S5 — Sparse-mask indices built as float32 [code-read; limit verified]

`extraction/extract.py` lines 65 and 74 build the pixel/ROI index tensors
with `torch.Tensor([...])` (float32), exact only up to 2²⁴ = 16,777,216.
Flattened pixel indices beyond that — fields of view larger than about
4096 × 4096 — round to a neighbouring pixel, silently mixing pixels between
ROIs. No cohort recording is that large; one-line fix in `upstream/`.

---

## Design notes

- **Gaussian reference smoothing is not Gaussian** (`registration/utils.py::gaussian_fft`):
  the kernel is centred on a half-pixel for even sizes and `torch.real(fft2(ifftshift(kernel)))`
  discards the resulting linear phase, leaving a real, zero-phase filter with a cosine
  roll-off instead of the Gaussian. No shift is introduced; only the spectral shape differs
  from the documented `smooth_sigma`. Harmless, consistent between rigid and nonrigid.
- **Crop symmetric in the shift magnitude** (`register.py::compute_crop`): `yrange` uses
  `max(|yoff|)` on both edges, over-cropping the side the sample did not move toward.
- **Unsigned 16-bit input is halved** (`io/tiff.py` line 133, `io/h5.py` line 95): absolute
  `F` units are half the raw ADC units for uint16 recordings; ΔF/F unaffected.
- **Bad frames are only excluded from detection binning when they are a minority of a batch**
  (`detection/detect.py::bin_movie` line 47); otherwise they are averaged in.
- **Compact minimum** `max(1.0, mrs/mrs0)` and the builtin grid minimum 0.9555 mean perfectly
  compact ROIs do not hit S1's wrap on the builtin model; they would on a user model trained
  where 1.0 is the minimum.

## Exonerated (checked, correct)

OASIS pool merging (`dcnv.py::oasis_trace`, matches Friedrich et al. 2017 with
`g = exp(-1/(tau·fs))`); maximin baseline (odd window, replicate padding,
Gaussian pre-smoothing); neuropil mask construction (inner exclusion ring,
`lam_percentile` cell-pixel map, rectangular growth to `min_neuropil_pixels`);
trace extraction as `lam`-weighted mean and neuropil mean; rigid phase
correlation (whitened cross-power spectrum, `maxregshift` window, argmax
decode); nonrigid block tiling (50 % overlap), SNR-gated block smoothing,
kriging subpixel upsampling (`mat_upsample`); reference recentering;
`pick_initial_reference` (uses 19 not 20 frames, cosmetic); sparsery threshold
`5·threshold_scaling·max(1,scale)` and the `nbinned/1200` multiplier; overlap
pruning in reverse detection order; classifier logistic layer; uint16/int32
input handling.
