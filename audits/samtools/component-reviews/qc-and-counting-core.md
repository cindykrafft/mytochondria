# Component: SAMtools QC and counting core (`develop` @ `ce612d2`, 2026-09-08, "samtools ce612d2 / Using htslib 1.24-1-ge503e04")

Read in full on `develop`: `stats.c` (2,965 lines; `samtools stats`), `bam_stat.c`
(346; `flagstat`), `bam2depth.c` (1,016; `depth`), `coverage.c` (737; `coverage`),
`bam_markdup.c` (2,657; `markdup`), `bam_plcmd.c` (1,360; `mpileup`), the counting
part of `bam_index.c` (`idxstats`), `sam_view.c` `process_aln` (`view -c` filters),
`stats_isize.c`, and `bam_mate.c` `calc_mate_score` (`fixmate -m`); in HTSlib
`develop` @ `e503e04`, `sam.c` `bam_plp_push` (depth cap), `tweak_overlap_quality` /
`overlap_push` (read-pair overlap removal) and `bam_plp64_next`. Every suspect was
**executed on the built binaries**: `develop` built here against HTSlib `develop`
(with the `htscodecs` submodule), the Ubuntu 24.04 package 1.19.2 (`apt-get install
samtools`), and 1.10 and 1.9 built from their release tags (the cohort's two most-cited
versions). Harnesses in `../verify/` build synthetic BAMs with pysam and compute every
truth independently in Python; captured outputs sit next to them.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### ST1 — CONFIRMED on `develop`, 1.19.2, 1.10 and 1.9: the `stats` coverage distribution wraps around a fixed ring buffer, so spliced alignments put their far exon's coverage next to the read start

**Code.** `samtools stats` accumulates the coverage distribution in `stats->cov_rbuf`, a
ring buffer of `size = 5 × nbases` `int`s — `nbases` starts at 300, so 1,500 cells for
reads up to 300 bp (`stats.c:2409`, `stats.c:778`). Cells are addressed relative to the
current read start by

```c
static inline int round_buffer_lidx2ridx(int offset, int size, hts_pos_t refpos, hts_pos_t pos)
{
    return (offset + (pos-refpos) % size) % size;      // stats.c:322-325
}
```

and `round_buffer_insert_read` (`stats.c:373-391`) increments `[from, to)` through that
map. The only guard is `to - from > size` (a single block longer than the buffer). Each
`M`/`=`/`X` block of a CIGAR is inserted separately (`stats.c:1489-1507`, and the `-t`
chunk path at 1455-1487), so a block that starts more than `size` positions after the
read start — the far exon of a spliced RNA-seq alignment — has `(pos - refpos) % size`
wrap and is added to the cells holding positions just after the read start. Those cells
are flushed into the `COV` histogram when later reads pass them
(`round_buffer_flush`, `stats.c:327-368`), so the histogram receives the far exon's
depth stacked onto the near exon's, and the far exon's positions are never counted.
The same buffer feeds `SN percentage of target genome with coverage > N (%)` under
`-t`/`-g` (`stats.c:1642-1647`). With 100-bp reads the threshold is an intron of about
1.4 kb; most human introns are longer.

**Verified** (`../verify/st1_stats_cov_ringbuffer.py` and `.out` files; identical on
all four builds):

| case | truth `COV` | samtools `COV` |
|---|---|---|
| A: `50M` at 1 + `50M1450N50M` at 1 | depth 1 × 50, depth 2 × 50 | **depth 3 × 50** |
| A2: same with `50M1000N50M` (block inside the buffer) | depth 1 × 50, depth 2 × 50 | depth 1 × 50, depth 2 × 50 |
| B: six-exon gene, 3,000 100-bp spliced reads (introns 0.3–12 kb) | 2,197 covered positions, mean depth 136.55, median 142, max 172 | **2,591 covered positions, mean 115.79, median 134, max 168** |
| C: `-t` exon list, `-g 0/5/10/20` | 99.86 / 99.50 / 99.14 / 98.73 % | **117.77 / 116.41 / 115.14 / 112.18 %** |

The sum of depth over positions is preserved (300,000 in B): coverage is moved, not
lost, which is why a percentage above 100 % is possible. Same output on 1.9, 1.10 and
1.19.2 (`.v1.9.out`, `.v1.10.out`, `.v1.19.2.out`); every case matches truth with the
patch below (`.patched.out`).

**Who is exposed.** Anyone running `samtools stats` on a spliced alignment (STAR,
HISAT2, minimap2 `-x splice`) and reading the `COV` section, plot-bamstats'
coverage plot, or the `-t`/`-g` target percentage. 166 cohort papers name RNA-seq or
splicing alongside samtools; 3 name `samtools stats` explicitly (cache lower bound).
The `SN` numbers that MultiQC tabulates (reads mapped, error rate, insert size, …) do
not go through this buffer and are unaffected (held up below).

**Fix shape.** Grow the buffer when a block would reach beyond it (doubling,
linearising the pending counts); `../upstream/0001-*.patch`, 39 lines in `stats.c`
plus two regression tests and a NEWS entry. Memory becomes proportional to the longest
read-start-to-block-end span.

**Upstream.** No prior report: searched 2026-09-08 for the coverage distribution with
spliced/RNA-seq/long reads, the target percentage above 100 %, and the ring buffer;
nearest #1003 (open: GC-depth off for long reads — a different `stats` buffer),
#640 and #969 (closed: `-t` and `-p` coverage), #875 (closed: `-t` segfault).

### ST2 — CONFIRMED on `develop`, 1.19.2, 1.10 and 1.9: reallocating the buffers for a longer read copies the pending coverage with byte lengths where element counts are needed

**Code.** When a read's unclipped length reaches `nbases` (300 at first),
`realloc_buffers` grows every per-cycle array and re-creates the coverage ring
(`stats.c:766-778`):

```c
int *rbuffer = calloc(sizeof(int),seq_len*5);
n = stats->cov_rbuf.size-stats->cov_rbuf.start;
memcpy(rbuffer,stats->cov_rbuf.buffer+stats->cov_rbuf.start,n);        // n is a count of ints
if ( stats->cov_rbuf.start>1 )
    memcpy(rbuffer+n,stats->cov_rbuf.buffer,stats->cov_rbuf.start);     // start is a count of ints
```

Both `memcpy` lengths are cell counts, so only a quarter of the intended cells are
copied and the rest of the new buffer stays zero. The loss is visible whenever the
pending window sits near the end of the ring at the moment a new maximum read length
arrives (and the `start>1` test should be `start>0`).

**Verified** (`../verify/st2_stats_cov_realloc.py`): ten 100-bp reads at 1401–1446
followed by a 350-bp read at 1451: truth `COV` has 50 positions at depth 11 and 260 at
depth 1; samtools reports 10 at depth 11 and 300 at depth 1 (case D). The same reads
with the long read first (nothing pending) are right (D2). Two hundred reads with
lengths growing from 1 to 20 kb (long-read style, every new maximum reallocates) lose
1,546 of 2,190,000 depth units (E). Same on 1.9, 1.10, 1.19.2; correct with the patch.
Illumina data of one fixed length never reallocates with anything pending (the first
read triggers it on an empty buffer), so this is a mixed-length and long-read defect.

**Fix.** Covered by the same patch (`round_buffer_resize` copies with
`sizeof(int)`).

### N1 — NOTE, verified: `stats -p` misses the overlap when mates have different lengths

`remove_overlaps` (`stats.c:1095-1102`) sends a read straight to the coverage buffer,
bypassing the pair hash, when `|TLEN| >= 2 × l_qseq` — "cannot overlap its mate" —
using the read's own length for both mates. With adapter-trimmed pairs of unequal
length the shorter mate takes that exit while the longer one waits in the hash, so the
overlap is counted twice in `bases mapped (cigar)` and in `COV`
(`../verify/note_stats_overlap_unequal_mates.py`): 150/90-bp mates with a 200-bp insert
give `bases mapped (cigar)` 48,000 for 200 pairs where the once-counted truth is 40,000
(equal 100/100-bp mates are handled correctly: 30,000 = truth). `-p` is a non-default
option; the correct test is `|TLEN| >= l_qseq + mate length` (the `MC` tag or
`bam_cigar2qlen` of the mate is not at hand, but `mpileup`'s `overlap_push` in HTSlib
adds `mpos >= end` to the same heuristic, which closes this case). No prior issue
(nearest #1036/#986, about `mpileup`'s separate overlap code).

### N2 — NOTE, verified, documentation: `reads duplicated` counts supplementary records, `sequences` does not

`collect_stats` counts `IS_DUP` before the `IS_ORIGINAL` gate (`stats.c:1254-1258` vs
1280), while `sequences`, `1st fragments` and `total length` exclude supplementary
records ("excluding supplementary and secondary reads", `stats.c:1596`). After
`markdup -S` or Picard, which flag supplementary records of duplicates, `reads
duplicated / sequences` — the ratio MultiQC and several pipelines print — overstates
the duplication rate: 25.0 % vs 20.0 % on a file where a quarter of the pairs carry a
supplementary record (`../verify/note_stats_counts_semantics.py`). `flagstat` prints
both numbers (`duplicates`, `primary duplicates`); `stats` prints only the wider one.

### N3 — NOTE, verified, minor: the insert-size standard deviation skips bin 0

`output_stats` sums `(isize − mean)²` from `isize = 1` (`stats.c:1576`) while the mean
and the denominator include bin 0. Same-chromosome pairs with `TLEN` 0 (an aligner
convention for some non-proper pairs) therefore pull the mean down but not the SD up:
1,000 pairs of which 100 have `TLEN` 0 give SD 36.6 where the population SD over the
same pairs is 100.8 (`../verify/note_stats_counts_semantics.py`). Rare in practice.

### N4 — NOTE, verified: `depth -s` keys overlap removal on the read name only, so supplementary records break it

`bam2depth.c:599-626` stores the first-seen record's end under its `QNAME` and clips
the next record with the same name. Supplementary records are not in the default
exclusion list (`bam2depth.c:744`), so a supplementary alignment of read 1 sorting
between the mates is clipped to nothing and consumes the entry; the mate then re-enters
the hash and the real overlap is counted twice (`../verify/note_depth_s_supplementary.py`:
positions 161–200 at depth 2 instead of 1, positions 121–150 at depth 1 instead of 2).
`-G 0x800` avoids it. `-s` is a non-default option.

### N5 — NOTE, verified, documentation: `coverage --rf` means "any of the bits", `depth --require-flags` means "all"

`coverage.c:188` keeps a read when `flag & required_flags` is non-zero; the man page
says "skip reads with mask bits unset". `depth --require-flags` and `view -f` require
all bits (`bam2depth.c:558`, `sam_view.c:171`); `mpileup --rf` is documented as
any-of. `--rf 0x42` on a mixed file selects 40 reads in `coverage` and 10 in `depth`
(`../verify/note_coverage_rf_semantics.py`).

### N6 — NOTE, design (by reading, acknowledged in the source): mismatches per cycle with `-r` ignore `N` operations

`count_mismatches_per_cycle` (`stats.c:513-515`) skips `N` without advancing the
reference pointer ("Not very frequent and not noticeable in the stats", a 2012
comment), so with `-r` the far exon of a spliced read is compared against the
reference immediately following the near exon. `MPC` rows on spliced RNA-seq BAMs with
`-r` are therefore not mismatches per cycle. Not executed (needs a reference; the
comment states the behaviour); `-r` is uncommon and `MPC` is a plot input.

### Withdrawn suspicions (own, killed by execution)

- W1: `mpileup` depth with the default overlap removal would drop bases whose
  quality was halved — no: matching bases keep the *sum* of both qualities on one
  mate, mismatching ones keep 0.8 × the higher; the Python port of
  `tweak_overlap_quality` matches the depth column at every position.
- W2: `markdup`'s optical distance uses only the original-vs-duplicate distance — no:
  `check_duplicate_chain` compares every pair within a duplicate group; 175/175 `dt:SQ`
  in the harness.
- W3: `flagstat` percentages lose precision through `(float)n / total` — the float
  has 24 mantissa bits, the printed value 2 decimals; below the display resolution for
  any file (by arithmetic, not executed).

## What held up (executed, not just read)

- **`flagstat`** (`../verify/heldup_flagstat_idxstats_view.py`): all 16 lines,
  QC-passed and QC-failed columns, equal a Python port of the SAM-flag definitions on
  4,244 records covering proper/improper pairs, singletons, unmapped pairs,
  duplicates, QC-fail, secondary and supplementary records; the `tsv` and `json`
  outputs carry the same numbers. Denominators as documented: `mapped %` over all
  records, `primary mapped %` over primary, `properly paired %` and `singletons %`
  over paired-in-sequencing primary records; `mapQ>=5` applied to the read's own MAPQ.
- **`idxstats`**: the indexed path and the streaming path agree with the truth on
  three contigs plus `*`; unmapped-but-placed mates count under their placement
  contig, unplaced ones under `*`.
- **`view -c`**: 15 filter combinations (`-q`, `-f`, `-F`, `--rf`, `-G`, `-m`, four
  `-e` expressions on flags/tags/MAPQ/qlen/rname/tlen, a region) equal Python counts.
- **`depth`** (`../verify/heldup_depth_coverage.py`): default, `-a`, `-J`, `-q 20`,
  `-Q 20`, `-q 30 -Q 40`, `-g DUP`, `-G SUPPLEMENTARY`, `-l 100`, `-s`, `-s -q 30`, `-r`
  and two input files all equal per-position Python truth (0 mismatching positions
  over 30,000) on 1,500 reads with insertions, deletions, 200/2,000-bp `N` skips,
  soft/hard clips and every filtered flag plus 400 overlapping pairs. Deletions count
  only with `-J`, `N` never, insertions never; `-l` measures aligned query bases
  without soft clips (the 2021 rewrite's documented change); no depth cap (`-d`
  ignored since 1.13, as documented).
- **`coverage`**: `numreads`, `covbases`, `coverage`, `meandepth`, `meanbaseq`,
  `meanmapq` equal Python truth at the printed precision for the default, `-q`, `-Q`,
  `-q -Q`, `-l`, `--ff`, `--min-depth 3` and `-r`. `meanbaseq` averages over counted
  bases only; `-l` measures `bam_cigar2qlen` (soft clips included, unlike `depth -l`).
- **`stats` SN** (`../verify/heldup_stats_sn.py`): 31 summary numbers — read counts by
  class, bases mapped and bases mapped (cigar), mismatches and error rate, average and
  maximum length, average quality, insert size average and standard deviation under the
  99 % main-bulk rule, inward/outward/other pairs, pairs on different chromosomes,
  percentage of properly paired reads — equal a Python port on a 4,000-read library
  with a long insert tail, under no filter, `-F 0x600`, `-d` and `-f 0x2`. The
  insert-size rule is as documented: each pair once, `-i 8000` cap, mean and
  population SD over the smallest set of bins holding more than 99 % of pairs.
- **`markdup`** (`../verify/heldup_markdup.py`): after `fixmate -m` and `sort`,
  `PAIRED`, `SINGLE`, `DUPLICATE PAIR`, `DUPLICATE SINGLE`, `EXAMINED`, `READ`,
  `DUPLICATE TOTAL` and `ESTIMATED_LIBRARY_SIZE` (Picard's bisection on
  `c/x − 1 + exp(−n/x)`, ported) equal truth on 600 fragments with 1–5 copies through
  differing soft clips; exactly one record per group stays unmarked and it has the
  highest sum of qualities ≥ 15; `flagstat` after `markdup` agrees; `-S` marks exactly
  the supplementary records of duplicate-marked reads (keyed on the `SA` tag);
  `-d 100` with Illumina-style names classifies 175/175 optical and 156/156 library
  duplicates (`dt:SQ`/`dt:LB`) and the library-size estimate excludes the optical
  pairs as Picard does.
- **`mpileup`** (`../verify/heldup_mpileup.py`): the depth column equals Python truth
  at every position under the defaults (`-Q 13`, overlap removal on), `-x`, `-x -Q 0`,
  `-x -Q 30`, `-Q 30`, `-x -q 30`, `-x --ff UNMAP,SECONDARY` and `-x -B -f ref.fa`;
  the port of HTSlib's `tweak_overlap_quality` (sum of qualities on one mate for
  agreeing bases, 0.8 × the higher for disagreeing) reproduces the default; a deleted
  or skipped position counts when the read's next base passes `-Q`; the `-d 8000`
  default caps 10,000 stacked reads at 8,000, `-d 0` removes the cap; BAQ (default when
  `-f` is given) changes the depth at 301 of 19,838 positions near indels and
  mismatches, as designed.

## Not audited

`sort`/`merge` ordering, `fixmate` beyond the `ms` score, `calmd`, `consensus`,
`ampliconclip`/`ampliconstats`, `bedcov`, `stats` GC-depth (`GCD`, open upstream as
#1003 for long reads), the `GCF`/`GCL`/`GCC` and per-cycle tables, `stats -r`
mismatches per cycle (N6 by reading), BAQ's arithmetic (`sam_prob_realn`), CRAM
paths, `view --subsample`, `markdup --barcode-*`/read-group modes and `-m s`.
