# Component: resting-state & connectivity tools
`3dReHo`, `3dRSFC`, `3dTproject`, `3dBandpass`, `3dNetCorr`, `3dTcorr*`, `3dGroupInCorr`

AF1 CONFIRMED, numerically reproduced (the audit's one finding with documented
   published exposure). `src/ptaylor/rsfc.c:63-118`. Ranks come from a true float
   sort, but tie *detection* compares int-truncated values: `int *sorted` receives
   `THD_get_voxel()` floats, so any two values sharing an integer part are declared
   tied, their ranks collapsed to a group average and the tie-correction term
   `T = sum n(n^2-1)` spuriously inflated, shrinking W's denominator.
   Bias measured against a faithful float port (27-voxel neighbourhood, N=200,
   true W ~= 0.60, 40 sims/point):

       SD of input   1000    50    10     5     3     2     1    0.5   0.25   0.05
       rel. error    0.0%  0.0%  0.1%  0.4%  1.4%  4.0% 20.4%  54.1%  0.2%   0.0%

   (`../reproductions/reho_tie_results.json`, checked in.)

   Non-monotonic, and the shape matters: see AF1b. Raw EPI (hundreds to thousands)
   and grand-mean-scaled-to-10,000 data are unaffected; percent-signal-change data,
   which is exactly what `afni_proc.py`'s default `scale` block produces
   (`db_mod.py:5620` `db_cmd_scale`, voxelwise `a/b*100`), sits at SD ~ 1-2.
   Residuals (`errts`) of that scaled data sit at SD ~ 0.5-2 -- the worst of the band.

AF1b CONFIRMED (second defect in the same routine, and the reason AF1's curve turns
   back down). The tie loop only closes a run when a *different* value appears
   (`rsfc.c:99-118`); a run reaching the end of the sorted array is never finalized.
   So when a voxel's whole series falls inside one integer bin, no ranks are
   rewritten and no tie term accumulates -- the answer is exactly correct, by
   accident. This exonerates L2-normalised input (`3dTproject -norm`, sum of squares
   = 1, |x| <= 1 by construction): a configuration an earlier pass of this audit had
   classified as the maximal-tie regime. Corrected here.

AF1c CONFIRMED, and the reason this is not merely a rescaling. The number of spurious
   ties is set by each voxel's own amplitude, so the buggy statistic is partly a
   measure of BOLD variance. Holding true W constant at 0.60 and varying only SD:

       SD (% signal change)  0.30   0.50   0.75   1.00   1.25   1.50   2.00   3.00
       computed W           0.543  0.265  0.403  0.480  0.516  0.548  0.570  0.595

   Two simulated groups with identical true ReHo and a 25% difference in BOLD
   amplitude -- an ordinary consequence of age, medication, vascular status or
   anaesthesia -- separate at Cohen's d = 2.7 on the buggy statistic where the true
   effect is zero (0.480 vs 0.399; seed-dependent, d ~ 2.5-2.7 across runs). Harness: `../reproductions/reho_tie_sim.py`.
   Fixed upstream: afni/afni PR #944 (`sorted` -> float).

AF18 LIKELY (convention vs docs). `src/3dTproject.c:687, 701-702, 1312-1313`.
   The +/-1e-4 Hz stopband margin is smaller than the +/-df/6 rounding nudge, so a
   bin sitting exactly at fbot/ftop is regressed out. Verified: passband 0.01-0.10 Hz
   over 300 s keeps bins 4-29, where `3dBandpass`/`1dBport` keep 3-30 -- about 4 DOF
   difference. Each tool is self-consistent; AFNI's own bandpass routes disagree
   slightly with each other, and the help does not describe the behaviour.

AF19 MINOR. `src/ptaylor/3dRSFC.c:540-543`: fALFF/fRSFA denominators drop the top
   frequency bin for odd-length series (typically <<1%).

VERIFIED CORRECT: Kendall tau-b (fuzzed against SciPy), Spearman tie handling,
Pearson and partial correlation, Fisher-z conventions across the C correlation tools,
RSFA's Parseval identity, and `3dTproject`'s DOF accounting.
