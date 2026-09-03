# deepTools audit against 167 published papers (2021–2026)

_Fourteenth audit in the series. Generated 2026-09-03 against `deeptools/deepTools`
`master` @ `ea0f68bb` (2025-01-20, version 3.5.6 — the `3.5.6` tag and PyPI's latest
release are this commit; the remote has no `develop` branch, and a `4.0.0` Rust-backend
branch was not audited). Focus: the code paths that produce published numbers —
bamCoverage/bamCompare counting and normalisation, computeMatrix binning and the
plotProfile/plotHeatmap summaries, multiBamSummary/multiBigwigSummary, plotCorrelation,
plotPCA, plotFingerprint metrics, bamPEFragmentSize, plotCoverage, estimateReadFiltering,
plotEnrichment — verified by executing the shipped code._

## What this is

The six-journal survey found **167 papers** in PNAS (74), *Nature* (71), *Cell* (19)
and *Science* (3), 2021–2026, that used deepTools, mostly to normalise and visualise
ChIP-seq, ATAC-seq, CUT&RUN and RNA-seq coverage. Its numerical core was read in full
on `master` and every suspicion was run through the installed package (master,
editable install in a Python 3.12 venv; the 3.5.1 wheel and 3.3.1 sdist from PyPI,
the cohort's most-cited versions, for version scope) on synthetic BAM and bigWig
files built with pysam/pyBigWig from known fragment lists, against numpy/scipy closed
forms or independent ports of the documented rules.

## Findings (details and line citations in [`component-reviews/coverage-and-summary-core.md`](component-reviews/coverage-and-summary-core.md); harnesses with captured output in [`verify/`](verify/))

| id | status | finding |
|---|---|---|
| **DT1** | **CONFIRMED on master, 3.5.1, 3.3.1**; open upstream as #1108/#1130 since 2021 | `bamCompare --skipZeroOverZero` derives each interval's coordinates from the previous interval's end and does not reset on a skipped bin, so every bin after a zero-over-zero bin in a chunk is written one bin too far left (375 of 400 bins wrong on a track with 206 empty bins; 0 without the option). bigwigCompare's copy of the loop resets and is right. |
| **DT2** | **CONFIRMED on master, 3.5.1, 3.3.1** | `plotPCA --log2` never reaches the matrix the SVD runs on (it rebinds `self.matrix`, the SVD uses the `--ntop` copy `m`); `--rowCenter` only works with `--ntop 0`. Loadings with `--log2` are identical to those without in every mode; the default and `--transpose` results equal a numpy SVD. |
| **DT3** | **CONFIRMED on master, 3.5.1, 3.3.1** | `plotCorrelation --removeOutliers` scales by `1.4826 × median(|x|)` — the median itself for counts — instead of the MAD it documents, so a bin is flagged only beyond ~300× the median: 25 planted bins at 40× the median in every sample are not removed and Pearson stays 0.998 where the documented rule gives ≈ 0. |
| **DT4** | **CONFIRMED on master, 3.5.1, 3.3.1**; open upstream as #1118 since 2022 | `bamCoverage --MNase` uses `read.tlen / 2` (true division since the Python 3 port), so odd-length fragments contribute four bases, one left and two right of the centre, instead of the documented three. |
| **DT5** | **CONFIRMED on master, 3.5.1, 3.3.1** (implementation vs documented definition) | `--normalizeUsing BPM` reduces algebraically to the CPM factor: the two tracks are bit-identical, the BPM track sums to (bins per read) × 1e6 (2.98e6 with 100-bp reads and 50-bp bins, 6.98e6 with `--extendReads 300`) where the help's definition gives 1e6. |
| **DT6** | **CONFIRMED on master, 3.5.1, 3.3.1** (small) | `--smoothLength` windows are truncated at every multiprocessing chunk edge (5 Mb genome-wide at typical depth, ≤ 1 Mb with `--region`): the four bins at each boundary carry a one-sided mean (1.33 vs 2.80 at 1,000,000 in the example); all other bins equal a chromosome-wide sliding mean. |
| **DT7** | **CONFIRMED on master, 3.5.1, 3.3.1** | `--ignoreDuplicates` given without any other read filter is not applied to the mapped-read count that CPM/RPKM/RPGC/BPM and `bamCompare --scaleFactorsMethod readCount` divide by (`fraction_kept` returns early without testing it; `--exactScaling` cannot override): a sample with 40 % duplicates gets CPM values 40 % low and readCount factors 0.60 instead of 1.00 against a duplicate-free sample of equal depth; adding a no-op filter changes every value. |
| **DT8** | **CONFIRMED on master, 3.5.1, 3.3.1** | `multiBigwigSummary` reads pyBigWig `stats()` zoom-level summaries (`exact=False`), which on bamCoverage tracks are not the bin means: at the default 10-kb bins median 3.4 % and up to 245 % off (144 of 200 bins by > 1 %), replicate Pearson 0.954 vs 0.999 from exact means; 1-kb bins and peak-sized BED regions fall back to the exact path. Every other deepTools bigWig reader is exact. |
| **DT9** | **CONFIRMED on master, 3.5.1, 3.3.1** (latent: sampling step = `--binSize`) | plotFingerprint's `SumCoveragePerBin` credits a fragment's last bin with a whole tile on its multi-bin path: 560 of 1,000 bins over-counted, totals 1.94× the per-base sum, when `--numberOfSamples` = genome / bin size; the default sampling takes the exact per-bin path. |
| N1–N11 | notes | multiBamSummary chunk-boundary partial bins (#1030); `computeMatrix --skipZeros` drops mean-zero rows; SES factors ignore read filters; sub-bin regions under `--nanAfterEnd`; synthetic-JSD index shift (1e-5); bigwigCompare drops a trailing zero-valued run; `--ignoreForNormalization` keeps the chromosome in the output; `--exactScaling` double-counts window-spanning reads (2e-4); 6-significant-digit output; computeMatrix strand/centre conventions; `--rowCenter` crash on integer matrices. |

**Held up under execution:** bamCoverage raw counts, `--scaleFactor`, CPM/RPKM/RPGC,
the MAPQ/flag/fragment-length filters and their denominators, `--skipNAs`, paired-end
counting with and without `--extendReads`, `--centerReads`, `--samFlagInclude 64`;
bamCompare's readCount factors, all eight `--operation`s, one- and two-value
pseudocounts, `--scaleFactors`, `--scaleFactorsMethod None` with CPM/RPKM, and SES
factors recovering an equal background depth; computeMatrix reference-point (TSS, TES,
center, `--nanAfterEnd`, `--missingDataAsZero`, every `--averageTypeBins`) and
scale-regions (unscaled ends, median bins, both strands, chromosome ends, short
regions) against an independent port; plotProfile `--averageType` and plotHeatmap's
matrix; multiBamSummary bins/BED counts and DESeq2-style `--scalingFactors`;
plotCorrelation Pearson/Spearman, `--skipZeros`, NaN rows; plotPCA default and
`--transpose`; multiBigwigSummary on 1-kb bins and BED regions; bamPEFragmentSize's
whole table; plotCoverage, estimateReadFiltering and plotEnrichment counts;
plotFingerprint's default per-bin sums and its AUC, X-intercept, elbow, JS distance,
CHANCE and synthetic-JSD metrics. Not audited: computeGCBias/correctGCBias (read, not
executed — no 2bit tooling here), alignmentSieve, bigwigAverage,
computeMatrixOperations, `--Offset`/`--filterRNAstrand`, GTF parsing, clustering,
everything drawn.

## How the papers use deepTools (lower bounds from the survey cache; see below)

| signal | papers |
|---|---|
| version stated | 39 (3.5.x 40 mentions: 3.5.1 ×20, 3.5.0 ×7, 3.5.4 ×3, 3.5.5 ×3; 3.3.x 10; 3.1.x 8; 3.2.x 6; 3.4.x 5; 3.0.x 4; 2.x 5) |
| bamCoverage / bigWig or coverage track produced | 64 / 78 |
| `--binSize` stated (10 ×6, 50 ×2, 1 ×1) | 32 |
| `--minMappingQuality` / MAPQ filter | 25 |
| `--normalizeUsing` named / CPM / RPKM / RPGC (1x) / BPM | 18 / 18 / 14 / 5 / 5 |
| `--scaleFactor` or spike-in scaling | 13 |
| `--ignoreDuplicates` | 13 |
| computeMatrix / plotHeatmap / plotProfile / scale-regions / reference-point | 14 / 8 / 4 / 4 / 1 |
| bamCompare / log2 ratio named / bigwigCompare-bigwigAverage | 11 / 3 / 2 |
| PCA / Spearman / Pearson / multiBamSummary / multiBigwigSummary | 19 / 4 / 2 / 3 / 2 |
| blacklist | 11 |
| `--smoothLength` / `--extendReads` / `--MNase` | 5 / 4 / 3 |
| plotFingerprint (JSD/CHANCE) / bamPEFragmentSize / plotEnrichment-plotCoverage / alignmentSieve | 1 / 1 / 1 / 2 |
| assay: ATAC-seq / ChIP-seq / RNA-seq / CUT&RUN-CUT&Tag / Hi-C | 24 / 23 / 53 / 9 / 2 |
| co-tools: samtools / MACS2 / Bowtie2 / BEDTools / Picard / STAR / HOMER / BWA | 105 / 95 / 85 / 66 / 46 / 45 / 41 / 40 |

Exposure by finding, as far as the cache can tell: DT7 needs `--ignoreDuplicates` with
a normalisation and no MAPQ/flag/length filter (13 papers name the option, 18 a
normalisation, 25 a MAPQ filter — whether they coincide is not decidable from a
snippet); DT8 needs multiBigwigSummary on bins ≥ 2 kb (2 papers name the tool, 19 name
a PCA); DT5 needs BPM (5); DT4 needs `--MNase` (3); DT1 needs `--skipZeroOverZero`
(none named); DT2 needs `plotPCA --log2`/`--rowCenter` (none named); DT3
`--removeOutliers` (none named); DT6 `--smoothLength` (5); DT9 a specific
`--numberOfSamples` (none). Every version the cohort names (2.0 to 3.5.5) carries all
nine by execution or by reading.

**Profiling caveat.** As for the Seurat, Scanpy and Cutadapt audits, this session had
no route to Europe PMC, so `deeptools_profile.py` ran in `--offline` mode over the
survey's stored evidence snippets; every record in `deeptools_profiles.jsonl` is
`source: survey_cache` and every count above is a lower bound. Rerun without
`--offline` from a host with Europe PMC access to replace them with full-text records.

## Filing channel (read before anything is sent)

- `.github/CONTRIBUTING.md`: fork, branch, PR with description, tests and Actions
  passing; feature work on `develop` (which no longer exists on the remote), so bug
  fixes go to `master`.
- `.github/ISSUE_TEMPLATE.md`: a four-item checklist (searched; `deeptools --version`
  and `python --version`; full command; output) — the `upstream/issue-dt*.md` texts
  answer it in that order. `.github/PULL_REQUEST_TEMPLATE.md`: four checkboxes,
  answered in `upstream/pr-bodies.md`.
- CI (`.github/workflows/test.yml`): `flake8` with the project's ignore list and
  `pytest` on Python 3.9–3.12; `CHANGES.txt` free-form bullets per version.
- **DT1 and DT4 are already open upstream** (#1108/#1130, #1118; no maintainer reply
  in three years) — their texts are drafted as comments with the cause and a patch.
  The other seven are new (tracker searched 2026-09-03). **The kit is in
  [`upstream/`](upstream/)**: nine issue/comment texts with self-contained
  reproductions run on 3.5.6 and 3.3.1, seven `git am`-able patches (fix + regression
  test failing on unmodified `master` + `CHANGES.txt` bullet; project tests, doctests
  and flake8 recorded in `upstream/test-runs.txt`), PR bodies, and the list of
  documents read. Nothing has been filed.

## Files

| file | what |
|---|---|
| `deeptools_profile.py`, `deeptools_profiles.jsonl`, `profile_run.log` | profiling pass (offline; see caveat) |
| `component-reviews/coverage-and-summary-core.md` | the review: DT1–DT9, N1–N11, withdrawn suspicions, held-up list, not-audited list |
| `verify/_synth.py` | shared helpers: synthetic BAM/bigWig writers, numpy reference quantities |
| `verify/dt1_skipzerooverzero_coordinates.py` (+ `.out`, `.v3.5.1.out`, `.v3.3.1.out`) | DT1: bamCompare with/without the option vs closed form; bigwigCompare control |
| `verify/dt2_plotpca_log2_rowcenter.py` (+ outs) | DT2: six option sets vs a numpy PCA reference |
| `verify/dt3_removeoutliers_mad.py` (+ outs) | DT3: documented MAD rule vs `get_outlier_indices`; Pearson through the CLI |
| `verify/dt4_mnase_center.py` (+ outs) | DT4: centre bases for six fragment lengths |
| `verify/dt5_bpm_equals_cpm.py` (+ outs) | DT5: CPM vs BPM tracks, documented BPM, with and without `--extendReads` |
| `verify/dt6_smoothlength_chunk_edges.py` (+ outs) | DT6: smoothed track vs chromosome-wide sliding mean, with and without `--region` |
| `verify/dt7_ignoreduplicates_scaling.py` (+ outs) | DT7: CPM factors and bamCompare readCount factors with and without a no-op filter |
| `verify/dt8_multibigwigsummary_zoom.py`, `dt8b_zoom_mechanism.py` (+ outs) | DT8: reported vs exact bin means at 10/5/2/1 kb and BED regions, replicate correlations; where the error comes from |
| `verify/heldup_fingerprint.py` (+ outs) | DT9 and the held-up fingerprint metrics: both sampling paths, AUC/elbow/JSD/CHANCE/synthetic JSD |
| `verify/heldup_bamcoverage_normalisation.py` (+ `.out`) | held-up: bamCoverage counting, normalisation and filters (N8, N9) |
| `verify/heldup_bamcompare.py` (+ `.out`) | held-up: bamCompare operations, pseudocounts, scale factors, SES |
| `verify/heldup_computematrix.py` (+ `.out`) | held-up: computeMatrix both modes vs an independent port; plotProfile/plotHeatmap summaries (N4, N10) |
| `verify/heldup_summaries.py` (+ `.out`) | held-up: multiBamSummary, multiBigwigSummary, plotCorrelation, bamPEFragmentSize, plotCoverage, estimateReadFiltering, plotEnrichment |
| `verify/note_misc.py` (+ `.out`) | N1, N2, N3, N6, N7 |
| `upstream/` | filing kit: issue/comment texts, MCVEs and outputs, patches 0001–0007, PR bodies, test runs, documents read |

Harnesses need an install of the version under test: `uv venv --python 3.12 venv &&
uv pip install -e <deepTools clone>` (pysam, py2bit, pyBigWig and deeptoolsintervals
come from PyPI), or `uv pip install deeptools==<version>` (3.5.1 needs
`matplotlib<3.9`; plotFingerprint on 3.5.1/3.3.1 needs Python 3.11 with
`numpy<1.24`). Each harness prints the version it ran against.

## Next steps

1. Post the DT1 and DT4 comments on #1108/#1130 and #1118 with their PRs; open the DT7,
   DT8, DT2, DT3, DT9 issues and PRs from the kit; open DT5 and DT6 as issues. Record
   numbers and maintainer responses here and in the top-level table.
2. Execute computeGCBias/correctGCBias against an independent GC tabulation once a 2bit
   genome with known truth can be built (needs `faToTwoBit` or a py2bit writer).
3. Full-text profiling rerun when Europe PMC is reachable, to see which papers combine
   `--ignoreDuplicates` with a normalisation and no other filter (DT7), and which run
   multiBigwigSummary on bamCoverage tracks (DT8).
