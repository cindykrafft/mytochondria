# GSEA audit against 720 published papers (2021–2026)

_Generated 2026-09-10 against `GSEA-MSigDB/gsea-desktop` **master** @ `dc35c764`
(2025-03-10). The latest release tag is **v4.4.0** (`2cfcbd98`, 2025-03-03); the only
difference between it and master is `scripts/readme.txt`, so this audit of master is an
audit of the current release. Focus: correctness at master, verified by executing built
jars._

## What this is

The six-journal survey found **720 papers** that used GSEA — the largest cohort in the
survey — for gene-set enrichment on ranked gene lists. Its numeric core (the running
enrichment score and the four scoring schemes, the phenotype and gene-set permutation
nulls, the nominal p-value, the NES, the FDR q-value, the five ranking metrics with the
minimum-standard-deviation rule, the five probe→gene collapse modes, the gene-set size
filter and tie handling) was read in full on master and every suspicion was run through
built jars on synthetic data with planted signal, against an independent numpy port
written from Subramanian et al. 2005 (`verify/ref_gsea.py`) and against `fgsea` 1.39.4
under R 4.3.3.

## Findings (details and line citations in [`component-reviews/statistical-core.md`](component-reviews/statistical-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **GS1** | **CONFIRMED on master, v4.4.0 (current release), v4.3.2, v4.1.0, v4.0.3** | `-scoring_scheme weighted_p1.5` raises the *signed* rank metric to the power 1.5 in `getHitScore` (`GeneSetScoringTables.java:228`) while the normalising total uses `Math.abs` (line 210). `Math.pow(negative, 1.5)` is NaN, so every negatively scored gene contributes the `0.000001f` fallback instead of `|r|^1.5`: the running sum never rises inside a down-regulated set. On a 20-gene MCVE whose exact answer is −12/17 = −0.7058824, `weighted` and `weighted_p2` return −0.7058824 and `weighted_p1.5` returns −0.999997 (−1.499997 on 4.0.3/4.1.0, outside the legal [−1, 1] range). On an 8,000-gene list a random set flips sign, +0.3430 (reference) → −0.3630 (reported). One-line fix; the other three schemes are correct. |
| **GS2** | **CONFIRMED on master, v4.4.0 (current release), v4.3.2, v4.1.0, v4.0.3** | `-set_min N -set_max N` (equal bounds) skips the gene-set size filter entirely instead of selecting the sets of size N (`GeneSetCohort.java:188-197`, `else { // @note hack }`): with sets of sizes 5, 20 and 60 in the GMT, `-set_min 20 -set_max 20` reports all three, each with an NES, a nominal p and an FDR q computed over the wrong family. The skipped branch is also where each set is intersected with the ranked list, so a set with one absent member aborts the run with `java.lang.IllegalArgumentException: No such name: …`. |
| N1 | note, definition, quantified | The FDR numerator averages each permutation's own fraction of more-extreme null NES (`SkewCorrectedFdrStruc.java:120-132`) where Subramanian 2005 pools all (S, π) pairs. Executed: the shipped q matches the code definition to 3.81e-4 and the paper definition to 2.00e-3 (median 2.43e-4) over 41 sets × 1,000 permutations — below the four decimals the `.edb` stores. |
| N2 | note, method property | The ES of a gene set inside a block of tied scores depends on the order of the input file: the same 40-gene tie block written in two orders gave ES −0.3675 (NES −1.045) and −0.6137 (NES −1.745) for the same set; a set spread outside the block was identical in both. |
| N3 | note, cosmetic | When the running sum's positive and negative extremes agree to within float32, GSEA keeps the positive one; 3 of 3,000 null (set, permutation) pairs, no real set affected. |
| N4 | note, documented convention | A nominal p more extreme than all permutations is printed as `0.0`, not `< 1/nperm`; 5 of 41 sets. |

**Held up under execution:** ES and the running sum for `classic`, `weighted` and
`weighted_p2` (max |ΔES| 6.0e-08, 2.0e-07, 1.7e-07 over 41 sets; 0 rank-at-ES and 0
leading-edge mismatches); NES (1.1e-05), nominal p (2.1e-03 = 1/nperm) and FWER
(0.00e+00); the FDR against the code's own definition (3.8e-04); the gene-set permutation
null; the phenotype permutation null (200 of 200 random ranked lists are exact
Signal2Noise rankings under a relabelling, the real labelling not among them, max
|ΔRND_ES| 5.0e-05 over 3,000 pairs); all five ranking metrics against numpy (≤ 3.4e-06,
float32 output precision, NaN handling identical); the 20 %-of-|mean| minimum-SD rule; all
five probe→gene collapse modes (≤ 5.7e-06, 1,125 symbols each); the size filter for
unequal bounds on all five builds; and ES against `fgsea` (4.3e-07, leading edge identical
for 41 of 41 sets). The project's own `XMathTest` and `VectorTest` (54 tests) pass on
master and on both patch branches. Not audited: `weighted_as` (unreachable from
`createAllScoringTables()`), leading-edge *analysis*, plots, ssGSEA, multi-class designs.

## How the papers use GSEA (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| ranked by a DESeq2/limma/edgeR statistic | 315 |
| single-cell / pseudobulk input | 259 |
| GSEA desktop / Broad / MSigDB named | 105 |
| GO / C5 sets | 99 |
| Hallmark gene sets | 96 |
| fgsea also used | 95 |
| clusterProfiler also used | 85 |
| log2 ratio / fold-change ranking | 77 |
| KEGG / Reactome / C2 sets | 61 |
| FDR cutoff quoted | 53 |
| ssGSEA / GSVA | 51 |
| GSEAPreranked / preranked | 41 |
| weighted / classic scoring named | 26 |
| version stated | 24 (4.1.0 ×8, 4.3.2 ×7, 4.0.3 ×7, 4.3.3 ×3, 4.2.3 ×3, 3.0 ×2, 2.2.3 ×2) |
| NES quoted | 18 |
| number of permutations stated | 12 |
| nominal p quoted | 5 |
| collapse / probe / chip | 4 |
| Signal2Noise named | 3 |
| t-test metric named | 3 |
| gene-set permutation named | 1 |
| min/max gene set size stated | 1 |

GS1 and GS2 are both present in every version the cohort names that could be built here
(4.0.3, 4.1.0, 4.3.2) and in the current release 4.4.0. Neither is reachable on default
settings: GS1 needs `-scoring_scheme weighted_p1.5`, GS2 needs `-set_min` equal to
`-set_max`. No cached paper names `p1.5`, and one names min/max set sizes, so the
measurable published exposure of each is small — they are correctness bugs in options the
tool offers without a warning, not silent corruption of the default path (which held up).

**Profiling caveat.** This session had no route to Europe PMC, so `gsea_profile.py` ran in
`--offline` mode over the survey's stored evidence snippets; all 720 records in
`gsea_profiles.jsonl` are `source: survey_cache` and every count above is a lower bound.
Rerun without `--offline` from a host with Europe PMC access to replace them with
full-text records.

## Environment and build

Java is OpenJDK **25.0.4** (the image's `java`; the project targets 21). Master and the
v4.4.0 tag build with the project's own wrapper, **Gradle 8.2.1**: `./gradlew jar` →
`build/libs/gsea-minimal-user.jar`, run as
`java -cp gsea-minimal-user.jar:modules/* xtools.gsea.GseaPreranked …`. The v4.3.2, v4.1.0
and v4.0.3 tags do **not** build with Gradle here (their build scripts fetch plugins this
environment cannot reach), so each was compiled with `javac` against that tag's own
`modules/` and `lib/` jars. **Released binaries could not be downloaded**:
`www.gsea-msigdb.org` and `data.broadinstitute.org` are refused by the proxy (HTTP 403 on
CONNECT) and the GitHub release carries no matching asset (404), so "the current release"
means the v4.4.0 tag built from source. Python 3.11.15 with numpy for the reference port;
R 4.3.3 with fgsea 1.39.4 for the cross-check.

GSEA's file parameters are cut at the first `-` in a path, so the scratch clone is reached
through a dash-free symlink `/tmp/gseawork`; the harnesses use it, and it must exist for
them to run (`ln -s <scratchpad>/gsea /tmp/gseawork`).

## Filing channel (read before anything is sent)

- `CONTRIBUTING.md` (the only contributing document; there is no `.github/` directory, no
  issue or PR template, no changelog file, and **no AI policy**): search the tracker
  first; a bug report needs a title, a clear description and "a code sample, executable
  test case, or clear set of instructions"; **patches are welcome as pull requests**, one
  focused problem per PR, referencing the issue number. `CODE_OF_CONDUCT.md` names
  gsea-team@broadinstitute.org.
- The repository's `README.md` points general questions at the GSEA website contact page;
  the help forum is the right place for usage questions, the tracker for defects. Both
  findings are defects with a reproduction, so both belong on the tracker.
- The tracker is small (16 issues found by search, 2017–2022) and quiet. Searched
  2026-09-10 for both findings under several phrasings: **no prior report of either**.
  Nearest: #5 "Size thresholds" (a different size-filter symptom — all sets pruned away),
  #26 "report sort error", #14 "GSEA 4.0 fails to Infinite values", #42 "Abs.max in
  Collapse Dataset".
- No fork `cindykrafft/gsea-desktop` exists, so there is no
  `upstream-declines-ai-contributions` topic to respect; nothing in the project's
  documents restricts AI-assisted contributions.
- Filing cap is two unanswered filings per repository. **GS1 goes first** (it returns a
  wrong ES, and an out-of-range one on two releases the cohort names); GS2 second.
- **The kit is in [`upstream/`](upstream/)** — two issue texts with MCVEs run on six
  builds, two `git am`-able patches (fix + regression tests that fail on unmodified
  master), and the PR bodies. **Nothing has been filed.**

## Files

| file | what |
|---|---|
| `gsea_profile.py`, `gsea_profiles.jsonl`, `profile_run.log` | profiling pass over the 720-paper cohort (offline; see caveat) |
| `component-reviews/statistical-core.md` | the review: GS1, GS2, N1–N4, held-up list, not-audited list |
| `verify/gsea_cli.py`, `verify/synth.py`, `verify/ref_gsea.py` | harness helpers: write GSEA inputs, run the jar, parse `results.edb` and the report TSVs; synthetic data; the numpy port of the paper |
| `verify/mcve-gs1.sh` (+ `.out`) | GS1 minimal reproduction, one hand-computed expected ES, run on master, the patch, and four release tags |
| `verify/gs1_weighted_p15_negative_hits.py` (+ `.out`, `.v4.*.out`, `.patched.out`) | GS1 at scale: ES, rank-at-ES and NES vs the reference for three schemes on an 8,000-gene list |
| `verify/mcve-gs2.sh` (+ `.out`) | GS2 minimal reproduction, run on master, the patch, and four release tags |
| `verify/gs2_setmin_eq_setmax_skips_filter.py` (+ `.out`, `.v4.*.out`, `.patched.out`) | GS2: five bound pairs × five set sizes, plus the abort on a member absent from the ranked list |
| `verify/heldup_preranked_vs_reference.py` (+ `.out`) | held-up: ES/rank-at-ES/leading edge for `classic`/`weighted`/`weighted_p2`, NES, nominal p, FWER, and FDR against both the code and the paper definitions |
| `verify/heldup_expression_metrics_collapse_phenotype.py` (+ `.out`) | held-up: the five ranking metrics, the minimum-SD rule, the five collapse modes, and the phenotype-permutation null |
| `verify/heldup_fgsea_vs_gsea.R` (+ `.out`) | held-up: ES/NES/leading edge vs fgsea 1.39.4 on the same ranked list |
| `verify/note_ties_input_order.py` (+ `.out`) | N2: the ES of a set inside a tie block under two input orders |
| `verify/unit_tests_before_after.out` | the project's `XMathTest`/`VectorTest` plus the two new test classes, on master and on each patch branch |
| `upstream/` | filing kit: two issue texts, patches 0001 (GS1) and 0002 (GS2) with regression tests, PR bodies, and what was read |

## Next steps

1. File GS1 upstream from the kit (issue, then PR); GS2 after GS1 is answered, to stay
   inside the two-filing cap. Record numbers and maintainer responses here.
2. Re-run the version-scope harnesses against the official binary distributions when a
   host can reach `gsea-msigdb.org`, to confirm the released jars match the tags.
3. Extend the review to the leading-edge analysis tool and to multi-class phenotype
   designs, the two core paths this audit left unchecked.
4. Full-text profiling rerun when Europe PMC is reachable.
