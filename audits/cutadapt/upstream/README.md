# Cutadapt upstream filing kit

_Prepared 2026-09-03 against `marcelm/cutadapt` `main` @ `50e9fb8d` (2026-06-26,
5.3.dev15). **Nothing has been filed.** The four fix branches exist only in the
session's scratch clone; the `git am`-able patches are in this directory._

## What was read before preparing this (step 4 of the method)

- `CONTRIBUTING.rst`: one topic per PR; open an issue first for larger changes;
  include unit/integration tests; add documentation and a changelog entry where
  appropriate; black formatting (pre-commit), Google-style docstrings, no
  abbreviations, capitalise FASTQ/BWA/CPU in prose. Shaped the kit: four separate
  patches, each with tests and a changelog entry; PR 3 (changes demultiplexing
  results) is marked "issue first".
- `.github/ISSUE_TEMPLATE/bug_report.md` and `.github/issue_template.md`: free-text
  template asking for Cutadapt and Python version, how installed, command-line
  parameters, an example read, the output produced and the expected output, no
  screenshots. The four `issue-ca*.md` texts follow those fields in that order.
  `feature-suggestion.md` is empty; there is no `config.yml`, no discussions link,
  no pinned policy issue, no code of conduct file, no PR template.
- `tox.ini` / `.github/workflows/ci.yml`: CI runs `flake8 src/ tests/ setup.py`
  (max line 120, `E,F,W,C90,W504`, extended ignores), `black==22.3.0 --check`,
  `mypy src/`, `sphinx-build -W` for docs, and `pytest --doctest-modules` on Python
  3.10–3.13. Black 22.3.0 and flake8 were run on every changed file of every patch.
- `CHANGES.rst`: entries are bullets under a `development version` heading
  (underlined with dashes) that sits above the last release until the next release
  is cut, each usually prefixed `:issue:\`NNN\`:` or `:pr:\`NNN\`:`. Each patch adds
  that heading with one bullet; the issue number has to be added once it exists.
- `doc/algorithms.rst` and `doc/guide.rst` ("Error tolerance", "Quality trimming",
  "Filtering reads", "Wildcards", "Alignment algorithm changes in Cutadapt 4") as the
  statement of intended behaviour that the findings are measured against.
- `pyproject.toml` (`[tool.pytest.ini_options]`: warnings are errors, `xfail_strict`,
  10 s timeout; `[tool.ruff] line-length = 130` exists but CI uses black/flake8).
- Issue tracker searched 2026-09-03 for each finding (semantic search over
  `marcelm/cutadapt` issues): no prior report of CA1 (nearest #358, #457, #615),
  CA2 (nearest #17, #441), CA3 (nearest #734, #612, #205, #614, #671) or CA4
  (nearest #685 "Disable k-mer heuristic in some cases", #695, #565).
- Matthew Rocklin's "Craft Minimal Bug Reports" as summarised in the audit brief:
  each issue text carries a script that makes its one read, has no line that is not
  needed, prints got vs expected, and says what shrinking revealed. The scripts are
  `mcve_ca*.py`; `mcve_outputs.txt` is their captured output on `main` and 5.2.

## Contents

| file | what |
|---|---|
| `issue-ca1-absolute-errors-rounding.md` | bug report: `-e N` loses one error for adapter lengths 49, 98, … (template fields, MCVE, cause, fix) |
| `issue-ca2-max-ee-quality-base.md` | bug report: `--max-ee`/`--max-aer` ignore `--quality-base` |
| `issue-ca3-index-criterion.md` | bug report: index ranks by matches, `--no-index` by score |
| `issue-ca4-prefilter-insertions.md` | bug report: anchored/non-internal adapters with an inserted base not found |
| `mcve_ca1_absolute_errors.py` … `mcve_ca4_prefilter_insertion.py`, `mcve_outputs.txt` | the reproductions embedded in the issues, and their output on `main` and 5.2 |
| `0001-Honour-an-absolute-number-of-errors-e-N-for-every-ad.patch` | CA1 fix + tests + changelog (`git am`-able on `50e9fb8d`) |
| `0002-Make-max-ee-and-max-aer-honour-quality-base.patch` | CA2 fix + tests + changelog |
| `0003-Choose-the-best-adapter-by-alignment-score-also-when.patch` | CA3 fix + tests + changelog |
| `0004-Fix-k-mer-heuristic-missing-anchored-adapters-with-a.patch` | CA4 fix + tests + changelog |
| `pr-bodies.md` | PR titles and bodies, and the notes about applying more than one patch |

## Verification status of the patches

Each branch was installed editable into its own Python 3.12 venv (Cython build) and
the harnesses in `../verify/` were rerun under it; the "without" column is the new
test file run against unmodified `main`.

| patch | new tests on unmodified `main` | touched modules with patch | full `tests/` with patch | harness under patch |
|---|---|---|---|---|
| 0001 (CA1) | `test_align.py`, `test_adapters.py`: **2 failed** | `test_align test_adapters test_kmer_heuristic test_kmer_finder`: 142 passed; `test_commandline test_paired test_trim test_modifiers`: 392 passed | 708 passed | 49-nt adapter with one substitution found under `-e 1` for every adapter class |
| 0002 (CA2) | `test_predicates.py`: **2 failed** | `test_predicates`: 19 passed; `test_commandline test_paired test_main`: 354 passed | 706 passed | `--max-ee`/`--max-aer` with `--quality-base 64` equal the reference (0 / 0 / 2 kept) |
| 0003 (CA3) | `test_adapters.py`: **2 failed** | `test_adapters test_modifiers test_commandline test_paired test_trim`: 442 passed | 706 passed | index and `--no-index` both assign B; mixed list picks the 3' adapter in both |
| 0004 (CA4) | `test_adapters.py`: **3 failed**; `test_kmer_heuristic.py`: 4 failed (window expectations) | `test_kmer_heuristic test_kmer_finder test_adapters test_commandline test_paired test_trim`: 439 passed | 707 passed | 0 of 2,000 / 3,500 / 2,200 accepted insertion reads lost |

Unmodified `main`: 704 passed. `black --check` (22.3.0) and `flake8` (project
config) pass on every changed file. `git apply --check` succeeds for each patch
against `50e9fb8d`; applying all four at once conflicts only in the `CHANGES.rst`
heading and in the tests that 0003 and 0004 both append to `tests/test_adapters.py`.

## Version scope (executed, `../verify/version_scope_cli.*.out`)

| finding | present | absent |
|---|---|---|
| CA1 | 4.1, 4.2, 4.3, 4.4, 4.5, 4.9, 5.0, 5.1, 5.2, `main` | — (feature exists since 3.0, by reading) |
| CA2 | 4.1, 4.2, 4.3, 4.4, 4.5, 4.9, 5.0, 5.1, 5.2, `main` | — (`--max-ee` exists since 2.9, by reading) |
| CA3 | 5.0, 5.1, 5.2, `main` (introduced with the 5.0 index rewrite) | 4.1, 4.2, 4.3, 4.4, 4.5, 4.9 |
| CA4 | 4.3, 4.4, 4.5, 4.9, 5.0, 5.1, 5.2, `main` (introduced with the 4.3 heuristic) | 4.1, 4.2 |

Releases 3.4 and 1.18 (the cohort's most-cited versions with 4.1) do not build on
Python 3.11/3.12 (`longintrepr.h`, Cython-era C), so their status is by reading only.

## Order of operations

1. Open the four issues from the texts above (CA1, CA2, CA4 are plain bugs; CA3
   changes demultiplexing results and asks for the maintainer's view first).
2. Push each branch to a fork, `git am` the patch onto a fresh `main`, add the issue
   number to the changelog bullet, open PRs 1, 2 and 4; open PR 3 after the CA3
   discussion.
3. Record issue and PR numbers, and every maintainer response, in `../README.md`
   and in the top-level status table.
