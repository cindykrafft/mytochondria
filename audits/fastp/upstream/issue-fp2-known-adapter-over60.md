Title: An auto-detected built-in adapter longer than 60 bases is printed and then discarded ("No adapter detected"), so nothing is trimmed

fastp prints the adapter it has just found and then reports "No adapter detected
for read1" and trims nothing. It happens for every built-in adapter longer than
60 nt, which is 139 of the 234 entries in `src/knownadapters.h` -- among them the
48 TruSeq Small RNA RPI primers and the RNA PCR Primer index series, i.e. the
libraries whose adapters have no shorter built-in prefix to fall back on.

**fastp version and platform:** master @ dce5c40, and the v1.3.6, v1.0.0 and
v0.26.0 release tags (built from source, g++ 13.3, Linux x86-64). Releases up to
v0.23.4 do not select a >60 nt adapter at all, so they never reach this line.

**Command line:** `fastp -i reads.fastq -o out.fastq` (single end, adapter
auto-detection, no other options)

**Example input:** 20,000 reads of 100 nt that read through into the TruSeq
Small RNA RPI1 adapter `TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACATCACGATCTCGTATGCC
GTCTTCTGCTTG` (63 nt, `>RNA_PCR_Primer_Index_1_(RPI1)_2,9` in
`src/knownadapters.h`); the script below builds the file.

**Output fastp produces:**

```
Detecting adapter sequence for read1...
TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG
No adapter detected for read1

reads with adapter trimmed: 0
bases trimmed due to adapters: 0
```

and the JSON report has no `adapter_cutting` section at all. On 2,000 such reads
the adapter is left in 2,000 of them, 143,139 adapter bases in total.

**Expected output:** the adapter is used, as it is when the same sequence is
passed with `--adapter_sequence` (20,000 of 20,000 reads trimmed).

**Minimal complete reproduction** (`mcve_fp2_known_adapter_over60.py`; the
detector needs at least 10,000 reads, so the file is generated in the script):

```python
import os, random, re, subprocess, sys, tempfile

FASTP = sys.argv[1] if len(sys.argv) > 1 else "fastp"
RPI1 = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"  # 63 nt
random.seed(0)
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "reads.fastq")
    with open(path, "w") as f:
        for i in range(20000):
            insert = "".join(random.choice("ACGT") for _ in range(random.randint(20, 37)))
            seq = (insert + RPI1)[:100]
            f.write("@r%d\n%s\n+\n%s\n" % (i, seq, "I" * len(seq)))
    for label, args in (("auto-detection", []), ("--adapter_sequence <RPI1>", ["-a", RPI1])):
        err = subprocess.run([FASTP, "-i", path, "-o", os.path.join(tmp, "out.fastq"),
                              "-j", os.path.join(tmp, "j"), "-h", os.path.join(tmp, "h")] + args,
                             capture_output=True, text=True).stderr
        printed = re.findall(r"^[ACGT]{20,}$", err, re.M)
        trimmed = re.search(r"reads with adapter trimmed: (\d+)", err)
        print("%-26s adapter printed by fastp: %-9s | %s | reads with adapter trimmed: %s"
              % (label, ("%d nt" % len(printed[0])) if printed else "none",
                 "'No adapter detected'" if "No adapter detected" in err else "adapter used",
                 trimmed.group(1) if trimmed else "?"))
```

```
auto-detection             adapter printed by fastp: 63 nt     | 'No adapter detected' | reads with adapter trimmed: 0
--adapter_sequence <RPI1>  adapter printed by fastp: none      | adapter used | reads with adapter trimmed: 20000
```

**Cause.** `src/main.cpp:458-459` (and `:474-475` for read2):

```cpp
            string adapt = eva.evalAdapterAndReadNum(readNum, false);
            if(adapt.length() > 60 )
                adapt.resize(0, 60);
```

`std::string::resize(size_type n, char c)` resizes the string to `n` and pads
with `c`, so `resize(0, 60)` empties the adapter rather than truncating it to 60
characters (`resize(60)`). The very next line, `if(adapt.length() > 0)`, is then
false, so fastp prints "No adapter detected" and sets `adapter.sequence = ""`.

The line has been there since 2018, but it was unreachable until v0.26.0: the
nucleotide-tree detector truncates its candidate to 60 characters *before*
`matchKnownAdapter` (`src/evaluator.cpp:560-563`), so it can only ever return an
adapter of at most 60 nt. `Evaluator::checkKnownAdapters` (added in v0.26.0,
"refine single-end adapter detection by searching known adapter first") returns
the full-length built-in entry, and 139 of the 234 built-ins are longer than 60.

A built-in adapter that has a shorter built-in prefix is shielded, because
`checkKnownAdapters` scans the table in `std::map` (lexicographic) order and
keeps a candidate only on a strictly larger hit count, so the shorter prefix
wins the tie: `>TruSeq_Adapter_Index_5` (63 nt) resolves to the 33 nt
`AGATCGGAAGAGCACACGTCTGAACTCCAGTCA` and is trimmed normally. 85 of the 139 have
no such prefix, and those are silently not trimmed.

**What shrinking the example showed.** The read content is irrelevant; the only
thing that matters is which built-in adapter wins the vote. Of seven built-ins
tested this way, the two with no shorter built-in prefix (RPI1, `RNA PCR Primer,
Index 35`) trimmed 0 of 20,000 reads, and the five that resolve to a shorter
entry (33 nt and 58 nt TruSeq, `Reverse_adapter`, `TruSeq_Adapter_Index_5`,
`pcr_dimer`) trimmed 20,000 of 20,000. For paired-end data with
`--detect_adapter_for_pe` the overlap analysis still catches most read-throughs,
but 24,735 instead of 40,000 reads were trimmed on the same data.

**Proposed fix.** `adapt.resize(60);` in both places (keeping the author's 60 nt
cap). Dropping the cap for built-in adapters would work too, since the trimmer
handles any adapter length. A branch with the fix and a
`scripts/test_known_adapter_over60.sh` in the style of
`scripts/test_issue_697_stdout_merge.sh` (it fails without the fix: 0 of 20,000
trimmed) is ready; PR follows.

Found in a source-level correctness audit of research software (methods and harnesses: https://github.com/cindykrafft/research-software-audit/tree/main/audits/fastp)

---
_Generated by [Claude Code](https://claude.ai/code)_
