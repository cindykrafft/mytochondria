# featureCounts audit against 331 published papers (2021–2026)

_Generated 2026-09-08 against `ShiLab-Bioinformatics/subread` `master` @ `55dc154`
(2023-07-30, builds as featureCounts v2.0.6) and the SourceForge release
tarballs 2.1.1 (the latest release, 2025), 2.0.3 and 2.0.1 (the cohort's
most-cited version). Focus: the code that produces the count matrix every
RNA-seq paper starts from — read-to-feature assignment, multi-mapping and
multi-overlap handling, strandedness, paired-end rules, the read filters and the
summary table — verified by executing the built binaries on synthetic BAMs with
known truth._

## What this is

The six-journal survey found **331 papers** in PNAS (164), *Nature* (143), *Cell*
(19) and *Science* (5), 2021–2026, that used featureCounts (part of the Subread
package; 25 name the Rsubread interface), almost always as the step between an
aligner (STAR in 148, HISAT2/TopHat in 62, Subread in 48) and DESeq2/edgeR/limma
(263). The whole of `readSummary.c`'s assignment path was read on `master` and
every suspicion was run through the built binary against an independent Python
implementation of the users guide's rules (`verify/fcref.py`), on random
annotations and random single-end and paired-end BAMs under 75 option sets, and
on hand-made cases. Findings were re-executed on the 2.1.1, 2.0.3 and 2.0.1
builds.

Two things to know about the repository before reading the table: the GitHub
`master` (v2.0.6) is two years behind the release channel — the maintainers
publish on SourceForge and Bioconductor (Rsubread) and push to GitHub in bulk;
the assignment logic is nevertheless the same on `master` and 2.1.1 (function
diffs are cosmetic, and every result reproduces on the 2.1.1 build). And the
project's issue tracker could not be read from this session (see "Filing
channel").

## Findings (details and line citations in [`component-reviews/read-assignment.md`](component-reviews/read-assignment.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **FC1** | **CONFIRMED on `master` (2.0.6), 2.1.1, 2.0.3 and 2.0.1** | held (rare option) | `-p --countReadPairs --splitOnly` counts every non-split fragment that has only one mapped record: a fragment is excluded only after *two* mapped non-split records were seen, and an unmapped mate (or the placeholder mate of a single-end record in a paired-end file) never reaches that counter. 1,000 of 1,000 non-split singletons Assigned where the manual says "all the other alignments will be ignored" (0/200 non-split proper pairs). Patch with a project test case ready. |
| **FC2** | **CONFIRMED on `master`, 2.1.1 and 2.0.3; 2.0.1 unaffected** (removed by the 2.0.2 changes, commit `1f24de1`, 2021-03-29) | held (mixed SE/PE files only); issue first | The documented "read type" filter — single-end reads inside a paired-end library are excluded from strand-specific counting because their strand cannot be related to the fragment — no longer exists: the `Unassigned_Read_Type` summary row is printed but nothing increments it, and such reads are counted as first reads. On a dUTP library (`-s 2`) with 300 pairs and 1,000 orphaned single-end reads from a `+` gene: S = 800, AS (antisense) = 500 instead of 300 / 0; 2.0.1 gives 300 / 0 with 1,000 `Unassigned_Read_Type`. Patch restoring the 2.0.1 branch, with a test, ready; the issue asks whether the removal was intended (then the manual needs the change). |
| N1 | note, summary rows only | — | In read-pair mode a fragment that fails two filters is labelled by the later filter, not the manual's first one (`-Q` is tested only on the second record, after chimera/length/duplicate/NH); counts unaffected. |
| N2 | note, design, undocumented | — | Features with strand `.` are never counted under `-s 1` and always (both strands) under `-s 2`. |
| N3 | note, summary only | — | `--byReadGroup` attributes the reads dropped by `-Q` to no read group; per-group columns do not sum to the input. |
| N4 | note, behaviour change 2.0.1 → 2.0.2 | — | `featureCounts -p` counts fragments on 2.0.1 (the cohort's most-cited version) and reads on 2.0.3+ (fragments need `--countReadPairs`): 500 assigned vs 941 on the same file. |
| N5 | note, documentation | — | `-C` drops same-strand pairs as chimeric as well as different-chromosome pairs; the option text mentions only the latter. |
| N6 | note, behaviour change 2.0.3 → 2.0.6 | — | `--largestOverlap` with `-O --fraction` divides by a different number of targets before 2.0.6 (fractions such as 1.17 and 2.67 where 2.0.6/2.1.1 give integers). |
| N7 | note, reporting | — | With a GTF and `-f`, count rows are named by `gene_id` (duplicated) and the `-R CORE` target is the gene, not the exon. |
| N8 | note, minor | — | A GTF attribute key given twice yields its last value. |

Four own suspicions were withdrawn by execution (a reference bug on singleton
fragments; the `-Q`/`--ignoreDup` label order, which is the pairer's record
order; the reverse feature index on long features; the automatic `chr`-prefix
matching, which works both ways). They are recorded in the review.

**Held up under execution:** on `master`, 2.1.1 and (bar N6/FC2) 2.0.3 and 2.0.1,
the documented assignment rules equal the independent implementation for every
fragment and every count under all 75 option sets on three random seeds
(default; `-O`; `-s 1/2`; `-M`, `--fraction`, `--primary`; `-Q`; `--ignoreDup`;
`--splitOnly`/`--nonSplitOnly`; `--minOverlap`, `--fracOverlap`, `--largestOverlap`,
`--nonOverlap`, `--fracOverlapFeature`, `--nonOverlapFeature`; `-f`; `--read2pos`,
`--readExtension5/3`; `-B`, `-C`, `-P -d -D`; read-level counting of paired data),
and the summary rows sum to the input in every run; the read pairer on
coordinate-sorted input (179,309 records, mates up to 300 kb apart, multi-mappers,
1 and 8 threads) equals name-adjacent input; `-J` junction counts; `-T`; per-file
`-s`; GTF vs SAF; GTF attribute parsing; the `Length` column; fraction rounding;
the project's own test suite. Not checked: `-L`, `cellCounts`, `-J -G`, `-A`,
`-R SAM/BAM`, read shifting, GFF3, the Rsubread interface.

**File-now candidates: none.** Under default and common settings the count
matrix held up; both confirmed findings need a non-default option (`--splitOnly`)
or an uncommon input (BAMs mixing paired and unpaired records under `-s 1/2`).

## How the papers use featureCounts (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 77 (2.0.1 ×41, 2.0.0 ×15, 1.6.4 ×12, 1.5.0 ×11, 1.6.3 ×10, 2.0.6 ×8, 1.5.2 ×8, 1.6.2 ×8, 1.6.0 ×6, 2.0.3 ×2, 2.1.1 ×1; families 2.0.x 69, 1.6.x 42, 1.5.x 23) |
| DESeq2 / edgeR / limma downstream | 263 |
| aligner named: STAR / Bowtie2-BWA / HISAT2-TopHat / Subread-Subjunc | 148 / 98 / 62 / 48 |
| RNA-seq / single-cell / ATAC-ChIP-CUT&RUN / long reads | 108 / 49 / 45 / 23 |
| GENCODE-Ensembl-RefSeq annotation / GTF-GFF / SAF | 58 / 16 / 1 |
| paired-end or fragment counting (`-p`, `--countReadPairs`) | 49 |
| a MAPQ threshold named (any tool) | 35 (cutoffs: 10 ×3, 1, 5, 20, 30, 40) |
| TPM / FPKM / RPKM / CPM computed from the counts | 35 |
| Rsubread interface | 25 |
| feature level (`-f`, exon counts) | 24 |
| strand-specific counting (`-s 1/2`) / unstranded stated | 19 / 7 (modes: 0 ×6, 1 ×6, 2 ×6) |
| multi-overlap `-O` / multi-mapping `-M` / `--fraction` / `--primary` | 15 / 14 / 6 / 4 |
| `-t` / `-g` stated | 9 / 9 (`-t exon` ×5, `gene` ×2; `-g gene_id` ×2, `gene_name` ×1) |
| `-B` / `-C` / `-P` / `--ignoreDup` / `--minOverlap` / `-J` | 7 / 5 / 1 / 2 / 2 / 1 |
| `--splitOnly` / `--nonSplitOnly` | 0 |

Exposure by finding: FC1 needs `--splitOnly` (0 in the cache); FC2 needs `-s 1/2`
with `-p` on a BAM containing unpaired records (19 papers name stranded counting,
49 paired-end; whether a BAM was mixed cannot be decided from the cache; the
common STAR path writes pairs only). N4 concerns the 41 papers naming 2.0.1
whose command lines, rerun on a current build, count reads instead of fragments.

**Profiling caveat.** As for the Seurat, Scanpy and Cutadapt audits, this
session had no route to Europe PMC, so `featurecounts_profile.py` ran in
`--offline` mode over the survey's stored evidence snippets; every record in
`featurecounts_profiles.jsonl` is `source: survey_cache` and every count above is a
lower bound. Rerun without `--offline` from a host with Europe PMC access to
replace them with full-text records.

## Filing channel (read before anything is sent)

- The repository has **no CONTRIBUTING file, no issue or PR templates, no
  `.github/` directory, no changelog and no linter**; `README.md` points users to
  the SourceForge release page, Bioconductor for Rsubread, and the users guide.
  Tests are shell scripts under `test/featureCounts/` comparing counts with `.ora`
  expectation files through `data/compare.sh`; both patches add a case there.
- **The GitHub issue tracker could not be read from this session**: the
  `search_issues` tool returns zero results for the repository under three
  phrasings, `list_issues` is not enabled for it, `api.github.com` is refused by
  the proxy and `github.com` HTML is blocked. Whether the maintainers answer
  GitHub issues, and whether either finding has a prior report, has to be checked
  by the lead before filing. The code itself cites the Subread Google Group
  (`readSummary.c:3311`) as a user forum, and Rsubread questions go to the
  Bioconductor support site; the GitHub history (50 commits, "sync code with
  Rsubread latest version") shows the repository is a mirror of the SourceForge
  releases rather than the development tree.
- The fork `github.com/cindykrafft/subread` does not exist yet (no
  `upstream-declines-ai-contributions` topic; `site/audits.json` has no entry).
- Nothing rises to "file now" (step 5). **The kit is in [`upstream/`](upstream/)**:
  two issue texts (free-form, no template exists) with self-contained
  reproductions run on `master`, 2.1.1, 2.0.3 and 2.0.1, two `git am`-able patches
  (fix + a `test/featureCounts` case that FAILS on unmodified `master` and PASSES
  with the patch; the full suite passes), PR bodies, and the list of documents
  read. FC2's issue asks the maintainers whether the 2.0.2 removal was intended
  before its PR is opened.

## Files

| file | what |
|---|---|
| `featurecounts_profile.py`, `featurecounts_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/read-assignment.md` | the review: FC1–FC2, N1–N8, withdrawn suspicions, held-up list, not-checked list |
| `verify/fclib.py`, `verify/fcref.py` | harness library (GTF/SAF/BAM writers, runner, parsers) and the independent implementation of the documented rules |
| `verify/heldup_bruteforce_random.py` (+ `.out`, `.seed2.out`, `.seed3.out`, `.v2.1.1.out`, `.v2.0.3.out`, `.v2.0.1.out`, `.patched_fc1.out`, `.patched_fc2.out`) | the 75-option-set battery on random data, per version and per patch |
| `verify/fc1_splitonly_pe_singletons.py` (+ `.out`, `.v2.1.1.out`, `.v2.0.3.out`, `.v2.0.1.out`, `.patched.out`) | FC1: five hand-made fragments and 1,000 singletons |
| `verify/fc2_read_type_stranded.py` (+ same set) | FC2: dUTP pairs plus orphaned first/second reads under `-s 0/1/2` and `-B` |
| `verify/heldup_misc.py` (+ `.out`) | `-J`, `-T`, per-file `-s`, GTF attributes, `-t exon,CDS`, SAF vs GTF, `Length`, fractions, `chr` prefix |
| `verify/heldup_sorted_input_pairer.py` (+ `.out`) | the pairer on coordinate-sorted input, 179k records, 1 vs 8 threads |
| `verify/note_filter_order_pe.py`, `note_unstranded_features.py`, `note_byreadgroup_mapq.py`, `note_p_semantics_versions.py` (+ `.out`, `.v*.out`) | N1–N4 |
| `upstream/` | filing kit: issue texts, MCVEs and their outputs, patches 0001 (FC1) and 0002 (FC2) with tests, PR bodies, documents read |

Harnesses need pysam (`uv venv --python 3.12 venv && uv pip install pysam`) and a
built binary named by `$FEATURECOUNTS` (default: the `master` build in the
scratchpad); `FC_OLD_PE=1` selects the pre-2.0.2 `-p` semantics for the 2.0.1 build.
2.0.1 needs `make -f Makefile.Linux CC_EXEC="gcc -fcommon" featureCounts`.

## Next steps

1. Read the open issues of `ShiLab-Bioinformatics/subread` from a session that
   can reach them: who answers, whether FC1/FC2 were reported, and whether the
   Google Group or Bioconductor support is the venue the maintainers prefer.
   Then file FC2 as a question-first issue and FC1 as an issue + PR, one at a time.
2. Extend the review to `-J -G` (splice-site strand inference) and `cellCounts`.
3. Full-text profiling rerun when Europe PMC is reachable, to see which papers
   used `--splitOnly` or mixed single/paired BAMs with stranded counting.
