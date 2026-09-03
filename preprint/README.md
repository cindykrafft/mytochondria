# Preprint

`main.tex` + `figures/` is the arXiv source of *Exhaustive AI-assisted auditing of
research software: a survey-driven method, nine packages, and the reanalysis of a
thirteen-year-old defect in AFNI's regional homogeneity*; `preprint.pdf` is the
compiled draft. Build with `pdflatex main.tex` twice (bibliography is inline).

Figures are generated from `audits/afni/reanalysis/results/` by
`audits/afni/reanalysis/analogue_cattarinussi2024/make_figure1_cat.py`, `make_mechanism_figure_cat.py` and `make_amplitude_figure.py`
(inputs exported to `fig_inputs/` from the results in
`analogue_cattarinussi2024/results/`).
