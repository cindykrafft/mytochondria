Title: [BUG] htseq-count discards a read pair as `__too_low_aQual` because of the MAPQ of its unmapped mate

<!-- htseq/htseq .github/ISSUE_TEMPLATE/bug_report.md fields -->

**Software versions**
- `HTSeq` 2.1.2 (PyPI wheel) and `main` @ `7672321` (editable install); reproduced on 0.11.2, 0.12.4 and 0.13.5 built from the sdists as well
- `Python` 3.12.3, pysam 0.24.0
- Linux (x86_64)
- aligner: any that keeps the unmapped mate of a pair in the BAM with the SAM-recommended placement (HISAT2, BWA, Bowtie2 without `--no-mixed`, STAR with `--outSAMunmapped Within`); the example below writes such records with pysam

**Describe the bug**

In paired-end mode `htseq-count` compares the MAPQ of *both* records of a pair with `--minaqual` without checking that the record is aligned (`HTSeq/scripts/count_features/count_features_per_file.py`, `_assess_pe_read`):

```python
    if (read_sequence[0] and read_sequence[0].aQual < minaqual) or (
        read_sequence[1] and read_sequence[1].aQual < minaqual
    ):
        read_stats.add_low_quality_read(read_sequence=read_sequence)
        return True
```

Aligners write MAPQ 0 on the record of an unmapped mate, so under the default `-a 10` every pair whose mate is unmapped *but present in the file* is counted as `__too_low_aQual` and not for its gene. The same pair is counted for the gene when the unmapped record is simply absent from the file (the pairer yields `(mate1, None)`), and when `-a 0` is given. The FAQ in `doc/htseqcount.rst` says: "What happened if the mate of an aligned read is not aligned? For the default mode union, only the aligned read determines how the read pair is counted." The same comparison is in `htseq-count-barcodes` (`count_with_barcodes.py`).

**Expected:** in the example below both pairs count for gene A (`A 2`, `__too_low_aQual 0`), because in both the only aligned mate has MAPQ 60.
**Got** (2.1.2 and `main`): `A 1`, `__too_low_aQual 1` — the pair whose unmapped mate is in the file is dropped.

On a 2,000-pair synthetic library with 6 % one-mate-unmapped pairs, all 113 such pairs go to `__too_low_aQual` with `-a 10` and all count for their gene with `-a 0` or with the unmapped records stripped, name- and position-sorted alike. Shrinking the example showed that only the presence of the unmapped record and `-a > 0` matter: the overlap mode, strandedness, `-r`, and the mapped mate's MAPQ (as long as it passes `-a`) do not.

**Minimal example showing the bug**

The script writes the BAM (3 records) and the GTF (1 line) itself; nothing needs to be attached.

```python
# mcve_hc2_unmapped_mate.py
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
```

**To Reproduce**

```
$ python mcve_hc2_unmapped_mate.py
2.1.2 {'A': '1', '__no_feature': '0', '__ambiguous': '0', '__too_low_aQual': '1', '__not_aligned': '0', '__alignment_not_unique': '0'}
Traceback (most recent call last):
  File "mcve_hc2_unmapped_mate.py", line 31, in <module>
    assert counts["A"] == "2" and counts["__too_low_aQual"] == "0", "both pairs should count for A"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: both pairs should count for A
```

Equivalent command line on the files the script writes: `htseq-count -q -s yes pairs.bam one_gene.gtf` (default `-a 10`); with `-a 0` both pairs count.

**Proposed fix:** test `aQual` only for aligned mates (`read_sequence[i] is not None and read_sequence[i].aligned and read_sequence[i].aQual < minaqual`) in `_assess_pe_read` and in `count_with_barcodes.py`. A branch with that change, a regression test (`test/test_htseq-count.py::HTSeqCount::test_pair_with_unmapped_mate_is_counted`, which fails on `main` and passes with the fix) and a `doc/history.rst` entry is ready; PR follows.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/htseq)

---
_Generated by [Claude Code](https://claude.ai/code)_
