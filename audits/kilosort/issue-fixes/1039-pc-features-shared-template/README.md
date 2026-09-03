# Kilosort issue #1039 — `make_pc_features` mixes up channel ids for clusters that share a detection template

**Issue:** [MouseLand/Kilosort#1039](https://github.com/MouseLand/Kilosort/issues/1039)
"BUG: make_pc_features can associate PC features with the wrong channel IDs when
multiple final clusters share a detection template" (gwfolk, 2026-07-26, open,
1 comment — the comment could not be read from this session; only the body).

**Reporter's claim:** when two final clusters are derived from the same
detection template, `make_pc_features` reorders the `tF` rows of *all* spikes
detected with that template while processing the first cluster, then reorders
the second cluster's rows again from the wrong starting order. Exported
`pc_features` / `pc_feature_ind` no longer correspond, and the output depends on
cluster iteration order. Visible in Phy's FeatureView as zero-valued / swapped
channels, worst with small `nearest_chans`. The reporter gave a 4-spike,
2-channel example and prototyped a fix on their fork
(`gwfolk/Kilosort@668370c`); no PR was opened.

## Diagnosis (upstream `main` @ `17743f2`)

`kilosort/postprocessing.py:105-127` (`make_pc_features`):

- line 107: `iunq = np.unique(spike_templates[spike_clusters==i])` — the
  templates of cluster *i*;
- lines 113-116: `get_data_cpu(ops, xy, iC, spike_templates, tF, ..., ix=ix)`
  is called with the **full** arrays, so `igood` is every spike whose template
  is in `iunq`, including spikes assigned to other final clusters;
- line 123: `tF[igood,:] = Xd[:, ind[:n_chans], :]` writes the re-ordered
  channels back for all of those spikes.

`get_data_cpu` (`kilosort/clustering_qr.py:560-598`) builds `dd` from `tF`
assuming each row's columns are in the template's original `iC[:, template]`
channel order (`dd[ij, imap[:, k]] = data[ij]`, line 589). Rows already
re-ordered by an earlier cluster violate that assumption, so the second
cluster's ranking and features are computed from mislabelled columns. The
cluster's *mean* (line 120) is also taken over other clusters' spikes, which is
not what the docstring ("features associated with the final clusters instead
of templates") describes.

## Fix (branch `fix/issue-1039-pc-features-shared-template`, commit `466c2a1`)

Select, rank and overwrite only the current cluster's spikes:

```python
cluster_spikes = np.flatnonzero(spike_clusters == i)
cluster_templates = spike_templates[cluster_spikes]
...
Xd, igood, ichan = get_data_cpu(ops, xy, iC, cluster_templates, tF[cluster_spikes], ...)
...
tF[cluster_spikes[igood.cpu().numpy()], :] = Xd[:, ind[:n_chans], :]
```

12 insertions / 5 deletions in `kilosort/postprocessing.py`; new
`tests/test_postprocessing.py` (2 tests). Patch: `0001-Fix-PC-features-for-final-clusters-that-share-a-dete.patch`.

Properties checked (`equiv.py`, output in `equiv.out`): on random data with
one-template-per-cluster the new function is byte-identical to `main`
(`feature_ind` and `pc_features`); with shared templates the new output is
invariant to relabelling clusters, whereas `main`'s `pc_feature_ind` is not.

## Reproduction

`repro.py` is the reporter's example (2 clusters, 1 shared template, 2 channels;
both clusters have their larger feature on channel 1).

Before (`repro.before.out`):

```
pc_feature_ind:
[[1 0]
 [0 1]]
restored (should equal source):
[[ 1. 20.]
 [10.  1.]
 [ 2. 18.]
 [ 8.  2.]]
pc_feature_ind correct: False; features restored correctly: False
```

After (`repro.after.out`):

```
pc_feature_ind:
[[1 0]
 [1 0]]
restored (should equal source):
[[ 1. 20.]
 [ 1. 10.]
 [ 2. 18.]
 [ 2.  8.]]
pc_feature_ind correct: True; features restored correctly: True
```

## Tests

Environment: Python 3.12 venv, kilosort editable from the clone, torch 2.14.0
(PyPI CUDA wheel run on CPU behind stub CUDA libraries, since
`download.pytorch.org` is blocked here; `torch.cuda.is_available() == False`).

| run | result |
|---|---|
| `pytest tests/test_postprocessing.py` before | 2 failed |
| `pytest tests/test_postprocessing.py` after | 2 passed (0.05 s) |
| `pytest tests` before | 5 failed, 8 passed, 1 skipped, 18 errors |
| `pytest tests` after | 3 failed, 10 passed, 1 skipped, 18 errors |

The 18 errors and the 3 remaining failures (`test_clustering.py::TestCenters::test_np1`,
`::test_np2_1shank`, `test_parameters.py::test_dmin`) are all pre-existing and
caused by the sandbox blocking the download of the test recording / probe
files (`URLError` / `Tunnel connection failed: 403`); they are identical before
and after.

Linter: the project ships no ruff/flake8 config. `ruff check` on the two touched
files: 2 findings before and after, both pre-existing on `main`
(`postprocessing.py:1 I001` import block order, `postprocessing.py:128 RUF059`
unused `sorted_chans`); `flake8 --select=E9,F`: 0 before and after.

## Other candidates considered

Only 15 issues are open on the repository (listed with
`search_issues` query `state:open`). Excluding the four filed by this account
(#1042, #1044, #1046, #1047) and pure feature requests:

- **#894** "cluster_templates function returns vastly different waveforms from
  the one in templates.npy" (5 comments, since 2025-03) — the body points at a
  plausible `spike_idx` semantics mismatch in `data_tools.cluster_templates`,
  but the claim needs a real sorting result to reproduce and the 5 unreadable
  comments likely already discuss it; not chosen.
- **#1041** GUI settings panel clipped unless fullscreen — Qt layout, needs a
  display; not chosen.
- **#686** drift correction on multi-shank probes (27 comments) — needs data and
  a design decision; not chosen.
- **#1039** — chosen: reporter's minimal example reproduces on `main`, no open
  PR (`search_pull_requests` for `make_pc_features`, `1039`, `pc_feature_ind`:
  none), 12-line fix in one function.

## Caveats

- The issue has one comment that could not be read from this session; if the
  maintainer already answered there, the PR body should be adjusted.
- The fix changes the channel ranking for clusters that share a template: the
  mean feature is now taken over the cluster's own spikes rather than pooled
  over all spikes of the shared template. The reporter suggested this or,
  alternatively, keeping the pooled ranking but writing only the current
  cluster's rows (which needs an untouched copy of `tF`). The per-cluster
  version is what the docstring describes and avoids the copy; the maintainers
  may prefer the other.
- The full-pipeline and data-dependent tests could not be run (no network);
  the touched function is exercised only by the new unit tests and
  `equiv.py`.
