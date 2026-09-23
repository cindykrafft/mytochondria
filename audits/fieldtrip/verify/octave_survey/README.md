# FieldTrip test suite under GNU Octave: the survey asked for on #2614

Asked by schoffelen on #2614 (2026-09-07, confirmed 2026-09-16: "the proof of the pudding is in the
eating"): how much of FieldTrip's test suite runs on a recent Octave, as input for the website's
Octave FAQ page. Run on 2026-09-22.

## Setup

- FieldTrip `master` at cfdad9b (2026-09-18); GNU Octave 8.4.0 (Ubuntu 24.04 package) with the
  `statistics` 1.6 and `signal` 1.4.5 packages loaded; no MEX files compiled for Octave; no display
  (gnuplot toolkit, figures invisible); four cores, three tests at a time.
- Every test function in `test/` marked `% DATA no`: 471 of the 1040. Each runs in a fresh Octave
  process with `ft_defaults`, `external/signal/dpss_hack` on the path, and the same four shims used for
  the #2608 and #2610 test runs (`convertCharsToStrings`, `convertStringsToChars`, `isstring`,
  `istable`), with a time limit of twice the test's `% WALLTIME` (at least 2 min, at most 30 min).
  Runner: `../octave_survey.py`; outcome PASS, FAIL (first 300 characters of the error and the file and
  line it was raised in), TIMEOUT or CRASH.
- Failures were classified by the error message (`classify.py`, rules in the docstring), then the
  failing tests were re-run on a fix branch three times, each time fixing the dominant cause that
  turned out to be FieldTrip's own (`merge.py` combines the runs; a test's final outcome is its row in
  the latest run that includes it). Raw runner output: `octave_survey_*_raw.tsv`; classified:
  `results_master.tsv`, `results_final.tsv`, `classify_final.txt` (per-test lists by category).

## Result

| category | master cfdad9b | with branch `fix/octave-compat-survey` |
|---|---|---|
| pass | 191 (40.6 %) | 288 (61.1 %) |
| `external/stats` not on the path (`nanmean` undefined) | 81 (17.2 %) | 0 |
| `compat/octave` `startsWith`/`endsWith`/`contains` with cell patterns | 77 (16.3 %) | 0 |
| `ft_fetch_data` options parsed positionally by Octave's inputParser | (hidden behind the above) | 0 |
| MATLAB function or signature that Octave 8.4 does not have | 40 (8.5 %) | 58 (12.3 %) |
| MEX file not compiled for Octave | 30 (6.4 %) | 51 (10.8 %) |
| graphics (gnuplot toolkit, no display) | 18 (3.8 %) | 31 (6.6 %) |
| a real difference or failure inside FieldTrip code, to look at one by one | 13 (2.8 %) | 16 (3.4 %) |
| external binary or toolbox not installed (OpenMEEG, dipoli, xunit, MOxUnit, hbf) | 10 (2.1 %) | 10 (2.1 %) |
| `dpss_hack` called with two outputs (the #2614 problem) | 8 (1.7 %) | 13 (2.8 %) |
| loads a file from the Donders file system despite `DATA no` | 2 | 2 |
| timeout (`test_issue1184` at 30 min; on the branch also `test_bug2265`, which ran past 9 min once it got past `startsWith`) | 1 | 2 |

The counts in the right column grow for the environmental categories because the fixes let tests
run further before stopping at the next cause.

## The three FieldTrip-side causes (branch `fix/octave-compat-survey` on the fork, PR #2622, four commits)

1. **`external/stats` is never added to the path** (81 tests, and `test_external_stats` fails on master
   for the same reason). 55ee593 (2026-09-15) removed the definition of `exclude_mfiles` in
   `ft_platform_supports.m` but kept its use in the `'stats'` case, so `ft_platform_supports('stats')`
   raises `'exclude_mfiles' undefined`; `ft_defaults` calls it inside a `try`, swallows the error and
   leaves the block before `addpath(external_stats)`. Without the Statistics Toolbox (MATLAB) or under
   Octave, whose statistics package no longer implements `nanmean`, every function that uses
   `nanmean`/`nanstd`/`nansum`/`nanvar`/`nanmax`/`nanmin` is broken. A one-week-old regression that
   also hits MATLAB users; fix: pass `{}` as the `images` and `signal` cases do (4dfba5c).
2. **The Octave compat shims `startsWith`, `endsWith` and `contains` do not take a cell array of
   patterns** (77 tests). They pass the pattern straight to `strncmp`/`strfind`, which under Octave
   errors with "nonconformant cell arrays" / "cell arguments must have matching sizes" when the
   sizes differ, and returns one value per pattern instead of one per string when they happen to agree
   (`ft_senstype` line 444 then fails on `1x2 & 1x3`). `ft_senstype`, `ft_checkdata` and others call
   them with cell patterns. Octave 8.4 has its own `startsWith`/`endsWith` that handle this, but
   FieldTrip's shims shadow them (the self-removal in the shim relies on `which -all`, which Octave
   does not implement). Fix: loop over the patterns and OR the results (4dfba5c, 9ad3bfb).
3. **`ft_fetch_data` declares its name-value options with `addOptional`** (10 tests, visible only after
   1 and 2). Octave's `inputParser` assigns `addOptional` arguments positionally, so `'header'` lands in
   `header`, the header struct in `begsample`, and the string `'endsample'` reaches
   `istrue(allowoverlap)`. Fix: `addParameter`, in `utilities/ft_fetch_data.m` and its identical copies
   `fileio/private/ft_fetch_data.m` (ce18267) and `test/private/ft_fetch_data.m` (99b4c3c, added after the
   PR bot pointed at `test_ft_fetch_data` and `test_issue1292`, which stopped in that third copy with
   "NaN: dimensions must be scalars"; both pass with it).

Verified: the 81 + 77 + 10 tests were re-run on the branch; all pass or stop at a different,
environmental cause (`results_final.tsv`, column `run`).

## What remains, and what it says for the FAQ

- **MATLAB-only functions** (58): `pad` (11 tests, via `ft_read_atlas`/`ft_sourceparcellate` paths),
  `strip` (9), `table`/`array2table` (8), `save -nocompression` (4), `round(x, n)` (2), `ifft(x, [], dim)`
  (2), `var(x, w, dim)` with Octave's signature, `corr(x, y, 'type', ...)`, `envelope`, `taylorwin`,
  `parula`, `alphamap`, `clim`, `mle`, `split`, `checkcode`, `isequal` on cell arrays of cells, `buffer`
  with a non-integer, `audiowrite` `.oga`. Each is a small compat shim or an `if is_octave` branch;
  `pad` and `strip` alone would recover 20 tests.
- **MEX files** (51): `plgndr`, `meg_leadfield1`, `bem_Cii_lin`, `routlm`, `ptriproj`, `spm_bwlabel`,
  `mat2file`/`file2mat`, `spm_conv_vol`, `zstream`, `CalcMD5`, `spm_existfile`. These can be built for
  Octave with `mkoctfile --mex`; the survey did not, so this row is "not compiled here", not "cannot
  work". Forward modelling and the SPM-based volume functions are behind it.
- **Graphics** (31): `colormap` with a figure argument, `get(0, 'DefaultFigureColormap')`, `surface`
  with a colour array of another size, `patch` with `cdata`, `getframe`, `zoom`/`rotate3d` with outputs,
  `alphamap`, `isosurface`. The plotting functions are the MATLAB-specific part the FAQ already names.
- **Real differences to look at one by one** (16): `ft_progress` uses a `fprintf` format Octave rejects;
  `ft_plot_vector` concatenates a scalar with an empty column (`1x1 vs 151x0`); `remove_double_vertices`
  indexes with an empty result of `unique(..., 'rows')` (3 tests); `test_ft_checkdata` "time axis is wrong"; `test_warp`
  "rigidbody coregistration failed"; `test_issue2265` finds a non-zero imaginary part at the Nyquist
  bin (`< 100*eps` assertion); four `isequal` assertions (`test_bug3048`, `test_bug3229`,
  `test_ft_timelocksimulation`, `test_bug2593`) and three tests that check MATLAB-specific error
  messages or version strings.
- **`dpss_hack` with two outputs** (13): the #2614 problem itself. Under Octave with the `signal` package
  loaded there is still no `dpss`, so `ft_specest_mtmfft` reaches the hack and stops; these 13 tests are
  the ones the website FAQ (`cfg.taper = 'hanning'` or `'sine'`) is for.
- **External binaries and toolboxes** (10) and **data despite `DATA no`** (2): environment; `test_pull1138`
  and `test_tutorial_networkanalysis_eeg20220126` should probably say `DATA private`.

So on Octave 8.4 with the three fixes: 61 % of the data-free tests (288 of 471) pass as is, roughly 75 % would
with the MEX files compiled and the dozen small compat shims above, and the plotting functions are
where the MATLAB dependence is real.
