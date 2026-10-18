# HMMER upstream filing kit

_Target: **`EddyRivasLab/hmmer`, branch `develop`** (PRs go against develop; `master` holds the
3.4 release). Prepared 2026-10-18 against `develop` @ `37f7148` (version string 3.5, July 2026;
unreleased — the current release on eddylab.org is 3.4) with Easel `develop` @ `69efc38`.
**Nothing filed. Fork needed: EddyRivasLab/hmmer.** The fix is one branch,
`fix/null2-bytrace`, with two commits (`80aadea` HM1, `787c2be` HM2), `git am`-able from
`0001-…patch` and `0002-…patch` on `37f7148`._

Filing tier (README step 5; `audits/TRIAGE.md`): **now** for HM1 + HM2, filed together as one
issue and one PR. They change the bit scores, `bias` columns and E-values that hmmsearch, hmmscan,
phmmer and jackhmmer print for multidomain hits, under default options. The code dates from
2008 (3.0); it was executed on 3.1b2, 3.3.2, 3.4 and develop. **Held:** HM3 (nhmmscan `-Z` ignored), HM4 (domain inclusion not nested in
reporting), HM5 (single-value GA in a protein alignment), N1 (`acc` documentation).

## What was read before preparing this

- **Contribution rules.** The tree has no `CONTRIBUTING`, no `CODE_OF_CONDUCT`, no issue or PR
  template and no `.github/` directory. `README.md` ("to clone a copy…" and "to report a
  problem"): "If you want to send us a pull request on GitHub, please base your changes on our
  **develop** branches", and report problems on the GitHub issue tracker. The user guide
  (`introduction.tex`, "How to report a bug") asks for a small reproducible test case. The wiki's
  Git-workflow page describes feature branches off `develop`. `.travis.yml` (clone Easel develop,
  `make`, `make dev`, `make check`) is the only CI config, and Travis no longer runs on this
  repository, so `make check` was run locally (`test-runs.txt`).
- **AI policy.** There is no written policy. Two signals: the maintainer's commit a37e75b fixing
  #348 begins "This AI-submitted report is verbose but correct", and he fixed the bug himself. #350
  (an automated "variant analysis" report) was fixed within two days with a thank-you. Outside PRs
  are merged (althonos #344, #307, #273; nawrockie #312, #309). So: a short report, with the
  reproduction up front and an "AI generation" line, not a long structured one.
- **Threads read in full** (WebFetch of the public pages, 2026-10-18): #348 (no comments), #350
  (one maintainer comment), #340 (one maintainer comment: `--incdomE` uses the conditional E-value,
  as intended), #12 (migrated HMMER2 record). Nothing in them bears on HM1/HM2.
- **Duplicate check:** `dupcheck-2026-10-18.md`. No prior report of HM1–HM5 or N1, and no branch
  holds a fix.
- `site/audits.json` has no HMMER entry and no fork of `EddyRivasLab/hmmer` under `cindykrafft`, so
  the `upstream-declines-ai-contributions` topic cannot apply yet.

## Contents

| file | what |
|---|---|
| `issue-hm1-null2-bytrace-inserts.md` | the bug report for HM1 + HM2: the two lines, SSE vs generic null2 on emitted traces, the replayed `n2sc`, EPHA8_HUMAN before/after, Swiss-Prot counts |
| `0001-Count-insert-state-residues-as-inserts-in-p7_Null2_B.patch` | HM1: `src/impl_sse/null2.c`, `src/impl_neon/null2.c`, `src/impl_vmx/null2.c` (one line each) plus `utest_null2_trace()` in the SSE test driver |
| `0002-Give-a-sampled-domain-s-first-residue-its-null2-rati.patch` | HM2: `src/p7_domaindef.c`, `<=` → `<` |
| `pr-bodies.md` | PR title and body |
| `test-runs.txt` | `make check` on develop and on the branch; the regression check; the harnesses on the patched build |
| `dupcheck-2026-10-18.md` | queries, candidates, verdicts |

## Verification status of the patches

| branch | commits | harness on the patched build | project tests |
|---|---|---|---|
| `fix/null2-bytrace` | `80aadea`, `787c2be` | `../verify/n2_null2_bytrace.patched.out`: SSE == generic null2 on every domain with insert states (fn3 0/469, Pkinase 0/784 differ); library `n2sc` == the documented `sqfrom..sqto` rule at 2356/2356 and 7825/7825 residues. `../verify/x1_null2_effect.out`: the size of the change. `e1`, `t1`, `h1` `.patched.out`: unchanged passes | Easel 102/102, HMMER 307/307 (`test-runs.txt`); the new unit test fails with the HM1 line reverted |

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| HM1, HM2 | 3.1b2, 3.3.2, 3.4, develop | patched |
| HM3 | 3.3.2, 3.4, develop (3.1b2 too: `z1_scan_Z.v3.1b2.out`) | — |
| HM4 | 3.1b2, 3.3.2, 3.4, develop | — |
| HM5 | 3.3.2, 3.4, develop write `GA 24.50 -99999.00`; 3.1b2 drops the GA line and `--cut_ga` then runs without any threshold | — |
| N1 | 3.1b2, 3.3.2, 3.4, develop | — |

## Order of operations (two-filing cap)

1. Fork `EddyRivasLab/hmmer` and tell the session, which pushes `fix/null2-bytrace` (based on
   `develop`).
2. Open the issue from `issue-hm1-null2-bytrace-inserts.md`. Then open the PR from
   `fix/null2-bytrace` **against `develop`**, with the body from `pr-bodies.md` § PR 1 and the issue
   number in its first line. That is filing 1 of 2. No second filing is planned; the held items
   wait for a reply.
3. After a maintainer reply, the held items can follow one at a time, in this order: HM4 (report
   only; the code comment and the man page both say inclusion is nested), HM3 (report, or a
   one-line PR that uses `pli->Z` when `-Z` is set), N1 (documentation), HM5.
4. Record issue/PR numbers and every maintainer response in `../README.md` and the top-level
   status table.
