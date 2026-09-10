Title: ILLUMINACLIP palindrome mode charges an integer Q/10 mismatch penalty, so mismatches below Q10 are free and pairs below palindromeClipThreshold get clipped

`IlluminaPrefixPair.calculatePalindromeDifferenceQuality` computes the
per-mismatch penalty with integer division, so a mismatch at Q0–Q9 costs
nothing at all and one at Q10–Q19 costs exactly 1.0 instead of 1.0–1.9. The
palindrome score therefore comes out too high, and read pairs whose
read-through alignment is *below* `palindromeClipThreshold` are clipped — with
the default `keepBothReads=false`, that means the reverse read is dropped.

Simple mode does the same arithmetic correctly, in the same file.

## Version

0.41 (both the release jar from the GitHub releases page and `main` @ `ef98d62`
built from source). Also reproduced on the 0.40, 0.39, 0.38, 0.36, 0.33 and
0.32 releases — the expression looks unchanged since the beginning.
Ubuntu 24.04, OpenJDK 25.0.4 for the release jars.

## Reproduction

The script writes everything it needs: a two-record adapter FASTA holding the
stock TruSeq3 `PrefixPE` pair, and one read pair. Geometry: a 40 nt insert read
through into the adapters on both sides, 50 nt reads, so the palindrome
alignment is 60 bases; 54 of the 60 match, and six mismatches are planted in
read 2 outside both 16-mer seeds. The only thing that varies between the two
runs is the quality of those six mismatched bases.

```python
import os, subprocess, sys, tempfile

JAR = sys.argv[1]
PREFIX1 = "TACACTCTTTCCCTACACGACGCTCTTCCGATCT"   # TruSeq3 PrefixPE/1
PREFIX2 = "GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT"   # TruSeq3 PrefixPE/2
READ1 = "CCGTAATGCCTTTCCCTAACAGAGTTTTTCGAACTCGTGTAGATCGGAAG"
READ2 = "CCCCGAGTTCGAAAAACTCTGTTAGGGAAAGGCATTAGGTAGCTCTGAAG"
MISMATCHES = [0, 2, 37, 39, 42, 45]

def run(tmp, mismatch_q):
    fa = os.path.join(tmp, "adapters.fa")
    open(fa, "w").write(">PrefixPE/1\n%s\n>PrefixPE/2\n%s\n" % (PREFIX1, PREFIX2))
    q1 = chr(33 + 35) * len(READ1)
    q2 = [chr(33 + 35)] * len(READ2)
    for p in MISMATCHES:
        q2[p] = chr(33 + mismatch_q)
    for name, seq, qual in (("in1.fq", READ1, q1), ("in2.fq", READ2, "".join(q2))):
        open(os.path.join(tmp, name), "w").write("@pair\n%s\n+\n%s\n" % (seq, qual))
    outs = [os.path.join(tmp, n) for n in ("1P.fq", "1U.fq", "2P.fq", "2U.fq")]
    subprocess.run(["java", "-jar", JAR, "PE", "-phred33",
                    os.path.join(tmp, "in1.fq"), os.path.join(tmp, "in2.fq")] + outs +
                   ["ILLUMINACLIP:%s:2:30:10" % fa], check=True, capture_output=True)
    def length(path):
        lines = open(path).read().split("\n")
        return len(lines[1]) if len(lines) > 1 and lines[1] else None
    return length(outs[0]) or length(outs[1]), length(outs[2]) or length(outs[3])

for mismatch_q in (10, 9):
    with tempfile.TemporaryDirectory() as tmp:
        print("Q%-2d -> read 1 %s, read 2 %s" % ((mismatch_q,) +
              tuple("%d nt" % n if n else "dropped" for n in run(tmp, mismatch_q))))
```

## Expected

`README.md` states one scoring rule for both modes:

> Each matching base adds just over 0.6, while each mismatch reduces the
> alignment score by Q/10.

54 matches × 0.60206 = 32.51, and six mismatches cost 6 × Q/10:

| mismatch quality | penalty | score | vs. `palindromeClipThreshold` 30 |
|---|---|---|---|
| Q10 | 6 × 1.0 = 6.0 | **26.51** | below → nothing to clip |
| Q9 | 6 × 0.9 = 5.4 | **27.11** | below → nothing to clip |

Both runs should leave the pair alone: `read 1 50 nt, read 2 50 nt`.

## Got

```
Q10 -> read 1 50 nt, read 2 50 nt
Q9  -> read 1 40 nt, read 2 dropped
```

Lowering the quality of the mismatched bases from Q10 to Q9 — making the
alignment *worse* — is what makes Trimmomatic accept it. As coded, the six Q9
mismatches cost 6 × 0 and the score is 32.51, over the threshold.

## Cause

`src/main/java/org/usadellab/trimmomatic/trim/IlluminaClippingTrimmer.java:486–498`

```java
int qual1 = offset1 < prefixLength ? 100 : quals1[offset1 - prefixLength];
int qual2 = offset2 < prefixLength ? 100 : quals2[offset2 - prefixLength];

if (ch1 == 'N' || ch2 == 'N')
        likelihood[i] = 0;
else if (ch1 != ch2) {
        if (qual1 < qual2)
                likelihood[i] = -qual1 / 10;      // int / int
        else
                likelihood[i] = -qual2 / 10;      // int / int
} else
        likelihood[i] = LOG10_4;
```

`qual1` and `qual2` are `int`, so `-qual1 / 10` is evaluated as integer division
and truncated toward zero before it is widened into the `float likelihood[]`.
Q0–Q9 → 0.0, Q10–Q19 → 1.0, Q20–Q29 → 2.0, and so on.

Simple mode, 60 lines further down at `:556`, already does it right:

```java
likelihood[i] = -quals[recPos] / 10.0f;
```

The fix is `10` → `10.0f` on both lines.

## How much this matters

The error is one-sided — the penalty is never too large — so the palindrome
score is always too high and the effect is always *extra* clipping and *extra*
dropped reverse reads, never fewer.

Priced by executing 0.41 and an independent port of the same algorithm on 4,000
synthetic 100 nt pairs (inserts 0–130 nt, read-through planted in 3,041,
quality-correlated errors): the shipped jar agrees with the as-coded port on
4,000/4,000 pairs, and changing *only* the penalty to `Q/10` changes the
outcome of 49 pairs (1.2 %). The exposure tracks how many overlap mismatches
land on bases below Q10: on a NovaSeq-like binned profile (Q2/Q12/Q23/Q37) and
on a uniformly Q30–41 profile, 0 of 4,000 pairs change. So this bites data with
low-quality bases inside the read-through overlap, and is invisible on clean
data.

On 3,000 pairs of independent random reads with no adapter and no insert,
nothing is clipped either way — the bug moves a threshold, it does not
manufacture adapter hits.

## What shrinking the example revealed

Starting from randomly generated pairs, most differences disappeared when the
mismatches were moved: the first version put mismatches wherever the random
error model placed them, and half the cases were explained by the 16-mer seed
scan, not by the penalty. Forcing all six mismatches outside both seeds isolated
the penalty, and made the pair reproducible at exactly one threshold crossing.
The pair of runs at Q9 and Q10 is what remains: same sequences, same positions,
one Phred unit apart, opposite outcomes. The Q10 run is the control that proves
the geometry, the seeds and the threshold are all as intended.

A patch (one character on each of the two lines, plus a JUnit regression test in
the style of the existing `IlluminaPalindrome*Test` classes) is ready if it
would be useful. On unmodified `main` the project's suite is 259 tests / 0
failures and the new test class is 4 tests / 1 failure; with the fix the suite
is 263 tests / 0 failures.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/trimmomatic)

---
_Generated by [Claude Code](https://claude.ai/code)_
