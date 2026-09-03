# Cutadapt audit against 331 published papers (2021–2026)

_Twelfth audit in the series. Generated 2026-09-03 against `marcelm/cutadapt` `main` @
`50e9fb8d` (2026-06-26, version string 5.3.dev15). Focus: the code paths that decide
which bases and which reads survive — the semi-global aligner and its error-rate
arithmetic, adapter-type semantics and best-match selection, the k-mer prefilter,
BWA-style quality trimming, the expected-error and length/N filters, and paired-end
filtering — verified by executing the shipped code._

## What this is

The six-journal survey found **331 papers** in *Nature* (150), PNAS (145), *Cell* (28)
and *Science* (8), 2021–2026, that used Cutadapt — in nearly every sequencing
pipeline, directly or through Trim Galore (33 papers name the wrapper). Its trimming
core was read in full on `main` and every suspicion was run through the installed
package (master, editable Cython build in a Python 3.12 venv; the 5.2 wheel from
PyPI, the latest release; and the 4.1, 4.2, 4.3, 4.4, 4.5, 4.9, 5.0 and 5.1 wheels
for version scope)
on synthetic reads with known truth, against independent Python ports of the
documented rules or against the package's own bare aligner run without its
prefilter.

## Findings (details and line citations in [`component-reviews/trimming-core.md`](component-reviews/trimming-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **CA1** | **CONFIRMED on `main`, 5.2 and every wheel executed (4.1–5.1)** | An absolute number of errors (`-e N`, N ≥ 1) becomes the rate N/len, and for adapter lengths 49, 98, 103, 107, 161, 187, … (N = 1, 2, 4), 47, 94, 147, … (N = 3), 77, 154 (N = 5) the product len × rate rounds to just below N in floating point, so one allowed error is lost everywhere it is floored: aligner band and acceptance test, `--no-indels` comparer, demultiplexing index, k-mer heuristic. `-e 1` on a 49-nt adapter finds the adapter only with 0 errors (CLI: 0 of 300 one-substitution reads trimmed; 300/300 with `-e 1.0000001`). Decimal rates people type (`0.05`–`0.3`) are unaffected up to 300 nt. |
| **CA2** | **CONFIRMED on `main`, 5.2 and every wheel executed (4.1–5.1)** | `--max-expected-errors` and `--max-average-error-rate` compute expected errors with Phred+33 regardless of `--quality-base`; on Phred+64 data the sum is ~1,259× too small and nothing is discarded (2,000 reads with 3–30 expected errors: all kept under `--max-ee 0.5/1/2 --quality-base 64`; `-q` honours the base correctly). Phred+64 data are rare today; the flag exists for exactly that data. |
| **CA3** | **CONFIRMED on `main`, 5.2, 5.1, 5.0** (introduced with the 5.0 index rewrite); 4.1–4.9 assign as `--no-index` does | The demultiplexing index (default for ≥ 2 anchored adapters) ranks candidates by number of matching bases and stores that count as the match `score`; the rest of Cutadapt ranks by the documented Cutadapt-4 alignment score (match +1, mismatch −1, indel −2). An 11-nt barcode matching exactly loses to a 12-nt barcode matching with one insertion (100/100 reads to A by default, 100/100 to B with `--no-index`); on random barcode sets the two rules agree on 10,000/10,000 (mixed lengths) and 9,998/10,000 (same length, tie cases); mixed lists of indexed barcodes and a regular adapter compare incompatible scores. |
| **CA4** | **CONFIRMED on `main`, 5.2 and every wheel from 4.3 on**; absent on 4.1 and 4.2 (before the 4.3 prefilter) | The k-mer prefilter searches anchored (`^ADAPTER`, `ADAPTER$`) and non-internal (`XADAPTER`, `ADAPTERX`) adapters in a window exactly as long as the adapter, so an occurrence with one inserted base — one position longer — is rejected before the aligner runs whenever exactly one error is allowed (10–19-nt adapters at the default `-e 0.1`, or `-e 1` at any length): 37–44 % of such reads are silently not trimmed (`-g ^NEXTERA`: 257/400 vs 400/400 for `-g NEXTERA`; 34-nt Illumina `-e 1`: 392/700 vs 700/700). Regular `-a`/`-g` adapters, `--no-indels` and index-based demultiplexing are unaffected. |
| N1 | note, documentation | The `Aligner` docstring's tie-break ("fewest errors, then leftmost") is not what the code or `doc/algorithms.rst` say (leftmost wins ties); executed. |
| N2 | note, latent, API only | `PrefixComparer` subtracts the lowercase-n count instead of adding it (`effective_length` 12 instead of 8 for `ACGTACGTnn`); unreachable from the CLI, which upper-cases adapters. |
| N3 | note, documentation | The Python snippet for the poly-A algorithm in `doc/algorithms.rst` iterates `enumerate(range(n))` and never trims; the Cython code is right. |
| N4 | note, design, minor | `--trim-n` and `--nextseq-trim` are case-sensitive (`N`, `G`) while adapter matching upper-cases reads. |

Four own suspicions were withdrawn by execution (stale Ukkonen-band cells; the
"planted exact occurrence not returned" cases, which are the documented leftmost
rule; `remainder()` under `--times 2`; and the first attribution of 1,107 "index
assigns, `--no-index` does not" reads to CA3 — they are CA4). They are recorded in
the review.

**Held up under execution:** BWA-style quality trimming equals a port of
`bwa_trim_read` and its 5' mirror on 40,000 random strings at both offsets;
`--nextseq-trim` and poly-A/poly-T equal their documented rules (40,000 / 30,000
cases); `expected_errors` equals Σ 10^(−q/10) to 5e-16 and the 94-entry table is
exact; `-m` keeps a read of exactly the minimum, `-M`, `--max-n` as count/fraction/0,
`--pair-filter any|both|first`, the `--discard-untrimmed` pair-filter defaults, `-l`,
`-u`, `--trim-n`, `--strip-suffix` all equal one-line references on 600 random
pairs; `--interleaved` in/out and `-j 3` are byte-identical to two-file `-j 1`;
across ~100,000 random alignments of seven adapter types the reported errors equal
the edit distance of the aligned substrings, the error-rate bound holds as an exact
rational on the non-N part, overlap and anchoring constraints hold, both prefixes
are never skipped, and for regular 3'/5' adapters the prefilter never suppresses an
alignment. Not audited: `--revcomp` beyond its score comparison, linked-adapter
`required/optional` semantics, `--pair-adapters`, combinatorial demultiplexing, the
5.2 `rightmost` adapters, `--rename`, the report/JSON statistics, BAM input.

## How the papers use Cutadapt (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 95 (1.x 60, 2.x 44, 3.x 37, 4.x 37; top: 1.18 ×21, 3.4 ×19, 4.1 ×17, 1.15 ×9, 2.8 ×8) |
| quality trimming (`-q` / Phred cutoff) | 79 (cutoffs named: 30 ×10, 20 ×7, 10 ×7) |
| RNA-seq / ATAC-ChIP-CUT&RUN / single-cell / amplicon-16S-primer | 74 / 46 / 45 / 55 |
| paired-end | 65 |
| minimum length (`-m`) | 57 (values: 20 ×9, 25 ×6, 15 ×5) |
| demultiplexing / barcodes | 56 |
| 3' adapter (`-a`) / 5' adapter (`-g`) / R2 adapter (`-A`/`-G`) / `-b` | 36 / 11 / 5 / 1 |
| Trim Galore wrapper | 33 |
| maximum length (`-M`) | 28 |
| Illumina TruSeq / universal / Nextera adapter named | 24 |
| CRISPR screen / UMI / small RNA / bisulfite / nanopore | 21 / 20 / 15 / 14 / 16 |
| error rate (`-e`) / overlap (`-O`) | 13 (`0.2` ×3, `0.1` ×2, `1` ×1) / 12 (`5` ×5, `3` ×2) |
| poly-A / `-u` / `-l` / `--times` | 10 / 7 / 4 / 3 |
| `--max-ee` / `--max-n` / `--nextseq-trim` / `--interleaved` | 3 / 2 / 2 / 1 |

Exposure by finding: CA1 needs the integer form of `-e` (named once in the cache)
with an adapter of one of the listed lengths; CA2 needs Phred+64 data (none named);
CA3 needs index demultiplexing with barcodes that are near-prefixes of each other
(56 papers demultiplex or mention barcodes, all on 4.x or older versions where the
executed 4.1–4.9 wheels assign as `--no-index` does); CA4 needs an anchored or
non-internal adapter with ≤ 1 allowed error on 4.3 or later (11 papers name a 5'
adapter, 37 name a 4.x version). None of these can be decided from the cache.

**Profiling caveat.** As for the Seurat and Scanpy audits, this session had no
route to Europe PMC, so `cutadapt_profile.py` ran in `--offline` mode over the
survey's stored evidence snippets; every record in `cutadapt_profiles.jsonl` is
`source: survey_cache` and every count above is a lower bound. Rerun without
`--offline` from a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- `CONTRIBUTING.rst`: one topic per PR, issue first for larger changes, tests,
  changelog entry, black formatting, Google docstrings. No PR template, no pinned
  policy issue, no discussions link.
- `.github/ISSUE_TEMPLATE/bug_report.md`: free text asking for Cutadapt/Python
  version, install method, command line, an example read, output and expected
  output — the `upstream/issue-ca*.md` texts follow those fields.
- `CHANGES.rst`: bullets under a `development version` heading, prefixed with the
  issue number once it exists; `tox.ini`: `black==22.3.0`, `flake8`, `mypy`, tests on
  3.10–3.13.
- CA1, CA2 and CA4 are crisp bug fixes; CA3 changes demultiplexing results and
  should go to the maintainer as an issue before its PR. None has a prior issue
  (tracker searched 2026-09-03). **The kit is in [`upstream/`](upstream/)**: four
  issue texts with reproductions run on `main` and 5.2, four `git am`-able patches
  (fix + tests + changelog; every new test fails on unmodified `main` and the full
  suite passes with each patch), PR bodies, and the list of documents read.

## Files

| file | what |
|---|---|
| `cutadapt_profile.py`, `cutadapt_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/trimming-core.md` | the review: CA1–CA4, N1–N4, withdrawn suspicions, held-up list, not-audited list |
| `verify/ca1_absolute_errors_fp_boundary.py` (+ `.out`, `.v5.2.out`) | CA1: closed form over (N, n, L); shipped classes; CLI |
| `verify/ca2_max_ee_quality_base.py` (+ `.out`, `.v5.2.out`) | CA2: CLI filters vs Python reference on Phred+33 and Phred+64 files |
| `verify/ca3_index_vs_noindex.py` (+ `.out`, `.v5.2.out`) | CA3: minimal example, random barcode sets (three-way), score field, CLI |
| `verify/ca4_kmer_prefilter_insertions.py` (+ `.out`, `.v5.2.out`) | CA4: `match_to` vs bare aligner per insertion position; CLI; anywhere blind spot |
| `verify/version_scope_cli.py` (+ `.master.out`, `.v5.2.out`, `.v5.1.out`, `.v5.0.out`, `.v4.9.out`, `.v4.5.out`, `.v4.4.out`, `.v4.3.out`, `.v4.2.out`, `.v4.1.out`) | the four findings through the CLI only, on every release that builds here |
| `verify/heldup_qualtrim_vs_reference.py` (+ `.out`) | held-up: BWA port, nextseq, poly-A, expected errors, predicate boundaries |
| `verify/heldup_aligner_properties.py` (+ `.out`) | held-up: aligner invariants and prefilter equivalence on ~100k random alignments |
| `verify/heldup_filters_paired_cli.py` (+ `.out`) | held-up: `-m/-M/--max-n`, pair filter, interleaved, `-j`, modifiers |
| `verify/note_aligner_tiebreak.py`, `note_prefixcomparer_lowercase_n.py`, `note_misc_docs_lowercase_times.py` (+ `.out`) | N1–N4 and withdrawn W3 |
| `upstream/` | filing kit: issue texts, MCVE scripts and outputs, patches 0001–0004, PR bodies, documents read |

Harnesses need an install of the version under test: `uv venv --python 3.12 venv
&& uv pip install -e <cutadapt clone>` (Cython and a C compiler) or `uv pip install
cutadapt==<version>`. Releases 3.4 and 1.18 (the cohort's most-cited versions
with 4.1) do not build on Python 3.11/3.12 here (`longintrepr.h`), so their status
for CA1/CA2 is by reading only (the code paths are unchanged since 3.0 / 2.9).

## Next steps

1. File CA1, CA2 and CA4 as issues + PRs from the kit; file CA3 as an issue and
   open its PR after the maintainer's view on the ambiguity rule. Record numbers
   and responses here and in the top-level table.
2. Extend the review to `--revcomp`, linked-adapter `required/optional` handling and
   `--pair-adapters`, the remaining read-selection paths.
3. Full-text profiling rerun when Europe PMC is reachable, to see which papers use
   `-e N`, anchored primers with ≤ 1 error, or `--no-index`.
