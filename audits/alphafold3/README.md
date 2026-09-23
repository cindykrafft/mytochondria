# AlphaFold 3 (google-deepmind/alphafold3)

Not a survey-driven audit: AlphaFold 3 entered the project through a code review of the
inference and data-pipeline code on 2026-09-02, made against `main` at c0f97ed (2026-08-19).
Fifteen findings came out of it, each as a fix branch on the fork
[cindykrafft/alphafold3](https://github.com/cindykrafft/alphafold3) with the reasoning in its
commit message (`upstream/README.md` has the table). None was filed at the time: the project's
two-per-repository cap and the CLA requirement put them behind the other kits.

## What has been filed

| when | what | outcome |
|---|---|---|
| 2026-09-23 | issue #746 + PR #747 (`fix/summary-confidences-chain-ids`, AF2) | Open; CLA check to watch. |
| 2026-09-22 | issue #744 + PR #745 (`fix/to-json-preserves-chain-order`, AF1) | Open; the CLA check is the thing to watch. |
| 2026-09-03 | PR #734, `fix/ccd-user-ccd-copy`: a `userCCD` overlay mutated the memoised base CCD dict, so one input's user CCD stayed visible to every later input in the process | Closed 2026-09-21 by Augustin-Zidek: "thanks for the PR and for catching this bug. I submitted a fix in 3485995 and I will make sure to mention you in the release notes for the next version!" The CLA bot had failed the PR (no CLA on file), so the maintainer committed the same change himself, crediting the PR in the commit message. Thread read in full 2026-09-22 (helper transcript, two comments). |

## The next two (kits ready 2026-09-22)

Both are pure-Python defects that change a file users read, both reproduced by execution on
`main` a66cc52 (2026-09-21) and shown fixed on the fork branches, both merge cleanly:

- **AF1** `Input.to_json()` reorders chains when identical chains are separated by a different
  chain. `run_alphafold.py` writes every job's `_data.json` with it and the documented two-stage
  workflow feeds that file back in, so the second stage runs a different chain order (token layout,
  `asym_id`/`entity_id`/`sym_id`) than the end-to-end run. A,B,C comes back as A,C,B. Present since
  v3.0.1. Branch `fix/to-json-preserves-chain-order` (fix + regression test that fails on `main`).
- **AF2** `summary_confidences.json` `chain_ids` is one entry per token, not per chain as
  `docs/output.md` says, so zipping it against `chain_ptm`/`chain_iptm` mislabels chains silently;
  150 entries against 2 on the run output shipped in `test_data`. Added in v3.0.4. Branch
  `fix/summary-confidences-chain-ids` (one line).

Kit: `upstream/issue-af1-*.md`, `upstream/issue-af2-*.md`, `upstream/pr-bodies.md`; reproducers,
stub runners and their outputs under `verify/`.

## Rules that apply here

- `CONTRIBUTING.md`: small bug-fix and documentation patches only. AI-generated code, docs or PR
  text is accepted if it is declared in the PR message, manually reviewed and manually tested
  ("we might ask you to fold a certain input"); hallucinated test results are called out
  explicitly. The PR bodies carry the declaration; the review and the test run must be the
  submitter's own before the PR is opened (`upstream/pr-bodies.md` lists the commands).
- Google CLA (https://cla.developers.google.com/) before any PR; #734 shows what happens without it.
- No issue or PR templates. Issues are labelled by the maintainers (`question`, `bug`, ...).
- Two unanswered filings per repository (`audits/TRIAGE.md`); the remaining twelve branches wait.

## How the reproducers ran

This environment has no AlphaFold 3 C++ build and no GPU. The pure-Python modules involved
(`common/folding_input.py`, `model/confidence_types.py`) were imported from a `git archive` of the
tree with the compiled modules (`alphafold3.cpp.*`, `structure.mmcif`, `chemical_components`,
`model.model`) replaced by stub modules whose attributes are inert dummy classes; nothing in the
stubs is called by the code paths exercised. `folding_input_test.py` runs the same way: 91 of its
110 tests pass on `main` and on the branch, and the 19 that error are the mmCIF/CCD-dependent
ones, identical on both (`verify/test-runs.txt`). The shipped run output
(`test_data/alphafold_run_outputs/*.pkl`) was unpickled with a lenient unpickler that keeps the
metadata dict intact.
