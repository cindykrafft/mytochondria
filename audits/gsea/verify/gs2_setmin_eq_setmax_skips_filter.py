#!/usr/bin/env python3
"""GS2: when -set_min equals -set_max, GSEA silently analyses gene sets of every size.

GeneSetCohort.Generator.filterGeneSetsByMembersAndSize
(src/main/java/edu/mit/broad/genome/alg/gsea/GeneSetCohort.java:188-197, master dc35c76)
runs the size filter only when geneSetMinSize != geneSetMaxSize; the equal case falls into
an `else { // @note hack }` branch that does nothing.  So `-set_min 20 -set_max 20` does not
select the size-20 sets -- it turns the filter off, and every set in the GMT is scored and
reported with a nominal p, an FDR q and an NES.

The same branch also skips the step that restricts each set to the genes present in the
ranked list (removeGeneSetsSmallerThan(gsets, min, rl) does that restriction), so a set with
one member missing from the ranked list aborts the run instead of being trimmed.

Both are shown here.  Synthetic ranked list, sets of known size, no external data.

Run: GSEA_CP=<classpath> python3 gs2_setmin_eq_setmax_skips_filter.py
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsea_cli as G  # noqa: E402
import synth  # noqa: E402

W = "/tmp/gseawork/gs2"
os.makedirs(W, exist_ok=True)
print("jar/classpath:", G.GSEA_CP)

names, sc, rng = synth.ranked_list(N=4000, seed=7)
SIZES = [5, 15, 20, 100, 600]
sets = {f"SET_{n}": list(rng.choice(names, n, replace=False)) for n in SIZES}
G.write_rnk(f"{W}/list.rnk", names, sc)
G.write_gmt(f"{W}/sets.gmt", sets)

# a second GMT: same sets, plus one set whose members are all present except one
sets2 = dict(sets)
sets2["SET_20_ONE_ABSENT"] = list(rng.choice(names, 19, replace=False)) + ["NOT_IN_LIST"]
G.write_gmt(f"{W}/sets_absent.gmt", sets2)


def run(gmt, smin, smax, tag):
    out = f"{W}/out_{tag}"
    cmd = [G.JAVA, "-Xmx2g", "-cp", G.GSEA_CP, "xtools.gsea.GseaPreranked", "-rnk", f"{W}/list.rnk",
           "-gmx", gmt, "-out", out, "-nperm", "100", "-rnd_seed", "149",
           "-collapse", "No_Collapse", "-set_min", str(smin), "-set_max", str(smax)] + G.COMMON
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=G.SCRATCH)
    log = r.stdout + r.stderr
    runs = sorted(p for p in os.listdir(out)) if os.path.isdir(out) else []
    runs = [p for p in runs if p.startswith("run.")]
    if r.returncode != 0 or not runs:
        err = [l for l in log.splitlines() if "Exception" in l or "No such name" in l]
        return None, (err[0][:110] if err else f"exit {r.returncode}")
    rep = G.parse_report_tsv(os.path.join(out, runs[-1]))
    return {k: int(v["SIZE"]) for k, v in rep.items()}, None


print("\nA. size filter, GMT with sets of sizes", SIZES)
for smin, smax in ((20, 500), (20, 100), (20, 20), (100, 100), (5, 5)):
    got, err = run(f"{W}/sets.gmt", smin, smax, f"{smin}_{smax}")
    if got is None:
        print(f"  -set_min {smin:>3} -set_max {smax:>3}: FAILED: {err}")
        continue
    want = sorted(n for n in SIZES if smin <= n <= smax)
    have = sorted(got.values())
    verdict = "ok" if have == want else "FILTER NOT APPLIED"
    print(f"  -set_min {smin:>3} -set_max {smax:>3}: sets reported {sorted(got)} sizes {have}; "
          f"expected sizes {want}  -> {verdict}")

print("\nB. same thresholds, GMT that also holds one set with a member absent from the .rnk")
for smin, smax in ((20, 500), (20, 20)):
    got, err = run(f"{W}/sets_absent.gmt", smin, smax, f"abs_{smin}_{smax}")
    if got is None:
        print(f"  -set_min {smin:>3} -set_max {smax:>3}: run ABORTED: {err}")
    else:
        print(f"  -set_min {smin:>3} -set_max {smax:>3}: sets reported {sorted(got)} sizes {sorted(got.values())}")
