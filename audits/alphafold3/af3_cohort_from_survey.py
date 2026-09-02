#!/usr/bin/env python3
"""AlphaFold 3 cohort, derived from the survey's stored evidence sentences.

`af3_profile.py` is the preferred instrument: it re-reads each paper's full
text from Europe PMC. That API is unreachable from the environment this audit
ran in (the egress proxy denies www.ebi.ac.uk), so this script falls back to
the evidence sentences already captured in survey/data/paper_software.tsv.

The fallback is strictly weaker. An evidence sentence is one sentence per
package per paper, so a paper that used AlphaFold 3 but whose captured sentence
happens not to say "3" is invisible here, and feature detection is limited to
what that one sentence plus the paper's recorded pipeline mention. Read the
counts below as a lower bound on AlphaFold 3 usage, not as a census.
"""
import csv, json, re
from collections import Counter, defaultdict

AF3 = re.compile(r"AlphaFold[ -]?3\b|AlphaFold ?v?3\.\d|\bAF3\b|AlphaFold[- ]?Server|alphafoldserver\.com", re.I)
AF2 = re.compile(r"AlphaFold[ -]?2\b|AlphaFold2|\bAF2\b|ColabFold", re.I)
SERVER = re.compile(r"AlphaFold[- ]?Server|alphafoldserver\.com", re.I)
FEATURES = {
    "AlphaFold Server named": SERVER,
    "ligand / small molecule": re.compile(r"ligand|small molecule|SMILES|\bCCD\b", re.I),
    "nucleic acid (DNA/RNA)": re.compile(r"\bDNA\b|\bRNA\b", re.I),
    "modified residue / PTM": re.compile(r"phosphoryl|glycosyl|acetylat|methylat|modified residue", re.I),
    "template mentioned": re.compile(r"template", re.I),
    "MSA mentioned": re.compile(r"\bMSA\b|multiple sequence alignment", re.I),
    "seed mentioned": re.compile(r"\bseed", re.I),
    "confidence metric (pLDDT/pTM/ipTM/PAE)": re.compile(r"pLDDT|\bpTM\b|\bipTM\b|\bPAE\b|predicted aligned error", re.I),
    "ranking score": re.compile(r"ranking score|ranked_0|top[- ]ranked", re.I),
    "molecular replacement / experimental": re.compile(r"molecular replacement|Phaser|PHENIX|cryo[- ]?EM|crystallograph", re.I),
}

rows = []
with open("../../survey/data/paper_software.tsv") as fh:
    for r in csv.DictReader(fh, delimiter="\t"):
        if r["package"] == "AlphaFold":
            rows.append(r)

papers = defaultdict(list)
for r in rows:
    papers[r["pmcid"]].append(r)

af3, af2_only, unclear = {}, 0, 0
for pmcid, rs in papers.items():
    blob = " ".join(r["evidence_sentence"] for r in rs)
    if AF3.search(blob):
        af3[pmcid] = (rs[0], blob)
    elif AF2.search(blob):
        af2_only += 1
    else:
        unclear += 1

print("AlphaFold-using papers in the survey:      %d" % len(papers))
print("  evidence sentence names AlphaFold 3/AF3/Server: %d" % len(af3))
print("  evidence sentence names only AlphaFold 2:       %d" % af2_only)
print("  evidence sentence names no major version:       %d" % unclear)

jc, fc, yc = Counter(), Counter(), Counter()
server = 0
for pmcid, (r, blob) in af3.items():
    jc[r["journal"]] += 1
    yc[r["year"]] += 1
    if SERVER.search(blob):
        server += 1
    for k, rx in FEATURES.items():
        if rx.search(blob):
            fc[k] += 1
print("\nJOURNAL:", dict(jc.most_common()))
print("YEAR:   ", dict(sorted(yc.items())))
print("AlphaFold Server explicitly named (i.e. not this codebase): %d/%d" % (server, len(af3)))
print("\nFEATURES named in the evidence sentence (papers):")
for k, n in fc.most_common():
    print("  %-42s %d" % (k, n))

with open("af3_cohort.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t")
    w.writerow(["pmcid", "doi", "journal", "year", "server_named", "evidence_sentence"])
    for pmcid, (r, blob) in sorted(af3.items(), key=lambda kv: (kv[1][0]["journal"], kv[1][0]["year"])):
        w.writerow([pmcid, r["doi"], r["journal"], r["year"],
                    bool(SERVER.search(blob)), blob[:600]])
print("\nwrote af3_cohort.tsv (%d papers)" % len(af3))
