"""Held-up check: MarkDuplicates against an independent duplicate caller.

Truth follows the documented algorithm: reads are grouped by library, unclipped 5' positions
of both ends, and strand orientation; within a group the read (pair) with the highest sum of
base qualities >= 15 is kept; unpaired reads at a position where a pair also starts are always
duplicates; secondary/supplementary/unmapped records are never marked (coordinate-sorted input);
optical duplicates are pairs in the same tile within OPTICAL_DUPLICATE_PIXEL_DISTANCE (100)
in both x and y, chained transitively (union-find) within a duplicate set; PERCENT_DUPLICATION =
(UNPAIRED_DUPS + 2 * PAIR_DUPS) / (UNPAIRED_EXAMINED + 2 * PAIRS_EXAMINED); ESTIMATED_LIBRARY_SIZE
solves the Lander-Waterman equation C/X = 1 - exp(-N/X) with N = pairs - optical pairs and
C = pairs - duplicate pairs. Usage: python heldup_markduplicates.py [picard.jar]
"""
import os, sys, random, math, collections, itertools
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(21)
L = 1000000
refs = [("chr1", L), ("chr2", L)]

def unclipped5(r):
    """0-based unclipped 5' coordinate and strand."""
    cig = parse_cigar(r["cigar"])
    neg = bool(r["flag"] & 16)
    if not neg:
        lead = cig[0][0] if cig[0][1] in "SH" else 0
        if len(cig) > 1 and cig[0][1] == "H" and cig[1][1] == "S": lead += cig[1][0]
        return r["pos"] - lead, "R" if neg else "F"
    trail = cig[-1][0] if cig[-1][1] in "SH" else 0
    if len(cig) > 1 and cig[-1][1] == "H" and cig[-2][1] == "S": trail += cig[-2][0]
    return r["pos"] + ref_len(r["cigar"]) - 1 + trail, "R"

def score(r): return sum(q for q in r["qual"] if q >= 15)

def loc(name):
    # names like "t7:1000:2000" -> tile 7, x 1000, y 2000 (READ_NAME_REGEX default handles "t7:1000:2000"? we use the 5-element form)
    parts = name.split(":")
    return int(parts[-3]), int(parts[-2]), int(parts[-1])

def truth(records, pixel=100):
    by_name = collections.defaultdict(list)
    for r in records:
        if r["flag"] & (0x4 | 0x100 | 0x800): continue
        by_name[r["name"]].append(r)
    pairs, frags = [], []
    for name, rs in by_name.items():
        if len(rs) == 2 and all(x["flag"] & 1 for x in rs) and not any(x["flag"] & 8 for x in rs):
            e = sorted([(x["tid"],) + unclipped5(x) for x in rs] , key=lambda t: (t[0], t[1]))
            # orientation by the leftmost end first; equal positions with opposite strands -> FR
            (t1, p1, s1), (t2, p2, s2) = e
            if p1 == p2 and t1 == t2 and s1 != s2: s1, s2 = "F", "R"
            key = ("P", t1, p1, s1, t2, p2, s2)
            pairs.append((key, name, sum(score(x) for x in rs)))
        else:
            for x in rs:
                if x["flag"] & 1 and not x["flag"] & 8: continue   # mate mapped but missing: not modelled
                t, p, s = (x["tid"],) + unclipped5(x)
                frags.append((("F", t, p, s), name, score(x), x))
    dups, optical = set(), 0
    groups = collections.defaultdict(list)
    for key, name, sc in pairs: groups[key].append((name, sc))
    pair_dups = 0
    for key, members in groups.items():
        if len(members) < 2: continue
        best = min(members, key=lambda m: (-m[1], loc(m[0])))   # highest score; ties by (tile, x, y) as Picard's sorted order
        for name, sc in members:
            if name != best[0]: dups.add(name); pair_dups += 1
        # optical: union-find over pairs within pixel distance on the same tile, one representative per cluster
        idx = list(range(len(members)))
        parent = list(idx)
        def find(i):
            while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
            return i
        locs = [loc(m[0]) for m in members]
        for i, j in itertools.combinations(idx, 2):
            (ti, xi, yi), (tj, xj, yj) = locs[i], locs[j]
            if ti == tj and abs(xi - xj) <= pixel and abs(yi - yj) <= pixel:
                parent[find(i)] = find(j)
        clusters = collections.Counter(find(i) for i in idx)
        optical += sum(c - 1 for c in clusters.values())
    frag_dups = 0
    fgroups = collections.defaultdict(list)
    for key, name, sc, x in frags: fgroups[key].append((name, sc))
    pair_starts = set()
    for key, name, sc in pairs:
        _, t1, p1, s1, t2, p2, s2 = key
        pair_starts.add((t1, p1, s1)); pair_starts.add((t2, p2, s2))
    for key, members in fgroups.items():
        _, t, p, s = key
        if (t, p, s) in pair_starts:
            for name, sc in members: dups.add(name); frag_dups += 1
        elif len(members) >= 2:
            best = min(members, key=lambda m: (-m[1], loc(m[0])))
            for name, sc in members:
                if name != best[0]: dups.add(name); frag_dups += 1
    n_pairs, n_frags = len(pairs), len(frags)
    pct = (frag_dups + 2 * pair_dups) / (n_frags + 2 * n_pairs)
    # library size
    N = n_pairs - optical; C = n_pairs - pair_dups
    lib = None
    if n_pairs > 0 and pair_dups > 0 and C < N:
        f = lambda x: C / x - 1 + math.exp(-N / x)
        lo, hi = 1.0 * C, 100.0 * C
        while f(hi) > 0: hi *= 10
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid) > 0: lo = mid
            else: hi = mid
        lib = int((lo + hi) / 2)
    return dict(dups=dups, READ_PAIRS_EXAMINED=n_pairs, UNPAIRED_READS_EXAMINED=n_frags, READ_PAIR_DUPLICATES=pair_dups,
                UNPAIRED_READ_DUPLICATES=frag_dups, READ_PAIR_OPTICAL_DUPLICATES=optical, PERCENT_DUPLICATION=pct, ESTIMATED_LIBRARY_SIZE=lib)

def nm(prefix, tile, x, y): return f"{prefix}:1:{tile}:{x}:{y}"

recs = []
# 1. plain PCR duplicate sets of sizes 1..5 (different tiles, far apart), best pair varies by quality
k = 0
for size in range(1, 6):
    for j in range(size):
        q = 30 + (j * 7) % 5
        recs += pair(nm(f"a{size}_{j}", 1 + j, 1000 * (j + 1), 5000 * (j + 1)), 10000 + size * 1000, 10000 + size * 1000 + 200, qual=q)
# 2. optical chains: 4 pairs in one tile at x = 0, 90, 180, 270 (a chain: adjacent within 100, ends 270 apart) + one far
for j, x in enumerate((0, 90, 180, 270, 5000)):
    recs += pair(nm(f"chain_{j}", 3, 1000 + x, 2000), 30000, 30300, qual=30)
# 3. three pairs within 100 px of each other in a triangle (all mutually close)
for j, (x, y) in enumerate(((0, 0), (50, 50), (80, 20))):
    recs += pair(nm(f"tri_{j}", 4, 1000 + x, 1000 + y), 40000, 40300, qual=30)
# 4. same coordinates, different libraries (second read group) -> not duplicates of each other
recs += pair(nm("libA", 5, 100, 100), 50000, 50300, qual=30)
recs += pair(nm("libB", 5, 100, 100), 50000, 50300, qual=30, tags1={"RG": "rg2"}, tags2={"RG": "rg2"})
# 5. soft-clipped duplicates: same unclipped 5' ends, different clipping
recs += pair(nm("clipA", 6, 100, 100), 60000, 60300, qual=30)
recs += pair(nm("clipB", 6, 100, 900), 60005, 60300, qual=30, cigar1="5S95M", cigar2="95M5S")   # read1 unclipped start 60000, read2 unclipped end 60399
# 6. fragments: 3 single-end reads at one position (best kept), and 2 single-end reads at a position where a pair starts (both dups)
for j in range(3):
    recs.append(simple_read(nm(f"frag_{j}", 7, 100 + 500 * j, 100), 70000, "100M", flag=0 if j != 1 else 16, qual=30 + j))
recs.append(simple_read(nm("fragR", 7, 3000, 100), 70000, "100M", flag=16, qual=30))     # reverse strand at the same start: different group
for j in range(2):
    recs.append(simple_read(nm(f"fragP_{j}", 7, 100 + 500 * j, 5000), 10000 + 1000, "100M", flag=0, qual=35))   # same 5' as the size-1 pair set
# 7. FR vs RF orientation at the same positions: not duplicates of each other
recs += pair(nm("fr", 8, 100, 100), 80000, 80300, qual=30)
rf = pair(nm("rf", 8, 100, 900), 80000, 80300, qual=30)
rf[0]["flag"] = 0x53 | 0x20 ^ 0x20; rf[0]["flag"] = 0x1 | 0x2 | 0x10 | 0x40; rf[1]["flag"] = 0x1 | 0x2 | 0x20 | 0x80   # read1 reverse at 80000, read2 forward at 80300
rf[0]["tlen"] = -(80400 - 80000); rf[1]["tlen"] = 80400 - 80000
recs += rf
# 8. secondary and supplementary records of a duplicate pair: never marked
recs += pair(nm("supp", 9, 100, 100), 90000, 90300, qual=30)
recs += pair(nm("supp2", 9, 900, 900), 90000, 90300, qual=31)
recs.append(simple_read(nm("supp", 9, 100, 100), 95000, "50M50H", flag=0x1 | 0x2 | 0x40 | 0x800, qual=30, mtid=0, mpos=90300))
# 9. mate-unmapped pair: read counted as unpaired
recs.append(simple_read(nm("mu_1", 10, 100, 100), 100000, "100M", flag=0x1 | 0x8 | 0x40, qual=30, mtid=0, mpos=100000))
recs.append(simple_read(nm("mu_1", 10, 100, 100), 100000, "100M", flag=0x1 | 0x4 | 0x80 | 0x20, qual=30, mtid=0, mpos=100000))
recs.append(simple_read(nm("mu_2", 10, 100, 100), 100000, "100M", flag=0x1 | 0x8 | 0x40, qual=32, mtid=0, mpos=100000))
recs.append(simple_read(nm("mu_2", 10, 100, 100), 100000, "100M", flag=0x1 | 0x4 | 0x80 | 0x20, qual=30, mtid=0, mpos=100000))
# 10. inter-chromosomal pairs, duplicates of each other
for j in range(2):
    r = pair(nm(f"inter_{j}", 11, 100 + 900 * j, 100), 110000, 110300, qual=30)
    r[1]["tid"] = 1; r[0]["mtid"] = 1; r[0]["tlen"] = r[1]["tlen"] = 0
    recs += r
# 11. 100 random pairs in a hot spot: many duplicate sets with random tiles, some optical
for j in range(100):
    p1 = 200000 + rng.choice(range(0, 2000, 400)); ins = rng.choice((300, 300, 300, 310))
    recs += pair(nm(f"hot_{j}", rng.choice((20, 21)), rng.randrange(0, 400), rng.randrange(0, 400)), p1, p1 + ins - 100, qual=rng.choice((25, 30, 35)))

for r in recs:
    if r["flag"] & 4: r["cigar"] = None; r["mapq"] = 0
bam = write_bam(os.path.join(d, "in.bam"), recs, refs, rg=[{"ID": "rg1", "SM": "s1", "LB": "lib1", "PL": "ILLUMINA"}, {"ID": "rg2", "SM": "s1", "LB": "lib2", "PL": "ILLUMINA"}])
out = os.path.join(d, "out.bam"); met = os.path.join(d, "dup.txt")
run("MarkDuplicates", "-I", bam, "-O", out, "-M", met, "--CREATE_INDEX", "false")   # default READ_NAME_REGEX: last three colon-separated fields = tile, x, y

# compare flags
got = {}
with pysam.AlignmentFile(out) as f:
    for a in f:
        if a.is_secondary or a.is_supplementary or a.is_unmapped: 
            if a.is_duplicate: print("  WARNING: secondary/supplementary/unmapped record marked duplicate:", a.query_name)
            continue
        got.setdefault(a.query_name, set()).add(a.is_duplicate)
t = truth([r for r in recs if not (r.get("tags", {}).get("RG") == "rg2")])   # library 2 pair handled separately below
# add library-2 records to truth as their own library (no duplicates)
inconsistent = [n for n, s in got.items() if len(s) > 1]
picard_dups = {n for n, s in got.items() if True in s}
missing = t["dups"] - picard_dups; extra = picard_dups - t["dups"]
print(f"records {len(recs)}, names {len(got)}; pairs marked inconsistently (one end only): {inconsistent}")
print(f"duplicate names: truth {len(t['dups'])}, picard {len(picard_dups)}; missing {sorted(missing)}; extra {sorted(extra)}")
m = parse_metrics(met)[0]
m1 = [x for x in m if x["LIBRARY"] == "lib1"][0]
for k in ("UNPAIRED_READS_EXAMINED", "READ_PAIRS_EXAMINED", "UNPAIRED_READ_DUPLICATES", "READ_PAIR_DUPLICATES", "READ_PAIR_OPTICAL_DUPLICATES", "PERCENT_DUPLICATION", "ESTIMATED_LIBRARY_SIZE"):
    tv = t[k]; gv = m1[k]
    ok = (abs(float(gv) - float(tv)) < 1e-6) if tv is not None and gv is not None else gv == tv
    print(f"  lib1 {k:28s} picard {gv!s:10s} truth {tv!s:10s} {'ok' if ok else 'MISMATCH'}")
m2 = [x for x in m if x["LIBRARY"] == "lib2"][0]
print(f"  lib2 READ_PAIRS_EXAMINED {m2['READ_PAIRS_EXAMINED']} READ_PAIR_DUPLICATES {m2['READ_PAIR_DUPLICATES']} (truth 1, 0)")
