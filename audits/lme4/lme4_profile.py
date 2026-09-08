#!/usr/bin/env python3
"""Profile how each cohort paper used lme4.

Mines the text for the choices that select lme4 code paths: lmer vs glmer,
REML vs ML, the GLMM family and link, random slopes / nested / crossed
designs, how p-values and intervals were obtained (lmerTest / Satterthwaite /
Kenward-Roger / likelihood-ratio / bootstrap / profile / Wald), post-hoc
tools (emmeans), model selection (AIC/BIC/anova), convergence and singularity
handling, optimizer choices, nAGQ, and the stated lme4 version.
One JSONL record per paper.

Usage: python3 lme4_profile.py            (fetch full texts, cache fallback)
       python3 lme4_profile.py --offline  (survey cache only, no network)

Two sources, recorded per paper in `source`:

  "fulltext"     the JATS body from Europe PMC (the normal path, as in the
                 other audits' *_profile.py scripts);
  "survey_cache" fallback when the full text cannot be fetched: the survey's
                 stored evidence for the paper -- the lme4 evidence sentence
                 in paper_software.tsv plus every per-package evidence
                 snippet in pipelines.jsonl.gz. A few hundred characters per
                 package, so feature counts from this source are LOWER
                 BOUNDS on usage, not measurements of it.

As for the Seurat and Scanpy audits, the 2026-09-08 run had no route to
Europe PMC (www.ebi.ac.uk denied by the session's egress policy; NCBI
likewise), so every record in lme4_profiles.jsonl is source=survey_cache.
Rerun from a host with Europe PMC access to replace them; the fetch path is
unchanged from the other audits.
Version regexes require a word boundary after "lme4".
"""
import csv, gzip, json, re, sys, xml.etree.ElementTree as ET
import concurrent.futures as cf
from collections import Counter

sys.path.insert(0, "../../survey/scripts")
import extract as E

FEATURES = {
 "lmer named":                          r"\blmer\b|linear mixed[- ]effects? model|linear mixed model|\bLMM\b|\bLMMs\b",
 "glmer named":                         r"\bglmer\b|generali[sz]ed linear mixed[- ]?(?:effects? )?model|\bGLMM\b|\bGLMMs\b",
 "glmer.nb / negative binomial":        r"glmer\.nb|negative[- ]binomial",
 "binomial / logistic family":          r"binomial|logistic (?:mixed|regression|model)|logit link",
 "poisson family":                      r"poisson",
 "gamma family":                        r"\bGamma\b|gamma (?:distribution|family|GLMM)",
 "REML stated":                         r"\bREML\b|restricted maximum likelihood",
 "ML stated":                           r"REML\s*=\s*FALSE|maximum likelihood",
 "random slope":                        r"random slopes?|by-(?:subject|participant|item) slopes?|\(\s*1\s*\+\s*[A-Za-z_.]+\s*\|",
 "random intercept only":               r"random intercepts?|\(\s*1\s*\|",
 "nested design":                       r"nested|\|\s*[A-Za-z_.]+\s*/\s*[A-Za-z_.]+\s*\)",
 "crossed random effects":              r"crossed random",
 "maximal random structure":            r"maximal random[- ]effects? structure|Barr et al",
 "lmerTest / Satterthwaite":            r"lmerTest|Satterthwaite",
 "Kenward-Roger / pbkrtest":            r"Kenward[- ]Roger|pbkrtest",
 "likelihood-ratio test / anova":       r"likelihood[- ]ratio|\bLRT\b|\banova\(",
 "AIC / BIC model selection":           r"\bAIC\b|\bBIC\b|Akaike",
 "emmeans / post hoc":                  r"emmeans|lsmeans|post[- ]hoc|Tukey",
 "confint / profile / Wald":            r"confint|profile (?:likelihood|confidence)|Wald",
 "bootstrap / bootMer":                 r"bootMer|bootstrap",
 "p-values reported":                   r"\bp\s*[<=]\s*0?\.\d+|p-?values?",
 "convergence / singular handling":     r"converge|singular fit|is ?Singular|boundary",
 "optimizer stated (bobyqa/NM/allFit)": r"bobyqa|Nelder[- ]Mead|nloptwrap|allFit|optimizer",
 "nAGQ stated":                         r"nAGQ|Gauss[- ]Hermite|quadrature|Laplace",
 "predict / simulate":                  r"\bpredict\(|simulate\(|re\.form",
 "R2 (MuMIn / r.squaredGLMM / performance)": r"MuMIn|r\.squaredGLMM|marginal R|conditional R|performance::",
 "glmmTMB also used":                   r"glmmTMB",
 "nlme also used":                      r"\bnlme\b|\blme\(",
 "afex / mixed()":                      r"\bafex\b|mixed\(",
 "brms / Bayesian alternative":         r"\bbrms\b|rstanarm|MCMCglmm|blme",
 "sjPlot / broom.mixed / DHARMa":       r"sjPlot|broom\.mixed|DHARMa",
 "lme4 version stated":                 r"lme4(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?\d+\.\d+",
 "repeated measures / longitudinal":    r"repeated[- ]measures|longitudinal",
 "subject / participant random effect": r"(?:subject|participant|animal|mouse|mice|individual)s?\s*(?:as|was|were)?\s*(?:a |the )?random",
 "trial / item random effect":          r"\b(?:item|trial|session|plot|site|litter|cage|batch)s?\s*(?:as|was|were)?\s*(?:a |the )?random",
}
CI = {"binomial / logistic family", "poisson family", "REML stated", "random slope",
      "random intercept only", "nested design", "crossed random effects",
      "maximal random structure", "likelihood-ratio test / anova", "emmeans / post hoc",
      "confint / profile / Wald", "bootstrap / bootMer", "p-values reported",
      "convergence / singular handling", "optimizer stated (bobyqa/NM/allFit)",
      "nAGQ stated", "R2 (MuMIn / r.squaredGLMM / performance)",
      "repeated measures / longitudinal", "subject / participant random effect",
      "trial / item random effect"}
FEATURES = {k: re.compile(v, re.I if k in CI else 0) for k, v in FEATURES.items()}

VER   = re.compile(r"lme4(?![A-Za-z])[^.;(]{0,25}?(?:v(?:ersion)?\.?\s*)?(\d+\.\d+(?:[.-]\d+)*)")
FAM   = re.compile(r"family\s*=\s*\"?([A-Za-z.]+)", re.I)
PADJ  = re.compile(r"(?:adjusted\s+[pP]|[pP]\s*adj|padj|FDR|[qQ][- ]?value|Bonferroni|Holm)[^.;]{0,25}?[<≤]\s*(0\.\d+)")
ALPHA = re.compile(r"\bp\s*[<≤]\s*(0?\.0[0-9]+|0?\.05)\b")
KWIN  = re.compile(r"lme4(?![A-Za-z])")

def family(v):
    m = re.match(r"(\d+)\.(\d+)", v)
    if not m: return None
    major, minor = int(m.group(1)), int(m.group(2))
    if major not in (1, 2): return None      # lme4 has had 1.x and (since 2026) 2.x releases
    return "%d.%d" % (major, minor)

def mine(c, text, source):
    feats = sorted(k for k, rx in FEATURES.items() if rx.search(text))
    vers  = set(VER.findall(text))
    if c.get("version_survey"):           # the survey's own full-text extraction
        vers.add(c["version_survey"])
    vers  = sorted(vers)
    fams  = sorted({f for f in (family(v) for v in vers) if f})
    c.update({
        "source": source,
        "features": feats,
        "versions_all": vers,
        "version_family": fams,
        "glm_families": sorted({f.lower() for f in FAM.findall(text)}),
        "padj_cutoffs": sorted(set(PADJ.findall(text))),
        "alpha_stated": sorted(set(ALPHA.findall(text))),
    })
    if source == "fulltext":
        ctx = []
        for m in KWIN.finditer(text):
            lo = max(0, m.start()-260); hi = min(len(text), m.end()+320)
            ctx.append(("..."+text[lo:hi]+"...").strip())
            if len(ctx) >= 3: break
        c["context"] = ctx
    return c

OFFLINE = "--offline" in sys.argv[1:]

def profile(c):
    raw, why = (None, "offline") if OFFLINE else E.fetch(c["pmcid"])
    if raw:
        try:
            root = ET.fromstring(raw)
            E._strip_refs(root)
            body = root.find(".//body")
            text = re.sub(r"\s+", " ", " ".join(body.itertext())) if body is not None else ""
            if text:
                return mine(c, text, "fulltext")
            why = "empty_body"
        except Exception:
            why = "parse"
    c["profile_error"] = why
    return mine(c, c.pop("_cache_text"), "survey_cache")

cohort, by_pmcid = [], {}
with open("../../survey/data/paper_software.tsv") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["package"] == "lme4":
            rec = {"pmcid": row["pmcid"], "doi": row["doi"],
                   "journal": row["journal"], "year": row["year"],
                   "version_survey": row["version"],
                   "in_methods": row["in_methods"] == "True",
                   "pipeline_stages_survey": row["pipeline_stages"],
                   "evidence_survey": row["evidence_sentence"],
                   "_cache_text": row["evidence_sentence"]}
            cohort.append(rec); by_pmcid[row["pmcid"]] = rec
with gzip.open("../../survey/data/pipelines.jsonl.gz", "rt") as fh:
    for line in fh:
        d = json.loads(line)
        rec = by_pmcid.get(d["pmcid"])
        if rec is None: continue
        rec["title"] = d.get("title", "")
        rec["co_packages"] = sorted(p for p in d["packages"] if p != "lme4")
        # Evidence snippets only (the pipeline_stages strings put other
        # packages' versions within a few characters of "lme4").
        rec["_cache_text"] = " ".join([rec["_cache_text"]] + list(d["evidence"].values()))
print("cohort:", len(cohort))
with cf.ThreadPoolExecutor(10) as ex:
    out = list(ex.map(profile, cohort))
with open("lme4_profiles.jsonl", "w") as fh:
    for c in out: fh.write(json.dumps(c)+"\n")
full  = [c for c in out if c["source"] == "fulltext"]
cache = [c for c in out if c["source"] == "survey_cache"]
print("full text: %d   survey-cache fallback: %d   (%s)" % (
    len(full), len(cache), dict(Counter(c.get("profile_error") for c in cache))))
fc, vc, fam, co, gf, padj, alpha, jr, yr = (Counter() for _ in range(9))
for c in out:
    for f in c["features"]: fc[f] += 1
    for v in c["versions_all"]: vc[v] += 1
    for f in c["version_family"]: fam[f] += 1
    for p in c.get("co_packages", []): co[p] += 1
    for f in c["glm_families"]: gf[f] += 1
    for p in c["padj_cutoffs"]: padj[p] += 1
    for a in c["alpha_stated"]: alpha[a] += 1
    jr[c["journal"]] += 1; yr[c["year"]] += 1
print("\nJOURNALS:", dict(jr.most_common()))
print("YEARS:", dict(sorted(yr.items())))
print("in_methods:", sum(c["in_methods"] for c in out))
print("\nFEATURES (papers; lower bounds where source=survey_cache):")
for k, n in fc.most_common(): print("  %-48s %d" % (k, n))
print("\nVERSION FAMILY:", dict(fam.most_common()))
print("VERSIONS (top 20):", dict(vc.most_common(20)))
print("\nfamily= strings:", dict(gf.most_common(10)))
print("padj cutoffs:", dict(padj.most_common(8)))
print("alpha stated:", dict(alpha.most_common(8)))
print("\nCO-PACKAGES (top 40):")
for k, n in co.most_common(40): print("  %-24s %d" % (k, n))
