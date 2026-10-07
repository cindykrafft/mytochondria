# Watching what is filed

A scheduled check-in (a Claude Code Routine bound to the working session, every six hours) keeps
two things current without anyone asking: the filing console, and the CI on our open pull
requests. Replies to maintainers stay with the project owner: the watcher drafts them, it never
posts them.

## Inputs

- `seen.json`: the last snapshot of every issue and PR filed by the author since `since` in
  `../audits.json` (repo, number, kind, state, merged, comment count, updated). Taken with the
  GitHub search API (`author:<author> is:issue|is:pr created:>=<since> -org:google`), which works for any
  public repository from the session; comment bodies on repositories the author does not own do
  not, so a changed comment count is a signal to ask the owner for the text, not something the
  watcher can read.
- `../filed-fixes.txt`, `../pushed-branches.txt`, `../audits.json` (`declines_ai`): what the
  console builder reads.
- The forks under github.com/cindykrafft: their Actions runs are readable from the session, and
  every PR branch lives on a fork, so a PR's CI is checked there (the upstream workflow files run
  on push to the fork).

## Threads that carry our fix but are not ours

The author search does not find PRs opened by maintainers that carry our commits. Check these by
number each round (search `repo:<repo> <number>`), record state changes in the kit README, and drop
them from this list once merged or closed:

- Our comments on maintainer-opened issues, kept in `seen.json` as kind `comment`: samtools/samtools #696
  (ST3), arq5x/bedtools2 #1142 (BT2), deeptools/deepTools #1108 (DT1) and #1118 (DT4).

Scope: only the scientific-software audit. The author's other open-source work (the `google`
organisation: googletest, gson, guava, filament, comprehensive-rust, ...) is not part of it and is
neither searched nor recorded; `google-deepmind/alphafold3` is a different organisation and is in
scope. Anything else the search returns from a repository outside `../audits.json` is left out
of `seen.json` and the report. The public status page applies the same rule through
`exclude_owners` in `../audits.json`; add an owner there too when one is excluded here.

## Ledger statuses (since 2026-10-01)

Every thread in `seen.json` carries a `status`, set only after the thread was read in full:

- `resolved`: fixed upstream by any route (our PR merged, or the maintainers fixed it their own way;
  `fixed_by` names the merge, commit or PR).
- `rejected`: a maintainer declined, whether or not they closed the thread.
- `withdrawn`: we closed or retracted it ourselves.
- `in progress`: a maintainer or reviewer engaged and nothing is settled; `whose_move` is `us` when the
  last substantive human message asks us something or asks for a change, else `them`.
- `unanswered`: no human but us has said or done anything (bots and our own posts do not count).
- `internal`: a PR on one of our own repositories; not a filing.

Each status has `evidence` (the decisive human quote or action, verbatim, with author, date and URL)
and `status_checked` (the date of that full read). PRs list the issues they fix in `fixes`; an issue
and its PRs are one finding, and `build.py` rolls the threads up into `out/ledger.json` and the
console's Ledger section. The two-unanswered cap counts findings whose status is `unanswered`.

On a check-in, any thread whose state, comment count or update time changed is re-read in full and
re-classified before anything else is done with it. Read it through a helper session opened on that
thread's own repository; a helper can read only its source repository, so open one session per
repository. Update `status`, `whose_move`, `evidence` and `status_checked` from that read. A new filing
starts as `unanswered`. Never change a status from counts alone.

## One check-in

1. Search again, diff against `seen.json`. Diff the full result set (no `updated:` filter), or, if a filter is used to save calls, start it at
   least a day before the snapshot's `taken`: on 2026-10-02 scDblFinder #147/#148 were filed two minutes before a
   snapshot and missed by an `updated:>=taken` search until 2026-10-04. Report to the owner only: a state change (merged,
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

## Projects that require the submitter's own text (owner's rule, 2026-10-07)

One aim of the project is to automate bug finding, so the owner does not file with projects that require issue or
PR text written by the submitter (NumPy, scikit-learn, Matplotlib). They are flagged `requires_own_text` in
`../audits.json`, their cards are out of Do next, and the console's waiting list marks them as ignored. Their audits
and kits stay. Check a new project's contribution policy for this before preparing its kit. Projects already filed
with that ask for the submitter's own wording (samtools, BCFtools) are not covered by the rule; the owner decides
those case by case.
