# Upstream filing kit — DESeq2

Everything that was filed for the DESeq2 audit findings (`../README.md`,
review in `../component-reviews/statistical-core.md`), the outcome, and what
this round got wrong.

## Outcome (filed and closed 2026-09-01)

| File | Filed as | Maintainer's response |
|---|---|---|
| `issue-ds1-weights-erratum.md` | [#130](https://github.com/thelovelab/DESeq2/issues/130) | closed: "This change was documented in NEWS" (it is, under 1.49.4) |
| `issue-ds2-lfcthreshold-docs.md` | [#133](https://github.com/thelovelab/DESeq2/issues/133) | closed: "already documented in NEWS" (it is, under 1.44.0, naming `greaterAbs2014`) |
| `issue-pr1-replace-round.md` | [#131](https://github.com/thelovelab/DESeq2/issues/131) | closed: "will not be taken up for the same reason" |
| `pr1-replace-round.md` + `0001-*.patch` | [#132](https://github.com/thelovelab/DESeq2/pull/132) | closed: "This PR would change DESeq2 results and so won't be taken on" |
| `support-post-zinbwave.md` | never posted, and will not be | see below |

Each reply pointed to the project's pinned policy,
[issue #1](https://github.com/thelovelab/DESeq2/issues/1) (2017): usage
questions go to the Bioconductor support site; non-minor PRs are discussed
there first; undiscussed major PRs are not accepted because the maintainer
cannot vet unintended consequences for the user base. `CONTRIBUTING.md`
(added July 2026) says the same.

## What went wrong

The maintainer was right on every point, and the filings cost him time
instead of saving it.

1. **The NEWS claim was false.** `issue-ds1-weights-erratum.md` says "there is
   no NEWS entry or user-facing notice for this fix." The project inspected the
   fix commit `abe5994`, which touches only `R/results.R` and a test, and
   concluded nothing was announced. The entry was added in the same-day
   version-bump commit `5f5e305`. A `grep -i weights NEWS` would have found it.
2. **The guidelines were not read.** This kit never mentioned issue #1 or
   `CONTRIBUTING.md`, while the SPM kit did read SPM's. The PR was sent cold,
   contrary to a policy that had been pinned for nine years.
3. **The PR contradicted the project's own judgment.** The review classified the
   truncation bias as "verified negligible", and the project's stated policy is
   to keep results stable. A negligible, results-changing PR is the exact case
   the policy exists to decline.

The filing-process fix is recorded in the top-level README (step 4): read
`CONTRIBUTING.md`, pinned policy issues, NEWS, and the issue/PR history
before filing; discuss non-minor or results-changing work in the project's
preferred venue first; note in each kit which of those were read.

## Nothing further is filed

`support-post-zinbwave.md` was drafted as a support-site notice for
zinbwave/weights users and never posted. It stays unposted. The maintainer has
reviewed the finding and judged the 1.49.4 NEWS entry sufficient; posting a
notice on his package's support forum after that would be going around him in
the venue his policy points to, and the cohort exposure (one paper naming
zinbwave, from 2020) does not justify it. The reproduction script and analysis
are public in this repository for anyone who needs to check an old analysis.

The rounding change is withdrawn.
