#!/usr/bin/env python3
"""Held-up checks for bamCoverage: raw counts, --scaleFactor, RPKM, CPM, RPGC,
--ignoreForNormalization, --minMappingQuality, --ignoreDuplicates,
--exactScaling, --extendReads (paired-end), --centerReads,
--minFragmentLength/--maxFragmentLength, --samFlagInclude, --skipNAs.

Every comparison is against a closed form computed from the fragment lists
with numpy (reads per bin = fragments overlapping the bin; scale factors as
documented in the --normalizeUsing help text, with the number of mapped reads
taken after the filters).
"""
import os
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(21)
d = S.tmpdir()
chroms = [("chr1", 400000), ("chr2", 100000)]
BS = 50
RL = 50

# --- single-end BAM with a MAPQ mixture and planted duplicates -------------
reads, frags = [], {"chr1": [], "chr2": []}
mapq = {"chr1": [], "chr2": []}
k = 0
for cid, (cname, L) in enumerate(chroms):
    n = 20000 if cname == "chr1" else 4000
    starts = rng.integers(0, L - RL, n)
    rev = rng.random(n) < 0.5
    q = np.where(rng.random(n) < 0.3, 5, 30)
    for i in range(n):
        reads.append(S.se_read(cid, starts[i], RL, bool(rev[i]), "r%d" % k, mapq=int(q[i])))
        frags[cname].append((int(starts[i]), int(starts[i]) + RL, bool(rev[i])))
        mapq[cname].append(int(q[i]))
        k += 1
        if i % 10 == 0:      # every 10th read gets an exact duplicate (same start, strand)
            reads.append(S.se_read(cid, starts[i], RL, bool(rev[i]), "d%d" % k, mapq=int(q[i])))
            frags[cname].append((int(starts[i]), int(starts[i]) + RL, bool(rev[i])))
            mapq[cname].append(int(q[i]))
            k += 1
bam = S.write_bam(os.path.join(d, "se.bam"), chroms, reads)
n_all = {c: len(frags[c]) for c in frags}
N = sum(n_all.values())


def dedup(fr):
    seen, out = set(), []
    for f in fr:
        key = (f[0], f[2])
        if key in seen:
            continue
        seen.add(key)
        out.append(f)
    return out


def track(extra, fmt="bigwig"):
    out = os.path.join(d, "t%d.%s" % (abs(hash(tuple(extra))) % 10**8, "bw" if fmt == "bigwig" else "bg"))
    S.run(["bamCoverage", "-b", bam, "-o", out, "-bs", BS, "-p", 1, "-of", fmt] + extra)
    if fmt == "bigwig":
        return {c: S.read_bigwig_per_base(out, c, L)[::BS] for c, L in chroms}
    bg = S.read_bedgraph(out)
    return {c: S.bedgraph_to_per_base(bg, c, L)[::BS] for c, L in chroms}


def report(name, got, ref):
    ok, worst = True, 0.0
    for c, L in chroms:
        g, r = np.nan_to_num(got[c]), ref[c]
        rel = np.max(np.abs(g - r) / np.maximum(np.abs(r), 1e-12))
        worst = max(worst, rel)
        ok &= np.allclose(g, r, rtol=1e-6, atol=1e-9)
    print("%-62s %s   (max rel diff %.2e)" % (name, "OK" if ok else "MISMATCH", worst))


counts = {c: S.bin_overlap_counts(frags[c], L, BS).astype(float) for c, L in chroms}
report("raw counts (reads overlapping each bin)", track([]), counts)
report("--scaleFactor 2.5", track(["--scaleFactor", "2.5"]), {c: 2.5 * counts[c] for c in counts})
report("CPM = counts * 1e6 / mapped", track(["--normalizeUsing", "CPM"]), {c: counts[c] * 1e6 / N for c in counts})
report("RPKM = counts / (mapped/1e6 * binsize/1e3)", track(["--normalizeUsing", "RPKM"]),
       {c: counts[c] / (N / 1e6 * BS / 1e3) for c in counts})
EGS = 450000
report("RPGC = counts * EGS / (mapped * read length)", track(["--normalizeUsing", "RPGC", "--effectiveGenomeSize", EGS]),
       {c: counts[c] * EGS / (N * RL) for c in counts})
report("CPM --ignoreForNormalization chr2 (chr2 excluded from mapped and from output)",
       track(["--normalizeUsing", "CPM", "--ignoreForNormalization", "chr2"]),
       {"chr1": counts["chr1"] * 1e6 / n_all["chr1"], "chr2": np.zeros_like(counts["chr2"])})

# filters: mapped-after-filter counts (small genome: fraction_kept scans it all)
hq = {c: [f for f, q in zip(frags[c], mapq[c]) if q >= 10] for c in frags}
Nhq = sum(len(v) for v in hq.values())
report("--minMappingQuality 10 CPM (mapped = reads with MAPQ >= 10)",
       track(["--normalizeUsing", "CPM", "--minMappingQuality", "10"]),
       {c: S.bin_overlap_counts(hq[c], L, BS) * 1e6 / Nhq for c, L in chroms})
report("--minMappingQuality 10 --exactScaling CPM",
       track(["--normalizeUsing", "CPM", "--minMappingQuality", "10", "--exactScaling"]),
       {c: S.bin_overlap_counts(hq[c], L, BS) * 1e6 / Nhq for c, L in chroms})
dd = {c: dedup(frags[c]) for c in frags}
Ndd = sum(len(v) for v in dd.values())
report("--ignoreDuplicates CPM (one read per start+strand)",
       track(["--normalizeUsing", "CPM", "--ignoreDuplicates"]),
       {c: S.bin_overlap_counts(dd[c], L, BS) * 1e6 / Ndd for c, L in chroms})
fwd = {c: [f for f in frags[c] if not f[2]] for c in frags}
Nf = sum(len(v) for v in fwd.values())
report("--samFlagExclude 16 CPM (forward-strand reads only)",
       track(["--normalizeUsing", "CPM", "--samFlagExclude", "16"]),
       {c: S.bin_overlap_counts(fwd[c], L, BS) * 1e6 / Nf for c, L in chroms})
got = track(["--skipNAs"], fmt="bedgraph")
ref = {c: counts[c].copy() for c in counts}
print("%-62s %s" % ("--skipNAs: zero bins absent, others equal counts",
                     "OK" if all(np.array_equal(np.nan_to_num(got[c]), ref[c]) and np.all(np.isnan(got[c][ref[c] == 0])) for c in ref) else "MISMATCH"))

# --- paired-end BAM ---------------------------------------------------------
pe_reads, pe_frags = S.random_pe_pairs(rng, 0, 400000, 8000, RL, [120, 150, 180, 210, 240, 400])
pe = S.write_bam(os.path.join(d, "pe.bam"), chroms, pe_reads)
Lc = 400000
n_mates = 2 * len(pe_frags)
med_fl = float(np.median([e - s for s, e in pe_frags]))


def petrack(extra):
    out = os.path.join(d, "pe%d.bw" % (abs(hash(tuple(extra))) % 10**8))
    S.run(["bamCoverage", "-b", pe, "-o", out, "-bs", BS, "-p", 1] + extra)
    return {"chr1": S.read_bigwig_per_base(out, "chr1", Lc)[::BS], "chr2": np.zeros(2000)}


both = {"chr1": 2.0 * S.bin_overlap_counts(pe_frags, Lc, BS), "chr2": np.zeros(2000)}
mates = [(s, s + RL) for s, e in pe_frags] + [(e - RL, e) for s, e in pe_frags]
report("paired-end, no extension: each mate counted as a read",
       petrack([]), {"chr1": S.bin_overlap_counts(mates, Lc, BS).astype(float), "chr2": np.zeros(2000)})
report("paired-end --extendReads: fragment counted once per mate (2x)", petrack(["--extendReads"]), both)
report("paired-end --extendReads RPGC = 2*frags*EGS/(2*frags*median fraglen)",
       petrack(["--extendReads", "--normalizeUsing", "RPGC", "--effectiveGenomeSize", EGS]),
       {"chr1": both["chr1"] * EGS / (n_mates * med_fl), "chr2": np.zeros(2000)})
cen = [((s + e) // 2 - RL // 2, (s + e) // 2 - RL // 2 + RL) for s, e in pe_frags]
report("paired-end --extendReads --centerReads: read-length window at fragment centre, 2x",
       petrack(["--extendReads", "--centerReads"]), {"chr1": 2.0 * S.bin_overlap_counts(cen, Lc, BS), "chr2": np.zeros(2000)})
sel = [(s, e) for s, e in pe_frags if 150 <= e - s <= 210]
report("--minFragmentLength 150 --maxFragmentLength 210 --extendReads",
       petrack(["--extendReads", "--minFragmentLength", "150", "--maxFragmentLength", "210"]),
       {"chr1": 2.0 * S.bin_overlap_counts(sel, Lc, BS), "chr2": np.zeros(2000)})
report("--extendReads --samFlagInclude 64 (first mates only): fragments once",
       petrack(["--extendReads", "--samFlagInclude", "64"]),
       {"chr1": S.bin_overlap_counts(pe_frags, Lc, BS).astype(float), "chr2": np.zeros(2000)})
report("--extendReads --samFlagInclude 64 CPM: mapped = first mates after filter",
       petrack(["--extendReads", "--samFlagInclude", "64", "--normalizeUsing", "CPM"]),
       {"chr1": S.bin_overlap_counts(pe_frags, Lc, BS) * 1e6 / len(pe_frags), "chr2": np.zeros(2000)})
