# IQ-TREE 2 audit against 258 published papers (2021–2026)

_Twelfth audit in the series. Generated 2026-09-03 against `iqtree/iqtree2` `master` @
`a00094e0` (2025-04-10, version string 2.4.0), the v2.4.0 release tag (2025-02-07, the
latest release in that repository), and `iqtree/iqtree3` `master` @ `8977d31a` (2026-08-03,
where development has moved). Focus: correctness of the numbers papers report, verified by
running the built binary against independent implementations._

## What this is

The six-journal survey found **258 papers** in PNAS (156), *Nature* (82), *Cell* (13),
*Science* (4) and *The Lancet* (3), 2021–2026, that used IQ-TREE, the most-cited
maximum-likelihood phylogenetics program of the period. The code that produces the numbers
those papers print — ModelFinder's information criteria and parameter counts, the
likelihood under `+G`/`+I`/`+R`/`+F`/`+ASC`, the ultrafast bootstrap (UFBoot2) support
percentages with and without `--bnni`, SH-aLRT, aBayes and the parametric aLRT, and the
gene/site concordance factors — was read in full on `master` and every suspicion was
executed on the shipped binary on synthetic alignments with known truth, with a numpy/
scipy implementation written for this project, or IQ-TREE's own exact alternatives (`-te`
runs, the standard bootstrap `-b`), as the reference.

## Findings (details and line citations in [`component-reviews/statistical-core.md`](component-reviews/statistical-core.md); harnesses with captured output in [`verify/`](verify/))

**No wrong number was found on `master`.** Every number checked equals the reference to
the precision printed. The notes:

| id | status | finding |
|---|---|---|
| IQ1 | note, documentation (design inherited from PhyML) | The `-alrt 0` "parametric aLRT" support is the *cube* of the ½χ²₀+½χ²₁ mixture CDF (`tree/phylotree.cpp:5221-5222`), not 1 − p as the manual's citation of Anisimova & Gascuel suggests. Executed on a 4-taxon JC alignment: statistic 2.0764, mixture CDF 0.9252 (p = 0.075), printed value 0.78 (port 0.7797); a branch at p = 0.05 would print 0.927. Same in v2.4.0, 1.6.12 (by reading) and iqtree3. No cohort paper names `-alrt 0`. |
| IQ2 | note, design (degenerate demonstration) | UFBoot never assigns a replicate to a tree more than 1 log-likelihood unit below the cutoff (`tree/iqtree.cpp:3553`). On 4 taxa with 100 constant columns and one informative site, IQ-TREE's standard bootstrap gives 61 % (63.4 % expected) and UFBoot **100 %** — all 1,000 replicate trees are the ML topology because the two alternatives (−153.43) sit 6.3 below the printed cutoff (−147.108). Did not reproduce on 6-taxon constructions (UFBoot 53/69/88 % vs standard 53/77/92 %) or star-tree data (4–6 taxa). Same in v2.4.0; line present in 1.6.12 and iqtree3. |
| IQ3 | note, reproducibility (upstream #228, closed) | With a fixed `-seed`, SH-aLRT values change with the thread count (95.8/97.6/95.3/99.8/97.7 at `-T 1` vs 96.1/97.3/95.8/99.8/98.1 at `-T 2`) and 12 of 1,000 UFBoot replicate trees differ; runs with the same `-T` are byte-identical. The manual documents `-seed` without this qualifier. |
| IQ4 | note, usability (silent output) | A species tree with a bifurcating root is read as rooted and the branch at the root gets `sCF = NA` in `--scf` (on a 4-taxon tree that is the only internal branch); a rooted gene tree makes `--gcf` abort with `Taxon not found in full tree: __root__`. Same in v2.4.0 and iqtree3; the concordance-factor manual page does not mention rooting. |
| IQ5 | withdrawn | Suspected double-counting of `+F` in the parameter count (`ModelDNA::getNDim` + `getNDimFreq`); `nFreqParams` returns 0 for `+F`, and the binary reports 19 for `GTR+F+I+G4` on 6 taxa (9 + 5 + 3 + 1 + 1). |

**Held up under execution** (all on `master` and v2.4.0): log-likelihoods under JC,
GTR+F, `+G4` (mean and `-gmedian`), `+I`, `+I+G4` and `+ASC` to ≤ 5e-5 of the pruning
reference; the discrete-gamma category rates against scipy; AIC/AICc/BIC arithmetic and
parameter counts for all 92 ModelFinder candidates and for `-p`/`-q`/`-Q` partition
models; aBayes; SH-aLRT against an independent RELL port (37.70 % vs 37.0 % printed,
20,000 replicates); UFBoot supports equal to the split frequencies of the `.ufboot`
trees, with and without `--bnni`; the bootstrap-correlation statistic; sCF exact on a
single-quartet tree and within Monte-Carlo error of the exhaustive average on 6 taxa,
every `.cf.quartet` row exact; gCF/gDF1/gDF2/gDFP exact on 17 gene trees with missing
taxa; duplicate-sequence handling. Not checked: tree search, topology tests, mixture/PoMo
models, `--scfl`, AliSim, dating, MPI.

## How the papers use IQ-TREE (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 104 (1.6.x 52 — 1.6.12 alone 28; 2.1.x 32; 2.2.x 27; 2.0.x 26; 2.3.x 11; 2.4.0 1; 3.0.1 1) |
| IQ-TREE 2 named / 1.x named / 3 named | 82 / 33 / 2 |
| ultrafast bootstrap (UFBoot) | 61 (1,000 replicates stated 74; 10,000 stated 4; `--bnni` 3) |
| ModelFinder (`-m MFP`/`TEST`) | 50 (`+MERGE`/PartitionFinder 26) |
| protein matrix named (LG/JTT/WAG…) / GTR / HKY-family | 41 / 23 / 8 |
| `+G` / `+F` / `+I` / `+R` / `+ASC` | 38 / 34 / 21 / 20 / 4 |
| concatenation / supermatrix | 30 |
| partition model (`-p`/`-q`/`-Q`) | 16 |
| SH-aLRT named | 9 (1,000 replicates stated 4) |
| standard bootstrap (`-b`) | 12 |
| protein mixture (C10–C60/LG4X/PMSF) | 11 |
| constraint tree (`-g`) | 5 |
| gCF/sCF | 0 detected in the cache (mined text is a few hundred characters per paper) |
| co-used: MAFFT/MUSCLE 163, trimAl/ClipKIT/Gblocks 24, RAxML 25, ASTRAL/coalescent 12, MrBayes/BEAST 22 | |

Versions pinned run 1.3 to 3.0; the four notes concern behaviour present in every version
the cohort names (IQ4 from 2.0 on).

**Profiling caveat.** As for the Seurat and Scanpy audits, this session had no route to
Europe PMC, so `iqtree_profile.py` ran in `--offline` mode over the survey's stored
evidence snippets; every record in `iqtree_profiles.jsonl` is `source: survey_cache` and
every count above is a lower bound. Rerun without `--offline` from a host with Europe PMC
access to replace them with full-text records.

## Build and environment notes

`master` and the v2.4.0 tag were cloned with `--recursive` and built with
`cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++` + `make -j4` (gcc 13.3, cmake
3.28, OpenMP, default vectorisation), which is the CI recipe minus `-DIQTREE_FLAGS=static`.
Three things the environment lacked, none of which touches IQ-TREE's sources: Eigen 3.4.0
(cloned from GitLab, passed as `-DEIGEN3_INCLUDE_DIR`), Boost 1.86 headers (the release
tarball from GitHub, `-DBoost_INCLUDE_DIR`; IQ-TREE uses one header, for the symmetry
test's binomial), and googletest at the commit the `cmaple` submodule pins (the
`github.com/.../archive` zip is blocked by the proxy; cloned by git and passed as
`-DFETCHCONTENT_SOURCE_DIR_GOOGLETEST`). The binary reports "IQ-TREE multicore version
2.4.0 for Linux x86 64-bit". iqtree3 `master` (version string 3.1.3) was built the same way to execute the notes on the
current development line (`verify/*.v3.out`): IQ1–IQ4 reproduce there with the same numbers
(parametric aLRT 0.78; one-site UFBoot 100 % vs `-b` 61 %; thread dependence; rooted-tree `NA`
and `__root__` abort), and the branch-test, UFBoot and concordance harnesses pass. No R, no Europe PMC, no NCBI, no
`github.com` HTML; 1.6.12 was read (Cibiv/IQ-TREE tag), not built, because nothing rose to
a confirmed defect.

## Filing channel (read before anything is sent)

- `iqtree/iqtree2` has **no `CONTRIBUTING.md`, no issue or PR templates** (`.github/`
  holds `FUNDING.yml` and the build workflow) and a Contributor Covenant
  `CODE_OF_CONDUCT.md`. `README.md` "User support": questions and feedback to GitHub
  Discussions, "feature requests bug reports" to GitHub Issues. `iqtree/iqtree3` (the
  active repository since 2025; its README still points at the iqtree2 Issues/Discussions
  URLs) is the same.
- The manual (`iqtree/iqtree.github.io`, `doc/Frequently-Asked-Questions.md:52-62`) still
  names the **IQ-TREE Google group** (`groups.google.com/d/forum/iqtree`) for questions,
  feature requests and bug reports, and `doc/Home.md:93` sends questions to
  `github.com/iqtree/iqtree3/discussions`. Three channels, then; the code repository's
  own README is the most recent statement: **Issues for bugs, Discussions for
  everything else**.
- Tests: `test_scripts/` is a job generator for the maintainers' cluster
  (`gen_test_standard.py`, `submit_jobs.sh`, alignments in `test_data/`), and `cmaple/`
  carries googletest unit tests; there is no `ctest` target for IQ-TREE itself. There is no
  changelog file in the repository; release notes live on the GitHub releases page.
- None of IQ1–IQ4 is a code defect that changes a published number on realistic data, so
  **none warrants an Issue in the repository's sense**. IQ1 and IQ4 are documentation gaps
  (the manual is a separate repository, `iqtree/iqtree.github.io`); IQ3 has a closed issue
  (#228); IQ2 is a design question for a Discussion. The kit in [`upstream/`](upstream/)
  holds two `git am`-able documentation patches for the manual repository (IQ1, IQ4), a
  Discussion draft for IQ2 with the reproduction, and a note on IQ3 relative to #228.
  Nothing has been filed.

## Files

| file | what |
|---|---|
| `iqtree_profile.py`, `iqtree_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/statistical-core.md` | the review: IQ1–IQ5, held-up list, design notes, not-checked list |
| `verify/iqt.py` | shared helpers: binary runner, numpy pruning likelihood, scipy discrete gamma, simulator, Newick/split utilities |
| `verify/heldup_likelihood_closed_form.py` (+ `.out`, `.v2.4.0.out`) | JC / +G mean & median / +I / +I+G / GTR+F / +ASC log-likelihoods and category rates vs reference; `+ASC` refusal |
| `verify/heldup_information_criteria.py` (+ `.out`, `.v2.4.0.out`) | parameter counts and AIC/AICc/BIC arithmetic: full model, 92 ModelFinder rows, `-p`/`-q`/`-Q`, `-m MFP -p` |
| `verify/heldup_branch_tests.py` (+ `.out`, `.v2.4.0.out`, `.v3.out`) | aBayes, parametric aLRT (port of the PhyML table; IQ1), SH-aLRT vs RELL port on a 4-taxon JC design |
| `verify/heldup_ufboot.py` (+ `.out`, `.v2.4.0.out`, `.v3.out`) | seed reproducibility, thread dependence (IQ3), support = `.ufboot` split frequency, `--bnni`, correlation |
| `verify/heldup_concordance_factors.py` (+ `.out`, `.v2.4.0.out`, `.v3.out`) | sCF exact / exhaustive / per-quartet, gCF exact; rooted-tree behaviour (IQ4) |
| `verify/note_degenerate_alignments.py` (+ `.out`, `.v2.4.0.out`, `.v3.out`) | one-site UFBoot 100 % vs `-b` 61 % with the cutoff mechanism (IQ2); all-constant input; duplicate sequences |
| `verify/note_ufboot_single_site.py`, `verify/note_ufboot_star_tree.py` (+ `.out`, `.v2.4.0.out`) | IQ2 scope: 6-taxon few-site branches and 4–6-taxon star trees, UFBoot vs `-b` |
| `upstream/` | filing kit: channel notes, two manual patches (IQ1, IQ4), Discussion draft (IQ2), #228 note (IQ3) |

Harnesses need a built binary: `IQTREE2=<path to iqtree2 or iqtree3 binary>
IQTREE_RUNDIR=<scratch dir> python3 verify/<harness>.py` (numpy, scipy).

## Next steps

1. Decide with the lead whether the two manual patches (IQ1, IQ4) go to
   `iqtree/iqtree.github.io` as PRs and whether IQ2 is worth a Discussion; nothing else
   is worth the maintainers' time.
2. Extend to the tree-search candidate set and the AU test (`-zb`), the two remaining
   paths cohort papers rely on; and `--scfl` in iqtree3, which 2.2.2+ users are pointed to.
3. Full-text profiling rerun when Europe PMC is reachable (gCF/sCF and `-alrt 0` usage
   are invisible in the cache).
