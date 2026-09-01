# Upstream filing kit — MACS

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
