# HTSeq upstream filing kit

Default branch of `htseq/htseq`: **`main`**.

_Prepared 2026-09-03 against `htseq/htseq` `main` @ `7672321` (2026-02-04, version
string 2.1.2). **Nothing has been filed, pushed or posted.** The two fix branches
exist only as local git worktrees of the audit clone; the `git am`-able patches are in
this directory:_

| branch (local) | commit | patch | finding |
|---|---|---|---|
| `fix/unmapped-mate-minaqual` | `620b7e4` | `0001-Apply-the-a-MAPQ-cutoff-to-aligned-mates-only-in-hts.patch` | HC2 |
| `fix/bam-reader-interval-offset` | `32035b6` | `0002-Fix-BAM_Reader-iv-fetching-from-iv.start-1-instead-o.patch` | HC1 |

Both patches apply cleanly on `7672321` (`git apply --check`) and are independent of
each other (they touch different files, except that both add a "Version 2.1.3 /
Unreleased" section at the top of `doc/history.rst`, which conflicts trivially when
both are applied).


## Fork branches (pushed 2026-09-03)

Each branch is one commit on top of `7672321` (`main`) in the fork
[cindykrafft/htseq](https://github.com/cindykrafft/htseq); PR compare URLs use
`https://github.com/<upstream>/compare/main...cindykrafft:htseq:<branch>`.

| branch | commit | patch |
|---|---|---|
| [`fix/unmapped-mate-minaqual`](https://github.com/cindykrafft/htseq/tree/fix/unmapped-mate-minaqual) | `de52947` | 0001 (HC2) |
| [`fix/bam-reader-interval-offset`](https://github.com/cindykrafft/htseq/tree/fix/bam-reader-interval-offset) | `9ba5be1` | 0002 (HC1) |

## What was read before preparing this (step 4 of the method)

- No `CONTRIBUTING.md` in the repository. `doc/contrib.rst` ("Contributing"): source on
  GitHub, Python 3 + Cython + SWIG (C++ `step_vector`), build with `setup.py`, test with
  `./test.sh` (`pytest test`; `-o` restricts to `test/test_htseq-count.py`; `-d` runs
  the doctests in `doc/*.rst`), docs with Sphinx. It says nothing about branches, PR
  form, tests-with-fixes or changelog entries. Shaped the kit: each patch carries a
  pytest test in the module that already covers the touched code, and both were run
  with the project's own `pytest test/...` invocation.
- `.github/ISSUE_TEMPLATE/bug_report.md`: title prefix `[BUG]`; fields **Software
  versions** (HTSeq, Python, OS, aligner), **Describe the bug**, **Minimal example
  showing the bug** ("Attach BAM, GTF, or other files needed ... smaller than 5MB"),
  **To Reproduce** ("paste the exact command line you ran"). The two `issue-hc*.md`
  texts use those headings in that order; each example script writes its own BAM and
  GTF (three records / one line), so nothing needs to be attached, and the exact
  command line is given. There is no PR template, no `config.yml`, no discussions
  link, no code of conduct, no pinned policy issue.
- `.github/workflows/ci.yml`, `.ci_test.sh`, `test.sh`: CI builds wheels for Python
  3.10–3.13 and runs `pytest test` and the rst doctests. No linter (no ruff/flake8/black
  configuration anywhere in the repository), so none was run; the changed lines follow
  the surrounding style (4-space indentation, the multi-line `if (...) or (...)`
  layout of the original).
- `doc/history.rst`: the changelog, one section per release ("Version x.y.z", a date
  line, a one-line characterisation, bullets). It stops at 2.0.9 (2024-09-12) although
  2.0.9 → 2.1.2 has been released, so the exact convention for the next entry is the
  maintainer's call; each patch adds a "Version 2.1.3 / Unreleased / Bugfix release:"
  section with one bullet in the file's voice.
- `doc/htseqcount.rst` (the options page and FAQ, in particular "*What happened if the
  mate of an aligned read is not aligned?*") and `doc/tutorials/tss.rst`
  (`sortedbamfile[window]`) as the statements of intended behaviour the two findings
  are measured against; `README.md` (cite the 2022 Bioinformatics paper).
- Issue tracker searched 2026-09-03 (semantic search over `htseq/htseq` issues, several
  phrasings each): no prior report of HC2 (nearest: #99 "Mate records missing" warning
  on STAR data, closed; #80 mate-not-found error, closed; #14 ambiguous mate pairing,
  closed; #96 meaning of the special counters, closed; #106 multimappers with
  `--nonunique all`, open) or of HC1 (nearest: #18 `-r pos`, #77 "Count=0; but reads is
  detected", #66 paired-end counts, all closed). #94 (open) asks what
  `--secondary-alignments score/ignore` mean — the place to mention N3 if it is ever
  raised. Neither of the two findings has a matching prior issue, so both are drafted
  as new issues.
- Matthew Rocklin's "Craft Minimal Bug Reports" as summarised in the audit brief: each
  issue text carries a script that writes its own synthetic data, has no line that is
  not needed to reproduce, ends in an assertion, states expected vs got with the
  complete traceback, and says what shrinking revealed (HC2: only the presence of the
  unmapped record and `-a > 0` matter; HC1: independent of strand, read and window
  length). The scripts are `mcve_hc*.py`; `mcve_outputs.txt` is their captured output
  on `main` and on the 2.1.2 wheel.

## Contents

| file | what |
|---|---|
| `issue-hc2-unmapped-mate-minaqual.md` | bug report: pair with an unmapped mate in the file is `__too_low_aQual` under the default `-a` (template fields, MCVE, cause, fix) |
| `issue-hc1-bam-reader-window.md` | bug report: `BAM_Reader[iv]` fetches from `iv.start + 1` |
| `mcve_hc2_unmapped_mate.py`, `mcve_hc1_bam_reader_window.py`, `mcve_outputs.txt` | the reproductions embedded in the issues, and their output on `main` and 2.1.2 |
| `0001-Apply-the-a-MAPQ-cutoff-to-aligned-mates-only-in-hts.patch` | HC2 fix in `count_features_per_file.py` and `count_with_barcodes.py` + test + history entry |
| `0002-Fix-BAM_Reader-iv-fetching-from-iv.start-1-instead-o.patch` | HC1 fix in `HTSeq/__init__.py` + test + history entry |
| `pr-bodies.md` | PR titles and bodies (`### PR n — branch — "title"`), `#NNN` placeholders |

## Verification status of the patches

Each branch was installed editable into its own Python 3.12 venv (Cython + SWIG build)
and the project's own tests were run from the repository root, as `test.sh` does. The
"new test on unmodified `main`" column is the new test function copied into the
unmodified checkout.

| patch | new test on unmodified `main` | touched test modules with patch | harness under patch |
|---|---|---|---|
| 0001 (HC2) | `test/test_htseq-count.py::HTSeqCount::test_pair_with_unmapped_mate_is_counted`: **failed** (`'2' != '3'`) | `test/test_htseq-count.py test/test_parsers.py`: 41 passed, 5 skipped (skips need loompy/anndata) | `../verify/hc2_unmapped_mate_minaqual.patched.out`: all 2,000 pairs count, `__too_low_aQual` 0 in every setting |
| 0002 (HC1) | `test/test_parsers.py::test_bam_reader_getitem_window`: **failed** (`['inside', 'last_base'] == ['covers_base_100', ...]`) | `test/test_parsers.py test/test_genomic.py`: 20 passed, 1 skipped (skip needs pyBigWig) | `../verify/hc1_bam_reader_interval_offset.patched.out`: 0 of 300 windows miss a record |

Unmodified `main`, the same three modules together: 48 passed, 6 skipped. No linter is
configured in the project.

## Version scope (executed, `../verify/hc*_*.v*.out`)

| finding | present (executed) | present (by reading) | absent |
|---|---|---|---|
| HC2 | 0.11.2, 0.12.4, 0.13.5, 2.1.2, `main` | 0.9.1 (`python3/HTSeq/scripts/count.py:236-237`) | — |
| HC1 | 0.11.2, 0.12.4, 0.13.5, 2.1.2, `main` | 0.9.1 (`python3/HTSeq/__init__.py:1049`) | — |

0.9.1 and 0.6.1 (the cohort's other most-cited versions) were not built on Python 3.12.

## Order of operations

1. Open the HC2 issue, then the HC1 issue, from the texts above (paste the MCVE output
   from a fresh run).
2. Push each branch to a fork, `git am` the patch onto a fresh `main`, replace `#NNN`
   in the PR body with the issue number, open PR 1 (HC2) and PR 2 (HC1). If the
   maintainer prefers the history entry folded into the next release's section, amend.
3. Record issue and PR numbers, and every maintainer response, in `../README.md` and
   in the top-level status table.
