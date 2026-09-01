# Kilosort upstream filing kit

Everything needed to file the Kilosort audit findings against
`MouseLand/Kilosort`. Recommended order:

## 1. KL1 — swarmsplitter refractoriness gate (PR only; issue already exists)

The bug is already reported as open issue
[#1042](https://github.com/MouseLand/Kilosort/issues/1042) (Aug 21 2026, no
maintainer response, no PR). Do **not** open a duplicate issue — open the fix
PR directly, with "Fixes #1042" (already in the PR body).

- Branch/patch: `0001-Fix-disabled-refractoriness-gate-in-swarmsplitter.ch.patch`
- PR body: `pr-kl1-swarmsplitter-gate.md`
- Live branch on the fork: `cindykrafft/kilosort@fix/swarmsplitter-ccg-guard` (549ec32)
  — open the PR from
  https://github.com/MouseLand/Kilosort/compare/main...cindykrafft:Kilosort:fix/swarmsplitter-ccg-guard?expand=1

## 2. KL2 — ContamPct = 0 for tiny clusters (issue, then PR)

- Issue body: `issue-kl2-contampct.md`
- PR body: `pr-kl2-contampct.md` (insert the new issue number)
- Branch/patch: `0001-Report-unevaluable-clusters-as-fully-contaminated-no.patch`
- Live branch on the fork: `cindykrafft/kilosort@fix/refract-contam-default` (d536ee6)
  — open the PR from
  https://github.com/MouseLand/Kilosort/compare/main...cindykrafft:Kilosort:fix/refract-contam-default?expand=1

## 3. KM3 — KS2/2.5/3 whitening covariance off-by-one (issue)

- Issue body: `issue-km3-nskipcov.md`
- One-line fix suggested inline; the MATLAB branches accepted the 2024
  issue-#594 fixes, so a branch fix is plausible if maintainers want it.

## 4. KM2 — KS2.5/3 identity whitening_mat export (documentation issue)

- Issue body: `issue-km2-whitening-export.md`
- Framed as a documentation/erratum request (branches are frozen; the point
  is to warn downstream consumers of existing outputs).

## Verification behind these filings

See `../verify/` — all three scripts run headless on CPU against shipped
kilosort 4.1.7 (KL1, KL2) or pure numpy (KM3). Both patches were re-validated
on their branches: the KL1 demo flips from `(False, False)`/split-allowed to
`(True, True)`/veto, with empty-input crash gone; the KL2 demo flips the
junk cluster from ContamPct 0.0 to 100.0 with the real unit unchanged at
93.9.

## Footers

GitHub issue bodies should end with the attribution footer shown at the
bottom of each issue file. PR descriptions should end with the PR footer
used elsewhere in this project.
