"""Build site/data.json: every issue and pull request this project has filed upstream, with its current state.

Discovery is by author and date through the GitHub search API (no registry to keep in sync); each item is
attached to an audit through the repository map in audits.json. Repositories the author owns are skipped
(forks, this repository). Needs GITHUB_TOKEN in the environment (the Actions token is enough).
"""
import json, os, sys, time, urllib.request, urllib.parse
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(os.path.join(HERE, "audits.json")))
AUTHOR, SINCE = cfg["author"], cfg["since"]
repo_to_audit = {r.lower(): a["dir"] for a in cfg["audits"] for r in a["repos"]}
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "research-software-audit-site",
                                               **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and attempt < 4:
                time.sleep(30 * (attempt + 1)); continue
            raise

def search(kind):
    q = f"author:{AUTHOR} is:{kind} created:>={SINCE}"
    items, page = [], 1
    while True:
        d = get("https://api.github.com/search/issues?" + urllib.parse.urlencode({"q": q, "per_page": 100, "page": page, "sort": "created", "order": "asc"}))
        items += d["items"]
        if len(items) >= d["total_count"] or not d["items"]: break
        page += 1
    return items

def slim(it, kind):
    repo = it["repository_url"].split("/repos/")[1]
    pr = it.get("pull_request") or {}
    merged = bool(pr.get("merged_at"))
    if kind == "pr":
        status = "merged" if merged else ("open" if it["state"] == "open" else "closed_unmerged")
    else:
        status = "open" if it["state"] == "open" else ("declined" if it.get("state_reason") == "not_planned" else "resolved")
    return {"repo": repo, "number": it["number"], "kind": kind, "title": it["title"], "url": it["html_url"], "status": status,
            "comments": it.get("comments", 0), "created": it["created_at"], "closed": it.get("closed_at"),
            "updated": it["updated_at"], "merged_at": pr.get("merged_at")}

# Forks that carry the "declines" topic: the upstream maintainers do not take AI-generated contributions.
TOPIC = cfg.get("declines_topic")
for a in cfg["audits"]:
    a.setdefault("declines_ai", False)
    if TOPIC and a.get("fork"):
        try:
            topics = get(f"https://api.github.com/repos/{a['fork']}/topics").get("names", [])
        except urllib.error.HTTPError as e:
            if e.code == 404: continue   # no fork yet
            raise
        if TOPIC in topics: a["declines_ai"] = True

items = []
unmapped = set()
for kind in ("issue", "pr"):
    for it in search(kind):
        repo = it["repository_url"].split("/repos/")[1]
        if repo.split("/")[0].lower() == AUTHOR.lower(): continue
        s = slim(it, kind)
        if repo.lower() not in repo_to_audit: unmapped.add(repo)
        s["audit"] = repo_to_audit.get(repo.lower())
        items.append(s)
items.sort(key=lambda x: x["created"])
out = {"generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "author": AUTHOR, "since": SINCE,
       "audits": cfg["audits"], "audit_repo": cfg["audit_repo"], "declines_topic": TOPIC, "items": items, "unmapped_repos": sorted(unmapped)}
json.dump(out, open(os.path.join(HERE, "data.json"), "w"), indent=1)
print(f"{len(items)} items across {len({i['repo'] for i in items})} repositories; unmapped: {sorted(unmapped)}", file=sys.stderr)
