# HMMER — E-values, search-space scaling, domain definition, null2, thresholds and calibration

_Read on `EddyRivasLab/hmmer` `develop` @ `37f7148` (2026-09-30, version string 3.5, July 2026;
not yet released — the eddylab.org tarball `hmmer.tar.gz` is still 3.4) with Easel `develop` @
`69efc38`; executed on that build and on the release tarballs 3.4, 3.3.2 and 3.1b2 built here.
Line numbers refer to `develop` @ `37f7148`. Every number below comes from a harness in
`../verify/` whose captured output sits next to it (`.out` for develop, `.v<version>.out` for the
releases, `.patched.out` for the fix branch)._

Files read: `src/p7_pipeline.c` (filters, `p7_Pipeline_Mainstage`, the long-target pipeline,
reportable/includable tests, `p7_pipeline_Merge`), `src/p7_domaindef.c` (region detection,
`is_multidomain_region`, `region_trace_ensemble`, `rescore_isolated_domain`),
`src/impl_sse/null2.c` and `src/generic_null2.c` (null2 by expectation and by trace; the NEON
and VMX copies), `src/p7_tophits.c` (`p7_tophits_Threshold`, the h74 workaround,
`ComputeNhmmerEvalues`, text/tabular/Xfam outputs), `src/evalues.c` (`p7_Calibrate`,
`p7_Lambda`, `p7_MSVMu`, `p7_ViterbiMu`, `p7_Tau`), `src/modelstats.c`, `src/p7_builder.c`
(`effective_seqnumber`, cutoff transfer), `src/eweight.c`, `src/p7_hmmfile.c` (cutoff
read/write), `src/nhmmer.c` (Z in megabases, strands, FM-index), `src/nhmmscan.c`,
`src/jackhmmer.c`, `src/hmmsearch.c`/`hmmscan.c` (diff against 3.4), and in Easel
`esl_exponential.c`, `esl_gumbel.c`; the user guide (`tabular.tex`, `pipeline.tex`,
`tutorial.tex`) and the man pages for the documented behaviour.

## Findings

### HM1 — the vector `p7_Null2_ByTrace()` scores insert-state residues with match emission odds (every version)

The null2 ("biased composition") correction of a domain that comes out of stochastic traceback
clustering is computed from 200 sampled traces in `region_trace_ensemble()`
(`p7_domaindef.c:596-641`), each domain of each trace through `p7_Null2_ByTrace()`
(`p7_domaindef.c:625`). The production (SSE) implementation counts state usage like this
(`impl_sse/null2.c:159-168`):

```c
if (tr->k[z] > 0)	/* must be an M or I */
  {
    // s = ( (tr->st[z] == p7T_M) ?  p7X_M : p7X_I);  // We don't need the state type <s>, but this is how you'd get it.
    q = p7X_NSCELLS * ( (tr->k[z] - 1) % Q) + p7X_M;
    ...  u.p[r] += 1.0;
```

so a residue emitted by insert state `I_k` is added to the match cell of node `k`. The sum that
follows weights match cells by the match emission odds and adds the insert cells with "insert
emission odds implicitly 1.0" (`:199-202`) — but the insert cells are never filled. The generic
reference `p7_GNull2_ByTrace()` counts inserts separately (`generic_null2.c:181-182`) and weights
them by `exp(ISC)` (`:202`), which is 1.0 because insert scores are 0 in a configured profile
(`modelconfig.c:164`). History: the state type `s` was computed and never used when the file was
written (d277c46, 2008); the 2016 `-Wall` cleanup (0529ea3) commented it out with "We don't need
the state type". The NEON (`impl_neon/null2.c:161-162`) and VMX (`impl_vmx/null2.c:172`) copies
are identical. Only regions resolved by clustering are affected (the `clu` column of `--tblout`);
single-domain regions use `p7_Null2_ByExpectation()`, which agrees with the generic version (its
unit test, `utest_null2_expectation`, is the only null2 test in the tree).

Execution (`verify/n2_null2_bytrace.c`, run through `n2_run.sh`): on 500 sequences emitted from the
tutorial fn3 model the SSE and generic null2 vectors agree on all 562 domains without an insert
state (max |Δ log odds| 3.8e-7) and differ on all 469 domains with one (max 1.2); Pkinase: 289 / 0
and 784 / 784 (max 0.81). Same on 3.4, 3.3.2 and 3.1b2. With the fix: 0 differ.

Effect on what a paper reads (`verify/x1_null2_effect.py`, default options, develop vs develop
with the fix): human Swiss-Prot (20,431 reviewed entries) searched with fn3 — 11 of 194 reported
sequences change score by up to 0.7 bits, E-values by 0.72–1.75×; with Pkinase 8 of 483, up to
0.6 bits. On a synthetic set of 2–6-domain proteins with a low-complexity segment inserted inside
half of the domains (the case where insert composition matters), 56 of 100 fn3 hits change, by up
to 4.8 bits, E-values 0.26–32×. No reported or included (E ≤ 0.01) set changed in any of these
runs: the error moves bit scores, the `bias` columns and E-values of multidomain hits, not which
hits pass default thresholds here.

Fix (`upstream/0001-…patch`): put the count in the I cell when `tr->st[z] != p7T_M`, in all three
vector files; adds `utest_null2_trace()` to the SSE null2 test driver (compares to the generic
version on profile-emitted traces; fails without the fix).

### HM2 — `region_trace_ensemble()` counts each sampled domain's first residue as outside the domain (every version)

```c
pos = 1;
for (d = 0; d < ddef->tr->ndom; d++) {
  p7_Null2_ByTrace(om, ddef->tr, ddef->tr->tfrom[d], ddef->tr->tto[d], wrk, null2);
  /* residues outside domains get bumped +1 ... */
  for (; pos <= ddef->tr->sqfrom[d]; pos++) ddef->n2sc[ireg+pos-1] += 1.0;          /* :628 */
  /* Residues inside domains get bumped by their null2 ratio */
  for (; pos <= ddef->tr->sqto[d];   pos++) ddef->n2sc[ireg+pos-1] += null2[...];   /* :631 */
}
```

`sqfrom[d]` is the first M-emitted residue of the domain (`hmmer.h:389`, set in
`p7_trace_Index`, `p7_trace.c:1189`), so the first loop also gives residue `sqfrom[d]` the
outside value 1.0. The second loop's `<= sqto` shows the domain is meant to be inclusive.

Execution: `n2_null2_bytrace.c` test 2 re-derives the region boundaries from the library's own
decoding arrays, replays the same 200 stochastic traces (same seed, same Forward matrix, same
`p7_Null2_ByTrace`) and accumulates them once as written and once with the domain as
`sqfrom..sqto`. On the 25 human Swiss-Prot proteins whose fn3 search has a clustered region,
the library's `n2sc` equals the as-written accumulation at 2356/2356 residues and the documented
one at 1444/2356 (max difference 0.29 nats); Pkinase 7825/7825 vs 5766/7825 (0.13). Same on all
four builds; with the fix, 2356/2356 and 7825/7825 equal the documented rule. End-to-end
(`x1`), alone: up to 0.7 bits / E 1.6× on human Swiss-Prot (fn3), up to 1.2 bits on the stress
set. Fix (`upstream/0002-…patch`): `<` for `<=` in the first loop.

HM1 and HM2 are filed together (one issue, one PR with two commits): same calculation, same
function family, and both fixes are one line.

### HM3 — `nhmmscan -Z` is accepted, echoed, and ignored (every version)

`nhmmscan` offers `-Z <x>` "set # of comparisons done, for E-value calculation"
(`nhmmscan.c:81`) and prints `# sequence search space set to: <x>` (`:247`), but its E-values
are set as `lnP += log(nmodels)` (`:513`) after the per-model `log(2L/MAXL)`; `pli->Z` (which `-Z`
sets, `p7_pipeline.c:197`) is never read on the long-target path (`p7_pipeline.c:411-412`: "database
size is already built into the Pval"). `verify/z1_scan_Z.py`: with one model, `-Z 1000` leaves
every E-value unchanged (ratio 1.0) on develop, 3.4 and 3.3.2, while `hmmscan -Z` scales E as
documented; `nhmmscan` and `nhmmer` otherwise agree on the same comparison. Held: rare option in
a rarely used program (no cohort evidence sentence names nhmmer or nhmmscan).

### HM4 — domain inclusion is not nested in domain reporting (every version)

`p7_tophits_Threshold()` flags a domain included when its target is included and the domain
passes `--incdomE`, whether or not it passed `--domE` (`p7_tophits.c:976-984`), although the
comment above says "(sequence|domain) must be reported to be included" (`:966-971`) and the man
pages say "Inclusion thresholds are stricter than reporting thresholds" (`hmmsearch.man.in:204`).
Targets are nested (a target must be reported to be included). `verify/i1_inclusion_nesting.py`:
`hmmsearch --domE 1e-12` (default `--incdomE 0.01`) reports 12 domains but writes 79 into the `-A`
alignment, and the tblout `inc` column sums to 79 against `rep` 12; `-E 1e-20` at the target level
behaves (14 reported, 14 included). The same path feeds jackhmmer's next-round alignment. Held:
needs a `--domE` stricter than `--incdomE`, which no cohort paper states.

### HM5 — a protein alignment with one `#=GF GA` value gets a domain GA of −99999 (every version)

Easel accepts `#=GF GA 24.50;` with one value. `p7_builder.c:983-988` copies GA1 and leaves GA2
at `p7_CUTOFF_UNSET` (−99999), and `p7_hmmfile.c:551` writes `GA    24.50 -99999.00` for a protein
model (for DNA the reader sets GA2 = GA1, `p7_hmmfile.c:1439`). `verify/g1_single_ga.py`:
`hmmsearch --cut_ga` with that model reports 460 domains down to −4.0 bits (99 targets ≥ 24.5)
on develop, 3.4 and 3.3.2. 3.1b2 behaves differently and no better: its hmmbuild writes no GA line
at all, yet `--cut_ga` runs without the "GA bit thresholds unavailable" error and applies no
threshold (a 24.3-bit target and domains down to 0.2 bits reported; `g1_single_ga.v3.1b2.out`).
Held: Pfam alignments always carry two values; this needs a hand-made alignment.

### N1 — the `acc` column is normalised by envelope length, not by aligned residues (documentation)

User guide `tabular.tex:313`: "acc: The mean posterior probability of aligned residues in the
MEA alignment". Code (`p7_tophits.c:1377, 1410, 1776`): `oasc / (1 + |jenv − ienv|)`, where
`oasc` is the optimal-accuracy score of the whole envelope. `verify/a1_acc_column.py`: when the
envelope equals the alignment, acc matches the mean of the alignment's PP line (4/4); when the
envelope is wider, 9 of 218 domains fall below the PP-derived bounds, e.g. globins4 domain ali
496–556 / env 489–630: acc 0.68 against a mean PP of 0.88. Held (documentation).

## Held up under execution (all four builds unless stated)

- **E-values from scores.** Every `--tblout`/`--domtblout` E-value (full sequence, best domain,
  i-Evalue, c-Evalue) equals `Z · exp(−λ(s − τ))` from the printed score and the HMM's `STATS
  LOCAL FORWARD` line, within printing precision, for globins4, fn3 and Pkinase on a
  1,670-sequence database (`e1`), with Z = number of targets and domZ = number of reported
  targets by default, and under `-Z 1e6 --domZ 50`; `rep` equals the domtblout rows per target;
  hmmscan's Z = number of models; hmmscan and hmmsearch give identical bit scores for the same
  pair; phmmer scales with `-Z`; `--cpu 0/2/4` give identical tables.
- **nhmmer.** `E = P · N / MAXL` with N = residues searched on both strands (one with
  `--watson`/`--crick`, `--toponly`/`--bottomonly` on 3.1b2); `-Z` in megabases equal to the true
  size reproduces the default E-values exactly; `-Z` ×10 scales by 10; `--cpu 0/1/4` and
  `--block_length 60000` change nothing; alignment coordinates, strand orientation, envelope
  containment and `sq len` are right for inserts on both strands (`n1`).
- **Thresholds.** `-E`, `-T`, `--domE` (conditional E-value), `--domT`, the inclusion line and
  the domain `!` marks (`--incE`, `--incdomE` defaults), `--cut_ga/tc/nc` (GA1 on targets, GA2 on
  domains, everything reported included) in hmmsearch and `--cut_ga` in hmmscan all select exactly
  the sets computed from an unthresholded run (`t1`, 68 checks).
- **Calibration.** λ = log 2 + 1.44/(M·H) recomputed from the emission probabilities in the file
  matches the stored λ (5 decimals) for all four models; MSV, Viterbi and Forward share it;
  `hmmbuild` is deterministic at the default seed; entropy weighting hits its target
  max(0.59 or 0.62, (45 − log2(2/(M(M+1))))/M); on 100,000 i.i.d. null sequences (L = 300) the
  fraction of comparisons with P ≤ 1e-3 and 1e-4 is within ±1.5× of nominal for all three protein
  models, with and without null2 (P ≤ 0.01 runs 0.94–1.28× of nominal and P ≤ 0.1 1.6–2.4×, the
  region where the exponential-tail fit is not claimed) (`c1`).
- **Consistency.** default vs `--max` give identical scores and E-values for every shared hit on
  human Swiss-Prot; jackhmmer's last round equals hmmsearch with that round's `--chkhmm` model
  (same 83 targets, scores within 0.1 bit, E-values within two `%.2g` roundings) (`h1`).
- **Version stability.** develop, 3.4, 3.3.2 and 3.1b2 produce byte-identical hmmsearch tables
  on the 1,670-sequence database for all three models.

## Already reported or fixed upstream (not raised)

- #319 (FM-index `nhmmer --watson/--crick` E-values 2× too small): fixed on develop by 56342ec
  (`nhmmer.c:483` multiplies `char_count` by 2 only for both strands); 3.4 still has
  `resCnt = 2 * fm_meta->char_count`. Not re-executed here (FM-index path).
- #348 (`is_multidomain_region` E(z)/B(z) overlap): fixed on develop by a37e75b. The fix changes
  which regions go to clustering on develop vs 3.4 (one of 25 test-2 proteins in `n2…v3.4.out`
  warns that the re-derived region count differs), not the outputs compared above.
- #340 (jackhmmer `--incdomE` thresholds the conditional E-value): answered by the maintainer
  as intended behaviour (2026-06-03).

## Not checked

`hmmalign`, `hmmpgmd`/`hmmserver`/`hmmclient`, MPI builds, the FM-index (`makehmmerdb`) search
path, `--pfamtblout`/`--dfamtblout` beyond reading, translated search, the NEON and VMX builds
(HM1's patch touches them; only the SSE build was compiled and run here), `--fragthresh`/`--symfrac`
model construction, and calibration accuracy for DNA models.
