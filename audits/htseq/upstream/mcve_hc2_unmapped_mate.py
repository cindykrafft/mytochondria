# Minimal example: a pair whose mate is unmapped (record present, MAPQ 0) is counted as
# __too_low_aQual under the default -a 10; the same pair counts when the unmapped record is
# not in the file. Needs pysam and HTSeq; writes one BAM and one GTF in the working directory.
import subprocess
import pysam

open("one_gene.gtf", "w").write('chr1\tsrc\texon\t1001\t2000\t.\t+\t.\tgene_id "A";\n')


def segment(name, flag, start, mapq, cigar, mate_start):
    a = pysam.AlignedSegment()
    a.query_name, a.flag, a.query_sequence = name, flag, "A" * 50
    a.query_qualities = pysam.qualitystring_to_array("I" * 50)
    a.reference_id, a.reference_start, a.mapping_quality, a.cigartuples = 0, start, mapq, cigar
    a.next_reference_id, a.next_reference_start = 0, mate_start
    return a


with pysam.AlignmentFile("pairs.bam", "wb", header={"HD": {"VN": "1.6"},
                                                    "SQ": [{"SN": "chr1", "LN": 5000}]}) as f:
    # pair 1: mate 1 in gene A with MAPQ 60, mate 2 unmapped and placed at mate 1 (flag 0x4, MAPQ 0)
    f.write(segment("mate2_unmapped", 0x1 | 0x8 | 0x40, 1100, 60, [(0, 50)], 1100))
    f.write(segment("mate2_unmapped", 0x1 | 0x4 | 0x80, 1100, 0, None, 1100))
    # pair 2: mate 1 in gene A with MAPQ 60, mate 2 not in the file at all
    f.write(segment("mate2_absent", 0x1 | 0x20 | 0x40, 1200, 60, [(0, 50)], 1500))

out = subprocess.run(["htseq-count", "-q", "-s", "yes", "pairs.bam", "one_gene.gtf"],
                     capture_output=True, text=True, check=True).stdout
counts = dict(line.split("\t") for line in out.splitlines())
print(subprocess.run(["htseq-count", "--version"], capture_output=True, text=True).stdout.strip(), counts)
assert counts["A"] == "2" and counts["__too_low_aQual"] == "0", "both pairs should count for A"
