# Seurat audit against 767 published papers (2021–2026)

_Tenth audit in the series. Profiling pass generated 2026-09-02; component reviews
not yet started._

## What this is

The six-journal survey found **767 papers** in *Nature* (377), PNAS (304), *Cell* (59)
and *Science* (27), 2021–2026, that used Seurat — the largest cohort of any package in
this repository after DESeq2, and growing every year (58 papers in 2021, 216 in 2025).
Seurat (`satijalab/seurat`; R with C++ for the graph clustering) is the dominant
toolkit for single-cell RNA-seq: QC filtering, normalisation, variable-feature
selection, PCA/UMAP, graph clustering, batch integration, differential expression
(cluster markers), module scoring and reference mapping. Nearly every number in a
single-cell paper — cluster count, marker gene lists and their fold changes and
adjusted p-values, module scores, cell-type proportions after integration — passes
through it.

Source under audit: `satijalab/seurat` `main` @ `084d9e4` (2026-08-28, version
5.5.1.9003), with tags `v3.2.2`, `v4.0.0`–`v4.4.0`, `v5.0.0`–`v5.5.1` available for
version dating. The papers pin v4 most (4.3.0, 4.1.0, 4.1.1), v3 in the early years, v5
from 2025 on; the audit therefore has to read each code path across the v3 → v4 → v5
lineage, not just `main`.

## Profiling pass: what was possible from this session

The other audits' profiling scripts re-mine each paper's full text from Europe PMC.
**This session had no route to Europe PMC** (`www.ebi.ac.uk` is denied by the
execution environment's egress policy; NCBI's E-utilities and PMC OA endpoints are
denied too). `seurat_profile.py` keeps the same fetch path as the other scripts and
falls back, per paper, to the survey's stored evidence: the Seurat evidence sentence
from `paper_software.tsv` plus every per-package evidence snippet the survey kept for
that paper in `pipelines.jsonl.gz`. That is a few hundred characters per package, not
the methods section, so **every feature count below is a lower bound on usage**, and
the parameter counts (resolutions, thresholds) are small samples. Each record in
`seurat_profiles.jsonl` carries `"source": "survey_cache"`; rerunning
`python3 seurat_profile.py` from a host with Europe PMC access replaces them with
`"source": "fulltext"` records and the counts should be rebuilt from those. The
`--offline` flag reproduces the cache-only run.

Version strings are the exception: the survey extracted them from the full text at
harvest time, so `version_survey` is complete for the 298 papers that stated one, and
the regex over the cached evidence adds 41 more.

## How the papers use Seurat (lower bounds; see above)

**Version lineage** (339 papers state a version; 428 do not):

| family | papers | by year |
|---|---|---|
| v5 | 61 | 2023: 1, 2024: 5, 2025: 32, 2026: 23 |
| v4 | 203 | 2021: 2, 2022: 19, 2023: 43, 2024: 62, 2025: 54, 2026: 23 |
| v3 | 70 | 2021: 25, 2022: 18, 2023: 12, 2024: 8, 2025: 5, 2026: 2 |
| v2 | 6 | 2021–2022, one 2025 |

Most-pinned releases: 4.3.0 (42), 4.1.0 (26), 5.1.0 (22), 4.1.1 (20), 5.0.1 (13),
3.2.2 (13), 4.0.3 (12), 4.0.4 (11). One paper's "1.9.0" is a Scanpy version the survey
attached to Seurat and is ignored.

**Code paths named in the cached evidence** (papers):

| stage | signal | papers |
|---|---|---|
| reduction | UMAP / RunUMAP | 628 |
| QC | doublet removal (DoubletFinder 72, Scrublet 53, scDblFinder 29) | 160 |
| QC | PercentageFeatureSet / mitochondrial fraction | 44 (16 state the cutoff: 5 % ×7, 10 % ×6, 15–25 % ×7) |
| QC | SoupX / CellBender ambient RNA | 40 |
| normalisation | SCTransform | 33 (v2/glmGamPoi named: 5) |
| normalisation | NormalizeData / LogNormalize | 23 |
| clustering | resolution stated | 40 (0.5 ×11, 0.6 ×6, 0.2 ×6, 0.8 ×4) |
| clustering | Louvain / Leiden named | 37 / 22 |
| clustering | FindNeighbors / FindClusters | 30 / 21 |
| reduction | PCs stated | 30 (20 ×23, 30 ×20, 50 ×16, 15 ×9) |
| integration | Harmony | 52 |
| integration | CCA / anchor integration (v3/v4) | 19 (RPCA: 3; IntegrateLayers v5: 2) |
| integration | fastMNN via SeuratWrappers | 8 |
| DE | adjusted p / p_val_adj | 56 (cutoff 0.05 ×36) |
| DE | pseudobulk (AggregateExpression etc.) | 32 |
| DE | Wilcoxon named / MAST named | 24 / 6 |
| DE | FindMarkers / FindAllMarkers | 21 / 8 |
| DE | log fold change reported | 18 (thresholds: 2 ×5, 1.5 ×4, 1 ×4, 0.5 ×3, 0.25 ×1) |
| scoring | AddModuleScore | 16 |
| scoring | CellCycleScoring | 4 |
| multimodal | Signac / ATAC | 80; WNN 10; spatial (Visium etc.) 14 |
| downstream | Monocle / trajectory tools | 152 |
| downstream | CellChat / ligand–receptor tools | 77 |
| downstream | SCENIC | 56 |
| also | Scanpy in the same paper | 102 |

Companion packages in the same papers (from the survey's per-paper package lists,
complete): UMAP 627, DESeq2 210, GSEA 193, scDblFinder-family doublet tools 150,
MACS2 149, STAR 144, Scanpy 102, edgeR 96, clusterProfiler 93, Monocle 74, limma 67,
fgsea 66, SCENIC 56, Signac 54, CellChat 45, ArchR 42, scVelo 41, Slingshot 41.

Two things already follow. First, the differential-expression path is where the
published numbers are: 210 papers hand Seurat-derived groups or pseudobulks to DESeq2,
193 run GSEA on ranked marker lists, and the cluster-marker tables that define cell
types in nearly every paper come from `FindAllMarkers`. Second, the cohort straddles
the v4 → v5 boundary (2024–2025), and the two lineages compute the log fold change
differently (below), so per-paper version matters for exposure.

## Audit targets, ranked

Read adversarially, in this order, each against the v3/v4/v5 tags the papers pin.
Lines are from `main` @ `084d9e4`.

1. **Differential expression** — `R/differential_expression.R` (2,569 lines).
   `FindMarkers` defaults: `test.use = "wilcox"`, `logfc.threshold = 0.1` (was 0.25
   through v4), `min.pct = 0.01`, Bonferroni on the number of features tested.
   `FoldChange` in v5 computes `log2((Σ expm1(x) + pseudocount) / n)` per group
   (`R/differential_expression.R:810-820`); v4 computed `log2(mean(expm1(x)) +
   pseudocount)`. The pseudocount moved inside the mean, which changes every reported
   `avg_log2FC` for low-expression genes and the set passing `logfc.threshold`. To
   verify: the exact formula in each tag, whether `FindMarkers` pre-filters on the
   *same* fold change it reports, the Wilcoxon path (base `wilcox.test` vs `presto`
   when installed vs the limma `rankSumTestWithCorrelation` used in some versions —
   three tie-handling and continuity conventions), `min.cells.group = 3` behaviour,
   the SCT-assay path (`PrepSCTFindMarkers`, whose multi-model bug was fixed in 5.5.1
   per NEWS), and the `FindConservedMarkers` meta-p combination.
2. **Normalisation and feature selection** — `R/preprocessing.R` (6,207 lines) and
   `R/preprocessing5.R`. `LogNormalize` with `scale.factor = 1e4`; `FindVariableFeatures`
   `vst` (loess span 0.3, standardised-variance clipping at √n) and `mean.var.plot`;
   `ScaleData` regression (`vars.to.regress`) and the `scale.max = 10` clip;
   `PercentageFeatureSet` (a layer-retrieval bug was fixed on `main` in #10438 —
   check which versions it affects); `SCTransform` is a wrapper on the separate
   `sctransform` package and is out of scope beyond the wrapper's argument handling.
3. **Graph clustering** — `R/clustering.R` (1,908 lines), `src/snn.cpp`,
   `src/ModularityOptimizer.cpp` (1,012 lines, a port of the Java Louvain optimiser).
   SNN construction with `prune.SNN = 1/15`, `k.param = 20`; `FindClusters`
   `resolution = 0.8`, `algorithm = 1`, `random.seed = 0`, `n.start = 10`,
   `n.iter = 10`; the modularity formulas (`modularity.fxn` 1 vs 2); Leiden via
   `leidenbase`/`igraph`. Cluster counts are reported in essentially every paper.
4. **Module and cell-cycle scoring** — `AddModuleScore` in `R/utilities.R`:
   24 expression bins, 100 control genes per bin, the `seed`; `CellCycleScoring`
   thresholds; the just-merged fix for `StdAssay` objects (#10448, 2026-08-28) shows
   this code is live. 16 papers name it, 4 name cell-cycle scoring.
5. **Integration** — `R/integration.R` (8,103 lines) and `R/integration5.R`.
   `FindIntegrationAnchors` (CCA/RPCA, `k.anchor = 5`, `k.filter = 200`,
   `k.score = 30`), anchor scoring and the `k.weight = 100` Gaussian weighting in
   `IntegrateData`; `FindTransferAnchors`/`TransferData` prediction scores. Harmony
   is a separate package; only the wrapper is in scope.
6. **Dimensional reduction** — `R/dimensional_reduction.R`: `RunPCA` via `irlba`
   (approximate; `npcs = 50`), `JackStraw` p-values, `RunUMAP` argument passing to
   `uwot` (the `uwot.init` change in 5.5.1).
7. **Sketching (v5)** — `R/sketching.R`: leverage-score sampling and `ProjectData`.
   One cohort paper so far; low priority.

Out of scope: `R/visualization.R` (10,013 lines; plots, not numbers), `mixscape.R`,
`tree.R`, spatial I/O.

## Filing channel (read before anything is sent — step 4 of the method)

- Seurat's README: bug reports and feature requests as GitHub issues; analysis
  questions to Discussions; "PRs are welcome".
- Wiki **Contributor's Guide**: fork, branch `fix/*` from `upstream/main`, regenerate
  roxygen docs, tests encouraged but not mandatory — a PR without tests must include
  a small reproducible example on `pbmc_small` or a `SeuratData` set; request review
  from @rsatija. Maintainers bump the version and write the NEWS entry themselves.
- `.github/pull_request_template.md`: summary, type of change, motivation, tests and
  examples on `pbmc_small`, related issues, checklist (`devtools::document()`,
  `devtools::check()` clean, maintainers may edit).
- `.github/ISSUE_TEMPLATE/bug-report.yml`: check the tracker and `NEWS.md` on `main`
  first; reproducible example on `pbmc_small` required.
- No pinned results-stability policy of the DESeq2 kind was found; NEWS shows
  behaviour-changing fixes are merged routinely. Still: grep NEWS.md and the closed
  issues for every candidate before writing it up.
- Adjacent repositories with their own trackers: `satijalab/seurat-object`,
  `satijalab/sctransform`, `immunogenomics/presto`, `satijalab/azimuth`.

## Files

| file | what |
|---|---|
| `seurat_profile.py` | profiling script; full-text path identical to the other audits, with the survey-cache fallback and `--offline` |
| `seurat_profiles.jsonl` | one record per paper: features, versions, version family, parameters, companion packages, source |
| `profile_run.log` | the 2026-09-02 run (offline) |

## Next steps

1. Rerun `seurat_profile.py` from a host that can reach Europe PMC; rebuild the table
   above from full text (expect DE and QC counts to rise several-fold).
2. Component review 1 (differential expression) across tags v3.2.2, v4.3.0, v5.1.0 and
   `main`; verification by running the shipped package on synthetic counts with known
   group means, as the DESeq2 audit did — R is installable in the sandbox.
3. Reviews 2–4, then exposure join per paper by version family and code path.
