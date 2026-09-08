# Component: featureCounts read-to-feature assignment (`master` @ `55dc154`, 2023-07-30, v2.0.6; release 2.1.1)

Read in full: `src/readSummary.c` (9,410 lines on `master`) — `process_line_buffer`
(the per-fragment filter chain and hit search, `:2924-3482`), `vote_and_add_count`
(the overlap scoring, `-O`, `--largestOverlap`, `--minOverlap`/`--fracOverlap`/
`--nonOverlap`/`--fracOverlapFeature` filters and the count increments,
`:4611-5059`), `calc_score_overlaps` (`:4576-4608`), `calc_total_frag_len` and
`parse_bin` (fragment length with soft clips and insertions; CIGAR sections; NH
tag, `:2119-2549`), `load_feature_info` and `sort_feature_info` (GTF/SAF parsing,
feature blocks and the reverse index, `:975-1686`), `calculate_multi_overlap_fraction`
/`calc_fixed_fraction`/`calc_float_fraction` (`:1701-1721`), the count and summary
writers (`:6933-7298`), `readSummary` and `main` (option wiring, `:7977-9408`);
`src/input-files.c` — the read pairer (`SAM_pairer_get_read_full_name`,
`SAM_pairer_do_one_BIN`, `SAM_pairer_do_read_test`, `:3534-3949`);
`src/HelperFunctions.c` — `GTF_extra_column_value` (`:510-640`); and
`doc/SubreadUsersGuide.tex` §"featureCounts" (`:803-1095`) as the statement of
intended behaviour.

Every suspicion was **executed on the built binary**: `make -f Makefile.Linux
featureCounts` on `master` (prints `v2.0.6`), and on the SourceForge source
tarballs of **2.1.1** (the latest release; `src/readSummary.c` dated 2025-04-16,
users guide "Rsubread v2.22.1/Subread v2.1.1"), **2.0.3** and **2.0.1** (the
cohort's most-cited version; needs `-fcommon` with a modern gcc). Harnesses in
`../verify/` write synthetic BAMs with pysam and compare the count table, the
`.summary` and the `-R CORE` per-read status with `fcref.py`, an independent
implementation of the users guide's rules. Note that GitHub `master` (2.0.6) is
*behind* the release channel: the maintainers publish on SourceForge and
Bioconductor and push to GitHub in bulk (50 commits in total, e.g. "sync code
with Rsubread latest version"); the assignment functions differ between `master`
and 2.1.1 only in buffer-clearing details (`diff -w` of `process_line_buffer`,
`vote_and_add_count`, `parse_bin`, `calc_total_frag_len`, `calc_score_overlaps`:
0-20 changed lines, none in the decision logic), and every result below was
reproduced on the 2.1.1 build.

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### FC1 — CONFIRMED on `master` (2.0.6), 2.1.1, 2.0.3 and 2.0.1: `--splitOnly` does not exclude singleton fragments in read-pair mode

**Code.** In `-p --countReadPairs` mode `process_line_buffer` walks the two
records of a fragment. A record that is unmapped leaves the loop at
`readSummary.c:3134` (`if(SAM_FLAG_UNMAPPED & alignment_masks) continue;`),
*before* the `--splitOnly` test at `:3190-3206`, which increments
`skipped_for_exonic` for a mapped non-split record and drops the fragment only
when the counter reaches `1 + is_paired_end_mode_assign` = 2. A fragment with
one mapped, non-split record and an unmapped mate reaches 1 and is counted; so
does a single-end record inside a paired-end file, whose missing mate the pairer
replaces with an unmapped placeholder (`parse_bin`, `:2504-2548`, via
`reverse_flag`). The users guide (`SubreadUsersGuide.tex:1089`) says: "only split
alignments (CIGAR strings contain letter 'N') will be counted. All the other
alignments will be ignored." `--nonSplitOnly` (`:3209-3220`) tests each mapped
record directly and is right.

**Verified** (`../verify/fc1_splitonly_pe_singletons.py`, `.out`, `.v2.1.1.out`,
`.v2.0.3.out`, `.v2.0.1.out`, `.patched.out`; `../upstream/mcve_outputs.txt`):

| case (`-p --countReadPairs --splitOnly`) | manual | `master`, 2.1.1, 2.0.3, 2.0.1 (`-p`) | patched |
|---|---|---|---|
| proper pair, both ends non-split | Unassigned_NonSplit | Unassigned_NonSplit | Unassigned_NonSplit |
| proper pair, one end split | Assigned | Assigned | Assigned |
| mapped non-split read, mate unmapped (record present) | Unassigned_NonSplit | **Assigned** | Unassigned_NonSplit |
| mapped split read, mate unmapped | Assigned | Assigned | Assigned |
| single-end non-split record in the paired-end file | Unassigned_NonSplit | **Assigned** | Unassigned_NonSplit |
| 1,000 non-split singletons + 200 non-split pairs in one gene | count 0 | **1,000** (1,000/1,000 singletons Assigned, 0/200 pairs) | 0 |
| same fragments, `-p --splitOnly` (read-level counting) | — | 0 (every non-split record Unassigned_NonSplit) | — |

**Who is exposed.** Users of `--splitOnly` with fragment counting on libraries that
contain singletons (any aligner that keeps a mapped read whose mate failed, or a
BAM with unpaired reads). The cohort cache names `--splitOnly` in 0 papers; the
option serves junction/exon-inclusion analyses. Not default, not common: **held**.

**Fix shape** (`../upstream/0001-featureCounts-apply-splitOnly-to-singleton-fragments.patch`):
count an unmapped record as a non-split record in read-pair mode before the
`continue`, and move the `Unassigned_NonSplit`/`Unassigned_Split` bookkeeping
into one helper. Adds `test/featureCounts/data/corner-SPLITONLY.{sam,ora}` and a
line in `test_corner_cases.sh` (expected `simu_gene1 = 3`; unmodified `master`
gives 8 and the test prints FAILED); the whole `featureCounts-test.sh` suite
passes with the patch (0 FAILED of 38 + 12 comparisons) and the random battery is
unchanged except for the `--splitOnly` set (`heldup_bruteforce_random.patched_fc1.out`).

### FC2 — CONFIRMED on `master` (2.0.6), 2.1.1 and 2.0.3; **2.0.1 unaffected** — the documented "read type" filter was removed in 2.0.2 while its summary row stayed: single-end reads in a paired-end file are counted under stranded pair counting as first reads

**Code.** `fc_read_counters.unassigned_read_type` is declared (`readSummary.c:114`),
merged (`:6136`, `:6197`, `:6212`) and printed as the summary row
`Unassigned_Read_Type` (`:7207`), but no line increments it. A record without the
paired flag in a run with `-p` sets `this_is_inconsistent_read_type` (`:2983-2991`);
the only consequence is `Unassigned_Singleton` under `-B` (`:3031-3044`). The
record is then paired with an unmapped placeholder mate and its own strand is
taken as the fragment strand — the first-read rule at `:3170-3180`. The users guide
(`SubreadUsersGuide.tex:935-937`) says the opposite: "if there are single end
reads included in a paired end read dataset ... and reads are required to be
counted in a strand-specific manner, then all the single end reads will be
excluded from counting because their strandness cannot be determined", and lists
`Unassigned_Read_Type` among the output rows (`:967`). Release 2.0.1 implemented
exactly that (`subread-2.0.1-source/src/readSummary.c:2911-2921`:
`if(this_is_inconsistent_read_type){ if(global_context -> is_strand_checked){ ...
unassigned_read_type++; return; }`); commit `1f24de1` (2021-03-29, "latest changes
to Subread, matching the subread-2.0.2 release") deleted that branch and kept
the counter. The same sentence is in the 2.0.1, 2.0.3, 2.1.1 and `master`
manuals.

**Verified** (`../verify/fc2_read_type_stranded.py` and `.out`, `.v2.1.1.out`,
`.v2.0.3.out`, `.v2.0.1.out`, `.patched.out`): gene S on `+` and gene AS antisense
to it on `−`; 300 dUTP pairs from S (R1 reverse, R2 forward) plus 500 orphaned
first reads (single-end records, reverse) and 500 orphaned second reads
(single-end, forward), all from S:

| run | manual | `master`, 2.1.1, 2.0.3 | 2.0.1 (`-p -s ...`) | patched |
|---|---|---|---|---|
| `-p --countReadPairs -s 2` | S = 300, AS = 0, Read_Type = 1,000 | **S = 800, AS = 500**, Read_Type = 0 | S = 300, AS = 0, Read_Type = 1,000 | S = 300, AS = 0, Read_Type = 1,000 |
| `-p --countReadPairs -s 1` | S = 0, AS = 300, Read_Type = 1,000 | **S = 500, AS = 800**, Read_Type = 0 | S = 0, AS = 300, Read_Type = 1,000 | as 2.0.1 |
| `-p --countReadPairs -s 0` | all ambiguous (S and AS overlap) | 1,300 Unassigned_Ambiguity | same | same |
| `-p --countReadPairs -s 2 -B` | Singleton 1,000 | S = 300, Singleton = 1,000 | same | same |

The 500 orphaned second reads land on the antisense gene under `-s 2` (the
protocol most cohort papers use) because an orphan carries no first/second flag
and is read as a first read. The random battery on 2.0.1
(`heldup_bruteforce_random.v2.0.1.out`) shows the same thing from the other side:
all 26 status differences under `-s 1`/`-s 2` are single-end records that 2.0.1
labels `Unassigned_Read_Type` and `master` assigns.

**Who is exposed.** Stranded fragment counting (`-s 1`/`-s 2` with `-p`) of BAMs
that mix paired and unpaired records — HISAT2 or Bowtie 2 runs given both `-1/-2`
and `-U` after trimming, merged BAMs, or BAMs from which one mate was filtered.
STAR writes only pairs, so the common STAR → featureCounts path is not affected.
The cohort cache has 19 papers naming stranded counting and 49 naming paired-end
counting; whether any BAM was mixed cannot be decided from the cache. Not default:
**held**, and because the maintainers may have removed the filter on purpose
(the manual would then be what needs changing), the issue text asks that question
first.

**Fix shape** (`../upstream/0002-featureCounts-restore-the-read-type-filter-for-stran.patch`):
restore the 2.0.1 branch at the point where the inconsistent read type is
detected, with the counter routed through the read-group tables and the scRNA
pool like its neighbours; it fires whenever `-p` is combined with `-s 1`/`-s 2`
(fragment and read-level counting). Adds `corner-READTYPE.{sam,ora}` (four proper
pairs and four single-end records inside a `+` gene, `-p --countReadPairs -s 1`;
expected 4, unmodified `master` gives 6, FAILED); full suite passes with the patch.

### N1 — NOTE (documentation, summary rows only): in read-pair mode a fragment that fails two filters is not labelled by the manual's first filter

`SubreadUsersGuide.tex:919-932` lists the order unmapped > read type > singleton >
mapping quality > chimeric > fragment length > duplicate > multi-mapping >
secondary > split and says a fragment "will only be allocated to ... the first
filter that filtered this alignment out". The code applies the mapping-quality
test only while looking at the second record of the pair (`readSummary.c:3046-3065`,
`max(first_read_quality_score, mapping_qual)`), after the chimera/fragment-length
tests (`:3067-3112`) and the first record's duplicate, NH, secondary and split
tests; and the "first" record is the one the pairer meets *later* in the file
(`input-files.c:3866-3870`, `:3916-3918`: the stored mate is passed second).
Executed (`../verify/note_filter_order_pe.out`): low-MAPQ pairs that are also
multi-mapping / duplicate / chimeric / over-length / secondary are labelled
`Unassigned_MultiMapping` / `_Duplicate` / `_Chimera` / `_FragmentLength` /
`_Secondary` instead of `Unassigned_MappingQuality`. Counts are unaffected — the
random battery (`heldup_bruteforce_random.out`) reproduces every label once the
walk order is modelled (`fcref.assign(..., code_order=True)`).

### N2 — NOTE (design, undocumented): features with strand `.` are never counted under `-s 1` and always counted under `-s 2`

A feature's strand is stored as 0 (`+`), 1 (`−`) or −1 (`.`, `readSummary.c:1150`,
`:1236`); `-s 1` requires equality with the fragment strand and `-s 2`
inequality (`:3387-3393`), so `−1` fails every `-s 1` test and passes every
`-s 2` test. Executed (`../verify/note_unstranded_features.out`): 10 forward + 10
reverse reads in each of a `+`, a `.` and a `−` feature give `-s 1`: 10/0/10 and
`-s 2`: 10/20/10. Strandless features occur in SAF files written without a strand
and in some ncRNA/repeat annotations; the manual does not say what happens to
them. Design choice; documenting it (or treating `.` as "count both strands" in
both modes) is the maintainers' call.

### N3 — NOTE (summary only): with `--byReadGroup` the reads dropped by `-Q` are attributed to no read group

Every other filter increments the read group's own counter through
`get_RG_tables`; the mapping-quality branch increments only
`thread_context->read_counters.unassigned_mappingquality` (`readSummary.c:3051`).
Executed (`../verify/note_byreadgroup_mapq.out`): 40 reads in two groups, 10 with
MAPQ 0, `--byReadGroup -Q 10 --ignoreDup`: each group's column shows Assigned 13,
Duplicate 2, MappingQuality 0 — 15 of 20 reads. Counts are right; the per-group
summary does not sum to the input.

### N4 — NOTE (behaviour change, documented in the 2.0.2 help text but not in the manual's version history): `featureCounts -p` counts fragments in 2.0.1 and reads in 2.0.3+

Executed (`../verify/note_p_semantics_versions.*.out`): 500 proper pairs over two
overlapping genes; `-p` gives A = 329, B = 171 (500 assigned) on 2.0.1 and A = 636,
B = 305 (941 assigned, 59 ambiguous) on 2.0.3, 2.0.6 and 2.1.1, which give the
2.0.1 numbers only with `-p --countReadPairs` (an option 2.0.1 rejects). The
cohort's most-cited version is 2.0.1 (41 papers) and 2.0.x is the largest family
(69); a pipeline written for 2.0.1 and rerun on a newer build silently doubles
its counts. Recorded because it matters for reproducing published numbers; it is
documented in the option help, so not a finding.

### N5 — NOTE (documentation): `-C` also drops same-chromosome pairs whose mates are on the same strand

`readSummary.c:3080-3110`: a pair is checked for fragment length only when
`mate_chr == read_chr && strand(R1) != strand(R2)`; otherwise, with `-C`, it is
`Unassigned_Chimera`. The option help (`SubreadUsersGuide.tex:1006`) describes
`-C` as "fragments that have their two ends aligned to different chromosomes";
the output section (`:970`) says "different chromosomes or have unexpected
orientation". The random battery models the second definition and matches
(15 % of its pairs are same-strand). Design choice; the option text is incomplete.

### N6 — NOTE (behaviour change between 2.0.3 and 2.0.6): `--largestOverlap` with `-O --fraction` divides by a different number of targets

The 15 Feb 2023 comments in `vote_and_add_count` (`readSummary.c:4838`, `:4924`)
make "largest overlap" a filter step before the `-O` fraction is computed. On
2.0.3 and 2.0.1 the same battery gives, for `-O --fraction --largestOverlap
--minOverlap 10` and `-f -O --fraction --largestOverlap`, fractions such as 1.17,
2.67 and 3.83 where `master`/2.1.1 (and the documented rule "1/y where y is the
number of features overlapping with the read" after the largest-overlap
selection) give whole numbers (`heldup_bruteforce_random.v2.0.3.out`,
`.v2.0.1.out`: 27-68 count differences per set, 0 status differences). Rare
option combination; recorded for version scope.

### N7 — NOTE (reporting): in feature-level mode (`-f`) the count table names every row by the `gene_id` attribute and the `-R CORE` target column carries the gene, not the exon

`load_feature_info` overwrites the `LINE_%07u` feature name with the value of `-g`
(`readSummary.c:1196`, `:1243`), and `write_read_details_FP` is always called with
`gene_name_array[exontable_geneid[exon]]` (`:4632-4634`, `:4969-4971`). With a GTF,
`-f` output rows are therefore identified only by position (Chr/Start/End), and a
CORE report cannot say which exon a read went to. The harness keys `-f` rows by
row index for that reason. Documented as "feature identifiers are assumed to be
unique" (`SubreadUsersGuide.tex:816`); worth a sentence in the `-f` help.

### N8 — NOTE (minor): a GTF attribute key that occurs twice yields its last value

`GTF_extra_column_value` (`HelperFunctions.c:510-640`) keeps scanning after a match,
so `gene_id "G5"; gene_id "G5b";` gives `G5b` (`../verify/heldup_misc.out`, item 4).
Keys are matched as whole tokens (`ref_gene_id` does not match `gene_id`),
unquoted `key=value` pairs work, and values keep internal spaces.

## Withdrawn (own suspicions that execution killed)

- **W1 — `--fracOverlap`/`--nonOverlap` on singleton fragments.** The first battery
  flagged 7 fragments with one unmapped mate as wrongly `Unassigned_Overlapping_Length`.
  Isolating them and varying every field showed featureCounts right (a 36-nt read
  overlapping 23 bases of an exon fails `--nonOverlap 5`); the reference's single-mate
  branch returned a fragment length of 0. Fixed in `fcref.fragment_length`, withdrawn.
- **W2 — `-Q`/`--ignoreDup` labels in read-pair mode.** The remaining label
  differences were the pairer's record order (the later record in the file is
  walked first). Modelled; the residue is N1.
- **W3 — the reverse index missing long features.** `sort_feature_info` builds
  feature blocks per 131,072-base bucket and registers each block in every bucket
  it spans (`readSummary.c:1386-1400`), so a read inside a long feature finds it
  from any bucket; the battery's genes span up to ~4 kb and the pairer harness's
  up to 3 kb, and the 179,309-record run found every hit the reference found. Not
  a finding; noted as checked only up to those sizes.
- **W4 — automatic `chr` prefix matching.** `process_line_buffer:3335-3345`
  looks a BAM name up without its `chr` prefix, or with `chr` added, when the
  annotation name is absent. A first harness case reported no match, but the
  read had been placed outside the gene; with the read inside, both directions
  (annotation `1`/BAM `chr1`, annotation `chr1`/BAM `1`) assign the read
  (`heldup_misc.out` item 6). An undocumented convenience, not a finding.

## What held up (executed, not just read)

- **The documented assignment rules, end to end.** `heldup_bruteforce_random.py`
  (seeds 1-3; `.out`, `.seed2.out`, `.seed3.out`): a random two-chromosome
  annotation (43-49 genes of 1-4 exons, overlapping and antisense genes, `.`
  strands, duplicated exon lines) and, per seed, 400 single-end fragments (622
  records: unmapped, soft-clipped, split, indel, NH 2-3 with secondary flags,
  duplicates, MAPQ 0-255) and 400 paired-end fragments (1,036 records: pairs,
  one-mate-unmapped, single-end records, chimeric, same-strand, multi-mapper pairs
  with HI tags), compared with `fcref.py` under 31 single-end option sets, 36
  read-pair option sets and 8 read-level (`-p` alone) sets: default, `-O`, `-s 1/2`,
  `-M`, `-M --fraction`, `--primary`, `-M --primary`, `-O --fraction`,
  `-M -O --fraction`, `-Q`, `--ignoreDup`, `--splitOnly`, `--nonSplitOnly`,
  `--minOverlap`, `--fracOverlap 0.5/1`, `--largestOverlap` (± `-O`),
  `--nonOverlap`, `--fracOverlapFeature`, `--nonOverlapFeature`, `-f` (± `-O`,
  `--fraction`, `--largestOverlap`), `--read2pos 5/3`, `--readExtension5/3`, `-B`,
  `-C`, `-P -d -D`, and combinations. Result on `master`: **75 of 75 option sets
  per seed with 0 status/target and 0 count differences**, and the summary rows
  sum to the number of fragments in every run (with the N1 walk order and the FC1
  singleton rule modelled explicitly). Same on 2.1.1 (75/75) and, apart from N6
  and FC2's 2.0.1 behaviour, on 2.0.3 (71/75) and 2.0.1 (58/67).
- **Overlap arithmetic in detail.** Inclusive 1-based coordinates at both ends;
  D and N do not count as aligned bases; soft clips and insertions enter the
  `--fracOverlap` denominator and not the overlap; a fragment's overlap with a gene
  is the union over both mates and all exons (mates that overlap each other are
  not double-counted); `--fracOverlap` thresholds use floor(f × len) + 1 when the
  remainder is ≥ 0.001; the two-end vote (a gene hit by both mates beats one hit by
  one mate; `-O` disables the preference) and `--largestOverlap`'s two-end
  tie-break; `--fraction` as 1/NH, 1/y and 1/(NH·y) in 1/65536 units printed to
  two decimals.
- **Filters.** `-Q` as "at least one end"; `-B`; `-C`; `-P -d -D` on |TLEN|;
  `--ignoreDup` on either mate; NH-based multi-mapping with and without `-M`;
  `--primary`; `--nonSplitOnly`; strand rules for R1, R2 and single-end reads
  under `-s 0/1/2`; the first-read rule in read-level counting of paired data.
- **Junction counting (`-J`).** 300 reads over two junctions, 20 % duplicates, a
  third NH = 2, a third MAPQ 0: `.jcounts` equals the expected per-junction totals
  (151, 153) and, as documented, counts every N-containing read regardless of the
  `-Q`/`--ignoreDup` filters (98 of 300 assigned) — `heldup_misc.out` item 1.
- **The read pairer.** 179,309 records (60,000 fragments with mates up to 300 kb
  apart, NH/HI multi-mappers, chimeric pairs, one-mate-unmapped pairs, single-end
  records): coordinate-sorted input with 1 and 8 threads and name-adjacent input
  with 8 threads give counts and summaries identical to name-adjacent input with 1
  thread under three option sets (`heldup_sorted_input_pairer.out`).
- **Threads, per-file `-s`, annotation formats.** `-T 1/4/8` identical on 10,159
  records; `-s 1,2` over two files equals separate runs; GTF and SAF give the same
  counts; `-t exon,CDS`; `-g` values with spaces; GFF-style `key=value`; the
  `Length` column is the union of exons on the same chromosome and strand
  (`heldup_misc.out` items 2-5).
- **The project's own suite.** `test/featureCounts/featureCounts-test.sh` passes
  on `master` and with each patch (0 FAILED).

## Not audited

Long-read mode (`-L`); `--byReadGroup` beyond N3; the scRNA/`cellCounts` code
(about half of `readSummary.c`); `-J` with `-G` (splice-site strand from the
genome); chromosome alias files (`-A`); `-R SAM/BAM` output; `--readShiftType`/
`--readShiftSize`; `--maxMOp` truncation; GFF3 input; the Rsubread R interface
(not installable here — no CRAN/Bioconductor route); coordinate overflow above
2^31 (`load_feature_info` refuses such lines).
