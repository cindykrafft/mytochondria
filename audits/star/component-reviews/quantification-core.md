# Component: STAR's quantification and mapping-statistics core (`master` @ `b1edc12`, 2026-09-10, "STAR 2.7.11b")

The commit audited is `alexdobin/STAR` `master` @ `b1edc1208d91a53bf40ebae8669f71d50b994851`,
which is also the tag `2.7.11b` — the latest release. Every `file:line` below is on that
commit. Built from `source/` with `make STAR` (g++ 13.3.0, `-O3 -std=c++11 -fopenmp`,
zlib; the bundled htslib builds with it). The releases `2.7.10a` and `2.7.9a` — the
cohort's first and third most-cited versions — were built from their tags the same way
and every harness was run on all three binaries.

What was read in full and executed: the code paths that produce published numbers.

- `--quantMode GeneCounts` → `ReadsPerGene.out.tab`: `Transcriptome_geneCountsAddAlign.cpp`,
  `Quantifications.cpp`, `Transcriptome.cpp:100-140`.
- `--quantMode TranscriptomeSAM` → `Aligned.toTranscriptome.out.bam`:
  `ReadAlign_quantTranscriptome.cpp`, `Transcriptome_quantAlign.cpp`,
  `Transcriptome_alignExonOverlap.cpp`.
- STARsolo counting: `Transcriptome_classifyAlign.cpp`,
  `Transcriptome_geneFullAlignOverlap.cpp`, `Transcriptome_geneFullAlignOverlap_ExonOverIntron.cpp`.
- `SJ.out.tab`: `ReadAlign_outputTranscriptSJ.cpp`, `OutSJ.cpp`, `outputSJ.cpp`,
  `sjdbInsertJunctions.cpp`, `twoPassRunPass1.cpp`, and the `--outSJfilter*` defaults in
  `parametersDefault`.
- SAM/BAM record fields: `ReadAlign_alignBAM.cpp`, `ReadAlign_outputTranscriptSAM.cpp`,
  `ReadAlign_calcCIGAR.cpp`, `Transcript_alignScore.cpp`, `ReadAlign_multMapSelect.cpp`,
  `funPrimaryAlignMark.cpp`, `ReadAlign_mappedFilter.cpp`.
- `Log.final.out`: `Stats.cpp`.
- GTF ingestion: `GTF.cpp`, `GTF_transcriptGeneSJ.cpp`.

The truths are independent: a fixed-seed two-chromosome synthetic genome
(`verify/_synth.py`) with 14 genes on both strands — overlapping genes, an antisense
gene, two isoforms of one gene, planted GT/AG, CT/AC, GC/AG, CT/GC, AT/AC, GT/AT and
non-canonical intron motifs, genes inside 2-, 3- and 12-copy repeats, and one gene whose
GTF strand column is `.` — with single-end 100 nt and paired-end 2 × 75 nt reads
simulated from the transcripts (0.3 % substitutions, indel reads, intronic, intergenic,
antisense, junk and half-junk reads). Every read name indexes a truth record. The
comparisons are against Python ports written from the manual and the SAM specification,
not from STAR's code: an HTSeq-union gene counter, a junction extractor with STAR's
documented `--outSJfilter*` rules, a transcriptome projector, a recomputation of
`NH`/`HI`/`AS`/`nM`/`NM`/`MD`/`jM`/`jI`/MAPQ/`XS` from the read and the genome, and a
recomputation of all 27 `Log.final.out` statistics.

## Findings

### ST1 — CONFIRMED on `master`/2.7.11b, 2.7.10a and 2.7.9a: a GTF feature whose strand column is `.` gets its strand inverted in the transcriptome BAM and is not counted at all by stranded STARsolo

A GTF exon line's strand column is parsed in `GTF.cpp:138-143` into three codes: `1` for
`+`, `2` for `-`, and `0` for anything else — which in practice means `.`, the value the
GTF/GFF3 specification prescribes for a feature with no strand. The same three codes
reach the gene table (`Transcriptome.cpp:120`) and the transcript table
(`Transcriptome.cpp:49`).

One counting path handles code `0` deliberately. `Transcriptome_geneCountsAddAlign.cpp:32-36`
computes `uint str1 = (uint)exG.str[e1]-1;` and then skips the strand test when
`str1 >= 2`, with the comment on line 34:

> `//str1<2 (i.e. strand=0) requirement means that genes w/o strand will accept reads from both strands`

So `--quantMode GeneCounts` gives a strandless gene the same count in all three
strandedness columns. That is the intended semantics, stated by STAR itself.

Four other paths test only for code `1` and treat everything else — code `0` included —
as the minus strand:

- `Transcriptome_quantAlign.cpp:107`
  `aTall[nAtr].Str = trStr[tr1]==1 ? aG.Str : 1-aG.Str; //TODO strandedness`
  — the transcriptomic alignment of a read on a strandless transcript gets the
  *inverted* strand, while `alignToTranscript` (`Transcriptome_quantAlign.cpp:42`)
  converts the coordinates only when `trStr1==2`, i.e. leaves them on the `+` strand.
  The record that reaches `Aligned.toTranscriptome.out.bam` therefore carries a POS
  computed as if the transcript were `+` and a FLAG `0x10` bit computed as if it were
  `-`. It is internally inconsistent: SEQ, which SAM requires to be given on the
  reference forward strand, no longer matches the transcript at the reported POS.
- `Transcriptome_classifyAlign.cpp:208` (STARsolo `Gene`) and
  `Transcriptome_geneFullAlignOverlap.cpp:24` and `:43` (`GeneFull`) and
  `Transcriptome_geneFullAlignOverlap_ExonOverIntron.cpp:30` (`GeneFull_Ex50pAS`) —
  same `==1 ? … : 1-…`, so under `--soloStrand Forward` every sense read on a
  strandless gene is rejected and the gene gets **zero** counts.
- `Transcriptome_alignExonOverlap.cpp:58`
  `bool str1 = int(strandType==0 ? aG.Str : 1-aG.Str) == (trStr[tr1]-1);`
  — for code `0` the right-hand side is `-1` (integer promotion of `uint8` 0 minus 1),
  which no strand value can equal, so a strandless transcript matches nothing at all.

**Executed** (`verify/st1_trsam_strandless_transcript.py`, output
`verify/st1_trsam_strandless_transcript.out`). A 6-kb random genome carries one two-exon
transcript with a GT/AG intron. The *same* reads — 10 sense and 10 antisense single-end,
the same as pairs, 40 sense cDNA reads with cell barcodes — are mapped against two
annotations that differ **only in the strand column**, `+` and `.`:

| | `+` annotation | `.` annotation |
|---|---|---|
| single-end transcriptome records | 20 | 20, at the **same 20 positions**, with the strand flag differing on **all 20** |
| SEQ mismatches against the transcript at the reported POS, summed over records | **0** | **1524** (single-end); **2018** (paired-end, 36 records, all 36 flags flipped) |
| reads whose (first) mate is on the transcript's forward strand — what `RSEM --forward-prob 1` keeps | 10 of 20 (truth: 10 sense) | 10 of 20 — **the other 10** |
| STARsolo `--soloStrand Forward`, `Gene` / `GeneFull` UMI counts | 40 / 40 | **0 / 0** |
| STARsolo `--soloStrand Unstranded` | 40 / 40 | 40 / 40 |

The transcriptome part is not a labelling nicety. A strand-aware transcript quantifier
reads the FLAG: on this annotation `RSEM --forward-prob 1` (and salmon or eXpress in a
stranded library type) would keep precisely the antisense reads and discard the sense
ones. The STARsolo part is a silent zero: the gene is in `features.tsv` with a count of
0 in every cell, and nothing in `Log.out` or `Summary.csv` says why.

The whole-annotation harness (`verify/heldup_transcriptome.py`) reproduces it inside the
larger synthetic annotation and bounds it: of 11,189 single-end transcriptome records,
**400** differ from the independent port and every one of them is a strand flag on `T14`,
the strandless transcript ("differences confined to the strand flag of records on the
strand-less transcript T14 (finding ST1): True"); paired-end, 800 of 20,748.

**Version scope, by execution** (`verify/st1_*.v2.7.10a.out`, `.v2.7.9a.out`,
`upstream/mcve_outputs.txt`): AFFECTED on `master`/2.7.11b (the latest release), 2.7.10a
and 2.7.9a, with identical numbers. Unaffected with the patch in `upstream/`
("strand flag differs 0 … SEQ mismatches … '.' total 0", solo `Gene` 40 / `GeneFull` 40).
The cohort's 2.5.2b was not built (STARsolo does not exist there); the code line
`trStr[tr1]==1 ? aG.Str : 1-aG.Str` predates every version tested, so 2.5.2b's
transcriptome BAM is expected to be affected too — **not executed, so not claimed**.

**Who is exposed.** Annotations distributed by GENCODE, Ensembl and RefSeq give every
feature `+` or `-`, so a stock human or mouse run is unaffected. `.` appears in
annotations built from strand-agnostic evidence: BED-derived custom GTFs (issue #1922 in
this tracker is a user who had exactly this), repeat and TE annotations, some ncRNA and
enhancer catalogues, viral and organelle add-ins, and GFF3 converted by tools that keep
`.`. The failure is silent in both directions — inverted flags, or zeros — so a user has
no signal that the strand column mattered.

### N1 — NOTE, verified, design: the default transcriptome output silently drops reads whose junction overhang is too short to extend

`--quantTranscriptomeSAMoutput`'s default `BanSingleEnd BanIndels ExtendSoftclip`
(`parametersDefault`; the manual's `--quantTranscriptomeSAMoutput` entry) makes the transcriptome BAM RSEM-compatible by extending soft clips into
full matches. When the extension runs off the transcript or produces too many mismatches
the alignment is dropped instead, and nothing counts it.

Executed (`verify/heldup_transcriptome.out`, the "note" block): of the simulated
single-end reads whose true junction overhang is 1–2 nt, **40 reads, 9 of which reach the
transcriptome BAM** under the default; with soft clips allowed (`--quantTranscriptomeSAMoutput
BanSingleEnd`) all 40 do. Over the whole run, **9,547** single-end reads reach the
transcriptome BAM by default against **9,797** with soft clips allowed — 250 reads (2.4 %
of the 10,299 genome-mapped reads) present only in the permissive run; paired-end, 9,441
against 9,595. The port attributes the default-run losses as: no compatible transcript
1,793; indel 200; no compatible transcript after soft-clip extension 50; soft-clipped
47. This is the documented design (RSEM cannot take soft clips), and the reads lost are
concentrated at junctions — but the manual does not say that extension can fail, and the
loss appears in no statistic. Not a wrong number at master; a bias worth knowing when
transcript-level counts are compared with gene-level counts from the same run.

### N2 — NOTE, verified, documentation: `ReadsPerGene.out.tab`'s `N_unmapped` includes reads mapped to too many loci

Executed (`verify/heldup_genecounts.out`). Single-end: `N_unmapped` is **501** while
`Log.final.out` reports 199 + 0 + 2 = **201** unmapped reads and 300 reads "mapped to too
many loci"; 501 = 201 + 300 exactly (the harness asserts it: "N_unmapped 501 ==
unmapped(mism+short+other) 201 + too many loci 300 : True"). Re-run with
`--outFilterMultimapNmax 2`, `N_unmapped` becomes **1,017** = 201 + 816. The four
`ReadsPerGene.out.tab` columns are documented in the manual ("Counting number of reads per gene"); the `N_*` header
rows are not documented at all, and a reader who computes an assignment rate from
`N_unmapped` will attribute multimapping to unmappability. The three columns do sum to
the input read count (10,800 in all three columns, matching `Log.final.out`'s "Number of
input reads"), so the file is internally consistent — the label is what misleads.

### N3 — NOTE, verified on 2.7.9a, already fixed at master: 2.7.9a wrote transcriptome records for reads it had discarded as mapping to too many loci

Executed (`verify/heldup_transcriptome.v2.7.9a.out` against `.v2.7.10a.out` and `.out`).
On 2.7.9a the transcriptome BAM holds **11,489** single-end records for **9,847** reads
where the independent port has 11,189 for 9,547; the 300 extra reads are all on `T12`,
the transcript inside the 12-copy repeat, whose reads exceed the default
`--outFilterMultimapNmax 10` and are counted as "mapped to too many loci" everywhere
else (`heldup_genecounts` truth table: "from gene G12 -> unmapped 300"). Paired-end,
598 extra records. On 2.7.10a and on `master` the transcriptome records equal the port
exactly, apart from ST1. This is a known regression: `CHANGES.md`, 2.7.10a bug fixes,
"Fixed a bug introduced in 2.7.9a for `--quantMode TranscriptomeSAM` output that resulted
in both mapped and unmapped output for some reads." Recorded here because **24 cohort
papers name 2.7.9a** and the effect is a transcript-level count inflated by reads the
same run reported as unmapped — worth knowing when re-analysing that data, not a finding
at master.

### Withdrawn suspicions (own, killed by execution)

- *"`--outSAMstrandField intronMotif` must infer XS from the motif and will get annotated
  non-canonical junctions wrong."* Withdrawn. `heldup_sam_tags.py` recomputes XS from the
  junction strands independently — annotation strand where the junction is annotated,
  motif strand otherwise — for all **1,350** spliced records in the `intronMotif` run;
  discrepancies: none (`verify/heldup_sam_tags.out`).
- *"MAPQ 255/3/1/0 will not line up with `NH` at the 3-vs-4 boundary."* Withdrawn. The
  independent map (`NH` 1 → 255, 2 → 3, 3–4 → 1, ≥ 5 → 0) matched every one of 11,639
  single-end and 10,768 paired-end alignment records.
- *"The `annotated` column of `SJ.out.tab` silently changes meaning in 2-pass mode."*
  Withdrawn as a finding: it does change (21 junctions, 21 unannotated in pass 1, all 21
  reported `annotated=1` in pass 2 — `verify/heldup_sjout.out`) but the manual states it
  explicitly (`SJ.out.tab` column 6: "Note that in 2-pass mode, junctions detected in the 1st pass are
  reported as annotated, in addition to annotated junctions from GTF"). Documented
  design, not a finding.
- *"The primary alignment among equal-score multimappers is picked non-deterministically,
  so `NH`/`HI` and the primary flag can disagree."* Withdrawn. Over both runs, records
  whose `NH` differs from the number of alignments of that read: **0**; reads without
  exactly one primary record: **0**; and the primary record always carries the maximal
  `AS` (`verify/heldup_sam_tags.out`, `verify/heldup_transcriptome.out`).
- *"`Log.final.out`'s percentages use inconsistent denominators."* Withdrawn. All 27
  statistics matched the port on three runs (`verify/heldup_logfinal.out`); the
  denominators are as documented — "Number of input reads" for the read percentages,
  mapped bases of uniquely-mapped reads over those reads for "Average mapped length"
  (947,107 / 9,476), mapped bases for the mismatch and indel rates — and
  unique + multi + too-many-loci + unmapped = input exactly on every run.

## What held up (executed, not just read)

Run on `master`/2.7.11b, 2.7.10a and 2.7.9a; the three binaries produced byte-identical
harness output apart from the version header, except where N3 says otherwise.

- **`--quantMode GeneCounts`** (`verify/heldup_genecounts.out`): all 18 rows of
  `ReadsPerGene.out.tab` — 14 genes plus `N_unmapped`, `N_multimapping`, `N_noFeature`,
  `N_ambiguous` — in all three strandedness columns, against an HTSeq-union port, on
  three runs (single-end, paired-end, and single-end with `--outFilterMultimapNmax 2`).
  **Rows differing: 0 of 18** in each. This covers multimappers going to
  `N_multimapping` and not to any gene, the overlapping pair G4/G5 and the antisense pair
  G1/G6 producing `N_ambiguous` (1,143 single-end reads) in the unstranded column but
  resolving in the stranded ones (278 and 276), the two isoforms of G7 counted once to
  the gene, the strandless gene G14 counted identically in all three columns (400/400/400
  — the intended behaviour that ST1's other paths do not follow), and columns summing to
  the input read count.
- **The stranded columns against the simulation truth**: for genes on `+`, 2,687 sense
  reads land in column 3 and 2,587 antisense reads in column 4; on `-`, 985 and 974; on
  the strandless gene, all 400 reads (190 antisense, 210 sense) land in column 3 as well
  as the others.
- **`SJ.out.tab`** (`verify/heldup_sjout.out`): all **9 columns of every row identical**
  to the port on eight runs — single-end and paired-end with a GTF, single-end and
  paired-end without, `--twopassMode Basic` with and without a GTF, `--outFilterType
  BySJout`, and `--outSJfilterCountUniqueMin -1 -1 -1 -1` (unique reads only). Intron
  motif codes 0/1/2/3/5, the annotated flag, unique and multi-mapping crossing counts
  (1,337 / 5 with the GTF; 1,114 / 257 without), and the maximum overhang (50 single-end,
  37 paired-end). The `--outSJfilter*` defaults were reproduced from `parametersDefault`
  and account for every removed junction: 4 non-canonical junctions removed for
  `count<3` and overhang below 30, 8 GT/AG and 5 GC/AG junctions removed for overhang
  below 12. All **17 true junctions** appear in `SJ.out.tab` with the GTF; under
  `BySJout`, of 1,371 junction crossings in the BAM, **0** are absent from `SJ.out.tab`.
- **2-pass novel-junction insertion**: without a GTF, pass 1 finds 21 junctions, all
  unannotated; pass 2 reports the same 21 with `annotated=1` and higher unique counts
  (1,252 against 1,114) — as documented.
- **SAM/BAM record fields** (`verify/heldup_sam_tags.out`): recomputed independently for
  every primary and secondary record of 10,299 single-end reads (11,639 alignments) and
  9,600 paired-end reads (10,768 alignments) — `NH`, `HI`, MAPQ (255/3/1/0),
  `nM`, `NM`, `MD`, `AS` (matches − mismatches, `sjdbScore` +2 per annotated junction, 0
  / −4 / −8 for GT/AG / GC/AG / AT/AC and non-canonical, −2 − 2 × length per indel, the
  genomic-span log term, floored at 0), `jM`/`jI`, the pair flags, mate fields and TLEN,
  `XS` under `--outSAMstrandField intronMotif` (1,350 spliced records), and exactly one
  maximal-`AS` primary per read. **Discrepancies: none** on all three runs. The
  coordinate-sorted BAM is a permutation of the unsorted one in non-decreasing
  (reference, position) order with unplaced records last (12,140 and 22,636 records).
- **`--outFilterMultimapNmax`**: lowering it from 10 to 2 moves exactly the right reads —
  multi-mapped 823 → 307, too many loci 300 → 816, unique unchanged at 9,476 — and
  `ReadsPerGene.out.tab` and `Log.final.out` both follow (`heldup_genecounts.out`,
  `heldup_logfinal.out`).
- **`Log.final.out`** (`verify/heldup_logfinal.out`): all **27 statistics, 0 differing**,
  on three runs, including the splice breakdown by motif (1,080 GT/AG, 72 GC/AG, 86
  AT/AC, 100 non-canonical, 1,337 annotated of 1,338), the mismatch, deletion and
  insertion rates and average lengths, and every percentage. The denominators were
  checked explicitly and are printed in the output.
- **`--quantMode TranscriptomeSAM`** (`verify/heldup_transcriptome.out`): 11,189
  single-end and 20,748 paired-end records equal to the port record for record —
  transcript, position, strand and CIGAR — apart from ST1; `NH` equal to the number of
  transcript alignments for every read (0 violations); exactly one primary per read
  (0 violations); reads on more than one transcript (1,642 single-end) all emitted.

## Not audited

Chimeric and fusion detection (`--chimSegmentMin`, `Chimeric.out.junction`), the
splice-graph / super-transcript path, `--genomeTransformType Diploid` and the WASP
filter, VCF/variant handling, `--soloUMIdedup` collapsing and the EM multi-mapper
distribution, `--soloCellFilter` (EmptyDrops_CR), `Velocyto` counting, the read-clipping
options (`--clipAdapterType`, `--clip*pNbases`), shared-memory genome loading,
`--bamRemoveDuplicatesType`, signal/bedGraph output, long-read mode (`STARlong`), and
the seeding and stitching search itself — which was read but not verified against an
independent implementation, because reproducing STAR's alignment search independently is
out of scope for this audit. The numbers above test what STAR *reports* about the
alignments it found, not that it found the best ones.
