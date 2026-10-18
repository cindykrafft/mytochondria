# Component: fgsea preranked GSEA core (ES, leading edge, fgseaSimple, fgseaMultilevel, NES)

## Code read

| repository | commit | date | version | role |
|---|---|---|---|---|
| `alserglab/fgsea` [`master`] (formerly `ctlab/fgsea`) | `570f590` | 2026-09-17 | 1.39.4 | development head; numerically identical to the release (below) |
| Bioconductor `RELEASE_3_23` | `1fe4644` | 2026-04-28 | 1.38.0 | **current release**; `git diff RELEASE_3_23 devel` touches only docs, CI, `RcppExports` names and a vignette; `../verify/v0_release_equals_master.out`: identical pval/padj/log2err/ES/NES/size/leadingEdge on the package example |
| `RELEASE_3_22` | — | 2025-10 | 1.36.2 | last release before the November 2025 multilevel rewrite (hash tie-breaking, integer weights) |
| `RELEASE_3_19` / `3_17` / `3_14` | `5f63439` / `102b439` / `b704f81` | 2024-04 / 2023-04 / 2021-10 | 1.30.0 / 1.26.0 / 1.20.0 | the cohort's most-cited versions (1.30.0 ×4, 1.28.0 ×4, 1.26.0 ×3, 1.22.0 ×3, 1.20.0 ×3) |

Files: `R/fgsea.R` (wrapper, `prepareStats`, `calcGseaStat`, `fgseaSimple`, `fgseaSimpleImpl`,
`collapsePathways`, `setUpBPPARAM`), `R/fgseaMultilevel.R`, `R/util.R`, `R/fgseaORA.R`,
`R/plot.R` (`plotEnrichmentData`), `src/esCalculation.{h,cpp}` (exact `score_t` arithmetic),
`src/fgseaMultilevel.cpp`, `src/fgseaMultilevelSupplement.{h,cpp}` (`EsRuler`), `src/fastGSEA.cpp`
(permutation sampler for `fgseaSimple`), `src/util.cpp` (`combination`, `uid_wrapper`,
`betaMeanLog`), `tests/testthat/`. Line numbers below are for `master` unless a version is named.

Builds: R 4.3.3, each version installed with `R CMD INSTALL --no-docs` into its own library from
the GitHub clone (master) or the Bioconductor git release branches (1.38.0, 1.36.2, 1.30.0,
1.26.0, 1.20.0; the three oldest needed `SystemRequirements: C++17` in place of `C++11` to compile
against BH 1.90, no source change). Dependencies from CRAN and Bioconductor 3.18 (BiocParallel
1.36.0, data.table 1.18.6.1, Rcpp 1.1.2, BH 1.90.0-1).

## How the numbers are made (as read)

- **Ranking and weights.** `prepareStats` (`R/fgsea.R:40-75`) stops on non-finite stats, warns
  about ties among *non-zero* values (`:47`), sorts decreasing (stable: tied genes keep input
  order), takes `abs(stats)^gseaParam` and, since 1.37.1, multiplies by `floor(2^30 / sum)` (or
  the unfloored ratio when the sum exceeds 2^30) and rounds to integers (`:63-73`).
- **ES.** `calcGseaStat` (`:112-180`): running sum after (`tops`) and before (`bottoms`) each hit;
  std ES = max top if it beats |min bottom|, min bottom if it loses, 0 on a tie (`:152-155`); a set
  whose weights sum to 0 is given equal weights (`:133-147`, "equivalent to rAdj being
  rep(eps, m)"). Leading edge: members up to `which.max(tops)` (ES > 0) or from
  `which.min(bottoms)` (ES < 0) (`:165-178`).
- **fgseaSimple.** Random sets of the largest tested size; each pathway takes the ES of the first
  `size` random genes (`src/fastGSEA.cpp:380-437`, convex-hull speed-up in `gseaStats1`), or, with
  a single pathway, R's `sample.int` + `calcGseaStat` (`R/fgsea.R:631-646`). p = min over the two
  tails of `(1 + #more extreme) / (1 + #same sign)` (`:700-701`); NES = ES / mean of same-sign
  random ES (`:693-697`).
- **fgseaMultilevel** (default of `fgsea()` since 1.13.2): a `fgseaSimpleImpl` stage with
  `nPermSimple = 1000` gives NES, the sign denominator `denomProb = (nSameSign + 1) / 1001`
  (`R/fgseaMultilevel.R:200`) and a crude p; pathways whose simple-stage error beats the
  multilevel error keep the simple p (`:160-192`), the rest go to `EsRuler` per gene-set size
  (`:202-212`). `EsRuler::extend` (`src/fgseaMultilevelSupplement.cpp:135-237`) splits at the
  median ES+ of 101 samples, MCMC-perturbs the samples above the level with exact `score_t`
  comparisons and (since 1.37.1) gene-hash tie-breaking; `getPvalue` (`:241-316`) sums
  `digamma(nhigh + 1) - digamma(N + 1)` per level (the expected log of the order-statistic Beta
  law) and counts same-sign samples at the final level; R divides by `denomProb` (`:221`) and
  floors at `eps = 1e-50` (`:239`).

## Findings

### FG1 — CONFIRMED on 1.20.0, 1.26.0, 1.30.0; fixed in 1.31.3 (released in 1.32.0, Bioconductor 3.20); reported upstream as #176 (closed 2025-08-11) — held (duplicate, fixed)

Up to 1.30.x the leading edge of a positive-ES pathway was cut at `which.max(bottoms)` — the
largest *pre-hit* running sum — instead of the peak of the running sum
(`RELEASE_3_19:R/fgsea.R:177,185,191`; fixed by `82f17c9`, 2024-09-20, NEWS 1.31.3 "minor fix
in leading edge calculation"). When the hit after the peak follows closely, the maximum of
`bottoms` falls on that later hit and every member up to it is reported. 1.20.0 and 1.26.0 also
applied the std rule to `scoreType = "pos"/"neg"` (fixed by `ecfb89c`, 2023-10-26).

`../verify/v1_es_leading_edge.out` (300 sets, sizes 15–500, on a 5,000-gene t-like list, the same
list rounded with 5 % zeros, `gseaParam` 0/1/2): on 1.30.0 the default run gives a different
leading edge for **14 of the 130 positive-ES sets (10.8 %)**, median +4 genes, up to +29
(`S035`: 61 genes where the definition gives 32); 20/103 at `gseaParam = 2`; none at
`gseaParam = 0`. 1.20.0/1.26.0: the same 14, plus 184/299 (`pos`) and 130/300 (`neg`) one-tailed
runs. 1.32+ (1.36.2, 1.38.0, master): 0 differences in every configuration. ES itself is right
in all versions (≤ 1.9e-15 on the double-weight versions). The issue reporter on #176 (fgsea
1.28.0) saw the leading edge end after the peak; the maintainer pointed to 1.31.3.

Cohort exposure: 23 of the 24 papers that state an fgsea version used ≤ 1.30 (only one states
1.34.0); every one of them that lists leading-edge genes of an up-regulated pathway may list a
few genes past the peak. clusterProfiler ≤ 4.18 computes its own `core_enrichment` (DOSE
`leading_edge`, see the clusterProfiler audit CP2) and is not affected by FG1.

### FG2 — CONFIRMED on 1.20.0/1.30.0 (no return), 1.36.2 (p overestimated up to 10^11); accurate on 1.38.0/master; upstream #151 (closed with the 1.37.1 rewrite, PR #178) — held (fixed)

The pre-rewrite `EsRuler` worked in doubles and split levels by value only. When the samples
above a level all share one score (tied top scores, ES at or near 1), the median cannot advance.
By reading, the level loop `while (enrichmentScores.back() <= ES - 1e-10)`
(`RELEASE_3_19:src/fgseaMultilevelSupplement.cpp:87`) then only exits through the `eps` level cap
(`:128-133`), which never fires when `eps = 0`. The executions below fit this reading: no return
with `eps = 0`, and with the default `eps` a return at the floor. 7282d85 (2024-08, in 1.32+)
breaks out when the median does not advance and marks the estimate as unreliable.

- `../verify/v6_es1_hang.*.out`: the top 15 genes of a 1,000-gene list with integer scores 1–4
  (ES = 1, exact p = 2.86e-33): 1.20.0 and 1.30.0 with `eps = 0` are killed by `timeout` after
  300 s; 1.30.0 with the default `eps = 1e-50` returns **p = 1e-50**, below the true value;
  1.36.2 returns **p = 1.0e-27** (log2err NA); 1.38.0 and master return 1.1e-32 (log2err 1.49).
- `../verify/v3_dp_tail.v1.36.0.out` (exact truth by dynamic programming, below): 1.36.2 is off
  by ×1.9e5 (k = 15, ES = 1), ×1.3e11 (k = 40, ES = 1), ×18 (k = 40, ES = 0.979) and ×1.3–1.4
  (k = 15, ES ≈ 0.98); everything with ES ≤ 0.94 is within its log2err. 1.30.0 and 1.20.0
  (`v3_dp_tail.v1.30.0.out`, `.v1.20.0.out`, ES = 1 sets skipped) match 1.36.2.
- `../verify/v2_exact_small.v1.30.0.out`: on a 32-gene list with tied scores, 1.30.0's multilevel
  p is **1.55× the exact value** for a set at p = 0.0103 (master: 0.94×); untied lists agree with
  enumeration.

Every miss above 2× is at p < 1e-25, so no significance call in the v3 runs changes; the tied
short list is the only case seen at an ordinary p. NEWS 1.37.1 ("P-values for ES close to 1 are
more accurate now"; "properly fixes #151") announces the fix.

### FG3 — CONFIRMED on 1.30.0, 1.36.2 and master — held (design question; issue draft `../upstream/issue-fg3-all-zero-set-order-dependent-es.md`)

A gene set whose present members all have stat exactly 0 gets equal weights
(`R/fgsea.R:133-147`), so its ES is a Kolmogorov–Smirnov statistic of where the block of zeros
sits in the ranking and of the members' **input order inside that block** (ties keep input order,
`:60`). `prepareStats` leaves zeros out of the ties warning (`:47`), so nothing is printed.
`../verify/v7_zero_block.v1.39.4-master.out` (20,000 genes, 6,000 at exactly 0):

| set (100 genes) | ES | NES | p | padj |
|---|---|---|---|---|
| all zero, scattered in input order | 0.356 | 1.16 | 0.155 | 0.75 |
| all zero, adjacent in input order | 0.552 | 1.79 | 1.5e-05 | **1.5e-03** |
| same set, moved first in input order | 0.652 | 2.14 | 1.4e-09 | — |
| same set, moved last in input order | **−0.644** | −2.11 | 2.6e-09 | — |
| 200 random 100-gene sets | median \|ES\| 0.31, max 0.46 | | | min 0.28 |

Same numbers on 1.30.0 and 1.36.2 (`v7_zero_block.v1.30.0.out`, `.v1.36.0.out`). The
equal-weight choice is deliberate and documented in a code comment, and it is the p → 0 limit, so
this is a design question rather than a defect. What is not documented is that the result then
depends on the order of the input vector, which the ties warning exists to flag. Precondition
exposure is small: the GSEA Desktop audit (GS3, same precondition) found no MSigDB 7.5.1 set
of 15–500 present members with every member at 0 on airway (13,757 zeros) or PBMC 3k (up to
4,344 zeros) lists. It needs a custom set of genes unexpressed in the data. That audit's README
says "fgsea computes the same order-dependent number but warns about ties"; for zeros it does
not warn. Since 1.37.1 the rounding to integers can also turn small non-zero stats into zeros (N1).

### FG4 — CONFIRMED on master (all versions by reading) — held (negligible at realistic list lengths)

`fgseaSimple` and the simple stage of `fgseaMultilevel` count permutation scores with
floating-point `<=`/`>=` against the observed ES (`R/fgsea.R:640-641`;
`src/fastGSEA.cpp:410-416`). A negative ES that sits at the first hit equals
`-(S1 - 1)/(N - k)` exactly for every set with the same first member, but `calcGseaStat` computes
it as `(r1/NR - a) - r1/NR` (`:141-147`), whose last bit depends on `r1/NR`. Exact ties then count
as less extreme. `../verify/v8_tie_counting.master.out` (all C(24,3) sets, exact rational ES):
6 sets tie with ES = −19/21, fgsea's doubles are equal for 2, and the exact p 0.0177 becomes
0.0138 (×0.78) by fgsea's own ES values. fgseaSimple with 10^6 permutations gives 0.0139 (single
pathway, R path) and 0.0119 (batch C++ path). For ES = −6/7 the factor is ×0.83. The multilevel stage
compares exact `score_t` values and is unaffected (0.0171). On lists of realistic length the tied
mass is a vanishing share of the tail (`../verify/v9_tie_mass.out`: ≤ 0.001 % for N = 500–20,000),
so this only matters on lists of a few dozen genes. Positive ES at the last hit is computed as
`1 - x` with `cumsum(...)[m] / NR` exactly 1 on integer weights, so no ties are lost there.

### FG5 — CONFIRMED on master — held (test and code quality; patches 0001/0002)

- The test "fgseaMultilevel is reproducable independent of bpparam settings"
  (`tests/testthat/test_gsea_multilevel.R:25-49`) compares `fr$nMoreExtreme`, a column
  `fgseaMultilevel()` drops (`R/fgseaMultilevel.R:237`), so `expect_equal(NULL, NULL)` passes
  whatever the p-values are. `../upstream/test-runs.txt`: with the nproc = 2 call seeded 43, the
  current test passes (3 expectations, 0 failed). The patched test fails (6 expectations, 2
  failed). It passes on unmodified master with matching seeds.
- `setUpBPPARAM` (`R/fgsea.R:722-730`) assigns `SerialParam()` for `nproc == 1` and then
  overwrites it with `MulticoreParam(workers = 1)` (`../verify/v5_reproducibility.v1.39.4-master.out`).
- Reproducibility itself holds: `set.seed(42)` gives identical pval and NES for `SerialParam`,
  `nproc` 1/2/4, the default `bpparam()` and `SnowParam(2)`, for `fgseaMultilevel` and
  `fgseaSimple` (same file). A different seed moves p by a median of 0.11 log2 units (max 2.5),
  which is Monte Carlo error. Upstream #145 and #162 were the same question ("call `set.seed()`
  right before each call"). PR #181 records the maintainer's position that results need to be
  reproducible for the same analysis on the same version, not identical between single-pathway
  and batch runs.

## Notes (verified, not findings)

- **N1 — integer weights since 1.37.1.** `../verify/v4_integer_scaling.*.out`, 400 sets on
  20,000-gene lists: at the default `gseaParam = 1` the reported ES is within 7.6e-6 of the
  double-precision definition for signed −log10 p (capped at 320), t(3)-like statistics,
  near-zero log2FC and statistics summing above 2^30 (1.36.2: exact). At `gseaParam = 2` on
  signed −log10 p the scale factor is 20, 5,717 of 20,000 non-zero stats round to 0, and ES moves
  by up to 4.1e-3. NEWS 1.37.1 says "might introduce minor result discrepancies in rare cases".
  The rounding also feeds FG3's equal-weight branch when every member rounds to 0.
- **N2 — seed-to-seed variation of the significant set.** Pathways with p ≳ 0.03 take their p
  from the 1,000-permutation simple stage; counts of padj < 0.05 move by a few percent between
  seeds (#145: 287–303; #162: 118 vs 127). By design (`nPermSimple`, `log2err`), not reported
  as a defect. `log2err` for multilevel pathways ignores the ±4–5 % error of `denomProb`.
- **N3 — single nonzero member.** A set of 99 zero-stat genes plus one gene with stat > 0.3 gets
  ES 0.991, p ≤ 1e-50 (`v7_zero_block`), because weighted GSEA hands all weight to the one
  non-zero gene. That is a property of the weighted statistic, not of fgsea.
- **N4 — docs.** `README.md` shows `eps`-floored p-values of 1e-10 while the default is 1e-50
  (also noted in the clusterProfiler audit, N5); `fgseaMultilevel`'s `@return` documents no
  `nMoreExtreme` but the reproducibility test reads it (FG5).

## Withdrawn (own suspicions killed by execution)

- **W1** — that the 1.37.1 rewrite biases multilevel p-values: against exact tails from 2.6e-4
  down to 1.8e-72 (`v3_dp_tail.master.out`) the geometric mean of 20 runs is 0.85–1.20× the exact
  value on every set, both signs, `pos` and `std`, and |Δlog2 p| ≤ 2·log2err in 85–100 % of runs.
- **W2** — that fgseaSimple miscounts ES = ±1 the way enrichit's `sample` path does (CPR1): with
  2·10^6 permutations a bottom set (ES = −1) gets p = 0.00099 and a top set 0.00098, exact ≈ 0.0010.
- **W3** — that `ES`'s flooring to the 2^-30 grid (`src/fgseaMultilevelSupplement.cpp:165`,
  `:250`) or `score_t::Compare` with mixed `diff` fields could miscount: the only mixed comparison
  (`ES` against a level bound) decides with hash 0, which can never be the smaller hash, and the
  exact-tail comparison above shows no bias.
- **W4** — that results depend on `nproc`/`BPPARAM` (FG5 bullet 3).
- **W5** — that the observed-vs-null weight handling of zeros differs between the R statistic
  (exact 0) and the C++ sampler (`statEps`, `src/fastGSEA.cpp:171-187`): ≤ 1e-8 relative weight,
  no measurable effect (v2, v4).

## What held up (executed)

- **ES** for std/pos/neg, `gseaParam` 0/1/2, tied and zero stats, absent and duplicated members,
  `size` as the overlap, `minSize`/`maxSize` on the overlap: all six versions against the Python
  reference (`../verify/_ref.py`; `v1_es_leading_edge.out`), ≤ 2e-15 on double-weight versions,
  ≤ 8.1e-7 on 1.38.0/master (N1).
- **Leading edge** on 1.32+ (1.36.2, 1.38.0, master): identical to the definition for every set
  and configuration (FG1 for older versions).
- **p-values**: exact enumeration of all C(n, k) sets for std/pos/neg on three short lists, one
  with ties and zeros (`v2_exact_small.master.out`): multilevel (geometric mean of 20 runs)
  0.94–1.19× exact, median 1.002; fgseaSimple (2·10^5 permutations) median 1.000 (the 0.77 cases
  are FG4). Exact tails by dynamic programming on a 1,000-gene list, 2.6e-4 to 1.8e-72
  (`v3_dp_tail.*.out`, DP checked against brute force in `dp_selftest.out`): master (identical to
  1.38.0, `v0_release_equals_master.out`) within its stated error everywhere; 1.20.0/1.30.0/1.36.2 everywhere except ES ≈ 1 (FG2).
- **NES** against ES / mean(same-sign exact null ES): on all 36 rows (v2) master's multilevel NES
  (1,000-permutation stage, median of 20 runs) is within 0.016 and fgseaSimple's (2·10^5) within 0.004.
- **eps**: p < eps → eps, log2err NA, warning (v7 output, v6 1.30.0).
- **Reproducibility** across back-ends and worker counts (FG5).
- **fgsea's own test suite**: 61 tests, 152 expectations, 0 failures, 2 skipped (reactome.db and
  GEOquery examples not installed) on master and on the patched branch (`../upstream/test-runs.txt`).

## Not audited

`fora` / `collapsePathwaysORA` (read only: `phyper(q - 1, m, n, k, lower.tail = FALSE)` and BH over
all size-filtered sets, which is standard), `collapsePathways` (read only), `fgseaLabel`, GESECA
(`geseca*`, `ScoreRuler`, `ScoreCalculation`), plotting beyond reading `plotEnrichmentData`
(same ranking and `calcGseaStat` as the analysis), Windows/macOS reproducibility (#170), and the
clusterProfiler/DOSE wrappers (covered by the clusterProfiler audit).
