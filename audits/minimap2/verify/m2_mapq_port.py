"""M2: MAPQ of reads without a competing hit, against a Python port of the
documented-in-code formula (hit.c mm_set_mapq2), for -x sr and map-ont.

For a primary with s2:i:0 no overlapping secondary existed at either
mm_set_parent pass, so dp_max2 = 0 and n_sub = 0, and the MAPQ is

  uniq   = s1 / (s1 + rl)
  pen_cm = min( (s1 > 100 ? 1 : s1/100) * uniq , cm > 10 ? 1 : cm/10 )
  mapq   = int( mlen/blen * pen_cm * 40 * (1 - max(s2, min_chain_score)/s1) * ln(ms/A) )
  (long reads only) mapq = min(mapq, int(6.02 * (mlen/blen)^2 * ms / A + .499))
  mapq   = clamp(mapq, 0, 60); 1 if it is 0 (dp_max > dp_max2)

with s1, s2, cm, rl, ms and mlen/blen (PAF columns 10 and 11) read from the
record. Reads: 40-150 bp with 0-8 mismatches (sr) and 150-1500 bp ONT-like
reads (map-ont) from a random reference, so most chains are short enough for
the s1 and cm penalties to bite.
"""
import os, sys, random, math, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(41)
G = 3000000
ref = rand_seq(rng, G)
d = tmpdir(); fa = os.path.join(d, "ref.fa"); write_fasta(fa, [("chr1", ref)])
print(version(), f" reference {G} bp random")


def f32(x):  # the C code computes in float; emulate the rounding that matters
    import struct
    return struct.unpack("f", struct.pack("f", x))[0]


def port(r, min_chain, A, is_sr):
    s1, s2, cm, rl, ms = r["tags"]["s1"], r["tags"]["s2"], r["tags"]["cm"], r["tags"]["rl"], r["tags"]["ms"]
    uniq = f32(s1 / (s1 + rl))
    pen_s1 = f32((1.0 if s1 > 100 else f32(0.01 * s1)) * uniq)
    pen_cm = 1.0 if cm > 10 else f32(0.1 * cm)
    pen_cm = min(pen_s1, pen_cm)
    subsc = max(s2, min_chain)
    ident = f32(r["nmatch"] / r["blen"])
    x = f32(subsc / s1)
    mapq = int(f32(f32(f32(ident * pen_cm) * 40.0) * f32(1.0 - x)) * f32(math.log(f32(ms / A))))
    if not is_sr:
        alt = int(f32(6.02 * ident * ident * ms / A) + .499)
        mapq = min(mapq, alt)
    mapq = max(mapq, 0); mapq = min(mapq, 60)
    if mapq == 0: mapq = 1
    return mapq


for label, args, min_chain, A, is_sr, gen in (
        ("-x sr", ["-x", "sr", "-c"], 25, 2, True, "sr"),
        ("map-ont", ["-x", "map-ont", "-c"], 40, 2, False, "ont")):
    reads = []
    for i in range(1500):
        if gen == "sr":
            L = rng.choice([40, 50, 60, 75, 100, 150]); st = rng.randint(0, G - L)
            s = mutate(rng, ref[st:st + L], n_sub=rng.randint(0, min(8, L // 10)), protect=5)
        else:
            L = rng.choice([150, 200, 300, 500, 800, 1500]); st = rng.randint(0, G - L)
            s = noisy(rng, ref[st:st + L], sub=rng.choice([.01, .03, .06]), ins=.02, dele=.02)
        if rng.random() < .5: s = revcomp(s)
        reads.append((f"r{i}_L{L}", s))
    fq = os.path.join(d, f"{gen}.fq"); write_fastq(fq, reads)
    recs = parse_paf(run(args + ["-t1", fa, fq]))
    per = collections.Counter(r["qname"] for r in recs)
    tested = ok = 0; diffs = []; hist = collections.Counter()
    for r in recs:
        if per[r["qname"]] != 1 or r["tags"].get("tp") != "P" or r["tags"].get("s2", 0) != 0:
            continue
        tested += 1
        p = port(r, min_chain, A, is_sr)
        hist[min(r["mapq"] // 10 * 10, 60)] += 1
        if p == r["mapq"]: ok += 1
        else: diffs.append((r["qname"], r["mapq"], p, r["tags"]["s1"], r["tags"]["cm"], r["tags"]["ms"], r["nmatch"], r["blen"]))
    print(f"\n[{label}] {len(reads)} reads, {len(recs)} records; {tested} single primaries with s2:i:0")
    print(f"  MAPQ distribution of the tested records (decades): {dict(sorted(hist.items()))}")
    print(("  ok   " if not diffs else "  FAIL ") + f"MAPQ matches the port on {ok}/{tested}"
          + ("" if not diffs else f"; differing (name, mapq, port, s1, cm, ms, mlen, blen): {diffs[:6]}"))
