# Component: PLINK 1.9 / 2.0 QC filters and association core (`chrchang/plink-ng` `master` @ `8bfebe8`, 2026-09-02)

Read in full on `master`: `1.9/plink_stats.c` lines 176–800 (`SNPHWE2`, `SNPHWE_t`,
`SNPHWE_midp_t`, `fisher22`), `1.9/plink_filter.c` `enforce_hwe_threshold`
(2941–2948 for `--hardy`, 3095–3135 for `--hwe`), `1.9/plink_misc.c` `het_report`
(3816–3990), `2.0/include/plink2_stats.cc` `HweLnP` (1780), `HweThresh`/`HweThreshMidp`
(2283, 2538) and `HweThreshLnMain` (2746), `2.0/plink2_filter.cc` `EnforceHweThresh`
(3539–3670). Targeted reads of the `--score`, `--indep-pairwise`, `--r2`/`--ld`,
`--genome`, `--make-king-table` and `--adjust` entry points to know what each column
means; those paths were verified by execution rather than by reading every line.

Every suspicion was **executed on the shipped code**: PLINK 1.9 (`1.9/plink`, version
string `v1.9.0-b.8`, LAPACK-linked against a locally built OpenBLAS) and PLINK 2.0
(`2.0/build_dynamic/plink2`, `v2.0.0-b.1`) built from the audited tree; the exact-test
functions were additionally linked verbatim from the build's object files into two
small drivers (`../verify/stats_driver19.c`, `../verify/stats_driver2.cc`) so that they
can be queried table by table. References are exact rational arithmetic
(`../verify/exact_ref.py`, `fractions.Fraction`) for the HWE and Fisher tests, and
scipy/statsmodels or closed forms for everything else, on synthetic genotypes generated
inside each harness. The confirmed finding was also run on PLINK 1.9 built from the
tags `v1.9.0-b.7.12` (2026-09-01, the latest 1.9 release tag), `v1.90b4` (2017-03-20)
and the commit `52f7793` (`v1.90b6.21`, 2020-10-19, the 1.9 build the cohort names
most often), all built without LAPACK (`NO_LAPACK`, version strings carry `NL`).

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### PL1 — CONFIRMED on `master`, `v1.9.0-b.7.12`, `v1.90b6.21`, `v1.90b4`; not in PLINK 2.0: `--hwe` removes variants whose exact HWE p-value is above the threshold when the variant has 2 or 3 heterozygotes

**Code.** `--hwe` does not compare the p-value that `--hardy` prints. It calls the
threshold-only routines `SNPHWE_t` / `SNPHWE_midp_t` (`plink_filter.c:3122-3124`, with
the threshold scaled by `1 - SMALL_EPSILON` at `:3103`), which sum relative
likelihoods until the verdict is decided. In both routines and both tail branches
the structure is: sum the centre (`plink_stats.c:427-440`, `:502-517`), test
`tailp1 + tailp2 >= exit_thresh` once with the observed element only (`:442`,
`:519`), extend the observed tail by one element — `tailp1 += lastp1` at `:458` /
`:531` — then walk the rest of that tail *only* `if (obs_homr > 1)` (`:460`) or
`if (obs_hets >= 4)` (`:534`), each step comparing against the threshold (`:470`,
`:543`). When that walk is skipped, the only comparison left is inside the loop over
the *other* tail (`:482-495`, `:555-568`), which compares only after adding a further
element and does not execute at all when that tail has one element or none. The
function then reaches `return 1` (`:496`, `:569`): the variant fails. For two
heterozygotes the other tail never has more than one element (the het count can only
go 0 → 2 → 4 … and P(4) is already in the centre), so the second element of the
observed tail — P(hets − 2), or P(hets + 2) in the upper branch — is never counted.
`SNPHWE_midp_t` has the same four sites (`:654`, `:674`, `:731`, `:751`, returns at
`:689`, `:766`). The filter therefore acts on p − P(hets − 2) instead of p, while
`--hardy` (`SNPHWE2`, `:176`) prints the correct p. PLINK 2.0's `HweThreshLnMain`
(`include/plink2_stats.cc:2746`) is a different implementation and is not affected.

A trace of `SNPHWE_t(2, 2, 2, 0.48)` (relative masses, P(obs) = 1): centre = P(4) =
1.333, tail 2 = P(6) = 0.178, tail 1 = P(2) + P(0) = 1 + 0.056; exit threshold
1.333 × 0.48/0.52 = 1.231; 1.056 + 0.178 = 1.233 ≥ 1.231 should pass, but the last
comparison made was 1 + 0.178 < 1.231 and the tail-2 loop has nothing left to add.

**Verified** (`../verify/pl1_hwe_threshold_boundary.py` → `.out`, and `.patched.out`
for the fixed build; `../verify/version_scope_hwe_cli.*.out`;
`../upstream/mcve_outputs.txt`):

| what | result |
|---|---|
| shipped `SNPHWE_t`, every table with n ≤ 200 and ≤ 6 hets (67,883 with 0 < p < 1), threshold bisected to 2⁻⁴² | wrong boundary on 19,399 tables: all 9,798 with 2 hets, 9,600 of 9,697 with 3 hets, 1 with 5 hets, none with 0, 1, 4, 6; offsets (flip threshold / p − 1) from −4.6e-5 to −2.7e-2 (2 hets) and up to −5.3e-2 (3 hets); largest at (3 hets, 1, 6), p = 0.4799 |
| shipped `SNPHWE_midp_t`, same tables (p < 0.5) | 19,399 wrong; offsets to −7.1e-2 (2 hets) and −1.36e-1 (3 hets) |
| plink2 `HweThreshLn`, same tables, both modes (control) | 0 wrong; offsets ≤ +8e-12 |
| patched `SNPHWE_t` / `SNPHWE_midp_t` (`../upstream/0001-*.patch`) | 0 wrong of 67,883, both modes |
| CLI, n = 6, counts 2/2/2, exact p = 37/77 = 0.480519, `--hardy` prints 0.4805 | `--hwe 0.48` and `--hwe 0.4805`: plink 1.9 **removed**, plink2 kept; `--hwe 0.46`, `0.45`: kept; `--hwe 0.4806`: both removed (correct); mid-p 2/7 = 0.2857: `--hwe 0.28 midp` plink 1.9 **removed**, plink2 kept |
| CLI, n = 1007, counts 2 het / 5 / 1000, p = 1.905e-12, P(0)/P(2) = 8.3e-5 | removed at thresholds p·(1 − 1e-5), p·(1 − 3e-5), p·(1 − 6e-5); kept at p·(1 − 1e-4) and below; mid-p: removed at p·(1 − 3e-5) and p·(1 − 1e-4) |
| CLI, n = 307, counts 3 het / 4 / 300, p = 1.246e-7, P(1)/P(3) = 1.0e-3 | removed at p·(1 − 1e-4), p·(1 − 3e-4); kept at p·(1 − 1e-3) and below |
| grid check (`../verify/heldup_exact_tests_exhaustive.plink19.out`), n ≤ 40, thresholds 1e-2 … 1e-50 | 5 of 115,020 (table, threshold) pairs disagree with `p < t`, all with 2 or 3 hets; 343 of 2,126 tables with `t` set to their own p are reported as failing (plink2: 0 and 0) |
| version scope (CLI script, both tables) | `master`, `v1.9.0-b.7.12`, `v1.90b6.21`, `v1.90b4`: **affected**; patched build: unaffected |
| patched build, whole `--hwe` held-up harness (`../verify/heldup_hardy_cli.patched.out`) | symmetric differences stay 0 (the harness's 400 random variants have no table in the affected band) |

**Magnitude and who is exposed.** The variant is removed when its exact p lies in
(p − P(hets − 2), p), i.e. relative to p the band is roughly P(hets − 2)/P(hets) =
2/(4·(hom_r + 1)·(hom_c + 1)) for two heterozygotes and 6/(4·(hom_r + 1)·(hom_c + 1))
for three. On GWAS-size samples this band is ~10⁻⁴–10⁻⁶ of p, so a given variant is
hit only if its p sits within that fraction above the threshold — a deterministic
wrong answer, but a rare one; on small samples (family studies, n in the tens) the
band is several per cent of p. Two- and three-heterozygote variants are the rare
variants that `--hwe` is most often applied to. Any PLINK 1.9 pipeline (the cohort
names 1.9 / 1.90 / 1.90b in 84 of the 184 papers) with `--hwe` is exposed; the
effect is a handful of rare variants dropped at the boundary, and the only symptom is
that `--hardy` reports a p above the threshold for a variant that `--hwe` removed.
This is a wrong number at `master`, not a design choice: the help text (`plink_help.c:1648`)
says "Exclude variants with Hardy-Weinberg equilibrium exact test p-values below a
threshold".

**Fix** (`../upstream/0001-*.patch`, 28 added lines, no behaviour change elsewhere):
compare the completed observed tail against the threshold before walking the other
tail, at the four sites (`:481`, `:554`, `:674`, `:751`): `if (tailp1 + tailp2 >=
exit_thresh) return 0;`.

## Notes (design or documentation; not wrong numbers)

### N1 — `--het` expected homozygosity: both versions default to 1 − 2pq; `small-sample` applies the 2n/(2n − 1) correction

`plink_misc.c:3936` (all-founder branch) uses `1 - 2p(1-p)` from the loaded allele
frequency, `:3955` (`small-sample` / non-founder branch) `1 - 2(1-p)·k/(2n-1)`.
Executed (`../verify/heldup_freq_missing_het.out`): plink 1.9 `E(HOM)` agrees with the
uncorrected reference to 5.0e-2 of ≈296 (1.7e-4 relative; 6 significant digits are
printed) and `F` to 4.9e-5; `small-sample` agrees with the corrected reference to
5.0e-2 / 4.8e-5; plink2 to 5.0e-4 / 4.9e-7 in both modes. A user switching between
the two modes sees `F` move by up to 3.1e-3 on 200 samples. Documented behaviour;
recorded so the reference in the harness is not mistaken for a finding.

### N2 — `--ld` reports the EM haplotype-frequency r², `--r2` the genotype correlation

Both versions: `--ld snp4 snp5` prints r² = 0.707983 and D' = 0.844295, equal to an
EM port on the 3 × 3 genotype table; `--r2 inter-chr` prints 0.720079 for the same
pair, equal to the pairwise-complete genotype correlation (`../verify/heldup_ld_prune_r2.out`).
Both are documented; the two numbers differ by 1.7 % here and users who mix them
should know why.

### N3 — `--indep-pairwise` pruned sets differ between 1.9, 2.0 and a port of the documented scan by 1–4 of 120 variants

`../verify/heldup_ld_prune_r2.out`: for `50 5 0.5`, plink 1.9 prunes 84, plink2 86, the
port 83, symmetric differences 3 and 3; for `100 25 0.4`: 89 / 93 / 89, differences 4
and 4; `20 10 0.8`: 0 / 0 / 0. The r² values themselves agree with numpy to 5e-7 on
7,140 pairs, so the differences are in the order of pairwise removals inside a window,
which the documentation leaves to the implementation (plink2's documentation says its
results differ from 1.9's). Not a wrong number; recorded as an implementation-defined
choice that changes which variants survive pruning.

### N4 — plink2 `--score center` with default mean imputation differs from plink 1.9 `center` and from the reference; cause not traced (open)

`../verify/heldup_score.out`: `SCORE1_AVG` differs from the reference by up to 6.5e-2
(and from plink 1.9's `center` output by the same amount) on 150 samples × 60 variants
with 8 % missing calls, while `center no-mean-imputation` agrees to 2.8e-7 and every
other mode (default, `sum`, `no-mean-imputation`) agrees to ≤ 5e-5 on both versions.
The difference is not a constant offset (std 2.2e-2 across samples) and is not
explained by any of five re-orderings of impute/centre/flip that were tried. This is
an executed discrepancy whose cause was not located in the session; it is listed as a
note rather than a finding until the intended semantics of `center` with imputed
dosages in plink2 are read from the code. Next step in `../README.md`.

### N5 — plink 1.9 `--adjust` row order for tied p-values is not the input order

`../verify/assoc_glm_adjust.out`: the `.adjusted` rows of `--assoc --adjust` are not in
stable-sorted order of p (plink2's are); every adjusted column still matches
statsmodels to printed precision. Cosmetic.

## Withdrawn (own suspicions killed by execution)

- **W1 — plink 1.9 `--adjust` GC column under `--linear`/quantitative `--assoc` uses
  one df for all rows.** The previous session's harness suggested a mismatch; rerun
  with the printed T statistics it is 5–7 of 200 rows "off by > 0.1 %" only because the
  reference was recomputed from 4-significant-digit T values; the printed `GC` equals
  `UNADJ` exactly when λ < 1 (`assoc_glm_adjust.out`, part C). Withdrawn.
- **W2 — KING kinship off by up to 5.5.** The harness indexed the genotype matrix on the
  wrong axis; corrected, plink2 `--make-king-table` matches the KING-robust port to
  2.4e-7 on 1,035 pairs. Withdrawn (harness error, recorded for honesty).
- **W3 — plink2 `--freq ALT_FREQS` off by 1.0 and `--glm BETA` off by 0.29.** Both were
  the harness ignoring that plink2 orients REF/ALT itself on `.ped` import; compared on
  the allele plink2 names in the `ALT`/`A1` column the differences are 5e-7 and 8e-7.
  Withdrawn.

## What held up (executed, not just read)

- **HWE exact test values.** plink 1.9 `SNPHWE2` and plink2 `HweLnP` equal the exact
  rational p (and mid-p) on every genotype table with n ≤ 60 (40,670 tables × 2 modes)
  to a relative 1.1e-15 (`heldup_exact_tests_exhaustive.*.out`); `--hardy` and
  `--hardy midp` on 400 random variants with 3 % missing calls (60 pushed out of HWE)
  agree with the exact p to the 4 / 6 significant digits printed (`heldup_hardy_cli.out`).
- **`--hwe` away from the boundary.** At 0.05, 1e-3 and 1e-6, with and without `midp`,
  both versions keep exactly the variants with exact p ≥ t on those 400 variants
  (symmetric difference 0 in all 12 runs).
- **Fisher's exact test.** plink 1.9 `fisher22` and plink2 `Fisher22TwoSidedP` (p and
  ln p) equal the exact two-sided p on every 2 × 2 table with N ≤ 40 (271,500 tables ×
  2 modes) to 2.4e-15; `--assoc fisher` on 200 variants to printed precision.
- **`--freq`, `--missing`.** MAF / `ALT_FREQS`, `NCHROBS` / `OBS_CT`, per-variant and
  per-sample `F_MISS` equal numpy on 300 variants with 5 % missing calls, a monomorphic,
  an all-missing (printed `NA` / `nan`) and an all-heterozygous variant.
- **`--assoc`, `--model`, `--logistic`, `--linear`, `--glm`.** Allelic χ², OR,
  Cochran–Armitage trend, genotypic χ², Wald z / p and OR of the additive logistic
  model with and without `sex` + a covariate, and OLS β / SE / t / p, on 200 variants ×
  500 samples, agree with scipy / statsmodels to printed precision (1.9 prints 4
  significant digits) and to ≤ 1e-5 relative for plink2 (`assoc_glm_adjust.out`).
  plink2 Firth: log OR within 0.14 and SE within 3.5e-3 of a Jeffreys-penalised Newton
  port on 200 variants — the port has no step-halving, so this is a loose check, not a
  discrepancy claim.
- **`--adjust`.** `BONF`, `HOLM`, `SIDAK_SS`, `SIDAK_SD`, `FDR_BH`, `FDR_BY` equal
  `statsmodels.stats.multitest.multipletests` (both versions, 200 tests) to printed
  precision; the `GC` column equals χ²-sf(χ²/λ) with λ = median(χ²)/0.456, and `QQ` =
  (i + 0.5)/m.
- **`--r2` / `--r2-unphased`.** 7,140 inter-chromosome pairs equal the pairwise-complete
  genotype correlation to 5e-7 in both versions; `--ld` equals the EM haplotype r² and D'.
- **`--genome`.** `Z0`/`Z1`/`Z2`/`PI_HAT` equal a first-principles port of the PLINK
  1.07 method-of-moments estimator (expected IBS probabilities from sampling alleles
  without replacement, successive solution, the documented clamping) to 5e-5 (4
  decimals printed) on 1,035 pairs including planted parent–offspring (PI_HAT 0.5135),
  full-sib (0.5038) and half-sib (0.2934) pairs; `IBS0/1/2` exact.
- **`--make-king-table`, `--king-cutoff`.** KINSHIP equals the KING-robust estimator to
  2.4e-7; planted 1st-degree pairs read 0.2524 / 0.2502, the half-sib pair 0.1461, an
  unrelated pair 0.0036; `--king-cutoff 0.177` removes 3 samples that break every
  first-degree pair.
- **`--score`.** Default (mean imputation, average), `sum`, `no-mean-imputation`, and
  1.9's `center` equal the reference to ≤ 5e-5 (6 digits printed) with a score file
  whose effect allele is sometimes REF; `CNT` is the number of non-missing alleles as
  documented; plink2 `DENOM` and `SCORE1_SUM` likewise. (plink2 `center` with
  imputation: N4.)
- **`--het` `O(HOM)`, `N(NM)` / `OBS_CT`** exact; `E(HOM)`/`F` as in N1.

## Not audited

`--pca` (variance explained, `approx`), `--clump`, `--fst`, chrX / haploid handling in
`--hardy`/`--freq`/`--hwe` (`HweXchrLnP` is in the driver but was not exercised),
`--mac`/`--max-mac`, `--geno`/`--mind` beyond `--missing`, `--indep` (VIF), dosage
input to `--score` and `--glm`, `--glm` with categorical covariates and `--vif`,
permutation tests, `--assoc` on chrX, `--check-sex`, `--homozyg`, file-format
conversion and every I/O path.
