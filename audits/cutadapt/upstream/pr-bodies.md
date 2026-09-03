# PR titles and bodies

Cutadapt has no pull-request template. `CONTRIBUTING.rst` asks for one topic per
PR, tests, a changelog entry where appropriate, black formatting and Google-style
docstrings; each PR below references its issue (to be opened first from the
`issue-ca*.md` texts). Replace `#NNN` with the issue number and add `:issue:\`NNN\`:`
to the changelog line before opening.

## PR 1 (from `0001-Honour-an-absolute-number-of-errors-e-N-for-every-ad.patch`)

**Title:** Honour an absolute number of errors (-e N) for every adapter length

Fixes #NNN.

With `-e N` (N ≥ 1) the number of errors becomes the rate `N / n`, and the aligner
accepts an alignment over `L` adapter characters if `errors <= L * rate`. For some
`n` the product `n * (N / n)` is slightly below `N` in floating point
(`49 * (1 / 49) == 0.9999999999999999`), so `-e 1` allowed no errors for a 49 nt
adapter and `-e 2` only one for a 98 nt adapter; the same floor was applied in
`PrefixComparer`, in `AdapterIndex` and in the k-mer heuristic.

This adds a 1e-9 tolerance to every `length * rate` product through one helper
(`align.max_errors_for_length`) and a `DEF` constant in `_align.pyx`, plus tests
in `test_align.py` and `test_adapters.py` that fail without the change. If you
would rather keep exact integer arithmetic (carry `N` and `n` into the aligner and
compare `errors * n <= L * N`), I am happy to rework it.

Changelog entry included under "development version".

## PR 2 (from `0002-Make-max-ee-and-max-aer-honour-quality-base.patch`)

**Title:** Make --max-ee and --max-aer honour --quality-base

Fixes #NNN.

`TooManyExpectedErrors` and `TooHighAverageErrorRate` called `expected_errors()`
with the default base 33 regardless of `--quality-base`, so on Phred+64 data every
quality was read 31 too high and the filters never discarded anything. This passes
the quality base through (as `-q` and `--nextseq-trim` already do), with two tests
in `test_predicates.py` that fail without the change. Changelog entry included.

## PR 3 (from `0003-Choose-the-best-adapter-by-alignment-score-also-when.patch`)

**Title:** Choose the best adapter by alignment score also when using an index

Fixes #NNN.

`AdapterIndex` ranked candidates by number of matching bases while
`MultipleAdapters.match_to` (and therefore `--no-index`) ranks by the Cutadapt 4
alignment score, so a read could be assigned to different barcodes depending on
whether an index was built (an 11 nt barcode matching exactly lost against a 12 nt
barcode matching with an insertion). The index also stored the match count in
`Match.score`.

The index now stores the alignment score (computed from errors, matches and the
two lengths), ranks and detects ambiguity by it, and stops the multi-length search
by score. The 5.0 rule of not assigning ambiguous reads is unchanged, but the set
of ambiguous strings can change, which the changelog entry says. Two tests added;
they fail without the change. Opened after discussion in #NNN as this changes
demultiplexing results.

## PR 4 (from `0004-Fix-k-mer-heuristic-missing-anchored-adapters-with-a.patch`)

**Title:** Fix k-mer heuristic missing anchored adapters with an inserted base

Fixes #NNN.

The search window of each partial-overlap class of the k-mer heuristic is exactly
as long as the class's longest adapter prefix, so an occurrence with an inserted
base has one chunk shifted out of the window and the other broken; anchored and
non-internal adapters have no internal search set to fall back on and lost ~40 %
of such reads whenever exactly one error was allowed. Each window is now widened
by the class's number of allowed errors (one line); the expected windows in
`test_kmer_heuristic.py` change accordingly and three tests in `test_adapters.py`
cover `^ADAPTER`, `ADAPTER$`, `XADAPTER` and `ADAPTERX` with an insertion (they fail
without the change). Changelog entry included.

## Notes for the maintainer that go with the PRs

- The four patches are independent and each adds the same "development version"
  heading to `CHANGES.rst`; PR 3 and PR 4 both append tests to the end of
  `tests/test_adapters.py`. Applying more than one needs a trivial merge of those
  two hunks (all code hunks apply together cleanly, checked with `git apply`).
- Full test suite: 704 passed on unmodified `main`; 708 / 706 / 706 / 707 with
  PR 1 / 2 / 3 / 4. `black --check` (22.3.0, as in `tox.ini`) and `flake8` pass on
  every changed file.
