# iqtree/iqtree3 #198 — SH-aLRT values change when the jackknife (`-j`/`-J`) is requested

Third issue-fix for IQ-TREE 3 (after #203 / PR #207 and #192 / PR #210, both merged without
discussion). **Filed as PR #214 on 2026-09-09.** Branch `fix/issue-198-sh-alrt-jackknife` on `cindykrafft/iqtree3` (one commit,
`e8ca14f3`, on upstream master `6799c7fa`). Chosen because it is a silent wrong-number in a
support value that ends up in papers: anyone who runs `--ufjack` (or `-j`) together with `-alrt`
gets inflated SH-aLRT supports, with no warning, in every 3.x release (and 2.x, where the same
code exists). #198 has no comments; #196 by the same reporter (the `--jack-prop` wording) is
already fixed on master (b8ef4238, 2026-08-03) and still open.

## Cause

`tree/phylotree.cpp`, `PhyloTree::resampleLh()`: the RELL replicates of the SH-aLRT test
(`testOneBranch()`) and of the local bootstrap probability are drawn with
`aln->createBootstrapAlignment(boot_freq, params->bootstrap_spec, rstream)`, and
`Alignment::createBootstrapAlignment()` → `random_resampling()` (`utils/tools.cpp`) switches to
delete-`jack_prop` jackknife sampling whenever the global `Params::jackknife_prop` is non-zero,
which `-j`/`-J` set to 0.5. A jackknife replicate sums only half the sites, so
`E[lh_new[i]] = lh[i] / 2` instead of `lh[i]`; the centred statistics `cs[i] = lh_new[i] − lh[i]`
in `testOneBranch()` acquire a mean of `−lh[i]/2`, the worst NNI tends to become `cs_best`, and
the criterion `aLRT > cs_best − cs_2nd_best + 0.05` is met far more often than under the bootstrap
null. Every branch's SH-aLRT goes up; weak branches most.

## Fix

`random_resampling()` and `createBootstrapAlignment(int*, spec, rstream)` (Alignment and the
SuperAlignment override) take an optional `double jackknife_prop`, negative by default meaning
"use the global setting"; `resampleLh()` passes `0.0`, so SH-aLRT/LBP replicates are bootstrap
samples as the tests are defined (Guindon et al. 2010; Adachi & Hasegawa 1996). The tree-search
resampling of `-j`/`-J`, and the `GENE`/`GENESITE`/`SCALE=` paths, are untouched. Alternative
kept for the maintainers: rescale jackknife replicates by `1/(1 − jack_prop)` (the pseudo-value
has the bootstrap expectation and, for delete-half, the bootstrap variance); the reference below
shows it agrees with the bootstrap.

## Verification (`repro.sh`, `repro.before.out`, `repro.after.out`)

AliSim, 24 taxa, JC, 800 sites; `-alrt 1000` alone, with `-bb 1000` and with `--ufjack 1000`,
same seed, `-T 1`:

| binary | none / `-bb` | `--ufjack` |
|---|---|---|
| master 3.1.3 | 96.8 99.9 100 100 100 **34.7** 100 **72.3** 100 92.7 **71.5** 100 99.9 **86.9** … | 100 100 100 100 100 **62.7** 100 **98.1** 100 100 **95.5** 100 100 **100** … |
| branch | same | same as `-bb` (one branch 72.4 vs 72.3: one replicate in 1000) |

UFBoot and UFJack values themselves are bit-identical before and after. On the maintainers'
`turtle.fa` with the test seed the nine SH-aLRT values are 98.4 89.8 98.2 61.7 47.6 47.9 98 100
81.1 with `-B` and 100 100 100 91.7 86 81.5 100 100 99.7 with `-J` on master; identical with the
branch.

`sh_alrt_reference.py` (+ `.out`) re-implements the `testOneBranch()` rule in numpy on site
log-likelihoods that IQ-TREE writes for the ML tree and its two NNI neighbours (branch lengths
re-optimised, so the aLRT differs a little from IQ-TREE's five-branch optimisation): on four
branches, bootstrap RELL 60.3 / 54.6 / 74.6 / 85.8, delete-half jackknife 74.0 / 82.9 / 97.6 /
100.0, jackknife × 2 (pseudo-value) 57.5 / 53.8 / 74.0 / 85.1, 20,000 replicates each. The
inflation is the missing centring.

## Filed, and the maintainers' first response (2026-09-10)

PR #214. The maintainer asked for the `test_scripts` additions to be removed: the CI is meant to
cover a few popular use cases and to build beta binaries within about twenty minutes, not to be an
extensive test suite, and further testing should go in the PR description as input files and
commands. The three `test_scripts` files were reverted and the branch force-pushed as commit
`04f81848` (code only, six files, same fix); the reproduction moved into the PR body and into
`comment-214-ci-removed.md`, using `turtle.fa`, which the repository already ships, so no
attachments are needed. The full suite result below stays in the kit as our own evidence.

## Test that was removed from the PR at the maintainers' request

`test_iqtree.sh` / `.ps1`: `turtle.fa -B 1000 -alrt 1000` and `turtle.fa -J 1000 -alrt 1000`,
same seed, followed by a check that the SH-aLRT labels of the two `.treefile`s are identical
(fails on unmodified master); `expect_ans.txt` rows `turtle.alrt.boot.iqtree` and
`turtle.alrt.jack.iqtree` (−5370.3730, threshold 1). Full `test_iqtree.sh` + `verify_results.sh`:
see `test-runs.txt`.

## Caveats

- The topology tests (`--test`, `treetesting.cpp:1162`) draw their RELL replicates the same way
  and the AU test errors out under `-j`/`-J`; left for a follow-up and said so in the PR body.
- The reporter saw "lower resolution" with jackknife; on our data and on turtle.fa the values are
  inflated (everything near 100), which is the same loss of discrimination.
- `expected_runtime.tsv` / `expected_memory.tsv` rows for the two new runs are the maintainers'
  to add, as for the previous two PRs.

## Other candidates considered (57 open issues read by title, 11 by body; comments of #196,
#128, #111, #85, #80, #135, #102, #166 could not be read: the helper export blocked on a permission)

| issue | why / why not |
|---|---|
| **#198** (chosen) | wrong support values under a documented option; reproduced from the body alone; 30-line fix with a test |
| #196 `--jack-prop` wording | already fixed on master (b8ef4238); could be closed |
| #80 `-mrate` cannot disable `+ASC` in partitioned ModelFinder | probably real (`getRateHet()` adds `+ASC` whenever a partition has no invariant site, and the partition path takes `merge_rates`/`ratehet_set` differently); next candidate, needs a partitioned reproduction |
| #128 LSD dating writes nothing (Windows, 4 taxa, data in the body) | reproducible from the body; not a wrong number; one unread comment |
| #111 `-g` with a mixed morphological/molecular partition crashes in `computeMixLh` | crash on valid input; needs the reporter's attachments |
| #85 `-te` not honoured by `--scfl` | needs the reporter's 400-locus data |
| #135 / #102 `setRootNode` assertion | fixed by PR #207; still open, maintainers' to close |
| #91 MPI `-nt AUTO` | needs an MPI build |

## Files

`repro.sh`, `repro.before.out`, `repro.after.out`, `sh_alrt_reference.py`, `sh_alrt_reference.out`,
`0001-SH-aLRT-draw-RELL-replicates-as-bootstrap-samples-wh.patch`, `pr-body.md`, `test-runs.txt`.
