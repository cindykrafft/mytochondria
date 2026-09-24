# scDblFinder upstream filing kit

_Default branch: **`devel`** (PRs go against it). Prepared 2026-09-24 against `plger/scDblFinder`
`devel` @ `2d0e5e4` (1.27.6). **Nothing filed, nothing pushed.** The three fixes are single commits on
local branches of the audit clone, `git am`-able from the patches in this directory against `2d0e5e4`;
they need a fork of `plger/scDblFinder` under `cindykrafft` to be pushed._

Filing tier (README step 5): **now** for SD1 and SD2 — SD1 makes an advertised output
(`scDblFinder.mostLikelyOrigin`) wrong three times out of four whenever `clusters` are given, on every
release since 1.4.0, with a contained fix; SD2 empties `scDblFinder.stats` for the most common way of
passing clusters. **SD3 ready** as the third filing (a documented call that returns `NaN`) once SD1 or
SD2 has a reply, under the two-unanswered-filings cap (issue + PR pairs count as one). N1 and N2 are
**held**.

The maintainer (plger) answers within a day in every thread read, acknowledges bugs plainly (#57:
"you're absolutely right, this was wrong and embarrassing … corrected it now and will push back to the
BioC release") and closes threads himself; expect a fast response.

## What was read before preparing this (step 4 of the method)

- No `CONTRIBUTING`, no PR template, no code of conduct, no AI policy (checked by the helper session
  across the tree). `.github/ISSUE_TEMPLATE/bug_report.md`: **Describe the bug** / **MRE — Minimal
  example to reproduce the bug** ("try to reproduce the error with a single sample and/or without
  multithreading") / **Traceback** (for R errors) / **Session info**; "Before posting your issue,
  please ensure that it is reproducible with a recent Bioconductor and `scDblFinder` version." The
  three issue texts follow that layout. The README's "Important notes" asks xgboost ≥ 3.1 users to be
  on scDblFinder ≥ 1.24.7 / 1.25.4.
- On the "recent version" requirement: the affected code is byte-identical on `devel` (2d0e5e4) and
  on the 1.16.0 release where the numbers were produced (this session's R 4.3.3 cannot install
  `devel`, which needs `scrapper`); every MRE uses only `mockDoubletSCE`, `getArtificialDoublets`,
  `scDblFinder` and `doubletThresholding` and runs on any version. If the submitter has a current
  Bioconductor at hand, running the MRE there before filing and replacing the session info is the
  better course; the texts say which version produced the numbers.
- The Bioconductor package page and the vignette ("Doublet origins and enrichments":
  `scDblFinder.mostLikelyOrigin`, `scDblFinder.originAmbiguous`, `metadata(sce)$scDblFinder.stats`,
  `plotDoubletMap`) as the statement of intended behaviour for SD1/SD2; the `doubletThresholding`
  roxygen ("minimally containing a `score` column"; `dbr` method "strictly based on the expected doublet
  rate") for SD3.
- Issue tracker searched 2026-09-24 (five `search_issues` phrasings) and twelve threads read in full
  through a helper session (artifact "Mytochondria threads scDblFinder 52 57 45 123 135 144 30 67 82
  106 62 108"): **no prior report of SD1, SD2 or SD3.** #52 (2021, closed) is a user wanting to use
  `scDblFinder.stats` to find over-represented cell-type combinations — the use case SD1 and SD2
  break; the maintainer's reply concerns sample-of-origin, not the stats. #57 (2022, closed the next
  day) was a `cxds2` argument bug, fixed. #123 (2025) is a `doubletThresholding` error with tiny
  clusters, unreproduced. #135 (2025–2026) is a `dbr.per1k` vs `dbr` discrepancy the maintainer traced
  to xgboost compatibility (#132). #45, #82 are `knownDoublets` errors (one open); #30 reworked the
  "griffiths" method; #67, #106, #62, #108, #144 are usage questions. No open PRs.
- `site/audits.json` records no fork of `plger/scDblFinder` under `cindykrafft`.

## Contents

| file | what |
|---|---|
| `issue-sd1-artificial-doublet-origins.md` | bug report in the template's layout: 12-line MRE with `getArtificialDoublets`, the end-to-end numbers, the cause, the fix |
| `issue-sd2-factor-cluster-labels.md` | bug report: `mockDoubletSCE()` + `clusters="cluster"`, the empty stats table and the coded cluster column, the fix |
| `issue-sd3-dbr-threshold-nan.md` | ready: three-line MRE returning `NaN`, the fix |
| `0001-createDoublets-keep-the-input-pair-order-when-adjust.patch` | SD1 fix (`fix/artificial-doublet-order`, `getArtificialDoublets.R`) |
| `0002-scDblFinder-keep-factor-cluster-labels-as-labels-in-.patch` | SD2 fix (`fix/factor-cluster-labels`, `scDblFinder.R`) |
| `0003-doubletThresholding-do-not-correct-dbr-for-homotypic.patch` | SD3 fix (`fix/dbr-threshold-without-artificial`, `doubletThresholding.R`) |
| `pr-bodies.md` | PR titles and bodies |
| `test-runs.txt` | harness runs on the 1.16.0 build carrying the changes; testthat 17/17 on both builds |

The three patches are independent (each applies to `2d0e5e4` on its own).

## Verification status of the patches

See `test-runs.txt`: `../verify/*.patched.out` are the four harnesses on 1.16.0 + all three changes
(SD1: 0 % mislabelled, `mostLikelyOrigin` 100 %, halving and single-pair cases right; SD2: stats filled
for a factor; SD3: the documented quantile), with the package's 17 testthat tests passing on the
installed and the patched build.

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| SD1 | 1.4.0, 1.8.0, 1.12.0, 1.16.0 (executed); `devel` (same code) | `fix/artificial-doublet-order`; runs without `clusters` or with `adjustSize=0` |
| SD2 | 1.8.0, 1.12.0, 1.16.0 (executed); `devel` (same code) | `fix/factor-cluster-labels`; character or integer labels |
| SD3 | 1.8.0, 1.12.0, 1.16.0 (executed); `devel` (same code) | `fix/dbr-threshold-without-artificial`; input with a `cluster` column |

## Order of operations

1. Fork `plger/scDblFinder`; tell the session; the three branches are pushed.
2. Open the SD1 issue from `issue-sd1-artificial-doublet-origins.md`, then the PR from
   `fix/artificial-doublet-order` with the body from `pr-bodies.md` § PR 1 (issue number in the first
   line). Same for SD2 (`fix/factor-cluster-labels`, § PR 2).
3. When one of them has a reply, SD3 (`fix/dbr-threshold-without-artificial`, § PR 3).
4. Record issue and PR numbers and every response in `../README.md` and the top-level status table.
