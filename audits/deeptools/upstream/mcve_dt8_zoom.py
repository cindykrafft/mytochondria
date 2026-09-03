"""multiBigwigSummary reports zoom-level summaries, not the mean of the bin.
A bigWig with 50-bp steps (like a bamCoverage track) and one 2-kb peak that ends exactly at
a 10-kb bin boundary; the bin after the peak has no peak signal, yet its reported value
includes it. The exact mean (pyBigWig stats(exact=True) / numpy) does not."""
import subprocess, numpy as np, pyBigWig

n = 400000
vals = np.random.RandomState(0).gamma(2.0, 1.0, n // 50).repeat(50)
vals[98000:100000] += 40.0          # peak in bin 90,000-100,000 only
bw = pyBigWig.open("/tmp/z.bw", "w"); bw.addHeader([("chr1", n)])
bw.addEntries(["chr1"] * (n // 50), list(range(0, n, 50)), ends=list(range(50, n + 1, 50)), values=[float(x) for x in vals[::50]]); bw.close()
subprocess.run(["multiBigwigSummary", "bins", "-b", "/tmp/z.bw", "/tmp/z.bw", "-bs", "10000", "-o", "/tmp/z.npz", "--outRawCounts", "/tmp/z.tab"], check=True, capture_output=True)
rows = {int(l.split()[1]): float(l.split()[3]) for l in open("/tmp/z.tab") if not l.startswith("#")}
for s in (90000, 100000):
    print("bin %d-%d: multiBigwigSummary %.3f, exact mean %.3f, pyBigWig stats(exact=True) %.3f"
          % (s, s + 10000, rows[s], vals[s:s + 10000].mean(), pyBigWig.open("/tmp/z.bw").stats("chr1", s, s + 10000, exact=True)[0]))
assert abs(rows[100000] - vals[100000:110000].mean()) < 1e-3, "the bin after the peak is not the mean of its values"
