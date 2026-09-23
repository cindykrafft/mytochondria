#!/usr/bin/env python3
"""Diff two saved GitHub search results (issues, PRs) against site/console/seen.json.

    diff_search.py <issues.json> <prs.json> [--write-now <path>]

Prints new, gone and changed items (state, merged, comments); with --write-now saves the fresh item
list for the snapshot update.
"""
import json, sys
def main():
    a = sys.argv[1:]; out = None
    if "--write-now" in a:
        i = a.index("--write-now"); out = a[i+1]; del a[i:i+2]
    items = {}
    for f, kind in ((a[0], "issue"), (a[1], "pr")):
        d = json.load(open(f))
        for it in d["items"]:
            repo = "/".join(it["repository_url"].split("/")[-2:])
            merged = bool((it.get("pull_request") or {}).get("merged_at")) if kind == "pr" else False
            items[(repo, it["number"])] = dict(repo=repo, number=it["number"], kind=kind, state=it["state"], merged=merged,
                                               comments=it["comments"], updated=it["updated_at"], title=it["title"])
        print(kind, d.get("total_count"), "found,", len(d["items"]), "returned")
    seen = json.load(open("site/console/seen.json"))
    old = {(i["repo"], i["number"]): i for i in seen["items"] if i["kind"] in ("issue", "pr")}
    print("new:", [(k, items[k]["title"][:70]) for k in items if k not in old])
    print("gone:", [k for k in old if k not in items])
    for k, i in items.items():
        o = old.get(k)
        if not o: continue
        diffs = [f for f in ("state", "merged", "comments") if o.get(f) != i[f]]
        if diffs: print("CHANGED", k, i["kind"], {f: (o.get(f), i[f]) for f in diffs}, i["updated"], "|", i["title"][:70])
    if out: json.dump({"items": list(items.values())}, open(out, "w"))
if __name__ == "__main__": main()
