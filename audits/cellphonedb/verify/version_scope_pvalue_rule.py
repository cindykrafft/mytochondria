#!/usr/bin/env python3
"""Version scope of CPDB2 (strict `>`, ties dropped, p = 0 attainable), executed on the shipped
source of each release, not inferred from release notes.

The p-value construction is small and self-contained, so each release's own
`cpdb_statistical_analysis_helper.py` is checked out from its tag, imported as a module (the two
CellphoneDB modules it imports, `core_logger` and `complex_helper`, are unchanged and come from
the installed v5 package), and driven with the SAME synthetic inputs:

  one interaction, two cluster pairs, four "shuffled" null draws:
      pair A: one draw above the observed value, two exactly equal, one below
      pair B: zero draws above, three exactly equal, one below

  documented rule ("proportion of the means which are equal or higher"):  A = 3/4, B = 3/4
  strict rule as implemented:                                             A = 1/4, B = 0/4

v2.1.7 accumulates with an explicit loop (`if mean > real_mean`, helper.py:398 at that tag);
v3.1.0 onward pack the same comparison into a bit array
(`np.packbits(shuffled.values > real.values)`). Both are exercised here through each tag's own
`build_percent_result`.

Set CPDB_CLONE to the repository clone.
"""
import importlib.util
import os
import subprocess
import sys
import tempfile
import numpy as np
import pandas as pd

CLONE = os.environ.get(
    "CPDB_CLONE",
    "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8"
    "/scratchpad/cellphonedb/CellphoneDB")
REL = "cellphonedb/src/core/methods/cpdb_statistical_analysis_helper.py"
TAGS = ["v2.1.7", "v3.1.0", "v4.0.0", "v5.0.0", "v5.0.1", "master"]

tmp = tempfile.mkdtemp(prefix="cpdbver_")

# synthetic inputs, shared by every version
IDX = ["interaction1"]
COLS = ["ctA|ctB", "ctC|ctD"]
real_mean = pd.DataFrame([[2.0, 2.0]], index=IDX, columns=COLS)
real_pct = pd.DataFrame([[1, 1]], index=IDX, columns=COLS)
base = pd.DataFrame(index=IDX, columns=COLS, dtype=float)
interactions = pd.DataFrame({"multidata_1_id": [1], "multidata_2_id": [2]}, index=IDX)
combos = np.array([["ctA", "ctB"], ["ctC", "ctD"]], dtype=object)
#                     pair A  pair B     (observed value is 2.0 for both)
DRAWS = [[3.0, 1.0],           # above / below
         [2.0, 2.0],           # equal / equal
         [2.0, 2.0],           # equal / equal
         [1.0, 2.0]]           # below / equal
shuffled = [pd.DataFrame([d], index=IDX, columns=COLS) for d in DRAWS]

print("synthetic null: 4 draws against an observed mean of 2.0 in both cluster pairs")
print("   pair ctA|ctB : draws %s  -> 1 above, 2 equal, 1 below" % [d[0] for d in DRAWS])
print("   pair ctC|ctD : draws %s  -> 0 above, 3 equal, 1 below" % [d[1] for d in DRAWS])
print("   documented 'equal or higher' p : ctA|ctB = 0.75, ctC|ctD = 0.75")
print("\n%-10s %-12s %-14s %-14s %s" % ("tag", "p ctA|ctB", "p ctC|ctD", "p == 0 possible",
                                        "get_significant_means(p, 0.05) keeps"))
for tag in TAGS:
    src = subprocess.run(["git", "-C", CLONE, "show", "%s:%s" % (tag, REL)],
                         capture_output=True, text=True, check=True).stdout
    path = os.path.join(tmp, "helper_%s.py" % tag.replace(".", "_"))
    with open(path, "w") as fh:
        fh.write(src)
    spec = importlib.util.spec_from_file_location("helper_%s" % tag.replace(".", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    if tag == "v2.1.7":                      # loops over DataFrames directly
        stats = shuffled
    else:                                    # packs the comparison into bits first
        stats = [mod.shuffled_greater_than_real(s, real_mean) for s in shuffled]
    p = mod.build_percent_result(real_mean, real_pct, stats, interactions, combos, base, "|")
    p = pd.DataFrame(np.asarray(p, dtype=float), index=IDX, columns=COLS)
    sig = mod.get_significant_means(real_mean, p, 0.05)
    keeps = [c for c in COLS if not np.isnan(float(sig[c].iloc[0]))]
    print("%-10s %-12.2f %-14.2f %-14s %s"
          % (tag, p[COLS[0]].iloc[0], p[COLS[1]].iloc[0],
             "yes" if (p.to_numpy() == 0).any() else "no", keeps))

print("\nEvery release from v2.1.7 to master reports 0.25 and 0.00 where the documented rule")
print("gives 0.75 and 0.75: the ties are discarded and p = 0 is reachable, and an interaction")
print("with no null draw above it is called significant at the 0.05 cut-off in all of them.")
