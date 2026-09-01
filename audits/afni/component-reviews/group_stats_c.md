# Component: group statistics in C
`3dttest++`, `3dttest` (legacy), `3dANOVA`/`3dANOVA2`/`3dANOVA3`, rank tests

AF2 CONFIRMED, demonstrated with a compiled harness. `src/3dttest++.c:4848`.
   A missing `!IS_PAIRED` guard lets the A-set-only `-zskip` reduction overwrite the
   pair-aligned arrays. When both sets contain zeros at non-identical subject
   indices, the paired t-test detects a length mismatch and silently writes
   mean = 0, t/z = 0.
   Impact: false negatives at exactly the partial-coverage voxels `-zskip` exists to
   rescue. Harness result: correct answer t = 5.0, program outputs 0.
   Exposure window is May 2021 onwards.

AF10 CONFIRMED. `src/3dttest++.c:4975-4977`: `-BminusA` combined with
   `-nomeans`/`-notests` negates the wrong result slots, so the output statistic
   keeps the A-B sign while labelled B-A -- directional and one-sided inferences are
   inverted. Default output mode is correct. Note `-singletonA <value>` auto-enables
   `-BminusA`, so `-singletonA ... -nomeans` is affected too.

AF11 CONFIRMED, numerically reproduced. `src/3dttest++.c:6614`,
   `src/3dGroupInCorr.c:4192`: a roundoff-prone copy of `GIC_student_t2z`, fixed
   years ago in `mri_stats.c` but never propagated, loses precision above z ~ 7.7 and
   saturates at z = 13.0 once two-sided p < ~2e-16 (verified: t = 30, df = 20 gives
   13.0 against a true 8.67). Does not move typical thresholds, but wrong z values
   appear in published maps and in meta-analyses of highly significant voxels.

AF17 LIKELY, data-dependent. `src/3dANOVA*.c`, `src/3dttest.c:898-963`: raw-score
   sums of squares in single precision. Catastrophic cancellation for data with
   mean >> sigma (un-demeaned signal) can let round-off dominate F statistics; the
   negative-SS clamps already in the code are the symptom. The post-2005
   mean/contrast t routines are double precision and fine.

VERIFIED CORRECT: `3dttest++`'s core t / Welch / covariate formulas,
Welch-Satterthwaite DF, covariate centering, and the permutation/Clustsim machinery;
the 2005-era `3dANOVA3` type 4/5 contrast fixes.
