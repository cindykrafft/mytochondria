# clusterProfiler (with fgsea) audit against 244 published papers (2021–2026)

_Generated 2026-09-08 against `YuLab-SMU/clusterProfiler` `devel` @ `93835a3` (2026-08-14,
4.21.1.003), its engine `YuLab-SMU/enrichit` `devel` @ `a261244` (0.2.2) and the CRAN releases
0.1.4/0.2.0/0.2.1, the legacy engine `YuLab-SMU/DOSE` 3.30.0 @ `53d1a8d`, and `ctlab/fgsea` `master`
@ `d466383` (1.39.4). Focus: the numbers — hypergeometric ORA, GSEA (ES, NES, p, leading edge),
multiple testing, q-values, `simplify` — verified by executing the shipped code._

## What this is

The six-journal survey found **244 papers** in PNAS (120), *Nature* (95), *Cell* (20) and *Science*
(9), 2021–2026, that used clusterProfiler, the most-cited R package for GO/KEGG over-representation
analysis and preranked GSEA; 122 name fgsea and 720 name GSEA, many through clusterProfiler. Since
4.19.3 (2025-12-07) clusterProfiler's `enricher`/`enrichGO`/`enrichKEGG` and `GSEA`/`gseGO`/
`gseKEGG` are thin wrappers over a new CRAN package, **enrichit**, which re-implements the ORA and
ports fgsea's multilevel GSEA to C++; every version the cohort names (4.10.1, 4.6.2, 3.14.3, 4.2.2,
4.0.5 …) ran the older engine in **DOSE** with **fgsea** underneath. All three engines, the wrappers
at `devel` and at 4.12.0, and the three enrichit versions a Bioconductor 3.23 user could have
installed were built here and run on synthetic data with known truth against scipy, an independent
numpy GSEA and exact enumeration of the permutation null, then on the real GO BP annotation
(org.Hs.eg.db 3.18.0) to measure magnitudes.

## Findings (details and line citations in [`component-reviews/enrichment-core.md`](component-reviews/enrichment-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **CP1** | **CONFIRMED on the current release** (clusterProfiler 4.20.0 + CRAN enrichit 0.1.4–0.2.1); fixed on `devel` (enrichit 0.2.2, 2026-08-14, not on CRAN as of 2026-09-08) | held (fixed and announced upstream; heads-up text kept) | `GSEA()`/`gseGO()`/`gseKEGG()` filter the result table on the raw p only, so it contains every gene set with p ≤ 0.05 whatever its `p.adjust`. GO BP, 18,870 ranked genes: 717 rows of which 515 have p.adjust > 0.05 (max 0.44); a pure-noise list gives 292 "enriched" terms; `devel` gives 204 and 0. |
| **CP2** | **CONFIRMED on every legacy version** (clusterProfiler ≤ 4.18 = all cohort versions; DOSE `leading_edge()` since 2016); fixed on `devel` by the engine change, unannounced | held | For a negative-ES gene set the leading edge is taken from the lowest *post-hit* running score instead of the running-sum minimum, so `core_enrichment` lists extra genes: 28 of 457 negative sets (6.1 %) on a 15,000-gene list, median +4 genes (+12 %), up to +31 (+225 %); 4.12.0 `GSEA()` returns 74 genes where the definition (and `devel`) gives 43. NES, p, `rank` unaffected. |
| **CP3** | **CONFIRMED on every legacy version** (DOSE `enricher_internal` since 2015); fixed on `devel` | held | With a user-supplied `universe`, query genes outside it were still counted as draws (n) and terms hit only by them were tested with `Count = 0`. GO BP, 20 of 200 query genes outside a 12,000-gene background: n = 200 vs 180, p larger by a median factor 1.21, 939 vs 1,130 terms at p.adjust ≤ 0.05, 191 calls differ. No effect when the query is a subset of the background. |
| **CP4** | **CONFIRMED at `devel` and on every enrichit release**, non-default path | held (issue + patch ready for `YuLab-SMU/enrichit`) | `gsea(method = "sample"/"permute")` and `adaptive = TRUE` divide by all permutations instead of the same-sign ones: p is ≈ half the GSEA-convention value (exact enumeration: 0.45 vs 0.88; median ratio 0.50 over 14 sets) and a set lying entirely at one end of the list gets p = 1/(nPerm+1). Reached from `GSEA(method = ...)`; the default `multilevel` is right. |
| **CP5** | **CONFIRMED on enrichit 0.1.4–0.1.5** (clusterProfiler 4.19.3–4.20.0 installed 2026-04 … 06); fixed in enrichit 0.2.0 (CRAN 2026-07-01) | dropped 2026-09-08: #819 read in full, the maintainer's 2026-06-22 comment already gives this cause and fix | ORA adjusted p over every gene set in the size window including `Count = 0` sets: GO BP, 198-gene query — 513 significant terms instead of 694 (BH over 6,379 instead of 3,856). |
| CP6 / CP7 | CONFIRMED on enrichit 0.1.x (CP6) and 0.1.x–0.2.0 (CP7); fixed on CRAN | held | Multilevel ranks scaled by a fixed 10^6: `NaN` ES/NES/p for small-magnitude statistics. Gene-set size window applied to the raw set instead of its overlap with the list. |
| CP8 | CONFIRMED at `devel`, design consequence | held (design question) | `simplify()` removes terms that are similar to no kept term (8/172, 4/60, 12/195 removed terms on three GO runs, including terms ranked 8th and 20th by p.adjust) because the greedy cluster rule removes a term in favour of a better term it is not itself similar to. |
| N1–N8 | notes | — | q-value policy changed with the engine (up to 0.18 on synthetic data, identical on the GO example); `method` help lists two invalid names; C++ vs R rounding in the `leading_edge` string; legacy `by = "DOSE"` crashes on equal-sized sets; `eps` not scaled by the sign fraction in enrichit (by reading; fgsea README says 1e-10, code 1e-50); ties keep input order; no reproducibility without `seed`/`set.seed()`; `enrichGO` SYMBOL path counts one-to-many symbols per id (none in human). |

Three own suspicions were withdrawn by execution (fgsea's integer scaling of the weights, ≤ 1.9e-7
on ES; BH over zero-overlap sets at `devel`; cross-cluster adjustment in `compareCluster`).

**Held up under execution:** the hypergeometric test, its parameters, ratios, z-score and BH against
scipy (1e-15); ES, leading edge, `rank`, `tags/list/signal`, set sizes with absent and duplicated
members, `minGSSize`/`maxGSSize`, `gseaParam`/`exponent` 0–2 and `scoreType` against the numpy
reference on all 34 sets for fgsea, enrichit (all methods) and `clusterProfiler::GSEA`; multilevel
p-values (fgsea and enrichit) and NES within their stated error of exact enumeration; `eps`
flooring; `enrichGO` ≡ engine, `compareCluster` ≡ per-cluster calls, `setReadable`; fgsea's own 49
tests and clusterProfiler's 9. See the review's held-up list.

## How the papers use clusterProfiler (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| DESeq2 / edgeR / limma in the same paper | 153 |
| Seurat / Scanpy in the same paper | 103 |
| `enrichGO` / GO ORA | 80 |
| GSEA named / `gseGO`-style GSEA through clusterProfiler / fgsea named | 79 / 54 / 18 |
| single-cell | 48 |
| adjusted p / BH / FDR cutoff (0.05 ×24, 0.1 ×3, 0.001 ×1) | 38 |
| `enrichKEGG` / KEGG | 37 |
| `enricher` / custom gene sets (MSigDB, hallmark) | 34 |
| ORA / hypergeometric / Fisher named | 29 |
| ontology named (BP 17, MF 3, CC 2) | 28 |
| ranking metric stated | 14 |
| background / universe stated | 9 |
| GSEA desktop / Broad | 9 |
| `setReadable` / symbols, q-value stated, `compareCluster`, `simplify`, NES reported, permutations stated, size limits | 5, 4, 3, 2, 2, 3, 2 |
| version stated | 35 (4.6.x 10, 4.10.x 9, 4.8.x 8, 4.0.x 8, 4.2.x 8, 4.12.x 7, 3.14.x 6, 4.14.x 4, 4.4.x 4, 3.18.x 4 …; top: 4.10.1 ×6, 4.6.2 ×6, 3.14.3 ×5, 4.2.2 ×5) |

Every stated version is ≤ 4.14, i.e. the DOSE/fgsea engine: the cohort is exposed to CP2 (every
GSEA paper reporting leading-edge genes of a suppressed pathway — 54 run GSEA through
clusterProfiler) and to CP3 (only where a DE list is not a subset of the stated background; 9 state
one), and to none of the enrichit-era findings CP1/CP4–CP7. CP1 will hit papers written on
Bioconductor 3.23 during 2026 unless the authors filtered `p.adjust` themselves.

**Profiling caveat.** As for the Seurat, Scanpy and Cutadapt audits, this session had no route to
Europe PMC, so `clusterprofiler_profile.py` ran in `--offline` mode over the survey's stored evidence
snippets; every record in `clusterprofiler_profiles.jsonl` is `source: survey_cache` and every count
above is a lower bound. Rerun without `--offline` from a host with Europe PMC access to replace them
with full-text records.

## Filing channel (read before anything is sent)

- clusterProfiler `CONTRIBUTING.md`: a reproducible example with packages at the top, data via
  `dput()`, commented code, checked in a fresh session; the "Pull requests" section is empty.
  `.github/issue_template.md`: checkboxes (latest release, documentation read, googled), a
  reproducible example with comments on expected vs actual, and "for questions, post to
  Bioconductor support or Biostars with the tag clusterProfiler". No PR template, no linter config.
  `NEWS.md` entries are `+ text (YYYY-MM-DD, Day, #issue)` under `# clusterProfiler x.y.z.nnn`.
  The template links the maintainer's "how to bug author" guide and the package book
  (`yulab-smu.top`); both hosts are unreachable from this session and **must be read before filing**.
  `docs/adr/0001` records the product direction (mechanism interpretation), not a results policy.
- enrichit (where CP4 lives): no CONTRIBUTING, no templates, `NEWS.md` in the same convention, a
  testthat suite; one issue in its tracker (closed). Default branches: clusterProfiler, enrichit,
  DOSE `devel`; fgsea `master` (development at `alserglab/fgsea`).
- fgsea: no CONTRIBUTING or templates, plain `NEWS`; nothing to file — everything held up.
- The project fork for these repositories does not exist yet; `site/audits.json` has no entry, so no
  `upstream-declines-ai-contributions` topic could apply. Tiers above follow README step 5: nothing
  is a file-now candidate — CP1 is fixed and announced upstream (only the CRAN release is missing),
  CP2/CP3/CP5–CP7 are fixed at master, CP4 is a non-default path, CP8 a design question. **The kit is
  in [`upstream/`](upstream/)**: one `git am`-able patch for enrichit (CP4, fix + exact-enumeration
  test + NEWS; the test fails on unmodified `devel`, the full suite passes with it), the CP4 issue
  text, a comment draft for #819 (CP5), a heads-up text for CP1, three MCVEs with outputs.

## Files

| file | what |
|---|---|
| `clusterprofiler_profile.py`, `clusterprofiler_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/enrichment-core.md` | the review: CP1–CP8, N1–N8, withdrawn, held-up, not-audited |
| `verify/ref_gsea.py` | independent numpy GSEA (running sum, ES, leading edge, tags/list/signal), exact permutation null, BH, hypergeometric |
| `verify/ora_vs_scipy.R` / `.py` (+ `.out`) | ORA (enrichit `devel`, DOSE 3.30.0) vs scipy; universe handling; CP3 |
| `verify/gsea_vs_reference.R` / `.py` (+ `.out`) | ES, leading edge, sizes, `gseaParam`, `scoreType`, ties, seeds on fgsea, enrichit (3 methods), DOSE (2 paths), `clusterProfiler::GSEA`; CP2 first sighting |
| `verify/gsea_exact_small.R` / `.py` (+ `.out`) | p-values and NES vs exact enumeration (2,024 / 91,390 / 142,506 gene sets); CP4 |
| `verify/enrichit_release_scope.R` (+ `.out`) | CP1, CP5, CP6, CP7 on enrichit 0.1.4 / 0.2.0 / 0.2.1 / `devel` |
| `verify/cp4_versions.R` (+ `.out`) | CP4 on enrichit 0.1.4 / 0.2.0 / 0.2.1 / `devel` / `devel` + patch |
| `verify/go_realdata.R` (+ `.out`) | magnitudes on GO BP (org.Hs.eg.db): CP1, CP3, CP5, N1 |
| `verify/legacy_leading_edge.R` (+ `.out`) | CP2 at scale, through DOSE and the 4.12.0 wrapper; N4 |
| `verify/heldup_wrappers.R` (+ `.out`) | `enrichGO` (both key paths), `setReadable`, `simplify`, `compareCluster`, `gseGO`, `method` values |
| `verify/note_simplify.R` (+ `.out`) | CP8 breakdown |
| `upstream/` | filing kit: patch 0001 (enrichit, CP4), issue/comment texts, MCVEs and outputs, documents read |

Environment: R 4.3.3 (`/usr/bin/R`); packages built with `R CMD INSTALL --no-docs` into private
libraries from the GitHub clones (fgsea, enrichit at four states, GOSemSim, gson, yulab.utils,
HDO.db, clusterProfiler `devel` and 4.12.0, DOSE 3.30.0) with the rest from apt; CRAN and
Bioconductor were unreachable, so the Bioconductor release branch itself could not be fetched —
"release" statements rest on the release commit `d67d9f6` (identical wrappers) plus the CRAN
enrichit versions from the `cran/enrichit` mirror. `enrichplot` and `aisdk` are stubs (plotting and
LLM only; see the review). Python side: `uv venv --python 3.12` with numpy 2.5.3, scipy 1.18.1.

## Next steps

1. Read the #819 thread and the maintainer's guide/book pages from a host that can reach them; post
   the CP5 comment is dropped: #819 was read in full on 2026-09-08 (`upstream/thread-819.txt`) and the maintainer's comment of 2026-06-22 already names the cause and the fix.
2. Once a maintainer has responded to anything from this project on these repositories, offer the
   CP4 patch to `YuLab-SMU/enrichit` (issue first, per the template's conventions).
3. Check CRAN for enrichit 0.2.2; if it is still absent at the Bioconductor 3.24 release, send the
   CP1 heads-up.
4. Full-text profiling rerun when Europe PMC is reachable, to count the papers that report
   leading-edge genes of suppressed pathways (CP2) and those with a background that does not contain
   the query (CP3).
