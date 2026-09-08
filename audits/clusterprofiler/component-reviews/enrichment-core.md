# Component: clusterProfiler enrichment core, its engine `enrichit`, and `fgsea`

Audited commits (all cloned from GitHub, default branch named in brackets):

| package | commit | date | version string | role |
|---|---|---|---|---|
| `YuLab-SMU/clusterProfiler` [`devel`] | `93835a3` | 2026-08-14 | 4.21.1.003 (DESCRIPTION says 4.21.1.002) | wrappers: `enricher`/`enrichGO`/`enrichKEGG`, `GSEA`/`gseGO`/`gseKEGG`, `simplify`, `compareCluster`, GO data assembly |
| `YuLab-SMU/enrichit` [`devel`] | `a261244` | 2026-08-14 | 0.2.2 | **the numbers**: hypergeometric ORA, GSEA (multilevel port of fgsea, plus `sample`/`permute`/adaptive permutation methods), leading edge, q-values, result filtering. clusterProfiler has delegated to it since 4.19.3 (2025-12-07) |
| `YuLab-SMU/DOSE` at `53d1a8d` | 2024-04-30 | 3.30.0 (Bioconductor 3.19) | the legacy engine (`enricher_internal`, `GSEA_fgsea`, `GSEA_DOSE`, `leading_edge`) behind every clusterProfiler version the cohort names (3.14–4.18); DOSE `devel` (`df6e838`, 4.7.2) now delegates to enrichit too |
| `ctlab/fgsea` [`master`] (development now at `alserglab/fgsea`) | `d466383` | 2026-06-27 | 1.39.4 | GSEA engine of clusterProfiler ≤ 4.18 and of the 122 cohort papers that name fgsea directly |
| CRAN mirror `cran/enrichit` | tags 0.0.8 … 0.2.1 | 2025-12-22 … 2026-08-04 | | what a Bioconductor 3.23 user actually runs under clusterProfiler 4.20.0 (`d67d9f6`, 2026-04-28, `Imports: enrichit (>= 0.1.1)`) |

Read in full: `enrichit` `R/ora.R`, `R/ora_gson.R`, `R/gsea.R`, `R/gseaScores.R`, `R/utilities.R`,
`R/setReadable.R`, `R/accessor.R`, `src/enrichit.cpp`, `src/gsea.cpp`, `src/gsea_scores.cpp`,
`src/esCalculation.cpp`, `src/gsea_multilevel.cpp`, `src/gsea_multilevel_util.cpp`;
`clusterProfiler` `R/enricher.R`, `R/enrichGO.R`, `R/enrichKEGG.R` (wrapper part), `R/gseAnalyzer.R`,
`R/simplify.R`, `R/compareCluster.R`, `R/go-utilities.R`, `R/gofilter.R`, `R/utilities.R`;
`DOSE` 3.30.0 `R/enricher_internal.R`, `R/gsea.R`; `fgsea` `R/fgsea.R`, `R/fgseaMultilevel.R`,
`R/util.R`, `R/fgseaORA.R`, `src/esCalculation.*`, `src/fastGSEA.cpp`, `src/fgseaMultilevel.cpp`,
`src/fgseaMultilevelSupplement.cpp`, `src/util.cpp`, `inst/exact/`.

**Everything was executed on the shipped code** (R 4.3.3): fgsea master, enrichit `a261244` and the
CRAN releases 0.1.4 / 0.2.0 / 0.2.1 (each built into its own library), clusterProfiler `devel`
built against enrichit 0.2.2, clusterProfiler 4.12.0 (`1866584`) built against DOSE 3.30.0, plus
GOSemSim `e6caf6d`, gson 0.2.1, yulab.utils 0.2.5, HDO.db 0.99.1 from their GitHub clones and GO.db /
org.Hs.eg.db 3.18.0, qvalue 2.34.0, AnnotationDbi 1.64.1 from apt. Two non-numeric imports could
not be built here (`enrichplot`, a plotting package with a deep ggplot dependency tree, and `aisdk`,
the LLM client); they were replaced by stub packages that export the seven names clusterProfiler
imports from each (every stub function stops when called) plus the one accessor clusterProfiler
fetches from enrichplot at load time, `as.data.frame.compareClusterResult`, copied verbatim from
`enrichplot-src/R/data_utils.R:372-374`. No computing code was stubbed. References: scipy
`hypergeom`, an independent numpy GSEA (`../verify/ref_gsea.py`, written from Subramanian et al.
2005 and the GSEA user guide) and exact enumeration of the gene-set permutation null on lists of
24–40 genes. Harnesses and captured output in `../verify/`.

Cohort exposure numbers are lower bounds from the survey cache (`../README.md`).

## Findings

### CP1 — CONFIRMED on the current Bioconductor release (clusterProfiler 4.20.0 with CRAN enrichit 0.1.4–0.2.1); fixed on `devel` (enrichit 0.2.2, not yet on CRAN): `GSEA()`/`gseGO()`/`gseKEGG()` report every gene set with raw p ≤ `pvalueCutoff`, whatever its `p.adjust`

**Code.** enrichit 0.2.1 (CRAN, `06bba24`) `R/gsea.R:352-354`:

```r
    # Filter by pvalueCutoff
    if (!is.null(pvalueCutoff)) {
        gsea_res <- gsea_res[!is.na(gsea_res$pvalue) & gsea_res$pvalue <= pvalueCutoff, ]
```

The same single filter is at 0.1.4 `R/gsea.R:300-302`. The legacy engine filtered on both the raw and
the adjusted p (DOSE 3.30.0 `R/gsea.R:89-90` and, for its own permutation path, `:325-326`), and so
does enrichit 0.2.2 (`R/gsea.R:377-378`, commit `a261244`, NEWS: "previously only the raw p-value
was filtered"). `pvalueCutoff` is documented by clusterProfiler as an adjusted-p cutoff and the
result table is what the package's book presents as the enriched terms. The Bioconductor 3.23
release, clusterProfiler 4.20.0 (`d67d9f6`, 2026-04-28), requires only `enrichit (>= 0.1.1)`; the
`cran/enrichit` mirror lists 0.2.1 (2026-08-04) as the latest CRAN release on 2026-09-08, so every
current release install carries the raw-p filter.

**Verified.** `../verify/go_realdata.out` (GO BP from org.Hs.eg.db, 6,379 terms of size 10–500 over
18,870 genes; a ranked list of all annotated genes with 5 terms planted up and 5 down):

| engine | result-table rows | rows with p.adjust > 0.05 | max p.adjust | pure-null list: rows |
|---|---|---|---|---|
| enrichit 0.1.4 (CRAN 2026-04-08) | 717 | 515 | 0.444 | 292 |
| enrichit 0.2.1 (CRAN 2026-08-04) | 718 | 514 | 0.444 | 292 |
| enrichit 0.2.2 (`devel`) | 204 | 0 | 0.049 | 0 |

On the synthetic list of `../verify/enrichit_release_scope.out` (34 sets, 2 planted) 0.1.4, 0.2.0 and
0.2.1 return 4 rows of which 2 have p.adjust 0.30–0.37; 0.2.2 returns the 2 planted sets. The
minimal reproduction (`../upstream/mcve_cp1_gsea_table_rawp.R`, pure noise, 400 sets) gives 14 rows
with p.adjust up to 0.965 under clusterProfiler `devel` + enrichit 0.2.1 and 0 rows under 0.2.2
(`../upstream/mcve_outputs.txt`).

**Version scope, by execution.** Affected: enrichit 0.1.4, 0.2.0, 0.2.1, i.e. clusterProfiler
4.19.3 … 4.21.1.002 including the release 4.20.x. Unaffected: enrichit 0.2.2 (`devel`), and DOSE
3.30.0 (every cohort version). No cohort paper names a version ≥ 4.19, so this is a defect of the
current release, not of the published record. Upstream fixed and announced it (enrichit NEWS 0.2.2,
clusterProfiler NEWS 4.21.1.003); only a CRAN release is missing. Tier: **held** — nothing to file
per README step 4; the heads-up text in `../upstream/issue-cp1-gsea-table-rawp.md` is for use only if
0.2.2 has not reached CRAN by the next Bioconductor release.

### CP2 — CONFIRMED on every legacy version (DOSE `leading_edge()` since 2016-07-04, i.e. clusterProfiler ≤ 4.18 — all cohort versions); fixed on `devel` by the engine change: the leading edge of a negative-ES gene set is taken from the wrong peak, so `core_enrichment` lists extra genes

**Code.** DOSE 3.30.0 `R/gsea.R:371-396`:

```r
leading_edge <- function(observed_info) {
    core_enrichment <- lapply(observed_info, function(x) {
        runningES <- x$runningES
        runningES <- runningES[runningES$position == 1,]     # hits only
        ES <- x$ES
        if (ES >= 0) {
            i <- which.max(runningES$runningScore)
            leading_gene <- runningES$gene[1:i]
        } else {
            i <- which.min(runningES$runningScore)          # minimum over POST-hit scores
            leading_gene <- runningES$gene[-c(1:(i-1))]
```

For a positive ES the running-sum maximum is always reached at a hit, so restricting to hits is
harmless. For a negative ES the minimum is always reached just *before* a hit (the sum only rises at
hits); the minimum over post-hit scores is a different point whenever an earlier hit's post-hit
score undercuts the post-hit score that follows the true minimum. GSEA defines the leading edge of a
negative set as the members at or after the peak of the running sum (user guide; Subramanian et al.
2005). The `tags` fraction at `:398-410` uses the same rule; `rank` (`:386-396`) uses the full running
sum and is right. The rule was introduced in DOSE commit `1dc19e9` (2016-07-04) and removed when
DOSE/clusterProfiler moved to enrichit (2025-12-05, `4a1d02d`). enrichit's `gsea_leading_edge_details`
(`R/utilities.R:104-178`, `which.min` over the full running sum at `:133`, members `peak_idx:N` at
`:158`) and its C++ `calculate_es_details` (`src/gsea.cpp:57-100`) use the global peak; fgsea's
`calcGseaStat` takes `which.min(bottoms)`, the pre-hit values (`R/fgsea.R:170,175`).

**Verified.** `../verify/gsea_vs_reference.out`: on 34 sets, fgsea, enrichit (all methods) and
`clusterProfiler::GSEA` on `devel` reproduce the reference leading edge 34/34; DOSE 3.30.0 (both
its fgsea-backed and its own permutation path) 32/34 — the two misses are negative sets (R10: 50
genes listed, reference 34; DUP: 5 vs 4), all extra genes lie before the true peak.
`../verify/legacy_leading_edge.out` (15,000 genes, 600 sets of 15–500 genes, 300 planted down):
143/143 positive sets right; 28 of 457 negative sets (6.1 %) differ — DOSE lists 1–31 extra genes
(median 4; median +12 % of the reference leading edge, up to +225 %), never misses one, and the
`rank` column is right for all 600. Through the wrapper, `clusterProfiler 4.12.0::GSEA()` on set R092
returns 74 `core_enrichment` genes where the reference has 43 (enrichit `devel`: 43).

**Who is exposed.** Every `core_enrichment`/`leading_edge` string for a suppressed pathway written by
clusterProfiler 3.14–4.18 (the versions the cohort pins: 4.10.1, 4.6.2, 3.14.3, 4.2.2, 4.0.5 …) is
wrong in about one negative set in sixteen; NES, p and p.adjust are untouched. Fixed on `devel`
without an announcement (the NEWS for 4.19.3 says only "use 'enrichit' as engine"). Tier: **held** —
no wrong number at master; recorded for readers of older results.

### CP3 — CONFIRMED on every legacy version (DOSE `enricher_internal` since 2015-12-20); fixed on `devel` by the engine change: query genes outside a user-supplied `universe` were still counted as draws, and terms hit only by them were tested with `Count = 0`

**Code.** DOSE 3.30.0 `R/enricher_internal.R:66,74,106`:

```r
                extID <- intersect(extID, universe)                  # N restricted to the universe
    qTermID2ExtID <- lapply(qTermID2ExtID, intersect, extID)          # k restricted
    n <- rep(length(qExtID2TermID), length(M))                       # n = query genes with ANY annotation
```

`n` counts every query gene that has an annotation, whether or not it is in the universe, so the
hypergeometric draws exceed the balls that can be white; the term list `qTermID` is built before the
restriction, so a term whose only query genes lie outside the universe is tested with `k = 0`.
enrichit computes `K` as `|query ∩ universe|` inside `src/enrichit.cpp:41-46` and drops `Count = 0`
rows (`R/ora_gson.R:98`).

**Verified.** `../verify/ora_vs_scipy.out` (synthetic annotation, 75 of 194 annotated query genes
outside a 2,000-gene user universe): DOSE `n = 194` vs enrichit `n = 119`, 263 vs 245 terms tested,
max p difference 0.842; with the default universe the two engines agree to 0 and both equal scipy.
`../verify/go_realdata.out` (GO BP, 12,000-gene user universe, 20 of 200 query genes outside it):
DOSE `n = 200` vs 180, 25 terms tested with `Count = 0`, p-values larger by a median factor 1.212, 939
vs 1,130 terms at p.adjust ≤ 0.05 and 191 terms whose call differs. The common case — the query is a
subset of the background — is unaffected. Tier: **held** (legacy only).

### CP4 — CONFIRMED at `devel` and on every enrichit release, non-default path: `gsea(method = "sample" | "permute")` and `adaptive = TRUE` divide by all permutations, so their p-values are about half of the GSEA-convention p that `multilevel`, fgsea and DOSE report

**Code.** enrichit `src/gsea.cpp:329-339`:

```cpp
        for (int p = 0; p < nPerm; ++p) {
            double pes = perm_es[i][p];
            if (obs_es > 0) {
                if (pes >= obs_es) count_better++;
                ...
        pvalues[i] = (double)(count_better + 1) / (double)(nPerm + 1);
```

and identically at `:517,536` for the adaptive path. The GSEA nominal p (Subramanian et al. 2005)
is the fraction of *same-sign* permutation scores at least as extreme; fgsea divides by
`1 + nGeZero` (`R/fgsea.R:700`), DOSE 3.30.0 by `sum(permScores >= 0) + 1` (`R/gsea.R:291`), and
enrichit's own multilevel path by `denomProb` (`src/gsea_multilevel.cpp:629,700`). A second, smaller
defect on the `sample` path: the observed ES is computed by `calculate_es_details` (dense loop) and
the permutations by `calculate_es_sparse` (block arithmetic); for a set lying entirely at one end of
the list (ES = ±1) the two roundings differ and no permutation is ever counted.

**Verified.** `../verify/gsea_exact_small.out` (exact enumeration of all C(24,3) = 2,024, C(40,4) =
91,390 and C(30,5) = 142,506 gene sets; 14 hand-picked sets): ratio of engine p to the exact
same-sign p — fgsea multilevel median 1.052 (0.995–1.313, mean of 40 runs), enrichit multilevel
1.036 (0.990–1.247), fgseaSimple 0.999, DOSE permutation 1.030; **enrichit `sample` 0.498
(0.005–1.214), `permute` 0.593, adaptive 0.496**; the `sample` p matches the *unconditional*
P(ES* ≥ ES) instead (median ratio 0.965). The three sets with ES = −1 get p = 5e-6 = 1/(nPerm + 1)
from `sample` where the exact value is 5e-4 to 1.5e-5. On the 2,000-gene list of
`../verify/gsea_vs_reference.out` a random set has p = 0.964 (fgsea), 0.965 (enrichit multilevel)
and 0.546 (`sample`) / 0.551 (`permute`). Identical on enrichit 0.1.4, 0.2.0, 0.2.1 and 0.2.2
(`sample p = 0.4458`, `permute` 0.4479 for the exact 0.8824 in each; `../verify/cp4_versions.out`), and
0.8791 / 0.8925 with the patch.

**Who is exposed.** Only callers of `GSEA()`/`gseGO()`/`gseKEGG()` with `method = "sample"`,
`"permute"` or `adaptive = TRUE` (clusterProfiler ≥ 4.19.3); the default `multilevel` is right. The
`nPerm` argument that older scripts pass is only honoured on these paths. No cohort paper can be
exposed (all pin ≤ 4.18). Tier: **held** (rare-option path). Fix and test in
`../upstream/0001-Condition-sample-permute-adaptive-GSEA-p-values-on-t.patch`: same-sign
denominators and the observed ES compared through the sparse routine; the new test fails on
unmodified `devel` (5 expectations) and the full enrichit suite passes with it (37 tests).

### CP5 — CONFIRMED on the release-era engine enrichit 0.1.4–0.1.5 (CRAN 2026-04-08 … 2026-06-30, i.e. clusterProfiler 4.19.3–4.20.0 as installed in spring 2026); fixed in enrichit 0.2.0 (CRAN 2026-07-01): ORA adjusted p-values over every gene set in the size window, including sets with no query gene

**Code.** enrichit 0.1.4 `R/ora_gson.R:130` runs `p.adjust` over `ora_res` with every set the size
filter kept; 0.2.0 added the `Count > 0` filter (`R/ora_gson.R:98` at `a261244`, NEWS 0.2.0:
"keep `Count = 0` rows out of `p.adjust`/`qvalue` … #821 & #819"). Legacy DOSE tested only terms hit
by at least one query gene (`R/enricher_internal.R:77-96`).

**Verified.** `../verify/go_realdata.out`: 198-gene query on GO BP — enrichit 0.1.4 adjusts over 6,379
terms (2,523 with `Count = 0`) and reports **513** terms at p.adjust ≤ 0.05; 0.2.1/0.2.2 and DOSE
3.30.0 adjust over the 3,856 hit terms and report **694**; the two planted terms' p.adjust move from
1.79e-59 to 1.08e-59. The MCVE (`../upstream/mcve_cp5_ora_zero_overlap_bh.R`) shows 200 rows, 99 with
`Count = 0`, p.adjust 5.22e-16 vs 2.64e-16 under 0.1.4. This is open upstream as issue #819 ("Big
differences in enricher results between clusterProfiler 4.16.0 and clusterProfiler 4.20.0",
2026-05-14, 6 comments unread from here). Tier: **comment** on #819 if the thread does not already
say that enrichit ≥ 0.2.0 restores the count (`../upstream/comment-cp5-issue819.md`).

### CP6 / CP7 — CONFIRMED on the release-era engines, fixed on CRAN: multilevel ranks scaled by a fixed 10^6 (0.1.x: `NaN` for small-magnitude statistics) and gene-set size filtered on the raw set instead of its overlap with the list (0.1.x–0.2.0)

`../verify/enrichit_release_scope.out`: with `stats * 1e-7` (e.g. correlation coefficients on a
small scale) enrichit 0.1.4 returns `ES = NaN, NES = NaN, p = NaN` for the planted set; 0.2.0 onward
(`scale_fgsea_ranks`, `R/gsea.R:256-270`, mirrors fgsea's `prepareStats`) returns ES 0.7536 at
either scale. A set of 520 members of which 480 are in the list is not tested by 0.1.4/0.2.0
(`maxGSSize = 500` applied to 520) and is tested by 0.2.1+ (overlap 480); a set of 16 members with 6
in the list is tested by 0.1.4/0.2.0 with `setSize = 6` and dropped by 0.2.1+ (`R/gsea.R:116`,
clusterProfiler #824). Both change the BH denominator and the tested set. Tier: **held** (fixed,
released).

### CP8 — CONFIRMED at `devel`, design consequence: `simplify()` removes terms that are not similar to any term it keeps

**Code.** clusterProfiler `R/simplify.R:108-128`: for each term *Y* in turn, the cluster is every
term with `similarity > cutoff` to *Y* (`:110`), the representative is the cluster member with the
smallest `p.adjust` (`:117`, ties to the term with more ancestors `:122`), and every other cluster
member goes to `GO_to_remove` (`:127`). A term *X* similar to *Y* is therefore removed when a third
term *Z*, similar to *Y* but not to *X*, ranks better — and *Y* may be removed too.

**Verified.** `../verify/note_simplify.out` (three `enrichGO` runs on GO BP, cutoff 0.7, Wang): of 172
/ 60 / 195 removed terms, 98 / 38 / 113 are redundant with a kept better-ranked term (the documented
case), 66 / 18 / 70 have a better similar term that was itself removed, and **8 / 4 / 12 are similar
to no kept term at all** — including terms ranked 8th and 20th by `p.adjust` in their runs. The kept
set is a valid independent set (0 pairs above the cutoff), p-values are unchanged, and
`../verify/heldup_wrappers.out` confirms the mechanics. Whether an "orphan" removal is acceptable is
the maintainer's call (the function is documented as "removing redundancy"; a rule that only removes
a term in favour of a kept term it is similar to would keep those 4–8 %). Tier: **held** (design
question; no patch).

### Notes (design, documentation, cosmetic)

- **N1 — q-value policy changed with the engine.** DOSE always called `qvalue(p, lambda = 0.05,
  pi0.method = "bootstrap")` (`R/enricher_internal.R:134`); enrichit tries `qvalue(p)` (smoother,
  λ = 0.05 … 0.95) first and falls back to the legacy call (`R/utilities.R:54-62`, since 0.1.1,
  `c1db09b`). The `qvalue` column feeds `qvalueCutoff = 0.2` (`get_enriched`, `R/utilities.R:215`).
  On the synthetic ORA the two differ by up to 0.179 (`../verify/ora_vs_scipy.out`); on the GO BP
  example the smoother fails and the fallback reproduces the legacy column exactly (0 terms crossing
  0.2, `../verify/go_realdata.out`). Data-dependent, undocumented.
- **N2 — documentation drift on `method`.** `GSEA()`'s help (`R/enricher.R:92`) lists `"multilevel",
  "monte carlo", "fgsea"`; enrichit accepts `sample | permute | multilevel`, so the two documented
  names error (`../verify/heldup_wrappers.out`). The ≤ 4.18 argument `by = "fgsea"` errors with
  "unused argument". Loud, not wrong.
- **N3 — `leading_edge` string rounding.** The C++ paths use `std::round` (half away from zero,
  `src/gsea.cpp:355,554`); R and the multilevel path use R's `round` (half to even): one of 34 strings
  differs (`list=19%` vs `18%` at 18.5, `../verify/gsea_vs_reference.out`). Cosmetic.
- **N4 — legacy `by = "DOSE"` path crashes on equal-sized sets.** DOSE 3.30.0 `geneSet_filter` uses
  `sapply` (`R/gsea.R:539`), which returns a matrix when every set has the same size after
  intersection (including a single set), and the analysis fails with "arguments imply differing
  number of rows" / returns `NULL` (`../verify/legacy_leading_edge.out`). Legacy, non-default.
- **N5 — `eps` in enrichit's multilevel path is not scaled by the sign fraction** (by reading only).
  fgsea passes `eps * min(denomProb)` to the C++ ruler (`R/fgseaMultilevel.R:290`) because the final
  p is `cppMPval / denomProb`; enrichit passes `eps` itself (`src/gsea_multilevel.cpp:685`) and then
  floors the final p at `eps` (`:704-706`). Only p-values between `eps` and `eps / denomProb` (about
  2 × `eps`) can be truncated. Default `eps = 1e-10` in clusterProfiler; fgsea's own default is
  1e-50 (`R/fgseaMultilevel.R:49`) while its README still says 1e-10 (`README.md:62`).
- **N6 — ties.** Both engines warn and keep tied genes in input order; ES then equals the reference
  computed on that order (0.413989 in all three, `../verify/gsea_vs_reference.out`). Documented
  design (fgsea issue #18 is the open discussion).
- **N7 — GSEA is not reproducible without a seed.** `seed = FALSE` (default) draws from R's RNG
  (`R/gsea.R:110`); two calls give p = 1.2e-19 and 1.8e-19 for the same set, `seed = 7` or a prior
  `set.seed()` fixes it (`../verify/gsea_vs_reference.out`). Documented since 4.21.1.003; the
  4.19.3–4.21.1.002 wrappers had no `seed` argument (`d67d9f6` `R/gseAnalyzer.R`), `set.seed()` still
  worked.
- **N8 — `enrichGO` with `keyType != "ENTREZID"`** maps the query (and universe) to Entrez ids first
  (`R/enrichGO.R:62-99`, #805). A one-to-many symbol would count once per id; org.Hs.eg.db 3.18.0
  has no such symbol among the 18,870 BP-annotated genes, and the SYMBOL and ENTREZID runs give
  identical p-values (`../verify/heldup_wrappers.out`). Organism-dependent; no effect for human.

### Withdrawn (own suspicions killed by execution)

- **W1** — that fgsea's 2025 switch to integer-scaled weights (`R/fgsea.R:72`) changes reported ES
  materially: max |ES − reference| is 8.99e-8 at `gseaParam = 1` and 1.87e-7 at 2, with unchanged
  leading edges and sizes (`../verify/gsea_vs_reference.out`); the exact-enumeration p ratios above
  show the multilevel estimator itself is unbiased within its stated error.
- **W2** — that enrichit's `BH` might run over the zero-overlap sets at `devel`: it does not
  (`Count > 0` filter, 0 such rows in every run); the release-era behaviour is CP5.
- **W3** — that `compareCluster` adjusts p across clusters: it runs the wrapper per cluster and
  binds the `as.data.frame` results (`R/compareCluster.R:154-160`), identical to the single calls
  (`../verify/heldup_wrappers.out`).

## What held up (executed, not just read)

- **Hypergeometric ORA** (enrichit `devel`, and DOSE 3.30.0 with the default universe): p equals
  `scipy.stats.hypergeom.sf(k−1, N, M, n)` to 1.1e-15 with N = all annotated genes (∩ user universe),
  M = term ∩ universe, n = query ∩ universe, k = overlap; `BgRatio`, `GeneRatio`, `Count`,
  `RichFactor`, `FoldEnrichment` equal their definitions; `zScore` equals (k − μ)/√Var to 2.5e-14
  with the hypergeometric variance; BH over the tested (hit, size-windowed) terms to 2.8e-15;
  `minGSSize`/`maxGSSize` applied to the intersected sizes; the `as.data.frame` view applies
  p ≤ cutoff, p.adjust ≤ cutoff and qvalue ≤ `qvalueCutoff` as documented (`../verify/ora_vs_scipy.out`).
  `enrichGO(ENTREZID)` equals the engine on the same GSON; the default universe is the set of genes
  with any annotation in the sub-ontology (18,870 for human BP); `compareCluster` = per-cluster
  wrapper; `setReadable` maps ids in order and leaves the numbers untouched
  (`../verify/heldup_wrappers.out`).
- **GSEA enrichment score, leading edge and set handling** (fgsea `fgseaSimple`/`fgseaMultilevel`,
  enrichit multilevel/sample/permute, `clusterProfiler::GSEA`, DOSE 3.30.0): ES equals the numpy
  reference at `gseaParam`/`exponent` 0, 1, 2 (≤ 1.9e-7 on the integer-scaled paths, ≤ 2.4e-14 on
  the double paths); members absent from the ranked list are dropped and `size`/`setSize` is the
  overlap (12 of 20; duplicates collapse to 15); sets below `minGSSize` or above `maxGSSize` after
  intersection are not tested; leading edge, `rank`, and the `tags/list/signal` string equal the
  GSEA definitions on all 34 sets for fgsea and enrichit; `scoreType = "pos"` returns the maximum of
  the running sum with the leading edge from the top (`../verify/gsea_vs_reference.out`).
- **GSEA p-values and NES** against exact enumeration: fgsea multilevel and enrichit multilevel
  p-values are within their `log2err` of the exact same-sign probability (ratios 0.99–1.31, mean of
  40 runs), fgseaSimple median ratio 0.999, DOSE's own permutation 1.030 down to its resolution;
  NES from all engines agree with ES / mean(same-sign exact null ES) to the second decimal
  (`../verify/gsea_exact_small.out`); fgsea, enrichit multilevel and DOSE-via-fgsea give the same
  p (6e-20 / 2e-19 / 1e-19) and NES (2.97–3.01) for the planted set on the 2,000-gene list.
- **`eps`**: p < eps → eps with `log2err = NA` and a warning (both engines, `R/fgseaMultilevel.R:239`,
  `src/gsea_multilevel.cpp:704-706`).
- **fgsea's own tests**: 49 tests in the stat/multilevel/analysis/fora/pathways files pass on the
  master build (1 skipped: `reactome.db` not installed); clusterProfiler's `test-gsea-params`,
  `test-enrichGO`, `test-compareCluster`, `test-bitr`: 9 tests pass on `devel`.

## Not audited

`enrichKEGG`/`gseKEGG` data retrieval (KEGG REST is unreachable here; the statistics are the same
`ora_gson`/`gsea_gson` calls), `enrichWP`, `enrichDAVID`, `enrichPC`, the network-based `nseGO`/
`mnseGO` family and Bayesian `bayes_enrich` (new in 2026, no cohort exposure), `groupGO`, weighted
ORA/GSEA (`weight =`, BiasedUrn), `fgseaLabel`, `collapsePathways`/`collapsePathwaysORA`, GESECA,
`geneSim`/`clusterSim`, all plotting (`enrichplot`), and `interpret()` (LLM).
