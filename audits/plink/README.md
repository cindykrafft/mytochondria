# PLINK audit against 184 published papers (2021–2026)

_Generated 2026-09-03 against `chrchang/plink-ng` `master` @ `8bfebe8` (2026-09-02;
PLINK 1.9 version string `v1.9.0-b.8`, PLINK 2.0 `v2.0.0-b.1`). Focus: the code
paths that decide which variants and samples survive QC and which association
numbers get published — the Hardy–Weinberg exact test and the `--hwe` filter,
`--freq`/`--missing`/`--het`, LD pruning and r², `--genome` / KING relatedness,
`--assoc`/`--model`/`--logistic`/`--linear`/`--glm` with `--adjust`, and `--score` —
verified by executing the built binaries and the shipped exact-test functions._


> **Fixed upstream (2026-09-03).** The maintainer closed PR #381 and committed his own fix,
> [`1fe42e5` "1.9: fix issue 380"](https://github.com/chrchang/plink-ng/commit/1fe42e5b11ec0709bbbb8179e0ba69d015e9b6e8),
> which inserts the same `tailp1 + tailp2 >= exit_thresh` check at the same four points as
> the audit's patch. Rebuilt at that commit and rerun: 0 of 9,061 tables wrongly removed
> through the shipped functions and the command line reports "unaffected"
> (`verify/hwe19_version_scope.upstream-1fe42e5.out`, `verify/version_scope_hwe_cli.upstream-1fe42e5.out`).
> Issue #380 was still open at the time of writing, with two maintainer comments not readable
> from the audit session. Nothing further to file.

## What this is

The six-journal survey found **184 papers** in PNAS (88), *Nature* (83), *Cell* (8)
and *Science* (5), 2021–2026, that used PLINK — for variant QC, PCA / LD pruning
before population-structure analysis, and association testing. Of the 100 papers
that name a version, 84 name a 1.9 build (`1.9`, `1.90`, `1.90b…`) and 13 name 2.0.
The QC and statistical core of both versions was read on `master` and every
suspicion was run through the binaries built from the audited tree (1.9 linked
against a locally built OpenBLAS; 2.0 from `2.0/build_dynamic`), on synthetic
genotypes with known truth against exact rational arithmetic, scipy/statsmodels
and independent ports. The confirmed finding was additionally run on PLINK 1.9
built from the tags `v1.9.0-b.7.12` (2026-09-01, the latest 1.9 release tag),
`v1.90b4` (2017-03-20) and commit `52f7793` (`v1.90b6.21`, 2020-10-19, the build
the cohort names most often), each built with `NO_LAPACK`.

## Findings (details and line citations in [`component-reviews/qc-and-association-core.md`](component-reviews/qc-and-association-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **PL1** | **CONFIRMED on `master`, `v1.9.0-b.7.12`, `v1.90b6.21`, `v1.90b4`; PLINK 2.0 unaffected** | PLINK 1.9 `--hwe` (and `--hwe midp`) removes variants whose exact HWE p-value is *above* the threshold when the variant has 2 or 3 heterozygotes: `SNPHWE_t`/`SNPHWE_midp_t` never compare the second element of the observed tail against the threshold when the other tail has ≤ 1 element, so the filter tests p − P(hets − 2) < t. Exhaustive over 67,883 tables (n ≤ 200, ≤ 6 hets): every 2-het table and 9,600 of 9,697 3-het tables flip at a threshold below their p (by up to 5 % of p; up to 14 % with `midp`); plink2's `HweThreshLn` on the same tables: 0. Command line: a variant with `--hardy` P = 0.4805 is removed by `--hwe 0.48`; a 2-het/5/1000 variant with p = 1.905e-12 is removed at thresholds within 6e-5 of its p. `--hardy` output is correct. Patch (28 lines) brings the exhaustive count to 0 and keeps every case. |
| N1 | note, documentation | `--het` defaults to `E(HOM) = 1 − 2pq` in both versions; `small-sample` applies 2n/(2n − 1); `F` moves by up to 3e-3 between the two on 200 samples. |
| N2 | note, documentation | `--ld` reports the EM haplotype r² (0.707983 on the test pair), `--r2` the genotype correlation (0.720079); both verified against their definitions. |
| N3 | note, design | `--indep-pairwise` pruned sets differ between 1.9, 2.0 and a port of the documented window scan by 1–4 of 120 variants although every r² agrees to 5e-7; the within-window removal order is implementation-defined. |
| N4 | note, **open** | plink2 `--score center` with default mean imputation differs from plink 1.9 `center` and from the reference by up to 6.5e-2 in `SCORE1_AVG` (8 % missing calls); `center no-mean-imputation` and every other mode agree to ≤ 5e-5. Cause not traced in this session — executed discrepancy, not yet a finding. |
| N5 | note, cosmetic | plink 1.9 `--adjust` does not order tied p-values stably; all adjusted columns are right. |

Three own suspicions were withdrawn by execution and are recorded in the review
(a `--adjust` GC-column df mismatch that was the reference's 4-digit input; a
KING mismatch and plink2 `--freq`/`--glm` orientation mismatches that were harness
errors).

**Held up under execution:** HWE exact p and mid-p on all 40,670 tables with n ≤ 60
(1.1e-15) and Fisher on all 271,500 2 × 2 tables with N ≤ 40 (2.4e-15), both
versions; `--hardy`, `--hwe` at 0.05/1e-3/1e-6 away from the boundary (12 runs,
0 differences); `--freq`, `--missing`; allelic/trend/genotypic tests, logistic and
linear regression with covariates, plink2 `--glm`; all `--adjust` columns and the
GC λ; `--r2`, `--ld`; `--genome` against a first-principles PLINK 1.07 port;
`--make-king-table` and `--king-cutoff`; `--score` in every mode but N4. Not
audited: `--pca`, `--clump`, `--fst`, chrX/haploid paths, `--indep` (VIF), dosage
input, permutations, `--homozyg`, `--check-sex`, I/O.

## How the papers use PLINK (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 69 by regex (100 in the survey's own column: 1.9 ×50, 1.90b ×18, 2.0 ×10, 1.90 ×10, 1.90b6.21 ×5, 2.00a ×3, 1.07 ×3, 1.90b6.26 ×2, …) |
| PLINK 1.9 named / PLINK 2 named / 1.07 named | 77 / 36 / 3 |
| PCA | 51 |
| GWAS / regression (`--glm`, `--linear`, `--logistic`) / covariates / Firth | 45 / 21 / 13 / 5 |
| MAF filter / missingness filter / MAC filter | 32 / 17 / 2 (MAF cutoffs: 0.05 ×5, 5 % ×3, 0.01 ×2, 1 % ×2, 0.001, 0.1) |
| LD pruning / parameters stated | 29 / 19 (`200 25 0.4` ×6, then one each of `1000 100 0.8`, `50 5 0.4`, `50 10 0.1`, `50 5 0.5`, `200 25 0.2`, `50 5 0.2`, `200 100 0.05`, `200 100 0.1`, `200 20 0.2`) |
| relatedness / IBD (`--genome`, KING, PI_HAT) | 23 |
| imputed / dosage data | 22 |
| `--clump` / `--r2`,`--ld` / ROH / Fst / `--het` | 17 / 16 / 16 / 15 / 10 |
| `--adjust`, GC λ, multiple testing / 5e-8 | 11 / 10 |
| polygenic score (`--score`) | 5 |
| HWE filter (`--hwe`) / threshold stated | 4 / 1 (`1.0 × 10−6`) |
| population-genetics context (ADMIXTURE, EIGENSOFT, ancient DNA) | 63 |
| REGENIE / SAIGE / BOLT / GCTA / fastGWA / GEMMA / LDSC / METAL co-used | 63 |

Exposure by finding: PL1 needs PLINK 1.9 with `--hwe` (4 papers name the filter in
the cache, 84 name a 1.9 version); the cache is a few hundred characters per paper,
so most `--hwe` uses are invisible to it. Whether any exposed paper lost a variant
depends on a 2- or 3-heterozygote variant having its p within ~10⁻⁴ of the threshold,
which cannot be decided from the papers.

**Profiling caveat.** As for the Seurat, Scanpy and Cutadapt audits, this session had
no route to Europe PMC, so `plink_profile.py` ran in `--offline` mode over the
survey's stored evidence snippets; every record in `plink_profiles.jsonl` is
`source: survey_cache` and every count above is a lower bound. Rerun without
`--offline` from a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- No `CONTRIBUTING`, no issue or PR template, no changelog file in the repository;
  `.github/workflows/` runs the plink2 functional tests (`2.0/Tests/run_tests.sh`)
  and the pgenlib wheel build. PLINK 1.9 has `1.9/tests/` (a dataset generator and
  `tests.py` comparing against a PLINK 1.07 build), no unit tests, and its README
  says active feature development ended in 2016 — bug fixes are still landing (the
  `v1.9.0-b.7.12` tag is from 2026-09-01).
- The top-level README names the plink2-users Google group as the technical-support
  forum; bug reports with a reproduction have historically gone to GitHub issues.
- No prior issue matches PL1 (tracker searched 2026-09-03 with four phrasings;
  nearest is #128 "`--hwe 0` still filters out variants", closed). **The kit is in
  [`upstream/`](upstream/)**: an issue text with an MCVE run on `master`, the latest 1.9
  tag, the cohort's most-cited 1.9 build and the patched build; a `git am`-able patch
  on `8bfebe8` (fix only — 1.9 has no unit-test runner; the MCVE and the exhaustive
  harness are the tests, and their before/after numbers are in the kit README); a PR
  body; and the list of documents read.

## Files

| file | what |
|---|---|
| `plink_profile.py`, `plink_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/qc-and-association-core.md` | the review: PL1, N1–N5, withdrawn suspicions, held-up list, not-audited list |
| `verify/synth.py`, `verify/exact_ref.py` | shared: PED/MAP writer, binary paths, exact rational HWE / Fisher references |
| `verify/stats_driver19.c`, `verify/stats_driver2.cc` | drivers linking the shipped exact-test functions from the build objects (build commands below) |
| `verify/pl1_hwe_threshold_boundary.py` (+ `.out`, `.patched.out`) | PL1: exhaustive bisection of the flip threshold through both drivers; CLI cases on three tables |
| `verify/version_scope_hwe_cli.py` (+ `.master.out`, `.v1.9.0-b.7.12.out`, `.v1.90b6.21.out`, `.v1.90b4.out`, `.patched.out`) | PL1 through the command line on every 1.9 build |
| `verify/heldup_exact_tests_exhaustive.py` (+ `.plink19.out`, `.plink2.out`) | held-up: HWE (n ≤ 60) and Fisher (N ≤ 40) exact values, threshold grid |
| `verify/heldup_hardy_cli.py` (+ `.out`, `.patched.out`) | held-up: `--hardy` / `--hardy midp` / `--hwe` at three thresholds, both versions; rerun with the patched 1.9 build |
| `verify/heldup_freq_missing_het.py` (+ `.out`) | held-up: `--freq`, `--missing`, `--het` (N1) |
| `verify/heldup_ld_prune_r2.py` (+ `.out`) | `--indep-pairwise` (N3), `--r2`, `--ld` with EM reference (N2) |
| `verify/heldup_king_genome.py` (+ `.out`) | `--make-king-table`, `--king-cutoff`, `--genome` |
| `verify/heldup_score.py` (+ `.out`) | `--score` modes, both versions (N4) |
| `verify/assoc_glm_adjust.py` (+ `.out`) | `--assoc`/`--model`/`--logistic`/`--linear`/`--glm`/Firth, `--adjust` columns (W1, N5) |
| `upstream/` | filing kit: issue text, MCVE + outputs, patch 0001, PR body, documents read |

**Building what the harnesses need.** From a clone at `8bfebe8`: PLINK 2.0 with
`cd 2.0/build_dynamic && make` after pointing `BLASFLAGS`/`CXXFLAGS` at an OpenBLAS
build (the `-lopenblas` system package is absent here; OpenBLAS 0.3.29 was built into
`scratchpad/plink/blas/`); PLINK 1.9 with `cd 1.9 && make ZLIB=-lz BLASFLAGS=<openblas>`;
older 1.9 tags with `make NO_LAPACK=1 CFLAGS="-Wall -O2 -DNOLAPACK -I../2.0/simde"
ZLIB=-lz` (v1.90b4: a direct `g++ -DNOLAPACK -x c++ *.c Rconnection.cc -lz -lpthread
-ldl` after copying `zlib-1.2.11/zlib.h` from a later checkout). The drivers link
`stats_driver19.c` with every `1.9/*.o` except `plink.o`, and `stats_driver2.cc`
with every `2.0/build_dynamic/*.o` except `plink2.o`/`plink2_cpu.o`, plus the OpenBLAS
archive. Harness paths are set by `PLINK19`, `PLINK2`, `STATS_DRIVER19`,
`STATS_DRIVER2` (defaults in `verify/synth.py`); the Python side needs numpy, scipy
and statsmodels (Python 3.12 venv).

Environment limits: no R, no Europe PMC, no `github.com` HTML; git clones and
`mcp__github__search_issues` worked. No PLINK 2.0 release tag was built in addition
to `master` because no finding involves 2.0.

## Next steps

1. File PL1 from the kit (issue, then the PR); record the numbers here and in the
   top-level table.
2. Trace N4 (plink2 `--score center` with imputed dosages) in `plink2_misc.cc`
   and either withdraw it or promote it to a finding with a patch.
3. Extend the review to `--pca` variance explained, `--clump`, `--fst`, chrX
   handling in `--hardy`/`--hwe`/`--freq`, and dosage input to `--score`/`--glm`.
4. Full-text profiling rerun when Europe PMC is reachable, to count `--hwe` users
   and thresholds properly.
