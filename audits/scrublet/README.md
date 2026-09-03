# Scrublet audit against 78 published papers (2021–2026)

_Twelfth audit in the series. Generated 2026-09-03 against `swolock/scrublet` `master`
@ `67f8ecb` (2020-12-28; its source is identical to the PyPI 0.2.3 wheel) and against
Scanpy's port of it, `scverse/scanpy` `main` @ `a656a33b` (2026-08-28, 1.14.0.dev1), with
the scanpy 1.12.4 wheel as the released comparison. Focus: correctness at master,
verified by executing the shipped code, and where the port differs from the original._

## What this is

The six-journal survey files doublet-detection tools under one package name,
`scDblFinder` (aliases `scDblFinder`, `DoubletFinder`, `Scrublet`): **179 papers**, of
which **78 name Scrublet** in the cached evidence (*Nature* 56, PNAS 9, *Cell* 8,
*Science* 5; lower bounds, see the profiling caveat). Scrublet simulates doublets by
adding random pairs of observed cells, embeds everything by PCA, scores each cell by the
fraction of simulated doublets among its k nearest neighbours, and thresholds the
simulated-score histogram. Most Python users run it through `scanpy.pp.scrublet`
(51 of the 78 Scrublet papers also name Scanpy), which re-implements the pipeline with
Scanpy's own preprocessing and neighbour search. Both were read in full and every
suspicion was run through the installed packages on simulated counts with labelled
doublets, with an independent numpy/scipy port as the reference.

## Findings (details and line citations in [`component-reviews/scrublet-core.md`](component-reviews/scrublet-core.md); harnesses with captured output in [`verify/`](verify/))

| id | where | status | finding |
|---|---|---|---|
| **SR1** | Scanpy port | **CONFIRMED on `main` and 1.12.4** | The classifier scores each cell over `k_adj − 1` neighbouring cells while dividing by `k_adj` (the original uses `k_adj`), and which variant applies — `k_adj − 1` others, or `k_adj − 1` plus the cell itself — is decided globally by whether any two points in the manifold coincide, which the port's own pair sampler produced in 7 of 7 runs. On the same PCA manifold 763 of 1,650 observed cells score lower than in the original (none higher), the maximum attainable score is 0.625 instead of 0.772, the threshold moves 0.1876 → 0.1697, 2 calls flip. Fix + test + release note in the kit. |
| **SR2** | original (master = 0.2.3); port metadata only | **CONFIRMED** | `subsample_counts` (used when `synthetic_doublet_umi_subsampling < 1`, default 1) thins the kept genes first and then re-draws the counts it just removed: simulated totals are rate·T + rate·(1 − rate)·F instead of rate·T (2,250 vs 2,000 in a constructed case; 1.056× at rate 0.8 in the pipeline), so every simulated doublet is normalised to 1e6 with an inflated total. Mean simulated score +0.047, threshold 0.1876 vs 0.1701, 1 call flips. The port runs the same code but only stores the result in `obs["n_counts"]` (1.2×). Fix + test in the kit. |
| **SR3** | Scanpy port | **CONFIRMED on `main` and 1.12.4** (undocumented behaviour difference) | `log_transform=True` applies `log1p` to median-normalised observed cells and to raw-count simulated doublets, *before* the 1e6 normalisation; the original normalises both first and logs both. A doublet made from a cell and itself lands 8 % (mean) / 19 % (max) away from that cell instead of on it. Measured effect on calls on the labelled data is small (recall 0.940 vs 0.980 without the log). Fix + test + release note in the kit. |
| **SR4** | original (master = 0.2.3) | **CONFIRMED** | `scrub_doublets(mean_center=True, normalize_variance=False)` raises `TypeError: np.matrix is not supported` from sklearn's PCA (CSC − `np.matrix` gives an `np.matrix`); reproduced with scikit-learn 1.4.2 through 1.9.0. The other three combinations run; the port converts to CSC and runs. One-line fix + test in the kit. |
| SR5 | both | note, design | The doublet score `q·ρ/r / (1 − ρ − q(1 − ρ − ρ/r))` is `odds/(1 + odds)` under a model in which every observed neighbour is a singlet; in a pure doublet state it evaluates to 1/(2 − ρ) = 0.526 at ρ = 0.1, reaching 1 only when no observed cell is among the neighbours. Calls are unaffected (threshold on the same scale); the paper's derivation could not be fetched. |
| SR6 | original | note, documentation | The v-score noise fit uses `np.percentile(·, 0.1)` — the 0.1th percentile, essentially the per-bin minimum — where the parameter name suggests a fraction. Deterministic and reproduced exactly. |
| SR7 | Scanpy `Neighbors` | note, by execution | For coincident cells `compute_neighbors` stores a cell as its own neighbour (self-edge); issue #2244 reports the same duplicates from the other side. Not audited further. |
| SR8 | original | note, design | `simulate_doublets` reseeds the *global* numpy RNG (`np.random.seed`), resetting the caller's session state. |
| W1–W4 | — | withdrawn | ddof-1 z-scores (uniform factor, invariant); `sparse_var` precision (2e-15); SR3 as a detection-wrecking bug (recall 0.94 vs 0.98); my first reading of SR1's sklearn path as "always self-counted". |

**Held up under execution:** the whole original pipeline with exact neighbours equals
the independent port bit for bit (gene filter, parents, PCA to 9e-12, scores, standard
errors, threshold, rates); dense/CSC/CSR/float32 inputs give identical scores;
`random_state` reproduces runs exactly, including annoy; the score is the stated
odds form, `se_q` is the Beta posterior sd, `se_Ld` is first-order error propagation
(2e-10); annoy vs exact neighbours changes no call on this data; the threshold fallback
behaves as documented; the port given the original's matrices agrees to Spearman 0.996
with only SR1 left. Not audited: plotting/embedding helpers, `batch_key`, pynndescent
accuracy, `threshold_minimum` internals.

## How the papers use the doublet tools (lower bounds from the survey cache)

| signal | all 179 | of the 78 naming Scrublet |
|---|---|---|
| Seurat in the same paper | 150 | 53 |
| doublets/cells removed by the score | 116 | 48 |
| DoubletFinder named | 73 | 1 |
| Scanpy in the same paper | 65 | 51 |
| run per sample / library | 51 | 26 |
| "default parameters" | 50 | 23 |
| scDblFinder named | 31 | 2 |
| threshold stated | 14 | 5 (values 0.01 ×3, 0.05 ×2, 0.3 ×2, 0.1, 0.15, 0.18, 0.25, 0.4, 0.9 across the cohort) |
| Scrublet version stated | 9 | 9 (0.2.1 ×7, 0.2.3 ×5, 0.2.2 ×1, 0.1 ×2) |
| `sim_doublet_ratio` / `n_neighbors` / `n_prin_comps` stated | 3 | 3 |
| expected doublet rate stated | 2 (5 %, 4.7 %) | 1 |
| Scanpy port named explicitly (`sc.pp.scrublet` / `scanpy.external`) | 1 | 1 |

Every stated version is a 0.2.x release with source identical to master, so SR2 and SR4
apply to every version the cohort names — but only on the non-default options
(`synthetic_doublet_umi_subsampling < 1`; `mean_center=True, normalize_variance=False`),
which no cached evidence mentions. SR1 and SR3 apply to whichever papers ran the port
(51 of 78 also name Scanpy; one names the port) — SR1 on every run, SR3 only with
`log_transform=True`. No cohort paper's numbers can be recomputed from here.

**Profiling caveat.** As for the Seurat and Scanpy audits, this session had no route to
Europe PMC, so `scrublet_profile.py` ran in `--offline` mode over the survey's stored
evidence snippets; every record in `scrublet_profiles.jsonl` is `source: survey_cache`
and every count above is a lower bound (`profile_run.log`). Two "versions" the window
caught (1.6.0, 3.6) are neighbouring packages' and are excluded from the family count.
Rerun without `--offline` from a host with Europe PMC access.

## Filing channel (read before anything is sent)

- **Scrublet** (`swolock/scrublet`): no `CONTRIBUTING.md`, no issue or PR template, no
  changelog, no test suite, no CI. `README.md` gives install instructions and best
  practices only. Last commit 2020-12-28; the tracker has open issues without maintainer
  replies since 2020 (#16, #19, #39, #58, #59). Expect no response; a plain GitHub issue
  per finding with the reproduction, and a PR from the patch, is the only channel. The
  kit's patches add a `tests/` directory (pytest) because there is nothing to extend.
- **Scanpy** (`scverse/scanpy`): `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/bug-report.yml`
  (checkboxes; a minimal code sample that runs under `uv run` with inline script
  metadata; error output; `sc.logging.print_versions()`), `config.yml` (questions to
  Discourse), `docs/dev/code.md` / `documentation.md` / `testing.md` (fork, branch,
  tests, towncrier fragment `docs/release-notes/+name.fix.md`, Ruff),
  `.github/pull_request_template.md` ("Closes #", tests or why not, release note or why
  not). The "Check for release notes" workflow wants the fragment renamed to
  `<PR>.fix.md` once the number exists. Tracker searched 2026-09-03: no prior report of
  SR1 or SR3; #2244 (duplicate cells in `pp.neighbors`) and #3068 (a scrublet test
  flaking by one cell at 1e-15) are related and should be cited.
- **The kit is in [`upstream/`](upstream/)**: four issue texts, four `git am`-able
  patches with tests (scanpy's with release-note fragments), PR bodies, and a README
  listing what was read. Nothing has been filed.

## Files

| file | what |
|---|---|
| `scrublet_profile.py`, `scrublet_profiles.jsonl`, `profile_run.log` | profiling pass over the 179-paper doublet-tool cohort (offline; see caveat) |
| `component-reviews/scrublet-core.md` | the review: SR1–SR8, withdrawn list, held-up list, not-audited list, and the original-vs-port table |
| `verify/synth.py`, `verify/reference.py` | synthetic counts with labelled doublets; the independent numpy/scipy port |
| `verify/heldup_reference_port.py` (+ `.out`, `.release.out`) | original vs reference: helpers, v-scores, full pipeline, closed forms, annoy |
| `verify/sr1_scanpy_knn_self_neighbour.py` (+ outs) | SR1: rule identification on a shared manifold, consequences, mechanism, per-seed branch taken |
| `verify/sr2_subsample_totals.py` (+ outs) | SR2: closed form, pipeline effect with the shipped vs fixed function, port metadata |
| `verify/sr3_scanpy_log_transform_order.py` (+ outs) | SR3: recall/precision by setting and package, per-cell sums at log time, self-doublet displacement |
| `verify/sr4_mean_center_np_matrix.py` (+ outs), `verify/sr4_sklearn_versions.py` (+ `.out`) | SR4: the four option combinations with traceback; scikit-learn 1.4.2–1.9.0 |
| `verify/compare_original_vs_scanpy.py` (+ outs) | same input, same seed: defaults, shared simulated doublets, shared manifold, ddof |
| `upstream/` | filing kit: `scrublet/` (2 issues, 2 patches), `scanpy/` (2 issues, 2 patches with tests and fragments), PR bodies, README |

Harnesses need both packages installed: `uv venv --python 3.12 venv && uv pip install
-e <scrublet clone> -e "<scanpy clone>[scrublet]" annoy pynndescent scikit-image`;
the `.release.out` files come from a venv with `scrublet==0.2.3 scanpy==1.12.4`.

## Next steps

1. File SR1 and SR3 on scanpy (issue, then PR from the kit; PR 1 needs the pinned
   `test_scrublet` expectations regenerated, which needs the pbmc3k download this
   environment could not make). File SR2 and SR4 on scrublet as plain issues + PRs and
   expect no reply; consider also noting on the scanpy issues that the port carries
   SR2's code.
2. Full-text profiling rerun when Europe PMC is reachable, to find which cohort papers
   ran the port and whether any used `log_transform` or UMI subsampling.
3. SR7 (`Neighbors` self-edges for coincident cells) deserves its own look under
   `sc.pp.neighbors`, next to #2244.
