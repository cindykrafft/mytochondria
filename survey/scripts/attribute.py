#!/usr/bin/env python3
"""Attribute each audited package's survey papers to the repository the audit targets.

The survey records a package whenever a paper names it. For most packages the name is the
program (STAR, samtools, Trimmomatic), so every paper is attributable to the audited
repository. For two audited packages the name is a method that several programs implement:

  GSEA   -> GSEA-MSigDB/gsea-desktop (the Broad/UCSD program), but also fgsea, clusterProfiler,
            GSEApy, GSVA/ssGSEA and web tools
  UMAP   -> lmcinnes/umap (umap-learn), but Seurat's RunUMAP, Monocle, ArchR and Signac run uwot

For those, each paper is classed from its evidence sentences (the package's own sentence and
every other sentence the survey kept for that paper) and from the other packages the survey
recorded for it:

  repo     the target implementation is named (program name, URL, a version only it has),
           or a co-named package is known to call it
  other    another implementation is named and the target is not
  name     only the method name

Independently, every version a paper states next to the package name is checked against the
release tags of the target repository (survey/data/repo_tags/<owner>_<repo>.txt, from
`git ls-remote --tags`), so versions whose code never lived in that repository (javaGSEA 2.x,
PLINK 1.07, IQ-TREE 1.6 in the iqtree3 repository) are visible.

Writes survey/data/attribution.tsv, prints a Markdown table, and with --write-site updates the
`attributed` fields in site/audits.json.
"""
import csv, json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
TSV = os.path.join(ROOT, "survey", "data", "paper_software.tsv")
TAGS = os.path.join(ROOT, "survey", "data", "repo_tags")
AUDITS = os.path.join(ROOT, "site", "audits.json")
OUT = os.path.join(ROOT, "survey", "data", "attribution.tsv")

# audit dir -> survey package name(s), target repo for tags, and (method-named only) the markers.
# `own` / `rival` are regexes on the paper's evidence text, `own_local` on the package's own sentence only; `own_pkgs` / `rival_pkgs` are packages the survey
# recorded for the same paper. `versioned_is_own`: a stated version identifies the target program.
PKG = {
    "freesurfer": dict(survey=["FreeSurfer"], repo="freesurfer/freesurfer"),
    "fsl": dict(survey=["FSL"], repo=None),
    "spm": dict(survey=["SPM"], repo="spm/spm"),
    "afni": dict(survey=["AFNI"], repo="afni/afni"),
    "deseq2": dict(survey=["DESeq2"], repo="thelovelab/DESeq2"),
    "macs2": dict(survey=["MACS2"], repo="macs3-project/MACS"),
    "kilosort": dict(survey=["Kilosort"], repo="MouseLand/Kilosort"),
    "fieldtrip": dict(survey=["FieldTrip"], repo="fieldtrip/fieldtrip"),
    "suite2p": dict(survey=["Suite2p"], repo="MouseLand/suite2p"),
    "seurat": dict(survey=["Seurat"], repo="satijalab/seurat"),
    "scanpy": dict(survey=["Scanpy"], repo="scverse/scanpy"),
    "scrublet": dict(survey=[], repo="swolock/scrublet", papers_override=78,
                     note="the survey files doublet tools under one scDblFinder alias group; the audit counted the 78 papers whose evidence names Scrublet, and the name is the program"),
    "cellphonedb": dict(survey=["CellPhoneDB"], repo="ventolab/CellphoneDB"),
    "umap": dict(survey=["UMAP"], repo="lmcinnes/umap", kind="method",
                 own=r"umap-learn|umap\.umap_|umap\.UMAP|\bsc\.tl\.umap|scanpy|flowjo", own_pkgs=["Scanpy"], own_local=r"python",
                 rival=r"\buwot\b|RunUMAP|monocle|archr|signac|seurat", rival_pkgs=["Seurat", "Monocle", "ArchR", "Signac"],
                 rival_name="uwot (Seurat, Monocle, ArchR, Signac)"),
    "cutadapt": dict(survey=["Cutadapt"], repo="marcelm/cutadapt"),
    "deeptools": dict(survey=["deepTools"], repo="deeptools/deepTools"),
    "iqtree": dict(survey=["IQ-TREE"], repo="iqtree/iqtree3"),
    "fastp": dict(survey=["fastp"], repo="OpenGene/fastp"),
    "bedtools": dict(survey=["BEDTools"], repo="arq5x/bedtools2"),
    "htseq": dict(survey=["HTSeq"], repo="htseq/htseq"),
    "plink": dict(survey=["PLINK"], repo="chrchang/plink-ng"),
    "samtools": dict(survey=["SAMtools"], repo="samtools/samtools"),
    "featurecounts": dict(survey=["featureCounts"], repo="ShiLab-Bioinformatics/subread"),
    "edger": dict(survey=["edgeR"], repo=None),
    "lme4": dict(survey=["lme4"], repo="lme4/lme4"),
    "clusterprofiler": dict(survey=["clusterProfiler"], repo="YuLab-SMU/clusterProfiler"),
    "star": dict(survey=["STAR"], repo="alexdobin/STAR"),
    "bcftools": dict(survey=["BCFtools"], repo="samtools/bcftools"),
    "gsea": dict(survey=["GSEA"], repo="GSEA-MSigDB/gsea-desktop", kind="method",
                 own=r"gsea(?:(?!msigdb)[^.;]){0,50}\bbroad\b|broad(?: institute)?(?:'s)? gsea|gsea-msigdb\.org/gsea(?!/msigdb)|"
                     r"software\.broadinstitute\.org/gsea|genepattern|javagsea|gsea ?desktop|gsea ?software|gsea ?application|gsea ?preranked|"
                     r"gseapreranked|xtools\.gsea|gsea[ _]?v?\.? ?[234]\.\d|gsea ?(?:version|ver\.?) ?[234]",
                 own_pkgs=[], versioned_is_own=True, own_local=r"\bdesktop\b|\bjava\b",
                 rival=r"\bfgsea\b|clusterprofiler|\bgse(?:GO|KEGG|Pathway|DO|MKEGG|WP)\b|gseapy|\bgsva\b|ssgsea|"
                       r"enrichr|webgestalt|metascape|g:profiler|\bpiano\b|ingenuity|\bIPA\b|camera\(|\bcamera\b|"
                       r"\bromer\b|\bfry\b|liger|\bgage\b|\bdecoupler|\bpathfindR|\bgsea\(|escape\b",
                 rival_pkgs=["fgsea", "clusterProfiler", "GSVA", "Enrichr", "Metascape"],
                 rival_name="fgsea, clusterProfiler, GSVA/ssGSEA, GSEApy, web tools"),
    "limma": dict(survey=["limma"], repo=None),
    "trimmomatic": dict(survey=["Trimmomatic"], repo="usadellab/Trimmomatic"),
}

PREFIX = re.compile(r"^(?:v\.?|release[_-]|STAR_|AFNI_|a|b)", re.I)


def norm(v):
    v = PREFIX.sub("", v.strip()).replace("-", ".").replace("_", ".")
    return v.lower()


def load_tags(repo):
    if not repo:
        return None
    p = os.path.join(TAGS, repo.replace("/", "_") + ".txt")
    if not os.path.exists(p):
        return None
    tags = {norm(t) for t in open(p).read().split() if re.search(r"\d", t)}
    tags = {t for t in tags if re.match(r"\d", t)}
    return tags if len(tags) >= 5 else None   # a repository with a handful of tags does not tag releases


def version_in_tags(v, tags):
    """A stated version is in the repository when it equals a tag, or is a prefix of one that the
    tag then extends with a letter, a dot or (for at least three characters, e.g. "1.9" -> "1.90b6")
    further digits: STAR tags "2.7.0a", MACS "2.1.1.20160309", PLINK "1.90b6.9"."""
    n = norm(v)
    if n in tags:
        return True
    if len(n) < 3:
        return False
    return any(t.startswith(n) and (not t[len(n)].isdigit() or n[-1].isalpha() or n.count(".") < 2) for t in tags if len(t) > len(n))


def main():
    rows = list(csv.DictReader(open(TSV), delimiter="\t"))
    by_paper = collections.defaultdict(list)
    for r in rows:
        by_paper[r["pmcid"]].append(r)
    audits = json.load(open(AUDITS))
    order = [a["dir"] for a in audits["audits"]]
    out = []
    for d in order:
        cfg = PKG[d]
        prs = [r for r in rows if r["package"] in cfg["survey"]]
        n = cfg.get("papers_override", len(prs))
        rec = dict(audit=d, package="/".join(cfg["survey"]) or "-", repo=cfg["repo"] or "-", papers=n,
                   repo_named=n, other=0, name_only=0, other_name="", versions=0, tag_hits=0, outside="", note=cfg.get("note", ""))
        if cfg.get("kind") == "method":
            own_re, rival_re = re.compile(cfg["own"], re.I), re.compile(cfg["rival"], re.I)
            c = collections.Counter()
            for r in prs:
                paper = by_paper[r["pmcid"]]
                text = " ".join(x["evidence_sentence"] for x in paper)
                pkgs = {x["package"] for x in paper}
                own = own_re.search(text) or (pkgs & set(cfg["own_pkgs"])) or (cfg.get("versioned_is_own") and r["version"]) \
                    or (cfg.get("own_local") and re.search(cfg["own_local"], r["evidence_sentence"], re.I))
                rival = rival_re.search(text) or (pkgs & set(cfg["rival_pkgs"]))
                c["repo" if own else "other" if rival else "name"] += 1
            rec.update(repo_named=c["repo"], other=c["other"], name_only=c["name"], other_name=cfg["rival_name"])
        tags = load_tags(cfg["repo"])
        vs = [r["version"] for r in prs if r["version"]]
        rec["versions"] = len(vs)
        if tags:
            hits = [v for v in vs if version_in_tags(v, tags)]
            rec["tag_hits"] = len(hits)
            miss = collections.Counter(v for v in vs if not version_in_tags(v, tags))
            rec["outside"] = ", ".join(f"{v}×{k}" if k > 1 else v for v, k in miss.most_common(8))
        else:
            rec["tag_hits"] = ""
            rec["outside"] = "(no version tags in the repository)" if cfg["repo"] else "(no repository)"
        out.append(rec)

    with open(OUT, "w") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(out)

    print("| audit | survey package | target repository | papers | attributable to the repository | another implementation | name only | versions stated | matching a release tag | stated versions with no release tag |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r in out:
        att = f"{r['repo_named']}" if r["papers"] else "–"
        oth = f"{r['other']} ({r['other_name']})" if r["other"] else ("–" if not r["papers"] else "0")
        print(f"| {r['audit']} | {r['package']} | {r['repo']} | {r['papers'] or '–'} | {att} | {oth} | {r['name_only'] if r['papers'] else '–'} | "
              f"{r['versions']} | {r['tag_hits'] if r['tag_hits'] != '' else '–'} | {r['outside'] or '—'} |")

    if "--write-site" in sys.argv:
        recs = {r["audit"]: r for r in out}
        for a in audits["audits"]:
            r = recs[a["dir"]]
            if PKG[a["dir"]].get("kind") == "method":
                a["attributed"] = r["repo_named"]
                a["attributed_note"] = (f"{r['repo_named']} papers name the program or a package that calls it, "
                                        f"{r['other']} name another implementation ({r['other_name']}), {r['name_only']} name only the method")
            else:
                a["attributed"] = r["papers"] if r["papers"] else None
            if r["tag_hits"] != "":
                a["versions_stated"], a["versions_in_repo"] = r["versions"], r["tag_hits"]
        json.dump(audits, open(AUDITS, "w"), indent=1)
        open(AUDITS, "a").write("\n")


if __name__ == "__main__":
    main()
