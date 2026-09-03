#!/usr/bin/env python3
"""Held-up checks, executed: closest, genomecov (BED and BAM) and multicov against
independent Python ports. BAM inputs are written with pysam from synthetic reads.

  closest    -d, -D ref/a/b sign conventions, -io, -s/-S, -k, -N, ties (-t all),
             -mdb each/all with two -b files
  genomecov  BED: default histogram, -bg, -bga, -d, -dz, -max, -scale, -strand,
             -5/-3 on stranded records, -split with BED12
             BAM: default (N counted as covered), -split (N splits, D covered),
             -ignoreD, -pc, -fs, -du with -strand, -5/-3
  multicov   -q, -p, -D, -F, -s/-S, -f, -r, -split (fraction semantics recorded)
"""
import os, random, sys, tempfile
import numpy as np
import pysam
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version(), "pysam", pysam.__version__)
rng = random.Random(99)
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed"); B2 = os.path.join(tmp, "b2.bed"); G = os.path.join(tmp, "g.genome")
fails = 0
def report(label, ok, detail=""):
    global fails
    fails += not ok
    print("   %-62s %s %s" % (label, "ok" if ok else "MISMATCH", detail))

# ------------------------------------------------------------------ closest
print("\n== closest (300 A, 600 B, two chromosomes, strands)")
def rand_rows(n, prefix, dup=0.0):
    rows = []
    for i in range(n):
        c = rng.choice(["chr1", "chr1", "chr2"]); L = rng.randint(1, 300); s = rng.randint(0, 100000 - L)
        rows.append([c, s, s + L, "%s%d" % (prefix, i), 0, rng.choice("++--.")])
    return sorted_bed(rows)
arows = rand_rows(300, "a"); brows = rand_rows(600, "b"); b2rows = rand_rows(200, "c")
write(A, arows); write(B, brows); write(B2, b2rows)
S = {"+": 1, "-": -1, ".": 0}

def closest_port(a, bs, mode=None, io=False, s=False, S_=False, k=1, N=False):
    a0, a1 = int(a[1]), int(a[2]); cands = []
    for b in bs:
        if b[0] != a[0]: continue
        if s and not (S[a[5]] != 0 and S[a[5]] == S[b[5]]): continue
        if S_ and not (S[a[5]] != 0 and S[b[5]] != 0 and S[a[5]] != S[b[5]]): continue
        if N and a[3] == b[3]: continue
        b0, b1 = int(b[1]), int(b[2])
        if overlap(a0, a1, b0, b1) > 0 or (a0 == a1 and b0 <= a0 <= b1) or (b0 == b1 and a0 <= b0 <= a1):
            if io: continue
            cands.append((0, b[3], 0))
        elif b0 >= a1:      # right
            d = b0 - a1 + 1
            up = (mode == "a" and a[5] == "-") or (mode == "b" and b[5] == "+")
            cands.append((d, b[3], -d if up else d))
        else:               # left
            d = a0 - b1 + 1
            up = not ((mode == "a" and a[5] == "-") or (mode == "b" and b[5] == "+"))
            cands.append((d, b[3], -d if up else d))
    cands.sort()
    out, used_d = [], []
    for d, name, sd in cands:
        if len(used_d) >= k and d not in used_d: break
        if d not in used_d: used_d.append(d)
        out.append((name, sd))
    return set(out)

for label, args, kw in (("-d", ["-d"], {}), ("-D ref", ["-D", "ref"], dict(mode="ref")), ("-D a", ["-D", "a"], dict(mode="a")), ("-D b", ["-D", "b"], dict(mode="b")),
                        ("-d -io", ["-d", "-io"], dict(io=True)), ("-d -s", ["-d", "-s"], dict(s=True)), ("-d -S", ["-d", "-S"], dict(S_=True)),
                        ("-d -k 3", ["-d", "-k", "3"], dict(k=3)), ("-D a -io -s", ["-D", "a", "-io", "-s"], dict(mode="a", io=True, s=True))):
    out = lines(run(["closest", "-a", A, "-b", B, *args]))
    got = {}
    for l in out:
        if l[6] != ".": got.setdefault(l[3], set()).add((l[9], int(l[12])))
    ref = {a[3]: closest_port(a, brows, **kw) for a in arows}; ref = {k_: v for k_, v in ref.items() if v}
    bad = [k_ for k_ in set(got) | set(ref) if got.get(k_) != ref.get(k_)]
    report("closest %s (all ties, signed distance)" % label, not bad, "" if not bad else "e.g. %s got %s ref %s" % (bad[0], got.get(bad[0]), ref.get(bad[0])))
out = lines(run(["closest", "-a", A, "-b", B, B2, "-d", "-mdb", "each"]))
got = {}
for l in out:
    if l[7] != ".": got.setdefault((l[3], l[6]), set()).add((l[10], int(l[13])))
ref = {}
for a in arows:
    for fid, bs in (("1", brows), ("2", b2rows)):
        r = closest_port(a, bs)
        if r: ref[(a[3], fid)] = r
report("closest -mdb each with two -b files", got == ref)
out = lines(run(["closest", "-a", A, "-b", B, B2, "-d", "-mdb", "all"]))
got = {}
for l in out:
    if l[7] != ".": got.setdefault(l[3], set()).add((l[6], l[10], int(l[13])))
ref = {}
for a in arows:
    c = [(d, "1", n, sd) for n, sd in closest_port(a, brows) for d in [abs(sd)]] + [(d, "2", n, sd) for n, sd in closest_port(a, b2rows) for d in [abs(sd)]]
    if c:
        m = min(x[0] for x in c); ref[a[3]] = {(f, n, sd) for d, f, n, sd in c if d == m}
report("closest -mdb all with two -b files", got == ref)
write(B, [["chr1", 10, 20, "same", 0, "+"], ["chr1", 30, 40, "other", 0, "+"]]); write(A, [["chr1", 10, 20, "same", 0, "+"]])
report("closest -N (skip same name)", lines(run(["closest", "-a", A, "-b", B, "-N", "-d"]))[0][9:] == ["other", "0", "+", "11"])

# ------------------------------------------------------------------ genomecov BED
print("\n== genomecov on BED (chr1 20000, chr2 8000; 400 records incl. duplicates and book-ended)")
write(G, [["chr1", 20000], ["chr2", 8000], ["chr3", 500]])
rows = []
for i in range(400):
    c = rng.choice(["chr1", "chr1", "chr2"]); cs = 20000 if c == "chr1" else 8000; L = rng.randint(1, 400); s = rng.randint(0, cs - L)
    rows.append([c, s, s + L, "r%d" % i, 0, rng.choice("+-")])
rows = sorted_bed(rows); write(B, rows)
def depth(rows, sizes, pick=None):
    d = {c: np.zeros(n, dtype=np.int64) for c, n in sizes.items()}
    for r in rows:
        s, e = int(r[1]), int(r[2])
        if pick == "5": s, e = (s, s + 1) if r[5] == "+" else (e - 1, e)
        if pick == "3": s, e = (e - 1, e) if r[5] == "+" else (s, s + 1)
        d[r[0]][s:e] += 1
    return d
sizes = {"chr1": 20000, "chr2": 8000, "chr3": 500}
def bg_port(d, all_=False, mx=None, scale=None):
    out = []
    for c in ("chr1", "chr2", "chr3"):
        arr = d[c]; i = 0
        while i < len(arr):
            j = i
            while j < len(arr) and arr[j] == arr[i]: j += 1
            v = int(arr[i])
            if v > 0 or all_:
                if mx is not None and v >= mx: v = mx
                out.append((c, i, j, v if scale is None else v * scale))
            i = j
    return out
d = depth(rows, sizes)
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-bg"]))]
report("-bg", got == bg_port(d))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-bga"]))]
report("-bga (zero regions, empty chr3 included)", got == bg_port(d, all_=True))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-bg", "-max", "3"]))]
report("-bg -max 3 (bedgraph caps at max)", got == bg_port(d, mx=3))
got = [(l[0], int(l[1]), int(l[2]), float(l[3])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-bg", "-scale", "0.25"]))]
report("-bg -scale 0.25", got == bg_port(d, scale=0.25))
got = [(l[0], int(l[1]), int(l[2])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-d"]))]
ref = [(c, i + 1, int(v)) for c in ("chr1", "chr2", "chr3") for i, v in enumerate(d[c])]
report("-d (1-based, every position)", got == ref)
got = [(l[0], int(l[1]), int(l[2])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-dz"]))]
report("-dz (0-based, non-zero only)", got == [(c, i, int(v)) for c in ("chr1", "chr2", "chr3") for i, v in enumerate(d[c]) if v > 0])
out = lines(run(["genomecov", "-i", B, "-g", G]))
ok = True
for c in ("chr1", "chr2", "chr3"):
    h = np.bincount(d[c]); ref = {i: int(n) for i, n in enumerate(h) if n > 0}
    got = {int(l[1]): int(l[2]) for l in out if l[0] == c}
    ok &= got == ref and all(int(l[3]) == sizes[c] and l[4] == "%g" % float(np.float32(int(l[2])) / np.float32(sizes[c])) for l in out if l[0] == c)
allh = np.bincount(np.concatenate([d[c] for c in sizes]))
got = {int(l[1]): int(l[2]) for l in out if l[0] == "genome"}
ok &= got == {i: int(n) for i, n in enumerate(allh) if n > 0} and all(int(l[3]) == 28500 for l in out if l[0] == "genome")
report("default histogram per chromosome and genome (float32 fraction, %g)", ok)
out = lines(run(["genomecov", "-i", B, "-g", G, "-max", "2"]))
h = np.bincount(np.minimum(d["chr1"], 2)); report("histogram -max 2 (>= max pooled)", {int(l[1]): int(l[2]) for l in out if l[0] == "chr1"} == {i: int(n) for i, n in enumerate(h) if n > 0})
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-bg", "-strand", "-"]))]
report("-bg -strand -", got == bg_port(depth([r for r in rows if r[5] == "-"], sizes)))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-bg", "-5"]))]
report("-bg -5 (stranded records)", got == bg_port(depth(rows, sizes, "5")))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-i", B, "-g", G, "-bg", "-3"]))]
report("-bg -3 (stranded records)", got == bg_port(depth(rows, sizes, "3")))
# -split with BED12
b12 = []
for i in range(200):
    blocks = rand_blocks(rng, rng.choice([1, 2, 3]), 5, 80, 5, 400); st = rng.randint(0, 20000 - blocks[-1][0] - blocks[-1][1])
    b12.append(bed12("chr1", st, blocks, "s%d" % i))
b12 = sorted_bed(b12); write(B2, b12)
def blocks_rows(r):
    st = int(r[1]); return [["chr1", st + o, st + o + s, "", 0, "+"] for o, s in zip((int(x) for x in r[11].split(",")), (int(x) for x in r[10].split(",")))]
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-i", B2, "-g", G, "-bg", "-split"]))]
report("-bg -split on BED12 (blocks only)", got == bg_port(depth([b for r in b12 for b in blocks_rows(r)], sizes)))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-i", B2, "-g", G, "-bg"]))]
report("-bg on BED12 without -split (whole span)", got == bg_port(depth(b12, sizes)))

# ------------------------------------------------------------------ genomecov BAM
print("\n== genomecov on BAM (pysam-written: single reads with M/N/D/I/S, proper pairs)")
BAM = os.path.join(tmp, "r.bam")
hdr = {"HD": {"VN": "1.6", "SO": "coordinate"}, "SQ": [{"LN": 20000, "SN": "chr1"}, {"LN": 8000, "SN": "chr2"}]}
reads = []   # (chrom, pos, cigar tuples, reverse, pair info)
def cig_blocks(pos, cig, split_N, split_D):
    """reference blocks covered by a CIGAR; N (and D when split) break blocks"""
    blocks, cur, p = [], pos, pos
    for op, ln in cig:
        if op in (0, 7, 8): p += ln
        elif op == 2: 
            if split_D: blocks.append((cur, p)); p += ln; cur = p
            else: p += ln
        elif op == 3:
            if split_N: blocks.append((cur, p)); p += ln; cur = p
            else: p += ln
    blocks.append((cur, p))
    return [(s, e) for s, e in blocks if e > s]
with pysam.AlignmentFile(BAM, "wb", header=hdr) as f:
    n = 0
    for i in range(300):   # single-end reads
        tid = rng.choice([0, 0, 1]); ln = 20000 if tid == 0 else 8000
        cig = [(4, 3)] if rng.random() < 0.3 else []
        cig.append((0, rng.randint(20, 60)))
        r = rng.random()
        if r < 0.3: cig += [(3, rng.randint(50, 500)), (0, rng.randint(20, 60))]
        elif r < 0.5: cig += [(2, rng.randint(1, 5)), (0, rng.randint(10, 40))]
        elif r < 0.6: cig += [(1, 2), (0, 10)]
        reflen = sum(l for op, l in cig if op in (0, 2, 3))
        pos = rng.randint(0, ln - reflen - 1)
        a = pysam.AlignedSegment(); a.query_name = "s%d" % i; a.reference_id = tid; a.reference_start = pos; a.cigar = cig
        a.query_sequence = "A" * sum(l for op, l in cig if op in (0, 1, 4)); a.mapping_quality = rng.choice([0, 5, 20, 60]); a.is_reverse = rng.random() < 0.5
        a.flag |= 0x400 if rng.random() < 0.1 else 0; a.flag |= 0x200 if rng.random() < 0.05 else 0
        reads.append(("chr1" if tid == 0 else "chr2", pos, cig, a.is_reverse, None, a.mapping_quality, bool(a.flag & 0x400), bool(a.flag & 0x200), a.query_name)); n += 1
        f.write(a)
    for i in range(200):   # proper pairs: forward first mate + reverse second mate (or swapped)
        tid = 0; L1, L2 = rng.randint(30, 60), rng.randint(30, 60); frag = rng.randint(120, 400); pos = rng.randint(0, 20000 - frag - 1)
        first_fwd = rng.random() < 0.5
        for mate in (1, 2):
            a = pysam.AlignedSegment(); a.query_name = "p%d" % i; a.reference_id = tid
            fwd = (mate == 1) == first_fwd
            a.reference_start = pos if fwd else pos + frag - (L1 if mate == 1 else L2)
            a.cigar = [(0, L1 if mate == 1 else L2)]; a.query_sequence = "C" * (L1 if mate == 1 else L2); a.mapping_quality = 60
            a.is_paired = True; a.is_proper_pair = True; a.is_reverse = not fwd; a.mate_is_reverse = fwd
            a.is_read1 = mate == 1; a.is_read2 = mate == 2; a.next_reference_id = tid
            a.next_reference_start = pos + frag - (L2 if mate == 1 else L1) if fwd else pos
            a.template_length = frag if fwd else -frag
            reads.append(("chr1", a.reference_start, a.cigar, a.is_reverse, (mate, pos, frag, first_fwd), 60, False, False, a.query_name))
            f.write(a)
pysam.sort("-o", BAM + ".s.bam", BAM); os.replace(BAM + ".s.bam", BAM); pysam.index(BAM)
def bam_depth(split_N, split_D, mode=None, strand=None, du=False):
    d = {c: np.zeros(n_, dtype=np.int64) for c, n_ in (("chr1", 20000), ("chr2", 8000))}
    for c, pos, cig, rev, pair, mq, dup, qc, name in reads:
        eff_rev = rev
        if du and pair and pair[0] == 2: eff_rev = not rev
        if strand is not None and (strand == "-") != eff_rev: continue
        if mode == "pc":
            if not pair: continue   # unpaired reads are skipped by the -pc branch? see below
            mate, p0, frag, first_fwd = pair
            if mate != 1: continue
            d[c][p0:p0 + frag] += 1; continue
        if mode and mode.startswith("fs"):
            fs = int(mode[2:]); end = pos + sum(l for op, l in cig if op in (0, 2, 3))
            if rev: d[c][max(0, end - fs):end] += 1
            else: d[c][pos:pos + fs] += 1
            continue
        if mode == "5" or mode == "3":
            end = pos + sum(l for op, l in cig if op in (0, 2, 3)) - 1
            p = (pos if not rev else end) if mode == "5" else (end if not rev else pos)
            d[c][p] += 1; continue
        for s, e in cig_blocks(pos, cig, split_N, split_D): d[c][s:e] += 1
    return d
sizes2 = {"chr1": 20000, "chr2": 8000}
def bg2(d): return [(c, s, e, v) for c, s, e, v in bg_port({**d, "chr3": np.zeros(0, dtype=np.int64)}) if c != "chr3"]
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg"]))]
report("BAM -bg (N and D counted as covered, I/S not)", got == bg2(bam_depth(False, False)))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg", "-split"]))]
report("BAM -bg -split (N splits, D covered)", got == bg2(bam_depth(True, False)))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg", "-split", "-ignoreD"]))]
report("BAM -bg -split -ignoreD (N and D split)", got == bg2(bam_depth(True, True)))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg", "-strand", "-"]))]
report("BAM -bg -strand -", got == bg2(bam_depth(False, False, strand="-")))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg", "-strand", "-", "-du"]))]
report("BAM -bg -strand - -du (second mates flipped)", got == bg2(bam_depth(False, False, strand="-", du=True)))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg", "-5"]))]
report("BAM -bg -5", got == bg2(bam_depth(False, False, mode="5")))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg", "-3"]))]
report("BAM -bg -3", got == bg2(bam_depth(False, False, mode="3")))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg", "-fs", "150"]))]
report("BAM -bg -fs 150 (reads extended to 150 bp from their 5' end)", got == bg2(bam_depth(False, False, mode="fs150")))
got = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in lines(run(["genomecov", "-ibam", BAM, "-bg", "-pc"]))]
ref_pairs_only = bg2(bam_depth(False, False, mode="pc"))
# genomeCoverageBed.cpp:301-334: with -pc, unpaired reads fall through no branch, so they add nothing
report("BAM -bg -pc (one fragment per proper pair; unpaired reads contribute nothing)", got == ref_pairs_only)

# ------------------------------------------------------------------ multicov
print("\n== multicov on the same BAM (100 BED intervals)")
ivs = sorted_bed([["chr1" if rng.random() < 0.8 else "chr2", s, s + rng.randint(20, 600), "i%d" % i, 0, rng.choice("+-")] for i, s in enumerate(rng.randint(0, 7000) for _ in range(100))])
write(A, ivs)
def mc_port(iv, q=0, p=False, D=False, F=False, s=False, S_=False, f=0.0, r=False, split=False):
    c, s0, e0, _, _, st = iv; s0, e0 = int(s0), int(e0); n = 0
    for rc, pos, cig, rev, pair, mq, dup, qc, name in reads:
        if rc != c: continue
        if mq < q or (dup and not D) or (qc and not F) or (p and not pair): continue
        rs = "-" if rev else "+"
        if s and rs != st: continue
        if S_ and rs == st: continue
        end = pos + sum(l for op, l in cig if op in (0, 2, 3))
        if not split:
            ov = overlap(s0, e0, pos, end)
            if ov <= 0: continue
            if ov / (e0 - s0) < f: continue
            if r and ov / (end - pos) < f: continue
            n += 1
        else:
            bl = cig_blocks(pos, cig, True, False); tot = sum(overlap(s0, e0, bs, be) for bs, be in bl)
            if tot <= 0: continue
            foot = sum(be - bs for bs, be in bl)
            # multiBamCov.cpp:91: fraction is relative to the READ footprint (a_blocks = read), strict '>'
            if not (tot / foot > f): continue
            if r and not (tot / (e0 - s0) > f): continue
            n += 1
    return n
for label, args, kw in (("default", [], {}), ("-q 20", ["-q", "20"], dict(q=20)), ("-p", ["-p"], dict(p=True)), ("-D", ["-D"], dict(D=True)), ("-F", ["-F"], dict(F=True)),
                        ("-s", ["-s"], dict(s=True)), ("-S", ["-S"], dict(S_=True)), ("-f 0.1", ["-f", "0.1"], dict(f=0.1)), ("-f 0.1 -r", ["-f", "0.1", "-r"], dict(f=0.1, r=True)),
                        ("-split", ["-split"], dict(split=True)), ("-split -f 0.5 (fraction of the read, strict >)", ["-split", "-f", "0.5"], dict(split=True, f=0.5))):
    got = [int(l[6]) for l in lines(run(["multicov", "-bams", BAM, "-bed", A, *args]))]
    ref = [mc_port(iv, **kw) for iv in ivs]
    report("multicov %s" % label, got == ref, "" if got == ref else "sum got %d ref %d" % (sum(got), sum(ref)))
# the -split -f semantic difference, isolated
write(A, [["chr1", 0, 20000, "whole", 0, "+"]])
got_ns = int(lines(run(["multicov", "-bams", BAM, "-bed", A, "-f", "0.5"]))[0][6]); got_sp = int(lines(run(["multicov", "-bams", BAM, "-bed", A, "-split", "-f", "0.5"]))[0][6])
print("   note N9: 20-kb interval, -f 0.5: without -split %d reads (no read covers 50 %% of 20 kb), with -split %d (fraction taken of the read)" % (got_ns, got_sp))
print("\nMISMATCHES: %d" % fails)
