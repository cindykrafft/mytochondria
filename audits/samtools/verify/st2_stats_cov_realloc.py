"""ST2: `samtools stats` realloc_buffers (stats.c) copies the pending coverage
ring buffer with memcpy lengths given in elements where bytes are required, so
when a read longer than every read seen so far forces the buffers to grow
while coverage is pending near the end of the ring, three quarters of that
pending coverage is dropped from the COV distribution.  Fires on mixed-length
data (a >=300-bp read after shorter ones; long-read data with growing lengths).
Usage: python st2_stats_cov_realloc.py [samtools-binary]
"""
import os, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from _synth import *

print("samtools:", version())
d = tmpdir()
refs = [("chr1", 2_000_000)]

def check(label, recs, extra=()):
    bam = write_bam(os.path.join(d, label + ".bam"), recs, refs)
    out, err, rc = run("stats", *extra, bam)
    got = parse_cov(out)
    exp = dict(cov_hist(depth_truth(recs, 0)))
    ok = got == exp
    tot_got = sum(k * v for k, v in got.items()); tot_exp = sum(k * v for k, v in exp.items())
    print(f"\n[{label}]  {'OK' if ok else 'MISMATCH'}")
    print("  truth COV   :", dict(sorted(exp.items()))[:20] if False else dict(sorted(exp.items())) if len(exp) <= 12 else f"{len(exp)} depth values, {sum(exp.values())} positions, sum depth {tot_exp}")
    print("  samtools COV:", dict(sorted(got.items())) if len(got) <= 12 else f"{len(got)} depth values, {sum(got.values())} positions, sum depth {tot_got}")
    if err.strip(): print("  stderr:", err.strip()[:300])
    return got, exp, out

def summarize(h):
    n = sum(h.values()); s = sum(k * v for k, v in h.items())
    ks = sorted(h)
    cum, med = 0, None
    for k in ks:
        cum += h[k]
        if med is None and cum >= n / 2: med = k
    return n, s / n if n else 0, med, max(ks) if ks else 0

# --- D. realloc path: 100-bp reads pending near the end of the ring (positions 1400-1500 mod 1500), then a 350-bp read
recs = [simple_read(f"s{i}", 1400 + i * 5, "100M") for i in range(10)] + [simple_read("long", 1450, "350M")]
check("D_realloc_with_pending_coverage_near_ring_end", recs)
# D2: same reads but the long read comes first (nothing pending at reallocation): correct
recs = [simple_read("long", 1300, "350M")] + [simple_read(f"s{i}", 1400 + i * 5, "100M") for i in range(10)]
check("D2_realloc_with_empty_buffer", recs)

# --- E. long-read style: 200 reads with lengths growing 1-20 kb (each new maximum reallocates the ring)
random.seed(2)
recs = []
pos = 0
for i in range(200):
    L = 1000 + i * 100
    pos += random.randrange(50, 400)
    recs.append(simple_read(f"L{i}", pos, f"{L}M"))
got, exp, _ = check("E_growing_long_reads", recs)
for name, h in (("truth", exp), ("samtools", got)):
    n, mean, med, mx = summarize(h)
    print(f"  {name:9s}: covered positions {n}, mean depth over covered {mean:.2f}, median {med}, max {mx}")
