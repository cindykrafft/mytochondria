"""S1: alignment score and the per-alignment tags recomputed from the documented
scoring scheme (MANUAL.markdown "Scoring options"): mismatch penalty
MN + floor((MX-MN) * min(Q,40)/40), N penalty --np, gap penalties
--rdg/--rfg open + N*extend, local-mode match bonus --ma; XM/XO/XG/NM/MD/CIGAR/POS
against the construction; --ignore-quals, --phred64, --mp, --rdg, --rfg, --np,
--local; and the --score-min threshold boundary in local mode (G,20,8 at
L=100 is 56.84; SimpleFunc::f truncates it to 56).
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(3)
G = 40000
refs = rand_seq(rng, G)
d = tmpdir()
write_fasta(os.path.join(d, "ref.fa"), [("chr1", refs)])
idx = build_index(os.path.join(d, "ref.fa"), os.path.join(d, "ref"))
print(f"bowtie2 {version()}  reference {G} bp random")

def other(b):
    return rng.choice([x for x in "ACGT" if x != b])

def unambiguous_del(pos0, off, n):
    """deleting ref[pos0+off : pos0+off+n] is placed unambiguously if the deleted
    run differs from the bases flanking it."""
    s = refs[pos0 + off - 1]; e = refs[pos0 + off + n]
    seg = refs[pos0 + off:pos0 + off + n]
    return seg[0] != s and seg[-1] != e and seg[0] != e and seg[-1] != s

def unambiguous_ins(pos0, off, bases):
    s = refs[pos0 + off - 1]; e = refs[pos0 + off]
    return bases[0] != s and bases[-1] != e and bases[0] != e and bases[-1] != s

def build_cases(mode, L, qual_scheme, **kw):
    """A set of reads with every edit type, at assorted qualities."""
    reads = []; truth = {}
    pos = 1000
    k = 0
    def add(edits, qual, tag):
        nonlocal pos, k
        name = f"{mode}_{tag}_{k}"; k += 1
        fw = k % 2 == 0
        rd = make_read(name, refs, pos, L, fw=fw, edits=edits, qual=qual, mode=mode, **kw)
        reads.append(fq(rd)); truth[name] = rd
        pos += L + 200
    for q in (40, 35, 30, 25, 20, 15, 10, 5, 2, 0):
        offs = rng.sample(range(15, L - 15), 3)
        quals = [40] * L
        for o in offs: quals[o] = q
        add([("mm", o, other(refs[pos + o])) for o in offs], quals if qual_scheme == "mixed" else q, f"mm3_q{q}")
    for q in (41, 50, 60):   # qualities above 40 are capped at 40
        offs = rng.sample(range(15, L - 15), 2)
        quals = [30] * L
        for o in offs: quals[o] = q
        add([("mm", o, other(refs[pos + o])) for o in offs], quals, f"mm2_q{q}")
    add([("N", 30), ("N", 60)], 40, "N2")
    add([("N", o) for o in range(20, 20 + 12)], 40, "N12")   # 12 Ns of 100: within the 0.15*L ceiling
    for n in (1, 2, 3, 5):
        while not unambiguous_del(pos, 40, n):
            pos += 1
        add([("del", 40, n)], 40, f"del{n}")
    for n in (1, 2, 3, 5):
        ins = "".join(rng.choice("ACGT") for _ in range(n))
        while not unambiguous_ins(pos, 40, ins):
            pos += 1
        add([("ins", 40, ins)], 40, f"ins{n}")
    while not unambiguous_del(pos, 30, 2) or not unambiguous_ins(pos, 72, "GA"):   # the 2-bp deletion at read offset 30 shifts read offset 70 to reference offset 72
        pos += 1
    add([("mm", 20, other(refs[pos + 20])), ("del", 30, 2), ("ins", 70, "GA"), ("mm", 85, other(refs[pos + 85]))], [35] * L, "mixed")
    return reads, truth

def check(mode, L, args, qual_scheme="const", strict_md=True, **kw):
    reads, truth = build_cases(mode, L, qual_scheme, **kw)
    recs, err = align(idx, unpaired=reads, args=args)
    n = 0; bad = 0
    for r in recs:
        t = truth[r.qname]; n += 1
        got = dict(pos=r.pos, cigar=r.cigar, md=r.tags.get("MD"), nm=r.tags.get("NM"), xm=r.tags.get("XM"), xo=r.tags.get("XO"), xg=r.tags.get("XG"), AS=r.tags.get("AS"))
        exp = {k: t[k] for k in got}
        if not strict_md:
            exp.pop("md"); got.pop("md")
        if r.flag & 4 or got != exp:
            bad += 1
            diffs = {k: (exp[k], got[k]) for k in exp if exp[k] != got[k]}
            print(f"   {r.qname}: flag {r.flag} differs {diffs}")
    return report(f"{mode} L={L} {' '.join(args) or 'default'} ({qual_scheme} quals): {n - bad}/{n} reads with expected POS/CIGAR/MD/NM/XM/XO/XG/AS", bad == 0)

check("e2e", 100, [])
check("e2e", 100, [], qual_scheme="mixed")
check("e2e", 150, ["--very-sensitive"])
check("e2e", 100, ["--ignore-quals"], mm_min=6)
check("e2e", 100, ["--mp", "7,1"], mm_max=7, mm_min=1)
check("e2e", 100, ["--mp", "4"], mm_max=4, mm_min=2)
check("e2e", 100, ["--np", "3", "--n-ceil", "L,0,0.2"], npen=3)
check("e2e", 100, ["--rdg", "8,2", "--rfg", "4,4"], rdg=(8, 2), rfg=(4, 4))
check("local", 100, ["--local"])
check("local", 100, ["--local", "--ma", "3"], ma=3)
check("local", 150, ["--very-sensitive-local"])
check("local", 100, ["--local", "--mp", "5,3", "--rdg", "6,2"], mm_max=5, mm_min=3, rdg=(6, 2))

# --phred64: the same reads with qualities written at +64
reads, truth = build_cases("e2e", 100, "mixed")
reads64 = [(n, s, "".join(chr(ord(c) - 33 + 64) for c in q)) for n, s, q in reads]
recs, err = align(idx, unpaired=reads64, args=["--phred64"])
bad = sum(1 for r in recs if r.tags.get("AS") != truth[r.qname]["AS"])
report(f"e2e --phred64 (mixed quals): AS as expected on {len(recs) - bad}/{len(recs)}", bad == 0)

# --score-min boundary in local mode: L=100, default G,20,8 = 20 + 8 ln 100 = 56.84
print("\n--score-min boundary, --local, L=100 (manual: minimum score 20 + 8.0*ln(L) = 56.84):")
for nmatch in (27, 28, 29):
    pos0 = 30000
    seq = refs[pos0:pos0 + nmatch] + "".join({"A": "C", "C": "A", "G": "T", "T": "G"}[b] for b in refs[pos0 + nmatch:pos0 + 100])
    recs, err = align(idx, unpaired=[(f"m{nmatch}", seq, "I" * 100)], args=["--local", "-L", "20", "-N", "1", "-i", "C,1,0", "-D", "50", "-R", "5"])
    r = recs[0]
    st = "unaligned" if r.flag & 4 else f"aligned AS:i:{r.tags['AS']} CIGAR {r.cigar} YT {r.tags.get('YT')}"
    print(f"   {nmatch} matching bases then complement bases (best local score {2 * nmatch}): {st}")
r56 = [r for r in align(idx, unpaired=[("m28", refs[30000:30028] + "".join({"A": "C", "C": "A", "G": "T", "T": "G"}[b] for b in refs[30028:30100]), "I" * 100)], args=["--local", "-L", "20", "-N", "1", "-i", "C,1,0", "-D", "50", "-R", "5"])[0]]
report("score 56 is rejected under the documented threshold 56.84", bool(r56[0].flag & 4),
       "" if r56[0].flag & 4 else "(reported as valid: the threshold is truncated toward zero to 56)")
