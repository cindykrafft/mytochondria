"""Held-up checks for `samtools fixmate -m` + `sort` + `markdup -s`: duplicate
pair/single counts, which record of each group is kept (highest summed quality
>= 15, then read name), unclipped-coordinate matching through soft clips,
-S (supplementary of duplicates), -d optical duplicates by read-name x/y, and
the ESTIMATED_LIBRARY_SIZE against a Python port of Picard's estimator.
Usage: python heldup_markdup.py [samtools]
"""
import math, os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
random.seed(5)
d = tmpdir()
refs = [("chr1", 2_000_000)]

def picard_els(read_pairs, unique_pairs):
    """Picard DuplicationMetrics.estimateLibrarySize (bisection on c/x - 1 + exp(-n/x))."""
    n, c = read_pairs, unique_pairs
    dup = n - c
    if not (n and dup and c) or n <= dup: return 0
    f = lambda x: c / x - 1 + math.exp(-n / x)
    m, M = 1.0, 100.0
    if f(m * c) < 0: return 0
    while f(M * c) > 0: M *= 10
    for _ in range(40):
        r = (m + M) / 2; u = f(r * c)
        if u > 0: m = r
        elif u < 0: M = r
        else: break
    return int(c * (m + M) / 2)

def build(with_optical, n_frag=600):
    """Fragments with k copies each; copies share unclipped 5' ends (some differ by soft clips) ."""
    recs = []; truth = collections.Counter(); best = {}
    for fi in range(n_frag):
        k = 1 if with_optical and random.random() < 0.5 else random.choice([1, 1, 1, 2, 2, 3, 5])
        if with_optical: k = min(k, 2)
        start = random.randrange(1000, 1_900_000); ins = random.randrange(200, 400)
        single = random.random() < 0.15
        tile = random.choice(["1101", "1102"]); x0, y0 = random.randrange(1000, 20000), random.randrange(1000, 20000)
        opt = with_optical and k == 2 and random.random() < 0.5
        truth["pair" if not single else "single"] += (2 if not single else 1) * k
        truth["dup pair" if not single else "dup single"] += (2 if not single else 1) * (k - 1)
        if opt: truth["optical pair" if not single else "optical single"] += (2 if not single else 1)
        for c in range(k):
            if c == 0: x, y = x0, y0
            elif opt: x, y = x0 + random.randrange(-50, 50), y0 + random.randrange(-50, 50)
            else: x, y = x0 + 5000, y0 + 5000
            name = f"M1:1:FC:1:{tile}:{x}:{y}" if with_optical else f"f{fi}c{c}"
            q = random.choice([20, 25, 30, 35, 40])
            sc1 = random.choice([0, 0, 3]); sc2 = random.choice([0, 0, 4])  # soft clips: unclipped ends unchanged
            if single:
                cig = f"{sc1}S{100 - sc1}M" if sc1 else "100M"
                recs.append(simple_read(name, start + sc1, cig, flag=0, qual=q))
            else:
                c1 = f"{sc1}S{100 - sc1}M" if sc1 else "100M"; c2 = f"{100 - sc2}M{sc2}S" if sc2 else "100M"
                p2 = start + ins - 100
                recs.append(simple_read(name, start + sc1, c1, flag=0x63, qual=q, mtid=0, mpos=p2, tlen=ins))
                recs.append(simple_read(name, p2, c2, flag=0x93, qual=q, mtid=0, mpos=start + sc1, tlen=-ins))
                if random.random() < 0.05:   # a supplementary record for read 2 (markdup -S keys on the SA tag of the primary)
                    sp = random.randrange(1000, 1_900_000)
                    recs[-1]["tags"] = {"SA": f"chr1,{sp + 1},-,30M70S,60,0;"}
                    recs.append(simple_read(name, sp, "30M70H", flag=0x93 | 0x800, qual=q, mtid=0, mpos=start + sc1, tlen=0, tags={"SA": f"chr1,{p2 + 1},-,{c2},60,0;"}))
                    truth["supp"] += 1
                    if c > 0: truth["supp of dup"] += 1
    return recs, truth

def markdup(recs, label, *extra):
    raw = os.path.join(d, label + ".raw.bam"); fm = os.path.join(d, label + ".fm.bam"); srt = os.path.join(d, label + ".srt.bam"); out = os.path.join(d, label + ".md.bam")
    header = {"HD": {"VN": "1.6", "SO": "queryname"}, "SQ": [{"SN": n, "LN": L} for n, L in refs]}
    recs = sorted(recs, key=lambda r: r["name"])
    with pysam.AlignmentFile(raw, "wb", header=header) as f:
        for r in recs:
            a = pysam.AlignedSegment(); a.query_name = r["name"]; a.flag = r["flag"]; a.reference_id = r["tid"]; a.reference_start = r["pos"]
            a.mapping_quality = r["mapq"]; a.cigarstring = r["cigar"]; a.query_sequence = r["seq"]
            a.query_qualities = pysam.qualitystring_to_array("".join(chr(q + 33) for q in r["qual"]))
            a.next_reference_id = r.get("mtid", -1); a.next_reference_start = r.get("mpos", -1); a.template_length = r.get("tlen", 0)
            if r.get("tags"): a.set_tags(list(r["tags"].items()))
            f.write(a)
    run("fixmate", "-m", raw, fm); run("sort", "-o", srt, fm)
    o, e, rc = run("markdup", "-s", *extra, srt, out)
    st = {}
    for l in e.splitlines():
        if ": " in l and not l.startswith("COMMAND"):
            k, v = l.split(": ", 1)
            try: st[k] = int(v)
            except ValueError: pass
    return st, out, e

print("\n--- A. duplicate counts, no optical")
recs, T = build(False)
st, out, e = markdup(recs, "A")
pairs = T["pair"] // 2; uniq = (T["pair"] - T["dup pair"]) // 2
exp = {"PAIRED": T["pair"], "SINGLE": T["single"], "DUPLICATE PAIR": T["dup pair"], "DUPLICATE SINGLE": T["dup single"],
       "DUPLICATE PAIR OPTICAL": 0, "DUPLICATE NON PRIMARY": 0, "DUPLICATE TOTAL": T["dup pair"] + T["dup single"],
       "EXAMINED": T["pair"] + T["single"], "READ": T["pair"] + T["single"] + T["supp"], "ESTIMATED_LIBRARY_SIZE": picard_els(pairs, uniq)}
bad = 0
for k, v in exp.items():
    ok = st.get(k) == v; bad += not ok
    print(f"  {'OK ' if ok else 'BAD'} {k:30s} samtools {st.get(k)!s:>8}  truth {v}")
# flagstat agrees with the stats block; the kept record of each group is the highest-quality one
fs, _, _ = run("flagstat", out)
dupline = [l for l in fs.splitlines() if "duplicates" in l and "primary" not in l][0]
print(f"  flagstat after markdup: {dupline}   (expected {T['dup pair'] + T['dup single']} + 0)")
kept_ok = True
groups = collections.defaultdict(list)
with pysam.AlignmentFile(out) as f:
    for a in f:
        if a.is_supplementary or a.is_secondary: continue
        key = (a.reference_start - (a.cigartuples[0][1] if a.cigartuples[0][0] == 4 else 0), a.is_reverse, a.is_paired, a.is_read1)
        groups[key].append((sum(q for q in a.query_qualities if q >= 15), a.query_name, a.is_duplicate))
n_groups = 0
for key, mem in groups.items():
    if len(mem) < 2: continue
    n_groups += 1
    keep = [m for m in mem if not m[2]]
    if len(keep) != 1 or max(mem)[0] != keep[0][0]: kept_ok = False
print(f"  {'OK ' if kept_ok else 'BAD'} in each of {n_groups} duplicate groups exactly one record is unmarked and it has the highest quality sum")
print("  wrong:", bad)

print("\n--- B. -S marks supplementary records of duplicates")
st, out, e = markdup(recs, "B", "-S")
# truth: every supplementary record whose primary read was marked duplicate (which copy is kept depends on quality)
dup_names, supp = set(), []
with pysam.AlignmentFile(out) as f:
    for a in f:
        if a.is_supplementary: supp.append(a)
        elif a.is_duplicate: dup_names.add(a.query_name)
supp_of_dup = sum(1 for a in supp if a.query_name in dup_names)
supp_marked = sum(1 for a in supp if a.is_duplicate)
ok = st.get("DUPLICATE NON PRIMARY") == supp_of_dup == supp_marked and not any(a.is_duplicate for a in supp if a.query_name not in dup_names)
print(f"  {'OK ' if ok else 'BAD'} DUPLICATE NON PRIMARY samtools {st.get('DUPLICATE NON PRIMARY')}  supplementary records of duplicate-marked reads {supp_of_dup}  supplementary records flagged DUP {supp_marked} (of {len(supp)}); DUPLICATE TOTAL {st.get('DUPLICATE TOTAL')} = {T['dup pair'] + T['dup single']} + {supp_of_dup}")

print("\n--- C. optical duplicates with -d 100 (Illumina-style names, groups of at most 2)")
recs, T = build(True)
st, out, e = markdup(recs, "C", "-d", "100")
pairs = T["pair"] // 2; uniq = (T["pair"] - T["dup pair"]) // 2; optp = T["optical pair"] // 2
exp = {"PAIRED": T["pair"], "DUPLICATE PAIR": T["dup pair"], "DUPLICATE PAIR OPTICAL": T["optical pair"], "DUPLICATE SINGLE": T["dup single"],
       "DUPLICATE SINGLE OPTICAL": T["optical single"], "ESTIMATED_LIBRARY_SIZE": picard_els(pairs - optp, uniq)}
bad = 0
for k, v in exp.items():
    ok = st.get(k) == v; bad += not ok
    print(f"  {'OK ' if ok else 'BAD'} {k:30s} samtools {st.get(k)!s:>8}  truth {v}")
# dt tags
sq = lb = 0
with pysam.AlignmentFile(out) as f:
    for a in f:
        if a.is_duplicate and not a.is_supplementary:
            t = a.get_tag("dt"); sq += t == "SQ"; lb += t == "LB"
print(f"  dt:SQ records {sq} (truth {T['optical pair'] + T['optical single']}), dt:LB records {lb} (truth {T['dup pair'] + T['dup single'] - T['optical pair'] - T['optical single']})")
print("  wrong:", bad)
