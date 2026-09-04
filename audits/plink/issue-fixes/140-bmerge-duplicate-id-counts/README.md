# PLINK 1.9 `--bmerge`: duplicate variant IDs are counted and warned about inconsistently (issue #140)

_Prepared 2026-09-03 against `chrchang/plink-ng` `master` @ `ff47b729` (2026-09-03, PLINK 1.9
version string `v1.9.0-b.8`). Fix branch `fix/issue-140-bmerge-duplicate-id-counts`, one
commit on top of `ff47b729`, exists only in the local scratch clone; nothing has been filed
or pushed._

## The issue

* **#140 — "Logging bug in bmerge"**, <https://github.com/chrchang/plink-ng/issues/140>,
  opened 2020-04-30 by **andrew-slater**, open, 2 comments (not readable from this session),
  no assignee.
* The reporter merged two small filesets with `--merge-mode 6` in both orders and got
  different numbers for the same file: `30 markers loaded from Plus.bim` / `29 markers to be
  merged from Normed.bim` in one direction, `27 markers loaded from Normed.bim` in the other,
  and different diff totals (`116 overlapping calls`, concordance 0.904762 vs `108`,
  0.897436). His data (`Report.zip`) is attached to the issue; GitHub attachments are not
  reachable from this session, so the reproduction below is synthetic and reproduces the same
  log shape.
* The maintainer's reply is not readable here, but his 2 May 2020 commit is: it added a
  duplicate-ID warning for the *first* fileset at `1.9/plink_data.c:16486`, with a comment
  naming this issue and leaving the rest as a todo — "also print this warning if the first
  fileset doesn't have a duplicate ID, but a later fileset does." That todo is what this fix
  implements, along with the count inconsistency the issue is titled after.

## Diagnosis (on `ff47b729`)

`--bmerge` keys the merge on variant ID: all records sharing an ID become one variant in the
merged fileset. `merge_datasets()` scans every fileset into one hash table
(`1.9/plink_data.c:16482`, `merge_bim_scan()` at `1.9/plink_data.c:14748`):

* `ullxx` (`tot_marker_ct`) counts **distinct IDs** across everything scanned so far, and is
  what `%u markers loaded from <base>.bim` prints (`1.9/plink_data.c:16508`);
* `cur_marker_ct` counts the **records** in the fileset just scanned, and is what
  `%u markers to be merged from <second>.bim` and the following
  `Of these, X are new, while Y are present in the base dataset` used
  (`1.9/plink_data.c:16509`, `:16513`).

So the same file is reported as N records when it is the second fileset and as M distinct IDs
when it is the base, and `Y = cur_marker_ct - new` can claim more variants are present in the
base dataset than the base dataset has.

The warning had the same asymmetry: its condition was `(!mlpos) && (ullxx != cur_marker_ct)`
(`1.9/plink_data.c:16486`), i.e. first fileset only. A later fileset's duplicate IDs cannot be
detected that way, because a repeated ID in fileset 2 is a hash hit exactly like an ID shared
with fileset 1 — `merge_bim_scan()` had no way to tell those apart, which is why the todo was
left standing.

**Fix** (`0001-1.9-bmerge-duplicate-ID-reporting-issue-140.patch`, 33 insertions / 8 deletions
in `1.9/plink_data.c`): each `Ll_bim` hash entry gains `last_fileset_idx` (in the spirit of
`Ll_fam::orig_order`), set on creation and updated on every match; a match against an entry
whose `last_fileset_idx` is already the current fileset is a within-fileset duplicate and is
counted into a new `cur_dup_ct` output. `merge_datasets()` then prints the warning for
whichever fileset has duplicates, naming it, and reports `cur_marker_ct - cur_dup_ct` for the
second fileset. Genotype output is untouched. The entry grows by 4 bytes, usually absorbed by
the 16-byte end-allocation rounding.

## Reproduction

`repro.sh` (`PLINK=<plink 1.9 binary> ./repro.sh`) writes two 3-sample filesets — `plus`
(4 records, 4 distinct IDs) and `normed` (4 records, 3 distinct IDs: `v2` twice) — and merges
them both ways with `--merge-mode 6` and with `--make-bed`.

Before (`repro.before.out`, master build of `ff47b729`):

```
=== --bfile plus --bmerge normed (--merge-mode 6) ===
4 markers loaded from plus.bim.
4 markers to be merged from normed.bim.            <- normed has 3 distinct IDs
Of these, 0 are new, while 4 are present in the base dataset.
                                                    (no duplicate-ID warning at all)
=== --bfile normed --bmerge plus (--merge-mode 6) ===
Warning: First fileset to be merged contains duplicate variant ID(s).  Variants
3 markers loaded from normed.bim.                  <- same file, different count
4 markers to be merged from plus.bim.
Of these, 1 is new, while 3 are present in the base dataset.
```

After (`repro.after.out`, patched build):

```
=== --bfile plus --bmerge normed (--merge-mode 6) ===
Warning: normed.bim contains duplicate variant ID(s).  Variants with matching
4 markers loaded from plus.bim.
3 markers to be merged from normed.bim.
Of these, 0 are new, while 3 are present in the base dataset.

=== --bfile normed --bmerge plus (--merge-mode 6) ===
Warning: normed.bim contains duplicate variant ID(s).  Variants with matching
3 markers loaded from normed.bim.
4 markers to be merged from plus.bim.
Of these, 1 is new, while 3 are present in the base dataset.
```

The merged fileset is the same 4 variants (`v1 v2 v3 v4`) in both directions, before and
after.

## Test and test results

New `2.0/Tests/TEST_BMERGE_DUP_IDS/run_tests.sh`, registered in `2.0/Tests/run_tests.sh`
(the suite the `PLINK2 functional tests` workflow runs on every PR, and which builds and
uses PLINK 1.9). It asserts the warning and both counts in each merge direction, that the
merged fileset has 4 variants either way, and that a duplicate-free pair produces no warning.
`1.9/tests/` has no unit-test target — its `tests.py` compares against a PLINK 1.07 build,
which is not available here — so this suite is where a 1.9 regression test can actually run.

| run | result |
|---|---|
| `2.0/Tests/run_tests.sh`, master 1.9 + master plink2 (before) | 9/9 pass (`tests_before.log`) |
| `2.0/Tests/run_tests.sh`, patched 1.9 + same plink2 (after) | 10/10 pass, including `TEST_BMERGE_DUP_IDS` |
| `TEST_BMERGE_DUP_IDS` alone, master 1.9 | **fails** at the first assertion (no duplicate-ID warning) |
| `TEST_BMERGE_DUP_IDS` alone, patched 1.9 | passes |
| build | clean, no new compiler warnings (`-Wall -O2`) |
| `git apply --check` / `git am` on `ff47b729` | OK |

Linter/formatter: the repository has no `clang-format`, editorconfig or other formatter
configuration (checked in the project's `upstream/README.md` and re-checked here), so the patch
follows the surrounding style (tabs at the existing indentation levels, braces on every `if`,
comments dated in the maintainer's `bugfix (date):` idiom).

Builds used: PLINK 1.9 `make ZLIB=-lz BLASFLAGS="<scratch>/plink/blas/lib/libopenblas.a -lm
-lpthread"` (LAPACK is needed for `--pca`, which `TEST_PHASED_VCF` exercises); PLINK 2.0
`2.0/build_dynamic` with the same OpenBLAS archive.

## Caveat / what this does not fix

With `--merge-mode 6` each *record* of the second fileset is still diffed against the base, so
the overlapping-call and concordance totals still depend on merge order when one fileset has
duplicate IDs (12 calls / 0.916667 vs 9 calls / 0.888889 on the reproduction; 116 / 0.904762
vs 108 / 0.897436 in the report). Making those symmetric would change what `--merge-mode 6`
counts, which is a semantics decision for the maintainer, so it is called out in the PR body
and the issue comment rather than patched. The reporter's own files could not be downloaded,
so the claim that his numbers have this same cause is inference from the log shape, not a
rerun of his data.

## Other candidates considered

The tracker has 35 open issues (enumerated in full on 2026-09-03 with
`mcp__github__search_issues`, `is:open`, plus ~50 closed ones for context). Excluding the ten
opened by this project's own concurrent sessions (#341, #353, #362–#365, #377, #380 …):

| issue | why not |
|---|---|
| #317 `--pca` fails with an infinite value in the GRM (2025-12, plink2) | The best 2.0 bug report open, but it needs the reporter's HGDP+1kGP pfile: the GRM is accumulated in double precision from values bounded by `kSmallEpsilon`, so no synthetic input in this session can overflow to infinity — the value has to come from the reporter's data, and diagnosing it without the file would be guesswork. |
| #98 "Unjustified NA output?" (2019, plink2 `--glm` logistic) | Real (plink2 returns all-NA where R's `glm()` converges), but the input is a GitHub attachment that cannot be fetched here, the 2019 build predates the `ERRCODE` column and `firth-fallback`, and what counts as "should have converged" is the maintainer's numerical-policy call. |
| #236 round-tripping VCF→pgen→VCF does not preserve contig names (2023) | Reproduced in a minute (`chr1` comes back as `1`), but this is `--output-chr`'s documented default, so "fixing" it is a default-behaviour decision for the maintainer, not a bug fix. |
| #245 multithread-only `--glm` floating-point exception (2023) | The body is a link to a plink2-users thread, which is not reachable from this session; no reproduction to work from, and nothing in the current `--glm` thread-partitioning code divides by a value that can be zero. |
| #186 restore `--allow-no-vars` (2021) | Feature restoration, and the maintainer's answer is in comments this session cannot read. |
| #140 (chosen) | User-reported, self-contained reproduction, unclaimed for five years, no assignee, and the fix is exactly the todo the maintainer left in the code at the site this issue points to. |

No open PR touches `--bmerge` or `merge_bim_scan` (`search_pull_requests`, `is:open`: the 22
open PRs are the plink2 feature ports #349–#379 plus #316).

## Files

| file | what |
|---|---|
| `repro.sh` | reproduction: two filesets, merged both ways, `--merge-mode 6` and `--make-bed` |
| `repro.before.out` / `repro.after.out` | its output on `ff47b729` and on the patched build |
| `0001-1.9-bmerge-duplicate-ID-reporting-issue-140.patch` | the fix + the new test (`git am`-able on `ff47b729`) |
| `pr-body.md` | PR title and body |
| `tests_before.log` / `tests_after.log` | full `2.0/Tests/run_tests.sh` output, 9/9 before and 10/10 after |
| `comment.md` | short comment for the issue thread |
