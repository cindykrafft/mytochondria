# Research software audit

An AI-assisted correctness audit of the open-source software that published science
actually runs — driven by a full-text survey of what the literature reports using,
then targeted source-level review of those exact components, with every suspected
defect verified numerically before it is reported upstream.

Research software is unusually hard code: mathematically intricate, evolving alongside
the science it serves, maintained for decades, and usually built by small teams under
tight grant budgets. The packages audited here are careful, well-engineered work. The
premise of this project is not that anyone was careless — it is that no team can read
an entire codebase at the depth every line deserves, and that exhaustive machine-assisted
review is a genuine complement to human testing. Findings go upstream as precise,
verified, patch-ready reports.

## How it works

**1. Survey.** Harvest five years of research articles from six high-impact journals
(*Nature*, *Science*, PNAS, *NEJM*, *The Lancet*, *Cell*) via the Europe PMC API, parse
every openly readable full text, and extract which open-source packages each paper used,
with a quotable evidence sentence and version where stated. Papers that could not be
read are listed individually rather than silently dropped.

**2. Target.** For a package under audit, re-mine the papers that used it to determine
*which parts* they ran — commands, options, versions — so review effort lands on the
code paths that carry published numbers.

**3. Audit and verify.** Read those components adversarially, then verify: compile the
routine under test verbatim against high-precision arithmetic, port it faithfully to
Python and test against ground truth, or simulate the full pipeline. Only then does a
finding get written up, with file:line evidence, a runnable harness, and a patch where
the fix is crisp.

What *held up* under the same scrutiny is recorded alongside what didn't, so findings
are read in proportion.

## Status

| Audit | Papers exposed | Findings | Upstream |
|---|---|---|---|
| [FreeSurfer](audits/freesurfer/) | 116 | 16, three reproduced numerically | 5 fix PRs + 9 issues filed on GitHub |
| [FSL](audits/fsl/) | 114 | 12, six with patches | reports and patches ready; filing via the FSL mailing list |
| [SPM](audits/spm/) | full-codebase audit (not survey-driven) | 83 confirmed + ~38 plausible; one fix regression-tested by executing the code | 2 issue+PR pairs filed on GitHub (open); 3 more staged with filing kit ready |
| [AFNI](audits/afni/) | 39 in the survey cohort; 57 adjudicated for the ReHo finding | 36 (9 high-impact, 15 narrower, 12 likely), one reproduced numerically | 1 fix PR merged upstream; 10 more written up |
| [DESeq2](audits/deseq2/) | 886 | 3 confirmed (one live 2017–2025, already fixed upstream but unannounced), 3 verified-negligible | erratum/NEWS request + docs note to file on GitHub |
| [MACS2](audits/macs2/) | 475 | 3 confirmed (one live in current MACS3, reproduced on shipped binary), 4 notes, 2 withdrawn by own review | one-word fix PR + issues to file on GitHub |

The survey itself covers **44,198 research articles**, of which **20,501** were openly
readable; **10,364** name at least one open-source package, across **270 distinct
packages**. Coverage is very uneven by journal (PNAS 78%, *Science* 5%) — see
[`survey/README.md`](survey/README.md) for the caveats that come with that, which matter
for any count in this repository.

## Layout

```
survey/
  README.md      the survey document: headline numbers, per-journal coverage,
                 most-used packages, and the caveats
  data/          papers.tsv, paper_software.tsv (36,424 usage records),
                 package_index.tsv, gap_list.tsv (23,697 unreadable papers),
                 pipelines.jsonl.gz
  packages/      one page per detected package (270), with evidence sentences
  scripts/       harvest + extraction pipeline (reproducible end to end)

audits/
  freesurfer/    component reviews, paper→feature exposure, numerical
                 reproductions, and the upstream filing kit
  fsl/           component reviews and paper→feature exposure
                 (reports, patches and harnesses: separate repo, below)
  spm/           eleven component reviews spanning the whole codebase,
                 verification harnesses incl. an Octave old-vs-new
                 regression, and the upstream filing kit
  afni/          nine subsystem reviews, paper→feature exposure, the ReHo
                 tie-handling reproduction, and the upstream filing queue
```

## Related repositories

- **[fsl-bug-reports](https://github.com/cindykrafft/fsl-bug-reports)** — the FSL
  findings as ready-to-send reports, `git format-patch` fixes, and verification
  harnesses. Kept separate because FSL takes reports on its mailing list, and those
  posts link to it directly.
- **[cindykrafft/freesurfer](https://github.com/cindykrafft/freesurfer)** — fork
  carrying the five FreeSurfer fix branches submitted upstream.
- **[cindykrafft/spm](https://github.com/cindykrafft/spm)** — fork carrying the five
  SPM fix branches plus a new `tests/test_spm_ECdensity.m` (not yet filed upstream).

## Reading these findings fairly

- A finding is **code-level** unless it says otherwise. "CONFIRMED" means the defect was
  traced end to end in the source and, where stated, verified numerically — not that
  anyone has run the shipped binary on imaging data and watched it happen.
- **"Paper is exposed" means the paper used the affected feature or version.** It does
  not mean its conclusions are wrong. Most of these biases are systematic and shared
  across subjects, which is exactly why they usually shift or attenuate measurements
  rather than reverse well-powered contrasts.
- Reproduction sometimes *shrinks* a finding, and that is recorded too — one FreeSurfer
  finding turned out not to fire on the standard pipeline at all once measured, and a
  faithful port of AFNI's ReHo tie loop moved one published paper back out of the
  exposed set.
- Nothing here has been adjudicated by the upstream maintainers yet. Their reading wins.

## Reproducing the survey

`survey/scripts/` runs the whole pipeline against the public Europe PMC API — metadata
harvest by ISSN, full-text fetch, then extraction. It needs no credentials. Expect the
fetch stage to take many hours and to hit articles that are marked open access but serve
no XML; those are routed to the gap list rather than retried indefinitely.

## License

Scripts are MIT (see `LICENSE`). The prose, tables and derived data are CC BY 4.0.
Evidence sentences are short quotations from the source articles, each attributed by PMID
and DOI; the underlying articles remain under their own licenses. No third-party source
code is redistributed here — patches and harnesses only.
