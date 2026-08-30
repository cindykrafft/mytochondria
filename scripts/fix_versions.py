#!/usr/bin/env python3
"""Recover versions that the in-span search missed.

For context-matched names ("STAR (v", "Python 3") the matched span stops before
the number, so no version was recorded. The evidence sentence is stored, so the
version can be recovered from it without re-fetching: anchor on the package name
(or any of its aliases) and require the number to follow immediately.
"""
import json, re, sys
sys.path.insert(0, ".")
from software_db import SAFE, AMBIGUOUS
from extract import VERSION_AFTER

ALIASES = {n: sorted(set([n] + list(al)), key=len, reverse=True)
           for n, (cat, al) in SAFE.items()}
for n in AMBIGUOUS:
    ALIASES.setdefault(n, [n])


def recover(name, sent):
    for a in ALIASES.get(name, [name]):
        a = a.strip()
        i = sent.find(a)
        while i >= 0:
            m = VERSION_AFTER.match(sent[i + len(a): i + len(a) + 32])
            if m:
                return m.group(1)
            i = sent.find(a, i + 1)
    return None


inp, out = sys.argv[1], sys.argv[2]
fixed = tot = 0
with open(out, "w") as fh:
    for line in open(inp):
        r = json.loads(line)
        if "error" not in r:
            for name, h in r.get("software", {}).items():
                tot += 1
                if not h.get("version"):
                    v = recover(name, h["evidence"][0])
                    if v:
                        h["version"] = v
                        fixed += 1
            for p in r.get("pipeline", []):
                h = r["software"].get(p["tool"])
                if h:
                    p["version"] = h.get("version")
        fh.write(json.dumps(r) + "\n")
print("versions recovered: %d of %d usage records" % (fixed, tot))
