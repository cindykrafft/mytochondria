# Component: BCFtools numeric core (`develop` @ `7abcc0d6`, 2026-09-13, "bcftools 7abcc0d6 / Using htslib 1.24-1-ge503e04")

Read in full on `develop`: `bam2bcf.c` (1,406 lines; per-read likelihoods, the
DP/AD/ADF/ADR/SP/I16 bookkeeping and the bias annotations of `mpileup`), `mcall.c`
(1,683; `call -m`), `plugins/fill-tags.c` (`+fill-tags`, `calc_hwe`), the counting and
printing parts of `vcfstats.c` (`stats`), the split/join and realignment parts of
`vcfnorm.c` (`norm`), the aggregate functions and vector logic of `filter.c`
(`view -i`/`filter -i`), the INFO-rule and Number=A/R/G handling of `vcfmerge.c`
(`merge`), the defaults in `mpileup.c` and `vcfcall.c`, and in HTSlib `develop` @
`e503e04` `sam.c` `bam_plp_push` (the `-d` cap). Every suspicion was **executed on
built binaries**: `develop` built here against HTSlib `develop`, the 1.24 release
(latest) built from its tag with HTSlib 1.24, and 1.13, 1.10.2 and 1.9 built from
their tags with matching HTSlib (the cohort's three most-cited versions are 1.9, 1.10.2
and 1.13). Harnesses in `../verify/` build BAMs with pysam and VCFs by hand, where every
read, quality, position and genotype is known, and compute every truth independently in
Python (scipy for the Mann-Whitney and Fisher tests; exact rational arithmetic for
HWE; a port of `call -m`; a left-aligner; the manual's expression semantics).

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### BC1 — CONFIRMED on `develop`, 1.24 and 1.13 (absent from 1.10.2 and 1.9): the Mann-Whitney bias Z-scores (`MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`, `MQSBZ`, `NMBZ`) are accumulated in 32-bit `int` and wrap once one quality bin holds 1,291 reads

**Code.** `bcftools mpileup` writes, by default (`mpileup.c:1399`), the Z-score
annotations `INFO/MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`, `MQSBZ` (and `NMBZ` on request),
all computed by `calc_mwu_biasZ()` (`bam2bcf.c:817-885`, called at
`bam2bcf.c:1165-1193`) on two histograms `a[]` (reference reads) and `b[]`
(alternate reads) over at most 100 bins — MAPQ and base quality capped at 59
(`bam2bcf.c:492-493`, `:506-512`), read position scaled to 0–99. The histograms are
pooled **over all samples** of the run (`bca->ref_mq` etc. are per-site, not
per-sample; `bcf_callaux_clean`, `bam2bcf.c:197-233`). The accumulation is

```c
int e = 0, l = 0, na = 0, nb = 0;                    // bam2bcf.c:828
...
        int p = a[i]+b[i];
        t += (p*p-1)*p;  // adjustment score for ties  // bam2bcf.c:846-847
...
double var2 = (na*nb)/12.0 * ((na+nb+1) - t/(double)((na+nb)*(na+nb-1)));  // :859
```

`t` is `int64_t`, but `(p*p-1)*p` is evaluated in `int`: it exceeds `INT32_MAX`
(2,147,483,647) once `p ≥ 1291` (1291³ = 2,151,685,171) and wraps. With BWA-style data
every reference read has MAPQ 60, so bin 59 of the MAPQ histogram holds the whole
reference depth of the site summed over samples; with NovaSeq-style binned base
qualities the same happens to the base-quality histogram. The wrapped tie term inflates
`var2` (or makes it ≤ 0, in which case the function returns 0, `bam2bcf.c:861-862`),
so the Z-scores shrink towards zero. `na*nb`, `e` and `l` (`:855-859`) are also `int`
products and overflow at about 46,000 reads per side; the same patch covers them.

**Verified** (`../verify/bc1_mpileup_mwu_biasZ_int_overflow.py` and `.out`; truth is
the tie-corrected normal approximation of the Mann-Whitney U on the same binned
values, `scipy.stats.mannwhitneyu(method="asymptotic", use_continuity=False)`, which
is what the function implements; an int32-wrap replica of the C loop is printed
alongside and reproduces bcftools' value in every affected case):

| case (single sample unless stated) | bin count | truth | `develop` |
|---|---|---|---|
| A: 30 ref + 12 alt reads, mixed MAPQ/BQ/positions/strands — model check | ≤ 20 | MQBZ −2.6164, BQBZ −3.5573, RPBZ −0.3760, MQSBZ −0.3198 | same four numbers |
| B: `-d 100000`, n ref reads at MAPQ 60 + 40 alt at MAPQ 30, n = 1290 | 1,290 | −36.4555 | −36.4555 |
| B, n = 1291 | 1,291 | −36.4692 | **−7.8056** |
| B, n = 1300 / 1500 / 2000 / 3000 | | −36.59 / −39.23 / −45.16 / −55.13 | **−7.88 / −9.66 / −10.49 / −11.13** |
| B, n = 5000 / 12000 | | −70.99 / −109.72 | **−10.93 / −10.94** |
| C: binned base qualities, 1,500 ref bases Q37 + alt 30×Q37, 10×Q12 (BQBZ) | 1,530 | −19.4218 | **−2.4713** |
| C, 3,000 ref | 3,030 | −27.4268 | **−2.8250** |
| D: **default `-d 250`**, one BAM per sample, 30 MAPQ-60 ref reads each, 3 samples with 10 MAPQ-30 alt reads; 40 samples | 1,200 | −35.0571 | −35.0571 |
| D, 44 samples | 1,320 | −36.7287 | **−6.9685** |
| D, 48 / 60 / 100 samples | 1,440 / 1,800 / 3,000 | −38.33 / −42.77 / −55.04 | **−7.90 / −10.87 / −9.65** |
| E: as D with 48 samples, BAQ on (the plain default command line) | 1,440 | −38.3275 | **−7.8989** |

`../upstream/mcve_mpileup_mqbz_overflow.sh` reproduces it from a 1,340-read SAM
written by `awk`: 1,300 MAPQ-60 reference reads and 40 MAPQ-30 alternate reads give
`MQBZ=-7.88325` where the closed form gives −36.5923; with 1,290 reference reads the
output is −36.4555 = truth (`../upstream/mcve_outputs.txt`, identical on `develop`,
1.24 and 1.13).

**Version scope (executed).** Identical wrong numbers on `develop`, 1.24 and 1.13
(`.out`, `.v1.24.out`, `.v1.13.out`: 17 affected cases each). 1.10.2 and 1.9 do not
have the Z-score annotations (`.v1.10.2.out`, `.v1.9.out`: `absent` in all 31 cases);
their `MQB`/`BQB`/`RPB` are the older `calc_mwu_bias()` p-value-like scores computed
in `double`. `calc_mwu_biasZ` is absent from the 1.11 and 1.12 sources too (checked on
the tags' `bam2bcf.c`; not built), so the affected range is 1.13 through the current
`develop`. With the patch below every case equals the truth (`.patched.out`: 0
affected, 31 ok).

**Who is exposed.** Anyone filtering or reporting on `MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`,
`MQSBZ` or `NMBZ` (the annotations bcftools' own filtering how-to recommends) at sites
where a single MAPQ or base-quality bin holds ≥ 1,291 reads: a single deep site when
`-d` is raised (amplicon, mitochondrial, viral, pooled and metagenomic data — 41 cohort
papers name such data), or, **under the default `-d 250`**, any multi-sample call whose
summed reference depth in MAPQ 60 reaches 1,291 (about 45 samples at 30×; 26 cohort
papers state a cohort size, 11 of them 1,000 samples). The effect is one-directional:
a real mapping- or base-quality bias is reported as several times weaker than it is,
so a `MQBZ < -3`-style filter that should remove an artefact keeps it; at very high
counts the score saturates around −11 regardless of the true value. `PL`, `AD`, `DP`,
`QUAL` and genotypes are not affected.

**Fix shape.** Accumulate in `int64_t` (`../upstream/0001-*.patch`, 11 lines changed
in `calc_mwu_biasZ`, a regression test with a 4.9-kB BAM of 1,340 20-bp reads, and a
NEWS entry).

**Upstream.** No prior report: searched 2026-09-13 for the Z-score annotations with
high depth, multi-sample runs, integer overflow and tie correction (four
`search_issues` phrasings); nearest #2003 (closed, 2023, "Is this the kind of
distribution expected for the BQBZ metrics?", 0 comments), #897 (open, 2018, MQB and
`-C`), #1058 (open, overlap detection and strand bias), #2185 (open, confidence at
low support).

### N1 — NOTE, verified, documentation: `merge` takes an unruled Number=A/R/G INFO tag from the *last* file that carries the allele, while the manual says "the first input file"

`doc/bcftools.txt:2146` ("Fields with no specified rule will take the value from the
first input file") holds for Number=1 tags but not for Number=A/R/G vectors, which go
through the `AGR_info` path (`vcfmerge.c:1423-1440` and following; the value for each
output allele is overwritten by every later file carrying that allele).
`../verify/heldup_merge.py`: with `AF=0.25` in file 1 and `AF=1` in file 2 the merged
`AF` is `1`; swapping the files gives `0.25`; a Number=1 float `XX` and a string `XS`
come from the first file in both orders. `AF` after `merge` is stale in either reading
(the manual's remedy is `+fill-tags`); this is a documentation discrepancy, not a wrong
count — `AN`, `AC` and `DP` are summed correctly (below).

### N2 — NOTE, verified, cosmetic binning: `stats` labels its default AF bins on a 100-step grid but bins on a 99-step grid

`init_iaf` puts an allele into bin `iaf = af*(m_af-2)` (`vcfstats.c:665`, `:696`;
`m_af` = 101 by default, `:449`), i.e. bins of width 1/99, and `print_stats` labels
bin `i` as `(i-1)/(m_af-1)` = `iaf/100` (`:1486`, also `:1635`, `:1837`). So the
`AF` rows (and `GCsAF`, `HWE`) carry labels that are the true AF truncated to the next
lower hundredth of a 99-grid: AF 0.25 prints as `0.240000`, 0.5 as `0.490000`, 1.0 as
`0.990000` (`../verify/heldup_stats.py`: nine AF rows, counts all correct, labels as
stated). The `-2` keeps AF = 1 inside the array; the label formula was not adjusted.
`--af-bins` labels are bin midpoints and are consistent.

### N3 — NOTE, verified, acknowledged in the source: `+fill-tags` HWE/ExcHet at multiallelic sites use allele counts that double-count the other ALT

`fill-tags.c:952-958` computes, for ALT *j*, `nref = nhom[0] + Σ_k nhet[k] − nhet[j]`,
which adds one reference allele for every heterozygous genotype involving *any* other
ALT (the comment at `:953` says "NB this neglects multiallelic genotypes"). On a site
with 0/0 ×100, 0/1 ×40, 0/2 ×30, 1/2 ×20, 1/1 ×10, 2/2 ×5 bcftools uses
`nref = 320` for ALT1 (pooling allele 2 with REF gives 2·135 + 60 = 330) and reports
`HWE = 0.377683, 0.784561`, `ExcHet = 0.872677, 0.711343` where the pooled exact values are
0.371175, 0.778104 and 0.890200, 0.753635 (`../verify/heldup_filltags_hwe_af.py`).
Biallelic sites are exact (held up below). Small, and there is no single right
definition of a biallelic HWE test at a multiallelic site; recorded because
`AC`/`AN`/`AF` at the same site are right and users may not expect `HWE` to differ.

### N4 — NOTE, verified, documentation (HTSlib): `mpileup -d` is not a per-position depth cap

`bam_plp_push` drops a read only when it *starts* at the current position while the
buffer already holds more than `maxcnt` reads (HTSlib `sam.c:6139`), so the depth at a
position can exceed `-d`. With 400 reads of random start covering one site,
`INFO/DP` is 170 under `-d 100` and 288 under the default `-d 250`
(`../verify/heldup_mpileup_counts.py`). The option's help text calls it "Max raw
per-file depth; avoids excessive memory usage", which is what it is; papers that
report "depth capped at 250" are reporting an approximate cap. Relevant to BC1: the
default cap does not stop bins from reaching 1,291 in multi-sample runs.

### N5 — NOTE, design, verified: `call -m` reports `./.` for a sample whose PLs are all 0

`set_pdg` (`mcall.c:532-540`, `FLAT_PDG_FOR_MISSING 0`) treats a flat PL vector
(`0,0,0`, what mpileup writes for a sample with no usable reads) as missing data, so
the genotype is `./.` and GQ is 0 rather than `0/0` with a low GQ. This is the
sensible choice and the port in `../verify/heldup_call_m_port.py` matches it once the
rule is included; noted because a flat PL from any other source is also silently
treated as missing.

### N6 — NOTE, verified, documentation: `stats` PSC `nSingletons` and `nTs`/`nTv` definitions

`PSC nSingletons` counts the sites where the sample carries the only non-reference
genotype, whatever it is (`vcfstats.c:1023`, `:1159`): a `1/1` (AC = 2) and an MNP
or indel genotype count, so the column is not the `SiS` "AC = 1" definition. Haploid
genotypes return before the transition/transversion tally (`:1012-1021`), so
`nHapAlt` sites do not appear in `nTs`/`nTv`. The PSC header (`:1789`) says only
that the ref/het/hom counts are SNP-only. Both verified on the four-sample VCF in
`../verify/heldup_stats.py`.

## Withdrawn suspicions (verification killed them)

- **`calc_hwe` recurrence and midpoint rounding** (`fill-tags.c:664-727`; `mid` is
  truncated and parity-fixed, the probabilities come from a two-sided recurrence in
  `double`): on 24 biallelic sites of 2,000 samples, including AA/AB/BB = 0/4/0,
  1990/10/0, 0/0/2000 and 1200/2/798, `HWE` and `ExcHet` agree with exact rational
  arithmetic to within 2 × 10⁻⁶ (float printing), including the "sum of probabilities
  ≤ p(obs)" tail definition of Wigginton et al. 2005.
- **`FORMAT/SP` rounding** `(int)(-4.343*log(p)+.499)` with the margin-≥ 2 guard
  (`bam2bcf.c:1361-1369`): equals the phred of `scipy.stats.fisher_exact` two-sided
  p on `DP4` in all four filter settings.
- **`I16` sums after the 255 → 20 and 60 caps on MAPQ** (`bam2bcf.c:452`, `:460`) and
  the `min_dist` cap at 25 (`:481-483`): all 16 sums equal the Python truth.

## Design choices seen and left alone

- `MQ0`-mapped reads enter the PL with base quality 4 (`bam2bcf.c:463`, "MQ=0 reads
  count as BQ=4"): 1 reference read at MAPQ 0 gives `PL=0,3,4`.
- The dependent-error model (`errmod_cal`, theta 0.83): 5 reference reads at Q30 give
  `PL(1/1)=129`, not 150; single reads give `0,3,q`.
- `INFO/MQ` after `call` is the arithmetic mean of the capped MAPQ over the DP4 reads
  (`mcall.c:1663`), not the RMS that GATK reports; 1.24 declared it `Integer` and
  truncates (38.57 → 38, 51.54 → 51), `develop` declares it `Float` (NEWS, unreleased).
- `MQSBZ` is a Mann-Whitney test of MAPQ between strands over *all* reads
  (`bam2bcf.c:1180`), so with uniform MAPQ it is 0 whatever the allele strand split;
  strand bias of the alternate allele is `FORMAT/SP` and `INFO/FS`.
- `norm -m -` fills the other ALT of a `1/2` genotype with REF by default
  (`--multi-overlaps 0`, `vcfnorm.c:2600`); `-m +` cannot recover `PL(1/2)` and writes
  `.` there.
- `stats` PSC average depth is over sites with `DP > 0` (`vcfstats.c:1119-1124`).
- The `call -m` prior `-P` is multiplied by the Watterson factor
  `1 + Σ_{i=2}^{n-1} 1/i` for n = total ploidy (`mcall.c:400-418`) — a design the
  port needed to reproduce QUAL.

## What held up (executed, not just read)

All on `develop`, and again on the 1.24 release build (`*.v1.24.out`; the only
differences there are the two documentation notes N1 and the `Integer` `MQ`).

- **`mpileup` counting** (`heldup_mpileup_counts.py`): on a 62-read site mixing
  ref/alt/third bases, base qualities 0–41, MAPQ 0/10/20/40/60/255, both strands, a
  spanning deletion and a spanning ref-skip — `INFO/DP` (raw, before `-Q`), `FORMAT/DP`,
  `DP4`, `AD`, `ADF`, `ADR`, `INFO/AD`, `SP`, all 16 `I16` sums, `MQ0F` and `call`'s
  `MQ`, under default, `-Q 13`, `-q 20` and `-Q 20 -q 30`: 44 checks, 0 mismatches.
  A clean 3-bp heterozygous deletion at 40× is called `0/1` with `AD=20,20`,
  `IDV=20`, `IMF=0.5`, `QUAL=222.3` through `mpileup | call -mv` with BAQ on.
- **`+fill-tags`** (`heldup_filltags_hwe_af.py`): `AN`, `AC`, `NS`, `AC_Het`,
  `AC_Hom`, `AC_Hemi`, `F_MISSING`, `AF`, `MAF`, `HWE`, `ExcHet` on 24 biallelic
  2,000-sample sites and one site mixing haploid, phased, half-missing (`./1`, counted
  as hemizygous and as missing by the documented conventions) and missing genotypes:
  0 mismatches.
- **`call -m`** (`heldup_call_m_port.py`): a Python port of the multiallelic caller
  (PL → probabilities, QS as allele-frequency weights, best allele set over 1–3 alleles
  with the Watterson-scaled prior, QUAL, per-sample GT/GQ, AC/AN) matches `call -m`,
  `-mv`, `-P 0.1`, `-P 1e-6` and `-mv --ploidy 1` on 12 six-sample sites (depths 0–30,
  ref/het/hom/third-allele genotypes): QUAL to 10⁻³ relative, GT, GQ, AC, AN, ALT
  identical, ref-only QUAL identical, `-v` dropping exactly the ref-only and all-hom-ref
  sites.
- **`stats`** (`heldup_stats.py`): on a 15-site, 4-sample VCF with SNPs, a
  multiallelic SNP, two indels, an MNP, a no-ALT site, missing and haploid genotypes —
  the eight `SN` counts, `TSTV` (all ALTs and first ALT), `SiS`, the counts in every
  `AF` row, the `DP` distribution (genotypes and sites), and the eleven `PSC` columns
  for all four samples: 0 mismatches.
- **`norm`** (`heldup_norm.py`): nine realignment cases in CAG, A₆ and AT repeats
  (deletions, insertions, a multiallelic del+ins, a 4-bp REF/ALT reducing to a SNP)
  equal a Python left-aligner; `-m -` on a multiallelic site with `AC`, `AF` (A),
  `AN`, `DP`, `GT`, `PL` (G), `AD` (R), `GQ` for five samples gives the correct
  Number=A/R/G elements; `-m +` restores ALT, AC, AF, GT and AD.
- **`view -i` / `filter -i`** (`heldup_filter_expressions.py`): 42 expressions on a
  7-site, 3-sample VCF — missing QUAL/INFO/FORMAT values, `&` vs `&&`, `|` vs `||`,
  `MIN`/`MAX`/`AVG`/`MEDIAN`/`SUM`, `sMAX`/`sSUM`, subscripts, the `GT` string tests,
  `TYPE`, `FILTER`, `N_PASS`/`F_PASS`, on-the-fly `AC`/`AN`/`MAF`/`F_MISSING`/`N_ALT`,
  `-e` as the complement of `-i`, `filter -s` — 0 mismatches against the manual's
  semantics.
- **`merge`** (`heldup_merge.py`): `DP:sum`, `AN:sum`, `AC:sum` per merged allele,
  QUAL = max, missing samples' `GT`/`PL`/`DP`/`AD`, and the Number=G/R expansion when
  the files carry different ALTs (`90,10,0` → `90,10,0,.,.,.`; `22,0,33` →
  `22,.,.,0,.,33`): 0 mismatches apart from the N1 documentation point.

## Not audited

The indel model beyond the smoke test (`bam2bcf_indel.c`, `bam2bcf_iaux.c`,
`bam2bcf_edlib.c`, `--indels-2.0`/`--indels-cns`), BAQ's arithmetic (HTSlib
`realn.c`), `call -c` (`ccall.c`, `prob1.c`, `em.c`), `roh`, `gtcheck`, `csq`,
`consensus`, `annotate`, `+trio-dnm2/3`, the `VDB`/`SGB` heuristics
(`bam2bcf.c:600-661`, `:895-931`; parameters fitted to simulations, no closed truth),
`--gvcf`, CRAM input, and the `stats` GC/indel-context/HWE-percentile sections.
