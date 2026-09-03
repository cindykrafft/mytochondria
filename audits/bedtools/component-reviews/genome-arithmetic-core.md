# Component: BEDTools genome-arithmetic core (`master` @ `614e9a5`, 2026-06-10)

Upstream `arq5x/bedtools2`, default branch **master**, HEAD
`614e9a5c5935ab86e873dab9072fbbaf003c1b7e` ("ci: install htslib build deps",
2026-06-10). Built with `make` (bundled htslib, system zlib/bzip2/lzma), C++.

Read in full on this commit: the sorted-sweep intersection engine
(`src/utils/NewChromsweep/NewChromsweep.cpp`, `CloseSweep.cpp`), the overlap
predicate and fraction rules (`src/utils/FileRecordTools/Records/Record.cpp`
`sameChromIntersects`), the split/blocked-overlap machinery
(`src/utils/FileRecordTools/Records/BlockMgr.cpp`), intersect
(`src/intersectFile/`, `src/utils/Contexts/ContextIntersect.cpp`), coverage
(`src/coverageFile/coverageFile.cpp`), closest
(`src/utils/NewChromsweep/CloseSweep.cpp`, `ContextClosest.cpp`), merge/cluster
(`src/utils/FileRecordTools/FileRecordMergeMgr.cpp`, `src/clusterBed/`), map and
groupby summaries (`src/utils/KeyListOps/`, `src/utils/VectorOps/VectorOps.cpp`),
genomecov (`src/genomeCoverageBed/genomeCoverageBed.cpp`), shuffle/random
(`src/shuffleBed/shuffleBed.cpp`, `src/randomBed/randomBed.cpp`,
`src/utils/general/Random.cpp`), slop/flank (`src/slopBed/`, `src/flankBed/`),
subtract (`src/subtractFile/subtractFile.cpp`), window
(`src/windowBed/windowBed.cpp`), multicov (`src/multiBamCov/multiBamCov.cpp`),
nuc (`src/nucBed/`), fisher (`src/fisher/fisher.cpp`, `src/fisher/kfunc.cpp`),
jaccard (`src/jaccard/jaccard.cpp`) and reldist (`src/reldist/reldist.cpp`).

Every suspect was **executed on the built binary** (`../verify/`), against an
independent Python port of the documented rule written for this audit (plain
Python / numpy — pybedtools was **not** used), against `scipy.stats.fisher_exact`
for `fisher`, and against the project's own `intersect` where two tools should
agree. Version scope was established by executing the same harnesses on the
`v2.30.0` and `v2.31.1` release tags built from the same repository, not from
release notes.

The BEDTools cohort exposure numbers are lower bounds from the survey cache (see
`../README.md`).

## Findings

| id | status | one line |
|---|---|---|
| **BT1** | **CONFIRMED** master, 2.31.1, 2.30.0 | `coverage -split` counts overlapping **blocks**, not database records, and ignores `-f`/`-F` |
| **BT2** | **CONFIRMED** master, 2.31.1, 2.30.0 | `intersect -split` tests `-F`/`-r` against the **summed** block length of all hits and clears the whole group (upstream #1142) |
| **BT3** | **CONFIRMED** master, 2.31.1, 2.30.0 | `closest -t first`/`-t last` break a left/right tie by stream order, not B-file order, under `-D a`/`-D b` |
| **BT4** | **CONFIRMED** master, 2.31.1, 2.30.0 | `reldist`, `subtract`, `flank` and `closest -d` truncate 64-bit coordinates to 32-bit `int` on chromosomes > 2^31 bp |
| **BT5** | **CONFIRMED** master, 2.31.1, 2.30.0 | `slop -pct`/`flank -pct` and the absolute `-l/-r/-b` values use `float`, losing one base at some percentages and rounding above 2^24 |
| BT6 | NOTE (design/limit, quantified) | `shuffle -incl` lets a placed feature extend past the include interval by up to L−1 bases |
| N1 | NOTE (cosmetic/limit) | overlap fractions are computed in `float`, so `-f 1.0`/`-F 1.0` accept a not-fully-contained interval above 16.7 Mb |
| N2–N9 | NOTE (design/doc) | strict-`>` in `subtract -N`; `-sw`/`-5`/`-3` treat `.` as reverse; genomecov zero-length widening; `-scale` 6-sig-fig printing; overlapping `nuc -pattern`; `-prec` help vs default; multicov `-split -f` denominator |

BT1, BT2, BT4 carry `git format-patch` patches with tests
(`../upstream/000{1,2,3}-*.patch`); each new test fails on unmodified master and
the full `make test` suite passes with the patch.

---

### BT1 — CONFIRMED: `coverage -split` counts blocks, not records, and ignores `-f`/`-F`

**Code.** `CoverageFile::checkSplits` (`src/coverageFile/coverageFile.cpp:236-247`)
replaces the hit list by the *per-block overlap* list that the depth array is
built from:

```cpp
upCast(_context)->getSplitBlockInfo()->findBlockedOverlaps(keySet, hitSet, resultSet, &overlapSet);
hitSet.swap(overlapSet);
```

`makeDepthCount` then does `_hitCount++` once per element of that list
(`:124-136`), and `doDefault`/`doCounts` print `_hitCount` as the "number of
features in B that overlapped A" column. A single database read with *k* blocks
overlapping A is therefore counted *k* times. The project's own test
`coverage.t10` even asserts this: a three-block read gives a count of 3
(`test/coverage/test-coverage.sh`). Separately, `findBlockedOverlaps` clears
`resultSet` when `-f`/`-F`/`-r` are not met, but `overlapSet` (the per-block
list) is kept, so the depth and the count survive the rejected fraction — `-f`
has no effect on `coverage -split`.

**Verified** (`../verify/bt1_coverage_split_count.py` / `.out`, master):

- minimal: A = chr1:100-1000, one BED12 read with two 100-bp blocks inside A →
  `coverage -split` count `2`, `-counts` `2`; `intersect -c -split` count `1`.
- minimal `-f`: A = chr1:100-200, one 10-bp read (10 % of A) → `coverage -split
  -f 0.5` reports count `1`, `10` bases, `0.10`; `intersect -c -split -f 0.5`
  reports `0`; `coverage -f 0.5` (no split) reports `0`.
- random (300 A, 3000 BED12 reads, 1–4 blocks): the shipped count equals the
  block count for 300/300 A intervals and the *record* count for only 102/300;
  it equals `intersect -c -split` (records) for 0/300. Totals: shipped 1653,
  records 995, blocks 1653. The bases-covered column is correct (union of
  overlaps, 300/300).
- random `-f 0.5`: `coverage -split -f 0.5` is byte-identical to `coverage
  -split` with no `-f` on 300/300 A intervals; 276 A intervals have count > 0
  under `-f 0.5` where both `intersect -c -split -f 0.5` and the per-record
  reference say 0.

**Impact.** Any pipeline that reads the count column (or `-counts`) of `coverage
-split` over spliced BAM/BED12 (RNA-seq read counting per feature) over-counts
multi-exon reads, and any `-f` threshold on `coverage -split` is silently
inert. This is a *wrong number at master*.

**Prior art.** #673 (open, 2018) reports `coverage -split -f 1.0 -counts` giving
444 instead of 30 on BAM — the same defect, unfixed for 8 years. #591, #8 are
related `-split` reporting issues.

**Fix** (`../upstream/0001-coverage-split-count.patch`): keep the count of
database records that survived the fraction test (`resultSet.size()`), and drop
the per-block overlaps when none survived. `test/coverage/test-coverage.sh`
t10/t10b now expect `1`; t10c–t10g add `-f 0.6`/`-f 0.7` and a BED12 record.
This changes the published `coverage.t10` expected value, so it is a
behaviour-changing fix and should go to the maintainer first.

---

### BT2 — CONFIRMED: `intersect -split -F`/`-r` uses a summed denominator and clears the whole group (upstream #1142)

**Code.** `Record::sameChromIntersects` skips the fraction test when `-split` is
set (`src/utils/FileRecordTools/Records/Record.cpp:215-218`), deferring it to
`BlockMgr::findBlockedOverlaps`. That function receives *all* database records
that touched one query record as a single `hitList`, sums their block lengths
into one `hitBlockSumLength`, takes the *non-redundant* overlap across all of
them as the numerator, and clears **every** hit for the query when the ratio is
below `-F` (or below `-f` under `-r`) (`BlockMgr.cpp:283-303`,
`resultList.clearAll()`). So `-F`/`-r` are not per record: a record 100 % inside
the query is dropped once another record also overlaps the query, and a record
that fails on its own is kept when a neighbour passes.

**Verified** (`../verify/bt2_intersect_split_F.py` / `.out`, master):

- minimal: A = chr1:100-200, three identical single-block BED12 reads chr1:120-170
  (each 100 % inside A) → `-split -F 0.5` prints 0 lines, `-split -F 0.33`
  prints 3, without `-split` prints 3 at any `-F`; the break sits at 50/150 =
  0.333, the summed denominator.
- random (200 A, 4000 BED12 reads): `-split -F 0.5` gives 530 false negatives
  and 48 false positives against the per-record reference (838 pairs); `-F 0.9`
  gives 579 false negatives; without `-split` the per-record reference is
  matched exactly (0/0). `-split -f 0.5 -r`: 1 reference pair, 0 shipped.
- `-f` under `-split` is confirmed **cumulative over B** (the project's own
  `intersect.t22.*` tests / issue #750), which is a documented design choice,
  not a defect; only the per-record nature of `-F`/`-r` is wrong.

**Prior art.** Upstream **#1142** (open, 2026-08-05) reports exactly this with a
root-cause read of `BlockMgr.cpp` and a real dataset (306 of 665 true positives
dropped). #1141 (open) is the same defect seen through `-wao -f`. The fix should
be filed as a comment on #1142, not a new issue.

**Fix** (`../upstream/0002-intersect-split-per-record-F.patch`): test `-F` and
`-r` against each database record's own block length and remove only the records
that fail; keep `-f` as the cumulative fraction of the query covered by the
survivors (issue #750). The existing `-F 0.20` test (`intersect.t22.p`) now also
reports `exon2` for the two-block read (20/100 bases); new cases t22.s/t22.t
cover three identical reads and the #1142 example. Behaviour-changing;
maintainer-first.

---

### BT3 — CONFIRMED: `closest -t first`/`-t last` break a left/right tie by stream order, not file order

**Code.** `CloseSweep::finalizeSelections` walks the upstream and downstream
lists and, on a tie (`upDist == downDist`), takes the upstream side unless
`-t last` and the downstream side unless `-t first`
(`CloseSweep.cpp:388-411`). "Upstream" is a signed-distance concept: under
`-D a` with a reverse-strand query, and under `-D b` with a forward-strand hit,
the record physically to the *right* of the query is upstream. The docs define
`-t first` as "Report the first tie that occurred in the B file" and `-t last`
as the last. So when the two tied records straddle the query, `-t first`
returns whichever is upstream in the `-D` orientation, which need not be the
first in file order.

**Verified** (`../verify/bt3_closest_tie_order.py` / `.out`, master):

- minimal: A = chr1:10-20 (−); B = b1 chr1:5-6 (+) and b2 chr1:24-25 (+), both
  distance 5. `-d -t first` → b1 (file order, correct). `-D ref -t first` → b1.
  `-D a -t first` → **b2**; `-D a -t last` → b1 (reversed). `-D b -t first` →
  **b2**.
- random (2000 queries, one tied left + one tied right each): `-D ref` matches
  file order for 0/2000 mismatches; `-D a -t first` returns the non-first record
  for 1027/2000 (all reverse-strand queries); `-D b -t first` for 469/2000 (all
  forward-strand hits); `-d -t first` 0/2000 (control).

**Nature.** A *wrong number at master* only in the narrow sense that the chosen
record is not the documented one; the distance is correct and `-t all` is
unaffected. Because a fix changes which single record `-t first`/`-t last`
report under `-D`, it is behaviour-changing and best raised as an issue first;
no patch is shipped (the cleanest fix — order the tie by original file position
within `finalizeSelections` — needs the record's file index threaded through
`RecDistList`, which is invasive). Recorded as CONFIRMED, patch deferred.

**Prior art.** No open or closed issue matches (searched "tie", "-t first",
"-D a"); the nearest, #157/#471, are about `-iu/-id` and `-k` with `-D`.

---

### BT4 — CONFIRMED: `reldist`, `subtract`, `flank`, `closest -d` truncate 64-bit coordinates to 32-bit `int`

**Code.** Coordinates are `CHRPOS` (`int64_t`) since 2.28 ("support for genomes
with large chromosomes"), but several tools narrow them:

- `reldist` (`src/reldist/reldist.cpp:44,109`): `(int)(bed.end + bed.start) / 2`
  — the midpoint overflows when `start + end >= 2^31`.
- `subtract` (`src/subtractFile/subtractFile.cpp:71-72,84-85,87-91,114,130-137`):
  `keyStart`, `keyEnd`, `hitStart`, `hitEnd`, the index locals and the block
  coordinates are `int`.
- `flank` (`src/flankBed/flankBed.cpp:54-58,77,133`, and the `static_cast<int>`
  boundary tests): `int chromSize`, `int leftFlank/rightFlank`.
- `closest` (`src/utils/NewChromsweep/CloseSweep.h:50,52,56`;
  `CloseSweep.cpp:97,293,307`): `RecDistList` stores distances as `int`
  (`_distIndex[i].first`, `(int)dist`) with `INT_MAX` sentinels.

**Verified** (`../verify/bt4_bigchrom_int_truncation.py` / `.out`, master, on a
5-Gb chromosome):

- reldist: B midpoints at base and base+1000, A midpoint at base+100, expected
  `0.100`. Correct at base 1e6, 1e9; **silently drops the query** (empty output)
  at base 1,073,741,000 and above (the `start + end >= 2^31` threshold).
- subtract: A = [3e9, 3e9+100) minus B = [3e9+10, 3e9+20) → the shipped output
  is `chr1 3000000000 -1294967286` (negative end); correct below 2^31.
- flank: A = [3e9, 3e9+100), `-l 10 -r 10` → shipped `chr1 0 3000000000`
  (single garbage flank); correct below 2^31 and for small coordinates on a big
  chromosome.
- closest `-d`: gap of 3e9 → shipped distance `1294967295` instead of
  `3000000001`; `-k 2` even reorders (near reported farther than far).
- controls at base 3e9 that use `CHRPOS` throughout — `intersect -wo`,
  `coverage`, `merge -d`, `cluster -d`, `slop`, `window -w` — are all correct.

**Impact.** A *wrong number (or dropped record) at master* for any genome with a
chromosome longer than ~2.15 Gb (wheat, maize, axolotl, lungfish, many plants
and amphibians). Silent: `subtract`/`flank` emit garbage coordinates,
`reldist`/`closest` misreport or drop.

**Prior art.** #1060 (open) is a related 32-bit overflow on line counts, not
coordinates. No issue matches these four tools.

**Fix** (`../upstream/0003-large-chrom-coordinates.patch`): use `CHRPOS` through
`reldist`, `subtract` and `flank`; adds a large-chromosome test to each. The
`closest -d`/`-k` truncation (`RecDistList`'s `int` distance store) is left
unpatched here — it needs the container's index type widened — and is recorded
as CONFIRMED, patch deferred.

---

### BT5 — CONFIRMED: `slop -pct`/`flank -pct` lose a base at some percentages; absolute `-l/-r/-b` round above 2^24

**Code.** `slopBed.cpp:57-60,87-88`: the fractional slop is computed as
`_leftSlop * (float)bedEntry.size()` and cast to `CHRPOS` (truncation); the
non-fractional `_leftSlop`/`_rightSlop` are themselves stored `float`
(`slopBed.h`), as are flank's (`flankBed.cpp:57-58`). When `pct * size` is an
exact integer *k* but the single-precision product lands just below *k*, one
base is lost.

**Verified** (`../verify/bt5_pct_float_truncation.py` / `.out`, master):

- closed form (numpy float32): 12 of 99 whole-percent values are affected at
  some size ≤ 20000 (0.13, 0.21, 0.26, 0.39, 0.42, 0.52, 0.53, 0.59, 0.65,
  0.71, 0.78, 0.84); the other 87 (including 0.10, 0.25, 0.50) are exact.
- shipped binary: over 36 (pct, size) cases from the closed form, `slop -pct`
  adds one base too few in 36/36 and `flank -pct` is one base short in 36/36
  (e.g. pct 0.53, size 100: 52 added, exact 53; pct 0.65, size 180: 116, exact
  117); controls 0.10/0.25/0.50 correct.
- absolute: `slop -b 20000001` on a 1e8 chromosome gives 5000000-45000010
  instead of 4999999-45000011, because `float32(20000001) == 20000000`.

**Nature.** A *wrong number at master* of magnitude one base (fractional) or the
low bits of a > 16.7 M slop (absolute). Small, but silent and deterministic.
No patch is shipped (the fix — compute the product in `double` and round, and
store the absolute slop as an integer — touches the option parsing signatures in
`slopMain`/`flankMain`); recorded CONFIRMED, patch deferred. No prior issue
(nearest #45, #195, closed, are other slop bugs).

---

## Notes (design, documentation, quantified limits — not "wrong at master")

- **BT6 — `shuffle -incl` spill.** `ChooseLocusFromInclusionFile`
  (`shuffleBed.cpp:447-462`) draws the start uniformly inside the chosen include
  interval and only rejects placements running past the chromosome end
  (`ShuffleWithInclusions`, `:253-258`), so a feature of length L can extend up
  to L−1 bases beyond the include interval. Verified
  (`../verify/bt6_shuffle_incl_spill.py`): for L=200, S=1000 include interval,
  19.5 % of placements spill (expected (L−1)/S = 19.9 %); a realistic mix put
  301,843 of 5,037,800 bases outside the include set across 475 of 5000
  features; `-noOverlapping` and `-excl` do not change this. This is a
  long-standing design limit (upstream **#1089** open, #381 closed for the
  related length-weighting issue), so it is a NOTE, not a wrong number — but a
  `-incl` null model that assumes features stay inside the include set is biased.
- **N1 — float overlap fractions.** `sameChromIntersects` computes `overlapA =
  (float)overlapBases / (float)aLen` (`Record.cpp:205-206`), so above 2^24 bp a
  1-base shortfall rounds away: `intersect -f 1.0 -u` on A = [0, 16777217),
  B = [0, 16777216) reports the interval as fully contained
  (`../verify/note_intersect_fraction_float.py`). For fractions people type
  (0.05–0.9) on intervals under 16.7 Mb the float rule never disagrees with
  exact arithmetic; only `-f`/`-F` = 1.0 on very long intervals is affected.
- **N2–N9** (`../verify/note_misc_edges.py`): `subtract -N` uses strict `>`
  where `-A -f` uses `>=` (exactly 50 % covered is removed by `-A` but kept by
  `-N`); `window -sw`, `genomecov -5/-3` and the merge/window strand handling
  treat a `.` strand as reverse; `genomecov` widens a zero-length record to two
  bases; `-scale` prints 6 significant figures (scientific notation above 1e6);
  `nuc -pattern` counts overlapping occurrences; `map -prec` help says default 5
  but `KeyListOps.h` sets 10; `multicov -split -f` takes the fraction of the read
  footprint with a strict `>` (different denominator from non-split `-f`).

## What held up (executed, not just read)

All against independent ports on random intervals unless noted; every check
below passed with **0 mismatches**.

- **intersect** (`../verify/heldup_overlap_tools.py`, 400 A × 1500 B, two
  chromosomes, strands, duplicates): `-wo`/`-wao`/`-loj`/`-c`/`-u`/`-v` and the
  overlap widths, with and without `-sorted`, for `-f`, `-F`, `-r`, `-e`, `-s`,
  `-S` and combinations; `-C` and multi-file `-wo` (file-id column); the
  sorted-sweep engine agrees with the brute-force port bit for bit.
- **coverage**: default columns (count, bases covered, length, `%0.7f` fraction
  computed in `float`), `-counts`, `-mean`, `-d`, `-hist` per record and the
  `all` summary — all equal the depth-array port (the fraction is float32, which
  the port reproduces).
- **subtract**: default fragments, `-f` (per hit), `-A`, `-A -f`, `-N -f`.
- **window**: `-w`, `-l/-r`, `-sw`, `-sm`, `-Sm`, `-u`, `-c`, `-v` (strand
  compared as strings, so `-sm` treats `.`==`.` as same strand; `-sw` flips for
  every non-`+` strand — note N3).
- **merge/cluster**: `-d 0/100/-1`, `-s` (per strand; `.` records dropped, matching
  `FileRecordMergeMgr`), `-S +`, and the 18 `-c/-o` summaries (file order within
  each group).
- **map** and **groupby**: sum, mean, median, min, max, absmin, absmax, stdev,
  sstdev, mode, antimode, count, count_distinct, collapse, distinct, first,
  last, with `-null` (count/count_distinct give 0, numeric ops give the null
  string for an A record with no hits); `map -o sum -f 0.5 -s`. The two
  independent implementations (`KeyListOpsMethods` for map, `VectorOps` for
  groupby) both match.
- **closest** (`../verify/heldup_closest_genomecov_multicov.py`, 300 A × 600 B):
  `-d`, `-D ref/a/b` sign conventions, `-io`, `-s/-S`, `-k` (ties at the k-th
  distance all reported), `-N`, `-mdb each/all` — all match the port (on
  sub-2^31 coordinates; the large-coordinate case is BT4).
- **genomecov** on BED: default histogram (per chromosome and genome, `%g`
  float32 fraction), `-bg`, `-bga`, `-d`, `-dz`, `-max`, `-scale`, `-strand`,
  `-5`, `-3`, `-split` on BED12; on BAM (pysam-written reads with M/N/D/I/S and
  proper pairs): `-bg` (N covered, D not, I/S not), `-ignoreD`, `-split`,
  `-split -ignoreD`, `-strand`, `-du`, `-5`, `-3`, `-fs`, `-pc`.
- **multicov**: default, `-q`, `-p`, `-D`, `-F`, `-s`, `-S`, `-f`, `-f -r`,
  `-split`, `-split -f`.
- **fisher** (`../verify/heldup_stats_fisher_jaccard_reldist.py`, 30 random
  pairs): the printed 2×2 table (record counts, the genome/mean-length `n22`
  heuristic, with and without `-m`) equals the port of `fisher.cpp:50-69`, and
  the left/right/two-tail p-values equal `scipy.stats.fisher_exact` to a
  relative 1e-4 (30/30); the odds ratio equals `(n11/n12)/(n21/n22)` and prints
  `inf`/`-nan` as `fisher.cpp:94-97` prescribes. The two documentation examples
  reproduce the printed table; the documented p-values (0.0045045) are from an
  older, slightly different `n22` heuristic — the current binary and scipy agree
  on the current table (0.0053476), which is a documentation-drift point, not a
  wrong number.
- **jaccard**: intersection, union, `%0.7f` jaccard, n_intersections on random
  overlapping sets (both files merged first), and `-s` (20/20).
- **reldist**: `-detail` values and the floor-to-0.01 summary histogram equal
  the Favorov port (5/5); confirmed that A records outside the span of B's
  midpoints on their chromosome are silently dropped (upstream #955).
- **nuc**: counts and `%f` pct_at/pct_gc (float32), `-s` reverse complement,
  `-pattern`/`-C` (case-sensitive, overlapping) on 200 random intervals.
- **shuffle/random** (`../verify/heldup_shuffle_random.py`): lengths/strands
  preserved; chromosome frequency proportional to size (χ² p = 0.74) and
  `-chromFirst` uniform over chromosomes (p = 0.89); start positions uniform
  along each chromosome (χ² p ≥ 0.17); `-chrom` keeps the chromosome; `-seed`
  reproducible and different seeds differ; `-excl` never overlapped (and `-excl
  -f`); `-noOverlapping` output has no pairwise overlap; `-allowBeyondChromEnd`
  clips at the chromosome end. `random -n/-l/-seed`: count, length, containment,
  chromosome proportions, strand balance. The Mersenne-Twister RNG
  (`Random.cpp`, `std::mt19937_64`) with rejection sampling is unbiased on these
  tests.

## Not audited here

BAM/CRAM/VCF/GFF parsing and BED12 field handling beyond block coordinates;
`getfasta`/`maskfasta` sequence extraction; `makewindows`; `sort`;
`complement`; `spacing`; `annotate`; `links`/`igv`; `tag`; `pairToPair`/
`pairToBed` and all BEDPE paths; `expand`; `split`; `sample`; `summary`; the
`-nonamecheck`/sort-order enforcement machinery; multi-threaded / `-nobuf`
output; and the plotting/report text.
