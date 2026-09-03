#!/usr/bin/env python3
"""DT5: bamCoverage --normalizeUsing BPM produces the CPM track.

getScaleFactor.get_scale_factor computes for BPM
    tpm_scaleFactor = (bam_mapped / tile_len_in_kb) / 1e6
    scale_factor *= 1 / (tpm_scaleFactor * tile_len_in_kb)
which is algebraically 1e6 / bam_mapped, the CPM factor. The help text
defines BPM as "number of reads per bin / sum of all reads per bin (in
millions)"; since a read is counted in every bin it overlaps, the sum of all
reads per bin exceeds the number of mapped reads by the mean number of bins a
read touches, and the documented BPM values would sum to 1e6 over the genome.

Single-end 100-bp reads with 50-bp bins (each read touches 2-3 bins) and, in
a second run, --extendReads 300 (6-7 bins). Compares the CPM and BPM bigWigs
bit for bit and reports the documented BPM value's ratio to the emitted one.
"""
import os
import numpy as np
import _synth as S

print(S.version())
rng = np.random.default_rng(5)
d = S.tmpdir()
L = 300000
BS = 50
reads, frags = S.random_se_reads(rng, 0, L, 20000, 100)
bam = S.write_bam(os.path.join(d, "se.bam"), [("chr1", L)], reads)
counts = S.bin_overlap_counts(frags, L, BS).astype(float)
n = len(frags)

for extra, label in [([], "100-bp reads, no extension"), (["--extendReads", "300"], "--extendReads 300")]:
    tracks = {}
    for norm in ["CPM", "BPM", "RPKM"]:
        out = os.path.join(d, "%s_%d.bw" % (norm, len(extra)))
        S.run(["bamCoverage", "-b", bam, "-o", out, "-bs", BS, "-p", 1, "--normalizeUsing", norm] + extra)
        tracks[norm] = S.read_bigwig_per_base(out, "chr1", L)[::BS]
    if extra:
        ext = [(s, s + 300) if not r else (e - 300, e) for s, e, r in frags]
        ext = [(max(0, s), min(L, e)) for s, e in ext]
        counts = S.bin_overlap_counts(ext, L, BS).astype(float)
    cpm_ref = counts * 1e6 / n
    bpm_doc = counts * 1e6 / counts.sum()
    print("\n%s: mapped reads %d, sum of reads per bin %d (%.2f bins per read)" % (label, n, counts.sum(), counts.sum() / n))
    print("  CPM track equals closed-form CPM: %s (max |diff| %.3g)"
          % (np.allclose(tracks["CPM"], cpm_ref, rtol=1e-5), np.max(np.abs(tracks["CPM"] - cpm_ref))))
    print("  BPM track identical to CPM track: %s (max |diff| %.3g); sum of BPM track over bins = %.0f (documented: 1e6)"
          % (np.array_equal(tracks["BPM"], tracks["CPM"]), np.max(np.abs(tracks["BPM"] - tracks["CPM"])), tracks["BPM"].sum()))
    print("  emitted BPM / documented BPM = %.3f on every covered bin (min %.3f, max %.3f)"
          % (np.median(tracks["BPM"][counts > 0] / bpm_doc[counts > 0]),
             np.min(tracks["BPM"][counts > 0] / bpm_doc[counts > 0]), np.max(tracks["BPM"][counts > 0] / bpm_doc[counts > 0])))
    print("  RPKM track = CPM / (bin length in kb): %s" % np.allclose(tracks["RPKM"], tracks["CPM"] / (BS / 1000.0), rtol=1e-5))
