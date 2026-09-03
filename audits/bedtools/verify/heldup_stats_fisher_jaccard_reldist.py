#!/usr/bin/env python3
"""Held-up checks, executed: the statistics tools.

  fisher   the printed 2x2 table vs a port of fisher.cpp:50-69 (overlap pairs, record
           counts, merged lengths, the genome/mean-length heuristic for n22), and the
           left / right / two-tail p-values vs scipy.stats.fisher_exact on that table;
           the two documentation examples (500-bp and 60-bp genome); -m merged input
  jaccard  intersection, union, jaccard and n_intersections vs a port on random sets
           with internal overlaps (both files are merged first), and -s
  reldist  -detail values and the summary histogram vs a port of the Favorov
           relative distance (records outside the span of B's midpoints are skipped)
  nuc      counts, pct_at/pct_gc (%f), -s reverse complement, -pattern / -C
"""
import os, random, sys, tempfile
from scipy.stats import fisher_exact
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
rng = random.Random(1234)
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed"); G = os.path.join(tmp, "g.genome"); FA = os.path.join(tmp, "s.fa")
fails = 0
def report(label, ok, detail=""):
    global fails
    fails += not ok
    print("   %-66s %s %s" % (label, "ok" if ok else "MISMATCH", detail))

def merge(rows):
    out = {}
    for c in sorted({r[0] for r in rows}):
        cur = None
        for r in sorted((x for x in rows if x[0] == c), key=lambda x: (int(x[1]), int(x[2]))):
            s, e = int(r[1]), int(r[2])
            if cur and s <= cur[1]: cur[1] = max(cur[1], e)
            else:
                if cur: out.setdefault(c, []).append(tuple(cur))
                cur = [s, e]
        if cur: out.setdefault(c, []).append(tuple(cur))
    return out

def rand_rows(n, prefix, chroms, maxL=800):
    rows = []
    for i in range(n):
        c, cs = rng.choice(chroms); L = rng.randint(1, maxL); s = rng.randint(0, cs - L)
        rows.append([c, s, s + L, "%s%d" % (prefix, i), 0, rng.choice("+-")])
    return sorted_bed(rows)

# ------------------------------------------------------------------ fisher
print("\n== fisher: 30 random pairs of interval sets on a 3-chromosome genome; table vs port, p-values vs scipy")
chroms = [("chr1", 500000), ("chr2", 300000), ("chr3", 100000)]
write(G, [list(c) for c in chroms]); gsize = sum(c[1] for c in chroms)
ok_table = ok_p = ok_ratio = 0; n_done = 0
for trial in range(30):
    na, nb = rng.randint(20, 400), rng.randint(20, 400)
    arows = rand_rows(na, "a", chroms, rng.choice([200, 2000, 20000])); brows = rand_rows(nb, "b", chroms, rng.choice([200, 2000, 20000]))
    # make some trials dependent: copy a fraction of A into B with jitter
    if trial % 2:
        brows = sorted_bed(brows + [[r[0], max(0, int(r[1]) - rng.randint(0, 100)), int(r[2]) + rng.randint(0, 100), "x", 0, "+"] for r in arows if rng.random() < 0.4])
    write(A, arows); write(B, brows)
    out = run(["fisher", "-a", A, "-b", B, "-g", G]).splitlines()
    # parse
    def num(prefix): return int(next(l for l in out if l.startswith(prefix)).split(":")[1])
    qn, dn, novl, n22full = num("# Number of query intervals"), num("# Number of db intervals"), num("# Number of overlaps"), num("# Number of possible intervals")
    tab = [l for l in out if l.startswith("#     in -a") or l.startswith("# not in -a")]
    n11, n12 = [int(x.strip()) for x in tab[0].split("|")[1:3]]; n21, n22 = [int(x.strip()) for x in tab[1].split("|")[1:3]]
    left, right, two, ratio = out[-1].split("\t")
    # port of fisher.cpp: records are merged within each file (ContextFisher <- ContextJaccard: setUseMergedIntervals)
    ma, mb = merge(arows), merge(brows)
    qcount = sum(len(v) for v in ma.values()); dcount = sum(len(v) for v in mb.values())
    qlen = sum(e - s for v in ma.values() for s, e in v); dlen = sum(e - s for v in mb.values() for s, e in v)
    pairs = sum(1 for c in ma for s, e in ma[c] for s2, e2 in mb.get(c, []) if overlap(s, e, s2, e2) > 0)
    dMean = 1.0 + dlen / dcount; qMean = 1.0 + qlen / qcount; bMean = qMean + dMean
    p11 = pairs; p12 = max(0, qcount - pairs); p21 = max(0, dcount - pairs)
    p22full = max(p21 + p12 + p11, int(gsize / bMean)); p22 = max(0, p22full - p12 - p21 - p11)
    tab_ok = (qn, dn, novl, n22full, n11, n12, n21, n22) == (qcount, dcount, pairs, p22full, p11, p12, p21, p22)
    ok_table += tab_ok
    T = [[n11, n12], [n21, n22]]
    pl = fisher_exact(T, alternative="less")[1]; pr = fisher_exact(T, alternative="greater")[1]; pt = fisher_exact(T, alternative="two-sided")[1]
    def close(a, b): return abs(float(a) - b) <= 1e-4 * max(1e-300, abs(b)) + 1e-12
    p_ok = close(left, pl) and close(right, pr) and close(two, pt)
    ok_p += p_ok
    r_ref = (n11 / n12) / (n21 / n22) if n12 and n21 and n22 else None
    r_ok = (ratio == "inf" and (n12 == 0 or n21 == 0)) or (ratio == "-nan" and r_ref is None) or (r_ref is not None and abs(float(ratio) - r_ref) < 5e-4 * max(1, abs(r_ref)))
    ok_ratio += r_ok; n_done += 1
    if not (tab_ok and p_ok and r_ok):
        print("   trial %d: table %s port %s; p %s %s %s vs scipy %.5g %.5g %.5g; ratio %s" % (trial, (qn, dn, novl, n22full, n11, n12, n21, n22), (qcount, dcount, pairs, p22full, p11, p12, p21, p22), left, right, two, pl, pr, pt, ratio))
report("table (counts, n22 heuristic) equals the port of fisher.cpp", ok_table == n_done, "%d/%d" % (ok_table, n_done))
report("left/right/two-tail p-values equal scipy.stats.fisher_exact (rel 1e-4)", ok_p == n_done, "%d/%d" % (ok_p, n_done))
report("odds ratio = (n11/n12)/(n21/n22)", ok_ratio == n_done, "%d/%d" % (ok_ratio, n_done))
print("   documentation examples (docs/content/tools/fisher.rst):")
write(A, [["chr1", 10, 20], ["chr1", 30, 40], ["chr1", 51, 52]]); write(B, [["chr1", 15, 25], ["chr1", 51, 52]])
for gs, doc in ((500, "37 possible; table 2 1 / 0 34; left 1 right 0.0045045 two 0.0045045 ratio inf"), (60, "4 possible; table 2 1 / 0 1; left 1 right 0.5 two 1 ratio inf")):
    write(G, [["chr1", gs]]); out = run(["fisher", "-a", A, "-b", B, "-g", G]).splitlines()
    print("   genome %3d: %s | %s | %s" % (gs, next(l for l in out if "possible" in l)[2:], " / ".join(l[2:].replace(" ", "") for l in out if "in -a" in l), out[-1].replace("\t", " ")))
    print("              docs: %s" % doc)
    T = [[int(x.strip()) for x in out[-6].split("|")[1:3]], [int(x.strip()) for x in out[-5].split("|")[1:3]]]
    print("              scipy on the printed table %s: left %.5g right %.5g two %.5g" % (T, fisher_exact(T, alternative="less")[1], fisher_exact(T, alternative="greater")[1], fisher_exact(T, alternative="two-sided")[1]))

# ------------------------------------------------------------------ jaccard
print("\n== jaccard: 20 random pairs of sets with internal overlaps")
write(G, [list(c) for c in chroms]); ok = 0
for trial in range(20):
    arows = rand_rows(rng.randint(50, 500), "a", chroms, 5000); brows = rand_rows(rng.randint(50, 500), "b", chroms, 5000)
    write(A, arows); write(B, brows)
    l = lines(run(["jaccard", "-a", A, "-b", B]))[1]
    ma, mb = merge(arows), merge(brows)
    inter = sum(overlap(s, e, s2, e2) for c in ma for s, e in ma[c] for s2, e2 in mb.get(c, []))
    npairs = sum(1 for c in ma for s, e in ma[c] for s2, e2 in mb.get(c, []) if overlap(s, e, s2, e2) > 0)
    union = sum(e - s for v in ma.values() for s, e in v) + sum(e - s for v in mb.values() for s, e in v) - inter
    good = int(l[0]) == inter and int(l[1]) == union and abs(float(l[2]) - inter / union) < 1e-6 and int(l[3]) == npairs
    ok += good
    if not good: print("   trial %d: got %s port %s" % (trial, l, (inter, union, inter / union, npairs)))
report("intersection, union, jaccard (float, 7 digits), n_intersections", ok == 20, "%d/20" % ok)
arows = rand_rows(300, "a", chroms, 3000); brows = rand_rows(300, "b", chroms, 3000); write(A, arows); write(B, brows)
l = lines(run(["jaccard", "-a", A, "-b", B, "-s"]))[1]
inter = union = npairs = 0
for st in "+-":
    ma, mb = merge([r for r in arows if r[5] == st]), merge([r for r in brows if r[5] == st])
    inter += sum(overlap(s, e, s2, e2) for c in ma for s, e in ma[c] for s2, e2 in mb.get(c, []))
    npairs += sum(1 for c in ma for s, e in ma[c] for s2, e2 in mb.get(c, []) if overlap(s, e, s2, e2) > 0)
    union += sum(e - s for v in ma.values() for s, e in v) + sum(e - s for v in mb.values() for s, e in v)
union -= inter
report("jaccard -s (per-strand merge and intersection)", int(l[0]) == inter and int(l[1]) == union and int(l[3]) == npairs, "" if int(l[0]) == inter else "got %s port %s" % (l, (inter, union, npairs)))

# ------------------------------------------------------------------ reldist
print("\n== reldist: 5 random pairs; -detail and summary vs a port (queries outside B's midpoint span skipped)")
ok = 0
for trial in range(5):
    arows = rand_rows(rng.randint(200, 2000), "a", chroms, 2000); brows = rand_rows(rng.randint(30, 500), "b", chroms, 2000)
    write(A, arows); write(B, brows)
    mids = {}
    for r in brows: mids.setdefault(r[0], []).append((int(r[1]) + int(r[2])) // 2)
    for c in mids: mids[c].sort()
    ref = []
    for r in arows:
        m = (int(r[1]) + int(r[2])) // 2; ms = mids.get(r[0])
        if not ms: continue
        import bisect
        i = bisect.bisect_left(ms, m)
        if i == 0 and ms[0] > m: continue
        if i == len(ms): continue
        lo = ms[i - 1] if i > 0 else ms[0]; hi = ms[i] if i > 0 else ms[1] if len(ms) > 1 else None
        if hi is None: continue
        if lo > m: continue
        d = min(m - lo, hi - m); rd = 0.0 if d == 0 else d / (hi - lo)
        ref.append((r[3], rd))
    got = [(l[3], float(l[6])) for l in lines(run(["reldist", "-a", A, "-b", B, "-detail"]))]
    d_ok = len(got) == len(ref) and all(g[0] == r_[0] and abs(g[1] - float("%.3f" % r_[1])) < 1e-9 for g, r_ in zip(got, ref))
    hist = {}
    import math
    for _, rd in ref:
        k = math.floor(rd * 100) / 100; hist[k] = hist.get(k, 0) + 1
    gs = lines(run(["reldist", "-a", A, "-b", B]))[1:]
    s_ok = {float(l[0]): int(l[1]) for l in gs} == {round(k, 2): v for k, v in hist.items()} and all(int(l[2]) == len(ref) and l[3] == "%.3f" % (int(l[1]) / len(ref)) for l in gs)
    ok += d_ok and s_ok
    if not (d_ok and s_ok): print("   trial %d: detail %s (%d vs %d) summary %s" % (trial, d_ok, len(got), len(ref), s_ok))
report("reldist -detail (%.3f) and summary (floor to 0.01, count, total, %.3f)", ok == 5, "%d/5" % ok)
print("   note: A records before the first or after the last B midpoint on their chromosome are silently dropped (issue #955)")

# ------------------------------------------------------------------ nuc
print("\n== nuc: 200 random intervals on a random 50-kb sequence with N and lowercase")
seq = "".join(rng.choice("ACGTACGTacgtN") for _ in range(50000))
with open(FA, "w") as f: f.write(">chr1\n" + "\n".join(seq[i:i + 60] for i in range(0, len(seq), 60)) + "\n")
ivs = sorted_bed([["chr1", s, s + rng.randint(1, 300), "n%d" % i, 0, rng.choice("+-")] for i, s in enumerate(rng.randint(0, 49000) for _ in range(200))])
write(A, ivs)
comp = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N", "a": "t", "c": "g", "g": "c", "t": "a"}
def prof(s):
    u = s.upper(); a, c, g, t, n = (u.count(x) for x in "ACGTN"); o = len(s) - a - c - g - t - n
    return ("%f" % ((a + t) / len(s)), "%f" % ((c + g) / len(s)), a, c, g, t, n, o, len(s))
def count_overlapping(s, p):
    return sum(1 for i in range(len(s)) if s[i:i + len(p)] == p)
for label, args, rc in (("default", [], False), ("-s (reverse complement of '-' records)", ["-s"], True)):
    out = lines(run(["nuc", "-fi", FA, "-bed", A, *args]))
    ok = True
    for l, iv in zip(out, ivs):
        s = seq[int(iv[1]):int(iv[2])]
        if rc and iv[5] == "-": s = "".join(comp[x] for x in reversed(s))
        p = prof(s); ok &= (l[6], l[7], int(l[8]), int(l[9]), int(l[10]), int(l[11]), int(l[12]), int(l[13]), int(l[14])) == p
    report("nuc %s: pct_at, pct_gc, A, C, G, T, N, other, length" % label, ok)
out = lines(run(["nuc", "-fi", FA, "-bed", A, "-pattern", "ACG"])); out_c = lines(run(["nuc", "-fi", FA, "-bed", A, "-pattern", "ACG", "-C"]))
report("nuc -pattern ACG (case-sensitive, overlapping occurrences) and -C", all(int(l[15]) == count_overlapping(seq[int(iv[1]):int(iv[2])], "ACG") for l, iv in zip(out, ivs)) and all(int(l[15]) == count_overlapping(seq[int(iv[1]):int(iv[2])].upper(), "ACG") for l, iv in zip(out_c, ivs)))
print("\nMISMATCHES: %d" % fails)
