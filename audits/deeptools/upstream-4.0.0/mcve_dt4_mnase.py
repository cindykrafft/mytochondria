"""bamCoverage --MNase counts four bases for an odd-length fragment (documented: three).
One proper pair with TLEN 149 starting at 100: fragment 100-249, centre base 174,
expected coverage at 173, 174, 175. Got 173-176 (four bases)."""
import subprocess, pysam

hdr = {"HD": {"VN": "1.0"}, "SQ": [{"SN": "chr1", "LN": 1000}]}
with pysam.AlignmentFile("/tmp/mn.u", "wb", header=hdr) as fh:
    for flag, start, tlen in [(99, 100, 149), (147, 199, -149)]:
        a = pysam.AlignedSegment(); a.query_name = "p"; a.query_sequence = "A" * 50; a.flag = flag
        a.reference_id = 0; a.reference_start = start; a.mapping_quality = 30; a.cigar = ((0, 50),)
        a.query_qualities = pysam.qualitystring_to_array("I" * 50)
        a.next_reference_id = 0; a.next_reference_start = 199 if flag == 99 else 100; a.template_length = tlen
        fh.write(a)
pysam.sort("-o", "/tmp/mn.bam", "/tmp/mn.u"); pysam.index("/tmp/mn.bam")
subprocess.run(["bamCoverage", "-b", "/tmp/mn.bam", "-o", "/tmp/mn.bg", "-of", "bedgraph", "--MNase", "-bs", "1"], check=True, capture_output=True)
covered = [line.split("\t")[1:3] for line in open("/tmp/mn.bg") if not line.rstrip().endswith("\t0")]
print("covered interval(s):", covered)
assert covered == [["173", "176"]], "expected [['173', '176']] (three bases 173, 174, 175)"
