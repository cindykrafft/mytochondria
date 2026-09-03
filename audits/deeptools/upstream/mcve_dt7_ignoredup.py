"""--ignoreDuplicates alone leaves the duplicates in the normalisation denominator.
3,000 reads of which 1,000 are exact duplicates; CPM scale factor with --ignoreDuplicates is
1e6/3000 (all reads); adding a no-op filter (--samFlagExclude 4) gives 1e6/2000."""
import re, subprocess, numpy as np, pysam

L = 100000
starts = np.random.RandomState(0).randint(0, L - 50, 2000)
with pysam.AlignmentFile("/tmp/d.u", "wb", header={"HD": {"VN": "1.0"}, "SQ": [{"SN": "chr1", "LN": L}]}) as fh:
    for i, s in enumerate(list(starts) + list(starts[:1000])):
        a = pysam.AlignedSegment(); a.query_name = "r%d" % i; a.query_sequence = "A" * 50; a.flag = 0
        a.reference_id = 0; a.reference_start = int(s); a.mapping_quality = 30; a.cigar = ((0, 50),)
        a.query_qualities = pysam.qualitystring_to_array("I" * 50); fh.write(a)
pysam.sort("-o", "/tmp/d.bam", "/tmp/d.u"); pysam.index("/tmp/d.bam")

def factor(extra):
    r = subprocess.run(["bamCoverage", "-b", "/tmp/d.bam", "-o", "/tmp/d.bw", "-bs", "50", "--normalizeUsing", "CPM", "--verbose"] + extra,
                       capture_output=True, text=True)
    return float(re.search(r"Final scaling factor: ([0-9.e+-]+)", r.stdout + r.stderr).group(1))

f1, f2 = factor(["--ignoreDuplicates"]), factor(["--ignoreDuplicates", "--samFlagExclude", "4"])
print("CPM factor with --ignoreDuplicates                    : %.3f  (1e6/3000 = %.3f)" % (f1, 1e6 / 3000))
print("CPM factor with --ignoreDuplicates --samFlagExclude 4 : %.3f  (1e6/2000 = %.3f)" % (f2, 1e6 / 2000))
assert abs(f1 - f2) < 1e-6, "the denominator changes with a no-op filter"
