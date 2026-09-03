#!/usr/bin/env python3
"""Held-up checks, executed: the overlap tools against independent Python ports on
random intervals (two chromosomes, strands, lengths 1-500, some nested/duplicated).

  intersect  -wo/-wa -wb, -u, -c, -C (two -b files), -v, -wao, -loj, -f, -F, -r, -e,
             -s, -S, each with and without -sorted
  coverage   default columns, -counts, -hist (per record and 'all'), -d, -mean
  subtract   default fragments, -A, -f (per hit), -N
  window     -w, -l/-r, -sw, -sm, -Sm, -u, -c, -v
  merge      -d 0/100/-1, -s, -S +, -c/-o summaries
  cluster    -d, -s
  map        -o sum, mean, median, min, max, count, count_distinct, stdev, sstdev, mode,
             antimode, collapse, distinct, first, last, absmin, absmax; -null; -f
  groupby    -g 1 -c 5 -o (same operations, VectorOps implementation)
"""
import os, random, sys, tempfile, math, statistics
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btlib import *

print(version())
rng = random.Random(2026)
tmp = tempfile.mkdtemp()
A = os.path.join(tmp, "a.bed"); B = os.path.join(tmp, "b.bed"); B2 = os.path.join(tmp, "b2.bed"); G = os.path.join(tmp, "g.genome")
write(G, [["chr1", 200000], ["chr2", 100000]])

def rand_rows(n, prefix, maxpos, dup=0.05):
    rows = []
    for i in range(n):
        c = rng.choice(["chr1", "chr1", "chr2"]); L = rng.randint(1, 500); s = rng.randint(0, maxpos - L)
        rows.append([c, s, s + L, "%s%d" % (prefix, i), rng.randint(0, 1000), rng.choice("++--.")])
        if rng.random() < dup: rows.append(list(rows[-1])); rows[-1][3] += "d"
    return sorted_bed(rows)

arows = rand_rows(400, "a", 60000); brows = rand_rows(1500, "b", 60000); b2rows = rand_rows(500, "c", 60000)
write(A, arows); write(B, brows); write(B2, b2rows)
S = {"+": 1, "-": -1, ".": 0}

def qualifies(a, b, f=0.0, F=0.0, r=False, e=False, s=False, S_=False):
    if a[0] != b[0]: return 0
    ov = overlap(int(a[1]), int(a[2]), int(b[1]), int(b[2]))
    if ov <= 0: return 0
    sa, sb = S[a[5]], S[b[5]]
    if s and not (sa != 0 and sa == sb): return 0
    if S_ and not (sa != 0 and sb != 0 and sa != sb): return 0
    if r: F = f
    fa = ov / (int(a[2]) - int(a[1])) >= f; fb = ov / (int(b[2]) - int(b[1])) >= F
    if (f > 0 or F > 0) and not ((fa or fb) if e else (fa and fb)): return 0
    return ov

fails = 0
def report(label, ok, detail=""):
    global fails
    fails += not ok
    print("   %-58s %s %s" % (label, "ok" if ok else "MISMATCH", detail))

def f32(n, d):
    """%0.7f of a float32 quotient, as coverageFile.cpp prints it"""
    return "%0.7f" % float(np.float32(n) / np.float32(d))

print("\n== intersect (400 A, 1500 B records)")
for label, args, kw in (("default", [], {}), ("-f 0.5", ["-f", "0.5"], dict(f=0.5)), ("-F 0.5", ["-F", "0.5"], dict(F=0.5)),
                        ("-f 0.3 -r", ["-f", "0.3", "-r"], dict(f=0.3, r=True)), ("-f 0.9 -F 0.1 -e", ["-f", "0.9", "-F", "0.1", "-e"], dict(f=0.9, F=0.1, e=True)),
                        ("-s", ["-s"], dict(s=True)), ("-S", ["-S"], dict(S_=True)), ("-f 0.5 -s", ["-f", "0.5", "-s"], dict(f=0.5, s=True))):
    ref = {(a[3], b[3]): qualifies(a, b, **kw) for a in arows for b in brows if qualifies(a, b, **kw) > 0}
    for sorted_flag in ([], ["-sorted"]):
        out = lines(run(["intersect", "-a", A, "-b", B, "-wo", *args, *sorted_flag]))
        got = {(l[3], l[9]): int(l[12]) for l in out}
        report("-wo %s %s: %d pairs, overlap widths" % (label, " ".join(sorted_flag), len(ref)), got == ref, "" if got == ref else "%d vs %d" % (len(got), len(ref)))
    cnt = {l[3]: int(l[6]) for l in lines(run(["intersect", "-a", A, "-b", B, "-c", *args]))}
    refc = {a[3]: sum(1 for b in brows if qualifies(a, b, **kw) > 0) for a in arows}
    report("-c %s" % label, cnt == refc)
    u = [l[3] for l in lines(run(["intersect", "-a", A, "-b", B, "-u", *args]))]
    report("-u %s (once per A, A order)" % label, u == [a[3] for a in arows if refc[a[3]] > 0])
    v = [l[3] for l in lines(run(["intersect", "-a", A, "-b", B, "-v", *args]))]
    report("-v %s" % label, v == [a[3] for a in arows if refc[a[3]] == 0])
out = lines(run(["intersect", "-a", A, "-b", B, "-wao"]))
got = {(l[3], l[9]): int(l[12]) for l in out}
ref = {(a[3], b[3]): qualifies(a, b) for a in arows for b in brows if qualifies(a, b) > 0}
refz = {(a[3], "."): 0 for a in arows if not any(qualifies(a, b) for b in brows)}
report("-wao: pairs + zero rows for A without hit", got == {**ref, **refz})
out = lines(run(["intersect", "-a", A, "-b", B, "-loj"]))
report("-loj: one row per pair, NULL B for A without hit", {(l[3], l[9]) for l in out} == set(ref) | set(refz))
out = lines(run(["intersect", "-a", A, "-b", B, B2, "-C"]))
refC = {}
for a in arows:
    refC[(a[3], "1")] = sum(1 for b in brows if qualifies(a, b)); refC[(a[3], "2")] = sum(1 for b in b2rows if qualifies(a, b))
report("-C with two -b files", {(l[3], l[6]): int(l[7]) for l in out} == refC)
out = lines(run(["intersect", "-a", A, "-b", B, B2, "-wo", "-sorted"]))
ref2 = {(a[3], "1", b[3]) for a in arows for b in brows if qualifies(a, b)} | {(a[3], "2", b[3]) for a in arows for b in b2rows if qualifies(a, b)}
report("-wo -sorted with two -b files (file id column)", {(l[3], l[6], l[10]) for l in out} == ref2)

print("\n== coverage")
def depth_profile(a):
    a0, a1 = int(a[1]), int(a[2]); d = [0] * (a1 - a0)
    for b in brows:
        if b[0] == a[0]:
            for i in range(max(a0, int(b[1])), min(a1, int(b[2]))): d[i - a0] += 1
    return d
prof = {a[3]: depth_profile(a) for a in arows}
out = lines(run(["coverage", "-a", A, "-b", B]))
ok = True
for l in out:
    d = prof[l[3]]; n = sum(1 for b in brows if qualifies(dict(zip(range(6), l[:6])) and l or l, b) > 0) if False else sum(1 for b in brows if b[0] == l[0] and overlap(int(l[1]), int(l[2]), int(b[1]), int(b[2])) > 0)
    nz = sum(1 for x in d if x > 0)
    ok &= int(l[6]) == n and int(l[7]) == nz and int(l[8]) == len(d) and l[9] == f32(nz, len(d))
report("default: count, bases covered, length, fraction (float32, %0.7f)", ok)
out = lines(run(["coverage", "-a", A, "-b", B, "-counts"]))
report("-counts", all(int(l[6]) == sum(1 for b in brows if b[0] == l[0] and overlap(int(l[1]), int(l[2]), int(b[1]), int(b[2])) > 0) for l in out))
out = lines(run(["coverage", "-a", A, "-b", B, "-mean"]))
report("-mean (%0.7f of float mean)", all(abs(float(l[6]) - sum(prof[l[3]]) / len(prof[l[3]])) < 2e-6 for l in out))
out = lines(run(["coverage", "-a", A, "-b", B, "-d"]))
got = {}
for l in out: got.setdefault(l[3], []).append((int(l[6]), int(l[7])))
report("-d (1-based position, depth)", all(got[k] == [(i + 1, x) for i, x in enumerate(v)] for k, v in prof.items()))
out = lines(run(["coverage", "-a", A, "-b", B, "-hist"]))
ok = True; allhist = {}; total = 0
for k, d in prof.items():
    total += len(d)
    for x in d: allhist[x] = allhist.get(x, 0) + 1
per = [l for l in out if l[0] != "all"]; alls = [l for l in out if l[0] == "all"]
for l in per:
    d = prof[l[3]]; cnt = d.count(int(l[6]))
    ok &= int(l[7]) == cnt and int(l[8]) == len(d) and l[9] == f32(cnt, len(d))
ok &= {int(l[1]): int(l[2]) for l in alls} == allhist and all(int(l[3]) == total and l[4] == f32(int(l[2]), total) for l in alls)
report("-hist per record and 'all' summary (float32 fractions)", ok)

print("\n== subtract")
def sub_port(a, f=0.0, A_=False, N=False):
    a0, a1 = int(a[1]), int(a[2]); hits = [b for b in brows if b[0] == a[0] and overlap(a0, a1, int(b[1]), int(b[2])) > 0]
    if f > 0 and not N: hits = [b for b in hits if overlap(a0, a1, int(b[1]), int(b[2])) / (a1 - a0) >= f]
    if not hits: return [(a0, a1)]
    if A_: return []
    cov = [False] * (a1 - a0)
    for b in hits:
        for i in range(max(a0, int(b[1])), min(a1, int(b[2]))): cov[i - a0] = True
    if N:
        return [] if sum(cov) / (a1 - a0) > f else [(a0, a1)]
    frags, i = [], 0
    while i < len(cov):
        if not cov[i]:
            j = i
            while j < len(cov) and not cov[j]: j += 1
            frags.append((a0 + i, a0 + j)); i = j
        else: i += 1
    return frags
for label, args, kw in (("default", [], {}), ("-f 0.5", ["-f", "0.5"], dict(f=0.5)), ("-A", ["-A"], dict(A_=True)), ("-A -f 0.5", ["-A", "-f", "0.5"], dict(A_=True, f=0.5)), ("-N -f 0.5", ["-N", "-f", "0.5"], dict(N=True, f=0.5))):
    out = lines(run(["subtract", "-a", A, "-b", B, *args]))
    got = {}
    for l in out: got.setdefault(l[3], []).append((int(l[1]), int(l[2])))
    ref = {a[3]: sub_port(a, **kw) for a in arows}; ref = {k: v for k, v in ref.items() if v}
    report("subtract %s" % label, got == ref)

print("\n== window")
def win_port(a, l, r, sw=False, sm=False, Sm=False):
    a0, a1 = int(a[1]), int(a[2])
    if sw and a[5] == "-": l, r = r, l
    w0, w1 = max(0, a0 - l), a1 + r
    hits = []
    for b in brows:
        if b[0] != a[0] or overlap(w0, w1, int(b[1]), int(b[2])) <= 0: continue
        if sm and not (a[5] == b[5] and a[5] != "."): continue   # anyHits: strands_are_same = string equality
        if Sm and not (a[5] != b[5]): continue
        hits.append(b[3])
    return hits
# note: bedFile::anyHits/allHits compare strand strings, so '.' == '.' counts as the same strand for -sm
def win_port_str(a, l, r, sw=False, sm=False, Sm=False):
    a0, a1 = int(a[1]), int(a[2])
    if sw and a[5] != "+": l, r = r, l   # windowBed.cpp:241-252 swaps for every non-'+' strand, '.' included (note N3)
    w0, w1 = max(0, a0 - l), a1 + r
    return [b[3] for b in brows if b[0] == a[0] and overlap(w0, w1, int(b[1]), int(b[2])) > 0 and (not sm or a[5] == b[5]) and (not Sm or a[5] != b[5])]
for label, args, kw in (("-w 1000", ["-w", "1000"], dict(l=1000, r=1000)), ("-l 50 -r 300", ["-l", "50", "-r", "300"], dict(l=50, r=300)),
                        ("-l 50 -r 300 -sw", ["-l", "50", "-r", "300", "-sw"], dict(l=50, r=300, sw=True)), ("-w 200 -sm", ["-w", "200", "-sm"], dict(l=200, r=200, sm=True)),
                        ("-w 200 -Sm", ["-w", "200", "-Sm"], dict(l=200, r=200, Sm=True))):
    out = lines(run(["window", "-a", A, "-b", B, *args]))
    got = {}
    for l in out: got.setdefault(l[3], []).append(l[9])
    ref = {a[3]: sorted(win_port_str(a, **kw)) for a in arows}; ref = {k: v for k, v in ref.items() if v}
    report("window %s (pairs; -sw flips '-' and '.'; strands as strings)" % label, {k: sorted(v) for k, v in got.items()} == ref)
    cnt = {l[3]: int(l[6]) for l in lines(run(["window", "-a", A, "-b", B, "-c", *args]))}
    report("window %s -c" % label, cnt == {a[3]: len(win_port_str(a, **kw)) for a in arows})
    u = [l[3] for l in lines(run(["window", "-a", A, "-b", B, "-u", *args]))]; v = [l[3] for l in lines(run(["window", "-a", A, "-b", B, "-v", *args]))]
    report("window %s -u / -v" % label, u == [a[3] for a in arows if win_port_str(a, **kw)] and v == [a[3] for a in arows if not win_port_str(a, **kw)])

print("\n== merge / cluster")
def merge_port(rows, d=0, strand=None):
    rows = [r for r in rows if strand is None or r[5] == strand]
    out = []
    for c in ("chr1", "chr2"):
        cur = None
        for r in sorted((x for x in rows if x[0] == c), key=lambda x: (int(x[1]), int(x[2]))):
            s, e = int(r[1]), int(r[2])
            if cur and s <= cur[1] + d:
                cur[1] = max(cur[1], e); cur[2].append(r)
            else:
                if cur: out.append(cur)
                cur = [s, e, [r]]
        if cur: out.append(cur)
    return [(c[2][0][0], c[0], c[1], c[2]) for c in out]
for d in (0, 100, -1):
    got = [(l[0], int(l[1]), int(l[2])) for l in lines(run(["merge", "-i", B, "-d", str(d)]))]
    report("merge -d %d" % d, got == [(c, s, e) for c, s, e, _ in merge_port(brows, d)])
got = {(l[0], int(l[1]), int(l[2]), l[3]) for l in lines(run(["merge", "-i", B, "-s", "-c", "6", "-o", "distinct"]))}
ref = {(c, s, e, st) for st in "+-" for c, s, e, _ in merge_port(brows, 0, st)}
report("merge -s (per strand; '.' records are dropped, FileRecordMergeMgr.cpp:54-58)", got == ref, "" if got == ref else "%d vs %d" % (len(got), len(ref)))
got = {(l[0], int(l[1]), int(l[2])) for l in lines(run(["merge", "-i", B, "-S", "+"]))}
report("merge -S +", got == {(c, s, e) for c, s, e, _ in merge_port(brows, 0, "+")})

def stats(vals, op):
    xs = [float(v) for v in vals]
    if op == "sum": return sum(xs)
    if op == "mean": return sum(xs) / len(xs)
    if op == "median": return statistics.median(xs)
    if op == "min": return min(xs)
    if op == "max": return max(xs)
    if op == "absmin": return min(abs(x) for x in xs)
    if op == "absmax": return max(abs(x) for x in xs)
    if op == "stdev": return statistics.pstdev(xs)
    if op == "sstdev": return statistics.stdev(xs) if len(xs) > 1 else float("nan")
    if op == "count": return len(vals)
    if op == "count_distinct": return len(set(vals))
    if op == "mode":
        f = {}; [f.__setitem__(v, f.get(v, 0) + 1) for v in vals]; m = max(f.values()); return sorted(k for k in f if f[k] == m)[0]
    if op == "antimode":
        f = {}; [f.__setitem__(v, f.get(v, 0) + 1) for v in vals]; m = min(f.values()); return sorted(k for k in f if f[k] == m)[0]
    if op == "collapse": return ",".join(vals)
    if op == "distinct": return ",".join(sorted(set(vals)))
    if op == "first": return vals[0]
    if op == "last": return vals[-1]
NUM = ("sum", "mean", "median", "min", "max", "absmin", "absmax", "stdev", "sstdev")
OPS = NUM + ("count", "count_distinct", "mode", "antimode", "collapse", "distinct", "first", "last")
def close(got, ref, op):
    if op in NUM:
        if isinstance(ref, float) and math.isnan(ref): return got == "."
        return abs(float(got) - ref) <= 1e-9 * max(1.0, abs(ref)) + 1e-9
    return str(got) == str(ref)
out = lines(run(["merge", "-i", B, "-d", "100", "-c", "5", "-o", ",".join(OPS)]))
ref = merge_port(brows, 100)
ok = len(out) == len(ref) and all(close(l[3 + i], stats([str(r[4]) for r in grp], op), op) for l, (c, s, e, grp) in zip(out, ref) for i, op in enumerate(OPS))
report("merge -d 100 -c 5 -o <18 operations> (file order within group)", ok)
# groupby on the merged groups: emulate with an explicit group column
grp_rows = []
for gi, (c, s, e, grp) in enumerate(ref):
    for r in grp: grp_rows.append(["g%04d" % gi, r[4]])
GB = write(os.path.join(tmp, "gb.txt"), grp_rows)
out = lines(run(["groupby", "-i", GB, "-g", "1", "-c", "2", "-o", ",".join(OPS)]))
ok = len(out) == len(ref) and all(close(l[1 + i], stats([str(r[4]) for r in grp], op), op) for l, (c, s, e, grp) in zip(out, ref) for i, op in enumerate(OPS))
report("groupby -g 1 -c 2 -o <18 operations> (VectorOps path)", ok)
def cluster_port(rows, d, strand=None):
    ids = {}
    for c, s, e, grp in merge_port(rows, d, strand):
        for r in grp: ids[r[3]] = (c, s, e, strand)
    return ids
for d in (0, 100):
    out = lines(run(["cluster", "-i", B, "-d", str(d)]))
    got = {}
    for l in out: got.setdefault(l[6], []).append(l[3])
    ref = {}
    for k, v in cluster_port(brows, d).items(): ref.setdefault(v, []).append(k)
    report("cluster -d %d (partition)" % d, sorted(sorted(v) for v in got.values()) == sorted(sorted(v) for v in ref.values()))
out = lines(run(["cluster", "-i", B, "-s"]))
got = {}
for l in out: got.setdefault(l[6], []).append(l[3])
ref = {}
for st in "+-":
    for k, v in cluster_port(brows, 0, st).items(): ref.setdefault(v, []).append(k)
report("cluster -s (partition; '.' records dropped)", sorted(sorted(v) for v in got.values()) == sorted(sorted(v) for v in ref.values()))

print("\n== map")
out = lines(run(["map", "-a", A, "-b", B, "-c", "5", "-o", ",".join(OPS), "-null", "NA"]))
ok = True
for l in out:
    a = next(x for x in arows if x[3] == l[3])
    hits = [str(b[4]) for b in brows if qualifies(a, b) > 0]   # B file order
    for i, op in enumerate(OPS):
        if not hits:
            ok &= l[6 + i] == ("0" if op in ("count", "count_distinct") else "NA")
        else:
            good = close(l[6 + i], stats(hits, op), op)
            if not good and ok: print("      first mismatch: %s %s got %s ref %s hits %s" % (l[3], op, l[6 + i], stats(hits, op), hits))
            ok &= good
report("map -c 5 -o <18 operations> -null NA (count/count_distinct give 0 for no hit)", ok)
out = lines(run(["map", "-a", A, "-b", B, "-c", "5", "-o", "sum", "-f", "0.5", "-s"]))
ref = {a[3]: sum(int(b[4]) for b in brows if qualifies(a, b, f=0.5, s=True) > 0) for a in arows}
report("map -o sum -f 0.5 -s", all((l[6] == "." and ref[l[3]] == 0 and not any(qualifies(a, b, f=0.5, s=True) for a in arows if a[3] == l[3] for b in brows)) or (l[6] != "." and int(float(l[6])) == ref[l[3]]) for l in out))
print("\nMISMATCHES: %d" % fails)
