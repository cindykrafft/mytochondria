# Component: Scanpy statistical core (`main` @ `a656a33b`, 2026-08-28, 1.14.0.dev1)

Read in full: `tools/_rank_genes_groups.py` (1,193 lines), `tools/_score_genes.py`
(378), `preprocessing/_normalization.py` (306), `preprocessing/_highly_variable_genes.py`
(844), `preprocessing/_scale.py` (327), `_settings/presets.py`; targeted reads of
`preprocessing/_simple.py` (`regress_out`), `preprocessing/_qc.py`,
`neighbors/_connectivity.py`, `get/_aggregated.py` (`_chan_combine`). Every suspect was
**executed on the shipped code**: master installed in editable mode into a Python 3.12
venv (`pip install -e .`, version string `1.14.0.dev1+ga656a33b0`), harnesses in
`../verify/` with captured output. Where a release comparison mattered, the 1.11.5 wheel
from PyPI (the latest non-prerelease at the time of writing) was diffed.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### SC1 — CONFIRMED on master and the 1.13 pre-releases (1.12.4, the latest stable release, is unaffected): `rank_genes_groups(method="t-test", mean_in_log_space=False)` runs the t-test on exponentiated values

**Code.** `compute_statistics` (`tools/_rank_genes_groups.py:655-658`):

```python
if method in {"t-test", "t-test_overestim_var"}:
    self._basic_stats(exponentiate_values=not mean_in_log_space, need_var=True)
    generate_test_results = self.t_test(method)
```

`_basic_stats` (lines 319-340) replaces `X` by `expm1(X)` when `exponentiate_values`
is set and computes the per-group means *and variances* on that; `t_test` (lines
454-504) builds Welch's statistic from those means and variances. So with
`mean_in_log_space=False` the t-test is Welch's test on the linear-scale normalized
counts, not on the log1p values the function documents as its input ("Expects
logarithmized data"). The parameter's own documentation (lines 828-833) describes only
the fold change: "Whether to do log(mean(e^x)) (False) or log(e^mean(x)) (True)". The
release note that introduced the parameter (1.13.0a1, PR #4037) says "for customizing
how log-fold-change is calculated". The exponentiation of the *test* input entered `main` with PR #4204 ("perf: optimization
of rank_genes_groups", 2026-07-17), which routed both the fold change and the test
through one aggregation pass. **Executed on the released wheels:** 1.12.4 (the latest
stable release, which carries a 1.12-branch version of #4204) keeps the t-test on the
log values for both settings and only accepts `mean_in_log_space` through `**kwds`;
1.13.0a2 reproduces the defect exactly as `main` does. An earlier draft of this review
said "since 1.12.3" from the release notes alone; that was wrong. The package's own test for the parameter (`tests/
test_rank_genes_groups.py::test_mean_in_log_space`) asserts only `logfoldchanges`.

**Verified** (`../verify/sc1_ttest_scale.py`; NB counts, 300 vs 1,700 cells, 3,000
genes, log1p-normalized):

| setting | vs Welch on log1p values | vs Welch on expm1 values |
|---|---|---|
| `mean_in_log_space=True` | max Δscore 1.4e-4 | 5.5 |
| `mean_in_log_space=False` | 5.5 | 5.0e-5 |

On a null dataset both settings are calibrated (10 vs 9 BH < 0.05 discoveries of
3,000, overlap 9). On the dataset with 150 genes 3× up, the two settings return 181 vs
259 significant genes (overlap 177): they are different tests with different power
profiles, not two conventions for one number.

**Who is exposed.** `ScanpyV1` (the default preset) has `mean_in_log_space=True`, so
`t-test` users on default settings get the documented log-scale test. The linear-scale
test runs for anyone who (a) passes `mean_in_log_space=False` explicitly, which the
docstring recommends as "accurate", or (b) uses `sc.settings.preset =
Preset.ScanpyV2Preview` — whose default is `False` — together with `method="t-test"` or
`"t-test_overestim_var"`. Under the V2 preset the default method is `wilcoxon`, which
is unaffected (ranks are always taken on `X`; only its fold change exponentiates).
No cohort paper can have been exposed: no stable release carries it. It is a defect at
master and in the 1.13 pre-releases that will reach the 2.0 defaults.

**Fix shape.** In `compute_statistics`, compute the t-test statistics on `X` and the
fold-change means separately when `mean_in_log_space=False` (a second mean-only
aggregate on `expm1(X)`, which is what the Wilcoxon branch already does two lines
later), or document that the parameter changes the test. Either way,
`test_mean_in_log_space` should also assert `scores`.

**Upstream.** No issue found for this (searched the tracker for the parameter name and
for t-test/exponentiation; the closest are #1454 and #967 about the log-input
assumption). Filing: GitHub issue with the reproduction above on `pbmc68k_reduced`,
then a PR per `docs/dev/code.md` (see `../README.md`).

### SC2 — CONFIRMED on master and in every release since the function was written: `score_genes` does not build `n_bins` equal-frequency bins; the top bin holds between 1 and ~`n_bins`/2 genes, or does not exist

**Code.** `tools/_score_genes.py:279-280`:

```python
n_items = int(np.round(len(obs_avg) / (n_bins - 1)))
obs_cut = obs_avg.rank(method="min") // n_items
```

Ranks run 1..N. Bins 0..`n_bins`−2 therefore hold `n_items` genes each (bin 0 one
fewer), and the last bin holds the `N − (n_bins−1)·n_items + 1` most-expressed genes:
1 gene when N is a multiple of `n_bins−1` (18,000 or 30,000 genes at the default
`n_bins=25`), 9 at N = 20,000, and when rounding goes the other way (N = 25,000 or
33,000) the last bin is empty and there are only `n_bins−1` bins. The docstring says
the function "reproduces the approach in Seurat" and that `n_bins` is the "number of
expression level bins for sampling"; Seurat's `AddModuleScore` uses `cut_number()`,
i.e. `n_bins` equal-frequency bins (800 genes each at N = 20,000). Identical code ships
in 1.11.5 (`scanpy/tools/_score_genes.py:235-236`).

**Verified** (`../verify/sc2_score_genes_bins.py`; part A closed form for N ∈ {2,000 …
33,000}, parts B/C the shipped function on 20,000-gene 10x-like data with no module
structure):

| gene list | shipped: controls used, score | equal-frequency bins: controls, score |
|---|---|---|
| 1 top-9 gene + 4 mid-ranked | 58, +0.39 ± 0.18 | 99, +0.19 ± 0.19 |
| 5 of the top-9 genes | **4**, +0.61 ± 0.57 | 49, +3.15 ± 0.38 |
| all top-9 genes | **RuntimeError: No control genes found in any cut** | 49, +2.88 ± 0.30 |
| all top-9, `ctrl_as_ref=False` | **RuntimeError** | 50, +2.93 ± 0.30 |
| 5 genes ranked ~10,000 | 50, −0.004 ± 0.09 | 49, 0.000 ± 0.09 |
| 50 random genes | 1,047, +0.002 ± 0.04 | 1,046, +0.002 ± 0.04 |

For any list that stays out of the top handful of genes the two binnings agree to
three decimals, so this does not touch typical marker-based signatures. It bites on
lists that include the most highly expressed genes — in PBMC-like data the top ten are
MALAT1, mitochondrial, ribosomal, B2M, TMSB4X, FTL/FTH1 — which is exactly what
"stress", "housekeeping", "ribosomal" and mitochondrial-content signatures contain: the
control set for that bin collapses to a few genes (score variance triples) or to none
(hard error, or a silent "No control genes for cut" warning when other bins still
supply controls, leaving those list genes unmatched). Note that the equal-frequency
scores for the top-gene lists are large and positive too: that is the Tirosh method
itself (bin-matched controls are on average less expressed than the extreme genes in a
heavy-tailed distribution) and Seurat shares it. The scanpy-specific defect is that
`n_bins` is not honoured and the top of the distribution is handled by 1–12 genes.

**Fix shape.** Two lines:

```python
obs_cut = ((obs_avg.rank(method="first") - 1) * n_bins // len(obs_avg)).astype(int)
```

(equal-frequency, `n_bins` bins, ties broken by order as `cut_number` does). Changes
control-gene draws for lists touching the top bin only; `rng`-seeded results for other
lists are unchanged in the number of controls but the sampled *identities* change
because the bin membership changes for the top ~4 % of genes, so the release note must
say scores can move. Part C of the harness is that patch, applied by monkey-patching.

**Upstream.** Not reported: searched for `score_genes` with bins/controls/top genes;
the closest are #3169 (NaN handling, closed) and #2153 (index dtype, closed). File as
an issue with the `pbmc68k_reduced` reproduction (its 765 genes give a 30-gene top
bin, so use the closed-form table plus a list of its top genes), then a PR.

### SC3 — NOTE (documented, quantified): the default Wilcoxon has no tie correction, and on sparse data that shrinks |z| by up to 4×

`rank_genes_groups(method="wilcoxon")` defaults to `tie_correct=False` (line 760);
the variance is then `n·m·(N+1)/12` without the tie term (lines 538-540, 571-573). On
count data almost every gene has a large tie block at zero. Measured on master
(`../verify/note_wilcoxon_tie_correct.py`), median ratio of |z| without correction to
|z| with it, by the gene's fraction of zero cells:

| zeros | < 50 % | 50–80 % | 80–95 % | > 95 % |
|---|---|---|---|---|
| ratio | 0.99 | 0.83 | 0.54 | 0.24 |

Null calibration is fine either way (0 discoveries of 4,000 on null data both ways);
with 200 genes 2.5× up, the default finds 128 and the corrected test 201. The
`illico` implementation behind the ScanpyV2 preset receives the same
`tie_correct=False` default. Conservative, documented, a one-flag choice — recorded
because it is the main reason scanpy's default marker lists are shorter than Seurat's
(presto tie-corrects by default) on the same data, and 14 cohort papers name a
Wilcoxon test.

### SC4 — NOTE (cosmetic): `normalize_total(exclude_highly_expressed=True)` on CSR builds `gene_subset` as a bitwise-negated index array

`preprocessing/_normalization.py:107`: `gene_subset = ~np.where(counts_per_cols)[0]`
is `~` applied to integer indices (giving `−i−1`), not the boolean mask the dense path
builds. It is only used in the log message `adata.var_names[~gene_subset]`, where the
double negation restores the indices, so the printed gene list and the numbers are
right: CSR and dense agree to 2e-5 (float32) in `../verify/heldup_wilcoxon_vs_scipy.py`.
Worth a one-line fix because any future use of `gene_subset` as a mask would be wrong.

### SC5 — NOTE (documentation): `filter_rank_genes_groups(min_fold_change=1)` is a threshold on log2 fold change

`tools/_rank_genes_groups.py:1113, 1189`: `fold_change_matrix` holds
`logfoldchanges` (log2) and is compared with `min_fold_change`, so the default 1 means
a two-fold change. The docstring does not say "log". Users reading it as a linear
fold change of 1 (no filter) get a 2× filter.

## What held up (executed, not just read)

- **Wilcoxon machinery.** With `tie_correct=True`, p-values equal scipy's asymptotic
  Mann–Whitney without continuity correction to 3e-7 (float32 scores); the numba
  `rankdata` and `_tiecorrect` ports equal `scipy.stats.rankdata`/`tiecorrect` exactly
  (`../verify/heldup_wilcoxon_vs_scipy.py`). Scanpy applies no continuity correction by
  design, and its `illico` path is called with `use_continuity=False` to match.
- **t-test on the default preset** equals Welch's test on the log1p values to 1.4e-4
  (SC1 table); `t-test_overestim_var` substitutes `nobs2 = nobs1` as documented.
- **vs-rest statistics via Chan's combine** (`_vars_rest`, `_chan_combine`): the
  leave-one-out variance is a cancellation-free pairwise combine; `means_rest` is the
  exact total-minus-group difference; singleton "remainder" groups are zeroed before
  combining. Consistent with the scipy reference above, which is computed directly on
  the two groups.
- **Multiple testing.** BH via `statsmodels.multipletests` over all tested genes with
  NaN → 1; Bonferroni multiplies by the number of tested genes (after `mask_var`).
- **Fold change** uses a symmetric 1e-9 pseudocount on means of `expm1` (or of
  exponentiated mean-of-logs when `mean_in_log_space=True`), so no group-size
  dependence of the kind found in Seurat v5.
- **`highly_variable_genes`.** `seurat_v3`: loess on log10 variance vs log10 mean
  (degree 2, span 0.3), clip at `mean + reg_std·√n` on the upper side only, normalized
  variance `Σ(clipped − mean)²/((n−1)·reg_std²)` — the same quantities as Seurat's
  `SparseRowVarStd` including the unclipped mean; batch ranking by median rank
  (`seurat_v3`) or by number of batches then rank (`seurat_v3_paper`), as documented.
  `seurat`: dispersion `var/mean` of `expm1(X)`, log-dispersion z-scored within 20
  equal-width bins of `log1p(mean)` with `ddof=1`, single-gene bins set to 1 with a debug
  message — Seurat's `mean.var.plot` conventions. `cell_ranger`: percentile bins and
  normalized MAD.
- **`scale`.** ddof = 1 (documented in 1.12.3), zero-variance genes left at 0, clipping
  symmetric when zero-centred and upper-only otherwise (with an info message).
- **`normalize_total`.** Median of non-zero totals as the default target, computed after
  the highly-expressed exclusion in both code paths.
- **`score_genes_cell_cycle`** phase assignment (S default, G2M if higher, G1 if both
  negative) matches Seurat's `CellCycleScoring`.
- **`regress_out`.** OLS residuals via a closed-form solve when the design is
  non-singular, statsmodels GLM otherwise; categorical regressors are per-category
  means. Same as Seurat's `RegressOutMatrix` (linear model residuals).
- **`describe_obs`/`calculate_qc_metrics`** percentages are `total_qc / total × 100`
  on the raw matrix; `pct_counts_in_top_N` from sorted per-cell segments.

## Not checked here

`pp.pca` (sparse implicit centering, solver choice), `pp.neighbors` beyond the
connectivity kernels, `tl.leiden`/`louvain` (external libraries), `tl.umap`,
`experimental.pp.normalize_pearson_residuals`, the dask code paths, and `illico`'s
internals.
