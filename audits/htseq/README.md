# HTSeq audit against 161 published papers (2021–2026)

_Fourteenth audit in the series. Generated 2026-09-03 against `htseq/htseq` `main` @
`7672321` (2026-02-04, version string 2.1.2 — the same day the 2.1.2 wheel was
published). Focus: the code paths that produce the published numbers —
`htseq-count`'s overlap resolution, `--nonunique` arithmetic, strandedness, mate
pairing and the special counters, the `GenomicArrayOfSets`/`StepVector` interval
machinery under it, `htseq-count-barcodes` and `htseq-qa` — verified by executing the
shipped code against an independent per-base port._

## What this is

The six-journal survey found **161 papers** in PNAS (89), *Nature* (61), *Cell* (9)
and *Science* (2), 2021–2026, that used HTSeq — almost always `htseq-count` to turn
STAR/HISAT2/Bowtie2 alignments into the gene-count matrix that DESeq2 (109 papers) or
edgeR/limma (33) then tests. Its counting core was read in full on `main` and every
suspicion was run through the installed package (master, editable Cython+SWIG build
in a Python 3.12 venv; the 2.1.2 wheel from PyPI; the 0.11.2, 0.12.4 and 0.13.5
sdists built on 3.12 for version scope) on synthetic BAM+GTF files made with pysam,
with an independent Python port of the documented semantics — brute-force per-base
enumeration, no HTSeq data structures — as the reference.

## Findings (details and line citations in [`component-reviews/htseq-count-core.md`](component-reviews/htseq-count-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **HC2** | **CONFIRMED on `main`, 2.1.2, 0.13.5, 0.12.4, 0.11.2** (executed; the same line is in 0.9.1 by reading) | `htseq-count` compares the MAPQ field of *both* records of a pair with `-a` without checking that the record is aligned. Aligners write MAPQ 0 on an unmapped mate's record, so under the default `-a 10` every pair whose mate is unmapped but present in the BAM is counted as `__too_low_aQual` instead of for its gene, while the same pair counts when the unmapped record is absent from the file or with `-a 0` — contrary to the FAQ ("only the aligned read determines how the read pair is counted"). 113 of 113 such pairs lost on a 2,000-pair synthetic library, all 20 genes short, name- and position-sorted alike; the same comparison sits in `htseq-count-barcodes`. Exposure: paired-end data from aligners that keep unmapped mates (HISAT2, BWA, Bowtie2 defaults; STAR only with `--outSAMunmapped Within`). Two-line fix with test. |
| **HC1** | **CONFIRMED on `main`, 2.1.2, 0.13.5, 0.12.4, 0.11.2** (executed; 0.9.1 by reading) | `BAM_Reader[iv]` calls pysam `fetch(chrom, iv.start + 1, iv.end)` although both use 0-based half-open coordinates, so an alignment whose last aligned base is `iv.start` overlaps `iv` (`iv.overlaps` says so) but is not returned: 7 of 300 random windows each lose one read. API path used by the TSS tutorial; `htseq-count` does not use it. One-token fix with test. |
| N1 | note, design + documentation | `--nonunique fraction` divides by the number of overlapping features per alignment record, never by NH; with `--secondary-alignments score` a multimapper contributes NH counts and the documented "sum equals the number of reads" fails (270 for 190 reads). |
| N2 | note, design, quantified | `htseq-count-barcodes` lets `__no_feature`, `__alignment_not_unique`, `__too_low_aQual` and `__ambiguous` reads outvote a gene inside one UMI, and ties discard the molecule: a UMI with one read in gene A and two outside any feature counts as `__no_feature` (A = 2 where cellranger's rule gives 5 on the six-UMI example). |
| N3 | note, documentation | `doc/htseqcount.rst` says `--secondary-alignments` and `--supplementary-alignments` default to `score`; the code defaults to `ignore` since 0.10.0 (history entry exists; 0.9.1 defaulted to `score`); `--help` states neither. |
| N4 | note, design, edge | A pair with one mate on a chromosome that carries no feature is `__no_feature` as a whole (`UnknownChrom`), even if the other mate lies in a gene. |
| N5 | note, API, cosmetic | `GenomicInterval.overlaps` is asymmetric for zero-length intervals. |
| N6 | note, documented | mtx/h5ad/loom count matrices are float32 (2²⁴ + 1 → 2²⁴); TSV output is exact. |
| N7 | note, design | `htseq-qa --primary-only` keeps supplementary records (chimeric reads count twice); a base quality above `--maxqual` (41) aborts the script. |

Two own suspicions were withdrawn by execution (set corruption while `apply` rewrites
the `StepVector` it iterates; position-sorted pairing of cross-chromosome, placed and
supplementary records) and are recorded in the review.

**Held up under execution:** all eight rows of the documentation's overlap-mode figure
for every mode and every `--nonunique` setting; on random data with spliced,
clipped, indel-bearing, multimapping, chimeric and half-unmapped reads, all 324
combinations of mode × strandedness × `--nonunique` × `-a`/secondary/supplementary ×
`-r name`/`-r pos` equal the independent per-base port once HC2 is modelled (all 108
single-end runs equal the documented port outright); `--nonunique random` conserves
counts; multiple `-i`/`-t` and `--feature-query`; both mate pairers on 1,866 truth
pairs; `GenomicArrayOfSets` on 36,000 bases; GTF/GFF3 1-based→0-based conversion;
`StepVector` against a dense vector; `overlaps`/`contains` for non-empty intervals;
`htseq-qa` base and quality fractions to 0.0. Not audited: `count_old.py`, UMI
correction internals, the matrix writers, `StretchVector`, BigWig/bedGraph, VCF,
multiprocessing.

## How the papers use HTSeq (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| DESeq2 downstream / edgeR-limma downstream | 109 / 33 |
| `htseq-count` named | 82 |
| aligner: STAR / HISAT2-TopHat / BWA-Bowtie | 73 / 42 / 35 |
| version stated | 32 (0.11.x 17, 0.6.x 16, 0.9.x 11, 2.0.x 8, 0.12.x 7, 0.13.x 5; top: 0.9.1 ×11, 0.11.2 ×11, 0.6.1 ×9, 0.12.4 ×7, 0.13.5 ×5) |
| paired-end named | 31 |
| GENCODE / Ensembl / RefSeq annotation named | 35 |
| uniquely mapped reads only | 17 |
| ChIP/ATAC/CUT&RUN | 16 |
| featureCounts also named | 14 |
| mode union / intersection-strict / intersection-nonempty | 13 / 2 / 1 |
| single-cell / 10x | 12 |
| `-s no` / `-s reverse` / `-s yes` | 5 / 4 / 3 |
| `--nonunique all` / `none` | 3 / 1 |
| `-r pos` / `-r name` | 3 / 3 |
| `-a` / MAPQ stated | 3 (cutoffs named: 10, 20) |
| `--secondary`/`--supplementary-alignments` | 1 |
| TCGA/GDC HTSeq counts downloaded (no local run) | 4 |

Versions pinned run 0.5 to 2.0; HC2 and HC1 are present in every version the cohort
names that could be executed (0.11.2, 0.12.4, 0.13.5) and, by reading, in 0.9.1; the
0.6.1 line was not examined. HC2's exposure is decided by the aligner and the
paired-end flag, neither of which the cache resolves per paper: 31 papers name
paired-end data and 77 name HISAT2/TopHat/BWA/Bowtie, whose defaults keep unmapped
mates.

**Profiling caveat.** As for the Seurat, Scanpy and Cutadapt audits, this session had
no route to Europe PMC, so `htseq_profile.py` ran in `--offline` mode over the
survey's stored evidence snippets; every record in `htseq_profiles.jsonl` is `source:
survey_cache` and every count above is a lower bound. Rerun without `--offline` from
a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- No `CONTRIBUTING.md`; `doc/contrib.rst` covers building (Cython + SWIG), `./test.sh`
  (pytest over `test/` and doctests over `doc/*.rst`), and layout. No PR template, no
  pinned policy issue, no code of conduct, no linter configuration (CI runs pytest
  only), no Discussions link.
- `.github/ISSUE_TEMPLATE/bug_report.md`: markdown template with the fields Software
  versions (HTSeq, Python, OS, aligner) / Describe the bug / Minimal example showing
  the bug (files under 5 MB) / To Reproduce (exact command line). The two issue texts
  follow those fields; their examples write their own BAM/GTF so nothing is attached.
- `doc/history.rst` is the changelog (one section per release with a date; the file
  stops at 2.0.9 although 2.1.2 is out); each patch adds a "Version 2.1.3 /
  Unreleased" entry.
- Both findings are crisp bug fixes with tests; HC2 changes counts on affected files,
  which the PR body flags. Neither has a prior issue (tracker searched 2026-09-03;
  nearest #99, #94, #96, #106, #80, #14). **The kit is in [`upstream/`](upstream/)**:
  two issue texts in the template's fields with reproductions run on `main` and 2.1.2,
  two `git am`-able patches (fix + regression test that fails on unmodified `main` +
  history entry; the touched test modules pass with each patch), and the PR bodies.

## Files

| file | what |
|---|---|
| `htseq_profile.py`, `htseq_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/htseq-count-core.md` | the review: HC1–HC2, N1–N7, W1–W2, held-up list, not-audited list |
| `verify/htseq_port.py` | the independent per-base port of the documented semantics + pysam BAM/GTF generator (shared by the harnesses) |
| `verify/hc2_unmapped_mate_minaqual.py` (+ `.out`, `.v2.1.2.out`, `.v0.13.5.out`, `.v0.12.4.out`, `.v0.11.2.out`, `.patched.out`) | HC2: three-pair minimal case with XF tags; 2,000-pair library under `-a 10`/`-a 0`/stripped, both orders |
| `verify/hc1_bam_reader_interval_offset.py` (+ same set of `.out`) | HC1: minimal window; 300 random windows vs pysam and `overlaps`; TSS-style profile |
| `verify/heldup_overlap_modes_figure.py` (+ `.out`) | held-up: the documentation figure's eight rows, every mode × `--nonunique`, per-row XF tags |
| `verify/heldup_bruteforce_random.py` (+ `.out`) | held-up: 324 CLI configurations on random single-end and paired-end data vs the port (documented, and with HC2 modelled); `random` conservation; multi `-i`/`-t`; `--feature-query` |
| `verify/heldup_genomicarray_intervals.py` (+ `.out`) | held-up: `GenomicArrayOfSets` per base, GTF/GFF3 conversion, `overlaps`/`contains`, `StepVector` vs dense, both pairers vs truth (W1, W2, N5) |
| `verify/note_nonunique_fraction_secondary.py`, `note_barcodes_umi_vote.py`, `note_cli_defaults_vs_docs.py`, `note_qa_statistics.py` (+ `.out`) | N1, N2, N3/N6, N7 and the `htseq-qa` held-up check |
| `upstream/` | filing kit: issue texts, MCVE scripts and their outputs on `main` and 2.1.2, patches 0001 (HC2) and 0002 (HC1), PR bodies, documents read |

Harnesses need an install of the version under test in the active venv: `uv venv
--python 3.12 venv && uv pip install setuptools swig cython numpy pysam && uv pip
install --no-build-isolation -e <htseq clone>` (the SWIG `StepVector` extension
builds with the `swig` PyPI package), or `uv pip install HTSeq==2.1.2`. The 0.11.2,
0.12.4 and 0.13.5 sdists build on 3.12 only with `cython<3`, `numpy<2`, `pysam<0.23`
and a hand conversion of their Python-2 SWIG wrapper `StepVector.py` (`raise X, "…"`,
`print "…"`, `sys.maxint`, `next` → `__next__`), which the old `setup.py` used to do
with `2to3`; 0.11.2 additionally needs `-f bam` (`HTSEQ_PORT_EXTRA_ARGS="-f bam"` for
the harnesses). 0.9.1 and 0.6.1 were not built.

## Next steps

1. File HC2 and HC1 from the kit in `upstream/` (issue first, then PR; HC2's PR body
   flags the count change). Record numbers and maintainer responses here and in the
   top-level table.
2. Ask upstream whether the N1 (`fraction` vs NH) and N2 (UMI vote) behaviours are
   intended and, if so, get them documented.
3. Full-text profiling rerun when Europe PMC is reachable, to see which paired-end
   papers used HISAT2/BWA/Bowtie2 with the default `-a` (HC2's exposure).
