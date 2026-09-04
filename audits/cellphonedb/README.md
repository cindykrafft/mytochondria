# CellPhoneDB audit against 46 published papers (2021–2026)

_Twelfth audit in the series. Generated 2026-09-03 against `ventolab/CellphoneDB` `master` @
`dc8abd15` (2025-06-06, version string 5.0.1). Focus: correctness at master, verified by
executing the shipped code._

## What this is

The six-journal survey found **46 papers** in *Nature* (27), PNAS (14), *Cell* (3) and *Science*
(2), 2021–2026, that used CellPhoneDB — the most-used ligand–receptor inference tool in the
cohort that is reachable from Python (CellChat, the only one used more, is R and out of scope for
this environment). Its statistical core — cluster means and expression percentages, the minimum
rule for heteromeric complexes, the interaction mean, the label-permutation test, the
significance cut-off, the microenvironment restriction, the DEG-based method and the v5
interaction-scoring module — was read in full on `master` and every suspicion was run through the
installed package (master, editable install in a Python 3.12 venv) against an independent numpy
implementation of the documented method on synthetic data with known truth, and, where the
permutation null was small enough, against an **exhaustive enumeration of all 1,680 label
assignments**.

The package code at `master` is byte-identical to tag `v5.0.1` and to the PyPI 5.0.1 wheel, so
everything confirmed here is confirmed in the latest release. Where a finding could be older,
each release's own source was checked out and executed rather than inferred from release notes.

## Findings (details and line citations in [`component-reviews/statistical-core.md`](component-reviews/statistical-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **CPDB1** | **CONFIRMED on master and 5.0.1** (structure present since v2.1.7, executed on master) | With `threads = T` the permutation workers all draw the **same** shuffles: every forked worker inherits the parent's numpy RNG state, so the null holds ~`iterations/T` distinct permutations, each counted T times. Measured at `iterations=1000`: 1000 distinct at `threads=1`, **504** at 2, **279** at 4, **137** at 8. The p-value estimator then has the precision of `iterations/T` draws (effective n 270 vs 1068 over 20 repeat runs), and two analyses run back to back in one session re-use 86 % of the same permutations, so re-running does not average the error away. `threads` defaults to 4; the tutorials pass 5 and 25. |
| **CPDB2** | **CONFIRMED on v2.1.7, v3.1.0, v4.0.0, v5.0.0, 5.0.1 and master** (each executed) | The p-value counts only permutations **strictly greater** than the observed mean (`np.packbits(shuffled > real)`), discarding ties, where the documentation says "as high as or higher" / "equal or higher" in both places it states the rule. Over the exhaustive 1,680-permutation null the tie mass is median 3.5 %, max 20.2 % of the null, and **3 of 22 tested entries change from not-significant to significant** at `pvalue=0.05`. Because the observed labelling is never counted, **p = 0 is reachable**: on the project's own endometrium example at documented defaults, **16,821 of 39,444 tested entries (42.6 %) are reported as exactly 0**. |
| **CPDB3** | **CONFIRMED on master and 5.0.1** (regression since v4.0.0) | In METHOD 1 (`cpdb_analysis_method`) the `threshold` argument changes **nothing** in any output: the only table that uses it, `significant_means`, is computed, used for a rank sort, and dropped from the returned dict, so it is never written either. Runs at `threshold=0.1` and `threshold=0.99` produce three **byte-identical** files. The documentation says this method "will report the means only if all the gene members of the interactions are expressed by at least a fraction of cells (`threshold`)". |
| **CPDB4** | **CONFIRMED on master and 5.0.1** (present since v3.1.0) | In `deconvoluted.txt` and `deconvoluted_percents.txt`, every **subunit** row of a heteromeric complex carries the **complex's minimum**, not that subunit's own mean/percentage: the row is labelled with the subunit's gene name but joined on the complex's multidata id. 6 of 6 subunit rows wrong on the fixture (e.g. SUB1 in CTB reported as 1.0, its own mean 3.0 — it is SUB2's value). This is the file the docs point users at to check whether all subunits of a heteromer are expressed, which it cannot show when every subunit reports the same number. Simple rows are correct. |
| **CPDB5** | **CONFIRMED on master, 5.0.1 and v5.0.0** | `threads=1` with `iterations <= 50` raises `ZeroDivisionError: float modulo` before producing anything, because `progress_step = round(iterations/100, 0)` is 0. `threads=1` is the workaround the code's own comment recommends for R/RStudio on Windows. One-line fix, no numerical effect. |
| **CPDB6** | **CONFIRMED on master and 5.0.1 with pandas >= 3** | `score_interactions=True` — the headline v5 feature, enabled in all three tutorial notebooks — fails with `ValueError: at least one array or dtype is required` from `MinMaxScaler`. Cause: a chained inplace `replace` (`matrix[index_name].replace(..., inplace=True)`) that is a no-op under copy-on-write, so the gene-name index is never applied and an empty frame reaches the scaler. Executed both ways: pandas 3.0.5 raises, pandas 2.3.3 completes. `pyproject.toml` allows `pandas>=1.5.0`; CI pins Python 3.8, which cannot install pandas 3. |
| N1 | note, documentation | `result_precision` is not applied to `pvalues.txt` (18-digit values at `iterations=300` while the means file has 3). |
| N2 | note, cosmetic | The significance cut-off is inclusive (`p > pvalue` masks), so p exactly equal to `pvalue` is kept; docs and docstring say "below" / "< 0.05". |
| N3 | note, edge case | `pvalue=0` silently inverts the filter (`if min_significant_mean:` is falsy): 34 of 36 entries kept, 13 of them with p = 1.0, and the one p = 0 entry dropped. |
| N4 | note, cosmetic | The scoring filter (`pct < threshold` drops) and the significance filter (`pct > threshold` keeps) disagree at an exact tie: the same gene scores 25.0 while its p-value is forced to 1. |
| N5 | note, by reading (not executed) | Several counts rows mapping to one `id_multidata` are **averaged**, so an undetected second transcript halves a gene's expression. Stated in the docstring; the consequence is not. |
| N6 | note, crash on a documented workflow | `db_utils.create_db` raises `ValueError: You are trying to merge on float64 and str columns for key 'uniprot_4'` when no complex in `complex_input.csv` fills the widest `uniprot_N` column — the normal case for a small custom database. Adding one four-subunit complex makes the same file build. |

**Held up under execution:** an independent numpy port of the documented method reproduces every
number the statistical pipeline produces on the fixture — cluster means (plain mean over all
cells, zeros included), percentages (per gene, on `counts > 0`), the complex **minimum taken
after** per-subunit averaging (and the minimum of percentages for the threshold), the interaction
mean `(x>0)(y>0)(x+y)/2`, the threshold rule, the p-value counting rule (exact match on a
tie-free fixture over the shuffles the package actually drew), `significant_means` and `rank`.
Rounding happens **after** the comparisons, so `result_precision` cannot move an interaction
across the cut-off. The shuffle is over cell labels with cluster sizes preserved, redrawn from
the original labels each iteration. Self-interactions (`clusterA|clusterA`) are ordinary columns
and need no special case. `microenvs` restricts only which cluster pairs are tested while the
permutation still shuffles across all cells, as documented. The v5 scoring protocol reproduces
its five documented steps **exactly** (max difference 0.000), including the geometric mean for
heteromers — deliberately different from the minimum used by the inference methods, and
documented as such. The DEG method's two criteria (either partner a DEG, AND both above the
percentage threshold) match the documentation.

**Not checked:** `search_utils`, the CellSign TF module beyond its call sites, the subsampler
(`geosketch`), database generation beyond using it, the plotting notebooks, CellphoneDBViz, and
the database *content* itself.

## How the papers use CellPhoneDB (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| Seurat / Scanpy upstream | 41 |
| CellPhoneDB version stated | 19 |
| CellChat also used | 6 |
| squidpy / Omnipath wrapper | 5 |
| CellSign / TF module named | 4 |
| microenvironments / database version stated | 3 / 3 |
| statistical method (method 2) named | 3 |
| LIANA also used / p-value cut-off stated | 3 / 3 |
| subsampling / spatial data / dot plots | 2 / 2 / 2 |
| NicheNet also used / log-normalised input stated | 2 / 2 |
| simple method (method 1) / DEG method (method 3) named | 1 / 1 |
| ktplots / threshold stated | 1 / 1 |
| version family: v2 / v3 / v4 / v5 | 7 / 2 / 1 / 2 (12 papers pin a version at all) |
| named in the Methods section | 36 |

Versions pinned run 2.0 to 5. CPDB2 is present in every one of them; CPDB1's structure likewise
(executed at master); CPDB3 covers the v4 and v5 papers; CPDB4 the v3, v4 and v5 papers; CPDB5
and CPDB6 are v5-only. The three papers that name the statistical method and the three that state
a p-value cut-off are the most directly exposed to CPDB2, but the p-value path is the default for
this tool and 36 papers describe it in their Methods.

**Profiling caveat.** As for the Seurat and Scanpy audits, this session had no route to Europe
PMC, so `cellphonedb_profile.py` ran in `--offline` mode over the survey's stored evidence
snippets; every record in `cellphonedb_profiles.jsonl` is `source: survey_cache` and **every
count above is a lower bound**, not a measurement. Rerun without `--offline` from a host with
Europe PMC access to replace them with full-text records. Because the cached text concatenates
the evidence snippets of every package a paper used, numeric settings and versions are read only
from a ±300-character window around a CellPhoneDB mention; feature flags are paper-level signals
and may be triggered by a co-package's snippet.

## Filing channel (read before anything is sent)

The repository's contributing conventions are **very light** — this is worth stating plainly
because it shapes the kit:

- **No `CONTRIBUTING.md`, no issue templates, no pull-request template, no code of conduct, no
  `CHANGELOG`.** `find` over the tree returns none of them; `.github/` contains exactly one file,
  `workflows/python-app.yml`.
- `README.md:242-244` is the whole of it: "CellphoneDB is an open-source project. If you are
  interested in contributing to this project, please let us know", pointing at the readthedocs
  documentation.
- Release notes live as prose in `previous_releases.md` and in the "Release notes" prose of
  `docs/RESULTS-DOCUMENTATION.md`; there is no per-PR fragment convention to follow.
- **CI** (`.github/workflows/python-app.yml`): Python **3.8**; `flake8 --select=E9,F63,F7,F82`
  blocking, then a non-blocking `flake8 --max-complexity=10 --max-line-length=127`; then
  `pytest method_tests.py` from `cellphonedb/src/tests`. Those tests **download the v4.1.0
  database from GitHub** in `setUp`, which is blocked here (HTTP 403), so the suite cannot be run
  in this environment — see the kit's README for what was run instead.
- Curation questions go to <contact@cellphonedb.org> or to the separate
  `ventolab/cellphonedb-data` repository (`docs/RESULTS-DOCUMENTATION.md:427`); code issues go to
  this repository's tracker.
- **Prior issues searched** (2026-09-03, `mcp__github__search_issues`; the GitHub issue-*reading*
  API is not available for this repository from this session, so only titles and bodies could be
  read — **not the maintainers' replies**). Nothing found for CPDB1, CPDB3, CPDB4, CPDB5 or
  CPDB6. For CPDB2 the neighbourhood is #179 "Can Minimum p-value less than 1e-3" (closed; a user
  raising 100,000 iterations and still seeing a floor), #60 "Precision of pvalues" (closed), #24,
  #155 "Exact p-value output file?" (open), #121 "Pvalue adjusting" (closed), #124. **None of
  them raises the strict-vs-inclusive rule or p = 0**, but #179 and #60 are close enough that
  their replies must be read before filing, in case a maintainer has already explained the
  estimator there.

CPDB2, CPDB3 and CPDB4 all change published numbers, so each gets an issue first rather than a
cold PR. CPDB5 and CPDB6 are crisp, no-numerical-effect fixes and carry patches.
**The kit is in [`upstream/`](upstream/)** — nothing has been filed.

## Files

| file | what |
|---|---|
| `cellphonedb_profile.py`, `cellphonedb_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/statistical-core.md` | the review: CPDB1–CPDB6, N1–N5, held-up list, not-checked list |
| `verify/tiny_dataset.py` | shared fixture: hand-written database built by the package's own `create_db`, 9-cell counts matrix, and the independent numpy reference |
| `verify/heldup_reference_vs_shipped.py` (+ `.out`) | held-up: every number of the pipeline vs the reference port |
| `verify/cpdb1_thread_duplicate_permutations.py` (+ `.out`) | CPDB1: distinct permutations by thread count, session re-use, effective sample size |
| `verify/cpdb2_pvalue_ties_and_zero.py` (+ `.out`) | CPDB2: exhaustive 1,680-permutation null, tie mass, significance flips, p = 0 |
| `verify/version_scope_pvalue_rule.py` (+ `.out`) | CPDB2 executed on v2.1.7 / v3.1.0 / v4.0.0 / v5.0.0 / v5.0.1 / master |
| `verify/realdata_endometrium.py` (+ `.out`) | CPDB1/CPDB2 impact on the repository's own endometrium example with the v5.0.0 database |
| `verify/cpdb3_method1_threshold_ignored.py` (+ `.out`) | CPDB3: byte-identical outputs at two thresholds; METHOD 2 contrast |
| `verify/cpdb4_deconvoluted_complex_subunits.py` (+ `.out`) | CPDB4: subunit rows vs their own means and percentages |
| `verify/cpdb5_iterations_le_50_crash.py` (+ `.out`) | CPDB5: the boundary and the full traceback |
| `verify/cpdb6_scoring_crashes_pandas3.py` (+ `.out`) | CPDB6: pandas 3 vs pandas 2, and the failing step in isolation |
| `verify/note_pvalue_precision_cutoff.py` (+ `.out`) | N1, N2, N3 |
| `verify/note_scoring_pipeline.py` (+ `.out`) | scoring port (held up) and N4 |
| `verify/note_create_db_empty_uniprot_column.py` (+ `.out`) | N6: `create_db` on a complex table with an unused subunit column |
| `upstream/` | filing kit: issue texts, patches for CPDB5 and CPDB6, PR bodies, and what was read |

Harnesses need the master install:
`uv venv --python /usr/bin/python3.12 venv && uv pip install -e <CellphoneDB clone>`.
`note_scoring_pipeline.py` must run in a **pandas < 3** environment (that is CPDB6);
`cpdb6_scoring_crashes_pandas3.py` is meant to be run in both.
`realdata_endometrium.py` and `version_scope_pvalue_rule.py` take `CPDB_CLONE` to locate the
clone. No harness needs the network: the database is built by the package from hand-written
tables, because the official download returns HTTP 403 from this environment.

## Next steps

1. File CPDB5 and CPDB6 (issue + patch each; both are safe, no numerical effect). Read the
   replies on #179 and #60 first, then file CPDB2 as an issue with the exhaustive-enumeration
   evidence — it is the finding that touches every published p-value.
2. File CPDB3 and CPDB4 as issues; both change what a documented output file contains.
3. CPDB1 needs a design decision from the maintainers (per-iteration seeding), so file the
   measurement and offer the `SeedSequence` patch rather than pushing one.
4. Rerun `cellphonedb_profile.py` without `--offline` when Europe PMC is reachable, and re-derive
   the exposure table from full text.
5. Not covered here and worth a second pass: `search_utils`, CellSign, and the subsampler.
