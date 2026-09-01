# FieldTrip audit

FieldTrip (fieldtrip/fieldtrip; MATLAB) is the dominant open toolbox for
MEG/EEG/iEEG analysis and the home of the cluster-based permutation test
(Maris & Oostenveld 2007). 42 papers in our six-journal cohort (2021–2026)
use it; 32 of them report Monte Carlo/permutation statistics and 19
explicitly cluster-based tests, so the permutation machinery is the primary
audit target, followed by the connectivity and spectral estimators.

All findings were verified by executing FieldTrip's own code under GNU
Octave (no re-implementation), against `master` @ 2e14f72.

## Cohort exposure

From `fieldtrip_profile.py` over the 42 full texts (`fieldtrip_profiles.jsonl`;
option-level re-grep in `fieldtrip_option_hits.json`):

| feature | papers |
|---|---|
| Monte Carlo / permutation statistics | 32 |
| cluster-based permutation explicitly | 19 |
| two-sided test at 0.05 described | 11 (5 state 0.025 per tail) |
| correlation-based cluster test | 8 |
| `maxsum` / cluster-mass named | 8 (`maxsize` named: 0) |
| exhaustive (`'all'`) permutations described | 1 |
| phase slope index | 1 |
| time-frequency (multitaper/wavelet) | 18 |
| connectivity measures | 17 |
| source reconstruction | 14 |
| FieldTrip version stated | 3 (all dated 2020 releases) |

## Findings

Full detail with file:line citations in
[`component-reviews/statistics-core.md`](component-reviews/statistics-core.md);
runnable Octave scripts with expected output in [`verify/`](verify/).

| id | component | finding | status |
|---|---|---|---|
| **FT1** | `clusterstat.m`, `ft_statistics_montecarlo.m` | Permutation p-values use strict `>`: with `numrandomization='all'` the identity permutation's exact tie is excluded and no +1 applies, so p is short by 1/Nperm and the most extreme observation gets **p = 0** (verified: 0.000000 vs exact 1/1024). With integer `maxsize` statistics ties are excluded systematically. | verified; fix patch |
| **FT7** | `ft_statfun_correlationT.m` | Cluster-forming critical value uses df = n−1 while the t-statistic has n−2 dof (threshold 3.4% too low at n=8). | verified; fix patch |
| **FT11** | `ft_connectivity_psi.m` | Phase slope index: last `nbin+1` frequency bins add the raw top-bin coherency; with `normalize='yes'` those bins are **−Inf**. | verified; fix patch |
| **FTR** | `ft_statfun_depsamplesregrT.m` | `unitselved` typo: any call with `cfg.cvar` crashes. | verified; fix patch |
| **FT2** | `ft_statistics_montecarlo.m` | The "two-sided without correcttail" warning fires only when alpha is exactly 0.05. | code-read; fix patch |

Design notes (documented behaviour with consequences for how papers should
be read): `correctm='fdr'` is Benjamini–Yekutieli, not BH;
`correcttail` defaults to `'no'` (per-tail alpha); several statfuns require
unit labels 1..N. Exonerations (coherence averaging, wPLI/PPC, beamformer
regularization, spectral scaling, F-statistic dfs, exhaustive enumeration
itself) are listed at the end of the component review.

## Verification

Octave 8.4 + `statistics` package; see [`verify/README.md`](verify/README.md)
for the two small shims Octave needs (`corr` signature; a 1-D `spm_bwlabel`
stand-in for the cluster harness). Every fix patch was re-validated by
re-running the corresponding script against the patched tree.

## Upstream

Five fix patches with PR bodies (and issues where discussion is warranted)
in [`upstream/`](upstream/). FieldTrip takes PRs on GitHub against `master`
from a fork.
