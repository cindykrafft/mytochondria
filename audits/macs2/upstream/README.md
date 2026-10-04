# Upstream filing kit — MACS

_Update 2026-10-04: MC1 resolved. taoliu (maintainer) approved and merged PR #753 on 2026-10-03 05:22 UTC (merge commit 6dbd9a2, our ed436c1 unchanged) and closed #752 ("Thanks for reporting and submitting the PR #753 !", 05:24). Thread read in full: https://claude.ai/artifact/8bDqeoHHostZ2Y9wAf32mm. MC3 (issue + PR) and MC2 move to Do next._

_Update 2026-10-02 18:50: MC1 filed by the owner as #752 with PR #753 (14:40 UTC); fork CI on ed436c1 green (x64, macOS, non-x64, Sphinx). MC3 and MC2 wait for a reply on it._

_Update 2026-10-02: both fix branches rebased onto `main` c544319 (3.0.5; the touched files had not changed) and force-pushed to `cindykrafft/MACS` as `fix/keepdup-auto-control-threshold` (`ed436c1`) and `fix/poisson-lower-tail-init` (`41daed5`), authored as Cindy Krafft; the patches here are regenerated from them. Re-verified on a build of c544319: `verify/keepdup_demo.py` keeps 48,636 of 60,000 control reads on main and 59,706 with the MC1 change; `python -m pytest test` gives 117 passed, 4 skipped on both. The issue and PR texts now follow the bug template and CONTRIBUTING.md (rewritten 2026-09-24; no AI policy): `issue-mc1-keepdup.md`, `pr-bodies.md` (PR 1 = MC1, PR 2 = MC3); the old `pr-mc1-keepdup.md` / `pr-mc3-poisson-init.md` are folded into it. Tracker searched again (two phrasings): nearest #163 (2016, "Error with --keep-dup", a different error), #14, #268; no prior report. Filing order now: MC1 issue + PR first (in the console's Do next); MC3 and MC2 after a reply on MC1._

Ready-to-file material for the MACS audit findings (`../README.md`, review in
`../component-reviews/callpeak-core.md`). MACS lives at
`macs3-project/MACS` on GitHub with issues and PRs open.

| File | Target | What it is |
|---|---|---|
| `issue-mc1-keepdup.md` | GitHub issue | companion issue: --keep-dup auto filters control with the treatment's threshold |
| `pr-mc1-keepdup.md` | GitHub PR body | the fix (filter line + 4 log/header lines), validated before/after on 3.0.4 |
| `0001-callpeak-filter-the-control-*.patch` | git am | same fix as format-patch vs current main |
| `issue-mc2-pvalue-convention.md` | GitHub issue | documentation request: P(X > t) convention, with exact tables |
| `issue-mc3-poisson-init.md` | GitHub issue | companion issue: dropped k=0 term / 2.x uninitialized variable |
| `pr-mc3-poisson-init.md` | GitHub PR body | one-line restore of the MACS 1.4 initialization |
| `0001-Prob-restore-the-k-0-term-*.patch` | git am | same fix as format-patch vs current main |

## Filing order

1. File `issue-mc1-keepdup.md`; note its number N1.
2. File `issue-mc2-pvalue-convention.md` (no PR; docs offer inside).
3. File `issue-mc3-poisson-init.md`; note its number N3.
4. The fix branches are pushed to the fork (`cindykrafft/macs`), one commit
   each on current main. Open each PR from its compare page with the pr-*.md
   body, replacing `#NNN` with N1/N3:
   - https://github.com/macs3-project/MACS/compare/main...cindykrafft:macs:fix/keepdup-auto-control-threshold
   - https://github.com/macs3-project/MACS/compare/main...cindykrafft:macs:fix/poisson-lower-tail-init

The filing console (artifact) has copy buttons and pre-filled links for all
of these. Note: the fix branches were authored against MACS main, which
requires Python ≥ 3.12 to build; validation was therefore performed by
applying the identical change to an installed MACS3 3.0.4 (the line is
unchanged between 3.0.4 and main) — before/after numbers in the PR body.
