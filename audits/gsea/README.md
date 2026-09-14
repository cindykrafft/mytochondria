# GSEA audit against 720 published papers naming GSEA (2021–2026), 69 of which identify the desktop application

_Generated 2026-09-13 against `GSEA-MSigDB/gsea-desktop` `master` @ `dc35c76` (2025-03-10;
the `v4.4.0` release tag `2cfcbd9` plus one README-only commit, so `master` is the current
release). Focus: the numbers in the GSEA report — enrichment score, NES, nominal p, FDR
q-value, FWER, the ranking metrics and probe collapsing that feed them — verified by
executing the shipped program on synthetic data with planted signal._

## What this is

**Which GSEA (attribution pass, 2026-09-13).** "GSEA" names a method as well as this program.
Classing each of the 720 papers by its evidence sentences and co-named packages
([`survey/scripts/attribute.py`](../../survey/scripts/attribute.py), table in
[`survey/README.md`](../../survey/README.md#attribution-to-a-repository)): **69** identify the
desktop application (name, `gsea-msigdb.org/gsea` URL, "Broad", or a stated version 2.x–4.x,
which only it has), 233 name another implementation (`fgsea`, `clusterProfiler`, GSVA/ssGSEA,
GSEApy, web tools) and 418 name only the method. The exposure this audit can claim for
`GSEA-MSigDB/gsea-desktop` is therefore 69 papers, not 720; the fgsea and clusterProfiler
routes are covered by the [clusterProfiler + fgsea audit](../clusterprofiler/). Of the 27
stated versions, 24 exist as tags of this repository; the three that do not (2.0, 2.2.3 ×2)
are the closed-source javaGSEA 2 line that predates it.

The six-journal survey found **720 papers** in PNAS (469), *Nature* (199), *Cell* (35),
*Science* (16) and *NEJM* (1), 2021–2026, that report a GSEA. The survey's package name
covers the method; at least 90 of the papers ran `fgsea` and 85 `clusterProfiler` for it,
55 name the Broad/UCSD desktop application or `javaGSEA`, 41 say "pre-ranked", and 23 state
a desktop version (4.3.x 10, 4.1.0 8, 4.0.3 7, 4.2.x 4, 3.x 3; lower bounds, see the
profiling caveat). The desktop application's enrichment core — the running-sum enrichment
score under its four weighting schemes, the gene-set and phenotype permutation nulls, the
NES, nominal p, FDR and FWER, the size filter, the ranking metrics (signal-to-noise with its
minimum-sigma rule, t-test, ratio and log2 ratio of classes, difference of classes) and
probe-to-gene collapsing — was read in full on `master` and every suspicion was run through
the program itself: the jar built from `dc35c76` with the repository's Gradle build, driven
through `xtools.gsea.GseaPreranked` and `xtools.gsea.Gsea` exactly as `gsea-cli.sh` does,
and the class trees compiled from the `v4.4.0`, `v4.3.2`, `v4.1.0` and `v4.0.3` tags (the
cohort's most-cited versions; the pre-built binaries are behind a host this session cannot
reach). The reference is an independent numpy port written from Subramanian et al. 2005
(`verify/gsea_port.py`) and, for the enrichment score, `fgsea` 1.39.4 (built from its GitHub
source on R 4.3.3; CRAN/Bioconductor are unreachable here).

## Findings (details and line citations in [`component-reviews/enrichment-core.md`](component-reviews/enrichment-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **GS3** | **CONFIRMED on `master`, 4.4.0, 4.3.2**; 4.1.0 and 4.0.3 report a different wrong value | **now** | Under the default `weighted` scheme a gene set whose members present in the list all have ranking score 0 has a total weight of 0, its hit weight is 0/0 = NaN, the running sum turns NaN at the first hit and `KSCore`'s comparisons against it are all false: the reported ES is the running sum just before the first hit, −(rank of first member)/(N − N_H), and it goes on to get an NES, nominal p, FDR and FWER from a null it cannot belong to, with no warning. On a 5,000-gene list with 30 % zeros (a DESeq2/edgeR list with untested genes at 0) a 40-gene all-zero set is reported at ES −0.7056, NES −2.02, p = 0.000, FDR = 0.000 — the second most negative NES of the run — and a 20-gene one at ES −0.4418, p 0.285; 4.1.0/4.0.3 give ES −1.0, NES −2.5, p = 0 for both. `classic` is unaffected; fgsea computes the same order-dependent number but warns about ties. Patch: equal weights (the p → 0 limit) plus a warning. |
| **GS1** | **CONFIRMED on `master`, 4.4.0, 4.3.2**; 4.1.0 and 4.0.3 carry the earlier form of the defect | held | `-scoring_scheme weighted_p1.5` computes `Math.pow(score, 1.5)` on the signed score in `getHitScore` (NaN for a negative score, replaced by 1e-6) while the normaliser uses |score|^1.5, so every gene-set member with a negative ranking metric adds 1e-6 to the running sum instead of |r|^1.5/N_R. On a 3,000-gene list: a 100-gene set spread over the bottom fifth reported at ES −0.9999 for a true −0.8276, an 80-gene negative-side set at −0.9999 for −0.6087, a random 100-gene set at −0.4544 for +0.2699 (sign flip; NES −0.87); positive-side sets and the `weighted`/`weighted_p2` schemes match the definition to 2e-7. 4.1.0/4.0.3 used `Math.pow(score, 0.5)` for the hits (fixed to 1.5 in 4.2.0 by `6c3aa77`, "fixed weighted_p1.5 bugs") and are wrong for every set (max |Δ| 2.18). One-line fix. |
| **GS2** | **CONFIRMED on `master`, 4.4.0, 4.3.2, 4.1.0, 4.0.3** | held | With `-set_min` equal to `-set_max` the size filter is skipped entirely (`// @note hack`): `-set_min 20 -set_max 20` analyses sets of size 5, 20, 20 and 900 alike (the parameters are documented as excluding sets outside the range), the FDR is computed over that collection, and because the skipped branch is also where sets are restricted to the identifiers in the data, a set with an absent identifier — normal with an MSigDB collection — aborts the run with `No such name`. One-hunk fix. |
| N1 | note, design, verified | held | The FDR q-value numerator averages, over permutations, the per-permutation fraction of same-sign null NES beyond NES\*, where the paper pools all (set, permutation) pairs; on GSEA's own null the two differ by at most 0.0012 (120 sets) and 0.0039 (24 sets), no set crosses 0.25 or 0.05 either way. The numerator counts ties (≥) while the nominal p counts strictly beyond (a p of exactly 0 for 30 of 120 sets at 1,000 permutations). |
| N2 | note, design, verified | held | Tied ranking scores keep their file order (stable sort) and nothing warns: a 40-gene set inside a block of 1,200 tied genes is reported at ES +0.6959 or −0.6959 depending only on the order of the tied lines in the `.rnk`; fgsea gives the same two numbers and prints a tie warning. |
| N3 | note, reporting convention | held | `RANK AT MAX` is the 0-based position of the extreme for a positive ES and N minus that position for a negative ES (counted from the bottom); the leading-edge percentages are right either way. |
| N4 | note, cosmetic, by reading | held | The `USE_BIASED` preference has no effect on the `tTest` metric (SS/n over n − 1 equals SS/(n − 1) over n); not exposed on the command line. |

**Real-data check of GS3 (2026-09-14).** The finding was verified on synthetic lists; whether its
precondition (every present member of a set at exactly 0) occurs in practice was then tested on
two public datasets with every MSigDB 7.5.1 collection (32,880 sets, about 23,000 with 15 to 500
members present; from the `msigdbr` 7.5.1 package data). Airway bulk RNA-seq (GSE52778, the
Bioconductor `airway` counts, DESeq2's algorithm via pydeseq2, design `~ cell + dex`): the
worst-case list of all 39,609 symbol-mapped genes with NA statistics set to 0 carries 13,757
zeros, yet no set meets the condition (closest: `chr11q11`, 35 of 37 members at 0; 4 sets at
90 % or more, 105 at 50 % or more), and the audited jar and the patched jar report every set
identically (44 sets at FDR < 0.25 either way; see [`verify/gs3_real_airway.py`](verify/gs3_real_airway.py)
and its `.out` files). 10x PBMC 3k single-cell (2,638 cells, 13,714 genes, the `cellxgene`
example file): Seurat-style avg_log2FC over every gene for 8 cell-type-versus-rest and 28
pairwise contrasts, up to 4,344 exact zeros (dendritic cells versus megakaryocytes), again no
set meets the condition (closest 94 %; [`verify/gs3_real_pbmc3k.py`](verify/gs3_real_pbmc3k.py)).
Curated sets of 15 or more genes always contain something expressed, so with the standard
collections GS3 needs a small custom set of tissue- or cell-type-specific genes on a list that
includes unexpressed genes. The defect stands as reported (a silent 0/0 path in the default
scheme, one-hunk fix), but its exposure in published work is small; the issue text says so.

Three own suspicions were withdrawn by execution (a loop-index/set-index mix-up on the last
gene of the list; an exactly tied ± extreme; phenotype-permutation calibration) and are
recorded in the review.

**Held up under execution:** the enrichment score of the `classic`, `weighted` and
`weighted_p2` schemes equals the port and `fgsea::calcGseaStat` to 2e-7 on 24 planted and
random sets; NES, nominal p, FWER and FDR recomputed from the program's own stored null
(`RND_ES` in `results.edb`) match the report to the 4-decimal rounding of that file; the
gene-set null (random sets of the same size from the whole list) and the phenotype null (a
relabelling that keeps class sizes, the dataset re-scored per permutation) are what the paper
describes, with 9 and 6 of 100 null sets at p < 0.05; Signal2Noise, tTest, Ratio_of_Classes,
log2_Ratio_of_Classes, Diff_of_Classes and the `-median` variant equal the port to 4e-5
including the documented minimum-sigma rule (σ ≥ 0.2·|mean|, 0.2 at mean 0) on 150 planted
low-variance and 30 zero-mean genes; all five collapse modes (`Max_probe` per sample,
median, mean, sum, absolute max) for the expression tool and for GSEAPreranked equal the port
to 1.3e-6; the size filter is inclusive and applied after restriction to the data when
`min ≠ max`; leading-edge tags and rank at max agree with the port's running sum.

## How the papers use GSEA (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| DESeq2 / edgeR / limma upstream of the ranking | 314 |
| single-cell context (Seurat / Scanpy / scRNA) | 249 |
| KEGG / Reactome / GO collections | 146 |
| Hallmark collection | 96 |
| `fgsea` used | 90 |
| `clusterProfiler` (gseGO/gseKEGG) | 85 |
| MSigDB named | 79 |
| GSEA desktop / javaGSEA / Broad named | 55 |
| ssGSEA / GSVA | 51 |
| pre-ranked | 41 |
| FDR threshold stated (0.05 ×23, 0.1, 0.2, 0.01, 0.001) | 28 |
| ranked by log fold change / by t, Wald or signed p | 28 / 8 |
| GSEA version stated (4.1.0 ×8, 4.3.2 ×7, 4.0.3 ×7, 4.3.3 ×3, 4.2.3 ×3, 3.0 ×2, 2.2.3 ×2) | 23 |
| NES reported | 18 |
| number of permutations stated (1,000 ×3, 2,000, 10,000) | 12 |
| GSEApy | 7 |
| weighted / classic scoring stated | 6 |
| phenotype / gene-set permutation stated | 0 / 4 |
| Signal2Noise named / t-test metric named | 3 / 0 |
| gene set size limits stated | 2 |

Versions named run from 3.0 to 4.3.3; GS2 and GS3 are present in every one of them, GS1
in its current form since 4.2.0 and in its earlier form before.

**Profiling caveat.** As for the Seurat and Scanpy audits, this session had no route to
Europe PMC, so `gsea_profile.py` ran in `--offline` mode over the survey's stored evidence
snippets; every record in `gsea_profiles.jsonl` is `source: survey_cache` and every count
above is a lower bound. Rerun without `--offline` from a host with Europe PMC access to
replace them with full-text records.

## Filing channel (read before anything is sent)

- `CONTRIBUTING.md` (the only contribution document): search the tracker first; an issue
  needs a title, a clear description and "a code sample, executable test case, or clear set
  of instructions"; bug-fix PRs are welcome, one issue per PR, with the problem and solution
  described and the issue number; feature changes go through an issue first. No AI policy,
  no sign-off, no templates (no `.github/` directory), no changelog file, no linter. Bug
  reports are also taken through the GSEA help forum / contact page (unreachable from here).
- The repository is essentially single-maintainer (256 of 263 commits fetched), with no
  merged external PR in that window; a PR may wait.
- No prior report of GS1, GS2 or GS3 in the tracker (searched 2026-09-13; nearest #5, #14,
  #10, #50). No fork under `cindykrafft` and no `declines_ai` entry, so the AI-contribution
  check cannot fail yet.
- **The kit is in [`upstream/`](upstream/)**: three issue texts (title + body in
  CONTRIBUTING's order, each with an executable shell MCVE and its output on `master` and on
  the patched build), three `git am`-able patches against `dc35c76` (fix + JUnit 5 test in
  the project's `src/test/java` layout; each new test fails on unmodified `master`, the
  project's 55 existing tests pass before and after), and the PR bodies. Ranking: GS3 first
  (default settings, current release), GS1 second, GS2 held.

## Files

| file | what |
|---|---|
| `gsea_profile.py`, `gsea_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/enrichment-core.md` | the review: GS1–GS3, N1–N4, withdrawn suspicions, held-up list, not-audited list |
| `verify/_gsea_common.py`, `verify/gsea_port.py` | CLI runner / report parsers, and the independent numpy port of the paper's statistics |
| `verify/gs1_weighted_p15_negative_scores.py` (+ `.out`, `.v4.4.0.out`, `.v4.3.2.out`, `.v4.1.0.out`, `.v4.0.3.out`, `.patched.out`) | GS1 on every build and on the patched jar |
| `verify/gs2_set_min_equals_max.py` (+ the same six `.out`) | GS2 |
| `verify/gs3_zero_weight_set.py` (+ the same six `.out`) | GS3 |
| `verify/gs3_real_airway_de.py` (+ `.out`), `verify/gs3_real_airway.py` (+ `.out`, `.patched.out`) | real-data check of GS3 on airway bulk RNA-seq: DESeq2 via pydeseq2, three ranked lists, every MSigDB 7.5.1 collection counted, KEGG 2016 + Hallmark run through the audited and the patched jar |
| `verify/gs3_real_pbmc3k.py` (+ `.out`) | real-data check of GS3 on 10x PBMC 3k: 36 cell-type contrasts, every MSigDB collection counted |
| `verify/heldup_preranked_core.py` (+ `.out`) | ES vs port and fgsea for three schemes; NES/p/FWER/FDR from the stored null; rank at max and leading edge |
| `verify/heldup_expression_metrics.py` (+ `.out`) | the five ranking metrics and the minimum-sigma rule; gene-set and phenotype permutation; null calibration |
| `verify/heldup_collapse.py` (+ `.out`) | the five collapse modes, expression tool and GSEAPreranked |
| `verify/note_fdr_formula.py`, `verify/note_ties.py` (+ `.out`) | N1, N2 |
| `upstream/` | filing kit: three issue texts, three MCVE scripts + outputs, patches 0001–0003, PR bodies, README |

Harnesses need `GSEA_SCRATCH` (default `/tmp/gseawork`, a symlink to the scratch clone — GSEA's
option parser splits any path containing `-`) with `src/` built (`./gradlew jar`) and the tag
checkouts compiled to `<tag>/out`; fgsea in `$GSEA_SCRATCH/rlib` for the two harnesses that
call R. Java runs on OpenJDK 25.0.4 here (the project targets 17 and bundles 21).

## Next steps

1. File GS3 (issue + PR 3) and GS1 (issue + PR 1) from the kit; GS2 after a response.
   Record numbers and maintainer responses here.
2. Extend the review to the leading-edge tool, the continuous-phenotype metrics and the
   balanced permutation modes.
3. Full-text profiling rerun when Europe PMC is reachable, to learn how many cohort papers
   ran the desktop application with `weighted_p1.5` or with preranked lists containing zeros.
