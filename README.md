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

**4. File upstream, on the project's terms.** Before anything is sent, read the
project's `CONTRIBUTING.md`, any pinned policy issue, the NEWS/changelog, and the
existing issue and PR history for the component. A finding that upstream has already
fixed and announced is not a finding to file. Non-minor changes, and anything that
changes numerical output, go to the project's preferred discussion venue first
(for Bioconductor packages that is the support site, not a cold PR). Each filing kit
records which documents were read and where the ask is being made. This step was
added after the DESeq2 round, where the audit filed four items without reading the
project's pinned policy or CONTRIBUTING.md, claimed a NEWS entry was missing when it
was not, and had all four closed by the maintainer within two hours.

What *held up* under the same scrutiny is recorded alongside what didn't, so findings
are read in proportion.

## Status

| Audit | Papers exposed | Findings | Upstream |
|---|---|---|---|
| [FreeSurfer](audits/freesurfer/) | 116 | 16, three reproduced numerically | 5 fix PRs + 9 issues filed on GitHub |
| [FSL](audits/fsl/) | 114 | 12, six with patches | reports and patches ready; filing via the FSL mailing list |
| [SPM](audits/spm/) | full-codebase audit (not survey-driven) | 83 confirmed + ~38 plausible; three verified by executing the code (one unit-tested, two reproduced on SPM's tutorial data) | 2 fix PRs merged upstream (M/EEG artefact-window baseline; downsample sampling rate); 3 issue+PR pairs open (χ² EC densities with new unit test; DCM free energy; parametric-modulation padding, filed 2026-09-02) |
| [AFNI](audits/afni/) | 39 in the survey cohort; 57 adjudicated for the ReHo finding | 36 (9 high-impact, 15 narrower, 12 likely), one reproduced numerically | 12 PRs + 14 issues filed on GitHub: 4 PRs merged (ReHo tie handling, NIfTI slice timing, two test-suite repairs), 8 open. [Reanalysis](audits/afni/reanalysis/) of the published ReHo design on open data (ds000030, 40 subjects): the pre-fix build returns NaN in 17 % of brain voxels and a third of the correct value elsewhere, and the SCZ-vs-control p < .001 maps from the two builds do not overlap |
| [DESeq2](audits/deseq2/) | 886 | 3 confirmed (one live 2017–2025, fixed upstream in 1.49.4 with a NEWS entry), 3 verified-negligible | 3 issues + 1 PR filed on GitHub 2026-09-01; all four closed by the maintainer the same day (the two NEWS requests were already met, the PR was declined under the project's results-stability policy). The filing skipped DESeq2's contribution guidelines and misread its NEWS; see the [filing kit](audits/deseq2/upstream/) for the correction |
| [MACS2](audits/macs2/) | 475 | 3 confirmed (one live in current MACS3, reproduced on shipped binary), 4 notes, 2 withdrawn by own review | not yet filed. MACS has a CONTRIBUTING.md with a PR template and a Slack channel; read both before filing (step 4 above) |
| [Kilosort](audits/kilosort/) | 60 | 3 new verified on shipped code (one disables KS4's refractory split veto since v4.1.5), 5 by code reading, plus exposure map for the known 2024 "spike holes" bug | 2 fix PRs + 3 issues filed on GitHub 2026-09-01 (#1043–#1047), all open, no maintainer response yet |
| [FieldTrip](audits/fieldtrip/) | 42 | 4 verified by executing FieldTrip's own code under Octave (permutation p-values exclude ties, p = 0 with exhaustive permutations; correlationT df; PSI edge bins −Inf; a statfun branch that cannot run) + 1 by code reading | 5 fix PRs + 2 issues filed on GitHub 2026-09-01/02 (#2607–#2613), all open; the two behavior-changing PRs carry new `test_pullNNNN.m` scripts as the project's bot requested |
| [Suite2p](audits/suite2p/) | 32 | 2 verified on the shipped 1.1.0 wheel (bidirectional-phase correction corrupts odd scan lines since v1.0; classifier bins values at the training minimum into the top bin) + 1 limit verified, 2 by code reading | 3 fix PRs + 3 issues filed on GitHub 2026-09-02 (#1265–#1270), all open, no maintainer response yet |
| [Seurat](audits/seurat/) | 767 | review 1 (differential expression) done: 1 confirmed undocumented behaviour change (v5 fold-change formula, pseudocount `1/n` per group — 79–88 % of lowest-expressed null genes in small clusters reported above +0.25; p-values unaffected), 5 notes, Wilcoxon/MAST paths held up. Profiling from the survey cache only (Europe PMC unreachable; full-text rerun pending) | filing channel read; upstream issue #9346 already raised the asymmetry and was closed — its reply must be read before filing; nothing filed |
| [Scanpy](audits/scanpy/) | 200 | 2 confirmed on master by executing the shipped code (t-test silently run on exponentiated values when `mean_in_log_space=False`, on main and the 1.13 pre-releases, not in 1.12.4; `score_genes` top expression bin holds 1–12 genes so lists with the most-expressed genes get almost no controls or error, all versions), 3 notes; Wilcoxon/HVG/scale/normalize paths held up | filing channel read; no prior issues for either; [filing kit](audits/scanpy/upstream/) ready; fix branches pushed to the [fork](https://github.com/cindykrafft/scanpy); issues and PRs not yet opened |
| [Cutadapt](audits/cutadapt/) | 331 | 4 confirmed by executing the shipped code on main, 5.2 and older wheels (`-e N` loses one allowed error for adapter lengths 49, 98, … through floating-point rounding of N/len, all versions since 3.0; `--max-ee`/`--max-aer` ignore `--quality-base`, so Phred+64 data are never filtered; the demultiplexing index ranks barcodes by matching bases while `--no-index` ranks by the documented alignment score, since 5.0; the k-mer prefilter added in 4.3 silently drops ~40 % of reads carrying an anchored/non-internal adapter with one inserted base whenever exactly one error is allowed), 4 notes, 4 own suspicions withdrawn; quality trimming, expected errors, filters, pair-filter, interleaved/multi-core and the aligner invariants held up against independent ports on ~100k random cases | filing channel read (CONTRIBUTING, bug-report template, CHANGES.rst convention); no prior issue for any of the four; [filing kit](audits/cutadapt/upstream/) with four `git am`-able patches (fix + tests + changelog, each new test failing on unmodified main) ready; nothing filed yet |
| [IQ-TREE 2](audits/iqtree/) | 258 | 0 wrong numbers on master; 4 notes verified by executing the built binary (parametric aLRT prints the cube of 1 − p; UFBoot's 1-log-likelihood candidate cutoff gives 100 % where the standard bootstrap gives 61 % on a degenerate 4-taxon alignment, not reproduced on 6 taxa; SH-aLRT/UFBoot vary with thread count at fixed seed; rooted trees get `NA`/abort in gCF/sCF), 1 withdrawn; likelihoods, gamma rates, `+I`/`+ASC`, ModelFinder criteria and parameter counts, UFBoot/`--bnni` supports, SH-aLRT, aBayes, gCF/sCF held up on master and v2.4.0; the four notes reproduce on iqtree3 3.1.3 | filing channel read (Issues for bugs, Discussions otherwise; no CONTRIBUTING or templates; development moved to `iqtree/iqtree3`); nothing rises to an Issue; [kit](audits/iqtree/upstream/) holds two manual patches and a Discussion draft, none filed |

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
  SPM fix branches plus a new `tests/test_spm_ECdensity.m` (two merged, two open upstream).
- **[cindykrafft/scanpy](https://github.com/cindykrafft/scanpy)** — fork carrying the two
  Scanpy fix branches (t-test input scale; `score_genes` bins), each with a test and a
  release-note fragment, not yet opened as PRs.

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
- Upstream maintainers' reading wins. Where they have adjudicated, the outcome is
  recorded next to the finding: SPM and AFNI have merged fixes and left others open;
  DESeq2's maintainer closed all four filings, and on the central factual point (whether
  the weights fix had been announced) he was right and this audit was wrong.

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
