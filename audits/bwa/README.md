# BWA audit against 418 published papers (2021–2026)

_Generated 2026-10-18 against `lh3/bwa` `master` @ `d82444c` (2026-08-07; VERSION 0.7.19-r1273,
code identical to the v0.7.19 release of 2025-03-22) built here, and the release tags 0.7.17,
0.7.15 and 0.7.12 built from source (the cohort's three most-cited versions; 0.7.15 and 0.7.17
need `-fcommon` with GCC ≥ 10). Focus: what a paper takes from a BWA run — MAPQ, the alignment
score and tags (AS/XS/NM/MD/SA/XA/MC), the insert-size estimate, the proper-pair flag, mate rescue
and primary/supplementary choice in `bwa mem`, plus `bwa aln/samse/sampe`. Each was verified by
executing the binaries on reads from random references where every edit, fragment length and
repeat copy is known._

## What this is

The six-journal survey found **418 papers** in *Nature* (195), PNAS (181), *Cell* (31), *Science*
(10) and NEJM (1), 2021–2026, that used BWA. It is the survey's most-used short-read aligner
(alignment/mapping in 378 papers, upstream of variant calling with GATK, Mutect and
HaplotypeCaller, ChIP/ATAC and Hi-C pipelines). The MAPQ, pairing, tag and split-read code was
read on `master`. Every suspicion was run on the four builds with harnesses whose truths are
computed independently in Python:
- the documented scoring scheme, a local Smith-Waterman, and NM/MD recomputed from SEQ, the
  reference and the CIGAR;
- a port of `mem_approx_mapq_se` and of the paired MAPQ;
- a port of `mem_pestat` run on the true fragment lengths;
- the records themselves for SA/MC/MQ.

## Findings (details and line citations in [`component-reviews/mapq-pairing-tags.md`](component-reviews/mapq-pairing-tags.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **BWA1** | **CONFIRMED on 0.7.12, 0.7.15, 0.7.17 and `master`** (code since r418, 2013; also in BWA-MEM2) | **now** (issue first; PR on request) | `mapQ_coef_fac` is declared `int` (`bwamem.h:79`) but holds ln 50 = 3.912. The MAPQ length factor is therefore `3/ln(l)` instead of `ln(50)/ln(l)`: it drops from 1 at l = 49 to 0.767 at l = 50, and squared it leaves every sub-cap MAPQ of an alignment ≥ 50 bp about 41 % low. One read with a one-mismatch second hit: MAPQ **27** at 40–49 bp, **15** at 50 bp. A port with FAC = 3 reproduces 158/158 MAPQs on every build; with ln 50, 120/158. Simulation (3 Mb, 33 % repeats): the fix makes MAPQ less conservative and closer to its Phred meaning, and adds 3–4 % of single-end reads at MAPQ ≥ 30, all correctly placed; pairs are almost unchanged. One-token fix, `int` → `float`; only column 5 changes. |
| BWA2 | CONFIRMED on 0.7.17 and `master` (`MC` added in 0.7.16) | held | `MC:Z` on a supplementary record prints the mate's CIGAR with its soft clips rewritten as hard clips: `add_cigar` applies the supplementary-record H rule to the mate (`bwamem.c:934`). 299 supplementary records (of 300 pairs whose mate has a 12-bp tail) show `12H138M` for an actual `12S138M`; correct with `-Y`. Picard and samtools count S and H alike for the mate's unclipped start, so no downstream number moves. One-token fix verified. |
| BWA3 | CONFIRMED on all four builds | held | Same-strand (FF) libraries: `mem_pair` codes orientation by strand, while `mem_infer_dir` (insert-size estimate, rescue, fallback flag) codes it by read order. Pairs from reverse-strand fragments are never paired. A repeat mate whose partner is unique is then placed at the true copy 100/200 times with MAPQ 0, against 200/200 with MAPQ 40 on forward fragments. FR/RF libraries are unaffected. |
| N1 | note, verified | held | The insert-size mean printed on stderr is the mean of TLEN − 1: 299.86 for fragments of mean 300.91. Bounds and flag are internally consistent (0x2 matches the port on 3,000/3,000 pairs). |
| N2 | note, verified, documented | held | `AS:i` of an unclipped alignment is the clipped (local) score when the end-to-end extension was preferred: `100M NM:1` with a first-base mismatch has AS 99 while the printed alignment scores 95 (96/456 reads, all with a mismatch in the first or last four bases). `bwa.1` (`-L`) documents it. |

**Held up under execution:**
- **CIGAR/POS/NM/MD/AS** for substitutions at every end position, Ns, 1–5-bp indels and mixed edits
  (456 reads × 4 builds). NM and MD equal the recomputation; AS equals the best local SW score.
- **Single-end MAPQ** against the port (158/158 with the compiled factor), including near-equal-hit
  counting and multi-copy zeros.
- **Paired MAPQ** for a repeat mate rescued by a unique mate (40/40), and 60/60 for unique pairs.
- **Insert-size estimate** (percentiles, mean, s.d., proper-pair bounds) equal to a port of
  `mem_pestat`; flag 0x2 exactly at the port's bounds; TLEN = ±fragment.
- **Mate rescue** of unseedable mates: 200/200 at the true position, NM 8, MAPQ 60.
- **Split reads:** SA entries (1,200/1,200 under default, `-Y`, `-M`), the supplementary MAPQ cap,
  RNEXT/PNEXT/MQ.
- **bwa aln/samse/sampe:** POS, NM/MD, TLEN, flag 0x2, and the insert-size estimate.

Not checked:
- ALT-contig handling;
- `-p`, `-5`;
- XA content beyond hit counting;
- references with IUPAC codes;
- BWA-SW;
- batch-size effects on the insert-size estimate (documented under `-K`);
- real human data (the calibration result rests on a simulated genome).

## How the papers use BWA (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 178 (0.7.17 ×98, 0.7.15 ×21, 0.7.12 ×19, 0.7.10 ×5, 0.7.18 ×4, 0.7.16 ×4, 0.5.10 ×4) |
| `bwa mem` / BWA-MEM named | 230 |
| `aln` / `samse` / `sampe` / backtrack | 27 |
| paired-end named / single-end named | 29 / 5 |
| GATK / HaplotypeCaller / Mutect downstream | 26 |
| MAPQ / mapping-quality threshold mentioned | 12 |
| "uniquely mapped" / XS / XA / multi-mapper | 8 |
| `-M` | 7 |
| ChIP/ATAC 9, Hi-C 10, ancient DNA 7 | |

Which finding reaches which paper:
- **BWA1** reaches every `bwa mem` run whose MAPQ is filtered or reported (GATK's default MQ ≥ 20
  read filter; `samtools view -q`). Most strongly it reaches single-end and short or trimmed reads
  (ChIP-seq, small-RNA, ancient-DNA and amplicon libraries), plus repeat-rich targets. On paired
  reads the pairing boost hides most of it.
- **BWA2** reaches tools that validate `MC` against the mate.
- **BWA3** reaches only same-strand libraries.

The profile (`bwa_profile.py`, `profile_run.log`) was run offline against the survey's stored
evidence sentences, so every count is a lower bound over a few hundred characters per paper.

## Filing channel

`lh3/bwa` has no `CONTRIBUTING.md`, no issue or PR template and no AI policy in the tree. It has a
Contributor Covenant `code_of_conduct.md`, and `README.md` points to the mailing list and forums.
CI only runs `make` on four platforms; there is no test suite.

The README now says BWA-MEM "will be replaced by minibwa" and sends users who want "the exact
legacy output of BWA-MEM" to BWA-MEM2 or BWA-MEM3. BWA-MEM2 carries the same `int` declaration.
So BWA1 goes as an issue that offers either the one-line code fix or a man-page sentence, and the
PR follows only if the maintainer wants the code changed.

Kit under [`upstream/`](upstream/): the BWA1 issue text, a PR body, a `git am`-able patch, test
runs and the duplicate check (no prior report). No fork of `lh3/bwa` exists under `cindykrafft`.

## Files

| path | what |
|---|---|
| `component-reviews/mapq-pairing-tags.md` | the review: BWA1–BWA3, N1–N2 with code citations, held-up list, withdrawn suspicions |
| `verify/_synth.py` | reference/read builders, SAM parser, NM/MD recomputation, CIGAR scoring, Python local SW |
| `verify/s1_scoring_tags.py` | CIGAR/POS/NM/MD/AS vs planted edits (N2) |
| `verify/m1_mapq.py` | MAPQ vs the port, single-end and paired; the 40–60-bp length scan (BWA1) |
| `verify/m2_mapq_calibration.py` | released vs fixed MAPQ calibration on a simulated repeat-rich genome (BWA1) |
| `verify/p1_pairing.py` | `mem_pestat` port, flag 0x2, TLEN, mate rescue (N1); the FF library (BWA3) |
| `verify/c1_split_reads.py` | SA, supplementary MAPQ, MC/MQ/RNEXT (BWA2) |
| `verify/a1_aln_samse_sampe.py` | BWA-backtrack POS, NM/MD, sampe TLEN/flag |
| `verify/run_all.sh` | runs every harness on every build |
| `verify/*.<build>.out` | captured output per build (`master`, `v0.7.17`, `v0.7.15`, `0.7.12`); `.patched.out` from the BWA1 fix, `c1_split_reads.bwa2-fix.out` from the BWA2 one-token change, `m2_mapq_calibration.master_vs_patched.out` |
| `bwa_profile.py`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit |

## Next steps

1. File BWA1 as an issue (`upstream/issue-bwa1-mapq-coef-fac-truncated.md`).
2. Fork `lh3/bwa`, push `fix/mapq-coef-fac-float`, and open the PR only if the maintainer wants
   the code change (otherwise offer the man-page sentence).
3. BWA2, BWA3, N1, N2 held. After a positive reply, BWA2 (one token) could follow.
