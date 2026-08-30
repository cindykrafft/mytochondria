#!/usr/bin/env python3
"""Fetch Europe PMC full text and extract software usage + pipeline evidence."""
import json, os, re, sys, time, urllib.error, urllib.request, xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from software_db import SAFE, AMBIGUOUS, DISCOVERY, PROPRIETARY

FT = "https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML"

# --- compile matchers -------------------------------------------------------
def _alt(aliases):
    pats = []
    for a in sorted(aliases, key=len, reverse=True):
        e = re.escape(a)
        # word boundary only where the alias edge is alphanumeric
        pre = r"(?<![A-Za-z0-9])" if a[0].isalnum() else ""
        suf = r"(?![A-Za-z0-9])" if a[-1].isalnum() else ""
        pats.append(pre + e + suf)
    return re.compile("|".join(pats))

# Compile one regex per package, but gate each behind a plain substring test.
# `lit in text` is a C-level fast search; running 288 of those and then only the
# handful of regexes whose literal actually appears is far cheaper than either
# 288 regex passes or one giant alternation (Python's re backtracks alternations
# position by position, so a 288-way alternation is slower, not faster).
SAFE_RE = {n: (_alt(al), cat, tuple(al)) for n, (cat, al) in SAFE.items()}
AMB_RE = {n: (re.compile(v[1]), re.compile(v[2]) if v[2] else None, v[0])
          for n, v in AMBIGUOUS.items()}
DISC_RE = {k: re.compile(v) for k, v in DISCOVERY.items()}
# The version must follow the package name immediately, separated only by
# space/comma/paren and an optional "v"/"version". A loose window search binds
# the wrong number: in "R package DESeq2 (v1.26.0)" the 1.26.0 is DESeq2's.
VERSION_AFTER = re.compile(
    r"^[\s,]*\(?\s*(?:v|ver|version|release)?\.?\s*(\d+\.\d+(?:\.\d+)*[A-Za-z]?)")
# For context-matched ambiguous names the version is inside the matched span.
VERSION_IN = re.compile(r"(\d+\.\d+(?:\.\d+)*[A-Za-z]?)")

METHODS_TITLE = re.compile(
    r"method|material|experimental procedure|star\s*.?\s*method|"
    r"data analysis|statistical analysis|analysis|procedure|protocol", re.I)

STEPS = [
 ("quality control",   r"quality control|quality[- ]check|QC\b|FastQC|MultiQC|contaminat"),
 ("read trimming",     r"trimm|adapter|demultiplex|deduplicat|filter(?:ed|ing) (?:reads|low)"),
 ("alignment/mapping", r"\balign|\bmapp?(?:ed|ing)\b|reference genome|pseudoalign"),
 ("variant calling",   r"variant call|genotyp|SNP call|haplotype"),
 ("quantification",    r"quantif|read count|expression matrix|TPM|FPKM|RPKM|abundance"),
 ("normalisation",     r"normali[sz]|batch (?:effect|correct)|scal(?:ed|ing)|regress out"),
 ("registration",      r"registrat|normali[sz]ed to (?:MNI|standard)|skull[- ]strip|"
                       r"motion correct|slice[- ]tim|spatial smooth|template space|realign"),
 ("dimensionality reduction/clustering",
                       r"cluster|principal component|\bPCA\b|\bUMAP\b|t-SNE|tSNE|dimensional"),
 ("differential/statistical testing",
                       r"differential|statistic|regression|linear model|mixed[- ]effect|"
                       r"p[- ]?value|FDR|false discovery|Bonferroni|permutation|Bayesian|hypothesis"),
 ("simulation/modelling", r"simulat|molecular dynamics|force field|trajector|Monte Carlo"),
 ("structure determination", r"refine|structure determination|density map|reconstruct|resolution estimat"),
 ("machine learning",  r"train(?:ed|ing)|neural network|deep learning|classifier|cross[- ]validat"),
 ("visualisation",     r"visuali[sz]|plotted|rendered|figures were"),
]
STEPS = [(n, re.compile(p, re.I)) for n, p in STEPS]

SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(])")


def text_of(el):
    return " ".join(el.itertext())


def clean(s):
    return re.sub(r"\s+", " ", s).strip()


def fetch(pmcid, tries=4):
    """Return (bytes, None) or (None, reason).

    A 404 here is permanent, not a blip: Europe PMC flags these records as
    `inEPMC=Y` but serves no JATS body for them (abstract- or PDF-only
    deposits). Retrying one costs ~5s of pure sleeping, so treat it as a
    definitive 'no full text' and move the paper to the gap list.
    """
    for a in range(tries):
        try:
            req = urllib.request.Request(FT % pmcid,
                                         headers={"User-Agent": "software-survey/1.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read(), None
        except urllib.error.HTTPError as e:
            if e.code in (400, 403, 404, 410):
                return None, "no_fulltext_xml"
            if a == tries - 1:
                return None, "http_%d" % e.code
        except Exception:
            if a == tries - 1:
                return None, "network_error"
        time.sleep(1.5 ** a)
    return None, "unknown"


def sections(root):
    """Return (full_body_text, methods_text)."""
    body = root.find(".//body")
    if body is None:
        return "", ""
    full = clean(text_of(body))
    meth = []
    for sec in body.iter("sec"):
        t = sec.find("title")
        if t is not None and METHODS_TITLE.search(clean(text_of(t)) or ""):
            meth.append(clean(text_of(sec)))
    if not meth:
        # Cell/Nature often put methods in a back-matter <sec sec-type="methods">
        for sec in root.iter("sec"):
            if (sec.get("sec-type") or "").lower().find("method") >= 0:
                meth.append(clean(text_of(sec)))
    return full, clean(" ".join(meth)) or full


def detect(text):
    """Dictionary names (prefiltered), plus context-guarded ambiguous names."""
    hits = {}
    for name, (rx, cat, lits) in SAFE_RE.items():
        for lit in lits:
            if lit in text:
                break
        else:
            continue
        m = rx.search(text)
        if m:
            hits[name] = {"category": cat, "pos": m.start(), "end": m.end(),
                          "match": m.group(0), "amb": False}
    for name, (ctx, neg, cat) in AMB_RE.items():
        for m in ctx.finditer(text):
            if neg and neg.search(text, max(0, m.start() - 20), m.end() + 20):
                continue
            hits[name] = {"category": cat, "pos": m.start(), "end": m.end(),
                          "match": m.group(0), "amb": True}
            break
    return hits


def evidence(text, hits):
    """Pull the sentence around each hit from a local window (cheap)."""
    for name, h in hits.items():
        p = h["pos"]
        lo, hi = max(0, p - 400), min(len(text), p + 500)
        win, rel = text[lo:hi], p - lo
        parts, off, sent = SENT.split(win), 0, win
        for frag in parts:
            if off <= rel < off + len(frag) + 1:
                sent = frag
                break
            off += len(frag) + 1
        sent = clean(sent)
        # keep the mention visible rather than truncating blindly from the start
        where = sent.find(h["match"][:24])
        if len(sent) > 400 and where > 250:
            st = where - 150
            sent = "..." + sent[st:st + 400] + ("..." if st + 400 < len(sent) else "")
        else:
            sent = sent[:400] + ("..." if len(sent) > 400 else "")
        ev = [sent]
        h["evidence"] = ev
        if h.get("amb"):
            vm = VERSION_IN.search(h["match"])
        else:
            vm = VERSION_AFTER.match(text[h["end"]:h["end"] + 32])
        h["version"] = vm.group(1) if vm else None
        h["steps"] = sorted({n for n, rx in STEPS if rx.search(ev[0])})
    return hits


DISC_GATE = {"rrid": "RRID", "github": "github.com", "zenodo": "zenodo",
             "cran": "cran.r-project", "bioc": "bioconductor.org"}


def discover(text):
    out = {}
    for k, rx in DISC_RE.items():
        gate = DISC_GATE.get(k)
        if gate and gate not in text:
            continue
        vals = []
        for m in rx.finditer(text):
            v = m.group(1) if rx.groups >= 1 else m.group(0)
            if k == "version":
                v = "%s %s" % (m.group(1), m.group(2))
            if v not in vals:
                vals.append(v)
            if len(vals) >= 40:
                break
        if vals:
            out[k] = vals
    return out


def process(rec):
    pmcid = rec.get("pmcid")
    raw, why = fetch(pmcid)
    if not raw:
        return {"pmcid": pmcid, "error": why}
    try:
        root = ET.fromstring(raw)
    except Exception as e:
        return {"pmcid": pmcid, "error": "parse_failed"}
    atype = root.get("article-type", "")
    full, meth = sections(root)
    if len(full) < 500:
        return {"pmcid": pmcid, "error": "no_body", "article_type": atype}
    # Search Methods first, then the rest of the body: software is also named in
    # figure legends, data-availability statements and supplementary notes.
    combined = meth + "\n\n" + full
    hits = evidence(combined, detect(combined))
    for n, h in hits.items():
        h["in_methods"] = h["pos"] < len(meth)
        h["license"] = "proprietary" if n in PROPRIETARY else "open-source"
    # first appearance (Methods ranked ahead of body) -> pipeline sequence
    order = sorted(hits.items(), key=lambda kv: kv[1]["pos"])
    pipeline = [{"tool": n, "version": h["version"], "steps": h["steps"],
                 "evidence": h["evidence"][0]} for n, h in order
                if h["license"] == "open-source"]
    return {
        "pmcid": pmcid, "pmid": rec.get("pmid"), "doi": rec.get("doi"),
        "journal": rec.get("_journal"), "year": rec.get("pubYear"),
        "title": rec.get("title"), "article_type": atype,
        "authors": (rec.get("authorString") or "")[:120],
        "n_software": sum(1 for h in hits.values() if h["license"] == "open-source"),
        "software": {n: {"category": h["category"], "version": h["version"],
                         "steps": h["steps"], "evidence": h["evidence"],
                         "in_methods": h["in_methods"], "license": h["license"]}
                     for n, h in hits.items()},
        "pipeline": pipeline,
        "discovery": discover(combined),
        "methods_chars": len(meth),
    }


if __name__ == "__main__":
    import concurrent.futures as cf
    inp, out = sys.argv[1], sys.argv[2]
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try:
                done.add(json.loads(line)["pmcid"])
            except Exception:
                pass
    recs = [json.loads(l) for l in open(inp)]
    recs = [r for r in recs if r.get("pmcid") and r["pmcid"] not in done]
    print("to process: %d (already done %d)" % (len(recs), len(done)), file=sys.stderr)
    n = 0
    with open(out, "a") as fh, cf.ThreadPoolExecutor(workers) as ex:
        for res in ex.map(process, recs):
            fh.write(json.dumps(res) + "\n")
            n += 1
            if n % 250 == 0:
                fh.flush()
                print("processed %d/%d" % (n, len(recs)), file=sys.stderr, flush=True)
    print("DONE %d" % n, file=sys.stderr)
