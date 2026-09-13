# Component: STAR quantification, junction and read-statistics core (`master` @ `b1edc12` = tag 2.7.11b, 2026-09-13)

Read in full on `master` @ `b1edc12` (the 2.7.11b release commit is the branch head; the
`STAR --version` of the build is `2.7.11b`): `Transcriptome_geneCountsAddAlign.cpp` (63 lines;
`--quantMode GeneCounts`), `Transcriptome_quantAlign.cpp` (114; `--quantMode TranscriptomeSAM`
projection), `ReadAlign_quantTranscriptome.cpp` (91; its filters and soft-clip extension),
`Transcriptome.cpp` (190; loading `transcriptInfo.tab` / `exonGeTrInfo.tab`, `ReadsPerGene`
writer), `Quantifications.cpp`, `GTF.cpp` (171; strand coding) and `GTF_transcriptGeneSJ.cpp`
(183; transcript/exon tables and GTF junctions), `ReadAlign_outputTranscriptSJ.cpp` (56),
`OutSJ.cpp` (123) and `outputSJ.cpp` (163; `SJ.out.tab` collapsing and `--outSJfilter*`),
`sjdbPrepare.cpp` (225), `sjdbInsertJunctions.cpp` (102), `sjdbLoadFromStream.cpp`,
`twoPassRunPass1.cpp` (2-pass), `stitchAlignToTranscript.cpp` (415; junction/indel scoring),
`extendAlign.cpp` (93), `stitchWindowAligns.cpp` (355; transcript finalisation, genomic-length
score, strand consistency, ordering), `ReadAlign_multMapSelect.cpp` (95; multimappers and the
primary flag), `ReadAlign_mappedFilter.cpp` (20), `ReadAlign_outputAlignments.cpp` (324),
`ReadAlign_outputTranscriptSAM.cpp` (359; SAM fields, MAPQ, tags), the flag/MAPQ/tag part of
`ReadAlign_alignBAM.cpp`, `Stats.cpp` (156; `Log.final.out`), the STARsolo annotation files
`Transcriptome_classifyAlign.cpp`, `Transcriptome_geneFullAlignOverlap.cpp`,
`Transcriptome_geneFullAlignOverlap_ExonOverIntron.cpp`, `Transcriptome_alignExonOverlap.cpp`
(the strand test only), and the relevant entries of `parametersDefault`. Every suspect was
**executed on built binaries**: `master` built here with `make STAR` (gcc 13.3.0), and 2.7.10a
and 2.7.9a built from their release tags (the cohort's two most-cited versions; both old tags built with
`CXXFLAGSextra="-include array"` for gcc 13). Harnesses in `../verify/` build a synthetic
two-chromosome genome (420 kb, seed 20260913) with 17 designed genes, a GTF, and reads
simulated from known transcripts (`_synth.py`); every truth is computed independently in
Python from the FASTA, the GTF and STAR's own genomic SAM records, never from STAR's counting
code. Captured outputs sit next to the harnesses.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### STA1 — CONFIRMED on `master` (2.7.11b), 2.7.10a and 2.7.9a: `Aligned.toTranscriptome.out.bam` inverts the strand flag and reverse-complements the sequence of every record on a transcript whose GTF strand is `.`

**Code.** `GTF.cpp:138-144` stores a transcript's strand as 1 (`+`), 2 (`-`) or 0 (anything
else, i.e. `.`). When a genomic alignment is projected onto a transcript,
`alignToTranscript` converts coordinates to the transcript's orientation only for strand 2
(`Transcriptome_quantAlign.cpp:42-60`, `if (trStr1==2)`), but the strand of the transcriptomic
record is then set by

```c++
aTall[nAtr].Str = trStr[tr1]==1 ? aG.Str : 1-aG.Str; //TODO strandedness   // Transcriptome_quantAlign.cpp:107
```

so a strand-0 transcript gets `+`-strand coordinates with a `-`-strand flag. The BAM writer
reverse-complements the sequence whenever the mate's orientation differs from `Str`
(`ReadAlign_alignBAM.cpp:491-495`, the same rule as `ReadAlign_outputTranscriptSAM.cpp:196-206`),
so the stored sequence is the reverse complement of the transcript at the stored position.

**Verified** (`../verify/heldup_transcriptome_sam.py`: an independent projection of every
genomic alignment onto every compatible GTF transcript with the default
`BanSingleEnd_BanIndels_ExtendSoftclip` rules; `../verify/st1_transcriptome_strandless.py`:
a self-contained eight-read reproduction):

| case | transcripts | reads differing from the projection (flag and sequence; position and CIGAR right) |
|---|---|---|
| 16-transcript synthetic annotation, 300 100-bp SE reads per transcript | T3 (`.`, two exons), T4 (`.`, one exon) | **300 / 300 and 300 / 300** (`heldup_transcriptome_sam.out`) |
| same, 200 2×75 PE pairs per transcript | T3, T4 | **196 / 196 and 200 / 200** |
| same, the 14 `+`/`-` transcripts (SE and PE, including overlapping genes, alternative isoforms and a duplicated gene) | T1–T17 | 0 differing; NH equal to the record count for all 5,745 SE and 6,948 PE records, exactly one primary per read |
| 3-kb genome, identical two-exon structure on `+` (TP) and `.` (TD), 60-mers forward/reverse, exonic and junction-spanning | TD | **4 / 4** (TP: 0 / 4); e.g. `TD_fwd_100` expected flag 0 at 101 with the read sequence, got flag 16 with its reverse complement (`st1_transcriptome_strandless.out`) |

Same output from 2.7.10a and 2.7.9a (`.v2.7.10a.out`, `.v2.7.9a.out`;
`../upstream/mcve_outputs.txt`); every record equals the projection with the patch below
(`.patched.out`: 0 of 4,727 SE and 0 of 3,069 PE reads differ).

**Who is exposed.** Anyone feeding `Aligned.toTranscriptome.out.bam` to RSEM, salmon (`-a`)
or eXpress with an annotation that has `.` strands: StringTie writes `.` for single-exon
transcripts, and merged or de novo GTFs carry them; GENCODE/Ensembl reference annotations do
not. RSEM and salmon score a read against the transcript sequence, so such reads mismatch at
every base. In the cohort 75 papers name TranscriptomeSAM/RSEM/salmon and 24 name
StringTie/Cufflinks (survey-cache lower bounds; the two sets were not intersected).

**Fix shape.** Invert only for strand 2 (`../upstream/0001-*.patch`, one line in
`Transcriptome_quantAlign.cpp`, plus STA2 below, a regression script and a `CHANGES.md`
entry).

**Upstream.** No prior report: tracker searched 2026-09-13 with five phrasings; nearest
#1922 (open: a user who mis-entered `+` for every strand asks how strand is used), #1880
(open: soft-clipped transcriptome records with STARsolo), #2679 (open: custom GTF at the
mapping step), #735/#2253 (missing reads), #2020 (feature request).

### STA2 — CONFIRMED on `master` (2.7.11b), 2.7.10a and 2.7.9a: STARsolo `--soloStrand Forward` (the default) counts none of the sense reads of a gene whose GTF strand is `.`; `Reverse` counts all of them

**Code.** The same expression decides which strand a `.` gene accepts in every STARsolo
feature: `Transcriptome_classifyAlign.cpp:208` (Gene: `(trStr[tr1]==1 ? aG.Str : 1-aG.Str) !=
P.pSolo.strand` skips the transcript), `Transcriptome_geneFullAlignOverlap.cpp:24-25`
(GeneFull), `Transcriptome_geneFullAlignOverlap_ExonOverIntron.cpp:30-31`, and
`Transcriptome_alignExonOverlap.cpp:58-59` (GeneFull_Ex50pAS: `== (trStr[tr1]-1)` is never
true for strand 0, so neither `Forward` nor `Reverse` counts anything). `--quantMode
GeneCounts` handles the case on purpose (`Transcriptome_geneCountsAddAlign.cpp:32-36`,
`str1<2` test with the comment "genes w/o strand will accept reads from both strands").

**Verified** (`../verify/st2_solo_strandless.py`: 300 sense-strand 90-bp cDNA reads per
transcript with one cell barcode and distinct UMIs, `--soloType CB_UMI_Simple`, all four
gene features, and `--quantMode GeneCounts` in the same run; 1,200 of 1,200 reads uniquely
mapped):

| gene | `Forward` (Gene / GeneFull / GeneFull_ExonOverIntron / GeneFull_Ex50pAS) | `Reverse` | `Unstranded` | GeneCounts column 3 |
|---|---|---|---|---|
| G1 `+` | 300 / 300 / 300 / 300 | 0 / 0 / 0 / 0 | 300 ×4 | 300 |
| G2 `-` | 300 / 300 / 300 / 300 | 0 / 0 / 0 / 0 | 300 ×4 | 300 |
| G3 `.` | **0 / 0 / 0 / 0** | **300 / 300 / 300 / 0** | 300 ×4 | 300 |
| G4 `.` | **0 / 0 / 0 / 0** | **300 / 300 / 300 / 0** | 300 ×4 | 300 |

8 of 8 feature × gene combinations on `master` and 2.7.10a; 4 of 4 on 2.7.9a, which has only
Gene and GeneFull (`.v2.7.10a.out`, `.v2.7.9a.out`). The eight-read MCVE shows it too: under
`Forward` the `.` gene's two counted reads are the reverse ones (`../upstream/mcve_outputs.txt`).
With the patch every `.` gene receives its 300 reads under `Forward` and, by the GeneCounts
convention, also under `Reverse` (`.patched.out`, 0 of 8).

**Who is exposed.** STARsolo users with `.`-strand genes in the annotation (109 cohort papers
name single-cell / STARsolo / Cell Ranger, lower bound; how many use a StringTie-derived GTF
is not measurable from the cache). Such genes are silently empty in the default stranded
count matrix.

**Fix shape.** Accept both strands for strand-0 genes in the four solo files (same patch).

### N1 — NOTE, verified, documentation: `XS` under `--outSAMstrandField intronMotif` uses the annotated strand for annotated junctions, not the motif

The manual says the strand is "derived from the intron motif". `stitchWindowAligns.cpp:114-128`
counts `sjStr`, which for an annotated junction is the sjdb strand
(`stitchAlignToTranscript.cpp:30,230`; for a `.` GTF junction the sjdb strand falls back to
the motif, `sjdbPrepare.cpp:179-189`) and for an unannotated one the motif strand
(`stitchAlignToTranscript.cpp:247-253`). Executed (`../verify/heldup_sam_tags.py`, run 4): all
17 alignments over G9's annotated non-canonical intron (chrA 52301-53000, motif 0) carry
`XS:A:+` from the annotation; with that rule, and with a strand-less junction not vetoing a
stranded one (1 alignment with motifs 0 and GT/AG gets `XS:A:+`), 6,383 of 6,383 `XS` values
match. Sensible; the manual could say so.

### N2 — NOTE, verified, design: the spliced and the soft-clipped version of one read at one locus are reported as two "loci" when they tie within `--outFilterMultimapScoreRange`

A read whose overhang across an unannotated non-canonical junction is 7–9 bases scores the
same (±1) spliced (`+overhang −8`) and soft-clipped, so `multMapSelect` keeps both
(`ReadAlign_multMapSelect.cpp:28`, score range 1), the read gets `NH:2`, MAPQ 3, is counted
under "mapped to multiple loci" (`ReadAlign_outputAlignments.cpp:30-31`) and as
`N_multimapping` in `ReadsPerGene`, and its junction gets a multi-mapper count. Executed:
5 of 300 SE reads and 3 of 200 PE pairs from G16 (unannotated `CC..GG` intron) have NH 2 with
both alignments at one locus (`heldup_sam_tags.out`), and `SJ.out.tab` lists the G16 junction
with 39 unique + 5 multi reads (`heldup_sjout.out`). GC/AG (−4) can tie at overhangs 3–5.
Annotated junctions (+2) never tie. A design consequence of the score-range rule, rare in
practice; it matches the manual's definition of a multimapper as an alignment within the
score range.

### N3 — NOTE, verified, design: an unannotated non-canonical junction can be displaced to a nearby canonical motif because non-canonical stitching allows no mismatches

`--alignSJstitchMismatchNmax 0 -1 0 0` (`stitchAlignToTranscript.cpp:314-315`) rejects a
non-canonical stitch with any mismatch in the stitched region, while a GT/AG or CT/AC stitch
accepts any number; with `--scoreGapNoncan -8` a canonical placement 10 bases away that costs
up to three mismatches wins. Executed: the default SE run reports junction chrA:130291-130990
(CT/AC, strand 2, 4 unique reads, overhang 49) ten bases from the simulated intron
130301-131000 (`heldup_sjout.out`), and 8 (default) / 35 (`intronMotif` run) of 300 G16 reads
have their primary alignment displaced with a simulated overhang ≥ 8 (`heldup_sam_tags.out`);
in the 2-pass run the displaced junction disappears once the true one is inserted
(`heldup_twopass.out`). Documented penalties; worth knowing when reading non-canonical rows.

### N4 — NOTE, verified, documentation: after 2-pass, `Log.final.out` "Number of splices: Annotated (sjdb)" counts pass-1 junctions as annotated

The manual states this for `SJ.out.tab` column 6 but not for `Log.final.out`. Executed:
1-pass 497 annotated of 646 splices, 2-pass 754 of 755 (`heldup_twopass.out`); the novel
junctions (70301-72000, 80301-81000, 130301-131000) are inserted (`_STARgenome/sjdbList.out.tab`)
and reported with column 6 = 1. Reads over inserted junctions gain `--sjdbScore` (+2 for 105
reads; +10 for the 39 over the non-canonical one, whose −8 penalty also disappears), which is
how 2-pass changes `AS` and can change multimapper status. All documented behaviour except the
`Log.final.out` line.

### N5 — NOTE, by reading: `outputTranscriptSJ` overhang ignores indels

`ReadAlign_outputTranscriptSJ.cpp:19-24` takes `min(left block, right block)` of the blocks
adjacent to the junction, where an indel ends a block ("TODO calculate the length of overhangs
taking into account indels"). The harness defines the truth the same way, so this is a
description of what column 9 measures, not a verification of the manual's "maximum spliced
alignment overhang".

### Withdrawn suspicions (own, killed by execution)

- **W1** `transcriptInfo.tab` column 4 (`trEmax`) looked one transcript late:
  `GTF_transcriptGeneSJ.cpp:99-105` writes `trend` before updating it with the transcript
  being written, so `trEmax[k]` is the maximum end of transcripts 0..k−1. That is exactly what
  the backward scan needs (`Transcriptome_quantAlign.cpp:111`: after checking `tr1` itself,
  continue while an earlier transcript can still contain the alignment); every projection on
  overlapping genes (G5/G6, G7/G8), alternative isoforms (T15a/T15b) and the duplicated gene
  matched. Withdrawn.
- **W2** A multimapper crossing the same junction in several alignments looked counted once
  per alignment (comment at `ReadAlign_outputTranscriptSJ.cpp:6-7` says so); the per-read
  duplicate scan at lines 26-40 dedupes it: the duplicated gene's junction shows 47 multi
  reads for 47 reads, not 94, and all five `SJ.out.tab` configurations equal the independent
  collapse (`heldup_sjout.out`). Withdrawn.
- **W3** `--outSJfilterDistToOtherSJmin` is applied to sorted neighbours only
  (`outputSJ.cpp:89-119`); suspected to differ from "distance to any other junction" — it is
  equivalent, and 0 rows differ under the default, relaxed and strict settings. Withdrawn.

## What held up (executed, not just read)

- **`--quantMode GeneCounts`** (`heldup_genecounts.py`): all 19 rows × 3 columns of
  `ReadsPerGene.out.tab` equal an independent union-mode counter on STAR's SAM in 4
  configurations (SE, PE, `--outFilterMultimapNmax 1`, PE `EndToEnd`), on `master`, 2.7.10a,
  2.7.9a and the patched build: same-strand overlapping genes (G5/G6) and antisense
  overlapping genes (G7/G8) go to `N_ambiguous` in the right columns, `.` genes count from both
  strands in columns 3 and 4, a read whose only aligned bases are intronic is `N_noFeature`,
  multimappers are `N_multimapping` (405 SE) and become `N_unmapped` = the four
  `Log.final.out` unmapped classes (459) with `--outFilterMultimapNmax 1`; column sums equal
  the input read count.
- **TranscriptomeSAM** for `+`/`-` transcripts (`heldup_transcriptome_sam.py`): positions,
  flags, sequences, CIGARs, NH and the single primary equal the projection for all 14 stranded
  transcripts, SE and PE, including reads compatible with two isoforms (NH 2), the duplicated
  gene (records on both copies), soft-clip extension with the mismatch cap, and the indel and
  single-mate bans.
- **`SJ.out.tab`** (`heldup_sjout.py`): 5 configurations (defaults SE and PE,
  `--outSJfilterReads Unique`, relaxed 1/1/5/0, strict 50-40-30-30/48/10) — every row (strand,
  motif code for GT/AG, CT/AC, GC/AG, AT/AC and non-canonical, annotated flag, unique and
  multi counts, maximum overhang) equals the independent collapse; a junction crossed by both
  mates counts once; annotated junctions bypass the count/overhang/distance filters; the
  intron-length-vs-read-count rule; 0 differing rows.
- **SAM tags and flags** (`heldup_sam_tags.py`): NH, HI (1..NH), MAPQ (255/3/1/0), nM
  (mismatches over M blocks, N excluded), jM (+20 when annotated) / jI, pair flags and mate
  fields, exactly one primary with the maximum AS — 6,401 SE, 3,803 PE and 60 indel
  alignments, 0 mismatches; **AS** recomputed from the CIGAR and genome (match +1, mismatch
  −1, annotated junction +2, GT/AG 0, GC/AG −4, AT/AC −8, non-canonical −8, indel −2−2·len,
  `ceil(log2(span)·(−0.25) − 0.5)`, floored at 0) equals STAR's for every alignment; `XS`
  under `intronMotif` (N1); with `intronMotif`, 34 of 48 spliced G16 alignments (unannotated
  non-canonical) are suppressed as documented; primary choice among equal-score multimappers
  is deterministic across runs (147 chrA / 153 chrB in both) and `--outSAMmultNmax 1` writes
  one primary record with NH 2.
- **Filters** (`heldup_filters_logfinal.py`): with `EndToEnd`, 100-bp reads with k planted
  mismatches map for k ≤ 10 (nM = k), are "too many mismatches" (uT 2) for 11 ≤ k ≤ 16 and
  "too short" (uT 1) for k ≥ 17 at the simulated locus, with the documented precedence
  (score/match filter before the mismatch filter; `--outFilterMismatchNoverLmax 0.05` cuts at
  k = 5/6, `--outFilterMismatchNmax 3` at 3/4); the only departures are alternative alignments
  with fewer mismatches or no seed ("other"), never a filtered read that the rules allow;
  `--outFilterMultimapNmax` N keeps N loci and rejects N+1 (2-locus and 5-locus reads).
- **`Log.final.out`** (`heldup_filters_logfinal.py`): all 26 numeric lines equal recomputation
  from the SAM and FASTQ in 3 runs (SE with mismatch and indel reads, PE, `--outFilterType
  BySJout`): percentages over input reads, average input length (PE = sum of mates), average
  mapped length / mismatch rate / splice counts by motif / indel rates and lengths over
  uniquely mapped reads only, "too many loci", and the read count preserved under BySJout's
  two-stage filtering.
- **2-pass** (`heldup_twopass.py`): the four novel pass-1 junctions are inserted, reads with a
  3- or 4-base overhang over a novel junction are soft-clipped in 1-pass and spliced in 2-pass
  (80 of 80), inserted junctions score +2, input read count unchanged.
- **Alignment accuracy** (as context, not a target): 5,044 of 5,091 unique SE and 3,348 of
  3,397 PE primary alignments equal the simulated blocks; the differences are simulated
  overhangs below the minimum (36 SE) and N3's displacement.

## Not audited

Chimeric detection (`--chimSegmentMin`, `Chimeric.out.junction`), STARsolo beyond the strand
rule (CB/UMI error correction, UMI deduplication, `--soloMultiMappers`, cell filtering, SJ and
Velocyto features), WASP, STARconsensus/STARdiploid genome transforms, `--peOverlap` mate
merging, long-read compilation, BAM sorting/`--outSAMtype BAM`, `--outSAMattributes` beyond the
ones checked (MC, CR/UR, GX/GN), `--sjdbFileChrStartEnd` inputs, `--outFilterIntronMotifs`
variants, the seed search and windowing heuristics (only their outcome on simulated reads),
`--varVCFfile` variation adjustment, and multi-threaded output ordering.
