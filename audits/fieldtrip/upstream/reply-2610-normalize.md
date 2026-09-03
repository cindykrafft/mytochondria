# Reply on PR #2610 to the maintainer's question about `normalize`

- what `normalize='yes'` computes (`verify/ft11c_psi_normalize_meaning.py` + `.out`): the normalizer is built after `x` holds the products, so it is `|C(f)||C(f+1)|²|C(f+2)| + 1`; the option multiplies the PSI by `1/(s⁴+1)` at constant coherence `s` (1.000 at 0.05, 0.941 at 0.5, 0.551 at 0.95); neither phase-only nor Nolte's `Ψ/std(Ψ)`.
- proposal: keep #2610 scoped to the edge bin; the normalize option is the maintainers' call (document, redefine as `Ψ/std(Ψ)` from the existing `v` output, or drop); happy to prepare whichever.
- rationale comment added to `test_ft_connectivity_psi.m` (`9d99bac`); `test_ft_connectivityanalysis` with hanning tapers passes on master and the branch under Octave (`verify/pull2610-octave/`).
