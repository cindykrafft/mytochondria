# Kilosort audit

Kilosort (MouseLand/Kilosort; MATLAB/CUDA through v3, Python/PyTorch from v4)
is the dominant spike sorter for high-density extracellular recordings —
60 papers in our six-journal survey cohort (2021–2026) use it, more than any
other spike sorter.

This audit covers the sorting core across the version lineage that the papers
actually pin, with adversarial code review of KS2 (v2.0.2), KS2.5 (v2.5.2),
KS3 (v3.0.2), and KS4 (v4.1.7), plus numerical verification of the new
findings on the shipped KS4 package (CPU build, kilosort 4.1.7 + torch 2.14).

## Cohort exposure

From `kilosort_profile.py` over the 60 papers' full texts
(`kilosort_profiles.jsonl`):

| version family | papers | notes |
|---|---|---|
| Kilosort 2 | 19 | largest group; branch never received the MATLAB-side spike-holes fix |
| Kilosort 2.5 | 12 | fixed only in v2.5.1/2 (Mar–Apr 2024) |
| Kilosort 3 | 10 | fixed only in v3.0.1/2 (Mar–Apr 2024) |
| Kilosort 4 | 1 | pre-4.1.5, so not exposed to KL1 |
| unversioned | 18 | context (Neuropixels/Phy/CatGT) indicates MATLAB era for most |

Context features: Neuropixels 33, Phy manual curation 33, single/multi-unit
inclusion criteria 46, quality metrics 10, CatGT/SpikeGLX 21, Open Ephys 16.
The inclusion-criteria numbers matter because two findings below (KL2, KM7)
target exactly the `good`/`mua` + ContamPct machinery those criteria rely on.

## Findings

Full detail with file:line citations in
[`component-reviews/sorting-core.md`](component-reviews/sorting-core.md).
Verification scripts with captured expected output in [`verify/`](verify/).

### New, verified on shipped code

| id | component | finding | impact |
|---|---|---|---|
| **KL1** | KS4 `swarmsplitter.py` (v4.1.5–v4.1.7) | `len(st2 == 0)` typo makes the guard fire on every non-empty spike train, so the refractory-CCG **split veto is dead code**; a maximally refractory pair (R12=0, Q12=0, pre-4.1.5 verdict "never split") sails through. The guard is also placed *after* `compute_CCG`, so the empty-array crash it targets still crashes. | Oversplitting of bursty/drifting single units on current KS4 releases. Independently reported as open issue [#1042](https://github.com/MouseLand/Kilosort/issues/1042) (no response, no PR); our contribution is the fix PR + guard relocation + quantified demo. |
| **KL2** | KS4 `CCG.py::refract` → `io.save_to_phy` | Clusters with ≤10 spikes are exported with **ContamPct = 0.0** — the best possible score (KS2.5/3 exported 100 for unevaluable units). Demo: 8-spike junk cluster → 0.0; 5000-spike Poisson unit → 93.9. | Papers filtering units by `ContamPct < x` without a spike-count floor silently admit junk clusters. |
| **KM3** | KS2/2.5/3 `get_whitening_matrix.m:48` | Covariance normalizer off-by-one: accumulates `floor((Nbatch−1)/nSkipCov)+1` batches, divides by `ceil(...)`. When `nSkipCov | (Nbatch−1)` (1 in 25 batch counts at defaults) the covariance inflates by (m+1)/m and all whitened-unit thresholds get `sqrt((m+1)/m)` harder — ×1.41 at ~57 s, ×1.05 at ~10 min, ×1.008 at 1 h. | Discontinuous detection-threshold changes across recording lengths; material for short recordings. Fixed in KS4. |

### New, established by code reading

| id | component | finding |
|---|---|---|
| **KM2** | KS2.5/KS3 `rezToPhy.m` | Exports a **scaled identity as `whitening_mat.npy`** (real `Wrot` line commented out) — KS2.0 exported the real matrix, KS4 does again. Templates "unwhitened" by downstream tools stay in whitened space; amplitudes not comparable across versions. No upstream documentation found. |
| **KM4** | KS2.5/KS3 `datashift2.m` | `ops.midpoint` chronic-recording branch calls `align_block`, which does not exist in the tree (and `yblk`/`F0`/`F0m` would be undefined) — the feature always crashes. |
| **KM5** | KS2.5 `splitAllClusters.m` | Split-provenance vector clobbered by a logical matrix (line 192); peak channels `iW` recomputed from post-tracking templates while features live on pre-tracking channel sets → split templates written to shifted channels for peak-drifting clusters. |
| **KM6** | KS2.5 `remove_ks2_duplicate_spikes.m` | `channel_separation_um` validated with `ischar` → numeric override impossible; the whole step is commented out of the default pipeline, so cross-template double counts remain in default output. |
| **KL3** | KS4 misc | `hierarchical.find_merges` pair-mass formula double-counts `cc[y,x]`/omits `cc[y,y]` (feeds an unreachable branch); undocumented loosening of the `good`-label p-threshold (0.05→0.2) on top of the documented `acg_threshold` change; spatial groups with <1000 spikes skip clustering entirely (one fused cluster). |

### Known upstream, exposure quantified here

**KM1 — "spike holes" (issue #594).** ~7 ms of undetected spikes every
~2.18 s (~0.3 % of the recording, periodic) in KS1→KS3 and pyKilosort; fixed
on the 2.5/3 branches only in **March–April 2024**, and on the KS2 branch only
partially (CUDA edge guards; the MATLAB batch loading/timestamping was never
patched). All 41 version-pinned MATLAB-era cohort papers — and effectively
the 18 unversioned ones — analyzed data with affected code. The first fix
(v2.5.1/v3.0.1) was itself revised a month later, so that intermediate
release is a third distinct behavior.

### Design notes (not defects)

`good`/`mua` labeling takes the minimum contamination over 10 nested CCG
windows against the most favorable of several baselines (KM7) — liberal by
construction, and KS4 loosened defaults further; drift registration uses
circular shifts that wrap probe ends (shared KS2.5→KS4). Papers treating
`KSLabel`/ContamPct as calibrated across versions inherit these choices.

### Withdrawn during review

KS4 batch tiling (no #594-style holes — verified padding algebra), the
interleaved matching-pursuit subtraction (correct by construction), the
`template_match` sign encoding, KS2.5's fixed `trackAndSort` tiling, filter
edge transients, and several others — see the end of
[`component-reviews/sorting-core.md`](component-reviews/sorting-core.md).

## Verification

```
verify/kl1_swarmsplitter_gate.py   # KL1 on shipped kilosort 4.1.7 (venv, torch CPU)
verify/kl2_contampct.py            # KL2 on shipped kilosort 4.1.7
verify/km3_nskipcov.py             # KM3 arithmetic + whitening-scale demo (pure numpy)
```

All three run headless on CPU; expected outputs are embedded in the module
docstrings and were captured from this audit's runs.

## Upstream status

- KL1: open issue #1042 exists (filed independently, also via Claude Code,
  Aug 21 2026); fix PR prepared in [`upstream/`](upstream/).
- KL2: issue + fix PR prepared in [`upstream/`](upstream/).
- KM2 (documentation erratum for KS2.5/3 Phy outputs) and KM3 are drafted as
  issues in [`upstream/`](upstream/); the MATLAB branches are frozen but did
  accept the 2024 #594 fixes, so KM3's one-character fix may still land.

## Files

- `kilosort_profile.py`, `kilosort_profiles.jsonl`, `profile_run.log` — cohort profiling
- `component-reviews/sorting-core.md` — full review with file:line citations
- `verify/` — reproduction scripts
- `upstream/` — filing kit (issues, PR bodies, patches)
