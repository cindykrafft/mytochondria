# Survey scripts

Run in order from this directory. Each step writes into the same directory and is
resumable — re-running `extract.py` skips PMCIDs already present in `results.jsonl`.

| Step | Script | Output |
|---|---|---|
| 1 | `harvest_ids.py` | `records.jsonl` — Europe PMC metadata for the six journals, 2021–2026, by ISSN |
| 2 | `classify.py` | `process_in.jsonl` (research articles with full text) and `gap_list.jsonl` (those without) |
| 3 | `extract.py process_in.jsonl results.jsonl 24` | `results.jsonl` — one JSON record per paper: software detected, versions, evidence sentences, pipeline stages |
| 4 | `fix_versions.py results.jsonl results_fixed.jsonl` | recovers versions the in-span search missed, from the stored evidence sentences |
| 5 | `cleanup.py results_fixed.jsonl results_clean.jsonl` | drops detections whose evidence proves the match was something else |
| 6 | `build_docs.py <outdir>` | `README.md`, `data/*.tsv`, `data/pipelines.jsonl`, `packages/*.md` |

Steps 4 and 5 exist because both problems are correctable from data already stored,
without re-fetching 26,599 full texts. `extract.py` and `software_db.py` also carry
the fixes at source, so a run from scratch does not need them.

`epmc_crosscheck.txt` holds independent per-package counts from Europe PMC's own
full-text search; `build_docs.py` renders it as a validation table if present.

`software_db.py` holds the package dictionary. To extend the survey, add entries
there and re-run step 3 against a fresh `results.jsonl`.

Names that collide with ordinary English go in `AMBIGUOUS` with a context regex
(and optionally a negative pattern) rather than `SAFE`, so that e.g. `STAR` is not
matched by *Cell*'s "STAR Methods" section heading.

Only the Europe PMC REST API is contacted; no credentials are required.
