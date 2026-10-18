"""Cohort profile for BWA from the survey cache (offline; evidence sentences only,
so every count is a lower bound). Usage: python3 bwa_profile.py [survey/data dir]"""
import csv, collections, re, sys, os
d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "..", "survey", "data")
rows = [r for r in csv.DictReader(open(os.path.join(d, "paper_software.tsv")), delimiter="\t") if r["package"] == "BWA"]
print("papers naming BWA:", len(rows))
v = collections.Counter(r["version"] for r in rows if r["version"])
print("version stated:", sum(v.values()), "  ", ", ".join("%s x%d" % kv for kv in v.most_common(12)))
pats = [("bwa mem / BWA-MEM", r"bwa[\s-]*mem|BWA[\s-]*MEM"), ("aln / samse / sampe / backtrack", r"\baln\b|sampe|samse|backtrack"),
        ("paired-end", r"paired[\s-]end"), ("single-end", r"single[\s-]end"), ("-M flag", r"\s-M\b"),
        ("MAPQ / mapping quality", r"MAPQ|mapping quality|\bMQ\b"), ("uniquely mapped / XS / XA / multi-map", r"unique|\bXS\b|\bXA\b|multi-?map"),
        ("GATK / HaplotypeCaller / Mutect", r"GATK|HaplotypeCaller|Mutect"), ("ancient DNA", r"ancient|aDNA"),
        ("ChIP-seq / ATAC", r"ChIP|ATAC"), ("Hi-C", r"Hi-?C\b")]
for name, p in pats:
    print("%-40s %d" % (name, sum(1 for r in rows if re.search(p, r["evidence_sentence"], re.I if name != "-M flag" else 0))))
st = collections.Counter(s for r in rows for s in r["pipeline_stages"].split(";") if s)
print("pipeline stages:", dict(st.most_common(6)))
