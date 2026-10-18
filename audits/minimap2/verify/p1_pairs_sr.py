"""P1: paired short reads under -x sr (pe.c mm_pair, format.c TLEN/flags).

Truth from the planted fragments: proper pair (0x2) expected for FR pairs whose
fragment fits -F (default 800: mm_pair allows a gap of F - len1 - len2 between the
mates), not for RF/FF; TLEN = +/- fragment length on the leftmost/rightmost mate
(SAM spec, outer coordinates; fragments shorter than the read are read through
into adapter that is soft-clipped); RNEXT/PNEXT and 0x20 from the mate's primary.
Also: one mate unique, the other in an exact two-copy repeat 3-20 kb away -- the
pairing must put the repeated mate on the copy next to its partner.
"""
import os, sys, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(31)
G = 4000000
ref = list(rand_seq(rng, G))
# exact two-copy repeats of 400 bp for the rescue class
reps = []
cur = 2000000
for i in range(40):
    a = cur; gap = rng.choice([3000, 8000, 20000]); b = a + 400 + gap
    ref[b:b + 400] = ref[a:a + 400]
    assert b + 400 < G
    reps.append((a, b))
    cur = b + 400 + 25000
refs = "".join(ref)
d = tmpdir(); fa = os.path.join(d, "ref.fa"); write_fasta(fa, [("chr1", refs)])
ADAPTER = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGGATGACTATCTCGTATGCCGTCTTCTGCTTGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
print(version(), f" reference {G} bp random, -x sr, 2 x {150} bp")

L = 150
r1s, r2s, truth = [], [], {}
cursor = 10000
def frag_pair(name, st, flen, ori):
    f = refs[st:st + flen]
    if flen >= L:
        a, b = f[:L], revcomp(f[-L:])
    else:  # read-through into adapter
        a = (f + ADAPTER)[:L]
        b = (revcomp(f) + ADAPTER)[:L]
    if ori == "RF":
        a, b = revcomp(f[:L]), f[-L:]
    elif ori == "FF":
        a, b = f[:L], f[-L:]
    r1s.append((name, a)); r2s.append((name, b))
    truth[name] = (st, flen, ori)

for flen in (100, 120, 150, 200, 300, 400, 500, 600, 640, 700, 760, 790, 800, 810, 840, 900, 1000, 1200):
    for k in range(6):
        for ori in ("FR", "RF", "FF"):
            if flen <= L and ori != "FR":  # at flen == L an RF pair is a swapped FR pair
                continue
            frag_pair(f"f{flen}_{ori}_{k}", cursor, flen, ori)
            cursor += flen + 3000
# swapped mates (read 1 is the reverse one) -- still FR
for flen in (300, 500):
    for k in range(6):
        st = cursor; f = refs[st:st + flen]
        name = f"swap{flen}_{k}"
        r1s.append((name, revcomp(f[-L:]))); r2s.append((name, f[:L]))
        truth[name] = (st, flen, "FR")
        cursor += flen + 3000
# dovetailed FR pairs (lh3/minimap2#1307): read 1 lost its first t bases (5' trimming), so
# read 2's alignment starts t bases before read 1's; fragment = read 2's span
dove = {}
for t in (2, 5, 10, 20):
    for k in range(6):
        st = cursor; f = refs[st:st + 150]
        name = f"dove{t}_{k}"
        r1s.append((name, f[t:])); r2s.append((name, revcomp(f[:150 - t])))
        dove[name] = t
        cursor += 3000
assert cursor < 2000000
# repeat class: mate 1 unique upstream of copy A or copy B, mate 2 inside the copy
rep_truth = {}
for i, (a, b) in enumerate(reps):
    for which, base in (("A", a), ("B", b)):
        flen = 350
        st = base + 400 - flen + 100   # mate 2's last 150 bp lie in the copy, mate 1 starts 50 bp upstream of it...
        st = base - 100                 # fragment starts 100 bp before the copy
        f = refs[st:st + flen]
        name = f"rep{i}{which}"
        r1s.append((name, f[:L])); r2s.append((name, revcomp(f[-L:])))
        truth[name] = (st, flen, "FR"); rep_truth[name] = (base, st + flen - L)
fq1 = os.path.join(d, "r1.fq"); fq2 = os.path.join(d, "r2.fq")
write_fastq(fq1, r1s); write_fastq(fq2, r2s)
recs = parse_sam(run(["-ax", "sr", "-t1", fa, fq1, fq2]))
prim = collections.defaultdict(dict)
for r in recs:
    if r["flag"] & 0x900:
        continue
    prim[r["qname"]][1 if r["flag"] & 0x40 else 2] = r

bad = collections.Counter(); rows = collections.defaultdict(lambda: collections.Counter())
examples = collections.defaultdict(list)
for name, (st, flen, ori) in truth.items():
    m = prim[name]
    if 1 not in m or 2 not in m:
        bad["missing"] += 1; continue
    a, b = m[1], m[2]
    cls = "rep" if name.startswith("rep") else ("swap" if name.startswith("swap") else f"{flen:5d} {ori}")
    both = not (a["flag"] & 4) and not (b["flag"] & 4)
    proper = bool(a["flag"] & 2) and bool(b["flag"] & 2)
    exp_proper = ori == "FR" and flen <= 800
    rows[cls]["n"] += 1
    rows[cls]["proper"] += proper
    if proper != exp_proper and both:
        rows[cls]["proper_wrong"] += 1
    # TLEN: + on the leftmost mate (equal starts: either), magnitude = fragment
    if both and ori == "FR":
        left, right = (a, b) if a["pos"] < b["pos"] or (a["pos"] == b["pos"] and not a["flag"] & 0x10) else (b, a)
        if not (left["tlen"] == flen and right["tlen"] == -flen):
            rows[cls]["tlen_wrong"] += 1
            examples[cls].append((name, a["pos"], a["cigar"], a["tlen"], b["pos"], b["cigar"], b["tlen"]))
    # RNEXT/PNEXT/0x20 consistency
    for x, y in ((a, b), (b, a)):
        if both and (x["pnext"] != y["pos"] or bool(x["flag"] & 0x20) != bool(y["flag"] & 0x10)):
            rows[cls]["mate_fields_wrong"] += 1
    if name in rep_truth:
        base, m2pos = rep_truth[name]
        rows[cls]["rep_mate2_correct"] += (b["pos"] - 1 == m2pos)
        rows[cls]["mapq_m2_sum"] += b["mapq"]
        rows[cls]["mapq_m2_ge20"] += b["mapq"] >= 20

print(f"{'class':12s} {'n':>3s} {'0x2':>4s} {'0x2 wrong':>9s} {'TLEN wrong':>10s} {'mate fields wrong':>17s}")
for cls in sorted(rows, key=lambda c: (c[0].isalpha(), c)):
    c = rows[cls]
    extra = ""
    if cls == "rep":
        extra = f"  mate 2 on the copy next to mate 1: {c['rep_mate2_correct']}/{c['n']}; mate 2 MAPQ >= 20: {c['mapq_m2_ge20']}/{c['n']} (mean {c['mapq_m2_sum'] / c['n']:.1f})"
    print(f"{cls:12s} {c['n']:3d} {c['proper']:4d} {c['proper_wrong']:9d} {c['tlen_wrong']:10d} {c['mate_fields_wrong']:17d}{extra}")
for cls, ex in examples.items():
    print(f"  TLEN examples {cls}: {ex[:3]}")
dv = collections.Counter()
for name, t in dove.items():
    m = prim[name]; a, b = m[1], m[2]
    dv[(t, bool(a["flag"] & 2 and b["flag"] & 2))] += 1
print("dovetailed FR pairs (read 2 starts t bp before read 1; not in the totals; lh3/minimap2#1307): "
      + ", ".join(f"t={t}: proper {dv[(t, True)]}/{dv[(t, True)] + dv[(t, False)]}" for t in (2, 5, 10, 20)))
print(f"missing records: {bad['missing']}")
tot_wrong = sum(c['proper_wrong'] + c['tlen_wrong'] + c['mate_fields_wrong'] for c in rows.values())
print(("ok  " if tot_wrong == 0 else "FAIL") + f" proper-pair flag, TLEN and mate fields vs the planted fragments ({tot_wrong} discrepancies)")

if os.environ.get("P1_DEBUG"):
    for name in sorted(rep_truth):
        base, m2pos = rep_truth[name]
        m = prim[name]
        a, b = m[1], m[2]
        if b["pos"] - 1 != m2pos:
            sec = [(r["pos"], r["flag"], r["mapq"], r["tags"].get("AS")) for r in recs if r["qname"] == name]
            print("REPDBG", name, "mate1", a["pos"], a["flag"], a["mapq"], "mate2", b["pos"], b["flag"], b["mapq"], "expected mate2 at", m2pos + 1, "all:", sec)
