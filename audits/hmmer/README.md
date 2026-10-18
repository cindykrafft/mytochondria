# HMMER audit against 162 published papers (2021–2026)

_Generated 2026-10-18 against `EddyRivasLab/hmmer` `develop` @ `37f7148` (version string 3.5,
July 2026, unreleased; the current release on eddylab.org is still 3.4) with Easel `develop` @
`69efc38`, built here, and the release tarballs 3.4, 3.3.2 and 3.1b2 from eddylab.org (the
current release and the cohort's most-cited versions; "3.1b" in the survey is 3.1b2, the last 3.1
beta). Focus: what a paper takes from a HMMER run — sequence and domain E-values and bit scores,
`-Z`/`--domZ` scaling (and nhmmer's `-Z` in megabases), the reporting and inclusion thresholds
(`-E`, `--incE`, `--domE`, `-T`, `--cut_ga/tc/nc`), domain definition and envelope coordinates, the
null2 bias correction, hmmbuild calibration (λ, MSV/Viterbi μ, Forward τ), jackhmmer iteration,
and the tblout/domtblout columns. Everything was verified by running the binaries on synthetic
databases with recorded truth, on human Swiss-Prot, and against Python recomputations of the
documented formulas._

## What this is

The six-journal survey found **162 papers** in PNAS (93), *Nature* (54), *Cell* (12) and
*Science* (3), 2021–2026, that used HMMER. Most use it for protein-family annotation (hmmsearch,
hmmscan against Pfam, TIGRFAM, KOfam or dbCAN) or for homology searches feeding phylogenies and
structure prediction. The pipeline, domain-definition, null2, top-hits, calibration and nhmmer
code was read on `develop`, and every suspicion was run on four builds. The harnesses compute their
truth independently. They recompute E-values in Python from the printed scores and the model's
STATS line, rebuild λ from the emission probabilities, and count i.i.d. null sequences for the
P-value tail. They also check threshold sets predicted from unthresholded runs, the generic
reference implementation against the SIMD one, and a replay of the library's own stochastic
traces.

## Findings (details and line citations in [`component-reviews/evalues-domains-null2-thresholds.md`](component-reviews/evalues-domains-null2-thresholds.md); harnesses with captured output in [`verify/`](verify/))

| id | status | tier | finding |
|---|---|---|---|
| **HM1** | **CONFIRMED on 3.1b2, 3.3.2, 3.4 and `develop`** | **now** (filed with HM2) | The SSE (and NEON, VMX) `p7_Null2_ByTrace()` adds every residue emitted by a model state to the node's *match* cell, so insert-state residues get match emission odds in the null2 correction of every domain resolved by stochastic traceback clustering. The generic reference `p7_GNull2_ByTrace()` counts them as inserts (odds 1.0), and the vector code's own sum expects that. The state type was computed and never used (2008) and was commented out as "not needed" in 2016. On emitted traces SSE ≠ generic on 469/469 fn3 domains with an insert state (0/562 without). Human Swiss-Prot, default options: 11 of 194 fn3 hits and 8 of 483 Pkinase hits change score by up to 0.7 bits (E 0.70–1.75×). On multidomain proteins with low-complexity insertions the change is up to 4.8 bits (E up to 32×). One-line fix per file plus a unit test against the generic version. |
| **HM2** | **CONFIRMED on 3.1b2, 3.3.2, 3.4 and `develop`** | **now** (same filing) | `region_trace_ensemble()` runs its "outside the domain" loop up to and including `sqfrom[d]`, the domain's first M-emitted residue. That residue gets null2 odds 1.0 in every sampled trace. A replay of the library's 200 traces reproduces its `n2sc` at 2356/2356 residues with the loop as written and at 1444/2356 with the documented `sqfrom..sqto` (25 human fn3 proteins). Alone it moves scores by up to 0.7 bits on Swiss-Prot. Together with HM1, 17 fn3 and 9 Pkinase hits move by up to 0.9 bits (E 0.74–2.0×; EPHA8_HUMAN 105.8 → 104.9 bits, bias 0.9 → 1.9). No reported or included set changed in any run. |
| HM3 | CONFIRMED on 3.1b2, 3.3.2, 3.4, `develop` | held | `nhmmscan -Z <x>` is documented ("set # of comparisons done, for E-value calculation"), echoed in the header ("sequence search space set to: 1000"), and ignored: E-values come from `log(nmodels)` plus the per-model `2L/MAXL`. `-Z 1000` against a one-model database leaves every E-value unchanged, while `hmmscan -Z` scales as documented. Rare option in a program no cohort sentence names. |
| HM4 | CONFIRMED on all four builds | held | Domain inclusion is not nested in domain reporting. With `--domE 1e-12` (default `--incdomE 0.01`), hmmsearch reports 12 domains but puts 79 into the `-A` alignment, and the tblout `inc` column sums to 79 against `rep` 12. The code comment says "(sequence\|domain) must be reported to be included", and the man pages say "Inclusion thresholds are stricter than reporting thresholds". Targets behave (14 reported, 14 included under `-E 1e-20`). The same path feeds jackhmmer's next round. Needs `--domE` stricter than `--incdomE`. |
| HM5 | CONFIRMED on 3.3.2, 3.4, `develop` (3.1b2 differs, below) | held | A protein Stockholm alignment with one value on `#=GF GA` is built into `GA 24.50 -99999.00`, so `--cut_ga` reports domains down to −4.0 bits (460 domains). For DNA models the reader sets GA2 = GA1. 3.1b2 drops the GA line entirely, and its `--cut_ga` then runs with no threshold at all (a 24.3-bit target reported). Pfam alignments carry two values, so this needs a hand-made alignment. |
| N1 | note, verified, documentation | held | The `acc` column is the envelope's optimal-accuracy score divided by the *envelope* length. The user guide says it is "the mean posterior probability of aligned residues in the MEA alignment". The two agree when envelope = alignment (4/4). They do not for 9 of 218 wider envelopes (globins4 ali 496–556 / env 489–630: acc 0.68 vs a PP-line mean of 0.88). |

**Held up under execution (all four builds unless stated):** every tblout/domtblout E-value
(full sequence, best domain, i-Evalue, c-Evalue) equals Z·exp(−λ(s−τ)) from the printed score
and the model's STATS line, with Z = number of targets (hmmsearch, phmmer) or models (hmmscan) and
domZ = number of reported targets, and under `-Z 1e6 --domZ 50`. The tblout `rep` column matches
the domtblout rows. hmmscan and hmmsearch give identical bit scores for the same pair. `--cpu 0/2/4`
give identical tables. nhmmer: E = P·N/MAXL with N = residues on both strands (one with
`--watson`/`--crick`); `-Z` in Mb equal to the true size reproduces the default exactly, and ×10
scales by 10. `--cpu 0/1/4` and `--block_length` change nothing. Coordinates, strand, envelope
containment and `sq len` are right on both strands. `-E`, `-T`, `--domE` (conditional), `--domT`,
the inclusion line and the domain `!` marks, and `--cut_ga/tc/nc` (GA1 on targets, GA2 on domains)
in hmmsearch and `--cut_ga` in hmmscan select exactly the predicted sets (68 checks). λ = log 2 +
1.44/(M·H) is recomputed from the file's emissions for four models; hmmbuild is deterministic at
the default seed; entropy weighting hits its relative-entropy target. On 100,000 i.i.d. null
sequences the fraction with P ≤ 1e-3 and ≤ 1e-4 is within 1.5× of nominal for three models, with
and without null2. The default and `--max` runs give identical scores for every shared hit on human
Swiss-Prot. jackhmmer's last round equals hmmsearch with its `--chkhmm` model. hmmsearch tables are
byte-identical across develop, 3.4, 3.3.2 and 3.1b2. Not checked: hmmalign, hmmpgmd/hmmserver, MPI,
the FM-index (`makehmmerdb`) path, translated search, the NEON and VMX builds (HM1's patch edits
them; only SSE was compiled), model construction options (`--symfrac`, `--fragthresh`), and
calibration accuracy for DNA models.

**Already reported or fixed upstream (not raised):** #319 (FM-index nhmmer `--watson/--crick`
E-values 2× too small) is fixed on develop by 56342ec but present in 3.4; not re-executed here.
#348 (`is_multidomain_region` overlap) is fixed on develop by a37e75b. #340 (jackhmmer `--incdomE`
uses the conditional E-value) was answered as intended.

## How the papers use HMMER (lower bounds from the survey cache)

| signal | papers |
|---|---|
| version stated | 52 (3.1b ×15, 3.3.2 ×14, 3.4 ×6, 3.3 ×4, 3.2.1 ×4, 3.1 ×3, others ×6) |
| hmmsearch / hmmscan named | 37 / 28 |
| phmmer / jackhmmer / hmmbuild | 3 / 2 / 6 |
| nhmmer / nhmmscan | 0 |
| Pfam named | 34 |
| `--cut_ga`/gathering thresholds | 7 |
| an E-value threshold stated | 21 |
| TIGRFAM / KOfam / dbCAN / antiSMASH / eggNOG | 7 |

`hmmer_profile.py` / `profile_run.log` count the survey's stored evidence sentences (one per paper,
`survey/data/paper_software.tsv`), so every number is a lower bound. Which finding reaches which
paper: HM1/HM2 reach every hmmsearch/hmmscan/phmmer/jackhmmer run that reports scores or E-values
of multidomain hits (Pfam domain tables, repeat-protein counts). In the runs here the change stays
inside default thresholds, so it moves printed numbers rather than hit lists. HM3–HM5 need options
or inputs no cohort sentence mentions.

## Filing channel

`EddyRivasLab/hmmer` has no CONTRIBUTING file, no templates, no `.github/` and no written AI policy.
README: PRs are based on `develop`, and problems go to the GitHub tracker. The maintainer fixed the
AI-submitted #348 himself, calling it "verbose but correct" in the commit, and outside PRs are
merged. Kit under [`upstream/`](upstream/): one issue text and one PR body (HM1 + HM2 together),
two `git am`-able patches on `develop` @ 37f7148, test runs and the duplicate check. **Fork
needed: EddyRivasLab/hmmer.**

## Files

| path | what |
|---|---|
| `component-reviews/evalues-domains-null2-thresholds.md` | the review: HM1–HM5, N1 with code citations, held-up list, upstream status |
| `verify/_hm.py` | shared helpers: builds, synthetic databases with recorded domain positions, HMM/tblout/domtblout/main-output parsers, the E-value formula |
| `verify/e1_evalues.py` | E-values vs Z·P(score), `-Z`/`--domZ`, hmmscan Z, phmmer, threads |
| `verify/n1_nhmmer_evalues.py` | nhmmer E = P·N/MAXL, `-Z` in Mb, strands, threads, block length, coordinates |
| `verify/t1_thresholds.py` | `-E`, `-T`, `--domE`, `--domT`, inclusion, `--cut_ga/tc/nc` in hmmsearch and hmmscan |
| `verify/c1_calibration.py` | λ formula, determinism, entropy-weighting target, null P-value tail on 100,000 sequences |
| `verify/h1_consistency.py` | default vs `--max`; jackhmmer vs hmmsearch on the checkpoint |
| `verify/n2_null2_bytrace.c`, `verify/n2_run.sh` | HM1 (SSE vs generic null2 on emitted traces) and HM2 (replay of `region_trace_ensemble`), compiled against each build |
| `verify/x1_null2_effect.py` | HM1/HM2 effect on hmmsearch tables: develop, HM1 only, HM2 only, both; human Swiss-Prot and stress set |
| `verify/z1_scan_Z.py`, `verify/i1_inclusion_nesting.py`, `verify/g1_single_ga.py`, `verify/a1_acc_column.py` | HM3, HM4, HM5, N1 |
| `verify/*.out`, `*.v<version>.out`, `*.patched.out` | captured output per build (`.out` = develop) |
| `hmmer_profile.py`, `profile_run.log` | cohort profile |
| `upstream/` | filing kit |

Data: synthetic databases are written by `_hm.py` from fixed seeds (cores emitted with the develop
`hmmemit`). Human Swiss-Prot was fetched from rest.uniprot.org on 2026-10-18 (20,431 entries, md5
`3e2011c3e0b55b524e1f1a29fcb20ed5`) into the session scratchpad and is not committed.

## Next steps

1. Fork `EddyRivasLab/hmmer`, push `fix/null2-bytrace`, and file the HM1 + HM2 issue and then the PR
   against `develop` (one filing).
2. Hold HM3–HM5 and N1 until a maintainer replies. HM4 goes first after that.
