Title: `external/stats` is no longer added to the path since 55ee593: `nanmean` etc. undefined without the Statistics Toolbox (and under Octave); `test_external_stats` fails on master

<!-- fieldtrip/fieldtrip has no issue template. Found by the Octave test survey asked for on #2614 (81 of 472 DATA-no tests fail on it); the regression is one week old and hits MATLAB without the Statistics Toolbox as well, which is why it goes as its own issue rather than only a line in the survey comment. Verified by execution on master cfdad9b under Octave 8.4 (audits/fieldtrip/verify/octave_survey/): before the fix ft_platform_supports('stats') errors and external/stats is off the path; with the one-line fix it is on the path and nanmean works. Prior-report search: none (search "exclude_mfiles", "external/stats", "nanmean undefined" on 2026-09-22). -->

Since 55ee593 ("no need to exclude mfiles for stats, those are nowadays in stats/private", 2026-09-15) `ft_platform_supports('stats')` raises

```
error: 'exclude_mfiles' undefined near line 137, column 57
error: called from
    ft_platform_supports at line 137 column 10
```

because the commit removed the definition of `exclude_mfiles` but kept its use:

```matlab
  case 'stats'
    root_dir = fileparts(which('ft_defaults'));
    if ~isempty(root_dir)
      external_stats_dir = fullfile(root_dir, 'external', 'stats');
      tf = has_all_functions_in_dir(external_stats_dir, exclude_mfiles);   % <- undefined
```

`ft_defaults` calls it inside a `try` block (the one that decides whether to add `external/stats`), so the error is swallowed and the block ends before `addpath(external_stats)`. The consequence is that `external/stats` is never added to the path. With the MathWorks Statistics Toolbox installed nothing is visible, since the toolbox provides `nanmean` and friends anyway; without it (MATLAB without the toolbox, or GNU Octave, whose statistics package no longer implements `nanmean`) every function that uses `nanmean`, `nanstd`, `nansum`, `nanvar`, `nanmax` or `nanmin` fails with `'nanmean' undefined`. `test_external_stats` exercises exactly this (`restoredefaultpath`, `ft_defaults`, then `exist('nanmean')`) and fails on master:

```
>> test_external_stats
error: assert (exist (filelist {k}, 'file') == 2 || exist (filelist {k}, 'file') == 3) failed
```

To see it directly, on master with no Statistics Toolbox (or in Octave):

```matlab
restoredefaultpath; addpath('/path/to/fieldtrip'); ft_defaults
ft_platform_supports('stats')     % error: 'exclude_mfiles' undefined
which nanmean                     % empty
nanmean([1 NaN 3])                % 'nanmean' undefined
```

Expected: `ft_platform_supports('stats')` returns true, `external/stats` is on the path when the toolbox is not, and `nanmean([1 NaN 3])` is 2, as before 55ee593.

The fix is to pass an empty exclusion list, as the `images` and `signal` cases already do:

```matlab
      tf = has_all_functions_in_dir(external_stats_dir, {});
```

In the Octave survey you asked for on #2614 (every `DATA no` test function on Octave 8.4, results there shortly), this one line accounts for 81 of the 280 failures. PR follows, together with two small Octave-only fixes from the same survey (`compat/octave/startsWith.m`, `endsWith.m` and `contains.m` with a cell array of patterns; `ft_fetch_data` with `addParameter`).
