# FieldTrip verification scripts

All scripts run FieldTrip's **own** MATLAB code (not a re-implementation) under
GNU Octave 8.4 with the `statistics` package. They were run against FieldTrip
`master` at commit 2e14f72 (Aug 2026). Set `FIELDTRIP` to the checkout:

```bash
export FIELDTRIP=/path/to/fieldtrip
octave-cli -q ft1a_all_perms.m
```

| script | finding | needs |
|---|---|---|
| `ft1a_all_perms.m` | FT1: strict `<` excludes the identity permutation; p = 0 with `numrandomization='all'` | nothing beyond FieldTrip |
| `ft1b_cluster_ties.m` | FT1: `maxsize` cluster p-values exclude ties (null simulation, 200 datasets); `maxsum` exonerated | `shims/spm_bwlabel.m` (see below), ~10 min |
| `ft7_corrT_df.m` | FT7: `ft_statfun_correlationT` critical value uses df = n−1 | `shims/corr.m` on Octave |
| `ft11_psi_edge.m`, `ft11b_psi_normalized.m` | FT11: PSI top-bin contamination / −Inf with `normalize='yes'` | nothing |
| `ftr_regrT_cvar.m` | FTR: `ft_statfun_depsamplesregrT` cvar branch crashes (`unitselved`) | nothing |

## Shims (Octave only)

- `shims/corr.m` — Octave's `corr` does not accept MATLAB's `'type'` argument;
  the shim computes column-wise Pearson r. Not needed on MATLAB.
- `shims/spm_bwlabel.m` — the cluster path calls SPM's `spm_bwlabel` mex. On
  Octave the mex is unavailable and FieldTrip's `external/spm12/spm_bwlabel.m`
  stub errors ("not compiled"). Because `ft_hastoolbox` prepends
  `external/spm12` to the path at run time, `addpath` cannot shadow the stub:
  copy the shim over `external/spm12/spm_bwlabel.m` (and `spm8`/`spm2`) in a
  scratch checkout. The shim implements 1-D run labeling only, which is all the
  single-channel harness uses. On MATLAB with SPM12 nothing is needed.

Expected outputs are quoted in `../component-reviews/statistics-core.md`.


## Running FieldTrip's own test scripts under Octave

`run_ft_test.sh <fieldtrip-tree> <test_name>` runs one `test/test_*.m` script
and prints a `RESULT ... PASS|FAIL` line. It puts `shims/` on the path:
`corr` (MATLAB `'type'` argument), `convertStringsToChars`, `strip`,
`istable` (MATLAB-only functions used by `ft_checkconfig`/plotting), and an
N-D `spm_bwlabel` stand-in (copy it over `external/spm*/spm_bwlabel.m` in the
tree under test, since `ft_hastoolbox` prepends those directories at run
time). Tests that need DCCN-private data, `websave`, or MATLAB numerics
(`test_bug3048`) cannot run this way; compare against unpatched master to
attribute any failure.
