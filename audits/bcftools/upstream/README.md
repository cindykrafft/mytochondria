# BCFtools upstream filing kit

_Default branch: **`develop`** (PRs go against it; `master` carries releases).
Prepared 2026-09-13 against `samtools/bcftools` `develop` @ `7abcc0d6` (built with
HTSlib `develop` @ `e503e04`). **Nothing filed.** The fork `cindykrafft/bcftools` was made on 2026-09-23 and the fix
pushed as branch `fix/mwu-biasz-int64` (commit 83b7888 on `develop` @ edf7fd9: the patch
rebased with one trivial conflict in `test/test.pl`, an adjacent `--progress` test line;
the submitter's authorship, the `Assisted-by:` trailer, and the submitter's `Signed-off-by:`,
added at her explicit instruction on 2026-09-23 since she could not do it from her phone; the
commit message is still the kit's draft). The same fix is `git am`-able from
`0001-mpileup-use-64-bit-accumulators-in-the-Mann-Whitney-.patch` against `7abcc0d6`
(`git apply --check` clean; the patch carries the test BAM as a `--binary` blob)._

Filing tier (README step 5): **now** for BC1 — it changes numbers that reach papers
(the `INFO/MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`, `MQSBZ`, `NMBZ` annotations that bcftools'
own filtering how-to recommends as filters) under default settings in multi-sample
runs and under a raised `-d` on deep data, on the current release and on every
release from 1.13 on. The six notes are **held**. BC1 is the only filing, well under
the two-per-repository cap.

## What was read before preparing this (step 4 of the method)

- `CONTRIBUTING.md` (identical in substance to samtools': "Complexity", "Completeness",
  "Signing your work", "AI Policy"). Shaped the kit as follows:
  - *Complexity*: small single-topic PRs against a recent `develop`; an issue first for
    large work — BC1 is an 11-line change in one function plus a test, so an issue with
    the reproduction and a single PR.
  - *Completeness*: documentation and test cases for all PRs; "Do not include huge test
    files. If it requires a lot of data for validation, consider auto-generating it (in
    a deterministic way)" — the regression test is a 4.9-kB BAM of 1,340 20-bp reads on
    a 300-bp reference (the smallest input that puts 1,300 reads in one MAPQ bin), in
    the tree's own `test/mpileup/<name>.bam` + `.fa` + `.1.out` convention wired through
    `test/test.pl`'s `test_mpileup`. The generator is `../verify/` (pysam) and the SAM
    equivalent is written by `awk` in the MCVE script, if the maintainers prefer a
    generated input.
  - *Signing*: Developer Certificate of Origin; a real-name `Signed-off-by:` on every
    commit; **"AI agents are not permitted to add Signed-off-by tags"** — the patch
    carries no sign-off. The submitter must review every line and `git commit --amend -s`.
  - *AI policy*: `Assisted-by: AGENT_NAME:MODEL_VERSION` line on each commit and at the
    end of the PR description; "commit messages and PR descriptions should be written
    by a human". The patch's commit message and `pr-bodies.md` carry
    `Assisted-by: Claude:claude-fable-5-1` and are drafts to be rewritten by the
    submitter in their own words before filing.
- `README.md` ("Support": bugs go to the GitHub issue tracker; security issues by
  e-mail). There is **no `.github/ISSUE_TEMPLATE/`** and no PR template in the
  bcftools tree (unlike samtools), so `issue-bc1-*.md` follows the samtools template's
  order informally: versions, environment, steps/command/output, expected vs got.
- `NEWS`: entries as `* bcftools <command>` headings with indented `- ` bullets under
  the unreleased `## Release a.b` heading, usually ending in `(#NNNN)`; the patch adds
  a `* bcftools mpileup` block there (the issue number to be added once it exists).
- `test/test.pl` and `Makefile`: `make test` builds `test/test-rbuf` and
  `test/test-regidx` and runs `test/test.pl` (`test_cmd` against `.out` files;
  `test_mpileup` runs each case on the `.bam` and, when present, `.sam`/`.cram` inputs,
  plain and through `-Ob | view`). No linter or formatter configuration in the tree
  (no `.clang-format`, no lint step in `.github/workflows/*`); the C follows the file's
  existing style.
- `doc/bcftools.txt` (`mpileup` "Output options" for the annotations; `merge -i`
  for N1; the FILTERING EXPRESSIONS section for the filter harness).
- Issue tracker searched 2026-09-13 (four `search_issues` phrasings, spaced to the
  shared rate limit): no prior report of BC1. Nearest: #2003 (closed, 2023-09, "Is
  this the kind of distribution expected for the BQBZ metrics?", 0 comments), #897
  (open, 2018, "Significant decrease of MQB when using -C during mpileup", 1 comment),
  #1058 (open, 2019, "mpilup read-pair overlap detection introduces strand-bias",
  4 comments), #2185 (open, 2024, confidence at low support, 3 comments). None is the
  same bug; the issue is drafted as a new issue and cites none of them.
- `site/audits.json` in this repository has no `bcftools` entry; a GitHub repository
  search for `bcftools user:cindykrafft` returns nothing, so there is no fork to carry
  the `upstream-declines-ai-contributions` topic. The `CONTRIBUTING.md` AI policy is an
  *acceptance with conditions*, not a refusal.
- Matthew Rocklin's "Craft Minimal Bug Reports" as summarised in the project brief:
  the issue's example is one reference and one SAM written by `awk` in the script,
  ends in expected-vs-got, and says what shrinking revealed (exactly one bin with ≥ 1291
  reads; alt count, annotation and file count irrelevant; the 1290 control).

## Contents

| file | what |
|---|---|
| `issue-bc1-mpileup-mwu-biasz-int-overflow.md` | bug report: cause, MCVE, expected vs got with the closed form, what shrinking showed, patch offer |
| `mcve_mpileup_mqbz_overflow.sh`, `mcve_outputs.txt` | the reproduction embedded in the issue and its output on unmodified `develop`, 1.24, 1.13 (1300 and 1290 reads) and the patched build |
| `0001-mpileup-use-64-bit-accumulators-in-the-Mann-Whitney-.patch` | BC1 fix (`calc_mwu_biasZ` accumulators to `int64_t`), test `test/mpileup/mwu-biasZ.1.{bam,bam.bai,fa,fa.fai,1.out}`, `test/test.pl` line, NEWS entry |
| `pr-bodies.md` | PR title and body draft, with the sign-off / `Assisted-by:` instructions |

## Verification status of the patch

| tree | `make test` | the new test (`.out` and `-Ob \| view` paths) |
|---|---|---|
| unmodified `develop` @ `7abcc0d6` | 2480 total: **2480 passed, 0 failed** | — |
| unmodified `develop` with the new test files copied in | 2482 total: **2480 passed, 2 failed** | both fail (`MQBZ=-7.88325` vs expected `-36.5924`) |
| `develop` + patch (branch `fix/mwu-biasz-int64`) | 2482 total: **2482 passed, 0 failed** | both pass |

The audit harness rerun against the patched binary
(`../verify/bc1_mpileup_mwu_biasZ_int_overflow.patched.out`): every case equals the
scipy truth (0 affected, 31 ok; e.g. 12,000 reads −109.7220 for −109.7224; 100
samples −55.0364). The other held-up harnesses are unaffected by the change (they do
not touch the Z-scores at counts below 1,291).

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| BC1 | 1.13, 1.24, `develop` (`../verify/bc1_mpileup_mwu_biasZ_int_overflow.v1.13.out`, `.v1.24.out`, `.out`; `mcve_outputs.txt`) | 1.9, 1.10.2 (no Z-score annotations; `.v1.9.out`, `.v1.10.2.out`); 1.11 and 1.12 by reading of their tags (`calc_mwu_biasZ` absent; not built); patched build |

## Order of operations

1. Open the issue from `issue-bc1-mpileup-mwu-biasz-int-overflow.md` (paste a fresh
   run of `mcve_mpileup_mqbz_overflow.sh`).
2. `git am` the patch onto a fresh `develop` in a fork, review every line, rewrite the
   commit message in your own words keeping the `Assisted-by:` line, `git commit
   --amend -s`, add the issue number to the NEWS bullet, push, open the PR against
   `develop` with the body from `pr-bodies.md` rewritten likewise.
3. Record issue and PR numbers, and every maintainer response, in `../README.md` and
   the top-level status table. The six notes stay held until the maintainers respond.
