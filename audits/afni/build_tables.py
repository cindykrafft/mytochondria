#!/usr/bin/env python3
"""Join the profiled AFNI cohort into the two published tables."""
import json, csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = [json.loads(l) for l in open(os.path.join(HERE, "afni_profiles.jsonl"))]

# finding -> (trigger test, condition note). Conservative: a paper is listed when
# it ran the *program*, with the option/data condition that actually fires the
# bug spelled out in parentheses.
def has(c, *cmds):  return any(x in c.get("commands", []) for x in cmds)
def feat(c, *fs):   return any(f in c.get("features", []) for f in fs)

RULES = [
 ("AF1",  lambda c: feat(c, "regional homogeneity (3dReHo)") or has(c, "3dReHo"),
          "if ReHo input was percent-scaled/z-scored"),
 ("AF2",  lambda c: has(c, "3dttest++"), "if -paired -zskip"),
 ("AF3",  lambda c: has(c, "3dMEMA"), "if -missing_data, >1 group"),
 ("AF4",  lambda c: has(c, "3dLMEr"), "if -gltCode and -glfCode in one run"),
 ("AF4b", lambda c: has(c, "3dLME"), "if multiple -glfCode with differing DF"),
 ("AF5",  lambda c: has(c, "3dMVM"), "if -robust with GLTs"),
 ("AF6",  lambda c: has(c, "3dTshift") or feat(c, "slice timing (3dTshift)"),
          "if sequential-descending NIfTI slice codes"),
 ("AF7",  lambda c: has(c, "3dROIstats"), "if -sigma/-nzsigma reported"),
 ("AF8",  lambda c: has(c, "3dcalc"), "if atanh() on r-maps reaching +/-1"),
 ("AF9",  lambda c: has(c, "3dFWHMx", "3dBlurToFWHM"),
          "if ACF FWHM quoted as kernel FWHM, or -acf -FWHM used"),
 ("AF10", lambda c: has(c, "3dttest++"), "if -BminusA with -nomeans/-notests"),
 ("AF11", lambda c: has(c, "3dttest++", "3dGroupInCorr"), "if -toz and |z| > 7.7"),
 ("AF12", lambda c: has(c, "3dTstat"), "if -DW/-tdiff/-nzmean"),
 ("AF13", lambda c: has(c, "3dBrickStat"), "if -automask or -absolute"),
 ("AF14", lambda c: has(c, "3dDWItoDT"), "if a zero-gradient row is present"),
 ("AF15", lambda c: has(c, "1dgenARMA11"), "if -arma31/-arma51"),
 ("AF17", lambda c: has(c, "3dANOVA", "3dANOVA2", "3dANOVA3", "3dttest"),
          "if raw un-demeaned data, mean >> sigma"),
 ("AF18", lambda c: has(c, "3dTproject", "3dBandpass"),
          "passband-edge bin differs between AFNI's own bandpass routes"),
]

with open(os.path.join(HERE, "afni_papers.tsv"), "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["pmcid", "doi", "journal", "year", "version", "commands", "features", "title"])
    for c in sorted(P, key=lambda c: (c["journal"], -int(c["year"]))):
        w.writerow([c["pmcid"], c["doi"], c["journal"], c["year"],
                    ";".join(c.get("versions_all", [])),
                    ";".join(c.get("commands", [])),
                    ";".join(c.get("features", [])),
                    c["title"]])

with open(os.path.join(HERE, "afni_paper_exposure.tsv"), "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["pmcid", "doi", "journal", "year", "versions", "findings", "title"])
    for c in sorted(P, key=lambda c: (c["journal"], -int(c["year"]))):
        f = ["%s (%s)" % (fid, note) for fid, test, note in RULES if test(c)]
        w.writerow([c["pmcid"], c["doi"], c["journal"], c["year"],
                    ";".join(c.get("versions_all", [])), ";".join(f), c["title"]])

from collections import Counter
n = Counter()
for c in P:
    for fid, test, note in RULES:
        if test(c): n[fid] += 1
print("papers:", len(P))
print("exposure counts:", dict(n.most_common()))
print("papers with at least one candidate finding:",
      sum(1 for c in P if any(t(c) for _, t, _ in RULES)))
