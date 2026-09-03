# Minimal example: BAM_Reader[iv] misses an alignment whose last aligned base is iv.start.
# Needs only pysam and HTSeq; writes a 2-read BAM in the working directory.
import pysam
import HTSeq

fn = "two_reads.bam"
with pysam.AlignmentFile(fn, "wb", header={"HD": {"VN": "1.6", "SO": "coordinate"},
                                           "SQ": [{"SN": "chr1", "LN": 1000}]}) as f:
    for name, start in (("covers_base_100", 91), ("inside", 95)):  # 10-nt reads: [91,101) and [95,105)
        a = pysam.AlignedSegment()
        a.query_name, a.query_sequence, a.flag = name, "A" * 10, 0
        a.reference_id, a.reference_start, a.mapping_quality, a.cigartuples = 0, start, 60, [(0, 10)]
        a.query_qualities = pysam.qualitystring_to_array("I" * 10)
        f.write(a)
pysam.index(fn)

iv = HTSeq.GenomicInterval("chr1", 100, 200, ".")
got = [a.read.name for a in HTSeq.BAM_Reader(fn)[iv]]
expected = [a.read.name for a in HTSeq.BAM_Reader(fn) if a.iv.overlaps(iv)]
print("HTSeq", HTSeq.__version__, "| reader[iv]:", got, "| records with iv.overlaps:", expected)
assert got == expected, "reader[iv] should return every alignment overlapping iv"
