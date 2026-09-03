# Component: Seurat differential expression (`R/differential_expression.R`)

Read in full on `main` @ `084d9e4` (2026-08-28, 2,569 lines): `FindAllMarkers`,
`FindConservedMarkers`, the `FindMarkers` methods (default/Assay/StdAssay/SCTAssay/
DimReduc/Seurat), the `FoldChange` methods, `PerformDE` and every test it dispatches to
(`WilcoxDETest`, `DiffExpTest` [bimod], `MarkerTest` [roc], `DiffTTest`, `GLMDETest`
[negbinom/poisson], `LRDETest`, `MASTDETest`, `DESeq2DETest`), `PrepSCTFindMarkers`,
`RegularizedTheta`, `ValidateCellGroups`, `IdentsToCells`. The same functions were read
at tags `v3.2.2`, `v4.3.0` and `v5.1.0` to date every difference, and `git log` on the
file between `v4.3.0` and `v5.0.0` was walked commit by commit. The external
implementations the Wilcoxon and MAST paths call were read from clones of
`immunogenomics/presto` and `RGLab/MAST` (2026-09-02); `limma` could not be fetched
(Bioconductor git is denied by this session's network policy).

Verification: faithful Python ports executed on simulated data with known truth
(`../verify/`). No R was available in this session, so nothing here was run through the
shipped package; the ports are of formulas short enough to transcribe exactly and are
quoted with line numbers.

Exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### SE1 — CONFIRMED (behaviour change, v5.0.0, undocumented): the reported fold change changed formula, and the new formula's pseudocount depends on group size

**What the code does.** `FoldChange` subtracts a per-group "mean function" of the
`data` layer. The function shipped has changed three times:

| versions | `avg_log(2)FC` per group | prefilter default | source |
|---|---|---|---|
| v3.x (≤ 3.2.3) | `ln(mean(expm1(x)) + 1)` | `logfc.threshold = 0.25` | `v3.2.2:R/differential_expression.R:557` |
| v4.0.0–4.4.0 | `log2(mean(expm1(x)) + 1)` | 0.25 | `v4.3.0:R/differential_expression.R:757` |
| v5.0.0 → main | `log2((sum(expm1(x)) + 1) / n_group)` | 0.1 | `main:R/differential_expression.R:812, 1123, 1128, 1201` (commit `69b054b7`, 2023-10-18, "change +1 in FoldChange"; default threshold in `d6b0152a`, 2023-10-13) |

`x` is the LogNormalize'd value `log1p(count / libsize × 1e4)`, so `expm1(x)` is the
normalized count and `mean(expm1(x))` the group's normalized mean μ. The v5 expression
equals `log2(μ + 1/n_group)`: the pseudocount is 1 on the group *total*, i.e. `1/n₁` for
`ident.1` and `1/n₂` for `ident.2`. The roxygen (line 674) still says "Pseudocount to add
to averaged expression values", which describes v4.

**Consequence 1 (exact).** For a gene with the same mean μ in both groups,

    avg_log2FC = log2((μ + 1/n₁) / (μ + 1/n₂))

which is zero only when n₁ = n₂. In `FindAllMarkers`, `ident.1` is one cluster and
`ident.2` every other cell, so n₁ < n₂ always and the term is positive. Values
(`../verify/se1_foldchange_group_size.py`, part A):

| n₁ vs n₂ | μ = 0.01 | 0.03 | 0.1 | 0.3 | 1 |
|---|---|---|---|---|---|
| 50 vs 5,000 | 1.56 | 0.73 | 0.26 | 0.09 | 0.03 |
| 200 vs 20,000 | 0.58 | 0.22 | 0.07 | 0.02 | 0.01 |
| 1,000 vs 20,000 | 0.13 | 0.05 | 0.01 | 0.005 | 0.001 |

μ here is on Seurat's ×10⁴ scale, on which most genes in a 10x dataset sit below 0.1.
So for small clusters the systematic term alone exceeds the common publication cutoff
of 0.25 for every gene with μ ≲ 0.03–0.1.

**Consequence 2 (simulated, 10x-like NB data, 5,000 genes, 10 % truly DE; part B2).**
Among *null* genes that pass `min.pct = 0.01`, in the lowest expression bin
(μ ∈ [0.005, 0.02)) the share reported with `avg_log2FC > +0.25` is

| cluster size n₁ (vs rest of 5,000) | v5 | v4 |
|---|---|---|
| 50 | 85 % | 0 % |
| 100 | 88 % | 0 % |
| 300 | 79 % | 0 % |
| 1,000 | 49 % | 0 % |

(The bin's mean reported FC exceeds the exact term because the `min.pct` filter
preferentially keeps genes with ≥ 1 count in the small group; that selection is part
of `FindMarkers` and is reproduced faithfully.) Across all expression bins, v5 reports
20–45 % of null genes beyond ±0.25 in either direction for n₁ ≤ 300, against ≤ 4 %
under v4. The prefilter itself is effectively removed for small clusters: at n₁ = 100,
3,272 of 4,500 null genes pass `|logFC| ≥ 0.1` under v5 versus 71 passing 0.25 under
v4 (part B1).

**Consequence 3 (what did *not* change).** The p-value never sees the fold change, so
significance calls are the same under both formulas given the same prefilter. Among
truly DE genes reaching Bonferroni `p_val_adj < 0.05` (part C), no sign flips occurred
under either version at any cluster size, and v5's reported magnitude is close to the
true log2 ratio (median reported/true 0.93–1.13) where v4 compressed it to roughly
half (0.38–0.69). So for genes that are genuinely and detectably DE, v5's number is the
*better* one; the damage is confined to the low-expression, small-cluster regime and
to comparability across versions.

**Why it matters for the cohort.** Papers threshold, rank and plot `avg_log2FC`: 18
cohort papers state a log-fold-change cutoff in the cached evidence alone (2 ×5, 1.5 ×4,
1 ×4, 0.5 ×3, 0.25 ×1), 193 run GSEA on ranked lists, and marker tables are supplementary
data in most single-cell papers. The two consequences for reproducibility:

- A v4 table and a v5 table of the same data are not comparable: v4 values are about
  half the true log2 ratio for the typical gene, v5 values are near the true ratio.
  The cohort straddles the boundary (203 papers pin v4, 61 pin v5, 428 unstated) and
  NEWS.md for 5.0.0 does not mention either the formula or the default-threshold change
  (it lists "Default fold change in FindMarkers() changed from ln to log2" — the v4
  change — and "Fix FoldChange and FindMarkers to support all normalization approaches",
  which is #7115, a different change).
- Under v5, marker lists for small clusters (rare cell types, the case where a
  marker list is most consequential) carry inflated positive fold changes for lowly
  expressed genes. A gene reported as a rare-cluster marker with `avg_log2FC` 0.3–1.5,
  `pct.1` 0.01–0.05 and a non-significant `p_val_adj` is the signature.

**Upstream state (read before filing).** Seurat's tracker already has this:
issue #9346 "FoldChange results depend on the group size" (2024-09-29), which derives
the same asymmetry on a toy object, proposes a fixed small pseudocount as Scanpy uses,
and was closed as completed on 2024-10-23 with four comments. Issue #8128 (2023-12-04)
reported the v4/v5 formula difference and was closed the next day with no comments.
The formula on `main` is unchanged, so #9346 was closed without a code change. **The
maintainers' reply on #9346 could not be read from this session** (issue comments on
satijalab/seurat are outside this session's GitHub scope); it must be read before
anything is filed, since it may state that the behaviour is intended. Related closed
issues: #9426 ("v5 FindAllMarkers avg_log2FC values diverge from Wilcoxon results"),
#9443, #9748, #9854, #6773, #5542.

**Fix shape.** Keep the intended small pseudocount but make it the same for both
groups, e.g. in `FoldChange.Assay`/`.SCTAssay` (lines 1119–1145, 1197–1212) define
`n.total <- length(cells.1) + length(cells.2)` and use
`log(rowMeans(expm1(x)) + pseudocount.use / n.total, base = base)` for both groups.
This is a one-line change per mean function that removes the group-size term
exactly, leaves the v5 scale (pseudocount ≈ 1/n) intact, and changes every
`avg_log2FC` in v5 output, so per the project's contribution norms it needs an issue
and a `pbmc_small` reproduction first, not a cold PR — and it should not be filed at
all if #9346's closure says the current behaviour is intended, in which case the ask
is a documentation and NEWS entry (roxygen line 674 is wrong as it stands).

### SE2 — NOTE (design, documented): Bonferroni denominator is all assay features

`FindMarkers.default` line 664 adjusts with `n = nrow(object)`, the full feature count
of the assay, not the number of genes actually tested after `min.pct` and
`logfc.threshold` — and regardless of a user-supplied `features` vector. Conservative
by construction; the docs say so. Recorded because users comparing `p_val_adj` to a
hand-made Bonferroni over the returned rows (issue #7759) find large differences.

### SE3 — NOTE: `FoldChange.Assay` with a non-LogNormalize `norm.method` takes the log of the mean of already-log (CLR) values

Lines 1130–1140: when the assay's recorded normalization is anything but
`LogNormalize`, the `data` slot goes through `counts.mean.fxn`, i.e.
`log2((Σx + 1)/n)`. For `RC` (relative counts) that is right. For `CLR` (Seurat's ADT
normalization, `log1p(x / geometric mean)`), the "fold change" becomes the log2 of a
mean of log-ratios, with the same `1/n` term as SE1. It is a monotone-ish summary but
not a fold change of protein abundance, and it is what CITE-seq marker tables report
(5 cohort papers name CLR/ADT in the cached evidence). Added in #7115 (5.0.0) with the
NEWS wording "support all normalization approaches". Documentation-level.

### SE4 — NOTE: `GLMDETest` drops genes silently when `glm.nb` fails

Lines 1663–1745: the negbinom path initialises `p.estimate <- 2`, wraps `glm.nb` in
`try(silent = TRUE)`, and afterwards removes every gene whose sentinel is still 2
(lines 1740–1744). Genes whose NB fit fails to converge vanish from the output with no
message; the only warnings are for the explicit skip conditions. Papers using
`test.use = "negbinom"` (1 cohort paper names a non-default test in the cached
evidence) can lose genes without knowing. Poisson has no `try`, so a failure there
errors loudly. Low exposure.

### SE5 — NOTE: `FindConservedMarkers` default meta-p is Tippett's minimum

Line 269 `meta.method = metap::minimump`: the combined p is `1 − (1 − min p)^k`, a test
of "DE in at least one group", while the function's name and documentation promise
markers conserved *across* groups. `max_pval` is also returned and is the conservative
statistic for that reading; the table is sorted by the minimum-p column. Users who
take the sort order as the "conserved" ranking get the union, not the intersection.
The gene set itself is the intersection of genes passing the prefilter in every group
(line 390), which partly rescues the intent. Design, not a defect.

### SE6 — NOTE: `PrepSCTFindMarkers` skip condition vs `FindMarkers.SCTAssay` check

`PrepSCTFindMarkers` (line 2222) skips re-correction when every model's stored median
UMI is *greater than* the current minimum observed median (after subsetting cells),
while `FindMarkers.SCTAssay` (lines 803–806) errors when any model median differs
from that minimum, telling the user to run `PrepSCTFindMarkers()`. On a subset object
the two conditions can both hold, producing the loop reported in open issue #9130
(8 comments). The documented way out is `recorrect_umi = FALSE`; the numbers are not
wrong, the workflow is. Out of numerical scope.

## What held up (verified, not just read)

- **Wilcoxon paths agree.** presto's p-value (`presto/R/utils.R:41-57`) ported verbatim
  matches scipy's asymptotic Mann–Whitney with continuity and tie correction to 1e-15
  on sparse single-cell-like data (80 vs 1,200 cells, 300 genes), with identical calls at
  0.05; this is the same normal approximation `stats::wilcox.test` uses whenever ties are
  present (always, for count data). presto reports p = 1 for all-zero features
  (`z[!is.finite(z)] <- 0`). Seurat's `res[1:(nrow(res)/2), ]` takes the rows for the
  first factor level, `Group1` = `cells.1` (`presto/R/utils.R:19-20`:
  `rep(groups, each = nfeatures)`); the two-sided p is the same for either group in any
  case. `../verify/heldup_wilcoxon_paths.py`. Near `min.cells.group = 3` with no ties the
  approximation differs from the exact test by up to 0.04 — inherent to all three paths.
- **`overflow.check`** (line 2509) only disables the limma path when `ncells²` overflows a
  32-bit integer (> 46,340 cells); the fallback is `wilcox.test`, slower but the same
  approximation.
- **MAST p-value extraction by column position.** `MASTDETest` line 1974 takes column 4
  of `summary(zlm)$datatable` for `component == "H"`. In MAST (`R/ZlmFit.R:264-274`) the
  datatable is `merge(llrt, dt)` keyed on `primerid, component, contrast`, so column 4 is
  `Pr(>Chisq)`. Correct today; fragile by construction.
- **bimod LRT** (`bimodLikData`, `DifferentialLRT`, lines 1401–1422, 1531–1538): two
  parameters (mixing weight, normal mean) plus a shared-by-formula SD per group versus
  the pooled fit, `df = 3`, matching McDavid 2013 as implemented since Seurat 1. The
  1e-5 clamp on the mixing weight and `sd = 1` for a single positive cell are the
  documented guards.
- **Ordering and `only.pos`.** `de.results[, 2]` is the fold-change column in every
  method's output layout (p_val first, then `fc.results`); `FindAllMarkers` filters on
  column 2 after `rbind`, consistent. `return.thresh = 0.01` on raw `p_val` is documented.
- **`min.pct` on rounded percentages** (lines 1081–1086: `round(..., 3)`): a gene at 0.0095
  passes a 0.01 cutoff. Immaterial.
- **DESeq2 path** (lines 1479–1508): `fitType = "local"`, Wald, `contrast = c("group",
  "Group1", "Group2")`; the "no prefilter" promise in the docs is honoured for the fold
  change and `min.diff.pct` but `min.pct` still applies (lines 573–581), exactly as the
  roxygen states.
- **`FindMarkers.Seurat` normalization lookup** (lines 1027–1043) reads the recorded
  `NormalizeData` command, else the integration command, else `NULL` → slot-based
  default, so a LogNormalize'd object with no command log still gets the `expm1` mean.

## Not audited here

`sctransform::correct_counts` (called by `PrepSCTFindMarkers`), `presto`'s AUC and
rank machinery beyond the p-value, `MAST::zlm` internals, `limma::
rankSumTestWithCorrelation` (source unreachable this session), and the BPCells
`marker_features` path.
