# Preprint: SPM

`main.tex` + `figures/` is the arXiv source of *Exhaustive AI-assisted review of
SPM: eighty-three verified defects, five fixes sent upstream, two merged and
measured on open data*; `preprint.pdf` is the compiled draft. Build with
`pdflatex main.tex` twice (bibliography is inline).

It is the SPM companion to `../preprint/` (the AFNI paper), kept separate so each
package's findings can be read on their own terms. Everything it reports is in
`../audits/spm/`: the eleven component reviews, the verification harnesses in
`reproductions/`, the real-data runs of the two merged fixes in
`reproductions/mmn_realdata/`, and the filing kit in `upstream/`.

Unlike the AFNI paper, which describes only fixes the maintainers have merged,
this one describes all five high-priority findings and gives each its upstream
status (two merged, three open as of 3 September 2026). Update Table 1 and the
abstract when the open pull requests are adjudicated.

## Figures

`figures/erpcore.pdf` (Figure 2, four panels) is drawn by `figures/make_figure2.py`
from `../audits/spm/reproductions/erpcore_realdata/results/` (a copy of the
script that lives there): `python3 make_figure2.py <results_dir> erpcore.pdf`,
where the results directory holds the per-participant TSVs and
`grand_averages.npz` written by `analyze.py`.

`figures/findings.pdf` (Figure 1, four panels) is drawn by `figures/make_figure1.py`:

```
python3 make_figure1.py <scratch_dir> findings.pdf
```

where `<scratch_dir>/mmn/` holds `sp3_prefix.mat` and `sp3_merged.mat` (the
global-field-power outputs of `../audits/spm/reproductions/mmn_realdata/sp3_pipeline.m`
run with `badsamples.m` before and after PR 163) and SPM's tutorial recording
`subject1.bdf`. Panel A is the closed-form ratio of the shipped to the correct
chi-squared EC density; panels B and C come from the Octave run of the real SPM
code; panel D decimates the recording with MNE-Python/SciPy, the same arithmetic
as `sp4_demo.py`. Needs numpy, scipy, matplotlib and mne.
