# Component: Trimmomatic trimming core (`main` @ `ef98d62`, 2026-07-03, version 0.41)

Read in full on `main` @ `ef98d6252abeae80cfee36acf9e0e1055097da0b` (the merge of the
V0.41 release branch): `trim/IlluminaClippingTrimmer.java` (968 lines: adapter file
handling, palindrome and simple mode, the 4-bit packing and seeds, the log-odds scoring),
`trim/SlidingWindowTrimmer.java` (69), `trim/MaximumInformationTrimmer.java` (111),
`trim/LeadingTrimmer.java`, `trim/TrailingTrimmer.java`, `trim/MinLenTrimmer.java`,
`trim/MaxLenTrimmer.java`, `trim/CropTrimmer.java`, `trim/HeadCropTrimmer.java`,
`trim/TailCropTrimmer.java`, `trim/AvgQualTrimmer.java`, `trim/BaseCountTrimmer.java`,
`trim/ToPhred33Trimmer.java`, `trim/ToPhred64Trimmer.java`, `trim/TrimmerFactory.java`,
`fastq/FastqRecord.java` (230: the trimmed-view constructor and `getQualityAsInteger`),
`fastq/FastqParser.java` (165: parsing and the Phred-offset histogram),
`fastq/PairingValidator.java`, `TrimStats.java`, `TrimmomaticPE.java`, `TrimmomaticSE.java`,
`Trimmomatic.java`, `threading/BlockOfWork.java` (229: the per-block trimming loop, the
paired/unpaired routing, the trim-log record), the trim-log and trim-stats collectors and
`threading/pipeline/ThreadedPipeline.java`; plus `README.md` ("Description of Trimming
Steps", "The Adapter Fasta") as the statement of intended behaviour, `versionHistory.txt`,
the shipped `adapters/*.fa`, and the project's JUnit tests for the trimmers. The
compression, file-name templating and logging code was not read beyond what the runs
exercise.

Every suspicion was **executed on the shipped code**: the jar built from `ef98d62` with
`mvn package` (JDK 25, version string 0.41), the 0.41 and 0.40 release jars from the GitHub
releases, the 0.39 release zip (the cohort's most-cited version), and the `v0.38`, `v0.36`,
`v0.33` and `v0.32` tags compiled with `javac` (the usadellab.org download site is not
reachable from this session, so those four are builds of the tagged sources with the
tagged `adapters/`; the tagged `TruSeq3-PE.fa` differs from `main`'s only by a trailing
newline). Harnesses are in `../verify/` with captured output; each confirmed finding was
run on every version through `../verify/version_scope_cli.py`. References are independent
Python implementations of the documented rules (`../verify/tm_ref.py`), written from the
README, run on synthetic reads with known adapter positions, insert sizes and qualities.

Cohort numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### TM1 — CONFIRMED on `main`, 0.41, 0.40, 0.39, 0.38, 0.36, 0.33 and 0.32: ILLUMINACLIP palindrome mode charges `int(Q/10)` per mismatch, not `Q/10`

**Code.** The README ("The Adapter Fasta") defines one score for both adapter-detection
modes: "Each matching base adds just over 0.6, while each mismatch reduces the alignment
score by Q/10." Simple mode does that in floating point,
`IlluminaClippingTrimmer.java:556` (`likelihood[i] = -quals[recPos] / 10.0f`). Palindrome
mode divides two `int`s: `:493-496`

```java
if (qual1 < qual2)
    likelihood[i] = -qual1 / 10;
else
    likelihood[i] = -qual2 / 10;
```

so a mismatch costs the integer part of Q/10 — nothing at Q2–Q9 (`#` … `*` in Phred+33),
1 at Q10–Q19, 2 at Q20–Q29, 3 at Q30–Q39, 4 at Q40. The truncation was there in 0.32
(`builds/v0.32/.../IlluminaClippingTrimmer.java:478-480`) and is unchanged on `main`. It
makes every palindrome alignment with mismatches at non-multiple-of-10 qualities score
higher than documented, by Σ frac(Q/10) — up to 0.9 per mismatch — so pairs whose
documented score is just below `palindromeClipThreshold` are clipped anyway: forward read
cut to the insert, reverse read dropped unless `keepBothReads`.

**Verified** (`../verify/tm1_palindrome_penalty.py` → `tm1_palindrome_penalty.out`;
`version_scope_cli.*.out`; `../upstream/mcve_outputs.txt`):

| what | result |
|---|---|
| one 2x50 pair, 42-nt insert reading through into the TruSeq3-PE adapters, two read-1 errors at Q19; 58 aligned bases, 56 matches | documented score 29.915 (< 30, keep both); integer-penalty score 31.715 (≥ 30); **shipped: forward-only survivor of 42 nt, reverse dropped** (`Both Surviving: 0 … Forward Only Surviving: 1`) |
| grid: 12 mismatch qualities (Q2 … Q40) × 1–3 read-1 errors, 200 pairs each, insert 42, 2x50, threshold 30 | shipped decision equals a port of the integer rule 7,200/7,200; differs from the documented rule for **600 of 7,200** pairs — the three rows Q15 × 3 errors (28.61 vs 30.11), Q19 × 2 (29.92 vs 31.72), Q19 × 3 (27.41 vs 30.11): documented clips 0/200, shipped 200/200 |
| control rows | Q10, Q20, Q30, Q40 (penalty a whole number under both rules) agree 200/200 in every row |
| simulated 2x50 library, 4,000 pairs, inserts 20–70, Illumina-like qualities, errors at 10^(−Q/10) | documented rule clips 1,745 pairs, integer rule and shipped clip 1,768: **23 pairs flip** (0.6 %), shipped == integer port 4,000/4,000 |
| 2x75, 2x100, 2x150 libraries (4,000 / 4,000 / 3,000 pairs) | 0 flips: the palindrome alignment then covers 2R − L ≥ 58 bases for every insert that qualifies, and at threshold 30 a couple of truncated penalties no longer decide |
| version scope (`version_scope_cli`): 200 pairs with two Q19 errors (documented 0/200 clipped) | `main`, 0.41, 0.40, 0.39 release, 0.39/0.38/0.36/0.33/0.32 builds: **200/200 clipped**; control with the errors at Q20: 0/200 on all nine |

**Who is exposed.** Every paired-end run with `ILLUMINACLIP` and a `Prefix…/1`,
`Prefix…/2` pair (the shipped TruSeq2/3-PE and Nextera files; 131 cohort papers mention
adapter clipping, 15 name `TruSeq3-PE`, lower bounds). The effect is confined to
alignments whose documented score lies within Σ frac(Q/10) below the threshold: short
reads or short overlaps with a few low- or mid-quality mismatches. In the 2x50 simulation
that is 0.6 % of pairs; with 75-nt or longer reads none flipped. The direction is always
towards clipping more (and, without `keepBothReads`, dropping the reverse read), so the
shipped palindrome mode is more permissive than the manual and than simple mode on the
same mismatch. Not a wrong number at typical read lengths; a wrong decision at the margin,
reproducible on every version.

**Fix shape** (`../upstream/0001-*.patch`): divide by `10.0f` in both branches, as simple
mode does. `IlluminaPalindromeMismatchPenaltyTest` (2 tests) fails on unmodified `main`
(`expected: not <null>` — the reverse read was dropped) and passes with the patch; the
`trim` package tests go 166 → 168 and the full suite 259 → 261, all passing.

**Upstream.** Tracker searched 2026-09-13 (semantic search, several phrasings): no prior
report. Nearest: #52 "question about ILLUMINACLIP 2:30:10", #16 "keepBothReads: flag or
boolean?", #56 and #15 (forward-only survivors, user questions).

### TM2 — CONFIRMED on `main`, 0.41, 0.40, 0.39, 0.38, 0.36, 0.33 and 0.32: MAXINFO trims every read to one base once `targetLength` reaches 248 at strictness 0.1, 495 at 0.2, or 711 at any strictness

**Code.** `MaximumInformationTrimmer` precomputes two tables in log space — the length
score `log(1/(1+e^{target−i−1})) + (1−s)·log(i+1)` (`:48-56`) and the per-quality term
`s·log(1 − 10^{−(q+0.5)/10})` (`:64`) — and scales both to `long` so that the per-read
loop (`:85-100`) can add them in integer arithmetic. The scale is
`normRatio = Math.max(calcNormalization(lengthScoreTmp, 2000), calcNormalization(qualProbTmp, 2000))`
(`:67-68`), with `calcNormalization` returning `Long.MAX_VALUE / (maxVal · margin)`
(`:27`). `Math.max` selects the *larger* ratio, i.e. the one computed for the table with
the *smaller* maximum — the quality table, whose largest magnitude is ≈ 1.23·s
(`calcNormalization` seeds `maxVal` with `array[0]` instead of `|array[0]|`, `:19`, so the
first entry, ≈ 2.22·s, is skipped). Applied to the length table, whose first entries are
≈ −(target − 1), the product leaves `long` range once (target − 1) > 2000 · 1.23 · s:
the cast `(long) (array[i] * ratio)` (`:34`) saturates at `Long.MIN_VALUE`, and
`long score = ls + accumQuality` (`:94`) with a negative `accumQuality` wraps to a large
positive value at position 0, which becomes `maxScore` (`:96-99`); no later position
beats it, so `maxScorePosition` stays 1 and the read is cut to one base (`:105-106`).
Independently, for target ≥ 711 `Math.exp(parLength − i − 1)` (`:48`) is `Infinity` at
the first positions, `Math.log(1/(1+Infinity))` is `−Infinity`, and the same saturation
follows at any strictness. The code is unchanged since 0.32 apart from formatting.

**Verified** (`../verify/tm2_maxinfo_normalisation.py` → `tm2_maxinfo_normalisation.out`;
`version_scope_cli.*.out`):

| what | result |
|---|---|
| closed form: (target − 1) · Long.MAX_VALUE / (2000 · 1.2306 · s) > Long.MAX_VALUE | target > 247.2 (s = 0.1), > 493.3 (0.2), > 739.5 (0.3), > 1231.8 (0.5) |
| 300-nt all-Q40 read, 25 target lengths × 6 strictness values, shipped vs a double-precision evaluation of the same formula | double rule keeps 300 in every cell; shipped keeps **1 base in 41 of 150 cells**: target ≥ 248 at s = 0.1, ≥ 495 at s = 0.2, ≥ 711 at every s (0.1 … 1.0); target 247/0.1, 490/0.2 and 710/0.3–1.0 keep 300 |
| 100 MiSeq-like 2x300 reads (Q37 then Q20), `MAXINFO:800:0.5` | shipped surviving lengths (1, 1) for all 100; double rule (300, 300) |
| held up: 5,000 150-nt reads with an Illumina-like profile at `40:0.5`, `35:0.5`, `100:0.2`, `50:0.8`, `36:0.9`, `150:1.0`, `150:0` | shipped == double rule **5,000/5,000 under each setting**, 0 reads differ by even one base |
| version scope: 300-nt Q40 read, `247:0.1` / `248:0.1` / `250:0.1` / `500:0.2` / `800:0.5` | 300 / 1 / 1 / 1 / 1 on `main`, 0.41, 0.40, 0.39 release and the 0.39/0.38/0.36/0.33/0.32 builds; `40:0.5` keeps 300 on all |

**Who is exposed.** Anyone running MAXINFO with a target length in the hundreds at low
strictness — 2x250/2x300 MiSeq amplicon or assembly libraries with `MAXINFO:250:0.1`-style
settings — or with a target above 710. The cohort's two MAXINFO settings (`100:0.2`,
`35:0.5`) are far from the boundary and held up. When it hits, it is not subtle: after
`MINLEN` every read is dropped, which a user would notice but might attribute to the data.
The manual gives no bound on `targetLength`.

**Fix shape** (`../upstream/0002-*.patch`): `Math.min` instead of `Math.max` (the smaller
ratio keeps both tables inside `long`: the length table's magnitude is then ≤
`Long.MAX_VALUE / 2000` and the quality sum over `LONGEST_READ` bases ≤ `Long.MAX_VALUE / 2`),
`Math.abs(array[0])` in `calcNormalization`, and `log(1/(1+e^x)) = −x` for `x > 700`.
`MaximumInformationTrimmerLargeTargetTest` (4 tests): 3 fail on unmodified `main`
(`expected: <300> but was: <1>`), all pass with the patch; `trim` package 166 → 170, full
suite 259 → 263. The harness rerun on the patched jar is `tm2_maxinfo_normalisation.patched.out`.

**Upstream.** Tracker searched 2026-09-13: no prior report. Nearest: #74 "About
MAXINFO:40:0.8" (closed), #22 "SLIDINGWINDOW vs MAXINFO" (closed), #84 "TrimmomaticPE
discarding (almost) all reads at Q36" (closed, a SLIDINGWINDOW question).

### N1 — NOTE (design, documented loosely): simple-mode ILLUMINACLIP scores the best sub-range of the alignment, not the whole overlap

`calculateDifferenceQuality` (`:540-567`) builds the per-base log-odds vector and returns
`calculateMaximumRange` (`:569-626`), a greedy merge of same-sign runs that keeps a
negative run only when both neighbours outweigh it; the score is the largest merged run,
not the sum. The README's sentence reads as a sum. Executed
(`../verify/heldup_illuminaclip_simple.py`, section A): on 6,000 150-nt reads with adapters
at random positions and realistic errors, the shipped clip position equals the
documented-sum rule for 5,971 (threshold 10) and 5,949 (threshold 7) reads and the
best-sub-range port for 5,982 / 5,959; the residual differences are reads with a
high-quality mismatch near the end of a short fragment (sum below threshold, sub-range
above) and the seed sampling of N2. Design choice — it makes the mode more tolerant of a
bad base near the alignment end — but the score is not the one the README describes.

### N2 — NOTE (by reading, with one executed symptom): the 16-base seed is sampled every fourth adapter position for adapters of 24 nt and longer

`IlluminaLongClippingSeq` keeps only every `INTERLEAVE = 4`th 16-mer of the adapter
(`:769-772`, `offset = i - j * INTERLEAVE`, `:803`), while medium (16–23 nt) adapters keep
all and short ones are matched through a mask. An adapter occurrence whose errors leave
no clean 16-mer at positions 0, 4, 8, … but one at another offset is not seeded. In the
simple-mode simulation this is part of the 0.5 % of reads where the shipped build leaves
an adapter that both references find (e.g. read `r229`, adapter at 119, in
`heldup_illuminaclip_simple.out`). Performance trade-off; the README describes the seed
as "16 bases" without the stride.

### N3 — NOTE (design, undocumented): every quality-based step scores an `N` base as quality 0

`FastqRecord.getQualityAsInteger(true)` (`:148`, `:156`) returns 0 for `N` whatever the
quality character says, and every trimmer calls it with `true`. LEADING/TRAILING therefore
remove Ns (the README's "low quality or N bases" says so for those two), but SLIDINGWINDOW,
AVGQUAL, MAXINFO and the ILLUMINACLIP mismatch penalty also see 0 there. The references
had to adopt it to match (`heldup_quality_trimmers.out`: "without that the ports differ").

### N4 — NOTE (design, undocumented): SLIDINGWINDOW drops every read shorter than the window, whatever its quality

`SlidingWindowTrimmer.java:32-33` returns `null` for `quals.length < windowLength`.
Executed: all-Q40 reads of 1, 2 and 3 nt are dropped by `SLIDINGWINDOW:4:15` and a 5-nt
one by `SLIDINGWINDOW:8:15` (`heldup_quality_trimmers.out`, section A). Harmless with the
usual `MINLEN:36`, visible with a large window and no MINLEN (a cohort paper uses
`SLIDINGWINDOW:10:20`). Otherwise the step held up: the cut lands at the end of the last
passing window, then trailing bases below the per-base threshold are removed
(`:54-58`), and a first failing window drops the read — as-coded and documented ports
agree with the shipped build on 20,000 reads under seven settings.

### N5 — NOTE (off-by-one, cosmetic): TRAILING drops a read whose only qualifying base is the first

`TrailingTrimmer.java:20` loops `for (int i = quals.length - 1; i > 0; i--)`, never
testing index 0, so a read whose first base is the only one at or above the threshold is
dropped instead of kept as a 1-nt read (LEADING keeps the mirror case as 1 nt). Executed:
`TRAILING:20` on a 40-nt read with a single Q30 first base → dropped; with the Q30 base
last → 40 nt; first two bases Q30 → 2 nt (`heldup_quality_trimmers.out`, B). The
project's own `TrailingTrimmerTest.testTrailingDropSingleBaseHigh` asserts this behaviour,
so it is known; no realistic pipeline keeps 1-nt reads.

### N6 — NOTE (design): automatic Phred-offset detection errors out on high-quality Phred+33 data and silently picks Phred+64 for quality characters above `o`

`FastqParser.determinePhredOffset` (`:100-117`) histograms the quality characters of the
first 10,000 reads and counts two windows, 33–58 (Phred+33 Q0–Q25) and 80–104 (Phred+64
Q16–Q40); it answers 33 or 64 only if exactly one window is non-empty. Executed
(`heldup_quality_trimmers.out`, E): typical Phred+33 and Phred+64 files are detected;
a Phred+33 file whose first 10,000 reads are all Q27–Q40 (a pre-filtered or binned
high-quality library) exits with "Unable to detect quality encoding" (issue #42, an
AVITI data set, is this symptom; closed 2026-01-08); a Phred+64 file that is all Q2–Q15
does the same; and a Phred+33 file with qualities up to Q93 (PacBio HiFi FASTQ) is
**detected as Phred+64** and processed with every quality 31 too low. The escape hatch is
`-phred33`/`-phred64`; the tool is for Illumina data. Noted because the last case is
silent.

### N7 — NOTE (design, bookkeeping): paired input files of unequal length are truncated to the shorter without a warning

`BlockOfWork.processPE` iterates `min(len1, len2)` pairs (`:90`) and `TrimStats.logPair`
counts only pairs with both records (`:41-42`). Executed: 100 forward + 90 reverse reads
→ `Input Read Pairs: 90`, the ten extra forward reads appear in no output file; with
`-validatePairs` a `WARNING: Pair validation failed at record: 90` is printed and the
result is the same (`heldup_palindrome_pe.out`, D). versionHistory 0.35 calls this
"Tolerate different length input files in paired mode", so it is intended.

### N8 — NOTE (documentation): MAXINFO's quality term uses (Q + 0.5)/10, and HEADCROP/CROP edge cases

`qualProbTmp[i] = log(1 − 10^{−(0.5+i)/10}) · strictness` (`MaximumInformationTrimmer.java:64`):
the error probability of a base with quality Q is taken as 10^{−(Q+0.5)/10}, half a
Phred unit better than the nominal value; the README does not give the formula. Executed
as part of TM2's held-up rows (the double-precision reference uses the same +0.5).
Also: `HEADCROP:n` drops a read of exactly `n` bases (`HeadCropTrimmer.java:86-87`) while
`CROP:0` writes a zero-length record (`CropTrimmer.java:29-32`; both in
`heldup_quality_trimmers.out`, C) — consistent enough, but the two empty-read conventions
differ.

## Withdrawn (own suspicions that execution killed)

- **Palindrome `minAdapterLength` off by one.** `maxCount = max(seqlen1, seqlen2) − 15 − minPrefix`
  (`:410`) looked like it might allow one adapter base fewer than `minAdapterLength`. The
  insert sweep with `minAdapterLength` 1, 8 and 20 on 2x100 and 2x150 pairs matches the
  reference at every insert length (`heldup_palindrome_pe.out`, A: 120/120 and 170/170 for
  every file and setting); the boundary is where the manual says.
- **Simple mode cannot find a 3' adapter fragment shorter than the seed.** The masked
  comparison (`calcSingleMask(packRec.length − i)`, `:797`) does find them: at threshold 7
  fragments of 12 nt and longer are clipped 200/200 (11 nt: 0/200), at threshold 10
  fragments of 16 nt and longer are clipped … *(section B of `heldup_illuminaclip_simple.out`)*,
  exactly where `int(threshold / 0.60206)` (capped at 15) says the minimum overlap is.
- **Results depend on `-threads`.** The block pipeline preserves order through the
  `Future` queue; four output files, `-summary` and `-trimlog` are byte-identical for
  `-threads 1/2/4/8` in PE mode and the SE output for 1/4/8 (`heldup_palindrome_pe.out`, C).
- **`-summary` percentages or the trim log disagree with the log line.** The `-summary`
  file equals the expected nine lines to the printed two decimals, and all 6,000 trim-log
  lines equal (name, surviving length, first surviving base, end, bases trimmed from the
  end) computed from the per-read reference (`heldup_palindrome_pe.out`, B).
- **`AVGQUAL` integer truncation.** `total < qual * seq.length()` is an exact integer
  comparison of the mean against the threshold; 5,000 reads agree with the reference at
  two thresholds.

## What held up (executed, not just read)

- **SLIDINGWINDOW** (`heldup_quality_trimmers.out`, A): 20,000 reads of 50–250 nt with
  ~1 % N under `4:15`, `4:20`, `5:20`, `4:30`, `3:20`, `4:5`, `10:25` — shipped equals the
  as-coded port and the documented reading 20,000/20,000 in every case.
- **LEADING/TRAILING** at 3, 20, 30: 20,000/20,000 each (TRAILING vs the documented rule
  and vs the as-coded rule, which differ only in N5's 1-nt case).
- **MINLEN, MAXLEN, CROP, HEADCROP, TAILCROP, AVGQUAL, BASECOUNT** on 5,000 reads of
  1–200 nt: 5,000/5,000 each; the chained `LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36`
  5,000/5,000.
- **TOPHRED33/TOPHRED64**: 200/200 reads round-trip exactly in both directions;
  TOPHRED33 on Phred+33 input is a no-op (D).
- **Phred auto-detection** on ordinary Phred+33 and Phred+64 files (E).
- **MAXINFO at typical settings**: 5,000 reads × 7 settings equal a double-precision
  evaluation of the formula (TM2 table).
- **ILLUMINACLIP palindrome geometry** (`heldup_palindrome_pe.out`, A): for TruSeq3-PE,
  TruSeq3-PE-2 and NexteraPE-PE, 2x100 and 2x150, inserts 0 … R+19 one pair each, with
  `2:30:10`, `2:30:10:1:true` and `2:30:10:20:false` — the shipped outcome (forward
  clipped to the insert, reverse dropped or kept, or the simple-mode clip of the leftover
  fragment) equals the reference 120/120 and 170/170 in all 18 sweeps. keepBothReads and
  minAdapterLength behave as documented.
- **ILLUMINACLIP simple mode** (`heldup_illuminaclip_simple.out`): clip positions on
  6,000 reads with errors agree with the documented rule for ≥ 99.1 % and with the
  best-sub-range port for ≥ 99.3 % at thresholds 10 and 7; no adapter-free read is
  clipped (0/1,237 and 0/1,126); 3' fragment sweep and 12-nt adapter behave as the
  threshold arithmetic predicts; reads starting inside the adapter are dropped.
- **Paired-end bookkeeping** (`heldup_palindrome_pe.out`, B): 3,000 pairs — every read
  lands in the expected file (1P/1U/2P/2U) with the expected sequence and quality
  3,000/3,000; the log line, the `-summary` file and the 6,000 trim-log lines equal the
  expectation.
- **`-threads` invariance** (C), as above.
- **The project's own suite**: 259 tests pass on unmodified `main` (fresh compile, JDK 25).

## Not audited

- Compression paths (`util/compression/*`: parallel gzip/bzip2 blocks, concatenated gzip
  input), `-basein`/`-baseout` templating, the Pairomatic tool, the simplified one-argument
  invocation beyond reading its fixed steps (`Trimmomatic.java:106-108`, `:129-131`), and
  the `-verbose` adapter statistics.
- Adapter files with `/1`-only or `/2`-only simple sequences (the shipped files have none
  besides the prefixes); wildcard characters in adapters (the code has no IUPAC support:
  anything but ACGT packs to 0 and scores like an N).
- Real sequencing data: every read here is synthetic, so the 0.6 % (TM1, 2x50) and
  0.5–0.9 % (N1/N2) rates are for the simulated error and quality profiles, not for any
  instrument.
- The palindrome seed walk (`:412-448`): its zigzag over `refIndex`/`testIndex` tests one
  16-mer pair per candidate insert; with error-free synthetic reads it never missed, and
  the TM1 simulation's 4,000/4,000 agreement with the integer-penalty port (which uses an
  any-16-mer seed) says it did not matter there either, but reads with errors inside that
  window were not targeted.
