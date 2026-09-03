# Component: fastp trimming, filtering and reporting core (`master` @ `dce5c40`, 2026-09-01, version string 1.3.6)

Read in full on `master`: `src/filter.cpp` (263 lines: `passFilter`,
`passLowComplexityFilter`, `trimAndCut`, index filtering),
`src/adaptertrimmer.cpp` (184: `trimBySequence`, `trimByMultiSequences`,
`trimByOverlapAnalysis`), `src/matcher.cpp` (100: the one-gap matcher),
`src/overlapanalysis.cpp` (210: overlap detection and merging),
`src/basecorrector.cpp` (106), `src/polyx.cpp` (129), `src/duplicate.cpp` (168),
`src/evaluator.cpp` (633: adapter auto-detection, read-number and sequence-length
estimation, overrepresented-sequence pre-scan), `src/stats.cpp` (982: per-cycle
counters, Q20/Q30, GC, k-mers, the JSON block), `src/umiprocessor.cpp` (88),
`src/filterresult.cpp` (473), `src/options.cpp` (525) and `src/main.cpp` (522:
option wiring and the order of the evaluation steps); targeted reads of
`src/peprocessor.cpp` and `src/seprocessor.cpp` (the per-read pipeline order,
insert-size statistics, adapter-dimer rule, split accounting),
`src/jsonreporter.cpp`, `src/threadconfig.cpp`, `src/simd.cpp` and
`src/knownadapters.h`. `README.md` is the statement of intended behaviour that
the findings are measured against.

Every suspicion was **executed on the shipped binary**: `master` built from
source (`make -j`, g++ 13.3, isa-l 2.31.0 / libdeflate 1.19 / libhwy 1.0.7 from
Ubuntu packages — the Makefile links them dynamically when no static library is
present, and `./fastp test` passes), harnesses in `../verify/` with captured
output. Each confirmed finding was also run on the release tags v1.3.6 (the
latest release), v1.0.0, v0.26.0, v0.23.4, v0.23.2, v0.22.0, v0.20.1 and v0.20.0
— every version the survey cohort names except 0.21.0, which has **no tag in the
repository** (the tags go v0.20.1 → v0.22.0), so v0.22.0 was built in its place.
References are independent Python ports of the documented and of the coded rules,
run on 10^4–10^5 synthetic reads with known truth (`../verify/fastp_ref.py`).

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### FP1 — CONFIRMED on `master` and on every release built (v0.20.0 … v1.3.6): `--cut_front`/`--cut_tail` discard `cut_window_size − 1` extra bases when combined with `--trim_front1`/`--trim_tail1`

**Code.** `Filter::trimAndCut` (`src/filter.cpp:68-191`) scans windows from
`front` and stops on the first one whose summed quality reaches
`w * (33 + cut_front_mean_quality)` (`:109-119`). It then advances the cut to the
end of that window (`:121-122`):

```cpp
        // the trimming in front is forwarded and rlen is recalculated
        if(s >0 )
            s = s+w-1;
```

Advancing to `s+w-1` is the implementation of "drop the bases in the [failing]
window": windows overlap, so dropping the last failing window, which ends at
`s+w-2`, means keeping from `s+w-1`. The guard exists to skip that advance when
the very first window already passes — but it compares `s` with the start of the
*untrimmed* read instead of `front`, the position the scan started from. With
`--trim_front1 > 0` the scan starts at `front > 0`, the guard is always true, and
`w-1` good bases are dropped from every read. `:189-190` is the 3' mirror, where
`if(t < l-1)` should be `if(t < l-tail-1)`. `--cut_right` is unaffected: it only
recomputes `rlen` when a window actually failed (`:157-161`).

**Verified** (`../verify/fp1_cut_window_edge.py`, `.out`). Part A, 100 reads of
60 nt in which *every* base is Q40, so no window can fail:

| options | expected | fastp |
|---|---|---|
| `-f 5` | 55 | 55 |
| `--cut_front` | 60 | 60 |
| `--cut_front -f 5` | 55 | **52** |
| `--cut_front -f 5 -W 10` | 55 | **46** |
| `--cut_front -f 1` | 59 | **56** |
| `--cut_tail -t 5` | 55 | **52** |
| `--cut_tail -t 5 -W 10` | 55 | **46** |
| `--cut_front --cut_tail -f 5 -t 5` | 50 | **44** |
| `--cut_right -f 5` / `--cut_right -t 5` | 55 | 55 |

Part B, 20,000 random reads (40–150 nt, Phred 2–40), against two ports of
`trimAndCut` that differ only in those two comparisons: the binary equals the
as-coded port on **20,000 / 20,000** reads in all eight option sets, and differs
from the corrected port on 11,509 (`--cut_front -f 5`), 11,638 (`--cut_tail -t 5`),
18,100 (`--cut_tail -t 3 -W 6 -M 15`) and 16,417 (`--cut_front --cut_tail -f 4 -t 4`)
of them. Part C, the same reads under the default filters with `-l 15`:
`--cut_front -f 5` keeps 18,119 reads and 1,571,378 bases where the corrected
rule keeps 19,999 reads and 1,742,512 bases — 1,880 reads and 9.8 % of the bases
lost. Version scope (`../verify/version_scope_cli.*.out`): 52 nt instead of 55 on
`master`, v1.3.6, v1.0.0, v0.26.0, v0.23.4, v0.23.2, v0.22.0, v0.20.1 and
v0.20.0; the code dates from 2018 (`8746036`).

**Who is exposed.** Anyone combining a sliding-window cutter with global
trimming. In the cohort cache 2 papers name `--cut_front`, 4 `--cut_tail`, 7
`--trim_front1` and 2 `--trim_tail1` (lower bounds), and **no cached paper names
both** — the one paper that combines global trimming with a window cutter
(PMC12390848, `--trim_tail1 1 --trim_tail2 1 --cut_right …`) uses `--cut_right`,
which is not affected. The exposure is therefore unquantified rather than
established: `-f`/`-t` with `-5`/`-3` is a common recipe (it is what issue #474
reports) but the survey cache cannot show how many of the 117 papers used it.

**Fix shape** (patch `../upstream/0001-…`): compare with `front` and
`l-tail-1`; two new cases in `Filter::test()` on an all-Q40 read, both failing
on unmodified `master`.

**Upstream.** Already reported: issue **#474** (2023-03-21, open) is exactly
this, with `-f 6 -5 -3` removing nine bases instead of six. The kit therefore
drafts the text as a comment on #474 rather than a new issue. #297 (2020, open)
asks what `trim_*` and `cut_*` do together and was never answered.

### FP2 — CONFIRMED on `master`, v1.3.6, v1.0.0 and v0.26.0: an auto-detected built-in adapter longer than 60 nt is printed and then thrown away, so adapter trimming is silently disabled

**Code.** `src/main.cpp:458-461` (and `:474-477` for read 2):

```cpp
            string adapt = eva.evalAdapterAndReadNum(readNum, false);
            if(adapt.length() > 60 )
                adapt.resize(0, 60);
            if(adapt.length() > 0 ) {
```

`std::string::resize(size_type n, char c)` resizes to `n` and pads with `c`, so
`resize(0, 60)` **empties** the adapter instead of truncating it to 60
characters. The `if` on the next line is then false: fastp prints "No adapter
detected for read1", sets `adapter.sequence = ""`, performs no adapter trimming
for SE data, and (because `Options::adapterCuttingEnabled()` is false) drops the
whole `adapter_cutting` section from the JSON report — one line after printing
the correct adapter to stderr.

The line dates from 2018 but was unreachable until v0.26.0: the nucleotide-tree
detector truncates its candidate to 60 characters *before* matching it against
the built-in table (`src/evaluator.cpp:523-526`), so it can only return an
adapter of at most 60 nt. `Evaluator::checkKnownAdapters` (`:220-343`, added in
v0.26.0, called first at `:366`) returns the built-in entry at full length, and
139 of the 234 entries in `src/knownadapters.h` are longer than 60 nt.

**Verified** (`../verify/fp2_known_adapter_over60.py`, `.out`; 20,000 SE reads of
100 nt per adapter, every read reading through into it):

| built-in adapter | length | printed by fastp | auto-detection: reads trimmed | `-a <same>`: reads trimmed |
|---|---|---|---|---|
| TruSeq Universal | 58 | 58 nt | 20,000 | 20,000 |
| TruSeq Read 1 | 33 | 33 nt | 20,000 | 20,000 |
| **TruSeq Small RNA RPI1** | 63 | 63 nt | **no `adapter_cutting` section, 0** | 20,000 |
| TruSeq Adapter Index 5 | 63 | 33 nt | 20,000 | 20,000 |
| Reverse_adapter | 64 | 33 nt | 20,000 | 20,000 |
| **RNA PCR Primer Index 35** | 63 | 63 nt | **0** | 20,000 |
| pcr_dimer | 119 | 58 nt | 20,000 | 20,000 |

A long built-in adapter that has a shorter built-in **prefix** is shielded:
`checkKnownAdapters` keeps a candidate only on a strictly larger hit count and
walks the table in `std::map` (lexicographic) order, so the shorter prefix wins
the tie and is returned instead (rows 4, 5, 7 above). 85 of the 139 long entries
have no such prefix — 48 TruSeq Small RNA RPI primers, 36 RNA PCR Primer index
primers and one `PrefixPE/2` — and those are the ones that get discarded. On
2,000 reads with RPI1 the adapter stayed in 2,000 of them (143,139 adapter bases
in the output). For paired-end data with `--detect_adapter_for_pe` the overlap
analysis still catches most read-throughs, but 24,735 of 40,000 reads were
trimmed instead of 40,000, and `read1_adapter_sequence` is reported as
`unspecified`.

Version scope (`../verify/version_scope_cli.*.out`): the 63-nt adapter is printed
and then discarded on `master`, v1.3.6, v1.0.0 and v0.26.0. On v0.23.4, v0.23.2,
v0.22.0, v0.20.1 and v0.20.0 nothing is printed and nothing is trimmed either,
but for a different reason — those versions never produce a candidate longer than
60 nt, so they simply fail to detect this adapter class at all.

**Who is exposed.** Single-end libraries whose adapter is one of the 85, i.e.
small-RNA/miRNA libraries above all (they are single-end and use exactly the
TruSeq Small RNA RPI primers), on v0.26.0 or later. The cohort cache names no
small-RNA paper and one paper on 1.0.1 (lower bounds), so no cohort paper is
demonstrably exposed; the defect is in the current release.

**Fix shape** (patch `../upstream/0002-…`): `adapt.resize(60);` in both places,
plus `scripts/test_known_adapter_over60.sh` in the style of the project's
existing `scripts/test_issue_697_stdout_merge.sh` (fails without the fix: 0 of
20,000 trimmed; passes with it: 20,000).

**Upstream.** No prior report. Nearest: #673 (2026, auto-detection finds far
fewer adapters than an explicit `--adapter_sequence`, but that run is paired-end
without `--detect_adapter_for_pe`, so no detection happens at all), #129 "Not
detecting the adapter in miRNAseq" (2019, predates `checkKnownAdapters`), #222,
#454, #557, #693.

### FP3 — CONFIRMED on `master`, v1.3.6, v1.0.0 and v0.26.0: the one-indel adapter search only ever tests read position 0, so an adapter with an indel is never trimmed

**Code.** `AdapterTrimmer::trimBySequence` (`src/adaptertrimmer.cpp:64-157`)
tries every offset `pos`. The exact-match loop passes the offset into the
comparison (`:91-93`):

```cpp
        int mismatch = fastp_simd::countMismatchesBounded(
            adata + startOffset, rdata + startOffset + pos,
            cmplen - startOffset, allowedMismatch);
```

The two gapped loops added in v0.26.0 (`eb461d5`, "support one base
insertion/deletion in SE mode adapter trimming") do not (`:110`, `:127`):

```cpp
            bool matched = Matcher::matchWithOneInsertion(rdata, adata, cmplen, allowedMismatch);
            ...
            bool matched = Matcher::matchWithOneInsertion(adata, rdata, cmplen, allowedMismatch);
```

`rdata` is the read from base 0. For every `pos` in `[0, rlen-alen-1]` the call
is byte-for-byte identical — same pointers, same `cmplen`, same allowance — so
the entire loop is a single test of "does the read *begin* with the adapter,
allowing one indel"; `pos` only selects where the read would be cut. The same
applies to the deletion loop.

**Verified** (`../verify/fp3_indel_adapter_offset.py`, `.out`; 33-nt TruSeq Read
1 adapter given with `-a`). Part A, 200 reads per group, adapter starting at base
40:

| group | trimmed to 40 nt | untrimmed |
|---|---|---|
| exact adapter (control) | 200 | 0 |
| one substitution | 200 | 0 |
| + 1 inserted base (position 5 / 16 / 28) | 0 / 0 / 0 | 200 / 199 / 200 |
| − 1 deleted base (position 5 / 16) | 0 / 0 | 200 / 200 |

Part B, 5,000 random reads with planted occurrences: the binary equals a port in
which the offset is ignored on **5,000 / 5,000** reads, and equals the port with
the offset applied on 3,544. Trimmed: 978/978 exact, 1,049/1,049 substitution,
**263 of 993** insertion and **266 of 967** deletion reads (those come from the
exact loop catching a short partial match at the 3' end), 0 of 1,013 adapter-free
reads. Part C, the same read content with the adapter moved: at position 0 the
read is trimmed to 0 nt, at positions 1, 5, 20, 40 and 60 it is not trimmed at
all. Version scope: identical on `master`, v1.3.6, v1.0.0 and v0.26.0; v0.23.4
and older have no gapped search at all (`mcve_outputs.txt` shows the
position-0 read untrimmed there).

**Who is exposed.** Single-end runs with `--adapter_sequence`, and the
paired-end fallback path that uses `--adapter_sequence`/`--adapter_sequence_r2`
when the overlap analysis fails — i.e. exactly the reads that carry a sequencing
indel in the adapter, the case issue #518 reports. The size of the effect
depends on the library's indel rate; on the synthetic battery it is the
difference between 26 % and 100 % of such reads being trimmed.

**Fix shape** (patch `../upstream/0003-…`): pass `rdata + pos` in both loops.
With the fix the binary equals the intended port on 5,000 / 5,000 reads,
993/993 insertions and 967/967 deletions are trimmed, and none of the 1,013
adapter-free reads is trimmed. Two new cases in `AdapterTrimmer::test()`, both
failing on unmodified `master`.

**Upstream.** Already reported as a symptom: issue **#518** (2023-08-22, open),
"fastp can not remove adapter when the read sequence has indels in the adpter" —
the gapped search was added for it. The kit drafts the text as a comment there.

## Notes (verified, not filed as findings)

### N1 — the overlap mismatch limits apply to the first 50 bases of the overlap only

`OverlapAnalysis::analyze` (`src/overlapanalysis.cpp:28-44`) compares at most
`complete_compare_require = 50` characters against `--overlap_diff_limit` /
`--overlap_diff_percent_limit`; if the prefix passes and the overlap is longer, it
recounts the mismatches over the whole overlap **without re-testing the limit**:

```cpp
        const int protectedPrefix = min(len, complete_compare_require);
        mismatchCount = fastp_simd::countMismatchesBounded(a, b, protectedPrefix, overlapDiffLimit);
        if (mismatchCount > overlapDiffLimit) return false;
        if (len > complete_compare_require) mismatchCount = fastp_simd::countMismatches(a, b, len);
        return true;
```

Executed (`../verify/notes_overlap_polyg_threads.out`, 200 pairs per row, 80 nt
overlap, default limits): with 6, 10, 20 or **30** mismatches placed in overlap
positions 50–79 all 200 pairs are still merged; with 6 or more in positions 0–49
none is. This is deliberate (the project's own unit test asserts it: a pair with
30 mismatches beyond position 50 is accepted with `overlapDiffLimit = 0`,
`overlapanalysis.cpp:200-209`, and commit `df27ddc` calls it "restore upstream
overlap matching semantics"), but the README documents `--overlap_diff_limit` as
"the maximum number of mismatched bases to detect overlapped region" with no
mention of the 50-base window. It decides PE adapter trimming, base correction,
merging and the insert-size histogram.

### N2 — `--overlap_len_require N` requires an overlap **longer** than N

The scan bounds are `while (offset < len1-overlapRequire)` and
`while (offset > -(len2-overlapRequire))` (`:48`, `:73`), so the shortest overlap
that can be accepted is `N+1`. Executed: with `--overlap_len_require 30`, 0 of
200 pairs with a 30 nt overlap merge and 200 of 200 with a 31 nt overlap.

### N3 — the insert-size histogram is filled by worker thread 0 only

`statInsertSize` is called under `if(config->getThreadId() == 0)`
(`src/peprocessor.cpp:449`, `:497`), so the reported histogram and its peak are
estimated from thread 0's share of the packs. Executed on 4,000 pairs with a
fixed insert size of 120: `-w 1` counts 4,000 pairs, `-w 2` 2,000, `-w 3` 2,000,
`-w 4` 1,000, `-w 8` 1,000. The peak is 120 in all cases, so the estimate is
unbiased here, but the histogram counts in the JSON depend on `--thread` and are
not the number of pairs processed. The report does not say so.

### N4 — `--poly_g_min_len N` already trims a tail of N−1 G

`PolyX::trimPolyG` tests `if(i >= compareReq)` after the loop
(`src/polyx.cpp:39`), where `i` is the index at which the scan stopped, while
`PolyX::trimPolyX` tests `if(pos+1 >= compareReq)` (`:98`). Executed with
`--poly_g_min_len 10` on 200 reads per row: tails of 6/7/8 G are kept (3/12/52
of 200 trimmed, those by chance in the preceding bases), tails of **9** G are
trimmed 200/200, as are 10, 11 and 12. The default `--poly_g_min_len 10`
therefore trims from 9 G on.

### N5 — `-m/--merge` silently switches on base correction

`Options::validate` sets `correction.enabled = true` whenever merging is enabled
(`src/options.cpp:119-121`). Executed: a PE run with `-m` reports
`corrected_bases: 200` although `-c` was not given, and plain PE reports no
`corrected_bases` at all. The README documents `--correction` as "not enabled by
default, specify -c" and does not mention that `-m` turns it on, so merged and
unmerged output carries quality-based base substitutions the user did not ask
for.

### N6 — the adapter search needs 5 matching bases at the read end, not `matchReq` = 4

The exact-match loop stops at `pos < rlen-matchReq` (`src/adaptertrimmer.cpp:87`)
with `matchReq = 4`, so the shortest comparison is 5 characters. Executed with
a 33-nt adapter: reads ending in 2, 3 or 4 adapter bases are not trimmed (0/200),
reads ending in 5 or more are (200/200). Worth knowing when comparing fastp's
adapter counts with cutadapt's `-O` semantics.

### N7 — by reading only: the overrepresented-sequence scans skip the last window

Both the candidate pre-scan (`Evaluator::computeOverRepSeq`) and the counting
pass (`Stats::statRead`, `src/stats.cpp:276`) iterate `for(int i=0; i<len-step; i++)`,
so a sequence occurring exactly at the read end is never counted; the pre-scan
also uses absolute count thresholds (3/5/20/100/500) over the first ~10,000 reads
regardless of the file size, while the reported counts come from a
1-in-`--overrepresentation_sampling` sample. Not executed against a reference;
recorded as a reading-level observation.

## Withdrawn (own suspicions that verification killed)

- **W1 — `--cut_right` leaking into the `--trim_tail1` region.** The "keep the
  good bases in the window" scan uses `l-1` rather than `l-tail` as its bound
  (`src/filter.cpp:159`), so it looked as though `rlen` could exceed
  `l-front-tail` and undo the tail trim. It cannot: the scan stops at the first
  base below the cutoff, and a window whose mean is below the cutoff must contain
  one, so it always stops inside the window, at most at `l-tail-2`. Executed:
  `--cut_right -f 5` and `--cut_right -t 5` on all-Q40 reads give exactly 55 nt.
- **W2 — integer division in `--average_qual`.** `(totalQual / rlen) < avgQualReq`
  (`src/filter.cpp:38`) truncates the mean, but for an integer threshold
  `floor(m) < T ⇔ m < T`, so the filter is exact. Executed at the boundary: a
  read with mean quality exactly 20 is kept by `-e 20` and dropped by `-e 21`.
- **W3 — uninitialised reads in `Matcher::matchWithOneInsertion`.** Both
  accumulator loops can break early, leaving the tail of
  `accMismatchFromLeft` uninitialised (`src/matcher.cpp:10-45`). The decision
  loop reads `accMismatchFromLeft[i-1]` only after its own guard
  `accMismatchFromLeft[i-1] + accMismatchFromRight[cmplen-1] > diffLimit`, which
  fires at the index where the accumulator loop broke (that element *is*
  assigned), so no uninitialised element is ever read; the right-hand loop fills
  its prefix explicitly. Not a defect.
- **W4 — bias of the hash-based duplication estimator.** Executed against known
  duplication levels on 20,000 reads: true 0.0000 / 0.2000 / 0.5000 → fastp
  0.0000 / 0.2000 / 0.5000 in both SE and PE mode, and `--dedup` keeps exactly
  the number of distinct reads (20,000 / 16,000 / 10,000).
- **W5 — reads lost or duplicated by `--split`.** Executed: `--split 4`,
  `--split 7` and `--split_by_lines 4000` on 5,000 reads produce 4, 7 and 6 files
  with 5,000 reads, none duplicated, none missing.

## What held up (executed, not just read)

- **The quality, length and complexity filters.** On 20,000 reads spanning
  lengths 5–150, four quality regimes, N-rich and low-complexity sequences, the
  set of surviving reads is identical to an independent port of `passFilter` for
  all 13 option sets tested (defaults, `-q 30 -u 20`, `-q 20 -u 0`, `-n 0`,
  `-n 3`, `-e 25`, `-e 30 -q 25 -u 30`, `-l 50`, `-l 50 --length_limit 100`,
  `-y`, `-y -Y 50`, `-Q`, `-L`), and the six `filtering_result` counters match
  the reference reasons exactly (1,406 / 14,934 / 1,168 / 1,003 / 743 / 746).
  Every threshold boundary behaves as documented (`-l N` keeps a read of exactly
  N, `--length_limit N` keeps exactly N, `-n N` keeps exactly N Ns, `-u N` keeps
  exactly N %, `-y -Y 50` keeps complexity exactly 0.5).
- **The reported statistics.** `total_reads`, `total_bases`, `q20_bases`,
  `q30_bases`, `q20_rate`, `q30_rate`, `gc_content` and `read1_mean_length`
  equal direct counting on the input (Q20 = `qual >= '5'`, Q30 = `qual >= '?'`,
  mean length truncated to an integer). The 1,024-entry `kmer_count` table
  matches a direct 5-mer count, N-containing k-mers excluded, with 0 mismatching
  entries out of 1,024 and 1,217,077 k-mers counted.
- **poly-G and poly-X trimming** equal ports of `trimPolyG`/`trimPolyX` on 20,000
  constructed tails (clean and error-containing) for `--poly_g_min_len` 5, 10 and
  20 and `--poly_x_min_len` 10 and 15: 20,000/20,000 in every row.
- **Global trimming.** `-f`, `-t`, `-f`+`-t`, `-b` and `-f`+`-b` equal one-line
  references on 20,000 reads with no unexpected read kept or dropped.
- **`--phred64`.** The same reads survive as with the phred+33 encoding of the
  same data, the output qualities are converted to phred+33, and the Q30 counts
  agree exactly.
- **Base correction (`-c`).** Corrections happen exactly when one base is
  ≥ Q30 and its mate ≤ Q14 (`src/basecorrector.cpp:30-31`); Q30/Q14 corrects,
  Q29/Q14 and Q30/Q15 and Q40/Q20 do not, and the corrected mate takes the
  donor's base *and* quality, as documented.
- **UMI extraction.** `--umi_loc read1` with `--umi_len`, `--umi_skip` and
  `--umi_prefix`, and `--umi_loc index1` from the read name, all produce the
  documented name and the documented remaining sequence.
- **`--reads_to_process`** returns exactly N reads for N = 1, 999, 1,000, 1,001,
  4,999, 5,000 and the whole file for N above the file size.
- **`--dedup` and the duplication rate** (W4 above).
- **`--split` conservation** (W5 above).
- **fastp's own unit tests** (`./fastp test`) pass on master and on all three fix
  branches.

## Not audited here

The HTML report and its plots; gzip/BGZF reading and writing and the
`--compression` path; `--stdin`/`--stdout`, `--interleaved_in` and the MGI id
fix; `--failed_out`/`--unpaired1`/`--unpaired2` routing;
`--filter_by_index1/2`; the merging output format beyond overlap detection
(`OverlapAnalysis::merge`, `ReadPair::fastMerge`) and `--overlapped_out`;
long-read (`> 300 cycle`) handling and the down-sampled quality curves; the
overrepresented-sequence machinery beyond the reading-level note N7; the
`parallel.py` batch script; the Highway SIMD kernels beyond the project's own
`fastp_simd::testSimd` and their agreement with the ports used here; and the
`--adapter_fasta` multi-adapter path beyond reading `trimByMultiSequences`.
