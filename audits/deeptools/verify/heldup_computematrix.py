#!/usr/bin/env python3
"""Held-up checks for computeMatrix (reference-point TSS/TES/center and
scale-regions, strand flipping, --averageTypeBins mean/median/max/sum/std,
--missingDataAsZero, --nanAfterEnd, --unscaled5prime/3prime, regions running
off chromosome ends, regions shorter than the body bins) and for the
plotProfile / plotHeatmap --averageType summaries computed from the matrix.

Reference: an independent numpy port of the documented binning. A bigWig with
per-base random values and NaN gaps on two chromosomes; BED regions on both
strands, near both chromosome ends, of varying length.
"""
import gzip
import os
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(41)
d = S.tmpdir()
chroms = [("chr1", 60000), ("chr2", 6000)]
vals = {}
for c, L in chroms:
    v = rng.gamma(2.0, 1.0, L)
    v[rng.random(L) < 0.05] = np.nan            # missing data
    v[np.where(rng.random(L) < 0.3)[0]] = 0.0   # exact zeros
    vals[c] = v
bw = S.write_bigwig(os.path.join(d, "s.bw"), chroms, vals)
regions = [("chr1", 10000, 12000, "+"), ("chr1", 20000, 20735, "-"), ("chr1", 30000, 30040, "+"),
           ("chr1", 41000, 45501, "-"), ("chr1", 300, 1200, "+"), ("chr1", 59000, 59900, "-"),
           ("chr2", 100, 900, "+"), ("chr2", 5200, 5900, "-"), ("chr1", 50000, 50005, "+")]
bed = os.path.join(d, "r.bed")
with open(bed, "w") as fh:
    for i, (c, s, e, st) in enumerate(regions):
        fh.write("%s\t%d\t%d\tr%d\t0\t%s\n" % (c, s, e, i, st))


def fetch(c, s, e, mdz):
    """per-base values for [s, e) with NaN (or 0) outside the chromosome"""
    L = dict(chroms)[c]
    out = np.full(e - s, np.nan)
    a, b = max(0, s), min(L, e)
    if b > a:
        out[a - s:b - s] = vals[c][a:b]
    if mdz:
        out[np.isnan(out)] = 0.0
    return out


def agg(x, how):
    x = x[~np.isnan(x)]
    if len(x) == 0:
        return np.nan
    return {"mean": np.mean, "median": np.median, "max": np.max, "sum": np.sum, "std": np.std, "min": np.min}[how](x)


def bins_of(arr, nb, how, offset=0):
    """Partition of len(arr) bases into nb bins: boundaries floor(linspace)
    with the same cumulative offset deepTools passes to np.linspace
    (heatmapper.coverage_from_array), so that floating-point rounding of a
    non-integer bin width lands on the same base."""
    n = len(arr)
    pos = np.linspace(offset, offset + n, nb, endpoint=False, dtype=int) - offset if nb > 1 else np.array([0])
    pos = np.append(pos, n)
    return np.array([agg(arr[int(pos[i]):max(int(pos[i + 1]), int(pos[i]) + 1)], how) for i in range(nb)])


def ref_refpoint(c, s, e, st, a, b, bs, how, mdz, point, nan_after_end):
    if point == "TSS":
        rp = s if st == "+" else e
    elif point == "TES":
        rp = e if st == "+" else s
    else:
        rp = s + (e - s) // 2          # deepTools: middle = size // 2 from the region start on both strands
    if st == "+":
        arr = fetch(c, rp - b, rp + a, mdz)
    else:
        arr = fetch(c, rp - a, rp + b, mdz)[::-1]
    if nan_after_end and point == "TSS":
        past = (rp + a) - e if st == "+" else s - (rp - a)
        if past > 0:
            arr[len(arr) - past:] = np.nan
    return np.concatenate([bins_of(arr[i * bs:(i + 1) * bs], 1, how) for i in range((a + b) // bs)])


def ref_scale(c, s, e, st, a, b, m, bs, how, mdz, u5, u3):
    """Zones in genomic orientation (deepTools bins every zone from the
    genomic left and reverses the whole row for '-' strand regions), so for a
    '-' region the 5' unscaled zone is the genomic-right end of the body."""
    body = fetch(c, s, e, mdz)
    if st == "+":
        left = fetch(c, s - b, s, mdz)
        right = fetch(c, e, e + a, mdz)
        gl, gr = u5, u3                       # unscaled bases at the genomic left / right of the body
        zones = [(left, b // bs), (body[:gl], gl // bs), (body[gl:len(body) - gr], m // bs),
                 (body[len(body) - gr:] if gr else body[:0], gr // bs), (right, a // bs)]
    else:
        left = fetch(c, s - a, s, mdz)
        right = fetch(c, e, e + b, mdz)
        gl, gr = u3, u5
        zones = [(left, a // bs), (body[:gl], gl // bs), (body[gl:len(body) - gr], m // bs),
                 (body[len(body) - gr:] if gr else body[:0], gr // bs), (right, b // bs)]
    parts, offset = [], 0
    for arr, nb in zones:
        if nb:
            parts.append(bins_of(arr, nb, how, offset))
        offset += len(arr)
    row = np.concatenate(parts)
    return row[::-1] if st == "-" else row


def read_matrix(path):
    rows = {}
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith("@"):
                continue
            f = line.rstrip("\n").split("\t")
            rows[f[3]] = np.array([float(x) for x in f[6:]])
    return rows


def compare(name, cmd, reffun, skip_short=0):
    out = os.path.join(d, "m.gz")
    S.run(cmd + ["-o", out, "-p", 1, "--quiet"])
    got = read_matrix(out)
    worst, nmis, n = 0.0, 0, 0
    for i, (c, s, e, st) in enumerate(regions):
        if skip_short and e - s < skip_short:
            continue
        g = got.get("r%d" % i)
        r = reffun(c, s, e, st)
        if g is None:
            print("  region r%d missing from output" % i)
            nmis += 1
            continue
        if g.shape != r.shape:
            print("  region r%d: shape %s vs reference %s" % (i, g.shape, r.shape))
            nmis += 1
            continue
        same = np.isclose(g, r, atol=2e-6) | (np.isnan(g) & np.isnan(r))
        nmis += (~same).any()
        n += 1
        worst = max(worst, np.nanmax(np.where(same, 0, np.abs(g - r))) if (~same).any() else 0)
    print("%-72s %s  (%d regions, max |diff| %.1e)" % (name, "OK" if nmis == 0 else "MISMATCH x%d" % nmis, n, worst))


base = ["computeMatrix", "reference-point", "-S", bw, "-R", bed, "-bs", 10, "-b", 300, "-a", 500]
for how in ["mean", "median", "max", "sum", "std"]:
    compare("reference-point TSS -b 300 -a 500 --averageTypeBins %s" % how, base + ["--averageTypeBins", how],
            lambda c, s, e, st, how=how: ref_refpoint(c, s, e, st, 500, 300, 10, how, False, "TSS", False))
compare("reference-point TSS --missingDataAsZero", base + ["--missingDataAsZero"],
        lambda c, s, e, st: ref_refpoint(c, s, e, st, 500, 300, 10, "mean", True, "TSS", False))
compare("reference-point TES", base[:2] + ["--referencePoint", "TES"] + base[2:],
        lambda c, s, e, st: ref_refpoint(c, s, e, st, 500, 300, 10, "mean", False, "TES", False))
compare("reference-point center", base[:2] + ["--referencePoint", "center"] + base[2:],
        lambda c, s, e, st: ref_refpoint(c, s, e, st, 500, 300, 10, "mean", False, "center", False))
compare("reference-point TSS --nanAfterEnd (regions >= 10 bp)", base + ["--nanAfterEnd"],
        lambda c, s, e, st: ref_refpoint(c, s, e, st, 500, 300, 10, "mean", False, "TSS", True), skip_short=10)
print("   (note: the 5-bp region r8 gets NaN in its first downstream bin under --nanAfterEnd; the padding is rounded to whole bins)")
sbase = ["computeMatrix", "scale-regions", "-S", bw, "-R", bed, "-bs", 10, "-b", 200, "-a", 100, "-m", 500]
compare("scale-regions -m 500 -b 200 -a 100 (regions >= 10 bp)", sbase,
        lambda c, s, e, st: ref_scale(c, s, e, st, 100, 200, 500, 10, "mean", False, 0, 0), skip_short=10)
compare("scale-regions --averageTypeBins median", sbase + ["--averageTypeBins", "median"],
        lambda c, s, e, st: ref_scale(c, s, e, st, 100, 200, 500, 10, "median", False, 0, 0), skip_short=10)
compare("scale-regions --unscaled5prime 50 --unscaled3prime 30 (regions >= 100 bp)",
        sbase + ["--unscaled5prime", 50, "--unscaled3prime", 30],
        lambda c, s, e, st: ref_scale(c, s, e, st, 100, 200, 500, 10, "mean", False, 50, 30), skip_short=100)
compare("scale-regions -b 0 -a 0 --missingDataAsZero", ["computeMatrix", "scale-regions", "-S", bw, "-R", bed, "-bs", 10, "-m", 300, "--missingDataAsZero"],
        lambda c, s, e, st: ref_scale(c, s, e, st, 0, 0, 300, 10, "mean", True, 0, 0), skip_short=10)

# --- plotProfile / plotHeatmap --averageType summaries over the matrix -------
out = os.path.join(d, "m.gz")
S.run(base + ["-o", out, "-p", 1, "--quiet"])
got = read_matrix(out)
M = np.array([got["r%d" % i] for i in range(len(regions))])
for how in ["mean", "median", "max", "min", "sum", "std"]:
    tab = os.path.join(d, "prof_%s.tab" % how)
    S.run(["plotProfile", "-m", out, "-o", os.path.join(d, "p.png"), "--averageType", how, "--outFileNameData", tab])
    line = [l for l in open(tab) if l.startswith("s")][0].rstrip("\n").split("\t")
    prof = np.array([float(x) for x in line[2:]])
    ref = np.array([agg(M[:, j], how) for j in range(M.shape[1])])
    print("%-72s %s" % ("plotProfile --averageType %s equals numpy over non-NaN rows" % how,
                        "OK" if np.allclose(prof, ref, atol=1e-5) else "MISMATCH (max |diff| %.2e)" % np.max(np.abs(prof - ref))))
tab = os.path.join(d, "hm.tab")
S.run(["plotHeatmap", "-m", out, "-o", os.path.join(d, "h.png"), "--averageType", "median", "--outFileNameMatrix", tab,
       "--sortRegions", "no"])
with gzip.open(tab, "rt") as fh:                     # plotHeatmap gzips this file
    rows = [l.rstrip("\n").split("\t") for l in fh if not l.startswith("#")]
hm = np.array([[float(x) for x in r[-M.shape[1]:]] for r in rows if len(r) > M.shape[1] and r[0].startswith("chr")])
print("%-72s %s" % ("plotHeatmap --outFileNameMatrix equals the computeMatrix values (4 s.f.)",
                    "OK" if np.allclose(np.nan_to_num(hm), np.nan_to_num(M), rtol=2e-3, atol=1e-3) else "MISMATCH"))
