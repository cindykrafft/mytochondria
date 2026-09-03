#!/usr/bin/env python3
"""Held-up checks for the summary tools: multiBamSummary (bins and BED-file,
--outRawCounts, --scalingFactors), multiBigwigSummary (bins and BED-file),
plotCorrelation (Pearson/Spearman, --skipZeros, NaN rows), bamPEFragmentSize
(--table percentiles), plotCoverage (--outCoverageMetrics and the printed
summary), estimateReadFiltering counts, plotEnrichment percentages.

References: numpy/scipy on the same synthetic data; DESeq2's median-of-ratios
size factors written out by hand.
"""
import os
import re
import subprocess
import numpy as np
import scipy.stats
import _synth as S
from deeptools.countReadsPerBin import estimateSizeFactors

print(S.version())
rng = np.random.default_rng(51)
d = S.tmpdir()
chroms = [("chr1", 200000), ("chr2", 50000)]
BS = 1000
RL = 50

# --- three single-end BAMs with different depths ----------------------------
bams, frags = [], []
for k, n in enumerate([6000, 9000, 4000]):
    rd, fr = [], {}
    for cid, (c, L) in enumerate(chroms):
        w = 1.0 + 3.0 * (np.sin(np.arange(L) / 3000.0 + k) > 0.8)
        r, f = S.random_se_reads(rng, cid, L, n if c == "chr1" else n // 4, RL, "s%d" % k, weights=w)
        rd += r
        fr[c] = f
    bams.append(S.write_bam(os.path.join(d, "s%d.bam" % k), chroms, rd))
    frags.append(fr)
counts = {c: np.array([S.bin_overlap_counts(fr[c], L, BS) for fr in frags]).T for c, L in chroms}
ref_bins = np.vstack([counts["chr1"], counts["chr2"]]).astype(float)


def load_npz(path):
    z = np.load(path)
    return np.asarray(z["matrix"].tolist()), [str(x) for x in z["labels"]]


npz = os.path.join(d, "bins.npz")
raw = os.path.join(d, "bins.tab")
sf = os.path.join(d, "sf.tab")
S.run(["multiBamSummary", "bins", "-b"] + bams + ["-o", npz, "-bs", BS, "-p", 1, "--outRawCounts", raw, "--scalingFactors", sf])
m, labels = load_npz(npz)
rows = [l.rstrip("\n").split("\t") for l in open(raw) if not l.startswith("#")]
order = sorted(range(len(rows)), key=lambda i: (rows[i][0], int(rows[i][1])))
mr = np.array([[float(x) for x in rows[i][3:]] for i in order])
coords = [(rows[i][0], int(rows[i][1]), int(rows[i][2])) for i in order]
print("%-70s %s" % ("multiBamSummary bins: matrix equals reads-per-bin reference", "OK" if np.array_equal(np.sort(m, axis=0), np.sort(ref_bins, axis=0)) else "MISMATCH"))
print("%-70s %s" % ("multiBamSummary bins --outRawCounts: consecutive 1-kb bins, values equal", "OK" if np.array_equal(mr, ref_bins) and all(e - s == BS or e == dict(chroms)[c] for c, s, e in coords) else "MISMATCH"))
print("%-70s %s" % ("labels are the BAM basenames", "OK" if labels == ["s0.bam", "s1.bam", "s2.bam"] else "MISMATCH %s" % labels))


def deseq_sf(mat):
    lg = np.log(mat)
    ok = np.all(np.isfinite(lg), axis=1)
    geo = lg[ok].mean(axis=1)
    return np.exp(np.median(lg[ok] - geo[:, None], axis=0))


sfs = [float(l.split("\t")[1]) for l in open(sf) if not l.startswith("sample")]
print("%-70s %s (deepTools %s, 1/DESeq2 %s)" % ("--scalingFactors = 1 / DESeq2 median-of-ratios size factors",
      "OK" if np.allclose(sfs, 1 / deseq_sf(ref_bins), atol=1e-4) else "MISMATCH", np.round(sfs, 4), np.round(1 / deseq_sf(ref_bins), 4)))
print("%-70s %s" % ("estimateSizeFactors() equals the hand-written DESeq2 rule",
                    "OK" if np.allclose(estimateSizeFactors(ref_bins), 1 / deseq_sf(ref_bins)) else "MISMATCH"))

# BED-file mode: regions of unequal length, one with two exons via BED12? keep simple BED3
regs = [("chr1", 1000, 2500), ("chr1", 50000, 50010), ("chr2", 10000, 30000), ("chr1", 199500, 200000)]
bed = os.path.join(d, "r.bed")
with open(bed, "w") as fh:
    for c, s, e in regs:
        fh.write("%s\t%d\t%d\n" % (c, s, e))
npz2 = os.path.join(d, "bed.npz")
raw2 = os.path.join(d, "bed.tab")
S.run(["multiBamSummary", "BED-file", "-b"] + bams + ["--BED", bed, "-o", npz2, "-p", 1, "--outRawCounts", raw2])
rows = [l.rstrip("\n").split("\t") for l in open(raw2) if not l.startswith("#")]
got = {(r[0], int(r[1]), int(r[2])): [float(x) for x in r[3:]] for r in rows}
ok = True
for c, s, e in regs:
    exp = [sum(1 for f in fr[c] if f[1] > s and f[0] < e) for fr in frags]
    ok &= got.get((c, s, e)) == exp
print("%-70s %s" % ("multiBamSummary BED-file: reads overlapping each region", "OK" if ok else "MISMATCH %s" % got))

# --- plotCorrelation vs numpy / scipy ---------------------------------------
def cormat(extra, method):
    tab = os.path.join(d, "c.tab")
    S.run(["plotCorrelation", "-in", npz, "-c", method, "-p", "heatmap", "--outFileCorMatrix", tab] + extra)
    rows = [l.rstrip("\n").split("\t") for l in open(tab) if not l.startswith("#") and not l.startswith("\t")]
    return np.array([[float(x) for x in r[1:]] for r in rows])


print("%-70s %s" % ("plotCorrelation pearson = numpy corrcoef (4 d.p.)",
                    "OK" if np.allclose(cormat([], "pearson"), np.corrcoef(m.T), atol=6e-5) else "MISMATCH"))
print("%-70s %s" % ("plotCorrelation spearman = scipy spearmanr (4 d.p.)",
                    "OK" if np.allclose(cormat([], "spearman"), scipy.stats.spearmanr(m)[0], atol=6e-5) else "MISMATCH"))
keep = m.sum(axis=1) != 0
print("%-70s %s (%d of %d bins kept)" % ("plotCorrelation --skipZeros pearson: bins with all-zero rows removed",
                                          "OK" if np.allclose(cormat(["--skipZeros"], "pearson"), np.corrcoef(m[keep].T), atol=6e-5) else "MISMATCH", keep.sum(), len(keep)))
mn = m.copy()
mn[rng.choice(len(mn), 30, replace=False), 1] = np.nan
npzn = os.path.join(d, "nan.npz")
with open(npzn, "wb") as fh:
    np.savez_compressed(fh, matrix=mn, labels=labels)
tab = os.path.join(d, "cn.tab")
S.run(["plotCorrelation", "-in", npzn, "-c", "pearson", "-p", "heatmap", "--outFileCorMatrix", tab])
rows = [l.rstrip("\n").split("\t") for l in open(tab) if not l.startswith("#") and not l.startswith("\t")]
cn = np.array([[float(x) for x in r[1:]] for r in rows])
print("%-70s %s" % ("plotCorrelation: rows with a NaN in any sample dropped before Pearson",
                    "OK" if np.allclose(cn, np.corrcoef(mn[~np.isnan(mn).any(axis=1)].T), atol=6e-5) else "MISMATCH"))

# --- multiBigwigSummary bins / BED-file ---------------------------------------
vals = {c: rng.gamma(2.0, 1.0, L) for c, L in chroms}
vals["chr1"][5000:7000] = np.nan
bws = [S.write_bigwig(os.path.join(d, "w%d.bw" % k), chroms, {c: vals[c] * (k + 1) for c in vals}) for k in range(2)]
npz3 = os.path.join(d, "bw.npz")
raw3 = os.path.join(d, "bw.tab")
S.run(["multiBigwigSummary", "bins", "-b"] + bws + ["-o", npz3, "-bs", BS, "-p", 1, "--outRawCounts", raw3])
rows = [l.rstrip("\n").split("\t") for l in open(raw3) if not l.startswith("#")]
worst, n, nan_ok = 0.0, 0, True
for r in rows:
    c, s, e = r[0], int(r[1]), int(r[2])
    for k in range(2):
        g = float(r[3 + k])
        seg = vals[c][s:e] * (k + 1)
        exp = np.nanmean(seg) if not np.all(np.isnan(seg)) else np.nan
        if np.isnan(exp) or np.isnan(g):
            nan_ok &= np.isnan(exp) == np.isnan(g)
            continue
        worst = max(worst, abs(g - exp) / exp)
        n += 1
print("%-70s max rel diff %.2e over %d bins; NaN bins agree: %s" % ("multiBigwigSummary bins: bin mean vs numpy nanmean (pyBigWig zoom-level stats)", worst, n, nan_ok))
# bins within 2 kb of a partially-NaN region vs the rest
S.run(["multiBigwigSummary", "BED-file", "-b"] + bws + ["--BED", bed, "-o", npz3, "-p", 1, "--outRawCounts", raw3])
rows = [l.rstrip("\n").split("\t") for l in open(raw3) if not l.startswith("#")]
worst = 0.0
for r in rows:
    c, s, e = r[0], int(r[1]), int(r[2])
    for k in range(2):
        worst = max(worst, abs(float(r[3 + k]) - np.nanmean(vals[c][s:e] * (k + 1))) / np.nanmean(vals[c][s:e] * (k + 1)))
print("%-70s max rel diff %.2e" % ("multiBigwigSummary BED-file: region mean vs numpy", worst))

# --- bamPEFragmentSize --------------------------------------------------------
pe_reads, pe_frags = S.random_pe_pairs(rng, 0, 200000, 3000, RL, np.arange(120, 420))
pe = S.write_bam(os.path.join(d, "pe.bam"), chroms, pe_reads)
tab = os.path.join(d, "fs.tab")
S.run(["bamPEFragmentSize", "-b", pe, "--table", tab, "-p", 1, "--distanceBetweenBins", 0, "--binSize", 200000])
hdr, row = [l.rstrip("\n").split("\t") for l in open(tab)]
fl = np.array([e - s for s, e in pe_frags], float)
got = dict(zip(hdr[1:], [float(x) for x in row[1:]]))
exp = {"Frag. Sampled": len(fl), "Frag. Len. Min.": fl.min(), "Frag. Len. 1st. Qu.": np.percentile(fl, 25),
       "Frag. Len. Mean": fl.mean(), "Frag. Len. Median": np.median(fl), "Frag. Len. 3rd Qu.": np.percentile(fl, 75),
       "Frag. Len. Max": fl.max(), "Frag. Len. Std.": fl.std(), "Frag. Med. Abs. Dev.": np.median(np.abs(fl - np.median(fl))),
       "Frag. Len. 10%": np.percentile(fl, 10), "Frag. Len. 90%": np.percentile(fl, 90), "Frag. Len. 99%": np.percentile(fl, 99),
       "Read Len. Mean": RL, "Reads Sampled": len(fl)}
bad = [k for k in exp if not np.isclose(got[k], exp[k], rtol=1e-6)]
print("%-70s %s" % ("bamPEFragmentSize --table: n, min/quartiles/median/mean/max/std(ddof=0)/MAD/percentiles = numpy", "OK" if not bad else "MISMATCH %s" % {k: (got[k], exp[k]) for k in bad}))

# --- plotCoverage ---------------------------------------------------------------
metrics = os.path.join(d, "cov.tab")
r = subprocess.run([S.tool("plotCoverage"), "-b", bams[0], "--outCoverageMetrics", metrics, "--coverageThresholds", "1",
                    "--coverageThresholds", "3", "-n", "5000", "-p", "1", "--region", "chr1:0:200000"], capture_output=True, text=True)
pb = S.per_base(frags[0]["chr1"], 200000)
lines = [l.split("\t") for l in r.stdout.splitlines() if l.startswith("s0")]
mean_got, std_got = float(lines[0][1]), float(lines[0][2])
sampled = pb[::40]      # numberOfSamples 5000 on 200 kb -> step 40, bin 1
print("%-70s %s (mean %.2f vs %.2f, std %.2f vs %.2f)" % ("plotCoverage sampled per-base mean/std (step 40) = numpy on the same positions",
      "OK" if abs(mean_got - sampled.mean()) < 0.005 and abs(std_got - sampled.std()) < 0.005 else "MISMATCH", mean_got, sampled.mean(), std_got, sampled.std()))
mt = {(l.split("\t")[0], l.split("\t")[1]): float(l.split("\t")[2]) for l in open(metrics) if l.startswith("s0")}
print("%-70s %s" % ("plotCoverage --outCoverageMetrics percent of sampled bases >= 1, >= 3",
                    "OK" if abs(mt[("s0.bam", "1")] - 100 * np.mean(sampled >= 1)) < 0.002 and abs(mt[("s0.bam", "3")] - 100 * np.mean(sampled >= 3)) < 0.002 else "MISMATCH %s" % mt))

# --- estimateReadFiltering ---------------------------------------------------------
r = subprocess.run([S.tool("estimateReadFiltering"), "-b", bams[0], "--minMappingQuality", "10", "--samFlagExclude", "16",
                    "--binSize", "200000", "--distanceBetweenBins", "0", "-p", "1"], capture_output=True, text=True)
line = [l.split("\t") for l in r.stdout.splitlines() if l.endswith("0.0") and not l.startswith("Sample")][0]
n_total = sum(len(v) for v in frags[0].values())
n_rev = sum(sum(1 for f in v if f[2]) for v in frags[0].values())
print("%-70s %s (%s)" % ("estimateReadFiltering: total, mapped, filtered (all MAPQ 30; reverse-strand reads by flag)",
                        "OK" if int(line[1]) == n_total and int(line[2]) == n_total and float(line[4]) == n_rev and float(line[7]) == n_rev else "MISMATCH", line[1:8]))

# --- plotEnrichment ---------------------------------------------------------------
feat = os.path.join(d, "f.bed")
with open(feat, "w") as fh:
    fh.write("chr1\t0\t100000\tA\nchr2\t0\t50000\tB\n")
raw4 = os.path.join(d, "enr.tab")
S.run(["plotEnrichment", "-b", bams[0], "--BED", feat, "--outRawCounts", raw4, "-p", 1])
rows = {l.split("\t")[1]: l.rstrip("\n").split("\t") for l in open(raw4) if not l.startswith("file")}
# features are labelled per BED file (the name column is not used without --attributeKey)
inF = sum(1 for f in frags[0]["chr1"] if f[0] < 100000) + len(frags[0]["chr2"])
r = rows["f.bed"]
ok = int(r[3]) == inF and int(r[4]) == n_total and abs(float(r[2]) - 100.0 * inF / n_total) < 0.006
print("%-70s %s (%s)" % ("plotEnrichment --outRawCounts: reads overlapping the BED file's regions / total, percent", "OK" if ok else "MISMATCH", r[1:]))
