# BCFtools: the numbers that reach a methods section

_Read on `samtools/bcftools` `develop` @ **`7abcc0d67cce011e670da2603dbb0b42538fb99f`**
("Fix a segfault caused by incorrect handling of symbolic ALT alleles", 2026-09-09),
built against `samtools/htslib` `develop` @ `e503e04` — `bcftools 7abcc0d / Using htslib
1.24-1-ge503e04`. Every `file:line` below is on that commit. Executed as well: the release
tags **1.24**, **1.13**, **1.10.2** and **1.9**, each built against its own HTSlib
(1.24, 1.13, 1.10, 1.9)._

The scope is the code that turns reads and genotypes into published numbers:
`mpileup`'s genotype likelihoods and per-site annotations, `call -m` and `call -c`,
`stats`, `+fill-tags`, `norm`, and the `filter`/`view` expression evaluator. Plotting,
indexing, format conversion and the I/O layer are out of scope.

## Findings

| id | status | tier | what |
|---|---|---|---|
| **BF1** | **CONFIRMED on `develop` (`7abcc0d`), 1.24 and 1.13** | **now** | `mpileup`'s Mann-Whitney bias annotations (`MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`, `MQSBZ`, `NMBZ`) accumulate the tie correction in a 32-bit `int`; once any one quality/position bin at a site holds 1291 reads the term overflows and the reported \|Z\| is too small. |
| N1 | note, verified | held | `stats` `PSC` `average depth` is the mean over genotypes with `DP > 0`, not over all genotypes. |
| N2 | note, verified | held | `stats` `DP` distribution omits genotypes with `DP = 0` entirely, so the bins do not sum to the number of genotypes. |
| W1 | **WITHDRAWN** | — | I expected `norm -m -any` to write `.` for the allele that moved to the other record; it writes `0`, which is what `--multi-overlaps [0]` documents. |
| W2 | **WITHDRAWN** | — | I expected `bam2bcf.c:506` to index a 60-cell array with `mapQ = 60` (BWA's maximum). Lines 492–493 clamp `baseQ` and `mapQ` to 59 first; there is no out-of-bounds write. |
| W3 | **WITHDRAWN** | — | I expected `+fill-tags`' `HWE`/`ExcHet` to be a chi-square or a mid-p approximation. They are the exact Wigginton–Cutler–Abecasis test and agree with an independent implementation to float32 precision on 40 sites. |

---

## BF1 — the Mann-Whitney bias Z-scores overflow at 1291 reads in a bin

**Status: CONFIRMED.** Harnesses: [`verify/bf1_mwu_tie_overflow.py`](../verify/bf1_mwu_tie_overflow.py)
(end to end, through `bcftools mpileup` on synthetic BAMs) and
[`verify/bf1b_mwu_unit_surface.py`](../verify/bf1b_mwu_unit_surface.py) (the shipped
`calc_mwu_biasZ()` linked straight out of the audited build's `bam2bcf.o`).

### The code

`mpileup` writes six bias annotations, all from one function
(`bam2bcf.c:1171`, `:1174`, `:1176`, `:1178`, `:1180`, `:1182`, `:1185`):

| INFO tag | call |
|---|---|
| `RPBZ` | `calc_mwu_biasZ(bca->ref_pos, bca->alt_pos, bca->npos, 0, 1)` |
| `MQBZ` | `calc_mwu_biasZ(bca->ref_mq, bca->alt_mq, bca->nqual, 1, 1)` |
| `BQBZ` | `calc_mwu_biasZ(bca->ref_bq, bca->alt_bq, bca->nqual, 0, 1)` |
| `MQSBZ` | `calc_mwu_biasZ(bca->fwd_mqs, bca->rev_mqs, bca->nqual, 0, 1)` |
| `SCBZ` | `calc_mwu_biasZ(bca->ref_scl, bca->alt_scl, 100, 0, 1)` |
| `NMBZ` | `calc_mwu_biasZ(bca->ref_nm, bca->alt_nm, B2B_N_NM, 0, 1)` |

`calc_mwu_biasZ()` (`bam2bcf.c:817`) is the tie-corrected normal approximation of the
Mann-Whitney U test. Its accumulators are declared at `bam2bcf.c:828`:

```c
    int e = 0, l = 0, na = 0, nb = 0;
```

and the tie correction is built at `bam2bcf.c:846-847`:

```c
            int p = a[i]+b[i];
            t += (p*p-1)*p;  // adjustment score for ties
```

`t` is `int64_t`, but `(p*p-1)*p` is evaluated in `int`. `p` is the number of reads in
one histogram bin, so the term is cubic in the depth of that bin: it leaves the range of
a 32-bit `int` at **p = 1291** (1290³ = 2,146,689,000 ≤ INT32_MAX < 1291³ =
2,151,685,171). The wrapped value is used at `bam2bcf.c:859`:

```c
    double var2 = (na*nb)/12.0 * ((na+nb+1) - t/(double)((na+nb)*(na+nb-1)));
```

Two further overflows sit in the same function and are fixed by the same change:
`m = na*nb / 2.0` (`bam2bcf.c:856`) and `(na*nb)/12.0` and `(na+nb)*(na+nb-1)`
(`bam2bcf.c:859`) are `int` products, and `e`/`l` are `int` accumulators of quantities of
order `na·nb`; those bite at ~46,000 reads rather than 1,291 and were not reached in a
pileup here, so they are fixed by reading, not by a reproduction.

### Why 1291 reads at a site is not exotic

Two properties make the threshold much lower than "1291× coverage".

1. **The histograms are per site, not per sample.** `bcf_callaux_clean()`
   (`bam2bcf.c:197`, memsets at `:199-210`) is called once per pileup position from
   `mpileup.c:580` and `:593`, after all input files have been processed. A cohort
   `bcftools mpileup -f ref.fa s1.bam … sN.bam` pools every sample's reads into the same
   `ref_mq` / `ref_bq` / `ref_pos` bins.
2. **One bin holds nearly the whole pileup.** `bam2bcf.c:492-493` clamps `baseQ` and
   `mapQ` to 59 and `nqual` is 60, so bin 59 is "MQ ≥ 59". BWA-MEM, Bowtie2 and
   minimap2 give their maximum MQ (60) to the great majority of uniquely mapped reads, so
   at an ordinary site `ref_mq[59]` ≈ the number of reads at the site. The same is true of
   `ref_bq[59]` on any data whose base qualities are capped at or above 59 by the
   sequencer's binning.

So the trigger is roughly *total reads at the site ≥ 1291* — reached by 30 samples at
100×, 44 samples at 30× WGS, 13 exomes at 100×, or one deep amplicon/mitochondrial
pileup run with `-d` above the default 250.

### What was executed

`verify/bf1b_mwu_unit_surface.py` links `calc_mwu_biasZ()` out of the audited build's
`bam2bcf.o` into a five-line C driver, so the arithmetic tested is the shipped
arithmetic. Truth is the same statistic in exact Python integers, cross-checked against
`scipy.stats.mannwhitneyu` (asymptotic, tie-corrected, no continuity correction) on a
case small enough to expand — they agree to |Z| 12.925547 vs 12.925547
([`bf1b_mwu_unit_surface.out`](../verify/bf1b_mwu_unit_surface.out)).

**The boundary is exactly where the arithmetic says it is** (one bin of `p` reads plus
40 alt reads in a second bin):

| p | p³ | int32 | truth Z | bcftools Z |
|---|---|---|---|---|
| 1290 | 2,146,689,000 | fits | −35.9942 | −35.9942 |
| **1291** | **2,151,685,171** | **overflows** | **−36.0077** | **−7.7068** |

**The error only ever goes one way.** Over a 431-pileup sweep (5 % alt fraction, total
reads at the site from 1,300 to 200,000), 430 pileups get a wrong Z, in **0** of them is
|Z| too large, in 0 does it collapse to exactly 0, in 0 does it become nan/inf. This
follows from the arithmetic: wrapping a positive `int` product can only lower it, `t` is
subtracted inside `var2`, so `var2` is always too large and |Z| always too small. The
worst case in the sweep: truth −312.1465 reported as −84.4097.

**It changes filtering verdicts.** `MQBZ < -3` is the mapping-quality-bias cut in the
bcftools/samtools calling workflow and the filter recipes built on it. Sweeping 160
pileups (total reads × alt fraction × fraction of alt reads at the lower MQ), 139 get a
wrong Z and in **41 the `MQBZ < -3` verdict flips from drop to keep** — for example a
1,500-read site whose true MQBZ is −12.13 is annotated −0.83.

End to end through `bcftools mpileup` on BAMs built by the harness
([`bf1_mwu_tie_overflow.out`](../verify/bf1_mwu_tie_overflow.out)):

| case | reads (files) | largest bin | truth Z | reported | verdict |
|---|---|---|---|---|---|
| A | 1,240 (1) | 1,200 | −21.6984 | −21.6984 | matches |
| B | 1,500 (1) | 1,460 | −23.9783 | −5.75778 | wrong |
| C | 3,000 (30) | 2,950 | −31.0770 | −6.87849 | wrong |
| D | 3,000 (1), mild bias | 2,990 | −13.8048 | −1.40338 | wrong |
| F | 1,500 (1), `BQBZ` | — | −27.0962 | −5.69437 | wrong |

Case D is the one that matters most for practice: a real bias with |Z| = 13.8 is
annotated as |Z| = 1.4, i.e. as no bias at all.

The `.out` files also carry a third column, an int32-wrapping replica of the C code
written independently in Python. It reproduces `bcftools`' output to 4 decimal places in
every wrong case, which is what identifies the defect as this overflow and not something
else.

### Version scope (executed, not inferred)

| version | `MQBZ` at 1,240 reads | at 1,500 reads | |
|---|---|---|---|
| 1.9 | tag absent | tag absent | **unaffected — the annotation does not exist** |
| 1.10.2 | tag absent | tag absent | **unaffected — the annotation does not exist** |
| 1.13 | −21.6984 | −5.75778 | **affected** |
| 1.24 (latest release) | −21.6984 | −5.75778 | **affected** |
| `develop` `7abcc0d` | −21.6984 | −5.75778 | **affected** |
| `develop` + patch `22e3099f` | −21.6984 | −23.9783 | fixed |

(`upstream/mcve_outputs.txt`, and `verify/bf1_mwu_tie_overflow.v*.out`.) `calc_mwu_biasZ`
and the `*BZ` tags do not exist in 1.9 or 1.10.2 — `grep -c calc_mwu_biasZ bam2bcf.c`
returns 0 in both, and those releases emit the older `MQB`/`BQB`/`RPB` p-values from
`calc_mwu_bias_cdf()`, which has no tie correction at all (it is commented out at
`bam2bcf.c:725-730`) and no overflow. The two most-cited versions in this cohort (1.9,
1.10.2) therefore predate the annotation; every version from 1.11 on that ships this
function carries the defect, and 1.13 and 1.24 were executed.

`calc_mwu_bias_cdf()` (`bam2bcf.c:715`) and `calc_mwu_bias()` (`bam2bcf.c:760`) have no
callers left in the tree on `7abcc0d` and were not patched.

### The fix

`upstream/0001-mpileup-compute-the-Mann-Whitney-bias-Z-scores-in-64.patch`: `e`, `l`,
`na`, `nb` and the per-bin `p` become `int64_t`, which fixes the tie term and the `na*nb`
products in the mean and variance at the same time. Plus `test/test-mwu.c`, a C unit test
in the style of `test/test-rbuf` and `test/test-regidx`, checking `calc_mwu_biasZ()` on
either side of the boundary and on a 30-sample pileup, wired into `TEST_PROGRAMS` and both
`check-*` targets; and a `NEWS` bullet. `make test` numbers are in
[`../upstream/README.md`](../upstream/README.md).

---

## N1 — `stats` `PSC` `average depth` conditions on `DP > 0`

**Status: NOTE (verified, arguably a design choice, not a wrong number at master).**
Harness: [`verify/heldup_stats.py`](../verify/heldup_stats.py).

On a 400-site, 4-sample synthetic VCF, `bcftools stats -s -` reports sample `s0`
`average depth` = **93.4**. The mean over that sample's genotypes with `DP > 0` is
**93.42**; the mean over all 400 genotypes, counting the 25 with `DP = 0` (and the
missing ones), is **67.73**. Neither the man page nor the `PSC` header row says which
denominator is used. A paper that quotes "mean depth from `bcftools stats`" is quoting
the first number. Not a wrong number — a documentation gap on a number that is copied
into methods sections.

## N2 — the `DP` distribution drops zero-depth genotypes

**Status: NOTE (verified).** Same harness.

The `DP` rows of `bcftools stats` bin genotype and site depths. On the same file, 6
genotype bins and 254 site bins were checked against a Python recount and all agree —
but the **803 genotypes with `DP = 0` appear in no bin at all**, so the genotype `DP`
histogram sums to fewer entries than there are genotypes. Anyone normalising the `DP`
rows to a fraction gets a denominator that excludes uncovered genotypes.

---

## What held up (executed, not just read)

Everything below was run against the built `develop` binary on synthetic data whose truth
is known, and matched.

- **`mpileup` genotype likelihoods and per-site annotations**
  ([`heldup_mpileup_pl.out`](../verify/heldup_mpileup_pl.out)). Two samples, a
  three-allele site, in four option settings (defaults; `-Q 13`; `-Q 20 -q 30`;
  `-Q 30 -q 20`): the full `PL` vector, `AD`, `SP` and the 16 `I16` fields all reproduce
  from the read qualities. 0 mismatches. `-Q` and `-q` remove exactly the reads they say
  they remove (`AD` 38,25,7 → 34,24,6 → 23,14,3 → 17,10,2).
- **`call -m` and `call -c`** ([`heldup_call_m.out`](../verify/heldup_call_m.out)).
  1,680 `GT`/`GQ`/`PL` values over 60 sites reproduce from an independent Python
  implementation of the multiallelic caller's posterior; `-v`, `--ploidy 1` and `-P 0.1`
  likewise (1,059 and 1,680 values, `QUAL`/`AN` over 60 sites); `call -c` assigns
  `0/0`, `0/1`, `1/1` for `PL` (0,60,200), (80,0,90), (220,70,0) and `QUAL` 255.243 /
  74.3083 as expected. **0 mismatches in 4,419 compared values.**
- **`+fill-tags`** ([`heldup_fill_tags_hwe.out`](../verify/heldup_fill_tags_hwe.out)).
  440 values over 40 sites — `AF`, `AC`, `AN`, `MAF`, `F_MISSING`, `HWE`, `ExcHet` —
  against an independent implementation. The `HWE` p-value is the **exact**
  Wigginton–Cutler–Abecasis test and agrees to float32 precision (e.g. 44 het / 5 hom-alt
  / 11 hom-ref → 0.000273079 both ways); `ExcHet` is the one-sided excess-heterozygosity
  tail (0.000240604). Haploid genotypes and missing calls are handled the way the
  independent implementation does. On a three-allele site `MAF` is the second-largest
  allele frequency counting REF, which is the correct definition of minor allele
  frequency. **0 mismatches.**
- **`norm`** ([`heldup_norm_split_join.out`](../verify/heldup_norm_split_join.out)).
  Left-alignment of 120 indels (homopolymers, di/tri/tetranucleotide repeats, padded
  representations) — **0 differ** from an independent Python left-aligner (`norm`'s own
  summary line reports 101 of the 120 realigned). `-m -any` splitting recomputes `AC`/`AF` correctly
  (2/0.25 and 3/0.375 for the constructed genotypes), takes the right slots out of
  `Number=A`, `Number=R` and `Number=G` fields (`AD`, `PL`), and `-m +any` joins them back
  to the original `GT`, `AD` and `AC`/`AF`, with the un-recoverable `1/2` `PL` cell
  written as `.`. **0 mismatches.**
- **`filter` / `view` expressions**
  ([`heldup_filter_expressions.out`](../verify/heldup_filter_expressions.out)). **47
  expressions** over a 300-site, 5-sample VCF with missing values sprinkled through
  `QUAL`, `INFO/DP`, `FMT/DP` and `GT`, each checked two ways: the site set matches an
  independent Python evaluator, and `-e` selects exactly the complement of `-i`.
  Covered: `"."` and `!="."` comparisons on `QUAL` and `INFO/DP`; `&` (same sample) vs
  `&&` (any sample) — `FMT/DP>10 & FMT/GQ>=20` selects 161 sites where `&&` selects 220,
  the documented difference; `MIN`/`MAX`/`AVG`/`MEDIAN`/`SUM`/`STDEV`; `COUNT`,
  `N_PASS`, `F_PASS`, `F_MISSING`, `SMPL_MAX`, `SMPL_SUM`; `GT="het"/"hom"/"mis"/"RR"/
  "AA"/"alt"`; `binom(FMT/AD)` and `fisher(INFO/DP4)`. **0 mismatches.**
- **`stats`** ([`heldup_stats.out`](../verify/heldup_stats.out)). `SN` record/SNP/indel/
  multiallelic counts and `TSTV` (400 records, ts/tv 0.43) reproduce; the `PSC` per-sample
  row (`nRefHom`, `nNonRefHom`, `nHets`, `nTs`, `nTv`, `nIndels`, `nSingletons`,
  `nHapRef`, `nHapAlt`, `nMissing`) reproduces; `--af-bins 0.1,0.3,0.6` with `--af-tag AF`
  puts 106 / 112 / 115 SNP alleles in the three bins, matching an independent binning.
  **0 mismatches** apart from the two semantics notes above.
- **BF1's own boundary and direction**, at the unit level, against `scipy` — see above.

## Not audited

- `bcftools merge` (the `AF`/`AC` merge rule and the `PL`/`GT` written for a sample
  absent from one input), `roh`, `gtcheck`, `csq`, `cnv`, `consensus`, `concat`,
  `annotate`, `query`, `isec`, `+split-vep` and the other plugins.
- The **indel** side of `mpileup`: the indel candidate generation, the realignment in
  `bam2bcf_indel.c` / `bam2bcf_iaux.c` / `bam2bcf_edlib.c`, `IDV`/`IMF`, and the
  `--indel-bias`/`--indel-size` options. Only SNP `PL`/`AD`/`I16` were reproduced.
- **BAQ**, which lives in HTSlib (`probaln_glocal`), and the `--redo-BAQ` path.
- The exact-calculation branch of `calc_mwu_biasZ()` (`na < 8 && nb < 8`,
  `mann_whitney_1947`), which is unreachable from the `do_Z = 1` callers.
- `call --ploidy` from a ploidy file, `--constrain alleles`, `--gvcf`, and the `call -C
  trio` paths.
- CRAM input, region/target indexing, multithreading, and every output format question.
