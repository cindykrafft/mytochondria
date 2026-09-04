# SP3 real-data demonstration — `@meeg/badsamples` baseline double-count

**Data:** SPM's MMN tutorial dataset (`eeg_mmn/subject1.bdf`, 512 Hz, 128-ch
Biosemi; 480 standards / 120 deviants). **Pipeline:** SPM's own "Advanced topics
in M/EEG artefact removal" chapter, which uses this dataset — downsample 200 Hz,
0.5–30 Hz, epoch −100..400 ms with baseline correction, artefact detection in
**mark** mode (z-scored-difference detector, 100 ms excision window,
badchanthresh 1), then **robust averaging with "Remove bad data = yes"**.
**Code:** the actual SPM functions executed in GNU Octave 8.4 (see
`sp4_result.md` for the build notes), run twice with `@meeg/badsamples.m` at
`530ec52` (pre-fix) and at upstream `main` after PR #163 (merged). Script:
`sp3_pipeline.m` / `run_sp3.sh`; comparison: `sp3_compare.py`; log: `sp3_run.log`.

## The mechanism, on real data
600 epochs, 101 samples each, `timeOnset = −0.1 s`, 200 Hz → baseline = 20 samples.

| | pre-fix | merged |
|---|---|---|
| trial 5: detector wrote its artefact at epoch sample 30 (130 ms long); `badsamples` marked | **51..77** | 31..57 |
| median onset shift, all 316 (channel, trial) bad runs present under both | **20 samples = 100 ms** (= the baseline) | — |
| bad samples marked in total | 7 584 | 9 017 |
| trials with any bad sample | 84 | 94 |
| bad runs truncated at the epoch end (artefact pushed off the edge) | **100** | 37 |
| Jaccard overlap of the two masks | 0.151 | |
| of the truly-artefactual samples, fraction pre-fix actually excluded | **24.2 %** | 100 % |
| of the samples pre-fix excluded, fraction that were actually clean | **71.2 %** | 0 % |

So on real data the pre-fix mask is mostly wrong in both directions: three
quarters of what it removed was clean signal, three quarters of the detected
artefact was kept, and ten trials' artefacts fell off the end of the epoch and
were lost entirely.

## Downstream effect on the ERP — small, and that is the honest result
MMN = deviant − standard from the robust average with Remove-bad-data:

| | pre-fix | merged |
|---|---|---|
| GFP peak | 255 ms (2.771) | 255 ms (2.778) |
| largest channel at peak (A14) | −10.91 µV | −10.91 µV |
| max \|difference\| across channels × time | 0.37 µV (at 300 ms) | |
| RMS difference over 100–300 ms | 0.044 µV vs MMN RMS 2.94 µV (**≈1.5 %**) | |

The final ERP barely moves because, in this workflow, the bad-sample mask is
*redundant with robust averaging*: the robust weights already down-weight the
outlying samples the mask was supposed to remove, whether or not the mask lands
on them. Only 84–94 of 600 trials carried any detected artefact, and passive-
oddball blinks are not time-locked to the deviants, so the misplaced exclusions
do not bias the average systematically.

## Where the defect *does* change results
`removebad` exists only inside the robust-averaging options, so that consumer
is always cushioned as above. The exposure that is not cushioned:

- **Bad-channel / bad-trial classification in mark mode** (`spm_eeg_artefact`
  line ~150 thresholds the *fraction* of bad samples per channel): the
  truncation at epoch edges lowers that fraction (7 584 vs 9 017 samples here,
  −16 %), so channels near `badchanthresh` are classified differently.
- Consumers that trust the mask directly on epoched data (`spm_eeg_cfc`
  weighting, `spm_eeg_firstlevel`, TF robust averaging with removebad).
- **Not** affected: continuous data (`timeOnset = 0`, e.g. DAiSS `bf_features_contcov`
  on continuous recordings) and the default `'reject'` artefact mode, which
  never calls `badsamples`.

**Reach correction relative to the project's Tier-1 write-up:** the defect fires
only in `'mark'` mode (a documented, tutorial-taught workflow, but not the
default `'reject'` mode), and its downstream effect on a robust average is
small. It remains a correct, merged fix — but "high priority" was earned by the
mask-level corruption and by silent misclassification, not by large ERP changes
on the canonical pipeline.
