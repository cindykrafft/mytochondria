"""bamCoverage --normalizeUsing BPM writes the CPM track: the two bigWigs are identical,
and the BPM values sum to (bins per read) * 1e6 over the genome, not to 1e6 as the
documented definition (reads per bin / sum of all reads per bin in millions) implies."""
import subprocess, numpy as np, pysam, pyBigWig

L = 100000
with pysam.AlignmentFile("/tmp/c.u", "wb", header={"HD": {"VN": "1.0"}, "SQ": [{"SN": "chr1", "LN": L}]}) as fh:
    for i, s in enumerate(np.random.RandomState(0).randint(0, L - 100, 5000)):
        a = pysam.AlignedSegment(); a.query_name = "r%d" % i; a.query_sequence = "A" * 100; a.flag = 0
        a.reference_id = 0; a.reference_start = int(s); a.mapping_quality = 30; a.cigar = ((0, 100),)
        a.query_qualities = pysam.qualitystring_to_array("I" * 100); fh.write(a)
pysam.sort("-o", "/tmp/c.bam", "/tmp/c.u"); pysam.index("/tmp/c.bam")
tracks = {}
for norm in ["CPM", "BPM"]:
    subprocess.run(["bamCoverage", "-b", "/tmp/c.bam", "-o", "/tmp/%s.bw" % norm, "-bs", "50", "--normalizeUsing", norm], check=True, capture_output=True)
    tracks[norm] = np.array(pyBigWig.open("/tmp/%s.bw" % norm).values("chr1", 0, L))[::50]
print("BPM == CPM bit for bit:", np.array_equal(tracks["CPM"], tracks["BPM"]))
print("sum of BPM over all bins: %.0f (documented definition gives 1e6)" % np.nansum(tracks["BPM"]))
assert not np.array_equal(tracks["CPM"], tracks["BPM"]), "BPM and CPM produced the same track"
