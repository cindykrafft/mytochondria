import json, os, re, urllib.parse
S = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "kits")
def kit(name):
    t = open(os.path.join(S, name)).read()
    m = re.match(r"\*\*Title:\*\* (.+)\n+", t)
    title = m.group(1).strip().strip("`") if m else ""
    return title, t[m.end():] if m else t

LIMIT = 7500
def q(d): return "&".join(k + "=" + urllib.parse.quote(v, safe="") for k, v in d.items() if v)

items = []
def pr(id, repo, branch, kitfile, why, closes=None, note=None, base="main", reply=None, reply_to=None):
    title, body = kit(kitfile)
    owner, name = repo.split("/")
    base = f"https://github.com/{repo}/compare/{base}...cindykrafft:{name}:{branch}?"
    url = base + q({"expand": "1", "title": title, "body": body})
    short = len(url) > LIMIT
    if short: url = base + q({"expand": "1", "title": title})
    replytext = open(os.path.join(S, reply)).read().strip() if reply else None
    items.append(dict(kind="pr", id=id, repo=repo, branch=branch, base=base, title=title, body=body, url=url, reply=replytext, reply_to=reply_to,
                      short=short, why=why, closes=closes, note=note,
                      fork_url=f"https://github.com/cindykrafft/{name}/tree/{branch}"))

FORM_LABELS = {"what-happened": "Describe the issue", "steps": "Steps to reproduce the problem",
    "version": "What version of GoogleTest are you using?", "os": "What operating system and version are you using?",
    "compiler": "What compiler and version are you using?", "buildsystem": "What build system are you using?",
    "additional": "Additional context"}
def issue_form(id, repo, template, jsonfile, why):
    f = json.load(open(os.path.join(S, jsonfile)))
    title = f.pop("title")
    base = f"https://github.com/{repo}/issues/new?"
    url = base + q(dict({"template": template, "title": title}, **f))
    short = len(url) > LIMIT
    if short: url = base + q({"template": template, "title": title})
    fields = [[FORM_LABELS.get(k, k), v] for k, v in f.items()]
    body = "\n\n".join("### " + k + "\n\n" + v for k, v in fields)
    items.append(dict(kind="form", id=id, repo=repo, title=title, url=url, short=short, why=why,
                      fields=fields, body=body))

pr("gson-inet-fix", "google/gson", "fix-inetaddress-literal-check", "gson-inetaddress-fix-pr.md",
   "Answer the maintainer on #3128: eamonnmcmanus said a PR tightening the check would probably be accepted. Open this PR first, then post the reply with its number filled in.",
   closes=3128, reply="gson-3128-reply.md", reply_to=3128)
pr("gson-1138", "google/gson", "fix-jsonsyntaxexception-javadoc", "gson-1138-pr.md",
   "Javadoc-only fix for a 2017 issue nobody has touched. The gentlest first PR.", closes=1138)
pr("gtest-4769", "google/googletest", "docs-windows-thread-safety", "googletest-4769-pr.md",
   "Docs-only fix in a different repository, so it can go in the same day.", closes=4769,
   note="googletest brings outside PRs in through an internal import, so a reply can take a week or more.")
pr("guava-2884", "google/guava", "docs-toSortedList-stability", "guava-docs-toSortedList-stability-pr.md",
   "First guava PR: a Javadoc-only fix for an issue the maintainers labelled triaged. Can go in alongside the gson and googletest PRs.",
   closes=2884, base="master",
   note="guava doesn't merge PRs on GitHub. A maintainer copies the change into Google's internal code, it comes back as a commit credited to you, and the PR is closed.")
pr("gson-skip", "google/gson", "fix-strict-skipvalue", "gson-skipvalue-pr.md",
   "First code fix for gson. Best opened once the Javadoc PR has had a reply, so the maintainers aren't hit with three at once.",
   note="There is no issue for this bug. The PR description carries the repro, which gson accepts for small fixes.")
pr("gtest-base64", "google/googletest", "fix-base64-unescape-high-bytes", "googletest-base64-pr.md",
   "First googletest code fix: a one-line memory-safety fix. Can go in alongside the docs PR.",
   note="There is no issue for this bug. googletest's CONTRIBUTING asks for an issue first, but a small, self-evident fix with a test is usually accepted directly.")
issue_form("gtest-death", "google/googletest", "00-bug_report.yml", "googletest-deathtest-issue.json",
   "The most serious googletest finding. It's an issue, not a PR, because the fix needs the maintainers to pick an approach.")
pr("guava-2690", "google/guava", "docs-futures-transform-exceptions", "guava-docs-futures-transform-exceptions-pr.md",
   "Second guava docs fix. Open it once the first guava PR has had a reply.", closes=2690, base="master")
pr("guava-nav", "google/guava", "fix-filtered-navigablemap-entries", "guava-fix-filtered-navigablemap-entries-pr.md",
   "First guava code fix, and the most serious guava finding: filtered NavigableMap views return the wrong entry.",
   base="master", note="There is no issue for this bug. guava's CONTRIBUTING says PRs are welcome for bug fixes that don't change the API.")
pr("gson-cache", "google/gson", "fix-getadapter-cache-poisoning", "gson-getadapter-pr.md",
   "Second gson code fix. Open after the skipValue PR gets a response.",
   note="There is no issue for this bug. The PR description carries the repro.")
pr("gtest-diff", "google/googletest", "fix-diff-trailing-newline", "googletest-diff-pr.md",
   "Second googletest code fix. Open after the Base64 PR gets a response.",
   note="There is no issue for this bug. The PR description shows the diff before and after.")

pr("guava-stats", "google/guava", "fix-stats-mean-overflow", "guava-fix-stats-mean-overflow-pr.md",
   "Second guava code fix. Open it after the NavigableMap PR gets a response.", base="master",
   note="There is no issue for this bug. Results for inputs that didn't overflow are unchanged, bit for bit.")
pr("guava-rotate", "google/guava", "fix-primitives-rotate-edge-cases", "guava-fix-primitives-rotate-edge-cases-pr.md",
   "Third guava code fix: the same small fix in all 8 primitive classes.", base="master",
   note="There is no issue for this bug.")

it_title, it_body = kit("gson-inetaddress-issue.md")
ibase = "https://github.com/google/gson/issues/new?"
iurl = ibase + q({"template": "bug_report.md", "title": it_title, "body": it_body})
ishort = len(iurl) > LIMIT
if ishort: iurl = ibase + q({"template": "bug_report.md", "title": it_title})
_, priv = kit("gson-inetaddress-report.md")
items.append(dict(kind="report", id="gson-inet", repo="google/gson", title=it_title, body=it_body,
                  url=iurl, short=ishort, private=priv,
                  why="Choose one route: a private report to Google's vulnerability program, or a public issue. Don't do both."))

held = [
 ("google/gson", "JsonTreeReader rejects quoted \"1.0\" / \"1e2\" as int or long, while JsonReader accepts them", "mirror image of #2817"),
 ("google/gson", "java.time adapters throw raw DateTimeException / ZoneRulesException / ArithmeticException", "fits with the Javadoc PR"),
 ("google/gson", "TypeToken.getParameterized drops the owner type of static nested classes", "touches type equality; file as an issue first"),
 ("google/gson", "Outer-class type variables are not resolved in inner-class fields", "touches type resolution; file as an issue first"),
 ("google/gson", "Locale round trip loses data for _US, scripts and en__POSIX", "compatibility question"),
 ("google/gson", "EnumSet<? extends E> / EnumMap<? extends K,V> fields throw", "small"),
 ("google/googletest", "testing::Range() overflows for narrow types or near the maximum: wrong tests, hangs, UB", "small fix; good third googletest PR"),
 ("google/googletest", "--gtest_fail_if_no_test_selected skips writing the XML/JSON report", "small fix in RunAllTests"),
 ("google/googletest", "volatile pointers print as 1 in failure messages", "small printer fix"),
 ("google/googletest", "--gtest_list_tests with XML/JSON output ignores --gtest_filter", "small"),
 ("google/googletest", "IsSubsetOf failure message says \"2 of 5 matchers\" instead of \"2 of 3 elements\"", "one line"),
 ("google/googletest", "Minor: invalid UTF-8 for U+110000..U+1FFFFF, JSON duration precision, unescaped JSON property keys, EXPECT_NEAR hint at DBL_MAX", "batch later"),
 ("google/guava", "BloomFilter.create(funnel, 1, 0.75) throws \"0 bits\" for valid settings", "one-line fix"),
 ("google/guava", "ByteSource.slice().slice() overflows past Long.MAX_VALUE instead of returning empty", "one-line fix"),
 ("google/guava", "InetAddresses accepts an empty IPv6 zone ID (\"fe80::1%\")", "one-line fix"),
 ("google/guava", "UnsignedInts.parseUnsignedInt(\"-0\") / decode(\"0x-0\") accept a sign", "small"),
 ("google/guava", "#2237: document the argument-order performance of Multisets.intersection/union", "benchmark claim needs checking"),
 ("google/guava", "Javadoc typo in rotate/reverse @throws (\"toIndex > fromIndex\") in all 8 primitive classes", "follow-up to the rotate PR"),
 ("google/guava", "TypeToken.toString() prints Outer$Inner<> for inner classes of generic classes", "cosmetic"),
]
data = dict(items=items, held=held)
page = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "template.html")).read()
page = page.replace("__DATA__", json.dumps(data).replace("</", "<\\/"))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "google-filing-console.html")
open(out, "w").write(page)
watch = [dict(id=i["id"], repo=i["repo"], kind=i["kind"], title=i["title"], branch=i.get("branch")) for i in items]
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "watch.json"), "w").write(json.dumps(watch, indent=1) + "\n")
for i in items: print(i["id"], len(i["url"]), "title-only" if i["short"] else "prefilled")
