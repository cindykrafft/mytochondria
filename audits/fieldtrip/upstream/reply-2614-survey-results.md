Title: (comment on #2614) Octave survey results, three FieldTrip-side fixes, FAQ PR

<!-- Reply to schoffelen's 2026-09-16 comment on #2614 (FAQ as a website PR: yes; adaptive weighting: leave it; Octave survey: "the proof of the pudding is in the eating"). Supersedes reply-2614-faq-octave.md. Before posting: (1) open the fieldtrip/website PR from the console card and put its number in place of NNN; (2) open issue FT17 (issue-ft17-external-stats-not-added.md) and the PR (pr-ft17-octave-compat.md) and put their numbers in place of MMMM and PPPP; or post this first with the last paragraph adjusted. The numbers come from audits/fieldtrip/verify/octave_survey/README.md. -->

Thanks. The FAQ is now a pull request on the website repository, fieldtrip/website#NNN (`faq/spectral/dpss_without_toolbox.md`); edit freely. On the adaptive weighting I will leave it as you say.

**Octave survey.** Every test function marked `DATA no` (471 of them), each in a fresh GNU Octave 8.4.0 process (Ubuntu package, `statistics` and `signal` packages loaded, no MEX files compiled, no display), on master cfdad9b, with a time limit of twice the test's `WALLTIME`. Runner and per-test results: https://github.com/cindykrafft/mytochondria/tree/main/audits/fieldtrip/verify/octave_survey.

| | master | after three fixes |
|---|---|---|
| pass | 191 (41 %) | 286 (61 %) |
| `external/stats` not on the path, `nanmean` undefined | 81 | 0 |
| `compat/octave` `startsWith`/`endsWith`/`contains` with a cell array of patterns | 77 | 0 |
| MATLAB-only function or signature (`pad`, `strip`, `table`, `save -nocompression`, `round(x,n)`, ...) | 40 | 58 |
| MEX file not compiled for Octave (`plgndr`, `meg_leadfield1`, `spm_bwlabel`, `mat2file`, ...) | 30 | 51 |
| graphics under the gnuplot toolkit | 18 | 31 |
| a real difference inside FieldTrip code, to look at one by one | 13 | 19 |
| OpenMEEG / dipoli / xunit / MOxUnit not installed | 10 | 10 |
| `dpss_hack` called with two outputs (this issue) | 8 | 13 |
| loads a Donders file despite `DATA no`; one timeout | 3 | 3 |

The right column grows for the environmental rows because the fixes let tests run further before they stop at the next cause.

**The two biggest causes are FieldTrip's own, and one of them is a regression that affects MATLAB too.**

1. Since 55ee593 (2026-09-15) `ft_platform_supports('stats')` raises `'exclude_mfiles' undefined` (the commit removed the variable's definition but kept its use). `ft_defaults` calls it inside a `try`, so the error is silent and `external/stats` is never added to the path: without the Statistics Toolbox, or under Octave, `nanmean`, `nanstd`, `nansum` and the rest are undefined, and `test_external_stats` fails on master. One-line fix (pass `{}`, as the `images` and `signal` cases do). Filed separately as #MMMM since it is not Octave-specific.
2. `compat/octave/startsWith.m`, `endsWith.m` and `contains.m` pass a cell array of patterns straight to `strncmp`/`strfind`, which under Octave errors with "nonconformant cell arrays" when the sizes differ and returns one value per pattern when they happen to agree; `ft_senstype` (`startsWith(sens.label, {'L', 'R'}) & endsWith(sens.label, {'bx', 'by', 'bz'})`) and `ft_checkdata` call them this way. Looping over the patterns fixes all 77.
3. Behind those two: `ft_fetch_data` declares its name-value options with `addOptional`, which Octave's `inputParser` assigns positionally, so the string `'endsample'` ends up in `istrue(allowoverlap)` (10 tests). `addParameter` fixes it, in `utilities/` and the identical `fileio/private/` copy.

The three are on PR #PPPP (branch `fix/octave-compat-survey`); the 168 tests they touch were re-run on it and pass or stop at an environmental cause.

**What remains** is what the FAQ page should say: the MEX files can be built for Octave (`mkoctfile --mex`; not done here), about a dozen small MATLAB-only functions cover the next 58 tests (`pad` and `strip` alone 20), the plotting functions are where the MATLAB dependence is real, and the 13 `dpss_hack` failures are this issue, i.e. `cfg.taper = 'hanning'` or `'sine'` under Octave. The 19 "real difference" tests (`ft_progress`'s `fprintf` format, `ft_plot_vector` concatenating a scalar with an empty column, `remove_double_vertices` on an empty `unique` result, a non-zero imaginary part at the Nyquist bin in `test_issue2265`, four `isequal` assertions) are listed in the results file; I have not gone into them.

If you want it, I can turn the paragraph above into a PR on the Octave FAQ page (`faq/matlab/octave.md`), replacing the "we don't have precise details on what works and what not" sentence with the table.
