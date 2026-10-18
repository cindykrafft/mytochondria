"""Cohort profile for kallisto from the survey's stored evidence sentences
(survey/data/paper_software.tsv, rows with package == kallisto).  Offline:
each count is a lower bound over a few hundred characters per paper."""
import collections, csv, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
tsv = os.path.join(here, "..", "..", "survey", "data", "paper_software.tsv")
rows = [r for r in csv.DictReader(open(tsv), delimiter="\t") if r["package"] == "kallisto"]
papers = {}
for r in rows:
    papers.setdefault(r["pmcid"], []).append(r)
print("rows %d, papers %d" % (len(rows), len(papers)))
ver = collections.Counter(r["version"] or "(none)" for r in rows)
print("versions:", ", ".join("%s x%d" % kv for kv in ver.most_common()))
pats = {
    "bootstrap (-b / bootstrap)": r"bootstrap|\b-b\s*\d",
    "single-end with -l/-s or --single": r"--single|single[- ]end|-l \d+ -s",
    "--single-overhang": r"single-overhang",
    "--bias": r"[-–]bias\b",
    "stranded option (--rf/--fr-stranded)": r"(rf|fr)-stranded",
    "TPM reported": r"\bTPM\b|transcripts per million",
    "sleuth downstream": r"sleuth",
    "threads stated": r"thread",
    "default parameters stated": r"default param",
}
for k, p in pats.items():
    n = sum(1 for pm, rs in papers.items() if any(re.search(p, r["evidence_sentence"], re.I) for r in rs))
    print("%-40s %d" % (k, n))
for pm, rs in papers.items():
    for r in rs:
        s = r["evidence_sentence"]
        if re.search(r"-l \d|single-overhang|[-–]bias\b|thread", s, re.I):
            print("  %s %s %s: %s" % (pm, r["year"], r["version"] or "-", s[:220]))
