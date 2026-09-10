# limma upstream filing kit

Default branch of the mirror `bioc/limma`: **`devel`** (Bioconductor's development
branch; releases live on `RELEASE_3_NN` branches, the current one `RELEASE_3_23`).
Audited commits: `devel` @ `57a8de7296ad733ac25d3e3c01de3fdddcd0a9ae` (3.99.0,
2026-08-30) and `RELEASE_3_23` @ `825d1c8330d024adb6c54af66d79b0f4ec258530` (3.68.5,
2026-08-10). **Nothing has been filed, posted, e-mailed or pushed.**

## Channel (step 4 of the method)

limma is a Bioconductor package. Its canonical git is `git.bioconductor.org` (not
reachable from this session) and `github.com/bioc/limma` is a **read-only mirror with no
issue tracker and no pull requests** — so there is no PR body in this kit, because there
is no repository that can accept one.

The channel is the **Bioconductor support site**, https://support.bioconductor.org, tag
`limma` (`vignettes/intro.Rmd:39`: "Further questions about the package should be
directed to the Bioconductor support site"), with the patch attached as a diff; or the
same by e-mail to the maintainer named in `DESCRIPTION` (`cre`: Gordon Smyth,
`smyth@wehi.edu.au`; `aut`: Lizhong Chen, who wrote the C kernel this touches). A
patch that changes results goes there first, never as a cold PR (the DESeq2 round's
lesson, top-level README step 4).

**The support site is unreachable from this session** — as are CRAN, Bioconductor and
`git.bioconductor.org` — so it could **not** be searched for prior reports, and it could
not be checked whether a thread on `arrayWeights` convergence already exists. That
search is a precondition for posting.

## What was read before preparing this

- `DESCRIPTION` on both branches: maintainer and authors, `URL:
  https://bioinf.wehi.edu.au/limma/`, no `BugReports` field. `NAMESPACE`.
- `vignettes/intro.Rmd` — the one statement of where questions go (line 39).
- `inst/NEWS.Rd` on `devel`, in full for the 4.0.0 section: the items that move
  `voomLmFit()` into limma and make it call `arrayWeights(method="reml")` for sample
  weights (lines 7-17), the `nthreads` item, and the item announcing the "C code backend
  for `.arrayWeightsPrWtsREML()`, which is called by arrayWeights() when `method="reml"`
  and prior weights" (lines 54-55) — i.e. the maintainers rewrote this function in C for
  4.0.0 and carried the criterion over unchanged. Also the 3.40.0 section ("Major rewrite
  of arrayWeights()"), which is where the prior-weights branch was split off (the file
  header of `R/arrayWeightsPrWtsREML.R` reads "Created 12 Feb 2019 from
  `.arrayWeightsREML`"). `inst/doc/changelog.txt` for the same period.
- `man/arrayWeights.Rd`: the Details section, which documents the `method="auto"` rule
  ("REML is chosen if there are no prior weights or missing values and otherwise the
  gene-by-gene algorithm is used") and the `prior.n` prior; `\item{tol}` is documented
  only as "convergence tolerance when `method="reml"`". `man/contrasts.fit.Rd` (for N1).
- The project's test convention. On `RELEASE_3_23` it is a single
  `tests/limma-Tests.R` with `tests/limma-Tests.Rout.save`, compared by `R CMD Rdiff`
  (the saved file has CRLF line endings and was generated on Windows with R 4.6.0 alpha).
  On `devel` there are additionally standalone `stopifnot()` scripts with no saved output
  — `dupcor-c.R`, `gls-series-c.R`, `lm-series-c.R`, `lmfit-contrasts.R`,
  `voomlmfit-contrasts.R`, added for the new C backends and announced in NEWS. The
  `devel` patch adds `tests/arrayweights-reml.R` in that style; the `RELEASE_3_23` patch
  appends to `limma-Tests.R` and updates the saved output, as the branch requires.
- Code style: tab indentation, a comment header per function with author and "Last
  revised" date; the release patch updates that date. The C files carry block comments
  explaining the algebra; the devel patch adds one where the criterion is computed.
  There is **no** `CONTRIBUTING`, no `.github/` directory, no issue or PR template, no
  linter and no lint configuration in the repository (checked on both branches).
- Prior reports: `mcp__github__search_issues` was run with three phrasings
  ("limma arrayWeights REML convergence prior weights sample weights not converged
  voomLmFit"; "arrayWeights convergence criterion divided by number of genes iteration
  stops early limma"; "voomWithQualityWeights sample weights differ genebygene reml
  limma"). It returned **nothing in any limma or Bioconductor repository** — the nearest
  hits were unrelated `lme4` issues about prior weights and convergence (#578, #192,
  #783, #880) and unrelated bedtools/scanpy/samtools issues. limma has no GitHub tracker,
  so this is expected; the support-site search is the one that matters and could not be
  run.
- No fork `cindykrafft/limma` exists (GitHub repository search, 2026-09-10), so no
  `upstream-declines-ai-contributions` topic applies and the kit may be filed.
- Matthew Rocklin's "Craft Minimal Bug Reports": the post's example is 500 genes x 6
  arrays made in the script, one call with weights and one without, ends in two rows that
  should be identical and are not, states expected vs got, and records what shrinking
  revealed (the weight values are irrelevant — all ones is enough; the gap is exactly the
  factor `ngenes + prior.n`, so it is not data-dependent and not floating point).

## Contents

| file | what |
|---|---|
| `issue-l1-arrayweights-reml-convergence.md` | the support-site post for L1 (Title line + body), minimal example run on 3.68.5 and 3.99.0 |
| `0001-arrayWeights-reml-prior-weights-convergence-criterion.RELEASE_3_23.patch` | fix + test + saved output against `RELEASE_3_23` @ `825d1c83`; that branch stores CRLF, so apply with `git am --keep-cr` or `git apply` |
| `0001-arrayWeights-reml-prior-weights-convergence-criterion.devel.patch` | the same against `devel` @ `57a8de72` (C kernel + `tests/arrayweights-reml.R` + a NEWS item); `git am`-clean |

No `pr-bodies.md`: the mirror takes no pull requests (Round 4 rule for
`github.com/bioc/*`).

## Verification of the patches

Built with `R CMD INSTALL --no-docs --library=<lib>` on R 4.3.3 and run through the
project's own tests.

`RELEASE_3_23`, `R CMD BATCH --vanilla tests/limma-Tests.R` then
`R CMD Rdiff` against the **updated** `limma-Tests.Rout.save`:

| build | Rdiff lines |
|---|---|
| unpatched | 92 — the new case prints `[1] "Mean relative difference: 0.007134731"` |
| + patch | 88 — the new case prints `[1] TRUE` |

88 is the baseline: this host is Linux with R 4.3.3 and the saved output was generated on
Windows with R 4.6.0 alpha, so the header block and a `summary()` of simulated values
differ either way. The patch removes exactly the 4 lines it is responsible for.

`devel`, each test script run with `Rscript`:

| test | unpatched | + patch |
|---|---|---|
| `tests/arrayweights-reml.R` (new) | **FAIL** — `max(abs(aw0 - aw1)) < 1e-08 is not TRUE` | PASS |
| `tests/dupcor-c.R` | PASS | PASS |
| `tests/gls-series-c.R` | PASS | PASS |
| `tests/lm-series-c.R` | PASS | PASS |
| `tests/lmfit-contrasts.R` | PASS | PASS |
| `tests/voomlmfit-contrasts.R` | PASS | PASS |
| `tests/limma-Tests.R` (Rdiff) | 88 lines (baseline) | 88 lines (baseline) |

There is no linter to run: the repository has no lint configuration on either branch.

The extended evidence is `../verify/l1_arrayweights_reml_convergence.*.out` (7 versions
plus both patched builds), `../verify/l1_voom_sample_weights_magnitude.*.out` (magnitude
and DE counts) and `../verify/l1_exposure_default_paths.*.out` (which call paths reach
the branch).

## Tiers and order

| id | tier | why |
|---|---|---|
| L1 | **now** — and specifically before limma 4.0.0 | wrong number at master on every version from 3.42.2 on; today reached only by an explicit `method="reml"`, but NEWS 4.0.0 makes it `voomLmFit()`'s default sample-weight path, so the cost of filing late rises sharply at the next release. One-term fix, tests for both branches, no behaviour change for any other call. |
| N1 | held | `contrasts.fit`'s approximation under voom weights is documented; its *size* (5 vs 2 genes at BH < 0.05) is a help-page question, worth raising only after L1 has an answer |
| N2–N7 | held | boundary conventions, approximation accuracies and design defaults; none is a wrong number |

Filing cap is two unanswered filings per repository; **L1 goes first and alone**.

## Order of operations

1. Search https://support.bioconductor.org for `arrayWeights`, "sample weights" and
   "voomLmFit" and read every matching thread in full. If a thread already covers this,
   turn the post into a comment on it (`comment-l1-…md`, first line
   `Title: (comment on #N) …`) and record the thread's comment count here first — no
   comment goes out before every comment on the thread has been read.
2. If nothing matches, post `issue-l1-arrayweights-reml-convergence.md` tagged `limma`,
   with `…RELEASE_3_23.patch` attached and `…devel.patch` linked.
3. Record the post URL and every maintainer reply in `../README.md` and the top-level
   status table. Nothing else goes out until they reply.
