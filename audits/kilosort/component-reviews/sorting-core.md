# Kilosort sorting core — adversarial review notes

Scope: the code paths that produce the outputs papers actually consume — spike
times, cluster assignments, and the `good`/`mua` + ContamPct quality labels.
Primary texts, weighted by cohort usage (see `../README.md`): Kilosort 2
(v2.0.2), Kilosort 2.5 (v2.5.2), Kilosort 3 (v3.0.2) in MATLAB/CUDA, and
Kilosort 4 (v4.1.7, Python/PyTorch) from `MouseLand/Kilosort`. Line numbers
refer to those tags.

Legend: **[verified]** = reproduced numerically on shipped code;
**[code-read]** = established by reading the code, mechanism unambiguous;
**[design note]** = intentional behavior worth knowing about, not a defect.

---

## A. MATLAB era (KS2 / KS2.5 / KS3) — the versions 41/60 cohort papers pin

### KM1 — "Spike holes" at batch boundaries (issue #594) [known upstream; exposure quantified here]

The community-documented batch-boundary bug: ~7 ms of spikes go undetected
every 65,536 samples (~2.18 s at 30 kHz), ~0.3 % of any recording, in a
periodic pattern. Reported by the IBL (issue #594, Feb 29 2024) after analysis
of >600 IBL and 91 Steinmetz-lab recordings; effects visible back to Kilosort 1.

What matters for the literature is the fix timeline:

| branch | affected releases | fixed in | fix date |
|---|---|---|---|
| KS2.5 | v2.5 (Nov 2020) | v2.5.1 / v2.5.2 | Mar 8 / Apr 8 2024 |
| KS3 | v3.0 (2021) | v3.0.1 / v3.0.2 | Mar 8 / Apr 8 2024 |
| KS2 | v2.0 (Oct 2020) | **never fully fixed** | v2.0.2 (Apr 2024) patched only the CUDA kernel edge guards (`CUDA/mexMPnu8.cu`), not the MATLAB batch loading/timestamping in `mainLoop/trackAndSort.m` (still `batchstart = 0:NT:...`, `fread(..., [NT ops.Nchan])`) |
| KS4 | not affected | — | padded-batch design (`spikedetect.py:41-42,164-165` zeroes exactly the padding, batches tile contiguously) |

Note also that the first fix attempt (v2.5.1/v3.0.1, "fixes main bug") was
itself revised a month later: v2.5.2 comments out v2.5.1's batch loading as
"old broken way ... spike holes bug issue #594, location 1/2" and rewrites
both the loading and the time-offset formula (`trackAndSort.m` v2.5.1 vs
v2.5.2 diff). Results from v2.5.1/v3.0.1 differ from both the original and
the final fix.

Every KS2/2.5/3 paper in our cohort published through 2024 — and realistically
the 2025 ones, given analysis lead times — sorted with affected code. This is
not our finding; the contribution here is the per-paper exposure table in
`../kilosort_profiles.jsonl` and the observation that the KS2 branch (the
largest group, 19/60 papers) never received the MATLAB-side fix.

### KM2 — KS2.5/KS3 export a fake (identity) whitening matrix to Phy [code-read]

`utils/rezToPhy.m` (KS2.5 line 70; KS3 `rezToPhy.m`/`rezToPhy2.m` line 77):

```matlab
% whiteningMatrix = rez.Wrot/rez.ops.scaleproc;
whiteningMatrix = eye(size(rez.Wrot)) / rez.ops.scaleproc;
```

KS2.0 (`utils/rezToPhy.m` line 69) exports the real `rez.Wrot`. KS2.5 and KS3
ship a scaled identity instead — from their first releases (Nov 2020 /
2021) — so:

- `whitening_mat.npy` / `whitening_mat_inv.npy` in every KS2.5/KS3 Phy output
  are not the whitening transform that was actually applied;
- `templates.npy` "unwhitened" with that inverse stays in whitened space:
  absolute amplitudes and the cross-channel energy distribution of exported
  templates are wrong for any downstream tool that trusts the standard Phy
  contract (waveform-amplitude metrics, unwhitened template shape analyses,
  µV conversions);
- amplitude-derived quantities are **not comparable across KS2.0 vs
  KS2.5/KS3** outputs, silently.

The likely rationale is that `params.py` points Phy at the already-whitened
`temp_wh.dat` (so identity is self-consistent *within* Phy). But nothing in
the output warns downstream consumers, and KS4 reverted to exporting the real
matrix (`kilosort/io.py:333-343`, with the identity hack kept as a comment:
"this was different in KS 2.5 because the binary file was already whitened").
We found no upstream issue documenting this. At minimum a documentation
erratum for KS2.5/KS3 users; the 22 KS2.5+KS3 cohort papers plus any pipeline
using `whitening_mat_inv.npy` (e.g. µV calibration steps) are in scope.

### KM3 — Whitening covariance normalizer off-by-one [verified, `verify/km3_nskipcov.py`]

`preProcess/get_whitening_matrix.m` line 48 (identical in KS2 v2.0.2, KS2.5
v2.5.2, KS3 v3.0.2):

```matlab
while ibatch<=Nbatch
    ...
    CC = CC + (datr' * datr)/NT;
    ibatch = ibatch + ops.nSkipCov;
end
CC = CC / ceil((Nbatch-1)/ops.nSkipCov);
```

The loop accumulates `floor((Nbatch-1)/nSkipCov) + 1` batches; the normalizer
is `ceil((Nbatch-1)/nSkipCov)`. When `nSkipCov | (Nbatch-1)` these differ by
one and the covariance is inflated by `(m+1)/m`, `m = (Nbatch-1)/nSkipCov`.
Since `Wrot ~ C^(-1/2)` the whitened data are uniformly scaled down by
`sqrt(m/(m+1))`, making every threshold in whitened units (`ops.Th`,
`ops.spkTh`) effectively `sqrt((m+1)/m)` harder:

| Nbatch | duration @30 kHz | covariance | effective thresholds |
|---|---|---|---|
| 26 | ~57 s | ×2.00 | ×1.414 |
| 51 | ~1.9 min | ×1.50 | ×1.225 |
| 251 | ~9.5 min | ×1.10 | ×1.049 |
| 1651 | ~62 min | ×1.015 | ×1.008 |

With default `nSkipCov = 25`, 1 in 25 batch counts is affected; the bias is
material for short recordings and cosmetic for hour-long ones. It also means
adding ~2 s of recording can discontinuously change detection thresholds.
KS4 fixed this by counting iterations
(`kilosort/preprocessing.py::get_whitening_matrix`, variable `k`).

Two adjacent, strictly negligible quirks in the same function [code-read]:
the covariance sums over `NTbuff = NT+3*ntbuff` samples but divides by `NT`
(uniform ×1.003, cancels through the whitening normalization), and filter
edge transients are included in the covariance batches.

### KM4 — `ops.midpoint` chronic-recording branch cannot run [code-read]

`preProcess/datashift2.m` lines 76-86 (KS2.5): the branch for concatenated
chronic recordings calls `align_block(...)`, which does not exist anywhere in
the v2.5.x or v3.0.x trees (only `align_block2.m` and `align_pairs.m` exist)
— "Undefined function" crash. Even if it ran, `yblk`, `F0`, `F0m` are
undefined on that path but consumed unconditionally at lines 136/148-149.
Loud failure, so no silent damage to papers; the feature is simply unusable.

### KM5 — splitAllClusters bookkeeping defects [code-read]

`postProcess/splitAllClusters.m` (KS2.5):

1. Line 192: `isplit = rez.simScore==1;` — the carefully maintained per-cluster
   provenance *vector* (line 30, updated at line 157) is clobbered by a
   logical *matrix*; `rez.isplit` ends up meaning "simScore was exactly 1",
   which includes the diagonal and any coincidental 1.0 scores. Split-parent
   pairs also keep `simScore = 1` forever (lines 193-194), pinning Phy's
   similarity ordering.
2. Line 27 recomputes the peak channel `iW` from the *final* (post-tracking)
   `rez.dWU`, while the PC features being split were extracted on the channel
   neighborhoods of the *initial* tracking `iW` (`trackAndSort.m` line 92
   computes `iW` once, before the batch loop, and `rez.iNeighPC` retains that
   assignment). For clusters whose peak channel drifted during tracking, the
   reconstructed split templates (lines 151-152) are written onto a shifted
   channel set. Affects a minority of clusters, by roughly one channel pitch;
   the subsequent `mexSVDsmall2` re-fit partially absorbs it.

### KM6 — remove_ks2_duplicate_spikes: unusable parameter, and off by default [code-read]

`postProcess/remove_ks2_duplicate_spikes.m` line 40 validates the *numeric*
`channel_separation_um` with `@(x) (ischar(x))`, so any attempt to pass a
custom numeric value is rejected by `inputParser` (the default 100 works only
because defaults are not validated). Moot in practice: the call is commented
out of `main_kilosort.m` (lines 47-49), so default KS2.5 output retains
cross-template double-counted spikes — one motivation for KS4's built-in
`remove_duplicates` (same-cluster only) and for downstream dedup tools.

### KM7 — Quality-label statistics are liberal by construction [design note]

The `good`/`mua` label chain (`postProcess/ccg.m` + `set_cutoff.m`) makes
three choices that each push toward more "good" units:

- contamination `Q = min(Qi / max(Q00, Q01))`: the *minimum* over 10 nested
  central windows (±1..±10 ms) of a noisy ratio, normalized by the *larger*
  of two baseline estimates — a multiple-comparisons minimum with the most
  favorable denominator;
- the refractoriness p-value `R = min(rir)` similarly takes the minimum over
  window sizes, with `lam` from the *largest* of three shoulder estimates
  (`ccg.m` lines 59-60), which makes small counts look more significantly
  refractory;
- `est_contam_rate` is reported at the final (reverted) amplitude threshold,
  i.e. after the cutoff search has already optimized the ACG.

These are documented-in-code design choices of the original authors, not
bugs; we note them because papers routinely treat `KSLabel == good` and
`ContamPct` as calibrated quantities, and because KS4 then *loosened* the
thresholds further (below). Minor mechanical quirks in `ccg.m` [code-read]:
the ±500 ms edge bins are correctly excluded from the far shoulders, but the
near shoulders are asymmetric (40 bins at −50..−11 ms vs 39 at +12..+50 ms,
correctly normalized by their counts); `Qin`/`Qin1` (lines 85-86) are
computed and discarded.

### KM8 — Diagnostic-only quirks [code-read]

`preProcess/align_block2.m`: registration uses `circshift`, so spike density
shifted past the probe end wraps around (up to ~4 % of bins at the ±15-bin
search limit) — shared by KS4's port (`datashift.py`), inherent to the
FFT-style approach. The `F0m` reconstruction (lines 111-117) reuses the
*nonrigid* `dt = -5:5` while total rigid shifts span ±15, so batches with
larger accumulated shifts are left unshifted in `F0m`; `F0m` is only stored
in `rez` (and discarded entirely in KS4's port), so no result depends on it.

---

## B. Kilosort 4 (current Python line) — filable upstream

### KL1 — Refractory-CCG split veto dead since v4.1.5 [verified, `verify/kl1_swarmsplitter_gate.py`]

`kilosort/swarmsplitter.py::check_CCG` (v4.1.5-v4.1.7):

```python
K , T = compute_CCG(st1, st2, nbins = nbins, tbin = tbin)
if len(st1) == 0 or len(st2 == 0) or T == 0:
    return False, False
```

`len(st2 == 0)` is the length of a boolean array — truthy for every non-empty
`st2` — so the guard fires on all real inputs and `check_CCG` always returns
`(False, False)`. `refractoriness()` therefore never vetoes a split, and the
`meta` (spike-times) channel threaded through `clustering_qr.run →
swarmsplitter.split` is dead code. KS4.0-4.1.4 applied the veto, as do the
MATLAB versions (`splitAllClusters.m` lines 118-127). Introduced in v4.1.5
(Jan 15 2026, likely while guarding the ZeroDivisionError of issue #1002);
present through v4.1.7 (Mar 4 2026, current).

Demonstration on shipped 4.1.7: a single simulated refractory neuron
(3 ms refractory period, ~10 Hz, 20 min) split in half gives
`CCG_metrics R12 = 0.0000, Q12 = 0.0000` — pre-4.1.5 verdict
`cross_refractory = True` ("never split") — yet `check_CCG` returns
`(False, False)` and `refractoriness` returns 0 ("allow split").

Secondary defect in the same line: the guard sits *after* `compute_CCG`, so
the empty-array case it tests has already crashed inside `compute_CCG`
(numba `ValueError` on `.max()` of an empty array); only the `T == 0` clause
can usefully trigger. The fix is to correct the parenthesis **and** move the
guard above the `compute_CCG` call.

Expected effect of the bug: oversplitting of units whose sub-clusters remain
mutually refractory (bursty or amplitude-varying or drifting units) —
exactly the failure mode the veto was added to prevent. Cohort exposure: the
single KS4 paper predates v4.1.5; this is forward-protection for the many
labs on current releases. Already independently reported as open issue
#1042 (Aug 21 2026, no maintainer response, no PR); our contribution is the
fix PR with the guard-placement correction and the quantified demonstration.

### KL2 — ContamPct = 0.0 exported for ≤10-spike clusters [verified, `verify/kl2_contampct.py`]

`kilosort/CCG.py::refract` initializes `R12 = np.zeros(Nfilt)` and computes
contamination only for clusters with `len(st1) > 10` and nonzero span;
`io.save_to_phy` (lines 406-423) writes `est_contam_rate * 100` to
`cluster_ContamPct.tsv`. A junk cluster with ≤10 spikes is exported with
**ContamPct 0.0 — the best possible score** — indistinguishable from a
genuinely clean unit. KS2.5/KS3 defaulted unevaluable units to
`est_contam_rate = 1` (100 %; `set_cutoff.m` lines 15, 30, 60).

Demonstration (4.1.7): 5000-spike Poisson unit → ContamPct 93.9 (correct);
8-spike junk cluster → ContamPct 0.0. Any paper selecting units by
`ContamPct < x` without a separate minimum-spike-count criterion admits every
tiny cluster. Fix: initialize to 1.0 (KS2.5 semantics) or NaN.

### KL3 — Latent/dead-code issues worth an upstream note [code-read]

1. `kilosort/hierarchical.py::find_merges` line 56:
   `m = cc[y,x] + cc[x,x] + cc[x,y] + cc[y,x]` counts `cc[y,x]` twice and
   omits `cc[y,y]`; feeds `tstat[:,2]`, which is only read in
   `swarmsplitter.split`'s fourth branch — unreachable because the bimodality
   branch always sets `criterion = ±1` (and its own comment says "not
   reachable"). No effect on results; a trap for future refactors.
2. `kilosort/datashift.py` lines 158-166 port the KM8 `F0m` quirk (shadowed
   `dt`), but both `F0` and `F0m` returns are discarded in `datashift.run`.
3. KS4's default "good" criteria are looser than both the KS4 paper and the
   MATLAB releases: `acg_threshold` 0.1→0.2 is documented in a code comment
   (`CCG.py` lines 82-85), but the accompanying p-threshold change
   (`Q12 < .05` → `Q12 < .2` for `is_refractory`, `CCG.py` line 90) is not
   documented anywhere we could find. Cross-version `KSLabel` counts are not
   comparable.
4. `clustering_qr.run` line 486: any spatial group with fewer than 1000
   spikes skips clustering entirely — all its spikes become one cluster.
   Consequential for short recordings and sparse-firing regions (several
   distinct low-rate neurons at one site get fused, then labeled by KL2's
   path if small enough). A documented `min_spikes_for_clustering`-style
   setting would make this visible to users. [design note]

---

## Withdrawn during review (checked and exonerated)

- **KS4 batch-boundary holes**: `spikedetect.py`/`template_matching.py` zero
  detections in exactly the `nt`-sample padding and batches tile contiguously
  (`(xy - nt) + ibatch*batch_size`); no KS2.5-style holes. The cross-boundary
  *duplicate suppression* (`max_pool` over `iC2`) is weakened within `nt` of
  boundaries — bounded, and later stages dedup same-cluster spikes.
- **KS4 `run_matching` interleaved subtraction**: the `n = 2` interleaved
  peel groups guarantee same-group peaks are > 2·nt apart, so the advanced-
  indexing `-=` never hits overlapping windows; the scheme is correct (peaks
  within nt of each other are excluded by the max-pool equality condition).
- **`template_match` sign recovery** (`spikedetect.py` line 157): the
  `(1+imax) * A[...].sign()` encoding is correct on inspection.
- **KS2.5 `ccg.m` sweep-line pair counting**: bounds and bin rounding are
  correct, including the ±500 ms edge bins being excluded from shoulders.
- **KS2.5 v2.5.2 fixed `trackAndSort`**: the `batchstart = ntpad:NT:...`
  tiling assigns each spike to exactly one batch with correct absolute times
  (offset algebra checked; contiguous, no overlap, no gap).
- **`preprocessDataSub` filter buffers**: 64-sample `ntbuff` blending with a
  3rd-order 300 Hz Butterworth leaves edge transients ~3e-4 of amplitude in
  the kept region — negligible.
- **KS4 `Mstats`** (`ki = m*ki/ki.sum()`): a no-op rescaling, not a bug.
- **KS4 `make_pc_features` in-place `tF` mutation**: each spike row is
  rewritten exactly once (clusters partition spikes); no cross-contamination.
