# minimap2: alignment score and tags, MAPQ, primary/secondary/supplementary, divergence, pairing and splicing

_Read on `lh3/minimap2` `master` @ `3c28777` (2026-05-19, "Release minimap2-2.31 (r1302)", which
is also the latest release). Executed on that build and on the 2.17-r941, 2.24-r1122 and
2.26-r1175 tags built from source (the cohort's three most-cited versions). Every number below
comes from a harness in `../verify/` whose captured output sits next to it: `.out` for master,
`.v<version>.out` for the releases, `.patched.out` for the fix. Line numbers refer to
`3c28777`._

Files read: `map.c` (`mm_map_frag_core`, `chain_post`, `align_regs`, the pair-orientation
flip in `worker_for`), `hit.c` (`mm_gen_regs`, `mm_set_parent`, `mm_hit_sort`, `mm_select_sub`,
`mm_sync_regs`, `mm_filter_strand_retained`, `mm_filter_regs`, `mm_seg_gen`, `mm_set_mapq2`,
`mm_set_inv_mapq`), `lchain.c` (`comput_sc`, `mg_lchain_dp`, backtracking), `align.c`
(`mm_fix_cigar`, `mm_update_extra`, `mm_align_sr_rna`, `mm_fix_bad_ends*`, `mm_align1`,
`mm_align1_inv`, `mm_event_identity`, `mm_update_dp_max`, `mm_align_skeleton`), `ksw2_extz2_sse.c`,
`ksw2_extd2_sse.c` and `ksw2_exts2_sse.c` (end handling, splice-signal tables), `esterr.c`,
`format.c` (tags, `cs`/`MD`, SAM flags, `TLEN`, `SA`, PAF), `pe.c` (`mm_select_sub_multi`,
`mm_pair`, `mm_set_pe_thru`), `options.c` (presets), and `minimap2.1`, `cookbook.md`, `FAQ.md`
for documented behaviour.

## Findings

### MM1: `AS:i` is above the score of the reported alignment when an extension reaches the query end (`-x sr`, every version)

`mm_align1` extends left and right of the chain with `KSW_EZ_EXTZ_ONLY` and `opt->end_bonus`
(`align.c:791`, `:883`). The ksw2 kernels set `ez->reach_end` and backtrack from the query
end when `ez->mqe + end_bonus > ez->max` (`ksw2_extz2_sse.c:304-306`, `ksw2_extd2_sse.c:393-395`,
`ksw2_exts2_sse.c:457-459`). That path scores `ez->mqe`. `mm_align1` takes the coordinates
of that path (`align.c:796-797`, `:888-889`), but adds `ez->max` to `dp_score`
(`align.c:794`, `:886`):

```c
if (ez->n_cigar > 0) {
    mm_append_cigar(r, ez->n_cigar, ez->cigar);
    r->p->dp_score += ez->max;          // best score anywhere = the clipped path
}
rs1 = rs - (ez->reach_end? ez->mqe_t + 1 : ez->max_t + 1);
```

`dp_score` is printed as `AS:i` (`format.c:403`). The `-x sr` preset sets `end_bonus = 10`
(`options.c:157`; the default is −1, `options.c:51`, which makes `reach_end` impossible). With
`-A2 -B8`, a single mismatch d bp from either end is always extended through, and AS is then
`8 − 2(d − 1)` above the CIGAR's score for d = 1..4:

| harness | result on 2.17 / 2.24 / 2.26 / 2.31 | patched |
|---|---|---|
| `s1_scores_tags.py`, `-x sr` L = 150 and 100, mismatch d = 1..8 bp from the 5'/3' end, forward and reverse reads | AS − port = +8, +6, +4, +2 for d = 1..4 (both ends, both strands), 0 for d ≥ 5 and for interior mismatches, 1–12-bp indels and clean reads; 132/180 records match per block on 2.31 (126/180 on 2.17–2.26, which also miss on N reads, see F1) | 180/180 |
| same harness, map-ont 2 kb and `-x splice` 1.5 kb | AS == port 180/180 | unchanged |
| `r1_as_prevalence.py`, 20,000 2 × 150 bp pairs, SNPs + small indels, Illumina-like 3' error | 2,803/40,000 primary records (7.0 %) above the CIGAR's score, by +2 (650), +4 (685), +6 (704), +8 (758), +10–16 (6); identical counts on all four builds | 0/40,000; no other field (FLAG, POS, MAPQ, CIGAR, TLEN, NM, ms, s1, s2, de) changes |
| `x1_as_issue_repro.py` (the issue's five reads) | `150M NM:i:1 AS:i:298/296/294/292/290` | `AS:i:290` × 5 |

`ms:i` (`dp_max0`) is not affected: `mm_update_extra` recomputes it from the CIGAR
(`align.c:254-303`). MAPQ and mate pairing use `dp_max`, so they are unaffected too. The
behaviour dates from r499 (7345621, 2017-10-11). Fix:
`../upstream/0001-Score-extensions-that-reach-the-query-end-by-the-end.patch` (add
`ez->reach_end? ez->mqe : ez->max`).

### MM2: the best hit keeps its `n_sub` count from the chaining pass, so the second pass adds on top (every version; small)

`mm_set_parent` (`hit.c:125-186`) counts for each primary the overlapping secondaries that are
nearly as good (`++rp->n_sub`, `hit.c:170,175,177`). `mm_set_mapq2` subtracts
`4.343·ln(n_sub+1)` from the MAPQ (`hit.c:478`). The function runs twice per read: on the
chains (`chain_post`, `map.c:209`, and `map.c:348` for multi-segment reads) and after base
alignment (`align_regs`, `map.c:220`). Every primary found in a pass starts from zero
(`ri->n_sub = 0`, `hit.c:182`) except `r[0]`, whose initialisation is
`w[0] = 0, r[0].parent = 0;` (`hit.c:133`). The 2017 commit that introduced `n_sub` (6a82a21,
r361) added the reset to line 182 but not to line 133.

`m1_nsub_mapq.py` uses an instrumented build that prints `r[0].n_sub` on entry to each call,
a patched build (`r[0].n_sub = 0` at `hit.c:133`), and reads from 108 two-copy repeat families
of known divergence:

- map-ont: `r[0]` enters the post-alignment pass with `n_sub = 1` carried over in 72 of 432
  reads, but no MAPQ changes (the reads have MAPQ 0 in identical copies or are clearly
  resolved).
- `-x sr` pairs: carried over in 776 of 2,880 post-alignment calls; MAPQ differs on 52 of 2,880
  records (1.8 %), 1–2 units higher with the reset, all 52 placed on the copy they came from.
  Threshold crossings: ≥10: 3, ≥20: 1, ≥60: 2. Placement accuracy at MAPQ ≥ 20 is the same
  (0 wrong on both builds).

**Tier: held.** The effect is real but small, and the MAPQ heuristics were tuned empirically
with this behaviour. Line identical in 2.17 (`hit.c:117`), 2.24 and 2.26 (`hit.c:133`); only
master was executed with the instrumented and patched builds.

### MM3: `dv:f` adds a missing minimizer at the right end using `qs` where the query's remaining length is `qlen − qe` (every version; tiny)

`mm_est_err` (`esterr.c:30-64`) estimates divergence from matched minimizers and adds one
expected-but-unmatched minimizer per end when both sequences continue past the chain:

```c
if (r->qs > avg_k && r->rs > avg_k) ++n_tot;                  // esterr.c:60
if (qlen - r->qs > avg_k && l_ref - r->re > avg_k) ++n_tot;   // esterr.c:61 -- qlen - r->qe
```

`qlen − r->qs` exceeds k for almost every hit, so an error-free read inside the reference gets
`dv = 1 − (n/(n+1))^(1/k)` instead of 0. In `d1_dv_divergence.py` (60 error-free reads,
default preset, PAF without `-c`), dv equals the `qs` port on 60/60: 0.0007–0.0008 for 500-bp
reads, 0.0001–0.0004 for 1–5 kb, 0 only for reads ending at the reference end. Identical on
all four builds. **Held:** at most 0.0008 and only without `-c`. The left/right tests also pair
the query start with the reference start for reverse-strand hits; not separately measured.

## Notes (verified, held)

**N1: `ms:i` and `dp_max` in `-x sr` charge every gap `O + E` whatever its length (since 2.22).**
`mm_update_extra` rescoring: `if (log_gap) s -= q + e·log2(1+len); else s -= q + e;`
(`align.c:283-284`, `:292-293`). It is called with `log_gap = !(is_sr || is_sr_rna)`
(`align.c:906`). Up to 2.21 the else branch was `q + e*len`; 161ae7f (r1079) changed it.
`s1_scores_tags.py`: on 2.24/2.26/2.31, `ms` matches the flat port on 48/48 gapped sr records
(a 12-bp deletion: `ms − AS` = 22); on 2.17 it matches the affine port 48/48. Long reads match
the log port 48/48 on 2.24+. The maintainer has said the log form is "used only for rescoring"
(#1000), so `ms`/`dp_max` is a ranking score by design. The manual's "DP score of the max
scoring segment" does not say this. Held as documentation; it does steer MAPQ and pairing for
short reads with long indels.

**N2: under `-x splice`, GC-AG and AT-AC introns of error-free reads can be placed at a nearby
GT donor with a compensating 1–5-bp indel.** The splice-signal tables
(`ksw2_exts2_sse.c:121-187`) are consistent across both strands and both extension directions
(checked line by line). With `KSW_EZ_SPLICE_CMPLX` a GC donor costs 5, AT 7 and GT 0–3, while
`-x splice` charges a short gap `2 + l` (`options.c:170-171`). `j1_splice_junctions.py` (120
planted genes, 600 introns, both genome strands): GT-AG 1,664/1,664 exact; GC-AG 24/373 off;
AT-AC 118/258 off (the planted AT-AC share of 10 % is far above the genomic ~0.1 %). Under
`-x splice:hq`: 0 GC-AG and 13 AT-AC off. On 2.17/2.24, before the miniprot splice model of
2.25 ("Improvement: use the miniprot splice model for RNA-seq alignment by default", NEWS):
GT-AG 43/1,664, GC-AG 153/373 and AT-AC 183/258 off, and `ts:A` wrong on 18/720 reads (2/720 on
2.26+). Improved upstream; held as a model trade-off.

**N3 (duplicate of lh3/minimap2#1307): dovetailed FR pairs never get 0x2.** `mm_pair` pairs a
"right" mate only with an earlier "left" mate in reference order (`pe.c:114-135`; the
orientation bit is `s ^ rev`, `pe.c:95`). If read 2's alignment starts before read 1's (5'
trimming), the pair is not formed. `p1_pairs_sr.py`: dovetails of 2, 5, 10 and 20 bp give
0/6 proper pairs each, on all four builds. Open in #1307, where the maintainer said "This is
something I want to improve as well."

## Fixed upstream (recorded, not raised)

- **F1:** in the ungapped short-read gap fill, an N scored `+sc_ambi` (+1) instead of −1
  through 2.28, so AS was +2 per N (`s1_scores_tags.v2.26.out`, "one N": AS − port = 2 on 6/6).
  Fixed by af09464 (r1263, 2.29): `align.c:828` now reads `opt->sc_ambi > 0? -opt->sc_ambi : opt->sc_ambi`.
- **F2:** on 2.17, `de:f` counted an N column as a match (`de:f:0` for an otherwise exact read
  with one N; port 1/L). Fixed by 161ae7f (r1079, 2.22), which introduced `mm_event_identity`
  (`align.c:997-1003`).

## Held up under execution

- **AS** against the manual's scoring for mismatches anywhere except the last four bases,
  N bases (2.29+), 1–12-bp insertions and deletions, clean reads, under `-x sr` (L = 100, 150),
  map-ont and `-x splice`; **NM, MD, cs, de** and **POS** against ports from the CIGAR: 180/180
  per block on all four builds (`de` with N excepted on 2.17, F2).
- **PAF** columns 3, 4, 8, 9, 10 and 11 with `-c` against the SAM record of the same read:
  180/180 (sr, map-ont). Without `-c` they are chain approximations, as the manual says
  (`minimap2.1:785`).
- **MAPQ** of uncontested hits (`s2:i:0`) against a port of `mm_set_mapq2`
  (`hit.c:432-485`: identity, the s1/cm penalties, `rl`, `min_chain_score`, the long-read
  `mapq_alt` cap, the floor of 1): 797/797 (`-x sr`, MAPQ spread 0–60) and 1,437/1,437
  (map-ont) on all four builds (`m2_mapq_port.py`).
- **Primary/secondary/supplementary and SA:** 120 long-read and 120 short-read chimeras.
  Exactly one primary and one hard-clipped supplementary per read, both segments at their
  origins, and every `SA` entry's RNAME/POS/strand/MAPQ/NM and clip lengths equal to the
  referenced record (240/240 each). Exact two-copy repeats: 1 primary + 1 secondary,
  MAPQ 0, `s2 == s1`, 120/120 (`c1_supplementary_sa.py`).
- **Pairing under `-x sr`:** proper-pair flag for FR fragments of 100–800 bp (on) and
  810–1,200 bp (off, `-F 800`), RF and FF (off), mates swapped (on), read-through into adapter
  (on). `TLEN` = ±fragment, RNEXT/PNEXT/0x20 consistent. A repeated mate is placed next to its
  unique partner 80/80 with MAPQ ≥ 20 (`p1_pairs_sr.py`, all four builds).
- **Splicing:** GT-AG junction placement exact on 1,664/1,664 error-free junctions (2.26+),
  `ts:A` relative to the read correct on 718/720 (`j1_splice_junctions.py`).

## Withdrawn suspicions

- `mm_filter_strand_retained` (`hit.c:283-299`, called at `map.c:335`) compacts the region
  array without `mm_sync_regs`. `id` and `parent` are not renumbered, but they stay consistent
  with each other, and the post-alignment `mm_set_parent` rebuilds both. No output path indexes
  by `parent` after the call, so there is no visible effect.
- `mm_set_mapq2` applies the BWA-like `mapq_alt` cap only when `!is_sr` (`hit.c:463`), although
  its comment says "mostly for short reads". This has been the design since fb8a1b55/311fa900
  (2017-10-31), so it is not a bug.
- `mm_align_sr_rna` counts matching positions instead of the exact-match run its comment
  describes (`align.c:377-382`, no `break`). It is a gate only (the DP result is validated
  afterwards) and exists only in `splice:sr` (2.29+, not in any surveyed version). **Not
  executed.**

## Not checked

`-x asm*` and `-x map-hifi`/`lr:hq` beyond what map-ont covers; `--MD`/`--cs` with `--eqx`;
`-L` long CIGARs; `--split-prefix` and multi-part indexes (`merge_hits`); `-x splice:sr` and
`--junc-bed`/`--spsc`; inversion records (`tp:A:I`); HPC indexes (`-H`, map-pb); `--qstrand`;
mappy; multithreaded output order; seeding sensitivity (`mid_occ`, `q_occ_frac`) beyond the
reads above; MAPQ of contested hits and of pairs (`mm_pair`'s blend) beyond the n_sub
comparison and the repeat-mate class.
