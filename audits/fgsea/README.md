# fgsea audit against 122 published papers (2021–2026)

_Generated 2026-10-18 against `alserglab/fgsea` `master` @ `570f590` (1.39.4, 2026-09-17), the
current Bioconductor release 1.38.0 (`RELEASE_3_23` @ `1fe4644`, numerically identical to
`master`), 1.36.2 (`RELEASE_3_22`, the last release before the November 2025 multilevel rewrite)
and the cohort's most-cited releases 1.30.0 (`RELEASE_3_19` @ `5f63439`), 1.26.0 (`RELEASE_3_17` @
`102b439`) and 1.20.0 (`RELEASE_3_14` @ `b704f81`), all built here (R 4.3.3). Focus: what a paper
takes from fgsea — `pval`/`padj` from `fgseaMultilevel` (the default) and `fgseaSimple`, the
multilevel lower bound (`eps`, `log2err`), NES, ES under `gseaParam` and ties, `scoreType`,
`leadingEdge`, size filtering, and seed/`nproc` reproducibility. Every check was run against a
reference computed independently: exact enumeration of all gene-set placements, an exact
dynamic-programming tail probability down to 1e-72, and a Python port of the documented
definitions._

## What this is

The six-journal survey found **122 papers** in *Nature* (68), PNAS (38), *Cell* (12) and *Science*
(4), 2021–2026, that name fgsea; many of the 720 papers that name "GSEA" reach it through
clusterProfiler ≤ 4.18 (DOSE) and other wrappers. The related clusterProfiler audit
(`../clusterprofiler/`) ran fgsea 1.39.4 as one engine among several and found nothing to file
in it. This audit checks fgsea on its own and goes further: version by version, at p-values far
below what permutations reach, and on tied, zero and one-tailed inputs. The numerical core
(`R/fgsea.R`, `R/fgseaMultilevel.R`, `src/fgseaMultilevelSupplement.cpp`, `src/esCalculation.*`,
`src/fastGSEA.cpp`, `src/util.cpp`) was read on `master` and on the release branches, and each
suspicion was run on six builds.

**Outcome.** The current release holds up. ES, leading edge, NES, and the multilevel p-values
from 2.6e-4 down to 1.8e-72 agree with exact values within the stated `log2err`, and results
are reproducible across back-ends. The two defects that changed published numbers (FG1, FG2)
are in the cohort's versions, were reported upstream, and were fixed in 1.32 and 1.38. Nothing
reaches the "now" tier.

## Findings (details and line citations in [`component-reviews/gsea-core.md`](component-reviews/gsea-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **FG1** | **CONFIRMED on 1.20.0, 1.26.0, 1.30.0**; fixed in 1.31.3 (released 1.32.0); duplicate of upstream #176 (closed 2025-08-11) | held (fixed upstream, already reported) | The leading edge of a positive-ES pathway was cut at the largest pre-hit running sum (`which.max(bottoms)`) instead of the peak, so it often runs past the peak. On a 5,000-gene list, 14 of 130 positive sets (10.8 %) get a different leading edge, median +4 genes, up to +29 (61 genes listed where the definition gives 32). 1.20.0/1.26.0 also apply the std rule to `scoreType = "pos"/"neg"` (184/299 and 130/300 sets differ). ES, p and NES are unaffected. 23 of the 24 cohort papers that state a version used ≤ 1.30. |
| **FG2** | **CONFIRMED on 1.20.0, 1.30.0, 1.36.2**; accurate on 1.38.0/`master`; upstream #151, fixed by the 1.37.1 rewrite (PR #178) | held (fixed upstream, already reported) | Before the rewrite the multilevel sampler could not get past tied scores near ES = 1. A set holding the top 15 genes of a list with tied integer scores (exact p 2.9e-33): 1.20.0/1.30.0 do not return within 300 s with `eps = 0`; 1.30.0 returns p = 1e-50 at the default `eps`; 1.36.2 returns 1.0e-27. Against exact tails 1.36.2 is ×10^5–10^11 off at ES = 1 and ×18 at ES 0.979 (k = 40). On a 32-gene list with tied scores, 1.30.0 gives 1.55× the exact p at p ≈ 0.01. All the large misses are at p < 1e-25, where significance calls do not change. |
| **FG3** | **CONFIRMED on 1.30.0, 1.36.2, `master`** | held (design question; issue draft ready) | A set whose present members all have stat exactly 0 is given equal weights, so its ES comes from where the zero block sits in the ranking and from the members' input order inside it. Zeros are excluded from the ties warning, so nothing is printed. With 6,000 zeros in 20,000 genes, a 100-gene all-zero set adjacent in input order gets padj 1.5e-3 (scattered: 0.75); moving it first or last in the input gives ES +0.65 or −0.64 at p ≈ 1e-9. Same precondition as GSEA Desktop's GS3, which a real-data check (airway, PBMC 3k, all MSigDB) never met. That audit says fgsea warns in this case; for zeros it does not. |
| FG4 | CONFIRMED on `master` | held (negligible exposure) | `fgseaSimple` and the simple stage of `fgseaMultilevel` count permutation scores with floating-point comparisons. A negative ES at the first hit, −(S1−1)/(N−k), is shared exactly by every set with the same first member, but floating cancellation makes most of those ties compare as less extreme. Exact enumeration on a 24-gene list gives p 0.0177; fgsea's own ES values give 0.0138 (×0.78); fgseaSimple returns 0.0139 (R path) and 0.0119 (C++ path). The multilevel stage is exact. On lists of 500–20,000 genes the tied mass is ≤ 0.001 % of the tail. |
| FG5 | CONFIRMED on `master` | held (test/code quality; patches 0001, 0002) | The test "fgseaMultilevel is reproducable independent of bpparam settings" compares `nMoreExtreme`, a column `fgseaMultilevel()` drops, so it passes whatever the p-values are; seeding one of its calls differently goes unnoticed (patched test: 2 failures). `setUpBPPARAM(nproc = 1)` overwrites its `SerialParam()` with `MulticoreParam(1)`. Reproducibility itself holds (identical output for every back-end and worker count). |
| N1 | note, verified | — | Since 1.37.1 gene weights are rounded to integers after scaling by floor(2^30/sum). At `gseaParam = 1` ES moves ≤ 7.6e-6 on four ranking metrics (1.36.2: exact). At `gseaParam = 2` on signed −log10 p, 5,717 of 20,000 non-zero stats round to 0 and ES moves ≤ 4.1e-3. NEWS documents "minor result discrepancies in rare cases". |
| N2 | note | — | Pathways with p ≳ 0.03 take their p from the 1,000-permutation simple stage, so the count of padj < 0.05 moves a few percent between seeds (upstream #145, #162). By design. `log2err` ignores the ±4–5 % error of the sign denominator. |
| N3, N4 | notes | — | Weighted GSEA gives a set of 99 zero-stat genes plus one gene at 0.3 an ES of 0.991 (a property of the weighted statistic). `README.md` shows 1e-10 floors while the default `eps` is 1e-50. |

Withdrawn by execution: 5 (bias of the rewritten multilevel estimator; an enrichit-CPR1-style
miscount at ES = ±1; ES flooring/`score_t` mixed comparisons; `nproc` dependence; zero-weight
handling between the R statistic and the C++ sampler). See the review.

**Held up under execution:** ES for std/pos/neg at `gseaParam` 0, 1 and 2, with tied and zero
stats and with absent and duplicated members, `size` as the overlap and `minSize`/`maxSize` on
the overlap, on all six builds against the Python reference (≤ 2e-15; ≤ 8.1e-7 with integer
weights). The leading edge on 1.32+ in every configuration. Multilevel and simple p-values for
std/pos/neg against exact enumeration of three short lists, one with ties and zeros (multilevel
geometric mean 0.94–1.19× exact, median 1.002; simple median 1.000). Multilevel p against exact
DP tails from 2.6e-4 to 1.8e-72 on a 1,000-gene list, k = 15 and 40, both signs (0.85–1.20×, 85–100 %
of runs within 2·log2err; DP checked against brute force). NES against ES / mean(same-sign exact
null) within 0.016. The `eps` floor and its warning. Output identical across `SerialParam`,
`nproc` 1/2/4, the default `bpparam()` and `SnowParam(2)`. 1.38.0 identical to `master`. fgsea's
own suite: 61 tests, 152 expectations, 0 failures (2 skipped: reactome.db and GEOquery
examples). **Not checked:** `fora`/`collapsePathways`/`collapsePathwaysORA` (read only),
`fgseaLabel`, GESECA, plots beyond reading `plotEnrichmentData`, Windows/macOS
cross-platform reproducibility (#170), and versions 1.22, 1.28 and 1.34 (bracketed by the
builds above; FG1 and FG2 are present in every version ≤ 1.30 and ≤ 1.36 respectively, by the
code at the release branches).

## How the papers use fgsea (lower bounds from the survey cache)

| signal | papers |
|---|---|
| version stated | 24 fgsea versions (1.30.0 ×4, 1.28.0 ×4, 1.26.0 ×3, 1.22.0 ×3, 1.20.0 ×3, 1.10.1 ×2, 1.8.0, 1.16.0, 1.18.0, 1.25.1, 1.34.0); 2 more give an R/Bioconductor version |
| ≤ 1.30 (FG1 leading edge; FG2 old sampler ≤ 1.36) | 23 of 24 |
| ≤ 1.12 (default was `fgseaSimple`, permutation p only) | 3 |
| NES reported / "normalized enrichment" | 30 / 4 |
| DESeq2 / limma / edgeR in the evidence sentence | 8 / 4 / 1 |
| via clusterProfiler, Seurat in the sentence | 4, 3 |
| `nperm` stated (2,000; 10,000; 100,000) | 3 |
| `minSize`/`maxSize` stated, multilevel named, collapsePathways | 2, 3, 2 |
| journals | *Nature* 68, PNAS 38, *Cell* 12, *Science* 4; 2021 11 … 2025 32, 2026 18 |

Which finding reaches which paper. FG1 affects every paper on ≤ 1.30 that lists the
leading-edge genes of an up-regulated pathway: about one pathway in ten, a few extra genes past
the peak. FG2 affects papers that report p or padj for near-perfect sets (only at p < 1e-25 in
these tests, so not the significance call) and runs that hung on tied rankings. FG3 needs a
custom gene set that is entirely unexpressed in the ranked list. FG4 needs a list of a few
dozen genes. The counts come from the survey's stored evidence sentences (`paper_software.tsv`,
row `fgsea`; no Europe PMC route from this session), so they are lower bounds.

## Filing channel

`alserglab/fgsea` has no `CONTRIBUTING`, no issue or PR template and no AI-contribution policy
in the tree (`.github/` holds only `R-CMD-check.yaml`, which runs `rcmdcheck` on macOS, Windows
and three Ubuntu R versions for every PR against `master`). Bug reports go to the GitHub tracker
(`BugReports:` in `DESCRIPTION`); the maintainer (Alexey Sergushichev, `assaron`) answers
quickly and asks for a reproducible example. The thread record is in
[`upstream/dupcheck-2026-10-18.md`](upstream/dupcheck-2026-10-18.md). Kit under
[`upstream/`](upstream/): nothing at the "now" tier. One held issue text (FG3), one held
issue + PR body with two `git am`-able patches (FG5), and the test runs. No fork of
`alserglab/fgsea` exists under `cindykrafft`.

## Files

| path | what |
|---|---|
| `component-reviews/gsea-core.md` | the review: FG1–FG5, N1–N4, withdrawn, held-up, not audited, with line citations |
| `verify/_ref.py` | independent reference: running sum, ES (std/+/−), leading edge, batch ES, exact enumeration, documented p/NES, exact DP tail `dp_tail_pos` |
| `verify/dp_selftest.py` (+ `.out`) | DP tail vs brute force (exact to the last digit) |
| `verify/v0_release_equals_master.R` (+ `.out`) | 1.38.0 vs `master` on the package example: identical |
| `verify/v1_es_leading_edge.R` / `.py` (+ `.out`, `v1_work/run_*.log`) | ES, size and leading edge on six builds (FG1) |
| `verify/v2_exact_small.R` / `.py` (+ `.master.out`, `.v1.30.0.out`, `v2_work/`) | p and NES vs exact enumeration, std/pos/neg, tied list (FG2, FG4) |
| `verify/v3_dp_tail.R` / `.py` (+ `.<version>.out`, `v3_truth.out`, `v3_work/`) | multilevel p vs exact DP tails to 1e-72 (FG2, W1) |
| `verify/v4_integer_scaling.R` (+ `.out`) | integer weights vs the double definition (N1) |
| `verify/v5_reproducibility.R` (+ `.out`) | seeds, back-ends, the vacuous test (FG5) |
| `verify/v6_es1_hang.R` (+ `.<version>.out`) | ES = 1 with tied top scores on 1.20/1.30/1.36/1.38/master (FG2) |
| `verify/v7_zero_block.R` (+ `.<version>.out`) | all-zero gene sets (FG3, N3) |
| `verify/v8_tie_counting.R` / `.py` (+ `.out`), `verify/v9_tie_mass.py` (+ `.out`) | floating tie counting and its exposure (FG4) |
| `upstream/` | filing kit (held items only) |

The large per-set JSON outputs of v1 and v8 (31 MB) were left in the session scratch directory;
rerun the `.R` script for the version, then the `.py`, to regenerate them.

## Next steps

1. Nothing to file under the triage rule: the defects that changed published numbers are
   reported and fixed upstream (FG1 #176, FG2 #151), and the current release is right.
2. If the project files against fgsea for another reason: FG5 (patches 0001/0002, a test fix the
   maintainer can check in a minute) is the low-risk first contact. FG3 goes as a question
   (warn on all-zero sets, or include zeros in the ties warning when some tested set has total
   weight 0) only after a positive reply.
3. Correct the GSEA Desktop audit's GS3 row and README, which say fgsea "warns about ties" in the
   all-zero case (FG3: it does not, because zeros are excluded from the warning).
