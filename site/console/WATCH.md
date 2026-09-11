# Watching what is filed

A scheduled check-in (a Claude Code Routine bound to the working session, every six hours) keeps
two things current without anyone asking: the filing console, and the CI on our open pull
requests. Replies to maintainers stay with the project owner: the watcher drafts them, it never
posts them.

## Inputs

- `seen.json`: the last snapshot of every issue and PR filed by the author since `since` in
  `../audits.json` (repo, number, kind, state, merged, comment count, updated). Taken with the
  GitHub search API (`author:<author> is:issue|is:pr created:>=<since>`), which works for any
  public repository from the session; comment bodies on repositories the author does not own do
  not, so a changed comment count is a signal to ask the owner for the text, not something the
  watcher can read.
- `../filed-fixes.txt`, `../pushed-branches.txt`, `../audits.json` (`declines_ai`): what the
  console builder reads.
- The forks under github.com/cindykrafft: their Actions runs are readable from the session, and
  every PR branch lives on a fork, so a PR's CI is checked there (the upstream workflow files run
  on push to the fork).

## One check-in

1. Search again, diff against `seen.json`. Report to the owner only: a state change (merged,
   closed, resolved, declined), a comment count that went up, a new filing that is not yet in
   `filed-fixes.txt` (the owner filed from the console; add the line), or a PR whose CI went red.
2. For every open PR with a branch on a fork: latest workflow runs on that branch. Red and ours
   to fix (the failure is in code the PR touches, or a test that pinned the values the PR changes):
   fix on the branch, run the repo's own checks locally, push to the fork, note it in the kit's
   `test-runs.txt`. Red on the base branch too: leave it, say so once. Never skip or disable a
   test to get green.
3. Rebuild the console (`python3 build.py && python3 gen_html.py`, output in `out/`) and
   republish it to the same artifact URL whenever anything above changed a card.
4. Any reply a maintainer's comment calls for: draft it under `audits/<pkg>/upstream/` (or the
   issue-fix directory) and hand it to the owner. Nothing is posted from the session.
5. Write the new snapshot to `seen.json`, commit to `main` with the kit notes, push.

Repositories whose forks carry the `declines_ai` flag get nothing: no pushes, no drafts, only the
state recorded.

## Reading a thread

Comment bodies on repositories the author does not own are not readable from the working
session (the GitHub tools are scoped to the attached forks; api.github.com and the issue pages'
client-rendered comments are unreachable). Before any comment is drafted on an existing issue or
PR, and before any reply to a maintainer, the thread is read in full this way:

1. Start a helper session on the upstream repository (`create_session` with `source_url` set to
   the upstream repo, `permission_mode` acceptEdits) with a read-only task: read the issue or PR
   and every comment, plus the threads it links to, and publish a verbatim transcript (author,
   association, timestamp, body) to the shared export artifact
   `https://claude.ai/code/artifact/371dd757-fc21-45a4-aea0-566f4ae06dfb`, updating it in place.
2. Read the artifact (`Artifact` action `read`), then draft or, if the thread already carries
   the point, drop the item and record why in the kit README.
3. Note in the kit README the date the thread was read and what it contained.

A helper in default mode can block on an Artifact permission prompt; acceptEdits avoids it. A
helper that still cannot publish is told to put the transcript in its final message instead.

## Checking a PR without reading GitHub (added 2026-09-11)

Comment bodies, reviews and mergeability on repositories this session does not own are
unreadable, and both workarounds have limits: `add_repo` refuses a cross-owner add once the
session holds `cindykrafft` repositories, and a helper session can only hand its answer back
through an artifact, which stalls on a permission prompt its own mode cannot grant. What does
work, and answers the question that actually needs action, is a local merge test:

    git -C <clone> fetch origin <base>            # upstream, public: git reads work
    git -C <clone> fetch fork
    git -C <clone> rev-list --count fork/<branch>..origin/<base>     # how far behind
    git -C <clone> merge-tree --write-tree fork/<branch> origin/<base>  # exit 0 = no conflict

A PR's `updated_at` moving while its comment count stays put is usually a base-branch push
recomputing mergeability, or CI re-running; the merge test tells you whether that matters. Only
a real conflict, or a maintainer comment the owner has read, is work.
