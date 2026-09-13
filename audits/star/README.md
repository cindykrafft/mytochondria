# STAR audit against 489 published papers (2021–2026)

_Generated 2026-09-13 against `alexdobin/STAR` `master` @ `b1edc12` (the 2.7.11b release
commit is the branch head; the build reports `2.7.11b`). Focus: the code paths whose
numbers reach papers — `--quantMode GeneCounts` and `TranscriptomeSAM`, `SJ.out.tab`, the
`NH`/`HI`/`AS`/`nM`/`jM`/`jI`/`XS` tags and MAPQ, the mapped-read filters, the 2-pass
junction insertion and `Log.final.out` — verified by executing the built binaries on a
synthetic genome with reads simulated from known transcripts and truths computed
independently in Python._

## What this is

The six-journal survey found **489 papers** in *Nature* (238), PNAS (198), *Cell* (36) and
*Science* (17), 2021–2026, that used STAR — the default RNA-seq aligner in bulk and
single-cell pipelines. Its quantification, junction and statistics core was read in full on
`master` and every suspicion was run through three builds: `master` (= 2.7.11b, built here),
and 2.7.10a and 2.7.9a built from their release tags (the cohort's two most-cited versions),
on a 420-kb two-chromosome random genome with 17 designed genes (plus, minus and undefined
strands, overlapping and antisense genes, GC/AG, AT/AC and non-canonical introns, a
duplicated gene and a five-copy segment for multimappers, alternative isoforms, genes absent
from the GTF for novel junctions) and reads simulated from the transcripts with planted
mismatches and indels. Truths — union-mode gene counts, transcript projections, junction
collapsing and filtering, alignment scores, MAPQ and tag rules, filter thresholds and every
`Log.final.out` line — are computed in Python from the FASTA, the GTF and STAR's own genomic
SAM, never from STAR's counting code.

## Findings (details and line citations in [`component-reviews/quantification-and-junction-core.md`](component-reviews/quantification-and-junction-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **ST1** | **CONFIRMED on `master` (2.7.11b), 2.7.10a and 2.7.9a** | **now** | `--quantMode TranscriptomeSAM` writes every alignment to a transcript whose GTF strand is `.` (undefined — StringTie's single-exon transcripts, merged/de novo GTFs) with the strand flag inverted and the sequence reverse-complemented at the unchanged `+`-strand position (`Transcriptome_quantAlign.cpp:107` treats strand 0 like `-`; the coordinate conversion does not). On the synthetic annotation **300/300 and 300/300** single-end reads and **196/196 and 200/200** paired-end pairs on the two `.` transcripts differ from an independent projection, 0 of the reads on the 14 `+`/`-` transcripts; an eight-read MCVE shows 4 of 4 `.` records wrong. RSEM/salmon then see reads that mismatch the transcript at every base. Same on every build executed; correct with the patch. |
| **ST2** | **CONFIRMED on `master`, 2.7.10a and 2.7.9a** | now (same patch) | STARsolo `--soloStrand Forward` (default) counts **0 of 300** sense reads of a `.` gene in Gene, GeneFull and GeneFull_ExonOverIntron and counts them under `Reverse` instead (300); GeneFull_Ex50pAS counts 0 under both (8 of 8 feature × gene combinations; 4 of 4 on 2.7.9a, which lacks the last two features). `--quantMode GeneCounts` on the same reads counts 300, by STAR's own "genes w/o strand accept both strands" rule. Same root cause as ST1 (`trStr==1 ? Str : 1-Str` in the four solo files). |
| N1 | note, verified, documentation | held | `XS` under `--outSAMstrandField intronMotif` takes the annotated strand for annotated junctions (17 alignments over an annotated non-canonical intron carry `XS:A:+`), the motif strand otherwise; the manual says "derived from the intron motif". |
| N2 | note, verified, design | held | The spliced and soft-clipped versions of one read tie within `--outFilterMultimapScoreRange` at an unannotated non-canonical junction with a 7–9-base overhang and are both reported: NH 2, MAPQ 3, "mapped to multiple loci", `N_multimapping`, a multi-mapper junction count (5 of 300 SE reads, 3 of 200 pairs on such a gene). |
| N3 | note, verified, design | held | Non-canonical stitching allows no mismatches while GT/AG stitching allows any, so an unannotated non-canonical junction is displaced to a canonical motif 10 bases away for 4 unique reads (a spurious `SJ.out.tab` row) and 8–35 of 300 reads get a displaced primary alignment; the 2-pass run removes it. |
| N4 | note, verified, documentation | held | After `--twopassMode Basic`, `Log.final.out` "Number of splices: Annotated (sjdb)" counts pass-1 junctions as annotated (754 of 755 vs 497 of 646 in 1-pass); documented for `SJ.out.tab` column 6, not for the log. |
| N5 | note, by reading | held | `SJ.out.tab` column 9 is `min(left block, right block)` of the blocks adjacent to the junction, where an indel ends a block (a `TODO` in the source). |

Three own suspicions were withdrawn by execution (`transcriptInfo.tab`'s cumulative maximum
end looked one transcript late; multimappers' junctions looked counted once per alignment;
the neighbour-only distance filter) and are recorded in the review.

**Held up under execution:** `ReadsPerGene.out.tab` (19 rows × 3 strand columns × 4
configurations, 0 differences on `master`, 2.7.10a, 2.7.9a; overlapping, antisense and `.`
genes, intronic reads, multimappers and the `N_unmapped` = four unmapped classes identity);
TranscriptomeSAM positions, flags, sequences, NH and the primary for all 14 stranded
transcripts (SE and PE, two-isoform reads, the duplicated gene, soft-clip extension, indel and
single-mate bans); `SJ.out.tab` in 5 filter configurations (0 differing rows: motif codes,
strands, annotated flag, unique/multi counts with per-read deduplication, overhang, the
count/overhang/intron-length/distance filters, `--outSJfilterReads Unique`); NH, HI, MAPQ,
nM, jM/jI, pair flags, one primary with the maximum AS, and `AS` recomputed from the CIGAR and
genome (junction and indel penalties, the log2 genomic-length term) for 10,264 alignments;
the mismatch/score/match filters and their precedence at the boundaries, `--outFilterMultimapNmax`
at N/N+1; all 26 `Log.final.out` lines in 3 runs including `BySJout`; 2-pass insertion,
short-overhang rescue (80/80) and the `+2` score. Not checked: chimeric detection, STARsolo
beyond the strand rule, WASP, genome transforms, `--peOverlap`, BAM sorting.

## How the papers use STAR (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 150 (2.7.10a ×26, 2.5.2b ×25, 2.7.9a ×24, 2.7.3a ×20, 2.6.1d ×13, 2.5.3a ×11, 2.7.1a ×11, 2.7.10b ×10, 2.7.11b ×9) |
| DESeq2 / edgeR / limma downstream | 327 |
| featureCounts / htseq-count | 170 |
| single-cell / STARsolo / Cell Ranger | 109 |
| TranscriptomeSAM / RSEM / salmon / kallisto | 75 |
| paired-end reads stated | 47 |
| 2-pass mode | 27 |
| multimapper option stated | 26 (`--outFilterMultimapNmax`: 1 ×8, 20 ×4, 100 ×4, 10 ×2) |
| outSAMstrandField / Cufflinks / StringTie | 24 |
| uniquely mapped reads reported / mapping rate reported | 21 / 5 |
| SJ.out.tab / splicing analysis | 17 |
| ENCODE options | 14 |
| stranded library stated | 13 |
| GeneCounts / ReadsPerGene named | 8 |
| chimeric / fusion | 5 |

Exposure by finding: ST1 needs `--quantMode TranscriptomeSAM` (75 name RSEM/salmon/
TranscriptomeSAM) with an annotation carrying `.` strands (24 name StringTie/Cufflinks; the
cache cannot tell which annotation fed STAR); ST2 needs STARsolo with such an annotation (109
name single-cell tools). Every version the cohort names that was built here (2.7.9a, 2.7.10a,
2.7.11b) is affected; earlier versions were not built.

**Profiling caveat.** As for the Seurat, Scanpy, SAMtools and Cutadapt audits, this session had
no route to Europe PMC, so `star_profile.py` ran in `--offline` mode over the survey's stored
evidence snippets; every record in `star_profiles.jsonl` is `source: survey_cache` and every
count above is a lower bound. Rerun without `--offline` from a host with Europe PMC access
to replace them with full-text records.

## Filing channel (read before anything is sent)

- `CONTRIBUTING.md`: questions go to the rna-star Google group, the tracker is for bugs and
  features; reproduce on the latest version with mostly default parameters, search the
  tracker first (comment on an open duplicate, link a closed one), give exact commands,
  observed vs expected, system information, reproducibility, and attach `Log.out`; PRs need a
  clear title, the purpose, the expected behaviour change and the assurance that **default
  behaviour does not change**, and detailed commit messages. No AI-contribution policy.
- No `.github/` directory (no issue form, PR template or CI); `.travis.yml` only runs
  `make STAR`; no unit-test runner or linter; `extras/tests/scripts/` holds awk checkers.
  `CHANGES.md` takes one `* Issue #NNNN: Fixed ...` bullet per fix under a version heading.
- ST1+ST2 are the one "file now" item (one issue, one PR — the two-unanswered-filings cap is
  met exactly): a wrong number under default settings on the current release and every
  release the cohort names, no prior issue (tracker searched 2026-09-13; nearest #1922, #1880,
  #2679, #735, #2253, #2020). **The kit is in [`upstream/`](upstream/)**: issue text in the
  CONTRIBUTING order with a self-contained eight-read MCVE (run on `master`, 2.7.10a, 2.7.9a
  and the patched build), one `git am`-able patch (five one-line fixes, a regression script
  that fails on unmodified `master` and passes with the patch, `CHANGES.md` entry), and the PR
  body draft.

## Files

| file | what |
|---|---|
| `star_profile.py`, `star_profiles.jsonl`, `profile_run.log` | profiling pass over the 489 cohort papers (offline; see caveat) |
| `component-reviews/quantification-and-junction-core.md` | the review: ST1–ST2, N1–N5, withdrawn suspicions, held-up list, not-audited list |
| `verify/_synth.py` | synthetic genome/GTF/read builder, STAR runner, SAM helpers (motif codes, junctions, mismatches) |
| `verify/st1_transcriptome_strandless.py` (+ `.out`, `.v2.7.10a.out`, `.v2.7.9a.out`, `.patched.out`) | ST1: self-contained eight-read reproduction |
| `verify/st2_solo_strandless.py` (+ same set) | ST2: STARsolo Forward/Reverse/Unstranded × 4 features × `+`/`-`/`.` genes, with GeneCounts alongside |
| `verify/heldup_transcriptome_sam.py` (+ same set) | TranscriptomeSAM vs an independent projection (ST1 in bulk; the 14 stranded transcripts held up) |
| `verify/heldup_genecounts.py` (+ same set) | GeneCounts vs an independent union-mode counter, 4 configurations |
| `verify/heldup_sjout.py` (+ `.out`) | `SJ.out.tab` vs an independent collapse, 5 filter configurations |
| `verify/heldup_sam_tags.py` (+ `.out`) | NH/HI/MAPQ/AS/nM/jM/jI/XS, flags, primary choice, alignment accuracy, N1–N3 numbers |
| `verify/heldup_filters_logfinal.py` (+ `.out`) | mismatch/score/multimap filter boundaries and all `Log.final.out` lines |
| `verify/heldup_twopass.py` (+ `.out`) | 2-pass junction insertion, short-overhang rescue, `AS` changes, N4 numbers |
| `upstream/` | filing kit: issue text, MCVE + outputs, patch 0001 (ST1+ST2), PR body, documents read, test numbers |

Harnesses take the STAR binary and a scratch directory (`python verify/<h>.py /path/to/STAR
/path/to/workdir`) and need a Python ≥ 3.12 venv with `pysam` and `numpy`
(`uv venv --python /usr/bin/python3.12 venv && uv pip install pysam numpy`). Builds: `make STAR`
in `source/` (gcc, zlib); the 2.7.10a and 2.7.9a tags were built with `CXXFLAGSextra="-include array"` (gcc 13).

## Next steps

1. File the ST1+ST2 issue from `upstream/issue-st1-undefined-strand.md` and the PR from the
   patch (order of operations in `upstream/README.md`); record numbers and responses here and
   in the top-level status table. The notes wait for a maintainer signal.
2. Extend the review to STARsolo's UMI deduplication and `--soloMultiMappers`, chimeric
   detection, and `--peOverlap`.
3. Full-text profiling rerun when Europe PMC is reachable, to intersect the TranscriptomeSAM
   and StringTie/de-novo-annotation signals.
