# minimap2 audit against 173 published papers (2021–2026)

_Generated 2026-10-18 against `lh3/minimap2` `master` @ `3c28777` (2026-05-19, "Release
minimap2-2.31 (r1302)", which is also the latest release; `git ls-remote` shows nothing pushed
since), built here, and the 2.17-r941, 2.24-r1122 and 2.26-r1175 tags built from source (the
cohort's three most-cited versions). Focus: what a paper takes from a minimap2 run. That means
`AS`/`NM`/`ms`/`MD`/`cs`, the `de`/`dv` divergence tags, MAPQ, chaining scores (`s1`/`s2`),
primary/secondary/supplementary choice and `SA`, PAF columns, splice-junction placement and
`ts:A` under `-x splice`, and the proper-pair flag and `TLEN` under `-x sr`. All of it was
verified by executing the builds on reads made from random references where every edit,
junction, fragment and repeat copy is known._

## What this is

The six-journal survey found **173 papers** in *Nature* (86), PNAS (71), *Cell* (11) and
*Science* (5), 2021–2026, that used minimap2. It is the survey's most-used long-read aligner,
upstream of variant calling, transcript and isoform analysis, assembly polishing and
evaluation, and metagenomic read assignment. The mapping, scoring, MAPQ, pairing, splicing and
output code was read on `master` (component review below), and each suspicion was run on
four builds. The harnesses compute their truths independently in Python: the manual's scoring
recomputed from each record's own CIGAR; ports of `mm_set_mapq2`, `mm_est_err` and the
max-segment rescoring; and the planted fragments, junctions and repeat copies.

## Findings (details and line citations in [`component-reviews/scoring-mapq-pairing-splice.md`](component-reviews/scoring-mapq-pairing-splice.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **MM1** | **CONFIRMED on 2.17, 2.24, 2.26 and 2.31 (`master`)** | **now** | Under `-x sr`, when the left or right extension reaches the read end (`ez->reach_end`, end bonus 10), the CIGAR is the end-to-end path but `mm_align1` adds `ez->max`, the clipped path's score, to `dp_score`. `AS:i` is then above the score of the reported alignment: `150M NM:i:1` with the mismatch 1/2/3/4 bp from either end prints `AS:i:298/296/294/292` instead of 290. On 20,000 simulated Illumina-like 2 × 150 bp pairs, 2,803 of 40,000 primary records (7.0 %) are overstated by 2–16. Two-line fix (`ez->reach_end? ez->mqe : ez->max`): AS then equals the CIGAR's score on 40,000/40,000 and no other field changes. The long-read presets (end bonus −1) are unaffected. |
| **MM2** | **CONFIRMED on `master`** (instrumented and patched builds); same line in 2.17/2.24/2.26 | held | `mm_set_parent` resets `n_sub` for every new primary except `r[0]` (`hit.c:133` vs `:182`), so the best hit carries its count from the chaining pass into the post-alignment pass and the MAPQ penalty `4.343·ln(n_sub+1)` counts the same competitors twice. Carried over in 776 of 2,880 `-x sr` calls and 72 of 432 map-ont calls on two-copy repeats; MAPQ is 1–2 lower on 52 of 2,880 sr records (1.8 %), all correctly placed; no MAPQ change for long reads. Small, and the heuristics were tuned with it. |
| **MM3** | **CONFIRMED on all four builds** | held | `mm_est_err` tests the right end with `qlen − r->qs` instead of `qlen − r->qe` (`esterr.c:61`), so `dv:f` counts a missing minimizer at the end of almost every hit. Error-free reads inside the reference get `dv:f` 0.0001–0.0008 instead of 0 (60/60 match the port with `qs`). PAF without `-c` only; tiny. |
| N1 | note, verified | held | Since 2.22 (161ae7f) the `ms:i`/`dp_max` rescoring charges every gap in `-x sr` `O + E` whatever its length (`align.c:284,293`). A 12-bp deletion gives `ms − AS = 22`; it steers short-read MAPQ and pairing. The maintainer calls this rescoring by design (#1000); the manual's "DP score of the max scoring segment" does not say so. Documentation. |
| N2 | note, verified | held | `-x splice` places 24/373 GC-AG and 118/258 AT-AC introns of error-free reads at a nearby GT donor with a compensating 1–5-bp indel (the low splice gap cost against the donor penalties). GT-AG is exact on 1,664/1,664; `splice:hq` misplaces 0 GC-AG. On 2.17/2.24, before the 2.25 splice model, 43/1,664 GT-AG and 153/373 GC-AG junctions were off and `ts:A` was wrong on 18/720 reads. Improved upstream; model trade-off. |
| N3 | **duplicate** of lh3/minimap2#1307 (open) | — | Dovetailed FR pairs (read 2 starting 2–20 bp before read 1, e.g. after 5' trimming) never get 0x2 (0/24 on all builds). The maintainer acknowledged it in #1307. |
| F1, F2 | fixed upstream | — | F1: N scored +1 instead of −1 in the ungapped short-read gap fill through 2.28 (AS +2 per N; fixed in 2.29, af09464). F2: `de:f` treated N as a match on 2.17–2.21 (fixed in 2.22, 161ae7f). |

**Held up under execution:** `AS` against the manual's scoring (outside the MM1 case),
`NM`, `MD`, `cs`, `de` and `POS` for mismatches, Ns, 1–12-bp indels and clean reads under
`-x sr`, map-ont and `-x splice` (180/180 per block, all builds). PAF columns 3/4/8/9/10/11
with `-c` against the SAM record (180/180). MAPQ of uncontested hits against a port of
`mm_set_mapq2`: 797/797 (`-x sr`, values spread 0–60) and 1,437/1,437 (map-ont), all builds.
Primary/supplementary choice, hard clipping and every `SA` field on 240 chimeric reads
(240/240), and primary + secondary with MAPQ 0 and `s2 == s1` in exact repeats (120/120).
Under `-x sr`: the proper-pair flag across 100–1,200-bp FR/RF/FF fragments (boundary exactly
at `-F 800`), `TLEN`, RNEXT/PNEXT/0x20, and placement of a repeated mate next to its partner
(80/80, MAPQ ≥ 20). GT-AG junction placement (1,664/1,664) and `ts:A` (718/720) on 2.26+.
Withdrawn after reading or running: `mm_filter_strand_retained` without a resync (no visible
effect), the `!is_sr` guard on `mapq_alt` (design since 2017), and the `mm_align_sr_rna`
counting loop (`splice:sr` only, 2.29+, **not executed**). Not checked: asm/HiFi presets beyond
map-ont, `-L`, multi-part indexes, `splice:sr`, `--junc-bed`, inversions, HPC, `--qstrand`,
mappy, MAPQ of contested hits and pairs beyond the MM2 comparison.

## How the papers use minimap2 (lower bounds from the survey cache; `minimap2_profile.py`, `profile_run.log`)

| signal | papers |
|---|---|
| version stated | 77 (2.17 ×24, 2.24 ×16, 2.26 ×8, 2.22 ×5, 2.20 ×4, 2.28 ×3, 2.12 ×3; 96 unstated) |
| `-ax` (SAM output) | 27 |
| ONT / map-ont | 27; PacBio / HiFi / map-pb 22 |
| splice / `-x splice` | 13 |
| `-x sr` / short reads named | 5 |
| asm5/asm10/asm20 | 7 |
| `--secondary=no` | 10; secondary/supplementary named 12 |
| MAPQ named | 1; `--cs`/paftools 2 |
| downstream stage named | alignment/mapping 140, variant calling 9, read trimming 10 |

Which finding reaches which paper: MM1 reaches every `-x sr` run whose downstream step uses
`AS:i`, such as AS thresholds or assigning reads between references by AS (host/graft or
strain separation). Across 2.17–2.31, 7 % of records carry an inflated value, so reads ending
in a mismatch are favoured over reads with the same mismatch inside. MM2 shifts short-read
MAPQ by 1–2 in near-identical repeats. MM3 affects `dv:f` from PAF runs without `-c`. N2
reaches `-x splice` junction coordinates for GC-AG introns (about 1 % of human introns), and
did so much more on 2.17/2.24, which 40 of the 77 version-stating papers used.

The profile was run offline against the survey's stored evidence sentences (one per paper),
so every count is a lower bound.

## Filing channel

`lh3/minimap2` has no `CONTRIBUTING.md`, no issue or PR template and no AI policy in the tree.
The README's "Getting help" sends bugs to the issue page. CI compiles only (gcc/clang x86_64,
aarch64, macOS arm64), and there is no test suite. Kit under [`upstream/`](upstream/): the MM1
issue text, the PR body, a `git am`-able patch against `3c28777`, test runs and the duplicate
check. **Fork needed: lh3/minimap2.** No fork exists under `cindykrafft` yet.

## Files

| path | what |
|---|---|
| `component-reviews/scoring-mapq-pairing-splice.md` | the review: MM1–MM3, N1–N3, F1–F2 with code citations, held-up list, withdrawn suspicions, not checked |
| `verify/_synth.py` | reference/read builders, SAM/PAF parsers, ports of the scoring, NM, MD, cs, de |
| `verify/s1_scores_tags.py` | AS/NM/MD/cs/de/POS vs ports for sr, map-ont, splice; ms gap model (N1); PAF columns (MM1, F1, F2) |
| `verify/r1_as_prevalence.py` | 20,000 Illumina-like pairs, AS vs CIGAR, tested vs fixed build (MM1) |
| `verify/x1_as_issue_repro.py` | the five-read reproduction in the MM1 issue |
| `verify/m1_nsub_mapq.py` | n_sub carry-over: instrumented, tested and fixed builds on two-copy repeats (MM2) |
| `verify/m2_mapq_port.py` | MAPQ of uncontested hits vs a port of `mm_set_mapq2` |
| `verify/d1_dv_divergence.py` | `dv:f` on error-free reads vs the `qs`/`qe` ports (MM3) |
| `verify/p1_pairs_sr.py` | proper pairs, TLEN, mate fields, repeat-mate placement, dovetails (N3) |
| `verify/j1_splice_junctions.py` | planted genes and introns: junction placement by motif, `ts:A` (N2) |
| `verify/c1_supplementary_sa.py` | chimeras, supplementary records, SA tag, repeat secondaries |
| `verify/*.out`, `*.v<version>.out`, `*.patched.out` | captured output per build; `.patched.out` from `fix/as-end-to-end-extension` |
| `minimap2_profile.py`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit |

## Next steps

1. Fork `lh3/minimap2`; push `fix/as-end-to-end-extension`; file MM1 (issue, then PR).
2. MM2 only after a maintainer reply, as an issue offering the one-line patch, framed as a
   question about intent.
3. MM3, N1 and N2 held. N3: #1307 is open; any comment there waits until the thread has been
   read in full.
