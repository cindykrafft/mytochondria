#!/usr/bin/env python3
"""BT3: `closest -t first` / `-t last` resolve a tie between a left-side and a right-side
B record by taking the *upstream* list first (CloseSweep::finalizeSelections), which is
B-file order only under -D ref. Under -D a (query on the - strand) or -D b (B on the +
strand) the right-hand record is "upstream", so -t first returns the later record and
-t last the earlier one. The documentation defines -t first as "the first tie that
occurred in the B file".

Part A: minimal example.
Part B: 2000 random queries with a tied left/right pair; mismatches vs B-file order
        counted per -D mode; -d and -D ref as controls.
"""
import os, random, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
rng = random.Random(3)
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed")

print("\n== A. minimal: A = chr1:10-20 (-); B = chr1:5-6 (b1, +) and chr1:24-25 (b2, +), both at distance 5")
write(A, [["chr1", 10, 20, "a1", 1, "-"]])
write(B, [["chr1", 5, 6, "b1", 1, "+"], ["chr1", 24, 25, "b2", 1, "+"]])
for args in (["-d", "-t", "first"], ["-D", "ref", "-t", "first"], ["-D", "a", "-t", "first"], ["-D", "a", "-t", "last"],
             ["-D", "b", "-t", "first"], ["-D", "b", "-t", "last"], ["-D", "a", "-t", "all"]):
    out = lines(run(["closest", "-a", A, "-b", B, *args]))
    print("   %-22s -> %s" % (" ".join(args), ", ".join("%s (dist %s)" % (l[9], l[-1]) for l in out)))
print("   (-t first documented as the first tie in the B file, i.e. b1 in every mode)")

print("\n== B. random: 2000 queries, each with one B record at distance d on the left and one on the right")
arows, brows = [], []
pos = 1000
for i in range(2000):
    L = rng.randint(1, 200); d = rng.randint(1, 100)
    qs = pos + 300; qe = qs + L
    arows.append(["chr1", qs, qe, "q%d" % i, 0, rng.choice("+-")])
    # distance convention: left record with end e gives qs - e + 1; right record with start s gives s - qe + 1
    brows.append(["chr1", qs - d, qs - d + 1, "q%dL" % i, 0, rng.choice("+-")])
    brows.append(["chr1", qe + d - 1, qe + d, "q%dR" % i, 0, rng.choice("+-")])
    pos = qe + 400
write(A, arows); write(B, sorted_bed(brows))
astrand = {r[3]: r[5] for r in arows}; bstrand = {r[3]: r[5] for r in brows}
for mode in ("ref", "a", "b"):
    for tie in ("first", "last"):
        out = lines(run(["closest", "-a", A, "-b", B, "-D", mode, "-t", tie]))
        assert len(out) == 2000, len(out)
        want = "L" if tie == "first" else "R"
        bad = [l for l in out if not l[9].endswith(want)]
        # characterise the mismatches by strand
        by = {}
        for l in bad:
            key = ("A%s" % astrand[l[3]]) if mode == "a" else ("B%s" % bstrand[l[9]]) if mode == "b" else "-"
            by[key] = by.get(key, 0) + 1
        print("   -D %-3s -t %-5s: %4d of 2000 not the %s tie in file order %s" % (mode, tie, len(bad), tie, dict(sorted(by.items())) if bad else ""))
out = lines(run(["closest", "-a", A, "-b", B, "-d", "-t", "first"]))
print("   -d -t first     : %4d of 2000 not the first tie (control)" % sum(1 for l in out if not l[9].endswith("L")))
