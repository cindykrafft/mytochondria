#!/usr/bin/env python3
"""Turn extraction results into the survey deliverable."""
import json, os, re, sys, csv
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import STEPS
STEP_ORDER = [n for n, _ in STEPS]

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
RES = os.path.join(HERE, "results.jsonl")
GAP = os.path.join(HERE, "gap_list.jsonl")

os.makedirs(os.path.join(OUT, "data"), exist_ok=True)
os.makedirs(os.path.join(OUT, "packages"), exist_ok=True)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def load():
    rows, errs = [], Counter()
    for line in open(RES):
        try:
            r = json.loads(line)
        except Exception:
            continue
        if "error" in r:
            errs[r["error"]] += 1
            continue
        rows.append(r)
    return rows, errs


def pipeline_text(rec):
    """Grounded pipeline description: tools bucketed into canonical stages."""
    oss = {t: h for t, h in rec["software"].items() if h["license"] == "open-source"}
    if not oss:
        return "", []
    by_step = defaultdict(list)
    unassigned = []
    for t, h in oss.items():
        label = t + (" v%s" % h["version"] if h["version"] else "")
        if h["steps"]:
            for s in h["steps"]:
                by_step[s].append(label)
        else:
            unassigned.append(label)
    stages = []
    for s in STEP_ORDER:
        if by_step.get(s):
            stages.append("%s [%s]" % (s, ", ".join(sorted(set(by_step[s])))))
    if unassigned:
        stages.append("stage not stated [%s]" % ", ".join(sorted(set(unassigned))))
    return " -> ".join(stages), stages


def main():
    rows, errs = load()
    papers = [r for r in rows if r["n_software"] > 0]
    print("processed=%d  with_oss=%d  errors=%s" % (len(rows), len(papers), dict(errs)))

    # ---------- package index ----------
    pkg = defaultdict(lambda: {"papers": [], "cat": "", "versions": Counter(),
                               "journals": Counter(), "years": Counter(), "steps": Counter()})
    for r in papers:
        for t, h in r["software"].items():
            if h["license"] != "open-source":
                continue
            p = pkg[t]
            p["cat"] = h["category"]
            p["papers"].append(r)
            if h["version"]:
                p["versions"][h["version"]] += 1
            p["journals"][r["journal"]] += 1
            p["years"][r["year"]] += 1
            for s in h["steps"]:
                p["steps"][s] += 1

    ranked = sorted(pkg.items(), key=lambda kv: -len(kv[1]["papers"]))

    # ---------- data/package_index.tsv ----------
    with open(os.path.join(OUT, "data", "package_index.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["package", "category", "n_papers", "journals", "years",
                    "top_versions", "typical_pipeline_stages"])
        for t, p in ranked:
            w.writerow([t, p["cat"], len(p["papers"]),
                        ";".join("%s=%d" % kv for kv in p["journals"].most_common()),
                        ";".join("%s=%d" % kv for kv in sorted(p["years"].items())),
                        ";".join("%s=%d" % kv for kv in p["versions"].most_common(5)),
                        ";".join("%s=%d" % kv for kv in p["steps"].most_common(4))])

    # ---------- data/papers.tsv + pipelines.jsonl ----------
    with open(os.path.join(OUT, "data", "papers.tsv"), "w", newline="") as fh, \
         open(os.path.join(OUT, "data", "pipelines.jsonl"), "w") as pf:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["pmcid", "pmid", "doi", "journal", "year", "title",
                    "n_oss_packages", "packages", "pipeline"])
        for r in sorted(papers, key=lambda r: (r["journal"], r["year"] or "", r["pmcid"])):
            pt, stages = pipeline_text(r)
            names = sorted(t for t, h in r["software"].items()
                           if h["license"] == "open-source")
            w.writerow([r["pmcid"], r["pmid"], r["doi"], r["journal"], r["year"],
                        (r["title"] or "").replace("\t", " "), len(names),
                        "; ".join(names), pt])
            pf.write(json.dumps({
                "pmcid": r["pmcid"], "doi": r["doi"], "journal": r["journal"],
                "year": r["year"], "title": r["title"], "authors": r.get("authors"),
                "packages": names, "pipeline_stages": stages,
                "evidence": {t: h["evidence"][0] for t, h in r["software"].items()
                             if h["license"] == "open-source"},
                "versions": {t: h["version"] for t, h in r["software"].items()
                             if h["license"] == "open-source" and h["version"]},
            }) + "\n")

    # ---------- data/paper_software.tsv ----------
    with open(os.path.join(OUT, "data", "paper_software.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["pmcid", "doi", "journal", "year", "package", "category",
                    "version", "in_methods", "pipeline_stages", "evidence_sentence"])
        for r in papers:
            for t, h in sorted(r["software"].items()):
                if h["license"] != "open-source":
                    continue
                w.writerow([r["pmcid"], r["doi"], r["journal"], r["year"], t,
                            h["category"], h["version"] or "", h["in_methods"],
                            "; ".join(h["steps"]),
                            h["evidence"][0].replace("\t", " ")])

    # ---------- per-package pages ----------
    for t, p in ranked:
        with open(os.path.join(OUT, "packages", slug(t) + ".md"), "w") as fh:
            fh.write("# %s\n\n" % t)
            fh.write("- **Category:** %s\n- **Papers in survey:** %d\n" % (p["cat"], len(p["papers"])))
            fh.write("- **Journals:** %s\n" % ", ".join("%s (%d)" % kv for kv in p["journals"].most_common()))
            fh.write("- **Years:** %s\n" % ", ".join("%s (%d)" % kv for kv in sorted(p["years"].items())))
            if p["versions"]:
                fh.write("- **Versions named:** %s\n" %
                         ", ".join("%s (%d)" % kv for kv in p["versions"].most_common(10)))
            if p["steps"]:
                fh.write("- **Pipeline stages it appears in:** %s\n" %
                         ", ".join("%s (%d)" % kv for kv in p["steps"].most_common()))
            fh.write("\n## Papers\n\n")
            for r in sorted(p["papers"], key=lambda r: (r["journal"], r["year"] or "")):
                pt, _ = pipeline_text(r)
                ev = r["software"][t]["evidence"][0]
                ver = r["software"][t]["version"]
                fh.write("### %s (%s %s)\n\n" % ((r["title"] or "").strip(), r["journal"], r["year"]))
                fh.write("- DOI: %s | PMCID: %s | PMID: %s\n" % (r["doi"], r["pmcid"], r["pmid"]))
                if ver:
                    fh.write("- Version used: **%s**\n" % ver)
                fh.write("- Evidence: %s\n" % ev)
                fh.write("- Full pipeline: %s\n\n" % (pt or "n/a"))
    print("wrote %d package pages" % len(ranked))
    return rows, papers, ranked, errs


if __name__ == "__main__":
    main()
