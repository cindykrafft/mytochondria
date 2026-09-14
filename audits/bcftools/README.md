# BCFtools audit against 202 published papers (2021–2026)

_Generated 2026-09-13 against `samtools/bcftools` `develop` @ `7abcc0d6` built with
`samtools/htslib` `develop` @ `e503e04` ("bcftools 7abcc0d6 / Using htslib
1.24-1-ge503e04"). Focus: the numbers that come out of `mpileup` (genotype
likelihoods, depth and allele counts, the strand/quality/position bias annotations),
`call -m` (QUAL, GT, GQ, AC/AN, the prior, `-v`, `--ploidy`), `+fill-tags`
(AF/AC/AN/MAF/HWE/ExcHet/F_MISSING), `stats`, `norm`, `view`/`filter` expressions and
`merge` — verified by executing the built binaries on synthetic BAMs and VCFs with
independently computed truths._

## What this is

The six-journal survey found **202 papers** in *Nature* (98), PNAS (86), *Cell* (13)
and *Science* (5), 2021–2026, that used BCFtools, mostly for variant calling after
BWA/minimap2 alignment and often alongside GATK, PLINK and VCFtools. Its numeric core
was read in full on `develop` and every suspicion was run through five builds:
`develop` (built here against HTSlib `develop`), the 1.24 release (latest) and 1.13,
1.10.2 and 1.9 built from their tags with matching HTSlib (the cohort's three most-cited
versions), on BAMs built with pysam where every base, quality, MAPQ, strand and
position is known and on hand-written VCFs, with the truths computed in Python
(scipy's Mann-Whitney and Fisher tests, exact rational HWE probabilities, a port of
the multiallelic caller, a left-aligner, the manual's expression semantics).

## Findings (details and line citations in [`component-reviews/numeric-core.md`](component-reviews/numeric-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **BC1** | **CONFIRMED on `develop`, 1.24 and 1.13** (absent from 1.10.2 and 1.9, which predate the annotations) | **now** | `bcftools mpileup` computes the default `INFO/MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`, `MQSBZ` (and `NMBZ`) Mann-Whitney Z-scores with 32-bit `int` accumulators; the tie term `(p*p-1)*p` wraps once one quality or position bin holds 1,291 reads (`p³ > INT32_MAX`), which inflates the variance and shrinks the score towards zero. Because the histograms are pooled over samples and MAPQ is capped at 59 (all BWA MAPQ-60 reads share a bin), this is reached at a single deep site with `-d` raised, and under the **default `-d 250`** in any multi-sample run whose summed reference depth passes 1,290 (about 45 samples at 30×). 1,300 MAPQ-60 reference reads + 40 MAPQ-30 alternate reads: `MQBZ −7.81` for a true −36.47 (1,290 reads: −36.46, correct); 44 single-sample BAMs of 30 reads under default settings: −6.97 for −36.73; 1,530 Q37 bases with binned qualities: `BQBZ −2.47` for −19.42; the score saturates near −11 (12,000 reads: −10.94 for −109.72), so a `MQBZ < -3` filter keeps the artefacts at the deepest sites. An int32-wrap replica reproduces every wrong value; `PL`, `AD`, `DP`, `QUAL` and genotypes are unaffected. |
| N1 | note, verified, documentation | held | `merge` takes an unruled Number=A/R/G INFO tag (e.g. `AF`) from the *last* file carrying the allele (`AF=1` from files with 0.25 and 1; 0.25 with the files swapped) while the manual says "the first input file"; Number=1 tags do come from the first. `AN`, `AC`, `DP` are summed correctly. |
| N2 | note, verified, cosmetic | held | `stats` bins AF on a 99-step grid (`af*(m_af-2)`) but labels rows on a 100-step grid, so AF 0.5 prints as `0.490000`, 0.25 as `0.240000`, 1.0 as `0.990000`; the counts in each row are right. |
| N3 | note, verified, acknowledged in source | held | `+fill-tags` HWE/ExcHet at a multiallelic site count a reference allele for every heterozygote of another ALT (`nref` 320 where pooling gives 330): `HWE=0.3777` vs 0.3712 exact, `ExcHet=0.8727` vs 0.8902. Biallelic sites are exact to 2 × 10⁻⁶. |
| N4 | note, verified, documentation (HTSlib) | held | `mpileup -d` drops reads only when they start at a position whose buffer already exceeds the cap, so per-position depth exceeds it: `INFO/DP` 170 under `-d 100` and 288 under the default 250 with 400 overlapping reads. A memory guard, not a depth cap; it does not prevent BC1. |
| N5 | note, design, verified | held | `call -m` treats a flat PL vector (`0,0,0`, zero coverage) as missing and writes `./.` with GQ 0 rather than `0/0`; the port matches once the rule is included. |
| N6 | note, verified, documentation | held | `stats` PSC `nSingletons` counts any sole non-reference genotype (`1/1`, MNP, indel), not the `SiS` "AC = 1" definition; haploid genotypes are excluded from `nTs`/`nTv`. |

Three own suspicions were withdrawn by execution (the `calc_hwe` midpoint/recurrence
precision; `FORMAT/SP`'s phred rounding; the `I16` sums under the MAPQ 255 → 20 and
60 caps) and are recorded in the review.

**Held up under execution:** `mpileup` `INFO/DP`, `FORMAT/DP`, `DP4`, `AD`/`ADF`/`ADR`,
`INFO/AD`, `SP`, all 16 `I16` sums, `MQ0F` and `call`'s `MQ` under default, `-Q 13`,
`-q 20` and `-Q 20 -q 30` (44 checks); single-read `PL` (`0,3,q`; MAPQ 0 → `0,3,4`); a
3-bp heterozygous deletion through `mpileup | call -mv`; `+fill-tags` `AN`/`AC`/`NS`/
`AC_Het`/`AC_Hom`/`AC_Hemi`/`F_MISSING`/`AF`/`MAF`/`HWE`/`ExcHet` on 24 biallelic
2,000-sample sites and a haploid/phased/half-missing site; a Python port of `call -m`
(QUAL to 10⁻³, GT, GQ, AC, AN, ALT identical) under `-m`, `-mv`, `-P 0.1`, `-P 1e-6`,
`--ploidy 1`; `stats` `SN`, `TSTV`, `SiS`, `AF` row counts, `DP` distribution and all
eleven `PSC` columns; `norm` left-alignment in CAG/A₆/AT repeats and the Number=A/R/G
arithmetic of `-m -`/`-m +`; 42 `view -i` expressions (missing values, `&` vs `&&`,
`|` vs `||`, `MIN`/`MAX`/`AVG`/`MEDIAN`/`SUM`, `sMAX`/`sSUM`, subscripts, `GT` tests,
`N_PASS`/`F_PASS`, on-the-fly `AC`/`MAF`/`F_MISSING`); `merge` `DP`/`AN`/`AC` sums, QUAL
= max, missing samples and the PL/AD expansion across different ALTs. All of it again
on the 1.24 release build. Not checked: the indel model beyond the smoke test, BAQ's
arithmetic, `call -c`, `roh`, `gtcheck`, `csq`, `consensus`, the `VDB`/`SGB` heuristics,
`--gvcf`, CRAM.

**Real-data check of BC1 (2026-09-14).** The finding was verified on synthetic BAMs; whether
its precondition (1,291 or more reads sharing one quality or position bin at a site) occurs in
practice was then tested on two real SARS-CoV-2 amplicon samples (nf-core/test-datasets,
`viralrecon` branch, `illumina/amplicon/sample1` and `sample2`; 27,721 and 21,481 read pairs
aligned with minimap2 to MT192765.1), the kind of data 41 papers in the cohort name. With the
depth cap raised as viral pipelines do (`-d 1000000`; nf-core/viralrecon runs `--max-depth 0`),
2,934 and 1,749 of the 29,829 positions exceed 1,291 reads in a single sample (maximum 2,857),
so the precondition holds across a tenth of the genome. On the consensus variants from
`call -mv --ploidy 1` (6, 15 and 17 sites) only the one deep site changes (`MQSBZ` −0.09 →
−1.59 in sample2; −0.13 → −2.13 pooled) and no filter decision moves. On every site with at
least two alternate reads, the sites a minor-variant analysis looks at, the unpatched and
patched builds differ at 328 (sample1), 769 (sample2) and 4,697 (both samples pooled) sites for
at least one score, most by one or more units, and the two builds fall on different sides of a
`< -3` filter at 231 / 87 / 1,440 sites for `MQBZ` and 141 / 118 / 1,194 for `BQBZ`; the
overflow always shrinks the score towards zero (`MQBZ` −1.26 reported for −21.24 at position
948 of sample1, DP 1,618, 7 alternate reads). Under the default `-d 250` with the two samples
pooled no site reaches the bin size and nothing changes. The multi-sample default-settings route
(about 45 samples at 30×) could not be tested on real data from this session; no such cohort is
reachable. Harness: [`verify/bc1_real_sarscov2_align.py`](verify/bc1_real_sarscov2_align.py) and
[`verify/bc1_real_sarscov2_sites.py`](verify/bc1_real_sarscov2_sites.py) with their `.out` files.

## How the papers use BCFtools (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 56 (1.9 ×31, 1.10 ×12, 1.13 ×6, 1.11 ×4, 1.8 ×4, 1.14 ×4, 0.1.x ×4) |
| aligner named (BWA / Bowtie / STAR / minimap2 / HISAT) | 139 |
| population genetics / GWAS / phasing / imputation named | 82 |
| GATK also used / other caller (freebayes, DeepVariant, …) | 76 / 29 |
| `mpileup` | 43 |
| amplicon / mitochondrial / viral / pooled / metagenomic data | 41 |
| RNA-seq / long reads | 31 / 30 |
| cohort size stated (`N samples/individuals/genomes`) | 26 (1,000 ×11) |
| allele frequency reported / QUAL threshold stated / DP threshold stated | 20 / 18 / 9 |
| `call` / `--ploidy` / GQ stated | 11 / 11 / 10 |
| `norm` / `roh` / `consensus` / `merge` / `stats` / `+fill-tags` or HWE | 9 / 9 / 7 / 3 / 1 / 1 |

Exposure by finding: BC1 needs `mpileup` output filtered or reported on the bias
Z-scores at sites where one quality bin holds ≥ 1,291 reads — deep amplicon,
mitochondrial, viral or pooled data with `-d` raised (41 papers name such data), or a
multi-sample call of roughly 45 or more 30× samples under default settings (26 state a
cohort size, 11 of them 1,000 samples) — on 1.13 or later (the 1.9/1.10 majority of
the cohort predates the annotations). Subcommand and filter names are rarely spelled
out in methods, so these are weak lower bounds. N1–N6 are documentation, cosmetic or
design points.

**Profiling caveat.** As for the Seurat, Scanpy, Cutadapt and SAMtools audits, this
session had no route to Europe PMC, so `bcftools_profile.py` ran in `--offline` mode
over the survey's stored evidence snippets; every record in `bcftools_profiles.jsonl`
is `source: survey_cache` and every count above is a lower bound. Rerun without
`--offline` from a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- `CONTRIBUTING.md` (the samtools text): small single-topic PRs against a recent
  `develop`; tests and documentation with every PR; no huge test files; Developer
  Certificate of Origin with a real-name `Signed-off-by:` on every commit; an **AI
  policy** — every AI-generated line reviewed by the submitter, `Assisted-by:
  AGENT:MODEL` on each commit and at the end of the PR description, **AI agents may not
  add sign-offs**, and commit messages and PR descriptions written by a human. This is
  acceptance with conditions, not a refusal; the kit's commit message and PR body are
  drafts for the submitter to rewrite and sign.
- No issue template and no PR template in the tree (`.github/` holds only workflows);
  `README.md` points bugs to the GitHub tracker and security issues to e-mail.
- `NEWS` entries as `* bcftools <command>` blocks with `- ` bullets under the unreleased
  `## Release a.b` heading; `make test` runs `test/test.pl` (`test_cmd` against `.out`
  files, `test_mpileup` over `.bam`/`.sam`/`.cram` and `-Ob | view`) plus two C unit
  tests; no formatter or linter configuration.
- BC1 is the only "file now" item: a wrong number under default settings on the
  current release, with no prior issue (tracker searched 2026-09-13; nearest #2003,
  #897, #1058, #2185). **The kit is in [`upstream/`](upstream/)**: issue text with an
  `awk`-generated MCVE (run on `develop`, 1.24, 1.13 and the patched build), one
  `git am`-able patch (fix + regression test failing on unmodified `develop` + NEWS
  entry; `make test` 2482 passed / 0 failed with the patch, 2480 / 2 without), and the
  PR body draft. No fork of `samtools/bcftools` exists under `cindykrafft`, so the
  `upstream-declines-ai-contributions` topic could not apply.

## Files

| file | what |
|---|---|
| `bcftools_profile.py`, `bcftools_profiles.jsonl`, `profile_run.log` | profiling pass over the 202 cohort papers (offline; see caveat) |
| `component-reviews/numeric-core.md` | the review: BC1, N1–N6, withdrawn suspicions, design choices, held-up list, not-audited list |
| `verify/_synth.py` | shared reference/BAM/VCF builders (pysam), runner and parsers |
| `verify/bc1_mpileup_mwu_biasZ_int_overflow.py` (+ `.out`, `.v1.24.out`, `.v1.13.out`, `.v1.10.2.out`, `.v1.9.out`, `.patched.out`) | BC1: model check, per-bin sweep across 1,291, binned base qualities, 40–100 single-sample BAMs under default `-d`, BAQ on |
| `verify/bc1_real_sarscov2_align.py`, `verify/bc1_real_sarscov2_sites.py` (+ `.out`) | real-data check of BC1 on two SARS-CoV-2 amplicon samples: alignment, base vs patched mpileup on called variants and on every site with alternate reads, at `-d 1000000` and the default `-d 250` |
| `verify/heldup_mpileup_counts.py` (+ `.out`, `.v1.24.out`) | held-up: DP/DP4/AD/ADF/ADR/SP/I16/MQ0F/MQ under four filter settings, `-d` (N4), single-read PLs, indel smoke test |
| `verify/heldup_filltags_hwe_af.py` (+ `.out`, `.v1.24.out`) | held-up: +fill-tags counts, exact HWE/ExcHet; N3 |
| `verify/heldup_call_m_port.py` (+ `.out`, `.v1.24.out`) | held-up: port of `call -m` (QUAL/GT/GQ/AC/AN, `-v`, `-P`, `--ploidy 1`); N5 |
| `verify/heldup_stats.py` (+ `.out`, `.v1.24.out`) | held-up: `stats` SN/TSTV/SiS/AF/QUAL/DP/PSC; N2, N6 |
| `verify/heldup_norm.py` (+ `.out`, `.v1.24.out`) | held-up: left-alignment, `-m -` / `-m +` arithmetic |
| `verify/heldup_filter_expressions.py` (+ `.out`, `.v1.24.out`) | held-up: 42 expressions, `-e` complement, `filter -s` |
| `verify/heldup_merge.py` (+ `.out`, `.v1.24.out`) | held-up: INFO rules, missing samples, PL/AD expansion; N1 |
| `upstream/` | filing kit: issue text, MCVE + outputs, patch 0001 (BC1), PR body, documents read, test numbers |

Harnesses take the bcftools binary as their first argument (`python
verify/<h>.py /path/to/bcftools`; `+fill-tags` is found in `plugins/` next to the
binary or via `BCFTOOLS_PLUGINS`) and need a Python ≥ 3.12 venv with `pysam`, `numpy`
and `scipy` (`uv venv --python /usr/bin/python3.12 venv && uv pip install pysam numpy
scipy`); set `AUDIT_TMP` to keep scratch files out of `/tmp`. Builds: `git submodule
update --init` in htslib, `autoreconf -i && ./configure && make`, then `autoheader &&
autoconf && ./configure --with-htslib=<htslib> && make` in bcftools (zlib, bzip2,
lzma, curl, gsl-free build).

## Next steps

1. File BC1 (issue, then PR from a fork branch `fix/mwu-biasz-int64` after a human
   review, rewritten commit message and DCO sign-off per `CONTRIBUTING.md`). The notes
   wait for a maintainer signal; N1 is a one-line manual fix worth mentioning in the PR
   discussion.
2. Extend the review to the indel model (`bam2bcf_indel.c`, `--indels-2.0`), BAQ in
   HTSlib, `call -c`, and `roh`/`gtcheck`/`csq`.
3. Full-text profiling rerun when Europe PMC is reachable, to see which papers filter on
   the Z-score annotations and at what depth.
