#!/usr/bin/env python3
"""Build the full survey deliverable: data files, package pages, README, gap list."""
import json, os, sys, csv, datetime
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_report as G
import software_db

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
G.OUT = OUT
os.makedirs(os.path.join(OUT, "data"), exist_ok=True)
os.makedirs(os.path.join(OUT, "packages"), exist_ok=True)

JOURNALS = ["Nature", "Science", "PNAS", "NEJM", "Lancet", "Cell"]
FULLNAME = {"Nature": "Nature", "Science": "Science",
            "PNAS": "PNAS", "NEJM": "New England J. of Medicine",
            "Lancet": "The Lancet", "Cell": "Cell"}
REASON = {"no_fulltext_xml": "indexed in Europe PMC but no full-text XML served (abstract/PDF-only deposit)",
          "no_body": "full-text XML has no usable body section",
          "parse_failed": "full-text XML could not be parsed",
          "network_error": "repeated network failure",
          "unknown": "unknown fetch failure"}


def tbl(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out) + "\n"


def main():
    rows, papers, ranked, errs = G.main()

    proc = {}
    for l in open(os.path.join(HERE, "process_in.jsonl")):
        r = json.loads(l)
        proc[r["pmcid"]] = r
    attempted = len(proc)

    # gap = never had a PMC record  +  had one but no usable full text
    gap = [(json.loads(l), "no open full text in Europe PMC")
           for l in open(os.path.join(HERE, "gap_list.jsonl"))]
    for line in open(os.path.join(HERE, "results.jsonl")):
        try:
            r = json.loads(line)
        except Exception:
            continue
        if "error" in r and r["pmcid"] in proc:
            gap.append((proc[r["pmcid"]], REASON.get(r["error"], r["error"])))

    with open(os.path.join(OUT, "data", "gap_list.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["pmid", "pmcid", "doi", "journal", "year", "title", "reason_not_readable"])
        for r, why in sorted(gap, key=lambda x: (x[0]["_journal"], x[0].get("pubYear") or "")):
            w.writerow([r.get("pmid"), r.get("pmcid", ""), r.get("doi"), r["_journal"],
                        r.get("pubYear"), (r.get("title") or "").replace("\t", " "), why])

    n_proc, n_hit, all_pkgs = len(rows), len(papers), len(ranked)
    total_mentions = sum(len(p["papers"]) for _, p in ranked)
    research_total = attempted + sum(1 for _ in open(os.path.join(HERE, "gap_list.jsonl")))
    nonresearch = 74928 - research_total

    jstat = defaultdict(lambda: [0, 0, 0])       # research, retrieved, with-oss
    for r, _ in gap:
        jstat[r["_journal"]][0] += 1
    for r in rows:
        jstat[r["journal"]][0] += 1
        jstat[r["journal"]][1] += 1
    for r in papers:
        jstat[r["journal"]][2] += 1

    cat = defaultdict(lambda: [0, 0])
    for t, p in ranked:
        cat[p["cat"]][0] += 1
        cat[p["cat"]][1] += len(p["papers"])

    seqs = Counter()
    for r in papers:
        _, stages = G.pipeline_text(r)
        key = " → ".join(s.split(" [")[0] for s in stages if not s.startswith("stage not"))
        if key:
            seqs[key] += 1

    disc = Counter()
    for r in rows:
        for g in (r.get("discovery", {}).get("github") or []):
            disc[g] += 1

    yr = Counter(r["year"] for r in papers)
    nver = sum(1 for r in papers for h in r["software"].values()
               if h["license"] == "open-source" and h["version"])

    R = []
    A = R.append
    A("# Open-source software in *Nature*, *Science*, *PNAS*, *NEJM*, *The Lancet* and *Cell*, 2021–2026\n")
    A("_Generated %s from the Europe PMC REST API. Reproducible with the scripts in `scripts/`._\n"
      % datetime.date.today().isoformat())

    A("## Read this first\n")
    A("The request behind this document was to read **every** paper published in these six journals\n"
      "over five years and record the open-source software each used. That is not achievable, and a\n"
      "document claiming to have done it would be untrustworthy. Two hard limits:\n")
    A("- **Volume.** These journals published **%s research articles** in 2021–2026 (plus ~%s\n"
      "  news, editorial, comment, letter and correction items, excluded here).\n"
      % (f"{research_total:,}", f"{nonresearch:,}"))
    A("- **Access.** Only **%s** of those (%.0f%%) have machine-readable full text. The rest are\n"
      "  paywalled or deposited abstract-only, so their Methods sections — where software is named —\n"
      "  cannot be read.\n"
      % (f"{n_proc:,}", 100.0 * n_proc / max(1, research_total)))
    A("What follows therefore covers **the %s research articles whose full text is openly readable**.\n"
      "Every row is extracted from the article's own text and carries a quotable evidence sentence, so\n"
      "each claim is checkable. The **%s articles that could not be read** are listed individually in\n"
      "`data/gap_list.tsv` — a stated blind spot, not a silent omission.\n"
      % (f"{n_proc:,}", f"{len(gap):,}"))

    A("\n### Coverage is very uneven by journal\n")
    A(tbl(["Journal", "Research articles", "Full text read", "Coverage", "≥1 OSS package"],
          [[FULLNAME[j], f"{jstat[j][0]:,}", f"{jstat[j][1]:,}",
            "%.0f%%" % (100.0 * jstat[j][1] / max(1, jstat[j][0])), f"{jstat[j][2]:,}"]
           for j in JOURNALS]))
    A("**This is the single most important caveat.** PNAS is fully open and supplies most of the\n"
      "corpus; NEJM, *The Lancet* and *Science* are largely closed. Absolute counts below reflect\n"
      "**what is readable, not what is used**. A package favoured in Lancet clinical trials will look\n"
      "rarer than one favoured in PNAS papers even if real-world use is identical. Compare packages\n"
      "within a journal, not across them.\n")

    A("\n## Headline numbers\n")
    A(tbl(["Metric", "Value"], [
        ["Research articles identified (2021–2026)", f"{research_total:,}"],
        ["Full text retrieved and parsed", f"{n_proc:,}"],
        ["Articles naming ≥1 open-source package", "%s (%.0f%% of those read)" % (f"{n_hit:,}", 100.0*n_hit/max(1,n_proc))],
        ["Distinct open-source packages detected", f"{all_pkgs:,}"],
        ["Total (paper × package) usage records", f"{total_mentions:,}"],
        ["Articles that could not be read (gap list)", f"{len(gap):,}"],
        ["Usage records with a version captured", "%s (%.0f%%)" % (f"{nver:,}", 100.0*nver/max(1,total_mentions))],
    ]))
    A("\nArticles using open-source software, by year: %s\n"
      % ", ".join("**%s** %s" % (y, f"{n:,}") for y, n in sorted(yr.items()) if y))

    A("\n## Most-used open-source packages\n")
    A(tbl(["#", "Package", "Domain", "Papers", "Versions most often named"],
          [[i+1, t, p["cat"], f"{len(p['papers']):,}",
            ", ".join(v for v, _ in p["versions"].most_common(3)) or "—"]
           for i, (t, p) in enumerate(ranked[:60])]))
    A("Complete ranking of all %d packages: `data/package_index.tsv`.\n" % all_pkgs)

    A("\n## By research domain\n")
    A(tbl(["Domain", "Distinct packages", "Usage records"],
          [[k, v[0], f"{v[1]:,}"] for k, v in sorted(cat.items(), key=lambda kv: -kv[1][1])]))

    A("\n## Most common analysis pipelines\n")
    A("Each tool's pipeline stage is inferred from the sentence that names it, then ordered\n"
      "canonically. The 25 most frequent stage sequences:\n")
    A(tbl(["Papers", "Pipeline stage sequence"], [[f"{n:,}", s] for s, n in seqs.most_common(25)]))
    A("Per-paper pipelines are in `data/papers.tsv` (`pipeline` column) and `data/pipelines.jsonl`.\n")

    neuro = [(t, p) for t, p in ranked if p["cat"] in ("neuroimaging", "neuro-tools")]
    if neuro:
        A("\n## Neuroimaging stack (relevance to this repository)\n")
        A("This survey was run in the AFNI repository, so neuroimaging tools are broken out. A bug in\n"
          "any of these would propagate to the papers listed on its package page.\n")
        A(tbl(["Package", "Papers", "Journals", "Versions named"],
              [[t, len(p["papers"]), ", ".join("%s (%d)" % kv for kv in p["journals"].most_common()),
                ", ".join(v for v, _ in p["versions"].most_common(4)) or "—"] for t, p in neuro]))

    if disc:
        A("\n## Discovery signals: packages outside the dictionary\n")
        A("Most-cited GitHub repositories in the corpus. These are candidates for extending the\n"
          "dictionary — detection is dictionary-bounded, so this is where its blind spots show.\n")
        A(tbl(["GitHub repository", "Papers"], [[k, v] for k, v in disc.most_common(40)]))

    # independent cross-check against Europe PMC's own full-text search
    xc = os.path.join(HERE, "epmc_crosscheck.txt")
    if os.path.exists(xc):
        pk = {t: len(p["papers"]) for t, p in ranked}
        lines = [l.split() for l in open(xc).read().splitlines()[1:] if l.strip()]
        rowsx = []
        for name, hits in [(a, b) for a, b in lines if b.isdigit()]:
            mine = pk.get(name)
            if mine is None:
                continue
            rowsx.append([name, f"{mine:,}", f"{int(hits):,}",
                          "%.2f" % (mine / int(hits)) if int(hits) else "—"])
        if rowsx:
            A("\n## Cross-check against an independent source\n")
            A("Europe PMC's own full-text search over the same six journals and years, compared with\n"
              "this survey's counts. The two measure different things: EPMC searches the **whole**\n"
              "article including its reference list, so a paper that merely *cites* a tool counts\n"
              "there but not here. EPMC also searches articles this survey could not parse. Its\n"
              "numbers are therefore an upper bound, and a ratio below 1 is expected and healthy —\n"
              "a ratio near or above 1 would suggest this survey is over-counting.\n")
            A(tbl(["Package", "This survey", "EPMC full-text hits", "Ratio"], rowsx))

    A("\n## Files\n")
    A(tbl(["File", "Contents"], [
        ["`data/papers.tsv`", "One row per paper: identifiers, packages used, full pipeline string"],
        ["`data/paper_software.tsv`", "One row per (paper × package): version, stage, **evidence sentence**"],
        ["`data/package_index.tsv`", "One row per package: paper count, journals, versions, typical stages"],
        ["`data/pipelines.jsonl`", "Per-paper pipeline stages and per-package evidence, machine-readable"],
        ["`data/gap_list.tsv`", "Every research article that could not be read, with the reason"],
        ["`packages/<name>.md`", "Per-package page: every paper using it, with version and pipeline"],
        ["`scripts/`", "The harvest, extraction and report code, to re-run or extend the survey"],
    ]))
    A("\n**For the next step (finding bugs that affect these papers), start at\n"
      "`packages/<name>.md`.** It gives, per package, the papers at risk and the **specific version\n"
      "each reported**, so a bug can be matched against the version range actually used.\n")

    A("\n## Method\n")
    A("1. **Corpus.** Europe PMC queried by **ISSN** for the six journals, 2021–2026, so sibling\n"
      "   titles (*Nature Communications*, *Science Advances*, *Cell Reports*) are excluded — a\n"
      "   journal-name search would have pulled them in.\n"
      "2. **Filtering.** News, editorials, comments, letters and corrections removed by publication\n"
      "   type and title pattern, leaving research articles.\n"
      "3. **Full text.** `fullTextXML` fetched per article and parsed as XML (not regexed over raw\n"
      "   markup); Methods located by section title and `sec-type`.\n"
      "4. **Detection.** A curated dictionary of **%d packages (%d name variants)** across 13 domains.\n"
      "   Names colliding with ordinary language require a disambiguating context match: `STAR` must\n"
      "   look like the aligner rather than *Cell*'s “STAR Methods”; `MUSCLE` the aligner, not tissue;\n"
      "   `Fiji` the image suite, not the country; `Salmon` the quantifier, not the fish; `R` must\n"
      "   appear with a version or an `R Core Team` citation. Detection runs over Methods first, then\n"
      "   the rest of the body, because tools are also named in figure legends and data-availability\n"
      "   statements.\n"
      "5. **Pipelines.** The sentence naming each tool is classified into analysis stages (quality\n"
      "   control, trimming, alignment, variant calling, quantification, normalisation, registration,\n"
      "   clustering, statistical testing, simulation, structure determination, machine learning,\n"
      "   visualisation) and ordered canonically.\n"
      "6. **Licence.** Proprietary tools (MATLAB, Imaris, VASP and similar) are detected but excluded\n"
      "   from open-source counts and never reported as OSS.\n"
      % (len(software_db.SAFE), sum(len(v[1]) for v in software_db.SAFE.values())))

    A("\n## Limitations\n")
    A("- **%s research articles could not be read** (`data/gap_list.tsv`). Roughly a third of these\n"
      "  are indexed in Europe PMC but serve no full-text XML; the rest are paywalled outright.\n" % f"{len(gap):,}")
    A("- **Detection is dictionary-bounded.** Packages not in the dictionary are missed. GitHub,\n"
      "  Zenodo, CRAN, Bioconductor and RRID signals are captured to expose that tail, but a survey\n"
      "  of one-off custom tools this is not.\n")
    A("- **Supplementary methods are not fetched.** Many papers put full Methods in a PDF supplement\n"
      "  outside the JATS body; tools named only there are missed.\n")
    A("- **Stage classification is heuristic.** It reads the one sentence naming the tool, so a tool\n"
      "  described across several sentences may get an incomplete stage list. The evidence sentence\n"
      "  is included in every row precisely so this can be audited.\n")
    A("- **Presence ≠ dependence.** A named package may have produced one supplementary figure rather\n"
      "  than the central result. Read the evidence sentence before concluding a bug matters.\n")
    A("- **Some names denote a method or a database as often as a program.** UMAP, GSEA and\n"
      "  AlphaFold are recorded whenever named, but a paper may mean the algorithm, a published\n"
      "  embedding, or the AlphaFold Protein Structure Database rather than a run of the software.\n"
      "  AlphaFold is the one package whose cross-check ratio exceeds 1, which is the signature of\n"
      "  exactly this effect — treat its count as an upper bound.\n")
    A("- **A version is recorded only when it is stated adjacent to the package name** —\n"
      "  `STAR (v2.7.5c)`, `Seurat v5.0.1`, `R version 4.1.2`. Where a paper separates the two\n"
      "  (`AFNI, http://... ) software (v.23.1.06)`) the version field is left empty rather than\n"
      "  guessed, because binding the wrong number would mismatch a bug's affected range in the\n"
      "  next step. %d%% of usage records carry a version; for the rest, the evidence sentence is\n"
      "  in `data/paper_software.tsv` and often contains it.\n"
      % round(100.0*nver/max(1,total_mentions)))
    A("- **Counts are of papers, not of runs.** A paper naming a package once and a paper built\n"
      "  entirely on it both count as 1.\n")

    with open(os.path.join(OUT, "README.md"), "w") as fh:
        fh.write("\n".join(R))
    print("README written | corpus=%d parsed=%d hits=%d pkgs=%d gap=%d"
          % (attempted, n_proc, n_hit, all_pkgs, len(gap)))


if __name__ == "__main__":
    main()
