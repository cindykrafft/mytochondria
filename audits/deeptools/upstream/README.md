# deepTools upstream filing kit

**Default branch: `master`** (`deeptools/deepTools`; the remote has no `develop` branch —
the last one was merged as PR #1356 on 2025-01-20 and deleted — so the fix branches are
cut from `master`; a `4.0.0` branch exists and was not audited).

_Prepared 2026-09-03 against `deeptools/deepTools` `master` @ `ea0f68bb` (2025-01-20,
version 3.5.6 = the `3.5.6` tag = PyPI's latest release). **Nothing has been filed.** The
seven fix branches exist only in the local clone; the `git am`-able patches are in this
directory:_

| branch | commit | patch | finding |
|---|---|---|---|
| `fix/bamcompare-skipzerooverzero-coordinates` | `c5675968` | 0001 | DT1 (comment for #1108/#1130) |
| `fix/plotpca-log2-rowcenter` | `2b6ab898` | 0002 | DT2 |
| `fix/plotcorrelation-mad-outliers` | `fd3b0e37` | 0003 | DT3 |
| `fix/mnase-odd-fragment-centre` | `ca5637f9` | 0004 | DT4 (comment for #1118) |
| `fix/ignoreduplicates-scale-factor` | `7f30bc8f` | 0005 | DT7 |
| `fix/multibigwigsummary-exact-stats` | `e7131b02` | 0006 | DT8 |
| `fix/sumcoverage-partial-bins` | `ffedd888` | 0007 | DT9 |

DT5 (BPM = CPM) and DT6 (smoothing at chunk edges) have issue texts but no patch: DT5 is
a code-or-documentation decision for the maintainers, DT6 needs overlapping chunk reads.


## Fork branches (pushed 2026-09-03)

Each branch is one commit on top of `ea0f68bb` (`master`) in the fork
[cindykrafft/deepTools](https://github.com/cindykrafft/deepTools); PR compare URLs use
`https://github.com/<upstream>/compare/master...cindykrafft:deepTools:<branch>`.

| branch | commit | patch |
|---|---|---|
| [`fix/bamcompare-skipzerooverzero-coordinates`](https://github.com/cindykrafft/deepTools/tree/fix/bamcompare-skipzerooverzero-coordinates) | `8710337` | 0001 (DT1) |
| [`fix/plotpca-log2-rowcenter`](https://github.com/cindykrafft/deepTools/tree/fix/plotpca-log2-rowcenter) | `fb40d15` | 0002 (DT2) |
| [`fix/plotcorrelation-mad-outliers`](https://github.com/cindykrafft/deepTools/tree/fix/plotcorrelation-mad-outliers) | `66471cd` | 0003 (DT3) |
| [`fix/mnase-odd-fragment-centre`](https://github.com/cindykrafft/deepTools/tree/fix/mnase-odd-fragment-centre) | `4593dc1` | 0004 (DT4) |
| [`fix/ignoreduplicates-scale-factor`](https://github.com/cindykrafft/deepTools/tree/fix/ignoreduplicates-scale-factor) | `5326074` | 0005 (DT7) |
| [`fix/multibigwigsummary-exact-stats`](https://github.com/cindykrafft/deepTools/tree/fix/multibigwigsummary-exact-stats) | `572d041` | 0006 (DT8) |
| [`fix/sumcoverage-partial-bins`](https://github.com/cindykrafft/deepTools/tree/fix/sumcoverage-partial-bins) | `70a0b1e` | 0007 (DT9) |

## What was read before preparing this (step 4 of the method)

- `.github/CONTRIBUTING.md`: fork; "check out a feature or bug branch"; feature work on
  the `develop` branch (gone from the remote — bug fixes here are cut from `master`);
  update README when needed; PR with a description; tests passing; branch mergeable;
  GitHub Actions passing. No changelog rule, no code-style statement beyond CI.
- `.github/ISSUE_TEMPLATE.md`: a four-item markdown checklist — search first and link
  the prior issue; paste `deeptools --version` and `python --version`; paste the full
  command; paste the output. Every `issue-dt*.md` answers those four items in that
  order, then gives cause, minimal reproduction, output, fix. It is a markdown template,
  not a YAML form, so there are no bold form-field headings.
- `.github/PULL_REQUEST_TEMPLATE.md`: four checkboxes (new feature / bugfix /
  documentation / galaxy wrapper); answered in every body in `pr-bodies.md`.
- `.github/workflows/test.yml`: CI runs `flake8 . --exclude=.venv,.build,build
  --ignore=E501,F403,E402,F999,F405,E722,W504,W605` and `pytest -v` on Python 3.9–3.12,
  and fails a PR to `master` whose `pyproject.toml` version does not match
  `galaxy/wrapper/deepTools_macros.xml` (the patches do not touch the version).
  `flake8` with exactly those options was run on every changed file of every patch.
- `CHANGES.txt`: free-form bullets under a version heading; the top heading is 3.5.5
  (3.5.6 has no entry). Each patch adds one bullet under a new `unreleased` heading;
  the bullets conflict textually when several patches are applied together, nothing
  else does.
- `docs/content/tools/*.rst` and the `--normalizeUsing`, `--MNase`, `--removeOutliers`,
  `--smoothLength`, `--exactScaling` help texts in `parserCommon.py`,
  `bamCoverage.py`, `plotCorrelation.py` as the statement of intended behaviour the
  findings are measured against.
- `pyproject.toml`: `pyBigWig >= 0.2.1` (the `exact` keyword patch 0006 uses needs
  ≥ 0.3.2 — flagged in the PR body); tests are plain pytest under `deeptools/test/`,
  doctests in the modules (run with `--doctest-modules`).
- No pinned policy issue, no discussions link, no code of conduct, no security policy.
- Issue tracker searched 2026-09-03 with several phrasings per finding
  (`mcp__github__search_issues`, 7 + 3 queries): **DT1 is #1108 (2021-12-04) and
  #1130 (2022-03-22), both open, no maintainer reply**; **DT4 is #1118 (2022-01-27),
  open, no reply**; nothing for DT2 (nearest #1215, #496), DT3 (nearest #9, #1406),
  DT5 (nearest #1311, #1228), DT6 (nearest #99, #1144), DT7 (nearest #309 closed 2016,
  #5), DT8 (nearest #1296, #1270, #1139), DT9 (none). N1 is #1030 (open, 3 comments
  not readable from here).
- Matthew Rocklin's "Craft Minimal Bug Reports" as summarised in the audit brief: each
  issue text carries a script that makes its own data, has no line that is not needed,
  ends in an assertion, quotes the complete traceback, states expected vs got and says
  what shrinking revealed. The scripts are `mcve_dt*.py`; `mcve_outputs.txt` is their
  captured output on 3.5.6 (master) and on 3.3.1, every one failing its assertion on
  both.

The two findings with open issues (DT1, DT4) are drafted as comments for those threads,
not as new issues, per the brief; their patches close the existing numbers.

## Contents

| file | what |
|---|---|
| `issue-dt1-skipzerooverzero-coordinates.md` | comment for #1108/#1130: cause, MCVE, fix |
| `issue-dt2-plotpca-log2-rowcenter.md` | bug report: `--log2` inert, `--rowCenter` inert at default `--ntop` |
| `issue-dt3-removeoutliers-mad.md` | bug report: median(\|x\|) instead of MAD |
| `issue-dt4-mnase-four-bases.md` | comment for #1118: true division, one-token fix |
| `issue-dt5-bpm-is-cpm.md` | bug report: BPM track is the CPM track; two possible fixes, no patch |
| `issue-dt6-smoothlength-chunk-edges.md` | bug report: smoothing truncated at chunk edges; no patch |
| `issue-dt7-ignoreduplicates-denominator.md` | bug report: `--ignoreDuplicates` alone not in the normalisation denominator |
| `issue-dt8-multibigwigsummary-zoom.md` | bug report: zoom-level summaries instead of bin means |
| `issue-dt9-fingerprint-partial-bins.md` | bug report: whole tile credited to a fragment's last bin (step = bin size) |
| `mcve_dt1_*.py` … `mcve_dt9_*.py`, `mcve_outputs.txt` | the reproductions embedded in the issues and their output on 3.5.6 and 3.3.1 |
| `0001-*.patch` … `0007-*.patch` | fix + regression test + `CHANGES.txt` bullet, `git am`-able on `ea0f68bb` |
| `pr-bodies.md` | PR titles and bodies in the template's checkbox form |
| `test-runs.txt` | the pytest / doctest / flake8 numbers below, as captured |

## Verification status of the patches (`test-runs.txt`)

Master installed editable into a Python 3.12 venv (numpy 2.5.2, pysam 0.24.0,
pyBigWig 0.3.25, pytest, flake8). Unmodified `master`: the four test modules the
patches touch pass (56 passed); the full suite is **99 passed, 1 failed** —
`test_plotCoverage.py::test_plotCoverage_default`, a pre-existing failure unrelated to
the patches (it fails identically on every branch); `flake8` with the project's options
reports 14 findings on `master`, none in the files the patches touch.

| patch | new test(s) on unmodified `master` | touched modules with the patch | doctests of the changed module | full suite with the patch | flake8 on changed files |
|---|---|---|---|---|---|
| 0001 (DT1) | `test_bam_compare_ZoverZ_interior_bins`: **1 failed** | 54 passed | `writeBedGraph.py`: 2 passed | 100 passed + the pre-existing failure | 0 |
| 0002 (DT2) | `test_plotPCA_log2_and_rowCenter_change_the_result`: **1 failed** | 54 passed | `correlation.py`: 1 passed | 100 + 1 pre-existing | 0 |
| 0003 (DT3) | `test_get_outlier_indices_uses_median_absolute_deviation`: **1 failed** | 54 passed | 1 passed | 100 + 1 pre-existing | 0 |
| 0004 (DT4) | `test_bam_coverage_MNase_odd_fragment_length`: **1 failed** | 54 passed | (none in module) | 100 + 1 pre-existing | 0 |
| 0005 (DT7) | `test_get_num_kept_reads_ignore_duplicates`: **1 failed** | 54 passed | (none) | 100 + 1 pre-existing | 0 |
| 0006 (DT8) | `test_multiBigwigSummary_bins_exact_mean` + updated `test_multiBigwigSummary_gtf`: **2 failed** | 54 passed | `getScorePerBigWigBin.py`: 3 passed | 100 + 1 pre-existing | 0 |
| 0007 (DT9) | `test_sum_coverage_partial_bins`: **1 failed** | 54 passed | `sumCoveragePerBin.py`: 1 passed | 100 + 1 pre-existing | 0 |

Each harness in `../verify/` was written against the shipped code; the patches were
verified through the project's tests above rather than by re-running the harnesses
under them.

## Version scope (executed, `../verify/*.v3.5.1.out`, `*.v3.3.1.out`)

| finding | affected | unaffected |
|---|---|---|
| DT1 | 3.3.1, 3.5.1, 3.5.6/master | — (option introduced in 3.2.1, by reading) |
| DT2 | 3.3.1, 3.5.1, master | — (options introduced in 3.2.0, by reading) |
| DT3 | 3.3.1, 3.5.1, master | — (line dates from 2.0.0, by reading) |
| DT4 | 3.3.1, 3.5.1, master | — (Python 3 builds since the 2.x port, by reading) |
| DT5 | 3.3.1, 3.5.1, master | — (BPM introduced in 3.0.0, by reading) |
| DT6 | 3.3.1, 3.5.1, master | — |
| DT7 | 3.3.1, 3.5.1, master | — (sampler introduced in 3.0.0, by reading) |
| DT8 | 3.3.1, 3.5.1, master | — (pyBigWig default in every version) |
| DT9 | 3.3.1, 3.5.1, master | — |

The 3.5.1 wheel needs `matplotlib < 3.9` (`cm.register_cmap`) and, for plotFingerprint,
`numpy < 1.24` (`np.int`) on Python 3.11; the 3.3.1 sdist likewise for plotFingerprint.
Those are packaging incompatibilities of the old releases with current numpy/matplotlib,
not findings.

## Order of operations

1. Post the DT1 text as a comment on #1108 (link #1130) and the DT4 text on #1118; open
   PRs 1 and 4 from the patches, referencing those numbers.
2. Open the DT7, DT8, DT2, DT3, DT9 issues (in that order of impact), then PRs 5, 6, 2,
   3, 7 with the issue numbers filled into `pr-bodies.md` and the `CHANGES.txt` bullets.
3. Open DT5 and DT6 as issues only; offer a documentation patch for DT5 if the
   maintainers prefer that route.
4. Record issue and PR numbers, and every maintainer response, in `../README.md` and in
   the top-level status table.
