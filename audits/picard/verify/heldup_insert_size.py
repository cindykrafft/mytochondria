"""Held-up check: CollectInsertSizeMetrics against an independent computation of every metric.

Truth follows the documented definitions: MEDIAN, MODE, MIN, MAX, MEDIAN_ABSOLUTE_DEVIATION over all
FR inserts (one per pair, insert size 0 and cross-contig pairs skipped, duplicates skipped by default),
MEAN and STANDARD_DEVIATION (sample SD) over the "core" after trimming inserts larger than
MEDIAN + DEVIATIONS * MAD (DEVIATIONS 10), WIDTH_OF_xx_PERCENT as the width of the symmetric window
around the median holding xx % of inserts, and the histogram. Two designs: (1) a discrete
distribution with a long right tail of chimeric-like inserts; (2) an even count with a half-integer
median. Usage: python heldup_insert_size.py [picard.jar]
"""
import os, sys, random, statistics, collections
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("picard:", version())
d = tmpdir()
rng = random.Random(11)
L = 200000
fa = write_fasta(os.path.join(d, "ref.fa"), [("chr1", rand_seq(rng, L))])

def truth(inserts, deviations=10.0):
    h = collections.Counter(inserts)
    n = len(inserts)
    s = sorted(inserts)
    med = statistics.median(s)
    mad = statistics.median(sorted(abs(x - med) for x in s))
    mode = max(sorted(h), key=lambda k: h[k])   # smallest key among ties
    width = int(med + deviations * mad)
    core = [x for x in inserts if x <= width]
    mean = statistics.fmean(core); sd = statistics.stdev(core) if len(core) > 1 else 0
    # widths: grow symmetric window around floor(median) one bin each side
    widths = {}
    lo = hi = int(med); covered = h.get(lo, 0); dist = 1
    def pct(): return covered / n
    for p in (10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 99):
        widths[p] = None
    while lo >= min(s) - 1 or hi <= max(s) + 1:
        for p in widths:
            if widths[p] is None and pct() >= p / 100: widths[p] = dist
        lo -= 1; hi += 1; dist += 2
        covered += h.get(lo, 0) + h.get(hi, 0)
    return dict(READ_PAIRS=n, MEDIAN_INSERT_SIZE=med, MODE_INSERT_SIZE=mode, MIN_INSERT_SIZE=min(s), MAX_INSERT_SIZE=max(s),
                MEDIAN_ABSOLUTE_DEVIATION=mad, MEAN_INSERT_SIZE=mean, STANDARD_DEVIATION=sd, **{f"WIDTH_OF_{p}_PERCENT": w for p, w in widths.items()})

def make(inserts, dup_inserts=()):
    recs = []
    for i, ins in enumerate(inserts):
        p1 = 1000 + i * 700
        recs += pair(f"p{i}", p1, p1 + ins - 100, rlen=100)
    for j, ins in enumerate(dup_inserts):
        p1 = 1000 + (len(inserts) + j) * 700
        recs += pair(f"d{j}", p1, p1 + ins - 100, rlen=100, dup=True)
    return recs

designs = {
 "design 1: 200 inserts around 300 plus 10 outliers 5000-50000": [rng.choice([280, 290, 300, 300, 300, 310, 320, 330]) for _ in range(200)] + [5000 * (k + 1) for k in range(10)],
 "design 2: even count, half-integer median": [200, 200, 210, 220, 220, 230, 240, 260, 300, 400],
 "design 3: 50 inserts with 3 duplicates flagged (excluded by default)": ([300] * 20 + [310] * 20 + [320] * 10, [1000, 1100, 1200]),
}
for label, ins in designs.items():
    dups = ()
    if isinstance(ins, tuple): ins, dups = ins
    bam = write_bam(os.path.join(d, "ins.bam"), make(ins, dups), [("chr1", L)])
    out = os.path.join(d, "ins.txt")
    run("CollectInsertSizeMetrics", "-I", bam, "-O", out, "-H", os.path.join(d, "ins.pdf"), "-R", fa)
    m, h = parse_metrics(out)
    m = [x for x in m if x["PAIR_ORIENTATION"] == "FR"][0]
    t = truth(ins)
    print(f"\n--- {label}")
    bad = 0
    for k, v in t.items():
        got = m[k]
        ok = abs(float(got) - float(v)) < 1e-4 if isinstance(v, (int, float)) else got == v
        bad += not ok
        print(f"  {k:28s} picard {got!s:12s} truth {v!s:12s} {'ok' if ok else 'MISMATCH'}")
    hist = h["All_Reads.fr_count"]
    exp_hist = collections.Counter(x for x in ins if x <= int(t["MEDIAN_INSERT_SIZE"] + 10 * t["MEDIAN_ABSOLUTE_DEVIATION"]))
    print(f"  histogram (trimmed to MEDIAN + 10 MAD): {'ok' if all(hist.get(k) == v for k, v in exp_hist.items()) and len(hist) == len(exp_hist) else 'MISMATCH ' + str(hist)}")
    print(f"  mismatches: {bad}")
