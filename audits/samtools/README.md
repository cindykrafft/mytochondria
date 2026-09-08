# SAMtools audit against 692 published papers (2021–2026)

_Generated 2026-09-08 against `samtools/samtools` `develop` @ `ce612d2` built with
`samtools/htslib` `develop` @ `e503e04` ("samtools ce612d2 / Using htslib
1.24-1-ge503e04"). Focus: the subcommands whose numbers appear in methods sections and
QC tables — `stats`, `flagstat`, `depth`, `coverage`, `idxstats`, `markdup`,
`mpileup`, `view -c` — verified by executing the built binaries on synthetic BAMs with
independently computed truths._

## What this is

The six-journal survey found **692 papers** in PNAS (316), *Nature* (313), *Cell* (50)
and *Science* (13), 2021–2026, that used SAMtools — the most-used tool in the survey
not yet audited, present in nearly every sequencing pipeline. Its QC and counting core
was read in full on `develop` and every suspicion was run through four builds: `develop`
(built here), the Ubuntu 24.04 package 1.19.2, and 1.10 and 1.9 built from their release
tags (the cohort's two most-cited versions), on BAMs constructed with pysam where
every flag, CIGAR, quality, position and insert size is known and the truth is computed
in Python (per-position depth, flag arithmetic, Picard's library-size estimator, a port
of HTSlib's overlap-removal rule).

## Findings (details and line citations in [`component-reviews/qc-and-counting-core.md`](component-reviews/qc-and-counting-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **ST1** | **CONFIRMED on `develop`, 1.19.2, 1.10 and 1.9** | **now** | `samtools stats` accumulates the coverage distribution (`COV` rows, and the `-t`/`-g` "percentage of target genome with coverage > N") in a ring buffer of 5 × read length (1,500 cells for ≤ 300-bp reads) indexed modulo its size relative to the read start. A block starting further than that beyond the read start — the far exon of a spliced RNA-seq alignment, any intron over ~1.4 kb at 100 bp — wraps around and is added to the positions next to the read start. Two reads reproduce it (`50M` + `50M1450N50M`: depth 3 × 50 instead of depth 1 × 50 + depth 2 × 50); on a simulated six-exon gene with 3,000 spliced reads samtools reports 2,591 covered positions for a true 2,197 (mean depth over covered 115.8 vs 136.6) and, with `-t` on the exons, `percentage of target genome with coverage > 0 (%)` = **117.77** (true 99.86). Same on every build executed; the `SN` numbers do not pass through this buffer. |
| **ST2** | **CONFIRMED on `develop`, 1.19.2, 1.10 and 1.9** | now (same patch) | When a read longer than any seen so far forces `realloc_buffers` to grow the buffers, the pending coverage ring is copied with `memcpy` lengths in cells where bytes are required, so three quarters of the pending counts are dropped if the window sits near the ring's end: ten 100-bp reads at 1,401–1,446 then a 350-bp read give `COV [11-11] 11 10` for a true 50. Fixed-length Illumina data never trigger it (the first read reallocates on an empty buffer); mixed-length and long-read data do (1,546 of 2,190,000 depth units lost on 200 reads of 1–20 kb). |
| N1 | note, verified, non-default option | held | `stats -p` (remove overlaps) exempts a read from the pair bookkeeping when `|TLEN| ≥ 2 × its own length`, so with mates of unequal length (150/90 bp, insert 200) the overlap is counted twice: `bases mapped (cigar)` 48,000 for 200 pairs where the once-counted truth is 40,000; equal-length mates are right. |
| N2 | note, verified, documentation | held | `reads duplicated` counts supplementary records with the DUP flag while `sequences` excludes supplementary records; after `markdup -S`/Picard, `reads duplicated / sequences` (what MultiQC prints) is 25.0 % on a file whose primary-read duplication rate is 20.0 %. `flagstat` prints both `duplicates` and `primary duplicates`. |
| N3 | note, verified, minor | held | The insert-size standard deviation loop starts at bin 1 while the mean and denominator include bin 0: 100 same-chromosome `TLEN 0` pairs among 1,000 give SD 36.6 where the population SD is 100.8. |
| N4 | note, verified, non-default option | held | `depth -s` keys overlap removal on `QNAME` alone; a supplementary record sorting between the mates is clipped to nothing and consumes the entry, so the real mate overlap is counted twice (`-G 0x800` avoids it). |
| N5 | note, verified, documentation | held | `coverage --rf` keeps a read with *any* of the mask bits (40 reads for `--rf 0x42`) while `depth --require-flags`/`view -f` need *all* (10); the `coverage` man page says "skip reads with mask bits unset". |
| N6 | note, by reading, acknowledged in the source | held | `stats -r` mismatches per cycle skip `N` operations without advancing the reference, so spliced reads' far exons are compared against the wrong reference bases ("Not very frequent and not noticeable", a 2012 comment). |

Three own suspicions were withdrawn by execution (overlap removal in `mpileup` was
thought to drop halved-quality bases; `markdup` optical checks were thought to be
original-vs-duplicate only; `flagstat`'s `float` percentage arithmetic) and are recorded
in the review.

**Held up under execution:** every `flagstat` line in all three output formats on
4,244 records; `idxstats` (indexed and streamed); 15 `view -c` filter combinations
including `-e` expressions; `depth` in 11 modes (`-a`, `-J`, `-q`, `-Q`, `-g`/`-G`,
`-l`, `-s`, `-r`, two files) with 0 mismatching positions over 30,000; the eight
`coverage` columns under `-q`/`-Q`/`-l`/`--ff`/`--min-depth`/`-r`; 31 `stats` SN
numbers (read classes, bases mapped (cigar), error rate, average quality, insert-size
mean and SD under the 99 % bulk rule, orientations, properly-paired percentage) under
four filter settings; `markdup` pair/single duplicate counts, the kept record, `-S`,
`-d` optical calls and `ESTIMATED_LIBRARY_SIZE` against a port of Picard's estimator;
`mpileup` depth under the default overlap removal (port of HTSlib's
`tweak_overlap_quality`), `-x`, `-Q`, `-q`, `--ff`, BAQ off, and the `-d 8000` cap.
Not checked: `sort`/`merge`, `calmd`, `consensus`, `bedcov`, `ampliconstats`, the
`stats` GC-depth and per-cycle tables, BAQ's arithmetic, CRAM paths, `--subsample`.

## How the papers use SAMtools (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 196 (1.9 ×92, 1.10 ×36, 1.3.1 ×26, 1.11 ×19, 1.16.1 ×17, 1.12 ×16, 1.3 ×14; 0.1.x ×14) |
| aligner named (BWA / Bowtie / STAR / minimap2 / HISAT) | 534 |
| duplicates (markdup / rmdup / duplicates named) | 267 (Picard also used 193; duplication rate reported 65) |
| RNA-seq / spliced data | 166 |
| MAPQ filter stated | 81 (thresholds: 30 ×25, 0 ×18, 20 ×13, 10 ×12) |
| `view` / filtering | 60 (`-f`/`-F` flag filter 43) |
| `mpileup` | 57 |
| long reads (nanopore / PacBio) | 55 |
| WGS / WES | 36 |
| mean depth / coverage reported | 18 |
| `flagstat` / `depth` / `coverage`,`bedcov` / `idxstats` / `stats` | 7 / 6 / 6 / 6 / 3 |
| insert size reported / error or mismatch rate reported | 6 / 5 |
| `fixmate` / `merge` / `fastq` / `calmd`,`consensus` / `faidx` | 6 / 6 / 4 / 3 / 1 |

Exposure by finding: ST1 needs `samtools stats` on spliced alignments and a reader of
its `COV` section, plot-bamstats coverage plot or `-t`/`-g` line (166 papers name
RNA-seq or splicing; 3 name `stats` in the cache — subcommand names are rarely spelled
out in methods, so this is a weak lower bound); ST2 needs mixed-length or long-read
data (55 name long reads). Every version the cohort names is affected. N1–N6 are on
non-default options or are documentation.

**Profiling caveat.** As for the Seurat, Scanpy and Cutadapt audits, this session had
no route to Europe PMC, so `samtools_profile.py` ran in `--offline` mode over the
survey's stored evidence snippets; every record in `samtools_profiles.jsonl` is
`source: survey_cache` and every count above is a lower bound. Rerun without
`--offline` from a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- `CONTRIBUTING.md` (added in 1.24): small single-topic PRs against a recent
  `develop`; tests and documentation with every PR; Developer Certificate of Origin
  with a real-name `Signed-off-by:` on every commit; an **AI policy** — every
  AI-generated line reviewed by the submitter, `Assisted-by: AGENT:MODEL` on each
  commit and at the end of the PR description, **AI agents may not add sign-offs**, and
  commit messages and PR descriptions written by a human. This is acceptance with
  conditions, not a refusal; the kit's commit message and PR body are drafts for the
  submitter to rewrite and sign.
- `.github/ISSUE_TEMPLATE/Bug_report.md`: three free-text headings (versions;
  OS/architecture/compiler; steps, command and output). No PR template.
- `NEWS.md` bullets under the unreleased heading; `make test` runs `test/test.pl`
  (`test_cmd` against `.expected` files) plus C unit and CRAM regression tests; no
  formatter or linter configuration.
- ST1 is the only "file now" item: a wrong number under default settings on the current
  release, with no prior issue (tracker searched 2026-09-08; nearest #1003, #640,
  #969). **The kit is in [`upstream/`](upstream/)**: issue text in the template's
  headings with a two-record MCVE (run on `develop`, 1.19.2, 1.9 and the patched
  build), one `git am`-able patch (fix + two regression tests that fail on unmodified
  `develop` + NEWS entry; `make test` 1007 passed / 0 failed with the patch, 1005 / 2
  without), and the PR body draft.

## Files

| file | what |
|---|---|
| `samtools_profile.py`, `samtools_profiles.jsonl`, `profile_run.log` | profiling pass over the 692 cohort papers (offline; see caveat) |
| `component-reviews/qc-and-counting-core.md` | the review: ST1–ST2, N1–N6, withdrawn suspicions, held-up list, not-audited list |
| `verify/_synth.py` | shared BAM builder (pysam), runner and truth helpers |
| `verify/st1_stats_cov_ringbuffer.py` (+ `.out`, `.v1.19.2.out`, `.v1.10.out`, `.v1.9.out`, `.patched.out`) | ST1: two-read wrap, short-intron control, six-exon gene simulation, `-t`/`-g` percentages |
| `verify/st2_stats_cov_realloc.py` (+ same set) | ST2: reallocation with pending coverage, empty-buffer control, growing long reads |
| `verify/heldup_flagstat_idxstats_view.py` (+ `.out`) | held-up: `flagstat` (3 formats), `idxstats`, 15 `view -c` cases |
| `verify/heldup_depth_coverage.py` (+ `.out`) | held-up: `depth` in 11 modes, `coverage` in 8 |
| `verify/heldup_stats_sn.py` (+ `.out`) | held-up: 31 `stats` SN numbers under 4 filter settings |
| `verify/heldup_markdup.py` (+ `.out`) | held-up: `fixmate -m` + `markdup -s` counts, kept record, `-S`, `-d`, library size vs Picard port |
| `verify/heldup_mpileup.py` (+ `.out`) | held-up: `mpileup` depth in 8 modes, BAQ note, `-d` cap |
| `verify/note_stats_overlap_unequal_mates.py`, `note_stats_counts_semantics.py`, `note_depth_s_supplementary.py`, `note_coverage_rf_semantics.py` (+ `.out`) | N1–N5 |
| `upstream/` | filing kit: issue text, MCVE + outputs, patch 0001 (ST1+ST2), PR body, documents read, test numbers |

Harnesses take the samtools binary as their first argument (`python verify/<h>.py
/path/to/samtools`) and need a Python ≥ 3.12 venv with `pysam` and `numpy`
(`uv venv --python /usr/bin/python3.12 venv && uv pip install pysam numpy`). Builds:
`git submodule update --init` in htslib, `autoreconf -i && ./configure && make`, then
`./configure --with-htslib=<htslib> && make` in samtools (zlib, bzip2, lzma, curl,
ncurses dev packages).

## Next steps

1. ST1 filed 2026-09-08: issue samtools/samtools#2378 and PR #2379 from the fork
   branch `fix/stats-coverage-ring-buffer` (commit `43069a1`, reviewed and signed off by
   the submitter, `Assisted-by:` trailer kept, per `CONTRIBUTING.md`). Waiting for the
   maintainers; the notes wait for a maintainer signal.
2. Extend the review to `stats` GC-depth (`GCD`; #1003 is open for long reads) and the
   per-cycle tables, `bedcov`, `consensus`, and BAQ's arithmetic in HTSlib.
3. Full-text profiling rerun when Europe PMC is reachable, to see which papers report
   `stats` coverage numbers on spliced data.
