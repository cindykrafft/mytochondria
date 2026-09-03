# IQ-TREE upstream filing kit

_Prepared 2026-09-03 against `iqtree/iqtree2` `master` @ `a00094e0` (2.4.0) and
`iqtree/iqtree.github.io` `master` @ `3576c649` (the manual, 2026-07-22). **Nothing has
been filed.** The audit found no defect that changes a published number on realistic data,
so this kit contains documentation patches and discussion material, not bug reports._

## What was read before preparing this (step 4 of the method)

| document | what it says | how it shaped the kit |
|---|---|---|
| `iqtree2/README.md` "User support" | questions and feedback → GitHub Discussions; "feature requests bug reports" → GitHub Issues | Issues are for bugs; none of IQ1–IQ4 is a bug in the maintainers' sense, so no issue text is drafted |
| `iqtree2/.github/` | only `FUNDING.yml` and `workflows/ci.yaml` — **no CONTRIBUTING.md, no issue template, no PR template** | free-form; the Discussion draft below follows the structure of the project's own closed issue #228 (command line, version line from the log, expected vs observed) |
| `iqtree2/CODE_OF_CONDUCT.md` | Contributor Covenant 2.0 | tone |
| `iqtree3/README.md`, `.github/` | same wording, still pointing at the iqtree2 Issues/Discussions URLs; no templates | file against iqtree2's tracker as the README says, but state that the lines exist in iqtree3 too (they do: `tree/phylotree.cpp:5336`, `tree/iqtree.cpp:3854`, `tree/discordance.cpp:156,171,789`) |
| manual `doc/Frequently-Asked-Questions.md:52-62` "How do I report a bug?" | bug reports and feature requests to the **IQ-TREE Google group** with: command line, log file, and the data if possible | the older channel; recorded, not used — the code repository's README supersedes it |
| manual `doc/Home.md:93` | questions → `github.com/iqtree/iqtree3/discussions` | the Discussion draft is addressed there |
| `iqtree2/test_scripts/README`, `test_configs.txt` | tests are cluster job scripts run by the maintainers (`gen_test_standard.py`, `submit_jobs.sh`); no local test target | no code patch here, so no test run to report; the audit's own harnesses (`../verify/`) are the regression evidence |
| GitHub releases page (release notes; no changelog file in the repository) | — | no changelog entry to write |
| tracker searches (2026-09-03): thread/seed reproducibility; parametric aLRT / PhyML table; sCF NA rooted / `__root__` | #228 "Sequence order in the input and parallelism affect reproducibility" (closed 2024-06-17, 5 comments); #415 "Site concordance factor" (open, definition of decisive sites); #337, #467 (gCF questions, closed); nothing on `-alrt 0` or the cube | IQ3 is already known upstream (#228) — do not re-file; IQ1 and IQ4 have no prior report |

Rocklin's minimal-bug-report rules were applied to the Discussion draft anyway: the
alignment is written by the script, no line is unnecessary, expected vs observed are stated,
and the shrinking that located the mechanism (6 taxa → 4 taxa; `-te` on the alternatives) is
described.

## Contents

| file | what | intended venue |
|---|---|---|
| `0001-doc-say-what-the-parametric-aLRT-alrt-0-support-valu.patch` | IQ1: one sentence in the `-alrt` row of `doc/Command-Reference.md` | PR to `iqtree/iqtree.github.io` |
| `0002-doc-concordance-factors-need-unrooted-species-and-ge.patch` | IQ4: a warning box in `doc/Concordance-Factor.md` | PR to `iqtree/iqtree.github.io` |
| `discussion-iq2-ufboot-cutoff.md` | IQ2: reproduction of UFBoot 100 % vs standard bootstrap 61 % on the one-site alignment, with the cutoff mechanism | GitHub Discussion (question to the authors, not an issue) |
| `note-iq3-threads.md` | IQ3: what #228 covers and the one-line manual addition that would close the gap | append to #228 or fold into the IQ1 manual PR |

Both patches apply with `git am` on `iqtree.github.io` @ `3576c649` (they were made
there on branches `doc/parametric-alrt-support` and `doc/concordance-rooted-trees`, one
commit each). The manual repository has no linter or test suite; the pages are Jekyll
markdown and the patches touch prose only.

## Order of operations, if the lead decides to proceed

1. Open the two manual PRs (independent, small, no behaviour change).
2. Post the IQ2 Discussion; if the authors consider the cutoff worth an option or a
   warning, follow their lead on whether an Issue is wanted.
3. Do not open anything for IQ3; if the IQ1 PR is accepted, add the `-seed` sentence from
   `note-iq3-threads.md` in the same file in a follow-up.
4. Record responses in `../README.md` and the top-level status table.
