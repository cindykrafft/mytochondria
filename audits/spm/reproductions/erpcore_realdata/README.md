# The `@meeg/badsamples` fix (SP3, PR #163) on ERP CORE: 39 participants, two paradigms

SPM's own MMN tutorial recording (`../mmn_realdata/`) showed the artefact-window
defect corrupting the bad-sample mask wholesale while the robust-averaged MMN moved
only 1.5 %. That is one participant, a 100 ms baseline, and a workflow with a
second safety net. This directory asks the question the way the AFNI reanalysis did:
on an open multi-participant dataset, with an ordinary SPM pipeline, how much does
the merged fix change the numbers a paper would report?

**Data.** ERP CORE (Kappenman et al. 2021, *NeuroImage* 225:117465; OSF `thsqg`):
40 neurotypical adults, Biosemi ActiveTwo, 30 scalp channels + 3 EOG, 1024 Hz. Two
of its seven paradigms were used, chosen for their epoch geometry, because the
defect's shift equals the distance from epoch start to time zero:

| Paradigm | Epoch | Shift of every artefact window | Measure (ERP CORE's own) |
|---|---|---|---|
| **P3**, active visual oddball, stimulus-locked | −200 … 800 ms | 200 ms | target − standard, Pz, 300–600 ms |
| **ERN**, flankers task, response-locked | −600 … 400 ms | 600 ms | error − correct, FCz, 0–100 ms |

39 participants have raw files for each paradigm (the OSF folders hold 39 numbered
subject directories per task); all 39 were processed.

**Pipeline** (`erpcore_pipeline.m`, real SPM functions executed in GNU Octave 8.4,
SPM MEX files rebuilt with `make PLATFORM=octave`). Build-independent stage: convert
from EEGLAB `.set`; shift stimulus codes by 26 ms (ERP CORE's monitor-delay
correction); re-reference to (P9+P10)/2 and form bipolar VEOG/HEOG (ERP CORE's
montage); resample 1024→256 Hz with the exact `resample` method (avoiding the SP4
path); 0.1 Hz high-pass, 30 Hz low-pass (SPM Butterworth defaults); epoch with ERP
CORE's bin definitions (P3: stimuli followed by a correct response within 200–1000 ms;
ERN: responses preceded by a flanker stimulus within 200–1000 ms) and baseline
(P3: −200–0 ms; ERN: −400 … −200 ms). Build-dependent stage, run once with
`badsamples.m` at `spm/spm@530ec52` and once at upstream `main` after PR #163, on the
same epoched file: `spm_eeg_artefact` in **mark** mode (`threshchan`, 100 µV,
200 ms excision window, EEG+EOG channels, bad-channel threshold 0.2, the defaults
apart from the threshold); the bad-sample mask via `badsamples`; then two
consumers of that mask, (i) `spm_eeg_artefact` in **reject** mode with the `events`
plugin (a trial is rejected if any channel has a marked sample) followed by a
**plain average**, and (ii) **robust averaging** with *remove bad data* on. No
ocular correction is applied: this is a threshold-only pipeline, which many SPM
users run and which SPM's manual chapters use; it is harsh on blink-heavy
participants under either build, and that is stated with the results.

**Reproduce.** `python3 osf_index.py etdkz P3; python3 osf_index.py q6gwp ERN`
(OSF file index), `bash fetch_all.sh P3; bash fetch_all.sh ERN` (2.2 + 4.3 GB),
two SPM trees differing only in `@meeg/badsamples.m` (see `run_subject.sh`),
`./run_workers.sh P3 3; ./run_workers.sh ERN 3`, then
`python3 analyze.py results out; python3 make_figure.py out out/erpcore.pdf`.
One Octave compatibility patch was applied identically to both trees:
`spm_robust_average.m`'s `nanmedian` helper returns NaN for an all-NaN column,
as MATLAB's `median([])` does, where Octave's raises an error. `logs/` holds the
per-participant trial counts and mask summaries from the actual runs.

## Results (`results/summary.json`, per-participant tables in `results/*_subjects.tsv`)

### The mask

| | P3 (shift 200 ms) | ERN (shift 600 ms) |
|---|---|---|
| Detector windows written (both builds see the same events) | 20,648 | 39,155 |
| Windows the shift pushes entirely out of the epoch | 15 % pooled, median 19 % per participant | **97 % pooled, median 98 %** |
| Share of true artefact samples the shipped code excluded (median) | 30 % | **0.5 %** |
| Share of the shipped code's exclusions that were clean (median) | 33 % | 17 % |
| Jaccard overlap of the two masks (median) | 0.25 | 0.005 |
| Bad-sample count, all participants | 1.03 M vs 2.06 M | 0.04 M vs 3.35 M |
| Channels classified bad (mark mode, threshold 0.2) | 5 vs 20, differing in 8 participants | **0 vs 16**, differing in 8 participants |

In the response-locked design every artefact that occurs after the response, which
is where blinks cluster, is written by the detector at 600–1000 ms into the epoch
and read back 600 ms later, off the end. The shipped `badsamples` returns an
essentially empty mask, and everything built on it behaves as if the artefact step
had not run.

### Consumer 1: rejection by marked events, then a plain average

| | P3 | ERN |
|---|---|---|
| Trials rejected, pooled | 3,655 vs 4,076 of 7,261 (50 % vs 56 %) | **326 vs 7,892 of 15,364 (2 % vs 51 %)** |
| Condition-of-interest trials retained (targets / errors) | 669 vs 570 | 1,571 vs 710 |
| Participants left with **no** trials of interest | 1 vs 3 | **0 vs 6** |
| Participants with fewer than 6 | 9 vs 15 | 1 vs 9 |
| Participants with ≥ 6 in both builds (analysed below) | 24 | 30 |
| Group mean of the ERP measure, before vs after | 7.6 vs 7.4 µV | **−10.4 vs −8.3 µV** |
| Paired *t* (before − after) | 1.10, *p* = 0.28 | **−3.23, *p* = 0.003** |
| Per-participant correlation before vs after | 0.99 | 0.76 |
| Median absolute change per participant | 0.29 µV (6 %) | **2.1 µV (24 %)** |
| Participants whose measure changed by > 10 % | 11 of 24 | 22 of 30 |
| One-sample *t* of the effect, before / after | 7.5 / 7.0 | −11.1 / −8.3 |

Under the shipped code the same rejection settings kept 98 % of ERN trials, and the
resulting grand-average ERN was 26 % larger than under the fixed code, with a
broader waveform and a delayed error positivity (figure panel C), consistent with
blink and movement artefact retained in the error trials. The paired difference is
reliable across the 30 participants. Six participants who have no artefact-free
error trials at this threshold, and whom the fixed code correctly leaves without an
ERN, were silently given one by the shipped code. The effect is not a loss of
significance: the ERN is present under both builds; its size, its waveform, and
which participants contribute are what changed.

### Consumer 2: robust averaging with *remove bad data*

| | P3 | ERN |
|---|---|---|
| Group mean before vs after | 5.61 vs 5.60 µV | −9.46 vs −9.31 µV |
| Paired *t* | 1.12, *p* = 0.27 | −1.52, *p* = 0.14 |
| Per-participant correlation | 0.9997 | 0.993 |
| Median absolute change | 0.0006 µV | 0.009 µV |
| Participants changed by > 1 µV | 0 | 1 |

As on the MMN data, robust weighting cushions the mask almost completely at the
measurement channel: the samples the mask fails to remove are the ones the robust
weights down-weight anyway. Whole-scalp RMS change of the difference wave is larger
(median 21 % for P3, 4 % for ERN) because it includes the frontal channels that
carry the artefact and, in eight participants per paradigm, are reclassified.

### Reading this fairly

- The ERN pipeline rejects half of all trials after the fix. A threshold-only
  pipeline without ocular correction is harsh on a response-locked task where
  participants blink after responding; that is a property of the pipeline, not of
  the fix. The point of the comparison is that the shipped code turned the same
  pipeline into one that rejected almost nothing, with no warning, so a user who
  chose these settings got neither the analysis they specified nor any sign of it.
- The P3 and MMN results bound the other end: with a short baseline the mask is
  partly right, and both consumers land close to the fixed result.
- This is Octave, not MATLAB, with one compatibility patch applied to both builds;
  the SPM code executed is otherwise unmodified.
- ERP CORE's own pipeline uses ICA blink correction and per-participant
  thresholds, so its published values are not what either build here reproduces;
  the comparison is build against build on identical settings.
