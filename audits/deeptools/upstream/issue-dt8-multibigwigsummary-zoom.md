Title: multiBigwigSummary reports zoom-level summaries, not the mean of the bin: up to several-fold off next to peaks at the default 10-kb bins

<!-- deeptools/deepTools .github/ISSUE_TEMPLATE.md checklist -->

- [x] Search whether this issue (or a similar issue) has been solved before: no prior report of the cause found (nearest: #1296 "conflict about the pheatmap and multibigwigsummary results", #1270, #1139 "bam and bigwig peak not the same").
- [x] deepTools version: 3.5.6 (`master` @ `ea0f68bb`; also reproduced on 3.5.1 and 3.3.1); Python 3.12.3; pyBigWig 0.3.25
- [x] Full command producing the issue: `multiBigwigSummary bins -b s.bw s2.bw -bs 10000 -o x.npz --outRawCounts raw.tab` on bamCoverage tracks (harness below; the small script at the end is the minimal one)
- [x] Output printed: see below

**What happens.** `getScorePerBigWigBin.countFragmentsInRegions_worker` (`deeptools/getScorePerBigWigBin.py`, line 107) calls `bwh.stats(chrom, exon[0], exon[1])` with pyBigWig's default `exact=False`, which answers from the bigWig's zoom level whose reduction span fits the query. For the run-length-encoded tracks bamCoverage writes (intervals of variable length that straddle the zoom records) those summaries are not the mean of the values inside the bin. computeMatrix, bigwigCompare and bigwigAverage read the exact per-base values (`bigwig.values`); multiBigwigSummary is the only tool that does not, and its help defines its output as "the average scores for each of the files in every genomic region".

**Measured** on a bamCoverage track (50-bp bins) from 300,000 synthetic 50-bp reads with 150 peaks on a 2-Mb chromosome (the file has zoom spans of 944 and 3,776 bp; the reference is numpy's mean of `bw.values()` over the bin, which `stats(exact=True)` matches to 1e-6):

| `--binSize` | \|reported − exact\| / exact, median | 95th percentile | max | bins off by more than 1 % |
|---|---|---|---|---|
| 10,000 (default) | 0.034 | 0.72 | 2.45 | 144 of 200 |
| 5,000 | 0.009 | 0.13 | 1.59 | 189 of 400 |
| 2,000 | 0.025 | 0.32 | 4.21 | 761 of 1,000 |
| 1,000; BED-file regions of 200–1,500 bp | 0 | 0 | 0 | 0 (no zoom level fits, the exact path is used) |

Examples: bin 1,850,000–1,860,000 reported 14.746, exact 5.850 (the neighbouring 10-kb bins average 15.9 and 37.5); bin 10,000–20,000 reported 18.648, exact 5.410. Two replicate tracks correlate at Pearson 0.9539 from the reported 10-kb values and 0.9990 from the exact means (Spearman 0.913 vs 0.909); at 2 kb, 0.9920 vs 0.9988. Rewriting the same intervals with pyBigWig in one `addEntries` call, in calls of 1,000, or with the default number of zoom levels gives identical errors, so it is not the way deepTools writes the file; a track of 50-bp aligned steps with one peak gives a median error of 0.38 % and 10 % at the peak bin, and tracks whose only zoom span exceeds the bin size are exact. The expected values of the existing `test_multiBigwigSummary_gtf` are themselves zoom summaries (27.3125 for the second transcript, whose exact mean is 27.8067).

**Minimal script** (a 50-bp-step track with one peak next to a bin boundary; the deviation here is small, 1.901 vs 1.906, because the steps are aligned — the harness linked below reproduces the large ones on bamCoverage output):

```python
import subprocess, numpy as np, pyBigWig

n = 400000
vals = np.random.RandomState(0).gamma(2.0, 1.0, n // 50).repeat(50)
vals[98000:100000] += 40.0          # peak in bin 90,000-100,000 only
bw = pyBigWig.open("/tmp/z.bw", "w"); bw.addHeader([("chr1", n)])
bw.addEntries(["chr1"] * (n // 50), list(range(0, n, 50)), ends=list(range(50, n + 1, 50)), values=[float(x) for x in vals[::50]]); bw.close()
subprocess.run(["multiBigwigSummary", "bins", "-b", "/tmp/z.bw", "/tmp/z.bw", "-bs", "10000", "-o", "/tmp/z.npz", "--outRawCounts", "/tmp/z.tab"], check=True, capture_output=True)
rows = {int(l.split()[1]): float(l.split()[3]) for l in open("/tmp/z.tab") if not l.startswith("#")}
for s in (90000, 100000):
    print("bin %d-%d: multiBigwigSummary %.3f, exact mean %.3f, pyBigWig stats(exact=True) %.3f"
          % (s, s + 10000, rows[s], vals[s:s + 10000].mean(), pyBigWig.open("/tmp/z.bw").stats("chr1", s, s + 10000, exact=True)[0]))
assert abs(rows[100000] - vals[100000:110000].mean()) < 1e-3, "the bin after the peak is not the mean of its values"
```

**Output** (3.5.6):

```
bin 90000-100000: multiBigwigSummary 10.043, exact mean 10.054, pyBigWig stats(exact=True) 10.054
bin 100000-110000: multiBigwigSummary 1.901, exact mean 1.906, pyBigWig stats(exact=True) 1.906
Traceback (most recent call last):
  File "mcve_dt8_zoom.py", line 17, in <module>
    assert abs(rows[100000] - vals[100000:110000].mean()) < 1e-3, "the bin after the peak is not the mean of its values"
AssertionError: the bin after the peak is not the mean of its values
```

**Fix.** `bwh.stats(chrom, exon[0], exon[1], exact=True)` (pyBigWig ≥ 0.3.2); slower on large bins, so an `--exact` switch defaulting to on may be preferable. A patch with a test and the updated expected values of `test_multiBigwigSummary_gtf` is ready and a PR follows. Note that plotFingerprint's bigWig input path (`sumCoveragePerBin.py`, line 93, `stats(..., nBins=...)`) has the same default.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/deeptools)

---
_Generated by [Claude Code](https://claude.ai/code)_
