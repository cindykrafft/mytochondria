# umap-learn audit against 1,111 published papers (2021–2026)

_Generated 2026-09-03 against `lmcinnes/umap` `master` @
`e78d85af` (2026-08-31, version string 0.5.12 — the same as the latest PyPI release).
Focus: the deterministic numerical core (fuzzy graph construction), verified by executing
the shipped code._

## What this is

The six-journal survey found **1,111 papers** in PNAS (544), *Nature* (453), *Cell* (77)
and *Science* (37), 2021–2026, that name UMAP — the largest exposure of any package in
the survey, and nearly every single-cell figure. Most reach it indirectly: 627 also name
Seurat (whose `RunUMAP` defaults to the R package `uwot`), 178 Monocle/ArchR/Signac (also
`uwot`), and 171 Scanpy, which calls umap-learn's `fuzzy_simplicial_set` and
`simplicial_set_embedding` directly with its own neighbour lists. Only 8 name
`umap-learn`/`umap.UMAP` explicitly. The numerical core that every route shares —
`smooth_knn_dist` (sigma and rho), `compute_membership_strengths`,
`fuzzy_simplicial_set` (the fuzzy union), `find_ab_params`, the spectral initialisation,
the exact / pynndescent / precomputed neighbour paths, `transform`, and the sparse-input
code path — was read in full on `master` and every suspicion was run through the
installed package (master, editable install in a Python 3.12 venv) on synthetic data with
known truth, against scipy, numpy or the paper's own definitions. The confirmed finding
was also run on the 0.5.12 and 0.5.3 wheels from PyPI. `uwot` (R) is out of scope for
this environment (no R).

## Findings (details and line citations in [`component-reviews/numerical-core.md`](component-reviews/numerical-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **U1** | **CONFIRMED on master, 0.5.12 and 0.5.3** (by git history, every release since 0.5.0) | `smooth_knn_dist`'s `MIN_K_DIST_SCALE` floor takes `np.mean` of a neighbour row that contains the `inf` marking a neighbour pruned by `disconnection_distance` (or an `inf` in a precomputed matrix), so sigma becomes `inf` and every remaining edge of that point gets membership strength exactly 1.0 instead of the graded kernel. Reproduced through the exact, pynndescent and both precomputed routes: 8 of 8 affected points, 56 of 56 kept edges at 1.0 where the paper's definition gives 1, 0.77, 0.69, 0.55, 0.41, 0.34, 0.14. Fires with default settings for `metric="jaccard"` on sparse binary data (513 of 1,000 rows wrongly `inf` on the test data) and for any hand-set `disconnection_distance`, which the FAQ recommends. Never with default euclidean, and only for exact antipodes with cosine/correlation. Rows without a pruned neighbour are unaffected. Patch with two tests ready. |
| U2 | note, design (documented remedy `unique=True`; docstring threshold understated) | Three duplicates of a point at k = 15 make the sigma equation unsolvable; sigma collapses to the floor and the point keeps weight only to its copies and its single nearest distinct neighbour (1–2 copies already halve the other weights). The docstring says it matters with "more duplicates than `n_neighbors`". |
| U3 | note, undocumented behaviour | `transform` builds its local graph with rho = 0 and the nearest training point excluded from the sigma sum, so even training points get different membership strengths (max diff 0.70, corr 0.87) than in `graph_`; only the identical full matrix short-circuits. |
| W1 | withdrawn | Open issue #1080 says `random_state` does not force `n_jobs = 1`; master does, and `n_jobs` 1 vs 4 are bit-identical on both neighbour paths. |
| W2 | withdrawn | Sparse metrics equal dense ones and scipy (≤ 6.7e-07); dense vs CSR fits are identical on the exact path. The pynndescent path differs between the two inputs, but that is the approximate search, as between two unseeded runs. |

**Held up under execution:** sigma/rho vs `brentq` on the paper's equation (rel. 4.6e-06;
row sums 3.9069 = log2 15), including fractional `local_connectivity`; the fuzzy union is
exactly symmetric, in [0, 1], and equals the numpy formula, for `set_op_mix_ratio` 1, 0.5
and 0; `find_ab_params` equals an independent least-squares fit (default a = 1.5769,
b = 0.8951); `spectral_layout` spans the dense `eigh` eigenspace to 1.6e-05 degrees and the
multi-component layout is finite; `precomputed` reproduces the euclidean fit; `transform`
is deterministic under `transform_seed`. Not audited: the SGD layout (`layouts.py`),
densMAP, Parametric/Aligned UMAP, the supervised intersection, `inverse_transform`,
`update`, the other metrics, pynndescent internals.

## How the papers use UMAP (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| Seurat named (RunUMAP → uwot by default) | 627 |
| Monocle / ArchR / Signac (uwot) | 178 |
| Scanpy named (calls umap-learn's graph and layout functions) | 171 |
| input: PCA / PCs stated | 267 (top PCs stated: 20 in 20 papers, 30 in 16, 50 in 15) |
| input: Harmony / scVI / latent space | 80 |
| Leiden / Louvain on the same graph | 96 |
| `n_neighbors` stated | 31 (30 in 12 papers, 20 in 6, 15 in 4, 50 in 3) |
| `min_dist` stated | 30 (0.3 in 5, 0 in 4, 0.1 in 4, 0.5 in 3) |
| cytometry input (CyTOF / flow / spectral) | 26 |
| spatial transcriptomics | 26 |
| metric stated: euclidean / cosine / correlation | 12 / 10 / 5 |
| `uwot` named / `umap-learn` or `umap.UMAP` named | 10 / 8 |
| random seed stated | 6 |
| transform / projection of new data | 5 |
| supervised UMAP / spread stated / 3-D or `n_components` | 2 / 3 / 4 |
| `disconnection_distance`, `unique`, `jaccard` mentioned | 0 |
| version stated | 2 (0.4.3, 0.5.1; a third string, 0.2.7.0, is not a umap-learn version) |
| scRNA-seq / snRNA-seq | 253 / 55 |
| year | 2021: 87, 2022: 130, 2023: 181, 2024: 239, 2025: 338, 2026: 136 |

U1 has no demonstrable published exposure: no cohort paper mentions
`disconnection_distance` or a bounded metric in its evidence snippets, and the Scanpy and
Seurat routes do not pass through `UMAP.fit`'s pruning. U2 is reachable by any umap-learn
user with duplicated rows (cytometry); U3 by the 5 papers projecting new data, if they
used umap-learn.

**Profiling caveat.** As for the Seurat and Scanpy audits, this session had no route to
Europe PMC, so `umap_profile.py` ran in `--offline` mode over the survey's stored evidence
snippets; every record in `umap_profiles.jsonl` is `source: survey_cache` and every count
above is a lower bound. Rerun without `--offline` from a host with Europe PMC access to
replace them with full-text records.

## Filing channel (read before anything is sent)

- `CONTRIBUTING.md` is the only contributing document: check the FAQ and search existing
  issues; reproduction instructions welcome; fork + PR with the issue number in the PR
  message; run `black`. **No `.github/` directory, so no issue or PR template.** No
  results-stability policy. `doc/release_notes.rst` lists features per minor release
  only; there is no per-PR changelog to add to.
- U1 is small, crisp, and changes numbers only for rows that currently get `inf`; file
  as an issue with the reproduction, then the PR. No prior issue (tracker searched
  2026-09-03; nearest #523, #410, #141). **The kit is in [`upstream/`](upstream/)**: the
  issue text with a minimal complete verifiable example run on `master` and 0.5.12, one
  `git am`-able patch (fix + two tests; both fail on unmodified `master`, the touched test
  files go from 25 to 27 passed with 7 skips), the PR body, and the list of documents
  read. Nothing has been filed and no fork was pushed.

## Files

| file | what |
|---|---|
| `umap_profile.py`, `umap_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/numerical-core.md` | the review: U1–U3, W1–W2, held-up list, not-audited list |
| `verify/u1_disconnected_sigma_inf.py` (+ `.out`, `_0.5.12.out`, `_0.5.3.out`) | U1: `smooth_knn_dist` vs the brentq reference with pruned neighbours; all four `fit` routes; default jaccard; the fixed function |
| `verify/note_duplicates_sigma_collapse.py` (+ `.out`) | U2: sigma and weights vs number of duplicates; `unique=True` |
| `verify/note_transform_vs_fit_graph.py` (+ `.out`) | U3: transform graph vs fit graph on training points; determinism |
| `verify/heldup_core_vs_reference.py` (+ `.out`) | held-up: sigma/rho vs brentq, symmetrisation, `find_ab_params`, spectral layout vs `eigh`, precomputed vs euclidean, `fast_knn_indices` |
| `verify/heldup_sparse_vs_dense.py` (+ `.out`) | W2: sparse vs dense metrics vs scipy; dense vs CSR fits |
| `verify/heldup_reproducibility.py` (+ `.out`) | W1: `random_state` across `n_jobs`, repeat runs |
| `upstream/` | filing kit: issue text, MCVE with outputs, patch 0001 (fix + tests), PR body, documents read |

Harnesses need the master install: `uv venv --python 3.12 venv && uv pip install -e
<umap clone> scikit-learn scipy numba pynndescent`. The 0.5.3 wheel additionally needs
`numpy<2 numba<0.60 scikit-learn<1.6 pynndescent<0.5.13 setuptools<80`.

## Next steps

1. File U1 upstream from the kit in `upstream/` (issue first, then PR from a fork).
   Record numbers and maintainer responses here.
2. Extend the review to `layouts.py` (the SGD, in particular the clipping and the
   negative-sampling epoch schedule) and to the supervised intersection.
3. Audit `uwot`, which is what most of the cohort actually ran, from a host with R.
4. Full-text profiling rerun when Europe PMC is reachable.
