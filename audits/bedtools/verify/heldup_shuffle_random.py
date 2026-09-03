#!/usr/bin/env python3
"""Held-up checks, executed: shuffle and random.

  shuffle  lengths and strands preserved; chromosome chosen in proportion to size
           (chi-square) and -chromFirst uniformly over chromosomes; start positions
           uniform along each chromosome (chi-square over 20 bins); -chrom keeps the
           chromosome; -seed reproducible and different seeds differ; -excl never
           overlapped (and -f honoured); -noOverlapping output has no overlaps;
           -allowBeyondChromEnd truncates at the chromosome end
  random   -n/-l/-seed: lengths, containment, chromosome proportions, strand balance
"""
import os, random, sys, tempfile
import numpy as np
from scipy.stats import chisquare
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
tmp = tempfile.mkdtemp()
I = os.path.join(tmp, "i.bed"); EXC = os.path.join(tmp, "excl.bed"); G = os.path.join(tmp, "g.genome")
sizes = {"chr1": 1_000_000, "chr2": 600_000, "chr3": 400_000}; write(G, [[c, n] for c, n in sizes.items()])
fails = 0
def report(label, ok, detail=""):
    global fails
    fails += not ok
    print("   %-70s %s %s" % (label, "ok" if ok else "MISMATCH", detail))

rng = random.Random(8)
feats = [["chr1", s, s + L, "f%d" % i, i, rng.choice("+-")] for i, (s, L) in enumerate((rng.randint(0, 900000), rng.randint(1, 5000)) for _ in range(20000))]
write(I, feats)
rows = lines(run(["shuffle", "-i", I, "-g", G, "-seed", "7"]))
report("length, name, score and strand preserved", all(int(r[2]) - int(r[1]) == int(f[2]) - int(f[1]) and r[3:] == [str(x) for x in f[3:]] for r, f in zip(rows, feats)))
report("every record inside its chromosome", all(0 <= int(r[1]) < int(r[2]) <= sizes[r[0]] for r in rows))
obs = np.array([sum(1 for r in rows if r[0] == c) for c in sizes]); exp = np.array([sizes[c] for c in sizes]) / sum(sizes.values()) * len(rows)
p = chisquare(obs, exp).pvalue
report("chromosome frequency proportional to size (chi-square p = %.3f)" % p, p > 0.001, str(obs.tolist()))
ok = True; ps = []
for c in sizes:
    starts = np.array([int(r[1]) for r in rows if r[0] == c]); h = np.histogram(starts, bins=20, range=(0, sizes[c]))[0]
    ps.append(chisquare(h).pvalue)
report("start positions uniform along each chromosome (chi-square p = %s)" % ["%.3f" % x for x in ps], min(ps) > 0.001)
rows_cf = lines(run(["shuffle", "-i", I, "-g", G, "-seed", "7", "-chromFirst"]))
obs = np.array([sum(1 for r in rows_cf if r[0] == c) for c in sizes]); p = chisquare(obs).pvalue
report("-chromFirst: chromosomes equally frequent (chi-square p = %.3f)" % p, p > 0.001, str(obs.tolist()))
rows_c = lines(run(["shuffle", "-i", I, "-g", G, "-seed", "7", "-chrom"]))
report("-chrom keeps the chromosome", all(r[0] == f[0] for r, f in zip(rows_c, feats)))
report("-seed reproducible", lines(run(["shuffle", "-i", I, "-g", G, "-seed", "7"])) == rows)
report("different seeds differ", lines(run(["shuffle", "-i", I, "-g", G, "-seed", "8"])) != rows)
excl = [["chr1", 0, 400000], ["chr2", 100000, 500000], ["chr3", 350000, 400000]]; write(EXC, excl)
rows_e = lines(run(["shuffle", "-i", I, "-g", G, "-seed", "7", "-excl", EXC], check=False))
nhit = sum(1 for r in rows_e for e in excl if r[0] == e[0] and overlap(int(r[1]), int(r[2]), e[1], e[2]) > 0)
report("-excl: no output record overlaps an excluded region (%d records)" % len(rows_e), nhit == 0, str(nhit))
rows_ef = lines(run(["shuffle", "-i", I, "-g", G, "-seed", "7", "-excl", EXC, "-f", "0.5"], check=False))
nbad = sum(1 for r in rows_ef for e in excl if r[0] == e[0] and overlap(int(r[1]), int(r[2]), e[1], e[2]) / (int(r[2]) - int(r[1])) >= 0.5)
report("-excl -f 0.5: no record has >= 50 %% of its bases excluded", nbad == 0, str(nbad))
small = feats[:3000]; write(I, small)
rows_n = lines(run(["shuffle", "-i", I, "-g", G, "-seed", "7", "-noOverlapping"], check=False))
by = {}
for r in rows_n: by.setdefault(r[0], []).append((int(r[1]), int(r[2])))
novl = sum(1 for c in by for i, (s, e) in enumerate(sorted(by[c])) if i and s < sorted(by[c])[i - 1][1])
report("-noOverlapping: %d of %d placed, no pairwise overlap" % (len(rows_n), len(small)), novl == 0, str(novl))
write(I, [["chr3", 0, 300000, "big"]])
rows_b = lines(run(["shuffle", "-i", I, "-g", G, "-seed", "3", "-allowBeyondChromEnd", "-chrom"]))
report("-allowBeyondChromEnd -chrom: end clipped at chromosome length", int(rows_b[0][2]) <= sizes["chr3"] and int(rows_b[0][2]) - int(rows_b[0][1]) <= 300000)

print("\n== random")
rows = lines(run(["random", "-g", G, "-n", "30000", "-l", "250", "-seed", "5"]))
report("random -n 30000 -l 250: count, length, containment", len(rows) == 30000 and all(int(r[2]) - int(r[1]) == 250 and 0 <= int(r[1]) and int(r[2]) <= sizes[r[0]] for r in rows))
obs = np.array([sum(1 for r in rows if r[0] == c) for c in sizes]); exp = np.array([sizes[c] for c in sizes]) / sum(sizes.values()) * len(rows); p = chisquare(obs, exp).pvalue
report("random: chromosome frequency proportional to size (chi-square p = %.3f)" % p, p > 0.001)
plus = sum(1 for r in rows if r[5] == "+"); p = chisquare([plus, len(rows) - plus]).pvalue
report("random: strand balance (chi-square p = %.3f)" % p, p > 0.001)
report("random -seed reproducible", lines(run(["random", "-g", G, "-n", "30000", "-l", "250", "-seed", "5"])) == rows)
print("\nMISMATCHES: %d" % fails)
