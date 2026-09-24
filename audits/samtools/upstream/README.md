# SAMtools upstream filing kit

_Default branch: **`develop`** (PRs go against it; `master` carries releases).
Prepared 2026-09-08 against `samtools/samtools` `develop` @ `ce612d2` (built with
HTSlib `develop` @ `e503e04`). **Nothing filed, nothing pushed.** The fix is one commit,
`fc25542`, on the local branch `fix/stats-coverage-ring-buffer` of the audit clone, and
`git am`-able from `0001-stats-grow-the-coverage-ring-buffer-instead-of-wrapp.patch`
against `ce612d2` (`git apply --check` clean)._

_Update 2026-09-24: ST1 (+ST2) was merged as PR #2379 (rebased, `de749a6` on `develop`,
daviesrob: "Looks OK, thanks. I've confirmed that the results match those from the
original code when modified to start with a buffer that doesn't need to be resized.");
issue #2378 closed as completed. The second kit, ST3 (= notes N2 + N3), is below._

## ST3 (2026-09-24): N2 duplicate counts + N3 insert-size SD — comment on #696 + PR

**Prior report found.** The tracker search for N2 (2026-09-24, `search_issues` "stats reads
duplicated supplementary") returned **#696** "Should stats exclude supplementary alignments
when counting duplicates?" (2017-06-22, open, opened by pd3, a maintainer, no comments,
no linked change; read in full 2026-09-24 via the helper artifact "Mytochondria threads
samtools 696 1046"). It asks whether duplicate marking flags the supplementary record too,
notes that `stats` would then overestimate the duplicate rate, and proposes the exact
move this kit makes (the `IS_DUP` block into the `IS_ORIGINAL` block). So N2 is **not a
new issue**: it is a comment on #696 with the reproduction and the measured effect, and a
PR that says `Fixes #696`. N3 has no prior report (#1046 "insert size average difference",
closed 2019 for lack of data, and its linked commit 618d624 "Fix stats insert size bugs"
touch the mean and the `-m` bulk rule, not the SD loop); it rides as the second, one-line
commit of the same PR, offered to be dropped if the maintainers want it separate.

| file | what |
|---|---|
| `comment-st3-696-dup-supplementary.md` | the comment for #696: two-pair MCVE with output on four builds, the 25.0 % vs 20.0 % measurement, the PR announcement including the SD commit |
| `mcve_st3_stats_dup_supp_isize_sd.sh`, `mcve_outputs_st3.txt` | the two reproductions (duplicates 5 of 4 sequences; SD 81.6 for a population SD of 141.4) run on `develop`, 1.19.2, 1.10, 1.9 and the patched build |
| `0002-stats-count-duplicates-for-the-same-records-as-seque.patch` | commit `99c2244`: `IS_DUP` block moved inside `IS_ORIGINAL`, `test/stat/22_dup_supp.sam` + `22.stats.expected`, `test/test.pl` line, NEWS bullet |
| `0003-stats-include-the-isize-0-bin-in-the-insert-size-sta.patch` | commit `723af0e`: SD loop from `isize=0`, `test/stat/23_isize_zero.sam` + `23.stats.expected`, `test/test.pl` line, NEWS bullet |
| `pr-bodies.md` § PR 2 | PR title and body draft (`Fixes #696`, `Assisted-by:` line) |

Branch `fix/stats-dup-supplementary-isize-sd` on `cindykrafft/samtools` = `99c2244` +
`723af0e` on `develop` `de749a6`, author Cindy Krafft, `Assisted-by: Claude:claude-fable-5-1`
trailer, **no `Signed-off-by` yet** (to be added at the submitter's word, as for BC1).

Verification: `perl test/test.pl` on the branch 1011 passed / 0 failed / 32 expected
failures, `make test` PASS (HTSlib `develop` `bgzip` on PATH for the test script); with
`stats.c` reverted the two new tests fail (`22.stats.expected`: 10 / 860 for 8 / 800;
`23.stats.expected`: SD 60.1 for 130.5). Affected: `develop`, 1.19.2, 1.10, 1.9
(`mcve_outputs_st3.txt`); the code is unchanged since at least 1.5 (#696's line links).

Order: post the comment on #696 first, then open the PR against `develop` with the body
from `pr-bodies.md` rewritten in your own words, keeping `Fixes #696` and the
`Assisted-by:` line; sign off the two commits (`git rebase --signoff de749a6` on the
fetched branch, or ask me to add the lines) before opening it.

Filing tier (README step 5): **now** for ST1 — it changes a number that reaches papers
(`samtools stats` `COV` coverage distribution and the `-t`/`-g` "percentage of target
genome with coverage > N", 117.77 % on a simulated gene) under default settings, on the
current release and on every release the cohort names. ST2 travels with it in the same
patch (same function family, same test file convention). The six notes are **held**.

## What was read before preparing this (step 4 of the method)

- `CONTRIBUTING.md` (new in 1.24, PR #2335). Shaped the kit as follows:
  - *Complexity*: keep PRs small, one topic; issue first for large work — ST1+ST2 is
    one 39-line change in one function family plus tests, so an issue with the
    reproduction and a single PR.
  - *Completeness*: documentation and test cases for all PRs; no huge test files, no
    remote data — the two new tests are 4- and 13-line SAM files compared on their
    `COV` rows (the same `| grep -e"^RFS"` pattern the project's ref-stats tests use).
  - *Signing*: Developer Certificate of Origin; a real-name `Signed-off-by:` on every
    commit; **"AI agents are not permitted to add Signed-off-by tags"** — the patch
    carries no sign-off. The submitter must review every line and `git commit --amend
    -s`.
  - *AI policy*: `Assisted-by: AGENT_NAME:MODEL_VERSION` line on each commit and at the
    end of the PR description; "commit messages and PR descriptions should be written
    by a human". The patch's commit message and `pr-bodies.md` carry
    `Assisted-by: Claude:claude-fable-5-1` and are drafts to be rewritten by the
    submitter in their own words before filing.
- `.github/ISSUE_TEMPLATE/Bug_report.md`: three free-text headings (version of
  samtools/HTSlib; OS, architecture, compiler; steps, command, output).
  `issue-st1-stats-cov-ring-buffer.md` follows them in order. `config.yml` and
  `Feature_request.md` exist; no PR template, no discussions link, no pinned policy
  issue.
- `NEWS.md`: entries as `* FIX.`/`* CHANGE.`/`* NEW.` bullets under the unreleased
  `Release a.b` heading, usually with `(PR #NNNN, fixes #NNNN)`; the patch adds a
  "Bug fixes:" bullet there (the PR/issue numbers to be added once they exist).
- `INSTALL` and `test/test.pl`: tests are `test_cmd` calls comparing a command's
  output with a `.expected` file (`exp_fix` for Windows line endings); `make test`
  runs `test/test.pl` plus the C unit tests and the CRAM regressions. No linter or
  formatter configuration in the tree (no `.clang-format`, no lint step in
  `.github/workflows/*`); the C follows the file's existing style.
- `doc/samtools-stats.1` ("COV reports a distribution of the alignment depth per
  covered reference site", `-t`, `-g`, `-p`) as the statement of intended behaviour.
- Issue tracker searched 2026-09-08 (four `search_issues` queries, spaced to the
  shared rate limit): no prior report of ST1 or ST2. Nearest: #1003 (open, 2019:
  "stats GC-depth calculation badly off for long reads" — the other `stats` buffer,
  worth cross-referencing in the issue), #640 and #969 (closed: `-t` coverage
  restriction, `-d`/`-p` coverage output), #875 (closed: `-t` segfault), #2201 (open:
  stats for long inserts). For the notes: N1 nearest #1036/#986 (`mpileup` overlap
  detection, open); N5 nearest #2234 (closed, `coverage --rf 256`).
- `site/audits.json` in this repository has no `samtools` entry and no fork of
  `samtools/samtools` under `cindykrafft` is recorded; GitHub's repository API is not
  reachable from this session, so the `upstream-declines-ai-contributions` topic could
  not be checked directly. The `CONTRIBUTING.md` AI policy is an *acceptance with
  conditions*, not a refusal.
- Matthew Rocklin's "Craft Minimal Bug Reports" as summarised in the project brief:
  the issue's example is two SAM records written by the script itself, ends in the
  expected-vs-got `COV` rows, and says what shrinking revealed (the exact wrap
  condition and the `1000N` control).

## Contents

| file | what |
|---|---|
| `issue-st1-stats-cov-ring-buffer.md` | bug report in the template's three headings: two-read MCVE, cause, the gene simulation numbers, the reallocation defect, patch offer |
| `mcve_st1_stats_cov_spliced.sh`, `mcve_outputs.txt` | the reproduction embedded in the issue and its output on `develop`, 1.19.2, 1.9 and the patched build |
| `0001-stats-grow-the-coverage-ring-buffer-instead-of-wrapp.patch` | ST1+ST2 fix (`round_buffer_resize`), tests `test/stat/20_spliced.sam` + `21_mixed_lengths.sam` with `.expected` files, `test/test.pl` lines, NEWS entry |
| `pr-bodies.md` | PR title and body draft, with the sign-off / `Assisted-by:` instructions |

## Verification status of the patch

| tree | `make test` | the two new tests |
|---|---|---|
| unmodified `develop` @ `ce612d2` with the two new tests copied in | 1039 total: **1005 passed, 2 failed**, 32 expected failures | both fail (`stat/20.stats.expected`, `stat/21.stats.expected`) |
| `develop` + patch (`fc25542`) | 1039 total: **1007 passed, 0 failed**, 32 expected failures | both pass |

The audit harnesses rerun against the patched binary
(`../verify/st1_stats_cov_ringbuffer.patched.out`, `../verify/st2_stats_cov_realloc.patched.out`):
every case equals the Python truth (gene simulation 2,197 covered positions, `-g 0`
99.86 %; reallocation case 50 positions at depth 11; long-read case 2,190,000 depth
units). `../verify/heldup_stats_sn.py` (31 SN numbers × 4 filter modes) is unchanged
under the patch.

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| ST1 | 1.9, 1.10, 1.19.2, `develop` (`../verify/st1_stats_cov_ringbuffer.v*.out`, `mcve_outputs.txt`) | patched `fc25542` |
| ST2 | 1.9, 1.10, 1.19.2, `develop` (`../verify/st2_stats_cov_realloc.v*.out`) | patched `fc25542` |

## Order of operations

1. Open the issue from `issue-st1-stats-cov-ring-buffer.md` (paste a fresh run of
   `mcve_st1_stats_cov_spliced.sh`); mention #1003 as the related long-read `stats`
   report.
2. `git am` the patch onto a fresh `develop` in a fork, review every line, rewrite the
   commit message in your own words keeping the `Assisted-by:` line, `git commit
   --amend -s`, add the issue number to the NEWS bullet, push, open the PR against
   `develop` with the body from `pr-bodies.md` rewritten likewise.
3. Record issue and PR numbers, and every maintainer response, in `../README.md` and
   the top-level status table. The six notes stay held until the maintainers respond.
