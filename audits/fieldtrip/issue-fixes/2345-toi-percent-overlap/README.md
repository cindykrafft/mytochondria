# fieldtrip/fieldtrip #2345 — `cfg.toi = 'NN%'` in `ft_freqanalysis` sets the step, not the overlap

**Issue:** [#2345 "% overlap actually defines % step in mtmconvol"](https://github.com/fieldtrip/fieldtrip/issues/2345),
opened 2023-11-19 by NirOfir, no labels, 0 comments, **no assignee** (checked via the API `assignee` field on 2026-09-03; the assigned open issues are #2440, #2277, #2245, #2106, #1859, #1858, #1855, #1705, #1598, #1252, #896, #856, #853, none of them a candidate here), no linked PR (checked the PR search for
"2345" and for "overlap toi freqanalysis": the only hit is the merged 2016 PR #193 that introduced the option).

**Reporter's claim:** for `cfg.method = 'mtmconvol'`, a percentage in `cfg.toi` is documented as the
degree of overlap between the shortest time windows, but `ft_freqanalysis.m` uses it as the step between
time points, so a larger percentage gives *fewer* time points; the proposed fix is `overlap = 1 - overlap`.

## Diagnosis (master @ 9c4a3af, 2026-09-03)

`ft_freqanalysis.m:118-122` documents the option: "the percentage specifies the degree of overlap between
the shortest time windows from cfg.t_ftimwin". `ft_freqanalysis.m:332-335` implements it as

```matlab
elseif strcmp(cfg.toi(end), '%') % percent overlap between smallest time windows
  overlap = str2double(cfg.toi(1:(end-1)))/100;
  cfg.toi = linspace(begtim, endtim, round((endtim-begtim) ./ (overlap * min(cfg.t_ftimwin))) + 1);
```

The denominator `overlap * min(cfg.t_ftimwin)` is the *step*, so the percentage is the fraction of the
window that is stepped over, and the overlap is `100 - NN` %. `'50%'` is the only value for which the two
coincide, which is why the tutorials (which use `'50%'`) never showed it. Also, `'0%'` requests a step of 0
and `linspace` is asked for an infinite number of points (on Octave "out of memory"; the same on MATLAB).

## Fix (branch `fix/issue-2345-toi-percent-overlap`, commit 899e004, `0001-*.patch`)

`ft_freqanalysis.m`: the step is `(1-overlap) * min(cfg.t_ftimwin)`; a percentage that is not finite, is
negative, or is 100 or more (a step of zero or less) raises `ft_error`. The comment is corrected. 7 lines
added, 3 removed. New `test/test_issue2345.m` (`DATA no`, synthetic data; copy in this directory).

## Reproduction (`repro.m`, GNU Octave 8.4, `pkg load statistics signal`, audit shims on the path)

2 trials, 1 channel, 200 Hz, 0–2 s; `mtmconvol`, hanning, `foi = 10`, `t_ftimwin = 0.5`.

Before (`repro.before.out`):
```
 cfg.toi    ntime       step (s)        overlap
     10%       41         0.0500          90.0%
     25%       17         0.1250          75.0%
     50%        9         0.2500          50.0%
     75%        6         0.4000          20.0%
     90%        5         0.5000           0.0%
```
After (`repro.after.out`):
```
 cfg.toi    ntime       step (s)        overlap
     10%        5         0.5000           0.0%
     25%        6         0.4000          20.0%
     50%        9         0.2500          50.0%
     75%       17         0.1250          75.0%
     90%       41         0.0500          90.0%
```
(`overlap` is computed from the realised step; the 10 %/25 % rows show the rounding of `linspace`,
see caveats.)

Run with `FIELDTRIP=<checkout> FTSHIMS=../../verify/shims FTSHIMS2=../../verify/pull2610-octave octave-cli -q repro.m`.

## Tests

`run_ft_test.sh <tree> <test>` (the audit's Octave runner; run it from a directory other than the FieldTrip
root, whose `private/` directory confuses Octave's private-function lookup). The 14 data-free
`test/test_*.m` scripts that mention `mtmconvol`, plus the new test, on unpatched master and on the branch
(`tests_master.out`, `tests_branch.out`):

| | master | branch |
|---|---|---|
| `test_issue2345` (new) | FAIL: `cfg.toi = '10%' gave 81 time points, expected 10 for 10% overlap of a 0.25 s window` | PASS |
| pass on both | 7: `test_bug1677`, `test_bug2364`, `test_bug3214`, `test_bug3238`, `test_ft_crossfrequencyanalysis`, `test_issue1866`, `test_old_ft_freqanalysis` | same 7 |
| fail identically on both (Octave) | 7: `dpss` two-output signature (`test_ft_connectivityanalysis`, `test_pull1757`), `taylorwin` missing (`test_ft_specest_mtmconvol`), MATLAB-only `strncmp` on cells (`test_example_ssvep20220113`, `test_ft_selectdata`, `test_spm_ft_integration`), `sq_string` (`test_bug2440`) | same 7, same messages |

No existing test uses a percentage `cfg.toi`, so none changes.

**Linter:** FieldTrip's only lint step is codespell (`.github/workflows/codespell.yml`, paths `plotting utilities`).
codespell 2.4.3 with the repo's `.codespellrc`: nothing in `test_issue2345.m`; six pre-existing typos in
`ft_freqanalysis.m` on lines this patch does not touch (125, 192, 306, 775, 801, 1159). Not fixed here to
keep the diff to the issue.

## Candidates considered (86 open issues listed via the GitHub search API and github.com; bodies read for the ones below; comments cannot be read from this session, only their counts)

- **#2345** (chosen): documented option does the opposite of its help; reporter gave the reproduction and the
  one-line fix; 0 comments, 2.75 years unclaimed; synthetic data, no toolbox.
- **#2605 / #2343** `ft_defaults` toggles `external/signal` (and `external/stats`) on and off on alternate calls
  when a Signal toolbox licence exists but the toolbox is not installed (`ft_hastoolbox('signal')` counts
  `window`/`hanning` from `external/signal` itself, `ft_hastoolbox.m:307`, `ft_defaults.m:249-257`). Real, two
  reports (2023 and 2026, the 2023 one has 3 unread comments). Not chosen: reproducing it needs a shim for
  `license()`, and the fix is a design choice about how to tell the MathWorks toolbox from the bundled
  replacement, which the maintainers should make.
- **#2590** `ctf275_neighb` adjacency not left-right symmetric (maintainer's own note, "I don't know whether I
  want to escalate this"). Not chosen: the fix is editing a template `.mat`, a data decision, not code.
- **#1307** `minimumnormestimate` squares lambda only without prewhitening (19 comments, unreadable here).
  Not chosen: changes numbers of a published method and has a long discussion we cannot read.
- **#855** `ft_convert_unit` does not scale `dipole.dip.mom` (maintainer's TODO from 2018, 4 comments). Not
  chosen: whether `mom` is in A·m and how `ft_warp_apply` should rotate it is a design question.
- Others (#2318 BDF reader, #2131/#2277 data2bids, #2234 Windows network drive, #2421/#2143 GUI, #2571/#2576
  SPM-sync MEX and copilot notes) need data, hardware, or a platform we do not have, or are not reproducible bugs.

## Caveats

- Behaviour change: every percentage other than `'50%'` now yields a different time axis. A user who wrote
  `'90%'` and tolerated 10 % overlap will now get 90 % (a 9x denser axis). This is what the help promised,
  but the PR says so explicitly so the maintainers can decide whether to note it in the release notes.
- The realised overlap still differs from the requested one by the rounding in `linspace` (e.g. `'10%'` with a
  0.5 s window on 2 s of data rounds to a 0.5 s step). That rounding is pre-existing and shared with
  `cfg.toi = 'all'`; a `begtim:step:endtim` axis would be exact but would change the last time point, so it
  is left alone and mentioned in the PR.
- The test suite could only be run under Octave; MATLAB numerics were not exercised. The changed lines use
  only `str2double`, `isfinite`, `linspace` and `ft_error`.
- I could not read the (zero) issue comments; the body was sufficient.
