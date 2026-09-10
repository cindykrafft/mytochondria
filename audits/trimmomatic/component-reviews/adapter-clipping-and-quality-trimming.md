# Trimmomatic — adapter clipping and quality trimming

_Read in full on `usadellab/Trimmomatic` **`main`** @ **`ef98d6252abeae80cfee36acf9e0e1055097da0b`**
("Merge branch 'V0.41' — release v0.41", 2026-07-03, version string 0.41).
All `file:line` citations below are on that commit. Every claim with a number in
it comes from a `.out` file in [`verify/`](../verify/); nothing here is inferred
from release notes._

## What was read

The whole numerical core of the trimming pipeline, i.e. everything that decides
which bases and which reads reach a published count:

| file | what it decides |
|---|---|
| `src/main/java/org/usadellab/trimmomatic/trim/IlluminaClippingTrimmer.java` (1–860) | ILLUMINACLIP: the FASTA-name convention that splits palindrome from simple mode, the 2-bit seed packing, the palindrome seed scan and its score, the four simple-mode clipping-sequence classes and their score, the pair bookkeeping (`keepBothReads`) |
| `trim/SlidingWindowTrimmer.java` | SLIDINGWINDOW |
| `trim/LeadingTrimmer.java`, `trim/TrailingTrimmer.java` | LEADING / TRAILING |
| `trim/MaximumInformationTrimmer.java` | MAXINFO |
| `trim/MinLenTrimmer.java`, `MaxLenTrimmer.java`, `CropTrimmer.java`, `HeadCropTrimmer.java`, `TailCropTrimmer.java`, `AvgQualTrimmer.java`, `BaseCountTrimmer.java` | length and quality filters |
| `trim/ToPhred33Trimmer.java`, `ToPhred64Trimmer.java`, `fastq/FastqParser.java` | Phred conversion and automatic offset detection |
| `Trimmomatic.java`, `TrimmomaticPE.java`, `TrimmomaticSE.java`, `threading/*` | paired-end bookkeeping, `-summary`, `-trimlog`, `-threads` |

The documented rules were taken from the repository's own `README.md` on the
same commit — above all `README.md:303`:

> The thresholds used are a simplified log-likelihood approach. Each matching
> base adds just over 0.6, while each mismatch reduces the alignment score by
> Q/10.

and `README.md:257–263` (SLIDINGWINDOW, MAXINFO), `README.md:245` (TRAILING).

## Method

`verify/trimmomatic_ref.py` is an independent Python implementation of each step,
written from the manual's definitions and, where the manual is silent, from the
code — the two variants are kept separate on purpose (`sliding_window_doc` vs
`sliding_window_coded`, `trailing_doc` vs `trailing_coded`, `palindrome_doc` vs
`palindrome_coded`, `simple_clip_doc` vs the class ports, and `int_division` as
an explicit switch). Synthetic reads are generated in the harnesses with known
truth (planted adapter position, planted insert length, quality profile), the
shipped JAR is run through its real command line, and the outputs are compared
record by record. Where the jar and the as-coded port agree everywhere, the port
is then used to price the difference between the coded rule and the documented
one over thousands of reads.

---

## Findings

### TC1 — CONFIRMED (wrong number at master). ILLUMINACLIP palindrome mode charges an *integer* Q/10 mismatch penalty, so mismatches below Q10 cost nothing and read pairs below `palindromeClipThreshold` are clipped and the reverse read dropped

`IlluminaPrefixPair.calculatePalindromeDifferenceQuality`
(`IlluminaClippingTrimmer.java:463–501`) builds the per-position log-odds array.
For a mismatch it does

```java
                if (ch1 == 'N' || ch2 == 'N')
                        likelihood[i] = 0;
                else if (ch1 != ch2) {
                        if (qual1 < qual2)
                                likelihood[i] = -qual1 / 10;      // :494
                        else
                                likelihood[i] = -qual2 / 10;      // :496
                } else
                        likelihood[i] = LOG10_4;                  // :498  (0.60206f, :28)
```

`qual1` and `qual2` are `int` (`:486–487`), so `-qual1 / 10` is **integer**
division, evaluated and truncated toward zero *before* it is widened into the
`float likelihood[]`. A mismatch at Q0–Q9 therefore costs `0.0`, one at Q10–Q19
costs `1.0`, one at Q20–Q29 costs `2.0`, and so on.

Simple mode, in the same file, does it correctly:
`IlluminaClippingSeq.calculateDifferenceQuality` at `:556` is
`likelihood[i] = -quals[recPos] / 10.0f;`. Palindrome mode is the only place in
the file where the division is integer, and the README (`:303`) states one rule
for both.

The error is one-sided: the penalty is always too small, never too large, so the
palindrome score is always too high, so pairs are clipped that the documented
rule leaves alone. The result of a palindrome hit is not a small trim — the
forward read is cut to the inferred insert and, with the default
`keepBothReads=false`, **the reverse read is dropped entirely**
(`IlluminaClippingTrimmer.java:276–286`).

**Executed** (`verify/tc1_palindrome_int_division.py`, output
`verify/tc1_palindrome_int_division.out`):

* *Part A, one constructed pair.* 50 nt reads, a 40 nt insert read through into
  the shipped `TruSeq3-PE-2.fa` adapters (60 aligned bases),
  `ILLUMINACLIP:TruSeq3-PE-2.fa:2:30:10`, six mismatches placed in read 2
  outside both 16-mer seeds (positions 0, 2, 37, 39, 42, 45):

  | quality of the six mismatched bases | documented score | coded score | shipped jar |
  |---|---|---|---|
  | Q9 | **27.11** (below 30 → leave alone) | **32.51** | read 1 clipped to 40 nt, **read 2 dropped** |
  | Q19 | **21.11** (below 30) | 26.51 (below 30) | untouched, 50 nt / 50 nt |
  | Q10 | 26.51 | 26.51 | untouched (control: the geometry is right) |
  | Q2 | 31.31 (above 30) | 32.51 | clipped / dropped under both rules |
  | none | 36.12 | 36.12 | clipped / dropped (positive control) |

  The arithmetic: 60 aligned bases, 54 matches × 0.60206 = 32.51; six mismatches
  at Q9 cost 6 × 0.9 = 5.4 by the README and 6 × 0 as coded.

* *Part C, population effect.* 4,000 synthetic pairs, 100 nt reads, inserts
  0–130 nt (read-through planted in 3,041), quality-correlated sequencing errors,
  a "mixed" profile with a low-quality tail. The shipped jar equals the as-coded
  port on **4,000/4,000** pairs (integer penalty, seeds, everything) — the port
  is faithful. Switching only the penalty to the documented `Q/10` changes the
  outcome of **49/4,000 pairs (1.2 %)**. In those 49 the coded clip point equals
  the planted insert length in 49 cases and the documented one in 13 — i.e. on
  this data the *bug is more often right than the documentation*, which is why it
  has survived; but its correctness is accidental and its direction is fixed.

* *Part E, quality profiles.* The exposure is entirely driven by how many
  mismatches inside the read-through overlap land on bases below Q10. On the
  mixed profile 29,948 of the overlap mismatches are at Q<10 and 49/4,000 pairs
  change. On a NovaSeq-like binned profile (Q2/Q12/Q23/Q37) **0/4,000** change,
  and on a uniformly high-quality profile (Q30–41) **0/4,000** change.

* *Part F, false positives.* 3,000 pairs of independent random 100 nt reads with
  no insert and no adapter: 0 touched by the jar, 0 by either port. The bug does
  not manufacture adapters out of nothing; it moves the threshold.

**Version scope, executed** (`verify/version_scope_cli.py`, one `.out` per build;
the probe is the Part A pair through the command line only, and a version counts
as AFFECTED only when the Q9 case is clipped, the Q10 case is not, and the
perfect-match control is clipped):

| build | TC1 |
|---|---|
| `main` @ `ef98d62` (0.41), built from source | **AFFECTED** (`version_scope_cli.master.out`) |
| 0.41 release jar (GitHub release asset) | **AFFECTED** (`.v0.41.out`) |
| 0.40 release jar | **AFFECTED** (`.v0.40.out`) |
| 0.39 release jar (the cohort's most-cited version, 82 papers) | **AFFECTED** (`.v0.39.out`) |
| 0.39 built from the `v0.39` tag | **AFFECTED** (`.v0.39-src.out`) |
| 0.38 (23 papers) | **AFFECTED** (`.v0.38.out`) |
| 0.36 (55 papers) | **AFFECTED** (`.v0.36.out`) |
| 0.33 (8 papers) | **AFFECTED** (`.v0.33.out`) |
| 0.32 (12 papers) | **AFFECTED** (`.v0.32.out`) |
| `main` + `upstream/0001-*.patch` | **not affected** (`.master-patched.out`) |

Every version this session could build or download carries it, which is
consistent with the line never having been touched: it is the original 2012
expression.

**Fix.** One character each on `:494` and `:496` — `10` → `10.0f` — plus a
regression test. `upstream/0001-Fix-charge-Q-10-per-mismatch-in-ILLUMINACLIP-palindr.patch`.
Verified end to end: `mvn test` on unmodified `main` is 259 tests / 0 failures;
the new `IlluminaPalindromeMismatchPenaltyTest` alone on unmodified `main` is
4 tests / **1 failure** (`testSixMismatchesAtQ9StayBelowThreshold`); with the
patch the whole suite is 263 tests / 0 failures
(`upstream/patch_verification.txt`).

**Who is exposed.** Paired-end runs with a `Prefix…/1` + `Prefix…/2` adapter pair
(that is: every stock `TruSeq*-PE*.fa` and `NexteraPE-PE.fa`) on data that has
bases below Q10 inside the read-through overlap. 158 of the 291 cohort papers
name ILLUMINACLIP, 62 state paired-end mode, 15 name a `TruSeq3-PE`/`PE-2`
adapter file and 15 quote the exact string `2:30:10` — the threshold the Part A
pair straddles. The cache cannot say how many of them have low-quality tails, so
the exposure is bounded but not counted.

---

## Notes (design, documentation, or known-and-tested behaviour — not wrong numbers)

Each of these was executed; none of them is a defect I would file.

* **N1 — MAXINFO throws on reads longer than 1,000 nt.**
  `MaximumInformationTrimmer.java:6` fixes `LONGEST_READ = 1000` and `:93`
  indexes `lengthScore[i]` by read position, so a 1,001 nt read raises
  `ArrayIndexOutOfBoundsException` and the run aborts
  (`verify/notes_misc.out` N1: 999 nt → 887 nt kept, 1,000 nt → 887 nt,
  1,001 nt → `Exception processing read`). This is **known and asserted by the
  project's own test**, `MaximumInformationTrimmerLongReadTest.testReadTooLong`
  ("MAXINFO has a hardcoded limit of 1000bp. Testing that it fails as
  expected"), so it is a documented limit rather than a finding. It is not in
  the manual, and 2 cohort papers use MAXINFO.

* **N2 — every quality step scores an `N` base as Q0**, whatever quality
  character the FASTQ carries (`FastqRecord.getQualityAsInteger(true)`).
  Executed: a 50 nt read of Q35 with Ns at 45–49 written at `'I'` (Q40) comes
  out 45 nt under `TRAILING:20`, 45 nt under `SLIDINGWINDOW:4:20`, dropped under
  `AVGQUAL:35`, 45 nt under `MAXINFO:50:0.9` (`notes_misc.out` N2). Sensible and
  undocumented.

* **N3 — automatic Phred detection refuses unambiguous phred33 data.**
  A file whose qualities are all Q30–41 (characters `?`–`J`) aborts with
  `Error: Unable to detect quality encoding`; so does Q26–46. One character in
  33–58 is enough to decide (`notes_misc.out` N3, and the same three cases in
  `heldup_simple_trimmers.out`). Those characters are also legal phred64
  (Q−1…Q10), so refusing is conservative and defensible; but modern
  high-quality-only files hit it, and `-phred33` is the workaround.

* **N4 — TRAILING never examines base 0.** `TrailingTrimmer.java:20` loops
  `for (int i = quals.length - 1; i > 0; i--)`, so a read whose only base at or
  above the threshold is its first base is **dropped** instead of trimmed to
  1 nt. Executed on 4,000 random reads: 20 such reads at `TRAILING:3`, 26 at
  `TRAILING:10`, 29 at `TRAILING:20`, 29 at `TRAILING:30`
  (`heldup_simple_trimmers.out`). `LeadingTrimmer.java:20` is symmetric and does
  cover the last base. This too is **asserted by the project's own test**
  (`TrailingTrimmerTest.testTrailingDropSingleBaseHigh`, whose comment reads
  "Due to implementation (i > 0), TrailingTrimmer drops reads if only the first
  base survives"), and any realistic pipeline has a `MINLEN` that would drop a
  1 nt read anyway. Known behaviour, not a finding.

* **N5 — SLIDINGWINDOW does not cut where the manual's wording implies.**
  `SlidingWindowTrimmer.java:44–58` keeps the read to the *end* of the window
  that fails (`lengthToKeep = i + windowLength`) and then walks back over
  trailing bases below the per-base `requiredQuality`. A literal reading of
  "cutting once the average quality within the window falls below a threshold"
  (`README.md:219`) would cut at the *start* of the failing window. On 4,000
  random reads the two differ on **2,501/4,000** at `SLIDINGWINDOW:4:20` and
  **2,591/4,000** at `4:15` (`heldup_simple_trimmers.out`). Worked example
  (`notes_misc.out` N6): quality `[30,30,30,30,30,30,10,10,10,10,30,30]`, window
  4, threshold 20 → the jar keeps 6 nt, the as-coded rule keeps 6 nt, the literal
  README rule keeps 5 nt. This is the behaviour of every Trimmomatic since 0.32
  (the sentinel in every `version_scope_cli.*.out` keeps 6 nt) and it is
  arguably the better rule; it is a **design choice with a documentation gap**,
  not an error. 59 cohort papers use SLIDINGWINDOW.

* **N6 — simple mode scores by a run-merging "maximum range", not the plain sum
  the README describes.** `IlluminaClippingSeq.calculateDifferenceQuality:567`
  ends in `calculateMaximumRange(likelihood)` (`:569–627`), which merges
  same-sign runs and then absorbs negative runs into their neighbours, returning
  the best contiguous sub-alignment; palindrome mode uses a plain
  `calculateTotal` (`:504–512`). Executed (`notes_misc.out` N7): 20 matching
  adapter bases followed by 13 mismatching Q30 bases sum to **−27.0** but score
  **12.0** by maximum range, and the jar clips; two Q35 mismatches at adapter
  positions 11 and 15 sum to 11.7 and score 10.2, so the read is clipped at
  threshold 10 and not at threshold 11. Priced over a population
  (`heldup_illuminaclip_simple.out` Part B): on 3,600 reads the coded result
  differs from the README's plain-sum-over-every-offset rule on 67 reads —
  21 explained by the seed requirement alone, 37 by the maximum-range score
  alone, 9 by both or neither. Maximum-range is the more sensible statistic; it
  is simply not what the manual says.

* **N7 — the seed heuristic costs real alignments, as documented.** The manual
  says the seed parameter exists "to make alignments more efficient"; the price
  is measurable. Palindrome mode: the README rule evaluated at every offset
  versus the coded seeded scan (float penalty in both, so N7 is isolated from
  TC1) differs on **208/4,000** pairs on the mixed profile, 49/4,000 on the
  NovaSeq-binned profile and 0/4,000 on high-quality data
  (`tc1_palindrome_int_division.out`). Simple mode: 21/3,600 reads
  (`heldup_illuminaclip_simple.out`). A design choice, quantified.

* **N8 — a 3' adapter fragment shorter than ~17 nt is invisible at the
  recommended threshold, by construction.** Two separate gates apply. A length
  gate, `minSequenceOverlap = (int)(simpleClipThreshold / 0.60206)` capped at 15
  (`IlluminaClippingTrimmer.java:140–143`), which requires `compLength > 15` at
  `:685`, `:747` and `:815` for any threshold of 10 or more; and the score gate
  `seqLikelihood >= simpleClipThreshold` (`:688`, `:750`, `:818`). For perfect
  matches the score gate is the binding one.
  Executed on 50 replicates per length, perfect Q35 matches with no errors
  (`heldup_illuminaclip_simple.out` Part C): at `ILLUMINACLIP:...:2:30:10` a
  partial adapter of k bases at the 3' end is clipped for every k ≥ 17 and never
  for k ≤ 16, matching `k × 0.60206 ≥ 10 ⟺ k ≥ 17` exactly. Part D confirms the
  same threshold logic for whole adapters: a 12 nt adapter (full-length score
  7.22) is clipped 100/100 at threshold 7 and 0/100 at threshold 10, while 20 nt
  and 30 nt adapters are clipped 100/100 at both. This is the documented
  arithmetic working as designed, and the reason the manual recommends 7–15.

* **N9 — `HEADCROP:n` / `TAILCROP:n` drop a read of exactly n bases, and
  SLIDINGWINDOW drops any read shorter than the window**
  (`SlidingWindowTrimmer.java:32`): 78 of 4,000 reads at window 4, and
  `SLIDINGWINDOW:4:20` on 1/2/3/4 nt reads of Q40 keeps only the 4 nt one
  (`notes_misc.out` N5). Consistent and undocumented.

---

## Withdrawn (my own suspicions that verification killed)

* **W1 — "`seedMismatches` is compared against a bit count, not a base count, so
  the seed is stricter than documented."** `:384` sets `seedMax = seedMaxMiss * 2`
  and `:416–417` test `Long.bitCount(ref1 ^ pack2[testIndex]) <= seedMax` over
  the 2-bit packing, so a mismatched base contributes 1 or 2 bit differences
  depending on which substitution it is. Reading further kills the concern: a
  seed with exactly `seedMismatches` mismatched bases has a bit count of at most
  `2 × seedMismatches`, so it *always* passes. The test is looser than the manual
  says, never tighter, and the seed is only a prefilter — the score threshold
  still decides. Documentation nit at most; no wrong number.

* **W2 — "the sliding window loop misses the last window."**
  `SlidingWindowTrimmer.java:44` runs `i < quals.length - windowLength`, which
  looked short by one. It is not: iteration `i` evaluates the window starting at
  `i+1`, so the last window evaluated starts at `quals.length - windowLength`,
  the final one. Confirmed by the port matching the jar on 4,000/4,000 reads for
  seven parameter settings.

* **W3 — "`minAdapterLengthPalindrome` is parsed but never enforced."** It only
  appears in `maxCount` (`:410`), never as an explicit length test, which looked
  like a dropped parameter. It is in fact how the minimum adapter length is
  enforced: `maxCount` bounds the scan so that the longest insert considered
  leaves at least `minPrefix` adapter bases. Executed: `:2:30:10` (default 8) and
  `:2:30:10:12` give different pair counts on the same 3,000 pairs
  ((3000, 459, 995, 298, 1248) vs (3000, 474, 980, 309, 1237)), and the port
  reproduces both exactly (`heldup_pe_bookkeeping.out`).

* **W4 — "results depend on `-threads`."** They do not; see below.

* **W5 — "MAXINFO's coded score is not the manual's formula."** The manual only
  describes the trade-off qualitatively ("targetLength… strictness"), and the
  coded score — `log(1/(1+e^(target−i−1))) + log(i+1)(1−strictness)` for length
  plus `strictness · log(1−10^(−(0.5+q)/10))` accumulated over bases,
  normalised into `long` (`MaximumInformationTrimmer.java:44–71`) — was ported
  in floating point and agrees with the jar on **4,000/4,000** reads for five
  parameter settings (`heldup_simple_trimmers.out`). The `long` normalisation,
  which I expected to lose ties, does not: no mismatch was observed.

---

## What held up (executed, not just read)

All of the following are `jar == independent Python reference` on every record,
with the record count and the option list in the `.out` files.

* **SLIDINGWINDOW** — 4,000 reads of length 1–160, seven settings
  (`4:20`, `4:15`, `5:20`, `10:25`, `1:20`, `4:30`, `3:3`): **4,000/4,000** each,
  no unexpected record in the output, input order preserved. Window average, cut
  position, short-read handling and the Phred offset all behave as coded and as
  the port predicts.
* **LEADING / TRAILING** — four thresholds each (3, 10, 20, 30): 4,000/4,000.
* **MAXINFO** — five settings (`40:0.8`, `50:0.5`, `36:0.9`, `100:0.2`,
  `75:0.5`): 4,000/4,000.
* **MINLEN, MAXLEN, CROP, HEADCROP, TAILCROP, AVGQUAL, BASECOUNT** — 21 settings
  in total, including the boundaries (`MINLEN:1`, `MINLEN:160`, `CROP:1`,
  `HEADCROP:1`): 4,000/4,000 each.
* **TOPHRED33 / TOPHRED64 and `-phred64` input** — 4,000/4,000 records identical
  after re-decoding at the other offset; `LEADING:20 TRAILING:20` under
  `-phred64` agrees with the reference on 4,000/4,000 (3,950 kept).
* **Automatic Phred detection** — correct on mixed-quality phred33 and phred64
  data (2,000/2,000 round-trip each); refuses high-quality-only data, see N3.
* **A multi-step pipeline** — `LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36`
  applied in order: 4,000/4,000, 1,642 kept. **Total record mismatches across
  every check above: 0.**
* **ILLUMINACLIP simple mode** — 3,600 reads (1,600 with a TruSeq3 adapter
  planted at positions 0–99, 2,000 adapter-free), three thresholds
  (`2:30:10`, `2:30:7`, `2:30:15`): jar equals the as-coded port on
  **3,600/3,600** each. Planted adapters are clipped at exactly the planted
  position in 819/1,600 at `2:30:10` (the rest are shorter than the score
  threshold allows, N8) and **0 of 2,000 adapter-free reads are touched**.
* **ILLUMINACLIP palindrome mode** — jar equals the as-coded port on
  **4,000/4,000** pairs on each of three quality profiles, and on
  **3,000/3,000** non-overlapping random pairs nothing is clipped by either.
* **Paired-end bookkeeping** — 3,000 pairs, five ILLUMINACLIP option sets
  including `keepBothReads` and `minAdapterLength` 1/8/12: all four outputs
  (`1P`, `1U`, `2P`, `2U`) byte-identical to the port's, the five
  `-summary` counters (input pairs, both surviving, forward only, reverse only,
  dropped) equal the port's and sum to the input, the percentages match, and
  every unpaired record appears in exactly the output its own survival implies
  (`heldup_pe_bookkeeping.out`).
* **`-summary` and `-trimlog`** — the summary block matches the port for all
  five PE option sets and for SE (3,000 input / 1,770 surviving / 59.00 % /
  1,230 dropped); the trimlog has exactly one line per input read
  (6,000 for PE, 3,000 for SE) and every field matches.
* **`-threads` invariance** — the same pipeline at `-threads` 1, 2, 4 and 8
  produces **byte-identical** `1P`/`1U`/`2P`/`2U` files and identical summaries.
  Results do not depend on the thread count.
* **Unequal input files** — file 1 given 7 extra reads at the end: Trimmomatic
  processes the 3,000 pairs they have in common and writes **0** of the extra
  reads to any output.
* **The project's own test suite** — 259 tests, 0 failures on `main` @ `ef98d62`
  with `mvn -o test` (JDK 25, `maven.compiler.release=25`).

## Not audited

* `BarcodeSplitter` (demultiplexing) — no cohort paper uses it.
* The compression layer (`gzip`/`bzip2` block queues, `util/*`) and the
  simplified-invocation auto-naming added in 0.41: I/O, not numbers.
* The 2-bit packing helpers were ported and exercised only indirectly, through
  the four clipping-sequence classes; no direct unit-level differential test of
  `packSeqExternal`/`packPrefixAndSeq` on adversarial input (e.g. long runs of
  `N`).
* Performance behaviour of the 0.41 virtual-thread pipeline under load; only
  determinism was checked (`-threads` invariance above).
* Interleaved input/output and the `-validatePairs` path.
* Whether the palindrome scan's *first-hit* return (`:435`, it returns on the
  first seed offset whose score passes rather than the best-scoring offset) ever
  picks a worse alignment than a later offset would: I could not construct a
  case, but I did not prove it cannot happen, so it is not claimed either way.
