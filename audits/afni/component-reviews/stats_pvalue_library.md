# Component: statistical distribution library & p-value machinery
`mri_stats.c`, `cdflib`, FDR machinery

No confirmed defects. This component is recorded because it is the one every other
finding depends on, and because a clean result here is load-bearing for reading the
rest of the audit in proportion.

VERIFIED CORRECT, against SciPy to reference precision including extreme tails: the
complete `mri_stats.c` p-value library -- t, F, correlation, chi-square, normal,
beta, binomial, gamma and Poisson conversions and their inverses.

Findings that live at the *callers* of this library, not in it: the stale private
t->z copy in `3dttest++`/`3dGroupInCorr` (AF11, see `group_stats_c.md`), and the
`qnorm(p)` vs `qnorm(p/2)` slip in `3dMVM -robust` (AF5, see `r_group_programs.md`).
Both are cases of correct mathematics existing in the tree and not being reached.

CONVENTION: the adaptive FDR scaling described in `dataset_arithmetic.md` is
implemented here and is deliberate.
