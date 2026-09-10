# BCFtools upstream filing kit

_Default branch: **`develop`** (PRs go against it; `master` carries releases).
Prepared 2026-09-10 against `samtools/bcftools` `develop` @ `7abcc0d` (built with HTSlib
`develop` @ `e503e04`). **Nothing filed, nothing pushed.** The fix is one commit,
`22e3099f`, on the local branch `fix/mwu-bias-int-overflow` of the audit clone, and
`git am`-able from
`0001-mpileup-compute-the-Mann-Whitney-bias-Z-scores-in-64.patch` against `7abcc0d`
(`git apply --check` clean)._

Filing tier: **now** for BF1 — a wrong number under default settings on the current
release, in an annotation that filtering recipes act on. It is the **only** item to file;
the two notes (N1, N2) are **held**. Filing cap is two unanswered filings per repository
and this uses one issue + one PR on the same finding.

## What was read before preparing this

- **`CONTRIBUTING.md`** (in the tree at `7abcc0d`; the same document as
  `samtools/samtools`', credited to the kernel's coding-assistants policy). It shaped the
  kit as follows:
  - *Complexity*: keep each PR small and single-topic; open an issue first for anything
    large. BF1 is a five-line type change in one function plus a unit test, so: one issue
    with the reproduction, one PR.
  - *Completeness*: documentation where relevant and **test cases for all PRs**; "do not
    include huge test files … consider auto-generating it (in a deterministic way)"; "do
    not attempt to access remote sources during testing". A SAM file with 1,291 reads at
    one position would be ~150 kB, so the regression test is instead a C unit test
    (`test/test-mwu.c`) in the existing `test/test-rbuf` / `test/test-regidx` idiom,
    which builds the histograms in memory. It needs no data files and no network.
  - *Signing*: Developer Certificate of Origin, real-name `Signed-off-by:` on every
    commit, no GitHub-alias or anonymous contributions.
  - *AI policy*: **"AI agents are not permitted to add Signed-off-by tags"** — the patch
    carries **no sign-off**. `Assisted-by: AGENT_NAME:MODEL_VERSION` on each commit and
    at the end of the PR description — the patch and `pr-bodies.md` carry
    `Assisted-by: Claude:claude-opus-5`. "Commit messages and PR descriptions should be
    written by a human" — the commit message and the PR body here are **drafts for the
    submitter to rewrite in their own words** before filing, then `git commit --amend -s`.
  - This is acceptance *with conditions*, not a refusal, so a kit is appropriate.
- **`.github/`**: contains `workflows/` only (`linux-build.yml`, `macos-build.yml`,
  `windows-build.yml`, `container-build.yml`, `vm-build.yml`). **There is no issue
  template and no PR template.** `issue-bf1-mwu-bias-int-overflow.md` therefore follows
  the order of the sibling project's `Bug_report.md` (versions → environment → steps,
  command and output), which is what maintainers of both repositories are used to reading.
- **`NEWS`**: entries are indented bullets under a `* bcftools <command>` heading inside
  the unreleased `## Release a.b` section, usually ending `(#NNNN)`. The patch adds a
  `* bcftools mpileup` section with one bullet and an `(#NNNN)` placeholder.
- **`Makefile`** and `test/`: `make test` runs `./test/test-rbuf`, `./test/test-regidx`
  and then `REF_PATH=: ./test/test.pl` (2,480 tests). `TEST_PROGRAMS` at `Makefile:83`
  lists the C unit tests; the patch adds `test/test-mwu` there, a build rule next to the
  `test-regidx` rule, and one line to each of `check-no-plugins` and `check-plugins`.
- **No linter or formatter configuration** in the tree — no `.clang-format`, no
  `.editorconfig`, no lint step in `.github/workflows/*`. The patch follows the
  surrounding style of `bam2bcf.c` (4-space indent, brace placement as in the function).
- **`doc/bcftools.txt`** for `mpileup`'s annotation list (`MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`,
  `MQSBZ`, `NMBZ`) and for `norm --multi-overlaps`, as the statement of intended
  behaviour.
- **Matthew Rocklin, "Craft Minimal Bug Reports"**: the issue's example is a `sh`
  script that writes its own reference and SAM with `awk`, has no line that is not
  needed, states expected and got, and says what shrinking revealed (the exact p = 1291
  boundary and the second-bin control).
- **`site/audits.json`** in this repository has no `bcftools` entry and no fork of
  `samtools/bcftools` under `cindykrafft` is recorded, so the
  `upstream-declines-ai-contributions` topic could not be checked directly (GitHub's
  repository API is not reachable from this session). `CONTRIBUTING.md`'s AI policy is
  acceptance with conditions.

## Prior art on the tracker

Searched 2026-09-10 with `mcp__github__search_issues`, three phrasings
("mpileup MQBZ BQBZ RPBZ bias test integer overflow wrong Z score high depth";
"MQBZ RPBZ values wrong or suspiciously small when many samples pooled deep coverage
bias annotation"; "Mann-Whitney tie correction calc_mwu_biasZ int overflow bam2bcf").
**No prior report of BF1.** Nearest, none of them the same bug:

| # | state | title | comments |
|---|---|---|---|
| 897 | open | "Significant decrease of MQB when using -C during mpileup" | 1 |
| 962 | closed | "Documentation for Mann-Whitney U tests from mpileup" | 1 |
| 1930 | open | "bcftools v1.17 no longer finds known variants from v1.8" | 14 |
| 1767 | closed | "output BCFtools mpileup gives abnormal values" | 2 |
| 2185 | open | "bcftools mpileup + call seemingly confident in allele only present in a few reads?" | 3 |

None is close enough to comment on rather than open a new issue, so
`issue-bf1-mwu-bias-int-overflow.md` is written as a **new issue**. (Comment bodies
cannot be read from this environment, only issue bodies, so #897 and #1930 were judged on
title and body alone; if the lead reads #1930's 14 comments and finds the MQBZ change
already discussed there, the issue text should be re-aimed as a comment.)

## Contents

| file | what |
|---|---|
| `issue-bf1-mwu-bias-int-overflow.md` | the bug report: versions, environment, the two-pileup MCVE, cause, boundary, direction, filter impact, patch offer |
| `mcve_bf1_mqbz_overflow.sh`, `mcve_outputs.txt` | the reproduction embedded in the issue, and its output on 1.9, 1.10.2, 1.13, 1.24, unpatched `develop` and patched `develop` |
| `0001-mpileup-compute-the-Mann-Whitney-bias-Z-scores-in-64.patch` | the fix (`bam2bcf.c`), `test/test-mwu.c`, the `Makefile` wiring and the `NEWS` bullet |
| `pr-bodies.md` | the PR title and body draft, with the sign-off / `Assisted-by:` instructions |

## Verification status of the patch

| tree | `make test` | `test/test-mwu` |
|---|---|---|
| unmodified `develop` @ `7abcc0d` | 2480 total: **2480 passed, 0 failed** | (test not present) |
| `7abcc0d` with `test/test-mwu.c` and the `Makefile` wiring but **not** the `bam2bcf.c` change | run stops at `test-mwu` | **fails 2 of 4 checks**: `p=1291` expected −36.007720, got −7.706832; `30 samples x 100x` expected −31.076996, got −6.878492 |
| `develop` + the full patch (`22e3099f`) | 2480 total: **2480 passed, 0 failed** | **all tests passed** |

`git apply --check 0001-*.patch` is clean against `7abcc0d`.

The audit harnesses rerun against the patched binary
(`../verify/bf1_mwu_tie_overflow.patched.out`,
`../verify/bf1b_mwu_unit_surface.patched.out`): every case now equals the truth — the
1,500-read pileup gives −23.9783 (was −5.75778), the 30-file pileup −31.0770 (was
−6.87849), and across the 431-pileup sweep and the 160-pileup filter sweep **0 cases are
wrong and 0 verdicts flip**.

## Version scope (executed)

| version | BF1 |
|---|---|
| 1.9 (30 papers in the cohort) | **unaffected — no `calc_mwu_biasZ`, no `*BZ` tags** |
| 1.10.2 (10 papers) | **unaffected — same** |
| 1.13 (6 papers) | **affected** |
| 1.24 (latest release) | **affected** |
| `develop` `7abcc0d` | **affected** |
| `develop` + `22e3099f` | fixed |

From `mcve_outputs.txt` and `../verify/bf1_mwu_tie_overflow.v*.out` only. 1.11 and 1.12
were not built; they contain the same function by inspection but that is not an executed
claim, so nothing here asserts it.

## Order of operations

1. Open the issue from `issue-bf1-mwu-bias-int-overflow.md`, pasting a fresh run of
   `mcve_bf1_mqbz_overflow.sh`. Mention #962 as the existing documentation thread for
   these tags.
2. `git am` the patch onto a fresh `develop` in a fork, review every line, rewrite the
   commit message in your own words keeping the `Assisted-by:` line, `git commit
   --amend -s`, put the issue number in the `NEWS` bullet, push, and open the PR against
   `develop` with the body from `pr-bodies.md` rewritten likewise.
3. Record the issue and PR numbers, and every maintainer response, in `../README.md` and
   the top-level status table. N1 and N2 stay held until the maintainers respond.
