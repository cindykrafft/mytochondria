# VCFtools: site filters, population-genetic statistics and format conversions

_Reviewed 2026-09-24 against `vcftools/vcftools` `master` @ `1f87a83` (`.tarball-version` 0.1.18,
2025-05-14, no release tag yet), with every check also executed on the release tags v0.1.16
(2018-08-02, the cohort's most-named version), v0.1.13, the Ubuntu 24.04 package
`vcftools 0.1.16-3`, and on the two fix branches. Harnesses and outputs in `../verify/`._

## What the cohort uses (112 papers, `../vcftools_profiles.jsonl`, survey-cache lower bounds)

| use | papers |
|---|---|
| called with GATK / bcftools / freebayes / Stacks upstream | 87 |
| LD (`--hap-r2` / `--geno-r2` / `--ld-window`) | 25 |
| `--weir-fst-pop` (Fst) | 25 |
| `--maf` / `--mac` | 21 |
| `--window-pi` / `--site-pi` | 20 |
| `--min-alleles 2 --max-alleles 2` | 18 |
| `--max-missing` / `--max-missing-count` | 17 |
| `--minDP` / `--maxDP` / `--minGQ` | 15 |
| `--relatedness` / `--relatedness2` | 13 |
| `--freq` / `--counts` | 13 |
| `--het` | 8 |
| `--012` / `--plink` / `--recode` | 4 |
| `--TajimaD` | 2 |
| version stated | 20 (0.1.16 ×24 mentions, 0.1.13 ×9, 0.1.14 ×6, 0.1.17 ×3) |

Typical pipeline in the cohort: filter (`--minDP`, `--minGQ`, `--max-missing 0.8–1`, `--maf
0.01–0.05`, biallelic SNPs only, `--recode`), then statistics on the filtered VCF (Fst between
populations, windowed π, LD decay, kinship for sample checks, heterozygosity per individual),
often handed to PLINK / ADMIXTURE / GEMMA afterwards.

## Code read

`src/cpp/`: `parameters.cpp` (option parsing), `entry_filters.cpp` (`filter_sites_by_allele_count`,
`filter_sites_by_frequency_and_call_rate`, `filter_genotypes_by_depth_range`, `filter_sites_by_thinning`),
`vcf_entry.cpp` (`filter_genotypes_by_depth`, `filter_genotypes_by_quality`), `entry_getters.cpp`
(`get_allele_counts`, `get_N_chr`, `get_genotype_counts`), `entry.cpp` (`SNPHWE`),
`variant_file_output.cpp` (`output_per_site_nucleotide_diversity`, `output_windowed_nucleotide_diversity`,
`output_Tajima_D`, `output_het`, `output_hwe`, `output_frequency`, `output_site_missingness`,
`output_indv_missingness`, `output_indv_depth`, `output_site_depth`, `output_weir_and_cockerham_fst`,
`output_windowed_weir_and_cockerham_fst`, `output_haplotype_r2`, `output_genotype_r2`,
`output_indv_relatedness_Manichaikul`), `variant_file_format_convert.cpp` (`output_as_012_matrix`,
`output_as_plink`, `output_as_LDhat_*`, `output_as_LDhelmet`, `output_as_IMPUTE`). Statement of intended
behaviour: `vcftools.1` (the man page) and the Manichaikul 2010 / Weir & Cockerham 1984 / Wigginton
2005 papers the options cite.

## Findings

### VT1 — every temporary-file output mode aborts with "buffer overflow detected" when built with a fortifying compiler (`--012`, `--plink`, `--hap-r2`, `--geno-r2`, ...)

Nineteen writers build the `mkstemp` template in a `std::string` and copy it into a stack buffer one
byte too small:

```cpp
string new_tmp = params.temp_dir+"/vcftools.XXXXXX";
char tmpname[new_tmp.size()];          // room for the characters, not the terminating NUL
strcpy(tmpname, new_tmp.c_str());
fd = mkstemp(tmpname);
```

(`variant_file_format_convert.cpp`: `output_as_plink`, `output_as_012_matrix`, `output_as_LDhat_phased`
×3, `output_as_LDhat_unphased` ×2, `output_as_LDhelmet` ×3; `variant_file_output.cpp`: `output_haplotype_r2`,
`output_genotype_r2`, `output_genotype_chisq`, `output_interchromosomal_genotype_r2`,
`output_interchromosomal_haplotype_r2`, `output_haplotype_r2_of_SNP_list_vs_all_others` ×2,
`output_genotype_r2_of_SNP_list_vs_all_others` ×2.) `strcpy` writes the NUL one byte past the end of the
array. GCC's fortified `strcpy` catches it when the array size can be checked at run time, which is the
case since GCC 12 / glibc 2.35 with `_FORTIFY_SOURCE=3`, the default on Ubuntu 24.04 (and Fedora, and
recent Debian) when compiling with any `-O`: `./configure && make` with the default `-g -O2` produces a
binary in which each of these modes prints its banner and then

```
*** buffer overflow detected ***: terminated
```

before writing any output (`../verify/v1_diversity_het_hwe.out`, `v2_fst_ld_relatedness.out`: `--012`
and `--hap-r2` produce nothing on `master`, v0.1.16 and v0.1.13 built that way). The Ubuntu package
(`0.1.16-3`, built with `_FORTIFY_SOURCE=2`, which cannot size a variable-length array) and any build
without fortification run the same code and merely write the NUL over whatever follows the array. Modes
affected: `--012`, `--plink`, `--plink-tped`, `--hap-r2`, `--geno-r2`, `--geno-chisq`, `--interchrom-hap-r2`,
`--interchrom-geno-r2`, `--hap-r2-positions`, `--geno-r2-positions`, `--ldhat`, `--ldhat-geno`, `--ldhelmet`
(every mode of `--IMPUTE` and `--BEAGLE-GL` is unaffected).

Fix (`fix/tmpname-buffer-size`, `../upstream/0001-…patch`): `new_tmp.size()+1` at all nineteen sites. With
it every mode above runs (`v1_diversity_het_hwe.patched.out` 13/13, `v2_fst_ld_relatedness.patched.out`
LD blocks 7090/7090 pairs matching the r² / D / D' port).

Cohort exposure: 25 papers use the LD outputs, 4 the 012/PLINK conversions; whether a given one hit
this depends on how their vcftools was built (bioconda's build, `_FORTIFY_SOURCE=2`, does not abort).
The visible symptom is an abort with no output, so results are not silently wrong; the cost is the
inability to use these modes from a source build on a current distribution.

### VT2 — `--relatedness2` underestimates kinship whenever genotypes are missing

`output_indv_relatedness_Manichaikul` computes the KING-robust estimator

φ̂ᵢⱼ = (N_AaAa − 2·N_AAaa) / (N_Aa⁽ⁱ⁾ + N_Aa⁽ʲ⁾)

with `N_AaAa[i][j]` and `N_AAaa[i][j]` counted over the sites at which both individuals are called, but
`N_Aa[i]` counted over every site at which individual i is called, whatever j's genotype. In Manichaikul
et al. 2010 (eq. 11 and the KING implementation) all four counts run over the same set of SNPs, the
ones called in both individuals. The extra heterozygous sites in the denominator scale the estimate
down by roughly the pairwise call rate:

| pair (truth) | complete genotypes | 20 % of genotypes missing at random | KING-robust over the shared sites |
|---|---|---|---|
| duplicate (0.5) | 0.5000 | **0.4003** | 0.5000 |
| duplicate (0.5) | 0.5000 | **0.4042** | 0.5000 |
| parent–offspring (0.25) | 0.2372 | **0.1877** | 0.2373 |
| parent–offspring (0.25) | 0.2527 | **0.2036** | 0.2565 |
| unrelated (0) | −0.0045 | −0.0055 | −0.0070 |

(`../verify/v2_fst_ld_relatedness.out`, 2000 biallelic sites, 40 individuals.) KING's published
classification cut-offs (> 0.354 duplicate / MZ, 0.177–0.354 first degree, 0.0884–0.177 second degree)
are applied to `RELATEDNESS_PHI` in the cohort's sample-checking use: at 20 % missingness a
duplicate pair reads as first degree (0.40) and a parent–offspring pair (0.19) sits at the edge of
second degree; at 30 % it crosses. Missingness of 10–30 % per genotype is ordinary in the RAD-seq
and low-coverage data the cohort runs this on, and `--relatedness2` is usually run before the
`--max-missing` filter, on the full call set, because kinship is used to choose which samples to keep.

Fix (`fix/relatedness2-missing-genotypes`, `../upstream/0002-…patch`): count `N_Aa[i][j]` as the sites at
which i is heterozygous and j is called; `N1_Aa` and `N2_Aa` in the output become the per-pair counts
(identical to the old columns when nothing is missing). With it the 20 % case gives 0.5000 / 0.5000 /
0.2373 / 0.2565 / −0.0070, equal to the KING-robust port (`v2_fst_ld_relatedness.patched2.out`).
The complete-data results are unchanged to all printed digits.

### VT3 — `--max-missing-count` counts missing chromosomes, the manual says genotypes

`vcftools.1`: "`--max-missing-count <integer>`: Exclude sites with more than this number of missing
genotypes over all individuals." `filter_sites_by_allele_count`:

```cpp
if ((N_chr-N_non_missing_chr) > max_missing_call_count)
    passed_filters = false;
```

`N_chr − N_non_missing_chr` is the number of missing *alleles* (two per missing diploid genotype). On
30 diploid individuals `--max-missing-count 3` keeps the 392 sites with at most one missing genotype,
not the 572 with at most three (`../verify/v3_filters.out`); every diploid user gets a filter twice as
strict as the one they wrote down. Either the manual or the comparison should change; as `--max-missing`
is defined on the proportion of *data* (chromosomes), the smaller change is the manual (say "missing
alleles (two per missing diploid genotype)"), and the issue text offers both.

### VT4 (note) — after a genotype filter, `--missing-site`'s `F_MISS` and `--max-missing`'s call rate disagree

`--minDP` / `--maxDP` / `--minGQ` mark genotypes as filtered (`include_genotype[i] = false`) rather than
missing. `--max-missing` then treats a filtered genotype as missing (its call rate is
`N_non_missing_chr / N_chr`, with `N_chr` summed over all included individuals), which is what the
manual implies and what users expect. `--missing-site` however reports `N_DATA` as the chromosomes of
the *unfiltered* genotypes, the filtered ones in their own column `N_GENOTYPES_FILTERED`, and
`F_MISS = N_MISS / N_DATA` over the unfiltered ones only. So after `--minDP 10` a site at which 19 of 30
genotypes were filtered and one is missing reports `F_MISS = 0.09` (`chr1 62 22 19 2 0.0909`), while
`--minDP 10 --max-missing 0.9` drops it (call rate 0.33). In the harness all 565 sites with `F_MISS ≤
0.1` under `--minDP 10 --missing-site` are removed by `--minDP 10 --max-missing 0.9`. The
per-site missingness report is the tool users run to pick a `--max-missing` threshold; with a
genotype filter in the same command it does not describe what that threshold will do. Reported as a
note (a documentation gap: the man page describes neither column).

### VT5 (note) — `--TajimaD` uses n = 2 × individuals regardless of missing genotypes

`output_Tajima_D` fixes `n = 2·N_indv` for `a1`, `a2`, `b`, `c`, `e` and for π's `n/(n−1)`, and computes
each site's allele frequency over its non-missing alleles. With 8 % of genotypes missing the actual
sample size per site is 65–80 of 80 chromosomes (`../verify/v1_diversity_het_hwe.out`); the constants
are those of n = 80. The manual gives no definition; the effect on D is small at low missingness and
the option is used by 2 cohort papers, so this is a note. (`--het`'s `E(HOM)` and `--site-pi` do use the
per-site non-missing count.)

### N1 — `--012` writes only biallelic sites, with a log warning and nothing in the manual

`output_as_012_matrix` skips every multi-allelic site (`012: Only outputting biallelic loci.` once in
the log); 104 of 2000 sites were dropped in the harness and the `.012.pos` file lists the survivors.
The man page's `--012` text does not say so (the `--IMPUTE` text does). #189 ("Numeric 012 format have
less SNP than expected") is this.

## Held up

| what | harness | result |
|---|---|---|
| `--site-pi`: mismatching pairs / pairs of non-missing alleles | `v1` | 2000/2000 sites |
| `--window-pi`: `N_VARIANTS`, `N_MONOMORPHIC` (master only), π with monomorphic sites at 2N(2N−1) pairs; step windows | `v1` | 20/20 and 80/80 windows |
| `--TajimaD` with complete genotypes: `N_SNPS`, D from Tajima's constants | `v1` | 20/20 bins |
| `--het`: `O(HOM)`, `E(HOM)` = Σ 1 − 2p(1−p)·n/(n−1) over biallelic polymorphic sites where the individual is called, `N_SITES`, F | `v1` | 40/40 |
| `--hardy`: genotype counts, χ², exact-test p-values (Wigginton 2005 port) | `v1` | 1896/1896 |
| `--freq`, `--counts`, `--missing-indv`, `--missing-site` (no genotype filter), `--depth`, `--site-mean-depth` (sample variance over all individuals' DP) | `v1` | all sites / individuals |
| `--012` dosages over the biallelic sites (patched build) | `v1` | 40/40 individuals |
| `--weir-fst-pop` per site, `MEAN_FST` and `WEIGHTED_FST` in the log, windowed, with and without missing genotypes (Weir & Cockerham 1984 port, a/(a+b+c) summed over alleles) | `v2` | 1500/1500 sites, 12/12 windows, both data sets |
| `--hap-r2`: `N_CHR`, r², D, D'; `--geno-r2`: r² = squared Pearson correlation of dosages (patched build) | `v2` | 7090/7090 pairs each |
| `--relatedness2` with complete genotypes | `v2` | equals KING-robust |
| `--maf` (least frequent allele over non-missing alleles, not necessarily the non-reference one), `--max-maf`, `--mac`, `--max-missing` (call rate ≥ x), `--minQ`, `--remove-filtered-all`, `--remove-indels`, `--keep-only-indels`, `--min-alleles`/`--max-alleles`, `--minDP` + `--max-missing`, `--minGQ` + `--max-missing`, `--minDP` + `--maf` (MAF over surviving genotypes), `--thin` (≥ distance from the last kept site) | `v3` | every kept set equals the recomputed one |
| `--missing-site` after `--minDP`: the column layout described in VT4 | `v3` | 1200/1200 sites |

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| VT1 | master, v0.1.16, v0.1.13 built with GCC 13 default flags (aborts); every version carries the overflow | Ubuntu package 0.1.16-3 (no abort), `fix/tmpname-buffer-size` |
| VT2 | master, v0.1.16, v0.1.13, Ubuntu 0.1.16-3 | `fix/relatedness2-missing-genotypes` |
| VT3, VT4, VT5, N1 | master, v0.1.16, v0.1.13, Ubuntu 0.1.16-3 | — |
