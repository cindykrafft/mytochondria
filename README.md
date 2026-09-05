# Mytochondria

*"It's the powerhouse of the cell." This one's mine.*

Maintainers of research software are short on time, not on care. Mytochondria spends
machine time on the part of their job that scales worst: reading the numerical core of a
package line by line, reproducing every suspicion by execution, and turning what survives
into a patch with a test that fails without it. What reaches a maintainer should be
something they can merge or decline in a few minutes, not another report to triage.

Research software is unusually hard code: mathematically intricate, evolving alongside
the science it serves, maintained for decades, and usually built by small teams under
tight grant budgets. The packages read here are careful, well-engineered work. The premise
is not that anyone was careless — it is that no team can read an entire codebase at the
depth every line deserves, and that patient machine-assisted reading is a genuine
complement to human testing. Nothing here carries any authority: every finding is an
offer, the maintainers decide, and a "no" is a complete answer.

## How it works

**1. Survey.** Harvest five years of research articles from six high-impact journals
(*Nature*, *Science*, PNAS, *NEJM*, *The Lancet*, *Cell*) via the Europe PMC API, parse
every openly readable full text, and extract which open-source packages each paper used,
with a quotable evidence sentence and version where stated. Papers that could not be
read are listed individually rather than silently dropped.

**2. Target.** For a package being read, re-mine the papers that used it to determine
*which parts* they ran — commands, options, versions — so review effort lands on the
code paths that carry published numbers.

**3. Read and verify.** Read those components adversarially, then verify: compile the
routine under test verbatim against high-precision arithmetic, port it faithfully to
Python and test against ground truth, or simulate the full pipeline. Only then does a
finding get written up, with file:line evidence, a runnable harness, and a patch where
the fix is crisp.

**4. File upstream, on the project's terms.** Before anything is sent, read the
project's `CONTRIBUTING.md`, any pinned policy issue, the NEWS/changelog, and the
existing issue and PR history for the component. A finding that upstream has already
fixed and announced is not a finding to file. Non-minor changes, and anything that
changes numerical output, go to the project's preferred discussion venue first
(for Bioconductor packages that is the support site, not a cold PR). Each filing kit
records which documents were read and where the ask is being made. This step was
added after the DESeq2 round, where the project filed four items without reading the
project's pinned policy or CONTRIBUTING.md, claimed a NEWS entry was missing when it
was not, and had all four closed by the maintainer within two hours.

**5. File sparingly; hold the rest.** Volume from one account is what reads as a
campaign to maintainers, not any single report. File now only a finding that changes a
number that ends up in a paper, under default or common settings, on the current
release. Crashes, rare-option paths, API-only paths, documentation drift and design
questions are held in the filing kit. At most two filings per repository until a
maintainer responds; after a positive signal, the held items for that repository follow
one at a time. A comment on an issue the maintainers already keep open is a separate,
low-cost category and does not count against the cap. Every prepared finding carries
its tier in [`audits/TRIAGE.md`](audits/TRIAGE.md).

Some maintainers have said they do not want AI-generated contributions. That is their
call and it is final for this project: the fork of their repository under
`github.com/cindykrafft` gets the topic **`upstream-declines-ai-contributions`**, and from
then on nothing is filed, commented, re-opened or pushed for that repository, held items
included. Open filings are left to the maintainers to close as they see fit; the project
stays published here, with the outcome recorded in its README and in the status ledger.
Before preparing or opening anything, check the fork's topics; the ledger's
[`site/audits.json`](site/audits.json) and the filing console read the same topic. This step was added after the first
week of filings put seven FieldTrip PRs up in two days and a reviewer's reply read as
"fine, but minor".

**6. Answer what the project already knows.** These reading passes kept finding bugs that users
had already reported and nobody had claimed (deepTools #1108 and #1118, BEDTools #1142,
fastp #474 and #518 among them), and a patch on a thread the maintainers keep open is the
lowest-friction contribution there is. So the project now alternates: for each repository
already checked, read its open issues, pick one reproducible bug with a wrong-number or
crash consequence and no existing PR, reproduce it on master by execution, fix it with a
test that fails before and passes after, run the project's own tests and linter, and file
the PR against the issue. Everything is recorded under `audits/<package>/issue-fixes/`,
one directory per issue, with the reproduction, outputs, patch, PR body and the other
candidates considered. The same limits apply: nothing for a repository that declines
AI-generated contributions, and no new PR while the repository has an unanswered one from
this project, unless it answers the maintainers' own issue. An issue with an assignee is
someone's claimed work: no PR on it; a verified diagnosis goes on the thread as a comment
with a link to the branch, and the assignee decides. The project method from steps 1
to 5 resumes once the open-issue backlog of the checked repositories is worked down.

What *held up* under the same scrutiny is recorded alongside what didn't, so findings
are read in proportion.

## Status

A live ledger of every filing and its state on GitHub, refreshed four times a day: https://cindykrafft.github.io/mytochondria/ (built from [`site/`](site/) by the `Status page` workflow).

Filing follows step 5 above; the per-finding tiers are in [`audits/TRIAGE.md`](audits/TRIAGE.md).

| Package | Papers exposed | Findings | Upstream |
|---|---|---|---|
| [FreeSurfer](audits/freesurfer/) | 116 | 16, three reproduced numerically | 5 fix PRs + 9 issues filed on GitHub |
| [FSL](audits/fsl/) | 114 | 12, six with patches | reports and patches ready; filing via the FSL mailing list |
| [SPM](audits/spm/) | full-codebase audit (not survey-driven) | 83 confirmed + ~38 plausible; three verified by executing the code (one unit-tested, two reproduced on SPM's tutorial data). [Reanalysis](audits/spm/reproductions/erpcore_realdata/) of the merged artefact-window fix on ERP CORE (39 participants): on response-locked epochs the shipped code discarded 97 % of detected artefact windows, kept 98 % of trials where the fix keeps 49 %, and the group ERN changed from −10.4 to −8.3 µV (paired p = 0.003) | 2 fix PRs merged upstream (M/EEG artefact-window baseline; downsample sampling rate); 3 issue+PR pairs open (χ² EC densities with new unit test; DCM free energy; parametric-modulation padding, filed 2026-09-02) |
| [AFNI](audits/afni/) | 39 in the survey cohort; 57 adjudicated for the ReHo finding | 36 (9 high-impact, 15 narrower, 12 likely), one reproduced numerically | 12 PRs + 14 issues filed on GitHub: 4 PRs merged (ReHo tie handling, NIfTI slice timing, two test-suite repairs), 8 open. [Reanalysis](audits/afni/reanalysis/) of the published ReHo design on open data (ds000030, 40 subjects): the pre-fix build returns NaN in 17 % of brain voxels and a third of the correct value elsewhere, and the SCZ-vs-control p < .001 maps from the two builds do not overlap |
| [DESeq2](audits/deseq2/) | 886 | 3 confirmed (one live 2017–2025, fixed upstream in 1.49.4 with a NEWS entry), 3 verified-negligible | 3 issues + 1 PR filed on GitHub 2026-09-01; all four closed by the maintainer the same day (the two NEWS requests were already met, the PR was declined under the project's results-stability policy). The filing skipped DESeq2's contribution guidelines and misread its NEWS; see the [filing kit](audits/deseq2/upstream/) for the correction |
| [MACS2](audits/macs2/) | 475 | 3 confirmed (one live in current MACS3, reproduced on shipped binary), 4 notes, 2 withdrawn by own review | not yet filed. MACS has a CONTRIBUTING.md with a PR template and a Slack channel; read both before filing (step 4 above) |
| [Kilosort](audits/kilosort/) | 60 | 3 new verified on shipped code (one disables KS4's refractory split veto since v4.1.5), 5 by code reading, plus exposure map for the known 2024 "spike holes" bug | 2 fix PRs + 3 issues filed on GitHub 2026-09-01 (#1043–#1047), all open, no maintainer response yet |
| [FieldTrip](audits/fieldtrip/) | 42 | 4 verified by executing FieldTrip's own code under Octave (permutation p-values exclude ties, p = 0 with exhaustive permutations; correlationT df; PSI edge bins −Inf; a statfun branch that cannot run) + 1 by code reading | 5 fix PRs + 2 issues filed on GitHub 2026-09-01/02 (#2607–#2613), all open; the two behavior-changing PRs carry new `test_pullNNNN.m` scripts as the project's bot requested |
| [Suite2p](audits/suite2p/) | 32 | 2 verified on the shipped 1.1.0 wheel (bidirectional-phase correction corrupts odd scan lines since v1.0; classifier bins values at the training minimum into the top bin) + 1 limit verified, 2 by code reading | 3 fix PRs + 3 issues filed on GitHub 2026-09-02 (#1265–#1270), all open, no maintainer response yet |
| [Seurat](audits/seurat/) | 767 | review 1 (differential expression) done: 1 confirmed undocumented behaviour change (v5 fold-change formula, pseudocount `1/n` per group — 79–88 % of lowest-expressed null genes in small clusters reported above +0.25; p-values unaffected), 5 notes, Wilcoxon/MAST paths held up. Profiling from the survey cache only (Europe PMC unreachable; full-text rerun pending) | filing channel read; upstream issue #9346 already raised the asymmetry and was closed — its reply must be read before filing; nothing filed |
| [Scanpy](audits/scanpy/) | 200 | 2 confirmed on master by executing the shipped code (t-test silently run on exponentiated values when `mean_in_log_space=False`, on main and the 1.13 pre-releases, not in 1.12.4; `score_genes` top expression bin holds 1–12 genes so lists with the most-expressed genes get almost no controls or error, all versions), 3 notes; Wilcoxon/HVG/scale/normalize paths held up | issue #4336 + PR #4337 (t-test, from the [fork](https://github.com/cindykrafft/scanpy)) filed 2026-09-02, open, release-note fragment renamed to the PR number; the `score_genes` PR waits on regenerating the `paul15` reference pickle; [filing kit](audits/scanpy/upstream/) |
| [Scrublet](audits/scrublet/) | 78 name Scrublet of 179 in the survey's doublet-tool group (lower bounds) | 4 confirmed by executing the shipped code — two in Scanpy's port (`sc.pp.scrublet` scores every cell over `k_adj − 1` neighbours instead of `k_adj`, with the variant chosen by whether any two points coincide; `log_transform=True` transforms observed and simulated cells on different scales — both on `main` and 1.12.4) and two in the original (UMI-subsampled synthetic-doublet totals inflated by rate·(1−rate)·F; `mean_center=True, normalize_variance=False` crashes on scikit-learn ≥ 1.4 — master = PyPI 0.2.3, non-default options), 4 notes, 4 withdrawn; the default original pipeline equals an independent port bit for bit; the two packages' calls agree (Jaccard 0.986) while their scores do not (Spearman 0.43, 0.996 once given the same simulated doublets) | not yet filed. Scrublet has no CONTRIBUTING/templates/tests and no maintainer activity since 2020 (plain issues + patches with new pytest files ready); Scanpy kit follows its bug-report template, Ruff and towncrier conventions, two patches with tests that fail on `main`; see the [filing kit](audits/scrublet/upstream/) |
| [CellPhoneDB](audits/cellphonedb/) | 46 | 6 confirmed by executing the shipped code (permutation workers draw duplicate shuffles, so `iterations` is effectively divided by `threads` — 279 distinct permutations of 1,000 at the default 4; p-values count only shuffles strictly greater than the observed mean, so ties are dropped and p = 0 is reported for 42.6 % of tested entries on the project's own example data, verified against an exhaustive 1,680-permutation null and on every release v2.1.7–5.0.1; `threshold` inert in METHOD 1; deconvoluted.txt reports the complex minimum on every subunit row; `ZeroDivisionError` at `threads=1, iterations<=50`; scoring broken on pandas 3), 6 notes; cluster means, complex minima, threshold rule, p-value counting, significant_means, microenvs, DEG method and the v5 scoring protocol held up | filing channel read (no CONTRIBUTING, no templates, no changelog convention); issue #231 (duplicate permutations across workers) filed 2026-09-03, open; the other five wait for a maintainer signal, and the replies on #179/#60 must be read before filing CPDB2; [filing kit](audits/cellphonedb/upstream/) with 2 tested patches on the [fork](https://github.com/cindykrafft/CellphoneDB) |
| [umap-learn](audits/umap/) | 1,111 (largest exposure in the survey; 627 also name Seurat, 171 Scanpy) | 1 confirmed on master, 0.5.12 and 0.5.3 by executing the shipped code (`smooth_knn_dist` returns sigma = inf for every point with a neighbour pruned by `disconnection_distance`, so all its remaining edges get membership 1.0; fires on the exact, pynndescent and precomputed paths and, with the default settings, for `metric="jaccard"` on sparse binary data), 2 notes (duplicate rows collapse sigma to the floor; `transform` builds a different local graph than `fit`), 2 withdrawn (`random_state` vs `n_jobs`, issue #1080 is stale on master; sparse vs dense metrics); sigma/rho vs the paper's equation, symmetrisation, `find_ab_params`, spectral init, sparse vs dense metrics and `random_state` across `n_jobs` held up | filing channel read (CONTRIBUTING only, no templates); issue #1286 + PR #1287 (from the [fork](https://github.com/cindykrafft/umap)) filed 2026-09-03, open, no maintainer response yet; [filing kit](audits/umap/upstream/) |
| [Cutadapt](audits/cutadapt/) | 331 | 4 confirmed by executing the shipped code on main, 5.2 and older wheels (`-e N` loses one allowed error for adapter lengths 49, 98, … through floating-point rounding of N/len, all versions since 3.0; `--max-ee`/`--max-aer` ignore `--quality-base`, so Phred+64 data are never filtered; the demultiplexing index ranks barcodes by matching bases while `--no-index` ranks by the documented alignment score, since 5.0; the k-mer prefilter added in 4.3 silently drops ~40 % of reads carrying an anchored/non-internal adapter with one inserted base whenever exactly one error is allowed), 4 notes, 4 own suspicions withdrawn; quality trimming, expected errors, filters, pair-filter, interleaved/multi-core and the aligner invariants held up against independent ports on ~100k random cases | filing channel read (CONTRIBUTING, bug-report template, CHANGES.rst convention); no prior issue for any of the four; issue #892 + PR #893 (`-e N` rounding, from the [fork](https://github.com/cindykrafft/cutadapt)) filed 2026-09-03, open, no maintainer response yet; the other three patches wait for a maintainer signal; [filing kit](audits/cutadapt/upstream/) |
| [deepTools](audits/deeptools/) | 167 | 9 confirmed by executing the shipped code on `master` (= 3.5.6), 3.5.1 and 3.3.1 (`bamCompare --skipZeroOverZero` shifts every bin after a skipped one — open upstream as #1108/#1130 since 2021; `plotPCA --log2` inert and `--rowCenter` inert at the default `--ntop`; `--removeOutliers` scales by the median instead of the MAD and removes nothing; `--MNase` counts four bases for odd fragments — open as #1118; BPM ≡ CPM against its documented definition; `--smoothLength` truncated at chunk edges; `--ignoreDuplicates` alone left out of the CPM/RPKM/RPGC and readCount denominators, 40 % low on a 40 %-duplicate sample; multiBigwigSummary reports zoom-level summaries, median 3.4 % and up to 245 % off at the default 10-kb bins; plotFingerprint over-counts a fragment's last bin when the sampling step equals the bin size), 11 notes, 2 withdrawn; bamCoverage/bamCompare arithmetic, computeMatrix binning, the profile/heatmap summaries, multiBamSummary, plotCorrelation, plotPCA default, bamPEFragmentSize, the fingerprint metrics and the coverage/filtering/enrichment counts held up against numpy/scipy and independent ports | filing channel read (markdown issue/PR checklists, flake8 + pytest CI, no changelog rule); two findings already open upstream unanswered, seven new; [filing kit](audits/deeptools/upstream/) with 9 issue/comment texts, MCVEs run on 3.5.6 and 3.3.1, and 7 `git am`-able patches whose new tests fail on unmodified `master`; nothing filed |
| [IQ-TREE 2](audits/iqtree/) | 258 | 0 wrong numbers on master; 4 notes verified by executing the built binary (parametric aLRT prints the cube of 1 − p; UFBoot's 1-log-likelihood candidate cutoff gives 100 % where the standard bootstrap gives 61 % on a degenerate 4-taxon alignment, not reproduced on 6 taxa; SH-aLRT/UFBoot vary with thread count at fixed seed; rooted trees get `NA`/abort in gCF/sCF), 1 withdrawn; likelihoods, gamma rates, `+I`/`+ASC`, ModelFinder criteria and parameter counts, UFBoot/`--bnni` supports, SH-aLRT, aBayes, gCF/sCF held up on master and v2.4.0; the four notes reproduce on iqtree3 3.1.3 | filing channel read (Issues for bugs, Discussions otherwise; no CONTRIBUTING or templates; development moved to `iqtree/iqtree3`); nothing rises to an Issue; [kit](audits/iqtree/upstream/) holds two manual patches and a Discussion draft, none filed |
| [fastp](audits/fastp/) | 117 | 3 confirmed by executing the built binary (`--cut_front`/`--cut_tail` with `--trim_front1`/`--trim_tail1` drop `cut_window_size − 1` extra bases from every read — 52 nt of a 60 nt all-Q40 read instead of 55 — on every release built, 0.20.0 through 1.3.6 and master; an auto-detected built-in adapter longer than 60 nt is printed and then emptied by `resize(0, 60)`, so 0 of 20,000 reads are trimmed and the JSON loses its `adapter_cutting` section, on 0.26.0 through master, hitting the 85 built-ins with no shorter prefix, i.e. the TruSeq Small RNA primers; the one-indel adapter search passes the read start instead of `rdata + pos`, so an adapter with an indel at the 3' end is never trimmed, 0 of 200 reads), 7 notes (overlap mismatch limits apply to the first 50 overlap bases only; insert-size histogram counted by thread 0 only; `--overlap_len_require`/`--poly_g_min_len` off by one; `-m` silently enables `-c`), 5 withdrawn; filters, `filtering_result`, Q20/Q30/GC/mean length, the k-mer table, poly-G/poly-X, base correction, UMI, `--split`, `--reads_to_process` and the duplication estimator held up against independent ports on 10^4–10^5 reads | filing channel read (no CONTRIBUTING, no templates, no changelog; `./fastp test` and `scripts/*.sh` are the test conventions); two of the three already have open upstream issues (#474, #518) so their texts are drafted as comments there, the third is a new issue; [filing kit](audits/fastp/upstream/) with three `git am`-able patches (fix + test, each new test failing on unmodified master); nothing filed, nothing pushed |
| [BEDTools](audits/bedtools/) | 302 | 5 confirmed by executing the built binary on `master` (= 614e9a5), v2.31.1 and v2.30.0 (`coverage -split` counts overlapping blocks, not database records, and ignores `-f`/`-F` — wrong count since #673 in 2018; `intersect -split` tests `-F`/`-r` against the summed block length of all hits and clears the whole group, 530 false negatives + 48 false positives in 838 pairs — open upstream as #1142; `closest -t first`/`last` break a left/right tie by `-D` stream order not B-file order, 1027/2000 reverse-strand queries under `-D a`; `reldist`/`subtract`/`flank`/`closest -d` truncate 64-bit coordinates to 32-bit int on chromosomes > 2.15 Gb, dropping queries or emitting negative coordinates; `slop -pct`/`flank -pct` lose one base at 12 of 99 whole-percent values and absolute slop rounds above 2^24), 1 note (`shuffle -incl` lets features spill past the include interval — #1089) + 8 minor notes; the whole intersect/coverage/subtract/window/merge/cluster/map/groupby matrix, closest/genomecov (BED+BAM)/multicov, fisher (vs `scipy.stats.fisher_exact`), jaccard, reldist, nuc and shuffle/random uniformity held up against independent Python ports | filing channel read (no CONTRIBUTING/templates/linter; CI is `make test`; `docs/content/history.rst` is the changelog); BT2 matches open #1142, BT1 relates to open #673, three findings new; [filing kit](audits/bedtools/upstream/) with 3 `git am`-able patches (fix + tests failing on unmodified master, full suite passing) + 5 issue/comment texts + MCVEs; nothing filed |
| [HTSeq](audits/htseq/) | 161 | 2 confirmed by executing the shipped code on `main`, the 2.1.2 wheel and the 0.11.2, 0.12.4 and 0.13.5 sdists (`htseq-count` compares the MAPQ field of an *unmapped* mate record, 0 by aligner convention, with `-a`, so every pair whose mate is unmapped but present in the BAM goes to `__too_low_aQual` under the default `-a 10` while the same pair counts when the record is absent, contrary to the FAQ — 113 of 113 such pairs lost on a 2,000-pair synthetic library, all versions; `BAM_Reader[iv]` calls pysam `fetch` with `iv.start + 1` and misses alignments whose last base is `iv.start`, API only, all versions), 6 notes (`--nonunique fraction` divides by overlapping features not by NH, so with `--secondary-alignments score` the documented "sum equals the number of reads" fails; `htseq-count-barcodes` lets `__no_feature`/`__alignment_not_unique`/`__too_low_aQual` reads outvote a gene inside a UMI; docs say `--secondary/--supplementary-alignments` default to `score` but the code defaults to `ignore` since 0.10.0; a pair with a mate on a chromosome absent from the GTF is `__no_feature` as a whole; zero-length `GenomicInterval.overlaps` asymmetric; float32 count matrices), 1 withdrawn; the three overlap modes, all `--nonunique` modes, strandedness, `-r name`/`-r pos` pairing, NH/secondary/supplementary handling and the GenomicArrayOfSets/StepVector arithmetic equal an independent per-base port on all 324 single-end and paired-end configurations once HC2 is modelled, and the documentation figure's eight rows reproduce exactly | filing channel read (markdown bug-report template, no CONTRIBUTING/PR template/linter; `doc/history.rst` is the changelog); no prior issue for either (nearest #99, #94, #96); [filing kit](audits/htseq/upstream/) with two `git am`-able patches (fix + test failing on `main` + history entry) ready; nothing filed | issue #109 + PR #110 filed 2026-09-03 and closed by the maintainer the same day; the project declines AI-generated contributions, so nothing further is filed (HC1 held); fork tagged `upstream-declines-ai-contributions` |
| [PLINK](audits/plink/) | 184 (84 name a 1.9 build, 13 name 2.0) | 1 confirmed by executing the built binaries on `master`, the `v1.9.0-b.7.12` tag (2026-09-01), `v1.90b6.21` and `v1.90b4` (PLINK 1.9 `--hwe`/`--hwe midp` removes variants with 2 or 3 heterozygotes whose exact HWE p is *above* the threshold — `SNPHWE_t` never compares the last element of the observed tail, so the filter tests p − P(hets − 2) < t; every one of 9,798 two-het tables with n ≤ 200 flips below its p, by up to 5 % of p; `--hardy` prints the right p; plink2 unaffected), 5 notes (one open: plink2 `--score center` with imputed dosages differs from 1.9 and the reference by up to 6.5e-2, cause not traced), 3 own suspicions withdrawn; HWE and Fisher exact p on all tables with n ≤ 60 / N ≤ 40 to 1e-15, `--hardy`, `--freq`, `--missing`, `--assoc`/`--model`/`--logistic`/`--linear`/`--glm`, all `--adjust` columns, `--r2`/`--ld`, `--genome`, KING, `--score` held up against exact arithmetic, scipy/statsmodels and independent ports | filing channel read (no CONTRIBUTING/templates/changelog; 1.9 has no unit-test runner); no prior issue (nearest #128); [filing kit](audits/plink/upstream/) with issue text, MCVE run on four 1.9 builds, and a 28-line `git am`-able patch that brings the exhaustive count from 19,399 to 0; nothing filed | issue #380 + PR #381 filed 2026-09-03; the maintainer closed the PR and committed the same fix himself the same morning (`1fe42e5`), verified by rerunning the exhaustive harness at that commit: 0 tables wrongly removed |

The survey itself covers **44,198 research articles**, of which **20,501** were openly
readable; **10,364** name at least one open-source package, across **270 distinct
packages**. Coverage is very uneven by journal (PNAS 78%, *Science* 5%) — see
[`survey/README.md`](survey/README.md) for the caveats that come with that, which matter
for any count in this repository.

## Layout

```
survey/
  README.md      the survey document: headline numbers, per-journal coverage,
                 most-used packages, and the caveats
  data/          papers.tsv, paper_software.tsv (36,424 usage records),
                 package_index.tsv, gap_list.tsv (23,697 unreadable papers),
                 pipelines.jsonl.gz
  packages/      one page per detected package (270), with evidence sentences
  scripts/       harvest + extraction pipeline (reproducible end to end)

audits/
  freesurfer/    component reviews, paper→feature exposure, numerical
                 reproductions, and the upstream filing kit
  fsl/           component reviews and paper→feature exposure
                 (reports, patches and harnesses: separate repo, below)
  spm/           eleven component reviews spanning the whole codebase,
                 verification harnesses incl. an Octave old-vs-new
                 regression, and the upstream filing kit
  afni/          nine subsystem reviews, paper→feature exposure, the ReHo
                 tie-handling reproduction, and the upstream filing queue

preprint/        LaTeX source, figures and compiled PDF of the AFNI paper
                 (method + the ReHo reanalysis on ds000030)
preprint-spm/    LaTeX source, figure and compiled PDF of the SPM companion
                 paper (the 83 findings, the five upstream fixes, the two
                 merged ones measured on SPM's MMN tutorial data)
```

## Related repositories

- **[fsl-bug-reports](https://github.com/cindykrafft/fsl-bug-reports)** — the FSL
  findings as ready-to-send reports, `git format-patch` fixes, and verification
  harnesses. Kept separate because FSL takes reports on its mailing list, and those
  posts link to it directly.
- **[cindykrafft/freesurfer](https://github.com/cindykrafft/freesurfer)** — fork
  carrying the five FreeSurfer fix branches submitted upstream.
- **[cindykrafft/spm](https://github.com/cindykrafft/spm)** — fork carrying the five
  SPM fix branches plus a new `tests/test_spm_ECdensity.m` (two merged, three open upstream).
- **[cindykrafft/scanpy](https://github.com/cindykrafft/scanpy)** — fork carrying the two
  Scanpy fix branches (t-test input scale, opened as PR #4337; `score_genes` bins, PR pending
  the reference-pickle regeneration) and the two Scrublet-port branches, each with a test and
  a release-note fragment.
- **[cindykrafft/cutadapt](https://github.com/cindykrafft/cutadapt)**,
  **[cindykrafft/umap](https://github.com/cindykrafft/umap)**,
  **[cindykrafft/CellphoneDB](https://github.com/cindykrafft/CellphoneDB)** — forks carrying
  the fix branches from those passes (one PR each opened 2026-09-03: cutadapt #893, umap #1287;
  CellPhoneDB has an issue, #231, and two branches held).

## Reading these findings fairly

- A finding is **code-level** unless it says otherwise. "CONFIRMED" means the defect was
  traced end to end in the source and, where stated, verified numerically — not that
  anyone has run the shipped binary on imaging data and watched it happen.
- **"Paper is exposed" means the paper used the affected feature or version.** It does
  not mean its conclusions are wrong. Most of these biases are systematic and shared
  across subjects, which is exactly why they usually shift or attenuate measurements
  rather than reverse well-powered contrasts.
- Reproduction sometimes *shrinks* a finding, and that is recorded too — one FreeSurfer
  finding turned out not to fire on the standard pipeline at all once measured, and a
  faithful port of AFNI's ReHo tie loop moved one published paper back out of the
  exposed set.
- Upstream maintainers' reading wins. Where they have adjudicated, the outcome is
  recorded next to the finding: SPM and AFNI have merged fixes and left others open;
  DESeq2's maintainer closed all four filings, and on the central factual point (whether
  the weights fix had been announced) he was right and this project was wrong.

## Reproducing the survey

`survey/scripts/` runs the whole pipeline against the public Europe PMC API — metadata
harvest by ISSN, full-text fetch, then extraction. It needs no credentials. Expect the
fetch stage to take many hours and to hit articles that are marked open access but serve
no XML; those are routed to the gap list rather than retried indefinitely.

## License

Scripts are MIT (see `LICENSE`). The prose, tables and derived data are CC BY 4.0.
Evidence sentences are short quotations from the source articles, each attributed by PMID
and DOI; the underlying articles remain under their own licenses. No third-party source
code is redistributed here — patches and harnesses only.
