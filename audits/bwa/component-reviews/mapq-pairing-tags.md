# BWA — MAPQ, insert-size estimation and pairing, alignment tags, split reads

_Read on `lh3/bwa` `master` @ `d82444c` (2026-08-07; code identical to the v0.7.19 release
`b92993c`, 2025-03-22: the four commits since touch only `README.md` and CI). Executed on that
build and on v0.7.17, v0.7.15 and 0.7.12 built from their tags here (0.7.15 and 0.7.17 need
`-fcommon` with GCC ≥ 10; nothing else changed). Every number below comes from a harness in
`../verify/` whose captured output sits next to it (`<harness>.<build>.out`; `.patched.out` is the
BWA1 fix)._

Files read: `bwamem.c` (`mem_opt_init`, `mem_chain`, `mem_chain2aln`, `mem_sort_dedup_patch`,
`mem_mark_primary_se`, `mem_approx_mapq_se`, `mem_reg2sam`, `mem_reg2aln`, `mem_aln2sam`,
`add_cigar`), `bwamem.h` (`mem_opt_t`), `bwamem_pair.c` (`mem_infer_dir`, `cal_sub`, `mem_pestat`,
`mem_matesw`, `mem_pair`, `mem_sam_pe`), `bwamem_extra.c` (`mem_gen_alt`, XA), `bwa.c`
(`bwa_fill_scmat`, `bwa_gen_cigar2`: CIGAR, NM, MD), `fastmap.c` (option parsing, batching),
`bwase.c`/`bwape.c`/`bwtaln.c` (samse MAPQ and MD, sampe insert size, `bwa_cal_maxdiff`), and
`bwa.1` as the statement of intended behaviour.

## Findings

### BWA1 — the MAPQ length factor is truncated: `mapQ_coef_fac` is an `int` holding ln 50 (every release since 0.7.6)

`mem_approx_mapq_se` (`bwamem.c:982-1006`), the default MAPQ estimator since r418 (2013-11-02,
released in 0.7.6, whose NEWS says "Changed the way mapping quality is estimated"), computes

```c
l = max(qe - qb, re - rb);
identity = 1. - (double)(l * opt->a - a->score) / (opt->a + opt->b) / l;
tmp = l < opt->mapQ_coef_len? 1. : opt->mapQ_coef_fac / log(l);     // bwamem.c:994
tmp *= identity * identity;
mapq = (int)(6.02 * (a->score - sub) / opt->a * tmp * tmp + .499);
```

with `o->mapQ_coef_len = 50; o->mapQ_coef_fac = log(o->mapQ_coef_len);` (`bwamem.c:107`; the
`-Q` handler at `fastmap.c:204-206` does the same). The struct declares the two fields as

```c
float mapQ_coef_len;     // bwamem.h:78
int mapQ_coef_fac;       // bwamem.h:79   <- ln 50 = 3.912 is stored as 3
```

so the length factor is `3/ln(l)` instead of `ln(50)/ln(l)`. The code is written so that the
factor is 1 up to l = 50 and then falls slowly as ln 50 / ln l; with the truncation it drops from 1
at l = 49 to 0.767 at l = 50 and stays 23 % below the intended value at every length above, so
`tmp*tmp` (the factor enters squared) is 41 % too small. Every primary MAPQ goes through this
function: single-end reads (`mem_reg2aln`, `bwamem.c:1136`), both mates of a pair (`q_se`,
`bwamem_pair.c:337, 347-348`, before the paired boost `q_se = max(q_se, min(q_pe, q_se + 40))`
at :339), and the MAPQ in `XB`. The cap at 60 hides the effect for reads that are clearly unique,
so it reaches the reads that matter for filtering: reads with a near-equal second hit, short or
heavily trimmed reads, and low-identity alignments.

Executed (`m1_mapq.py`):

- A Python port of the formula reproduces **158/158** single-end MAPQs on every build (master,
  0.7.17, 0.7.15, 0.7.12) with `FAC = 3` and only **120/158** with `FAC = ln 50`; the 38 that
  differ are the 37 reads with 0 < MAPQ < 60 and aligned length ≥ 50, plus one 150-bp read
  (AS 150 / XS 149) that is 0 as released and 1 with the fix. Examples
  (master): two-copy segment with 8 differences between copies, 100-bp perfect read, AS 100 /
  XS 85 → **MAPQ 38** (intended 60); 150 bp, AS 135 / XS 120 → **30** (51); 70 bp, AS 70 / XS 60
  → **30** (51); 100 bp, AS 95 / XS 90 → **9** (18); unique 50-bp read with 4 mismatches, AS 31 →
  **31** (53).
- Length scan across the boundary (two copies of a segment differing at one base; reads of 40-60
  bp centred on it, AS = L, XS = L − 5, one near-equal hit): MAPQ **27** for every length 40-49,
  then **15** at 50 and 51, falling to 13 at 60. With the fix: 27 up to 52, then 26, 25, 24 —
  continuous. A 49-bp read passes a MAPQ ≥ 20 filter, the same read one base longer does not.
- The patched build (`int` → `float`, `0001-Declare-mapQ_coef_fac-as-float-...patch`) matches the
  `ln 50` port on 158/158 and the length scan on 21/21 (`m1_mapq.patched.out`), and differs from
  master in column 5 only: every other SAM field (POS, CIGAR, flags, mate fields, TLEN, NM, MD,
  AS, XS, SA, XA) is identical across the m1 and m2 read sets, and the s1, p1, c1 and a1
  harness outputs are byte-identical between the two builds.

Is the truncated value an accidental improvement? `m2_mapq_calibration.py` compares the two builds
on the same simulated reads (3-Mb genome, 33 % planted repeats of 300-3,000 bp with 2-20 copies at
0.5-15 % divergence; 0.5 % substitution errors; a primary is wrong if more than 10 bp from its
origin). Both builds are conservative, and the fix moves MAPQ toward calibration without adding
errors where filters are usually set:

| read set | MAPQ 1-59: wrong / promised, released → fixed | reads with MAPQ ≥ 30, released → fixed (wrong) |
|---|---|---|
| single-end 150 bp | 12 / 1,089 (0.01) → 23 / 292 (0.08) | 51,892 → 54,082 (0 → 0) |
| single-end 100 bp | 37 / 1,163 (0.03) → 42 / 200 (0.21) | 50,125 → 52,064 (0 → 0) |
| single-end 60 bp | 30 / 752 (0.04) → 33 / 143 (0.23) | 49,209 → 49,719 (0 → 0); at MAPQ ≥ 20: 49,619 (0) → 51,098 (5) |
| paired 2×150 | 7 / 27 (0.26) → 7 / 25 (0.28) | 58,016 → 58,017 (0 → 0) |

("promised" = Σ 10^(−MAPQ/10) over the bin.) So on this simulation the truncation discards 3-4 %
of single-end reads at the MAPQ ≥ 30 filter that are all correctly placed; pairs are almost
unaffected because the pairing boost lifts both mates. The simulation is not the human genome;
the claim is limited to "the truncation is not an empirical calibration in disguise: removing it
makes MAPQ less conservative and closer to its Phred meaning, here".

Scope: identical code and identical behaviour on 0.7.12, 0.7.15, 0.7.17, 0.7.19/master. BWA-MEM2
(`bwa-mem2/bwa-mem2` @ `97978f9`, `src/bwamem.h:103`) copies the same `int` declaration, so the
two programs agree today and a fix in one would make their MAPQs differ, which matters because
the BWA README sends users who want "the exact legacy output of BWA-MEM" to BWA-MEM2.

Fix: one token, `int mapQ_coef_fac;` → `float mapQ_coef_fac;` (same size, so `mem_opt_t` keeps its
layout for library users). Alternative if the maintainer prefers to keep legacy output frozen: say
in `bwa.1` that MAPQ uses `3/ln(l)` above 50 bp.

### BWA2 — `MC:Z` on a supplementary record rewrites the mate's soft clips as hard clips (0.7.16 onward)

`mem_aln2sam` prints the mate CIGAR with the current record's rank:
`if (m && m->n_cigar) { kputsn("\tMC:Z:", 6, str); add_cigar(opt, m, str, which); }`
(`bwamem.c:934`), and `add_cigar` turns every S/H into H when `which > 0` unless `-Y`
(`bwamem.c:838-849`, `c = which? 4 : 3; // use hard clipping for supplementary alignments`). That
rule is meant for the record's own CIGAR; applied to the mate it makes `MC:Z` disagree with the
mate's actual CIGAR. `c1_split_reads.py`: 600 pairs with a chimeric mate 1 (90 bp chr1 + 60 bp
chr2) and a mate 2 that has a 12-bp soft clip in half of them: **299** supplementary records carry
`MC:Z:12H138M` while the mate's record reads `12S138M` (master and 0.7.17; correct with `-Y`;
0.7.12 and 0.7.15 emit no `MC`). Held: the tools that read `MC` for the mate's unclipped position
(Picard, samtools `markdup`) count S and H alike, so no downstream number changes; it is a SAM
consistency defect (the spec defines `MC` as the mate's CIGAR string). Fix: pass 0 instead of
`which` for the mate (`add_cigar(opt, m, str, 0)`); with that one token `MC:Z` equals the mate's
CIGAR on 1,800/1,800 records in all three modes (`c1_split_reads.bwa2-fix.out`; not packaged as a
patch while held).

### BWA3 — same-strand libraries: `mem_pair` and `mem_infer_dir` classify FF/RR pairs differently (every version)

`mem_infer_dir` (`bwamem_pair.c:49-56`), used by `mem_pestat`, mate rescue and the fallback
proper-pair check (`:411-412`), codes a same-strand pair by **read order** (0 = mate 2 downstream
of mate 1 in mate 1's direction, 3 = upstream). `mem_pair` (`:229-231`) codes it by **strand**
(`dir = r<<1 | strand`: 0 = both forward, 3 = both reverse). For an FF library `mem_pestat`
estimates orientation 0 and fails 3, so `mem_pair` accepts only the pairs from forward-strand
fragments; pairs from reverse-strand fragments never pair, fall through to `no_pairing`, and get
single-end MAPQ and independently chosen primaries (the fallback check then still sets 0x2 when
the two top hits happen to be concordant). `p1_pairing.py` part C (FF library, the left mate in an
exact two-copy repeat, the right mate unique): forward fragments 200/200 at the true copy, 0x2 on
200, MAPQ 40; reverse fragments **100/200** at the true copy, 0x2 on **100**, MAPQ **0** —
identical on all four builds. FR and RF libraries (opposite strands) are unaffected: both
functions agree there. Held: same-strand libraries are rare (SOLiD mate pairs, some custom
protocols); open #405 (wheat homeologs, mapq-0 mate placed away from its mate) shows the same
symptom on an ordinary library and is a different path.

### N1 — the printed insert-size mean is the mean of TLEN − 1 (note)

`mem_infer_dir` measures from the leftmost base of one mate to the rightmost base of the other
without the +1 that TLEN carries (`bwamem.c:891`), so the "mean and std.dev" and the proper-pair
bounds on stderr are in units of TLEN − 1: 299.86 for fragments whose mean is 300.91
(`p1_pairing.*.out`, part A). The bounds and the flag are internally consistent (flag 0x2 matches
the port on 3,000/3,000 pairs); only the printed mean is 1 bp low. Held (stderr, 1 bp).

### N2 — AS:i on an unclipped alignment is the clipped (local) score (documented)

When the end-to-end extension is preferred because it scores more than the local one minus the
clipping penalty, the record is printed without a clip but `AS:i` keeps the local score:
100M with a mismatch at the first base, NM 1, **AS 99** while the printed alignment scores 95
(96/456 records in `s1_scoring_tags`, every one a mismatch in the first or last four bases). `bwa.1`
(`-L`) says so ("the SAM AS tag reports the best SW score; clipping penalty is not deduced").
Recorded because pipelines that recompute scores from CIGAR+MD will disagree with AS by up to the
clipping penalty; not a defect.

## Held up under execution

- **CIGAR, POS, NM, MD, AS** (`s1_scoring_tags`, 456 reads × 4 builds + patched): perfect reads,
  1-5 substitutions, substitutions at every one of the first/last seven positions, two Ns, 1-5-bp
  insertions and deletions mid-read and at 12 bp from the end, a mixed sub+ins+del read, 100 and
  150 bp, both strands. POS/strand at the planted origin 456/456; NM and MD equal an independent
  recomputation from SEQ, reference and CIGAR (N counted as a mismatch, as samtools calmd does)
  456/456; AS equals the best local Smith-Waterman score computed in Python 456/456; the printed
  alignment never scores worse than the planted edits.
- **Single-end MAPQ** against the port (above), including `sub_n` (near-equal hits within 7) and
  the 0 for exact multi-copy hits; **paired MAPQ** for a repeat mate rescued by a unique mate
  (port of `mem_pair`'s score with the normal-tail term, `q_pe`, the +40 rule): 40/40, and 60/60
  for 360 unique pairs.
- **Insert-size estimation** (`p1_pairing` A): percentiles, mean, s.d. and proper-pair bounds equal
  a port of `mem_pestat` run on the true fragment lengths (3,000 FR pairs, 3 % long outliers);
  flag 0x2 set exactly when the fragment falls inside the port's bounds (3,000/3,000); TLEN =
  ±fragment (3,000/3,000).
- **Mate rescue** (`p1_pairing` B): 200 mates with a mismatch every 12 bp (no exact 19-mer) are all
  placed by mate-SW at the true position with NM 8, flag 0x2, MAPQ 60.
- **Split reads** (`c1_split_reads`): every SA entry equals the record it names (RNAME, POS,
  strand, CIGAR, MAPQ, NM; 1,200/1,200, also under `-Y` and `-M`); supplementary MAPQ ≤ primary
  (600/600); RNEXT/PNEXT/MQ on every record equal the mate's primary (1,800/1,800); flag 0x2 on
  all records of concordant chimeric pairs.
- **bwa aln/samse/sampe** (`a1_aln_samse_sampe`, 4 builds): POS and NM/MD for 36/50/75-bp reads
  with 0-3 substitutions or a 1-2-bp indel (341/341); sampe TLEN and flag 0x2 on 2,000 pairs, the
  printed insert size equal to the simulated mean (250.13). Four reads with three substitutions in
  the 5' 32 bp are unmapped, which is the documented `-l 32 -k 2` seed rule (they map with
  `-l 1000`).

Not checked: ALT-contig handling (`.alt`, `pa:f`, `XA` with ALT hits), `-p` smart pairing, `-5`
(Hi-C), `-a` beyond its use for counting near-equal hits, XA content beyond its use above,
`bwa index` on references with IUPAC codes (ambiguous bases are replaced by random bases, which
`bwa.1` documents for aln), BWA-SW, multithreaded batch-size effects on the insert-size estimate
(documented under `-K`), `bwa-mem2` beyond reading its declaration.

## Withdrawn suspicions

- `mem_pestat` percentile indexing and the `isize` buffer `memset` with `sizeof(kvec_t(int))`:
  the indexing never reaches `n`, and the two kvec types have the same size; the port agrees.
- Proper-pair flag when the unpaired score wins (`o <= score_un`): by arithmetic the normal-tail term
  stays above ≈ −14.5 inside the bounds even for a uniform distribution, so `o` stays above
  `score_un = s1 + s2 − 17`; and flag 0x2 matched the port on all 3,000 pairs in `p1_pairing` A.
- Uninitialised `rid` in `mem_matesw` when `rb >= re`: guarded by `re - rb >= min_seed_len`.
- Missing aln reads with three substitutions: the seed rule, documented (above).
