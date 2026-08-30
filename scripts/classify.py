#!/usr/bin/env python3
"""Split harvested records into processable corpus vs. no-open-full-text gap list."""
import json, re
from collections import defaultdict

NONRESEARCH = re.compile(
    r"news|editorial|comment|letter|correction|erratum|retract|biograph|obituar|"
    r"interview|congress|historical article|portrait|bibliograph|video-audio|"
    r"newspaper article|address|lecture|introductory journal article", re.I)
TITLE_SKIP = re.compile(r"^(correction|erratum|retraction|corrigendum|addendum|"
                        r"reply to|response to|author correction|publisher correction)", re.I)


def is_research(r):
    pt = r.get("pubType", "") or ""
    title = r.get("title", "") or ""
    if TITLE_SKIP.match(title.strip()):
        return False
    if "research-article" in pt:
        return True
    if "journal article" in pt and not NONRESEARCH.search(pt):
        return True
    return False


if __name__ == "__main__":
    recs = [json.loads(l) for l in open("records.jsonl")]
    corpus, gap, nonres = [], [], 0
    for r in recs:
        if not is_research(r):
            nonres += 1
            continue
        (corpus if r.get("inEPMC") == "Y" and r.get("pmcid") else gap).append(r)
    with open("process_in.jsonl", "w") as fh:
        for r in corpus:
            fh.write(json.dumps(r) + "\n")
    with open("gap_list.jsonl", "w") as fh:
        for r in gap:
            fh.write(json.dumps(r) + "\n")
    print("total records      : %d" % len(recs))
    print("non-research        : %d" % nonres)
    print("research articles   : %d" % (len(corpus) + len(gap)))
    print("  -> full text avail: %d  (process_in.jsonl)" % len(corpus))
    print("  -> NO full text   : %d  (gap_list.jsonl)" % len(gap))
    d = defaultdict(lambda: [0, 0])
    for r in corpus: d[r["_journal"]][0] += 1
    for r in gap:    d[r["_journal"]][1] += 1
    print("\n%-8s %8s %8s %7s" % ("JOURNAL", "CORPUS", "GAP", "COVER"))
    for k in ("Nature","Science","PNAS","NEJM","Lancet","Cell"):
        a, b = d[k]
        print("%-8s %8d %8d %6.0f%%" % (k, a, b, 100*a/max(1,a+b)))
