# Upstream filing kit — DESeq2

Everything ready-to-file for the DESeq2 audit findings (`../README.md`,
review in `../component-reviews/statistical-core.md`).

DESeq2 accepts GitHub issues at `thelovelab/DESeq2`; the Bioconductor support
site is the user-facing channel. Unlike the FreeSurfer round, the headline
finding (DS1) is **already fixed upstream** — the filings are about
*communication*: an erratum so eight years of affected releases aren't silent,
and visibility for the lfcThreshold behavior change.

| File | Target | What it is |
|---|---|---|
| `issue-ds1-weights-erratum.md` | GitHub issue | request NEWS/erratum for the weights misalignment (releases 1.16.0–1.49.x), repro attached |
| `support-post-zinbwave.md` | support.bioconductor.org | PSA draft so weights-workflow users can check their analyses |
| `issue-ds2-lfcthreshold-docs.md` | GitHub issue | visibility request for the v1.44 lfcThreshold statistic change |
| `issue-pr1-replace-round.md` | GitHub issue | companion issue for the rounding PR |
|  `pr1-replace-round.md` | GitHub PR body | the one-line `round()` fix |
| `0001-replaceOutliers-round-*.patch` | git am | the same fix as a format-patch (applies to current devel) |

## Filing order

1. File `issue-ds1-weights-erratum.md` (the important one).
2. Post `support-post-zinbwave.md` on the support site, linking the issue.
3. File `issue-ds2-lfcthreshold-docs.md`.
4. File `issue-pr1-replace-round.md`, note its number N.
5. The fix branch is pushed to the fork (`cindykrafft/deseq2`,
   `fix/replace-outliers-rounding`, commit c0a7715). Open the PR from the
   compare page with `pr1-replace-round.md` as body, replacing `#NNN` with N:
   https://github.com/thelovelab/DESeq2/compare/devel...cindykrafft:deseq2:fix/replace-outliers-rounding

The filing console (artifact) has copy buttons and pre-filled GitHub links for
all of these.
