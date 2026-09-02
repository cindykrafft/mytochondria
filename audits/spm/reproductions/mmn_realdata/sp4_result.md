# SP4 real-data demonstration — `spm_eeg_downsample` stamped sampling rate

**Data:** SPM's own MMN tutorial dataset (`eeg_mmn/subject1.bdf`, Biosemi 128-ch,
512 Hz, 915 s; 480 standards / 120 deviants). **Code:** the actual SPM functions
executed in GNU Octave 8.4 (SPM MEX files rebuilt with `make PLATFORM=octave`;
FieldTrip's 24-bit BDF reader replaced by an equivalent pure-MATLAB decoder,
verified against MNE-Python's independent decode to 4 decimals).

## When the bug fires
`spm_eeg_downsample` defaults to `method='resample'` (exact rational resampler)
and silently falls back to `'fft'` (also exact) when the Signal Processing
Toolbox is absent — both stamp the correct rate. The defect fires only when the
user explicitly selects `'decimate'` or `'downsample'` **and** the requested
ratio is non-integer, because `ft_preproc_resample` then uses
`fac = round(Fold/Fnew)`.

## Real SPM run: 512 Hz → requested 200 Hz, `method='decimate'`
`fac = round(512/200) = 3`, so the data are really at 512/3 = **170.667 Hz**.

| version | on-screen "Resampling frequency" | **stamped** `fsample(D)` | last sample's reported time | true recording length |
|---|---|---|---|---|
| pre-fix (`530ec52`) | 170.7 Hz | **200.0000 Hz** | **780.795 s** | 914.994 s |
| merged (PR #165) | 170.7 Hz | 170.7000 Hz | 914.815 s | 914.994 s |

Pre-fix, SPM *prints* the right rate and *stores* the wrong one: the 915-second
recording is reported as 781 seconds long, and every time value derived from the
file is 14.7% too small. (The merged version stores the 0.1-Hz-rounded rate the
code always used for display, 170.7 vs 170.667 — a pre-existing 0.02% residual,
0.18 s over the recording, outside this fix's scope.)

## Downstream consequence on the MMN (Python transcription of the same arithmetic, `sp4_demo.py`)
Epoching -100..400 ms, 0.5-30 Hz, average reference; MMN = deviant − standard;
GFP peak on the true time axis at 275.4 ms (max channel C4, +61.9 µV).

| | reported MMN peak latency | error |
|---|---|---|
| pre-fix (200 Hz stamp) | **235.0 ms** | −40.4 ms |
| merged (170.667 Hz stamp) | 275.4 ms | 0 |

And every user-specified window is silently mis-cut under the wrong stamp:
a requested −100..400 ms epoch really covers −85..341 ms, the −100..0 ms
baseline really covers −85..0 ms, and a 100..250 ms MMN window really covers
85..213 ms of real time.
