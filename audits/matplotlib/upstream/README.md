# Upstream kit — Matplotlib

Fact sheets only. Matplotlib's contribution policy (`doc/devel/contribute.rst`, "Use of AI" on 44f2e00) does not
accept AI-generated issue or PR text or AI agents acting on GitHub, and asks for an AI Disclosure section on PRs.
The owner writes every issue, PR and reply from these facts. Nothing here is posted from a session.

The same policy lists as unacceptable "Increasing breadth of contributions, i.e. simultaneously contributing to
several projects. Instead of spreading your resources, you can provide greater value by engaging more deeply with
one or two projects." (contribute.rst:219–221). The audit files in many repositories at once, so whether and how to
file here is the owner's decision before anything else.

| folder | finding | fix (one line) | tests on the overlay env |
|---|---|---|---|
| `MPL1-boundarynorm-last-colour/` | BoundaryNorm with more colours than bins never uses the last colour | exact integer index, `colors.py:3317` | 4 new cases fail before, pass after; nothing else changes |
| `MPL2-violin-stats-masked/` | `violin_stats`/`violinplot` keep masked values (3.11.0–3.11.2, despite the 3.11 note) | `np.asanyarray`, `cbook.py:1591` | 3 new cases fail before, pass after; nothing else changes |
| `MPL4-hexbin-marginals-count/` | `hexbin(marginals=True)` with `C=None` draws every bar as 1 | `reduce_C_function = np.sum` when `C is None` | 1 new test; nothing else changes |
| `MPL15-stackplot-weighted-wiggle/` | `weighted_wiggle` baseline is the minimiser for the reversed layer order | `first_line = -center - 0.5 * total`, `stackplot.py:128` | new test passes; `test_stackplot_baseline[png]` must be regenerated (only the weighted_wiggle panel changes) |

Each folder: `facts.md` (versions, observed vs expected, documented promise and cause with file:line, related
threads, issue-template fields, AI-disclosure facts, weak points), `repro.py` + `repro.out` (re-run 2026-10-03 on
3.11.2: identical), `fix.patch` (applies to 44f2e00, ruff clean), `tests.txt` (before/after pytest counts on 3.11.2
with main's files overlaid; a full build of main is blocked by its SheenBidi download).

Separate problems noticed while testing, not searched on the tracker and not in any patch: the hexbin vertical
marginal drops points at min(y) (unpadded range), and the hexbin marginal colour-sync callback sets the horizontal
bars' colormap twice and the vertical bars' limits twice (`_axes.py:5927–5931`).
