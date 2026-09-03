# Component: deepTools coverage, comparison, matrix and summary core (`master` @ `ea0f68bb`, 2025-01-20, version 3.5.6)

Read in full on `deeptools/deepTools` `master` at `ea0f68bb4a1587d713dacb3791861308751ef7d0`
(the `3.5.6` tag; PyPI's latest release, 3.5.6, is this commit, so "master" and "latest
release" are the same code below; the remote has no `develop` branch — the last one was
merged as PR #1356 and deleted — and a `4.0.0` branch with a Rust backend that was not
audited): `countReadsPerBin.py` (1,033 lines), `getScaleFactor.py` (305),
`bamCoverage.py` (416), `bamCompare.py` (314), `getRatio.py` (82), `writeBedGraph.py`
(354), `writeBedGraph_bam_and_bw.py` (239), `SES_scaleFactor.py` (195), `utilities.py`
(390), `mapReduce.py` (263), `heatmapper.py` (1,372), `computeMatrix.py` (429),
`sumCoveragePerBin.py` (240), `plotFingerprint.py` (484), `getScorePerBigWigBin.py`
(322), `multiBamSummary.py` (294), `multiBigwigSummary.py` (281), `correlation.py`
(706), `plotPCA.py` (200), `getFragmentAndReadSize.py` (166), `bamPEFragmentSize.py`
(369), `plotCoverage.py` (344), `estimateReadFiltering.py` (376), the counting half of
`plotEnrichment.py`, the summary-statistic lines of `plotProfile.py`/`plotHeatmap.py`,
the option help in `parserCommon.py`, and the GC-bias core of `computeGCBias.py` /
`correctGCBias.py` (read, not executed; see "Not audited").

Every suspicion was **executed on the shipped code**: master installed in editable mode
into a Python 3.12 venv (`bamCoverage --version` = 3.5.6, numpy 2.5.2, pysam 0.24.0,
pyBigWig 0.3.25), harnesses in `../verify/` with captured `.out` files, synthetic BAM
and bigWig files written with pysam/pyBigWig from known fragment lists, and numpy/scipy
closed forms as the reference. Every confirmed finding was also run on the 3.5.1 wheel
and the 3.3.1 sdist from PyPI (the cohort's two most-cited versions; `.v3.5.1.out`,
`.v3.3.1.out`).

Cohort exposure numbers are lower bounds from the survey cache (see `../README.md`).

## Findings

### DT1 — CONFIRMED on master (= 3.5.6), 3.5.1 and 3.3.1: `bamCompare --skipZeroOverZero` shifts the coordinates of every bin after a skipped bin

**Code.** `writeBedGraph.py:246-274` (`WriteBedGraph.writeBedGraph_worker`): the
run-length encoder derives each interval's coordinates from the previous interval's
`writeEnd`; a bin skipped by

```python
if self.skipZeroOverZero and np.sum(tileCoverage) == 0:
    continue
```

neither advances `writeEnd` nor resets `previous_value`, so the next written bin is
placed one bin too far left, and so is everything after it in the chunk; if its value
equals the previous one it is merged into the run, and the skipped bin is *written*
with that value. The sibling implementation for bigWig input
(`writeBedGraph_bam_and_bw.py:100-102`, used by bigwigCompare) resets
`previousValue = None` on the skip and is correct.

**Verified** (`../verify/dt1_skipzerooverzero_coordinates.py`; two BAMs on a 20-kb
chromosome, 50-bp bins, 206 of 400 bins zero in both files):

| run | bins with a wrong value | bins with a value where the output should be empty |
|---|---|---|
| default (no skip) | 0 of 400 | 0 |
| `--skipZeroOverZero --operation log2` | **375 of 400** | 196 |
| `--skipZeroOverZero --operation subtract` | **372 of 400** | 196 |
| bigwigCompare `--skipZeroOverZero` on the same data | 4 of 400 (N6, a different, minor defect) | — |

Introduced with the option (commit `6f68c67a`, 2019-04-01, first in 3.2.1). The
project's own `test_bam_compare_ZoverZ` only has a *leading* zero bin, which the
`previous_value is None` branch handles, so it passes. **Upstream already knows:**
issues #1108 (2021-12-04) and #1130 (2022-03-22) report exactly this with IGV
screenshots; both are open and unanswered. Fix: flush the run and reset on the skip
(`../upstream/0001-*.patch`, with a test that has an interior zero bin).

### DT2 — CONFIRMED on master, 3.5.1 and 3.3.1: `plotPCA --log2` has no effect; `--rowCenter` has no effect unless `--ntop 0` (or fewer rows than `--ntop`)

**Code.** `correlation.py:606-629` (`Correlation.plot_pca`):

```python
m = self.matrix
...
if self.ntop > 0 and m.shape[0] > self.ntop:
    m = m[np.argpartition(rvs, -self.ntop)[-self.ntop:], :]     # a copy
if self.log2:
    self.matrix = np.log2(self.matrix + 0.01)                     # rebinds self.matrix, not m
if self.rowCenter and not self.transpose:
    _ = self.matrix.mean(axis=1)
    self.matrix -= _[:, None]                                     # in place on self.matrix
...
m2 = (m - np.mean(m, axis=0))                                      # the SVD input is m
```

The SVD input `m` never sees the log2 transform; it sees the row centring only when it
is the same object as `self.matrix` (no `--ntop` copy, default `--ntop` is 1000 so any
genome-wide matrix is copied) and `--log2` is off (the rebind breaks the aliasing).

**Verified** (`../verify/dt2_plotpca_log2_rowcenter.py`; 4,000 bins × 4 samples with a
strong per-bin baseline; loadings from `--outFileNameData` compared up to sign with a
numpy port of the documented pipeline):

| option set | equals the no-option output? | equals its own reference? |
|---|---|---|
| `--log2` | **True** | False |
| `--rowCenter` | **True** | False |
| `--ntop 0 --log2` | **True** | False |
| `--ntop 0 --rowCenter` | False | True |
| `--ntop 0 --log2 --rowCenter` | **True** | False |
| `--transpose --log2` | **True** | False |

The default and `--transpose` outputs equal the numpy reference (eigenvalues to 0.0).
PC1 loadings with `--log2` are `[0.4981 0.4974 0.5019 0.5026]` (identical to no
option) where the reference gives `[0.5022 0.4981 0.5013 0.4985]`; with `--rowCenter`
the reference is `[-0.5844 -0.5517 -0.1061 0.5855]`. Introduced with the options
(commit `ad8ef44e`, 2019-02-15, first in 3.2.0). Not previously reported (tracker
searched; nearest #1215 asks for normalisation in plotPCA). An integer matrix makes
`--rowCenter` crash instead (`UFuncOutputCastingError` on the in-place subtraction;
`../upstream/mcve_outputs.txt` first run), a side effect of the same lines. Fix:
transform `m` (`../upstream/0002-*.patch`, with a test against the numpy reference).

### DT3 — CONFIRMED on master, 3.5.1 and 3.3.1: `plotCorrelation --removeOutliers` scales by the median of |x|, not by the median absolute deviation

**Code.** `correlation.py:117-119` (`Correlation.get_outlier_indices`):

```python
median = np.median(data)
b_value = 1.4826  # value set for a normal distribution
mad = b_value * np.median(np.abs(data))
```

The docstring cites Iglewicz & Hoaglin (1993) and the `--removeOutliers` help says
"median absolute deviation (MAD) method applying a threshold of 200"; the MAD is
`median(|x − median|)`, and `median(|x|)` is the median itself for counts. A bin is
therefore flagged only when `|x − median| > 200 × 1.4826 × median`, about 300 times
the typical count.

**Verified** (`../verify/dt3_removeoutliers_mad.py`; 5,000 Poisson(100) bins in three
samples plus 25 planted bins of ~4,000 in every sample):

| | threshold on \|x − median\| | bins flagged (column 0) | Pearson off-diagonals | bins removed by plotCorrelation |
|---|---|---|---|---|
| documented rule (numpy) | 2,076 | 25 | −0.0023, 0.0008, 0.0163 | 25 |
| shipped `get_outlier_indices` | 29,652 | **0** | 0.9984, 0.9983, 0.9985 | **0** |

The Pearson correlation the option exists to protect ("Bins with abnormally high reads
counts artificially increase pearson correlation") is 0.998 with the option and
≈ 0 without the hot bins. Dates from the pep8 pass of 2015-12-09 (`7cf1bec3`, 2.0.0).
Not previously reported (nearest #9, the 2013 request for the option, and #1406).
One-line fix (`../upstream/0003-*.patch`).

### DT4 — CONFIRMED on master, 3.5.1 and 3.3.1: `bamCoverage --MNase` counts four bases, off centre, for odd fragment lengths

**Code.** `bamCoverage.py:405-420` (`CenterFragment.get_fragment_from_read`):

```python
if read.tlen % 2 == 0:
    fragment_start = read.pos + read.tlen / 2 - 1
    fragment_end = fragment_start + 2
else:
    fragment_start = read.pos + read.tlen / 2 - 1
    fragment_end = fragment_start + 3
```

`/` is true division under Python 3, so for odd TLEN the start is a half-integer;
`countReadsPerBin.get_coverage_of_region:697-698` floors the start bin and ceils the end
bin, and with the recommended `--binSize 1` the window `[x.5, x.5+3)` covers four bins.
Under Python 2 (`2c44b2c5`, 2015-12-14) the same expression was an integer division and
gave the documented three central bases.

**Verified** (`../verify/dt4_mnase_center.py`): six proper pairs of lengths 149, 150,
151, 200, 131, 199 — the two even ones give the two central bases; all four odd ones
give four bases, the centre base plus one to its left and two to its right (e.g.
fragment 100–249: 173–176 instead of 173–175). **Upstream already knows:** #1118
(2022-01-27, "taking four nucleotides instead of three", with a BAM attached) is open
and unanswered. Fix: `//` (`../upstream/0004-*.patch`, with a test on the shipped
`test_paired2.bam`, whose 147- and 154-bp pairs cover both cases).

### DT5 — CONFIRMED on master, 3.5.1 and 3.3.1 (implementation contradicts the documented definition): `--normalizeUsing BPM` writes the CPM track

**Code.** `getScaleFactor.py:284-292`:

```python
tile_len_in_kb = float(args.binSize) / 1000
tpm_scaleFactor = (bam_mapped / tile_len_in_kb) / 1e6
scale_factor *= 1 / (tpm_scaleFactor * tile_len_in_kb)
```

which is `1e6 / bam_mapped`, the CPM factor (`:278-279`). The `--normalizeUsing` help
defines "BPM (per bin) = number of reads per bin / sum of all reads per bin (in
millions)" and "same as TPM in RNA-seq". A read is counted in every bin it overlaps
(`get_coverage_of_region:697-705`), so the sum of all reads per bin is the number of
mapped reads times the mean number of bins a read touches, and the documented values
sum to 1e6 over the genome. The commented-out `# sampled_bins_sum = getSampledSum(args.bam)`
on line 288 is the remnant of that sum (commit `2fbfaf26`, 2017-11-21, 3.0.0:
"implmented BPM norm, not tested for accuracy").

**Verified** (`../verify/dt5_bpm_equals_cpm.py`): CPM and BPM bigWigs are bit-for-bit
identical; with 100-bp reads and 50-bp bins each read touches 2.98 bins, the BPM
track sums to 2,980,650 (documented: 1e6) and every emitted value is 2.981 × the
documented one; with `--extendReads 300` the factor is 6.979. RPKM = CPM / (bin
length in kb) as documented. Whether this is a code bug or a documentation bug is the
maintainers' call; either way the number a user gets under "BPM" is not the one the
help text defines, and 5 cohort papers name BPM. No patch: the issue text offers both
fixes (`../upstream/issue-dt5-bpm-is-cpm.md`).

### DT6 — CONFIRMED on master, 3.5.1 and 3.3.1 (small, at chunk edges): `--smoothLength` windows are truncated at every multiprocessing chunk boundary

**Code.** `writeBedGraph.py:238-243`: the smoothing window is taken from the chunk's
own coverage vector, `getSmoothRange(tileIndex, binLength, smoothLength, coverage.shape[0])`,
so bins within half a window of a chunk edge average over a one-sided window. Chunk
edges fall every `min(5e6, 2e6 / (mapped reads per bp × files))` bases rounded to the
bin size (`writeBedGraph.py:337-339`), or every ≤ 1e6 bases with `--region`
(`mapReduce.getUserRegion`). The output therefore depends on the chunking.

**Verified** (`../verify/dt6_smoothlength_chunk_edges.py`; 3-Mb chromosome, 50-bp
bins, `--smoothLength 250`): with `--region chr1:0:3000000` (1-Mb chunks) 8 of 60,000
bins differ from a chromosome-wide sliding mean — the four bins at each of 1,000,000
and 2,000,000 (e.g. bin at 1,000,000: 1.3333 vs 2.8000); every other bin agrees to
1e-6; the genome-wide run on the same file is a single chunk and agrees everywhere.
On a human-sized genome at typical depth the chunk length is 5 Mb, so ~600 boundaries
× (window − 1) bins carry a one-sided average. No patch (the fix needs overlapping
chunk reads); issue text only.

### DT7 — CONFIRMED on master, 3.5.1 and 3.3.1: `--ignoreDuplicates` alone leaves the duplicates in the normalisation denominator

**Code.** `getScaleFactor.py:126-135` (`fraction_kept`):

```python
if (not args.minMappingQuality or args.minMappingQuality == 0) and \
   (not args.samFlagInclude or args.samFlagInclude == 0) and \
   (not args.samFlagExclude or args.samFlagExclude == 0) and \
   (not args.minFragmentLength or args.minFragmentLength == 0) and \
   (not args.maxFragmentLength or args.maxFragmentLength == 0):
    ...
        return 1.0
```

The early return does not look at `args.ignoreDuplicates`, although the function's
docstring lists it among the filters it accounts for and `getFractionKept_worker:62-79`
does count duplicates once the sampler runs. `--exactScaling` is applied after the
early return (`:149`) and cannot help. The per-bin counts are deduplicated
(`get_coverage_of_region:653-669`) but the "number of mapped reads" that CPM, RPKM,
RPGC and BPM divide by (`get_scale_factor`) and that `bamCompare --scaleFactorsMethod
readCount` uses (`bamCompare.py:215-223`) is the pre-deduplication count — unless any
other filter is set, in which case it is deduplicated.

**Verified** (`../verify/dt7_ignoreduplicates_scaling.py`; sample A 9,994 reads of
which 40.4 % exact duplicates, sample B 6,000 with none; all reads MAPQ 30):

| bamCoverage on A, `--normalizeUsing CPM` | scale factor | 1e6/mapped used | track = dedup counts × 1e6 / dedup mapped? |
|---|---|---|---|
| `--ignoreDuplicates` | 100.06 | 9,994 | **no** (40 % low) |
| `--ignoreDuplicates --exactScaling` | 100.06 | 9,994 | **no** |
| `--ignoreDuplicates --minMappingQuality 1` | 168.04 | 5,951 | yes |

bamCompare readCount factors A:B are `[0.6004, 1]` with `--ignoreDuplicates` alone and
`[0.9998, 1]` once a no-op MAPQ filter is added; the deduplicated depths are equal, so
the second is right. Between two samples with different duplication rates the
comparison is biased by the ratio of their duplicate fractions. Present since the
sampler was written (`d770792d`, 2017-09-08, 3.0.0). Not previously reported (the
2016 issue #309 led to `fraction_kept`; #5 is the 2013 bamCorrelate bug). Thirteen
cohort papers name `--ignoreDuplicates` and 18 `--normalizeUsing`. One-line fix
(`../upstream/0005-*.patch`).

### DT8 — CONFIRMED on master, 3.5.1 and 3.3.1: `multiBigwigSummary` reports zoom-level approximations, off by up to several-fold next to peaks at the default 10-kb bins

**Code.** `getScorePerBigWigBin.py:107`: `score = bwh.stats(chrom, exon[0], exon[1])`
— pyBigWig's `stats()` with its default `exact=False`, which answers from the bigWig's
zoom level whose reduction span fits the query. On the run-length-encoded tracks
bamCoverage writes (variable-length intervals that straddle the zoom records) those
summaries are not the mean of the values inside the bin
(`../verify/dt8b_zoom_mechanism.py`: the same intervals rewritten with pyBigWig in one
`addEntries` call, in calls of 1,000, or with the default zoom levels give identical
errors, so it is not deepTools' writer; a track of 50-bp aligned steps with one peak
gives a median of 0.38 % and 10 % at the peak bin; a track whose only zoom span exceeds
the bin size is exact). Every other bigWig consumer in deepTools
reads the exact per-base values (`heatmapper.py:719` `bigwig.values`,
`writeBedGraph_bam_and_bw.py:25`, `bigwigAverage`).

**Verified** (`../verify/dt8_multibigwigsummary_zoom.py`; a bamCoverage track (50-bp
bins) from 300,000 reads with 150 peaks on a 2-Mb chromosome; the file's zoom spans are
944 and 3,776 bp; reference = numpy `nanmean` of `bw.values()`, which
`stats(exact=True)` matches to 1e-6):

| bins | \|reported − exact\| / exact: median | 95th pct | max | bins off by > 1 % |
|---|---|---|---|---|
| 10,000 bp (default) | 0.034 | 0.72 | **2.45** | 144 of 200 |
| 5,000 bp | 0.009 | 0.13 | 1.59 | 189 of 400 |
| 2,000 bp | 0.025 | 0.32 | **4.21** | 761 of 1,000 |
| 1,000 bp, and BED-file regions of 200–1,500 bp | 0 | 0 | 0 | 0 (no zoom level fits; exact path) |

The worst bins are those next to a peak: e.g. bin 1,850,000–1,860,000 reported 14.75,
exact 5.85, with the neighbouring 10 kb at 15.9 and 37.5. Two replicate tracks give
Pearson 0.9539 from the reported 10-kb values and 0.9990 from the exact means
(Spearman 0.913 vs 0.909); at 2 kb, 0.9920 vs 0.9988. The existing project test
`test_multiBigwigSummary_gtf` carries an expected value that is itself a zoom summary
(27.3125 for the second transcript; exact 27.8067), while its `--metagene` twin is
exact. Not previously reported (nearest #1296, #1270, #1139 report
unexplained disagreements between bigWig summaries and other views). One-word fix
(`exact=True`, `../upstream/0006-*.patch`) at a speed cost; 3 cohort papers name
multiBigwigSummary, 2 plotCorrelation on bigWigs cannot be told apart from the cache.

### DT9 — CONFIRMED on master, 3.5.1 and 3.3.1 (latent: only when the sampling step equals `--binSize`): `plotFingerprint` credits a fragment's last bin with a whole tile

**Code.** `sumCoveragePerBin.py:169-199`: `eIdx` is the *ceiling* bin of the fragment
end; the loop `while _ < eIdx: coverages[_] += tileSize` adds a full tile to every bin
up to `eIdx − 1`, which is the bin the fragment ends in; the "last bin" branch then
adds `fragmentEnd − (reg[0] + eIdx × tileSize)`, which is ≤ 0 by construction and is
clamped to 0. The path is only taken for a multi-bin region, i.e. when
`countReadsPerBin.count_reads_in_region:483-484` passes one `(start, end, binLength)`
region because `stepSize == binLength` — `--numberOfSamples` = genome length /
`--binSize`, or any `--region` with that ratio. With the default `-n 500000` the step
differs from the bin size and each bin is its own 2-tuple region, where the code is
exact.

**Verified** (`../verify/heldup_fingerprint.py`; 500-kb chromosome, 500-bp bins):
`-n 2000` (step 250): all 1,999 bin sums equal the per-base sums; `-n 1000` (step 500 =
bin): 560 of 1,000 bins over-counted, sum reported / sum exact 1.939 (chip) and 1.918
(input), mean excess 1,677.5 per over-counted bin (a 50-bp read ending inside a bin
credits it with 500). The AUC/elbow/JSD/CHANCE formulas applied to those (wrong) counts
still equal the independent formulas, so the metrics silently inherit the distortion.
Patch replaces the three-part bookkeeping with the per-bin overlap
(`../upstream/0007-*.patch`).

## Notes (design choices, documentation, small deviations; each executed unless marked)

- **N1 — multiBamSummary chunk boundaries** (`countReadsPerBin.py:299`, chunk length
  not rounded to the bin size, unlike `writeBedGraph.py:339`): a chunk edge inside a
  bin yields one short bin and restarts the grid (issue #1030, open). Shown with
  `--genomeChunkSize 62901`: 4 of 201 bins are not 1,000 bp
  (`../verify/note_misc.out`). The default chunk is only shorter than a chromosome for
  deep data (1e7 bp here), so it is rare; a partial bin then enters the correlation
  as if it were a full one.
- **N2 — `computeMatrix --skipZeros`** removes rows whose *mean* is 0
  (`heatmapper.py:1346-1349`), so a log2-ratio row of +1/−1 values is dropped with the
  all-zero rows (`note_misc.out`, `r_cancel`). Design, undocumented.
- **N3 — SES scale factors ignore the read filters**: `SES_scaleFactor.py:92-99`
  counts unfiltered reads, so `--scaleFactorsMethod SES` gives the same factors
  (0.98646, 1) with and without `--minMappingQuality 10` when the filter halves one
  sample; `readCount` accounts for it. The 0.8 × max-difference rank
  (`SES_scaleFactor.py:129`) is a documented departure from Diaz et al. Design.
- **N4 — `--nanAfterEnd` on a region shorter than a bin** drops its bases (padding is
  rounded to whole bins, `heatmapper.py:517-526`); design at bin granularity.
- **N5 — synthetic JSD index shift**: `plotFingerprint.py:252` places the Poisson mass
  for value *k* at index *k − 1*; measured effect 0.524959 vs 0.524968
  (`heldup_fingerprint.out`), negligible for λ of hundreds.
- **N6 — bigwigCompare drops a trailing run whose value is exactly 0**
  (`writeBedGraph_bam_and_bw.py:135`, `if previousValue and ...`): the four wrong bins
  in DT1's bigwigCompare control and `note_misc.out` (`[(0, 1000, 1.0)]`, expected a
  second interval `(1000, 2000, 0.0)`). Affects `--operation subtract`/`log2` output
  where a chunk ends in equal signal; not in the focus list, recorded for the issue.
- **N7 — `--ignoreForNormalization`** still writes the ignored chromosome, scaled by
  the factor from the other chromosomes (documented; `note_misc.out`).
- **N8 — `--exactScaling` is not exact**: `getFractionKept_worker:34` fetches reads
  overlapping each 50-kb window, so reads spanning a window edge are counted twice;
  the filtered fraction differs from the true one by 3e-5 (MAPQ) to 2e-4 (strand)
  relative (`heldup_bamcoverage_normalisation.out`). Negligible; the help promises
  "the exact number".
- **N9 — bedGraph/bigWig values carry 6 significant digits** (`writeBedGraph.py:235`,
  `{:g}`), a ≤ 5e-6 relative rounding of every normalised value.
- **N10 — computeMatrix conventions** (all held up once ported): '−'-strand regions
  are partitioned from the genomic left and reversed (`heatmapper.py:545-546`), so bin
  boundaries differ by ≤ 1 bp from a 5'→3' partition when the length is not a multiple
  of the bin count; `--referencePoint center` is `start + len // 2` on both strands
  (`chopRegionsFromMiddle:85`); non-integer bin widths use `np.linspace(valStart, …,
  dtype=int)` with the cumulative offset, so a boundary can land one base off between
  zones.
- **N11 — `--rowCenter` on an integer matrix crashes** (in-place float subtraction on
  int64, `correlation.py:623`); resolved by the DT2 patch as a side effect.

Two own suspicions were withdrawn by execution: that plotFingerprint's default path
over-counts (it uses one 2-tuple region per bin and is exact, `heldup_fingerprint.out`),
and that `--ignoreForNormalization` drops the ignored chromosome from the output (N7).

## What held up (executed, not just read)

- **bamCoverage** (`heldup_bamcoverage_normalisation.out`): raw counts = fragments
  overlapping each bin, exactly; `--scaleFactor`; CPM, RPKM and RPGC equal their
  documented closed forms to the 6-digit formatting (≤ 4e-6); `--minMappingQuality`,
  `--samFlagExclude`, `--exactScaling` denominators within 2e-4 of the true filtered
  counts (N8); `--skipNAs`; paired-end without extension (each mate a read); `--extendReads`
  (each fragment counted once per mate, i.e. twice, as documented), RPGC on it with the
  median fragment length, `--centerReads` (a read-length window at the fragment centre,
  twice), `--minFragmentLength/--maxFragmentLength`, `--samFlagInclude 64` (fragments
  once) and its CPM denominator.
- **bamCompare** (`heldup_bamcompare.out`): readCount factors `min(n1,n2)/n`; every
  `--operation` (log2, ratio, subtract, add, mean, reciprocal_ratio, first, second) with
  the default pseudocount and with `--pseudocount 0.5 2`; `--pseudocount 0` (0/0 → NaN,
  x/0 → inf, as coded); `--scaleFactors a:b`; `--scaleFactorsMethod None` with CPM,
  RPKM and None; SES factors (0.99, 1) on two samples with equal background depth and
  a 50 % peak excess in one (readCount gives 0.667, 1), i.e. SES recovers the
  background ratio as intended.
- **computeMatrix** (`heldup_computematrix.out`): reference-point TSS with
  `--averageTypeBins` mean/median/max/sum/std, `--missingDataAsZero`, TES, center,
  `--nanAfterEnd`; scale-regions with `-b/-a`, median bins, `--unscaled5prime/3prime`,
  `-b 0 -a 0 --missingDataAsZero`; both strands, regions off both chromosome ends,
  regions shorter than the body bins; all equal the port to 0.0 under the conventions
  in N10. **plotProfile `--averageType`** mean/median/max/min/sum/std equal numpy over
  the non-NaN rows; **plotHeatmap `--outFileNameMatrix`** equals the matrix.
- **multiBamSummary** (`heldup_summaries.out`): bins and BED-file counts, consecutive
  1-kb bins in `--outRawCounts`, labels; `--scalingFactors` = 1 / DESeq2 median-of-ratios
  size factors (hand-written rule), and `estimateSizeFactors` likewise.
- **plotCorrelation**: Pearson = `numpy.corrcoef`, Spearman = `scipy.stats.spearmanr`
  (4 d.p. file), `--skipZeros` drops all-zero rows only, rows with a NaN in any sample
  are dropped before Pearson (as the warning says).
- **plotPCA** default and `--transpose` equal the numpy SVD pipeline (loadings to 1e-6,
  eigenvalues to 0.0) — DT2 concerns only `--log2`/`--rowCenter`.
- **multiBigwigSummary BED-file** on peak-sized regions and 1-kb bins are exact (DT8
  concerns bins for which a zoom level fits).
- **bamPEFragmentSize `--table`**: n, min, quartiles, median, mean, max, std (ddof 0),
  MAD, 10th–99th percentiles all equal numpy on the proper pairs.
- **plotCoverage** sampled per-base mean/std and `--outCoverageMetrics` percentages
  equal numpy on the same positions; **estimateReadFiltering** totals and per-filter
  counts; **plotEnrichment** feature counts, totals and percentages.
- **plotFingerprint** (`heldup_fingerprint.out`, default path): per-bin sums exact;
  AUC, X-intercept, elbow, JS distance (independent implementation of the documented
  construction to 1e-6), CHANCE % genome enriched and differential enrichment, and the
  synthetic JSD (to 1e-5, N5).
- **bamCoverage `--MNase` even fragments**, `--Offset`-free paths, `--region` handling
  and the bedGraph run-length encoding without `--skipZeroOverZero` (DT1's default
  run: 0 of 400 wrong).

## Not audited here

`computeGCBias`/`correctGCBias` (read: the sampling is deterministic, `arange(start,
end, stepSize)` per chunk, the ratio is `F_gc/N_gc × ΣN/ΣF` with reads above a Poisson
cutoff dropped; not executed — no `faToTwoBit` here to build a 2bit genome with known
truth, and the shipped `test_corrGC/sequence.2bit` has no independent reference),
`alignmentSieve`, `bigwigAverage`, `computeMatrixOperations`, `--Offset`/`--filterRNAstrand`
beyond reading, GTF/`--metagene` region parsing (deeptoolsintervals), the blacklist
subtraction of chunks, plotHeatmap clustering (`kmeans` without a seed) and
silhouette, `plotCorrelation`'s dendrogram, everything drawn.
