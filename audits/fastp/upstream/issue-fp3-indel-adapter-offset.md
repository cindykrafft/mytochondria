Title: The one-indel adapter search only ever looks at the start of the read (comment on #518)

_This is a **comment for the existing issue [#518](https://github.com/OpenGene/fastp/issues/518)**
("fastp can not remove adapter when the read sequence has indels in the
adapter"), not a new issue. #518 is still open; the code added in v0.26.0
("support one base insertion/deletion in SE mode adapter trimming", eb461d5) was
meant to handle exactly that case, and it does not fire, because the read offset
is not passed to the comparison._

---

**fastp version and platform:** master @ dce5c40 and the v1.3.6, v1.0.0 and
v0.26.0 release tags, built from source with g++ 13.3 on Linux x86-64. Releases
before v0.26.0 have no gapped search at all.

**Command line:** `fastp -i reads.fastq -o out.fastq -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA
--disable_quality_filtering --disable_length_filtering --disable_trim_poly_g`

**Example input reads** (74 nt: 40 nt of insert, then the TruSeq Read 1 adapter,
once exactly and once with one inserted base):

```
@exact
TTTTAACCCCCCCCCCCCCCCCCCCCCCCCCCCCAATTTTAGATCGGAAGAGCACACGTCTGAACTCCAGTCA
@one_inserted_base
TTTTAACCCCCCCCCCCCCCCCCCCCCCCCCCCCAATTTTAGATCGGAGAGAGCACACGTCTGAACTCCAGTCA
```

**Output fastp produces:** `exact` is trimmed to 40 nt; `one_inserted_base` and
the corresponding one-deletion read come out untrimmed at 74 and 72 nt.

**Expected output:** 40 nt for all three.

**Minimal complete reproduction** (`mcve_fp3_indel_adapter.py`):

```python
import os, subprocess, sys, tempfile

FASTP = sys.argv[1] if len(sys.argv) > 1 else "fastp"
AD = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"
INSERT = "TTTTAACCCCCCCCCCCCCCCCCCCCCCCCCCCCAATTTT"      # 40 nt
reads = [("exact", INSERT + AD, 40),
         ("one_inserted_base", INSERT + AD[:8] + "G" + AD[8:], 40),
         ("one_deleted_base", INSERT + AD[:8] + AD[9:], 40),
         ("insertion_at_position_0", AD[:8] + "G" + AD[8:] + INSERT, 0)]
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "reads.fastq")
    with open(path, "w") as f:
        for name, seq, _ in reads:
            f.write("@%s\n%s\n+\n%s\n" % (name, seq, "I" * len(seq)))
    out = os.path.join(tmp, "out.fastq")
    subprocess.run([FASTP, "-i", path, "-o", out, "-a", AD,
                    "--disable_quality_filtering", "--disable_length_filtering",
                    "--disable_trim_poly_g", "-j", os.path.join(tmp, "j"),
                    "-h", os.path.join(tmp, "h")], capture_output=True)
    lines = open(out).read().splitlines()
    got = {lines[i][1:]: lines[i + 1] for i in range(0, len(lines), 4)}
    for name, seq, expected in reads:
        print("%-24s output %3d nt (expected %d)" % (name, len(got.get(name, "")), expected))
```

```
exact                    output  40 nt (expected 40)
one_inserted_base        output  74 nt (expected 40)   <-- adapter left in the read
one_deleted_base         output  72 nt (expected 40)   <-- adapter left in the read
insertion_at_position_0  output   0 nt (expected 0)
```

**Cause.** In `AdapterTrimmer::trimBySequence` the exact-match loop compares the
adapter with the read *at the current offset*
(`src/adaptertrimmer.cpp:91-93`):

```cpp
        int mismatch = fastp_simd::countMismatchesBounded(
            adata + startOffset, rdata + startOffset + pos,
            cmplen - startOffset, allowedMismatch);
```

but the two gapped loops pass `rdata`, i.e. always the beginning of the read
(`:110` and `:127`):

```cpp
            bool matched = Matcher::matchWithOneInsertion(rdata, adata, cmplen, allowedMismatch);
            ...
            bool matched = Matcher::matchWithOneInsertion(adata, rdata, cmplen, allowedMismatch);
```

For every `pos` from 0 up to `rlen-alen-1` the call is byte-for-byte identical
(same pointers, same `cmplen`, same allowance), so the loop is a single test of
"does the read *begin* with the adapter, allowing one indel"; `pos` only decides
where the read would be cut. That is why the fourth read above, which starts
with the adapter, is handled and the others are not.

**What shrinking the example showed.** One read per case is enough and the flanks
do not matter; what matters is only the distance between the read start and the
adapter -- the same read with the adapter at position 0 is trimmed, at position 1
or beyond it is not. On 5,000 random reads (a quarter of them carrying the
adapter with one random indel) fastp trimmed 263 of 993 insertion reads and 266
of 967 deletion reads; those come from the exact-match loop picking up a short
partial match at the 3' end, not from the gapped search.

**Proposed fix.** Pass `rdata + pos` in both loops. With that one change the same
5,000 reads give 993 of 993 and 967 of 967, and none of the 1,013 reads without
an adapter is trimmed. A branch with the fix and two new cases in
`AdapterTrimmer::test()` (both fail without it) is ready; PR follows.

Found in a source-level correctness audit of research software (methods and harnesses: https://github.com/cindykrafft/research-software-audit/tree/claude/software-package-audit-ablwee/audits/fastp)

---
_Generated by [Claude Code](https://claude.ai/code)_
