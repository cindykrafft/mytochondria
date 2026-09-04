# Numerical reproductions

Standalone harnesses for the AFNI findings that were verified by more than reading.
Each runs on its own and needs no AFNI installation.

| Harness | Finding | What it establishes |
|---|---|---|
| `reho_tie_sim.py` | AF1 / AF1b / AF1c | Faithful port of `CalcRanksForReHo` + `ReHoIt`, buggy vs fixed, across data scales and pipeline configurations |
| `reho_tie_results.json` | — | The checked-in output the project README and `../component-reviews/resting_state_connectivity.md` quote |

## reho_tie_sim.py

```
python3 reho_tie_sim.py          # three tables
python3 reho_tie_sim.py --json   # regenerate reho_tie_results.json
```

Requires numpy. Seeded (`default_rng(0)`), so the tables reproduce; the Cohen's *d*
in the last block moves by about ±0.1 between runs because it is estimated from a
separate draw.

Two implementation details are deliberate and must not be "tidied":

1. `sorted` is truncated with `np.trunc` — C's `int` cast truncates toward zero, it
   does not round.
2. The trailing tie run is **not** finalized by default, because the C loop at
   `rsfc.c:99-118` in every AFNI release through 26.2.03 only closes a run when a
   different value appears. This is AF1b, and it is what makes the error curve
   non-monotonic: input that fits entirely inside one integer bin gets no tie
   correction at all and therefore comes out exactly right.

   `CLOSE_TAIL = True` (or `reho(block, True, close_tail=True)`) models commit
   `29384a2` (authored 2023-09-27, merged to master only on 2026-08-27, one day
   before the float fix `94ee52b`), which closes the trailing run. With integer
   truncation still in place that turns every series lying inside one integer bin
   into one full-length tie, the denominator becomes exactly zero, and ReHo is
   NaN — which every AFNI program then reads as 0. That state shipped for about a
   day and is not what any published paper ran; it is modelled because the first
   pass of `../reanalysis/` accidentally used it as the "pre-fix" arm.

   Both regimes were verified voxel-for-voxel (four decimals) against 3dReHo
   binaries built from `29384a2^` and from `4c2bd54` on synthetic volumes
   (`../reanalysis/README.md`, "Three builds").

That second point corrected an earlier pass of this project, which had classified
sum-of-squares-normalised input (`3dTproject -norm`) as the maximal-tie, maximal-bias
regime. It is the opposite: unaffected. One published paper moved out of the exposed
set as a result — recorded in `../README.md`.
