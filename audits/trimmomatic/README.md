# Trimmomatic audit against 291 published papers (2021–2026)

_Round-4 audit, generated 2026-09-10 against `usadellab/Trimmomatic` `main` @
`ef98d6252abeae80cfee36acf9e0e1055097da0b` (2026-07-03, version string 0.41).
Focus: the code paths that decide which bases and which reads survive —
ILLUMINACLIP in both its palindrome and simple modes, SLIDINGWINDOW,
LEADING/TRAILING, MAXINFO, the length and quality filters, Phred conversion and
detection, and the paired-end bookkeeping that produces the `-summary` counts —
verified by executing the built JARs._

## What this is

The six-journal survey found **291 papers** that used Trimmomatic, almost always
as the first step of a sequencing pipeline. Its trimming core was read in full on
`main` and every suspicion was run through the shipped JAR — `main` built from
source, the 0.41, 0.40 and 0.39 release JARs, and the `v0.39`, `v0.38`, `v0.36`,
`v0.33` and `v0.32` tags built from source — against an independent Python
implementation of each step, written from the manual's definitions, on synthetic
reads with known truth (planted adapter position, planted insert length, known
quality profile).

## Findings (details and line citations in [`component-reviews/adapter-clipping-and-quality-trimming.md`](component-reviews/adapter-clipping-and-quality-trimming.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **TC1** | **CONFIRMED on `main` and on every release executed (0.32 → 0.41)** | ILLUMINACLIP's palindrome mode computes the per-mismatch penalty with **integer** division — `likelihood[i] = -qual1 / 10` on `int` operands, `IlluminaClippingTrimmer.java:494,496` — so a mismatch at Q0–Q9 costs 0.0 instead of 0.0–0.9 and one at Q10–Q19 costs 1.0 instead of 1.0–1.9, against the README's "each mismatch reduces the alignment score by Q/10" (`README.md:303`) and against simple mode's own `-quals[recPos] / 10.0f` at `:556`. The error is one-sided, so pairs *below* `palindromeClipThreshold` get clipped and, with the default `keepBothReads=false`, the reverse read dropped. Executed: a 40 nt insert in 50 nt reads with six Q9 mismatches scores **27.11** by the manual (below the default threshold 30) and **32.51** as coded — read 1 comes out 40 nt and **read 2 is dropped**; the same pair with the mismatches at Q10 (a *worse* alignment) is left untouched. On 4,000 synthetic pairs the JAR equals an as-coded port 4,000/4,000 and the documented penalty changes the outcome of **49 pairs (1.2 %)**; on a NovaSeq-like binned profile and on uniformly Q30–41 data, **0 of 4,000**. No prior report on the tracker. |
| N1 | note, known limit (asserted by the project's own test) | `MAXINFO` throws `ArrayIndexOutOfBoundsException` and aborts the run on any read longer than 1,000 nt (`MaximumInformationTrimmer.java:6,93`); 999 and 1,000 nt work. Not in the manual; 2 cohort papers use MAXINFO. |
| N2 | note, undocumented | Every quality step scores an `N` base as Q0 whatever quality character the FASTQ carries: a 50 nt Q35 read with five Ns written at Q40 comes out 45 nt under `TRAILING:20` and is dropped under `AVGQUAL:35`. |
| N3 | note, conservative-but-fatal | Automatic Phred detection refuses data whose qualities are all Q30–41 (`Error: Unable to detect quality encoding`); those characters are also legal phred64, so the refusal is defensible, and `-phred33` is the workaround. |
| N4 | note, known behaviour (asserted by the project's own test) | `TRAILING` never examines base 0 (`TrailingTrimmer.java:20`, `i > 0`), so a read whose only base above the threshold is its first is dropped instead of trimmed to 1 nt: 20–29 of 4,000 random reads at thresholds 3–30. `LEADING` is symmetric and correct. |
| N5 | note, design choice + documentation gap, quantified | `SLIDINGWINDOW` keeps the read to the **end** of the failing window and then strips trailing bases below the per-base threshold, where "cutting once the average quality within the window falls below a threshold" (`README.md:219`) reads as cutting at the window's start: **2,501/4,000** reads differ at `4:20`, **2,591/4,000** at `4:15`. Behaviour is identical on every version back to 0.32. 59 cohort papers use SLIDINGWINDOW. |
| N6 | note, design choice + documentation gap, quantified | ILLUMINACLIP **simple** mode scores an alignment by a run-merging "maximum range" (`:569`), not the plain sum the manual describes; palindrome mode uses the plain sum. 20 matching adapter bases followed by 13 mismatching Q30 bases sum to **−27.0** and score **12.0** by maximum range, and the read is clipped. Over 3,600 reads the coded rule differs from the manual's on 67 (37 attributable to maximum range alone). |
| N7 | note, documented heuristic, priced | The 16-mer seed prefilter costs real alignments, as the manual says it may: palindrome mode differs from an exhaustive evaluation of the same score on **208/4,000** pairs (mixed profile), 49/4,000 (NovaSeq-binned), 0/4,000 (high quality); simple mode on 21/3,600 reads. |
| N8 | note, by construction | A 3' adapter fragment is invisible below the length the score threshold implies: at `simpleClipThreshold` 10 a perfect partial adapter is clipped for every k ≥ 17 bases and never for k ≤ 16 (50/50 replicates each), matching `k × 0.60206 ≥ 10` exactly. A 12 nt adapter (score 7.22) is clipped 100/100 at threshold 7 and 0/100 at threshold 10. |
| N9 | note, undocumented | `HEADCROP:n`/`TAILCROP:n` drop a read of exactly n bases, and `SLIDINGWINDOW` drops any read shorter than the window (78 of 4,000 at window 4). |

Five of my own suspicions were withdrawn by verification (a "too strict" seed
bit-count test; a missed last window in `SLIDINGWINDOW`; an unenforced
`minAdapterLengthPalindrome`; thread-dependent results; a `long`-normalisation
error in `MAXINFO`). They are recorded in the review with what killed each.

**Held up under execution.** All of the following are *jar == independent Python
reference on every record*, with zero mismatches in total across 4,000-read runs:
SLIDINGWINDOW at seven settings; LEADING and TRAILING at four thresholds each;
MAXINFO at five settings (the `long`-normalised score reproduces in floating
point exactly); MINLEN, MAXLEN, CROP, HEADCROP, TAILCROP, AVGQUAL and BASECOUNT
across 21 settings including the boundaries; TOPHRED33/TOPHRED64 round-trips and
`-phred64` input; automatic Phred detection on mixed-quality phred33 and phred64
data; and a four-step pipeline applied in order. ILLUMINACLIP simple mode equals
its port on 3,600/3,600 reads at three thresholds, clipping planted adapters at
exactly the planted position and touching **0 of 2,000** adapter-free reads;
palindrome mode equals its port on 4,000/4,000 pairs on each of three quality
profiles and clips **nothing** in 3,000 pairs of unrelated random reads. The
paired-end bookkeeping holds on 3,000 pairs across five ILLUMINACLIP option sets
(`keepBothReads` and `minAdapterLength` included): all four outputs
byte-identical to the port's, the five `-summary` counters equal and summing to
the input, the percentages right, `-trimlog` one line per input read with every
field matching, and inputs of unequal length handled by processing only the
pairs in common. **Results do not depend on `-threads`**: at 1, 2, 4 and 8 the
four output files are byte-identical. The project's own suite is 259 tests /
0 failures on `main` @ `ef98d62`.

## How the papers use Trimmomatic (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| ILLUMINACLIP (adapter clipping) | 158 |
| version stated | 114 |
| RNA-seq | 88 |
| FastQC / MultiQC also used | 77 |
| "default parameters" | 71 |
| paired-end mode (PE) / MINLEN | 62 / 62 |
| SLIDINGWINDOW | 59 |
| Cutadapt or Trim Galore also used | 40 |
| TRAILING / LEADING | 38 / 34 |
| metagenomics, 16S or amplicon | 24 |
| single-cell | 23 |
| ILLUMINACLIP parameters stated | 21 |
| TruSeq3-PE / PE-2 adapters | 15 |
| ATAC / ChIP / CUT&RUN | 10 |
| bisulfite / methylation | 9 |
| WGS / WES / resequencing / custom adapter file | 8 / 8 |
| single-end mode (SE) / fastp also used / AVGQUAL | 7 / 7 / 7 |
| `-phred33` / `-phred64` stated | 5 |
| palindrome, `keepBothReads` or `minAdapterLength` mentioned | 4 |
| NexteraPE adapters / unpaired outputs discussed | 3 / 3 |
| MAXINFO / TruSeq3-SE adapters | 2 / 2 |
| TOPHRED33/64 / `-threads` / HEADCROP / TruSeq2 adapters | 1 each |
| versions named | 0.39 ×82, 0.36 ×55, 0.38 ×23, 0.32 ×12, 0.33 ×8, 0.35 ×4, 0.40 ×2, then singletons |
| ILLUMINACLIP strings quoted | `2:30:10` ×15, `2:30:7` ×2, then `2:30:10:1:FALSE`, `2:30:10:2:True`, `2:30:10:1:true`, `0:6:6` |
| SLIDINGWINDOW values | `4:15` ×21, `4:20` ×6, `5:20` ×4, `4:25` ×2, `4:5` ×2, then singletons |

Exposure by finding: **TC1** needs paired-end mode with a `Prefix…/1` +
`Prefix…/2` adapter pair — every stock `TruSeq*-PE*.fa` and `NexteraPE-PE.fa`
qualifies — and data with bases below Q10 inside the read-through overlap.
158 papers name ILLUMINACLIP, 62 state paired-end mode, 15 name a TruSeq3 PE
adapter file, and 15 quote the exact string `2:30:10`, the threshold the
harness's pair straddles. How many of those runs had low-quality tails cannot be
answered from the cache, so the exposure is bounded, not counted. **N5** touches
the 59 papers using SLIDINGWINDOW but changes no result relative to any other
Trimmomatic version — it is a gap between the manual and 14 years of consistent
behaviour, not a regression.

**Profiling caveat.** As for the Scanpy, Cutadapt and fastp audits, this session
had no route to Europe PMC, so `trimmomatic_profile.py` ran in `--offline` mode
over the survey's stored evidence snippets; every record in
`trimmomatic_profiles.jsonl` is `source: survey_cache` and **every count above is
a lower bound**. Rerun without `--offline` from a host with Europe PMC access to
replace them with full-text records. The version families 0.39/0.36/0.38/0.32/
0.33 match the survey's own `top_versions`; the handful of `2.4`, `2.6`, `1.1`
values are neighbouring packages' versions caught by the ±25-character window
around the word "Trimmomatic" in a software table.

**Build caveat.** This environment has **javac 21 only** (openjdk-21-jdk) plus a
**JRE 25**, while `pom.xml` sets `<maven.compiler.release>25</maven.compiler.release>`.
Every source build below therefore added `-Dmaven.compiler.release=21`; the
sources compile unchanged under 21. The upstream-built release JARs were run as
shipped; the 0.41 release JAR is compiled to class file version 69 and refuses to
start under Java 21 (`UnsupportedClassVersionError`), which is why
`openjdk-25-jre-headless` was installed. It reproduces TC1 identically to the
locally built `main`, so the release override does not affect any finding
(`upstream/mcve_outputs.txt`). Maven ran offline against a warm `~/.m2`.
The 0.35 tag, which 4 cohort papers name, was not built: the five tags built
are the survey's five `top_versions`.

## Filing channel (read before anything is sent)

- Trimmomatic has **no `CONTRIBUTING.md`, no issue template, no PR template, no
  code of conduct and no linter configuration**. `.github/` holds three
  workflows; `build-and-test.yml` runs `mvn -B clean verify` on JDK 25 for every
  push and PR to `main`. `versionHistory.txt` is the changelog, one
  `Fix:`/`Feature:`/`Performance:` line per entry under a `Version <n>:` heading.
- **No `cindykrafft/Trimmomatic` fork exists**, so the
  `upstream-declines-ai-contributions` topic could not be checked and
  `site/audits.json` has no `declines_ai` entry for this package; upstream
  publishes no AI policy of its own. The kit is prepared in full and flagged for
  a policy re-check before anything is posted.
- **No prior report of TC1**: seven phrasings through
  `mcp__github__search_issues`; nearest are #52 ("question about ILLUMINACLIP
  2:30:10", closed, 2 comments) and #56 (PE survival counts, closed, 2 comments).
  Neither is the same bug, and **comment bodies cannot be read from this
  session**, so both should be read in full before filing.
- Maintainers are active: last commit `ef98d62` on 2026-07-03, issues answered up
  to #88 (2026-07-01). The **exact open-issue count could not be obtained** —
  the GitHub list and commit APIs are refused for this repository in this
  session; only semantic issue search works.
- **The kit is in [`upstream/`](upstream/)**: one issue text, a standalone MCVE
  run on four builds, one `git am`-able patch (fix + a JUnit regression test that
  fails on unmodified `main` + a changelog entry), the PR body, and
  `patch_verification.txt` with the test numbers with and without the patch.
  **Nothing has been filed and nothing has been pushed.**

## Files

| file | what |
|---|---|
| `trimmomatic_profile.py`, `trimmomatic_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/adapter-clipping-and-quality-trimming.md` | the review: TC1, N1–N9, five withdrawn suspicions, held-up list, not-audited list |
| `verify/trimmomatic_ref.py` | the independent ports — every trimmer, the 2-bit packing, both clipping-score variants, `sliding_window_doc`/`_coded`, `trailing_doc`/`_coded`, `palindrome_doc`/`_coded` with an `int_division` switch — plus the FASTQ and command-line helpers |
| `verify/tc1_palindrome_int_division.py` (+ `.out`) | TC1: the constructed pair at five mismatch qualities, 4,000 pairs on three quality profiles, the seed heuristic priced separately, and a 3,000-pair false-positive control |
| `verify/heldup_illuminaclip_simple.py` (+ `.out`) | simple mode: 3,600 reads at three thresholds, the coded-vs-documented rule split by cause, the partial-3'-adapter length sweep, three adapter length classes |
| `verify/heldup_simple_trimmers.py` (+ `.out`) | SLIDINGWINDOW, LEADING/TRAILING, MAXINFO, the seven length/quality filters, Phred conversion and detection, and a four-step pipeline — 4,000 reads each |
| `verify/heldup_pe_bookkeeping.py` (+ `.out`) | paired-end outputs, the five `-summary` counters, `-trimlog`, `-threads` invariance, unequal-length inputs, SE mode |
| `verify/notes_misc.py` (+ `.out`) | N1–N7 as worked single-record examples |
| `verify/version_scope_cli.py` (+ `.master.out`, `.master-patched.out`, `.v0.41.out`, `.v0.40.out`, `.v0.39.out`, `.v0.39-src.out`, `.v0.38.out`, `.v0.36.out`, `.v0.33.out`, `.v0.32.out`) | TC1 through the command line only, on every build, with SLIDINGWINDOW/TRAILING/MAXINFO sentinels |
| `upstream/` | filing kit: issue text, MCVE and its outputs, patch 0001, PR body, patch verification, documents read |

The harnesses take the path of a Trimmomatic JAR (or a `classes/`+`lib/`
directory built from an old ant tag) as their first argument:

```
git clone https://github.com/usadellab/Trimmomatic && cd Trimmomatic
mvn -B -DskipTests package            # add -Dmaven.compiler.release=21 on a JDK 21
python3 verify/tc1_palindrome_int_division.py target/trimmomatic-0.41.jar
```

## Next steps

1. Read #52 and #56 in full, confirm the repository states no AI-contribution
   policy, then open the TC1 issue and the PR from `upstream/pr-bodies.md`.
   Record the numbers and the maintainer response here and in the top-level table.
2. Offer N1 (the 1,000 nt MAXINFO limit) and N5/N6 (the SLIDINGWINDOW and
   simple-mode scoring wording) as a documentation patch **only if** the TC1
   thread goes well — they are not defects, and the filing cap is two.
3. Extend the review to the paths listed under "Not audited", above all
   `BarcodeSplitter` and a direct differential test of the 2-bit packing helpers.
4. Full-text profiling rerun when Europe PMC is reachable, to settle how many of
   the 291 papers ran paired-end ILLUMINACLIP on data with low-quality tails
   (TC1's exposure).
