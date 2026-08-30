#!/usr/bin/env python3
"""Drop detections whose stored evidence shows the match was not the software.

"Quantifoil R 1.2/1.3" is a cryo-EM grid hole specification, not the R language,
but it satisfies the `R <version>` context pattern. Same idea for any other
context name whose evidence sentence proves the match was something else.
"""
import json, re, sys

REJECT = {
    "R": re.compile(r"[Qq]uantifoil|UltrAuFoil|holey|\d\.\d\s*/\s*\d\.\d", re.I),
}

inp, out = sys.argv[1], sys.argv[2]
dropped = 0
with open(out, "w") as fh:
    for line in open(inp):
        r = json.loads(line)
        if "error" not in r:
            for name, rx in REJECT.items():
                h = r["software"].get(name)
                if h and rx.search(h["evidence"][0]):
                    del r["software"][name]
                    r["pipeline"] = [p for p in r["pipeline"] if p["tool"] != name]
                    dropped += 1
            r["n_software"] = sum(1 for h in r["software"].values()
                                  if h["license"] == "open-source")
        fh.write(json.dumps(r) + "\n")
print("dropped %d misidentified detections" % dropped)
