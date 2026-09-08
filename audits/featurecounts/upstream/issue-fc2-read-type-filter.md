Title: Single-end reads in a paired-end file are counted as first reads under -s 1/-s 2; the documented Unassigned_Read_Type filter is gone since 2.0.2

**Version:** featureCounts v2.1.1 (SourceForge source tarball), v2.0.3 and GitHub `master` (`55dc154`, v2.0.6) behave as described below; **v2.0.1 does not** (it implements the filter). Linux x86_64, built with `make -f Makefile.Linux`.

**Command:** `featureCounts -p --countReadPairs -s 2 -a a.gtf -o out a.sam`

**Expected (users guide, "Read filtering"):** "if there are single end reads included in a paired end read dataset (such data can be produced from a read trimming program for instance) and reads are required to be counted in a strand-specific manner, then all the single end reads will be excluded from counting because their strandness cannot be determined." The output section lists the row `Unassigned_Read_Type` for them. In the example below (gene S on +, gene AS antisense on −, one dUTP pair from S, one orphaned second read and one orphaned first read from S written as single-end records): S = 1, AS = 0, `Unassigned_Read_Type` = 2.

**Got:** S = 2, AS = 1, `Unassigned_Read_Type` = 0. The two single-end records are counted, each with its own strand taken as the fragment strand, i.e. as first reads: the orphaned first read (reverse) goes to S, the orphaned second read (forward) goes to the antisense gene. On a larger file with 300 pairs, 500 orphaned first reads and 500 orphaned second reads, all from S: S = 800 and AS = 500 under `-s 2` (S = 500, AS = 800 under `-s 1`); v2.0.1 gives S = 300, AS = 0 and `Unassigned_Read_Type` = 1,000 with the same file.

**Why:** the counter `unassigned_read_type` is declared, merged and printed as the `Unassigned_Read_Type` row, but nothing increments it. Release 2.0.1 had, where the inconsistent read type is detected (`readSummary.c:2911-2921` in the 2.0.1 tarball):

```c
if(this_is_inconsistent_read_type){
    if(global_context -> is_strand_checked){
        ... "Unassigned_Read_Type" ... unassigned_read_type++;
        return; // strand_specific assignment only accept the correct mode of reads.
    }
```

The 2.0.2 changes (commit `1f24de1`, "latest changes to Subread, matching the subread-2.0.2 release") removed that branch and kept only the `-B` singleton rule; the manual kept the sentence (it is in the 2.0.3 and 2.1.1 manuals). Shrinking the example showed that a single single-end record in a run with `-p` and `-s 1` or `-s 2` is enough; `-s 0` and `-B` (which makes them `Unassigned_Singleton`) are unaffected.

**Question first:** was the removal intended? If single-end records in a paired-end library are meant to be counted as first reads, the manual's "Read filtering" and "Program output" sections and the summary row should say so (an orphaned second read from a dUTP library then lands on the antisense gene). If the manual is right, a patch that restores the 2.0.1 branch — with the counter routed through the read-group tables and the scRNA pool like the neighbouring filters, applying whenever `-p` is combined with `-s 1`/`-s 2` — and adds `test/featureCounts/data/corner-READTYPE.{sam,ora}` (expected `simu_gene1 = 4`; current code gives 6) is ready; the full `featureCounts-test.sh` suite passes with it.

**Minimal reproduction** (Python 3, no dependencies; pass the path to the binary):

```python
#!/usr/bin/env python3
import subprocess, sys, tempfile
fc = sys.argv[1] if len(sys.argv) > 1 else "featureCounts"
d = tempfile.mkdtemp()
open(f"{d}/a.gtf", "w").write('chr1\tx\texon\t1000\t2000\t.\t+\t.\tgene_id "S";\n'
                              'chr1\tx\texon\t1000\t2000\t.\t-\t.\tgene_id "AS";\n')
S = "A" * 50; Q = "I" * 50
open(f"{d}/a.sam", "w").write(
    "@HD\tVN:1.6\tSO:unsorted\n@SQ\tSN:chr1\tLN:10000\n"
    f"pair1\t83\tchr1\t1200\t60\t50M\t=\t1100\t-150\t{S}\t{Q}\n"    # dUTP pair from S: R1 reverse, R2 forward
    f"pair1\t163\tchr1\t1100\t60\t50M\t=\t1200\t150\t{S}\t{Q}\n"
    f"orphanR2\t0\tchr1\t1300\t60\t50M\t*\t0\t0\t{S}\t{Q}\n"        # orphaned second read of a fragment from S
    f"orphanR1\t16\tchr1\t1400\t60\t50M\t*\t0\t0\t{S}\t{Q}\n")      # orphaned first read of a fragment from S
subprocess.run([fc, "-p", "--countReadPairs", "-s", "2", "-a", f"{d}/a.gtf", "-o", f"{d}/out", f"{d}/a.sam"],
               check=True, capture_output=True)
counts = {l.split("\t")[0]: l.split("\t")[-1].strip() for l in open(f"{d}/out") if not l.startswith(("#", "Geneid"))}
summ = {l.split("\t")[0]: l.split("\t")[1].strip() for l in open(f"{d}/out.summary")}
print(f"S={counts['S']} AS={counts['AS']} Unassigned_Read_Type={summ['Unassigned_Read_Type']} (manual: S=1, AS=0, Unassigned_Read_Type=2)")
```

Output on v2.1.1, v2.0.3 and `master`:

```
S=2 AS=1 Unassigned_Read_Type=0 (manual: S=1, AS=0, Unassigned_Read_Type=2)
```

On v2.0.1 (`-p -s 2`, before `--countReadPairs` existed) and with the patch:

```
S=1 AS=0 Unassigned_Read_Type=2 (manual: S=1, AS=0, Unassigned_Read_Type=2)
```

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/featurecounts)

---
_Generated by [Claude Code](https://claude.ai/code)_
