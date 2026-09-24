# Google open-source contributions

These are contributions to Google's GitHub projects, gson and googletest in particular. The work
is separate from the Mytochondria audits and is kept on its own branch.

- `console/`: the Google OSS Filing Console (https://claude.ai/artifact/PbYYM9MogdfvzJSTybwbuf).
  `gen.py` builds `google-filing-console.html` from `template.html` and the kits, and also writes
  `watch.json`, the list the watcher checks.
- `kits/`: the PR descriptions and issue texts, exactly as the console submits them.
- `findings/`: the two bug hunts. Each finding was reproduced against the upstream HEAD of the day
  and checked for existing reports.
- `CLAUDE.md`: rules for everything we write upstream (don't overstate; say only what the code and our runs show).
- `WATCH.md`: how the scheduled watcher keeps the console's filing status current.

The code for each fix lives on a branch of the matching fork (`cindykrafft/gson`,
`cindykrafft/googletest`). The branch names are in `console/watch.json`.
