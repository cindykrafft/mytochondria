# Bowtie 2 upstream filing kit

_Default branch: **`master`** (PRs go against it). Prepared 2026-09-24 against
`BenLangmead/bowtie2` `master` @ `58e34bf` (VERSION 2.5.5, unreleased; last release 2.5.4).
**Nothing filed, nothing pushed.** The two fixes are single commits on local branches of the
audit clone, `git am`-able from the patches here against `58e34bf`; they need a fork of
`BenLangmead/bowtie2` under `cindykrafft` to be pushed._

Filing tier (README step 5): **now** for BW1 (a master-only regression from 2026-09-14 that
would ship with 2.5.5; one-token fix) and BW2 (every version; six-line fix). **BW3 and BW4
ready** as reports (BW3: code or manual, the maintainers' call; BW4: mechanism established, PR
shape offered) once BW1 or BW2 has a reply, under the two-unanswered-filings cap. N1–N3 held.

## What was read before preparing this (step 4 of the method)

- No `CONTRIBUTING.md`, no `CODE_OF_CONDUCT`, no issue or PR template, no AI-contribution
  policy anywhere in the tree (`README.md`, `MANUAL.markdown`, `.github/` — which holds only
  `simple-tests.yml` and `random-tests.yml` — `NEWS`, `TUTORIAL` searched). The manual's
  "Getting help" section points at the mailing list and the GitHub tracker; bug reports with
  reproductions are the norm on the tracker.
- `.github/workflows/simple-tests.yml`: `make -j4 allall` then `make simple-test`
  (`scripts/test/simple_tests.pl`, Perl with `Test::Deep`, against the normal, debug and
  sanitized builds) on Linux, Linux with `SSE_AVX2=0`, and macOS; `random-tests.yml` runs the
  simulator. The PR bodies name the test script; it was run here on both branches
  (`test-runs.txt`).
- `MANUAL.markdown`: the scoring, "Mapping quality", "Aligning pairs", "Mixed mode",
  `--no-mixed`, `--no-discordant`, `-I/-X`, `-3/-5`, `--trim-to`, `--score-min` and
  `--soft-clipped-unmapped-tlen` entries, as the statement of intended behaviour.
- `git blame`/`git log`: BW1's line is from 41ee86b (2026-09-14, "Add support for MQ:i SAM
  flag"), not in any tag (`git tag --contains` empty; 2.5.4 is the latest tag); BW2's branch in
  `sam.cpp` and the `--no-mixed` gating in `aln_sink.cpp` predate 2.3.5.1 (executed on the
  2.3.5.1 binary); BW4 reproduces identically on the 2.3.5.1 binary.
- Issue tracker searched 2026-09-24 (twelve `search_issues` phrasings: MAPQ mate, MQ:i, XS
  mate, no-mixed discordant, TLEN soft clip, maxins trimmed, score-min, spurious indel,
  insertion mate window ...) and the threads listed below read in full through two helper
  sessions. **No prior report of BW1, BW2 or BW4.** Related: #430 (open, 2023, "very
  different alignment rates with and without --no-mixed --no-discordant" — a different
  effect, on concordant counts); #474 (open, 2024, asks what the two options are for); #180
  and #346 (open, soft clips in `TLEN`) for N1; #56 (closed 2017) for the local
  `--score-min` default; #337 (closed, fixed in 2.4.3) and #407 (open) on MAPQ semantics; #95
  (open, labelled bug) turned out to be gap penalties outside Bowtie 2's limits, not BW4; #58
  (closed) and its 2022 comment show users counting "concordantly exactly 1 time" pairs by the
  absence of `XS:i` and getting different numbers — the concordant case is not BW2, but the
  same recipe is what BW2 breaks for unpaired mates; #180's reporter asked (2018, open) for
  the `TLEN` soft-clip option to be mentioned in the local-alignment and dovetailing sections.
- Threads read in full: helper artifacts "Mytochondria threads bowtie2 430 95 196 203 357 407
  56 337 474 78 252 254" and "Mytochondria threads bowtie2 346 180 26 140 344 276 58 466".
- `site/audits.json` records no fork of `BenLangmead/bowtie2` under `cindykrafft`; the
  `upstream-declines-ai-contributions` topic cannot apply.

## Contents

| file | what |
|---|---|
| `issue-bw1-mate2-mapq-opposite-length.md` | bug report: the `reportHits` call, six pairs with the two MAPQs, the port, the fix |
| `issue-bw2-xs-missing-unpaired-mates.md` | bug report: the `printAlignedOptFlags` branch, 30 `YT:Z:UP` records with MAPQ 1 and no `XS:i`, the fix |
| `issue-bw3-no-mixed-suppresses-discordant.md` | report: manual vs code for `--no-mixed`, 80 discordant pairs → 0, either fix offered |
| `issue-bw4-maxins-boundary-spurious-insertions.md` | report: the fragment-length scan, the 6,000-pair library, the mechanism (`otherMate` window → gapped rescue alignment → `RedundantAlns` drops the exact one), three fix shapes offered |
| `0001-Use-the-opposite-mate-s-length-when-computing-mate-2.patch` | BW1 fix (`aln_sink.h`, one token), commit 08b9e93 on `fix/mate2-mapq-opposite-length` |
| `0001-Report-XS-i-for-mates-aligned-as-unpaired-alignments.patch` | BW2 fix (`sam.cpp`), commit 9d17d42 on `fix/xs-for-unpaired-mates` |
| `pr-bodies.md` | PR titles and bodies |
| `test-runs.txt` | Bowtie 2's own `simple_tests.pl` on both branches; the harness runs on the patched builds |

## Verification status of the patches

| branch | commit | harness on the patched build | project tests |
|---|---|---|---|
| `fix/mate2-mapq-opposite-length` | `08b9e93` | `../verify/m1_mapq.patched.out`: 9/9 blocks; all 16 concordant pairs give both mates the port's value (6 differed on master) | see `test-runs.txt` |
| `fix/xs-for-unpaired-mates` | `9d17d42` | `../verify/a1_summary_arithmetic.patched.out`: `XS:i` on 30/30 `YT:Z:UP` multi-mapping mates (0/30 on master); every other line unchanged | see `test-runs.txt` |

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| BW1 | `master` (58e34bf) | 2.3.5.1, 2.4.2, 2.4.5, 2.5.1, 2.5.4; patched |
| BW2 | 2.3.5.1, 2.4.2, 2.4.5, 2.5.1, 2.5.4, `master` | patched |
| BW3, BW4, N1, N2, N3 | 2.3.5.1, 2.4.2, 2.4.5, 2.5.1, 2.5.4, `master` | — |

## Order of operations

1. Fork `BenLangmead/bowtie2`; tell the session; the two branches are pushed.
2. Open the BW1 issue from `issue-bw1-mate2-mapq-opposite-length.md`, then the PR from
   `fix/mate2-mapq-opposite-length` with the body from `pr-bodies.md` § PR 1 (issue number in
   the first line). Same for BW2 (`fix/xs-for-unpaired-mates`, § PR 2).
3. When one of them has a maintainer reply: BW3, then BW4 (reports; no PR until the maintainers
   choose the shape).
4. Record issue and PR numbers and every maintainer response in `../README.md` and the
   top-level status table.
