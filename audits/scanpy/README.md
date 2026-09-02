# Scanpy audit against 200 published papers (2021–2026)

_Eleventh audit in the series. Generated 2026-09-02 against `scverse/scanpy` `main` @
`a656a33b` (2026-08-28, version string 1.14.0.dev1). Focus: correctness at master,
verified by executing the shipped code._

## What this is

The six-journal survey found **200 papers** in *Nature* (129), PNAS (38), *Cell* (24)
and *Science* (9), 2021–2026, that used Scanpy, the dominant Python toolkit for
single-cell analysis; 102 of them also used Seurat. Its statistical core — library-size
normalisation, highly-variable-gene selection, scaling and regression, graph
clustering, marker-gene tests (`rank_genes_groups`), gene-set scoring
(`score_genes`) and QC metrics — was read in full on `main` and every suspicion was
run through the installed package (master, editable install in a Python 3.12 venv) on
simulated data with known truth, with scipy or a closed form as the reference. Where a
release comparison mattered, the 1.11.5 wheel (the latest non-prerelease on PyPI) was
diffed.

## Findings (details and line citations in [`component-reviews/statistical-core.md`](component-reviews/statistical-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **SC1** | **CONFIRMED on master**, since 1.12.3 (2026-07-24) | `rank_genes_groups(method="t-test", mean_in_log_space=False)` runs Welch's t-test on `expm1` of the log-normalized values, not on the values themselves. The parameter is documented and release-noted as controlling only the fold change; the change came in with a performance refactor (PR #4204) and the package's test for the parameter checks only the fold change. Reproduced on master: scores match Welch on `expm1(X)` to 5e-5 and differ from Welch on `X` by up to 5.5; 181 vs 259 significant genes on the same data. Reached by an explicit `mean_in_log_space=False` (the docstring's "accurate" option) or by the `ScanpyV2Preview` preset with a t-test method. |
| **SC2** | **CONFIRMED on master and 1.11.5**, present since the function was written | `score_genes` builds its expression bins as `rank // round(N/(n_bins−1))`, so the top bin holds 1–12 genes (or none), not N/`n_bins`; the docstring promises Seurat's `cut_number` behaviour. Gene lists containing the most-expressed genes get a handful of matched controls (4 for five top genes on 20,000-gene data) or fail with `RuntimeError: No control genes found in any cut`. Lists that avoid the top handful are unaffected (scores agree to 3 decimals with equal-frequency bins). Two-line fix. |
| SC3 | note, documented, quantified | Default Wilcoxon has no tie correction: on genes with > 95 % zeros |z| is shrunk to 0.24 of the corrected value; 128 vs 201 discoveries on the same data. Conservative and a one-flag choice; recorded because 14 cohort papers name a Wilcoxon test and Seurat's presto tie-corrects by default. |
| SC4 | note, cosmetic | `normalize_total(exclude_highly_expressed=True)` on CSR builds `gene_subset` as a bitwise-negated index array; only logged, numbers correct (CSR vs dense agree to 2e-5). |
| SC5 | note, documentation | `filter_rank_genes_groups(min_fold_change=1)` thresholds the log2 fold change; the docstring does not say so. |

**Held up under execution:** the Wilcoxon machinery with tie correction equals
scipy's asymptotic Mann–Whitney; the numba rank and tie-correction ports equal scipy
exactly; the default-preset t-test equals Welch on the log values; BH/Bonferroni; the
symmetric 1e-9 fold-change pseudocount (no group-size dependence of the Seurat v5
kind); `highly_variable_genes` in all three flavours against Seurat's formulas;
`scale`, `normalize_total`, `regress_out`, `score_genes_cell_cycle` phase logic and the
QC percentages. Not audited: `pp.pca`, `pp.neighbors` beyond the kernels, Leiden/
Louvain, UMAP, Pearson residuals, dask paths, `illico` internals.

## How the papers use Scanpy (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| UMAP | 171 |
| Seurat in the same paper | 102 |
| doublet removal (Scrublet etc.) | 70 |
| trajectory / PAGA / diffusion / velocity | 57 |
| PCA | 47 |
| Leiden / Louvain | 42 / 12 |
| CellChat / ligand–receptor tools | 41 |
| batch integration (Harmony, BBKNN, scVI, ComBat, Scanorama) | 32 |
| spatial (squidpy, Visium, Xenium, MERFISH) | 19 |
| `highly_variable_genes` | 18 (n_top_genes stated 4; seurat_v3 named 1) |
| adjusted p / BH | 18 |
| `log1p` / `normalize_total` | 18 / 12 |
| Wilcoxon named / t-test named / logreg | 14 / 3 / 1 |
| `score_genes` / `score_genes_cell_cycle` | 8 / 1 |
| `rank_genes_groups` named | 4 |
| `regress_out` / `scale` | 4 / 2 |
| version stated | 35 (1.9.x 30, 1.8.x 11, 1.6.x 11, 1.10.x 8, 1.4.x 7, 1.7.x 6, 1.11.x 2) |

Versions pinned run 1.4 to 1.11; SC1 (1.12.3+) therefore has no published exposure
yet, and SC2 is present in every version the cohort names.

**Profiling caveat.** As for the Seurat audit, this session had no route to Europe PMC,
so `scanpy_profile.py` ran in `--offline` mode over the survey's stored evidence
snippets; every record in `scanpy_profiles.jsonl` is `source: survey_cache` and every
count above is a lower bound. Rerun without `--offline` from a host with Europe PMC
access to replace them with full-text records.

## Filing channel (read before anything is sent)

- `CONTRIBUTING.md`: search the tracker first; a minimal complete verifiable example
  with every bug report; environment via `sc.logging.print_versions()`.
- `.github/ISSUE_TEMPLATE/bug-report.yml`: checkboxes for "not already reported",
  "exists on the latest version", optional "exists on main"; a minimal code sample.
  Analysis questions go to Discussions (`config.yml`).
- `docs/dev/code.md`: fork, branch, tests passing, docs built, PR, **and a release note
  fragment in `docs/release-notes/`** with each PR. `.github/pull_request_template.md`
  wants "Closes #", tests included or a reason, release note or a reason. Ruff
  formatting via `hatch check fmt --fix`.
- Both SC1 and SC2 are small, crisp, and change numbers; file each as an issue with the
  reproduction, then a PR with a test and a release note. Neither has a prior issue
  (tracker searched 2026-09-02). **The kit is in [`upstream/`](upstream/)**: two issue
  texts in the bug-report template's fields with reproductions run on `main`, two
  `git am`-able patches (fix + test + towncrier fragment; each new test fails on
  unmodified `main` and the affected test file passes with the patch, except the
  `paul15` reference pickle that PR 2 must regenerate), and the PR bodies.

## Files

| file | what |
|---|---|
| `scanpy_profile.py`, `scanpy_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/statistical-core.md` | the review: SC1–SC5, held-up list, not-audited list |
| `verify/sc1_ttest_scale.py` (+ `.out`) | SC1 on master: scores vs scipy Welch on log and linear values; null and DE datasets |
| `verify/sc2_score_genes_bins.py` (+ `.out`) | SC2: closed-form bin sizes; shipped `score_genes` vs an equal-frequency patch on 20,000-gene data |
| `verify/note_wilcoxon_tie_correct.py` (+ `.out`) | SC3: |z| shrinkage by sparsity, null and DE discoveries |
| `verify/heldup_wilcoxon_vs_scipy.py` (+ `.out`) | held-up: Wilcoxon vs scipy, rankdata/tiecorrect ports, CSR vs dense `normalize_total` |
| `upstream/` | filing kit: issue texts, patches 0001 (SC1) and 0002 (SC2) with tests and release-note fragments, PR bodies, checklist |

Harnesses need the master install: `uv venv --python 3.12 venv && uv pip install -e
<scanpy clone> scikit-misc igraph leidenalg`.

## Next steps

1. File SC1 and SC2 upstream from the kit in `upstream/` (issue first, then PR; PR 2
   needs the `paul15` reference pickle regenerated, which this environment could not
   download). Record numbers and maintainer responses here.
2. Extend the review to `pp.pca` and `pp.neighbors`, the two remaining core paths every
   cohort paper runs.
3. Full-text profiling rerun when Europe PMC is reachable.
