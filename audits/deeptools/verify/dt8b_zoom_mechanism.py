#!/usr/bin/env python3
"""DT8, mechanism: where the zoom-level error comes from.

Three synthetic bigWigs and one bamCoverage track are queried with pyBigWig's
default stats() (zoom levels) and with exact=True (intervals):
  A  three long intervals (background / peak / background): one zoom span of
     400,000 bp, larger than the 10-kb query, so the exact path is used
  B  random run lengths (multiples of 50 bp): one span of 15,952 bp, exact path
  C  50-bp aligned steps with one peak: span 800 bp, median error 0.38 %, 10 %
     at the peak bin
  D  the bamCoverage track of the DT8 harness (33,391 run-length-encoded
     intervals of variable length, spans 944 / 3,776 bp): median 3.4 %, max
     245 %, identical whether the same intervals are rewritten in one
     addEntries call, in calls of 1,000, or with the default maxZooms.
So the error is not in how deepTools writes the file but in the zoom summaries
of run-length-encoded tracks whose intervals straddle the zoom records; the
reader-side fix (exact=True) removes it.
"""
import os
import struct
import numpy as np
import pyBigWig
import _synth as S

print(S.version(), "pyBigWig", pyBigWig.__version__)


def spans(p):
    with open(p, "rb") as fh:
        h = fh.read(64)
        n = struct.unpack("<IHH", h[:8])[2]
        return [struct.unpack("<IIQQ", fh.read(24))[0] for _ in range(n)]


def err(path, vals, L, bs=10000):
    b = pyBigWig.open(path)
    r = []
    for s in range(0, L, bs):
        ex = np.nanmean(vals[s:s + bs])
        r.append(abs(b.stats("chr1", s, s + bs)[0] - ex) / ex)
    r = np.array(r)
    return "median %.2e, max %.2e" % (np.median(r), r.max())


d = S.tmpdir()
n = 400000
rng = np.random.RandomState(0)
# A
p = os.path.join(d, "A.bw")
bw = pyBigWig.open(p, "w"); bw.addHeader([("chr1", n)])
bw.addEntries(["chr1"] * 3, [0, 98000, 100000], ends=[98000, 100000, n], values=[1.0, 41.0, 1.0]); bw.close()
vals = np.ones(n); vals[98000:100000] = 41.0
print("A three long intervals: spans %s; 10-kb stats error %s" % (spans(p), err(p, vals, n)))
# B
starts, v, pos = [0], [], 0
vals = np.zeros(n)
while pos < n:
    Lr = 50 * rng.randint(1, 40); x = float(rng.gamma(2.0, 1.0)) + (40.0 if 98000 <= pos < 100000 else 0.0)
    vals[pos:min(n, pos + Lr)] = x; v.append(x); pos = min(n, pos + Lr); starts.append(pos)
p = os.path.join(d, "B.bw")
bw = pyBigWig.open(p, "w"); bw.addHeader([("chr1", n)])
bw.addEntries(["chr1"] * len(v), starts[:-1], ends=starts[1:], values=v); bw.close()
print("B random run lengths (x50 bp): spans %s; 10-kb stats error %s" % (spans(p), err(p, vals, n)))
# C
vals = rng.gamma(2.0, 1.0, n // 50).repeat(50); vals[99000:101000] += 40
p = os.path.join(d, "C.bw")
bw = pyBigWig.open(p, "w"); bw.addHeader([("chr1", n)])
bw.addEntries(["chr1"] * (n // 50), list(range(0, n, 50)), ends=list(range(50, n + 1, 50)), values=[float(x) for x in vals[::50]]); bw.close()
print("C 50-bp aligned steps: spans %s; 10-kb stats error %s" % (spans(p), err(p, vals, n)))
# D
rng2 = np.random.default_rng(71)
L = 2000000
w = np.ones(L)
for q in rng2.integers(0, L - 2000, 150):
    w[q:q + rng2.integers(300, 2000)] += rng2.integers(5, 40)
reads, frags = S.random_se_reads(rng2, 0, L, 300000, 50, weights=w)
bam = S.write_bam(os.path.join(d, "s.bam"), [("chr1", L)], reads)
p = os.path.join(d, "s.bw")
S.run(["bamCoverage", "-b", bam, "-o", p, "-bs", 50, "-p", 1])
h = pyBigWig.open(p); iv = h.intervals("chr1"); vals = np.array(h.values("chr1", 0, L))
print("D bamCoverage track: %d intervals, spans %s; 10-kb stats error %s" % (len(iv), spans(p), err(p, vals, L)))
st = [x[0] for x in iv]; en = [x[1] for x in iv]; vv = [x[2] for x in iv]
for label, chunk, mz in [("one addEntries call, maxZooms 10", len(iv), 10), ("calls of 1,000 intervals, maxZooms 10", 1000, 10), ("one call, default maxZooms", len(iv), None)]:
    q = os.path.join(d, "re.bw"); o = pyBigWig.open(q, "w")
    o.addHeader([("chr1", L)]) if mz is None else o.addHeader([("chr1", L)], maxZooms=mz)
    for i in range(0, len(iv), chunk):
        o.addEntries(["chr1"] * len(st[i:i + chunk]), st[i:i + chunk], ends=en[i:i + chunk], values=vv[i:i + chunk])
    o.close()
    print("  D rewritten (%s): spans %s; 10-kb stats error %s" % (label, spans(q), err(q, vals, L)))
