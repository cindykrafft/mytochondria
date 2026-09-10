# Component: GSEA statistical core (`master` @ `dc35c764`, 2025-03-10)

Repository `GSEA-MSigDB/gsea-desktop`, default branch **master**, HEAD
`dc35c7642d93fabc3223f1db5f844b0f1cadbdc2`. The latest release tag is **v4.4.0**
(`2cfcbd98`, 2025-03-03); `git diff v4.4.0 master` touches one file, `scripts/readme.txt`,
so for every path in this review **master and the current release are byte-identical**.

Read in full on master: `edu/mit/broad/genome/alg/gsea/GeneSetScoringTables.java` (the
four scoring schemes), `KSCore.java` (the running sum and the ES), `KSTests.java`,
`GeneSetCohort.java` (the size filter), `PValueCalculatorImpls.java` (NES, nominal p,
FWER, FDR dispatch), `edu/mit/broad/genome/alg/fdr/FdrAlgs.java` and
`objects/strucs/SkewCorrectedFdrStruc.java` (the FDR q-value),
`edu/mit/broad/genome/math/XMath.java` (p-value, FWER, median/mean/max helpers),
`edu/mit/broad/genome/alg/Metrics.java` and `DatasetStatsCore.java` (the ranking metrics
and the minimum-standard-deviation rule), `DatasetGenerators.java` (probe→gene
collapsing), `alg/GeneSetGenerators.java`, `xtools/gsea/AbstractGseaTool.java`,
`AbstractGsea2Tool.java`, `GseaPreranked.java`.

**Everything below was executed on built jars**, not inferred: master and the v4.4.0 tag
built with the project's own Gradle 8.2.1 wrapper (`./gradlew jar`, OpenJDK 25.0.4;
`gsea-minimal-user.jar` + `modules/`), and the v4.3.2, v4.1.0 and v4.0.3 tags compiled
with `javac` against each tag's own `modules/` and `lib/` (their Gradle builds need
plugins this environment cannot fetch). Runs are `java -cp <jar> xtools.gsea.GseaPreranked`
and `xtools.gsea.Gsea` with `-gui false`; every number read back comes from the files the
run wrote (`edb/results.edb`, `gsea_report_for_*.tsv`, `ranked_gene_list_*.tsv`).
The independent reference is `../verify/ref_gsea.py`, a numpy port written from
Subramanian et al. 2005 (PNAS 102:15545) and its supplement, and — for ES/NES on the same
ranked list — `fgsea` 1.39.4 under R 4.3.3.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### GS1 — CONFIRMED on master, v4.4.0 (current release), v4.3.2, v4.1.0 and v4.0.3: `-scoring_scheme weighted_p1.5` does not count genes with a negative rank metric as hits

**Code.** `GeneSetScoringTables.WeightedOnePointFive` (`GeneSetScoringTables.java:191-235`).
The constructor normalises with the absolute value (line 210):

```java
float score_pow = (float) Math.pow(Math.abs(score), 1.5);
totalWeight_sq += Float.isFinite(score_pow) ? score_pow : 0.000001f;
```

but `getHitScore` does not (lines 226-231):

```java
public float getHitScore(String name) {
    float score = rankedList.getScore(name);
    float ss = (float) Math.pow(score, 1.5);          // <-- signed base
    float hitScore = ss / totalWeight_sq;
    return Float.isFinite(hitScore) ? hitScore : 0.000001f;
}
```

`Math.pow` of a negative base and a non-integral exponent is `NaN`, so for every gene with
a negative rank metric `hitScore` is `NaN` and the method returns the fallback
`0.000001f`. The two halves of P_hit therefore disagree: the denominator counts the
negative genes at `|r|^1.5`, the numerator gives them ~0. The running enrichment score
never rises inside a gene set that sits on the negative side of the ranked list, so the
sum simply falls to the end of the list. The sibling schemes are correct: `Weighted` uses
`_abs(score)` in both places (lines 120, 137) and `WeightedSquared` squares, which is
sign-safe (lines 165, 183). Subramanian et al. 2005 defines P_hit with `|r_j|^p`.

`weighted_p1.5` is a first-class option: `createAllScoringTables()` (line 18) puts it in the
"Enrichment statistic" combo box of the desktop GUI and it is accepted by
`-scoring_scheme` on both command-line tools (`Param.SCORING_SCHEME`,
`GeneSetScoringTableReqdParam:26-29`, `GseaWrapper.java:46`, `GseaPrerankedWrapper.java:44`).
Nothing in the parameter's help text ("The statistic used to score hits (gene set members)
and misses (non-members)") warns about it.

**Verified — MCVE** (`../verify/mcve-gs1.sh`, output `mcve-gs1.out`). 20 genes with scores
10 … 1, −1 … −10; one gene set of the three genes at ranks 12–14. Exactly one number is
determined by hand: the running sum falls by 1/(20−3) per miss, so it bottoms out at rank
11, just before the first member, at −12/17 = −0.7058824, whatever `p` is (those three
genes carry all the hit weight under every weighted scheme). Same script, six builds:

| build | ES(weighted) | ES(weighted_p2) | ES(weighted_p1.5) |
|---|---|---|---|
| master `dc35c764` | −0.7058824 | −0.7058824 | **−0.999997** |
| v4.4.0 (current release) | −0.7058824 | −0.7058824 | **−0.999997** |
| v4.3.2 | −0.7058824 | −0.7058824 | **−0.999997** |
| v4.1.0 | −0.7058824 | −0.7058824 | **−1.499997** |
| v4.0.3 | −0.7058824 | −0.7058824 | **−1.499997** |
| master + patch 0001 | −0.7058824 | −0.7058824 | −0.7058824 |

The `−1.5` in 4.0.3/4.1.0 is the same defect before the `Float.isFinite` guard was added:
there the `NaN` reached the running sum and the reported ES left the legal [−1, 1] range
altogether. Shrinking the example showed that the data do not matter — any ranked list
with negative scores and any set containing a negatively scored gene reproduces it — and
that `weighted` and `weighted_p2` are unaffected, which is what points at the exponent.

**Verified — full comparison against the reference port**
(`../verify/gs1_weighted_p15_negative_hits.py`, outputs `.out`, `.v4.*.out`, `.patched.out`).
8,000-gene synthetic ranked list, four planted sets, `nperm` 1000, seed 149:

| set (master) | ES reported | ES from `ref_gsea.py` | rank-at-ES reported / reference | NES reported |
|---|---|---|---|---|
| DOWN_MID (all members negative) | −1.0000 | −0.8225 | 7999 / 6546 | −1.907 |
| MIXED | −0.5334 | −0.5004 | 7999 / 7716 | −1.013 |
| RANDOM | **−0.3630** | **+0.3430** | 7999 / 1033 | −0.692 |
| UP_MID (all members positive) | 0.8271 | 0.8271 | 1415 / 1415 | 1.948 |

RANDOM changes sign: a set the paper's algorithm calls weakly enriched at the top of the
list is reported as depleted. Under `weighted` and `weighted_p2` all four sets match the
reference exactly (max |ΔES| 2.0e-7 over the same runs). With patch 0001 all four match
under `weighted_p1.5` too (0 mismatching pairs; DOWN_MID −0.8225, NES −2.473).

**Who is exposed.** Only runs that select `weighted_p1.5`; `weighted` (the default),
`classic` and `weighted_p2` are correct. 26 cohort papers mention a weighted or classic
scoring scheme; none of the 720 names `p1.5` in the cached evidence, so the published
exposure we can measure is zero — but the option is one click away in the GUI and is
silently wrong for anyone who takes it, and 4.0.3/4.1.0 return an out-of-range ES.

### GS2 — CONFIRMED on master, v4.4.0 (current release), v4.3.2, v4.1.0 and v4.0.3: `-set_min N -set_max N` turns the gene-set size filter off instead of selecting sets of size N

**Code.** `GeneSetCohort.Generator.filterGeneSetsByMembersAndSize`
(`GeneSetCohort.java:185-204`):

```java
if (geneSetMinSize != geneSetMaxSize) {
    gsets = GeneSetGenerators.removeGeneSetsSmallerThan(gsets, geneSetMinSize, rl);
    gsets = GeneSetGenerators.removeGeneSetsLargerThan(gsets, geneSetMaxSize, rl);
} else { // @note hack
    log.info("Skipped gene set size filtering: max and min thresholds are equal");
}
```

Equal bounds are the one case in which the filter is most specific — "give me the sets of
exactly this size" — and it is the one case that is skipped. Every set in the GMT is then
scored and reported with an ES, an NES, a nominal p, an FDR q and an FWER p. The only
trace is an INFO log line; the report gives no warning, and the `.rpt` file still records
the thresholds the user asked for. The documented meaning of the parameter is a filter
("Gene sets smaller than this number are EXLCUDED from the analysis",
`AbstractGseaTool.java:25`).

The skipped branch is also where each set is intersected with the ranked list:
`removeGeneSetsSmallerThan(gsets, min, rl)` calls `GeneSet.cloneDeep(rl)`
(`GeneSetGenerators.java:61-80`). With equal bounds that intersection never happens, so a
set with a member absent from the ranked list reaches the scoring table, which asks the
list for that gene's score, and the run dies.

**Verified — MCVE** (`../verify/mcve-gs2.sh`, output `mcve-gs2.out`). 200-gene ranked list,
three sets of sizes 5, 20 and 60, run twice:

| build | `-set_min 5 -set_max 60` | `-set_min 20 -set_max 20` |
|---|---|---|
| master `dc35c764` | SET_5 (5), SET_20 (20), SET_60 (60) | SET_5 (5), SET_20 (20), SET_60 (60) |
| v4.4.0 (current release) | same | SET_5 (5), SET_20 (20), SET_60 (60) |
| v4.3.2 / v4.1.0 / v4.0.3 | same | SET_5 (5), SET_20 (20), SET_60 (60) |
| master + patch 0002 | same | **SET_20 (20)** |

**Verified — the wider harness**
(`../verify/gs2_setmin_eq_setmax_skips_filter.py`, outputs `.out`, `.v4.*.out`,
`.patched.out`). 4,000-gene ranked list, sets of sizes 5, 15, 20, 100, 600. On all five
builds `-set_min 20 -set_max 500` and `-set_min 20 -set_max 100` report exactly the two
sets in range, while `-set_min 20 -set_max 20`, `-set_min 100 -set_max 100` and
`-set_min 5 -set_max 5` each report all five sets. Part B adds a set with one member
absent from the ranked list: `-set_min 20 -set_max 500` trims it and runs; on every build
`-set_min 20 -set_max 20` aborts with
`java.lang.IllegalArgumentException: No such name: NOT_IN_LIST` and writes no report. With
patch 0002 all five bound pairs report exactly the sets in range and part B runs to
completion.

**Who is exposed.** Only runs with `-set_min` equal to `-set_max` (defaults are 15 and
500). One cohort paper states min/max set sizes. This is a small population, but the
failure is silent: an FDR q-value computed over a different, larger family of sets than
the user asked for is a wrong published number, and the size filter is the one parameter
GSEA's own documentation tells users to think about.

## Notes (design, documentation, cosmetic — not wrong numbers at master)

### N1 — the FDR numerator averages per-permutation fractions; the paper pools them

`SkewCorrectedFdrStruc` (`objects/strucs/SkewCorrectedFdrStruc.java:100-141`) walks each
permutation column, computes that column's own fraction
`#{NES(S,π) ≥ NES*} / #{NES(S,π) ≥ 0}` (`col_mean`, line 120), sums those fractions and
divides by the number of non-empty columns (line 132) — a mean of ratios. Subramanian et
al. 2005's supplement defines the numerator as one pooled fraction over all (S, π) pairs —
a ratio of sums. The denominator matches the paper: the observed fraction
`(rank + 1) / #same-sign sets` (lines 91, 134-140). Columns with no same-sign NES are
skipped, and the result is clipped to 1 (and a NaN turned into 1) by the caller,
`PValueCalculatorImpls.java:113-124`. Executed
(`../verify/heldup_preranked_vs_reference.py`, 41 sets, 1,000 permutations): the shipped
FDR matches the code definition to **3.81e-4** and the paper definition to **2.00e-3**
(median 2.43e-4), so on data of this shape the two conventions agree to within the four
decimals the `.edb` stores. Recorded as a note, not a finding: the difference is real but
sub-rounding here, and it is a definition choice, not an error.

### N2 — the enrichment score of a tie block depends on the order of the input file

`KSCore` walks the ranked list in its stored order and GSEA keeps equal scores in the
order they arrive (file order for `.rnk`, row order for a `.gct` metric). Executed
(`../verify/note_ties_input_order.py`, output `note_ties_input_order.out`): a 40-gene tie
block was written in two orders; the set drawn from the early part of the block scored
ES −0.3675 (NES −1.045) in one and −0.6137 (NES −1.745) in the other — Δ|ES| 0.2462 — and
the set spread outside the block was identical (−0.2884) in both. Under the paper's
definition the ES of a set inside a tie block is not defined by the score vector alone, so
this is not a wrong number; it is a property of the method that GSEA does not warn about.
The same order-preservation was confirmed on the expression path (19–21 tied adjacent
pairs kept in row order for every metric,
`heldup_expression_metrics_collapse_phenotype.out` section A).

### N3 — the sign of the ES when the running sum's two extremes are equal to within float32

`KSCore` accumulates the running sum in `double` but keeps the extremum in a `float` and
replaces it only on a strict increase in absolute value
(`KSCore.java:187-188`, "`@note abs here` / `@note no abs here!`"), so the first of two
equally extreme deviations wins. Executed: over 3,000 (set, permutation) pairs on the
phenotype-permutation path, 3 pairs had `max + min = −2.6e-14` — a difference below float32
resolution — and GSEA reported +0.4811 / +0.4838 / +0.4805 where the float64 numpy port,
which sees the negative extreme as marginally larger and reached first, takes the negative
(`heldup_expression_metrics_collapse_phenotype.out` section C). Three in three thousand,
only in null permutations of a deliberately low-variance set, and no real set was affected;
cosmetic.

### N4 — a nominal p of 0 is printed as `0.0`, not as `< 1/nperm`

`XMath.getPValueTwoTailed_pos_neg_seperate` (`XMath.java:228-249`) counts strictly more
extreme same-sign null values with no `+1` correction, so a set more extreme than all of
its 1,000 permutations gets exactly 0. Executed: 5 of 41 sets reported p = 0
(`heldup_preranked_vs_reference.out` section B). This is the documented GSEA convention and
matches the reference port to 2.07e-3 (= 1/nperm, the granularity), so it is recorded, not
filed.

## What held up (executed, not just read)

Everything in this section was run on the master build and compared against
`../verify/ref_gsea.py` or `fgsea`, on synthetic data with planted signal.

- **The running sum and the enrichment score.** `classic` (p = 0), `weighted` (p = 1, the
  default) and `weighted_p2` over 41 gene sets on an 8,000-gene list: max |ES − reference|
  **6.02e-08**, **1.98e-07** and **1.73e-07**; **0** mismatches in rank-at-ES and **0** in
  the leading-edge gene lists (`heldup_preranked_vs_reference.out` section A).
- **NES, nominal p, FWER.** max |ΔNES| **1.07e-05** (the reference is rebuilt from the
  4-dp `RND_ES` the tool stores), max |Δp| **2.07e-03** = 1/nperm, max |ΔFWER| **0.00e+00**
  (section B).
- **FDR q-value.** Matches the code's own definition to **3.81e-4** and the paper's to
  **2.00e-3** (see N1). Calibration: the four planted sets all got q = 0, and 3 of 36
  random sets fell under q < 0.25 (section C).
- **Gene-set permutation null.** Null ES range [−0.7044, 0.6731] over 1,000 permutations
  per set, sizes 15–300 (section C).
- **Phenotype permutation.** 200 saved random ranked lists were checked to be exact
  Signal2Noise rankings under a relabelling of the 8 + 8 samples — **200 of 200**, 198
  distinct relabellings, and the real labelling was **not** among them, i.e. the
  permutation null is a genuine label permutation. max |RND_ES − reference| **5.00e-05**
  (the 4-dp storage) over 3,000 (set, permutation) pairs
  (`heldup_expression_metrics_collapse_phenotype.out` section C).
- **The ranking metrics**, against numpy on a 3,000 × 16 dataset: Signal2Noise,
  tTest, Ratio_of_Classes, log2_Ratio_of_Classes, Diff_of_Classes — max absolute
  differences 1.30e-07, 4.29e-07, 3.36e-06, 6.38e-07, 3.13e-07, all at float32 output
  precision, with identical non-finite counts and NaN placed last (section A).
- **The minimum-standard-deviation rule.** `Vector.stddev(biased, fixlow)`
  (`math/Vector.java:457-468`) floors each class's SD at `0.20 * |mean|`, or at 0.20 when
  the mean is nearly zero; `DatasetStatsCore.java:154-156` passes `fixlow` for the
  two-class metrics. On a planted block with SD 0.01 and mean 5 the floor is 1.0 per
  class and the observed S2N range was [−0.0042, 0.0054], inside the ±0.02 the floor
  allows; a constant block scored exactly 0.0 rather than dividing by zero (section A).
- **Probe→gene collapsing**, all five modes, against a pandas groupby on the same
  probe→symbol map: Max_probe, Median_of_probes, Mean_of_probes, Sum_of_probes,
  Abs_max_of_probes — 1,125 symbols each (the expected count) and max differences 9.50e-07,
  8.84e-07, 1.13e-06, 5.66e-06, 9.50e-07, with no NaN introduced (section B).
- **The gene-set size filter for unequal bounds** — the normal case — keeps exactly the
  sets whose in-list size lies in range, on all five builds
  (`gs2_setmin_eq_setmax_skips_filter*.out` part A, first two rows of each).
- **`fgsea` cross-check.** Same 8,000-gene ranked list, same 41 sets, fgsea 1.39.4 under
  R 4.3.3: max |ES_fgsea − ES_gsea| **4.27e-07**, sizes equal, NES sign agreement 41 of 41
  (max |ΔNES| 0.092, different null construction), and the leading-edge gene sets identical
  for **41 of 41** (`heldup_fgsea_vs_gsea.out`).
- **The project's own unit tests.** `XMathTest` and `VectorTest` (54 tests) pass on master
  and on both patch branches (`unit_tests_before_after.out`).

## Not audited

- The `weighted_as` / `WeightedDoubleSidedAs` scoring table
  (`GeneSetScoringTables.java:239-400`): it is not reachable from
  `createAllScoringTables()`, so no CLI or GUI run can select it. Read only.
- Leading-edge *analysis* (the `LeadingEdgeTool` clustering and its heat maps), the
  Enrichment Map export, and every plot.
- `xtools.gsea.GseaPreranked`'s `-norm meandiv` alternatives beyond the default, and the
  `Chip2Chip`/`CollapseDataset` tools as tools (the collapsing *algorithm* was checked).
- ssGSEA (not in this repository), the MSigDB content, and the GenePattern module
  wrappers beyond confirming they pass `-scoring_scheme` through.
- Multi-class (`.cls` with more than two classes) and the `-permute phenotype` path with
  unbalanced or very small designs (8 + 8 only).
- Memory/threading behaviour and anything about file parsing beyond what the harnesses
  exercise.
