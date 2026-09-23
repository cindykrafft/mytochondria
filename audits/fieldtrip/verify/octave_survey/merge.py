#!/usr/bin/env python3
"""Merge the survey runs into one final outcome per test and print the before/after tables.

Runs (raw TSVs from octave_survey.py, in this directory):
  octave_survey_raw.tsv         all 472 DATA-no tests on master cfdad9b
  octave_survey_fixed_raw.tsv   the 280 failures re-run on branch fix/octave-compat-survey at 4dfba5c
                                (external/stats path; startsWith/endsWith cell patterns)
  octave_survey_fixed2_raw.tsv  the tests still failing after that, re-run at 9ad3bfb (+ contains cell patterns)
  octave_survey_fixed3_raw.tsv  the tests still failing in istrue, re-run at ce18267 (+ ft_fetch_data addParameter)
  octave_survey_fixed4_raw.tsv  the bot-suggested tests of PR #2622 re-run at 99b4c3c (+ the test/private copy of ft_fetch_data)
A test's final outcome is its row in the latest run that includes it. Writes results_master.tsv and
results_final.tsv (with the category from classify.py and the run the row comes from).
"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify import classify

def load(p):
    return {r.split("\t")[0]: (r.rstrip("\n").split("\t") + [""] * 6)[:6] for r in open(p) if not r.startswith("test\t")}

H = os.path.dirname(os.path.abspath(__file__))
runs = [("master", "octave_survey_raw.tsv"), ("fixed", "octave_survey_fixed_raw.tsv"),
        ("fixed2", "octave_survey_fixed2_raw.tsv"), ("fixed3", "octave_survey_fixed3_raw.tsv"),
        ("fixed4", "octave_survey_fixed4_raw.tsv")]
data = [(name, load(os.path.join(H, f))) for name, f in runs if os.path.exists(os.path.join(H, f))]
master = data[0][1]
# test_ft_connectivityanalysis_hanning is this project's own test from the #2610 work (untracked in the
# survey checkout, not an upstream test); it is left out of the tables, which cover the 471 upstream tests.
master.pop("test_ft_connectivityanalysis_hanning", None)
final = {}
for t, r in master.items():
    src = "master"; row = r
    for name, d in data[1:]:
        if t in d: src, row = name, d[t]
    final[t] = (row, src)

def write(path, table):
    with open(path, "w") as f:
        f.write("test\toutcome\tseconds\twalltime\tmem\tcategory\tmessage\trun\n")
        for t in sorted(table):
            row, src = table[t]
            f.write("\t".join([row[0], row[1], row[2], row[3], row[4], classify(row[1], row[5]), row[5], src]) + "\n")

write(os.path.join(H, "results_master.tsv"), {t: (r, "master") for t, r in master.items()})
write(os.path.join(H, "results_final.tsv"), final)

def tally(table):
    return collections.Counter(classify(row[1], row[5]) for row, _ in table.values())
n = len(master)
before = tally({t: (r, "master") for t, r in master.items()}); after = tally(final)
cats = ["pass", "ft-nanmean", "ft-startswith", "ft-fetchdata", "matlab-only", "mex", "graphics", "octave-difference",
        "external", "dpss-hack", "data", "timeout", "crash"]
print(f"| category | master cfdad9b | with the fix branch |\n|---|---|---|")
for c in cats:
    if before[c] or after[c]:
        print(f"| {c} | {before[c]} ({100*before[c]/n:.1f} %) | {after[c]} ({100*after[c]/n:.1f} %) |")
print(f"| total | {n} | {n} |")
print()
for c in ("octave-difference", "matlab-only", "graphics", "mex", "external", "dpss-hack", "data", "timeout", "ft-nanmean", "ft-startswith", "ft-fetchdata"):
    sel = sorted((t, row) for t, (row, _) in final.items() if classify(row[1], row[5]) == c)
    if not sel: continue
    print(f"## still failing after the fix branch: {c} ({len(sel)})")
    for t, row in sel: print(f"- {t}: {row[5][:150]}")
    print()
