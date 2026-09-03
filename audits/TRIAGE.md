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
