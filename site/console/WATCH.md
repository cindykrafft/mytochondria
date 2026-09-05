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
