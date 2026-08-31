# Component: randomise (permutation inference + TFCE) + fdr
Traced at master (tag 2203.3, ~FSL 6.0.6 era) with full git history for version dating.

F1 CONFIRMED historical (FSL <=5.0.6, fixed 5.0.7 commit 67a7e9a 2014-07): F-contrast TFCE
   enhanced the RAW F map and converted to z only after enhancement -> a different statistic
   than documented TFCE-on-z (peak-dominated effects gain, extent-dominated lose).
   Papers pinning FSL <=5.0.6 with F-TFCE have p-values that do not reproduce on >=5.0.7,
   with differences that can cross 0.05 either way near threshold. t-TFCE unaffected.

F2 CONFIRMED (all 4.1.x-6.0.x): fast tfce() excludes the outermost voxel shell
   (newimagefns.h:2422 minX=1..max-1). Border suprathreshold voxels get TFCE=0 (never
   significant); clusters touching the volume face under-enhanced in observed AND null.
   Standard padded MNI152 analyses unaffected; tight FOV/subject-space masks exposed.

F3 CONFIRMED: --twopass second pass drops variance smoothing and voxelwise EVs
   (randomise.cc:733-737 uses plain calculateTstat) -> normalised null on a different
   scale than pass-1 sums. Hidden option, rare in publications.

F4 CONFIRMED UB: --detectNull reads uninitialized isFlipping (randomise.cc:1012-1015 vs
   first assignment :1042) -> permutation space depends on stack garbage. Hidden beta flag.

F5 CONFIRMED: --uncorrp writes all-zero "uncorrected p" images for cluster extent/mass
   statistics (store overload never updates uncorrectedStatistic; OutputStat writes it
   anyway) -> _clustere/_clusterm *_p_* images are p=1 everywhere. corrp unaffected.

F6 CONFIRMED input hazard: .fts rows counted only when coefficient == exactly 1
   (randomise.cc:917) -> hand-edited VEST values silently drop contrasts from F tests.

F7 CONFIRMED historical (fixed FSL 6.0.6, 2022-03): fdr computed in float; 1-p near 1.0
   quantized (~6e-8) -> parametric-map FDR adjusted p truncated in extreme tail
   (randomise-derived p immune; q=0.05 decisions essentially never flip). Pre-2012
   step-up used strict < (conservative on discrete grids).

F8 PLAUSIBLE by-design: permutation space built on unique rows of projected design
   (labels), Freedman-Lane statistic not invariant within label class -> classic
   randomise coset behavior (Winkler 2014); differs from PALM at 3rd decimal. Not a bug.

VERIFIED CORRECT: p convention exact Phipson-Smyth with identity included, p >= 1/nPerms,
ties against H0, sampling without replacement, exhaustive enumeration correct incl.
multi-block; genuine Freedman-Lane with rank-robust dof; TFCE core (fixed dh from perm 1
reused across perms, connectivity tables, H/E/C defaults incl. --T2, F->z BEFORE
enhancement since 5.0.7, cancelling constants); current fdr is correct BH step-up.

REPRODUCIBILITY NOTE: RNG changed rand()->mt19937_64 in FSL 6.0.6 (Nov 2021): identical
--seed gives different permutation sets across that boundary; pre-6.0.6 not reproducible
across platforms at all. Cross-version p mismatches are expected, not evidence of bugs.

MAPS TO: 10 randomise papers (5.0.9 x11 named versions => F1 exposure check for F-TFCE;
TBSS/--T2 users; tight-FOV studies for F2).
