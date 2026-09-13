# Trimmomatic audit against 291 published papers (2021–2026)

_Round-4 audit, generated 2026-09-13 against `usadellab/Trimmomatic` `main` @ `ef98d62`
(2026-07-03, the V0.41 release merge, version string 0.41). Focus: the code paths that
decide which bases and which reads survive — ILLUMINACLIP in palindrome and simple mode
(seeds, the log-odds score, minAdapterLength, keepBothReads), SLIDINGWINDOW, MAXINFO,
LEADING/TRAILING, MINLEN/MAXLEN/CROP/HEADCROP/TAILCROP/AVGQUAL/BASECOUNT, TOPHRED33/64,
Phred-offset auto-detection, the paired-end bookkeeping, `-summary`, `-trimlog` and
`-threads` — verified by executing the shipped jars and builds._

## What this is

The six-journal survey found **291 papers** in PNAS (184), *Nature* (92), *Cell* (13)
and *Science* (2), 2021–2026, that used Trimmomatic, always as a read-trimming step
(291 under "read trimming", 60 also under "alignment/mapping", 59 under "quality control").
Its trimming core was read in full on `main` and every suspicion was run through the
shipped code — the jar built from `ef98d62`, the 0.41 and 0.40 release jars from GitHub,
the 0.39 release zip (the cohort's most-cited version) and the `v0.38`, `v0.36`, `v0.33`
and `v0.32` tags compiled from source — against independent Python implementations of the
README's rules on synthetic reads with known adapter positions, insert sizes and qualities.

## Findings (details and line citations in [`component-reviews/trimming-core.md`](component-reviews/trimming-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **TM1** | **CONFIRMED on `main`, 0.41, 0.40, 0.39, 0.38, 0.36, 0.33, 0.32** | ILLUMINACLIP palindrome mode charges `int(Q/10)` per mismatch (`IlluminaClippingTrimmer.java:494`, `:496`, integer division) where the README and simple mode (`:556`, `/ 10.0f`) charge Q/10: a mismatch at Q2–Q9 costs nothing, at Q19 costs 1 instead of 1.9. A 2x50 pair with a 42-nt insert and two Q19 errors scores 29.9 under the documented rule (keep) and 31.7 as shipped (forward clipped to 42 nt, reverse dropped). On a 7,200-pair grid the shipped decision differs from the documented one for 600 pairs and equals a port of the integer rule 7,200/7,200; in a simulated 2x50 library 23 of 4,000 pairs flip, in 2x75/2x100/2x150 libraries none. |
| **TM2** | **CONFIRMED on `main`, 0.41, 0.40, 0.39, 0.38, 0.36, 0.33, 0.32** | MAXINFO trims every read to one base once `targetLength` reaches 248 at strictness 0.1, 495 at 0.2, or 711 at any strictness: the two log-score tables are scaled to `long` with `Math.max` of the two candidate ratios (`MaximumInformationTrimmer.java:67-68`), the length table saturates at `Long.MIN_VALUE` (`:34`) and the sum wraps positive at the first base (`:94`); above 710 `Math.exp` overflows (`:48`). 41 of 150 (target, strictness) cells on a 300-nt Q40 read keep 1 base where a double-precision evaluation keeps 300; at the settings people use (35–150, 0.2–1.0) 5,000/5,000 reads equal the double rule. |
| N1 | note, design + documentation | Simple-mode ILLUMINACLIP scores the best sub-range of the alignment (`calculateMaximumRange`), not the sum the README describes; on 6,000 reads with errors the shipped clip equals the documented sum for 5,971/5,949/5,965 reads (thresholds 10/7/15) and the sub-range port for 5,982/5,959/5,997. |
| N2 | note, by reading with one executed symptom | Adapters of 24 nt and longer are seeded with every fourth 16-mer only (`INTERLEAVE = 4`), part of the 0.3–0.9 % of adapter reads the shipped build leaves untouched while both references find them. |
| N3 | note, design | Every quality-based step scores an `N` base as quality 0 (`FastqRecord.getQualityAsInteger(true)`), also in SLIDINGWINDOW, AVGQUAL, MAXINFO and the ILLUMINACLIP penalty. |
| N4 | note, design | SLIDINGWINDOW drops every read shorter than the window whatever its quality (all-Q40 1–3-nt reads under `4:15`, 5-nt under `8:15`). |
| N5 | note, off-by-one, cosmetic | TRAILING never tests the first base, so a read whose only qualifying base is the first is dropped rather than kept as 1 nt; the project's own test asserts it. |
| N6 | note, design | Phred auto-detection exits on a Phred+33 file that is all Q27–Q40 in its first 10,000 reads (issue #42's symptom) and silently chooses Phred+64 for Phred+33 data with qualities above Q46 (PacBio HiFi FASTQ). |
| N7 | note, bookkeeping | Paired inputs of unequal length are truncated to the shorter (100 + 90 reads → `Input Read Pairs: 90`, ten forward reads in no output); `-validatePairs` warns, the result is the same. |
| N8 | note, documentation | MAXINFO's error probability is 10^(−(Q+0.5)/10); `HEADCROP:n` drops an n-nt read while `CROP:0` writes a zero-length record. |

Five own suspicions were withdrawn by execution (palindrome `minAdapterLength` off by
one; 3' fragments shorter than the seed not found; `-threads` changing results;
`-summary`/`-trimlog` disagreeing with the log; AVGQUAL truncation). They are recorded in
the review.

**Held up under execution:** SLIDINGWINDOW equals both an as-coded port and the
documented reading on 20,000 reads under seven settings; LEADING/TRAILING at three
thresholds, MINLEN/MAXLEN/CROP/HEADCROP/TAILCROP/AVGQUAL/BASECOUNT and the chained
`LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36` match 100 %; TOPHRED33/64 round-trip
200/200; MAXINFO at seven typical settings equals a double-precision evaluation
5,000/5,000; the palindrome geometry (insert 0 … R+19, three adapter files, 2x100 and
2x150, keepBothReads and minAdapterLength 1/8/20) matches the reference in all 18 sweeps;
simple-mode clip positions, the 3' fragment minimum (12 nt at threshold 7, 17 at 10, 25
at 15) and adapter-only reads behave as the README's arithmetic predicts; the four
paired-end outputs, the log line, the `-summary` file and 6,000 `-trimlog` lines equal a
per-read expectation on 3,000 pairs; outputs are byte-identical for `-threads 1/2/4/8`;
the project's own suite passes (259 tests on `main`, 261 and 263 with the patches).

## How the papers use Trimmomatic (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| ILLUMINACLIP / adapter clipping mentioned | 131 |
| version stated | 116 (0.39 ×82, 0.36 ×53, 0.38 ×23, 0.32 ×11, 0.33 ×7, 0.35 ×4, 0.40 ×2) |
| RNA-seq / assembly / WGS-variant / metagenomics-16S / ChIP-ATAC / single-cell | 95 / 82 / 52 / 40 / 22 / 22 |
| FastQC/MultiQC also used / Cutadapt, Trim Galore or fastp also used | 82 / 49 |
| "default parameters" | 76 |
| SLIDINGWINDOW | 59 (4:15 ×21, 4:20 ×6, 5:20 ×4, 4:25 ×2, 4:5 ×2, then 3:18, 4:19, 4:30, 5:30, 10:20, 4:10, 3:20) |
| MINLEN | 57 (36 ×14, 50 ×7, 75 ×3, 20 ×3, then 100, 25, 35, 30, 40, 5, 45, 80) |
| paired-end / single-end stated | 55 / 7 |
| LEADING / TRAILING | 39 / 41 (LEADING 3 ×18, 20 ×6; TRAILING 3 ×17, 20 ×7) |
| ILLUMINACLIP thresholds stated | 2:30:10 ×15, 2:30:7 ×2, 2:30:10:1:false, 2:30:10:2:true, 2:30:10:1:true, 0:6:6 |
| TruSeq3-PE / TruSeq3-SE / TruSeq2 / Nextera / custom adapter file | 15 / 2 / 1 / 5 / 7 |
| palindrome / keepBothReads named | 5 |
| MAXINFO | 2 (`100:0.2`, `35:0.5`) |
| HEADCROP / TOPHRED / `-phred` flag | 1 / 1 / 5 |

Exposure by finding: **TM1** needs paired-end ILLUMINACLIP with a prefix pair — the
default way the cohort runs it (`ILLUMINACLIP:TruSeq3-PE.fa:2:30:10` is the most-named
setting) — and read pairs whose palindrome alignment is short enough for one or two
truncated penalties to decide: 0.6 % of pairs in a simulated 2x50 library, none in 2x75
and longer. Which cohort papers ran 50-nt paired reads cannot be settled from the cache.
**TM2** needs MAXINFO with a target length of 248+ at strictness 0.1 (495+ at 0.2, 711+
anywhere); the two MAXINFO settings in the cache are unaffected, so the exposure in this
cohort is nil as far as the cache shows.

**Profiling caveat.** As for the Seurat, Scanpy, Cutadapt and fastp audits, this session
had no route to Europe PMC, so `trimmomatic_profile.py` ran in `--offline` mode over the
survey's stored evidence snippets; every record in `trimmomatic_profiles.jsonl` is
`source: survey_cache` and every count above is a lower bound. Rerun without `--offline`
from a host with Europe PMC access to replace them with full-text records. Some of the
"versions named" values (`2.6.0`, `2.4.0`, `0.7.16`, `0.9.6`) are neighbouring packages'
versions caught by the ±25-character window around the word "Trimmomatic" in a software
table; the families 0.39/0.36/0.38/0.32/0.33 match the survey's own `top_versions`.

**Build caveat.** The usadellab.org download site is not reachable from this session, so
0.38, 0.36, 0.33 and 0.32 are `javac` builds of the tagged sources (with the tagged
`adapters/`, whose `TruSeq3-PE.fa` differs from `main`'s only by a trailing newline), not
the released jars; 0.39 is the release zip from GitHub and 0.40/0.41 the GitHub release
jars. The `main` jar was built with `mvn package` on JDK 25.0.4 (the pom's release
target; the session's default `javac` is 21 and `openjdk-25-jdk-headless` had to be
installed with apt). Maven ran offline from a cache that already held the plugins.

## Filing channel (read before anything is sent)

- Trimmomatic has **no `CONTRIBUTING.md`, no issue or PR templates, no linter
  configuration and no changelog file beyond `versionHistory.txt`** (last entry 0.40; the
  0.41 release added none). `.github/workflows/build-and-test.yml` runs `mvn -B clean
  verify` on JDK 25 for pushes and PRs to `main`; `release.yml` packages on `v*.*` tags.
  The tests are JUnit 5 under `src/test/java/org/usadellab/trimmomatic/`, one class per
  concern, which the two patches follow.
- The tracker is active: issues opened in 2021–2025 were answered and closed in
  batches in 2025–2026 (e.g. #42 closed 2026-01-08, #37/#40/#62 closed 2026-07), and
  0.40 (2025-08) and 0.41 (2026-07) were released from this repository. **No prior report
  of either finding** (nearest #52, #16, #56, #15 for TM1; #74, #22, #84 for TM2).
- No fork `github.com/cindykrafft/Trimmomatic` exists yet, so no
  `upstream-declines-ai-contributions` topic applies.
- **The kit is in [`upstream/`](upstream/)**: two issue texts with MCVEs run on `main`,
  0.41 and 0.39, two `git am`-able patches (fix + JUnit test; each new test fails on
  unmodified `main`), the PR bodies, `patch_verification.txt` with every test run with
  and without each patch, and the documents read. Ranking under the two-filings cap:
  **TM1 first** (default settings, silent, every version), **TM2 second** (rare
  settings, loud). **Nothing has been filed and nothing has been pushed.**

## Files

| file | what |
|---|---|
| `trimmomatic_profile.py`, `trimmomatic_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/trimming-core.md` | the review: TM1–TM2, N1–N8, five withdrawn suspicions, held-up list, not-audited list |
| `verify/tm_ref.py` | the independent references (documented and as-coded SLIDINGWINDOW, TRAILING, MAXINFO in double precision, simple-mode and palindrome ILLUMINACLIP with the documented Q/10 and the integer penalty, the best-sub-range port) and the jar runner |
| `verify/tm1_palindrome_penalty.py` (+ `.out`, `.patched.out`) | TM1: the pair, the 7,200-pair grid, four simulated libraries |
| `verify/tm2_maxinfo_normalisation.py` (+ `.out`, `.patched.out`) | TM2: closed form, the 25 × 6 grid, seven typical settings on 5,000 reads, 2x300 reads at target 800 |
| `verify/heldup_quality_trimmers.py` (+ `.out`) | held up + N3–N6, N8: SLIDINGWINDOW, LEADING/TRAILING, length and quality filters, TOPHRED, Phred detection |
| `verify/heldup_illuminaclip_simple.py` (+ `.out`) | held up + N1/N2: simple mode with errors, 3' fragment sweep, 12-nt adapter, adapter-only reads |
| `verify/heldup_palindrome_pe.py` (+ `.out`) | held up + N7: palindrome insert sweeps, PE bookkeeping, `-summary`, `-trimlog`, `-threads`, unequal inputs |
| `verify/version_scope_cli.py` (+ `.master.out`, `.v0.41.out`, `.v0.40.out`, `.v0.39-release.out`, `.v0.39-build.out`, `.v0.38-build.out`, `.v0.36-build.out`, `.v0.33-build.out`, `.v0.32-build.out`, `.patched-tm1.out`, `.patched-tm2.out`) | the two findings through the command line only, on every version and on the patched jars |
| `upstream/` | filing kit: issue texts, MCVEs and their outputs, patches 0001–0002, PR bodies, patch verification, documents read |

The harnesses take a jar path (or a directory with `classes/` and `lib/`) as their first
argument and, for the ILLUMINACLIP ones, the `adapters/` directory as the second:
`git clone https://github.com/usadellab/Trimmomatic && cd Trimmomatic && mvn package`
(JDK 25), then `python3 verify/tm1_palindrome_penalty.py target/trimmomatic-0.41.jar adapters`.

## Next steps

1. Open the TM1 issue and PR 1 from `upstream/`; once the maintainers respond, TM2.
   Record numbers and responses here and in the top-level table.
2. Extend the review to the palindrome seed walk with erroneous reads inside the seed
   window, to adapter files with `/1`- and `/2`-only simple sequences, and to the
   compression paths (see "Not audited").
3. Full-text profiling rerun when Europe PMC is reachable, to settle how many of the 291
   papers ran 50-nt paired reads through ILLUMINACLIP (TM1) and whether any used MAXINFO
   with a large target (TM2).
