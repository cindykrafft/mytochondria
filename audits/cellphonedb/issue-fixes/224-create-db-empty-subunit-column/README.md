**Filed 2026-09-04 as PR #232** (issue #224; comment posted on the issue).

# Issue fix: #224 — `create_db` fails when a `uniprot_N` column of `complex_input.csv` is unused

_Prepared 2026-09-03 against `ventolab/CellphoneDB` `master` @ `dc8abd15` (version string 5.0.1), in a
Python 3.12 venv with the clone installed editable, pandas 2.3.3 / numpy 2.5.2. Nothing has been
filed or pushed; the branch `fix/issue-224-create-db-empty-subunit-column` (one commit, `98184df`,
on top of `dc8abd15`) exists only in the scratch clone and as `0001-*.patch` here._

## The issue

**[#224 "problems in build database by files"](https://github.com/ventolab/CellphoneDB/issues/224)**,
opened 2025-10-19, 0 comments, unlabelled, unassigned (the same traceback was reported in #137 in 2023, closed). The reporter followed the official
`T0_BuildDBfromFiles` notebook with the six input files (`interaction_input.csv`, `gene_input.csv`,
`complex_input.csv`, `protein_input.csv`, `transcription_factor_input.csv`,
`sources/uniprot_synonyms.tsv`) and `db_utils.create_db()` raised

    ValueError: You are trying to merge on float64 and object columns. If you wish to proceed you should use pd.concat

They had already tried converting every `uniprot` column to strings, checking for NaN and
`.fillna('')`, "despite these changes, the error persists". The issue body does not include the
traceback or the files; the comments (0) add nothing.

## Diagnosis (line numbers on `dc8abd15`)

- `create_db` (`cellphonedb/utils/db_utils.py:281`) reads the four CSVs with plain
  `pd.read_csv` (`get_dfs`, `db_utils.py:461-469`, via `file_utils.read_data_table_from_file`,
  `file_utils.py:20`) — no `dtype` is given, so pandas infers each column.
- It then calls `run_sanity_tests` (`db_utils.py:316`), whose step 9 is
  `sanity_test_report_unknown_proteins` (`db_utils.py:597-608`, called at `:687`). That function
  merges the complex table against the protein table once per subunit column:

      for col in protein_column_names:                       # uniprot_1 .. uniprot_4 (+ uniprot_5 if present)
          aux_df = pd.merge(complex_db_df, protein_db_df, left_on=col, right_on='uniprot', how='outer')   # :603

- If **no complex in the file fills one of the `uniprot_N` columns present in the header**, pandas
  reads that column as all-NaN `float64`, and `pd.merge` refuses to join it against the string
  `uniprot` column: `ValueError: You are trying to merge on float64 and object columns for key
  'uniprot_3'` (pandas 2; "float64 and str" on pandas 3). The reporter's message is this one with
  the key name elided.
- This is the normal shape of a custom database: the released `complex_input.csv` (v5.0.0,
  `ventolab/cellphonedb-data` @ `71ffa8a`) has columns `uniprot_1..uniprot_5`; of its 362 complexes
  only **4 use `uniprot_4` and 1 uses `uniprot_5`**. Any subset that drops those five rows — or any
  hand-written file that keeps the documented header while its complexes are dimers — cannot be
  built. Converting the columns to strings before saving, as the reporter did, cannot help,
  because `create_db` re-reads the CSVs and pandas infers `float64` again. The project had noted the
  same crash as N6 (`../../verify/note_create_db_empty_uniprot_column.py`) without connecting it to
  a user report.
- Every other consumer of those columns already tolerates NaN floats
  (`isinstance(x, str)` filters at `db_utils.py:365,371`, `str(i) != 'nan'` at `:498`, set
  differences at `:570`), so the merge is the only failing site.

## Fix (`0001-fix-build-the-database-when-a-uniprot_N-column-of-co.patch`)

`sanity_test_report_unknown_proteins` now takes the non-empty accessions of each subunit column
and reports those absent from `protein_input.csv`:

```python
    known_proteins = set(protein_db_df['uniprot'].tolist())
    for col in protein_column_names:
        complex_proteins = set(complex_db_df[col].dropna().tolist())
        unknown_proteins = unknown_proteins.union(complex_proteins - known_proteins)
```

That is exactly the set the outer merge computed (`uniprot` null and `uniprot_N` not null), with no
dependence on the column dtype; the warning text is untouched. Diff: `db_utils.py` +6/−3,
`method_tests.py` +61 (test only). No analysis result can change: the function only prints.

**Equivalence on real data.** With the released v5.0.0 input files loaded through `get_dfs`, the
master function (loaded from `git show master:cellphonedb/utils/db_utils.py`) and the fixed one
print identical output — nothing as-is, and the identical two-line warning when `P05556` (ITGB1)
and `P08514` (ITGA2B) are removed from `protein_input.csv` (`equivalence_realdata.out` in the
scratch `work/`; summarised in `pr-body.md`).

## Reproduction (`repro.py`)

Hand-written `gene/protein/complex/interaction_input.csv` (3 proteins, 1 dimer complex, 1
interaction) with the standard four-column complex header; no download. Run from the venv.

`repro.before.out` (master):

    complex_input.csv as read by pandas: {'uniprot_1': 'object', 'uniprot_2': 'object', 'uniprot_3': 'float64', 'uniprot_4': 'float64'}
    RESULT: create_db raised
      File ".../cellphonedb/utils/db_utils.py", line 603, in sanity_test_report_unknown_proteins
        aux_df = pd.merge(complex_db_df, protein_db_df, left_on=col, right_on='uniprot', how='outer')
    ValueError: You are trying to merge on float64 and object columns for key 'uniprot_3'. If you wish to proceed you should use pd.concat

`repro.after.out` (with the patch):

    Created /tmp/cpdb224_.../cellphonedb_09_03_2026_231752.zip successfully
    RESULT: created ['cellphonedb_09_03_2026_231752.zip']

## Tests

New `CreateDbUnitTests` in `cellphonedb/src/tests/method_tests.py` (the project's single test
file; a new `TestCase` with its own `setUp`, like the project's earlier patches, so it needs no
database download and can run in CI):

| | `-k CreateDbUnitTests` | full `pytest method_tests.py` |
|---|---|---|
| master `dc8abd15` (test file added, source unchanged) | **2 failed** (`ValueError` above, from both tests) | 4 failed, 2 passed |
| with the fix | **2 passed** | 4 failed, 4 passed |

The four failures are pre-existing and unrelated: `test_basic_method`, `test_statistical_method`
and `test_deg_method` open `../../../example_data/test.h5ad`, which on `master` is at
`example_data/test_data/test.h5ad` (the open PR #210 "this should fix the pytest workflow" fixes
the paths); `test_compare_downloaded_created_dbs` compares line counts against a downloaded zip.
To run the suite at all here (the v4.1.0 download returns HTTP 403), `test_data/downloaded_db/
cellphonedb.zip` and `test_data/generated_db/*` were pre-populated from a depth-1 clone of
`ventolab/cellphonedb-data` (v5.0.0 files), which is why the comparison test's counts differ.

**flake8**, both CI invocations, before and after: `--select=E9,F63,F7,F82` → 0;
`--exit-zero --max-complexity=10 --max-line-length=127` → 0. The patch applies to a clean
`master` with `git am` (checked in a throw-away worktree).

## Other candidates considered

All 65 open issues were listed (`is:open`, perPage 100, sorted by creation) and the bodies of the
21 that looked like defects were read; only the issue *bodies* are readable from this session, not
the comments, so "N comments" below is all that is known of the maintainers' replies. Open PRs:
only #227 (a `set_index` KeyError on ~500k-cell inputs) and #210 (test paths); neither touches
this.

- **#190 / #225 — `KeyError: 'COL11A1_integrin_a11b1_complex'` / `'BMP8A_ACVR_1A2B_receptor'` in
  `score_product`** (8 and 0 comments). Reproduced here on the project fixture with a **negative**
  subunit mean (`alt-190-225-scoring-keyerror-probe.py`, `.out`): both reported keys involve a
  complex, and the cause is `scoring_utils._geometric_mean` taking a fractional power of a
  negative subunit product (scaled / z-scored input, cf. #192) → NaN → `MinMaxScaler` keeps NaN →
  `DataFrame.stack()` in `_get_lr_scores` (`scoring_utils.py:225`) drops NaN cells on pandas < 3 →
  the pair is absent from `interacting_pair2score` → `KeyError` at `:293`. Not chosen: the input
  is arguably invalid (the method expects non-negative normalised counts) and the fix is a
  maintainer decision — report NaN scores (`stack(dropna=False)`, what both reporters ask for) or
  reject negative input with a clear message — and #190 has 8 unreadable comments that may already
  settle it. Worth a follow-up issue comment with this diagnosis either way.
- **#197 — `meta_preprocessor` rejects a metadata file in which every cell type has exactly one
  sample** (`num_unique_vals_in_first_col > num_unique_vals_in_second_col`,
  `method_preprocessors.py:41`; bulk data). Genuine, one-character (`>=`), body is enough. Not
  chosen: it is a heuristic for unlabelled columns and the equal case is ambiguous by construction;
  the documented column names avoid it.
- **#194 — means differ between `A|B` and `B|A`**: expected (partner_a is taken from the first
  cell type, partner_b from the second); not a bug. **#192** negative means: scaled input, not a
  bug. **#163 / #148 / #167**: outdated tutorial unpacking, a data-type problem behind screenshots,
  and the Windows `spawn` guard — environment or user error. **#158** version string: already
  5.0.1 on master.
- **#137** (closed 2023-08, "Error in generating costomize interaction database", 3 comments,
  retrieved on a second search) is **the same failure two years earlier**: a custom interaction set
  with a pseudo `complex_input.csv` whose `uniprot_N` columns are empty, and the identical traceback
  from the same `pd.merge` in the sanity test (then `run_sanity_tests`, `db_utils.py:433`):
  `ValueError: You are trying to merge on float64 and object columns`. Its closing comments are not
  readable from here; the code path is unchanged on `master`, so whatever was said there was a
  workaround, not a fix. The PR body cites it.

## Caveats

- The reporter's traceback is not in the issue, so the diagnosis rests on the message text (which
  is unique to `pd.merge` key coercion) and on the one merge in `create_db` whose key can be an
  all-NaN column; the other merges in `create_db` (`uniprot`, `protein_name`, `partner_a/b` vs
  `name`) join fully populated string columns and cannot produce it. Their attempted fix
  (stringifying the CSVs) is consistent with this: it has no effect on what `read_csv` infers.
- Alternative the maintainers might prefer: read the `uniprot_N` columns as strings in `get_dfs`
  (`dtype={...}` per DB version) so that every downstream user sees the same dtype. That is a
  wider change touching version-dependent column lists; the patch keeps the fix in the one
  function that failed.
- Not verified under pandas 3 in this session (the venv was pinned to pandas < 3 so that the
  scoring probe could run); the new code path uses only `dropna()` and set difference, which are
  dtype-agnostic, and the project's N6 harness shows the same crash on pandas 3.0.5.
