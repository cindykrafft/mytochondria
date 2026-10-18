"""Cohort profile for minimap2 from the survey cache (survey/data/paper_software.tsv).
Counts are lower bounds: each paper contributes one stored evidence sentence."""
import csv, re, collections, os, sys
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "survey", "data")
rows = [r for r in csv.DictReader(open(os.path.join(root, "paper_software.tsv")), delimiter="\t") if r["package"] == "minimap2"]
print(f"papers: {len(set(r['pmcid'] for r in rows))}")
print("journals:", dict(collections.Counter(r["journal"] for r in rows)))
v = collections.Counter(r["version"] or "unstated" for r in rows)
print("versions:", ", ".join(f"{k} x{n}" for k, n in v.most_common()))
pats = {
    "-ax (SAM output)": r"-ax\b", "map-ont / nanopore / ONT": r"map-ont|[Nn]anopore|\bONT\b",
    "map-pb / map-hifi / PacBio / HiFi": r"map-pb|map-hifi|[Hh]i[Ff]i|PacBio", "-x splice / splice": r"splice",
    "-x sr / short-read mode": r"-x\s*sr\b|\bsr\b preset|short[- ]read", "asm5/asm10/asm20": r"asm5|asm10|asm20|-x\s*asm",
    "--secondary=no": r"secondary=no", "secondary/supplementary named": r"secondary|supplementary",
    "MAPQ / mapping quality": r"MAPQ|mapping quality", "PAF": r"\bPAF\b|\.paf\b", "cs tag / paftools": r"--cs|cs tag|paftools",
}
for k, p in pats.items():
    print(f"  {k:36s} {len(set(r['pmcid'] for r in rows if re.search(p, r['evidence_sentence'])))}")
print("pipeline stages:", collections.Counter(s for r in rows for s in r["pipeline_stages"].split(";") if s).most_common(6))
