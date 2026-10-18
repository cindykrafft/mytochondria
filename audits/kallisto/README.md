# kallisto audit against 125 published papers (2021–2026)

_Generated 2026-10-18 against `pachterlab/kallisto` `master` @ `4e9f29c` (= the v0.52.0 tag, the current
release; `devel` @ `34aba49` differs by one usage-text commit). Built here with the default CMake options
(no HDF5) and with `-DUSE_HDF5=ON`. Also v0.51.1 (`0397342`) and v0.50.1 (`34e5814`) built from their
tags, plus the GitHub release binaries 0.46.1, 0.48.0, 0.50.1, 0.51.1 and 0.52.0 (the cohort's most-cited
versions are 0.46.x and 0.44.0/0.48.0). Focus: what a paper takes from a `kallisto quant` run, meaning
est_counts and TPM, the effective length (fragment-length distribution, `--single -l/-s`, short targets),
the EM and its stopping rule, `--bias`, bootstraps, pseudoalignment and the strand options, and
run_info.json. All of it was verified by executing the binaries on simulated transcriptomes and reads
whose abundances, fragment lengths and compatibility classes are known._

## What this is

The six-journal survey found **125 papers** (PNAS 62, *Nature* 48, *Cell* 10, *Science* 5; 2021–2026)
that used kallisto, mostly for bulk RNA-seq quantification, as TPM tables or as counts for
sleuth/DESeq2/edgeR. The quantification code (`EMAlgorithm.h`, `weights.cpp`, `MinCollector.cpp`,
`ProcessReads.cpp`, `KmerIndex.cpp`, `Bootstrap.cpp`, `PlaintextWriter.cpp`, `H5Writer.cpp`, `main.cpp`) was
read on `master`, and every suspicion was run on up to ten builds with harnesses whose truths are computed
independently in Python:

- reads simulated under kallisto's own likelihood with known abundances and a known FLD;
- a port of the documented effective-length formula `L − mu_L + 1` and of the TPM formula;
- exact compatibility classes (targets containing every read of a fragment);
- an independent EM on those classes run to 1e-13.

## Findings (details and line citations in [`component-reviews/quant-em-efflen-bootstrap.md`](component-reviews/quant-em-efflen-bootstrap.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **KA1** | **CONFIRMED on `master`/0.52.0, v0.51.1 and v0.50.1 built with the default CMake options, and on the 0.48.0 release binary**; HDF5 builds (0.46.1 binary, 0.50+ release binaries, `-DUSE_HDF5=ON`) unaffected | **now** (lead's call: a silent omission, not a wrong number, cf. VCFtools VT1) | `quant -b N --plaintext -t T` with `T > 1` runs **no bootstraps** in a build without HDF5. The bootstrap thread pool is compiled only `#ifdef USE_HDF5` (`main.cpp:2942-2945`), and `--plaintext` is exactly what `CheckOptionsEM` tells non-HDF5 users to pass for bootstraps. No `bs_abundance_*.tsv`, no message, exit 0, and `run_info.json` still says `n_bootstraps: N` (0 of 8 tables with `-t 2`/`-t 4`, 8 of 8 with `-t 1`). Affected: the CMake default (`USE_HDF5=OFF`, INSTALL.md's `cmake ..`), the 0.48.0 release binary, and by its `debian/rules` the Debian/Ubuntu package. Bioconda and Homebrew build with HDF5. Two-line fix with a functional test; tables identical to `-t 1`. |
| KA2 | **CONFIRMED on all eight builds** | held (documented default; design; prior #230 open, unanswered) | Single-end default (no `--single-overhang`): a read is dropped from every target where start + `-l` would overhang (`ProcessReads.cpp:1162-1207`), while the effective length `L − mu_L + 1` assumes those fragments were counted. Every target ≤ `-l` gets est_counts 0 (TPM 0), targets up to ~`-l + 2·sd` are shrunk, and the rest absorb the mass. `-l 200 -s 20`: 150/180/200-bp targets 0/0/9 reads for 56/105/126 simulated, 220 bp 173 for 225; with `--single-overhang` all exact. Forward-side off-by-one: the last valid start is also dropped. Comment on #230 drafted. |
| KA3 | **CONFIRMED** (0.46.1, 0.48.0, 0.52.0; `--bias` crashes on 0.50/0.51, see KA5) | duplicate (#151, PR #260; `--bias` unsupported per #465) | With `--bias`, bootstrap EMs use the plain effective lengths (`Bootstrap.cpp:4-13`) while the point estimate uses bias-corrected ones and the tables are labelled with them. 9 of 108 targets have bootstrap means > 4 SE off the point estimate (up to +18 %), against 1–2 without `--bias`. |
| KA4 | **CONFIRMED** (0.46.1, 0.48.0, 0.52.0) | held (`--bias` unsupported, #465) | `update_eff_lens` sums `L − mu − 6` forward and `L − mu` reverse start positions and halves them (`weights.cpp:141-199`), so on an unbiased library the bias-corrected effective length is −4.15 ± 0.62 bp off `L − mu + 1`. |
| KA5 | **CONFIRMED on v0.50.1, v0.51.1** (tag builds and release binaries); 0.46.1, 0.48.0, 0.52.0 complete | already reported (#465), fixed in 0.52.0 (`d0ac69b`) | `quant --bias` segfaults (exit −11, no output) after "[em] quantifying the abundances". |
| N1 | note, verified | held | Paired-end: targets shorter than the shortest of the ≤ 10,000 sampled fragments get `eff_length = L + 1` (40 bp → 41; true 7.6) while slightly longer ones can get ~1 (100 bp → 4.5; true 10.1). Unstable TPMs for very short targets. |
| N2 | note, verified | held | EM stopping rule (1 % relative change for targets with α > 0.01, ≥ 50 rounds, as in the paper): 0.02–0.07 % of reads differ from a fully converged EM. The largest per-target gap is in a slowly converging isoform family, within sampling error. |
| N3 | note, verified | held | FLD estimated from pairs on one unitig/EC block and one target, fragments < 1000 bp: within ±0.6 bp on single-isoform transcriptomes, 1–5 bp low on isoform-rich ones; TPM effect ≤ 0.5 % for targets ≥ 500 bp. |

**Held up under execution:**

- **TPM.** The formula matches in every abundance.tsv, bootstrap table and abundance.h5 (all builds).
- **Single-end effective length.** It equals the truncated-Gaussian port for 40–3,000-bp targets under five
  `-l/-s` settings, including the cohort's `-l 55 -s 1e-08` and `-l 50 -s 20`, and across the
  `MAX_FRAG_LEN` boundary.
- **Paired-end effective length.** It matches kallisto's own FLD.
- **Pseudoalignment.** Per-read ECs (via `bus --num`) equal the exact compatibility classes for all 119,987
  error-free fragments.
- **Strand options.** `--fr-stranded`/`--rf-stranded`, paired and single-end, under both protocols with
  antisense overlaps, give exactly the stranded classes in 12 of 12 configurations.
- **run_info.json.** `n_processed`, `n_pseudoaligned`, `n_unique` and `p_pseudoaligned` are correct with
  substitution errors and random pairs.
- **Determinism and HDF5.** `-t 1` and `-t 4` give identical results; HDF5 `est_counts`/`eff_lengths` equal
  the TSV.
- **Bootstraps without `--bias`.** They centre on the point estimate.

Not checked: indels and real error profiles, `--genomebam`/`--pseudobam`, gene-level output, `quant-tcc`
numerics, single-cell `bus`/bustools, long reads, `--priors`, d-list indexes, other k, real data, and the
Debian binary itself (KA1's Debian exposure is read from its `debian/rules`).

## How the papers use kallisto (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 46 (0.46.1 ×11, 0.46.0 ×7, 0.44.0 ×6, 0.46.2 ×6, 0.48.0 ×4, 0.50.1 ×3, 0.43.x ×3, 0.42.5 ×2, 0.45.x ×2, "0.46" ×2) |
| TPM reported | 11 |
| bootstraps (`-b 100`, 30, 60) | 5 (one regex hit is cutadapt's `-b`) |
| sleuth downstream | 5 |
| single-end `-l/-s` | 3 (`-l 200 -s 20`, `-l 50 -s 20`, `-l 55 -s 1e-08`); `--single-overhang` 1 |
| `--bias` | 1 (0.43.1, with `--rf-stranded`) |
| stranded option | 2 |
| threads stated | 1 ("100 bootstrapped samples and 6 threads", 0.46.2, an HDF5 build, so unaffected by KA1) |

Which finding reaches which paper:

- **KA1** reaches runs that request bootstraps with several threads on a non-HDF5 build. That means 0.48.0
  from the release tarball (4 cohort papers on 0.48.0), source builds of 0.48+ with default options, and
  Debian/Ubuntu packages. Those runs have no bootstrap tables while their metadata says they do, so any
  bootstrap-based variance or interval (sleuth-style technical variance, CIs) is either missing or quietly
  computed from nothing.
- **KA2** reaches every single-end run without `--single-overhang`: short transcripts (≤ `-l`) are reported
  at 0 TPM and slightly longer ones are biased low.
- **KA3/KA4** reach `--bias` runs on 0.48 and earlier, a path the maintainers no longer support.

The profile (`kallisto_profile.py`, `profile_run.log`) was run offline against the survey's stored
evidence sentences, so every count is a lower bound over a few hundred characters per paper.

## Filing channel

`pachterlab/kallisto` has no `CONTRIBUTING.md`, no issue or PR template and no AI policy in the tree.
`.github/` holds only `workflows/test.yml`, a manually dispatched build + `make test` (the
`func_tests/runtests.sh` functional tests, which need bustools). README: "Please report bugs to the Github
issues page". On pull requests, "please make sure to request to merge into `devel` and NOT `master`".
Questions go to the kallisto-and-applications Google Group. Kit under [`upstream/`](upstream/): the KA1
issue text and PR body with a `git am`-able patch (applies cleanly to `devel` @ `34aba49` and `master` @
`4e9f29c`), the test runs, the duplicate check, and a held comment draft for #230 (KA2). No fork of
`pachterlab/kallisto` exists under `cindykrafft` yet.

## Files

| path | what |
|---|---|
| `component-reviews/quant-em-efflen-bootstrap.md` | the review: KA1–KA5, N1–N3 with code citations, held-up list, withdrawn items |
| `verify/_sim.py` | transcriptome and read simulator (kallisto's likelihood), FLD and effective-length ports, exact compatibility classes, independent EM, TPM |
| `verify/t1_tpm_efflen.py` | TPM formula; single-end effective length vs the truncated-Gaussian port; paired-end FLD and implied truncated means (N1) |
| `verify/t2_ec_em.py` | per-read ECs (`bus --num`) vs exact classes; independent EM vs est_counts (N2); run_info |
| `verify/t3_single_overhang.py` | single-end overhang filter vs truth with and without `--single-overhang`; position scan (KA2) |
| `verify/t4_strand.py` | `--fr-stranded`/`--rf-stranded` vs exact stranded classes |
| `verify/t5_fld_estimate.py` | FLD estimate on single-isoform and isoform-rich transcriptomes (N3) |
| `verify/t6_bias_bootstrap.py` | bootstrap centring with and without `--bias` (KA3); `--bias` effective-length offset (KA4) |
| `verify/t7_threads_bootstrap.py` | bootstraps vs `-t` (KA1); `-t` determinism; run_info with errors and random pairs |
| `verify/t8_bias_runs.py` | `--bias` completion per build (KA5) |
| `verify/t9_h5.py` | abundance.h5 vs abundance.tsv, bootstraps in HDF5 with `-t 1`/`-t 4` |
| `verify/run_all.sh` | runs a harness on every build |
| `verify/*.out`, `*.<tag>.out`, `*.patched*.out`, `*-hdf5.out` | captured output per build |
| `kallisto_profile.py`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit |

## Next steps

1. Fork `pachterlab/kallisto`; push `fix/bootstrap-threads-without-hdf5` (based on `devel` @ `34aba49`);
   file KA1 (issue, then PR against `devel`).
2. KA2 as a comment on the open #230 (a comment on an open issue, not counted against the cap), only if
   the lead agrees and only after #230 is re-read in full. The maintainers have not answered there since 2019.
3. KA3, KA5: duplicates, nothing to file. KA4: held (`--bias` unsupported). N1–N3 held.
