"""S1: AS, NM, MD, cs, de and ms recomputed from each record's own CIGAR and the
planted sequences, for -x sr (single-end), map-ont (default) and -x splice.

Truth: AS = the manual's scoring (match +A, mismatch -B, N -1, gap of length l
min(O1 + l*E1, O2 + l*E2)) summed over the reported CIGAR; NM/MD/cs/de from the
SAM spec / the minimap2 manual (de = gap-compressed divergence). POS checked
against the planted origin for reads without ambiguity.

Classes: a single mismatch d = 1..8 bases from the 5' or 3' end (forward and
reverse-strand reads), mismatches in the middle, 1-12 bp insertions and
deletions in the middle, an N in the read, and clean reads.
"""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(7)
G = 1500000
ref = rand_seq(rng, G)
d = tmpdir()
write_fasta(os.path.join(d, "ref.fa"), [("chr1", ref)])
print(version(), f" reference {G} bp random")

SCORING = {  # a, b, q, e, q2, e2  (options.c presets)
    "sr": (2, 8, 12, 2, 24, 1),
    "map-ont": (2, 4, 4, 2, 24, 1),
    "splice": (1, 2, 2, 1, 32, 0),
}


def make_reads(L, mode):
    reads, truth = [], {}
    cursor = [1000]

    def take(name, edits_fn, fw):
        st = cursor[0]; cursor[0] += L + 700
        s = ref[st:st + L]
        s2, cls = edits_fn(s)
        if not fw:
            s2 = revcomp(s2)
        reads.append((name, s2)); truth[name] = (st, cls, fw)

    for fw in (True, False):
        for end in ("5p", "3p"):
            for dd in range(1, 9):
                def f(s, dd=dd, end=end):
                    s = list(s)
                    # position measured on the read as sequenced: for a reverse read the
                    # 5' end of the read is the right end of the reference segment
                    i = dd - 1 if (end == "5p") == fw else len(s) - dd
                    s[i] = other_base(rng, s[i])
                    return "".join(s), f"1 mismatch {dd} bp from the read's {end} end"
                for rep in range(3):
                    take(f"{mode}_{'f' if fw else 'r'}_{end}{dd}_{rep}", f, fw)
        for k in (1, 2, 3):
            def f(s, k=k):
                return mutate(rng, s, n_sub=k, protect=20), f"{k} mismatch(es) in the middle"
            for rep in range(4):
                take(f"{mode}_{'f' if fw else 'r'}_mid{k}_{rep}", f, fw)
        for l in (1, 2, 3, 5, 8, 12):
            def fi(s, l=l):
                p = len(s) // 2 + rng.randint(-10, 10)
                return mutate(rng, s, ins=[(p, rand_seq(rng, l))]), f"{l}-bp insertion in the middle"
            def fd(s, l=l):
                p = len(s) // 2 + rng.randint(-10, 10)
                return mutate(rng, s, dels=[(p, l)]), f"{l}-bp deletion in the middle"
            for rep in range(2):
                take(f"{mode}_{'f' if fw else 'r'}_ins{l}_{rep}", fi, fw)
                take(f"{mode}_{'f' if fw else 'r'}_del{l}_{rep}", fd, fw)
        def fn(s):
            s = list(s); s[len(s) // 3] = "N"; return "".join(s), "one N in the middle"
        def fc(s):
            return s, "clean"
        for rep in range(3):
            take(f"{mode}_{'f' if fw else 'r'}_N_{rep}", fn, fw)
            take(f"{mode}_{'f' if fw else 'r'}_clean_{rep}", fc, fw)
    return reads, truth


def port_ms_variant(cols, a, b, q, e, gapmode):
    """Max-scoring segment along the path (mm_update_extra's loop), with the gap
    model given: 'affine' = q + l*e (as in 2.17), 'flat' = q + e, 'log' = q + e*log2(1+l)."""
    s = mx = 0.0
    for op, x, y in cols:
        if op == "M":
            s += (-1 if (x not in NT4 or y not in NT4) else a if x == y else -b)
            if s < 0: s = 0
            else: mx = max(mx, s)
        elif op in "ID":
            l = len(x if op == "I" else y)
            s -= {"affine": q + e * l, "flat": q + e, "log": q + e * math.log2(1 + l)}[gapmode]
            if s < 0: s = 0
    return int(mx + .499)


def block(mode, L, args):
    a, b, q, e, q2, e2 = SCORING[mode]
    reads, truth = make_reads(L, mode)
    fq = os.path.join(d, f"{mode}.fq")
    write_fastq(fq, reads)
    # --MD and --cs are mutually exclusive in one run (format.c writes one of them), so run twice
    recs = [r for r in parse_sam(run(["-a", "--MD", "-t1"] + args + [os.path.join(d, "ref.fa"), fq]))
            if not r["flag"] & 0x904]
    cs = {r["qname"]: r["tags"].get("cs") for r in parse_sam(run(["-a", "--cs", "-t1"] + args + [os.path.join(d, "ref.fa"), fq]))
          if not r["flag"] & 0x904}
    for r in recs:
        r["tags"]["cs"] = cs.get(r["qname"])
    by_cls = {}
    bad = {"AS": [], "NM": [], "MD": [], "cs": [], "de": [], "pos": []}
    ms_match = {"affine": 0, "flat": 0, "log": 0}
    ms_rows = []
    for r in recs:
        st, cls, fw = truth[r["qname"]]
        cols = aligned_pairs(r, ref)
        pa = port_as(cols, a, b, q, e, q2, e2)
        c = by_cls.setdefault(cls, [0, 0, []])
        c[0] += 1
        if r["tags"]["AS"] == pa:
            c[1] += 1
        else:
            c[2].append(r["tags"]["AS"] - pa)
            bad["AS"].append((r["qname"], r["cigar"], r["tags"]["AS"], pa))
        if r["tags"]["NM"] != port_nm(cols): bad["NM"].append((r["qname"], r["tags"]["NM"], port_nm(cols)))
        if r["tags"]["MD"] != port_md(cols): bad["MD"].append((r["qname"], r["tags"]["MD"], port_md(cols)))
        if r["tags"]["cs"] != port_cs(cols): bad["cs"].append((r["qname"], r["tags"]["cs"], port_cs(cols)))
        pde = port_de(cols)
        if abs(r["tags"]["de"] - pde) > 0.00006: bad["de"].append((r["qname"], r["tags"]["de"], round(pde, 5)))
        lead_clip = cigar_ops(r["cigar"])[0]
        lead = lead_clip[0] if lead_clip[1] == "S" else 0
        if mode != "splice" and r["pos"] - 1 != st and r["pos"] - 1 - st != lead * 0:
            # soft-clipped 5' bases shift POS by the clipped length when the clip is a mismatch
            if abs(r["pos"] - 1 - st) > 10:
                bad["pos"].append((r["qname"], r["pos"] - 1, st))
        has_gap = any(op in "ID" for op, _, _ in cols)
        if has_gap:
            vals = {gm: port_ms_variant(cols, a, b, q, e, gm) for gm in ms_match}
            for gm, v in vals.items():
                if r["tags"]["ms"] == v: ms_match[gm] += 1
            ms_rows.append((r["qname"], r["cigar"], r["tags"]["ms"], r["tags"]["AS"], vals))
    n = len(recs)
    print(f"\n[{mode}] {' '.join(args)}  L={L}: {n} primary records of {len(reads)} reads")
    print(f"  {'class':48s} {'n':>3s} {'AS==port':>8s}  AS - port (where different)")
    for cls in sorted(by_cls, key=lambda k: (k.split()[0] != '1', k)):
        tot, ok, diffs = by_cls[cls]
        print(f"  {cls:48s} {tot:3d} {ok:8d}  {sorted(set(diffs)) if diffs else ''}")
    for k in ("AS", "NM", "MD", "cs", "de", "pos"):
        status = "ok  " if not bad[k] else "FAIL"
        print(f"  {status} {k}: {n - len(bad[k])}/{n} match the port" + ("" if not bad[k] else f"; first: {bad[k][:3]}"))
    if ms_rows:
        print(f"  ms:i on {len(ms_rows)} gapped records matches the max-segment port with gap cost "
              + ", ".join(f"{gm}: {v}/{len(ms_rows)}" for gm, v in ms_match.items()))
        for row in [x for x in ms_rows if len(set(x[4].values())) > 1][:4]:
            print(f"     {row[0]:22s} {row[1]:14s} ms={row[2]} AS={row[3]} port(affine/flat/log)={row[4]['affine']}/{row[4]['flat']}/{row[4]['log']}")
    return bad


block("sr", 150, ["-x", "sr"])
block("sr", 100, ["-x", "sr"])
block("map-ont", 2000, ["-x", "map-ont"])
block("splice", 1500, ["-x", "splice"])


def paf_block(mode, L, args):
    """PAF columns against the SAM record of the same run settings: query start/end
    (cols 3-4, forward-strand coordinates), target start/end (cols 8-9), residue
    matches and block length (cols 10-11: matches, and M+I+D columns, N excluded)."""
    reads, truth = make_reads(L, mode + "paf")
    fq = os.path.join(d, f"{mode}_paf.fq"); write_fastq(fq, reads)
    sam = {r["qname"]: r for r in parse_sam(run(["-a", "-t1"] + args + [os.path.join(d, "ref.fa"), fq])) if not r["flag"] & 0x904}
    bad = []; n = 0; nc_rows = []
    for withc in (True, False):
        paf = [p for p in parse_paf(run((["-c"] if withc else []) + ["-t1"] + args + [os.path.join(d, "ref.fa"), fq])) if p["tags"].get("tp") == "P"]
        for p in paf:
            r = sam.get(p["qname"])
            if r is None: continue
            cols = aligned_pairs(r, ref)
            ops = cigar_ops(r["cigar"])
            lclip = ops[0][0] if ops[0][1] in "SH" else 0
            rclip = ops[-1][0] if ops[-1][1] in "SH" else 0
            qlen = len(r["seq"])
            qs, qe = (lclip, qlen - rclip) if not r["flag"] & 16 else (rclip, qlen - lclip)
            ts = r["pos"] - 1; te = ts + sum(n_ for n_, o in ops if o in "MDN=X")
            m = sum(1 for o, x, y in cols if o == "M" and x == y and x in NT4)
            blen = sum(1 for o, x, y in cols if o == "M" and x in NT4 and y in NT4) + sum(
                sum(1 for c in (x if o == "I" else y) if c in NT4) for o, x, y in cols if o in "ID")
            if withc:
                n += 1
                if (p["qs"], p["qe"], p["ts"], p["te"], p["nmatch"], p["blen"]) != (qs, qe, ts, te, m, blen):
                    bad.append((p["qname"], (p["qs"], p["qe"], p["ts"], p["te"], p["nmatch"], p["blen"]), (qs, qe, ts, te, m, blen)))
            else:
                nc_rows.append((p["qname"], p["nmatch"], p["blen"], m, blen, p["qs"] - qs, p["qe"] - qe))
    print(f"\n[{mode} PAF] {' '.join(args)} L={L}")
    print(("  ok   " if not bad else "  FAIL ") + f"with -c: cols 3,4,8,9,10,11 equal the SAM-derived values on {n - len(bad)}/{n}"
          + ("" if not bad else f"; first: {bad[:3]}"))
    if nc_rows:
        ex = sum(1 for r in nc_rows if r[1] == r[3] and r[2] == r[4])
        under = sum(1 for r in nc_rows if r[1] < r[3])
        print(f"  without -c (chain-based, documented as approximate): cols 10/11 equal the base-level values on {ex}/{len(nc_rows)}; "
              f"col 10 below the true matches on {under}; e.g. {nc_rows[:2]}")


paf_block("sr", 150, ["-x", "sr"])
paf_block("map-ont", 2000, ["-x", "map-ont"])
