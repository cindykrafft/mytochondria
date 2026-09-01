# rstanarm

- **Category:** general
- **Papers in survey:** 5
- **Journals:** PNAS (4), Science (1)
- **Years:** 2021 (2), 2022 (2), 2024 (1)
- **Versions named:** 2.21.1 (1)
- **Pipeline stages it appears in:** differential/statistical testing (2)

## Papers

### Neural circuit mechanisms of sensorimotor disability in cancer treatment. (PNAS 2021)

- DOI: 10.1073/pnas.2100428118 | PMCID: PMC8713769 | PMID: 34911753
- Evidence: All models were developed with the rstanarm package (version 2.18.1) ( 63 ) in R (version 3.5.0) ( 61 ).
- Full pipeline: machine learning [DeepLabCut v2.1.5.2] -> stage not stated [R v3.5.0, rstanarm]

### Noninvasive detection of any-stage cancer using free glycosaminoglycans. (PNAS 2022)

- DOI: 10.1073/pnas.2115328119 | PMCID: PMC9897435 | PMID: 36469776
- Evidence: We fit the models using rstanarm package (2.21.1) with four chains for a total of 4,000 iterations (2,000 warm-up).
- Full pipeline: differential/statistical testing [R v4.0.4, brms v2.14.4] -> stage not stated [rstanarm]

### Female reproductive aging in seven primate species: Patterns and consequences. (PNAS 2022)

- DOI: 10.1073/pnas.2117669119 | PMCID: PMC9171789 | PMID: 35533284
- Evidence: We used the R statistical computing environment for all analyses ( 77 ), and we fit all models using the survival analysis development branch of the R package rstanarm found in ref.
- Full pipeline: differential/statistical testing [R, rstanarm]

### Water quality-fisheries tradeoffs in a changing climate underscore the need for adaptive ecosystem-based management. (PNAS 2024)

- DOI: 10.1073/pnas.2322595121 | PMCID: PMC11551330 | PMID: 39467116
- Evidence: We developed a Bayesian multiple linear regression model using the rstanarm package ( 165 ) in R ( 166 ) with Stan ( 167 ) to predict hypoxic area from the cumulative TP load and the spring air temperature ( SI Appendix ).
- Full pipeline: differential/statistical testing [R, Stan, rstanarm]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **2.21.1**
- Evidence: Analyses in R (4.0.2) ( 60 ) were conducted using the following main packages: brms (2.13.9) ( 58 , 59 ), rstanarm (2.21.1) ( 91 ), rstan (2.21.2) ( 92 ), data.table (1.13.3) ( 93 ), and ggplot2 (3.3.2) ( 94 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

