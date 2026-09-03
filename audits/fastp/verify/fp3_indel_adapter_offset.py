#!/usr/bin/env python3
"""FP3: the one-indel adapter search never leaves read position 0.

`AdapterTrimmer::trimBySequence` (src/adaptertrimmer.cpp:64-157 (function starts at :64)) scans the read
for the adapter at every offset `pos`. The exact-match loop passes the offset to
the comparison (`rdata + startOffset + pos`, :91-93), but the two gapped loops
that were added in v1.0.0 ("support one base insertion/deletion in SE mode
adapter trimming") do not:

    Matcher::matchWithOneInsertion(rdata, adata, cmplen, allowedMismatch);  // :110
    Matcher::matchWithOneInsertion(adata, rdata, cmplen, allowedMismatch);  // :127

`rdata` is the read from base 0. For every `pos` in [0, rlen-alen-1] the call is
byte-for-byte identical (same pointers, same cmplen, same allowance), so the
whole loop is one test of "does the read START with the adapter, with one indel";
`pos` only ever changes where the read is then cut. Consequence: an adapter that
occurs at the 3' end with one inserted or deleted base is never found.

Part A  reads carrying the adapter with one indel, at a known position
Part B  the shipped binary vs two independent ports (offset ignored / offset applied)
Part C  dependence on where the adapter sits in the read

Usage: python3 fp3_indel_adapter_offset.py [path-to-fastp]
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastp_ref import run_fastp  # noqa: E402

EXE = sys.argv[1] if len(sys.argv) > 1 else "./fastp"
random.seed(7)
print("fastp:", os.popen(f"{EXE} --version 2>&1").read().strip())

AD = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"  # Illumina TruSeq Read 1, 33 nt
NOFILT = ["-Q", "-L", "-G", "-w", "1"]


def rnd(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def insert_base(ad, p):
    return ad[:p] + ("G" if ad[p] != "G" else "T") + ad[p:]


def delete_base(ad, p):
    return ad[:p] + ad[p + 1:]


# --------------------------------------------------- ports of the C++ routines
def match_with_one_insertion(ins, normal, cmplen, diff_limit):
    """Port of Matcher::matchWithOneInsertion (src/matcher.cpp:10-45).

    `ins` carries one extra base relative to `normal`; both are compared over
    `cmplen` characters of `normal` and `cmplen`+1 of `ins`.
    """
    if cmplen <= 0 or len(ins) <= cmplen or len(normal) < cmplen:
        return False
    left = [0] * cmplen
    right = [0] * cmplen
    left[0] = 0 if ins[0] == normal[0] else 1
    right[cmplen - 1] = 0 if ins[cmplen] == normal[cmplen - 1] else 1
    for i in range(1, cmplen):
        left[i] = left[i - 1] + (ins[i] != normal[i])
    for i in range(cmplen - 2, -1, -1):
        right[i] = right[i + 1] + (ins[i + 1] != normal[i])
    for i in range(1, cmplen):
        if left[i - 1] + right[cmplen - 1] > diff_limit:
            return False
        if left[i - 1] + right[i] <= diff_limit:
            return True
    return False


def trim_by_sequence(seq, adapter, match_req=4, apply_offset=False):
    """Port of AdapterTrimmer::trimBySequence. apply_offset=False reproduces the
    shipped code (the gapped loops ignore `pos`); True is the intended search."""
    rlen, alen = len(seq), len(adapter)
    if alen < match_req:
        return seq, None
    start = -4 if alen >= 16 else (-3 if alen >= 12 else (-2 if alen >= 8 else 0))
    for pos in range(start, rlen - match_req):
        cmplen = min(rlen - pos, alen)
        allowed = cmplen // 8
        so = max(0, -pos)
        mism = sum(1 for i in range(so, cmplen) if adapter[i] != seq[i + pos])
        if mism <= allowed:
            return (seq[:pos] if pos > 0 else ""), ("exact", pos)
    for pos in range(0, rlen - match_req - 1):
        cmplen = min(rlen - pos - 1, alen)
        allowed = cmplen // 8 - 1
        ins = seq[pos:] if apply_offset else seq
        if match_with_one_insertion(ins, adapter, cmplen, allowed):
            return (seq[:pos] if pos > 0 else ""), ("insertion", pos)
    for pos in range(0, rlen - match_req):
        cmplen = min(rlen - pos, alen - 1)
        allowed = cmplen // 8 - 1
        norm = seq[pos:] if apply_offset else seq
        if match_with_one_insertion(adapter, norm, cmplen, allowed):
            return (seq[:pos] if pos > 0 else ""), ("deletion", pos)
    return seq, None


# ------------------------------------------------------------------- Part A
print("\n== Part A: 200 reads per group, 100 nt, adapter starts at base 40, -a "
      + AD)
groups = {
    "exact adapter (control)": lambda: AD,
    "adapter + 1 inserted base (p=5)": lambda: insert_base(AD, 5),
    "adapter + 1 inserted base (p=16)": lambda: insert_base(AD, 16),
    "adapter + 1 inserted base (p=28)": lambda: insert_base(AD, 28),
    "adapter - 1 deleted base (p=5)": lambda: delete_base(AD, 5),
    "adapter - 1 deleted base (p=16)": lambda: delete_base(AD, 16),
    "adapter with 1 substitution": lambda: AD[:16] + ("T" if AD[16] != "T" else "A") + AD[17:],
}
recs, truth = [], {}
for gi, (label, mk) in enumerate(groups.items()):
    for i in range(200):
        name = f"g{gi}_{i}"
        pre = rnd(40)
        s = (pre + mk() + rnd(60))[:100]
        recs.append((name, s, "I" * 100))
        truth[name] = 40
reads, _, _ = run_fastp(EXE, ["-a", AD] + NOFILT, records=recs)
print(f"  {'group':<34} {'trimmed to 40 nt':>17} {'untrimmed':>10} {'other':>7}")
for gi, label in enumerate(groups):
    ok = un = other = 0
    for i in range(200):
        got = reads.get(f"g{gi}_{i}")
        ln = len(got[0]) if got else 0
        ok += ln == 40
        un += ln == 100
        other += ln not in (40, 100)
    print(f"  {label:<34} {ok:>17} {un:>10} {other:>7}")

# ------------------------------------------------------------------- Part B
print("\n== Part B: 5,000 random reads vs the two ports "
      "(adapter at a random position, 0/1 indel/substitution)")
recs2 = []
kinds = {}
for i in range(5000):
    kind = random.choice(["none", "exact", "ins", "del", "sub"])
    kinds[f"x{i}"] = kind
    p = random.randint(0, 60)
    if kind == "none":
        s = rnd(100)
    else:
        ad = {"exact": AD,
              "ins": insert_base(AD, random.randrange(1, 33)),
              "del": delete_base(AD, random.randrange(1, 33)),
              "sub": AD[:5] + "T" + AD[6:]}[kind]
        s = (rnd(p) + ad + rnd(100))[:100]
    recs2.append((f"x{i}", s, "I" * 100))
reads2, _, _ = run_fastp(EXE, ["-a", AD] + NOFILT, records=recs2)
same_ship = same_fix = 0
ship_trim = fix_trim = 0


def after_dimer_filter(res, info, dimer_max_len=2):
    """A read trimmed to <= --dimer_max_len bases is dropped as an adapter dimer
    (seprocessor.cpp:255-260, a v1.x feature), so it is absent from the output."""
    if info is not None and len(res) <= dimer_max_len:
        return None
    return res


per_kind = {}
for name, seq, qual in recs2:
    got = reads2.get(name)
    got_seq = got[0] if got else None
    ship, sinfo = trim_by_sequence(seq, AD, apply_offset=False)
    fix, finfo = trim_by_sequence(seq, AD, apply_offset=True)
    same_ship += got_seq == after_dimer_filter(ship, sinfo)
    same_fix += got_seq == after_dimer_filter(fix, finfo)
    ship_trim += sinfo is not None
    fix_trim += finfo is not None
    k = per_kind.setdefault(kinds[name], [0, 0, 0])
    k[0] += 1
    k[1] += sinfo is not None
    k[2] += finfo is not None
print(f"  shipped binary == port with the offset IGNORED (as coded): {same_ship}/5000")
print(f"  shipped binary == port with the offset APPLIED (intended): {same_fix}/5000")
print(f"  reads trimmed: shipped {ship_trim}, with the offset applied {fix_trim}")
print(f"  {'planted':<12} {'reads':>6} {'shipped trims':>14} {'offset applied':>15}")
for k in ("none", "exact", "sub", "ins", "del"):
    n, s, f = per_kind[k]
    print(f"  {k:<12} {n:>6} {s:>14} {f:>15}")

# ------------------------------------------------------------------- Part C
print("\n== Part C: same read content, adapter (with one inserted base) moved along the read")
for p in (0, 1, 5, 20, 40, 60):
    recs3 = []
    for i in range(200):
        s = (rnd(p) + insert_base(AD, 8) + rnd(100))[:100]
        recs3.append((f"p{p}_{i}", s, "I" * 100))
    r3, _, _ = run_fastp(EXE, ["-a", AD] + NOFILT, records=recs3)
    lens = {}
    for i in range(200):
        got = r3.get(f"p{p}_{i}")
        ln = len(got[0]) if got else 0
        lens[ln] = lens.get(ln, 0) + 1
    print(f"  adapter starts at base {p:>2}: output lengths {dict(sorted(lens.items()))}"
          f"   (correct: {p})")
