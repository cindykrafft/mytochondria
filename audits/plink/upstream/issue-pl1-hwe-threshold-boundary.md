Title: PLINK 1.9: --hwe removes variants with 2 or 3 heterozygotes whose exact p-value is above the threshold (SNPHWE_t skips the last tail comparison)

**Version.** PLINK 1.9 built from `master` @ `8bfebe8` (`v1.9.0-b.8 64-bit (1 Sep 2026)`); also reproduced on the tags `v1.9.0-b.7.12` (2026-09-01) and `v1.90b4` (2017) and on `v1.90b6.21`. PLINK 2.0 (`v2.0.0-b.1`, same tree) is not affected. Linux x86-64, gcc 13, `NO_LAPACK` and LAPACK builds behave the same.

**What happens.** `--hwe <p>` excludes a variant although `--hardy` reports a p-value above `<p>`, whenever the variant has exactly 2 (and, in most shapes, 3) heterozygotes and its p-value lies within a narrow band above the threshold. The band is (p − P(hets − 2), p): for a 2-het / 2-hom / 2-hom variant it is (0.4589, 0.4805), for a 2-het / 5-hom / 1000-hom variant (p = 1.905e-12) it is about 8e-5 of p wide — narrow on large samples, several per cent on small ones. `--hwe … midp` has the same defect (band up to 14 % of p in the exhaustive check).

**Reproduction** (6 samples, 2 variants; `snp1` has counts 2 het / 2 hom / 2 hom, exact HWE p = 185/385 = 0.480519):

```python
import os, subprocess, sys, tempfile
plink = sys.argv[1]
d = tempfile.mkdtemp()
open(f"{d}/x.map", "w").write("1\tsnp1\t0\t1000\n1\tsnp2\t0\t2000\n")
# snp1: 2 het, 2 hom, 2 hom; snp2: a filler variant in HWE so that the --hwe run keeps at least one variant
open(f"{d}/x.ped", "w").write("".join(f"F{i} I{i} 0 0 2 -9 {g} {f}\n" for i, (g, f) in enumerate(zip(["A A", "A A", "A T", "A T", "T T", "T T"], ["A A", "A T", "T T", "A A", "A T", "A A"]), 1)))
subprocess.run([plink, "--file", f"{d}/x", "--hardy", "--out", f"{d}/h"], capture_output=True)
print(open(f"{d}/h.hwe").read().splitlines()[1])                       # snp1 row: P = 0.4805
subprocess.run([plink, "--file", f"{d}/x", "--hwe", "0.48", "--write-snplist", "--out", f"{d}/w"], capture_output=True)
kept = open(f"{d}/w.snplist").read().split()
print("kept after --hwe 0.48:", kept)
print("expected: ['snp1', 'snp2']  (exact p = 185/385 = 0.480519 > 0.48)")
assert "snp1" in kept, "snp1 removed although its HWE p-value is above the threshold"
```

**Got** (`master`, `v1.9.0-b.7.12`, `v1.90b6.21` all identical):

```
   1 snp1  ALL(NP)    T    A                2/2/2   0.3333      0.5       0.4805
kept after --hwe 0.48: ['snp2']
expected: ['snp1', 'snp2']  (exact p = 185/385 = 0.480519 > 0.48)
Traceback (most recent call last):
  File "mcve_pl1_hwe_threshold.py", line 17, in <module>
    assert "snp1" in kept, "snp1 removed although its HWE p-value is above the threshold"
           ^^^^^^^^^^^^^^
AssertionError: snp1 removed although its HWE p-value is above the threshold
```

**Expected:** `snp1` kept — `--hwe` is documented as excluding variants with "exact test p-values below a threshold", and 0.4805 > 0.48. `--hwe 0.46` and `0.45` keep it, `0.4806` removes it (correctly), so the wrong verdicts are exactly the thresholds in (0.4589, 0.4805). plink2 `--hwe 0.48` on the same files keeps it.

Shrinking the example showed that only the heterozygote count matters: with 0, 1, 4 or 6 heterozygotes the boundary is exact, with 2 it is always wrong, with 3 it is wrong in 9,600 of 9,697 tables. Driving the shipped `SNPHWE_t` directly (linked from the build objects) over every genotype table with n ≤ 200 and ≤ 6 heterozygotes and bisecting the threshold at which the verdict flips: 19,399 of 67,883 tables flip below their exact p (offsets up to −5.3 % of p; `SNPHWE_midp_t`: up to −13.6 %). plink2's `HweThreshLn` on the same tables: 0.

**Cause** (`1.9/plink_stats.c`, `SNPHWE_t` and `SNPHWE_midp_t`, both tail branches). After the centre is summed, the tail containing the observed count is extended by one element (`tailp1 += lastp1`, lines 458 / 531), but the loop that then compares the running tail sum with `exit_thresh` is only entered `if (obs_homr > 1)` (line 460) / `if (obs_hets >= 4)` (line 534). When it is skipped, the only remaining comparison is inside the loop over the other tail (lines 482–495 / 555–568), which compares after adding an element and does not iterate when that tail has at most one element — always the case with two heterozygotes, since P(4) is already in the centre. The function falls through to `return 1` (lines 496 / 569) and the variant fails, so the filter effectively tests `p − P(hets − 2) < threshold`. A trace of `SNPHWE_t(2, 2, 2, 0.48)` in relative masses: centre 1.333, tail 2 = 0.178, tail 1 = 1 + 0.056, threshold 1.231; 1.234 ≥ 1.231 should pass, but the last comparison made was 1.178 < 1.231. `SNPHWE2()` (used by `--hardy`) sums everything and is right, which is why `--hardy` and `--hwe` disagree.

**Fix:** compare the completed tail before walking the other one, at the four sites (lines 481, 554, 674, 751):

```c
    if (tailp1 + tailp2 >= exit_thresh) {
      return 0;
    }
    exit_threshx = exit_thresh - tailp1;
```

With that change the exhaustive count goes from 19,399 to 0 wrong tables in both functions, the reproduction passes, and `--hwe` at 0.05 / 1e-3 / 1e-6 on 400 random variants still matches the exact p (0 differences before and after). A PR with the patch follows.

Found in a source-level correctness audit of research software (methods and harnesses: https://github.com/cindykrafft/research-software-audit/tree/main/audits/plink)

---
_Generated by [Claude Code](https://claude.ai/code)_
