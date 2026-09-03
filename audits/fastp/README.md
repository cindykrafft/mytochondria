# fastp audit against 117 published papers (2021–2026)

_Round-2 audit, generated 2026-09-03 against `OpenGene/fastp`
`master` @ `dce5c40` (2026-09-01, version string 1.3.6). Focus: the code paths
that decide which bases and which reads survive — the sliding-window quality
cutters, global trimming, the quality/length/complexity filters, adapter
auto-detection and adapter trimming, poly-G/poly-X trimming, overlap analysis,
base correction, deduplication, UMI handling, and the numbers fastp reports in
its JSON — verified by executing the built binary._

## What this is

The six-journal survey found **117 papers** in PNAS (65), *Nature* (44) and
*Cell* (8), 2021–2026, that used fastp, almost always as the first step of a
sequencing pipeline (77 of them under "read trimming", 23 also under
"alignment/mapping", 17 under "quality control"). Its trimming and filtering core
was read in full on `master` and every suspicion was run through the built
binary — `master`, plus the v1.3.6 (latest release), v1.0.0, v0.26.0, v0.23.4,
v0.23.2, v0.22.0, v0.20.1 and v0.20.0 release tags, all compiled from source —
against independent Python ports of the documented and of the coded rules on
10^4–10^5 synthetic reads with known truth.

## Findings (details and line citations in [`component-reviews/trimming-and-filtering-core.md`](component-reviews/trimming-and-filtering-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **FP1** | **CONFIRMED on `master` and on every release built (0.20.0 → 1.3.6)** | `--cut_front`/`--cut_tail` combined with `--trim_front1`/`--trim_tail1` discard `cut_window_size − 1` extra bases from every read, even when no window fails: a 60 nt read whose every base is Q40 comes out 52 nt with `-f 5 --cut_front` (55 expected), 46 nt with `-W 10`, 44 nt with `--cut_front --cut_tail -f 5 -t 5`. The guard that suppresses the "drop the failing window" advance is written against the start of the untrimmed read (`if(s > 0)`, `if(t < l-1)`) instead of the trimmed start. On 20,000 random reads the shipped binary equals an as-coded port 20,000/20,000 and differs from the corrected rule on 11,509; with the default filters that is 1,880 reads and 9.8 % of the surviving bases. `--cut_right` is unaffected. **Already reported upstream as [#474](https://github.com/OpenGene/fastp/issues/474) (2023, open).** |
| **FP2** | **CONFIRMED on `master`, 1.3.6, 1.0.0, 0.26.0**; 0.23.4 and older not affected (they never produce such a candidate) | `main.cpp` truncates a long auto-detected adapter with `adapt.resize(0, 60)`, which *empties* the string instead of cutting it to 60 characters, so fastp prints the adapter it just found, then says "No adapter detected", trims nothing, and drops the `adapter_cutting` section from the JSON. Reachable since v0.26.0 added the built-in-table lookup: 139 of the 234 built-in adapters are longer than 60 nt and 85 of them have no shorter built-in prefix to fall back on — the 48 TruSeq Small RNA RPI primers and the RNA PCR Primer index series. Executed: 0 of 20,000 reads trimmed for two of them, 20,000/20,000 with the same sequence passed as `--adapter_sequence`; paired-end with `--detect_adapter_for_pe` trims 24,735 of 40,000 instead of 40,000. |
| **FP3** | **CONFIRMED on `master`, 1.3.6, 1.0.0, 0.26.0**; older releases have no such code | The one-insertion and one-deletion adapter loops added in v0.26.0 pass `rdata` (the read start) instead of `rdata + pos`, so they test only whether the read *begins* with the adapter: an adapter occurring at the 3' end with one indel is never trimmed (0 of 200 reads, against 200/200 for the same reads without the indel). The shipped binary equals a port that ignores the offset on 5,000/5,000 random reads; with the offset applied, 993/993 insertions and 967/967 deletions are trimmed and no adapter-free read is touched. **Already reported as a symptom in [#518](https://github.com/OpenGene/fastp/issues/518) (2023, open)**, which the v0.26.0 code was written for. |
| N1 | note, design + documentation, quantified | `--overlap_diff_limit`/`--overlap_diff_percent_limit` are enforced over the first 50 bases of the overlap only; 30 mismatches placed beyond position 50 of an 80 nt overlap still merge 200/200 pairs, 6 mismatches inside the first 50 reject all. Deliberate (the project's own unit test asserts it) but not documented; it governs PE adapter trimming, correction, merging and insert size. |
| N2 | note, off-by-one | `--overlap_len_require 30` accepts only overlaps of 31 nt or more (0/200 at 30 nt, 200/200 at 31). |
| N3 | note, threading | The insert-size histogram is filled by worker thread 0 only: 4,000 pairs give 4,000 counted at `-w 1`, 2,000 at `-w 2` and `-w 3`, 1,000 at `-w 4` and `-w 8`. The peak was correct in all cases. |
| N4 | note, off-by-one | `--poly_g_min_len 10` already trims a tail of 9 G (200/200), while poly-X uses the other convention. |
| N5 | note, undocumented side effect | `-m/--merge` silently switches on `--correction`: a PE run with `-m` alone reports `corrected_bases: 200`. |
| N6 | note | The adapter search needs 5 matching bases at the read end, not the `matchReq = 4` the code names (0/200 at 4 bases, 200/200 at 5). |
| N7 | note, by reading only | Both overrepresented-sequence scans iterate `i < len-step`, so a sequence at the very end of a read is never counted. |

Five own suspicions were withdrawn by verification (`--cut_right` leaking past
`--trim_tail1`; integer division in `--average_qual`; uninitialised reads in
`Matcher::matchWithOneInsertion`; bias in the duplication estimator; reads lost
by `--split`). They are recorded in the review.

**Held up under execution:** the quality/length/complexity filters and all six
`filtering_result` counters equal an independent port on 20,000 reads for 13
option sets, including every threshold boundary; `total_bases`, `q20_bases`,
`q30_bases`, the rates, `gc_content` and `read1_mean_length` equal direct
counting; the 1,024-entry `kmer_count` table matches exactly; poly-G and poly-X
trimming equal their ports on 20,000 constructed tails at three/two minimum
lengths; `-f`/`-t`/`-b`; `--phred64`; the base-correction quality rules
(Q30/Q14) and their boundaries; UMI extraction from read1 and from the index;
`--reads_to_process`; `--split` (no read lost or duplicated); and the
duplication rate, which reproduces a known 0 %, 20 % and 50 % duplication level
to four decimals in SE and PE mode, with `--dedup` keeping exactly the distinct
reads. `./fastp test` passes on master and on all three fix branches.

## How the papers use fastp (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| adapter trimming mentioned | 48 |
| "default parameters" | 37 |
| version stated | 24 |
| RNA-seq / metagenomics-16S / ATAC-ChIP-CUT&RUN / single-cell | 23 / 13 / 9 / 3 |
| `--qualified_quality_phred` (`-q`) | 20 (values 30 ×5, 15 ×3, 20 ×3) |
| `--length_required` (`-l`) | 13 (15 ×2, 36 ×2, then 30, 50, 75, 80, 100, 150) |
| FastQC/MultiQC also used / Cutadapt or Trim Galore / Trimmomatic | 13 / 11 / 7 |
| paired-end stated | 11 |
| `--dedup` or duplication rate | 11 |
| `--cut_right` / `--cut_tail` / `--cut_front` | 8 / 4 / 2 |
| `--correction` (`-c`) | 8 |
| `--trim_front1/2` / `--trim_tail1/2` | 7 / 2 |
| `--unqualified_percent_limit` (`-u`) / `--n_base_limit` (`-n`) / `--average_qual` (`-e`) | 7 / 5 / 3 |
| cut window size / mean quality stated | 6 (window 4 ×4, 10 ×1; mean quality 20 ×3, 15, 10) |
| adapter auto-detection / `--detect_adapter_for_pe` / explicit adapter | 6 / 4 / 2 |
| `--trim_poly_g` / `--trim_poly_x` | 3 / 3 |
| `--umi` / `--merge` / `--low_complexity_filter` / `--reads_to_process` | 2 / 2 / 1 / 1 |
| versions named | 0.20.0 ×10, 0.20.1 ×8, 0.23.2 ×7, 0.23.4 ×7, 0.21.0 ×6, 0.23.1 ×2, then 0.19.7, 0.12.4, 0.23.0, 0.24.2, 1.0.1 |

Exposure by finding: **FP1** needs `--cut_front`/`--cut_tail` together with
`--trim_front1`/`--trim_tail1`; no cached paper names both, and the one paper
that combines global trimming with a window cutter uses `--cut_right`, which is
not affected — so the exposure is unquantified rather than established.
**FP2** needs single-end auto-detection of one of the 85 long built-ins on
v0.26.0 or later; the cache names one paper on a 1.x version and no small-RNA
library, so no cohort paper is demonstrably exposed and the defect is a
present-release one. **FP3** needs `--adapter_sequence` (or the PE fallback) on
v0.26.0 or later. None of this can be settled from the cache.

**Profiling caveat.** As for the Seurat, Scanpy and Cutadapt audits, this session
had no route to Europe PMC, so `fastp_profile.py` ran in `--offline` mode over
the survey's stored evidence snippets; every record in `fastp_profiles.jsonl` is
`source: survey_cache` and every count above is a lower bound. Rerun without
`--offline` from a host with Europe PMC access to replace them with full-text
records. Two of the "versions named" values (`0.7.17`, `0.22.08`) are neighbouring
packages' versions caught by the ±25-character window around the word "fastp" in
a software table; the version families 0.20/0.23/0.21 match the survey's own
`top_versions` for fastp.

**Build caveat.** fastp's README asks for Google Highway ≥ 1.1.0; this session
built against Ubuntu's `libhwy-dev` 1.0.7 (plus `libisal-dev` 2.31.0 and
`libdeflate-dev` 1.19), which compiles through the compatibility shims in
`src/simd.cpp` and passes `./fastp test`, including `fastp_simd::testSimd`. The
SIMD kernels were additionally checked indirectly: every filter and statistic
they feed matches an independent port. The cohort's fifth most-cited version,
0.21.0, has **no tag in the repository** (the tags go v0.20.1 → v0.22.0), so
v0.22.0 was built in its place.

## Filing channel (read before anything is sent)

- fastp has **no `CONTRIBUTING.md`, no issue or PR templates, no changelog file
  and no linter configuration**; `.github/` holds only `workflows/ci.yml`, which
  builds the binary and runs `./fastp --version` and
  `./fastp -i testdata/R1.fq -o /dev/null`. The unit tests are `./fastp test`
  (`src/unittest.cpp`), which must be run from the repository root.
  `scripts/test_issue_697_stdout_merge.sh` is the project's convention for a
  regression script, and patch 0002 follows it.
- **FP1 and FP3 already have open issues** (#474 and #518), so their texts are
  drafted as comments on those issues rather than new issues; **FP2 has no prior
  report**. #474's single comment could not be read from this session (only issue
  *search* is available here) and must be read before posting.
- **The kit is in [`upstream/`](upstream/)**: three texts with reproductions run
  on `master`, v1.3.6 and v0.23.4, three MCVE scripts with captured output, three
  `git am`-able patches (fix + test; each new test fails on unmodified `master`),
  the PR bodies, and `patch_verification.txt` with every test run with and
  without each patch. **Nothing has been filed and nothing has been pushed.**

## Files

| file | what |
|---|---|
| `fastp_profile.py`, `fastp_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/trimming-and-filtering-core.md` | the review: FP1–FP3, N1–N7, five withdrawn suspicions, held-up list, not-audited list |
| `verify/fastp_ref.py` | the independent ports (`trimAndCut` in both variants, poly-G/poly-X, `passFilter`) and the fastq/runner helpers |
| `verify/fp1_cut_window_edge.py` (+ `.out`) | FP1: constant-quality matrix, 20,000 random reads vs both ports, cost under the default filters |
| `verify/fp2_known_adapter_over60.py` (+ `.out`) | FP2: census of the built-in table, seven adapters SE, PE with `-2`, adapter bases left in the reads |
| `verify/fp3_indel_adapter_offset.py` (+ `.out`) | FP3: indel groups, 5,000 random reads vs both ports, adapter position sweep |
| `verify/heldup_filters_and_stats.py` (+ `.out`) | held up: filters, `filtering_result`, JSON summary, k-mer table, global trims, `--phred64`, threshold boundaries |
| `verify/heldup_pipeline_and_dup.py` (+ `.out`) | held up: poly-G/poly-X, base correction, UMI, `--reads_to_process`, `--split`, duplication rate and `--dedup` |
| `verify/notes_overlap_polyg_threads.py` (+ `.out`) | N1–N6 |
| `verify/version_scope_cli.py` (+ `.master.out`, `.v1.3.6.out`, `.v1.0.0.out`, `.v0.26.0.out`, `.v0.23.4.out`, `.v0.23.2.out`, `.v0.22.0.out`, `.v0.20.1.out`, `.v0.20.0.out`) | the three findings through the command line only, on every version built |
| `upstream/` | filing kit: issue/comment texts, MCVEs and their outputs, patches 0001–0003, PR bodies, patch verification, documents read |

The harnesses take the path of a fastp binary as their first argument:
`git clone https://github.com/OpenGene/fastp && cd fastp && make -j` (needs
`libisal`, `libdeflate` and `libhwy`; `apt install libisal-dev libdeflate-dev
libhwy-dev nasm` is enough on Ubuntu 24.04), then
`python3 verify/fp1_cut_window_edge.py ./fastp`.

## Next steps

1. Read the comment on #474, then post the FP1 and FP3 texts on #474 and #518,
   open the FP2 issue, and open the three PRs from `upstream/pr-bodies.md`.
   Record numbers and maintainer responses here and in the top-level table.
2. Extend the review to the paths listed under "Not audited", above all the
   overrepresented-sequence machinery (N7 is a reading-level observation) and
   the merging output.
3. Full-text profiling rerun when Europe PMC is reachable, to settle how many of
   the 117 papers combine `-f`/`-t` with `-5`/`-3` (FP1) and how many run
   single-end small-RNA libraries (FP2).
