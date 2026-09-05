import subprocess, pysam

def bam(path, starts):
    with pysam.AlignmentFile(path + ".u", "wb", header={"HD": {"VN": "1.0"}, "SQ": [{"SN": "chr1", "LN": 500}]}) as fh:
        for i, s in enumerate(starts):
            a = pysam.AlignedSegment(); a.query_name = "r%d" % i; a.query_sequence = "A" * 50; a.flag = 0
            a.reference_id = 0; a.reference_start = s; a.mapping_quality = 30; a.cigar = ((0, 50),)
            a.query_qualities = pysam.qualitystring_to_array("I" * 50); fh.write(a)
    pysam.sort("-o", path, path + ".u"); pysam.index(path)

bam("/tmp/a.bam", [10, 220])   # one read in bin 0-100 and one in bin 200-300; bin 100-200 empty
subprocess.run(["bamCompare", "-b1", "/tmp/a.bam", "-b2", "/tmp/a.bam", "-o", "/tmp/out.bg", "-of", "bedgraph",
                "-bs", "100", "--scaleFactors", "1:1", "--skipZeroOverZero"], check=True, capture_output=True)
got = open("/tmp/out.bg").read()
print("got:\n" + got)
expected = "chr1\t0\t100\t0\nchr1\t200\t300\t0\n"
assert got == expected, "expected:\n" + expected
