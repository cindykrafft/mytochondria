#!/usr/bin/env python3
"""Held-up checks for plotFingerprint: per-bin coverage sums (--outRawCounts),
AUC / X-intercept / elbow point, Jensen-Shannon distance against a reference
sample, the CHANCE metrics and the synthetic (Poisson) JSD, against
independent numpy implementations of the documented definitions
(http://deeptools.readthedocs.io/en/latest/content/feature/plotFingerprint_QC_metrics.html).

Also exercises the two code paths of sumCoveragePerBin.get_coverage_of_region:
the default one (--numberOfSamples such that the sampling step differs from
--binSize: one 2-tuple region per bin) and the one taken when the step equals
the bin size (a single 3-tuple region covering the chunk), see note N4.
"""
import os
import numpy as np
from scipy import interpolate
from scipy.stats import poisson
import _synth as S

print(S.version())
rng = np.random.default_rng(81)
d = S.tmpdir()
L = 500000
BS = 500
w = np.ones(L)
for p in rng.integers(0, L - 3000, 30):
    w[p:p + 1500] += 20
r_in, f_in = S.random_se_reads(rng, 0, L, 20000, 50, "i")
r_ch, f_ch = S.random_se_reads(rng, 0, L, 20000, 50, "c", weights=w)
bam_in = S.write_bam(os.path.join(d, "input.bam"), [("chr1", L)], r_in)
bam_ch = S.write_bam(os.path.join(d, "chip.bam"), [("chr1", L)], r_ch)
pb_in, pb_ch = S.per_base(f_in, L), S.per_base(f_ch, L)


def run(nsamples):
    raw = os.path.join(d, "raw%d.tab" % nsamples)
    qm = os.path.join(d, "qm%d.tab" % nsamples)
    S.run(["plotFingerprint", "-b", bam_ch, bam_in, "--labels", "chip", "input", "--outRawCounts", raw,
           "--outQualityMetrics", qm, "--JSDsample", bam_in, "-bs", BS, "-n", nsamples, "-p", 1])
    counts = np.array([[float(x) for x in l.split()] for l in open(raw) if not l.startswith("#") and not l.startswith("'")])
    metrics = {}
    lines = [l.rstrip("\n").split("\t") for l in open(qm)]
    for row in lines[1:]:
        # releases before 3.5.1 write "NA" for the reference sample's own JSD/CHANCE
        metrics[row[0]] = dict(zip(lines[0][1:], [float(x) if x not in ("NA", "nan") else np.nan for x in row[1:]]))
    return counts, metrics


def expected_windows(nsamples):
    step = max(int(L / nsamples), 1)
    return [(i, i + BS) for i in range(0, L, step) if i + BS <= L]


for nsamples in [2000, 1000]:
    step = max(int(L / nsamples), 1)
    counts, metrics = run(nsamples)
    wins = expected_windows(nsamples)
    ref = np.array([[pb_ch[s:e].sum(), pb_in[s:e].sum()] for s, e in wins], float)
    same = counts.shape == ref.shape and np.array_equal(counts, ref)
    print("\n--numberOfSamples %d (sampling step %d, bin %d -> %s path): %d windows; per-bin coverage sums equal per-base reference: %s"
          % (nsamples, step, BS, "3-tuple chunk" if step == BS else "2-tuple per-bin", len(wins), same))
    if not same and counts.shape == ref.shape:
        diff = counts - ref
        print("  sum reported / sum exact: chip %.3f, input %.3f; bins over-counted: %d of %d; mean excess per over-counted bin %.1f"
              % (counts[:, 0].sum() / ref[:, 0].sum(), counts[:, 1].sum() / ref[:, 1].sum(), (diff[:, 0] > 0).sum(), len(ref), diff[diff[:, 0] > 0, 0].mean()))
    # --- metrics from the reported counts (so the metric formulas are tested on their own) ---
    for j, lab in enumerate(["chip", "input"]):
        reads = counts[:, j]
        cs = np.cumsum(np.sort(reads))
        cs = cs / cs[-1]
        n = len(cs)
        auc = cs.sum() / n
        xint = (np.argmax(cs > 0) + 1) / n
        line = np.arange(n) / (n - 1)
        elbow = (np.argmax(line - cs) + 1) / n
        m = metrics[lab]
        print("  %s: AUC %.6f (ref %.6f), X-int %.6f (ref %.6f), elbow %.6f (ref %.6f) -> %s"
              % (lab, m["AUC"], auc, m["X-intercept"], xint, m["Elbow Point"], elbow,
                 "OK" if np.allclose([m["AUC"], m["X-intercept"], m["Elbow Point"]], [auc, xint, elbow], atol=1e-9) else "MISMATCH"))

    # JSD (chip vs input): the documented construction, written independently
    def signal_cdf(hist):
        k = np.arange(len(hist))
        bin_cdf = np.cumsum(hist) / hist.sum()
        sig_cdf = np.cumsum(hist * k) / (hist * k).sum()
        f = interpolate.interp1d(bin_cdf, sig_cdf, bounds_error=False, fill_value=(0, 1))
        return f(np.arange(0, 1.00001, 0.00001))

    def jsd_from_hists(h1, h2):
        c1, c2 = signal_cdf(h1), signal_cdf(h2)
        for c in (c1, c2):
            if np.isnan(c[0]):
                c[0] = 1e-12
        p1, p2 = np.diff(c1), np.diff(c2)
        M = (p1 + p2) / 2
        with np.errstate(divide="ignore", invalid="ignore"):
            j = 0.5 * np.nansum(p1 * np.log2(p1 / M)) + 0.5 * np.nansum(p2 * np.log2(p2 / M))
        return np.sqrt(j)

    def hist_of(v):
        v = v[v > 0].astype(int)
        return np.bincount(v, minlength=int(v.max()) + 2)

    jsd = jsd_from_hists(hist_of(counts[:, 0]), hist_of(counts[:, 1]))
    m = metrics["chip"]
    print("  JS distance chip vs input: %.6f (independent %.6f) -> %s" % (m["JS Distance"], jsd, "OK" if abs(m["JS Distance"] - jsd) < 1e-6 else "MISMATCH"))
    # CHANCE
    sub = counts[np.argsort(counts[:, 0])]
    cs = np.cumsum(sub, axis=0) / np.cumsum(sub, axis=0)[-1]
    k = np.argmax(cs[:, 1] - cs[:, 0])
    p, q = cs[k, 0], cs[k, 1]
    pce, dfe = 100.0 * (len(cs) - k) / len(cs), 100.0 * (q - p)
    print("  CHANCE %% genome enriched %.4f (ref %.4f), diff. enrichment %.4f (ref %.4f) -> %s"
          % (m["% genome enriched"], pce, m["diff. enrichment"], dfe, "OK" if np.allclose([m["% genome enriched"], m["diff. enrichment"]], [pce, dfe], atol=1e-6) else "MISMATCH"))
    # synthetic JSD: Poisson(lambda = mean bin sum) input; value k at index k (deepTools puts value k at index k-1, note N5)
    lam = counts[:, 0].mean()
    hin = np.concatenate([[0.0], poisson.pmf(np.arange(1, 10000000), lam)]) * counts[:, 0].sum()
    hin_shifted = poisson.pmf(np.arange(1, 10000000), lam) * counts[:, 0].sum()
    print("  synthetic JSD %.6f; independent Poisson reference %.6f; the same with deepTools' index shift %.6f"
          % (m["Synthetic JS Distance"], jsd_from_hists(hist_of(counts[:, 0]), hin), jsd_from_hists(hist_of(counts[:, 0]), hin_shifted)))
