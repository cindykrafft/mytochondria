#!/usr/bin/env python3
"""Lower-bound profile of how the cohort's HMMER papers use it, from the survey's stored
evidence sentences only (survey/data/paper_software.tsv; one sentence per paper, so every
count is a lower bound). Usage: python3 hmmer_profile.py > profile_run.log"""
import csv, re, collections, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "survey", "data", "paper_software.tsv")
rows = [r for r in csv.DictReader(open(D), delimiter="\t") if r["package"] == "HMMER"]
txt = collections.defaultdict(str)
for r in rows: txt[r["pmcid"]] += " " + r["evidence_sentence"]
F = {"hmmsearch": r"hmmsearch", "hmmscan": r"hmmscan", "phmmer": r"phmmer", "jackhmmer": r"jackhmmer",
     "nhmmer/nhmmscan": r"nhmmer|nhmmscan", "hmmbuild": r"hmmbuild", "Pfam named": r"Pfam",
     "--cut_ga/tc/nc or 'gathering'": r"cut_ga|gathering|--cut_tc|--cut_nc|trusted cutoff",
     "E-value threshold stated": r"[Ee]-?value|E <|E ?=|-E \d|evalue", "bit-score threshold": r"bit ?score|-T \d|--domT",
     "domain E-value / --domE": r"domE|domain E|i-Evalue|c-Evalue|incdomE", "-Z stated": r" -Z |-Z \d",
     "TIGRFAM/KOfam/dbCAN/antiSMASH/eggNOG": r"TIGRFAM|KOfam|kofam|dbCAN|antiSMASH|eggNOG",
     "AlphaFold/ColabFold MSAs": r"AlphaFold|ColabFold|UniRef90|BFD|MGnify"}
print("papers", len(txt))
for k, v in F.items(): print("%-40s %d" % (k, sum(1 for p in txt if re.search(v, txt[p]))))
print("versions", collections.Counter(r["version"] for r in rows if r["version"]).most_common())
