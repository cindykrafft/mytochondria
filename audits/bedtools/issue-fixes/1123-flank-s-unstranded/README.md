# bedtools #1123 — `flank -s` produces no output for records without a `+`/`-` strand

_Prepared 2026-09-03 against `arq5x/bedtools2` **master** @ `614e9a5` (2026-06-10),
built with `make -j8` from a fresh `git clone --depth 1`. Nothing has been filed, pushed
or committed outside this directory; the fix branch lives in the session scratchpad._

## The issue

- **#1123** — "bedtools flank -s not work", opened 2025-04-18, open, 0 comments:
  https://github.com/arq5x/bedtools2/issues/1123
- Reporter's claim: with `bedtools flank -s -i tmp.bed -g PG.genome.bed -l 2000 -r 0`
  (v2.30.0) the command "does not generate output", while the same command without `-s`
  prints the left flank. The record shown is a 6-column BED with `.` score and `-` strand.
- The same symptom was reported in **#1057** ("Strandedness `-s` not working in flankBed,
  producing no output", 2023, closed as "[resolved]"; the input there was a 4-column BED
  with the strand in column 4).

## Diagnosis (`master` @ `614e9a5`)

`src/flankBed/flankBed.cpp:61-68`, `BedFlank::FlankBed()`:

```cpp
if ((_forceStrand == false) || (bedEntry.strand == "+"))
{
    AddFlank(bedEntry,  leftFlank, rightFlank);
}
else if ((_forceStrand == true) && (bedEntry.strand == "-" ))
{
    AddStrandedFlank(bedEntry,  leftFlank, rightFlank);
}
```

With `-s`, a record is flanked only if its column-6 strand is exactly `+` or `-`. Every
other record — a BED3/BED4/BED5 line (no strand column, `strand` is empty), or a `.`
strand — satisfies neither condition and is **silently dropped**. A strand-less file
therefore yields no output at all under `-s`, which is exactly the reporter's symptom.
`slop -s` handles the same situation by swapping only for `-`
(`src/slopBed/slopBed.cpp:86`, `should_swap = _forceStrand && bed.strand == "-"`), so a
strand-less record is treated as forward; `flank` is the odd one out.

The reporter's *exact* record (`chr1 35674 60016 Ponkan1g_000020 . -`, tab-delimited)
is flanked correctly under `-s` on master, and `flankBed.cpp` is byte-identical between
`v2.30.0`, `v2.31.1` and master (only help text in `flankBedMain.cpp` changed), so that
line as pasted does not reproduce; see the caveats.

## Fix (branch `fix/issue-1123-flank-s-unstranded`, patch `0001-*.patch`)

Dispatch on `-s` the way `slop` does: a `-` record goes through `AddStrandedFlank()`,
every other record through `AddFlank()`. `+`/`-` output is unchanged. One sentence added
to `docs/content/tools/flank.rst` under `-s`. No changelog entry: `docs/content/history.rst`
is written by hand at release time (see `../../upstream/README.md`).

```
 docs/content/tools/flank.rst |  2 +-
 src/flankBed/flankBed.cpp    | 11 +++++++----
 test/flank/dotstrand.bed     |  2 ++
 test/flank/nostrand.bed      |  1 +
 test/flank/test-flank.sh     | 33 +++++++++++++++++++++++++++++++++
```

`git apply --check` of the patch succeeds against a clean `master` checkout.

## Reproduction

`repro.sh` (synthetic data, `BT=/path/to/bedtools bash repro.sh`); outputs in
`repro.before.out` (master) and `repro.after.out` (fixed build). The `-s` runs on a
BED3 file, on a `.`-strand record, and on a BED4 file print nothing before the fix and
the forward flank after it; `+`/`-` records and the no-`-s` runs are identical before
and after.

```
== flank -i bed3.bed -l 5 -r 0            == flank -i bed3.bed -l 5 -r 0 -s
   chr1	95	100   (both)                     before: (nothing)   after: chr1	95	100
== flank -i dot.bed -l 5 -r 0 -s
   before: chr1	600	605	f2	0	-             after: + chr1	95	100	f1	0	.
```

## Tests

New cases in the project's own style (`test/flank/test-flank.sh`, `check obs exp`):

| test | input | command | expected |
|---|---|---|---|
| flank.t12 | `nostrand.bed` (BED3) | `-l 5 -r 0 -s` | `chr1 95 100` |
| flank.t13 | `nostrand.bed` | `-b 5 -s` | same two flanks as without `-s` |
| flank.t14 | `dotstrand.bed` (`.` and `-` records) | `-l 5 -r 0 -s` | `.` → left flank, `-` → right flank |

| run | result |
|---|---|
| `test/flank` on unmodified master (`tests.flank.before.out`) | t1–t11 ok, **t12, t13, t14 fail** (obs empty), exit 1 |
| `test/flank` with the fix (`tests.flank.after.out`) | 14/14 ok, exit 0 |
| full `make test` on unmodified master (`maketest.before.out`) | 31 tool suites pass, `negativecontrol` fails by design |
| full `make test` with the fix (`maketest.after.out`) | 31 tool suites pass, `negativecontrol` fails by design |

Linter/formatter: the project has none (no `.clang-format`, no lint step in
`.github/workflows/main.yml`); the change follows the surrounding indentation.

## Candidates considered

Read 100+ open issues (of 250 open) by title via `search_issues` (`repo:arq5x/bedtools2
is:open`, plus symptom and tool-name queries); bodies read for the ones below. Issue
**comments cannot be read from this session**, so "0 comments" is the only signal of
maintainer response. `search_pull_requests` (`repo:arq5x/bedtools2 flank strand`) finds
no open PR for `flank -s` (only the closed #777 for #738). #1142, #673, #1089 and the
audit's BT1–BT6 were skipped as instructed.

- **#1123 (chosen)** — reproducible on master for strand-less / `.` input; one-condition
  fix with an in-project precedent (`slop -s`); tests fail before, pass after.
- **#1111** `intersect -sorted -g` misses hits after a genome-file chromosome absent from
  one input — would be the highest-impact wrong result, but a minimal reconstruction
  (genome `chr1,MT,X,Y`; A lacking `MT`, B having it; `-wao`, `-s`, `-c`; 5-chromosome
  variant with gaps) gives the correct hits on master. Not reproducible from the body;
  the reporter's files are not available.
- **#1133** `intersect -wo -s -split` reports a BED12 hit that touches neither block —
  the two records from the body give **no** output on master (correct). Not reproducible.
- **#1073** `summary` "length incorrect if intervals overlap" — reproduced that
  `total_ivl_bp` sums overlapping intervals (200 for `0-100` + `50-150`); whether the
  column should count unique bases is a naming/design call for the maintainers.
- **#1114 / #1048** `unionbedg -header` — reproduced a smaller defect: without `-names`
  the header is only `chrom start end` while the rows carry one column per file
  (`multiinter -header` prints the file names). A separate one-line candidate.
- **#1085** `multiinter -header` "broken BED" — not reproduced on a two-file example.
- **#1103** `shift -p/-m`, `window` "strand broken" — the docs example is a 4-column BED
  with the strand in column 4, which bedtools does not read as a strand; a documentation
  issue rather than a code bug.

## Caveats

- The reporter's exact record works on master under `-s`, and `flankBed.cpp` has not
  changed since v2.30.0, so their failure was most likely a tab/column issue in the real
  file (the paste is space-separated). The patch fixes the reproducible form of the same
  symptom (no output under `-s` for strand-less or `.`-strand records, which is also
  #1057's case); the comment text says so.
- A 4-column BED whose 4th column is `+`/`-` (#1057, #1103 style) is still not read as
  stranded — bedtools takes the strand from column 6 only — so after the fix such a file
  is flanked as forward rather than dropped. That matches `slop -s` and the documented
  BED format; the maintainers might instead prefer a warning on stderr for records
  without a recognised strand under `-s`. Either is a two-line change on this branch.
- `history.rst` was left untouched per the project's release-time convention.

## Files

| file | what |
|---|---|
| `0001-flank-with-s-treat-records-without-a-strand-as-forwa.patch` | `git format-patch` of the one commit on `fix/issue-1123-flank-s-unstranded` over `614e9a5` |
| `repro.sh`, `repro.before.out`, `repro.after.out` | reproduction and its output on master / fixed build |
| `tests.flank.before.out`, `tests.flank.after.out` | `test/flank/test-flank.sh` on master / fixed build |
| `maketest.before.out`, `maketest.after.out` | full `make test` summaries |
| `pr-body.md` | PR title and body (no project template exists) |
| `comment.md` | comment for the #1123 thread |
