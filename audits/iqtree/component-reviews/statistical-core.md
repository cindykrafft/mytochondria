# Component: IQ-TREE 2 statistical core (`master` @ `a00094e0`, 2025-04-10, version string 2.4.0)

Read in full: `main/phylotesting.cpp` (information criteria, ModelFinder candidate
handling; 3,772 lines), `model/modelfactory.cpp` (parameter counting, `+ASC` setup; 1,591),
`model/rategamma.cpp` (478), `model/rategammainvar.cpp` (330), `model/rateinvar.cpp` (138),
`model/ratefree.cpp` (677), `tree/discordance.cpp` (gCF/sCF; 933); targeted reads of
`tree/phylotree.cpp` (`testOneBranch`/`testAllBranches`, `Statistics_To_Probabilities`,
`resampleLh`, `getNBranchParameters`), `tree/iqtree.cpp` (`saveCurrentTree`,
`summarizeBootstrap`, `computeBootstrapCorrelation`, `refineBootTrees`, the log-likelihood
cutoff), `pda/splitgraph.cpp` (`scaleWeight`), `tree/mtree.cpp` (`createBootstrapSupport`),
`alignment/alignment.cpp` (`createBootstrapAlignment`, `getUnobservedConstPatterns`, the
constant/invariant flags), `tree/phylokernelnew.h` (the Lewis correction),
`model/modelmarkov.cpp`, `model/modeldna.cpp`, `model/modelgtr.cpp`, `utils/tools.cpp`
(`nFreqParams`, option parsing, defaults), `main/phyloanalysis.cpp` (`reportTree`).

Every suspicion was **executed on the shipped binary**: `master` built with gcc 13.3
(`cmake` + `make`, OpenMP on, see `../README.md` for the three dependencies the
environment lacked), the v2.4.0 release tag built the same way, and — because the manual
now sends users to `iqtree/iqtree3` — the iqtree3 `master` too (see `../README.md`).
Harnesses in `../verify/` with captured output (`.out` = master, `.v2.4.0.out` = release
tag, `.v3.out` = iqtree3 3.1.3 for the four harnesses that carry the notes; all identical). The reference is an independent numpy/scipy implementation written for this project
(`../verify/iqt.py`: Felsenstein pruning under a reversible model, Yang's discrete gamma
via `scipy.stats.gamma`, RELL resampling, quartet counting), or IQ-TREE's own slower
alternatives (`-te` fully optimised alternative topologies; the standard bootstrap `-b`).

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Summary

No defect in a published number was found on `master`. Everything the cohort papers
report — log-likelihoods, ModelFinder's AIC/AICc/BIC and parameter counts (single and
partitioned), the discrete-gamma rates (mean and `-gmedian`), `+I`, `+I+G`, `+ASC`, UFBoot
support percentages, SH-aLRT, aBayes, the parametric aLRT, gCF and sCF — equals the
reference to the precision printed. The five items below are notes: one on what the
"parametric aLRT support" number actually is, one on an undocumented sensitivity of
UFBoot to its candidate-tree cutoff that shows on a degenerate 4-taxon alignment, one on
reproducibility across thread counts with a fixed seed, and two on rooted input trees in
the concordance-factor code. One suspicion (double-counting `+F`) was withdrawn.

## Findings

### IQ1 — NOTE (documentation; design inherited from PhyML): the `-alrt 0` "parametric aLRT" support is the cube of the mixture-χ² CDF, not `1 − p`

**Code.** `tree/phylotree.cpp:5228-5252` (`testOneBranch`) computes the aLRT statistic
`2·(ℓ₀ − max(ℓ₁, ℓ₂))` over the two NNI alternatives (five branches re-optimised,
`:5028`) and converts it with `Statistics_To_Probabilities` (`:5057-5225`, marked "TAKEN
FROM PHYML source code alrt.c"). That function linearly interpolates a table of χ²₁
quantiles (`:5069-5209`), caps at 0.9999 above 12.116 (`:5211`), then

```cpp
rough_value=rough_value+(1.0-rough_value)/2.0;    // :5221  -> 1 - p under 1/2 chi2_0 + 1/2 chi2_1
rough_value=rough_value*rough_value*rough_value;   // :5222  -> cubed
```

The first line is the Anisimova & Gascuel (2006) mixture null; the second cubes it. The
manual (`Command-Reference.md:545`) says only that `-alrt 0` performs "the parametric
aLRT test (Anisimova and Gascuel 2006)". Anisimova & Gascuel's own PhyML implementation
carries the same two lines, so this is not an IQ-TREE transcription error; it is an
undocumented transform of the number users read as a support value.

**Executed** (`../verify/heldup_branch_tests.py`, 4-taxon JC alignment so the NNI
alternatives are the other two topologies and their log-likelihoods come from `-te`
runs): with `ℓ₀ = −1230.5062`, `ℓ₁ = −1231.5444`, `ℓ₂ = −1231.7738`, the statistic is
2.0764; the χ²₁ CDF is 0.8504, the mixture CDF 0.9252 (p = 0.075), and the binary prints
`0.78` — the port of the table gives 0.7797. So a branch whose mixture-null p-value is
0.075 is labelled 0.78, and one at the conventional p = 0.05 (statistic 3.841 → mixture
CDF 0.975) would be labelled 0.927. Identical on v2.4.0 (`.v2.4.0.out`), present in
1.6.12 by reading (`Cibiv/IQ-TREE` v1.6.12 `tree/phylotree.cpp:4513-4514`) and in iqtree3
`master` (`tree/phylotree.cpp:5336`). The cohort exposure is tiny (no paper names
`-alrt 0`; 9 name SH-aLRT), which is why this is a note rather than a finding — but the
manual should say what the number is. A cosmetic edge: the interval test at `:5097` uses
`>` where the others use `>=`, so a statistic of exactly 0.000982 falls through to an
interpolation with `a = b = 0` (division by zero); unreachable in practice.

### IQ2 — NOTE (design; degenerate demonstration): UFBoot's candidate-tree cutoff can exclude every alternative topology, and then the support is 100 % whatever the data say

**Code.** `tree/iqtree.cpp:2293-2295` sets `logl_cutoff` to the minimum original-alignment
log-likelihood among the trees currently assigned to bootstrap replicates, and
`saveCurrentTree` (`:3551-3553`) discards any tree whose log-likelihood is more than 1
unit below it:

```cpp
if (logl_cutoff != 0.0 && cur_logl < logl_cutoff - 1.0)
    return;
```

Trees that survive compete per replicate by RELL likelihood with a documented tie rule
(within `ufboot_epsilon = 0.5`, `utils/tools.cpp:1307`, the incumbent is replaced with
probability `1/(count+1)`, `:3617-3619`). The cutoff is a speed device from the UFBoot
design; its consequence is that an alternative topology more than one log-likelihood unit
worse on the *original* alignment can never be chosen for a replicate, even if that
replicate's resampled sites would prefer it.

**Executed** (`../verify/note_degenerate_alignments.py`, part A): 4 taxa, 100 constant
columns plus a single AABB site. IQ-TREE's own standard bootstrap (`-b 200`) gives 61 %
for the split (the site is in a replicate with probability 63.4 %); UFBoot (`-B 1000`)
gives **100 %** and all 1,000 `.ufboot` trees are the ML topology (three seeds). The log
prints the cutoff, −147.108; the two alternative topologies, fully optimised with `-te`,
have log-likelihood −153.4339, i.e. 6.3 below it, so they are never candidates. SH-aLRT
on the same branch is 91.8–93.8 % and aBayes 0.999, which is what those tests do by
construction (a single site with Δℓ = 6.7 is "significant"); they are not affected by
the cutoff. Identical on v2.4.0; the cutoff line exists in 1.6.12
(`tree/iqtree.cpp:3500`) and iqtree3 (`tree/iqtree.cpp:3854`).

**Scope.** This did not reproduce in less degenerate settings: with 6 taxa, 500 simulated
sites and a branch supported by k = 1, 2, 4 added sites, UFBoot gave 53 / 69 / 88 % against
the standard bootstrap's 53 / 77 / 92 % (`../verify/note_ufboot_single_site.py`), and on
star-tree data with 4–6 taxa UFBoot's supports (27–77 %) tracked or undercut `-b 200`
(`../verify/note_ufboot_star_tree.py`). So on realistic data the cutoff leaves enough
near-optimal trees in play. It is recorded because the failure mode is silent, the
hard-coded `1.0` is not an option, and the manual does not describe it.

### IQ3 — NOTE (reproducibility; upstream issue #228 closed 2024-06-17): SH-aLRT and UFBoot with a fixed `-seed` depend on the thread count

**Code.** `testOneBranch` seeds one stream per OpenMP thread from `ran_seed +
omp_get_thread_num()` and splits the RELL replicates across threads (`tree/phylotree.cpp:
5268-5271`); `saveCurrentTree` draws a fresh `rand_seed` from the global stream and does
the same for the per-replicate tie-breaking (`tree/iqtree.cpp:3594-3600`); the sCF
sampler likewise (`tree/discordance.cpp:46`).

**Executed** (`../verify/heldup_ufboot.py`): `-alrt 1000 -seed 3` on an 8-taxon
alignment gives 95.8 / 97.6 / 95.3 / 99.8 / 97.7 with `-T 1` and 96.1 / 97.3 / 95.8 /
99.8 / 98.1 with `-T 2` (two `-T 1` runs are identical). With `-B 1000 -seed 3`, 12 of
the 1,000 `.ufboot` replicate trees differ between `-T 1` and `-T 2`, though the rounded
supports coincide on this alignment. Documented only as `-seed` "to reproduce a previous
run" (`Command-Reference.md:84`); issue #228 raised exactly this and is closed. A
sentence in the manual ("with the same thread count") is all that is missing.

### IQ4 — NOTE (usability; silent output): a rooted species tree gets `NA` for the branch at its root in `--scf`/`--gcf`, and a rooted gene tree aborts `--gcf`

**Code.** IQ-TREE reads a Newick with a bifurcating root as rooted (adding a `__root__`
leaf). `computeSiteConcordance` returns before computing anything for a branch adjacent to
the root (`tree/discordance.cpp:152-155, 166-169`), and `computeGeneConcordance` treats a
gene tree's `__root__` as a taxon and stops with "Taxon not found in full tree" (`:733`).

**Executed** (`../verify/heldup_concordance_factors.py`): `-t '((A,B),(C,D));' --scf 100`
logs "rooted tree with 4 taxa and 7 branches" and writes `sCF = NA` for both internal
rows of `.cf.stat` — the only real internal branch of a 4-taxon tree gets no value;
the unrooted spelling `(A,B,(C,D));` gives sCF 80 (exact). `--gcf` with a gene tree
written `((A,B),(C,D));` aborts with `ERROR: Taxon not found in full tree: __root__`.
Same on v2.4.0 and iqtree3 (`tree/discordance.cpp:156, 171, 789`). Concordance factors
appeared in 2.0, so 1.6.12 is not affected. The manual's concordance-factor page does
not mention rooting; users who pass a rooted species tree from ASTRAL or a dating run
get `NA` on the root split with no warning.

### IQ5 — WITHDRAWN (own suspicion): `+F` is not double-counted in the parameter count for DNA models

`ModelDNA::getNDim` (`model/modeldna.cpp:422-440`) adds `nFreqParams(freq_type)` for
non-estimated frequencies while `ModelMarkov::getNDimFreq` (`model/modelmarkov.cpp:
978-1000`) adds `num_states − 1` for `FREQ_EMPIRICAL`, and `getNParameters` sums both
(`model/modelfactory.cpp:1031-1035`). That looked like counting the three `+F` parameters
twice. `nFreqParams` (`utils/tools.cpp:7817-7838`) returns 1 or 2 only for the
Lie-Markov frequency classes and 0 otherwise, so `+F` is counted once. Executed:
`GTR+F+I+G4` on 6 taxa reports 19 free parameters = 9 branches + 5 + 3 + 1 + 1
(`../verify/heldup_information_criteria.py`), and all 92 ModelFinder rows have the
parameter count their names imply.

## What held up (executed, not just read)

- **Likelihood engine** (`../verify/heldup_likelihood_closed_form.py`, 5 taxa, 300 sites,
  `-te -blfix` with fixed model parameters): JC, JC+G4{0.6}, JC+G4 with `-gmedian`,
  JC+I{0.3}, JC+I{0.3}+G4{0.6}, GTR{…}+F{…}, GTR+F+G4, JC+ASC, GTR+F+ASC+G4 all agree with
  the numpy pruning reference to ≤ 4.7e-5 (the report's four decimals).
- **Discrete gamma** (`model/rategamma.cpp:98-172`): the mean-of-bin rates equal Yang's
  eqs 9–10 via `scipy.special.gammainc` (0.05311, 0.3123, 0.8813, 2.753 at α = 0.6), and
  `-gmedian` gives the (2i+1)/2k quantiles rescaled to mean 1 (0.05037, 0.3453, 0.9783,
  2.626). The manual documents mean as the default and the median switch
  (`Substitution-Models.md:436`).
- **`+I+G`** (`model/rategammainvar.cpp:33, 58`): gamma rates scaled by 1/(1 − p_inv)
  (0.07587, 0.4461, 1.259, 3.933 at p_inv = 0.3) with proportions (1 − p_inv)/k = 0.175;
  the mean rate is 1 and the log-likelihood matches.
- **`+ASC`** (`model/modelfactory.cpp:674-705`, `tree/phylokernelnew.h:3212-3219`):
  Lewis's correction ℓ − n·log(1 − Σ P(constant pattern)) over the unobserved constant
  patterns of every state, matching the reference on the 168 variable columns; the
  guard refuses an alignment with invariant sites ("Invalid use of +ASC because of 132
  invariant sites") and writes the variable-site alignment for the user. "Invariant"
  includes gap/ambiguity-compatible columns (`alignment/alignment.cpp:1018`), which is
  the correct notion for conditioning on variability.
- **Information criteria** (`main/phylotesting.cpp:483-487`; sample size = alignment
  length, `:244`, or the sum over partitions, `:247-250`): AIC = −2ℓ + 2k, AICc = AIC +
  2k(k+1)/max(n−k−1, 1), BIC = −2ℓ + k·ln n. Reported values equal the recomputation to
  ≤ 1.5e-3 (the table prints three decimals) for all 92 ModelFinder candidates and the
  full-model report; the best model is the BIC argmin (ties go to the earlier row,
  `:280-286`); k matches the count implied by each model name (rate parameters + 3 for
  `+F` + 1 each for `+G`, `+I` + 2c−2 for `+Rc` + 2n−3 branches).
- **Partition parameter counts** (`tree/phylotree.cpp:2567-2591`, `main/phylotesting.cpp:
  1836-1839`): `-p` (proportional) 9 + 1 + 2·9 = 28, `-q` 27, `-Q` 36 for two `GTR+F+G4`
  partitions; `-m MFP -p` selecting `K2P+G4` and `HKY+F+I` reports 17 = 9 + 1 + 2 + 5.
- **FreeRate** (`model/ratefree.cpp:286-296`): `+Rc` counts 2c−2 free parameters
  (proportions and rates each constrained by one normalisation), categories sorted by rate
  after optimisation (`:246`); reflected in ModelFinder's k above.
- **aBayes** (`tree/phylotree.cpp:5255`) equals 1/(1 + e^{ℓ₁−ℓ₀} + e^{ℓ₂−ℓ₀}) to 6e-4 using
  `-te` log-likelihoods (the NNI optimisation stops a little short of the `-te` optimum).
- **SH-aLRT** (`tree/phylotree.cpp:5273-5307`): RELL resampling of the three site-
  log-likelihood vectors (`resampleLh` → `createBootstrapAlignment`, multinomial over
  sites, `alignment/alignment.cpp:3822-3846`), Guindon et al.'s rule counting a replicate
  when the observed aLRT exceeds the centred best-minus-second-best plus 0.05. An
  independent port gives 37.70 % against the printed 37.0 % with 20,000 replicates (MC
  s.e. of the difference 0.48) and 100 % vs 100 % on a strongly supported branch.
- **UFBoot summary** (`tree/iqtree.cpp:3683-3736`, `pda/splitgraph.cpp:634-642`,
  `tree/mtree.cpp:2736-2783`): support = round(100 · k/1000) for each split of the ML
  tree; all five branches match a recount of the `.ufboot` trees (994/1000 → 99,
  973 → 97, 977 → 98, …). Two runs with the same seed and thread count are byte-identical.
  `--bnni` (`refineBootTrees`, `:2650-2830`: two branch-length passes then an NNI search
  on each replicate's alignment) refined 58 of 1,000 trees and the printed supports again
  equal the refined split frequencies. The convergence statistic is Pearson's correlation
  of split frequencies between the two halves of the run (`:4139-4172, :4173-4212`;
  threshold 0.99, `utils/tools.cpp:1316`); 1.000 in the log.
- **Concordance factors** (`tree/discordance.cpp:99-116, 144-300, 704-860`): on a 4-taxon
  tree the single quartet gives sCF 80, sDF1 6.67, sDF2 13.33, sN 15, exactly the site
  counts [12, 1, 2]; on 6 taxa, 20,000 sampled quartets give 88.57 / 90.83 / 81.98 against
  the exhaustive four-quartet averages 88.58 / 90.83 / 81.93; every one of 150 rows in
  `.cf.quartet` (`--cf-quartet`) matches the port's counts; gCF, gDF1, gDF2, gDFP and gN
  equal an independent implementation (decisive = a taxon in each of the four subtrees,
  concordant = induced split present, NNI alternatives tested in order) on 17 gene trees
  with missing taxa. sN averages the decisive-site count over quartets, and sCF is the
  mean of per-quartet fractions, as the 2020 paper defines them. Issue #415 (open)
  questions that definition's denominator — a design question, not a defect.
- **Duplicate sequences** are kept in the tree ("E is identical to A but kept") and the
  reported log-likelihood equals the reference at the printed branch lengths (1.1e-5).
- **Tie handling in UFBoot** is randomised reservoir replacement (documented UFBoot2
  behaviour, `tree/iqtree.cpp:3617-3625`), so identical-likelihood candidates share the
  replicates rather than the first one winning (star-tree checks).

## Design choices worth knowing (not findings)

- AICc uses `max(n − k − 1, 1)` in the denominator (`main/phylotesting.cpp:485`), so for
  k ≥ n − 1 the penalty is finite and the report prints a warning block rather than
  refusing (`main/phyloanalysis.cpp:781-808`).
- For codon alignments tested as nucleotide under ModelOmatic the BIC sample size is the
  codon count (`MF_SAMPLE_SIZE_TRIPLE`, `main/phylotesting.cpp:251-252, 2603`).
- SH-aLRT reuses the same RELL weights for every branch (the per-thread streams are
  re-seeded per branch, `tree/phylotree.cpp:5270`) — common random numbers, fine.
- The SH-like test is not a bootstrap: on the one-site alignment it gives ~93 % because
  replicates without the site still see the two alternatives tie (Guindon et al.'s rule);
  users comparing it with UFBoot's 100 % and the standard bootstrap's 61 % should know the
  three numbers estimate different things.

## Not checked here

Tree search (NNI/SPR candidate set, stopping rules, `-nstop`), the AU/KH/SH topology tests
(`-zb`), mixture and PoMo models, `--scfl` (likelihood-based sCF, iqtree3), AliSim, dating
(LSD2/MCMCtree), MPI builds, checkpoint/restart, protein-matrix internals beyond parameter
counts, and the `1.6.12` branch-length/likelihood kernels (1.6.12 was read for the three
line citations above, not built).
