Title: (comment on #2610) test_pull2610 removed; extended tests pass; dpss issue filed

<!-- Reply to schoffelen's comment of 2026-09-04 on PR #2610 ("OK, touché ..."). Plain tone. Fill in the dpss issue number once FT12 is filed. -->

Thanks for taking the normalization in hand.

- `test_pull2610` is removed (9af1fc4), as suggested.
- Your extended `test_ft_connectivity_psi` passes on the branch head under Octave 8.4 (with a stand-in for `sum(..., 'omitnan')`, which this Octave lacks), and `test_ft_connectivityanalysis` with hanning tapers passes on it as well.
- The dpss point is filed as #NNNN with a reproduction. `ft_specest_mtmfft` asks `double_dpss` for two outputs and `external/signal/dpss_hack/dpss.m` returns one, so every `taper='dpss'` call through the hack stops with "Too many output arguments" (Octave: "dpss: function called with too many outputs"). `ft_specest_mtmconvol` and `ft_specest_irasa` ask for one output and are unaffected. The issue proposes returning the concentrations as a second output of the hack, precomputed alongside the tapers; since the hack is the only dpss route Octave has, that would cover Octave too.
