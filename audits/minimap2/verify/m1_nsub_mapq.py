"""M1: the n_sub term of the MAPQ (hit.c mm_set_parent / mm_set_mapq2).

mm_set_parent() counts, for each primary hit, the overlapping secondary hits that
are "nearly as good" (n_sub; MAPQ -= 4.343*ln(n_sub+1)). It is called twice per
read: on the chains (chain_post) and again after base-level alignment
(align_regs). Every primary found in a call starts from n_sub = 0
(`ri->n_sub = 0`, hit.c:182) except the first, r[0] (hit.c:133), which keeps the
count from the chaining pass and adds the second pass on top.

This harness runs reads drawn from two-copy repeats of known divergence through
three builds given in $MM2 (tested build), $MM2_FIX (r[0].n_sub = 0 added at
hit.c:133) and $MM2_INSTR (master + stderr print of r[0].n_sub on entry to and
exit from each mm_set_parent call), and reports
  - from the instrumented build: how often r[0] enters the post-alignment call
    with a non-zero n_sub carried over from chaining,
  - the MAPQ of the same reads on the tested and fixed builds, per class, with
    the placement truth (primary within 50 bp of the copy the read came from).
"""
import os, sys, random, subprocess, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

FIX = os.environ.get("MM2_FIX")
INSTR = os.environ.get("MM2_INSTR")
rng = random.Random(23)
G = 5000000
ref = list(rand_seq(rng, G))
fams = []  # (kind, div, posA, posB, length)
cursor = 20000
spec = []
for div in (0.0, 0.002, 0.005, 0.01, 0.02, 0.04):
    for rep in range(6):
        spec.append(("long", div, 12000))
for div in (0.0, 0.005, 0.01, 0.02, 0.03, 0.05):
    for rep in range(12):
        spec.append(("short", div, 1200))
for kind, div, R in spec:
    posA = cursor; posB = cursor + R + 10000
    seg = ref[posA:posA + R]
    copy = list(seg)
    nsub = int(round(div * R))
    for p in rng.sample(range(R), nsub):
        copy[p] = other_base(rng, copy[p])
    ref[posB:posB + R] = copy
    fams.append((kind, div, posA, posB, R))
    cursor = posB + R + 10000
assert cursor < G
refs = "".join(ref)
d = tmpdir()
fa = os.path.join(d, "ref.fa")
write_fasta(fa, [("chr1", refs)])
print(version(), f" reference {G} bp, {len(fams)} two-copy repeat families")

long_reads, short1, short2, truth = [], [], [], {}
for fi, (kind, div, posA, posB, R) in enumerate(fams):
    for c, base in (("A", posA), ("B", posB)):
        if kind == "long":
            for k in range(6):
                L = rng.randint(2000, 6000)
                st = base + rng.randint(0, R - L)
                s = noisy(rng, refs[st:st + L], sub=0.03, ins=0.015, dele=0.015)
                fw = rng.random() < .5
                name = f"L{fi}_{c}_{k}_d{div}"
                long_reads.append((name, s if fw else revcomp(s)))
                truth[name] = (st, div)
        else:
            for k in range(10):
                frag = rng.randint(300, 500)
                st = base + rng.randint(0, R - frag)
                f = refs[st:st + frag]
                r1 = mutate(rng, f[:150], n_sub=rng.choice([0, 0, 1, 2]))
                r2 = revcomp(mutate(rng, f[-150:], n_sub=rng.choice([0, 0, 1, 2])))
                name = f"S{fi}_{c}_{k}_d{div}"
                short1.append((name, r1)); short2.append((name, r2))
                truth[name] = (st, div)
lfq = os.path.join(d, "long.fq"); write_fastq(lfq, long_reads)
s1fq = os.path.join(d, "s_1.fq"); write_fastq(s1fq, short1)
s2fq = os.path.join(d, "s_2.fq"); write_fastq(s2fq, short2)


def run_bin(binpath, args, env=None):
    p = subprocess.run([binpath] + args, capture_output=True, text=True, env=env)
    return p.stdout, p.stderr


def primaries(sam):
    out = {}
    for r in parse_sam(sam):
        if r["flag"] & 0x904:
            continue
        key = r["qname"] + ("/2" if r["flag"] & 0x80 else "")
        out[key] = r
    return out


def correct(r, st, frag_or_len_slack=60):
    base = r["qname"].split("_")[1]
    return r["rname"] == "chr1" and abs((r["pos"] - 1) - st) <= 7000  # same copy (copies are >= 16 kb apart)


cases = [("long reads, map-ont", ["-ax", "map-ont", "-t1", fa, lfq]),
         ("short pairs, -x sr", ["-ax", "sr", "-t1", fa, s1fq, s2fq])]
for label, args in cases:
    print(f"\n== {label}")
    if INSTR:
        env = dict(os.environ, MM_NSUB_DEBUG="1")
        _, err = run_bin(INSTR, args, env)
        enters = [l.split("\t") for l in err.splitlines() if l.startswith("NSUB\tenter")]
        tot = len(enters)
        carried = [e for e in enters if e[5] == "r0.has_p=1" and e[4] != "r0.n_sub=0"]
        aligned_calls = [e for e in enters if e[5] == "r0.has_p=1"]
        print(f"  instrumented: {tot} mm_set_parent calls; {len(aligned_calls)} after alignment; "
              f"r[0] enters {len(carried)} of those with n_sub > 0 carried over from chaining "
              f"(values: {dict(collections.Counter(e[4] for e in carried))})")
    out_t, _ = run_bin(MM2, args)
    out_f, _ = run_bin(FIX, args)
    pt, pf = primaries(out_t), primaries(out_f)
    rows = collections.defaultdict(lambda: [0, 0, 0, 0, collections.Counter(), [], []])
    thr = collections.Counter()
    for k, rt in pt.items():
        rf = pf.get(k)
        if rf is None or rt["flag"] & 4:
            continue
        name = rt["qname"]
        st, div = truth[name]
        ok = abs((rt["pos"] - 1) - st) <= 7000
        row = rows[div]
        row[0] += 1
        if rt["mapq"] != rf["mapq"]:
            row[1] += 1
            row[4][rf["mapq"] - rt["mapq"]] += 1
            if ok: row[2] += 1
            row[5].append(rt["mapq"]); row[6].append(rf["mapq"])
            for t in (1, 5, 10, 20, 30, 60):
                if (rt["mapq"] >= t) != (rf["mapq"] >= t):
                    thr[t] += 1
        if (rt["rname"], rt["pos"], rt["flag"] & 0x10, rt["cigar"]) != (rf["rname"], rf["pos"], rf["flag"] & 0x10, rf["cigar"]):
            row[3] += 1
    print(f"  {'divergence':>10s} {'records':>7s} {'MAPQ differs':>12s} {'of which placed correctly':>26s} {'position/CIGAR differs':>23s}  fixed - tested MAPQ")
    tot_n = tot_d = tot_ok = 0
    for div in sorted(rows):
        n, nd, nok, npos, delta, _, _ = rows[div]
        tot_n += n; tot_d += nd; tot_ok += nok
        print(f"  {div:10.3f} {n:7d} {nd:12d} {nok:26d} {npos:23d}  {dict(sorted(delta.items()))}")
    print(f"  total: {tot_n} mapped primary records, MAPQ differs on {tot_d} ({100.0 * tot_d / max(tot_n, 1):.1f} %), "
          f"{tot_ok} of them placed on the copy they came from")
    print(f"  records whose MAPQ crosses a threshold between the builds: " + ", ".join(f">={t}: {thr[t]}" for t in (1, 5, 10, 20, 30, 60)))
    # placement accuracy among reads that pass MAPQ>=20 on each build
    for nm, P in (("tested", pt), ("fixed", pf)):
        pas = [r for r in P.values() if not r["flag"] & 4 and r["mapq"] >= 20]
        wrong = [r for r in pas if abs((r["pos"] - 1) - truth[r["qname"]][0]) > 7000]
        print(f"  {nm:6s} build: {len(pas)} records with MAPQ >= 20, {len(wrong)} on the wrong copy")
