# kallisto: quant, effective length, EM, bootstraps, strand options and run_info

_Read on `pachterlab/kallisto` `master` @ `4e9f29c` (2026-01-20, the v0.52.0 tag; `devel` @ `34aba49`
is the same minus one usage-text commit). Executed on that commit built with the default CMake options
(no HDF5) and with `-DUSE_HDF5=ON`; on v0.51.1 (`0397342`) and v0.50.1 (`34e5814`) built from their
tags; and on the GitHub release binaries 0.46.1, 0.48.0, 0.50.1, 0.51.1 and 0.52.0. Every number below
comes from a harness in `../verify/`. Its captured output sits next to it: `.out` for the master build,
`.<tag>.out` for the others, `.patched.out` for the fix, and `-hdf5` for the HDF5 builds. Line numbers refer to
`4e9f29c`._

Files read: `EMAlgorithm.h` (EM, stopping rule, zeroing, `compute_rho`), `weights.cpp/.h` (`calc_eff_lens`,
`get_frag_len_means`, `update_eff_lens`, `calc_weights`, `trunc_gaussian_fld`), `MinCollector.cpp/.h`
(`compute_mean_frag_lens_trunc`, `init_mean_fl_trunc`, `get_mean_frag_len`, `countBias`, `intersectKmers`,
`intersectECs`), `ProcessReads.cpp` (the per-read loop: pseudoalignment, the single-end overhang filter,
`doStrandSpecificity`, fragment-length and bias collection, `MasterProcessor::update`/`processReads`),
`KmerIndex.cpp` (`mapPair`, `findPositions`, `mapTranscriptPosition`, `loadTranscriptSequences`),
`Bootstrap.cpp/.h`, `PlaintextWriter.cpp` (`counts_to_tpm`, `plaintext_writer`, `plaintext_aux`),
`H5Writer.cpp`, and `main.cpp` (`ParseOptionsEM`, `CheckOptionsEM`, the `quant` and `quant-tcc` branches).

## Findings

### KA1: with `-t > 1`, a build without HDF5 runs no bootstraps (silently)

`main.cpp:2933-2946`, the `quant` branch:

```cpp
if (opt.threads > 1) {
  auto n_threads = opt.threads;
  if (opt.threads > opt.bootstrap) { ... n_threads = opt.bootstrap; }
#ifdef USE_HDF5
  BootstrapThreadPool pool(opt.threads, seeds, collection.counts, index, collection,
                           em.eff_lens_, opt, &writer, fl_means);
#endif
} else {
  for (auto b = 0; b < B; ++b) { ... plaintext_writer(... "/bs_abundance_" ...) ... }
}
```

`USE_HDF5` is `OFF` by default (`CMakeLists.txt`, `option(USE_HDF5 ... OFF)`). Without it,
`CheckOptionsEM` (`main.cpp:1876-1882`) keeps `-b` only when `--plaintext` is given, and tells the user to
run with `--plaintext`. With `--plaintext` and more than one thread, the branch above is empty. No bootstrap
EM runs, no `bs_abundance_*.tsv` is written, nothing is printed, the exit status is 0, and `run_info.json`
still says `"n_bootstraps": N` (`main.cpp:2898-2905`). `BootstrapThreadPool`/`BootstrapWorker`
(`Bootstrap.cpp:15-92`) do not depend on HDF5: the worker writes plaintext tables itself when
`opt.plaintext` is set (`Bootstrap.cpp:84-90`), so nothing stops the pool from being used in every build.
`quant-tcc` runs its bootstraps serially and is not affected.

Executed (`t7_threads_bootstrap.py`, `-b 8 --plaintext --seed 42`, 20,000 pairs):

| build | HDF5 | `-t 1` | `-t 2` | `-t 4` | `run_info` n_bootstraps |
|---|---|---|---|---|---|
| master `4e9f29c`, default CMake | no | 8 tables | **0** | **0** | 8 |
| v0.51.1, v0.50.1 from tags, default CMake | no | 8 | **0** | **0** | 8 |
| 0.48.0 release binary | no | 8 | **0** | **0** | 8 |
| 0.46.1 release binary | yes | 8 | 8 | 8 | 8 |
| 0.50.1, 0.51.1, 0.52.0 release binaries | yes | 8 | 8 | 8 | 8 |
| master `-DUSE_HDF5=ON` | yes | 8 | 8 | 8 | 8 |
| patched (`0001-…patch`), default CMake and `-DUSE_HDF5=ON` | either | 8 | 8, identical to `-t 1` | 8, identical | 8 |

The guard appeared when HDF5 became optional (0.48.0 has it, `main.cpp:3082-3084` at that tag; 0.46.1
compiles the pool unconditionally). Which binaries users get: bioconda (`-DUSE_HDF5=ON` in
`build.sh`) and Homebrew (`-DUSE_HDF5=ON`) are unaffected. Debian's `debian/rules` (kallisto 0.51.1+dfsg)
passes no `-DUSE_HDF5`, so the Debian/Ubuntu package should be affected; that is read from the packaging,
not executed here. `gen_release.sh` uses `cmake -DLINK=static ..` with no HDF5 flag. The 0.50+ release
binaries nevertheless carry HDF5 (executed: they write `abundance.h5` and pass), so they were not
built by that script as checked in. A source build with the documented `cmake ..` (INSTALL.md) is affected.

Fix: construct the pool in every build, passing the HDF5 writer only when there is one, and pass
`n_threads` (the warning just above already caps it at the number of bootstraps). Two-line change plus a
functional test (`../upstream/0001-Run-multi-threaded-bootstraps-in-builds-without-HDF5.patch`). Point
estimates are unchanged (T1/T2/T4 outputs on the patched build are identical to master's). The bootstrap
tables with `-t 2` and `-t 4` equal the `-t 1` tables, because the seeds are drawn before the branch
(`main.cpp:2926-2932`) and each worker writes table `cur_id` with seed `cur_id`.

### KA2: single-end default drops reads whose mean-length fragment would overhang, while the effective length assumes they were counted

`ProcessReads.cpp:1158-1207`: unless `--single-overhang` is given, for single-end reads (and for orphan
mates when `-l` is given in paired mode), a target is removed from the read's pseudoalignment when the
read's start plus the mean fragment length `fl = (int) tc.get_mean_frag_len()` (= `-l`) runs past the
target's end (forward reads, `x.first + fl <= target_len` at :1191) or before its start (reverse reads,
`x.first - fl >= 0` at :1198). If no target survives, the read is not pseudoaligned. The effective
length used for the same target is `L - mu_L + 1` (`weights.cpp:58-79`), where `mu_L` is the mean of the
Gaussian(`-l`, `-s`) truncated at `L` (`trunc_gaussian_fld`, `weights.cpp:248-271`, via
`MinCollector::init_mean_fl_trunc`). That length assumes fragments shorter than `-l` exist and were counted.
The two disagree for every target shorter than about `-l + 2·-s`:

- a target with `L <= -l` can never receive a read: est_counts 0, TPM 0;
- a target slightly longer keeps only reads starting in `[0, L - l]` but is divided by `L - mu_L + 1`;
- all other targets' TPMs rise to absorb the lost mass.

Executed (`t3_single_overhang.py`, reads simulated under kallisto's own likelihood, i.e. target
probability ∝ rho·(L − mu_L + 1), equal true TPM 71,429 for 14 isolated targets of 120–4,000 bp):

| `--single -l 200 -s 20`, 75-bp reads | L=150 | 180 | 200 | 220 | 250 | 1000 | 4000 |
|---|---|---|---|---|---|---|---|
| reads simulated | 56 | 105 | 126 | 225 | 395 | 6149 | 29240 |
| est_counts, default | **0** | **0** | **9** | 173 | 348 | 6091 | 29165 |
| TPM, default | **0** | **0** | **7,291** | 87,789 | 91,403 | 102,522 | 103,449 |
| est_counts / TPM, `--single-overhang` | 56 / 76,539 | 105 / 90,571 | 126 / 72,541 | 225 / 81,141 | 395 / 73,730 | 6149 / 73,552 | 29240 / 73,706 |

With `-l 250 -s 50` (100-bp reads) every target up to 220 bp gets 0. The inflation of the long targets
(+37–45 % here) is exaggerated by the toy: 4 of 14 targets are short. In a real transcriptome the
redistribution is small, while the zeroing and shrinking of short targets is not. Same numbers on all eight
builds (0.46.1–0.52.0). The position scan in the same harness also shows an off-by-one on the forward
side: `x.first` is 1-based (`KmerIndex.cpp:2539`, "position pos (1-based)"), so the forward test drops the last valid start
(start `L - l`, 0-based: start 200 of a 400-bp target with `-l 200` is dropped), while the reverse
test is exact (starts 150+ kept with 50-bp reads).

Tier: held. The exclusion is the documented default (`--single-overhang` "Include reads where
unobserved rest of fragment is predicted to lie outside a transcript"), and the fix is a modelling
choice: make the effective length count only the start positions the filter keeps, or include the reads by
default. Prior thread: #230 (open since 2019, three comments, no maintainer reply) asks why a read at the end
of a transcript fails without `--single-overhang`. Nobody there connects it to the effective length.
A comment on #230 is drafted (`../upstream/comment-ka2-230.md`). The cohort uses single-end `-l/-s` in at
least 3 of 125 papers (`-l 200 -s 20`, `-l 50 -s 20`, `-l 55 -s 1e-08`) and `--single-overhang` in 1.

### KA3: `--bias` bootstraps use the plain effective lengths (duplicate of #151 / PR #260)

`Bootstrap::run_em` (`Bootstrap.cpp:4-13`) builds a fresh `EMAlgorithm` from the fragment-length means,
i.e. with `calc_eff_lens` (`EMAlgorithm.h:43-46`), and runs it with `recomputeEffLen = false`. The point
estimate (`main.cpp:2871`, `em.run(10000, 50, true, opt.bias)`) replaces the lengths with
`update_eff_lens` at round 50 (`EMAlgorithm.h:113-116`). The writers then label every bootstrap with the
point estimate's bias-corrected lengths (`main.cpp:2958-2959`; `Bootstrap.cpp:86-89`). Executed
(`t6_bias_bootstrap.py`, 60 bootstraps, GC-biased library): with `--bias`, 9 of 108 targets with ≥ 50 reads
have a bootstrap mean more than 4 standard errors from the point estimate (up to +18 % / −13 %),
against 1–2 of ~105 without `--bias`. The bootstrap means are closer to an EM run with the plain lengths
(mean |Δ| 5.0 reads) than to one with the bias-corrected lengths (9.2). Already reported: #151 (2017,
diagnosed by the reporter in 2020) and PR #260 (open, unreviewed). The maintainers no longer support
`--bias` (#465, 2024: "The bias option is no longer supported"; it was removed from the usage text but
is still parsed, `main.cpp:241`). Duplicate, not filed.

### KA4: bias-corrected effective length is about 4 bp short on an unbiased library

`update_eff_lens` (`weights.cpp:141-159`, `176-195`) sums the hexamer ratio over forward start positions
`j < L - mu - 6` (`L - mu - 6` positions) and reverse positions `mu - 6 <= j < L - 6` (`L - mu`
positions), then halves the sum (`:199`). With every ratio equal to 1 that gives `L - mu - 3`, not
`L - mu + 1`. Executed (`t6_bias_bootstrap.py` (c), 40 single-isoform targets of 1.5–3 kb, 200,000 unbiased
pairs, `--bias`): `eff_length − (L − mu + 1)` = −4.15 on average (sd 3.92, so ± 0.62 for the mean), the same
on 0.46.1, 0.48.0 and 0.52.0. That is 0.2 % at 2 kb but 8 % for a 300-bp target at `mu = 250`. There is
also a cut-over at `:206`: a bias-corrected length at or below the mean fragment length falls back to the plain
length, a discontinuity for targets near `2·mu`. Held: `--bias` is unsupported (#465).

### KA5: `--bias` segfaults on 0.50.x–0.51.1 (already reported, fixed in 0.52.0)

`t8_bias_runs.py`: on v0.50.1 and v0.51.1 (tag builds and release binaries) every `quant --bias` run
(paired and single-end) dies with SIGSEGV (exit −11) after "[em] quantifying the abundances ..." and
writes no abundance.tsv. 0.46.1, 0.48.0 and 0.52.0 complete. `update_eff_lens` and
`loadTranscriptSequences` iterated over `index.num_trans`. Commit `d0ac69b` (2025-11-17, "fixes issues with
num_trans", in 0.52.0) switched them to `target_lens_.size()`. Reported as #465 (2024). Nothing to file.

## Notes (verified, held)

- **N1: short targets in paired-end mode.** `compute_mean_frag_lens_trunc` (`MinCollector.cpp:641-662`)
  leaves `mean_fl_trunc[L] = 0` for every `L` below the shortest of the (at most 10,000,
  `ProcessReads.cpp:1028`) sampled fragments, so such targets get `eff_length = L + 1`. A slightly longer target
  gets `L − f_min + 1`, which can be 1. T1 (N(250,40)): 40/60/80-bp targets have eff_length 41/61/81 (the
  true-FLD value for 40 bp is 7.6), and a 100-bp target has 4.5 (true 10.1). Single-end `-l 55 -s 1e-08`
  (as in one cohort paper) gives `L + 1` below 55 bp and `L − 54` above. A design consequence of the
  sampled FLD. TPMs of targets shorter than ~2 × the shortest fragment are unstable.
- **N2: EM stopping rule.** `EMAlgorithm.h:174-221`: stop after ≥ 50 rounds once no target with
  `alpha > 0.01` changes by more than 1 % in a round, zero `alpha < 1e-8`, and run one more round.
  This is the rule in the kallisto paper. T2 against an independent EM on the exact classes run to 1e-13:
  total |Δ| 0.069 % and 0.019 % of the reads. 4 and 0 targets with ≥ 10 reads differ by more than 1 %, the
  largest a slowly converging isoform family (17.25 vs 11.14 reads, truth 29.1). Within sampling error,
  and the mean absolute error to the truth is the same (0.109 vs 0.110 reads per read).
- **N3: fragment-length estimate.** `mapPair` (`KmerIndex.cpp:1691-1767`) returns a length only when both
  mates' first k-mers lie on the same unitig, in the same EC block, and only for pairs compatible with
  one target (`ProcessReads.cpp:1252-1258`). Fragments ≥ 1000 bp are dropped (`MAX_FRAG_LEN`).
  T5: single-isoform transcriptomes give the simulated mean within ±0.6 bp. Isoform-rich ones (60–250-bp
  exons) come out 1.0–3.6 bp low against all fragments and 1.5–4.8 bp low against the uniquely compatible
  ones (the longer the FLD, the more fragments span a unitig boundary). The TPM effect is ≤ 0.5 % for
  targets ≥ 500 bp.

## Held up under execution

- **TPM.** `counts_to_tpm` (`PlaintextWriter.cpp:5-27`) matches `1e6·(c/l)/Σ(c/l)` to 1e-5 in every
  abundance.tsv, every bootstrap table and the TPM recomputed from abundance.h5 (T1, T6, T9; all builds).
- **Single-end effective length.** It equals `L − mu_L + 1` with the truncated Gaussian for every target
  (40–3,000 bp, including targets shorter than `-l` and the 999/1000/1001 boundary of `MAX_FRAG_LEN`). This
  holds for `-l/-s` 200/20, 180/30, 50/20, 55/1e-8 and 300/80, to 5e-6 (T1).
- **Paired-end effective length.** It equals `L + 1 − mu_L` with kallisto's own FLD. The FLD matches the
  truth apart from N1/N3 (T1, T5).
- **Pseudoalignment.** On error-free reads, every one of 119,987 fragments' ECs (`bus --num`) equals
  the exact set of targets containing both mates; `n_pseudoaligned`/`n_unique` equal the exact counts (T2).
- **Strand options.** `--fr-stranded` and `--rf-stranded` (`ProcessReads.cpp:61-133`), paired and
  single-end, under fr and rf protocols with antisense overlaps: `n_pseudoaligned` and `n_unique` equal the
  exact stranded compatibility in all 12 configurations. With the matching option every read goes to its
  source (|Δ| = 0). With the opposite option exactly the antisense-overlap reads are kept, assigned to the
  partner (T4).
- **run_info.json.** `n_processed` = pairs; random pairs never pseudoalign; `p_pseudoaligned` =
  100·n_pseudoaligned/n_processed to one decimal; the sum of est_counts equals `n_pseudoaligned` (T7, with
  0.5 % substitution errors and 10 % random pairs).
- **Determinism.** `-t 1` and `-t 4` give identical abundance.tsv and run_info counts (T7). With HDF5,
  bootstrap datasets are identical across thread counts (T9; the order problem of #236 is gone).
- **HDF5.** `est_counts`, `aux/eff_lengths`, `aux/ids` and `aux/num_bootstrap` equal the TSV and the request
  (T9: master with HDF5, the 0.52.0 and 0.46.1 release binaries).
- **Bootstraps without `--bias`.** They centre on the point estimate: 1–2 of ~105 targets beyond 4 SE,
  median |z| 0.8 (T6).

## Withdrawn or not pursued

- `countBias` always returns `false` (`MinCollector.cpp:774-777`), so the per-batch `biasgoal` is never
  decremented (`ProcessReads.cpp:1244-1248`) and bias hexamers are collected for whole batches until
  `maxBiasCount` is passed. Read only, not executed; it affects only the unsupported `--bias` path.
- A memory leak in the EM inner loop (`continue` before `delete[] trs` when `denom < TOLERANCE`,
  `EMAlgorithm.h:155-157`, `delete[]` at :166). No effect on numbers.
- `EMAlgorithm::set_start` computes starting values and then overwrites them with `std::copy`
  (`EMAlgorithm.h:438-462`). Dead code: bootstraps no longer call it (`Bootstrap.cpp:8`).
- The `calc_eff_lens` fallback `if (cur_eff_len < 1.0) cur_eff_len = L` (`weights.cpp:71-74`) cannot trigger,
  because `mu_L <= L` always.

## Not checked

Reads with indels and real-data error profiles; `--genomebam`/`--pseudobam` (no htslib in these builds);
gene-level output (`-g`/`--gtf`); `quant-tcc` beyond reading its effective-length branch (with no FLD
given, all effective lengths are 1, `main.cpp:3210-3213`, by design); `bus`/bustools single-cell
workflows; long-read mode; `--priors`; d-list indexes; k other than 31; Windows/macOS builds; the Debian
package binary itself.
