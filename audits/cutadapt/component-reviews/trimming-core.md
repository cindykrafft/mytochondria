# Component: Cutadapt trimming core (`main` @ `50e9fb8d`, 2026-06-26, 5.3.dev15)

Read in full: `src/cutadapt/_align.pyx` (882 lines: the semi-global aligner,
`PrefixComparer`/`SuffixComparer`, `edit_environment`), `align.py` (182),
`adapters.py` (1,602: adapter types, `MultipleAdapters`, `AdapterIndex`, linked
adapters, `remainder`), `kmer_heuristic.py` (231) and `_kmer_finder.pyx` (257: the
k-mer prefilter added in 4.3), `qualtrim.pyx` (190) with `expected_errors.h` (140),
`modifiers.py` (918), `predicates.py` (173), `steps.py` (580), `pipeline.py` (153),
`parser.py` (563); targeted reads of `cli.py` (option wiring, filter construction,
pair-filter defaults) and `runners.py` (multi-core chunking), plus `doc/algorithms.rst`
and the relevant sections of `doc/guide.rst` as the statement of intended behaviour.
Every suspicion was **executed on the shipped code**: `main` installed editable into a
Python 3.12 venv (version string `5.3.dev15+g50e9fb8d3`, Cython build), harnesses in
`../verify/` with captured output; each confirmed finding was also run on the 5.2
wheel from PyPI (the latest release) and, through the CLI-only script
`../verify/version_scope_cli.py`, on the 4.1 wheel (the most-cited version in the
cohort that still builds on Python 3.12; 3.4 and 1.18 do not, see `../README.md`).
References are independent Python ports of the documented rules run on random
reads, or the package's own bare aligner run without the prefilter.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### CA1 — CONFIRMED on `main`, 5.2 and 4.1: an absolute number of errors (`-e N`) is converted to a rate, and for some adapter lengths the rate multiplied back is a hair below N, so one allowed error is lost

**Code.** `adapters.py:580-582` turns `-e N` (N ≥ 1) into `max_error_rate = N / (len −
#N)`. The aligner accepts an alignment covering `L` adapter characters when
`cost <= cur_effective_length * max_error_rate` (`_align.pyx:513`, `:559`) and bounds
its Ukkonen band with `k = <int>(max_error_rate * m)` (`:343`); `PrefixComparer`
(the `--no-indels` anchored path) uses `max_k = int(max_error_rate * effective_length)`
(`:633`); the demultiplexing index and the k-mer heuristic floor the same product
(`adapters.py:1378`, `:1400`, `:1418`; `kmer_heuristic.py:95`, `:142`). In IEEE
double arithmetic `49 * (1/49)` is `0.9999999999999999`, so for a 49-nt adapter
`-e 1` means "no errors" everywhere along that chain, and `-e 2` on a 98-nt adapter
means "one error". The documentation (`doc/guide.rst:649-652`) promises the opposite:
"with an adapter of length 10, using `-e 2` will set the maximum error rate to 0.2".

**Verified** (`../verify/ca1_absolute_errors_fp_boundary.py`, `.out` and `.v5.2.out`;
`version_scope_cli.*.out`):

| what | result |
|---|---|
| closed form, `int(n·(k/n)) < k`, n ≤ 300 | k=1,2,4: n ∈ {49, 98, 103, 107, 161, 187, 196, 197, 206, 214, 237, 239, 249, 253}; k=3: {47, 94, 147, 173, 188, 294}; k=5: {77, 154}; partial lengths hit too (k=2, n=98: L=49) |
| decimal rates typed by users (`-e 0.05 … 0.3`), L ≤ 300 | 0 affected lengths; `-e 0.29` loses an error at L = 100 and 200 |
| shipped classes, adapter of 49 nt with `-e 1`, read carrying it with exactly one substitution | `BackAdapter`, `FrontAdapter`, `PrefixAdapter` (indels and `--no-indels`), `SuffixAdapter`: **not found**; found with 0 substitutions; controls n = 48, 50 found with one |
| same with n = 98 (`-e 1`, `-e 2`), n = 47 (`-e 3`), n = 49 (`-e 2`) | not found with k errors, found with k − 1 |
| wildcard adapter, 50 nt with one N (`effective_length` 49), `-e 1` | not found |
| `AdapterIndex` on two 49-nt barcodes, `-e 1` | `max_k` = 0 for both; read with one substitution unassigned |
| CLI, 300 reads = 20 nt + 49-nt adapter with one substitution + 30 nt | `-e 1`: 0 of 300 trimmed to 20 nt (8 random 3-mer end matches); `-e 1.0000001`, `-e 2`: 300/300 |
| version scope (CLI script) | `main`, 5.2, 4.1: 0/300 trimmed; control `-e 1.0000001` 300/300 on all three |

**Who is exposed.** Anyone using the integer form of `-e` (documented since 3.0;
the cohort cache names `-e 1` once and "1 mismatch every 10 bp" once, lower bounds)
with an adapter whose length is in the table — 47- to 49-nt sequences are the size of
a TruSeq adapter plus index or of many amplicon primer pairs, and the 98/103/107-nt
rows are linked-adapter and long-primer territory. The loss is exactly one error at
full length and, for k ≥ 2, at some partial lengths; reads with fewer errors are
unaffected. The default `-e 0.1` and the other decimal rates people type are not
affected at any length up to 300.

**Fix shape** (patch `../upstream/0001-Honour-an-absolute-number-of-errors-e-N-for-every-ad.patch`):
a tolerance of 1e-9 on every `length × rate` product, as a `DEF` constant in
`_align.pyx` and a `max_errors_for_length()` helper in `align.py` used by
`adapters.py` and `kmer_heuristic.py`. Tests added to `tests/test_align.py` and
`tests/test_adapters.py` fail on unmodified `main` (2 failed) and pass with the
patch; the touched modules' suites pass (142 + 392 tests) and the full suite passes.
An exact-rational alternative (keep N and n and compare `errors·n ≤ L·N`) would be
cleaner but touches the Cython signature; the issue text offers both.

**Upstream.** Tracker searched 2026-09-03 for the absolute-errors rounding: no
prior report (#358 introduced the feature, #457 and #615 concern how the allowed
number is displayed).

### CA2 — CONFIRMED on `main`, 5.2 and 4.1: `--max-expected-errors` and `--max-average-error-rate` ignore `--quality-base`

**Code.** `predicates.py:70-71` and `:91-95` call `expected_errors(read.qualities)`
with the default base 33; `cli.py:762` and `:777` construct the predicates without
`args.quality_base`, whereas the quality trimmers receive it (`cli.py:941`, `:1058`).
`--quality-base` is documented as global ("Assume that quality values in FASTQ are
encoded as ascii(quality + N)", `cli.py:274-277`; `doc/guide.rst:1000-1003`). On
Phred+64 data every quality is read 31 too high, so the expected-error sum is
10^3.1 ≈ 1,259 times too small.

**Verified** (`../verify/ca2_max_ee_quality_base.py`, `.out` and `.v5.2.out`; 2,000
random reads of 50–150 nt, Phred 2–40 uniform):

| filter | reference keeps | Phred+33 file, default base | Phred+64 file, `--quality-base 64` |
|---|---|---|---|
| `--max-ee 0.5` | 0 / 2000 | 0 (= reference) | **2000** |
| `--max-ee 1.0` | 0 | 0 | **2000** |
| `--max-ee 2.0` | 2 | 2 | **2000** |
| `--max-aer 0.01` / `0.02` | 0 / 0 | 0 / 0 | **2000 / 2000** |
| control `-q 20` | BWA port | identical | identical |

For read `r0` the true expected-error count is 7.2616 and the predicate computes
0.005768. Version scope (CLI script): `main`, 5.2 and 4.1 keep 300/300 reads with
10.5–23.9 expected errors under `--max-ee 1 --quality-base 64`.

**Who is exposed.** Only users of Phred+64 data (Illumina 1.3–1.7, pre-2011); the
cohort's three `--max-ee` mentions are on modern data. A wrong number nonetheless: the
filter silently becomes a no-op on exactly the data the flag exists for.

**Fix shape** (patch `0002-Make-max-ee-and-max-aer-honour-quality-base.patch`): a
`quality_base` parameter on both predicates, passed from `cli.py`. Two tests added
to `tests/test_predicates.py` fail on `main` (2 failed) and pass with the patch
(19 passed; `test_commandline`/`test_paired`/`test_main` 354 passed).

**Upstream.** No prior report (searched `quality-base` with `max-ee`/expected
errors; #17 from 2015 is about `-q` and was fixed).

### CA3 — CONFIRMED on `main` and 5.2 (4.1 gives the score-consistent answer): the demultiplexing index ranks adapters by number of matching bases, the rest of Cutadapt by alignment score, so the same read is assigned differently with and without `--no-index`

**Code.** `MultipleAdapters.match_to` (`adapters.py:1278-1284`) keeps the match
with the highest `score` (match +1, mismatch −1, indel −2: `_align.pyx:16-19`,
documented as the Cutadapt 4 criterion in `doc/algorithms.rst:103-121`), ties by
fewer errors, then list order. `AdapterIndex` — built automatically for two or more
anchored adapters without wildcards and ≤ 3 errors, i.e. the demultiplexing case —
stores `(adapter, errors, matches)` from `edit_environment` (`:1421-1429`) or the
Hamming sphere (`:1431-1442`), ranks by `matches` in `_match_to_multiple_lengths`
(`:1522`), declares ties in `matches` ambiguous (`:1426`, `:1439`) and passes the
match count into the `score` slot of the returned `Match` (`:1490`, `:1533` via
`_make_match(adapter, length, score, errors, …)`). Its own `_lookup_with_n` path
(`:1535-1551`) returns `match.score` into that slot instead, so the index is
inconsistent with itself as well. "Number of matches" is the pre-4.0 criterion that
`doc/algorithms.rst:79-101` describes as replaced.

**Verified** (`../verify/ca3_index_vs_noindex.py`, `.out` and `.v5.2.out`):

| case | index (default) | `--no-index` |
|---|---|---|
| A = `ACGTACGTACGT` (12 nt), B = `ACGTACGTACA` (11 nt), `-e 0.1`; read starts `ACGTACGTACAGT…` = B exact (score 11, 0 errors) = A with one insertion (12 matches, score 10) | **A**, `score=12 errors=1`, both list orders | B, `score=11 errors=0` |
| CLI, that read × 100, `-g A=^… -g B=^… -o {name}.fastq` | A: 100 | B: 100 |
| 6 random barcodes of 10–12 nt, 10,000 reads with one random edit, `-e 1` (index vs the bare aligner under the score rule) | 10,000 / 10,000 agree | — |
| 6 random barcodes all 10 nt, same | 9,998 agree; 2 reads with an insertion assigned to different barcodes (score ties broken by errors-then-length in the index, by list order in `MultipleAdapters`; both listed in the `.out`) | — |
| `Match.score` of an indexed match with one insertion (10 matches) | 10 | 8 |
| mixed list `[^bc1, ^bc2, 3'-adapter]`, read = bc1 with an insertion + 15 nt + 9 nt of the 3' adapter | bc1 (score field 10) | 3' adapter (score 9) |
| version scope (CLI script) | `main`, 5.2: A 50 / B 0 vs `--no-index` B 50; 4.1: B 50 both ways | |

So the index disagrees with the documented criterion deterministically on
constructed inputs, rarely on random same-length barcodes (2 / 10,000, all tie
cases), and systematically in the `score` it reports — which matters whenever an
indexed group is combined with a regular adapter in one `-g/-a` list or with
`--revcomp` (both compare `score` sums, `modifiers.py:286-288`, `:350-374`).

**Not a finding.** The 5.0 behaviour of refusing ambiguous reads (#827) is a design
choice and is kept by the patch; only the quantity that decides "best" and
"ambiguous" changes.

**Fix shape** (patch `0003-Choose-the-best-adapter-by-alignment-score-also-when.patch`):
store the alignment score in the index (derivable from errors, matches and the two
lengths), rank and detect ambiguity by it, stop the multi-length search on
`length < best_score`. Two tests added to `tests/test_adapters.py` fail on `main`
and pass with the patch; `test_adapters`/`test_modifiers`/`test_commandline`/
`test_paired`/`test_trim` pass (442). Under the patch the harness assigns B in both
paths and the mixed-list case chooses the 3' adapter in both. Because this changes
which reads are "ambiguous", it should go to the maintainer as an issue first.

**Upstream.** Closest prior items: #734 (index collisions, fixed 4.5), #612/#205
(first vs best match), #614 (open, `MultipleAdapters` early stop), #671 (open,
leftmost vs best alignment). None reports the criterion mismatch.

### CA4 — CONFIRMED on `main` and 5.2 (absent on 4.1, which predates the prefilter): the k-mer prefilter rejects anchored and non-internal adapter occurrences that carry one inserted base whenever exactly one error is allowed

**Code.** Since 4.3 (PR #663) every adapter runs `kmer_finder.kmers_present(read)`
before the aligner and returns `None` without aligning when it is false
(`adapters.py:715-716`, `:823-824`, `:964-965`, `:1001-1002`). The search sets are built
in `kmer_heuristic.py:87-117`: for each error class `(max_errors, length)` the
adapter prefix of the class's shortest length is cut into `max_errors + 1` chunks and
searched in the last `length` characters of the read (`:114-115`, window
`(-length, None)`; mirrored to `(0, length)` for 5' adapters at `:157-159`). An
occurrence with an inserted base spans `length + 1` read positions, so the chunk on
the far side of the insertion is shifted out of the window while the chunk on the
near side is broken by the insertion. With more than two chunks a third chunk still
lies inside the window; with exactly two (one allowed error) nothing does. Regular
3'/5' adapters are rescued by their internal search set `(0, None)` (`:161-163`);
anchored and non-internal adapters have `internal=False` (`adapters.py:960`,
`:997`, and `PrefixAdapter`/`SuffixAdapter` inherit it) and no rescue. With
`--no-indels` the anchored types use `PrefixComparer` and `MockKmerFinder`
(`adapters.py:1032-1047`) and are unaffected.

**Verified** (`../verify/ca4_kmer_prefilter_insertions.py`, `.out` and `.v5.2.out`;
`heldup_aligner_properties.out` P5; `version_scope_cli.*.out`). `match_to` (prefilter +
aligner) against the bare `aligner.locate` on reads = adapter with one inserted base at
every position p plus random flanks, 200 draws per p:

| adapter, `-e` | allowed errors | anchored 5' | anchored 3' | non-internal 5' | non-internal 3' | regular 5'/3' |
|---|---|---|---|---|---|---|
| Illumina 34 nt, 0.1 | 3 | 0 lost | 0 | 0 | 0 | 0 |
| small-RNA 21 nt, 0.1 | 2 | 0 | 0 | 0 | 0 | 0 |
| Nextera 19 nt, 0.1 | 1 | **1,466 / 4,000 (37 %)**, p = 1–8 | 1,497 (37 %), p = 11–18 | 697 (17 %), p = 10–13 | 702 (18 %), p = 6–9 | 0 |
| Illumina 34 nt, `-e 1` | 1 | **3,108 / 7,000 (44 %)**, p = 1–16 | 3,106 (44 %) | 3,052 (44 %) | 3,038 (43 %) | 0 |
| small-RNA 21 nt, `-e 1` | 1 | 1,717 / 4,400 (39 %) | 1,592 (36 %) | 1,700 (39 %) | 1,550 (35 %) | 0 |

CLI on the same construction (20 reads per insertion position): Illumina `-e 1`:
`-g ^AD` 392/700, `-g XAD` 398/700, `-a AD$` 388/700 trimmed vs `-g AD` and `-a AD`
700/700; Nextera `-e 0.1`: `^AD` 257/400, `XAD` 332/400, `AD$` 253/400 vs 400/400;
Illumina `-e 0.1`: 700/700 everywhere. Version scope: `main` and 5.2 trim 197/350
(`^AD`, 34 nt `-e 1`) and 126/200 (`^AD`, 19 nt `-e 0.1`) where 4.1 trims 350/350 and
200/200. In the random battery (`heldup_aligner_properties.out`) every one of the 23 +
31 + 7 + 15 prefilter/aligner disagreements for these four types was a read with an
insertion; regular 3'/5' adapters had 0 in 10,000 alignments.

A second, smaller blind spot (Part C): for `-b` (anywhere) adapters, reads that lie
entirely inside the adapter (which the aligner matches, `_align.pyx:118-127`) are
rejected by the prefilter in 114 of 234 substrings of the Illumina adapter at
`min_overlap` 3. Not patched; recorded in the issue text.

**Who is exposed.** Anchored 5' adapters/primers of 10–19 nt at the default `-e 0.1`
(`-g ^PRIMER`, the recommended form for primers; `--no-index` demultiplexing with
10–19-nt barcodes; the cohort cache has 11 explicit 5' adapters and 56
barcode/demultiplexing mentions), and any anchored or non-internal adapter with
`-e 1`. Index-based demultiplexing (≥ 2 anchored adapters, the default) does not use
the prefilter and is unaffected; so is `--no-indels`. Reads with only substitutions
or a deletion are unaffected. The effect is a loss of roughly 40 % of the reads that
carry the adapter with one inserted base — a small fraction of most libraries, but
exactly the fraction the error tolerance was set to keep, and it is silent.

**Fix shape** (patch `0004-Fix-k-mer-heuristic-missing-anchored-adapters-with-a.patch`):
widen each class's window by its `max_errors` (`(-(length + max_errors), None)`),
one line plus the four expected windows in `tests/test_kmer_heuristic.py`. Under the
patch the harness loses 0 of 2,000/3,500/2,200 accepted reads for every affected
type; three new tests in `tests/test_adapters.py` fail on `main` and pass with the
patch; the heuristic/finder/adapter/CLI suites pass (439).

**Upstream.** No prior report found (searched anchored + insertion + heuristic;
#695 is the heuristic's initialisation time, #749 very long adapters).

### N1 — NOTE (documentation): the `Aligner` docstring's tie-break ("fewest errors, then leftmost") is not what the code or `doc/algorithms.rst` say

`_align.pyx:146-154` promises that among equal-score alignments the one with the
fewest errors wins. The update rule (`:548-552`, `:590-594`) only replaces the
current best on a strictly higher score, so ties go to the earlier occurrence — which
is the rule `doc/algorithms.rst:123-126` documents for Cutadapt 4 ("leftmost …
preferred even if a later match has fewer errors"). Executed
(`../verify/note_aligner_tiebreak.out`): 3' adapter `ACGTACGTAC`, internal
occurrence with one mismatch (score 8, 1 error) at read position 5 and an exact
8-nt partial occurrence at the read end (score 8, 0 errors): the position-5 match
is chosen; the 5' mirror likewise takes the leftmost. Design choice, docstring stale.
The same rule explains every "planted exact occurrence not returned" in the random
battery: in 3 + 6 + 14 (+ 7 + 1 + 3 without indels) of ~3,800 planted cases an
earlier occurrence within the error tolerance won (`heldup_aligner_properties.out`).

### N2 — NOTE (latent, API only): `PrefixComparer` subtracts the lowercase-n count instead of adding it

`_align.pyx:628`: `effective_length -= reference.count('N') - reference.count('n')`.
Executed (`../verify/note_prefixcomparer_lowercase_n.out`): reference `ACGTACGTnn`
gets `effective_length` 12 (should be 8) and `max_k` 3 instead of 2; `Aligner` gets 8.
Unreachable from the CLI because `SingleAdapter.__init__` upper-cases the sequence
(`adapters.py:577`; the `PrefixAdapter` route shows `max_k=2`). One-character fix
(`+`), worth folding into the CA1 patch review.

### N3 — NOTE (documentation): the Python snippet for the poly-A algorithm in `doc/algorithms.rst:209-222` never trims

It iterates `enumerate(range(n))`, so `nuc` is an integer and `nuc == "A"` is never
true. Run verbatim on `CGTACGTACG` + 12 A it returns the whole string; the shipped
`poly_a_trim_index` returns `CGTACGTACG` (`../verify/note_misc_docs_lowercase_times.out`).
The Cython implementation matches the prose description on 30,000 random cases (held-up
list). Replace `enumerate(range(n))` by `enumerate(s)`.

### N4 — NOTE (design, minor): `--trim-n` and `--nextseq-trim` are case-sensitive while adapter matching is not

`modifiers.py:906-907` (`^N+`, `N+$`) and `qualtrim.pyx:107` (`== 'G'`); reads are
upper-cased only inside the aligner (`_align.pyx:327`). Executed: `nnACGTACGTNN`
keeps its lowercase `nn`; a Q2 run of `gggggggggg` is not trimmed by
`--nextseq-trim=20` where `GGGGGGGGGG` is. Lowercase FASTQ is rare (soft-masked
reads from some pipelines); recorded, not filed.

## Withdrawn (own suspicions that execution killed)

- **W1 — stale DP cells beyond the Ukkonen band.** Reading `_align.pyx:441-511`
  I suspected that rows first touched when the band grows reuse initial-column
  values and could yield alignments that skip both a reference prefix and a query
  prefix. 100,000 random alignments across all seven adapter types: reported errors
  equal the Levenshtein/Hamming distance of the aligned substrings in every case
  (P1 = 0) and `astart == 0 or rstart == 0` always holds (P6 = 0). Withdrawn.
- **W2 — "planted exact occurrence not returned".** The first version of the random
  battery flagged 3–14 cases per type; every one was an earlier occurrence within the
  tolerance, i.e. the documented leftmost rule (see N1). Withdrawn; the harness now
  counts them separately.
- **W3 — `remainder()` for `--times 2` with `--action mask/lowercase`.** Suspected
  the composed interval could be off for mixed 5'/3' matches; executed both adapter
  orders on a `GGGGGGGG…TTTTTTTT` read: masked and lowercased regions are exactly the
  two adapters (`note_misc_docs_lowercase_times.out`). Withdrawn.
- **W4 — CA3 "index assigns, `--no-index` does not" (1,107 / 10,000).** First seen in
  the CA3 harness and briefly attributed to the index criterion; the three-way rerun
  shows it is entirely CA4 (all 1,107 are insertion reads lost by the prefilter, the
  bare aligner agrees with the index on 10,000 / 10,000). Re-attributed, not a CA3 effect.

## What held up (executed, not just read)

- **Quality trimming.** `quality_trim_index` equals a port of BWA's
  `bwa_trim_read` (3' end) and its mirror (5' end) on 40,000 random quality strings,
  Phred+33 and Phred+64, cutoffs 0–40, including the `start >= stop → (0, 0)` rule
  (`heldup_qualtrim_vs_reference.out`). `-q 20 --quality-base 64` through the CLI
  equals the port (CA2 harness, control row). The `doc/algorithms.rst:162-190`
  description is what the code does.
- **`--nextseq-trim`.** Equals the documented variant (G counted as `cutoff − 1`)
  on 40,000 cases, both offsets.
- **Poly-A / poly-T.** `poly_a_trim_index` equals an implementation of the prose
  rule (≤ 20 % non-A, +1/−2 score, shorter suffix wins ties, tails < 3 ignored) on
  30,000 cases in both directions; the `errors·5 ≤ length` integer test is exact.
- **Expected errors.** `expected_errors` equals `Σ 10^(−q/10)` to 5.4e-16
  relative on 10,000 strings at both offsets; the 94-entry `SCORE_TO_ERROR_RATE`
  table deviates 0.00e+00 from `10^(−q/10)`; Phred 94 raises. `--max-ee` discards on
  `>` (a read at exactly the threshold is kept), as documented.
- **Length and N filters.** `TooShort` is `<` (a read of exactly `-m` is kept: 10 of 10
  30-nt reads kept under `-m 30`), `TooLong` is `>`; `--max-n 2`, `0.1` and `0` equal
  the count / fraction / any-N references on 600 reads
  (`heldup_filters_paired_cli.out`).
- **Paired-end filtering.** `-m 30:20` with `--pair-filter any | both | first`
  equals the or / and / R1-only references (243 / 529 / 336 pairs kept); `-m 30`
  applies to both mates; `--discard-untrimmed` uses `any` with `-a -A` (41 pairs, both
  mates trimmed) and is overridden to `both` when only `-a` is given (152 = R1 trimmed),
  matching `cli.py:861-869`.
- **Interleaved and multi-core.** For a pipeline with `-a -A -q 20 -m 20 --trim-n
  --max-n 0.2`, `--interleaved` input, `--interleaved` output and `-j 3` are all
  byte-identical to two-file `-j 1` (187 pairs).
- **`-l`, `-u`, `--trim-n`, `--strip-suffix`** equal their one-line references on 600
  reads.
- **Aligner invariants** (`heldup_aligner_properties.out`, ~100,000 alignments over
  seven adapter types, `-e` ∈ {0.1, 0.2, 0.25, 1, 2}, `min_overlap` ∈ {1, 3, 5}, with
  and without indels, adapters with and without N): errors = edit distance of the
  aligned substrings (Hamming without indels); `errors / (aligned adapter length − #N)
  ≤ rate` as an exact rational; overlap ≥ `min_overlap`; anchored types always align
  the full adapter; never both prefixes skipped; a planted exact occurrence is
  returned unless an earlier acceptable one exists (N1). For regular 3' and 5' adapters
  the prefilter and the bare aligner agree on 20,000 / 20,000 reads.
- **N wildcards.** The error rate is computed on the non-N part of the aligned
  adapter (`_align.pyx:504-510`, `:543-551`), as `doc/guide.rst:685-704` says (P2 = 0
  with N-containing adapters).
- **Absolute errors as documented for unaffected lengths.** `-e 1` on 48- and 50-nt
  adapters and `-e 2`/`-e 3` on 50/30 nt behave as specified (CA1 Part B controls).

## Not audited here

`--revcomp` beyond reading its score comparison; linked-adapter `required`/
`optional` semantics beyond reading `parser.py:496-507` and `adapters.py:1215-1227`;
`--pair-adapters` and combinatorial demultiplexing; the `rightmost` adapters new in
5.2; `--rename` templates; the report and JSON statistics (`report.py`, including the
`ErrorRanges` display that floors the same product as CA1, `report.py:428-429`); BAM
input; `--action=retain/crop` with linked adapters.
