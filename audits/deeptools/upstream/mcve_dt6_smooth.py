"""bamCoverage --smoothLength averages within each multiprocessing chunk, so the bins next
to a chunk boundary get a one-sided window. --region forces 1-Mb chunks; with 50-bp bins
and a 250-bp (5-bin) window the bins at 999,900-1,000,050 differ from a chromosome-wide
sliding mean, every other bin agrees."""
import subprocess, numpy as np, pysam

L = 2000000
rng = np.random.RandomState(0)
starts = rng.randint(0, L - 50, 40000)
with pysam.AlignmentFile("/tmp/s.u", "wb", header={"HD": {"VN": "1.0"}, "SQ": [{"SN": "chr1", "LN": L}]}) as fh:
    for i, s in enumerate(starts):
        a = pysam.AlignedSegment(); a.query_name = "r%d" % i; a.query_sequence = "A" * 50; a.flag = 0
        a.reference_id = 0; a.reference_start = int(s); a.mapping_quality = 30; a.cigar = ((0, 50),)
        a.query_qualities = pysam.qualitystring_to_array("I" * 50); fh.write(a)
pysam.sort("-o", "/tmp/s.bam", "/tmp/s.u"); pysam.index("/tmp/s.bam")
subprocess.run(["bamCoverage", "-b", "/tmp/s.bam", "-o", "/tmp/s.bg", "-of", "bedgraph", "-bs", "50", "--smoothLength", "250",
                "--region", "chr1:0:2000000"], check=True, capture_output=True)
got = np.zeros(L // 50)
for line in open("/tmp/s.bg"):
    c, s, e, v = line.split(); got[int(s) // 50:int(e) // 50] = float(v)
counts = np.zeros(L // 50)
for s in starts:
    counts[s // 50:(s + 49) // 50 + 1] += 1
ref = np.array([counts[max(0, i - 2):i + 3].mean() for i in range(len(counts))])
bad = np.flatnonzero(~np.isclose(got, ref, atol=1e-6))
print("bins differing from the chromosome-wide 5-bin mean:", [int(b * 50) for b in bad])
assert len(bad) == 0, "smoothed values differ next to the chunk boundary at 1,000,000"
