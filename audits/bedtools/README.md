# BEDTools audit against 302 published papers (2021–2026)

_Generated 2026-09-03 against `arq5x/bedtools2` **master** @ `614e9a5`
(2026-06-10), C++. Focus: correctness at master of the tools whose output is a
published number, verified by executing the built binary._

## What this is

The six-journal survey found **302 papers** in *Nature* (148), PNAS (126),
*Cell* (17) and *Science* (11), 2021–2026, that used BEDTools — the standard
toolkit for genome arithmetic, in nearly every ChIP/ATAC/CUT&RUN, RNA-seq,
methylation, variant and Hi-C pipeline. Its genome-arithmetic core — the
sorted-sweep intersection engine, the split/blocked-overlap machinery, the
fraction and strand rules, and the tools that turn intervals into counts,
fractions, distances, coverage and p-values — was read in full on `master` and
every suspicion was run through the built binary
(`make`; the `v2.30.0` and `v2.31.1` release tags built from the same
repository for version scope), against an independent Python port of the
documented rule written for this project (plain Python / numpy — **not**
pybedtools), against `scipy.stats.fisher_exact` for `fisher`, and against the
project's own `intersect` where two tools should agree. BAM harnesses build
their reads with pysam.

## Findings (details and line citations in [`component-reviews/genome-arithmetic-core.md`](component-reviews/genome-arithmetic-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **BT1** | **CONFIRMED** on master, 2.31.1 and 2.30.0 | `coverage -split` reports the number of overlapping **blocks**, not database records (a 3-exon read counts as 3; `intersect -c -split` counts it once), and it ignores `-f`/`-F` (a 10 % overlap is reported under `-f 0.5`). Wrong number since at least 2018 (issue #673). Patch + tests. |
| **BT2** | **CONFIRMED** on master, 2.31.1 and 2.30.0 | `intersect -split` tests `-F` and `-r` against the **summed** block length of every database record that touched the query and clears the whole group, so a record 100 % inside the query is dropped when a neighbour also overlaps (530 false negatives + 48 false positives in 838 pairs at `-F 0.5`). Upstream **#1142** (open). Patch + tests. |
| **BT3** | **CONFIRMED** on master, 2.31.1 and 2.30.0 | `closest -t first`/`-t last` break a left/right tie by `-D` stream order, not B-file order, so under `-D a` (reverse query) or `-D b` (forward hit) `-t first` returns the wrong record (1027/2000 reverse-strand queries under `-D a`). Distance correct, `-t all` unaffected. Patch deferred (invasive). |
| **BT4** | **CONFIRMED** on master, 2.31.1 and 2.30.0 | `reldist`, `subtract`, `flank` and `closest -d` narrow 64-bit coordinates to 32-bit `int`, so on chromosomes > 2^31 bp (~2.15 Gb; wheat, maize, axolotl, many plants/amphibians) `reldist` silently drops queries, `subtract`/`flank` emit negative/garbage coordinates and `closest -d` misreports the distance. Patch (reldist/subtract/flank) + tests; `closest -d` patch deferred. |
| **BT5** | **CONFIRMED** on master, 2.31.1 and 2.30.0 | `slop -pct`/`flank -pct` compute the fraction in single precision and truncate, losing one base at 12 of 99 whole-percent values (0.13, 0.21, 0.26, 0.39, 0.42, 0.52, 0.53, 0.59, 0.65, 0.71, 0.78, 0.84); the absolute `-l/-r/-b` are also `float`, so values above 2^24 round. Patch deferred. |
| BT6 | note (design/limit, quantified) | `shuffle -incl` lets a placed feature extend up to L−1 bases past its include interval (19.5 % of a 200-bp feature into a 1-kb interval); a `-incl` null model that assumes containment is biased. Upstream #1089 (open). |
| N1–N9 | notes (design/doc) | float overlap fractions accept a not-fully-contained interval above 16.7 Mb under `-f/-F 1.0`; `subtract -N` strict `>`; `-sw`/`-5`/`-3`/merge strand treat `.` as reverse; genomecov zero-length widening and `-scale` 6-sig-fig printing; overlapping `nuc -pattern`; `-prec` help vs code default; `multicov -split -f` denominator. |

**Held up under execution** (0 mismatches against the ports): the whole
`intersect` matrix (`-wo/-wao/-loj/-c/-C/-u/-v`, `-f/-F/-r/-e/-s/-S`, sorted and
unsorted, multi-`-b`); `coverage` default/`-counts`/`-mean`/`-d`/`-hist`;
`subtract` default/`-f/-A/-N`; `window` `-w/-l/-r/-sw/-sm/-Sm/-u/-c/-v`;
`merge`/`cluster` (`-d/-s/-S` and 18 `-c/-o` summaries); `map` and `groupby`
(all 18 operations, `-null`, `-f`); `closest` `-d/-D/-io/-s/-S/-k/-N/-mdb` on
normal coordinates; `genomecov` on BED and BAM (`-bg/-bga/-d/-dz/-max/-scale/
-strand/-5/-3/-split/-ignoreD/-du/-fs/-pc`); `multicov`; `fisher` (table vs a
port, p-values vs `scipy.stats.fisher_exact`, odds ratio); `jaccard`; `reldist`;
`nuc`; and `shuffle`/`random` (uniformity and reproducibility by χ²). See the
review for the full list.

## How the papers use BEDTools (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| any overlap / intersection language | 121 |
| `intersect` named (`bedtools intersect` ×23) | 54 |
| version stated | 51 |
| ATAC / ChIP / CUT&RUN context | 88 |
| RNA-seq context | 77 |
| `merge` | 20 |
| `-c`/`-u`/`-v` counting/reporting named | 18 |
| `genomecov` / `-bg`/`-bga`/`-scale` | 14 / 12 |
| `closest` / `coverage` | 9 / 9 |
| `-f`/`-F`/`-r`/`-e` fraction named | 9 |
| `subtract` / `getfasta`/`nuc` / `makewindows` | 7 / 10 / 6 |
| `multicov` / `jaccard` / `fisher` / `cluster` / `shuffle` | 4 / 3 / 1 / 1 / 1 |
| `-split` named | 3 |
| `slop`/`flank` / `-pct` | 3 / 0 |
| pybedtools | 3 |
| version family (2.30 ×45, 2.29 ×17, 2.27 ×14, 2.31 ×10, 2.26 ×10, 2.25 ×8) | 51 stated |

Top co-packages: SAMtools 172, R 167, Bowtie2 118, MACS2 111, DESeq2 104,
Cutadapt 73, Picard 71, BWA 71, STAR 69, deepTools 66.

Exposure by finding: BT1 needs `coverage -split` on spliced reads (RNA-seq
per-feature counting; `-split` named in 3 papers, `coverage` in 9, but the
survey cache rarely records the `-split` flag); BT2 needs `intersect -split
-F/-r` (isoform/exon comparison); BT3 needs `closest -D a/-D b -t first/last`;
BT4 needs a chromosome > 2.15 Gb (large plant/amphibian genomes); BT5 needs
`-pct` or an absolute slop > 16.7 Mb. None of these can be decided from the
cache — the flags and the genome are not in the stored snippets.

**Profiling caveat.** As for the Seurat, Scanpy and Cutadapt audits, this
session had no route to Europe PMC, so `bedtools_profile.py` ran in `--offline`
mode over the survey's stored evidence snippets; every record in
`bedtools_profiles.jsonl` is `source: survey_cache` and every count above is a
**lower bound**. Rerun without `--offline` from a host with Europe PMC access to
replace them with full-text records.

## Filing channel (read before anything is sent)

- **No `CONTRIBUTING.md`, no issue or PR template, no `config.yml`, no pinned
  policy issue, no code of conduct, no `.clang-format`** in the repository
  (checked `.github/`, repo root). The only CI is `.github/workflows/main.yml`:
  `make -j8 && make test` then `make -j8 static` on ubuntu-latest — so the bar
  for a PR is "the tool test suites still pass". There is no changelog fragment
  convention; `docs/content/history.rst` is edited by hand per release (numbered
  bullets thanking contributors by GitHub handle).
- The tracker (`arq5x/bedtools2` Issues) was searched with several phrasings for
  each finding (`mcp__github__search_issues`, 2026-09-03). Nearest prior issues:
  BT1 → **#673** (open, 2018, `coverage -split -f 1.0 -counts` gives the wrong
  count — the same defect), #591, #8; BT2 → **#1142** (open, 2026-08, exact
  match with a `BlockMgr.cpp` root-cause read), #1141 (same via `-wao -f`), #928;
  BT3 → none (nearest #157, #471 about `-iu/-id` and `-k`); BT4 → #1060 (open,
  32-bit line-count overflow, different); BT5 → none (#45, #195 closed);
  BT6 → **#1089** (open, 2024), #381 (closed, related length weighting).
- BT2's fix belongs as a **comment on #1142**, not a new issue. BT1 could be a
  comment on #673 or a fresh issue (its scope — the count column and `-f`,
  not just `-counts` — is broader than #673). BT3, BT4, BT5 are new issues.
  **Every one of these findings changes published numbers**, so all four patched
  items should be raised as issues (or on #1142/#673) and discussed before a PR
  is opened, per step 4 of the method.
- **The kit is in [`upstream/`](upstream/)**: issue/comment texts, three
  `git format-patch` patches (BT1, BT2, BT4 — fix + tests; each new test fails
  on unmodified master and the full `make test` suite passes with the patch),
  MCVE scripts, and the documents-read list.

## Files

| file | what |
|---|---|
| `bedtools_profile.py`, `bedtools_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/genome-arithmetic-core.md` | the review: BT1–BT6, N1–N9, held-up list, not-checked list |
| `verify/btlib.py` | shared harness helpers: run the binary, independent interval arithmetic |
| `verify/bt1_coverage_split_count.py` (+ `.out`, `.v2.31.1.out`) | BT1: minimal + random BED12 vs record/block counts vs `intersect -c -split`; `-f` |
| `verify/bt2_intersect_split_F.py` (+ …) | BT2: minimal + random false-neg/pos vs the per-record reference; `-r`; the `-f`/#750 control |
| `verify/bt3_closest_tie_order.py` (+ …) | BT3: minimal + 2000 tied queries, mismatch counts per `-D` mode |
| `verify/bt4_bigchrom_int_truncation.py` (+ …) | BT4: reldist/subtract/flank/closest at 3e9 vs the truncation threshold; CHRPOS controls |
| `verify/bt5_pct_float_truncation.py` (+ …) | BT5: closed form + shipped `slop -pct`/`flank -pct`; absolute `-b` |
| `verify/bt6_shuffle_incl_spill.py` (+ …) | BT6: spill fraction vs (L−1)/S; realistic mix; `-noOverlapping`/`-excl` |
| `verify/note_intersect_fraction_float.py`, `note_misc_edges.py` (+ `.out`) | N1–N9 |
| `verify/heldup_overlap_tools.py` (+ `.out`) | held-up: intersect/coverage/subtract/window/merge/cluster/map/groupby vs ports |
| `verify/heldup_closest_genomecov_multicov.py` (+ `.out`) | held-up: closest/genomecov (BED+BAM)/multicov vs ports |
| `verify/heldup_stats_fisher_jaccard_reldist.py` (+ `.out`) | held-up: fisher vs scipy, jaccard, reldist, nuc |
| `verify/heldup_shuffle_random.py` (+ `.out`) | held-up: shuffle/random uniformity and reproducibility (χ²) |
| `verify/version_scope_cli.py` (+ `.master.out`, `.v2.31.1.out`, `.v2.30.0.out`) | the six findings through the CLI on all three builds |
| `upstream/` | filing kit: issue/comment texts, patches 0001–0003, PR bodies, MCVEs, documents read |

Harnesses need the built binary and a Python 3.12 venv with numpy, scipy,
pysam: `uv venv --python 3.12 venv && uv pip install numpy scipy pysam`. Point
`BT` at the binary under test (default: the master build in the scratchpad);
`version_scope_cli.py` was run with `BT` set to each release tag's binary.

**Build note.** `v2.30.0` does not compile as-is with GCC here — `ParseTools`
uses `uint32_t`/`n` without including `<cstdint>`; a one-line
`#include <cstdint>` was added to `src/utils/general/ParseTools.h` in the tag
checkout to build it for version-scope execution (it reports `2.30.0-dirty`).
`v2.31.1` and master build clean. All three carry every confirmed finding
identically.

## Next steps

1. Comment on **#1142** with the BT2 patch, and on **#673** (or open a fresh
   issue) with the BT1 scope and patch; open new issues for BT3, BT4, BT5. All
   change published numbers, so discuss before the PRs.
2. Ship the deferred patches (BT3 tie order via `RecDistList` file-index; BT4
   `closest`/`RecDistList` int→CHRPOS; BT5 double-precision `-pct` and integer
   absolute slop) after maintainer agreement on the number changes.
3. Full-text profiling rerun when Europe PMC is reachable, to see which papers
   run `-split`, `-pct`, `closest -D`, or large-genome pipelines.
