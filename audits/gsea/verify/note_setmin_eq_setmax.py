#!/usr/bin/env python3
"""N-note: GeneSetCohort.Generator.filterGeneSetsByMembersAndSize skips the size filter
when set_min == set_max ("@note hack"), which also skips the step that restricts each set
to the genes present in the ranked list.  A set with one member absent from the list
then reaches the scoring table, which asks the ranked list for that member's score.

Run: python3 note_setmin_eq_setmax.py
"""
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsea_cli as G  # noqa: E402
import synth  # noqa: E402

W = "/tmp/gseawork/note_setmin"
os.makedirs(W, exist_ok=True)
names, sc, rng = synth.ranked_list(N=2000, seed=11)
gs = {"ALL_PRESENT": list(rng.choice(names, 20, replace=False)),
      "ONE_ABSENT": list(rng.choice(names, 19, replace=False)) + ["NOT_IN_LIST"]}
G.write_rnk(f"{W}/list.rnk", names, sc)
G.write_gmt(f"{W}/sets.gmt", gs)
for smin, smax in ((15, 500), (20, 20), (19, 19)):
    cmd = [G.JAVA, "-Xmx1g", "-cp", G.GSEA_CP, "xtools.gsea.GseaPreranked", "-rnk", f"{W}/list.rnk",
           "-gmx", f"{W}/sets.gmt", "-out", f"{W}/out_{smin}_{smax}", "-nperm", "10", "-rnd_seed", "149",
           "-collapse", "No_Collapse", "-set_min", str(smin), "-set_max", str(smax)] + G.COMMON
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=G.SCRATCH)
    log = r.stdout + r.stderr
    err = [l for l in log.splitlines() if "Exception" in l or "No such name" in l]
    ok = r.returncode == 0 and os.path.isdir(f"{W}/out_{smin}_{smax}") and any(
        p.startswith("run.") for p in os.listdir(f"{W}/out_{smin}_{smax}"))
    sets = ""
    if ok:
        run = sorted(os.path.join(f"{W}/out_{smin}_{smax}", p) for p in os.listdir(f"{W}/out_{smin}_{smax}") if p.startswith("run."))[-1]
        sets = ", ".join(f"{k}(size {v['SIZE']})" for k, v in G.parse_report_tsv(run).items())
    print(f"set_min={smin} set_max={smax}: exit={r.returncode} report written={ok}; sets reported: {sets or '-'}; "
          f"first error line: {err[0][:120] if err else '-'}")
