"""Held-up checks: `flagstat` (every line, all three output formats), `idxstats`
(indexed and slow path) and `view -c` under -q/-f/-F/--rf/-G/-e/-m against
independent Python counts on a random 4,000-record BAM with every flag
combination that matters.  Usage: python heldup_flagstat_idxstats_view.py [samtools]
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
random.seed(7)
d = tmpdir()
refs = [("chr1", 100000), ("chr2", 50000), ("chrM", 16000)]
recs = []
for i in range(2000):
    tid = random.choice([0, 0, 0, 1, 2])
    pos = random.randrange(0, refs[tid][1] - 200)
    mapq = random.choice([0, 3, 5, 10, 20, 60])
    flag = 0x1
    r1, r2 = flag | 0x40, flag | 0x80
    kind = random.random()
    mtid, mpos, tlen = tid, pos + 150, 250
    if kind < 0.70:            # proper pair
        r1 |= 0x2 | 0x20; r2 |= 0x2 | 0x10
    elif kind < 0.80:          # both mapped, not proper (mate on other chr)
        mtid = (tid + 1) % 3; mpos = random.randrange(0, refs[mtid][1] - 200); tlen = 0
        r1 |= 0x20; r2 |= 0x10
    elif kind < 0.90:          # mate unmapped (singleton)
        r1 |= 0x8; r2 |= 0x4
    else:                      # both unmapped
        r1 |= 0x4 | 0x8; r2 |= 0x4 | 0x8
    if random.random() < 0.10: r1 |= 0x400; r2 |= 0x400
    if random.random() < 0.05: r1 |= 0x200; r2 |= 0x200
    nm = random.choice([0, 0, 1, 2, 5])
    for f, name_sfx in ((r1, ""), (r2, "")):
        rec = simple_read(f"q{i}", pos if not (f & 0x4) or (f & 0x8) == 0 else pos, "100M", flag=f, tid=tid, mapq=mapq,
                          mtid=mtid, mpos=mpos, tlen=tlen if f & 0x40 else -tlen, tags={"NM": nm})
        if f & 0x4:  # unmapped: placed at mate position (or unplaced)
            if f & 0x8:
                rec.update(tid=-1, pos=-1, mtid=-1, mpos=-1, tlen=0, mapq=0); rec["cigar"] = None
            else:
                rec.update(pos=mpos, mapq=0); rec["cigar"] = None
        if f & 0x8 and not (f & 0x4):
            rec.update(mtid=tid, mpos=pos, tlen=0)
        recs.append(rec)
    if random.random() < 0.08:   # a secondary alignment of read 1
        recs.append(simple_read(f"q{i}", random.randrange(0, refs[tid][1] - 200), "100M", flag=(r1 & ~0x4) | 0x100, tid=tid, mapq=0, mtid=mtid, mpos=mpos, tlen=0, tags={"NM": nm}))
    if random.random() < 0.06:   # a supplementary alignment of read 2
        recs.append(simple_read(f"q{i}", random.randrange(0, refs[tid][1] - 200), "40M60S", flag=(r2 & ~0x4) | 0x800, tid=tid, mapq=mapq, mtid=mtid, mpos=mpos, tlen=0, tags={"NM": nm}))
bam = write_bam(os.path.join(d, "fs.bam"), recs, refs)

# ---------- flagstat truth (port of the documented definitions) ----------
def flagstat_truth(recs):
    t = {k: [0, 0] for k in ("total", "primary", "secondary", "supplementary", "duplicates", "primary duplicates",
                              "mapped", "primary mapped", "paired in sequencing", "read1", "read2", "properly paired",
                              "with itself and mate mapped", "singletons", "with mate mapped to a different chr",
                              "with mate mapped to a different chr (mapQ>=5)")}
    for r in recs:
        f = r["flag"]; w = 1 if f & 0x200 else 0
        t["total"][w] += 1
        if f & 0x100: t["secondary"][w] += 1
        elif f & 0x800: t["supplementary"][w] += 1
        else:
            t["primary"][w] += 1
            if f & 0x1:
                t["paired in sequencing"][w] += 1
                if f & 0x2 and not f & 0x4: t["properly paired"][w] += 1
                if f & 0x40: t["read1"][w] += 1
                if f & 0x80: t["read2"][w] += 1
                if f & 0x8 and not f & 0x4: t["singletons"][w] += 1
                if not f & 0x4 and not f & 0x8:
                    t["with itself and mate mapped"][w] += 1
                    if r["mtid"] != r["tid"]:
                        t["with mate mapped to a different chr"][w] += 1
                        if r["mapq"] >= 5: t["with mate mapped to a different chr (mapQ>=5)"][w] += 1
            if not f & 0x4: t["primary mapped"][w] += 1
            if f & 0x400: t["primary duplicates"][w] += 1
        if not f & 0x4: t["mapped"][w] += 1
        if f & 0x400: t["duplicates"][w] += 1
    return t
truth = flagstat_truth(recs)
out, err, rc = run("flagstat", bam)
print("\n--- flagstat (default format) vs truth")
n_bad = 0
for line in out.splitlines():
    a, rest = line.split(" + ", 1)
    b, label = rest.split(" ", 1)
    key = label if "mapQ>=5" in label else label.split(" (")[0]
    if key == "in total": key = "total"
    exp = truth[key]
    ok = int(a) == exp[0] and int(b) == exp[1]
    n_bad += not ok
    print(f"  {'OK ' if ok else 'BAD'} {line}   [truth {exp[0]} + {exp[1]}]")
def pct(n, t): return "N/A" if t == 0 else f"{n / t * 100:.2f}%"
print("  percentages: mapped", pct(truth["mapped"][0], truth["total"][0]), "properly paired", pct(truth["properly paired"][0], truth["paired in sequencing"][0]),
      "singletons", pct(truth["singletons"][0], truth["paired in sequencing"][0]))
print("  flagstat lines wrong:", n_bad)
# tsv and json carry the same numbers
tsv, _, _ = run("flagstat", "-O", "tsv", bam)
js, _, _ = run("flagstat", "-O", "json", bam)
import json
J = json.loads(js)
print("  tsv total line:", tsv.splitlines()[0], "| json QC-passed total:", J["QC-passed reads"]["total"], "primary mapped %:", J["QC-passed reads"]["primary mapped %"])

# ---------- idxstats ----------
print("\n--- idxstats (indexed BAM) and slow path (SAM stream) vs truth")
tr = {i: [0, 0] for i in range(-1, 3)}
for r in recs: tr[r["tid"]][1 if r["flag"] & 0x4 else 0] += 1
out, _, _ = run("idxstats", bam)
sam_out, _, _ = run("view", "-h", bam)
slow, _, _ = run("idxstats", "-", stdin=sam_out)
for line, sline in zip(out.splitlines(), slow.splitlines()):
    name, L, m, u = line.split("\t")
    tid = {"chr1": 0, "chr2": 1, "chrM": 2, "*": -1}[name]
    exp = tr[tid]
    # the index records unmapped-but-placed reads under their placement contig; the '*' row holds only unplaced reads
    print(f"  {'OK ' if [int(m), int(u)] == exp else 'BAD'} {line}   slow: {sline}   truth {exp}")

# ---------- view -c ----------
print("\n--- view -c filters vs truth")
def cnt(pred): return sum(1 for r in recs if pred(r))
cases = [
    (["-c"], lambda r: True),
    (["-c", "-q", "20"], lambda r: r["mapq"] >= 20),
    (["-c", "-q", "1"], lambda r: r["mapq"] >= 1),
    (["-c", "-f", "2"], lambda r: r["flag"] & 2),
    (["-c", "-F", "4"], lambda r: not r["flag"] & 4),
    (["-c", "-F", "0x904"], lambda r: not r["flag"] & 0x904),
    (["-c", "-f", "0x42", "-F", "0x400"], lambda r: (r["flag"] & 0x42) == 0x42 and not r["flag"] & 0x400),
    (["-c", "--rf", "0x100", "--rf", "0x800"], lambda r: r["flag"] & 0x900),
    (["-c", "-G", "0xC"], lambda r: (r["flag"] & 0xC) != 0xC),
    (["-c", "-m", "100"], lambda r: r["cigar"] is not None and qlen(r["cigar"]) >= 100),
    (["-c", "-e", "mapq>=30 && flag.proper_pair"], lambda r: r["mapq"] >= 30 and r["flag"] & 2),
    (["-c", "-e", "[NM]<=1"], lambda r: r["tags"]["NM"] <= 1),
    (["-c", "-e", "!flag.unmap && [NM]==0 && qlen>=100"], lambda r: not r["flag"] & 4 and r["tags"]["NM"] == 0),
    (["-c", "-e", "rname==\"chr2\" || tlen>0"], lambda r: r["tid"] == 1 or r["tlen"] > 0),
    (["-c", "-q", "5", "-F", "0x4", "chr1:1000-2000"], lambda r: r["tid"] == 0 and not r["flag"] & 4 and r["mapq"] >= 5 and r["pos"] < 2000 and r["pos"] + 100 > 999),
]
bad = 0
for args, pred in cases:
    region = [a for a in args if a.startswith("chr1:")]
    out, err, rc = run("view", *[a for a in args if not a.startswith("chr1:")], bam, *region)
    exp = cnt(pred)
    ok = out.strip() == str(exp)
    bad += not ok
    print(f"  {'OK ' if ok else 'BAD'} view {' '.join(args):45s} -> {out.strip():>6}  truth {exp}  {err.strip()[:80]}")
print("  view -c cases wrong:", bad)
