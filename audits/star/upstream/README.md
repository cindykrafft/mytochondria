# STAR upstream filing kit

_Default branch: **`master`** (there is no `develop`; PRs and the compare URL go against
`master`). Prepared 2026-09-10 against `alexdobin/STAR` `master` @ `b1edc12`, which is
also the tag `2.7.11b`, the latest release. **Nothing filed, nothing pushed, nothing
commented.** The fix is one commit, `aedf5db`, on the local branch
`fix/strandless-transcript-strand` of the audit clone, and `git am`-able from
`0001-Fix-strand-handling-for-GTF-features-with-undefined-.patch` against `b1edc12`
(`git apply --check` clean)._

Filing tier: **now** for ST1 — an internally inconsistent BAM record and a silent zero in
a count matrix, under default settings, on the current release and on every release the
cohort names. It is the only item in this kit; N1–N3 in the review are **held** (N1 and
N2 are documentation about a documented design; N3 is a regression the maintainers
already fixed in 2.7.10a and recorded in `CHANGES.md`). The filing cap is two unanswered
filings per repository, so if only one thing is sent it is ST1 — the issue first, with
the PR offered in its last line and opened once a maintainer responds. That order comes
from `CONTRIBUTING.md`, which routes questions to the mailing list and asks that bug
reports carry the reproduction; the tracker is past issue #2670 and has a single maintainer, so
an unsolicited PR is more likely to sit than an issue with a 40-line reproduction.

## AI-contribution policy check

The project's fork used by this audit, `github.com/cindykrafft/STAR`, could not be
resolved (`mcp__github__search_repositories` for `repo:cindykrafft/STAR` returns
"the listed users and repositories cannot be searched either because the resources do not
exist or you do not have permission to view them"), and `site/audits.json` in the audit
repository has no STAR entry yet, so there is no `upstream-declines-ai-contributions`
topic and no `declines_ai` flag to respect. `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`,
`README.md` and `RELEASEnotes.md` in `alexdobin/STAR` say nothing about AI-generated
contributions, and there is no pinned policy issue. The kit is therefore prepared
normally — but the lead should re-check the fork's topics before anything is sent, since
this session could not see the fork at all.

## What was read before preparing this

- **`CONTRIBUTING.md`** (the only contribution document in the tree). Shaped the kit:
  - *"Please do not file an issue to ask a question"* — questions go to the
    [rna-star Google group](https://groups.google.com/forum/#!forum/rna-star). ST1 is a
    bug report with a reproduction, not a question, so the tracker is the right channel.
  - *"check if you can reproduce the problem in the latest version of STAR and if the
    problem happens when you run with mostly default parameters"* — the MCVE runs on
    2.7.11b, the current release, and uses no non-default option except the ones the
    feature itself needs (`--quantMode TranscriptomeSAM`, the `--solo*` block); the
    issue records 2.7.10a and 2.7.9a as well.
  - *"Check the Log.out file for ERROR/WARNING/SOLUTION messages"* and *"Attach the
    Log.out file"* — the issue states that no run produces any such line, which is part
    of the point: the failure is silent.
  - *"Describe the exact steps ... the command you used ... copy/pasteable snippets ...
    the behavior you observed ... which behavior you expected"* and *"System
    information"* and *"Can you reliably reproduce the issue?"* — these are the headings
    of `issue-st1-strandless-transcript-strand.md`, in that order.
  - *Pull Requests*: clear title; state the purpose; *"Make sure that the default STAR
    behavior does not change"*; detailed code documentation and commit messages. The PR
    body answers the default-behaviour clause explicitly, the commit message explains
    each of the six changed conditions, and every changed line carries an inline comment.
- **No issue template, no PR template, no `.github/` directory at all** — the issue body
  is free-form markdown following the `CONTRIBUTING.md` bug-report order.
- **`CHANGES.md`**: entries under a `STAR <version> --- <date> ::: <summary>` heading with
  `* Issue #NNNN: Fixed …` / `* PR #NNNN: …` bullets. The patch adds a
  `STAR 2.7.11c --- unreleased` heading with one such bullet, `#NNNN` to be replaced with
  the issue number. `RELEASEnotes.md` is the older, coarser version of the same file and
  has not been updated since 2.7.x began; the patch does not touch it.
- **`CODE_OF_CONDUCT.md`**: Contributor Covenant 1.4; nothing that changes the kit.
- **Tests**: STAR has **no test suite and no CI** — `extras/tests/scripts/` contains three
  `awk` checkers for STARsolo `CellReads.stats` and nothing that runs them, and there is
  no `make test` target, no `.github/workflows/`, no `tox`/`ctest`/`meson`. So "run the
  project's own tests for the touched module with and without the patch" has no existing
  suite to run; the patch adds the first executable regression test in the tree, in the
  same `extras/tests/scripts/` directory and the same shell-script style as the `awk`
  checkers. Numbers:

  | build | `bash extras/tests/scripts/testStrandlessTranscript.sh <STAR>` | exit |
  |---|---|---|
  | `master` @ `b1edc12` (unpatched) | 2 FAIL, 0 PASS — transcriptome FLAGs `0`/`16` swapped between the `+` and `.` annotations; STARsolo `Gene`/`GeneFull`/`GeneFull_Ex50pAS` `4` with `+` and `0` with `.` | 1 |
  | `master` + `0001-…patch` | 0 FAIL, 2 PASS | 0 |

  The audit's own five harnesses were also re-run on the patched binary: the
  `st1_trsam_strandless_transcript` harness goes from "AFFECTED" to "unaffected"
  (`../verify/st1_trsam_strandless_transcript.patched.out`), and nothing else in the
  synthetic annotation moves.
- **Linters/formatters**: none in the tree (no `.clang-format`, no `.editorconfig`, no
  lint step anywhere). The patch matches the surrounding style — 4-space indent, `};`
  after blocks, trailing `//` comments — and compiles with `-Wall -Wextra` producing no
  new warning.

## Prior issues searched (tracker searched 2026-09-10, `mcp__github__search_issues`)

Five phrasings, none of them a report of this bug:

| phrasing | nearest results |
|---|---|
| "transcriptome BAM strand inverted for transcripts with undefined strand '.' in GTF" | #2679, #2020, #1990, #1922, #2024, #2253, #735, #2233 |
| "STARsolo genes with no strand get zero counts soloStrand Forward" | #2098, #2677, #711, #2076, #788, #1615, #2197, #1858 |
| "GTF strand column dot period unstranded annotation transcripts reverse complement RSEM" | #2679, #1922, #1705, #1880, #842, #1856 |
| "Aligned.toTranscriptome.out.bam wrong flag reverse strand sequence does not match transcript" | #735, #2020, #2588, #2024, #1990, #2211 |
| "custom GTF strand '.' no strand gene not counted GeneFull STARsolo zero UMI" | #2098, #2679, #2600, #898, #1557, #1380 |

The nearest is **#1922** ("mis-entry of strand information in gtf for ref building",
open, 5 comments, 2023-08-04): a user built a GTF from a BED file, lost the strand
information, recorded everything as `+`, and asks what STAR does in that case. It is the
same *situation* — a custom GTF whose strand column is not trustworthy — but not the same
*bug*: that user wrote `+` everywhere, which is exactly what this patch makes `.` behave
like, and the thread does not mention `.` or the transcriptome BAM's flag. **A new issue,
not a comment on #1922.** If the lead prefers to raise it on that thread instead, #1922's
5 comments must be read first (this environment cannot read comment bodies) and the text
re-cast as a comment.

Also noted while searching, not the same bug and not filed on: #2253 ("Missing reads in
Transcriptome BAM file when using `--quantMode TranscriptomeSAM`", 0 comments) and #735
("Mapped reads seemingly not reported in `.Aligned.toTranscriptome.out.bam`", 4 comments)
both concern reads *absent* from the transcriptome BAM, which is N1 in the review (the
default `ExtendSoftclip` drops reads whose junction overhang is too short to extend). N1
is a documented design choice and is held, but if the lead ever files it, those two
threads are where it belongs, as comments, after their comments have been read.

## Files

| file | what |
|---|---|
| `issue-st1-strandless-transcript-strand.md` | the issue text, `Title:` first line, `CONTRIBUTING.md` bug-report order |
| `mcve_st1_strandless_transcript.sh` | the MCVE from the issue, as a runnable script |
| `mcve_outputs.txt` | its output on 2.7.11b/`master`, 2.7.10a, 2.7.9a and the patched build |
| `0001-Fix-strand-handling-for-GTF-features-with-undefined-.patch` | the fix + `CHANGES.md` entry + the new regression test, `git am`-able onto `b1edc12` |
| `pr-bodies.md` | the PR body draft, `CONTRIBUTING.md` § Pull Requests order |

Compare URL once the branch is pushed to a fork:
`https://github.com/alexdobin/STAR/compare/master...<fork>:fix/strandless-transcript-strand`
