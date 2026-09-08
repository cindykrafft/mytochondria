# Filing triage (from 2026-09-03)

After the first week of filings (SPM, FieldTrip, Kilosort, Suite2p, DESeq2, then Scanpy,
Cutadapt, umap-learn and CellPhoneDB), the volume per repository, not any single report,
is what risks reading as a campaign to maintainers. From here on:

**Rule.** File now only a finding that changes a number that ends up in a paper, under
default or common settings, on the current release. Crashes, rare-option paths, API-only
paths, documentation drift and design questions are held. At most two filings per
repository until a maintainer responds; after a positive signal, the held items for that
repository follow one at a time. A comment on an issue the maintainers already keep open
is a separate, low-cost category and is not counted against the cap.

**Read the whole thread first (from 2026-09-08).** No comment on an existing issue or PR, and
no issue that cites a prior thread, is drafted before every comment on that thread (and on the
threads it links to) has been read in full. Comment counts and titles are not enough: a thread
with six replies may already carry the diagnosis, the fix, or the maintainer's decision, and a
draft written from the opener alone repeats or contradicts it. Comment bodies on repositories
this project does not own cannot be read from the audit session; a helper session started on the
upstream repository exports them verbatim to the "FieldTrip Threads" artifact
(`site/console/WATCH.md`, "Reading a thread"), and the kit's `README.md` records the date the
thread was read and what it already contained. The same applies before replying on our own
filings.

**Declined repositories.** A fork carrying the topic `upstream-declines-ai-contributions`
means the maintainers do not take AI-generated contributions. Nothing further goes to that
repository: no issue, no comment, no PR, no follow-up on open items. Its held findings stay
in the kit indefinitely.

**Grades of everything prepared and unfiled** (kits under `audits/<package>/upstream/`):

| tier | finding | reason |
|---|---|---|
| file now | HTSeq HC2 | default `-a 10` discards every pair whose mate is unmapped but present, as HISAT2/BWA/Bowtie2 write them; all versions |
| file now | deepTools DT7 | `--ignoreDuplicates` alone is left out of the CPM/RPKM/RPGC/BPM denominator |
| file now | deepTools DT8 | `multiBigwigSummary` reports zoom-level summaries at the default bin size; replicate correlations move |
| file now | PLINK PL1 | 1.9 `--hwe` removes 2- and 3-heterozygote variants whose printed p is above the threshold; most-cited build affected |
| file now | fastp FP2 | 85 built-in adapters longer than 60 nt are auto-detected and then discarded, so nothing is trimmed |
| file now | BEDTools BT1 | `coverage -split` counts blocks, not records, and ignores `-f`/`-F` |
| file now | CellPhoneDB CPDB2 | strict inequality drops ties, p = 0 for 42.6 % of tested entries; **read the replies on #179 and #60 first** |
| comment | deepTools DT1 (#1108/#1130); DT4 posted 2026-09-08 as a comment on #1118 with PR #1466; fastp FP1 (#474), FP3 (#518) | cause and patch on threads the maintainers keep open; BEDTools BT2 posted 2026-09-05 as a comment on #1142 with PR #1144 |
| filed | Cutadapt CA1 (#892/#893), umap-learn U1 (#1286/#1287), CellPhoneDB CPDB1 (#231), Scanpy SC1 (#4336/#4337) | 2026-09-02/03; umap #1287 merged 2026-09-05, the rest open |
| held | HTSeq HC1 | API path (`BAM_Reader[iv]`), not `htseq-count` |
| held | deepTools DT2, DT3, DT5, DT6, DT9 | plot options, an outlier heuristic, docs-vs-code (BPM), a small edge effect, a latent path |
| held | BEDTools BT3, BT4, BT5 | tie order under one flag; chromosomes over 2.1 Gb; one base at some `-pct` values |
| held | Cutadapt CA2, CA3, CA4 | Phred+64 data only; demultiplexing rank under an index; CA4 is on the line (40 % of anchored-adapter reads with one insertion, but only at exactly one allowed error) and follows once #893 has a reply |
| held | Scrublet-in-Scanpy SR1, SR3; original Scrublet | `k_adj − 1` neighbours and the `log_transform` order are subtle; the original repository is unmaintained |
| held | CellPhoneDB CPDB3–CPDB6 | inert `threshold`, subunit-row minima, a crash at `threads=1, iterations<=50`, pandas 3 breakage |
| held | IQ-TREE IQ2 | design question for Discussions, no wrong number |
| held | FieldTrip, Suite2p, Kilosort, MACS2 items not yet filed | those repositories already have several open filings from this project |

The console (`scratchpad/console2`, published as the Audit Filing Console) groups each
repository's cards by these tiers, with the held ones collapsed.

## Catch-up, 2026-09-03 evening: every repository filed against, and the next action

Sources: GitHub search for everything filed by the project account (45 issues, 38 PRs
outside the project's own repositories), the upstream git logs, and a scan of every
repository's contribution documents for an AI-contribution policy (none of the 19 has a
written one; HTSeq's decision was made in the thread). Comment threads on other people's
repositories cannot be read from the project session, so "unread" below means the user has to
read them.

| repository | filed | state | next action |
|---|---|---|---|
| afni/afni | 12 PRs, 14 issues | 4 PRs merged, 4 issues resolved; 8 PRs + 10 issues open; PR #960 has one unread comment (2026-09-02) | read #960 and act on it; **no new filings** (the open backlog is already far over the cap) |
| freesurfer/freesurfer | 5 PRs, 9 issues | 2026-09-08 01:00-01:06Z: the maintainers closed all nine issues, one comment each (unread from the session; the owner reports they decline AI-generated analysis); the five PRs still open at 01:15Z | **declined**: `declines_ai` set in site/audits.json; nothing further filed, commented or pushed; the #1358 fix stays in the repository |
| spm/spm | 5 PRs, 5 issues | 2 PRs merged + 2 issues resolved; #159 and #161 open with 3 unread comments each; #167/#168 new | read #159/#161 and respond; no new filings |
| fieldtrip/fieldtrip | 5 PRs, 2 issues | #2613 merged; #2610 'almost ready to merge' (2026-09-07), maintainer asks about the +1 as a bandwidth term; #2614 judged minor by the maintainer, who asked for a website FAQ and an Octave survey instead; #2608, #2611, #2612 no comments | replies drafted 2026-09-07: FT15 (#2610, with the bandwidth measurement) and FT16 (#2614, FAQ draft in the kit, Octave survey offered) — on the console |
| MouseLand/Kilosort | 2 PRs, 3 issues | all open, no comment | **freeze** |
| MouseLand/suite2p | 3 PRs, 3 issues | all open, no comment | **freeze** |
| thelovelab/DESeq2 | 1 PR, 3 issues | all closed by the maintainer 2026-09-01 under the results-stability policy | done; nothing further |
| scverse/scanpy | 1 PR, 1 issue | open; only the milestone bot has commented; issue carries the Triage label | wait; the `score_genes` PR (SC2) and the two Scrublet-port items stay held until a maintainer answers |
| lmcinnes/umap | 1 PR, 1 issue | open, no comment | wait |
| marcelm/cutadapt | 1 PR, 1 issue | open, no comment | wait; CA2–CA4 held |
| ventolab/CellphoneDB | 1 issue | open, no comment | wait; CPDB2–CPDB6 held |
| htseq/htseq | 1 PR, 1 issue | both closed by the maintainer within an hour; declines AI-generated contributions | done; fork to carry `upstream-declines-ai-contributions`; HC1 held permanently |
| chrchang/plink-ng | 1 PR, 1 issue | PR closed by the maintainer in favour of his own identical fix `1fe42e5`; issue open with 2 unread comments | done; verified at the fix commit; read #380 |
| deeptools, bedtools2, fastp, iqtree3, MACS, seurat | nothing filed | kits ready (deepTools, BEDTools, fastp), IQ-TREE discussion draft, MACS and Seurat unfiled | file the "now" tier only: DT7, DT8, BT1, FP2; the comments on open issues (#1108, #1118, #1142, #474, #518) after reading those threads |

Rule going forward, restated: no repository gets a new filing while it has an unanswered
one, and none gets more than two until a maintainer replies.

## Issue-fix round (from 2026-09-03 evening)

Posture change, recorded in README step 6: instead of filing more audit findings, work
through the checked repositories' own open issues, one reproducible bug each, and file a
PR against the issue. Deliverables under `audits/<package>/issue-fixes/<n>-<slug>/`. Rules:
nothing for HTSeq (declines); for repositories with unanswered audit filings (AFNI,
FreeSurfer, Suite2p, Kilosort, Scanpy, umap, Cutadapt, CellPhoneDB) the PR answers the
maintainers' own issue and is the only new item until they reply; the project-finding queue
stays frozen meanwhile.

Assigned issues (2026-09-04): no PR; comment with the diagnosis and a branch link instead. First case: SPM #104–#106 are assigned to the toolbox author.

### Issue-fix round, results (2026-09-04)

| repository | issue | what | state |
|---|---|---|---|
| spm/spm | #106 | `spm_MDP_VB_prune` NaN column when the surviving entries carry no prior mass | comment posted 2026-09-03 |
| MouseLand/suite2p | #1079 | rigid-only z-registration against a reference list crashes (`compute_shifts` zero-width nonrigid offsets) | assigned to the maintainer: comment + branch link, no PR |
| MouseLand/Kilosort | #1039 | `make_pc_features` re-orders channels twice for clusters sharing a detection template | PR ready |
| arq5x/bedtools2 | #1123 | `flank -s` drops every record without a `-`/`+` strand | PR #1143 open (filed 2026-09-04) |
| OpenGene/fastp | #638 (= #528) | `--dedup` drops counted as passed; `--merge --dedup` removed nothing | PR #715 open (filed 2026-09-04); behaviour change on `--merge` flagged |
| ventolab/CellphoneDB | #224 (= #137) | `create_db` merge on an all-NaN `uniprot_N` column | PR #232 open (filed 2026-09-04) |
| marcelm/cutadapt | #518 | `--info-file` offsets wrong after 5' trimming (maintainer's own 2021 issue) | PR #894 open (filed 2026-09-04; body addresses the Match-object idea) |
| deeptools/deepTools | #1423 | `computeMatrix` gzipped BED crash in `sortMatrix` | PR #1451 closed after the 4.0.0 merge; residual sort fix held |
| fieldtrip/fieldtrip | #2345 | `cfg.toi = 'NN%'` is the step, not the overlap | PR ready; every percentage but 50 changes the time axis |
| afni/afni | #73 | stale AFNI extension time axis; `3dvolreg` zero-byte output with exit 0 | PR #974 open (filed 2026-09-04) |
| lmcinnes/umap | #1194 | `transform` refuses precomputed distances above 4096 rows | PR #1288 filed 2026-09-08 (second umap fix, after #1287 merged) |
| chrchang/plink-ng | #140 | `--bmerge` duplicate-ID counts and warning asymmetric | PR #387 filed and closed 2026-09-05 within a minute, one comment (unread from the session; likely the maintainer's own fix, as with #381) |
| freesurfer/freesurfer | #1358 | `mri_convert --out_orientation` shifts by one voxel per flipped axis | not to be filed: the maintainers decline AI-generated contributions (2026-09-08) |
| scverse/scanpy | #3809 | `.distances` keeps `n_neighbors` entries on transformer paths (≥ 8192 cells by default) | PR ready; 6 unread comments on the issue |
| macs3-project/MACS | #715 | `bdgdiff` scores truncated to integers | PR #739 open (filed 2026-09-05); two held findings in the kit README |
| iqtree/iqtree3 | #203 (+ #89, likely #135/#102) | `setRootNode` assertion when the outgroup is absent from a partition/quartet | PR #207 **merged 2026-09-08** (no discussion); closes #203 and #89 |
| iqtree/iqtree3 | #192 | `GY{...}+FU{61 freqs}` silently becomes `GY+F`: user codon frequencies ignored, 60 free parameters, wrong likelihood (2.4.0 correct) | PR #210 open (filed 2026-09-08) |

Each kit under `audits/<package>/issue-fixes/<n>-<slug>/` records the alternates considered, so the next round can start from those.

### deepTools after the 4.0.0 rewrite (2026-09-04/05)

`master` was replaced by the 4.0.0 squash merge (`4db9d816`, then `6f939b0`): Rust backend, Python
in `pydeeptools/`. Re-verified by execution (`audits/deeptools/README.md`, top section): DT1 survives
in part (no shift; a skipped bin is still merged into its neighbours), DT3, DT4, DT5, DT8 (wider:
every bin ≥ 1280 bp is a zoom summary), DT9 survive; DT2 and DT6 fixed by the rewrite; DT7 not
applicable (option removed). Six patches on `fix4/*` branches of the fork, all `git am`-clean on
`6f939b0`, pytest 233 and `cargo test` 48/50 passing. The maintainers closed #1108, #1130, #1423
and #1140 on 2026-09-05 with the merge; #1118 is still open. Filing plan under the cap: DT8 PR now
(self-contained body, no prior issue), DT4 comment + PR on the open #1118; DT1 needs a fresh issue
(its threads closed) and is held with DT3, DT5, DT9 and the residual #1423 sort fix. Two new
4.0.0-only defects were filed 2026-09-05 as pre-release reports: bamCompare `--operation` (#1457, PR #1458) and
plotPCA loadings (#1459, PR #1460). PR #1451 (the #1423 fix against 3.5.6) was closed after the merge.
deepTools now has two unanswered filings; everything else there is held.

## Round 3 (2026-09-08): samtools, featureCounts, edgeR, lme4, clusterProfiler

Five new packages, chosen for citation volume outside the neuroscience/single-cell set already
covered. Every finding below was verified by execution (READMEs under `audits/<package>/`); the
kits live under `audits/<package>/upstream/` and the console carries them in the "Do next" list.
Fixes that are already on the upstream development branch (edgeR EG1/EG2, lme4 LM5/LM6,
clusterProfiler CP1/CP2/CP3/CP6/CP7) are recorded and not raised.

| tier | finding | reason |
|---|---|---|
| filed 2026-09-08 (#2378 / PR #2379) | samtools ST1 (+ ST2, same patch) | `samtools stats` coverage distribution (COV rows, `-t`/`-g` target percentage) is accumulated in a ring of 5 × read length indexed modulo its size, so spliced (RNA-seq) alignments wrap around and mixed-length reads lose counts on buffer reallocation; every version since at least 1.9; issue then PR the same day |
| comment | lme4 LM2 on the maintainers' open #867 | default `glmer` Hessian standard errors about 100× too small in 9 of 150 ordinary Bernoulli fits, with only a `max|grad|` warning; measurement plus a guard (patch 0003) as the PR once the comment is up |
| file now (low magnitude, lead's call) | edgeR EG3 | `filterByExpr` drops a gene sitting exactly on the CPM cutoff by one ulp when the median library is a real library; all versions; one-line fix; goes to the Bioconductor support site because bioc/edgeR is a read-only mirror |
| comment | clusterProfiler CP5 on the open #819 | the 4.16 vs 4.20 difference the reporter saw is enrichit 0.1.x running BH over zero-overlap sets, fixed in enrichit 0.2.0; post only after reading the six comments already there |
| held | featureCounts FC1, FC2 | FC1 is a rare option (`--splitOnly` with unmapped mates); FC2 needs a mixed single/paired-end file; the ShiLab tracker's conventions could not be read from the session, so FC2 goes issue-first when a signal comes |
| held | lme4 LM1, LM3, LM4, LM7 | LM1 is a pre-release defect on `master` only (worth a heads-up before 2.x ships); LM3 is a warning-text nit; LM4 and LM7 are documentation |
| held | clusterProfiler CP4 (enrichit), CP8 | CP4 is a non-default `gsea(method = "sample")` path with an issue + patch ready for YuLab-SMU/enrichit, to follow a positive signal on #819; CP8 is a design question about `simplify()` |

Channel notes. samtools' CONTRIBUTING.md accepts AI-assisted work with an `Assisted-by` trailer,
a human-written commit message and PR description, and a human DCO sign-off; the kit's patch carries
the trailer and no sign-off. edgeR has no tracker or PRs. clusterProfiler's maintainer guide and
book were unreachable from the session and must be read before posting. Forks needed for the PRs:
samtools/samtools, lme4/lme4, YuLab-SMU/enrichit.
