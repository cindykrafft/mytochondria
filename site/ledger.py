"""Roll ledger thread statuses (console/seen.json) up to findings. Shared by console/build.py and build_data.py.

An issue and the pull requests that say they fix it are one finding. Its status is the best of its threads:
resolved > in progress > rejected > all withdrawn > unanswered.
"""
ORDER = ("resolved", "in progress", "rejected", "withdrawn", "unanswered")

def threads(seen, skip_owners=()):
    """Classified threads from seen.json, without own repositories (status internal) or skipped owners."""
    skip = {o.lower() for o in skip_owners}
    return [x for x in seen["items"] if isinstance(x, dict) and x.get("status") and x["status"] != "internal"
            and x["repo"].split("/")[0].lower() not in skip]

def _roll(st):
    if "resolved" in st: return "resolved"
    if "in progress" in st: return "in progress"
    if "rejected" in st: return "rejected"
    if all(s == "withdrawn" for s in st): return "withdrawn"
    if "unanswered" in st: return "unanswered"
    return "withdrawn"

def rollup(items):
    """Group threads into findings: a list of (status, whose_move, threads), threads lead with the issue."""
    used, groups = set(), []
    for x in sorted(items, key=lambda x: (x["repo"], x["number"])):
        if x["kind"] == "pr": continue
        grp = [x] + [p for p in items if p["kind"] == "pr" and p["repo"] == x["repo"] and x["number"] in (p.get("fixes") or [])]
        used.update((g["repo"], g["number"]) for g in grp)
        groups.append(grp)
    groups += [[p] for p in items if (p["repo"], p["number"]) not in used]
    out = []
    for grp in groups:
        s = _roll([g["status"] for g in grp])
        mv = ("us" if any(g.get("whose_move") == "us" for g in grp) else "them") if s == "in progress" else None
        out.append((s, mv, grp))
    return out
