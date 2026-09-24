# Bowtie 2 audit against 477 published papers (2021–2026)

_Generated 2026-09-24 against `BenLangmead/bowtie2` `master` @ `58e34bf` (VERSION 2.5.5,
unreleased; last release 2.5.4) built here, and the release binaries 2.3.5.1, 2.4.2, 2.4.5,
2.5.1 and 2.5.4 (the cohort's most-cited versions and the current release). Focus: what a
paper takes from a Bowtie 2 run — the alignment score and tags, MAPQ, concordant/discordant
classification and `TLEN` under `-I/-X`, and the alignment summary that becomes "x % overall
alignment rate" — verified by executing the binaries on reads built from random references
where every edit, fragment length and repeat copy is known._

## What this is

The six-journal survey found **477 papers** in PNAS (239), *Nature* (190), *Cell* (37) and
*Science* (11), 2021–2026, that used Bowtie 2 — the survey's most-used short-read aligner not
yet audited, sitting under MACS2 (126 co-uses), deepTools (88), Picard (97) and samtools (224)
in ChIP-seq, ATAC-seq, CUT&RUN, Hi-C, CRISPR-screen, small-RNA and host-depletion pipelines.
The scoring, MAPQ, pairing and reporting code was read on `master` and every suspicion was run
on six builds with harnesses whose truths are computed independently in Python (the manual's
penalty formulas; a port of the default MAPQ calculator; a port of the pair classifier; counts
taken from the SAM for the summary).

## Findings (details and line citations in [`component-reviews/scoring-mapq-pairing-summary.md`](component-reviews/scoring-mapq-pairing-summary.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **BW1** | **CONFIRMED on `master`** (regression from 41ee86b, 2026-09-14, unreleased); 2.3.5.1–2.5.4 unaffected | **now** (before the next release) | `reportHits` computes mate 2's MAPQ with mate 2's own length passed as the opposite mate's length, so the perfect and minimum scores of a concordant pair are summed over 2 × mate 2. Mates of unequal length (the norm after trimming) get different MAPQs for the same pair: 40 / **23** for a 150/50-bp pair with 3 + 2 mismatches, 6 / **30** for a perfect 150/60-bp pair in a two-copy repeat. One-token fix with the port reproducing every value. |
| **BW2** | **CONFIRMED on 2.3.5.1, 2.4.2, 2.4.5, 2.5.1, 2.5.4 and `master`** | **now** | A mate reported as an unpaired alignment (`YT:Z:UP`) never carries `XS:i`: `printAlignedOptFlags` takes the paired second-best for any read that is part of a pair, and that field is only filled for concordant/discordant pairs. The record gets MAPQ 0/1 and the summary counts it under "aligned >1 times", but the tag most pipelines use to recognise a multi-mapper is absent (30 of 30 in the harness; 30 of 30 present with the six-line fix). |
| **BW3** | **CONFIRMED on all six builds** | now (report; code or manual) | `--no-mixed` also suppresses discordant alignments — discordant pairs are assembled from the mates' unpaired alignments, which `--no-mixed` stops the search from storing — while the manual says the option only disables the per-mate fallback and reserves `--no-discordant` for discordant pairs. 80 discordant pairs → 0 `YT:Z:DP`, "0 aligned discordantly", overall alignment rate 58 % instead of 82 %. |
| **BW4** | **CONFIRMED on all six builds** | now (report with mechanism; PR after the maintainers choose the shape) | A pair whose fragment is longer than `-X` by roughly 18–33 bp (100-bp reads, default scoring) gets one mate reported with a spurious 2–12-bp insertion near its end: the mate-rescue DP fits the read into the `-X` window by opening a gap, that alignment is reported as the mate's unpaired alignment, and the exact gap-free alignment found afterwards is dropped as "redundant" because it shares cells with it. 100 % of pairs in the band; MAPQ 23–42, no `XS:i`, `TLEN` capped at about `X + 18`; on a library with fragments ~N(380, 70) at the default `-X 500`, 50 of 12,000 mates (0.4 %) carry a false insertion and the same reads at `-X 1000` have none. Not in `--local` (soft clips absorb it). |
| N1 | note, verified | held | `-I/-X` are checked on the mapped extent while `TLEN` includes the outer soft clips unless `--soft-clipped-unmapped-tlen`: a `--local` pair with mapped distance 480 and 20-bp outer clips is concordant under `-X 500` with `TLEN` ±520; the option is documented, the interplay is not. Prior threads #180 and #346 (read in full). |
| N2 | note, verified, documentation | held | The manual says `-I/-X` with `-3/-5` "is applied with respect to the untrimmed mates"; the trimmed bases never reach the aligner (`pretrim5p = pretrim3p = 0` at every `setShape` call), so both the constraint and `TLEN` use the trimmed extents (fragment 520 with `-3 20 -5 20` is concordant under `-X 500`, `TLEN` ±480). |
| N3 | note, verified, documentation | held | `--score-min` is truncated toward zero: the local default `G,20,8` at L = 100 is 56.84 in the manual and 56 in the code (a read with 28 matching bases, score 56, is reported). |

**Held up under execution:** `AS:i` and `XM/XO/XG/NM/MD/CIGAR/POS` for mismatches at every
quality (including Q > 40 and Q = 0), N bases, 1–5-bp insertions and deletions, under the
default, `--ignore-quals`, `--mp`, `--np`/`--n-ceil`, `--rdg/--rfg`, `--phred64`, `--local`,
`--ma` and the presets (24/24 reads × 13 configurations × 6 builds); the default MAPQ for
unpaired reads against a port of `BowtieMapq2` (576 reads per build across repeat families
with 0–20 substitutions, both modes, three read lengths, `--mp 4,2`, presets) and for
concordant pairs on the releases; concordance and `TLEN` against a port of `peClassifyPair`
for fragment lengths across `-I 200 -X 500`, `--fr/--rf/--ff`, and overlap / containment /
dovetail under the defaults, `--no-overlap`, `--no-contain`, `--dovetail`; every line of the
alignment summary and the overall alignment rate against SAM-derived counts in the default
mode, `--no-mixed`, `--no-discordant`, both, and `-k 2`; `--un-conc/--al-conc/--un/--al`
record counts. Not checked: seed-search sensitivity (which alignments are found, beyond the
cases above), `-k`/`-a` alignment lists, the V1/V3 MAPQ calculators, `--un-gz` variants,
BAM input, `bowtie2-build` correctness beyond round-tripping the harness references,
`--xeq`, `--sam-append-comment`, and multithreaded output order.

## How the papers use Bowtie 2 (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 89 (2.4.2 ×24, 2.4.5 ×20, 2.3.5.1 ×19, 2.4.1 ×17, 2.3.4.1 ×15, 2.3.5 ×14, 2.2.9 ×13, 2.5.1 ×8, 2.5.4 ×4; 2.5.x 23) |
| paired-end named | 139 |
| `--very-sensitive` / `--very-sensitive-local` | 41 |
| `--local` or a local preset | 33; `--end-to-end` or an end-to-end preset 29 |
| `-X`/`--maxins` stated | 27 (2000 ×8, 700 ×8, 1000 ×3, 500 ×2, 800 ×2) |
| `--no-mixed` / `--no-discordant` | 24 / 20 (2 sentences name `--no-mixed` without `--no-discordant`) |
| `-k`/`-a` multi-reporting | 29 |
| MAPQ threshold applied afterwards | 60 (30 ×12, 10 ×8, 20 ×8, 0 ×11) |
| "uniquely mapped" / XS-tag filter | 27 |
| assay: ATAC 60, ChIP 59, RNA/small RNA 132, CUT&RUN/CUT&Tag 13, Hi-C 11, CRISPR screens 18, host depletion / metagenomics 35, bisulfite via Bismark 16 | |
| downstream: MACS2 126, deepTools 88, Picard 97, samtools 224, variant calling 48 | |

Which finding reaches which paper: BW1 would reach every paired-end run on the next release
(unequal mate lengths after trimming; a MAPQ filter then splits pairs); BW2 reaches every
paired-end run whose pipeline filters on the `XS:i` tag or on "uniquely mapped" (27 papers say
so) — the affected records are mates of pairs where the other mate failed; BW3 reaches the runs
that use `--no-mixed` alone and read the discordant line or look for discordant pairs; BW4
reaches every end-to-end paired-end run whose fragment-length distribution crosses `-X`
(the default 500, or 700/1000 as stated), with the affected mates passing MAPQ filters and
feeding indel callers (48 papers call variants), insert-size distributions and `TLEN`-based
fragment filters (ATAC, Hi-C).

The profile (`bowtie2_profile.py`, `bowtie2_profiles.jsonl`, `profile_run.log`) was run
offline against the survey's stored evidence sentences (no route to Europe PMC from the session),
so every count is a lower bound over a few hundred characters per paper.

## Filing channel

`BenLangmead/bowtie2` has no `CONTRIBUTING.md`, no issue or PR template and no AI policy in the
tree (`README.md`, `MANUAL.markdown`, `.github/` searched; `.github/` holds only the two test
workflows). Bug reports go to the GitHub tracker (the manual's "Getting help" points to the
mailing list and the tracker); CI runs `make simple-test` (`scripts/test/simple_tests.pl`
against the normal, debug and sanitized builds) on Linux, Linux without AVX2 and macOS for
every PR. Kit under [`upstream/`](upstream/): four issue texts (BW1–BW4), two PR bodies with
`git am`-able patches (BW1, BW2), and the test runs. No fork of `BenLangmead/bowtie2` exists
under `cindykrafft` yet.

## Files

| path | what |
|---|---|
| `component-reviews/scoring-mapq-pairing-summary.md` | the review: BW1–BW4, N1–N3 with code citations, held-up list, withdrawn suspicions |
| `verify/_synth.py` | reference/index/read builders, SAM and summary parsers, ports of the penalty table, `--score-min`, `BowtieMapq2` and `peClassifyPair` |
| `verify/s1_scoring_tags.py` | AS and tags vs the manual's formulas; the `--score-min` boundary (N3) |
| `verify/m1_mapq.py` | MAPQ vs the port, unpaired and paired, equal and unequal mate lengths (BW1) |
| `verify/p1_pair_constraints.py` | `-I/-X`, orientations, overlap/contain/dovetail vs the port; trimming and soft clips vs `TLEN` (N1, N2) |
| `verify/a1_summary_arithmetic.py` | the summary vs the SAM; `XS:i` on unpaired mates (BW2); `--no-mixed` and discordant pairs (BW3); `--un-conc`/`--al-conc` |
| `verify/x1_maxins_boundary.py`, `verify/x2_maxins_realistic_library.py` | the `-X` boundary scan and the realistic library (BW4) |
| `verify/*.out`, `*.v<version>.out`, `*.patched.out` | captured output per build; `.patched.out` from the fix branches |
| `bowtie2_profile.py`, `bowtie2_profiles.jsonl`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit |

## Next steps

1. Fork `BenLangmead/bowtie2`; the two fix branches are pushed; file BW1 (issue + PR) and BW2
   (issue + PR) — BW1 first, it should land before 2.5.5 ships.
2. BW3 and BW4 as reports once one of the first two has a reply (two-unanswered-filings cap);
   BW4 carries the mechanism and an offer to prepare the PR in whichever shape the maintainers
   prefer.
3. N1–N3 held; N2 and N3 could go into one documentation issue later.
