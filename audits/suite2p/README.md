# Suite2p audit

Suite2p (MouseLand/suite2p; Python/PyTorch) is the dominant open pipeline for
two-photon calcium-imaging analysis: registration, ROI detection, trace
extraction with neuropil correction, OASIS deconvolution, and an ROI
classifier. 32 papers in our six-journal cohort (2021–2026) use it.

Adversarial review of `main` @ 90be895 (v1.1.0), with every finding verified
on the shipped `suite2p==1.1.0` wheel on CPU.

## Cohort exposure

From `suite2p_profile.py` over the 32 full texts (`suite2p_profiles.jsonl`)
and an option-level re-grep (`suite2p_option_hits.json`):

| feature | papers |
|---|---|
| two-photon | 31 |
| registration / motion correction described | 23 |
| bidirectional / resonant scanning described | 14 |
| deconvolution (OASIS / `spks`) | 18 |
| neuropil correction | 17 (coefficient 0.7 stated: 5) |
| classifier / `iscell` probability used | 8 |
| Cellpose (anatomical) mode | 3 |
| baseline method stated | 2 |
| suite2p version ≥ 1.0 stated | 0 (only one paper states any version) |

## Findings

Full detail with file:line citations in
[`component-reviews/pipeline-core.md`](component-reviews/pipeline-core.md);
runnable scripts with expected output in [`verify/`](verify/).

| id | component | finding | status |
|---|---|---|---|
| **S2** | `registration/bidiphase.py` | Bidirectional-phase correction corrupts every odd scan line when given torch tensors (overlapping in-place copy); the registration path has passed torch tensors since **v1.0.0.1 (Feb 2026)**. 34 % of odd-line pixels wrong end-to-end through `register_frames`; the reference image stays correct, so frames and reference disagree. Opt-in setting, recommended for resonant scanning (14 cohort papers). | verified; fix patch validated |
| **S1** | `classification/classifier.py` | Feature values at/below the training minimum (and NaNs) are binned into the **last** bin: skew below the minimum scores P(cell) 0.986 instead of 0.535. 0.4 % of the builtin training set, no verdict flips there; user-trained classifiers hit their minima more often. | verified; fix patch validated |
| **S5** | `extraction/extract.py` | Sparse-mask indices built as float32 — exact only to 2²⁴ pixels (~4096²); larger fields of view mix pixels between ROIs. | limit verified; fix patch |
| **S3** | `extraction/dcnv.py` | `baseline='constant'` subtracts one scalar (global minimum over all neurons), not a per-trace constant; non-default. | code-read; issue |
| **S7** | `detection/anatomical.py` | Spatial high-pass applied twice in Cellpose mode (duplicated line, new in v1.0.0.1); changes which ROIs Cellpose finds when `highpass_spatial` is set. | code-read; issue |
| **S4** | `registration/nonrigid.py` | Nonrigid warp truncates to int16 (−0.5 mean offset in all traces). | negligible; noted |

Exonerations (OASIS, maximin baseline, neuropil masks, extraction weighting,
rigid/nonrigid phase correlation, sparsery thresholds, uint16 handling) are
listed at the end of the component review.

## Upstream

Three fix patches plus two issues in [`upstream/`](upstream/). Suite2p takes
PRs on GitHub against `main` from a fork.
