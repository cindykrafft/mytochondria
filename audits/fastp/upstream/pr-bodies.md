# PR titles and bodies

fastp has no pull-request template, no CONTRIBUTING file and no changelog file
(release notes are written on the GitHub releases page), so these bodies follow
the shape of the merged PRs in the repository: what changed, why, and how it was
tested. Each PR is one commit on top of `master` @ `dce5c40`. Replace `#NNN`
with the issue number before opening.

---

### PR 1 — `fix/cut-window-trim-front` — "fix: --cut_front/--cut_tail must not drop a window of good bases after --trim_front1/--trim_tail1"

Fixes #NNN (#474).

`Filter::trimAndCut` stops the 5' scan on the first window whose mean quality
passes and then moves the cut to the end of that window. That is correct when a
window failed — windows overlap, so dropping the last failing window means
keeping from `s+w-1` — and the `if(s > 0)` guard is there to skip it when the
very first window already passes. The guard compares with the start of the
untrimmed read instead of `front`, the position where the scan started, so with
`--trim_front1 > 0` it is always true and `cut_window_size - 1` good bases are
dropped from every read. `if(t < l-1)` has the same problem on the 3' side.

Measured on a 60 nt read whose every base is Q40 (no window can fail):
`-f 5 --cut_front` produced 52 nt instead of 55, and 46 nt with `-W 10`;
`-t 5 --cut_tail` likewise. `--cut_right` is unaffected. On 20,000 random reads
(40–150 nt, Phred 2–40) `--cut_front -f 5` differed from the corrected rule on
11,509 reads; with the default filters and `-l 15` that is 1,624 reads and 6.9 %
of the surviving bases.

`Filter::test()` gains a 5' and a 3' case on an all-Q40 read; both fail without
this change ("cut_front with trim_front1=5 should keep 35 of 40 bases") and pass
with it. `./fastp test` is green, and the CI smoke test
(`./fastp -i testdata/R1.fq -o /dev/null`) runs.

**Behaviour change to flag in review:** reads become `cut_window_size - 1` bases
longer whenever `--cut_front`/`--cut_tail` is combined with
`--trim_front1`/`--trim_tail1`, so read counts and lengths in the reports move.

---

### PR 2 — `fix/known-adapter-truncation` — "fix: keep an auto-detected adapter that is longer than 60 bases"

Fixes #NNN.

`std::string::resize(n, c)` resizes to `n` and pads with `c`, so
`adapt.resize(0, 60)` in `main.cpp` empties the adapter instead of truncating it
to 60 characters. Since v0.26.0 the detector matches the built-in table first
(`Evaluator::checkKnownAdapters`) and returns entries at their full length; 139
of the 234 built-in adapters are longer than 60 nt. For those libraries fastp
prints the adapter it has just found, then reports "No adapter detected", trims
nothing, and drops the `adapter_cutting` section from the JSON report. The
families with no shorter built-in prefix to fall back on — the TruSeq Small RNA
RPI primers and the RNA PCR Primer index series, 85 entries — are the ones that
hit it.

This truncates to 60 characters as intended. `scripts/test_known_adapter_over60.sh`
is added in the style of `scripts/test_issue_697_stdout_merge.sh`: it makes
20,000 reads that read through into the 63 nt RPI1 adapter and requires that
they are trimmed. Without this change it fails with "only 0 of 20000 reads had
their adapter trimmed"; with it, 20,000 of 20,000. `./fastp test` is green.

---

### PR 3 — `fix/adapter-indel-offset` — "fix: search for a gapped adapter at the read offset, not only at the read start"

Fixes #NNN (#518).

The exact-match loop in `AdapterTrimmer::trimBySequence` compares the adapter
with the read at the current offset (`rdata + startOffset + pos`), but the two
loops added in v0.26.0 for one insertion and one deletion pass `rdata`, the
start of the read. For every `pos` up to `rlen-alen-1` the call is then
identical, so the loop is a single test of "does the read begin with the
adapter" and an adapter occurring at the 3' end with one indel — the case #518
reports — is never found: 0 of 200 such reads were trimmed, against 200 of 200
for the same reads without the indel.

Passing `rdata + pos` in both loops recovers them. On 5,000 random reads with
planted occurrences: 993 of 993 insertions and 967 of 967 deletions trimmed
(263 and 266 before), 1,049 of 1,049 substitutions and 978 of 978 exact matches
unchanged, and 0 of 1,013 adapter-free reads trimmed. `AdapterTrimmer::test()`
gains an insertion and a deletion case; both fail without this change.
`./fastp test` is green.

---

## Notes for the maintainer that go with the PRs

- The three branches touch three different files (`src/filter.cpp`,
  `src/main.cpp` + `scripts/`, `src/adaptertrimmer.cpp`); all three patches
  apply together cleanly on `dce5c40`.
- PR 1 and PR 3 change how many bases survive, so they will move the numbers in
  existing reports; PR 2 changes them only for libraries whose adapter is one of
  the >60 nt built-ins.
- The project has no linter configuration and no changelog file, so no formatting
  or release-note changes are included; the CI workflow's build and smoke test
  and `./fastp test` were run for every branch.
