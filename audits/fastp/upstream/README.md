# fastp upstream filing kit

_Prepared 2026-09-03 against `OpenGene/fastp` **default branch `master`** @
`dce5c40` (2026-09-01, version string 1.3.6). **Nothing has been filed and
nothing has been pushed.** The three fix branches exist only in the local clone;
each is one commit on top of `dce5c40`:_

| branch | commit | patch | finding |
|---|---|---|---|
| `fix/cut-window-trim-front` | `2373579` | 0001 | FP1 |
| `fix/known-adapter-truncation` | `4a8e832` | 0002 | FP2 |
| `fix/adapter-indel-offset` | `7b5579d` | 0003 | FP3 |

PR compare URLs will be
`https://github.com/OpenGene/fastp/compare/master...<fork>:<branch>`.


## Fork branches (pushed 2026-09-03)

Each branch is one commit on top of `dce5c40` (`master`) in the fork
[cindykrafft/fastp](https://github.com/cindykrafft/fastp); PR compare URLs use
`https://github.com/<upstream>/compare/master...cindykrafft:fastp:<branch>`.

| branch | commit | patch |
|---|---|---|
| [`fix/cut-window-trim-front`](https://github.com/cindykrafft/fastp/tree/fix/cut-window-trim-front) | `5de9fbd` | 0001 (FP1) |
| [`fix/known-adapter-truncation`](https://github.com/cindykrafft/fastp/tree/fix/known-adapter-truncation) | `91ef002` | 0002 (FP2) |
| [`fix/adapter-indel-offset`](https://github.com/cindykrafft/fastp/tree/fix/adapter-indel-offset) | `154a750` | 0003 (FP3) |

## What was read before preparing this (step 4 of the method)

- The repository has **no `CONTRIBUTING.md`, no issue templates, no pull-request
  template, no code of conduct, no changelog/NEWS file and no pinned policy
  issue** — `.github/` contains only `workflows/ci.yml`. Release notes are
  written on the GitHub releases page, so no changelog fragment is included in
  any patch. The README's only instruction to users is "If you find a bug or
  have additional requirement for `fastp`, please file an issue:
  https://github.com/OpenGene/fastp/issues/new".
- `.github/workflows/ci.yml`: builds isa-l 2.31.1, libdeflate 1.23 and Highway
  1.3.0 from source, then `make -j`, `./fastp --version` and
  `./fastp -i testdata/R1.fq -o /dev/null` on ubuntu-latest and macos-latest.
  There is no linter, no formatter config and no test job — the project's unit
  tests are `./fastp test` (`src/unittest.cpp`), which must be run from the
  repository root because `FastqReader::test` opens `testdata/R1.fq`. Both were
  run for every branch (`patch_verification.txt`).
- `scripts/test_issue_697_stdout_merge.sh`: the project's own convention for a
  regression script — a `python - <<'PY'` heredoc that writes a small FASTQ, a
  `./fastp` invocation, an assertion, and a `PASS:`/`FAIL:` line.
  `scripts/test_known_adapter_over60.sh` in patch 0002 follows it exactly.
- `README.md` (the option reference and the "per read cutting by quality score",
  "adapters", "filtering" and "global trimming" sections) as the statement of
  intended behaviour that the findings are measured against.
- `src/unittest.cpp`: `Filter::test`, `AdapterTrimmer::test` and the other
  per-class tests, which patches 0001 and 0003 extend.
- Matthew Rocklin's "Craft Minimal Bug Reports" as summarised in the audit brief:
  each of the three texts carries a script that builds its own data, has no line
  that is not needed, prints got vs expected, and says what shrinking the example
  revealed. The scripts are `mcve_fp*.py`; `mcve_outputs.txt` is their captured
  output on master, on v1.3.6 and on v0.23.4.
- Issue tracker searched 2026-09-03 (`mcp__github__search_issues`, several
  phrasings per finding). **Two of the three findings already have an open
  issue**, so their texts are written as comments on those issues rather than as
  new issues:
  - **FP1 → [#474](https://github.com/OpenGene/fastp/issues/474)** "global
    trimming trims too much when combined with quality pruning for SE data"
    (2023-03-21, open, 1 comment): reports exactly this, `-f 6 -5 -3` removing
    nine bases instead of six. **Its one comment could not be read from this
    session** (only issue *search* is available here) and must be read before
    posting. Nearest others: #297 (open, asks what `trim_*` + `cut_*` do
    together, never answered), #453, #493, #329, #24, #122, #328.
  - **FP3 → [#518](https://github.com/OpenGene/fastp/issues/518)** "fastp can not
    remove adapter when the read sequence has indels in the adpter" (2023-08-22,
    open, 0 comments): the case the v0.26.0 gapped search was added for.
    Nearest others: #424, #416, #583, #232.
  - **FP2**: no prior report. Nearest: #673 (2026-03-23, open, auto-detection
    finds far fewer adapters than an explicit `--adapter_sequence` — a different
    path: that run is paired-end without `--detect_adapter_for_pe`, so no
    detection happens at all), #129 "Not detecting the adapter in miRNAseq"
    (2019, open, predates `checkKnownAdapters`), #222, #454, #557, #693, #613.

## Contents

| file | what |
|---|---|
| `issue-fp1-cut-window-trim-front.md` | FP1, drafted as a **comment on #474** |
| `issue-fp2-known-adapter-over60.md` | FP2, a **new issue** |
| `issue-fp3-indel-adapter-offset.md` | FP3, drafted as a **comment on #518** |
| `mcve_fp1_cut_front_trim_front.py`, `mcve_fp2_known_adapter_over60.py`, `mcve_fp3_indel_adapter.py` | the reproductions embedded in those texts |
| `mcve_outputs.txt` | their output on master `dce5c40`, v1.3.6 and v0.23.4 |
| `0001-fix-cut_front-cut_tail-must-not-drop-a-window-of-goo.patch` | FP1 fix + two new `Filter::test()` cases |
| `0002-fix-keep-an-auto-detected-adapter-that-is-longer-tha.patch` | FP2 fix + `scripts/test_known_adapter_over60.sh` |
| `0003-fix-search-for-a-gapped-adapter-at-the-read-offset-n.patch` | FP3 fix + two new `AdapterTrimmer::test()` cases |
| `pr-bodies.md` | PR titles and bodies |
| `patch_verification.txt` | every test run with and without each patch |

All three patches are `git am`-able against `dce5c40` and apply together
cleanly (they touch different files).

## Version scope (executed, `../verify/version_scope_cli.*.out`)

| finding | affected | not affected |
|---|---|---|
| FP1 | `master`, 1.3.6, 1.0.0, 0.26.0, 0.23.4, 0.23.2, 0.22.0, 0.20.1, 0.20.0 | — (the code dates from 2018, 8746036) |
| FP2 | `master`, 1.3.6, 1.0.0, 0.26.0 | 0.23.4, 0.23.2, 0.22.0, 0.20.1, 0.20.0 — those never select a >60 nt adapter (the tree detector truncates to 60 before matching), so the reads are equally untrimmed but for a different reason |
| FP3 | `master`, 1.3.6, 1.0.0, 0.26.0 (the gapped search exists and never fires) | 0.23.4 and older have no gapped search at all |

The cohort's fifth most-cited version, 0.21.0, has no tag in the repository
(the tags go v0.20.1 → v0.22.0), so v0.22.0 was built in its place.

## Order of operations

1. Read the existing comment on #474, then post the FP1 text there; post the FP3
   text on #518; open the FP2 issue from `issue-fp2-known-adapter-over60.md`.
2. Push the three branches to a fork, open PRs 1–3 from `pr-bodies.md`, adding
   the issue numbers.
3. Record issue and PR numbers, and every maintainer response, in `../README.md`
   and in the top-level status table.
