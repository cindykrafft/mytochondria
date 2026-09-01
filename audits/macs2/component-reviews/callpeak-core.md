# Component: MACS2/MACS3 callpeak statistical core

Primary text: the MACS2 2.2.7.1 sdist (the version papers pin most), read in
full — callpeak_cmd.py, PeakDetect.pyx, IO/CallPeakUnit.pyx, Prob.pyx,
Pileup.pyx, IO/FixWidthTrack.pyx, PeakModel.pyx (~8,000 lines) — with every
finding cross-checked against MACS2 2.1.1.20160309, MACS 1.4.3 (the original
2008 lineage) and current MACS3 (3.0.4 / git head). End-to-end reproductions
run on the shipped MACS3 3.0.4 binary.

## Confirmed findings

**MC1 CONFIRMED (2.1.x → current MACS3; reproduced on shipped 3.0.4):
`--keep-dup auto` filters the control with the treatment's duplicate
threshold.** `callpeak_cmd.py` computes the control-specific binomial
threshold, prints it to the log, and never uses it: 2.2.7.1 line 124 computes
`control_max_dup_tags`, line 133 runs `control.filter_dup(treatment_max_dup_tags)`;
identical in 2.1.1 (via `separate_dups`) and current MACS3
(`callpeak_cmd.py:133` vs `:142`). Reproduction (synthetic BEDs, thresholds
1 vs 3): the log prints "max_dup_tags based on binomial = 3" for control,
then "tags after filtering in control: 48636" — exactly the threshold-1
outcome (60,000 − 2×5,000 duplicates − collisions); at its own threshold the
control would keep ~59,99x. Because the binomial threshold grows only
logarithmically, the thresholds differ only when treatment and control
depths differ by roughly 5–10× (1 vs 2, 2 vs 3) — shallow-ChIP/deep-input
designs. Effect: duplicated control positions lose real reads → local lambda
underestimated at exactly the high-duplication loci → anticonservative
there (or conservative in the mirrored deep-treatment case). One-word fix.

**MC2 CONFIRMED convention note (every version since MACS 1.4, 2008): the
p-value is P(X > t), not the textbook discrete p-value P(X ≥ t).**
`get_pscore` → `poisson_cdf(n, λ, lower=False)`; all upper-tail
implementations sum from k+1 (verified in 1.4.3, 2.1.1, 2.2.7.1, 3.0.4).
One probability atom smaller than P(X ≥ t): at the default −log10 p = 5
cutoff the admitted null rate is 2× (λ=25) to 14× (λ=0.5) the nominal —
largest exactly in sparse-background ATAC/CUT&RUN data. Q-values inherit it
through the pqtable. Consistent for 17 years, so a definition/documentation
report, not a regression (`verify/tail_convention.py`).

**MC3 CONFIRMED latent (2.x releases): `__poisson_cdf_large_lambda` uses
`cdf` uninitialized.** The 2.x cythonization dropped MACS 1.4's `cdf = next`
initialization (Prob.pyx:261-301 in 2.2.7.1): C stack garbage enters the
sum. MACS3 zero-initializes (fixing the garbage) but still omits the k=0
term — numerically negligible at the λ>700 this branch requires. Unreachable
from the CLI in 2.x (all command paths use the log-space branch), so a
landmine rather than an active bias; trivial fix.

## Verified-negligible / notes

- **MC4**: scaled treatment pileup is truncated (`<int32_t>` cast) at every
  position before the Poisson while the control λ stays float
  (CallPeakUnit.pyx:692, 1267). Bites whenever treatment is scaled down —
  the default `--scale-to small` whenever treatment is deeper — a systematic
  ~0.5-count loss (conservative); floor-vs-round moves marginal calls.
- **MC5**: `call_broadpeaks` iterates chromosomes from the *lvl1* peak list
  (CallPeakUnit.pyx:1528): chromosomes with only weak-level regions lose all
  their broadPeak output.
- **MC6**: q-values are BH over basepairs with tie groups ranked at their
  first basepair (CallPeakUnit.pyx:711-728) — conservative; pscores rounded
  to 5 decimals in −log10 space enlarge ties (harmless).
- **MC7**: the model's cross-correlation lag axis is built with
  `np.linspace(−peaksize, peaksize, 2·peaksize)` against a `mode="full"`
  slice whose true lags run 1−peaksize..peaksize (PeakModel.pyx:213-214):
  d is off by ~1 bp. Negligible at d≈150-250.
- The no-control path uses only max(λBG, λ10k-of-treatment) — no d-window or
  slocal — where the with-control path uses max of three windows; the code
  comments itself ask "should this match w control??". Method note; this is
  the path most ATAC papers (no input) actually run.

## Withdrawn during review (raised, then disproven by closer reading)

- The summit "double-check" that discards a whole peak when its max-pileup
  segment fails a cutoff, and the mid-loop `return` in the `--call-summits`
  variant that would truncate summit lists: with the single scoring
  criterion `callpeak` always uses, every segment in a peak already passed
  that cutoff, so neither branch can fire. Dead code in standard runs, not
  a defect.

## What held up (verified, not just read)

- **--shift/--extsize arithmetic**: exact for the ATAC convention — with
  `--shift −75 --extsize 150` both strands produce [cut−75, cut+75)
  (FixWidthTrack.pileup_a_chromosome five/three-shift algebra traced for
  both strands, with and without directionality).
- **Local lambda**: max(λ_d, λ_slocal, λ_llocal) with λBG floor, faithfully
  the published model; control window scalings d/S·ratio verified; PE-mode
  ×2 control-end accounting is self-consistent through the ratio, the
  pileup mass, and the scaling factors.
- **The Jie Wang pileup algorithm**: independent sorting of starts/ends is
  valid (pileup needs no pairing); chromosome-end clipping keeps mass;
  bedGraph interval semantics through the treat/ctrl pairing merge.
- **filter_dup**: per-position/per-strand cap with correct total/length
  bookkeeping; duplicate threshold formula matches its binomial doc.
- **Scaling direction** (default to-small) decision table; log-space Poisson
  upper-tail series (term recursion, logspace_add, convergence); peak-model
  pairing balance checks (0.5 < plus/minus < 2, correct orientation).

## Maps to papers

199 ChIP / 181 ATAC / 72 scATAC / 48 CUT&RUN papers; only 32 mention an
input control, so the no-control path dominates the ATAC side. MC2's low-λ
regime is precisely that cohort. MC1 requires `--keep-dup auto` (subset of
the 26 keep-dup papers) plus a depth imbalance. 43 papers feed peaks into
DESeq2/edgeR and 28 into DiffBind — peak-list shifts propagate into the
differential analyses audited in ../deseq2.
