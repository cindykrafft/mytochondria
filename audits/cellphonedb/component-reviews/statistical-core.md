# Component: CellPhoneDB statistical core (`master` @ `dc8abd15`, 2025-06-06, version string 5.0.1)

Read in full: `cellphonedb/src/core/methods/cpdb_statistical_analysis_helper.py` (791 lines),
`cpdb_statistical_analysis_complex_method.py` (373), `cpdb_statistical_analysis_method.py` (163),
`cpdb_analysis_method.py` (376), `cpdb_degs_analysis_method.py` (488),
`cellphonedb/utils/scoring_utils.py` (353); targeted reads of `utils/db_utils.py` (696),
`utils/file_utils.py` (469), `src/core/preprocessors/*`, `src/core/models/complex/complex_helper.py`,
`src/core/utils/subsampler.py`, and `src/tests/method_tests.py`.

Every suspicion was **executed on the shipped code**: master installed editable into a Python
3.12 venv (`uv pip install -e`, version string 5.0.1), harnesses in `../verify/` with captured
output. The package code at `master` is byte-identical to tag `v5.0.1` (`git diff v5.0.1 master
-- cellphonedb/` is empty) and to the PyPI 5.0.1 wheel (`diff -r` over the installed tree), so
everything below that is confirmed at master is confirmed in the latest release. Where a finding
could be older, each release's own source was checked out and executed
(`../verify/version_scope_pvalue_rule.py`).

**Database.** `db_utils.download_database` fetches
`github.com/ventolab/cellphonedb-data/archive/refs/tags/<v>.zip`, which returns HTTP 403 from
this environment. Two substitutes were used, neither downloaded: (a) a **minimal database built
by the package's own `db_utils.create_db`** from four hand-written `*_input.csv` tables
(5 proteins, 6 gene rows, 2 complexes, 4 interactions -- `../verify/tiny_dataset.py`), which is
what every unit-scale harness uses; (b) the **official v5.0.0 database that ships inside the
repository** at `NatureProtocols2024_case_studies/v5.0.0/cellphonedb.zip`, used for the
real-data run on the repository's own endometrium example.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### CPDB1 — CONFIRMED on master and 5.0.1: with `threads = T` the permutation workers draw the same shuffles, so the null holds ~`iterations/T` distinct permutations

**Code.** `shuffled_analysis` (`cpdb_statistical_analysis_helper.py:494-506`) dispatches the
iterations to a process pool:

```python
with Pool(processes=threads) as pool:
    statistical_analysis_thread = partial(_statistical_analysis, ...)
    for result in tqdm(pool.imap(statistical_analysis_thread, range(iterations)), ...):
```

and each task shuffles through the **global** numpy RNG (`shuffle_meta`, line 96:
`np.random.shuffle(meta_copy['cell_type'].values)`). On a fork platform every worker inherits
the parent's RNG state at fork and then advances its own private copy, so worker *k*'s *j*-th
shuffle equals worker *l*'s *j*-th shuffle. `imap` hands out tasks dynamically, so multiplicities
are not exactly `T` (a worker that happens to run more tasks contributes a few unique draws at
the tail), but the bulk of the null is `T` copies of the same permutation.

**Verified** (`../verify/cpdb1_thread_duplicate_permutations.py`, fixture of 30 cells in three
cell types of ten, so 30!/(10!)³ = 5.55e12 distinct assignments exist and repeats cannot arise
by chance; `iterations=1000`, `debug_seed=-1`, i.e. the default user path; permutations recorded
by wrapping the package's own `shuffle_meta`):

| `threads` | shuffles drawn | distinct | multiplicity |
|---|---|---|---|
| 1 | 1000 | **1000** | 1×: 1000 |
| 2 | 1000 | **504** | 2×: 496, 1×: 8 |
| 4 | 1000 | **279** | 4×: 219, 3×: 27, 2×: 10, 1×: 23 |
| 8 | 1000 | **137** | 8×: 110, 7×: 3, 6×: 8, … |

Two consequences, both measured:

- **Repeat runs in one session are not independent replicates.** Nothing in the parent process
  consumes the global RNG when `threads > 1` (all shuffling happens in the children), so the
  second `Pool()` forks from the same state as the first. Two analyses run back to back:
  `threads=4` shares 258 of run 1's 300 distinct permutations (86 %); `threads=1` shares 0.
- **The estimator has the precision of `iterations/threads` draws.** Over 20 repeats run as
  separate processes, the median per-entry standard deviation of the reported p-value is 0.01275
  at `threads=1` and 0.02764 at `threads=4`; converting to an effective sample size
  p(1−p)/var gives **1068** and **270** against a nominal 1000 iterations.

**Who is exposed.** `threads` defaults to 4 in all three methods, and the tutorial notebooks pass
5 (`T1_Method1`, `T1_Method2`) and 25 (`T1_Method3`); one cohort paper's quoted command uses 40.
A user who asks for 1000 iterations on 25 threads gets a null of about 40 distinct permutations.
The `debug_seed` docstring already warns the seed only works single-threaded
(`cpdb_statistical_analysis_method.py:59-61`), but nothing says the *number of permutations* is
divided by the thread count.

**Version scope.** The `Pool(processes=threads)` + global-`np.random.shuffle` structure is
present in `v2.1.7`, `v3.1.0`, `v4.0.0`, `v5.0.0` and master (read at each tag); the duplication
was **executed on master/5.0.1 only**. Platform-dependent: it needs `fork` (Linux default, and
the default on macOS before 3.8). Under `spawn` each worker seeds itself independently and the
duplication does not occur — so this changes results between operating systems as well as
between thread counts.

**Fix shape.** Give each task its own seeded generator, e.g. pass the iteration number into
`_statistical_analysis` (it already receives it, unused) and use
`np.random.default_rng(seed_seq.spawn(...))` per iteration, or seed the worker in a `Pool`
initializer from a `SeedSequence`. Either makes the result independent of `threads` and lets
`debug_seed` work in parallel, which would also close the standing request behind the
`threads=1` workaround comment.

### CPDB2 — CONFIRMED on every release from v2.1.7 to master (executed on each): the p-value counts only permutations *strictly greater* than the observed mean, discards ties, and can be 0

**Code.** `shuffled_greater_than_real` (`helper.py:537-539`) and `build_percent_result`
(`helper.py:611-613`):

```python
return np.packbits(shuffled_mean_analysis.values > real_mean_analysis.values, axis=None)
...
percent_result += np.unpackbits(statistical_mean, axis=None)[:result_size].reshape(result_shape)
percent_result /= len(statistical_mean_analysis)
```

so p = #{shuffles with mean **>** observed} / iterations. The documentation states the rule twice,
both times inclusively:

- `docs/RESULTS-DOCUMENTATION.md:62` — "the proportion of the means that are **as high as or
  higher** than the actual mean";
- `docs/RESULTS-DOCUMENTATION.md:104` — "By calculating the proportion of the means which are
  **equal or higher** than the actual mean".

This is also the estimator of the CellPhoneDB v2 protocol paper. The observed labelling is itself
one of the permutations and always ties with itself, so the documented rule has a floor of
1/(number of assignments) and the standard permutation correction (b+1)/(m+1) has a floor of
1/(iterations+1); the shipped rule has no floor.

**Verified** (`../verify/cpdb2_pvalue_ties_and_zero.py`). The fixture is 9 cells in three groups
of three, so the **entire null of 1680 label assignments was enumerated** — and enumerated
through the package's own `build_clusters` / `mean_analysis`, so the arithmetic (float32 means
from `numpy_groupies`, the complex minimum, the zero rule) is identical to a real run:

| quantity, over the 22 tested entries | value |
|---|---|
| tie mass #(mean == observed)/1680 | min 0.0006, **median 0.0345**, max **0.2024** |
| entries whose call at `pvalue <= 0.05` differs between the two rules | **3 of 22** |
| a real 20,000-iteration run vs the exact strict-rule p | max difference 0.0040 (2 × binomial se = 0.0141) |
| the same run vs the exact documented p | max difference **0.2038** |

so the run estimates the strict quantity: the gap is the estimand, not Monte-Carlo noise. The
three flips all go the same way — e.g. `LIG1_REC1` in `CTA|CTA` has documented p = 0.0833 (not
significant) and shipped p = 0.0119 (significant). One entry is reported as **p = 0** where the
exact documented p is 0.0006.

**On real data**, using the repository's own endometrium example (1,949 cells, 20 cell types)
and the repository's v5.0.0 database at the documented defaults (`iterations=1000`,
`threshold=0.1`, `pvalue=0.05`), `../verify/realdata_endometrium.py`: of the 39,444 entries of
the 1,671 × 400 p-value matrix that are not forced to 1, **16,821 (42.6 %) are reported as
exactly 0** (`threads=1`; 18,273, 47.3 %, at `threads=4`). Downstream plotting of −log10(p) —
which is what the project's recommended `ktplots`/`ktplotspy` dot plots draw — turns those into
infinities.

**Arithmetic footnote.** Cluster means are float32 (`counts_preprocessor` casts to float32,
`npg.aggregate` returns float32), so permutations that are mathematically tied with the observed
value can fall on either side of the strict comparison through ~1e-7 of rounding. On the fixture
the exact-arithmetic tie mass has median 0.0458 against 0.0345 as the float32 comparison sees it:
part of the tied mass is already being split arbitrarily before the strict-vs-inclusive question
arises.

**Version scope, executed** (`../verify/version_scope_pvalue_rule.py`; each tag's own
`cpdb_statistical_analysis_helper.py` checked out and driven with identical synthetic input —
one draw above, two equal, one below, and a second pair with none above and three equal):

| tag | p (1 above, 2 equal, 1 below) | p (0 above, 3 equal, 1 below) | documented |
|---|---|---|---|
| v2.1.7, v3.1.0, v4.0.0, v5.0.0, v5.0.1, master | 0.25 | **0.00** | 0.75 / 0.75 |

In every release the second interaction is called significant at 0.05 with no null draw above it.
v2.1.7 accumulates with an explicit `if mean > real_mean` loop; v3.1.0 onward use the packbits
form. The cohort names v2 (7 papers), v3 (2), v4 (1) and v5 (2).

**Fix shape.** `>=` in `shuffled_greater_than_real` matches the documentation; the standard
(b+1)/(m+1) also removes p = 0 and is what a permutation test should report at finite
`iterations`. Both change published numbers, so this needs the maintainers' decision, not a
silent patch — and the tie-splitting by float32 means a float64 comparison (or comparing on the
sums rather than the means) should be considered at the same time.

### CPDB3 — CONFIRMED on master and 5.0.1 (and by reading in v4.0.0): in METHOD 1 the `threshold` argument changes nothing in any output

**Code.** `cpdb_analysis_method.call` computes the percent analysis (line 134-138) and passes it
to `build_results`, which uses it — and only it — to build `significant_means`
(`cpdb_analysis_method.py:240-242`). The returned dict is then assembled from three keys
(lines 175-177):

```python
analysis_result['means_result'] = means_result
analysis_result['deconvoluted'] = deconvoluted_result
analysis_result['deconvoluted_percents'] = deconvoluted_percents
```

`significant_means` is used for a rank sort (lines 171-173) and dropped.
`file_utils.save_dfs_as_tsv` (line 184) writes exactly the keys of that dict, so no thresholded
file is written either.

The documentation for this method says the opposite, twice:

- `docs/RESULTS-DOCUMENTATION.md:59` — "CellphoneDB will report the means only if all the gene
  members of the interactions are expressed by at least a fraction of cells in a cell type
  (`threshold`). If the condition `threshold` is not met, the interaction will be ignored in the
  corresponding cell type pairs."
- `docs/RESULTS-DOCUMENTATION.md:78` — "Only interactions involving receptors and ligands
  expressed by more than a fraction of the cells (`threshold` default is 0.1, which is 10%) in
  the specific cluster are included."

**Verified** (`../verify/cpdb3_method1_threshold_ignored.py`): METHOD 1 run at `threshold=0.1`
and at `threshold=0.99` on the same data writes three files, **all three byte-identical**
(`filecmp.cmp(..., shallow=False)`), and `means_result` differs by 0.0e+00. 14 of the 36 cells of
that means table carry a non-zero mean that the documented threshold rule excludes. For contrast,
METHOD 2 on the same data keeps 9 significant entries at `threshold=0.1` and 6 at `threshold=0.99`
— the parameter works there, because METHOD 2 returns and writes `significant_means`.

**Version scope.** v3.1.0 still returned `significant_means` to the caller
(`cpdb_analysis_method.py:150` at that tag). v4.0.0 already dropped it (line 164: returns
`means_result, deconvoluted_result`, and saves only those two). So this is a v4-era regression,
present in v4.0.0, v5.0.0, v5.0.1 and master; **executed on master/5.0.1**. One cohort paper
states it ran `cpdb_analysis_method.call` (in v4.0.0).

**Fix shape.** Either add `significant_means` to the returned dict (restoring the documented
behaviour and the file), or state in the docstring and the METHOD 1 documentation that
`threshold` has no effect on this method's output. The first is a two-line change; it adds a file
to METHOD 1's output, which is a behaviour change worth an issue first.

### CPDB4 — CONFIRMED on master and 5.0.1 (and by reading back to v3.1.0): every subunit row of a complex in `deconvoluted.txt` carries the complex's minimum, not that subunit's own mean

**Code.** `deconvolute_complex_interaction_component`
(`cpdb_statistical_analysis_complex_method.py:366-371`) fills each subunit row's `multidata_id`
from the **complex** while filling `gene_name` from the **subunit**:

```python
deconvoluted_result[
    ['multidata_id', 'protein_name', 'gene_name', 'name', 'is_complex', 'id_cp_interaction',
     'receptor', 'complex_name']] = \
    deconvolution_complex[
        ['complex_multidata_id', 'protein_name_simple', 'gene_name_simple', 'name_simple', ...]]
```

and `deconvoluted_complex_result_build` (lines 292-304) then indexes by `multidata_id` and joins
the per-cluster tables, which hold one row per complex containing the minimum over its subunits
(`build_clusters`, `helper.py:154-159`):

```python
deconvoluted_result.set_index('multidata_id', inplace=True, drop=True)
deconvoluted_result = pd.concat([deconvoluted_result,
                                 clusters_means.reindex(deconvoluted_result.index)], ...)
```

The documented meaning of those columns (`docs/RESULTS-DOCUMENTATION.md:287`) is "mean: Mean
expression of the corresponding gene in each cluster", with `gene_name` being "one of the
subunits"; the percentages file "denotes the percentage of cells expressing a given gene"
(line 255). The file's stated purpose (line 254) is precisely to let a reader check heteromers —
"multiple molecules have to be expressed in the same cluster in order for the interacting partner
to be functional" — which it cannot do when every subunit shows the same number.

**Verified** (`../verify/cpdb4_deconvoluted_complex_subunits.py`), on the fixture where
`RECCPLX = SUB1 + SUB2` and `BIGCPLX = REC1 + SUB1 + SUB2 + LIG2`:

| gene | complex | reported (CTA, CTB, CTC) | the gene's own mean |
|---|---|---|---|
| SUB1 | RECCPLX | 1.0, **1.0**, 0.667 | 1.0, **3.0**, 0.667 |
| SUB2 | RECCPLX | 1.0, 1.0, **0.667** | 2.0, 1.0, **2.0** |
| REC1 | BIGCPLX | **0.0**, 1.0, 0.333 | **0.333**, 2.0, 0.333 |
| SUB1 | BIGCPLX | 0.0, 1.0, 0.333 | 1.0, 3.0, 0.667 |
| SUB2 | BIGCPLX | 0.0, 1.0, 0.333 | 2.0, 1.0, 2.0 |
| LIG2 | BIGCPLX | 0.0, 1.0, 0.333 | 0.0, 2.0, 4.0 |

6 of 6 subunit rows report a mean that is not the gene's mean, and the same 6 rows in
`deconvoluted_percents.txt` report the complex's minimum percentage. All simple (non-complex)
rows are correct — checked programmatically in the same harness. A reader asking "is SUB1
expressed in CTB?" is shown 1.0, which is SUB2's value.

**Version scope.** The same two lines are present at `v3.1.0`, `v4.0.0`, `v5.0.0` and master
(read at each tag); **executed on master/5.0.1**. (`deconvoluted_percents` itself is new in v5.)

**Fix shape.** Carry the subunit's `protein_multidata_id` in a separate column and join the
per-gene tables on that for complex rows, keeping `complex_name` for grouping. This changes the
numbers in a published output file, so it needs an issue first.

### CPDB5 — CONFIRMED on master, 5.0.1 and v5.0.0: `threads=1` with `iterations <= 50` raises `ZeroDivisionError`

**Code.** The single-threaded branch of `shuffled_analysis` (`helper.py:479, 490`):

```python
progress_step = round(iterations / 100, 0)
for i in range(iterations):
    ...
    if i % progress_step == 0:
```

`round(iterations/100, 0)` is `0.0` for every `iterations <= 50` (0.5 rounds to 0 under banker's
rounding), and the modulus raises before any result is produced.

**Verified** (`../verify/cpdb5_iterations_le_50_crash.py`), complete traceback captured:
`iterations=10, threads=1` raises `ZeroDivisionError: float modulo` at `helper.py:490`;
`iterations=10, threads=4` completes; `iterations=51, threads=1` completes. The boundary is
mapped arithmetically for 1 … 1000.

This is not an exotic path: the comment immediately above the branch
(`helper.py:476-478`) recommends `threads=1` as the only working option when the package is
driven from R/RStudio on Windows, citing issue #102 — and a first quick run with a small
`iterations` is the natural thing to do there. **Version scope:** the `threads == 1` branch was
introduced in v5.0.0 (v4.0.0 has no such branch), so v5.0.0, v5.0.1 and master.

**Fix shape.** `progress_step = max(1, round(iterations / 100))`, or guard the modulus. One line,
no numerical effect — the cleanest thing in this report to file.

### CPDB6 — CONFIRMED on master and 5.0.1 with pandas >= 3: `score_interactions=True` fails with an unrelated-looking `ValueError`

**Code.** `heteromer_geometric_expression_per_cell_type` (`scoring_utils.py:135-140`) rewrites
the matrix index from multidata ids to gene names with a chained inplace assignment:

```python
if matrix.index.intersection(genes[counts_data]).empty:
    index_name = matrix.index.name
    matrix = matrix.reset_index()
    matrix[index_name].replace(to_replace=id2name, inplace=True)   # operates on a temporary
    matrix.set_index(index_name, inplace=True)
```

`matrix[index_name]` is a new Series; under copy-on-write (opt-in in pandas 2.x, the only
behaviour in 3.0) the inplace write is discarded and pandas raises `ChainedAssignmentError` as a
warning. The index therefore stays integer, the next line
`idx = [gene in list(genes[counts_data]) for gene in matrix.index]` selects nothing, and the
empty frame reaches `scale_expression` (line 207), where `MinMaxScaler.fit` raises
**`ValueError: at least one array or dtype is required`** — an error naming neither the scoring
step nor the cause.

**Verified** (`../verify/cpdb6_scoring_crashes_pandas3.py`, run in two venvs, both outputs in the
`.out`):

| environment | `df['i'].replace(..., inplace=True)` takes effect | `score_interactions=True` |
|---|---|---|
| pandas 3.0.5 | **False** | **ValueError** (full traceback captured) |
| pandas 2.3.3 | True | completes, 14 non-zero score entries |

The same harness calls `heteromer_geometric_expression_per_cell_type` in isolation: 5 input rows
in, **0 rows out** under pandas 3, where 5 genes + 2 complexes are expected.

`pyproject.toml` requires only `pandas = ">=1.5.0"`, so a fresh `pip install cellphonedb` today
resolves pandas 3.x and the v5 headline feature ("A scoring methodology to rank interaction based
on the expression specificity of the interacting partners", `README.md`) cannot run. All three
tutorial notebooks pass `score_interactions=True`. The project's CI
(`.github/workflows/python-app.yml`) pins Python 3.8, which cannot install pandas 3, so
`test_basic_method` — which passes `score_interactions=True` — still passes there.

**Fix shape.** `matrix[index_name] = matrix[index_name].replace(to_replace=id2name)` (one line,
correct on every pandas version), and a floor on the pandas requirement or a CI job on a current
Python. Note that `scoring_utils.py:138` is not the only chained-inplace call in the file —
`interactions_df.replace(to_replace=id2name, inplace=True)` (line 273) operates on a DataFrame
and is fine.

## Notes

### N1 — `result_precision` does not apply to `pvalues.txt`

`build_results` rounds the means (line 219) and the significant means (lines 191, 220), but
`result_percent` is concatenated unrounded (line 229). With an `iterations` that is not a power
of ten the p-value column carries the full float repr: at `iterations=300, result_precision=3`
the written file contains 18-digit values such as `0.006666666666666667`, while the means file
holds 3 (`../verify/note_pvalue_precision_cutoff.py`). The parameter is documented as "Number of
decimal digits in results." Users have asked about p-value precision more than once (issues #60,
#24, #155); the maintainers' replies are not readable from this environment (see `../README.md`).

### N2 — the significance cut-off is inclusive, not strict

`get_significant_means` masks with `result_percent > min_significant_mean` (`helper.py:72`), so an
interaction whose p-value is exactly `pvalue` is kept. Executed at the boundary: p = 0.049 kept,
p = 0.050 **kept**, p = 0.051 dropped. Both the docstring ("A p-value below which a
ligand/receptor expression mean is considered to be statistically significant",
`cpdb_statistical_analysis_method.py:64-66`) and `docs/RESULTS-DOCUMENTATION.md:273` ("If
p.value < 0.05, the value will be the mean") describe a strict comparison. p == 0.05 exactly is
reachable — 50 exceedances out of the default 1000 iterations. Minor, and it errs towards keeping
interactions.

### N3 — `pvalue=0` silently inverts the filter

The same line is guarded by `if min_significant_mean:` (`helper.py:71`), and `0.0` is falsy, so
the function takes its non-statistical branch, `mask = result_percent == 0`. Executed: the same
analysis run with `pvalue=0.0` keeps **34 of 36** entries in `significant_means`, 13 of them with
p-value 1.0, and drops the one entry whose p-value is 0 — the exact opposite of the request. With
`pvalue=0.05` the same run keeps 9. A user sweeping cut-offs, or scripting `pvalue=0` to mean
"nothing passes", gets a full table of non-significant interactions with no warning.

### N4 — the scoring filter and the significance filter disagree on the boundary

`filter_genes_per_cell_type` zeroes a gene when `gene_expr_pct < min_pct_cell`
(`scoring_utils.py:52`), keeping a gene whose percentage equals the threshold exactly, while
`percent_analysis` requires `pct > threshold` (`helper.py:453`) and rejects it. Executed on a
12-cell fixture where LIG1 sits at exactly 0.50 with `threshold=0.5`
(`../verify/note_scoring_pipeline.py`): `LIG1_REC1` in `CTA|CTB` gets p-value 1.0 and
`significant_mean = NaN`, and `interaction_score = 25.0`. One `threshold` argument, two
answers to "is this gene expressed here". Cosmetic in most runs (an exact tie needs a round
percentage) but trivially fixable by using the same comparison in both places.

### N5 — duplicate gene rows are averaged, not summed or maxed (by reading; not executed)

`add_multidata_and_means_to_counts` ends with `counts = counts.groupby(counts.index).mean()`
(`helper.py:789`), so when several rows of the user's matrix map to the same
`id_multidata` — two Ensembl ids for one UniProt accession, or a duplicated gene symbol — the
gene's expression becomes the **mean across those rows**. A protein whose second transcript is
undetected therefore enters the analysis at half its measured expression, in both the mean and
(via the averaged row) the percent. The docstring says "calculates the means grouped by
id_multidata", so the behaviour is stated; the consequence is not, and a maximum or a sum would
be the more usual choice. Recorded as a design note because it was not executed.

### N6 — `db_utils.create_db` crashes when a `uniprot_N` column of `complex_input.csv` is entirely empty

`sanity_test_report_unknown_proteins` (`db_utils.py:597-608`) merges the complex table against the
protein table once per subunit column. If no complex in the file fills, say, `uniprot_4`, pandas
reads that column as all-NaN float64 and refuses to merge it against the string `uniprot` column:
`ValueError: You are trying to merge on float64 and str columns for key 'uniprot_4'`. Building a
custom database — the documented `notebooks/T0_BuildDBfromFiles.ipynb` workflow — therefore fails
whenever every complex has fewer subunits than the widest column in the header, which is the
normal case for a small hand-made file. **Verified**
(`../verify/note_create_db_empty_uniprot_column.py`, full traceback captured): a
`complex_input.csv` containing one dimer raises; the same file plus one four-subunit complex
builds successfully. The message names a column of the user's input, so it is diagnosable, but it
comes from a sanity test whose purpose is to warn about unknown proteins, and no unknown protein
is involved. A dtype-safe merge (skip all-NaN columns, or compare as strings) fixes it. This
audit's own fixture had to carry a four-subunit complex for exactly this reason.

## What held up (executed, not just read)

`../verify/heldup_reference_vs_shipped.py` reimplements the documented method in plain numpy and
compares **every number** the shipped statistical pipeline produces on the 9-cell fixture. All of
the following matched:

- **Cluster means** are the plain mean over all the cluster's cells, zeros included
  (`npg.aggregate(codes, counts.values, func='mean')`, `helper.py:139`) — asserted against a
  hand-written table, not just against my port.
- **Percents** are computed per gene on `counts > 0` (`helper.py:145`), i.e. the fraction of the
  cluster's cells with any non-zero value, and are computed only for the real data
  (`skip_percent=True` in the shuffles), which is correct for this test.
- **Complexes are summarised by the minimum over subunits, taken *after* the per-subunit cluster
  means** (`helper.py:154-159`) — the order the documentation describes. The percent of a complex
  is likewise the minimum of its subunits' percents, which is the documented "all subunits of the
  complex are expressed by a proportion of cells (`threshold`)" requirement.
- **The interaction mean** is `(x > 0) * (y > 0) * (x + y) / 2` (`helper.py:357-360`): the mean of
  the two cluster means, forced to 0 when either side's cluster mean is exactly 0 — note this
  zeroing is on the *mean*, not on the percent threshold. Shipped vs reference: max difference
  5.5e-8 (float32).
- **The threshold rule** is `((x > threshold) * (y > threshold))` (`helper.py:452-455`), applied
  per interaction and cluster pair, with the complex handled through its minimum percent.
- **The p-value rule** — p = #(shuffled > observed)/iterations with p forced to 1 where the
  observed mean is 0 or the threshold flag is 0 (`helper.py:615-617`) — reproduced **exactly**
  (`max |difference| = 0`) on a continuous fixture over the 200 shuffles the package actually
  drew (recorded by wrapping `shuffle_meta`, so no assumption about the RNG stream is needed).
  Ties are the subject of CPDB2; the counting rule itself is as described here.
- **`significant_means`** is the mean where p <= `pvalue` and NaN otherwise, and **`rank`** is the
  count of non-NaN entries divided by the number of cluster-pair columns, rounded to 3
  (`helper.py:651-654`): identical to the reference, including the rank values.
- **Rounding happens after the comparisons.** `significant_means` is built from the unrounded
  means and p-values and rounded afterwards (`complex_method.py:189-191`), so `result_precision`
  cannot move an interaction across the cut-off.
- **The shuffle is over cell labels, with cluster sizes preserved** (`np.random.shuffle` on the
  `cell_type` column, `helper.py:96`), which is the documented "randomly permuting the cluster
  labels of all cells"; it is drawn afresh from the original labels each iteration, not
  cumulatively.
- **Self-interactions** (`cluster1|cluster1`) are included as ordinary columns
  (`get_cluster_combinations`, `helper.py:257-259`, uses the full product including the diagonal)
  and get the same treatment in the null; nothing special-cases them, and nothing needs to.
- **`microenvs`** restricts only which cluster pairs are tested
  (`helper.py:260-267`: pairs within each microenvironment, deduplicated), while the permutation
  still shuffles labels across all cells — the documented behaviour ("restrict the cell type
  interacting pairs to those sharing a microenviroment"). The scoring module likewise scales
  across all cell types and applies microenvironments only at the final product, as
  `docs/RESULTS-DOCUMENTATION.md:196` states.
- **The v5 scoring protocol** reproduces its five documented steps exactly
  (`../verify/note_scoring_pipeline.py`, max difference **0.000** against an independent port):
  per-cell-type filtering, per-cell-type mean, **geometric** mean over subunits for heteromers,
  MinMax rescaling to 0–10 per gene across cell types, and the product of the two scaled values.
  The geometric mean here differs deliberately from the minimum used by the inference methods;
  both the code comment (`scoring_utils.py:158-160`) and the docs say so. The rescaling makes the
  lowest-expressing cell type of every gene score exactly 0, which the documentation also warns
  about.
- **The DEG method.** `degs_analysis` marks an interaction relevant when **either** partner is a
  DEG in its cluster (`((x + y) > 0)`, `cpdb_degs_analysis_method.py:483-486`), and
  `relevant_interactions` is that AND the percent threshold
  (`real_percents_analysis.values & real_degs_analysis.values`, lines 175-177) — exactly the two
  documented criteria. A complex counts as a DEG if any subunit is (`max` over subunits,
  lines 425-431), which is the natural reading of the documentation but is not stated there.
- **`get_significant_means` for the non-statistical methods** uses the `result_percent == 0`
  branch (`helper.py:73-74`), i.e. the threshold/relevance flag rather than a p-value, as its
  docstring says.

## Not checked here

`utils/search_utils.py` (result querying), `src/core/utils/cellsign.py` (the CellSign TF module
beyond reading its call sites), `db_utils.create_db` sanity tests beyond using them,
the `Subsampler` (geometric sketching, which delegates to `geosketch`/`fbpca`),
`generate_input_files*.py`, the plotting notebooks and `ktplotspy`, and the CellphoneDBViz
web components. The database *content* (which interactions are curated, and the v5 directionality
annotation) is out of scope: this review covers only the code that turns a counts matrix and a
database into numbers.
