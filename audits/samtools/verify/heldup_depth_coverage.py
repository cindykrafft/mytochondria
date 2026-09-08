"""Held-up checks for `samtools depth` (-a, -J, -q, -Q, -l, -s, -G/-g, -r,
multiple files) and `samtools coverage` (tabular columns, -q/-Q/-l, -r,
--min-depth) against per-position Python truth on a random BAM with
insertions, deletions, splices, soft/hard clips, every filtered flag, and
overlapping mate pairs.  Usage: python heldup_depth_coverage.py [samtools]
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
random.seed(11)
d = tmpdir()
L = 30000
refs = [("chr1", L), ("chr2", 5000)]

def rand_cigar(n=100):
    k = random.random()
    if k < 0.5: return f"{n}M"
    if k < 0.6: return f"{n//2}M3D{n - n//2}M"
    if k < 0.7: return f"{n//2}M2I{n - n//2 - 2}M"
    if k < 0.8: return f"{n//3}M{random.choice([200, 2000])}N{n - n//3}M"
    if k < 0.9: return f"5S{n - 12}M7S"
    return f"3H{n}M"

recs = []
for i in range(1500):
    pos = random.randrange(0, L - 3000)
    flag = 0
    r = random.random()
    if r < 0.05: flag |= 0x400
    elif r < 0.08: flag |= 0x200
    elif r < 0.11: flag |= 0x100
    elif r < 0.13: flag |= 0x800
    mapq = random.choice([0, 5, 20, 40, 60])
    cig = rand_cigar()
    n = qlen(cig)
    quals = [random.choice([2, 10, 20, 30, 40]) for _ in range(n)]
    recs.append(simple_read(f"s{i}", pos, cig, flag=flag, mapq=mapq, qual=quals))
# 400 overlapping proper pairs (both mates plain 100M), insert 120-260 so they overlap by 0-80 bp
for i in range(400):
    pos = random.randrange(0, L - 400)
    ins = random.randrange(100, 260)
    q1 = [random.choice([10, 30, 40]) for _ in range(100)]; q2 = [random.choice([10, 30, 40]) for _ in range(100)]
    recs.append(simple_read(f"p{i}", pos, "100M", flag=0x63, mapq=60, qual=q1, mtid=0, mpos=pos + ins - 100, tlen=ins))
    recs.append(simple_read(f"p{i}", pos + ins - 100, "100M", flag=0x93, mapq=60, qual=q2, mtid=0, mpos=pos, tlen=-ins))
# a few reads on chr2 and one unmapped
recs.append(simple_read("c2", 100, "100M", tid=1))
recs.append(dict(name="u", flag=4, tid=-1, pos=-1, mapq=0, cigar=None, seq="A" * 50, qual=[30] * 50))
bam = write_bam(os.path.join(d, "dc.bam"), recs, refs)

def depth_rows(args):
    out, err, rc = run("depth", *args, bam)
    if rc: print("   depth failed:", err.strip())
    rows = {}
    for line in out.splitlines():
        if line.startswith("#"): continue
        c, p, *vals = line.split("\t")
        rows[(c, int(p) - 1)] = [int(v) for v in vals]
    return rows

def compare(label, args, truth_fn, all_pos=False):
    rows = depth_rows(args)
    got = {k: v[0] for k, v in rows.items() if k[0] == "chr1"}
    exp = truth_fn()
    if all_pos:
        exp = {p: exp.get(p, 0) for p in range(L)}
    else:
        exp = {p: v for p, v in exp.items() if v > 0}
    gotp = {p: v for (c, p), v in got.items()}
    bad = sum(1 for p in set(gotp) | set(exp) if gotp.get(p, 0) != exp.get(p, 0))
    print(f"  {'OK ' if not bad else 'BAD'} depth {' '.join(args):28s}: {len(gotp)} rows, {sum(gotp.values())} total depth, truth rows {len(exp)}, mismatching positions {bad}")
    return bad

def overlap_truth(min_bq=0, min_mq=0, excl=0x4 | 0x100 | 0x200 | 0x400):
    """depth -s: first-seen mate stores its end; the later mate's bases before that end are dropped."""
    dd = collections.Counter(); seen = {}
    for r in sorted(recs, key=lambda r: (r["tid"], r["pos"])):
        if r["tid"] != 0 or (r["flag"] & excl) or r["mapq"] < min_mq: continue
        clip = 0
        if r["flag"] & 1 and not r["flag"] & 8:
            if r["name"] in seen: clip = seen.pop(r["name"])
            else:
                end = r["pos"] + ref_len(r["cigar"])
                if r["mpos"] == -1 or (r["mtid"] == r["tid"] and r["mpos"] <= end): seen[r["name"]] = end
        p, s = r["pos"], 0
        for n, op in parse_cigar(r["cigar"]):
            if op in "M=X":
                for i in range(n):
                    if p + i >= clip and r["qual"][s + i] >= min_bq: dd[p + i] += 1
                p += n; s += n
            elif op in "DN": p += n
            elif op in "IS": s += n
    return dd

print("\n--- samtools depth vs Python (chr1 only; default flags UNMAP,SECONDARY,QCFAIL,DUP)")
tot = 0
tot += compare("default", [], lambda: depth_truth(recs, 0))
tot += compare("-a", ["-a"], lambda: depth_truth(recs, 0), all_pos=True)
tot += compare("-J", ["-J"], lambda: depth_truth(recs, 0, include_del=True))
tot += compare("-q 20", ["-q", "20"], lambda: depth_truth(recs, 0, min_bq=20))
tot += compare("-Q 20", ["-Q", "20"], lambda: depth_truth(recs, 0, min_mq=20))
tot += compare("-q 30 -Q 40", ["-q", "30", "-Q", "40"], lambda: depth_truth(recs, 0, min_bq=30, min_mq=40))
tot += compare("-G DUP (keep dups)", ["-g", "0x400"], lambda: depth_truth(recs, 0, excl=0x4 | 0x100 | 0x200))
tot += compare("-G SUPPLEMENTARY", ["-G", "0x800"], lambda: depth_truth(recs, 0, excl=0x4 | 0x100 | 0x200 | 0x400 | 0x800))
tot += compare("-l 100", ["-l", "100"], lambda: depth_truth([r for r in recs if r["cigar"] and sum(n for n, op in parse_cigar(r["cigar"]) if op in "MI=X") >= 100], 0))
tot += compare("-s", ["-s"], overlap_truth)
tot += compare("-s -q 30", ["-s", "-q", "30"], lambda: overlap_truth(min_bq=30))
# region
rows = depth_rows(["-r", "chr1:10001-12000"])
exp = {p: v for p, v in depth_truth(recs, 0).items() if 10000 <= p < 12000 and v > 0}
gotp = {p: v[0] for (c, p), v in rows.items()}
bad = sum(1 for p in set(gotp) | set(exp) if gotp.get(p, 0) != exp.get(p, 0))
print(f"  {'OK ' if not bad else 'BAD'} depth -r chr1:10001-12000: {len(gotp)} rows, truth {len(exp)}, mismatching {bad}"); tot += bad
# two files: same BAM twice
out, _, _ = run("depth", bam, bam)
two_ok = all(l.split("\t")[2] == l.split("\t")[3] for l in out.splitlines())
print(f"  {'OK ' if two_ok else 'BAD'} depth f.bam f.bam: both columns equal on {len(out.splitlines())} rows")
print("  depth mismatching positions in total:", tot)

print("\n--- samtools coverage vs Python")
def cov_truth(min_bq=0, min_mq=0, min_len=0, excl=0x4 | 0x100 | 0x200 | 0x400, region=None, mindepth=1):
    beg, end = (0, L) if region is None else region
    sel = [r for r in recs if r["tid"] == 0 and not (r["flag"] & excl) and r["mapq"] >= min_mq
           and (not min_len or qlen(r["cigar"]) >= min_len)
           and (region is None or (r["pos"] < end and r["pos"] + ref_len(r["cigar"]) > beg))]
    dd = collections.Counter(); qsum = collections.Counter()
    for r in sel:
        p, s = r["pos"], 0
        for n, op in parse_cigar(r["cigar"]):
            if op in "M=X":
                for i in range(n):
                    if r["qual"][s + i] >= min_bq:
                        dd[p + i] += 1; qsum[p + i] += r["qual"][s + i]
                p += n; s += n
            elif op in "DN": p += n
            elif op in "IS": s += n
    covered = [p for p, v in dd.items() if beg <= p < end and v >= mindepth]
    sumd = sum(dd[p] for p in covered); sumq = sum(qsum[p] for p in covered)
    return dict(numreads=len(sel), covbases=len(covered), coverage=100.0 * len(covered) / (end - beg),
                meandepth=sumd / (end - beg), meanbaseq=sumq / sumd if sumd else 0,
                meanmapq=sum(r["mapq"] for r in sel) / len(sel) if sel else 0)
def cov_line(args, chrom="chr1"):
    out, err, rc = run("coverage", *args, bam)
    for l in out.splitlines():
        if l.startswith(chrom + "\t"):
            f = l.split("\t")
            return dict(numreads=int(f[3]), covbases=int(f[4]), coverage=float(f[5]), meandepth=float(f[6]), meanbaseq=float(f[7]), meanmapq=float(f[8]))
    print("  coverage failed:", err.strip())
def fmt(t):
    return dict(numreads=t["numreads"], covbases=t["covbases"], coverage=float(f"{t['coverage']:g}"), meandepth=float(f"{t['meandepth']:g}"),
                meanbaseq=float(f"{t['meanbaseq']:.3g}"), meanmapq=float(f"{t['meanmapq']:.3g}"))
cases = [
    ([], {}),
    (["-q", "20"], dict(min_mq=20)),
    (["-Q", "30"], dict(min_bq=30)),
    (["-q", "5", "-Q", "20"], dict(min_mq=5, min_bq=20)),
    (["-l", "100"], dict(min_len=100)),
    (["--ff", "UNMAP,SECONDARY,QCFAIL"], dict(excl=0x4 | 0x100 | 0x200)),
    (["--min-depth", "3"], dict(mindepth=3)),
    (["-r", "chr1:5001-9000"], dict(region=(5000, 9000))),
]
bad = 0
for args, kw in cases:
    got = cov_line(args); exp = fmt(cov_truth(**kw))
    ok = got == exp
    bad += not ok
    print(f"  {'OK ' if ok else 'BAD'} coverage {' '.join(args):32s} got {got}\n      truth {exp}")
print("  coverage cases wrong:", bad)
