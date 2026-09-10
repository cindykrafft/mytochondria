#!/usr/bin/env python3
"""Held-up checks: ILLUMINACLIP 'simple' mode (single-end) against an as-coded port
and against the README's rule, on synthetic reads with planted adapters.

Usage: python3 heldup_illuminaclip_simple.py <trimmomatic.jar | build dir>

Part A  TruSeq3-SE adapters planted at every position, with substitution errors
        and N's: jar vs as-coded port (seeds + maximum-range score), record by record.
Part B  the same reads against the README's rule (plain sum of +0.6/-Q/10, no
        seed): how often the coded heuristics change the decision, and which one.
Part C  partial adapter at the 3' end, k = 1..33 bases: detection by adapter length.
Part D  the three adapter classes (short < 16, medium 16-23, long >= 24 nt) with
        thresholds 7 and 10.
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trimmomatic_ref as R

target = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
rng = random.Random(7)

IDX = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC"   # TruSeq3 IndexedAdapter (33 nt)
UNI = "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTA"   # TruSeq3 UniversalAdapter (33 nt)
tmp = os.path.join(os.environ.get("TMPDIR", "/tmp"), "trimmo_simple_%d" % os.getpid())
os.makedirs(tmp, exist_ok=True)
fa = os.path.join(tmp, "TruSeq3-SE.fa")
with open(fa, "w") as fh:
    fh.write(">TruSeq3_IndexedAdapter\n%s\n>TruSeq3_UniversalAdapter\n%s\n" % (IDX, UNI))


def plant(rng, n, adapter, pos, err, nrate=0.0):
    """read of n bases whose bases from `pos` on are the adapter (then random)."""
    insert = R.rand_seq(rng, pos)
    tail = adapter + R.rand_seq(rng, max(0, n - pos - len(adapter)))
    seq = (insert + tail)[:n]
    quals = R.rand_quals(rng, n, "mixed")
    # errors correlated with quality: p = 10^(-q/10), capped
    out = []
    for b, q in zip(seq, quals):
        u = rng.random()
        if u < nrate:
            out.append("N")
        elif u < nrate + err * min(1.0, 4 * 10 ** (-q / 10.0)):
            out.append(rng.choice([c for c in "ACGT" if c != b]))
        else:
            out.append(b)
    return "".join(out), quals


# ---------------------------------------------------------------- Part A
reads, truth = [], {}
i = 0
for err in (0.0, 0.5, 1.0, 2.0):
    for pos in range(0, 100):
        for rep in range(4):
            n = rng.choice([100, 100, 75, 150, 36])
            ad = rng.choice([IDX, UNI])
            seq, q = plant(rng, n, ad, pos, err, nrate=0.01)
            name = "a%d_p%d_e%s" % (i, pos, err); i += 1
            reads.append((name, seq, q)); truth[name] = pos
for k in range(2000):  # adapter-free reads
    n = rng.choice([100, 75, 150])
    seq = R.rand_seq(rng, n)
    reads.append(("f%d" % k, seq, R.rand_quals(rng, n, "mixed"))); truth["f%d" % k] = None
N = len(reads)
print("Part A: %d reads (%d with a planted TruSeq3 adapter at positions 0-99, %d adapter-free)" % (N, N - 2000, 2000))

clip = R.IlluminaClip(fa, 2, 30, 10)
for thr in (10, 7, 15):
    clip = R.IlluminaClip(fa, 2, 30, thr)
    out, log = R.run_se(target, reads, ["ILLUMINACLIP:%s:2:30:%d" % (fa, thr)])
    got = {n: s for n, s, _ in out}
    same = 0; diffs = []
    kept_len = {}
    for name, seq, q in reads:
        k1, _ = clip.process((seq, q))
        kept_len[name] = k1
        g = got.get(name)
        if (g is None and k1 is None) or (g is not None and k1 is not None and len(g) == k1):
            same += 1
        else:
            diffs.append((name, None if g is None else len(g), k1))
    clipped = sum(1 for n in kept_len if kept_len[n] is not None and kept_len[n] < len(dict((a, b) for a, b, _ in reads)[n]))
    print("  ILLUMINACLIP:TruSeq3-SE.fa:2:30:%-2d  jar == as-coded port on %d/%d reads; %d dropped, %d clipped, %d untouched (jar)"
          % (thr, same, N, sum(1 for n in got if False) + (N - len(got)), clipped, len(got) - clipped))
    for d in diffs[:5]:
        print("     mismatch:", d)
    if thr == 10:
        # exposure of the planted position
        exact = sum(1 for name, seq, q in reads if truth[name] is not None and name in got and len(got[name]) == truth[name])
        planted = sum(1 for name in truth if truth[name] is not None)
        fp = sum(1 for name, seq, q in reads if truth[name] is None and (name not in got or len(got[name]) != len(seq)))
        print("     planted adapters clipped at exactly the planted position: %d/%d; adapter-free reads touched: %d/2000" % (exact, planted, fp))

# ---------------------------------------------------------------- Part B
print("\nPart B: as-coded port vs the README's rule (plain sum, every offset), ILLUMINACLIP:...:2:30:10")
clip = R.IlluminaClip(fa, 2, 30, 10)
adapters = [("idx", IDX), ("uni", UNI)]
n_doc_diff = n_seed = n_range = n_both = 0
ex = []
for name, seq, q in reads:
    coded, _ = clip.process((seq, q))
    doc = R.simple_clip_doc(seq, q, adapters, 10)
    doc_keep = len(seq) if doc is None else (doc if doc > 0 else None)
    if coded != doc_keep:
        n_doc_diff += 1
        noseed, _ = clip.process((seq, q), use_seeds=False)
        norange, _ = clip.process((seq, q), use_maxrange=False)
        if noseed == doc_keep and norange != doc_keep:
            n_seed += 1
        elif norange == doc_keep and noseed != doc_keep:
            n_range += 1
        else:
            n_both += 1
        if len(ex) < 4:
            ex.append((name, coded, doc_keep, noseed, norange))
print("  reads where the coded result differs from the README rule: %d/%d" % (n_doc_diff, N))
print("    explained by the seed requirement alone: %d; by the maximum-range score alone: %d; by both/neither: %d" % (n_seed, n_range, n_both))
for e in ex:
    print("    e.g. %s: coded keep=%s, README keep=%s, coded-without-seeds=%s, coded-with-plain-sum=%s" % e)
# direction of the maximum-range effect
more = less = 0
for name, seq, q in reads:
    a, _ = clip.process((seq, q))
    b, _ = clip.process((seq, q), use_maxrange=False)
    if a != b:
        if a is None or (b is not None and a < b):
            more += 1
        else:
            less += 1
print("  maximum-range vs plain sum (same seeds): %d reads clipped more/dropped with max-range, %d clipped less" % (more, less))

# ---------------------------------------------------------------- Part C
print("\nPart C: partial IndexedAdapter at the 3' end of a 100 nt read, all Q35, no errors (ILLUMINACLIP:...:2:30:10)")
rows = []
for k in range(1, 34):
    recs = []
    for r in range(50):
        seq = R.rand_seq(rng, 100 - k) + IDX[:k]
        recs.append(("k%d_%d" % (k, r), seq, [35] * 100))
    out, _ = R.run_se(target, recs, ["ILLUMINACLIP:%s:2:30:10" % fa])
    got = {n: len(s) for n, s, _ in out}
    clipped = sum(1 for n, s, q in recs if got.get(n, 0) == 100 - k)
    port = sum(1 for n, s, q in recs if clip.process((s, q))[0] == 100 - k)
    rows.append((k, clipped, port))
print("  k(adapter bases) : clipped by jar / by port  (of 50); README threshold 10 needs k*0.602 >= 10, i.e. k >= 17")
print("  " + "  ".join("%d:%d/%d" % r for r in rows))

# ---------------------------------------------------------------- Part D
print("\nPart D: adapter classes. Custom adapters: short 12 nt, medium 20 nt, long 30 nt; planted at position 60 of 100 nt reads, Q35, no errors")
SH = "ACGTTGCAGCTA"; ME = "TGCATGCAGTCAGTCAGGAT"; LO = "GATCGGAAGAGCACACGTCTGAACTCCAGT"
fa2 = os.path.join(tmp, "classes.fa")
with open(fa2, "w") as fh:
    fh.write(">short\n%s\n>medium\n%s\n>long\n%s\n" % (SH, ME, LO))
for thr in (7, 10):
    clip2 = R.IlluminaClip(fa2, 2, 30, thr)
    for label, ad in (("short(12)", SH), ("medium(20)", ME), ("long(30)", LO)):
        recs = [("d%d" % r, R.rand_seq(rng, 60) + ad + R.rand_seq(rng, 40 - len(ad)), [35] * 100) for r in range(100)]
        out, _ = R.run_se(target, recs, ["ILLUMINACLIP:%s:2:30:%d" % (fa2, thr)])
        got = {n: len(s) for n, s, _ in out}
        cj = sum(1 for n, s, q in recs if got.get(n) == 60)
        cp = sum(1 for n, s, q in recs if clip2.process((s, q))[0] == 60)
        print("  threshold %2d  %-11s clipped at 60: jar %3d/100, port %3d/100  (full-length score %.2f)" % (thr, label, cj, cp, len(ad) * R.LOG10_4))
