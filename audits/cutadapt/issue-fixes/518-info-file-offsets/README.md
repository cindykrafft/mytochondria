# cutadapt #518 — `--info-file` offsets and sequences are wrong after `--cut` / `-q` / `--nextseq-trim`

_Prepared 2026-09-03 against `marcelm/cutadapt` `main` @ `50e9fb8d` (2026-06-26), the
same commit as the audit. Fix branch `fix/issue-518-info-file-offsets`, one commit
(`00b47a7`), patch in this directory. Nothing has been pushed or posted._

## The issue

- **#518 "Offsets in info file sometimes incorrect"**, https://github.com/marcelm/cutadapt/issues/518,
  opened 2021-03-16 by the maintainer (marcelm) while fixing #517, still open, one comment
  (comments cannot be read from this session; the body is self-contained).
- Claim: "If read modifications are done before adapter trimming (such as quality
  trimming), the info file does not contain the correct offsets and sequences. The
  offsets are relative to the sequence as seen by the adapter trimmer (for example,
  with low-quality bases removed), not relative to the original sequence. This is a
  problem when the read has been trimmed at the 5' end. The three reported sequences
  are also incorrect because the *original sequence* is split up according to the
  wrong offsets."
- No open or closed PR references it (`search_pull_requests` for "info file offsets 518":
  0 results).

## Diagnosis (`main` @ `50e9fb8d`)

- `src/cutadapt/cli.py:941-970`: the modifier list is built as `--cut` cutters, then
  `--nextseq-trim`, then `--quality-cutoff`, then the adapter cutter. All three run
  before adapter search and each removes a prefix and/or a suffix of the read
  (`src/cutadapt/modifiers.py:520-526` `UnconditionalCutter`, `:834-837`
  `NextseqQualityTrimmer`, `:853-858` `QualityTrimmer`). The `Match` objects the adapter
  cutter appends to `info.matches` therefore carry `rstart`/`rstop` relative to the
  shortened read.
- `src/cutadapt/steps.py:232-247` `InfoFileWriter.__call__` starts from
  `info.original_read` (`:233`) and calls `match.get_info_records(current_read)` (`:238`),
  and `SingleMatch.get_info_records` (`src/cutadapt/adapters.py:395-417`) slices that
  read at `self.rstart:self.rstop`. With `k` bases removed from the 5' end the offsets
  are too small by `k` and columns 5-7 and 9-11 show the original read split at the
  wrong place (the "matched" column shows `k` bases from before the adapter plus the
  first `len-k` of it). Removing bases from the 3' end only (`-u -N`, `--nextseq-trim`)
  leaves the offsets correct. With `--revcomp` and a reverse-complemented read the
  roles of the prefix and the suffix swap.
- `doc/reference.rst` ("Info file format") promises that "the concatenation of the
  fields 5-7 yields the full read sequence" and that the coordinates are those of the
  adapter match, so the original read is the documented frame of reference.

## The fix (commit `00b47a7`, `0001-Make-info-file-offsets-refer-to-the-original-read.patch`)

- `ModificationInfo` (`info.pyx`, `info.pyi`) gets two counters, `removed_front` and
  `removed_back`; `UnconditionalCutter`, `QualityTrimmer` and `NextseqQualityTrimmer`
  add what they removed from each end.
- `InfoFileWriter` splits the (possibly reverse-complemented) original read into the
  removed prefix, the read the adapters were searched in, and the removed suffix,
  lets the matches produce their records relative to the searched read (so `--times`
  rows and the two linked-adapter rows stay exactly as documented, i.e. relative to the
  successively shorter reads), and adds the prefix and suffix back to the first record
  (offsets shifted by the prefix length, columns 5/7 and 9/11 extended).
- `CHANGES.rst` entry under a new "development version" heading with `` :issue:`518` ``;
  one sentence added to the info-file reference.

Diff: 8 files, +174/−5 (`CHANGES.rst` +8, `doc/reference.rst` +4/−1, `info.pyi` +2,
`info.pyx` +11/−1, `modifiers.py` +5, `steps.py` +31, `tests/test_info_file.py` +108,
`tests/test_modifiers.py` +6/−2).

## Reproduction (`repro.py`, synthetic single read, run through `python -m cutadapt`)

Read `AAAAACCCCCCCCCCCGATTACAGGGG` (27 nt), adapter `GATTACA` at 16-23.

| case | `main` (`repro.before.out`) | with fix (`repro.after.out`) |
|---|---|---|
| no pre-trimming | 16-23, `GATTACA` | 16-23, `GATTACA` |
| `-u 5` | **11-18, `CCCCCGA`** | 16-23, `GATTACA` |
| `-q 20,0` (first five bases Phred 2) | **11-18, `CCCCCGA`** | 16-23, `GATTACA` |
| `-u 5 --revcomp` | **11-18, `CCCCCGA`** | 16-23, `GATTACA` |

`extra_checks.py` (300 random reads with the 14-nt adapter planted, random Phred 2/40
qualities, 11 option combinations including `-u N -u -M`, `-q`, `--nextseq-trim`,
`--revcomp`, `--times 2`, `--action=retain`, `-g`, a linked adapter, `-j 2` and
paired-end with `--info-file-paired`/`-U`) checks that in the first row of every read
columns 5-7 and 9-11 concatenate to the (reverse-complemented if flagged) original
read, that column 6 is the original read sliced at columns 3-4, and that an error-free
match of the planted adapter is a substring of it: **2,953 of 3,255 rows wrong on
`main`, 0 with the fix** (`extra_checks.before.out` / `.after.out`).

## Tests

- New: `tests/test_info_file.py::test_info_file_offsets_after_cut_or_quality_trim`
  (parametrised: `-u 5`, `-u -3`, `-q 20,20`, `--nextseq-trim 20`, `-u 5 --revcomp`),
  `::test_info_file_offsets_after_cut_reverse_complemented` (`-u -3 -q 20,0 --revcomp`,
  read actually reverse-complemented), `::test_info_file_offsets_after_cut_times`
  (`--times 2`, FASTA); `tests/test_modifiers.py::test_unconditional_cutter` and
  `::test_quality_trimmer` assert the new counters.
- On unmodified `main` with the new tests: `test_info_file.py test_modifiers.py`
  **7 failed, 53 passed** (the `-u -3` and `--nextseq-trim` cases pass on `main`, as
  expected: 3'-only removal never shifted the offsets; they are regression guards).
- With the fix: `test_info_file.py test_modifiers.py` 60 passed; full `tests/`
  **710 passed, 1 failed** (`test_command.py::test_run_cutadapt_process`, which
  `subprocess`-calls `cutadapt` and fails only because the venv is not on `PATH`; it
  fails identically on unmodified `main`, where the suite is 703 passed / 1 failed).
- `black --check` 22.3.0: the four changed `.py` files unchanged. `flake8` on them:
  clean (the project-wide run reports one pre-existing `E226` in `report.py:623`, not
  touched). `mypy src/`: "Success: no issues found in 25 source files".

## Other candidates considered (100 of the 105 open issues listed; bodies read for the ones below)

- **#889** "Error when combining multiple 5' adapter search with `-g file:` and
  `;rightmost`" (2026-07, 0 comments): reproduced here as
  `TypeError: SingleAdapter.__init__() got an unexpected keyword argument 'rightmost'`
  for `-g 'file:g.fa;rightmost'` — a crash on valid input in the new 5.2 `rightmost`
  feature, but the fix is a design question (which adapter classes should accept the
  parameter, and how `file:` parameters combine with `;rightmost`), so it was left as a
  second choice.
- **#856** "`--rest-file` with linked adapters: `AttributeError: 'LinkedMatch' object has
  no attribute 'rest'`" (2025-08, 1 comment): reproduced here, but #357 (maintainer)
  proposes removing `--rest-file` altogether, so a fix may be unwanted.
- **#760** "When demultiplexing, report contains irrelevant line" (2024-02, maintainer,
  0 comments): reproduced (`Reads discarded as untrimmed: 0 (0.0%)` printed without
  `--discard-untrimmed`); cosmetic report text rather than a wrong result.
- **#586** "Inconsistent number of fields in info output file" (2021-12): the
  4-column no-match row is documented behaviour; changing it is a format decision.
- **#855**, **#839**, **#631**, **#565**, **#466**: trimming-behaviour reports whose
  bodies read as expected-behaviour questions or that need the reporter's data.
- #892 (this audit's CA1) and the held CA2-CA4 findings were skipped as instructed.

## Caveats

- The one comment on #518 could not be read; if the maintainer had a different frame of
  reference in mind (rows relative to the read as the trimmer saw it, without the
  removed bases), the writer change shrinks to dropping the prefix/suffix re-addition,
  and the counters are still needed to locate the searched read inside the original.
- The counters are updated by the three modifiers that run before adapter search; a
  modifier added before the adapter cutter in future would have to do the same, which
  the `ModificationInfo` comment says.
- `PairedReverseComplementer` (swapping R1/R2 under `--revcomp` in paired mode) was not
  exercised beyond the existing tests; the paired property check ran without `--revcomp`.
