# limma upstream filing kit

Default branch of the mirror `bioc/limma`: **`devel`** (Bioconductor's development branch;
releases live on `RELEASE_3_NN` branches, the current one `RELEASE_3_23`). Audited commits:
`devel` @ `57a8de72` (3.99.0, 2026-08-30) and `RELEASE_3_23` @ `825d1c83` (3.68.5,
2026-08-10). Nothing has been filed, posted or pushed.

## Channel (step 4 of the method)

limma is a Bioconductor package. Its canonical git is `git.bioconductor.org` (not reachable
from this session), and the GitHub mirror is read-only with issues disabled, so there is no
tracker and no PR flow. The channel is the **Bioconductor support site**
(`vignettes/intro.Rmd:39`: "Further questions about the package should be directed to the
Bioconductor support site"), tag `limma`, with the patch attached as a diff; the maintainer
(Gordon Smyth) is named with an e-mail address in `DESCRIPTION`, and Lizhong Chen is the
author of the 4.0.0 C code that LI1's `devel` patch touches. Results-affecting changes go
there first, never as a cold PR (the DESeq2 round's lesson, top-level README step 4). The
support site cannot be reached from this session and **must be searched before posting**.

## What was read before preparing this

- `DESCRIPTION` (maintainer, authors, `URL`, no `BugReports` field), `NAMESPACE`,
  `vignettes/intro.Rmd` (the help/support statement).
- `inst/NEWS.Rd` on both branches, in full for 3.60.0 → 4.0.0: the 4.0.0 items (C backends
  for `lm.series`, `gls.series`, `duplicateCorrelation` and `.arrayWeightsPrWtsREML`,
  `voomLmFit` transferred from edgeR and now calling `arrayWeights(method="reml")` when no
  df are lost, `voomLmFit` giving `offset` priority over `offset.prior`/`lib.size`, the
  `contrasts` argument), the 3.68.0 items (`offset` and `offset.prior` for `voom`,
  `adaptive.span` default), 3.66.0 (`span` and `legacy` for `squeezeVar`/`eBayes`,
  `removeBatchEffect` covariate centring), 3.64.0 (`diffSplice`).
- `inst/doc/changelog.txt` (both branches): the maintainers' dated per-version entries,
  one section per commit; the patches add their bullets there (under the existing 3.99.0
  section on `devel`; under a proposed "13 Sep 2026: limma 3.68.6" heading on the release
  branch, for the maintainer to relabel).
- `tests/limma-Tests.R` + `limma-Tests.Rout.save` (compared by `R CMD Rdiff`; 76 lines
  already differ on this platform without any patch) and, on `devel`, the stand-alone
  `stopifnot` test scripts added with the C code (`tests/lm-series-c.R`,
  `gls-series-c.R`, `dupcor-c.R`, `lmfit-contrasts.R`, `voomlmfit-contrasts.R`). The patches
  follow the latter convention: `tests/arrayweights-reml.R` and `tests/voom-offset.R`.
- Code style: tab indentation, a comment header per function with author and "Last
  modified" date (the patches update it); `RELEASE_3_23` files carry CRLF line endings (the
  release patch keeps them; apply with `git am --keep-cr`), `devel` files LF.
- `man/arrayWeights.Rd` (the `method`, `tol`, `maxiter` items and the auto rule),
  `man/voomLmFit.Rd`, `man/voomWithQualityWeights.Rd`, `man/voom.Rd` (the `offset` and
  `offset.prior` items and the Details paragraph that LI2's patch rewrites),
  `man/contrasts.fit.Rd` (the approximation statement, N2).
- edgeR's `voomLmFit` on 4.0.16 (apt) and 4.10.5 (the edgeR audit's `RELEASE_3_23` build)
  and `scaleOffset`'s help page, to state the offset convention LI2 relies on.
- No fork `cindykrafft/limma` exists (GitHub repository search 2026-09-13), so no
  `upstream-declines-ai-contributions` topic applies.
- Prior reports: `mcp__github__search_issues` for "limma arrayWeights REML convergence
  prior weights voom sample weights" and "limma contrasts.fit approximation weights
  stdev.unscaled non-orthogonal" returned only unrelated issues in other repositories
  (lme4 #192, #880, #783, #338; umap #601; plink-ng #466; freesurfer #1463); limma has no
  GitHub tracker.
- Matthew Rocklin's "Craft Minimal Bug Reports": each post's example is made in the script,
  ends in an unexpected number, states expected vs got, and records what shrinking revealed.

## Contents

| file | what |
|---|---|
| `issue-li1-arrayweights-reml-convergence.md` | the support-site post for LI1 (Title line + body), example run on 3.68.5 and devel |
| `0001-arrayWeights-fix-the-convergence-criterion-of-the-pr.patch` | LI1 fix (`src/awreml.c`) + test + changelog/NEWS against `devel` @ `57a8de72` (`git am`-clean) |
| `0001-arrayWeights-fix-the-convergence-criterion.RELEASE_3_23.patch` | LI1 fix (`R/arrayWeightsPrWtsREML.R`) + test + changelog against `RELEASE_3_23` @ `825d1c83` (CRLF branch: `git am --keep-cr`) |
| `issue-li2-voom-offset-double-count.md` | the support-site post for LI2 |
| `0002-voom-give-an-edgeR-style-offset-precedence-over-lib.size.patch` | LI2 change (`R/voom.R`, `man/voom.Rd`) + test + changelog/NEWS against `devel`, on top of 0001 |
| `pr-bodies.md` | the notes accompanying the patches, in the kit's fixed PR-body format |

## Verification of the patches

Built with `R CMD INSTALL --no-docs` and run through the project's own tests
(`R CMD BATCH --vanilla tests/limma-Tests.R` then `R CMD Rdiff` against
`limma-Tests.Rout.save`; the `devel` `stopifnot` scripts with `Rscript`):

| build | `limma-Tests.R` Rdiff | new test files | devel C tests |
|---|---|---|---|
| `devel` unpatched | 76 lines (pre-existing) | `arrayweights-reml.R` FAIL (`all.equal(w0, w1)` not TRUE), `voom-offset.R` FAIL (`all.equal(v0$E, v1$E)` not TRUE) | — |
| `devel` + 0001 + 0002 | 76 lines, identical set | both PASS | all five PASS |
| `RELEASE_3_23` unpatched | 76 lines (pre-existing) | `arrayweights-reml.R` FAIL | — |
| `RELEASE_3_23` + 0001 | 76 lines, identical set | PASS | — |

The harnesses `../verify/lm1_arrayweights_prwts_convergence.R` and
`../verify/lm2_voom_offset_double_count.R` on the patched builds
(`.vdevel-patched.out`, `.v3.68.5-patched.out`) show the two REML routines agreeing to
1.8e-14 with 5 iterations each, and the DGEList offset example returning identical `E`
(8.9e-16) and 37 vs 37 genes.

## Tiers and ranking (filing cap: two unanswered filings per repository)

| id | tier | why |
|---|---|---|
| LI1 | **now, first** | wrong number on every version since 2019 at default settings of a documented method; no help-page text defends it; becomes the default sample-weight path of `voomLmFit()` in 4.0.0; one-line fix on each branch, a single post is the whole cost |
| LI2 | **now, second** | wrong logCPM/logFC for the edgeR objects the feature targets, on the current release and in edgeR 4.10.x; documented, so it is offered as a semantics question (align `voom()` with the new `voomLmFit()` reading, as the 4.0.0 NEWS already does for `voomLmFit`) rather than a bug report; the devel patch is the proposal |
| N1, N2 | held (questions) | the df.prior floor of the unequal-df estimator; a help-page sentence for voom users on the `contrasts.fit` approximation — after LI1 has an answer |
| N3–N9 | held | design choices, documented approximations, cosmetic |

## Order of operations

1. Search the support site for "arrayWeights reml", "voomWithQualityWeights reml" and
   ".arrayWeightsPrWtsREML"; if nothing matches, post `issue-li1-arrayweights-reml-convergence.md`
   with the `RELEASE_3_23` patch attached (and the `devel` one linked), tag `limma`.
2. Record the post URL and every maintainer reply in `../README.md` and the top-level status
   table.
3. When LI1 is answered (or after a reasonable interval), search for "voom offset DGEList"
   and post `issue-li2-voom-offset-double-count.md` with the `devel` patch. Nothing else goes
   out until they reply.
