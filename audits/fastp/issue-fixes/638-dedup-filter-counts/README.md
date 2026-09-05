**Filed 2026-09-04 as PR #715** (issue #638; comment posted on the issue).

# fastp #638 / #528 — `--dedup` removals counted as "passed filter"

_Prepared 2026-09-03 against `OpenGene/fastp` `master` @ `dce5c40` (version
string 1.3.6), built with `make` against Ubuntu's libisal 2.31.0, libdeflate
1.19 and libhwy 1.0.7 as in [`../../verify/`](../../verify/). Nothing has been
filed, pushed or committed outside this directory; the fix branch
`fix/issue-638-dedup-filter-counts` exists only in the session's scratch clone._

## The issue

- **[#638](https://github.com/OpenGene/fastp/issues/638)** "Deduplication not
  reported in the html report" (2025-10-21, open, 0 comments). The reporter runs
  the same PE command with and without `--dedup`: the report's "reads passed
  filter" is identical in both runs (30,765,342 = 15,382,671 pairs), while the
  output files hold 15,382,671 pairs without `--dedup` and 13,396,876 with it —
  "which makes sense but doesn't agree with the report".
- **[#528](https://github.com/OpenGene/fastp/issues/528)** "Discrepency in
  filtering restults and reads after filtering" (2023-10-12, open, 3 comments —
  the comments could not be read from this session) reports the same thing from
  the JSON: `filtering_result.passed_filter_reads` 18,724,357 against
  `summary.after_filtering.total_reads` 10,933,431 in a `--dedup` run, "what
  happened to the 8 or so million reads?".

Both bodies are enough on their own; no open PR touches this
(`mcp__github__search_pull_requests`, "dedup duplicate passed_filter_reads
filtering result report": 0 hits).

## Diagnosis (line numbers on `dce5c40`)

The per-read decision to drop a duplicate is taken at
`src/seprocessor.cpp:213-218` (SE) and `src/peprocessor.cpp:397-402` (PE):
`dedupOut = true` when `--dedup` is on and `Duplicate::checkRead/checkPair` says
the read was seen before. That flag only gates the *output*
(`if(!dedupOut)` at `seprocessor.cpp:280` and `peprocessor.cpp:575`); the
filter category is recorded before it is consulted,
`config->addFilterResult(result, 1)` at `seprocessor.cpp:278` and
`config->addFilterResult(max(result1, result2), 2)` at `peprocessor.cpp:573`,
with `result == PASS_FILTER`. So every read that `--dedup` removes is still
counted under `mFilterReadStats[PASS_FILTER]`, which is what
`FilterResult::print()` (`filterresult.cpp:209`), `reportJson()`
(`filterresult.cpp:238`, key `passed_filter_reads`) and `reportHtml()`
(`filterresult.cpp:361`, row "reads passed filters") print. The
`summary.after_filtering` block is computed from `Stats::statRead` on the reads
actually written, so it is right, and the two blocks of the same JSON disagree
by exactly the number of removed duplicates. No category exists for those reads
at all.

A second consequence of the same omission: in `--merge` mode the merged branch
(`peprocessor.cpp:526-531`) never looks at `dedupOut` — the merged read is
written whenever it passes the filters — so `--merge --dedup` removes no
duplicates (the `--include_unmerged` branch at `peprocessor.cpp:547-556` does
check the flag).

## Reproduction (`repro.sh <fastp>`, synthetic data made in the script)

SE: 2,000 distinct 100-nt reads each written twice; PE: 1,000 distinct
overlapping pairs each written twice; all other filters off (`-A -G -Q -L`).

Before (`repro.before.out`, unmodified `dce5c40`):

```
== SE, 4000 reads (2000 distinct), --dedup
  stderr: reads passed filter: 4000
  filtering_result.passed_filter_reads = 4000
  filtering_result.duplicated_reads    = (absent)
  summary.after_filtering.total_reads  = 2000
  reads written to output      = 2000
== PE, 2000 pairs (1000 distinct), --dedup
  stderr: reads passed filter: 4000
  filtering_result.passed_filter_reads = 4000
  summary.after_filtering.total_reads  = 2000
  pairs written to output      = 1000
== PE, same pairs, --merge --dedup
  stderr: reads passed filter: 4000
  stderr: Read pairs merged: 2000
  merged reads written         = 2000  (1000 distinct pairs)
```

After (`repro.after.out`, fix branch):

```
== SE, 4000 reads (2000 distinct), --dedup
  stderr: reads passed filter: 2000
  stderr: reads failed due to duplication: 2000
  filtering_result.passed_filter_reads = 2000
  filtering_result.duplicated_reads    = 2000
  summary.after_filtering.total_reads  = 2000
  reads written to output      = 2000
== PE, 2000 pairs (1000 distinct), --dedup
  stderr: reads passed filter: 2006
  stderr: reads failed due to duplication: 1994
  filtering_result.passed_filter_reads = 2006
  filtering_result.duplicated_reads    = 1994
  summary.after_filtering.total_reads  = 2006
  pairs written to output      = 1003
== PE, same pairs, --merge --dedup
  stderr: reads passed filter: 2000
  stderr: reads failed due to duplication: 2000
  stderr: Read pairs merged: 1000
  merged reads written         = 1000  (1000 distinct pairs)
```

(The PE `--dedup` count moves between runs — 1,000 pairs in the "before" run,
1,003 here — because fastp's deduplication is a multi-threaded Bloom filter;
that is the known non-determinism of #562/#506 and not part of this fix. The
point is that after the fix the three counts agree with each other and with the
file in every run.)

## The fix (`0001-*.patch`, 28 insertions, 2 deletions in 4 source files + 1 script)

Following the way `FAIL_ADAPTER_DIMER` was added: a new filter category
`FAIL_DUPLICATE = 29` in `src/common.h` (tag `failed_duplicate`), and in each of
the four places a result is recorded — SE, PE merged branch, PE
`--include_unmerged` branch, PE plain — a read or pair that would otherwise pass
but is dropped by `--dedup` is recorded as `FAIL_DUPLICATE` before
`addFilterResult`. Reads that fail another filter keep that reason, as before.
`FilterResult` prints the new count as `reads failed due to duplication:` on
stderr, `"duplicated_reads"` in the JSON `filtering_result` and `reads
duplicated:` in the HTML summary table, each only when `--dedup` is on (like
`adapter_dimer_reads` is gated on adapter trimming), so reports of runs without
`--dedup` are byte-identical. Because the merged branch now records
`FAIL_DUPLICATE` and only writes on `PASS_FILTER`, `--merge --dedup` drops
duplicate merged pairs — the one behaviour change in output files.

## Tests

| what | before (master `dce5c40`) | after (fix branch) |
|---|---|---|
| `make -j8` | ok, no warnings | ok, no warnings |
| `./fastp test` (unit tests, from the repository root) | ALL PASSED | ALL PASSED |
| `scripts/test_issue_697_stdout_merge.sh` (existing) | PASS | PASS |
| `scripts/test_issue_638_dedup_filter_counts.sh` (new) | `FAIL: SE --dedup wrote 500 reads but reported passed_filter_reads=1000 duplicated_reads=-1 after_filtering.total_reads=500` | `PASS: issue #638 repro: SE wrote 500 reads, merge wrote 200 reads, counts agree with the reports` |

The new script follows `scripts/test_issue_697_stdout_merge.sh` exactly
(`python -` heredoc writes the FASTQ, one `./fastp` call per case, `PASS:`/
`FAIL:` line, exit status): an SE run asserts `passed_filter_reads ==
after_filtering.total_reads == reads written` and `duplicated_reads == 1000 −
written`, and checks the stderr line; an interleaved `--stdin --merge` run
asserts that no more than the 200 distinct pairs are written and that the two
counters sum to the 800 input reads. Both assertions are robust to the Bloom
filter's run-to-run variation.

**Linter/formatter:** fastp has none (no `.clang-format`, no lint job in
`.github/workflows/ci.yml`); the patch keeps the surrounding style (4-space
indent, `if(` without a space, the comment style of the adapter-dimer code).
**Changelog:** none in the repository (release notes live on the GitHub
releases page), so no entry is included. **PR template / CONTRIBUTING:** none.

## Other candidates considered

| issue | outcome |
|---|---|
| [#481](https://github.com/OpenGene/fastp/issues/481) dovetail trimming with 150/50-nt reads "capped at 50" | **Reproduced on master** (`exp/`: 150/50 reads, inserts 40–140 nt; inserts ≤ 45 trimmed, inserts ≥ 50 leave R1 at 150 with the adapter in it). Cause: `OverlapAnalysis::analyze` reverse loop `offset > -(len2-overlapRequire)` bounds the overlap to 31–50 nt for a 50-nt R2, and `trimByOverlapAnalysis` only trims when `offset < 0`, so a read pair where R2 is fully contained in R1 (offset ≥ 0, R1 extends past the insert) is never trimmed. Not chosen: the fix is a design extension of the overlap model (when to trust an offset ≥ 0 overlap as an insert end) and the maintainer's one comment could not be read. |
| [#664](https://github.com/OpenGene/fastp/issues/664) `--overlap_len_require 15` leaves an extra `A` on R1 | **Reproduced on master** with the reporter's pair (24 nt vs 23 nt). Not a bug: `trimByOverlapAnalysis` keeps `overlap_len + frontTrimmed2` bases of R1 on purpose (the R2 bases removed by `-F 1` are treated as insert bases, and the `T`/`A` pair is the A-tail), whereas at the default 30 the 23-nt overlap is never found and `trimBySequence` with the user's `AAGATCGG…` adapter removes the `A`. An explanation for the thread, not a fix. |
| [#499](https://github.com/OpenGene/fastp/issues/499) `--adapter_fasta` reported as "no adapter" | **Partly reproduced on master**: stderr now counts the trimmed reads (fixed since 0.23.2), but the JSON/HTML `adapter_cutting` section is still omitted because `Options::adapterCuttingEnabled()` (`options.cpp:41`) ignores `adapter.hasFasta`. A one-line fix; held as the runner-up because it only affects a report section for a less-used option. |
| [#711](https://github.com/OpenGene/fastp/issues/711) reads missed in concatenated BGZF input | Already fixed on master by PR #712 (`bgzf.h:148-152` skips embedded EOF blocks); plain multi-member gzip also reads 3,000/3,000 here. Issue left open upstream. |
| [#660](https://github.com/OpenGene/fastp/issues/660) poly-T tail not trimmed | Not reproduced: the reporter's read loses 139 bases with `--trim_poly_x --poly_x_min_len 10` on master. |
| [#694](https://github.com/OpenGene/fastp/issues/694) hang on desynchronised PE input | Not reproduced on master (5,000/4,995 reads, `-w 4`: exits in seconds); the report is against 0.23.2. |
| [#620](https://github.com/OpenGene/fastp/issues/620) empty read drops reads | The reporter's record has no sequence and no quality line (two-line record), i.e. invalid FASTQ; a proper empty record is handled on master. |
| [#693](https://github.com/OpenGene/fastp/issues/693) lowercase auto-detected adapter aborts | The abort path (`options.cpp:378`) is real, but the detector returned no adapter for lowercase synthetic reads here, so the trigger could not be reproduced. |
| [#344](https://github.com/OpenGene/fastp/issues/344) `-f/-F/-t/-T` together | Not reproduced on master (SE `-f 5 -t 5` → 50 nt; PE `-f 8 -F 8 -t 8 -T 8` → 134 nt both mates). |

Also noticed while reading `main.cpp:290-294`: the deprecated `--cut_by_quality3`
alias sets `enabledFront` instead of `enabledTail` and therefore does nothing
(verified: a read with a Q2 tail is left at 60 nt). No open issue names it; not
pursued because the option is deprecated.

## Caveats

- The comments on #528 (3) could not be read from this session; #638 has none.
- Naming of the new report fields (`duplicated_reads`, "reads failed due to
  duplication", "reads duplicated") is my choice by analogy with
  `adapter_dimer_reads`; the maintainers may prefer other wording. Downstream
  parsers (e.g. MultiQC's fastp module) read `passed_filter_reads`, whose meaning
  becomes "reads written", which is what both reporters expected.
- The `--merge --dedup` change alters output files (duplicate merged pairs are
  now dropped). It is stated separately in the PR body so the maintainers can
  ask for it to be split out.

## Files

| file | what |
|---|---|
| `repro.sh`, `repro.before.out`, `repro.after.out` | reproduction on synthetic data and its output on `dce5c40` and on the fix |
| `0001-fix-count-reads-dropped-by-dedup-as-duplicates-not-a.patch` | `git format-patch` of the one commit on `fix/issue-638-dedup-filter-counts` (fix + `scripts/test_issue_638_dedup_filter_counts.sh`) |
| `pr-body.md`, `comment.md` | PR title/body and the comment for the issue thread |
