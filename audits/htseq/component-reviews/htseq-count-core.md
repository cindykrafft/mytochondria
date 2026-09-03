# Component: HTSeq counting core (`main` @ `7672321`, 2026-02-04, version string 2.1.2)

Read in full: `HTSeq/scripts/count.py` (528 lines), `HTSeq/scripts/count_features/
count_features_per_file.py` (466), `reads_io_processor.py` (187), `reads_stats.py`
(92), `HTSeq/scripts/count_with_barcodes.py` (746), `HTSeq/scripts/qa.py` (336),
`HTSeq/scripts/utils.py` (372), `HTSeq/features.py` (489), `HTSeq/__init__.py`
(1,249: `GenomicArrayOfSets`, the two pairers, `BAM_Reader`), `src/HTSeq/_HTSeq.pyx`
(2,095: `GenomicInterval`, `ChromVector`, `GenomicArray`, CIGAR parsing,
`SAM_Alignment`), `src/step_vector.h`, `src/StepVector.i`, `src/AutoPyObjPtr.i`,
`HTSeq/StepVector.py` (the SWIG wrapper), `HTSeq/_HTSeq_internal.py`, and
`doc/htseqcount.rst`, `doc/counting.rst`, `doc/history.rst`, the figure
`doc/images/count_modes.png`. Every suspect was **executed on the shipped code**:
`main` installed editable (Cython + SWIG build) into a Python 3.12 venv, the 2.1.2
wheel from PyPI (the latest release, same date as `main`'s HEAD) in a second venv, and
the 0.11.2, 0.12.4 and 0.13.5 sdists built on 3.12 in three more (see `../README.md`
for what that took). Harnesses are in `../verify/` with captured output; the reference
is an independent Python port of the documented semantics on synthetic BAM+GTF made
with pysam (`../verify/htseq_port.py`), evaluated by brute-force per-base enumeration.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### HC2 — CONFIRMED on `main`, 2.1.2, 0.13.5, 0.12.4 and 0.11.2 (executed); same line in 0.9.1 (by reading): a read pair whose mate is unmapped but present in the BAM is discarded as `__too_low_aQual`

**Code.** `_assess_pe_read` (`HTSeq/scripts/count_features/count_features_per_file.py:389-393`):

```python
    if (read_sequence[0] and read_sequence[0].aQual < minaqual) or (
        read_sequence[1] and read_sequence[1].aQual < minaqual
    ):
        read_stats.add_low_quality_read(read_sequence=read_sequence)
        return True
```

`aQual` is the record's MAPQ field (`_HTSeq.pyx:1864`) whether or not the record is
aligned, and every aligner writes MAPQ 0 on the record of an unmapped mate (STAR with
`--outSAMunmapped Within`, HISAT2, BWA, Bowtie2 defaults). So under the default `-a
10` the unmapped mate fails the cutoff and the pair is skipped. The comment above the
call site (lines 158-162) and the FAQ in `doc/htseqcount.rst:353-355` ("*What happened
if the mate of an aligned read is not aligned?* For the default mode "union", only the
aligned read determines how the read pair is counted") describe the opposite. The same
pair *is* counted when the unmapped record is simply not in the file: the pairer then
yields `(mate1, None)` and `None` short-circuits the test. `htseq-count-barcodes` has
the same comparison (`count_with_barcodes.py:309-310`). The lines are unchanged since
0.9.1 (`python3/HTSeq/scripts/count.py:236-237` in the 0.9.1 sdist).

**Verified** (`../verify/hc2_unmapped_mate_minaqual.py`, `.out` per version):

| case (mate 1 MAPQ 60 inside gene A) | `-a 10` (default) | `-a 0` |
|---|---|---|
| mate 2 unmapped, record in file (MAPQ 0) | `__too_low_aQual` | A |
| mate 2 absent from the file | A | A |
| both mates mapped | A | A |

On a 2,000-pair synthetic library with 113 one-mate-unmapped pairs: gene sum 1,887 and
`__too_low_aQual` 113 with the default, 2,000 and 0 with `-a 0` or with the unmapped
records stripped from the file, name- and position-sorted alike; all 20 genes differ
from the documented expectation. Identical numbers on 2.1.2, 0.13.5, 0.12.4 and 0.11.2
(the last with `-f bam`, that version's `-f` defaulting to `sam`). The random
brute-force harness (`../verify/heldup_bruteforce_random.py`) shows the same thing from
the other side: 162 of 324 CLI runs disagree with the documented port, every one of
them paired-end with `-a > 0`, and 0 of 324 disagree once the port models this one
rule. With the patch in `../upstream/` all pairs count (`.patched.out`).

**Who is exposed.** Paired-end data from an aligner that keeps unmapped mates, counted
with the default `-a`. STAR's default (`--outSAMunmapped None`) omits them and rarely
produces one-mate alignments, so STAR users are mostly unaffected; HISAT2, BWA and
Bowtie2 users with paired data are affected in proportion to their one-mate-unmapped
pairs (typically a few per cent of pairs, concentrated at gene ends and in
low-complexity regions). In the cohort 31 papers name paired-end data and 42 name
HISAT2/TopHat, 35 BWA/Bowtie (lower bounds; the cache cannot say which pairs). The
error is a systematic loss, similar across samples of one experiment, so it attenuates
counts more than it changes fold changes — but `__too_low_aQual` is often used as a QC
statistic, and here it is inflated by pairs that have nothing wrong with their MAPQ.

**Fix shape.** Check `aligned` before `aQual` for both mates (patch 0001 in
`../upstream/`, with a test that fails on `main`). This is a behaviour change for the
affected files (gene counts rise, `__too_low_aQual` falls), which the PR body flags.

### HC1 — CONFIRMED on `main`, 2.1.2, 0.13.5, 0.12.4 and 0.11.2 (executed); same line in 0.9.1 (by reading): `BAM_Reader[iv]` misses alignments whose last aligned base is `iv.start`

**Code.** `BAM_Reader.__getitem__` (`HTSeq/__init__.py:1065`):

```python
        for pa in self.sf.fetch(iv.chrom, iv.start + 1, iv.end):
```

`pysam.AlignmentFile.fetch(contig, start, stop)` takes 0-based half-open coordinates,
the same convention as `GenomicInterval` (`_HTSeq.pyx:36-42`), so the `+ 1` shifts the
window right by one base. An alignment ending at `iv.start + 1` (its last base is
`iv.start`) overlaps `iv` — `GenomicInterval.overlaps` (`_HTSeq.pyx:201-221`) says so
and pysam's own `fetch(iv.start, iv.end)` returns it — but `reader[iv]` does not
return it. This is the API path the TSS tutorial uses (`doc/tutorials/tss.rst:217,
250`: `sortedbamfile[window]`); `htseq-count` iterates the file and is not affected.

**Verified** (`../verify/hc1_bam_reader_interval_offset.py`, `.out` per version): the
minimal case returns 2 of the 3 overlapping reads; on 300 random windows over 2,000
random reads, 7 windows each miss one overlapping record and no non-overlapping record
is ever returned, every missed record ending exactly at `iv.start + 1`. (Part C's
±100 nt TSS profile happens to have no read ending at the window's first base, so the
two profiles coincide there; the defect is the 7 misses of part B.) Same output on
2.1.2, 0.13.5, 0.12.4 and 0.11.2; 0 misses with patch 0002.

**Fix shape.** Drop the `+ 1` (patch 0002 in `../upstream/`, with a test that fails on
`main`).

### N1 — NOTE (design, documentation): `--nonunique fraction` divides by the number of overlapping features, never by NH

`_update_feature_set_counts` (`count_features_per_file.py:236-239`): `val = 1.0 /
len(fs)` per alignment *record*. With the default `--secondary-alignments ignore` only
the primary record of a multimapper is seen, so the documented "the sum of all counts
will be equal to the number of reads" (`doc/htseqcount.rst:63-67`) holds for the
feature counts (190 = 190 reads in `../verify/note_nonunique_fraction_secondary.py`).
With `--secondary-alignments score` each of a multimapper's NH records contributes
1/len(fs), so the feature sum is 270 for 190 reads (40 multimappers × 3 records) and
`__alignment_not_unique` is 120; `random` behaves the same (270). featureCounts'
`--fraction` divides by NH; HTSeq's does not and the documentation does not say which.
Design choice; the docs' sum claim should be qualified.

### N2 — NOTE (design, quantified): in `htseq-count-barcodes` the special counters take part in the per-UMI majority vote

`count_with_barcodes.py:389-406` collapses the reads of one (cell, UMI) to one count by
`udic.most_common(2)`, discarding ties; `udic` also holds `__no_feature`,
`__alignment_not_unique`, `__too_low_aQual` and `__ambiguous`
(`count_with_barcodes.py:224, 237, 248, 286, 304, 314, 345, 351`). So a molecule with
one read uniquely in gene A and two reads outside any feature is counted as
`__no_feature`; one read in A and one multimapper is a 1:1 tie and the molecule is
discarded; two reads in A and three with MAPQ 0 count as `__too_low_aQual`
(`../verify/note_barcodes_umi_vote.py`: A = 2 where the "count the gene the assigned
reads support" rule of cellranger gives 5). Whether unassigned reads should veto a
molecule is a modelling decision; it is undocumented and differs from the tool the
script targets (`doc/htseqcount_with_barcodes.rst`). The cohort cache names
`htseq-count-barcodes` in no paper.

### N3 — NOTE (documentation): `doc/htseqcount.rst` says `--secondary-alignments` and `--supplementary-alignments` default to `score`; the code defaults to `ignore`

`count.py:379-394` (`default="ignore"` for both) vs `doc/htseqcount.rst:249-257`
("(default: ``score``)"). The change is in the history (`doc/history.rst`, 0.10.0:
"htseq-count ignores secondary and supplementary alignments by default", commit
`7be4fe3`, 2018-05-16) and in 0.9.1's `count.py:413` the default was indeed `score`,
so this is a documented behaviour change with a stale options page, not an undocumented
one; `--help` does not state the default either
(`../verify/note_cli_defaults_vs_docs.py`: one read with primary + secondary +
supplementary records in gene A counts 1 by default, 2 with `--secondary-alignments
score`, 3 with both). Open issue #94 asks what the two modes mean.

### N4 — NOTE (design, edge): a pair with one mate on a chromosome absent from the annotation is `__no_feature` as a whole

`_align_reads_to_feature_set` raises `UnknownChrom` on the first interval whose
chromosome has no feature vector (`count_features_per_file.py:272-273`) and the caller
files the unit under `__no_feature` (lines 182-183) even when the other mate lies in a
gene. With `--feature-query` (which leaves only one gene's chromosomes in the array) the
random harness's paired-end data show one such pair (G7 8 instead of 9,
`../verify/heldup_bruteforce_random.out`); the port agrees once the rule is modelled.
Union semantics would count the pair. Affects chimeric pairs onto unannotated contigs.

### N5 — NOTE (API, cosmetic): `GenomicInterval.overlaps` is asymmetric for zero-length intervals

`_HTSeq.pyx:218-221`: `[5,5).overlaps([3,10))` is `True`, `[3,3).overlaps([3,10))` is
`False` but `[3,10).overlaps([3,3))` is `True` (`../verify/heldup_genomicarray_intervals.py`,
part C: 133 of 20,000 random pairs differ from the per-base definition, all involving a
zero-length interval). Nothing in `htseq-count` builds zero-length intervals.

### N6 — NOTE (documented): mtx/h5ad/loom count matrices are float32

`count.py:100` passes `dtype=np.float32` to `_write_output`; a count of 2²⁴ + 1 is
stored as 2²⁴ (`../verify/note_cli_defaults_vs_docs.out`). Documented in
`doc/htseqcount.rst:270`; the TSV path prints exact integers. Only matters above
16.7 M reads on one feature in one sample.

### N7 — NOTE (design): `htseq-qa --primary-only` keeps supplementary records; a quality above `--maxqual` aborts

`qa.py:85-87` skips only `not_primary_alignment` (0x100), so a chimeric read with a
supplementary record counts twice (200 aligned records for 100 reads with
`primary_only=True`, `../verify/note_qa_statistics.out`); `_HTSeq.pyx:1401-1402` raises
`ValueError: Too large quality value encountered.` for a Q42 base under the default
`-m 41`. Both are choices the options page implies; the statistics themselves are right
(below).

## Withdrawn (own suspicions killed by execution)

- **W1** `ChromVector.apply` (`_HTSeq.pyx:574-577`) rewrites steps of the underlying
  `StepVector` while `steps()` is iterating the same C++ map; I suspected overlapping
  features could corrupt earlier sets. 406 random and deliberately abutting/nested
  intervals on both strands: every one of 36,000 bases and 2,400 point lookups equals
  the per-base dictionary (`../verify/heldup_genomicarray_intervals.py`, part A).
  `std::map` insertion does not invalidate iterators and `set_value` only erases keys
  behind the iterator.
- **W2** `pair_SAM_alignments_with_buffer` requires `-TLEN` of one mate to equal the
  other's and identical mate pointers (`HTSeq/__init__.py:555-565, 581-591`); I
  suspected mates on different chromosomes (TLEN 0), placed unmapped mates and
  supplementary records would fail to pair or pair wrongly. On 1,866 truth pairs
  including all of those, the position-sorted pairer and the name-sorted pairer both
  return exactly the truth multiset (part E). Aligners that write inconsistent TLEN
  signs would still be affected, but that is their inconsistency, and the script
  warns ("Mate records missing").

## What held up (executed, not just read)

- **The three overlap modes.** All eight rows of the documentation figure reproduce
  exactly for `union`, `intersection-strict` and `intersection-nonempty`, per row via
  the `XF` tag and in aggregate for `--nonunique none/all/fraction`, and equal the
  independent per-base port (`../verify/heldup_overlap_modes_figure.py`). On random
  data (260 GTF lines, 133 gene_ids on both strands with overlaps; 1,725 single-end
  records; 3,235 paired-end records forming 1,546 pairs and 143 lone mates, with
  soft clips, insertions, deletions, N gaps, MAPQ 0–255, NH 1/2/3, secondary and
  supplementary records, unmapped reads and mates, mates on different chromosomes)
  every one of 324 CLI configurations — 3 modes × `-s yes/no/reverse` × `--nonunique
  none/all/fraction` × 4 settings of `-a`/`--secondary-alignments`/
  `--supplementary-alignments`, name- and position-sorted — equals the port once HC2
  is modelled, and all 108 single-end runs equal the documented port outright
  (`../verify/heldup_bruteforce_random.py`). `--nonunique random` conserves counts
  (feature sum = unique + ambiguous in both orders). `-i gene_id -i gene_name` with
  `-t exon -t gene` and `--additional-attr` give the joined ids and the same counts;
  `--feature-query` restricts as documented (N4 aside).
- **Strandedness.** `yes` (mate 2 inverted), `reverse` (both inverted), `no`
  (strand ignored on an unstranded array) all equal the port above.
- **Special counters and their order.** `__not_aligned` (both mates), secondary and
  supplementary records silently skipped when ignored (they enter no counter, and
  the sum of counters is therefore short by them — as the code intends),
  `__alignment_not_unique` per record from NH > 1 (also with `--nonunique all`, before
  the MAPQ test, so low-MAPQ multimappers are counted there *and* in
  `__too_low_aQual`), `__too_low_aQual`, `__no_feature`, `__ambiguous[...]` — all
  equal the port on the random data.
- **Pairing.** `pair_SAM_alignments` (name order) and
  `pair_SAM_alignments_with_buffer` (position order) return the same multiset of
  pairs as the generator's truth on 1,866 pairs with multimappers, missing mates,
  placed unmapped mates and supplementary records (W2).
- **Interval arithmetic.** `GenomicArrayOfSets` on `auto` chromosomes, stranded and
  unstranded, equals a per-base dictionary (W1); `GFF_Reader` converts 1-based closed
  GTF and GFF3 to 0-based half-open exactly (`chr1 1 1` → `[0,1)`, `101 200` →
  `[100,200)`), `end_included=False` as documented, strand `.` carried through and
  rejected by a stranded array with the documented `ValueError`
  (`features.py:517-520, 806-810`); `StepVector` set/add equals a dense vector over
  3,000 random operations with contiguous, merged steps; `overlaps`/`contains`/
  `is_contained_in` equal the per-base definition for all non-empty intervals
  including the `.`-matches-either strand rule.
- **CIGAR handling.** `build_cigar_list` (`_HTSeq.pyx:1547-1584`) with pysam's
  operation codes in the right order; only M/=/X reference bases count, N/D bases and
  soft/hard clips do not — the port enumerates the same bases and agrees.
- **`htseq-qa` statistics.** Base composition by position and quality-by-position
  fractions equal a direct numpy computation to 0.0 on FASTQ and on BAM, with
  minus-strand records counted in sequencing orientation and aligned/unaligned split
  as documented (`../verify/note_qa_statistics.py`).

## Not audited here

`HTSeq/scripts/count_old.py` (not installed), `correct_barcodes` UMI collapsing beyond
reading it, the mtx/h5ad/loom writers and `--append-output`/`--with-header` (I/O),
`StretchVector`, `BigWig`/bedGraph readers and writers, `FastaReader`/`FastqReader`
beyond what `htseq-qa` exercises, the `VCF_Reader`, the doctest tutorials, and
multiprocessing (`-n`).
