# VCFtools upstream filing kit

_Default branch: **`master`** (PRs go against it). Prepared 2026-09-24 against `vcftools/vcftools`
`master` @ `1f87a83` (0.1.18 unreleased). **Nothing filed, nothing pushed.** The two fixes are single
commits on local branches of the audit clone, `git am`-able from the patches in this directory against
`1f87a83`; they need a fork of `vcftools/vcftools` under `cindykrafft` to be pushed._

Filing tier (README step 5): **now** for VT1 and VT2 — VT1 makes thirteen output modes unusable
from a source build on a current distribution, with a mechanical 19-line fix; VT2 changes a number
(kinship) that reaches sample-relationship decisions on every release, with a fix that leaves
complete-data results unchanged. Neither has a prior report. **VT3 ready** as the third filing (a
documentation discrepancy known to a reporter since 2016, #28, never fixed) once VT1 or VT2 has a
reply, under the two-unanswered-filings cap (issue + PR pairs count as one). VT4, VT5 and the #189
comment are **held**.

Expectation management: the tracker shows no maintainer reply in any of the twelve threads read
(2016–2024) and four open PRs from 2016–2026; the last commit is from 2025-05-14. The filings are
still worthwhile (the tracker is where users of the tool look, #28 and #189 show them searching for
exactly these behaviours), but a response may take a long time or not come.

## What was read before preparing this (step 4 of the method)

- Repository root: no `CONTRIBUTING`, no `.github/`, no issue or PR template, no code of conduct, no
  AI policy. `README.md`'s "Getting Help": "The best way to get help regarding VCFtools is to use the
  GitHub Issues page." Build: `./autogen.sh && ./configure && make`. No test suite (`examples/` holds
  sample inputs and expected outputs for the Perl tools; there is no `make check` target).
- `src/cpp/vcftools.1` (the man page, also rendered at vcftools.github.io/man_latest.html) as the
  statement of intended behaviour; Manichaikul et al. 2010 for `--relatedness2`.
- Issue tracker searched 2026-09-24 (seven `search_issues` phrasings) and twelve threads read in full
  through a helper session (artifact "Mytochondria threads vcftools 28 190 163 189 180 50 210 194 137
  216 182 203"): **no prior report of VT1 or VT2.** #28 (2016, closed by its reporter) is VT3: the
  reporter worked out for themself that `--max-missing-count` "refers to the number of missing
  alleles and not the number of missing genotypes"; nobody replied and the manual still says
  genotypes. #163 (open, 2 comments) is a different `--missing-site` question (a site with `.`
  single-dot missing genotypes gets `N_DATA + N_MISS` twice the individual count — the haploid
  code path). #189 (open, 1 comment) is N1: the `.012.pos` file has fewer sites than the log says
  were kept; the one commenter guesses multi-allelic sites, which is right. #180 (open, no comments)
  reports `--relatedness` / `--relatedness2` writing no values on a GATK VCF — a different problem
  (the log shows both one-off warnings, so sites were read; the output was presumably empty for a
  ploidy reason), not VT2. #50 (open, 9 comments, no maintainer) says `--minDP` / `--minGQ` "does
  not work": checked here, `--minDP 10 --recode` does write the filtered genotypes as `./.` on
  `master` and v0.1.16. #210 (`--het` counting one site for one individual) is explained by the
  held-up behaviour: `--het` uses sites polymorphic among the kept individuals. #194, #203 (Tajima's
  D questions), #216 (`-nan` r² at monomorphic sites), #182 (output directory not writable), #137
  (zlib link error) are unrelated.
- Open PRs: #228 (2026, windowed Tajima's D), #159 (2020, 32-bit large files), #123 (2018, vcf-merge),
  #43 (2016, BED header) — none touches the temporary-file writers or `--relatedness2`.
- `site/audits.json` records no fork of `vcftools/vcftools` under `cindykrafft`.

## Contents

| file | what |
|---|---|
| `issue-vt1-tmpname-buffer-overflow.md` | bug report: build on Ubuntu 24.04, `--012` / `--hap-r2` abort, the code, the fix |
| `issue-vt2-relatedness2-missing-genotypes.md` | bug report: 40-individual VCF with duplicates and parent–offspring pairs, 20 % missing, the numbers, the formula, the fix |
| `issue-vt3-max-missing-count-alleles-vs-genotypes.md` | ready: documentation discrepancy (#28), the 392-vs-572 reproduction, man-page patch offered |
| `0001-Size-the-temporary-file-name-buffers-for-the-termina.patch` | VT1 fix (`fix/tmpname-buffer-size`, 19 sites in `variant_file_format_convert.cpp` and `variant_file_output.cpp`) |
| `0002-relatedness2-count-each-individual-s-heterozygous-si.patch` | VT2 fix (`fix/relatedness2-missing-genotypes`, `output_indv_relatedness_Manichaikul`); independent of 0001, both apply to `1f87a83` |
| `pr-bodies.md` | PR titles and bodies |
| `comment-n1-189-012-biallelic.md` | held: answer for #189 |
| `test-runs.txt` | what was run on the two branches (no upstream test suite) |

## Verification status of the patches

`fix/tmpname-buffer-size` (`9bb4040`): every temporary-file mode runs on the fortified build
(`../verify/v1_diversity_het_hwe.patched.out` 13/13 incl. `--012` dosages on 40/40 individuals;
`v2_fst_ld_relatedness.patched.out` `--hap-r2` and `--geno-r2` 7090/7090 pairs equal to the r² / D / D'
port; `--plink`, `--plink-tped`, `--geno-chisq`, `--interchrom-*`, `--ldhat`, `--ldhat-geno`,
`--ldhelmet`, `--IMPUTE` exit 0 on a six-sample VCF). Everything else identical to `master`.

`fix/relatedness2-missing-genotypes` (`798544e`): `v2_fst_ld_relatedness.patched2.out` — with 20 % of
genotypes missing, duplicates 0.5000 / 0.5000, parent–offspring 0.2373 / 0.2565, unrelated −0.0070,
equal to the KING-robust port over the shared sites; complete-data output unchanged to all printed
digits; every other harness line identical to `master` (the LD lines still abort there, that branch
not carrying 0001).

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| VT1 | `master`, v0.1.16, v0.1.13 as built with GCC 13 / glibc 2.39 defaults; the overflow is in every version | Ubuntu 24.04 package 0.1.16-3 (`_FORTIFY_SOURCE=2`, no abort), `fix/tmpname-buffer-size` |
| VT2 | `master`, v0.1.16, v0.1.13, Ubuntu 0.1.16-3 | `fix/relatedness2-missing-genotypes` |
| VT3 | all four | — |

## Order of operations

1. Fork `vcftools/vcftools`; tell the session; the two branches are pushed.
2. Open the VT1 issue from `issue-vt1-tmpname-buffer-overflow.md`, then the PR from
   `fix/tmpname-buffer-size` with the body from `pr-bodies.md` § PR 1 (issue number in the first line).
   Same for VT2 (`fix/relatedness2-missing-genotypes`, § PR 2).
3. When one of them has a maintainer reply, VT3 (issue; the man-page change is in the issue text) and,
   if wanted, the #189 comment.
4. Record issue and PR numbers and every response in `../README.md` and the top-level status table.
