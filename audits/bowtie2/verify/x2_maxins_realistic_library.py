"""X2: how often the -X boundary effect (see x1) hits a library with a realistic
fragment-length distribution. 6,000 pairs of 100-bp mates, fragments drawn from
a normal distribution (mean 380, SD 70, truncated to 150-800), reads exact
copies of a 300-kb random reference, aligned with the default -X 500 and with
-X 1000. Every gap in a reported alignment is spurious. Reports the number of
pairs in the affected fragment band and the number of mates reported with a
gap, their MAPQ, and the TLEN error.
"""
import random, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _synth import *

rng = random.Random(33)
G = 300000
refs = rand_seq(rng, G)
d = tmpdir()
write_fasta(os.path.join(d, "ref.fa"), [("chr1", refs)])
idx = build_index(os.path.join(d, "ref.fa"), os.path.join(d, "ref"))
N = 6000
mates = []; fls = {}
for i in range(N):
    fl = int(round(rng.gauss(380, 70)))
    fl = min(800, max(150, fl))
    pos = rng.randint(100, G - 1000)
    m1, m2 = mate_pair(f"p{i}", refs, pos, fl, 100, 100)
    mates.append((fq(m1), fq(m2))); fls[f"p{i}"] = fl
print(f"bowtie2 {version()}  {N} pairs, fragment ~ N(380, 70): {sum(1 for f in fls.values() if f > 500)} fragments > 500, {sum(1 for f in fls.values() if 515 < f <= 535)} in 516-535")
for X in (500, 1000):
    recs, err = align(idx, mates=mates, args=["-X", str(X)])
    gapped = []; tlen_err = []
    by = collections.defaultdict(dict)
    for r in recs:
        by[r.qname][1 if r.flag & 64 else 2] = r
        if not (r.flag & 4) and ("I" in r.cigar or "D" in r.cigar):
            gapped.append(r)
    for q, pr in by.items():
        if pr[1].tlen != 0 and abs(pr[1].tlen) != fls[q]:
            tlen_err.append((fls[q], abs(pr[1].tlen)))
    mq = collections.Counter(r.mapq for r in gapped)
    band = collections.Counter(fls[r.qname] for r in gapped)
    print(f"\n-X {X}: {len(gapped)} mates reported with a gap (of {2 * N}); fragment lengths of those pairs: {min(band) if band else '-'}-{max(band) if band else '-'}; MAPQ of the gapped mates: {dict(sorted(mq.items()))}")
    print(f"   pairs whose |TLEN| differs from the true fragment length: {len(tlen_err)} (e.g. {tlen_err[:4]})")
    print(f"   summary: {parse_summary(err)}")
    report(f"-X {X}: no spurious gaps and every reported |TLEN| equals the fragment length", not gapped and not tlen_err)
