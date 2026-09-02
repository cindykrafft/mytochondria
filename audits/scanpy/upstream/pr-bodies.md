# PR bodies (scverse/scanpy `.github/pull_request_template.md`)

Branch names follow the conventional-commit prefixes towncrier expects (`fix`).
Each patch carries its release-note fragment as `docs/release-notes/+<slug>.fix.md`;
the contributing guide says to create it with `hatch run towncrier:create` and to
enter the PR number when asked, so once the PR number is known, rename the fragment
to `<PR number>.fix.md` (the `+` prefix marks an orphan fragment and is accepted as-is).

---

## PR 1 — `0001-fix-run-t-test-on-log-values-regardless-of-mean_in_l.patch`

**Title:** fix: run t-test on log values regardless of `mean_in_log_space`

- [x] Closes #<SC1 issue>
- [x] [Tests][] included: `test_mean_in_log_space_does_not_change_ttest` asserts `scores` and `pvals` are identical for `mean_in_log_space=True/False` with both t-test methods on `pbmc68k_reduced`; it fails on `main` and passes with the fix. Full `tests/test_rank_genes_groups.py` passes.
- [ ] [Release notes][] not necessary because: — (fragment `docs/release-notes/+ttest-log-space.fix.md` included)

Since #4204, `compute_statistics` computed the per-group means and variances on
`expm1(X)` for the t-test methods whenever `mean_in_log_space=False`, so Welch's test
ran on linear-scale values. `mean_in_log_space` is documented as a fold-change option
only (#4037 release note), and the function expects log data. This computes the test
statistics on `X`, materializes the test results, and only then recomputes the means
on `expm1(X)` for `logfoldchanges` when requested — the same order the `wilcoxon`
branch uses. `logfoldchanges` are unchanged (existing `test_mean_in_log_space` still
passes).

[tests]: https://scanpy.readthedocs.io/en/stable/dev/testing.html#writing-tests
[release notes]: https://scanpy.readthedocs.io/en/stable/dev/documentation.html#adding-to-the-docs

---

## PR 2 — `0002-fix-build-n_bins-equal-frequency-expression-bins-in-.patch`

**Title:** fix: build `n_bins` equal-frequency expression bins in `score_genes`

- [x] Closes #<SC2 issue>
- [x] [Tests][] included: `test_bins_are_equal_frequency` checks that the top five genes share one bin that supplies a full `ctrl_size` set of controls, for N = 2,000 / 18,000 / 25,000 (the three rounding regimes), and that scoring them no longer raises. `test_gene_list_is_control` now pins the seed its `ctrl_as_ref=True` case relies on (the single control drawn from g3's two-gene bin must be g3 itself).
- [ ] [Release notes][] not necessary because: — (fragment `docs/release-notes/+score-genes-bins.fix.md` included)

`_score_genes_bins` used `rank // round(N / (n_bins - 1))`, which fills bins
`0..n_bins-2` with `round(N/(n_bins-1))` genes each and leaves the top bin with
between one and about `n_bins/2` genes, or removes it. Lists containing the most
highly expressed genes got almost no matched controls or raised "No control genes
found". This uses `n_bins` equal-frequency bins (ties by order), which is what the
docstring's reference to Seurat (`cut_number`) describes.

**Behaviour change to flag in review:** bin membership shifts for every gene, so
seeded control draws change. `tests/_data/score_genes_reference_paul2015.pkl` was
generated "using the same code" (per `test_score_with_reference`'s docstring) and
must be regenerated with this branch:

```python
import pickle, scanpy as sc
from testing.scanpy._helpers.data import paul15
adata = paul15(); sc.pp.normalize_total(adata, target_sum=1e4); sc.pp.scale(adata)
sc.tl.score_genes(adata, gene_list=adata.var_names[:100], score_name="Test")
pickle.dump(adata.obs["Test"].to_numpy(), open("tests/_data/score_genes_reference_paul2015.pkl", "wb"))
```

I could not regenerate it myself (the `paul15` download is blocked from my
environment); every other test in `tests/test_score_genes.py` passes.

[tests]: https://scanpy.readthedocs.io/en/stable/dev/testing.html#writing-tests
[release notes]: https://scanpy.readthedocs.io/en/stable/dev/documentation.html#adding-to-the-docs
