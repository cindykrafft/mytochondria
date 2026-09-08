# edgeR upstream filing kit

Default branch of the mirror `bioc/edgeR`: **`devel`** (Bioconductor's development
branch; releases live on `RELEASE_3_NN` branches, the current one `RELEASE_3_23`).
Audited commits: `devel` @ `db4e697f` (4.99.4, 2026-09-06) and `RELEASE_3_23` @
`c4a54bda` (4.10.5, 2026-09-04). Nothing has been filed, posted or pushed.

## Channel (step 4 of the method)

edgeR is a Bioconductor package. Its canonical git is `git.bioconductor.org` (not
reachable from this session), and the GitHub mirror is read-only with issues disabled, so
there is no tracker and no PR flow. The channel is the **Bioconductor support site**
(`vignettes/intro.Rmd:44`: "Further questions about the package should be directed to
the Bioconductor support site"), tag `edgeR`, with the patch attached as a diff; the
maintainers (Yunshun Chen, Gordon Smyth) are named with e-mail addresses in
`DESCRIPTION`. Results-affecting changes go there first, never as a cold PR (the DESeq2
round's lesson, top-level README step 4).

## What was read before preparing this

- `DESCRIPTION` (maintainers, `URL`, no `BugReports` field), `NAMESPACE`,
  `vignettes/intro.Rmd` (the help/support statement), the User's Guide stub
  (`vignettes/edgeRUsersGuide.Rnw`, PDF only).
- `inst/NEWS.Rd` on both branches, in full for 4.0.0 → 4.10.0 and the `devel` 5.0.0
  section: the 4.10.0 entries (dispersion cap, `glmQLFit` no longer reading trended
  dispersions, `DGEListFromTximport`), the 4.4.0 entries (C rewrite, `top.proportion`
  default, `s2.post` rename), the 4.2.0 default switch to `legacy=FALSE`, the 4.8.0 span
  change, and the 5.0.0 `offset.prior` and `estimateDisp` items. No 4.10.x point-release
  entries exist; the release-branch commit messages (`git log RELEASE_3_23`, read for
  4.9.1 → 4.10.5) are the maintainers' statements for EG1 (`1da6863`, "Restoring previous
  behavior …"), EG2 (`f8bb002`, "Fix bug in aveLogCPM() when offset matrix is provided")
  and N8 (`bc2f1e1`). Both are therefore known and fixed upstream and are **not filed**.
- `tests/edgeR-Tests.R` and `tests/edgeR-Tests.Rout.save`: the project's test convention
  (a script whose output is compared by `R CMD Rdiff`; `options(warnPartialMatch…)` on).
  The patch adds one case there. There is no linter, no CONTRIBUTING, no template.
- Code style: tab indentation, a comment header per function with author and "Last
  modified" date; the patch updates that date.
- No fork `cindykrafft/edgeR` exists (GitHub repository search 2026-09-08), so no
  `upstream-declines-ai-contributions` topic applies.
- Prior reports: `mcp__github__search_issues` for "edgeR cpm offset library sizes wrong"
  returned two unrelated issues in other repositories (Suite2p #404, deepTools #974);
  edgeR itself has no GitHub tracker. The support site is not reachable from this session
  and **must be searched for "filterByExpr" before posting**.
- Matthew Rocklin's "Craft Minimal Bug Reports": the post's example is two genes and
  three library sizes, made in the script, ends in an unexpected `FALSE`, states expected
  vs got, and records what shrinking revealed (odd sample count; exactly `min.count` reads
  in the median library; design irrelevant beyond `MinSampleSize`).

## Contents

| file | what |
|---|---|
| `issue-eg3-filterbyexpr-boundary.md` | the support-site post for EG3 (Title line + body), example run on 4.10.5 |
| `0001-filterByExpr-tolerate-last-bit-rounding-at-the-CPM-c.patch` | fix + test + saved output against `devel` @ `db4e697f` (`git am`-clean) |
| `0001-filterByExpr-tolerate-last-bit-rounding.RELEASE_3_23.patch` | the same against `RELEASE_3_23` @ `c4a54bda` (CRLF branch: `git am --keep-cr` or `git apply`) |
| `pr-bodies.md` | the note accompanying the patch, in the kit's fixed PR-body format |

## Verification of the patches

Built with `R CMD INSTALL --no-docs` against limma 3.68.4 and run through the project's
own test file (`R CMD BATCH --vanilla tests/edgeR-Tests.R`, then `R CMD Rdiff` against
`edgeR-Tests.Rout.save`):

| build | Rdiff vs the updated saved output |
|---|---|
| `devel` unpatched | 4 lines: the new case prints `[1] FALSE  TRUE` |
| `devel` + patch | 0 lines |
| `RELEASE_3_23` unpatched | 4 lines: the new case prints `[1] FALSE  TRUE` |
| `RELEASE_3_23` + patch | 0 lines |

The harness `../verify/eg3_filterbyexpr_boundary.R` is the extended evidence (six
versions).

## Tiers

| id | tier | why |
|---|---|---|
| EG3 | **now** (low magnitude; the lead decides) | wrong decision of a documented rule on the current release at default settings; changes the retained gene set by ~4 genes per 20,000 with an odd number of samples; one-line fix; a single support-site post is the whole cost |
| EG1, EG2 | held (fixed upstream) | reverted/fixed by the maintainers on 2026-08-09 and 2026-08-29; the audit records them for users of 4.10.0–4.10.3 with offsets |
| N4 | held | NEWS wording vs code (AveLogCPM dependence); mention only if EG3 gets a reply |
| N5 | held (question, not a report) | QL calibration in a harsh simulation regime; a support-site question with the script, after EG3 |
| N1–N3, N6–N8 | held | design choices and cosmetic points |

## Order of operations

1. Search the support site for `filterByExpr` and "CPM cutoff"; if nothing matches, post
   `issue-eg3-filterbyexpr-boundary.md` with the `RELEASE_3_23` patch attached (and the
   `devel` one linked), tag `edgeR`.
2. Record the post URL and every maintainer reply in `../README.md` and the top-level
   status table. Nothing else goes out until they reply.
