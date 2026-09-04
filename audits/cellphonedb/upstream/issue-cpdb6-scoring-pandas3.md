Title: `score_interactions=True` fails on pandas >= 3 with "ValueError: at least one array or dtype is required"

<!-- ventolab/CellphoneDB has no issue template; this follows the structure of a minimal
     complete verifiable example. -->

**Version:** 5.0.1 (PyPI wheel and `master` @ `dc8abd15`, byte-identical), Python 3.12,
**pandas 3.0.5**. Works on pandas 2.3.3.

### Summary

Scoring dies for every input on pandas 3 (and on pandas 2 with
`pd.options.mode.copy_on_write = True`). Since `pyproject.toml` requires only
`pandas = ">=1.5.0"`, a fresh `pip install cellphonedb` now resolves pandas 3.x, and
`score_interactions=True` — the v5 headline feature, enabled in all three tutorial notebooks —
cannot run. CI does not catch it because `.github/workflows/python-app.yml` pins Python 3.8,
which cannot install pandas 3, so `test_basic_method` still passes there.

The error message names neither the scoring step nor the cause:

```
  File ".../cellphonedb/src/core/methods/cpdb_statistical_analysis_method.py", line 157, in call
    interaction_scores = scoring_utils.score_interactions_based_on_participant_expressions_product(
  File ".../cellphonedb/utils/scoring_utils.py", line 343, in score_interactions_based_on_participant_expressions_product
    cpdb_fms = scale_expression(cpdb_fmsh,
  File ".../cellphonedb/utils/scoring_utils.py", line 207, in scale_expression
    scaler = MinMaxScaler(feature_range=(0, upper_range), clip=True).fit(matrix.T)
  ...
  File ".../sklearn/utils/validation.py", line 922, in check_array
    dtype_orig = np.result_type(*dtypes_orig)
ValueError: at least one array or dtype is required
```

### Cause

`heteromer_geometric_expression_per_cell_type` (`scoring_utils.py:135-140`) rewrites the index
from multidata ids to gene names with a chained inplace assignment:

```python
if matrix.index.intersection(genes[counts_data]).empty:
    index_name = matrix.index.name
    matrix = matrix.reset_index()
    matrix[index_name].replace(to_replace=id2name, inplace=True)   # mutates a temporary
    matrix.set_index(index_name, inplace=True)
```

`matrix[index_name]` is a new Series; under copy-on-write the inplace write is discarded (pandas
raises `ChainedAssignmentError` as a warning pointing at exactly this line). The index therefore
stays integer, so the next line

```python
idx = [gene in list(genes[counts_data]) for gene in matrix.index]
```

selects nothing, every gene and complex is dropped, and the empty frame reaches
`scale_expression`, where `MinMaxScaler.fit` raises.

### Minimal reproduction (no database, no counts file)

```python
import pandas as pd
from cellphonedb.utils import scoring_utils

genes = pd.DataFrame({'gene_name': ['LIG1', 'REC1', 'SUB1', 'SUB2'], 'protein_id': [0, 1, 2, 3]})
complex_composition = pd.DataFrame({'complex_multidata_id': [4, 4], 'protein_multidata_id': [2, 3]})
complex_expanded = pd.DataFrame({'complex_multidata_id': [4], 'name': ['RECCPLX']})
id2name = {0: 'LIG1', 1: 'REC1', 2: 'SUB1', 3: 'SUB2', 4: 'RECCPLX'}
matrix = pd.DataFrame({'ctA': [1.0, 2.0, 4.0, 1.0], 'ctB': [3.0, 1.0, 2.0, 2.0]},
                      index=pd.Index([0, 1, 2, 3], name='id_multidata'))

out = scoring_utils.heteromer_geometric_expression_per_cell_type(
    matrix=matrix, counts_data='gene_name', genes=genes,
    complex_composition=complex_composition, complex_expanded=complex_expanded, id2name=id2name)
print("rows in:", len(matrix), " rows out:", len(out), " index:", list(out.index))
assert len(out) == 5, "expected 4 genes + 1 complex, got %d rows" % len(out)
```

**Output (pandas 3.0.5)**

```
.../cellphonedb/utils/scoring_utils.py:138: ChainedAssignmentError: A value is being set on a copy
of a DataFrame or Series through chained assignment using an inplace method.
Such inplace method never works to update the original DataFrame or Series, because the
intermediate object on which we are setting values always behaves as a copy (due to Copy-on-Write).
  matrix[index_name].replace(to_replace=id2name, inplace=True)
rows in: 4  rows out: 0  index: []
Traceback (most recent call last):
  File "repro_cpdb6.py", line 13, in <module>
    assert len(out) == 5, "expected 4 genes + 1 complex, got %d rows" % len(out)
           ^^^^^^^^^^^^^
AssertionError: expected 4 genes + 1 complex, got 0 rows
```

**Expected:** 5 rows (LIG1, REC1, SUB1, SUB2 and the complex RECCPLX). **Got:** 0 rows on pandas
3.0.5; the same script prints 5 rows on pandas 2.3.3.

*What shrinking the example revealed:* the counts matrix, the database and the whole analysis are
irrelevant — the function fails on four hand-built rows, which is what isolated the index rewrite
from the geometric-mean and scaling steps that the traceback pointed at. Running the identical
script under pandas 2.3.3 and 3.0.5 confirmed the boundary is the pandas version, not the input.
The neighbouring `interactions_df.replace(to_replace=id2name, inplace=True)`
(`scoring_utils.py:273`) is fine, because it operates on a DataFrame rather than a column.

### Suggested fix

```python
matrix[index_name] = matrix[index_name].replace(to_replace=id2name)
```

correct on every pandas version. **A patch with a regression test is attached in the PR** (the
test drives the function on the hand-built tables above and needs no database download; it fails
on unpatched master under pandas 3 and passes with the fix). It would also be worth adding a CI
job on a current Python so that pandas 3 is exercised, and/or capping/raising the pandas
requirement in `pyproject.toml`.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses:
https://github.com/cindykrafft/mytochondria/tree/main/audits/cellphonedb)

---
_Generated by [Claude Code](https://claude.ai/code)_
