#!/usr/bin/env python3
"""Reproduction for macs3-project/MACS issue #715:

    "macs3 bdgdiff produces scores less than -C cutoff in cond1/2 bed
     file, and scores of all zeroes in common bed file"

Part 1 builds four tiny bedGraph tracks whose log10 likelihood ratios
are fractional, runs `macs3 bdgdiff -C 0.2` on them, and prints the
score column of the three output BED files next to the values the
documentation promises (the mean log10LR of the region).

Part 2 repeats the project's own `test/cmdlinetest` bdgdiff step on the
CTCF chr22 test data shipped in `test/` and compares the score column
with `test/standard_results_bdgdiff/` (which was generated with a
float-correct MACS).

Usage: python repro.py <path-to-MACS-source-checkout>
"""
import math
import os
import subprocess
import sys
import tempfile

LOG10_E = math.log10(math.e)


def logLR_asym(x, y):
    if x > y:
        return (x * (math.log(x) - math.log(y)) + y - x) * LOG10_E
    if x < y:
        return (x * (-math.log(x) + math.log(y)) - y + x) * LOG10_E
    return 0.0


def logLR_sym(x, y):
    # same formula as MACS3.Signal.ScoreTrack.logLR_sym (x > y branch mirrored)
    if x > y:
        return (x * (math.log(x) - math.log(y)) + y - x) * LOG10_E
    if x < y:
        return -(y * (math.log(y) - math.log(x)) + x - y) * LOG10_E
    return 0.0


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout)
        print(r.stderr)
        raise SystemExit(f"command failed: {' '.join(cmd)}")
    return r


def read_scores(path):
    out = []
    with open(path) as f:
        for line in f:
            if line.startswith("track"):
                continue
            p = line.rstrip("\n").split("\t")
            out.append((p[0], int(p[1]), int(p[2]), float(p[4])))
    return out


def part1(tmp):
    print("== Part 1: synthetic four-track case, macs3 bdgdiff -C 0.2 --d1 1 --d2 1")
    pseudo = 0.01  # TwoConditionScores default pseudocount (bdgdiff does not override it)
    # (start, end, t1, c1, t2, c2)
    regions = [(0, 1000, 20.0, 2.0, 18.0, 2.0),      # both enriched, nearly equal -> common
               (1000, 2000, 20.0, 2.0, 15.0, 2.0),   # cond1 > cond2, small fractional logLR
               (2000, 3000, 40.0, 2.0, 15.0, 2.0),   # cond1 >> cond2, logLR > 1
               (3000, 4000, 2.0, 2.0, 2.0, 2.0)]     # background
    names = ["t1", "c1", "t2", "c2"]
    for i, n in enumerate(names):
        with open(os.path.join(tmp, n + ".bdg"), "w") as f:
            for r in regions:
                f.write(f"chr1\t{r[0]}\t{r[1]}\t{r[2 + i]}\n")
    run([sys.argv[2] if len(sys.argv) > 2 else "macs3", "bdgdiff",
         "--t1", "t1.bdg", "--c1", "c1.bdg", "--t2", "t2.bdg", "--c2", "c2.bdg",
         "--d1", "1", "--d2", "1", "-C", "0.2", "-l", "200", "-g", "100",
         "--o-prefix", "syn", "--outdir", tmp], cwd=tmp)
    print("expected mean log10LR per region (documented score column):")
    for r in regions[:3]:
        t1, c1, t2, c2 = (v + pseudo for v in r[2:])
        print(f"  chr1:{r[0]}-{r[1]}  t1_vs_c1={logLR_asym(t1, c1):.4f}  "
              f"t2_vs_c2={logLR_asym(t2, c2):.4f}  t1_vs_t2={logLR_sym(t1, t2):.4f}")
    for cat in ("cond1", "cond2", "common"):
        path = os.path.join(tmp, f"syn_c0.2_{cat}.bed")
        rows = read_scores(path)
        print(f"{cat}.bed score column: " +
              (", ".join(f"{c}:{s}-{e} -> {v}" for c, s, e, v in rows) if rows else "(empty)"))


def part2(src, tmp):
    print("\n== Part 2: project's own test data (test/cmdlinetest step 10, bdgdiff)")
    macs3 = sys.argv[2] if len(sys.argv) > 2 else "macs3"
    test = os.path.join(src, "test")
    chip = os.path.join(test, "CTCF_SE_ChIP_chr22_50k.bed.gz")
    ctrl = os.path.join(test, "CTCF_SE_CTRL_chr22_50k.bed.gz")
    run([macs3, "callpeak", "-g", "52000000", "-t", chip, "-c", ctrl, "-n", "n0", "-B",
         "--outdir", tmp])
    run([macs3, "callpeak", "-g", "10000000", "--nomodel", "--extsize", "250", "-c", chip,
         "-t", ctrl, "-n", "rev", "-B", "--outdir", tmp])
    run([macs3, "bdgdiff", "--t1", os.path.join(tmp, "n0_treat_pileup.bdg"),
         "--c1", os.path.join(tmp, "n0_control_lambda.bdg"),
         "--t2", os.path.join(tmp, "rev_treat_pileup.bdg"),
         "--c2", os.path.join(tmp, "rev_control_lambda.bdg"),
         "--o-prefix", "run_bdgdiff_prefix", "--outdir", tmp])
    for cat in ("cond1", "cond2", "common"):
        got = read_scores(os.path.join(tmp, f"run_bdgdiff_prefix_c3.0_{cat}.bed"))
        ref = read_scores(os.path.join(test, "standard_results_bdgdiff",
                                       f"run_bdgdiff_prefix_c3.0_{cat}.bed"))
        same_coords = [g[:3] for g in got] == [r[:3] for r in ref]
        nint = sum(1 for g in got if g[3] == int(g[3]))
        ndiff = sum(1 for g, r in zip(got, ref) if abs(g[3] - r[3]) > 1e-3)
        print(f"{cat}: {len(got)} regions (reference {len(ref)}), coordinates identical: {same_coords}, "
              f"integer-valued scores: {nint}/{len(got)}, scores differing from reference: {ndiff}")
        for g, r in list(zip(got, ref))[:3]:
            print(f"   {g[0]}:{g[1]}-{g[2]}  got {g[3]}  reference {r[3]}")


if __name__ == "__main__":
    src = sys.argv[1]
    with tempfile.TemporaryDirectory() as tmp:
        part1(tmp)
        part2(src, tmp)
