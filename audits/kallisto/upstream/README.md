# kallisto upstream filing kit

_Target branch: **`devel`** (README.md: "please make sure to request to merge into `devel` and NOT
`master`"). Prepared 2026-10-18 against `pachterlab/kallisto` `master` @ `4e9f29c` (v0.52.0, the current
release) and `devel` @ `34aba49` (`master` minus one usage-text commit). **Nothing filed.** The fix is a
single commit, `git am`-able from the patch here onto either branch. In the scratch clone it is `67b4269` on
`fix/bootstrap-threads-without-hdf5` (based on `master`) and `7e930af` on
`fix/bootstrap-threads-without-hdf5-devel` (the same patch applied onto `devel`; this is the branch to push).
**Fork needed: pachterlab/kallisto.**_

Filing tier (TRIAGE): **now** for KA1. It is a silent omission on the CMake default build with common
options: bootstraps are requested with threads and none are produced, while `run_info.json` claims they were.
The precedent is VCFtools VT1 (no output on the default build of a current toolchain), graded "file now".
Whether that counts as "changes a number that ends up in a paper" is the lead's call. KA2 is held: a
documented default and a design question, with a comment on the open #230 drafted. KA3 and KA5 are
duplicates/already reported. KA4 is held (`--bias` unsupported, #465). One filing in total, under the
two-filing cap.

## What was read before preparing this

- No `CONTRIBUTING.md`, no `CODE_OF_CONDUCT`, no issue or PR template, and no AI-contribution policy
  anywhere in the tree (`README.md`, `INSTALL.md`, `.github/`, which holds only `workflows/test.yml`,
  searched; `ext/` excluded). README: bugs to the GitHub issues page, usage questions to the
  kallisto-and-applications Google Group, PRs to `devel`.
- `.github/workflows/test.yml` runs only on `workflow_dispatch`: build with `-DBUILD_FUNCTESTING=ON`,
  install bustools, `make test` (`func_tests/runtests.sh`). The script was run here on `master`, the
  patched branch, and both with `-DUSE_HDF5=ON` (`test-runs.txt`). It stops at its first failure, and one
  existing d-list check fails on unpatched `master` too (bustools `d4d7a28`), so the runs use a copy that
  continues past failures.
- `git log`/`git show`: the `#ifdef USE_HDF5` around `BootstrapThreadPool` is present at v0.48.0
  (`main.cpp:3082-3084` there) and absent at v0.46.1. Commit `d0ac69b` (2025-11-17, in 0.52.0) fixed the
  `--bias` segfault (KA5).
- Packaging, as checked: bioconda `build.sh` uses `-DUSE_HDF5=ON`, Homebrew `-DUSE_HDF5=ON`, Debian
  `debian/rules` (0.51.1+dfsg-2) no HDF5 flag; `gen_release.sh` has `cmake -DLINK=static ..` (no HDF5),
  yet the 0.50+ release binaries carry HDF5 (executed).
- Issue tracker searched 2026-10-18 (eight `search_issues` phrasings, three `search_pull_requests`). The
  threads below were read in full from their public pages; see `dupcheck-2026-10-18.md`. **No prior report of
  KA1.** Nearest: #382 (open, 2023) and #277 (closed, 2020), both the no-`--plaintext` warning path on
  non-HDF5 builds; #353 (closed, 2022), where the maintainer recommends `--threads=12` with `-b 100`.
  KA2: #230 (open, 2019, unanswered) and #184. KA3: #151 and PR #260 (open since 2020, unreviewed). KA5 and
  the `--bias` policy: #465 ("The bias option is no longer supported", Yenaled, 2024-10-30).
- `site/audits.json` is not consulted from this session. No `cindykrafft/kallisto` fork is known, so the
  `upstream-declines-ai-contributions` topic cannot apply yet.

## Contents

| file | what |
|---|---|
| `issue-ka1-bootstraps-skipped-with-threads-without-hdf5.md` | bug report: the `#ifdef` in `main.cpp`, reproduction on the repository's `test/` data (`-t 1` writes 10 tables, `-t 4` none, `run_info` says 10), affected builds, the fix |
| `0001-Run-multi-threaded-bootstraps-in-builds-without-HDF5.patch` | KA1 fix (`src/main.cpp`, construct the pool in every build) + a functional test in `func_tests/runtests.sh` |
| `pr-bodies.md` | PR title and body (§ PR 1) |
| `repro-ka1.txt` | the reproduction log the issue quotes, plus the patched run (tables identical to `-t 1`) |
| `test-runs.txt` | `func_tests/runtests.sh` on master and patched, with and without HDF5 |
| `dupcheck-2026-10-18.md` | queries, candidates, verdicts |
| `comment-ka2-230.md` | **held** comment for #230 (KA2) |

## Verification status of the patch

| branch | commit | harness on the patched build | project tests |
|---|---|---|---|
| `fix/bootstrap-threads-without-hdf5` (on `master`) | `67b4269` | `../verify/t7_threads_bootstrap.patched.out`: 8/8 tables with `-t 2` and `-t 4`, identical to `-t 1` (0/8 on master); `t1`/`t2`/`t4` outputs identical to master's; `-DUSE_HDF5=ON`: `t7…patched-hdf5.out`, `t9_h5.patched-hdf5.out` pass | `test-runs.txt`: 59 OK / 1 pre-existing failure on both builds (master: 58 OK / 2, the new test failing without HDF5) |
| `fix/bootstrap-threads-without-hdf5-devel` (on `devel`) | `7e930af` | `../verify/t7_threads_bootstrap.patched-devel.out` | `test-runs.txt`, last section |

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| KA1 | master/0.52.0, v0.51.1, v0.50.1 built with default CMake; 0.48.0 release binary | 0.46.1 binary; 0.50.1/0.51.1/0.52.0 release binaries (HDF5); `-DUSE_HDF5=ON`; patched |
| KA2 | all eight builds 0.46.1–0.52.0 | `--single-overhang` |
| KA3, KA4 | 0.46.1, 0.48.0, 0.52.0 (0.50/0.51 crash first) | — |
| KA5 | v0.50.1, v0.51.1 | 0.46.1, 0.48.0, 0.52.0 |

## Order of operations

1. Fork `pachterlab/kallisto`; tell the session; push `fix/bootstrap-threads-without-hdf5` from the
   `devel`-based commit (`git am` the patch onto `devel`).
2. Open the KA1 issue from `issue-ka1-…md`, then the PR **against `devel`** with the body from
   `pr-bodies.md` § PR 1 (issue number in the first line).
3. KA2: only on the lead's go-ahead, re-read #230 in full and post `comment-ka2-230.md` there (a comment on an
   open issue, not counted against the cap).
4. Record issue/PR numbers and every maintainer response in `../README.md` and the top-level status table.
