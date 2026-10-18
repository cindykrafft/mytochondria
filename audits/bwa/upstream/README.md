# BWA upstream filing kit

_Default branch: **`master`** (PRs go against it). Prepared 2026-10-18 against `lh3/bwa` `master`
@ `d82444c` (code identical to the v0.7.19 release, 2025-03-22). **Nothing filed.** The fix is a
single commit, `git am`-able from the patch here onto `d82444c`; it exists only in the session
scratchpad (branch `fix/mapq-coef-fac-float`, commit `9e57ba8`) and has not been pushed anywhere._

**Fork needed: lh3/bwa** (no fork under `cindykrafft` exists yet; `site/audits.json` has no BWA
entry, so the `upstream-declines-ai-contributions` topic cannot apply).

Filing tier (`../../TRIAGE.md`): **now** for BWA1 (default MAPQ on every release since 0.7.6;
MAPQ filters such as GATK's MQ ≥ 20 or `samtools view -q 20/30` decide which reads a paper
counts). BWA2 and BWA3 **held** (BWA2 changes no downstream number; BWA3 needs a same-strand
library). N1 and N2 held as notes.

## What was read before preparing this

- No `CONTRIBUTING.md`, no issue or PR template, no `.github/ISSUE_TEMPLATE`, no AI-contribution
  policy anywhere in the tree. Searched: `README.md`, `README-alt.md`, `NEWS.md`, `ChangeLog`,
  `code_of_conduct.md` (Contributor Covenant: issues, feature requests and pull requests are all
  welcome; maintainers may reject contributions), `.github/` (holds only `workflows/ci.yaml`).
- `README.md` "Seeking help": the man page, the bio-bwa-help mailing list, BioStar and SEQanswers.
  The GitHub tracker is in use (issues and PRs were merged on 2025-03-21/22 for 0.7.19).
- `README.md` note at the top (2026): "BWA-MEM has been replaced by minimap2 for long reads and
  will be replaced by minibwa for short reads. If you still prefer the exact legacy output of
  BWA-MEM, try BWA-MEM2 or the compatibility mode of BWA-MEM3." This means BWA is in maintenance
  and its output may be treated as frozen. BWA-MEM2 copies the same `int mapQ_coef_fac`
  (`bwa-mem2` @ `97978f9`, `src/bwamem.h:103`). So BWA1 goes as an **issue first**, offering
  either the one-line code fix or a sentence in `bwa.1`. The PR is opened only if the maintainer
  prefers the code change.
- `.github/workflows/ci.yaml`: `make` on ubuntu-latest, ubuntu-24.04-arm, macos-15-intel and
  macos-latest for every PR; there is no test suite. `make` was run on the fix (`test-runs.txt`).
- Prior threads: #213 (closed 2018, read in full) is the maintainer's long defence of MAPQ
  semantics against an ad-hoc change ("This thread is concluded."). The BWA1 text therefore
  leads with the type defect and its measurement, not with a request to change calibration.
  #164 (lh3: "There is no simple equation") and #61/#169 do not touch the factor. Full list in
  `dupcheck-2026-10-18.md`.
- `git log -S mapQ_coef_fac`: introduced in 623da05 (2013-09-06, "alternative way to estimate
  mapQ") with `int`. It became the default with len 50 in deb1959 (r418, 2013-11-02; 0.7.6). The
  field is unchanged in 0.7.12, 0.7.15, 0.7.17 and 0.7.19, all executed.

## Contents

| file | what |
|---|---|
| `issue-bwa1-mapq-coef-fac-truncated.md` | report: the declaration, the 40-60-bp scan (MAPQ 27 → 15 at 50 bp), the port, the calibration simulation, both remedies |
| `0001-Declare-mapQ_coef_fac-as-float-so-the-MAPQ-length-fa.patch` | BWA1 fix (`bwamem.h`, one token), commit 9e57ba8 on `fix/mapq-coef-fac-float` |
| `pr-bodies.md` | PR title and body (open only after a positive reply) |
| `test-runs.txt` | build on the fix branch; the harness runs on the patched build |
| `dupcheck-2026-10-18.md` | queries, threads read, verdicts |

## Verification status of the patch

| branch | commit | harness on the patched build | project tests |
|---|---|---|---|
| `fix/mapq-coef-fac-float` | `9e57ba8` | `../verify/m1_mapq.patched.out`: ln-50 port 158/158, length scan continuous; `../verify/m2_mapq_calibration.master_vs_patched.out`; s1/p1/c1/a1 byte-identical to master | `make` (CI's only step): OK, same warnings as master |

## Version scope (executed)

| finding | affected | unaffected |
|---|---|---|
| BWA1 | 0.7.12, 0.7.15, 0.7.17, 0.7.19/`master` | patched |
| BWA2 | 0.7.17, `master` | 0.7.12, 0.7.15 (no `MC` tag); `-Y` on every build |
| BWA3 | 0.7.12, 0.7.15, 0.7.17, `master` | FR/RF libraries |
| N1, N2 | 0.7.12, 0.7.15, 0.7.17, `master` | — |

## Order of operations

Two-filing cap: at most two open filings on `lh3/bwa` until a maintainer replies. Only one
filing is planned.

1. File the BWA1 issue from `issue-bwa1-mapq-coef-fac-truncated.md` (no prior thread to read
   first; #213 was read in full on 2026-10-18 and is not cited).
2. Fork `lh3/bwa` and push `fix/mapq-coef-fac-float` (apply the patch with `git am` on `master`).
   Open the PR (`pr-bodies.md` § PR 1, issue number in the first line) **only if** the maintainer
   says he wants the code change. If he prefers documentation, offer a `bwa.1` sentence instead.
   If he closes the issue, nothing further.
3. BWA2 and BWA3 stay held. After a positive reply, they could follow one at a time (BWA2 is a
   one-token fix, `add_cigar(opt, m, str, 0)`, verified in
   `../verify/c1_split_reads.bwa2-fix.out`).
4. Record the issue number and every maintainer response in `../README.md` and the top-level
   status table.
