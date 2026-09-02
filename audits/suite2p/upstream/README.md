# Suite2p upstream filing kit

Suite2p takes issues and PRs on GitHub (`MouseLand/suite2p`, base `main`) from
a fork. Recommended order:

1. **S2 — bidiphase corruption** (`issue-s2-bidiphase.md`, then `pr-s2-bidiphase.md`;
   patch `0001-bidiphase.shift-...patch`). Reference the issue number from the PR.
2. **S1 — classifier bin wrap** (`pr-s1-classifier.md`; patch `0001-Classifier-...patch`).
3. **S5 — integer index tensors** (`pr-s5-index-dtype.md`; patch `0001-extract_traces-...patch`).
4. **S3 — constant baseline** (`issue-s3-constant-baseline.md`, question).
5. **S7 — doubled high-pass** (`issue-s7-double-highpass.md`, question).

## Live branches on the fork (cindykrafft/suite2p, each one commit on main @ 90be895)

| finding | branch | head | compare page |
|---|---|---|---|
| S2 | `fix/bidiphase-torch-overlap` | 4615ebc | https://github.com/MouseLand/suite2p/compare/main...cindykrafft:suite2p:fix/bidiphase-torch-overlap?expand=1 |
| S1 | `fix/classifier-bin-clip` | 8921874 | https://github.com/MouseLand/suite2p/compare/main...cindykrafft:suite2p:fix/classifier-bin-clip?expand=1 |
| S5 | `fix/extract-index-dtype` | 9110c72 | https://github.com/MouseLand/suite2p/compare/main...cindykrafft:suite2p:fix/extract-index-dtype?expand=1 |

Each patch applies independently to `main` @ 90be895. From a fork:

```bash
git clone --depth 1 https://github.com/<you>/suite2p && cd suite2p
for p in ../0001-*.patch; do b=$(basename "$p" .patch | sed 's/^0001-//'); git checkout -b "fix/$b" main && git am "$p" && git checkout main; done
git push -u origin --all
```

All three patches were validated against the harnesses in `../verify/`
(odd lines exact; P(cell) continuous at the training minimum; int64 indices).
