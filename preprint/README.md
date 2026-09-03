# Preprint

`main.tex` + `figures/` is the arXiv source of *Exhaustive AI-assisted auditing of
research software: a survey-driven method, nine packages, and the reanalysis of a
thirteen-year-old defect in AFNI's regional homogeneity*; `preprint.pdf` is the
compiled draft. Build with `pdflatex main.tex` twice (bibliography is inline).

Figures are generated from `audits/afni/reanalysis/results/` by
`audits/afni/reanalysis/scripts/make_figure1_ext.py` and `make_mechanism_figure_ext.py`
(inputs exported to `scripts/fig_inputs/` from the 73-participant results in
`results/enlarged_sample/`).
