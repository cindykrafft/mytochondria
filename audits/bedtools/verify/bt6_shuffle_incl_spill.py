#!/usr/bin/env python3
"""BT6: `shuffle -incl` chooses the start uniformly inside the chosen include interval
(shuffleBed.cpp:455) and only rejects placements that run past the chromosome end
(:253-258), so a shuffled feature of length L can extend up to L-1 bases beyond the
include interval it was assigned to. (Prior reports: #1089 open, #381 closed.)

Part A: spill fraction for several (feature length, include size) combinations.
Part B: bases of the shuffled output outside the include set, over a realistic mix.
Part C: -incl with -noOverlapping and with -excl.
"""
import os, random, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
rng = random.Random(11)
tmp = tempfile.mkdtemp()
I = os.path.join(tmp, "i.bed"); INC = os.path.join(tmp, "incl.bed"); EXC = os.path.join(tmp, "excl.bed"); G = os.path.join(tmp, "g.genome")
write(G, [["chr1", 10_000_000], ["chr2", 5_000_000]])

def spill(rows, incl):
    """features not fully inside any include interval; bases outside the include set"""
    n_out = 0; bases_out = 0
    for r in rows:
        c, s, e = r[0], int(r[1]), int(r[2])
        inside = [(a, b) for cc, a, b in incl if cc == c and a <= s and e <= b]
        if not inside:
            n_out += 1
            bases_out += (e - s) - merged_length([(max(s, a), min(e, b)) for cc, a, b in incl if cc == c and overlap(s, e, a, b) > 0])
    return n_out, bases_out

print("\n== A. 2000 features of length L, one include interval of size S, 5 seeds each")
for L, S in ((50, 100), (50, 1000), (200, 1000), (1000, 1000), (10, 10000), (500, 10000)):
    write(I, [["chr1", 0, L, "f%d" % i] for i in range(2000)])
    incl = [("chr1", 1_000_000, 1_000_000 + S)]; write(INC, [list(x) for x in incl])
    n_out = 0; bases = 0; total = 0
    for seed in range(5):
        rows = lines(run(["shuffle", "-i", I, "-g", G, "-incl", INC, "-seed", str(seed)]))
        o, b = spill(rows, incl); n_out += o; bases += b; total += len(rows)
    print("   L=%5d S=%6d: %5d of %d shuffled features extend past the include interval (%.1f %%); expected spill for uniform start: %.1f %%" %
          (L, S, n_out, total, 100.0 * n_out / total, 100.0 * (L - 1) / S if L <= S else 100.0))

print("\n== B. realistic mix: 5000 features of 20-2000 bp, 300 include intervals of 500-20000 bp (two chromosomes)")
feats = [["chr%d" % rng.choice([1, 2]), 0, rng.randint(20, 2000), "f%d" % i] for i in range(5000)]
for f in feats:
    s = rng.randint(0, 4_000_000); f[1], f[2] = s, s + f[2]
write(I, feats)
incl = []
for c, cmax in (("chr1", 10_000_000), ("chr2", 5_000_000)):
    p = 10000
    for _ in range(150):
        size = rng.randint(500, 20000); incl.append((c, p, p + size)); p += size + rng.randint(1000, 20000)
write(INC, [list(x) for x in incl])
rows = lines(run(["shuffle", "-i", I, "-g", G, "-incl", INC, "-seed", "42"]))
o, b = spill(rows, incl)
print("   %d of %d features not fully inside an include interval; %d bases placed outside the include set (of %d)" %
      (o, len(rows), b, sum(int(r[2]) - int(r[1]) for r in rows)))
print("   features starting outside any include interval: %d" %
      sum(1 for r in rows if not any(cc == r[0] and a <= int(r[1]) < bb for cc, a, bb in incl)))

print("\n== C. -incl plus -noOverlapping / -excl (same mix)")
rows2 = lines(run(["shuffle", "-i", I, "-g", G, "-incl", INC, "-seed", "42", "-noOverlapping"], check=False))
o2, b2 = spill(rows2, incl)
print("   -noOverlapping: %d features returned, %d not fully inside an include interval" % (len(rows2), o2))
excl = [("chr1", a - 200, a) for c, a, bb in incl if c == "chr1"]  # 200 bp before each chr1 include interval
write(EXC, [list(x) for x in excl])
rows3 = lines(run(["shuffle", "-i", I, "-g", G, "-incl", INC, "-excl", EXC, "-seed", "42"], check=False))
o3, b3 = spill(rows3, incl)
n_excl_hit = sum(1 for r in rows3 if any(cc == r[0] and overlap(int(r[1]), int(r[2]), a, bb) > 0 for cc, a, bb in excl))
print("   -excl (200 bp before each chr1 include interval): %d features, %d overlap an -excl interval (expected 0), %d not fully inside an include interval" % (len(rows3), n_excl_hit, o3))
