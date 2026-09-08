# edgeR audit against 318 published papers (2021–2026)

_Generated 2026-09-08 against the Bioconductor git of `edgeR` (read through the
`bioc/edgeR` mirror): `RELEASE_3_23` @ `c4a54bda` (4.10.5, 2026-09-04, the current
release branch) and `devel` @ `db4e697f` (4.99.4, 2026-09-06). Focus: the pipeline the
cohort runs — `filterByExpr`, `normLibSizes`/`calcNormFactors`, `estimateDisp`,
`glmQLFit`/`glmQLFTest`, `glmFit`/`glmLRT`, `exactTest`, `topTags`, `cpm`/`rpkm`,
`decideTests` — verified by executing six shipped versions against independent ports of
the published methods._

## What this is

The six-journal survey found **318 papers** in PNAS (173), *Nature* (121), *Cell* (20)
and *Science* (4), 2021–2026, that used edgeR — the second most-used differential
expression package after DESeq2 (66 of them use both, 77 also name limma/voom). Its
statistical core was read in full on the two commits above and diffed against the 3.36.0,
4.0.16, 4.4.2 and 4.10.1 sources, and every suspicion was run through the installed
package: R 4.3.3 with edgeR 4.0.16 (the apt build on this host), 3.36.0, 4.4.2 and
4.10.1 (Ubuntu pool source tarballs), 4.10.5 and 4.99.4 (mirror branches), each in its
own library (`verify/rlib.sh`), against numpy/scipy ports written from the papers
(Robinson & Oshlack 2010 TMM; Robinson & Smyth 2008 exact test; McCarthy, Chen & Smyth
2012 Cox–Reid APL; Lund et al 2012 and Chen et al 2025 quasi-likelihood) or closed-form
arithmetic on synthetic negative-binomial data with known truth.

edgeR is mature and its authors are statisticians, and that is what the execution shows:
the normalisation, dispersion, GLM, quasi-likelihood, exact-test and multiple-testing
arithmetic reproduce the published methods to 1e-9 or better wherever a reference could
be computed, and the default pipeline is calibrated in typical and moderate dispersion
regimes. The three confirmed items are one floating-point boundary that is live on every
version and two offset-handling regressions that appeared in the 2026 release cycle and
were fixed by the maintainers before this audit ran.

## Findings (details and line citations in [`component-reviews/statistical-core.md`](component-reviews/statistical-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **EG3** | **CONFIRMED on 3.36.0, 4.0.16, 4.4.2, 4.10.1, 4.10.5 and `devel`** | now (low magnitude — lead's call) | `filterByExpr()` compares `cpm()` values computed in C as `y*1e6/lib.size` with a cutoff computed in R as `min.count/median(lib.size)*1e6`. With an odd number of samples the median library is a real library, and a gene with exactly `min.count` reads in it — mathematically on the cutoff, which the help page says is kept — fails the comparison by one ulp for 12.4 % of library sizes (17.2 % with the pre-4.4 C++). In 40 simulated data sets 148 of 1,589 such margin genes (9.3 %, about 4 per 20,000 genes) were dropped; every disagreement with the documented rule is this case. Minimal example: `L = (1e6, 1000010, 3e6)`, gene `(5, 10, 5)` → `FALSE` on all six versions. One-line fix with a test in the [kit](upstream/). |
| EG1 | CONFIRMED on the 4.10.0/4.10.1 release tarball; **fixed upstream** 2026-08-09 (4.10.5, `devel`); 3.36.0–4.4.2 unaffected | held (fixed) | `cpm()`/`rpkm()` on a DGEList carrying an offset matrix row-centred the offset and added it to `log(lib.size)`, counting each library size twice: CPM off by `geomean(L)/L_j` per column, log-CPM by up to 1.0 log2 units, RPKM by up to 8.8× on a four-fold library-size range. The maintainers reverted it as "restoring previous behavior"; no NEWS entry. |
| EG2 | CONFIRMED on 4.4.2 and 4.10.1 (4.4.0 through 4.10.3); **fixed upstream** 2026-08-29 (4.10.4); 3.36.0, 4.0.16 unaffected | held (fixed) | `aveLogCPM(y, offset=<matrix>)` skipped the offset setup for the first gene (`if((tag >= 1) && ...)`), returning 26.8 instead of 9.2 log2-CPM for gene 1. Reached only with a full offset matrix (not by the DGEList pipeline). |
| N1–N8 | notes | held | TMM tie blocks at the trim boundary (≤ 9.5e-4); exact-test tail choice (p ≥ 0.986 either way) and the `dispersion=0` rejection region; `topTags` `<=` vs `decideTests` `<` at the threshold; `glmQLFit` p-values still depend on a prior `estimateDisp()` through `AveLogCPM` (≤ 10 %) although NEWS 4.10.0 says results are now the same; default QL liberal in a harsh simulation regime (7.1 % null rate, FDR 8–11 %) while calibrated in typical/moderate ones; dispersion-grid interpolation (7e-4); Levenberg tolerance (p ≤ 5e-6); release-branch changes documented only in the `devel` NEWS. |

Four own suspicions were withdrawn by execution (R's `$` partial matching of
`offset`/`offset.prior`; two errors in the reference ports; the GLM residual). They are
recorded in the review.

**Held up under execution** (all on 4.10.5, most also on 4.0.16): TMM, RLE and
upper-quartile factors equal the Robinson–Oshlack port to 4.7e-15 including the
reference-library rule and inverse-variance weights; log-CPM equals the prior-count
formula to 5e-14, RPKM to 5e-15, `aveLogCPM` the one-group NB MLE to 2.5e-11; the exact
test equals a scipy enumeration of the conditional NB law to 2e-15 (relative 1.4e-14 on
every p < 0.05), its beta approximation is within 0.2 % at p ≈ 1e-3, and `exactTest()`'s
logFC is the documented shrunk estimate to 7e-15; the Cox–Reid APL equals the port to
1.7e-8, the common dispersion is exactly the spline maximiser of the port grid, `prior.df`
equals `limma::squeezeVar` on independent deviances, tagwise and trended dispersions
equal WLEB on the port grid to 1e-9; `glmFit`/`glmLRT`/`predFC` equal an NB-GLM port
within the Levenberg tolerance; both QL methods' F, denominator df and p recompute from
their components to 1e-13; BH runs over all tested genes; the full default pipeline is
calibrated (null rate 5.2 %, empirical FDR 4.7–5.3 %) where `glmLRT`/`exactTest` are not
(7.7–8.2 %). Not audited: `glmTreat`, `diffSplice`, `voomLmFit`, gene-set tests, the
Salmon/kallisto/RSEM readers, `robust=TRUE`, observation weights, plotting.

## How the papers use edgeR (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| voom / limma also named | 77 |
| DESeq2 also used | 66 |
| TMM / `normLibSizes` / `calcNormFactors` named | 62 |
| featureCounts / Rsubread upstream | 59 |
| pseudo-bulk / single-cell | 58 |
| adjusted p / FDR / BH | 53 (cutoffs: 0.05 ×26, 0.01 ×5, 0.1 ×2) |
| batch / covariate / paired design | 52 |
| ATAC / ChIP / CUT&RUN / methylation | 42 |
| cpm / logCPM / rpkm / TPM reported | 39 |
| Salmon / kallisto / tximport | 32 |
| edgeR version stated | 29 in the cache text, 82 with a survey-recorded version (3.32.1 ×7, 3.36.0 ×6, 3.26.8 ×6, 3.30.3 ×5, 3.40.2 ×4, 3.24.3 ×4, 3.42.4 ×4, 4.0.16 ×3, 4.2.2 ×3; 65 papers name a 3.x version, 15 a 4.x) |
| log fold-change cutoff | 21 (1 ×5, 2 ×3) |
| `glmQLFit` / QL F-test named | 12 |
| `filterByExpr` / low-count filter described | 9 |
| CRISPR screen / sgRNA | 8 |
| `glmFit` / `glmLRT` / `exactTest` / `estimateDisp` named | 7 / 5 / 5 |
| gene-set tests (camera/fry/roast/goana) | 3 |

Exposure by finding: EG3 is present in every version the cohort names and needs an odd
number of samples (the survey cache does not record sample counts); EG1 and EG2 need an
offset matrix in the DGEList (cqn, EDASeq, RUVSeq, csaw users — none identifiable from
the cache) and, for EG1, edgeR 4.10.0–4.10.2 (April–August 2026; only the 33 papers from
2026 could have used it, one of which names 4.6.2, none names 4.10).

**Profiling caveat.** As for the Seurat and Scanpy audits, this session had no route to
Europe PMC, so `edger_profile.py` ran in `--offline` mode over the survey's stored
evidence snippets; every record in `edger_profiles.jsonl` is `source: survey_cache` and
every count above is a lower bound. Rerun without `--offline` from a host with Europe
PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- edgeR is a Bioconductor package: its git lives at `git.bioconductor.org` (not
  reachable from this session; `bioc/edgeR` on GitHub is a read-only mirror with issues
  disabled), there is no `CONTRIBUTING`, no issue or PR template, no linter, and no
  changelog convention beyond the maintainer-written `inst/NEWS.Rd`. `vignettes/intro.Rmd`
  line 44: "Further questions about the package should be directed to the Bioconductor
  support site"; `DESCRIPTION` names the maintainers (Yunshun Chen, Gordon Smyth) with
  e-mail addresses. The channel is therefore a support-site post tagged `edgeR` with a
  reproducible example and the patch attached as a diff, or the same by e-mail — never a
  cold PR.
- The project's tests are `tests/edgeR-Tests.R` with `edgeR-Tests.Rout.save`, compared
  by `R CMD Rdiff`; the patch adds one boundary case there and updates the saved output.
- No fork `cindykrafft/edgeR` exists, so no `upstream-declines-ai-contributions` topic
  applies. The tracker search (`mcp__github__search_issues`, one query) found nothing
  relevant; the support site cannot be searched from this session and must be searched
  before posting.
- **The kit is in [`upstream/`](upstream/)**: the EG3 support-site post with the minimal
  example run on 4.10.5, two `git am`-able patches (fix + test + saved output) against
  `devel` and `RELEASE_3_23`, and the list of documents read. EG1 and EG2 are fixed and
  are not filed; N5 could become a support-site *question* after EG3 has an answer.

## Files

| file | what |
|---|---|
| `edger_profile.py`, `edger_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/statistical-core.md` | the review: EG1–EG3, N1–N8, withdrawn W1–W4, held-up list, not-audited list |
| `verify/rlib.sh`, `verify/rrun.py`, `verify/nbglm.py` | version selector for the six builds; R runner for the Python harnesses; independent NB-GLM fitter |
| `verify/eg1_cpm_offset.R` (+ `.v<version>.out` ×6) | EG1 and EG2: cpm/rpkm/aveLogCPM with offsets vs closed-form references; `getOffset` |
| `verify/eg3_filterbyexpr_boundary.R` (+ `.out` ×6) | EG3: boundary failure rate over 200,000 library sizes, 40 simulated data sets, minimal example |
| `verify/heldup_filterbyexpr.R` (+ `.out` ×2) | held-up: the documented rule in five call forms |
| `verify/heldup_tmm_port.py` (+ `.out` ×2) | held-up: TMM/RLE/UQ vs the Robinson–Oshlack port; N1 |
| `verify/heldup_exact_test.py` (+ `.out` ×2) | held-up: exact test vs enumeration, beta approximation, `exactTest()` end to end; N2 |
| `verify/heldup_cpm_avelogcpm.py` (+ `.out` ×2) | held-up: log-CPM, RPKM, `aveLogCPM` ports |
| `verify/heldup_apl_disp.py` (+ `.out`) | held-up: Cox–Reid APL, common/trended/tagwise dispersions, `prior.df`; N6 |
| `verify/heldup_glm_lrt_ql.py` (+ `.out` ×2) | held-up: `glmFit`/`glmLRT`/`predFC`, legacy and new QL arithmetic; N7 |
| `verify/sim_ql_calibration.R` (+ `.out` ×2) | held-up / N5: type I error and FDR of the four tests in three dispersion regimes |
| `verify/note_toptags_decidetests.R`, `verify/note_glmqlfit_disp_source.R` (+ `.out`) | N3, N4 |
| `upstream/` | filing kit: support-site post, patches for `devel` and `RELEASE_3_23`, PR-body section, documents read |

Harnesses need the builds described in `verify/rlib.sh` (sources from
`archive.ubuntu.com/ubuntu/pool/universe/r/r-bioc-edger/` and `r-bioc-limma/`, mirror
branches from `github.com/bioc/edgeR`; `R CMD INSTALL --no-docs --library=<lib>`), and a
Python 3.12 venv with numpy 2.5.3 and scipy 1.18.1 for the ports. The 3.36.0 build
needs the three-line `FCONE` patch described in `rlib.sh` because its C++ predates R
4.3's Fortran-length API. Europe PMC, CRAN, Bioconductor and `git.bioconductor.org` were
unreachable; the Bioconductor git was read through the GitHub mirror.

## Next steps

1. Search the Bioconductor support site for prior reports of the `filterByExpr` boundary,
   then post EG3 from the kit with the `RELEASE_3_23` patch attached; record the reply here
   and in the top-level table.
2. If the maintainers respond, raise N5 (QL calibration in the harsh regime) as a
   question with the simulation script, and N4 as a one-line NEWS wording note.
3. Extend the review to `glmTreat` and `diffSplice`, the remaining test paths cohort
   papers name, and full-text profiling when Europe PMC is reachable (sample counts per
   paper decide EG3's exposure).
