# Component: GSEA enrichment core (`master` @ `dc35c76`, 2025-03-10; = `v4.4.0` + one README commit)

Read in full on `master`: `alg/gsea/KSCore.java` (396 lines, running sum and ES),
`alg/gsea/GeneSetScoringTables.java` (566, hit/miss weights of the four scoring schemes),
`alg/gsea/GeneSetCohort.java` (230, size filter, restriction to the data),
`alg/gsea/KSTests.java` (302, the two permutation drivers), `alg/gsea/Norms.java` (188,
NES), `alg/gsea/PValueCalculatorImpls.java` (153) with `alg/fdr/FdrAlgs.java` (127) and
`objects/strucs/SkewCorrectedFdrStruc.java` (219) (nominal p, FDR, FWER),
`alg/GeneSetGenerators.java` (random gene sets, size filters), `alg/Metrics.java` (331) with
`math/XMath.java` (754) and `math/Vector.java` (929) (ranking metrics, the minimum-sigma
rule, p-value counts), `alg/DatasetGenerators.java` (collapse), `alg/DatasetMetrics.java`,
`math/DoubleElement.java` (sort/tie order), `objects/TemplateFactoryRandomizer.java`
(phenotype permutation), and the tool classes `xtools/gsea/{AbstractGseaTool,
AbstractGsea2Tool,Gsea,GseaPreranked}.java` for parameters and defaults. Line numbers below
are on `dc35c76`; every finding was **executed on the shipped code**: the jar built from
`dc35c76` with the repository's Gradle build (Java 17 target, run on OpenJDK 25.0.4) through
its own command-line entry points (`xtools.gsea.GseaPreranked`, `xtools.gsea.Gsea`, as
`gsea-cli.sh` does), plus the class trees compiled with `javac` from the `v4.4.0`, `v4.3.2`,
`v4.1.0` and `v4.0.3` tags. Reference: an independent numpy port written from Subramanian
et al. 2005 (`../verify/gsea_port.py`) and, for the ES, `fgsea` 1.39.4 built from its GitHub
source on R 4.3.3. Harnesses and captured output in `../verify/`.

Terminology: p is the exponent of the weighting scheme (`classic` p = 0, `weighted` p = 1
default, `weighted_p1.5`, `weighted_p2`); N the list length, N_H the set's members present
in the list, N_R = Σ|r|^p over those members.

## Findings

### GS1 — CONFIRMED on `master`/4.4.0/4.3.2 (4.1.0 and 4.0.3 carry a different form of the same defect): `weighted_p1.5` gives every gene-set member with a negative ranking score a hit weight of 1e-6

**Code.** `GeneSetScoringTables.java:202-235` (`WeightedOnePointFive`). The constructor
(line 210) builds the normaliser from `Math.pow(Math.abs(score), 1.5)`; `getHitScore`
(line 228) computes `Math.pow(score, 1.5)` on the signed score, which is NaN for a negative
score, and line 230 replaces the NaN by `0.000001f`. The hit weights of a set therefore no
longer sum to one: members on the negative side of the list add 1e-6 to the running sum
instead of |r|^1.5 / N_R. `Weighted` (line 137, `_abs`) and `WeightedSquared` (line 183,
`score * score`) are sign-symmetric. The 4.1.0 and 4.0.3 trees have `Math.pow(score,
0.5)` for the hit and `Math.pow(score, 1.5)` (no absolute value) for the normaliser
(`git log -S`: changed by `6c3aa77`, 2021-12-14, "fixed weighted_p1.5 bugs", first in
4.2.0), so there the scheme is wrong for every set, not only the negative-side members.

**Verified** (`../verify/gs1_weighted_p15_negative_scores.py`; 3,000-gene list, 1,576
negative scores, eight planted sets, 1,000 gene-set permutations; the port computes ES from
the |r|^p definition on the same list):

| set (weighted_p1.5) | GSEA ES `master` | port ES | GSEA ES 4.1.0 / 4.0.3 |
|---|---|---|---|
| TOP_40 | 1.00000 | 1.00000 | −1.10357 |
| BOTTOM_40 | −1.00000 | −1.00000 | −1.50000 |
| BOTTOM_100_SPREAD | −0.99990 | −0.82759 | −1.49990 |
| NEG_SIDE_RANDOM_80 | −0.99992 | −0.60865 | −1.49992 |
| RANDOM_100 | −0.45441 | +0.26989 | −1.49990 |
| max \|GSEA − port\| over 8 sets | **0.724** | | **2.18** |
| same sets, `weighted_p2` / `weighted` | 1.95e-7 / 1.54e-7 | | 1.95e-7 / 1.54e-7 |

The NES, p and FDR built on the wrong ES follow it (RANDOM_100: NES −0.87 instead of a
positive NES). The MCVE in `../upstream/mcve_gs1_weighted_p15.sh` (12 genes, set {g, i, k}
scored −1, −3, −5) reports ES −0.999997 for a true −0.7202; with the patch it reports
−0.7202288 (`../upstream/mcve_outputs.txt`). Same numbers on the `v4.4.0` and `v4.3.2`
builds (`.v4.4.0.out`, `.v4.3.2.out`); with patch 0001 every set matches the definition to
2e-7 (`.patched.out`).

**Exposure.** A documented option, not the default; 6 of the 720 cohort papers state a
scoring scheme at all (lower bound). Anyone who chose `weighted_p1.5` got wrong scores for
every set with members on the negative side — in the 4.0/4.1 era for every set.

**Fix.** `Math.pow(Math.abs(score), 1.5)` in `getHitScore` (patch 0001 with
`GeneSetScoringTablesTest`).

### GS2 — CONFIRMED on `master`, 4.4.0, 4.3.2, 4.1.0 and 4.0.3: `-set_min` equal to `-set_max` disables the gene-set size filter, and a set with an identifier absent from the data then aborts the run

**Code.** `GeneSetCohort.java:185-204`, `Generator.filterGeneSetsByMembersAndSize`:

```java
if (geneSetMinSize != geneSetMaxSize) {
    gsets = GeneSetGenerators.removeGeneSetsSmallerThan(gsets, geneSetMinSize, rl);
    gsets = GeneSetGenerators.removeGeneSetsLargerThan(gsets, geneSetMaxSize, rl);
} else { // @note hack
    log.info("Skipped gene set size filtering: max and min thresholds are equal");
}
```

The parameters are described (`AbstractGseaTool.java:25-26`) as "Gene sets smaller/larger
than this number are EXLCUDED from the analysis". The skipped calls are also the only place
where each set is restricted to the identifiers present in the ranked list
(`GeneSetGenerators.java:61-80`, `cloneDeep(rl)`); without it `Weighted.<init>`
(`GeneSetScoringTables.java:119`) asks the ranked list for the score of an absent member and
`DefaultRankedList.getScore` throws `IllegalArgumentException: No such name`.

**Verified** (`../verify/gs2_set_min_equals_max.py`; 2,000-gene list; sets of size 5, 20,
20 and 900; 200 permutations):

| run | sets analysed | notes |
|---|---|---|
| `-set_min 20 -set_max 21` (control) | SIZE_20_RANDOM, SIZE_20_TOP | SIZE_20_RANDOM: NES 1.165, FDR 0.264 |
| `-set_min 20 -set_max 20` | SIZE_20_RANDOM, SIZE_20_TOP, **SIZE_5, SIZE_900** | SIZE_20_RANDOM: NES 1.144, FDR 0.325 (the FDR is computed over the wrong collection) |
| `-set_min 15 -set_max 15` (no set of that size) | the same four | expected "After pruning, none of the gene sets passed size thresholds" |
| `-set_min 20 -set_max 21`, one set with 5 absent ids | three sets, SIZE_20_WITH_ABSENT restricted to 20 | |
| `-set_min 20 -set_max 20`, the same file | **run fails: `No such name: NOT_IN_LIST_0`** | |

Identical on the four release builds (`.v4.*.out`). With patch 0002 the equal-thresholds runs
keep the two size-20 sets, `-set_min 15 -set_max 15` raises the "none of the gene sets
passed" error, and the absent-identifier collection runs (`.patched.out`). The MCVE in
`../upstream/mcve_gs2_set_min_equals_max.sh` (30 genes, sets of 5/10/20) shows the same.

**Exposure.** A rare parameter choice (2 cohort papers state size limits at all); when
chosen with an MSigDB collection the run fails rather than mis-reporting, and when every
identifier happens to be present the whole collection is analysed. Recorded as a wrong
number under a documented option, held.

**Fix.** Run the two filters unconditionally (patch 0002 with `GeneSetCohortGeneratorTest`).
If the equal-thresholds branch was meant as a "no size filter" switch, it still needs the
restriction to the ranked list and a sentence in the parameter description.

### GS3 — CONFIRMED on `master`, 4.4.0, 4.3.2 (4.1.0 and 4.0.3 with a different wrong value): a gene set whose present members all have score 0 gets a spurious ES/NES and p-value under the default `weighted` scheme

**Code.** `GeneSetScoringTables.java:135-139`: the hit weight is `|score| / totalWeight`;
with every member at score 0, `totalWeight` is 0 and the weight is NaN. `KSCore.java:175-176`
adds it to the running sum, which is NaN from the first hit on; the comparisons at lines
162 and 187 (`Math.abs(ess_maxdev[g]) < Math.abs(runningScores[g])`) are false against NaN,
so `ess_maxdev` keeps the value recorded at line 163 just before the first hit:
−(rank of the first member) / (N − N_H). That ES is then normalised, compared with the
set's permutation null (random sets have ordinary weights and finite ES) and reported with
NES, p, FDR and FWER. No warning: `checkRankedListForInfinityOrNaN` (`KSTests.java:297`)
looks at the ranking scores, not at the weights, and the report's NaN check
(`EnrichmentReports.java:186-192`) sees a finite ES. The 4.1.0/4.0.3 `KSCore` handles the
NaN differently and reports ES = −1.0 for the same set.

**Verified** (`../verify/gs3_zero_weight_set.py`; 5,000-gene list with 1,500 zeros (30 %)
between the positive and the negative block, 1,000 gene-set permutations):

| set (weighted) | GSEA ES | = −rank_first/(N−N_H) | NES | NOM p | FDR | port |
|---|---|---|---|---|---|---|
| ALL_ZERO_20 (start of the zero block) | −0.4418 | −2200/4980 = −0.4418 | −1.112 | 0.285 | 0.327 | undefined (0/0) |
| ALL_ZERO_40_LATE (end of the block) | −0.7056 | −3500/4960 = −0.7056 | −2.020 | 0.000 | 0.000 | undefined |
| ZERO_19_PLUS_1 (one member scored 0.001) | 0.5785 | | 1.351 | 0.085 | | 0.5785 |
| on 4.1.0 / 4.0.3: ALL_ZERO_20 | −1.0000 | | −2.517 (−2.862 for the 40-gene set) | 0.000 | | |

ALL_ZERO_40_LATE has the second most negative NES of the run, after the planted BOTTOM_30
(−2.78). Under `classic` the same sets get the defined, position-dependent ES the port
also computes (ALL_ZERO_20: +0.5582, ALL_ZERO_40_LATE: −0.7056). With patch 0003 the
weighted run gives those classic values (ALL_ZERO_20: ES 0.5582, NES 1.287, p 0.125) and
logs a warning (`gs3_zero_weight_set.patched.out`). The MCVE in
`../upstream/mcve_gs3_zero_weight_set.sh` (40 genes, a 12-member all-zero set) reports
ES −5/28 = −0.1786 with p and FDR where the classic value is +0.8214
(`../upstream/mcve_outputs.txt`).

**Exposure.** Default scheme, default settings. The input is a preranked list that scores
untested genes 0 (DESeq2/edgeR statistics with NA → 0; fgsea's tie warning fires at such
lists routinely) together with a set of tissue-specific genes that are all unexpressed —
a small fraction of sets, but each one is reported as a (usually negative) hit whose sign
and size are set by where the zeros sit. fgsea 1.39.4 computes the same order-dependent
number for such a set (ZERO_40 in `note_ties.out`: −0.7095 and −0.7973 in both tools) but
prints a tie warning. How often the combination occurs in the cohort cannot be told from
the survey snippets.

**Fix.** Equal scores mean equal weights: return 1/N_H when the total weight is 0 and log a
warning naming the set (patch 0003, `ZeroWeightGeneSetTest`); or exclude such sets with a
warning. Either way a general warning about ties in the ranked list (fgsea has one; GSEA
has none, see N2) would tell users what they are looking at.

### N1 — NOTE (design, verified, small effect): the FDR q-value numerator is a mean of per-permutation fractions, not the pooled fraction of the paper

`SkewCorrectedFdrStruc.java:100-132`: for each permutation column c, GSEA counts
#{S : NES(S,π_c) ≥ NES\*} / #{S : NES(S,π_c) ≥ 0} (columns with no same-sign value are
skipped) and averages the fractions over the columns; the denominator is
(rank of NES\* among the observed same-sign NES + 1) / #observed same-sign sets. The paper
(Methods, "Multiple hypothesis testing") pools all (S, π) pairs. The two agree when every
column has the same number of positive NES values. Measured on GSEA's own null
(`../verify/note_fdr_formula.py`, 120 sets, 1,000 permutations, 80–111 positive NES per
column): report vs the per-permutation formula max |Δq| 4.4e-4 (the `RND_ES` values in
`results.edb` carry 4 decimals); per-permutation vs pooled max |Δq| 0.0012, mean 0.0001;
the same 40 sets under 0.25 and 30 under 0.05 either way. On the 24-set held-up run
(`heldup_preranked_core.out`) the pooled formula differs by up to 0.0039. A design choice
with a small numerical footprint; documented nowhere in the code beyond the comment
"go to every COLUMN of the rnd norm matrix".

Related, same file: the numerator counts null values ≥ NES\* (`XMath.getMoreThanCount`,
`XMath.java:720-731`, breaks at the first strictly smaller value) while the nominal p counts
strictly beyond (`XMath.java:200-249`): strict vs ties-counted p differ by 0 on real-valued
nulls (`note_fdr_formula.out`), and with 1,000 permutations 30 of 120 sets report p = 0.000
exactly (documented GSEA behaviour; no 1/(n+1) floor).

### N2 — NOTE (design, verified): tied ranking scores keep their file order, without a warning

`RankedListParser` sorts the `.rnk` with `DoubleElementComparator` (`DoubleElement.java:87-112`,
returns 0 for equal values) through a stable sort, so tied genes stay in file order. For a
set inside a block of 1,200 genes tied at 0.3 (`../verify/note_ties.py`) the reported ES is
+0.6959 when the block is written one way and −0.6959 when the lines of the
block are reversed; the port on GSEA's order agrees, fgsea 1.39.4 gives the same two numbers
and prints "There are ties in the preranked stats (39.97% of the list). The order of those
tied genes will be arbitrary"; GSEA's log has no line about ties. A set of 40 genes tied at
score 0 is GS3.

### N3 — NOTE (reporting convention, verified): `RANK AT MAX` is counted from the bottom of the list for a negative ES

`GeneSetSignalImpl.java:81-83`: the report column holds the 0-based position of the
extreme for a positive ES and `N − position` for a negative one (`heldup_preranked_core.out`
part C: BOTTOM_15 at position 3,984 of 4,000 is reported as 16). The leading-edge "tags"
percentages are right either way. Not stated in the report; a reader who computes the
position from the running-sum plot gets a different number for negative sets.

### N4 — NOTE (cosmetic, by reading): `USE_BIASED` has no effect on the `tTest` metric

`XMath.tTest` (`XMath.java:671-690`): with `usebiased` the variance is SS/n and the
denominator divides it by n − 1; without, SS/(n − 1) divided by n — the same number. The
preference is not exposed on the command line (`AbstractGsea2Tool.getMetricParams`,
`XPreferencesFactory.kBiasedVar` default false), so nothing reaches users.

### Withdrawn

- *The last gene of the list is scored with the wrong gene-set index.* `KSCore.java:169`
  tests `gcoh.isMember(i, rowName)` with the loop index `i` rather than the set index `g`;
  on the last iteration `genesetIndices[i] == i`, so the two coincide. The ES of every
  set matches the port to 2e-7 on lists where the last gene is and is not a member
  (`heldup_preranked_core.out`).
- *An exactly tied positive and negative extreme.* A 20 + 20 split set under `classic` has
  running-sum extremes of exactly +0.5 and −0.5; GSEA reports −0.50000006 (float rounding
  of the miss penalty), the port +0.5, fgsea another value. A measure-zero tie, resolved
  arbitrarily by every implementation; the harness uses a 20 + 19 split instead.
- *Phenotype-permutation calibration.* On null data (8 vs 10 samples, 100 random sets,
  1,000 permutations) 9 of 100 sets have nominal p < 0.05 under phenotype permutation and
  6 of 100 under gene-set permutation, KS distance from uniform 0.066 (p = 0.75) and 0.058
  (p = 0.87); 2 and 1 sets under FDR 0.25 (`heldup_expression_metrics.out`). Within the
  binomial noise of 100 sets; nothing to report.

## What held up (executed, not just read)

- **Enrichment score, all three sign-symmetric schemes.** On a 4,000-gene list with 24
  planted and random sets (sizes 15–400, three absent identifiers per set), the report's
  ES equals the port's |r|^p running-sum extreme and `fgsea::calcGseaStat(gseaParam = p)`
  to 1.8e-7 (`classic`, 0 exact except the withdrawn tie), 1.8e-7 (`weighted`) and 2.0e-7
  (`weighted_p2`) — float32 arithmetic in Java (`heldup_preranked_core.out`, part A). The
  same on the expression tool's ranked list (`heldup_expression_metrics.out`, part B,
  1.8e-7).
- **NES.** ES divided by the mean of the same-sign part of the set's own null
  (`Norms.java:289-339`, `MeanDivPosNegSeperate`): recomputed from the run's `RND_ES` to
  4.5e-5 (rounding of the stored null).
- **Nominal p, FWER.** p = fraction of the same-sign null strictly beyond the ES
  (`XMath.java:228-249`), FWER = fraction of permutations whose most extreme same-sign NES
  over all sets is beyond the observed NES (`XMath.java:42-75`): 3e-8 and 1e-3 (one
  permutation at the 4-decimal boundary) from the stored null.
- **FDR** equals the per-permutation formula of N1 to 3.4e-4 from the stored null (part B);
  q clipped at 1 and set to 1 when the NES sign disagrees with the ES
  (`PValueCalculatorImpls.java:119-125`).
- **Leading edge and rank at max** agree with the port's running sum for all 24 sets once
  the N3 convention is applied (part C).
- **Gene-set permutation null.** Random sets of the same size drawn from the whole ranked
  list (`GeneSetGenerators.java:23-51`, `randomlySampleWithoutReplacement`); one null per set;
  seed 149 by default, so runs are reproducible (identical NES on `master`, 4.4.0, 4.3.2,
  4.1.0).
- **Phenotype permutation.** `TemplateFactoryRandomizer.java:74-131`: a random permutation
  of the sample labels keeping class sizes (`XMath.randomizeWithoutReplacement`), the
  dataset re-scored with the chosen metric for every permutation (`KSTests.java:138-170`),
  the same size filter and NaN handling as for the real list; NES/p/FDR from the stored
  null to 1.7e-5 / 2.3e-3 / 8.9e-4 on the signal data, planted sets recovered with the
  right signs, calibration as above.
- **Ranking metrics** on a 3,000-gene, 8 vs 10 dataset (`heldup_expression_metrics.out`,
  part A): Signal2Noise (mean difference over the sum of the two standard deviations, ddof
  1), tTest (mean difference over √(s²_A/n_A + s²_B/n_B)), Ratio_of_Classes,
  log2_Ratio_of_Classes (NaN for a negative ratio, as the port), Diff_of_Classes, and
  Signal2Noise with `-median true` (medians in the numerator, standard deviations
  unchanged) equal the port to ≤ 4e-5 absolute (float32 output) and the ranking order is
  the port's order. **The minimum-sigma rule** (`Vector.java:457-468`): σ is floored at
  0.2·|mean|, and at 0.2 when |mean| ≤ 1e-9 (`XMath.isNearlyZero`); 150 planted low-variance
  genes (σ ≈ 0.45, mean 100) and 30 zero-mean genes score exactly as the port with that rule
  (G0260: 0.00414 both; G0370: 0.04376 both).
- **Collapse** (`heldup_collapse.out`): with a `.chip` of 1,500 symbols carried by 1–4
  probes each plus 60 probes marked `---`, all five modes (Max_probe per sample,
  Median_of_probes, Mean_of_probes, Sum_of_probes, Abs_max_of_probes) give ranked-list
  scores equal to metric(collapse(X)) from the port to ≤ 1.3e-6 for Diff_of_Classes and
  Signal2Noise, 1,500 symbols, same order; GSEAPreranked's collapse of a `.rnk` (max /
  median / mean / sum / abs-max of the probe scores) to ≤ 6.3e-7.
- **Gene-set size filter** in the normal case (`min ≠ max`): inclusive on both ends,
  applied after restriction to the ranked list (`GeneSetGenerators.java:53-98`; GS2's
  control runs and `GeneSetCohortGeneratorTest.rangeIsInclusiveAndRestrictsSetsToTheRankedList`).
- **Absent identifiers** in a set (three per set in the held-up run) are dropped before
  scoring and do not enter N_H or N_R.
- **Duplicate identifiers** in a `.rnk` are reported and the first occurrence kept
  (`AbstractGseaTool.uniquize`, by reading only).

## Not audited

Leading-edge analysis (`LeadingEdgeTool`), the continuous-phenotype metrics (Pearson,
Spearman, Cosine, Euclidean, Manhattan), the balanced phenotype permutation modes
(`EQUALIZE_AND_BALANCE`), the `weighted_as` tables (not selectable from the tools), the
marker-selection report (`PermutationTest`), the HTML/plot output, the Cytoscape/Enrichment
Map export, GenePattern module wrappers, chip-file download and MSigDB version handling.
