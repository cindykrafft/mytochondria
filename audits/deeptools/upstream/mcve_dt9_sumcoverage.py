"""plotFingerprint's SumCoveragePerBin over-counts a fragment's last bin when it is given a
multi-bin region (the path taken when the sampling step equals --binSize). One 50-bp read at
50-100 and 40-bp bins over 0-200: per-base coverage sums are [0, 30, 20, 0, 0]; got [0, 30, 40, 0, 0]."""
import numpy as np, pysam
from deeptools.sumCoveragePerBin import SumCoveragePerBin

with pysam.AlignmentFile("/tmp/f.u", "wb", header={"HD": {"VN": "1.0"}, "SQ": [{"SN": "chr1", "LN": 200}]}) as fh:
    a = pysam.AlignedSegment(); a.query_name = "r"; a.query_sequence = "A" * 50; a.flag = 0
    a.reference_id = 0; a.reference_start = 50; a.mapping_quality = 30; a.cigar = ((0, 50),)
    a.query_qualities = pysam.qualitystring_to_array("I" * 50); fh.write(a)
pysam.sort("-o", "/tmp/f.bam", "/tmp/f.u"); pysam.index("/tmp/f.bam")
c = SumCoveragePerBin([], stepSize=40, binLength=40)
got = c.get_coverage_of_region(pysam.AlignmentFile("/tmp/f.bam"), "chr1", [(0, 200, 40)])
print("bin sums:", got.tolist(), " expected: [0, 30, 20, 0, 0]")
np.testing.assert_equal(got, [0, 30, 20, 0, 0])
