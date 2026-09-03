"""bamCompare --skipZeroOverZero shifts the coordinates of every bin after a skipped bin.
One 500-bp chromosome, 100-bp bins; reads (50 bp) only in bins 0 and 2, so bin 1 is zero
in both files and is skipped. Expected --operation first output: bin 0 and bin 2 at their
own coordinates. Got: bin 2's value written at bin 1's coordinates."""
import subprocess, pysam

def bam(path, starts):
    with pysam.AlignmentFile(path + ".u", "wb", header={"HD": {"VN": "1.0"}, "SQ": [{"SN": "chr1", "LN": 500}]}) as fh:
        for i, s in enumerate(starts):
            a = pysam.AlignedSegment(); a.query_name = "r%d" % i; a.query_sequence = "A" * 50; a.flag = 0
            a.reference_id = 0; a.reference_start = s; a.mapping_quality = 30; a.cigar = ((0, 50),)
            a.query_qualities = pysam.qualitystring_to_array("I" * 50); fh.write(a)
    pysam.sort("-o", path, path + ".u"); pysam.index(path)

bam("/tmp/a.bam", [10, 20, 220]); bam("/tmp/b.bam", [10, 220])
subprocess.run(["bamCompare", "-b1", "/tmp/a.bam", "-b2", "/tmp/b.bam", "-o", "/tmp/out.bg", "-of", "bedgraph",
                "-bs", "100", "--scaleFactors", "1:1", "--operation", "first", "--skipZeroOverZero"], check=True, capture_output=True)
got = open("/tmp/out.bg").read()
print("got:\n" + got)
expected = "chr1\t0\t100\t2\nchr1\t200\t300\t1\n"
assert got == expected, "expected:\n" + expected
