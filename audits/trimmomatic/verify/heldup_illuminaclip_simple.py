#!/usr/bin/env python3
"""Held-up checks and notes for ILLUMINACLIP simple mode: clip position on reads carrying a
known adapter (full or 3'-truncated, with sequencing errors), how short a 3' adapter
fragment can be and still be found, adapters shorter than the 16-base seed, adapters
overhanging the 5' end. Shipped build vs the documented sum-of-scores rule and vs a port of
the shipped best-sub-range scoring (tm_ref.simple_clip).

Usage: python3 heldup_illuminaclip_simple.py <trimmomatic.jar | build-dir> [adapters-dir]
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tm_ref as T

build = T.build_from_arg(sys.argv[1])
adir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(sys.argv[1].rstrip("/")), "adapters")
AD = os.path.join(adir, "TruSeq3-SE.fa")
ads = dict(T.load_fasta(AD)); IDX, UNI = ads["TruSeq3_IndexedAdapter"], ads["TruSeq3_UniversalAdapter"]
print("build:", " ".join(build)); print("adapters:", AD, {k: len(v) for k, v in ads.items()})

def qual_profile(rng, R):
    return [rng.choice([40, 40, 37, 37, 32, 27]) if i < R * 0.6 else rng.choice([37, 32, 27, 22, 14, 11, 2]) for i in range(R)]

def ref_len(seq, quals, thr, mode):
    """Clip position of the documented (mode='doc') or best-sub-range (mode='code') rule over
    both adapters: the smallest keep-length wins (as processRecords takes the minimum)."""
    best = None
    for a in (IDX, UNI):
        k = T.simple_clip(seq, quals, a, 2, thr, mode=mode, min_overlap=T.code_min_overlap(thr))
        if k is not None and (best is None or k < best): best = k
    return best

# ---------------------------------------------------------------- A. adapters at random positions with errors
print("\nA. 6,000 reads of 150 nt: 60% carry TruSeq3_IndexedAdapter, 20% the universal adapter, 20% none; adapter starts at a")
print("   random position 10-149 (truncated at the read end); per-base sequencing errors at rate 10^(-Q/10):")
for thr in (10, 7, 15):
    rng = random.Random(100 + thr)
    reads, truth = [], {}
    for k in range(6000):
        u = rng.random()
        ad = IDX if u < 0.6 else (UNI if u < 0.8 else None)
        R = 150
        seq = list(T.rand_seq(rng, R)); pos = None
        if ad:
            pos = rng.randint(10, 149)
            for i, b in enumerate(ad):
                if pos + i < R: seq[pos + i] = b
        quals = qual_profile(rng, R)
        for i in range(R):
            if rng.random() < 10 ** (-quals[i] / 10.0): seq[i] = T.mutate(rng, seq[i])
        name = "r%d" % k
        reads.append((name, "".join(seq), quals)); truth[name] = pos
    step = "ILLUMINACLIP:%s:2:30:%d" % (AD, thr)
    res, log, d = T.run_se(build, reads, [step])
    eq_doc = eq_code = tp = fp = fn = 0; n_with = n_frag16 = 0
    ex = []
    for name, seq, quals in reads:
        got = len(res[name][0]) if name in res else 0
        rd = ref_len(seq, quals, thr, "doc"); rc = ref_len(seq, quals, thr, "code")
        rd = 150 if rd is None else rd; rc = 150 if rc is None else rc
        eq_doc += got == rd; eq_code += got == rc
        if got != rd and len(ex) < 3: ex.append((name, truth[name], got, rd, rc))
        pos = truth[name]
        if pos is not None:
            n_with += 1
            if 150 - pos >= 16: n_frag16 += 1
            if got == pos: tp += 1
            elif got == 150: fn += 1
        elif got != 150: fp += 1
    print("   threshold %-3d shipped == documented-sum rule %d/6000, == best-sub-range port %d/6000; adapter reads clipped exactly at the adapter start %d/%d (%d have >= 16 adapter bases), missed %d; adapter-free reads clipped %d/%d%s"
          % (thr, eq_doc, eq_code, tp, n_with, n_frag16, fn, fp, 6000 - n_with, ("; e.g. (name, adapter pos, shipped, doc, port): " + str(ex)) if ex else ""))

# ---------------------------------------------------------------- B. 3' fragment length sweep
print("\nB. 3' adapter fragments: 200 error-free reads (Q37) of 100 nt whose last k bases are the first k bases of TruSeq3_IndexedAdapter:")
print("   %-4s %-30s %-30s %-30s %s" % ("k", "thr 7 clipped/200 (doc: k*0.602>=7 & k>11)", "thr 10 (k>15)", "thr 15 (k>15)", "score k*0.602"))
for k in range(4, 26):
    rng = random.Random(k)
    reads = [("f%d" % j, T.rand_seq(rng, 100 - k) + IDX[:k], [37] * 100) for j in range(200)]
    row = "   %-4d" % k
    for thr in (7, 10, 15):
        res, log, d = T.run_se(build, reads, ["ILLUMINACLIP:%s:2:30:%d" % (AD, thr)])
        clipped = sum(1 for n, s, q in reads if len(res[n][0]) == 100 - k)
        doc = 200 if (k * T.LOG10_4 >= thr and k > T.code_min_overlap(thr)) else 0
        row += "%-30s" % ("%d (doc %d)" % (clipped, doc))
    print(row + "%.2f" % (k * T.LOG10_4))

# ---------------------------------------------------------------- C. adapter shorter than the 16-base seed
print("\nC. a 12-nt adapter (AGATCGGAAGAG) in a custom FASTA, placed at position 80 of 100-nt Q37 reads:")
d12 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_short12.fa")
with open(d12, "w") as fh: fh.write(">short12\nAGATCGGAAGAG\n")
for thr in (5, 7, 8, 10):
    rng = random.Random(thr)
    reads = [("s%d" % j, T.rand_seq(rng, 80) + "AGATCGGAAGAG" + T.rand_seq(rng, 8), [37] * 100) for j in range(200)]
    res, log, d = T.run_se(build, reads, ["ILLUMINACLIP:%s:2:30:%d" % (d12, thr)])
    clipped = sum(1 for n, s, q in reads if len(res[n][0]) == 80)
    print("   threshold %-3d clipped at 80: %d/200 (12 matches score %.2f; code minimum overlap %d)" % (thr, clipped, 12 * T.LOG10_4, T.code_min_overlap(thr) + 1))
os.remove(d12)

# ---------------------------------------------------------------- D. adapter overhanging the 5' end
print("\nD. reads that start inside the adapter (adapter[10:] + 50 random bases, Q37), ILLUMINACLIP:...:2:30:10:")
rng = random.Random(4)
reads = [("o%d" % j, IDX[10:] + T.rand_seq(rng, 50), [37] * (len(IDX) - 10 + 50)) for j in range(200)]
res, log, d = T.run_se(build, reads, ["ILLUMINACLIP:%s:2:30:10" % AD])
print("   surviving reads:", len(res), "of 200 |", T.summary_line(log), "(clip offset <= 0 drops the read)")
reads = [("m%d" % j, T.rand_seq(rng, 20) + IDX + T.rand_seq(rng, 20), [37] * (len(IDX) + 40)) for j in range(200)]
res, log, d = T.run_se(build, reads, ["ILLUMINACLIP:%s:2:30:10" % AD])
print("   20 random + full adapter + 20 random: kept exactly 20 bases for %d/200" % sum(1 for n, s, q in reads if len(res[n][0]) == 20))
