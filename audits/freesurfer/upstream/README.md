# Upstream filing kit

Ready-to-file GitHub issues and pull requests for the defects found in the
FreeSurfer audit (`../README.md`, reproductions in `../reproductions/`).

Five fixes are implemented and pushed to the `cindykrafft/freesurfer` fork.
Open each upstream PR from the compare link; the matching body is in
`pr-bodies.md`:

| Branch | Fix | Compare URL |
|---|---|---|
| `fix/fsglm-ffx-fstat` | FFx multi-row F-test /J | https://github.com/freesurfer/freesurfer/compare/dev...cindykrafft:freesurfer:fix/fsglm-ffx-fstat |
| `fix/vol2surf-projfrac-endpoint` | projfrac endpoint drop | https://github.com/freesurfer/freesurfer/compare/dev...cindykrafft:freesurfer:fix/vol2surf-projfrac-endpoint |
| `fix/gcsa-island-loglikelihood` | island relabel int truncation | https://github.com/freesurfer/freesurfer/compare/dev...cindykrafft:freesurfer:fix/gcsa-island-loglikelihood |
| `fix/anatomical-stats-thickness-range` | -i silent no-op | https://github.com/freesurfer/freesurfer/compare/dev...cindykrafft:freesurfer:fix/anatomical-stats-thickness-range |
| `fix/aparc2aseg-stale-state` | stale winner state / uninit read | https://github.com/freesurfer/freesurfer/compare/dev...cindykrafft:freesurfer:fix/aparc2aseg-stale-state |

Each PR also has a **companion bug issue** (`issue-pr1-*.md` through
`issue-pr5-*.md`): file the issue first, then reference it from the PR with
"Fixes #N" so the pair is linked and the issue closes on merge.

Issues without a PR (already fixed on dev, need a decision, or need a
larger change): `issue-b1-*.md`, `issue-b3-*.md`, `issue-b6-*.md`, and the
race half of `issue-b12-*.md`.

Verification honesty: the fixes were validated by extracting the changed
logic into standalone harnesses (loop enumeration for the projfrac fix;
200k-draw Monte Carlo calibration for the FFx fix) and by careful diff
review. Full compilation was not run in the authoring environment (ITK is
required); please build before merging.

Suggested filing order: B1 first (release-blocking for statistics; fix
already on dev, ask is a backport/release note), then the five PRs, then
the remaining issues.
