#!/usr/bin/env python3
"""Harvest Europe PMC metadata for the six target journals, 2021-2026."""
import json, sys, time, urllib.parse, urllib.request, os

BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
JOURNALS = {
    "Nature":  ["0028-0836", "1476-4687"],
    "Science": ["0036-8075", "1095-9203"],
    "PNAS":    ["0027-8424", "1091-6490"],
    "NEJM":    ["0028-4793", "1533-4406"],
    "Lancet":  ["0140-6736", "1474-547X"],
    "Cell":    ["0092-8674", "1097-4172"],
}
OUT = os.path.join(os.path.dirname(__file__), "records.jsonl")

def fetch(params, tries=5):
    url = BASE + "?" + urllib.parse.urlencode(params)
    for a in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return json.load(r)
        except Exception as e:
            if a == tries - 1:
                raise
            time.sleep(2 ** a)

total = 0
with open(OUT, "w") as fh:
    for name, issns in JOURNALS.items():
        query = "(%s) AND (PUB_YEAR:[2021 TO 2026])" % " OR ".join("ISSN:%s" % i for i in issns)
        cursor, n = "*", 0
        while True:
            d = fetch({"query": query, "format": "json", "pageSize": 1000,
                       "resultType": "lite", "cursorMark": cursor})
            res = d["resultList"]["result"]
            if not res:
                break
            for r in res:
                r["_journal"] = name
                fh.write(json.dumps(r) + "\n")
            n += len(res)
            nxt = d.get("nextCursorMark")
            if not nxt or nxt == cursor:
                break
            cursor = nxt
            print("  %s %d/%d" % (name, n, d["hitCount"]), file=sys.stderr, flush=True)
        print("DONE %s: %d" % (name, n), file=sys.stderr, flush=True)
        total += n
print("TOTAL %d -> %s" % (total, OUT), file=sys.stderr)
