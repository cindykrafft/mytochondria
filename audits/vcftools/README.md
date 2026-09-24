# VCFtools audit against 112 published papers (2021–2026)

_Generated 2026-09-24 against `vcftools/vcftools` `master` @ `1f87a83` (0.1.18 in `.tarball-version`,
2025-05-14, no tag) built here, the v0.1.16 and v0.1.13 tags built the same way, and the Ubuntu 24.04
package `vcftools 0.1.16-3`. Focus: the site and genotype filters, the population-genetic statistics
(π, Tajima's D, Fst, heterozygosity, HWE, LD, kinship) and the 012/PLINK conversions the papers run —
verified by running the binary on VCFs generated with known genotypes, missingness, depths and
population structure, against exact recomputations and ports of the cited estimators._

## What this is

The six-journal survey found **112 papers** in PNAS, *Nature*, *Cell* and *Science*, 2021–2026, that
used VCFtools, nearly always after GATK / bcftools / freebayes / Stacks calling (87) and often beside
PLINK (38) and ADMIXTURE (22): filtering by minor allele frequency, missingness, depth and genotype
quality, then Fst between populations, windowed nucleotide diversity, LD decay, kinship for sample
checks, and per-individual heterozygosity. The statistics and filter code was read on `master` and
every number recomputed from the input in Python (`verify/_synth.py`: per-site π, Tajima's constants,
the Weir & Cockerham 1984 estimator, the Wigginton 2005 exact test, KING-robust kinship, r² / D / D').

## Findings (details and line citations in [`component-reviews/statistics-filters-conversions.md`](component-reviews/statistics-filters-conversions.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **VT1** | **CONFIRMED on `master`, v0.1.16, v0.1.13** (source builds, GCC 13 default flags); no prior report | now (issue + PR, 19-line fix) | Every temporary-file output mode (`--012`, `--plink`, `--hap-r2`, `--geno-r2`, `--geno-chisq`, the interchromosomal and SNP-list r² modes, `--ldhat`, `--ldhelmet`) copies the `mkstemp` template into a stack buffer one byte too small. Built with a fortifying compiler (`_FORTIFY_SOURCE=3`, the default on Ubuntu 24.04, Fedora and Debian 13 with `-O2`) each mode aborts with `*** buffer overflow detected ***` before writing anything; other builds write the NUL past the array. |
| **VT2** | **CONFIRMED on all four builds**; no prior report (#180 is an empty-output question) | now (issue + PR) | `--relatedness2` counts each individual's heterozygous sites over every site where that individual is called, while the numerator counts only sites called in both, so with missing genotypes the KING-robust kinship is scaled down by roughly the pairwise call rate: at 20 % missingness a duplicate pair reports 0.40 (KING: 0.50, cut-off for duplicates 0.354) and a parent–offspring pair 0.19 (0.24; cut-off for first degree 0.177). |
| **VT3** | **CONFIRMED on all four builds**; #28 (2016, closed by the reporter after working it out, no maintainer reply, manual unchanged) | ready (documentation issue, patch to the man page) | `--max-missing-count N` excludes sites with more than N missing *alleles*; the manual says "missing genotypes". For diploid data the filter is twice as strict as written: 30 individuals, `--max-missing-count 3` keeps the 392 sites with ≤ 1 missing genotype, not the 572 with ≤ 3. |
| VT4 | note, verified (#163 is a different `--missing-site` layout question) | held | After a genotype filter (`--minDP`, `--minGQ`), `--missing-site` reports `F_MISS` over the unfiltered genotypes only, while `--max-missing` counts the filtered genotypes as missing: every one of 565 sites with `F_MISS ≤ 0.1` under `--minDP 10 --missing-site` is removed by `--minDP 10 --max-missing 0.9`. The man page describes neither `N_DATA` nor `N_GENOTYPES_FILTERED`. |
| VT5 | note, verified | held | `--TajimaD` uses n = 2 × individuals for every bin regardless of missing genotypes (per-site sample sizes 65–80 of 80 in the harness). |
| N1 | note, verified; #189 (2022, open) asks exactly this | held (comment for #189 ready if wanted) | `--012` writes biallelic sites only, with a one-off log warning; the manual's `--012` text does not say so (the `--IMPUTE` text does). |

**Held up under execution (all four builds unless stated):** `--site-pi`; `--window-pi` with and without
a step (`N_MONOMORPHIC` is a `master`-only column); `--TajimaD` with complete genotypes; `--het`
(`O(HOM)`, `E(HOM)`, `N_SITES`, F over biallelic sites polymorphic among the kept individuals — the
explanation of #210); `--hardy` incl. the exact test; `--freq`, `--counts`, `--missing-indv`,
`--missing-site`, `--depth`, `--site-mean-depth`; `--weir-fst-pop` per site, windowed, `MEAN_FST` and
`WEIGHTED_FST`, with and without missing genotypes; `--hap-r2` and `--geno-r2` (on the builds that run
them); `--relatedness2` with complete genotypes; `--012` dosages; `--maf`, `--max-maf`, `--mac`,
`--max-missing`, `--minQ`, `--remove-filtered-all`, `--remove-indels`, `--keep-only-indels`,
`--min-alleles`/`--max-alleles`, `--minDP`/`--minGQ` combined with `--max-missing` and `--maf`,
`--thin`. Not checked: the Perl tools, BCF input, haploid / mixed-ploidy sites, `--LROH`, `--TsTv*`,
`--SNPdensity`, `--fst-window` on multi-population input, `--BEAGLE-GL` / `--IMPUTE` content.

## Verification method

Every claim above was executed: `verify/v1_diversity_het_hwe.py`, `v2_fst_ld_relatedness.py` and
`v3_filters.py` generate VCFs (40 individuals × 2000 sites with 8 % missing genotypes and multi-allelic
sites; 40 individuals in two populations with duplicate, parent–offspring and unrelated pairs; 30
individuals × 1200 sites with DP / GQ / QUAL / FILTER / indels), run the binary given on the command line
and compare every output column with the exact recomputation; `.out` is `master`, `.v<version>.out` the
tags and the Ubuntu package, `.patched.out` / `.patched2.out` the two fix branches.

## How the papers use VCFtools (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 20 (0.1.16 ×24 mentions, 0.1.13 ×9, 0.1.14 ×6, 0.1.15 ×4, 0.1.17 ×3) |
| called upstream with GATK / bcftools / freebayes / Stacks | 87 |
| LD (`--hap-r2` / `--geno-r2`) | 25 |
| Fst (`--weir-fst-pop`) | 25 |
| `--maf` / `--mac` | 21 |
| π (`--window-pi` / `--site-pi`) | 20 |
| biallelic filter | 18 |
| `--max-missing` (values 0.8, 0.75, 1; percentages 10–25) | 17 |
| `--minDP` / `--minGQ` | 15 |
| kinship (`--relatedness` / `--relatedness2`) | 13 |
| `--het` | 8 |
| `--012` / `--plink` / `--recode` | 4 |
| `--TajimaD` | 2 |
| co-packages: SAMtools 64, GATK 58, BWA 54, BCFtools 48, PLINK 36, ADMIXTURE 22 | |

The profile (`vcftools_profile.py`, `vcftools_profiles.jsonl`, `profile_run.log`) ran on the survey's
stored evidence sentences (no route to Europe PMC from this session), so the counts are lower bounds.

## Filing channel

`vcftools/vcftools` has no CONTRIBUTING file, no issue or PR template and no AI policy; the README
says the GitHub Issues page is the way to get help. The tracker shows no maintainer reply in any of
the twelve threads read for this audit (2016–2024) and four open PRs from 2016–2026; the last commit is
from 2025-05-14. Kit in [`upstream/`](upstream/).

## Files

| path | what |
|---|---|
| `component-reviews/statistics-filters-conversions.md` | the review: VT1–VT5, N1 with code citations, held-up list, version scope |
| `verify/_synth.py` | VCF writer, runner (records aborts), the recomputed statistics |
| `verify/v1_diversity_het_hwe.py` | π, windowed π, Tajima's D, `--het`, `--hardy`, `--freq`, `--counts`, missingness, depth, `--012` |
| `verify/v2_fst_ld_relatedness.py` | Fst per site / windowed / log, `--hap-r2`, `--geno-r2`, `--relatedness2` with and without missing data |
| `verify/v3_filters.py` | every site and genotype filter against the recomputed kept set; `--missing-site` after `--minDP` |
| `verify/*.out`, `*.v<version>.out`, `*.patched*.out` | captured output per build |
| `vcftools_profile.py`, `vcftools_profiles.jsonl`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit: issue texts, PR bodies, the two patches |

## Next steps

1. Fork `vcftools/vcftools`; push `fix/tmpname-buffer-size` and `fix/relatedness2-missing-genotypes`.
2. File VT1 (issue + PR) and VT2 (issue + PR) from the kit; VT3 when one of them has a reply.
3. Record numbers and responses here and in the top-level status table.
