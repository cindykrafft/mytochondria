# featureCounts (Subread) upstream filing kit

_Prepared 2026-09-08 against `ShiLab-Bioinformatics/subread`, **default branch
`master`**, @ `55dc154` (2023-07-30; builds as featureCounts v2.0.6). **Nothing
filed.** Both findings are held (step 5: neither changes a number under default or
common settings), and the tracker could not be read from this session, so the
lead has to check for prior reports and for maintainer activity before anything
is sent._

Release channel: the maintainers publish Subread on SourceForge
(`https://sourceforge.net/projects/subread/`, source tarballs `subread-<v>-source.tar.gz`;
2.1.1 is the latest, `readSummary.c` dated 2025-04-16) and the same C code as the
Bioconductor package Rsubread (the 2.1.1 users guide is titled "Rsubread
v2.22.1/Subread v2.1.1"). The GitHub repository has 50 commits, pushed in bulk
("Importing subread-2.0.1 codes", "latest changes to Subread, matching the
subread-2.0.2 release", "sync code with Rsubread latest version"); its only tag
is `2.0.2`; `master` is at the 2.0.6 code. Whether the maintainers use the
GitHub issue tracker is **unknown from here**: `mcp__github__search_issues`
returns 0 results for the repository under three phrasings, `list_issues` is not
enabled for it in this session, `api.github.com` answers 403 through the proxy
and `github.com` HTML is blocked. A code comment cites the Subread Google Group
(`readSummary.c:3311`, `groups.google.com/forum/#!topic/subread/...`) as a user
forum, and Rsubread users are directed to the Bioconductor support site.

Branches (in the scratchpad clone, not pushed): `fix/splitonly-singleton-fragments`
(`3ad59a3`, patch 0001) and `fix/read-type-filter` (`2c28bce`, patch 0002), each one
commit on top of `55dc154`.

## What was read before preparing this (step 4 of the method)

- `README.md` (the only contributing document): installation from the SourceForge
  release page or Bioconductor, `make -f Makefile.Linux` in `src/`, `test/test_all.sh`
  for the test suite, the three citations. No CONTRIBUTING, no issue/PR templates,
  no `.github/`, no changelog, no code style or linter, no pinned policy issue.
  Shaped the kit: free-form issue texts (a `Title:` line and a body), patches that
  follow the file's own style (tabs, `SUBREADprintf`, the read-group table pattern
  used by the neighbouring filters), and a test case in the project's own harness.
- `test/featureCounts/featureCounts-test.sh`, `test_corner_cases.sh` and
  `data/compare.sh`: each case is a SAM file, a GTF/SAF and an `.ora` file listing
  every gene's expected count; `compare.sh` runs `../../bin/featureCounts` and
  compares column 7. Both patches add `corner-<NAME>.sam` + `.ora` and one line to
  `test_corner_cases.sh`.
- `doc/SubreadUsersGuide.tex` §"featureCounts" (read filtering order, the
  `--splitOnly` and `Unassigned_Read_Type` descriptions, the option table) as the
  statement of intended behaviour; the same sentences are in the 2.0.1, 2.0.3 and
  2.1.1 tarballs' manuals.
- The GitHub history (`git log`, `git show 1f24de1 -- src/readSummary.c`): the
  read-type branch was removed with the 2.0.2 changes in one bulk commit; there is
  no commit message or manual change explaining it, which is why FC2 is an
  issue-first item.
- Matthew Rocklin's "Craft Minimal Bug Reports": each issue carries a
  self-contained script that writes a two-line GTF and a four-record SAM, runs one
  command, and prints got vs expected; `mcve_outputs.txt` is their output on
  `master`, 2.1.1, 2.0.3, 2.0.1 and the patched builds. Shrinking showed that FC1
  needs exactly one mapped non-split record with no mapped mate, and FC2 exactly
  one single-end record in a stranded run.

## Contents

| file | what |
|---|---|
| `issue-fc1-splitonly-singletons.md` | bug report: `--splitOnly` counts non-split singleton fragments in read-pair mode |
| `issue-fc2-read-type-filter.md` | question + bug report: the documented read-type filter was removed in 2.0.2; single-end reads counted as first reads under `-s 1/2` |
| `mcve_fc1_splitonly_singletons.py`, `mcve_fc2_read_type_stranded.py`, `mcve_outputs.txt` | the reproductions embedded in the issues and their outputs per version |
| `0001-featureCounts-apply-splitOnly-to-singleton-fragments.patch` | FC1 fix + helper + test case (`git am`-able on `55dc154`) |
| `0002-featureCounts-restore-the-read-type-filter-for-stran.patch` | FC2 fix + test case |
| `pr-bodies.md` | PR titles and bodies |

## Verification status of the patches

| patch | new test on unmodified `master` | full `test/featureCounts` suite with patch | harnesses with patch |
|---|---|---|---|
| 0001 (FC1) | `corner-SPLITONLY`: **FAILED** (8 vs expected 3) | 0 FAILED (38 corner + 12 across-gene/intron comparisons PASS) | `fc1_splitonly_pe_singletons.patched.out`: 0/1,000 singletons Assigned; random battery 74/75 sets unchanged, the `--splitOnly` set now follows the manual (`heldup_bruteforce_random.patched_fc1.out`) |
| 0002 (FC2) | `corner-READTYPE`: **FAILED** (6 vs expected 4) | 0 FAILED | `fc2_read_type_stranded.patched.out`: S = 300, AS = 0, Read_Type = 1,000 under `-s 2` (as 2.0.1); random battery: the 7 `-s 1/2` sets differ from the `master`-modelled reference only in the 26 single-end records now labelled `Unassigned_Read_Type` (`heldup_bruteforce_random.patched_fc2.out`), exactly as 2.0.1 does |

Unmodified `master`: 0 FAILED. There is no linter or formatter in the project;
the patches keep the file's tab indentation and brace style. Each applies with
`git apply --check` on `55dc154`; both together apply cleanly (they touch
different hunks of `process_line_buffer` and different lines of
`test_corner_cases.sh` — the second needs a three-way merge of that one-line
insertion or a manual line).

## Version scope (executed)

| finding | present | absent |
|---|---|---|
| FC1 | 2.0.1, 2.0.3, `master` (2.0.6), 2.1.1 | — |
| FC2 | 2.0.3, `master` (2.0.6), 2.1.1 (removed in 2.0.2, commit `1f24de1`) | 2.0.1 |

Rsubread (Bioconductor) shares the C code but was not executed (no CRAN/Bioconductor
route from this session; R 4.3.3 is installed, Rsubread is not).

## Order of operations

1. Read the open issues and recent closed ones of `ShiLab-Bioinformatics/subread`
   (who answers, response times); decide between GitHub, the Google Group and the
   Bioconductor support site.
2. FC2 first, as an issue asking whether the 2.0.2 removal of the read-type filter
   was intended; if the answer is "the manual is right", open the PR from patch
   0002; if "the code is right", offer a manual fix instead.
3. FC1 as an issue + PR from patch 0001 (or the PR alone if the maintainers prefer).
4. Record numbers and responses in `../README.md` and the top-level status table.
