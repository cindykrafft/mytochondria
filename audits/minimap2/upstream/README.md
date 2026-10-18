# minimap2 upstream filing kit

_Default branch: **`master`** (PRs go against it). Prepared 2026-10-18 against `lh3/minimap2`
`master` @ `3c28777` ("Release minimap2-2.31 (r1302)", 2026-05-19; `git ls-remote` confirms
nothing has been pushed since). **Nothing filed.** **Fork needed: lh3/minimap2.** No fork
exists under `cindykrafft`. The fix is a single commit (`bc409e9` in the audit scratch clone),
`git am`-able from the patch here against `3c28777`, to be pushed as branch
`fix/as-end-to-end-extension`._

Filing tier (TRIAGE): **now** for MM1 (AS:i above the score of the reported alignment under
the default `-x sr` preset, every version from 2.17 to 2.31, 7.0 % of records on simulated
Illumina pairs; two-line fix). Caveat: AS is rarely reported in a paper by itself. It reaches
papers through AS thresholds and AS-based assignment between references, and the grade rests
on that. **Held:** MM2 (MAPQ n_sub carry-over, 1–2 MAPQ units on 1.8 % of records in
near-identical repeats), MM3 (`dv:f` end test, ≤ 0.0008), notes N1 and N2. **Duplicate:** N3 is
lh3/minimap2#1307 (open, acknowledged by the maintainer). Two-filing cap: MM1 is the only
filing (issue + PR). Nothing else goes until it has a reply. After a positive reply, MM2 could
follow as an issue with the one-line patch offered (`fix/nsub` in the scratch clone), framed as
a question, because the MAPQ heuristics were tuned empirically with the current behaviour.

## What was read before preparing this

- **Contribution rules:** no `CONTRIBUTING.md`, no issue or PR template, no `.github/ISSUE_TEMPLATE`,
  and no AI-contribution policy anywhere in the tree (`README.md`, `FAQ.md`, `cookbook.md`,
  `NEWS.md`, `code_of_conduct.md`, `.github/` searched; `.github/` holds only
  `workflows/ci.yaml`). README "Getting help": "If you encounter bugs or have further questions
  or requests, you can raise an issue at the issue page. There is not a specific mailing list."
  `code_of_conduct.md` is Contributor Covenant 1.0.0 (maintainers may reject contributions
  that do not align with it; nothing about tooling).
- **CI** (`ci.yaml`): compile-only on gcc/clang x86_64, gcc aarch64 and clang macOS arm64. There
  is no test target in the `Makefile`. The equivalent checks (gcc and clang builds, the README
  example commands on `test/` diffed against master, and the audit harnesses) are in
  `test-runs.txt`.
- **Maintainer practice on the tracker** (2025–2026 threads read for duplicates): lh3 answers
  briefly and closes questions himself ("This is not exposed.", "Don't use -uf", "See README.").
  He acknowledged #1307 ("This is something I want to improve as well."). The only
  automated-pipeline report in 2026 (#1363, disclosed as such and "not execution-verified")
  got no reply and was closed by its author after 12 days. The MM1 issue therefore leads with
  a five-read reproduction and real output, and keeps the explanation short.
- **History:** `git log -S reach_end -- align.c`: the `reach_end` coordinates next to
  `dp_score += ez->max` date from 7345621 (r499, 2017-10-11, "end bonus working; DP region needs
  improve!"). The same lines sit at `align.c:700` and `:767` on the 2.17 tag, and the behaviour
  was executed identically on the 2.17 build. The fix touches only those two lines.
- **Duplicates:** `dupcheck-2026-10-18.md`. No prior report of MM1, MM2 or MM3. N3 = #1307.

## Contents

| file | what |
|---|---|
| `issue-mm1-as-overstated-end-extension.md` | bug report: five-read reproduction with output, cause (`align.c:792-797`, `884-889`), prevalence, fix |
| `0001-Score-extensions-that-reach-the-query-end-by-the-end.patch` | MM1 fix (`align.c`, two lines), commit `bc409e9` on `fix/as-end-to-end-extension` |
| `pr-bodies.md` | PR 1 title and body |
| `test-runs.txt` | gcc/clang builds, README examples master vs branch, harness results on the branch |
| `dupcheck-2026-10-18.md` | queries, candidates, verdicts, upstream head check |

## Verification status of the patch

| branch | commit | harness on the patched build | project checks |
|---|---|---|---|
| `fix/as-end-to-end-extension` | `bc409e9` | `../verify/s1_scores_tags.patched.out`: AS == port 180/180 in every block (was 132/180 in both sr blocks); everything else unchanged. `../verify/r1_as_prevalence.out`: 40,000/40,000 consistent (was 37,197), 0 other fields changed. `../verify/x1_as_issue_repro.patched.out`: all five reads AS:i:290 | `test-runs.txt`: gcc and clang build; README examples identical |

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| MM1 | 2.17, 2.24, 2.26, 2.31 (`master`) under `-x sr` | default long-read presets (end bonus −1); patched |
| MM2 | executed on 2.31 (instrumented + patched builds); line identical in 2.17 (`hit.c:117`), 2.24, 2.26 (`hit.c:133`) | patched (`fix/nsub`) |
| MM3 | 2.17, 2.24, 2.26, 2.31 | — |
| N3 (#1307) | 2.17, 2.24, 2.26, 2.31 | — |

## Order of operations

1. Fork `lh3/minimap2` (**fork needed**). Push `fix/as-end-to-end-extension` from the patch
   (`git am` on `3c28777`); tell the session the fork exists.
2. Open the MM1 issue from `issue-mm1-as-overstated-end-extension.md`, then the PR from
   `fix/as-end-to-end-extension` with the body in `pr-bodies.md` § PR 1 (issue number in the
   first line).
3. Wait for a maintainer reply. MM2 (issue with the one-line patch offered) only after that;
   MM3, N1, N2 stay held. N3: nothing, #1307 is open and acknowledged. A comment there could
   carry the measurement (a 2-bp dovetail already loses 0x2) only after reading the thread in
   full, and that one is optional.
4. Record issue and PR numbers and every maintainer response in `../README.md` and the
   top-level status table.
