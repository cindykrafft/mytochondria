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
| comment | deepTools DT1 (#1108/#1130), DT4 (#1118); BEDTools BT2 (#1142); fastp FP1 (#474), FP3 (#518) | cause and patch on threads the maintainers keep open |
| filed | Cutadapt CA1 (#892/#893), umap-learn U1 (#1286/#1287), CellPhoneDB CPDB1 (#231), Scanpy SC1 (#4336/#4337) | 2026-09-02/03, all open, no response yet |
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
| freesurfer/freesurfer | 5 PRs, 9 issues | all open, no comment in four days | **freeze**: nothing more until a maintainer replies; 7 confirmed findings stay held |
| spm/spm | 5 PRs, 5 issues | 2 PRs merged + 2 issues resolved; #159 and #161 open with 3 unread comments each; #167/#168 new | read #159/#161 and respond; no new filings |
| fieldtrip/fieldtrip | 5 PRs, 2 issues | all open; #2610 (7 comments), #2608 (3), #2613 (1), #2609 (1), last activity 2026-09-03 | read all four threads; add the requested rationale comment to `test_ft_connectivity_psi.m` on #2610; no new filings |
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
| spm/spm | #106 | `spm_MDP_VB_prune` NaN column when the surviving entries carry no prior mass | assigned to the toolbox author: comment with diagnosis + branch link, no PR |
| MouseLand/suite2p | #1079 | rigid-only z-registration against a reference list crashes (`compute_shifts` zero-width nonrigid offsets) | assigned to the maintainer: comment + branch link, no PR |
| MouseLand/Kilosort | #1039 | `make_pc_features` re-orders channels twice for clusters sharing a detection template | PR ready |
| arq5x/bedtools2 | #1123 | `flank -s` drops every record without a `-`/`+` strand | PR ready |
| OpenGene/fastp | #638 (= #528) | `--dedup` drops counted as passed; `--merge --dedup` removed nothing | PR ready; behaviour change on `--merge` flagged |
| ventolab/CellphoneDB | #224 (= #137) | `create_db` merge on an all-NaN `uniprot_N` column | PR ready |
| marcelm/cutadapt | #518 | `--info-file` offsets wrong after 5' trimming (maintainer's own 2021 issue) | PR ready |
| deeptools/deepTools | #1423 | `computeMatrix` gzipped BED crash in `sortMatrix` | PR ready |
| fieldtrip/fieldtrip | #2345 | `cfg.toi = 'NN%'` is the step, not the overlap | PR ready; every percentage but 50 changes the time axis |
| afni/afni | #73 | stale AFNI extension time axis; `3dvolreg` zero-byte output with exit 0 | PR ready; repository has a large unanswered backlog from us |
| lmcinnes/umap | #1194 | `transform` refuses precomputed distances above 4096 rows | PR ready |
| chrchang/plink-ng | #140 | `--bmerge` duplicate-ID counts and warning asymmetric | PR ready |
| freesurfer/freesurfer | #1358 | `mri_convert --out_orientation` shifts by one voxel per flipped axis | PR ready; large unanswered backlog from us |
| scverse/scanpy | #3809 | `.distances` keeps `n_neighbors` entries on transformer paths (≥ 8192 cells by default) | PR ready; 6 unread comments on the issue |
| macs3-project/MACS | #715 | `bdgdiff` scores truncated to integers | PR ready; two held findings in the kit README |
| iqtree/iqtree3 | #203 (+ #89, likely #135/#102) | `setRootNode` assertion when the outgroup is absent from a partition/quartet | PR ready once a fork of iqtree/iqtree3 exists |

Each kit under `audits/<package>/issue-fixes/<n>-<slug>/` records the alternates considered, so the next round can start from those.
