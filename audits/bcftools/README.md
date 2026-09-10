# BCFtools audit against 202 published papers (2021–2026)

_Generated 2026-09-10 against `samtools/bcftools` `develop` @ `7abcc0d` built with
`samtools/htslib` `develop` @ `e503e04` ("bcftools 7abcc0d / Using htslib
1.24-1-ge503e04"). Focus: the code that turns reads and genotypes into published
numbers — `mpileup`'s genotype likelihoods and bias annotations, `call -m`/`-c`,
`stats`, `+fill-tags`, `norm`, and the `filter`/`view` expression evaluator — verified by
executing the built binaries on synthetic data whose truth is computed independently in
Python and scipy._

## What this is

The six-journal survey found **202 papers** in *Nature* (98), PNAS (86), *Cell* (13) and
*Science* (5), 2021–2026, that used BCFtools — the variant-calling half of the
samtools/htslib stack and the second most-used genomics tool in the survey. Its numerical
core was read on `develop` and every suspicion was run through four builds: `develop`
(built here against HTSlib `develop`) and the release tags **1.24**, **1.13**, **1.10.2**
and **1.9**, each against its own HTSlib. Truths are independent Python implementations —
the multiallelic caller's posterior, the exact Wigginton–Cutler–Abecasis HWE test, a
left-aligner, a filter-expression evaluator, and `scipy.stats` for the Mann-Whitney and
binomial tests.

## Findings (details and line citations in [`component-reviews/mpileup-and-annotation-core.md`](component-reviews/mpileup-and-annotation-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **BF1** | **CONFIRMED on `develop` (`7abcc0d`), 1.24 and 1.13** | **now** | `bcftools mpileup` builds the tie correction of its Mann-Whitney bias annotations (`INFO/MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`, `MQSBZ`, `NMBZ`) as `int p = a[i]+b[i]; t += (p*p-1)*p;` in 32-bit `int` (`bam2bcf.c:846-847`). `p` is the number of reads in one quality or position bin, so the term overflows at **p = 1291** (1290³ = 2,146,689,000 ≤ INT32_MAX < 1291³). The bins are filled once per *site* across all input files and MQ is clamped to bin 59, where most aligners put most reads, so the trigger is simply 1291 reads at the site — 30 samples at 100×, 44 at 30× WGS, or one deep amplicon pileup. The wrap is always downward, so `var2` is always too large and the reported \|Z\| always too small: on a 1,500-read site `MQBZ` is **−5.75778** where the tie-corrected Mann-Whitney Z is **−23.9783**; on 3,000 reads over 30 files, **−6.87849** for a true **−31.0770**. Over a 431-pileup sweep, 430 are wrong and \|Z\| is too large in **0** of them. Over 160 realistic pileups, **41 flip the `MQBZ < -3` verdict from drop to keep** (a 1,500-read site with true MQBZ −12.13 is annotated −0.83). 1.9 and 1.10.2 do not have the annotation at all. |
| N1 | note, verified, documentation | held | `bcftools stats -s -` reports `PSC` `average depth` **93.4** for a sample whose mean over genotypes with `DP > 0` is 93.42 and whose mean over all 400 genotypes is 67.73: the denominator excludes zero-depth genotypes and is not documented. |
| N2 | note, verified, documentation | held | The `stats` `DP` distribution omits genotypes with `DP = 0` from every bin (803 of them on the test file), so the genotype `DP` histogram does not sum to the number of genotypes. |

Three own suspicions were withdrawn by execution (`norm -m -any` was thought to write `.`
for the allele that moved to the other record — it writes `0`, the documented
`--multi-overlaps` default; `bam2bcf.c` was thought to index a 60-cell array with MQ 60 —
it clamps to 59 first; `+fill-tags` `HWE` was thought to be an approximation — it is the
exact test) and are recorded in the review.

**Held up under execution:** `mpileup` `PL`, `AD`, `SP` and all 16 `I16` fields on a
two-sample three-allele site in four `-Q`/`-q` settings (0 mismatches); `call -m` `GT`,
`GQ`, `PL`, `QUAL` and `AN` against an independent implementation of the multiallelic
posterior, with `-v`, `--ploidy 1` and `-P 0.1` (**0 mismatches in 4,419 values**) and
`call -c`; `+fill-tags` `AF`/`AC`/`AN`/`MAF`/`F_MISSING`/`HWE`/`ExcHet` (440 values over
40 sites, the exact Wigginton HWE p-value to float32 precision, multiallelic sites
included); `norm` left-alignment on 120 constructed indels (0 differ from an independent
left-aligner) and the `AC`/`AF`/`AD`/`PL`/`GT` arithmetic of `-m -any` split and
`-m +any` join; **47 `filter`/`view` expressions** including missing-value comparisons,
`&` vs `&&`, `MIN`/`MAX`/`AVG`/`MEDIAN`/`SUM`/`STDEV`, `COUNT`/`N_PASS`/`F_PASS`/
`F_MISSING`/`SMPL_*`, the `GT="het"/"hom"/"mis"/"RR"/"AA"/"alt"` classes and
`binom()`/`fisher()`, each checked both against a Python evaluator and for `-i`/`-e`
complementarity; `stats` `SN`, `TSTV`, the ten `PSC` per-sample counters, the site and
genotype `DP` bins and `--af-bins`. Not checked: `merge`, `roh`, `gtcheck`, `csq`, the
indel model and realignment, BAQ (which lives in HTSlib), `--constrain`/`--gvcf`, CRAM.

## How the papers use BCFtools (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 56 (1.9 ×30, 1.10.2 ×10, 1.13 ×6, 1.11 ×4, 1.8 ×4, 1.14 ×4) |
| SAMtools also used | 136 |
| PLINK / VCFtools downstream | 80 |
| GATK also used | 76 |
| `mpileup` | 43 |
| VEP / SnpEff / ANNOVAR | 39 |
| indel calling | 38 |
| `call` | 32 |
| long reads (nanopore / PacBio) | 30 |
| mitochondrial | 28 |
| population genetics / GWAS | 26 |
| RNA-seq | 24 |
| other caller (freebayes / DeepVariant / …) | 23 |
| MQ / mapping-quality filter stated | 20 (thresholds: 30 ×6, 20 ×6, 40 ×2) |
| microbial / viral | 20 |
| QUAL threshold stated | 19 (30 ×8, 20 ×5, 25 ×3) |
| ploidy / haploid | 18 |
| WGS / WES / exome | 17 |
| low coverage / imputation (GLIMPSE, BEAGLE) | 16 |
| BAQ / `-B` / `-Q` / `-q` options | 13 |
| ancient DNA | 9 |
| depth threshold stated / `norm` / `roh` | 9 / 9 / 9 |
| `consensus` | 7 |
| `filter`/`view -i/-e` | 5 |
| `call -m` | 4 |
| GATK-style filter expression | 3 |
| `merge` | 3 |
| `+fill-tags` / `annotate` / `stats` / `isec` / `concat` / `call -c` | 1 each |

Exposure for BF1: it needs `mpileup` (43 papers name it) at a site with ≥ 1291 reads, so
either a multi-sample pileup or high depth — 28 papers are mitochondrial (where depth of
thousands is routine), 20 microbial/viral (amplicon panels), 17 WGS/WES cohorts, 16
low-coverage imputation cohorts. It also needs someone to *read* an `*BZ` value, directly
or through a filter expression (5 papers name `filter`/`view`, 3 a GATK-style expression;
subcommand names and filter strings are rarely spelled out in methods, so these are weak
lower bounds). The two most-cited versions in the cohort, 1.9 (30 papers) and 1.10.2
(10), predate the annotation and are unaffected.

**Profiling caveat.** As for the Seurat, Scanpy, Cutadapt and SAMtools audits, this
session had no route to Europe PMC, so `bcftools_profile.py` ran in `--offline` mode over
the survey's stored evidence snippets; every record in `bcftools_profiles.jsonl` is
`source: survey_cache` and every count above is a **lower bound**. Rerun without
`--offline` from a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- **`CONTRIBUTING.md`** — the same document as `samtools/samtools`', word for word in the
  parts that matter: small single-topic PRs against a recent `develop`; documentation and
  **test cases for all PRs**, no huge test files, no remote data in tests; Developer
  Certificate of Origin with a real-name `Signed-off-by:` on every commit; and an **AI
  policy** (credited to the kernel's coding-assistants document) — every AI-generated line
  reviewed by the submitter, `Assisted-by: AGENT:MODEL` on each commit and at the end of
  the PR description, **AI agents may not add sign-offs**, and commit messages and PR
  descriptions written by a human. Acceptance with conditions, not a refusal; the kit's
  commit message and PR body are drafts for the submitter to rewrite and sign. This
  mirrors the handling in [`../samtools/upstream/`](../samtools/upstream/).
- **No issue template and no PR template**: `.github/` holds only `workflows/`. The issue
  text follows the sibling project's `Bug_report.md` order (versions; environment; steps,
  command and output), which is what these maintainers read.
- **`NEWS`** bullets under a `* bcftools <command>` heading in the unreleased
  `## Release a.b` section, usually ending `(#NNNN)`. `make test` runs `test/test-rbuf`,
  `test/test-regidx` and `test/test.pl` (2,480 tests). No linter or formatter
  configuration in the tree.
- BF1 is the only "file now" item, and the only filing: a wrong number under default
  settings on the current release, with no prior issue (tracker searched 2026-09-10 with
  three phrasings; nearest #897, #962, #1930, #1767, #2185 — details in
  [`upstream/README.md`](upstream/README.md)). **The kit is in
  [`upstream/`](upstream/)**: issue text with a self-contained `sh` MCVE (run on six
  builds), one `git am`-able patch (fix + a `test/test-mwu.c` unit test that fails on
  unmodified `develop` + `NEWS` entry; `make test` 2480 passed / 0 failed with the patch
  and on unmodified `develop`, and `test-mwu` fails 2 of its 4 checks without it), and the
  PR body draft. Comment bodies on existing threads cannot be read from this environment,
  so #1930's 14 comments were not read; the issue is drafted as a new issue on the
  strength of its title and body.

## Files

| file | what |
|---|---|
| `bcftools_profile.py`, `bcftools_profiles.jsonl`, `profile_run.log` | profiling pass over the 202 cohort papers (offline; see caveat) |
| `component-reviews/mpileup-and-annotation-core.md` | the review: BF1, N1–N2, three withdrawn suspicions, held-up list, not-audited list |
| `verify/_synth.py` | shared VCF/BAM builders, runner and truth helpers |
| `verify/bf1_mwu_tie_overflow.py` (+ `.out`, `.v1.24.out`, `.v1.13.out`, `.v1.10.2.out`, `.v1.9.out`, `.patched.out`) | BF1 end to end through `bcftools mpileup`, with an int32-wrapping replica of the C code as a third column |
| `verify/bf1b_mwu_unit_surface.py` (+ `.out`, `.patched.out`) | BF1 at the unit level: the shipped `calc_mwu_biasZ()` linked out of `bam2bcf.o`; scipy cross-check, the p = 1291 boundary, the direction sweep, the `MQBZ < -3` verdict sweep |
| `verify/heldup_mpileup_pl.py` (+ `.out`) | held-up: `PL`, `AD`, `SP`, `I16` in four `-Q`/`-q` settings |
| `verify/heldup_call_m.py` (+ `.out`) | held-up: `call -m` (`-v`, `--ploidy`, `-P`) and `call -c` |
| `verify/heldup_fill_tags_hwe.py` (+ `.out`) | held-up: `+fill-tags` `AF`/`AC`/`AN`/`MAF`/`F_MISSING`/`HWE`/`ExcHet` vs the exact Wigginton test |
| `verify/heldup_norm_split_join.py` (+ `.out`) | held-up: `norm` left-alignment and the split/join arithmetic |
| `verify/heldup_filter_expressions.py` (+ `.out`) | held-up: 47 `filter`/`view` expressions |
| `verify/heldup_stats.py` (+ `.out`) | held-up: `SN`, `TSTV`, `PSC`, `DP` bins, `--af-bins`; source of N1 and N2 |
| `upstream/` | filing kit: issue text, MCVE + outputs on six builds, patch 0001 (fix + unit test + NEWS), PR body, documents read, test numbers |

Harnesses take the `bcftools` binary as their first argument (`python verify/<h>.py
/path/to/bcftools`), except `bf1b_mwu_unit_surface.py`, which takes the *build
directory* and the HTSlib directory (`python verify/bf1b_mwu_unit_surface.py <bcftools
src> <htslib src>`) because it links the shipped object file. They need a Python ≥ 3.12
venv with `pysam`, `numpy` and `scipy`. Builds: `autoreconf -i && ./configure && make` in
htslib, then `autoheader && autoconf && ./configure --with-htslib=<htslib> && make` in
bcftools (zlib, bzip2, lzma, curl, libdeflate dev packages).

## Next steps

1. File BF1: the issue from `upstream/issue-bf1-mwu-bias-int-overflow.md`, then the PR
   from the branch `fix/mwu-bias-int-overflow` (commit `22e3099f`) after the submitter has
   reviewed every line, rewritten the message, and added a `Signed-off-by:` — the
   `Assisted-by:` trailer stays, per `CONTRIBUTING.md`. Before posting, read #1930's 14
   comments to be sure BF1 is not already discussed there.
2. Extend the review to the parts left out: `merge`'s `AF`/`AC` rule and the `PL`/`GT` it
   writes for a sample missing from one input, `roh`, `gtcheck`, `csq`, and the indel
   model in `bam2bcf_indel.c`/`bam2bcf_iaux.c`.
3. Full-text profiling rerun when Europe PMC is reachable, to see how many of the 43
   `mpileup` papers pile up multiple samples together or report an `*BZ` filter.
